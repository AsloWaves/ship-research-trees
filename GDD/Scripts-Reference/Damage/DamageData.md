---
tags: [script, damage, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Damage.Data
file-path: Assets/Scripts/Damage/Data/DamageData.cs
status: IMPLEMENTED
size: ~453 lines
feature-group: damage
---

# DamageData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Damage.Data
**File**: `Assets/Scripts/Damage/Data/DamageData.cs`
**Size**: ~453 lines
**Dependencies**: None (standalone data)

---

## Purpose
Core damage system data structures. Includes damage types, compartment states, fire/flooding severity, critical damage, and damage calculation parameters. Based on GDD damage model specifications.

---

## Damage Enums

### DamageType (7 types)

```csharp
public enum DamageType
{
    Penetrating,    // AP shell that penetrated armor
    Explosive,      // HE shell, torpedo, or bomb
    Splash,         // Area damage from nearby explosion
    Fire,           // Damage over time from fire
    Flooding,       // Damage from flooding
    Collision,      // Ramming or grounding
    CriticalHit     // Direct hit to vital component
}
```

### CompartmentType (13 types)

```csharp
public enum CompartmentType
{
    // Hull sections
    BowSection, MidSection, SternSection,

    // Vital compartments
    Bridge, EngineRoom, Magazine, FuelTank, Rudder,

    // Specialized
    TorpedoRoom, FireControlCenter, RadioRoom, CrewQuarters, Deck
}
```

### FireSeverity (5 levels)

| Level | Description | Damage/sec |
|-------|-------------|------------|
| None | No fire | 0 |
| Minor | Small fire | 5 |
| Moderate | Medium fire | 15 |
| Major | Large fire, may spread | 30 |
| Catastrophic | Uncontrollable, magazine risk | 60 |

### FloodSeverity (5 levels)

| Level | Description | Flood Rate/sec |
|-------|-------------|----------------|
| None | No flooding | 0% |
| Minor | Small leak | 2% |
| Moderate | Significant flooding | 5% |
| Major | Heavy flooding, affects stability | 10% |
| Critical | Risk of capsizing | 20% |

### ShipDamageState (6 states)

| State | HP Range | Description |
|-------|----------|-------------|
| Operational | >70% | Full functionality |
| Damaged | 30-70% | Some systems impaired |
| HeavyDamage | 10-30% | Major impairment |
| Critical | <10% | Risk of sinking |
| Sinking | - | Ship is going down |
| Destroyed | 0% | Ship lost |

### CriticalType (10 types)

```csharp
public enum CriticalType
{
    EngineRoom,         // Speed reduction
    Rudder,             // Turning impaired
    FireControl,        // Accuracy reduced
    Magazine,           // Risk of detonation
    FuelTank,           // Fire risk, speed loss
    Bridge,             // All stats reduced
    PropellerShaft,     // Speed/maneuverability
    Turret,             // Weapon disabled
    TorpedoTubes,       // Torpedoes disabled
    Communications      // Spotting reduced
}
```

---

## Damage Event Data

### DamageEvent

```csharp
[Serializable]
public class DamageEvent
{
    // Source
    public uint sourceShipNetId;
    public uint projectileId;
    public DamageType damageType;

    // Hit Info
    public Vector3 hitPoint;
    public Vector3 hitDirection;
    public string compartmentHit;
    public bool belowWaterline;

    // Damage Values
    public float rawDamage;
    public float actualDamage;      // After armor/modifiers
    public float armorPenetrated;

    // Effects
    public bool causedFire;
    public bool causedFlooding;
    public bool causedCritical;
    public string criticalType;

    // Timestamp
    public float eventTime;
}
```

---

## Ship Health State

### ShipHealthState

```csharp
[Serializable]
public class ShipHealthState
{
    // Health
    public float currentHealth;
    public float maxHealth;
    public float healthPercent => currentHealth / maxHealth;

    // Armor (mm)
    public float beltArmor;         // Side armor
    public float deckArmor;         // Top armor
    public float bulkheadArmor;     // Internal armor

    // Damage State
    public ShipDamageState damageState;
    public float totalDamageTaken;

    // Hazards
    public int activeFireCount;
    public int floodedCompartmentCount;
    public float listAngle;         // Ship tilt from flooding
    public float sinkingRate;       // Meters per second

    // Modifiers (applied to ship systems)
    public float speedModifier = 1f;
    public float turnModifier = 1f;
    public float accuracyModifier = 1f;
    public float reloadModifier = 1f;

    public void ApplyDamage(float damage);
    public void UpdateDamageState();
}
```

---

## Compartment System

### CompartmentState

```csharp
[Serializable]
public class CompartmentState
{
    // Identity
    public string compartmentId;
    public CompartmentType type;
    public bool isVital;

    // Position
    public Vector3 centerPosition;
    public Bounds bounds;
    public bool isBelowWaterline;

    // Health
    public float currentHealth;
    public float maxHealth;
    public float armorThickness;

    // Flooding
    public FloodSeverity floodSeverity;
    public float floodLevel;        // 0-1 percentage
    public float floodRate;
    public bool canBeSealed;

    // Fire
    public FireSeverity fireSeverity;
    public float fireIntensity;     // 0-1
    public float fireSpreadChance;
    public bool isBeingFought;

    // Functionality
    public bool isDestroyed;
    public bool isFunctional = true;
    public float efficiencyModifier = 1f;

    public float TakeDamage(float damage);
    public void StartFire(FireSeverity severity);
    public void StartFlooding(FloodSeverity severity, float rate);
    public void ExtinguishFire();
    public void SealFlooding();
}
```

---

## Fire & Flooding Instances

### FireInstance

```csharp
[Serializable]
public class FireInstance
{
    public string fireId;
    public string compartmentId;
    public Vector3 origin;
    public FireSeverity severity;
    public float intensity;         // 0-1
    public float damagePerSecond;
    public float spreadTimer;
    public bool isBeingFought;
}
```

### FloodingInstance

```csharp
[Serializable]
public class FloodingInstance
{
    public string floodId;
    public string compartmentId;
    public Vector3 breachPoint;
    public FloodSeverity severity;
    public float currentLevel;      // 0-1 percentage
    public float ingressRate;       // Water coming in
    public float pumpRate;          // Pumping out
    public bool isSealed;
}
```

---

## Critical Damage

### CriticalDamage

```csharp
[Serializable]
public class CriticalDamage
{
    public string criticalId;
    public string compartmentId;
    public CriticalType type;
    public float severity;          // 0-1
    public float effectModifier;    // Reduction to related stats
    public bool canBeRepaired;
    public float repairProgress;

    public float GetPenalty() => 1f - (severity * effectModifier);
}
```

---

## Damage Calculation

### DamageCalculationParams

```csharp
[Serializable]
public class DamageCalculationParams
{
    // Incoming
    public float baseDamage;
    public DamageType damageType;
    public float penetration;
    public float impactAngle;

    // Target
    public float targetArmor;
    public bool isBelowWaterline;
    public CompartmentType targetCompartment;

    // Modifiers
    public float crewDamageControl = 1f;
    public float moduleDamageReduction = 0f;
    public float tierModifier = 1f;
}
```

### DamageCalculationResult

```csharp
[Serializable]
public class DamageCalculationResult
{
    public float finalDamage;
    public bool didPenetrate;
    public float effectiveArmor;
    public float damageReduction;
    public bool triggersFire;
    public bool triggersFlooding;
    public bool triggersCritical;
    public CriticalType? criticalType;
}
```

---

## Integration Points

### Dependencies
- None (standalone data)

### Used By
- [[DamageController]] - Damage application
- [[DamageControlTeam]] - Fire/flooding repair
- [[BallisticsCalculator]] - Hit result generation
- [[ProjectileManager]] - Damage delivery

---

## Related Files
- [[DamageController]] - Damage management
- [[DamageControlTeam]] - Damage control operations
- [[BallisticsData]] - Ballistics system

---

## Design Notes
- 13 compartment types cover all ship sections
- Fire and flooding are separate hazard systems
- Critical damage has lasting effects until repaired
- Modifiers affect speed, turn, accuracy, reload
- Sinking triggers at 45 degree list or 60% flood
- Magazine detonation is instant destruction

