---
tags: [script, networking, playfab, persistence, crew, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Networking.Managers
file-path: Assets/Scripts/Networking/Managers/PlayFabCrewService.cs
status: IMPLEMENTED
size: ~8 KB (313 lines)
feature-group: networking
---

# PlayFabCrewService.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Networking.Managers
**File**: `Assets/Scripts/Networking/Managers/PlayFabCrewService.cs`
**Size**: ~8 KB (313 lines)
**Dependencies**: PlayFab Server SDK, CrewCard

---

## Purpose
PlayFab-based crew persistence service. Provides read/write operations for player crew cards using PlayFab User Data API. Uses optimistic locking for conflict resolution.

This service manages:
- Crew card collection load/save via PlayFab
- Version-based optimistic locking
- JSON serialization via wrapper class
- Coroutine wrappers for Unity integration

---

## PlayFab Data Keys

```
KEY_CREW_CARDS      = "CrewCards"           // CrewCardList JSON wrapper
KEY_CREW_VERSION    = "CrewCardsVersion"    // Version for optimistic locking
KEY_CREW_LAST_SAVED = "CrewCardsLastSaved"  // UTC timestamp (ISO 8601)
```

---

## Singleton Access

```csharp
public static PlayFabCrewService Instance { get; }
```

Uses `FindFirstObjectByType<>()` for lazy initialization.

---

## Data Wrapper Class

```csharp
[Serializable]
private class CrewCardList
{
    public List<CrewCard> Cards = new List<CrewCard>();
}
```

Required because Unity's JsonUtility cannot serialize top-level List<T> directly.

---

## Public Methods

### LoadCrewCards
Loads player's crew cards from PlayFab.

```csharp
public void LoadCrewCards(
    string playFabId,
    Action<List<CrewCard>, int, bool> callback)
```

**Parameters**:
- `playFabId` - Player's PlayFab ID
- `callback` - Returns (crewCards, version, success)

**Behavior**:
- Fetches from PlayFab User Data API
- Creates empty list if no crew exists
- Parses JSON via CrewCardList wrapper

### SaveCrewCards
Saves player's crew cards to PlayFab.

```csharp
public void SaveCrewCards(
    string playFabId,
    List<CrewCard> crewCards,
    int currentVersion,
    Action<int, bool> callback)
```

**Parameters**:
- `playFabId` - Player's PlayFab ID
- `crewCards` - List of CrewCard to save
- `currentVersion` - Version for optimistic locking
- `callback` - Returns (newVersion, success)

**Behavior**:
- Wraps cards in CrewCardList for serialization
- Increments version number
- Saves to PlayFab with timestamp

---

## Coroutine Wrappers

### LoadCrewCardsCoroutine
```csharp
public IEnumerator LoadCrewCardsCoroutine(
    string playFabId,
    Action<List<CrewCard>, int, bool> callback)
```

### SaveCrewCardsCoroutine
```csharp
public IEnumerator SaveCrewCardsCoroutine(
    string playFabId,
    List<CrewCard> crewCards,
    int currentVersion,
    Action<int, bool> callback)
```

Use with `StartCoroutine()` for Unity-friendly async operations.

---

## Optimistic Locking

Same pattern as [[PlayFabShipService]]:

```
1. Load crew with current version
2. Make changes in memory
3. Save with current version
4. Version auto-incremented on save
5. Reload and retry on conflict
```

---

## Integration Points

### Dependencies
- **PlayFab.ServerModels** - GetUserData, UpdateUserData requests
- [[CrewCard]] - Crew data structure
- [[DebugManager]] - Logging

### Used By
- [[CrewManager]] - Caches and manages crew data
- [[WOSNetworkManager]] - Loads crew on player connect

---

## PlayFab Configuration

```csharp
public bool ValidatePlayFabConfiguration()
```

**Validates**:
- TitleId is configured in PlayFabSettings
- DeveloperSecretKey loaded from `PLAYFAB_SECRET_KEY` environment variable

---

## Error Handling

- Logs errors via DebugManager with `DebugCategory.Ship`
- Returns `false` success flag on API failures
- Creates empty list on load failure (graceful fallback)
- Handles JSON parse errors gracefully

---

## Comparison with PlayFabShipService

| Feature | PlayFabShipService | PlayFabCrewService |
|---------|-------------------|-------------------|
| Data Type | PlayerShipCollection | List<CrewCard> |
| Starter Data | Creates starter ship | Empty list |
| Auto-Save Starter | Yes | No (empty list OK) |
| Wrapper Class | No (collection is wrapper) | Yes (CrewCardList) |

---

## Related Files
- [[PlayFabShipService]] - Similar pattern for ship data
- [[PlayFabInventoryService]] - Inventory persistence
- [[CrewManager]] - Uses this service
- [[CrewCard]] - Crew data structure

---

## Testing Notes
- Requires server build with PlayFab Server SDK
- DeveloperSecretKey from environment variable
- New players start with empty crew list
- Crew cards assigned during gameplay

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added coroutine wrappers
- **2025-01**: Added version-based locking

