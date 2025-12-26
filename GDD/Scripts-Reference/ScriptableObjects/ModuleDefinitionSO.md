# ModuleDefinitionSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Items/ModuleDefinitionSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Items` |
| **Inheritance** | `EquipmentDefinitionSO` → `ScriptableObject` |
| **Lines** | 279 |
| **Architecture** | Configuration-Driven Design with RNG Quality Variance |

---

## Purpose

Defines module equipment with **procedural quality variance** (70-130% GDD spec). Modules are ship systems that provide passive or active bonuses to fire control, damage control, radar, sonar, and communications.

**Key Features**:
- **Quality Variance System**: Each module instance rolls 70-130% quality on generation
- **Base Values**: Configure base stats at 100% quality
- **Active vs Passive**: Passive modules always active, active modules require activation
- **Resource Costs**: Power consumption and ammunition requirements
- **Crew Skill Requirements**: Higher-level crew improves module effectiveness

---

## Module Type

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `moduleType` | `ModuleType` | `FireControl` | Type of module system |

### ModuleType Values
- **FireControl**: Improves turret accuracy
- **DamageControl**: Improves damage repair speed (active ability)
- **Radar**: Increases detection range
- **Sonar**: Increases underwater detection (submarine/torpedo detection)
- **Communications**: Party coordination bonus

---

## Module Effects (Base Values at 100% Quality)

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `baseEffectValue` | `float` | 0-100% | 15 | Base primary effect value (e.g., +15% accuracy) - **actual varies 70-130%** |
| `baseSecondaryEffectValue` | `float` | 0-50% | 0 | Base secondary effect value (optional bonus) - **actual varies 70-130%** |

**Important**: These are **base values at 100% quality**. Actual effect varies based on rolled quality percentage.

**Example**: Fire Control Module
- Base effect: +15% turret accuracy
- Rolled quality: 120% (Good quality)
- Actual effect: +18% turret accuracy (15 × 1.2)

---

## Quality Variance (GDD: 70-130%)

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `enableQualityVariance` | `bool` | - | `true` | Enable procedural quality variance when generating module instances |
| `minQuality` | `float` | 0.5-1.0 | 0.7 | Minimum quality multiplier (Poor quality = 70%) |
| `maxQuality` | `float` | 1.0-1.5 | 1.3 | Maximum quality multiplier (Exceptional quality = 130%) |

### Quality Tier Distribution
Quality is rolled on a probability curve:
- **Poor** (70-85%): 15% chance - Gray
- **Below Average** (85-95%): 20% chance - White
- **Average** (95-105%): 30% chance - Green
- **Good** (105-115%): 20% chance - Blue
- **Excellent** (115-125%): 10% chance - Purple
- **Exceptional** (125-130%): 5% chance - Gold

**Implementation**: See `QualityGenerator` class in `WOS.ScriptableObjects.Core`

---

## Active vs Passive

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `isPassive` | `bool` | - | `true` | Is this module always active or requires activation? |
| `cooldownTime` | `float` | 0-300 seconds | 60 | Cooldown time in seconds (for active modules) |
| `effectDuration` | `float` | 0-120 seconds | 30 | Duration of effect in seconds (for active modules) |

**Passive Modules**: Always active, no cooldown (Fire Control, Radar, Sonar, Communications)

**Active Modules**: Require activation, have cooldown (Damage Control)

---

## Resource Costs

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `powerConsumption` | `float` | 0-100 | 10 | Power consumption (affects ship systems) |
| `requiresAmmo` | `bool` | - | `false` | Requires ammunition/consumables to use? |
| `requiredAmmoType` | `string` | - | Empty | Ammo type required (if applicable) |

**Example**: Damage Control module
- `isPassive`: false (active ability)
- `requiresAmmo`: true
- `requiredAmmoType`: "RepairKit"
- `powerConsumption`: 25

---

## Crew Requirements

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `minimumCrewLevel` | `int` | 1-200 | 1 | Minimum crew level required to operate |
| `optimalCrewSize` | `int` | 3-20 sailors | 5 | Optimal crew size for this module |

---

## Key Methods

### Generate Module Instance
```csharp
public ModuleInstanceData GenerateModuleInstance(string playerId)
```
Generates a module instance with rolled quality using GDD probability distribution.

**Returns**: `ModuleInstanceData` with:
- Unique instance ID (GUID)
- Rolled quality percentage (70-130%)
- Quality tier (Poor, Average, Good, Excellent, Exceptional)
- Actual effect values (base × quality)
- Creation timestamp

**Example**:
```csharp
ModuleDefinitionSO fireControl = // from database
ModuleInstanceData instance = fireControl.GenerateModuleInstance("player_12345");

Debug.Log($"Quality: {instance.qualityPercent * 100}%"); // e.g., "112%"
Debug.Log($"Tier: {instance.qualityTier}"); // e.g., "Good"
Debug.Log($"Effect: +{instance.effectValue}% accuracy"); // e.g., "+16.8%"
```

### Get Effect at Quality
```csharp
public float GetEffectAtQuality(float quality)
```
Calculate effect value at specific quality percentage.

**Example**: `GetEffectAtQuality(1.2f)` → `baseEffectValue × 1.2`

### Get Effect Range
```csharp
public StatRange GetEffectRange()
```
Returns the min-max range of effect based on quality variance.

**Example**: Fire Control with base 15%
- Min: 15 × 0.7 = 10.5%
- Max: 15 × 1.3 = 19.5%

### Get Effect Description
```csharp
public string GetEffectDescription()
```
Returns human-readable effect description for UI.

**Examples**:
- Fire Control: "+10.5% - 19.5% Turret Accuracy" (if variance enabled)
- Radar: "+15% Detection Range" (if variance disabled)

### Can Activate
```csharp
public bool CanActivate(float currentPower, bool hasAmmo)
```
Check if module is currently usable based on power and ammo availability.

---

## ModuleInstanceData Structure

Runtime instance of a module with rolled stats (separate from definition).

### Identity
| Field | Type | Description |
|-------|------|-------------|
| `instanceId` | `string` | Unique instance ID (GUID) |
| `playerId` | `string` | Owner player ID |
| `definitionId` | `string` | Reference to ModuleDefinitionSO.equipmentId |
| `moduleName` | `string` | Display name |
| `moduleType` | `ModuleType` | Type of module |

### Quality (GDD: 70-130%)
| Field | Type | Description |
|-------|------|-------------|
| `qualityPercent` | `float` | Rolled quality percentage (0.7-1.3) |
| `qualityTier` | `QualityTier` | Tier classification (Poor, Average, Good, etc.) |

### Rolled Stats
| Field | Type | Description |
|-------|------|-------------|
| `effectValue` | `float` | Actual primary effect (base × quality) |
| `secondaryEffectValue` | `float` | Actual secondary effect (base × quality) |

### State
| Field | Type | Description |
|-------|------|-------------|
| `isEquipped` | `bool` | Is this module currently equipped? |
| `equippedShipId` | `string` | Ship ID where equipped |
| `equippedSlot` | `string` | Slot identifier |

### Metadata
| Field | Type | Description |
|-------|------|-------------|
| `createdAt` | `DateTime` | Instance creation timestamp |
| `updatedAt` | `DateTime` | Last modification timestamp |

### Instance Methods
- `GetQualityName()`: Returns quality display name (e.g., "Good", "Exceptional")
- `GetQualityColor()`: Returns Unity Color for UI (e.g., Blue for Good, Gold for Exceptional)
- `GetQualityPercentString()`: Returns formatted percentage (e.g., "112%")

---

## Tier-Based Effect Scaling (OnValidate)

### Tier 1
- Base Effect: 5-15%
- Low-tier modules provide minimal bonuses

### Tier 5
- Base Effect: 30-50%
- Mid-tier modules provide significant bonuses

### Tier 7
- Base Effect: 50-75%
- High-tier modules provide major bonuses

**Note**: These are base values. Actual values vary 70-130% based on quality roll.

---

## Module Type Auto-Configuration

### Damage Control (OnValidate)
When `moduleType` is set to `DamageControl`:
- `isPassive`: Automatically set to **false** (active ability)
- `requiresAmmo`: Automatically set to **true**
- `requiredAmmoType`: Automatically set to "RepairKit"

This ensures Damage Control modules are always configured correctly.

---

## Auto-Generated Values (OnValidate)

### Equipment ID
**Format**: `Module_T{tier}_{moduleType}`

**Example**: `Module_T5_FireControl`

### Equipment Name
**Format**: `{moduleType} System (T{tier})`

**Example**: `FireControl System (T5)`

---

## Usage Example

```csharp
// Create via Unity menu: Create > WOS > Equipment > Module
ModuleDefinitionSO fireControl = // from database

// Generate module instance with random quality
ModuleInstanceData module = fireControl.GenerateModuleInstance("player_12345");

// Display quality info
Debug.Log($"Quality: {module.GetQualityPercentString()}"); // "112%"
Debug.Log($"Tier: {module.GetQualityName()}"); // "Good"
Debug.Log($"Effect: +{module.effectValue}% accuracy"); // "+16.8%"

// Check if module can be activated (for active modules)
float shipPower = 75f;
bool hasRepairKits = true;
if (fireControl.CanActivate(shipPower, hasRepairKits))
{
    Debug.Log("Module can be activated");
}

// Get effect range for UI display
var range = fireControl.GetEffectRange();
Debug.Log($"Effect range: {range.min}% - {range.max}%");

// Get description for tooltip
string desc = fireControl.GetEffectDescription();
Debug.Log(desc); // "+10.5% - 19.5% Turret Accuracy"
```

---

## Integration Points

### Used By
- **ServerInventoryManager.cs** - Module instance generation and management
- **PlayFabInventoryService.cs** - Module instance persistence
- **EquipmentPanel.cs** - Module inventory UI
- **ItemDatabaseSO.cs** - Master equipment database
- **EquipmentDatabaseSO.cs** - Specialized equipment database

### Related Systems
- **EquipmentDefinitionSO** - Base class for all equipment
- **TurretDefinitionSO** - Turret equipment
- **QualityGenerator** - Quality variance RNG system
- **StatRange** - Min-max range data structure
- **ModuleInstanceData** - Runtime instance data

---

## Design Notes

### Quality Variance Philosophy

Modules use a **procedural quality variance system** (70-130%) to add:

1. **Loot Excitement**: Finding a 130% quality Fire Control module is rewarding
2. **Trade Economy**: Quality variance creates a market for high-quality modules
3. **Progression Depth**: Players can upgrade from Poor → Average → Good → Exceptional
4. **RNG Without Frustration**: 70-130% variance is meaningful but not game-breaking

### Navy Field Inspiration

This system is inspired by Navy Field's module quality system where:
- Modules have base stats
- Quality affects actual performance (70-130% range)
- Players hunt for high-quality modules
- Trading economy revolves around module quality

### Module vs Turret Difference

**Modules** have quality variance, **Turrets** do not:
- **Turrets**: Fixed stats, deterministic performance
- **Modules**: Variable stats, RNG-based performance

This design choice makes modules feel like "special equipment" while keeping turrets consistent and predictable.

### Passive vs Active Balance

**Passive Modules** (Fire Control, Radar):
- Always active
- No cooldown
- Low power consumption
- Steady bonus

**Active Modules** (Damage Control):
- Requires activation
- Long cooldown (60-120 seconds)
- High power consumption
- Temporary powerful effect

This creates strategic choice: passive reliability vs active power.

---

## Create via Unity Menu

**Path**: `Create > WOS > Equipment > Module`

**Order**: 3

**Default Filename**: `Module_T1_FireControl`
