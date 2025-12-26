# GuildManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Guild/GuildManager.cs` |
| **Namespace** | `WOS.Guild` |
| **Inheritance** | `NetworkBehaviour` |
| **Pattern** | Singleton |
| **Lines** | ~844 |
| **Architecture** | Server-authoritative guild management |

## Purpose
Server-authoritative guild system manager handling guild creation, membership, invites, officer management, and permissions. Ensures unique guild names and tags.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `enableGuilds` | true | Enable guild system |
| `defaultMaxMembers` | 50 | Default guild size |
| `minGuildNameLength` | 3 | Minimum name length |
| `maxGuildNameLength` | 30 | Maximum name length |
| `guildTagLength` | 3 | Required tag length |
| `inviteExpirationSeconds` | 300 (5 min) | Invite expiration |

---

## Server State

```csharp
// Guild storage (guildId -> GuildData)
private Dictionary<string, GuildData> activeGuilds;

// Player membership (connectionId -> guildId)
private Dictionary<uint, string> playerGuilds;

// Pending invites
private List<GuildInvite> pendingInvites;

// Uniqueness tracking
private HashSet<string> usedGuildNames;  // Case-insensitive
private HashSet<string> usedGuildTags;   // Case-insensitive
```

---

## Commands (Client → Server)

### Guild Lifecycle
```csharp
[Command] public void CmdCreateGuild(string guildName, string guildTag)
[Command] public void CmdLeaveGuild()
[Command] public void CmdDisbandGuild()  // Leader only
```

### Invites
```csharp
[Command] public void CmdInviteToGuild(string targetPlayerName)
[Command] public void CmdAcceptGuildInvite(string guildId)
[Command] public void CmdDeclineGuildInvite(string guildId)
```

### Member Management
```csharp
[Command] public void CmdKickFromGuild(uint targetConnectionId)
[Command] public void CmdPromoteToOfficer(uint targetConnectionId)  // Leader only
[Command] public void CmdDemoteOfficer(uint targetConnectionId)     // Leader only
[Command] public void CmdUpdateGuildDescription(string newDescription)
```

---

## GuildInvite Struct

```csharp
[Serializable]
public struct GuildInvite
{
    public string guildId;
    public uint inviterId;
    public uint inviteeId;
    public string inviterName;
    public string guildName;
    public string guildTag;
    public DateTime sentTime;
    public float expireTimeSeconds;

    public bool IsExpired => (DateTime.Now - sentTime).TotalSeconds > expireTimeSeconds;
}
```

---

## Permission Rules

| Action | Leader | Officer | Member |
|--------|--------|---------|--------|
| Create guild | ✅* | - | - |
| Invite members | ✅ | ✅ | ❌ |
| Kick members | ✅ | ✅** | ❌ |
| Promote officer | ✅ | ❌ | ❌ |
| Demote officer | ✅ | ❌ | ❌ |
| Update description | ✅ | ✅ | ❌ |
| Disband guild | ✅ | ❌ | ❌ |

*Not in any guild
**Officers cannot kick other officers

---

## Public API

```csharp
// Get player's guild ID
public string GetPlayerGuild(uint connectionId)

// Get guild data
public GuildData? GetGuild(string guildId)

// Check if player is in a guild
public bool IsInGuild(uint connectionId)
```

---

## Client RPCs

### Targeted
| RPC | Purpose |
|-----|---------|
| `TargetGuildCreated` | Confirm creation |
| `TargetGuildInviteSent` | Confirm invite sent |
| `TargetGuildInviteReceived` | Show invite popup |
| `TargetGuildInviteDeclined` | Confirm decline |
| `TargetGuildJoined` | Confirm join |
| `TargetGuildLeft` | Confirm leave |
| `TargetGuildKicked` | Notify kicked |
| `TargetGuildDisbanded` | Notify disbanded |
| `TargetGuildNotification` | General notifications |
| `TargetGuildError` | Error messages |

---

## Disconnect Handling

```csharp
[Server]
private void OnPlayerDisconnected(NetworkConnectionToClient conn)
{
    uint connectionId = (uint)conn.connectionId;

    if (playerGuilds.TryGetValue(connectionId, out string guildId))
    {
        if (guild.IsLeader(connectionId))
        {
            // Leader disconnect = disband guild
            DisbandGuild(guildId, "Guild leader disconnected");
        }
        else
        {
            // Member disconnect = remove from guild
            guild.RemoveMember(connectionId);
            NotifyGuildMembers(guildId, $"{playerName} has disconnected");
        }
    }

    // Remove pending invites
    pendingInvites.RemoveAll(inv =>
        inv.inviterId == connectionId || inv.inviteeId == connectionId);
}
```

---

## Usage Example

```csharp
// Create guild
GuildManager.Instance.CmdCreateGuild("Sea Wolves", "WLF");

// Invite player
GuildManager.Instance.CmdInviteToGuild("SailorJoe");

// Accept invite
GuildManager.Instance.CmdAcceptGuildInvite(guildId);

// Promote to officer (leader only)
GuildManager.Instance.CmdPromoteToOfficer(memberId);

// Update description
GuildManager.Instance.CmdUpdateGuildDescription("Elite naval fleet");

// Check membership
if (GuildManager.Instance.IsInGuild(connectionId))
    Debug.Log($"In guild: {GuildManager.Instance.GetPlayerGuild(connectionId)}");
```

---

## Integration Points

### Dependencies
- `Mirror` - Networking
- `WOS.Debugging.DebugManager` - Logging

### TODOs
- AccountManager integration for player names
- Persistent storage for guilds

---

## Design Notes

### Uniqueness Enforcement
- Guild names are case-insensitive unique
- Guild tags are case-insensitive unique
- HashSets track used names/tags

### Leader Disconnection
- If leader disconnects, guild is disbanded
- All members notified with reason
- Consider: transfer to officer instead

### Invite System
- 5-minute expiration (vs 30s for parties)
- Longer for more serious commitment
