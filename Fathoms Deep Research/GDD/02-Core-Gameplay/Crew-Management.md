---
tags: [planned, phase2, crew-management, navy-field-inspired, core-system]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-17
---

# Crew Management System

## Overview
The Crew Management System is a Navy Field-inspired card-based progression system where crew cards represent permanent investments that grow with players across ships. Unlike traditional MMOs, crew cards have no ongoing costs - only initial training and battle replenishment. The system creates strategic tension through weight-based constraints that limit high-level crews on small ships, driving natural progression toward larger vessels.

## Implementation Status
**Status**: 📋 PLANNED (designed but not implemented)
**Phase**: Phase 2 - Core Gameplay Systems
**Scripts**: TBD (pending implementation)
**Priority**: HIGH (core Phase 2 feature, fundamental to progression)

---

## Design Specification

### Core Philosophy
The crew system mirrors Navy Field's card-based approach with modern extraction game stakes. Crew cards are **permanent investments** that grow with you across ships, but face **real permadeath risk** in high-tier combat. Unlike traditional MMOs, there are **no ongoing costs** - just initial training and battle replenishment.

**Key Design Pillars:**
- **Permanent Investment**: Crew cards persist across ships and battles
- **No Maintenance Costs**: Zero salaries, upkeep, or morale systems
- **Weight-Based Constraints**: Natural progression gating through physics
- **Permadeath Stakes**: Real risk/reward in high-tier combat (see [[Crew-Permadeath]])
- **Universal Applicability**: Gunners work on ALL turrets, engineers on ALL engines

### Key Features
- **Crew Card System**: Card-based representation of sailor groups (not individuals)
- **Dynamic Sailor Scaling**: Crew size grows with level (10 sailors at L1 → 705 at L200)
- **Weight Management**: Higher-level crew weighs more, limiting small ship usage
- **Position-Based Slots**: Fixed crew positions per ship class (5 slots on DD, 20 on carrier)
- **Free Transfer**: Move crew cards between ships without retraining costs
- **Classification System**: Permanent specialization choices (see [[Crew-Specialization]])
- **Efficiency Mechanics**: Level matching affects performance (see [[Crew-Progression]])

### User Experience
Players acquire neutral Level 1 crew cards at port, assign them to ship positions, and level them through combat or paid training. As crew cards level up, they gain more sailors and weight, eventually becoming too heavy for small ships. Players must strategically manage crew composition to balance effectiveness with weight constraints, creating meaningful decisions about which ships can field veteran crews.

**Player Interaction Flow:**
1. Recruit neutral crew cards at friendly ports
2. Assign cards to ship crew positions (turrets, engines, AA batteries, etc.)
3. Level crew through combat or training
4. Choose permanent classifications at level thresholds
5. Manage weight constraints as crew levels increase
6. Transfer veteran crew to larger ships as you tier up

---

## Technical Implementation

### Current Implementation
**Not yet implemented** - This section is a design specification for Phase 2 development.

### Key Components

#### Crew Card Structure
```
CrewCard {
  - ID: Unique identifier
  - Level: 1-200
  - CurrentSailors: Dynamic based on level and casualties
  - MaxSailors: Dynamic based on level
  - Classification: Neutral/Gunner/Engineer/etc (see Crew-Specialization.md)
  - SpecializationTier: Basic/Advanced/Elite
  - Experience: Current XP progress
  - Weight: Calculated value (SailorCount × 0.1 × LevelModifier)
}
```

#### Sailor Count Scaling Formula
```
Levels 1-50:   10 + (Level - 1) × 5 sailors
Levels 51-100: 255 + (Level - 50) × 4 sailors
Levels 101-150: 455 + (Level - 100) × 3 sailors
Levels 151-200: 605 + (Level - 150) × 2 sailors

Examples:
- Level 1 Neutral: 10 sailors
- Level 20 Gunner: 105 sailors
- Level 50 Engineer: 255 sailors
- Level 100 Master Gunnery Officer: 455 sailors
- Level 200 Elite Gunner: 705 sailors
```

#### Weight System Formula
```
Crew Weight = Sailor Count × Base Weight × Level Modifier

Base Weight: 0.1 ton per sailor
Level Modifier: 1.0 + (Level / 100)

Example Calculations:
- Level 1 (10 sailors):   10 × 0.1 × 1.01 = 1.01 tons
- Level 20 (105 sailors): 105 × 0.1 × 1.20 = 12.6 tons
- Level 50 (255 sailors): 255 × 0.1 × 1.50 = 38.3 tons
- Level 100 (455 sailors): 455 × 0.1 × 2.00 = 91 tons
- Level 200 (705 sailors): 705 × 0.1 × 3.00 = 211.5 tons
```

**Note**: Classification does NOT affect weight - only level and sailor count matter.

#### Ship Crew Position Slot System

| Ship Class | Crew Positions | Weight Limit | Strategic Impact |
|------------|---------------|--------------|------------------|
| T1 Destroyer | 5 positions | 250 tons | Cannot support L150+ crew |
| T3 Light Cruiser | 8 positions | 600 tons | Mid-level crew viable |
| T5 Heavy Cruiser | 12 positions | 1,200 tons | High-level crew emerging |
| T7 Battleship | 15 positions | 1,800 tons | Elite crew viable |
| T10 Carrier | 20 positions | 2,500 tons | Full elite roster possible |

**Position Types Examples:**
- Main Battery Turret #1 (requires Gunner classification)
- Main Battery Turret #2 (requires Gunner classification)
- Secondary Battery (requires Gunner classification)
- AA Battery (requires AA Specialist classification)
- Engine Room (requires Engineer classification)
- Damage Control (requires Engineer classification)
- Radar Station (requires Electronics classification)
- Aircraft Squadron #1 (requires Aviation classification, carriers only)

#### Crew Acquisition Methods
1. **Port Recruitment**: Create new Level 1 neutral crew cards at friendly ports
2. **Battle Drops**: Capture enemy crew cards from defeated ships (rare)
3. **Mission Rewards**: Earn crew cards from campaign missions
4. **Player Trade**: Buy/sell crew cards on player market
5. **Retrieval**: Recover dead crews from battle locations (see [[Crew-Permadeath]])

### Configuration

**Tunable Parameters:**
```
CREW_MAX_LEVEL = 200
CREW_SAILOR_BASE_WEIGHT = 0.1 tons
CREW_LEVEL_MODIFIER = 1.0 + (Level / 100)

// Sailor count scaling breakpoints
SAILOR_SCALING_L1_50 = { base: 10, increment: 5 }
SAILOR_SCALING_L51_100 = { base: 255, increment: 4 }
SAILOR_SCALING_L101_150 = { base: 455, increment: 3 }
SAILOR_SCALING_L151_200 = { base: 605, increment: 2 }

// Ship class crew limits
T1_CREW_SLOTS = 5
T1_CREW_WEIGHT_LIMIT = 250 tons

T3_CREW_SLOTS = 8
T3_CREW_WEIGHT_LIMIT = 600 tons

T5_CREW_SLOTS = 12
T5_CREW_WEIGHT_LIMIT = 1200 tons

T7_CREW_SLOTS = 15
T7_CREW_WEIGHT_LIMIT = 1800 tons

T10_CREW_SLOTS = 20
T10_CREW_WEIGHT_LIMIT = 2500 tons
```

---

## Integration Points

### Depends On
- [[Ship-Stats-System]] - Crew positions tied to ship modules and turrets
- [[Weight-System]] - Crew weight contributes to total ship weight
- [[Port-Services]] - Recruitment and replenishment services
- [[Economy-System]] - Credit costs for training, recruitment, replenishment

### Used By
- [[Crew-Progression]] - XP and leveling mechanics
- [[Crew-Specialization]] - Classification and specialization trees
- [[Crew-Permadeath]] - Death conditions and retrieval mechanics
- [[Combat-System]] - Crew efficiency affects module performance
- [[Casualty-System]] - Battle damage reduces crew sailor counts
- [[Player-Progression]] - Crew cards represent long-term investment

---

## Strategic Gameplay Impact

### Natural Progression Gates

**Weight-Based Restriction:**
High-level crew cards weigh too much for small ships, creating natural progression:
- **T1 Destroyer**: Can't fit Level 150+ crew cards (too heavy)
- **T5 Cruiser**: Can support mix of high/mid-level crew
- **T10 Battleship**: Can field full elite crew rosters (Level 180-200)

**Example: Captain Jones' Over-Leveling Problem**
- Wants Level 150 crew on T3 cruiser
- Level 150 crew card = 9 tons per sailor
- 50-sailor card = 450 tons
- T3 cruiser limit = 600 tons total
- Can only fit 1 high-level crew card
- Must use lower-level crew for other positions
- **Natural incentive to upgrade to larger ship**

### Crew Transfer Strategy

**Unrestricted Transfer System:**
- ✅ Move crew cards between ships **freely**
- ✅ **No retraining costs** when switching ships
- ✅ Gunner works on destroyer AND battleship turrets identically
- ✅ Engineer works on all engine types universally
- ✅ Bring veteran crew to larger ships as you progress

**Player Progression Path:**
1. Start T1 destroyer with fresh Level 1 crew
2. Level crew to 50-75 through T1-T3 combat
3. Upgrade to T5 cruiser, **transfer same crew cards**
4. Continue leveling crew to 100-125 through T5-T7
5. Reach T10 battleship with **elite Level 150+ crew library**

**Multi-Ship Rotation:**
Experienced players maintain multiple ships with shared crew pools:
- High-tier main ship with best crew (Level 150+ elite crews)
- Mid-tier farming ship with backup crew (Level 75-100)
- Low-tier training ship for leveling new crew (Level 1-50)
- Swap crew cards based on mission requirements and risk tolerance

### Economic Design

**No Ongoing Costs Philosophy:**
Unlike traditional MMOs, crew cards have **zero maintenance**:
- ❌ No salaries
- ❌ No upkeep fees
- ❌ No morale systems
- ✅ One-time training costs only (see [[Crew-Progression]])
- ✅ One-time classification unlock costs only (see [[Crew-Specialization]])
- ✅ Battle replenishment costs only when damaged

**Credit Sinks:**
- Initial crew card creation at port
- Combat/training XP purchases
- Classification unlock fees
- Battle casualty replenishment
- High-tier crew insurance (optional)

**Player Economy Integration:**
- Trade high-level crew cards on marketplace
- Sell captured enemy crew cards
- Retrieval profession earnings (see [[Crew-Permadeath]])
- Crew card appraisal services

---

## Example Scenarios

### Scenario 1: New Player Progression
**Captain Murphy starts T1 destroyer**

- Creates 5 neutral Level 1 crew cards at port (100 credits each = 500 total)
- Assigns to ship positions:
  - Main Battery Turret #1: Crew Card A
  - Main Battery Turret #2: Crew Card B
  - Engine Room: Crew Card C
  - AA Battery: Crew Card D
  - Damage Control: Crew Card E
- Fights T1-T2 battles, crew reaches Level 25 (6-8 hours gameplay)
- Total crew weight: ~200 tons (well within T1 DD 250-ton limit)
- Chooses classifications at Level 25:
  - Cards A & B: Gunner classification
  - Card C: Engineer classification
  - Card D: AA Specialist classification
  - Card E: Damage Control classification
- Upgrades to T3 Light Cruiser, **transfers same 5 crew cards** (no retraining cost)
- Crew weight at Level 40: ~350 tons (within T3 CL 600-ton limit)
- Continues progression to T5 Heavy Cruiser with same core crew roster

**Outcome**: Seamless progression without retraining costs or crew replacement.

### Scenario 2: Elite Crew Investment
**Captain Yamamoto operates T8 Battleship**

- Main battery crew card: **Level 180 Master Gunnery Officer**
- Sailor count at L180: 100 sailors
- Weight: 100 × 0.1 × 2.8 = **28 tons**
- Wait, this seems wrong. Let me recalculate...
- Level 180 sailor count: 605 + (180 - 150) × 2 = 665 sailors
- Weight: 665 × 0.1 × 2.8 = **186 tons** for ONE crew card
- Can only fit on T7+ ships (weight restriction)
- Provides 125% efficiency on Level 120 turrets (over-leveling bonus)
- **Investment**: 400+ hours of combat + 5M credits training
- Fights in T8 zones (40% crew card permadeath risk per card)
- **Ship destroyed in battle** → 40% chance crew card dies forever
- **Card survives** → transfers to replacement T8 battleship
- **Sailor casualties separate** → even surviving cards lose sailors (replaceable)
- Represents months of investment at risk

**Outcome**: High-risk, high-reward gameplay for veteran players.

### Scenario 3: Multi-Ship Crew Management
**Captain Schmidt maintains 3 ships**

**T10 Battleship (Main Ship):**
- 8 crew positions filled with Level 150-180 elite crews
- Total weight: ~1,400 tons (crew alone)
- Used for high-stakes T9-T10 operations
- Crews at risk of permadeath

**T5 Cruiser (Farming Ship):**
- 6 crew positions filled with Level 75-100 backup crews
- Total weight: ~550 tons (crew)
- Used for safer T4-T5 credit farming
- No permadeath risk in these tiers

**T2 Destroyer (Training Ship):**
- 5 crew positions filled with Level 1-25 trainee crews
- Total weight: ~80 tons (crew)
- Used to level new crew cards safely
- Sells leveled crews on player market

**Strategy**: Rotates crews based on mission risk, maintains elite crew library for high-tier operations while farming credits with backup crews.

---

## Known Issues
- **None (design phase)** - Not yet implemented

## Future Enhancements
- **Crew Portraits**: Visual customization for crew cards
- **Crew Backgrounds**: Historical flavor text and nation-specific traits
- **Crew Medals**: Achievement tracking for veteran crews (battles survived, kills, etc.)
- **Crew Quarters Module**: Ship upgrade that increases crew position slots
- **Crew Training Facilities**: Player-owned port buildings for XP bonuses
- **Crew Academies**: Nation-specific training bonuses for certain classifications

---

## Cross-References
- [[Crew-Progression]] - XP system, leveling, and efficiency mechanics
- [[Crew-Specialization]] - Classification trees and specialization paths
- [[Crew-Permadeath]] - Death conditions, retrieval system, and risk scaling
- [[Ship-Stats-System]] - How crew integrates with ship modules
- [[Weight-System]] - Ship weight limits and balance
- [[Port-Services]] - Recruitment and replenishment services
- [[Combat-System]] - How crew affects battle performance
- [[Economy-System]] - Credit costs and player trading

---

## Testing

### Test Coverage
- [ ] Crew card creation and sailor count scaling
- [ ] Weight calculation and ship limit enforcement
- [ ] Position slot assignment and restrictions
- [ ] Free transfer between ships
- [ ] Weight impact on ship performance
- [ ] Multi-ship crew rotation workflows
- [ ] Player market trading
- [ ] Performance with 100+ crew cards per player

### Test Results
Not yet implemented - testing pending Phase 2 development.

---

## Changelog
- **2025-11-17**: Initial design document created from GDD_Updated-1.md (lines 162-516)
