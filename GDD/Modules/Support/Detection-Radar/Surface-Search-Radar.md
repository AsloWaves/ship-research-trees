---
module_id: SUP-006
name: Surface Search Radar
category: support
subcategory: detection
era: 1940-present
slot_type: support
weight: 5000
crew_required: 2
tags: [support, detection, radar, wwii, game-changer]
---

# Surface Search Radar

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | SUP-006 |
| **Era** | 1940-Present |
| **Category** | Detection |
| **Weight** | 5,000 kg |
| **Crew Required** | 2 |

## Description

Radio detection and ranging equipment for surface contacts. Transmits radio pulses and detects echoes from ships, giving range and bearing regardless of visibility. The single most important naval technology of WWII.

## Effect on Fog of War

```
Detection Range:      25-40 km (depending on type)
Weather Effect:       None (works in all conditions)
Night Effect:         None (full capability)
Update Rate:          Every antenna rotation (4-15 sec)
```

**THIS IS THE GAME-CHANGER**: Radar contacts appear on minimap!

## Effect on UI

When installed with CIC Bridge:
- **Minimap Contacts**: Surface ships displayed
- **Range/Bearing**: Automatic, accurate
- **Contact Tracking**: Movement vectors shown
- **Beyond Horizon**: Can detect ships you can't see

## Radar Types by Era

| Type | Era | Range | Notes |
|------|-----|-------|-------|
| Type 271 (UK) | 1941 | 15 km | First effective set |
| SC (US) | 1942 | 25 km | Air/surface search |
| SG (US) | 1942 | 35 km | Excellent surface search |
| Type 272 (UK) | 1943 | 20 km | Improved resolution |
| Modern | 1970+ | 50+ km | Digital processing |

## Fog of War: Vision Sharing

When combined with Voice Radio:
- Your radar contacts can be shared with allies
- Allied ships can see YOUR contacts
- Creates combined tactical picture
- Requires communication module!

## Detection Table

| Target | Detection Range | Notes |
|--------|-----------------|-------|
| Battleship | 40 km | Large radar cross-section |
| Carrier | 40 km | Flight deck reflects well |
| Cruiser | 30 km | |
| Destroyer | 20 km | Smaller return |
| Submarine (surfaced) | 15 km | Very small target |
| Periscope | 5-8 km | Difficult but possible |
| PT Boat | 10 km | Small, fast |

## Limitations

- Cannot see submerged submarines
- Can be jammed (ECM)
- Reveals your position (enemy RWR detects)
- Requires electrical power
- Minimum range ~500m (too close to detect)

## Countermeasures

Enemy can counter with:
- **Radar Warning Receiver**: Knows you're scanning
- **Radar Jammer**: Disrupts your display
- **Chaff**: Creates false contacts

## Historical Notes

Radar decided battles. At Cape Matapan, British radar detected the Italian fleet at night, enabling a devastating ambush. At Guadalcanal, radar-equipped US ships had significant advantages in night fighting. By 1943, radar was considered essential equipment.

## Requires

- CIC Bridge (or Director Bridge for basic function)
- 50 kW power available
- Antenna mounting position

## Compatible With

- Director Bridge (range only)
- CIC Bridge (full integration)
- Modern Bridge (enhanced)
