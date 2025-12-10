---
module_id: SON-001
name: Basic Hydrophone
category: support
subcategory: detection-sonar
sonar_type: passive
era: 1915
nation: Universal
slot_type: support

# Coverage Mechanics
scan_pattern: omni
cone_angle: 360           # degrees per beam
sweep_arc: 360           # degrees total (all-around)
sweep_time: 0            # seconds per sweep (continuous)
modes: [passive]
default_mode: passive

# Performance
detection_range_active: 0    # km (not active capable)
detection_range_passive: 3   # km (bearing only)
depth_capability: 150        # meters max depth detection
resolution: 500              # meters
bearing_accuracy: 10         # degrees

# Physical
hull_mounted: true
weight: 500
crew_required: 1
reliability: 85

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 100

tags: [sonar, passive, hydrophone, universal, wwi, basic]
---

# Basic Hydrophone

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Basic Hydrophone |
| **Nation** | Universal |
| **Type** | Passive |
| **Scan Pattern** | Omnidirectional |
| **Era** | 1915+ |

## Coverage Pattern
```
Pattern:          Omnidirectional
Beam Width:       360°
Sweep Arc:        360° all-around
Sweep Time:       Continuous
Coverage:         Complete horizontal plane
```

```
        [Ship]
          |
    ------+------  360° Listening
          |
     (Passive Only)
```

## Detection Performance

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 3km | Bearing only, loud engines |
| Submarine (electric) | 1.5km | Bearing only, very quiet |
| Surface ship | 5km | Very loud, easy detect |
| Torpedo | 2km | High-speed screws distinctive |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 90% |
| 10 knots | 70% |
| 15 knots | 50% |
| 20+ knots | 30% |

## Operation
### Passive Mode
Silent listening device that detects underwater sounds without revealing the listener's position. The hydrophone operator listens for propeller noise, machinery sounds, and torpedo motors. Provides bearing information only - the direction to the sound, but not the distance.

**Key Gameplay**: Shows bearing lines (like spokes) pointing toward contacts. Must triangulate with movement or multiple ships to determine range.

### Operator Skills
Trained operators can:
- Classify contacts by sound signature
- Count propeller blades by acoustic pattern
- Estimate target speed from screw RPM
- Distinguish multiple simultaneous contacts
- Identify torpedo warnings

## Specifications
| Spec | Value |
|------|-------|
| Weight | 500 kg |
| Crew | 1 operator |
| Reliability | 85% |

## Historical Notes

The Basic Hydrophone represents the earliest underwater detection technology, developed during WWI as navies struggled to counter the submarine threat. Simple hydrophones were essentially underwater microphones that amplified sounds transmitted through water. British, German, and American navies all deployed similar systems.

Early hydrophones were crude - operators literally listened with headphones to the sounds of the ocean, trying to distinguish submarine propellers from whales, fishing boats, and their own ship's machinery. Despite limitations, hydrophones provided the only practical means of detecting submerged submarines before active sonar development.

## Tactical Tips
- Stop or slow to minimum speed for best detection
- Own ship noise masks distant contacts
- Bearing-only means you need movement to triangulate
- Thermal layers can hide deep submarines
- Completely passive - target has no idea you're listening
- Essential for submarine vs submarine combat
- Use multiple ships to triangulate contact position
