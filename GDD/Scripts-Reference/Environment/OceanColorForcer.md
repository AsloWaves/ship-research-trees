# OceanColorForcer.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/OceanColorForcer.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~136 |
| **Architecture** | Emergency ocean color override tool |

## Purpose
Emergency debugging script to force correct ocean tile colors. Bypasses all other color systems and directly sets tile colors. Provides context menu actions and runtime GUI for testing different ocean color schemes.

---

## Configuration

### Emergency Color Override
| Setting | Default | Description |
|---------|---------|-------------|
| `forcedOceanColor` | (0.05, 0.1, 0.25) | MidnightZone dark blue |
| `continuousOverride` | true | Apply color every frame |
| `applyOnStart` | true | Apply color on Start |
| `showDebugInfo` | true | Show debug GUI |

---

## Core Implementation

```csharp
/// Emergency: Force all ocean tiles to use the specified color
[ContextMenu("Force Ocean Colors")]
public void ForceOceanColors()
{
    var allGameObjects = FindObjectsByType<GameObject>(FindObjectsSortMode.None);
    int coloredCount = 0;

    foreach (var go in allGameObjects)
    {
        if (go.name.Contains("OceanTile"))
        {
            var spriteRenderer = go.GetComponent<SpriteRenderer>();
            if (spriteRenderer != null)
            {
                spriteRenderer.color = forcedOceanColor;
                coloredCount++;
            }

            var renderer = go.GetComponent<Renderer>();
            if (renderer != null && renderer.material != null)
            {
                renderer.material.color = forcedOceanColor;
            }
        }
    }

    if (showDebugInfo)
    {
        DebugManager.Log(DebugCategory.Ocean,
            $"EMERGENCY: Forced color {forcedOceanColor} on {coloredCount} ocean tiles", this);
    }
}
```

---

## Context Menu Actions

### Test Colors
```csharp
[ContextMenu("Test Dark Blue")]
public void TestDarkBlue()
{
    forcedOceanColor = new Color(0.05f, 0.1f, 0.25f, 1f);
    ForceOceanColors();
}

[ContextMenu("Test Medium Blue")]
public void TestMediumBlue()
{
    forcedOceanColor = new Color(0.1f, 0.3f, 0.6f, 1f);
    ForceOceanColors();
}

[ContextMenu("Test Light Blue")]
public void TestLightBlue()
{
    forcedOceanColor = new Color(0.3f, 0.6f, 0.9f, 1f);
    ForceOceanColors();
}

[ContextMenu("Test Red (Debug)")]
public void TestRed()
{
    forcedOceanColor = Color.red;
    ForceOceanColors();
}
```

---

## Runtime GUI

```csharp
private void OnGUI()
{
    if (!showDebugInfo) return;

    // Count ocean tiles
    var allGameObjects = FindObjectsByType<GameObject>(FindObjectsSortMode.None);
    int oceanTileCount = 0;
    foreach (var go in allGameObjects)
    {
        if (go.name.Contains("OceanTile"))
            oceanTileCount++;
    }

    GUILayout.BeginArea(new Rect(Screen.width - 250, Screen.height - 150, 240, 140));
    GUILayout.Label("<size=14><color=red><b>EMERGENCY COLOR FORCER</b></color></size>");
    GUILayout.Label($"<color=white>Ocean Tiles Found: {oceanTileCount}</color>");
    GUILayout.Label($"<color=white>Forced Color: R={forcedOceanColor.r:F2} G={forcedOceanColor.g:F2} B={forcedOceanColor.b:F2}</color>");

    if (GUILayout.Button("Force Dark Blue"))
        TestDarkBlue();

    if (GUILayout.Button("Force Red (Test)"))
        TestRed();

    GUILayout.EndArea();
}
```

---

## Usage Example

```csharp
// Add to scene for emergency color debugging
OceanColorForcer forcer = FindFirstObjectByType<OceanColorForcer>();

// Test different colors via context menu or code
forcer.TestDarkBlue();   // Deep ocean color
forcer.TestMediumBlue(); // Standard ocean
forcer.TestLightBlue();  // Shallow water
forcer.TestRed();        // Debug visibility

// Or set custom color
forcer.forcedOceanColor = new Color(0.2f, 0.4f, 0.8f, 1f);
forcer.ForceOceanColors();
```

---

## Integration Points

### Dependencies
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Emergency Tool
- Designed for debugging ocean color issues
- Bypasses normal color systems completely
- Continuous mode forces color every frame
- Ensures colors stay consistent regardless of other systems

### Color Presets
- **MidnightZone**: (0.05, 0.1, 0.25) - Deep ocean
- **Medium Blue**: (0.1, 0.3, 0.6) - Standard ocean
- **Light Blue**: (0.3, 0.6, 0.9) - Shallow water
- **Red**: Debug color for visibility testing

### Performance Consideration
- Uses FindObjectsByType every frame when continuous
- Only for debugging - should be disabled in production
- GUI shows tile count and current color for verification
