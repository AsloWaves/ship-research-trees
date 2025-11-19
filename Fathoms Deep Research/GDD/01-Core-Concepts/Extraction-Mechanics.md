---
tags: [planned, design, core-concepts]
status: 📋 PLANNED
phase: Vision/Foundation
priority: HIGH
last-updated: 2025-11-17
---

# Extraction Mechanics

## Overview
The extraction mechanic is the core gameplay loop of Fathoms Deep, defining how players venture into dangerous waters, acquire valuable resources through combat or collection, and must successfully return to friendly ports to secure their gains. This document outlines the "Hunt, Fight, Extract, Survive" cycle that drives all player decision-making.

## Implementation Status
**Status**: 📋 PLANNED - Core gameplay loop design
**Phase**: Vision/Foundation
**Priority**: HIGH - Foundational to entire game design

---

## Core Extraction Loop

### The Five-Phase Cycle

#### Phase 1: Outfitting (At Friendly Port)
**Objective**: Prepare ship for expedition with limited resources

**Player Activities:**
- Load ammunition into ship inventory (grid)
- Fuel ship for journey into ship inventory (grid)
- Select crew assignments and specialists (All modules need crew cards to work, some are critical for leaving port, others are not critical)
- Install or swap modules based on mission objectives()
- Purchase Consumables (repair materials, medical supplies, etc.)
- Review intelligence on target areas (Recent reports on resources and enemy activity)

**Key Decisions:**
- **Ammunition variety vs. quantity**: Bring AP for armored targets or HE for general combat?
- **Fuel range**: Enough for quick extraction or extended hunting?
- **Cargo space**: Leave room for valuable loot or maximize combat capability?
- **Insurance**: Purchase coverage for higher-tier expeditions?
- **Route planning**: Safe but long paths or dangerous shortcuts?

**Emotional State**: Anticipation and strategic planning

**Design Philosophy**: This phase should feel like preparation for a mission, not a chore. Players are making meaningful trade-offs with limited ship space and economic resources.

---

#### Phase 2: Hunting (En Route and On Station)
**Objective**: Navigate to target area and identify valuable opportunities

**Player Activities:**
- Navigate through contested waters toward objectives
- Monitor radar and visual contacts
- Assess potential targets (cargo indicators, ship tier, damage state)
- Evade or engage hostile encounters
- Search for resource extraction points (shipwrecks, supply convoys)
- Scout enemy positions and fleet movements

**Threat Sources:**
- **Enemy players**: Hostile nation ships or pirates hunting laden vessels
- **NPC patrols**: AI-controlled ships protecting their waters
- **Environmental hazards**: Storms, minefields, shallow waters
- **Fuel/ammunition depletion**: Resource management pressure
- **Time pressure**: Longer hunting increases risk exposure

**Key Decisions:**
- **Target selection**: Attack damaged ship vs. wait for better opportunity?
- **Risk tolerance**: Engage superior force for high-value cargo?
- **Zone depth**: Penetrate deeper into hostile territory for better loot?
- **Opportunistic aggression**: Break peace treaty for valuable target?
- **Resource conservation**: Fight now or save ammunition for extraction?

**Emotional State**: Building tension and opportunity assessment

**Design Philosophy**: Hunting phase should create tactical dilemmas. Every contact is a potential threat or opportunity. Radar/visual mechanics create "fog of war" where players must make decisions with incomplete information.

---

#### Phase 3: Combat (Engagement)
**Objective**: Defeat enemies or secure resources through PvPvE combat

**Player Activities:**
- Execute tactical maneuvers (positioning, speed control, evasion)
- Manage ammunition selection and fire control
- Coordinate multi-domain warfare (surface, air, submarine)
- Direct crew to damage control and repair priorities
- Assess loot on destroyed/disabled enemies
- Defend against counter-attacks from reinforcements

**Combat Outcomes:**
- **Total Victory**: Enemy destroyed, full cargo salvage opportunity
- **Partial Victory**: Enemy disabled/retreating, limited salvage time
- **Pyrrhic Victory**: Win but with heavy damage/casualties
- **Tactical Withdrawal**: Disengage before destruction
- **Defeat**: Ship disabled, crew evacuates, permadeath check

**Loot Acquisition:**
- **Ship modules**: Turrets, engines, fire control systems (high value)
- **Resources**: Chromium, steel, rare materials (trade goods)
- **Ammunition**: Salvage unfired rounds from enemy Inventory
- **Crew**: Rescue enemy crew as prisoners (ransom/recruitment)
- **Intelligence**: Maps, codes, tactical data (reputation rewards)

**Key Decisions:**
- **Engagement commitment**: All-in attack or probing strikes?
- **Loot priority**: High-value modules vs. quick bulk resources?
- **Salvage time**: How long to loot before enemies respond?
- **Damage threshold**: Continue fighting or abort with current cargo?
- **Crew risk**: Expose crew to danger for better loot access?

**Emotional State**: Adrenaline, tactical focus, and growing stakes

**Design Philosophy**: Combat should be decisive but not instant. Time-to-kill allows for tactical repositioning. Loot acquisition during combat creates tension (stay to loot vs. flee while alive).

---

#### Phase 4: Extraction (Return Journey)
**Objective**: Successfully return to friendly port with cargo intact

**Threat Escalation:**
- **Pursuers**: Enemies following damaged ship seeking revenge/loot
- **Ambushers**: Players camping extraction routes
- **System failures**: Damaged engines reducing speed, fires spreading
- **Crew casualties**: Reduced combat effectiveness if attacked
- **Fuel shortage**: May not reach closest safe port
- **Cargo vulnerability**: Loot containers can be destroyed by combat damage

**Player Activities:**
- Navigate toward nearest friendly port (often different from departure)
- Manage damaged systems and crew injuries
- Evade or fight pursuing enemies
- Request squadron assistance if available
- Make emergency repairs with limited supplies
- Calculate fuel range and alternative safe harbors

**Key Decisions:**
- **Route selection**: Fastest path (dangerous) vs. safest path (slower)?
- **Engagement avoidance**: Fight or flee when intercepted?
- **Repair priorities**: Fix engines for speed or weapons for defense?
- **Port destination**: Close but minor port vs. distant major port?
- **Cargo jettison**: Dump low-value loot to gain speed?
- **Distress calls**: Call for help and split loot vs. solo extraction?

**Critical Scenarios:**

**Scenario A: Clean Extraction**
- No pursuers, minimal damage
- Direct route to friendly port
- Low tension, high satisfaction
- **Success rate**: ~60% of expeditions

**Scenario B: Damaged Extraction**
- Significant damage, reduced speed
- Potential pursuers detecting weakness
- Must evade or fight with compromised ship
- **Success rate**: ~30% of expeditions

**Scenario C: Desperate Extraction**
- Critical damage, crew casualties
- Active pursuit by hostile forces
- May require jettisoning cargo to survive
- Emergency repairs during flight
- **Success rate**: ~10% of expeditions (but creates best stories)

**Emotional State**: Maximum tension and anxiety

**Design Philosophy**: Extraction is where stakes culminate. Nothing is secured until port docking. Even dominant victories can turn into defeats during extraction. This phase creates the "relief" half of the tension/release cycle.

---

#### Phase 5: Progression (At Friendly Port)
**Objective**: Secure gains and prepare for next expedition

**Player Activities:**
- Dock at friendly port (cargo secured permanently)
- Sell loot on player market or to NPCs
- Repair ship damage and heal crew
- Upgrade modules with acquired resources
- Advance crew skills and specializations
- Purchase better equipment for next expedition
- Review performance statistics and reputation changes

**Progression Dimensions:**
- **Economic**: Bank balance increases, market investments
- **Ship advancement**: Unlock higher tier vessels or modules
- **Crew development**: Skill points, specialization unlocks
- **Reputation**: Nation standing improves/declines based on actions
- **Knowledge**: Learn from mistakes and successes

**Loot Liquidation:**
- **Immediate sale**: Quick cash at NPC prices (safe but lower value)
- **Market listing**: Higher prices but may take time to sell
- **Module installation**: Keep valuable equipment for personal use
- **Squadron sharing**: Distribute loot among fleet members
- **Long-term investment**: Hold rare materials for price speculation

**Key Decisions:**
- **Reinvestment**: Upgrade current ship or save for higher tier?
- **Risk level**: Return to same tier or push to higher stakes?
- **Economic strategy**: Cash out or hold for better market prices?
- **Crew advancement**: Generalist skills or specialized expertise?
- **Next objective**: Repeat successful strategy or try new approach?

**Emotional State**: Relief, satisfaction, and planning excitement

**Design Philosophy**: This phase delivers the "payoff" for successful extraction. Progression should feel earned and meaningful. Losses during extraction make this moment especially satisfying when achieved.

---

## Extraction Stakes & Consequences

### What You Risk on Every Expedition

#### Always At Risk (All Tiers)
1. **Cargo and Loot**: Valuable items not secured until port arrival
2. **Ammunition Expenditure**: Fired rounds are permanently consumed
3. **Fuel Consumption**: Must reach port or be stranded
4. **Repair Costs**: Damage must be repaid even if extraction succeeds
5. **Time Investment**: Failed expeditions yield no progression
6. **Reputation**: Aggressive actions create diplomatic consequences

#### Tier-Based Escalating Risks

**Tiers 1-5: Protected Learning Zone**
- **Ship Permadeath**: 0% (ships ALWAYS recovered, guaranteed safety)
- **Crew Card Permadeath**: 0% (crew cards ALWAYS safe, no permanent loss)
- **Sailor Casualties**: Variable based on damage (replaceable at ports for credits)
- **Module Damage**: Escalating risk (10-40% chance of destroyed modules)
- **Cargo Loss**: Always at risk if ship destroyed
- **Purpose**: Safe environment for learning mechanics and training crew cards
- **Key Insight**: T1-T5 ships can explore ANYWHERE on the map with zero permadeath risk

**Tier 6: First Permadeath Risk**
- **Ship Permadeath**: 10% permanent destruction (no recovery if failed)
- **Crew Card Permadeath**: 10% per card (independent rolls, permanent loss of officer + all levels)
- **Sailor Casualties**: Variable based on damage (replaceable at ports)
- **Module Destruction**: 50% loss chance (modified by damage type/caliber)
- **Cargo Loss**: Always at risk
- **Insurance Available**: 30,000 credits (reduces 10% → 5%)
- **Purpose**: First real stakes, psychological barrier for players

**Tier 7: Escalating Risk**
- **Ship Permadeath**: 20% permanent destruction
- **Crew Card Permadeath**: 20% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Destruction**: 55% loss chance
- **Cargo Loss**: Always at risk
- **Insurance Available**: 50,000 credits (reduces 20% → 10%)
- **Purpose**: Moderate risk/reward balance for mid-tier operations

**Tier 8: High Stakes**
- **Ship Permadeath**: 40% permanent destruction
- **Crew Card Permadeath**: 40% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Destruction**: 60% loss chance
- **Cargo Loss**: Always at risk
- **Insurance Available**: 150,000 credits (reduces 40% → 25%)
- **Purpose**: Substantial risk for veteran players, backup ships essential

**Tier 9: Extreme Risk**
- **Ship Permadeath**: 60% permanent destruction
- **Crew Card Permadeath**: 60% per card (independent rolls)
- **Sailor Casualties**: Variable based on damage (replaceable)
- **Module Destruction**: 70% loss chance
- **Cargo Loss**: Always at risk
- **Insurance Available**: 300,000 credits (reduces 60% → 40%)
- **Purpose**: Very high stakes, only for experienced players with strong risk management

**Tier 10: Absolute Permadeath**
- **Ship Permadeath**: 100% GUARANTEED permanent destruction
- **Crew Card Permadeath**: 100% ALL crew cards destroyed (no exceptions)
- **Sailor Casualties**: 100% (irrelevant since all cards destroyed)
- **Module Destruction**: 100% all modules permanently lost
- **Cargo Loss**: Always at risk
- **Insurance Available**: 1,000,000+ credits (reduces 100% → 70%)
- **No Recovery**: ABSOLUTE TOTAL LOSS - bring only expendable ships/crews
- **Purpose**: Ultimate stakes for server-defining accomplishments

### Three Separate Loss Mechanics Explained

**Critical Understanding**: There are THREE independent loss systems that all activate when your ship is destroyed:

**1. Ship Permadeath (Tier-Based, Permanent)**
- Determined solely by ship tier (T1-T5: 0%, T6: 10%, T7: 20%, T8: 40%, T9: 60%, T10: 100%)
- Location on map does NOT affect this percentage
- If ship fails permadeath roll: Permanently destroyed, must buy/build new ship
- If ship survives: Towed to port, requires expensive repairs (50-80% of ship value)

**2. Crew Card Permadeath (Tier-Based, Permanent)**
- Each crew card rolls independently at same percentages as ship tier
- If card fails permadeath roll: Officer + all levels/stats/progress PERMANENTLY LOST
- Must recruit new Level 1 card and retrain from scratch (months of progression lost)
- If card survives: Returns to barracks but likely has sailor casualties (see #3)

**3. Sailor Casualties (Damage-Based, Replaceable)**
- Individual sailors die based on combat damage severity (NOT tier-based)
- Occurs on ALL crew cards, even those that survive permadeath rolls
- Reduces crew card effectiveness: 30/50 sailors = 60% performance
- Can be replaced at ports for credits (economic cost, not permanent loss)
- Completely separate from crew card permadeath

**Example**: T8 Battleship destroyed in combat
- Ship rolls: 40% chance → If fails, ship permanently destroyed
- Each crew card rolls separately: 40% chance → Some cards may be lost forever
- Sailor casualties: Damage-based → All surviving cards lose sailors (replaceable)
- All three systems activate independently

### Risk Mitigation Options

**Insurance Systems** (Design Concept):
- Purchase coverage before expedition
- Reduces permadeath chance (e.g., Tier 10 from 100% to 70%)
- Expensive - only economic for valuable cargo runs
- Must be purchased per-expedition (prevents abuse)

**Squadron Support**:
- Escort ships provide protection during extraction
- Medical ships can reduce crew casualty chances
- Repair ships can fix critical damage en route
- Creates social gameplay and loot-sharing dynamics

**Strategic Positioning**:
- Stay near friendly waters for quick extraction
- Use lower-tier ships in high-tier zones (reduced risk but lower effectiveness)
- Flee before critical damage threshold reached
- Master disengagement tactics and speed management

**Emergency Measures**:
- Jettison cargo to gain speed (sacrifice loot for survival)
- Emergency repairs with limited supplies (temporary fixes)
- Distress beacons (call for help but reveal position)
- Crew evacuation (save crew, lose ship, cargo, and modules)

---

## Expedition Examples

### Example 1: Successful Economic Expedition
**Captain Profile**: Schmidt (Germany, Tier 2 Cruiser Königsberg)

**Outfitting Phase:**
- Load balanced AP/HE ammunition (60% magazine capacity)
- Fuel for 2-hour operational range
- Leave 40% cargo space for loot
- Basic crew (no specialists)
- Total cost: 5,000 credits

**Hunting Phase:**
- Transit through neutral waters toward contested zone
- Spot damaged American destroyer (USS Porter) limping toward Pearl Harbor
- Visual observation shows cargo containers (valuable loot visible)
- Germany-USA peace treaty in effect (reputation consequences if attacking)

**Combat Phase:**
- Decide to attack despite peace treaty (greed overcomes diplomacy)
- Porter is damaged and outgunned, minimal resistance
- Victory in 8 minutes, crew evacuates without casualties
- Loot acquired:
  - Rare fire control modules (40,000 credit value)
  - 20 tons chromium ore (15,000 credit value)
  - Salvaged 5-inch ammunition (3,000 credit value)

**Extraction Phase:**
- Königsberg took minor damage (5,000 repair cost)
- No pursuers (USA players not nearby)
- Clean extraction to German-controlled port
- 45-minute total expedition time

**Progression Phase:**
- Gross profit: 58,000 credits
- Costs: 10,000 credits (outfitting + repairs)
- Net profit: 48,000 credits (960% return on investment)
- **Reputation consequence**: -500 USA standing (future American port restrictions)
- Crew gained experience, 1 skill point earned
-

**Outcome**: Highly successful economic raid but created diplomatic complications

---

### Example 2: Failed High-Tier Extraction
**Captain Profile**: Nakamura (Japan, Tier 8 Battleship Nagato)

**Outfitting Phase:**
- Full combat load with premium ammunition (200,000 credit investment)
- Extended fuel reserves for deep penetration
- Minimal cargo space (confidence in combat dominance)
- 8 veteran crew cards (Level 120-180, months of training invested)
- Insurance purchased (150,000 credits, reduces ship/crew card permadeath from 40% to 25%)

**Hunting Phase:**
- Deep penetration into American-controlled Pacific waters
- Hunt for high-tier targets with valuable modules
- 90-minute transit to hostile zone

**Combat Phase:**
- Engage American Tier 7 cruiser squadron (3 ships)
- Intense 30-minute battle, Nagato takes heavy damage
- Victory: 2 cruisers sunk, 1 retreated
- Loot acquired:
  - Legendary fire control system (500,000 credit value)
  - Advanced radar modules (300,000 credit value)
  - Rare ammunition (50,000 credit value)
- **Critical damage**: Main battery turret destroyed, speed reduced to 60%

**Extraction Phase:**
- 120-minute journey back to friendly waters
- American player squadron (4 ships) detects damaged Nagato
- Attempts to flee but reduced speed prevents escape
- Desperate fighting retreat, expenditure of remaining ammunition
- Final American torpedo strike destroys Nagato 20km from safety

**Permadeath Rolls (Three Separate Systems):**

**Ship Permadeath**: 25% chance (with insurance reducing from 40% base)
- Rolled 18 → **SHIP PERMANENTLY DESTROYED** (needed 26+ to survive)
- Nagato lost forever, must buy/build new T8 battleship

**Crew Card Permadeath** (8 cards, each rolls 25% independently):
- Master Gunner (Level 180): Rolled 12 → **DESTROYED** (400+ hours lost)
- Fire Control (Level 150): Rolled 67 → Survived
- Heavy Gunner (Level 145): Rolled 88 → Survived
- Engineer (Level 140): Rolled 19 → **DESTROYED** (months of training lost)
- Damage Control (Level 135): Rolled 44 → Survived
- AA Master (Level 130): Rolled 73 → Survived
- Electronics (Level 125): Rolled 22 → **DESTROYED**
- Command (Level 120): Rolled 51 → Survived
- **Result**: 3 crew cards permanently destroyed, 5 survived

**Sailor Casualties** (on surviving cards):
- All 5 surviving crew cards took heavy sailor casualties from combat damage
- Average 45% sailor loss per card (replaceable at port for ~200,000 credits)

**Modules**: All modules destroyed (since ship was lost)
**Cargo**: All 850,000 credits worth of loot destroyed

**Progression Phase (Defeat):**
- Total loss: ~1.2 million credits (ship value + loot + modules)
- Time investment: 4 hours
- Reputation: +200 Japan (fought bravely) -300 USA (aggressive actions)
- Surviving crew traumatized (temporary skill penalties)
- Must rebuild from lower-tier ship

**Outcome**: Catastrophic failure despite combat victory - extraction failure negated all gains

---

### Example 3: Desperate Survival Extraction
**Captain Profile**: Chen (China, Tier 6 Destroyer Anshan)

**Outfitting Phase:**
- Light torpedo-focused load
- Moderate fuel reserves
- Mixed crew (some veterans, some recruits)
- No insurance (economic expedition, lower risk expected)

**Hunting Phase:**
- Patrol contested zone near Chinese waters
- Encounter Soviet Tier 6 cruiser attacking Chinese merchant convoy
- Decide to defend convoy (reputation opportunity)

**Combat Phase:**
- Successful torpedo attack on Soviet cruiser
- Cruiser disabled but not destroyed
- Light damage to Anshan (15% hull integrity lost)
- Modest loot from damaged cruiser
- **Unexpected**: Soviet player's squadron mate arrives (Tier 7 destroyer)

**Extraction Phase:**
- Flee toward Chinese port with superior enemy pursuing
- Progressive damage from long-range gunfire
- **Critical moment**: Speed reduced to 70% (engine damaged)
- Decision: Jettison cargo (20,000 credit value) to gain speed boost
- Emergency repairs extend engine life temporarily
- Desperate 30-minute chase
- Enter Chinese territorial waters, enemy breaks off pursuit
- Limp into port with 8% hull integrity remaining

**Progression Phase:**
- Loot lost: 20,000 credits (jettisoned)
- Repair costs: 18,000 credits
- Reputation gain: +500 China (defended convoy)
- Crew: No casualties (Tier 6 permadeath chance avoided)
- Net economic loss: -18,000 credits
- **Intangible gain**: Thrilling survival story, learned evasion tactics

**Outcome**: Economic failure but emotional triumph - survived impossible odds

---

## Design Principles for Extraction Mechanics

### 1. Nothing Is Secure Until Port Arrival
**Principle**: Players must physically return to friendly port to bank any gains.

**Implementation:**
- No mid-expedition banking or teleportation
- Cargo destroyed if ship sinks
- Can't trade loot in open water
- Must choose which port to extract to (some safer but further)

**Why This Matters**: Creates the core tension of extraction gameplay. Even dominant victories require successful return journey.

### 2. Risk Scales With Reward
**Principle**: Higher-value opportunities exist in more dangerous locations.

**Implementation:**
- Deeper penetration into hostile territory = rarer resources and higher-tier enemies
- High-traffic areas have better targets but more competition
- Time spent hunting increases both reward opportunity and exposure risk
- Higher-tier ships provide access to more valuable targets but increase permadeath stakes

**Why This Matters**: Players must constantly evaluate risk/reward trade-offs. Greed is balanced against survival instinct.

### 3. Extraction Is Distinct Gameplay Phase
**Principle**: Return journey is separate experience from hunting/combat.

**Implementation:**
- Damaged ship handles differently (speed, maneuverability)
- Cargo weight affects performance
- Depleted ammunition limits defensive options
- Pursuers have intelligence on your cargo value (incentive to chase)
- Different routing options (fast/dangerous vs. slow/safe)

**Why This Matters**: Extraction creates unique tactical scenarios. Combat victories don't guarantee expedition success.

### 4. Player Agency in Risk Selection
**Principle**: Players choose their risk exposure level.

**Implementation:**
- Ship tier system (T1-5 safe, T6-9 graduated risk, T10 maximum permadeath)
- Insurance options reduce but don't eliminate permadeath
- Location selection (stay near friendly ports vs. deep penetration into hostile waters)
- Expedition length (quick raids vs. extended hunting)
- Target selection (fight equals or punch above weight class)

**Why This Matters**: Different player risk tolerances accommodated. Hardcore and cautious players both have valid strategies.

### 5. Failure Is Expensive But Instructive
**Principle**: Failed extractions hurt but teach valuable lessons.

**Implementation:**
- Time investment lost (30-180 minutes)
- Outfitting costs not recovered
- Potential ship/crew permadeath
- Reputation consequences from aggressive actions
- Clear feedback on what went wrong

**Why This Matters**: Losses should inform future strategy. Players learn from mistakes and improve tactics over time.

### 6. Emergent Stories Through Systems
**Principle**: Memorable moments arise from mechanical interactions, not scripts.

**Implementation:**
- Dynamic encounters (player and NPC)
- Unpredictable combat outcomes
- Desperate extraction scenarios
- Near-misses and dramatic rescues
- Betrayals and unexpected alliances

**Why This Matters**: Best gameplay stories are player-created. Extraction mechanics naturally generate dramatic situations worth sharing.

---

## Integration with Other Systems

### Depends On
- [[Ship-Systems]] - Physical inventory, fuel, ammunition management
- [[Combat-Mechanics]] - PvPvE engagements during hunting/extraction
- [[Permadeath-System]] - Stakes and consequences of failed extraction
- [[Port-Systems]] - Outfitting before and banking after expeditions
- [[Reputation-System]] - Diplomatic consequences of aggressive actions
- [[Zone-Control]] - Territory ownership affects safe extraction routes
- [[Loot-Tables]] - What players acquire during expeditions

### Used By
- [[Economy-System]] - Loot circulation drives player trading
- [[Progression-System]] - Successful extractions fund ship/crew advancement
- [[Squadron-Mechanics]] - Coordinated fleet extractions
- [[Insurance-System]] - Risk mitigation for high-tier expeditions
- [[Session-Structure]] - Extraction defines typical gameplay loop
- [[New-Player-Experience]] - Early expeditions teach core loop

---

## Success Metrics

### Extraction Success Rates (Target Goals)
- **Tiers 1-5**: 80-90% success rate (protected learning zone, 0% permadeath)
- **Tiers 6-7**: 50-60% success rate (first permadeath risk, moderate stakes)
- **Tiers 8-9**: 35-45% success rate (high stakes)
- **Tier 10**: 15-25% success rate (legendary difficulty, 100% permadeath)

### Player Engagement Metrics
- **Average expedition length**: 60-90 minutes
- **Expeditions per session**: 1-2 for most players
- **Loot secured percentage**: 60-70% overall
- **Extraction phase excitement rating**: 8/10 or higher
- **Memorable extraction stories**: 1 per 10 expeditions worthy of sharing

### Economic Health Indicators
- **Loot circulation rate**: 70-80% of acquired loot reaches market
- **Ship loss rate**: 5-10% of high-tier ships per week (permadeath cycling)
- **Insurance purchase rate**: 40-60% of Tier 8-10 expeditions
- **Cargo jettison frequency**: 5-10% of expeditions (desperate measures)

---

## Known Issues & Design Challenges

### Challenge 1: Extraction Camping
**Problem**: Players ambush extraction routes creating frustrating choke points

**Mitigation Strategies:**
- Multiple viable extraction ports per region
- Detection systems warn of nearby hostiles
- NPC patrols near friendly ports (deterrent but not invulnerable)
- Reputation penalties for excessive camping
- Dynamic safe zone boundaries

### Challenge 2: Expedition Length Variability
**Problem**: Some players have 30 minutes, others have 3 hours

**Solutions:**
- Safe logout in designated zones (expedition pauses)
- Quick extraction routes near friendly waters (lower reward)
- Deep penetration for extended sessions (higher reward)
- Squadron play allows shift changes

### Challenge 3: Extraction Difficulty Balance
**Problem**: Too easy = no tension, too hard = frustration

**Balancing Approach:**
- Graduated difficulty by tier
- Player skill expression in routing and tactics
- Insurance system as pressure valve
- Clear feedback when extraction fails (learn what went wrong)

### Challenge 4: New Player Frustration
**Problem**: Learning extraction under pressure is stressful

**Onboarding Solutions:**
- Protected Tiers 1-4 with no permadeath
- Tutorial expeditions with clear objectives
- Practice scenarios without real stakes
- Mentor systems with veteran players

---

## Future Enhancements

### Planned Features
- **Dynamic extraction events**: Random encounters during return journey
- **Convoy extraction**: NPC escorts for safer but slower returns
- **Alternative extraction methods**: Aerial extraction for crew/small cargo
- **Extraction contracts**: Pre-arranged pickup points with squadron support
- **Black market ports**: Fence stolen goods without reputation loss

### Potential Additions
- **Extraction modifiers**: Weather, day/night, special events affect difficulty
- **Pursuit mechanics**: Enhanced chase gameplay systems
- **Emergency protocols**: Self-destruct options to deny loot to enemies
- **Extraction achievements**: Special rewards for dramatic successful escapes
- **Historical scenarios**: Famous WWII extraction missions as templates

---

## Cross-References
- [[Game-Vision]] - Extraction as core of player fantasy
- [[Permadeath-System]] - Stakes that make extraction meaningful
- [[Combat-Mechanics]] - Engagements during hunt and extraction phases
- [[Ship-Systems]] - Physical inventory and damage affecting extraction
- [[Port-Systems]] - Outfitting and banking at endpoints
- [[Economy-System]] - Loot circulation through extraction
- [[Zone-Control]] - Territory affecting extraction routes
- [[Session-Structure]] - How extraction fits into typical play session

---

## Changelog
- **2025-11-17**: Initial document creation - extracted from GDD_Updated-1.md lines 23-50, 26-31
