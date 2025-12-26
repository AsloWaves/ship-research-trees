---
tags: [script, networking, playfab, persistence, inventory, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Networking.Managers
file-path: Assets/Scripts/Networking/Managers/PlayFabInventoryService.cs
status: IMPLEMENTED
size: ~24 KB (859 lines)
feature-group: networking
---

# PlayFabInventoryService.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Networking.Managers
**File**: `Assets/Scripts/Networking/Managers/PlayFabInventoryService.cs`
**Size**: ~24 KB (859 lines)
**Dependencies**: PlayFab Server SDK, CargoGrid, ShipLoadout, WalletData

---

## Purpose
Comprehensive PlayFab-based inventory persistence service. Handles ship cargo, port storage, ship loadouts, and player wallet using PlayFab User Data API. Integrates with DefaultLoadoutService for new player starter items.

This service manages:
- Ship cargo inventory load/save
- Per-port warehouse storage
- Ship loadout persistence
- Player wallet (credits and premium currency)
- Optimistic locking for all data types
- Both callback and async Task APIs

---

## PlayFab Data Keys

```
KEY_SHIP_CARGO          = "ShipCargo"           // CargoGrid JSON
KEY_INVENTORY_VERSION   = "InventoryVersion"    // Version for locking
KEY_INVENTORY_LAST_SAVED = "InventoryLastSaved" // UTC timestamp
KEY_PORT_STORAGE_PREFIX = "PortStorage_"        // PortStorage_{portId}
KEY_SHIP_LOADOUT_PREFIX = "ShipLoadout_"        // ShipLoadout_{shipId}
KEY_WALLET              = "Wallet"              // WalletData JSON
```

---

## Default Configuration

```csharp
DEFAULT_SHIP_CARGO_WIDTH      = 10
DEFAULT_SHIP_CARGO_HEIGHT     = 10
DEFAULT_SHIP_CARGO_MAX_WEIGHT = 5000f
```

Port storage defaults (in async API):
```csharp
portWidth  = 20
portHeight = 20
maxWeight  = 50000f
```

---

## Singleton Access

```csharp
public static PlayFabInventoryService Instance { get; }
```

---

## Ship Cargo Methods

### LoadInventory (Callback)
```csharp
public void LoadInventory(
    string playFabId,
    Action<CargoGrid, int, bool> callback)
```

**Behavior**:
- Fetches ship cargo from PlayFab
- Creates default inventory via DefaultLoadoutService if none exists
- Immediately saves default inventory for new players

### SaveInventory (Callback)
```csharp
public void SaveInventory(
    string playFabId,
    CargoGrid inventory,
    int currentVersion,
    Action<int, bool> callback)
```

---

## Port Storage Methods

### LoadPortStorage
```csharp
public void LoadPortStorage(
    string playFabId,
    string portId,
    int portWidth,
    int portHeight,
    float maxWeight,
    Action<CargoGrid, int, bool> callback)
```

**Data Key Format**: `PortStorage_{portId}`

**Behavior**:
- Loads port-specific storage for player
- Creates empty storage if none exists
- OwnerId format: `{playFabId}_{portId}`

### SavePortStorage
```csharp
public void SavePortStorage(
    string playFabId,
    string portId,
    CargoGrid storage,
    int currentVersion,
    Action<int, bool> callback)
```

---

## Ship Loadout Methods (Async Task API)

### LoadShipLoadout
```csharp
public Task<ShipLoadout> LoadShipLoadout(string playFabId, string shipId)
```

**Data Key Format**: `ShipLoadout_{shipId}`

**Behavior**:
- Returns existing loadout or creates empty default
- Returns null on API failure

### SaveShipLoadout
```csharp
public Task<bool> SaveShipLoadout(
    string playFabId,
    string shipId,
    ShipLoadout loadout)
```

---

## Wallet Methods (Async Task API)

### GetWallet
```csharp
public Task<WalletData> GetWallet(string playFabId)
```

**Behavior**:
- Returns existing wallet or creates default
- Default credits from DefaultLoadoutService config
- Auto-saves new wallet for new players

### UpdateWallet
```csharp
public Task<bool> UpdateWallet(string playFabId, WalletData wallet)
```

**Behavior**:
- Updates timestamp before save
- Returns success/failure

---

## Coroutine Wrappers

### Inventory Coroutines
```csharp
public IEnumerator LoadInventoryCoroutine(
    string playFabId,
    Action<CargoGrid, int, bool> callback)

public IEnumerator SaveInventoryCoroutine(
    string playFabId,
    CargoGrid inventory,
    int currentVersion,
    Action<int, bool> callback)
```

### Port Storage Coroutines
```csharp
public IEnumerator LoadPortStorageCoroutine(
    string playFabId,
    string portId,
    int portWidth,
    int portHeight,
    float maxWeight,
    Action<CargoGrid, int, bool> callback)

public IEnumerator SavePortStorageCoroutine(
    string playFabId,
    string portId,
    CargoGrid storage,
    int currentVersion,
    Action<int, bool> callback)
```

---

## Async Task API (for InventoryServiceProvider)

Simplified async wrappers for use with async/await:

```csharp
public Task<CargoGrid> LoadInventory(string playFabId)
public Task<bool> SaveInventory(string playFabId, CargoGrid inventory)
public Task<CargoGrid> LoadPortStorage(string playFabId, string portId)
public Task<bool> SavePortStorage(string playFabId, string portId, CargoGrid storage)
```

Note: Async save methods load current version internally for locking.

---

## Default Inventory Creation

```csharp
private CargoGrid CreateDefaultInventory(string playFabId)
```

**Process**:
1. Try `DefaultLoadoutService.GenerateDefaultInventory(playFabId)`
2. If service returns items, use populated inventory
3. Fallback: Create empty 10x10 CargoGrid

**DefaultLoadoutService Integration**:
- Provides starter items based on configuration
- Used for consistent new player experience
- Fallback to empty if service unavailable

---

## Optimistic Locking

All save operations use version-based locking:

```
1. Load data with version number
2. Make changes
3. Save with current version
4. Version incremented on successful save
5. Reload on conflict
```

---

## Integration Points

### Dependencies
- **PlayFab.ServerModels** - GetUserData, UpdateUserData
- [[CargoGrid]] - Inventory grid system
- [[ShipLoadout]] - Equipment loadout data
- [[WalletData]] - Currency data
- [[DefaultLoadoutService]] - Starter item configuration
- [[DebugManager]] - Logging

### Used By
- [[ServerInventoryManager]] - Inventory caching layer
- [[InventoryServiceProvider]] - Service abstraction
- [[WOSNetworkManager]] - Player data loading

---

## Data Persistence Model

| Data Type | Key Pattern | Create Default | Auto-Save Default |
|-----------|-------------|----------------|-------------------|
| Ship Cargo | `ShipCargo` | Yes (with items) | Yes |
| Port Storage | `PortStorage_{portId}` | Yes (empty) | No |
| Ship Loadout | `ShipLoadout_{shipId}` | Yes (empty) | No |
| Wallet | `Wallet` | Yes (with credits) | Yes |

---

## Error Handling

- Logs via DebugManager with `DebugCategory.Networking`
- Returns null/false on failures
- Creates sensible defaults on missing data
- Graceful JSON parse error handling
- Warns but continues if default save fails

---

## Related Files
- [[PlayFabShipService]] - Ship collection persistence
- [[PlayFabCrewService]] - Crew card persistence
- [[ServerInventoryManager]] - Server-side inventory cache
- [[CargoGrid]] - Inventory data structure
- [[DefaultLoadoutService]] - Starter item configuration

---

## Testing Notes
- Requires server build with PlayFab Server SDK
- Port storage keyed by port ID for per-location warehouses
- Ship loadouts keyed by ship ID
- Async API handles version loading internally
- DefaultLoadoutService must be configured for starter items

---

## Changelog
- **2024-12**: Initial implementation (ship cargo only)
- **2025-01**: Added port storage support
- **2025-01**: Added ship loadout persistence
- **2025-01**: Added wallet methods
- **2025-01**: Added async Task API for InventoryServiceProvider
- **2025-01**: Integrated DefaultLoadoutService for starter items

