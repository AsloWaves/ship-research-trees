# HarborExitManager

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/HarborExitManager.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 268 |
| **Status** | **⚠️ DEPRECATED - Use new port system instead** |
| **Architecture** | Harbor scene management with PlayerPrefs persistence |

## Deprecation Notice

```csharp
[Obsolete("Use WOS.Port.Core.PortTransitionManager and
          WOS.Port.Harbor.HarborSceneManager instead.
          This script uses PlayerPrefs which has been replaced by
          PortSceneStateHolder ScriptableObject.")]
```

### Migration Path

| Old System | New System |
|------------|------------|
| `HarborExitManager` | `WOS.Port.Harbor.HarborSceneManager` |
| `PlayerPrefs` persistence | `WOS.Port.Core.PortSceneStateHolder` (ScriptableObject) |
| Manual scene loading | `WOS.Port.Core.PortTransitionManager` |
| Exit zone detection | `WOS.Port.Harbor.ExitZoneController` |

## Purpose

Manages harbor scene and handles returning to main game world. Reads saved entry data from `PlayerPrefs` and provides exit functionality via UI button or keyboard shortcuts.

## Configuration

### Harbor Scene Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `exitHarborButton` | `Button` | - | UI button to exit harbor (optional) |
| `enableKeyboardExit` | `bool` | `true` | Enable R/ESC key shortcuts |
| `showDebugInfo` | `bool` | `true` | Display harbor entry information |

### Exit Transition

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `useAsyncLoading` | `bool` | `true` | Use async scene loading |
| `exitDelay` | `float` | `0.5f` | Delay before transition (for effects) |

### Saved Data (Read-Only)

| Field | Type | Description |
|-------|------|-------------|
| `savedEntryPosition` | `Vector3` | Position where ship docked |
| `savedEntryRotation` | `Vector3` | Rotation when ship docked |
| `savedPortID` | `string` | Port ScriptableObject name |
| `savedExitSceneName` | `string` | Main scene to return to |

## Key Features

### PlayerPrefs Data Loading

```csharp
// Reads saved port entry data
"PortEntry_Position"    → Entry position (JSON Vector3)
"PortEntry_Rotation"    → Entry rotation (JSON Quaternion)
"PortEntry_PortID"      → Port configuration ID
"PortEntry_ExitScene"   → Scene to return to
"PortEntry_PortCenter"  → Port center position (NEW)
"PortEntry_RelativeOffset" → Offset from port center (NEW)
```

### Exit Controls

| Key | Action | Availability |
|-----|--------|-------------|
| **R** | Exit Harbor | When `enableKeyboardExit = true` |
| **ESC** | Exit Harbor | When `enableKeyboardExit = true` |
| **Button Click** | Exit Harbor | If `exitHarborButton` assigned |

### Port-Relative Positioning

```csharp
// NEW SYSTEM: Uses port-relative offsets for multi-port support
Vector3 originalPortCenter = JsonUtility.FromJson<Vector3>(
    PlayerPrefs.GetString("PortEntry_PortCenter"));
Vector3 relativeOffset = JsonUtility.FromJson<Vector3>(
    PlayerPrefs.GetString("PortEntry_RelativeOffset"));

// Exit position = PortCenter + Offset
// Allows correct exit even if port moved in main scene
exitPosition = originalPortCenter + relativeOffset;
```

### 180° Rotation on Exit

```csharp
// Ship faces AWAY from port on exit
Quaternion entryRotation = Quaternion.Euler(savedEntryRotation);
Quaternion exitRotation = entryRotation * Quaternion.Euler(0, 180, 0);

// Ensures ship doesn't immediately re-enter docking zone
```

## Public API

### Exit Methods

#### `ExitHarbor()`
```csharp
public void ExitHarbor()
```

Main exit method. Prepares exit data with 180° rotation and triggers scene transition.

**Exit Sequence**:
1. Reads saved entry data from PlayerPrefs
2. Calculates exit position (port-relative or absolute)
3. Rotates 180° from entry direction
4. Saves exit data to PlayerPrefs
5. Loads main scene (async or direct)

#### `OnExitButtonClicked()`
```csharp
public void OnExitButtonClicked()
```

UI button callback. Calls `ExitHarbor()`.

#### `ExitToSpecificScene(string sceneName)`
```csharp
public void ExitToSpecificScene(string sceneName)
```

Override exit scene. Useful for testing or special transitions.

## Usage Examples

### Basic Setup

```csharp
// Harbor Scene Setup:
// 1. Create GameObject "HarborManager"
// 2. Add HarborExitManager component
// 3. Assign exitHarborButton (optional)
// 4. Enable enableKeyboardExit = true
// 5. Set showDebugInfo = true for testing
```

### Button Integration

```csharp
// UI Canvas Setup:
// 1. Add Button to Canvas
// 2. Assign to exitHarborButton in Inspector
// 3. Button automatically configured on Start
// 4. Click handler added: ExitHarbor()
```

### Expected Console Output

```
[HarborExitManager] Loading Harbor Data:
  Port: Pearl_Harbor_Tier3
  Exit Scene: Ocean
  Entry Position: (1234.5, 678.9, 0)
  Rotation: (0, 0, 45)

[User presses R or clicks button]

[HarborExitManager] Exiting harbor...
  Using port-relative exit: PortCenter=(1000, 500), Offset=(234.5, 178.9)
  Calculated exit position: (1234.5, 678.9)
  Exit rotation set to: (0, 0, 225) [180° rotated]
  Ship will be rotated 180° from entry direction
  Loading scene: Ocean
```

## Integration Points

### Scene Flow

```
SimplePortTest (Ocean Scene)
  ↓ Press E to enter harbor
  ↓ Saves entry data to PlayerPrefs
HarborExitManager (Harbor Scene)
  ↓ Loads entry data on Start
  ↓ Press R to exit
  ↓ Saves exit data to PlayerPrefs
ScenePortManager (Ocean Scene)
  ↓ Reads exit data
  ↓ Positions ship with 180° rotation
```

### Data Flow

```csharp
// SimplePortTest → PlayerPrefs (WRITE)
PlayerPrefs.SetString("PortEntry_Position", positionJson);
PlayerPrefs.SetString("PortEntry_PortCenter", portCenterJson);

// HarborExitManager → PlayerPrefs (READ & WRITE)
string posJson = PlayerPrefs.GetString("PortEntry_Position");
PlayerPrefs.SetString("PortExit_Position", exitPositionJson);
PlayerPrefs.SetInt("PortExit_Valid", 1);

// ScenePortManager → PlayerPrefs (READ & CLEANUP)
string exitPosJson = PlayerPrefs.GetString("PortExit_Position");
PlayerPrefs.DeleteKey("PortExit_Valid");
```

## Design Notes

### Fallback Behavior

```csharp
// If no exit scene saved
if (string.IsNullOrEmpty(savedExitSceneName))
{
    savedExitSceneName = "MainScene"; // Hardcoded fallback
}
```

### Exit Data Structure

```csharp
// Saved to PlayerPrefs for ScenePortManager
"PortExit_Position"  → Calculated exit position
"PortExit_Rotation"  → 180° rotated from entry
"PortExit_Throttle"  → 0f (ensure stopped)
"PortExit_Speed"     → 0f (ensure stopped)
"PortExit_Valid"     → 1 (flag for ScenePortManager)
```

### Async Loading

```csharp
// Optional async scene loading with progress
while (!asyncLoad.isDone)
{
    float progress = Mathf.Clamp01(asyncLoad.progress / 0.9f);
    DebugManager.Log(DebugCategory.System,
        $"Loading progress: {progress * 100}%", this);
    yield return null;
}
```

## Troubleshooting

### Issue: No exit scene data
**Solution**: Ensure SimplePortTest saved data before entering harbor

### Issue: Ship spawns at wrong position
**Solution**: Check ScenePortManager is in main scene and configured

### Issue: R key not working
**Solution**: Verify chat panel is closed (uses `ChatPanel.IsMenuOpen()` check)

### Issue: Wrong rotation on exit
**Solution**: Verify entry rotation was saved correctly by SimplePortTest

## Related Scripts

- **SimplePortTest**: Main scene port entry/docking (saves entry data)
- **ScenePortManager**: Main scene port return handler (reads exit data) [DEPRECATED]
- **PortTransitionManager**: NEW - Replacement for this system
- **PortSceneStateHolder**: NEW - ScriptableObject-based state persistence
