---
tags: [script, modules, scriptableobject, configuration, implemented]
script-type: ScriptableObject
namespace: WOS.Modules.ScriptableObjects
file-path: Assets/Scripts/Modules/ScriptableObjects/ModuleDefinitionSO.cs
status: IMPLEMENTED
size: ~238 lines
feature-group: modules
---

# ModuleDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Modules.ScriptableObjects
**File**: `Assets/Scripts/Modules/ScriptableObjects/ModuleDefinitionSO.cs`
**Size**: ~238 lines
**Dependencies**: EquipmentDefinitionSO, ModuleData
**Create Menu**: `Create > WOS > Equipment > Module`

---

## Purpose
ScriptableObject definition for ship modules. Inherits from EquipmentDefinitionSO for base equipment properties. Defines module category, quality, stat modifiers, active abilities, conditional effects, restrictions, and upgrade paths.

---

## Inheritance

```
EquipmentDefinitionSO (base equipment)
    └── ModuleDefinitionSO (module-specific)
```

Inherits all equipment properties (name, description, icon, tier, weight, price, etc.)

---

## Configuration

### Classification

```csharp
[Header("Module Classification")]
public ModuleCategory category;
public ModuleQuality baseQuality = ModuleQuality.Standard;
public List<ModuleSlotType> compatibleSlots;
```

### Stat Modifiers

```csharp
[Header("Stat Modifiers")]
public List<ModuleStatModifier> statModifiers;
```

### Active Ability

```csharp
[Header("Active Ability")]
public bool hasActiveAbility;
public ModuleActiveAbilityConfig activeAbility;
```

### Conditional Effects

```csharp
[Header("Conditional Effects")]
public List<ModuleConditionalEffectConfig> conditionalEffects;
```

### Restrictions

```csharp
[Header("Restrictions")]
public List<string> allowedShipClasses;
public List<string> incompatibleModules;
[Range(1, 6)]
public int maxPerShip = 1;
```

### Upgrade Path

```csharp
[Header("Upgrade Path")]
public bool isUpgradeable = true;
[Range(0, 5)]
public int maxUpgradeLevel = 5;
public float upgradeeCostMultiplier = 1.5f;
```

### Visual

```csharp
[Header("Visual")]
public GameObject activationEffectPrefab;
public GameObject passiveEffectPrefab;
```

---

## Methods

### Get Stat Modifier

```csharp
public float GetStatModifier(ModuleStatType statType)
{
    foreach (var mod in statModifiers)
    {
        if (mod.statType == statType)
        {
            return mod.percentageModifier + mod.flatBonus;
        }
    }
    return 0f;
}
```

### Ship Class Check

```csharp
public bool CanEquipOnShipClass(string shipClass)
{
    if (allowedShipClasses.Count == 0) return true;  // Universal
    return allowedShipClasses.Contains(shipClass);
}
```

### Incompatibility Check

```csharp
public bool IsIncompatibleWith(string moduleId)
{
    return incompatibleModules.Contains(moduleId);
}
```

### Calculate Upgrade Cost

```csharp
public int CalculateUpgradeCost(int targetLevel)
{
    if (targetLevel <= 0 || targetLevel > maxUpgradeLevel) return 0;

    float cost = purchasePrice * 0.2f;  // Base is 20% of purchase
    for (int i = 1; i < targetLevel; i++)
    {
        cost *= upgradeeCostMultiplier;  // 1.5x per level
    }
    return Mathf.RoundToInt(cost);
}
```

---

## Auto-Slot Assignment

OnValidate automatically assigns compatible slots based on category:

| Category | Auto Slot Type |
|----------|---------------|
| ArmorPlating, DamageControl, FireSuppression, FloodingControl | Defensive |
| FireControl, Targeting, Ammunition, GunneryTraining | Offensive |
| Engine, Propulsion, Steering | Mobility |
| Radar, Sonar, Communications, Concealment | Utility |
| AircraftHandling, FlightDeck | Carrier |
| Others | Universal |

---

## ModuleActiveAbilityConfig

```csharp
[Serializable]
public class ModuleActiveAbilityConfig
{
    // Ability Info
    public string abilityName;
    public string abilityDescription;
    public Sprite abilityIcon;

    // Timing
    public float cooldown = 60f;         // 10-300 seconds
    public float duration = 20f;         // 5-120 seconds

    // Activation
    public int charges = 1;              // 1-5 charges
    public float chargeRestoreTime = 60f;

    // Effect
    public List<ModuleStatModifier> activeModifiers;

    // Audio/Visual
    public AudioClip activationSound;
    public GameObject activationVFX;
}
```

---

## ModuleConditionalEffectConfig

```csharp
[Serializable]
public class ModuleConditionalEffectConfig
{
    // Trigger
    public ModuleTriggerType triggerType;
    public float triggerChance = 1f;     // 0-1
    public float triggerCooldown = 30f;  // 0-120 seconds

    // Condition
    public float healthThreshold = 0.25f;  // For OnLowHealth

    // Effect
    public float effectDuration = 10f;   // 0 = instant
    public List<ModuleStatModifier> effectModifiers;

    // Feedback
    public AudioClip triggerSound;
    public GameObject triggerVFX;
}
```

---

## Upgrade Cost Formula

Base upgrade cost = 20% of purchase price
Each level multiplied by 1.5x

| Level | Cost Multiplier |
|-------|-----------------|
| 1 | 0.20x |
| 2 | 0.30x |
| 3 | 0.45x |
| 4 | 0.675x |
| 5 | 1.0125x |

---

## Integration Points

### Dependencies
- [[EquipmentDefinitionSO]] - Base class
- [[ModuleData]] - Enums and data types

### Used By
- [[ModuleController]] - Module management
- UI module panels
- Inventory system

---

## Related Files
- [[ModuleData]] - Data structures
- [[ModuleController]] - Module mechanics
- [[EquipmentDefinitionSO]] - Base equipment

---

## Design Notes
- Inherits from EquipmentDefinitionSO for base properties
- Category determines auto-assigned compatible slots
- Active abilities have cooldown, duration, and charges
- Conditional effects trigger on 9 event types
- Ship class restrictions for specialized modules
- Incompatibility list prevents conflicting modules
- Max 1 of same module by default (maxPerShip)
- Upgrade costs scale exponentially (1.5x)
- Visual effects for both activation and passive display
- OnValidate ensures slot compatibility

