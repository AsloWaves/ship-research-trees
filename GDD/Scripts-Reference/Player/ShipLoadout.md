# ShipLoadout.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/Data/ShipLoadout.cs` |
| **Namespace** | `WOS.Player.Data` |
| **Inheritance** | None (Serializable data classes) |
| **Lines of Code** | 375 |
| **Architecture** | Ship equipment slot system with crew assignments |

## Purpose

`ShipLoadout` defines the complete equipment configuration and crew assignments for a single ship. It manages:
- **Equipment slots**: Turrets, engines, modules (with tier restrictions)
- **Crew positions**: Crew card assignments to specific ship positions
- **Weight calculation**: Total weight of all installed equipment and assigned crew
- **Slot validation**: Check compatibility before installation

This data is stored as JSONB in the `player_ships.equipment_loadout` database column.

## ShipLoadout Class

### Equipment Slots

| Field | Type | Description |
|-------|------|-------------|
| `Turrets` | `List<TurretMount>` | Main battery, secondary battery, AA gun slots |
| `Engines` | `List<EngineSlot>` | Engine room slots |
| `Modules` | `List<ModuleSlot>` | Fire control, damage control, radar slots |

### Crew Assignments

| Field | Type | Description |
|-------|------|-------------|
| `Crew` | `List<CrewAssignment>` | Crew card assignments to ship positions |

## Key Methods

### Weight Calculation

```csharp
public float GetEquipmentWeight()
{
    float totalWeight = 0f;

    // Turret weight
    foreach (var turret in Turrets)
    {
        if (!string.IsNullOrEmpty(turret.EquipmentItemId))
            totalWeight += turret.EquipmentWeight;
    }

    // Engine weight
    foreach (var engine in Engines)
    {
        if (!string.IsNullOrEmpty(engine.EquipmentItemId))
            totalWeight += engine.EquipmentWeight;
    }

    // Module weight
    foreach (var module in Modules)
    {
        if (!string.IsNullOrEmpty(module.EquipmentItemId))
            totalWeight += module.EquipmentWeight;
    }

    return totalWeight;
}

public float GetCrewWeight()
{
    float totalWeight = 0f;

    foreach (var crewAssignment in Crew)
    {
        if (!string.IsNullOrEmpty(crewAssignment.CrewId))
            totalWeight += crewAssignment.CrewWeight;
    }

    return totalWeight;
}
```

**Purpose**: Calculate total weight of equipment and crew separately. Used for ship performance calculations.

### Slot Queries

```csharp
// Check if a slot is occupied
public bool IsSlotOccupied(string slotId)

// Check if crew position is occupied
public bool IsCrewPositionOccupied(string positionId)

// Get crew assignment for specific position
public CrewAssignment GetCrewAtPosition(string positionId)

// Get all equipped turrets (excluding empty slots)
public List<TurretMount> GetEquippedTurrets()
```

### Clone Operation

```csharp
public ShipLoadout Clone()
{
    return new ShipLoadout
    {
        Turrets = new List<TurretMount>(this.Turrets.Select(t => t.Clone())),
        Engines = new List<EngineSlot>(this.Engines.Select(e => e.Clone())),
        Modules = new List<ModuleSlot>(this.Modules.Select(m => m.Clone())),
        Crew = new List<CrewAssignment>(this.Crew.Select(c => c.Clone()))
    };
}
```

**Purpose**: Deep clone loadout for UI previews or undo functionality.

## TurretMount Class

### Purpose
Represents a turret mounting point on the ship with tier and type restrictions.

### Slot Definition

| Field | Type | Description |
|-------|------|-------------|
| `SlotId` | `string` | Unique ID (e.g., "MainBattery1", "AAGun3") |
| `AllowedType` | `TurretType` | Main, Secondary, or AA |
| `MinTier` | `int` | Minimum turret tier allowed |
| `MaxTier` | `int` | Maximum turret tier allowed |
| `MountPosition` | `Vector3` | 3D position on ship model |

### Equipped Item

| Field | Type | Description |
|-------|------|-------------|
| `EquipmentItemId` | `string` | Item ID from inventory (null if empty) |
| `EquipmentDefinitionId` | `string` | Definition ID (e.g., "MainBattery_T5_16inch") |
| `EquipmentWeight` | `float` | Weight of equipped turret (tons) |
| `EquipmentTier` | `int` | Tier of equipped turret (1-7) |

### Crew Requirement

| Field | Type | Description |
|-------|------|-------------|
| `RequiredCrewLevel` | `int` | Minimum crew level to operate |
| `AssignedCrewId` | `string` | Crew assigned to this turret (optional) |

### Validation

```csharp
public bool CanInstallEquipment(int equipmentTier, TurretType equipmentType)
{
    if (equipmentType != AllowedType)
        return false;

    if (equipmentTier < MinTier || equipmentTier > MaxTier)
        return false;

    return true;
}
```

## EngineSlot Class

### Purpose
Represents an engine room slot with tier restrictions.

### Slot Definition

| Field | Type | Description |
|-------|------|-------------|
| `SlotId` | `string` | Unique ID (e.g., "EngineRoom1") |
| `MinTier` | `int` | Minimum engine tier allowed |
| `MaxTier` | `int` | Maximum engine tier allowed |

### Equipped Item

| Field | Type | Description |
|-------|------|-------------|
| `EquipmentItemId` | `string` | Item ID from inventory |
| `EquipmentDefinitionId` | `string` | Definition ID (e.g., "Engine_T5_Turbine") |
| `EquipmentWeight` | `float` | Weight of equipped engine |
| `EquipmentTier` | `int` | Tier of equipped engine |

### Performance Boost

| Field | Type | Description |
|-------|------|-------------|
| `SpeedMultiplier` | `float` | Speed boost from engine (1.0 = base, 1.5 = +50%) |
| `AccelerationMultiplier` | `float` | Acceleration boost |

### Crew Requirement

| Field | Type | Description |
|-------|------|-------------|
| `RequiredCrewLevel` | `int` | Minimum engineer crew level |
| `AssignedCrewId` | `string` | Engineer crew assigned |

### Validation

```csharp
public bool CanInstallEquipment(int equipmentTier)
{
    return equipmentTier >= MinTier && equipmentTier <= MaxTier;
}
```

## ModuleSlot Class

### Purpose
Represents a module slot for utility systems (fire control, radar, etc.).

### Slot Definition

| Field | Type | Description |
|-------|------|-------------|
| `SlotId` | `string` | Unique ID (e.g., "FireControl1") |
| `AllowedType` | `ModuleType` | FireControl, DamageControl, Radar, Sonar, Communications |
| `MinTier` | `int` | Minimum module tier allowed |
| `MaxTier` | `int` | Maximum module tier allowed |

### Equipped Item

| Field | Type | Description |
|-------|------|-------------|
| `EquipmentItemId` | `string` | Item ID from inventory |
| `EquipmentDefinitionId` | `string` | Definition ID |
| `EquipmentWeight` | `float` | Weight of equipped module |
| `EquipmentTier` | `int` | Tier of equipped module |

### Module Effects

| Field | Type | Description |
|-------|------|-------------|
| `EffectValue` | `float` | Module-specific effect (e.g., +15% accuracy) |

### Crew Requirement

| Field | Type | Description |
|-------|------|-------------|
| `RequiredCrewLevel` | `int` | Minimum crew level |
| `AssignedCrewId` | `string` | Crew assigned to module |

### Validation

```csharp
public bool CanInstallEquipment(int equipmentTier, ModuleType equipmentType)
{
    if (equipmentType != AllowedType)
        return false;

    return equipmentTier >= MinTier && equipmentTier <= MaxTier;
}
```

## CrewAssignment Class

### Purpose
Links a crew card to a specific position on the ship.

### Assignment

| Field | Type | Description |
|-------|------|-------------|
| `PositionId` | `string` | Position on ship (e.g., "Main Battery 1", "Engine Room") |
| `CrewId` | `string` | UUID of assigned crew card (null if empty) |
| `Classification` | `CrewClassification` | Expected classification for this position |
| `MinLevel` | `int` | Minimum crew level required |

### Crew Stats (Cached)

| Field | Type | Description |
|-------|------|-------------|
| `CrewName` | `string` | Crew member name |
| `CrewLevel` | `int` | Current crew level |
| `CrewWeight` | `float` | Crew weight in tons |
| `CrewEfficiency` | `int` | Calculated efficiency percentage (0-100+) |

**Design Note**: Crew stats are **cached** in the assignment for performance. Must be updated when crew levels up or takes casualties.

## Enums

### TurretType

```csharp
public enum TurretType
{
    Main,           // Main battery (large caliber guns)
    Secondary,      // Secondary battery (medium guns)
    AA              // Anti-aircraft guns
}
```

### ModuleType

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

### CrewClassification

```csharp
public enum CrewClassification
{
    Gunner,             // Main/Secondary battery crew
    Engineer,           // Engine room crew
    Navigator,          // Navigation and helm
    DamageControl,      // Repair and firefighting
    FireControl,        // Fire control systems
    AAGunner            // Anti-aircraft gunners
}
```

## Usage Examples

### Creating a Loadout

```csharp
ShipLoadout loadout = new ShipLoadout();

// Add turret slots
loadout.Turrets.Add(new TurretMount
{
    SlotId = "MainBattery1",
    AllowedType = TurretType.Main,
    MinTier = 1,
    MaxTier = 5,
    MountPosition = new Vector3(0, 5, 10)
});

// Add engine slot
loadout.Engines.Add(new EngineSlot
{
    SlotId = "EngineRoom1",
    MinTier = 1,
    MaxTier = 5
});

// Add crew positions
loadout.Crew.Add(new CrewAssignment
{
    PositionId = "Gunnery1",
    Classification = CrewClassification.Gunner,
    MinLevel = 1
});
```

### Installing Equipment

```csharp
// Find slot
TurretMount slot = loadout.Turrets.Find(t => t.SlotId == "MainBattery1");

// Validate equipment
if (slot.CanInstallEquipment(equipmentTier: 5, TurretType.Main))
{
    // Install turret
    slot.EquipmentItemId = turret.ItemId;
    slot.EquipmentDefinitionId = turret.DefinitionId;
    slot.EquipmentWeight = turret.Weight;
    slot.EquipmentTier = turret.Tier;
}
```

### Assigning Crew

```csharp
// Find crew position
CrewAssignment position = loadout.GetCrewAtPosition("Gunnery1");

if (position != null && string.IsNullOrEmpty(position.CrewId))
{
    // Assign crew
    position.CrewId = crewCard.CrewId;
    position.CrewName = crewCard.CrewName;
    position.CrewLevel = crewCard.CurrentLevel;
    position.CrewWeight = crewCard.CrewWeight;
}
```

### Calculating Total Weight

```csharp
float equipmentWeight = loadout.GetEquipmentWeight();
float crewWeight = loadout.GetCrewWeight();
float totalWeight = equipmentWeight + crewWeight;

Debug.Log($"Equipment: {equipmentWeight} tons");
Debug.Log($"Crew: {crewWeight} tons");
Debug.Log($"Total: {totalWeight} tons");
```

## Integration Points

### Database Persistence
- **Storage**: JSONB column in `player_ships.equipment_loadout`
- **Serialization**: JSON serialization via Unity JsonUtility
- **Size**: Compact representation (IDs only, not full equipment data)

### Related Systems

| System | Integration |
|--------|-------------|
| **PlayerShipData** | Contains `ShipLoadout` as property |
| **ShipEquipmentManager** | Installs/uninstalls equipment to slots |
| **CrewManager** | Assigns/unassigns crew to positions |
| **NetworkedNavalController** | Reads loadout for physics calculations |
| **ShipDefinitionSO** | Defines valid slot configurations per ship class |

## Design Notes

### Slot-Based Architecture

The loadout uses a **slot-based system** where:
1. Ship has predefined slots (defined in `ShipDefinitionSO`)
2. Slots have tier restrictions (e.g., T1-T5 slot can't fit T7 equipment)
3. Slots have type restrictions (e.g., Main Battery slot can't fit AA guns)
4. Empty slots have `EquipmentItemId = null`

This prevents:
- Installing too many turrets (limited by slot count)
- Installing wrong equipment types (type validation)
- Power creep (tier restrictions)

### Crew Position System

Crew positions are **separate from equipment slots**:
- Equipment slots = physical mounting points
- Crew positions = job assignments

**Example**:
- `MainBattery1` (equipment slot) has a 16-inch triple turret installed
- `Gunnery1` (crew position) has Level 120 Gunner assigned
- Gunner operates all main battery turrets (not tied to specific turret)

This design:
1. Simplifies crew management (fewer positions than equipment slots)
2. Matches naval reality (gunnery division operates all main guns)
3. Allows flexible crew assignments

### Weight System

Equipment and crew weights are tracked **separately** but summed for total displacement:
```
Total Ship Weight = Base Hull Weight + Equipment Weight + Crew Weight + Cargo Weight
```

This enables:
- Performance penalties for overloading
- Strategic weight management
- Realistic naval engineering constraints

### Cached Crew Stats

`CrewAssignment` caches crew stats for performance:
```csharp
position.CrewName = crewCard.CrewName;
position.CrewLevel = crewCard.CurrentLevel;
position.CrewWeight = crewCard.CrewWeight;
```

**Trade-off**:
- **Pro**: Fast lookups without querying `CrewCard` every frame
- **Con**: Must manually sync when crew data changes (level-ups, casualties)

**Sync Points**:
- After crew levels up → update `CrewLevel` and `CrewWeight`
- After combat casualties → update `CrewWeight`
- When crew unassigned → clear all cached fields

### Tier Restrictions

Slots have **min/max tier ranges** to gate progression:

| Ship Tier | Main Battery Slot | Engine Slot |
|-----------|-------------------|-------------|
| T1 | T1-T2 | T1-T2 |
| T3 | T1-T4 | T1-T4 |
| T5 | T3-T6 | T3-T6 |
| T7 | T5-T7 | T5-T7 |

This ensures:
1. Can't install T7 equipment on T1 ship (overpowered)
2. Can install slightly higher tier equipment (upgrade path)
3. Old equipment becomes obsolete (progression incentive)

### Performance Multipliers

`EngineSlot` stores performance multipliers:
```csharp
public float SpeedMultiplier;        // 1.0 = base, 1.5 = +50%
public float AccelerationMultiplier;
```

These are **calculated from equipment stats** when engine is installed, then cached for physics system to use directly.

### Empty Slot Detection

Check if slot is empty: `string.IsNullOrEmpty(slot.EquipmentItemId)`

All slot types use this pattern for consistency:
```csharp
if (!string.IsNullOrEmpty(turret.EquipmentItemId))
{
    // Slot has equipment installed
}
```

### Future Enhancements

Potential additions:
1. **Slot groups**: Main battery group (all main guns fire together)
2. **Slot prerequisites**: Radar required for fire control module
3. **Slot bonuses**: Specific slot combinations grant bonuses
4. **Dynamic slots**: Convertible slots (main battery OR torpedo tubes)
5. **Slot upgrades**: Increase tier limits via research

### Clone Safety

The `Clone()` method performs **deep cloning** of all slot lists:
```csharp
Turrets = new List<TurretMount>(this.Turrets.Select(t => t.Clone()))
```

This prevents reference sharing bugs when using loadout data for:
- UI previews (show changes without committing)
- Undo/redo systems (restore previous state)
- Comparison systems (diff two loadouts)
