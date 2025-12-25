---
module_id: RAD-009
name: Type 284 Fire Control Radar
category: support
subcategory: detection-radar
function: fire_control
era: 1941
nation: UK
slot_type: support

# Coverage Mechanics
scan_type: directional
cone_angle: 20           # degrees
rotation_speed: manual   # manually aimed
sector_options: []
modes: [manual]
default_mode: manual

# Performance
detection_range: 15      # km
accuracy: 95             # % bearing accuracy
resolution: 50           # meters (distinguish close contacts)
update_rate: 1           # seconds between detections (continuous)
height_finding: false

# Physical
weight: 3200
crew_required: 2
reliability: 82

# Limitations
min_range: 200           # meters
weather_penalty: 10      # % range loss
sea_clutter: low

tags: [radar, fire_control, uk, wwii, 1941, gunnery]
---

# Type 284 Fire Control Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 284 |
| **Nation** | United Kingdom |
| **Era** | 1941+ |
| **Function** | Fire Control (Main Battery) |
| **Scan Type** | Directional 20° |

## Coverage Pattern
```
Scan Type:        Directional (manually aimed)
Cone Angle:       20° narrow beam
Rotation Speed:   Manual (follows gunnery director)
Coverage:         Only where operator points it
Update Rate:      Continuous (1-second updates when locked on target)
```

**Visual Pattern:**
```
        N
        |
        |    20° Beam
        |   /---\
        |  /     \
W ------+------------ E
      TARGET

Narrow beam must be aimed at specific target
Provides continuous range/bearing when locked
Like a searchlight - illuminates only what it's pointed at
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 15 km | Maximum range for large targets |
| Cruiser | 14 km | Excellent tracking |
| Destroyer | 12 km | Reliable lock even at range |
| Submarine (surfaced) | 8 km | Difficult but possible |
| MTB/PT Boat | 5 km | Small targets at minimum size |

**Note**: Type 284 is NOT a search radar. It must be cued to a target by other means (visual, search radar, or fire control directors) before it can track.

## Operation Modes
### Manual Mode (Only Mode)
Operator manually aims the narrow 20° beam at the target. The radar is slaved to the main battery director, tracking where the guns are pointed. Once locked onto a target, provides continuous range and bearing data to the fire control computer.

**Operation Sequence**:
1. Surface search radar or visual sighting detects enemy
2. Main battery director trains onto target bearing
3. Type 284 beam illuminates target
4. Radar locks and provides precise range
5. Fire control computer uses radar data for gunnery solution
6. Guns fire with radar-derived accuracy

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,200 kg |
| Crew Required | 2 |
| Reliability | 82% |
| Frequency | 50 cm (UHF) |
| Antenna Type | Directional dish |
| Mounting | Slaved to director |

## Advantages
- Exceptional accuracy (95%) for gunnery solutions
- Precise range measurement to within 50 meters
- Continuous tracking updates every second
- Enables blind firing through smoke, night, or poor visibility
- Far superior to optical rangefinding in reduced visibility
- Relatively reliable (82%) for early-war equipment
- Moderate weight suitable for mounting on directors
- Works in conditions that defeat optical rangefinders
- Can track targets obscured by funnel smoke or battle haze

## Disadvantages
- **Not a search radar** - cannot find targets
- Narrow 20° beam requires accurate initial cueing
- Can only track one target at a time
- Requires operator skill to maintain lock on maneuvering targets
- Limited range (15 km) compared to gun range
- Must be manually aimed - cannot auto-track
- Loses lock if target moves outside narrow beam
- 200m minimum range prevents close-range use

## Historical Notes

Type 284 was the Royal Navy's first effective main battery fire control radar, entering service in 1941. It revolutionized naval gunnery by providing accurate range information regardless of visibility conditions, eliminating the limitations of optical rangefinders in darkness, smoke, or poor weather.

The radar proved decisive at the Second Battle of Sirte (March 1942), where HMS Cleopatra's Type 284 enabled accurate gunnery despite heavy smoke screens deployed by both sides. Italian optical rangefinders were effectively blind, while British radar-directed fire remained accurate.

At the Battle of North Cape (December 1943), HMS Duke of York's Type 284 tracked Scharnhorst through Arctic darkness and snow squalls. The radar maintained continuous range data even when optical sights completely lost the target. Duke of York's devastatingly accurate fire - achieving hits at ranges beyond 10 km in near-zero visibility - was largely due to Type 284's performance.

During the Normandy landings (June 1944), Type 284-equipped cruisers and battleships conducted shore bombardment with unprecedented accuracy. The radar allowed precise ranging on specific buildings and fortifications, even through smoke from fires and artillery.

The Type 284's one-target limitation meant that in multi-ship engagements, gunnery directors had to choose priority targets carefully. Once locked onto a target, switching to a different ship required reacquiring the new target, creating gaps in fire control.

Over 400 Type 284 sets were produced, equipping battleships, cruisers, and some large destroyers. The radar remained in Royal Navy service into the 1950s, testament to its effective design.

## Tactical Tips
- **Cueing is Critical**: Type 284 cannot find targets for you. Ensure you have functional search radar (Type 271/272) or good visual lookouts to detect enemies first.
- **Priority Target Selection**: You can only track ONE target. Choose the most dangerous enemy ship and maintain lock. Switching targets costs precious seconds.
- **Night Fighting**: Type 284's true value emerges in darkness. While enemy optical rangefinders struggle, your radar-controlled guns maintain accuracy. Press night engagements aggressively.
- **Smoke Advantage**: If the enemy deploys smoke screens, they blind themselves more than you. Type 284 tracks right through smoke - fire with confidence.
- **Maintain Lock**: Brief the radar operator to keep the beam on target even during evasive maneuvers. Losing lock means starting over.
- **Range Data Priority**: The most valuable Type 284 output is RANGE. Bearing can be estimated optically, but accurate range is nearly impossible without radar. Trust the range data.
- **Fire Control Integration**: Feed Type 284 data directly to your main battery computer. The combination of radar range + computer ballistics = devastating accuracy.
- **Weather Operations**: Heavy rain reduces range by 10%, but Type 284 still outperforms optical rangefinders in storms. Use weather to your advantage.
- **Multiple Directors**: Large ships with multiple directors (e.g., King George V with separate fore/aft directors) can install multiple Type 284 sets to track different targets simultaneously.
- **Maneuvering Targets**: Against zig-zagging destroyers, use the continuous 1-second updates to maintain tracking. The rapid update rate handles evasive maneuvers.
- **Beyond Visual Range**: Type 284 enables engagement at ranges where the enemy is barely visible or completely obscured. Open fire earlier than optical-only ships can.
- **Backup Optical**: If Type 284 fails (18% chance), immediately fall back to optical rangefinding. Train backup optical crews to be ready.
