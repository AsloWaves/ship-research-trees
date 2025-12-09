---
module_id: BRG-003
name: Director Bridge
category: bridge
era: 1920-1945
slot_type: bridge
weight: 15000
power_draw: 25
crew_required: 10
tags: [bridge, interwar, fire-control]
---

# Director Bridge

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-003 |
| **Era** | 1920-1945 |
| **Weight** | 15,000 kg |
| **Power Draw** | 25 kW |
| **Crew Required** | 10 |

## Description

Advanced bridge design integrating fire control director systems. Features dedicated director tower, mechanical fire control computer, and centralized gunnery control. The bridge crew can now coordinate all main battery fire from a single position.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Accurate | Gyrocompass |
| Speed Indicator | Accurate | Engine telegraph |
| Heading Indicator | Accurate | Gyro-stabilized |
| Minimap | Basic | Ship position only |
| Contacts Display | Limited | Visual + spotting aircraft |
| Range Display | Accurate | Optical rangefinder integration |
| Lead Indicator | Basic | Mechanical computer solution |
| Team Chat | Text | Wireless telegraph |
| Detection Warning | Limited | Hydrophone only |

## Fog of War

- **Base Visibility**: Visual range + aircraft spotting
- **Max Contacts Tracked**: 12 (fire control plotting)
- **Link Capability**: Radio telegraph, aircraft relay

## Compatibility

- **Supported Detection Modules**: All optical, Hydrophone, Floatplane Catapult
- **Supported Comms Modules**: All non-satellite
- **Supported Fire Control**: All mechanical systems
- **NOT Compatible**: Digital fire control, Phased array radar

## Stats

```
Command Efficiency: 85%
Weather Vulnerability: Low
Night Operations: Moderate (searchlights)
Damage Resistance: Medium-High
```

## Special Features

### Fire Control Integration
When paired with Mechanical Fire Control Computer:
- Basic lead indicator displayed
- Range automatically updated
- Salvo timing assistance

### Aircraft Spotting
When paired with Floatplane Catapult:
- Temporary visibility extension
- Fall-of-shot correction
- Beyond-horizon contact reports

## Historical Notes

The director system revolutionized naval gunnery. By centralizing fire control, all guns could be aimed and fired as a coordinated salvo. The British led development after Jutland, with the US and Japan quickly following.

## Upgrade Path

← [[Enclosed-Bridge]] (earlier)
→ [[Combat-Information-Center]] (1940+)
