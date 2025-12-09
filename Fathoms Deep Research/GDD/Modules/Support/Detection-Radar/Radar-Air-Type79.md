---
module_id: RAD-005
name: Type 79 Air Search Radar
category: support
subcategory: detection-radar
function: air_search
era: 1940
nation: UK
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360          # degrees (360 for full rotation)
rotation_speed: 12       # seconds per full rotation
sector_options: [90, 120, 180]
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 80      # km (for aircraft)
accuracy: 75             # % bearing accuracy
resolution: 2000         # meters (distinguish close contacts)
update_rate: 12          # seconds between detections
height_finding: false

# Physical
weight: 6800
power_draw: 65
crew_required: 3
reliability: 68

# Limitations
min_range: 2000          # meters
weather_penalty: 20      # % range loss
sea_clutter: high

tags: [radar, air_search, uk, wwii, 1940, early]
---

# Type 79 Air Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 79 |
| **Nation** | United Kingdom |
| **Era** | 1940+ |
| **Function** | Air Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   12 seconds per sweep
Coverage:         Complete hemispheric air coverage
Update Rate:      Aircraft position updates every 12 seconds
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  (Antenna rotates continuously)
      / | \     (Vertical polarization for aircraft)
     /  |  \
   SW   |   SE
        |
        S

Sweep: -----> (12 seconds for full rotation)
Designed primarily for detecting aircraft
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Heavy Bomber (high) | 80 km | Maximum range at altitude |
| Medium Bomber | 65 km | Reliable detection |
| Fighter (high) | 50 km | Smaller radar cross-section |
| Torpedo Bomber (low) | 30 km | Reduced due to low altitude |
| Dive Bomber | 40 km | Variable by altitude |
| Battleship (surface) | 15 km | Poor surface performance |
| Cruiser (surface) | 12 km | Surface search not primary role |

## Operation Modes
### Auto Mode
Antenna rotates continuously at 12-second intervals, providing all-around air coverage. The relatively slow rotation means fast aircraft may move several kilometers between updates. Operators must mentally extrapolate aircraft tracks.

### Manual Mode
Operator can pause rotation to focus on specific bearings where large formations are detected. Useful for counting aircraft in a raid or distinguishing multiple groups approaching simultaneously.

### Sector Mode
Locks antenna to sweep a specific arc (90°, 120°, or 180°). Update rate improves to 5-6 seconds in the focused sector. Recommended when CAP (Combat Air Patrol) is airborne - focus on the sector they're defending.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 6,800 kg |
| Power Draw | 65 kW |
| Crew Required | 3 |
| Reliability | 68% |
| Frequency | 7.5 m (HF) |
| Antenna Type | Fixed dipole array (rotating platform) |
| Display | A-scope display |

## Advantages
- First operational naval air search radar in the world
- Excellent range against high-altitude aircraft (80 km)
- 360° coverage provides early warning from all directions
- Can detect incoming strikes with enough time to scramble CAP
- Revolutionized fleet air defense in 1940
- Provides fighter direction capability
- Historic significance - won the Battle of Britain at sea

## Disadvantages
- Very early technology - metric wavelength limits accuracy
- Poor resolution (2000m) - cannot distinguish individual aircraft
- Slow 12-second rotation means large gaps in tracking
- No height-finding capability - altitude unknown
- Poor surface search performance (not designed for it)
- Large, heavy antenna system
- Low reliability (68%) by later-war standards
- High power consumption
- Requires three crew members to operate effectively
- Weather significantly degrades performance

## Historical Notes

Type 79 was the world's first operational naval air warning radar, entering service in 1938-1939 aboard Royal Navy capital ships. Its deployment gave the RN a revolutionary capability: detecting incoming air raids long before visual contact, allowing time to prepare anti-aircraft defenses and scramble fighter cover.

During the Norwegian Campaign (April 1940), HMS Sheffield's Type 79 detected German aircraft at ranges that amazed Allied observers, providing crucial early warning. At the Battle of Calabria (July 1940), HMS Warspite's Type 79 detected Italian reconnaissance aircraft, alerting the fleet to impending action.

The Type 79's most famous contribution was during Mediterranean convoy operations. In 1940-1941, radar-equipped carriers like HMS Illustrious could detect incoming Italian bomber raids at 70-80 km range, vectoring Fulmar fighters to intercept. Without Type 79, Malta convoys would have suffered even heavier losses.

The radar's limitations became apparent as the war progressed. The metric wavelength (7.5m) provided poor accuracy - operators could detect a large raid but couldn't determine if it was 20 or 50 aircraft. Height-finding was impossible, forcing visual observation once aircraft closed. By 1942, Type 79 was being replaced by the superior centimetric Type 281, but it remained in service on older vessels and auxiliaries through 1943.

Over 200 Type 79 sets were installed on battleships, carriers, cruisers, and armed merchant cruisers. It represented Britain's early lead in naval radar technology, a lead that proved decisive in the critical 1940-1941 period.

## Tactical Tips
- **Early Warning**: Type 79's 80 km detection range provides 6-8 minutes warning before bombers arrive. Use this time to increase speed, turn into wind, and man all AA stations.
- **Fighter Direction**: Vector your CAP fighters using Type 79 bearings. The range is accurate, but bearing accuracy is only 75% - tell pilots to search ±10° from given bearing.
- **Raid Estimation**: Multiple blips on the A-scope mean multiple aircraft, but counting is difficult. Assume "large raid" if you see 5+ distinct returns.
- **Low-Level Threats**: Type 79 struggles with torpedo bombers at wave-top height (30 km max). Don't trust it for low-level defense - keep visual lookouts alert.
- **Sector Focus**: If defending a convoy, use sector mode focused upwind. Most attacks develop from upwind to enable torpedo runs into wind.
- **Reliability Management**: The 68% reliability means frequent breakdowns. Have backup plans for air defense without radar. Run diagnostics every 4 hours.
- **Combine with Type 271**: If your ship has both Type 79 (air) and Type 271 (surface), station operators to monitor both. The combination provides comprehensive situational awareness.
- **Weather Compensation**: In storms, reduce effective range by 20%. Heavy rain creates clutter that masks aircraft returns.
- **Formation Coordination**: The carrier should have Type 79. Escorts can manage with surface search radar - let the carrier do fighter direction.
- **Historical Roleplaying**: If playing a 1940-1941 scenario, Type 79 gives you a significant advantage over Axis forces without comparable equipment. Use it aggressively.
