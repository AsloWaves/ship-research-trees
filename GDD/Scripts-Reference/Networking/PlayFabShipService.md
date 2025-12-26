---
tags: [script, networking, playfab, persistence, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Networking.Managers
file-path: Assets/Scripts/Networking/Managers/PlayFabShipService.cs
status: IMPLEMENTED
size: ~10 KB (363 lines)
feature-group: networking
---

# PlayFabShipService.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Networking.Managers
**File**: `Assets/Scripts/Networking/Managers/PlayFabShipService.cs`
**Size**: ~10 KB (363 lines)
**Dependencies**: PlayFab Server SDK, PlayerShipData, CargoGrid

---

## Purpose
PlayFab-based ship persistence service. Provides read/write operations for player ship data using PlayFab User Data API. Automatically creates starter ships for new players with optimistic locking for conflict resolution.

This service manages:
- Ship collection load/save via PlayFab User Data
- Starter ship creation for new players
- Version-based optimistic locking
- Coroutine wrappers for Unity integration

---

## PlayFab Data Keys

```
KEY_SHIP_COLLECTION     = "ShipCollection"           // PlayerShipCollection JSON
KEY_SHIP_VERSION        = "ShipCollectionVersion"    // Version for optimistic locking
KEY_SHIP_LAST_SAVED     = "ShipCollectionLastSaved"  // UTC timestamp (ISO 8601)
```

---

## Singleton Access

```csharp
public static PlayFabShipService Instance { get; }
```

Uses `FindFirstObjectByType<>()` for lazy initialization.

---

## Public Methods

### LoadShipCollection
Loads player's ship collection from PlayFab.

```csharp
public void LoadShipCollection(
    string playFabId,
    Action<PlayerShipCollection, int, bool> callback)
```

**Parameters**:
- `playFabId` - Player's PlayFab ID
- `callback` - Returns (collection, version, success)

**Behavior**:
- Fetches from PlayFab User Data API
- Creates starter ship if no ships exist
- Immediately saves starter ship to persist for new players

### SaveShipCollection
Saves player's ship collection to PlayFab.

```csharp
public void SaveShipCollection(
    string playFabId,
    PlayerShipCollection collection,
    int currentVersion,
    Action<int, bool> callback)
```

**Parameters**:
- `playFabId` - Player's PlayFab ID
- `collection` - PlayerShipCollection to save
- `currentVersion` - Version for optimistic locking
- `callback` - Returns (newVersion, success)

**Behavior**:
- Increments version number
- Serializes collection to JSON
- Saves to PlayFab with timestamp

---

## Starter Ship Creation

```csharp
private PlayerShipCollection CreateStarterShipCollection(string playFabId)
```

**Default Configuration**:
```
DEFAULT_SHIP_CLASS_ID = "T1_Destroyer_USA"
DEFAULT_SHIP_NAME     = "USS Starter"
DEFAULT_CARGO_WIDTH   = 10
DEFAULT_CARGO_HEIGHT  = 10
MAX_WEIGHT            = 5000f
```

**Created Ship Data**:
- Unique ShipId (GUID)
- ActiveShip = true (first ship is active)
- Empty ShipLoadout
- Empty CargoGrid (10x10)
- CreatedAt/UpdatedAt timestamps

---

## Coroutine Wrappers

### LoadShipCollectionCoroutine
```csharp
public IEnumerator LoadShipCollectionCoroutine(
    string playFabId,
    Action<PlayerShipCollection, int, bool> callback)
```

### SaveShipCollectionCoroutine
```csharp
public IEnumerator SaveShipCollectionCoroutine(
    string playFabId,
    PlayerShipCollection collection,
    int currentVersion,
    Action<int, bool> callback)
```

Use with `StartCoroutine()` for Unity-friendly async operations.

---

## Optimistic Locking Flow

```
1. Load collection with current version
2. Make changes to collection in memory
3. Save with current version
4. Service increments version on save
5. If conflict detected, reload and retry
```

This prevents data loss when multiple save operations occur.

---

## Integration Points

### Dependencies
- **PlayFab.ServerModels** - GetUserData, UpdateUserData requests
- [[PlayerShipData]] - Ship data structure
- [[CargoGrid]] - Cargo inventory system
- [[DebugManager]] - Logging

### Used By
- [[PlayerShipManager]] - Caches and manages ship data
- [[WOSNetworkManager]] - Loads ships on player connect

---

## PlayFab Configuration

```csharp
public bool ValidatePlayFabConfiguration()
```

**Validates**:
- TitleId is configured in PlayFabSettings
- DeveloperSecretKey loaded from `PLAYFAB_SECRET_KEY` environment variable

Note: Secret key is loaded by [[PlayFabServerAuthConfig]] at runtime, not stored in settings.

---

## Error Handling

- Logs errors via DebugManager with `DebugCategory.Ship`
- Returns `false` success flag on API failures
- Gracefully handles JSON parse failures
- Warns but continues if starter ship save fails

---

## Related Files
- [[PlayFabCrewService]] - Similar pattern for crew data
- [[PlayFabInventoryService]] - Inventory persistence
- [[PlayerShipManager]] - Uses this service for persistence
- [[PlayerShipData]] - Ship data structure

---

## Testing Notes
- Requires server build with PlayFab Server SDK
- DeveloperSecretKey from environment variable
- Creates starter ship for new PlayFab accounts
- Starter ship immediately persisted on creation

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added starter ship auto-save on creation
- **2025-01**: Added coroutine wrappers

