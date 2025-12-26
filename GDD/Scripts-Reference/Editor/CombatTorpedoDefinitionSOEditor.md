# CombatTorpedoDefinitionSOEditor.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/CombatTorpedoDefinitionSOEditor.cs` |
| **Namespace** | `WOS.Combat.Editor` |
| **Inheritance** | `UnityEditor.Editor` |
| **Lines** | 549 |
| **Architecture** | Custom Editor for Torpedo Ammunition Geometry |

## Purpose

Custom Unity Editor for `Combat.TorpedoDefinitionSO` ScriptableObjects that configures torpedo ammunition geometry (not launchers). Provides interactive visual editor for positioning warhead tips, effect spawn points, and collision geometry. Part of the Combat namespace system for ammunition definitions, separate from the launcher equipment system.

## Key Features

### Visual Geometry Editor
- **Interactive Preview**: Top-down 2D view with grid and zoom/pan controls
- **Draggable Points**: Yellow warhead tip and green effect spawn points
- **Sprite Preview**: Optional torpedo sprite overlay for visual reference
- **Grid System**: Configurable grid with snap-to-grid functionality
- **Presets**: Quick position templates for common torpedo types

### Editor Controls
- **Zoom**: Mouse wheel (2x to 0.25x range)
- **Pan**: Right-click drag
- **Grid Toggle**: Show/hide alignment grid
- **Grid Snap**: Snap points to grid intersections
- **Reset View**: Return to default zoom/pan state

### Torpedo Geometry Configuration
- **Warhead Tip**: Impact/detonation point (yellow)
- **Effect Spawns**: Particle effect and trail positions (green)
- **Collision Shape**: Physics collision geometry
- **Visual Feedback**: Color-coded handles with labels

## Configuration Tables

### Torpedo Type Presets
| Preset | Warhead Tip | Effect Points | Use Case |
|--------|-------------|---------------|----------|
| Standard | (0, 0.8) | Trail at (0, -0.5) | Basic torpedoes |
| Long Lance | (0, 1.0) | Trail at (0, -0.7), bubble at (0, -0.6) | Japanese oxygen torpedoes |
| Mk14 | (0, 0.9) | Trail at (0, -0.6) | US Navy torpedoes |
| Acoustic | (0, 0.85) | Trail at (0, -0.5), sonar at (0, 0) | Homing torpedoes |

### Color Scheme
| Element | Color | Purpose |
|---------|-------|---------|
| Warhead Tip | Yellow | Impact/detonation point |
| Effect Spawns | Green | VFX positions |
| Grid Lines | Light Gray | Alignment guide |
| Selection | Cyan | Active handle |

### Torpedo Classes
| Class | Description | Typical Configuration |
|-------|-------------|----------------------|
| Surface | Anti-ship torpedoes | Standard warhead + trail |
| ASW | Anti-submarine | Acoustic homing + sonar |
| Wakeless | Oxygen torpedoes | Long range + minimal trail |
| Practice | Training rounds | No warhead, smoke trail |

## Key Code Snippets

### Visual Preview Section
```csharp
private void DrawVisualPreview()
{
    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Torpedo Ammunition Geometry Editor", EditorStyles.boldLabel);

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
    DrawTorpedoGeometry(previewRect);

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Creates the main preview UI with controls for grid visibility, snapping, and view reset.

### Interactive Torpedo Editor
```csharp
private void DrawTorpedoGeometry(Rect rect)
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

    // Draw torpedo sprite if available
    if (torpedoDef.torpedoSprite != null && showSprite)
    {
        DrawSpritePreview(rect, center, scale);
    }

    // Draw and handle warhead tip point (yellow)
    Vector2 warheadScreen = WorldToScreen(torpedoDef.warheadTip, center, scale);
    if (DrawHandle(warheadScreen, Color.yellow, "Warhead Tip"))
    {
        torpedoDef.warheadTip = ScreenToWorld(Event.current.mousePosition, center, scale);
        MarkDirty();
    }

    // Draw and handle effect spawn points (green)
    for (int i = 0; i < torpedoDef.effectSpawnPoints.Count; i++)
    {
        Vector2 effectScreen = WorldToScreen(torpedoDef.effectSpawnPoints[i], center, scale);
        string label = i == 0 ? "Trail" : $"Effect {i}";
        if (DrawHandle(effectScreen, Color.green, label))
        {
            torpedoDef.effectSpawnPoints[i] = ScreenToWorld(Event.current.mousePosition, center, scale);
            MarkDirty();
        }
    }

    Handles.EndGUI();
}
```

**Purpose**: Main torpedo geometry rendering loop with coordinate transforms, sprite overlay, and interactive point manipulation.

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
    Undo.RecordObject(torpedoDef, "Apply Torpedo Ammunition Preset");

    torpedoDef.effectSpawnPoints.Clear();

    switch (presetName)
    {
        case "Standard":
            torpedoDef.warheadTip = new Vector2(0f, 0.8f);
            torpedoDef.effectSpawnPoints.Add(new Vector2(0f, -0.5f)); // Trail
            break;
        case "Long Lance":
            torpedoDef.warheadTip = new Vector2(0f, 1.0f);
            torpedoDef.effectSpawnPoints.Add(new Vector2(0f, -0.7f)); // Trail
            torpedoDef.effectSpawnPoints.Add(new Vector2(0f, -0.6f)); // Bubble wake
            break;
        case "Mk14":
            torpedoDef.warheadTip = new Vector2(0f, 0.9f);
            torpedoDef.effectSpawnPoints.Add(new Vector2(0f, -0.6f)); // Trail
            break;
        case "Acoustic":
            torpedoDef.warheadTip = new Vector2(0f, 0.85f);
            torpedoDef.effectSpawnPoints.Add(new Vector2(0f, -0.5f)); // Trail
            torpedoDef.effectSpawnPoints.Add(new Vector2(0f, 0f));    // Sonar ping
            break;
    }

    EditorUtility.SetDirty(torpedoDef);
}
```

**Purpose**: Applies predefined torpedo ammunition configurations with undo support.

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

**Purpose**: Converts between world coordinates (torpedo local space) and screen coordinates (editor preview space) with optional grid snapping.

## Public API

### Unity Menu Items
None - this is a CustomEditor that appears automatically in the Inspector when a `Combat.TorpedoDefinitionSO` asset is selected.

### Inspector Actions
| Button | Action |
|--------|--------|
| Apply Preset → Standard | Configure standard torpedo |
| Apply Preset → Long Lance | Configure Japanese oxygen torpedo |
| Apply Preset → Mk14 | Configure US Navy torpedo |
| Apply Preset → Acoustic | Configure homing torpedo |
| Add Effect Spawn | Add new VFX position |
| Remove Effect Spawn | Delete last VFX position |

## Usage Examples

### Creating a New Torpedo Ammunition Type
1. Create torpedo asset: `Create > WOS > Combat > Torpedo Definition`
2. Select asset in Project window
3. In Inspector, scroll to "Torpedo Ammunition Geometry Editor" section
4. Click "Apply Preset → Long Lance" for oxygen torpedo configuration
5. Adjust warhead tip (yellow) by dragging to impact point
6. Fine-tune effect spawn points (green) by dragging
7. Enable "Show Grid" and "Snap to Grid" for precise alignment
8. Assign torpedo sprite for visual reference
9. Configure remaining properties (damage, speed, range, etc.)

### Custom Torpedo Configuration
```csharp
// Manually configure custom torpedo ammunition
var torpedo = CreateInstance<Combat.TorpedoDefinitionSO>();
torpedo.warheadTip = new Vector2(0f, 0.9f); // Impact point at nose
torpedo.effectSpawnPoints.Clear();
torpedo.effectSpawnPoints.Add(new Vector2(0f, -0.6f)); // Main trail
torpedo.effectSpawnPoints.Add(new Vector2(-0.1f, -0.5f)); // Port trail
torpedo.effectSpawnPoints.Add(new Vector2(0.1f, -0.5f)); // Starboard trail
```

### Adjusting Existing Geometry
1. Select torpedo ammunition asset
2. In Torpedo Ammunition Geometry Editor, enable "Show Grid"
3. Drag warhead tip to desired impact point
4. Drag each effect spawn point to VFX position
5. Use zoom/pan for fine adjustments
6. Changes save automatically

## Integration Points

### Dependencies
- **Combat.TorpedoDefinitionSO**: The ScriptableObject being edited (Combat namespace)
- **UnityEditor.Handles**: For 2D drawing in preview
- **UnityEditor.Undo**: For undo/redo support

### Related Systems
- **TorpedoDefinitionSO** (Equipment): Launcher geometry (separate namespace)
- **Combat System**: Uses warhead tip for collision detection
- **VFX System**: Uses effect spawn points for particle systems
- **Physics System**: Uses collision geometry for impact detection
- **Damage System**: Warhead tip determines damage application point

### Data Flow
```
CombatTorpedoDefinitionSOEditor (ammunition geometry)
    → Combat.TorpedoDefinitionSO (asset)
    → TorpedoController (runtime torpedo)
    → Collision System (warhead impact)
    → VFX System (trail/bubble effects)
    → Damage System (explosion application)
```

## Design Notes

### Architectural Decisions
- **Combat Namespace**: Separate from equipment system (ammunition vs launcher)
- **Visual-First Design**: Immediate visual feedback reduces trial-and-error
- **Preset System**: Historical torpedo types as starting points
- **Effect Flexibility**: Multiple effect spawns for complex VFX
- **Color Coding**: Yellow warhead (critical) vs green effects (visual)

### Performance Considerations
- Preview renders only when Inspector is visible
- Handle interaction uses event-based input (not polling)
- Grid drawing optimized for typical zoom ranges
- Sprite preview cached and reused

### Namespace Architecture
- **WOS.Combat**: Ammunition definitions (this editor)
- **WOS**: Equipment definitions (launcher editor)
- **Separation Rationale**: Ammunition independent of launcher type

### Limitations
- 2D preview only (top-down view)
- No 3D depth visualization for submerged torpedoes
- Grid size fixed at 0.1 units
- Maximum zoom constrained to prevent performance issues
- No trajectory preview or ballistics simulation

### Future Enhancements
- Torpedo trajectory preview
- Warhead explosion radius visualization
- Effect preview (show actual particle systems)
- Copy/paste geometry between torpedo types
- Custom preset saving
- Multi-torpedo batch editing
- Export geometry to JSON
- Import from external modeling tools
- Acoustic homing cone visualization
- Depth settings for submarine launches

### Common Patterns
- All geometry edits wrapped in `Undo.RecordObject()`
- Changes trigger `EditorUtility.SetDirty()` for asset saving
- Mouse events consumed with `Event.current.Use()`
- Coordinate transforms isolated in helper methods
- Same visual architecture as weapon editors for consistency

### Debugging Tips
- Enable "Show Grid" to verify coordinate system orientation
- Check warhead tip is at torpedo nose (impact point)
- Verify effect points align with expected VFX positions
- Test zoom/pan if handles not responding to input
- Ensure torpedo sprite matches actual asset dimensions
- Check effect spawn spacing for realistic particle placement
- Verify warhead tip is forward-facing (positive Y)
