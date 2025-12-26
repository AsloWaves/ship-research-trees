# HarborEffects.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/HarborEffects.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~727 |
| **Architecture** | Harbor ambient effects with URP 2D lighting |

## Purpose
Manages harbor ambient effects including particle systems, audio, and dynamic lighting. Optimized for URP 2D rendering pipeline with LOD and performance management. Responds to player proximity and time of day.

---

## Configuration

### Configuration Asset
| Setting | Description |
|---------|-------------|
| `visualConfig` | `PortVisualConfigurationSO` for effect settings |

### Effect Detection
| Setting | Default | Description |
|---------|---------|-------------|
| `detectionRadius` | 200 | Radius for ship detection |
| `shipLayerMask` | Layer 8 | Layer mask for ships |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `updateInterval` | 0.5 | Seconds between updates |
| `maxEffectDistance` | 600 | Max distance before culling |

### Audio
| Setting | Description |
|---------|-------------|
| `ambientAudioSource` | Ambient harbor sounds |
| `interactiveAudioSource` | One-shot event sounds |

### Lighting
| Setting | Description |
|---------|-------------|
| `harborLights` | Light2D array for harbor |
| `enableDynamicLighting` | Time of day lighting |

---

## Effect Categories

### Water Effects
- Water splash effects around docks
- Foam effects near shore
```csharp
private void CreateWaterEffects()
{
    if (visualConfig.waterSplashPrefab != null)
    {
        for (int i = 0; i < visualConfig.waterEffectCount; i++)
        {
            Vector3 spawnPos = transform.position + GetRandomWaterPosition();
            GameObject effect = Instantiate(visualConfig.waterSplashPrefab, spawnPos, Quaternion.identity, effectsContainer);
            ParticleSystem ps = effect.GetComponent<ParticleSystem>();
            waterEffects.Add(ps);
        }
    }
}
```

### Atmospheric Effects
- Mist/fog
- Seagulls
```csharp
private void CreateAtmosphericEffects()
{
    if (visualConfig.mistEffectPrefab != null)
    {
        // Central mist effect
        Vector3 spawnPos = transform.position + Vector3.up * 5f;
        GameObject effect = Instantiate(visualConfig.mistEffectPrefab, spawnPos, ...);
    }

    if (visualConfig.seagullEffectPrefab != null)
    {
        for (int i = 0; i < visualConfig.seagullCount; i++)
        {
            // Sky position seagulls
        }
    }
}
```

### Structural Effects
- Smoke from chimneys
- Building effects

---

## Ship Detection (Physics2D)

```csharp
private void DetectShipsInRange()
{
    detectedShips.Clear();
    playerInRange = false;

    Collider2D[] ships = Physics2D.OverlapCircleAll(transform.position, detectionRadius, shipLayerMask);

    foreach (Collider2D ship in ships)
    {
        detectedShips.Add(ship.transform);

        if (ship.CompareTag("Player"))
            playerInRange = true;
    }
}
```

---

## LOD Integration

```csharp
private void ApplyLODSettings()
{
    float lodMultiplier = currentLOD switch
    {
        LODLevel.High => 1f,
        LODLevel.Medium => 0.75f,
        LODLevel.Low => 0.5f,
        LODLevel.VeryLow => 0.25f,
        LODLevel.Culled => 0f,
        _ => 1f
    };

    effectIntensityMultiplier = lodMultiplier;

    ApplyIntensityToEffects(waterEffects, lodMultiplier);
    ApplyIntensityToEffects(atmosphericEffects, lodMultiplier);
    ApplyIntensityToEffects(structuralEffects, lodMultiplier);
}
```

---

## Dynamic Lighting (URP 2D)

```csharp
private void UpdateLightingForTimeOfDay()
{
    // dayFactor peaks at noon (timeOfDay = 0.5)
    float dayFactor = Mathf.Clamp01(1f - Mathf.Abs((timeOfDay - 0.5f) * 2f));
    float nightFactor = 1f - dayFactor;

    for (int i = 0; i < harborLights.Length; i++)
    {
        if (harborLights[i] != null)
        {
            // Harbor lights brighter at night
            float intensity = originalLightIntensities[i] * (0.3f + nightFactor * 0.7f);
            Color color = Color.Lerp(visualConfig.dayLightColor, visualConfig.nightLightColor, nightFactor);

            harborLights[i].intensity = intensity;
            harborLights[i].color = color;
        }
    }
}
```

---

## Audio Management

```csharp
private void InitializeAudioSystems()
{
    if (ambientAudioSource != null && visualConfig.ambientHarborSound != null)
    {
        ambientAudioSource.clip = visualConfig.ambientHarborSound;
        ambientAudioSource.loop = true;
        ambientAudioSource.volume = 0f;
        ambientAudioSource.spatialBlend = 0.7f;  // Mostly 3D
        ambientAudioSource.rolloffMode = AudioRolloffMode.Logarithmic;
        ambientAudioSource.maxDistance = detectionRadius;
        ambientAudioSource.Play();
    }
}

private void UpdateAudioSystems()
{
    // Smooth volume transitions
    currentAmbientVolume = Mathf.Lerp(currentAmbientVolume, targetAmbientVolume, Time.deltaTime * 2f);
    ambientAudioSource.volume = currentAmbientVolume;
}
```

---

## Effect Intensity Based on Ships

```csharp
private void UpdateEffectIntensity()
{
    float baseIntensity = playerInRange ? 1f : 0.3f;
    float shipMultiplier = 1f + (detectedShips.Count * 0.1f);
    float targetIntensity = baseIntensity * shipMultiplier * effectIntensityMultiplier;

    // Water effects most responsive
    foreach (ParticleSystem ps in waterEffects)
    {
        var emission = ps.emission;
        emission.rateOverTimeMultiplier = targetIntensity;
    }

    // Atmospheric effects less responsive
    float atmosphericIntensity = Mathf.Lerp(0.5f, targetIntensity, 0.3f);
    // ...
}
```

---

## Public API

### Play Interactive Sound
```csharp
public void PlayInteractiveSound(AudioClip clip, float volume = 1f)
// One-shot sound effect
```

### Get Statistics
```csharp
public HarborEffectsStats GetStats()

public struct HarborEffectsStats
{
    public bool effectsActive;
    public bool playerInRange;
    public int detectedShipCount;
    public LODLevel currentLOD;
    public float effectIntensity;
    public float ambientVolume;
    public float timeOfDay;
}
```

---

## Usage Example

```csharp
// Effects auto-activate when player enters range
HarborEffects harbor = FindFirstObjectByType<HarborEffects>();

// Get current state
var stats = harbor.GetStats();
Debug.Log($"Harbor: Active={stats.effectsActive}, Ships={stats.detectedShipCount}");

// Play docking sound
harbor.PlayInteractiveSound(dockingClip, 0.8f);
```

---

## Integration Points

### Dependencies
- `PortVisualConfigurationSO` - Effect configuration
- `EnvironmentLODManager` - LOD coordination
- `Light2D` (URP) - Harbor lighting
- `Physics2D` - Ship detection
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Time of Day Cycle
- `timeOfDay`: 0 = midnight, 0.5 = noon, 1 = midnight
- Configurable via `visualConfig.timeOfDaySpeed`
- Affects lighting intensity and color

### Proximity Activation
- Effects only active when player/ships nearby
- Reduces overhead for distant harbors
- Smooth audio fade in/out

### URP 2D Compatibility
- Uses Light2D components
- Particle systems configured for 2D
- Z-depth handled appropriately
