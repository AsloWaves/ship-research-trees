---
tags: [script, port, ocean, visual, lighting, implemented]
script-type: MonoBehaviour
namespace: WOS.Port.Ocean
file-path: Assets/Scripts/Port/Ocean/PortBuoyLight.cs
status: IMPLEMENTED
size: ~392 lines
feature-group: port
---

# PortBuoyLight.cs

## Quick Reference
**Type**: MonoBehaviour (Light Controller)
**Namespace**: WOS.Port.Ocean
**File**: `Assets/Scripts/Port/Ocean/PortBuoyLight.cs`
**Size**: ~392 lines
**Dependencies**: Light2D (URP), PortEnums

---

## Purpose
Dynamic 2D light buoy marker for port zones. Uses URP 2D Point Light with gradient falloff and optional animations. Supports nationality-based color schemes.

---

## Enums

```csharp
public enum ZoneType { AoP, AoI, Exit }

public enum AnimationType
{
    None,       // Static light
    Pulse,      // Intensity pulse (lighthouse)
    ColorCycle, // Cycle through colors
    CandyCane   // Blend between two colors
}
```

---

## Nationality Colors

| Nationality | Primary | Secondary |
|-------------|---------|-----------|
| UnitedStates | Blue | Light Blue |
| UnitedKingdom | Gold | Light Gold |
| Japan | Red | Light Red |
| Germany | Grey | Light Grey |
| Neutral | White | Cyan |

---

## Initialization

```csharp
public void Initialize(Nationality nation, ZoneType zone, AnimationType anim)
{
    nationality = nation;
    zoneType = zone;
    animationType = anim;
    ApplyNationalityColors();
    ConfigureLight();
}
```

---

## Animation Methods

```csharp
private void UpdatePulseAnimation()
{
    float pulse = (Mathf.Sin(animationTime * Mathf.PI * 2f) + 1f) * 0.5f;
    buoyLight.intensity = Mathf.Lerp(pulseMinIntensity, 1f, pulse) * baseIntensity;
}

private void UpdateCandyCaneAnimation()
{
    float t = Mathf.PingPong(animationTime, 1f);
    buoyLight.color = Color.Lerp(primaryColor, secondaryColor, t);
}
```

---

## Integration Points

### Used By
- [[PortZoneManager]] - Creates and controls buoys

