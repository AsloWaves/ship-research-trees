# Fathoms Deep GDD - Master TODO List
**Generated**: 2025-12-10
**Documents Reviewed**: 40+ primary design documents from 564 total files
**Last Updated**: 2025-12-10

---

## Quick Status

| Category | Critical | High | Medium | Low |
|----------|----------|------|--------|-----|
| Missing Mechanics | 12 | 18 | 15 | 8 |
| Incomplete Mechanics | 8 | 14 | 12 | 6 |
| Contradictions | 6 | 8 | - | - |
| Design Questions | - | - | 70+ | - |
| Integration Gaps | 10 | 10 | - | - |

---

## CRITICAL PRIORITY (Block Phase 2)

### Must Resolve Before Combat Implementation

- [ ] **Crew-Module Efficiency Formula**: Define interaction between `Sailor_Factor × Stat_Factor` and module quality variance (70-130%)
- [ ] **Permadeath Crew Recovery**: Define exact window, location, cost, and prerequisites for crew card retrieval
- [ ] **Firing Solution Formula**: Align buildup/degradation rates with stated solution modifier ranges (0.5-1.0×)
- [ ] **Ammunition Storage**: Define stack sizes, weight per stack, cargo grid consumption, and mid-combat depletion
- [ ] **Crew Classification System**: Resolve "any crew can operate any module" vs "Gunner required for turrets" contradiction
- [ ] **Module Quality-to-Efficiency**: Define how 70-130% quality affects ongoing efficiency (cap? reduction? multiplicative?)

---

## MISSING MECHANICS

### Combat Systems

- [ ] **Torpedo Detonation Mechanics**: Obstacles, decoys, evasion handling, detonation distance
- [ ] **Ramming Mechanics**: Ship collision damage system
- [ ] **Friendly Fire System**: Blue-on-blue handling in team combat
- [ ] **Artillery Spotting System**: Observer ship fire correction mechanics
- [ ] **Gunnery Dispersion Formula**: Mathematical model for shell spread pattern
- [ ] **Bounce/Ricochet Mechanics**: Shell deflection angles and probabilities
- [ ] **Fire Spread Mechanics**: Compartment-to-compartment fire propagation
- [ ] **Aircraft Recovery Mechanics**: Carrier aircraft fuel exhaustion, ditching, recovery
- [ ] **Magazine Detonation Prevention**: Magazine flooding mechanics and effects

### Crew Systems

- [ ] **Morale System**: Effects on crew performance (or confirm "zero morale" design)
- [ ] **Crew Stat Generation**: Initial stat distribution at Level 1
- [ ] **Crew Training Costs**: Exact credit costs for classification unlocks
- [ ] **Crew Reassignment Under Fire**: Emergency mid-combat crew reassignment rules
- [ ] **Crew Panic/Breakdown**: Heavy damage effects on crew performance
- [ ] **Crew Death Visuals**: What happens when crew card is wiped out

### Ship Systems

- [ ] **Ship Stability/Listing**: How damage affects turning and speed
- [ ] **Compartmentalization**: Torpedo damage spread rules
- [ ] **Bulkhead Integrity**: Hit capacity before damage spreads
- [ ] **Secondary Gun Auto-Fire**: AI targeting rules for secondary batteries
- [ ] **Ship Sinking Animation**: Time from fatal damage to sinking
- [ ] **Submarine Surfacing/Diving**: Time, vulnerability window, mechanics

### Detection & Targeting

- [ ] **Horizon Distance Formula**: Visual horizon calculation based on observer height
- [ ] **Weather Transition Timing**: How long weather changes take to propagate
- [ ] **Contact Memory Duration**: Exact decay timing after losing contact
- [ ] **Bearing Arc Randomization**: Distribution type (linear, Gaussian, etc.)
- [ ] **Misidentification Update**: Real-time shadow correction with better equipment

### Module System

- [ ] **Module Slot Rotation**: Can modules be rotated during placement?
- [ ] **Structural Support**: Do some modules require foundation modules?
- [ ] **Module Degradation**: Non-combat wear over time
- [ ] **Component Interchangeability**: Salvaged module direct installation rules

### Economy Systems

- [ ] **Currency Exchange Rates**: Resource Points to Credits conversion
- [ ] **Market Price Algorithm**: NPC price generation formula
- [ ] **Player Tax/Tariff System**: Port transaction taxation
- [ ] **Inflation Control**: Economy scaling as server wealth increases
- [ ] **Resource Decay**: Stored resource degradation over time
- [ ] **Storage Fees**: Port storage costs for player loot
- [ ] **Trade Route Automation**: Automated merchant trading mechanics

### Permadeath System

- [ ] **Crew Recovery Window**: Exact time limit for permadead crew retrieval
- [ ] **Ship Wreck Persistence**: How long wrecks remain as salvage opportunities
- [ ] **Insurance Claim Processing**: Time and process for payouts
- [ ] **Permadeath Announcements**: Public or private death notifications
- [ ] **Crew Resurrection Methods**: Any path to recover dead crews

### Multiplayer Features

- [ ] **Alliance/Guild Structures**: Complete system definition
- [ ] **Diplomacy Declaration**: Alliance formation/breaking mechanics
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
| C1 | Crew-Module-Mechanics | Damage-Model | Casualty timing: during combat vs post-battle? |
| C2 | GDD-Overview | Damage-Model | T10 100% loss: automatic or 100% roll per card? |
| C3 | Module-System | Crew-Management | "Any crew operates any module" vs "Gunner required for turrets" |
| C4 | Ballistics-Gunnery | Detection-System | Solution buildup rate interpretation (+%/sec meaning) |
| C5 | Crew-Management examples | Formula text | Weight calculation formula consistency |
| C6 | Module-System | Module-System | Repair slower than installation (2-5 min vs 5-15 min) |

### Minor Contradictions

| ID | Issue | Resolution Needed |
|----|-------|-------------------|
| C7 | Ammunition in cargo grid vs magazine system | Define capacity, stack size, jettison rules |
| C8 | Loot rarity vs module quality | Are these separate systems or connected? |
| C9 | Fire control module bonus vs solution cap | Can accuracy exceed 100%? |
| C10 | Aircraft fuel consumption | Ship inventory vs global supply? |
| C11 | Radar range variance (SG 35km vs 20-50km table) | Clarify SG-specific vs general ranges |
| C12 | Crew experience numbers | Missing XP-to-level table |
| C13 | Battle casualty timing | Real-time updates or post-battle only? |
| C14 | Insurance system existence | Mentioned but no mechanics document |

---

## DESIGN QUESTIONS

### Combat System (Q1-Q10)

1. **Citadel Definition**: Where exactly is citadel zone? Can multiple shells hit simultaneously?
2. **Penetration Angles**: Does 60° auto-bounce apply to all shell types or only AP?
3. **Fire Control Failure**: Solution collapse: immediate to 0% or gradual decay?
4. **Magazine Detonation Roll**: Per hit or once per engagement?
5. **Torpedo Evasion**: Player-controlled or automatic? Probability formula?
6. **Aircraft Attrition Selection**: Random or most-damaged-first destruction?
7. **Submarine Depth Levels**: Specific depths or shallow/medium/deep categories?
8. **Ramming Damage Distribution**: Equal to both ships? Asymmetric by class?
9. **Fog Spotting with Radar**: Can observer provide targeting without line-of-sight?
10. **Gun Magazine Capacity**: Reload from cargo after depletion?

### Crew System (Q11-Q18)

11. **Crew Specializations**: What classifications beyond Gunner/Engineer/AA?
12. **Cross-Ship Crew Efficiency**: Destroyer crew on battleship turret penalty/bonus?
13. **Morale System Status**: Actually absent or simplified?
14. **Initial Stat Variance**: Random or fixed at Level 1? Nationality effects?
15. **Crew Fatigue**: Extended combat performance degradation?
16. **Crew Cross-Training**: Can Gunner retrain as Engineer?
17. **Crew Achievement Tracking**: Kill counts, battles survived?
18. **Officer Name Generation**: Random or database-driven? Player customizable?

### Detection System (Q19-Q28)

19. **Shadow Misidentification Recovery**: Real-time update when better equipped ally detects?
20. **Phase Transition During Combat**: Solution behavior when target goes Phase 3→2?
21. **Bearing Randomization Frequency**: Per second? Per radar sweep?
22. **Passive Sonar Accuracy**: Single line or 2-3° arc?
23. **Radar Clutter/Chaff**: False contacts in storms? Decoy mechanics?
24. **Visual Detection Through Smoke**: Can visible turrets identify target?
25. **Detection Toggle Spam**: Cooldown between sonar on/off?
26. **Contact Persistence Post-Combat**: Do enemy contacts fade or persist?
27. **Radar vs Sonar Priority**: Single crew monitoring both simultaneously?
28. **Shared Misidentification**: Does ally see sender's error or own data?

### Module System (Q29-Q37)

29. **Module Rotation**: 2×2 module orientation flexibility?
30. **Modular Redundancy**: Dual identical engines advantage?
31. **Cascading Failures**: Adjacent module collateral damage?
32. **Module Cooling**: Deliberate overheating through sustained fire?
33. **Module Warm-Up**: New installation fire delay?
34. **Weapon Interchangeability**: DD turret on cruiser mounting?
35. **Quality Impact on Efficiency**: 70% vs 130% quality effect on formula?
36. **Armor Stacking**: Multiple armor section installations?
37. **Module vs Crew Weight**: Separate calculations or combined budget?

### Economy System (Q38-Q48)

38. **Resource Conversion**: Chromium to Electronics exchange rate?
39. **Port Fee Determinants**: Tier, cargo value, ship size, reputation?
40. **Market Volatility**: Real-time or periodic price calculation?
41. **Black Market Locations**: All ports or secret locations?
42. **Intelligence Valuation**: Who determines initial value?
43. **Crafting Skill Progression**: XP per craft determination?
44. **Player Market Taxes**: Where do fees go? Sink? Nation? Port owner?
45. **Inflation Control**: Server wealth spiral prevention?
46. **Resource Gathering**: Mining operations? Harvesting zones?
47. **Production Facility Ownership**: Individual or guild only?
48. **Trade Route Automation**: Profit model vs manual trading?

### Permadeath System (Q49-Q53)

49. **Recovery Mechanics**: Window length, location, cost, prerequisites?
50. **Insurance Claims**: Auto-pay or submission required? Fraud detection?
51. **Public Announcements**: Server memorial? Legacy impact?
52. **Resurrection Methods**: Any path to recover dead crews?
53. **Partial Ship Survival**: Condition after surviving T6-T9 roll?

### Extraction System (Q54-Q59)

54. **Cargo Capacity**: Weight, volume, or item-count based?
55. **Cargo Visibility Radius**: Same as ship detection or different?
56. **Loot Crate Quantity**: Per HP, per class, or fixed?
57. **Port Security Variance**: Reputation affect cargo safety?
58. **Cargo Insurance**: Available? Cost? Coverage?
59. **Extraction Failure Salvage**: Can sunken cargo be recovered?

### Progression System (Q60-Q64)

60. **Ship Tier Unlock**: Credits only? Reputation? Missions?
61. **Module Tech Trees**: Branching or linear? Nation choice?
62. **Crew Collection Limit**: Max cards? Storage limit?
63. **Post-Permadeath Progression**: Restart from scratch or accelerated?
64. **Achievement System**: Tracking, rewards, bonuses?

### Multiplayer Coordination (Q65-Q70)

65. **Fleet Radar Sharing**: Automatic ally target sharing?
66. **Voice Communication Range**: Bypass 2km radio limit?
67. **Guild Management**: Size, treasury, ranks, shared resources?
68. **Nation Diplomacy Votes**: War declaration mechanics?
69. **Cross-Nation Grouping**: Grouping during active war?
70. **PvP Flagging**: Indicate intent? Go peaceful?

---

## INTEGRATION GAPS

### Major Gaps

| ID | Systems | Issue |
|----|---------|-------|
| I1 | Crew-Module Weight | No interaction explanation between crew weight and module weight budgets |
| I2 | Offline Training + Economy | Training facility fees undefined; free training devalues paid methods |
| I3 | Ammunition + Combat | No mid-combat depletion mechanic; magazine vs cargo undefined |
| I4 | Fuel + Economy | Fuel efficiency vs distance calculation; long-distance trade viability |
| I5 | Permadeath + Insurance | No provider system, claim triggers, cost calculation |
| I6 | Reputation + Economy | "Nation Standing" vs "Reputation" terminology; inheritance after death |
| I7 | Detection + Combat | No "sprint to break contact" mechanic; detection vs engagement range mismatch |
| I8 | Crew Casualty + Combat | No visual feedback; no damage control priority system; no automation explanation |
| I9 | Submarine Sonar + Surface Radar | Can surface ships detect submerged subs? Asymmetrical advantage? |
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

- [ ] `03-Combat-Systems/Firing-Solution-System.md` - Complete firing solution calculation
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

1. Crew-Module Efficiency Formula completion
2. Permadeath Crew Recovery definition
3. Firing Solution Formula alignment
4. Ammunition Storage mechanics
5. Crew Classification contradiction resolution
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
- Crew-module efficiency calculations incomplete
- Permadeath recovery system undefined
- Firing solution formula misaligned
- Ammunition storage system undefined
- Crew classification system contradictory

### Estimated Resolution Time
2-3 weeks of design work (not implementation) for Phase 2 blockers

---

*This document should be updated as mechanics are resolved. Check off items as they are completed.*
