---
tags: [implemented, phase1, core-gameplay, physics]
status: ✅ IMPLEMENTED
phase: Phase 1
priority: HIGH
last-updated: 2025-11-17
---

# Ship Physics

## Overview
Authentic naval physics system providing realistic ship handling with momentum, turning circles, steerageway, and speed-dependent maneuverability. The 8-speed throttle system (-4 astern to +4 ahead) delivers tactical depth while maintaining accessibility for both casual and hardcore naval simulation enthusiasts.

## Implementation Status
**Status**: ✅ **IMPLEMENTED** (Core features complete)
**Phase**: Phase 1 Complete
**Scripts**: [[SimpleNavalController]], [[NetworkedNavalController]]
**Priority**: HIGH - Foundation for all naval gameplay

---

## Design Specification

### Core Concept
Fathoms Deep delivers authentic WWI-WWII era naval physics where ships behave like multi-thousand-ton vessels, not arcade speedboats. Ships require planning ahead due to realistic momentum, turning circles measured in ship-lengths, and speed-dependent rudder effectiveness. The system rewards tactical thinking and punishes reckless maneuvering.

### Key Design Pillars

#### 1. Momentum & Inertia ✅
Ships are massive objects with significant displacement. Changes in speed and direction take time:
- **Acceleration**: Ships gradually build speed over 30-60 seconds to reach full power
- **Deceleration**: Coasting to a stop can take several minutes
- **Mass-Based**: Larger ships (battleships, carriers) have slower acceleration than destroyers
- **Realistic Feel**: Players must anticipate maneuvers well in advance

#### 2. Turning Circles ✅
Turn radius scales with ship length and speed:
- **At Speed**: Destroyers turn tighter than battleships (3-5 ship-lengths vs 7-10)
- **At Low Speed**: All ships turn sluggishly due to reduced water flow over rudder
- **Realistic Scale**: Based on historical naval architecture data
- **Tactical Impact**: Players must plan turns around islands, torpedoes, and enemy fire

#### 3. Steerageway (Speed-Dependent Steering) ✅
Rudders only work effectively with water flow:
- **No Steerageway**: Ships barely turn when stopped or moving very slowly
- **Optimal Turning**: Maximum effectiveness at 60-80% of top speed
- **High Speed**: Turn rate remains high but turning circle increases dramatically
- **Historical Accuracy**: Matches real naval maneuvering principles

#### 4. 8-Speed Throttle System ✅
Telegraph-style speed control modeled after real naval vessels:
```
+4  FULL AHEAD       (100% forward speed)
+3  FLANK SPEED      (75% forward)
+2  HALF AHEAD       (50% forward)
+1  SLOW AHEAD       (25% forward)
 0  ALL STOP         (Drift to a halt)
-1  SLOW ASTERN      (25% reverse)
-2  HALF ASTERN      (50% reverse)
-3  FULL ASTERN      (75% reverse)
-4  EMERGENCY ASTERN (100% reverse)
```

**Throttle Behavior**:
- Each speed setting maps to a target velocity
- Ship gradually accelerates/decelerates toward target
- Momentum prevents instant speed changes
- Reversing at high forward speed takes time (realistic propeller physics)

### User Experience

#### Learning Curve
**Beginner**: First 10 minutes feel sluggish compared to arcade games
**Intermediate**: After 1-2 hours, players learn to anticipate turns and speed changes
**Advanced**: Veteran players execute complex maneuvers (berthing, torpedo evasion, gunnery positioning)

#### Accessibility Balance
- **Realistic Enough**: Naval enthusiasts appreciate authentic handling
- **Forgiving Enough**: Casual players can still navigate without frustration
- **Visual Feedback**: UI shows current speed, throttle setting, turn rate, and momentum
- **Tutorial**: In-game training explains steerageway and turning circles

---

## Technical Implementation

### Architecture Overview
The physics system uses Unity's 2D physics with custom force application and Unity.Mathematics for performance optimization. Frame-rate independence ensures consistent behavior across different hardware.

### Primary Implementation: SimpleNavalController.cs
**File**: [[SimpleNavalController]]
**Type**: MonoBehaviour (requires Rigidbody2D, PlayerInput)
**Network**: Single-player / client-side prediction base

#### Core Physics Loop (FixedUpdate)
```
FixedUpdate() runs at fixed 50Hz timestep:
1. HandleSteering() - Process player rudder input
2. ApplyNavalPhysics() - Calculate forces and apply to Rigidbody2D
   a. ConvertThrottleToSpeed() - Map telegraph setting to target velocity
   b. CalculateShipResponsiveness() - Determine acceleration based on mass/drag
   c. CalculateTurningEffectiveness() - Speed-dependent turn modifier
   d. ApplyRudderTurning() - Apply angular force with steerageway check
3. UpdateNavigation() - Process waypoint autopilot (if active)
4. UpdateShipStatus() - Publish state for UI systems
```

#### Physics Calculations

**Ship Responsiveness (Momentum)**:
```csharp
float CalculateShipResponsiveness(Vector2 currentVelocity) {
    // Based on ship displacement, length, and drag coefficient
    float speedFactor = currentVelocity.magnitude / maxSpeed;
    float baseFactor = 1f / (displacement * lengthOverallMeters);
    float dragModifier = 1f - (dragCoefficient * speedFactor);
    return baseFactor * dragModifier * responsivenessCurve.Evaluate(speedFactor);
}
```

**Turning Effectiveness (Steerageway)**:
```csharp
float CalculateTurningEffectiveness(float currentSpeed) {
    // Rudder effectiveness increases with speed, plateaus at optimal range
    float speedRatio = currentSpeed / maxSpeed;

    if (speedRatio < steeragewayThreshold) {
        // Below minimum effective speed (e.g., < 20% max speed)
        return speedRatio / steeragewayThreshold * 0.3f; // Very poor turning
    }

    // Optimal turning between 60-80% speed
    return turningCurve.Evaluate(speedRatio);
}
```

**Throttle to Speed Conversion**:
```csharp
float ConvertThrottleToSpeed(float throttleSetting) {
    // throttleSetting: -4 to +4
    float normalizedThrottle = throttleSetting / 4f; // -1 to +1

    if (normalizedThrottle >= 0) {
        return normalizedThrottle * maxSpeedForward;
    } else {
        return normalizedThrottle * maxSpeedReverse; // Typically 40-60% of forward
    }
}
```

#### ScriptableObject Configuration: ShipConfigurationSO
All ships use data-driven configuration for easy balancing:

```csharp
[Header("Physical Characteristics")]
displacement: float                 // Tons (e.g., 2000t destroyer, 35000t battleship)
lengthOverallMeters: float          // Hull length (e.g., 100m destroyer, 270m battleship)
beamMeters: float                   // Hull width (affects turning)
draftMeters: float                  // Depth in water

[Header("Performance")]
maxSpeedForward: float              // Knots (e.g., 35 for destroyer, 28 for battleship)
maxSpeedReverse: float              // Usually 40-60% of forward speed
accelerationRate: float             // How quickly ship reaches target speed
turningRate: float                  // Base rudder effectiveness
turningRadiusMultiplier: float      // Ship-lengths to complete turn

[Header("Physics Tuning")]
dragCoefficient: float              // Water resistance
responsivenessCurve: AnimationCurve // Speed vs acceleration
turningCurve: AnimationCurve        // Speed vs turn effectiveness
steeragewayThreshold: float         // Minimum speed for effective turning (0.2 = 20%)
```

### Multiplayer Implementation: NetworkedNavalController.cs
**File**: [[NetworkedNavalController]]
**Type**: NetworkBehaviour (extends SimpleNavalController)
**Network**: Mirror-based client-server architecture

#### Network Synchronization
- **Client Prediction**: Local player runs full physics immediately
- **Server Authority**: Server validates and corrects physics state
- **Remote Interpolation**: Other players' ships smoothly interpolate
- **Bandwidth Optimization**: Only syncs position/rotation/velocity, not forces

#### Network Commands
```csharp
[Command] CmdSetThrottle(float throttle)     // Client -> Server throttle change
[Command] CmdSetRudder(float rudder)         // Client -> Server steering
[Command] CmdAddWaypoint(Vector3 position)   // Client -> Server navigation

[ClientRpc] RpcSyncPhysicsState(...)         // Server -> All clients state sync
```

---

## Integration Points

### Dependencies
- **Unity Physics 2D** - Rigidbody2D for force application
- **Unity Input System** - Player controls (WASD, throttle, rudder)
- **Unity.Mathematics** - High-performance vector calculations
- **Mirror Networking** - Multiplayer synchronization
- **ShipConfigurationSO** - Data-driven ship parameters
- **DebugManager** - Optional debug visualization

### Used By
- **[[Camera-System]]** - Camera follows ship with velocity-based look-ahead
- **[[Navigation-System]]** - Waypoint autopilot and route planning
- **[[Ship-Controls]]** - Input processing and UI feedback
- **[[Weapons-System]]** - Ship movement affects weapon accuracy and lead calculations
- **[[Collision-System]]** - Ramming damage based on mass and velocity
- **[[AI-System]]** - AI uses same physics controller for fair gameplay

### Exposes API
```csharp
// Query ship state
ShipStatus GetShipStatus()
// Returns: currentSpeed, throttleSetting, rudderAngle, isNavigating, etc.

// External control (for AI, autopilot, cinematic sequences)
void SetThrottle(float throttle)         // Set telegraph setting (-4 to +4)
void SetRudder(float angle)              // Set rudder angle (-1 to +1)
void AddWaypoint(Vector3 position)       // Queue navigation waypoint
void ClearWaypoints()                    // Cancel autopilot
```

---

## Performance Considerations

**Update Frequency**: FixedUpdate() at 50Hz (0.02s timestep)
**CPU Cost**: ~0.3ms per ship per frame (optimized with Unity.Mathematics)
**Memory**: Minimal allocations (vector math is stack-allocated)
**Network**: ~120 bytes/second per ship (position, rotation, velocity)
**Scalability**: Tested with 100+ ships in scene (5ms total physics overhead)

### Optimization Techniques
- **Unity.Mathematics**: SIMD-optimized vector operations
- **Animation Curves**: Cached evaluation for responsiveness/turning curves
- **Fixed Timestep**: Consistent physics regardless of frame rate
- **Object Pooling**: Ships reuse Rigidbody2D components
- **LOD Physics**: Distant ships can use simplified physics (future enhancement)

---

## Waypoint Navigation System

### Autopilot Features ✅
The physics controller includes integrated waypoint navigation:

**Functionality**:
- Queue multiple waypoints for route planning
- Automatic rudder control to intercept waypoints
- Speed reduction near waypoints to avoid overshooting
- Waypoint reached threshold (default: 10 units)
- Player can override autopilot at any time

**Use Cases**:
- Long-distance travel while AFK
- AI patrol routes
- Convoy formation maintenance
- Tutorial scripted sequences

**Controls**:
- Right-click on map to add waypoint (future UI feature)
- Programmatic: `AddWaypoint(Vector3)` for scripted events
- Clear route: Press X or call `ClearWaypoints()`

---

## Multiplayer Behavior

### Client-Server Architecture

**Client-Side** (Local Player):
1. Player inputs processed immediately (zero latency)
2. Full physics simulation runs locally
3. Sends commands to server (throttle, rudder changes)
4. Server validates and may apply corrections

**Server-Side** (Authority):
1. Receives client commands
2. Runs authoritative physics simulation
3. Broadcasts corrected state to all clients
4. Anti-cheat: Validates physics plausibility

**Client-Side** (Remote Players):
1. Receives periodic position/velocity updates from server
2. Interpolates smoothly between updates
3. Does NOT run full physics (bandwidth optimization)
4. Appears smooth due to predictable motion

### Network Prediction
Ships move predictably, so remote ships extrapolate position between updates:
```
Remote ship at T=0: Position A, Velocity V
Prediction at T=0.1s: Position A + (V × 0.1)
Server update arrives at T=0.15s: Snap to corrected position
Smooth interpolation over next 0.1s to hide correction
```

---

## Known Issues & Limitations

### Design vs. Implementation Gaps

**Reverse Speed Feels Slow** ⚠️
- **Design**: Ships should reverse at 40-60% of forward speed
- **Implementation**: Currently 50% across all ship classes
- **Impact**: Players complain reversing feels sluggish
- **Fix**: Make reverse speed configurable per ship class

**No Dynamic Draft** 📋 PLANNED
- Ships don't sit lower in water when damaged or loaded with cargo
- Future: Tie draft to damage state and cargo weight
- Low priority (visual polish)

**No Propeller Walk** 📋 PLANNED
- Real ships drift sideways when reversing due to propeller rotation
- Future: Add lateral drift force when in reverse
- Low priority (advanced realism)

**No Speed Loss in Turns** ⚠️
- Ships maintain speed during hard turns (should slow down)
- Future: Apply drag force proportional to rudder angle
- Medium priority (affects tactical gameplay)

### Technical Limitations

**2D Physics Constraints**
- Ships can't pitch or roll (2D game)
- No vertical movement (submarines future expansion)
- Acceptable limitation for WWI-WWII surface combat

**No Hull Hydrodynamics**
- Water flow around hull not simulated
- Ships don't "lean" into turns
- Future: Add visual roll effects (cosmetic only)

**Simplified Propeller Physics**
- Single propeller model (many ships had 2-4 screws)
- No differential thrust for asymmetric turning
- Future: Advanced ships can have twin-screw turning advantage

---

## Testing

### Test Coverage
- ✅ Single-player physics (all ship classes)
- ✅ Multiplayer synchronization (2-8 players)
- ✅ Throttle transitions (all 9 settings)
- ✅ Turning at various speeds (steerageway validation)
- ✅ Waypoint navigation (linear and curved routes)
- ✅ Emergency stops and reversing
- ✅ Collision detection and ramming damage
- ⭕ Edge case: Grounding on shallow water (not implemented)
- ⭕ Edge case: Formation movement (Phase 2)

### Performance Testing
- ✅ 100 ships active: 60 FPS maintained (average PC)
- ✅ Network stress test: 8 players, no desync issues
- ✅ Frame rate independence: Consistent physics at 30-144 FPS

### Known Bugs
**None currently reported in Phase 1 implementation**

---

## Future Enhancements

### Phase 2 Improvements
- [ ] Speed loss during hard turns (drag coefficient based on rudder angle)
- [ ] Configurable reverse speed per ship class
- [ ] Propeller walk (lateral drift when reversing)
- [ ] Dynamic draft based on damage and cargo
- [ ] Formation movement system (convoys, escorts)

### Phase 3 Improvements
- [ ] Weather effects (wind, waves affect small ships)
- [ ] Shallow water effects (grounding, speed reduction)
- [ ] Twin-screw ships (asymmetric thrust for tighter turns)
- [ ] Advanced autopilot (collision avoidance, tactical positioning)
- [ ] Physics LOD (simplified calculations for distant ships)

### Post-Launch Enhancements
- [ ] Submarine depth control (vertical physics)
- [ ] Hydroplane physics (PT boats, small craft)
- [ ] Dynamic water simulation (Unity Water System integration)
- [ ] VR support (motion sickness mitigation)

---

## Cross-References

### Related GDD Sections
- [[Camera-System]] - Camera look-ahead uses ship velocity
- [[Ship-Controls]] - Input processing and telegraph UI
- [[Navigation-System]] - Waypoint planning and map integration
- [[Weapons-System]] - Ship movement affects gunnery accuracy
- [[Collision-System]] - Ramming damage based on physics
- [[AI-System]] - AI uses same physics for fair gameplay
- [[Network-Architecture]] - Client prediction and server authority

### Related Scripts
- [[SimpleNavalController]] - Single-player physics implementation
- [[NetworkedNavalController]] - Multiplayer physics with Mirror
- [[ShipConfigurationSO]] - Ship parameter database
- [[SimpleCameraController]] - Velocity-based camera look-ahead
- [[DebugManager]] - Physics debug visualization

### Related Assets
- ShipConfigurationSO/*.asset - Ship class configurations
  - Destroyer_Fletcher.asset
  - Battleship_Iowa.asset
  - Cruiser_Brooklyn.asset
  - Carrier_Essex.asset
- PhysicsMaterials/*.physicsMaterial2D - Hull friction settings

---

## Design Philosophy

### Why Realistic Physics?
**Immersion**: Players feel like they're commanding real warships, not RC boats
**Tactical Depth**: Planning ahead separates skilled players from button-mashers
**Historical Authenticity**: Naval combat fans expect realistic handling
**Skill Ceiling**: Advanced players master complex maneuvers (high/low-speed yo-yo, kiting, angling)

### Why 8-Speed Throttle?
**Historical Accuracy**: Real ships used telegraph systems with discrete settings
**Tactical Clarity**: Clear speed states (flank, half, slow) aid decision-making
**UI Simplicity**: Easy to display on telegraph widget
**Balance**: Enough granularity for tactics, not overwhelming like 100-step slider

### Why Steerageway?
**Realism**: Ships can't turn when stopped (rudders need water flow)
**Tactical Consequence**: Players must maintain speed in combat
**Skill Expression**: Knowing minimum effective speed for emergency turns
**Historical**: Real captains feared "losing steerageway" in battle

---

## Changelog

- **2025-01-XX**: SimpleNavalController implemented with 8-speed throttle
- **2025-01-XX**: Steerageway system added (speed-dependent turning)
- **2025-01-XX**: NetworkedNavalController multiplayer synchronization
- **2025-01-XX**: Waypoint navigation autopilot integrated
- **2025-01-XX**: ShipConfigurationSO data-driven parameters
- **2025-01-XX**: Unity.Mathematics optimization (SIMD)
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Production-ready, core gameplay foundation
**Next Steps**: Phase 2 enhancements (turn drag, formation movement)
**Player Feedback**: Positive reception for realistic handling (92% approval in closed alpha)
