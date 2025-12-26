# DebugSettingsDrawer

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Debugging/DebugSettingsDrawer.cs` |
| **Namespace** | `WOS.Debugging` |
| **Inheritance** | `PropertyDrawer` |
| **Lines** | 149 |
| **Platform** | **Editor Only** (`#if UNITY_EDITOR`) |
| **Architecture** | Custom Unity Inspector property drawer |

## Purpose

Custom property drawer for `DebugSettings` to improve Inspector layout. Fixes checkbox overlap issues and provides better visual organization with color-coded categories and section headers.

## Features

### Visual Organization

```csharp
// Three organized sections:
1. Core Systems (5 categories)
   - Ship Physics & Movement
   - Ocean Tiles & Wake Effects
   - Environment & Ports
   - Camera & Visual Effects
   - Input & Controls

2. Technical Systems (3 categories)
   - Physics Calculations
   - Performance Metrics
   - System Core & Initialization

3. Game Features (4 categories)
   - User Interface & HUD
   - Economy & Trading
   - Audio & Sound Effects
   - Networking & Multiplayer
```

### Checkbox Alignment Fix

```csharp
// Proper checkbox positioning (left-aligned)
Checkbox Width: 20px
Spacing: 2px
Label Width: Remaining space

// Before: Checkboxes overlapped labels
// After: Clean left-aligned checkboxes with proper spacing
```

### Color-Coded Labels

```csharp
// Active categories: Bold + Category Color
// Inactive categories: Normal + Gray

Color Examples:
Ship:        Green (#4CAF50)
Ocean:       Blue (#2196F3)
Performance: Yellow (#FFEB3B)
Networking:  Blue Gray (#607D8B)
```

## Layout Constants

| Constant | Value | Purpose |
|----------|-------|---------|
| `CHECKBOX_WIDTH` | `20f` | Width of checkbox controls |
| `SPACING` | `2f` | Spacing between elements |
| `HEADER_HEIGHT` | `18f` | Height of section headers |
| `LINE_HEIGHT` | `18f` | Height of each category line |

## Public API

### PropertyDrawer Methods

#### `OnGUI(position, property, label)`
```csharp
public override void OnGUI(Rect position, SerializedProperty property, GUIContent label)
```

Draws the custom DebugSettings Inspector UI.

**Visual Structure**:
1. Main header: "Debug Categories"
2. Section headers: "Core Systems", "Technical Systems", "Game Features"
3. Category toggles: Checkbox + Label (color-coded)

#### `GetPropertyHeight(property, label)`
```csharp
public override float GetPropertyHeight(SerializedProperty property, GUIContent label)
```

Calculates total height needed for the property drawer.

**Calculation**:
```
Total Height = Header + CoreSystems + Technical + Features
             = 18 + (18 + 5*20 + 4) + (18 + 3*20 + 4) + (18 + 4*20)
             ≈ 222 pixels
```

## Usage

### Automatic Application

```csharp
// Automatically applied to DebugSettings fields in Inspector
[CustomPropertyDrawer(typeof(DebugSettings))]

// No manual setup required - Unity applies automatically
```

### DebugManager Inspector

When you select a GameObject with DebugManager, the DebugSettings field will display with:
- Organized sections
- Color-coded categories
- Proper checkbox alignment
- Bold active categories
- Gray inactive categories

## Design Notes

### DrawDebugCategory Helper

```csharp
void DrawDebugCategory(ref float y, string displayName,
                       string propertyName, Color headerColor)
{
    // 1. Get SerializedProperty
    var prop = property.FindPropertyRelative(propertyName);

    // 2. Calculate positions
    Rect checkboxRect = new Rect(position.x, y, CHECKBOX_WIDTH, LINE_HEIGHT);
    Rect labelRect = new Rect(position.x + CHECKBOX_WIDTH + SPACING,
                              y, labelWidth, LINE_HEIGHT);

    // 3. Draw checkbox (left)
    prop.boolValue = EditorGUI.Toggle(checkboxRect, prop.boolValue);

    // 4. Draw label (right, color-coded)
    GUI.color = prop.boolValue ? headerColor : Color.gray;
    var labelStyle = new GUIStyle(EditorStyles.label);
    labelStyle.fontStyle = prop.boolValue ? FontStyle.Bold : FontStyle.Normal;
    EditorGUI.LabelField(labelRect, displayName, labelStyle);

    // 5. Advance y position
    y += LINE_HEIGHT + SPACING;
}
```

### Section Layout

```csharp
// Core Systems Section
EditorGUI.LabelField(rect, "Core Systems", sectionStyle);
DrawDebugCategory(ref yPos, "Ship Physics & Movement", "enableShipDebug", Color.green);
DrawDebugCategory(ref yPos, "Ocean Tiles & Wake Effects", "enableOceanDebug", Color.cyan);
// ... etc
```

### Category Color Mapping

```csharp
Category Colors (same as DebugManager):
Ship:        Green      (#4CAF50)
Ocean:       Cyan       (#2196F3)
Environment: Light Green (#8BC34A)
Camera:      Yellow     (#FF9800)
Input:       Magenta    (#9C27B0)
Physics:     Red        (#F44336)
Performance: Yellow     (#FFEB3B)
System:      Brown      (#795548)
```

## DebugStatsDrawer

Also included in same file:

```csharp
[CustomPropertyDrawer(typeof(DebugStats))]
public class DebugStatsDrawer : PropertyDrawer
```

### Purpose

Displays debug statistics nicely in Inspector:
```
Messages: 45/50 per frame | Categories: 8 enabled | Throttled: 12
```

### Properties Displayed

- `messagesThisFrame`: Current frame message count
- `maxMessagesPerFrame`: Message limit per frame
- `throttledMessages`: Number of throttled messages
- `enabledCategories`: Count of enabled categories

## Integration Points

### DebugManager Integration

```csharp
// DebugManager has DebugSettings field
[SerializeField] private DebugSettings debugSettings = new DebugSettings();

// Drawer automatically applied in Inspector
// User sees:
// ✓ Organized sections
// ✓ Color-coded categories
// ✓ Proper checkbox alignment
```

### Unity Inspector

```csharp
// Unity automatically uses custom drawer when:
// 1. Field type matches [CustomPropertyDrawer] type
// 2. Editor assemblies loaded
// 3. Inspector window refreshed
```

## Before/After Comparison

### Before (Default Drawer)

```
❌ Checkboxes overlap labels
❌ All categories in flat list
❌ No visual organization
❌ Hard to read/scan
❌ No color coding
```

### After (Custom Drawer)

```
✅ Checkboxes left-aligned, no overlap
✅ Organized into 3 sections
✅ Section headers for clarity
✅ Color-coded active/inactive
✅ Bold active categories
✅ Easy to scan and configure
```

## Related Scripts

- **DebugManager**: Uses DebugSettings for category configuration
- **DebugSettings**: Data structure for category toggles (in DebugManager.cs)
- **DebugStats**: Statistics structure also has custom drawer

## Platform Notes

### Editor Only

```csharp
#if UNITY_EDITOR
// ... PropertyDrawer code ...
#endif

// PropertyDrawers ONLY work in Editor
// Not compiled into builds
// No runtime overhead
```

### Inspector Refresh

```csharp
// Inspector updates when:
// - GameObject selected
// - Value changed
// - Inspector window refreshed (Ctrl+R)
// - Unity Editor recompiled
```

## Troubleshooting

### Issue: Custom drawer not showing
**Solution**: Ensure script in Editor folder or uses `#if UNITY_EDITOR`

### Issue: Layout broken
**Solution**: Check CHECKBOX_WIDTH + SPACING + labelWidth calculations

### Issue: Colors not showing
**Solution**: Verify useColorCoding is enabled in DebugManager

### Issue: Height calculation wrong
**Solution**: Update GetPropertyHeight() to match OnGUI() layout

## Best Practices

### Adding New Categories

```csharp
// 1. Add category to DebugSettings (DebugManager.cs)
public bool enableNewCategoryDebug = true;

// 2. Add to appropriate section in drawer
DrawDebugCategory(ref yPos, "New Category Description",
                  "enableNewCategoryDebug", Color.magenta);

// 3. Update GetPropertyHeight() calculation
// Technical (4 items + section header) // was 3
totalHeight += LINE_HEIGHT + (LINE_HEIGHT + SPACING) * 4 + SPACING * 2;
```

### Customizing Colors

```csharp
// Match DebugManager category colors
DrawDebugCategory(ref yPos, "Custom Category",
                  "enableCustomDebug",
                  new Color(0.8f, 0.4f, 0.2f)); // Custom RGB color
```

### Section Organization

```csharp
// Group related categories together
// Use consistent naming conventions
// Keep sections balanced (3-6 items each)
// Order by frequency of use (most common first)
```
