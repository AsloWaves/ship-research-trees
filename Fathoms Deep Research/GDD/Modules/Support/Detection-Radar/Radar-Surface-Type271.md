---
module_id: RAD-001
name: Type 271 Surface Search Radar
category: support
subcategory: detection-radar
function: surface_search
era: 1941
nation: UK
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360           # degrees (360 for full rotation)
rotation_speed: 8        # seconds per full rotation
sector_options: [90, 120, 180]  # if sector scan capable
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 20      # km
accuracy: 85             # % bearing accuracy
resolution: 400          # meters (distinguish close contacts)
update_rate: 8           # seconds between detections
height_finding: false    # can determine altitude?

# Physical
weight: 4200
power_draw: 45
crew_required: 2
reliability: 78

# Limitations
min_range: 500           # meters
weather_penalty: 12      # % range loss
sea_clutter: moderate

tags: [radar, surface_search, uk, wwii, 1941]
---

# Type 271 Surface Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 271 |
| **Nation** | United Kingdom |
| **Era** | 1941+ |
| **Function** | Surface Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   8 seconds per sweep
Coverage:         Complete all-around coverage
Update Rate:      Contact position updates every 8 seconds
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

Sweep: -----> (8 seconds for full rotation)
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 20 km | Clear, reliable detection |
| Cruiser | 18 km | Good return |
| Destroyer | 15 km | Smaller but detectable |
| Submarine (surfaced) | 10 km | Difficult in sea clutter |
| MTB/PT Boat | 8 km | Minimum detection |
| Periscope | 3 km | Only in calm seas |

## Operation Modes
### Auto Mode
Antenna rotates continuously at 8-second intervals. All contacts within range are automatically detected and displayed on the PPI (Plan Position Indicator) scope. No operator input required beyond monitoring.

### Manual Mode
Operator can slow or pause rotation to focus on specific bearings. Useful for tracking suspicious contacts or distinguishing multiple targets in the same general direction. Reduces overall coverage but improves tracking precision.

### Sector Mode
Locks antenna to sweep only a chosen sector (90°, 120°, or 180°). Update rate improves to 3-4 seconds in focused arc. Excellent for pursuit situations or known threat axes, but creates blind spots in uncovered areas.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 4,200 kg |
| Power Draw | 45 kW |
| Crew Required | 2 |
| Reliability | 78% |
| Frequency | 10 cm (S-band) |
| Antenna Type | Rotating parabolic |
| Display | PPI scope |

## Advantages
- First truly effective Royal Navy surface search radar
- Compact centimetric design fits destroyers and escorts
- Good resolution for distinguishing close targets
- Relatively reliable for early-war equipment
- Excellent for night surface actions
- 10cm wavelength reduces weather interference vs earlier metric sets

## Disadvantages
- Moderate range compared to later American sets
- 8-second rotation somewhat slow for fast torpedo craft
- Sea clutter degrades performance in rough weather
- Cannot provide height information for aircraft
- Minimum range blind spot of 500m
- Requires skilled operator interpretation

## Historical Notes

The Type 271 radar revolutionized Royal Navy convoy escort operations from 1941 onward. Its centimetric wavelength (10cm) provided far better resolution than earlier metric radars, allowing escorts to distinguish individual surfaced U-boats from friendly ships at night.

The radar proved decisive at the Second Battle of Sirte in March 1942, where HMS Penelope used her Type 271 to track Italian warships through smoke screens. During the Battle of the Barents Sea (December 1942), the destroyer HMS Onslow's Type 271 enabled effective coordination of British forces despite Arctic darkness and snow squalls.

Type 271 equipped escorts sank their first U-boat in November 1941. By 1943, the combination of Type 271 radar, Leigh Lights, and Hedgehog weapons closed the "Atlantic Gap," turning the tide against the U-boat threat. Over 1,000 Type 271 sets were produced for destroyers, frigates, corvettes, and coastal forces.

## Tactical Tips
- **Night Fighting**: Type 271 excels in darkness. Use auto mode for general awareness, then switch to manual when contacts appear to refine their position before engaging.
- **Convoy Escort**: Position your ship on the threatened flank. The 8-second sweep is adequate for detecting surfaced U-boats attempting night surface attacks.
- **Fast Targets**: Against E-boats or torpedo craft, consider sector mode focused forward. The faster update rate (3-4 sec) better tracks their movements.
- **Multiple Contacts**: If PPI shows contacts merging, use manual mode to pause rotation on that bearing for 15-20 seconds to distinguish individual ships.
- **Weather**: Performance degrades in heavy seas. Close detection range by 2-3 km in rough weather to avoid false contacts from wave returns.
- **Coordination**: Share radar contacts with allied ships via voice radio. One radar-equipped escort can guide the entire convoy.
