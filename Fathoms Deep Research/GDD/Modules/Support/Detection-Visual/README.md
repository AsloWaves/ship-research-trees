# Visual Detection Modules

Optical and visual detection systems for naval vessels, from basic lookouts to sophisticated rangefinders and searchlights.

## Module Categories

### Lookout Stations
Basic visual observation systems using human lookouts.

| Module ID | Name | Era | Detection Range | Coverage | Notes |
|-----------|------|-----|-----------------|----------|-------|
| VIS-001 | Basic Lookout Station | 1890+ | 8 km | 360° | Naked eye observation |
| VIS-002 | Binocular Lookout Station | 1900+ | 15 km | 360° | 7x50 naval binoculars |
| VIS-003 | Crow's Nest Lookout | 1890+ | 18 km | 360° | Elevated position (+20% range) |
| VIS-004 | Director Tower Lookout | 1920+ | 20 km | 360° | Armored, integrated with fire control |

### Optical Rangefinders
Precision optical instruments for measuring range to targets.

| Module ID | Name | Era | Ranging Range | Accuracy | Baseline | Typical Use |
|-----------|------|-----|---------------|----------|----------|-------------|
| VIS-005 | 1m Optical Rangefinder | 1900+ | 8 km | ±150m | 1m | Destroyers |
| VIS-006 | 3m Optical Rangefinder | 1910+ | 15 km | ±100m | 3m | Cruisers |
| VIS-007 | 9m Optical Rangefinder | 1915+ | 25 km | ±60m | 9m | Battleships |
| VIS-008 | 15m Optical Rangefinder | 1930+ | 35 km | ±40m | 15m | Super-battleships (Yamato) |

### Searchlights
Night illumination systems for visual detection and gunnery.

| Module ID | Name | Era | Illumination Range | Beam Width | Power Draw | Notes |
|-----------|------|-----|-------------------|------------|------------|-------|
| VIS-009 | 36-inch Searchlight | 1900+ | 5 km | 30° | 12 kW | Standard naval searchlight |
| VIS-010 | 60-inch Searchlight | 1920+ | 8 km | 25° | 30 kW | Heavy searchlight, capital ships |

## Design Philosophy

Visual detection systems form the foundation of naval awareness from antiquity through the radar era. Even with radar, visual systems remained essential for:

- **Positive identification** of friend or foe
- **Periscope detection** (submarines)
- **Small craft spotting** (torpedo boats, mines)
- **Backup systems** when radar fails
- **Survivor recovery** operations

### Progression Path

1. **Early Era (1890-1910)**: Basic lookouts and small rangefinders
2. **Dreadnought Era (1910-1920)**: Binocular lookouts, medium rangefinders (3-5m)
3. **Interwar (1920-1935)**: Director towers, long-baseline rangefinders (9m)
4. **Late Battleship (1935-1945)**: Peak optical technology (15m rangefinders)
5. **Transition (1940-1960)**: Radar supplements then replaces optical systems

### Game Mechanics

#### Detection Range
- Affected by weather, time of day, target size, and sea state
- Lookouts provide 360° continuous coverage
- Rangefinders provide narrow, directed coverage

#### Rangefinding Accuracy
- Baseline length directly affects accuracy
- Longer baseline = better accuracy at long range
- Required for accurate gunnery in pre-radar era

#### Night Combat
- Visual detection severely limited at night
- Searchlights enable night gunnery BUT reveal position
- Risk/reward decision: illuminate or stay dark?

#### Weather Effects
- Rain and fog severely degrade optical systems
- Storm conditions reduce effectiveness by 35-40%
- Searchlights scatter in precipitation

## Compatibility

### Lookout Stations
- Compatible with all bridge types
- No power requirements
- Can stack multiple stations (diminishing returns)
- Work with all rangefinders and fire control systems

### Optical Rangefinders
- Require clear line of sight
- Integrate with mechanical fire control computers
- Backup to radar fire control
- Cannot range through smoke

### Searchlights
- Require electrical power system
- Risk tactical exposure when used
- Useful for night surface combat (pre-radar)
- AA illumination role

## Historical Context

Visual detection dominated naval warfare for millennia. Even in WWII, lookouts remained critical:

- **Japanese Lookouts**: Legendary for keen eyesight and endurance
- **Optical Quality**: German Zeiss and Japanese Nikko optics were world-class
- **Battleship Rangefinders**: Grew from 1m (1900) to 15m (Yamato, 1941)
- **Night Fighting**: Searchlights enabled close-range night combat
- **Radar Transition**: By 1943, radar largely replaced optical fire control

### Notable Examples

- **HMS Hood**: 9m rangefinder in director control tower
- **Yamato/Musashi**: Massive 15m rangefinders, finest optical systems ever built
- **USS Enterprise (CV-6)**: Maintained lookout stations throughout WWII despite radar
- **Battle of Guadalcanal**: Searchlight-illuminated night combat at point-blank range

## Obsolescence

Radar fire control (1941+) gradually replaced optical systems:

1. **Early Radar (1941-1943)**: Optical systems still primary
2. **Mid-War (1943-1945)**: Radar primary, optical backup
3. **Post-War (1945-1960)**: Optical systems retained for backup only
4. **Modern Era (1960+)**: Visual systems limited to identification/navigation

However, lookouts remained standard until the 1960s for tasks radar couldn't handle.

## Additional Files

Legacy files (original format):
- `Lookout-Station.md` - General lookout station concept (SUP-001)
- `Optical-Rangefinder.md` - General rangefinder concept (SUP-003)

## Module File Format

Each module file includes:
- **YAML frontmatter**: Technical specifications
- **Overview table**: Quick reference
- **Description**: Module purpose and function
- **Performance tables**: Detection/ranging capabilities by condition
- **Fog of War effects**: How this affects player visibility
- **Advantages/Disadvantages**: Gameplay trade-offs
- **Historical notes**: Real-world context and examples

## Related Systems

- **Fire Control Modules**: Rangefinder data feeds fire control computers
- **Bridge Modules**: Required mounting location for most optical systems
- **Power Systems**: Searchlights require electrical power
- **Radar Modules**: Eventually supplement/replace optical detection
- **Electronic Warfare**: Not applicable to optical systems (no emissions)
