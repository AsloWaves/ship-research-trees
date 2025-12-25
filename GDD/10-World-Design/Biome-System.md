---
tags: [partial, phase2, world-design, biomes]
status: 🚧 PARTIAL
phase: Phase 2
priority: MEDIUM
last-updated: 2025-11-17
---

# Biome System

## Overview
The Biome System expands the existing [[Ocean-Environment]] implementation to create distinct visual and gameplay regions across the game world. While the core chunk-based ocean rendering is already implemented, the Biome System will add zone-specific variations, environmental features, and geographic authenticity. This system integrates with [[Zone-System]] to create unique regional identities for Pacific, Atlantic, Mediterranean, and Arctic theaters.

**Core Philosophy**: Visual variety enhances immersion and reinforces geographic identity, while biome-specific features create tactical opportunities.

## Implementation Status
**Status**: 🚧 PARTIAL
**Phase**: Phase 1 (Core) + Phase 2 (Expansion)
**Current Implementation**: [[Ocean-Environment]] provides foundation
**Remaining Work**: Zone-specific biomes, environmental features, regional variations
**Priority**: MEDIUM - Builds on existing system

---

## Current Implementation Review

### Existing Ocean Environment System
**Status**: ✅ IMPLEMENTED (Phase 1)

**Current Features**:
- ✅ Chunk-based ocean rendering (1024x1024 Unity units per tile)
- ✅ 5 depth-based biomes (Coastal, Shallow, Medium, Deep, Abyssal)
- ✅ Procedural depth generation via Perlin noise
- ✅ Color blending between neighboring tiles
- ✅ Configurable biome properties via ScriptableObject
- ✅ Performance optimization (tile spawning, culling, pooling)

**Integration Points**:
- **Camera System**: Chunks follow camera position
- **Color Gradients**: Smooth transitions between depth zones
- **Biome Configuration**: Artist-controlled via `OceanBiomeConfigurationSO`

**See**: [[Ocean-Environment]] for complete implementation details

---

## Design Specification

### Zone-Specific Biome Expansion

The existing depth-based biome system will be expanded with zone-specific configurations to create regional identity.

#### Pacific Theater Biomes

**Tropical Pacific**
- **Color Palette**: Bright turquoise to deep blue
  - Coastal (0-50m): Turquoise (#40E0D0) → Cyan (#00CED1)
  - Shallow (50-200m): Azure (#007FFF) → Ocean Blue (#0077BE)
  - Medium (200-1000m): Navy Blue (#001F3F) → Deep Blue (#003F7F)
  - Deep (1000-4000m): Midnight Blue (#000A1A) → Dark Navy (#001433)
  - Abyssal (4000m+): Near Black (#000510) → Pure Black (#000000)

- **Visual Characteristics**:
  - Bright, clear water (high visibility)
  - Vibrant color saturation
  - Coral reef hints in shallow coastal areas
  - Tropical sunlight reflection

- **Environmental Features** (Phase 2):
  - Coral reef systems (visual markers in shallow zones)
  - Volcanic seamounts (T3-T4 zones)
  - Atoll formations (T1-T2 zones)
  - Deep ocean trenches (T4 zones)

- **Biome Configuration**:
  - Use existing `OceanBiomeConfigurationSO`
  - Create "Pacific_TropicalBiome.asset"
  - Higher color saturation values
  - Brighter base colors

**North Pacific**
- **Color Palette**: Cooler tones, gray-blue
  - Coastal: Gray-Blue (#6A9FB5) → Steel Blue (#4682B4)
  - Shallow: Ocean Blue (#0077BE) → Deep Gray-Blue (#2C5F7C)
  - Medium: Dark Blue (#003F7F) → Slate Blue (#1A334A)
  - Deep: Very Dark Blue (#00142B) → Near Black (#000A14)
  - Abyssal: Black (#000000)

- **Visual Characteristics**:
  - Cooler color temperature
  - Moderate visibility
  - Rougher water surface (integrate with weather)
  - Fog banks common (weather integration)

- **Environmental Features** (Phase 2):
  - Deep ocean basins
  - Seamount chains
  - Cold water currents (visual effects)

---

#### Atlantic Theater Biomes

**North Atlantic**
- **Color Palette**: Cold gray-blue, stormy
  - Coastal: Gray (#708090) → Storm Blue (#4F7087)
  - Shallow: Gray-Blue (#5A7A94) → Steel Blue (#4682B4)
  - Medium: Dark Gray-Blue (#3A5A6A) → Navy (#1C3A4A)
  - Deep: Very Dark Blue (#001428) → Near Black (#000A14)
  - Abyssal: Black (#000000)

- **Visual Characteristics**:
  - Gray, cold appearance
  - Stormy atmosphere (even in clear weather)
  - Whitecaps and choppy seas (weather integration)
  - Reduced color saturation (harsh environment)

- **Environmental Features** (Phase 2):
  - Iceberg fields (northern regions)
  - Deep ocean basins
  - Underwater canyons (submarine hideouts)
  - Grand Banks (shallow fishing grounds)

**Mid-Atlantic**
- **Color Palette**: Moderate blue
  - Similar to North Atlantic but slightly warmer
  - Moderate saturation
  - Transitional zone between cold north and warm south

**Caribbean/South Atlantic**
- **Color Palette**: Warmer, clearer blue
  - Similar to Pacific tropical but slightly less saturated
  - Clear water, good visibility

---

#### Mediterranean Theater Biomes

**Mediterranean Sea**
- **Color Palette**: Distinctive Mediterranean blue
  - Coastal: Aquamarine (#7FDBFF) → Light Blue (#87CEEB)
  - Shallow: Mediterranean Blue (#0E86D4) → Cerulean (#0492C2)
  - Medium: Deep Blue (#003D7A) → Navy (#002855)
  - Deep: Very Dark Blue (#001428) → Near Black (#000A14)
  - Abyssal: Rare (Mediterranean mostly shallow-medium depth)

- **Visual Characteristics**:
  - Crystal clear water (highest visibility)
  - Bright, warm sunlight
  - Calm surface (most of time)
  - Highest color saturation of all theaters

- **Environmental Features** (Phase 2):
  - Rocky coastlines (visual markers)
  - Island chains (visible on horizon)
  - Shallow continental shelf (widespread)
  - Limited deep ocean (central Mediterranean only)

---

#### Arctic Theater Biomes

**Arctic Ocean**
- **Color Palette**: Cold gray-white, icy
  - Coastal (with ice): White-Gray (#D3D3D3) → Ice Blue (#B0E0E6)
  - Shallow: Gray-Blue (#778899) → Cold Blue (#4682B4)
  - Medium: Dark Gray-Blue (#2F4F4F) → Slate (#1C2833)
  - Deep: Very Dark Blue (#00111F) → Black (#000000)
  - Abyssal: Black (#000000)

- **Visual Characteristics**:
  - Gray, cold atmosphere
  - Ice floes visible (seasonal)
  - Low color saturation (harsh, monochrome feel)
  - Polar lighting (dim, indirect)

- **Environmental Features** (Phase 2):
  - Ice fields (seasonal, movable obstacles)
  - Icebergs (navigation hazards)
  - Pack ice (blocks passages)
  - Open water leads (navigation channels)

**Ice Coverage by Season**:
- **Winter**: 70% ice coverage
- **Spring**: 50% ice coverage (melting)
- **Summer**: 20% ice coverage (minimal)
- **Fall**: 40% ice coverage (refreezing)

---

### Environmental Features (Phase 2)

These features are planned expansions to the biome system, adding visual and tactical elements.

#### Coral Reefs
**Location**: Pacific shallow coastal zones (T1-T2)

**Visual Elements**:
- Coral formations visible through clear water
- Colorful reef structures (procedural placement)
- Fish schools (animated particle effects)

**Gameplay Impact**:
- **Navigation Hazard**: Shallow draft required
- **Visual Landmark**: Natural navigation markers
- **Ambush Point**: Hide near reef formations
- **Resource Spawn**: Rare materials near reefs

**Implementation**:
- Spawn coral prefabs in coastal biome tiles
- Procedural placement based on tile position
- Collision detection (optional: damage if hit)

---

#### Volcanic Seamounts
**Location**: Pacific deep zones (T3-T4)

**Visual Elements**:
- Underwater mountains rising from ocean floor
- Volcanic vents (visual effects)
- Dark rock formations visible in deep water

**Gameplay Impact**:
- **Acoustic Interference**: Disrupts sonar/detection
- **Tactical Cover**: Hide behind seamounts
- **Navigation Challenge**: Avoid shallow peaks
- **Resource Spawn**: Rare materials at volcanic vents

**Implementation**:
- Spawn seamount prefabs in deep ocean tiles
- Randomized height and position
- Sonar interference zones

---

#### Ice Fields and Icebergs
**Location**: Arctic Ocean (seasonal)

**Visual Elements**:
- Floating ice floes (movable)
- Large icebergs (static obstacles)
- Pack ice (impassable barriers)
- Open water leads (navigation channels)

**Gameplay Impact**:
- **Navigation Obstacle**: Requires careful routing
- **Icebreaker Requirement**: Some ships cannot pass ice
- **Visual Concealment**: Hide behind icebergs
- **Collision Damage**: Hitting icebergs damages ship

**Implementation**:
- Spawn ice prefabs in Arctic biome tiles
- Seasonal variation (more ice in winter)
- Ice movement system (slow drift)
- Collision detection and damage

---

#### Underwater Canyons
**Location**: Atlantic deep zones, Pacific trenches

**Visual Elements**:
- Visible depth variations (darker areas)
- Canyon edges marked on map
- Topographic detail (if visible)

**Gameplay Impact**:
- **Submarine Hideout**: Hide in canyon depths
- **Acoustic Advantage**: Sound reflection conceals subs
- **Tactical Approach**: Use canyon for stealth infiltration
- **Navigation Challenge**: Avoid running aground

**Implementation**:
- Depth map texture variations
- Specialized biome tiles for canyon areas
- Sonar display shows topography

---

#### Shallow Banks and Reefs
**Location**: Grand Banks (Atlantic), Saya de Malha (Indian Ocean)

**Visual Elements**:
- Lighter water color (shallow depth)
- Visible seafloor (if clear weather)
- Reef systems (tropical)

**Gameplay Impact**:
- **Submarine Limit**: Too shallow for submarine operations
- **Navigation Hazard**: Large ships risk grounding
- **Resource Spawn**: Rich fishing grounds (NPC merchant vessels)
- **Tactical Choice**: Fast ships can cross, heavy ships cannot

**Implementation**:
- Shallow biome tiles in specific locations
- Depth restrictions for submarines
- Navigation warnings for capital ships

---

### Biome Integration with Other Systems

#### Zone System Integration
**Mechanism**: Each zone tier has recommended biome configurations

**Area-Biome Mapping** (internal design):
- **Core National Waters**: Home nation biomes (e.g., USA ports use Pacific Tropical)
- **Protected Waters**: Regional biomes (e.g., Midway uses North Pacific)
- **Contested Areas**: Transitional biomes (mixed characteristics)
- **Deep Ocean Areas**: Open ocean biomes (deep, featureless)
- **Enemy Core Waters**: Enemy nation biomes (e.g., Tokyo Bay uses Japan biome)

**Dynamic Biome Switching**:
- When camera enters new area, load that area's biome configuration
- Smooth transition over 10-20 seconds
- Blend between biome color palettes

**Example**:
```
Player sails from Pearl Harbor (T0, Tropical Pacific biome)
→ Crosses into open Pacific (T3, North Pacific biome)
→ Ocean colors gradually shift from bright turquoise to gray-blue
→ Transition completes over 15 seconds
```

---

#### Weather System Integration
**Mechanism**: Weather modifies biome appearance

**Weather Effects on Biome Colors**:
- **Clear Skies**: Full biome color saturation (100%)
- **Rain**: Desaturated colors (75% saturation), darker tone
- **Fog**: Gray filter over biome colors (50% saturation)
- **Storm**: Very dark, desaturated (40% saturation), high contrast
- **Snow**: White-gray overlay (Arctic only)

**Implementation**:
- Weather system modifies `colorBlendStrength` in OceanChunkManager
- Post-processing color grading adjusts saturation and hue
- Real-time shader adjustments for weather transitions

**Example**:
```
Mediterranean biome in clear weather: Bright azure blue
→ Storm approaches
→ Colors desaturate and darken
→ Mediterranean now appears gray-blue, stormy
```

---

#### Map Layout Integration
**Mechanism**: Biomes reflect geographic location

**Geographic Biome Distribution**:
- **Pacific Theater**: Tropical Pacific (south), North Pacific (north)
- **Atlantic Theater**: North Atlantic (north), Caribbean (south)
- **Mediterranean Theater**: Mediterranean biome (entire theater)
- **Arctic Theater**: Arctic biome (entire theater)

**Biome Boundaries**:
- Biomes transition smoothly at geographic boundaries
- No hard edges between biomes
- Transition zones (e.g., North Pacific → Tropical Pacific at ~30°N)

**Map Overlay**:
- World map shows biome regions (color-coded)
- Players can see which biome they're in
- Helps with navigation and geographic orientation

---

### Technical Implementation

#### OceanBiomeConfigurationSO Expansion

**Current Configuration** (Phase 1):
```
[Depth Zones] (5 zones)
- minDepth, maxDepth
- tilePrefab
- baseColor, deepColor
```

**Phase 2 Expansion**:
```
[Depth Zones] (unchanged)
- minDepth, maxDepth
- tilePrefab
- baseColor, deepColor

[Regional Characteristics] (NEW)
- biomeID (Pacific_Tropical, Atlantic_North, etc.)
- regionName (display name)
- weatherAffinity (preferred weather types)
- featureSpawnRules (coral reefs, icebergs, etc.)

[Environmental Features] (NEW)
- coralReefPrefabs[]
- seamountPrefabs[]
- icebergPrefabs[]
- featureSpawnDensity (per km²)
- featureSpawnProbability (0-1)

[Seasonal Variations] (NEW)
- winterColorPalette (optional color override)
- summerColorPalette (optional)
- seasonalFeatures (ice coverage, etc.)
```

**Asset Structure**:
```
Biomes/
├── Pacific/
│   ├── Pacific_TropicalBiome.asset
│   ├── Pacific_NorthBiome.asset
├── Atlantic/
│   ├── Atlantic_NorthBiome.asset
│   ├── Atlantic_Caribbean.asset
├── Mediterranean/
│   └── Mediterranean_Biome.asset
└── Arctic/
    └── Arctic_Biome.asset
```

---

#### Zone-Biome Manager (New Component)

**Purpose**: Manages biome transitions based on zone entry

**Component Responsibilities**:
- Detect zone changes (subscribe to zone events)
- Load appropriate biome configuration for zone
- Trigger biome transition in OceanChunkManager
- Handle smooth color palette blending

**Example Code Structure**:
```csharp
public class ZoneBiomeManager : MonoBehaviour
{
    [SerializeField] private OceanChunkManager oceanManager;
    [SerializeField] private ZoneManager zoneManager;

    // Biome configurations per zone
    [SerializeField] private Dictionary<string, OceanBiomeConfigurationSO> zoneBiomes;

    void OnZoneEntered(Zone newZone)
    {
        // Get biome config for this zone
        OceanBiomeConfigurationSO biomeConfig = zoneBiomes[newZone.zoneID];

        // Trigger transition in ocean manager
        oceanManager.TransitionToBiome(biomeConfig, transitionDuration: 15f);
    }

    // Smoothly blend between current and new biome
    void TransitionToBiome(OceanBiomeConfigurationSO newBiome, float duration)
    {
        // Lerp color palettes over time
        // Update chunk colors gradually
        // Swap feature spawn rules
    }
}
```

---

#### Feature Spawning System (Phase 2)

**Purpose**: Procedurally place environmental features in biome tiles

**Feature Spawner**:
```csharp
public class BiomeFeatureSpawner : MonoBehaviour
{
    // Called when tile is spawned
    public void SpawnFeaturesForTile(Transform tile, OceanBiomeConfigurationSO biome)
    {
        // Check biome feature rules
        if (biome.coralReefPrefabs.Length > 0 && Random.value < biome.featureSpawnProbability)
        {
            // Spawn coral reef
            int reefIndex = Random.Range(0, biome.coralReefPrefabs.Length);
            Vector3 spawnPos = tile.position + GetRandomOffset();
            Instantiate(biome.coralReefPrefabs[reefIndex], spawnPos, Quaternion.identity, tile);
        }

        // Repeat for icebergs, seamounts, etc.
    }
}
```

**Feature Types**:
- **Static Features**: Icebergs, seamounts (don't move)
- **Dynamic Features**: Ice floes (slowly drift)
- **Animated Features**: Fish schools, volcanic vents (particle effects)

---

### Visual Design Guidelines

#### Color Palette Coherence
**Guideline**: Each theater has distinct color identity

**Color Relationships**:
- **Pacific**: Bright, saturated blues and greens
- **Atlantic**: Gray, desaturated blues
- **Mediterranean**: Warm, bright blues (highest saturation)
- **Arctic**: Gray-white, cold blues (lowest saturation)

**Design Goal**: Players can identify theater by color alone

---

#### Transition Smoothness
**Guideline**: Biome transitions must be imperceptible

**Transition Requirements**:
- 10-20 second transition duration
- Color lerp using smooth curves (not linear)
- No pop-in or sudden changes
- Audio transitions match visual transitions

---

#### Performance Considerations
**Guideline**: Features must not impact performance

**Performance Requirements**:
- Maximum 5 features per tile (coral, icebergs, etc.)
- LOD system for distant features (reduce poly count)
- Occlusion culling (don't render underwater features if not visible)
- Object pooling for features (reuse objects)

**Target Performance**:
- No FPS drop below 60 FPS with features enabled
- Maximum 2ms frame time increase from feature rendering

---

## Cross-References

### Related Systems
- [[Ocean-Environment]] - Core implementation (already done)
- [[Zone-System]] - Biomes vary by zone tier
- [[Map-Layout]] - Geographic distribution of biomes
- [[Weather-System]] - Weather modifies biome appearance
- [[Navigation-System]] - Features affect navigation

### Related Documents
- [[Combat-System]] - Features affect tactical combat (cover, ambush)
- [[Submarine-Warfare]] - Underwater topography affects submarine gameplay
- [[Resource-Distribution]] - Features mark resource spawn locations

---

## Design Decisions

### Why Build on Existing Ocean Environment?
**Decision**: Expand existing system rather than replace

**Reasoning**:
- Existing system is performant and functional
- No need to reinvent the wheel
- Expansion is less risky than replacement
- Backward compatible with Phase 1 work
- Iterative improvement (Phase 1 → Phase 2)

### Why Zone-Specific Biomes?
**Decision**: Different biomes per zone/theater

**Reasoning**:
- Creates geographic identity (players know where they are)
- Historical authenticity (Pacific looks different from Atlantic)
- Visual variety prevents monotony
- Supports immersion (world feels real)
- Enables regional gameplay identity

### Why Add Environmental Features?
**Decision**: Coral reefs, icebergs, seamounts, etc.

**Reasoning**:
- Adds visual interest (breaks up flat ocean)
- Creates tactical opportunities (cover, ambush)
- Navigation challenges (skill-based gameplay)
- Resource spawn markers (directs player exploration)
- Authenticity (oceans have features, not just flat water)

### Why Smooth Biome Transitions?
**Decision**: 10-20 second gradual transitions

**Reasoning**:
- Prevents jarring pop-in
- Maintains immersion
- Feels natural (real weather/geography changes gradually)
- No performance spikes (gradual transition = gradual load)
- Player-friendly (not disorienting)

---

## Phase 2 Implementation Roadmap

### Priority 1: Zone-Biome Integration
**Goal**: Connect existing ocean system to zone system

**Tasks**:
1. Create theater-specific biome configurations
   - Pacific_TropicalBiome.asset
   - Atlantic_NorthBiome.asset
   - Mediterranean_Biome.asset
   - Arctic_Biome.asset
2. Implement ZoneBiomeManager component
3. Add biome transition system (color palette lerp)
4. Test zone boundary crossing

**Completion Criteria**:
- Biomes change when entering new zones
- Smooth 15-second transitions
- No performance impact

---

### Priority 2: Environmental Features
**Goal**: Add visual variety with procedural features

**Tasks**:
1. Create feature prefabs (coral, icebergs, seamounts)
2. Implement BiomeFeatureSpawner
3. Add feature spawning rules to biome configs
4. Integrate with existing chunk spawning

**Completion Criteria**:
- Features appear in appropriate biomes
- No performance impact
- Features despawn with tiles

---

### Priority 3: Weather Integration
**Goal**: Weather modifies biome appearance

**Tasks**:
1. Weather system modifies biome colors
2. Post-processing for weather effects
3. Smooth weather transitions
4. Shader updates for real-time weather

**Completion Criteria**:
- Storm darkens ocean
- Fog desaturates colors
- Clear weather shows full biome colors

---

### Priority 4: Seasonal Variations
**Goal**: Arctic ice coverage changes by season

**Tasks**:
1. Implement seasonal system (spring/summer/fall/winter)
2. Ice coverage varies by season
3. Biome color palettes adjust seasonally
4. Test seasonal transitions

**Completion Criteria**:
- Arctic has more ice in winter
- Seasonal changes happen gradually
- Color palettes shift with seasons

---

## Testing and Validation

### Test Scenarios

**Zone Transition Test**:
1. Sail from T0 zone (home port) to T3 zone (open ocean)
2. Verify biome changes from coastal to deep ocean
3. Confirm smooth color transition (no pop-in)
4. Check performance (no FPS drop)

**Feature Spawning Test**:
1. Enter zone with coral reef features
2. Verify coral spawns in coastal tiles only
3. Check feature density (not too many, not too few)
4. Confirm features despawn with tiles

**Weather Integration Test**:
1. Sail in clear weather, observe biome colors
2. Trigger storm weather
3. Verify colors darken and desaturate
4. Return to clear weather, colors restore

**Performance Test**:
1. Spawn maximum grid (15x15 tiles)
2. Add maximum features per tile
3. Measure FPS (target: 60+ FPS)
4. Verify no memory leaks over time

---

## Known Limitations

### Phase 1 Limitations (Current)
- **Single Biome Config**: Only one biome active at a time
  - **Fix**: Phase 2 adds zone-biome system
- **No Features**: Flat ocean, no visual variety
  - **Fix**: Phase 2 adds environmental features
- **Static Colors**: Colors don't change with weather
  - **Fix**: Phase 3 weather integration

### Phase 2 Limitations (After Expansion)
- **Basic Features**: Features are visual only, no physics
  - **Future**: Add collision detection and damage
- **Static Ice**: Ice doesn't move
  - **Future**: Add ice drift system
- **No Underwater View**: Features not visible when submerged
  - **Future**: Add underwater camera mode

---

## Future Enhancements

### Post-Phase 2 Additions
- **Underwater Camera**: View ocean from below surface
- **Dynamic Ice Drift**: Ice floes slowly move with currents
- **Animated Features**: Volcanic eruptions, geysers
- **Bioluminescence**: Glowing plankton at night (tropical zones)
- **Wreck Sites**: Permanent shipwreck markers (historical battles)

### Phase 3 Polish
- **Wave Simulation**: Realistic wave motion (shader-based)
- **Wake Effects**: Ships create wakes and foam trails
- **Reflections**: Sky and ship reflections on water
- **Caustics**: Underwater light caustics in shallow water
- **Time of Day**: Ocean color shifts with day/night cycle

---

**Status**: 🚧 Phase 1 complete (Ocean Environment), Phase 2 design ready
**Current**: Ocean chunk system fully functional
**Next Steps**: Implement zone-biome integration, add environmental features
**Dependencies**: Ocean Environment (done), Zone System (in progress)
