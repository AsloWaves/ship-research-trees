---
tags: [planned, phase2, crew-management, specialization, skill-trees, navy-field-inspired]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-17
---

# Crew Specialization System

## Overview
The Crew Specialization System provides a three-tier classification tree (Basic → Advanced → Elite) that transforms neutral crew cards into specialized experts. Inspired by Navy Field's crew classification system, specializations are **permanent choices** that define crew roles and unlock performance bonuses. The system creates strategic depth through irreversible decisions, specialization trees that reward focused investment, and universal applicability across all ship classes.

## Implementation Status
**Status**: 📋 PLANNED (designed but not implemented)
**Phase**: Phase 2 - Core Gameplay Systems
**Scripts**: TBD (pending implementation)
**Priority**: HIGH (critical to crew depth and player choice)

---

## Design Specification

### Core Philosophy
Crew specialization is built on **permanent, meaningful choices**:
1. **No Respeccing**: Classifications are permanent once chosen
2. **Tiered Progression**: Basic → Advanced → Elite (three tiers)
3. **Universal Applicability**: Gunner works on ALL turrets, all ships
4. **Strategic Specialization**: Advanced/Elite require committing to specific paths
5. **Economic Investment**: Each tier costs credits to unlock

**Key Design Pillars:**
- **Permanent Choices**: No respeccing creates weight to decisions
- **Three-Tier Depth**: Basic (role), Advanced (specialization), Elite (mastery)
- **Ship-Agnostic**: Specializations work on any ship class
- **Stacking Bonuses**: Each tier adds to previous tier bonuses
- **Economic Gating**: Classification unlocks require credit investment

### Key Features
- **8 Basic Classifications**: Core crew roles (Gunner, Engineer, AA, Torpedoman, etc.)
- **Advanced Specializations**: Focused sub-paths within basic roles
- **Elite Masteries**: Ultimate specializations for endgame crews
- **Performance Bonuses**: Each tier adds stat bonuses to relevant modules
- **Universal Transfer**: Gunner works on destroyer AND battleship turrets identically
- **No Retraining**: Free crew transfer between ships without respeccing
- **Level Gates**: Specializations unlock at specific level thresholds

### User Experience
Players start with neutral Level 1 crew cards. At designated level thresholds, they choose classifications that permanently define crew roles. Basic classifications (Tier 1) define broad roles like "Gunner" or "Engineer". Advanced specializations (Tier 2) narrow focus within that role, such as "Heavy Gunner" for large-caliber weapons. Elite masteries (Tier 3) represent ultimate expertise like "Master Gunnery Officer". Each choice is permanent and shapes the crew's capabilities forever.

**Specialization Flow:**
1. Level neutral crew card to Tier 1 threshold (Level ~25-30)
2. Pay unlock cost, choose Basic Classification (Gunner, Engineer, etc.)
3. Continue leveling to Tier 2 threshold (Level ~75-80)
4. Pay unlock cost, choose Advanced Specialization (Heavy Gunner, Rapid Fire Gunner, etc.)
5. Continue leveling to Tier 3 threshold (Level ~125-130)
6. Pay unlock cost, choose Elite Mastery (Master Gunnery Officer, etc.)
7. Crew is now fully specialized, providing maximum bonuses

---

## Technical Implementation

### Current Implementation
**Not yet implemented** - This section is a design specification for Phase 2 development.

### Key Components

#### Classification Tier Structure

**Tier 1: Basic Classification (Unlocks at Level 25-30)**

The foundation specializations that define crew role:

1. **Gunner**
   - **Role**: Operates main battery and secondary battery turrets
   - **Applies To**: All gun turrets (main/secondary) on all ship classes
   - **Base Bonuses**: +5% accuracy, +3% reload speed
   - **Progression Paths**: Heavy Gunner, Fire Control Gunner, Rapid Fire Gunner

2. **AA Specialist**
   - **Role**: Operates anti-aircraft batteries
   - **Applies To**: All AA mounts on all ship classes
   - **Base Bonuses**: +8% AA accuracy, +5% AA range
   - **Progression Paths**: Flak Gunner, Proximity Fuse Expert, Tracking Specialist

3. **Torpedoman**
   - **Role**: Operates torpedo tubes
   - **Applies To**: All torpedo launchers on destroyers, cruisers, submarines
   - **Base Bonuses**: +5% torpedo speed, +3% torpedo range
   - **Progression Paths**: Long Lance Master, Spread Fire Expert, Stealth Torpedoman

4. **Engineer**
   - **Role**: Operates engines and propulsion systems
   - **Applies To**: All engine modules on all ship classes
   - **Base Bonuses**: +5% max speed, +8% acceleration
   - **Progression Paths**: Speed Engineer, Efficiency Engineer, Endurance Engineer

5. **Damage Control**
   - **Role**: Operates repair systems and fire suppression
   - **Applies To**: Damage control modules on all ship classes
   - **Base Bonuses**: +10% repair speed, +8% fire suppression
   - **Progression Paths**: Fire Master, Flooding Expert, Emergency Repair Specialist

6. **Electronics**
   - **Role**: Operates radar, sonar, and fire control systems
   - **Applies To**: Electronics modules on all ship classes
   - **Base Bonuses**: +10% radar range, +8% target acquisition speed
   - **Progression Paths**: Radar Expert, Sonar Master, Fire Control Director

7. **Aviation**
   - **Role**: Operates aircraft (carriers, seaplanes, catapult planes)
   - **Applies To**: Aircraft squadrons on carriers, seaplane catapults on battleships/cruisers
   - **Base Bonuses**: +8% aircraft speed, +5% aircraft survivability
   - **Progression Paths**: Fighter Ace, Dive Bomber Expert, Torpedo Bomber Specialist

8. **Command**
   - **Role**: Operates bridge systems, provides ship-wide buffs
   - **Applies To**: Command modules on all ship classes
   - **Base Bonuses**: +5% crew efficiency (ship-wide), +3% XP gain
   - **Progression Paths**: Tactical Commander, Fleet Commander, Morale Officer

**Tier 1 Unlock Cost:** TBD credits (example: 100,000 credits)

---

**Tier 2: Advanced Specialization (Unlocks at Level 75-80)**

Focused sub-paths within basic classifications. Examples within **Gunner** path:

1. **Fire Control Gunner**
   - **Focus**: Accuracy and targeting systems
   - **Bonuses**: +12% accuracy (stacks with Tier 1), +8% fire control range
   - **Penalty**: -2% reload speed
   - **Best For**: Long-range engagements, battleship main batteries
   - **Elite Path**: Master Gunnery Officer

2. **Heavy Gunner**
   - **Focus**: Large-caliber weapons (14"+ guns)
   - **Bonuses**: +15% damage on 14"+ guns, +5% penetration
   - **Penalty**: -3% reload speed on <14" guns
   - **Best For**: Battleship main batteries, heavy cruiser main guns
   - **Elite Path**: Siege Gunner

3. **Rapid Fire Gunner**
   - **Focus**: Reload speed and sustained fire
   - **Bonuses**: +18% reload speed (stacks with Tier 1), +5% sustained accuracy
   - **Penalty**: -5% damage per shot
   - **Best For**: Secondary batteries, light cruiser rapid-fire guns, destroyers
   - **Elite Path**: Suppression Master

**Example Advanced Paths for Engineer:**

1. **Speed Engineer**
   - **Focus**: Maximum speed and agility
   - **Bonuses**: +15% max speed (stacks with Tier 1), +10% turning rate
   - **Penalty**: -8% fuel efficiency
   - **Best For**: Destroyers, fast cruisers, hit-and-run tactics

2. **Efficiency Engineer**
   - **Focus**: Fuel economy and endurance
   - **Bonuses**: +25% fuel efficiency, +10% engine durability
   - **Penalty**: -5% max speed
   - **Best For**: Long-range operations, convoy escorts, extraction missions

3. **Endurance Engineer**
   - **Focus**: Engine durability and damage resistance
   - **Bonuses**: +30% engine HP, +15% resistance to engine criticals
   - **Penalty**: -3% max speed
   - **Best For**: Brawling ships, prolonged engagements

**Tier 2 Unlock Cost:** TBD credits (example: 500,000 credits)

---

**Tier 3: Elite Specialization (Unlocks at Level 125-130)**

Ultimate masteries representing peak expertise. Examples:

1. **Master Gunnery Officer** (from Fire Control Gunner path)
   - **Focus**: Ultimate accuracy and fire control
   - **Bonuses**: +20% accuracy (total: +37% with all tiers), +15% critical hit chance, +10% fire control range
   - **Penalty**: -5% reload speed
   - **Signature Ability**: "Precision Strike" - Once per battle, guaranteed critical hit
   - **Best For**: Endgame battleship main batteries, precision long-range combat

2. **Siege Gunner** (from Heavy Gunner path)
   - **Focus**: Maximum damage and penetration
   - **Bonuses**: +25% damage on 14"+ guns (total: +40%), +15% penetration, +10% AP shell effectiveness
   - **Penalty**: -8% reload speed
   - **Signature Ability**: "Devastating Salvo" - Once per battle, double damage on all shells in salvo
   - **Best For**: Citadel hits, armor penetration, devastating strikes

3. **Suppression Master** (from Rapid Fire Gunner path)
   - **Focus**: Sustained fire and suppression
   - **Bonuses**: +30% reload speed (total: +51%), +15% sustained accuracy, +10% fire chance
   - **Penalty**: -8% damage per shot
   - **Signature Ability**: "Barrage Mode" - Once per battle, 50% reload speed for 30 seconds
   - **Best For**: Continuous pressure, fire-starting, suppressing enemy repairs

**Elite Engineering Examples:**

1. **Legendary Engineer** (from Speed Engineer path)
   - **Focus**: Ultimate speed and maneuverability
   - **Bonuses**: +25% max speed (total: +45%), +20% acceleration, +15% turning rate
   - **Penalty**: -15% fuel efficiency
   - **Signature Ability**: "Emergency Power" - Once per battle, +50% speed for 20 seconds
   - **Best For**: Destroyer duels, torpedo runs, evasion tactics

2. **Fleet Engineer** (from Efficiency Engineer path)
   - **Focus**: Ultimate endurance and efficiency
   - **Bonuses**: +40% fuel efficiency, +20% engine durability, +15% extended range
   - **Penalty**: -8% max speed
   - **Signature Ability**: "Extended Operations" - Once per battle, engines immune to damage for 15 seconds
   - **Best For**: Long-range fleet operations, convoy missions, extraction gameplay

**Tier 3 Unlock Cost:** TBD credits (example: 2,000,000 credits)

---

#### Classification Rules & Mechanics

**Permanent Choice System:**
- ✅ Choose classification at designated level thresholds
- ❌ **No respeccing** - classification is permanent once chosen
- ❌ Cannot change Basic classification after selection
- ❌ Cannot change Advanced specialization after selection
- ❌ Cannot change Elite specialization after selection
- ⚠️ **Think carefully** - decisions are irreversible

**Stacking Bonus Mechanics:**
```
Bonuses stack additively across tiers:

Example: Fire Control Gunner → Master Gunnery Officer
- Tier 1 (Gunner): +5% accuracy
- Tier 2 (Fire Control Gunner): +12% accuracy
- Tier 3 (Master Gunnery Officer): +20% accuracy
- Total Accuracy Bonus: +37%

Penalties also stack:
- Tier 2: -2% reload speed
- Tier 3: -5% reload speed
- Total Reload Penalty: -7%

Net Result: +37% accuracy, -7% reload speed
```

**Universal Applicability:**
- ✅ Gunner classification works on **all turrets** regardless of ship class
- ✅ Engineer classification works on **all engines** regardless of ship class
- ✅ Heavy Gunner (14"+ bonus) applies to ANY ship with 14"+ guns
- ✅ Rapid Fire Gunner applies to ANY fast-firing turrets
- ✅ **No retraining needed when changing ships**

**Example Universal Application:**
```
Level 150 Heavy Gunner crew card:
- On T7 Battleship: Applies to 16" main battery (+40% damage)
- Transfer to T5 Heavy Cruiser: Applies to 8" main battery (no bonus, <14")
- Transfer to T9 Battleship: Applies to 18" main battery (+40% damage)
- **Zero retraining cost, instant transfer, full functionality**

Same crew card, different ships, no penalties
```

#### Level Thresholds & Unlock Costs

**Tier 1: Basic Classification**
- **Unlock Level**: 25-30 (TBD, testing needed)
- **Unlock Cost**: 100,000 credits (example)
- **Time to Reach**: 8-12 hours combat or 50M credits training
- **Strategic Window**: Early-game decision, defines crew role

**Tier 2: Advanced Specialization**
- **Unlock Level**: 75-80 (TBD, testing needed)
- **Unlock Cost**: 500,000 credits (example)
- **Time to Reach**: 50-70 hours combat from L1 or 300M credits training
- **Strategic Window**: Mid-game decision, narrows focus

**Tier 3: Elite Specialization**
- **Unlock Level**: 125-130 (TBD, testing needed)
- **Unlock Cost**: 2,000,000 credits (example)
- **Time to Reach**: 200-250 hours combat from L1 or 1.5B credits training
- **Strategic Window**: Endgame decision, ultimate mastery

**Total Investment (L1 → L130 Elite):**
- **Time**: 200-250 hours combat grinding
- **Credits**: 2.6M unlock costs + 800M training costs (if hybrid approach)
- **Total Value**: ~3B+ credits equivalent

### Configuration

**Tunable Parameters:**
```
// Level Thresholds (TBD - need playtesting)
TIER_1_UNLOCK_LEVEL = 30
TIER_2_UNLOCK_LEVEL = 80
TIER_3_UNLOCK_LEVEL = 130

// Unlock Costs (TBD - need economy balancing)
TIER_1_UNLOCK_COST = 100000 credits
TIER_2_UNLOCK_COST = 500000 credits
TIER_3_UNLOCK_COST = 2000000 credits

// Respec Policy
ALLOW_RESPEC = false (permanent choice design)
RESPEC_COST = null (not applicable)

// Universal Applicability
SPECIALIZATION_SHIP_LOCKED = false (works on all ships)
SPECIALIZATION_WEAPON_LOCKED = false (works on all weapons of type)
```

**Example Specialization Definitions:**
```json
{
  "basic_classifications": [
    {
      "id": "gunner",
      "name": "Gunner",
      "unlock_level": 30,
      "unlock_cost": 100000,
      "applies_to": ["main_battery", "secondary_battery"],
      "bonuses": {
        "accuracy": 0.05,
        "reload_speed": 0.03
      },
      "advanced_paths": ["fire_control_gunner", "heavy_gunner", "rapid_fire_gunner"]
    },
    {
      "id": "engineer",
      "name": "Engineer",
      "unlock_level": 30,
      "unlock_cost": 100000,
      "applies_to": ["engine", "propulsion"],
      "bonuses": {
        "max_speed": 0.05,
        "acceleration": 0.08
      },
      "advanced_paths": ["speed_engineer", "efficiency_engineer", "endurance_engineer"]
    }
  ],
  "advanced_specializations": [
    {
      "id": "fire_control_gunner",
      "name": "Fire Control Gunner",
      "requires": "gunner",
      "unlock_level": 80,
      "unlock_cost": 500000,
      "bonuses": {
        "accuracy": 0.12,
        "fire_control_range": 0.08
      },
      "penalties": {
        "reload_speed": -0.02
      },
      "elite_paths": ["master_gunnery_officer"]
    }
  ],
  "elite_specializations": [
    {
      "id": "master_gunnery_officer",
      "name": "Master Gunnery Officer",
      "requires": "fire_control_gunner",
      "unlock_level": 130,
      "unlock_cost": 2000000,
      "bonuses": {
        "accuracy": 0.20,
        "critical_chance": 0.15,
        "fire_control_range": 0.10
      },
      "penalties": {
        "reload_speed": -0.05
      },
      "signature_ability": {
        "name": "Precision Strike",
        "description": "Once per battle, guaranteed critical hit",
        "cooldown": null,
        "uses_per_battle": 1
      }
    }
  ]
}
```

---

## Integration Points

### Depends On
- [[Crew-Management]] - Base crew card system
- [[Crew-Progression]] - Level thresholds for unlocks
- [[Economy-System]] - Unlock costs and credit sinks
- [[Combat-System]] - Bonus application to modules

### Used By
- [[Ship-Modules]] - Specialization bonuses affect module stats
- [[Player-Progression]] - Specialization choices shape playstyle
- [[Crew-Permadeath]] - Elite crews represent massive specialization investment at risk

---

## Strategic Gameplay Impact

### Specialization Decision Trees

**Example Decision: Gunner Path Choice at Level 80**

Player has Level 80 Gunner on T7 Battleship with 16" guns. Which Advanced path?

**Option A: Fire Control Gunner**
- **Pros**: +12% accuracy (huge for long-range)
- **Cons**: -2% reload speed
- **Best For**: Precision long-range combat, sniping
- **Elite Path**: Master Gunnery Officer (ultimate accuracy)
- **Playstyle**: Patient, methodical, accuracy-focused

**Option B: Heavy Gunner**
- **Pros**: +15% damage on 16" guns, +5% penetration
- **Cons**: -3% reload on smaller guns (not relevant for 16" battleship)
- **Best For**: Devastating alpha strikes, citadel hits
- **Elite Path**: Siege Gunner (maximum damage)
- **Playstyle**: Aggressive, brawling, high-damage

**Option C: Rapid Fire Gunner**
- **Pros**: +18% reload speed
- **Cons**: -5% damage per shot (bad for 16" guns)
- **Best For**: Secondary batteries, NOT main 16" guns
- **Elite Path**: Suppression Master (sustained fire)
- **Playstyle**: Continuous pressure, fire-starting
- **Verdict**: **Poor choice for 16" battleship main battery**

**Player Choice:** Heavy Gunner (matches playstyle and ship class)
- Commits to damage-focused path
- **Permanent decision** - cannot change to Fire Control later
- Must live with -3% reload penalty
- Gains +15% damage and +5% penetration immediately

### Multi-Crew Composition Strategies

**T10 Battleship Crew Roster Example:**
```
15 crew positions, optimized composition:

Main Battery Turret #1: Level 180 Master Gunnery Officer (Fire Control path)
- Role: Precision long-range sniping
- Bonuses: +37% accuracy, +15% crit chance
- Weight: 186 tons

Main Battery Turret #2: Level 170 Siege Gunner (Heavy path)
- Role: Maximum damage alpha strikes
- Bonuses: +40% damage on 16" guns, +15% penetration
- Weight: 175 tons

Main Battery Turret #3: Level 160 Heavy Gunner (Heavy path, not Elite yet)
- Role: Damage support
- Bonuses: +20% damage on 16" guns
- Weight: 168 tons

Secondary Battery #1: Level 150 Suppression Master (Rapid Fire path)
- Role: Sustained fire, destroyer defense
- Bonuses: +51% reload speed, +15% sustained accuracy
- Weight: 156 tons

Secondary Battery #2: Level 140 Rapid Fire Gunner (Rapid Fire path, not Elite yet)
- Role: Secondary fire support
- Bonuses: +21% reload speed
- Weight: 149 tons

AA Battery #1: Level 150 Tracking Specialist (AA Elite path)
- Role: Aircraft interception
- Bonuses: +35% AA accuracy, +20% tracking speed
- Weight: 156 tons

AA Battery #2: Level 130 Flak Gunner (AA Advanced path)
- Role: AA support
- Bonuses: +18% AA accuracy
- Weight: 138 tons

Engine Room: Level 180 Legendary Engineer (Speed path)
- Role: Maximum speed and maneuverability
- Bonuses: +45% max speed, +20% acceleration
- Weight: 186 tons

Damage Control: Level 160 Fire Master (Damage Control Elite path)
- Role: Fire suppression, emergency repair
- Bonuses: +40% fire suppression, +25% repair speed
- Weight: 168 tons

Radar Station: Level 150 Radar Expert (Electronics Elite path)
- Role: Target acquisition, radar range
- Bonuses: +35% radar range, +20% acquisition speed
- Weight: 156 tons

[5 more positions filled with Level 100-140 support crews]

Total Crew Weight: ~1,800 tons (within T10 limit of 2,500)
Total Investment: ~2,500 hours + 15B credits equivalent
```

**Strategic Composition Notes:**
- **Mixed Gunner Paths**: Fire Control for accuracy, Heavy for damage
- **Specialized Roles**: Each crew optimized for specific position
- **Weight Management**: Elite crews fit within T10 weight limits
- **Backup Strategy**: Lower-level support crews reduce risk (easier to replace)
- **Permadeath Risk**: If ship dies at T10, entire 15B investment lost (100% death)

### Classification Synergies

**Destroyer Build: "Torpedo Ninja"**
```
5 crew positions optimized for stealth torpedo runs:

Torpedo Tubes: Level 180 Stealth Torpedoman (Elite)
- Bonuses: +50% torpedo detection reduction, +25% torpedo speed
- Signature Ability: "Silent Launch" - Undetectable torpedo launch once per battle

Engine: Level 170 Legendary Engineer (Speed path)
- Bonuses: +45% max speed, +20% acceleration
- Signature Ability: "Emergency Power" - +50% speed burst

Electronics: Level 150 Sonar Master (Electronics Elite)
- Bonuses: +35% sonar range, +20% submarine detection
- Perfect for hunting subs and avoiding detection

Damage Control: Level 130 Flooding Expert
- Bonuses: +30% flooding repair, +15% torpedo damage resistance
- Survives enemy torpedo hits better

Command: Level 120 Tactical Commander
- Bonuses: +15% crew efficiency, +8% concealment
- Ship-wide stealth boost

Synergy: Maximum stealth, speed, and torpedo lethality
Playstyle: Hit-and-run, torpedo ambushes, evasion
Weakness: Low durability, relies on not being hit
```

**Carrier Build: "Air Superiority"**
```
20 crew positions optimized for aircraft dominance:

Fighter Squadron #1: Level 200 Fighter Ace (Aviation Elite)
- Bonuses: +60% fighter combat effectiveness, +30% aircraft speed
- Signature Ability: "Ace Maneuver" - Invincible fighters for 10 seconds

Dive Bomber Squadron #1: Level 190 Dive Bomber Expert (Aviation Elite)
- Bonuses: +50% dive bomber accuracy, +25% bomb penetration
- Signature Ability: "Precision Dive" - Guaranteed citadel hit

Torpedo Bomber Squadron #1: Level 180 Torpedo Bomber Specialist (Aviation Elite)
- Bonuses: +45% torpedo bomber survivability, +20% torpedo damage
- Signature Ability: "Coordinated Strike" - All torpedoes hit simultaneously

[Additional squadrons with Level 140-170 Aviation specialists]

AA Defense: Multiple Level 150 AA Tracking Specialists
- Protect carrier from enemy aircraft

Electronics: Level 160 Radar Expert
- Detect enemy ships for aircraft strikes

Synergy: Overwhelming air power, multi-role strike capability
Playstyle: Dominate through aircraft, stay at range
Investment: ~5,000 hours + 30B credits for full elite air wing
```

---

## Example Scenarios

### Scenario 1: First Classification Choice
**Captain Singh reaches Level 30 with Gunner candidate**

**Situation:**
- Neutral Level 30 crew card
- 100,000 credits available
- Operating T3 Light Cruiser with 6" rapid-fire guns
- Planning to progress to T5 Heavy Cruiser (8" guns) then T7 Battleship (14" guns)

**Options:**
1. Choose Gunner (generic, works everywhere)
2. Wait to see future ship progression (risky, crew sits at L30)

**Decision:** Choose Gunner now
- Pays 100,000 credits
- Unlocks Gunner classification
- Gains +5% accuracy, +3% reload speed immediately
- **Locks in basic path, cannot change**

**Future Planning:**
- At Level 80: Will choose between Fire Control, Heavy, or Rapid Fire
- Current T3 ship has rapid-fire 6" guns (Rapid Fire would be good)
- Future T7 battleship has 14" heavy guns (Heavy Gunner would be good)
- **Dilemma: Optimize for current ship or future ship?**

**Long-Term Thinking:**
- Decides to optimize for future T7 battleship
- Will choose Heavy Gunner at Level 80 (even though suboptimal for T3)
- Accepts -5% damage on current T3 rapid-fire guns
- **Plans for endgame, sacrifices short-term efficiency**

### Scenario 2: Advanced Specialization Commitment
**Captain Zhang reaches Level 80, must choose Advanced path**

**Setup:**
- Level 80 Gunner crew card
- Operating T7 Battleship with 16" main battery
- 500,000 credits available for unlock
- Considering endgame T10 operations

**Analysis:**

**Fire Control Gunner Path:**
- **Immediate Bonuses**: +12% accuracy, +8% fire control range
- **Immediate Penalties**: -2% reload speed
- **Elite Path**: Master Gunnery Officer (ultimate accuracy build)
- **Best For**: Long-range precision, sniping playstyle
- **Zhang's Playstyle**: Prefers brawling and close-range combat
- **Verdict**: Doesn't match playstyle ❌

**Heavy Gunner Path:**
- **Immediate Bonuses**: +15% damage on 16" guns, +5% penetration
- **Immediate Penalties**: -3% reload on <14" guns (irrelevant for 16" BB)
- **Elite Path**: Siege Gunner (maximum damage build)
- **Best For**: Alpha strikes, citadel hits, brawling
- **Zhang's Playstyle**: Aggressive close-range combat
- **Verdict**: Perfect match ✅

**Rapid Fire Gunner Path:**
- **Immediate Bonuses**: +18% reload speed
- **Immediate Penalties**: -5% damage per shot
- **Elite Path**: Suppression Master (sustained fire build)
- **Best For**: Secondary batteries, light cruisers, DDs
- **Zhang's Playstyle**: Not suited for 16" main battery
- **Verdict**: Wrong specialization for this crew ❌

**Decision:** Heavy Gunner
- Pays 500,000 credits
- Gains +15% damage and +5% penetration on 16" guns
- **Permanently commits to damage-focused path**
- Cannot pivot to Fire Control accuracy build later
- **Accepts consequences of permanent choice**

**6 Months Later (Level 130):**
- Zhang reaches Elite unlock threshold
- Only option: Siege Gunner (Heavy path continuation)
- Pays 2,000,000 credits
- Gains +25% damage (total +40%), +15% penetration, +10% AP effectiveness
- Signature Ability: "Devastating Salvo" (double damage once per battle)
- **Total investment: 3M credits + 300 hours = ultimate damage build**

### Scenario 3: Multi-Crew Diversification
**Captain Schmidt builds versatile crew library**

**Strategy: Don't put all eggs in one basket**

**Year 1: Core Crew Development**
- Levels 4 Gunner crews to Level 80
- **Diversifies specializations:**
  - Crew A: Fire Control Gunner (accuracy build)
  - Crew B: Heavy Gunner (damage build)
  - Crew C: Rapid Fire Gunner (reload build)
  - Crew D: Fire Control Gunner (backup accuracy)

**Reasoning:**
- **Flexibility**: Can optimize for different ships
- **Risk Management**: If one crew dies (permadeath), others survive
- **Ship-Specific Optimization**: Use Heavy Gunner on BB, Rapid Fire on CL

**Year 2: Elite Specializations**
- Pushes Crews A & B to Level 130 Elite
  - Crew A: Master Gunnery Officer (ultimate accuracy)
  - Crew B: Siege Gunner (ultimate damage)
- Keeps Crews C & D at Level 100-120 (backup tier)

**Year 3: Operational Deployment**

**T10 Battleship (High-Risk Operations):**
- Main Battery #1: Crew A (Master Gunnery Officer)
- Main Battery #2: Crew B (Siege Gunner)
- **Risk**: Both elite crews at T10 (100% death if ship destroyed)
- **Mitigation**: Has Crews C & D as backups

**T8 Cruiser (Farming Operations):**
- Main Battery: Crew C (Rapid Fire Gunner, Level 120)
- **Risk**: 40% crew card permadeath chance (moderate risk)
- **Efficiency**: Good reload speed for rapid-fire cruiser guns

**T5 Destroyer (Training New Crews):**
- Uses Level 1-50 trainee crews
- **Risk**: Zero crew card permadeath (T5 is completely safe tier)
- **Note**: T1-T5 all have 0% crew card permadeath - perfect for training

**Outcome:**
- **Versatile crew library**: Can field optimal crews for any ship
- **Risk management**: Backups available if elites die
- **Specialization coverage**: Accuracy, damage, and reload builds all represented
- **Investment**: ~1,000 hours + 8B credits across 4 Gunner crews

### Scenario 4: Specialization Mistake
**Captain Johnson regrets permanent choice**

**The Setup:**
- Level 80 Engineer crew card
- Chose **Efficiency Engineer** (fuel economy focus)
- Reasoning: "I do lots of long-range missions, fuel efficiency is important"
- Paid 500,000 credits unlock cost

**6 Months Later:**
- Johnson's playstyle evolved
- Now prefers fast destroyer combat and hit-and-run tactics
- **Efficiency Engineer is WRONG specialization** for destroyers
- Should have chosen **Speed Engineer** for +15% max speed

**The Problem:**
- **Cannot respec** - choice is permanent
- Efficiency Engineer gives: +25% fuel efficiency, +10% engine durability
- But Johnson needs: +15% max speed, +10% turning rate (Speed Engineer)
- **Stuck with suboptimal specialization forever**

**Options:**
1. **Accept the mistake**, use Efficiency Engineer on destroyers (suboptimal)
   - Pro: Uses existing Level 150 crew (time investment preserved)
   - Con: Slower destroyer, disadvantaged in speed-based combat

2. **Level new Engineer crew** from scratch with Speed path
   - Pro: Gets optimal Speed Engineer specialization
   - Con: 200+ hours to reach Level 130 again + 3M credits
   - Con: Original Level 150 Efficiency Engineer wasted (600 hours + 2B credits)

3. **Repurpose Efficiency Engineer** for different ship type
   - Use on long-range battleship or cruiser (where fuel efficiency matters)
   - Level new Speed Engineer for destroyers
   - Pro: Both crews have roles
   - Con: Still requires leveling new crew (200+ hours)

**Johnson's Decision:** Option 3 (repurpose)
- Keeps Efficiency Engineer for T8 Battleship (fuel efficiency useful for long ops)
- Starts new Engineer crew, will choose Speed path at Level 80
- **Lesson learned: Plan specializations around long-term playstyle**
- **Cost of mistake: 200 hours + 2B credits for redundant crew**

**Design Success:**
- Permanent choice created real consequences
- Player must think carefully about specializations
- Mistakes are costly but not game-breaking (can level new crew)
- **Meaningful decision with stakes = good design**

### Scenario 5: Min-Max Elite Composition
**Captain Yamamoto builds ultimate T10 battleship**

**Goal:** Maximum performance through perfect crew composition

**15 Crew Positions, Fully Optimized:**

**Main Batteries (3 positions):**
1. Level 200 Master Gunnery Officer (Fire Control → Elite)
   - Total Bonuses: +37% accuracy, +15% crit chance, +10% FC range
   - Penalties: -7% reload speed
   - Role: Primary accuracy-focused main battery
   - Investment: 500 hours + 3B credits

2. Level 200 Siege Gunner (Heavy → Elite)
   - Total Bonuses: +40% damage on 18" guns, +15% penetration, +10% AP effectiveness
   - Penalties: -11% reload speed
   - Role: Maximum alpha damage main battery
   - Investment: 500 hours + 3B credits

3. Level 190 Heavy Gunner (Heavy → Advanced, not Elite)
   - Total Bonuses: +20% damage on 18" guns, +5% penetration
   - Penalties: -3% reload speed
   - Role: Backup damage battery
   - Investment: 350 hours + 2B credits

**Secondary Batteries (2 positions):**
4. Level 180 Suppression Master (Rapid Fire → Elite)
   - Total Bonuses: +51% reload speed, +15% sustained accuracy, +10% fire chance
   - Penalties: -13% damage per shot
   - Role: Destroyer defense, fire-starting
   - Investment: 400 hours + 2.5B credits

5. Level 150 Rapid Fire Gunner (Rapid Fire → Advanced)
   - Total Bonuses: +21% reload speed
   - Penalties: -5% damage per shot
   - Role: Secondary fire support
   - Investment: 250 hours + 1.5B credits

**AA Batteries (3 positions):**
6. Level 180 Tracking Specialist (AA → Elite)
   - Total Bonuses: +35% AA accuracy, +20% tracking speed, +15% flak burst damage
   - Role: Primary air defense
   - Investment: 400 hours + 2.5B credits

7-8. Level 140 Flak Gunners (AA → Advanced) ×2
   - Total Bonuses: +18% AA accuracy each
   - Role: AA support coverage
   - Investment: 200 hours + 1B credits each

**Engineering (2 positions):**
9. Level 200 Legendary Engineer (Speed → Elite)
   - Total Bonuses: +45% max speed, +20% acceleration, +15% turning
   - Penalties: -23% fuel efficiency
   - Signature: "Emergency Power" (+50% speed burst)
   - Role: Maximum agility and speed
   - Investment: 500 hours + 3B credits

10. Level 160 Endurance Engineer (Endurance → Advanced)
    - Total Bonuses: +30% engine HP, +15% resistance to criticals
    - Penalties: -3% max speed
    - Role: Engine durability and backup
    - Investment: 280 hours + 1.8B credits

**Support Systems (5 positions):**
11. Level 170 Fire Master (Damage Control → Elite)
    - Total Bonuses: +40% fire suppression, +25% repair speed
    - Role: Emergency damage control
    - Investment: 350 hours + 2.2B credits

12. Level 160 Radar Expert (Electronics → Elite)
    - Total Bonuses: +35% radar range, +20% acquisition speed
    - Role: Target detection and fire control
    - Investment: 300 hours + 2B credits

13. Level 150 Tactical Commander (Command → Elite)
    - Total Bonuses: +20% crew efficiency (ship-wide), +10% XP gain
    - Role: Ship-wide buff and morale
    - Investment: 250 hours + 1.5B credits

14-15. Level 120 Basic Support ×2 (various Tier 1 classifications)
    - Role: Fill remaining positions, lower investment
    - Investment: 150 hours + 800M credits each

**Total Composition Investment:**
- **Time**: ~5,000 hours of active gameplay
- **Credits**: ~30B credits equivalent
- **Weight**: ~2,200 tons (within T10 2,500-ton limit)
- **Real-World Value**: ~$15,000+ if time valued at $3/hour

**Performance Result:**
- **Main Battery**: +37% accuracy OR +40% damage (depending on turret choice)
- **Secondary Battery**: +51% reload speed (destroyer shredder)
- **AA Defense**: +35% tracking (aircraft killer)
- **Speed**: +45% max speed (battleship with cruiser mobility)
- **Durability**: +40% fire suppression, +30% engine HP
- **Overall**: Ultimate endgame battleship, peak performance

**The Risk:**
- **T10 destruction = 100% crew death, all 15 crews lost instantly**
- **Total loss: 5,000 hours + 30B credits gone forever**
- **No retrieval possible in T10**
- **This is why T10 is the ultimate stakes**

**Yamamoto's Strategy:**
- **Never uses this composition at T10** (too risky)
- Reserves this crew set for T9 operations (60% crew card permadeath risk, retrieval possible)
- For T10, uses separate "expendable" Level 100-130 crew set
- Elite composition is for T9 dominance, not T10 suicide
- Even 60% risk at T9 is acceptable for this much power

**Design Validation:**
- Ultimate min-max build requires ~5,000 hours investment
- Creating real fear of T10 permadeath = successful stakes design
- Players self-regulate T10 risk = healthy game behavior

---

## Known Issues
- **None (design phase)** - Not yet implemented

## Future Enhancements
- **Specialization Reset Tokens**: Ultra-rare consumable that allows one-time respec (expensive, limited)
- **Dual Specialization**: High-level crews can train secondary spec at reduced effectiveness
- **Specialization Synergies**: Ship-wide bonuses when certain specs are combined
- **Historical Specializations**: Nation-specific elite paths (e.g., "Long Lance Master" for Japanese torpedoes)
- **Signature Abilities UI**: Visual indicators and cooldown tracking
- **Specialization Achievements**: Medals for reaching Elite tier, special titles
- **Training Simulators**: Port facilities that reduce specialization unlock costs

---

## Cross-References
- [[Crew-Management]] - Base crew card system and structure
- [[Crew-Progression]] - Level thresholds for specialization unlocks
- [[Crew-Permadeath]] - Elite specializations represent massive investment at risk
- [[Ship-Modules]] - Specialization bonuses apply to modules
- [[Combat-System]] - Bonus calculations and signature abilities
- [[Economy-System]] - Specialization unlock costs and credit sinks

---

## Testing

### Test Coverage
- [ ] Specialization unlock flow (Tier 1 → Tier 2 → Tier 3)
- [ ] Bonus stacking calculations (additive across tiers)
- [ ] Penalty stacking calculations (additive across tiers)
- [ ] Universal applicability (same crew on different ships)
- [ ] Permanent choice enforcement (no respeccing)
- [ ] Credit cost deduction for unlocks
- [ ] Signature ability mechanics and cooldowns
- [ ] Edge cases (unlocking at exact level threshold, etc.)

### Test Results
Not yet implemented - testing pending Phase 2 development.

---

## Changelog
- **2025-11-17**: Initial design document created from GDD_Updated-1.md (lines 162-516)
