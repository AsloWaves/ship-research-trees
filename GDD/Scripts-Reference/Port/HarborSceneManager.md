---
tags: [script, port, harbor, manager, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Harbor
file-path: Assets/Scripts/Port/Harbor/HarborSceneManager.cs
status: IMPLEMENTED
size: ~633 lines
feature-group: port
---

# HarborSceneManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Port.Harbor
**File**: `Assets/Scripts/Port/Harbor/HarborSceneManager.cs`
**Size**: ~633 lines
**Dependencies**: PortDefinitionSO, PortSceneStateHolder, PortVisualStyleSO

---

## Purpose
Server-authoritative manager for harbor scenes. Singleton that loads PortDefinitionSO at runtime, spawns docks/buildings/decorations from visual style, handles dock and exit zone detection, and sends UI prompts to clients via TargetRpc.

---

## Singleton Pattern

```csharp
public static HarborSceneManager Instance { get; private set; }

private void Awake()
{
    if (Instance != null && Instance != this)
    {
        Destroy(gameObject);
        return;
    }
    Instance = this;
}
```

---

## Configuration

```csharp
[Header("References")]
[SerializeField] private PortSceneStateHolder stateHolder;

[Header("Prefabs")]
[SerializeField] private GameObject dockingSquarePrefab;
[SerializeField] private GameObject exitZonePrefab;

[Header("Runtime")]
[SerializeField] private PortDefinitionSO currentPort;
[SerializeField] private List<DockingSquareController> activeDocks = new();
[SerializeField] private ExitZoneController activeExitZone;
```

---

## Initialization

```csharp
public override void OnStartServer()
{
    base.OnStartServer();

    // Load port from state holder (set before scene transition)
    currentPort = stateHolder.CurrentPort;

    if (currentPort == null)
    {
        Debug.LogError("HarborSceneManager: No port in state holder!");
        return;
    }

    InitializeHarbor();
}

private void InitializeHarbor()
{
    SpawnDockingSquares();
    SpawnExitZone();
    SpawnBuildings();
    SpawnDecorations();

    stateHolder.CompleteHarborEntry();
}
```

---

## Spawning Methods

### Docking Squares

```csharp
private void SpawnDockingSquares()
{
    for (int i = 0; i < currentPort.DockingSquares.Length; i++)
    {
        var data = currentPort.DockingSquares[i];

        var dockObj = Instantiate(dockingSquarePrefab, data.Position, Quaternion.Euler(0, 0, data.Rotation));
        NetworkServer.Spawn(dockObj);

        var controller = dockObj.GetComponent<DockingSquareController>();
        controller.Initialize(i, data.Size, data.IsLargeDock);

        activeDocks.Add(controller);
    }
}
```

### Exit Zone

```csharp
private void SpawnExitZone()
{
    var exitObj = Instantiate(
        exitZonePrefab,
        currentPort.ExitZonePosition,
        Quaternion.identity
    );
    NetworkServer.Spawn(exitObj);

    activeExitZone = exitObj.GetComponent<ExitZoneController>();
    activeExitZone.Initialize(currentPort.ExitZoneRadius);
}
```

### Buildings & Decorations

```csharp
private void SpawnBuildings()
{
    var style = currentPort.VisualStyle;

    foreach (var placement in currentPort.Buildings)
    {
        var prefab = style.GetBuildingPrefab(placement.BuildingType);
        var obj = Instantiate(prefab, placement.Position, Quaternion.Euler(0, 0, placement.Rotation));
        NetworkServer.Spawn(obj);
    }
}

private void SpawnDecorations()
{
    var style = currentPort.VisualStyle;

    foreach (var placement in currentPort.Decorations)
    {
        var prefab = style.GetDecorationPrefab(placement.DecorationType);
        var obj = Instantiate(prefab, placement.Position, Quaternion.Euler(0, 0, placement.Rotation));
        NetworkServer.Spawn(obj);
    }
}
```

---

## Zone Detection (Server-Only)

### Dock Zone Entry

```csharp
[Server]
public void OnPlayerEnteredDockZone(NetworkIdentity player, int dockIndex)
{
    var stateController = player.GetComponent<PlayerPortStateController>();
    if (stateController == null) return;

    stateController.SetZoneState(PortPlayerState.Harbor_InDockZone);
    stateController.SetCurrentDock(dockIndex);

    TargetShowDockPrompt(player.connectionToClient, dockIndex);
}

[Server]
public void OnPlayerExitedDockZone(NetworkIdentity player, int dockIndex)
{
    var stateController = player.GetComponent<PlayerPortStateController>();
    if (stateController == null) return;

    if (stateController.CurrentState == PortPlayerState.Harbor_InDockZone)
    {
        stateController.SetZoneState(PortPlayerState.Harbor_Sailing);
        TargetHideDockPrompt(player.connectionToClient);
    }
}
```

### Exit Zone Detection

```csharp
[Server]
public void OnPlayerEnteredExitZone(NetworkIdentity player)
{
    var stateController = player.GetComponent<PlayerPortStateController>();
    if (stateController == null) return;

    stateController.SetZoneState(PortPlayerState.Harbor_AtExitZone);
    TargetShowExitPrompt(player.connectionToClient);
}

[Server]
public void OnPlayerExitedExitZone(NetworkIdentity player)
{
    var stateController = player.GetComponent<PlayerPortStateController>();
    if (stateController == null) return;

    if (stateController.CurrentState == PortPlayerState.Harbor_AtExitZone)
    {
        stateController.SetZoneState(PortPlayerState.Harbor_Sailing);
        TargetHideExitPrompt(player.connectionToClient);
    }
}
```

---

## Client UI Prompts (TargetRpc)

```csharp
[TargetRpc]
private void TargetShowDockPrompt(NetworkConnection conn, int dockIndex)
{
    PortInteractionUI.Instance?.ShowPrompt($"Press E to dock at Berth {dockIndex + 1}");
}

[TargetRpc]
private void TargetHideDockPrompt(NetworkConnection conn)
{
    PortInteractionUI.Instance?.HidePrompt();
}

[TargetRpc]
private void TargetShowExitPrompt(NetworkConnection conn)
{
    PortInteractionUI.Instance?.ShowPrompt("Press E to leave harbor");
}

[TargetRpc]
private void TargetHideExitPrompt(NetworkConnection conn)
{
    PortInteractionUI.Instance?.HidePrompt();
}

[TargetRpc]
private void TargetShowDockedUI(NetworkConnection conn)
{
    PortServicesUI.Instance?.Show(currentPort);
}
```

---

## Dock Management

```csharp
public Vector2 GetDockPosition(int dockIndex)
{
    if (dockIndex < 0 || dockIndex >= activeDocks.Count)
        return Vector2.zero;

    return activeDocks[dockIndex].transform.position;
}

public float GetDockRotation(int dockIndex)
{
    if (dockIndex < 0 || dockIndex >= activeDocks.Count)
        return 0f;

    return activeDocks[dockIndex].transform.eulerAngles.z;
}

public bool IsDockOccupied(int dockIndex)
{
    if (dockIndex < 0 || dockIndex >= activeDocks.Count)
        return true;

    return activeDocks[dockIndex].IsOccupied;
}
```

---

## Port Query

```csharp
public PortDefinitionSO GetCurrentPort() => currentPort;
public string GetPortName() => currentPort?.PortName ?? "Unknown";
public Nationality GetNationality() => currentPort?.Nationality ?? Nationality.Neutral;
```

---

## Cleanup

```csharp
private void OnDestroy()
{
    if (Instance == this)
        Instance = null;
}

public override void OnStopServer()
{
    base.OnStopServer();

    // Cleanup spawned objects
    foreach (var dock in activeDocks)
    {
        if (dock != null)
            NetworkServer.Destroy(dock.gameObject);
    }
    activeDocks.Clear();

    if (activeExitZone != null)
        NetworkServer.Destroy(activeExitZone.gameObject);
}
```

---

## Integration Points

### Dependencies
- [[PortSceneStateHolder]] - Current port reference
- [[PortDefinitionSO]] - Port configuration
- [[PortVisualStyleSO]] - Visual assets
- [[DockingSquareController]] - Dock triggers
- [[ExitZoneController]] - Exit trigger

### Used By
- [[PlayerPortStateController]] - State updates
- [[DockingSquareController]] - Delegates detection
- [[ExitZoneController]] - Delegates detection
- [[PortInteractionUI]] - UI prompts

---

## Related Files
- [[DockingSquareController]] - Dock triggers
- [[ExitZoneController]] - Exit trigger
- [[PlayerPortStateController]] - Player state
- [[PortDefinitionSO]] - Port config

---

## Design Notes
- Singleton for global access
- Server spawns all harbor content
- NetworkServer.Spawn for network visibility
- TargetRpc for player-specific UI
- Single scene loads different ports via PortDefinitionSO
- Visual style separation for nationality theming

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added TargetRpc UI prompts
- **2025-01**: Added visual style integration
- **2025-01**: Added dock occupied tracking

