---
tags: [script, ui, loading-screen, tips, implemented]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: Assets/Scripts/UI/LoadingTipsController.cs
status: ✅ IMPLEMENTED
size: ~9 KB (335 lines)
feature-group: loading-screen
---

# LoadingTipsController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Assets/Scripts/UI/LoadingTipsController.cs`
**Size**: ~9 KB (335 lines)
**Dependencies**: LoadingScreenConfigSO, TMPro

---

## Purpose
Controls the rotating display of loading tips with fade transitions during loading screens.

Provides educational and helpful tips to players while loading, with configurable timing, fade effects, and randomization options.

---

## Implements GDD Features
- [[UI-Overview]] - Loading screen content
- [[Menu-System]] - Player education during loading

---

## Key Components

### Public Properties
```
IsRunning (bool): Whether tip rotation is active
```

### Public Methods
- `StartTipRotation()` - Begin cycling through tips
- `StopTipRotation()` - Stop cycling and hide
- `SetTip(string tip)` - Display specific tip immediately
- `Show()` - Show panel without starting rotation
- `Hide()` - Hide panel immediately
- `SetConfiguration(LoadingScreenConfigSO config)` - Apply new configuration
- `ApplyConfiguration()` - Reapply current configuration

---

## Configuration

### Inspector Fields
```
[Header("UI References")]
tipText (TextMeshProUGUI): Text component for tips
tipIcon (Image): Icon displayed next to tips
tipsPanel (GameObject): Container for show/hide

[Header("Configuration")]
config (LoadingScreenConfigSO): Configuration ScriptableObject

[Header("Fallback Settings")]
fallbackDisplayDuration (float, 6): Seconds per tip
fallbackFadeDuration (float, 0.4): Fade transition duration
```

### From LoadingScreenConfigSO
```
loadingTips (string[]): Array of tip strings
tipDisplayDuration (float): 3-15 seconds per tip
tipFadeDuration (float): 0.1-1 second fade
tipTextColor (Color): Text color
tipIcon (Sprite): Icon sprite
randomizeTips (bool): Random vs sequential
avoidRepeatTips (bool): Prevent consecutive repeats
```

---

## Technical Details

### Tip Rotation Flow
```
StartTipRotation()
  └─ TipRotationRoutine()
       ├─ ShowNextTip() - Display first tip immediately
       └─ Loop:
            ├─ WaitForSecondsRealtime(displayDuration)
            ├─ FadeTipText(1 → 0) - Fade out
            ├─ ShowNextTip() - Switch content
            └─ FadeTipText(0 → 1) - Fade in
```

### Fade Animation
```csharp
private IEnumerator FadeTipText(float startAlpha, float endAlpha)
{
    float elapsed = 0f;
    while (elapsed < fadeDuration)
    {
        elapsed += Time.unscaledDeltaTime;
        float alpha = Mathf.Lerp(startAlpha, endAlpha, elapsed / fadeDuration);

        tipText.color = new Color(tipColor.r, tipColor.g, tipColor.b, alpha);
        tipIcon.color = new Color(iconColor.r, iconColor.g, iconColor.b, alpha);

        yield return null;
    }
}
```

### Tip Selection
```csharp
// Random mode (avoids previous tip)
if (config.randomizeTips)
{
    tipContent = config.GetRandomTip(lastTipIndex);
}
// Sequential mode
else
{
    currentTipIndex = (currentTipIndex + 1) % config.loadingTips.Length;
    tipContent = config.GetTipAtIndex(currentTipIndex);
}
```

### Performance
- Uses `WaitForSecondsRealtime` (works during pause)
- Single coroutine for entire rotation
- Minimal per-frame allocations during fade

---

## Integration Points

### Dependencies
- [[LoadingScreenConfigSO]] - Tip content and configuration
- **TMPro** - TextMeshPro for text rendering

### Used By
- [[LoadingScreenManager]] - Primary controller

---

## Example Usage

### Basic Control
```csharp
var tips = GetComponent<LoadingTipsController>();

// Start automatic rotation
tips.StartTipRotation();

// Or set specific tip
tips.SetTip("Custom loading message here...");

// Stop when done
tips.StopTipRotation();
```

### Runtime Configuration
```csharp
var newConfig = Resources.Load<LoadingScreenConfigSO>("QuickTipsConfig");
tips.SetConfiguration(newConfig);
tips.StartTipRotation();
```

---

## Tip Content Guidelines

### Recommended Categories
1. **Combat Tips**: Aiming, weapons, tactics
2. **Ship Handling**: Speed, turning, docking
3. **Economy**: Trading, cargo, profit
4. **Multiplayer**: Chat, coordination, safety
5. **Controls**: Key bindings, shortcuts
6. **General**: Game mechanics, features

### Writing Tips
- Keep tips concise (under 100 characters ideal)
- Use active voice ("Press ESC" not "ESC can be pressed")
- Be specific and actionable
- Avoid spoilers for new players
- Include tips for all skill levels

---

## Related Files
- [[LoadingScreenManager]] - Parent controller
- [[LoadingScreenConfigSO]] - Configuration and tip content
- [[LoadingSpinnerController]] - Companion component

---

## Testing Notes
- Starts hidden in Awake
- Fallback values used if no config assigned
- First tip shown immediately (no initial fade-in delay)
- Properly stops on disable/destroy

### Edge Cases
- Empty tips array: Shows "Loading..." fallback
- Single tip: Displays without rotation
- Rapid start/stop: Coroutine properly cancelled

---

## Changelog
- **2025-01**: Initial implementation with fade transitions
- **2025-01**: Added configuration ScriptableObject support
- **2025-01**: Added icon fade alongside text
