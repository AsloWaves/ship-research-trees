---
module_id: RAD-006
name: SK Air Search Radar
category: support
subcategory: detection-radar
function: air_search
era: 1942
nation: USA
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360          # degrees (360 for full rotation)
rotation_speed: 4        # seconds per full rotation
sector_options: [90, 120, 180]
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 120     # km (for aircraft)
accuracy: 88             # % bearing accuracy
resolution: 800          # meters (distinguish close contacts)
update_rate: 4           # seconds between detections
height_finding: false

# Physical
weight: 7200
crew_required: 3
reliability: 85

# Limitations
min_range: 1500          # meters
weather_penalty: 12      # % range loss
sea_clutter: moderate

tags: [radar, air_search, usa, wwii, 1942, standard]
---

# SK Air Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | SK (Signal-King) |
| **Nation** | United States |
| **Era** | 1942+ |
| **Function** | Air Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   4 seconds per sweep
Coverage:         Complete hemispheric air coverage
Update Rate:      Aircraft position updates every 4 seconds
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  (Antenna rotates rapidly)
      / | \     (Optimized for aircraft detection)
     /  |  \
   SW   |   SE
        |
        S

Sweep: ======> (4 seconds for full rotation)
Fast rotation provides near-continuous tracking
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Heavy Bomber (high) | 120 km | Excellent long-range detection |
| Medium Bomber | 100 km | Reliable early warning |
| Fighter (high) | 75 km | Good against even small aircraft |
| Torpedo Bomber (low) | 50 km | Significantly better than British sets |
| Dive Bomber | 65 km | Tracks throughout approach |
| Large Formation | 130 km | Mass of aircraft increases range |
| Battleship (surface) | 25 km | Acceptable surface detection |

## Operation Modes
### Auto Mode
Antenna rotates continuously at 4-second intervals, providing rapid updates on all air contacts. The fast rotation combined with good resolution allows operators to build accurate raid plots without manual intervention. Default mode for fleet operations.

### Manual Mode
Operator can slow or pause rotation to study specific contacts in detail. The high-quality PPI display makes this rarely necessary - most situations handled in auto mode. Use manual for extremely large raids where counting aircraft groups is critical.

### Sector Mode
Restricts sweep to a chosen arc (90°, 120°, or 180°). Update rate improves to 1.5-2 seconds in focused sector. Excellent for fighter direction during active engagements - the near-continuous updates allow vectoring fighters with precision.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 7,200 kg |
| Crew Required | 3 |
| Reliability | 85% |
| Frequency | 1.5 m (VHF) |
| Antenna Type | Bedspring array |
| Display | Large PPI scope |

## Advantages
- Exceptional range (120 km) provides 10-15 minutes warning
- Very fast 4-second rotation tracks aircraft continuously
- Good resolution (800m) distinguishes individual groups
- High reliability (85%) - consistently operational
- Excellent accuracy (88%) for fighter direction
- Can track low-altitude threats effectively (50 km)
- Large PPI display easy for operators to interpret
- Adequate surface search capability (25 km)
- Proven reliability in Pacific theater conditions
- Heavy jamming resistance

## Disadvantages
- No height-finding capability (requires separate Type SK-2)
- Heavy and requires substantial mounting structure
- High power consumption (70 kW)
- Large "bedspring" antenna visible from long range
- Three-person crew requirement
- Antenna vulnerable to storm damage and combat
- Moderate sea clutter in rough conditions
- 1500m minimum range blind spot

## Historical Notes

The SK air search radar became the standard US Navy air warning radar from 1942 onwards, equipping carriers, battleships, and cruisers throughout the Pacific War. Its combination of long range, fast rotation, and reliable operation made it the backbone of fleet air defense.

At the Battle of the Philippine Sea (June 1944), SK-equipped carriers detected the incoming Japanese raid at over 110 km range, providing ample time for Admiral Mitscher to launch his fighter screen. The resulting "Great Marianas Turkey Shoot" was partly enabled by SK radar's early warning, allowing Hellcat fighters to climb to altitude and position for interception.

During kamikaze operations in 1944-1945, SK radar proved invaluable for detecting individual suicide aircraft approaching from all directions. The 4-second update rate allowed CAP fighters to be vectored continuously as kamikazes maneuvered. However, the lack of height-finding meant visual observation was still needed to determine if contacts were high or low.

At Okinawa (April-June 1945), SK radar on radar picket destroyers provided the first line of defense against massed kamikaze raids. Ships like USS Laffey survived multiple attacks partly because SK radar gave gunners maximum warning time. The fast rotation meant even diving aircraft were tracked until seconds before impact.

The distinctive "bedspring" antenna became an iconic sight on US warships. Over 1,000 SK sets were produced, and many remained in service into the 1950s. The SK-2 variant added height-finding capability, but basic SK remained the most common installation.

## Tactical Tips
- **Raid Detection**: SK's 120 km range gives you 12-15 minutes before bombers arrive. Use every second - launch CAP, scramble ready aircraft, prepare AA defenses, increase speed.
- **Fighter Direction**: In sector mode focused on the raid bearing, update rate drops to 2 seconds. Vector fighters with confidence - "Bogey bearing 045, range 70 miles, closing."
- **CAP Management**: Use SK to maintain CAP station coverage. If fighters stray from their assigned sector, you'll see it on the scope and can redirect them.
- **Kamikaze Defense**: The 4-second rotation is fast enough to track even diving kamikazes. Once visual contact is made, radar operators can call out bearing changes to gun directors.
- **Night Operations**: SK excels at night fighter direction. Vector night fighters using radar bearings, guiding them to within visual range (1-2 km) of enemy aircraft.
- **Raid Composition**: Multiple discrete blips = multiple groups. A solid mass = tight formation. Use this to estimate attack type: spread out = search pattern, tight = coordinated strike.
- **Low-Level Detection**: SK's 50 km low-level detection is excellent. Don't assume torpedo bombers will sneak through - you'll see them coming.
- **Surface Utility**: While not optimized for surface search, SK's 25 km surface range is adequate for fleet screening. Use it to maintain formation awareness at night.
- **Weather Compensation**: In heavy weather, reduce effective range by 12%. Rain squalls can mask aircraft - tell CAP to visually check squall areas.
- **Combine with SM Fighter Control**: SK provides detection; SM height-finding radar determines altitude. Together they create a complete air picture for CIC.
- **Picket Duty**: If assigned radar picket duty, keep SK running continuously even if it means reducing speed to conserve power. Your job is to be the fleet's eyes.
