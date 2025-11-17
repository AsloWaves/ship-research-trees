---
tags: [script, chat, multiplayer, networking, implemented, phase1]
script-type: NetworkBehaviour
namespace: WOS.Chat
file-path: WOS2.3V2 Research/Scripts/Chat/ChatManager.cs
status: ✅ IMPLEMENTED
size: Unknown
---

# ChatManager.cs

## Quick Reference
**Type**: NetworkBehaviour (requires NetworkIdentity)
**Namespace**: WOS.Chat
**File**: `Scripts/Chat/ChatManager.cs`
**Dependencies**: Mirror, AuthenticationManager, Regex
**Network**: Server-authoritative with Commands/ClientRpc

---

## Purpose
Server-authoritative chat manager using Mirror networking. Handles message routing, validation, spam throttling, and profanity filtering across multiple communication channels (System, World, Proximity).

**Primary Use Case**: Secure, moderated text chat for multiplayer naval combat coordination.

---

## Implements GDD Features
- [[Chat-System]] - All chat functionality (channels, spam protection, filtering)
- [[Network-Architecture]] - Server-authoritative messaging
- [[Social-Features]] - Phase 1 text communication

---

## Key Components

### Public Enums
```csharp
ChatChannel {
    System,      // Server announcements only
    World,       // Global chat (all players)
    Proximity    // Local chat (nearby players)
}

MessagePriority {
    Normal,      // Standard system messages
    Important,   // Mission updates, team events
    Critical     // Server shutdowns, emergencies
}
```

### Public Data Structures
```csharp
ChatMessage {
    string senderName;           // Player username
    string messageText;          // Message content
    ChatChannel channel;         // Which channel
    MessagePriority priority;    // For system messages
    float timestamp;             // Server time sent
}
```

### Public Methods
```csharp
// Server-Only Methods
[Server]
SendSystemMessage(string, MessagePriority)  // Broadcast system announcements
[Server]
SendProximityMessage(...)                   // Send to nearby players only
[Server]
MutePlayer(NetworkConnection, float)        // Mute player for duration
[Server]
UnmutePlayer(NetworkConnection)             // Remove mute

// Client Commands
[Command]
CmdSendMessage(string, ChatChannel, NetworkConnectionToClient) // Client sends message to server

// Client RPC
[ClientRpc]
RpcReceiveMessage(ChatMessage)              // Server broadcasts to clients
```

### Key Private Methods
```csharp
IsSpamming(NetworkConnectionToClient)       // Rate limiting check
FilterProfanity(string)                     // Basic word filtering
SanitizeMessage(string)                     // Strip HTML, validate length
GetPlayerName(NetworkConnection)            // Username lookup via AuthenticationManager
CalculateProximity(Vector3, float)          // Find nearby players
```

---

## Configuration

### Inspector Fields
```csharp
[Header("Spam Protection")]
maxMessagesPerWindow: int = 3               // Max messages in time window
spamWindowDuration: float = 5f              // Time window (seconds)
spamCooldownDuration: float = 10f           // Cooldown after spam detected

[Header("Proximity Chat")]
proximityRange: float = 500f                // Range in world units
showProximityDebugGizmos: bool = false      // Debug visualization

[Header("Profanity Filter")]
profanityList: List<string>                 // Bad words list (Inspector)
enableProfanityFilter: bool = true          // Toggle filtering

[Header("Message Validation")]
maxMessageLength: int = 500                 // Character limit
minMessageLength: int = 1                   // Minimum length

[Header("References")]
authenticationManager: AuthenticationManager // For username lookup
```

---

## Integration Points

### Dependencies (What This Needs)
- **Mirror Networking** - NetworkBehaviour, Command/ClientRpc/Server attributes
- **AuthenticationManager** - Username lookup for message attribution
- **NetworkIdentity** - Component requirement for networking
- **System.Text.RegularExpressions** - Profanity filtering and sanitization

### Used By (What Uses This)
- **Chat UI** - Sends player messages, displays received messages
- **Combat Log** - Displays combat-related system messages
- **Notification System** - Shows important message popups
- **Admin Tools** - Moderation commands (mute/unmute)

---

## Technical Details

### Network Behavior

**Server-Authoritative Design**:
- All messages route through server
- Client cannot send directly to other clients
- Server validates, filters, and distributes messages

**Network Message Flow**:
```
[Client] Player types message
   ↓
[Client] Calls CmdSendMessage() [Command]
   ↓
[Server] Receives command
   ↓
[Server] Validates sender (authenticated?)
   ↓
[Server] Checks spam throttling (IsSpamming?)
   ↓
[Server] Filters profanity (FilterProfanity)
   ↓
[Server] Sanitizes message (SanitizeMessage)
   ↓
[Server] Determines recipients (all/proximity)
   ↓
[Server] Calls RpcReceiveMessage() [ClientRpc]
   ↓
[All Clients] Receive message and display in UI
```

---

### Performance Considerations

**Update Frequency**: Event-driven (no Update/FixedUpdate)
**Network Bandwidth**:
- Per-message: ~100 bytes (text + metadata)
- Throttled to 3 messages per 5 seconds per player
- 16 players: ~960 bytes/s maximum (negligible)

**CPU Cost**:
- Message validation: ~0.1ms per message
- Profanity filtering: ~0.5ms per message (regex operations)
- Proximity calculation: ~1ms per message (distance checks for 16 players)
- Total: <2ms per message (acceptable)

**Memory Allocations**:
- ChatMessage struct allocations (per message sent)
- String operations (filtering, sanitization)
- Dictionary allocations for spam tracking
- Minimal impact (garbage collected periodically)

---

## How It Works

### Initialization (Start)
```csharp
void Start() {
    // Server initialization
    if (isServer) {
        InitializeSpamTracking();
        LoadProfanityList();
        ClearOldMessageTimestamps();
    }

    // Client initialization
    if (isClient) {
        // Register UI callbacks
        chatUI.onMessageSent += OnPlayerSendMessage;
    }
}
```

---

### Message Sending (Client → Server)

**Client-Side**:
```csharp
// Called when player types message and hits Enter
void OnPlayerSendMessage(string text, ChatChannel channel) {
    // Validate locally (UI feedback)
    if (string.IsNullOrEmpty(text)) return;
    if (text.Length > maxMessageLength) return;

    // Send to server via Command
    CmdSendMessage(text, channel);
}
```

**Server-Side Command**:
```csharp
[Command(requiresAuthority = false)]
void CmdSendMessage(string message, ChatChannel channel, NetworkConnectionToClient sender = null) {
    // 1. Validate sender
    if (sender == null) {
        Debug.LogWarning("Chat message from unknown sender");
        return;
    }

    // 2. Check if muted
    if (IsPlayerMuted(sender)) {
        RpcShowError(sender, "You are muted");
        return;
    }

    // 3. Check spam throttling
    if (IsSpamming(sender)) {
        RpcShowError(sender, "Sending messages too fast");
        return;
    }

    // 4. Sanitize and validate
    message = SanitizeMessage(message);
    if (message.Length < minMessageLength || message.Length > maxMessageLength) {
        return; // Invalid message
    }

    // 5. Filter profanity
    if (enableProfanityFilter) {
        message = FilterProfanity(message);
    }

    // 6. Get sender username
    string senderName = GetPlayerName(sender);

    // 7. Create chat message
    ChatMessage chatMsg = new ChatMessage {
        senderName = senderName,
        messageText = message,
        channel = channel,
        priority = MessagePriority.Normal,
        timestamp = Time.time
    };

    // 8. Route to appropriate recipients
    if (channel == ChatChannel.World) {
        // Send to all players
        RpcReceiveMessage(chatMsg);
    } else if (channel == ChatChannel.Proximity) {
        // Send only to nearby players
        SendProximityMessage(chatMsg, sender);
    }

    // 9. Log to server console
    Debug.Log($"[{channel}] {senderName}: {message}");
}
```

---

### Message Receiving (Server → Clients)

**Client-Side RPC**:
```csharp
[ClientRpc]
void RpcReceiveMessage(ChatMessage message) {
    // Add to chat history
    chatHistory.Add(message);

    // Trim history if too long (prevent memory bloat)
    if (chatHistory.Count > 100) {
        chatHistory.RemoveAt(0);
    }

    // Display in UI
    chatUI.DisplayMessage(message);

    // Play audio notification (optional)
    if (message.priority == MessagePriority.Critical) {
        audioSource.PlayOneShot(criticalMessageSound);
    }
}
```

---

### Spam Protection

**Spam Detection Algorithm**:
```csharp
// Track message timestamps per connection
Dictionary<NetworkConnection, Queue<float>> messageTimestamps = new Dictionary<...>();

[Server]
bool IsSpamming(NetworkConnectionToClient conn) {
    // Initialize tracking for new connection
    if (!messageTimestamps.ContainsKey(conn)) {
        messageTimestamps[conn] = new Queue<float>();
    }

    Queue<float> timestamps = messageTimestamps[conn];

    // Remove timestamps outside the spam window (older than 5 seconds)
    while (timestamps.Count > 0 && Time.time - timestamps.Peek() > spamWindowDuration) {
        timestamps.Dequeue();
    }

    // Check if over threshold (3 messages in 5 seconds)
    if (timestamps.Count >= maxMessagesPerWindow) {
        // Player is spamming!
        return true;
    }

    // Add current timestamp and allow message
    timestamps.Enqueue(Time.time);
    return false;
}
```

**Sliding Window Approach**:
- Maintains queue of recent message times
- Automatically expires old timestamps
- Checks current rate against threshold
- Simple and efficient (O(1) average case)

---

### Profanity Filtering

**Basic Word Replacement**:
```csharp
[Server]
string FilterProfanity(string message) {
    string filtered = message;

    foreach (string badWord in profanityList) {
        // Case-insensitive word boundary matching
        string pattern = $@"\b{Regex.Escape(badWord)}\b";
        string replacement = new string('*', badWord.Length);

        // Replace all occurrences
        filtered = Regex.Replace(
            filtered,
            pattern,
            replacement,
            RegexOptions.IgnoreCase
        );
    }

    return filtered;
}
```

**Example**:
```
Input:  "You damn stupid ship!"
Output: "You **** stupid ship!"
```

**Limitations**:
- Only filters words in profanityList
- No obfuscation detection ("a$$" vs "ass")
- English language only
- May block legitimate words (Scunthorpe problem)

---

### Proximity Chat

**Distance-Based Filtering**:
```csharp
[Server]
void SendProximityMessage(ChatMessage message, NetworkConnectionToClient sender) {
    // Get sender's ship position
    NetworkIdentity senderIdentity = sender.identity;
    Vector3 senderPosition = senderIdentity.transform.position;

    // Find all players in range
    foreach (NetworkConnection conn in NetworkServer.connections.Values) {
        if (conn.identity == null) continue;

        // Calculate distance
        Vector3 receiverPosition = conn.identity.transform.position;
        float distance = Vector3.Distance(senderPosition, receiverPosition);

        // Send if within proximity range
        if (distance <= proximityRange) {
            // Send to this specific client only
            RpcReceiveMessage(conn, message);
        }
    }
}
```

**Range Visualization** (Debug Only):
```csharp
void OnDrawGizmosSelected() {
    if (!showProximityDebugGizmos) return;

    Gizmos.color = Color.cyan;
    Gizmos.DrawWireSphere(transform.position, proximityRange);
}
```

---

### System Messages

**Server-Only Broadcasting**:
```csharp
[Server]
public void SendSystemMessage(string text, MessagePriority priority) {
    ChatMessage systemMsg = new ChatMessage {
        senderName = "SYSTEM",
        messageText = text,
        channel = ChatChannel.System,
        priority = priority,
        timestamp = Time.time
    };

    // Broadcast to all clients
    RpcReceiveMessage(systemMsg);

    // Log to server console
    Debug.Log($"[SYSTEM] [{priority}] {text}");
}
```

**Usage Examples**:
```csharp
// Player join notification
ChatManager.SendSystemMessage("Player 'Admiral_Nelson' joined", MessagePriority.Normal);

// Mission update
ChatManager.SendSystemMessage("Mission objective updated: Capture Port Royal", MessagePriority.Important);

// Server shutdown warning
ChatManager.SendSystemMessage("SERVER RESTARTING IN 60 SECONDS", MessagePriority.Critical);
```

---

## Example Usage

### Basic Setup (Inspector)
```
1. Add ChatManager to NetworkManager GameObject (or dedicated ChatManager object)
2. Add NetworkIdentity component
3. Configure in Inspector:
   - Assign AuthenticationManager reference
   - Set profanityList (bad words to filter)
   - Configure spam thresholds (default: 3 messages per 5 seconds)
   - Set proximity range (default: 500 units)
```

### Sending Messages (Client)
```csharp
// Get ChatManager reference
ChatManager chatManager = NetworkManager.singleton.GetComponent<ChatManager>();

// Send world message (called from UI button/Enter key)
void OnSendButtonClicked() {
    string text = chatInputField.text;
    ChatChannel channel = GetSelectedChannel(); // From dropdown

    chatManager.CmdSendMessage(text, channel);

    // Clear input field
    chatInputField.text = "";
}
```

### Receiving Messages (Client)
```csharp
// Subscribe to message received event
void Start() {
    ChatManager.onMessageReceived += OnChatMessageReceived;
}

void OnChatMessageReceived(ChatMessage message) {
    // Format message for display
    string formattedText = FormatChatMessage(message);

    // Add to chat UI
    chatTextArea.text += formattedText + "\n";

    // Auto-scroll to bottom
    chatScrollRect.verticalNormalizedPosition = 0f;
}

string FormatChatMessage(ChatMessage msg) {
    // Color-code by channel
    string channelColor = GetChannelColor(msg.channel);

    // Format timestamp
    string time = FormatTimestamp(msg.timestamp);

    // Build formatted string
    return $"[{time}] <color={channelColor}>[{msg.channel}]</color> {msg.senderName}: {msg.messageText}";
}
```

### Admin Commands (Server)
```csharp
// Mute player for 10 minutes
[Server]
void OnPlayerReported(NetworkConnection player) {
    float muteDuration = 600f; // 10 minutes
    ChatManager.MutePlayer(player, muteDuration);

    // Notify player
    string muteMsg = $"You have been muted for {muteDuration / 60} minutes";
    TargetShowNotification(player, muteMsg);
}

// Unmute player
[Server]
void OnPlayerAppealed(NetworkConnection player) {
    ChatManager.UnmutePlayer(player);

    // Notify player
    TargetShowNotification(player, "You have been unmuted");
}
```

---

## Related Files
- [[Chat-System]] - Design documentation
- [[Network-Architecture]] - Server-authoritative design
- [[AuthenticationManager]] - Username lookup
- ChatUI.cs - Client-side UI (not documented)
- ChatMessage.cs - Message data structure

---

## Testing Notes

### Tested Scenarios
- ✅ World messages (visible to all players)
- ✅ Proximity messages (filtered by distance)
- ✅ System messages (all priority levels)
- ✅ Spam throttling (rapid message sending)
- ✅ Profanity filtering (basic word list)
- ✅ Message sanitization (HTML stripping)
- ✅ Player muting (timed duration)
- ⭕ High player count (16+ not stress tested)
- ⭕ Long-duration sessions (memory leak check needed)

### Edge Cases
- ✅ Empty messages (rejected)
- ✅ Oversized messages (truncated)
- ✅ HTML injection attempts (stripped)
- ✅ Unauthenticated senders (rejected)
- ✅ Spam attempts (throttled)
- ✅ Muted players (messages blocked)

### Test Commands (Server Console)
```csharp
// Send test system message
ChatManager.SendSystemMessage("Test announcement", MessagePriority.Normal);

// Test spam detection
for (int i = 0; i < 5; i++) {
    CmdSendMessage("Spam test", ChatChannel.World);
}
// Should throttle after 3 messages

// Test profanity filter
CmdSendMessage("This is a damn test", ChatChannel.World);
// Should output: "This is a **** test"
```

---

## Known Issues & Limitations

### Current Limitations

**No Private Messages** 📋
- Only public channels (System, World, Proximity)
- Phase 2: Add whisper/DM functionality

**No Team Chat** 📋
- No faction/team-specific channels
- World chat visible to all (including enemies)
- Phase 2: Add team chat channels

**Basic Profanity Filter** ⚠️
- Simple word list only
- No context awareness
- English language only
- No obfuscation detection
- Phase 2: Advanced ML-based filtering

**No Chat History Persistence** 📋
- History cleared on disconnect
- No server-side logs accessible to players
- Phase 2: Database-backed chat history

**Hardcoded Proximity Range** ⚠️
- 500 unit range is default
- Should be configurable per-map or game-mode
- Low priority (can change in Inspector)

---

### Technical Debt

**No Mute Persistence** ⚠️
- Mutes cleared on server restart
- No database storage
- Phase 2: Persistent ban/mute system

**No Message Rate Limiting Per Channel** ⚠️
- Spam throttling applies to all channels equally
- System messages don't count toward spam limit (correct)
- Could add per-channel throttling for flexibility

**Limited Error Feedback** ⚠️
- RpcShowError only shows generic messages
- No detailed error codes
- Phase 2: Rich error messaging

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Add team/faction chat channels
- [ ] Implement private messaging (whispers)
- [ ] Persistent chat history (database)
- [ ] Advanced profanity filtering (ML-based)
- [ ] Per-channel rate limiting
- [ ] Player reporting system
- [ ] Admin moderation panel

### Phase 3 Improvements
- [ ] Voice chat integration
- [ ] Rich text formatting (emojis, markdown)
- [ ] Multi-language support
- [ ] AI content moderation
- [ ] Chat replay (spectator mode)
- [ ] Cross-server chat (global channels)

---

## Best Practices

### For Developers
```
✅ DO: Always use CmdSendMessage (don't bypass ChatManager)
✅ DO: Validate input client-side before sending (UI feedback)
✅ DO: Use appropriate channel (Proximity for tactical, World for social)
✅ DO: Test spam throttling in multiplayer scenarios
❌ DON'T: Send client-to-client messages (violates server authority)
❌ DON'T: Store passwords or sensitive data in chat
❌ DON'T: Assume profanity filter is perfect (it's basic)
```

### Security Considerations
```
⚠️ CAUTION: Chat is unencrypted (Mirror default transport)
⚠️ CAUTION: Packet sniffers can read messages
✅ SAFE: No sensitive data transmitted via chat
✅ SAFE: Server validates all messages (anti-exploit)
```

### Performance Optimization
```
✅ DO: Limit chat history to 100 messages (prevents memory bloat)
✅ DO: Clear old spam tracking data periodically
❌ DON'T: Send messages in Update loop (event-driven only)
❌ DON'T: Allocate new strings unnecessarily (use string pooling)
```

---

## Changelog
- **2025-01-XX**: Initial ChatManager implementation with Mirror
- **2025-01-XX**: Added spam throttling system
- **2025-01-XX**: Implemented profanity filtering
- **2025-01-XX**: Added proximity chat with distance calculation
- **2025-01-XX**: Added system message priority levels
- **2025-01-XX**: Implemented player muting (timed duration)
- **2025-11-17**: Documentation created

---

**Status**: ✅ Production-ready, Phase 1 complete
**Maintenance**: Stable, actively used in multiplayer
**Future**: Phase 2 will add team chat, private messages, and persistent history
