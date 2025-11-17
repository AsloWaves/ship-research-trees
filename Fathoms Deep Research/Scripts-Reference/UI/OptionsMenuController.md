---
tags: [script, ui, menu, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/OptionsMenuController.cs
status: ✅ IMPLEMENTED
size: 2.4 KB (2,387 bytes)
---

# OptionsMenuController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/OptionsMenuController.cs`
**Size**: 2.4 KB (2,387 bytes)
**Dependencies**: UnityEngine, UnityEngine.UI, TMPro (TextMeshProUGUI, TMP_Dropdown)

---

## Purpose
OptionsMenuController provides a placeholder settings menu for future implementation. It will handle audio settings, graphics quality, keybindings, and other player preferences, saving/loading from PlayerPrefs.

**Current Status**: Placeholder implementation - functional but minimal settings. Full settings system planned for Phase 2.

---

## Implements GDD Features
- [[UI-Overview]] - Settings menu UI (future implementation)
- [[Menu-System]] - Options panel navigation

---

## Key Components

### Public Methods
- `LoadSettings()` - Load settings from PlayerPrefs (placeholder)
- `SaveSettings()` - Save settings to PlayerPrefs (placeholder)
- `OnBackButtonClicked()` - Return to previous menu (main menu or in-game menu)

### Key Private Methods
- `ApplySettings()` - Apply loaded settings to game systems (placeholder)
- `ResetToDefaults()` - Reset all settings to default values (placeholder)

---

## Configuration

### Inspector Fields
```csharp
[Header("UI References")]
statusText (TextMeshProUGUI): Status message display
- Type: TextMeshProUGUI
- Purpose: Show save/load feedback
- Optional: Can be null (no status display)

[Header("Buttons")]
backButton (ButtonManager/Button): Return to previous menu
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Navigate back to main/in-game menu
- Callback: OnBackButtonClicked()

[Header("Settings UI (Placeholder)")]
audioSlider (Slider): Master volume control (future)
- Type: Slider
- Purpose: Audio volume adjustment
- Range: 0.0 - 1.0
- PlayerPrefs key: "MasterVolume"

graphicsDropdown (TMP_Dropdown): Graphics quality preset (future)
- Type: TMP_Dropdown
- Purpose: Quality settings (Low/Medium/High/Ultra)
- Options: ["Low", "Medium", "High", "Ultra"]
- PlayerPrefs key: "GraphicsQuality"
```

---

## Integration Points

### Dependencies (What This Needs)
- **Unity Systems**:
  - UnityEngine - MonoBehaviour, PlayerPrefs
  - UnityEngine.UI - Slider, Button
  - TMPro - TMP_Dropdown, TextMeshProUGUI

- **WOS Systems**:
  - [[MenuManager]] - Panel navigation

### Used By (What Uses This)
- [[MainMenuController]] - Routes "Options" button to this panel
- [[InGameMenuController]] - Routes "Settings" button to this panel
- [[MenuManager]] - Shows/hides panel

---

## Technical Details

### Performance Considerations
- **Update Frequency**: Event-driven only (no Update loop)
- **Memory**: Minimal (< 100 bytes, UI references)
- **PlayerPrefs**: Small overhead (< 1 KB settings data)

---

## How It Works

### Settings Flow (Placeholder)
```
LoadSettings():
1. Load from PlayerPrefs:
   - MasterVolume = PlayerPrefs.GetFloat("MasterVolume", 1.0f)
   - GraphicsQuality = PlayerPrefs.GetInt("GraphicsQuality", 2)
2. Apply to UI:
   - audioSlider.value = MasterVolume
   - graphicsDropdown.value = GraphicsQuality
3. ApplySettings() (update game systems)

SaveSettings():
1. Read UI values:
   - float volume = audioSlider.value
   - int quality = graphicsDropdown.value
2. Save to PlayerPrefs:
   - PlayerPrefs.SetFloat("MasterVolume", volume)
   - PlayerPrefs.SetInt("GraphicsQuality", quality)
3. PlayerPrefs.Save() (write to disk)
4. Display "Settings saved!" status
```

---

## Planned Features (Phase 2)

### Audio Settings
```
- Master Volume (slider, 0-100%)
- Music Volume (slider, 0-100%)
- SFX Volume (slider, 0-100%)
- Voice Chat Volume (slider, 0-100%)
- Mute All (toggle)
```

### Graphics Settings
```
- Quality Preset (dropdown: Low/Medium/High/Ultra)
- Resolution (dropdown: all supported resolutions)
- Fullscreen Mode (dropdown: Fullscreen/Windowed/Borderless)
- VSync (toggle)
- Anti-Aliasing (dropdown: Off/2x/4x/8x)
- Shadow Quality (dropdown: Off/Low/Medium/High)
- Texture Quality (dropdown: Low/Medium/High/Ultra)
- View Distance (slider, 500m-5000m)
- FPS Cap (dropdown: 30/60/120/144/Unlimited)
```

### Gameplay Settings
```
- Mouse Sensitivity (slider, 0.1-5.0)
- Invert Y Axis (toggle)
- Field of View (slider, 60-120)
- Camera Shake (toggle)
- Show FPS Counter (toggle)
- Show Network Stats (toggle)
```

### Keybindings
```
- Movement: WASD (rebindable)
- Camera: Mouse (rebindable)
- Fire: Left Click (rebindable)
- Reload: R (rebindable)
- ... (full keybind system)
```

---

## Example Usage

### Current Placeholder Flow
```
1. User clicks "Options" in Main Menu
2. OptionsMenuController panel shown
3. LoadSettings() called
4. (No settings UI yet - placeholder)
5. User clicks "Back" button
6. OnBackButtonClicked() returns to Main Menu
```

### Future Full Settings Flow
```
1. User opens Options menu
2. LoadSettings() populates all UI elements
3. User adjusts:
   - Master Volume: 80%
   - Graphics Quality: High
   - Mouse Sensitivity: 2.5
4. User clicks "Apply" button
5. SaveSettings() writes to PlayerPrefs
6. ApplySettings() updates game systems
7. Status: "Settings saved!"
8. User clicks "Back" to return
```

---

## Related Files
- [[MainMenuController]] - Routes to this panel
- [[InGameMenuController]] - Routes to this panel (in-game settings)
- [[MenuManager]] - Panel navigation
- [[Menu-System]] - Navigation design

---

## Testing Notes

### What Has Been Tested
- ✅ Panel navigation (open/close)
- ✅ Back button functionality
- ⚠️ Settings UI (placeholder only, minimal testing)

### Known Limitations
- ⚠️ No actual settings implemented yet (Phase 2)
- ⚠️ PlayerPrefs not fully utilized
- ⚠️ No settings validation
- ⚠️ No default reset functionality

---

## Implementation Checklist (Phase 2)

### High Priority
- [ ] Audio settings (volume sliders)
- [ ] Graphics quality presets
- [ ] Resolution and fullscreen mode
- [ ] Mouse sensitivity
- [ ] FOV slider

### Medium Priority
- [ ] Advanced graphics options
- [ ] Keybinding system
- [ ] Default reset button
- [ ] Settings validation

### Low Priority
- [ ] Profile save/load (multiple profiles)
- [ ] Cloud settings sync
- [ ] Accessibility options

---

## Changelog
- **2025-01-XX**: Initial placeholder implementation
- **2025-11-17**: Documentation created
- **Phase 2 (TBD)**: Full settings system implementation

---

**Status**: ✅ Implemented (placeholder)
**Maintenance**: Phase 2 expansion planned
**Performance**: N/A (minimal functionality)
