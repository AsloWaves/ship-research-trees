# ChatHistory.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/ChatHistory.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~152 |
| **Architecture** | Per-channel message storage with automatic cleanup |

## Purpose
Manages chat message history per channel. Stores up to 200 messages per channel with automatic cleanup, tracks unread counts, and fires events when messages arrive.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `maxMessagesPerChannel` | 200 | Maximum messages stored per channel |

---

## State

```csharp
// Message history per channel
private Dictionary<ChatChannel, List<ChatMessage>> channelHistory;

// Unread count per channel
private Dictionary<ChatChannel, int> unreadCount;
```

---

## Events

```csharp
// Fired when a new message is added
public event System.Action<ChatMessage> OnMessageAdded;
```

---

## Public API

### Message Management
```csharp
// Add message to channel
public void AddMessage(ChatMessage message)

// Get all messages for channel (returns copy)
public List<ChatMessage> GetMessages(ChatChannel channel)

// Get last N messages for channel
public List<ChatMessage> GetRecentMessages(ChatChannel channel, int count)

// Clear specific channel
public void ClearChannel(ChatChannel channel)

// Clear all channels
public void ClearAll()
```

### Unread Tracking
```csharp
// Get unread count for channel
public int GetUnreadCount(ChatChannel channel)

// Mark channel as read
public void MarkAsRead(ChatChannel channel)

// Get total message count
public int GetMessageCount(ChatChannel channel)
```

---

## Auto-Cleanup

When messages exceed the limit, oldest are removed:

```csharp
public void AddMessage(ChatMessage message)
{
    history.Add(message);
    unreadCount[message.channel]++;

    // Auto-cleanup old messages
    if (history.Count > maxMessagesPerChannel)
    {
        int removeCount = history.Count - maxMessagesPerChannel;
        history.RemoveRange(0, removeCount);  // Remove oldest
    }

    OnMessageAdded?.Invoke(message);
}
```

---

## Initialization

All channels initialized on Awake:

```csharp
private void InitializeChannels()
{
    foreach (ChatChannel channel in Enum.GetValues(typeof(ChatChannel)))
    {
        channelHistory[channel] = new List<ChatMessage>();
        unreadCount[channel] = 0;
    }
}
```

---

## Usage Example

```csharp
// Add message
ChatMessage msg = new ChatMessage("Player1", "Hello!", ChatChannel.World);
chatHistory.AddMessage(msg);

// Get recent messages for display
var recent = chatHistory.GetRecentMessages(ChatChannel.World, 50);

// Check unread count for tab badge
int unread = chatHistory.GetUnreadCount(ChatChannel.Party);
if (unread > 0)
    partyTab.ShowBadge(unread);

// Mark as read when tab selected
chatHistory.MarkAsRead(ChatChannel.Party);

// Subscribe to new messages
chatHistory.OnMessageAdded += OnNewMessage;
```

---

## Integration Points

### Dependencies
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `ChatPanel` (UI) - Displays messages
- `ChatManager` - Stores received messages
- `MentionSystem` - Adds notification messages
- All chat handlers

---

## Design Notes

### Memory Management
- 200 messages per channel = ~1,400 max total
- Automatic cleanup prevents memory growth
- Returns copies to prevent external modification

### Unread Tracking
- Incremented on every AddMessage
- UI should call MarkAsRead when channel is viewed
- Used for tab badge notifications

### Event-Driven
- OnMessageAdded allows UI to react immediately
- Decouples history from display logic
