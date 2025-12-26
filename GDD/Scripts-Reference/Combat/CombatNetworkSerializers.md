---
tags: [script, combat, networking, serialization, implemented]
script-type: Static Class
namespace: WOS.Combat.Data
file-path: Assets/Scripts/Combat/Data/CombatNetworkSerializers.cs
status: IMPLEMENTED
size: ~11 KB (392 lines)
feature-group: combat
---

# CombatNetworkSerializers.cs

## Quick Reference
**Type**: Static Class (Extension Methods)
**Namespace**: WOS.Combat.Data
**File**: `Assets/Scripts/Combat/Data/CombatNetworkSerializers.cs`
**Size**: ~11 KB (392 lines)
**Dependencies**: Mirror

---

## Purpose
Custom Mirror serializers for combat data types. Mirror cannot auto-generate serializers for complex types with Dictionaries or nested Lists. These extension methods provide explicit read/write implementations.

---

## Why Custom Serializers?

Mirror's Weaver (code generator) handles simple types automatically:
- Primitives (int, float, bool, string)
- Unity types (Vector3, Quaternion)
- Simple structs

But fails for:
- Dictionary<K,V>
- Nested List<List<T>>
- Complex class hierarchies
- Types with [NonSerialized] fields mixed in

This file provides manual serializers for combat data structures.

---

## Serialized Types

### AmmoCountEntry
```csharp
public static void WriteAmmoCountEntry(
    this NetworkWriter writer, AmmoCountEntry entry)
{
    writer.WriteInt((int)entry.ammoType);
    writer.WriteInt(entry.count);
}

public static AmmoCountEntry ReadAmmoCountEntry(
    this NetworkReader reader)
{
    var ammoType = (AmmunitionType)reader.ReadInt();
    var count = reader.ReadInt();
    return new AmmoCountEntry(ammoType, count);
}
```

---

### WeaponMountState
Full weapon mount state with null checking.

**Serialized Fields**:
- mountId (string)
- mountIndex (int)
- state (WeaponState enum)
- reloadProgress (float)
- currentRotation (float)
- targetRotation (float)
- currentElevation (float)
- targetElevation (float)
- loadedAmmoType (AmmunitionType enum)
- currentAmmo (int)
- maxAmmo (int)
- healthPercent (float)
- isJammed (bool)
- isFlooded (bool)
- crewEfficiency (float)
- assignedCrew (int)
- requiredCrew (int)

---

### AmmunitionStorage
Magazine storage with ammo lists.

**Serialized Fields**:
- storageId (string)
- isMagazine (bool)
- ammoCountList (List<AmmoCountEntry>)
- maxAmmoList (List<AmmoCountEntry>)
- healthPercent (float)
- isFlooded (bool)
- isOnFire (bool)

**Note**: Calls `RebuildCaches()` after deserialization to restore local Dictionary caches.

---

### ShipWeaponLoadout
Complete ship weapon configuration.

**Serialized Fields**:
- mainGuns (List<WeaponMountState>)
- secondaryGuns (List<WeaponMountState>)
- torpedoTubes (List<WeaponMountState>)
- antiAirGuns (List<WeaponMountState>)
- magazines (List<AmmunitionStorage>)
- fireControlEfficiency (float)
- radarBonus (float)
- hasFireControlDamage (bool)

---

### FiringSolution
Targeting solution data.

**Serialized Fields**:
- targetNetId (uint)
- targetPosition (Vector3)
- targetVelocity (Vector3)
- predictedPosition (Vector3)
- range (float)
- flightTime (float)
- leadAngle (float)
- elevationAngle (float)
- azimuthAngle (float)
- accuracy (float)
- dispersionRadius (float)
- calculationTime (float)
- isValid (bool)
- isInRange (bool)
- hasLineOfSight (bool)

---

### ProjectileData
In-flight projectile data.

**Serialized Fields**:
- projectileId (uint)
- sourceShipNetId (uint)
- sourceMountIndex (int)
- ammoType (AmmunitionType enum)
- caliber (GunCaliber enum)
- shellWeight (float)
- explosiveWeight (float)
- position (Vector3)
- velocity (Vector3)
- muzzleVelocity (float)
- currentVelocity (float)
- penetration (float)
- damage (float)
- splashRadius (float)
- timeAlive (float)
- maxLifetime (float)
- hasDetonated (bool)

---

## Usage Pattern

### Automatic Registration
Mirror automatically discovers extension methods on NetworkWriter/NetworkReader. Just having this file in the project enables serialization.

### Null Handling
All serializers write a bool first indicating if value is null:
```csharp
public static void WriteWeaponMountState(
    this NetworkWriter writer, WeaponMountState state)
{
    if (state == null)
    {
        writer.WriteBool(false);
        return;
    }
    writer.WriteBool(true);
    // ... write fields
}

public static WeaponMountState ReadWeaponMountState(
    this NetworkReader reader)
{
    bool hasValue = reader.ReadBool();
    if (!hasValue) return null;
    // ... read fields
}
```

### List Serialization Helper
```csharp
private static void WriteWeaponMountList(
    NetworkWriter writer, List<WeaponMountState> mounts)
{
    int count = mounts?.Count ?? 0;
    writer.WriteInt(count);
    if (mounts != null)
    {
        foreach (var mount in mounts)
        {
            writer.WriteWeaponMountState(mount);
        }
    }
}
```

---

## Integration Points

### Used By
- **Mirror SyncVars** - Automatic serialization
- **Command/ClientRpc parameters** - Method arguments
- **NetworkMessages** - Custom messages

### Serializes For
- [[WeaponData]] - All combat data structures
- [[BallisticsData]] - FiringSolution
- [[WeaponController]] - SyncVar weaponLoadout
- [[TargetingSystem]] - Firing solutions

---

## Performance Considerations

| Type | Approx Bytes | Notes |
|------|-------------|-------|
| AmmoCountEntry | 8 | Enum + int |
| WeaponMountState | ~70 | Full state |
| AmmunitionStorage | Variable | Depends on ammo types |
| ShipWeaponLoadout | Variable | Depends on mount count |
| FiringSolution | ~80 | Full solution |
| ProjectileData | ~90 | Full projectile |

---

## Related Files
- [[WeaponData]] - Data structures
- [[BallisticsData]] - Ballistics structures
- [[WeaponController]] - Uses serialized SyncVars

---

## Testing Notes
- All serializers null-safe
- Lists rebuilt on deserialization
- Caches rebuilt after network sync
- Enums serialized as int for version safety

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added AmmunitionStorage serializer
- **2025-01**: Added cache rebuild on deserialization

