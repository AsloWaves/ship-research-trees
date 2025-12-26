# PortReturnHandler

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/PortReturnHandler.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 185 |
| **Status** | **⚠️ DEPRECATED - Use new port system instead** |
| **Architecture** | Player ship positioning for harbor returns (non-networked) |

## Deprecation Notice

```csharp
[Obsolete("Use WOS.Port.Player.PlayerPortStateController instead.
          Functionality has been migrated to CheckForPortReturn() method.
          This script uses PlayerPrefs which has been replaced by
          PortSceneStateHolder ScriptableObject.")]
```

### Migration Path

| Old System | New System |
|------------|------------|
| `PortReturnHandler` | `WOS.Port.Player.PlayerPortStateController.CheckForPortReturn()` |
| `PlayerPrefs` persistence | `WOS.Port.Core.PortSceneStateHolder` |
| Manual state reset | Unified state management system |

## Purpose

Handles returning the player to the main scene after exiting a harbor. Attaches to player ship in main scene and checks for port exit data on scene load. **Non-networked version** - for single-player or local testing.

## Configuration

### Return Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `autoCheckOnStart` | `bool` | `true` | Automatically check for port exit data on Start |
| `shipController` | `SimpleNavalController` | - | Ship controller reference (auto-finds if null) |
| `cameraController` | `SimpleCameraController` | - | Camera controller reference (auto-finds if null) |

### Debug

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `showDebugInfo` | `bool` | `true` | Show debug messages in console |

## Key Features

### Automatic Port Return Detection

```csharp
// Checks PlayerPrefs on Start
if (PlayerPrefs.GetInt("PortExit_Valid", 0) == 1)
{
    // Valid port exit data found
    RestoreShipFromPortExit();
    PlayerPrefs.DeleteKey("PortExit_Valid"); // Clear flag
}
```

### Ship State Restoration

```csharp
// Restores ship position, rotation, and state
transform.position = exitPosition;
transform.rotation = exitRotation;
ResetShipState(); // Physics + controller reset
```

### Camera Following

```csharp
// Auto-sets camera to follow ship
if (cameraController != null)
{
    cameraController.SetTarget(transform);
}
```

## Public API

### Main Methods

#### `CheckForPortReturn()`
```csharp
public void CheckForPortReturn()
```

Checks for valid port exit data and restores ship if found.

**Data Flow**:
1. Check `PortExit_Valid` flag in PlayerPrefs
2. If found, read position and rotation
3. Apply to ship transform
4. Reset ship physics and controller
5. Set camera to follow ship
6. Clean up PlayerPrefs
7. Clear valid flag

### Context Menu Methods

#### `ForcePortReturnCheck()`
```csharp
[ContextMenu("Force Port Return Check")]
public void ForcePortReturnCheck()
```

Manually trigger port return check. Useful for testing.

## Usage Examples

### Basic Setup

```csharp
// Player Ship Setup (Single-Player):
// 1. Add PortReturnHandler to player ship prefab
// 2. Assign shipController (or leave null to auto-find)
// 3. Assign cameraController (or leave null to auto-find)
// 4. Enable autoCheckOnStart = true
// 5. Enable showDebugInfo = true for testing
```

### Integration with Harbor System

```csharp
// Complete Flow:
// 1. SimplePortTest (Ocean) → Saves entry data
// 2. HarborExitManager (Harbor) → Saves exit data
// 3. PortReturnHandler (Ocean) → Restores ship at exit position

// NOTE: For networked multiplayer, use ScenePortManager instead
```

### Expected Console Output

```
[PortReturnHandler] PORT RETURN DETECTED - Restoring ship position
  Ship restored to position: (1234.5, 678.9, 0)
  Ship rotation set to: (0, 0, 225) (180° from entry)
  Rigidbody2D rotation synchronized
  Throttle reset to 0
  Speed reset to 0
  Ship state reset - Ready for player control
  Use W/S to control throttle and move
  Camera set to follow ship
  Port transition data cleaned up
```

## Integration Points

### Ship Controller

```csharp
// Uses reflection to reset SimpleNavalController private fields
var throttleField = typeof(SimpleNavalController)
    .GetField("currentThrottle", BindingFlags.NonPublic | BindingFlags.Instance);
throttleField.SetValue(shipController, 0f);

var speedField = typeof(SimpleNavalController)
    .GetField("currentSpeed", BindingFlags.NonPublic | BindingFlags.Instance);
speedField.SetValue(shipController, 0f);
```

### PlayerPrefs Data

```csharp
// Reads exit data saved by HarborExitManager
string posJson = PlayerPrefs.GetString("PortExit_Position");
Vector3 exitPosition = JsonUtility.FromJson<Vector3>(posJson);

string rotJson = PlayerPrefs.GetString("PortExit_Rotation");
Quaternion exitRotation = JsonUtility.FromJson<Quaternion>(rotJson);
```

## Design Notes

### Auto-Component Finding

```csharp
// Finds components if not manually assigned
if (shipController == null)
{
    shipController = GetComponent<SimpleNavalController>();
}

if (cameraController == null)
{
    cameraController = FindFirstObjectByType<SimpleCameraController>();
}
```

### Ship State Reset

```csharp
void ResetShipState()
{
    // Rigidbody2D reset
    rb.bodyType = RigidbodyType2D.Dynamic; // Ensure physics enabled
    rb.linearVelocity = Vector2.zero;      // Stop movement
    rb.angularVelocity = 0f;               // Stop rotation

    // Controller reset (via reflection)
    throttleField.SetValue(shipController, 0f);
    speedField.SetValue(shipController, 0f);

    // Re-enable controller
    shipController.enabled = true;
}
```

### Data Cleanup

```csharp
void CleanupPortData()
{
    PlayerPrefs.DeleteKey("PortEntry_Position");
    PlayerPrefs.DeleteKey("PortEntry_Rotation");
    PlayerPrefs.DeleteKey("PortEntry_PortID");
    PlayerPrefs.DeleteKey("PortEntry_ExitScene");
    PlayerPrefs.DeleteKey("PortExit_Position");
    PlayerPrefs.DeleteKey("PortExit_Rotation");
    PlayerPrefs.DeleteKey("PortExit_Throttle");
    PlayerPrefs.DeleteKey("PortExit_Speed");
    PlayerPrefs.Save();
}
```

## Comparison: PortReturnHandler vs ScenePortManager

| Feature | PortReturnHandler | ScenePortManager |
|---------|-------------------|-------------------|
| **Network Support** | ❌ No | ✅ Yes (Mirror) |
| **Target** | `SimpleNavalController` | `NetworkedNavalController` |
| **Authority** | Local | Server-authoritative |
| **Port Finding** | ❌ No | ✅ Yes (port-relative) |
| **Use Case** | Single-player testing | Multiplayer production |
| **Deprecated** | ✅ Yes | ✅ Yes (both replaced by new system) |

## Troubleshooting

### Issue: Ship not positioned on return
**Solution**: Check `PortExit_Valid` flag in PlayerPrefs (use Debug.Log)

### Issue: Ship still moving after exit
**Solution**: Verify `ResetShipState()` is called and `shipController.enabled = true`

### Issue: Camera not following
**Solution**: Ensure `SimpleCameraController` exists in scene and is found

### Issue: Wrong rotation
**Solution**: Check `HarborExitManager` saved correct 180° rotation

## Related Scripts

- **HarborExitManager**: Harbor scene exit handler (saves exit data) [DEPRECATED]
- **ScenePortManager**: Networked version of this script [DEPRECATED]
- **SimpleNavalController**: Non-networked ship controller
- **SimpleCameraController**: Camera following system
- **PlayerPortStateController**: NEW - Replacement for this script
