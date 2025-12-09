---
module_id: BRG-008
name: Submarine Conning Tower
category: bridge
subcategory: submarine
era: 1914-1945
slot_type: bridge
weight: 8000
crew_required: 3
pressure_depth: 100
tags: [bridge, submarine, wwii, periscope]
---

# Submarine Conning Tower

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-008 |
| **Era** | 1914-1945 |
| **Weight** | 8,000 kg |
| **Power Draw** | 15 kW |
| **Crew Required** | 3 |
| **Pressure Depth** | 100m |

## Description

Small armored compartment atop the pressure hull housing the attack periscope, torpedo data computer, and helm station. The captain fights the boat from here during submerged attacks. Features the attack periscope for targeting and the helm for precise maneuvering.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Accurate | Gyrocompass |
| Speed Indicator | Accurate | Integrated |
| Heading Indicator | Accurate | Gyro |
| Depth Indicator | Precise | Critical for subs |
| Periscope View | Yes | Attack periscope |
| Minimap | None | Periscope only |
| Contacts Display | Sonar | Hydrophone bearings |
| Range Display | Periscope | Stadimeter ranging |
| Lead Indicator | TDC | Torpedo data computer |
| Team Chat | None | Silent running |

## Fog of War - Submerged

- **Base Visibility**: Periscope only (limited arc, brief exposure)
- **Detection**: Hydrophone bearings (no range)
- **Maximum Stealth**: Enemies cannot see you if deep

## Fog of War - Surfaced

- **Base Visibility**: Bridge watch (fair weather lookouts)
- **Detection**: Visual + hydrophone
- **Vulnerability**: Radar-detectable, aircraft-vulnerable

## Special Features

### Attack Periscope
- 6x magnification for targeting
- Stadimeter for range estimation
- Limited to ~20m depth (periscope depth)
- Risk: Periscope feather visible to alert enemies

### Torpedo Data Computer
When targeting:
- Calculates torpedo lead angle
- Accounts for target speed/course
- Generates firing solution
- Increases torpedo hit probability

### Silent Running
- Can minimize all noise
- Reduces enemy passive detection
- Trade-off: Limited own-ship sensors

## Operational Modes

### Surface Running
- Bridge watch for lookouts
- Diesel engines charging
- Maximum visibility
- Vulnerable to aircraft

### Periscope Depth
- Attack position
- Limited visibility (periscope arc)
- Can engage surface targets
- Risk of detection

### Deep Running
- Maximum stealth
- Blind (sonar only)
- Safe from surface detection
- Cannot attack

## Damage Resistance

```
Pressure Hull: Rated to 100m
Depth Charge (Close): Critical
Depth Charge (Medium): Serious
Depth Charge (Far): Minor
Gunfire (Surfaced): Vulnerable
```

## Historical Notes

The conning tower was the heart of submarine combat from WWI through WWII. German U-boat commanders like Otto Kretschmer conducted attacks from this cramped space, using the attack periscope to line up torpedo shots. The Type VIIC U-boat's conning tower was barely large enough for the captain, helmsman, and one plotter. American fleet submarines had larger conning towers with more sophisticated TDCs, contributing to their success in the Pacific.

## Suitable Ships

- WWI submarines (all types)
- WWII submarines (all types)
- Early post-war conventional subs

## Upgrade Path

→ [[Submarine-Sail]] (modern submarines, 1950+)
