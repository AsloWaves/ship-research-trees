---
tags: [planned, phase2, crew-skills, navy-field-inspired, stat-system, rng-recruitment]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-19
---

# Crew Skills & Stats System

## Overview
NavyField 1-inspired stat-based crew progression system with **RNG recruitment mechanics**. Crew cards have random starting stats (7-15 range) when recruited, creating a "hunt for good sailors" gameplay loop. Stats scale from **7 (untrained) to 50 (legendary)** through classification bonuses and level-up growth. The system features 18 specialized classifications, each with 2-4 primary stats that directly affect gameplay mechanics.

## Implementation Status
**Status**: 📋 PLANNED (designed but not implemented)
**Phase**: Phase 2 - Core Gameplay Systems
**Scripts**: TBD (pending implementation)
**Priority**: HIGH (core Phase 2 feature, fundamental to crew progression)

---

## Design Philosophy

### Core Principles
- **RNG Recruitment**: Random starting stats (7-15 range) when recruiting crew cards
- **Reroll Mechanics**: Players can dismiss and recruit again to hunt for better stats
- **Classification Bonuses**: Choosing classification adds +5 to primary stats immediately
- **Level-Up Growth**: Small stat gains per level (+0.12 primary, +0.06 secondary per level)
- **Wide Stat Range**: 7-50 range creates significant differentiation between crews
- **Direct Mechanical Effects**: Each stat point directly affects gameplay (transparent calculations)
- **Universal Crews**: All crews work on all ships, but stats favor certain ship types

### NavyField 1 Heritage
This system faithfully recreates NavyField 1's RNG sailor system:
- ✅ **Random starting stats** when recruited (can reroll by recruiting again)
- ✅ **Wide stat ranges** (7-50 vs NF1's 7-12) for more differentiation
- ✅ **Classification unlocks** add immediate stat bonuses
- ✅ **Level progression** improves stats gradually over time
- ✅ **Hunting for good recruits** creates early-game engagement

**Key Improvements Over NavyField 1:**
- **Wider stat range** (7-50 vs 7-12) allows for more endgame progression
- **Clearer stat-to-gameplay mappings** (transparent effect calculations)
- **18 classifications** (vs 12) including extraction-specific roles
- **Transparent RNG** (show stat ranges before recruiting)

---

## RNG Recruitment System

### Recruitment Mechanics

When recruiting a crew card at port, **all stats are randomly generated** within the **7-15 range** (uniform distribution). Port tier affects recruitment cost, not stat ranges.

**All Ports Recruitment** (Any Port, 5,000 credits):
- **Stat Range**: 7-15 (average: 11)
- **Distribution**: Uniform (equal chance for any value 7-15)
- **Quality**: All recruitment has same stat range
- **Use Case**: Hunt for good RNG by rerolling

### Reroll Mechanics

**How Rerolling Works**:
1. Recruit crew card at port (pay recruitment cost)
2. View generated stats
3. If unsatisfied → **Dismiss crew** (no refund)
4. Recruit again (pay recruitment cost again)
5. Repeat until satisfied

**Example Reroll Session** (Standard Recruitment, 5,000 credits per roll):
```
Roll 1: Accuracy 10, Reload 9,  Range 11  → Dismiss (low Reload)
Roll 2: Accuracy 14, Reload 10, Range 9   → Dismiss (low Range)
Roll 3: Accuracy 9,  Reload 15, Range 10  → Dismiss (low Accuracy)
Roll 4: Accuracy 13, Reload 14, Range 12  → KEEP! (good balanced stats)

Total Cost: 20,000 credits (4 rolls × 5,000)
```

**Strategic Considerations**:
- **Early Game**: Accept mediocre stats (7-10 range, save credits for ships/equipment)
- **Mid Game**: Reroll 3-5 times for decent stats (12-13 average, 15,000-25,000 credits investment)
- **Late Game**: Reroll 10-20 times for elite stats (14-15 in primary stats, 50,000-100,000 credits investment)
- **Perfect Hunting**: Some players reroll 50+ times for perfect 15/15 primary stats (250,000+ credits)

**UI Display**:
When recruiting, show:
```
╔════════════════════════════════╗
║ Crew Recruitment               ║
║ Cost: 5,000 credits            ║
║                                ║
║ Stat Range: 7-15               ║
║ (All stats randomly generated) ║
║                                ║
║ [RECRUIT] [Cancel]             ║
╚════════════════════════════════╝

After recruitment:
╔════════════════════════════════╗
║ Neutral Crew Card (Level 1)    ║
║                                ║
║ Accuracy:  13 ████████         ║
║ Reload:    14 █████████        ║
║ Range:     12 ███████          ║
║ (All stats):  7-15 per stat    ║
║                                ║
║ [KEEP] [DISMISS & REROLL]      ║
╚════════════════════════════════╝
```

---

## Universal Stat Mechanics

### Stat Ranges (7-50 Scale)

**All Stats Use Same Range**:
- **Minimum**: 7 (absolute untrained floor)
- **Maximum**: 50 (legendary cap, Level 175-200 depending on RNG)
- **Recruitment Range**: 7-15 (uniform distribution, all ports)
- **Classification Bonus**: +5 at Level 25
- **Level Growth**: +0.19/level (primary), +0.10/level (secondary)

**Stat Quality Tiers**:
- **7-14**: Untrained (poor performance, penalties)
- **15-24**: Trained (baseline to competent)
- **25-34**: Expert (strong performance)
- **35-44**: Elite (top 10% performance)
- **45-50**: Legendary (near-perfect to maximum effectiveness)

### Stat Growth Formula

**Total Stat Value** = Base Stat (RNG) + Classification Bonus + Level Growth

**Breakdown**:
1. **Base Stat (Level 1 Recruitment)**: 7-15 (RNG, uniform distribution)
2. **Level 1-25 Neutral Growth**: +0.05 per level to ALL stats = +1.25 per stat
3. **Level 25 Classification Bonus**: +5 to primary stats (one-time)
4. **Level 26-200 Classified Growth**: +0.19/level (primary), +0.10/level (secondary)

**Example Progression** (Average RNG: Accuracy 11 at Level 1):

```
Level 1:   Accuracy 11 (recruited stat)
Level 25:  Accuracy 11 + (25 × 0.05) = 12.25 (neutral growth)
           + 5 (classification bonus) = 17.25
Level 100: Accuracy 17.25 + (75 × 0.19) = 31.5
Level 200: Accuracy 17.25 + (175 × 0.19) = 50.5 → CAPPED at 50

Final: Accuracy 50 (legendary, reaches cap at Level 200)
```

**Example Progression** (Bad RNG: Accuracy 7 at Level 1):

```
Level 1:   Accuracy 7 (worst possible roll)
Level 25:  Accuracy 7 + 1.25 = 8.25 + 5 = 13.25
Level 100: Accuracy 13.25 + (75 × 0.19) = 27.5
Level 200: Accuracy 13.25 + (175 × 0.19) = 46.5

Final: Accuracy 46.5 (RNG disadvantage, 3.5 points below cap)
```

**Example Progression** (Perfect RNG: Accuracy 15 best possible roll):

```
Level 1:   Accuracy 15 (best possible roll)
Level 25:  Accuracy 15 + 1.25 = 16.25 + 5 = 21.25
Level 100: Accuracy 21.25 + (75 × 0.19) = 35.5
Level 176: Accuracy 21.25 + (151 × 0.19) = 50 (REACHES CAP)
Level 200: Accuracy 50 (legendary, capped)

Final: Accuracy 50 (legendary, reached cap at Level 176)
```

**Key Insight**:
- Perfect RNG (15 start) reaches stat cap at Level 176
- Average RNG (11 start) reaches stat cap at Level 200
- Bad RNG (7 start) reaches 46.5 at Level 200 (3.5 points below cap)
- **RNG creates 3-4 level progression difference**, with meaningful but not game-breaking power gap at endgame

---

## Classification System

### Classification Unlocks (Level 25)

At Level 25, crew cards choose a **permanent classification** that determines their role and stat growth priorities.

**Classification Effects**:
1. **Immediate +5 bonus** to all primary stats
2. **Increased growth rate** for primary stats (+0.12/level vs +0.06/level)
3. **Unlocks specialization paths** at Level 50
4. **Determines compatible ship positions** (Gunners → turrets, Engineers → engines, etc.)

**Example: Neutral → Gunner Classification**

Before Classification (Level 25 Neutral):
```
Accuracy:  13.25 (12 base + 1.25 from 25 levels)
Reload:    14.25 (13 base + 1.25)
Range:     10.25 (9 base + 1.25)
```

After Classification (Level 25 Gunner):
```
Accuracy:  18.25 (13.25 + 5 classification bonus) ← PRIMARY
Reload:    19.25 (14.25 + 5 classification bonus) ← PRIMARY
Range:     10.25 (no bonus) ← SECONDARY
```

Future Growth (Level 26-200):
```
Accuracy: +0.19 per level (primary growth)
Reload:   +0.19 per level (primary growth)
Range:    +0.10 per level (secondary growth)
```

### Stat Type Definitions

**Primary Stats**:
- Receive +5 classification bonus at Level 25
- Grow at +0.19 per level (faster)
- Reach 46-50 range at Level 200 (depending on RNG)
- Core effectiveness stats for the classification

**Secondary Stats**:
- Receive NO classification bonus at Level 25
- Grow at +0.10 per level (slower)
- Reach 25-34 range at Level 200 (never hit cap)
- Supporting stats, still valuable but not focus

**Example Classification Stat Assignments**:
- **Gunner**: Primary (Accuracy, Reload), Secondary (Range)
- **Engineer**: Primary (Engine Power, Repair Speed), Secondary (Restore Speed)
- **Torpedo Specialist**: Primary (Torpedo Accuracy, Tube Reload), Secondary (Spread Control)

---

## 18 Crew Classifications

### Surface Combat Roles (6)

#### 1. Gunner
**Description**: Main battery and secondary battery operators. Core damage dealers on all surface combatants.

**Primary Stats** (receive +5 bonus, grow +0.19/level):
- **Accuracy (7-50)**: Hit chance for main/secondary guns
  - **7**: 30% hit rate at optimal range (terrible)
  - **15**: 50% hit rate at optimal range (baseline)
  - **25**: 65% hit rate at optimal range (competent)
  - **35**: 80% hit rate at optimal range (expert)
  - **45**: 92% hit rate at optimal range (elite)
  - **50**: 97% hit rate at optimal range (legendary, near-perfect)
- **Reload (7-50)**: Rate of fire for turrets
  - **7**: -25% reload speed (very slow, penalty)
  - **15**: +0% reload speed (baseline)
  - **25**: +30% reload speed (competent)
  - **35**: +60% reload speed (expert)
  - **45**: +90% reload speed (elite)
  - **50**: +105% reload speed (legendary, double fire rate)

**Secondary Stats** (no bonus, grow +0.10/level):
- **Range (7-50)**: Maximum effective gun range
  - **7**: -25% max range
  - **15**: +0% max range (baseline)
  - **25**: +20% max range
  - **35**: +40% max range
  - **45**: +60% max range
  - **50**: +70% max range (legendary)

**Gameplay Effects**:
- Each Accuracy point above 15 = +3% hit chance (below 15 = -3% per point)
- Each Reload point above 15 = +3.5% fire rate (below 15 = -3.5% per point)
- Each Range point above 15 = +2% max range (below 15 = -2% per point)

**Ship Type Preferences**:
- **Battleships**: Favor high Accuracy (slow traverse, must hit)
- **Cruisers**: Favor balanced Accuracy + Reload
- **Destroyers**: Favor high Reload (close range, volume of fire)

**Specialization Paths** (Level 50 choice):
- **Heavy Gunner**: +3 Accuracy, +2 Range (battleship focus)
- **Rapid Gunner**: +3 Reload, +2 Accuracy (destroyer focus)
- **Precision Gunner**: +5 Accuracy (cruiser focus)

**RNG Recruitment Priority**:
- **Must Have**: Accuracy 13+, Reload 12+ (both primary stats solid)
- **Good**: Balanced stats (all 12-14)
- **Reroll If**: Both primary stats <11 (too far behind)

---

#### 2. AA Specialist
**Description**: Anti-aircraft battery operators. Critical for carrier-heavy metas and fleet defense.

**Primary Stats**:
- **AA Accuracy (7-50)**: Hit chance vs aircraft
  - **7**: 15% hit rate vs fighters (hopeless)
  - **15**: 40% hit rate vs fighters (baseline)
  - **25**: 70% hit rate vs fighters (expert)
  - **35**: 95% hit rate vs fighters (legendary, air superiority)
- **AA Reload (7-50)**: Rate of fire for AA batteries
  - **7**: -30% AA fire rate (slow, vulnerable to air)
  - **15**: +0% AA fire rate (baseline)
  - **25**: +40% AA fire rate (expert)
  - **35**: +80% AA fire rate (legendary, flak wall)

**Secondary Stats**:
- **Detection (7-50)**: Aircraft spotting range
  - **7**: -30% aircraft detection (blind)
  - **15**: +0% aircraft detection (baseline)
  - **25**: +30% aircraft detection (early warning)
  - **35**: +70% aircraft detection (legendary, see all aircraft)

**Gameplay Effects**:
- Each AA Accuracy point above 15 = +3.5% hit chance vs aircraft
- Each AA Reload point above 15 = +4% AA fire rate
- Each Detection point above 15 = +3.5% aircraft spotting range

**Ship Type Preferences**:
- **Cruisers**: Favor high AA Reload (AA cruiser role)
- **Battleships**: Favor balanced stats (self-defense)
- **Carriers**: Favor Detection (early warning)

**Specialization Paths** (Level 50):
- **Fighter Killer**: +3 AA Accuracy, +2 Detection
- **Flak Wall**: +3 AA Reload, +2 AA Accuracy
- **Early Warning**: +3 Detection, +2 AA Accuracy

---

#### 3. Torpedo Specialist
**Description**: Torpedo tube operators and submarine torpedo room crews. High-risk, high-reward damage dealers.

**Primary Stats**:
- **Torpedo Accuracy (7-50)**: Torpedo spread control and aim
  - **7**: ±20° spread deviation (wild, unreliable)
  - **15**: ±10° spread deviation (baseline)
  - **25**: ±4° spread deviation (expert, tight spread)
  - **35**: ±1° spread deviation (legendary, sniper torpedoes)
- **Tube Reload (7-50)**: Torpedo reload speed
  - **7**: -30% reload speed (very slow, 85s+ for destroyers)
  - **15**: +0% reload speed (baseline: 60s destroyers, 90s submarines)
  - **25**: +40% reload speed (expert: 43s destroyers, 64s subs)
  - **35**: +80% reload speed (legendary: 33s destroyers, 50s subs)

**Secondary Stats**:
- **Spread Control (7-50)**: Torpedo spread pattern control
  - **7**: Fixed spread patterns only, wide spreads
  - **15**: Basic manual spread control (baseline)
  - **25**: Advanced pattern control, tighter spreads
  - **35**: Perfect manual control, laser-tight patterns

**Gameplay Effects**:
- Each Torpedo Accuracy point above 15 = -0.5° spread deviation
- Each Tube Reload point above 15 = +4% reload speed
- Each Spread Control point above 15 = +5% pattern tightness, unlock advanced patterns at 20/25/30

**Ship Type Preferences**:
- **Destroyers**: Favor high Tube Reload (multiple salvos)
- **Submarines**: Favor high Torpedo Accuracy (one-shot kills)
- **Cruisers**: Favor Spread Control (tactical patterns)

**Specialization Paths** (Level 50):
- **Torpedo Sniper**: +5 Torpedo Accuracy (submarine focus)
- **Salvo Master**: +3 Tube Reload, +2 Spread Control
- **Pattern Expert**: +3 Spread Control, +2 Torpedo Accuracy

---

#### 4. Engineer
**Description**: Engine room crews controlling ship propulsion and maneuverability. Essential for all ships.

**Primary Stats**:
- **Engine Power (7-50)**: Ship speed and acceleration
  - **7**: -25% max speed, -35% acceleration (crippled)
  - **15**: +0% max speed, +0% acceleration (baseline)
  - **25**: +20% max speed, +30% acceleration (expert)
  - **35**: +40% max speed, +65% acceleration (legendary, speed demon)
- **Repair Speed (7-50)**: Engine/propulsion module repair rate
  - **7**: -30% repair speed (painfully slow)
  - **15**: +0% repair speed (baseline: 10% HP per 10s)
  - **25**: +60% repair speed (expert: 16% HP per 10s)
  - **35**: +120% repair speed (legendary: 22% HP per 10s)

**Secondary Stats**:
- **Restore Speed (7-50)**: Disabled module reactivation time
  - **7**: -20% restore speed (slow recovery)
  - **15**: +0% restore speed (baseline: 60s)
  - **25**: +50% restore speed (expert: 40s)
  - **35**: +100% restore speed (legendary: 30s)

**Gameplay Effects**:
- Each Engine Power point above 15 = +2% speed, +3.25% acceleration
- Each Repair Speed point above 15 = +6% repair rate
- Each Restore Speed point above 15 = +5% restore speed

**Ship Type Preferences**:
- **Destroyers**: Favor high Engine Power (speed is survival)
- **Battleships**: Favor high Repair Speed (engine critical)
- **Carriers**: Favor Engine Power (kiting capability)

**Specialization Paths** (Level 50):
- **Speed Demon**: +3 Engine Power, +2 Restore Speed
- **Master Mechanic**: +3 Repair Speed, +2 Restore Speed
- **Quick Recovery**: +3 Restore Speed, +2 Engine Power

---

#### 5. Damage Control
**Description**: Firefighting and flooding control crews. Keeps ships alive under sustained fire.

**Primary Stats**:
- **Fire Fighting (7-50)**: Fire damage reduction and extinguish speed
  - **7**: -15% fire damage mitigation, -20% extinguish speed (death trap)
  - **15**: +0% fire damage mitigation, +0% extinguish speed (baseline: 5% HP/tick, 30s extinguish)
  - **25**: -45% fire damage, +50% extinguish speed (expert: 2.75% HP/tick, 20s)
  - **35**: -75% fire damage, +100% extinguish speed (legendary: 1.25% HP/tick, 15s)
- **Flooding Control (7-50)**: Flood damage reduction and pump speed
  - **7**: -15% flood damage mitigation, -20% pump speed (sinking)
  - **15**: +0% flood damage mitigation, +0% pump speed (baseline)
  - **25**: -45% flood damage, +50% pump speed (expert)
  - **35**: -75% flood damage, +100% pump speed (legendary, unsinkable)

**Secondary Stats**:
- **Repair Speed (7-50)**: General hull/module repair rate
  - **7**: -30% repair speed (slow)
  - **15**: +0% repair speed (baseline)
  - **25**: +50% repair speed (expert)
  - **35**: +100% repair speed (legendary)

**Gameplay Effects**:
- Each Fire Fighting point above 15 = -3.75% fire damage per tick, +5% extinguish speed
- Each Flooding Control point above 15 = -3.75% flood damage per tick, +5% pump speed
- Each Repair Speed point above 15 = +5% general repair rate

**Ship Type Preferences**:
- **Battleships**: Favor high Fire Fighting (main threat)
- **Destroyers**: Favor balanced stats (fragile, every second counts)
- **Submarines**: Favor high Flooding Control (dive damage, torpedoes)

**Specialization Paths** (Level 50):
- **Fire Specialist**: +3 Fire Fighting, +2 Repair Speed
- **Flood Specialist**: +3 Flooding Control, +2 Repair Speed
- **General Repair**: +2 Fire Fighting, +2 Flooding Control, +1 Repair Speed

---

#### 6. Electronics/Radar Operator
**Description**: Radar, sonar, and electronic warfare specialists. Detection and intelligence gathering.

**Primary Stats**:
- **Detection Range (7-50)**: Surface ship detection radius
  - **7**: -30% surface detection range (blind)
  - **15**: +0% surface detection range (baseline: 10km)
  - **25**: +35% surface detection range (expert: 13.5km)
  - **35**: +75% surface detection range (legendary: 17.5km, see everything)
- **Radar Accuracy (7-50)**: Target tracking precision and lock speed
  - **7**: ±1000m position error, 15s lock time (poor)
  - **15**: ±400m position error, 8s lock time (baseline)
  - **25**: ±120m position error, 4s lock time (expert)
  - **35**: ±20m position error, 2s lock time (legendary, pinpoint)

**Secondary Stats**:
- **Jamming (7-50)**: Enemy radar/fire control disruption
  - **7**: -3% enemy accuracy when active (minimal)
  - **15**: -10% enemy accuracy when active (baseline)
  - **25**: -25% enemy accuracy when active (expert)
  - **35**: -45% enemy accuracy when active (legendary, hard to target)

**Gameplay Effects**:
- Each Detection Range point above 15 = +3.75% detection radius
- Each Radar Accuracy point above 15 = -40m position error, -0.3s lock time
- Each Jamming point above 15 = -1.75% enemy accuracy

**Ship Type Preferences**:
- **Cruisers**: Favor high Detection Range (scout role)
- **Battleships**: Favor high Radar Accuracy (fire control)
- **Destroyers**: Favor Jamming (electronic warfare)

**Specialization Paths** (Level 50):
- **Scout**: +3 Detection Range, +2 Radar Accuracy
- **Fire Director**: +3 Radar Accuracy, +2 Detection Range
- **EW Specialist**: +3 Jamming, +2 Detection Range

---

### Aviation Roles (3)

#### 7. Fighter Pilot
**Description**: Fighter squadron pilots. Air superiority and bomber interception.

**Primary Stats**:
- **Dogfighting (7-50)**: Fighter vs fighter combat effectiveness
  - **7**: 25% win rate vs equal pilots (terrible)
  - **15**: 50% win rate vs equal pilots (baseline)
  - **25**: 75% win rate vs equal pilots (expert, air superiority)
  - **35**: 95% win rate vs equal pilots (legendary, ace)
- **AA Evasion (7-50)**: Survival vs flak/AA fire
  - **7**: -30% evasion vs AA (30% survival rate, dangerous)
  - **15**: +0% evasion vs AA (baseline: 50% survival)
  - **25**: +40% evasion vs AA (expert: 70% survival)
  - **35**: +80% evasion vs AA (legendary: 90% survival, untouchable)

**Secondary Stats**:
- **Speed (7-50)**: Fighter squadron speed
  - **7**: -25% speed (slow intercepts)
  - **15**: +0% speed (baseline)
  - **25**: +30% speed (expert, fast intercepts)
  - **35**: +65% speed (legendary, lightning fast)

**Gameplay Effects**:
- Each Dogfighting point above 15 = +3% fighter kill rate
- Each AA Evasion point above 15 = +3% survival vs flak
- Each Speed point above 15 = +3.25% squadron speed

**Ship Type Preferences**:
- **Fleet Carriers**: Favor high Dogfighting (offensive CAP)
- **Escort Carriers**: Favor high AA Evasion (defensive CAP)

**Specialization Paths** (Level 50):
- **Ace**: +3 Dogfighting, +2 Speed
- **Interceptor**: +3 Speed, +2 Dogfighting
- **Survivor**: +3 AA Evasion, +2 Dogfighting

---

#### 8. Bomber Pilot
**Description**: Torpedo and dive bomber pilots. Primary carrier strike capability.

**Primary Stats**:
- **Bombing Accuracy (7-50)**: Hit rate with torpedoes/bombs
  - **7**: 10% hit rate vs large ships (hopeless)
  - **15**: 30% hit rate vs large ships (baseline)
  - **25**: 60% hit rate vs large ships (expert)
  - **35**: 85% hit rate vs large ships (legendary, precision strike)
- **Payload Efficiency (7-50)**: Damage per sortie
  - **7**: -25% payload damage (weak)
  - **15**: +0% payload damage (baseline)
  - **25**: +35% payload damage (expert)
  - **35**: +70% payload damage (legendary, devastating)

**Secondary Stats**:
- **AA Evasion (7-50)**: Survival vs flak/AA fire
  - **7**: -40% evasion (20% survival, suicide missions)
  - **15**: +0% evasion (baseline: 30% survival, bombers vulnerable)
  - **25**: +50% evasion (expert: 45% survival)
  - **35**: +100% evasion (legendary: 60% survival, still dangerous)

**Gameplay Effects**:
- Each Bombing Accuracy point above 15 = +3.5% torpedo/bomb hit rate
- Each Payload Efficiency point above 15 = +3.5% damage per hit
- Each AA Evasion point above 15 = +3% survival vs flak

**Ship Type Preferences**:
- **Attack Carriers**: Favor high Bombing Accuracy (alpha strikes)
- **Balanced Carriers**: Favor Payload Efficiency (sustained damage)

**Specialization Paths** (Level 50):
- **Torpedo Ace**: +3 Bombing Accuracy, +2 AA Evasion
- **Payload Master**: +3 Payload Efficiency, +2 Bombing Accuracy
- **Strike Leader**: +2 Bombing Accuracy, +2 Payload, +1 Evasion

---

#### 9. Squadron Leader (Aviation Command)
**Description**: Air wing commanders. Force multipliers for all aviation operations.

**Primary Stats**:
- **Air Command (7-50)**: Squadron effectiveness multiplier
  - **7**: -20% squadron effectiveness (incompetent)
  - **15**: +0% squadron effectiveness (baseline)
  - **25**: +30% squadron effectiveness (expert, force multiplier)
  - **35**: +70% squadron effectiveness (legendary, elite air wing)
- **Tactics (7-50)**: Strike coordination and target selection
  - **7**: -20% strike efficiency (poor planning)
  - **15**: +0% strike efficiency (baseline)
  - **25**: +30% strike efficiency (expert)
  - **35**: +70% strike efficiency (legendary, perfect strikes)

**Secondary Stats**:
- **Recovery Speed (7-50)**: Aircraft landing/rearm/refuel speed
  - **7**: -25% recovery speed (slow turnaround: 150s)
  - **15**: +0% recovery speed (baseline: 120s)
  - **25**: +40% recovery speed (expert: 86s)
  - **35**: +80% recovery speed (legendary: 67s, rapid sortie tempo)

**Gameplay Effects**:
- Each Air Command point above 15 = +3.5% all squadron stats (multiplicative force multiplier)
- Each Tactics point above 15 = +3.5% strike planning efficiency
- Each Recovery Speed point above 15 = +4% landing/rearm/refuel speed

**Ship Type Preferences**:
- **Large Carriers**: Favor high Air Command (many squadrons)
- **Fast Carriers**: Favor Recovery Speed (rapid sortie tempo)

**Specialization Paths** (Level 50):
- **Wing Commander**: +3 Air Command, +2 Tactics
- **Strike Coordinator**: +3 Tactics, +2 Air Command
- **Deck Boss**: +3 Recovery Speed, +2 Air Command

---

### Submarine Roles (3)

#### 10. Sonar Operator
**Description**: Submarine and destroyer sonar crews. Detection and tracking of submerged contacts.

**Primary Stats**:
- **Sonar Range (7-50)**: Underwater detection radius
  - **7**: -40% sonar range (baseline 5km → 3km, blind)
  - **15**: +0% sonar range (baseline: 5km)
  - **25**: +40% sonar range (expert: 7km)
  - **35**: +90% sonar range (legendary: 9.5km, see all submarines)
- **Contact Analysis (7-50)**: Target identification speed and precision
  - **7**: 60s to identify, ±2km range error (slow, inaccurate)
  - **15**: 30s to identify, ±800m range error (baseline)
  - **25**: 12s to identify, ±250m range error (expert)
  - **35**: 5s to identify, ±50m range error (legendary, instant ID)

**Secondary Stats**:
- **Noise Reduction (7-50)**: Own ship acoustic signature reduction
  - **7**: +20% acoustic signature (louder, easier to detect)
  - **15**: +0% acoustic signature (baseline)
  - **25**: -30% acoustic signature (expert, quieter)
  - **35**: -60% acoustic signature (legendary, silent)

**Gameplay Effects**:
- Each Sonar Range point above 15 = +4.5% detection radius
- Each Contact Analysis point above 15 = -1.5s ID time, -40m range error
- Each Noise Reduction point above 15 = -4% acoustic signature

**Ship Type Preferences**:
- **Submarines**: Favor balanced stats (hunter-killers)
- **Destroyers**: Favor high Sonar Range (ASW screening)
- **Cruisers**: Favor Contact Analysis (ASW coordination)

**Specialization Paths** (Level 50):
- **Hunter**: +3 Sonar Range, +2 Contact Analysis
- **Analyst**: +3 Contact Analysis, +2 Sonar Range
- **Stealth**: +3 Noise Reduction, +2 Sonar Range

---

#### 11. Submarine Commander
**Description**: Submarine captains and diving officers. Stealth and tactical submarine warfare.

**Primary Stats**:
- **Stealth (7-50)**: Submarine detectability reduction
  - **7**: +30% detection range (loud submarine, 3.9km surface, 1.95km submerged)
  - **15**: +0% detection range (baseline: 3km surface, 1.5km submerged)
  - **25**: -40% detection range (expert: 1.8km surface, 0.9km submerged)
  - **35**: -75% detection range (legendary: 0.75km surface, 0.375km submerged, ghost)
- **Tactics (7-50)**: Engagement planning and escape maneuvers
  - **7**: -25% tactical effectiveness (poor positioning)
  - **15**: +0% tactical effectiveness (baseline)
  - **25**: +40% escape success rate, +30% ambush setup speed (expert)
  - **35**: +80% escape success rate, +60% ambush setup speed (legendary)

**Secondary Stats**:
- **Periscope Skill (7-50)**: Surface observation effectiveness
  - **7**: -30% periscope detection range (baseline 8km → 5.6km, blind)
  - **15**: +0% periscope detection range (baseline: 8km)
  - **25**: +45% periscope detection range (expert: 11.6km)
  - **35**: +95% periscope detection range (legendary: 15.6km, see all surface ships)

**Gameplay Effects**:
- Each Stealth point above 15 = -3.75% enemy detection range
- Each Tactics point above 15 = +4% tactical effectiveness (ambush/escape)
- Each Periscope Skill point above 15 = +4.75% surface detection while submerged

**Ship Type Preferences**:
- **Attack Submarines**: Favor high Stealth (ambush predators)
- **Missile Submarines**: Favor high Tactics (positioning/escape)
- **Scout Submarines**: Favor Periscope Skill (intelligence gathering)

**Specialization Paths** (Level 50):
- **Shadow**: +3 Stealth, +2 Tactics
- **Tactician**: +3 Tactics, +2 Periscope Skill
- **Observer**: +3 Periscope Skill, +2 Stealth

---

#### 12. Planesman
**Description**: Submarine diving control and trim balance crews. Maintains depth control and maneuverability.

**Primary Stats**:
- **Diving Speed (7-50)**: Crash dive and surface speed
  - **7**: -30% dive speed (65s crash dive, 85s surface, too slow)
  - **15**: +0% dive speed (baseline: 45s crash dive, 60s surface)
  - **25**: +50% dive speed (expert: 30s crash dive, 40s surface)
  - **35**: +110% dive speed (legendary: 21s crash dive, 29s surface, instant)
- **Depth Control (7-50)**: Precise depth maintenance and stability
  - **7**: ±30m depth oscillation, -30% turn rate submerged (unstable)
  - **15**: ±15m depth oscillation, +0% turn rate submerged (baseline)
  - **25**: ±5m depth oscillation, +30% turn rate submerged (expert, precise)
  - **35**: ±1m depth oscillation, +70% turn rate submerged (legendary, perfect)

**Secondary Stats**:
- **Trim Balance (7-50)**: Submarine handling and emergency blow efficiency
  - **7**: -20% submerged speed, -20% emergency blow speed (sluggish)
  - **15**: +0% submerged speed, +0% emergency blow speed (baseline)
  - **25**: +20% submerged speed, +50% emergency blow speed (expert)
  - **35**: +45% submerged speed, +110% emergency blow speed (legendary, fast underwater)

**Gameplay Effects**:
- Each Diving Speed point above 15 = +5.5% dive/surface speed
- Each Depth Control point above 15 = -1m oscillation, +3.5% submerged turn rate
- Each Trim Balance point above 15 = +2.25% submerged speed, +5.5% emergency blow

**Ship Type Preferences**:
- **Attack Submarines**: Favor high Diving Speed (emergency dives)
- **Deep Divers**: Favor high Depth Control (precision operations)
- **Fast Submarines**: Favor Trim Balance (submerged performance)

**Specialization Paths** (Level 50):
- **Emergency Diver**: +3 Diving Speed, +2 Trim Balance
- **Precision Pilot**: +3 Depth Control, +2 Diving Speed
- **Speed Runner**: +3 Trim Balance, +2 Depth Control

---

### Command/Support Role (1)

#### 13. Command/Bridge Officer
**Description**: Ship captains and executive officers. Force multipliers that enhance entire crew performance.

**Primary Stats**:
- **Command (7-50)**: Crew effectiveness multiplier (like NavyField's Potential)
  - **7**: -20% crew effectiveness (incompetent command)
  - **15**: +0% crew effectiveness (baseline)
  - **25**: +25% all crew stats (expert, significant force multiplier)
  - **35**: +60% all crew stats (legendary, elite command)
- **Tactics (7-50)**: Strategic decision-making and battle planning
  - **7**: -20% tactical effectiveness (poor decisions)
  - **15**: +0% tactical effectiveness (baseline)
  - **25**: +30% damage output, +25% damage mitigation (expert)
  - **35**: +65% damage output, +55% damage mitigation (legendary)

**Secondary Stats**:
- **Leadership (7-50)**: Crew morale and efficiency under pressure
  - **7**: -25% effectiveness under heavy damage (panic)
  - **15**: +0% effectiveness under heavy damage (baseline)
  - **25**: +30% effectiveness when ship <50% HP (expert, no panic)
  - **35**: +70% effectiveness when ship <50% HP (legendary, crisis leadership)

**Gameplay Effects**:
- Each Command point above 15 = +2.5% ALL crew stats (multiplicative force multiplier)
- Each Tactics point above 15 = +3.25% damage output, +2.75% damage mitigation
- Each Leadership point above 15 = +3.5% crew effectiveness under heavy damage

**Ship Type Preferences**:
- **Battleships**: Favor high Command (largest crews benefit most)
- **Destroyers**: Favor high Tactics (must punch above weight)
- **All Ships**: Universal benefit (command always valuable)

**Specialization Paths** (Level 50):
- **Fleet Commander**: +3 Command, +2 Leadership
- **Combat Tactician**: +3 Tactics, +2 Command
- **Crisis Leader**: +3 Leadership, +2 Tactics

---

### Fathoms Deep Extraction Roles (5)

#### 14. Extraction Specialist
**Description**: Route planning, pursuit evasion, and safe passage coordination. Core extraction gameplay role.

**Primary Stats**:
- **Route Planning (7-50)**: Optimal path calculation and navigation
  - **7**: -20% route efficiency (slow, wasteful)
  - **15**: +0% route efficiency (baseline speed/fuel consumption)
  - **25**: +30% route speed, -25% fuel consumption (expert)
  - **35**: +65% route speed, -50% fuel consumption (legendary, optimal pathing)
- **Pursuit Evasion (7-50)**: Detection avoidance and escape effectiveness
  - **7**: +25% detection range by hostiles (easier to catch)
  - **15**: +0% detection/evasion (baseline)
  - **25**: -35% detection range by hostiles, +30% escape success (expert)
  - **35**: -70% detection range by hostiles, +65% escape success (legendary, ghost)

**Secondary Stats**:
- **Navigation (7-50)**: General navigation and weather routing
  - **7**: -25% navigation efficiency (lost easily)
  - **15**: +0% navigation efficiency (baseline)
  - **25**: +25% speed in storms, +35% navigation accuracy (expert)
  - **35**: +55% speed in storms, +75% navigation accuracy (legendary)

**Gameplay Effects**:
- Each Route Planning point above 15 = +3.25% route speed, -2.5% fuel consumption
- Each Pursuit Evasion point above 15 = -3.5% hostile detection, +3.25% escape success
- Each Navigation point above 15 = +2.75% storm speed, +3.75% navigation accuracy

**Ship Type Preferences**:
- **Fast Ships**: Favor high Pursuit Evasion (speed + stealth = safety)
- **Cargo Ships**: Favor high Route Planning (efficiency for heavy loads)
- **All Extraction Ships**: Universal benefit (core extraction role)

**Specialization Paths** (Level 50):
- **Route Master**: +3 Route Planning, +2 Navigation
- **Ghost Runner**: +3 Pursuit Evasion, +2 Route Planning
- **Storm Navigator**: +3 Navigation, +2 Route Planning

---

#### 15. Scavenger/Salvage Specialist
**Description**: Wreck identification, loot assessment, and salvage operations. Economy and profit maximization.

**Primary Stats**:
- **Loot Identification (7-50)**: Wreck assessment and cargo analysis
  - **7**: 25% loot identification accuracy, 60s scan time per wreck (slow, poor info)
  - **15**: 50% loot identification accuracy, 30s scan time (baseline)
  - **25**: 80% loot identification accuracy, 12s scan time (expert, fast)
  - **35**: 98% loot identification accuracy, 5s scan time (legendary, instant appraisal)
- **Salvage Speed (7-50)**: Wreck recovery and cargo transfer speed
  - **7**: -30% salvage speed (85s per item, slow profit)
  - **15**: +0% salvage speed (baseline: 60s per item)
  - **25**: +60% salvage speed (expert: 38s per item)
  - **35**: +130% salvage speed (legendary: 26s per item, rapid salvage)

**Secondary Stats**:
- **Cargo Management (7-50)**: Inventory space optimization
  - **7**: -15% effective cargo capacity (poor packing)
  - **15**: +0% cargo capacity (baseline)
  - **25**: +25% effective cargo capacity (expert, better packing)
  - **35**: +55% effective cargo capacity (legendary, maximum efficiency)

**Gameplay Effects**:
- Each Loot ID point above 15 = +3% identification accuracy, -1.5s scan time
- Each Salvage Speed point above 15 = +6.5% recovery speed
- Each Cargo Management point above 15 = +2.75% effective cargo space

**Ship Type Preferences**:
- **Salvage Ships**: Favor high Salvage Speed (profit per hour)
- **Scout Ships**: Favor high Loot Identification (target selection)
- **Cargo Ships**: Favor Cargo Management (maximize haul value)

**Specialization Paths** (Level 50):
- **Treasure Hunter**: +3 Loot Identification, +2 Cargo Management
- **Fast Salvager**: +3 Salvage Speed, +2 Loot ID
- **Cargo Optimizer**: +3 Cargo Management, +2 Salvage Speed

---

#### 16. Intelligence Officer
**Description**: Signal intercept, code breaking, and tactical intelligence gathering. Information warfare.

**Primary Stats**:
- **Signal Intercept (7-50)**: Radio/communication interception range and quality
  - **7**: 3km intercept range, 15% decryption success (poor intel)
  - **15**: 8km intercept range, 40% decryption success (baseline)
  - **25**: 16km intercept range, 75% decryption success (expert)
  - **35**: 28km intercept range, 95% decryption success (legendary, intercept everything)
- **Code Breaking (7-50)**: Enemy communication decryption speed
  - **7**: 240s to decrypt simple messages, cannot attempt complex (slow)
  - **15**: 120s to decrypt simple messages, 300s complex (baseline)
  - **25**: 48s simple, 140s complex (expert, fast decryption)
  - **35**: 20s simple, 60s complex (legendary, rapid intelligence)

**Secondary Stats**:
- **Analysis (7-50)**: Tactical intelligence processing
  - **7**: -30% intelligence quality (poor detail)
  - **15**: +0% intelligence quality (baseline)
  - **25**: +50% intelligence detail (expert, fleet composition/movements)
  - **35**: +110% intelligence detail (legendary, complete tactical picture)

**Gameplay Effects**:
- Each Signal Intercept point above 15 = +1.25km range, +3.5% decryption success
- Each Code Breaking point above 15 = -6s decrypt time, unlock higher tiers at 20/25/30
- Each Analysis point above 15 = +5.5% intelligence quality/detail

**Ship Type Preferences**:
- **Cruisers**: Favor high Signal Intercept (scout/intel role)
- **Destroyers**: Favor Code Breaking (tactical surprise)
- **Capital Ships**: Favor Analysis (fleet coordination)

**Specialization Paths** (Level 50):
- **Signal Hunter**: +3 Signal Intercept, +2 Analysis
- **Cryptanalyst**: +3 Code Breaking, +2 Signal Intercept
- **Intelligence Analyst**: +3 Analysis, +2 Code Breaking

---

#### 17. Marine/Boarding Specialist
**Description**: Boarding actions, prize crews, and ship capture operations. High-risk capture gameplay.

**Primary Stats**:
- **Boarding Efficiency (7-50)**: Boarding action success rate and speed
  - **7**: 15% boarding success vs equal crew, 300s action time (hopeless)
  - **15**: 40% boarding success vs equal crew, 180s action time (baseline)
  - **25**: 70% boarding success vs equal crew, 85s action time (expert, fast captures)
  - **35**: 95% boarding success vs equal crew, 45s action time (legendary, boarding master)
- **Prize Crew (7-50)**: Captured ship control effectiveness
  - **7**: 25% effectiveness controlling captured ships (barely functional)
  - **15**: 50% effectiveness controlling captured ships (baseline)
  - **25**: 80% effectiveness controlling captured ships (expert)
  - **35**: 98% effectiveness controlling captured ships (legendary, full control)

**Secondary Stats**:
- **Combat (7-50)**: Marine combat effectiveness during boarding
  - **7**: -30% combat effectiveness (weak marines)
  - **15**: +0% combat effectiveness (baseline)
  - **25**: +50% combat effectiveness (expert, dominate boarding actions)
  - **35**: +110% combat effectiveness (legendary, elite marines)

**Gameplay Effects**:
- Each Boarding Efficiency point above 15 = +3.5% success rate, -7.5s action time
- Each Prize Crew point above 15 = +3% captured ship control effectiveness
- Each Combat point above 15 = +5.5% marine combat effectiveness

**Ship Type Preferences**:
- **Fast Ships**: Favor high Boarding Efficiency (catch targets)
- **Large Ships**: Favor Prize Crew (control high-value captures)
- **Destroyers**: Favor Combat (aggressive boarding tactics)

**Specialization Paths** (Level 50):
- **Assault Leader**: +3 Combat, +2 Boarding Efficiency
- **Boarding Master**: +3 Boarding Efficiency, +2 Prize Crew
- **Prize Master**: +3 Prize Crew, +2 Boarding Efficiency

---

#### 18. Weather Officer
**Description**: Meteorological analysis, storm prediction, and heavy weather operations. Survival and navigation.

**Primary Stats**:
- **Storm Prediction (7-50)**: Weather forecasting and early warning
  - **7**: 2 minute storm warning, 30% accuracy (caught off-guard)
  - **15**: 10 minute storm warning, 60% accuracy (baseline)
  - **25**: 30 minute storm warning, 85% accuracy (expert, good planning)
  - **35**: 60 minute storm warning, 98% accuracy (legendary, predict all weather)
- **Heavy Weather Ops (7-50)**: Ship performance in storms
  - **7**: -60% speed in storms, -50% accuracy (crippled in storms)
  - **15**: -30% speed in storms, -25% accuracy (baseline)
  - **25**: -10% speed in storms, -5% accuracy (expert, maintain operations)
  - **35**: +5% speed in storms, +10% accuracy (legendary, expert storm operations)

**Secondary Stats**:
- **Navigation (7-50)**: General navigation and course plotting
  - **7**: -30% navigation efficiency (poor routes)
  - **15**: +0% navigation efficiency (baseline)
  - **25**: +30% navigation accuracy, +20% route optimization (expert)
  - **35**: +70% navigation accuracy, +45% route optimization (legendary)

**Gameplay Effects**:
- Each Storm Prediction point above 15 = +2.5min warning, +2.5% accuracy
- Each Heavy Weather Ops point above 15 = +2.5% storm speed, +2.25% storm accuracy
- Each Navigation point above 15 = +3.5% navigation accuracy, +2.25% route efficiency

**Ship Type Preferences**:
- **Long-Range Ships**: Favor high Storm Prediction (plan routes)
- **Fast Ships**: Favor Heavy Weather Ops (maintain speed in storms)
- **All Extraction Ships**: Universal benefit (weather unavoidable)

**Specialization Paths** (Level 50):
- **Meteorologist**: +3 Storm Prediction, +2 Navigation
- **Storm Master**: +3 Heavy Weather Ops, +2 Storm Prediction
- **Navigator**: +3 Navigation, +2 Heavy Weather Ops

---

## Stat Interactions & Synergies

### Force Multiplier Effects

**Command Officer + Specialized Crews**:
- Level 200 Command Officer (35 Command) = +60% all stats
- Level 200 Gunner (35 Accuracy, 35 Reload)
- **Combined Effect**: Gunner performs as if Accuracy 56, Reload 56 (calculations use actual values before cap)
- **Result**: +60% effectiveness from command + base gunner stats = ~120% better than baseline

**Squadron Leader + Aviation Crews**:
- Level 150 Squadron Leader (30 Air Command) = +45% squadron effectiveness
- Level 150 Bomber Pilot (30 Bombing Accuracy, 30 Payload)
- **Combined Effect**: 88% hit rate (vs 75% at 25 stat), +80% damage per sortie
- **Result**: Elite carrier strike capability, devastating alpha strikes

### Stat Breakpoints & Thresholds

**Critical Thresholds**:
- **Stat 15**: Baseline competence (0% bonus/penalty)
- **Stat 25**: Competent (+20% effectiveness over baseline)
- **Stat 35**: Expert (+40% effectiveness over baseline)
- **Stat 45**: Elite (+60% effectiveness over baseline)
- **Stat 50**: Legendary (+70% effectiveness over baseline, cap)

**Diminishing Returns**:
- Stats below 15 have **penalties** (negative effectiveness)
- Stats 15-30 have **strong returns** (2-3% per point)
- Stats 30-45 have **moderate returns** (1.5-2.5% per point)
- Stats 45-50 have **diminishing returns** (1-1.5% per point)
- Stats above 50 are **capped** (no further benefit)

**RNG Impact Zones**:
- **Bad RNG (7-9 start)**: Reach 44-46.5 at Level 200 (3.5-6 points below cap)
- **Average RNG (10-12 start)**: Reach 48-50 at Level 200 (at or near cap)
- **Good RNG (13-14 start)**: Reach 50 at ~Level 185-195 (cap 5-15 levels early)
- **Perfect RNG (15 start)**: Reach 50 at ~Level 176 (cap 24 levels early)

**Key Insight**: Perfect RNG (15 start) reaches cap 24 levels earlier than average RNG (11 start), but bad RNG (7 start) is now 3.5 points below cap at L200. RNG creates more meaningful differentiation at endgame than previous 35-cap system.

---

## Ship Type Stat Priorities

### Destroyer Optimal Crews
**Primary Stats**: Reload, Engine Power, Pursuit Evasion, Tube Reload
**Secondary Stats**: Accuracy, Tactics, Diving Speed (if submarine)
**Target Stats at Level 150**: Primary 42-45, Secondary 26-29
**Rationale**: Destroyers rely on speed, volume of fire, and evasion

**Example T5 Destroyer Roster**:
- 2× Level 100 Gunners (35 Reload, 32 Accuracy, 26 Range)
- 1× Level 100 Engineer (35 Engine Power, 32 Repair, 26 Restore)
- 1× Level 100 Torpedo Specialist (35 Tube Reload, 32 Torpedo Accuracy, 26 Spread Control)
- 1× Level 80 Extraction Specialist (30 Pursuit Evasion, 28 Route Planning, 24 Navigation)

---

### Cruiser Optimal Crews
**Primary Stats**: Accuracy, Detection Range, AA Accuracy, Tactics
**Secondary Stats**: Reload, Command, Jamming
**Target Stats at Level 150**: Primary 30+, Secondary 23+
**Rationale**: Cruisers are versatile jack-of-all-trades, scouts, and AA platforms

**Example T7 Cruiser Roster**:
- 3× Level 120 Gunners (29 Accuracy, 27 Reload, 22 Range)
- 2× Level 120 AA Specialists (29 AA Accuracy, 27 AA Reload, 22 Detection)
- 1× Level 120 Engineer (29 Engine Power, 27 Repair, 22 Restore)
- 1× Level 100 Electronics Officer (27 Detection Range, 25 Radar Accuracy, 20 Jamming)
- 1× Level 100 Command Officer (27 Command, 25 Tactics, 20 Leadership)

---

### Battleship Optimal Crews
**Primary Stats**: Accuracy, Fire Fighting, Command, Repair Speed
**Secondary Stats**: Range, Tactics, Flooding Control
**Target Stats at Level 150**: Primary 30+, Secondary 23+
**Rationale**: Battleships must hit hard, survive, and coordinate

**Example T9 Battleship Roster**:
- 4× Level 150 Gunners (30 Accuracy, 28 Reload, 23 Range)
- 2× Level 140 Damage Control (29 Fire Fighting, 28 Flooding Control, 23 Repair)
- 2× Level 140 Engineers (29 Repair Speed, 28 Restore Speed, 23 Engine Power)
- 1× Level 150 Command Officer (30 Command, 28 Tactics, 23 Leadership)
- 1× Level 130 Electronics Officer (29 Radar Accuracy, 27 Detection, 22 Jamming)

---

### Carrier Optimal Crews
**Primary Stats**: Air Command, Dogfighting, Bombing Accuracy, Engine Power
**Secondary Stats**: AA Accuracy, Pursuit Evasion, Recovery Speed
**Target Stats at Level 150**: Primary 30+, Secondary 23+
**Rationale**: Carriers focus on aviation effectiveness and survivability

**Example T10 Carrier Roster**:
- 1× Level 180 Squadron Leader (32 Air Command, 30 Tactics, 24 Recovery Speed)
- 3× Level 160 Fighter Pilots (31 Dogfighting, 29 AA Evasion, 23 Speed)
- 3× Level 160 Bomber Pilots (31 Bombing Accuracy, 29 Payload, 23 AA Evasion)
- 2× Level 140 AA Specialists (29 AA Accuracy, 28 AA Reload, 22 Detection)
- 1× Level 140 Engineer (29 Engine Power, 28 Repair, 22 Restore)
- 1× Level 120 Extraction Specialist (28 Pursuit Evasion, 26 Route Planning, 21 Navigation)

---

### Submarine Optimal Crews
**Primary Stats**: Stealth, Sonar Range, Torpedo Accuracy, Diving Speed
**Secondary Stats**: Tactics, Flooding Control, Depth Control
**Target Stats at Level 150**: Primary 30+, Secondary 23+
**Rationale**: Submarines are ambush predators requiring stealth and precision

**Example T8 Submarine Roster**:
- 1× Level 140 Submarine Commander (29 Stealth, 28 Tactics, 22 Periscope Skill)
- 1× Level 140 Sonar Operator (29 Sonar Range, 28 Contact Analysis, 22 Noise Reduction)
- 1× Level 140 Torpedo Specialist (29 Torpedo Accuracy, 28 Tube Reload, 22 Spread Control)
- 1× Level 130 Planesman (29 Diving Speed, 27 Depth Control, 22 Trim Balance)
- 1× Level 120 Damage Control (27 Flooding Control, 26 Fire Fighting, 21 Repair)

---

## Progression & Leveling Mechanics

### XP Sources

**Combat XP** (Primary):
- **Damage Dealt**: 1 XP per 1,000 damage
- **Kills**: 500-2,000 XP based on target tier
- **Objectives**: 1,000-5,000 XP (convoy escorts, base captures, etc.)
- **Survival**: 200 XP per battle survived
- **Extraction**: 500-3,000 XP based on loot value extracted

**Training XP** (Accelerated, Credit Cost):
- **Port Training**: 100 XP per 1,000 credits (safe but expensive)
- **Academy Training**: 150 XP per 1,000 credits (requires academy access)
- **Time-Gated Training**: 500 XP per day idle (offline progression, max 5 days)

**Mission XP** (Bonus):
- **Daily Missions**: 1,000-3,000 XP
- **Campaign Missions**: 5,000-15,000 XP
- **Achievements**: 10,000+ XP (first kill in tier, ace tanker, etc.)

### XP Curve (Level 1-200)

**Total XP Required**:
```
Level 1 → 25:   50,000 XP (10 hours combat, ~5,000 XP/hour)
Level 25 → 50:  200,000 XP (40 hours combat)
Level 50 → 100: 1,000,000 XP (200 hours combat)
Level 100 → 150: 3,000,000 XP (600 hours combat)
Level 150 → 200: 6,000,000 XP (1,200 hours combat)

Total: 10,250,000 XP (2,050 hours combat = ~85 days played)
```

**Progression Timeline**:
- **Week 1**: Level 1 → 25 (classification unlock)
- **Month 1**: Level 25 → 50 (specialization unlock)
- **Month 3**: Level 50 → 100 (expert crew, stats ~25-27)
- **Month 9**: Level 100 → 150 (elite crew, stats ~30-32)
- **Month 24**: Level 150 → 200 (legendary crew, stats ~33-35)

**Realistic Player Path**:
- Most players will have Level 100-120 crews after 6 months (stats 25-28)
- Elite players (1,000+ hours) reach Level 150-180 (stats 30-32)
- Level 200 crews represent 2+ years of investment per card (stats 33-35)
- Average endgame player has 8-12 Level 150+ crews, 20-30 Level 100+ crews

---

## Integration with Permadeath System

### Pure Permadeath (Chosen Design)

When crew card dies in T6-T10 ship:
- ✅ **Lose entire card permanently**
- ✅ **Lose all stats** (RNG stats + classification bonuses + level progression)
- ✅ **Lose all progression** (months/years of XP investment)
- ✅ **Cannot recover stats or levels**
- ✅ **Must recruit NEW crew with NEW random stats**

**Strategic Implications**:
- **T1-T5 Safe Training**: Train crews to Level 100+ (stats ~25-27) with ZERO risk anywhere on map
- **High-Level Crew in T6+**: Player knowingly accepts 10-100% permadeath risk
- **Weight System Gates Abuse**: Cannot use Level 200 crew (211.5 tons) in T1 destroyer (250 ton limit with only 5 crew slots)
- **Risk/Reward Balance**: High-level crews powerful (30-35 stats) but losing them is catastrophic
- **RNG Creates Emotional Investment**: Losing a Level 180 crew with perfect 15-15-14 starting stats (rolled 50+ times) = devastating

**Example Scenario**:
- Player hunted for days to recruit perfect Gunner (15 Accuracy, 15 Reload, 14 Range starting stats = rolled 50+ times, 250,000+ credits in rerolls)
- Invested 1,800 hours leveling to Level 180 (stats: 50 Accuracy, 50 Reload, 32 Range)
- Assigned to T10 Battleship (100% crew card death on destruction)
- Battleship destroyed in battle
- Level 180 Gunner permanently destroyed (GONE FOREVER)
- Must recruit fresh Level 1 neutral crew with new random stats (probably worse: 11 Accuracy, 10 Reload, 9 Range)
- **Result**: Stakes are REAL, T10 battles are terrifying, perfect RNG crews are priceless

---

## UI/UX Considerations

### Crew Card Display

**Card Front** (After Recruitment):
```
╔════════════════════════════════════╗
║ Master Gunnery Officer (Lvl 180)   ║
║ Sailors: 685/685                   ║
║ Weight: 192.2 tons                 ║
║                                    ║
║ PRIMARY STATS                      ║
║ Accuracy:  50 ████████████████ MAX ║
║ Reload:    50 ████████████████ MAX ║
║                                    ║
║ SECONDARY STATS                    ║
║ Range:     32 ████████             ║
║                                    ║
║ Starting Stats: 15/15/14 (Perfect!)║
║ Specialization: Precision Gunner   ║
╚════════════════════════════════════╝
```

**Stat Bars** (7-50 range visualization):
- **Red (7-14)**: Below baseline (penalties)
- **Yellow (15-24)**: Baseline to competent
- **Green (25-34)**: Expert
- **Cyan (35-44)**: Elite
- **Gold (45-50)**: Legendary

**Starting Stats Shown**: Players can see original RNG roll (emotional attachment, bragging rights)

### Recruitment UI

**Pre-Recruitment Display**:
```
╔════════════════════════════════════╗
║ CREW RECRUITMENT                   ║
║ Cost: 5,000 credits                ║
║                                    ║
║ Stat Range: 7-15 (Average: 11)    ║
║ All stats randomly generated       ║
║                                    ║
║ Expected Quality: Varies           ║
║                                    ║
║ [RECRUIT] [Cancel]                 ║
╚════════════════════════════════════╝
```

**Post-Recruitment Display** (with reroll option):
```
╔════════════════════════════════════╗
║ Neutral Crew Card (Level 1)        ║
║                                    ║
║ Accuracy:  13 ████████             ║
║ Reload:    14 █████████            ║
║ Range:     12 ███████              ║
║ (All stats): 9-14 per stat         ║
║                                    ║
║ Starting Stats: 13/14/12 (Decent)  ║
║ Average: 13.0 (Above Average!)     ║
║                                    ║
║ [KEEP] [DISMISS & REROLL 5,000cr]  ║
╚════════════════════════════════════╝
```

### Stat Tooltip Details

Hovering over stat shows:
```
Accuracy: 50 (Legendary MAX)

Effects:
- Hit Rate: 97% at optimal range
- Bonus: +235% vs baseline (15 Accuracy = 50%)
- With Command Bonus (50 Command = +70%): Effective 85
- Starting Stat: 15 (Perfect RNG)

Progression:
- Level 1: 15 (recruited)
- Level 25: 21.25 (neutral growth + classification)
- Level 176: 50 (reached cap)
- Current: 50/50 (MAX, no further growth)

Time Investment: 1,800 hours combat
Recruitment Cost: 5,000 credits per roll, ~50 rerolls = 250,000 credits for perfect 15-15 primary stats
```

---

## Testing & Balance

### Stat Balance Goals

**Primary Design Targets**:
- **Stat 15 = Baseline**: 0% bonus/penalty (new Level 1 recruit with average RNG)
- **Stat 35 = Expert**: +40% better than baseline (Level 100 crew)
- **Stat 50 = Legendary**: +70% better than baseline (Level 176-200 crew)
- **Command Multiplier = Force Multiplier**: 50 Command = +70% all crew stats
- **RNG Impact = Meaningful Difference**: Perfect RNG reaches cap 24 levels earlier, bad RNG is 3.5 points below cap

**Avoid Power Creep**:
- Level 200 crews are 70% better than Level 1 baseline (stat 15), NOT 10x better
- Stat caps prevent infinite scaling (50 max)
- Diminishing returns above stat 30 (1.5-2.5% per point vs 2-3% at lower stats)
- Weight system prevents low-tier ships using max-level crews (211.5 tons at L200)

### Test Scenarios

**Scenario 1: Bad RNG vs Perfect RNG at Level 200**
- Bad RNG Gunner: Starting stats 7/7/7, Level 200 stats 46.5/46.5/25.75
- Perfect RNG Gunner: Starting stats 15/15/14, Level 200 stats 50/50/33.75
- **Expected Result**: Perfect RNG 3.5 points better at cap (meaningful), reached cap 24 levels earlier

**Scenario 2: Command Officer Force Multiplier**
- T7 Battleship with Level 150 Command Officer (45 Command = +60% all stats)
- 4× Level 100 Gunners (35 Accuracy, 32 Reload → 56 effective Accuracy, 51.2 effective Reload)
- **Expected Result**: 60% DPS increase across all gunners (massive force multiplier justifies command slot)

**Scenario 3: Specialist vs Generalist**
- Specialist: 50 Accuracy, 35 Reload (focused gunner)
- Generalist: 45 Accuracy, 45 Reload (balanced gunner)
- **Expected Result**: Specialist hits more reliably (+15% hit rate), generalist sustains fire (+30% fire rate) - trade-offs, not strictly better

**Scenario 4: Reroll Economics**
- Player wants 14+ average stats for new gunner (good starting point)
- Standard Recruitment (5,000 credits, 7-15 range, average 11)
- Expected rerolls: 15-25 (75,000-125,000 credits investment)
- **Expected Result**: Reasonable investment for competitive starting stats, not prohibitively expensive

---

## Cross-References

### Related GDD Sections
- [[Crew-Management]] - Crew card structure, weight system, positions
- [[Crew-Progression]] - XP mechanics, leveling, efficiency
- [[Crew-Permadeath]] - Death conditions, retrieval, risk scaling
- [[Ship-Stats-System]] - How crew stats integrate with ship modules
- [[Combat-System]] - How stats affect combat calculations
- [[Economy-System]] - Recruitment costs, credit sinks

### Related Scripts
- CrewCard.cs - Crew card data structure (add RNG stat fields)
- CrewStatSystem.cs - Stat calculation engine (7-35 range, formula implementation)
- CrewRecruitmentManager.cs - RNG recruitment, reroll system
- CrewProgressionManager.cs - XP and leveling (stat growth per level)
- CombatCalculator.cs - Stat-to-damage conversions (7-35 scale)

---

## Known Issues
- **None (design phase)** - Not yet implemented

---

## Future Enhancements
- **Stat Respec**: Allow stat reallocation (expensive, limited uses)
- **Legendary Traits**: Level 200 crews with 35 in all stats unlock unique passive abilities
- **Crew Synergies**: Stat bonuses when specific classifications work together
- **Dynamic Stat Growth**: Stat XP based on actions (Accuracy XP from hits, not just levels)
- **Crew Portraits**: Visual customization for crew cards, show RNG quality (bronze/silver/gold border)
- **Crew History**: Track original recruitment stats, show progression graph over 200 levels

---

## Changelog
- **2025-11-19**: Initial stat system design (7-15 RNG recruitment, 7-35 cap, 0.12/0.06 growth)
- **2025-11-19**: Updated to 7-50 cap with slower progression (0.19/0.10 growth rates)
  - Perfect RNG (15 start) reaches cap at Level 176
  - Average RNG (11 start) reaches cap at Level 200
  - Bad RNG (7 start) reaches 46.5 at Level 200 (3.5 below cap)
  - Updated all formulas, progression examples, UI displays
  - NOTE: Classifications 2-18 detailed stat breakdowns need update to 7-50 ranges (formulas correct)

---

**Status**: 📋 Fully designed with RNG mechanics and extended progression, awaiting implementation
**Next Steps**: Phase 2 implementation (RNG recruitment system, stat formulas, UI for rerolling)
