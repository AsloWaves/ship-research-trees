---
tags: [script, submarines, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Submarines.Controllers
file-path: Assets/Scripts/Submarines/Controllers/SubmarineController.cs
status: IMPLEMENTED
size: ~588 lines
feature-group: submarines
---

# SubmarineController.cs

## Quick Reference
**Type**: NetworkBehaviour (per-submarine)
**Namespace**: WOS.Submarines.Controllers
**File**: `Assets/Scripts/Submarines/Controllers/SubmarineController.cs`
**Size**: ~588 lines
**Dependencies**: SubmarineData, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative submarine mechanics controller. Handles depth control, power management (battery/diesel), atmosphere (oxygen/CO2), stealth (noise), and torpedo tube operations. Based on GDD Submarine-Warfare.md specifications.

---

## Configuration

```csharp
[Header("Submarine Configuration")]
[SerializeField] private SubmarineStats stats;

[Header("Torpedo Tubes")]
[SerializeField] private List<TorpedoTube> torpedoTubes;
[SerializeField] private int maxTorpedoStorage = 12;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnDepthChanged))]
private float currentDepth;

[SyncVar(hook = nameof(OnModeChanged))]
private SubmarineMode operatingMode;

[SyncVar] private float batteryCharge = 100f;
[SyncVar] private float oxygenLevel = 100f;
[SyncVar] private float noiseLevel;
[SyncVar] private DepthState depthState = DepthState.Surfaced;
```

---

## Events

```csharp
public event Action<float> OnDepthUpdate;
public event Action<SubmarineMode> OnModeUpdate;
public event Action<DepthState> OnDepthStateChanged;
public event Action OnEmergencySurface;
public event Action<float> OnCrushDepthWarning;
public event Action OnBatteryLow;
public event Action OnOxygenLow;
```

---

## Depth Control

### Set Target Depth

```csharp
[Command]
public void CmdSetTargetDepth(float depth)
{
    depth = Mathf.Clamp(depth, 0f, stats.crushDepth);
    targetDepth = depth;
}
```

### Emergency Blow

```csharp
[Command]
public void CmdEmergencyBlow()
{
    operatingMode = SubmarineMode.Emergency;
    targetDepth = 0f;
    submarineState.ballastLevel = 0f;

    OnEmergencySurface?.Invoke();
    RpcNotifyEmergencyBlow();
}
```

### Depth Update

```csharp
[Server]
private void UpdateDepthControl(float deltaTime)
{
    float rate = operatingMode == SubmarineMode.Emergency
        ? stats.surfaceRate * 2f
        : (targetDepth > currentDepth ? stats.diveRate : stats.surfaceRate);

    currentDepth = Mathf.MoveTowards(currentDepth, targetDepth, rate * deltaTime);
    UpdateDepthState();
}
```

### Depth State Thresholds

| Depth | State |
|-------|-------|
| <1m | Surfaced |
| 1-20m | PeriscopeDepth |
| 20-50m | ShallowDepth |
| 50-testDepth | OperatingDepth |
| testDepth-crushDepth | DeepDepth |
| >crushDepth | CrushDepth |

---

## Power Systems

### Set Operating Mode

```csharp
[Command]
public void CmdSetOperatingMode(SubmarineMode mode)
{
    // Surface mode only on surface
    if (mode == SubmarineMode.Surface && currentDepth > 1f) return;

    // Snorkel only at periscope depth
    if (mode == SubmarineMode.Snorkel && currentDepth > 20f) return;

    operatingMode = mode;
}
```

### Power Consumption

| Mode | Battery Effect |
|------|----------------|
| Surface | Recharge: +5%/min |
| Snorkel | Recharge: +5%/min |
| Electric | Drain: -1x/sec |
| Silent | Drain: -0.3x/sec |
| Emergency | Drain: -2x/sec |

```csharp
[Server]
private void UpdatePowerSystems(float deltaTime)
{
    switch (operatingMode)
    {
        case SubmarineMode.Surface:
        case SubmarineMode.Snorkel:
            batteryCharge += stats.dieselRechargeRate * (deltaTime / 60f);
            break;
        case SubmarineMode.Electric:
            batteryCharge -= stats.electricConsumption * deltaTime;
            break;
        case SubmarineMode.Silent:
            batteryCharge -= stats.electricConsumption * stats.silentModeMultiplier * deltaTime;
            break;
    }

    // Force surface if battery depleted
    if (batteryCharge <= 0f && currentDepth > 0f)
    {
        CmdEmergencyBlow();
    }
}
```

---

## Atmosphere System

```csharp
[Server]
private void UpdateAtmosphere(float deltaTime)
{
    if (depthState == DepthState.Surfaced || operatingMode == SubmarineMode.Snorkel)
    {
        // Fresh air - restore oxygen
        oxygenLevel = Mathf.MoveTowards(oxygenLevel, 100f, 10f * deltaTime);
        submarineState.co2Level = Mathf.MoveTowards(submarineState.co2Level, 0f, 5f * deltaTime);
        return;
    }

    // Consume oxygen while submerged
    int crewCount = 30; // Placeholder
    oxygenLevel -= stats.oxygenConsumption * crewCount * (deltaTime / 60f);
    submarineState.co2Level += stats.co2Production * crewCount * (deltaTime / 60f);

    // CO2 scrubber
    submarineState.co2Level -= stats.scrubberEfficiency * 0.1f * (deltaTime / 60f);

    // Crew damage from low oxygen or high CO2
    if (oxygenLevel < 10f || submarineState.co2Level > 5f)
    {
        // Apply crew damage
    }
}
```

---

## Stealth System

```csharp
[Server]
private void UpdateStealth()
{
    float baseNoise = stats.baseNoiseLevel;

    // Mode modifier
    switch (operatingMode)
    {
        case SubmarineMode.Surface:
            baseNoise *= stats.surfaceNoiseMultiplier;    // 2x louder
            break;
        case SubmarineMode.Silent:
            baseNoise *= stats.silentNoiseMultiplier;     // 0.2x quieter
            break;
    }

    // Speed cavitation
    if (speed > stats.cavitationSpeed)
    {
        baseNoise *= 3f;
        submarineState.isCavitating = true;
    }

    // Depth modifier (deeper = quieter)
    baseNoise *= (1f - (currentDepth / stats.crushDepth) * 0.3f);

    noiseLevel = baseNoise;
}
```

---

## Crush Depth

```csharp
[Server]
private void CheckCrushDepth(float deltaTime)
{
    if (currentDepth < stats.testDepth) return;

    float depthExcess = currentDepth - stats.testDepth;
    float maxExcess = stats.crushDepth - stats.testDepth;
    float damagePercent = depthExcess / maxExcess;

    // Progressive damage beyond test depth
    if (Time.time - lastDepthDamageTime >= 1f)
    {
        float damage = 10f * damagePercent * damagePercent;
        // Apply hull damage
        lastDepthDamageTime = Time.time;

        if (currentDepth >= stats.crushDepth)
        {
            depthState = DepthState.Destroyed;
            // Trigger destruction
        }
    }
}
```

---

## Torpedo Operations

### Load Torpedo

```csharp
[Command]
public void CmdLoadTorpedo(int tubeNumber, string torpedoId)
{
    var tube = torpedoTubes[tubeNumber - 1];
    if (tube.state != TorpedoTubeState.Empty) return;
    if (!storedTorpedoIds.Contains(torpedoId)) return;

    tube.state = TorpedoTubeState.Loading;
    tube.loadedTorpedoId = torpedoId;
    storedTorpedoIds.Remove(torpedoId);

    StartCoroutine(ReloadTube(tube));
}
```

### Fire Torpedo

```csharp
[Command]
public void CmdFireTorpedo(int tubeNumber, FiringSolution solution)
{
    var tube = torpedoTubes[tubeNumber - 1];
    if (tube.state != TorpedoTubeState.Ready) return;
    if (!solution.isValidSolution) return;

    tube.state = TorpedoTubeState.Firing;
    // Spawn torpedo with solution data
    tube.state = TorpedoTubeState.Empty;

    RpcNotifyTorpedoFired(tubeNumber, solution.targetBearing);
}
```

---

## Public API

```csharp
public float GetCurrentDepth();
public DepthState GetDepthState();
public SubmarineMode GetOperatingMode();
public float GetBatteryCharge();
public float GetOxygenLevel();
public float GetNoiseLevel();
public List<TorpedoTube> GetTorpedoTubes();
public int GetStoredTorpedoCount();
```

---

## Client RPCs

```csharp
[ClientRpc] private void RpcNotifyDepthStateChanged(DepthState state);
[ClientRpc] private void RpcNotifyEmergencyBlow();
[ClientRpc] private void RpcNotifyBatteryLow();
[ClientRpc] private void RpcNotifyOxygenLow();
[ClientRpc] private void RpcNotifyTubeReady(int tubeNumber);
[ClientRpc] private void RpcNotifyTorpedoFired(int tubeNumber, float bearing);
```

---

## Integration Points

### Dependencies
- [[SubmarineData]] - Data structures and enums
- Mirror networking
- WOS.Debugging

### Used By
- [[SonarSystem]] - Gets current depth for thermocline
- [[NetworkedNavalController]] - Speed for cavitation check
- UI depth/power displays

---

## Related Files
- [[SubmarineData]] - Data structures
- [[SonarSystem]] - Sonar system
- [[TorpedoController]] - Torpedo management

---

## Design Notes
- Server-authoritative with SyncVar synchronization
- Battery depleted forces emergency surface
- Silent mode reduces noise 80%, battery drain 70%
- Cavitation at high speed increases noise 3x
- Deeper depth reduces noise propagation
- Test depth: warning, crush depth: damage
- Torpedo reload takes ~30 seconds
- Oxygen/CO2 managed with crew count

