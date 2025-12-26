# OceanTileController.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/OceanTileController.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~442 |
| **Architecture** | Individual ocean tile management |

## Purpose
Controls individual ocean tile behavior, animations, and optimizations. Manages tile-specific effects like gentle wave motion and material properties. Works with OceanChunkManager for chunk-based ocean rendering.

---

## Configuration

### Tile Animation
| Setting | Default | Description |
|---------|---------|-------------|
| `enableWaveAnimation` | true | Enable wave visual animation |
| `waveSpeed` | 0.5 | Wave animation speed multiplier |
| `waveAmplitude` | 0.1 | Wave height amplitude |

### Material Animation
| Setting | Default | Description |
|---------|---------|-------------|
| `animateTexture` | true | Animate texture offset |
| `textureScrollSpeed` | (0.02, 0.01) | Texture scroll speed UV |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `lodDistance` | 3000 | Distance for detail reduction |
| `enableCulling` | true | Enable frustum culling |

---

## Initialization

```csharp
public void Initialize(Vector2Int chunkCoord, float size)
{
    chunkCoordinates = chunkCoord;
    tileSize = size;
    isInitialized = true;

    // Generate deterministic wave phase from chunk position
    uint seed = (uint)(chunkCoord.x * 73856093 ^ chunkCoord.y * 19349663);
    if (seed == 0) seed = 1;  // Unity.Mathematics.Random requires non-zero
    Unity.Mathematics.Random random = new Unity.Mathematics.Random(seed);
    wavePhase = random.NextFloat(0f, 2f * math.PI);

    // Set tile-specific shader properties
    if (propertyBlock != null && tileRenderer != null)
    {
        propertyBlock.SetVector(TilePosition, new Vector4(transform.position.x, transform.position.z, 0, 0));
        tileRenderer.SetPropertyBlock(propertyBlock);
    }
}
```

---

## Visibility and Culling

```csharp
private void UpdatePerformanceState()
{
    // Frustum culling check
    Bounds tileBounds = tileRenderer.bounds;
    Plane[] frustumPlanes = GeometryUtility.CalculateFrustumPlanes(oceanCamera);
    bool inFrustum = GeometryUtility.TestPlanesAABB(frustumPlanes, tileBounds);

    isVisible = inFrustum;

    // Enable/disable renderer
    if (enableCulling && tileRenderer.enabled != isVisible)
    {
        tileRenderer.enabled = isVisible;
    }

    // LOD based on distance
    float distanceToCamera = Vector3.Distance(transform.position, oceanCamera.transform.position);
    isHighDetail = distanceToCamera <= lodDistance;
}
```

---

## Wave Animation

```csharp
private void UpdateWaveAnimation()
{
    if (!isHighDetail) return;

    // Wave animation affects material only - tiles stay stationary
    float time = Time.time * waveSpeed;
    float waveValue = math.sin(time + wavePhase) * waveAmplitude;

    // Apply to material shader properties
    if (propertyBlock != null && tileRenderer != null)
    {
        propertyBlock.SetFloat(WaveOffset, time + wavePhase);
    }

    // DO NOT move tile position - tiles remain stationary like real ocean
}
```

---

## Texture Animation

```csharp
private void UpdateTextureAnimation()
{
    if (propertyBlock == null || tileRenderer == null) return;

    Vector2 textureOffset = textureScrollSpeed * Time.time;

    propertyBlock.SetFloat(WaveOffset, Time.time * waveSpeed + wavePhase);

    if (tileMaterial != null && tileMaterial.HasProperty(MainTexOffset))
    {
        Vector4 tilingOffset = tileMaterial.GetVector(MainTexOffset);
        tilingOffset.z = textureOffset.x % 1f;  // Wrap UV
        tilingOffset.w = textureOffset.y % 1f;
        propertyBlock.SetVector(MainTexOffset, tilingOffset);
    }

    tileRenderer.SetPropertyBlock(propertyBlock);
}
```

---

## Shader Property IDs

```csharp
private static readonly int MainTexOffset = Shader.PropertyToID("_MainTex_ST");
private static readonly int WaveOffset = Shader.PropertyToID("_WaveOffset");
private static readonly int TilePosition = Shader.PropertyToID("_TilePosition");
```

---

## Public API

### Visibility Control
```csharp
public void SetVisibility(bool visible)
public void SetDetailLevel(bool highDetail)
```

### Material Variation
```csharp
public void ApplyMaterialVariation(Material newMaterial)
```

### Performance Info
```csharp
public TilePerformanceInfo GetPerformanceInfo()

public struct TilePerformanceInfo
{
    public Vector2Int chunkCoordinates;
    public bool isVisible;
    public bool isHighDetail;
    public float distanceToCamera;
    public bool isAnimating;
}
```

### Cleanup
```csharp
public void Cleanup()  // Called when tile is pooled/destroyed
```

---

## Usage Example

```csharp
// Tiles are created by OceanChunkManager
OceanTileController tile = Instantiate(tilePrefab);
tile.Initialize(new Vector2Int(5, 3), 100f);

// LOD manager can control visibility
tile.SetDetailLevel(false);  // Low detail mode
tile.SetVisibility(true);    // Keep visible

// Get performance stats
var info = tile.GetPerformanceInfo();
Debug.Log($"Tile {info.chunkCoordinates}: Visible={info.isVisible}");
```

---

## Integration Points

### Dependencies
- `OceanChunkManager` - Parent manager
- `EnvironmentLODManager` - LOD coordination
- `WOS.Debugging.DebugManager` - Logging
- `Unity.Mathematics` - Random generation

### Unity Callbacks
- `OnBecameVisible()` / `OnBecameInvisible()` - Renderer visibility

---

## Design Notes

### Stationary Tiles
- Tiles never move position
- Only visual effects animate (shader properties)
- Position locked to `basePosition`

### Deterministic Randomness
- Wave phase generated from chunk coordinates
- Same coordinates = same wave pattern
- Uses Unity.Mathematics.Random with position-based seed

### MaterialPropertyBlock Usage
- Avoids material instancing
- Per-tile shader properties without allocation
- Better batching performance
