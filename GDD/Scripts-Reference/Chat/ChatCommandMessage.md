# ChatCommandMessage.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/ChatCommandMessage.cs` |
| **Namespace** | `WOS.Chat` |
| **Type** | `struct` implementing `NetworkMessage` |
| **Lines** | ~14 |
| **Architecture** | Network message for client-to-server chat |

## Purpose
Network message structure for sending chat messages from client to server. Replaces the `[Command]` pattern which requires client authority over the NetworkIdentity.

---

## Struct Definition

```csharp
public struct ChatCommandMessage : NetworkMessage
{
    public string content;      // Message text
    public ChatChannel channel; // Target channel
}
```

---

## Why NetworkMessage Instead of Command?

### Problem with [Command]
```csharp
// This requires client to have authority over the object
[Command]
public void CmdSendMessage(string content, ChatChannel channel) { }
```

Commands require the client to have authority over the NetworkIdentity, which isn't always the case with shared managers like ChatManager.

### Solution: NetworkMessage
```csharp
// Client sends message without authority requirement
ChatCommandMessage msg = new ChatCommandMessage
{
    content = "Hello world",
    channel = ChatChannel.World
};
NetworkClient.Send(msg);
```

---

## Message Flow

```
Client                          Server
  |                               |
  |--- ChatCommandMessage ------->|
  |                               | → ChatManager.ProcessChatMessage()
  |                               | → Validate, filter, sanitize
  |<-- RpcReceiveMessage ---------|
  |                               |
```

---

## Server-Side Handler

Registered in `WOSNetworkManager.OnStartServer()`:

```csharp
NetworkServer.RegisterHandler<ChatCommandMessage>(OnChatMessageReceived);

private void OnChatMessageReceived(NetworkConnectionToClient conn, ChatCommandMessage msg)
{
    // Get ChatManager and process
    chatManager.ProcessChatMessageFromNetwork(conn, msg.content, msg.channel);
}
```

---

## Usage Example

```csharp
// Client sending chat message
public void SendChatMessage(string text, ChatChannel channel)
{
    if (!NetworkClient.active) return;

    ChatCommandMessage msg = new ChatCommandMessage
    {
        content = text,
        channel = channel
    };

    NetworkClient.Send(msg);
}
```

---

## Integration Points

### Dependencies
- `Mirror` - NetworkMessage interface

### Used By
- `ChatPanel` (UI) - Sends messages when user presses Enter
- `ChatCommands` - Sends /roll results
- `WOSNetworkManager` - Registers server handler

---

## Design Notes

### Early Registration
Handler must be registered in `WOSNetworkManager.OnStartServer()` before any clients connect. This is critical for HOST mode where the local client connects immediately.

### Minimal Structure
Only sends essential data (content + channel). Server adds sender name, timestamp, and performs validation.
