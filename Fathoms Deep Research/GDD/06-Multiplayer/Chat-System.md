---
tags: [implemented, phase1, multiplayer, chat, social]
status: ✅ IMPLEMENTED
phase: Phase 1
priority: HIGH
last-updated: 2025-11-17
---

# Chat System

## Overview
Server-authoritative text chat system using Mirror networking with support for multiple communication channels (System, World, Proximity), spam protection, profanity filtering, and message validation. Provides essential communication for coordinated naval warfare in multiplayer environments.

## Implementation Status
**Status**: ✅ **IMPLEMENTED** (Phase 1 complete)
**Phase**: Phase 1 Complete
**Scripts**: [[ChatManager]]
**Priority**: HIGH - Essential for multiplayer coordination

---

## Design Specification

### Core Philosophy

**Server-Authoritative Design**:
All chat messages are routed through the server for validation and distribution. This architecture provides:
- **Anti-Spam**: Server controls message rate limiting
- **Moderation**: Profanity filtering applied server-side
- **Security**: Prevents client-side chat exploits
- **Authority**: Server can mute players, moderate content
- **Logging**: All messages logged server-side for moderation review

**Why Not Peer-to-Peer?**:
- P2P chat is vulnerable to spam and exploits
- No centralized moderation capability
- Harder to implement muting/blocking
- Inconsistent message delivery

---

### Chat Channels

#### System Channel ✅
**Purpose**: Official game announcements and notifications
**Color**: Yellow/Gold (high visibility)
**Authority**: Server-only (players cannot send system messages)
**Priority Levels**: Normal, Important, Critical

**Use Cases**:
- Player join/leave notifications
- Server announcements ("Server restarting in 5 minutes")
- Achievement unlocks
- Mission updates
- Faction events
- Combat notifications ("Red team destroyed enemy flagship!")

**Example Messages**:
```
[SYSTEM] Player "Admiral_Nelson" has joined the battle
[SYSTEM] Mission objective updated: Capture Port Royal
[SYSTEM] Server maintenance in 10 minutes
```

---

#### World Channel ✅
**Purpose**: Global text chat visible to all players on the server
**Color**: White/Light Gray
**Range**: Unlimited (entire server)
**Use Cases**:
- Team coordination across long distances
- Diplomatic negotiations
- Trade requests
- Social interaction
- Looking for group (LFG) messages

**Example Messages**:
```
[World] Captain_Sparrow: Anyone want to raid the Spanish port?
[World] BlackBeard88: Looking for crew members for merchant convoy
[World] Admiral_Zhao: Trading cannonballs for repair supplies
```

---

#### Proximity Channel ✅
**Purpose**: Local chat for nearby ships only (tactical communication)
**Color**: Blue/Cyan
**Range**: Configurable radius (default: 500 units)
**Use Cases**:
- Tactical coordination in fleet battles
- Quick communication with nearby allies
- Stealth operations (doesn't reveal position globally)
- Immersive roleplay (shouting distance)

**Technical Implementation**:
- Server calculates distance between sender and all players
- Only delivers message to players within proximity range
- Position checked at message send time (not updated)

**Example Messages**:
```
[Proximity] SquadLeader: Enemy frigate at 2 o'clock!
[Proximity] Wingman: I'll flank from the left
[Proximity] Support: Need repairs ASAP
```

---

### Message Priority System

**System messages have priority levels for importance**:

**Normal Priority**:
- Standard notifications (player joins/leaves)
- General announcements
- Non-urgent updates

**Important Priority**:
- Mission objectives
- Team-wide announcements
- Resource notifications

**Critical Priority**:
- Server shutdowns
- Emergency messages
- Critical game events
- Security alerts

**Visual Indicators**:
- Normal: Standard system color
- Important: Bold text or icon
- Critical: Flashing/pulsing effect, sound alert

---

## Technical Implementation

### Server-Authoritative Flow

```
Client Input:
1. Player types message in chat UI
2. Player selects channel (World/Proximity)
3. Client calls [Command] CmdSendMessage(text, channel)
4. Message sent to server

Server Processing:
5. Server receives command
6. Server validates sender (is player authenticated?)
7. Server checks spam throttling (is player sending too fast?)
8. Server filters profanity (replace bad words with asterisks)
9. Server validates message length (prevent oversized messages)
10. Server determines recipients based on channel type
11. Server calls [ClientRpc] RpcReceiveMessage() to recipients

Client Display:
12. Clients receive RpcReceiveMessage()
13. Chat UI displays message with appropriate color/formatting
14. Message added to chat history
15. Audio notification plays (optional)
```

---

### Spam Protection

**Rate Limiting**:
- **Threshold**: 3 messages per 5 seconds
- **Cooldown**: 10 seconds if threshold exceeded
- **Server-Side**: Can't be bypassed by client modification
- **Feedback**: Client shows "Sending too fast" error

**Implementation**:
```csharp
Dictionary<NetworkConnection, Queue<float>> messageTimestamps;

bool IsSpamming(NetworkConnection conn) {
    if (!messageTimestamps.ContainsKey(conn)) {
        messageTimestamps[conn] = new Queue<float>();
    }

    var timestamps = messageTimestamps[conn];

    // Remove timestamps older than 5 seconds
    while (timestamps.Count > 0 && Time.time - timestamps.Peek() > 5f) {
        timestamps.Dequeue();
    }

    // Check if over threshold
    if (timestamps.Count >= 3) {
        return true; // Spamming!
    }

    // Add current timestamp
    timestamps.Enqueue(Time.time);
    return false;
}
```

**Anti-Spam Features**:
- Per-connection message rate tracking
- Sliding window (5 second intervals)
- Automatic cooldown (no manual reset)
- Server logs repeated spam attempts

---

### Profanity Filtering

**Basic Word Filtering**:
- Server maintains list of prohibited words
- Case-insensitive matching
- Replaces bad words with asterisks
- Preserves message length (maintains context)

**Filter Implementation**:
```csharp
string FilterProfanity(string message) {
    string filtered = message;

    foreach (string badWord in profanityList) {
        // Case-insensitive replacement
        string pattern = $@"\b{Regex.Escape(badWord)}\b";
        string replacement = new string('*', badWord.Length);
        filtered = Regex.Replace(filtered, pattern, replacement, RegexOptions.IgnoreCase);
    }

    return filtered;
}
```

**Example**:
```
Input:  "You stupid enemy ship!"
Output: "You ****** enemy ship!"
```

**Limitations** (Phase 1):
- Basic word list only (no advanced NLP)
- No context awareness (may block legitimate words)
- English language only
- No obfuscation detection ("a$$" vs "ass")

**Phase 2 Improvements**:
- Context-aware filtering
- Multi-language support
- Obfuscation detection
- User-reported content moderation

---

### Message Validation

**Security Checks**:
- **Max Length**: 500 characters (prevent oversized packets)
- **Min Length**: 1 character (no empty messages)
- **HTML/Script Injection**: Strip dangerous characters
- **Authentication**: Sender must be authenticated player
- **Channel Validation**: Ensure valid channel type

**Sanitization**:
```csharp
string SanitizeMessage(string input) {
    // Remove leading/trailing whitespace
    input = input.Trim();

    // Limit length
    if (input.Length > 500) {
        input = input.Substring(0, 500);
    }

    // Strip HTML tags
    input = Regex.Replace(input, "<.*?>", string.Empty);

    // Escape special characters
    input = input.Replace("<", "&lt;").Replace(">", "&gt;");

    return input;
}
```

---

## Integration Points

### Dependencies
- **Mirror Networking**: NetworkBehaviour, Command/ClientRpc
- **AuthenticationManager**: Username lookup for message attribution
- **NetworkIdentity**: Sender identification
- **Regex**: Profanity filtering and sanitization

### Used By
- **Chat UI**: Displays messages, sends player input
- **Notification System**: Shows message popups
- **Combat Log**: Records combat-related messages
- **Admin Tools**: Moderation and player management

### API for Other Systems
```csharp
// Send system message (server-only)
ChatManager.SendSystemMessage("Server restarting in 5 minutes", MessagePriority.Critical);

// Get chat history (for UI)
List<ChatMessage> history = ChatManager.GetChatHistory(50); // Last 50 messages

// Mute/unmute player (admin command)
ChatManager.MutePlayer(playerConnection, duration: 600); // 10 minute mute
ChatManager.UnmutePlayer(playerConnection);

// Check if player is muted
bool isMuted = ChatManager.IsPlayerMuted(playerConnection);
```

---

## User Experience

### Chat UI Design

**Input Field**:
- Text input box at bottom of screen
- Channel selector dropdown (World/Proximity)
- Enter key sends message
- Escape key closes chat
- Auto-focus when typing starts

**Message Display**:
- Scrollable message history (last 100 messages)
- Color-coded by channel
- Timestamp (optional, can toggle)
- Player names bolded or highlighted
- Auto-scroll to latest message

**Visual Formatting**:
```
[12:34] [SYSTEM] Server maintenance in 10 minutes
[12:35] [World] Admiral_Nelson: Anyone near Port Royal?
[12:35] [Proximity] CaptainKidd: I'm here, need help?
[12:36] [World] Admiral_Nelson: Yes! Join voice channel 1
```

**Accessibility**:
- Adjustable text size
- High-contrast mode
- Color-blind friendly channel colors
- Transparency slider (for HUD overlay)

---

### Immersion & Realism

**Historical Radio Communication Feel**:
- Proximity chat simulates voice range
- System messages feel like radio broadcasts
- World chat is "telegraph network" (unrealistic but necessary)

**Optional Enhancements (Phase 3)**:
- Radio static sound effects
- Transmission delay based on distance
- "Radio chatter" audio overlay
- Morse code visual effects for system messages

---

## Performance Considerations

**Network Bandwidth**:
- Average message: ~100 bytes (text + metadata)
- Spam throttling: Max 3 messages/5s = 0.6 messages/s
- Per-player bandwidth: ~60 bytes/s average
- 16 players: ~960 bytes/s total (negligible)

**Server CPU**:
- Message validation: ~0.1ms per message
- Profanity filtering: ~0.5ms per message (regex)
- Proximity calculation: ~1ms per message (16 players)
- Total: <2ms per message (acceptable)

**Client Performance**:
- Message display: UI update only (negligible)
- Chat history: Limited to 100 messages (prevents memory bloat)
- No impact on gameplay frame rate

---

## Security & Moderation

### Anti-Exploit Protections

**Server-Side Validation**:
- All validation happens on server (can't be bypassed)
- Client-side input is untrusted
- Message sanitization prevents injection attacks

**Rate Limiting**:
- Prevents chat flooding
- Stops DoS attacks via message spam
- Per-connection tracking (isolates bad actors)

**Authentication Integration**:
- Messages attributed to authenticated accounts
- Anonymous players can't send messages
- Banned accounts auto-muted

---

### Moderation Tools

**Server-Side Features (Implemented)**:
- Profanity filtering (automatic)
- Spam throttling (automatic)
- Message logging (server console)

**Admin Tools (Phase 2)**:
- Manual player muting (duration-based)
- Chat history review panel
- Player report system
- Auto-mute on repeated reports

**Phase 3 Enhancements**:
- AI-powered content moderation
- Sentiment analysis (detect toxic behavior)
- Automated warning system
- Appeal/dispute resolution

---

## Known Issues & Limitations

### Current Limitations

**No Voice Chat** 📋
- Text-only in Phase 1
- Voice requires separate solution (Vivox, Agora, etc.)
- Phase 3: Integrate voice chat system

**No Private Messages** 📋
- Only public channels (System, World, Proximity)
- No whisper/DM functionality
- Phase 2: Add team-only and private message channels

**No Team Chat** 📋
- World chat is visible to all players (including enemies)
- No faction-specific chat
- Phase 2: Add team/faction chat channels

**Basic Profanity Filter** ⚠️
- Simple word list only
- English language only
- No obfuscation detection
- Phase 2: Advanced filtering

**No Chat History Persistence** 📋
- Chat history cleared on disconnect
- No server-side chat logs accessible to players
- Phase 2: Add persistent chat history (database storage)

---

### Technical Debt

**Hardcoded Message Limit** ⚠️
- 500 character limit is hardcoded
- Should be configurable
- Low priority (500 is reasonable)

**Proximity Range Hardcoded** ⚠️
- 500 unit range is hardcoded
- Should be configurable per-scene or per-game-mode
- Medium priority (affects tactical gameplay)

**No Emoji/Rich Text Support** 📋
- Plain text only
- No emojis, markdown, or formatting
- Phase 2: Add rich text support (TextMeshPro tags)

---

## Testing

### Test Coverage
- ✅ Message sending (all channels)
- ✅ Server-authoritative routing
- ✅ Spam throttling (tested with rapid sends)
- ✅ Profanity filtering (basic word list)
- ✅ Proximity range calculation
- ✅ System message broadcasting
- ✅ Message validation (length, sanitization)
- ⭕ High player count stress test (16+ players)
- ⭕ Multi-language support (not tested)
- ⭕ Long-duration spam attacks (not tested)

### Test Scenarios
```
1. Normal Usage:
   - Send World message, visible to all
   - Send Proximity message, visible to nearby only
   - System messages display correctly

2. Spam Protection:
   - Send 3 messages rapidly → OK
   - Send 4th message → Throttled
   - Wait 5 seconds → Can send again

3. Profanity Filter:
   - Send message with profanity → Filtered
   - Send message with obfuscated profanity → Not filtered (known limitation)

4. Edge Cases:
   - Send empty message → Rejected
   - Send 501 character message → Truncated to 500
   - Send HTML tags → Stripped
```

### Known Bugs
- **None reported in Phase 1 scope**

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Add team/faction chat channels
- [ ] Implement private messaging (whispers)
- [ ] Persistent chat history (database storage)
- [ ] Advanced profanity filtering (ML-based)
- [ ] Chat history search functionality
- [ ] Player mute/block system
- [ ] Admin moderation panel

### Phase 3 Improvements
- [ ] Voice chat integration (Vivox/Agora)
- [ ] Rich text formatting (emojis, markdown)
- [ ] Multi-language support
- [ ] AI-powered content moderation
- [ ] Chat replay system (spectator mode)
- [ ] Cross-server chat (global channels)

---

## Cross-References

### Related GDD Sections
- [[Network-Architecture]] - Server-authoritative design
- [[Authentication]] - Username lookup for messages
- [[UI-Systems]] - Chat UI design
- [[Social-Features]] - Friend system, guilds (Phase 2)

### Related Scripts
- [[ChatManager]] - Core chat implementation
- [[AuthenticationManager]] - Username attribution
- ChatUI.cs - Client-side UI (not documented)
- ChatMessage.cs - Message data structure

### External Dependencies
- [Mirror Networking](https://mirror-networking.gitbook.io/)
- [TextMeshPro](https://docs.unity3d.com/Manual/com.unity.textmeshpro.html) - UI text rendering

---

## Developer Guidelines

### Adding New Chat Channels

To add a new channel type:

```csharp
// 1. Add to ChatChannel enum
public enum ChatChannel {
    System,
    World,
    Proximity,
    Team,      // NEW
    Faction    // NEW
}

// 2. Update CmdSendMessage validation
[Command]
void CmdSendMessage(string message, ChatChannel channel) {
    if (channel == ChatChannel.Team) {
        // Get sender's team
        int teamId = GetPlayerTeam(conn);
        // Send only to team members
        SendToTeam(message, teamId);
    }
}

// 3. Update UI channel selector
chatChannelDropdown.options.Add(new Dropdown.OptionData("Team"));
```

---

### Message Priority Guidelines

**When to use each priority**:

**Normal**:
- Player join/leave
- Non-urgent info
- Routine events

**Important**:
- Mission updates
- Team objectives
- Resource alerts

**Critical**:
- Server shutdowns
- Emergency warnings
- Security alerts
- Game-breaking events

**Example**:
```csharp
// Normal priority
ChatManager.SendSystemMessage("Player joined", MessagePriority.Normal);

// Important priority
ChatManager.SendSystemMessage("Mission objective updated!", MessagePriority.Important);

// Critical priority
ChatManager.SendSystemMessage("SERVER RESTARTING IN 60 SECONDS", MessagePriority.Critical);
```

---

## Best Practices

### For Players
```
✅ DO: Use Proximity for tactical coordination (doesn't alert enemies)
✅ DO: Use World for recruiting, trading, diplomacy
✅ DO: Keep messages concise and relevant
❌ DON'T: Spam messages (will be throttled)
❌ DON'T: Use profanity (will be filtered)
❌ DON'T: Share personal information (security risk)
```

### For Developers
```
✅ DO: Always route chat through ChatManager (don't bypass)
✅ DO: Use appropriate channel for message type
✅ DO: Test spam throttling with rapid sends
❌ DON'T: Send client-to-client chat (must go through server)
❌ DON'T: Store sensitive data in chat messages
❌ DON'T: Assume chat is secure (it's unencrypted)
```

---

## Changelog

- **2025-01-XX**: ChatManager implemented with Mirror
- **2025-01-XX**: Added spam throttling system
- **2025-01-XX**: Added profanity filtering
- **2025-01-XX**: Implemented proximity chat with range calculation
- **2025-01-XX**: Added system message priority levels
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Fully functional, Phase 1 complete
**Next Steps**: Phase 2 will add team chat, private messages, and persistent history
**Blockers**: None
