# Crew-Module Interaction Mechanics

**Document Type**: Core Mechanics Implementation
**Status**: Active Development
**Tags**: [mechanics, crew, modules, efficiency, casualties, navy-field-inspired]
**Last Updated**: 2025-12-10

---

## Overview

This document defines how crew cards interact with ship modules to determine combat effectiveness. The system combines Navy Field's crew card mechanics with a physics-based weight system to create meaningful crew management decisions.

**Core Principles:**
1. **One Crew Card Per Module** - Each module slot accepts exactly one crew card
2. **Generic Classifications** - A Gunner can operate ANY gun mount (main, secondary, AA)
3. **Efficiency = Sailors × Stats** - Performance depends on both crew survival and skill
4. **Weight Gating** - Mount capacity limits which crews can be assigned (module + crew weight)
5. **Localized Casualties** - Hits damage specific crew cards, not ship-wide pools

---

## Crew Assignment System

### Basic Rules

Every module that requires crew has exactly **one crew slot**. The crew slot accepts crew cards of the appropriate classification.

```
Assignment_Rules:
  - Each module has ONE crew slot
  - Crew card classification must match module type
  - Crew card weight + Module weight must fit mount capacity
  - Modules without assigned crew are NON-FUNCTIONAL
  - Crew cards with 0 sailors remain assigned but module is NON-FUNCTIONAL
```

### Classification → Module Type Mapping

| Module Category | Required Classification | Notes |
|-----------------|------------------------|-------|
| Main Battery Turret | Gunner | Any caliber main gun |
| Secondary Battery | Gunner | Casemate or turret secondaries |
| AA Battery | AA Specialist | Light, medium, or heavy AA |
| Torpedo Tubes | Torpedo Specialist | Surface or submarine tubes |
| Depth Charge Rack | Torpedo Specialist | ASW weapons |
| Engine Room | Engineer | All propulsion systems |
| Damage Control Station | Damage Control | DC centers, firefighting |
| Radar System | Electronics | All radar types |
| Sonar System | Sonar Operator | Hydrophones, active sonar |
| Fire Control Director | Electronics | Gunnery fire control |
| Communications | Electronics | Radio, signal equipment |
| SIGINT/EW Systems | Electronics | Intercept, jamming |
| Bridge | Command Officer | Ship command center |
| Aircraft Hangar | Squadron Leader | Carrier aviation ops |
| Fighter Squadron | Fighter Pilot | CAP and interception |
| Bomber Squadron | Bomber Pilot | Strike operations |
| Submarine Control | Submarine Commander | Sub bridge/conn |
| Diving Station | Planesman | Depth control |

### Neutral Crew Flexibility

**Neutral crews** (unclassified, Level 1-24) can be assigned to ANY module type with a **-20% efficiency penalty**. This allows emergency crewing but incentivizes proper classification.

```
Neutral_Crew_Assignment:
  - Can fill any module slot regardless of type
  - Suffers -20% base efficiency penalty
  - Still affected by sailor count and stat values
  - Intended for: emergencies, early game, backup
```

---

## Module Efficiency System

### Core Formula

Module efficiency determines how well the module performs compared to its base stats. Efficiency is calculated from two factors:

```
Module_Efficiency = Sailor_Factor × Stat_Factor

Where:
  Sailor_Factor = Current_Sailors / Max_Sailors
  Stat_Factor = Stat_Modifier based on relevant primary stat(s)
```

### Sailor Factor (Casualty Scaling)

The sailor count represents the crew card's **resilience buffer**. More sailors = more ability to absorb casualties while maintaining function.

```
Sailor_Factor = Current_Sailors / Max_Sailors

Examples:
  Level 1 Crew (10 max sailors):
    10/10 = 100% sailor factor
    5/10 = 50% sailor factor
    1/10 = 10% sailor factor
    0/10 = 0% (module non-functional)

  Level 100 Crew (455 max sailors):
    455/455 = 100% sailor factor
    355/455 = 78% sailor factor
    155/455 = 34% sailor factor
    1/455 = 0.2% sailor factor (barely functional)
```

**Key Insight**: Higher level crews have more "depth" to absorb casualties. A hit that kills 50 sailors devastates a Level 1 crew but barely affects a Level 100 crew.

### Stat Factor (Skill Scaling)

Each crew stat modifies efficiency based on its value relative to baseline (15):

```
Stat_Factor = 1.0 + ((Primary_Stat - 15) × 0.02)

Stat Value → Stat Factor:
  Stat 7:  1.0 + ((7 - 15) × 0.02)  = 0.84 (16% penalty)
  Stat 15: 1.0 + ((15 - 15) × 0.02) = 1.00 (baseline)
  Stat 25: 1.0 + ((25 - 15) × 0.02) = 1.20 (+20% bonus)
  Stat 35: 1.0 + ((35 - 15) × 0.02) = 1.40 (+40% bonus)
  Stat 45: 1.0 + ((45 - 15) × 0.02) = 1.60 (+60% bonus)
  Stat 50: 1.0 + ((50 - 15) × 0.02) = 1.70 (+70% bonus, cap)
```

### Combined Efficiency Examples

**Example 1: Fresh Level 1 Crew**
```
Level 1 Gunner: 10 sailors, Accuracy 11, Reload 12
Sailor_Factor: 10/10 = 100%
Accuracy_Factor: 1.0 + ((11 - 15) × 0.02) = 0.92
Reload_Factor: 1.0 + ((12 - 15) × 0.02) = 0.94

Spread Efficiency: 100% × 0.92 = 92% of base spread
Reload Efficiency: 100% × 0.94 = 94% of base reload
```

**Example 2: Veteran Level 100 Crew at Full Strength**
```
Level 100 Gunner: 455 sailors, Accuracy 35, Reload 32
Sailor_Factor: 455/455 = 100%
Accuracy_Factor: 1.0 + ((35 - 15) × 0.02) = 1.40
Reload_Factor: 1.0 + ((32 - 15) × 0.02) = 1.34

Spread Efficiency: 100% × 1.40 = 140% (40% tighter spread)
Reload Efficiency: 100% × 1.34 = 134% (34% faster reload)
```

**Example 3: Veteran Crew After Heavy Casualties**
```
Level 100 Gunner: 155/455 sailors (300 casualties), Accuracy 35, Reload 32
Sailor_Factor: 155/455 = 34%
Accuracy_Factor: 1.40
Reload_Factor: 1.34

Spread Efficiency: 34% × 1.40 = 47.6%
Reload Efficiency: 34% × 1.34 = 45.6%

Result: Despite veteran skill, heavy casualties cripple performance
```

**Example 4: Crew at Minimum Function**
```
Level 100 Gunner: 1/455 sailors (454 casualties), Accuracy 35
Sailor_Factor: 1/455 = 0.22%
Accuracy_Factor: 1.40

Spread Efficiency: 0.22% × 1.40 = 0.31%

Result: Module barely functions - essentially random fire
```

---

## Stat-to-Module Effect Mapping

### Gunner (Main/Secondary Batteries)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Accuracy** (Primary) | Shell Spread | `Final_Spread = Base_Spread × (2.0 - Efficiency)` |
| **Reload** (Primary) | Fire Rate | `Final_Reload = Base_Reload / Efficiency` |
| **Range** (Secondary) | Max Effective Range | `Final_Range = Base_Range × Efficiency` |

**Accuracy Clarification**: Accuracy affects the **spread** of shells around your aim point, NOT whether you hit. A high-accuracy gunner lands shells in a tighter pattern - you still need to aim correctly.

```
Spread_Example:
  16"/50 Turret Base_Spread: ±400m at 20km range

  Accuracy 15 Gunner (1.0 factor): ±400m spread
  Accuracy 35 Gunner (1.4 factor): ±286m spread (400 / 1.4)
  Accuracy 50 Gunner (1.7 factor): ±235m spread (400 / 1.7)
```

### AA Specialist (Anti-Aircraft Batteries)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **AA Accuracy** (Primary) | Hit Rate vs Aircraft | `Hit_Chance = Base_Hit × Efficiency` |
| **AA Reload** (Primary) | Sustained Fire Rate | `Final_Reload = Base_Reload / Efficiency` |
| **Detection** (Secondary) | Aircraft Spotting Range | `Spot_Range = Base_Range × Efficiency` |

### Torpedo Specialist (Torpedo Tubes, Depth Charges)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Torpedo Accuracy** (Primary) | Torpedo Spread Angle | `Final_Spread = Base_Spread / Efficiency` |
| **Tube Reload** (Primary) | Reload Time | `Final_Reload = Base_Reload / Efficiency` |
| **Spread Control** (Secondary) | Pattern Tightness | `Pattern_Mod = Efficiency` |

### Engineer (Propulsion Systems)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Engine Power** (Primary) | Speed & Acceleration | `Speed_Mod = 0.7 + (0.3 × Efficiency)` |
| **Repair Speed** (Primary) | Engine Self-Repair | `Repair_Rate = Base_Rate × Efficiency` |
| **Restore Speed** (Secondary) | Disabled Recovery | `Restore_Time = Base_Time / Efficiency` |

**Note**: Engine efficiency has a floor of 70% - even badly damaged engines provide some propulsion.

### Damage Control (DC Systems)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Fire Fighting** (Primary) | Fire Suppression Speed | `Extinguish_Time = Base_Time / Efficiency` |
| **Flood Control** (Primary) | Pump Rate | `Pump_Rate = Base_Rate × Efficiency` |
| **Repair Speed** (Secondary) | Hull Repair Rate | `Repair_Rate = Base_Rate × Efficiency` |

### Electronics (Radar, Fire Control, Communications)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Detection Range** (Primary) | Radar/Sensor Range | `Det_Range = Base_Range × Efficiency` |
| **Radar Accuracy** (Primary) | Target Lock Speed | `Lock_Time = Base_Time / Efficiency` |
| **Jamming** (Secondary) | ECM Effectiveness | `Jam_Effect = Base_Effect × Efficiency` |

### Sonar Operator (Sonar Systems)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Sonar Range** (Primary) | Detection Radius | `Det_Range = Base_Range × Efficiency` |
| **Contact Analysis** (Primary) | ID Speed & Accuracy | `ID_Time = Base_Time / Efficiency` |
| **Noise Reduction** (Secondary) | Own Ship Quieting | `Signature = Base × (2.0 - Efficiency)` |

### Command Officer (Bridge)

| Stat | Module Effect | Formula |
|------|--------------|---------|
| **Command** (Primary) | All Crew Stat Bonus | `Bonus = (Command - 15) × 0.025` |
| **Tactics** (Primary) | Damage Output/Mitigation | `Tac_Bonus = (Tactics - 15) × 0.02` |
| **Leadership** (Secondary) | Low-HP Efficiency | `Crisis_Bonus` when ship <50% HP |

**Command Multiplier**: The Command stat provides a **force multiplier** to ALL other crew cards on the ship:
```
Effective_Crew_Stat = Base_Stat × (1 + Command_Bonus)

Example: Level 150 Command Officer with Command 40
  Command_Bonus = (40 - 15) × 0.025 = 0.625 (+62.5%)

  A Gunner with Accuracy 30 effectively has:
  Effective_Accuracy = 30 × 1.625 = 48.75
```

---

## Casualty Mechanics

### Localized Damage

When a module takes a direct hit, **only that module's crew card** suffers casualties:

```
Casualty_Calculation:
  Damage_to_Module → Crew_Casualties

  Casualties = (Damage / Module_HP) × Crew_Sailor_Count × Lethality_Factor

  Lethality_Factor by damage type:
    HE Shell: 0.15 (fires, fragmentation)
    AP Shell (penetrating): 0.25 (internal damage)
    AP Shell (non-pen): 0.05 (spalling only)
    Torpedo: 0.10 (flooding focused)
    Bomb: 0.20 (concussion, fire)
```

**Example: Main Turret Hit**
```
16" Turret HP: 5,000
HE Shell deals: 1,200 damage
Crew Card: Level 100 Gunner (455 sailors)

Casualties = (1200 / 5000) × 455 × 0.15
Casualties = 0.24 × 455 × 0.15 = 16 sailors killed

Result: 455 → 439 sailors (96.5% efficiency from sailor factor)
```

### Penetrating Damage Cascade

A penetrating hit may damage modules **behind** the initial impact:

```
Penetration_Cascade:
  Shell penetrates Turret → continues into Barbette → into Magazine

  Each module in path takes:
    Damage = Remaining_Energy × Penetration_Factor

  Each module's crew takes casualties separately
```

### Fire & Flooding (Ship-Wide)

Fire and flooding cause **distributed casualties** across ALL crew cards:

```
Fire_Casualties:
  Per_Tick = Fire_Intensity × Ship_Total_Sailors × 0.002
  Distributed proportionally across all crew cards

  Example:
    Fire Intensity 50%, Ship has 2,000 total sailors
    Per_Tick = 0.5 × 2000 × 0.002 = 2 sailors/tick
    Spread across all crew cards by percentage of total

Flood_Casualties:
  Per_Tick = Flood_Severity × Ship_Total_Sailors × 0.003
  Concentrated in flooded compartments first

  Flooded compartment modules take 3x casualty rate
```

### Crew Card Survival Rules

```
Crew_Card_Rules:
  - Sailor count can drop to 0 during combat
  - At 0 sailors: Module NON-FUNCTIONAL, crew card REMAINS ASSIGNED
  - Crew card is NOT destroyed by casualties (only by permadeath system)
  - At port: Replenish sailors with credits
  - Even 1 sailor remaining = module functions at minimal efficiency
```

---

## Weight System Integration

### Mount Weight Capacity

Every module mount has a **weight capacity** that must accommodate both the module AND its crew:

```
Mount_Fitting_Check:
  Total_Weight = Module_Weight + Crew_Card_Weight

  IF Total_Weight > Mount_Capacity THEN
    Cannot assign this crew card to this module
  ELSE
    Assignment successful
```

### Crew Card Weight Formula

From Crew-Management.md:
```
Crew_Weight = Sailor_Count × Base_Weight × Level_Modifier

Base_Weight: 0.1 ton per sailor
Level_Modifier: 1.0 + (Level / 100)

Examples:
  Level 1 (10 sailors):   10 × 0.1 × 1.01 = 1.01 tons
  Level 50 (255 sailors): 255 × 0.1 × 1.50 = 38.3 tons
  Level 100 (455 sailors): 455 × 0.1 × 2.00 = 91 tons
  Level 200 (705 sailors): 705 × 0.1 × 3.00 = 211.5 tons
```

### Natural Gating Examples

**1900s Destroyer Turret Mount**
```
Mount Capacity: 30 tons
5"/38 Turret Weight: 18 tons
Available for Crew: 12 tons

Maximum Crew Level: ~Level 25 (12.6 tons)
Level 100 Crew (91 tons): CANNOT FIT
Level 200 Crew (211 tons): CANNOT FIT

Result: Early destroyers limited to low-level crews
```

**1940s Battleship Main Turret Mount**
```
Mount Capacity: 3,000 tons
16"/50 Triple Turret Weight: 1,700 tons
Available for Crew: 1,300 tons

Maximum Crew Level: Level 200 easily fits (211 tons)
Can accommodate multiple crew cards if module design allows

Result: Capital ships can field veteran crews
```

### Current Sailor Count & Weight

**Important**: Crew weight is based on **MAX sailor count**, not current:

```
Weight_Rule:
  Crew_Weight = MAX_Sailors × Weight_Formula

  NOT affected by casualties

  Rationale: The "weight" represents equipment, quarters, supplies
             for the full crew complement, not just survivors
```

---

## Unmanned Module Behavior

### Functional Requirements

Modules that require crew will **not function** without an assigned crew card with at least 1 sailor:

```
Module_Function_Check:
  IF No_Crew_Assigned:
    Module.Functional = false
    Module displays "UNMANNED" status

  ELSE IF Crew_Sailors == 0:
    Module.Functional = false
    Module displays "CREW WIPED OUT" status
    Crew card remains assigned (can replenish at port)

  ELSE:
    Module.Functional = true
    Performance = Base_Stats × Efficiency
```

### Module Categories by Crew Requirement

| Category | Requires Crew | Notes |
|----------|--------------|-------|
| Weapons (all) | YES | Turrets, torpedoes, AA, depth charges |
| Detection | YES | Radar, sonar, lookouts |
| Propulsion | YES | Engines require engineers |
| Damage Control | YES | DC stations need crew |
| Communications | YES | Radio, signals |
| Bridge | YES | Command requires officers |
| Aviation | YES | Hangars, squadrons |

**Note**: There are no "passive" module types that work without crew. Armor is applied to hull zones (not a module), and systems like fuel storage are part of the hull design, not installable modules.

---

## UI Display Requirements

### Module Status Indicators

```
Module_Status_Display:
  - Module Name
  - Assigned Crew: [Crew Card Name] or "UNMANNED"
  - Sailor Count: Current / Max
  - Efficiency: XX% (color coded)
  - Primary Stat Effects: +XX% Spread, +XX% Reload

Color Coding:
  Green (80-100%): Fully operational
  Yellow (50-79%): Degraded performance
  Orange (25-49%): Severely degraded
  Red (1-24%): Critical / Barely functional
  Gray (0%): Non-functional
```

### Fitting Screen Requirements

When assigning crew to modules:
```
Display:
  - Mount Weight Capacity: XXX tons
  - Module Weight: XXX tons
  - Available for Crew: XXX tons
  - Crew Card Weight: XXX tons
  - FIT CHECK: [FITS] or [TOO HEAVY]

  - Projected Efficiency: XX%
  - Projected Stat Effects: +XX% Accuracy, +XX% Reload
```

---

## Combat Integration

### Real-Time Updates

During combat, the following update in real-time:

```
Real_Time_Updates:
  - Sailor count (after each casualty event)
  - Efficiency (recalculated after casualties)
  - Module performance (spread, reload, etc.)
  - Module status (functional/non-functional)
```

### Performance Degradation Sequence

```
Damage_Sequence:
  1. Module takes hit
  2. Calculate crew casualties from hit
  3. Update sailor count
  4. Recalculate efficiency
  5. Apply new efficiency to module performance
  6. If sailors = 0, module becomes non-functional
  7. Display updated status to player
```

---

## Cross-Reference Documents

**Related Systems:**
- [[Crew-Management]] - Crew card structure, weight system
- [[Crew-Skills]] - Stat definitions and classifications
- [[Crew-Progression]] - Leveling and XP mechanics
- [[Crew-Permadeath]] - Crew card death conditions
- [[Module-Dependencies]] - Module requirements and synergies
- [[Ballistics-Gunnery-Mechanics]] - How spread affects combat
- [[Status-Effects-Mechanics]] - Fire and flooding effects

---

## Summary: Key Mechanics

### Quick Reference

1. **One crew card per module** - Generic classifications (Gunner works on any turret)
2. **Efficiency = Sailors × Stats** - Both matter for performance
3. **Sailor count = casualty buffer** - Veterans absorb losses better
4. **Mount weight = module + crew** - Natural gating for veteran crews
5. **0 sailors = non-functional** - But crew card survives for replenishment
6. **Localized casualties** - Turret hit → that turret's crew suffers
7. **Fire/flood = ship-wide** - Distributed casualties across all crew

### Design Goals Achieved

- **Navy Field Heritage**: Crew cards with sailor counts, stats affecting performance
- **Weight-Based Gating**: No artificial era restrictions, physics determines limits
- **Meaningful Progression**: Higher level crews are both more skilled AND more resilient
- **Tactical Depth**: Crew placement, casualty management, retreat decisions
- **Clear Feedback**: Players understand why modules perform as they do

---

*This document provides the framework for crew-module interactions. Specific values may be adjusted during balance testing.*
