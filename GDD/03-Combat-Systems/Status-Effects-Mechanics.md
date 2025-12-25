# Status Effects Mechanics

**Document Type**: Core Mechanics Implementation
**Status**: Active Development
**Tags**: [mechanics, combat, damage, fire, flooding, critical-hits, repair]
**Last Updated**: 2025-01-17

---

## Overview

Status effects represent ongoing damage and system degradation that ships suffer in combat. Unlike direct HP damage, status effects create emergent tactical situations requiring active management and difficult decisions.

**Design Philosophy:**
1. **Progressive Danger** - Effects worsen over time if unaddressed
2. **Resource Trade-offs** - Damage control is limited, forcing prioritization
3. **Tactical Depth** - Causing specific status effects is a valid combat strategy
4. **Extraction Tension** - Accumulated status effects threaten mission success

---

## Fire System

### Fire Initiation

Fires can start from various damage sources:

| Damage Source | Fire Chance | Notes |
|---------------|-------------|-------|
| HE Shell Hit | 15-25% | Higher caliber = higher chance |
| SAP Shell Hit | 8-12% | Lower than HE |
| AP Shell Penetration | 3-5% | Internal detonation only |
| Bomb Hit (Dive Bomber) | 25-35% | High incendiary effect |
| Rocket Hit | 20-30% | Aircraft rockets |
| Secondary Explosion | 40-60% | Ammunition/fuel detonation |
| Damage Control Failure | 5-10% | Failed repair attempt |

### Fire Intensity Levels

Each fire has an intensity level that determines damage rate:

| Intensity | Damage Rate | Spread Chance | Duration | Visual |
|-----------|-------------|---------------|----------|--------|
| Smoldering | 0.1% HP/sec | 5%/10 sec | 30 sec | Light smoke |
| Minor | 0.2% HP/sec | 10%/10 sec | 45 sec | Small flames |
| Standard | 0.3% HP/sec | 15%/10 sec | 60 sec | Medium flames |
| Major | 0.5% HP/sec | 25%/10 sec | 90 sec | Large flames |
| Inferno | 1.0% HP/sec | 40%/10 sec | Until extinguished | Massive fire |

### Fire Intensity Escalation

Unattended fires intensify over time:

```
Fire_Escalation:
- Smoldering → Minor: After 15 seconds unattended
- Minor → Standard: After 20 seconds unattended
- Standard → Major: After 30 seconds unattended
- Major → Inferno: After 45 seconds unattended

De-escalation (partial suppression):
- Inferno → Major: 50% damage control progress
- Major → Standard: 40% damage control progress
- Standard → Minor: 30% damage control progress
```

### Fire Spread Mechanics

Fires can spread to create multiple fire zones:

```
Spread_Chance_Per_Interval = Base_Spread_Chance
                            × Adjacent_Fire_Modifier
                            × Material_Modifier
                            × Weather_Modifier

Adjacent_Fire_Modifier:
- 0 adjacent fires: ×1.0
- 1 adjacent fire: ×1.5
- 2+ adjacent fires: ×2.0

Material_Modifier (by ship era):
- Wooden ships (Pre-1890): ×2.0
- Early steel (1890-1920): ×1.2
- Modern steel (1920+): ×1.0
- Armored sections: ×0.5

Weather_Modifier:
- Calm: ×1.0
- Wind 10-20 kn: ×1.2
- Wind 20+ kn: ×1.5
- Rain: ×0.7
- Storm: ×0.5
```

### Maximum Fires

| Ship Class | Maximum Simultaneous Fires |
|------------|---------------------------|
| Destroyer | 3 |
| Light Cruiser | 4 |
| Heavy Cruiser | 4 |
| Battleship | 5 |
| Carrier | 6 |

### Fire Damage Calculation

```
Total_Fire_Damage_Per_Second = Σ(Individual_Fire_Damage_Rates)

Example: Cruiser with 3 fires
- Fire 1: Minor (0.2% HP/sec)
- Fire 2: Standard (0.3% HP/sec)
- Fire 3: Standard (0.3% HP/sec)
Total: 0.8% HP/sec = 48% HP per minute if unaddressed
```

### Fire Extinguishing

**Automatic Extinguishing:**
- Fires naturally burn out after their duration expires
- Intensity reduces if ship takes no new fire damage for 30 seconds

**Damage Control Party:**
```
Extinguish_Time = Base_Time × (1 / Fire_Fighting_Modifier)

Base_Time by Intensity:
- Smoldering: 5 seconds
- Minor: 10 seconds
- Standard: 15 seconds
- Major: 25 seconds
- Inferno: 40 seconds

Fire_Fighting_Modifier (from Crew Skills):
- Skill 7: ×0.75 (slower)
- Skill 15: ×1.00 (baseline)
- Skill 50: ×2.05 (much faster)
```

**Damage Control Priority:**
- Only ONE fire can be actively fought at a time per damage control party
- Choose which fire to extinguish - tactical decision
- Additional damage control modules add parties

### Fire Secondary Effects

| Effect | Trigger | Consequence |
|--------|---------|-------------|
| Ammunition Cook-off | Fire in magazine area | 10% chance of magazine detonation per 30 sec |
| Fuel Fire | Fire near fuel tanks | Fire cannot be fully extinguished, only suppressed |
| Smoke | Any fire | Reduced crew efficiency in affected areas (-10%) |
| Visibility | Major+ fire | Ship easier to detect (+20% detection range) |
| Aircraft Damage | Carrier deck fire | Aircraft on deck destroyed |

---

## Flooding System

### Flood Initiation

| Damage Source | Flood Chance | Severity |
|---------------|--------------|----------|
| Torpedo Hit | 100% | Heavy or Catastrophic |
| Mine Hit | 100% | Heavy |
| Underwater Shell Hit | 50% | Light to Standard |
| Ram Damage | 75% | Standard to Heavy |
| Depth Charge (Surface) | 60% | Standard |
| Structural Failure | 25% | Light |
| Near-Miss Bomb | 15% | Light |

### Flood Severity Levels

| Severity | Damage Rate | Speed Penalty | List Angle | Duration |
|----------|-------------|---------------|------------|----------|
| Seepage | 0.1% HP/sec | -2% | 0° | 120 sec |
| Light | 0.3% HP/sec | -5% | 2° | 90 sec |
| Standard | 0.5% HP/sec | -10% | 5° | 60 sec |
| Heavy | 1.0% HP/sec | -20% | 10° | Until repaired |
| Catastrophic | 2.0% HP/sec | -40% | 15°+ | Until repaired |

### Flooding Progression

Uncontrolled flooding worsens:

```
Flood_Progression:
- Seepage → Light: 60 seconds unaddressed
- Light → Standard: 45 seconds unaddressed
- Standard → Heavy: 30 seconds unaddressed
- Heavy → Catastrophic: 30 seconds unaddressed

Reverse (with pumping):
- Catastrophic → Heavy: 40% pump progress
- Heavy → Standard: 60% pump progress
- Standard → Light: 80% pump progress
- Light → Seepage: 100% pump progress (sealed)
```

### Multiple Flood Sources

Unlike fire, multiple torpedo hits create multiple flood zones:

| Ship Class | Maximum Flood Zones | Typical Survivable Torpedoes |
|------------|--------------------|-----------------------------|
| Destroyer | 2 | 1-2 |
| Light Cruiser | 3 | 2-3 |
| Heavy Cruiser | 3 | 2-4 |
| Battleship | 4 | 4-6 |
| Carrier | 4 | 3-5 |

### Flood Damage Calculation

```
Total_Flood_Damage_Per_Second = Σ(Individual_Flood_Damage_Rates)
                               × Hull_Integrity_Modifier

Hull_Integrity_Modifier:
- 100-75% HP: ×1.0
- 75-50% HP: ×1.2 (damaged hull takes more water)
- 50-25% HP: ×1.5
- <25% HP: ×2.0

Example: Battleship with 2 floods at 60% HP
- Flood 1: Standard (0.5% HP/sec)
- Flood 2: Heavy (1.0% HP/sec)
- Hull Modifier: ×1.2
Total: (0.5 + 1.0) × 1.2 = 1.8% HP/sec = 108% HP per minute
```

### Counter-Flooding

Intentional flooding to correct list:

```
Counter_Flood_Command:
- Action: Flood compartments on opposite side
- Effect: Reduces list angle
- Cost: Additional HP damage (0.5% HP per 5° correction)
- Benefit: Prevents capsizing, restores gun functionality

List Effects on Gunnery:
- 0-5° list: No effect
- 5-10° list: -15% accuracy
- 10-15° list: -30% accuracy, some turrets cannot traverse
- 15-20° list: -50% accuracy, half turrets inoperable
- 20°+ list: Ship capsizing, abandon ship
```

### Pumping and Repair

```
Pump_Rate = Base_Pump_Capacity
           × Power_Available_Modifier
           × Crew_Modifier
           × Pump_Module_Bonus

Base_Pump_Capacity by Ship Class:
- Destroyer: 0.4% flood/sec removed
- Cruiser: 0.5% flood/sec removed
- Battleship: 0.6% flood/sec removed
- Carrier: 0.5% flood/sec removed

Power_Available_Modifier:
- Full power: ×1.0
- Partial power (50%): ×0.7
- Emergency power only: ×0.4
- No power: ×0.1 (manual pumps only)

Crew_Modifier (Flooding Control skill):
- Skill 7: ×0.75
- Skill 15: ×1.00
- Skill 50: ×2.05
```

### Flood Secondary Effects

| Effect | Trigger | Consequence |
|--------|---------|-------------|
| Magazine Flooding | Flood near magazine | Disables ammunition feed (+50% reload time) |
| Engine Room Flood | Flood in machinery | Progressive speed loss |
| Electrical Short | Flood + active systems | Random system failures |
| Loss of Stability | Multiple floods | Increased capsize risk |
| Reduced Freeboard | Heavy flooding | Waves can cause additional flooding |

---

## Critical System Failures

### Engine Damage

| Damage Level | Speed Effect | Repair Time | Permanent Damage |
|--------------|--------------|-------------|------------------|
| Light | -10% max speed | 30 sec | None |
| Moderate | -25% max speed | 60 sec | -5% max speed |
| Heavy | -50% max speed | 90 sec | -10% max speed |
| Critical | Dead in water | 120 sec | -20% max speed |
| Destroyed | Permanent DIW | Port repair only | Engine replacement |

### Steering Damage

| Damage Level | Effect | Repair Time |
|--------------|--------|-------------|
| Light | +20% turn radius | 15 sec |
| Moderate | +50% turn radius | 30 sec |
| Heavy | +100% turn radius | 45 sec |
| Jammed | Stuck in current turn | 60 sec |
| Destroyed | No steering | Port repair only |

### Turret Damage

| Damage Level | Effect | Repair Time |
|--------------|--------|-------------|
| Traverse Jam | Cannot rotate | 20 sec |
| Elevation Jam | Fixed elevation | 25 sec |
| Single Gun | Only 1 gun fires | 40 sec |
| Disabled | Turret inoperable | 60 sec |
| Destroyed | Permanent loss | Cannot repair at sea |

### Fire Control Damage

| Damage Level | Effect | Repair Time |
|--------------|--------|-------------|
| Degraded | -20% accuracy | 10 sec |
| Impaired | -40% accuracy, no lead indicator | 20 sec |
| Failed | Manual aiming only | 30 sec |
| Destroyed | -60% accuracy, no assistance | Port repair |

### Radar/Sonar Damage

| Damage Level | Effect | Repair Time |
|--------------|--------|-------------|
| Interference | -30% range | 10 sec |
| Degraded | -50% range, intermittent | 20 sec |
| Failed | No radar/sonar | 30 sec |
| Destroyed | Permanent loss | Port repair |

---

## Crew Casualties

### Casualty Rates

| Damage Type | Crew Casualty Rate |
|-------------|-------------------|
| HE Shell Hit | 2-5% of module crew |
| AP Penetration | 5-10% of module crew |
| Fire (per tick) | 0.5% of affected area crew |
| Flooding | 1% per severity level per tick |
| Magazine Explosion | 50-100% of magazine crew |
| Depth Charge | 3-8% of submarine crew |

### Casualty Effects

| Casualty % | Ship Effectiveness | Notes |
|------------|-------------------|-------|
| 0-10% | 100% | Combat ready |
| 10-25% | 85-90% | Light impact |
| 25-50% | 60-75% | Significant degradation |
| 50-75% | 40-50% | Critical manning |
| 75-90% | 20-30% | Skeleton crew |
| 90%+ | 0-10% | Ship nearly incapacitated |

### Crew Recovery

```
Crew_Recovery_Rate:
- In combat: 0% (no recovery)
- Out of combat, at sea: 0.5% crew per minute (medical treatment)
- At port: 5% crew per minute (medical + reinforcement)

Medical Bay Module Bonus:
- Basic: +50% recovery rate
- Advanced: +100% recovery rate
- Hospital Ship: +200% recovery rate
```

---

## Damage Control System

### Damage Control Party

Each ship has a limited number of damage control parties based on crew and modules.

| Ship Class | Base DC Parties | Max with Modules |
|------------|----------------|------------------|
| Destroyer | 1 | 2 |
| Light Cruiser | 2 | 3 |
| Heavy Cruiser | 2 | 4 |
| Battleship | 3 | 5 |
| Carrier | 3 | 5 |

### DC Party Actions

Each party can perform ONE action at a time:

| Action | Duration | Cooldown | Effect |
|--------|----------|----------|--------|
| Fight Fire | 5-40 sec | 10 sec | Extinguish one fire |
| Pump Flooding | Continuous | None | Reduce flood severity |
| Repair Turret | 45 sec | 30 sec | Restore 50% function |
| Repair Engine | 60 sec | 45 sec | Restore 50% speed |
| Repair Steering | 30 sec | 20 sec | Restore 70% function |
| Repair Electronics | 15 sec | 15 sec | Restore full function |

### DC Priority Decision Matrix

When multiple status effects are active, prioritization matters:

```
Threat_Priority_Score = Damage_Rate × Time_To_Critical × Consequence_Weight

Consequence_Weight:
- Fire near magazine: ×3.0 (detonation risk)
- Heavy flooding: ×2.5 (sinking risk)
- Engine damage (in combat): ×2.0 (can't escape)
- Standard fire: ×1.5
- Light flooding: ×1.0
- Turret damage: ×0.8
- Radar damage: ×0.5

Recommendation: Address highest priority score first
```

### Damage Control Consumables

Optional equipment that enhances DC:

| Consumable | Effect | Cooldown | Module Required |
|------------|--------|----------|-----------------|
| Emergency Repair | Instant 50% flood reduction | 180 sec | Damage Control Module |
| Fire Suppression | Extinguish all fires instantly | 240 sec | Fire Suppression System |
| Hull Patch Kit | +100% pump rate for 30 sec | 120 sec | Repair Kit |
| Bulkhead Seal | Prevent flood spreading | 300 sec | Advanced DC Module |

---

## Status Effect Interactions

### Compounding Effects

Some status effects interact negatively:

| Combination | Interaction |
|-------------|-------------|
| Fire + Flooding | Cannot fight fire in flooded compartment |
| Flooding + Engine Damage | Pumps less effective without power |
| Fire + Ammunition | Increased cook-off risk |
| Multiple Fires | Spread chance compounds |
| Heavy Flooding + List | Counter-flooding more dangerous |

### Positive Interactions

Some tactics can use effects strategically:

| Tactic | Effect |
|--------|--------|
| Magazine Flooding | Prevents magazine detonation, causes flood damage |
| Intentional List | Can help extinguish deck fires (water wash) |
| Scuttling Charges | Controlled flooding to sink ship (deny loot) |

---

## Balance Notes

### Fire vs Flooding Priority

**Fire:**
- Multiple fires more common
- Each fire individually less dangerous
- Easier to extinguish
- Spread creates emergency

**Flooding:**
- Single flood can be fatal
- Harder to control
- Causes secondary effects (speed, list)
- Requires continuous pumping

**Design Intent:** Fire is about sustained pressure and resource drain. Flooding is about immediate crisis management.

### Repair Time Balancing

All repair times assume baseline crew skill (15). Skilled crews significantly reduce times:

```
Actual_Repair_Time = Base_Repair_Time × (15 / Crew_Skill)

Example: 60-second engine repair with skill 30
Actual_Time = 60 × (15 / 30) = 30 seconds
```

### Extraction Tension

Status effects create extraction decisions:
- Badly damaged ship may not survive return journey
- Taking on additional damage compounds existing problems
- "One more engagement" can turn recoverable damage into fatal
- Must balance risk vs reward

---

## Implementation Notes

### For Programmers

1. **Tick Rate**: Process status effects every 1 second
2. **Damage Application**: Apply status effect damage before healing/repair
3. **State Machine**: Use state machines for fire/flood intensity levels
4. **Priority Queue**: Implement DC party actions as priority queue
5. **Visual Sync**: Ensure visual effects match mechanical state
6. **Save State**: All status effects must be serializable for persistence

### UI Requirements

**Status Panel Should Display:**
- Fire count and intensity icons
- Flood count and severity meters
- DC party status (available/working/cooldown)
- Estimated time to critical (if status effects severe)
- List angle indicator
- Speed penalty indicator

### Audio Cues

| Event | Audio Cue |
|-------|-----------|
| Fire started | Alarm + crew shout |
| Fire spreading | Intensifying crackling |
| Fire extinguished | Hiss + relief sound |
| Flooding detected | Klaxon + rushing water |
| Flooding critical | Loud groaning metal |
| Flood controlled | Pump sounds normalize |
| Magazine warning | Urgent repeated alarm |

---

## Cross-Reference Documents

**Related Combat Systems:**
- [[Damage-Model]] - HP damage and penetration
- [[Ballistics-Gunnery-Mechanics]] - Hit mechanics
- [[Surface-Combat]] - Tactical scenarios

**Related Module Documents:**
- [[Damage-Control-Module]] - DC party bonuses
- [[Fire-Suppression-System]] - Fire consumables
- [[Pumping-System]] - Flood control modules

**Related Systems:**
- [[Crew-Skills]] - Repair and firefighting skills
- [[Extraction-Mechanics]] - Status effects during extraction

---

## Summary Tables

### Fire Quick Reference

| Intensity | Damage/sec | Spread | Duration | Extinguish Time |
|-----------|------------|--------|----------|-----------------|
| Smoldering | 0.1% | 5% | 30s | 5s |
| Minor | 0.2% | 10% | 45s | 10s |
| Standard | 0.3% | 15% | 60s | 15s |
| Major | 0.5% | 25% | 90s | 25s |
| Inferno | 1.0% | 40% | Forever | 40s |

### Flood Quick Reference

| Severity | Damage/sec | Speed Penalty | List | Pump Rate Needed |
|----------|------------|---------------|------|------------------|
| Seepage | 0.1% | -2% | 0° | 0.1%/s |
| Light | 0.3% | -5% | 2° | 0.3%/s |
| Standard | 0.5% | -10% | 5° | 0.5%/s |
| Heavy | 1.0% | -20% | 10° | 1.0%/s |
| Catastrophic | 2.0% | -40% | 15°+ | 2.0%/s |

---

*This document provides the core framework for status effects. Specific values may be adjusted during balance testing.*
