---
module_id: SON-004
name: Type 93 Hydrophone
category: support
subcategory: detection-sonar
sonar_type: passive
era: 1940
nation: Japan
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
detection_range_passive: 3.5 # km (bearing only)
depth_capability: 180        # meters max depth detection
resolution: 400              # meters
bearing_accuracy: 8          # degrees

# Physical
hull_mounted: true
weight: 650
crew_required: 1
reliability: 82

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 100

tags: [sonar, passive, hydrophone, japan, ijn, submarine, type93]
---

# Type 93 Hydrophone

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Type 93 Passive Hydrophone |
| **Nation** | Japan |
| **Type** | Passive |
| **Scan Pattern** | Omnidirectional |
| **Era** | 1940+ |

## Coverage Pattern
```
Pattern:          Omnidirectional
Beam Width:       360°
Sweep Arc:        360° all-around
Sweep Time:       Continuous
Coverage:         Complete horizontal plane
```

```
      [I-Class]
         |||
    -----------  360° Passive
     Simple Array
   (12 elements)
```

## Detection Performance

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Destroyer (running) | 3.5km | Bearing only, adequate detection |
| Cargo vessel | 4km | Bearing only, loud machinery |
| Submarine (diesel) | 3km | Bearing only, limited sensitivity |
| Submarine (electric) | 1.5km | Bearing only, difficult detection |
| Torpedo | 2km | Basic warning capability |
| Task force | 5km | Multiple contacts |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 5 knots | 88% |
| 10 knots | 68% |
| 15 knots | 48% |
| 20+ knots | 28% |

## Operation
### Passive Mode
The Type 93 Hydrophone is the standard passive sonar for Japanese submarines during WWII. While adequate for basic underwater detection, it represents a simpler design compared to contemporary American and German systems, reflecting Japan's focus on torpedo technology over detection systems.

**Design Characteristics**:
- **Basic Array**: 12 hydrophone elements
- **Simple Electronics**: Reliable but limited processing
- **Single Operator**: Minimal crew requirement
- **Compact Design**: Fits smaller Japanese submarines

**Gameplay**: Type 93 provides basic bearing-only detection with moderate range. Adequate for submarine operations but inferior to Allied equivalents. Best used in conjunction with visual observation and aggressive tactics.

### Operator Function
Type 93 operators provide:
- Basic bearing to contacts
- Simple contact classification (large/small)
- Torpedo warnings
- Limited multiple-contact tracking
- Speed estimation (approximate)

## Specifications
| Spec | Value |
|------|-------|
| Weight | 650 kg |
| Crew | 1 operator |
| Reliability | 82% |
| Array Elements | 12 hydrophones |

## Historical Notes

The Type 93 Hydrophone equipped most Japanese submarines during the Pacific War, but it reflected Japan's tactical philosophy that emphasized offensive power (the excellent Type 95 torpedo) over defensive sensors. Japanese submarine doctrine focused on fleet operations and aggressive surface attacks rather than cautious submerged approaches.

In practice, this meant Japanese submarines often operated on the surface using visual observation, relying on their high speed and powerful torpedoes. The Type 93 was adequate for basic underwater detection and provided essential torpedo warnings, but Japanese sonarmen generally had less training and experience than their American counterparts.

The system's limitations became apparent in 1943-44 when American destroyer escorts with superior sonar began hunting Japanese submarines aggressively. The Type 93's shorter range and lower resolution made it difficult for Japanese submarines to detect threats early enough to evade.

## Tactical Tips
- Adequate for basic submarine operations
- Best used at very slow speeds (under 5 knots)
- Shorter range means less warning time against escorts
- Supplement with visual observation when possible
- Less effective in Pacific thermal layers than Allied systems
- Focus on aggressive surface tactics rather than cautious stalking
- Provides basic torpedo warning but with less range
- Reliability issues in extended patrols
- Train operators thoroughly to maximize limited capability
