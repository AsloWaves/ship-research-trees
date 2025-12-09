---
module_id: SON-008
name: ASDIC Type 144
category: support
subcategory: detection-sonar
sonar_type: active
era: 1940
nation: UK
slot_type: support

# Coverage Mechanics
scan_pattern: scanning
cone_angle: 12           # degrees per beam
sweep_arc: 150           # degrees total (forward arc)
sweep_time: 5            # seconds per sweep
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 3    # km
detection_range_passive: 4   # km (bearing only)
depth_capability: 200        # meters max depth detection
resolution: 100              # meters
bearing_accuracy: 3          # degrees

# Physical
hull_mounted: true
weight: 3200
power_draw: 28
crew_required: 2
reliability: 86

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 200

tags: [sonar, active, asdic, uk, royal-navy, scanning, wwii-standard]
---

# ASDIC Type 144

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | ASDIC Type 144 |
| **Nation** | United Kingdom |
| **Type** | Active/Passive |
| **Scan Pattern** | Scanning (Automatic) |
| **Era** | 1940+ |

## Coverage Pattern
```
Pattern:          Automatic Scanning
Beam Width:       12°
Sweep Arc:        150° forward arc
Sweep Time:       5 seconds per complete sweep
Coverage:         Automatic forward hemisphere
```

```
       \    |    /
        \   |   /
     75° \  |  / 75°
          \ | /
          [Ship]

   Automatic 150° Sweep
   Updates Every 5 Seconds
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 3km | Clear echo, full range |
| Submarine (creeping) | 2.5km | Good detection |
| Submarine (stopped) | 1.5km | Weak echo but detectable |
| Torpedo | 1km | Fast-moving small target |
| Large wreck | 3km | Strong permanent return |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 4km | Bearing only, excellent range |
| Submarine (electric) | 2.5km | Bearing only, quiet operation |
| Surface ship | 6km | Bearing only, very loud |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 93% |
| 10 knots | 82% |
| 15 knots | 68% |
| 20 knots | 52% |
| 25+ knots | 38% |

## Operation
### Passive Mode
Omnidirectional passive listening for initial detection. The Type 144 features excellent passive capabilities, allowing escorts to detect submarines without alerting them before beginning active prosecution.

### Active Mode - Automatic Scanning
**AUTOMATIC SWEEP**: Unlike earlier searchlight ASDIC, the Type 144 automatically sweeps a 150-degree forward arc without manual operator intervention. This revolutionary improvement dramatically increased detection probability.

**How It Works**:
1. Beam automatically sweeps left to right (75° port to 75° starboard)
2. 12° beam transmits ping at each position
3. Complete sweep takes 5 seconds
4. Contacts updated each time beam passes their position
5. Operator sees all contacts in forward arc

**Coverage**: 150° forward arc means excellent coverage ahead of ship, but **no detection astern**. Submarines behind the ship remain undetected.

**Alert Radius**: When you ping, submarines can hear you at 6km (2x your detection range).

### Contact Refresh Rate
Each contact is refreshed every 5 seconds as the beam sweeps past. Fast-moving submarines can maneuver between sweeps, so operators must track contact motion.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,200 kg |
| Power Draw | 28 kW |
| Crew | 2 operators |
| Reliability | 86% |
| Beam Width | 12° |
| Sweep Arc | 150° |
| Sweep Time | 5 seconds |
| Coverage | Forward hemisphere only |

## Historical Notes

The ASDIC Type 144 was the Royal Navy's standard WWII escort sonar, representing a massive improvement over earlier searchlight systems. Introduced in 1940, the Type 144's automatic scanning meant operators no longer had to manually sweep sectors - the system did it automatically, dramatically reducing operator workload and increasing detection probability.

The Type 144 equipped hundreds of British corvettes, frigates, and destroyers during the Battle of the Atlantic. Its 3km range and automatic 150-degree sweep made it far more effective than the earlier Type 123. Operators could detect multiple submarines simultaneously and maintain continuous tracking during approach.

The system's main limitation was the lack of rear coverage - submarines could escape by passing astern of the hunting ship. Escort groups learned to coordinate, with one ship maintaining contact while others attacked from different angles. The Type 144's reliability and effectiveness made it the backbone of Allied ASW efforts from 1940-1945.

## Tactical Tips
- Automatic scanning eliminates manual sweep workload
- Forward 150° arc provides excellent ahead coverage
- **No rear coverage** - submarines can escape astern
- 5-second refresh rate means contacts update continuously
- Excellent for convoy escort (forward arc covers threats ahead)
- Multiple contacts tracked simultaneously
- Use passive mode for initial detection
- Switch to active for prosecution
- Speed over 15 knots degrades detection significantly
- Coordinate with other escorts to cover all angles
- Submarine behind ship? Turn to bring into forward arc
- Best WWII escort sonar for reliability and coverage
