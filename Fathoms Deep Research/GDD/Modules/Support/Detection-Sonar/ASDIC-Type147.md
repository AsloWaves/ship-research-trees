---
module_id: SON-009
name: ASDIC Type 147
category: support
subcategory: detection-sonar
sonar_type: active
era: 1943
nation: UK
slot_type: support

# Coverage Mechanics
scan_pattern: scanning
cone_angle: 14           # degrees per beam
sweep_arc: 160           # degrees total (forward arc)
sweep_time: 4            # seconds per sweep
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 4    # km
detection_range_passive: 5   # km (bearing only)
depth_capability: 250        # meters max depth detection
resolution: 75               # meters
bearing_accuracy: 2          # degrees

# Physical
hull_mounted: true
weight: 3500
power_draw: 32
crew_required: 3
reliability: 88

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 150

tags: [sonar, active, asdic, uk, royal-navy, scanning, hedgehog, squid]
---

# ASDIC Type 147

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | ASDIC Type 147 |
| **Nation** | United Kingdom |
| **Type** | Active/Passive |
| **Scan Pattern** | Scanning (Automatic) |
| **Era** | 1943+ |

## Coverage Pattern
```
Pattern:          Automatic Scanning (Enhanced)
Beam Width:       14°
Sweep Arc:        160° forward arc
Sweep Time:       4 seconds per complete sweep
Coverage:         Wide forward hemisphere
```

```
       \    |    /
        \   |   /
     80° \  |  / 80°
          \ | /
          [Ship]

   Fast 160° Sweep
   Hedgehog/Squid Compatible
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 4km | Excellent range, clear echo |
| Submarine (creeping) | 3.5km | Strong detection |
| Submarine (stopped) | 2km | Good detection even stationary |
| Submarine (deep) | 3.5km | Tracks to 250m depth |
| Torpedo | 1.5km | Improved small-target detection |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 5km | Bearing only, superior sensitivity |
| Submarine (electric) | 3km | Bearing only, quiet targets |
| Surface ship | 7km | Bearing only, very loud |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 94% |
| 10 knots | 84% |
| 15 knots | 72% |
| 20 knots | 58% |
| 25+ knots | 42% |

## Operation
### Passive Mode
Enhanced passive listening array provides superior range and sensitivity compared to Type 144. Often used for initial detection and approach before switching to active prosecution.

### Active Mode - Advanced Scanning
**IMPROVED AUTOMATIC SWEEP**: The Type 147 features faster scanning (4 seconds vs 5 seconds) and slightly wider coverage (160° vs 150°) than the Type 144. More importantly, it provides **continuous tracking** for ahead-throwing weapons.

**How It Works**:
1. Beam sweeps 160° forward arc automatically
2. 14° beam width provides good resolution
3. Complete sweep every 4 seconds (20% faster than Type 144)
4. Enhanced electronics maintain contact during weapon approach
5. **Does NOT lose contact** when attacking with Hedgehog/Squid

**Key Advantage**: Earlier ASDIC lost contact as the ship passed over the submarine (dead zone beneath ship). Type 147 maintains tracking throughout Hedgehog/Squid attack.

**Alert Radius**: When you ping, submarines can hear you at 8km (2x your detection range).

### Ahead-Throwing Weapon Integration
The Type 147 was specifically designed to work with Hedgehog and Squid ahead-throwing weapons:
- **Maintains contact** during approach
- **No dead zone** during attack
- **Fire control data** automatically calculated
- **Continuous tracking** through weapon flight

## Specifications
| Spec | Value |
|------|-------|
| Weight | 3,500 kg |
| Power Draw | 32 kW |
| Crew | 3 operators |
| Reliability | 88% |
| Beam Width | 14° |
| Sweep Arc | 160° |
| Sweep Time | 4 seconds |
| Fire Control | Integrated |

## Historical Notes

The ASDIC Type 147 was developed in 1943 specifically to support ahead-throwing weapons like Hedgehog and Squid. Earlier ASDIC systems had a critical flaw - they lost contact as the attacking ship passed over the submarine, forcing escorts to drop depth charges blindly in the last known position.

Hedgehog and Squid fired forward of the ship, allowing the escort to maintain sonar contact throughout the attack. But this required sonar that could track continuously during the approach and provide fire control data. The Type 147 solved this problem with improved electronics and integrated fire control.

The system proved devastatingly effective. Hedgehog attacks with Type 147 guidance achieved kill rates of over 30%, compared to under 5% for traditional depth charge attacks. The combination of continuous tracking and accurate ahead-throwing weapons represented the pinnacle of WWII ASW technology.

Late-war River-class frigates and Castle-class corvettes carried the Type 147/Squid combination, making them the most effective U-boat hunters of the war.

## Tactical Tips
- 4-second sweep provides 20% faster contact updates than Type 144
- Wider 160° arc improves coverage
- **Essential for Hedgehog/Squid attacks** - maintains contact throughout
- Three operators provide fire control calculations
- Excellent 4km range for early detection
- Superior passive mode (5km) for stealthy approach
- No dead zone during ahead-throwing weapon attacks
- Can engage without passing over submarine
- Much higher kill probability than depth charge attacks
- Integrated fire control reduces operator workload
- Faster sweep helps track maneuvering submarines
- Best combined with Hedgehog or Squid
