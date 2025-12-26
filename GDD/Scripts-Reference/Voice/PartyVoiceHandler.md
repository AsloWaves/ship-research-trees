# PartyVoiceHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Voice/PartyVoiceHandler.cs` |
| **Namespace** | `WOS.Voice` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~112 |
| **Architecture** | Party-specific voice chat handler |

## Purpose
Handles party-specific voice chat using Odin rooms. Automatically joins/leaves voice rooms when the player joins/leaves a party. Provides volume control and member muting for party voice.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `enablePartyVoice` | true | Enable party voice chat |
| `partyVoiceVolume` | 1.0 | Party voice volume (0-1) |

---

## Core Methods

### Party Events
```csharp
// Called when player joins a party
public void OnJoinedParty(string partyId)
{
    currentPartyRoomName = $"party_{partyId}";
    OdinManager.Instance.JoinRoom(currentPartyRoomName, OdinRoomType.Party);
}

// Called when player leaves a party
public void OnLeftParty()
{
    OdinManager.Instance.LeaveRoom(currentPartyRoomName);
    currentPartyRoomName = "";
}
```

### Audio Control
```csharp
// Set party voice volume
public void SetPartyVolume(float volume)
{
    partyVoiceVolume = Mathf.Clamp01(volume);

    // Apply to all party room playback components
    PlaybackComponent[] playbacks =
        OdinHandler.Instance.GetPlaybackComponents(currentPartyRoomName);
    foreach (var playback in playbacks)
        playback.PlaybackSource.volume = partyVoiceVolume;
}

// Mute a specific party member
public void MutePartyMember(string playerName, bool muted)
{
    OdinManager.Instance.MutePlayer(playerName, muted);
}
```

---

## Room Naming Convention

Party rooms use the format: `party_{partyId}`

Example: `party_abc123`

---

## Usage Example

```csharp
// When player joins a party
partyVoiceHandler.OnJoinedParty("party123");

// Adjust volume
partyVoiceHandler.SetPartyVolume(0.75f);

// Mute annoying party member
partyVoiceHandler.MutePartyMember("LoudPlayer", true);

// When player leaves party
partyVoiceHandler.OnLeftParty();
```

---

## Integration Points

### Dependencies
- `OdinManager` - Room management
- `OdinNative.Unity` - Playback components
- `WOS.Debugging.DebugManager` - Logging

### Called By
- Party system when player joins/leaves
- Voice settings panel for volume control

---

## Design Notes

### Automatic Room Management
- Room joined automatically when party joined
- Room left automatically when party left
- Room left on component destroy

### Volume Per Channel
- Party volume independent of master volume
- Applied to all playback components in party room
