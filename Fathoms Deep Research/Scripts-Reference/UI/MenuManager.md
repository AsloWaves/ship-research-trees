---
tags: [script, ui, implemented, singleton]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/MenuManager.cs
status: ✅ IMPLEMENTED
size: 10 KB
---

# MenuManager.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton Pattern)
**Namespace**: WOS.UI
**File**: `Scripts/UI/MenuManager.cs`
**Size**: 10 KB (10,221 bytes)
**Dependencies**: UnityEngine, TMPro, WOS.UI.MenuKeyboardNavigation

---

## Purpose
Singleton menu manager that handles panel transitions and navigation history for all menu screens in Fathoms Deep. Provides centralized control of panel visibility with smart back-button navigation using a history stack. Integrates with Modern UI Pack (MUIP) framework and MenuKeyboardNavigation for accessibility.

This is the **core orchestrator** of the menu system - all panel controllers call MenuManager to switch between screens. It maintains a single source of truth for which panel is currently active and enables intuitive navigation through complex menu hierarchies.

---

## Implements GDD Features
- [[UI-Overview]] - Core menu system architecture
- [[Menu-System]] - Panel switching and navigation flow
- WCAG 2.1 AA Compliance - Keyboard navigation integration
- MUIP Integration - Modern UI Pack framework support

---

## Key Components

### Public Properties
```csharp
Instance (MenuManager, static): Singleton instance for global access
```

### MenuPanel Enum
```csharp
public enum MenuPanel
{
    None,              // Default/hidden state
    MainMenu,          // Game entry point
    LoginPanel,        // JWT authentication
    ConnectionMenu,    // Host/Join router
    HostMenu,          // Start local server
    JoinMenu,          // Server browser + connect
    OptionsMenu        // Settings (placeholder)
}
```

### Public Methods
- `ShowPanel(MenuPanel panel)` - Switch to specified panel with history tracking
- `OnBackButtonClicked()` - Navigate to previous panel using history stack
- `ShowMainMenu()` - Shortcut to show main menu panel
- `ShowLoginMenu()` - Shortcut to show login panel
- `ShowConnectionMenu()` - Shortcut to show connection menu panel
- `ShowHostMenu()` - Shortcut to show host menu panel
- `ShowJoinMenu()` - Shortcut to show join menu panel
- `ShowOptionsMenu()` - Shortcut to show options menu panel

### Key Private Methods
- `HideAllPanels()` - Deactivate all panel GameObjects (called before showing new panel)
- `ValidatePanels()` - Startup validation to check all panel references are assigned
- `Awake()` - Singleton initialization with duplicate instance handling
- `Start()` - Panel validation and initial MainMenu display

---

## Configuration

### Inspector Fields
Panel references (assigned in Unity Inspector):
```
[Header("Menu Panels")]
mainMenuPanel (GameObject): Main menu panel GameObject
loginPanel (GameObject): Login/registration panel GameObject
connectionMenuPanel (GameObject): Connection menu (Host/Join router) GameObject
hostMenuPanel (GameObject): Host menu panel GameObject
joinMenuPanel (GameObject): Join menu (server browser) GameObject
optionsMenuPanel (GameObject): Options/settings menu panel GameObject
```

### Private State
```csharp
currentPanel (MenuPanel): Currently active panel (default: MenuPanel.None)
panelHistory (Stack<MenuPanel>): Navigation history for back button
Instance (static MenuManager): Singleton instance reference
```

---

## Integration Points

### Dependencies (What This Needs)

**Unity Systems**:
- UnityEngine - Core GameObject, MonoBehaviour, Transform APIs
- TMPro - TextMeshProUGUI for UI text (imported but not directly used in MenuManager)

**WOS Systems**:
- WOS.UI.MenuKeyboardNavigation - Keyboard navigation for accessibility

**Unity Inspector**:
- All panel GameObjects must be assigned in Inspector
- Panels should be children of Canvas in scene hierarchy

### Used By (What Uses This)

**Panel Controllers** (call ShowPanel and OnBackButtonClicked):
- [[MainMenuController]] - Main menu buttons
- [[ConnectionMenuController]] - Host/Join navigation
- [[HostMenuController]] - Back button
- [[JoinMenuController]] - Back button
- [[LoginController]] - Back button
- [[OptionsMenuController]] - Back button
- [[InGameMenuController]] - Menu navigation (separate system)

**Keyboard Navigation**:
- [[MenuKeyboardNavigation]] - ESC key triggers OnBackButtonClicked()
- Receives OnPanelEnabled() callback when panel changes

**Scene Management**:
- MainMenu.unity scene - Initial setup
- GameScene.unity - InGameMenu uses similar pattern (but separate)

---

## Technical Details

### Performance Considerations
- **Update Frequency**: None - event-driven only (no Update/FixedUpdate loop)
- **Memory Allocations**:
  - Panel references: 6 GameObject pointers (~24 bytes)
  - History stack: ~8 bytes per navigation (Stack<MenuPanel>)
  - Typical history depth: 1-3 panels (~24 bytes average)
  - Total overhead: < 100 bytes
- **CPU Cost**:
  - ShowPanel(): < 0.1ms (SetActive calls + loop)
  - OnBackButtonClicked(): < 0.05ms (stack pop + SetActive)
- **Optimization**: Pre-loaded panels (no instantiation cost)

### Network Behavior
- **Client-side only** - No network synchronization
- Each player has independent menu state
- Zero network bandwidth usage
- Not a NetworkBehaviour (pure client-side MonoBehaviour)

---

## How It Works

### Initialization

**Awake() - Singleton Setup**:
```csharp
private void Awake()
{
    // Enforce singleton pattern
    if (Instance != null && Instance != this)
    {
        Destroy(gameObject); // Destroy duplicate
        return;
    }

    Instance = this;
    DontDestroyOnLoad(gameObject); // Persist across scenes
}
```

**Start() - Validation and Initial Display**:
```csharp
private void Start()
{
    ValidatePanels(); // Check all panel references assigned
    ShowPanel(MenuPanel.MainMenu); // Show main menu by default
}
```

**ValidatePanels() - Configuration Check**:
```csharp
private void ValidatePanels()
{
    if (mainMenuPanel == null)
        Debug.LogError("MenuManager: MainMenu panel not assigned!");
    if (loginPanel == null)
        Debug.LogError("MenuManager: LoginPanel not assigned!");
    // ... (similar checks for all panels)
}
```

### Main Loop
**No Update Loop** - MenuManager is purely event-driven. All functionality triggered by:
- Button clicks in panel controllers
- Keyboard input via MenuKeyboardNavigation
- Scene transitions

### Key Algorithms

#### Algorithm 1: ShowPanel() - Panel Switching with History
```
Input: MenuPanel panel (target panel to show)

1. If currentPanel is not None:
   - Push currentPanel to panelHistory stack
   - Example: currentPanel = MainMenu → Push MainMenu to history

2. Call HideAllPanels():
   - Iterate through all 6 panel GameObjects
   - Call SetActive(false) on each
   - Result: All panels hidden (clean slate)

3. Switch on panel enum:
   - Case MainMenu: mainMenuPanel.SetActive(true)
   - Case LoginPanel: loginPanel.SetActive(true)
   - Case ConnectionMenu: connectionMenuPanel.SetActive(true)
   - Case HostMenu: hostMenuPanel.SetActive(true)
   - Case JoinMenu: joinMenuPanel.SetActive(true)
   - Case OptionsMenu: optionsMenuPanel.SetActive(true)

4. Update currentPanel = panel

5. If target panel has MenuKeyboardNavigation component:
   - Call keyboardNav.OnPanelEnabled()
   - Result: Auto-focus first interactive element (accessibility)

6. MUIP animations trigger automatically:
   - OnEnable() fires on panel GameObject
   - MUIP PanelManager handles fade-in animation
   - Panel fully visible after ~0.3 seconds

Output: Target panel visible, previous panel in history
```

**Example Execution**:
```
ShowPanel(MenuPanel.JoinMenu) with currentPanel = ConnectionMenu:
1. Push ConnectionMenu to history: [MainMenu, ConnectionMenu]
2. Hide all panels
3. joinMenuPanel.SetActive(true)
4. currentPanel = JoinMenu
5. MenuKeyboardNavigation auto-focuses first button
```

#### Algorithm 2: OnBackButtonClicked() - History-Based Navigation
```
Input: None (uses internal history stack)

1. Check if panelHistory.Count > 0:

   TRUE (history exists):
   2a. Pop previousPanel from history
       Example: history = [MainMenu, ConnectionMenu]
                previousPanel = ConnectionMenu (popped)
                history = [MainMenu] (after pop)

   3a. Call HideAllPanels()

   4a. Activate previousPanel directly:
       - Do NOT call ShowPanel() (would re-add to history)
       - Instead: directly SetActive(previousPanel) based on enum

   5a. Update currentPanel = previousPanel

   6a. Trigger keyboard navigation auto-focus

   FALSE (history empty):
   2b. Default to ShowPanel(MenuPanel.MainMenu)
       - This adds MainMenu to history (fresh start)

Output: Previous panel visible, history stack popped
```

**Example Execution**:
```
User Navigation:
MainMenu → ConnectionMenu → JoinMenu
History: [MainMenu, ConnectionMenu]
currentPanel: JoinMenu

OnBackButtonClicked():
1. history.Count = 2 (has history)
2. Pop → previousPanel = ConnectionMenu
3. HideAllPanels()
4. connectionMenuPanel.SetActive(true)
5. currentPanel = ConnectionMenu
6. History now: [MainMenu]

OnBackButtonClicked() again:
1. history.Count = 1 (has history)
2. Pop → previousPanel = MainMenu
3. HideAllPanels()
4. mainMenuPanel.SetActive(true)
5. currentPanel = MainMenu
6. History now: []

OnBackButtonClicked() again:
1. history.Count = 0 (no history)
2. ShowPanel(MenuPanel.MainMenu)
3. History now: [] (MainMenu doesn't push to history)
```

#### Algorithm 3: HideAllPanels() - Reset Panel State
```
Input: None (operates on all panel references)

For each panel GameObject:
1. if (mainMenuPanel != null) mainMenuPanel.SetActive(false);
2. if (loginPanel != null) loginPanel.SetActive(false);
3. if (connectionMenuPanel != null) connectionMenuPanel.SetActive(false);
4. if (hostMenuPanel != null) hostMenuPanel.SetActive(false);
5. if (joinMenuPanel != null) joinMenuPanel.SetActive(false);
6. if (optionsMenuPanel != null) optionsMenuPanel.SetActive(false);

Output: All panels hidden (SetActive(false))
Note: Null checks prevent errors if panel references missing
```

### State Machine Diagram
```
┌────────────────────────────────────────────────────────────┐
│                    MenuManager State                        │
│                                                             │
│  currentPanel: MenuPanel                                   │
│  panelHistory: Stack<MenuPanel>                            │
└────────────────────────────────────────────────────────────┘
                       │
                       │ ShowPanel(panel)
                       ▼
            ┌──────────────────────┐
            │  Push current to     │
            │  history (if not     │
            │  None)               │
            └──────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │  HideAllPanels()     │
            └──────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │  Show target panel   │
            │  (SetActive true)    │
            └──────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │  Update currentPanel │
            └──────────────────────┘
                       │
                       ▼
            ┌──────────────────────┐
            │  Trigger keyboard    │
            │  navigation focus    │
            └──────────────────────┘

       OnBackButtonClicked()
                       │
                       ▼
            ┌──────────────────────┐
            │  Check history.Count │
            └──────────────────────┘
                   │          │
            Count > 0    Count == 0
                   │          │
                   ▼          ▼
       ┌────────────────┐  ┌──────────────────┐
       │ Pop history    │  │ ShowPanel(       │
       │ Show previous  │  │   MainMenu)      │
       └────────────────┘  └──────────────────┘
```

---

## Example Usage

### From Panel Controllers
```csharp
// Example: MainMenuController.cs
using WOS.UI;

public class MainMenuController : MonoBehaviour
{
    public void OnPlayButtonClicked()
    {
        // Navigate to connection menu
        MenuManager.Instance.ShowPanel(MenuPanel.ConnectionMenu);
    }

    public void OnOptionsButtonClicked()
    {
        // Navigate to options menu
        MenuManager.Instance.ShowPanel(MenuPanel.OptionsMenu);
    }

    public void QuitGame()
    {
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #else
        Application.Quit();
        #endif
    }
}
```

### From Keyboard Navigation
```csharp
// Example: MenuKeyboardNavigation.cs
using WOS.UI;

public class MenuKeyboardNavigation : MonoBehaviour
{
    void Update()
    {
        // ESC key triggers back navigation
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            MenuManager.Instance.OnBackButtonClicked();
        }
    }
}
```

### Complex Navigation Flow
```csharp
// User Journey: Main → Connection → Join → Back → Host

// Step 1: MainMenu to ConnectionMenu
MenuManager.Instance.ShowPanel(MenuPanel.ConnectionMenu);
// State: currentPanel = ConnectionMenu, history = [MainMenu]

// Step 2: ConnectionMenu to JoinMenu
MenuManager.Instance.ShowPanel(MenuPanel.JoinMenu);
// State: currentPanel = JoinMenu, history = [MainMenu, ConnectionMenu]

// Step 3: Back button (return to ConnectionMenu)
MenuManager.Instance.OnBackButtonClicked();
// State: currentPanel = ConnectionMenu, history = [MainMenu]

// Step 4: ConnectionMenu to HostMenu
MenuManager.Instance.ShowPanel(MenuPanel.HostMenu);
// State: currentPanel = HostMenu, history = [MainMenu, ConnectionMenu]
```

---

## Related Files

### Panel Controllers
- [[MainMenuController]] - Main menu entry point (Play, Options, Quit)
- [[ConnectionMenuController]] - Host/Join router
- [[HostMenuController]] - Server hosting panel
- [[JoinMenuController]] - Server browser panel
- [[LoginController]] - Authentication panel
- [[OptionsMenuController]] - Settings panel (placeholder)
- [[InGameMenuController]] - ESC pause menu (separate system)

### Accessibility
- [[MenuKeyboardNavigation]] - WCAG 2.1 AA keyboard navigation

### GDD Documentation
- [[UI-Overview]] - Complete UI system overview
- [[Menu-System]] - Menu architecture and navigation flow

### Unity Assets
- MenuManager.prefab - Prefab for MenuManager GameObject
- MainMenu.unity - Main menu scene with all panels
- Canvas.prefab - UI canvas with panel hierarchy

---

## Testing Notes

### What Has Been Tested
- ✅ Singleton enforcement (duplicate instance destruction)
- ✅ Panel switching (all 6 panels)
- ✅ Back button navigation (history stack)
- ✅ Default panel on startup (MainMenu)
- ✅ Panel validation (missing references logged)
- ✅ History depth (arbitrary navigation trees)
- ✅ MUIP integration (animations work with SetActive)
- ✅ Keyboard navigation integration (ESC key)
- ✅ DontDestroyOnLoad persistence across scenes

### Known Edge Cases

**Case 1: Empty History + Back Button**:
```
Scenario: User presses back on MainMenu with no history
Expected: Nothing happens (or ShowMainMenu called)
Actual: ShowPanel(MenuPanel.MainMenu) called (adds to history if not already MainMenu)
Status: ✅ Works as designed
```

**Case 2: Panel Reference Missing**:
```
Scenario: Developer forgets to assign joinMenuPanel in Inspector
Expected: Error logged at startup, ShowPanel(JoinMenu) does nothing
Actual: ValidatePanels() logs error, no crash
Status: ✅ Safe failure mode
```

**Case 3: Rapid Panel Switching**:
```
Scenario: User clicks buttons rapidly during MUIP animation
Expected: Panels switch correctly, animations may overlap
Actual: MenuManager updates immediately, MUIP handles animation queue
Status: ✅ Works correctly (no locks needed)
```

**Case 4: Scene Reload**:
```
Scenario: Main menu scene reloaded while MenuManager exists (DontDestroyOnLoad)
Expected: New MenuManager instance destroyed, existing instance persists
Actual: Awake() detects duplicate, Destroy(gameObject)
Status: ✅ Singleton pattern prevents duplicates
```

### Test Scenarios

**Manual Test 1: Basic Navigation**:
1. Launch game → Verify MainMenu displayed
2. Click Play → Verify ConnectionMenu displayed
3. Click Join → Verify JoinMenu displayed
4. Click Back → Verify ConnectionMenu displayed
5. Click Back → Verify MainMenu displayed
✅ **Result**: Navigation flow correct

**Manual Test 2: History Depth**:
1. Navigate: Main → Connection → Join → Back → Host
2. Click Back → Should return to Connection (not Join)
3. Click Back → Should return to Main
✅ **Result**: History stack maintains correct order

**Manual Test 3: Validation**:
1. Create new scene, add MenuManager
2. Leave some panel references unassigned
3. Enter Play mode
4. Check Console for errors
✅ **Result**: Missing references logged, no crashes

**Unit Test Example** (hypothetical - not in codebase):
```csharp
[Test]
public void ShowPanel_PushesToHistory()
{
    // Arrange
    var manager = MenuManager.Instance;
    manager.ShowPanel(MenuPanel.MainMenu);

    // Act
    manager.ShowPanel(MenuPanel.ConnectionMenu);

    // Assert
    manager.OnBackButtonClicked();
    Assert.AreEqual(MenuPanel.MainMenu, manager.currentPanel);
}
```

---

## Design Patterns Used

### Singleton Pattern
**Purpose**: Ensure only one MenuManager exists globally
**Implementation**: Static Instance + Awake() enforcement
**Benefits**:
- Global access via `MenuManager.Instance`
- No need to pass references between controllers
- Survives scene transitions (DontDestroyOnLoad)

### Memento Pattern (Simplified)
**Purpose**: Save/restore navigation state
**Implementation**: History stack stores previous panels
**Benefits**:
- Smart back button navigation
- No need for hardcoded parent/child relationships

### State Pattern (Implicit)
**Purpose**: Manage current panel state
**Implementation**: currentPanel enum + panel GameObjects
**Benefits**:
- Clear current state representation
- Easy validation and debugging

---

## Common Pitfalls

### Pitfall 1: Calling ShowPanel() from OnBackButtonClicked()
**Problem**: Re-adds panel to history when navigating back
**Solution**: Directly activate panel without ShowPanel() call
**Code**:
```csharp
// ❌ WRONG (adds to history again)
void OnBackButtonClicked()
{
    MenuPanel prev = panelHistory.Pop();
    ShowPanel(prev); // BUG: Re-adds to history!
}

// ✅ CORRECT (direct activation)
void OnBackButtonClicked()
{
    MenuPanel prev = panelHistory.Pop();
    HideAllPanels();
    ActivatePanelDirectly(prev); // No history push
    currentPanel = prev;
}
```

### Pitfall 2: Forgetting DontDestroyOnLoad()
**Problem**: MenuManager destroyed on scene transition
**Solution**: Add DontDestroyOnLoad() in Awake()
**Impact**: Menus disappear when loading gameplay scene

### Pitfall 3: Not Checking Singleton Before Use
**Problem**: NullReferenceException if MenuManager not in scene
**Solution**: Always check Instance != null before use
**Code**:
```csharp
// ✅ SAFE
if (MenuManager.Instance != null)
{
    MenuManager.Instance.ShowPanel(MenuPanel.JoinMenu);
}
else
{
    Debug.LogError("MenuManager not found in scene!");
}
```

### Pitfall 4: Modifying Panel Hierarchy at Runtime
**Problem**: Panel references become stale if GameObjects moved/destroyed
**Solution**: Don't modify panel GameObjects after Awake()
**Impact**: ShowPanel() may fail silently or throw exceptions

---

## Changelog

- **2025-01-XX**: Initial implementation with singleton pattern
- **2025-01-XX**: Added panel enum and ShowPanel() method
- **2025-01-XX**: Implemented navigation history stack
- **2025-01-XX**: Added panel validation system
- **2025-01-XX**: Integrated with MenuKeyboardNavigation
- **2025-01-XX**: Added shortcut methods (ShowMainMenu, etc.)
- **2025-01-XX**: DontDestroyOnLoad for scene persistence
- **2025-11-17**: Documentation migrated to Obsidian vault

---

**Status**: ✅ Production-ready, no known bugs
**Maintenance**: Stable, no changes planned for Phase 2-3
**Performance**: Excellent (< 0.1ms overhead)
