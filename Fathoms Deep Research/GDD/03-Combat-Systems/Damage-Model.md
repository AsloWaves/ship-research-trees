# Damage Model - Penetration, Critical Hits, and Module Damage

**Document Type**: Combat System Design
**Status**: 📋 PLANNED (Phase 2 Priority)
**Tags**: [planned, phase2, combat-systems, damage, penetration, critical-hits]
**Priority**: HIGH
**Last Updated**: 2025-01-17

---

## Document Purpose

This document details the comprehensive damage model for Fathoms Deep, covering armor penetration mechanics, critical hit systems, module-specific damage, crew casualties, fire and flooding systems, and progressive damage degradation.

---

## Core Damage Philosophy

Combat in Fathoms Deep balances **accessibility** (assisted targeting, clear feedback) with **mastery** (manual aiming, module optimization, tactical positioning). The hybrid damage model rewards both precision shooting (critical hits, module damage) and sustained pressure (HP attrition). Multi-domain warfare creates rock-paper-scissors dynamics where submarines threaten battleships, destroyers hunt submarines, and aircraft strike all surface vessels.

**Design Principles**:
- **Hybrid System**: HP pool + compartmentalized damage for depth
- **Skill Rewards**: Critical hits and module damage reward precision
- **Progressive Degradation**: Damaged systems reduce combat effectiveness
- **Tactical Feedback**: Visual and UI indicators show damage state
- **Extraction Stakes**: Damage accumulation threatens survival and loot

---

## Damage Model Architecture

### Hybrid System: HP Pool + Compartmentalized Damage

#### **Primary Health Pool**

**Core HP System**:
- Every ship has a **total HP value** based on class and tier
- HP represents overall structural integrity
- Reaching 0 HP = ship destruction
- HP visible to all players (yours and enemies)

**Typical HP Values by Ship Class**:
- **Destroyers**: 10,000-25,000 HP
- **Light Cruisers**: 25,000-40,000 HP
- **Heavy Cruisers**: 40,000-60,000 HP
- **Battleships**: 60,000-100,000 HP
- **Aircraft Carriers**: 50,000-80,000 HP
- **Submarines**: 5,000-15,000 HP

---

#### **Compartmentalized Damage Zones**

Ships divided into damage zones with individual integrity:

**Zone Distribution**:
1. **Bow Section** (10% of total HP) - Forward hull
2. **Forward Superstructure** (15% of total HP) - Bridge, forward modules
3. **Citadel/Amidships** (40% of total HP) - **CRITICAL ZONE** - Magazines, engines
4. **Aft Superstructure** (15% of total HP) - Rear modules, communications
5. **Stern Section** (10% of total HP) - Rear hull
6. **Underwater Hull** (10% of total HP) - Submarine/torpedo damage zone

---

### Damage Distribution Mechanics

**Dual Damage System**:
- Hits reduce **both** total HP and zone HP
- When zone HP depletes → zone "destroyed" → special effects
- Example: Bow destroyed → flooding, speed penalty

**Zone-Specific Damage Multipliers**:
- **Citadel hits** deal **1.5x damage** to total HP
- **Underwater hits** bypass armor, deal **2x flooding damage**
- **Superstructure hits** deal normal damage, high fire chance
- **Module direct hits** have critical hit chance

---

## Weapon Systems & Damage Types

### 1. Main Battery Guns

**Primary anti-ship weapons delivering precision long-range damage**

#### **Shell Types**

**Armor-Piercing (AP) Shells**:
- **Purpose**: Maximum penetration against heavily armored targets
- **Characteristics**:
  - High penetration, devastating citadels
  - Overpenetrates lightly armored ships (destroyers)
  - Best at medium-long range
- **Damage**: Full damage on penetration, 33% damage on overpenetration
- **Fire Chance**: 3-5%

**High-Explosive (HE) Shells**:
- **Purpose**: Reliable damage against all targets
- **Characteristics**:
  - Universal effectiveness
  - High fire chance (15-25%)
  - Cannot citadel penetration
- **Damage**: Consistent damage regardless of armor
- **Fire Chance**: 15-25%

**Semi-Armor-Piercing (SAP) Shells**:
- **Purpose**: Middle ground between AP and HE
- **Characteristics**:
  - No overpenetration mechanic
  - Moderate fire chance (8-12%)
  - Balanced damage
- **Damage**: Good against cruisers and battleships
- **Fire Chance**: 8-12%

---

### 2. Secondary Battery Guns

**Faster-firing support weapons**:
- **Reload**: 5-8 seconds
- **Range**: 5-8km
- **Auto-fire mode**: Available
- **Damage**: Lower per-shell, higher rate of fire
- **Use Case**: Anti-destroyer defense, sustained pressure

---

### 3. Anti-Aircraft (AA) Guns

**Defensive systems against aircraft**:
- **Automatic targeting**: Within AA range
- **AA Bubbles**: Three zones
  - **Long Range** (5-7km): Light damage
  - **Medium Range** (3-5km): Moderate damage
  - **Short Range** (0-3km): Heavy damage
- **Consumption**: AA shells auto-consumed from inventory (500+ rounds/stack)

---

### 4. Torpedoes

**Devastating underwater weapons**:
- **Damage**: 15,000-40,000 HP per torpedo
- **Characteristics**: Slow, visible, dodgeable
- **Limited ammo**: 6-16 per ship
- **Flooding**: 100% flood chance on hit
- **Module damage**: High chance of engine/rudder destruction

**Torpedo Types**:
- **Standard**: Unguided, straight-running
- **Long Lance** (Japanese): Extended range, higher damage
- **Acoustic Homing**: Tracks target propeller noise

---

### 5. Aircraft Ordnance

**AI-controlled squadrons with player-directed waypoint system**:

**Torpedo Bombers**:
- **Damage**: 25,000+ HP per torpedo
- **Flooding**: 100% chance
- **Module damage**: Critical systems vulnerable

**Dive Bombers**:
- **Damage**: 8,000-15,000 HP per bomb
- **Fire chance**: High (25-35%)
- **Precision**: Most accurate bomber type

**Level Bombers**:
- **Damage**: Heavy carpet bombing
- **Area effect**: Multiple hits possible
- **Less precise**: Lower accuracy than dive bombers

---

### 6. Depth Charges

**Anti-submarine warfare weapon**:
- **Deployment**: Dropped from stern or projected
- **Area-of-effect**: Spherical blast pattern
- **Damage scaling**:
  - **Direct hit**: Catastrophic damage (80-100% HP)
  - **Near miss (<50m)**: Heavy damage (40-60% HP)
  - **Proximity (<100m)**: Moderate damage (20-40% HP)
  - **Distant (<200m)**: Light damage (5-20% HP)

---

### 7. Naval Mines

**Area denial weapons**:
- **Types**: Contact, Magnetic, Acoustic
- **Damage**: 20,000-40,000 HP
- **Flooding**: 100% chance
- **Persistence**: Remain after deployment
- **Detection**: Visual, minesweeping, limited sonar

---

## Armor & Penetration System

### Armor Zones by Ship Type

#### **Battleship Example (T5 USS Iowa)**

**Armor Thickness**:
- **Belt Armor**: 12.1" (307mm) - Main side protection
- **Deck Armor**: 7.5" (190mm) - Top protection
- **Turret Face**: 17.0" (432mm) - Gun turret front
- **Superstructure**: 1.5" (38mm) - Light protection
- **Bow/Stern**: 0.75" (19mm) - Minimal protection

---

### Penetration Mechanics

**Penetration Calculation Formula**:
```
Shell Penetration Value vs. Armor Thickness = Outcome
```

**Penetration Outcomes**:

**Full Penetration** (Shell pen > Armor):
- **Result**: Full damage applied + citadel potential
- **Critical chance**: Base critical chance applies
- **Module damage**: Can destroy internal modules

**Partial Penetration** (Shell pen ≈ Armor):
- **Result**: 50% damage
- **Critical chance**: Reduced
- **Module damage**: Limited

**Non-Penetration / Bounce** (Shell pen < Armor):
- **Result**: 10% damage
- **Critical chance**: None
- **Visual**: Shell ricochets off armor

**Overpenetration** (Shell pen >>> Armor):
- **Result**: 33% damage (shell passes through without exploding)
- **Critical chance**: None
- **Common against**: Destroyers hit by battleship AP

---

### Angling Mechanics

**Armor Effectiveness Based on Impact Angle**:

**Auto-Bounce Angle**:
- **Impact >60°**: Automatic ricochet, 10% damage only
- **Impact 45-60°**: Reduced penetration chance
- **Impact 30-45°**: Moderate penetration reduction
- **Impact 0-30°**: Full penetration potential

**Effective Armor Thickness**:
- **Angled armor** counts as thicker
- **Example**: 300mm at 45° angle = effectively 424mm
- **Tactical depth**: "Angle your ship" to maximize armor

**Angling Examples**:
- **Bow-in**: Present minimal profile, maximum armor angle
- **Broadside**: Maximum firepower but vulnerable to penetration
- **Kiting away**: Rear aspect, good armor angles but reduced firepower

---

## Critical Hit System

### Critical Hit Mechanics

**Base Critical Chance**: 10%

**Critical Chance Modifiers**:
- **Citadel hits**: +15% critical chance
- **Manual targeting**: +25% critical chance
- **Module direct hits**: +10% critical chance
- **Gunner Accuracy stat**: +0% at stat 15 (baseline), up to +35% at stat 50 (legendary)

**Critical Hit Effects**:
- **1.5x damage multiplier**
- **Guaranteed status effect** (fire, flooding, module damage)
- **Instant module destruction** (if module hit directly)
- **Visual feedback**: Larger explosion, special effects

---

### Magazine Detonation

**Catastrophic Critical Hit**:
- **Trigger**: Citadel penetration with 5% detonation chance
- **Result**: Instant ship destruction
- **No counterplay**: Cannot be repaired
- **Prevention**: Magazine flooding consumable (reduces to 1% chance)

**Historical Examples**:
- HMS Hood vs KMS Bismarck: Magazine detonation from plunging fire
- HMS Barham: Catastrophic explosion from submarine torpedo

---

## Module Damage & Critical Hits

### Damageable Modules

#### **Main Battery Turrets**

**Damage States**:
1. **Fully Operational** (100% HP): Maximum rate of fire, full accuracy
2. **Light Damage** (75% HP): Reduced rate of fire (-15%), slight accuracy penalty (-5%)
3. **Moderate Damage** (50% HP): Significant rate reduction (-30%), notable accuracy loss (-15%)
4. **Heavy Damage** (25% HP): Single gun operation only, poor accuracy (-30%)
5. **Destroyed** (0% HP): Turret completely non-functional

**Combat Repair**:
- **Repair time**: 45 seconds (baseline Repair Speed stat 15), reduced to ~18 seconds with Repair Speed 50
- **Restored capacity**: 50% functionality
- **Requires**: Damage control party available

**Critical Hit Chance**: 15% when hit directly

---

#### **Engine/Propulsion System**

**Damage States**:
- **100% HP**: Full speed
- **75% HP**: -10% speed
- **50% HP**: -25% speed
- **25% HP**: -50% speed
- **0% HP**: Dead in water (0 knots)

**Combat Repair**:
- **Repair time**: 60 seconds (baseline Repair Speed stat 15), reduced to ~24 seconds with Repair Speed 50
- **Restored capacity**: 50% speed restoration
- **Tactical impact**: Vulnerable during repair

---

#### **Rudder/Steering System**

**Damage States**:
- **100% HP**: Normal turning radius
- **75% HP**: +20% turning radius
- **50% HP**: +50% turning radius
- **25% HP**: +100% turning radius
- **0% HP**: Stuck in turn (cannot change course)

**Combat Repair**:
- **Repair time**: 30 seconds (baseline Repair Speed stat 15), reduced to ~12 seconds with Repair Speed 50
- **Restored capacity**: 70% restoration

---

#### **Fire Control System**

**Damage States**:
- **100% HP**: Full accuracy
- **50% HP**: -30% accuracy penalty
- **0% HP**: Manual aiming only, no fire control computer

**Combat Repair**:
- **Repair time**: 15 seconds (baseline Repair Speed stat 15), reduced to ~6 seconds with Repair Speed 50
- **Restored capacity**: Full restoration

---

#### **Radar/Sonar Systems**

**Damage States**:
- **100% HP**: Full detection range
- **50% HP**: -50% detection range
- **0% HP**: Visual detection only (no radar/sonar)

**Combat Repair**:
- **Repair time**: 10 seconds (baseline Repair Speed stat 15), reduced to ~4 seconds with Repair Speed 50
- **Restored capacity**: Full restoration

**Tactical Impact**:
- Cannot detect submarines without sonar
- Reduced situational awareness
- Vulnerable to stealth attacks

---

## Fire & Flooding Mechanics

### Fire System

**Fire Initiation**:
- **HE shells**: 15-25% fire chance per hit
- **Aircraft rockets**: 20-30% fire chance
- **Secondary batteries**: 10-15% fire chance

**Fire Characteristics**:
- **Maximum fires**: Up to 4 simultaneous fires
- **Damage rate**: 0.3% max HP per second per fire
- **Duration**: 60 seconds if not extinguished
- **Total damage**: 18% max HP per fire over full duration

**Fire Locations**:
1. **Bow fire**
2. **Forward superstructure fire**
3. **Amidships fire**
4. **Aft superstructure fire**

**Fire Management**:
- **Damage Control Party**: Instant extinguish, 90-second cooldown (baseline Fire Fighting stat 15), reduced to ~36 seconds with Fire Fighting 50
- **Fire Fighting stat effectiveness**: Stat 7 (-25% slower extinguishing), stat 15 (baseline), stat 50 (+105% faster extinguishing)
- **Passive burn**: Fires extinguish naturally after 60 seconds
- **Multiple fires**: Strategic decision - which fire to extinguish first?

---

### Flooding System

**Flood Initiation**:
- **Torpedo hits**: 100% flood chance
- **Underwater shell hits**: 50% flood chance
- **Mine hits**: 100% flood chance
- **Ram damage**: 75% flood chance

**Flood Severity Levels**:

**Light Flooding**:
- **Damage rate**: 0.5% max HP per second
- **Duration**: 90 seconds
- **Total damage**: 45% max HP over full duration

**Heavy Flooding**:
- **Damage rate**: 1.0% max HP per second
- **Duration**: 120 seconds
- **Total damage**: 120% max HP (lethal if not repaired)

**Catastrophic Flooding**:
- **Damage rate**: 2.0% max HP per second
- **Duration**: Continuous until repaired
- **Result**: Rapid sinking

**Flooding Characteristics**:
- **Maximum floods**: Up to 2 simultaneous floods
- **Speed penalty**: -10% speed per flood
- **List/Heel**: Visual ship listing to damaged side

**Flood Management**:
- **Damage Control Party**: Reduces flood damage by 50% (baseline Flooding Control stat 15), up to 78% with Flooding Control 50, 90-second cooldown (baseline stat 15), reduced to ~36 seconds with stat 50
- **Flooding Control stat effectiveness**: Stat 7 (-25% slower mitigation), stat 15 (baseline 50% reduction), stat 50 (+105% faster mitigation, 78% damage reduction)
- **Emergency repairs**: Temporary fix, requires port for full repair
- **Counter-flooding**: Equalize ship balance, accepts additional water

---

### Strategic Fire/Flood Trade-off

**Single Damage Control Party**:
- **Must choose**: Address fire OR flooding
- **Cannot do both**: Same consumable for both hazards
- **Tactical decision**: Which threat is more immediate?

**Example Scenario**:
Ship suffering from 3 fires (54% HP damage potential) and 1 heavy flood (120% HP damage potential). Must prioritize flood to prevent sinking, accept fire damage.

---

## Crew Casualties & Personnel Management

### Crew Status Categories

**Combat Effectiveness by Casualty Level**:

**Combat Ready** (0-10% casualties):
- **Effectiveness**: 100%
- **Penalties**: None
- **Morale**: High

**Light Casualties** (10-25% casualties):
- **Effectiveness**: 85-90%
- **Penalties**: Minor reload speed reduction (-5%)
- **Morale**: Moderate

**Heavy Casualties** (25-50% casualties):
- **Effectiveness**: 60-75%
- **Penalties**:
  - Significant reload speed reduction (-15%)
  - Accuracy penalty (-10%)
  - Repair speed reduction (-20%)
- **Morale**: Low

**Critical Casualties** (50%+ casualties):
- **Effectiveness**: 40-50%
- **Penalties**:
  - Major reload speed reduction (-30%)
  - Severe accuracy penalty (-25%)
  - Repair speed reduction (-40%)
  - Module functionality degraded
- **Morale**: Very low, risk of crew panic

---

### Crew Reassignment Under Fire

**Dynamic Crew Management**:
- **Destroyed modules**: Crew survivors reassigned to functional systems
- **Mixed crew effectiveness**: Combined crews operate at reduced efficiency
- **Repair priorities**: Player assigns crew to critical repairs
- **Medical treatment**: Medical bay modules accelerate crew recovery

**Example: USS Atlanta After Air Attack**:
**Initial State**: 40% crew casualties, 6 gun mounts damaged

**Crew Reallocation**:
1. **Damage Assessment**: 8x5-inch guns operational, 4x5-inch guns destroyed
2. **Crew Reallocation**: Survivors from destroyed mounts → remaining guns
3. **Effectiveness Impact**: Remaining guns operate at 85% efficiency (mixed crews)
4. **Repair Priority**: Engineering crew assigned to restore power before guns
5. **Combat Capability**: Ship retains 60% of original firepower with reduced accuracy

---

## Targeting & Fire Control Systems

### Mode 1: Assisted Targeting (Default)

**Player-Friendly Fire Control**:
- **Lead indicator**: Game displays predicted impact point
- **Target tracking**: Automatic shell travel time calculation
- **Accuracy**: 70% base hit rate
- **Modifiers**: Affected by crew skill, modules, range, weather
- **Best for**: New players, multi-tasking

---

### Mode 2: Auto Targeting

**AI-Assisted Fire Control**:
- **Requirements**: "Auto Fire Control" module installed
- **Function**: Ship automatically aims and fires
- **Accuracy**: 60% base (lower than assisted)
- **Multi-target**: Can engage multiple targets if module supports
- **Best for**: Managing carriers, multi-ship fleet operations

---

### Mode 3: Manual Targeting (Advanced)

**Skill-Based Fire Control**:
- **Requirements**: "Manual Fire Director" module
- **Function**: No lead indicators, pure player skill
- **Accuracy bonus**: +15% base accuracy
- **Critical bonus**: +25% critical hit chance
- **Best for**: Veteran players, competitive play, maximum damage output

**Skill Requirements**:
- Calculate shell travel time
- Predict target movement
- Account for ship motion and weather
- Manual range adjustment

---

### Fire Control Module Progression

**Technology Tiers**:
- **Tier 1 (Basic)**: +5% accuracy
- **Tier 2 (Improved)**: +10% accuracy
- **Tier 3 (Advanced)**: +15% accuracy, unlocks manual targeting
- **Tier 4 (Electronic)**: +20% accuracy, improved auto-target
- **Tier 5 (Radar FCS)**: +25% accuracy, beyond visual range targeting

---

## Visual & Audio Feedback Systems

### Visual Damage Feedback

**Hit Indicators**:
- **Shell splashes**: Show near misses, help adjust aim
- **Hit markers**: Indicate successful strikes
- **Penetration indicators**: Show armor penetration success
- **Critical hit effects**: Larger explosions, special visual effects

**Damage State Visualization**:
- **Turrets**: Visibly destroyed when disabled
- **Smoke**: Damaged modules emit smoke
- **Fire effects**: Animated flames on burning sections
- **Flooding**: Ship lists to damaged side
- **Hull breaches**: Visible damage to ship structure

---

### Audio Damage Feedback

**Combat Sounds**:
- **Shell impacts**: Varying intensity based on damage
- **Explosion sounds**: Scaled to damage severity
- **Crew voice lines**: Report critical events
  - "Fire in engineering!"
  - "Flooding in the bow section!"
  - "Turret destroyed!"
  - "We're taking on water!"

**Warning Systems**:
- **Klaxons**: Flooding/fire warnings
- **Damage alarms**: Module destruction alerts
- **Low HP warning**: Critical damage threshold

---

### UI Damage Display

**Primary Indicators**:
- **HP bar**: Shows total ship health with color coding
  - Green: 70-100% HP
  - Yellow: 40-69% HP
  - Orange: 20-39% HP
  - Red: 0-19% HP
- **Module status indicators**: Show individual module health
- **Fire/flood counters**: Display active hazards
- **Ammunition counters**: Remaining shells per battery
- **Resource gauges**: Fuel, battery, air (submarines)

**Detailed Damage Display**:
- **Ship cross-section view**: Shows compartment damage
- **Module health percentages**: Exact damage values
- **Repair timers**: Countdown for active repairs
- **Crew status**: Casualty count and effectiveness

---

## Environmental Combat Factors

### Weather Impact on Combat

**Combat Effectiveness Modifiers**:

**Calm Seas**:
- **Accuracy**: +15% bonus
- **Fire control**: Stable platform
- **Visibility**: Maximum

**Moderate Seas**:
- **Accuracy**: Standard
- **Fire control**: Slight rolling, timing affected
- **Visibility**: Good

**Rough Seas**:
- **Accuracy**: -25% penalty
- **Fire control**: Severe gun platform movement
- **Visibility**: Reduced
- **Flooding risk**: Increased damage from hits

**Storm Conditions**:
- **Accuracy**: -40% penalty
- **Fire control**: Extreme difficulty
- **Visibility**: 2-5km maximum
- **Flooding risk**: Significantly increased

**Night Combat**:
- **Accuracy**: -30% penalty without radar
- **Visual detection**: Severely limited
- **Radar advantage**: Ships with radar have major edge
- **Fire illumination**: Muzzle flashes reveal positions

---

## Permadeath & Damage Persistence

### Tier-Based Death Penalties

**T1-T5** (Safe Learning Tiers):
- **Ship Permadeath**: 0% (ships ALWAYS recovered)
- **Crew Card Permadeath**: 0% (crew cards ALWAYS safe)
- **Sailor Casualties**: Variable based on damage (replaceable at ports)
- **Module Damage**: 0-40% module damage on recovery
- **Cargo Loss**: Partial to significant inventory loss
- **Purpose**: Safe environment for learning mechanics anywhere on map

**T6** (First Permadeath Tier):
- **Ship Permadeath**: 10% permanent destruction
- **Crew Card Permadeath**: 10% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Damage**: 40-50% module damage, expensive repairs
- **Cargo Loss**: Full inventory loss

**T7** (Escalating Risk):
- **Ship Permadeath**: 20% permanent destruction
- **Crew Card Permadeath**: 20% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Damage**: 50-60% module damage
- **Cargo Loss**: Full inventory loss

**T8** (High Stakes):
- **Ship Permadeath**: 40% permanent destruction
- **Crew Card Permadeath**: 40% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Damage**: 60-70% module damage
- **Cargo Loss**: Full inventory loss + high module loss risk

**T9** (Extreme Risk):
- **Ship Permadeath**: 60% permanent destruction
- **Crew Card Permadeath**: 60% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Damage**: 70-90% module damage
- **Cargo Loss**: Full inventory loss + very high module loss risk

**T10** (Absolute Permadeath):
- **Ship Permadeath**: 100% GUARANTEED permanent destruction
- **Crew Card Permadeath**: 100% ALL crew cards permanently destroyed
- **Sailor Casualties**: 100% (irrelevant since all cards destroyed)
- **Module Damage**: 100% - all modules permanently lost
- **Cargo Loss**: Everything permanently lost (no recovery)

---

## Damage Model Balancing

### Fair Combat Principles

**Player vs Player**:
- **Same damage models**: All players use identical systems
- **No artificial advantages**: No stat boosts or handicaps
- **Tier matchmaking**: Prevents seal clubbing
- **Skill-based**: Precision and tactics determine outcomes

**Player vs NPC**:
- **NPCs use player systems**: Identical damage calculations
- **Difficulty through tactics**: AI improves through better positioning and coordination
- **Learnable patterns**: Players can study and counter AI behaviors
- **Consistent damage**: No hidden multipliers or cheats

---

## Cross-Reference Documents

**Related Combat Systems**:
- [Combat-Overview.md](Combat-Overview.md) - Multi-domain warfare philosophy
- [Surface-Combat.md](Surface-Combat.md) - Gunnery and ballistics application
- [Carrier-Operations.md](Carrier-Operations.md) - Aircraft damage mechanics
- [Submarine-Warfare.md](Submarine-Warfare.md) - Underwater damage systems

**Related Game Systems**:
- Module Customization System (GDD Core) - Damage control modules
- Crew Training System (GDD Core) - Crew casualties and management
- Permadeath System (GDD Core) - Death penalties and recovery
- Extraction System (GDD Core) - Damaged ship extraction challenges

---

## Implementation Priority

**Phase 2 Development Focus**:

**Priority 1 - Core Damage System**:
1. HP pool and compartmentalized damage
2. Armor penetration mechanics
3. Module damage and degradation
4. Basic fire and flooding systems

**Priority 2 - Critical Hits & Feedback**:
5. Critical hit system implementation
6. Visual damage feedback (fires, smoke, damage states)
7. Audio feedback (explosions, warnings, crew voice lines)
8. UI damage indicators

**Priority 3 - Advanced Systems**:
9. Crew casualty and reassignment systems
10. Weather impact on combat
11. Progressive damage degradation
12. Environmental hazards

**Critical Success Factors**:
- Clear visual and audio feedback for all damage events
- Meaningful consequences for taking damage
- Tactical depth through module targeting
- Accessible to new players, rewarding for veterans
- Extraction tension created by accumulated damage
- Fair and consistent damage calculations across all scenarios

---

This comprehensive damage model creates deep, engaging combat where every hit matters, module damage creates tactical opportunities, and the threat of destruction drives extraction-based decision-making across all tiers of gameplay.
