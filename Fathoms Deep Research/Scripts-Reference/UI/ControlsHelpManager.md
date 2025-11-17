---
tags: [script, ui, utility, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ControlsHelpManager.cs
status: ✅ IMPLEMENTED
size: 3.5 KB
---

# ControlsHelpManager.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/ControlsHelpManager.cs`
**Size**: 3.5 KB
**Dependencies**: TMPro, Michsky.MUIP (optional)

---

## Purpose
Manages the F1 controls help panel displaying configurable keybindings for all game controls.

Auto-generates formatted help text from serialized keybinding data. Supports both MUIP CustomInputField and standard TextMeshPro components for flexible UI integration.

---

## Implements GDD Features
- [[GDD-UI-Controls-Help]] - In-game controls reference panel (F1 key)
- [[GDD-Accessibility-Keyboard]] - Keyboard-accessible help system
- [[GDD-UI-Configuration]] - Configurable keybinding display

---

## Key Components

### Public Properties
```
helpPanel (GameObject): The panel to show/hide on F1
controlsTextField (TMP_InputField or TextMeshProUGUI): Text field for controls display
controlBindings (List<ControlBinding>): Configurable keybinding list
```

### Public Methods
- `ToggleHelpPanel()` - Show/hide controls panel
- `RefreshControlsText()` - Regenerate help text from bindings
- `UpdateBinding(string action, string key)` - Modify keybinding at runtime

### Key Private Methods
- `GenerateHelpText()` - Formats bindings into readable text
- `DetectTextFieldType()` - Auto-detect MUIP vs standard TMP components

---

## Configuration

### Inspector Fields
```
[Header("UI References")]
helpPanel (GameObject): Panel to toggle on F1 press
controlsTextField (Component): TMP_InputField or TextMeshProUGUI

[Header("Keybindings")]
controlBindings (List<ControlBinding>): Control action and key pairs

[Header("Settings")]
toggleKey (KeyCode, F1): Key to show/hide panel
autoGenerateOnStart (bool, true): Generate help text on Start()
```

### ControlBinding Structure
```
action (string): Description of the control (e.g., "Move Forward")
key (string): Key name (e.g., "W", "Left Click", "Shift")
category (string): Group (e.g., "Movement", "Camera", "UI")
```

---

## Integration Points

### Dependencies (What This Needs)
- TMPro - TextMeshPro text fields for display
- Michsky.MUIP - CustomInputField component (optional)
- Unity Input System - F1 key detection

### Used By (What Uses This)
- [[GameUIManager]] - Coordinates with other UI panels
- [[InputRebindingManager]] - Updates bindings when user remaps keys
- [[PauseMenuController]] - Accessible from pause menu

---

## Technical Details

### Performance Considerations
- Help text generated once on Start, cached for display
- F1 key polled in Update (lightweight check)
- No frame-by-frame updates when panel closed
- Minimal memory footprint

### Text Formatting
- Groups controls by category (Movement, Navigation, Camera, UI)
- Left-aligns action names, right-aligns key names
- Adds spacing between categories
- Supports multi-line format for readability

---

## How It Works

### Initialization
On Start, auto-detects text field component type (MUIP CustomInputField vs TMP_InputField vs TextMeshProUGUI). Generates formatted help text from controlBindings list and caches it.

### Main Loop
Update method checks for F1 key press. On press, toggles helpPanel visibility. No processing when panel is closed.

### Key Algorithms
**Text Generation**: Iterates through controlBindings, groups by category, formats as "Action Name ..... Key Name". Adds section headers and spacing for readability.

**Component Detection**: Checks for MUIP CustomInputField first, falls back to TMP_InputField, then TextMeshProUGUI. Sets text using appropriate API for detected type.

---

## Example Usage
```csharp
// Configure in Inspector or via code
var helpManager = GetComponent<ControlsHelpManager>();

// Add custom keybinding
helpManager.controlBindings.Add(new ControlBinding {
    action = "Toggle Minimap",
    key = "M",
    category = "UI"
});

// Refresh display
helpManager.RefreshControlsText();

// Programmatically show panel
helpManager.ToggleHelpPanel();
```

---

## Related Files
- [[InputRebindingManager]] - Updates bindings when user remaps controls
- [[GameUIManager]] - Manages UI panel hierarchy
- [[MenuKeyboardNavigation]] - Keyboard navigation for help panel
- [[GDD-Controls-Help]] - Design specification for controls help system

---

## Testing Notes
- F1 toggle tested in all game states (menu, gameplay, pause)
- Text formatting verified with short and long action names
- MUIP CustomInputField integration tested
- Standard TMP_InputField fallback tested
- TextMeshProUGUI text component tested
- All control categories (movement, navigation, camera, UI) displayed
- Multi-line text wrapping verified
- Panel visibility toggle confirmed

---

## Changelog
- **2024-01**: Initial implementation with F1 toggle
- **2024-02**: Added auto-generation of help text from bindings
- **2024-03**: Added MUIP CustomInputField support
- **2024-04**: Added category grouping and improved formatting
