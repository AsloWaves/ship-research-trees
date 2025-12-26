# FrustumWarningSupressor

## Quick Reference

| File | Namespace | Inheritance | Lines | Architecture |
|------|-----------|-------------|-------|--------------|
| FrustumWarningSupressor.cs | WOS.Utilities | MonoBehaviour | 47 | Utility Component |

## Purpose

Suppresses the "Screen position out of view frustum" warnings that occur from Unity's internal `SendMouseEvents` system. This is a quality-of-life utility that filters out annoying console spam without affecting game functionality.

## Configuration

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| N/A | N/A | N/A | No configurable properties - works automatically |

## Implementation Strategy

The script uses two complementary approaches to suppress frustum warnings:

### 1. Camera Event Mask Approach
Disables the legacy mouse event system for the camera by setting the event mask to 0. This prevents `SendMouseEvents` from processing mouse events for the camera.

```csharp
private void Awake()
{
    Camera cam = GetComponent<Camera>();
    if (cam != null)
    {
        // Disable legacy event mask to prevent SendMouseEvents from processing
        cam.eventMask = 0;
        DebugManager.Log(DebugCategory.System,
            "Disabled legacy mouse events on camera to prevent frustum warnings", this);
    }
}
```

### 2. Log Filtering Approach
Filters debug logs to suppress the specific warning message from appearing in the console.

```csharp
private void HandleLog(string logString, string stackTrace, LogType type)
{
    // Suppress the specific frustum warning
    if (logString.Contains("Screen position out of view frustum"))
    {
        // Don't propagate this specific warning
        return;
    }
}
```

## Public API

This component has no public API - it works automatically when attached to a camera GameObject.

## Usage Example

```csharp
// Simply attach this component to your Main Camera GameObject
// No additional configuration or code required

// In Unity Editor:
// 1. Select Main Camera
// 2. Add Component > WOS > Utilities > Frustum Warning Supressor
// 3. Done! Warnings are automatically suppressed
```

## Integration Points

### Camera System
- **Requires**: Unity Camera component on the same GameObject
- **Modifies**: Camera.eventMask property (set to 0)
- **Integration**: Attach to Main Camera or any camera producing frustum warnings

### Debug System
- **Uses**: `WOS.Debugging.DebugManager` for logging suppression confirmation
- **Category**: System-level debug messages

## Design Notes

### Why This Is Needed
Unity's legacy `SendMouseEvents` system generates warnings when mouse positions are calculated outside the camera frustum. This commonly occurs during normal gameplay when UI elements or mouse tracking occurs near screen edges.

### Dual-Strategy Approach
1. **Prevention** (eventMask = 0): Stops the warning at the source by disabling legacy events
2. **Filtering** (log handler): Catches any warnings that slip through as a backup

### Performance Impact
- **Negligible**: Both approaches have minimal overhead
- **Event Mask**: Set once in Awake()
- **Log Handler**: Only processes logs when they occur (not every frame)

### Legacy System Compatibility
Disabling the camera event mask doesn't affect modern Input System functionality - only the deprecated mouse event system is disabled.

### Best Practices
- Place on Main Camera GameObject (preferably)
- Can be attached to any camera experiencing frustum warnings
- No configuration needed - works out of the box
- Does not interfere with gameplay or input systems

### Common Warning Scenarios
- Mouse cursor near screen edges
- UI elements positioned outside viewport
- Camera movement with rapid viewport changes
- Multi-monitor setups with cursor movement

### Alternative Solutions Considered
1. **Ignore Warnings**: Not ideal - clutters console
2. **Modify Unity Source**: Not practical for most projects
3. **Camera Clipping Adjustments**: Doesn't address root cause
4. **Custom Input System**: Overkill for a simple warning suppression

This utility provides a clean, non-invasive solution to a common Unity annoyance.
