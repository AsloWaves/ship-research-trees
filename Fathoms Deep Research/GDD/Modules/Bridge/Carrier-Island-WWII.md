---
module_id: BRG-010
name: Carrier Island (WWII)
category: bridge
subcategory: carrier
era: 1922-1960
slot_type: bridge
weight: 80000
crew_required: 50
tags: [bridge, carrier, wwii, aviation]
---

# Carrier Island (WWII)

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-010 |
| **Era** | 1922-1960 |
| **Weight** | 80,000 kg |
| **Power Draw** | 100 kW |
| **Crew Required** | 50 |

## Description

Compact superstructure on the starboard side of the flight deck housing the navigation bridge, flight control (Pri-Fly), radar antennas, and funnel uptakes. Designed as small as possible to maximize flight deck area while providing essential command functions.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Accurate | Gyrocompass |
| Speed Indicator | Accurate | Critical for flight ops |
| Heading Indicator | Accurate | Gyro-stabilized |
| Wind Indicator | Yes | Essential for launches |
| Minimap | Radar | Air search integration |
| Contacts Display | Air + Surface | Dual radar systems |
| Air Operations | Full | Launch/recovery control |
| CAP Control | Yes | Fighter direction |
| Team Chat | Voice | Multi-channel radio |
| Detection Warning | Limited | Early RWR |

## Fog of War

- **Base Visibility**: Extensive (air search radar)
- **Air Detection**: 80+ km (aircraft)
- **Surface Detection**: 35+ km (ships)
- **Air Control**: Can vector fighters to contacts

## Special Features

### Primary Flight Control (Pri-Fly)
- Controls all flight deck operations
- Launch/recovery timing
- Aircraft handling
- Crash response

### Fighter Direction
When equipped with CIC:
- Vector CAP to intercept bogies
- Track multiple raids
- Coordinate defense

### Air Search Radar
- Long-range aircraft detection
- Critical for fleet defense
- Early warning of attacks

### Multi-Channel Radio
- Air traffic control
- Fighter direction
- Fleet coordination
- Strike coordination

## Operational Capabilities

### Flight Operations
| Function | Capability |
|----------|------------|
| Launch Rate | 2-3 aircraft/minute |
| Recovery Rate | 1 aircraft/90 seconds |
| Deck Spot | Visual management |
| Wind Requirements | 25+ knots over deck |

### Combat Direction
- Control embarked air group
- Coordinate fleet CAP
- Manage strike packages
- Rescue coordination

## Damage Vulnerability

```
Location: Exposed on flight deck
Bomb Hit: Severe (air ops stopped)
Kamikaze: Critical vulnerability
Fire: Dangerous (fuel/ordnance)
Gunfire: Vulnerable
```

## The Island Problem

The island creates turbulence affecting landing aircraft. All carriers place the island to starboard because:
- Propeller torque pulls aircraft left in emergency
- Pilots naturally dodge right
- Standardized approach patterns

## Historical Notes

The carrier island evolved from early flush-deck designs as navies realized that a superstructure was necessary for effective ship and air operations control. HMS Hermes (1924) was the first carrier designed from the keel up with an island. During WWII, the island became the target of choice for kamikaze attacks - a single hit could knock out both navigation and flight control. USS Franklin's island was devastated by bomb hits in March 1945, killing most of the air department leadership.

## Suitable Ships

- Fleet carriers (CV)
- Light carriers (CVL)
- Escort carriers (CVE)

## Upgrade Path

→ [[Carrier-Island-Modern]] (supercarrier, 1960+)
