# InventoryServiceProvider.cs

## Quick Reference

| **File** | InventoryServiceProvider.cs |
|----------|----------------------------|
| **Namespace** | WOS.Networking.Managers |
| **Inheritance** | MonoBehaviour |
| **Lines** | 491 |
| **Architecture** | Singleton, Strategy pattern, async/await API |

---

## Purpose

Singleton service provider that abstracts inventory storage backend. Enables seamless switching between PlayFab (production) and Local (testing) storage.

**Key Benefits**:
- Single API for all inventory operations
- Easy backend switching via Inspector or ServerConfig
- Supports both PlayFab and Local file storage
- Async/await modern C# API
- Event system for UI integration

---

## Configuration

### Storage Backend Enum

```csharp
public enum StorageBackend
{
    PlayFab,    // Production - uses PlayFab User Data API
    Local       // Testing - uses local JSON files
}
```

### Inspector Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `_backend` | StorageBackend | `PlayFab` | Active storage backend |
| `_useServerConfigOverride` | bool | `true` | Override from ServerConfig if available |
| `_verboseLogging` | bool | `false` | Log all inventory operations |

### ServerConfig Override

```csharp
// Resources/ServerConfigs/ServerConfig.asset
public class ServerConfig : ScriptableObject
{
    public bool useLocalInventory;  // If true, uses Local backend
}
```

---

## Public API

### Configuration

#### `CurrentBackend`
Gets current active storage backend.

**Returns**: `StorageBackend`

#### `IsLocalStorage`
Whether using local file storage.

**Returns**: `bool`

#### `IsPlayFabStorage`
Whether using PlayFab cloud storage.

**Returns**: `bool`

#### `SetBackend(StorageBackend backend)`
Changes active storage backend at runtime.

**Example**:
```csharp
// Switch to local testing
InventoryServiceProvider.Instance.SetBackend(StorageBackend.Local);
```

### Async Inventory Operations

#### `LoadInventoryAsync(string playerId)`
Loads player inventory from active backend.

**Returns**: `Task<CargoGrid>`

**Example**:
```csharp
CargoGrid inventory = await InventoryServiceProvider.Instance.LoadInventoryAsync(playerId);
if (inventory != null)
{
    Debug.Log($"Loaded {inventory.Items.Count} items");
}
```

#### `SaveInventoryAsync(string playerId, CargoGrid inventory)`
Saves player inventory to active backend.

**Returns**: `Task<bool>`

**Example**:
```csharp
bool success = await InventoryServiceProvider.Instance.SaveInventoryAsync(playerId, inventory);
```

#### `LoadPortStorageAsync(string playerId, string portId)`
Loads port storage from active backend.

**Returns**: `Task<CargoGrid>`

#### `SavePortStorageAsync(string playerId, string portId, CargoGrid storage)`
Saves port storage to active backend.

**Returns**: `Task<bool>`

#### `LoadShipLoadoutAsync(string playerId, string shipId)`
Loads ship loadout from active backend.

**Returns**: `Task<ShipLoadout>`

#### `SaveShipLoadoutAsync(string playerId, string shipId, ShipLoadout loadout)`
Saves ship loadout to active backend.

**Returns**: `Task<bool>`

### Wallet Operations

#### `GetWalletAsync(string playerId)`
Gets player wallet from active backend.

**Returns**: `Task<WalletData>`

#### `UpdateWalletAsync(string playerId, WalletData wallet)`
Updates player wallet in active backend.

**Returns**: `Task<bool>`

---

## Events

### `OnBackendChanged(StorageBackend backend)`
Fired when storage backend changes.

**Example**:
```csharp
InventoryServiceProvider.Instance.OnBackendChanged += (backend) =>
{
    Debug.Log($"Storage backend changed to: {backend}");
    UpdateUIIndicator(backend);
};
```

### `OnInventoryLoaded(CargoGrid inventory)`
Fired when inventory is loaded.

### `OnInventorySaved(bool success)`
Fired when inventory save completes.

---

## Usage Examples

### Basic Inventory Operations

```csharp
public class InventoryManager : MonoBehaviour
{
    async void LoadPlayerInventory(string playerId)
    {
        try
        {
            // Load inventory (automatically uses configured backend)
            CargoGrid inventory = await InventoryServiceProvider.Instance.LoadInventoryAsync(playerId);

            if (inventory != null)
            {
                Debug.Log($"Loaded {inventory.Items.Count} items");
                DisplayInventory(inventory);
            }
        }
        catch (Exception ex)
        {
            Debug.LogError($"Failed to load inventory: {ex.Message}");
        }
    }

    async void SavePlayerInventory(string playerId, CargoGrid inventory)
    {
        bool success = await InventoryServiceProvider.Instance.SaveInventoryAsync(playerId, inventory);

        if (success)
        {
            Debug.Log("Inventory saved successfully");
        }
        else
        {
            Debug.LogError("Failed to save inventory");
        }
    }
}
```

### Backend Switching

```csharp
public class ServerConfigManager : MonoBehaviour
{
    [SerializeField] private bool useLocalTesting = false;

    void Awake()
    {
        var provider = InventoryServiceProvider.Instance;

        if (useLocalTesting)
        {
            // Switch to local file storage for testing
            provider.SetBackend(StorageBackend.Local);
            Debug.Log("Using LOCAL file storage (testing mode)");
        }
        else
        {
            // Use PlayFab cloud storage for production
            provider.SetBackend(StorageBackend.PlayFab);
            Debug.Log("Using PLAYFAB cloud storage (production mode)");
        }
    }
}
```

### UI Integration

```csharp
public class InventoryUI : MonoBehaviour
{
    [SerializeField] private Text statusText;

    void Start()
    {
        var provider = InventoryServiceProvider.Instance;

        // Subscribe to events
        provider.OnInventoryLoaded += OnInventoryLoaded;
        provider.OnInventorySaved += OnInventorySaved;
        provider.OnBackendChanged += OnBackendChanged;

        // Display current backend
        UpdateStatusText();
    }

    void UpdateStatusText()
    {
        statusText.text = InventoryServiceProvider.Instance.GetStatusString();
        // "📁 Local Storage (Testing)" or "☁️ PlayFab Cloud (Production)"
    }

    void OnInventoryLoaded(CargoGrid inventory)
    {
        Debug.Log($"Inventory loaded: {inventory.Items.Count} items");
    }

    void OnInventorySaved(bool success)
    {
        Debug.Log($"Inventory saved: {success}");
    }

    void OnBackendChanged(StorageBackend backend)
    {
        UpdateStatusText();
    }
}
```

---

## Backend Routing

### How It Works

```csharp
// InventoryServiceProvider routes to appropriate service
public async Task<CargoGrid> LoadInventoryAsync(string playerId)
{
    if (_backend == StorageBackend.Local)
    {
        // Route to LocalFileInventoryService
        return await LocalService.LoadInventory(playerId);
    }
    else
    {
        // Route to PlayFabInventoryService
        return await PlayFabService.LoadInventory(playerId);
    }
}
```

### Service Auto-Creation

**LocalFileInventoryService**:
- Auto-created if not found when `StorageBackend.Local` is active
- Created as child GameObject under InventoryServiceProvider

**PlayFabInventoryService**:
- Should exist in scene (not auto-created)
- Uses PlayFab Server API (requires authentication)

---

## Design Notes

### Strategy Pattern

InventoryServiceProvider implements Strategy pattern:

```
┌─────────────────────────────────┐
│  InventoryServiceProvider       │
│  (Context)                      │
└─────────────────────────────────┘
              ↓
    ┌─────────┴─────────┐
    ↓                   ↓
┌───────────────┐  ┌──────────────────────┐
│ PlayFabInv... │  │ LocalFileInv...      │
│ (Strategy A)  │  │ (Strategy B)         │
└───────────────┘  └──────────────────────┘
```

**Benefits**:
- Easy to add new storage backends
- Switch backends at runtime
- Components never directly depend on PlayFab or Local implementations

### Async/Await Modern API

**Old Pattern** (callback hell):
```csharp
LoadInventory(playerId, (inventory, success) =>
{
    if (success)
    {
        SaveInventory(playerId, inventory, (saveSuccess) =>
        {
            if (saveSuccess) { /* ... */ }
        });
    }
});
```

**New Pattern** (async/await):
```csharp
var inventory = await LoadInventoryAsync(playerId);
if (inventory != null)
{
    bool success = await SaveInventoryAsync(playerId, inventory);
}
```

### ServerConfig Override

**Priority**:
1. ServerConfig override (if `_useServerConfigOverride = true`)
2. Inspector setting (`_backend`)

**Example ServerConfig**:
```
Resources/ServerConfigs/ServerConfig.asset
- useLocalInventory = true  → Uses Local backend
- useLocalInventory = false → Uses PlayFab backend
```

---

## Key Takeaways

1. **Single API**: One interface for all inventory operations (PlayFab or Local)
2. **Easy Switching**: Change backend via Inspector or ServerConfig
3. **Async/Await**: Modern C# async API (no callback hell)
4. **Event System**: Subscribe to load/save events for UI updates
5. **Strategy Pattern**: Clean abstraction over storage implementations
6. **Auto-Creation**: Automatically creates LocalFileInventoryService when needed
