---
tags: [script, port, player, state-machine, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Player
file-path: Assets/Scripts/Port/Player/PlayerPortStateController.cs
status: IMPLEMENTED
size: ~616 lines
feature-group: port
---

# PlayerPortStateController.cs

## Quick Reference
**Type**: NetworkBehaviour (Player State Machine)
**Namespace**: WOS.Port.Player
**File**: `Assets/Scripts/Port/Player/PlayerPortStateController.cs`
**Size**: ~616 lines
**Dependencies**: PortSceneStateHolder, PortDefinitionSO, Mirror networking

---

## Purpose
Player state machine for port system interactions. Manages transitions between ocean and harbor states, handles input for port entry/exit and docking, and synchronizes state across network. Replaces legacy PortReturnHandler functionality.

---

## Network Synchronization

```csharp
[SyncVar(hook = nameof(OnStateChanged))]
[SerializeField] private PortPlayerState currentState = PortPlayerState.Ocean_Normal;

[SyncVar]
[SerializeField] private string currentPortId = "";

[SyncVar]
[SerializeField] private int currentDockIndex = -1;
```

---

## Configuration

```csharp
[Header("References")]
[SerializeField] private PortSceneStateHolder stateHolder;

[Header("Input")]
[SerializeField] private KeyCode interactKey = KeyCode.E;

[Header("Detection")]
[SerializeField] private float zoneCheckInterval = 0.25f;  // Zone detection rate
```

---

## State Properties

```csharp
public PortPlayerState CurrentState => currentState;
public bool IsInOcean => currentState <= PortPlayerState.Ocean_InAoI;
public bool IsInHarbor => currentState >= PortPlayerState.Harbor_Sailing;
public bool IsDocked => currentState == PortPlayerState.Harbor_Docked;
public bool CanInteract => CanInteractInCurrentState();
```

---

## State Machine Flow

### Ocean States

```csharp
private void UpdateOceanState()
{
    if (!isLocalPlayer) return;

    var nearestPort = FindNearestPort();
    if (nearestPort == null)
    {
        if (currentState != PortPlayerState.Ocean_Normal)
            CmdSetState(PortPlayerState.Ocean_Normal);
        return;
    }

    float distance = Vector2.Distance(transform.position, nearestPort.OceanPosition);
    float aopRadius = nearestPort.GetAoPRadius();
    float aoiRadius = nearestPort.GetAoIRadius();

    if (distance <= aoiRadius)
        CmdSetState(PortPlayerState.Ocean_InAoI, nearestPort.PortId);
    else if (distance <= aopRadius)
        CmdSetState(PortPlayerState.Ocean_InAoP, nearestPort.PortId);
    else
        CmdSetState(PortPlayerState.Ocean_Normal);
}
```

### Harbor States

```csharp
// Set by HarborSceneManager via zone triggers
public void SetZoneState(PortPlayerState newState)
{
    if (!isServer) return;

    if (ValidateStateTransition(currentState, newState))
    {
        currentState = newState;
    }
}
```

---

## Input Handling

```csharp
private void Update()
{
    if (!isLocalPlayer) return;

    if (Input.GetKeyDown(interactKey))
    {
        HandleInteraction();
    }
}

private void HandleInteraction()
{
    switch (currentState)
    {
        case PortPlayerState.Ocean_InAoI:
            CmdRequestEnterHarbor(currentPortId);
            break;

        case PortPlayerState.Harbor_InDockZone:
            CmdRequestDock(currentDockIndex);
            break;

        case PortPlayerState.Harbor_Docked:
            CmdRequestUndock();
            break;

        case PortPlayerState.Harbor_AtExitZone:
            CmdRequestExitHarbor();
            break;
    }
}
```

---

## Server Commands

### Harbor Entry

```csharp
[Command]
private void CmdRequestEnterHarbor(string portId)
{
    if (currentState != PortPlayerState.Ocean_InAoI) return;

    var port = PortDatabase.GetPort(portId);
    if (port == null) return;

    // Store ocean state
    var rb = GetComponent<Rigidbody2D>();
    stateHolder.BeginHarborEntry(port, rb.position, rb.rotation, rb.linearVelocity);

    // Transition to harbor
    TargetLoadHarborScene(connectionToClient, portId);
}

[TargetRpc]
private void TargetLoadHarborScene(NetworkConnection conn, string portId)
{
    SceneManager.LoadScene("HarborScene");
}
```

### Docking

```csharp
[Command]
private void CmdRequestDock(int dockIndex)
{
    if (currentState != PortPlayerState.Harbor_InDockZone) return;

    currentState = PortPlayerState.Harbor_AutoDocking;
    currentDockIndex = dockIndex;

    StartCoroutine(AutoDockSequence(dockIndex));
}

private IEnumerator AutoDockSequence(int dockIndex)
{
    var dock = GetDockPosition(dockIndex);

    // Animate ship to dock position
    yield return MoveToPosition(dock.Position, dock.Rotation, 2.0f);

    currentState = PortPlayerState.Harbor_Docked;
    stateHolder.SetDocked(dockIndex);

    TargetShowDockedUI(connectionToClient);
}
```

### Harbor Exit

```csharp
[Command]
private void CmdRequestExitHarbor()
{
    if (currentState != PortPlayerState.Harbor_AtExitZone) return;

    stateHolder.BeginHarborExit();
    TargetLoadOceanScene(connectionToClient);
}

[TargetRpc]
private void TargetLoadOceanScene(NetworkConnection conn)
{
    SceneManager.LoadScene("OceanScene");
}
```

---

## Port Return (Ocean Restoration)

```csharp
// Called when player spawns in ocean after leaving harbor
public void RestoreOceanState()
{
    if (!stateHolder.IsInHarbor) return;

    var rb = GetComponent<Rigidbody2D>();
    rb.position = stateHolder.LastOceanPosition;
    rb.rotation = stateHolder.LastOceanRotation;

    // Only restore velocity if player wasn't docked
    if (!stateHolder.WasDockedOnExit)
    {
        rb.linearVelocity = stateHolder.LastOceanVelocity;
    }
    else
    {
        rb.linearVelocity = Vector2.zero;
    }

    stateHolder.CompleteHarborExit();
}
```

---

## State Transition Validation

```csharp
private bool ValidateStateTransition(PortPlayerState from, PortPlayerState to)
{
    switch (from)
    {
        case PortPlayerState.Ocean_Normal:
            return to == PortPlayerState.Ocean_InAoP;

        case PortPlayerState.Ocean_InAoP:
            return to == PortPlayerState.Ocean_Normal ||
                   to == PortPlayerState.Ocean_InAoI;

        case PortPlayerState.Ocean_InAoI:
            return to == PortPlayerState.Ocean_InAoP ||
                   to == PortPlayerState.Harbor_Sailing;

        case PortPlayerState.Harbor_Sailing:
            return to == PortPlayerState.Harbor_InDockZone ||
                   to == PortPlayerState.Harbor_AtExitZone;

        case PortPlayerState.Harbor_InDockZone:
            return to == PortPlayerState.Harbor_Sailing ||
                   to == PortPlayerState.Harbor_AutoDocking;

        case PortPlayerState.Harbor_AutoDocking:
            return to == PortPlayerState.Harbor_Docked;

        case PortPlayerState.Harbor_Docked:
            return to == PortPlayerState.Harbor_Undocking;

        case PortPlayerState.Harbor_Undocking:
            return to == PortPlayerState.Harbor_Sailing;

        case PortPlayerState.Harbor_AtExitZone:
            return to == PortPlayerState.Harbor_Sailing ||
                   to == PortPlayerState.Ocean_InAoI;
    }
    return false;
}
```

---

## State Change Hook

```csharp
private void OnStateChanged(PortPlayerState oldState, PortPlayerState newState)
{
    // Update UI prompts
    UpdateInteractionPrompt(newState);

    // Toggle combat eligibility
    var combat = GetComponent<CombatController>();
    combat?.SetInvincible(newState >= PortPlayerState.Ocean_InAoP);

    // Notify other systems
    OnPortStateChanged?.Invoke(newState);
}
```

---

## Events

```csharp
public event Action<PortPlayerState> OnPortStateChanged;
public event Action<PortDefinitionSO> OnEnteredHarbor;
public event Action OnExitedHarbor;
public event Action<int> OnDocked;
public event Action OnUndocked;
```

---

## Integration Points

### Dependencies
- [[PortSceneStateHolder]] - State persistence
- [[PortDefinitionSO]] - Port configuration
- [[PortEnums]] - State enum
- Mirror networking

### Used By
- [[HarborSceneManager]] - Sets zone states
- [[DockingSquareController]] - Dock zone detection
- [[ExitZoneController]] - Exit zone detection
- [[PortInteractionUI]] - UI prompts

---

## Related Files
- [[PortSceneStateHolder]] - State persistence
- [[HarborSceneManager]] - Zone management
- [[PortEnums]] - State definitions

---

## Design Notes
- Server-authoritative state machine
- SyncVar with hook for client updates
- Validation prevents invalid transitions
- Replaces legacy PortReturnHandler
- Auto-docking uses coroutine animation
- Combat invincibility in AoP zones

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added auto-docking animation
- **2025-01**: Merged PortReturnHandler functionality
- **2025-01**: Added state transition validation

