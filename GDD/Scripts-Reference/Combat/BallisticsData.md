---
tags: [script, combat, data, ballistics, implemented]
script-type: Data Classes
namespace: WOS.Combat.Data
file-path: Assets/Scripts/Combat/Data/BallisticsData.cs
status: IMPLEMENTED
size: ~7 KB (260 lines)
feature-group: combat
---

# BallisticsData.cs

## Quick Reference
**Type**: Static Constants and Data Classes
**Namespace**: WOS.Combat.Data
**File**: `Assets/Scripts/Combat/Data/BallisticsData.cs`
**Size**: ~7 KB (260 lines)
**Dependencies**: UnityEngine, System

---

## Purpose
Ballistics calculation data and constants. Based on GDD Surface-Combat.md ballistics specifications.

This file contains:
- Physical constants for ballistics
- Shell ballistic profile
- Trajectory calculation data
- Hit result structure
- Environmental modifiers

---

## BallisticsConstants

Static physical constants for ballistics calculations.

```csharp
public static class BallisticsConstants
{
    // Physics
    const float Gravity = 9.81f;                     // m/s^2
    const float AirDensitySeaLevel = 1.225f;         // kg/m^3
    const float DragCoefficient = 0.3f;              // Typical shell Cd

    // Shell velocity decay
    const float VelocityRetentionPerKm = 0.92f;      // 8% loss per km

    // Penetration (simplified Krupp formula)
    const float PenetrationConstant = 0.0006f;       // K value

    // Dispersion
    const float BaseDispersionPerKm = 15f;           // Meters per km
    const float MaxDispersionMultiplier = 3f;        // Max at extreme range

    // Range limits
    const float MinEngagementRange = 500f;           // Meters
    const float MaxEngagementRange = 40000f;         // Meters (40km)
}
```

---

## BallisticProfile

Ballistic characteristics of a shell type.

```csharp
[Serializable]
public class BallisticProfile
{
    // Shell Properties
    public float caliber;           // mm
    public float shellWeight;       // kg
    public float muzzleVelocity;    // m/s
    public float dragCoefficient;

    // Armor Interaction
    public float penetrationAt1km;  // mm at 1km
    public float normalizeAngle;    // Degrees
    public float ricochetAngle;     // Degrees
    public float fuseArmingThreshold; // mm to arm fuse

    // Damage
    public float baseDamage;
    public float explosiveFiller;   // kg
    public float fireChance;        // 0-1
    public float floodChance;       // 0-1

    // Flight
    public float maxRange;          // Meters
    public float optimalRange;      // Best accuracy
}
```

### Methods
- `CalculatePenetration(range)` - Penetration at distance
- `CalculateFlightTime(range)` - Time to target
- `CalculateDispersion(range, crew)` - Spread at range

### Penetration Formula
```csharp
public float CalculatePenetration(float range)
{
    float rangeKm = range / 1000f;
    float velocityRetention = Mathf.Pow(
        BallisticsConstants.VelocityRetentionPerKm, rangeKm);
    float currentVelocity = muzzleVelocity * velocityRetention;

    // Penetration proportional to velocity squared
    float velocityFactor = currentVelocity / muzzleVelocity;
    return penetrationAt1km * velocityFactor * velocityFactor;
}
```

---

## TrajectoryData

Calculated trajectory for a shot.

```csharp
[Serializable]
public class TrajectoryData
{
    // Launch Parameters
    public Vector3 origin;
    public Vector3 direction;
    public float launchAngle;       // Elevation degrees
    public float azimuthAngle;      // Horizontal degrees
    public float muzzleVelocity;

    // Target
    public Vector3 targetPosition;
    public Vector3 impactPoint;

    // Flight
    public float totalFlightTime;
    public float maxAltitude;       // Peak of arc
    public float impactAngle;       // Descent angle
    public float impactVelocity;

    // Arc Points (visualization)
    public Vector3[] trajectoryPoints;
    public int pointCount;
}
```

### Methods
- `GetPositionAtTime(t)` - Interpolate position along arc

---

## HitResult

Hit result data from ballistics calculation.

```csharp
[Serializable]
public class HitResult
{
    // Hit Info
    public bool didHit;
    public Vector3 hitPoint;
    public Vector3 hitNormal;
    public float impactAngle;
    public float impactVelocity;

    // Target
    public uint targetNetId;
    public string hitCompartment;   // Ship section hit
    public bool isAboveWaterline;

    // Armor Interaction
    public float armorThickness;
    public float effectiveThickness;  // After angle calc
    public float shellPenetration;
    public bool didPenetrate;
    public bool didRicochet;
    public bool didOverpenetrate;     // Through without detonating

    // Damage
    public float damageDealt;
    public bool causedFire;
    public bool causedFlooding;
    public bool causedCritical;       // Magazine, engine, etc.
    public string criticalType;
}
```

---

## BallisticEnvironment

Environmental conditions affecting ballistics.

```csharp
[Serializable]
public class BallisticEnvironment
{
    // Weather
    [Range(0f, 1f)]
    public float visibility = 1f;
    [Range(0f, 50f)]
    public float windSpeed;           // m/s
    public Vector2 windDirection;

    // Sea State
    [Range(0f, 10f)]
    public float seaState;            // 0-10 scale
    public float waveHeight;

    // Calculated Modifiers
    public float accuracyModifier = 1f;
    public float rangeModifier = 1f;
    public float windDriftPerKm;
}
```

### Methods
- `CalculateModifiers()` - Update modifiers from conditions
- `ApplyWindDrift(pos, flightTime)` - Apply wind to position

### Accuracy Calculation
```csharp
public void CalculateModifiers()
{
    // Visibility affects accuracy
    accuracyModifier = Mathf.Lerp(0.5f, 1f, visibility);

    // High sea state reduces accuracy
    accuracyModifier *= Mathf.Lerp(1f, 0.6f, seaState / 10f);

    // Wind drift
    windDriftPerKm = windSpeed * 0.5f;
}
```

---

## Integration Points

### Used By
- [[BallisticsCalculator]] - Uses all structures
- [[TargetingSystem]] - Uses BallisticEnvironment
- [[ProjectileManager]] - Uses HitResult
- [[WeaponDefinitionSO]] - Creates BallisticProfile

---

## Physical Accuracy Notes

| Constant | Value | Real-World Basis |
|----------|-------|------------------|
| Gravity | 9.81 m/s^2 | Standard Earth |
| Velocity Loss | 8%/km | Simplified drag |
| Base Dispersion | 15m/km | Historical accuracy |
| Max Range | 40km | Battleship limits |

---

## Related Files
- [[BallisticsCalculator]] - Uses these structures
- [[WeaponData]] - Projectile data
- [[ProjectileManager]] - Hit processing
- [[CombatNetworkSerializers]] - Network sync

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added environmental modifiers
- **2025-01**: Added trajectory interpolation

