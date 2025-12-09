---
module_id: SON-005
name: ASDIC Type 123
category: support
subcategory: detection-sonar
sonar_type: active
era: 1935
nation: UK
slot_type: support

# Coverage Mechanics
scan_pattern: searchlight
cone_angle: 20           # degrees per beam
sweep_arc: 20            # degrees total (must manually aim)
sweep_time: 0            # seconds per sweep (continuous in aimed direction)
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 1.5  # km
detection_range_passive: 2.5 # km (bearing only)
depth_capability: 150        # meters max depth detection
resolution: 100              # meters
bearing_accuracy: 3          # degrees

# Physical
hull_mounted: true
weight: 2200
power_draw: 18
crew_required: 2
reliability: 80

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 200

tags: [sonar, active, asdic, uk, royal-navy, searchlight, early]
---

# ASDIC Type 123

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | ASDIC Type 123 |
| **Nation** | United Kingdom |
| **Type** | Active/Passive |
| **Scan Pattern** | Searchlight (Manual Aim) |
| **Era** | 1935+ |

## Coverage Pattern
```
Pattern:          Searchlight
Beam Width:       20°
Sweep Arc:        20° (manual aim required)
Sweep Time:       Continuous in aimed direction
Coverage:         Narrow cone, operator controlled
```

```
        [Ship]
          |
          |  20° Beam
         /|\  (Manual Aim)
        / | \
       /  |  \
      /   |   \
     Must Manually
     Search Area
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 1.5km | Full range, clear echo |
| Submarine (creeping) | 1.2km | Weaker echo |
| Submarine (stopped) | 0.8km | Difficult, weak return |
| Torpedo | 0.5km | Very difficult |
| Large wreck | 1.5km | Strong return |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 2.5km | Bearing only, passive listening |
| Submarine (electric) | 1.5km | Bearing only, very quiet |
| Surface ship | 4km | Bearing only, loud |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 92% |
| 10 knots | 78% |
| 15 knots | 60% |
| 20+ knots | 40% |

## Operation
### Passive Mode
Silent listening mode using the ASDIC transducer as a hydrophone. Provides bearing-only information without alerting the target. Operators typically begin searches in passive mode to detect submarine general location.

### Active Mode
**MANUAL AIM REQUIRED**: The Type 123 uses a narrow 20-degree beam that must be manually aimed by the operator. The operator rotates the transducer to sweep different bearings, transmitting a "ping" and listening for echoes.

**Critical Limitation**: Only covers where you're looking! Easy to miss submarines outside the narrow beam. Operators must systematically sweep sectors to search an area.

**Alert Radius**: When you ping, submarines can hear you at 3km (2x your detection range).

### Manual Aim Operation
1. Operator selects bearing to search
2. Transducer rotates to aimed bearing (2-3 seconds)
3. Ping transmitted in narrow cone
4. Listen for echo (takes 2-10 seconds depending on range)
5. If no contact, select new bearing and repeat

## Specifications
| Spec | Value |
|------|-------|
| Weight | 2,200 kg |
| Power Draw | 18 kW |
| Crew | 2 operators |
| Reliability | 80% |
| Beam Width | 20° |
| Ping Interval | 5-8 seconds |

## Historical Notes

The ASDIC Type 123 was the Royal Navy's first practical active sonar system, entering service in the mid-1930s. Named after the "Anti-Submarine Detection Investigation Committee," ASDIC was considered a revolutionary solution to the U-boat threat that had nearly strangled Britain in WWI.

The Type 123's searchlight pattern reflected the limited technology of the era. With a narrow 20-degree beam, operators had to manually aim the transducer and systematically search sectors. This made it relatively easy for submarines to slip past if not directly in the beam path. The system also suffered from a "dead zone" directly beneath the ship and struggled to detect submarines at different depths.

Despite limitations, the Type 123 represented a massive improvement over pure hydrophone listening. For the first time, surface ships could determine both bearing AND range to submerged submarines, enabling accurate depth charge attacks. Early war optimism about ASDIC's effectiveness proved overstated, but it remained a crucial ASW tool when combined with proper tactics.

## Tactical Tips
- Start in passive mode to locate general bearing
- Switch to active for attack approach (target already alerted)
- Narrow beam means systematic sector searching required
- Very easy to miss submarines outside the 20° cone
- Slow speed (under 10 knots) crucial for detection
- Ping alerts target at 2x your detection range
- Two operators allow continuous operation (one aims, one listens)
- Thermal layers completely block detection
- Best combined with depth charges for attack
- Lost contact? Return to passive mode and relocate
