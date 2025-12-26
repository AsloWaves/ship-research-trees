---
tags: [script, combat, scriptableobject, ammunition, implemented]
script-type: ScriptableObject
namespace: WOS.Combat.ScriptableObjects
file-path: Assets/Scripts/Combat/ScriptableObjects/AmmunitionDefinitionSO.cs
status: IMPLEMENTED
size: ~6 KB (217 lines)
feature-group: combat
---

# AmmunitionDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Combat.ScriptableObjects
**File**: `Assets/Scripts/Combat/ScriptableObjects/AmmunitionDefinitionSO.cs`
**Size**: ~6 KB (217 lines)
**Dependencies**: EquipmentDefinitionSO, WeaponData
**Asset Menu**: `WOS/Combat/Ammunition Definition`

---

## Purpose
ScriptableObject definition for ammunition types. Each ammo type has different characteristics for penetration, damage, and effects. Based on GDD Surface-Combat.md specifications.

---

## Configuration Fields

### Ammunition Type
```
ammoType (AmmunitionType): AP, HE, SAP, AA, Flare, Smoke
caliberMM (float, 5-610): Designed caliber in mm
```

### Ballistic Modifiers
```
velocityModifier (float, 0.8-1.2): Velocity multiplier
penetrationModifier (float, 0.5-2.0): Penetration multiplier
damageModifier (float, 0.5-2.0): Damage multiplier
dragModifier (float, 0.8-1.5): Range effect
```

### Damage Effects
```
splashRadius (float, 0-50): Area damage radius (0 for AP)
fireChance (float, 0-1): Fire chance on hit
floodChance (float, 0-1): Flooding chance
moduleDamageModifier (float, 0.5-2.0): Module damage bonus
crewDamageModifier (float, 0.5-2.0): Crew damage bonus
```

### Armor Interaction
```
fuseArmThreshold (float, 0-100): Min armor to arm fuse (mm)
ricochetAngle (float, 45-85): Ricochet threshold degrees
normalizeAngle (float, 0-45): Shell normalization degrees
canOverpenetrate (bool): Can pass through without detonating
```

### Economy
```
costPerShell (int, 1-10000): Shell cost
resupplyPriority (int, 1-10): Restock order
```

### Visual
```
tracerColor (Color): Tracer color
explosionPrefab (GameObject): Detonation effect
trailPrefab (GameObject): Shell trail effect
```

---

## Ammunition Type Characteristics

### AP (Armor Piercing)
```
penetrationModifier: 1.2+ (highest)
splashRadius: 0 (no splash)
fireChance: 0.15 max
canOverpenetrate: true
```
Best against: Battleships, Heavy Cruisers

### HE (High Explosive)
```
penetrationModifier: 0.6 max
splashRadius: caliberMM * 0.1
fireChance: 0.2+ (high fire chance)
canOverpenetrate: false
```
Best against: Destroyers, Superstructure

### SAP (Semi-Armor Piercing)
```
penetrationModifier: 0.8-1.2 (balanced)
splashRadius: caliberMM * 0.05
canOverpenetrate: false
```
Best against: Light Cruisers, balanced targets

### AA (Anti-Aircraft)
```
penetrationModifier: 0.3 (low)
splashRadius: caliberMM * 0.2 (large)
crewDamageModifier: 1.5 (high crew damage)
canOverpenetrate: false
```
Best against: Aircraft

---

## Methods

### GetEffectivePenetration
```csharp
public float GetEffectivePenetration(float basePenetration)
{
    return basePenetration * penetrationModifier;
}
```

### GetEffectiveDamage
```csharp
public float GetEffectiveDamage(float baseDamage)
{
    return baseDamage * damageModifier;
}
```

### GetEffectivenessAgainst
Returns effectiveness multiplier against target type.
```csharp
public float GetEffectivenessAgainst(string targetType)
{
    return (ammoType, targetType) switch
    {
        (AmmunitionType.AP, "Battleship") => 1.2f,
        (AmmunitionType.AP, "Cruiser") => 1.0f,
        (AmmunitionType.AP, "Destroyer") => 0.7f,    // Overpenetration
        (AmmunitionType.HE, "Destroyer") => 1.3f,
        (AmmunitionType.HE, "Battleship") => 0.6f,
        (AmmunitionType.AA, "Aircraft") => 1.5f,
        _ => 1.0f
    };
}
```

---

## OnValidate Defaults

Auto-sets appropriate values based on ammo type:

```csharp
switch (ammoType)
{
    case AmmunitionType.AP:
        penetrationModifier = 1.2f;
        splashRadius = 0f;
        canOverpenetrate = true;
        break;

    case AmmunitionType.HE:
        penetrationModifier = 0.6f;
        splashRadius = caliberMM * 0.1f;
        fireChance = 0.2f;
        canOverpenetrate = false;
        break;

    case AmmunitionType.SAP:
        penetrationModifier = 0.9f;
        splashRadius = caliberMM * 0.05f;
        canOverpenetrate = false;
        break;

    case AmmunitionType.AA:
        penetrationModifier = 0.3f;
        splashRadius = caliberMM * 0.2f;
        crewDamageModifier = 1.5f;
        break;
}
```

---

## Example Assets

### 127mm AP Shell
```
ammoType: AP
caliberMM: 127
penetrationModifier: 1.2
damageModifier: 1.0
fireChance: 0.1
tracerColor: Yellow
costPerShell: 50
```

### 406mm HE Shell
```
ammoType: HE
caliberMM: 406
penetrationModifier: 0.5
damageModifier: 1.2
splashRadius: 40
fireChance: 0.35
costPerShell: 500
```

---

## Integration Points

### Inherits From
- [[EquipmentDefinitionSO]] - Base equipment class

### Used By
- [[WeaponController]] - Ammo selection
- [[ProjectileManager]] - Damage calculation
- [[ProjectileVisual]] - Tracer colors

---

## Related Files
- [[WeaponDefinitionSO]] - Weapon configuration
- [[WeaponData]] - AmmunitionType enum
- [[BallisticsCalculator]] - Damage calculation

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added effectiveness matrix
- **2025-01**: Added OnValidate auto-defaults

