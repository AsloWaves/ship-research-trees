# SimpleNavalController

## Quick Reference

| File | Namespace | Inheritance | Lines | Architecture |
|------|-----------|-------------|-------|--------------|
| SimpleNavalController.cs | WOS.Player | MonoBehaviour | 744 | **LEGACY** - Naval Physics Controller |

## ⚠️ LEGACY COMPONENT

**Status**: Archived / Deprecated
**Replaced By**: `NetworkedNavalController.cs`
**Reason**: This is the original client-only naval controller that was replaced by the networked version for multiplayer support.

## Purpose

Enhanced naval physics controller with authentic ship handling characteristics. Integrates Unity Input System with Job System optimization for performance. This was the original single-player naval controller before networking was implemented.

## Configuration

### Ship Configuration
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| shipConfig | ShipDefinitionSO | null | Ship configuration (displacement, speeds, turning) |
| enableDebugVisualization | bool | true | Show debug information and gizmos |
| globalSpeedMultiplier | float | 1.0 | Global speed multiplier (0.1-2.0) |

### Navigation Configuration
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| waypointContainer | Transform | null | Container for waypoint objects |
| waypointPrefab | GameObject | null | Prefab for waypoint visualization |
| courseLineRenderer | LineRenderer | null | Line renderer for course visualization |

## Core Architecture

### 8-Speed Throttle System

The controller implements an authentic naval throttle system:

```csharp
// Throttle Range: -4 to +4
// -4: Full Astern (100% reverse)
// -3: Half Astern (66% reverse)
// -2: Slow Astern (33% reverse)
// -1: Dead Slow Astern (15% reverse)
//  0: Full Stop
// +1: Slow Ahead (25% forward)
// +2: Half Ahead (50% forward)
// +3: Full Ahead (75% forward)
// +4: Flank Ahead (100% forward)

private float ConvertThrottleToSpeed(float throttle)
{
    int throttleInt = Mathf.RoundToInt(throttle);
    return throttleInt switch
    {
        -4 => -shipConfig.maxSpeed,           // Full Astern
        -3 => -shipConfig.maxSpeed * 0.66f,   // Half Astern
        -2 => -shipConfig.maxSpeed * 0.33f,   // Slow Astern
        -1 => -shipConfig.maxSpeed * 0.15f,   // Dead Slow Astern
        0 => 0f,                              // Full Stop
        1 => shipConfig.maxSpeed * 0.25f,     // Slow Ahead
        2 => shipConfig.maxSpeed * 0.50f,     // Half Ahead
        3 => shipConfig.maxSpeed * 0.75f,     // Full Ahead
        4 => shipConfig.maxSpeed,             // Flank Ahead
        _ => 0f
    };
}
```

### Rudder Physics System

Authentic rudder mechanics with speed-dependent effectiveness:

```csharp
// Rudder angle: -35° to +35°
// Effectiveness based on water flow over rudder
float propWashSpeed = 0.5f; // Minimum flow from propeller
float waterFlowSpeed = Mathf.Max(Mathf.Abs(currentSpeed), propWashSpeed);

// Steerageway effect (minimum 15% from prop wash)
float steerageEffect = Mathf.InverseLerp(0f, shipConfig.steerageway, waterFlowSpeed);
steerageEffect = Mathf.Max(steerageEffect, 0.15f);

effectiveRudderAngle = rudderAngle * steerageEffect;
```

### Scalable Momentum System

Physics system that accounts for ship characteristics:

```csharp
private float CalculateShipResponsiveness(Vector2 targetVelocity)
{
    // 1. Mass inertia (based on displacement)
    float normalizedMass = Mathf.Clamp01(shipConfig.displacement / 50000f);
    float massInertia = Mathf.Lerp(0.1f, 0.6f, normalizedMass);

    // 2. Speed change factor
    float velocityDelta = Mathf.Abs(targetVelocityMag - currentVelocityMag);
    float speedChangeFactor = Mathf.Clamp01(velocityDelta / 10f);

    // 3. Direction change factor
    float directionChange = (1f - Vector2.Dot(currentDir, targetDir)) * 0.5f;

    // 4. Ship design characteristics
    float lengthFactor = Mathf.Clamp01(shipConfig.length / 200f);
    float designResponsiveness = 1f - (lengthFactor * 0.3f);

    // 5. Water resistance (drag coefficient)
    float dragResponse = Mathf.Lerp(1.2f, 0.8f, shipConfig.dragCoefficient / 2f);

    // Combine all factors
    float totalInertia = massInertia + (speedChangeFactor * 0.4f) + (directionChange * 0.3f);
    totalInertia *= (2f - designResponsiveness);
    totalInertia /= dragResponse;

    return Mathf.Clamp(scaledResponseRate, minResponse, maxResponse);
}
```

### Waypoint Navigation System

```csharp
// Waypoint management using Unity.Mathematics.float3
private List<float3> waypoints;
private int currentWaypointIndex;
private bool autoNavigationEnabled;

// Navigation calculation
private void CalculateNavigationDirect(float3 currentPos, float3 targetDir)
{
    float currentHeading = transform.rotation.eulerAngles.z * Mathf.Deg2Rad;
    float targetHeading = Mathf.Atan2(targetDir.x, targetDir.z);
    float headingDifference = targetHeading - currentHeading;

    // Normalize to [-π, π]
    while (headingDifference > Mathf.PI) headingDifference -= 2f * Mathf.PI;
    while (headingDifference < -Mathf.PI) headingDifference += 2f * Mathf.PI;

    // Calculate steering input
    float steeringInput = headingDifference * shipConfig.helmResponse;
    autoSteeringInput = Mathf.Clamp(steeringInput, -1f, 1f);
}
```

## Input System Integration

### Action Map: "Naval"

| Action | Input | Description |
|--------|-------|-------------|
| Steering | A/D or Arrow Keys | Rudder control (-1 to +1) |
| ThrottleUp | W | Increase throttle setting |
| ThrottleDown | S | Decrease throttle setting |
| EmergencyStop | Space | Immediate full stop |
| SetWaypoint | Right Mouse | Place waypoint at mouse position |
| AutoNavigate | Z | Toggle autopilot mode |
| ClearWaypoints | X | Clear all waypoints |

### Event System

```csharp
// Global events for UI and system integration
public static Action<float> OnSpeedChanged;
public static Action<float> OnThrottleChanged;
public static Action<Vector3> OnWaypointAdded;
public static Action OnWaypointsCleared;
public static Action<bool> OnAutoNavigationToggled;

// Subscribe to events
SimpleNavalController.OnSpeedChanged += UpdateSpeedDisplay;
SimpleNavalController.OnThrottleChanged += UpdateThrottleIndicator;
```

## Public API

### Ship Status

| Method | Returns | Description |
|--------|---------|-------------|
| GetShipStatus() | ShipStatus | Complete ship status for UI |
| GetVelocity() | Vector3 | Current velocity vector |
| GetCurrentSpeed() | float | Current speed in m/s |
| GetThrottle() | float | Current throttle setting (-4 to +4) |
| GetShipConfiguration() | ShipDefinitionSO | Ship configuration reference |

### Control Methods

| Method | Parameters | Description |
|--------|------------|-------------|
| SetThrottle | float throttleValue | Set throttle directly (-4 to +4) |
| AddWaypoint | Vector3 position | Add waypoint programmatically |

### ShipStatus Structure

```csharp
[Serializable]
public struct ShipStatus
{
    public float speed;           // Current speed (m/s)
    public float throttle;        // Throttle setting (-4 to +4)
    public float heading;         // Ship heading (degrees)
    public float rudderAngle;     // Rudder angle (degrees)
    public bool isAutoNavigating; // Autopilot active
    public int waypointCount;     // Total waypoints
    public int currentWaypoint;   // Current waypoint index
}
```

## Events

### Speed and Throttle Events

```csharp
// Speed changed event
OnSpeedChanged?.Invoke(currentSpeed);

// Throttle changed event
OnThrottleChanged?.Invoke(currentThrottle);
```

### Navigation Events

```csharp
// Waypoint added
OnWaypointAdded?.Invoke(mouseWorldPos);

// Waypoints cleared
OnWaypointsCleared?.Invoke();

// Auto-navigation toggled
OnAutoNavigationToggled?.Invoke(autoNavigationEnabled);
```

## Usage Example

```csharp
// 1. Setup in scene
public class GameSetup : MonoBehaviour
{
    [SerializeField] private ShipDefinitionSO shipConfig;
    [SerializeField] private GameObject shipPrefab;

    void Start()
    {
        // Spawn ship with controller
        GameObject ship = Instantiate(shipPrefab);
        SimpleNavalController controller = ship.GetComponent<SimpleNavalController>();

        // Subscribe to events
        SimpleNavalController.OnSpeedChanged += UpdateSpeedUI;
        SimpleNavalController.OnThrottleChanged += UpdateThrottleUI;
    }
}

// 2. UI integration
public class ShipHUD : MonoBehaviour
{
    [SerializeField] private Text speedText;
    [SerializeField] private Text throttleText;

    void Start()
    {
        SimpleNavalController.OnSpeedChanged += OnSpeedChanged;
        SimpleNavalController.OnThrottleChanged += OnThrottleChanged;
    }

    private void OnSpeedChanged(float speed)
    {
        speedText.text = $"{speed:F1} m/s";
    }

    private void OnThrottleChanged(float throttle)
    {
        string throttleName = GetThrottleName(throttle);
        throttleText.text = throttleName;
    }
}

// 3. AI control example
public class AIController : MonoBehaviour
{
    private SimpleNavalController controller;

    void Start()
    {
        controller = GetComponent<SimpleNavalController>();

        // Set waypoints programmatically
        controller.AddWaypoint(new Vector3(100, 0, 100));
        controller.AddWaypoint(new Vector3(200, 0, 50));

        // Set speed
        controller.SetThrottle(2); // Half Ahead
    }
}
```

## Integration Points

### Input System
- **Requires**: Unity Input System package
- **Configuration**: `InputSystem_Actions.inputactions`
- **Action Map**: "Naval"
- **Player Input**: PlayerInput component required

### ShipDefinitionSO
- **Provides**: All ship physical characteristics
- **Properties Used**:
  - displacement (mass/inertia)
  - maxSpeed (knots)
  - acceleration/deceleration
  - maxRudderAngle
  - rudderRate (deg/sec)
  - steerageway (minimum speed for steering)
  - helmResponse (steering sensitivity)
  - dragCoefficient
  - length, beam (dimensions)

### Physics System
- **Rigidbody2D**:
  - gravityScale: 0 (no gravity in 2D naval game)
  - linearDamping: 0.5 (water resistance)
  - angularDamping: 2.0 (rotational resistance)
  - interpolation: Interpolate (smooth rendering)

### Debug System
- **Uses**: `WOS.Debugging.DebugManager`
- **Categories**: Ship, Physics, Input, Camera
- **Visualization**: Gizmos for ship bounds, turning circle, heading

## Design Notes

### Why This Was Replaced

1. **No Networking**: Client-only, not suitable for multiplayer
2. **No Authority**: Can't validate inputs server-side
3. **No Synchronization**: No SyncVars or RPCs for state sync
4. **Single Player Focus**: Designed before multiplayer requirements

### What Was Carried Forward to NetworkedNavalController

✅ **Kept**:
- 8-speed throttle system
- Rudder physics with steerageway
- Scalable momentum system
- Input System integration
- Debug visualization
- ShipDefinitionSO configuration

✅ **Added in Networked Version**:
- Server authority for physics
- SyncVar state synchronization
- ServerRpc / TargetRpc for commands
- Network prediction/reconciliation
- Multiplayer waypoint system

### Performance Optimizations

1. **Rigidbody2D Interpolation**: Prevents jitter between physics and render updates
2. **Component Caching**: All components cached in Awake()/Start()
3. **Event-Driven Input**: Only processes input when events fire
4. **Waypoint Pooling**: Reuses waypoint objects
5. **Conditional Debug**: Debug visualization only when enabled

### Physics Accuracy

The controller implements realistic naval physics:

- **Momentum**: Ships have significant inertia based on displacement
- **Steerageway**: Ships need water flow for rudder effectiveness
- **Prop Wash**: Minimum rudder effect even when stationary
- **Turning Circle**: Based on ship length and rudder angle
- **Acceleration Curves**: Different rates for acceleration vs deceleration

### Input Validation

```csharp
// Mouse position validation for waypoint placement
if (mouseScreenPos.x <= 0 || mouseScreenPos.y <= 0 ||
    mouseScreenPos.x >= Screen.width || mouseScreenPos.y >= Screen.height)
{
    // Invalid mouse position - skip waypoint
    return;
}
```

### Cleanup Strategy

```csharp
private void CleanupResources()
{
    // Clear waypoints
    waypoints?.Clear();

    // Unsubscribe from all input events
    throttleUpAction.performed -= OnThrottleUp;
    throttleDownAction.performed -= OnThrottleDown;
    // ... etc
}

private void OnDestroy() => CleanupResources();
private void OnDisable() => CleanupResources();
```

### Debug Visualization

```csharp
private void OnDrawGizmosSelected()
{
    // Ship dimensions (yellow)
    Gizmos.color = Color.yellow;
    Vector3 shipSize = new Vector3(shipConfig.beam, shipConfig.length, 1f);
    Gizmos.DrawWireCube(transform.position, shipSize);

    // Turning circle (cyan)
    Gizmos.color = Color.cyan;
    DrawWireCircle(transform.position, shipConfig.GetTurningRadius());

    // Center of mass (red)
    Gizmos.color = Color.red;
    Gizmos.DrawSphere(transform.position + centerOfMass, 0.5f);
}
```

### Migration Path

If you need to use this controller:

1. **Single Player Projects**: Can use as-is
2. **Multiplayer Projects**: Use `NetworkedNavalController` instead
3. **Hybrid Approach**: Reference code from this for physics logic
4. **Learning Reference**: Good example of Unity Input System integration

### Historical Context

This controller was the foundation for the current networked naval system. It proved the physics model and gameplay feel before networking was added. The code remains valuable as:
- Reference implementation
- Single-player mode template
- Physics algorithm documentation
- Input system example

### Best Practices Demonstrated

✅ **Input System**: Modern Input System (not legacy)
✅ **Component Caching**: Cache in Awake(), never in Update()
✅ **Event-Driven**: Static events for loose coupling
✅ **ScriptableObject Configuration**: All tunable parameters in SO
✅ **Physics Interpolation**: Smooth rendering independent of physics
✅ **Debug Visualization**: Comprehensive gizmos and debug logs
✅ **Resource Cleanup**: Proper cleanup in OnDestroy/OnDisable

This legacy controller serves as an excellent reference for Unity physics implementation and Input System usage.
