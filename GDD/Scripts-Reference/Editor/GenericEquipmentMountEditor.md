# GenericEquipmentMountEditor.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Editor/GenericEquipmentMountEditor.cs` |
| **Namespace** | `WOS.Editor` |
| **Inheritance** | `UnityEditor.Editor` |
| **Lines** | 143 |
| **Architecture** | Custom Editor for Equipment Mount Configuration |

## Purpose

Custom Unity Editor for `GenericEquipmentMount` components that provides visual feedback for equipment mount status and quick rotation presets for common naval weapon arcs. Simplifies configuration of weapon mounting points on ships with predefined arc presets (Bow, Wing, Broadside, 360°).

## Key Features

### Visual Status Display
- **Mount Status**: Displays current equipment mount state (Empty, Equipped, Disabled)
- **Equipment Info**: Shows mounted equipment details when equipped
- **Color Coding**: Visual feedback for mount status
- **Rotation Display**: Current rotation limits shown

### Rotation Presets
- **Bow Guns**: ±30° arc (forward-facing armament)
- **Wing Guns**: ±90° arc (limited traverse)
- **Broadside Guns**: ±150° arc (wide traverse)
- **360° Turrets**: Full rotation capability
- **Custom**: Manual rotation limit configuration

### Quick Configuration
- **One-Click Presets**: Apply common configurations instantly
- **Visual Feedback**: Immediate preview of rotation limits
- **Undo Support**: All preset changes reversible

## Configuration Tables

### Rotation Arc Presets
| Preset | Min Rotation | Max Rotation | Use Case |
|--------|--------------|--------------|----------|
| Bow | -30° | +30° | Forward-facing guns (A turret, bow casemates) |
| Wing | -90° | +90° | Side-mounted guns (wing turrets) |
| Broadside | -150° | +150° | Main battery with wide arc |
| 360° | -180° | +180° | Centerline turrets with full rotation |

### Mount Status Colors
| Status | Color | Description |
|--------|-------|-------------|
| Empty | Gray | No equipment mounted |
| Equipped | Green | Equipment mounted and functional |
| Disabled | Red | Mount disabled or equipment broken |
| Invalid | Yellow | Configuration error |

### Common Naval Mounting Positions
| Position | Typical Preset | Description |
|----------|---------------|-------------|
| A Turret | Bow | Forward-most main turret |
| B Turret | 360° | Forward centerline turret |
| X Turret | 360° | Aft centerline turret |
| Y Turret | Bow (aft-facing) | Stern-most main turret |
| Casemates | Wing/Broadside | Side-mounted secondary guns |
| AA Mounts | 360° | Anti-aircraft batteries |

## Key Code Snippets

### Status Display
```csharp
public override void OnInspectorGUI()
{
    serializedObject.Update();

    GenericEquipmentMount mount = (GenericEquipmentMount)target;

    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Equipment Mount Status", EditorStyles.boldLabel);

    // Status display
    GUIStyle statusStyle = new GUIStyle(EditorStyles.label);
    statusStyle.fontStyle = FontStyle.Bold;

    if (mount.IsEmpty)
    {
        statusStyle.normal.textColor = Color.gray;
        EditorGUILayout.LabelField("Status: Empty", statusStyle);
    }
    else if (mount.IsEquipped)
    {
        statusStyle.normal.textColor = Color.green;
        EditorGUILayout.LabelField("Status: Equipped", statusStyle);
        EditorGUILayout.LabelField($"Equipment: {mount.EquippedItem.equipmentName}");
        EditorGUILayout.LabelField($"Type: {mount.EquippedItem.GetType().Name}");
    }
    else
    {
        statusStyle.normal.textColor = Color.red;
        EditorGUILayout.LabelField("Status: Disabled", statusStyle);
    }

    EditorGUILayout.EndVertical();

    EditorGUILayout.Space();

    // Draw default inspector
    DrawDefaultInspector();

    EditorGUILayout.Space();

    // Rotation presets
    DrawRotationPresets();

    serializedObject.ApplyModifiedProperties();
}
```

**Purpose**: Displays mount status with color-coded feedback and equipment details.

### Rotation Preset Buttons
```csharp
private void DrawRotationPresets()
{
    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Rotation Arc Presets", EditorStyles.boldLabel);

    EditorGUILayout.BeginHorizontal();

    if (GUILayout.Button("Bow (±30°)", GUILayout.Height(25)))
    {
        ApplyRotationPreset(-30f, 30f);
    }

    if (GUILayout.Button("Wing (±90°)", GUILayout.Height(25)))
    {
        ApplyRotationPreset(-90f, 90f);
    }

    EditorGUILayout.EndHorizontal();

    EditorGUILayout.BeginHorizontal();

    if (GUILayout.Button("Broadside (±150°)", GUILayout.Height(25)))
    {
        ApplyRotationPreset(-150f, 150f);
    }

    if (GUILayout.Button("360° Rotation", GUILayout.Height(25)))
    {
        ApplyRotationPreset(-180f, 180f);
    }

    EditorGUILayout.EndHorizontal();

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Provides one-click buttons to apply common rotation arc configurations.

### Preset Application
```csharp
private void ApplyRotationPreset(float minRotation, float maxRotation)
{
    GenericEquipmentMount mount = (GenericEquipmentMount)target;

    Undo.RecordObject(mount, "Apply Rotation Preset");

    SerializedProperty minProp = serializedObject.FindProperty("minRotation");
    SerializedProperty maxProp = serializedObject.FindProperty("maxRotation");

    minProp.floatValue = minRotation;
    maxProp.floatValue = maxRotation;

    serializedObject.ApplyModifiedProperties();
    EditorUtility.SetDirty(mount);

    Debug.Log($"Applied rotation preset: {minRotation}° to {maxRotation}°");
}
```

**Purpose**: Applies rotation preset with undo support and serialized property updates.

### Current Rotation Display
```csharp
private void DrawCurrentRotation()
{
    GenericEquipmentMount mount = (GenericEquipmentMount)target;

    EditorGUILayout.BeginVertical(EditorStyles.helpBox);
    EditorGUILayout.LabelField("Current Configuration", EditorStyles.boldLabel);

    float minRot = serializedObject.FindProperty("minRotation").floatValue;
    float maxRot = serializedObject.FindProperty("maxRotation").floatValue;
    float arcSize = maxRot - minRot;

    EditorGUILayout.LabelField($"Rotation Arc: {arcSize}° ({minRot}° to {maxRot}°)");

    // Visual arc indicator
    Rect rect = GUILayoutUtility.GetRect(100, 20);
    DrawArcIndicator(rect, minRot, maxRot);

    EditorGUILayout.EndVertical();
}
```

**Purpose**: Displays current rotation limits and visual arc indicator.

## Public API

### Unity Menu Items
None - this is a CustomEditor that appears automatically in the Inspector when a `GenericEquipmentMount` component is selected.

### Inspector Actions
| Button | Function |
|--------|----------|
| Bow (±30°) | Apply bow gun rotation arc |
| Wing (±90°) | Apply wing gun rotation arc |
| Broadside (±150°) | Apply broadside rotation arc |
| 360° Rotation | Apply full rotation capability |

## Usage Examples

### Configuring Ship Equipment Mounts

**Forward Main Turret (A Turret)**:
1. Select ship prefab in Hierarchy
2. Find "A Turret Mount" component in Inspector
3. Click "Bow (±30°)" preset
4. Verify rotation arc: -30° to +30°

**Centerline Turret (B/X Turret)**:
1. Select ship prefab
2. Find "B Turret Mount" component
3. Click "360° Rotation" preset
4. Verify rotation arc: -180° to +180°

**Side Casemate Guns**:
1. Select ship prefab
2. Find casemate mount components
3. Click "Wing (±90°)" or "Broadside (±150°)" preset
4. Verify arc matches historical configuration

### Custom Arc Configuration
```csharp
// Manually configure non-standard arc
var mount = GetComponent<GenericEquipmentMount>();
mount.minRotation = -45f; // Custom minimum
mount.maxRotation = 135f; // Custom maximum
// Results in 180° arc offset to starboard
```

### Programmatic Mount Configuration
```csharp
// Configure mount in script
GenericEquipmentMount mount = gameObject.AddComponent<GenericEquipmentMount>();
mount.minRotation = -90f;
mount.maxRotation = 90f;
mount.equipmentType = EquipmentType.Turret;
mount.mountPosition = new Vector3(0f, 1.5f, 3f);
```

## Integration Points

### Dependencies
- **GenericEquipmentMount**: The component being edited
- **EquipmentDefinitionSO**: Base class for mounted equipment
- **UnityEditor.Undo**: For undo/redo support

### Related Systems
- **ShipConfigurationSO**: Defines ship equipment mount layout
- **TurretDefinitionSO**: Turret equipment that can be mounted
- **TorpedoDefinitionSO**: Torpedo launcher equipment
- **EquipmentDatabaseSO**: Source of available equipment
- **Runtime Equipment System**: Uses mount configuration for gameplay

### Data Flow
```
ShipConfigurationSO (defines mount positions)
    → GenericEquipmentMount (mount component)
    → GenericEquipmentMountEditor (configuration UI)
    → Runtime Equipment System (mount behavior)
    → Combat System (firing arcs)
```

## Design Notes

### Architectural Decisions
- **Visual Status**: Immediate feedback on mount configuration
- **Preset System**: Common configurations accessible with one click
- **Color Coding**: Intuitive status display (gray/green/red)
- **Naval Terminology**: Presets use historical naval naming

### Performance Considerations
- Editor-only code (zero runtime overhead)
- Status checks only when Inspector is visible
- Minimal GUI allocations
- Undo system properly integrated

### Historical Accuracy
- **Bow Preset**: Based on WWI-WWII forward turret limitations
- **Wing Preset**: Typical casemate gun arcs
- **Broadside Preset**: Battleship main battery coverage
- **360° Preset**: Modern or centerline turret capability

### Limitations
- No visualization of firing arc in Scene view
- No collision detection with ship superstructure
- Preset angles are approximations
- No elevation angle configuration
- Manual arc configuration still requires direct property editing

### Future Enhancements
- Scene view arc visualization (gizmos)
- Collision detection with ship geometry
- Elevation angle presets (AA guns)
- Custom preset saving
- Batch configure multiple mounts
- Import/export mount configurations
- Historical ship templates (Iowa-class, etc.)
- Arc validation against ship model
- Visual arc editor (similar to turret geometry editor)
- Equipment compatibility warnings

### Common Patterns
- All preset changes wrapped in `Undo.RecordObject()`
- Changes trigger `EditorUtility.SetDirty()`
- Status display uses color-coded labels
- SerializedProperty used for undo-compatible changes
- Default inspector still accessible below custom UI

### Debugging Tips
- Check mount status color for configuration issues
- Verify rotation arc makes sense for mount position
- Test rotation in Play mode to verify behavior
- Check for conflicts with ship superstructure
- Ensure equipment type matches mount configuration
- Verify mount position is on ship mesh
