# GameObjectLifecycleMonitor

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Debugging/GameObjectLifecycleMonitor.cs` |
| **Namespace** | `WOS.Debugging` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 307 |
| **Architecture** | GameObject lifecycle tracking across scene changes |

## Purpose

Monitors GameObject lifecycle across scene transitions. Tracks which GameObjects are destroyed or disabled during scene changes. **CRITICAL** for diagnosing DontDestroyOnLoad issues, scene transition bugs, and unexpected object destruction.

## Configuration

### Monitoring Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enableMonitoring` | `bool` | `true` | Enable lifecycle monitoring |
| `logAllGameObjectsBeforeSceneChange` | `bool` | `false` | Log ALL GameObjects before scene change (verbose) |
| `onlyTrackDontDestroyOnLoad` | `bool` | `false` | Only track GameObjects with DontDestroyOnLoad |
| `verboseLogging` | `bool` | `true` | Show detailed logs for each GameObject |

### Filters

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `ignoreUnityInternals` | `bool` | `true` | Ignore Unity internal GameObjects (EventSystem, etc.) |

## Key Features

### Scene Transition Tracking

```csharp
// Captures snapshots on scene unload
OnSceneUnloaded → CaptureGameObjectSnapshot()

// Analyzes changes on scene load
OnSceneLoaded → AnalyzeGameObjectChanges()
```

### GameObject Snapshot System

```csharp
// Snapshot includes:
- name (GameObject name)
- instanceId (unique Unity ID)
- wasActive (hierarchy active state)
- sceneName (scene name or "DontDestroyOnLoad")
- parentName (parent object or "<root>")
- hasDontDestroyOnLoad (DontDestroyOnLoad flag)
```

### Change Detection

Detects three types of changes:
1. **Destroyed**: GameObject no longer exists
2. **Disabled**: GameObject exists but became inactive
3. **Survived**: GameObject still exists and active

## Public API

### Context Menu Methods

#### `ManualCaptureSnapshot()`
```csharp
[ContextMenu("Capture Snapshot Now")]
public void ManualCaptureSnapshot()
```

Manually trigger snapshot capture. Useful for testing or debugging at specific moments.

#### `ManualAnalyzeChanges()`
```csharp
[ContextMenu("Analyze Changes Now")]
public void ManualAnalyzeChanges()
```

Manually analyze changes from last snapshot. Useful for testing without scene transitions.

## Usage Examples

### Basic Setup

```csharp
// 1. Create GameObject "LifecycleMonitor"
// 2. Add GameObjectLifecycleMonitor component
// 3. Set enableMonitoring = true
// 4. Set verboseLogging = true
// 5. Enable ignoreUnityInternals = true
// 6. Press Play and change scenes
```

### Tracking DontDestroyOnLoad Issues

```csharp
// Setup:
// 1. Set onlyTrackDontDestroyOnLoad = true
// 2. Set verboseLogging = true
// 3. Change scenes
// 4. Check console for destroyed DontDestroyOnLoad objects

// Example Output:
[LifecycleMonitor] ❌ DESTROYED: NetworkManager
  (scene: DontDestroyOnLoad, parent: <root>, active: True)
```

### Finding Missing Objects

```csharp
// Setup:
// 1. Set logAllGameObjectsBeforeSceneChange = true
// 2. Capture snapshot before scene change
// 3. Load new scene
// 4. Analyze which objects were destroyed

// Useful for:
// - Missing UI elements
// - Lost manager references
// - Unexpected object destruction
```

### Console Output Example

```
═══════════════════════════════════════════════════════
[LifecycleMonitor] Scene LOADED: PortHarbor (Additive)
[LifecycleMonitor] Transition: Ocean → PortHarbor
═══════════════════════════════════════════════════════

[LifecycleMonitor] Analyzing changes from snapshot of 45 GameObjects...

[LifecycleMonitor] ✅ SURVIVED: DebugManager (scene: DontDestroyOnLoad)
[LifecycleMonitor] ✅ SURVIVED: NetworkManager (scene: DontDestroyOnLoad)
[LifecycleMonitor] ❌ DESTROYED: PlayerShip (scene: Ocean, parent: <root>, active: True)
[LifecycleMonitor] ⚠️ DISABLED: UICanvas (scene: DontDestroyOnLoad)

═══════════════════════════════════════════════════════
[LifecycleMonitor] SUMMARY:
[LifecycleMonitor] ✅ Survived:  35
[LifecycleMonitor] ⚠️  Disabled:  2
[LifecycleMonitor] ❌ Destroyed: 8
═══════════════════════════════════════════════════════
```

## Integration Points

### Scene Management

```csharp
// Subscribes to Unity scene events
SceneManager.sceneLoaded += OnSceneLoaded;
SceneManager.sceneUnloaded += OnSceneUnloaded;
```

### DebugManager Integration

```csharp
// All logging uses DebugCategory.System
DebugManager.Log(DebugCategory.System,
    "[LifecycleMonitor] GameObject lifecycle monitoring initialized", this);
```

## Design Notes

### DontDestroyOnLoad Requirement

```csharp
// CRITICAL: Monitor must survive scene changes
if (transform.parent != null)
{
    DebugManager.Log(DebugCategory.System,
        "[LifecycleMonitor] GameObject is NOT root - moving to root", this);
    transform.SetParent(null);
}
DontDestroyOnLoad(gameObject);
```

### Unity Internal Filtering

```csharp
// Ignored objects (when ignoreUnityInternals = true):
- EventSystem
- StandaloneInputModule
- InputSystemUIInputModule
- Main Camera (default Unity camera)
- Directional Light (default light)
- Canvas (default UI canvas)
```

### Instance ID Tracking

```csharp
// Uses Unity GetInstanceID() for reliable object tracking
int instanceId = gameObject.GetInstanceID();

// Survives scene changes, unique per object instance
// More reliable than object name or reference equality
```

### Snapshot Timing

```csharp
// Snapshot BEFORE scene unload
OnSceneUnloaded(Scene scene)
{
    CaptureGameObjectSnapshot();
}

// Analysis AFTER scene load
OnSceneLoaded(Scene scene, LoadSceneMode mode)
{
    AnalyzeGameObjectChanges();
}
```

## Data Structures

### GameObjectSnapshot

```csharp
public class GameObjectSnapshot
{
    public string name;              // GameObject name
    public int instanceId;           // Unity instance ID
    public bool wasActive;           // Active in hierarchy
    public string sceneName;         // Scene name
    public string parentName;        // Parent name or "<root>"
    public bool hasDontDestroyOnLoad; // In DontDestroyOnLoad scene

    public override string ToString()
    {
        string tag = hasDontDestroyOnLoad ? " [DontDestroyOnLoad]" : "";
        return $"{name} (scene: {sceneName}, parent: {parentName},
                 active: {wasActive}){tag}";
    }
}
```

## Use Cases

### Diagnosing Scene Transition Issues

**Problem**: Objects missing after scene change
**Solution**:
1. Enable monitoring
2. Set `verboseLogging = true`
3. Change scenes
4. Check console for destroyed objects
5. Identify cause (expected destruction or bug)

### Tracking DontDestroyOnLoad Persistence

**Problem**: Manager objects not persisting
**Solution**:
1. Set `onlyTrackDontDestroyOnLoad = true`
2. Change scenes
3. Check if DontDestroyOnLoad objects survived
4. Verify they're in DontDestroyOnLoad scene

### Finding Rogue Object Destruction

**Problem**: Unknown object destroying itself
**Solution**:
1. Set `logAllGameObjectsBeforeSceneChange = true`
2. Capture snapshot before suspected destruction
3. Trigger destruction
4. Analyze changes
5. Identify destroyed object by name/parent

### Validating Scene Cleanup

**Problem**: Too many objects surviving scene changes
**Solution**:
1. Enable monitoring
2. Load scene A
3. Load scene B
4. Check survived count
5. Identify unwanted persistent objects

## Troubleshooting

### Issue: Monitor destroyed on scene change
**Solution**: Ensure GameObject is root (not parented) and DontDestroyOnLoad is called

### Issue: No snapshot captured
**Solution**: Verify `enableMonitoring = true` and scene actually unloads

### Issue: Too much console spam
**Solution**: Disable `logAllGameObjectsBeforeSceneChange` and `verboseLogging`

### Issue: Missing objects not detected
**Solution**: Verify objects existed before scene change (check snapshot)

### Issue: Duplicate monitoring
**Solution**: Ensure only ONE GameObjectLifecycleMonitor exists in scene

## Performance Considerations

### Performance Impact

| Setting | Impact | Recommendation |
|---------|--------|----------------|
| `enableMonitoring = true` | Low | Safe for production |
| `verboseLogging = true` | Medium | Disable in builds |
| `logAllGameObjectsBeforeSceneChange = true` | High | Editor only |
| `onlyTrackDontDestroyOnLoad = true` | Low | Recommended for focused debugging |

### Optimization Tips

```csharp
// Use filters to reduce tracking overhead
onlyTrackDontDestroyOnLoad = true;  // Track only persistent objects
ignoreUnityInternals = true;        // Ignore Unity default objects

// Disable verbose logging in builds
verboseLogging = false;

// Disable all monitoring in production
enableMonitoring = false;
```

## Related Scripts

- **DebugManager**: Centralized logging system
- **SceneManager**: Unity scene management
- **DontDestroyOnLoad**: Unity persistence mechanism
