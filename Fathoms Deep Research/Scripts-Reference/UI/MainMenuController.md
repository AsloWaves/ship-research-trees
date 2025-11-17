---
tags: [script, ui, menu, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/MainMenuController.cs
status: ✅ IMPLEMENTED
size: 2.2 KB (2,180 bytes)
---

# MainMenuController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/MainMenuController.cs`
**Size**: 2.2 KB (2,180 bytes)
**Dependencies**: UnityEngine, TMPro (TextMeshProUGUI), WOS.UI (MenuManager)

---

## Purpose
MainMenuController manages the main menu panel, providing entry points to gameplay (Play button routes to Join menu), settings, and application exit. Simplified for dedicated Edgegap server deployment where hosting is server-side only.

This is the first menu players see after authentication, serving as the primary navigation hub for all game features.

---

## Implements GDD Features
- [[UI-Overview]] - Main menu UI
- [[Menu-System]] - Primary navigation hub
- [[Network-Architecture]] - Client-only menu (simplified for Edgegap)

---

## Key Components

### Public Methods
- `OnPlayButtonClicked()` - Navigate to Join menu (server browser)
- `OnOptionsButtonClicked()` - Navigate to Options menu
- `QuitGame()` - Exit application (handles Editor vs Build)

### Key Private Methods
- `UpdateStatus(string message, bool isError)` - Display status with error handling (optional)

---

## Configuration

### Inspector Fields
```csharp
[Header("UI References")]
statusText (TextMeshProUGUI): Status message display
- Type: TextMeshProUGUI
- Purpose: Show navigation feedback, errors
- Optional: Can be null (no status display)

[Header("Buttons")]
playButton (ButtonManager/Button): Navigate to Join menu
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Start multiplayer (routes to server browser)
- Callback: OnPlayButtonClicked()
- Note: No "Host" option (Edgegap dedicated servers only)

optionsButton (ButtonManager/Button): Navigate to Options menu
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Open settings panel
- Callback: OnOptionsButtonClicked()

quitButton (ButtonManager/Button): Exit application
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Quit game
- Callback: QuitGame()
```

---

## Integration Points

### Dependencies (What This Needs)
- **Unity Systems**:
  - UnityEngine - MonoBehaviour, Application.Quit()
  - TMPro - TextMeshProUGUI for UI

- **WOS Systems**:
  - [[MenuManager]] - Panel navigation

### Used By (What Uses This)
- **Game Entry Point** - First menu after authentication
- [[LoginController]] - Routes to this panel after login
- [[MenuManager]] - Shows/hides panel
- [[ConnectionMenuController]] - Receives "Play" navigation (routes to Join menu)
- [[OptionsMenuController]] - Receives "Options" navigation

---

## Technical Details

### Performance Considerations
- **Update Frequency**: Event-driven only (no Update loop)
- **Memory**: Minimal (< 50 bytes, UI references only)
- **CPU**: Zero overhead when idle

---

## How It Works

### Navigation Flow
```
OnPlayButtonClicked():
1. Call MenuManager.Instance.ShowJoinMenu()
   - Note: Direct to Join menu (no Connection menu needed)
   - Reason: Client-only build, no hosting option
2. MenuManager hides Main Menu panel
3. MenuManager shows Join Menu panel
4. Player selects server from browser

OnOptionsButtonClicked():
1. Call MenuManager.Instance.ShowOptionsMenu()
2. MenuManager hides Main Menu panel
3. MenuManager shows Options panel
4. Player adjusts settings

QuitGame():
1. Check if in Editor or Build:
   - Editor: UnityEditor.EditorApplication.isPlaying = false
   - Build: Application.Quit()
2. Application exits
```

---

## Example Usage

### Typical Flow After Login
```
1. Player logs in successfully
2. LoginController routes to Main Menu
3. Main Menu panel shown with Play/Options/Quit
4. Player clicks "Play" button
5. OnPlayButtonClicked() routes to Join Menu
6. Player sees server browser (Edgegap servers)
7. Player selects server and joins
```

### Options Flow
```
1. Player at Main Menu
2. Player clicks "Options" button
3. OnOptionsButtonClicked() routes to Options Menu
4. Player adjusts settings
5. Player clicks "Back" button
6. Returns to Main Menu
```

---

## Design Notes

### Simplified for Edgegap Deployment
**Original Design** (WOS 2.2):
```
Main Menu → Connection Menu → Host/Join
```

**Current Design** (Fathoms Deep):
```
Main Menu → Join Menu (server browser only)
```

**Reason**:
- Dedicated Edgegap servers (no player hosting)
- Client-only builds (no server executable)
- Simplified UX (one less navigation step)
- Server browser fetches Edgegap deployments

**Trade-offs**:
- ✅ Simpler navigation (fewer clicks)
- ✅ Clearer intent (no confusion about hosting)
- ⚠️ No LAN/local hosting (acceptable for MMO design)
- ⚠️ Requires backend API (Edgegap dependency)

---

## Related Files
- [[LoginController]] - Routes to this panel after login
- [[JoinMenuController]] - "Play" button destination
- [[OptionsMenuController]] - "Options" button destination
- [[MenuManager]] - Panel navigation system
- [[Menu-System]] - Navigation design

---

## Testing Notes

### What Has Been Tested
- ✅ Play button navigation (to Join Menu)
- ✅ Options button navigation
- ✅ Quit button (Editor + Build)
- ✅ Status message display (if used)
- ✅ MenuManager integration

### Known Edge Cases
- **Rapid Button Clicking**: Navigation handled correctly (MenuManager prevents double-navigation)
- **Quit in Editor**: Stops play mode correctly

---

## Changelog
- **2025-01-XX**: Initial implementation with Play/Options/Quit
- **2025-01-XX**: Simplified for Edgegap (removed Connection menu step)
- **2025-11-17**: Documentation created

---

**Status**: ✅ Production-ready
**Maintenance**: Stable, Phase 1 complete
**Performance**: Excellent (event-driven only)
