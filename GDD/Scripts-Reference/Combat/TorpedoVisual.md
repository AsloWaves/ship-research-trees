---
tags: [script, combat, visual, client, implemented]
script-type: MonoBehaviour
namespace: WOS.Combat.Visuals
file-path: Assets/Scripts/Combat/Visuals/TorpedoVisual.cs
status: IMPLEMENTED
size: ~8 KB (301 lines)
feature-group: combat
---

# TorpedoVisual.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Combat.Visuals
**File**: `Assets/Scripts/Combat/Visuals/TorpedoVisual.cs`
**Size**: ~8 KB (301 lines)
**Dependencies**: TorpedoDefinitionSO

---

## Purpose
Client-side torpedo visual. Handles torpedo sprite, wake effect, and movement interpolation. Unlike shells, torpedoes travel in straight lines without gravity.

This component manages:
- Torpedo sprite rendering
- Wake trail effect
- Bubble particle effects
- Straight-line movement with wobble
- Heading maintenance

---

## Configuration

### Inspector Fields
```
[Header("Visual Components")]
spriteRenderer (SpriteRenderer): Torpedo sprite
wakeTrail (TrailRenderer): Wake trail effect
bubbleEffect (ParticleSystem): Bubble particles

[Header("Movement")]
velocity (Vector3): Movement velocity
wobbleAmount (float, 0.1): Side-to-side wobble
wobbleSpeed (float, 2): Wobble frequency

[Header("Lifetime")]
maxLifetime (float, 120): Max display time (2 min)

[Header("Wake Settings")]
wakeWidth (float, 0.3): Trail width
wakeLength (float, 2): Trail length
wakeColor (Color): Wake color (white, 0.5 alpha)
```

---

## Properties

```csharp
public uint TorpedoId { get; }  // Network torpedo ID
```

---

## Initialization Methods

### Initialize (Full)
```csharp
public void Initialize(
    uint id,
    Vector3 direction,
    float speed,
    TorpedoDefinitionSO torpedoDef = null)
```
- Sets velocity from direction and speed
- Applies sprite from torpedoDef
- Adjusts wake width based on torpedo diameter
- Sets up wake trail

### Initialize (Simple)
```csharp
public void Initialize(
    uint id,
    Vector3 direction,
    float speed,
    Sprite sprite)
```
- Simpler version for RPC spawning
- Sets sprite directly

---

## Movement System

### No Gravity
Unlike shells, torpedoes maintain straight-line travel:

```csharp
private void UpdateMovement()
{
    // Torpedoes travel in straight line (no gravity)
    // Add slight wobble for realism
    float wobble = Mathf.Sin((Time.time + wobbleOffset) * wobbleSpeed)
                 * wobbleAmount;
    Vector3 wobbleDir = Vector3.Cross(velocity.normalized, Vector3.forward);

    Vector3 finalVelocity = velocity + wobbleDir * wobble;
    transform.position += finalVelocity * Time.deltaTime;

    // Maintain heading
    if (velocity.sqrMagnitude > 0.01f)
    {
        float angle = Mathf.Atan2(velocity.y, velocity.x) * Mathf.Rad2Deg - 90f;
        transform.rotation = Quaternion.Euler(0, 0, angle);
    }
}
```

### Wobble Effect
Random wobble offset per torpedo for natural variation:
```csharp
private void Awake()
{
    wobbleOffset = Random.value * Mathf.PI * 2f;
}
```

---

## Wake Trail Setup

```csharp
private void SetupWakeTrail()
{
    if (wakeTrail == null) return;

    wakeTrail.time = wakeLength / velocity.magnitude;
    wakeTrail.startWidth = wakeWidth;
    wakeTrail.endWidth = wakeWidth * 0.5f;

    // Set wake color gradient
    var gradient = new Gradient();
    gradient.SetKeys(
        new GradientColorKey[]
        {
            new GradientColorKey(wakeColor, 0f),
            new GradientColorKey(wakeColor, 1f)
        },
        new GradientAlphaKey[]
        {
            new GradientAlphaKey(wakeColor.a, 0f),
            new GradientAlphaKey(0f, 1f)  // Fade out
        }
    );
    wakeTrail.colorGradient = gradient;
}
```

---

## Effects

### On Torpedo Hit
```csharp
public void OnTorpedoHit(Vector3 hitPoint)
{
    // Stop wake trail
    if (wakeTrail != null)
        wakeTrail.emitting = false;

    if (bubbleEffect != null)
    {
        var emission = bubbleEffect.emission;
        emission.enabled = false;
    }

    // Let wake trail finish, then destroy
    float destroyDelay = wakeTrail?.time ?? 0.1f;
    Destroy(gameObject, destroyDelay);
}
```

### On Torpedo Expired
Called when torpedo runs out of range.
```csharp
public void OnTorpedoExpired()
{
    // Same cleanup as hit
    // Stop effects, delayed destroy
}
```

---

## Static Factory

### CreateSimpleTorpedo
Creates a basic torpedo visual when no prefab assigned.

```csharp
public static TorpedoVisual CreateSimpleTorpedo(
    Vector3 position,
    Vector3 direction,
    float speed)
{
    var go = new GameObject("TorpedoVisual");
    go.transform.position = position;

    // Add sprite renderer (long dark rectangle)
    var sr = go.AddComponent<SpriteRenderer>();
    sr.sprite = CreateTorpedoSprite();
    sr.color = new Color(0.2f, 0.2f, 0.2f);  // Dark gray
    sr.sortingOrder = 50;

    // Add wake trail
    var trail = go.AddComponent<TrailRenderer>();
    trail.time = 3f;
    trail.startWidth = 0.2f;
    trail.endWidth = 0.05f;
    trail.startColor = new Color(1f, 1f, 1f, 0.6f);
    trail.endColor = new Color(1f, 1f, 1f, 0f);

    // Add visual component
    var visual = go.AddComponent<TorpedoVisual>();
    visual.Initialize(0, direction, speed, (Sprite)null);

    return visual;
}
```

### Sprite Generation
```csharp
private static Sprite CreateTorpedoSprite()
{
    // 2x10 rectangle for torpedo shape
    int width = 2;
    int height = 10;

    var texture = new Texture2D(width, height);
    // Fill with black color
    texture.filterMode = FilterMode.Point;

    // Pivot at center, facing up
    return Sprite.Create(texture,
        new Rect(0, 0, width, height),
        new Vector2(0.5f, 0.5f), 32f);
}
```

---

## Sorting Layer
```
sortingLayerName: "Default"
sortingOrder: 50 (below shells, above water)
```

---

## Key Differences from ProjectileVisual

| Feature | ProjectileVisual | TorpedoVisual |
|---------|-----------------|---------------|
| Gravity | Yes | No |
| Wobble | No | Yes |
| Lifetime | 30s | 120s |
| Trail | Tracer | Wake |
| Color | Yellow/ammo-based | White/translucent |

---

## Integration Points

### Spawned By
- [[ProjectileManager]] - Via RpcSpawnTorpedoVisual

### Uses
- [[TorpedoDefinitionSO]] - Visual configuration

---

## Related Files
- [[ProjectileManager]] - Spawns and manages visuals
- [[TorpedoDefinitionSO]] - Visual configuration
- [[TorpedoController]] - Launches torpedoes
- [[ProjectileVisual]] - Similar for shells

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added wobble effect
- **2025-01**: Added static factory

