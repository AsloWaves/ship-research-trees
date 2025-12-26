# OceanCullingDebugger.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/OceanCullingDebugger.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~318 |
| **Architecture** | Runtime culling debug tool with reflection |

## Purpose
Runtime debugging tool for ocean tile culling systems. Provides sliders and controls to override all culling behaviors during gameplay. Uses reflection to modify private fields in OceanChunkManager and EnvironmentLODManager.

---

## Configuration

### Master Culling Controls
| Setting | Default | Description |
|---------|---------|-------------|
| `disableAllCulling` | true | Completely disable ALL culling |
| `forceEnableAllTiles` | true | Force enable all renderers |

### Distance Override Controls
| Setting | Default | Description |
|---------|---------|-------------|
| `overrideLODDistances` | true | Override LOD distances |
| `forceCullDistance` | 10000 | Override cull distance |
| `forceLowDetailDistance` | 8000 | Override low detail distance |
| `forceMediumDetailDistance` | 5000 | Override medium detail distance |
| `forceHighDetailDistance` | 2000 | Override high detail distance |

### Grid Control
| Setting | Default | Description |
|---------|---------|-------------|
| `overrideGridRadius` | true | Override chunk grid radius |
| `forceGridRadius` | 5 | Forced grid radius (1-10) |
| `forceTilesPerFrame` | 50 | Tiles to spawn per frame (1-100) |

### Debug Information
| Setting | Default | Description |
|---------|---------|-------------|
| `showTileCount` | true | Show tile count on screen |
| `logCullingActions` | true | Log override actions |

---

## Reflection-Based Overrides

### OceanChunkManager Override
```csharp
private void OverrideOceanChunkManager()
{
    // Force settings via reflection since fields are private
    var gridRadiusField = typeof(OceanChunkManager).GetField("gridRadius",
        System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
    var tilesPerFrameField = typeof(OceanChunkManager).GetField("tilesPerFrame",
        System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);

    if (gridRadiusField != null)
    {
        gridRadiusField.SetValue(oceanChunkManager, forceGridRadius);
        if (logCullingActions)
            DebugManager.Log(DebugCategory.Ocean, $"Forced gridRadius to {forceGridRadius}", this);
    }

    if (tilesPerFrameField != null)
    {
        tilesPerFrameField.SetValue(oceanChunkManager, forceTilesPerFrame);
        if (logCullingActions)
            DebugManager.Log(DebugCategory.Ocean, $"Forced tilesPerFrame to {forceTilesPerFrame}", this);
    }
}
```

### EnvironmentLODManager Override
```csharp
private void OverrideEnvironmentLODManager()
{
    // Force LOD manager to use our distances
    var cullDistanceField = typeof(EnvironmentLODManager).GetField("cullDistance",
        System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
    var lowDetailField = typeof(EnvironmentLODManager).GetField("lowDetailDistance", ...);
    var mediumDetailField = typeof(EnvironmentLODManager).GetField("mediumDetailDistance", ...);
    var highDetailField = typeof(EnvironmentLODManager).GetField("highDetailDistance", ...);
    var manageOceanTilesField = typeof(EnvironmentLODManager).GetField("manageOceanTiles", ...);

    if (disableAllCulling && manageOceanTilesField != null)
    {
        manageOceanTilesField.SetValue(environmentLODManager, false);
        if (logCullingActions)
            DebugManager.Log(DebugCategory.Ocean, "Disabled EnvironmentLODManager ocean tile management", this);
    }

    if (cullDistanceField != null) cullDistanceField.SetValue(environmentLODManager, forceCullDistance);
    if (lowDetailField != null) lowDetailField.SetValue(environmentLODManager, forceLowDetailDistance);
    if (mediumDetailField != null) mediumDetailField.SetValue(environmentLODManager, forceMediumDetailDistance);
    if (highDetailField != null) highDetailField.SetValue(environmentLODManager, forceHighDetailDistance);
}
```

---

## Force Enable Tiles

```csharp
private void ForceEnableAllTileRenderers()
{
    if (oceanTileControllers == null) return;

    int enabledCount = 0;
    foreach (var tileController in oceanTileControllers)
    {
        if (tileController != null)
        {
            // Force visibility and detail level
            tileController.SetVisibility(true);
            tileController.SetDetailLevel(true);

            // Also force the renderer directly
            var renderer = tileController.GetComponent<Renderer>();
            if (renderer != null && !renderer.enabled)
            {
                renderer.enabled = true;
                enabledCount++;
            }

            // Override culling settings via reflection
            if (disableAllCulling)
            {
                var enableCullingField = typeof(OceanTileController).GetField("enableCulling",
                    System.Reflection.BindingFlags.NonPublic | System.Reflection.BindingFlags.Instance);
                if (enableCullingField != null)
                    enableCullingField.SetValue(tileController, false);
            }
        }
    }
}
```

---

## Context Menu Actions

```csharp
/// Force rebuild the entire ocean with current settings
[ContextMenu("Force Rebuild Ocean")]
public void ForceRebuildOcean()
{
    if (oceanChunkManager != null)
    {
        ApplyOverrides();

        // Call rebuild method via reflection
        var rebuildMethod = typeof(OceanChunkManager).GetMethod("RebuildOcean",
            System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.Instance);
        if (rebuildMethod != null)
        {
            rebuildMethod.Invoke(oceanChunkManager, null);
            DebugManager.Log(DebugCategory.Ocean, "Forced ocean rebuild with new culling settings", this);
        }
    }
}

/// Emergency: Enable all renderers in scene
[ContextMenu("Emergency Enable All Renderers")]
public void EmergencyEnableAllRenderers()
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
    if (!showTileCount) return;

    GUILayout.BeginArea(new Rect(10, 10, 300, 200));
    GUILayout.Label($"<size=14><color=white><b>Ocean Culling Debug</b></color></size>");
    GUILayout.Label($"<color=white>Active Tiles: {(oceanTileControllers?.Length ?? 0)}</color>");
    GUILayout.Label($"<color=white>Grid Radius: {forceGridRadius} ({(forceGridRadius * 2 + 1)}x{(forceGridRadius * 2 + 1)})</color>");
    GUILayout.Label($"<color=white>Culling Disabled: {disableAllCulling}</color>");
    GUILayout.Label($"<color=white>Force Enable: {forceEnableAllTiles}</color>");

    if (GUILayout.Button("Force Rebuild Ocean"))
        ForceRebuildOcean();

    if (GUILayout.Button("Emergency Enable All"))
        EmergencyEnableAllRenderers();

    GUILayout.EndArea();
}
```

---

## Gizmo Visualization

```csharp
private void OnDrawGizmosSelected()
{
    if (oceanChunkManager == null) return;

    Vector3 center = transform.position;
    float tileSize = 1024f;

    // Draw grid bounds
    Gizmos.color = Color.green;
    float gridSize = forceGridRadius * 2 + 1;
    float totalSize = gridSize * tileSize;
    Gizmos.DrawWireCube(center, new Vector3(totalSize, 10f, totalSize));

    // Draw distance circles
    Gizmos.color = Color.yellow;
    DrawCircle(center, forceHighDetailDistance);

    Gizmos.color = new Color(1f, 0.5f, 0f); // Orange
    DrawCircle(center, forceMediumDetailDistance);

    Gizmos.color = Color.red;
    DrawCircle(center, forceCullDistance);
}
```

---

## Usage Example

```csharp
// Add to scene for culling debugging
OceanCullingDebugger debugger = FindFirstObjectByType<OceanCullingDebugger>();

// Force all tiles visible
debugger.disableAllCulling = true;
debugger.forceEnableAllTiles = true;

// Override grid settings
debugger.forceGridRadius = 5;  // 11x11 grid
debugger.forceTilesPerFrame = 50;

// Force rebuild
debugger.ForceRebuildOcean();

// Emergency fix
debugger.EmergencyEnableAllRenderers();
```

---

## Integration Points

### Dependencies
- `OceanChunkManager` - Ocean tile management
- `EnvironmentLODManager` - LOD coordination
- `OceanTileController` - Individual tile control
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Reflection Usage
- Uses reflection to access private fields
- Allows runtime modification without code changes
- Useful for debugging production builds

### Override Priority
- Overrides applied every 0.5 seconds
- Ensures settings persist despite other systems
- Emergency enable runs on-demand

### Distance Visualization
- Gizmos show LOD distance circles
- Grid bounds shown as wire cube
- Helps visualize culling regions

### Performance
- Updates every 0.5 seconds (not every frame)
- Tile controller array refreshed periodically
- Logging can be disabled for performance
