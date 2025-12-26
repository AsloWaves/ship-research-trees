---
tags: [script, port, core, scene, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Core
file-path: Assets/Scripts/Port/Core/PortTransitionManager.cs
status: IMPLEMENTED
size: ~493 lines
feature-group: port
---

# PortTransitionManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton, DontDestroyOnLoad)
**Namespace**: WOS.Port.Core
**File**: `Assets/Scripts/Port/Core/PortTransitionManager.cs`
**Size**: ~493 lines
**Dependencies**: PortSceneStateHolder, LoadingScreenManager

---

## Purpose
Manages port scene transitions while keeping Mirror connection active. Coordinates between LoadingScreenManager and PortSceneStateHolder. Handles both client and server transition requests.

---

## Events

```csharp
public event Action<PortDefinitionSO> OnHarborEntryStarted;
public event Action<PortDefinitionSO> OnHarborEntryCompleted;
public event Action OnHarborExitStarted;
public event Action OnHarborExitCompleted;
public event Action<string> OnTransitionError;
```

---

## Harbor Entry Flow

```csharp
public void RequestEnterHarbor(PortDefinitionSO port, Vector2 pos, float rot, Vector2 vel)
{
    sceneState?.BeginHarborEntry(port, pos, rot, vel);

    if (isClient && !isServer)
        CmdRequestHarborEntry(port.portId, pos, rot, vel);
    else
        StartHarborTransition(port);
}

private IEnumerator HarborEntryRoutine(PortDefinitionSO port)
{
    isTransitioning = true;
    OnHarborEntryStarted?.Invoke(port);

    yield return LoadingScreenManager.Instance?.FadeOutAndShowLoading($"Entering {port.portName}...");

    AsyncOperation loadOp = SceneManager.LoadSceneAsync(harborSceneName);
    while (!loadOp.isDone) yield return null;

    sceneState?.CompleteHarborEntry();
    yield return LoadingScreenManager.Instance?.HideLoadingAndFadeIn();

    OnHarborEntryCompleted?.Invoke(port);
}
```

---

## Integration Points

### Dependencies
- [[PortSceneStateHolder]], [[LoadingScreenManager]], [[PortDatabaseSO]]

