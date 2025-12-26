---
tags: [script, ui, loading-screen, animation, implemented]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: Assets/Scripts/UI/LoadingSpinnerController.cs
status: ✅ IMPLEMENTED
size: ~7 KB (270 lines)
feature-group: loading-screen
---

# LoadingSpinnerController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Assets/Scripts/UI/LoadingSpinnerController.cs`
**Size**: ~7 KB (270 lines)
**Dependencies**: LoadingScreenConfigSO

---

## Purpose
Controls an animated loading spinner with rotation and optional pulse effects for maritime-themed loading indicators.

Designed for ship wheel, compass rose, anchor, or similar maritime-themed spinners that provide visual feedback during loading operations.

---

## Implements GDD Features
- [[UI-Overview]] - Loading screen visual feedback
- [[Menu-System]] - Loading animation

---

## Key Components

### Public Properties
```
IsSpinning (bool): Whether spinner is currently animating
```

### Public Methods
- `StartSpinning()` - Start rotation and pulse animation
- `StopSpinning()` - Stop animation and hide
- `Show()` - Show spinner without animation (static display)
- `Hide()` - Hide spinner immediately
- `SetRotationSpeed(float speed)` - Change rotation speed at runtime
- `SetPulseEnabled(bool enabled)` - Toggle pulse animation
- `SetConfiguration(LoadingScreenConfigSO config)` - Apply new configuration
- `ApplyConfiguration()` - Reapply current configuration

---

## Configuration

### Inspector Fields
```
[Header("UI References")]
spinnerTransform (RectTransform): The transform to rotate
spinnerImage (Image): For sprite assignment
spinnerContainer (GameObject): Container for show/hide

[Header("Configuration")]
config (LoadingScreenConfigSO): Configuration ScriptableObject

[Header("Fallback Settings")]
fallbackRotationSpeed (float, 180): Degrees per second
fallbackEnablePulse (bool, true): Enable pulse animation
fallbackPulseAmount (float, 0.1): Pulse scale range
fallbackPulseSpeed (float, 1.5): Pulse speed multiplier
```

### From LoadingScreenConfigSO
```
spinnerSprite: Maritime-themed sprite
spinnerRotationSpeed: 30-360 degrees/second
enableSpinnerPulse: Toggle pulse effect
spinnerPulseAmount: 0.05-0.3 scale range
spinnerPulseSpeed: 0.5-3x speed
```

---

## Technical Details

### Animation System
Uses `Time.unscaledDeltaTime` so animation continues during pause.

**Rotation**:
```csharp
currentRotation += rotationSpeed * deltaTime;
spinnerTransform.localRotation = Quaternion.Euler(0f, 0f, -currentRotation);
```

**Pulse Effect**:
```csharp
float pulse = 1f + Mathf.Sin(Time.unscaledTime * pulseSpeed * Mathf.PI * 2f) * pulseAmount;
spinnerTransform.localScale = baseScale * pulse;
```

### Performance
- Single transform rotation per frame
- Optional scale animation
- No allocations in Update loop

---

## Integration Points

### Dependencies
- [[LoadingScreenConfigSO]] - Configuration data

### Used By
- [[LoadingScreenManager]] - Primary controller

---

## Example Usage

### Basic Control
```csharp
var spinner = GetComponent<LoadingSpinnerController>();

// Start spinning
spinner.StartSpinning();

// Change speed
spinner.SetRotationSpeed(360f); // Fast spin

// Disable pulse
spinner.SetPulseEnabled(false);

// Stop when done
spinner.StopSpinning();
```

### Runtime Configuration
```csharp
var newConfig = Resources.Load<LoadingScreenConfigSO>("FastSpinnerConfig");
spinner.SetConfiguration(newConfig);
spinner.StartSpinning();
```

---

## Editor Utilities

### Context Menu Options
- **Preview Spinner**: Rotate to 45 degrees for visual preview
- **Reset Spinner**: Reset rotation and scale to identity

```csharp
#if UNITY_EDITOR
[ContextMenu("Preview Spinner")]
private void PreviewSpinner()
{
    spinnerTransform.localRotation = Quaternion.Euler(0f, 0f, -45f);
}

[ContextMenu("Reset Spinner")]
private void ResetSpinner()
{
    spinnerTransform.localRotation = Quaternion.identity;
    spinnerTransform.localScale = Vector3.one;
}
#endif
```

---

## Related Files
- [[LoadingScreenManager]] - Parent controller
- [[LoadingScreenConfigSO]] - Configuration asset
- [[LoadingTipsController]] - Companion component

---

## Maritime Spinner Suggestions
- **Ship Wheel**: Classic naval theme, 8-spoke wheel
- **Compass Rose**: Navigation theme, 16-point rose
- **Anchor**: Simple anchor rotating
- **Propeller**: Mechanical theme, 3-4 blade
- **Radar Sweep**: Modern tech theme, sweeping line

---

## Testing Notes
- Starts hidden in Awake
- Fallback values used if no config assigned
- Scale reset on stop to prevent drift
- State properly reset on disable/destroy

---

## Changelog
- **2025-01**: Initial implementation with rotation and pulse
- **2025-01**: Added configuration ScriptableObject support
- **2025-01**: Added editor preview utilities
