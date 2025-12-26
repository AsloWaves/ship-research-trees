# PlayerShipData.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/Data/PlayerShipData.cs` |
| **Namespace** | `WOS.Player.Data` |
| **Inheritance** | None (Serializable data class) |
| **Lines of Code** | 194 |
| **Architecture** | Data model for multi-ship ownership system |

## Purpose

`PlayerShipData` represents a single ship owned by a player in the naval MMO. It encapsulates ship identity, equipment loadout, per-ship cargo inventory, and operational status. This class maps directly to the `player_ships` database table and enables the multi-ship ownership system where players can own multiple ships but only have one active at a time.

The companion class `PlayerShipCollection` manages the list of all ships owned by a player, providing utilities for active ship selection and ship filtering.

## Data Structure

### Ship Identity

| Field | Type | Description |
|-------|------|-------------|
| `ShipId` | `string` | Unique UUID from database |
| `PlayerId` | `string` | Owner's player ID |
| `ShipClassId` | `string` | References `ShipDefinitionSO` asset (e.g., "T1_Destroyer_USA") |
| `ShipName` | `string` | Custom player-defined name |
| `ActiveShip` | `bool` | Only one ship can be active at a time |

### Equipment & Inventory

| Field | Type | Description |
|-------|------|-------------|
| `Loadout` | `ShipLoadout` | Turrets, engines, modules, crew assignments |
| `ShipCargo` | `CargoGrid` | Per-ship Tetris-style inventory |

### Metadata

| Field | Type | Description |
|-------|------|-------------|
| `CreatedAt` | `DateTime` | Ship creation timestamp |
| `UpdatedAt` | `DateTime` | Last modification timestamp |

## Key Methods

### Weight Calculation

```csharp
public float GetTotalWeight()
{
    float totalWeight = 0f;

    // Cargo weight from ship's cargo hold
    totalWeight += ShipCargo.GetTotalWeight();

    // Equipment weight from loadout
    totalWeight += Loadout.GetEquipmentWeight();

    // Crew weight from assigned crew
    totalWeight += Loadout.GetCrewWeight();

    return totalWeight;
}
```

**Purpose**: Calculate total weight of all equipment + cargo + crew on the ship. Used for performance calculations and displacement validation against `ShipDefinitionSO` limits.

### Operational Validation

```csharp
public bool IsOperational(out string reason)
{
    // Check for engine
    if (Loadout.Engines == null || Loadout.Engines.Count == 0 ||
        Loadout.Engines.TrueForAll(e => string.IsNullOrEmpty(e.EquipmentItemId)))
    {
        reason = "Ship requires at least one engine installed.";
        return false;
    }

    // Check for minimum crew (engineer for engine)
    bool hasEngineer = false;
    if (Loadout.Crew != null)
    {
        foreach (var crewAssignment in Loadout.Crew)
        {
            if (crewAssignment.Classification == CrewClassification.Engineer &&
                !string.IsNullOrEmpty(crewAssignment.CrewId))
            {
                hasEngineer = true;
                break;
            }
        }
    }

    if (!hasEngineer)
    {
        reason = "Ship requires at least one Engineer crew assigned to Engine Room.";
        return false;
    }

    reason = "Ship is operational.";
    return true;
}
```

**Purpose**: Validate that ship meets minimum operational requirements:
- Must have at least one engine installed
- Must have at least one Engineer crew assigned to engine room

**Returns**: `true` if operational, `false` if requirements not met (with reason in `out` parameter)

### Cargo Space Check

```csharp
public bool HasCargoSpace(ItemData item, int x, int y)
{
    return ShipCargo.CanPlaceItem(item, x, y);
}
```

**Purpose**: Check if ship has space in cargo hold for new item at specified grid position.

### Clone Operation

```csharp
public PlayerShipData Clone()
{
    return new PlayerShipData
    {
        ShipId = this.ShipId,
        PlayerId = this.PlayerId,
        ShipClassId = this.ShipClassId,
        ShipName = this.ShipName,
        ActiveShip = this.ActiveShip,
        Loadout = this.Loadout.Clone(),
        ShipCargo = this.ShipCargo.Clone(),
        CreatedAt = this.CreatedAt,
        UpdatedAt = this.UpdatedAt
    };
}
```

**Purpose**: Deep clone ship data for UI previews or undo functionality.

## PlayerShipCollection

### Purpose
Manages the list of all ships owned by a player. Provides utilities for active ship selection and filtering.

### Key Methods

```csharp
// Get the currently active ship
public PlayerShipData GetActiveShip()

// Get ship by ID
public PlayerShipData GetShipById(string shipId)

// Set a ship as active (deactivates all others)
public void SetActiveShip(string shipId)

// Get ships filtered by tier (e.g., "T1_", "T5_")
public List<PlayerShipData> GetShipsByTier(int tier)
```

## Constructors

### Default Constructor

```csharp
public PlayerShipData()
{
    ShipId = Guid.NewGuid().ToString();
    Loadout = new ShipLoadout();
    ShipCargo = new CargoGrid();
    ActiveShip = false;
    CreatedAt = DateTime.Now;
    UpdatedAt = DateTime.Now;
}
```

### Parameterized Constructor

```csharp
public PlayerShipData(string playerId, string shipClassId, string shipName)
{
    ShipId = Guid.NewGuid().ToString();
    PlayerId = playerId;
    ShipClassId = shipClassId;
    ShipName = shipName;
    ActiveShip = false;
    Loadout = new ShipLoadout();
    ShipCargo = new CargoGrid();
    CreatedAt = DateTime.Now;
    UpdatedAt = DateTime.Now;
}
```

## Usage Examples

### Creating a New Ship

```csharp
PlayerShipData newShip = new PlayerShipData(
    playerId: "player123",
    shipClassId: "T5_Battleship_USA",
    shipName: "USS Missouri"
);
```

### Checking Operational Status

```csharp
if (!ship.IsOperational(out string reason))
{
    Debug.LogWarning($"Ship cannot sail: {reason}");
    // Display UI warning to player
}
```

### Calculating Total Weight

```csharp
float totalWeight = ship.GetTotalWeight();
float maxWeight = shipDefinitionSO.MaxDisplacement;

if (totalWeight > maxWeight)
{
    Debug.LogError($"Ship overloaded: {totalWeight}/{maxWeight} tons");
}
```

### Managing Active Ship

```csharp
PlayerShipCollection collection = new PlayerShipCollection();

// Get current active ship
PlayerShipData activeShip = collection.GetActiveShip();

// Switch to different ship
collection.SetActiveShip("ship-uuid-456");

// Filter by tier
List<PlayerShipData> battleships = collection.GetShipsByTier(5);
```

## Integration Points

### Database Persistence
- **Table**: `player_ships`
- **Primary Key**: `ShipId` (UUID)
- **Foreign Key**: `PlayerId` references `players.player_id`
- **Persistence Service**: `PlayFabShipService` handles loading/saving ship collections

### Related Systems

| System | Integration |
|--------|-------------|
| **PlayerShipManager** | Manages ship creation, deletion, active ship selection |
| **ShipEquipmentManager** | Handles equipment installation/uninstallation to ship loadout |
| **CrewManager** | Manages crew assignments to ship positions |
| **NetworkedNavalController** | Reads active ship loadout for physics simulation |
| **ShipDefinitionSO** | ScriptableObject defining ship class properties (max displacement, slot counts) |

### Data Flow

```
PlayFab Database
    ↓ Load
PlayerShipManager (cache: playerShipCollections)
    ↓ Set Active Ship
ShipEquipmentManager + CrewManager (cache: playerActiveShips)
    ↓ Modify Loadout/Cargo
PlayerShipManager.SavePlayerShips()
    ↓ Save
PlayFab Database
```

## Design Notes

### Multi-Ship Ownership Architecture

The system supports players owning multiple ships, but only one can be **active** (currently piloted) at a time. Switching ships is restricted to port locations to prevent mid-ocean teleportation exploits.

**Active Ship Constraints**:
- Only one ship can have `ActiveShip = true` per player
- Active ship is loaded into memory for physics simulation
- Inactive ships are stored in database only
- Cannot delete active ship (must switch first)

### Weight System

Ships track three separate weight categories:
1. **Cargo Weight**: Items in `ShipCargo` grid
2. **Equipment Weight**: Turrets, engines, modules in `Loadout`
3. **Crew Weight**: Assigned crew cards (calculated from sailor count + level)

Total weight affects ship performance (speed, turning, acceleration) through `NetworkedNavalController`.

### Cargo Grid System

Each ship has its own **per-ship cargo hold** separate from the player's port inventory. This enables:
- Ships can carry cargo while sailing
- Equipment can be stored on ship when not installed
- Tetris-style spatial inventory with grid positioning
- Weight-based cargo limits (not just grid space)

### Operational Requirements

Ships have minimum requirements to be considered **operational**:
1. **At least one engine installed** in an engine slot
2. **At least one Engineer crew** assigned to engine room

These requirements are validated before allowing ship departure from port.

### Ship Class ID Format

Ship classes follow the naming convention: `T{tier}_{type}_{nation}`

Examples:
- `T1_Destroyer_USA` - Tier 1 US Destroyer
- `T5_Battleship_Japan` - Tier 5 Japanese Battleship
- `T7_Cruiser_Germany` - Tier 7 German Cruiser

This format enables:
- Easy tier extraction via string parsing
- Nation-based filtering
- Ship type categorization

### Database Mapping

The `PlayerShipData` class serializes to JSON and is stored in the `player_ships.equipment_loadout` JSONB column. This allows flexible schema evolution without database migrations.

**Key Fields**:
- `ship_id` (UUID, primary key)
- `player_id` (foreign key)
- `ship_class_id` (string)
- `ship_name` (string)
- `active_ship` (boolean)
- `equipment_loadout` (JSONB) - serialized `ShipLoadout`
- `ship_cargo` (JSONB) - serialized `CargoGrid`
- `created_at` (timestamp)
- `updated_at` (timestamp)

### Cloning Strategy

The `Clone()` method performs **deep cloning** of nested objects (`Loadout`, `ShipCargo`) to prevent unintended mutations when using ship data for UI previews or undo/redo systems.

Shallow cloning would create reference copies that share the same `Loadout` and `ShipCargo` objects, leading to bugs when modifying preview data.
