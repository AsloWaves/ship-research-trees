# ProximityVoiceHandler.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Voice/ProximityVoiceHandler.cs` |
| **Namespace** | `WOS.Voice` |
| **Inheritance** | `NetworkBehaviour` |
| **Required Components** | `ProximityDetector` |
| **Lines** | ~241 |
| **Architecture** | Proximity-based 3D spatial voice chat |

## Purpose
Handles proximity-based spatial voice chat using Odin. Implements 3D positional audio with distance-based volume falloff, enabling players to hear nearby ships with realistic spatial positioning.

---

## Configuration

### Inspector Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `enableProximityVoice` | true | Enable proximity voice |
| `maxProximityRange` | 50 units | Maximum voice range |
| `volumeFalloffCurve` | Linear | Distance → volume curve |
| `proximityVoiceVolume` | 1.0 | Base volume (0-1) |
| `positionUpdateInterval` | 0.1s | Position sync frequency |
| `useDirectionalAudio` | true | Left/right positioning |
| `useDopplerEffect` | false | Doppler simulation |

---

## Spatial Audio Flow

### 1. Join Proximity Room
```csharp
public override void OnStartClient()
{
    if (!isLocalPlayer) return;

    proximityDetector = GetComponent<ProximityDetector>();

    if (enableProximityVoice && OdinManager.Instance != null)
        JoinProximityVoice();
}

private void JoinProximityVoice()
{
    OdinManager.Instance.JoinRoom("proximity_world", OdinRoomType.Proximity);
}
```

### 2. Update 3D Positions
```csharp
private void Update()
{
    if (!isClient || !isLocalPlayer || !enableProximityVoice)
        return;

    positionUpdateTimer += Time.deltaTime;
    if (positionUpdateTimer >= positionUpdateInterval)  // Every 0.1s
    {
        UpdateSpatialAudioPositions();
        positionUpdateTimer = 0f;
    }
}
```

### 3. Apply Spatial Audio
```csharp
private void UpdateSpatialAudioPositions()
{
    Vector3 myPosition = transform.position;

    foreach (var ship in proximityDetector.NearbyShips)
    {
        Vector3 targetPosition = ship.transform.position;
        float distance = Vector3.Distance(myPosition, targetPosition);

        // Calculate volume from distance
        float normalizedDistance = Mathf.Clamp01(distance / maxProximityRange);
        float volume = volumeFalloffCurve.Evaluate(normalizedDistance)
                       * proximityVoiceVolume;

        // Find Odin peer and apply
        Peer peer = FindPeerForShip(proximityRoom, ship);
        if (peer != null)
        {
            foreach (var playback in OdinHandler.Instance.GetPlaybackComponents(peer.Id))
            {
                playback.PlaybackSource.volume = volume;
                playback.PlaybackSource.spatialBlend = useDirectionalAudio ? 1.0f : 0.0f;

                if (useDirectionalAudio)
                    playback.transform.position = targetPosition;
            }
        }
    }
}
```

---

## Peer Matching

```csharp
private Peer FindPeerForShip(Room room, NetworkedNavalController ship)
{
    uint shipNetId = ship.netId;

    foreach (var peer in room.RemotePeers)
    {
        string peerData = peer.UserData?.ToString() ?? "";

        // Format: "ShipName:NetId" or just NetId
        if (peerData.Contains(":"))
        {
            string[] parts = peerData.Split(':');
            if (uint.TryParse(parts[1], out uint peerNetId))
                if (peerNetId == shipNetId)
                    return peer;
        }
        else if (uint.TryParse(peerData, out uint peerNetId))
        {
            if (peerNetId == shipNetId)
                return peer;
        }
    }
    return null;
}
```

---

## Public API

```csharp
// Set proximity voice volume
public void SetProximityVolume(float volume)

// Set maximum proximity range
public void SetProximityRange(float range)
```

---

## Usage Example

```csharp
// Configure proximity voice
proximityVoiceHandler.SetProximityVolume(0.9f);
proximityVoiceHandler.SetProximityRange(100f);  // 100 unit range

// Check nearby ships from ProximityDetector
foreach (var ship in proximityVoiceHandler.GetComponent<ProximityDetector>().NearbyShips)
{
    Debug.Log($"Can hear: {ship.name}");
}
```

---

## Integration Points

### Dependencies
- `ProximityDetector` - Nearby ship detection (required)
- `OdinManager` - Room management
- `OdinNative.Unity` - Spatial audio components
- `WOS.Player.NetworkedNavalController` - Ship matching

### Room Name
- Single server-wide room: `proximity_world`

---

## Design Notes

### Spatial Audio Implementation
- Uses Unity AudioSource spatialBlend for 3D positioning
- PlaybackComponent positions updated to match ship positions
- Volume falloff via AnimationCurve for custom falloff shapes

### Performance Optimization
- Position updates limited to 10/second (configurable)
- Only processes nearby ships from ProximityDetector
- Skips inactive or null ships

### Peer Matching
- Matches Odin peers to ships via NetworkIdentity netId
- User data format: `ShipName:NetId` or just `NetId`
