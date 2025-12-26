# SimpleWakeSprite.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/SimpleWakeSprite.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~106 |
| **Architecture** | Simple sprite-based wake component |

## Purpose
Simple sprite-based wake particle for 2D naval game. Provides default wake sprite settings and helper methods for CustomWakeParticle integration. Acts as a visual component wrapper for wake effects.

---

## Configuration

### Default Wake Sprite Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `defaultWakeSprite` | null | Default sprite (overridden by particle settings) |
| `defaultColor` | (1, 1, 1, 0.8) | Default particle color with alpha |
| `defaultScale` | 1 | Default particle scale |

---

## Component Requirements

```csharp
[RequireComponent(typeof(SpriteRenderer))]
public class SimpleWakeSprite : MonoBehaviour
```

---

## Initialization

```csharp
private void Awake()
{
    // Get or add SpriteRenderer
    spriteRenderer = GetComponent<SpriteRenderer>();
    if (spriteRenderer == null)
    {
        spriteRenderer = gameObject.AddComponent<SpriteRenderer>();
    }

    // Apply default settings
    ApplyDefaultSettings();
}

private void ApplyDefaultSettings()
{
    if (spriteRenderer == null) return;

    // Set default sprite if none assigned
    if (spriteRenderer.sprite == null && defaultWakeSprite != null)
    {
        spriteRenderer.sprite = defaultWakeSprite;
    }

    // Set default color
    spriteRenderer.color = defaultColor;

    // Set default scale
    transform.localScale = Vector3.one * defaultScale;

    // Configure sprite settings for wake particles
    spriteRenderer.sortingLayerName = "Default";
    spriteRenderer.sortingOrder = 0;

    // For 2D wake effects, we want additive or alpha blending
    // Note: This requires a material with appropriate blend mode
}
```

---

## Public API

### Update Sprite
```csharp
/// Update sprite properties (called by CustomWakeParticle)
public void UpdateSprite(Sprite sprite, Color color, float scale)
{
    if (spriteRenderer == null) return;

    if (sprite != null)
        spriteRenderer.sprite = sprite;

    spriteRenderer.color = color;
    transform.localScale = Vector3.one * scale;
}
```

### Visibility Control
```csharp
/// Set sprite visibility
public void SetVisible(bool visible)
{
    if (spriteRenderer != null)
        spriteRenderer.enabled = visible;
}
```

### Bounds Query
```csharp
/// Get sprite bounds for collision/culling calculations
public Bounds GetSpriteBounds()
{
    return spriteRenderer != null ? spriteRenderer.bounds : new Bounds();
}
```

---

## Editor Integration

```csharp
#if UNITY_EDITOR
private void OnValidate()
{
    // Apply settings in editor when values change
    if (Application.isPlaying) return;

    if (spriteRenderer == null)
        spriteRenderer = GetComponent<SpriteRenderer>();

    ApplyDefaultSettings();
}
#endif
```

---

## Usage Example

```csharp
// Create wake particle prefab with SimpleWakeSprite
GameObject wakeParticle = new GameObject("WakeParticle");
SimpleWakeSprite wakeSprite = wakeParticle.AddComponent<SimpleWakeSprite>();
wakeSprite.defaultWakeSprite = wakeSpriteSO;
wakeSprite.defaultColor = new Color(1f, 1f, 1f, 0.6f);
wakeSprite.defaultScale = 2f;

// Update at runtime
wakeSprite.UpdateSprite(newSprite, fadedColor, scaledSize);

// Toggle visibility for pooling
wakeSprite.SetVisible(false);  // Deactivate
wakeSprite.SetVisible(true);   // Reactivate

// Get bounds for culling
Bounds bounds = wakeSprite.GetSpriteBounds();
```

---

## Integration Points

### Dependencies
- `SpriteRenderer` - Required component (auto-added)
- `CustomWakeParticle` - Primary consumer

---

## Design Notes

### Component Wrapper
- Abstracts SpriteRenderer configuration
- Provides sensible defaults for wake effects
- Simplifies CustomWakeParticle code

### Blend Mode Note
- Default sorting: "Default" layer, order 0
- For best wake appearance, use material with:
  - Sprites/Default shader
  - Alpha blend mode or additive

### Editor Preview
- OnValidate applies settings in edit mode
- Changes visible without entering play mode
- Helps with prefab setup

### Sprite Sorting
- Default layer ensures wake renders behind ships
- Order 0 can be adjusted per-particle if needed
- Consider dedicated "Wake" sorting layer for production
