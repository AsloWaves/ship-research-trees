---
tags: [script, damage, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Damage.Controllers
file-path: Assets/Scripts/Damage/Controllers/DamageController.cs
status: IMPLEMENTED
size: ~810 lines
feature-group: damage
---

# DamageController.cs

## Quick Reference
**Type**: NetworkBehaviour (per-ship)
**Namespace**: WOS.Damage.Controllers
**File**: `Assets/Scripts/Damage/Controllers/DamageController.cs`
**Size**: ~810 lines
**Dependencies**: DamageData, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative damage controller for individual ships. Manages health, compartments, fire, flooding, critical hits, sinking, and destruction. Based on GDD damage model specifications.

---

## Configuration

```csharp
[Header("Configuration")]
[SerializeField] private ShipDamageConfigSO damageConfig;

[Header("Health")]
[SerializeField] private float baseMaxHealth = 10000f;
[SerializeField] private float beltArmor = 100f;
[SerializeField] private float deckArmor = 50f;

[Header("Compartments")]
[SerializeField] private List<CompartmentDefinition> compartmentDefinitions;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
[SerializeField] private bool invulnerable = false;
```

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnHealthChanged))]
private float currentHealth;

[SyncVar] private ShipDamageState damageState = ShipDamageState.Operational;
[SyncVar] private int activeFireCount;
[SyncVar] private int floodedCompartments;
[SyncVar] private float listAngle;
```

---

## Events

```csharp
public event Action<float, float> OnHealthUpdated;              // current, max
public event Action<DamageEvent> OnDamageTaken;
public event Action<ShipDamageState> OnDamageStateChanged;
public event Action<string, FireSeverity> OnFireStarted;
public event Action<string> OnFireExtinguished;
public event Action<string, FloodSeverity> OnFloodingStarted;
public event Action<string> OnFloodingStopped;
public event Action<CriticalDamage> OnCriticalHit;
public event Action OnShipDestroyed;
public event Action OnShipSinking;
```

---

## Damage Application

### ApplyDamage

```csharp
[Server]
public void ApplyDamage(DamageEvent damageEvent)
{
    if (invulnerable || damageState == ShipDamageState.Destroyed) return;

    // Calculate final damage after armor
    float finalDamage = CalculateFinalDamage(damageEvent);
    damageEvent.actualDamage = finalDamage;

    // Apply to health
    healthState.ApplyDamage(finalDamage);
    currentHealth = healthState.currentHealth;

    // Apply to compartment
    if (!string.IsNullOrEmpty(damageEvent.compartmentHit))
    {
        ApplyCompartmentDamage(damageEvent);
    }

    // Handle secondary effects
    if (damageEvent.causedFire) StartFire(compartmentId, severity);
    if (damageEvent.causedFlooding) StartFlooding(compartmentId, severity);
    if (damageEvent.causedCritical) ApplyCriticalDamage(damageEvent);

    // Check for destruction
    if (healthState.damageState == ShipDamageState.Destroyed)
    {
        HandleDestruction(damageEvent.sourceShipNetId);
    }
}
```

### Damage Calculation

```csharp
private float CalculateFinalDamage(DamageEvent damageEvent)
{
    float damage = damageEvent.rawDamage;

    // Armor reduction for penetrating hits
    if (damageEvent.damageType == DamageType.Penetrating)
    {
        float armorRatio = healthState.beltArmor / damageEvent.armorPenetrated;
        if (armorRatio > 1f)
        {
            damage *= 0.1f;     // Armor not penetrated
        }
        else
        {
            damage *= (1f - (armorRatio * 0.5f));   // Penetrated
        }
    }

    // Splash damage reduction
    if (damageEvent.damageType == DamageType.Splash)
    {
        damage *= 0.5f;
    }

    return damage;
}
```

---

## Fire System

### Fire Damage Per Second

| Severity | DPS |
|----------|-----|
| Minor | 5 |
| Moderate | 15 |
| Major | 30 |
| Catastrophic | 60 |

```csharp
[Server]
public void StartFire(string compartmentId, FireSeverity severity)
{
    var compartment = GetCompartment(compartmentId);
    if (compartment.fireSeverity >= severity) return;

    compartment.StartFire(severity);
    activeFireCount++;

    OnFireStarted?.Invoke(compartmentId, severity);
    RpcOnFireStarted(compartmentId, (int)severity);
}

[Server]
private void UpdateFires(float deltaTime)
{
    foreach (var compartment in compartments)
    {
        if (compartment.fireSeverity == FireSeverity.None) continue;

        // Fire damage over time
        float fireDamage = GetFireDamagePerSecond(compartment.fireSeverity) * deltaTime;
        healthState.ApplyDamage(fireDamage);

        // Fire grows if uncontrolled
        if (!compartment.isBeingFought)
        {
            compartment.fireIntensity += deltaTime * 0.05f;
        }

        // Major fires can spread
        if (compartment.fireSeverity >= FireSeverity.Major)
        {
            TrySpreadFire(compartment);
        }

        // Magazine detonation check
        if (compartment.type == CompartmentType.Magazine &&
            compartment.fireSeverity == FireSeverity.Catastrophic)
        {
            HandleMagazineDetonation();
        }
    }
}
```

---

## Flooding System

### Flood Rates Per Second

| Severity | Rate/sec |
|----------|----------|
| Minor | 2% |
| Moderate | 5% |
| Major | 10% |
| Critical | 20% |

```csharp
[Server]
public void StartFlooding(string compartmentId, FloodSeverity severity)
{
    var compartment = GetCompartment(compartmentId);
    if (compartment.floodSeverity >= severity) return;

    compartment.StartFlooding(severity, GetFloodRate(severity));
    floodedCompartments++;

    OnFloodingStarted?.Invoke(compartmentId, severity);
}

[Server]
private void UpdateFlooding(float deltaTime)
{
    float totalFloodLevel = 0f;

    foreach (var compartment in compartments)
    {
        if (compartment.floodSeverity == FloodSeverity.None) continue;

        compartment.floodLevel += compartment.floodRate * deltaTime;
        compartment.floodLevel = Mathf.Clamp01(compartment.floodLevel);
        totalFloodLevel += compartment.floodLevel;

        // Flooding puts out fires
        if (compartment.floodLevel > 0.5f)
        {
            ExtinguishFire(compartment.compartmentId);
        }
    }

    // Calculate list (tilt) from asymmetric flooding
    listAngle = CalculateListAngle();

    // Check for capsizing
    if (Mathf.Abs(listAngle) > 45f || totalFloodLevel > compartments.Count * 0.6f)
    {
        StartSinking();
    }
}
```

---

## Sinking & Destruction

```csharp
private void StartSinking()
{
    if (damageState == ShipDamageState.Sinking) return;

    damageState = ShipDamageState.Sinking;
    healthState.sinkingRate = 0.5f; // meters per second

    OnShipSinking?.Invoke();
    RpcOnShipSinking();
}

private void HandleDestruction(uint killerNetId)
{
    damageState = ShipDamageState.Destroyed;

    OnShipDestroyed?.Invoke();
    RpcOnShipDestroyed(killerNetId);

    // TODO: Trigger permadeath/extraction logic
    // TODO: Award kill credit
}

private void HandleMagazineDetonation()
{
    // Instant destruction
    healthState.ApplyDamage(healthState.maxHealth * 2f);
    HandleDestruction(0);
}
```

---

## Critical Damage

```csharp
private void ApplyCriticalDamage(DamageEvent damageEvent)
{
    var compartment = GetCompartment(damageEvent.compartmentHit);
    CriticalType critType = GetCriticalType(compartment.type);

    var critical = new CriticalDamage
    {
        type = critType,
        severity = damageEvent.rawDamage / 5000f,
        effectModifier = 0.5f,
        canBeRepaired = true
    };

    ApplyCriticalEffects(critical);
    OnCriticalHit?.Invoke(critical);
}
```

### Critical Effects

| Critical Type | Effect |
|---------------|--------|
| EngineRoom | Speed *= penalty |
| Rudder | Turn *= penalty |
| FireControl | Accuracy *= penalty |
| Bridge | All stats *= penalty |
| Magazine | 30% detonation chance |

---

## Vital Compartment Destruction

```csharp
private void HandleVitalCompartmentDestruction(CompartmentState compartment)
{
    switch (compartment.type)
    {
        case CompartmentType.Bridge:
            healthState.accuracyModifier *= 0.5f;
            healthState.turnModifier *= 0.7f;
            break;

        case CompartmentType.EngineRoom:
            healthState.speedModifier *= 0.3f;
            break;

        case CompartmentType.Rudder:
            healthState.turnModifier *= 0.1f;
            break;

        case CompartmentType.Magazine:
            if (UnityEngine.Random.value < 0.3f)
            {
                HandleMagazineDetonation();
            }
            break;
    }
}
```

---

## Public API

```csharp
public float GetCurrentHealth();
public float GetMaxHealth();
public float GetHealthPercent();
public ShipDamageState GetDamageState();
public int GetActiveFireCount();
public int GetFloodedCompartmentCount();
public float GetListAngle();
public ShipHealthState GetHealthState();
public List<CompartmentState> GetCompartments();

public float GetSpeedModifier();
public float GetTurnModifier();
public float GetAccuracyModifier();
```

---

## Compartment Definition

```csharp
[Serializable]
public class CompartmentDefinition
{
    public string id;
    public CompartmentType type;
    public bool isVital;
    public Vector3 localPosition;
    public bool isBelowWaterline;
    public float maxHealth = 1000f;
    public float armorThickness = 50f;
    public bool canBeSealed = true;
}
```

---

## Client RPCs

```csharp
[ClientRpc] private void RpcOnDamageTaken(Vector3 hitPoint, float damage);
[ClientRpc] private void RpcOnFireStarted(string compartmentId, int severity);
[ClientRpc] private void RpcOnFireExtinguished(string compartmentId);
[ClientRpc] private void RpcOnFloodingStarted(string compartmentId, int severity);
[ClientRpc] private void RpcOnShipSinking();
[ClientRpc] private void RpcOnShipDestroyed(uint killerNetId);
```

---

## Integration Points

### Dependencies
- [[DamageData]] - Data structures and enums
- Mirror networking
- WOS.Debugging

### Used By
- [[DamageControlTeam]] - Fire/flooding repair
- [[ProjectileManager]] - Damage delivery
- [[WeaponController]] - Hit registration
- [[PermadeathManager]] - Death processing

---

## Related Files
- [[DamageData]] - Data structures
- [[DamageControlTeam]] - Damage control operations
- [[CrewManager]] - Casualty integration

---

## Design Notes
- Server-authoritative with SyncVar synchronization
- Per-compartment damage tracking
- Fire spreads if uncontrolled, extinguished by flooding
- Asymmetric flooding causes list (ship tilt)
- 45 degree list or 60% total flooding triggers sinking
- Magazine fires risk catastrophic detonation
- Critical damage applies lasting stat penalties
- Invulnerable mode for testing

