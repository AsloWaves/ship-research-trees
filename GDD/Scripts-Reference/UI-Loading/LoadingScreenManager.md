---
tags: [script, ui, loading-screen, scene-management, implemented]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: Assets/Scripts/UI/LoadingScreenManager.cs
status: ✅ IMPLEMENTED
size: 56 KB (~1713 lines)
feature-group: loading-screen
---

# LoadingScreenManager.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton, DontDestroyOnLoad)
**Namespace**: WOS.UI
**File**: `Assets/Scripts/UI/LoadingScreenManager.cs`
**Size**: ~56 KB (1713 lines)
**Dependencies**: LoadingScreenConfigSO, LoadingTipsController, LoadingSpinnerController, OceanChunkManager

---

## Purpose
Central manager for all loading screen functionality including fade transitions, progress tracking, and scene loading coordination.

This is the **core orchestrator** of the loading screen system. It handles:
- Fade to/from black transitions
- Progress bar updates with milestone-based animation
- Async scene loading with visual feedback
- Ocean chunk loading integration
- Coordination with tips and spinner controllers
- Audio playback during loading

---

## Implements GDD Features
- [[UI-Overview]] - Loading screen presentation
- [[Menu-System]] - Scene transition handling
- [[Ocean-Environment]] - Ocean chunk loading feedback

---

## Key Components

### Public Properties
```
Instance (static LoadingScreenManager): Singleton accessor with auto-creation
IsFading (bool): Whether a fade transition is active
IsLoadingVisible (bool): Whether loading panel is shown
IsLoading (bool): Whether a scene load operation is in progress
Configuration (LoadingScreenConfigSO): Current configuration asset
```

### Public Methods
- `FadeToBlack(Action onComplete)` - Fade screen to black
- `FadeFromBlack(Action onComplete)` - Fade screen from black to transparent
- `ShowLoadingScreen(string text)` - Display loading panel without fade
- `ShowLoadingScreenWithFade(string text, Action onComplete)` - Fade + show loading
- `HideLoadingScreen()` - Hide loading panel
- `HideLoadingScreenWithFade(Action onComplete)` - Hide + fade in
- `LoadSceneAsync(string sceneName, string message, Action onComplete)` - Full scene load with transitions
- `UpdateProgress(float progress)` - Update progress bar (0-1)
- `UpdateLoadingText(string text)` - Change loading message
- `StartSimulatedProgress()` - Begin milestone-based progress animation
- `SetProgressMilestone(float milestone)` - Set target progress (0-1)
- `CompleteProgress()` - Jump to 100% and stop
- `WaitForOceanChunks()` - Integrate with ocean chunk loading
- `ForceHideLoadingScreen()` - Immediate hide (emergency fallback)
- `SetConfiguration(LoadingScreenConfigSO config)` - Apply new config at runtime

### Events
```csharp
event Action OnFadeOutComplete;      // Fired when fade to black completes
event Action OnFadeInComplete;       // Fired when fade from black completes
event Action<float> OnLoadProgress;  // Fired on progress updates (0-1)
event Action OnLoadComplete;         // Fired when scene load finishes
```

---

## Configuration

### Inspector Fields
```
[Header("Fade Settings")]
fadeDuration (float, 0.5): Duration of fade transitions in seconds
fadeColor (Color, black): Color of the fade overlay

[Header("Loading Screen Settings")]
minimumLoadingTime (float, 0.5): Minimum display time (prevents flash)

[Header("UI References")]
loadingCanvas (Canvas): Parent canvas for loading UI
fadeOverlay (Image): Full-screen fade image
loadingPanel (GameObject): Main loading panel container
loadingText (TextMeshProUGUI): "Loading..." text
progressText (TextMeshProUGUI): "0%" text
progressBarFill (Image): Progress bar fill image

[Header("Extended UI (Optional)")]
backgroundImage (Image): Themed background artwork
backgroundImageAlt (Image): Secondary for crossfade
gameLogo (Image): Game logo display
versionText (TextMeshProUGUI): Version display
copyrightText (TextMeshProUGUI): Copyright display

[Header("Controllers (Optional)")]
tipsController (LoadingTipsController): Tips rotation controller
spinnerController (LoadingSpinnerController): Spinner animation controller

[Header("Audio (Optional)")]
musicSource (AudioSource): Background music player
sfxSource (AudioSource): Sound effects player

[Header("Configuration")]
config (LoadingScreenConfigSO): ScriptableObject configuration
```

### ScriptableObject Dependencies
- [[LoadingScreenConfigSO]] - Centralized configuration for all loading screen visuals and behavior

---

## Integration Points

### Dependencies (What This Needs)
- **UnityEngine.SceneManagement** - Async scene loading
- **TMPro** - TextMeshPro for UI text
- **OceanChunkManager** - For ocean loading progress events
- **DebugManager** - Logging system
- [[LoadingScreenConfigSO]] - Configuration data
- [[LoadingTipsController]] - Tips display coordination
- [[LoadingSpinnerController]] - Spinner animation coordination

### Used By (What Uses This)
- [[PortTransitionManager]] - Harbor/ocean scene transitions
- [[JoinMenuController]] - Server connection flow
- [[InGameMenuController]] - Scene navigation
- **HarborExitManager** - Harbor exit transitions
- **SimplePortTest** - Port transition testing

---

## Technical Details

### Performance Considerations
- Uses `Time.unscaledDeltaTime` for animations (works during pause)
- Coroutine-based transitions (minimal per-frame allocation)
- Auto-creates UI if not assigned (runtime safety)
- Canvas sorting order 1000 (always on top)

### Singleton Pattern
```csharp
// Thread-safe singleton with lazy creation
public static LoadingScreenManager Instance
{
    get
    {
        if (_instance == null)
        {
            _instance = FindFirstObjectByType<LoadingScreenManager>();
            if (_instance == null)
            {
                CreateInstance();
            }
        }
        return _instance;
    }
}
```

### Progress Bar System
Supports two progress bar modes:
1. **Filled Image**: Uses `fillAmount` (0-1)
2. **Anchor-Based**: Stretches via `anchorMax.x` (for sliced images)

---

## How It Works

### Initialization (Awake)
1. Singleton setup with `DontDestroyOnLoad`
2. `EnsureUISetup()` - Creates missing UI components
3. `ApplyConfiguration()` - Applies ScriptableObject settings
4. `HideImmediate()` - Ensures hidden at start

### Milestone-Based Progress
```
SetProgressMilestone(0.15)  → Discovery started
SetProgressMilestone(0.30)  → Server found
SetProgressMilestone(0.50)  → Connection established
SetProgressMilestone(0.70)  → Authenticating
SetProgressMilestone(0.90)  → Authentication complete
SetProgressMilestone(1.00)  → Ready
```

Progress animates smoothly toward each milestone, with speed proportional to distance.

### Ocean Chunk Integration
```csharp
WaitForOceanChunks()
  → SubscribeToOceanEvents()
  → WaitForOceanChunkManagerRoutine()
  → OnOceanLoadingProgress(float)  // Maps 0-1 to 50%-100%
  → OnOceanFullyLoaded()
  → CompleteOceanLoadingAndHide()
```

### Loading Flow Example
```
1. ShowLoadingScreenWithFade()
   ├─ FadeRoutine(0→1) - Fade to black
   ├─ ShowLoadingScreen() - Display loading UI
   │  ├─ SetRandomBackground() - Apply background
   │  ├─ StartTipsRotation() - Begin tip cycling
   │  ├─ StartSpinner() - Begin spinner animation
   │  └─ StartAmbientMusic() - Play background audio
   └─ StartSimulatedProgress() - Animate progress bar

2. During Loading
   ├─ SetProgressMilestone(0.15) - Discovery
   ├─ SetProgressMilestone(0.30) - Server found
   ├─ SetProgressMilestone(0.50) - Connected
   └─ WaitForOceanChunks() - Ocean loading

3. Complete and Hide
   ├─ CompleteProgress() - Set to 100%
   ├─ HideLoadingScreenWithFade()
   │  ├─ HideLoadingScreen() - Stop tips/spinner/music
   │  └─ FadeRoutine(1→0) - Fade from black
   └─ OnLoadComplete event
```

---

## Example Usage

### Basic Scene Load
```csharp
LoadingScreenManager.Instance.LoadSceneAsync(
    "GameScene",
    "Loading game...",
    () => Debug.Log("Scene loaded!")
);
```

### Custom Loading with Milestones
```csharp
var loader = LoadingScreenManager.Instance;

// Show loading screen
loader.ShowLoadingScreenWithFade("Connecting...");
loader.StartSimulatedProgress();

// Update milestones as operations complete
loader.SetProgressMilestone(0.25f);
yield return ConnectToServer();

loader.SetProgressMilestone(0.50f);
yield return Authenticate();

loader.SetProgressMilestone(0.75f);
yield return LoadPlayerData();

loader.SetProgressMilestone(1.0f);

// Hide when done
loader.HideLoadingScreenWithFade();
```

### Ocean Chunk Integration
```csharp
// After scene loads, wait for ocean
LoadingScreenManager.Instance.WaitForOceanChunks();
// Loading screen automatically hides when ocean fully loads
```

---

## Related Files
- [[LoadingScreenConfigSO]] - Configuration ScriptableObject
- [[LoadingTipsController]] - Tips rotation controller
- [[LoadingSpinnerController]] - Spinner animation controller
- [[PortTransitionManager]] - Scene transition coordinator
- [[OceanChunkManager]] - Ocean loading events
- [[JoinMenuController]] - Connection flow integration

---

## Testing Notes
- **Fallback UI**: Auto-creates UI if not assigned in Inspector
- **100% Progress Fallback**: If OnOceanFullyLoaded doesn't fire, fallback triggers after 1s at 100%
- **Safety Timeout**: 30s max wait for OceanChunkManager, 10s for ocean load completion
- **Force Hide**: `ForceHideLoadingScreen()` for emergency situations

### Edge Cases
- Multiple simultaneous load requests are ignored
- Destroyed during fade: Safety checks prevent null reference
- Missing canvas: Auto-creates entire default UI
- Missing progress bar: Logged warning, continues without

---

## Changelog
- **2024-12**: Initial implementation with basic fade and progress
- **2024-12**: Added milestone-based progress system
- **2024-12**: Added ocean chunk integration
- **2025-01**: Added enhanced features (tips, spinner, audio, backgrounds)
- **2025-01**: Added ForceHideLoadingScreen for fallback scenarios
