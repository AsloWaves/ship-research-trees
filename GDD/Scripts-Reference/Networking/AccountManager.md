# AccountManager.cs

## Quick Reference

| **File** | AccountManager.cs |
|----------|------------------|
| **Namespace** | WOS.Networking.Managers |
| **Inheritance** | MonoBehaviour |
| **Lines** | 119 |
| **Architecture** | Singleton, server-side connection tracking |

---

## Purpose

Server-side account data storage and lookup service. Maps Mirror connection IDs to player account IDs (PlayFab IDs) and usernames for persistence systems. Authentication is handled by AuthenticationManager via PlayFab SessionTickets.

---

## Public API

### Player Registration

#### `RegisterPlayer(int connectionId, string playerId, string username)`
Registers a connected player after successful PlayFab authentication.

**Parameters**:
- `connectionId` - Mirror connection ID
- `playerId` - PlayFab ID (UUID)
- `username` - Display username

**Example**:
```csharp
// After successful authentication
AccountManager.Instance.RegisterPlayer(conn.connectionId, playFabId, username);
```

#### `UnregisterPlayer(int connectionId)`
Unregisters a player when they disconnect.

**Example**:
```csharp
void OnServerDisconnect(NetworkConnection conn)
{
    AccountManager.Instance.UnregisterPlayer(conn.connectionId);
}
```

### Player Lookup

#### `GetPlayerId(int connectionId)`
Gets the player account ID for a connection.

**Returns**: `string` (PlayFab ID) or null

**Example**:
```csharp
string playerId = AccountManager.Instance.GetPlayerId(conn.connectionId);
```

#### `GetUsername(int connectionId)`
Gets the username for a connection.

**Returns**: `string` or null

#### `IsPlayerRegistered(int connectionId)`
Checks if a connection has a validated player account.

**Returns**: `bool`

### Statistics

#### `GetConnectedPlayerCount()`
Gets total number of connected authenticated players.

**Returns**: `int`

#### `GetAllConnectedPlayerIds()`
Gets all connected player IDs.

**Returns**: `List<string>`

---

## Usage Example

```csharp
[Server]
public void HandlePlayerRequest(NetworkConnection conn)
{
    // Validate player is authenticated
    if (!AccountManager.Instance.IsPlayerRegistered(conn.connectionId))
    {
        Debug.LogWarning("Unauthorized request from unauthenticated connection");
        return;
    }

    string playerId = AccountManager.Instance.GetPlayerId(conn.connectionId);
    string username = AccountManager.Instance.GetUsername(conn.connectionId);

    Debug.Log($"Request from {username} (ID: {playerId})");
    // Process request...
}
```

---

## Key Takeaways

1. **Connection Mapping**: Maps Mirror connection IDs to PlayFab IDs
2. **Server-Side Only**: Runs only on server builds
3. **Authentication Bridge**: Links Mirror networking to PlayFab identity
4. **Simple Lookup**: O(1) dictionary lookups for player data
