---
module_id: SON-014
name: Towed Array Sonar
category: support
subcategory: detection-sonar
sonar_type: towed
era: 1970
nation: USA
slot_type: support

# Coverage Mechanics
scan_pattern: omni
cone_angle: 360          # degrees (omnidirectional)
sweep_arc: 360           # degrees total (emphasis on stern)
sweep_time: 0            # seconds (continuous)
modes: [passive]
default_mode: passive

# Performance
detection_range_active: 0    # km (passive only)
detection_range_passive: 30  # km (bearing only)
depth_capability: 800        # meters max depth detection
resolution: 50               # meters
bearing_accuracy: 1          # degrees

# Physical
hull_mounted: false
weight: 4500
power_draw: 25
crew_required: 2
reliability: 88

# Limitations
own_speed_penalty: true
thermal_layer_blocked: false
min_range: 500

tags: [sonar, passive, towed-array, usa, usn, long-range, modern]
---

# Towed Array Sonar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | AN/SQR-19 Towed Array |
| **Nation** | United States |
| **Type** | Passive Only |
| **Scan Pattern** | Omnidirectional (Passive) |
| **Era** | 1970+ |

## Coverage Pattern
```
Pattern:          Omnidirectional Passive
Beam Width:       360° (emphasis astern)
Sweep Arc:        360° all-around
Sweep Time:       Continuous
Coverage:         Complete passive coverage
```

```
    [Ship]
      |
      |  ~~~~~~~~  300m Cable
      |
    [Array]  <--- Hydrophones
      |||
   360° Passive
   Behind Ship
```

## Detection Performance

### Passive Mode ONLY
| Target | Range | Notes |
|--------|-------|-------|
| Nuclear submarine (reactor) | 30km | Bearing only, exceptional range |
| Nuclear submarine (quiet) | 20km | Bearing only, excellent detection |
| Diesel submarine (snorkel) | 18km | Bearing only, strong detection |
| Diesel submarine (battery) | 12km | Bearing only, good quiet detection |
| Surface ship | 40km+ | Bearing only, extreme range |
| Torpedo | 8km | Bearing only, early warning |

**NO ACTIVE MODE**: Towed array is purely passive. Cannot ping for range information.

## Speed Penalty
| Own Speed | Detection Modifier | Deployment |
|-----------|-------------------|------------|
| Stopped | 100% | Deployed |
| 5 knots | 98% | Deployed |
| 10 knots | 95% | Deployed |
| 15 knots | 88% | Deployed |
| 20 knots | 70% | Deployed |
| 25 knots | 40% | Retrieving |
| 30+ knots | 0% | Must retrieve |

**Critical Limitation**: Towed array must be retrieved at speeds above 25 knots. Deployment/retrieval takes several minutes.

## Operation
### Passive Mode - Long-Range Detection
**PASSIVE ONLY**: The towed array is purely passive - it listens but never transmits. This makes it completely stealthy - targets have no idea they're being detected.

**How It Works**:
1. 300-meter cable towed behind ship
2. Array contains dozens of hydrophones
3. Far behind ship = away from own propeller noise
4. Exceptional sensitivity to low-frequency sounds
5. Can detect submarines beyond horizon

**Key Advantages**:
- **Extreme Range**: 30km+ passive detection
- **Completely Stealthy**: Target never knows
- **Below Own Noise**: Towed far astern, away from propellers
- **Low Frequency**: Detects long-range submarine sounds
- **Thermal Layer Penetration**: Low frequencies bend around layers

**Key Disadvantages**:
- **Passive Only**: No range information, bearing only
- **Speed Limited**: Must retrieve above 25 knots
- **Deployment Time**: Takes 5-10 minutes to deploy/retrieve
- **Minimum Range**: Poor detection close to ship (500m+)
- **No Active Capability**: Cannot ping for range

### Deployment States
1. **Stowed**: Array winched tight to hull, inactive
2. **Deploying**: Cable paying out, takes 5 minutes
3. **Deployed**: Array 300m astern, fully operational
4. **Retrieving**: Winching in, takes 8 minutes

**Tactical Note**: Must plan ahead - cannot deploy instantly during combat.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 4,500 kg (array + winch) |
| Power Draw | 25 kW |
| Crew | 2 operators |
| Reliability | 88% |
| Array Length | 60m |
| Cable Length | 300m |
| Hydrophones | 48 elements |
| Frequency Range | Very low frequency |

## Historical Notes

Towed array sonars revolutionized Cold War submarine detection in the 1970s. The concept was simple but brilliant: tow hydrophones far behind the ship, away from its own propeller noise, allowing detection of quiet submarines at extreme ranges.

The AN/SQR-19 was the first American towed array system, entering service in 1970. Its ability to detect Soviet nuclear submarines at 30+ kilometers provided unprecedented early warning. The system's low-frequency hydrophones could hear submarine reactor cooling pumps and machinery at ranges impossible for hull-mounted sonars.

Towed arrays proved so effective that they became standard equipment on all American frigates, destroyers, and ASW ships. The main tactical challenge was the speed limitation - ships had to maintain moderate speed (under 20 knots) for optimal detection, and rapid maneuvers required retrieving the array first.

The system's purely passive nature meant it provided bearing-only information. Ships had to maneuver over time to triangulate range, or use other sensors (hull sonar, helicopters) to complete the targeting solution. Despite this limitation, the towed array's extreme detection range made it invaluable for Cold War ASW.

Modern towed arrays have grown even longer (some over 1km) and more sophisticated, but the basic concept remains the same.

## Tactical Tips
- **Extreme passive range** (30km+) - best long-range detector
- **Completely stealthy** - target never knows you're listening
- Deploy BEFORE combat expected (takes 5 minutes)
- Must retrieve for high-speed operations (25+ knots)
- Bearing only - use multiple ships to triangulate
- Best at slow/moderate speeds (10-15 knots)
- Can detect through thermal layers
- No active mode - combine with hull sonar for ranging
- Excellent for initial detection at extreme range
- Poor at close range (500m minimum)
- Plan deployments - not instant-on capability
- Nuclear submarines very loud - easy 30km detection
- Diesel submarines on battery harder but still 12km+
- Two operators manage deployment and contact tracking
- Vulnerable to damage if not retrieved before high speed
