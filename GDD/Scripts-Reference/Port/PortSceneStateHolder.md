---
tags: [script, port, scriptableobject, state, implemented]
script-type: ScriptableObject
namespace: WOS.Port
file-path: Assets/Scripts/Port/Core/PortSceneStateHolder.cs
status: IMPLEMENTED
size: ~257 lines
feature-group: port
---

# PortSceneStateHolder.cs

## Quick Reference
**Type**: ScriptableObject (Runtime State Container)
**Namespace**: WOS.Port
**File**: `Assets/Scripts/Port/Core/PortSceneStateHolder.cs`
**Size**: ~257 lines
**Create**: `Create > WOS > Port > Scene State Holder`
**Dependencies**: PortDefinitionSO

---

## Purpose
ScriptableObject that persists port transition state across scene loads. Stores the player's ocean position, rotation, and velocity before entering a harbor so they can be restored when exiting. Enables seamless scene transitions between ocean and harbor scenes.

---

## TransitionState Enum

```csharp
public enum TransitionState
{
    None,           // Default, no transition in progress
    EnteringHarbor, // Player initiated harbor entry
    ExitingHarbor,  // Player initiated harbor exit
    Docked,         // Player is docked in harbor
    InTransit       // Scene load in progress
}
```

---

## State Properties

```csharp
[Header("Current Transition")]
public TransitionState CurrentTransition = TransitionState.None;

[Header("Port Reference")]
public PortDefinitionSO CurrentPort;

[Header("Ocean State (Preserved)")]
public Vector2 LastOceanPosition;
public float LastOceanRotation;
public Vector2 LastOceanVelocity;

[Header("Harbor State")]
public int CurrentDockIndex = -1;
public bool WasDockedOnExit = false;
```

---

## Key Methods

### Harbor Entry

```csharp
public void BeginHarborEntry(PortDefinitionSO port, Vector2 oceanPos, float oceanRot, Vector2 velocity)
{
    CurrentPort = port;
    LastOceanPosition = oceanPos;
    LastOceanRotation = oceanRot;
    LastOceanVelocity = velocity;
    CurrentTransition = TransitionState.EnteringHarbor;
}

public void CompleteHarborEntry()
{
    CurrentTransition = TransitionState.None;
}
```

### Docking State

```csharp
public void SetDocked(int dockIndex)
{
    CurrentDockIndex = dockIndex;
    CurrentTransition = TransitionState.Docked;
}

public void ClearDocked()
{
    CurrentDockIndex = -1;
    CurrentTransition = TransitionState.None;
}
```

### Harbor Exit

```csharp
public void BeginHarborExit()
{
    WasDockedOnExit = (CurrentTransition == TransitionState.Docked);
    CurrentTransition = TransitionState.ExitingHarbor;
}

public void CompleteHarborExit()
{
    CurrentPort = null;
    CurrentDockIndex = -1;
    WasDockedOnExit = false;
    CurrentTransition = TransitionState.None;
}
```

### State Queries

```csharp
public bool IsInHarbor => CurrentPort != null && CurrentTransition != TransitionState.ExitingHarbor;
public bool IsDocked => CurrentTransition == TransitionState.Docked;
public bool IsTransitioning => CurrentTransition == TransitionState.EnteringHarbor ||
                                CurrentTransition == TransitionState.ExitingHarbor ||
                                CurrentTransition == TransitionState.InTransit;
```

---

## Scene Transition Flow

### Ocean → Harbor

```
1. Player in Ocean_InAoI state
2. Player presses E
3. BeginHarborEntry() called with current position/rotation/velocity
4. Scene loads to HarborScene
5. HarborSceneManager reads CurrentPort, spawns appropriate content
6. Player spawned at harbor spawn point
7. CompleteHarborEntry() called
```

### Harbor → Ocean

```
1. Player in Harbor_AtExitZone state
2. Player presses E
3. BeginHarborExit() called
4. Scene loads to OceanScene
5. Player restored to LastOceanPosition/Rotation
6. If WasDockedOnExit, velocity = 0; else restore LastOceanVelocity
7. CompleteHarborExit() called
```

---

## Usage Example

```csharp
// In PlayerPortStateController
[SerializeField] private PortSceneStateHolder stateHolder;

private void EnterHarbor(PortDefinitionSO port)
{
    var rb = GetComponent<Rigidbody2D>();
    stateHolder.BeginHarborEntry(
        port,
        rb.position,
        rb.rotation,
        rb.linearVelocity
    );

    SceneManager.LoadScene("HarborScene");
}

private void ExitHarbor()
{
    stateHolder.BeginHarborExit();
    SceneManager.LoadScene("OceanScene");
}
```

---

## Integration Points

### Dependencies
- [[PortDefinitionSO]] - Port configuration reference

### Used By
- [[PlayerPortStateController]] - Initiates transitions
- [[HarborSceneManager]] - Reads port config on load
- [[PortReturnHandler]] - Restores ocean position (legacy)

---

## Related Files
- [[PortDefinitionSO]] - Port configuration
- [[PlayerPortStateController]] - State machine
- [[HarborSceneManager]] - Harbor scene setup

---

## Design Notes
- ScriptableObject survives scene transitions
- Stores minimal state (position, rotation, velocity)
- Clear transition lifecycle (Begin → Complete)
- Query properties for state checks
- WasDockedOnExit prevents velocity restore if player was stationary

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added velocity preservation
- **2025-01**: Added WasDockedOnExit flag

