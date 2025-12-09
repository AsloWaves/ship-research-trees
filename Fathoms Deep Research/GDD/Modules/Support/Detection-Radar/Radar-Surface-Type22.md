---
module_id: RAD-003
name: Type 22 Surface Search Radar
category: support
subcategory: detection-radar
function: surface_search
era: 1942
nation: Japan
slot_type: support

# Coverage Mechanics
scan_type: sector
cone_angle: 120          # degrees
rotation_speed: 4        # seconds per sector sweep
sector_options: [60, 90, 120]
modes: [auto, manual, sector]
default_mode: sector

# Performance
detection_range: 18      # km
accuracy: 80             # % bearing accuracy
resolution: 600          # meters (distinguish close contacts)
update_rate: 4           # seconds between detections
height_finding: false

# Physical
weight: 3800
power_draw: 38
crew_required: 2
reliability: 65

# Limitations
min_range: 700           # meters
weather_penalty: 18      # % range loss
sea_clutter: high

tags: [radar, surface_search, japan, wwii, 1942, limited]
---

# Type 22 Surface Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 22 (二号二型電波探信儀) |
| **Nation** | Imperial Japanese Navy |
| **Era** | 1942+ |
| **Function** | Surface Search |
| **Scan Type** | Sector Scan 120° |

## Coverage Pattern
```
Scan Type:        Sector Scan
Cone Angle:       120° (adjustable arc)
Rotation Speed:   4 seconds per sector sweep
Coverage:         Limited arc - must be aimed
Update Rate:      Contact position updates every 4 seconds (within sector)
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE          120° Sector Example:
     \  |  /                  ___---___
      \ | /               _--    N    --_
W -----+-----E          /    NW | NE     \
      / | \            |        |         |
     /  |  \            \    W--+--E     /
   SW   |   SE            --__   |   __--
        |                     ---+---
        S                     BLIND

Sector sweeps back and forth: <=====>
FAST updates within arc, BLIND outside
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 18 km | Must be within scan sector |
| Cruiser | 16 km | Moderate range only |
| Destroyer | 14 km | Reliable if in coverage arc |
| Submarine (surfaced) | 9 km | Difficult in sea clutter |
| MTB/PT Boat | 6 km | Very limited detection |
| Periscope | 2 km | Nearly impossible to detect |

## Operation Modes
### Auto Mode
Antenna sweeps automatically within the selected sector arc. Operator must manually rotate the entire radar mount to change which sector is covered. Not truly "automatic" compared to 360° rotating radars.

### Manual Mode
Operator manually aims the radar at suspected contact bearings. Requires constant attention and good tactical judgment. Missing targets outside the narrow beam is common with inexperienced crews.

### Sector Mode
The default and most practical mode. Operator selects 60°, 90°, or 120° arc width. Narrower arcs provide faster updates (2-3 seconds for 60°) but reduce coverage. Typically pointed at most likely threat axis.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,800 kg |
| Power Draw | 38 kW |
| Crew Required | 2 |
| Reliability | 65% |
| Frequency | 10 cm (S-band) |
| Antenna Type | Sector-scan parabolic |
| Display | Basic PPI scope |

## Advantages
- Lighter than Allied rotating radars
- Lower power consumption
- Fast update rate within scanned sector (4 seconds)
- Compact design fits on smaller vessels
- Less electromagnetic signature than full-rotation sets
- Narrow beam provides good bearing accuracy within arc
- Adequate for forward-focused night actions

## Disadvantages
- **Major limitation**: Only covers 120° arc - large blind spots
- Cannot detect threats from unscanned directions
- Requires operator to correctly predict threat bearing
- Poor resolution (600m) - struggles with close formations
- Limited range (18 km) compared to Allied sets
- High sea clutter in rough weather
- Low reliability (65%) - frequent breakdowns
- 700m minimum range is quite large
- No 360° coverage option
- Vulnerable to flanking attacks

## Historical Notes

The Type 22 represented Japan's attempt to field radar technology despite industrial limitations. Introduced in 1942, it reflected IJN radar development philosophy: smaller, lighter sets that could be produced with limited resources, sacrificing capability for availability.

The Type 22's sector-scan design was partly intentional (to reduce power requirements and complexity) and partly a limitation (Japanese industry struggled to produce reliable rotating mechanisms). In practice, this meant IJN ships often detected only contacts directly ahead or astern, depending on how the radar was aimed.

During the Battle of Empress Augusta Bay (November 1943), Rear Admiral Omori's cruisers equipped with Type 22 radar failed to detect American forces approaching from the flanks, as their radars were focused forward. At the Battle of Cape St. George (November 1943), Japanese destroyers' Type 22 sets were pointed toward Rabaul (their destination), missing the American destroyer squadron stalking them from astern.

Production was limited, with only about 200 Type 22 sets manufactured. By 1944, surviving sets had low serviceability rates due to spare parts shortages. The IJN increasingly relied on optical lookouts - ironically returning to pre-radar tactics even as radar-equipped ships dominated naval warfare.

## Tactical Tips
- **Predict the Threat**: Type 22's effectiveness depends entirely on pointing it the right direction. Study the tactical situation and aim accordingly.
- **Forward Focus**: When advancing or pursuing, keep the sector aimed dead ahead. You'll detect enemies you're heading toward, but be vulnerable to ambush from flanks.
- **Stern Guard**: When retreating or being pursued, aim the sector astern. Accept that you're blind forward - focus on the known threat behind you.
- **Narrow Arc When Certain**: If you KNOW the enemy bearing, switch to 60° arc for 2-second updates. Only do this when you're sure.
- **Combine with Lookouts**: Position optical lookouts to cover your radar blind spots. Type 22 + good lookouts = acceptable awareness.
- **Frequent Reorientation**: In fluid battles, regularly rotate the radar mount to sweep different sectors. Accept 10-15 second gaps when reorienting.
- **Ambush Defense**: When at anchor or stationary, slowly rotate the entire mount every 30 seconds to provide quasi-360° coverage, though with large gaps.
- **Know Your Weakness**: Never assume you're safe because your radar shows nothing. Something could be 5km off your beam and you'd never know.
- **Power Management**: The low power draw means you can keep Type 22 running even on auxiliary power. Better partial coverage than none.
