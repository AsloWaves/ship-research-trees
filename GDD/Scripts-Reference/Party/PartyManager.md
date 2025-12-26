# PartyManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Party/PartyManager.cs` |
| **Namespace** | `WOS.Party` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~542 |
| **Architecture** | Server-authoritative party management |

## Purpose
Server-authoritative party management system handling party creation, invites, kicks, leadership transfer, and disbanding. Integrates with AuthenticationManager for player names.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `maxPartySize` | 8 | Maximum members per party |
| `inviteExpirationTime` | 30s | How long invites last |

---

## Server State

```csharp
// Active parties (partyId -> PartyData)
private Dictionary<string, PartyData> activeParties;

// Player to party mapping (connectionId -> partyId)
private Dictionary<uint, string> playerParties;

// Pending invites
private List<PartyInvite> pendingInvites;

// Player names (connectionId -> playerName)
private Dictionary<uint, string> playerNames;
```

---

## Commands (Client → Server)

### Party Lifecycle
```csharp
[Command] public void CmdCreateParty()
[Command] public void CmdLeaveParty()
[Command] public void CmdDisbandParty()  // Leader only
```

### Invites
```csharp
[Command] public void CmdInviteToParty(string targetPlayerName)
[Command] public void CmdAcceptPartyInvite(string partyId)
[Command] public void CmdDeclinePartyInvite(string partyId)
```

### Management
```csharp
[Command] public void CmdKickFromParty(uint targetConnectionId)  // Leader only
```

---

## Client RPCs

### Targeted (Single Client)
| RPC | Purpose |
|-----|---------|
| `TargetPartyCreated` | Confirm party creation |
| `TargetPartyJoined` | Confirm join success |
| `TargetPartyLeft` | Confirm leave |
| `TargetPartyKicked` | Notify kicked from party |
| `TargetPartyDisbanded` | Notify party disbanded |
| `TargetReceivePartyInvite` | Show invite notification |
| `TargetPartyError` | Show error message |
| `TargetPartyInfo` | Show info message |

### Broadcast (All Clients)
| RPC | Purpose |
|-----|---------|
| `RpcPartyUpdate` | Sync party state |
| `RpcPartyMemberJoined` | Notify member joined |
| `RpcPartyMemberLeft` | Notify member left |
| `RpcPartyLeaderChanged` | Notify leader change |

---

## Leader Transfer Logic

```csharp
[Server]
private void RemovePlayerFromParty(uint connectionId, string partyId)
{
    party.RemoveMember(connectionId);
    playerParties.Remove(connectionId);

    // If party empty, remove it
    if (party.MemberCount == 0)
    {
        activeParties.Remove(partyId);
        return;
    }

    // If leader left, promote first member
    if (party.IsLeader(connectionId))
    {
        party.leaderId = party.memberIds[0];
        RpcPartyLeaderChanged(partyId, party.leaderId);
    }
}
```

---

## Validation Rules

| Action | Requirements |
|--------|--------------|
| Create party | Not already in a party |
| Invite player | Must be leader, party not full, target not in party |
| Accept invite | Not in party, invite not expired, party exists & not full |
| Kick player | Must be leader, target is member, can't kick self |
| Disband | Must be leader |

---

## Usage Example

```csharp
// Create a party
PartyManager.Instance.CmdCreateParty();

// Invite a player by name
PartyManager.Instance.CmdInviteToParty("SailorJoe");

// Accept invite
PartyManager.Instance.CmdAcceptPartyInvite(partyId);

// Leave party
PartyManager.Instance.CmdLeaveParty();

// Kick member (leader only)
PartyManager.Instance.CmdKickFromParty(targetConnectionId);

// Disband (leader only)
PartyManager.Instance.CmdDisbandParty();
```

---

## Integration Points

### Dependencies
- `AuthenticationManager` - Player name lookup
- `WOS.Debugging.DebugManager` - Logging
- `Mirror` - Networking

### Triggers For
- `PartyVoiceHandler` - Voice room join/leave

---

## Design Notes

### Server Authority
- All party logic runs on server
- Clients can only request actions
- Server validates all operations

### Name Resolution
- Uses `AuthenticationManager.GetUsername()`
- Falls back to "Player{connectionId}"

### Auto Leader Transfer
- When leader leaves, first member becomes leader
- Empty parties auto-disband
