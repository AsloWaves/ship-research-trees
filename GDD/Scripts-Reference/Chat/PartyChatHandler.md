# PartyChatHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/PartyChatHandler.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~73 |
| **Phase** | Phase 2: Party text chat |
| **Architecture** | Server-side party-specific chat routing |

## Purpose
Handles party-specific chat routing. Only sends messages to players in the same party group. Server-side filtering using PartyManager for membership validation.

---

## Dependencies

```csharp
private ChatManager chatManager;
private PartyManager partyManager;
```

---

## Server API

```csharp
[Server]
public void SendPartyMessage(NetworkConnectionToClient sender, ChatMessage message)
```

---

## Message Flow

```
1. Player sends message with ChatChannel.Party
2. ChatManager routes to PartyChatHandler.SendPartyMessage()
3. Server gets sender's party from PartyManager
4. If not in party → message dropped (or error sent)
5. Get all party members
6. Send message to each member via TargetRpc
```

---

## Current Implementation (Placeholder)

```csharp
[Server]
public void SendPartyMessage(NetworkConnectionToClient sender, ChatMessage message)
{
    if (sender == null || sender.identity == null)
        return;

    // NOTE: Placeholder - needs PartyManager integration
    // TODO: Get party by connection ID
    // TODO: Send to all party members

    // Currently just echoes back to sender
    TargetReceivePartyMessage(sender, message);
}
```

---

## Client RPC

```csharp
[TargetRpc]
private void TargetReceivePartyMessage(NetworkConnection target, ChatMessage message)
{
    ChatHistory history = FindFirstObjectByType<ChatHistory>();
    if (history != null)
    {
        history.AddMessage(message);
    }
}
```

---

## Required PartyManager Integration

To fully implement, PartyManager needs:

```csharp
// Required methods:
string GetPlayerParty(uint connectionId)
List<uint> GetPartyMembers(string partyId)
bool IsInParty(uint connectionId)
```

---

## Usage Example

```csharp
// Called by ChatManager when channel is Party
chatManager.PartyChatHandler.SendPartyMessage(senderConnection, message);

// Party members receive:
// [PARTY] CaptainJoe: Form up on my position!
```

---

## Integration Points

### Dependencies
- `ChatManager` - Routing from main manager
- `PartyManager` - Party membership queries
- `ChatHistory` - Store received messages
- `WOS.Debugging.DebugManager` - Logging

### TODOs
- Add method to PartyManager to get party by connection ID
- Implement full party member iteration
- Add error handling for non-party members

---

## Design Notes

### Server-Side Filtering
- All filtering done on server
- Non-party members can't receive party messages
- Prevents eavesdropping

### Party Requirement
- Must be in a party to send/receive
- Should show error if sending without party

### Phase 2 Feature
- Text chat only initially
- Party voice chat added in same phase
