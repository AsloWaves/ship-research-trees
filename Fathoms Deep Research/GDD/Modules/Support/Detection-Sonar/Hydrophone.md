---
module_id: SUP-004
name: Hydrophone
category: support
subcategory: detection
era: 1915-1945
slot_type: support
weight: 500
crew_required: 1
tags: [support, detection, sonar, passive, asw]
---

# Hydrophone

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | SUP-004 |
| **Era** | 1915-1945 |
| **Category** | Detection |
| **Weight** | 500 kg |
| **Crew Required** | 1 operator |

## Description

Passive underwater listening device. Hydrophones detect sounds transmitted through water - propeller noise, machinery, torpedo motors. Unlike active sonar, hydrophones do not reveal the listener's position.

## Effect on Fog of War

Adds underwater detection layer:
```
Detection Range:      3-8 km (depends on target noise)
Direction:            Bearing only (no range)
Best Conditions:      Own ship stopped/slow
Degraded:             Own ship moving fast
```

## Effect on UI

When installed:
- **Bearing Indicator**: Shows direction to underwater sounds
- **Torpedo Warning**: Alert when torpedo detected
- **Submarine Warning**: Bearing to submarine if detected

**Key Limitation**: No range information! Only bearing.

## Detection Capabilities

| Target | Bearing Range | Notes |
|--------|---------------|-------|
| Submarine (running) | 5-8 km | Diesel engines loud |
| Submarine (creeping) | 2-3 km | Electric motors quieter |
| Submarine (stopped) | <1 km | Nearly silent |
| Torpedo | 2-3 km | High-speed screws distinctive |
| Surface ship | 10+ km | Very loud |

## Operator Skill

Trained operators can:
- Classify contacts by sound (screw count, RPM)
- Estimate target speed
- Distinguish friendly from enemy
- Detect multiple contacts

## Limitations

- Bearing only, no range
- Degraded by own ship's noise
- Degraded at high speed
- Weather affects propagation
- "Deaf" in certain thermal layers

## Tactical Use

1. **Torpedo Warning**: Primary early-war use
2. **ASW Search**: Locate general submarine area
3. **Passive Tracking**: Follow without revealing yourself
4. **Ambush Detection**: Hear enemy before they hear you

## Historical Notes

Hydrophones were the primary ASW sensor in WWI and early WWII. British "ASDIC" (active sonar) began replacing passive hydrophones in the 1920s, but hydrophones remained valuable for their stealth - they don't alert the enemy. Submarines used hydrophones extensively to avoid detection.

## Replaced By

- [[Active-Sonar]] provides range but alerts target
- Modern towed arrays combine passive sensitivity with processing

## Compatible With

- Enclosed Bridge+
- All ships (even boats)
- Submarines (essential equipment)
