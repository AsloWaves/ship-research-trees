---
module_id: SON-002
name: GHG Hydrophone
category: support
subcategory: detection-sonar
sonar_type: passive
era: 1935
nation: Germany
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
detection_range_passive: 5   # km (bearing only)
depth_capability: 250        # meters max depth detection
resolution: 300              # meters
bearing_accuracy: 5          # degrees

# Physical
hull_mounted: true
weight: 850
crew_required: 2
reliability: 90

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 50

tags: [sonar, passive, hydrophone, germany, kriegsmarine, submarine, ghg]
---

# GHG Hydrophone

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Gruppenhorchgerät (GHG) |
| **Nation** | Germany |
| **Type** | Passive |
| **Scan Pattern** | Omnidirectional Array |
| **Era** | 1935+ |

## Coverage Pattern
```
Pattern:          Omnidirectional Array
Beam Width:       360°
Sweep Arc:        360° all-around
Sweep Time:       Continuous
Coverage:         Complete horizontal plane
```

```
     [U-Boot]
    /   |   \
   /    |    \  360° Superior
  /     |     \ Passive Detection
 /      |      \
   (24 elements)
```

## Detection Performance

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Destroyer (running) | 5km | Bearing only, excellent clarity |
| Corvette (patrol) | 4km | Bearing only, clear detection |
| Submarine (diesel) | 4km | Bearing only, can classify type |
| Submarine (electric) | 2.5km | Bearing only, superior sensitivity |
| Torpedo | 3km | Early warning, bearing accuracy |
| Convoy (multiple ships) | 8km | Mass of contacts |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 3 knots | 95% |
| 5 knots | 85% |
| 8 knots | 65% |
| 12+ knots | 40% |

## Operation
### Passive Mode
The Gruppenhorchgerät (GHG) is Germany's premier passive sonar system, standard equipment on all U-boats from 1935 onward. Using a sophisticated array of 24 hydrophone elements arranged around the submarine's bow, the GHG provides exceptional passive detection capability.

**Advanced Features**:
- **Multiple Elements**: 24 hydrophones for superior directionality
- **Balanced Arrays**: Compensates for own ship noise
- **Trained Operators**: Two-man team for classification and tracking
- **Superior Resolution**: 5-degree bearing accuracy

**Gameplay**: GHG shows precise bearing lines with better accuracy than basic hydrophones. Trained operators can classify contact types and track multiple targets simultaneously.

### Contact Classification
Experienced GHG operators can identify:
- Ship class by propeller signature (2-prop vs 4-prop)
- Engine types (steam turbine vs diesel)
- Speed estimation from screw RPM
- Multiple contacts in same bearing
- Torpedo warnings with type classification

## Specifications
| Spec | Value |
|------|-------|
| Weight | 850 kg |
| Crew | 2 operators |
| Reliability | 90% |
| Array Elements | 24 hydrophones |

## Historical Notes

The Gruppenhorchgerät represented the pinnacle of WWII passive sonar technology. German U-boats relied heavily on the GHG for both hunting and survival - it could detect convoy escorts long before the U-boat was in danger, allowing commanders to position for attack or evade.

GHG operators were highly trained specialists who could identify individual Allied destroyer classes by their acoustic signatures. The system's sensitivity was such that experienced operators could hear ships beyond the horizon, detect convoy movements through thermal layers, and provide early warning of depth charge attacks.

The GHG's only weakness was that it provided bearing-only information. U-boat commanders had to use careful maneuvering and multiple bearings over time to establish firing solutions. Despite this limitation, the GHG remained one of the most effective submarine detection systems of the war.

## Tactical Tips
- Operate at minimum speed (3-5 knots) for optimal sensitivity
- GHG excels at detecting escorts before they detect you
- Use bearing changes over time to estimate range
- Can hear convoy through thermal layers when active sonar cannot
- Two operators allow simultaneous tracking of multiple contacts
- Essential for submerged approach to convoy
- Superior to Allied hydrophones in clarity and range
- Stop completely when being hunted for maximum stealth
