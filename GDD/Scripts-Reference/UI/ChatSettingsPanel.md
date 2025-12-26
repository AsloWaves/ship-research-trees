---
tags: [script, ui, chat, settings, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ChatSettingsPanel.cs
status: ✅ IMPLEMENTED
size: 9.5 KB
---

# ChatSettingsPanel.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/UI/ChatSettingsPanel.cs` |
| **Namespace** | `WOS.UI` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~293 |
| **Architecture** | Settings panel with PlayerPrefs persistence |

---

## Purpose

Chat settings panel for configuring chat appearance and behavior. Provides UI controls for timestamps, profanity filter, font size, panel opacity, and proximity chat range. Settings are persisted to PlayerPrefs and applied to ChatPanel and related systems in real-time.

**Phase 1**: Basic settings (timestamps, font size, opacity, proximity range)
**Phase 2+**: Voice settings, channel enable/disable

---

## Configuration

### Inspector Fields

```csharp
[Header("References")]
chatPanel (ChatPanel): ChatPanel to apply settings to
proximityDetector (ProximityDetector): ProximityDetector to update range

[Header("UI Components")]
timestampsToggle (Toggle): Toggle for showing timestamps
profanityFilterToggle (Toggle): Toggle for profanity filter
fontSizeSlider (Slider): Slider for font size (8-24)
fontSizeText (TextMeshProUGUI): Text showing current font size
opacitySlider (Slider): Slider for panel opacity (0.3-1.0)
opacityText (TextMeshProUGUI): Text showing current opacity percentage
proximityRangeSlider (Slider): Slider for proximity range (10-200 units)
proximityRangeText (TextMeshProUGUI): Text showing current range in meters
saveButton (ButtonManager): Save settings button
resetButton (ButtonManager): Reset to defaults button
closeButton (ButtonManager): Close panel button

[Header("Default Values")]
defaultTimestamps (bool, default: true): Show timestamps by default
defaultProfanityFilter (bool, default: true): Enable filter by default
defaultFontSize (float, default: 14f): Default font size
defaultOpacity (float, default: 0.9f): Default panel opacity (90%)
defaultProximityRange (float, default: 50f): Default proximity range (50 meters)
```

### PlayerPrefs Keys

```csharp
const string PREF_TIMESTAMPS = "Chat_ShowTimestamps"
const string PREF_PROFANITY = "Chat_ProfanityFilter"
const string PREF_FONT_SIZE = "Chat_FontSize"
const string PREF_OPACITY = "Chat_Opacity"
const string PREF_PROXIMITY = "Chat_ProximityRange"
```

---

## Public API

### Settings Management

```csharp
void LoadSettings()
```
**Purpose**: Load settings from PlayerPrefs and apply to UI
**Behavior**:
- Reads all settings from PlayerPrefs (uses defaults if not found)
- Updates UI controls (toggles, sliders, text)
- Applies settings to ChatPanel and ProximityDetector

```csharp
void SaveSettings()
```
**Purpose**: Save current UI values to PlayerPrefs
**Behavior**:
- Writes all settings to PlayerPrefs
- Calls PlayerPrefs.Save() to persist
- Shows confirmation message in chat ("✅ Chat settings saved")

```csharp
void ResetToDefaults()
```
**Purpose**: Reset all settings to default values
**Behavior**:
- Sets UI controls to default values
- Calls SaveSettings() to persist
- Logs reset action

```csharp
void ClosePanel()
```
**Purpose**: Hide settings panel
**Behavior**:
- Calls gameObject.SetActive(false)

---

## Integration Points

### Dependencies (What This Needs)

**Unity Systems**:
- UnityEngine - MonoBehaviour, GameObject, PlayerPrefs
- UnityEngine.UI - Toggle, Slider, Button
- TMPro - TextMeshProUGUI for text display
- Michsky.MUIP - ButtonManager for buttons

**WOS Systems**:
- `ChatPanel` - Applies timestamps, font size, opacity settings
- `WOS.Chat.ChatManager` - Applies profanity filter setting
- `WOS.Chat.ProximityDetector` - Applies proximity range setting
- `WOS.Chat.ChatHistory` - For showing confirmation messages
- `WOS.Debugging.DebugManager` - Logging

### Used By (What Uses This)

**Settings Menu**:
- `OptionsMenuController` - Opens settings panel
- `InGameMenuController` - Opens settings panel
- Player HUD - Settings button opens panel

---

## How It Works

### Initialization

**Awake()**: Find references

```csharp
private void Awake()
{
    if (chatPanel == null)
        chatPanel = FindFirstObjectByType<ChatPanel>();

    if (proximityDetector == null)
        proximityDetector = FindFirstObjectByType<ProximityDetector>();

    if (chatPanel != null)
        chatPanelCanvasGroup = chatPanel.GetComponent<CanvasGroup>();
}
```

**Start()**: Initialize UI and load settings

```csharp
private void Start()
{
    InitializeUI(); // Setup button/slider listeners
    LoadSettings(); // Load from PlayerPrefs
}
```

### UI Initialization

**Algorithm: InitializeUI()**

```
1. Add listeners to toggles:
   - timestampsToggle.onValueChanged += OnTimestampsChanged
   - profanityFilterToggle.onValueChanged += OnProfanityFilterChanged

2. Add listeners to sliders:
   - fontSizeSlider.onValueChanged += OnFontSizeChanged
   - opacitySlider.onValueChanged += OnOpacityChanged
   - proximityRangeSlider.onValueChanged += OnProximityRangeChanged

3. Add listeners to buttons (MUIP ButtonManager):
   - saveButton → SaveSettings()
   - resetButton → ResetToDefaults()
   - closeButton → ClosePanel()

Output: All UI controls have listeners attached
```

### Settings Loading

**Algorithm: LoadSettings()**

```
Input: PlayerPrefs data (or defaults if not found)

1. Load timestamps:
   - showTimestamps = PlayerPrefs.GetInt(PREF_TIMESTAMPS, defaultTimestamps ? 1 : 0) == 1
   - timestampsToggle.isOn = showTimestamps
   - chatPanel.showTimestamps = showTimestamps

2. Load profanity filter:
   - useProfanityFilter = PlayerPrefs.GetInt(PREF_PROFANITY, defaultProfanityFilter ? 1 : 0) == 1
   - profanityFilterToggle.isOn = useProfanityFilter

3. Load font size:
   - fontSize = PlayerPrefs.GetFloat(PREF_FONT_SIZE, defaultFontSize)
   - fontSizeSlider.value = fontSize
   - OnFontSizeChanged(fontSize) // Apply

4. Load opacity:
   - opacity = PlayerPrefs.GetFloat(PREF_OPACITY, defaultOpacity)
   - opacitySlider.value = opacity
   - OnOpacityChanged(opacity) // Apply

5. Load proximity range:
   - proximityRange = PlayerPrefs.GetFloat(PREF_PROXIMITY, defaultProximityRange)
   - proximityRangeSlider.value = proximityRange
   - OnProximityRangeChanged(proximityRange) // Apply

Output: UI controls and systems updated with saved settings
```

### Settings Saving

**Algorithm: SaveSettings()**

```
Input: Current UI control values

1. Save toggles:
   - PlayerPrefs.SetInt(PREF_TIMESTAMPS, timestampsToggle.isOn ? 1 : 0)
   - PlayerPrefs.SetInt(PREF_PROFANITY, profanityFilterToggle.isOn ? 1 : 0)

2. Save sliders:
   - PlayerPrefs.SetFloat(PREF_FONT_SIZE, fontSizeSlider.value)
   - PlayerPrefs.SetFloat(PREF_OPACITY, opacitySlider.value)
   - PlayerPrefs.SetFloat(PREF_PROXIMITY, proximityRangeSlider.value)

3. Persist to disk:
   - PlayerPrefs.Save()

4. Show confirmation:
   - chatHistory.AddMessage("✅ Chat settings saved", ChatChannel.System)

Output: Settings saved to PlayerPrefs and persisted
```

### UI Callbacks

**OnTimestampsChanged(bool value)**:
```csharp
if (chatPanel != null)
{
    chatPanel.showTimestamps = value; // Update setting
    chatPanel.RefreshDisplay(); // Re-render messages with/without timestamps
}
```

**OnProfanityFilterChanged(bool value)**:
```csharp
var chatManager = FindFirstObjectByType<ChatManager>();
if (chatManager != null)
{
    chatManager.enableProfanityFilter = value;
}
```

**OnFontSizeChanged(float value)**:
```csharp
// Update label
fontSizeText.text = $"{value:F0}"; // "14" (no decimals)

// Apply to chat panel
if (chatPanel != null && chatPanel.messageDisplayText != null)
{
    chatPanel.messageDisplayText.fontSize = value;
}
```

**OnOpacityChanged(float value)**:
```csharp
// Update label
opacityText.text = $"{(value * 100):F0}%"; // "90%" (0.9 → 90%)

// Apply to chat panel CanvasGroup
if (chatPanelCanvasGroup != null)
{
    chatPanelCanvasGroup.alpha = value; // 0.3 (30%) to 1.0 (100%)
}
```

**OnProximityRangeChanged(float value)**:
```csharp
// Update label
proximityRangeText.text = $"{value:F0}m"; // "50m" (no decimals)

// Apply to proximity detector
if (proximityDetector != null)
{
    proximityDetector.SetProximityRange(value); // Update detection range
}
```

---

## Performance Considerations

- **Update Frequency**: None - event-driven only (no Update loop)
- **Memory**: Minimal overhead
  - Panel references: ~200 bytes
  - UI control references: ~200 bytes
- **CPU Cost**:
  - LoadSettings(): < 0.1ms (PlayerPrefs reads)
  - SaveSettings(): < 0.5ms (PlayerPrefs writes + disk I/O)
  - UI callbacks: < 0.05ms each
- **Disk I/O**: PlayerPrefs.Save() writes to registry (Windows) or plist (Mac) - ~1ms

---

## Example Usage

### Opening Settings Panel

```csharp
// From OptionsMenuController or InGameMenuController
public void OpenChatSettings()
{
    chatSettingsPanel.gameObject.SetActive(true);
    // Settings automatically loaded on first activation (Start() called)
}
```

### User Adjusts Settings

```
User Flow:
1. User opens settings panel
2. User moves font size slider from 14 to 18
   - OnFontSizeChanged(18) fires immediately
   - fontSizeText updates: "18"
   - chatPanel.messageDisplayText.fontSize = 18
   - User sees chat text get larger in real-time
3. User clicks "Save"
   - SaveSettings() writes to PlayerPrefs
   - Confirmation message shown in chat
4. User closes settings panel
   - Settings persist across sessions
```

### Reset to Defaults

```
User Flow:
1. User clicks "Reset to Defaults" button
2. ResetToDefaults() called:
   - timestampsToggle.isOn = true (default)
   - profanityFilterToggle.isOn = true (default)
   - fontSizeSlider.value = 14f (default)
   - opacitySlider.value = 0.9f (default)
   - proximityRangeSlider.value = 50f (default)
3. SaveSettings() called automatically
4. All UI callbacks fire (OnFontSizeChanged, etc.)
5. Settings applied to systems
6. Confirmation message shown
```

---

## Design Notes

### Real-Time Preview

**UX Design**:
- Settings applied immediately as sliders/toggles change
- No need to click "Apply" - changes visible instantly
- "Save" button only persists to PlayerPrefs (already applied visually)

**Benefits**:
- User sees result before saving
- Can experiment with settings
- Can close without saving (reverts on next load)

### PlayerPrefs Persistence

**Data Storage**:
- Windows: Registry (HKEY_CURRENT_USER\Software\CompanyName\GameName)
- Mac: ~/Library/Preferences/com.CompanyName.GameName.plist
- Linux: ~/.config/unity3d/CompanyName/GameName/prefs

**Limitations**:
- No cloud sync (local machine only)
- Cleared if user deletes PlayerPrefs
- Not encrypted (don't store sensitive data)

### Future Enhancements (Phase 2+)

**Voice Chat Settings**:
- Voice volume slider
- Push-to-talk keybind
- Voice activation threshold
- Microphone selection

**Channel Settings**:
- Enable/disable specific channels
- Channel-specific colors
- Channel-specific font sizes
- Channel notification sounds

**Advanced Settings**:
- Chat history buffer size
- Message fade time
- Timestamp format (12h/24h)
- Language/localization

---

## Related Files

### Chat System
- `ChatPanel` - Main chat UI (applies settings)
- `WOS.Chat.ChatManager` - Profanity filter configuration
- `WOS.Chat.ProximityDetector` - Proximity range configuration
- `WOS.Chat.ChatHistory` - Confirmation messages

### Settings Integration
- `OptionsMenuController` - Opens settings from main menu
- `InGameMenuController` - Opens settings in-game
- `GraphicsSettingsPanel` - Similar pattern for graphics settings
- `VoiceSettingsPanel` - Similar pattern for voice settings

---

## Testing Notes

### What Has Been Tested
- ✅ Load settings from PlayerPrefs
- ✅ Save settings to PlayerPrefs
- ✅ Reset to defaults
- ✅ Real-time preview of all settings
- ✅ Slider value display (font size, opacity, proximity)
- ✅ Toggle state persistence
- ✅ Confirmation message on save
- ✅ Close panel functionality

### Known Edge Cases

**Case 1: First Launch (No PlayerPrefs)**:
```
Scenario: User launches game for first time
Expected: Default values used
Actual: Works correctly (PlayerPrefs.Get* returns defaults)
Status: ✅ Tested
```

**Case 2: Invalid PlayerPrefs Values**:
```
Scenario: PlayerPrefs corrupted or manually edited
Expected: Clamped to slider min/max ranges
Actual: Unity Slider component clamps automatically
Status: ✅ Safe
```

**Case 3: Close Without Saving**:
```
Scenario: User adjusts settings, clicks Close (not Save)
Expected: Changes visible but not persisted
Actual: Next launch loads old values, reverts changes
Status: ✅ Intended behavior
```

---

## Changelog

- **Phase 1**: Initial settings panel implementation
- **Phase 1**: Added timestamps, font size, opacity, proximity range
- **Phase 1**: PlayerPrefs persistence
- **Phase 1**: Real-time preview
- **2025-12-20**: Documentation created

---

**Status**: ✅ Production-ready (Phase 1 complete)
**Maintenance**: Stable
**Performance**: Excellent (event-driven, no overhead)
