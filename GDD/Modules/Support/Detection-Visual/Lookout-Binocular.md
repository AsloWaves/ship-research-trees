---
module_id: VIS-002
name: Binocular Lookout Station
category: support
subcategory: detection-visual
era: 1900+
nation: Universal
slot_type: support

# Detection
detection_range_day: 15       # km
detection_range_night: 2      # km (without searchlight)
coverage_arc: 360             # degrees
update_rate: continuous

# Physical
weight: 500
crew_required: 4
weather_penalty: 35           # % reduction in storms

tags: [visual, detection, lookout, binoculars]
---

# Binocular Lookout Station

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | VIS-002 |
| **Era** | 1900+ |
| **Detection Range** | 15 km (day) |
| **Coverage** | 360° |

## Description
Enhanced observation post equipped with 7x50 naval binoculars for each lookout. The standard configuration for warships from WWI onward, combining optical magnification with wide field of view. Lookouts sweep assigned sectors methodically, reporting all contacts immediately.

## Detection Performance
| Condition | Range | Notes |
|-----------|-------|-------|
| Clear day | 15 km | Battleship-size |
| Hazy | 10 km | -30% visibility |
| Night (moonlit) | 2 km | Better than naked eye |
| Night (dark) | 0.8 km | Very limited |
| Storm | 5 km | Rain interferes with optics |

## Effect on Fog of War
- Extended visual detection range
- Can identify ship types at 8-10 km
- Spots smoke at maximum range
- Better low-light performance than basic lookouts
- Cannot provide accurate ranging

## Advantages
- Nearly doubles detection range
- 7x magnification aids identification
- Standard naval equipment
- Reliable and simple
- Good light-gathering (50mm objective)

## Disadvantages
- Requires steady hands in rough seas
- Optics fog in humid conditions
- Limited night vision capability
- Still cannot see over horizon
- Crew fatigue remains a factor

## Historical Notes
The 7x50 naval binocular became the standard lookout optic for most navies by WWI. The 7x magnification provided good target detail while maintaining a wide enough field of view for scanning. The 50mm objective lenses gathered sufficient light for dawn/dusk operations. German Zeiss and Japanese Nikko binoculars were particularly prized for optical quality.
