---
module_id: BRG-001
name: Open Bridge
category: bridge
era: 1890-1920
slot_type: bridge
weight: 2000
crew_required: 4
tags: [bridge, early-era, basic]
---

# Open Bridge

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-001 |
| **Era** | 1890-1920 |
| **Weight** | 2,000 kg |
| **Crew Required** | 4 |

## Description

The traditional open bridge design with minimal weather protection. Command is exercised through direct voice commands and speaking tubes to various stations throughout the ship.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Basic | Magnetic only, may drift ±3° |
| Speed Indicator | Estimate | Rough RPM-based estimate |
| Heading Indicator | Basic | Magnetic compass |
| Minimap | Disabled | No electronic systems |
| Contacts Display | Disabled | Visual range only |
| Range Display | Disabled | Must estimate |
| Lead Indicator | Disabled | Manual gunnery |
| Team Chat | Disabled | Signal flags only |
| Detection Warning | Disabled | No sensors |

## Fog of War

- **Base Visibility**: Visual range only (weather dependent)
- **Max Contacts Tracked**: 3 (manual plotting)
- **Link Capability**: Signal flags (visual range, preset messages)

## Compatibility

- **Supported Detection Modules**: Lookout Station, Searchlight, Optical Rangefinder
- **Supported Comms Modules**: Signal Flags, Signal Lamp
- **NOT Compatible**: Radar, Sonar, Radio systems

## Stats

```
Command Efficiency: 60%
Weather Vulnerability: High (exposed)
Night Operations: Poor
Damage Resistance: Low
```

## Historical Notes

Open bridges were standard on warships until WWI. Captains preferred the unobstructed view despite exposure to weather and enemy fire. The lack of protection became problematic as engagement ranges increased and high-angle fire became more common.

## Upgrade Path

→ [[Enclosed-Bridge]] (1910+)
