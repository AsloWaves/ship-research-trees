# ChatCommands.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/ChatCommands.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~218 |
| **Architecture** | Client-side chat command processor |

## Purpose
Extended chat command system handling /help, /clear, /roll, and future commands (/whisper, /party, /nation, /guild). Phase 1 implements basic commands; Phase 2+ adds extended commands.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `rollCooldown` | 3.0 | Seconds between /roll commands |

---

## Available Commands

### Phase 1 (Implemented)
| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/clear` | Clear current channel messages |
| `/roll` | Roll random number 1-100 |

### Phase 2+ (Placeholder)
| Command | Description |
|---------|-------------|
| `/w [player] [msg]` | Whisper to player |
| `/whisper` | Same as /w |
| `/p [msg]` | Party chat |
| `/party` | Same as /p |
| `/n [msg]` | Nation chat |
| `/nation` | Same as /n |
| `/g [msg]` | Guild chat |
| `/guild` | Same as /g |

---

## Command Processing

```csharp
public bool ProcessCommand(string input, ChatChannel currentChannel)
{
    if (!input.StartsWith("/"))
        return false;

    string[] parts = input.Split(' ', StringSplitOptions.RemoveEmptyEntries);
    string command = parts[0].ToLower();

    switch (command)
    {
        case "/help":
            ShowHelp();
            return true;

        case "/clear":
            ClearChannel(currentChannel);
            return true;

        case "/roll":
            RollDice();
            return true;

        // Placeholder commands
        case "/w":
        case "/whisper":
            ShowNotImplementedMessage("Whisper");
            return true;

        // ... other placeholders

        default:
            ShowUnknownCommand(command);
            return true;
    }
}
```

---

## /help Command

```csharp
private void ShowHelp()
{
    chatHistory.AddMessage(new ChatMessage("", "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", ChatChannel.System));
    chatHistory.AddMessage(new ChatMessage("", "📖 Available Chat Commands", ChatChannel.System, MessagePriority.Important));
    chatHistory.AddMessage(new ChatMessage("", "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", ChatChannel.System));

    // Phase 1 commands
    chatHistory.AddMessage(new ChatMessage("", "/help - Show this help message", ChatChannel.System));
    chatHistory.AddMessage(new ChatMessage("", "/clear - Clear current channel messages", ChatChannel.System));
    chatHistory.AddMessage(new ChatMessage("", "/roll - Roll a random number (1-100)", ChatChannel.System));

    // Coming soon
    chatHistory.AddMessage(new ChatMessage("", "", ChatChannel.System));
    chatHistory.AddMessage(new ChatMessage("", "🔒 Coming Soon:", ChatChannel.System));
    chatHistory.AddMessage(new ChatMessage("", "/w [player] [msg] - Whisper to player", ChatChannel.System));
    // ... etc

    chatHistory.AddMessage(new ChatMessage("", "💡 Tip: Use number keys 1-3 to switch tabs", ChatChannel.System));
}
```

---

## /roll Command with Rate Limiting

```csharp
private void RollDice()
{
    // Rate limiting
    float timeSinceLastRoll = Time.time - lastRollTime;
    if (timeSinceLastRoll < rollCooldown)
    {
        float remaining = rollCooldown - timeSinceLastRoll;
        chatHistory.AddMessage(new ChatMessage("",
            $"⏳ Please wait {remaining:F1} seconds before rolling again.",
            ChatChannel.System));
        return;
    }

    int roll = Random.Range(1, 101);

    if (NetworkClient.active)
    {
        // Send to World chat
        ChatCommandMessage msg = new ChatCommandMessage
        {
            content = $"🎲 rolled {roll} (1-100)",
            channel = ChatChannel.World
        };
        NetworkClient.Send(msg);
        lastRollTime = Time.time;
    }
}
```

---

## Error Handling

```csharp
private void ShowNotImplementedMessage(string featureName)
{
    chatHistory.AddMessage(new ChatMessage("",
        $"⚠️ {featureName} is not yet available. Coming in a future update!",
        ChatChannel.System,
        MessagePriority.Important));
}

private void ShowUnknownCommand(string command)
{
    chatHistory.AddMessage(new ChatMessage("",
        $"❌ Unknown command: {command}. Type /help for available commands.",
        ChatChannel.System,
        MessagePriority.Important));
}
```

---

## Usage Example

```csharp
// In ChatPanel input handling
if (inputText.StartsWith("/"))
{
    if (chatCommands.ProcessCommand(inputText, currentChannel))
    {
        // Command was handled, don't send as chat
        ClearInput();
        return;
    }
}

// Send as regular chat message
SendChatMessage(inputText, currentChannel);
```

---

## Integration Points

### Dependencies
- `ChatManager` - For future network commands
- `ChatHistory` - Local message display
- `NetworkClient` - Send /roll results
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Rate Limiting
- /roll has 3-second cooldown
- Prevents spam in World chat
- Remaining time shown to user

### Client-Side Processing
- Commands processed locally
- Only /roll sends network message
- Future commands may need server validation

### Phased Implementation
- Phase 1: Basic utility commands
- Phase 2+: Social features (whisper, party, guild)
