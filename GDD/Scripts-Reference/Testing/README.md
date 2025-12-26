# Testing & Debugging Scripts Reference

Comprehensive documentation for all testing and debugging scripts in the Fathoms Deep naval game project.

## Overview

This directory contains documentation for:
- **Testing Scripts** (7): Port systems, inventory, PlayFab integration
- **Debugging Scripts** (3): Centralized logging, lifecycle monitoring, Inspector customization

## Quick Navigation

### Testing Scripts

| Script | Purpose | Status | Lines |
|--------|---------|--------|-------|
| [PlayFabConnectionTest](PlayFabConnectionTest.md) | PlayFab SDK integration testing | Active | 112 |
| [InventoryTestManager](InventoryTestManager.md) | Inventory/equipment testing framework | Active | 800+ |
| [SimplePortTest](SimplePortTest.md) | Port docking and scene transitions | Active | 826 |
| [PortConfigTester](PortConfigTester.md) | Port configuration validation | Active | 204 |
| [HarborExitManager](HarborExitManager.md) | Harbor scene exit handler | ⚠️ DEPRECATED | 268 |
| [ScenePortManager](ScenePortManager.md) | Networked port return handler | ⚠️ DEPRECATED | 381 |
| [PortReturnHandler](PortReturnHandler.md) | Non-networked port return | ⚠️ DEPRECATED | 185 |

### Debugging Scripts

| Script | Purpose | Platform | Lines |
|--------|---------|----------|-------|
| [DebugManager](DebugManager.md) | Centralized logging system | All | 1715 |
| [GameObjectLifecycleMonitor](GameObjectLifecycleMonitor.md) | Scene transition tracking | All | 307 |
| [DebugSettingsDrawer](DebugSettingsDrawer.md) | Custom Inspector UI | Editor Only | 149 |

## By Category

### PlayFab Integration
- **[PlayFabConnectionTest](PlayFabConnectionTest.md)**: Basic authentication testing

### Inventory & Equipment
- **[InventoryTestManager](InventoryTestManager.md)**: Complete inventory testing framework with mock data and persistence

### Port Systems

#### Active Scripts
- **[SimplePortTest](SimplePortTest.md)**: Main port entry/exit system with docking mechanics
- **[PortConfigTester](PortConfigTester.md)**: Configuration validation and zone testing

#### Deprecated Scripts (Use New Port System)
- **[HarborExitManager](HarborExitManager.md)**: → Use `WOS.Port.Harbor.HarborSceneManager`
- **[ScenePortManager](ScenePortManager.md)**: → Use `WOS.Port.Core.PortTransitionManager`
- **[PortReturnHandler](PortReturnHandler.md)**: → Use `WOS.Port.Player.PlayerPortStateController`

### Debugging & Logging
- **[DebugManager](DebugManager.md)**: Centralized logging with 18 categories, file logging, Unity log capture
- **[GameObjectLifecycleMonitor](GameObjectLifecycleMonitor.md)**: Scene transition debugging
- **[DebugSettingsDrawer](DebugSettingsDrawer.md)**: Enhanced Inspector UI for debug categories

## Common Tasks

### Testing PlayFab Integration
1. Read [PlayFabConnectionTest](PlayFabConnectionTest.md)
2. Configure Title ID in PlayFab settings
3. Add component to test scene
4. Run test via Context Menu or Start

### Testing Inventory System
1. Read [InventoryTestManager](InventoryTestManager.md)
2. Enable `useTestingMode = true` for mock data
3. Assign panel references
4. Use hotkeys: **I** (inventory), **E** (equipment), **C** (crew)
5. Enable `usePersistence` for data persistence

### Testing Port Mechanics
1. Read [SimplePortTest](SimplePortTest.md) and [PortConfigTester](PortConfigTester.md)
2. Assign `PortConfigurationSO` in Inspector
3. Drive ship toward port (green = protection, blue = docking)
4. Press **E** to enter harbor
5. Press **R** to exit harbor

### Debugging Scene Transitions
1. Read [GameObjectLifecycleMonitor](GameObjectLifecycleMonitor.md)
2. Add to scene with `DontDestroyOnLoad`
3. Enable `verboseLogging = true`
4. Change scenes
5. Check console for destroyed/disabled/survived objects

### Configuring Debug Logging
1. Read [DebugManager](DebugManager.md)
2. Add DebugManager to scene
3. Enable desired categories (18 available)
4. Configure file logging (Editor only)
5. Use presets for quick configuration

## Hotkey Reference

### InventoryTestManager
- **I**: Toggle Inventory Panel
- **E**: Toggle Equipment Panel
- **C**: Toggle Crew Panel
- **P**: Toggle Ship Selection Panel
- **T**: Toggle Trading Panel
- **R**: Refresh All Panels
- **F1-F8**: API service tests (when `useLocalService = true`)

### SimplePortTest
- **E**: Enter Harbor (when in docking zone)
- **R**: Exit Harbor (when in harbor)

## Architecture Patterns

### Testing Mode System
```csharp
// InventoryTestManager supports dual modes:
useTestingMode = true   → Mock/persistent data (no network)
useTestingMode = false  → PlayFab live data (network required)
```

### Persistence System
```csharp
// Local file persistence for rapid iteration:
LocalFileInventoryService.Instance.LoadInventory(playerId)
LocalFileInventoryService.Instance.SaveInventory(playerId, inventory)

// Files: Logs/InventoryData/player_*.json
```

### Network Architecture
```csharp
// Mirror server-authoritative pattern:
[ServerRpc]  → Client requests to server
[ObserversRpc] → Server broadcasts to all clients
[SyncVar]    → Automatically synchronized variables

// NetworkBehaviour: SimplePortTest, ScenePortManager
// MonoBehaviour: PortReturnHandler (non-networked)
```

### Debug Logging Pattern
```csharp
// All scripts use DebugManager:
DebugManager.Log(DebugCategory.Testing, "Message", this);
DebugManager.LogWarning(DebugCategory.System, "Warning", this);
DebugManager.LogError(DebugCategory.Networking, "Error", this);

// 18 categories: Ship, Ocean, Environment, Camera, Input, Physics,
//                Performance, UI, Economy, Audio, Networking, System,
//                Chat, External, Inventory, Testing, Combat, Gameplay
```

## File Locations

### Source Files
```
Assets/Scripts/Testing/
  ├── PlayFabConnectionTest.cs
  ├── InventoryTestManager.cs
  ├── SimplePortTest.cs
  ├── PortConfigTester.cs
  ├── HarborExitManager.cs (DEPRECATED)
  ├── ScenePortManager.cs (DEPRECATED)
  └── PortReturnHandler.cs (DEPRECATED)

Assets/Scripts/Debugging/
  ├── DebugManager.cs
  ├── GameObjectLifecycleMonitor.cs
  └── DebugSettingsDrawer.cs
```

### Documentation Files
```
D:\Research\Fathoms Deep Research\Scripts-Reference\Testing\
  ├── README.md (this file)
  ├── PlayFabConnectionTest.md
  ├── InventoryTestManager.md
  ├── SimplePortTest.md
  ├── PortConfigTester.md
  ├── HarborExitManager.md
  ├── ScenePortManager.md
  ├── PortReturnHandler.md
  ├── DebugManager.md
  ├── GameObjectLifecycleMonitor.md
  └── DebugSettingsDrawer.md
```

### Log Output
```
Logs/
  ├── WOS_Log_2025-12-20_14-30-45_a1b2c3d4.txt
  ├── Screenshots/
  │   └── Error_2025-12-20_14-30-45-123_a1b2c3d4_NullRef.png
  └── InventoryData/
      ├── player_test_player_001_inventory.json
      └── player_test_player_001_ship_ship_001_loadout.json
```

## Migration Guide

### Deprecated Port System → New Port System

| Old Component | New Component | Migration Steps |
|---------------|---------------|-----------------|
| `HarborExitManager` | `WOS.Port.Harbor.HarborSceneManager` | 1. Remove HarborExitManager<br>2. Add HarborSceneManager<br>3. Update UI button references |
| `ScenePortManager` | `WOS.Port.Core.PortTransitionManager` | 1. Remove ScenePortManager<br>2. Add PortTransitionManager<br>3. Configure PortSceneStateHolder SO |
| `PortReturnHandler` | `WOS.Port.Player.PlayerPortStateController` | 1. Remove PortReturnHandler<br>2. PlayerPortStateController auto-handles returns<br>3. No manual setup required |
| PlayerPrefs persistence | `PortSceneStateHolder` ScriptableObject | 1. Create PortSceneStateHolder SO<br>2. Assign to PortTransitionManager<br>3. Remove PlayerPrefs cleanup code |

### Benefits of New System
- ✅ **ScriptableObject persistence** (no PlayerPrefs)
- ✅ **Unified transition manager** (cleaner architecture)
- ✅ **Automatic player state restoration** (less manual code)
- ✅ **Better multi-port support** (port-relative positioning)
- ✅ **Improved network sync** (server-authoritative)

## Best Practices

### Testing
1. **Always use DebugManager** for logging (category-based filtering)
2. **Enable persistence** for inventory testing (faster iteration)
3. **Use hotkeys** for rapid panel testing
4. **Check network context** in logs ([SERVER]/[CLIENT]/[HOST])
5. **Validate configurations** with Context Menu methods

### Debugging
1. **Enable file logging** for session review (Editor only)
2. **Use GameObjectLifecycleMonitor** for scene transition issues
3. **Configure appropriate categories** (avoid logging everything)
4. **Check log rotation settings** (prevent disk space issues)
5. **Take manual screenshots** for visual debugging

### Performance
1. **Disable verbose logging** in builds
2. **Limit max messages per frame** (default 50)
3. **Use message throttling** (default 0.1s)
4. **Filter Unity internal logs** when not needed
5. **Clear log history** periodically

## Troubleshooting Guide

### Common Issues

#### DebugManager singleton issues
**Problem**: Multiple instances or destroyed on scene change
**Solution**: See [DebugManager Troubleshooting](DebugManager.md#troubleshooting)

#### Port entry not working
**Problem**: E key not responding
**Solution**: See [SimplePortTest Troubleshooting](SimplePortTest.md#troubleshooting)

#### Inventory panels not loading
**Problem**: Panels empty or not responding
**Solution**: See [InventoryTestManager Troubleshooting](InventoryTestManager.md#troubleshooting)

#### PlayFab authentication failing
**Problem**: Title ID or connection errors
**Solution**: See [PlayFabConnectionTest Troubleshooting](PlayFabConnectionTest.md#error-handling)

#### Scene transition object destruction
**Problem**: Objects disappearing on scene change
**Solution**: See [GameObjectLifecycleMonitor Usage](GameObjectLifecycleMonitor.md#usage-examples)

## Related Documentation

### Core Systems
- **Player**: `Scripts-Reference/Player/`
- **Networking**: `Scripts-Reference/Networking/`
- **UI**: `Scripts-Reference/UI/`
- **Inventory**: `Scripts-Reference/Inventory/`

### Configuration
- **ScriptableObjects**: `Scripts-Reference/ScriptableObjects/`
- **Port System**: `Scripts-Reference/Port/`

### Architecture
- **CLAUDE.md**: Project overview and quick reference
- **Documentation/Architecture/**: System architecture documentation

## Version History

| Date | Changes |
|------|---------|
| 2025-12-20 | Initial documentation created for all 10 testing/debugging scripts |
| 2025-01-15 | Port system migration to new architecture (3 scripts deprecated) |

---

**Last Updated**: 2025-12-20
**Total Scripts Documented**: 10 (7 Testing + 3 Debugging)
**Documentation Status**: ✅ Complete
