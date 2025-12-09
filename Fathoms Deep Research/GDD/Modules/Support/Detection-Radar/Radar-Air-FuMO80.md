---
module_id: RAD-008
name: FuMO 80 Air Search Radar
category: support
subcategory: detection-radar
function: air_search
era: 1943
nation: Germany
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360          # degrees (360 for full rotation)
rotation_speed: 8        # seconds per full rotation
sector_options: [90, 120, 180]
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 60      # km (for aircraft)
accuracy: 78             # % bearing accuracy
resolution: 1500         # meters (distinguish close contacts)
update_rate: 8           # seconds between detections
height_finding: false

# Physical
weight: 5800
power_draw: 62
crew_required: 3
reliability: 70

# Limitations
min_range: 2500          # meters
weather_penalty: 18      # % range loss
sea_clutter: moderate

tags: [radar, air_search, germany, wwii, 1943, late_war]
---

# FuMO 80 Air Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | FuMO 80 Freya (Funkmessortung) |
| **Nation** | Kriegsmarine (Germany) |
| **Era** | 1943+ |
| **Function** | Air Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   8 seconds per sweep
Coverage:         Complete hemispheric air coverage
Update Rate:      Aircraft position updates every 8 seconds
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  (Antenna rotates continuously)
      / | \     (Freya-pattern detection)
     /  |  \
   SW   |   SE
        |
        S

Sweep: -----> (8 seconds for full rotation)
Moderate rotation provides acceptable tracking
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Heavy Bomber (high) | 60 km | Maximum range, high altitude |
| Medium Bomber | 50 km | Reliable detection |
| Fighter (high) | 35 km | Adequate against small aircraft |
| Torpedo Bomber (low) | 25 km | Limited low-altitude capability |
| Dive Bomber | 30 km | Marginal warning time |
| Large Formation | 70 km | Mass increases detection range |
| Battleship (surface) | 12 km | Poor surface search performance |

## Operation Modes
### Auto Mode
Antenna rotates continuously at 8-second intervals, providing regular updates on air contacts. The moderate rotation speed balances coverage with tracking precision. Operators can build reasonably accurate raid plots without excessive extrapolation.

### Manual Mode
Operator can pause or slow rotation to study specific contacts in detail. Useful when multiple formations approach from different bearings and operators need to distinguish them. The FuMO 80's display requires interpretation, making manual mode valuable for experienced crews.

### Sector Mode
Restricts antenna sweep to a chosen arc (90°, 120°, or 180°). Update rate improves to 3-4 seconds in focused sector. Recommended when protecting a known approach lane, such as detecting Allied bombers approaching from British bases.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 5,800 kg |
| Power Draw | 62 kW |
| Crew Required | 3 |
| Reliability | 70% |
| Frequency | 2.4 m (VHF) |
| Antenna Type | Mattress array |
| Display | Panoramic oscilloscope |

## Advantages
- Naval adaptation of proven Luftwaffe Freya design
- Adequate range (60 km) for early warning
- Moderate 8-second rotation provides acceptable tracking
- Reasonable reliability (70%) for late-war German equipment
- Familiar technology - leverages existing radar expertise
- Works in Baltic and North Sea conditions
- Can detect large formations at useful ranges
- Moderate power consumption suitable for surface vessels

## Disadvantages
- Introduced late in the war (1943) - limited deployment
- Inferior to contemporary Allied air search radars
- No height-finding capability
- Moderate resolution struggles with close formations
- Large minimum range (2500m) blind spot
- Production limited by Allied bombing and resource priority
- Metric wavelength technology becoming obsolete by 1943
- Weather significantly affects performance
- Required trained operators increasingly scarce

## Historical Notes

The FuMO 80 represented the Kriegsmarine's late-war effort to provide surface vessels with dedicated air search capability. Based on the Luftwaffe's successful Freya ground-based radar, the FuMO 80 adapted this proven technology for naval use, mounting the "mattress" antenna array on capital ships and large vessels.

Introduced in 1943, FuMO 80 installation was limited primarily to surviving capital ships, heavy cruisers, and specialized vessels. Scharnhorst received a FuMO 80 installation before her final sortie against Convoy JW 55B in December 1943. The radar detected RAF shadowing aircraft at approximately 50 km range, but this early warning proved insufficient as the ship ultimately succumbed to overwhelming British naval forces.

The cruiser Prinz Eugen operated with FuMO 80 during Baltic operations in 1944-1945, using it to detect Soviet aircraft during shore bombardment missions. The moderate 60 km range provided adequate warning in the tactical environment of Baltic operations, where engagements occurred at shorter ranges than in the Atlantic or Pacific.

Limited production meant most Kriegsmarine vessels never received FuMO 80 installations. The radar was primarily allocated to vessels still conducting offensive operations, while ships in Norway or defensive positions in the Baltic relied on older equipment or no radar at all. By late 1944, production essentially ceased as Allied bombing destroyed manufacturing facilities.

The FuMO 80's 70% reliability was reasonable for German late-war standards, but spare parts scarcity meant even minor failures could sideline a set for weeks. Technical crews improvised repairs using components cannibalized from damaged ships.

## Tactical Tips
- **Baltic Operations**: FuMO 80 is adequate for Baltic Sea air defense. The shorter ranges involved mean 60 km detection provides sufficient warning against Soviet air attacks.
- **Early Warning**: Use the 60 km range to maximum advantage. Begin AA preparations immediately upon detection - you have perhaps 6-8 minutes before bombers arrive.
- **Fighter Direction**: If you have CAP aircraft (rare for Kriegsmarine), use sector mode for fighter direction. The 3-4 second updates in sector mode are marginally adequate for vectoring.
- **Formation Tracking**: The 8-second rotation allows building raid plots. Have operators manually plot each detection to determine course and speed of incoming formations.
- **Combine with Surface Search**: Use FuMO 80 for air, FuMO 25 for surface. Don't rely on FuMO 80 for surface contacts - its 12 km surface range is inadequate.
- **Weather Compensation**: North Sea and Baltic storms degrade performance by 18%. In heavy weather, assume effective range is 50 km or less.
- **Reliability Management**: Expect the radar to be non-functional 30% of the time. Maintain visual lookout procedures as backup. Have technical crew ready for rapid repairs.
- **Large Raids**: FuMO 80 performs better against large formations. A 20-30 aircraft raid is more likely to be detected at maximum range than 2-3 aircraft.
- **Night Operations**: The radar provides valuable night air warning capability that visual lookouts cannot match. This is your primary advantage in darkness.
- **Resource Scarcity**: If playing late-war scenarios (1944-45), spare parts are scarce. Operate conservatively - don't push the equipment beyond necessary. A working radar at 80% performance is better than broken radar at 0%.
- **Historical Context**: By 1944, Allied air supremacy meant German surface vessels rarely sortied. If your ship has FuMO 80, you're probably in the Baltic supporting ground forces or evacuating refugees. Use the radar for defensive air warning during these missions.
