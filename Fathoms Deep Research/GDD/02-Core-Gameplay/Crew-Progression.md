---
tags: [planned, phase2, crew-management, progression, navy-field-inspired]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-17
---

# Crew Progression System

## Overview
The Crew Progression System governs how crew cards gain experience, level up, and improve performance over time. Built on Navy Field's proven progression mechanics, the system rewards both active combat participation and direct credit investment through paid training. Level matching creates efficiency curves that incentivize bringing appropriate-level crews to ships while preventing excessive over-leveling through weight constraints.

## Implementation Status
**Status**: 📋 PLANNED (designed but not implemented)
**Phase**: Phase 2 - Core Gameplay Systems
**Scripts**: TBD (pending implementation)
**Priority**: HIGH (core Phase 2 feature, critical to player retention)

---

## Design Specification

### Core Philosophy
Crew progression follows a **combat-primary advancement system** with supplementary paid training:
1. **Combat Experience**: Earned through battle participation (primary source, required)
2. **Paid Training**: Supplementary XP boost with credits (cannot replace combat, only enhance)

**Critical Rule**: Paid training can only provide up to **50% of any level's XP requirement**. The remaining 50% MUST come from combat experience. This ensures all crews have meaningful battle experience and prevents "buying" elite crews without actual gameplay.

**Key Design Pillars:**
- **Combat-Primary Progression**: Combat XP is mandatory, paid training is supplementary
- **50% Training Cap**: Paid training cannot exceed 50% of any level's XP
- **Exponential Cost Scaling**: Higher levels require significantly more investment
- **Level Matching Rewards**: Appropriate-level crews perform optimally
- **Over-Leveling Bonuses**: Higher-level crews provide efficiency bonuses (capped)
- **No Decay**: Crew XP/levels are permanent (unless crew dies)
- **Performance-Based XP**: Better combat performance = more XP earned

### Key Features
- **200-Level Cap**: Maximum crew level of 200 across all classifications
- **Four Level Brackets**: 1-50 (Basic), 51-100 (Intermediate), 101-150 (Advanced), 151-200 (Elite)
- **Efficiency Curve System**: Level matching affects module performance (35%-130% range)
- **Combat XP Scaling**: Higher-tier battles award more XP
- **Training Cost Progression**: Exponential credit cost increases
- **Casualty Impact**: Reduced sailor count = reduced efficiency
- **Battle Replenishment**: Pay to restore lost sailors

### User Experience
Players level crew cards through combat or paid training at ports. During battles, crew cards assigned to ship positions earn XP based on performance (damage dealt, kills, objectives). Lower-level crews operate modules at reduced efficiency, creating incentive to level up. Casualties during combat reduce crew efficiency until replenished at port for a credit cost.

**Progression Flow:**
1. Assign crew cards to ship positions before battle
2. Earn combat XP during battles (proportional to performance)
3. Return to port, optionally pay for training to boost XP
4. Level up crew cards when XP thresholds reached
5. Unlock classification choices at level thresholds (see [[Crew-Specialization]])
6. Manage efficiency through level matching with modules
7. Replenish casualties after battles to maintain full efficiency

### Crew Card Safety by Ship Tier

**CRITICAL DISTINCTION**: Crew cards face permadeath risk ONLY based on ship tier destroyed, NOT map location.

**T1-T5 Ships (Safe Tiers)**:
- 0% crew card permadeath risk
- Crew training is COMPLETELY SAFE on these ships
- Can operate ANYWHERE on the map without crew card loss risk
- Sailor casualties still occur (separate system, replaceable)
- **Recommended for**: All crew leveling activities, regardless of map location

**T6-T10 Ships (Permadeath Tiers)**:
- 10%-100% crew card permadeath risk (see [[Crew-Permadeath]])
- High-level crew cards at risk of permanent loss
- **Only use for**: End-game operations with elite crews where rewards justify risk

**Strategic Training Approach**:
- Train ALL crew cards to Level 200 in T1-T5 ships (zero permadeath risk)
- Can safely train in high-danger map areas using low-tier ships
- Location doesn't matter - only ship tier determines crew card permadeath risk
- Once crews are Level 200, transfer to T6+ ships only for critical missions

**Example**: Training a crew card from Level 1 → 200
- Use T1-T5 ships for entire journey (0% crew card permadeath)
- Can explore hostile territories, fight high-tier NPCs, loot valuable areas
- Ship tier determines XP gained, but all XP is safe (no crew card permadeath)
- Upon reaching Level 200, crew is ready for T6+ permadeath-tier operations

---

## Technical Implementation

### Current Implementation
**Not yet implemented** - This section is a design specification for Phase 2 development.

### Key Components

#### Experience & Leveling System

**XP Sources:**
1. **Combat Experience**:
   - Gain XP per battle based on performance
   - More XP for kills, damage dealt, objectives completed
   - Crew must be equipped on active ship during battle
   - XP awards scale with SHIP TIER used, NOT map location:
     - T1 ship earns T1 XP anywhere on map (Safe Waters or Hostile Waters)
     - T5 ship earns T5 XP anywhere on map
     - XP scaling: T1 (100 XP) < T3 (300 XP) < T5 (500 XP) < T10 (1500 XP)
     - Ship tier determines both XP gained AND permadeath risk

2. **Paid Training** (Supplementary Only):
   - Purchase additional XP at port training facilities
   - **50% Cap**: Can only provide up to 50% of each level's XP requirement
   - Remaining 50% MUST come from combat experience
   - Higher levels = exponentially higher training costs
   - Accelerates progression but cannot replace combat

**XP Award Calculation (Combat):**
```
Base XP = Battle Tier × Performance Multiplier × Time Multiplier

Performance Multiplier:
- 0.5x = Defeat/minimal contribution
- 1.0x = Standard participation
- 1.5x = High damage/kills
- 2.0x = MVP performance

Time Multiplier:
- Short battle (< 5 min): 0.8x
- Standard battle (5-15 min): 1.0x
- Long battle (15+ min): 1.2x

Example T5 Battle:
- Standard performance: 500 base XP × 1.0x = 500 XP
- High performance: 500 base XP × 1.5x = 750 XP
- MVP long battle: 500 base XP × 2.0x × 1.2x = 1,200 XP
```

**Paid Training Cost Formula:**
```
Training Cost (per 100 XP) = Base Cost × Level Bracket Multiplier × Level Modifier

Base Cost: 1,000 credits per 100 XP

Level Bracket Multipliers:
- Levels 1-50:   1.0x (Basic training - low cost)
- Levels 51-100: 2.5x (Intermediate training - medium cost)
- Levels 101-150: 6.0x (Advanced training - high cost)
- Levels 151-200: 15.0x (Elite training - extreme cost)

Level Modifier: 1.0 + (Current Level / 50)

Examples:
- Level 1 → 10: 1,000 × 1.0 × 1.02 = 1,020 credits per 100 XP
- Level 50 → 51: 1,000 × 1.0 × 2.0 = 2,000 credits per 100 XP
- Level 100 → 101: 1,000 × 2.5 × 3.0 = 7,500 credits per 100 XP
- Level 150 → 151: 1,000 × 6.0 × 4.0 = 24,000 credits per 100 XP
- Level 190 → 200: 1,000 × 15.0 × 4.8 = 72,000 credits per 100 XP
```

**Total XP Required (by Level):**
```
Level 1 → 50:   ~50,000 XP total (~1,000 XP per level)
Level 51 → 100:  ~250,000 XP total (~5,000 XP per level)
Level 101 → 150: ~750,000 XP total (~15,000 XP per level)
Level 151 → 200: ~2,000,000 XP total (~40,000 XP per level)

Total to reach Level 200: ~3,050,000 XP
```

#### Level Brackets & Progression Tiers

**Bracket 1: Basic Training (Levels 1-50)**
- **Duration**: 20-30 hours of active combat
- **Cost**: ~50M credits if fully paid-trained
- **Milestone**: Basic classification unlock at Level 25-30
- **Performance**: Suitable for T1-T3 ships
- **Strategic Use**: Initial crew development, trainer ships

**Bracket 2: Intermediate Training (Levels 51-100)**
- **Duration**: 60-80 hours of active combat
- **Cost**: ~200M credits if fully paid-trained
- **Milestone**: Advanced specialization unlock at Level 75-80
- **Performance**: Suitable for T4-T6 ships
- **Strategic Use**: Mid-tier ship operations, backup crews

**Bracket 3: Advanced Training (Levels 101-150)**
- **Duration**: 150-200 hours of active combat
- **Cost**: ~800M credits if fully paid-trained
- **Milestone**: Elite specialization unlock at Level 125-130
- **Performance**: Suitable for T7-T9 ships
- **Strategic Use**: High-tier operations, main ship crews

**Bracket 4: Elite Training (Levels 151-200)**
- **Duration**: 300-400 hours of active combat
- **Cost**: ~2,000M credits if fully paid-trained
- **Milestone**: Maximum mastery at Level 200
- **Performance**: Suitable for T9-T10 ships
- **Strategic Use**: Ultimate endgame investment, flagship crews

**Total Time Investment:**
- Level 1 → 200: ~500-700 hours of active combat (no paid training, slowest)
- Level 1 → 200: ~250-350 hours combat + ~1.5B credits (maximum paid training, fastest)
- **Realistic Mix**: 350-450 hours combat + 500M-800M credits for Level 200
- **NOTE**: Pure paid training impossible - minimum 50% of all XP must come from combat

#### Performance & Efficiency System

**Level Matching Mechanics:**
Each module/turret has a **recommended crew level** for 100% efficiency:
- Level 90 turret needs Level 90+ crew for full performance
- Lower level crew operates at reduced efficiency (penalty)
- Higher level crew provides efficiency **bonus** (capped)

**Efficiency Curve Formula:**
```
Efficiency = Base Efficiency × Level Match Factor × Casualty Factor

Level Match Factor:
- Crew Level < Module Level:
  Factor = 0.35 + (Crew Level / Module Level) × 0.65

- Crew Level = Module Level:
  Factor = 1.0 (100% efficiency)

- Crew Level > Module Level:
  Factor = 1.0 + min(0.30, (Crew Level - Module Level) / Module Level × 0.5)
  (Bonus capped at +30% efficiency)

Casualty Factor:
- Factor = Current Sailors / Max Sailors
- Linear scaling with sailor count

Examples (Level 90 Turret):
- Level 1 crew:   0.35 + (1/90) × 0.65 = 35.7% efficiency
- Level 45 crew:  0.35 + (45/90) × 0.65 = 67.5% efficiency
- Level 70 crew:  0.35 + (70/90) × 0.65 = 85.6% efficiency
- Level 90 crew:  100% efficiency (perfect match)
- Level 120 crew: 100% + min(30%, (30/90) × 50%) = 116.7% efficiency
- Level 200 crew: 100% + 30% = 130% efficiency (capped)
```

**Natural Balancing:**
Over-leveling is limited by weight constraints (see [[Crew-Management]]):
- Small ships can't support Level 200 crew (too heavy)
- Large ships benefit from veteran crew investments
- Creates progression incentive (bring crew to bigger ships)

**Efficiency Impact on Combat:**
```
Module Performance = Base Stats × Efficiency Factor

Example: Level 90 Main Battery Turret
- Base damage: 1,000 HP per shot
- Base reload: 20 seconds
- Base accuracy: 60%

With Level 1 Crew (35% efficiency):
- Damage: 350 HP per shot
- Reload: 57 seconds (20 / 0.35)
- Accuracy: 21%
- **Severely crippled performance**

With Level 90 Crew (100% efficiency):
- Damage: 1,000 HP per shot
- Reload: 20 seconds
- Accuracy: 60%
- **Optimal performance**

With Level 200 Crew (130% efficiency):
- Damage: 1,300 HP per shot
- Reload: 15.4 seconds (20 / 1.30)
- Accuracy: 78%
- **Enhanced performance**
```

#### Battle Casualties & Replenishment

**Casualty Mechanics During Combat:**
When ship takes damage, crew cards can lose individual sailors:
- Direct hits to crew positions cause casualties
- Fire/flooding kills crew over time
- Critical hits can devastate entire crew cards
- Casualty rate scales with damage severity

**Casualty Impact on Efficiency:**
```
Crew cards with reduced sailor counts perform worse:

Example: Level 20 Gunner (105 sailors at full strength)
- Full strength (105/105 sailors): 100% efficiency
- 60% casualties (42/105 sailors): 40% efficiency
- 75% casualties (26/105 sailors): 25% efficiency

Casualties reduce both effectiveness AND card weight proportionally
```

**Replenishment System:**
Lost sailors can be replaced at port:
- **Cost scales with crew card level**
- Higher level crew = more expensive to replenish per sailor
- Replenishment is instant (no waiting time)

**Replenishment Cost Formula:**
```
Cost per Sailor = Base Cost × Level Modifier

Base Cost: 50 credits per sailor
Level Modifier: 1.0 + (Level / 100)

Examples:
- Level 1 crew: 50 × 1.01 = 50.5 credits per sailor
- Level 20 crew: 50 × 1.20 = 60 credits per sailor
- Level 50 crew: 50 × 1.50 = 75 credits per sailor
- Level 100 crew: 50 × 2.00 = 100 credits per sailor
- Level 200 crew: 50 × 3.00 = 150 credits per sailor
```

**Example Replenishment Scenario:**
```
Level 100 Gunnery Officer (455 sailors max)
- Loses 68 sailors in battle (15% casualties)
- Remaining: 387 sailors (85% efficiency)
- Replenishment cost: 68 × 100 = 6,800 credits

Level 150 Master Engineer (605 sailors max)
- Loses 181 sailors in battle (30% casualties)
- Remaining: 424 sailors (70% efficiency)
- Replenishment cost: 181 × 125 = 22,625 credits
```

**Performance During Battle:**
Depleted crew cards operate at reduced efficiency until replenished:
- Level 100 card (455 sailors) reduced to 228 sailors = 50% efficiency
- Creates tactical decisions: retreat to replenish or continue weakened

**Strategic Considerations:**
- High casualties mid-mission force decision: continue at reduced efficiency or abort?
- Elite crew replenishment costs can be significant (Level 200 = 150 credits/sailor)
- Budget-conscious players may accept partial casualties to save credits
- Casualty management becomes part of economic strategy

### Configuration

**Tunable Parameters:**
```
// XP System
MAX_CREW_LEVEL = 200
BASE_XP_PER_LEVEL_L1_50 = 1000
BASE_XP_PER_LEVEL_L51_100 = 5000
BASE_XP_PER_LEVEL_L101_150 = 15000
BASE_XP_PER_LEVEL_L151_200 = 40000

// Combat XP Awards
T1_BATTLE_BASE_XP = 100
T3_BATTLE_BASE_XP = 300
T5_BATTLE_BASE_XP = 500
T7_BATTLE_BASE_XP = 800
T10_BATTLE_BASE_XP = 1500

// Training Costs
BASE_TRAINING_COST = 1000 credits per 100 XP
TRAINING_BRACKET_1_MULT = 1.0x (Levels 1-50)
TRAINING_BRACKET_2_MULT = 2.5x (Levels 51-100)
TRAINING_BRACKET_3_MULT = 6.0x (Levels 101-150)
TRAINING_BRACKET_4_MULT = 15.0x (Levels 151-200)
TRAINING_XP_CAP_PER_LEVEL = 0.50 (50% max - remaining must be combat XP)

// Efficiency System
MIN_EFFICIENCY = 0.35 (35% at Level 1 on high-level modules)
MAX_EFFICIENCY = 1.30 (130% bonus cap for over-leveling)
OVERLEVELING_BONUS_CAP = 0.30 (+30% maximum)

// Replenishment Costs
BASE_SAILOR_COST = 50 credits
SAILOR_COST_LEVEL_MODIFIER = 1.0 + (Level / 100)
```

---

## Integration Points

### Depends On
- [[Crew-Management]] - Base crew card system and structure
- [[Combat-System]] - XP awards during battles
- [[Port-Services]] - Training facilities and replenishment
- [[Economy-System]] - Credit costs for training and replenishment

### Used By
- [[Crew-Specialization]] - Level thresholds unlock classifications
- [[Crew-Permadeath]] - High-level crews represent massive investment at risk
- [[Ship-Modules]] - Efficiency affects module performance
- [[Player-Progression]] - Crew leveling is core progression loop

---

## Example Scenarios

### Scenario 1: Combat + Paid Training
**Captain Rodriguez levels a Gunner from 1 → 50**

**Option A: Pure Combat (Minimum Required)**
- Needs 50,000 total XP
- **Minimum 50% from combat**: 25,000 XP required from battles
- Plays T1-T3 battles averaging 300 XP per battle
- Requires ~84 battles minimum (combat portion only)
- Time investment: ~12-15 hours of gameplay minimum
- Credit cost: 0 (slowest but free)

**Option B: Combat + Maximum Paid Training (Fastest)**
- Needs 50,000 total XP
- **50% from combat**: 25,000 XP (~84 battles, 12-15 hours)
- **50% from training**: 25,000 XP (~255,000 credits)
- Time investment: 12-15 hours (half of pure combat)
- Credit cost: 255,000 credits
- **Fastest possible progression - cuts time in half**

**Option C: Combat + Partial Training (Balanced)**
- Plays 120 battles, earns 36,000 XP through combat (18 hours)
- Pays for remaining 14,000 XP at port (143,000 credits)
- Total: 18 hours + 143K credits
- **Most common approach - moderate time savings**

**NOTE**: Pure paid training is NOT possible. Combat experience is mandatory.

### Scenario 2: Efficiency Curve Impact
**Captain Tanaka operates Level 90 Heavy Cruiser**

**Scenario A: Under-Leveled Crew**
- Main turret requires Level 90 crew for 100% efficiency
- Currently has Level 45 Gunner assigned
- Efficiency: 67.5%
- Turret damage: 1,000 × 0.675 = **675 damage per shot**
- Reload time: 20 / 0.675 = **29.6 seconds**
- **Significantly handicapped in combat**

**Decision:** Invest 120,000 XP to level Gunner from 45 → 90
- Combat grinding: ~40 battles (6-8 hours)
- Paid training: ~900,000 credits
- **Result:** Full 1,000 damage, 20-second reload

**Scenario B: Over-Leveled Crew**
- Levels Gunner to 150 (overkill for Level 90 turret)
- Efficiency: 116.7% (capped bonus)
- Turret damage: 1,000 × 1.167 = **1,167 damage per shot**
- Reload time: 20 / 1.167 = **17.1 seconds**
- **+16.7% performance boost**

**Tradeoff:** Extra 60 levels (45M XP) = 300+ hours or 5M+ credits
- Marginal benefit (+16.7%) for massive investment
- Weight also increased significantly (455 → 605 sailors)
- **Only viable on large ships with weight capacity**

### Scenario 3: Casualty Recovery Decision
**Captain Lee's Battleship takes heavy damage**

**Initial State:**
- Main battery crew: Level 120 Gunner
- Started with 505 sailors (max for Level 120)
- Current efficiency: 100%

**After Prolonged Battle:**
- Down to 202 sailors (303 casualties = 60% loss)
- Current efficiency: 202/505 = **40%**
- Turret performance: Severely degraded

**Options:**
1. **Continue Mission at 40% Efficiency (Risky)**
   - Accept degraded combat capability
   - Risk further casualties or ship loss
   - Save replenishment credits

2. **Retreat to Port, Replenish (Safe)**
   - Pay 303 × 110 = **33,330 credits** to restore to 505 sailors
   - Return to 100% efficiency
   - Abort current mission rewards

3. **Extract with Cargo, Accept Reduced Capability**
   - Complete extraction objectives with 40% efficiency
   - Hope to survive return trip
   - Replenish after successful extraction

**Decision Factors:**
- Current cargo value vs. replenishment cost
- Mission importance and time investment
- Risk tolerance for further casualties
- Credit reserves available

### Scenario 4: Long-Term Investment
**Captain Müller builds elite crew roster over 1 year**

**Month 1-2: Basic Crews (Levels 1-50)**
- Creates 8 crew cards, levels to 50 through T1-T3 combat
- Time: 80 hours gameplay (combat required)
- Cost: 0 credits (no training used)
- Unlocks basic classifications

**Month 3-6: Intermediate Crews (Levels 51-100)**
- Levels 6 primary crews to 100 through T4-T6 combat + supplementary training
- Time: 100 hours gameplay (combat)
- Cost: ~200M credits (50% training supplement)
- Unlocks advanced specializations

**Month 7-10: Advanced Crews (Levels 101-150)**
- Focuses on 4 main crews for T7-T8 operations
- Time: 120 hours gameplay (combat)
- Cost: ~600M credits (50% training supplement)
- Unlocks elite specializations

**Month 11-12: Elite Crews (Levels 151-200)**
- Pushes 2 critical crews to 200 (main gunner, main engineer)
- Time: 80 hours gameplay (combat)
- Cost: ~700M credits (50% training supplement)
- Reaches maximum mastery

**Total Investment:**
- **Time:** 380 hours active gameplay (combat mandatory)
- **Credits:** ~1.5B total (supplementary training)
- **Result:** 2 Level 200 elite crews, 4 Level 150 advanced crews, 8 Level 50-100 backup crews
- **Strategic Value:** Can field optimal crews for T10 battleship with elite performance
- **NOTE:** Combat time cannot be reduced below ~380 hours - training only supplements, never replaces

---

## Known Issues
- **None (design phase)** - Not yet implemented

## Future Enhancements
- **Crew Training Missions**: Special PvE missions that award bonus XP for specific classifications
- **Mentor System**: High-level crews provide small XP bonus to lower-level crews in same ship
- **Combat Medals**: Crew cards earn medals for achievements (100 kills, 50 battles survived, etc.)
- **XP Boosts**: Consumable items or premium features for temporary XP bonuses
- **Crew Rest System**: Diminishing XP returns after extended play sessions (anti-grind mechanism)
- **Training Simulators**: Port facilities that reduce paid training costs

---

## Cross-References
- [[Crew-Management]] - Base crew card system, weight constraints, ship slots
- [[Crew-Specialization]] - Classification trees unlocked at level thresholds
- [[Crew-Permadeath]] - Risk of losing high-level crew investments
- [[Combat-System]] - XP awards and efficiency impact on battles
- [[Economy-System]] - Training costs and replenishment economics
- [[Port-Services]] - Training facilities and casualty replenishment

---

## Testing

### Test Coverage
- [ ] XP award calculation for various battle performances
- [ ] Paid training cost scaling across all level brackets
- [ ] Efficiency curve accuracy for level matching
- [ ] Casualty impact on efficiency
- [ ] Replenishment cost calculations
- [ ] Weight scaling with level increases
- [ ] Edge cases (Level 1 on Level 200 module, etc.)
- [ ] Long-term progression balance (1 → 200 time/cost)

### Test Results
Not yet implemented - testing pending Phase 2 development.

---

## Changelog
- **2025-11-17**: Initial design document created from GDD_Updated-1.md (lines 162-516)
