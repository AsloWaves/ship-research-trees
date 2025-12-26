# DebugManager

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Debugging/DebugManager.cs` |
| **Namespace** | `WOS.Debugging` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 1715 |
| **Architecture** | Centralized debug logging system with file logging, Unity log capture, and network context |

## Purpose

Comprehensive debug logging system for WOS naval game. Provides:
- Category-based filtering (18 categories)
- File logging with automatic rotation
- Unity log capture (all Debug.Log, exceptions, third-party libraries)
- Session tracking with statistics
- Network context ([SERVER]/[CLIENT]/[HOST]/[OFFLINE])
- Screenshot on error/exception (Editor only)
- Log history for runtime querying
- Robust singleton persistence across scenes

## Configuration

### Master Controls

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enableAllDebug` | `bool` | `true` | Master switch for all debug output |
| `enableFileLogging` | `bool` | `true` | Create log files in Logs/ folder (Editor only) |
| `logAllToFile` | `bool` | `true` | Log ALL messages regardless of category filters |

### Unity Log Capture

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `captureUnityLogs` | `bool` | `true` | Capture ALL Unity logs to file |
| `captureExceptions` | `bool` | `true` | Capture Unity exceptions and errors |
| `screenshotOnError` | `bool` | `true` | Take screenshot when error/exception occurs |
| `maxScreenshotsPerSession` | `int` | `10` | Maximum screenshots to keep per session |

### Network Context

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `showNetworkContext` | `bool` | `true` | Show network role in log messages |

### Log File Management

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `maxLogFiles` | `int` | `10` | Maximum number of log files to keep (0 = unlimited) |
| `deleteLogsOlderThanDays` | `int` | `7` | Delete log files older than X days |

### Debug Categories

18 categories with individual toggles:
- **Core Systems**: Ship, Ocean, Environment, Camera, Input
- **Technical**: Physics, Performance, System
- **Features**: UI, Economy, Audio, Networking, Chat, External, Inventory, Testing, Combat, Gameplay

### Format Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `showTimestamps` | `bool` | `true` | Show timestamps in messages |
| `showFrameCount` | `bool` | `true` | Show frame count in messages |
| `showSceneName` | `bool` | `false` | Show scene name in messages |
| `useColorCoding` | `bool` | `true` | Color-code messages by category |

### Stack Trace Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `stackTraceMode` | `StackTraceMode` | `ErrorsOnly` | When to include stack traces |
| `stackTraceDepth` | `int` | `5` | Number of stack frames to include (0 = all) |

### Performance

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `maxMessagesPerFrame` | `int` | `50` | Maximum debug messages per frame (prevents spam) |
| `messageThrottleTime` | `float` | `0.1f` | Seconds between identical messages |
| `keepLogHistory` | `bool` | `true` | Keep log history in memory for review |
| `maxLogHistorySize` | `int` | `2000` | Maximum log entries to keep in memory |

### File Logging Options

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `customLogsFolder` | `string` | `""` | Custom logs folder path (relative or absolute) |
| `currentLogFolder` | `string` | `""` | Current resolved log folder path (read-only) |
| `flushAfterEveryMessage` | `bool` | `false` | Flush log file after every message (slower but safer) |
| `flushIntervalSeconds` | `float` | `5f` | Flush interval in seconds (0 = only flush on quit) |
| `includeColorsInFile` | `bool` | `false` | Include color codes in file output |

### Quick Presets

| Field | Description |
|-------|-------------|
| `preset_AllCategories` | Enable all categories |
| `preset_UIAndInput` | Enable UI, Input, Chat, System only |
| `preset_NetworkingOnly` | Enable Networking, System only |
| `preset_PerformanceOnly` | Enable Performance, System only |
| `preset_ErrorsOnly` | Enable System only (errors always shown) |

## Public API

### Static Logging Methods

#### `Log(category, message, context)`
```csharp
[Conditional("UNITY_EDITOR"), Conditional("DEVELOPMENT_BUILD"), Conditional("DEBUG_LOGGING")]
public static void Log(DebugCategory category, string message, UnityEngine.Object context = null)
```

Log debug message with category filtering. **Stripped from release builds**.

**Example**:
```csharp
DebugManager.Log(DebugCategory.Ship, "Ship speed: 25 knots", this);
// [12.34s] [F567] [CLIENT] [SHIP] Ship speed: 25 knots
```

#### `LogWarning(category, message, context)`
```csharp
[Conditional("UNITY_EDITOR"), Conditional("DEVELOPMENT_BUILD"), Conditional("DEBUG_LOGGING")]
public static void LogWarning(DebugCategory category, string message, UnityEngine.Object context = null)
```

Log warning message with category filtering. **Stripped from release builds**.

#### `LogError(category, message, context)`
```csharp
public static void LogError(DebugCategory category, string message, UnityEngine.Object context = null)
```

Log error message (always shown). **NOT stripped** - errors logged in all builds for safety.

#### `Assert(condition, category, message, context)`
```csharp
public static void Assert(bool condition, DebugCategory category, string message, UnityEngine.Object context = null)
```

Log assertion failure with stack trace if condition is false.

**Example**:
```csharp
DebugManager.Assert(health > 0, DebugCategory.Combat,
    "Ship health must be positive!", this);
```

#### `LogPerformance(operation, timeMs, context)`
```csharp
[Conditional("UNITY_EDITOR"), Conditional("DEVELOPMENT_BUILD"), Conditional("DEBUG_LOGGING")]
public static void LogPerformance(string operation, float timeMs, UnityEngine.Object context = null)
```

Log performance-related message with timing.

**Example**:
```csharp
DebugManager.LogPerformance("Ship physics update", 2.5f, this);
// ⚡ [PERF] Ship physics update: 2.50ms
```

#### `LogOnce(category, message, context)`
```csharp
[Conditional("UNITY_EDITOR"), Conditional("DEVELOPMENT_BUILD"), Conditional("DEBUG_LOGGING")]
public static void LogOnce(DebugCategory category, string message, UnityEngine.Object context = null)
```

Log message only once (prevents spam).

#### `LogVerbose(category, message, context)`
```csharp
[Conditional("UNITY_EDITOR"), Conditional("DEVELOPMENT_BUILD"), Conditional("DEBUG_LOGGING")]
public static void LogVerbose(DebugCategory category, string message, UnityEngine.Object context = null)
```

Log verbose message (only to file, not console).

#### `LogForce(message, context)`
```csharp
public static void LogForce(string message, UnityEngine.Object context = null)
```

Force log message regardless of category settings. **Use sparingly**.

### Context Menu Actions

#### `EnableAllCategories()`
```csharp
[ContextMenu("Enable All Categories")]
public void EnableAllCategories()
```

Enable all debug categories.

#### `DisableAllCategories()`
```csharp
[ContextMenu("Disable All Categories")]
public void DisableAllCategories()
```

Disable all debug categories.

#### `OpenLogsFolder()`
```csharp
[ContextMenu("Open Logs Folder")]
public void OpenLogsFolder()
```

Open logs folder in Windows Explorer (Editor only).

#### `ForceFlushLogFile()`
```csharp
[ContextMenu("Force Flush Log File")]
public void ForceFlushLogFile()
```

Immediately flush log file to disk.

#### `ExportLogHistory()`
```csharp
[ContextMenu("Export Log History")]
public void ExportLogHistory()
```

Export in-memory log history to file.

#### `PrintSessionStats()`
```csharp
[ContextMenu("Print Session Stats")]
public void PrintSessionStats()
```

Print session statistics to console.

#### `CleanupOldLogsNow()`
```csharp
[ContextMenu("Cleanup Old Logs Now")]
public void CleanupOldLogsNow()
```

Manually trigger log file cleanup (Editor only).

#### `TakeDebugScreenshot()`
```csharp
[ContextMenu("Take Debug Screenshot")]
public void TakeDebugScreenshot()
```

Manually capture debug screenshot (Editor only).

### Log History Methods

#### `GetLogHistory()`
```csharp
public List<LogEntry> GetLogHistory()
```

Get all log entries from history.

#### `GetLogHistory(category)`
```csharp
public List<LogEntry> GetLogHistory(DebugCategory category)
```

Get log entries filtered by category.

#### `GetLogHistory(logType)`
```csharp
public List<LogEntry> GetLogHistory(LogType logType)
```

Get log entries filtered by log type (Log, Warning, Error, Assert).

#### `SearchLogHistory(searchText)`
```csharp
public List<LogEntry> SearchLogHistory(string searchText)
```

Search log history for messages containing text (case-insensitive).

#### `ClearLogHistory()`
```csharp
public void ClearLogHistory()
```

Clear in-memory log history.

### Accessors

#### `SessionId`
```csharp
public string SessionId { get; }
```

Get current session ID (8-character GUID).

#### `SessionStartTime`
```csharp
public DateTime SessionStartTime { get; }
```

Get session start time.

#### `CurrentLogFilePath`
```csharp
public string CurrentLogFilePath { get; }
```

Get current log file path (Editor only).

#### `GetStats()`
```csharp
public DebugStats GetStats()
```

Get debug statistics (messages, warnings, errors, etc.).

#### `GetNetworkContext()`
```csharp
public static string GetNetworkContext()
```

Get current network context string ([SERVER]/[CLIENT]/[HOST]/[OFFLINE]).

## Usage Examples

### Basic Logging

```csharp
// Simple log
DebugManager.Log(DebugCategory.Ship, "Ship spawned", this);

// Warning
DebugManager.LogWarning(DebugCategory.Networking,
    "High latency detected: 250ms", this);

// Error (always shown, not stripped)
DebugManager.LogError(DebugCategory.Combat,
    "Weapon system failed to initialize!", this);
```

### Performance Logging

```csharp
float startTime = Time.realtimeSinceStartup;
PerformExpensiveOperation();
float elapsed = (Time.realtimeSinceStartup - startTime) * 1000f;
DebugManager.LogPerformance("Expensive operation", elapsed, this);
```

### Conditional Logging

```csharp
// Only log once (prevents spam in Update loops)
DebugManager.LogOnce(DebugCategory.System,
    "Initialization complete", this);

// Verbose (file only, not console)
DebugManager.LogVerbose(DebugCategory.Inventory,
    "Item grid layout: " + gridLayoutJson, this);
```

### Assertions

```csharp
// Assert with automatic stack trace
DebugManager.Assert(player != null, DebugCategory.Gameplay,
    "Player reference is null!", this);

// Assert with custom message
DebugManager.Assert(inventory.Count <= maxCapacity, DebugCategory.Inventory,
    $"Inventory overflow: {inventory.Count}/{maxCapacity}", this);
```

## Log File Format

### Session Header

```
================================================================================
  WAVES OF STEEL - DEBUG LOG
================================================================================
  Session ID:        a1b2c3d4
  Start Time:        2025-12-20 14:30:45
  Unity Version:     6000.0.55f1
  Platform:          WindowsEditor
  Scene:             MainMenu
  Product:           Waves of Steel v0.3.0
  Network:           [OFFLINE]
================================================================================
  Categories Enabled:  Ship, Ocean, Environment, Performance, System, ...
  File Logging:        All=True, Colors=False
  Unity Log Capture:   True, Exceptions=True
  Screenshot on Error: True
  Log Rotation:        Max=10 files, Delete after 7 days
================================================================================
```

### Log Entry Format

```
[12.34s] [F567] [CLIENT] [SHIP] Ship speed: 25 knots
[23.45s] [F890] [SERVER] [NETWORKING] Client connected: Player1
[34.56s] [F1234] [HOST] ⚠️ [PERFORMANCE] Frame time: 18.5ms
[45.67s] [F1567] [OFFLINE] ❌ [SYSTEM] Configuration load failed!
```

### Scene Transition Marker

```
============================================================
  SCENE LOADED: PortHarbor (Additive)
  Time: 14:30:45.123 | Unity Time: 45.67s | Frame: 1234
  Network: [CLIENT]
============================================================
```

### Session Summary

```
================================================================================
  SESSION SUMMARY
================================================================================
  End Time:            2025-12-20 15:45:30
  Duration:            4485.2 seconds (01:14:45)
  Total Messages:      8432
  Warnings:            145
  Errors:              7
  Unity Logs Captured: 234
  Exceptions Captured: 2
  Screenshots Taken:   2
  Final Scene:         Ocean
  Final Frame:         269154
  Final Network:       [OFFLINE]
================================================================================
```

## Integration Points

### Unity Log Capture

```csharp
// Captures ALL Unity logs (including third-party code)
Application.logMessageReceived += OnUnityLogReceived;

// Example captures:
[UNITY] Shader compilation: 234ms
[UNITY WARNING] Missing reference in Scene
[UNITY ERROR] NullReferenceException: Object reference not set
[UNITY EXCEPTION] IndexOutOfRangeException: Index was outside bounds
```

### Network Context Detection

```csharp
// Uses reflection to detect Mirror network state (no hard dependency)
var networkServerType = Type.GetType("Mirror.NetworkServer, Mirror");
var serverActive = (bool?)networkServerType.GetProperty("active")?.GetValue(null);

// Result:
[OFFLINE] - No network active
[CLIENT]  - Client-only mode
[SERVER]  - Dedicated server mode
[HOST]    - Combined server + client
```

### Screenshot on Error

```csharp
// Automatically captures screenshots on errors/exceptions (Editor only)
// Location: Logs/Screenshots/Error_2025-12-20_14-30-45-123_a1b2c3d4_NullRef.png
// Limit: maxScreenshotsPerSession (default 10)
```

## Design Notes

### Singleton Persistence

```csharp
// Robust singleton with DontDestroyOnLoad
// - Survives scene changes
// - Prevents duplicates
// - Root object requirement (auto-moves if parented)
// - Graceful degradation if missing
```

### Conditional Compilation

```csharp
// Log/LogWarning/LogVerbose/LogOnce stripped from release builds
[Conditional("UNITY_EDITOR")]
[Conditional("DEVELOPMENT_BUILD")]
[Conditional("DEBUG_LOGGING")]

// LogError/LogForce NEVER stripped (safety)
```

### Performance Optimization

```csharp
// Message throttling (prevents spam)
messageThrottleTime = 0.1f; // 100ms between identical messages

// Frame limit (prevents console overload)
maxMessagesPerFrame = 50; // Max 50 logs per frame

// Network context caching (reduces overhead)
cachedNetworkContext updated every 1 second (not per log)
```

### Log Rotation

```csharp
// Automatic cleanup on startup
// 1. Delete files older than deleteLogsOlderThanDays (default 7)
// 2. Keep only maxLogFiles most recent (default 10)
// 3. Also cleans up old screenshots
```

## Troubleshooting

### Issue: Logs not appearing in console
**Solution**: Check category is enabled in `debugSettings`

### Issue: Log file not created
**Solution**: Verify `enableFileLogging = true` and running in Editor

### Issue: Too many log files
**Solution**: Reduce `maxLogFiles` or `deleteLogsOlderThanDays`

### Issue: Performance degradation
**Solution**: Reduce `maxMessagesPerFrame` or disable verbose categories

### Issue: Singleton destroyed on scene change
**Solution**: Ensure GameObject is root (not parented), check for multiple instances

## Related Scripts

- **DebugSettingsDrawer**: Custom Inspector for DebugSettings (Editor only)
- **GameObjectLifecycleMonitor**: Tracks GameObject destruction across scenes
- All WOS scripts use DebugManager for logging

## Debug Categories

| Category | Color | Use Case |
|----------|-------|----------|
| **Ship** | Green | Ship physics, movement, controls |
| **Ocean** | Blue | Ocean tiles, wake effects |
| **Environment** | Light Green | Ports, weather, LOD |
| **Camera** | Orange | Camera movement, effects |
| **Input** | Purple | User input, controls |
| **Physics** | Red | Physics calculations |
| **Performance** | Yellow | Performance metrics |
| **UI** | Cyan | User interface, HUD |
| **Economy** | Green | Trading, cargo |
| **Audio** | Pink | Sound effects, music |
| **Networking** | Blue Gray | Multiplayer, server |
| **System** | Brown | Core systems, init |
| **Chat** | Deep Orange | Chat system |
| **External** | Gray | Captured Unity logs |
| **Inventory** | Light Blue | Inventory, equipment |
| **Testing** | Lime | Test systems |
| **Combat** | Dark Red | Combat systems |
| **Gameplay** | Dark Purple | General gameplay |
