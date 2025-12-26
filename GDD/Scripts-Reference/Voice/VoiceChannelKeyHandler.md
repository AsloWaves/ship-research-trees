# VoiceChannelKeyHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Voice/VoiceChannelKeyHandler.cs` |
| **Namespace** | `WOS.Voice` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~363 |
| **Architecture** | Voice channel hotkey and mute management |

## Purpose
Runtime handler for voice channel mute hotkeys. Listens for key presses during gameplay and toggles channel mutes with audio/visual feedback. Integrates with VoiceSettingsData for persistence.

---

## Configuration

### Inspector Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `voiceSettings` | VoiceSettingsData | Voice settings asset |
| `proximityVoiceHandler` | (auto-find) | Proximity handler reference |
| `partyVoiceHandler` | (auto-find) | Party handler reference |
| `playSoundFeedback` | true | Play audio on toggle |
| `muteSound` | AudioClip | Sound when muting |
| `unmuteSound` | AudioClip | Sound when unmuting |
| `showNotification` | true | Show visual notification |
| `notificationDuration` | 2s | Notification display time |

---

## Channel Hotkeys

Hotkeys defined in `VoiceSettingsData`:
- `proximityMuteKey` - Toggle proximity voice
- `partyMuteKey` - Toggle party voice
- `guildMuteKey` - Toggle guild voice
- `nationMuteKey` - Toggle nation voice
- `portMuteKey` - Toggle port voice

---

## Mute Toggle Flow

```csharp
private void Update()
{
    if (voiceSettings == null) return;

    // Block when typing
    if (UIInputBlocker.IsInputActive()) return;

    // Check hotkeys
    if (Input.GetKeyDown(voiceSettings.proximityMuteKey))
        ToggleProximityMute();

    if (Input.GetKeyDown(voiceSettings.partyMuteKey))
        TogglePartyMute();

    // ... other channels
}

public void ToggleProximityMute()
{
    voiceSettings.proximityMuted = !voiceSettings.proximityMuted;

    // Apply to handler
    if (proximityVoiceHandler != null)
        proximityVoiceHandler.enableProximityVoice = !voiceSettings.proximityMuted;

    // Persist
    voiceSettings.SaveToPlayerPrefs();

    // Feedback
    OnChannelMuteToggled("Proximity", voiceSettings.proximityMuted);
}
```

---

## Mute Toggle Methods

```csharp
public void ToggleProximityMute()   // Toggle proximity channel
public void TogglePartyMute()       // Toggle party channel
public void ToggleGuildMute()       // Toggle guild channel
public void ToggleNationMute()      // Toggle nation channel
public void TogglePortMute()        // Toggle port channel
```

---

## Feedback System

```csharp
private void OnChannelMuteToggled(string channelName, bool isMuted)
{
    // Audio feedback
    if (playSoundFeedback && audioSource != null)
    {
        AudioClip clip = isMuted ? muteSound : unmuteSound;
        if (clip != null)
            audioSource.PlayOneShot(clip);
    }

    // Visual notification
    if (showNotification)
    {
        string message = $"{channelName} voice: {(isMuted ? "MUTED" : "UNMUTED")}";
        ShowNotification(message);
    }
}
```

---

## Public API

```csharp
// Get mute state for channel
public bool IsChannelMuted(string channelName)
// Returns: true if muted

// Set mute state for channel
public void SetChannelMute(string channelName, bool muted)
// channelName: "proximity", "party", "guild", "nation", "port"
```

---

## Usage Example

```csharp
var keyHandler = GetComponent<VoiceChannelKeyHandler>();

// Check if channel is muted
if (keyHandler.IsChannelMuted("proximity"))
    Debug.Log("Proximity voice is muted");

// Programmatically mute a channel
keyHandler.SetChannelMute("party", true);

// Toggle via method (same as hotkey)
keyHandler.ToggleProximityMute();
```

---

## Integration Points

### Dependencies
- `VoiceSettingsData` - Hotkeys and mute states
- `ProximityVoiceHandler` - Proximity voice control
- `PartyVoiceHandler` - Party voice control
- `UIInputBlocker` - Input blocking
- `WOS.Debugging.DebugManager` - Logging

### Auto-Discovery
- Finds `VoiceSettingsData` in Resources if not assigned
- Auto-finds voice handlers via `FindFirstObjectByType`

---

## Design Notes

### Input Blocking
- Hotkeys blocked when typing in chat
- Uses `UIInputBlocker.IsInputActive()`

### Persistence
- Mute states saved via `VoiceSettingsData.SaveToPlayerPrefs()`
- Restored on game load

### Feedback
- Audio clips for mute/unmute (optional)
- Visual notification (placeholder for UI system)

### Future TODOs
- Integration with notification UI system
- Guild and nation voice handler integration
