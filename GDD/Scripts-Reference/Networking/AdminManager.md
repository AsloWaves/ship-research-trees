# AdminManager.cs

## Quick Reference

| **File** | AdminManager.cs |
|----------|----------------|
| **Namespace** | WOS.Networking.Managers |
| **Inheritance** | MonoBehaviour |
| **Lines** | 389 |
| **Architecture** | Singleton, PlayFab User Data (Read-Only), server-authoritative |

---

## Purpose

Server-authoritative admin role management system using PlayFab Read-Only User Data for secure permission storage.

**Security Model**:
- Admin status stored in PlayFab Read-Only User Data (cannot be modified by client)
- Loaded during authentication and cached server-side
- All admin commands validate against cached status
- Runs server-side only

---

## Admin Levels

| Level | Name | Permissions |
|-------|------|-------------|
| 0 | Player | No admin access |
| 1 | Moderator | Chat moderation, player reports |
| 2 | Game Master | Testing commands, player inspection |
| 3 | Developer | Full access, economy manipulation |
| 4 | Super Admin | Account management, server control |

---

## Configuration Setup

### PlayFab Game Manager

1. Navigate to: Players → [Player] → Player Data (Title)
2. Add key: `AdminLevel`
3. Set value: `"1"`, `"2"`, `"3"`, or `"4"`
4. Set permission: **Read Only** (prevents client modification)

---

## Public API

### Admin Status Loading

#### `LoadAdminStatus(string playFabId, Action<int> callback)`
Loads admin status from PlayFab during authentication.

**Parameters**:
- `playFabId` - PlayFab ID
- `callback` - Callback with admin level

**Example**:
```csharp
AdminManager.Instance.LoadAdminStatus(playFabId, adminLevel =>
{
    Debug.Log($"Admin level: {adminLevel}");
});
```

#### `UnloadAdminStatus(string playFabId)`
Unloads admin status when player disconnects.

#### `SetLocalTestAdminLevel(string playerId, int adminLevel)`
Sets admin level for local testing (bypasses PlayFab).

**Example**:
```csharp
// Unity Editor testing
AdminManager.Instance.SetLocalTestAdminLevel("test_player", AdminManager.LEVEL_DEVELOPER);
```

### Admin Validation

#### `GetAdminLevel(string playFabId)`
Gets admin level by PlayFab ID.

**Returns**: `int` (0-4)

#### `GetAdminLevelByConnection(int connectionId)`
Gets admin level by Mirror connection ID.

**Returns**: `int` (0-4)

#### `HasAdminLevel(string playFabId, int requiredLevel)`
Checks if player has at least specified admin level.

**Returns**: `bool`

**Example**:
```csharp
if (AdminManager.Instance.HasAdminLevel(playFabId, AdminManager.LEVEL_GAME_MASTER))
{
    // Allow GM command
}
```

#### `IsAdmin(string playFabId)`
Checks if player is any type of admin (level >= 1).

**Returns**: `bool`

### Utility Methods

#### `GetAdminLevelName(int level)`
Gets human-readable name for admin level.

**Returns**: `string` ("Player", "Moderator", "Game Master", "Developer", "Super Admin")

#### `GetRequiredLevel(AdminPermission permission)`
Gets required admin level for specific permission.

**Returns**: `int`

**Example**:
```csharp
int requiredLevel = AdminManager.GetRequiredLevel(AdminPermission.BanPlayer);
// Returns: LEVEL_SUPER_ADMIN (4)
```

---

## AdminPermission Enum

```csharp
public enum AdminPermission
{
    // Moderator (Level 1)
    MutePlayer,
    KickPlayer,
    ViewReports,

    // Game Master (Level 2)
    AddCrewXP,
    ApplyCasualties,
    InspectPlayer,
    TeleportPlayer,
    SpawnItems,

    // Developer (Level 3)
    GiveCurrency,
    GiveShip,
    ModifyInventory,
    ToggleGodMode,

    // Super Admin (Level 4)
    BanPlayer,
    ResetPlayerData,
    ServerControl,
    GrantAdminRights
}
```

---

## Usage Example

### Command Validation

```csharp
[Server]
public void HandleAdminCommand(NetworkConnection conn, AdminPermission permission)
{
    // Get required level for permission
    int requiredLevel = AdminManager.GetRequiredLevel(permission);

    // Check if player has permission
    if (!AdminManager.Instance.HasAdminLevelByConnection(conn.connectionId, requiredLevel))
    {
        Debug.LogWarning($"Unauthorized admin command from connection {conn.connectionId}");
        return;
    }

    string username = AccountManager.Instance.GetUsername(conn.connectionId);
    Debug.Log($"Admin command {permission} executed by {username}");

    // Execute command...
}
```

### Authentication Integration

```csharp
// AuthenticationManager.cs
private void OnPlayerAuthenticated(string playFabId, NetworkConnection conn)
{
    // Load admin status
    AdminManager.Instance.LoadAdminStatus(playFabId, adminLevel =>
    {
        if (adminLevel > 0)
        {
            string levelName = AdminManager.GetAdminLevelName(adminLevel);
            Debug.Log($"Admin connected: {playFabId} ({levelName})");
        }

        // Continue with player setup...
    });
}
```

---

## Design Notes

### Security Architecture

**Read-Only User Data**:
- Stored in PlayFab with Read-Only permission
- Clients cannot modify their own admin level
- Only Game Manager (web console) can change admin status
- Server loads from PlayFab on authentication

**Server-Side Validation**:
```csharp
// Client CANNOT do this (no access to AdminManager)
AdminManager.Instance.SetLocalTestAdminLevel(...); // Server-only

// Client CAN request, but server validates
[ServerRpc]
void CmdBanPlayer(string targetPlayerId)
{
    // Server validates permission
    if (!AdminManager.Instance.HasAdminLevel(playFabId, LEVEL_SUPER_ADMIN))
    {
        return; // Rejected
    }
    // Execute...
}
```

### Admin Level Hierarchy

Higher levels inherit all lower-level permissions:

```
Super Admin (4) → Can do everything
    ↓
Developer (3) → Can do Dev + GM + Mod permissions
    ↓
Game Master (2) → Can do GM + Mod permissions
    ↓
Moderator (1) → Can do Mod permissions
    ↓
Player (0) → No admin permissions
```

---

## Key Takeaways

1. **Server-Authoritative**: Admin status validated server-side only
2. **PlayFab Integration**: Uses Read-Only User Data for secure storage
3. **Permission System**: Granular permissions with hierarchical levels
4. **Authentication Integration**: Loads automatically during player authentication
5. **Testing Support**: Local test mode for Unity Editor development
