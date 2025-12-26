# CustomWakeSpawner.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/CustomWakeSpawner.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~454 |
| **Architecture** | Ship-specific wake spawning with object pooling |

## Purpose
Custom wake particle spawner with ship-specific control over size, density, shape, and lifetime. Replaces Unity's particle system for more realistic naval wake physics. Uses object pooling for performance and animation curves for ship characteristic-based wake properties.

---

## Configuration

### Ship Configuration
| Setting | Description |
|---------|-------------|
| `shipController` | Reference to NetworkedNavalController or SimpleNavalController |
| `wakeSpawnOffset` | Offset from ship center (default: 0, -2, 0) |

### Wake Particle Settings
| Setting | Description |
|---------|-------------|
| `wakeSettings` | Base WakeParticleSettings configuration |
| `wakeParticlePrefab` | Prefab with CustomWakeParticle component |

### Spawning Control
| Setting | Default | Description |
|---------|---------|-------------|
| `baseSpawnRate` | 10 | Particles per second when moving |
| `maxActiveParticles` | 300 | Maximum active particles |
| `minimumSpeedThreshold` | 0.5 | Minimum speed (knots) to spawn |

### Ship-Specific Properties
| Setting | Description |
|---------|-------------|
| `densityByDisplacement` | AnimationCurve: 1000t→0.5x, 50000t→2x |
| `sizeByLength` | AnimationCurve: 50m→0.5x, 300m→3x |
| `lifetimeByBeam` | AnimationCurve: 10m→0.8x, 50m→1.5x |

### Wake Physics
| Setting | Default | Description |
|---------|---------|-------------|
| `wakeSpreadAngle` | 45 | Spread angle in degrees |
| `velocityInheritance` | 0.3 | Velocity inheritance from ship |
| `velocityVariation` | 0.5 | Random velocity variation |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `updateInterval` | 0.05 | Spawn update frequency |
| `cullDistance` | 1500 | Distance for culling particles |

---

## Object Pooling

```csharp
private void PopulateParticlePool()
{
    if (wakeParticlePrefab == null) return;

    // Pre-create pool of particles
    int poolSize = Mathf.Min(maxActiveParticles / 2, 100);

    for (int i = 0; i < poolSize; i++)
    {
        GameObject pooledParticle = Instantiate(wakeParticlePrefab, particleContainer);
        pooledParticle.SetActive(false);
        particlePool.Enqueue(pooledParticle);
    }
}

private GameObject GetPooledParticle()
{
    // Try to get from pool first
    if (particlePool.Count > 0)
    {
        GameObject pooledParticle = particlePool.Dequeue();
        pooledParticle.SetActive(true);
        return pooledParticle;
    }

    // Create new if pool is empty and under limit
    if (activeParticles.Count < maxActiveParticles && wakeParticlePrefab != null)
    {
        return Instantiate(wakeParticlePrefab, particleContainer);
    }

    return null;
}
```

---

## Ship-Specific Wake Calculation

```csharp
private WakeParticleSettings CalculateShipSpecificSettings(float currentSpeed)
{
    WakeParticleSettings settings = wakeSettings;

    // Apply ship-specific modifiers based on ship characteristics
    if (shipPropertiesCached)
    {
        settings.densityMultiplier = densityByDisplacement.Evaluate(shipDisplacement);
        settings.sizeMultiplier = sizeByLength.Evaluate(shipLength);
        settings.lifetimeMultiplier = lifetimeByBeam.Evaluate(shipBeam);

        // Speed affects turbulence and drag
        settings.turbulenceStrength = wakeSettings.turbulenceStrength * (1f + currentSpeed * 0.05f);
        settings.dragCoefficient = wakeSettings.dragCoefficient * (1f + currentSpeed * 0.02f);
    }

    return settings;
}
```

---

## Wake Spawning

```csharp
private void SpawnWakeParticle(WakeParticleSettings settings, float shipSpeed)
{
    // Calculate spawn position with speed compensation
    Vector3 shipVelocity = (transform.position - lastShipPosition) / Time.deltaTime;
    Vector3 shipForward = transform.up; // 2D ship forward direction

    // Speed compensation to reduce gap at high speeds
    float speedCompensation = Mathf.Clamp(shipSpeed * 0.08f, 0f, 1.5f);
    Vector3 compensatedOffset = wakeSpawnOffset - (shipForward * speedCompensation);

    // Add random spread within wake angle
    float randomAngle = UnityEngine.Random.Range(-wakeSpreadAngle * 0.5f, wakeSpreadAngle * 0.5f);
    Vector3 spreadDirection = Quaternion.Euler(0f, 0f, randomAngle) * Vector3.right;

    Vector3 spawnPosition = transform.position + transform.TransformDirection(compensatedOffset);
    spawnPosition += transform.TransformDirection(spreadDirection) * UnityEngine.Random.Range(0f, 2f);

    // Calculate initial particle velocity
    Vector3 wakeDirection = (-shipForward + spreadDirection).normalized;
    Vector3 particleVelocity = shipVelocity * velocityInheritance;
    particleVelocity += wakeDirection * UnityEngine.Random.Range(0.5f, 2f);

    // Add velocity variation
    particleVelocity += new Vector3(
        UnityEngine.Random.Range(-velocityVariation, velocityVariation),
        UnityEngine.Random.Range(-velocityVariation, velocityVariation),
        UnityEngine.Random.Range(-velocityVariation * 0.5f, velocityVariation * 0.5f)
    );

    // Get particle from pool and initialize
    GameObject particleObj = GetPooledParticle();
    if (particleObj == null) return;

    CustomWakeParticle particle = particleObj.GetComponent<CustomWakeParticle>();
    if (particle != null)
    {
        particle.Initialize(settings, particleVelocity, spawnPosition);
        activeParticles.Add(particle);
    }
}
```

---

## Controller Support

```csharp
/// Get ship status from controller (supports both controller types)
private ShipStatus GetShipStatus()
{
    if (shipController is NetworkedNavalController networked)
        return networked.GetShipStatus();
    else if (shipController is SimpleNavalController simple)
        return simple.GetShipStatus();

    return new ShipStatus();
}

/// Get ship configuration from controller
private ShipDefinitionSO GetShipConfiguration()
{
    if (shipController is NetworkedNavalController networked)
        return networked.GetShipConfiguration();
    else if (shipController is SimpleNavalController simple)
        return simple.GetShipConfiguration();

    return null;
}
```

---

## Public API

### Statistics
```csharp
public CustomWakeStats GetStats()

public struct CustomWakeStats
{
    public int activeParticleCount;
    public int pooledParticleCount;
    public int particlesSpawnedThisFrame;
    public int particlesCulledThisFrame;
    public float currentSpawnRate;
    public float shipDisplacement;
    public float shipLength;
    public float shipBeam;
}
```

### Control
```csharp
public void ClearAllParticles()  // Force clear all active particles
```

---

## Usage Example

```csharp
// Attached to ship prefab
CustomWakeSpawner spawner = ship.GetComponent<CustomWakeSpawner>();

// Get wake statistics
var stats = spawner.GetStats();
Debug.Log($"Wake: {stats.activeParticleCount} active, {stats.pooledParticleCount} pooled");

// Clear wake on scene transition
spawner.ClearAllParticles();
```

---

## Integration Points

### Dependencies
- `CustomWakeParticle` - Individual particle component
- `WakeParticleSettings` - Configuration struct
- `NetworkedNavalController` - Multiplayer ship controller
- `SimpleNavalController` - Single-player ship controller
- `ShipDefinitionSO` - Ship configuration ScriptableObject
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Ship Characteristic-Based Wake
- **Displacement**: Heavier ships = denser wake (more particles)
- **Length**: Longer ships = larger wake particles
- **Beam**: Wider ships = longer-lasting wake
- AnimationCurves allow fine-tuning per ship class

### Speed Compensation
- High-speed ships would leave gaps without compensation
- Offset moves spawn point backward relative to speed
- Prevents visible spacing at full speed

### Wake Spread Pattern
- V-shaped wake pattern using spread angle
- Random variation within angle for natural appearance
- Velocity inheritance creates realistic momentum

### Performance Optimizations
- Object pooling with Queue<GameObject>
- Pre-populated pool (50% of max, capped at 100)
- Update interval controls spawn frequency
- Distance-based culling from ship
- Max 5 particles spawned per update
