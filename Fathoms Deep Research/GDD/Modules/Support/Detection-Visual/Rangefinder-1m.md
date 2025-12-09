---
module_id: VIS-005
name: 1m Optical Rangefinder
category: support
subcategory: detection-visual
era: 1900+
nation: Universal
slot_type: support

# Detection
detection_range_day: 12       # km
detection_range_night: 2      # km
coverage_arc: 120             # degrees (directed)
update_rate: continuous

# Rangefinding
rangefinding_range: 8         # km effective
rangefinding_accuracy: 150    # meters at max range
baseline: 1.0                 # meters

# Physical
weight: 400
crew_required: 2
weather_penalty: 35           # % reduction in storms

tags: [visual, detection, rangefinder, destroyer]
---

# 1m Optical Rangefinder

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | VIS-005 |
| **Era** | 1900+ |
| **Detection Range** | 12 km (day) |
| **Coverage** | 120° (directed) |

## Description
Compact coincidence rangefinder with 1-meter baseline. The smallest practical rangefinding instrument, designed for destroyers and small craft where weight and space are critical. Provides basic range measurement capability for gunnery fire control at typical destroyer engagement distances.

## Detection Performance
| Condition | Range | Notes |
|-----------|-------|-------|
| Clear day | 12 km | Detection only |
| Hazy | 8 km | Reduced clarity |
| Night (moonlit) | 2 km | Very limited |
| Night (dark) | 0.5 km | Nearly useless |
| Storm | 4 km | Rain obscures optics |

## Rangefinding Performance
| Range | Accuracy | Notes |
|-------|----------|-------|
| 2 km | ±25m | Very accurate |
| 4 km | ±50m | Good accuracy |
| 6 km | ±100m | Acceptable |
| 8 km | ±150m | Maximum effective range |
| 10 km+ | ±300m+ | Unreliable |

## Effect on Fog of War
- Provides range data to fire control
- Limited arc of coverage (must be aimed)
- Enables accurate gunnery within 8 km
- Supplements lookout detection

## Advantages
- Lightweight for small vessels
- Simple to operate
- Reliable mechanism
- No power required
- Adequate for destroyer combat ranges

## Disadvantages
- Short baseline limits accuracy
- Poor performance beyond 8 km
- Single operator fatigue
- Weather dependent
- Requires clear line of sight
- Cannot range through smoke

## Historical Notes
The 1m rangefinder was standard on destroyers and light cruisers from the early 1900s through WWII. While not as capable as the larger instruments on capital ships, it provided sufficient accuracy for the close-range gun duels typical of destroyer actions. British and Japanese destroyers typically mounted 1-1.5m rangefinders on their bridges.
