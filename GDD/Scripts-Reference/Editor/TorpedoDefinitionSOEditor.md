# TorpedoDefinitionSOEditor.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/TorpedoDefinitionSOEditor.cs` |
| **Namespace** | `WOS.Editor` |
| **Inheritance** | `UnityEditor.Editor` |
| **Lines** | 548 |
| **Architecture** | Custom Editor with Visual Geometry Preview (Torpedo Variant) |

## Purpose

Custom Unity Editor for `TorpedoDefinitionSO` ScriptableObjects that mirrors the turret editor functionality but specialized for torpedo launcher geometry. Provides interactive top-down 2D preview with draggable pivot and tube exit points, enabling precise positioning of torpedo launch geometry without manual coordinate entry.

## Key Features

### Visual Geometry Editor
- **Interactive Preview**: Top-down 2D view with grid and zoom/pan controls
- **Draggable Points**: Yellow pivot point (rotation center) and green tube exit points (launch positions)
- **Sprite Preview**: Optional launcher sprite overlay for visual reference
- **Grid System**: Configurable grid with snap-to-grid functionality
- **Presets**: Quick position templates for common torpedo launcher configurations

### Editor Controls
- **Zoom**: Mouse wheel (2x to 0.25x range)
- **Pan**: Right-click drag
- **Grid Toggle**: Show/hide alignment grid
- **Grid Snap**: Snap points to grid intersections
- **Reset View**: Return to default zoom/pan state

### Launcher Configuration
- **Pivot Point**: Single rotation center (yellow)
- **Tube Exits**: Multiple torpedo launch positions (green)
- **Presets**: Single, Twin, Triple, Quad tube configurations
- **Visual Feedback**: Color-coded handles with labels

## Configuration Tables

### Torpedo Tube Presets
| Preset | Pivot | Tube Count | Layout |
|--------|-------|------------|--------|
| Single | (0, 0) | 1 | Center tube at (0, 0.5) |
| Twin | (0, 0) | 2 | Tubes at (-0.3, 0.5) and (0.3, 0.5) |
| Triple | (0, 0) | 3 | Tubes at (-0.4, 0.5), (0, 0.5), (0.4, 0.5) |
| Quad | (0, 0) | 4 | Two rows: (-0.3, 0.3), (0.3, 0.3), (-0.3, 0.7), (0.3, 0.7) |

### Color Scheme
| Element | Color | Purpose |
|---------|-------|---------|
| Pivot Point | Yellow | Rotation center |
| Tube Exits | Green | Launch positions |
| Grid Lines | Light Gray | Alignment guide |
| Selection | Cyan | Active handle |

### Launcher Types
| Type | Description | Typical Configuration |
|------|-------------|----------------------|
| Fixed | Non-rotating launchers | Single/Twin tubes |
| Trainable | Rotating launchers | Twin/Triple tubes |
| Deck Mounted | Surface launchers | Any configuration |
| Submerged | Underwater launchers | Single/Twin tubes |

## Key Code Snippets

### Visual Preview Section
```csharp
private void DrawVisualPreview()
{
    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Torpedo Launcher Geometry Editor", EditorStyles.boldLabel);

    // Toolbar for controls
    EditorGUILayout.BeginHorizontal();
    showGrid = GUILayout.Toggle(showGrid, "Show Grid", EditorStyles.miniButton);
    snapToGrid = GUILayout.Toggle(snapToGrid, "Snap to Grid", EditorStyles.miniButton);
    if (GUILayout.Button("Reset View", EditorStyles.miniButton))
    {
        zoom = 1f;
        panOffset = Vector2.zero;
    }
    EditorGUILayout.EndHorizontal();

    // Preview rect
    Rect previewRect = GUILayoutUtility.GetRect(400, 400);
    DrawLauncherGeometry(previewRect);

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Creates the main preview UI with controls for grid visibility, snapping, and view reset.

### Interactive Launcher Editor
```csharp
private void DrawLauncherGeometry(Rect rect)
{
    Handles.BeginGUI();

    // Transform to preview space
    Vector2 center = rect.center;
    float scale = zoom * 100f;

    // Draw grid if enabled
    if (showGrid)
    {
        DrawGrid(rect, center, scale);
    }

    // Draw launcher sprite if available
    if (torpedoDef.launcherSprite != null && showSprite)
    {
        DrawSpritePreview(rect, center, scale);
    }

    // Draw and handle pivot point (yellow)
    Vector2 pivotScreen = WorldToScreen(torpedoDef.pivotPoint, center, scale);
    if (DrawHandle(pivotScreen, Color.yellow, "Pivot"))
    {
        torpedoDef.pivotPoint = ScreenToWorld(Event.current.mousePosition, center, scale);
        MarkDirty();
    }

    // Draw and handle tube exit points (green)
    for (int i = 0; i < torpedoDef.tubeExitPoints.Count; i++)
    {
        Vector2 tubeScreen = WorldToScreen(torpedoDef.tubeExitPoints[i], center, scale);
        if (DrawHandle(tubeScreen, Color.green, $"Tube {i + 1}"))
        {
            torpedoDef.tubeExitPoints[i] = ScreenToWorld(Event.current.mousePosition, center, scale);
            MarkDirty();
        }
    }

    Handles.EndGUI();
}
```

**Purpose**: Main launcher geometry rendering loop with coordinate transforms, sprite overlay, and interactive point manipulation.

### Handle Interaction
```csharp
private bool DrawHandle(Vector2 position, Color color, string label)
{
    bool isDragging = false;
    float handleSize = 10f;
    Rect handleRect = new Rect(position.x - handleSize / 2, position.y - handleSize / 2, handleSize, handleSize);

    // Draw handle circle
    Handles.color = color;
    Handles.DrawSolidDisc(new Vector3(position.x, position.y, 0), Vector3.forward, handleSize / 2);

    // Draw label
    GUIStyle labelStyle = new GUIStyle(EditorStyles.miniLabel);
    labelStyle.normal.textColor = color;
    GUI.Label(new Rect(position.x + 12, position.y - 8, 100, 20), label, labelStyle);

    // Handle mouse input
    Event e = Event.current;
    if (e.type == EventType.MouseDown && handleRect.Contains(e.mousePosition))
    {
        isDragging = true;
        e.Use();
    }
    else if (e.type == EventType.MouseDrag && handleRect.Contains(e.mousePosition))
    {
        isDragging = true;
        e.Use();
    }

    return isDragging;
}
```

**Purpose**: Renders draggable handle with color-coded visual feedback and mouse interaction detection.

### Preset Application
```csharp
private void ApplyPreset(string presetName)
{
    Undo.RecordObject(torpedoDef, "Apply Torpedo Launcher Preset");

    torpedoDef.pivotPoint = Vector2.zero;
    torpedoDef.tubeExitPoints.Clear();

    switch (presetName)
    {
        case "Single":
            torpedoDef.tubeExitPoints.Add(new Vector2(0f, 0.5f));
            break;
        case "Twin":
            torpedoDef.tubeExitPoints.Add(new Vector2(-0.3f, 0.5f));
            torpedoDef.tubeExitPoints.Add(new Vector2(0.3f, 0.5f));
            break;
        case "Triple":
            torpedoDef.tubeExitPoints.Add(new Vector2(-0.4f, 0.5f));
            torpedoDef.tubeExitPoints.Add(new Vector2(0f, 0.5f));
            torpedoDef.tubeExitPoints.Add(new Vector2(0.4f, 0.5f));
            break;
        case "Quad":
            torpedoDef.tubeExitPoints.Add(new Vector2(-0.3f, 0.3f));
            torpedoDef.tubeExitPoints.Add(new Vector2(0.3f, 0.3f));
            torpedoDef.tubeExitPoints.Add(new Vector2(-0.3f, 0.7f));
            torpedoDef.tubeExitPoints.Add(new Vector2(0.3f, 0.7f));
            break;
    }

    EditorUtility.SetDirty(torpedoDef);
}
```

**Purpose**: Applies predefined launcher configurations with undo support.

### Coordinate Transformation
```csharp
private Vector2 WorldToScreen(Vector2 worldPos, Vector2 center, float scale)
{
    Vector2 screenPos = center + (worldPos + panOffset) * scale;
    return screenPos;
}

private Vector2 ScreenToWorld(Vector2 screenPos, Vector2 center, float scale)
{
    Vector2 worldPos = ((screenPos - center) / scale) - panOffset;

    if (snapToGrid)
    {
        float gridSize = 0.1f;
        worldPos.x = Mathf.Round(worldPos.x / gridSize) * gridSize;
        worldPos.y = Mathf.Round(worldPos.y / gridSize) * gridSize;
    }

    return worldPos;
}
```

**Purpose**: Converts between world coordinates (launcher local space) and screen coordinates (editor preview space) with optional grid snapping.

## Public API

### Unity Menu Items
None - this is a CustomEditor that appears automatically in the Inspector when a `TorpedoDefinitionSO` asset is selected.

### Inspector Actions
| Button | Action |
|--------|--------|
| Apply Preset → Single | Configure single tube |
| Apply Preset → Twin | Configure dual tubes |
| Apply Preset → Triple | Configure triple tubes |
| Apply Preset → Quad | Configure quad tubes |
| Add Tube Exit | Add new launch position |
| Remove Tube Exit | Delete last launch position |

## Usage Examples

### Creating a New Torpedo Launcher
1. Create launcher asset: `Create > WOS > Items > Torpedo Definition`
2. Select asset in Project window
3. In Inspector, scroll to "Torpedo Launcher Geometry Editor" section
4. Click "Apply Preset → Triple" for triple-tube configuration
5. Adjust pivot point (yellow) by dragging to rotation center
6. Fine-tune tube positions (green) by dragging
7. Enable "Show Grid" and "Snap to Grid" for precise alignment
8. Assign launcher sprite for visual reference
9. Configure remaining properties (torpedo type, reload time, etc.)

### Custom Launcher Configuration
```csharp
// Manually configure asymmetric launcher
var launcher = CreateInstance<TorpedoDefinitionSO>();
launcher.pivotPoint = new Vector2(0.1f, -0.2f); // Offset pivot
launcher.tubeExitPoints.Clear();
launcher.tubeExitPoints.Add(new Vector2(-0.5f, 0.6f)); // Port tube
launcher.tubeExitPoints.Add(new Vector2(0.5f, 0.6f));  // Starboard tube
launcher.tubeExitPoints.Add(new Vector2(0f, 0.4f));    // Center tube (aft)
```

### Adjusting Existing Geometry
1. Select launcher asset
2. In Torpedo Launcher Geometry Editor, enable "Show Grid"
3. Drag pivot point to desired rotation center
4. Drag each tube exit point to launch position
5. Use zoom/pan for fine adjustments
6. Changes save automatically

## Integration Points

### Dependencies
- **TorpedoDefinitionSO**: The ScriptableObject being edited
- **UnityEditor.Handles**: For 2D drawing in preview
- **UnityEditor.Undo**: For undo/redo support

### Related Systems
- **EquipmentDatabaseSOEditor**: Manages collections of torpedo definitions
- **ShipDefinitionSOEditor**: References torpedo launchers in ship loadouts
- **Combat System**: Uses tube exit points for torpedo spawning
- **Submarine Systems**: Special integration for submerged launches

### Data Flow
```
TorpedoDefinitionSOEditor (geometry)
    → TorpedoDefinitionSO (asset)
    → ShipDefinitionSO (ship loadout)
    → Runtime Combat System (torpedo spawning)
    → TorpedoController (torpedo physics)
```

## Design Notes

### Architectural Decisions
- **Visual-First Design**: Immediate visual feedback reduces trial-and-error
- **Preset System**: Common configurations available with one click
- **Grid Snapping**: Optional precision without forcing rigid alignment
- **Color Coding**: Yellow/green distinction prevents confusion
- **Parallel Design**: Mirrors turret editor for consistency

### Performance Considerations
- Preview renders only when Inspector is visible
- Handle interaction uses event-based input (not polling)
- Grid drawing optimized for typical zoom ranges
- Sprite preview cached and reused

### Limitations
- 2D preview only (top-down view)
- No visualization for torpedo launch angles
- Grid size fixed at 0.1 units
- Maximum zoom constrained to prevent performance issues
- No depth axis visualization for submerged launches

### Future Enhancements
- Launch angle visualization (elevation/depression)
- Torpedo trajectory preview
- Copy/paste geometry between launchers
- Symmetry tools (mirror port/starboard)
- Custom preset saving
- Multi-launcher batch editing
- Export geometry to JSON
- Import from external modeling tools
- Submerged launch depth configuration

### Common Patterns
- All geometry edits wrapped in `Undo.RecordObject()`
- Changes trigger `EditorUtility.SetDirty()` for asset saving
- Mouse events consumed with `Event.current.Use()`
- Coordinate transforms isolated in helper methods
- Same architecture as TurretDefinitionSOEditor for maintainability

### Debugging Tips
- Enable "Show Grid" to verify coordinate system orientation
- Check pivot point is centered on rotation axis
- Verify tube points align with launcher geometry
- Test zoom/pan if handles not responding to input
- Ensure launcher sprite matches actual asset dimensions
- Check tube exit spacing for realistic torpedo separation
