# ShipWakeController.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/ShipWakeController.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~546 |
| **Architecture** | Physics-based ship wake effects |

## Purpose
Controls ship wake and trail effects based on ship movement and physics. Integrates with NetworkedNavalController (multiplayer) or SimpleNavalController (testing) for realistic wake generation. Supports particle systems, trail renderers, and LOD optimization.

---

## Configuration

### Wake Configuration
| Setting | Default | Description |
|---------|---------|-------------|
| `mainWakeParticles` | - | Particle system for main wake trail |
| `turbulenceParticles` | - | Particle system for bubbles/turbulence |
| `wakeTrail` | - | TrailRenderer for continuous wake line |

### Wake Intensity
| Setting | Default | Description |
|---------|---------|-------------|
| `baseEmissionRate` | 50 | Base particle emission rate |
| `maxEmissionRate` | 250 | Max emission at full speed |
| `minimumWakeSpeed` | 1 | Min speed before wake appears |
| `maxIntensitySpeed` | 15 | Speed for max wake intensity |

### Wake Position
| Setting | Default | Description |
|---------|---------|-------------|
| `wakeSpawnOffset` | (0, -1, -3) | Offset from ship center |
| `adjustForShipLength` | true | Auto-adjust based on ship size |

### Turning Effects
| Setting | Default | Description |
|---------|---------|-------------|
| `turningIntensityMultiplier` | 1.5 | Extra wake when turning |
| `turningThreshold` | 10 | Rudder angle threshold |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `lodDistance` | 1000 | Distance for LOD reduction |
| `updateInterval` | 0.1 | Seconds between calculations |
| `disableParticlesForTesting` | false | Debug: disable for Job System testing |

---

## Controller Integration

```csharp
private void Awake()
{
    // Try NetworkedNavalController first (multiplayer)
    shipController = GetComponent<NetworkedNavalController>();
    if (shipController == null)
        shipController = GetComponent<SimpleNavalController>();  // Fallback (testing)
}

private void Start()
{
    // Subscribe to speed events based on controller type
    if (shipController is NetworkedNavalController)
        NetworkedNavalController.OnSpeedChangedEvent += OnShipSpeedChanged;
    else if (shipController is SimpleNavalController)
        SimpleNavalController.OnSpeedChanged += OnShipSpeedChanged;
}
```

---

## Wake Intensity Calculation

```csharp
private float CalculateSpeedIntensity(float speed)
{
    if (speed < minimumWakeSpeed)
        return 0f;

    float normalizedSpeed = Mathf.Clamp01(speed / maxIntensitySpeed);
    return Mathf.Lerp(0.2f, 1f, normalizedSpeed);
}

private float CalculateTurningIntensity(float rudderAngle, float speed)
{
    float absRudder = Mathf.Abs(rudderAngle);
    if (absRudder < turningThreshold || speed < minimumWakeSpeed)
        return 0f;

    float rudderFactor = Mathf.Clamp01(absRudder / 35f);
    float speedFactor = Mathf.Clamp01(speed / 10f);

    return rudderFactor * speedFactor * turningIntensityMultiplier;
}
```

---

## Particle Velocity Compensation

```csharp
// Apply velocity compensation so particles "stay in water"
Vector3 shipVelocity = (transform.position - lastShipPosition) / Time.deltaTime;
float shipSpeedKnots = shipVelocity.magnitude * 1.944f;  // m/s to knots

// Dynamic spawn offset for high speeds
float speedCompensation = Mathf.Clamp(shipSpeedKnots * 0.1f, 0f, 2f);
Vector3 dynamicOffset = wakeSpawnOffset - (shipForward * speedCompensation);

// Counteract ship movement with particle velocity
Vector3 velocityCompensation = -shipVelocity * 0.3f;
velocityOverLifetime.x = new ParticleSystem.MinMaxCurve(velocityCompensation.x);
velocityOverLifetime.y = new ParticleSystem.MinMaxCurve(velocityCompensation.y);
```

---

## LOD Management

```csharp
private void SetDetailLevel(bool highDetail)
{
    if (mainWakeParticles != null)
    {
        var main = mainWakeParticles.main;
        main.maxParticles = highDetail ? 1000 : 200;
    }

    if (turbulenceParticles != null)
    {
        var main = turbulenceParticles.main;
        main.maxParticles = highDetail ? 500 : 100;
    }

    if (wakeTrail != null)
        wakeTrail.enabled = highDetail;
}
```

---

## Public API

### Get Wake Statistics
```csharp
public WakeStats GetWakeStats()
// Returns: isActive, intensity, speed, rudderAngle, isHighDetail, particleCount

public struct WakeStats
{
    public bool isActive;
    public float intensity;
    public float speed;
    public float rudderAngle;
    public bool isHighDetail;
    public int particleCount;
}
```

### Trigger Wake Burst
```csharp
public void TriggerWakeBurst(float burstIntensity = 2f)
// Manual wake burst for special events (explosions, etc.)
```

---

## Usage Example

```csharp
// Wake controller auto-initializes on ship prefab
// Access wake stats for UI display
ShipWakeController wake = ship.GetComponent<ShipWakeController>();
WakeStats stats = wake.GetWakeStats();
Debug.Log($"Wake active: {stats.isActive}, Intensity: {stats.intensity:F2}");

// Trigger burst on impact
wake.TriggerWakeBurst(3f);
```

---

## Integration Points

### Dependencies
- `NetworkedNavalController` or `SimpleNavalController` - Ship physics
- `ShipDefinitionSO` - Ship configuration (length for offset)
- `WOS.Debugging.DebugManager` - Logging

### Related Systems
- `EnvironmentLODManager` - LOD coordination
- `OceanChunkManager` - Ocean rendering

---

## Design Notes

### World Space Simulation
- Particles use `ParticleSystemSimulationSpace.World`
- Particles stay in water as ship moves
- Velocity compensation counteracts ship movement

### Performance
- Updates at configurable interval (not every frame)
- LOD reduces particle counts for distant ships
- Trail disabled at low detail levels

### Ship Size Adaptation
- Wake spawn offset scales with ship length
- Larger ships = wake spawns further back
