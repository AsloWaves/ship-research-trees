---
tags: [script, combat, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Combat.Data
file-path: Assets/Scripts/Combat/Data/WeaponData.cs
status: IMPLEMENTED
size: ~11 KB (397 lines)
feature-group: combat
---

# WeaponData.cs

## Quick Reference
**Type**: Data Classes and Enums
**Namespace**: WOS.Combat.Data
**File**: `Assets/Scripts/Combat/Data/WeaponData.cs`
**Size**: ~11 KB (397 lines)
**Dependencies**: UnityEngine, System

---

## Purpose
Weapon system data structures for naval combat. Based on GDD Surface-Combat.md specifications.

This file contains:
- Weapon category and state enums
- Ammunition type definitions
- Weapon mount runtime state
- Ammunition storage system
- Firing solution data
- Projectile in-flight data
- Ship weapon loadout summary

---

## Enums

### WeaponCategory
```csharp
public enum WeaponCategory
{
    MainGun,        // Primary ship armament
    SecondaryGun,   // Secondary/AA armament
    Torpedo,        // Torpedo tubes
    DepthCharge,    // Anti-submarine weapons
    AntiAir,        // Dedicated AA systems
    Missile         // Future: Guided missiles
}
```

### GunCaliber
```csharp
public enum GunCaliber
{
    Small,      // < 100mm
    Medium,     // 100-200mm
    Large,      // 200-350mm
    SuperHeavy  // > 350mm (battleship main guns)
}
```

### AmmunitionType
```csharp
public enum AmmunitionType
{
    AP,     // Armor Piercing - high penetration, low splash
    HE,     // High Explosive - area damage, low penetration
    SAP,    // Semi-Armor Piercing - balanced
    AA,     // Anti-Aircraft - for AA guns
    Flare,  // Illumination rounds
    Smoke   // Smoke screen rounds
}
```

### WeaponState
```csharp
public enum WeaponState
{
    Ready,          // Can fire
    Reloading,      // Between shots
    Disabled,       // Damaged, cannot fire
    Destroyed,      // Permanently destroyed
    OutOfAmmo,      // No ammunition
    Overheated      // Thermal limit reached
}
```

---

## Data Classes

### AmmoCountEntry
Network-serializable ammo count for Mirror compatibility.

```csharp
[Serializable]
public struct AmmoCountEntry
{
    public AmmunitionType ammoType;
    public int count;
}
```

---

### WeaponMountState
Runtime state of a single weapon mount.

```csharp
[Serializable]
public class WeaponMountState
{
    // Identification
    public string mountId;
    public int mountIndex;

    // State
    public WeaponState state = WeaponState.Ready;
    public float reloadProgress;      // 0-1
    public float currentRotation;     // Degrees
    public float targetRotation;
    public float currentElevation;
    public float targetElevation;

    // Ammunition
    public AmmunitionType loadedAmmoType = AmmunitionType.AP;
    public int currentAmmo;
    public int maxAmmo;

    // Damage
    public float healthPercent = 1f;  // 0-1
    public bool isJammed;
    public bool isFlooded;

    // Crew
    public float crewEfficiency = 1f;
    public int assignedCrew;
    public int requiredCrew;
}
```

**Methods**:
- `CanFire()` - Check if weapon can fire
- `GetReloadModifier()` - Get reload speed based on crew

---

### AmmunitionStorage
Magazine/ammo storage data with Mirror serialization support.

```csharp
[Serializable]
public class AmmunitionStorage
{
    public string storageId;
    public bool isMagazine;         // Can explode when hit

    // Network-serializable lists (instead of Dictionary)
    public List<AmmoCountEntry> ammoCountList;
    public List<AmmoCountEntry> maxAmmoList;

    // State
    public float healthPercent = 1f;
    public bool isFlooded;          // Safe but unusable
    public bool isOnFire;           // Risk of explosion
}
```

**Methods**:
- `GetAmmo(type)` - Get available ammo count
- `GetMaxAmmo(type)` - Get max capacity
- `ConsumeAmmo(type, amount)` - Use ammo
- `SetAmmoCount(dict)` - Set from dictionary (server)
- `RebuildCaches()` - Rebuild after network sync

---

### FiringSolution
Calculated firing solution for targeting.

```csharp
[Serializable]
public class FiringSolution
{
    // Target
    public uint targetNetId;
    public Vector3 targetPosition;
    public Vector3 targetVelocity;
    public Vector3 predictedPosition;

    // Ballistics
    public float range;
    public float flightTime;
    public float leadAngle;
    public float elevationAngle;
    public float azimuthAngle;

    // Accuracy
    public float accuracy;           // 0-1
    public float dispersionRadius;   // Meters at range

    // Validity
    public float calculationTime;
    public bool isValid;
    public bool isInRange;
    public bool hasLineOfSight;
}
```

**Methods**:
- `IsStillValid(time, maxAge)` - Check if solution is current

---

### ProjectileData
Projectile in-flight data.

```csharp
[Serializable]
public class ProjectileData
{
    // Identification
    public uint projectileId;
    public uint sourceShipNetId;
    public int sourceMountIndex;

    // Projectile Type
    public AmmunitionType ammoType;
    public GunCaliber caliber;
    public float shellWeight;        // kg
    public float explosiveWeight;    // kg of filler

    // Ballistics
    public Vector3 position;
    public Vector3 velocity;
    public float muzzleVelocity;
    public float currentVelocity;

    // Damage
    public float penetration;        // mm of armor
    public float damage;
    public float splashRadius;       // For HE shells

    // State
    public float timeAlive;
    public float maxLifetime;
    public bool hasDetonated;
}
```

---

### ShipWeaponLoadout
Summary of all weapons on a ship.

```csharp
[Serializable]
public class ShipWeaponLoadout
{
    // Weapon Mounts
    public List<WeaponMountState> mainGuns;
    public List<WeaponMountState> secondaryGuns;
    public List<WeaponMountState> torpedoTubes;
    public List<WeaponMountState> antiAirGuns;

    // Ammunition
    public List<AmmunitionStorage> magazines;

    // Fire Control
    public float fireControlEfficiency = 1f;
    public float radarBonus;
    public bool hasFireControlDamage;
}
```

**Methods**:
- `GetMounts(category)` - Get mounts by category
- `CountReadyWeapons(category)` - Count ready weapons

---

## Integration Points

### Used By
- [[WeaponController]] - Uses all data structures
- [[TargetingSystem]] - Uses FiringSolution
- [[ProjectileManager]] - Uses ProjectileData
- [[CombatNetworkSerializers]] - Serializes for network

---

## Network Serialization Note
Mirror cannot auto-serialize Dictionary types. This file uses `List<AmmoCountEntry>` instead of `Dictionary<AmmunitionType, int>` with local caching for fast lookup.

---

## Related Files
- [[CombatNetworkSerializers]] - Custom serializers
- [[BallisticsData]] - Ballistics structures
- [[WeaponController]] - Uses these structures
- [[WeaponDefinitionSO]] - Static configuration

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added crew efficiency system
- **2025-01**: Added AmmoCountEntry for Mirror serialization

