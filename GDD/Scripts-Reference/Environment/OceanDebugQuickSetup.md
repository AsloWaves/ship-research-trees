# OceanDebugQuickSetup.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/OceanDebugQuickSetup.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~154 |
| **Architecture** | Quick fix script for ocean culling issues |

## Purpose
Quick setup script to immediately disable all ocean culling systems. Designed as a one-click solution for ocean visibility issues. Can be added to any GameObject in the scene for instant culling control.

---

## Configuration

### Instant Fixes
| Setting | Default | Description |
|---------|---------|-------------|
| `applyOnStart` | true | Apply fixes on Start |
| `showTileInfo` | true | Show tile information GUI |

---

## Core Implementation

```csharp
/// Apply all known fixes for ocean tile culling issues
[ContextMenu("Apply All Ocean Fixes")]
public void ApplyAllFixes()
{
    DebugManager.Log(DebugCategory.Ocean, "=== APPLYING ALL OCEAN CULLING FIXES ===", this);

    // 1. Fix OceanChunkManager
    FixOceanChunkManager();

    // 2. Fix EnvironmentLODManager
    FixEnvironmentLODManager();

    // 3. Fix all OceanTileController instances
    FixAllOceanTileControllers();

    // 4. Emergency enable all renderers
    EmergencyEnableAllOceanRenderers();

    DebugManager.Log(DebugCategory.Ocean, "=== ALL OCEAN FIXES APPLIED ===", this);
}
```

---

## Fix Methods

### OceanChunkManager Fix
```csharp
private void FixOceanChunkManager()
{
    var oceanManager = FindFirstObjectByType<OceanChunkManager>();
    if (oceanManager != null)
    {
        // Use reflection to set private fields
        var gridRadiusField = typeof(OceanChunkManager).GetField("gridRadius",
            System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
        var tilesPerFrameField = typeof(OceanChunkManager).GetField("tilesPerFrame",
            System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);

        gridRadiusField?.SetValue(oceanManager, 5);
        tilesPerFrameField?.SetValue(oceanManager, 50);

        DebugManager.Log(DebugCategory.Ocean,
            "Fixed OceanChunkManager: gridRadius=5, tilesPerFrame=50", this);

        // Trigger rebuild
        oceanManager.ForceRebuildOcean();
    }
}
```

### EnvironmentLODManager Fix
```csharp
private void FixEnvironmentLODManager()
{
    var lodManager = FindFirstObjectByType<EnvironmentLODManager>();
    if (lodManager != null)
    {
        // Disable ocean tile management
        var manageOceanTilesField = typeof(EnvironmentLODManager).GetField("manageOceanTiles",
            System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);

        manageOceanTilesField?.SetValue(lodManager, false);

        DebugManager.Log(DebugCategory.Ocean,
            "Fixed EnvironmentLODManager: disabled ocean tile management", this);
    }
}
```

### OceanTileController Fix
```csharp
private void FixAllOceanTileControllers()
{
    var tileControllers = FindObjectsByType<OceanTileController>(FindObjectsSortMode.None);
    int fixedCount = 0;

    foreach (var controller in tileControllers)
    {
        if (controller != null)
        {
            // Disable culling
            var enableCullingField = typeof(OceanTileController).GetField("enableCulling",
                System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);

            enableCullingField?.SetValue(controller, false);

            // Force visibility
            controller.SetVisibility(true);
            controller.SetDetailLevel(true);

            fixedCount++;
        }
    }

    DebugManager.Log(DebugCategory.Ocean, $"Fixed {fixedCount} OceanTileController instances", this);
}
```

### Emergency Renderer Enable
```csharp
private void EmergencyEnableAllOceanRenderers()
{
    var allRenderers = FindObjectsByType<Renderer>(FindObjectsSortMode.None);
    int enabledCount = 0;

    foreach (var renderer in allRenderers)
    {
        if (renderer.gameObject.name.Contains("OceanTile") && !renderer.enabled)
        {
            renderer.enabled = true;
            enabledCount++;
        }
    }

    DebugManager.LogWarning(DebugCategory.Ocean,
        $"EMERGENCY: Force-enabled {enabledCount} ocean tile renderers", this);
}
```

---

## Runtime GUI

```csharp
private void OnGUI()
{
    if (!showTileInfo) return;

    var oceanManager = FindFirstObjectByType<OceanChunkManager>();
    if (oceanManager == null) return;

    var stats = oceanManager.GetOceanStats();
    var tileControllers = FindObjectsByType<OceanTileController>(FindObjectsSortMode.None);

    GUILayout.BeginArea(new Rect(Screen.width - 300, 10, 280, 200));
    GUILayout.Label("<size=14><color=yellow><b>Ocean Debug Info</b></color></size>");
    GUILayout.Label($"<color=white>Active Tiles: {stats.activeTileCount}</color>");
    GUILayout.Label($"<color=white>Tile Controllers: {tileControllers.Length}</color>");
    GUILayout.Label($"<color=white>Spawn Queue: {stats.tilesInSpawnQueue}</color>");
    GUILayout.Label($"<color=white>Grid: {stats.gridRadius * 2 + 1}x{stats.gridRadius * 2 + 1}</color>");

    if (GUILayout.Button("Apply All Fixes"))
        ApplyAllFixes();

    GUILayout.EndArea();
}
```

---

## Usage Example

```csharp
// Method 1: Add component to any GameObject
// Fixes apply automatically on Start

// Method 2: Manual trigger
OceanDebugQuickSetup quickSetup = FindFirstObjectByType<OceanDebugQuickSetup>();
quickSetup.ApplyAllFixes();

// Method 3: Context menu
// Right-click component → "Apply All Ocean Fixes"
```

---

## Integration Points

### Dependencies
- `OceanChunkManager` - Ocean management
- `EnvironmentLODManager` - LOD management
- `OceanTileController` - Individual tiles
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### One-Click Solution
- Single method applies all known fixes
- No configuration required
- Works on any GameObject in scene

### Fix Order
1. OceanChunkManager - Grid settings
2. EnvironmentLODManager - Disable management
3. OceanTileControllers - Disable per-tile culling
4. Emergency renderers - Force enable all

### Default Values
- Grid radius: 5 (11x11 grid)
- Tiles per frame: 50
- Ocean tile management: disabled
- Culling: disabled

### When to Use
- Ocean tiles not appearing
- Tiles disappearing at distance
- Culling issues during development
- Quick testing without configuration
