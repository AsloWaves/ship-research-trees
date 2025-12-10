---
module_id: SON-010
name: Sonar QGB
category: support
subcategory: detection-sonar
sonar_type: active
era: 1943
nation: USA
slot_type: support

# Coverage Mechanics
scan_pattern: scanning
cone_angle: 15           # degrees per beam
sweep_arc: 180           # degrees total (forward arc)
sweep_time: 4.5          # seconds per sweep
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 4    # km
detection_range_passive: 5   # km (bearing only)
depth_capability: 250        # meters max depth detection
resolution: 70               # meters
bearing_accuracy: 2          # degrees

# Physical
hull_mounted: true
weight: 3400
crew_required: 2
reliability: 90

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 150

tags: [sonar, active, qgb, usa, usn, scanning, destroyer-escort]
---

# Sonar QGB

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | QGB Scanning Sonar |
| **Nation** | United States |
| **Type** | Active/Passive |
| **Scan Pattern** | Scanning (Automatic) |
| **Era** | 1943+ |

## Coverage Pattern
```
Pattern:          Automatic Scanning
Beam Width:       15°
Sweep Arc:        180° forward arc
Sweep Time:       4.5 seconds per complete sweep
Coverage:         Complete forward hemisphere
```

```
      \     |     /
       \    |    /
    90° \   |   / 90°
         \  |  /
          \ | /
          [Ship]

   Full 180° Forward
   Beam-to-Beam Coverage
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 4km | Excellent range and clarity |
| Submarine (creeping) | 3.5km | Strong detection |
| Submarine (stopped) | 2km | Clear detection |
| Submarine (deep) | 4km | Excellent deep target capability |
| Torpedo | 1.5km | Reliable torpedo detection |
| Mine | 0.8km | Can detect moored mines |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 5km | Bearing only, excellent sensitivity |
| Submarine (electric) | 3km | Bearing only, superior quiet target detection |
| Surface ship | 7km | Bearing only, loud contacts |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 95% |
| 10 knots | 85% |
| 15 knots | 74% |
| 20 knots | 60% |
| 25+ knots | 45% |

## Operation
### Passive Mode
Superior passive hydrophone array provides excellent detection range and sensitivity. US doctrine emphasized passive detection first, allowing approach without alerting submarines.

### Active Mode - Full Forward Scanning
**COMPLETE FORWARD COVERAGE**: The QGB scans a full 180-degree forward arc (beam-to-beam, port to starboard), providing complete coverage ahead of the ship. This eliminates the "edge gaps" present in narrower-arc systems.

**How It Works**:
1. Automatic 180° sweep every 4.5 seconds
2. 15° beam provides good resolution
3. Complete forward hemisphere coverage
4. Multiple contact tracking with high reliability
5. Simplified operator interface reduces errors

**Coverage Advantage**: Full 180° means submarines anywhere ahead are detected - no gaps at beam positions like narrower-arc sonars.

**Alert Radius**: When you ping, submarines can hear you at 8km (2x your detection range).

### High Reliability
The QGB features exceptionally reliable electronics (90%), higher than British equivalents. American manufacturing quality and robust design made the QGB the most dependable WWII scanning sonar.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,400 kg |
| Crew | 2 operators |
| Reliability | 90% |
| Beam Width | 15° |
| Sweep Arc | 180° |
| Sweep Time | 4.5 seconds |
| MTBF | 240 hours |

## Historical Notes

The QGB Sonar was the US Navy's premier WWII escort sonar, equipping destroyer escorts (DEs) and destroyers from 1943 onward. Representing a major improvement over the earlier searchlight QC system, the QGB incorporated scanning technology that the British had pioneered, combined with superior American electronics manufacturing.

The QGB's 180-degree forward coverage provided complete ahead detection, crucial for convoy escort and submarine hunting. American destroyer escorts in the Atlantic used QGB to devastating effect, with some individual ships sinking multiple U-boats. The system's high reliability meant it rarely failed during critical engagements.

The QGB also saw extensive Pacific service, where its reliability in tropical conditions proved superior to British ASDIC. American destroyer escorts protected carrier task forces, hunted Japanese submarines, and provided convoy escort throughout the Pacific theater. The system's two-operator crew reflected American emphasis on automation and simplified operation.

Post-war, the QGB's design influenced the development of more advanced scanning sonars, and some QGB-equipped ships remained in service into the 1960s.

## Tactical Tips
- Full 180° forward coverage eliminates edge gaps
- Excellent for convoy escort (complete forward protection)
- High 90% reliability means dependable operation
- 4.5-second sweep provides rapid contact updates
- Two-operator crew simplifies manning
- Superior passive mode (5km) for initial detection
- Excellent range (4km active) for early contact
- Can detect submarines at beam positions (true 180°)
- Very effective in tropical Pacific conditions
- Reliable electronics reduce maintenance burden
- Multiple contact tracking with clear display
- Best combined with hedgehog for attack
