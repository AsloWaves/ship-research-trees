# EquipmentDefinitionSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Items/EquipmentDefinitionSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Items` |
| **Inheritance** | `ScriptableObject` |
| **Type** | Abstract Base Class |
| **Lines** | 111 |
| **Architecture** | Configuration-Driven Design |

---

## Purpose

**Abstract base class** for all ship equipment ScriptableObjects (turrets, engines, modules, torpedoes). Provides common equipment properties like tier, nation, weight, economy, and grid size. Cannot be instantiated directly - use derived classes instead.

**Derived Equipment Types**:
- **TurretDefinitionSO** - Gun turrets and batteries
- **TorpedoDefinitionSO** - Torpedo launchers
- **ModuleDefinitionSO** - Ship systems (fire control, radar, damage control)
- **EngineDefinitionSO** - Engine and propulsion systems

---

## Equipment Identity

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `equipmentId` | `string` | Auto-generated | Unique equipment ID (e.g., 'MainBattery_T5_16inch') |
| `equipmentName` | `string` | Empty | Display name shown to players |
| `historicalDesignation` | `string` | Empty | Historical designation (e.g., 'Mark 12 5"/38 caliber') |
| `description` | `string` (TextArea) | Empty | Equipment description and stats |

---

## Nation & Era

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `nation` | `EquipmentNation` | `USA` | Nation that designed/manufactured this equipment |
| `era` | `Era` | `Interwar` | Historical era of introduction |
| `yearIntroduced` | `int` | 1935 | Year of introduction (1890-1960) |

### EquipmentNation Values
- USA, Japan, Britain, Germany, Russia, France, Italy, China
- Additional nations can be added via enum

### Era Values
- **PreDreadnought** (1890-1905): Early steam warships
- **Dreadnought** (1906-1918): WWI era
- **Interwar** (1919-1938): Between world wars
- **WWII** (1939-1945): World War II
- **PostWar** (1946-1960): Early Cold War

---

## Tier & Classification

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `tier` | `int` | 1-7 | 1 | Equipment tier (1-7) - higher tier = more powerful but restricted to higher tier ships |
| `equipmentLevel` | `int` | 20-140 | 20 | Equipment level (auto-calculated: tier × 20) |
| `rarity` | `EquipmentRarity` | `Common` | Equipment rarity affects drop rates and availability |

### Tier System
- **Tier 1**: Starting equipment, low performance
- **Tier 3**: Early-mid game equipment
- **Tier 5**: Mid-game equipment, balanced
- **Tier 7**: End-game equipment, high performance

**Equipment Level Formula**: `tier × 20`
- Tier 1 → Level 20
- Tier 2 → Level 40
- Tier 5 → Level 100
- Tier 7 → Level 140

This matches **Navy Field's equipment level system**.

### EquipmentRarity Values
- **Common**: Standard equipment, high availability
- **Uncommon**: Improved stats, moderate availability
- **Rare**: High stats, low availability
- **Epic**: Exceptional stats, very rare
- **Legendary**: Unique equipment, quest/achievement rewards

---

## Physical Properties

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `weightTons` | `float` | 0.1-3,000 tons | 10 | Equipment weight in tons (affects ship performance) |

**Weight Impact**:
- Heavy equipment reduces ship speed and maneuverability
- Ships have weight capacity limits per slot
- Weight calculation factors into ship stability and balance

---

## Grid & Inventory

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `gridSize` | `Vector2Int` | (2, 2) | Inventory grid size (width × height) for Tetris-style inventory |
| `icon` | `Sprite` | null | Equipment icon for inventory UI |
| `prefab` | `GameObject` | null | 3D model/prefab for visual representation |

**Grid Size Examples**:
- Small module: (2, 2)
- Medium turret: (3, 3)
- Large engine: (4, 5)
- Massive battleship turret: (6, 6)

---

## Economy

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `purchasePrice` | `int` | 100-1,000,000 | 1,000 | Base purchase price in credits |
| `sellPriceMultiplier` | `float` | 0.0-1.0 | 0.5 | Sell price (% of purchase price) |
| `isTradeable` | `bool` | - | `true` | Can this equipment be traded between players? |

### Sell Price Calculation
```csharp
public int GetSellPrice()
{
    return Mathf.RoundToInt(purchasePrice * sellPriceMultiplier);
}
```

**Default**: Players get 50% of purchase price when selling.

**Non-Tradeable Equipment**: Quest rewards, event items, achievement unlocks

---

## Key Methods

### Get Sell Price
```csharp
public int GetSellPrice()
```
Calculate sell price based on purchase price × sell price multiplier.

**Example**: 10,000 credits purchase → 5,000 credits sell (default 50%)

### Calculate Equipment Level
```csharp
public int CalculateEquipmentLevel()
```
Calculate equipment level from tier using Navy Field formula.

**Formula**: `tier × 20`

**Called automatically in `OnValidate()`.**

### OnValidate (Editor)
```csharp
protected virtual void OnValidate()
```
Auto-calculates values when editing in Unity Inspector:
- Auto-calculates `equipmentLevel` from tier
- Auto-generates `equipmentId` from filename if empty

**Override in derived classes** to add custom validation logic.

---

## Usage Example

```csharp
// This is an abstract class - use derived classes instead
TurretDefinitionSO turret = // from database

// Access base class properties
Debug.Log($"Equipment ID: {turret.equipmentId}");
Debug.Log($"Nation: {turret.nation}");
Debug.Log($"Tier: {turret.tier}");
Debug.Log($"Level: {turret.equipmentLevel}"); // tier × 20
Debug.Log($"Weight: {turret.weightTons} tons");

// Get sell price
int sellPrice = turret.GetSellPrice();
Debug.Log($"Sell for {sellPrice} credits");

// Check if tradeable
if (turret.isTradeable)
{
    Debug.Log("This equipment can be traded with other players");
}

// Historical info
Debug.Log($"Introduced: {turret.yearIntroduced} ({turret.era})");
Debug.Log($"Historical designation: {turret.historicalDesignation}");
```

---

## Derived Classes

### TurretDefinitionSO
Extends with:
- Firepower stats (caliber, barrels, damage, rate of fire)
- Ammunition (shell types, magazine capacity, reload time)
- Turret geometry (muzzle positions, elevation limits)
- Implements `IVisualMount`

### TorpedoDefinitionSO
Extends with:
- Torpedo specifications (caliber, tubes, damage, range, speed)
- Launcher properties (reload time, rotation speed)
- Guidance systems (passive, active, wire-guided)
- Implements `IVisualMount`

### ModuleDefinitionSO
Extends with:
- Module effects (quality variance 70-130%)
- Active vs passive configuration
- Resource costs (power, ammunition)
- Quality-based stat generation

### EngineDefinitionSO
Extends with:
- Propulsion stats (horsepower, fuel consumption, top speed)
- Engine type (diesel, turbine, steam, nuclear)
- Performance characteristics

---

## Integration Points

### Used By
- **ItemDatabaseSO** - Master equipment database
- **EquipmentDatabaseSO** - Specialized equipment database
- **ServerInventoryManager.cs** - Equipment instance management
- **PlayFabInventoryService.cs** - Equipment persistence
- **EquipmentPanel.cs** - Equipment inventory UI

### Related Systems
- **IVisualMount** - Visual mount interface (turrets, torpedoes)
- **WeaponMountData** - Geometry data structure
- **QualityGenerator** - Quality variance system (modules only)
- **ItemDefinitionSO** - Separate item definition system (cargo, consumables)

---

## Design Notes

### Abstract Base Class Pattern

`EquipmentDefinitionSO` uses the **Template Method Pattern**:

1. **Base class** provides common equipment properties (tier, nation, weight, economy)
2. **Derived classes** add specialized properties (firepower, propulsion, module effects)
3. **Virtual `OnValidate()`** allows custom validation in derived classes

**Benefits**:
- Reduces code duplication
- Ensures consistent equipment identity across all types
- Easy to add new equipment types

### Navy Field Compatibility

Equipment level calculation (`tier × 20`) matches **Navy Field's system**:
- Familiar to Navy Field players
- Tier-based progression (T1-T7)
- Equipment level gates (e.g., "Requires Level 100")

### Weight System

Equipment weight affects ship performance:
- **Light equipment**: Faster ship, better maneuverability
- **Heavy equipment**: Slower ship, worse turning

This creates **meaningful equipment choices** beyond raw stats.

### Grid-Based Inventory

`gridSize` supports **Tetris-style inventory** (similar to Resident Evil, Diablo):
- Equipment takes up variable space
- Players must manage limited cargo hold
- Strategic packing decisions

### Historical Accuracy

`historicalDesignation`, `yearIntroduced`, and `era` support:
- Authentic naval warfare atmosphere
- Educational value (historical gun designations)
- Era-locked servers (e.g., "WWII only" game modes)

---

## Create via Unity Menu

**This is an abstract class and cannot be created directly.**

Use derived classes instead:
- `Create > WOS > Equipment > Turret`
- `Create > WOS > Equipment > Torpedo Launcher`
- `Create > WOS > Equipment > Module`
- `Create > WOS > Equipment > Engine`
