# PortChatHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/PortChatHandler.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~111 |
| **Phase** | Phase 2: Port text chat |
| **Architecture** | Server-side port-specific chat routing |

## Purpose
Handles port-specific chat routing. Only sends messages to players currently docked in the same port zone. Server-side filtering ensures messages don't leak to players at sea or in different ports.

---

## Dependencies

```csharp
private ChatManager chatManager;
private PortZoneManager portZoneManager;
```

---

## Server API

```csharp
[Server]
public void SendPortMessage(NetworkConnectionToClient sender, ChatMessage message)
```

---

## Message Flow

```
1. Player sends message with ChatChannel.Port
2. ChatManager routes to PortChatHandler.SendPortMessage()
3. Server gets sender's current port from PortZoneManager
4. If not in port → send error to sender
5. Get all ships in same port
6. Send message to each ship via TargetRpc
```

---

## Server Logic

```csharp
[Server]
public void SendPortMessage(NetworkConnectionToClient sender, ChatMessage message)
{
    // Get sender's current port
    string currentPort = portZoneManager.GetShipCurrentPort(sender.identity);

    if (string.IsNullOrEmpty(currentPort))
    {
        TargetPortError(sender, "You must be in a port to use port chat!");
        return;
    }

    // Get all ships in the same port
    var shipsInPort = portZoneManager.GetShipsInPort(currentPort);

    // Send to each ship
    foreach (var ship in shipsInPort)
    {
        if (ship?.connectionToClient != null)
        {
            TargetReceivePortMessage(ship.connectionToClient, message, currentPort);
        }
    }
}
```

---

## Client RPCs

```csharp
// Receive port message
[TargetRpc]
private void TargetReceivePortMessage(NetworkConnection target, ChatMessage message, string portName)

// Receive error (not in port)
[TargetRpc]
private void TargetPortError(NetworkConnection target, string errorMessage)
```

---

## Error Handling

```csharp
[TargetRpc]
private void TargetPortError(NetworkConnection target, string errorMessage)
{
    ChatHistory history = FindFirstObjectByType<ChatHistory>();
    if (history != null)
    {
        ChatMessage error = new ChatMessage("", errorMessage, ChatChannel.System,
                                            MessagePriority.Important);
        history.AddMessage(error);
    }
}
```

---

## Usage Example

```csharp
// Called by ChatManager when channel is Port
chatManager.PortChatHandler.SendPortMessage(senderConnection, message);

// Player receives if in same port:
// [PORT] CaptainJoe: Anyone need repairs?
```

---

## Integration Points

### Dependencies
- `ChatManager` - Routing from main manager
- `PortZoneManager` - Port location queries
- `ChatHistory` - Store received messages
- `WOS.Debugging.DebugManager` - Logging

### Integration with PortZoneManager
```csharp
// Required methods from PortZoneManager:
string GetShipCurrentPort(NetworkIdentity ship)
List<NetworkIdentity> GetShipsInPort(string portName)
```

---

## Design Notes

### Server-Side Filtering
- All filtering done on server
- Clients can't receive messages from other ports
- Prevents information leakage

### Port Requirement
- Must be docked in a port to send/receive
- Error message sent if trying to use at sea

### Phase 2 Feature
- Text chat only initially
- Phase 3 adds voice chat for ports
