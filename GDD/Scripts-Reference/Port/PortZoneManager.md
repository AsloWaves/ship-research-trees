---
tags: [script, port, ocean, manager, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Ocean
file-path: Assets/Scripts/Port/Ocean/PortZoneManager.cs
status: IMPLEMENTED
size: ~884 lines
feature-group: port
---

# PortZoneManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Port.Ocean
**File**: `Assets/Scripts/Port/Ocean/PortZoneManager.cs`
**Size**: ~884 lines
**Dependencies**: PortDefinitionSO, PortZoneTrigger, PortBuoyLight, Light2D

---

## Purpose
Server-authoritative manager for port zone detection in the ocean scene. Creates AoP/AoI colliders from PortDefinitionSO array, spawns visual indicators (light buoys, water color zones), tracks player zone states, and syncs state to clients via TargetRpc.

---

## Configuration

```csharp
[Header("Port Configuration")]
[SerializeField] private PortDefinitionSO[] portDefinitions;

[Header("Buoy Configuration")]
[SerializeField] private bool useLightBuoys = true;
[SerializeField] private float aopBuoyIntensity = 2f;
[SerializeField] private float aoiBuoyIntensity = 1.5f;
[SerializeField] private float buoyLightRadius = 15f;

[Header("Water Color Zones")]
[SerializeField] private bool enableWaterColorZones = true;
[SerializeField] private Color aopWaterTint;
[SerializeField] private Color aoiWaterTint;
```

---

## Runtime Data

```csharp
public class PortZoneInstance
{
    public PortDefinitionSO definition;
    public CircleCollider2D aopCollider;
    public CircleCollider2D aoiCollider;
    public List<PortBuoyLight> lightBuoys;
}

public class PortZoneState
{
    public PortDefinitionSO currentPort;
    public bool isInAoP;
    public bool isInAoI;
}
```

---

## Zone Detection (Server)

```csharp
[Server]
public void OnPlayerEnteredAoP(NetworkIdentity player, PortDefinitionSO portDef)
{
    playerZoneStates[player] = new PortZoneState { currentPort = portDef, isInAoP = true };
    TargetOnEnteredAoP(player.connectionToClient, portDef.portId, portDef.portName);
}

[Server]
public void OnPlayerEnteredAoI(NetworkIdentity player, PortDefinitionSO portDef)
{
    playerZoneStates[player].isInAoI = true;
    TargetOnEnteredAoI(player.connectionToClient, portDef.portId, portDef.portName);
}
```

---

## Client RPCs

```csharp
[TargetRpc]
private void TargetOnEnteredAoI(NetworkConnection target, string portId, string portName)
{
    GetLocalPlayerPortState()?.SetZoneState(PortPlayerState.Ocean_InAoI);
    PortInteractionUI.Instance?.ShowEnterPortPrompt(portName);
}
```

---

## Buoy Control

```csharp
public void SetBuoyAnimationsEnabled(string portId, bool enabled);
public void SetBuoyAnimationType(string portId, PortBuoyLight.AnimationType animType);
public void ToggleAllBuoyLights(bool enabled);
```

---

## Integration Points

### Dependencies
- [[PortDefinitionSO]], [[PortZoneTrigger]], [[PortBuoyLight]], [[PortInteractionUI]]

---

## Related Files
- [[PortZoneTrigger]] - Zone triggers
- [[PortBuoyLight]] - Light buoys

