---
tags: [script, ships, scriptableobject, configuration, implemented]
script-type: ScriptableObject
namespace: WOS.Ships.ScriptableObjects
file-path: Assets/Scripts/Ships/ScriptableObjects/ShipDefinitionSO.cs
status: IMPLEMENTED
size: ~880 lines
feature-group: ships
---

# ShipDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Ships.ScriptableObjects
**File**: `Assets/Scripts/Ships/ScriptableObjects/ShipDefinitionSO.cs`
**Size**: ~880 lines
**Create**: `Create > WOS > Ships > Ship Definition`

---

## Purpose
Master ScriptableObject defining a ship type's base stats, slot configuration, armor, and economics. Based on GDD Ship-Progression.md and Tiers.md specifications. Every equipment slot has an associated crew slot; all supplies use unified Tetris inventory.

---

## Configuration Sections

### Identity

```csharp
[Header("Identity")]
public string shipDefinitionId;    // Unique ID (e.g., "destroyer_t1_usn")
public string defaultName;         // Display name
public string description;         // Historical/descriptive text
public Sprite shipIcon;            // UI icon
public GameObject shipPrefab;      // 3D model prefab
```

### Classification

```csharp
[Header("Classification")]
public ShipClass shipClass;        // Destroyer, Cruiser, Battleship, etc.
public ShipTier tier = ShipTier.T1; // T1-T10
public ShipNation nation;          // USN, RN, IJN, KM, etc.
public string designEra;           // "WWII", "Cold War"
```

### Physical Dimensions

```csharp
[Header("Physical Dimensions")]
public float displacement = 5000f;  // Tons (500-100000)
public float length = 100f;         // Meters (20-300)
public float beam = 15f;            // Width in meters (5-50)
```

### Survivability

```csharp
[Header("Survivability")]
public float baseHealth = 1000f;    // Base HP
public float torpedoProtection = 0f; // 0-1 damage reduction
```

### Armor (Navy Field Style)

```csharp
[Header("Armor Configuration")]
public ArmorConfiguration armorConfiguration;
```

9-zone armor system:
- Deck: Forward, Center, Aft
- Belt: Forward, Center, Aft
- Structural: Conning Tower, Main Turrets, Secondary Turrets

### Mobility

```csharp
[Header("Mobility")]
public float maxSpeed = 20f;        // Knots (5-50)
public float acceleration = 2f;    // Knots/s²
public float deceleration = 1.5f;  // Braking power
public float turnRate = 10f;       // Degrees/s (1-30)
public float maxRudderAngle = 35f; // Degrees (15-45)
public float rudderShiftTime = 5f; // Seconds to full rudder
public float steerageway = 3f;     // Min speed for steering
public float helmResponse = 2f;    // Auto-nav response
public float dragCoefficient = 0.5f; // Water drag
```

### Detection

```csharp
[Header("Detection")]
public float surfaceDetectionRange = 10f; // km
public float airDetectionRange = 6f;      // km
```

### Turret Slots

```csharp
[Header("Turret Slots")]
public List<TurretSlotConfig> turretSlots;
```

### Module Slots

```csharp
[Header("Module Slots")]
public List<ShipModuleSlotConfig> moduleSlots;
```

### Cargo

```csharp
[Header("Cargo")]
public Vector2Int cargoGridSize = new Vector2Int(10, 10);
public float maxCargoWeight = 500f;  // Tons
```

### Aircraft (Carriers)

```csharp
[Header("Aircraft")]
public int aircraftCapacity = 0;
public List<string> compatibleAircraftTypes;
```

### Economics

```csharp
[Header("Economics")]
public long purchasePrice = 10000;
public long premiumPrice = 0;
public float repairCostPerHp = 1f;
public long operatingCost = 100;
public long baseInsuranceCost = 1000;
```

### Unlock Requirements

```csharp
[Header("Unlock Requirements")]
public ShipUnlockRequirements unlockRequirements;
```

---

## Slot Configuration Classes

### TurretSlotConfig

```csharp
public class TurretSlotConfig
{
    public string slotId;
    public string slotName;
    public Vector2 position;
    public bool canRotate360;
    public Vector2 rotationLimits;
    public float naturalForward;
    public List<FiringArc> firingArcs;
    public Vector2 elevationLimits;
    public TurretMountType mountType;
    public int minTier, maxTier;
    public float maxWeightTons;
    public Vector2Int slotSize;
    public List<int> compatibleCalibers;
    public int maxBarrels;
    public CrewClassificationType requiredCrewClassification;
}
```

### ShipModuleSlotConfig

```csharp
public class ShipModuleSlotConfig
{
    public string slotId;
    public string slotName;
    public Vector2 position;
    public ModuleSlotType slotType;  // Bridge, Engine, Support
    public SupportModuleCategory supportCategory;
    public int minTier, maxTier;
    public float maxWeightTons;
    public Vector2Int slotSize;
    public CrewClassificationType requiredCrewClassification;
}
```

---

## Utility Methods

```csharp
public float rudderRate => maxRudderAngle / rudderShiftTime;
public float GetTurningRadius();
public (int min, int max) GetEquipmentTierRange();
public int GetTotalCrewPositions();
public int GetTotalEquipmentSlots();
public float GetEffectiveStat(ShipStatType statType, float modifier);
public float GetAverageArmorThickness();
public float GetEffectiveMaxSpeed();
public float GetTotalArmorWeight();
public long GetTotalArmorCost();
public float GetEarningsMultiplier();
public float GetXPMultiplier();
public float GetPermadeathRisk();
public ShipLoadout CreateUIShipLoadout();
```

---

## Permadeath Risk by Tier

| Tier | Risk |
|------|------|
| T1-T2 | 0% |
| T3 | 5% |
| T4 | 10% |
| T5 | 15% |
| T6 | 20% |
| T7 | 25% |
| T8 | 30% |
| T9 | 35% |
| T10 | 40% |

---

## Integration Points

### Dependencies
- [[ShipProgressionData]] - Enums and data classes
- [[ArmorConfiguration]] - 9-zone armor system

### Used By
- [[FleetManager]] - Ship definitions lookup
- [[EquipmentPanel]] - Slot configuration
- [[NetworkedNavalController]] - Physics parameters

---

## Related Files
- [[ShipProgressionData]] - Data structures
- [[FleetManager]] - Fleet management
- [[ArmorConfiguration]] - Armor system

