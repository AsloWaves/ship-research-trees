---
tags: [script, port, ocean, trigger, implemented]
script-type: MonoBehaviour
namespace: WOS.Port.Ocean
file-path: Assets/Scripts/Port/Ocean/PortZoneTrigger.cs
status: IMPLEMENTED
size: ~152 lines
feature-group: port
---

# PortZoneTrigger.cs

## Quick Reference
**Type**: MonoBehaviour (Trigger Component)
**Namespace**: WOS.Port.Ocean
**File**: `Assets/Scripts/Port/Ocean/PortZoneTrigger.cs`
**Size**: ~152 lines
**Dependencies**: PortZoneManager, PortDefinitionSO, CircleCollider2D

---

## Purpose
Trigger component attached to AoP/AoI colliders in the ocean scene. Detects player ship entry/exit and notifies PortZoneManager. Server-only trigger processing.

---

## ZoneType Enum

```csharp
public enum ZoneType
{
    AoP,  // Area of Protection (outer zone)
    AoI   // Area of Interaction (inner zone)
}
```

---

## Configuration

```csharp
[SerializeField] private ZoneType zoneType;
[SerializeField] private PortDefinitionSO portDefinition;
private PortZoneManager zoneManager;
```

---

## Initialization

```csharp
public void Initialize(PortZoneManager manager, PortDefinitionSO portDef, ZoneType type)
{
    zoneManager = manager;
    portDefinition = portDef;
    zoneType = type;
}
```

---

## Trigger Detection

```csharp
private void OnTriggerEnter2D(Collider2D other)
{
    if (!NetworkServer.active) return;

    var networkIdentity = other.GetComponentInParent<NetworkIdentity>();
    if (networkIdentity == null || !IsPlayerShip(other.gameObject)) return;

    switch (zoneType)
    {
        case ZoneType.AoP:
            zoneManager.OnPlayerEnteredAoP(networkIdentity, portDefinition);
            break;
        case ZoneType.AoI:
            zoneManager.OnPlayerEnteredAoI(networkIdentity, portDefinition);
            break;
    }
}
```

---

## Integration Points

### Used By
- [[PortZoneManager]] - Creates and initializes triggers

---

## Related Files
- [[PortZoneManager]] - Parent manager
- [[PortDefinitionSO]] - Port configuration

