---
tags: [script, port, scriptableobject, visual, implemented]
script-type: ScriptableObject
namespace: WOS.ScriptableObjects
file-path: Assets/Scripts/ScriptableObjects/Port/PortVisualStyleSO.cs
status: IMPLEMENTED
size: ~167 lines
feature-group: port
---

# PortVisualStyleSO.cs

## Quick Reference
**Type**: ScriptableObject
**Namespace**: WOS.ScriptableObjects
**File**: `Assets/Scripts/ScriptableObjects/Port/PortVisualStyleSO.cs`
**Size**: ~167 lines
**Create**: `Create > WOS > Port > Visual Style`

---

## Purpose
Visual style configuration for ports based on nationality. Allows creating nationality-themed ports without separate scenes. Contains sprites, colors, and prefabs for that nation's style.

---

## Configuration

```csharp
[Header("Identity")]
public Nationality nationality;
public string styleName;

[Header("Water Appearance")]
public Color waterTint;
public Sprite waterSprite;
public Color aopWaterTint;
public Color aoiWaterTint;

[Header("Dock Visuals")]
public Sprite[] dockSprites;
public Sprite dockHighlightSprite;
public Sprite dockOccupiedSprite;

[Header("Buoy Visuals")]
public Sprite aopBuoySprite;
public Sprite exitBuoySprite;
public Color buoyTint;

[Header("Environment - Industrial")]
public Sprite[] industrialBuildingSprites;
public Sprite[] craneSprites;
public Sprite[] groundSprites;

[Header("Environment - Decorative")]
public Sprite[] decorationSprites;
public Sprite flagSprite;
public Sprite[] lightingSprites;

[Header("Atmosphere")]
public Color fogColor;
public float fogDensity;
public Color ambientTint;

[Header("Audio")]
public string ambientSoundBank;
public string musicBank;
```

---

## Utility Methods

```csharp
public Sprite GetRandomDockSprite();
public Sprite GetRandomBuildingSprite();
public Sprite GetRandomDecorationSprite();
public Sprite GetRandomCraneSprite();
public Color GetWaterColor();
public bool ValidateStyle();
```

---

## Usage

1. Create one PortVisualStyleSO per nationality
2. Assign sprites, colors, and prefabs
3. Reference from PortDefinitionSO
4. HarborSceneManager loads and spawns visuals at runtime

---

## Integration Points

### Used By
- [[PortDefinitionSO]], [[HarborSceneManager]], [[PortZoneManager]]

