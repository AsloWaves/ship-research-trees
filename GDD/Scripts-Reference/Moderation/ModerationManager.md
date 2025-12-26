# ModerationManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Moderation/ModerationManager.cs` |
| **Namespace** | `WOS.Moderation` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~301 |
| **Phase** | Phase 5: Advanced moderation |
| **Architecture** | Server-side moderation system |

## Purpose
Server-side moderation system handling mutes, bans, player reports, and chat logging. Supports auto-mute based on violation thresholds. All moderation actions are server-authoritative.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `enableModeration` | true | Enable/disable moderation system |
| `chatLogRetentionHours` | 24 | Hours to retain chat logs |
| `autoMuteThreshold` | 3 | Violations before auto-mute |

---

## Server State

```csharp
// Muted players (connectionId -> unmute time)
private Dictionary<uint, DateTime> mutedPlayers;

// Banned accounts (accountId -> reason)
private Dictionary<string, string> bannedAccounts;

// Player violations (connectionId -> violation count)
private Dictionary<uint, int> playerViolations;

// Chat logs (for moderation review)
private List<ChatLogEntry> chatLogs;

// Player reports (reportId -> report data)
private Dictionary<string, PlayerReport> pendingReports;
```

---

## Data Structures

### ChatLogEntry
```csharp
[Serializable]
public struct ChatLogEntry
{
    public DateTime timestamp;
    public uint connectionId;
    public string playerName;
    public string message;
    public string channel;
}
```

### PlayerReport
```csharp
[Serializable]
public struct PlayerReport
{
    public string reportId;
    public uint reporterConnectionId;
    public uint targetConnectionId;
    public string category;         // "Spam", "Harassment", "Cheating"
    public string description;
    public DateTime timestamp;
}
```

---

## Mute System

### MutePlayer
```csharp
[Server]
public void MutePlayer(uint connectionId, int durationMinutes, string reason)
{
    DateTime unmuteTime = DateTime.Now.AddMinutes(durationMinutes);
    mutedPlayers[connectionId] = unmuteTime;

    // Notify player via TargetRpc
    TargetPlayerMuted(conn, durationMinutes, reason);
}
```

### UnmutePlayer
```csharp
[Server]
public void UnmutePlayer(uint connectionId)
{
    mutedPlayers.Remove(connectionId);
    TargetPlayerUnmuted(conn);
}
```

### IsPlayerMuted
```csharp
[Server]
public bool IsPlayerMuted(uint connectionId)
{
    if (!mutedPlayers.TryGetValue(connectionId, out DateTime unmuteTime))
        return false;

    // Auto-unmute if expired
    if (DateTime.Now >= unmuteTime)
    {
        UnmutePlayer(connectionId);
        return false;
    }

    return true;
}
```

---

## Ban System

### BanPlayer
```csharp
[Server]
public void BanPlayer(string accountId, string reason)
{
    bannedAccounts[accountId] = reason;
    // TODO: Disconnect player by accountId
}
```

### IsAccountBanned
```csharp
[Server]
public bool IsAccountBanned(string accountId)
{
    return bannedAccounts.ContainsKey(accountId);
}
```

---

## Violation System

```csharp
[Server]
public void RecordViolation(uint connectionId, string reason)
{
    if (!playerViolations.ContainsKey(connectionId))
        playerViolations[connectionId] = 0;

    playerViolations[connectionId]++;
    int violationCount = playerViolations[connectionId];

    // Auto-mute if threshold reached
    if (violationCount >= autoMuteThreshold)
    {
        MutePlayer(connectionId, 30, $"Auto-muted: {violationCount} violations");
    }
}
```

---

## Chat Logging

### LogChatMessage
```csharp
[Server]
public void LogChatMessage(uint connectionId, string playerName, string message, string channel)
{
    ChatLogEntry entry = new ChatLogEntry
    {
        timestamp = DateTime.Now,
        connectionId = connectionId,
        playerName = playerName,
        message = message,
        channel = channel
    };

    chatLogs.Add(entry);
    CleanupOldLogs();  // Remove logs older than retention period
}
```

### GetPlayerChatLogs
```csharp
[Server]
public List<ChatLogEntry> GetPlayerChatLogs(uint connectionId)
{
    return chatLogs.FindAll(log => log.connectionId == connectionId);
}
```

---

## Report System

### CmdSubmitReport
```csharp
[Command(requiresAuthority = false)]
public void CmdSubmitReport(uint targetConnectionId, string category,
                            string description, NetworkConnectionToClient sender = null)
{
    string reportId = Guid.NewGuid().ToString();

    PlayerReport report = new PlayerReport
    {
        reportId = reportId,
        reporterConnectionId = (uint)sender.connectionId,
        targetConnectionId = targetConnectionId,
        category = category,
        description = description,
        timestamp = DateTime.Now
    };

    pendingReports[reportId] = report;

    // Confirm to reporter
    TargetReportSubmitted(sender);
}
```

---

## Client RPCs

```csharp
[TargetRpc]
private void TargetPlayerMuted(NetworkConnection target, int durationMinutes, string reason)
// Shows mute notification to player

[TargetRpc]
private void TargetPlayerUnmuted(NetworkConnection target)
// Shows unmute notification to player

[TargetRpc]
private void TargetReportSubmitted(NetworkConnection target)
// Confirms report was received
```

---

## Usage Example

```csharp
// Check mute status before allowing chat
if (moderationManager.IsPlayerMuted(connectionId))
{
    // Block message, player is muted
    return;
}

// Record violation from ChatManager
if (containsProfanity)
{
    moderationManager.RecordViolation(connectionId, "Profanity");
}

// Log chat for moderation review
moderationManager.LogChatMessage(connectionId, playerName, message, "World");

// Admin mutes player
moderationManager.MutePlayer(targetConnectionId, 60, "Spamming");

// Admin bans account
moderationManager.BanPlayer(accountId, "Cheating");

// Client submits report
moderationManager.CmdSubmitReport(targetId, "Harassment", "Player was toxic in chat");
```

---

## Integration Points

### Dependencies
- `Mirror` - NetworkBehaviour, Server/Client RPCs
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `ChatManager` - Mute checks, violation recording, chat logging
- `AdminManager` - Mute/ban commands
- `PlayerContextMenu` - Report submission UI

---

## Report Categories

| Category | Description |
|----------|-------------|
| Spam | Excessive or repeated messages |
| Harassment | Toxic behavior, personal attacks |
| Cheating | Suspected hacks or exploits |
| Inappropriate | Offensive content, NSFW |
| Other | General rule violations |

---

## Design Notes

### Server-Only State
- All moderation state stored server-side only
- Clients cannot access muted/banned lists
- Prevents manipulation

### Auto-Mute System
- Tracks violations per connection
- Auto-mutes after 3 violations (configurable)
- 30-minute auto-mute duration

### Mute Expiration
- Mutes checked lazily (on IsPlayerMuted call)
- Auto-unmutes when expired
- No scheduled cleanup needed

### Chat Log Retention
- Default 24-hour retention
- Cleaned up when new logs added
- Enables retroactive moderation

### Report Workflow
- Players submit reports via Command
- Reports stored in pendingReports
- TODO: Admin notification system
- TODO: Admin review panel

### TODOs in Code
- Disconnect banned players
- Show mute/unmute UI notifications
- Show report confirmation UI
- Admin notification system
