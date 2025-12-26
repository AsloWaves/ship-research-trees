---
module_id: FCS-CMP-002
name: Dreyer Fire Control Table Mk V
category: fire-control
subcategory: computer
type: mechanical-plotting
era: 1918
nation: UK
manufacturer: Elliott Brothers

# Physical
weight_kg: 2200
dimensions: 3.0m x 2.0m x 1.2m
crew: 6
power_requirements: manual + electric motors

# Capabilities
max_range_m: 30000
max_target_speed_kn: 30
own_speed_compensation: true
wind_correction: manual
plotting_type: continuous

tags: [computer, dreyer-table, uk, mechanical, wwi, dreadnought, pioneer]
---

# Dreyer Fire Control Table Mk V

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Dreyer Fire Control Table Mk V |
| **Nation** | United Kingdom |
| **Era** | 1918-1940s |
| **Type** | Mechanical Plotting Table |
| **Designer** | Captain Frederic Dreyer RN |

## Description

The Dreyer Table was the Royal Navy's primary fire control computer from WWI through the interwar period. A hybrid plotting/computing device, it combined graphical tracking with mechanical calculation to produce firing solutions.

**Key Innovation**: Combined plotting (visual tracking) with mechanical computation - operators could SEE the solution developing on paper while the machine calculated.

## Historical Significance

The Dreyer Table was born from the Battle of Jutland (1916):
- British ships struggled to hit at long range
- Existing systems couldn't track fast-moving targets
- Post-battle analysis led to the Dreyer Table design
- First truly integrated fire control computer

## How It Works

The Dreyer Table combined three functions:

### 1. Plotting Section
A moving paper plot showed target track:
```
     Range
       ▲
       │    Target Track
       │    ─────────●───▶
       │   /
       │  /
       │ /  Plot shows target
       │/   motion over time
───────┼────────────────▶ Time
       │
```

### 2. Rate Computing Section
Mechanical integrators calculated:
- Range rate (closing/opening speed)
- Bearing rate (angular velocity)
- Future position prediction

### 3. Gun Order Section
Converted range/bearing predictions to:
- Gun elevation order
- Gun bearing order
- Sight setter values

## Physical Specifications

| Specification | Value |
|--------------|-------|
| Weight | 2,200 kg (4,850 lbs) |
| Dimensions | 3.0m × 2.0m × 1.2m |
| Crew | 6 operators |
| Power | Manual cranks + electric motors |
| Plot Speed | 3 feet/minute |
| Paper Roll | 200 feet continuous |

## Operator Stations

| Station | Role |
|---------|------|
| Rate Officer | Supervises solution, judges accuracy |
| Range Plotter | Plots range readings on paper |
| Bearing Plotter | Plots bearing readings |
| Dumaresq Operator | Sets course/speed estimates |
| Calculator | Operates mechanical solver |
| Communicator | Transmits gun orders |

## The Dumaresq

The Dreyer Table incorporated a Dumaresq - a mechanical vector solver:

```
        Target Course
              ▲
              │
     Speed ───┼───▶ Target Speed
              │
              │
   ●──────────┼──────────●
 Own Ship            Target
              │
              ▼
        Rate of Change
```

The Dumaresq computed how fast range and bearing changed based on both ships' movements.

## Plotting Process

1. **Range readings** from rangefinder marked on paper
2. **Best-fit line** drawn through points
3. **Slope of line** = range rate
4. **Extrapolation** predicts future range
5. **Same process** for bearing
6. **Combine** to get gun orders

## Combat Record

**Battle of Jutland (1916)**
Early Dreyer Tables (Mk III) equipped some ships but were incomplete. Post-battle analysis drove Mk IV and Mk V development.

**Interwar Exercises**
Mk V tables proved capable at 20,000+ yards in exercises. The visual plotting helped officers understand target motion.

**WWII Service**
By WWII, older battleships still used Dreyer Tables. HMS Warspite at Calabria (1940) used her Dreyer Table to achieve hits at 26,000 yards on Giulio Cesare.

## Variants

| Model | Era | Key Features |
|-------|-----|--------------|
| Mk I | 1912 | Basic plotting only |
| Mk II | 1914 | Added Dumaresq |
| Mk III | 1915 | Improved rate solvers |
| Mk IV | 1917 | Full mechanical integration |
| Mk V | 1918 | Most refined version |
| Mk V* | 1925 | Extended range capability |

## Dreyer vs. Pollen

The Dreyer Table competed with Arthur Pollen's Argo Clock:

| Feature | Dreyer Table | Argo Clock |
|---------|--------------|------------|
| Type | Plotting + computing | Pure computing |
| Visual Feedback | Yes (paper plot) | No |
| Operator Skill | High | Lower |
| Cost | Lower | Higher |
| Rate Finding | Manual observation | Automatic |

The Navy chose Dreyer's system partly for cost, partly because officers preferred visible plotting.

## Replacement

The Dreyer Table was superseded by:
- **Admiralty Fire Control Table (AFCT)** - 1936+
- Full mechanical integration
- Faster computation
- Better for high-speed targets

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| Accuracy Bonus | +18% | Main battery fire |
| Rate Finding | Manual | Operator dependent |
| Solution Time | 45 seconds | Initial solution |
| Crew Requirement | 6 | Large team needed |
| Reliability | 88% | Complex mechanism |

## Advantages
- Visual tracking (operators see the solution)
- Proven WWI combat record
- Relatively simple repairs
- Crew can detect errors visually
- Works with optical ranging only

## Disadvantages
- Large crew requirement
- Slower than pure mechanical systems
- Manual rate determination
- Paper plotting limits speed
- Superseded by AFCT by WWII

## Legacy

The Dreyer Table established principles used in all subsequent fire control:
1. Continuous tracking (not discrete shots)
2. Rate-based prediction
3. Mechanical computation of ballistics
4. Integration of multiple data sources

## Cross-References
- [[Computers/Admiralty-FCT-Mk-X|Admiralty FCT Mk X (Successor)]]
- [[Directors/DCT-Mk-II|DCT Director]]
- [[/GDD/04-Ships/Great-Britain/Battleships/Queen-Elizabeth-Class|Ships using Dreyer Table]]

---
*The Dreyer Table was the first true fire control computer - a mechanical brain that turned the chaos of naval gunnery into calculable science.*
