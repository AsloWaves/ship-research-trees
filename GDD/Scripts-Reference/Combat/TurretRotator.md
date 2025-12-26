---
tags: [script, combat, turrets, animation, implemented]
script-type: MonoBehaviour
namespace: WOS.Combat.Controllers
file-path: Assets/Scripts/Combat/Controllers/TurretRotator.cs
status: ✅ IMPLEMENTED
size: ~12 KB (458 lines)
feature-group: combat
---

# TurretRotator.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Combat.Controllers
**File**: `Assets/Scripts/Combat/Controllers/TurretRotator.cs`
**Size**: ~12 KB (458 lines)
**Dependencies**: TurretDefinitionSO

---

## Purpose
Controls individual turret rotation, muzzle point management, and firing coordination for ship turrets.

This is the **per-turret controller** that manages:
- Turret rotation toward targets
- Firing arc limits
- Barrel/muzzle point positions
- Sequential and salvo firing
- Visual sprite updates

---

## Implements GDD Features
- [[Surface-Combat]] - Turret mechanics
- [[Ship-Customization]] - Turret configurations

---

## Key Components

### Properties
```
TurretDefinition (TurretDefinitionSO): Turret configuration
CurrentRotation (float): Current angle in degrees
TargetRotation (float): Target angle in degrees
IsRotating (bool): Whether turret is moving
IsOnTarget (bool): Within 1 degree of target
BarrelCount (int): Number of muzzle points
RotationSpeed (float): Degrees per second
```

### Public Methods
- `SetTurretDefinition(TurretDefinitionSO)` - Set turret config at runtime
- `SetTargetRotation(float angle)` - Set target angle (ship-relative)
- `SetTargetPosition(Vector2 worldPos)` - Aim at world position
- `StopTracking()` - Hold current rotation
- `FireNextBarrel()` - Fire next barrel in sequence
- `FireAllBarrels()` - Fire all barrels simultaneously (salvo)
- `IsAngleInFiringArc(float angle)` - Check if angle is valid
- `SetRotationImmediate(float angle)` - Instant rotation (no animation)

### Events
```csharp
event Action OnTargetReached;                        // Turret reached target angle
event Action<Vector3, Vector3, int> OnBarrelFired;   // Barrel fired (pos, dir, index)
```

---

## Configuration

### Inspector Fields
```
[Header("Turret Definition")]
turretDefinition (TurretDefinitionSO): Stats and configuration

[Header("Turret Components")]
rotatingPart (Transform): The rotating child transform
muzzlePoints (List<Transform>): Barrel spawn points
spriteRenderer (SpriteRenderer): Turret visual

[Header("Rotation Limits")]
minRotation (float, -150): Min angle (ship-relative)
maxRotation (float, 150): Max angle (ship-relative)
fullRotation (bool): Allow 360 degree rotation

[Header("State")]
currentRotation (float, 0): Current angle

[Header("Debug")]
drawGizmos (bool, true): Draw firing arc gizmos
muzzleGizmoColor (Color, red): Muzzle point color
arcGizmoColor (Color, yellow): Firing arc color
```

---

## Rotation System

### Rotation Logic
```csharp
private void UpdateRotation()
{
    if (Mathf.Abs(currentRotation - targetRotation) <= 0.5f)
    {
        currentRotation = targetRotation;
        OnTargetReached?.Invoke();
        return;
    }

    // Calculate shortest rotation path
    float delta = Mathf.DeltaAngle(currentRotation, targetRotation);
    float step = RotationSpeed * Time.deltaTime;

    if (Mathf.Abs(delta) <= step)
        currentRotation = targetRotation;
    else
        currentRotation += Mathf.Sign(delta) * step;

    currentRotation = ClampToFiringArc(currentRotation);
    ApplyRotation();
}
```

### Firing Arc Clamping
```csharp
private float ClampToFiringArc(float angle)
{
    if (fullRotation) return NormalizeAngle(angle);
    return Mathf.Clamp(NormalizeAngle(angle), minRotation, maxRotation);
}
```

### Angle Normalization
```csharp
private float NormalizeAngle(float angle)
{
    while (angle > 180f) angle -= 360f;
    while (angle < -180f) angle += 360f;
    return angle;
}
```

---

## Firing System

### Sequential Firing
```csharp
public (Vector3 position, Vector3 direction) FireNextBarrel()
{
    var muzzle = muzzlePoints[currentBarrelIndex];
    Vector3 position = muzzle.position;
    Vector3 direction = muzzle.up; // Muzzle points "up" in 2D

    OnBarrelFired?.Invoke(position, direction, currentBarrelIndex);

    // Cycle to next barrel
    currentBarrelIndex = (currentBarrelIndex + 1) % muzzlePoints.Count;

    return (position, direction);
}
```

### Salvo Firing
```csharp
public (Vector3 position, Vector3 direction)[] FireAllBarrels()
{
    var results = new (Vector3, Vector3)[muzzlePoints.Count];

    for (int i = 0; i < muzzlePoints.Count; i++)
    {
        var muzzle = muzzlePoints[i];
        results[i] = (muzzle.position, muzzle.up);
        OnBarrelFired?.Invoke(muzzle.position, muzzle.up, i);
    }

    return results;
}
```

---

## Muzzle Point Management

### Auto-Discovery
```csharp
private void FindMuzzlePoints()
{
    muzzlePoints.Clear();
    var searchRoot = rotatingPart ?? transform;

    // Look for "Muzzle_0", "Muzzle_1", etc.
    for (int i = 0; i < 10; i++)
    {
        var muzzle = searchRoot.Find($"Muzzle_{i}");
        if (muzzle != null)
            muzzlePoints.Add(muzzle);
        else if (i == 0)
        {
            // Try "Muzzle" without number for single barrel
            muzzle = searchRoot.Find("Muzzle");
            if (muzzle != null) muzzlePoints.Add(muzzle);
            break;
        }
        else break;
    }
}
```

### Editor Creation
```csharp
public void CreateMuzzlePoints(int count)
{
    var parent = rotatingPart ?? transform;

    for (int i = 0; i < count; i++)
    {
        var muzzle = new GameObject($"Muzzle_{i}");
        muzzle.transform.SetParent(parent);
        muzzle.transform.localPosition = new Vector3(
            (i - (count - 1) * 0.5f) * 0.2f, // Spread horizontally
            0.5f,  // Forward offset
            0
        );
        muzzlePoints.Add(muzzle.transform);
    }
}
```

---

## Integration Points

### Dependencies
- [[TurretDefinitionSO]] - Turret configuration

### Used By
- [[WeaponController]] - Ship-level weapon management
- **Ship Prefabs** - Attached to turret objects

---

## Example Usage

### Setting Target by Position
```csharp
// Aim at enemy ship
turret.SetTargetPosition(enemyShip.transform.position);
```

### Firing
```csharp
// Wait until on target
if (turret.IsOnTarget)
{
    var (muzzlePos, muzzleDir) = turret.FireNextBarrel();
    SpawnProjectile(muzzlePos, muzzleDir);
}
```

### Checking Firing Arc
```csharp
// Can we hit this angle?
float targetAngle = CalculateAngleToTarget();
if (turret.IsAngleInFiringArc(targetAngle))
{
    turret.SetTargetRotation(targetAngle);
}
```

---

## Gizmo Visualization

```
Green line: Current rotation direction
Cyan line: Target rotation direction (when tracking)
Yellow arc: Firing arc limits
Red spheres: Muzzle point positions
Red lines: Muzzle forward directions
```

---

## Related Files
- [[TurretDefinitionSO]] - Turret configuration asset
- [[WeaponController]] - Ship weapon coordinator
- [[ProjectileManager]] - Projectile spawning

---

## Testing Notes
- Auto-finds components if not assigned
- Supports 1-10 barrels per turret
- Rotation speed from TurretDefinitionSO
- Full 360 rotation optional

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added salvo firing
- **2025-01**: Added editor muzzle point creation
