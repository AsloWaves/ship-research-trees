---
module_id: SON-006
name: Sonar QC
category: support
subcategory: detection-sonar
sonar_type: active
era: 1940
nation: USA
slot_type: support

# Coverage Mechanics
scan_pattern: searchlight
cone_angle: 25           # degrees per beam
sweep_arc: 25            # degrees total (must manually aim)
sweep_time: 0            # seconds per sweep (continuous in aimed direction)
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 2.5  # km
detection_range_passive: 3   # km (bearing only)
depth_capability: 200        # meters max depth detection
resolution: 80               # meters
bearing_accuracy: 2.5        # degrees

# Physical
hull_mounted: true
weight: 2800
crew_required: 2
reliability: 85

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 150

tags: [sonar, active, qc, usa, usn, searchlight, destroyer]
---

# Sonar QC

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | QC Sonar |
| **Nation** | United States |
| **Type** | Active/Passive |
| **Scan Pattern** | Searchlight (Manual Aim) |
| **Era** | 1940+ |

## Coverage Pattern
```
Pattern:          Searchlight
Beam Width:       25°
Sweep Arc:        25° (manual aim required)
Sweep Time:       Continuous in aimed direction
Coverage:         Narrow cone, operator controlled
```

```
        [Ship]
          |
          |  25° Beam
         /|\  (Manual Aim)
        / | \
       /  |  \
      /   |   \
     /    |    \
    Wider Than UK
    ASDIC Type 123
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 2.5km | Full range, strong echo |
| Submarine (creeping) | 2km | Clear echo |
| Submarine (stopped) | 1.2km | Weak return, difficult |
| Torpedo | 0.8km | Small target |
| Large whale | 2km | Can cause false contacts |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 3km | Bearing only, passive listening |
| Submarine (electric) | 2km | Bearing only, quiet |
| Surface ship | 5km | Bearing only, loud machinery |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 93% |
| 10 knots | 80% |
| 15 knots | 65% |
| 20 knots | 48% |
| 25+ knots | 35% |

## Operation
### Passive Mode
Silent hydrophone mode for initial detection without alerting targets. The QC provides better passive range than early British systems, allowing US destroyers to detect submarines before beginning active searches.

### Active Mode
**MANUAL AIM REQUIRED**: The QC uses a 25-degree searchlight beam that must be manually aimed by the operator. Slightly wider than British ASDIC Type 123, making sector searches somewhat faster, but still requires systematic sweeping.

**Improved Range**: At 2.5km active range, the QC provides better detection than early British systems, reflecting improved electronics and more powerful transmitters.

**Alert Radius**: When you ping, submarines can hear you at 5km (2x your detection range).

### Manual Aim Operation
1. Operator selects target bearing
2. Transducer trains to bearing (2 seconds)
3. Powerful ping transmitted
4. Listen for echo return
5. Range and bearing displayed to operator
6. Manually sweep to adjacent sector

**Faster Sweeping**: 25° beam allows fewer steps to cover forward arc than 20° beam systems.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 2,800 kg |
| Crew | 2 operators |
| Reliability | 85% |
| Beam Width | 25° |
| Ping Interval | 4-6 seconds |
| Max Depth | 200m |

## Historical Notes

The QC Sonar was the US Navy's primary early-war active sonar system, equipping destroyers and destroyer escorts in 1940-1943. Developed independently from British ASDIC, the QC incorporated lessons from British experience while using American electronics and manufacturing techniques.

The QC's 25-degree beam was slightly wider than the British Type 123's 20-degree cone, representing a deliberate choice to balance detection range with coverage area. American doctrine emphasized aggressive prosecution of contacts, so the ability to sweep sectors faster was valued over absolute maximum range.

US destroyer escorts used the QC effectively in the Atlantic, where it proved reliable and maintainable. The system's main limitation remained the searchlight pattern - submarines could slip between sonar sweeps if operators weren't methodical. By 1943, the improved scanning-pattern QGB began replacing QC systems on newer ships.

## Tactical Tips
- Begin in passive mode for stealthy initial detection
- Switch to active once contact bearing is known
- 25° beam covers forward arc in 15 steps (7 each side of bow)
- Systematic sector searching prevents gaps in coverage
- Excellent range for WWII searchlight sonar
- Two-operator crew allows continuous operation
- Better reliability than British equivalents
- Ping alerts submarines at considerable range (5km)
- Thermal layers remain a significant limitation
- Best speed for detection: 10-15 knots
- Combine with hedgehog or depth charges for attack
- Lost contact? Drop speed and return to passive mode
