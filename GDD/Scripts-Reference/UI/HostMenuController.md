---
tags: [script, ui, menu, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/HostMenuController.cs
status: ✅ IMPLEMENTED
size: 2.8 KB (2,821 bytes)
---

# HostMenuController.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/HostMenuController.cs`
**Size**: 2.8 KB (2,821 bytes)
**Dependencies**: UnityEngine, TMPro, Mirror (NetworkManager)

---

## Purpose
HostMenuController provides a simple hosting interface for testing and local gameplay. It starts a Mirror host (server + client in same process) and automatically joins as a player, streamlining the development and testing workflow.

This controller is primarily used for local testing and LAN multiplayer, offering a quick way to start a server without dedicated server deployment.

---

## Implements GDD Features
- [[UI-Overview]] - Host panel UI
- [[Menu-System]] - Hosting workflow
- [[Network-Architecture]] - Mirror host setup

---

## Key Components

### Public Methods
- `OnStartHostButtonClicked()` - Start Mirror host (server + client)
- `OnBackButtonClicked()` - Return to connection menu

### Key Private Methods
- `UpdateStatus(string message, bool isError)` - Display status with error handling

---

## Configuration

### Inspector Fields
```csharp
[Header("UI References")]
statusText (TextMeshProUGUI): Status message display
- Type: TextMeshProUGUI
- Purpose: Show hosting status, errors
- Color-coded: Green (success), Red (error)

[Header("Buttons")]
startHostButton (ButtonManager/Button): Start Host button
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Initiate host + client
- Callback: OnStartHostButtonClicked()

backButton (ButtonManager/Button): Back to connection menu
- Type: ButtonManager (MUIP) or Button (Unity UI)
- Purpose: Cancel and return
- Callback: OnBackButtonClicked()
```

---

## Integration Points

### Dependencies (What This Needs)
- **Unity Systems**:
  - UnityEngine - MonoBehaviour
  - TMPro - TextMeshProUGUI for UI

- **Third-Party Assets**:
  - Mirror - NetworkManager.StartHost()

- **WOS Systems**:
  - [[MenuManager]] - Panel navigation

### Used By (What Uses This)
- [[ConnectionMenuController]] - Routes "Host" button to this panel
- [[MenuManager]] - Shows/hides panel
- [[NetworkManager]] - Receives host command

---

## Technical Details

### Performance Considerations
- **Update Frequency**: Event-driven only (no Update loop)
- **Memory**: Minimal (< 100 bytes, UI references only)
- **Network**: Starts both server and client (host mode)

### Network Behavior
- **Host mode** - Server + client in same process
- **Local/LAN** - Not designed for dedicated servers
- **Development use** - Primarily for testing

---

## How It Works

### Hosting Flow
```
OnStartHostButtonClicked():
1. Check if NetworkManager exists
2. Call NetworkManager.singleton.StartHost()
3. Display "Starting host..." status
4. On success:
   - Status: "Host started! Waiting for players..."
   - Scene loads automatically (NetworkManager)
5. On failure:
   - Status: "Failed to start host" (error)
   - Button re-enabled
```

---

## Example Usage

### Starting a Host
```
1. User clicks "Host" button in Connection Menu
2. HostMenuController panel shown
3. User clicks "Start Host" button
4. NetworkManager.StartHost() called
5. Status: "Host started! Waiting for players..."
6. Scene transitions to game
7. Server listens on port 7777 (default)
8. User plays as client in their own server
```

---

## Related Files
- [[ConnectionMenuController]] - Routes to this panel
- [[JoinMenuController]] - Alternative to hosting (joining)
- [[MenuManager]] - Panel navigation
- [[Network-Architecture]] - Mirror hosting design

---

## Testing Notes

### What Has Been Tested
- ✅ Host start/stop
- ✅ Auto-join as client
- ✅ Error handling (NetworkManager missing)
- ✅ Status message display
- ✅ Back button navigation

### Known Edge Cases
- **Port Already in Use**: Mirror error displayed, status shows failure
- **NetworkManager Not in Scene**: Error logged, graceful failure

---

## Changelog
- **2025-01-XX**: Initial implementation with host + client
- **2025-11-17**: Documentation created

---

**Status**: ✅ Production-ready
**Maintenance**: Stable, minimal changes planned
**Performance**: Excellent (event-driven only)
