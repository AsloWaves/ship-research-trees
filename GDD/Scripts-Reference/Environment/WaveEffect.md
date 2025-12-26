# WaveEffect.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/WaveEffect.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~370 |
| **Architecture** | Individual wave effect animation |

## Purpose
Individual wave effect component for ambient ocean wave animations. Handles wave crest movement, foam effects, and ripple animations. Managed by WaveEffectSpawner for object pooling.

---

## Wave Types

```csharp
public enum WaveType
{
    Crest,      // Wave peaks and crests
    Foam,       // Foam patches and whitecaps
    Ripple      // Small surface ripples
}
```

---

## Configuration

### Wave Animation
| Setting | Default | Description |
|---------|---------|-------------|
| `waveType` | Crest | Type of wave effect |
| `scaleMultiplier` | 1.0 | Base scale multiplier |
| `enableRotation` | false | Enable rotation animation |
| `rotationSpeed` | 10 | Degrees per second |

### Movement
| Setting | Default | Description |
|---------|---------|-------------|
| `enableMovement` | true | Move with wind |
| `movementSpeed` | 0.5 | Movement speed multiplier |
| `movementVariation` | 0.3 | Random movement variation |

### Lifecycle
| Setting | Default | Description |
|---------|---------|-------------|
| `enableFadeIn` | true | Fade in animation |
| `fadeInDuration` | 2.0 | Fade in seconds |
| `enableFadeOut` | true | Fade out animation |
| `fadeOutDuration` | 3.0 | Fade out seconds |

---

## Initialization

```csharp
public void Initialize(float animSpeed, float waveLifetime)
{
    animationSpeed = animSpeed;
    lifetime = waveLifetime;
    age = 0f;

    // Random movement direction
    float randomAngle = UnityEngine.Random.Range(0f, 360f);
    movementDirection = new Vector3(
        math.cos(math.radians(randomAngle)),
        0f,
        math.sin(math.radians(randomAngle))
    );

    // Random movement phase
    movementPhase = UnityEngine.Random.Range(0f, 2f * math.PI);

    // Apply scale variation
    float scaleVariation = UnityEngine.Random.Range(0.8f, 1.2f);
    transform.localScale = baseScale * scaleMultiplier * scaleVariation;
}
```

---

## Animation Update

```csharp
public void UpdateWave(float deltaTime, Vector2 windVelocity)
{
    age += deltaTime;

    if (enableMovement)
        UpdateMovement(deltaTime, windVelocity);

    if (enableRotation)
        UpdateRotation(deltaTime);

    UpdateVisualProperties();
}

private void UpdateMovement(float deltaTime, Vector2 windVelocity)
{
    Vector3 windVector = new Vector3(windVelocity.x, 0f, windVelocity.y);
    Vector3 movement = (windVector + movementDirection * movementVariation) * movementSpeed;

    // Sinusoidal variation
    float sineWave = math.sin(age * animationSpeed + movementPhase) * 0.5f;
    movement *= (1f + sineWave * 0.3f);

    transform.position += movement * deltaTime;
}
```

---

## Animation Curves by Wave Type

### Crest
```csharp
// Scale: Start small, grow, fade
scaleCurve.AddKey(0f, 0.5f);
scaleCurve.AddKey(0.3f, 1.2f);
scaleCurve.AddKey(0.7f, 1f);
scaleCurve.AddKey(1f, 0.8f);

// Alpha: Fade in, hold, fade out
alphaCurve.AddKey(0f, 0f);
alphaCurve.AddKey(0.2f, 1f);
alphaCurve.AddKey(0.8f, 1f);
alphaCurve.AddKey(1f, 0f);
```

### Foam
```csharp
// Scale: Quick appearance, steady, dissolve
scaleCurve.AddKey(0f, 0.8f);
scaleCurve.AddKey(0.1f, 1.1f);
scaleCurve.AddKey(0.5f, 1f);
scaleCurve.AddKey(1f, 1.2f);
```

### Ripple
```csharp
// Scale: Expand outward
scaleCurve.AddKey(0f, 0.1f);
scaleCurve.AddKey(0.5f, 1f);
scaleCurve.AddKey(1f, 1.5f);

// Alpha: Start full, fade as expanding
alphaCurve.AddKey(0f, 1f);
alphaCurve.AddKey(0.3f, 0.8f);
alphaCurve.AddKey(1f, 0f);
```

---

## Shader Properties

```csharp
private static readonly int AlphaProperty = Shader.PropertyToID("_Alpha");
private static readonly int TimeProperty = Shader.PropertyToID("_Time");
private static readonly int PhaseProperty = Shader.PropertyToID("_Phase");
```

---

## Public API

### State Queries
```csharp
public float GetAge()        // Current age in seconds
public bool IsExpired()      // age >= lifetime
public float GetAlpha()      // Current alpha value
```

### Control
```csharp
public void Reset()                      // Reset for pooling
public void SetWaveType(WaveType type)   // Change type, reinit curves
```

---

## Usage Example

```csharp
// Created by WaveEffectSpawner
WaveEffect wave = Instantiate(wavePrefab);
wave.Initialize(animSpeed: 0.8f, waveLifetime: 15f);

// Updated each frame by spawner
wave.UpdateWave(Time.deltaTime, windDirection * windStrength);

// Check expiration for pooling
if (wave.IsExpired())
{
    wave.Reset();
    wavePool.Enqueue(wave);
}
```

---

## Integration Points

### Dependencies
- `WaveEffectSpawner` - Lifecycle management
- `Unity.Mathematics` - Math functions
- `MaterialPropertyBlock` - Shader properties

---

## Design Notes

### Object Pooling
- `Reset()` clears state for reuse
- Spawner maintains pool queue
- Avoids runtime allocation

### Animation Curves
- Pre-generated based on wave type
- Smooth tangents applied
- Evaluated each frame for alpha/scale

### Wind Integration
- Wind velocity from spawner
- Combined with random direction
- Sinusoidal variation for natural feel
