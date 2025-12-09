---
module_id: SON-003
name: JP Hydrophone
category: support
subcategory: detection-sonar
sonar_type: passive
era: 1940
nation: USA
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
detection_range_passive: 4   # km (bearing only)
depth_capability: 200        # meters max depth detection
resolution: 350              # meters
bearing_accuracy: 7          # degrees

# Physical
hull_mounted: true
weight: 720
power_draw: 7
crew_required: 1
reliability: 88

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 75

tags: [sonar, passive, hydrophone, usa, usn, submarine, jp]
---

# JP Hydrophone

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | JP Passive Array |
| **Nation** | USA |
| **Type** | Passive |
| **Scan Pattern** | Omnidirectional Array |
| **Era** | 1940+ |

## Coverage Pattern
```
Pattern:          Omnidirectional Array
Beam Width:       360°
Sweep Arc:        360° all-around
Sweep Time:       Continuous
Coverage:         Complete horizontal plane
```

```
      [Submarine]
         |||
    -----------  360° Passive
      Bow Array
   (16 elements)
```

## Detection Performance

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Destroyer (running) | 4km | Bearing only, clear detection |
| Merchant vessel | 5km | Bearing only, loud engines |
| Submarine (diesel) | 3.5km | Bearing only, good sensitivity |
| Submarine (electric) | 2km | Bearing only, quiet operation |
| Torpedo | 2.5km | High-speed detection |
| Task force | 6km | Multiple loud contacts |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 4 knots | 90% |
| 8 knots | 75% |
| 12 knots | 55% |
| 16+ knots | 35% |

## Operation
### Passive Mode
The JP Hydrophone is the standard passive sonar array for US submarines during WWII. Featuring 16 hydrophone elements arranged in the submarine's bow, the JP provides excellent passive detection capability for hunting enemy shipping and avoiding escorts.

**Design Features**:
- **Bow-Mounted Array**: 16 elements for good directionality
- **Streamlined Housing**: Minimal hydrodynamic impact
- **Single Operator**: Efficient manning for submarine operations
- **Reliable Electronics**: Rugged construction for Pacific operations

**Gameplay**: JP shows accurate bearing lines to contacts with good range. Optimal for submarine patrol and convoy approach. Less sophisticated than German GHG but more reliable in tropical conditions.

### Operator Capabilities
JP operators are trained to:
- Detect and classify surface contacts
- Identify destroyer screw patterns
- Provide torpedo warnings
- Track multiple contacts in bearing
- Estimate contact speed from sound

## Specifications
| Spec | Value |
|------|-------|
| Weight | 720 kg |
| Power Draw | 7 kW |
| Crew | 1 operator |
| Reliability | 88% |
| Array Elements | 16 hydrophones |

## Historical Notes

The JP Hydrophone equipped American fleet submarines throughout the Pacific War. While not as sophisticated as the German GHG system, the JP proved reliable and effective in the demanding conditions of Pacific operations - extreme temperatures, long patrols, and rough handling.

US submarine doctrine emphasized aggressive surface attacks at night using radar, but the JP remained essential for submerged approaches, avoiding escorts, and operating in contested waters. The single-operator design reflected American submarine manning efficiency, with one skilled sonarman providing adequate passive detection.

The JP's effectiveness improved dramatically as operators gained experience. By 1943-44, veteran sonarmen could identify specific Japanese destroyer classes by their acoustic signatures, detect convoys beyond visual range, and provide crucial warnings during depth charge attacks.

## Tactical Tips
- Slow to 4 knots or less for maximum detection range
- JP excels at detecting convoy targets before periscope depth
- Single operator means simplified training and watch rotation
- Use for submerged approach when escorts are present
- Can detect destroyer screws through thermal layers
- Bearing-only requires careful maneuvering for range estimation
- More reliable than German GHG in tropical heat
- Essential for avoiding enemy submarines
- Provides critical torpedo warning capability
