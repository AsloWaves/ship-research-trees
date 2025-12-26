---
tags: [script, combat, visual, client, implemented]
script-type: MonoBehaviour
namespace: WOS.Combat.Visuals
file-path: Assets/Scripts/Combat/Visuals/ProjectileVisual.cs
status: IMPLEMENTED
size: ~8 KB (289 lines)
feature-group: combat
---

# ProjectileVisual.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Combat.Visuals
**File**: `Assets/Scripts/Combat/Visuals/ProjectileVisual.cs`
**Size**: ~8 KB (289 lines)
**Dependencies**: AmmunitionDefinitionSO

---

## Purpose
Client-side projectile visual for shells. Spawned by ProjectileManager RPC, handles visual representation only. Server handles actual physics and collision.

This component manages:
- Shell sprite rendering
- Tracer/trail effects
- Client-side movement interpolation
- Velocity-based rotation
- Lifetime and fade-out

---

## Configuration

### Inspector Fields
```
[Header("Visual Components")]
spriteRenderer (SpriteRenderer): Shell sprite
trailRenderer (TrailRenderer): Tracer trail
smokeTrail (ParticleSystem): Smoke particles

[Header("Movement")]
velocity (Vector3): Simulated velocity

[Header("Lifetime")]
maxLifetime (float, 30): Max display time
fadeOutTime (float, 0.5): Fade out duration

[Header("Effects")]
rotateToVelocity (bool, true): Face movement direction
trailTime (float, 0.5): Trail length
```

---

## Properties

```csharp
public uint ProjectileId { get; }  // Network projectile ID
```

---

## Initialization Methods

### Initialize (Full)
```csharp
public void Initialize(
    uint id,
    Vector3 direction,
    float speed,
    AmmunitionDefinitionSO ammoDef = null)
```
- Sets velocity from direction and speed
- Applies sprite and tracer color from ammoDef
- Sets initial rotation toward velocity

### Initialize (Simple)
```csharp
public void Initialize(
    uint id,
    Vector3 direction,
    float speed,
    Sprite sprite,
    Color tracerColor)
```
- Simpler version for RPC spawning
- Directly sets sprite and tracer color

---

## Update Logic

### Movement
```csharp
private void UpdateMovement()
{
    if (isFading) return;

    // Apply gravity for visual realism
    velocity.y -= 9.81f * Time.deltaTime;

    transform.position += velocity * Time.deltaTime;
}
```
Note: Simple linear + gravity. Server handles actual physics.

### Rotation
```csharp
private void UpdateRotation()
{
    if (!rotateToVelocity || velocity.sqrMagnitude < 0.01f) return;

    float angle = Mathf.Atan2(velocity.y, velocity.x) * Mathf.Rad2Deg - 90f;
    transform.rotation = Quaternion.Euler(0, 0, angle);
}
```

### Lifetime
```csharp
private void UpdateLifetime()
{
    float elapsed = Time.time - spawnTime;

    if (!isFading && elapsed >= maxLifetime - fadeOutTime)
    {
        StartFadeOut();
    }

    if (elapsed >= maxLifetime)
    {
        Destroy(gameObject);
    }
}
```

---

## Effects

### Fade Out
```csharp
private void StartFadeOut()
{
    isFading = true;

    if (trailRenderer != null)
        trailRenderer.emitting = false;

    if (smokeTrail != null)
    {
        var emission = smokeTrail.emission;
        emission.enabled = false;
    }
}
```

### On Destroyed
Called by ProjectileManager RPC when projectile hits or expires.
```csharp
public void OnProjectileDestroyed(bool hit, Vector3 hitPoint)
{
    // Stop trail emission
    // Let trail finish, then destroy
    float destroyDelay = trailRenderer?.time ?? 0.1f;
    Destroy(gameObject, destroyDelay);
}
```

---

## Static Factory

### CreateSimpleShell
Creates a basic shell visual when no prefab is assigned.

```csharp
public static ProjectileVisual CreateSimpleShell(
    Vector3 position,
    Vector3 direction,
    float speed,
    int caliberMM)
{
    var go = new GameObject("ShellVisual");
    go.transform.position = position;

    // Add sprite renderer (sized by caliber)
    var sr = go.AddComponent<SpriteRenderer>();
    sr.sprite = CreateSimpleSprite(caliberMM);

    // Add trail renderer (yellow tracer)
    var trail = go.AddComponent<TrailRenderer>();
    trail.time = 0.3f;
    trail.startWidth = caliberMM * 0.001f;
    trail.startColor = new Color(1f, 0.8f, 0.2f, 1f);

    // Add visual component
    var visual = go.AddComponent<ProjectileVisual>();
    visual.Initialize(0, direction, speed, null, Color.yellow);

    return visual;
}
```

### Sprite Generation
```csharp
private static Sprite CreateSimpleSprite(int caliberMM)
{
    int width = Mathf.Clamp(caliberMM / 20, 1, 4);
    int height = Mathf.Clamp(caliberMM / 10, 2, 8);

    var texture = new Texture2D(width, height);
    // Fill with yellow color
    texture.filterMode = FilterMode.Point;

    return Sprite.Create(texture,
        new Rect(0, 0, width, height),
        new Vector2(0.5f, 0.5f), 32f);
}
```

---

## Integration Points

### Spawned By
- [[ProjectileManager]] - Via RpcSpawnProjectileVisual

### Uses
- [[AmmunitionDefinitionSO]] - Tracer colors, sprites

---

## Sorting Layer
```
sortingLayerName: "Default"
sortingOrder: 100 (above ships)
```

---

## Performance Notes

- Client-side only, no network sync per-frame
- Simple physics (gravity only) for visual approximation
- Trail renderer for tracer effect
- Auto-cleanup after lifetime expires
- Delayed destroy allows trail to finish

---

## Related Files
- [[ProjectileManager]] - Spawns and manages visuals
- [[AmmunitionDefinitionSO]] - Visual configuration
- [[TorpedoVisual]] - Similar for torpedoes

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added static factory
- **2025-01**: Added fade-out effects

