# PartyData.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Party/PartyData.cs` |
| **Namespace** | `WOS.Party` |
| **Lines** | ~101 |
| **Architecture** | Data structures for party/fleet system |

## Purpose
Defines data structures for the party (fleet group) system, supporting 4-8 players per party with leader, members, and time-limited invites.

---

## PartyData Struct

```csharp
[Serializable]
public struct PartyData
{
    public string partyId;          // Unique GUID
    public uint leaderId;           // Leader connection ID
    public List<uint> memberIds;    // All member connection IDs
    public string partyName;        // "Fleet {id.Substring(0,6)}"
    public DateTime createdTime;    // Creation timestamp
    public int maxMembers;          // Default: 8

    public PartyData(uint leaderId, int maxMembers = 8);
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
| `IsLeader(uint)` | Check if connection is leader |
| `IsMember(uint)` | Check if connection is member |
| `AddMember(uint)` | Add member (returns false if full/exists) |
| `RemoveMember(uint)` | Remove member by connection ID |

---

## PartyInvite Struct

```csharp
[Serializable]
public struct PartyInvite
{
    public string partyId;              // Target party
    public uint inviterId;              // Sender connection ID
    public uint inviteeId;              // Recipient connection ID
    public string inviterName;          // Display name
    public DateTime sentTime;           // Sent timestamp
    public float expireTimeSeconds;     // Default: 30s

    public PartyInvite(string partyId, uint inviterId, uint inviteeId,
                       string inviterName, float expireTime = 30f);
}
```

### Properties
| Property | Description |
|----------|-------------|
| `IsExpired` | True if (Now - sentTime) > expireTimeSeconds |

---

## Usage Example

```csharp
// Create a party
PartyData party = new PartyData(leaderId: 1, maxMembers: 8);

// Check status
if (!party.IsFull)
    party.AddMember(2);

Debug.Log($"Party {party.partyId}: {party.MemberCount} members");

// Create invite
PartyInvite invite = new PartyInvite(
    party.partyId,
    inviterId: 1,
    inviteeId: 3,
    inviterName: "Captain",
    expireTime: 30f
);

if (!invite.IsExpired)
    Debug.Log("Invite still valid");
```

---

## Integration Points

### Used By
- `PartyManager` - Server-side party management
- `PartyVoiceHandler` - Party voice chat rooms

---

## Design Notes

### Fleet Metaphor
- Parties called "Fleets" in UI
- Auto-generated names: "Fleet abc123"
- Supports 4-8 players (configurable)

### Invite Expiration
- Default 30 second expiration
- Prevents invite spam and stale invites
