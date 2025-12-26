# EquipmentData.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/Data/EquipmentData.cs` |
| **Namespace** | `WOS.Player.Data` |
| **Inheritance** | Abstract base class `EquipmentItem` with 3 derived classes |
| **Lines of Code** | 388 |
| **Architecture** | Equipment item hierarchy with crew efficiency system |

## Purpose

`EquipmentData.cs` defines the equipment item hierarchy for naval weapons, engines, and modules that can be installed on ships. Equipment items have crew requirements, weight properties, and tier-based performance scaling. Each equipment type (Turret, Engine, Module) has specific stats that affect ship performance.

## Class Hierarchy

```
EquipmentItem (abstract base)
    ├── TurretEquipment (Main/Secondary/AA guns)
    ├── EngineEquipment (Steam/Diesel/Turbine/Nuclear)
    └── ModuleEquipment (FireControl/DamageControl/Radar/Sonar)
```

## EquipmentItem (Base Class)

### Equipment Identity

| Field | Type | Description |
|-------|------|-------------|
| `ItemId` | `string` | Unique item instance ID (UUID) |
| `DefinitionId` | `string` | Item definition ID (e.g., "MainBattery_T5_16inch") |
| `DisplayName` | `string` | User-facing name |
| `Description` | `string` | Item description |

### Equipment Properties

| Field | Type | Description |
|-------|------|-------------|
| `Tier` | `int` | Equipment tier (1-7) |
| `Weight` | `float` | Weight in tons |
| `InventorySize` | `Vector2Int` | Grid size in inventory (width × height) |

### Economy

| Field | Type | Description |
|-------|------|-------------|
| `BuyPrice` | `long` | Purchase price in credits |
| `SellPrice` | `long` | Sell price (typically 60% of buy price) |

### Crew Requirements

| Field | Type | Description |
|-------|------|-------------|
| `RequiredCrewLevel` | `int` | Minimum crew level to operate |
| `RequiredCrewType` | `CrewClassification` | Type of crew needed |

### Base Methods

```csharp
public abstract EquipmentType GetEquipmentType();

public bool CanBeOperatedBy(CrewCard crew)
{
    if (crew.Classification != RequiredCrewType)
        return false;

    if (crew.CurrentLevel < RequiredCrewLevel)
        return false;

    return true;
}
```

## TurretEquipment Class

### Purpose
Naval gun turrets (Main Battery, Secondary Battery, AA guns) that provide offensive firepower.

### Turret Specifications

| Field | Type | Description |
|-------|------|-------------|
| `TurretType` | `TurretType` | Main, Secondary, AA |
| `Caliber` | `int` | Gun caliber in mm (e.g., 406mm, 155mm) |
| `BarrelCount` | `int` | Number of barrels (e.g., 3 for triple turret) |

### Combat Stats

| Field | Type | Description |
|-------|------|-------------|
| `Damage` | `float` | Base damage per shot |
| `Range` | `float` | Maximum range in meters |
| `Accuracy` | `float` | Base accuracy percentage (0-100) |
| `ReloadTime` | `float` | Reload time in seconds |
| `TurretRotationSpeed` | `float` | Degrees per second |

### Ammo

| Field | Type | Description |
|-------|------|-------------|
| `MaxAmmo` | `int` | Maximum ammunition capacity |
| `AmmoType` | `AmmoType` | AP (Armor Piercing), HE (High Explosive), SAP (Semi-Armor Piercing) |

### Crew Efficiency Methods

```csharp
public float GetEffectiveDamage(CrewCard crew, int shipTier)
{
    if (crew == null)
        return Damage * 0.5f; // No crew = 50% efficiency

    float crewEfficiency = crew.GetTotalEfficiency(shipTier);
    return Damage * crewEfficiency;
}

public float GetEffectiveReloadTime(CrewCard crew, int shipTier)
{
    if (crew == null)
        return ReloadTime * 2.0f; // No crew = 2x slower

    float crewEfficiency = crew.GetTotalEfficiency(shipTier);
    return ReloadTime / crewEfficiency;
}
```

**Design Intent**:
- Higher level crew = more damage output
- Higher level crew = faster reload times
- No crew = 50% damage, 2x slower reload (emergency operation)

### Inventory Size

Turrets occupy **3×2 grid cells** in inventory (large equipment).

## TurretType Enum

```csharp
public enum TurretType
{
    Main,           // Main battery (large caliber guns)
    Secondary,      // Secondary battery (medium guns)
    AA              // Anti-aircraft guns
}
```

## AmmoType Enum

```csharp
public enum AmmoType
{
    AP,   // Armor Piercing - high penetration, low damage
    HE,   // High Explosive - high damage, low penetration
    SAP   // Semi-Armor Piercing - balanced
}
```

## EngineEquipment Class

### Purpose
Propulsion systems that determine ship speed and acceleration.

### Engine Specifications

| Field | Type | Description |
|-------|------|-------------|
| `EngineType` | `EngineType` | Steam, Diesel, Turbine, Nuclear |

### Performance Stats

| Field | Type | Description |
|-------|------|-------------|
| `SpeedBoost` | `float` | Speed multiplier (e.g., 1.5 = +50% speed) |
| `AccelerationBoost` | `float` | Acceleration multiplier |
| `FuelEfficiency` | `float` | Fuel consumption multiplier (lower = better) |
| `Horsepower` | `int` | Engine power rating |

### Reliability

| Field | Type | Description |
|-------|------|-------------|
| `Durability` | `float` | Engine health/durability |
| `MaintenanceCost` | `float` | Credits per hour of operation |

### Crew Efficiency Method

```csharp
public float GetEffectiveSpeedBoost(CrewCard crew, int shipTier)
{
    if (crew == null)
        return SpeedBoost * 0.6f; // No engineer = 60% efficiency

    float crewEfficiency = crew.GetTotalEfficiency(shipTier);
    return SpeedBoost * crewEfficiency;
}
```

**Design Intent**:
- Engineers improve engine performance
- No engineer = 60% speed (emergency operation possible)

### Inventory Size

Engines occupy **4×3 grid cells** in inventory (very large equipment).

## EngineType Enum

```csharp
public enum EngineType
{
    Steam,      // Early tiers (T1-T3)
    Diesel,     // Mid tiers (T3-T5)
    Turbine,    // High tiers (T5-T7)
    Nuclear     // Special (T7+)
}
```

**Historical Progression**: Reflects real naval engine technology advancement.

## ModuleEquipment Class

### Purpose
Utility systems that provide bonuses (Fire Control, Damage Control, Radar, Sonar).

### Module Specifications

| Field | Type | Description |
|-------|------|-------------|
| `ModuleType` | `ModuleType` | FireControl, DamageControl, Radar, Sonar, Communications |

### Effect Stats

| Field | Type | Description |
|-------|------|-------------|
| `EffectValue` | `float` | Module-specific effect value (e.g., +15% accuracy) |
| `EffectDescription` | `string` | Human-readable effect description |

### Module Properties

| Field | Type | Description |
|-------|------|-------------|
| `RequiresPower` | `bool` | Does module require engine power? |
| `PowerConsumption` | `float` | Power draw from engines |

### Crew Efficiency Method

```csharp
public float GetEffectiveBonus(CrewCard crew, int shipTier)
{
    if (crew == null)
        return EffectValue * 0.7f; // No crew = 70% efficiency

    float crewEfficiency = crew.GetTotalEfficiency(shipTier);
    return EffectValue * crewEfficiency;
}
```

**Design Intent**:
- Fire Control crew improves module effectiveness
- No crew = 70% effectiveness (better than turrets/engines)

### Inventory Size

Modules occupy **2×2 grid cells** in inventory (medium-sized equipment).

## ModuleType Enum

```csharp
public enum ModuleType
{
    FireControl,        // Improves turret accuracy
    DamageControl,      // Reduces damage from hits
    Radar,              // Detection range
    Sonar,              // Underwater detection
    Communications      // Party coordination bonus
}
```

## EquipmentPricing (Static Helper)

### Turret Pricing

```csharp
public static long CalculateTurretPrice(int tier, int caliber, TurretType type)
{
    long basePrice = 0;

    switch (type)
    {
        case TurretType.Main:
            basePrice = 5000;
            break;
        case TurretType.Secondary:
            basePrice = 3000;
            break;
        case TurretType.AA:
            basePrice = 2000;
            break;
    }

    float tierMultiplier = Mathf.Pow(tier, 2.5f); // T1=1x, T5=55x, T7=146x
    float caliberMultiplier = caliber / 100f;      // Larger guns = more expensive

    return (long)(basePrice * tierMultiplier * caliberMultiplier);
}
```

**Formula**: `Base Price × Tier Multiplier × Caliber Multiplier`

| Tier | Caliber | Type | Calculation | Price |
|------|---------|------|-------------|-------|
| T1 | 203mm | Main | `5000 × 1 × 2.03` | ₡10,150 |
| T5 | 406mm | Main | `5000 × 55 × 4.06` | ₡1,116,500 |
| T7 | 460mm | Main | `5000 × 146 × 4.60` | ₡3,358,000 |

### Engine Pricing

```csharp
public static long CalculateEnginePrice(int tier, int horsepower)
{
    long basePrice = 3000;
    float tierMultiplier = Mathf.Pow(tier, 2.5f);
    float horsepowerMultiplier = horsepower / 1000f;

    return (long)(basePrice * tierMultiplier * horsepowerMultiplier);
}
```

### Module Pricing

```csharp
public static long CalculateModulePrice(int tier, float effectValue)
{
    long basePrice = 10000;
    float tierMultiplier = Mathf.Pow(tier, 2.0f);
    float effectMultiplier = effectValue / 10f;

    return (long)(basePrice * tierMultiplier * effectMultiplier);
}
```

### Sell Price

```csharp
public static long CalculateSellPrice(long buyPrice)
{
    return (long)(buyPrice * 0.6f); // 60% of buy price
}
```

## EquipmentDefinitionSO (ScriptableObject)

### Purpose
Defines equipment templates in Unity's asset system. Acts as item database for equipment shop and loot drops.

### Fields

| Field | Type | Description |
|-------|------|-------------|
| `Type` | `EquipmentType` | Equipment type (Turret, Engine, Module) |
| `TurretData` | `TurretEquipment` | Turret template (if Type = Turret) |
| `EngineData` | `EngineEquipment` | Engine template (if Type = Engine) |
| `ModuleData` | `ModuleEquipment` | Module template (if Type = Module) |

### CreateInstance Method

```csharp
public EquipmentItem CreateInstance()
{
    switch (Type)
    {
        case EquipmentType.Turret:
            var turret = new TurretEquipment();
            CopyDataToInstance(turret, TurretData);
            return turret;

        case EquipmentType.Engine:
            var engine = new EngineEquipment();
            CopyDataToInstance(engine, EngineData);
            return engine;

        case EquipmentType.Module:
            var module = new ModuleEquipment();
            CopyDataToInstance(module, ModuleData);
            return module;

        default:
            return null;
    }
}
```

**Purpose**: Create a new equipment instance from ScriptableObject template. Automatically generates unique `ItemId` for each instance.

**Usage**:
```csharp
EquipmentDefinitionSO definition = Resources.Load<EquipmentDefinitionSO>("Items/T5_16inch_Triple");
TurretEquipment turret = (TurretEquipment)definition.CreateInstance();
// turret.ItemId = "new-uuid-123" (unique instance)
```

## Usage Examples

### Creating Equipment from Definition

```csharp
// Load ScriptableObject template
EquipmentDefinitionSO turretDef = Resources.Load<EquipmentDefinitionSO>("Items/MainBattery_T5_16inch");

// Create instance
TurretEquipment turret = (TurretEquipment)turretDef.CreateInstance();

// Equipment is ready to use
Debug.Log($"Created: {turret.DisplayName}");
Debug.Log($"Damage: {turret.Damage}, Range: {turret.Range}m");
Debug.Log($"Price: ₡{turret.BuyPrice:N0}");
```

### Calculating Effective Performance

```csharp
// Get turret and assigned crew
TurretEquipment mainBattery = GetMainBattery();
CrewCard gunner = GetAssignedGunner();

// Calculate effective stats with crew efficiency
float effectiveDamage = mainBattery.GetEffectiveDamage(gunner, shipTier: 5);
float effectiveReload = mainBattery.GetEffectiveReloadTime(gunner, shipTier: 5);

Debug.Log($"Base damage: {mainBattery.Damage}");
Debug.Log($"Effective damage: {effectiveDamage}");
Debug.Log($"Reload time: {effectiveReload}s (base: {mainBattery.ReloadTime}s)");

// Level 120 crew on T5 equipment:
// effectiveDamage = 1000 × 1.4 = 1400 (40% bonus)
// effectiveReload = 30s / 1.4 = 21.4s (faster reload)
```

### Validating Crew Assignment

```csharp
TurretEquipment turret = GetTurretEquipment();
CrewCard crew = GetCrewCard();

if (!turret.CanBeOperatedBy(crew))
{
    if (crew.Classification != turret.RequiredCrewType)
    {
        Debug.LogError($"Wrong crew type: needs {turret.RequiredCrewType}, got {crew.Classification}");
    }
    else if (crew.CurrentLevel < turret.RequiredCrewLevel)
    {
        Debug.LogError($"Crew level too low: needs {turret.RequiredCrewLevel}, got {crew.CurrentLevel}");
    }
}
```

### Equipment Pricing

```csharp
// Calculate turret price
long turretPrice = EquipmentPricing.CalculateTurretPrice(
    tier: 5,
    caliber: 406,
    type: TurretType.Main
);
Debug.Log($"T5 16-inch triple turret: ₡{turretPrice:N0}");

// Calculate sell price
long sellPrice = EquipmentPricing.CalculateSellPrice(turretPrice);
Debug.Log($"Sell for: ₡{sellPrice:N0}");
```

## Integration Points

### Related Systems

| System | Integration |
|--------|-------------|
| **ItemDatabaseSO** | Stores all equipment definitions as ScriptableObjects |
| **ShipLoadout** | Equipment installed in ship slots (TurretMount, EngineSlot, ModuleSlot) |
| **CargoGrid** | Equipment stored in inventory as `ItemData` |
| **CrewCard** | Crew efficiency affects equipment performance |
| **ShipEquipmentManager** | Handles equipment installation/uninstallation |

### Data Flow

```
EquipmentDefinitionSO (ScriptableObject)
    ↓ CreateInstance()
EquipmentItem instance (runtime object)
    ↓ Store in CargoGrid
ItemData (inventory item)
    ↓ Install to ship
ShipLoadout slot (equipment reference)
    ↓ Combat
GetEffectiveDamage/Reload (crew efficiency applied)
```

## Design Notes

### Equipment Type Specialization

Each equipment type has unique characteristics:
- **Turrets**: Offensive power, most affected by crew skill
- **Engines**: Performance, less crew-dependent (60% base efficiency)
- **Modules**: Utility bonuses, moderate crew-dependence (70% base efficiency)

### Crew Efficiency Philosophy

Equipment performs **better with higher level crew**, but can still function without crew:
- **No crew penalty**: Equipment still works at reduced efficiency
- **Crew bonus scaling**: ±2% per level difference from equipment tier
- **Efficiency caps**: 20% minimum, 200% maximum

This design:
1. Prevents total equipment failure (player frustration)
2. Rewards crew investment (progression incentive)
3. Creates strategic depth (crew assignment optimization)

### Inventory Grid Sizes

Equipment has different grid sizes based on physical size:

| Equipment Type | Grid Size | Reasoning |
|----------------|-----------|-----------|
| Turret | 3×2 (6 cells) | Large gun mechanisms |
| Engine | 4×3 (12 cells) | Massive propulsion machinery |
| Module | 2×2 (4 cells) | Electronic/utility systems |

This creates **spatial inventory puzzle** gameplay (Resident Evil 4 style).

### Tier-Based Pricing Curve

Pricing uses **exponential tier multiplier** to create dramatic cost increases:
- **Turrets**: `tier^2.5` (T5 is 55x more expensive than T1)
- **Engines**: `tier^2.5` (same curve as turrets)
- **Modules**: `tier^2.0` (slightly less expensive scaling)

This ensures:
1. Higher tier equipment is **aspirational** (long-term goals)
2. Players can't skip tiers (progression gating)
3. Economy remains balanced across tiers

### ScriptableObject Pattern

Using `EquipmentDefinitionSO` enables:
1. **Designer-friendly**: Edit equipment in Unity Inspector
2. **Asset database**: All equipment lives in Resources folder
3. **Instance creation**: Generate unique runtime instances
4. **Mod support**: Community can add equipment via asset bundles

### Crew Type Matching

Equipment requires **specific crew classifications**:
- Turrets → Gunner/AAGunner
- Engines → Engineer
- Modules → FireControl/DamageControl

This creates **crew management depth**:
- Must recruit diverse crew types
- Can't use Level 200 Gunner for everything
- Specialization vs. flexibility tradeoffs

### Effect Value Abstraction

Modules use **EffectValue** as abstract bonus:
- Fire Control: +15% accuracy (EffectValue = 15)
- Damage Control: -20% damage taken (EffectValue = 20)
- Radar: +5000m detection range (EffectValue = 5000)

Each module type interprets `EffectValue` differently based on its function.

### Power System (Future)

Modules have `RequiresPower` and `PowerConsumption` fields for future power management system:
- Engines generate power based on horsepower
- Modules consume power when active
- Overloading electrical system = performance penalties

Currently unused but designed for future expansion.

### Torpedo System Note

The file defines `TorpedoType` enum (Surface, Submarine, Aerial) but the actual `TorpedoEquipment` class is defined separately in `TorpedoDefinitionSO.cs`. This suggests a refactoring opportunity to consolidate torpedo data.
