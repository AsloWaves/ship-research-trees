# Example: Script Reference Enhancement for GDD
## Before/After Comparison - Camera System Section

---

## 📋 BEFORE (Current GDD - Lines 1253-1257)

```markdown
**Camera System**:
- **Tactical View**: 2D top-down with dynamic zoom (10m to 100km scale)
- **Follow Mode**: Camera tracks player ship with smooth interpolation
- **Strategic Mode**: Full map overview for theater-level planning
- **Cinematic Mode**: Dynamic camera for dramatic combat moments (optional)
```

**Issues with Current Version**:
- ❌ No implementation status
- ❌ No script references
- ❌ Vague technical details ("smooth interpolation" - how smooth? what algorithm?)
- ❌ Missing features mentioned (Strategic Mode not implemented)
- ❌ No developer guidance
- ❌ Can't verify if this matches actual implementation

---

## ✅ AFTER (Enhanced with Script References)

```markdown
## **Camera System** [IMPLEMENTED ✅]

**Implementation Status**: IMPLEMENTED (Core features complete, advanced features planned)

**Script References**:
- `WOS2.3V2 Research/Scripts/Camera/SimpleCameraController.cs` - Primary camera controller (multiplayer-aware)
- `WOS2.3V2 Research/Scripts/Camera/CameraController.cs` - Advanced camera with effects and look-ahead

---

### Design Specification

**Tactical View**: 2D top-down with dynamic zoom (10m to 100km scale)
**Follow Mode**: Camera tracks player ship with smooth interpolation
**Strategic Mode**: Full map overview for theater-level planning
**Cinematic Mode**: Dynamic camera for dramatic combat moments (optional)

---

### Technical Implementation

#### **Current Implementation** ✅

**SimpleCameraController.cs** - Network-Aware Camera System
- **Auto-detects local player** in multiplayer (ignores remote players)
- **Smooth following** with configurable damping (default: 0.125f)
- **Look-ahead mode**: Camera leads ship based on velocity vector
- **Zoom system**: Mouse wheel control (min: 5, max: 50, default: 20)
- **Manual panning**: Middle mouse button for temporary camera control
- **Input locking**: Integrates with UI systems (menus disable camera input)

**Key Implementation Details**:
```csharp
// Camera Follow with Look-Ahead (SimpleCameraController.cs:178-192)
Vector3 targetPosition = currentTarget.position;

if (!isCenteredMode && lookAheadEnabled) {
    Vector2 velocity = targetRigidbody.velocity;
    if (velocity.magnitude > 0.1f) {
        targetPosition += (Vector3)(velocity.normalized * lookAheadDistance);
    }
}

Vector3 smoothedPosition = Vector3.Lerp(
    transform.position,
    new Vector3(targetPosition.x, targetPosition.y, transform.position.z),
    followSmoothing
);
```

**Zoom Implementation**:
```csharp
// Mouse Wheel Zoom (SimpleCameraController.cs:210-218)
float scroll = Mouse.current.scroll.ReadValue().y;
if (Mathf.Abs(scroll) > 0.01f) {
    targetZoom -= scroll * zoomSpeed * 0.01f;
    targetZoom = Mathf.Clamp(targetZoom, minZoom, maxZoom);
}
Camera.orthographicSize = Mathf.Lerp(
    Camera.orthographicSize,
    targetZoom,
    zoomSmoothing * Time.deltaTime
);
```

**Manual Panning**:
```csharp
// Middle Mouse Button Panning (SimpleCameraController.cs:230-245)
if (Mouse.current.middleButton.isPressed && !inputLocked) {
    Vector2 mouseDelta = Mouse.current.delta.ReadValue();
    Vector3 panDelta = new Vector3(
        -mouseDelta.x * panSpeed * Time.deltaTime,
        -mouseDelta.y * panSpeed * Time.deltaTime,
        0
    );
    manualPanOffset += panDelta;
    isManuallyPanning = true;
}
// Returns to follow mode after 2 seconds of inactivity
```

**Multiplayer Integration**:
```csharp
// Local Player Detection (SimpleCameraController.cs:98-112)
void FindLocalPlayer() {
    var players = FindObjectsOfType<NetworkedNavalController>();
    foreach (var player in players) {
        if (player.isLocalPlayer) {
            SetTarget(player.transform);
            return;
        }
    }
}
```

---

#### **CameraController.cs** - Advanced Features (Optional)
- **Camera shake effects** for explosions and weapon fire
- **Dynamic look-ahead** with velocity prediction
- **Pan-to-position** for tactical map integration
- **Camera status queries** for UI integration
- **ScriptableObject configuration** (CameraSettingsSO)

**Camera Shake Example**:
```csharp
// Trigger shake on explosion (CameraController.cs:245-260)
public void StartShake(float intensity, float duration) {
    shakeIntensity = intensity;
    shakeDuration = duration;
    isShaking = true;
}

// Shake calculation using Perlin noise
Vector3 shakeOffset = new Vector3(
    Mathf.PerlinNoise(Time.time * 10, 0) - 0.5f,
    Mathf.PerlinNoise(0, Time.time * 10) - 0.5f,
    0
) * shakeIntensity * shakeCurve.Evaluate(shakeTimer / shakeDuration);
```

---

#### **Camera Modes**

**Implemented** ✅:
1. **Tactical View (Default)** - 2D orthographic, zoom range 5-50 units
2. **Follow Mode** - Smooth tracking with damped spring interpolation
3. **Look-Ahead Mode** - Camera leads ship movement (toggle: C key)
4. **Manual Pan Mode** - Temporary camera control (middle mouse button)

**Planned** 📋:
5. **Strategic Mode** - Full map overview (requires minimap system)
6. **Cinematic Mode** - Dynamic camera angles (post-Phase 3)

---

### Configuration & Parameters

**Adjustable Settings** (SimpleCameraController.cs:30-45):
```csharp
[Header("Follow Behavior")]
[SerializeField] private float followSmoothing = 0.125f;      // Camera lag (0 = instant, 1 = very slow)
[SerializeField] private float lookAheadDistance = 5f;        // How far ahead to look
[SerializeField] private bool lookAheadEnabled = true;        // Enable velocity-based offset

[Header("Zoom Settings")]
[SerializeField] private float minZoom = 5f;                  // Maximum zoom in
[SerializeField] private float maxZoom = 50f;                 // Maximum zoom out
[SerializeField] private float defaultZoom = 20f;             // Starting zoom level
[SerializeField] private float zoomSpeed = 1f;                // Zoom sensitivity
[SerializeField] private float zoomSmoothing = 5f;            // Zoom transition speed

[Header("Manual Panning")]
[SerializeField] private float panSpeed = 10f;                // Pan speed multiplier
[SerializeField] private float returnToFollowDelay = 2f;      // Auto-return timer
```

---

### Performance Considerations

**Update Frequency**: Camera updates in `LateUpdate()` after all ship movement calculations
**Optimization**: Camera only follows local player in multiplayer (no wasted calculations)
**Memory**: Minimal allocations (Vector3 lerp operations are stack-allocated)
**Network**: Zero network traffic (camera is client-side only)

---

### Integration Points

**Dependencies**:
- **Unity Input System** - Mouse scroll and middle button detection
- **Mirror Networking** - Local player identification (NetworkIdentity)
- **UI System** - Input locking when menus open
- **Ship Controllers** - Target transform and velocity for look-ahead

**Used By**:
- All gameplay scenes (Main game scene, test scenes)
- Debug UI systems (camera status display)
- Future minimap system (camera bounds)

---

### Known Gaps & Technical Debt

**Design vs. Implementation Differences**:
- ⚠️ **Strategic Mode**: Designed but not implemented (requires minimap system in Phase 2)
- ⚠️ **Cinematic Mode**: Designed but not implemented (low priority, post-Phase 3)
- ⚠️ **Zoom Range**: Design says "10m to 100km" but implementation is 5-50 orthographic units
  - *Note: Orthographic size 50 ≈ 100m view width, not 100km. Needs clarification.*

**Missing Features**:
- No camera bounds/constraints (can pan infinitely)
- No camera shake dampening based on ship stability
- No smooth transitions when switching targets
- No saved camera preferences (zoom resets on scene load)

**Technical Improvements Needed**:
- Add camera shake to SimpleCameraController (currently only in CameraController)
- Add configurable key bindings for look-ahead toggle
- Add camera zoom presets (tactical/strategic/detail views)
- Add smooth zoom-to-target feature for contextual focus

---

### Testing Status

**Unit Tests**: ❌ None
**Manual Testing**: ✅ Passed
- Follow mode works correctly in single-player ✅
- Follow mode works correctly in multiplayer (local player only) ✅
- Zoom system responsive and smooth ✅
- Manual panning works and auto-returns ✅
- Look-ahead mode provides good game feel ✅

**Known Bugs**:
- None currently reported

---

### Developer Notes

#### **Adding Camera Shake to Your Scene**:
```csharp
// Option 1: Use SimpleCameraController (basic)
SimpleCameraController cam = Camera.main.GetComponent<SimpleCameraController>();
cam.SetCenteredMode(false); // Enable look-ahead

// Option 2: Use CameraController (advanced with shake)
CameraController advCam = Camera.main.GetComponent<CameraController>();
advCam.StartShake(0.5f, 1.0f); // intensity, duration
```

#### **Customizing Camera Behavior**:
1. Create `CameraSettingsSO` ScriptableObject asset
2. Configure desired parameters in Inspector
3. Assign to CameraController component
4. Camera automatically loads settings on Start()

#### **Multiplayer Considerations**:
- Camera ONLY follows local player (automatic detection)
- Remote players' cameras are independent
- No camera sync across network (intentional)
- Server doesn't run camera code (client-only)

#### **Future Enhancements** (Post-Phase 3):
- **Replay System**: Record camera movements for killcams
- **Spectator Mode**: Free-cam for observers
- **Battle Recorder**: Cinematic replay generation
- **Multi-Monitor**: Tactical view + strategic map simultaneously

---

### Cross-References

**Related GDD Sections**:
- Section 4.2 - Ship Physics & Controls (camera follows ship movement)
- Section 5.1 - UI/UX System (camera input locking for menus)
- Section 6.3 - Multiplayer Client Prediction (camera-ship synchronization)

**Related Scripts**:
- `SimpleNavalController.cs` - Ship movement that camera follows
- `NetworkedNavalController.cs` - Multiplayer ship movement
- `MenuManager.cs` - Locks camera input when menus open
- `ShipDebugUI.cs` - Displays camera status for debugging

**Asset Files**:
- `CameraSettingsSO.asset` - ScriptableObject configuration (if using CameraController)
- Main Camera prefab in game scene

---

### Changelog

**2025-01-XX**: SimpleCameraController implemented with multiplayer support
**2025-01-XX**: CameraController implemented with advanced features
**2025-01-XX**: Look-ahead mode added for better game feel
**[PENDING]**: Strategic mode awaiting minimap system
**[PENDING]**: Cinematic mode deferred to post-Phase 3

---
```

---

## 📊 Comparison Summary

### What the Enhancement Adds:

1. **✅ Implementation Status Badge** - Immediately know what's built
2. **📁 Script References** - Direct file paths to code
3. **💻 Code Examples** - Actual implementation snippets with line numbers
4. **⚙️ Technical Specifications** - Exact parameters and formulas
5. **🔗 Integration Points** - How it connects to other systems
6. **⚠️ Known Gaps** - Honest assessment of design vs. implementation
7. **🧪 Testing Status** - What's been validated
8. **📝 Developer Notes** - Practical usage examples
9. **🔄 Cross-References** - Links to related sections and scripts
10. **📅 Changelog** - Implementation timeline

### Benefits for Development:

- **Designer**: Can verify if vision matches implementation
- **Developer**: Has exact code location and usage examples
- **QA Tester**: Knows what to test and expected behavior
- **New Team Member**: Can understand system in 5 minutes
- **Project Manager**: Can track implementation progress

---

*This is the level of detail I would add to EVERY section of the GDD that has implemented code.*
