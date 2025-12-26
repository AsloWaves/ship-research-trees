---
tags: [script, submarines, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Submarines.Controllers
file-path: Assets/Scripts/Submarines/Controllers/SonarSystem.cs
status: IMPLEMENTED
size: ~573 lines
feature-group: submarines
---

# SonarSystem.cs

## Quick Reference
**Type**: NetworkBehaviour (per-submarine)
**Namespace**: WOS.Submarines.Controllers
**File**: `Assets/Scripts/Submarines/Controllers/SonarSystem.cs`
**Size**: ~573 lines
**Dependencies**: SubmarineData, SubmarineController, Mirror

---

## Purpose
Server-authoritative sonar detection and tracking system. Handles passive listening, active pings, contact classification, target tracking, and firing solution generation. Based on GDD Submarine-Warfare.md specifications.

---

## Configuration

```csharp
[Header("Sonar Configuration")]
[SerializeField] private SonarConfig sonarConfig;

[Header("Detection Settings")]
[SerializeField] private float passiveScanInterval = 2f;
[SerializeField] private float contactLostTimeout = 60f;
[SerializeField] private int maxTrackedContacts = 20;

[Header("Environment")]
[SerializeField] private float thermoclineDepth = 50f;
[SerializeField] private float seaStateNoise = 10f;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
private readonly SyncList<SonarContact> syncedContacts = new SyncList<SonarContact>();

[SyncVar] private bool isActiveMode = false;
[SyncVar] private float lastPingTime;
```

---

## Events

```csharp
public event Action<SonarContact> OnNewContact;
public event Action<SonarContact> OnContactUpdated;
public event Action<string> OnContactLost;
public event Action OnActivePing;
public event Action<string, float> OnTorpedoDetected;  // contactId, range
```

---

## Passive Sonar

```csharp
[Server]
private void UpdatePassiveSonar(float deltaTime)
{
    passiveScanTimer += deltaTime;
    if (passiveScanTimer < passiveScanInterval) return;
    passiveScanTimer = 0f;

    var potentialTargets = FindPotentialTargets();
    foreach (var target in potentialTargets)
    {
        ProcessPotentialContact(target, isActivePing: false);
    }
}
```

### Passive Sonar Characteristics

| Feature | Value |
|---------|-------|
| Range | 5000m |
| Bearing Accuracy | 5 degrees |
| Update Rate | 2 seconds |
| Range Accuracy | 30% error |

---

## Active Sonar

```csharp
[Command]
public void CmdActivePing()
{
    if (Time.time - lastPingTime < sonarConfig.activePingCooldown) return;

    lastPingTime = Time.time;
    isActiveMode = true;

    var potentialTargets = FindPotentialTargets();
    foreach (var target in potentialTargets)
    {
        ProcessPotentialContact(target, isActivePing: true);
    }

    // IMPORTANT: Active ping reveals position
    BroadcastPingDetection();

    OnActivePing?.Invoke();
    RpcNotifyActivePing();
}
```

### Active Sonar Characteristics

| Feature | Value |
|---------|-------|
| Range | 15000m |
| Bearing Accuracy | 1 degree |
| Range Accuracy | 50m |
| Cooldown | 30 seconds |
| Detection Range | 20000m (others hear ping) |

---

## Detection Calculation

```csharp
[Server]
private float CalculateDetectionChance(DetectableTarget target, float range, bool isActivePing)
{
    float baseChance = 1f;

    // Range falloff
    float maxRange = isActivePing ? sonarConfig.activeRange : sonarConfig.passiveRange;
    baseChance *= 1f - (range / maxRange);

    // Target noise level
    float noiseRatio = target.noiseLevel / sonarConfig.noiseFloorThreshold;
    baseChance *= Mathf.Clamp01(noiseRatio);

    // Thermocline effect (30% detection loss through layer)
    bool targetBelowThermocline = target.depth > thermoclineDepth;
    bool weBelowThermocline = ourDepth > thermoclineDepth;
    if (targetBelowThermocline != weBelowThermocline)
    {
        baseChance *= (1f - sonarConfig.depthLayerPenalty);
    }

    // Sea state reduces passive detection
    if (!isActivePing)
    {
        baseChance *= (1f - seaStateNoise / 50f);
    }

    // Active ping more reliable
    if (isActivePing)
    {
        baseChance *= 1.5f;
    }

    return Mathf.Clamp01(baseChance);
}
```

---

## Contact Management

### New Contact

```csharp
[Server]
private void CreateNewContact(DetectableTarget target, float range, bool isActivePing)
{
    var contact = new SonarContact
    {
        contactId = Guid.NewGuid().ToString(),
        targetNetId = target.id,
        classification = ClassifyTarget(target),
        confidence = isActivePing ? 0.8f : 0.5f,
        bearing = CalculateBearing(target.position),
        estimatedRange = isActivePing ? range : EstimatePassiveRange(range),
        estimatedDepth = target.depth,
        estimatedSpeed = target.speed,
        estimatedCourse = target.heading,
        isClosing = Vector3.Dot(target.velocity, transform.position - target.position) > 0,
        trackNumber = nextTrackNumber++
    };

    trackedContacts[target.id] = contact;
    syncedContacts.Add(contact);

    OnNewContact?.Invoke(contact);

    // Special torpedo alert
    if (contact.classification == ContactClassification.Torpedo)
    {
        OnTorpedoDetected?.Invoke(contact.contactId, contact.estimatedRange);
        RpcNotifyTorpedoIncoming(contact.bearing, contact.estimatedRange);
    }
}
```

### Contact Tracking

```csharp
[Server]
private void UpdateContactTracking(float deltaTime)
{
    foreach (var contact in trackedContacts.Values)
    {
        float timeSinceUpdate = Time.time - contact.lastUpdateTime;

        // Mark as lost contact after 50% timeout
        if (timeSinceUpdate > contactLostTimeout * 0.5f)
        {
            contact.isLostContact = true;
            contact.confidence *= 0.5f;
        }

        // Remove after full timeout
        if (timeSinceUpdate > contactLostTimeout)
        {
            OnContactLost?.Invoke(contact.contactId);
            trackedContacts.Remove(contact.contactId);
        }
    }
}
```

---

## Firing Solutions

```csharp
public FiringSolution GenerateFiringSolution(string contactId, float torpedoSpeed)
{
    var contact = trackedContacts[contactId];

    var solution = new FiringSolution
    {
        targetId = contactId,
        targetPosition = contact.lastKnownPosition,
        targetBearing = contact.bearing,
        targetRange = contact.estimatedRange,
        targetSpeed = contact.estimatedSpeed,
        targetCourse = contact.estimatedCourse,
        targetDepth = contact.estimatedDepth
    };

    // Calculate intercept point
    float timeToTarget = contact.estimatedRange / torpedoSpeed;
    Vector3 interceptPoint = contact.lastKnownPosition + targetVelocity * timeToTarget;

    solution.interceptBearing = CalculateBearing(interceptPoint);
    solution.interceptRange = Vector3.Distance(transform.position, interceptPoint);
    solution.runTime = solution.interceptRange / torpedoSpeed;

    solution.hitProbability = CalculateHitProbability(contact, solution);
    solution.isValidSolution = solution.hitProbability > 0.1f;

    return solution;
}
```

### Hit Probability Factors

| Factor | Effect |
|--------|--------|
| Contact confidence | Multiplier |
| Range | Decreases with distance |
| Target speed | Faster = harder |
| Active sonar data | +30% bonus |

---

## Public API

```csharp
public List<SonarContact> GetAllContacts();
public SonarContact GetContact(string contactId);
public bool IsActiveMode { get; }
public float GetPingCooldownRemaining();
```

---

## Client RPCs

```csharp
[ClientRpc] private void RpcNotifyActivePing();
[ClientRpc] private void RpcNotifyNewContact(int trackNumber, ContactClassification classification, float bearing);
[ClientRpc] private void RpcNotifyContactLost(int trackNumber);
[ClientRpc] private void RpcNotifyTorpedoIncoming(float bearing, float range);
```

---

## Integration Points

### Dependencies
- [[SubmarineData]] - Contact and sonar data
- [[SubmarineController]] - Current depth for thermocline
- Mirror networking

### Used By
- [[SubmarineController]] - Torpedo firing
- Sonar display UI
- Torpedo guidance systems

---

## Related Files
- [[SubmarineData]] - Data structures
- [[SubmarineController]] - Submarine mechanics
- [[TorpedoController]] - Torpedo launching

---

## Design Notes
- Server-authoritative with SyncList for contacts
- Passive sonar: silent but less accurate
- Active sonar: accurate but reveals position
- Thermocline at 50m reduces cross-layer detection 30%
- Contacts tracked up to 60 seconds without update
- Maximum 20 tracked contacts
- Firing solutions calculate lead intercept
- Torpedo detection triggers special alert
- Track numbers assigned sequentially

