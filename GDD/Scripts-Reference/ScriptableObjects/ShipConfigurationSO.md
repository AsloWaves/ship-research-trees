# ShipConfigurationSO

**DEPRECATED - Use ShipDefinitionSO Instead**

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Ships/ShipConfigurationSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Ships` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | 527 |
| **Architecture** | Configuration-Driven Design |
| **Status** | Obsolete - Replaced by `WOS.Ships.ScriptableObjects.ShipDefinitionSO` |

---

## Purpose

**DEPRECATED LEGACY SYSTEM**: This ScriptableObject defined ship configurations for Tiers 1-7 only. It has been replaced by the new `ShipDefinitionSO` system which supports:

- ✅ T8-T10 tier support
- ✅ 9-zone Navy Field armor system
- ✅ Firing arc definitions
- ✅ Permadeath risk calculations
- ✅ Aircraft carrier support

This class will be removed in a future version. Use `ShipDefinitionSO` from the `WOS.Ships.ScriptableObjects` namespace instead.

---

## Ship Identity

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `shipClassId` | `string` | - | Auto-generated | Unique ship class ID (e.g., 'T5_Battleship_Japan') |
| `shipName` | `string` | - | Auto-generated | Display name shown to players |
| `description` | `string` | - | Empty | Ship description and historical background |

---

## Classification

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `shipTier` | `int` | 1-7 | 1 | Ship tier determines available equipment tier ranges |
| `shipType` | `ShipType` | Enum | `Destroyer` | Ship type classification (Destroyer, Cruiser, Battleship, etc.) |
| `nation` | `Nation` | Enum | `USA` | Nation/faction (USA, Japan, Britain, Germany, Russia, France, Italy, China) |

### ShipType Enum
- **Destroyer**: Fast, agile, light armor
- **LightCruiser**: Balanced speed and firepower
- **HeavyCruiser**: Heavy guns, moderate speed
- **Battlecruiser**: Fast battleship, lighter armor
- **Battleship**: Heavy armor, big guns, slow
- **AircraftCarrier**: Air support, vulnerable
- **Submarine**: Stealth, torpedoes

---

## Physical Stats

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `displacement` | `float` | 500-100,000 tons | 5,000 | Ship displacement in tons (affects weight calculations) |
| `maxCargoCapacity` | `float` | 100-50,000 tons | 2,000 | Maximum cargo capacity in tons |
| `cargoGridSize` | `Vector2Int` | - | (20, 15) | Cargo grid dimensions (width x height) for Tetris-style inventory |

---

## Performance Stats

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `maxSpeed` | `float` | 10-50 knots | 30 | Maximum speed in knots |
| `acceleration` | `float` | 0.5-5 knots/sec | 2 | Acceleration rate (knots per second) |
| `turningRadius` | `float` | 100-2,000 meters | 500 | Turning radius in meters |
| `stoppingDistance` | `float` | 200-5,000 meters | 1,000 | Stopping distance in meters |

---

## Durability

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `maxHitPoints` | `int` | 1,000-100,000 | 10,000 | Maximum hit points |
| `armorThickness` | `int` | 10-500 | 100 | Armor thickness (affects damage reduction) |

---

## Equipment Slots

### Turret Slots
**Type**: `List<TurretSlotDefinition>`

Each turret slot defines:
- `slotId`: Unique slot ID (e.g., 'MainBattery1', 'SecondaryPort1')
- `allowedType`: Allowed turret type (Main, Secondary, AA)
- `minTier`/`maxTier`: Tier restrictions (1-7)
- `maxWeightTons`: Maximum weight this mount can support (1-500 tons)
- `mountPosition`: Position on ship for visuals
- `isRequired`: Whether required to operate ship

### Engine Slots
**Type**: `List<EngineSlotDefinition>`

Each engine slot defines:
- `slotId`: Unique slot ID (e.g., 'EngineBay1', 'BoilerRoom1')
- `allowedType`: Engine type (Any, Diesel, Turbine, Steam, Nuclear, Hybrid)
- `minTier`/`maxTier`: Tier restrictions (1-7)
- `maxWeightTons`: Maximum weight (1-1,000 tons)
- `isRequired`: Always true for engines

### Module Slots
**Type**: `List<ModuleSlotDefinition>`

Each module slot defines:
- `slotId`: Unique slot ID (e.g., 'FireControl1', 'Radar1')
- `allowedType`: Module type (Any, FireControl, DamageControl, Radar, Sonar, Communications)
- `minTier`/`maxTier`: Tier restrictions (1-7)
- `maxWeightTons`: Maximum weight (1-200 tons)
- `isRequired`: Usually false (optional equipment)

---

## Crew Configuration

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `crewPositions` | `List<CrewPositionDefinition>` | - | Empty | Crew position definitions |
| `totalCrewCapacity` | `int` | 50-3,000 | 500 | Total crew capacity |

### CrewPositionDefinition
- `positionId`: Unique position ID (e.g., 'GunCrew1', 'Engineering1')
- `classification`: Required crew classification (Gunner, Navigator, Engineer, etc.)
- `minLevel`: Minimum crew level required (1-200)
- `isRequired`: Whether required to operate ship

---

## Economy

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `purchasePrice` | `int` | 10,000-10,000,000 | 100,000 | Purchase price in credits |
| `sellPriceMultiplier` | `float` | 0.0-1.0 | 0.6 | Sell price multiplier (60% of purchase price) |
| `dailyMaintenanceCost` | `int` | 100-50,000 | 1,000 | Daily maintenance cost (auto-calculated as 1% of purchase price) |

---

## Visual & Prefabs

| Property | Type | Description |
|----------|------|-------------|
| `shipIcon` | `Sprite` | Ship icon for UI |
| `shipPreview` | `Sprite` | Ship preview image |
| `shipPrefab` | `GameObject` | Ship prefab for spawning |

---

## Key Methods

### Equipment Tier Range
```csharp
public (int min, int max) GetEquipmentTierRange()
```
Returns allowed equipment tier range based on ship tier. Ships can use equipment ±1 tier from ship tier.

**Example**: Tier 5 ship → equipment tier range (4, 6)

### Total Equipment Slots
```csharp
public int GetTotalEquipmentSlots()
```
Calculate total slot count across turrets, engines, and modules.

### Sell Price
```csharp
public int GetSellPrice()
```
Get ship sell price based on purchase price × sell price multiplier.

### Weight Penalty Threshold
```csharp
public float GetWeightPenaltyThreshold()
```
Performance degrades when cargo weight exceeds 80% of max capacity.

### Create UI Ship Loadout
```csharp
public ShipLoadout CreateUIShipLoadout()
```
Creates a UI ShipLoadout with empty slots based on ship configuration. Used by EquipmentPanel to initialize loadout structure.

Creates:
- Turret mount slots (one per turret slot)
- Engine slots (one per engine slot)
- Module slots (one per module slot)
- Bridge slots (for Captain, Navigator positions)

### Validate Configuration
```csharp
[ContextMenu("Validate Ship Configuration")]
public void ValidateConfiguration()
```
Validates ship configuration and logs errors/warnings:
- Checks for empty shipClassId
- Checks for missing equipment slots
- Checks for duplicate slot IDs
- Checks for missing prefab/icon

---

## Tier-Based Auto-Constraints (OnValidate)

### Tier 1: Small Destroyers
- Displacement: 500-2,000 tons
- Hit Points: 1,000-5,000
- Max Speed: 25-40 knots
- Purchase Price: 10,000-50,000 credits

### Tier 3: Light Cruisers
- Displacement: 3,000-8,000 tons
- Hit Points: 5,000-15,000
- Max Speed: 25-35 knots
- Purchase Price: 50,000-200,000 credits

### Tier 5: Battleships
- Displacement: 20,000-50,000 tons
- Hit Points: 30,000-70,000
- Max Speed: 20-30 knots
- Purchase Price: 500,000-2,000,000 credits

### Tier 7: Super Battleships
- Displacement: 50,000-100,000 tons
- Hit Points: 70,000-100,000
- Max Speed: 15-28 knots
- Purchase Price: 2,000,000-10,000,000 credits

### Auto-Generated Values
- `shipClassId`: Auto-generated as `T{tier}_{shipType}_{nation}` if empty
- `shipName`: Auto-generated as `{nation} {shipType} (Tier {tier})` if empty
- `totalCrewCapacity`: Auto-calculated based on displacement (displacement / 10)
- `maxCargoCapacity`: Auto-clamped to 10%-50% of displacement
- `dailyMaintenanceCost`: Auto-calculated as 1% of purchase price

---

## Usage Example

```csharp
// Create via Unity menu: Create > WOS/Ships/DEPRECATED - Ship Configuration
// This will create a ShipConfigurationSO asset

// Access in code
ShipConfigurationSO shipConfig = // reference from Inspector or database

// Get equipment tier range
var (minTier, maxTier) = shipConfig.GetEquipmentTierRange();
Debug.Log($"Ship can use equipment from tier {minTier} to {maxTier}");

// Check weight penalty
float cargoWeight = 1500f;
if (cargoWeight > shipConfig.GetWeightPenaltyThreshold())
{
    Debug.Log("Warning: Cargo weight exceeds optimal threshold!");
}

// Create UI loadout structure
var loadout = shipConfig.CreateUIShipLoadout();
Debug.Log($"Ship has {loadout.TurretMounts.Count} turret mounts");
```

---

## Integration Points

### Used By
- ❌ **DEPRECATED**: Use `ShipDefinitionSO` instead
- `EquipmentPanel.cs` - Creates UI loadout structure (legacy support only)
- `PlayerShipManager.cs` - Ship configuration loading (legacy support only)

### Related Systems
- **ShipDefinitionSO** (WOS.Ships.ScriptableObjects) - **NEW CANONICAL SYSTEM**
- **EquipmentDefinitionSO** - Equipment definitions
- **CrewTemplateSO** - Crew templates
- **ShipLoadout** (UI.Inventory) - UI representation of ship loadout

---

## Design Notes

### Why Deprecated?

This system was designed for the initial T1-T7 tier range and basic equipment slots. The new `ShipDefinitionSO` system provides:

1. **Extended Tier Support**: T8-T10 for late-game progression
2. **Advanced Armor System**: 9-zone Navy Field armor model with penetration mechanics
3. **Firing Arcs**: Turret positioning with realistic firing arc constraints
4. **Carrier Support**: Aircraft carrier systems with hangar bays and squadrons
5. **Permadeath Integration**: Risk calculation for hardcore mode
6. **Better Performance**: Optimized data structures for large ship counts

### Migration Path

1. Create new `ShipDefinitionSO` assets to replace `ShipConfigurationSO` instances
2. Update ship spawning and management code to use `ShipDefinitionSO`
3. Remove references to `ShipConfigurationSO`
4. This legacy class will be deleted in future version

### Historical Context

This was the original ship configuration system designed for the MVP version of the game. As the game evolved to include more sophisticated naval combat mechanics (armor penetration, firing arcs, aircraft carriers), a more comprehensive system was needed.

---

## Create via Unity Menu

**Path**: `Create > WOS > Ships > DEPRECATED - Ship Configuration`

**Order**: 999 (de-prioritized due to deprecated status)

**Warning**: Creating new assets from this template is not recommended. Use `ShipDefinitionSO` instead.
