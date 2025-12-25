---
module_id: VIS-006
name: 3m Optical Rangefinder
category: support
subcategory: detection-visual
era: 1910+
nation: Universal
slot_type: support

# Detection
detection_range_day: 18       # km
detection_range_night: 2.5    # km
coverage_arc: 120             # degrees (directed)
update_rate: continuous

# Rangefinding
rangefinding_range: 15        # km effective
rangefinding_accuracy: 100    # meters at max range
baseline: 3.0                 # meters

# Physical
weight: 1200
crew_required: 2
weather_penalty: 30           # % reduction in storms

tags: [visual, detection, rangefinder, cruiser]
---

# 3m Optical Rangefinder

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | VIS-006 |
| **Era** | 1910+ |
| **Detection Range** | 18 km (day) |
| **Coverage** | 120° (directed) |

## Description
Medium-baseline coincidence rangefinder optimized for cruiser-scale vessels. The 3-meter baseline provides a good balance between accuracy and size, suitable for engagement ranges of 12-15 km. Standard equipment on light and heavy cruisers from WWI through the early radar era.

## Detection Performance
| Condition | Range | Notes |
|-----------|-------|-------|
| Clear day | 18 km | Good detection range |
| Hazy | 12 km | Reduced clarity |
| Night (moonlit) | 2.5 km | Limited capability |
| Night (dark) | 0.8 km | Poor performance |
| Storm | 6 km | Rain affects optics |

## Rangefinding Performance
| Range | Accuracy | Notes |
|-------|----------|-------|
| 5 km | ±20m | Excellent accuracy |
| 10 km | ±50m | Very good |
| 15 km | ±100m | Maximum effective range |
| 20 km | ±250m | Marginal |
| 25 km+ | ±500m+ | Unreliable |

## Effect on Fog of War
- Provides accurate ranging to 15 km
- Directed coverage (operator aims)
- Feeds data to mechanical fire control
- Enables precise gunnery at cruiser ranges
- Better low-light performance than 1m

## Advantages
- Good accuracy at typical combat ranges
- Manageable size and weight
- Suitable for cruisers and large destroyers
- Reliable performance
- Well-proven technology

## Disadvantages
- Still limited beyond 15 km
- Requires trained operators
- Single target at a time
- Weather dependent
- Cannot see through smoke
- Degrades with range

## Historical Notes
The 3-meter rangefinder became standard on cruisers during WWI. British Town-class cruisers mounted 3m instruments, while American and Japanese cruisers used similar 2.5-3.5m units. These instruments proved their worth in surface actions like the Battle of the River Plate (1939), where HMS Ajax and HMS Achilles used optical rangefinding to engage Graf Spee at 13-15 km ranges.
