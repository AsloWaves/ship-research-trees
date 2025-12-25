# Environment Scripts

The Environment folder contains 14 scripts for ocean rendering, wake effects, and visual effects.

## Ocean Chunk System
- **OceanChunkManager.cs** (35KB) - Infinite ocean background using chunk-based tile system with depth-based spawning
- **OceanTileController.cs** (12KB) - Controls individual ocean tiles
- **OceanTileColorBlender.cs** (11KB) - Smooth color blending between neighboring tiles

## Visual Effects
- **ShipWakeController.cs** (20KB) - Ship wake generation system
- **CustomWakeSpawner.cs** (16KB) - Custom wake particle spawner
- **CustomWakeParticle.cs** (11KB) - Individual wake particle behavior
- **SimpleWakeSprite.cs** (3KB) - Simple sprite-based wake effects
- **WaveEffect.cs** (12KB) - Ocean wave visual effects
- **WaveEffectSpawner.cs** (17KB) - Spawns wave effects around ships

## Harbor & Port Systems
- **HarborEffects.cs** (26KB) - Port and harbor visual effects (seagulls, smoke, ambient particles)

## Ocean Rendering & Optimization
- **EnvironmentLODManager.cs** (18KB) - Level-of-detail management for environment objects
- **OceanColorForcer.cs** (4KB) - Forces specific ocean colors
- **OceanCullingDebugger.cs** (13KB) - Debug tool for ocean tile culling
- **OceanDebugQuickSetup.cs** (6KB) - Quick setup utility for ocean debugging

## Key Systems

### Ocean Chunk Management
The OceanChunkManager creates an infinite ocean by spawning/despawning tiles around the camera:
- Depth-based biome system with configurable tile types
- Performance-controlled spawning (configurable tiles per frame)
- Deterministic procedural variation using seeded random
- Runtime culling controls with debug GUI
- Color blending between neighboring tiles
- Support for features (reefs, wrecks, etc.) based on depth

### Wake & Wave Effects
Multiple systems for realistic water interaction:
- Ship wake particles based on speed and turning
- Wave effects that spawn around moving ships
- Custom particle systems for visual variety
- LOD management for distant effects

### Performance
- Chunk-based rendering (only tiles near camera are active)
- Frustum culling for ocean tiles
- LOD system for environment objects
- Configurable update rates and tile limits
