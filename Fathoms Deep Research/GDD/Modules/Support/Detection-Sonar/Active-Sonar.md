---
module_id: SUP-008
name: Active Sonar (ASDIC)
category: support
subcategory: detection
era: 1920-present
slot_type: support
weight: 3000
power_draw: 25
crew_required: 2
tags: [support, detection, sonar, active, asw]
---

# Active Sonar (ASDIC)

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | SUP-008 |
| **Era** | 1920-Present |
| **Category** | Detection |
| **Weight** | 3,000 kg |
| **Power Draw** | 25 kW |
| **Crew Required** | 2 |

## Description

Active sound navigation and ranging system. Transmits a "ping" and listens for echoes from submerged objects. Unlike passive hydrophones, active sonar provides both bearing AND range to the target.

## Effect on Fog of War

Adds precise underwater detection:
```
Detection Range:      2-5 km (WWI) to 10+ km (modern)
Information:          Bearing AND Range
Ping Interval:        Every 5-10 seconds
Tradeoff:             Target KNOWS you're pinging
```

## Effect on UI

When installed with Director Bridge+ :
- **Sonar Contact Marker**: Shows submarine position
- **Range Ring**: Distance to contact
- **Movement Vector**: Contact course/speed (with tracking)
- **Classification**: Submarine vs. whale vs. wreck

## Sonar Types

| Type | Era | Range | Notes |
|------|-----|-------|-------|
| ASDIC Type 123 | 1920s | 2 km | Early British |
| ASDIC Type 144 | 1940 | 3 km | Standard WWII |
| QC/JK (US) | 1942 | 3-4 km | US equivalent |
| SQS-26 | 1960s | 10+ km | Cold War sonar |
| Modern | 1980+ | 20+ km | Towed arrays, processing |

## The Tradeoff

**Active sonar reveals YOU to the target!**

When you ping:
- Your position is revealed to target
- Range: Target can hear ping at 2x your detection range
- The submarine knows you're hunting

## Detection Factors

```
Base Detection:       4 km
Thermal Layer:        May block entirely
Sea State:            Rough = -50% range
Target Depth:         Below layer = harder
Own Speed:            Fast = -30% range
Target Speed:         Fast = +20% (more noise)
```

## Tactical Use

1. **Final Approach**: Use passive to close, active to attack
2. **Datum Search**: Ping area of last known contact
3. **Depth Charge Aim**: Need range for accurate drops
4. **Deterrent**: Pinging may force sub to disengage

## Historical Notes

British ASDIC (later called Sonar) was considered the answer to submarines before WWII. Reality proved different - ASDIC had significant limitations, particularly against deep-diving boats. Combined with radar, depth charges, and aircraft, it became part of an effective ASW system.

## Limitations

- Cannot detect surfaced submarines (use radar)
- "Dead zone" directly below ship
- Thermal layers block sound
- Target can hear you pinging
- Degraded in rough weather

## Compatible With

- Director Bridge+
- CIC Bridge (full integration)
- Dedicated ASW ships recommended
