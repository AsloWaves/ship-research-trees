# GuildData.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Guild/GuildData.cs` |
| **Namespace** | `WOS.Guild` |
| **Lines** | ~93 |
| **Architecture** | Data structures for guild/clan system |

## Purpose
Defines data structures for the guild (clan) system with hierarchical ranks, officer promotion, and configurable max members.

---

## GuildData Struct

```csharp
[Serializable]
public struct GuildData
{
    public string guildId;          // Unique GUID
    public string guildName;        // Display name (3-30 chars)
    public string guildTag;         // Short tag (3 chars, e.g., [WOS])
    public uint leaderId;           // Leader connection ID
    public List<uint> memberIds;    // All members (including leader)
    public List<uint> officerIds;   // Officers (subset of members)
    public DateTime createdTime;    // Creation timestamp
    public int maxMembers;          // Default: 50
    public string description;      // Guild description

    public GuildData(uint leaderId, string name, string tag, int maxMembers = 50);
}
```

### Properties
| Property | Description |
|----------|-------------|
| `IsFull` | True if memberIds.Count >= maxMembers |
| `MemberCount` | Current member count |

### Methods
| Method | Description |
|--------|-------------|
| `IsLeader(uint)` | Check if connection is guild leader |
| `IsOfficer(uint)` | Check if connection is officer |
| `IsMember(uint)` | Check if connection is member |
| `AddMember(uint)` | Add member (returns false if full/exists) |
| `RemoveMember(uint)` | Remove member (also removes from officers) |

---

## GuildRank Enum

```csharp
public enum GuildRank
{
    Leader,     // Full permissions
    Officer,    // Can invite/kick members
    Member      // Basic member
}
```

### Permission Matrix
| Action | Leader | Officer | Member |
|--------|--------|---------|--------|
| Invite members | ✅ | ✅ | ❌ |
| Kick members | ✅ | ✅* | ❌ |
| Promote to officer | ✅ | ❌ | ❌ |
| Demote officer | ✅ | ❌ | ❌ |
| Update description | ✅ | ✅ | ❌ |
| Disband guild | ✅ | ❌ | ❌ |

*Officers cannot kick other officers

---

## Usage Example

```csharp
// Create a guild
GuildData guild = new GuildData(
    leaderId: 1,
    name: "Sea Wolves",
    tag: "WLF",
    maxMembers: 50
);

// Check ranks
if (guild.IsLeader(connectionId))
    Debug.Log("You are the guild leader");
else if (guild.IsOfficer(connectionId))
    Debug.Log("You are an officer");
else if (guild.IsMember(connectionId))
    Debug.Log("You are a member");

// Add member
if (!guild.IsFull)
    guild.AddMember(newMemberId);

// Remove member (also removes officer status)
guild.RemoveMember(leavingMemberId);
```

---

## Integration Points

### Used By
- `GuildManager` - Server-side guild management
- Voice system - Guild voice rooms

---

## Design Notes

### Guild Tags
- 3-character tags for display
- Shown in brackets: [WOS]
- Must be unique across server

### Officer System
- Officers are a subset of members
- Removing member auto-removes officer status
- Leader cannot be an officer (separate role)

### Size Limits
- Default 50 members
- Configurable per guild
