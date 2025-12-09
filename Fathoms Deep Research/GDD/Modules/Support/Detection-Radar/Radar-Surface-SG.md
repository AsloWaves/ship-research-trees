---
module_id: RAD-002
name: SG Surface Search Radar
category: support
subcategory: detection-radar
function: surface_search
era: 1942
nation: USA
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360           # degrees (360 for full rotation)
rotation_speed: 6        # seconds per full rotation
sector_options: [90, 120, 180]
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 35      # km
accuracy: 92             # % bearing accuracy
resolution: 300          # meters (distinguish close contacts)
update_rate: 6           # seconds between detections
height_finding: false

# Physical
weight: 5100
power_draw: 55
crew_required: 2
reliability: 88

# Limitations
min_range: 400           # meters
weather_penalty: 8       # % range loss
sea_clutter: low

tags: [radar, surface_search, usa, wwii, 1942, excellent]
---

# SG Surface Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | SG (Signal-George) |
| **Nation** | United States |
| **Era** | 1942+ |
| **Function** | Surface Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   6 seconds per sweep
Coverage:         Complete all-around coverage
Update Rate:      Contact position updates every 6 seconds
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  (Antenna rotates continuously)
      / | \
     /  |  \
   SW   |   SE
        |
        S

Sweep: =====> (6 seconds for full rotation)
Fast rotation catches quick-moving targets
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 35 km | Excellent long-range detection |
| Cruiser | 32 km | Very clear return |
| Destroyer | 28 km | Reliable tracking |
| Submarine (surfaced) | 18 km | Good even in moderate seas |
| MTB/PT Boat | 12 km | Small craft clearly visible |
| Periscope | 5 km | Detectable in calm conditions |

## Operation Modes
### Auto Mode
Antenna sweeps continuously at 6-second intervals, providing rapid updates on all surface contacts. The fast rotation makes this the default mode for most operations, as it provides excellent situational awareness without manual intervention.

### Manual Mode
Operator can adjust rotation speed or pause on specific bearings for detailed examination. The high-quality PPI display allows operators to distinguish between ships in close formation or identify contacts partially obscured by land returns.

### Sector Mode
Restricts sweep to a chosen arc (90°, 120°, or 180°), improving update rate to 2-3 seconds. Particularly effective for gunnery engagements or tracking fast torpedo boats. The SG's excellent resolution makes sector mode highly precise.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 5,100 kg |
| Power Draw | 55 kW |
| Crew Required | 2 |
| Reliability | 88% |
| Frequency | 10 cm (S-band) |
| Antenna Type | Parabolic reflector |
| Display | High-quality PPI scope |

## Advantages
- Exceptional range (35 km) for a surface search radar
- Fast 6-second rotation tracks even fast torpedo boats
- Superior resolution distinguishes close contacts
- Excellent reliability (88%) - consistently operational
- Low sea clutter compared to metric-wavelength sets
- Clear PPI display easy for operators to interpret
- Can detect periscopes in favorable conditions
- Works effectively in moderate weather

## Disadvantages
- Higher power draw than British equivalents
- Slightly heavier than Type 271
- No height-finding capability for aircraft
- 400m minimum range blind spot
- Can be detected by enemy RWR at maximum range
- Requires two trained operators for optimal use

## Historical Notes

The SG radar became the standard US Navy surface search radar from 1942 through the end of WWII and beyond. Its combination of long range, fast rotation, and excellent reliability made it the benchmark against which all other surface search radars were measured.

During the Naval Battle of Guadalcanal (November 1942), USS Helena's SG radar detected Japanese ships at 27,000 yards in complete darkness, giving Admiral Callaghan crucial early warning. At the Battle of Empress Augusta Bay (November 1943), Rear Admiral Merrill used SG radar to maintain perfect formation control while maneuvering his cruisers in darkness, achieving a decisive victory.

The SG proved particularly valuable in the confined waters of the Solomon Islands, where its ability to distinguish land returns from ship contacts prevented friendly fire incidents. During the Battle of Surigao Strait (October 1944), SG-equipped ships tracked the Japanese Southern Force through the narrow strait, enabling Admiral Oldendorf to position his forces for the last battleship-versus-battleship action in history.

Over 10,000 SG radars were produced, equipping everything from destroyers to battleships. Many remained in service into the 1960s on reserve fleet vessels, testament to the design's effectiveness.

## Tactical Tips
- **Night Surface Actions**: The SG excels here. Trust the 35km range - you'll detect enemies long before visual contact. Use the extra time to position advantageously.
- **Fast Target Tracking**: The 6-second update rate is fast enough to track even Tokyo Express destroyer runs. Keep in auto mode - manual intervention usually unnecessary.
- **Formation Keeping**: Use sector mode focused astern when in formation. The 2-3 second updates help maintain precise station-keeping in darkness.
- **Ambush Setup**: Deploy SG with emissions control (EMCON) off, then go EMCON silent once you've mapped enemy positions. They'll lose you but you remember where they were.
- **Fire Control Integration**: Feed SG bearing/range to your main battery fire control radar. The SG finds them, FC radar locks them, guns sink them.
- **PT Boat Defense**: When escorting at night, the SG's 12 km detection of small craft gives ample warning. Vector CAP or nearby destroyers to intercept.
- **Periscope Hunting**: In ASW operations, use sector mode focused ahead at slow speed. The 5 km periscope detection only works if you're patient and systematic.
