---
tags: [script, networking, loading-screen, scene-management, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Core
file-path: Assets/Scripts/Port/Core/PortTransitionManager.cs
status: ✅ IMPLEMENTED
size: ~13 KB (493 lines)
feature-group: loading-screen
---

# PortTransitionManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton, DontDestroyOnLoad)
**Namespace**: WOS.Port.Core
**File**: `Assets/Scripts/Port/Core/PortTransitionManager.cs`
**Size**: ~13 KB (493 lines)
**Dependencies**: LoadingScreenManager, PortSceneStateHolder, Mirror

---

## Purpose
Manages port scene transitions while keeping Mirror network connection active, coordinating between LoadingScreenManager and PortSceneStateHolder.

This is the **scene transition coordinator** for harbor/ocean navigation. It:
- Handles Ocean → Harbor transitions (entering ports)
- Handles Harbor → Ocean transitions (leaving ports)
- Maintains network connection during transitions
- Coordinates with LoadingScreenManager for visual feedback
- Preserves player position/state across transitions

---

## Implements GDD Features
- [[Network-Architecture]] - Scene transitions with active connection
- [[UI-Overview]] - Loading screen integration
- [[Zone-System]] - Port entry/exit zones

---

## Key Components

### Public Properties
```
Instance (static): Singleton accessor
IsTransitioning (bool): Whether a transition is in progress
SceneState (PortSceneStateHolder): Current scene state holder
```

### Public Methods
- `RequestEnterHarbor(PortDefinitionSO port, Vector2 pos, float rot, Vector2 vel)` - Request harbor entry
- `RequestExitHarbor()` - Request return to ocean
- `CancelTransition()` - Cancel in-progress transition
- `GetReturnPosition()` - Get saved ocean position
- `GetReturnRotation()` - Get saved ocean rotation
- `SetDockedState(int slot, Vector2 pos, float rot)` - Mark player as docked
- `ClearDockedState()` - Clear docked state

### Events
```csharp
event Action<PortDefinitionSO> OnHarborEntryStarted;
event Action<PortDefinitionSO> OnHarborEntryCompleted;
event Action OnHarborExitStarted;
event Action OnHarborExitCompleted;
event Action<string> OnTransitionError;
```

---

## Configuration

### Inspector Fields
```
[Header("Configuration")]
sceneState (PortSceneStateHolder): Scene state holder asset
harborSceneName (string, "Harbor"): Harbor scene name
oceanSceneName (string, "Ocean"): Ocean scene name

[Header("Transition Settings")]
preLoadDelay (float, 0.2): Delay before loading scene
postLoadDelay (float, 0.3): Delay after scene load
```

---

## Technical Details

### Network Commands

**Harbor Entry** (Client → Server → Client):
```csharp
// Client requests entry
[Command(requiresAuthority = false)]
CmdRequestHarborEntry(portId, position, rotation, velocity)

// Server validates and responds
[TargetRpc]
TargetProceedWithHarborEntry(target, portId)
```

**Harbor Exit** (Client → Server → Client):
```csharp
[Command(requiresAuthority = false)]
CmdRequestHarborExit()

[TargetRpc]
TargetProceedWithHarborExit(target)
```

### Scene Flow

**Ocean → Harbor**:
```
RequestEnterHarbor(port, ...)
  ├─ sceneState.BeginHarborEntry(port, position, rotation, velocity)
  ├─ [Client] CmdRequestHarborEntry() → Server
  │            └─ Server validates → TargetProceedWithHarborEntry()
  └─ StartHarborTransition(port)
       └─ HarborEntryRoutine()
            ├─ OnHarborEntryStarted.Invoke(port)
            ├─ sceneState.SetInTransit()
            ├─ LoadingScreenManager.FadeOutAndShowLoading("Entering...")
            ├─ WaitForSecondsRealtime(preLoadDelay)
            ├─ SceneManager.LoadSceneAsync(harborSceneName)
            ├─ [Loop] LoadingScreenManager.UpdateProgress(progress)
            ├─ WaitForSecondsRealtime(postLoadDelay)
            ├─ sceneState.CompleteHarborEntry()
            ├─ LoadingScreenManager.HideLoadingAndFadeIn()
            └─ OnHarborEntryCompleted.Invoke(port)
```

**Harbor → Ocean**:
```
RequestExitHarbor()
  ├─ sceneState.BeginHarborExit()
  ├─ [Client] CmdRequestHarborExit() → Server
  │            └─ Server validates → TargetProceedWithHarborExit()
  └─ StartOceanTransition()
       └─ HarborExitRoutine()
            ├─ OnHarborExitStarted.Invoke()
            ├─ sceneState.SetInTransit()
            ├─ LoadingScreenManager.FadeOutAndShowLoading("Returning to sea...")
            ├─ WaitForSecondsRealtime(preLoadDelay)
            ├─ SceneManager.LoadSceneAsync(oceanSceneName)
            ├─ [Loop] LoadingScreenManager.UpdateProgress(progress)
            ├─ WaitForSecondsRealtime(postLoadDelay)
            ├─ sceneState.CompleteHarborExit()
            ├─ LoadingScreenManager.HideLoadingAndFadeIn()
            └─ OnHarborExitCompleted.Invoke()
```

### Position Preservation
Player position is saved in PortSceneStateHolder before transition and restored after:
```csharp
// Before entering harbor - save ocean position
sceneState.BeginHarborEntry(port, playerPosition, playerRotation, playerVelocity);

// After exiting harbor - retrieve saved position
Vector2 returnPos = sceneState.GetReturnPosition();
float returnRot = sceneState.GetReturnRotation();
```

---

## Integration Points

### Dependencies
- **Mirror** - NetworkBehaviour, Commands, TargetRpc
- [[LoadingScreenManager]] - Visual loading feedback
- [[PortSceneStateHolder]] - Scene state persistence
- [[PortDefinitionSO]] - Port configuration data
- [[PortDatabaseSO]] - Port lookup by ID

### Used By
- **ExitZoneController** - Triggers harbor exit
- **DockingSquareController** - Docking state management
- **PlayerPortStateController** - Player state tracking

---

## Example Usage

### Triggering Harbor Entry
```csharp
// From a port AoI zone trigger
void OnPlayerEnterPortZone(PortDefinitionSO port)
{
    if (Input.GetKeyDown(KeyCode.E))
    {
        var player = GetLocalPlayer();
        PortTransitionManager.Instance.RequestEnterHarbor(
            port,
            player.transform.position,
            player.transform.eulerAngles.z,
            player.Velocity
        );
    }
}
```

### Triggering Harbor Exit
```csharp
// From harbor exit zone
void OnPlayerEnterExitZone()
{
    PortTransitionManager.Instance.RequestExitHarbor();
}
```

### Listening to Events
```csharp
void Start()
{
    PortTransitionManager.Instance.OnHarborEntryCompleted += OnEnteredHarbor;
    PortTransitionManager.Instance.OnHarborExitCompleted += OnReturnedToSea;
    PortTransitionManager.Instance.OnTransitionError += OnError;
}

void OnEnteredHarbor(PortDefinitionSO port)
{
    Debug.Log($"Welcome to {port.portName}!");
}
```

---

## Editor Utilities

### Context Menu (Play Mode Only)
- **Debug: Force Enter Harbor** - Enter first port in database
- **Debug: Force Exit Harbor** - Exit current harbor

---

## Related Files
- [[LoadingScreenManager]] - Loading screen display
- [[PortSceneStateHolder]] - Scene state persistence
- [[PortDefinitionSO]] - Port configuration
- [[PortDatabaseSO]] - Port lookup
- [[Zone-System]] - Port zones design

---

## Testing Notes
- Requires PortSceneStateHolder asset in Resources/PortConfigurations/
- Transitions blocked if already transitioning
- Cancel resets loading screen immediately via SetClearImmediate()
- Network validation on server before client proceeds

### Edge Cases
- Missing PortSceneStateHolder: Logged warning, creates via Resources.Load
- Scene load failure: Error event fired, transition cancelled
- Duplicate transition requests: Ignored with log message

---

## Changelog
- **2024-12**: Initial implementation with basic scene loading
- **2025-01**: Added Mirror network commands for client/server
- **2025-01**: Integrated LoadingScreenManager for visual feedback
- **2025-01**: Added docked state tracking
