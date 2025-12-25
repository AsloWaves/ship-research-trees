---
tags: [script, ui, accessibility, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/MenuKeyboardNavigation.cs
status: ✅ IMPLEMENTED
size: 2.4 KB
---

# MenuKeyboardNavigation.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/MenuKeyboardNavigation.cs`
**Size**: 2.4 KB
**Dependencies**: UnityEngine.UI, UnityEngine.EventSystems, Michsky.MUIP

---

## Purpose
Provides ADA-compliant keyboard navigation for menu panels following WCAG 2.1 AA accessibility standards.

Enables full keyboard control of UI panels using Tab, Arrow keys, Enter, and Escape. Supports automatic focus management, wrap-around navigation, and visual/audio feedback for enhanced accessibility and user experience.

---

## Implements GDD Features
- [[GDD-UI-Accessibility]] - WCAG 2.1 AA compliance for keyboard navigation
- [[GDD-UI-Navigation]] - Menu navigation system with keyboard support
- [[GDD-Accessibility-Standards]] - ADA-compliant interface controls

---

## Key Components

### Public Properties
```
enableVisualFeedback (bool): Enable scale/color feedback on focus
enableAudioFeedback (bool): Enable audio cues on navigation
wrapNavigation (bool): Allow wrap-around at list boundaries
```

### Public Methods
- `SetNavigableElements(List<Selectable>)` - Define navigable UI elements
- `FocusElement(int index)` - Set focus to specific element by index
- `EnableNavigation(bool)` - Toggle keyboard navigation system
- `ResetFocus()` - Return focus to first element

### Key Private Methods
- `HandleTabNavigation()` - Tab/Shift+Tab for sequential navigation
- `HandleArrowNavigation()` - Arrow keys for directional navigation
- `HandleActivation()` - Enter/Space to activate focused element
- `HandleEscape()` - Escape key to cancel or go back
- `ApplyFocusFeedback()` - Visual highlight on focused element

---

## Configuration

### Inspector Fields
```
[Header("Navigation Settings")]
autoFocusOnEnable (bool, true): Auto-focus first element when panel activates
tabNavigationEnabled (bool, true): Enable Tab key navigation
arrowNavigationEnabled (bool, true): Enable Arrow key navigation
wrapNavigation (bool, true): Wrap to first/last on boundaries

[Header("Visual Feedback")]
enableVisualFeedback (bool, true): Show visual highlight on focus
focusScale (float, 1.05f): Scale multiplier for focused element
focusColor (Color, yellow): Tint color for focused element

[Header("Audio Feedback")]
enableAudioFeedback (bool, false): Play audio on navigation
navigationSound (AudioClip): Sound effect for navigation events
activationSound (AudioClip): Sound effect for element activation
```

---

## Integration Points

### Dependencies (What This Needs)
- Unity UI System - Selectable components for navigation
- Unity Event System - Input detection and focus management
- Michsky MUIP - Modern UI components (optional, graceful fallback)
- Unity Audio - Audio feedback (optional)

### Used By (What Uses This)
- [[MainMenuManager]] - Main menu keyboard navigation
- [[SettingsPanel]] - Settings menu accessibility
- [[PauseMenuController]] - In-game pause menu navigation
- [[ShipCustomizationUI]] - Ship configuration interface

---

## Technical Details

### Performance Considerations
- Update method checks input every frame (lightweight)
- No memory allocations during navigation
- Caches Selectable components on initialization
- Efficient input polling without delegates

### Accessibility Standards
- WCAG 2.1 AA compliant keyboard navigation
- Supports Tab, Shift+Tab, Arrow keys, Enter, Escape
- Visual focus indicators for screen visibility
- Audio feedback support for screen readers
- Focus trap within modal dialogs
- Logical tab order maintenance

---

## How It Works

### Initialization
On Enable, caches all Selectable UI elements in the panel and optionally auto-focuses the first element. Validates navigation graph structure and establishes wrap-around boundaries.

### Main Loop
Update method polls keyboard input every frame. Detects Tab, Arrow keys, Enter, and Escape. Routes input to appropriate navigation handler and updates visual/audio feedback accordingly.

### Key Algorithms
**Tab Navigation**: Moves focus sequentially through Selectable list. Shift+Tab reverses direction. Wraps to beginning/end if enabled.

**Arrow Navigation**: Moves focus based on spatial relationship of UI elements. Uses Unity's navigation graph for Up/Down/Left/Right movement.

**Focus Feedback**: Applies scale and color tint to focused element. Restores previous element to normal state. Plays optional audio cue.

---

## Example Usage
```csharp
// Add to menu panel GameObject
var keyboardNav = menuPanel.AddComponent<MenuKeyboardNavigation>();

// Configure navigation
keyboardNav.autoFocusOnEnable = true;
keyboardNav.wrapNavigation = true;
keyboardNav.enableVisualFeedback = true;

// Manually set focus if needed
keyboardNav.FocusElement(0); // Focus first button

// Toggle navigation on/off
keyboardNav.EnableNavigation(true);
```

---

## Related Files
- [[MainMenuManager]] - Uses keyboard navigation for main menu
- [[UIInputManager]] - Coordinates input across UI systems
- [[AccessibilitySettings]] - User preferences for accessibility features
- [[GDD-Accessibility]] - Design specification for accessibility requirements

---

## Testing Notes
- Tested with Tab and Shift+Tab across all menu panels
- Arrow key navigation verified in grid and list layouts
- Wrap-around behavior tested at boundaries
- Enter key activation confirmed for buttons and toggles
- Escape key tested in nested modal dialogs
- Visual feedback tested with color-blind simulation
- Audio feedback tested with screen reader software
- WCAG 2.1 AA compliance validated with accessibility auditor

---

## Changelog
- **2024-01**: Initial implementation with WCAG 2.1 AA compliance
- **2024-02**: Added visual feedback system with scale and color
- **2024-03**: Added audio feedback support for screen readers
- **2024-04**: Improved arrow key navigation with spatial awareness
