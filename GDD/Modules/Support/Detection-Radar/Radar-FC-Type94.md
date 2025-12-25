---
module_id: RAD-011
name: Type 94 Fire Control Radar
category: support
subcategory: detection-radar
function: fire_control
era: 1944
nation: Japan
slot_type: support

# Coverage Mechanics
scan_type: directional
cone_angle: 30           # degrees
rotation_speed: manual   # manually aimed
sector_options: []
modes: [manual]
default_mode: manual

# Performance
detection_range: 12      # km
accuracy: 85             # % bearing accuracy
resolution: 150          # meters (distinguish close contacts)
update_rate: 2           # seconds between detections
height_finding: false

# Physical
weight: 2900
crew_required: 2
reliability: 55

# Limitations
min_range: 400           # meters
weather_penalty: 22      # % range loss
sea_clutter: high

tags: [radar, fire_control, japan, wwii, 1944, late_war, limited]
---

# Type 94 Fire Control Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 94 (九号四型電波探信儀) |
| **Nation** | Imperial Japanese Navy |
| **Era** | 1944+ |
| **Function** | Fire Control (Main Battery) |
| **Scan Type** | Directional 30° |

## Coverage Pattern
```
Scan Type:        Directional (manually aimed)
Cone Angle:       30° relatively wide beam
Rotation Speed:   Manual (follows gunnery director)
Coverage:         Only where operator points it
Update Rate:      2-second updates when locked on target
```

**Visual Pattern:**
```
        N
        |
        |    30° Beam
        |   /-----\
        |  /       \
W ------+-------------- E
      TARGET

Wider beam than Allied FC radars
Easier to acquire targets but less precise
Late-war development with limited deployment
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 12 km | Maximum range for large targets |
| Cruiser | 11 km | Adequate tracking |
| Destroyer | 9 km | Limited range against small targets |
| Submarine (surfaced) | 5 km | Poor performance |
| MTB/PT Boat | 3 km | Barely detectable |

**Note**: Type 94 is NOT a search radar. Must be cued by other means before it can track. Range significantly inferior to Allied FC radars.

## Operation Modes
### Manual Mode (Only Mode)
Operator manually aims the 30° beam at the target. The wider beam makes initial acquisition easier than Allied narrow-beam systems, but provides less precise tracking data. Once locked onto a target, provides range and bearing data to the fire control system, though with less accuracy than Allied equivalents.

**Operation Sequence**:
1. Surface search radar or visual sighting detects enemy
2. Main battery director trains onto approximate target bearing
3. Type 94's wide beam finds target (easier than narrow beams)
4. Radar locks and provides range/bearing data
5. Fire control computer uses radar data for gunnery solution
6. Guns fire with radar-derived accuracy (inferior to Allied solutions)

## Specifications
| Spec | Value |
|------|-------|
| Weight | 2,900 kg |
| Crew Required | 2 |
| Reliability | 55% |
| Frequency | 10 cm (S-band) |
| Antenna Type | Directional reflector |
| Mounting | Director-slaved |

## Advantages
- Lighter than Allied FC radars (2,900 kg)
- Lower power consumption (32 kW)
- Wider 30° beam easier to acquire targets initially
- Provides some radar fire control capability (vs. none)
- Works in night conditions where optical rangefinding fails
- Can track through smoke screens
- Better than relying entirely on optical rangefinders

## Disadvantages
- **Major limitation**: Very low reliability (55%) - often inoperative
- Limited range (12 km) inferior to Allied FC radars
- Poor accuracy (85%) compared to Mk 37 (98%)
- Coarse resolution (150m) struggles with precision tracking
- Slow 2-second update rate inferior to Allied sub-second rates
- No height-finding capability for AA fire
- Large minimum range (400m) prevents close engagements
- High sea clutter in rough weather
- Introduced very late (1944) - limited production
- Spare parts virtually nonexistent by late 1944
- Trained operators scarce

## Historical Notes

The Type 94 fire control radar represented the IJN's belated attempt to field radar-directed gunnery comparable to Allied systems. Development began in 1943 after the devastating impact of Allied radar-controlled fire became apparent. The system entered limited production in mid-1944, far too late to affect the war's outcome.

Very few Type 94 sets were actually installed before the war ended. The few ships that received them included the super-battleship Yamato during her final refit, and cruiser Yahagi. The extreme scarcity meant most IJN vessels fought through 1944-1945 relying entirely on optical fire control.

During Operation Ten-Go (April 1945), Yamato's Type 94 radar was used during the sortie toward Okinawa. However, constant American air attacks prevented effective employment of the gunnery radar, as directors were forced to constantly shift between surface and AA targets. The radar's performance in this action, if any, went unrecorded as the ship sank.

The Type 94's 55% reliability was optimistic - actual operational availability was likely lower due to the complete breakdown of Japanese logistics by 1944. Ships that received Type 94 installations often found them non-functional within weeks due to lack of spare parts or trained technicians.

The irony of Type 94's development was that by 1944, the IJN's surface warfare doctrine had collapsed. Most surviving ships were relegated to transport missions or stationary AA platforms. The sophisticated fire control radar arrived just as there were no longer targets to use it against.

Production totaled perhaps 20-30 sets, a negligible number compared to the 1,000+ Mk 37 directors produced by the United States. The Type 94 stands as a symbol of Japan's inability to match Allied technological and industrial capacity.

## Tactical Tips
- **Expect Failures**: With 55% reliability, assume Type 94 will be non-functional more often than not. Maintain optical fire control as your primary method.
- **Wider Beam Advantage**: The 30° beam makes target acquisition easier than Allied narrow-beam systems. Use this to compensate for less skilled operators.
- **Limited Range Tactics**: The 12 km range means you must close to medium ranges before radar fire control is effective. Don't expect long-range radar gunnery.
- **Night Engagement**: Type 94's primary value is night fighting capability. If it's working, press night actions where optical rangefinding is difficult.
- **Backup Optical**: Always have optical rangefinders manned and ready. When (not if) Type 94 fails, immediately fall back to optical fire control.
- **Smoke Screens**: If the enemy deploys smoke, Type 94 can track through it - a significant advantage if the radar is functional.
- **Priority Target**: Since you can only track one target and reliability is poor, choose your target carefully. Focus on the most dangerous enemy ship.
- **Weather Degradation**: Heavy weather reduces range by 22%. In storms, effective range may be only 9 km. Don't rely on Type 94 in bad weather.
- **Slow Updates**: The 2-second update cycle means maneuvering targets are hard to track. Against zig-zagging destroyers, optical tracking may actually be superior.
- **Conservation**: The low power draw (32 kW) means you can keep Type 94 running even on limited power. Better to have it ready if needed.
- **Historical Context**: If playing late-war scenarios (1944-45), having a functional Type 94 is historically rare. Most IJN ships didn't have one at all.
- **Spare Parts Crisis**: In campaign mode, assume Type 94 spare parts are unavailable. Once it breaks, it stays broken unless you reach a major port.
- **Training Deficit**: By 1944, experienced radar operators are scarce in the IJN. Assume operator skill is low, reducing effective performance further.
- **Realistic Expectations**: Type 94 is vastly inferior to Allied FC radars. Don't expect Mk 37 performance - it's a marginal improvement over pure optical fire control, nothing more.
