# ScenePortManager

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/ScenePortManager.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 381 |
| **Status** | **⚠️ DEPRECATED - Use new port system instead** |
| **Architecture** | Networked player positioning for harbor returns |

## Deprecation Notice

```csharp
[Obsolete("Use WOS.Port.Core.PortTransitionManager and
          WOS.Port.Player.PlayerPortStateController instead.
          This script uses PlayerPrefs which has been replaced by
          PortSceneStateHolder ScriptableObject.")]
```

### Migration Path

| Old System | New System |
|------------|------------|
| `ScenePortManager` | `WOS.Port.Core.PortTransitionManager` |
| `PlayerPrefs` persistence | `WOS.Port.Core.PortSceneStateHolder` |
| Manual player positioning | `WOS.Port.Player.PlayerPortStateController` |

## Purpose

Manages networked player positioning when returning from harbor scenes. Works with Mirror NetworkManager - does NOT spawn players, only positions already-spawned networked ships at exit coordinates with proper rotation.

## Configuration

### Network Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `showNetworkDebug` | `bool` | `true` | Log network-specific debug messages |

### Camera Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `cameraController` | `SimpleCameraController` | - | Camera reference (auto-finds if null) |

### Spawn Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `defaultSpawnPosition` | `Vector3` | `(0, 0, 0)` | Fallback spawn position |
| `defaultSpawnRotation` | `Vector3` | `(0, 0, 0)` | Fallback spawn rotation |

### Ship Orientation

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `shipSpriteForwardOffset` | `float` | `90f` | Sprite forward direction (90° if sprite points up, 0° if points right) |

## Key Features

### Network-Aware Positioning

```csharp
// CRITICAL: Server-authoritative positioning
if (NetworkServer.active)
{
    localPlayerShip.transform.position = exitPosition;
    localPlayerShip.transform.rotation = exitRotation;
    ResetShipStateAfterPort(localPlayerShip, exitRotation);
}

// Only server modifies player position (Mirror sync)
```

### Port-Relative Exit Calculation

```csharp
// NEW SYSTEM: Port-relative positioning
1. Read port ID from PlayerPrefs
2. Find matching SimplePortTest in scene
3. Get current port center position
4. Calculate exit = portCenter + relativeOffset
5. Calculate rotation facing AWAY from port
```

### Directional Exit Rotation

```csharp
// Always face AWAY from port, regardless of entry direction
Vector3 directionAwayFromPort = (exitPosition - portCenter).normalized;
float angleInDegrees = Mathf.Atan2(directionAwayFromPort.y,
                                   directionAwayFromPort.x) * Mathf.Rad2Deg;
exitRotation = Quaternion.Euler(0, 0, angleInDegrees);
```

## Public API

### Context Menu Methods

#### `ForcePortReturnCheck()`
```csharp
[ContextMenu("Force Port Return Check")]
public void ForcePortReturnCheck()
```

Manually trigger port return check. Useful for testing or debugging exit issues.

## Usage Examples

### Basic Setup

```csharp
// Ocean Scene Setup:
// 1. Create GameObject "ScenePortManager"
// 2. Add ScenePortManager component
// 3. Set showNetworkDebug = true
// 4. Assign cameraController (or leave null to auto-find)
// 5. Leave default positions as fallbacks
```

### Network Flow

```csharp
// Server (Host) Flow:
// 1. NetworkManager spawns player ship (server authority)
// 2. ScenePortManager waits 0.5s for spawn
// 3. Finds local player via NetworkIdentity.isLocalPlayer
// 4. Checks for PortExit_Valid flag
// 5. Calculates exit position (port-relative)
// 6. SERVER positions ship and resets state
// 7. Mirror syncs to all clients

// Client Flow:
// 1. Receives spawned ship from server
// 2. ScenePortManager skips positioning (not server)
// 3. Receives position/rotation via Mirror sync
```

### Expected Console Output

```
[ScenePortManager] Found LOCAL networked player: PlayerShip(Clone)
[ScenePortManager] PORT RETURN DETECTED - Calculating port-relative exit
  Found port 'Pearl_Harbor_Tier3' at (1000, 500)
  Calculated exit position: (1000, 500) + (234.5, 178.9) = (1234.5, 678.9)
  Direction away from port: (0.80, 0.60)
  Atan2 angle: 36.87° (pointing direction)
  Exit rotation set to: (0, 0, 36.87)
[SERVER] Positioned networked player at (1234.5, 678.9), rotation: (0, 0, 36.87)
  Rigidbody2D rotation synchronized: 36.87°
  Network throttle reset to 0
  Network speed reset to 0
  Rudder angle reset to 0
  Networked ship ready for player control
```

## Integration Points

### Player Detection

```csharp
// Finds LOCAL player among all networked ships
var allShips = FindObjectsByType<NetworkedNavalController>(FindObjectsSortMode.None);
foreach (var shipCtrl in allShips)
{
    var networkIdentity = shipCtrl.GetComponent<NetworkIdentity>();
    if (networkIdentity != null && networkIdentity.isLocalPlayer)
    {
        localPlayerShip = shipCtrl.gameObject;
        return;
    }
}
```

### Port Finder

```csharp
// Finds port by ScriptableObject name (port ID)
SimplePortTest FindPortByID(string portID)
{
    SimplePortTest[] allPorts = FindObjectsByType<SimplePortTest>(...);
    foreach (var port in allPorts)
    {
        if (port.portConfig != null && port.portConfig.name == portID)
            return port;
    }
    return null;
}
```

### Ship State Reset

```csharp
// Resets NetworkedNavalController via reflection
var shipType = typeof(NetworkedNavalController);
var throttleField = shipType.GetField("currentThrottle",
    BindingFlags.NonPublic | BindingFlags.Instance);
throttleField.SetValue(shipController, 0f);

// Also resets:
// - currentSpeed (SyncVar)
// - effectiveRudderAngle (SyncVar)
// - Rigidbody2D (Dynamic, zero velocity)
```

## Design Notes

### Startup Sequence

```csharp
// Waits for NetworkManager spawn before checking
IEnumerator WaitForNetworkSpawnAndCheckPortReturn()
{
    yield return new WaitForSeconds(0.5f); // Allow spawn to complete
    FindLocalPlayerShip();
    if (NetworkServer.active && !hasCheckedPortReturn)
    {
        CheckAndHandlePortReturn();
        hasCheckedPortReturn = true; // Prevent double-check
    }
}
```

### Rotation Calculation

```csharp
// 2D top-down rotation calculation
// Ship sprite pointing up (north) = 0° rotation in Unity
float angleInDegrees = Mathf.Atan2(directionAwayFromPort.y,
                                   directionAwayFromPort.x) * Mathf.Rad2Deg;

// No sprite offset applied (shipSpriteForwardOffset unused in current version)
```

### Data Cleanup

```csharp
// Cleans up ALL port-related PlayerPrefs after successful positioning
void CleanupPortData()
{
    PlayerPrefs.DeleteKey("PortEntry_Position");
    PlayerPrefs.DeleteKey("PortEntry_Rotation");
    PlayerPrefs.DeleteKey("PortEntry_PortID");
    PlayerPrefs.DeleteKey("PortEntry_ExitScene");
    PlayerPrefs.DeleteKey("PortEntry_PortCenter");
    PlayerPrefs.DeleteKey("PortEntry_RelativeOffset");
    PlayerPrefs.DeleteKey("PortExit_Position");
    PlayerPrefs.DeleteKey("PortExit_Rotation");
    PlayerPrefs.DeleteKey("PortExit_Throttle");
    PlayerPrefs.DeleteKey("PortExit_Speed");
    PlayerPrefs.Save();
}
```

### Rigidbody Synchronization

```csharp
// CRITICAL: Set rotation AFTER body is Dynamic
rb.bodyType = RigidbodyType2D.Dynamic;
rb.rotation = targetRotation.eulerAngles.z; // 2D rotation (Z-axis)
rb.linearVelocity = Vector2.zero;
rb.angularVelocity = 0f;

// Ensures physics engine has correct rotation before resetting velocities
```

## Troubleshooting

### Issue: Ship not positioned on return
**Solution**: Verify `NetworkServer.active` is true (must be server or host)

### Issue: Ship positioned but rotation wrong
**Solution**: Check `shipSpriteForwardOffset` matches sprite orientation

### Issue: Port not found
**Solution**: Ensure SimplePortTest exists in scene with matching `portConfig.name`

### Issue: Ship still moving after exit
**Solution**: Verify `ResetShipStateAfterPort()` resets Rigidbody2D and SyncVars

### Issue: Double positioning
**Solution**: Check `hasCheckedPortReturn` flag prevents multiple checks

## Related Scripts

- **HarborExitManager**: Harbor scene exit handler (saves exit data) [DEPRECATED]
- **SimplePortTest**: Port entry/docking (saves entry data)
- **NetworkedNavalController**: Ship physics with SyncVars
- **SimpleCameraController**: Camera following system
- **PortTransitionManager**: NEW - Replacement for this system
- **PlayerPortStateController**: NEW - Player state management
