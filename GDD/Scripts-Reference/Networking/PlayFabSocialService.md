# PlayFabSocialService.cs

## Quick Reference

| **File** | PlayFabSocialService.cs |
|----------|------------------------|
| **Namespace** | WOS.Networking.Managers |
| **Inheritance** | MonoBehaviour |
| **Lines** | 296 |
| **Architecture** | Singleton, PlayFab Server API integration |

---

## Purpose

PlayFab-based social data persistence service that provides read/write operations for player social data using PlayFab User Data API. Handles friend lists, parties, and social relationships with optimistic locking via version numbers.

**Key Responsibilities**:
- Load/save player social data from/to PlayFab User Data API
- Manage version numbers for optimistic locking
- Create default empty data for new players
- Integrate with SocialDataManager's caching system

---

## Configuration

### PlayFab User Data Keys

| Key | Type | Purpose |
|-----|------|---------|
| `SocialData` | JSON | SocialPlayerData serialized to JSON |
| `SocialDataVersion` | int | Version number for optimistic locking |
| `SocialDataLastSaved` | DateTime (ISO 8601) | UTC timestamp of last save |

### Storage Architecture

```
PlayFab User Data (Private)
├── SocialData: { playerId, friendsList, partyData, ... }
├── SocialDataVersion: 3
└── SocialDataLastSaved: "2025-01-15T14:30:00.000Z"
```

---

## Public API

### Core Methods

#### `LoadSocialData(string playFabId, Action<SocialPlayerData, int, bool> callback)`
Loads player's social data from PlayFab. Creates default empty data if none exists.

**Parameters**:
- `playFabId` - Player's PlayFab ID
- `callback` - Callback with (SocialPlayerData data, int version, bool success)

**Returns**: Via callback - SocialPlayerData instance, version number, success status

**Example**:
```csharp
PlayFabSocialService.Instance.LoadSocialData(playFabId, (socialData, version, success) =>
{
    if (success)
    {
        Debug.Log($"Loaded social data version {version}");
        // Use socialData.friendsList, socialData.partyData, etc.
    }
});
```

#### `SaveSocialData(string playFabId, SocialPlayerData socialData, int currentVersion, Action<int, bool> callback)`
Saves player's social data to PlayFab using optimistic locking.

**Parameters**:
- `playFabId` - Player's PlayFab ID
- `socialData` - SocialPlayerData to save
- `currentVersion` - Current version for optimistic locking
- `callback` - Callback with (int newVersion, bool success)

**Returns**: Via callback - New version number, success status

**Example**:
```csharp
PlayFabSocialService.Instance.SaveSocialData(playFabId, socialData, currentVersion, (newVersion, success) =>
{
    if (success)
    {
        Debug.Log($"Social data saved: v{currentVersion} → v{newVersion}");
    }
});
```

### Coroutine Wrappers

#### `LoadSocialDataCoroutine(string playFabId, Action<SocialPlayerData, int, bool> callback)`
Coroutine wrapper for LoadSocialData.

#### `SaveSocialDataCoroutine(string playFabId, SocialPlayerData socialData, int currentVersion, Action<int, bool> callback)`
Coroutine wrapper for SaveSocialData.

### Utility Methods

#### `ValidatePlayFabConfiguration()`
Validates that PlayFab is configured correctly for server API calls.

**Returns**: `bool` - True if TitleId is configured

**Note**: DeveloperSecretKey is loaded via environment variable `PLAYFAB_SECRET_KEY` by PlayFabServerAuthConfig, not stored in PlayFabSettings.

---

## Integration Points

### PlayFab Server API

**PlayFab Endpoints Used**:
- `PlayFabServerAPI.GetUserData` - Load social data
- `PlayFabServerAPI.UpdateUserData` - Save social data with Private permission

**Authentication**:
- Requires PlayFab DeveloperSecretKey (loaded by PlayFabServerAuthConfig)
- Server-side only (never expose secret key to clients)

### SocialDataManager Integration

The service integrates with SocialDataManager's caching system:
```csharp
// SocialDataManager loads data once and caches
PlayFabSocialService.Instance.LoadSocialData(playFabId, (socialData, version, success) =>
{
    if (success)
    {
        // SocialDataManager caches this data
        socialDataCache[playFabId] = socialData;
        versionCache[playFabId] = version;
    }
});
```

---

## Design Notes

### Optimistic Locking

The service uses version numbers to prevent concurrent modification bugs:

```csharp
// Load current data
LoadSocialData(playerId, (data, version, success) =>
{
    // Modify data
    data.friendsList.Add(newFriend);

    // Save with version check
    SaveSocialData(playerId, data, version, (newVersion, saveSuccess) =>
    {
        if (saveSuccess)
        {
            // Version incremented: v3 → v4
            // If another save happened concurrently, this would fail
        }
    });
});
```

### Data Structure

**SocialPlayerData** structure (defined elsewhere):
```csharp
[Serializable]
public class SocialPlayerData
{
    public string playerId;
    public List<string> friendsList;
    public PartyData partyData;
    public DateTime lastSaved;
    // Additional social fields...
}
```

### Default Data Creation

If no social data exists for a player:
1. Service creates default empty SocialPlayerData with playerId
2. Version is set to 1
3. No automatic save - SocialDataManager decides when to persist

### Server-Only Architecture

**Security Model**:
- Runs on server only (headless builds or Editor host mode)
- Uses PlayFab Server API (requires DeveloperSecretKey)
- Client cannot directly modify social data (server-authoritative)
- Data stored as Private in PlayFab User Data (client cannot read)

### Error Handling

**Failure Scenarios**:
- Invalid PlayFabId → Callback with (null, 0, false)
- Null social data → Callback with (null, 0, false)
- PlayFab API error → Callback with defaults, error logged
- JSON parse error → Creates new default data

---

## Usage Example

### Complete Social Data Workflow

```csharp
// Server-side social system
public class SocialManager : NetworkBehaviour
{
    [Server]
    public void AddFriend(string playerId, string friendId)
    {
        // Load current social data
        PlayFabSocialService.Instance.LoadSocialData(playerId, (socialData, version, success) =>
        {
            if (!success)
            {
                Debug.LogError($"Failed to load social data for {playerId}");
                return;
            }

            // Modify data
            if (!socialData.friendsList.Contains(friendId))
            {
                socialData.friendsList.Add(friendId);

                // Save with optimistic locking
                PlayFabSocialService.Instance.SaveSocialData(playerId, socialData, version,
                    (newVersion, saveSuccess) =>
                    {
                        if (saveSuccess)
                        {
                            Debug.Log($"Friend added: {playerId} → {friendId} (v{newVersion})");
                        }
                        else
                        {
                            Debug.LogError($"Failed to save social data for {playerId}");
                        }
                    });
            }
        });
    }
}
```

---

## Key Takeaways

1. **Server-Authoritative**: Only runs on server builds, uses PlayFab Server API
2. **Optimistic Locking**: Version numbers prevent concurrent modification bugs
3. **Caching Integration**: Designed to work with SocialDataManager's in-memory cache
4. **Default Creation**: Auto-creates empty social data for new players
5. **Security**: DeveloperSecretKey loaded from environment (never hardcoded)
6. **Private Storage**: Data stored with Private permission in PlayFab User Data
