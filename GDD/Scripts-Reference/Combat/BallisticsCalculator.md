---
tags: [script, combat, ballistics, static, implemented]
script-type: Static Class
namespace: WOS.Combat.Controllers
file-path: Assets/Scripts/Combat/Controllers/BallisticsCalculator.cs
status: ✅ IMPLEMENTED
size: ~10 KB (389 lines)
feature-group: combat
---

# BallisticsCalculator.cs

## Quick Reference
**Type**: Static Class
**Namespace**: WOS.Combat.Controllers
**File**: `Assets/Scripts/Combat/Controllers/BallisticsCalculator.cs`
**Size**: ~10 KB (389 lines)
**Dependencies**: BallisticsData

---

## Purpose
Server-side ballistics calculation system providing trajectory calculation, hit detection, and damage determination.

This is the **core physics engine** for naval combat. It calculates:
- Firing solutions with lead angles
- Ballistic trajectories with gravity and drag
- Armor penetration mechanics
- Ricochet determination
- Damage with fire/flood chances
- Splash damage for HE shells

---

## Implements GDD Features
- [[Surface-Combat]] - Ballistics specifications
- Armor penetration mechanics
- Shell types (AP, HE, SAP) behavior

---

## Key Methods

### Trajectory Calculation
```csharp
static FiringSolution CalculateFiringSolution(
    Vector3 origin,           // Firing position
    Vector3 targetPos,        // Target position
    Vector3 targetVel,        // Target velocity
    BallisticProfile profile, // Shell characteristics
    BallisticEnvironment env  // Weather conditions
)
```

### Trajectory Generation
```csharp
static TrajectoryData GenerateTrajectory(
    Vector3 origin,
    float azimuth,
    float elevation,
    float muzzleVelocity,
    int pointCount = 50
)
```

### Hit Calculation
```csharp
static HitResult CalculateHit(
    ProjectileData projectile,
    Vector3 hitPoint,
    Vector3 hitNormal,
    float armorThickness,
    bool isAboveWaterline,
    string compartment = "Hull"
)
```

### Splash Damage
```csharp
static float CalculateSplashDamage(
    Vector3 detonationPoint,
    Vector3 targetPoint,
    float baseDamage,
    float splashRadius
)
```

---

## Physics Constants

```csharp
public static class BallisticsConstants
{
    const float Gravity = 9.81f;              // m/s²
    const float DragCoefficient = 0.3f;       // Typical shell Cd
    const float VelocityRetentionPerKm = 0.92f; // 8% loss per km
    const float BaseDispersionPerKm = 15f;    // Meters dispersion per km
    const float MinEngagementRange = 500f;    // Meters
    const float MaxEngagementRange = 40000f;  // Meters (40km)
}
```

---

## Firing Solution Algorithm

### Step 1: Range Validation
```csharp
solution.range = Vector3.Distance(origin, targetPos);
solution.isInRange = solution.range >= MinEngagementRange
                  && solution.range <= profile.maxRange;
```

### Step 2: Flight Time Calculation
```csharp
solution.flightTime = profile.CalculateFlightTime(solution.range);
```

### Step 3: Lead Prediction
```csharp
// Predict where target will be when shell arrives
solution.predictedPosition = targetPos + (targetVel * solution.flightTime);

// Apply wind drift correction
solution.predictedPosition = environment.ApplyWindDrift(
    solution.predictedPosition, solution.flightTime);
```

### Step 4: Aim Angles
```csharp
Vector3 aimDirection = solution.predictedPosition - origin;
solution.azimuthAngle = Mathf.Atan2(aimDirection.x, aimDirection.z) * Mathf.Rad2Deg;
solution.elevationAngle = CalculateElevationAngle(origin, solution.predictedPosition, muzzleVelocity);
```

---

## Penetration Mechanics

### Armor Interaction
```csharp
// Calculate impact angle effect
float angleMultiplier = 1f / Mathf.Cos(impactAngle * Mathf.Deg2Rad);
float effectiveThickness = armorThickness * Mathf.Min(angleMultiplier, 3f);

// Get shell penetration at impact velocity
float shellPenetration = projectile.penetration *
    (projectile.currentVelocity / projectile.muzzleVelocity);

// Determine result
bool penetrated = shellPenetration >= effectiveThickness;
```

### Ricochet Calculation
```csharp
// Steep angles cause ricochets
if (impactAngle > 60f)
{
    float ricochetChance = (impactAngle - 60f) / 30f; // 0-100% from 60-90 degrees
    if (Random.value < ricochetChance)
    {
        result.didRicochet = true;
        result.didPenetrate = false;
    }
}
```

### Overpenetration
```csharp
// AP shells need minimum armor to arm fuse
if (penetrated && projectile.ammoType == AmmunitionType.AP)
{
    float fuseArmThreshold = projectile.shellWeight * 0.01f;
    if (armorThickness < fuseArmThreshold)
    {
        result.didOverpenetrate = true;
        result.damageDealt = baseDamage * 0.1f; // Minimal damage
    }
}
```

---

## Damage Calculation by Shell Type

| Shell Type | Damage Modifier | Fire Chance | Notes |
|------------|-----------------|-------------|-------|
| AP | 100% | 10% | Best penetration |
| HE | 80% | 25% | Splash damage, low pen |
| SAP | 90% | 15% | Balanced |

### Critical Hit System
```csharp
// Critical compartments: Magazine, Engine, Bridge, Rudder, FireControl
if (IsCriticalCompartment(compartment))
{
    if (Random.value < 0.2f) // 20% critical chance
    {
        result.causedCritical = true;
        result.damageDealt *= 2f; // Double damage
    }
}
```

### Flooding
```csharp
// Below waterline hits can cause flooding
if (!isAboveWaterline && didPenetrate)
{
    result.causedFlooding = Random.value < 0.4f; // 40% chance
}
```

---

## Integration Points

### Dependencies
- [[BallisticsData]] - Profile, trajectory, hit result structures

### Used By
- [[TargetingSystem]] - Firing solution requests
- [[ProjectileManager]] - Hit result calculations
- [[WeaponController]] - Accuracy calculations

---

## Example Usage

### Get Firing Solution
```csharp
var solution = BallisticsCalculator.CalculateFiringSolution(
    gunPosition,
    targetPosition,
    targetVelocity,
    shellProfile,
    currentWeather
);

if (solution.isValid)
{
    AimTurret(solution.azimuthAngle, solution.elevationAngle);
}
```

### Calculate Hit Result
```csharp
HitResult result = BallisticsCalculator.CalculateHit(
    projectileData,
    hit.point,
    hit.normal,
    armorThickness,
    hit.point.y > 0, // above waterline
    "Engine"
);

if (result.didPenetrate)
{
    ApplyDamage(result.damageDealt);
    if (result.causedFire) StartFire();
    if (result.causedFlooding) StartFlooding();
}
```

---

## Related Files
- [[BallisticsData]] - Data structures
- [[TargetingSystem]] - Uses for firing solutions
- [[ProjectileManager]] - Uses for hit detection

---

## Testing Notes
- Uses simplified ballistics (not full physics simulation)
- Elevation calculation uses quadratic formula
- Low arc trajectory preferred (naval combat standard)
- Random values for ricochet, fire, flood chances

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added overpenetration mechanics
- **2025-01**: Added critical hit system
