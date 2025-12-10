---
module_id: RAD-012
name: FuMO 27 Fire Control Radar
category: support
subcategory: detection-radar
function: fire_control
era: 1942
nation: Germany
slot_type: support

# Coverage Mechanics
scan_type: directional
cone_angle: 20           # degrees
rotation_speed: manual   # manually aimed
sector_options: []
modes: [manual]
default_mode: manual

# Performance
detection_range: 14      # km
accuracy: 90             # % bearing accuracy
resolution: 80           # meters (distinguish close contacts)
update_rate: 1           # seconds between detections
height_finding: false

# Physical
weight: 3100
crew_required: 2
reliability: 74

# Limitations
min_range: 300           # meters
weather_penalty: 14      # % range loss
sea_clutter: moderate

tags: [radar, fire_control, germany, wwii, 1942, kriegsmarine]
---

# FuMO 27 Fire Control Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | FuMO 27 (Funkmessortung) |
| **Nation** | Kriegsmarine (Germany) |
| **Era** | 1942+ |
| **Function** | Fire Control (Main Battery) |
| **Scan Type** | Directional 20° |

## Coverage Pattern
```
Scan Type:        Directional (manually aimed)
Cone Angle:       20° narrow beam
Rotation Speed:   Manual (follows gunnery director)
Coverage:         Only where operator points it
Update Rate:      1-second updates when locked on target
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

Narrow beam requires accurate pointing
Provides continuous range when locked
Similar concept to British Type 284
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 14 km | Maximum range for large targets |
| Cruiser | 13 km | Good tracking capability |
| Destroyer | 11 km | Adequate against smaller vessels |
| Submarine (surfaced) | 6 km | Limited small-target performance |
| MTB/PT Boat | 4 km | Poor detection of small craft |

**Note**: FuMO 27 is NOT a search radar. Must be cued to target by FuMO 25 search radar or visual sighting before it can track.

## Operation Modes
### Manual Mode (Only Mode)
Operator manually aims the narrow 20° beam at the target. The radar is typically slaved to the main battery director, tracking where the guns are pointed. Once locked onto a target, provides continuous range and bearing data to the fire control computer, significantly improving gunnery accuracy over optical rangefinding alone.

**Operation Sequence**:
1. FuMO 25 search radar or visual lookouts detect enemy
2. Main battery director trains onto target bearing
3. FuMO 27 beam illuminates target
4. Radar locks and provides precise range data
5. Fire control computer calculates firing solution
6. Guns fire with radar-enhanced accuracy

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,100 kg |
| Crew Required | 2 |
| Reliability | 74% |
| Frequency | 82 cm (UHF) |
| Antenna Type | Directional reflector |
| Mounting | Director-slaved |

## Advantages
- Provides accurate range data (90% accuracy) for gunnery
- Good resolution (80m) for precision tracking
- Continuous 1-second updates track maneuvering targets
- Enables blind firing through smoke, night, or poor visibility
- Moderate weight suitable for capital ships and cruisers
- Reasonable power consumption (36 kW)
- Better than optical rangefinding in reduced visibility
- Can track targets obscured by battle haze

## Disadvantages
- Limited range (14 km) compared to Allied FC radars
- Narrow 20° beam requires accurate cueing
- Can only track one target at a time
- Below-average reliability (74%) for fire control equipment
- No height-finding capability for AA fire
- 300m minimum range prevents very close engagements
- Operator skill required to maintain lock
- Weather degrades performance by 14%
- Limited production numbers
- Spare parts increasingly scarce after 1943

## Historical Notes

The FuMO 27 fire control radar represented the Kriegsmarine's effort to provide radar-directed gunnery to its surface fleet. Introduced in 1942, it equipped the major capital ships including Tirpitz, Scharnhorst, and remaining cruisers. The system significantly improved gunnery accuracy compared to pure optical fire control.

During the Battle of the Barents Sea (December 1942), German cruisers equipped with FuMO 27 achieved better gunnery accuracy than expected given the Arctic conditions - darkness, snow squalls, and extreme cold. However, the German commander's tactical hesitancy meant this technical advantage was not fully exploited.

At the Battle of North Cape (December 1943), Scharnhorst's FuMO 27 radar initially provided effective fire control against the British covering force. However, British radar fire control (Type 284) proved superior, and HMS Duke of York's devastating accuracy in near-zero visibility contributed to Scharnhorst's destruction. The German radar's 14 km range was also inferior to the British 15+ km range.

Tirpitz's FuMO 27 installation was damaged during various air attacks on the battleship in Norwegian fjords. Spare parts shortages meant the radar was frequently non-operational during 1943-1944. During the final British attacks that sank the ship in November 1944, Tirpitz's FuMO 27 was reportedly inoperative.

The FuMO 27's 74% reliability rating reflected both technical limitations and the deteriorating Kriegsmarine logistics situation. By 1944, many installations were degraded or non-functional due to lack of maintenance and spare parts.

Production was limited compared to Allied programs. Perhaps 30-40 FuMO 27 sets were manufactured, equipping only the most important surface vessels. Smaller ships relied on optical fire control throughout the war.

## Tactical Tips
- **Cueing Requirement**: FuMO 27 cannot find targets independently. Ensure FuMO 25 search radar or visual lookouts detect enemies first before attempting to engage with radar fire control.
- **Range Limitation**: The 14 km range means you must close to medium ranges for radar fire control. Don't expect effective radar gunnery beyond this distance.
- **Night Advantage**: FuMO 27's primary value is night fighting. In darkness where British ships have Type 284, you're on more equal footing than in daylight.
- **Arctic Operations**: The radar performs reasonably well in Arctic conditions (Norway, Barents Sea). Use it to compensate for limited daylight in northern latitudes.
- **Maintain Lock**: Brief operators to keep the narrow 20° beam on target. Losing lock means reacquiring, which wastes critical seconds during engagements.
- **Priority Target**: Since you can only track one target, choose the most dangerous enemy ship. Against multiple British cruisers, focus on the one most likely to land hits on you.
- **Reliability Management**: At 74% reliability, expect FuMO 27 to be non-functional about 1/4 of the time. Always maintain optical fire control capability as backup.
- **Weather Compensation**: Heavy North Sea or Atlantic weather reduces range by 14%. In storms, effective range may be only 12 km.
- **Combine with FuMO 25**: Use FuMO 25 to search, FuMO 27 to track. The combination provides comprehensive radar capability for surface actions.
- **Smoke Screens**: If engaged in smoke screen conditions (common in North Sea actions), FuMO 27 can track through smoke while enemy optical systems are blinded.
- **Range Data Priority**: The most valuable FuMO 27 output is precise RANGE. Bearing can be estimated optically, but accurate range is crucial for gunnery solutions.
- **Historical Context**: If playing 1943-1944 scenarios, reflect increasing unreliability due to spare parts shortages. By 1944, many German FC radars were degraded or inoperative.
- **Capital Ship Advantage**: FuMO 27 is typically only available on battleships and heavy cruisers. Smaller vessels lack this capability, so exploit it when you have it.
- **Concentration of Force**: With limited radar-equipped ships, concentrate your radar-capable vessels together. A formation with multiple FuMO 27-equipped ships has significant advantage over non-radar enemies.
