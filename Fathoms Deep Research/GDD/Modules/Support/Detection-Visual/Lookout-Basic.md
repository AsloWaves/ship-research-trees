---
module_id: VIS-001
name: Basic Lookout Station
category: support
subcategory: detection-visual
era: 1890+
nation: Universal
slot_type: support

# Detection
detection_range_day: 8        # km
detection_range_night: 1      # km (without searchlight)
coverage_arc: 360             # degrees
update_rate: continuous

# Physical
weight: 300
crew_required: 2
weather_penalty: 40           # % reduction in storms

tags: [visual, detection, lookout, basic]
---

# Basic Lookout Station

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | VIS-001 |
| **Era** | 1890+ |
| **Detection Range** | 8 km (day) |
| **Coverage** | 360° |

## Description
Simple observation post with naked-eye lookouts scanning the horizon. The most basic form of naval detection, requiring nothing more than trained eyes and discipline. Effective for spotting large vessels and smoke at moderate ranges, though limited by human visual acuity.

## Detection Performance
| Condition | Range | Notes |
|-----------|-------|-------|
| Clear day | 8 km | Battleship-size |
| Hazy | 5 km | -30% visibility |
| Night (moonlit) | 1.5 km | Limited |
| Night (dark) | 0.5 km | Very limited |
| Storm | 3 km | Severely degraded |

## Effect on Fog of War
- Reveals surface contacts within detection range
- 360° continuous scanning (split between lookouts)
- Cannot provide precise range data
- Smoke plumes visible before hull

## Advantages
- Zero power requirements
- Lightweight installation
- Reliable in all eras
- No mechanical failures
- Low crew requirement

## Disadvantages
- Limited range compared to optics
- Highly weather dependent
- Fatigue affects performance
- Cannot see over horizon
- No night capability without searchlights

## Historical Notes
The foundation of naval detection from antiquity through the modern era. Even in the radar age, basic lookouts remained essential for spotting periscopes, small craft, floating mines, and survivors. Many critical sightings throughout naval history came from alert lookouts rather than sophisticated equipment.
