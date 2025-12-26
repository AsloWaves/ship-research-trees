# OdinManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Voice/OdinManager.cs` |
| **Namespace** | `WOS.Voice` |
| **Inheritance** | `MonoBehaviour` |
| **Pattern** | Singleton with DontDestroyOnLoad |
| **Lines** | ~496 |
| **Architecture** | Central Odin SDK voice chat manager |

## Purpose
Singleton manager for the Odin voice chat system (4Players.io). Handles SDK initialization, room management, push-to-talk controls, volume settings, and event handling for all voice chat functionality.

---

## Configuration

### Inspector Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `odinAccessKey` | "" | Odin API access key from 4Players.io |
| `enableVoiceChat` | true | Master voice chat toggle |
| `pushToTalkMode` | true | PTT mode vs voice activity detection |
| `pushToTalkKey` | V | Key for push-to-talk |
| `masterVolume` | 1.0 | Master volume (0-1) |
| `showDebugLogs` | true | Enable debug logging |

---

## Room Types

```csharp
public enum OdinRoomType
{
    Party,          // Party voice (room-based)
    Proximity,      // Proximity voice (spatial audio)
    Port,           // Port voice (zone-based)
    Nation,         // Nation voice (faction-based)
    Guild,          // Guild voice (clan-based)
    World           // World voice (server-wide)
}
```

---

## Core Methods

### Initialization
```csharp
private void InitializeOdin()
{
    // Configure access key
    if (OdinHandler.Config != null)
        OdinHandler.Config.AccessKey = odinAccessKey;

    // Wire up event listeners
    OdinHandler.Instance.OnRoomJoined.AddListener(OnOdinRoomJoined);
    OdinHandler.Instance.OnRoomLeft.AddListener(OnOdinRoomLeft);
    OdinHandler.Instance.OnPeerJoined.AddListener(OnOdinPeerJoined);
    OdinHandler.Instance.OnPeerLeft.AddListener(OnOdinPeerLeft);
    OdinHandler.Instance.OnMediaAdded.AddListener(OnOdinMediaAdded);
    OdinHandler.Instance.OnMediaRemoved.AddListener(OnOdinMediaRemoved);
}
```

### Room Management
```csharp
// Join a voice room
public void JoinRoom(string roomName, OdinRoomType roomType)

// Leave a voice room
public void LeaveRoom(string roomName)

// Leave all rooms
public void LeaveAllRooms()

// Check if in room
public bool IsInRoom(string roomName)

// Get active room names
public List<string> GetActiveRooms()
```

### Audio Control
```csharp
// Set master volume (0-1)
public void SetMasterVolume(float volume)

// Mute specific player
public void MutePlayer(string playerName, bool muted)
```

---

## Push-to-Talk

```csharp
private void Update()
{
    if (!enableVoiceChat || !pushToTalkMode)
        return;

    // Block PTT when typing in chat
    if (UIInputBlocker.IsInputActive())
    {
        if (isPushToTalkActive)
        {
            isPushToTalkActive = false;
            SetMicrophoneActive(false);
        }
        return;
    }

    // Handle PTT key
    bool wasPushToTalkActive = isPushToTalkActive;
    isPushToTalkActive = Input.GetKey(pushToTalkKey);

    if (isPushToTalkActive != wasPushToTalkActive)
        SetMicrophoneActive(isPushToTalkActive);
}

private void SetMicrophoneActive(bool active)
{
    OdinHandler.Instance.Microphone.SilenceCapturedAudio = !active;
}
```

---

## Event Handlers

| Event | Handler | Description |
|-------|---------|-------------|
| `OnRoomJoined` | `OnOdinRoomJoined` | Apply master volume to new room |
| `OnRoomLeft` | `OnOdinRoomLeft` | Remove from local tracking |
| `OnPeerJoined` | `OnOdinPeerJoined` | Log peer join |
| `OnPeerLeft` | `OnOdinPeerLeft` | Log peer leave |
| `OnMediaAdded` | `OnOdinMediaAdded` | New audio stream |
| `OnMediaRemoved` | `OnOdinMediaRemoved` | Audio stream ended |

---

## OdinRoomData Class

```csharp
public class OdinRoomData
{
    public string roomName;
    public OdinRoomType roomType;
    public DateTime joinedTime;

    public OdinRoomData(string name, OdinRoomType type)
    {
        roomName = name;
        roomType = type;
        joinedTime = DateTime.Now;
    }
}
```

---

## Usage Example

```csharp
// Join party voice room
OdinManager.Instance.JoinRoom("party_12345", OdinRoomType.Party);

// Set master volume
OdinManager.Instance.SetMasterVolume(0.8f);

// Mute a player
OdinManager.Instance.MutePlayer("PlayerName", true);

// Check room membership
if (OdinManager.Instance.IsInRoom("party_12345"))
    Debug.Log("In party voice");

// Leave room
OdinManager.Instance.LeaveRoom("party_12345");
```

---

## Integration Points

### Dependencies
- `OdinNative.Odin` - Odin SDK core
- `OdinNative.Unity` - Unity integration
- `WOS.UI.UIInputBlocker` - Input blocking during chat
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `PartyVoiceHandler` - Party voice rooms
- `ProximityVoiceHandler` - Proximity voice
- `PortVoiceHandler` - Port voice rooms
- `VoiceChannelKeyHandler` - Channel muting

---

## Design Notes

### Singleton Persistence
- Uses `DontDestroyOnLoad` for scene persistence
- Automatically moves to root if parented (Unity requirement)
- Cleans up event listeners on destroy

### PTT vs VAD
- Push-to-talk (PTT) is default mode
- Voice Activity Detection (VAD) available
- PTT blocked when typing in chat

### SDK Requirements
- Requires Odin SDK from 4Players.io
- OdinHandler component must exist in scene
- Access key from 4Players.io dashboard
