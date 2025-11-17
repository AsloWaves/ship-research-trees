---
tags: [implemented, phase1, core-gameplay, camera]
status: ✅ IMPLEMENTED
phase: Phase 1
priority: HIGH
last-updated: 2025-11-17
---

# Camera System

## Overview
Tactical 2D top-down camera system with smooth ship following, dynamic zoom, look-ahead mode, and multiplayer awareness. Designed for naval tactical gameplay with emphasis on situational awareness and control precision.

## Implementation Status
**Status**: ✅ **IMPLEMENTED** (Core features complete)
**Phase**: Phase 1 Complete
**Scripts**: [[SimpleCameraController]], [[CameraController]]
**Priority**: HIGH - Foundation for all gameplay

---

## Design Specification

### Camera Modes

#### Tactical View (Default) ✅
- **View**: 2D orthographic top-down perspective
- **Zoom Range**: 5-50 orthographic units (~10m to 100m view width)
- **Purpose**: Primary gameplay view for naval combat and navigation
- **Controls**: Mouse wheel zoom, always active

#### Follow Mode ✅
- **Behavior**: Camera tracks player ship with smooth interpolation
- **Smoothing**: Configurable damping (default: 0.125f for slight lag)
- **Purpose**: Provides stable view during ship movement
- **Auto-targeting**: Automatically finds local player in multiplayer

#### Look-Ahead Mode ✅
- **Behavior**: Camera leads ship movement based on velocity vector
- **Distance**: Configurable offset (default: 5 units ahead)
- **Purpose**: Improves situational awareness by showing where ship is going
- **Toggle**: C key (default), or can be permanently enabled
- **Feel**: Creates more dynamic, arcade-like camera movement

#### Manual Pan Mode ✅
- **Controls**: Middle mouse button drag
- **Behavior**: Temporarily override follow mode for tactical scouting
- **Auto-Return**: Returns to follow mode after 2 seconds of inactivity
- **Purpose**: Allows players to look around battlefield without moving ship

#### Strategic Mode 📋 PLANNED
- **View**: Full map overview for theater-level planning
- **Status**: Awaiting minimap system implementation (Phase 2)
- **Purpose**: Grand strategy view of entire operational area

#### Cinematic Mode 📋 PLANNED
- **View**: Dynamic camera angles for dramatic moments
- **Status**: Deferred to post-Phase 3 (low priority)
- **Purpose**: Replay system and killcam support

---

## Technical Implementation

### Primary Implementation: SimpleCameraController.cs
**File**: [[SimpleCameraController]]
**Type**: MonoBehaviour (requires Camera component)
**Network**: Client-side only, multiplayer-aware

#### Key Features
- **Auto-detects local player** in multiplayer environments
- **Smooth following** with configurable spring damping
- **Velocity-based look-ahead** for improved game feel
- **Mouse wheel zoom** with smooth transitions
- **Manual panning** with auto-return timer
- **Input locking integration** for UI systems (menus, chat, etc.)

#### Core Algorithm: Follow with Look-Ahead
The camera tracks the player ship's position with optional velocity prediction:

```
1. Get target ship position
2. If look-ahead enabled AND ship is moving:
   - Calculate velocity vector
   - Project camera ahead by (velocity.normalized × lookAheadDistance)
3. Smooth camera position using Lerp with followSmoothing factor
4. If manual panning active, add manual offset
5. If panning inactive for returnToFollowDelay seconds, reset offset
```

#### Configuration Parameters
```
Follow Behavior:
- followSmoothing: 0.125f (camera lag factor, 0 = instant, 1 = very slow)
- lookAheadDistance: 5f (units ahead of ship to look)
- lookAheadEnabled: true (enable velocity prediction)

Zoom Settings:
- minZoom: 5f (maximum zoom in)
- maxZoom: 50f (maximum zoom out)
- defaultZoom: 20f (starting zoom level)
- zoomSpeed: 1f (zoom sensitivity)
- zoomSmoothing: 5f (zoom transition speed)

Manual Panning:
- panSpeed: 10f (pan drag multiplier)
- returnToFollowDelay: 2f (seconds before auto-return)
```

---

### Advanced Implementation: CameraController.cs
**File**: [[CameraController]]
**Type**: MonoBehaviour with ScriptableObject configuration
**Purpose**: Extended features for advanced camera control

#### Additional Features
- **Camera shake effects** for explosions and weapon fire
- **Dynamic look-ahead** with advanced velocity prediction
- **Pan-to-position** API for tactical map integration
- **Camera status queries** for UI integration
- **ScriptableObject configuration** (CameraSettingsSO)
- **Naval physics integration** for dynamic effects

#### Camera Shake System
Triggered by combat events (explosions, hits, weapon fire):
```
Trigger: StartShake(intensity, duration)
Implementation: Perlin noise-based offset
Dampening: Animation curve for natural falloff
Result: Subtle screen shake that enhances combat feedback
```

---

## Integration Points

### Dependencies
- **Unity Input System** - Mouse input (scroll, middle button, delta)
- **Mirror Networking** - NetworkIdentity for local player detection
- **UI Systems** - Input locking (MenuManager, ChatManager)
- **Ship Controllers** - Target transform and velocity data

### Used By
- **All gameplay scenes** - Main game, test scenes
- **Debug UI** - [[ShipDebugUI]], [[ShipDebugUIManager]]
- **Future minimap system** - Camera bounds for tactical map
- **Future replay system** - Camera recording/playback

### API for Other Systems
```csharp
// Lock/unlock camera input for UI
SimpleCameraController.LockInput();   // Call when opening menu
SimpleCameraController.UnlockInput(); // Call when closing menu

// Toggle camera modes
SetCenteredMode(bool centered);       // Enable/disable look-ahead

// Query camera state
bool isFollowing = currentTarget != null;
bool isPanning = isManuallyPanning;
```

---

## Known Issues & Limitations

### Design vs. Implementation Gaps

**Zoom Range Mismatch** ⚠️
- **Design States**: "10m to 100km scale"
- **Implementation**: Orthographic size 5-50 units
- **Reality**: Max zoom ≈ 100m view width, NOT 100km
- **Impact**: Need to clarify if this is acceptable or requires adjustment

**Strategic Mode Missing** 📋
- Designed but not implemented
- Awaiting Phase 2 minimap system
- Low priority (tactical zoom covers most use cases)

**Cinematic Mode Missing** 📋
- Designed but deferred to post-Phase 3
- Requires replay/recording system
- Nice-to-have, not essential

### Technical Limitations

**No Camera Bounds**
- Camera can pan infinitely in any direction
- No world boundaries enforced
- Future: Add configurable constraints for map edges

**No Zoom Presets**
- Players must manually zoom each session
- No saved camera preferences
- Future: Add "Close/Medium/Far" preset hotkeys

**Limited Shake Integration**
- Shake only in CameraController, not SimpleCameraController
- Most gameplay uses SimpleCameraController
- Future: Merge shake system into primary controller

**No Smooth Target Transitions**
- If target ship changes, camera jumps
- Not currently an issue (player doesn't change ships)
- Future: Add smooth transition for spectator mode

---

## Performance Considerations

**Update Frequency**: LateUpdate() - runs after all ship physics
**CPU Cost**: Negligible (~0.1ms per frame)
**Memory**: Minimal (Vector3 lerp operations are stack-allocated)
**Network**: Zero bandwidth (camera is client-side only)
**Optimization**: Only follows local player (no wasted calculations on remote ships)

---

## Multiplayer Behavior

### Local Player Detection
```
On Start:
1. Find all NetworkedNavalController instances
2. Check each for isLocalPlayer flag
3. Automatically set first local player as camera target
4. Remote players are ignored (no camera tracking)
```

### Network Efficiency
- Camera does **not** sync across network
- Each client has independent camera
- Remote players' cameras are invisible to server
- Zero network messages related to camera

---

## User Experience

### Feel & Responsiveness
- **Smooth Following**: 0.125f damping provides slight lag that feels natural
- **Look-Ahead**: 5-unit offset improves player's sense of speed and direction
- **Zoom**: Smooth transitions prevent jarring camera changes
- **Manual Pan**: 2-second auto-return balances exploration with convenience

### Accessibility
- **Mouse Wheel Zoom**: Universal control scheme
- **Middle Mouse Pan**: Standard RTS/tactical game convention
- **Keyboard Toggle**: C key for look-ahead (optional, can be always-on)
- **No Motion Sickness**: 2D orthographic prevents 3D camera disorientation

---

## Testing

### Test Coverage
- ✅ Single-player ship following (tested)
- ✅ Multiplayer local player detection (tested)
- ✅ Zoom controls (tested)
- ✅ Manual panning (tested)
- ✅ Look-ahead mode (tested)
- ✅ Input locking for UI (tested)
- ⭕ Camera bounds/constraints (not implemented)
- ⭕ Zoom presets (not implemented)
- ⭕ Strategic mode (not implemented)

### Known Bugs
None currently reported.

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Add camera bounds/world constraints
- [ ] Implement zoom preset hotkeys (1/2/3 for close/medium/far)
- [ ] Add smooth transitions when changing targets
- [ ] Merge camera shake into SimpleCameraController

### Phase 3 Improvements
- [ ] Strategic mode (full map overview)
- [ ] Cinematic replay camera
- [ ] Multi-monitor support (tactical + strategic views)
- [ ] Saved camera preferences

---

## Cross-References

### Related GDD Sections
- [[Ship-Physics]] - Camera follows ship movement
- [[Ship-Controls]] - Ship movement affects camera look-ahead
- [[UI-Overview]] - Camera input locking for menus
- [[Network-Architecture]] - Multiplayer player detection

### Related Scripts
- [[SimpleNavalController]] - Ship movement source
- [[NetworkedNavalController]] - Multiplayer ship movement
- [[MenuManager]] - Locks camera when menus open
- [[ShipDebugUI]] - Displays camera status

### Related Assets
- CameraSettingsSO.asset - ScriptableObject config (if using CameraController)
- Main Camera prefab - Scene setup

---

## Changelog

- **2025-01-XX**: SimpleCameraController implemented
- **2025-01-XX**: CameraController implemented with advanced features
- **2025-01-XX**: Look-ahead mode added
- **2025-01-XX**: Multiplayer local player detection added
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Fully functional, no blockers
**Next Steps**: Phase 2 enhancements (camera bounds, zoom presets)
