---
module_id: SON-007
name: ASDIC Type 127
category: support
subcategory: detection-sonar
sonar_type: active
era: 1942
nation: UK
slot_type: support

# Coverage Mechanics
scan_pattern: searchlight
cone_angle: 15           # degrees per beam
sweep_arc: 15            # degrees total (must manually aim)
sweep_time: 0            # seconds per sweep (continuous in aimed direction)
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 2    # km
detection_range_passive: 3   # km (bearing only)
depth_capability: 250        # meters max depth detection
resolution: 50               # meters (excellent)
bearing_accuracy: 2          # degrees

# Physical
hull_mounted: true
weight: 2600
power_draw: 20
crew_required: 3
reliability: 83

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 150

tags: [sonar, active, asdic, uk, royal-navy, searchlight, depth-finding]
---

# ASDIC Type 127

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | ASDIC Type 127 |
| **Nation** | United Kingdom |
| **Type** | Active/Passive |
| **Scan Pattern** | Searchlight (Manual Aim) |
| **Era** | 1942+ |

## Coverage Pattern
```
Pattern:          Searchlight with Depth-Finding
Beam Width:       15°
Sweep Arc:        15° (manual aim required)
Sweep Time:       Continuous in aimed direction
Coverage:         Narrow cone, excellent depth resolution
```

```
        [Ship]
          |
          | 15° Narrow Beam
         /|\  (Depth-Finding)
        / | \
       /  |  \
      /   |   \
     Horizontal +
     Vertical Scan
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 2km | Full range, excellent depth data |
| Submarine (creeping) | 1.8km | Clear echo with depth |
| Submarine (stopped) | 1.2km | Weak but depth accurate |
| Submarine (deep) | 2km | Can track to 250m depth |
| Torpedo | 0.6km | Difficult but possible |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 3km | Bearing only, good sensitivity |
| Submarine (electric) | 2km | Bearing only, quiet |
| Surface ship | 5km | Bearing only, loud |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 92% |
| 10 knots | 78% |
| 15 knots | 60% |
| 20+ knots | 42% |

## Operation
### Passive Mode
Standard hydrophone listening mode for initial detection without alerting target. Operators begin searches passively to locate submarine bearing.

### Active Mode - Depth Finding
**UNIQUE CAPABILITY**: The Type 127 is specifically designed for **depth determination**. Unlike earlier ASDIC that could only provide bearing and range, the Type 127 uses a narrower beam with vertical scanning to determine target depth.

**Manual Aim with Depth Scan**:
1. Operator aims 15° beam at contact bearing
2. Transducer can tilt vertically to scan depth layers
3. Ping transmitted, echo analyzed
4. **Range, Bearing, AND Depth** displayed
5. Data used for accurate depth charge settings

**Critical for Weapons**: Deep-diving submarines (German Type VII could reach 200m) required accurate depth data for effective depth charge attacks. The Type 127 provided this crucial information.

**Alert Radius**: When you ping, submarines hear you at 4km (2x your detection range).

### Three-Operator Crew
- **Primary Operator**: Controls bearing and triggers pings
- **Depth Operator**: Controls vertical scanning and depth analysis
- **Recorder**: Logs contacts and provides tactical plot

## Specifications
| Spec | Value |
|------|-------|
| Weight | 2,600 kg |
| Power Draw | 20 kW |
| Crew | 3 operators |
| Reliability | 83% |
| Beam Width | 15° horizontal |
| Vertical Scan | ±30° |
| Depth Resolution | 10 meters |
| Max Tracking Depth | 250m |

## Historical Notes

The ASDIC Type 127 was developed in 1942 specifically to counter deep-diving German U-boats. Early in WWII, U-boat commanders discovered they could escape depth charge attacks by diving deep - often below 150 meters. Standard ASDIC could track range and bearing but not depth, forcing escort commanders to guess depth charge settings.

The Type 127 solved this problem with a revolutionary depth-finding capability. By using a narrower beam and vertical scanning, the system could determine target depth with 10-meter accuracy. This allowed escorts to set depth charges precisely, dramatically increasing kill probability.

The system required a third operator to manage depth scanning, but this was considered worthwhile given the improved effectiveness. Type 127 equipped many late-war frigates and destroyers. The narrow 15-degree beam made sector searching slower than wider-beam systems, but the accurate depth data was invaluable during attack runs.

## Tactical Tips
- Use passive mode for initial detection
- Narrow 15° beam means slower sector searches
- **Depth data is the key advantage** - know exactly where target is
- Allows precise depth charge depth settings
- Essential against deep-diving submarines
- Three operators provide excellent contact management
- Slower sweeping than Type 123 or QC
- Once contact established, depth scanning is rapid
- Combine with depth charges set to exact target depth
- Can track submarines diving below 200m
- Excellent resolution (50m) for fire control
- Best used during final attack approach, not initial search
