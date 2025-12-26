# SystemMessageHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/SystemMessageHandler.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~201 |
| **Phase** | Phase 1: Server announcements |
| **Architecture** | Server-side automatic system message generation |

## Purpose
Handles system messages and server announcements. Automatically broadcasts player join/leave notifications, combat logs, maintenance warnings, and custom server announcements.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `announcePlayerJoin` | true | Announce when players join |
| `announcePlayerLeave` | true | Announce when players leave |
| `showConnectionMessages` | true | Show connection status messages |

---

## Server Events

### OnStartServer
```csharp
public override void OnStartServer()
{
    // Welcome message
    chatManager.SendSystemMessage("🌊 Welcome to Waves of Steel! Server is online.",
                                   MessagePriority.Important);
    chatManager.SendSystemMessage("Type /help for available commands.",
                                   MessagePriority.Normal);

    // Subscribe to connection events
    NetworkServer.OnConnectedEvent += OnPlayerConnected;
    NetworkServer.OnDisconnectedEvent += OnPlayerDisconnected;
}
```

### Player Connect/Disconnect
```csharp
private void OnPlayerConnected(NetworkConnectionToClient conn)
{
    string playerName = GetPlayerName(conn);
    chatManager.SendSystemMessage($"⚓ {playerName} has joined the fleet!",
                                   MessagePriority.Normal);
}

private void OnPlayerDisconnected(NetworkConnectionToClient conn)
{
    string playerName = GetPlayerName(conn);
    chatManager.SendSystemMessage($"⚓ {playerName} has left the fleet.",
                                   MessagePriority.Normal);
}
```

---

## Public API (Server)

### Announcements
```csharp
[Server]
public void SendAnnouncement(string message, MessagePriority priority = MessagePriority.Important)
// Sends: 📢 {message}
```

### Combat Log
```csharp
[Server]
public void SendCombatLog(string attacker, string target, int damage, bool killed = false)
// Sends: ⚔️ {attacker} hit {target} for {damage} damage
// Or:    💀 {attacker} destroyed {target}!
```

### Server Warnings
```csharp
[Server]
public void SendServerWarning(string warning)
// Sends: ⚠️ {warning} with MessagePriority.Urgent
```

### Maintenance Notices
```csharp
[Server]
public void SendMaintenanceNotice(int minutesUntilShutdown)
// Sends: 🔧 Server maintenance in X minute(s). Please prepare to disconnect.
```

---

## Client Events

```csharp
public override void OnStartClient()
{
    // Local client connection confirmation
    history.AddMessage(new ChatMessage("", "✅ Connected to server",
                       ChatChannel.System, MessagePriority.Important));
    history.AddMessage(new ChatMessage("", "Type /help for available commands",
                       ChatChannel.System));
}

public override void OnStopClient()
{
    // Local client disconnection
    history.AddMessage(new ChatMessage("", "❌ Disconnected from server",
                       ChatChannel.System, MessagePriority.Important));
}
```

---

## Player Name Resolution

```csharp
private string GetPlayerName(NetworkConnectionToClient conn)
{
    // Try AuthenticationManager first
    if (AuthenticationManager.Instance != null)
    {
        string username = AuthenticationManager.Instance.GetUsername(conn.connectionId);
        if (!string.IsNullOrEmpty(username))
            return username;
    }

    // Fallback
    return $"Player{conn.connectionId}";
}
```

---

## Message Icons

| Type | Icon | Priority |
|------|------|----------|
| Welcome | 🌊 | Important |
| Join/Leave | ⚓ | Normal |
| Announcement | 📢 | Important |
| Combat Hit | ⚔️ | Normal |
| Combat Kill | 💀 | Normal |
| Warning | ⚠️ | Urgent |
| Maintenance | 🔧 | Urgent |
| Connect | ✅ | Important |
| Disconnect | ❌ | Important |

---

## Usage Example

```csharp
// Server admin announcement
systemMessageHandler.SendAnnouncement("Double XP weekend starts now!");

// Combat log
systemMessageHandler.SendCombatLog("USS Enterprise", "Enemy Destroyer", 150, false);
// Output: ⚔️ USS Enterprise hit Enemy Destroyer for 150 damage

// Kill notification
systemMessageHandler.SendCombatLog("USS Enterprise", "Enemy Destroyer", 0, true);
// Output: 💀 USS Enterprise destroyed Enemy Destroyer!

// Maintenance warning
systemMessageHandler.SendMaintenanceNotice(5);
// Output: 🔧 Server maintenance in 5 minutes. Please prepare to disconnect.
```

---

## Integration Points

### Dependencies
- `ChatManager` - Send system messages
- `AuthenticationManager` - Get player names
- `ChatHistory` - Client-side message storage
- `NetworkServer` - Connection events
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Event Subscription
- Subscribe in OnStartServer
- Unsubscribe in OnStopServer
- Prevents memory leaks

### Client vs Server Messages
- Server messages go through ChatManager.SendSystemMessage()
- Client-only messages (connect/disconnect) added directly to ChatHistory

### Phase 1 Feature
- Core system messaging
- Foundation for all other chat features
