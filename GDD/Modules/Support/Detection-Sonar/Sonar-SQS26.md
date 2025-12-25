---
module_id: SON-013
name: Sonar SQS-26
category: support
subcategory: detection-sonar
sonar_type: active
era: 1960
nation: USA
slot_type: support

# Coverage Mechanics
scan_pattern: omni
cone_angle: 360          # degrees (omnidirectional)
sweep_arc: 360           # degrees total (all-around)
sweep_time: 1            # seconds (near-continuous)
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 15   # km
detection_range_passive: 20  # km (bearing only)
depth_capability: 600        # meters max depth detection
resolution: 25               # meters
bearing_accuracy: 0.5        # degrees

# Physical
hull_mounted: true
weight: 12000
crew_required: 4
reliability: 94

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 50

tags: [sonar, active, sqs-26, usa, usn, omni, bow-dome, cold-war]
---

# Sonar SQS-26

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | SQS-26 Omnidirectional Sonar |
| **Nation** | United States |
| **Type** | Active/Passive |
| **Scan Pattern** | Omnidirectional (360°) |
| **Era** | 1960+ |

## Coverage Pattern
```
Pattern:          Omnidirectional
Beam Width:       360° simultaneous
Sweep Arc:        360° all-around
Sweep Time:       1 second (near-continuous)
Coverage:         Complete sphere
```

```
       \    |    /
        \   |   /
      ---[Ship]---  360° Complete
        /   |   \   Coverage
       /    |    \

   Bow-Dome Array
   All Directions Simultaneously
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Nuclear submarine | 15km | Full range, loud reactor pumps |
| Diesel submarine (snorkel) | 12km | Strong detection |
| Diesel submarine (battery) | 10km | Excellent quiet detection |
| Submarine (creeping) | 8km | Good even ultra-quiet |
| Submarine (stopped) | 6km | Detectable at significant range |
| Submarine (deep) | 15km | Exceptional deep capability (600m) |
| Torpedo | 5km | Excellent torpedo detection |
| Mine | 2km | Clear mine detection |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Nuclear submarine | 20km | Bearing only, extremely loud |
| Diesel submarine (diesel) | 15km | Bearing only, clear detection |
| Diesel submarine (electric) | 8km | Bearing only, good sensitivity |
| Surface ship | 30km | Bearing only, extreme range |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 10 knots | 94% |
| 15 knots | 88% |
| 20 knots | 80% |
| 25 knots | 70% |
| 30 knots | 58% |
| 35+ knots | 45% |

## Operation
### Passive Mode
Exceptional passive arrays provide 20km+ detection range against nuclear submarines. The SQS-26's passive capability often exceeds active range, making it the primary search mode for Cold War ASW.

### Active Mode - True Omnidirectional
**REVOLUTIONARY DESIGN**: Unlike scanning sonars that sweep a beam, the SQS-26 transmits and receives in ALL directions SIMULTANEOUSLY. This provides complete 360-degree coverage with no blind spots and near-instantaneous contact updates.

**How It Works**:
1. Massive bow-dome houses hundreds of transducer elements
2. All elements transmit simultaneously (omnidirectional ping)
3. Receive arrays detect echoes from all directions
4. Digital beamforming determines bearing to each contact
5. Complete tactical picture updated every second

**No Blind Spots**: Submarines anywhere around the ship are detected - ahead, astern, beam, all positions covered continuously.

**Alert Radius**: When you ping, submarines can hear you at 30km (2x your detection range).

### Advanced Processing
The SQS-26 features sophisticated digital processing:
- **Automatic Target Tracking**: Maintains multiple contact tracks
- **Contact Classification**: Distinguishes submarine types
- **Doppler Processing**: Determines contact speed and course
- **False Contact Rejection**: Filters biologics and clutter
- **Depth Determination**: Estimates target depth from echo

## Specifications
| Spec | Value |
|------|-------|
| Weight | 12,000 kg |
| Crew | 4 operators |
| Reliability | 94% |
| Coverage | 360° omnidirectional |
| Update Rate | 1 second |
| Max Depth | 600m |
| Processing | Full digital |
| Transducers | 400+ elements |

## Historical Notes

The SQS-26 represented a revolutionary advance in sonar technology when it entered service in 1960. Designed specifically for Cold War ASW against Soviet nuclear submarines, the SQS-26 was the first truly omnidirectional active sonar, providing complete spherical coverage without scanning delays.

The system's massive bow-dome became a distinctive feature of American destroyers and frigates. The dome housed hundreds of transducer elements arranged to provide omnidirectional transmission and reception. Digital beamforming allowed the system to determine bearing to contacts in any direction simultaneously, eliminating the blind spots of scanning sonars.

The SQS-26's 15km active range and 20km passive range provided unprecedented detection capability. Against noisy Soviet nuclear submarines, the system could detect contacts at extreme ranges, allowing escort groups to maintain large protective zones around carrier battle groups. The ability to track submarines to 600m depth countered Soviet deep-diving capabilities.

The SQS-26 equipped American destroyers, frigates, and cruisers throughout the Cold War and remained in service into the 1990s on some ships. Its design influenced all subsequent omnidirectional sonar systems.

## Tactical Tips
- Complete 360° coverage eliminates all blind spots
- No scanning delay - all contacts detected simultaneously
- 1-second update rate provides near-real-time tracking
- Exceptional range (15km active, 20km passive)
- Passive mode often detects before active needed
- Can track submarines at any depth to 600m
- Multiple contact tracking for complex scenarios
- Digital processing dramatically reduces false contacts
- High reliability (94%) for extended operations
- Best combined with ASROC for standoff attack
- Massive bow-dome requires hull integration
- Power hungry (75 kW) but worth it
- Speed penalty less severe than WWII/early Cold War systems
- Nuclear submarines very loud - easy detection
- True omnidirectional - no tactical blind spots
