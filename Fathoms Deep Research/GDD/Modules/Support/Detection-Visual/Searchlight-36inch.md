---
module_id: VIS-009
name: 36-inch Searchlight
category: support
subcategory: detection-visual
era: 1900+
nation: Universal
slot_type: support

# Detection
detection_range_day: 0        # km (not used during day)
detection_range_night: 5      # km (illumination beam)
coverage_arc: 30              # degrees (narrow beam)
update_rate: continuous

# Illumination
beam_range: 5                 # km effective illumination
beam_width: 30                # degrees

# Physical
weight: 800
crew_required: 2
weather_penalty: 40           # % reduction in storms

tags: [visual, detection, searchlight, night, illumination]
---

# 36-inch Searchlight

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | VIS-009 |
| **Era** | 1900+ |
| **Detection Range** | 5 km (night illumination) |
| **Coverage** | 30° beam |

## Description
Standard naval searchlight with 36-inch (91cm) diameter mirror. Projects an intense beam of light to illuminate targets at night, enabling visual identification and gunnery fire control when radar is unavailable. The workhorse night-fighting tool from the dreadnought era through WWII.

## Detection Performance
| Condition | Range | Notes |
|-----------|-------|-------|
| Clear night | 5 km | Full illumination |
| Hazy night | 3 km | Scatter reduces range |
| Moonlit | 6 km | Helps but not required |
| Storm | 2 km | Rain scatters beam badly |
| Fog | 1 km | Nearly useless |

## Illumination Performance
| Range | Effect | Notes |
|-------|--------|-------|
| 1 km | Bright illumination | Target clearly visible |
| 3 km | Good illumination | Identification possible |
| 5 km | Marginal illumination | Silhouette visible |
| 7 km+ | Glow only | Insufficient for gunnery |

## Effect on Fog of War
- Reveals and illuminates single target
- Enables night gunnery
- Also reveals YOUR position (double-edged sword)
- Narrow beam must be aimed accurately
- Can dazzle/blind enemy lookouts

## Advantages
- Enables visual night combat
- Can illuminate specific targets
- Useful for identification
- Good range for its size
- Standard equipment on most warships

## Disadvantages
- REVEALS YOUR POSITION prominently
- Narrow beam (must aim accurately)
- High power consumption
- Makes your ship a target
- Weather sensitive
- Can be shot out easily

## Historical Notes
Searchlights were essential for night combat in the pre-radar era. British and Japanese navies particularly emphasized night-fighting tactics using searchlights. The First Naval Battle of Guadalcanal (November 1942) saw intense close-range night action with searchlights illuminating targets at point-blank range. However, searchlights were a double-edged sword - illuminating the enemy also revealed your position. The Japanese quickly learned to shoot out American searchlights first. By 1943, radar-directed gunnery made searchlights obsolescent for surface combat, though they remained useful for anti-aircraft work and signaling.
