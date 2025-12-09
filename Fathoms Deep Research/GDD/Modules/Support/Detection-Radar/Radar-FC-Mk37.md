---
module_id: RAD-010
name: Mk 37 Fire Control Radar
category: support
subcategory: detection-radar
function: fire_control
era: 1941
nation: USA
slot_type: support

# Coverage Mechanics
scan_type: directional
cone_angle: 25           # degrees
rotation_speed: manual   # manually aimed
sector_options: []
modes: [manual]
default_mode: manual

# Performance
detection_range: 18      # km
accuracy: 98             # % bearing accuracy
resolution: 30           # meters (distinguish close contacts)
update_rate: 0.5         # seconds between detections (near-continuous)
height_finding: true     # can determine altitude for AA fire

# Physical
weight: 3600
power_draw: 40
crew_required: 2
reliability: 92

# Limitations
min_range: 150           # meters
weather_penalty: 8       # % range loss
sea_clutter: very_low

tags: [radar, fire_control, usa, wwii, 1941, dual_purpose, excellent]
---

# Mk 37 Fire Control Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Mk 37 Director with FC Radar |
| **Nation** | United States |
| **Era** | 1941+ |
| **Function** | Fire Control (Dual-Purpose: Surface & AA) |
| **Scan Type** | Directional 25° |

## Coverage Pattern
```
Scan Type:        Directional (manually aimed)
Cone Angle:       25° narrow beam
Rotation Speed:   Manual (follows Mk 37 director)
Coverage:         Only where operator points it
Update Rate:      Near-continuous (0.5-second updates when locked)
Height Finding:   YES - can determine altitude for AA fire
```

**Visual Pattern:**
```
        N
        |
        |    25° Beam
        |   /----\
        |  /      \
W ------+------------- E
      TARGET

Narrow beam tracks surface ships OR aircraft
Height-finding capability for AA engagements
Most advanced FC radar of WWII
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 18 km | Maximum surface range |
| Cruiser | 17 km | Excellent tracking |
| Destroyer | 15 km | Reliable lock |
| Aircraft (high) | 12 km | AA mode with altitude data |
| Aircraft (low) | 8 km | Altitude determination included |
| MTB/PT Boat | 6 km | Small surface targets |

**Dual-Purpose**: Tracks both surface ships AND aircraft, providing altitude data for AA gunnery.

## Operation Modes
### Manual Mode (Only Mode)
Operator manually aims the narrow 25° beam at the target. The radar is integrated with the Mk 37 gun director, automatically tracking where the director points. Provides continuous range, bearing, and (for aircraft) altitude data to the Mk 37 fire control computer.

**Surface Gunnery Sequence**:
1. Search radar or visual sighting detects enemy ship
2. Mk 37 director trains onto target bearing
3. FC radar locks and provides precise range/bearing
4. Mk 37 computer calculates firing solution
5. Guns fire with exceptional accuracy

**AA Gunnery Sequence**:
1. Air search radar detects incoming aircraft
2. Mk 37 director elevates to aircraft bearing/altitude
3. FC radar locks and provides range/bearing/ALTITUDE
4. Mk 37 computer calculates lead angle and fuze setting
5. 5"/38 guns fire VT-fuzed shells with radar-predicted intercept

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,600 kg |
| Power Draw | 40 kW |
| Crew Required | 2 |
| Reliability | 92% |
| Frequency | 10 cm (S-band) |
| Antenna Type | Precision directional dish |
| Mounting | Integrated with Mk 37 director |

## Advantages
- **Dual-purpose**: Tracks both surface ships and aircraft
- **Height-finding**: Determines aircraft altitude for AA fire
- Exceptional accuracy (98%) - best FC radar of WWII
- Superior resolution (30m) distinguishes close targets
- Near-continuous updates (0.5 seconds) track maneuvering targets
- Outstanding reliability (92%) - consistently operational
- Excellent range (18 km) exceeds most FC radars
- Integrates seamlessly with Mk 37 director/computer
- Low sea clutter performance
- Small minimum range (150m) allows close engagements
- Works effectively in all weather conditions

## Disadvantages
- Can only track one target at a time (like all FC radars)
- Narrow 25° beam requires accurate cueing
- Not a search radar - must be cued to target
- Higher power draw than some equivalents (40 kW)
- Requires skilled operators for optimal performance
- Moderate weight increases director mass
- Expensive and complex system

## Historical Notes

The Mk 37 gun director with integrated fire control radar became the most effective naval AA fire control system of WWII. The combination of the Mk 37 director, FC radar, ballistic computer, and 5"/38 dual-purpose guns created an integrated weapon system unmatched by any other navy.

During the Naval Battle of Guadalcanal (November 1942), USS Washington used her Mk 37-equipped 5"/38 secondary battery to engage Japanese destroyers at night with devastating accuracy. The radar-directed secondaries achieved hits that optical fire control could never have made in darkness.

The Mk 37's true brilliance emerged in AA defense. At the Battle of the Philippine Sea (June 1944), Mk 37-equipped ships formed the core of Task Force 58's AA defenses. The radar's altitude-finding capability allowed computer-predicted intercepts of diving aircraft - something impossible with optical directors.

During kamikaze operations at Okinawa (1945), the Mk 37 system proved itself under the most extreme conditions. Ships like USS Laffey survived multiple kamikaze attacks partly because Mk 37 directors maintained tracking even on diving aircraft in the final seconds before impact, directing 5"/38 fire with lethal precision.

The height-finding capability was revolutionary. Previous AA fire control required visual estimation of altitude, introducing significant error. Mk 37 radar measured altitude directly, feeding precise data to the Mk 37 computer for accurate fuze settings and lead angles.

Over 1,000 Mk 37 directors were produced during WWII, equipping everything from destroyers (1 director) to battleships (4+ directors). The system remained in US Navy service through the 1960s on FRAM-upgraded destroyers.

## Tactical Tips
- **Dual-Purpose Versatility**: Switch between surface and AA targets as threats change. The 0.5-second update rate allows rapid target switching compared to other FC radars.
- **AA Priority**: Against aircraft, Mk 37's height-finding is decisive. Use it aggressively - you can engage aircraft with precision that enemy AA cannot match.
- **VT Fuze Synergy**: Mk 37 radar + VT proximity fuzes = devastating AA effectiveness. The radar provides altitude, VT fuzes detonate automatically. This combination dominated Pacific air battles.
- **Night Surface Actions**: In darkness, Mk 37 radar provides accuracy impossible for enemy optical fire control. Engage aggressively at night.
- **Multiple Directors**: Destroyers have 1 Mk 37, cruisers have 2-4, battleships have 4-6. Assign each director to separate targets for maximum firepower distribution.
- **Maintain Lock**: The 25° beam is forgiving compared to narrower FC radars. However, brief operators to track smoothly - losing lock wastes precious seconds.
- **Computer Integration**: Trust the Mk 37 computer's solution. The combination of radar ranging + ballistic computation is more accurate than human estimation.
- **Kamikaze Defense**: Against diving kamikazes, Mk 37 tracks continuously until seconds before impact. Keep firing even when the target seems impossibly close.
- **Range Advantage**: The 18 km range exceeds many enemy FC radars. You can engage under radar control while enemies still use optical ranging.
- **Weather Operations**: The 8% weather penalty is minimal. In storms that blind optical fire control, Mk 37 maintains near-full effectiveness.
- **Small Target Tracking**: The 30m resolution allows tracking even small targets like PT boats. Don't assume small size means impossible to hit.
- **Reliability Trust**: At 92% reliability, Mk 37 is one of the most dependable systems in your arsenal. Build tactics assuming it will work.
- **Training Investment**: Mk 37's capabilities require skilled operators. Ensure radar/director crews are trained to expert level for maximum effectiveness.
- **Altitude Exploitation**: When engaging high-altitude bombers, use Mk 37's altitude data to set optimal fuze timing. This capability wins AA engagements.
