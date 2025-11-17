---
tags: [script, ui, utility, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ReadOnlyTextField.cs
status: ✅ IMPLEMENTED
size: 3.3 KB
---

# ReadOnlyTextField.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/ReadOnlyTextField.cs`
**Size**: 3.3 KB
**Dependencies**: TMPro

---

## Purpose
Utility component that makes TMP_InputField or TextMeshProUGUI components read-only (non-editable).

Simple helper for converting editable text fields into display-only labels while preserving text field styling. Useful for status displays, calculated values, and information labels.

---

## Implements GDD Features
- [[GDD-UI-Text-Utilities]] - Text field utility components
- [[GDD-UI-Status-Display]] - Read-only status information fields

---

## Key Components

### Public Properties
```
isReadOnly (bool): Current read-only state
textComponent (Component): Reference to TMP_InputField or TextMeshProUGUI
```

### Public Methods
- `SetReadOnly(bool readOnly)` - Toggle read-only state
- `SetText(string text)` - Update displayed text content
- `GetText()` - Retrieve current text content

---

## Configuration

### Inspector Fields
```
[Header("Component Reference")]
textComponent (Component): TMP_InputField or TextMeshProUGUI to make read-only

[Header("Settings")]
readOnlyOnStart (bool, true): Apply read-only on Start()
allowSelection (bool, false): Allow text selection when read-only
```

---

## Integration Points

### Dependencies (What This Needs)
- TMPro - TextMeshPro text components (TMP_InputField, TextMeshProUGUI)

### Used By (What Uses This)
- [[ShipDebugUI]] - Read-only debug information display
- [[ShipDebugUIManager]] - Status field displays
- [[ControlsHelpManager]] - Read-only controls help text
- [[StatisticsPanel]] - Game statistics display
- [[InfoPanel]] - Information labels and descriptions

---

## Technical Details

### Performance Considerations
- No Update/FixedUpdate overhead
- SetReadOnly called once on initialization
- Minimal memory footprint
- No frame-by-frame processing

### Component Support
Automatically detects and supports:
- TMP_InputField - Sets interactable = false, readOnly = true
- TextMeshProUGUI - Already read-only by default, no action needed

---

## How It Works

### Initialization
On Start, auto-detects component type (TMP_InputField or TextMeshProUGUI). If readOnlyOnStart is true, applies read-only state immediately.

### SetReadOnly Implementation
For TMP_InputField: Sets `interactable = false` and `readOnly = true`. Optionally allows text selection via `selectionColor` and `selectOnClick` properties.

For TextMeshProUGUI: No action needed (inherently read-only), but SetText/GetText still functional.

---

## Example Usage
```csharp
// Add to TMP_InputField
var readOnlyField = inputField.AddComponent<ReadOnlyTextField>();

// Set text programmatically
readOnlyField.SetText("Status: Active");

// Toggle read-only state
readOnlyField.SetReadOnly(true); // Make read-only
readOnlyField.SetReadOnly(false); // Make editable again

// Get current text
string currentText = readOnlyField.GetText();
```

---

## Related Files
- [[ShipDebugUI]] - Uses read-only fields for debug display
- [[ShipDebugUIManager]] - Uses read-only fields for telemetry
- [[ControlsHelpManager]] - Uses read-only field for controls help
- [[GDD-UI-Text-Utilities]] - Design specification for UI text utilities

---

## Testing Notes
- TMP_InputField read-only state verified
- TextMeshProUGUI compatibility confirmed
- SetText/GetText methods tested
- Read-only toggle tested at runtime
- Text selection behavior tested (allow/disallow)
- Integration tested with MUIP CustomInputField
- No console warnings or errors during state changes

**Use Cases**:
- Status displays that look like input fields
- Calculated values in forms
- Information labels with input field styling
- Debug telemetry displays
- Read-only configuration values

---

## Changelog
- **2024-01**: Initial implementation with TMP_InputField support
- **2024-02**: Added TextMeshProUGUI fallback support
- **2024-03**: Added text selection configuration option
