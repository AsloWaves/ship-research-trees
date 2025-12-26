---
tags: [script, combat, scriptableobject, weapons, implemented]
script-type: ScriptableObject
namespace: WOS.Combat.ScriptableObjects
file-path: Assets/Scripts/Combat/ScriptableObjects/WeaponDefinitionSO.cs
status: IMPLEMENTED
size: ~7 KB (233 lines)
feature-group: combat
---

# WeaponDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Combat.ScriptableObjects
**File**: `Assets/Scripts/Combat/ScriptableObjects/WeaponDefinitionSO.cs`
**Size**: ~7 KB (233 lines)
**Dependencies**: EquipmentDefinitionSO, BallisticsData
**Asset Menu**: `WOS/Combat/Weapon Definition`

---

## Purpose
ScriptableObject definition for weapon systems. Inherits from EquipmentDefinitionSO for inventory/loadout integration. Based on GDD Surface-Combat.md specifications.

Defines:
- Weapon classification and caliber
- Ballistic properties
- Combat performance stats
- Ammunition capacity
- Crew requirements
- Visual/audio effects

---

## Configuration Fields

### Weapon Classification
```
weaponCategory (WeaponCategory): Main Gun, Secondary, Torpedo, etc.
caliber (GunCaliber): Small, Medium, Large, SuperHeavy
caliberMM (float, 20-510): Caliber in millimeters
barrelCount (int, 1-4): Barrels per mount
```

### Ballistic Properties
```
muzzleVelocity (float, 200-1000): Shell velocity m/s
maxRange (float, 5000-45000): Maximum range meters
optimalRange (float, 2000-30000): Best accuracy range
penetration (float, 10-800): Penetration at 1km in mm
shellWeight (float, 1-2000): Shell weight kg
explosiveFiller (float, 0-100): Explosive kg
```

### Combat Performance
```
baseDamage (float, 100-10000): Damage per shell
reloadTime (float, 2-60): Reload time seconds
rotationSpeed (float, 1-60): Turret rotation deg/s
maxElevation (float, 15-90): Max gun elevation
minElevation (float, -10-0): Min gun elevation
firingArc (float, 30-180): Arc per side in degrees
```

### Ammunition
```
defaultAmmoCapacity (int, 10-500): Default ammo per mount
compatibleAmmo (AmmunitionType[]): Allowed ammo types
fireChance (float, 0-1): Fire chance on penetrating hit
floodChance (float, 0-1): Flood chance below waterline
```

### Crew Requirements
```
crewRequired (int, 1-100): Crew for full efficiency
crewMinimum (int, 1-50): Minimum to operate
```

### Visual/Audio
```
muzzleFlashPrefab (GameObject): Muzzle flash effect
shellTracerPrefab (GameObject): Shell tracer effect
firingSound (string): FMOD event path
reloadSound (string): FMOD reload event
```

---

## Methods

### CreateBallisticProfile
Creates a BallisticProfile from weapon definition for physics calculations.

```csharp
public BallisticProfile CreateBallisticProfile()
{
    return new BallisticProfile
    {
        caliber = caliberMM,
        shellWeight = shellWeight,
        muzzleVelocity = muzzleVelocity,
        dragCoefficient = BallisticsConstants.DragCoefficient,
        penetrationAt1km = penetration,
        normalizeAngle = 30f,
        ricochetAngle = 70f,
        fuseArmingThreshold = Mathf.Max(caliberMM * 0.1f, 10f),
        baseDamage = baseDamage,
        explosiveFiller = explosiveFiller,
        fireChance = fireChance,
        floodChance = floodChance,
        maxRange = maxRange,
        optimalRange = optimalRange
    };
}
```

### CalculateDPS
Returns damage per second.
```csharp
public float CalculateDPS()
{
    float shotsPerSecond = barrelCount / reloadTime;
    return baseDamage * shotsPerSecond;
}
```

### EstimateHitProbability
Estimates hit probability at given range.
```csharp
public float EstimateHitProbability(float range, float crewAccuracy = 1f)
{
    if (range > maxRange) return 0f;
    float rangeRatio = range / optimalRange;
    float baseAccuracy = rangeRatio <= 1f ? 0.8f : 0.8f / rangeRatio;
    return Mathf.Clamp01(baseAccuracy * crewAccuracy);
}
```

---

## OnValidate Auto-Calculations

Editor-time validation auto-calculates:
- Ensures optimalRange < maxRange (sets to 70%)
- Auto-calculates shellWeight from caliber if not set
- Auto-calculates penetration from caliber if not set
- Sets GunCaliber enum from caliberMM

```csharp
if (caliberMM < 100) caliber = GunCaliber.Small;
else if (caliberMM < 200) caliber = GunCaliber.Medium;
else if (caliberMM < 350) caliber = GunCaliber.Large;
else caliber = GunCaliber.SuperHeavy;
```

---

## Caliber Classifications

| Caliber | Range (mm) | Typical Ships |
|---------|------------|---------------|
| Small | < 100 | AA guns, PT boats |
| Medium | 100-200 | Destroyers, Cruisers |
| Large | 200-350 | Heavy Cruisers, Battlecruisers |
| SuperHeavy | > 350 | Battleships (406mm, 460mm) |

---

## Example Assets

### 127mm/38 (US Destroyer Gun)
```
caliberMM: 127
barrelCount: 2
muzzleVelocity: 792
maxRange: 15700
reloadTime: 4
baseDamage: 800
```

### 406mm/45 (US Battleship)
```
caliberMM: 406
barrelCount: 3
muzzleVelocity: 820
maxRange: 36000
reloadTime: 30
baseDamage: 8000
```

---

## Integration Points

### Inherits From
- [[EquipmentDefinitionSO]] - Base equipment class

### Used By
- [[WeaponController]] - Weapon configuration
- [[BallisticsCalculator]] - Ballistic profiles
- [[TurretRotator]] - Rotation speed

---

## Related Files
- [[AmmunitionDefinitionSO]] - Ammo types
- [[BallisticsData]] - BallisticProfile structure
- [[WeaponController]] - Runtime weapon system

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added crew requirements
- **2025-01**: Added auto-calculation in OnValidate

