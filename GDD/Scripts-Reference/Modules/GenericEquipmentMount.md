---
tags: [script, modules, component, visual, implemented]
script-type: MonoBehaviour
namespace: WOS.Modules
file-path: Assets/Scripts/Modules/GenericEquipmentMount.cs
status: IMPLEMENTED
size: ~586 lines
feature-group: modules
---

# GenericEquipmentMount.cs

## Quick Reference
**Type**: MonoBehaviour (per-mount)
**Namespace**: WOS.Modules
**File**: `Assets/Scripts/Modules/GenericEquipmentMount.cs`
**Size**: ~586 lines
**Dependencies**: EquipmentDefinitionSO, IVisualMount

---

## Purpose
Generic equipment mount component that works with any IVisualMount equipment. Attach to ship mount points to display turrets, torpedo launchers, or other visual equipment. Automatically configures itself from the equipment definition's geometry data.

---

## Usage

1. Add this component to a mount point on the ship
2. Call `SetEquipment()` with any EquipmentDefinitionSO that implements IVisualMount
3. The component creates visual and exit point transforms automatically

---

## Configuration

```csharp
[Header("Mount Configuration")]
[SerializeField] private float minRotation = -150f;
[SerializeField] private float maxRotation = 150f;
[SerializeField] private bool fullRotation = false;

[Header("Current Equipment")]
[SerializeField] private EquipmentDefinitionSO currentEquipment;

[Header("Generated Components")]
[SerializeField] private Transform rotatingPart;
[SerializeField] private SpriteRenderer spriteRenderer;
[SerializeField] private List<Transform> exitPoints;

[Header("State")]
[SerializeField] private float currentRotation = 0f;
[SerializeField] private float currentElevation = 0f;

[Header("Debug")]
[SerializeField] private bool drawGizmos = true;
[SerializeField] private Color exitPointColor = Color.red;
[SerializeField] private Color arcColor = Color.yellow;
```

---

## Properties

```csharp
public EquipmentDefinitionSO CurrentEquipment { get; }
public IVisualMount VisualMount { get; }
public float CurrentRotation { get; }
public float CurrentElevation { get; }
public bool IsRotating { get; }           // Currently rotating
public bool IsOnTarget { get; }           // Within 1 degree of target
public int ExitPointCount { get; }        // Number of barrels/tubes
public bool CanRotate { get; }            // From equipment data
public float RotationSpeed { get; }       // From equipment or 20 deg/s default
public bool HasEquipment { get; }         // Equipment installed?
```

---

## Events

```csharp
public event Action OnTargetReached;
public event Action<Vector3, Vector3, int> OnExitPointFired;  // position, direction, index
public event Action<EquipmentDefinitionSO> OnEquipmentChanged;
```

---

## Equipment Setup

### Install Equipment

```csharp
public void SetEquipment(EquipmentDefinitionSO equipment)
{
    ClearEquipment();

    if (equipment == null) return;

    currentEquipment = equipment;
    SetupFromEquipment(equipment);

    OnEquipmentChanged?.Invoke(equipment);
}

private void SetupFromEquipment(EquipmentDefinitionSO equipment)
{
    // Check if equipment implements IVisualMount
    visualMount = equipment as IVisualMount;

    if (visualMount == null)
    {
        Debug.LogWarning($"Equipment '{equipment.name}' does not implement IVisualMount");
        return;
    }

    // Get mount data
    mountData = visualMount.GetMountData();

    // Create rotating part
    CreateRotatingPart();

    // Apply visual
    ApplyVisual();

    // Create exit points
    CreateExitPoints();
}
```

### Clear Equipment

```csharp
public void ClearEquipment()
{
    // Destroy generated exit points
    foreach (var exitPoint in exitPoints)
    {
        Destroy(exitPoint.gameObject);
    }
    exitPoints.Clear();

    // Destroy rotating part
    if (rotatingPart != null && rotatingPart.parent == transform)
    {
        Destroy(rotatingPart.gameObject);
        rotatingPart = null;
    }

    currentEquipment = null;
    visualMount = null;
    mountData = null;
}
```

---

## Aiming

### Set Target Rotation

```csharp
public void SetTargetRotation(float angle)
{
    targetRotation = ClampToFiringArc(angle);
    isTracking = true;
}

public void SetTargetElevation(float angle)
{
    if (mountData != null)
    {
        targetElevation = Mathf.Clamp(angle, mountData.minElevation, mountData.maxElevation);
    }
}

public void SetTargetPosition(Vector2 worldPosition)
{
    Vector2 toTarget = worldPosition - (Vector2)transform.position;
    float angle = Mathf.Atan2(toTarget.y, toTarget.x) * Mathf.Rad2Deg - 90f;

    // Convert to mount-relative angle
    float mountAngle = transform.parent != null ? transform.parent.eulerAngles.z : 0f;
    float relativeAngle = angle - mountAngle;

    SetTargetRotation(relativeAngle);
}
```

### Control Methods

```csharp
public void StopTracking();                    // Hold current rotation
public void SetRotationImmediate(float angle); // Instant set (no animation)
public bool IsAngleInFiringArc(float angle);   // Check if angle valid
```

---

## Firing

### Sequential Fire

```csharp
public (Vector3 position, Vector3 direction) FireNextExitPoint()
{
    if (exitPoints.Count == 0)
    {
        return (transform.position, transform.up);
    }

    var exitPoint = exitPoints[currentExitIndex];
    Vector3 position = exitPoint.position;
    Vector3 direction = exitPoint.up;

    OnExitPointFired?.Invoke(position, direction, currentExitIndex);

    // Cycle to next exit point
    currentExitIndex = (currentExitIndex + 1) % exitPoints.Count;

    return (position, direction);
}
```

### Salvo Fire

```csharp
public (Vector3 position, Vector3 direction)[] FireAllExitPoints()
{
    var results = new (Vector3, Vector3)[exitPoints.Count];

    for (int i = 0; i < exitPoints.Count; i++)
    {
        var exitPoint = exitPoints[i];
        results[i] = (exitPoint.position, exitPoint.up);
        OnExitPointFired?.Invoke(exitPoint.position, exitPoint.up, i);
    }

    return results;
}
```

### Exit Point Access

```csharp
public Transform GetExitPoint(int index);
public Vector3[] GetAllExitPointPositions();
```

---

## Rotation System

### Update Rotation

```csharp
private void UpdateRotation()
{
    if (!CanRotate) return;

    if (Mathf.Abs(currentRotation - targetRotation) <= 0.5f)
    {
        currentRotation = targetRotation;
        ApplyRotation();
        OnTargetReached?.Invoke();
        return;
    }

    // Calculate rotation direction (shortest path)
    float delta = Mathf.DeltaAngle(currentRotation, targetRotation);
    float step = RotationSpeed * Time.deltaTime;

    if (Mathf.Abs(delta) <= step)
    {
        currentRotation = targetRotation;
    }
    else
    {
        currentRotation += Mathf.Sign(delta) * step;
    }

    currentRotation = ClampToFiringArc(currentRotation);
    ApplyRotation();
}

private void ApplyRotation()
{
    if (rotatingPart != null)
    {
        rotatingPart.localRotation = Quaternion.Euler(0, 0, currentRotation);
    }
}
```

### Firing Arc

```csharp
private float ClampToFiringArc(float angle)
{
    if (fullRotation) return NormalizeAngle(angle);
    return Mathf.Clamp(NormalizeAngle(angle), minRotation, maxRotation);
}

private float NormalizeAngle(float angle)
{
    while (angle > 180f) angle -= 360f;
    while (angle < -180f) angle += 360f;
    return angle;
}
```

---

## Editor Helpers

```csharp
public void RefreshSetup();  // Rebuild from current equipment
public void SetRotationLimits(float min, float max, bool full360 = false);
```

---

## Gizmos

- Yellow arc shows firing arc limits
- Green line shows current rotation
- Cyan line shows target rotation (when tracking)
- Red spheres show exit points
- Red lines show exit point directions

---

## Integration Points

### Dependencies
- [[EquipmentDefinitionSO]] - Equipment base class
- IVisualMount interface
- WeaponMountData structure

### Used By
- Turret systems
- Torpedo launchers
- Any rotating ship equipment
- Combat systems

---

## Related Files
- [[ModuleDefinitionSO]] - Module definitions
- [[TurretDefinitionSO]] - Turret definitions
- [[TorpedoDefinitionSO]] - Torpedo definitions

---

## Design Notes
- Works with any equipment implementing IVisualMount
- Auto-generates visual and exit point transforms
- Firing arc defined by mount, not equipment
- Supports both sequential and salvo firing
- Rotation uses shortest path algorithm
- On-target threshold is 1 degree
- Exit points cycle for sequential fire
- Gizmos visualize firing arc and state
- Handles both limited and full 360 rotation
- Equipment-agnostic design for flexibility

