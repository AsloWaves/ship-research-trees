# CustomWakeParticle.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/CustomWakeParticle.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~345 |
| **Architecture** | Individual wake particle with custom physics |

## Purpose
Individual wake particle component with custom physics simulation for naval realism. Features drag, buoyancy, and turbulence effects with lifecycle management. Provides fine-grained control over wake behavior that replaces Unity's particle system.

---

## Configuration

### Particle Properties
| Setting | Default | Description |
|---------|---------|-------------|
| `age` | 0 | Current age in seconds |
| `lifetime` | 15 | Maximum lifetime before despawn |
| `size` | 1 | Current size multiplier |
| `alpha` | 1 | Alpha transparency (0-1) |

### Physics
| Setting | Default | Description |
|---------|---------|-------------|
| `velocity` | Vector3.zero | Current velocity in world space |
| `drag` | 0.5 | Drag coefficient for slowdown |
| `buoyancy` | 0.1 | Vertical displacement effect |
| `turbulence` | 0.2 | Random drift influence |

---

## Initialization

```csharp
public void Initialize(WakeParticleSettings settings, Vector3 spawnVelocity, Vector3 spawnPosition)
{
    // Store initial state
    lifetime = settings.baseLifetime;
    initialSize = settings.baseSize;
    initialColor = settings.baseColor;
    initialVelocity = spawnVelocity;

    // Apply ship-specific modifications
    lifetime *= settings.lifetimeMultiplier;
    size = initialSize * settings.sizeMultiplier;
    drag = settings.dragCoefficient;
    buoyancy = settings.buoyancyEffect;
    turbulence = settings.turbulenceStrength;

    // Set initial properties
    velocity = spawnVelocity;
    age = 0f;
    alpha = 1f;

    // Position in world space
    particleTransform.position = spawnPosition;

    // Apply initial visual properties
    if (spriteRenderer != null)
    {
        spriteRenderer.sprite = settings.particleSprite;
        spriteRenderer.color = initialColor;
        particleTransform.localScale = Vector3.one * size;
    }

    isActive = true;
}
```

---

## Physics Simulation

```csharp
private void UpdatePhysics()
{
    float deltaTime = Time.deltaTime;

    // Apply drag (water resistance)
    velocity *= (1f - drag * deltaTime);

    // Apply buoyancy (vertical water displacement)
    velocity.y += buoyancy * deltaTime;

    // Apply turbulence (random water movement)
    if (turbulence > 0f)
    {
        float turbulenceTime = Time.time + turbulencePhase;
        Vector3 turbulenceForce = new Vector3(
            Mathf.Sin(turbulenceTime * 0.7f) * turbulence,
            Mathf.Cos(turbulenceTime * 0.5f) * turbulence * 0.5f,
            Mathf.Sin(turbulenceTime * 0.9f) * turbulence
        ) * deltaTime;

        velocity += turbulenceForce;
    }

    // Apply velocity to position
    particleTransform.position += velocity * deltaTime;
}
```

---

## Lifecycle Animation

### Size Evolution
```csharp
// Growth phase (0-30% of lifetime)
if (lifecycleProgress < 0.3f)
    sizeProgress = Mathf.Lerp(0.2f, 1f, lifecycleProgress / 0.3f);

// Stable phase (30-70% of lifetime)
else if (lifecycleProgress < 0.7f)
    sizeProgress = 1f;

// Decay phase (70-100% of lifetime)
else
    sizeProgress = Mathf.Lerp(1f, 0.3f, (lifecycleProgress - 0.7f) / 0.3f);
```

### Alpha Fade
```csharp
// Alpha fade: sharp fade in final 20% of lifetime
if (lifecycleProgress > 0.8f)
    alpha = Mathf.Lerp(1f, 0f, (lifecycleProgress - 0.8f) / 0.2f);
else
    alpha = 1f;
```

---

## WakeParticleSettings Struct

```csharp
[System.Serializable]
public struct WakeParticleSettings
{
    [Header("Base Properties")]
    public float baseLifetime;          // Base particle lifetime in seconds
    public float baseSize;              // Base particle size
    public Color baseColor;             // Base particle color
    public Sprite particleSprite;       // Sprite to use for particle

    [Header("Ship-Specific Modifiers")]
    public float lifetimeMultiplier;    // Ship-specific lifetime modifier
    public float sizeMultiplier;        // Ship-specific size modifier
    public float densityMultiplier;     // Ship-specific spawn rate modifier

    [Header("Physics")]
    public float dragCoefficient;       // Water resistance
    public float buoyancyEffect;        // Vertical displacement
    public float turbulenceStrength;    // Random movement intensity

    [Header("Visual Effects")]
    public AnimationCurve sizeOverLifetime;   // Size evolution curve
    public AnimationCurve alphaOverLifetime;  // Alpha evolution curve
    public bool enableRotation;               // Particle rotation based on velocity
}
```

---

## Public API

### State Queries
```csharp
public float GetAge()           // Current age in seconds
public WakeParticleStatus GetStatus()  // Full status for debugging
```

### Control
```csharp
public void ApplyForce(Vector3 force)  // Apply external force (wind, wash)
public void DestroyParticle()          // Manually destroy/return to pool
```

### WakeParticleStatus
```csharp
public struct WakeParticleStatus
{
    public float age;
    public float lifetime;
    public float size;
    public float alpha;
    public Vector3 velocity;
    public Vector3 position;
    public bool isActive;
}
```

---

## Usage Example

```csharp
// Created by CustomWakeSpawner
CustomWakeParticle particle = Instantiate(particlePrefab);

// Initialize with ship-specific settings
WakeParticleSettings settings = WakeParticleSettings.Default();
settings.lifetimeMultiplier = 1.5f;  // Larger ship = longer wake
settings.sizeMultiplier = 2.0f;       // Larger ship = bigger particles

particle.Initialize(settings, shipVelocity * 0.3f, spawnPosition);

// Apply external force (wind effect)
particle.ApplyForce(windDirection * windStrength);

// Check status
var status = particle.GetStatus();
Debug.Log($"Particle: Age={status.age:F1}s, Size={status.size:F2}");
```

---

## Integration Points

### Dependencies
- `WakeParticleSettings` - Configuration struct (same file)
- `WakeParticleStatus` - Status struct (same file)
- `CustomWakeSpawner` - Lifecycle manager
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Physics Model
- Drag simulates water resistance (velocity decay)
- Buoyancy creates vertical displacement
- Turbulence adds natural random movement via sinusoidal functions
- Uses unique phase offset per particle for variety

### Lifecycle Phases
- **0-30%**: Growth phase (size 0.2 → 1.0)
- **30-70%**: Stable phase (size 1.0)
- **70-100%**: Decay phase (size 1.0 → 0.3)
- **80-100%**: Alpha fade (1.0 → 0.0)

### Performance
- Static camera reference (cached once)
- Distance culling at 2000 units
- Random turbulence phase prevents synchronized movement
- Rotation based on velocity magnitude

### Object Pooling Ready
- `DestroyParticle()` can be enhanced to return to pool
- `isActive` flag for pool management
- Settings struct enables quick reinitialization
