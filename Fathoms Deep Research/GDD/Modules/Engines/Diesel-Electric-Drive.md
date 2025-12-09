---
module_id: ENG-006
name: Diesel-Electric Drive
category: engine
era: 1920-present
slot_type: engine
power_output: 8000
efficiency: 90
weight: 80000
reliability: 85
noise_level: 15
acceleration: fast
fuel_type: diesel
tags: [engine, diesel, electric, submarine, silent]
---

# Diesel-Electric Drive

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | ENG-006 |
| **Era** | 1920-Present |
| **Power Output** | 8,000 SHP per unit |
| **Efficiency** | 90% |
| **Weight** | 80 tons |
| **Fuel Type** | Diesel |

## Description

Diesel engines drive generators that power electric motors connected to the propeller shafts. This arrangement allows the diesel engines to run at optimal RPM regardless of propeller speed, and enables silent running on batteries alone.

## Performance Stats

```
Power Output:     8,000 SHP (per engine set)
Max Ship Speed:   ~20 knots surfaced
Acceleration:     Fast (1 minute to full power)
Fuel Consumption: 0.20 kg diesel per SHP-hour
Range Factor:     3.0x (excellent economy)
Battery Mode:     4-8 knots, 2-4 hours
```

## Characteristics

| Stat | Rating | Notes |
|------|--------|-------|
| Power | Medium | Not for capital ships |
| Efficiency | Excellent | Best fuel economy |
| Weight | Light | Compact system |
| Reliability | Good | Diesel proven reliable |
| Noise | Very Low | Electric motors silent |
| Maintenance | Low | Simple components |

## Special Feature: Silent Running

When running on batteries only:
- Noise level drops to 5 (nearly silent)
- Speed limited to 4-8 knots
- Duration: 2-4 hours (battery dependent)
- Ideal for submarine approach/evasion

## Advantages

- Exceptional fuel efficiency
- Silent running capability
- Good low-speed performance
- Flexible power arrangement
- Easy to maintain

## Disadvantages

- Limited maximum power
- Battery capacity constraints
- Not suitable for high-speed ships
- Diesel exhaust on surface

## Historical Notes

Diesel-electric became the standard submarine powerplant from the 1920s onward. The ability to run silently on batteries was essential for submarine tactics. Surface ships also adopted the system for auxiliaries and smaller combatants where fuel economy mattered more than speed.

## Compatible Ships

- Submarines (primary)
- Corvettes
- Patrol boats
- Auxiliaries
- Merchant conversions

## Submarine Detection Modifier

```
Surfaced (diesel): Normal detection range
Snorkeling:        -25% detection range
Battery only:      -75% detection range
```

## Upgrade Path

← [[Diesel-Engine]] (simpler)
→ [[Nuclear-Reactor]] (unlimited underwater)
