# ChatMessage.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/ChatMessage.cs` |
| **Namespace** | `WOS.Chat` |
| **Lines** | ~95 |
| **Architecture** | Data structures for chat system |

## Purpose
Defines core data structures for the chat system including message format, channel types, and priority levels. Supports 7 chat channels with color-coded formatting.

---

## ChatMessage Struct

```csharp
[Serializable]
public struct ChatMessage
{
    public string sender;           // Player name (empty for system)
    public string content;          // Message text (max 256 chars)
    public ChatChannel channel;     // Which channel
    public DateTime timestamp;      // When sent
    public MessagePriority priority; // Urgency level

    public ChatMessage(string sender, string content, ChatChannel channel,
                       MessagePriority priority = MessagePriority.Normal);
}
```

### Content Length Limit
```csharp
// Constructor auto-truncates to 256 characters
this.content = content.Length > 256 ? content.Substring(0, 256) : content;
```

---

## ChatChannel Enum

| Channel | Phase | Color | Description |
|---------|-------|-------|-------------|
| `System` | 1 | Gold (#FFD700) | Server announcements, combat log |
| `Proximity` | 1 | Green (#00FF00) | Ships within range |
| `World` | 1 | Deep Sky Blue (#00BFFF) | Server-wide |
| `Port` | 2 | Orange (#FFA500) | Port zones only |
| `Party` | 2 | Hot Pink (#FF69B4) | Group members |
| `Nation` | 4 | Orange Red (#FF4500) | Faction members |
| `Guild` | 5 | Medium Purple (#9370DB) | Guild members |

---

## MessagePriority Enum

| Priority | Behavior |
|----------|----------|
| `Normal` | Standard message |
| `Important` | Yellow badge on tab |
| `Urgent` | Red badge, play sound, flash tab |
| `Mention` | @Mention - Red badge, sound notification |

---

## Display Formatting

```csharp
public string FormatForDisplay(bool includeTimestamp = true)
{
    // Format: [HH:mm] [CHANNEL] PlayerName: message
    string prefix = GetChannelPrefix();      // e.g., [WORLD]
    string coloredName = $"<color={color}>{sender}</color>: ";
    string timestamp = $"<color=#888888>[{this.timestamp:HH:mm}]</color> ";

    return $"{timestamp}{prefix}{coloredName}{content}";
}
```

### Channel Prefixes
| Channel | Prefix |
|---------|--------|
| System | `<color=#FFD700>[SYS]</color>` |
| Proximity | `<color=#00FF00>[PROX]</color>` |
| World | `<color=#00BFFF>[WORLD]</color>` |
| Port | `<color=#FFA500>[PORT]</color>` |
| Party | `<color=#FF69B4>[PARTY]</color>` |
| Nation | `<color=#FF4500>[NATION]</color>` |
| Guild | `<color=#9370DB>[GUILD]</color>` |

---

## Usage Example

```csharp
// Create message
ChatMessage msg = new ChatMessage(
    "CaptainJoe",
    "Ahoy, mateys!",
    ChatChannel.World,
    MessagePriority.Normal
);

// Get formatted display string
string display = msg.FormatForDisplay();
// Result: [14:30] [WORLD] CaptainJoe: Ahoy, mateys!

// System message (no sender)
ChatMessage sysMsg = new ChatMessage(
    "",
    "Server restart in 5 minutes",
    ChatChannel.System,
    MessagePriority.Urgent
);
```

---

## Integration Points

### Used By
- `ChatManager` - Message creation and routing
- `ChatHistory` - Message storage
- `ChatPanel` (UI) - Message display
- All chat handlers (Port, Party, System)

---

## Design Notes

### Phased Implementation
- Phase 1: System, Proximity, World (text)
- Phase 2: Port, Party (text)
- Phase 3: Voice integration
- Phase 4: Nation (text + voice)
- Phase 5: Guild (text + voice)

### Color Scheme
- Each channel has distinct, readable color
- Timestamp uses muted gray (#888888)
- Maintains readability on dark backgrounds
