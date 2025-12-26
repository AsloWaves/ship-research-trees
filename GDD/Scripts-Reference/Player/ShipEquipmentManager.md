# ShipEquipmentManager.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/ShipEquipmentManager.cs` |
| **Namespace** | `WOS.Player` |
| **Inheritance** | `NetworkBehaviour` (Mirror networking) |
| **Lines of Code** | 607 |
| **Architecture** | Server-authoritative equipment installation/uninstallation system |

## Purpose

`ShipEquipmentManager` handles the installation and uninstallation of equipment (turrets, engines, modules) between port inventory and ship slots. It validates tier restrictions, type compatibility, and slot availability before allowing equipment changes.

**Key Features**:
- Install equipment from port inventory to ship slots
- Uninstall equipment from ship slots back to port inventory
- Validate tier and type restrictions
- Auto-find empty inventory space
- Coordinate with `PlayerShipManager` for persistence

## Singleton Pattern

```csharp
private static ShipEquipmentManager _instance;
public static ShipEquipmentManager Instance { get; }
```

**Access**: `ShipEquipmentManager.Instance.CmdInstallEquipment(...)`

## Configuration

| Field | Type | Description |
|-------|------|-------------|
| `enableDebugLogs` | `bool` | Enable detailed debug logging |

## Server State

| Cache | Type | Description |
|-------|------|-------------|
| `playerActiveShips` | `Dictionary<string, PlayerShipData>` | Player ID → Active ship data |
| `portInventories` | `Dictionary<string, CargoGrid>` | Player ID → Port inventory |

## Equipment Installation System

### Install Equipment

```csharp
[Command(requiresAuthority = false)]
public void CmdInstallEquipment(string slotId, string itemId,
    NetworkConnectionToClient sender = null)
```

**Purpose**: Install equipment from port inventory to ship slot.

**Validation**:
1. Player authentication
2. Active ship exists
3. Port inventory loaded
4. Equipment item exists in inventory
5. Item is equipment type
6. Slot compatibility (tier, type)

**Process**:
1. Find equipment item in port inventory
2. Validate item type (Turret/Engine/Module)
3. Find target slot on ship
4. Check slot compatibility via `CanInstallEquipment()`
5. Install equipment to slot
6. Remove item from port inventory
7. Save ship via `PlayerShipManager`
8. Send result RPC to client

**Example**:
```csharp
ShipEquipmentManager.Instance.CmdInstallEquipment(
    slotId: "MainBattery1",
    itemId: "turret-item-uuid-123"
);
```

### Install Turret

```csharp
[Server]
private bool InstallTurret(PlayerShipData ship, CargoGrid inventory,
    string slotId, ItemData equipmentItem, out string errorMessage)
{
    // Find turret slot
    TurretMount slot = ship.Loadout.Turrets.Find(t => t.SlotId == slotId);
    if (slot == null)
    {
        errorMessage = "Turret slot not found";
        return false;
    }

    // Check slot occupied
    if (!string.IsNullOrEmpty(slot.EquipmentItemId))
    {
        errorMessage = "Turret slot already occupied";
        return false;
    }

    // Validate tier and type
    if (!slot.CanInstallEquipment(equipmentItem.EquipmentTier,
        GetTurretType(equipmentItem.EquipmentSubType)))
    {
        errorMessage = $"Tier {equipmentItem.EquipmentTier} not compatible " +
            $"with slot (requires {slot.MinTier}-{slot.MaxTier}, type: {slot.AllowedType})";
        return false;
    }

    // Install turret
    slot.EquipmentItemId = equipmentItem.ItemId;
    slot.EquipmentDefinitionId = equipmentItem.EquipmentDefinitionId;
    slot.EquipmentWeight = equipmentItem.EquipmentWeight;
    slot.EquipmentTier = equipmentItem.EquipmentTier;

    return true;
}
```

**Purpose**: Validate and install turret to turret slot.

**Validation**:
- Slot exists
- Slot not already occupied
- Turret tier within slot range (e.g., T3-T6 slot can fit T5 turret)
- Turret type matches slot type (Main/Secondary/AA)

### Install Engine

```csharp
[Server]
private bool InstallEngine(PlayerShipData ship, CargoGrid inventory,
    string slotId, ItemData equipmentItem, out string errorMessage)
{
    // Similar validation to InstallTurret
    // Check tier restrictions only (no type restrictions for engines)

    EngineSlot slot = ship.Loadout.Engines.Find(e => e.SlotId == slotId);
    if (!slot.CanInstallEquipment(equipmentItem.EquipmentTier))
    {
        errorMessage = "Tier not compatible";
        return false;
    }

    // Install engine
    slot.EquipmentItemId = equipmentItem.ItemId;
    slot.EquipmentDefinitionId = equipmentItem.EquipmentDefinitionId;
    slot.EquipmentWeight = equipmentItem.EquipmentWeight;
    slot.EquipmentTier = equipmentItem.EquipmentTier;

    return true;
}
```

### Install Module

```csharp
[Server]
private bool InstallModule(PlayerShipData ship, CargoGrid inventory,
    string slotId, ItemData equipmentItem, out string errorMessage)
{
    // Validate tier AND type (like turrets)
    ModuleSlot slot = ship.Loadout.Modules.Find(m => m.SlotId == slotId);

    if (!slot.CanInstallEquipment(equipmentItem.EquipmentTier,
        GetModuleType(equipmentItem.EquipmentSubType)))
    {
        errorMessage = "Tier or type not compatible";
        return false;
    }

    // Install module
    slot.EquipmentItemId = equipmentItem.ItemId;
    slot.EquipmentDefinitionId = equipmentItem.EquipmentDefinitionId;
    slot.EquipmentWeight = equipmentItem.EquipmentWeight;
    slot.EquipmentTier = equipmentItem.EquipmentTier;

    return true;
}
```

## Equipment Uninstallation System

### Uninstall Equipment

```csharp
[Command(requiresAuthority = false)]
public void CmdUninstallEquipment(string slotId, string equipmentType,
    NetworkConnectionToClient sender = null)
```

**Purpose**: Uninstall equipment from ship slot back to port inventory.

**Process**:
1. Find slot on ship
2. Verify slot has equipment installed
3. Create `ItemData` for uninstalled equipment
4. Clear slot
5. Try to place item in port inventory
6. Save ship via `PlayerShipManager`
7. Send result RPC to client

**Inventory Space Check**: If port inventory is full, uninstall fails.

### Uninstall Turret

```csharp
[Server]
private bool UninstallTurret(PlayerShipData ship, string slotId,
    out ItemData uninstalledItem, out string errorMessage)
{
    TurretMount slot = ship.Loadout.Turrets.Find(t => t.SlotId == slotId);

    if (string.IsNullOrEmpty(slot.EquipmentItemId))
    {
        errorMessage = "Turret slot is empty";
        return false;
    }

    // Create item data for inventory
    uninstalledItem = new ItemData
    {
        ItemId = slot.EquipmentItemId,
        ItemType = "Turret",
        EquipmentDefinitionId = slot.EquipmentDefinitionId,
        EquipmentTier = slot.EquipmentTier,
        EquipmentWeight = slot.EquipmentWeight,
        EquipmentSubType = slot.AllowedType.ToString(),
        Quantity = 1,
        Size = new GridSize(3, 2)  // Turrets are 3x2 grid
    };

    // Clear slot
    slot.EquipmentItemId = null;
    slot.EquipmentDefinitionId = null;
    slot.EquipmentWeight = 0f;
    slot.EquipmentTier = 0;

    return true;
}
```

**Purpose**: Remove turret from slot and create inventory item.

**Grid Sizes**:
- Turrets: **3×2** (6 cells)
- Engines: **4×3** (12 cells)
- Modules: **2×2** (4 cells)

### Uninstall Engine

```csharp
[Server]
private bool UninstallEngine(PlayerShipData ship, string slotId,
    out ItemData uninstalledItem, out string errorMessage)
{
    // Similar to UninstallTurret
    // Creates ItemData with Size = new GridSize(4, 3)
}
```

### Uninstall Module

```csharp
[Server]
private bool UninstallModule(PlayerShipData ship, string slotId,
    out ItemData uninstalledItem, out string errorMessage)
{
    // Similar to UninstallTurret
    // Creates ItemData with Size = new GridSize(2, 2)
}
```

## Helper Methods

### Auto-Find Inventory Space

```csharp
[Server]
private bool TryPlaceItemInInventory(CargoGrid inventory, ItemData item)
{
    // Try to find empty space
    for (int y = 0; y < inventory.Height; y++)
    {
        for (int x = 0; x < inventory.Width; x++)
        {
            if (inventory.CanPlaceItem(item, x, y))
            {
                return inventory.PlaceItem(item, x, y);
            }
        }
    }

    return false;  // No space found
}
```

**Purpose**: Automatically find first available space in inventory grid.

**Algorithm**: Scan left-to-right, top-to-bottom for first valid placement.

### Type Conversion

```csharp
private TurretType GetTurretType(string typeString)
{
    if (Enum.TryParse<TurretType>(typeString, out TurretType result))
        return result;
    return TurretType.Main;  // Default
}

private ModuleType GetModuleType(string typeString)
{
    if (Enum.TryParse<ModuleType>(typeString, out ModuleType result))
        return result;
    return ModuleType.FireControl;  // Default
}
```

**Purpose**: Convert string types from `ItemData` to enum types for slot validation.

## Client RPC Responses

```csharp
[TargetRpc]
private void TargetRpcInstallResult(NetworkConnectionToClient conn,
    bool success, string message)

[TargetRpc]
private void TargetRpcUninstallResult(NetworkConnectionToClient conn,
    bool success, string message)
```

**Purpose**: Send operation results to client for UI feedback.

## Public API

### Load Player Active Ship

```csharp
[Server]
public void LoadPlayerActiveShip(string playerId, PlayerShipData ship)
{
    playerActiveShips[playerId] = ship;
}
```

**Purpose**: Cache player's active ship.

**Called By**: `PlayerShipManager` when active ship changes.

### Load Port Inventory

```csharp
[Server]
public void LoadPortInventory(string playerId, CargoGrid inventory)
{
    portInventories[playerId] = inventory;
}
```

**Purpose**: Cache player's port inventory.

**Called By**: `PlayerShipManager` when player docks at port.

### Unload Player Data

```csharp
[Server]
public void UnloadPlayerData(string playerId)
{
    playerActiveShips.Remove(playerId);
    portInventories.Remove(playerId);
}
```

**Purpose**: Clean up player data on disconnect.

**Called By**: `PlayerShipManager`.

## Integration Points

### Manager References

| Manager | Purpose |
|---------|---------|
| `AccountManager` | Player ID lookup |
| `PlayerShipManager` | Save ship changes, query active ship |

### Data Flow

```
Client: CmdInstallEquipment()
    ↓
Server: Validate (slot, tier, type)
    ↓
Server: Update slot on ship
    ↓
Server: Remove from port inventory
    ↓
Server: PlayerShipManager.SavePlayerShips()
    ↓
PlayFab: Save ship collection
    ↓
Server: TargetRpcInstallResult()
    ↓
Client: Update UI
```

## Design Notes

### Slot Compatibility Validation

Equipment must match **both tier range and type**:

**Turret Example**:
- Slot: Main Battery (T3-T6)
- Equipment: T5 16-inch Main Battery ✓ Valid
- Equipment: T5 5-inch Secondary ✗ Wrong type
- Equipment: T7 18-inch Main Battery ✗ Tier too high

**Engine Example**:
- Slot: Engine Room (T1-T5)
- Equipment: T5 Turbine Engine ✓ Valid (no type restriction)

**Module Example**:
- Slot: Fire Control (T3-T7)
- Equipment: T5 Fire Control System ✓ Valid
- Equipment: T5 Radar System ✗ Wrong type

### Inventory Space Check

Uninstallation **fails if inventory full**:
```csharp
if (!TryPlaceItemInInventory(inventory, uninstalledItem))
{
    TargetRpcUninstallResult(sender, false,
        "No space in port inventory for uninstalled equipment");
    return;
}
```

**Player Action**: Must free up inventory space before uninstalling.

### Grid Size Constants

Equipment grid sizes are **hardcoded** in uninstall methods:
```csharp
Size = new GridSize(3, 2)  // Turrets
Size = new GridSize(4, 3)  // Engines
Size = new GridSize(2, 2)  // Modules
```

**Future**: Should load from `EquipmentDefinitionSO.InventorySize`.

### Shared Cache with PlayerShipManager

Both managers share the **same active ship reference**:
```csharp
// PlayerShipManager sets:
shipEquipmentManager.LoadPlayerActiveShip(playerId, activeShip);

// ShipEquipmentManager uses:
PlayerShipData ship = playerActiveShips[playerId];
```

**Benefit**: Single source of truth, automatic sync.

### Save Delegation

`ShipEquipmentManager` doesn't save directly - it delegates to `PlayerShipManager`:
```csharp
PlayerShipManager.Instance?.SavePlayerShips(playerId);
```

**Reason**: `PlayerShipManager` owns ship collection persistence logic.

### Port-Only Restriction

Equipment installation/uninstallation should be **port-only**:
```csharp
// TODO: Verify player is at port
if (!IsPlayerAtPort(playerId))
{
    TargetRpcInstallResult(sender, false,
        "Must be at port to install equipment");
    return;
}
```

**Future**: Add port location check to prevent mid-ocean equipment swaps.

### Equipment Reference Storage

Slots store equipment as **reference IDs**, not full objects:
```csharp
slot.EquipmentItemId = equipmentItem.ItemId;
slot.EquipmentDefinitionId = equipmentItem.EquipmentDefinitionId;
```

**Benefits**:
- Lightweight storage (JSON serialization)
- Equipment definition loaded from ScriptableObject when needed
- No data duplication

### Item Removal from Inventory

After installation, item is **removed from inventory**:
```csharp
inventory.RemoveItem(itemId);
```

This prevents:
- Equipment duplication (installed + in inventory)
- Weight counting twice
- Exploits (sell installed equipment)

### Auto-Placement Algorithm

`TryPlaceItemInInventory()` uses **greedy left-to-right, top-to-bottom** scan:
```
□ □ □ □ □
□ □ □ □ □
□ □ ■ ■ □  ← Finds first fit here
□ □ ■ ■ □
```

**Alternative**: Could optimize for "best fit" (minimize fragmentation).

### Error Message Clarity

Provides **detailed error messages** for debugging:
```csharp
errorMessage = $"Equipment tier {equipmentItem.EquipmentTier} not compatible " +
    $"with slot (requires {slot.MinTier}-{slot.MaxTier}, type: {slot.AllowedType})";
```

**Example**: "Equipment tier 7 not compatible with slot (requires 1-5, type: Main)"

### Type String Conversion

Uses **safe enum parsing** with defaults:
```csharp
if (Enum.TryParse<TurretType>(typeString, out TurretType result))
    return result;
return TurretType.Main;  // Fallback to Main if parsing fails
```

Prevents crashes from invalid data.

### Future Enhancements

1. **Port location check**: Restrict to ports only
2. **Installation time**: Time-gated installation (large equipment takes hours)
3. **Installation costs**: Credits for installation/uninstallation
4. **Crew requirements**: Require crew to install equipment
5. **Equipment damage**: Installed equipment can be damaged in combat
6. **Auto-organize**: Optimize inventory layout automatically
7. **Loadout presets**: Save/load entire ship configurations
8. **Batch operations**: Install multiple items at once
