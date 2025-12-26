---
tags: [script, scriptableobject, loading-screen, configuration, implemented]
script-type: ScriptableObject
namespace: WOS.ScriptableObjects
file-path: Assets/Scripts/ScriptableObjects/Configs/LoadingScreenConfigSO.cs
status: ✅ IMPLEMENTED
size: ~8 KB (294 lines)
feature-group: loading-screen
---

# LoadingScreenConfigSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.ScriptableObjects
**File**: `Assets/Scripts/ScriptableObjects/Configs/LoadingScreenConfigSO.cs`
**Size**: ~8 KB (294 lines)
**Create Menu**: `WOS/UI/Loading Screen Configuration`

---

## Purpose
Centralized configuration asset for all loading screen visual, timing, audio, and content settings.

This ScriptableObject allows designers to customize every aspect of the loading screen without modifying code:
- Background images and logos
- Spinner appearance and animation
- Loading tips content and timing
- Color schemes for all UI elements
- Audio settings for ambient music and SFX
- Footer text (version, copyright)

---

## Implements GDD Features
- [[UI-Overview]] - Loading screen customization
- [[Menu-System]] - Consistent visual theming

---

## Key Components

### Configuration Categories

#### Visual Settings
```
backgroundImages (Sprite[]): Background images for random selection
randomizeBackground (bool): Enable random background selection
backgroundCrossfadeDuration (float): Duration for crossfade transitions
gameLogo (Sprite): Game logo sprite
logoScale (float): Logo scale multiplier (0.5-2)
spinnerSprite (Sprite): Maritime-themed spinner (wheel, compass, anchor)
tipIcon (Sprite): Icon displayed next to tips
```

#### Spinner Configuration
```
spinnerRotationSpeed (float): Degrees per second (30-360)
enableSpinnerPulse (bool): Enable scale pulse animation
spinnerPulseAmount (float): Pulse scale range (0.05-0.3)
spinnerPulseSpeed (float): Pulse speed multiplier (0.5-3)
```

#### Color Settings
```
[Panel Colors]
panelBackgroundColor: Loading panel background
panelBorderColor: Panel border/frame

[Progress Bar Colors]
progressBarFillColor: Active progress fill
progressBarCompleteColor: Completed progress (100%)
progressBarBackgroundColor: Empty progress background
progressBarGlowColor: Optional glow effect

[Text Colors]
loadingTextColor: Main "Loading..." text
progressTextColor: Percentage text
tipTextColor: Loading tip text
footerTextColor: Version/copyright text
```

#### Loading Tips
```
loadingTips (string[]): Array of tip strings (15+ default)
tipDisplayDuration (float): Seconds per tip (3-15)
tipFadeDuration (float): Fade transition duration (0.1-1)
randomizeTips (bool): Random vs sequential order
avoidRepeatTips (bool): Prevent consecutive repeats
```

#### Timing Settings
```
fadeDuration (float): Screen fade duration (0.1-2s)
minimumLoadingTime (float): Minimum display time (0-2s)
completionDelay (float): Delay at 100% before hiding (0-1s)
```

#### Audio Settings
```
ambientMusic (AudioClip): Background music during loading
completionSound (AudioClip): Sound on load complete
fadeTransitionSound (AudioClip): Optional fade sound
ambientMusicVolume (float): Music volume (0-1)
sfxVolume (float): SFX volume (0-1)
fadeOutMusicOnComplete (bool): Fade music on completion
musicFadeOutDuration (float): Music fade duration (0.1-2s)
```

#### Footer Settings
```
versionFormat (string): Format string for version (default: "v{0}")
copyrightText (string): Copyright display text
showVersion (bool): Show/hide version
showCopyright (bool): Show/hide copyright
```

---

## Default Loading Tips

The default configuration includes 15 naval-themed tips:

**Naval Combat**:
- "Aim ahead of moving targets - shells take time to reach their destination."
- "Different shell types are effective against different armor. Choose wisely."
- "Torpedoes are devastating but slow - lead your target significantly."

**Ship Handling**:
- "Larger ships take longer to accelerate and turn. Plan your maneuvers early."
- "Use 'Dead Slow' speed for precise harbor maneuvering."
- "Your ship's turning radius decreases at lower speeds."

**Economy & Trading**:
- "Check commodity prices at different ports - profit margins vary."
- "Cargo weight affects your ship's speed and handling."
- "Rare goods fetch higher prices but carry greater risk."

**Multiplayer**:
- "Coordinate with allies using the chat system."
- "Stay aware of your surroundings - enemies can appear from any direction."
- "Ports offer safety - hostile players cannot attack you in harbors."

**General**:
- "Press ESC to access the main menu at any time."
- "Your progress is automatically saved when docking at ports."
- "Customize your ship's loadout at any shipyard."

---

## Public Methods

### Tip Helpers
- `GetRandomTip(int previousIndex = -1)` - Returns random tip, avoiding previous if enabled
- `GetTipAtIndex(int index)` - Returns specific tip (wraps around)

### Background Helpers
- `GetRandomBackground()` - Returns random background sprite

### Version Helpers
- `GetVersionString()` - Returns formatted version using `Application.version`

---

## Validation

The `OnValidate()` method ensures all values stay within valid ranges:
```csharp
fadeDuration = Mathf.Clamp(fadeDuration, 0.1f, 2f);
tipDisplayDuration = Mathf.Clamp(tipDisplayDuration, 2f, 30f);
tipFadeDuration = Mathf.Clamp(tipFadeDuration, 0.1f, tipDisplayDuration * 0.3f);
spinnerRotationSpeed = Mathf.Max(10f, spinnerRotationSpeed);
// ... etc
```

---

## Integration Points

### Used By
- [[LoadingScreenManager]] - Primary consumer
- [[LoadingTipsController]] - Tip configuration
- [[LoadingSpinnerController]] - Spinner configuration

### Dependencies
- None (pure data container)

---

## Example Usage

### Creating Configuration Asset
1. Right-click in Project window
2. Create → WOS → UI → Loading Screen Configuration
3. Configure in Inspector
4. Assign to LoadingScreenManager

### Runtime Configuration Change
```csharp
// Load different config for different scenes
var newConfig = Resources.Load<LoadingScreenConfigSO>("Configs/DarkLoadingConfig");
LoadingScreenManager.Instance.SetConfiguration(newConfig);
```

### Accessing Tips Programmatically
```csharp
var config = LoadingScreenManager.Instance.Configuration;
string tip = config.GetRandomTip();
Debug.Log($"Tip: {tip}");
```

---

## Related Files
- [[LoadingScreenManager]] - Primary consumer
- [[LoadingTipsController]] - Tips display
- [[LoadingSpinnerController]] - Spinner animation
- `Resources/LoadingScreen/` - Background images

---

## Asset Locations

### Default Config Location
```
Assets/Resources/Configs/LoadingScreenConfig.asset
```

### Background Images
```
Assets/Resources/LoadingScreen/
├── Background_01.png
├── Background_02.png
└── ...
```

---

## Testing Notes
- All fields have sensible defaults
- Missing sprites gracefully handled (disabled components)
- Missing audio clips safely ignored
- Validation prevents invalid ranges in Editor

---

## Changelog
- **2025-01**: Initial implementation with full configuration support
- **2025-01**: Added audio settings (ambient music, completion sound)
- **2025-01**: Added footer settings (version, copyright)
