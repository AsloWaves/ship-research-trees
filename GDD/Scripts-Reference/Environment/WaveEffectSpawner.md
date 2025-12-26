# WaveEffectSpawner.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/WaveEffectSpawner.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~513 |
| **Architecture** | Wave effect spawning with object pooling |

## Purpose
Spawns and manages ambient wave effects across the ocean surface. Creates scattered wave crests, foam patterns, and surface details for ocean atmosphere. Uses object pooling for performance.

---

## Configuration

### Wave Prefabs
| Setting | Description |
|---------|-------------|
| `waveCrestPrefab` | Prefab for wave crest effects |
| `foamPatchPrefab` | Prefab for foam patch effects |
| `ripplePrefab` | Prefab for ripple effects |

### Spawning Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `spawnRadius` | 1000 | Radius around camera for spawning |
| `waveDensity` | 8 | Waves per 1000 square units |
| `minWaveSpacing` | 50 | Minimum distance between waves |
| `despawnDistance` | 1500 | Distance for despawning |

### Wave Type Probabilities
| Setting | Default | Description |
|---------|---------|-------------|
| `crestProbability` | 0.6 | Chance of crest wave |
| `foamProbability` | 0.3 | Chance of foam patch |
| `rippleProbability` | 0.1 | Chance of ripple |

### Wave Animation
| Setting | Default | Description |
|---------|---------|-------------|
| `waveAnimationSpeed` | 0.8 | Base animation speed |
| `speedVariation` | 0.2 | Random speed variation |
| `waveLifetime` | 15 | Seconds before expiration |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `maxActiveWaves` | 200 | Maximum active waves |
| `wavesPerFrame` | 3 | Spawn/despawn per frame |
| `updateInterval` | 0.5 | Seconds between spawn checks |

### Wind Effects
| Setting | Default | Description |
|---------|---------|-------------|
| `windDirection` | (1, 0.5) | Wind direction vector |
| `windStrength` | 0.5 | Wind strength |
| `enableWindVariation` | true | Dynamic wind changes |

---

## Object Pooling

```csharp
private void PopulateWavePool()
{
    int poolSize = Mathf.Min(maxActiveWaves, 100);

    for (int i = 0; i < poolSize; i++)
    {
        WaveEffect wave = CreateWaveObject();
        if (wave != null)
        {
            wave.gameObject.SetActive(false);
            wavePool.Enqueue(wave);
        }
    }
}

private WaveEffect GetPooledWave()
{
    if (wavePool.Count > 0)
        return wavePool.Dequeue();

    return CreateWaveObject();  // Create new if pool empty
}

private void DespawnWave(WaveEffect wave)
{
    wave.Reset();
    wave.gameObject.SetActive(false);
    wavePool.Enqueue(wave);
}
```

---

## Spawning Logic

```csharp
private void SpawnWavesAroundCamera(Vector3 cameraPosition)
{
    int wavesToSpawn = Mathf.Min(
        wavesPerFrame - wavesSpawnedThisFrame,
        maxActiveWaves - activeWaves.Count
    );

    for (int i = 0; i < wavesToSpawn; i++)
    {
        Vector3 spawnPos = GenerateRandomSpawnPosition(cameraPosition);

        if (IsValidSpawnPosition(spawnPos))  // Check min spacing
        {
            SpawnWaveAt(spawnPos);
            wavesSpawnedThisFrame++;
        }
    }
}

private void SpawnWaveAt(Vector3 position)
{
    WaveEffect wave = GetPooledWave();
    if (wave == null) return;

    wave.transform.position = position;
    wave.transform.rotation = Quaternion.Euler(0f, 0f, randomGenerator.NextFloat() * 360f);
    wave.gameObject.SetActive(true);

    float animSpeed = waveAnimationSpeed * (1f + randomGenerator.NextFloat(-speedVariation, speedVariation));
    wave.Initialize(animSpeed, waveLifetime);

    activeWaves.Add(wave);
}
```

---

## Wave Type Selection

```csharp
private GameObject ChooseWavePrefab()
{
    float random = randomGenerator.NextFloat();

    if (random <= crestProbability && waveCrestPrefab != null)
        return waveCrestPrefab;
    else if (random <= crestProbability + foamProbability && foamPatchPrefab != null)
        return foamPatchPrefab;
    else if (ripplePrefab != null)
        return ripplePrefab;

    // Fallback
    return waveCrestPrefab ?? foamPatchPrefab ?? ripplePrefab;
}
```

---

## Position Generation (2D)

```csharp
private Vector3 GenerateRandomSpawnPosition(Vector3 center)
{
    float angle = randomGenerator.NextFloat() * 2f * math.PI;
    float distance = randomGenerator.NextFloat(spawnRadius * 0.3f, spawnRadius);

    Vector3 offset = new Vector3(
        math.cos(angle) * distance,
        math.sin(angle) * distance,  // 2D uses Y axis
        0.5f  // Z depth behind ship, in front of ocean
    );

    return center + offset;
}
```

---

## Update Loop

```csharp
private void Update()
{
    wavesSpawnedThisFrame = 0;
    wavesDespawnedThisFrame = 0;

    UpdateActiveWaves();  // Update all waves, despawn expired

    if (Time.time - lastUpdateTime >= updateInterval)
    {
        UpdateWaveSpawning();  // Spawn new waves if needed
        lastUpdateTime = Time.time;
    }

    if (enableWindVariation)
        UpdateWindEffects();
}

private void UpdateActiveWaves()
{
    for (int i = activeWaves.Count - 1; i >= 0; i--)
    {
        WaveEffect wave = activeWaves[i];
        wave.UpdateWave(Time.deltaTime, windDirection * windStrength);

        // Despawn conditions
        float distance = Vector3.Distance(wave.transform.position, cameraTransform.position);
        bool shouldDespawn = distance > despawnDistance ||
                            wave.GetAge() > waveLifetime ||
                            wavesDespawnedThisFrame >= wavesPerFrame;

        if (shouldDespawn)
        {
            DespawnWave(wave);
            activeWaves.RemoveAt(i);
            wavesDespawnedThisFrame++;
        }
    }
}
```

---

## Public API

### Get Statistics
```csharp
public WaveSpawnerStats GetStats()

public struct WaveSpawnerStats
{
    public int activeWaveCount;
    public int pooledWaveCount;
    public int targetWaveCount;
    public float spawnRadius;
    public Vector2 windDirection;
    public float windStrength;
}
```

### Force Respawn
```csharp
public void RespawnAllWaves()  // Clear all and respawn fresh
```

---

## Usage Example

```csharp
// Spawner auto-manages waves around camera
WaveEffectSpawner spawner = FindFirstObjectByType<WaveEffectSpawner>();

// Get stats for debugging
var stats = spawner.GetStats();
Debug.Log($"Waves: {stats.activeWaveCount}/{stats.targetWaveCount}");

// Force respawn (scene change, etc.)
spawner.RespawnAllWaves();
```

---

## Integration Points

### Dependencies
- `WaveEffect` - Individual wave components
- `EnvironmentLODManager` - LOD coordination
- `Unity.Mathematics.Random` - Deterministic random
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Density Calculation
```csharp
int targetCount = Mathf.RoundToInt((spawnArea / 1000000f) * waveDensity);
```

### Frame Budget
- Max `wavesPerFrame` spawned/despawned per frame
- Prevents frame spikes from mass operations

### Minimum Spacing
- Prevents wave clustering
- O(n) check against existing waves
- Reduces visual overlap

### Wind Variation
- Subtle direction rotation over time
- Creates natural wind movement feel
