---
module_id: SON-011
name: Type 3 Sonar
category: support
subcategory: detection-sonar
sonar_type: active
era: 1942
nation: Japan
slot_type: support

# Coverage Mechanics
scan_pattern: scanning
cone_angle: 18           # degrees per beam
sweep_arc: 120           # degrees total (forward arc)
sweep_time: 6            # seconds per sweep
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 2.5  # km
detection_range_passive: 3.5 # km (bearing only)
depth_capability: 180        # meters max depth detection
resolution: 120              # meters
bearing_accuracy: 4          # degrees

# Physical
hull_mounted: true
weight: 2900
power_draw: 24
crew_required: 2
reliability: 78

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 200

tags: [sonar, active, type3, japan, ijn, scanning, limited]
---

# Type 3 Sonar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 3 Active Sonar |
| **Nation** | Japan |
| **Type** | Active/Passive |
| **Scan Pattern** | Scanning (Automatic) |
| **Era** | 1942+ |

## Coverage Pattern
```
Pattern:          Automatic Scanning (Limited)
Beam Width:       18°
Sweep Arc:        120° forward arc
Sweep Time:       6 seconds per complete sweep
Coverage:         Limited forward arc only
```

```
         \   |   /
       60°\  |  /60°
           \ | /
           [Ship]

   Limited 120° Sweep
   Slower Than Allied
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (running) | 2.5km | Adequate range, moderate clarity |
| Submarine (creeping) | 2km | Detectable but weak echo |
| Submarine (stopped) | 1km | Difficult detection |
| Submarine (deep) | 2km | Limited deep capability |
| Torpedo | 0.8km | Basic detection |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 3.5km | Bearing only, adequate sensitivity |
| Submarine (electric) | 2km | Bearing only, limited quiet detection |
| Surface ship | 5km | Bearing only, loud targets |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 90% |
| 10 knots | 72% |
| 15 knots | 55% |
| 20+ knots | 38% |

## Operation
### Passive Mode
Basic hydrophone capability provides bearing-only detection. Adequate for initial contact but less sensitive than Allied systems, reflecting Japan's lower emphasis on ASW technology.

### Active Mode - Limited Scanning
**NARROW ARC**: The Type 3 scans only 120 degrees forward (60° each side of bow), compared to 150-180° on Allied scanning sonars. This narrower arc means less coverage and potential gaps at wider angles.

**How It Works**:
1. Automatic 120° sweep every 6 seconds (slower than Allied)
2. 18° beam width (wider = lower resolution)
3. Forward coverage only, large gaps at beam positions
4. Adequate for basic submarine detection
5. Simplified electronics for easier manufacture

**Coverage Limitation**: 120° arc leaves significant gaps between 60° off bow and beam positions. Submarines approaching from these angles may avoid detection.

**Alert Radius**: When you ping, submarines can hear you at 5km (2x your detection range).

### Slower Refresh Rate
6-second sweep time is slower than Allied sonars (4-5 seconds), meaning contacts update less frequently. Maneuvering submarines have more time to change position between updates.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 2,900 kg |
| Power Draw | 24 kW |
| Crew | 2 operators |
| Reliability | 78% |
| Beam Width | 18° |
| Sweep Arc | 120° |
| Sweep Time | 6 seconds |

## Historical Notes

The Type 3 Sonar represented Japan's entry into automatic scanning sonar technology, introduced in 1942 as the IJN attempted to counter growing American submarine threats. However, the Type 3 reflected Japan's lower priority on ASW - most resources went to offensive weapons and aircraft rather than defensive systems.

The Type 3's limitations were apparent compared to contemporary Allied systems. Its 120-degree arc provided less coverage than British or American sonars, the 6-second sweep was slower, and its 2.5km range was adequate but unexceptional. Lower reliability (78%) meant more maintenance and higher failure rates during extended operations.

Japanese escort doctrine emphasized aggressive tactics and visual observation rather than sophisticated sonar operation. The Type 3 was adequate for basic submarine detection, but Japanese escorts generally lacked the training and experience that Allied crews developed. As American submarines became more aggressive in 1943-44, the Type 3's limitations became increasingly apparent.

Despite these shortcomings, the Type 3 equipped many late-war Japanese escorts and provided basic ASW capability for convoy protection and coastal defense.

## Tactical Tips
- Limited 120° arc means submarines can approach from wider angles
- Slower 6-second sweep allows submarines more maneuver time
- Adequate range (2.5km) but less than Allied equivalents
- Lower reliability means more maintenance requirements
- Best used in combination with visual observation
- Gaps at beam positions (beyond 60° off bow)
- Simplified electronics easier to maintain
- Passive mode adequate for initial detection
- Speed penalty significant (avoid high speeds)
- Less effective against quiet or deep targets
- Combine with depth charges for attack
- Train operators thoroughly to maximize limited capability
