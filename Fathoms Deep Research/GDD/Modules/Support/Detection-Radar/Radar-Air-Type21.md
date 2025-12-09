---
module_id: RAD-007
name: Type 21 Air Search Radar
category: support
subcategory: detection-radar
function: air_search
era: 1941
nation: Japan
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360          # degrees (360 for full rotation)
rotation_speed: 15       # seconds per full rotation
sector_options: [90, 120, 180]
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 70      # km (for aircraft)
accuracy: 70             # % bearing accuracy
resolution: 3000         # meters (distinguish close contacts)
update_rate: 15          # seconds between detections
height_finding: false

# Physical
weight: 6200
power_draw: 58
crew_required: 3
reliability: 58

# Limitations
min_range: 3000          # meters
weather_penalty: 25      # % range loss
sea_clutter: high

tags: [radar, air_search, japan, wwii, 1941, limited]
---

# Type 21 Air Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 21 (二号一型電波探信儀) |
| **Nation** | Imperial Japanese Navy |
| **Era** | 1941+ |
| **Function** | Air Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   15 seconds per sweep
Coverage:         Complete hemispheric air coverage
Update Rate:      Aircraft position updates every 15 seconds
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  (Antenna rotates slowly)
      / | \     (Long gaps between updates)
     /  |  \
   SW   |   SE
        |
        S

Sweep: ---> (15 seconds for full rotation)
Slow rotation creates tracking gaps
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Heavy Bomber (high) | 70 km | Maximum range, ideal conditions |
| Medium Bomber | 55 km | Marginal early warning |
| Fighter (high) | 40 km | Limited detection of small aircraft |
| Torpedo Bomber (low) | 25 km | Poor low-altitude performance |
| Dive Bomber | 35 km | Inadequate warning time |
| Large Formation | 80 km | Mass formation more visible |
| Battleship (surface) | 10 km | Very poor surface detection |

## Operation Modes
### Auto Mode
Antenna rotates continuously at 15-second intervals. The slow rotation means aircraft can move 3-5 kilometers between updates, creating "jumping" contacts on the display. Operators must extrapolate tracks manually, introducing significant error.

### Manual Mode
Operator can pause rotation to focus on specific bearings. Given the poor resolution (3000m) and low accuracy, manual mode provides limited benefit. Primarily used when trying to distinguish between large formations approaching from similar bearings.

### Sector Mode
Locks antenna to sweep a specific arc (90°, 120°, or 180°). Update rate improves to 6-8 seconds in focused sector. This mode somewhat compensates for the slow base rotation, but still inferior to Allied rotating sets in auto mode.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 6,200 kg |
| Power Draw | 58 kW |
| Crew Required | 3 |
| Reliability | 58% |
| Frequency | 4.2 m (VHF) |
| Antenna Type | Metric dipole array |
| Display | A-scope display |

## Advantages
- Provides some air warning capability (better than none)
- 360° coverage eventually detects threats from all directions
- Adequate range (70 km) under ideal conditions
- Can detect large bomber formations at useful ranges
- Lighter than some contemporary Allied sets
- Requires moderate power (58 kW)
- When working, provides critical early warning

## Disadvantages
- **Major limitation**: Very slow 15-second rotation
- Poor resolution (3000m) - cannot distinguish individual aircraft
- Low accuracy (70%) makes fighter direction difficult
- Low reliability (58%) - frequently inoperative
- Poor performance against low-altitude threats
- Very large minimum range (3000m) blind spot
- Heavy weather severely degrades performance
- Requires three operators despite limited capability
- Limited production numbers
- Spare parts increasingly scarce after 1943

## Historical Notes

The Type 21 air search radar represented the IJN's attempt to field air warning radar comparable to Allied systems. Introduced in 1941-1942, it was installed on major fleet units including carriers, battleships, and heavy cruisers. However, limited production meant many vessels never received radar at all.

At the Battle of the Philippine Sea (June 1944), Japanese carriers equipped with Type 21 detected the incoming American raid at approximately 70 km range. However, the slow update rate and poor accuracy meant Japanese fighter controllers struggled to vector interceptors effectively. Combined with poorly trained radar operators, the result was the "Great Marianas Turkey Shoot."

The Type 21's limitations became tragically apparent during the Battle of Leyte Gulf (October 1944). Admiral Kurita's Center Force, equipped with Type 21 on several ships, detected American carrier aircraft but could not provide effective fighter direction. The slow 15-second updates meant contacts "jumped" across the display, making it nearly impossible to vector CAP fighters accurately.

During the kamikaze campaign, Type 21-equipped ships theoretically could detect incoming American raids, but the combination of low reliability, untrained operators, and slow update rates meant visual lookouts often detected aircraft first. By 1945, fuel shortages meant ships at anchor often couldn't generate enough power for continuous radar operation.

Production was limited to approximately 150 sets, far fewer than needed. By late 1944, operational readiness of surviving Type 21 sets was below 40% due to lack of spare parts, battle damage, and inadequate maintenance. Many ships officially equipped with radar had non-functional sets.

## Tactical Tips
- **Expect Failures**: With 58% reliability, assume your Type 21 will be non-functional 40% of the time. Maintain visual lookout doctrine as primary detection method.
- **Sector Focus for CAP**: If defending against a known threat axis, use sector mode. The 6-8 second updates are marginally adequate for fighter direction, though still inferior to Allied standards.
- **Early Launch**: The slow updates mean you need more warning time. If Type 21 detects aircraft at 70 km, launch CAP immediately - don't wait for better tracking data.
- **Extrapolate Manually**: Train operators to mentally plot aircraft movement between 15-second updates. Mark each detection on a manual plotting board to create tracks.
- **Large Formations**: Type 21 is better at detecting large raids than small groups. A 50-plane strike is much more likely to be detected reliably than 3-4 aircraft.
- **Supplement with Visual**: Station lookouts to report aircraft that radar misses. In Pacific visibility conditions, lookouts may detect low-altitude threats before Type 21.
- **Power Management**: The moderate 58 kW draw means Type 21 can run on auxiliary power. Keep it operating even when main engines are down.
- **Weather Degradation**: In storms or heavy rain, effective range drops to 50 km or less. Don't trust negative radar returns in bad weather.
- **Pre-Position CAP**: Since fighter direction is difficult, pre-position CAP at likely intercept points rather than trying to vector them from the ship.
- **Historical Context**: If playing late-war scenarios (1944-45), assume Type 21 is frequently inoperative. This is historically accurate and reflects IJN's declining technical capability.
- **Coordinate with Allies**: If operating with multiple IJN ships, designate one as primary radar guard. Concentration of effort better than multiple unreliable sets.
