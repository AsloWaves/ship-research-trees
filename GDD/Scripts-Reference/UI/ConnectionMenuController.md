---
tags: [script, ui, menu, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ConnectionMenuController.cs
status: ✅ IMPLEMENTED
size: 2.4 KB (2,410 bytes)
---

# ConnectionMenuController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/ConnectionMenuController.cs`
**Size**: 2.4 KB (2,410 bytes)
**Dependencies**: UnityEngine, UnityEngine.UI, TMPro, Mirror, WOS.Networking (ServerConfig)

---

## Purpose
ConnectionMenuController handles navigation on the Connection panel, providing Host/Join button routing. It serves as the multiplayer mode selection hub, bridging the main menu with hosting and joining workflows.

This controller works seamlessly with MenuManager's multi-panel system, maintaining navigation history and providing clean panel transitions.

---

## Implements GDD Features
- [[UI-Overview]] - Connection panel UI
- [[Menu-System]] - Multi-panel navigation
- [[Network-Architecture]] - Connection flow routing

---

## Key Components

### Public Methods
- `OnHostButtonClicked()` - Navigate to Host panel
- `OnJoinButtonClicked()` - Navigate to Join panel
- `OnBackButtonClicked()` - Return to main menu

### Key Private Methods
- `UpdateStatus(string message)` - Display status messages

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
hostButton (ButtonManager/Button): Navigate to Host panel
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Route to hosting workflow
- Callback: OnHostButtonClicked()

joinButton (ButtonManager/Button): Navigate to Join panel
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Route to join workflow
- Callback: OnJoinButtonClicked()

backButton (ButtonManager/Button): Return to main menu
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Navigate back
- Callback: OnBackButtonClicked()
```

---

## Integration Points

### Dependencies (What This Needs)
- **Unity Systems**:
  - UnityEngine - MonoBehaviour
  - UnityEngine.UI - Button events
  - TMPro - TextMeshProUGUI for UI

- **Third-Party Assets**:
  - Mirror - Network configuration

- **WOS Systems**:
  - [[MenuManager]] - Panel navigation and history
  - [[ServerConfig]] - Server configuration data

### Used By (What Uses This)
- [[MainMenuController]] - Routes "Play" button to this panel
- [[MenuManager]] - Shows/hides panel, manages navigation
- [[HostMenuController]] - Receives "Host" navigation
- [[JoinMenuController]] - Receives "Join" navigation

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
OnHostButtonClicked():
1. Call MenuManager.Instance.ShowHostMenu()
2. MenuManager hides Connection panel
3. MenuManager shows Host panel
4. Navigation history updated (back button support)

OnJoinButtonClicked():
1. Call MenuManager.Instance.ShowJoinMenu()
2. MenuManager hides Connection panel
3. MenuManager shows Join panel
4. Navigation history updated (back button support)

OnBackButtonClicked():
1. Call MenuManager.Instance.ShowMainMenu()
2. MenuManager hides Connection panel
3. MenuManager shows Main Menu panel
4. Navigation history popped
```

---

## Example Usage

### Typical Navigation
```
1. User clicks "Play" in Main Menu
2. MainMenuController routes to Connection Menu
3. Connection panel shown with Host/Join buttons
4. User clicks "Join" button
5. OnJoinButtonClicked() called
6. MenuManager shows Join panel
7. User enters server IP and connects
```

---

## Related Files
- [[MainMenuController]] - Routes to this panel
- [[HostMenuController]] - Host panel destination
- [[JoinMenuController]] - Join panel destination
- [[MenuManager]] - Panel navigation system
- [[Menu-System]] - Navigation design

---

## Testing Notes

### What Has Been Tested
- ✅ Host button navigation
- ✅ Join button navigation
- ✅ Back button navigation
- ✅ MenuManager integration
- ✅ Navigation history (back button stack)

---

## Changelog
- **2025-01-XX**: Initial implementation with Host/Join routing
- **2025-11-17**: Documentation created

---

**Status**: ✅ Production-ready
**Maintenance**: Stable, minimal changes planned
**Performance**: Excellent (event-driven only)
