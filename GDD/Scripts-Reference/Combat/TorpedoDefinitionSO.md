---
tags: [script, combat, scriptableobject, torpedoes, implemented]
script-type: ScriptableObject
namespace: WOS.Combat.ScriptableObjects
file-path: Assets/Scripts/Combat/ScriptableObjects/TorpedoDefinitionSO.cs
status: IMPLEMENTED
size: ~8 KB (290 lines)
feature-group: combat
---

# TorpedoDefinitionSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.Combat.ScriptableObjects
**File**: `Assets/Scripts/Combat/ScriptableObjects/TorpedoDefinitionSO.cs`
**Size**: ~8 KB (290 lines)
**Dependencies**: EquipmentDefinitionSO
**Asset Menu**: `WOS/Combat/Torpedo Definition`

---

## Purpose
ScriptableObject definition for torpedo weapons. Torpedoes have unique mechanics separate from guns. Based on GDD Submarine-Warfare.md specifications.

---

## Configuration Fields

### Torpedo Classification
```
torpedoDiameterMM (int, 324-660): Diameter in mm (standard: 450, 533, 610)
torpedoLengthMeters (float, 2-12): Length in meters
torpedoWeightTons (float, 0.1-5): Weight in tons
```

### Performance
```
maxSpeedKnots (float, 10-80): Maximum speed in knots
maxRangeMiles (float, 0.5-30): Range at cruise speed (nautical miles)
rangeAtMaxSpeedMiles (float, 0.25-25): Range at max speed
cruiseSpeedKnots (float, 8-60): Extended range speed
runningDepthMeters (float, 1-30): Running depth
```

### Warhead
```
warheadWeightKg (float, 10-1000): Explosive weight kg
damageMJ (float, 50-10000): Base damage in megajoules
splashRadius (float, 5-30): Near-miss damage radius
floodChance (float, 0.5-1): Flooding chance (very high)
canCauseCatastrophicDamage (bool): Can break ship in half
```

### Guidance System
```
guidanceType (TorpedoGuidance): Guidance type
turnRate (float, 0-30): Turn rate degrees/second
homingRange (float, 0-2000): Acoustic homing range
searchWidth (float, 0-500): Pattern search width
```

### Launch Requirements
```
reloadTime (float, 30-180): Reload time seconds
minLaunchDepth (float, 0-50): Min depth for submarines
maxLaunchDepth (float, 0-300): Max depth for submarines
armingDistance (float, 50-500): Distance to arm
```

### Detection
```
wakeVisibility (float, 0-1): Visual wake factor
acousticSignature (float, 0-1): Sonar detectability
```

### Economy
```
costPerTorpedo (int, 100-50000): Cost each
reloadsPerTube (int, 1-5): Reloads per tube
```

### Torpedo Geometry
```
torpedoCenter (Vector3): Pivot point
exitPoints (Vector3[]): Effect spawn points
visualScale (float, 0.1-5): Sprite scale
```

---

## Guidance Types

### TorpedoGuidance Enum
```csharp
public enum TorpedoGuidance
{
    Straight,           // Runs in straight line
    PatternRunning,     // Zigzag search pattern
    AcousticHoming,     // Homes on engine noise
    WireGuided,         // Player/AI controlled
    WakeHoming          // Follows ship wake (advanced)
}
```

### Guidance Defaults (OnValidate)
```csharp
switch (guidanceType)
{
    case TorpedoGuidance.Straight:
        turnRate = 0f;
        homingRange = 0f;
        searchWidth = 0f;
        break;

    case TorpedoGuidance.PatternRunning:
        searchWidth = 200f min;
        turnRate = 10f min;
        break;

    case TorpedoGuidance.AcousticHoming:
        homingRange = 1000f min;
        turnRate = 20f min;
        break;

    case TorpedoGuidance.WireGuided:
        turnRate = 25f min;
        break;
}
```

---

## Methods

### Speed Conversions
```csharp
public float GetMaxSpeedMS()
{
    return maxSpeedKnots * 0.514444f;  // knots to m/s
}

public float GetCruiseSpeedMS()
{
    return cruiseSpeedKnots * 0.514444f;
}
```

### Range Conversions
```csharp
public float GetMaxRangeMeters()
{
    return maxRangeMiles * 1852f;  // nautical miles to meters
}

public float GetRangeAtMaxSpeedMeters()
{
    return rangeAtMaxSpeedMiles * 1852f;
}
```

### Time to Target
```csharp
public float GetTimeToTarget(float range)
{
    return range / GetMaxSpeedMS();
}
```

### Depth Check
```csharp
public bool CanLaunchAtDepth(float depth)
{
    return depth >= minLaunchDepth && depth <= maxLaunchDepth;
}
```

### Angle-Based Damage
```csharp
public float GetEffectiveDamageMJ(float hitAngle)
{
    // Perpendicular hits (90 degrees) do most damage
    float angleModifier = Mathf.Abs(Mathf.Sin(hitAngle * Mathf.Deg2Rad));
    return damageMJ * Mathf.Lerp(0.5f, 1f, angleModifier);
}
```

---

## Standard Torpedo Sizes

| Diameter | Usage | Typical Ships |
|----------|-------|---------------|
| 450mm | Light torpedoes | PT boats, small craft |
| 533mm | Standard | Destroyers, Submarines |
| 610mm | Heavy | Japanese Long Lance |

---

## Example Assets

### Mark 15 (US Destroyer Torpedo)
```
torpedoDiameterMM: 533
maxSpeedKnots: 45
maxRangeMiles: 6
warheadWeightKg: 375
damageMJ: 1200
guidanceType: Straight
reloadTime: 60
costPerTorpedo: 5000
```

### Type 93 Long Lance
```
torpedoDiameterMM: 610
maxSpeedKnots: 52
maxRangeMiles: 22
warheadWeightKg: 490
damageMJ: 2400
guidanceType: Straight
wakeVisibility: 0.3 (very low wake)
costPerTorpedo: 15000
```

### Mark 48 (Modern Homing)
```
torpedoDiameterMM: 533
maxSpeedKnots: 55
maxRangeMiles: 5
guidanceType: AcousticHoming
homingRange: 1500
turnRate: 25
```

---

## Integration Points

### Inherits From
- [[EquipmentDefinitionSO]] - Base equipment class

### Used By
- [[TorpedoController]] - Torpedo launching
- [[ProjectileManager]] - Torpedo physics
- [[TorpedoVisual]] - Visual configuration

---

## Related Files
- [[TorpedoController]] - Runtime torpedo system
- [[TorpedoVisual]] - Client-side rendering
- [[ProjectileManager]] - Torpedo spawning

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added guidance types
- **2025-01**: Added torpedo geometry fields

