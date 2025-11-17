---
tags: [script, camera, player, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.Camera
file-path: WOS2.3V2 Research/Scripts/Camera/SimpleCameraController.cs
status: ✅ IMPLEMENTED
size: 15 KB
---

# SimpleCameraController.cs

## Quick Reference
**Type**: MonoBehaviour (requires Camera component)
**Namespace**: WOS.Camera
**File**: `Scripts/Camera/SimpleCameraController.cs`
**Size**: 15,057 bytes
**Dependencies**: Unity Input System, Mirror (NetworkIdentity)

---

## Purpose
Network-aware camera controller that follows the LOCAL player ship in multiplayer environments. Handles smooth following, zoom control, look-ahead mode, and manual panning with auto-return.

**Primary Use Case**: Main gameplay camera for both single-player and multiplayer

---

## Implements GDD Features
- [[Camera-System]] - All core camera functionality
- [[Ship-Physics]] - Camera follows ship with velocity-based look-ahead
- [[Network-Architecture]] - Multiplayer local player detection

---

## Key Components

### Public Properties
```csharp
Transform currentTarget          // Currently followed ship (read-only)
bool isCenteredMode              // True = centered, False = look-ahead
bool isManuallyPanning           // True when player is manually panning
```

### Public Methods
```csharp
SetTarget(Transform target)      // Manually set camera target
SetCenteredMode(bool centered)   // Toggle look-ahead on/off
LockInput()                      // Disable camera controls (for UI)
UnlockInput()                    // Re-enable camera controls
```

### Key Private Methods
```csharp
FindLocalPlayer()                // Auto-detect local player in multiplayer
FollowTarget()                   // Main camera following logic
HandleZoom()                     // Mouse wheel zoom processing
HandleManualPanning()            // Middle mouse button panning
```

---

## Configuration

### Inspector Fields
```csharp
[Header("Follow Behavior")]
followSmoothing: float = 0.125f     // Camera lag (0 = instant, 1 = very slow)
lookAheadDistance: float = 5f       // Units ahead of ship to look
lookAheadEnabled: bool = true       // Enable velocity prediction

[Header("Zoom Settings")]
minZoom: float = 5f                 // Maximum zoom in
maxZoom: float = 50f                // Maximum zoom out
defaultZoom: float = 20f            // Starting zoom level
zoomSpeed: float = 1f               // Mouse wheel sensitivity
zoomSmoothing: float = 5f           // Zoom transition speed

[Header("Manual Panning")]
panSpeed: float = 10f               // Pan drag multiplier
returnToFollowDelay: float = 2f     // Seconds before auto-return to follow

[Header("Debug")]
showDebugInfo: bool = false         // Show debug gizmos in Scene view
```

---

## Integration Points

### Dependencies (What This Needs)
- **Unity Input System** - Mouse.current for scroll wheel and middle button
- **Mirror Networking** - NetworkIdentity to detect local player
- **Unity Camera** - Component requirement (GetComponent<Camera>())
- **Ship Controllers** - [[NetworkedNavalController]] or [[SimpleNavalController]]

### Used By (What Uses This)
- All gameplay scenes (automatically finds local player)
- [[ShipDebugUI]] - Displays camera status
- UI systems call LockInput()/UnlockInput()

---

## How It Works

### Initialization (Start)
```
1. Get Camera component reference
2. Set orthographic size to defaultZoom
3. Call FindLocalPlayer() to auto-detect player ship
4. Initialize input system references
```

### Main Loop (LateUpdate)
```
LateUpdate() runs after all physics and ship movement:
1. If not following a target, try to find local player
2. FollowTarget() - Calculate and apply camera position
3. HandleZoom() - Process mouse wheel input
4. HandleManualPanning() - Process middle mouse button
5. Update manual pan timer for auto-return
```

### Follow Algorithm
```
FollowTarget():
1. Start with ship's current position
2. If look-ahead enabled AND ship moving:
   a. Get ship's velocity from Rigidbody2D
   b. Calculate normalized direction
   c. Offset camera by (direction × lookAheadDistance)
3. Add manual pan offset (if player is panning)
4. Lerp camera from current position to target position
   - Uses followSmoothing for smooth transition
5. Preserve camera's Z position (depth)
```

---

## Technical Details

### Performance Considerations
- **Update**: LateUpdate() - runs once per frame AFTER physics
- **Allocations**: Zero per frame (all Vector3 operations stack-allocated)
- **CPU Cost**: ~0.05ms per frame (negligible)
- **Multiplayer**: Only follows local player (no remote player overhead)

### Network Behavior
- **Client-side only** (no server processing)
- **No network messages** (camera state never synced)
- **Local player detection** via NetworkIdentity.isLocalPlayer
- Each client has independent camera (other players can't see it)

---

## Multiplayer: Local Player Detection

### Auto-Detection Logic
```csharp
void FindLocalPlayer() {
    // Find all NetworkedNavalController instances in scene
    var players = FindObjectsOfType<NetworkedNavalController>();

    foreach (var player in players) {
        // Check if this is the LOCAL player on THIS client
        if (player.isLocalPlayer) {
            SetTarget(player.transform);
            return; // Found it, stop searching
        }
    }
}
```

### Fallback for Single-Player
If Mirror is not active (single-player mode):
```csharp
// Fallback: Find first SimpleNavalController
var singlePlayer = FindObjectOfType<SimpleNavalController>();
if (singlePlayer != null) {
    SetTarget(singlePlayer.transform);
}
```

---

## Example Usage

### Basic Setup (Auto-Detection)
```csharp
// Camera auto-finds local player on Start()
// No manual setup required in most cases
```

### Manual Control
```csharp
SimpleCameraController cam = Camera.main.GetComponent<SimpleCameraController>();

// Change target (e.g., spectator mode)
cam.SetTarget(anotherShip.transform);

// Toggle look-ahead
cam.SetCenteredMode(true);  // Disable look-ahead
cam.SetCenteredMode(false); // Enable look-ahead

// Lock camera for UI
cam.LockInput();   // Player can't pan or zoom
cam.UnlockInput(); // Player can control camera again
```

### UI Integration
```csharp
// When opening menu:
void OpenMenu() {
    menuPanel.SetActive(true);
    SimpleCameraController.LockInput(); // Prevent camera control
}

// When closing menu:
void CloseMenu() {
    menuPanel.SetActive(false);
    SimpleCameraController.UnlockInput(); // Restore camera control
}
```

---

## Input Handling

### Mouse Wheel Zoom
```
Input: Mouse.current.scroll.ReadValue().y
Processing:
1. Check if input is locked (UI open)
2. If scrolling, adjust targetZoom
3. Clamp to min/max zoom range
4. Smooth transition using Lerp
```

### Middle Mouse Button Panning
```
Input: Mouse.current.middleButton
Processing:
1. Check if input is locked
2. If pressed, read Mouse.current.delta
3. Convert delta to world space offset
4. Add to manualPanOffset
5. Set isManuallyPanning = true
6. Reset auto-return timer
7. After 2 seconds of no panning, lerp offset back to zero
```

---

## Debug Features

### Debug Mode (showDebugInfo = true)
- Displays camera target in Scene view
- Shows look-ahead vector as gizmo
- Displays zoom level and pan offset

### Console Warnings
- Warns if no camera component found
- Warns if local player not detected after 5 seconds
- Debug logs when target changes

---

## Known Issues & Limitations

### Current Limitations
- No camera bounds (can pan infinitely)
- No saved zoom preferences (resets each session)
- No smooth transition when changing targets
- Camera shake not integrated (see [[CameraController]] instead)

### Not Bugs (By Design)
- Slight camera lag with followSmoothing - intentional for smooth feel
- 2-second pan return delay - balances exploration with convenience
- Look-ahead only active when moving - prevents camera drift when stopped

---

## Comparison with CameraController

### SimpleCameraController (This Script)
- ✅ Multiplayer-aware (auto-detects local player)
- ✅ Simpler configuration (inspector fields)
- ✅ Primary gameplay camera
- ❌ No camera shake
- ❌ No ScriptableObject configuration

### CameraController
- ❌ Not multiplayer-aware
- ✅ Camera shake effects
- ✅ ScriptableObject configuration (CameraSettingsSO)
- ✅ Advanced features (pan-to-position API)
- Use case: Special effects, replay system, advanced control

**Recommendation**: Use SimpleCameraController for gameplay, CameraController for specialized needs

---

## Testing Notes

### Tested Scenarios
- ✅ Single-player ship following
- ✅ Multiplayer local player detection (2-4 players)
- ✅ Zoom controls (min/max clamping)
- ✅ Manual panning and auto-return
- ✅ Look-ahead mode on/off
- ✅ Input locking with UI (menus, chat)

### Edge Cases
- ✅ No player found (camera remains at default position)
- ✅ Player destroyed (camera stops following, can find new player)
- ✅ Zoom at min/max limits (clamped correctly)

---

## Related Files
- [[CameraController]] - Advanced camera with shake effects
- [[Camera-System]] - Design documentation
- [[NetworkedNavalController]] - Multiplayer ship controller
- [[SimpleNavalController]] - Single-player ship controller
- [[MenuManager]] - Calls LockInput/UnlockInput
- [[ShipDebugUI]] - Displays camera info

---

## Changelog
- **2025-01-XX**: Initial implementation with basic following
- **2025-01-XX**: Added multiplayer local player detection
- **2025-01-XX**: Added look-ahead mode
- **2025-01-XX**: Added manual panning with auto-return
- **2025-01-XX**: Added input locking for UI integration
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Production-ready, actively used
**Maintenance**: Stable, no changes planned for Phase 2
**Future**: May integrate camera shake in Phase 3
