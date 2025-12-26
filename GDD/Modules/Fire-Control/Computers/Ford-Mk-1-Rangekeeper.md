---
module_id: FCS-CMP-001
name: Ford Mk 1 Range Keeper
category: fire-control
subcategory: computer
type: mechanical-analog
era: 1930
nation: USA
manufacturer: Ford Instrument Company

# Physical
weight_kg: 1360
dimensions: 1.5m x 1.2m x 0.9m
crew: 3
power_requirements: 115V AC

# Capabilities
max_range_m: 40000
max_target_speed_kn: 35
own_speed_compensation: true
wind_correction: true
ballistic_tables: interchangeable

tags: [computer, rangekeeper, usa, mechanical, wwii, battleship]
---

# Ford Mk 1 Range Keeper

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Ford Mk 1 Range Keeper |
| **Nation** | United States |
| **Era** | 1930-1945 |
| **Type** | Mechanical Analog Computer |
| **Manufacturer** | Ford Instrument Company |

## Description

The Ford Mk 1 Range Keeper was the mechanical brain of US Navy battleship fire control during WWII. This precision analog computer continuously calculated firing solutions, tracking target motion and compensating for ballistic effects to produce gun orders that hit targets at ranges exceeding 30km.

**Key Innovation**: Continuous mechanical integration - tracking position continuously rather than taking discrete measurements.

## How It Works

The Range Keeper solved the fire control problem mechanically:

### Inputs (from director)
1. **Initial Range** - From rangefinder or radar
2. **Bearing** - Target direction
3. **Own Course/Speed** - From ship's instruments
4. **Estimated Target Course** - Operator input
5. **Estimated Target Speed** - Operator input

### Internal Processing
```
┌─────────────────────────────────────────────┐
│              FORD Mk 1 RANGE KEEPER          │
├─────────────────────────────────────────────┤
│  ┌─────────┐   ┌─────────┐   ┌──────────┐  │
│  │ Range   │──▶│ Rate    │──▶│ Ballistic│  │
│  │ Input   │   │ Solver  │   │ Cam      │  │
│  └─────────┘   └─────────┘   └──────────┘  │
│       │              │             │        │
│       ▼              ▼             ▼        │
│  ┌─────────┐   ┌─────────┐   ┌──────────┐  │
│  │ Bearing │──▶│ Lead    │──▶│ Gun      │  │
│  │ Tracker │   │ Angle   │   │ Orders   │  │
│  └─────────┘   └─────────┘   └──────────┘  │
└─────────────────────────────────────────────┘
```

### Outputs (to gun mounts)
1. **Gun Bearing Order** - Where to point guns
2. **Gun Elevation Order** - How high to elevate
3. **Range to Target** - For crew information
4. **Time of Flight** - For spotting correction

## Physical Specifications

| Specification | Value |
|--------------|-------|
| Weight | 1,360 kg (3,000 lbs) |
| Dimensions | 1.5m × 1.2m × 0.9m |
| Crew | 3 operators |
| Power | 115V AC, 400Hz |
| Gears | 2,000+ precision gears |
| Cams | Interchangeable ballistic cams |

## Computational Capabilities

| Parameter | Capability |
|-----------|------------|
| Maximum Range | 40,000m (44,000 yards) |
| Target Speed | 0-35 knots |
| Own Ship Speed | 0-35 knots |
| Range Rate | ±1,000 m/min |
| Bearing Rate | ±10°/min |
| Wind Correction | 0-50 knots |

## Ballistic Cams

The Mk 1 used interchangeable cam drums containing ballistic data:

| Cam Set | Gun Type | Shells |
|---------|----------|--------|
| 14"/45 | Standard battleship | AP, HC |
| 14"/50 | New Mexico class | AP, HC |
| 16"/45 | Colorado class | AP, HC, Bombardment |
| 16"/50 | Iowa class | AP, HC, HC/VT |

Changing cams took 10-15 minutes and was done when guns were reamed to new ballistic profile.

## Operators

| Station | Role |
|---------|------|
| Range Keeper Operator | Sets target course/speed estimates |
| Plotter | Verifies solutions, monitors errors |
| Tracker | Monitors rangefinding, calls corrections |

## The "Keeping" Concept

"Range Keeping" means continuously tracking where the target IS:

1. **Initial Input**: Rangefinder provides range at time T₀
2. **Rate Computation**: Computer calculates closing/opening rate
3. **Continuous Update**: Mechanical gears constantly update predicted range
4. **Error Correction**: When new ranges arrive, computer adjusts

**Result**: The computer "keeps" track of range continuously between rangefinder readings.

## Combat Record

**Battle of Surigao Strait (October 1944)**
USS West Virginia's Ford Mk 1 produced firing solutions at 22,000+ yards in darkness, using radar range inputs. The battleship achieved hits with her first salvo.

**Shore Bombardment (1944-1945)**
Range Keepers computed solutions for fixed targets using chart data, enabling precision bombardment of Japanese positions.

## Variants

| Model | Era | Changes |
|-------|-----|---------|
| Mk 1 | 1930 | Original |
| Mk 1A | 1936 | Improved rate solvers |
| Mk 1 Mod 1 | 1941 | Radar range input |
| Mk 1 Mod 3 | 1943 | Automatic rate tracking |

## Comparison with Mk 37 Computer

| Feature | Ford Mk 1 | Mk 37 Computer |
|---------|-----------|----------------|
| Primary Use | Main battery (14"-16") | Dual-purpose (5") |
| Target Type | Surface ships | Surface + Aircraft |
| Complexity | ~2,000 gears | ~1,500 gears |
| Size | Larger | Smaller |
| AA Capability | None | Full |

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| Accuracy Bonus | +25% | Main battery fire |
| Range Tracking | Continuous | Mechanical integration |
| Radar Integration | Yes | Mk 1 Mod 1+ |
| Crew Requirement | 3 | Trained operators |
| Reliability | 94% | Robust mechanical design |

## Advantages
- Continuous solution (not discrete)
- Reliable mechanical design
- Proven combat record
- Interchangeable ballistic cams
- Radar-compatible (later models)

## Disadvantages
- Large and heavy
- Requires trained crew
- Mechanical wear over time
- No AA capability
- Limited target speed range

## Cross-References
- [[Directors/Mk-38-Director|Mk 38 Director]]
- [[Integrated/Mk-38-GFCS|Mk 38 GFCS]]
- [[Computers/Mk-37-Computer|Mk 37 Computer]]

---
*The Ford Mk 1 Range Keeper represented American industrial precision - thousands of gears working in harmony to solve the complex mathematics of naval gunnery.*
