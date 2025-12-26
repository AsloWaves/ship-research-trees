# MentionSystem.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/MentionSystem.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~158 |
| **Phase** | Phase 3: @Mention system |
| **Architecture** | Client-side mention detection and highlighting |

## Purpose
Handles @mention detection and highlighting in chat messages. Plays sound notifications when the local player is mentioned and highlights mentions with distinct colors.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `enableMentions` | true | Enable @mention system |
| `mentionHighlightColor` | Gold (1, 0.8, 0.2) | Color for local player mentions |
| `mentionSound` | (AudioClip) | Sound to play when mentioned |
| `audioSource` | (AudioSource) | For playing sound |

---

## Public API

### Detection
```csharp
// Check if message contains @LocalPlayerName
public bool ContainsMention(string messageContent)

// Extract all @mentions from message
public string[] ExtractMentions(string messageContent)
```

### Formatting
```csharp
// Highlight all @mentions in message
public string HighlightMentions(string messageContent)
```

### Notification
```csharp
// Handle mention notification
public void OnMentioned(ChatMessage message)

// Set local player name
public void SetLocalPlayerName(string playerName)
```

---

## Mention Detection

Uses regex to detect @PlayerName patterns:

```csharp
public bool ContainsMention(string messageContent)
{
    // Match @PlayerName with word boundary
    string pattern = $@"@{Regex.Escape(localPlayerName)}\b";
    return Regex.IsMatch(messageContent, pattern, RegexOptions.IgnoreCase);
}
```

---

## Mention Highlighting

```csharp
public string HighlightMentions(string messageContent)
{
    string pattern = @"@(\w+)";
    string hexColor = ColorUtility.ToHtmlStringRGB(mentionHighlightColor);

    return Regex.Replace(messageContent, pattern, match =>
    {
        string username = match.Groups[1].Value;

        // Local player = gold highlight
        if (username.Equals(localPlayerName, StringComparison.OrdinalIgnoreCase))
            return $"<color=#{hexColor}>@{username}</color>";

        // Others = gray highlight
        return $"<color=#AAAAAA>@{username}</color>";
    });
}
```

---

## Notification Flow

```csharp
public void OnMentioned(ChatMessage message)
{
    // 1. Play sound
    PlayMentionSound();

    // 2. Add system notification
    ChatMessage notification = new ChatMessage(
        "",
        $"💬 You were mentioned by {message.sender} in {message.channel}",
        ChatChannel.System,
        MessagePriority.Mention
    );
    chatHistory.AddMessage(notification);

    // 3. TODO: Flash tab if not viewing channel
}
```

---

## Usage Example

```csharp
// Set player name on login
mentionSystem.SetLocalPlayerName("CaptainJoe");

// Check incoming message for mention
if (mentionSystem.ContainsMention(message.content))
{
    mentionSystem.OnMentioned(message);
}

// Format message for display with highlights
string formatted = mentionSystem.HighlightMentions(message.content);
// "Hey @CaptainJoe!" → "Hey <color=#FFD700>@CaptainJoe</color>!"

// Extract all mentions
string[] mentions = mentionSystem.ExtractMentions("Hey @Player1 and @Player2");
// ["Player1", "Player2"]
```

---

## Integration Points

### Dependencies
- `ChatHistory` - Add notification messages
- `AudioSource` - Play notification sound
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `ChatPanel` (UI) - Call on incoming messages

### TODOs
- Get actual player name from controller/network
- Implement tab flashing in ChatPanel

---

## Design Notes

### Pattern: @username
- Case-insensitive matching
- Word boundary prevents false positives
- `@CaptainJoe` matches, `@CaptainJoeBob` doesn't

### Color Scheme
- Local player mentions: Gold (#FFD700) - high visibility
- Other mentions: Gray (#AAAAAA) - visible but not distracting

### Notification
- Sound + system message
- MessagePriority.Mention triggers special UI handling
