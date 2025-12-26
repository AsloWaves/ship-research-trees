---
tags: [script, modules, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Modules.Data
file-path: Assets/Scripts/Modules/Data/ModuleData.cs
status: IMPLEMENTED
size: ~457 lines
feature-group: modules
---

# ModuleData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Modules.Data
**File**: `Assets/Scripts/Modules/Data/ModuleData.cs`
**Size**: ~457 lines
**Dependencies**: None (standalone data)

---

## Purpose
Core module system data structures. Includes module categories, slot types, quality tiers, stat modifiers, module instances, slots, loadouts, active effects, and upgrade requirements. Based on GDD Module-System.md specifications.

---

## Module Enums

### ModuleCategory (22 categories)

| Category | Domain |
|----------|--------|
| ArmorPlating | Defensive |
| DamageControl | Defensive |
| FireSuppression | Defensive |
| FloodingControl | Defensive |
| FireControl | Offensive |
| Targeting | Offensive |
| Ammunition | Offensive |
| GunneryTraining | Offensive |
| Engine | Mobility |
| Propulsion | Mobility |
| Steering | Mobility |
| Radar | Utility |
| Sonar | Utility |
| Communications | Utility |
| Concealment | Utility |
| AircraftHandling | Carrier |
| FlightDeck | Carrier |
| CargoExpansion | Economy |
| FuelEfficiency | Economy |
| Captain | Special |
| Crew | Special |
| Experimental | Special |

### ModuleSlotType (7 types)

```csharp
public enum ModuleSlotType
{
    Universal,          // Any module type
    Defensive,          // Armor/damage control modules
    Offensive,          // Fire control/targeting modules
    Mobility,           // Engine/steering modules
    Utility,            // Radar/sonar/communications
    Special,            // Captain/crew/experimental
    Carrier             // Aircraft-related modules
}
```

### ModuleQuality (5 tiers)

| Quality | Stat Multiplier |
|---------|-----------------|
| Standard | 1.0x (100%) |
| Improved | 1.1x (+10%) |
| Advanced | 1.25x (+25%) |
| Elite | 1.4x (+40%) |
| Prototype | 1.6x (+60%) |

### ModuleStatType (26 stat types)

**Combat Stats**:
- MainBatteryReload, SecondaryBatteryReload, AAReload, TorpedoReload
- Accuracy, Range, TraverseSpeed

**Defensive Stats**:
- ArmorEffectiveness, DamageReduction
- FireResistance, FloodingResistance, CriticalResistance

**Mobility Stats**:
- MaxSpeed, Acceleration, TurnRate, RudderShift

**Detection Stats**:
- SurfaceDetection, AirDetection, RadarRange, SonarRange

**Utility Stats**:
- RepairSpeed, RepairAmount, CrewEfficiency, XPGain, CreditGain

**Carrier Stats**:
- AircraftCapacity, AircraftRestoration, PlaneSpeed, PlaneHealth

---

## Module Data Classes

### ModuleStatModifier

```csharp
[Serializable]
public class ModuleStatModifier
{
    public ModuleStatType statType;
    public float flatBonus;            // Added to stat
    public float percentageModifier;   // Multiplier (0.1 = +10%)
    public bool isPenalty;             // Negative effect?

    public float Apply(float baseValue)
    {
        float modified = baseValue + flatBonus;
        modified *= (1f + percentageModifier);
        return modified;
    }
}
```

### ModuleInstance

```csharp
[Serializable]
public class ModuleInstance
{
    // Identity
    public string instanceId;
    public string moduleDefinitionId;
    public ModuleQuality quality = ModuleQuality.Standard;

    // State
    public bool isEquipped;
    public string equippedSlotId;
    public float condition = 1f;        // 0-1, affects effectiveness

    // Upgrades
    public int upgradeLevel;            // 0-5 upgrade levels
    public List<string> appliedEnhancements;
}
```

**Methods**:
- `GetQualityMultiplier()` - Returns 1.0-1.6 based on quality
- `GetUpgradeMultiplier()` - Returns 1.0 + (level * 0.05), +5% per level
- `GetEffectiveness()` - Returns condition * quality * upgrade multipliers

### ModuleStatBonus

```csharp
[Serializable]
public struct ModuleStatBonus
{
    public ModuleStatType statType;
    public float value;
}
```

Network-serializable bonus entry (List instead of Dictionary for Mirror).

### ModuleSlot

```csharp
[Serializable]
public class ModuleSlot
{
    // Slot Identity
    public string slotId;
    public string slotName;
    public ModuleSlotType slotType;

    // Restrictions
    public int minTier = 1;             // Minimum ship tier to unlock
    public List<ModuleCategory> allowedCategories;

    // State
    public bool isUnlocked = true;
    public string equippedModuleInstanceId;

    public bool CanEquip(ModuleCategory category);
}
```

### ShipModuleLoadout

```csharp
[Serializable]
public class ShipModuleLoadout
{
    // Slots
    public List<ModuleSlot> slots;

    // Equipped Modules
    public List<ModuleInstance> equippedModules;

    // Cached Stats (List for Mirror serialization)
    public List<ModuleStatBonus> cachedBonusList;

    // Local cache (not serialized)
    private Dictionary<ModuleStatType, float> _bonusCache;
}
```

**Methods**:
- `GetSlot(string slotId)` - Returns slot by ID
- `GetModule(string instanceId)` - Returns module by ID
- `GetStatBonus(ModuleStatType statType)` - Returns total bonus for stat
- `SetCachedBonuses(Dictionary)` - Server sets bonuses
- `GetCachedBonuses()` - Returns dictionary
- `RebuildBonusCache()` - Rebuilds local cache from list after network sync

---

## Module Effects

### ModuleActiveEffect

```csharp
[Serializable]
public class ModuleActiveEffect
{
    public string effectId;
    public string effectName;
    public string description;

    // Activation
    public float cooldown;              // Seconds between uses
    public float duration;              // Effect duration
    public float activationCost;        // Resource cost

    // Effect
    public List<ModuleStatModifier> temporaryModifiers;

    // State
    public float currentCooldown;
    public bool isActive;
    public float activeTimeRemaining;
}
```

### ModuleConditionalEffect

```csharp
[Serializable]
public class ModuleConditionalEffect
{
    public string effectId;

    // Trigger
    public ModuleTriggerType triggerType;
    public float triggerChance = 1f;    // 0-1 probability
    public float triggerCooldown;       // Min time between triggers

    // Effect
    public List<ModuleStatModifier> effectModifiers;
    public float effectDuration;

    // State
    public float lastTriggerTime;
}
```

### ModuleTriggerType (9 types)

```csharp
public enum ModuleTriggerType
{
    OnHit,                  // When ship is hit
    OnFire,                 // When fire starts
    OnFlooding,             // When flooding starts
    OnCritical,             // When critical damage occurs
    OnKill,                 // When enemy destroyed
    OnLowHealth,            // When health below threshold
    OnSpotted,              // When detected by enemy
    OnBattleStart,          // At battle beginning
    OnBattleEnd             // At battle end
}
```

---

## Module Upgrades

### ModuleUpgradeRequirements

```csharp
[Serializable]
public class ModuleUpgradeRequirements
{
    public int targetLevel;             // Upgrade level (1-5)
    public int creditCost;
    public int specialCurrencyCost;     // Premium currency
    public List<MaterialRequirement> materials;
    public float successChance = 1f;    // Upgrade success probability
}
```

### MaterialRequirement

```csharp
[Serializable]
public class MaterialRequirement
{
    public string materialId;
    public int quantity;
}
```

---

## Integration Points

### Dependencies
- None (standalone data)

### Used By
- [[ModuleController]] - Module management
- [[ModuleNetworkSerializers]] - Network serialization
- [[ModuleDefinitionSO]] - Module definitions
- UI module panels

---

## Related Files
- [[ModuleController]] - Module mechanics
- [[ModuleNetworkSerializers]] - Network serialization
- [[ModuleDefinitionSO]] - ScriptableObject definitions

---

## Design Notes
- 22 module categories covering all ship systems
- 7 slot types for equipment restrictions
- 5 quality tiers with 10-60% stat bonuses
- 26 stat types for comprehensive modification
- Condition (0-1) affects module effectiveness
- Upgrade levels 0-5 with +5% per level
- Active effects have cooldown and duration
- Conditional effects trigger on 9 event types
- Uses List instead of Dictionary for Mirror serialization
- Local cache rebuilt after network sync

