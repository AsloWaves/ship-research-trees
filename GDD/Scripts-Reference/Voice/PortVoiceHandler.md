# PortVoiceHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Voice/PortVoiceHandler.cs` |
| **Namespace** | `WOS.Voice` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~87 |
| **Architecture** | Port-specific voice chat handler |

## Purpose
Handles port-specific voice chat using Odin rooms. Automatically joins/leaves voice rooms when the player's ship enters/exits a port. Provides volume control for port voice channels.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `enablePortVoice` | true | Enable port voice chat |
| `portVoiceVolume` | 1.0 | Port voice volume (0-1) |

---

## Core Methods

### Port Events
```csharp
// Called when ship enters a port
public void OnEnteredPort(string portId, string portName)
{
    if (!enablePortVoice || OdinManager.Instance == null)
        return;

    currentPortRoomName = $"port_{portId}";
    OdinManager.Instance.JoinRoom(currentPortRoomName, OdinRoomType.Port);
}

// Called when ship exits a port
public void OnExitedPort(string portName)
{
    if (string.IsNullOrEmpty(currentPortRoomName))
        return;

    OdinManager.Instance.LeaveRoom(currentPortRoomName);
    currentPortRoomName = "";
}
```

### Volume Control
```csharp
public void SetPortVolume(float volume)
{
    portVoiceVolume = Mathf.Clamp01(volume);
    // TODO: Apply to Odin room playback components
}
```

---

## Room Naming Convention

Port rooms use the format: `port_{portId}`

Example: `port_new_york`

---

## Usage Example

```csharp
// When ship enters port
portVoiceHandler.OnEnteredPort("new_york", "New York Harbor");

// Adjust volume
portVoiceHandler.SetPortVolume(0.6f);

// When ship exits port
portVoiceHandler.OnExitedPort("New York Harbor");
```

---

## Integration Points

### Dependencies
- `OdinManager` - Room management
- `WOS.Debugging.DebugManager` - Logging

### Called By
- Port system when ship enters/exits
- `PlayerPortStateController` state transitions
- Voice settings panel

---

## Design Notes

### Automatic Room Management
- Room joined when entering port
- Room left when exiting port
- Room left on component destroy

### Zone-Based Voice
- Each port has its own voice room
- Players in same port can communicate
- Exits port = leaves voice room
