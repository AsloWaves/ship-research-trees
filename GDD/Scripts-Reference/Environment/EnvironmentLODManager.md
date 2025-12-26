# EnvironmentLODManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/EnvironmentLODManager.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~498 |
| **Architecture** | Central LOD orchestration for environment |

## Purpose
Manages Level of Detail (LOD) for all environment systems. Coordinates performance optimization across ocean tiles, waves, and ship effects. Supports dynamic LOD adjustment based on frame time performance.

---

## Configuration

### LOD Update
| Setting | Default | Description |
|---------|---------|-------------|
| `lodCamera` | Camera.main | Camera for distance calculation |
| `lodUpdateInterval` | 0.5 | Seconds between LOD updates |

### Distance Thresholds
| Setting | Default | Description |
|---------|---------|-------------|
| `highDetailDistance` | 1500 | High detail render distance |
| `mediumDetailDistance` | 3000 | Medium detail distance |
| `lowDetailDistance` | 5000 | Low detail distance |
| `cullDistance` | 8000 | Complete culling distance |

### Performance Targets
| Setting | Default | Description |
|---------|---------|-------------|
| `targetFrameTime` | 16.6 | Target ms (60 FPS) |
| `enableDynamicLOD` | true | Auto-adjust based on performance |
| `performanceSensitivity` | 0.8 | Adjustment sensitivity |

### System Controls
| Setting | Default | Description |
|---------|---------|-------------|
| `manageOceanTiles` | true | LOD for ocean tiles |
| `manageWaveEffects` | true | LOD for wave effects |
| `manageShipWakes` | true | LOD for ship wakes |

---

## LOD Levels

```csharp
public enum LODLevel
{
    High,       // Full detail, all effects
    Medium,     // Reduced effects, full geometry
    Low,        // Basic effects, simplified geometry
    VeryLow,    // Minimal effects, very basic geometry
    Culled      // Not rendered
}
```

---

## Dynamic LOD Adjustment

```csharp
private void UpdateDynamicLOD()
{
    // Calculate performance pressure
    float performancePressure = averageFrameTime / targetFrameTime;

    // Adjust multiplier based on pressure
    if (performancePressure > 1.2f)  // Performance worse than target
    {
        performanceMultiplier = Mathf.Max(0.5f, performanceMultiplier - Time.deltaTime * performanceSensitivity);
    }
    else if (performancePressure < 0.8f)  // Performance better than target
    {
        performanceMultiplier = Mathf.Min(1.5f, performanceMultiplier + Time.deltaTime * performanceSensitivity * 0.5f);
    }
}
```

---

## LOD Calculation

```csharp
private LODLevel CalculateLODLevel(float distance)
{
    float adjustedHighDistance = highDetailDistance * performanceMultiplier;
    float adjustedMediumDistance = mediumDetailDistance * performanceMultiplier;
    float adjustedLowDistance = lowDetailDistance * performanceMultiplier;

    if (distance <= adjustedHighDistance)
        return LODLevel.High;
    else if (distance <= adjustedMediumDistance)
        return LODLevel.Medium;
    else if (distance <= adjustedLowDistance)
        return LODLevel.Low;
    else if (distance <= cullDistance)
        return LODLevel.VeryLow;
    else
        return LODLevel.Culled;
}
```

---

## System Updates

### Ocean Tiles LOD
```csharp
private void UpdateOceanTilesLOD(Vector3 cameraPosition)
{
    foreach (OceanTileController tile in oceanTileControllers)
    {
        float distance = Vector3.Distance(tile.transform.position, cameraPosition);
        LODLevel tileLOD = CalculateLODLevel(distance);

        // Apply global LOD constraint
        if (currentGlobalLOD < tileLOD)
            tileLOD = currentGlobalLOD;

        ApplyTileLOD(tile, tileLOD, distance);
    }
}
```

### Wave Effects LOD
```csharp
private void UpdateWaveEffectsLOD()
{
    // Calculate wave density multiplier
    float lodMultiplier = currentGlobalLOD switch
    {
        LODLevel.High => 1f,
        LODLevel.Medium => 0.75f,
        LODLevel.Low => 0.5f,
        LODLevel.VeryLow => 0.25f,
        _ => 1f
    };
}
```

---

## Performance Monitoring

```csharp
private void UpdatePerformanceMonitoring()
{
    // Record frame time (rolling 30-frame average)
    float currentFrameTime = Time.unscaledDeltaTime * 1000f;
    frameTimeHistory[frameTimeIndex] = currentFrameTime;
    frameTimeIndex = (frameTimeIndex + 1) % frameTimeHistory.Length;

    // Calculate rolling average
    float total = 0f;
    for (int i = 0; i < frameTimeHistory.Length; i++)
        total += frameTimeHistory[i];
    averageFrameTime = total / frameTimeHistory.Length;
}
```

---

## Public API

### Get Statistics
```csharp
public LODManagerStats GetStats()

public struct LODManagerStats
{
    public LODLevel currentGlobalLOD;
    public float averageFrameTime;
    public float targetFrameTime;
    public float performanceMultiplier;
    public int oceanTileCount;
    public int shipWakeCount;
    public float highDetailDistance;
    public float mediumDetailDistance;
    public float lowDetailDistance;
}
```

### Force Update
```csharp
public void ForceUpdateLOD()  // Immediate LOD recalculation
```

### Manual LOD Control
```csharp
public void SetManualLOD(LODLevel lodLevel)  // Disable dynamic, set fixed
public void EnableDynamicLOD()               // Re-enable dynamic adjustment
```

---

## Usage Example

```csharp
// LOD manager is singleton-like
EnvironmentLODManager lodManager = FindFirstObjectByType<EnvironmentLODManager>();

// Get current state
var stats = lodManager.GetStats();
Debug.Log($"LOD: {stats.currentGlobalLOD}, FPS: {1000f/stats.averageFrameTime:F0}");

// Force quality mode
lodManager.SetManualLOD(LODLevel.High);

// Return to dynamic
lodManager.EnableDynamicLOD();
```

---

## Integration Points

### Dependencies
- `OceanChunkManager` - Ocean tile management
- `WaveEffectSpawner` - Wave effect system
- `ShipWakeController` - Ship wake effects
- `OceanTileController` - Individual tiles
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Dynamic Performance Adjustment
- 30-frame rolling average for stable readings
- Asymmetric adjustment (faster to reduce, slower to increase)
- Performance multiplier scales all distance thresholds

### Global LOD Constraint
- Individual system LOD cannot exceed global LOD
- Ensures consistent quality across all systems
- Prevents visual inconsistencies

### Target Frame Time
- Default 16.6ms (60 FPS)
- Configurable for different platforms
- Performance pressure > 1.0 = below target
