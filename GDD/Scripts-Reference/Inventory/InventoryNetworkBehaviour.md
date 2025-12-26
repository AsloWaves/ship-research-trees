---
tags: [script, inventory, networking, mirror, implemented]
script-type: NetworkBehaviour
namespace: WOS.Inventory.Networking
file-path: Assets/Scripts/Inventory/Networking/InventoryNetworkBehaviour.cs
status: IMPLEMENTED
size: ~24 KB (865 lines)
feature-group: inventory
---

# InventoryNetworkBehaviour.cs

## Quick Reference
**Type**: NetworkBehaviour (Mirror)
**Namespace**: WOS.Inventory.Networking
**File**: `Assets/Scripts/Inventory/Networking/InventoryNetworkBehaviour.cs`
**Size**: ~24 KB (865 lines)
**Dependencies**: Mirror, ShipInventory, WalletInventory, ServerInventoryManager, AuthenticationManager

---

## Purpose
Client-side network behaviour for inventory synchronization using Mirror. Handles all client-server communication for inventory operations using Command/TargetRpc pattern. Implements dirty flag batching for efficient updates.

---

## Architecture

```
Client                          Server
  |                               |
  |--[Command]-- Request -------->|
  |                               |-- Validate via ServerInventoryManager
  |<--[TargetRpc]-- Result -------|
  |                               |
```

---

## Configuration

```csharp
[Header("Configuration")]
[SerializeField] private bool enableDebugLogging = true;

[Header("Performance")]
[SerializeField] private float syncCooldown = 0.1f;  // Prevents spam

[Header("Runtime State (Read-Only)")]
[SerializeField] private bool isInventoryLoaded = false;
[SerializeField] private int currentVersion = 0;
```

---

## Events

```csharp
public static event Action<CargoGrid> OnShipInventoryLoaded;
public static event Action<CargoGrid> OnShipInventoryUpdated;
public static event Action<WalletInventory> OnContainerOpened;
public static event Action<string> OnContainerClosed;
public static event Action<string, bool, string> OnItemOperationResult;  // itemId, success, message
public static event Action<string, string, bool, string> OnTransferResult;  // itemId, targetType, success, message
```

---

## Public API - Client Operations

### State Access
```csharp
public ShipInventory GetShipInventory()
public WalletInventory GetOpenContainer(string containerItemId)
public bool IsInventoryReady => isInventoryLoaded && _shipInventory != null;
```

### Load Operations
```csharp
public void RequestLoadInventory()
```
Called automatically in `OnStartLocalPlayer()`.

### Item Operations
```csharp
public void RequestMoveItem(string itemId, int newX, int newY, int rotation = 0)
public void RequestRotateItem(string itemId)
public void RequestUseItem(string itemId, int quantity = 1)
public void RequestRemoveItem(string itemId, int quantity = 1)
```

### Container Operations
```csharp
public void RequestOpenContainer(string containerItemId)
public void CloseContainer(string containerItemId)
```

### Transfer Operations
```csharp
public void RequestTransferToContainer(string itemId, string containerItemId, int destX = -1, int destY = -1)
public void RequestTransferFromContainer(string itemId, string containerItemId, int destX = -1, int destY = -1)
```

### Stack Operations
```csharp
public void RequestSplitStack(string itemId, int splitQuantity, int newX = -1, int newY = -1)
public void RequestMergeStacks(string sourceItemId, string targetItemId)
```

---

## Commands (Client → Server)

| Command | Purpose | Server Validation |
|---------|---------|-------------------|
| CmdRequestLoadInventory | Load player inventory | Creates new if none exists |
| CmdMoveItem | Move/rotate item | Position and rotation validation |
| CmdUseItem | Use consumable | Quantity check |
| CmdRemoveItem | Drop/delete item | Quantity check |
| CmdOpenContainer | Open container item | Container type validation |
| CmdTransferItem | Move between grids | Space and type validation |
| CmdSplitStack | Split stack | Quantity validation |
| CmdMergeStacks | Merge stacks | Type matching |

---

## TargetRpcs (Server → Client)

| TargetRpc | Parameters | Fires Event |
|-----------|------------|-------------|
| TargetInventoryLoaded | CargoGrid, version | OnShipInventoryLoaded |
| TargetInventorySync | CargoGrid, version | OnShipInventoryUpdated |
| TargetItemMoveResult | success, itemId, position, rotation, message | OnItemOperationResult |
| TargetItemUseResult | success, itemId, remaining, message | OnItemOperationResult |
| TargetItemRemoveResult | success, itemId, remaining, message | OnItemOperationResult |
| TargetContainerOpened | containerId, contents, width, height | OnContainerOpened |
| TargetTransferResult | success, itemId, targetType, message | OnTransferResult |

---

## Network Message Handlers

Registered in `OnStartClient()`:
- InventoryLoadedMessage
- InventorySyncMessage
- ItemMovedMessage
- ItemAddedMessage
- ItemRemovedMessage
- ItemUsedMessage

---

## Operation Throttling

```csharp
private bool CanPerformOperation()
{
    if (!isOwned) return false;
    if (!isInventoryLoaded) return false;
    if (Time.time - _lastSyncTime < syncCooldown) return false;

    _lastSyncTime = Time.time;
    return true;
}
```

Default cooldown: 100ms between operations.

---

## Server-Side Helpers

```csharp
private string GetPlayerId()         // From AuthenticationManager or connection ID
private CargoGrid GetServerInventory(string playerId)  // From ServerInventoryManager cache
private int GetInventoryVersion(string playerId)
private void MarkDirty(string playerId)  // Triggers save via ServerInventoryManager
```

---

## Player ID Resolution

**Server-side**:
1. Try AuthenticationManager.GetPlayerId(connectionId)
2. Fallback to connectionId.ToString()

**Client-side**:
1. Try NetworkClient.connection.identity.netId
2. Fallback to "local_test"

---

## Lifecycle

```csharp
OnStartClient()        → Register message handlers (owned only)
OnStopClient()         → Unregister message handlers
OnStartLocalPlayer()   → RequestLoadInventory()
```

---

## Integration Points

### Dependencies
- [[ServerInventoryManager]] - Server-side data management
- [[AuthenticationManager]] - Player ID resolution
- [[ShipInventory]] - Client inventory wrapper
- [[WalletInventory]] - Container wrapper
- [[CargoGrid]] - Grid data
- [[DebugManager]] - Logging

### Used By
- [[InventoryPanel]] - UI integration
- [[EquipmentPanel]] - Equipment UI
- Player prefab (NetworkIdentity required)

---

## Related Files
- [[ServerInventoryManager]] - Server-side counterpart
- [[PlayFabInventoryService]] - Backend persistence
- [[InventoryManager]] - Client-side orchestrator (non-network)
- [[CargoGrid]] - Core inventory grid

---

## Message Types (Separate File)

Referenced from `WOS.Networking.Messages`:
- InventoryLoadedMessage
- InventorySyncMessage
- ItemMovedMessage
- ItemAddedMessage
- ItemRemovedMessage
- ItemUsedMessage

---

## Testing Notes
- Requires NetworkIdentity component
- Messages registered only for owned objects
- Inventory auto-loads on local player start
- Default 30x30 grid created for new players
- Sync cooldown prevents spam (100ms)
- Stack operations trigger full inventory sync

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added container operations
- **2025-01**: Added stack split/merge
- **2025-01**: Added transfer operations
- **2025-01**: Added message-based sync

