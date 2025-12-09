---
module_id: SUP-003
name: Optical Rangefinder
category: support
subcategory: detection
era: 1900-1970
slot_type: support
weight: 2000
power_draw: 0
crew_required: 2
tags: [support, detection, rangefinding, fire-control]
---

# Optical Rangefinder

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | SUP-003 |
| **Era** | 1900-1970 |
| **Category** | Detection / Fire Control |
| **Weight** | 2,000 kg |
| **Power Draw** | None |
| **Crew Required** | 2 |

## Description

Precision optical instrument for measuring distance to targets. Uses stereoscopic or coincidence principles - the operator adjusts until two images align, and the mechanism converts the angle to range. Essential for accurate gunnery.

## Effect on UI

When installed:
- **Range Display**: Enabled (with accuracy based on type)
- **Targeting Assist**: Range data fed to fire control

## Rangefinder Types

| Type | Era | Base Length | Accuracy |
|------|-----|-------------|----------|
| Coincidence (short) | 1900+ | 1-2m | ±500 yards |
| Coincidence (medium) | 1910+ | 3-5m | ±300 yards |
| Stereoscopic | 1915+ | 5-8m | ±200 yards |
| Director-mounted | 1920+ | 8-15m | ±100 yards |

## Accuracy Factors

```
Base Accuracy:        ±300 yards (5m instrument)
Crew Skill Bonus:     ±50 yards per level
Target Motion:        +100 yards error if fast
Visibility:           +200 yards error if haze
Range:                +50 yards per 5km distance
```

## UI Integration

The rangefinder enables:
1. Range readout on HUD (with error margin)
2. Fire control computer input (if installed)
3. Fall-of-shot correction

## Limitations

- Requires clear line of sight
- Degraded in poor visibility
- Cannot range through smoke
- Maximum effective range ~25km
- Requires steady platform (accuracy drops at speed)

## Historical Notes

Rangefinders grew from 1m instruments on early destroyers to massive 15m units on battleships. Japanese rangefinders were considered excellent, particularly the 15m units on Yamato. British stereoscopic rangefinders required specially selected operators with good depth perception.

## Replaced By

Fire Control Radar (1941+) provides all-weather ranging with greater accuracy. However, optical backup remained standard through the 1970s.

## Compatible With

- Enclosed Bridge+
- Director Bridge (full integration)
- CIC (backup system)
