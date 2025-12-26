# PlayerShipManager.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/PlayerShipManager.cs` |
| **Namespace** | `WOS.Player` |
| **Inheritance** | `NetworkBehaviour` (Mirror networking) |
| **Lines of Code** | 800 |
| **Architecture** | Server-authoritative multi-ship ownership system |

## Purpose

`PlayerShipManager` handles the multi-ship ownership system where players can own multiple ships but only have one **active** (currently piloted) ship at a time. It manages ship creation, deletion, active ship selection, and coordinates with `ShipEquipmentManager` and `CrewManager` for complete ship management.

**Key Features**:
- Create/delete ships
- Set active ship (one per player)
- Ship collection persistence (PlayFab)
- Ship loadout initialization
- Port inventory management

## Singleton Pattern

```csharp
private static PlayerShipManager _instance;
public static PlayerShipManager Instance { get; }
```

**Lifecycle**: `DontDestroyOnLoad` - persists across scenes.

## Configuration

| Field | Type | Description |
|-------|------|-------------|
| `enableDebugLogs` | `bool` | Enable detailed debug logging |
| `shipPurchaseCost` | `long` | Base cost for T1 ships (₡50,000) |

## Server State

| Cache | Type | Description |
|-------|------|-------------|
| `playerShipCollections` | `Dictionary<string, PlayerShipCollection>` | Player ID → Ship collection |
| `portInventories` | `Dictionary<string, CargoGrid>` | Player ID → Port inventory |
| `shipCollectionVersions` | `Dictionary<string, int>` | Optimistic locking versions |
| `dirtyFlags` | `Dictionary<string, bool>` | Track unsaved changes |

## Multi-Ship Ownership System

### Create New Ship

```csharp
[Command(requiresAuthority = false)]
public void CmdCreateShip(string shipClassId, string shipName,
    NetworkConnectionToClient sender = null)
```

**Purpose**: Create a new ship for the player.

**Validation**:
- Ship name (max 100 characters)
- Player credits (TODO)
- Valid ship class ID

**Process**:
1. Create `PlayerShipData` with unique `ShipId`
2. Initialize loadout from `ShipDefinitionSO` (slots based on tier)
3. Create default cargo grid (10×10)
4. Set `ActiveShip = false` (new ships start inactive)
5. Add to player's ship collection
6. Save to PlayFab
7. Send result RPC to client

**Example**:
```csharp
CrewManager.Instance.CmdCreateShip(
    shipClassId: "T5_Battleship_USA",
    shipName: "USS Missouri"
);
```

### Initialize Ship Loadout

```csharp
[Server]
private void InitializeShipLoadout(PlayerShipData ship, string shipClassId)
{
    // TODO: Load ShipDefinitionSO asset
    // For now, create placeholder slots based on tier

    int tier = ExtractTierFromClassId(shipClassId);

    // Create turret slots (2 main battery)
    for (int i = 0; i < 2; i++)
    {
        ship.Loadout.Turrets.Add(new TurretMount
        {
            SlotId = $"MainBattery{i + 1}",
            AllowedType = TurretType.Main,
            MinTier = 1,
            MaxTier = tier + 1
        });
    }

    // Create engine slot
    ship.Loadout.Engines.Add(new EngineSlot
    {
        SlotId = "EngineRoom1",
        MinTier = 1,
        MaxTier = tier + 1
    });

    // Create module slots
    ship.Loadout.Modules.Add(new ModuleSlot
    {
        SlotId = "FireControl1",
        AllowedType = ModuleType.FireControl,
        MinTier = 1,
        MaxTier = tier + 1
    });

    // Create crew positions (tier-based count)
    int crewPositions = tier <= 3 ? 5 : tier <= 5 ? 10 : 15;
    for (int i = 0; i < crewPositions; i++)
    {
        ship.Loadout.Crew.Add(new CrewAssignment
        {
            PositionId = $"CrewPosition{i + 1}",
            Classification = CrewClassification.Gunner,
            MinLevel = 1
        });
    }
}
```

**Purpose**: Create slot structure based on ship tier.

**Future**: Load slot definitions from `ShipDefinitionSO` ScriptableObject.

## Active Ship Selection

### Set Active Ship

```csharp
[Command(requiresAuthority = false)]
public void CmdSetActiveShip(string shipId, NetworkConnectionToClient sender = null)
```

**Purpose**: Switch to a different ship (only allowed at port).

**Process**:
1. Find target ship in collection
2. Verify player is at port (TODO)
3. Deactivate current active ship
4. Unload from other managers (`ShipEquipmentManager`, `CrewManager`)
5. Activate target ship
6. Load into other managers
7. Save to PlayFab
8. Send result RPC to client

**Important**: Only one ship can be active per player.

### Get Active Ship

```csharp
[Server]
public PlayerShipData GetActiveShip(string playerId)
{
    if (playerShipCollections.TryGetValue(playerId, out var collection))
    {
        return collection.GetActiveShip();
    }
    return null;
}
```

**Purpose**: Query current active ship for a player.

## Ship Deletion

```csharp
[Command(requiresAuthority = false)]
public void CmdDeleteShip(string shipId, NetworkConnectionToClient sender = null)
```

**Purpose**: Delete a ship from player's collection.

**Restrictions**:
- Cannot delete active ship (must switch first)

**Process**:
1. Find ship in collection
2. Verify not active ship
3. Unassign all crew from this ship via `CrewManager`
4. Remove ship from collection
5. Save to PlayFab
6. Send result RPC to client

**Crew Safety**: All assigned crew are automatically unassigned before deletion to prevent orphaned crew.

## Ship List Query

```csharp
[Command(requiresAuthority = false)]
public void CmdRequestShipList(NetworkConnectionToClient sender = null)

[Server]
public List<PlayerShipData> GetPlayerShips(string playerId)
```

**Purpose**: Get list of all ships owned by player.

**Use Cases**:
- Ship selection UI
- Fleet management screen
- Statistics display

## PlayFab Persistence

### Save Ship Collection

```csharp
[Server]
private void SaveShipCollectionToPlayFab(string playerId)
{
    if (!dirtyFlags[playerId]) return;

    PlayerShipCollection collection = playerShipCollections[playerId];
    int currentVersion = shipCollectionVersions[playerId];

    playFabShipService.SaveShipCollection(playerId, collection, currentVersion,
        (newVersion, success) =>
    {
        if (success)
        {
            shipCollectionVersions[playerId] = newVersion;
            dirtyFlags[playerId] = false;
        }
    });
}
```

**Purpose**: Save ship collection to PlayFab with optimistic locking.

**Public Trigger**:
```csharp
[Server]
public void SavePlayerShips(string playerId)
{
    MarkDirty(playerId);
    SaveShipCollectionToPlayFab(playerId);
}
```

**Called By**: `ShipEquipmentManager` when loadout changes.

### Load Ship Collection

```csharp
[Server]
public void LoadShipCollectionFromPlayFab(string playerId,
    Action<PlayerShipCollection> callback = null)
{
    playFabShipService.LoadShipCollection(playerId, (collection, version, success) =>
    {
        if (success && collection != null)
        {
            playerShipCollections[playerId] = collection;
            shipCollectionVersions[playerId] = version;

            // Load active ship into other managers
            PlayerShipData activeShip = collection.GetActiveShip();
            if (activeShip != null)
            {
                shipEquipmentManager?.LoadPlayerActiveShip(playerId, activeShip);
                crewManager?.LoadPlayerActiveShip(playerId, activeShip);
            }

            callback?.Invoke(collection);
        }
    });
}
```

**Purpose**: Load ship collection from PlayFab on player connect.

## Public API

### Load Player Ship Collection

```csharp
[Server]
public void LoadPlayerShipCollection(string playerId,
    PlayerShipCollection collection, int version = 1)
```

**Purpose**: Load ship collection into cache.

**Called By**: `AccountManager` on player connect.

### Load Port Inventory

```csharp
[Server]
public void LoadPortInventory(string playerId, CargoGrid inventory)
{
    portInventories[playerId] = inventory;

    // Share with ShipEquipmentManager
    shipEquipmentManager?.LoadPortInventory(playerId, inventory);
}
```

**Purpose**: Cache player's port inventory for equipment installation.

### Unload Player Data

```csharp
[Server]
public void UnloadPlayerData(string playerId)
{
    // Save pending changes
    if (dirtyFlags[playerId])
    {
        SaveShipCollectionToPlayFab(playerId);
    }

    // Clean up caches
    playerShipCollections.Remove(playerId);
    portInventories.Remove(playerId);
    shipCollectionVersions.Remove(playerId);
    dirtyFlags.Remove(playerId);

    // Notify other managers
    shipEquipmentManager?.UnloadPlayerData(playerId);
    crewManager?.UnloadPlayerData(playerId);
}
```

**Purpose**: Clean up player data on disconnect.

**Called By**: `AccountManager`.

### Create Starting Ship

```csharp
[Server]
public IEnumerator CreateStartingShipCoroutine(string playerId)
{
    // Create T1 starting ship
    PlayerShipData startingShip = new PlayerShipData
    {
        ShipId = Guid.NewGuid().ToString(),
        PlayerId = playerId,
        ShipClassId = "T1_Destroyer_USA",
        ShipName = "USS Starter",
        ActiveShip = true,  // First ship is active by default
        Loadout = new ShipLoadout(),
        ShipCargo = new CargoGrid(10, 10)
    };

    InitializeShipLoadout(startingShip, "T1_Destroyer_USA");

    // Create collection
    PlayerShipCollection collection = new PlayerShipCollection
    {
        Ships = new List<PlayerShipData> { startingShip }
    };

    playerShipCollections[playerId] = collection;

    // Save to PlayFab
    bool saveComplete = false;
    playFabShipService.SaveShipCollection(playerId, collection, 0,
        (newVersion, success) =>
    {
        if (success)
        {
            shipCollectionVersions[playerId] = newVersion;
        }
        saveComplete = true;
    });

    yield return new WaitUntil(() => saveComplete);

    // Load into other managers
    shipEquipmentManager?.LoadPlayerActiveShip(playerId, startingShip);
    crewManager?.LoadPlayerActiveShip(playerId, startingShip);
}
```

**Purpose**: Create default starting ship for new players.

**Called By**: `AccountManager` after account creation.

**Starting Ship**:
- Class: T1 Destroyer (USA)
- Name: "USS Starter"
- Active: `true` (first ship)
- Loadout: Initialized with T1 slots
- Cargo: 10×10 grid

## Client RPC Responses

```csharp
[TargetRpc]
private void TargetRpcShipCreationResult(NetworkConnectionToClient conn,
    bool success, string message, string shipId)

[TargetRpc]
private void TargetRpcActiveShipResult(NetworkConnectionToClient conn,
    bool success, string message)

[TargetRpc]
private void TargetRpcShipDeletionResult(NetworkConnectionToClient conn,
    bool success, string message)

[TargetRpc]
private void TargetRpcShipListResult(NetworkConnectionToClient conn,
    List<PlayerShipData> ships)
```

## Integration Points

### Manager References

| Manager | Purpose |
|---------|---------|
| `AccountManager` | Player ID lookup |
| `ShipEquipmentManager` | Share active ship data |
| `CrewManager` | Share active ship data |
| `PlayFabShipService` | Save/load ship collections |

### Data Flow

```
Client: CmdCreateShip()
    ↓
Server: Create PlayerShipData
    ↓
Server: InitializeShipLoadout()
    ↓
Server: Add to PlayerShipCollection
    ↓
Server: SaveShipCollectionToPlayFab()
    ↓
PlayFab: Optimistic locking save
    ↓
Server: TargetRpcShipCreationResult()
    ↓
Client: Update UI
```

## Design Notes

### Active Ship Constraint

Only **one ship can be active** per player:
```csharp
foreach (var ship in collection.Ships)
{
    ship.ActiveShip = (ship.ShipId == targetShipId);
}
```

This prevents:
- Multiple ships spawned simultaneously
- Conflicting ship states
- Inventory duplication exploits

### Ship Switching Restrictions

**Future**: Restrict ship switching to ports only:
```csharp
// TODO: Verify player is at port
if (!IsPlayerAtPort(playerId))
{
    TargetRpcActiveShipResult(sender, false, "Must be at port to switch ships");
    return;
}
```

Prevents:
- Mid-ocean ship teleportation
- Combat exploits (switch to fresh ship mid-battle)

### Manager Coordination

When active ship changes, notify other managers:
```csharp
shipEquipmentManager?.LoadPlayerActiveShip(playerId, activeShip);
crewManager?.LoadPlayerActiveShip(playerId, activeShip);
```

This ensures:
- Equipment manager uses correct ship for installation
- Crew manager uses correct ship for assignments
- Single source of truth for active ship

### Tier Extraction

```csharp
private int ExtractTierFromClassId(string shipClassId)
{
    // Parse "T5_Battleship_Japan" → 5
    if (shipClassId.StartsWith("T") && shipClassId.Length > 1)
    {
        if (int.TryParse(shipClassId.Substring(1, 1), out int tier))
        {
            return tier;
        }
    }
    return 1; // Default to T1
}
```

**Format**: `T{tier}_{type}_{nation}`

### Placeholder Slot Initialization

Currently uses **hardcoded slot counts**:
```csharp
for (int i = 0; i < 2; i++)  // Always 2 turrets
{
    ship.Loadout.Turrets.Add(...);
}
```

**Production**: Should load from `ShipDefinitionSO`:
```csharp
ShipDefinitionSO definition = Resources.Load<ShipDefinitionSO>(shipClassId);
ship.Loadout.Turrets = definition.CreateTurretSlots();
```

### Crew Unassignment on Delete

Before deleting ship, unassign all crew:
```csharp
List<CrewCard> assignedCrew = crewManager.GetAssignedCrew(playerId, shipId);
foreach (CrewCard crew in assignedCrew)
{
    crew.IsAssigned = false;
    crew.AssignedShipId = null;
    crew.AssignedPosition = null;
}
```

Prevents orphaned crew that reference deleted ships.

### Port Inventory Sharing

Port inventory is shared with `ShipEquipmentManager`:
```csharp
shipEquipmentManager?.LoadPortInventory(playerId, inventory);
```

Both managers need access for:
- Equipment installation (from port to ship)
- Equipment uninstallation (from ship to port)

### Future Enhancements

1. **Ship purchase validation**: Check credits before creation
2. **Ship class unlocking**: Require research before purchasing
3. **Ship naming validation**: Profanity filter, uniqueness
4. **Ship customization**: Visual skins, paint schemes
5. **Ship repair costs**: Deduct credits for battle damage
6. **Ship selling**: Sell ships for partial refund
7. **Ship rental**: Temporary access to premium ships
8. **Port restrictions**: Ship switching only at ports
