# TurretDefinitionSOEditor.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/TurretDefinitionSOEditor.cs` |
| **Namespace** | `WOS.Editor` |
| **Inheritance** | `UnityEditor.Editor` |
| **Lines** | 617 |
| **Architecture** | Custom Editor with Visual Geometry Preview |

## Purpose

Custom Unity Editor for `TurretDefinitionSO` ScriptableObjects that provides an interactive visual geometry editor for configuring turret mounting and firing positions. Features a top-down 2D preview with draggable pivot and muzzle exit points, allowing designers to precisely position turret geometry without manual coordinate entry.

## Key Features

### Visual Geometry Editor
- **Interactive Preview**: Top-down 2D view with grid and zoom/pan controls
- **Draggable Points**: Yellow pivot point (rotation center) and green muzzle exit points (firing positions)
- **Sprite Preview**: Optional sprite overlay for visual reference
- **Grid System**: Configurable grid with snap-to-grid functionality
- **Presets**: Quick position templates for common turret configurations

### Editor Controls
- **Zoom**: Mouse wheel (2x to 0.25x range)
- **Pan**: Right-click drag
- **Grid Toggle**: Show/hide alignment grid
- **Grid Snap**: Snap points to grid intersections
- **Reset View**: Return to default zoom/pan state

### Geometry Configuration
- **Pivot Point**: Single rotation center (yellow)
- **Muzzle Exits**: Multiple firing positions (green)
- **Presets**: Single, Twin, Triple, Quad barrel configurations
- **Visual Feedback**: Color-coded handles with labels

## Configuration Tables

### Turret Categories
| Category | Description |
|----------|-------------|
| AntiAircraft | AA guns (dual purpose possible) |
| DualPurpose | Surface and air targets |
| MainGun | Primary armament |
| SecondaryGun | Auxiliary batteries |
| Torpedo | Torpedo launchers |

### Geometry Presets
| Preset | Pivot | Muzzle Count | Layout |
|--------|-------|--------------|--------|
| Single | (0, 0) | 1 | Center barrel at (0, 0.5) |
| Twin | (0, 0) | 2 | Barrels at (-0.3, 0.5) and (0.3, 0.5) |
| Triple | (0, 0) | 3 | Barrels at (-0.4, 0.5), (0, 0.5), (0.4, 0.5) |
| Quad | (0, 0) | 4 | Two rows: (-0.3, 0.3), (0.3, 0.3), (-0.3, 0.7), (0.3, 0.7) |

### Color Scheme
| Element | Color | Purpose |
|---------|-------|---------|
| Pivot Point | Yellow | Rotation center |
| Muzzle Exits | Green | Firing positions |
| Grid Lines | Light Gray | Alignment guide |
| Selection | Cyan | Active handle |

## Key Code Snippets

### Visual Preview Section
```csharp
private void DrawVisualPreview()
{
    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Visual Geometry Editor", EditorStyles.boldLabel);

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
    DrawGeometryEditor(previewRect);

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Creates the main preview UI with controls for grid visibility, snapping, and view reset.

### Interactive Geometry Editor
```csharp
private void DrawGeometryEditor(Rect rect)
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

    // Draw sprite preview if available
    if (turretDef.turretSprite != null && showSprite)
    {
        DrawSpritePreview(rect, center, scale);
    }

    // Draw and handle pivot point (yellow)
    Vector2 pivotScreen = WorldToScreen(turretDef.pivotPoint, center, scale);
    if (DrawHandle(pivotScreen, Color.yellow, "Pivot"))
    {
        turretDef.pivotPoint = ScreenToWorld(Event.current.mousePosition, center, scale);
        MarkDirty();
    }

    // Draw and handle muzzle exit points (green)
    for (int i = 0; i < turretDef.muzzleExitPoints.Count; i++)
    {
        Vector2 muzzleScreen = WorldToScreen(turretDef.muzzleExitPoints[i], center, scale);
        if (DrawHandle(muzzleScreen, Color.green, $"Muzzle {i + 1}"))
        {
            turretDef.muzzleExitPoints[i] = ScreenToWorld(Event.current.mousePosition, center, scale);
            MarkDirty();
        }
    }

    Handles.EndGUI();
}
```

**Purpose**: Main geometry editor rendering loop that handles coordinate transforms, sprite overlay, and interactive point manipulation.

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
    Undo.RecordObject(turretDef, "Apply Turret Preset");

    turretDef.pivotPoint = Vector2.zero;
    turretDef.muzzleExitPoints.Clear();

    switch (presetName)
    {
        case "Single":
            turretDef.muzzleExitPoints.Add(new Vector2(0f, 0.5f));
            break;
        case "Twin":
            turretDef.muzzleExitPoints.Add(new Vector2(-0.3f, 0.5f));
            turretDef.muzzleExitPoints.Add(new Vector2(0.3f, 0.5f));
            break;
        case "Triple":
            turretDef.muzzleExitPoints.Add(new Vector2(-0.4f, 0.5f));
            turretDef.muzzleExitPoints.Add(new Vector2(0f, 0.5f));
            turretDef.muzzleExitPoints.Add(new Vector2(0.4f, 0.5f));
            break;
        case "Quad":
            turretDef.muzzleExitPoints.Add(new Vector2(-0.3f, 0.3f));
            turretDef.muzzleExitPoints.Add(new Vector2(0.3f, 0.3f));
            turretDef.muzzleExitPoints.Add(new Vector2(-0.3f, 0.7f));
            turretDef.muzzleExitPoints.Add(new Vector2(0.3f, 0.7f));
            break;
    }

    EditorUtility.SetDirty(turretDef);
}
```

**Purpose**: Applies predefined geometry configurations with undo support.

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

**Purpose**: Converts between world coordinates (turret local space) and screen coordinates (editor preview space) with optional grid snapping.

## Public API

### Unity Menu Items
None - this is a CustomEditor that appears automatically in the Inspector when a `TurretDefinitionSO` asset is selected.

### Inspector Actions
| Button | Action |
|--------|--------|
| Apply Preset → Single | Configure single barrel |
| Apply Preset → Twin | Configure dual barrels |
| Apply Preset → Triple | Configure triple barrels |
| Apply Preset → Quad | Configure quad barrels |
| Add Muzzle Exit | Add new firing position |
| Remove Muzzle Exit | Delete last firing position |

## Usage Examples

### Creating a New Turret
1. Create turret asset: `Create > WOS > Items > Turret Definition`
2. Select asset in Project window
3. In Inspector, scroll to "Visual Geometry Editor" section
4. Click "Apply Preset → Twin" for dual-barrel configuration
5. Adjust pivot point (yellow) by dragging to rotation center
6. Fine-tune muzzle positions (green) by dragging
7. Enable "Show Grid" and "Snap to Grid" for precise alignment
8. Assign turret sprite for visual reference
9. Configure remaining properties (damage, fire rate, etc.)

### Custom Geometry Configuration
```csharp
// Manually configure asymmetric turret
var turret = CreateInstance<TurretDefinitionSO>();
turret.pivotPoint = new Vector2(0.1f, -0.2f); // Offset pivot
turret.muzzleExitPoints.Clear();
turret.muzzleExitPoints.Add(new Vector2(-0.5f, 0.6f)); // Left barrel
turret.muzzleExitPoints.Add(new Vector2(0.3f, 0.4f));  // Right barrel (offset)
```

### Adjusting Existing Geometry
1. Select turret asset
2. In Visual Geometry Editor, enable "Show Grid"
3. Drag pivot point to desired rotation center
4. Drag each muzzle exit point to firing position
5. Use zoom/pan for fine adjustments
6. Changes save automatically

## Integration Points

### Dependencies
- **TurretDefinitionSO**: The ScriptableObject being edited
- **UnityEditor.Handles**: For 2D drawing in preview
- **UnityEditor.Undo**: For undo/redo support

### Related Systems
- **TurretPrefabGenerator**: Uses geometry data to create turret prefabs
- **EquipmentDatabaseSOEditor**: Manages collections of turret definitions
- **ShipDefinitionSOEditor**: References turret definitions in ship loadouts
- **Combat System**: Uses muzzle exit points for projectile spawning

### Data Flow
```
TurretDefinitionSOEditor (geometry)
    → TurretDefinitionSO (asset)
    → TurretPrefabGenerator (prefab creation)
    → ShipDefinitionSO (ship loadout)
    → Runtime Combat System (projectile spawning)
```

## Design Notes

### Architectural Decisions
- **Visual-First Design**: Immediate visual feedback reduces trial-and-error
- **Preset System**: Common configurations available with one click
- **Grid Snapping**: Optional precision without forcing rigid alignment
- **Color Coding**: Yellow/green distinction prevents confusion

### Performance Considerations
- Preview renders only when Inspector is visible
- Handle interaction uses event-based input (not polling)
- Grid drawing optimized for typical zoom ranges
- Sprite preview cached and reused

### Limitations
- 2D preview only (top-down view)
- No 3D perspective for elevation angles
- Grid size fixed at 0.1 units
- Maximum zoom constrained to prevent performance issues

### Future Enhancements
- Barrel elevation angle visualization
- Copy/paste geometry between turrets
- Symmetry tools (mirror left/right)
- Custom preset saving
- Multi-turret batch editing
- Export geometry to JSON
- Import from external modeling tools

### Common Patterns
- All geometry edits wrapped in `Undo.RecordObject()`
- Changes trigger `EditorUtility.SetDirty()` for asset saving
- Mouse events consumed with `Event.current.Use()`
- Coordinate transforms isolated in helper methods

### Debugging Tips
- Enable "Show Grid" to verify coordinate system orientation
- Check pivot point is centered on rotation axis
- Verify muzzle points align with barrel geometry
- Test zoom/pan if handles not responding to input
- Ensure turret sprite matches actual asset dimensions
