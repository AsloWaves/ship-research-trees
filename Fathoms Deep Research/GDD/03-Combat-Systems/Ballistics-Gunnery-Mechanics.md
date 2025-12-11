# Ballistics & Gunnery Mechanics

**Document Type**: Core Mechanics Implementation
**Status**: Active Development
**Tags**: [mechanics, combat, gunnery, ballistics, formulas, fire-control]
**Last Updated**: 2025-01-17

---

## Overview

This document defines the mathematical formulas and logic for naval gunnery in Fathoms Deep. It integrates with the Detection System's firing solution mechanics, fire control modules, crew skills, and environmental factors to create a cohesive combat resolution system.

**Design Philosophy**: Gunnery should reward:
1. **Positioning** - Range and angle matter
2. **Patience** - Building firing solutions before shooting
3. **Equipment** - Fire control modules improve accuracy
4. **Skill** - Manual targeting offers highest accuracy ceiling
5. **Tactics** - Choosing when to fire (movement vs. accuracy trade-off)

---

## Core Hit Probability Formula

### Master Accuracy Calculation

```
Hit_Probability = Base_Accuracy
                  × Solution_Modifier
                  × Range_Modifier
                  × Fire_Control_Modifier
                  × Target_Speed_Modifier
                  × Shooter_Movement_Modifier
                  × Weather_Modifier
                  × Crew_Skill_Modifier
                  × Targeting_Mode_Modifier
```

Each modifier is a multiplier typically between 0.5 and 1.5.

---

## Base Accuracy by Gun Caliber

Base accuracy represents the inherent precision of the weapon system at optimal conditions.

| Gun Caliber | Base Accuracy | Typical Ships |
|-------------|---------------|---------------|
| 20mm-40mm | 45% | AA guns, close-in weapons |
| 3-inch (76mm) | 50% | Destroyer secondary |
| 4-inch (100mm) | 55% | Light destroyer guns |
| 5-inch (127mm) | 60% | Destroyer main, cruiser secondary |
| 6-inch (152mm) | 58% | Light cruiser main |
| 8-inch (203mm) | 55% | Heavy cruiser main |
| 11-inch (280mm) | 50% | Pocket battleship main |
| 14-inch (356mm) | 48% | Older battleship main |
| 15-inch (381mm) | 45% | Standard battleship main |
| 16-inch (406mm) | 42% | Modern battleship main |
| 18-inch (460mm) | 38% | Super battleship (Yamato) |

**Design Note**: Larger calibers have lower base accuracy due to longer reload times, greater dispersion, and the difficulty of hitting targets at typical engagement ranges. This is offset by devastating damage when hits occur.

---

## Firing Solution Modifier

> **See [[Firing-Solution-System]] for the authoritative, complete firing solution mechanics.**
> That document resolves formula contradictions and provides definitive buildup rates and caps.

The firing solution is a "living number" that affects accuracy.

### Solution Quality to Accuracy Modifier

| Solution % | Accuracy Modifier | Description |
|------------|-------------------|-------------|
| 0-10% | ×0.10 | Blind fire, almost no chance |
| 11-25% | ×0.30 | Poor solution, low probability |
| 26-50% | ×0.55 | Developing solution, moderate |
| 51-75% | ×0.75 | Good solution, reliable |
| 76-90% | ×0.90 | Excellent solution, high accuracy |
| 91-100% | ×1.00 | Perfect solution, maximum accuracy |

**Formula for continuous calculation:**
```
Solution_Modifier = 0.10 + (Solution_Percentage × 0.009)

Example: 65% solution
Solution_Modifier = 0.10 + (65 × 0.009) = 0.10 + 0.585 = 0.685
```

### Firing Without Solution

Firing with <25% solution applies severe penalties:
- ×0.5 additional penalty on top of low Solution_Modifier
- Gives away your position (muzzle flash)
- Wastes ammunition
- May be tactically useful for suppression or area denial

---

## Range Modifier

### Range Bands and Accuracy

| Range Band | Distance | Accuracy Modifier | Notes |
|------------|----------|-------------------|-------|
| Point Blank | 0-2 km | ×1.25 | Close quarters, knife-fight range |
| Short | 2-5 km | ×1.15 | Destroyer engagement range |
| Medium | 5-10 km | ×1.00 | Standard combat range (baseline) |
| Long | 10-15 km | ×0.85 | Extended engagement |
| Very Long | 15-20 km | ×0.70 | Battleship preferred range |
| Extreme | 20-30 km | ×0.50 | Maximum effective range |
| Maximum | 30+ km | ×0.30 | Plunging fire, observation required |

### Continuous Range Calculation

For precise calculations between range bands:

```
Range_Modifier = 1.25 - (Range_km × 0.03)
Minimum: 0.20
Maximum: 1.25

Example: 12 km range
Range_Modifier = 1.25 - (12 × 0.03) = 1.25 - 0.36 = 0.89
```

### Gun-Specific Range Effectiveness

Some guns are optimized for specific ranges:

| Gun Type | Optimal Range | Out-of-Range Penalty |
|----------|---------------|----------------------|
| DD Main (5") | 5-10 km | ×0.7 beyond 15 km |
| CL Main (6") | 8-15 km | ×0.6 beyond 20 km |
| CA Main (8") | 10-18 km | ×0.5 beyond 25 km |
| BB Main (14"+) | 15-25 km | ×0.5 beyond 35 km |

---

## Fire Control Equipment Modifiers

Fire control systems from modules directly improve accuracy.

### Fire Control Module Tiers

| Module Tier | Era | Accuracy Bonus | Module ID |
|-------------|-----|----------------|-----------|
| Basic Rangefinder | 1890-1920 | ×1.05 | FC-001 |
| Coincidence Rangefinder | 1910-1940 | ×1.10 | FC-002 |
| Fire Control Director | 1920-1950 | ×1.15 | FC-003 |
| Analog Computer | 1935-1960 | ×1.20 | FC-004 |
| Radar Fire Control | 1942-1970 | ×1.30 | FC-005 |
| Digital Fire Control | 1960+ | ×1.40 | FC-006 |

### Radar Integration Bonus

When radar provides range data (requires radar module):

| Radar Type | Additional Accuracy Bonus |
|------------|---------------------------|
| Search Radar Only | ×1.00 (no bonus) |
| Fire Control Radar | ×1.10 |
| Gun-Laying Radar | ×1.15 |
| Track-While-Scan | ×1.20 |

**Combined Fire Control:**
```
Fire_Control_Modifier = FC_Module_Bonus × Radar_Bonus

Example: Radar Fire Control + Gun-Laying Radar
Fire_Control_Modifier = 1.30 × 1.15 = 1.495 ≈ ×1.50
```

---

## Target Speed Modifier

Faster targets are harder to hit due to prediction difficulty.

| Target Speed | Accuracy Modifier | Notes |
|--------------|-------------------|-------|
| Stationary | ×1.20 | Dead in water, easy target |
| 0-10 knots | ×1.10 | Slow maneuvering |
| 10-20 knots | ×1.00 | Standard cruise (baseline) |
| 20-30 knots | ×0.90 | Fast maneuvering |
| 30-40 knots | ×0.80 | High speed (destroyers) |
| 40+ knots | ×0.65 | Maximum speed (PT boats) |

### Continuous Calculation

```
Target_Speed_Modifier = 1.20 - (Target_Speed_Knots × 0.015)
Minimum: 0.50
Maximum: 1.20

Example: Target at 28 knots
Target_Speed_Modifier = 1.20 - (28 × 0.015) = 1.20 - 0.42 = 0.78
```

---

## Shooter Movement Modifier

Your own ship's movement affects gunnery stability.

### Speed Penalty

| Your Speed | Accuracy Modifier | Notes |
|------------|-------------------|-------|
| Stationary | ×1.05 | Stable gun platform |
| 0-10 knots | ×1.00 | Baseline |
| 10-20 knots | ×0.95 | Slight vibration |
| 20-30 knots | ×0.90 | Moderate platform motion |
| 30+ knots | ×0.80 | Severe stability issues |

### Course Change Penalty

Turning while firing severely impacts accuracy:

| Maneuver | Accuracy Modifier | Duration |
|----------|-------------------|----------|
| Steady course | ×1.00 | - |
| Gentle turn (<5°/sec) | ×0.85 | While turning |
| Standard turn (5-10°/sec) | ×0.70 | While turning |
| Hard turn (>10°/sec) | ×0.50 | While turning |
| Emergency maneuver | ×0.30 | While turning + 5 sec after |

### Combined Shooter Movement

```
Shooter_Movement_Modifier = Speed_Modifier × Turn_Modifier

Example: 25 knots, standard turn
Speed_Modifier = 0.90
Turn_Modifier = 0.70
Shooter_Movement_Modifier = 0.90 × 0.70 = 0.63
```

**Tactical Implication**: Maintaining steady course at moderate speed maximizes accuracy but makes you predictable. High-speed maneuvering sacrifices accuracy for survivability.

---

## Weather Modifier

See also: Detection-System.md for weather effects on visibility.

| Weather Condition | Accuracy Modifier | Notes |
|-------------------|-------------------|-------|
| Calm seas, clear day | ×1.10 | Optimal conditions |
| Light seas, clear | ×1.00 | Baseline |
| Moderate seas | ×0.90 | Some roll/pitch |
| Heavy seas | ×0.75 | Significant platform motion |
| Storm conditions | ×0.55 | Extreme difficulty |
| Fog/Rain | ×0.85 | Reduced visibility (visual targeting) |
| Night (no radar) | ×0.60 | Visual targeting only |
| Night (with radar) | ×0.90 | Radar-assisted targeting |

### Weather Effect Stacking

```
Weather_Modifier = Sea_State_Modifier × Visibility_Modifier × Time_of_Day_Modifier

Example: Moderate seas, rain, night with radar
Sea_State = 0.90
Visibility = 0.85
Time = 0.90
Weather_Modifier = 0.90 × 0.85 × 0.90 = 0.689
```

---

## Crew Skill Modifier

Crew skills from the Crew-Skills system modify gunnery performance.

### Gunner Accuracy Skill

| Skill Level | Accuracy Modifier | Description |
|-------------|-------------------|-------------|
| 1 (Untrained) | ×0.50 | New recruit |
| 7 (Novice) | ×0.70 | Basic training complete |
| 15 (Trained) | ×1.00 | Baseline (fully trained) |
| 25 (Experienced) | ×1.20 | Veteran gunner |
| 35 (Expert) | ×1.40 | Elite performance |
| 50 (Legendary) | ×1.60 | Master gunner |

### Formula

```
Crew_Skill_Modifier = 0.50 + (Skill_Level × 0.022)

Example: Skill level 30
Crew_Skill_Modifier = 0.50 + (30 × 0.022) = 0.50 + 0.66 = 1.16
```

---

## Targeting Mode Modifier

Based on the fire control mode selected by the player.

| Targeting Mode | Accuracy Modifier | Critical Bonus | Requirements |
|----------------|-------------------|----------------|--------------|
| Auto-Target | ×0.85 | ×1.0 | Auto Fire Control module |
| Assisted Target | ×1.00 | ×1.0 | Default mode |
| Manual Target | ×1.15 | ×1.25 | Manual Fire Director module |

**Manual Targeting Bonus**: Players who master shell flight times and target prediction gain significant advantages. The critical hit bonus compounds this reward.

---

## Shell Dispersion Mechanics

Dispersion determines the spread pattern of shells around the aim point.

### Base Dispersion by Caliber

| Gun Caliber | Base Dispersion (meters) | At 10km | At 20km |
|-------------|--------------------------|---------|---------|
| 5-inch (127mm) | 50m | 100m | 200m |
| 6-inch (152mm) | 65m | 130m | 260m |
| 8-inch (203mm) | 85m | 170m | 340m |
| 11-inch (280mm) | 110m | 220m | 440m |
| 14-inch (356mm) | 140m | 280m | 560m |
| 15-inch (381mm) | 155m | 310m | 620m |
| 16-inch (406mm) | 170m | 340m | 680m |
| 18-inch (460mm) | 200m | 400m | 800m |

### Dispersion Formula

```
Actual_Dispersion = Base_Dispersion × (Range_km / 10) × FC_Dispersion_Modifier × Weather_Dispersion_Modifier

FC_Dispersion_Modifier:
- No fire control: ×1.50
- Basic: ×1.30
- Coincidence: ×1.15
- Director: ×1.00
- Analog Computer: ×0.85
- Radar FC: ×0.70
- Digital FC: ×0.60

Weather_Dispersion_Modifier:
- Calm: ×0.90
- Moderate: ×1.00
- Heavy: ×1.25
- Storm: ×1.50
```

### Salvo Dispersion Pattern

Shells in a salvo fall within an ellipse:
- **Long axis** (range dispersion): Full dispersion value
- **Short axis** (lateral dispersion): 50% of dispersion value

```
Example: 16-inch guns at 20km with Analog Computer, moderate seas
Base_Dispersion = 170m
Range_Factor = 20/10 = 2.0
FC_Modifier = 0.85
Weather_Modifier = 1.00

Actual_Dispersion = 170 × 2.0 × 0.85 × 1.00 = 289m (long axis)
Lateral_Dispersion = 289 × 0.5 = 144m (short axis)

Shells will land within a 289m × 144m ellipse centered on aim point.
```

---

## Shell Flight Time

Shell flight time determines how far ahead to aim for moving targets.

### Flight Time by Caliber and Range

| Caliber | 5km | 10km | 15km | 20km | 25km | 30km |
|---------|-----|------|------|------|------|------|
| 5-inch | 5s | 12s | 20s | 30s | - | - |
| 6-inch | 6s | 13s | 22s | 33s | - | - |
| 8-inch | 7s | 15s | 25s | 38s | 52s | - |
| 11-inch | 8s | 17s | 28s | 42s | 58s | - |
| 14-inch | 10s | 20s | 32s | 46s | 62s | 80s |
| 15-inch | 11s | 22s | 35s | 50s | 68s | 88s |
| 16-inch | 12s | 24s | 38s | 54s | 72s | 94s |
| 18-inch | 14s | 28s | 44s | 62s | 84s | 108s |

### Flight Time Formula

```
Flight_Time = (Range_km × Shell_Speed_Factor) + Range_km²/Velocity_Factor

Simplified approximation:
Flight_Time_Seconds ≈ Range_km × 1.2 × Caliber_Factor

Caliber_Factor:
- 5-inch: 1.0
- 8-inch: 1.1
- 14-inch: 1.3
- 16-inch: 1.4
- 18-inch: 1.5
```

### Lead Calculation for Moving Targets

```
Lead_Distance = Target_Speed_Meters_Per_Second × Flight_Time

Example: Target moving at 25 knots (12.9 m/s), range 15km, 16-inch guns
Flight_Time = 38 seconds
Lead_Distance = 12.9 × 38 = 490 meters

Player must aim 490m ahead of the target's current position.
```

---

## Complete Hit Probability Example

### Scenario: USS Iowa vs IJN Kongo

**Conditions:**
- Range: 18 km
- Your speed: 20 knots, steady course
- Target speed: 28 knots, steady course
- Weather: Moderate seas, clear day
- Fire control: Radar Fire Control + Gun-Laying Radar
- Crew: Gunner skill 25
- Targeting: Assisted
- Firing solution: 75%

**Calculation:**

| Factor | Value | Modifier |
|--------|-------|----------|
| Base Accuracy (16-inch) | - | 0.42 |
| Solution (75%) | 0.10 + (75 × 0.009) | ×0.775 |
| Range (18km) | 1.25 - (18 × 0.03) | ×0.71 |
| Fire Control (RFC + GLR) | 1.30 × 1.15 | ×1.50 |
| Target Speed (28kn) | 1.20 - (28 × 0.015) | ×0.78 |
| Your Speed (20kn, steady) | - | ×0.95 |
| Weather (moderate, clear) | 0.90 × 1.00 | ×0.90 |
| Crew Skill (25) | 0.50 + (25 × 0.022) | ×1.05 |
| Targeting (Assisted) | - | ×1.00 |

```
Hit_Probability = 0.42 × 0.775 × 0.71 × 1.50 × 0.78 × 0.95 × 0.90 × 1.05 × 1.00
                = 0.42 × 0.775 × 0.71 × 1.50 × 0.78 × 0.95 × 0.90 × 1.05
                = 0.234 or 23.4%
```

**Result**: Each shell has approximately a 23% chance to hit. In a 9-gun salvo, expected hits: 2.1 shells.

---

## Fire Control Integration with Detection System

### How Detection Affects Gunnery

The Detection System (see Detection-System.md) determines what information is available for fire control:

| Detection Phase | Gunnery Capability |
|-----------------|---------------------|
| Phase 1 (Direction only) | Cannot target, no firing solution |
| Phase 2 (Shadow) | Can attempt blind fire at bearing, ×0.1 accuracy |
| Phase 3 (Sprite) | Can build firing solution, normal gunnery rules |
| Phase 4 (Full Detail) | Full information, optimal solution building |

### Firing Solution Building Rate

From Detection-System.md, solution builds based on equipment:

| Equipment Tier | Base Buildup | Max Solution |
|----------------|--------------|--------------|
| Basic (Pre-1920) | 2%/sec | 70% |
| Standard (1920-1940) | 5%/sec | 85% |
| Advanced (1940+) | 10%/sec | 95% |
| Modern (1960+) | 15%/sec | 100% |

**Gunnery Implication**: Even with a target in view, you must wait for solution to build for accurate fire. Patience is rewarded.

---

## Ammunition and Penetration

### Shell Selection Impact

Different shell types have different accuracy characteristics:

| Shell Type | Accuracy Modifier | Best Use Case |
|------------|-------------------|---------------|
| AP (Armor Piercing) | ×1.00 | Armored targets, citadel hits |
| APC (AP Capped) | ×1.00 | Better penetration angles |
| HE (High Explosive) | ×1.05 | Unarmored targets, fires |
| HC (High Capacity) | ×1.05 | Maximum HE damage |
| SAP (Semi-AP) | ×1.02 | Balanced damage |
| Common | ×1.00 | Basic AP performance |

### Penetration at Range

Penetration decreases with range due to velocity loss:

```
Effective_Penetration = Base_Penetration × Range_Retention_Factor

Range_Retention_Factor:
- 0-5km: ×1.00
- 5-10km: ×0.90
- 10-15km: ×0.80
- 15-20km: ×0.70
- 20-25km: ×0.60
- 25-30km: ×0.50
- 30+km: ×0.40
```

See Ammunition folder for specific shell penetration values.

---

## Balance Notes

### Intended Gameplay Balance

**Destroyers vs Battleships:**
- Destroyers have high base accuracy (5-inch: 60%)
- Battleships have low base accuracy (16-inch: 42%)
- BUT battleship fire control is typically better
- AND battleship hits are devastating
- Result: Destroyers rely on volume, battleships on precision

**Close vs Long Range:**
- Close range heavily favors smaller, faster ships
- Long range heavily favors ships with better fire control
- Medium range is the balanced engagement zone

**Static vs Mobile:**
- Stationary targets are easier to hit (×1.20)
- Fast movers are hard to hit (×0.65 at 40+ knots)
- YOUR movement also hurts accuracy (×0.80 at 30+ knots)
- Creates "stand and fight vs run and dodge" tactical choices

**Equipment Progression:**
- Era-appropriate fire control matters significantly
- Modern fire control (×1.40) vs Basic (×1.05) = 33% accuracy difference
- Radar bonus stacks multiplicatively
- Rewards players who invest in fire control modules

### Critical Hit Interaction

From Damage-Model.md:
- Base critical chance: 10%
- Manual targeting: +25% critical chance
- Solution quality: Affects critical chance proportionally
- Module hits: +10% critical chance

High accuracy builds naturally lead to more critical hits, creating a positive feedback loop for skilled play.

---

## Implementation Notes

### For Programmers

1. **Calculation Order**: Always multiply in the order shown to ensure consistent results
2. **Minimum Values**: Most modifiers have minimums (0.20 for range, 0.50 for speed, etc.)
3. **Capping**: Final hit probability should be capped at 95% maximum (never guaranteed)
4. **Random Variation**: Apply ±10% random variation to final result for gameplay variety
5. **Update Frequency**: Recalculate hit probability every 0.5 seconds for smooth UI updates
6. **Salvo Calculation**: Roll hit chance separately for each shell in a salvo

### Integration Points

- **Detection-System.md**: Provides firing solution percentage
- **Damage-Model.md**: Receives hit results for damage calculation
- **Crew-Skills.md**: Provides gunner skill values
- **Module-System.md**: Provides fire control module bonuses
- **Weather-System**: Provides environmental modifiers

---

## Cross-Reference Documents

**Related Combat Systems:**
- [[Detection-System]] - Contact information and firing solution
- [[Damage-Model]] - Hit damage and penetration
- [[Surface-Combat]] - Tactical scenarios and examples

**Related Module Documents:**
- [[Fire-Control-Director]] - Fire control modules
- [[Radar modules]] - Radar fire control integration

**Related Systems:**
- [[Crew-Skills]] - Gunner skill progression
- [[Weather-System]] - Environmental effects

---

## Summary Table: Quick Reference

| Factor | Typical Range | Impact |
|--------|---------------|--------|
| Base Accuracy | 38-60% | Foundation |
| Solution Quality | ×0.10-1.00 | CRITICAL |
| Range | ×0.30-1.25 | Major |
| Fire Control | ×1.05-1.40 | Major |
| Target Speed | ×0.65-1.20 | Moderate |
| Your Movement | ×0.30-1.05 | Moderate |
| Weather | ×0.50-1.10 | Variable |
| Crew Skill | ×0.50-1.60 | Major |
| Targeting Mode | ×0.85-1.15 | Minor |

**Most Impactful Factors:**
1. Firing Solution Quality (×0.10 to ×1.00 - 10x range!)
2. Crew Skill (×0.50 to ×1.60 - 3x range)
3. Range (×0.30 to ×1.25 - 4x range)
4. Fire Control Equipment (×1.05 to ×1.40 × radar bonuses)

---

*This document provides the core mathematical framework for naval gunnery. Specific values may be adjusted during balance testing.*
