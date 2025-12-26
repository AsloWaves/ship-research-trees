---
tags: [script, port, data, serializable, implemented]
script-type: Serializable Class
namespace: WOS.ScriptableObjects
file-path: Assets/Scripts/ScriptableObjects/Port/DockingSquareData.cs
status: IMPLEMENTED
size: ~100 lines
feature-group: port
---

# DockingSquareData.cs

## Quick Reference
**Type**: Serializable Class (Configuration Data)
**Namespace**: WOS.ScriptableObjects
**File**: `Assets/Scripts/ScriptableObjects/Port/DockingSquareData.cs`
**Size**: ~100 lines
**Dependencies**: None

---

## Purpose
Configuration data for a single docking square in a harbor. Defines position, orientation, and auto-dock/undock behavior. Used as array element in PortDefinitionSO.

---

## Fields

```csharp
[Header("Identity")]
public int squareIndex;
public string displayName = "Dock";

[Header("Position & Orientation")]
public Vector2 position;
public float dockRotation = 0f;
public float exitRotation = 180f;

[Header("Docking Behavior")]
public Vector2 approachDirection = Vector2.up;
public float safeExitDistance = 30f;
public float autoDockSpeed = 5f;
public float dockRotationTime = 1.5f;

[Header("Trigger Zone")]
public float triggerRadius = 15f;
public Color highlightColor;
```

---

## Utility Methods

```csharp
public Vector2 GetExitPosition()
{
    float exitAngleRad = exitRotation * Mathf.Deg2Rad;
    Vector2 exitDir = new Vector2(Mathf.Cos(exitAngleRad), Mathf.Sin(exitAngleRad));
    return position + exitDir * safeExitDistance;
}

public bool IsInTriggerZone(Vector2 testPosition)
{
    return Vector2.Distance(testPosition, position) <= triggerRadius;
}

public static DockingSquareData CreateDefault(int index, Vector2 pos);
```

---

## Integration Points

### Used By
- [[PortDefinitionSO]], [[HarborSceneManager]], [[DockingSquareController]]

