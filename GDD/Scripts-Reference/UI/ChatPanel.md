---
tags: [script, ui, chat, implemented, phase1, input-system]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ChatPanel.cs
status: ✅ IMPLEMENTED
size: 50 KB
---

# ChatPanel.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/UI/ChatPanel.cs` |
| **Namespace** | `WOS.UI` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~1480 |
| **Architecture** | Complex UI controller with New Input System integration |

---

## Purpose

Main chat panel UI controller handling 7 chat channels (System, Proximity, World, Port, Party, Nation, Guild). Manages message display, tab switching, input handling, and integration with New Input System. Includes minimize/maximize functionality, unread badge indicators, and proper input focus management to prevent conflicts with ship controls.

**Critical Features**:
- New Input System (activeInputHandler=2) compatibility
- Combat-critical control restoration (no delays)
- Chat mode vs. game mode input coordination
- Double-send prevention and frame-perfect input handling
- Network disconnect handling

**Phase 1**: System, Proximity, World channels (text only)
**Phase 2+**: Port, Party, Nation, Guild channels

---

## Configuration

### Inspector Fields

```csharp
[Header("UI References")]
tabButtons[7] (ButtonManager[]): Tab buttons (System, Proximity, World, Port, Party, Nation, Guild)
messageScrollRect (ScrollRect): Message display scroll container
messageContentTransform (RectTransform): Content where messages instantiated
messagePrefab (GameObject): Prefab for each chat message
messageDisplayText (TextMeshProUGUI): LEGACY - single text field (replaced by instantiation)
messageInputField (TMP_InputField): Message typing input
sendButton (ButtonManager): Send message button
minimizeButton (ButtonManager): Minimize/maximize toggle

[Header("Tab Badge Indicators")]
tabBadges[7] (GameObject[]): Badge GameObjects for unread count
tabBadgeTexts[7] (TextMeshProUGUI[]): Badge text components

[Header("Settings")]
showTimestamps (bool, default: true): Show timestamps on messages
autoScroll (bool, default: true): Auto-scroll to bottom on new message
maxDisplayMessages (int, default: 100): Maximum messages to display (performance)

[Header("Minimize/Maximize Settings")]
maximizedOffsets (Vector4): Left, Right, Top, Bottom (0, 1350, 850, 0)
minimizedOffsets (Vector4): Left, Right, Top, Bottom (0, 1350, 50, 0)

[Header("References")]
chatManager (ChatManager): For sending messages to server
chatHistory (ChatHistory): For message storage and retrieval
chatCommands (ChatCommands): For command processing (/help, /clear, /roll, etc.)

[Header("Input System")]
inputActions (InputActionAsset): InputSystem_Actions.inputactions asset
```

### Private State

```csharp
currentChannel (ChatChannel): Currently active channel (default: System)
isChatActive (bool): Is chat mode active? (input focused)
isMinimized (bool): Is panel minimized?
skipEnterActivationThisFrame (bool): Prevent Enter reactivation after exit
escapeConsumedThisFrame (bool): Prevent menu from opening when Escape exits chat
justSentMessageThisFrame (bool): Prevent OnInputSubmit from exiting after send
messageSentThisFrame (bool): DOUBLE-SEND PREVENTION flag
isSendingMessage (bool): Prevents OnInputUnfocused during ActivateInputField
deactivationCoroutine (Coroutine): Delayed chat deactivation (allows UI clicks)
navalController (NetworkedNavalController): For disabling/enabling ship controls
instantiatedMessages (List<GameObject>): Instantiated message GameObjects
```

---

## Public API

### Display Methods

```csharp
void SwitchToTab(ChatChannel channel, bool activateChat = true)
```
**Purpose**: Switch to different chat tab
**Parameters**:
- `channel`: Target channel (System, Proximity, World, etc.)
- `activateChat`: If true, activates chat mode (user clicked tab). If false, just switches tab (initialization)
**Behavior**:
- Activates chat mode if requested
- Updates tab button visuals (highlights active tab)
- Marks channel as read (clears unread badge)
- Refreshes message display

```csharp
void RefreshDisplay()
```
**Purpose**: Refresh message display for current channel
**Behavior**:
- Gets recent messages from ChatHistory (max: maxDisplayMessages)
- Clears existing instantiated messages
- Instantiates messagePrefab for each message
- Auto-scrolls to bottom if enabled

```csharp
bool IsMenuOpen()
```
**Purpose**: Check if chat is currently active (for blocking game input)
**Returns**: `isChatActive` state
**Usage**: Called by `UIInputBlocker` and ship controllers

```csharp
bool WasEscapeConsumed()
```
**Purpose**: Check if Escape key was consumed to exit chat this frame
**Returns**: `escapeConsumedThisFrame` flag
**Usage**: Prevents `InGameMenuController` from opening menu when Escape exits chat

```csharp
void AddTestMessages()
```
**Purpose**: Add test messages for development/testing (F2 key or Context Menu)
**Behavior**:
- Adds ~15 messages to System, World, and Proximity channels
- Used for UI testing without network connection

---

## Integration Points

### Dependencies (What This Needs)

**Unity Systems**:
- UnityEngine - MonoBehaviour, GameObject, Transform
- UnityEngine.UI - Button, ScrollRect
- UnityEngine.InputSystem - InputAction, InputActionAsset
- UnityEngine.EventSystems - BaseEventData
- TMPro - TextMeshProUGUI, TMP_InputField
- Michsky.MUIP - ButtonManager

**WOS Systems**:
- `WOS.Chat.ChatManager` - Network message sending (NetworkClient.Send)
- `WOS.Chat.ChatHistory` - Message storage, retrieval, unread tracking
- `WOS.Chat.ChatCommands` - Command processing (/help, /clear, /roll)
- `WOS.Chat.ChatMessage` - Message data structure
- `WOS.Chat.ChatChannel` - Channel enum
- `WOS.Chat.ChatCommandMessage` - Network message type
- `WOS.Chat.ProximityDetector` - Proximity range settings
- `WOS.Player.NetworkedNavalController` - Ship control disable/enable
- `WOS.Debugging.DebugManager` - Logging
- Mirror - NetworkClient for network connectivity

### Used By (What Uses This)

**Input Blocking**:
- `UIInputBlocker` - Calls IsMenuOpen() to block game controls during chat
- `NetworkedNavalController` - Checks UIInputBlocker before processing ship input

**Chat System**:
- `ChatManager` - Populates messages via ChatHistory
- `ChatHistory` - Triggers OnMessageReceived() event

**Settings**:
- `ChatSettingsPanel` - Modifies showTimestamps, font size, opacity

---

## How It Works

### Initialization

**Awake()**: Find references and configure

```csharp
private void Awake()
{
    // Find component references
    if (chatManager == null)
        chatManager = FindFirstObjectByType<ChatManager>();
    if (chatHistory == null)
        chatHistory = FindFirstObjectByType<ChatHistory>();
    if (chatCommands == null)
        chatCommands = FindFirstObjectByType<ChatCommands>();

    // Find NetworkedNavalController for input coordination
    // May not exist yet (networked player spawns after scene load)
    navalController = FindFirstObjectByType<NetworkedNavalController>();
}
```

**Start()**: Initialize UI and subscriptions

```csharp
private void Start()
{
    ShowCursor(); // Keep cursor visible for testing
    InitializeTabs(); // Setup tab buttons
    InitializeInput(); // Setup input field and send button
    InitializeMinimize(); // Setup minimize/maximize
    InitializeInputActions(); // NEW INPUT SYSTEM - Load asset and subscribe
    RefreshDisplay(); // Show initial messages

    // Subscribe to ChatHistory events
    chatHistory.OnMessageAdded += OnMessageReceived;

    // Subscribe to network disconnect event
    NetworkClient.OnDisconnectedEvent += OnNetworkDisconnected;
}
```

### New Input System Integration

**InitializeInputActions()**:

```
Algorithm:
1. Validate inputActions asset assigned (InputSystem_Actions.inputactions)
2. Verify correct asset (name == "InputSystem_Actions", NOT "InventoryInputActions")
3. Find "Chat" action map in asset
4. Find individual actions:
   - OpenChat (Enter key) - Open chat / send message
   - CloseChat (Escape key) - Close chat / cancel
   - SwitchToTab1/2/3 (1/2/3 keys) - Switch channels
   - AddTestMessages (F2 key) - Testing utility
5. Subscribe to action.performed events:
   - openChatAction.performed += OnOpenChatPerformed
   - closeChatAction.performed += OnCloseChatPerformed
   - switchToTab1Action.performed += OnSwitchToTab1Performed
   - switchToTab2Action.performed += OnSwitchToTab2Performed
   - switchToTab3Action.performed += OnSwitchToTab3Performed
   - addTestMessagesAction.performed += OnAddTestMessagesPerformed
6. Chat action map enabled in OnEnable() lifecycle method

Note: Action map is NOT enabled here - OnEnable() handles it for proper lifecycle
```

**OnEnable() / OnDisable()**: Enable/disable Chat action map

```csharp
private void OnEnable()
{
    var chatMap = inputActions.FindActionMap("Chat");
    if (chatMap != null)
        chatMap.Enable(); // Enable when GameObject becomes active
}

private void OnDisable()
{
    var chatMap = inputActions.FindActionMap("Chat");
    if (chatMap != null)
        chatMap.Disable(); // Disable when GameObject becomes inactive
}
```

### Input Callbacks (New Input System)

**OnOpenChatPerformed()** - Enter key pressed

```
Flow:
1. Check if skipEnterActivationThisFrame (just exited chat)
   - If true: Ignore, return
   - If false: Continue

2. Check if messageInputField.isFocused:
   - If focused AND text not empty:
     a. Call SendChatMessage()
     b. SendChatMessage handles re-activation
   - If focused AND text empty:
     a. Exit chat mode (DeactivateChatMode)
     b. Set skipEnterActivationThisFrame = true
   - If NOT focused:
     a. Check if chat active:
        - If not active: ActivateChatMode() + FocusInputFieldDelayed()
        - If active but input unfocused:
          - If input empty: DeactivateChatMode()
          - If input has text: FocusInputFieldDelayed()

Purpose: Handles BOTH opening chat (Enter when not focused) AND sending messages (Enter when focused)
```

**OnCloseChatPerformed()** - Escape key pressed

```
Flow:
1. Check if chat active
   - If not active: Ignore, return

2. Mark escape consumed:
   - escapeConsumedThisFrame = true
   - UIInputBlocker.ConsumeEscape()

3. Clear any typed text (Escape = cancel):
   - if (messageInputField.text not empty)
     messageInputField.text = ""

4. Deactivate chat mode:
   - DeactivateChatMode()

Purpose: Cancel chat (discard typed message) and prevent menu from opening
```

**OnSwitchToTab1/2/3Performed()** - 1/2/3 keys pressed

```
Flow:
1. Check if typing in chat (messageInputField.isFocused)
   - If focused: Ignore (don't switch tabs while typing)
   - If not focused: Continue

2. Check if chat active:
   - If not active: ActivateChatMode()

3. Switch to channel:
   - SwitchToTab(ChatChannel.System/Proximity/World)

Purpose: Quick channel switching with hotkeys (1=System, 2=Proximity, 3=World)
```

### Message Sending

**Algorithm: SendChatMessage()**

```
Input: messageInputField.text

1. DOUBLE-SEND PREVENTION:
   if (messageSentThisFrame)
     return; // Already sent this frame

2. Validate:
   if (messageInputField == null || chatManager == null)
     return;

3. Get content:
   content = messageInputField.text.Trim()
   if (content.IsNullOrWhiteSpace)
     return;

4. Check if command:
   if (content.StartsWith("/"))
     HandleCommand(content) // Delegate to ChatCommands
     messageInputField.text = ""
     return;

5. Send to server (if connected):
   if (NetworkClient.active)
     a. Set isSendingMessage = true (prevents OnInputUnfocused during ActivateInputField)

     b. Create ChatCommandMessage:
        msg.content = content
        msg.channel = currentChannel

     c. Send to server:
        NetworkClient.Send(msg)
        messageSentThisFrame = true // Mark as sent

     d. Set justSentMessageThisFrame = true (prevents OnInputSubmit exit)

     e. Clear and refocus:
        messageInputField.text = ""
        messageInputField.ActivateInputField() // Keep focus

     f. Cancel pending deactivation:
        if (deactivationCoroutine != null)
          StopCoroutine(deactivationCoroutine)
          deactivationCoroutine = null

     g. Ensure chat stays active:
        if (!isChatActive)
          ActivateChatMode()
        else
          DisableGameInput() // Re-disable if needed

     h. Clear flag:
        isSendingMessage = false

Output: Message sent to server, input cleared, chat stays active
```

### Chat Mode Management

**ActivateChatMode()**:

```
Flow:
1. Check if already active:
   if (isChatActive)
     return;

2. Cancel pending deactivation:
   if (deactivationCoroutine != null)
     StopCoroutine(deactivationCoroutine)
     deactivationCoroutine = null

3. Activate chat:
   isChatActive = true
   DisableGameInput() // Disable ship controls
   ShowCursor() // Ensure cursor visible

Output: Chat active, game input disabled, cursor shown
```

**DeactivateChatMode()**:

```
Flow:
1. Force unfocus input field:
   ForceUnfocusInputField() // ALWAYS call, even if isChatActive is false

2. Check if already inactive:
   if (!isChatActive)
     return;

3. Deactivate chat:
   isChatActive = false
   EnableGameInput() // Re-enable ship controls
   // HideCursor() // Disabled for testing

Output: Chat inactive, game input enabled, input unfocused
```

**ForceUnfocusInputField()** - CRITICAL for proper unfocus:

```
Algorithm:
1. Call DeactivateInputField():
   messageInputField.DeactivateInputField()

2. Clear EventSystem selection:
   EventSystem.current.SetSelectedGameObject(null)

3. Trigger OnDeselect event:
   var pointer = new BaseEventData(EventSystem.current)
   messageInputField.OnDeselect(pointer)

Purpose: Ensures input field is FULLY unfocused
- DeactivateInputField() alone is not enough
- Must clear EventSystem selection to prevent keyboard input capture
- Must trigger OnDeselect to hide caret
```

### Input Focus Management

**OnInputFocused(string text)**: Called when input gains focus

```
Flow:
1. Activate chat mode:
   ActivateChatMode()

Output: Chat active, game input disabled
```

**OnInputUnfocused(string text)**: Called when input loses focus

```
Flow:
1. Check if in middle of sending message:
   if (isSendingMessage)
     return; // Ignore unfocus during SendChatMessage()

2. Cancel existing deactivation coroutine:
   if (deactivationCoroutine != null)
     StopCoroutine(deactivationCoroutine)
     deactivationCoroutine = null

3. Check if input is actually still focused:
   if (messageInputField.isFocused)
     return; // Race condition prevention

4. COMBAT-CRITICAL: Immediately restore controls:
   EnableGameInput() // No delay for combat situations!

5. Start delayed panel close:
   deactivationCoroutine = StartCoroutine(DeactivateChatModeDelayed())

Output: Controls restored immediately, chat panel closes after 0.2s delay
```

**DeactivateChatModeDelayed()** - Coroutine:

```
Algorithm:
1. Wait 0.2 seconds:
   yield return new WaitForSeconds(0.2f)

2. Check if input regained focus:
   if (messageInputField.isFocused)
     yield break; // Keep chat active

3. Deactivate chat:
   deactivationCoroutine = null
   DeactivateChatMode()

Purpose: Allows clicking tabs/buttons before closing chat
- If user clicks tab, ActivateChatMode() cancels this coroutine
- If user does nothing, chat closes after delay
```

### Ship Control Coordination

**DisableGameInput()**: Disable ship controls during chat

```csharp
if (navalController != null)
{
    navalController.DisableNavalControls(); // ONLY Naval action map
}
```

**EnableGameInput()**: Re-enable ship controls after chat

```csharp
if (navalController != null)
{
    navalController.EnableNavalControls(); // ONLY Naval action map
}
```

**Critical Implementation Details**:
- ChatPanel and NetworkedNavalController have DIFFERENT InputActionAsset instances
- Must call controller methods to disable/enable (can't disable entire asset)
- Only Naval action map disabled (Chat map stays enabled)
- This prevents conflicts between chat input and ship input

---

## Performance Considerations

- **Update Frequency**: Update loop only for:
  - Finding navalController if not found (TryFindNavalController)
  - Updating tab badges (UpdateTabBadges)
- **CPU Cost**:
  - Update: < 0.1ms (checks and badge updates)
  - SendChatMessage: < 0.5ms (network send)
  - RefreshDisplay: 1-5ms (instantiate messages, depends on count)
- **Memory**:
  - Panel references: ~500 bytes
  - Instantiated messages: ~500 bytes per message * maxDisplayMessages (50KB for 100 messages)
  - Input System actions: ~200 bytes
- **Optimization**:
  - Message instantiation cached (no search for components)
  - Badge updates only when unread count changes
  - Panel search throttled (1s interval)

---

## Network Behavior

**Client-side Only**: UI controller with no network synchronization

**Server Communication**:
- `ChatCommandMessage` sent via `NetworkClient.Send(msg)` when sending messages
- `ChatHistory` populated by server via network events
- `NetworkClient.OnDisconnectedEvent` subscription for cleanup

**Network Requirements**:
- `NetworkClient.active` must be true to send messages
- Server validates all messages (spam prevention, profanity filter, etc.)

---

## Design Patterns Used

### Event-Driven Architecture

**Purpose**: Decouple UI from data
**Implementation**:
- `ChatHistory.OnMessageAdded` event subscription
- `NetworkClient.OnDisconnectedEvent` subscription
- Input Action `performed` events
**Benefits**:
- No polling (efficient)
- Easy to add listeners
- Clear separation of concerns

### State Machine Pattern

**States**:
- **Chat Inactive**: Game input enabled, cursor hidden (testing: visible), input unfocused
- **Chat Active**: Game input disabled, cursor visible, input can be focused
- **Transition Triggers**: Enter key, Escape key, input focus/unfocus

### Frame-Perfect Input Handling

**Problem**: Multiple systems processing same input in one frame
**Solution**: Frame-specific flags
- `skipEnterActivationThisFrame`: Prevents Enter from reactivating after exit
- `escapeConsumedThisFrame`: Prevents menu from opening when Escape exits chat
- `justSentMessageThisFrame`: Prevents OnInputSubmit from exiting after send
- `messageSentThisFrame`: DOUBLE-SEND PREVENTION

**Cleanup**: `LateUpdate()` clears all flags after frame processing complete

---

## Common Pitfalls

### Pitfall 1: Not Using New Input System Callbacks

**Problem**: Legacy `Input.GetKeyDown()` doesn't work with `activeInputHandler=2` in builds
**Solution**: Use Input Action callbacks (`action.performed += OnOpenChatPerformed`)
**Impact**: Enter key won't send messages in builds (works in Editor, fails in build)

### Pitfall 2: Forgetting to Clear EventSystem Selection

**Problem**: Input field still receives keyboard input after DeactivateInputField()
**Solution**: Call `EventSystem.current.SetSelectedGameObject(null)` in ForceUnfocusInputField()
**Impact**: Ship controls don't respond because input field is silently focused

### Pitfall 3: Disabling Entire InputActionAsset

**Problem**: Disabling ChatPanel's inputActions disables entire asset (including Chat map)
**Solution**: Only disable specific action maps, never entire asset
**Impact**: Chat shortcuts (Enter, Escape, 1/2/3) stop working

### Pitfall 4: Not Handling isSendingMessage Flag

**Problem**: OnInputUnfocused fires during ActivateInputField() call in SendChatMessage()
**Solution**: Set `isSendingMessage = true` before ActivateInputField(), clear after
**Impact**: Game controls enabled while still in chat mode

---

## Related Files

### Chat System
- `WOS.Chat.ChatManager` - Network message manager
- `WOS.Chat.ChatHistory` - Message storage and retrieval
- `WOS.Chat.ChatCommands` - Command processing
- `WOS.Chat.ChatMessage` - Message data structure
- `WOS.Chat.ProximityDetector` - Proximity range detection
- `ChatSettingsPanel` - Chat appearance/behavior settings

### Input Coordination
- `WOS.Player.NetworkedNavalController` - Ship control disable/enable
- `UIInputBlocker` - Centralized input blocking utility
- `InGameMenuController` - Escape key coordination

### Configuration
- `Assets/Resources/InputSystem_Actions.inputactions` - Input Action asset

---

## Testing Notes

### What Has Been Tested
- ✅ New Input System callbacks (Enter, Escape, 1/2/3, F2)
- ✅ Message sending with Network connectivity
- ✅ Tab switching with badges
- ✅ Minimize/maximize functionality
- ✅ Input focus/unfocus coordination with ship controls
- ✅ Double-send prevention
- ✅ Frame-perfect input handling
- ✅ Network disconnect cleanup
- ✅ Command processing (/help, /clear, etc.)
- ✅ Combat-critical control restoration (immediate, no delay)

### Known Edge Cases

**Case 1: Rapid Enter Presses**:
```
Scenario: User presses Enter repeatedly while typing
Expected: Send → Refocus → Send → Refocus (no exit)
Actual: Works correctly with justSentMessageThisFrame flag
Status: ✅ Fixed
```

**Case 2: Send Button Click + Enter Same Frame**:
```
Scenario: User clicks Send button while pressing Enter
Expected: Message sent once
Actual: messageSentThisFrame prevents double-send
Status: ✅ Fixed
```

**Case 3: Escape During Message Typing**:
```
Scenario: User types message, presses Escape
Expected: Message discarded, chat closed, menu does NOT open
Actual: Text cleared, chat closed, escapeConsumedThisFrame prevents menu
Status: ✅ Works correctly
```

---

## Changelog

- **Phase 1**: Initial chat panel implementation with 3 channels
- **Phase 1**: Migrated to New Input System (activeInputHandler=2)
- **Phase 1**: Added combat-critical control restoration (immediate, no delay)
- **Phase 1**: Fixed double-send prevention and frame-perfect input handling
- **Phase 1**: Added network disconnect handling
- **2025-12-20**: Documentation created

---

**Status**: ✅ Production-ready (Phase 1 complete)
**Maintenance**: Active development
**Performance**: Excellent (event-driven, minimal Update overhead)
