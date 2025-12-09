---
module_id: BRG-006
name: Armored Conning Tower
category: bridge
era: 1890-1920
slot_type: bridge
weight: 50000
power_draw: 5
crew_required: 8
armor_thickness: 300
tags: [bridge, pre-dreadnought, armored, battleship]
---

# Armored Conning Tower

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-006 |
| **Era** | 1890-1920 |
| **Weight** | 50,000 kg |
| **Power Draw** | 5 kW |
| **Crew Required** | 8 |
| **Armor** | 300mm |

## Description

Heavily armored cylindrical tower designed to protect the captain and helmsman during close-range battle. Features narrow vision slits and voice tubes for communication. Traded visibility for survivability in an era of short-range gunnery duels.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Basic | Magnetic compass |
| Speed Indicator | Basic | Telegraph to engine room |
| Heading Indicator | Basic | Visual compass |
| Minimap | None | No electronic aids |
| Contacts Display | None | Visual only through slits |
| Range Display | Estimated | Stadiametric estimation |
| Lead Indicator | None | Gunner's skill |
| Team Chat | Flags Only | Signal flags, very limited |
| Detection Warning | None | Visual lookouts only |

## Fog of War

- **Base Visibility**: Severely limited (vision slits only)
- **Advantage**: Excellent protection from shell splinters
- **Weakness**: Very poor situational awareness

## Special Features

### Extreme Protection
- 300mm armor protects from most shell fragments
- Immune to small/medium caliber hits
- Captain can survive near-misses

### Severe Visibility Penalty
- -50% visual detection range when buttoned up
- Must rely on lookouts reporting via voice tubes
- Very difficult to coordinate battle from inside

### Historical Design
- Standard on pre-dreadnought battleships
- Fell out of favor as battle ranges increased
- By WWI, commanders preferred open bridges despite risk

## Tactical Considerations

**When to Button Up:**
- Close-range battle (under 5km)
- Heavy incoming fire
- Last-ditch survival

**When to Use Open Bridge:**
- Long-range gunnery
- General operations
- When situational awareness critical

## Damage Resistance

```
Direct Hit (Large): Survivable
Direct Hit (Medium): Protected
Shell Splinters: Immune
Fire: Resistant
Flooding: N/A (above waterline)
```

## Historical Notes

The armored conning tower was the standard command position for battleships from 1880-1915. At Tsushima (1905), Russian Admiral Rozhestvensky was wounded when a shell fragment entered his conning tower's vision slit - demonstrating both the protection's value and its limitations. By WWI, ranges had increased to the point where commanders accepted the risk of open bridges for better visibility. Admiral Beatty at Jutland commanded from HMS Lion's open bridge, not her armored tower.

## Suitable Ships

- Pre-dreadnought battleships
- Early dreadnoughts
- Armored cruisers

## Upgrade Path

→ [[Enclosed-Bridge]] (better visibility, less armor)
→ [[Director-Bridge]] (fire control integration)
