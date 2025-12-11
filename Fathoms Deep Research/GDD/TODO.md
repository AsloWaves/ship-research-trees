# Fathoms Deep GDD - Master TODO List
**Generated**: 2025-12-10
**Documents Reviewed**: 40+ primary design documents from 564 total files
**Last Updated**: 2025-12-11

---

## Quick Status

| Category | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| Missing Mechanics | 4 | 12 | 12 | 8 |
| Incomplete Mechanics | 3 | 10 | 10 | 6 |
| Contradictions | 1 | 4 | - | - |
| Design Questions | - | - | 25+ | - |
| Integration Gaps | 4 | 8 | - | - |

*Updated 2025-12-11: Major Q&A session resolved 40+ design questions*
*Resolved via: [[Crew-Module-Mechanics]], [[Tetris-Fitting-Mechanics]], [[Research-Unlock-System]], [[Firing-Solution-System]], [[Design-Decisions-2025-12-11]]*

---

## CRITICAL PRIORITY (Block Phase 2)

### Must Resolve Before Combat Implementation

- [x] **Crew-Module Efficiency Formula**: Define interaction between `Sailor_Factor × Stat_Factor` and module quality variance (70-130%) ✅ *Resolved in [[Crew-Module-Mechanics]]*
- [x] **Permadeath Crew Recovery**: Define exact window, location, cost, and prerequisites for crew card retrieval ✅ *Resolved 2025-12-11: Insurance-based recovery only. NPC + Player-run insurance. Processing takes days. See [[Design-Decisions-2025-12-11]]*
- [x] **Firing Solution Formula**: Align buildup/degradation rates with stated solution modifier ranges (0.5-1.0×) ✅ *Resolved in [[Firing-Solution-System]]*
- [x] **Ammunition Storage**: Define stack sizes, weight per stack, cargo grid consumption, and mid-combat depletion ✅ *Resolved 2025-12-11: Cargo-only system, stacks by caliber, manual ammo type switching. See [[Design-Decisions-2025-12-11]]*
- [x] **Crew Classification System**: Resolve "any crew can operate any module" vs "Gunner required for turrets" contradiction ✅ *Resolved in [[Crew-Module-Mechanics]] - any crew can operate, specialists get bonuses*
- [x] **Module Quality-to-Efficiency**: Define how 70-130% quality affects ongoing efficiency (cap? reduction? multiplicative?) ✅ *Resolved 2025-12-11: Direct multiplier (70% quality = 70% stats). See [[Design-Decisions-2025-12-11]]*

---

## MISSING MECHANICS

### Combat Systems

- [ ] **Torpedo Detonation Mechanics**: Obstacles, decoys, evasion handling, detonation distance
- [x] **Ramming Mechanics**: Ship collision damage system ✅ *Resolved 2025-12-11: Asymmetric by class/size (larger ship takes less damage)*
- [x] **Friendly Fire System**: Blue-on-blue handling in team combat ✅ *Resolved 2025-12-11: Full friendly fire always on*
- [ ] **Artillery Spotting System**: Observer ship fire correction mechanics
- [ ] **Gunnery Dispersion Formula**: Mathematical model for shell spread pattern
- [ ] **Bounce/Ricochet Mechanics**: Shell deflection angles and probabilities
- [ ] **Fire Spread Mechanics**: Compartment-to-compartment fire propagation
- [x] **Aircraft Recovery Mechanics**: Carrier aircraft fuel exhaustion, ditching, recovery ✅ *Resolved 2025-12-11: Plane lost, pilot crew card loses sailors (not card itself)*
- [x] **Magazine Detonation Prevention**: Magazine flooding mechanics and effects ✅ *Resolved 2025-12-11: Per penetrating hit roll, chance scales with ammo quantity in cargo*

### Crew Systems

- [x] **Morale System**: Effects on crew performance (or confirm "zero morale" design) ✅ *Resolved 2025-12-11: Confirmed zero-morale design - crew performance purely stat-based*
- [x] **Crew Stat Generation**: Initial stat distribution at Level 1 ✅ *Confirmed in [[Crew-Skills]]: 7-15 starting range, Navy Field-style randomization*
- [ ] **Crew Training Costs**: Exact credit costs for classification unlocks
- [ ] **Crew Reassignment Under Fire**: Emergency mid-combat crew reassignment rules
- [ ] **Crew Panic/Breakdown**: Heavy damage effects on crew performance *(Note: May be N/A due to zero-morale design)*
- [x] **Crew Death Visuals**: What happens when crew card is wiped out ✅ *Resolved 2025-12-11: Station goes red/disabled when crew drops below threshold*

### Ship Systems

- [ ] **Ship Stability/Listing**: How damage affects turning and speed
- [ ] **Compartmentalization**: Torpedo damage spread rules
- [ ] **Bulkhead Integrity**: Hit capacity before damage spreads
- [ ] **Secondary Gun Auto-Fire**: AI targeting rules for secondary batteries
- [ ] **Ship Sinking Animation**: Time from fatal damage to sinking
- [x] **Submarine Surfacing/Diving**: Time, vulnerability window, mechanics ✅ *Resolved 2025-12-11: Category-based depths (Surface/Periscope/Shallow/Deep/Crush) limited by ocean depth and hull type*

### Detection & Targeting

- [ ] **Horizon Distance Formula**: Visual horizon calculation based on observer height
- [ ] **Weather Transition Timing**: How long weather changes take to propagate
- [x] **Contact Memory Duration**: Exact decay timing after losing contact ✅ *Resolved 2025-12-11: Instant fade (no memory/last-known-position)*
- [x] **Bearing Arc Randomization**: Distribution type (linear, Gaussian, etc.) ✅ *Resolved 2025-12-11: Uniform distribution within arc*
- [x] **Misidentification Update**: Real-time shadow correction with better equipment ✅ *Resolved 2025-12-11: Initial ID locked - only visual confirmation can override*

### Module System

- [x] **Module Slot Rotation**: Can modules be rotated during placement? ✅ *Resolved in [[Tetris-Fitting-Mechanics]] - yes, if shape makes sense*
- [ ] **Structural Support**: Do some modules require foundation modules?
- [ ] **Module Degradation**: Non-combat wear over time
- [ ] **Component Interchangeability**: Salvaged module direct installation rules

### Economy Systems

- [x] **Currency Exchange Rates**: Resource Points to Credits conversion ✅ *Resolved 2025-12-11: No conversion - separate economies*
- [x] **Market Price Algorithm**: NPC price generation formula ✅ *Resolved 2025-12-11: Supply/demand simulation (dynamic economy)*
- [x] **Player Tax/Tariff System**: Port transaction taxation ✅ *Resolved 2025-12-11: Split (port owner + nation tax)*
- [ ] **Inflation Control**: Economy scaling as server wealth increases
- [x] **Resource Decay**: Stored resource degradation over time ✅ *Resolved 2025-12-11: No decay (permanent storage)*
- [ ] **Storage Fees**: Port storage costs for player loot
- [x] **Trade Route Automation**: Automated merchant trading mechanics ✅ *Resolved 2025-12-11: Guild convoy system only*

### Permadeath System

- [x] **Crew Recovery Window**: Exact time limit for permadead crew retrieval ✅ *Resolved 2025-12-11: Insurance-based recovery only (no timed retrieval)*
- [x] **Ship Wreck Persistence**: How long wrecks remain as salvage opportunities ✅ *Resolved 2025-12-11: 1-4 hours*
- [x] **Insurance Claim Processing**: Time and process for payouts ✅ *Resolved 2025-12-11: Takes days (real-time), unlimited coverage*
- [x] **Permadeath Announcements**: Public or private death notifications ✅ *Resolved 2025-12-11: Private (no server broadcast)*
- [x] **Crew Resurrection Methods**: Any path to recover dead crews ✅ *Resolved 2025-12-11: Insurance only - returns same stats/level, different identity (name)*

### Multiplayer Features

- [x] **Alliance/Guild Structures**: Complete system definition ✅ *Resolved 2025-12-11: Large guilds (500+), full alliance system, full sharing including ships*
- [x] **Diplomacy Declaration**: Alliance formation/breaking mechanics ✅ *Resolved 2025-12-11: Dev-controlled events + auto-escalation from player actions*
- [ ] **Player Housing/Guild Halls**: Absent entirely
- [ ] **Seasonal Content Rotation**: Content refresh cadence

---

## INCOMPLETE MECHANICS

### Combat Systems

- [ ] **AP Overpenetration Damage**: Clarify explosive charge behavior on over-pen
- [ ] **Citadel Zone Definition**: Spatial definition per ship class
- [ ] **Module Destruction Probability**: Critical hit → destroy chance
- [ ] **Fire Damage Continuation**: Does fire continue without crew or engines?

### Crew Systems

- [ ] **XP Amounts Per Level**: Exact experience thresholds
- [ ] **Efficiency Matching Bonus**: Level 200 crew on Level 50 turret behavior
- [ ] **Classification Decision Tree**: Unlock path visualization
- [ ] **Damage Severity Definition**: What constitutes "severity" for casualties

### Carrier Operations

- [ ] **Aircraft Waypoint System**: UI and control design
- [ ] **AA Hit Probability Formula**: Anti-aircraft effectiveness calculation
- [ ] **Wing Destruction Inventory**: Player inventory space for lost wings
- [ ] **Aviation Fuel Pool**: Capacity and storage mechanics

### Submarine Warfare

- [ ] **Silent Running Percentage**: Detection reduction amount
- [ ] **Thermal Layer Mechanics**: How sonar contact breaks/regains
- [ ] **Depth Charge Falloff**: Blast damage vs distance formula
- [ ] **Periscope Attack Details**: Visibility, raise/lower timing

### Detection System

- [ ] **Solution Degradation Formula**: Exact calculation for maneuver-based decay
- [ ] **Shadow Size Convergence**: Speed of shadow correction as range closes
- [ ] **Contact Memory Decay Type**: Linear or sudden loss
- [ ] **Night Modifier Variance**: When 0.05× vs 0.15× applies

### Module System

- [ ] **Emergency Repair Mechanics**: 50% restoration on destroyed module behavior
- [ ] **Concurrent Installation Types**: Same vs different module types
- [ ] **Installation Time Determinants**: What factors affect time
- [ ] **Quality Upgrade Mechanics**: How quality factors in enhancement

### Economy Systems

- [ ] **Resource Category Unification**: Consolidate Strategic/Industrial/Fuel categories
- [ ] **Repair Cost Formula**: Cost tied to crew size, tier, or module count?
- [ ] **Black Market Reputation**: Access requirements (mentioned nowhere else)

### Permadeath System

- [ ] **Per-Card vs Total Roll**: T6 10% per card or total chance clarification
- [ ] **Cargo Insurance**: Can cargo be insured?

---

## CONTRADICTIONS TO RESOLVE

### Major Contradictions

| ID | Document A | Document B | Conflict |
|----|------------|------------|----------|
| ~~C1~~ | ~~Crew-Module-Mechanics~~ | ~~Damage-Model~~ | ~~Casualty timing: during combat vs post-battle?~~ ✅ *Resolved 2025-12-11: Real-time (immediate effect)* |
| ~~C2~~ | ~~GDD-Overview~~ | ~~Damage-Model~~ | ~~T10 100% loss: automatic or 100% roll per card?~~ ✅ *Resolved 2025-12-11: Per-card roll (T6=10%, T7=25%, T8=50%, T9=75%, T10=100%)* |
| ~~C3~~ | ~~Module-System~~ | ~~Crew-Management~~ | ~~"Any crew operates any module" vs "Gunner required for turrets"~~ ✅ *Resolved in [[Crew-Module-Mechanics]]* |
| ~~C4~~ | ~~Ballistics-Gunnery~~ | ~~Detection-System~~ | ~~Solution buildup rate interpretation (+%/sec meaning)~~ ✅ *Resolved in [[Firing-Solution-System]]*|
| ~~C5~~ | ~~Crew-Management examples~~ | ~~Formula text~~ | ~~Weight calculation formula consistency~~ ✅ *Resolved in [[Crew-Module-Mechanics]]* |
| C6 | Module-System | Module-System | Repair slower than installation (2-5 min vs 5-15 min) |

### Minor Contradictions

| ID | Issue | Resolution Needed |
|----|-------|-------------------|
| ~~C7~~ | ~~Ammunition in cargo grid vs magazine system~~ | ~~Define capacity, stack size, jettison rules~~ ✅ *Resolved 2025-12-11: Cargo-only, stacks by caliber* |
| C8 | Loot rarity vs module quality | Are these separate systems or connected? |
| ~~C9~~ | ~~Fire control module bonus vs solution cap~~ | ~~Can accuracy exceed 100%?~~ ✅ *Resolved 2025-12-11: Soft cap with logarithmic diminishing returns* |
| C10 | Aircraft fuel consumption | Ship inventory vs global supply? |
| C11 | Radar range variance (SG 35km vs 20-50km table) | Clarify SG-specific vs general ranges |
| C12 | Crew experience numbers | Missing XP-to-level table |
| ~~C13~~ | ~~Battle casualty timing~~ | ~~Real-time updates or post-battle only?~~ ✅ *Resolved 2025-12-11: Real-time* |
| ~~C14~~ | ~~Insurance system existence~~ | ~~Mentioned but no mechanics document~~ ✅ *Resolved 2025-12-11: Full system defined - NPC + Player providers, level-based costs, days processing*

---

## DESIGN QUESTIONS

### Combat System (Q1-Q10)

1. **Citadel Definition**: Where exactly is citadel zone? Can multiple shells hit simultaneously?
2. **Penetration Angles**: Does 60° auto-bounce apply to all shell types or only AP?
3. ~~**Fire Control Failure**: Solution collapse: immediate to 0% or gradual decay?~~ ✅ *Gradual decay (accelerated 2-3×)*
4. ~~**Magazine Detonation Roll**: Per hit or once per engagement?~~ ✅ *Per penetrating hit, chance scales with ammo quantity*
5. **Torpedo Evasion**: Player-controlled or automatic? Probability formula?
6. **Aircraft Attrition Selection**: Random or most-damaged-first destruction?
7. ~~**Submarine Depth Levels**: Specific depths or shallow/medium/deep categories?~~ ✅ *Category-based, limited by ocean depth + hull*
8. ~~**Ramming Damage Distribution**: Equal to both ships? Asymmetric by class?~~ ✅ *Asymmetric by class/size*
9. **Fog Spotting with Radar**: Can observer provide targeting without line-of-sight?
10. ~~**Gun Magazine Capacity**: Reload from cargo after depletion?~~ ✅ *Cargo-only system, manual ammo switching*

### Crew System (Q11-Q18)

11. ~~**Crew Specializations**: What classifications beyond Gunner/Engineer/AA?~~ ✅ *18 classes in 4 branches (Gunnery, Engineering, Operations, Aviation) + extraction roles*
12. ~~**Cross-Ship Crew Efficiency**: Destroyer crew on battleship turret penalty/bonus?~~ ✅ *No penalty - any crew can operate any compatible module*
13. ~~**Morale System Status**: Actually absent or simplified?~~ ✅ *Confirmed zero-morale design - purely stat-based*
14. ~~**Initial Stat Variance**: Random or fixed at Level 1? Nationality effects?~~ ✅ *7-15 NF-style random, no nationality effect*
15. **Crew Fatigue**: Extended combat performance degradation?
16. ~~**Crew Cross-Training**: Can Gunner retrain as Engineer?~~ ✅ *Full respec (costly)*
17. **Crew Achievement Tracking**: Kill counts, battles survived?
18. **Officer Name Generation**: Random or database-driven? Player customizable?

### Detection System (Q19-Q28)

19. ~~**Shadow Misidentification Recovery**: Real-time update when better equipped ally detects?~~ ✅ *Initial ID locked - only visual confirmation overrides*
20. ~~**Phase Transition During Combat**: Solution behavior when target goes Phase 3→2?~~ ✅ *Solution independent of phase*
21. **Bearing Randomization Frequency**: Per second? Per radar sweep?
22. **Passive Sonar Accuracy**: Single line or 2-3° arc?
23. **Radar Clutter/Chaff**: False contacts in storms? Decoy mechanics?
24. ~~**Visual Detection Through Smoke**: Can visible turrets identify target?~~ ✅ *No visual through smoke/weather (complete block)*
25. ~~**Detection Toggle Spam**: Cooldown between sonar on/off?~~ ✅ *5-10 second cooldown*
26. ~~**Contact Persistence Post-Combat**: Do enemy contacts fade or persist?~~ ✅ *Instant fade (no memory)*
27. **Radar vs Sonar Priority**: Single crew monitoring both simultaneously?
28. ~~**Shared Misidentification**: Does ally see sender's error or own data?~~ ✅ *Best data wins (system compares all observers)*

### Module System (Q29-Q37)

29. ~~**Module Rotation**: 2×2 module orientation flexibility?~~ ✅ *Resolved in [[Tetris-Fitting-Mechanics]]*
30. ~~**Modular Redundancy**: Dual identical engines advantage?~~ ✅ *No redundancy - each module independent*
31. ~~**Cascading Failures**: Adjacent module collateral damage?~~ ✅ *No cascade - isolated damage*
32. **Module Cooling**: Deliberate overheating through sustained fire?
33. ~~**Module Warm-Up**: New installation fire delay?~~ ✅ *No warm-up - all modules installed in port*
34. ~~**Weapon Interchangeability**: DD turret on cruiser mounting?~~ ✅ *Cross-nation freely interchangeable*
35. ~~**Quality Impact on Efficiency**: 70% vs 130% quality effect on formula?~~ ✅ *Direct multiplier (70% = 70% stats)*
36. ~~**Armor Stacking**: Multiple armor section installations?~~ ✅ *Navy Field style - thickness allocation to zones, not modules*
37. ~~**Module vs Crew Weight**: Separate calculations or combined budget?~~ ✅ *Resolved in [[Crew-Module-Mechanics]] - separate, both count toward mount capacity*

### Economy System (Q38-Q48)

38. ~~**Resource Conversion**: Chromium to Electronics exchange rate?~~ ✅ *No conversion - RP and Credits are separate economies*
39. **Port Fee Determinants**: Tier, cargo value, ship size, reputation?
40. ~~**Market Volatility**: Real-time or periodic price calculation?~~ ✅ *Supply/demand simulation (dynamic)*
41. ~~**Black Market Locations**: All ports or secret locations?~~ ✅ *Hidden locations (must discover)*
42. ~~**Intelligence Valuation**: Who determines initial value?~~ ✅ *Relevance-based pricing (freshness + importance)*
43. **Crafting Skill Progression**: XP per craft determination?
44. ~~**Player Market Taxes**: Where do fees go? Sink? Nation? Port owner?~~ ✅ *Split (port owner + nation)*
45. **Inflation Control**: Server wealth spiral prevention?
46. **Resource Gathering**: Mining operations? Harvesting zones?
47. ~~**Production Facility Ownership**: Individual or guild only?~~ ✅ *Guild-owned facilities*
48. ~~**Trade Route Automation**: Profit model vs manual trading?~~ ✅ *Guild convoy system only*

### Permadeath System (Q49-Q53)

49. ~~**Recovery Mechanics**: Window length, location, cost, prerequisites?~~ ✅ *Insurance-based only, NPC + Player providers, level-based costs, days processing*
50. ~~**Insurance Claims**: Auto-pay or submission required? Fraud detection?~~ ✅ *Processing takes days, unlimited coverage per crew, returns same stats/level but different name*
51. ~~**Public Announcements**: Server memorial? Legacy impact?~~ ✅ *Private (no server broadcast)*
52. ~~**Resurrection Methods**: Any path to recover dead crews?~~ ✅ *Insurance only - same stats/level, new identity*
53. ~~**Partial Ship Survival**: Condition after surviving T6-T9 roll?~~ ✅ *50% sailor casualties on surviving crew cards*

### Extraction System (Q54-Q59)

54. **Cargo Capacity**: Weight, volume, or item-count based?
55. **Cargo Visibility Radius**: Same as ship detection or different?
56. **Loot Crate Quantity**: Per HP, per class, or fixed?
57. **Port Security Variance**: Reputation affect cargo safety?
58. ~~**Cargo Insurance**: Available? Cost? Coverage?~~ ✅ *Not available - only ship/crew insurance*
59. **Extraction Failure Salvage**: Can sunken cargo be recovered?

### Progression System (Q60-Q64)

60. ~~**Ship Tier Unlock**: Credits only? Reputation? Missions?~~ ✅ *Resolved in [[Research-Unlock-System]] - RP research then build or buy*
61. ~~**Module Tech Trees**: Branching or linear? Nation choice?~~ ✅ *Resolved in [[Research-Unlock-System]] - three separate trees (ships, turrets, modules), nation-specific*
62. **Crew Collection Limit**: Max cards? Storage limit?
63. **Post-Permadeath Progression**: Restart from scratch or accelerated?
64. **Achievement System**: Tracking, rewards, bonuses?

### Multiplayer Coordination (Q65-Q70)

65. ~~**Fleet Radar Sharing**: Automatic ally target sharing?~~ ✅ *Range-limited sharing (~radio range)*
66. ~~**Voice Communication Range**: Bypass 2km radio limit?~~ ✅ *Equipment-dependent (radio module quality)*
67. ~~**Guild Management**: Size, treasury, ranks, shared resources?~~ ✅ *Large (500+), full sharing including ships, full alliance system*
68. ~~**Nation Diplomacy Votes**: War declaration mechanics?~~ ✅ *Dev-controlled + auto-escalation from player actions*
69. ~~**Cross-Nation Grouping**: Grouping during active war?~~ ✅ *Not allowed during war*
70. ~~**PvP Flagging**: Indicate intent? Go peaceful?~~ ✅ *Always PvP enabled (no flag system)*

---

## INTEGRATION GAPS

### Major Gaps

| ID | Systems | Issue |
|----|---------|-------|
| ~~I1~~ | ~~Crew-Module Weight~~ | ~~No interaction explanation between crew weight and module weight budgets~~ ✅ *Resolved in [[Crew-Module-Mechanics]] and [[Tetris-Fitting-Mechanics]]* |
| I2 | Offline Training + Economy | Training facility fees undefined; free training devalues paid methods |
| ~~I3~~ | ~~Ammunition + Combat~~ | ~~No mid-combat depletion mechanic; magazine vs cargo undefined~~ ✅ *Resolved 2025-12-11: Cargo-only, stacks by caliber, manual switching* |
| I4 | Fuel + Economy | Fuel efficiency vs distance calculation; long-distance trade viability |
| ~~I5~~ | ~~Permadeath + Insurance~~ | ~~No provider system, claim triggers, cost calculation~~ ✅ *Resolved 2025-12-11: NPC + Player providers, level-based costs, days processing* |
| I6 | Reputation + Economy | "Nation Standing" vs "Reputation" terminology; inheritance after death |
| I7 | Detection + Combat | No "sprint to break contact" mechanic; detection vs engagement range mismatch |
| ~~I8~~ | ~~Crew Casualty + Combat~~ | ~~No visual feedback; no damage control priority system; no automation explanation~~ ✅ *Resolved 2025-12-11: Station goes red/disabled, real-time casualties* |
| ~~I9~~ | ~~Submarine Sonar + Surface Radar~~ | ~~Can surface ships detect submerged subs? Asymmetrical advantage?~~ ✅ *Resolved 2025-12-11: Radar cannot detect submerged subs - sonar only* |
| I10 | Crafting Quality + Market | How does quality affect pricing? Certification system? |

### Minor Gaps

| ID | Systems | Issue |
|----|---------|-------|
| I11 | Crew Stats + Fire Control | Stat and module bonus stacking (multiplicative?) |
| I12 | Crew Slots + Module Count | Example shows 10 modules, 12 crew positions - 2 unused slots |
| I13 | Port Tier + Services | Tier identification before travel; cost differential |
| I14 | Salvage + Module Quality | Functionality % vs quality % interaction |
| I15 | Multi-Nation Tech | Mixing nations penalty/bonus undefined |
| I16 | Offshore Platforms | Capture mechanics, resource generation |
| I17 | Convoy Escort + Loot | Reward scaling with loot value |
| I18 | NPC Economy | Resource production per nation; blockade strategy |
| I19 | Crew Rarity | Rarity levels, stat effects, captured crew rarity |
| I20 | Insurance + Permadeath | Full coverage eliminates tension; denial scenarios |

---

## DOCUMENTS TO CREATE

### Critical (Phase 2 Blocking)

- [x] `03-Combat-Systems/Firing-Solution-System.md` - Complete firing solution calculation ✅ *Created 2025-12-11*
- [ ] `03-Combat-Systems/Damage-States.md` - Module and ship damage state definitions
- [ ] `02-Core-Gameplay/Ammunition-System.md` - Storage, depletion, resupply mechanics
- [ ] `07-Economy/Insurance-System.md` - Providers, coverage, claims, costs

### High Priority

- [ ] `03-Combat-Systems/Depth-System.md` - Submarine depth mechanics
- [ ] `03-Combat-Systems/Aircraft-Supply-System.md` - Carrier fuel and ordnance
- [ ] `03-Combat-Systems/Detection-Range-Formulas.md` - Complete detection calculations
- [ ] `02-Core-Gameplay/Crew-Stat-Generation.md` - Initial stat distribution

### Medium Priority

- [ ] `05-Multiplayer/Guild-System.md` - Alliance and guild mechanics
- [ ] `05-Multiplayer/Diplomacy-System.md` - Nation state transitions
- [ ] `07-Economy/Market-Algorithm.md` - NPC pricing formulas
- [ ] `03-Combat-Systems/Friendly-Fire.md` - Blue-on-blue handling

---

## PRIORITY MATRIX

### Phase 2 Blockers (Resolve First)

1. ~~Crew-Module Efficiency Formula completion~~ ✅
2. Permadeath Crew Recovery definition
3. ~~Firing Solution Formula alignment~~ ✅ *Resolved in [[Firing-Solution-System]]*
4. Ammunition Storage mechanics
5. ~~Crew Classification contradiction resolution~~ ✅
6. Module Quality-to-Efficiency mapping

### Before Phase 2 Complete

7. Casualty Application Timing finalization
8. Repair Time Formula creation
9. NPC Economy Simulation pseudocode
10. Complete Submarine Mechanics

### Before Phase 3

11. Guild/Squadron Management System
12. Complete Insurance System Design
13. Nation Diplomatic State Machine
14. Offline Training Premium Features

---

## NOTES

### Design Strengths
- Comprehensive extraction-based gameplay loop
- Well-designed crew card system with weight-based progression gates
- Detailed module system with dual hardpoint/equipment slot architecture
- Mathematical rigor in detection and firing solution mechanics
- Clear multi-tier economy design with strategic depth

### Critical Gaps
- ~~Crew-module efficiency calculations incomplete~~ ✅
- Permadeath recovery system undefined
- ~~Firing solution formula misaligned~~ ✅ *Resolved in [[Firing-Solution-System]]*
- Ammunition storage system undefined
- ~~Crew classification system contradictory~~ ✅

### Estimated Resolution Time
2-3 weeks of design work (not implementation) for Phase 2 blockers

---

*This document should be updated as mechanics are resolved. Check off items as they are completed.*
