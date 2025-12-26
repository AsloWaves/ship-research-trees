# OceanTileColorBlender.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Environment/OceanTileColorBlender.cs` |
| **Namespace** | `WOS.Environment` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | ~337 |
| **Architecture** | Neighbor-based color blending with caching |

## Purpose
Handles smooth color blending between ocean tiles based on neighboring tile depths. Creates natural color gradients across the ocean surface by averaging colors with nearby tiles using distance-weighted blending.

---

## Configuration

### Blending Configuration
| Setting | Default | Description |
|---------|---------|-------------|
| `enableBlending` | true | Enable color blending |
| `blendRadius` | 80 | Radius to search for neighbors |
| `blendStrength` | 0.3 | Blend strength (0-1) |
| `useDistanceWeighting` | true | Weight by distance |
| `blendUpdateInterval` | 0.5 | Update frequency in seconds |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `maxNeighbors` | 8 | Maximum neighbors to blend |
| `smoothTransition` | true | Smooth color transitions |
| `transitionSpeed` | 2 | Color transition speed |

### Debug
| Setting | Description |
|---------|-------------|
| `showDebugInfo` | Log blending information |
| `visualizeNeighbors` | Draw gizmo lines to neighbors |

---

## Neighbor Finding

### Cache-Based Search (Fast)
```csharp
private void FindNeighborsFromCache()
{
    Vector3 myPosition = transform.position;

    // Check tiles in a grid pattern around us
    int searchRadius = Mathf.CeilToInt(blendRadius / 64f); // Assuming tile size of 64

    for (int x = -searchRadius; x <= searchRadius; x++)
    {
        for (int y = -searchRadius; y <= searchRadius; y++)
        {
            if (x == 0 && y == 0) continue; // Skip self

            Vector2Int neighborCoord = myChunkCoord + new Vector2Int(x, y);

            if (tileCache.TryGetValue(neighborCoord, out OceanTileController neighbor))
            {
                if (neighbor != null && neighbor != tileController)
                {
                    float distance = Vector3.Distance(myPosition, neighbor.transform.position);
                    if (distance <= blendRadius)
                    {
                        neighborTiles.Add(neighbor);
                        if (neighborTiles.Count >= maxNeighbors) return;
                    }
                }
            }
        }
    }
}
```

### Physics-Based Search (Fallback)
```csharp
private void FindNeighborsWithPhysics()
{
    // Use physics overlap to find nearby tiles
    Collider2D[] nearbyColliders = Physics2D.OverlapCircleAll(transform.position, blendRadius);

    foreach (var collider in nearbyColliders)
    {
        if (collider.gameObject == gameObject) continue;

        var neighborTile = collider.GetComponent<OceanTileController>();
        if (neighborTile != null)
        {
            neighborTiles.Add(neighborTile);
            if (neighborTiles.Count >= maxNeighbors) break;
        }
    }
}
```

---

## Color Blending

```csharp
private Color CalculateBlendedColor()
{
    if (neighborTiles.Count == 0) return originalColor;

    Color totalColor = originalColor;
    float totalWeight = 1f;
    Vector3 myPosition = transform.position;

    foreach (var neighbor in neighborTiles)
    {
        if (neighbor == null) continue;

        var neighborRenderer = neighbor.GetComponent<SpriteRenderer>();
        if (neighborRenderer == null) continue;

        Color neighborColor = neighborRenderer.color;

        if (useDistanceWeighting)
        {
            // Weight by inverse distance
            float distance = Vector3.Distance(myPosition, neighbor.transform.position);
            float weight = 1f - (distance / blendRadius);
            weight = Mathf.Max(0f, weight);

            totalColor += neighborColor * weight;
            totalWeight += weight;
        }
        else
        {
            // Simple average
            totalColor += neighborColor;
            totalWeight += 1f;
        }
    }

    // Average the colors
    if (totalWeight > 0f)
        totalColor /= totalWeight;

    // Preserve alpha
    totalColor.a = originalColor.a;

    return totalColor;
}
```

---

## Update Loop

```csharp
private void Update()
{
    if (!enableBlending || spriteRenderer == null) return;

    // Update blend calculation periodically
    if (Time.time - lastBlendUpdate > blendUpdateInterval)
    {
        UpdateColorBlend();
        lastBlendUpdate = Time.time;
    }

    // Smooth transition to target color
    if (smoothTransition && currentColor != targetBlendedColor)
    {
        currentColor = Color.Lerp(currentColor, targetBlendedColor, Time.deltaTime * transitionSpeed);
        spriteRenderer.color = currentColor;
    }
    else if (!smoothTransition)
    {
        spriteRenderer.color = targetBlendedColor;
    }
}
```

---

## Static Tile Cache

```csharp
// Cache for fast neighbor lookups
private static Dictionary<Vector2Int, OceanTileController> tileCache =
    new Dictionary<Vector2Int, OceanTileController>();

private void Start()
{
    // Register in cache
    if (!tileCache.ContainsKey(myChunkCoord))
        tileCache[myChunkCoord] = tileController;
}

private void OnDestroy()
{
    // Remove from cache
    if (tileCache.ContainsKey(myChunkCoord))
        tileCache.Remove(myChunkCoord);
}

/// Clear the tile cache (call when rebuilding ocean)
public static void ClearTileCache()
{
    tileCache.Clear();
}
```

---

## Public API

### Color Control
```csharp
public void ForceUpdate()                    // Force immediate color update
public void SetOriginalColor(Color color)    // Set base color before blending
```

### Cache Management
```csharp
public static void ClearTileCache()          // Clear when rebuilding ocean
```

---

## Usage Example

```csharp
// Blending happens automatically when tiles are created
// Each tile blends with neighbors within radius

// Force update after depth zone change
OceanTileColorBlender blender = tile.GetComponent<OceanTileColorBlender>();
blender.SetOriginalColor(newDepthColor);
blender.ForceUpdate();

// Clear cache when rebuilding ocean
OceanTileColorBlender.ClearTileCache();
```

---

## Integration Points

### Dependencies
- `OceanTileController` - Chunk coordinates, visibility
- `OceanChunkManager` - Ocean system reference
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### Blending Algorithm
- **Original weight**: 1.0 (always included)
- **Neighbor weight**: Inverse distance ratio (0-1)
- **Final blend**: (original + weighted neighbors) / total weight
- **Blend strength**: Lerp between original and blended result

### Caching Strategy
- Static dictionary of all tiles by chunk coordinate
- O(1) lookup for neighbors
- Falls back to Physics2D if cache empty
- Cache cleared on ocean rebuild

### Performance Optimizations
- Update interval (0.5s default) reduces calculations
- Max neighbors cap prevents expensive searches
- Smooth transition uses deltaTime for consistent speed
- Grid-based search pattern instead of full scan

### Color Transitions
- Smooth mode: Lerp over time (natural appearance)
- Instant mode: Direct assignment (faster)
- Alpha preserved from original color
