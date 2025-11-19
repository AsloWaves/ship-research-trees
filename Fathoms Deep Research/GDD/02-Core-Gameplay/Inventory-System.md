---
tags: [planned, phase2, core-gameplay, inventory, logistics]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-01-19
---

# Inventory System

## Overview
Tetris-style spatial inventory system with **unified cargo management** where all items (ammunition, modules, fuel, loot) share a single ship inventory. Players manage both **grid capacity** (spatial slots) and **weight capacity** (tonnage budget) determined by ship design and armor loadout. The system creates meaningful pre-mission loadout decisions, mid-combat resource awareness, and extraction-phase tension through dual capacity constraints affecting ship performance.

## Implementation Status
**Status**: 📋 **PLANNED** (Phase 2 Priority)
**Phase**: Phase 2
**Scripts**: Not yet implemented
**Priority**: HIGH - Foundational system affecting combat, extraction, economy, and progression

---

## Design Specification

### Core Concept
Fathoms Deep uses a **unified spatial inventory system** where all items share a single cargo hold—no separate magazines, fuel tanks, or module bays. Items occupy grid spaces based on physical size, and players must balance both **spatial capacity** (grid slots) and **weight capacity** (tonnage) determined by ship construction. A heavily armored battleship has the same grid space as a lightly armored one, but significantly less weight budget. This creates strategic depth in loadout planning, forces meaningful decisions about ammunition vs. cargo vs. fuel, and generates extraction tension when players must choose what loot to keep under fire.

### Key Design Pillars

#### 1. Spatial Tetris Inventory (Not List-Based)
Items occupy physical grid space based on real-world dimensions:
- **Small shells (5-inch)**: 1x1 slots, stack to 100 rounds
- **Large shells (16-inch)**: 1x2 slots, stack to 50 rounds
- **Torpedoes**: 1x3 to 1x4 slots depending on type, no stacking
- **Fighters**: 3x3 slots (compact folding wings)
- **Bombers**: 3x4 slots (larger airframe)
- **Modules**: Varied sizes (1x1 starter radar, 2x3 engine, 3x3 advanced radar, etc.)
- **Cargo crates**: 2x2 to 4x4 depending on contents
- **Fuel barrels**: 1x1 slots, stack to 100 units

#### 2. Dual Capacity System - Grid Space & Weight Budget
Ships have **two separate limits** that both constrain loadout:

**Grid Capacity (Spatial Slots)**:
- Fixed number of inventory grid slots per ship
- Determined by ship hull design (cargo hold size)
- Example: Destroyer might have 120 grid slots, Battleship 300 slots
- Items must fit spatially in the grid (Tetris puzzle)

**Weight Capacity (Tonnage Budget)**:
- Total weight limit in tons that ship can carry
- **Varies by armor/equipment**: Heavily armored ships have less weight budget
- **Hard cap**: Cannot exceed maximum weight (like turret mount limits)
- Example: Heavy armor battleship might have 400 tons capacity, light armor version 600 tons
- Each item has weight: shells (0.1 tons each), torpedoes (2 tons each), modules (5-20 tons), fuel (0.01 tons per unit)

**Auto-Balancing**:
- Players do NOT manually balance cargo left/right
- System automatically distributes weight for optimal ship balance
- No listing penalties from poor cargo placement

**Performance Impact**:
- **Weight affects**: Max speed, acceleration, turn radius
- **Grid capacity affects**: What you can physically carry
- **Strategic depth**: Must optimize BOTH constraints simultaneously

#### 3. Per-Ship Capacity (Not Standardized)
Each ship has **individual grid and weight capacity** determined by its specific design:

**Ship-to-Ship Variation**:
- **Same tier, different capacity**: Two T5 destroyers may have different grid/weight limits
- **Design trade-offs**: Fast destroyer has less cargo, cargo-focused destroyer has less speed
- **Armor variants**: Heavy armor reduces weight capacity, light armor increases it
- **Diversity**: Prevents "one best ship" meta, creates meaningful ship choice

**Example Comparison (T5 Destroyers)**:
- **USS Fletcher** (balanced): 120 grid slots, 200 tons weight capacity
- **USS Sumner** (firepower-focused): 100 grid slots, 180 tons (heavier guns reduce cargo)
- **USS Gearing** (endurance-focused): 150 grid slots, 250 tons (larger hull, more cargo)

**General Capacity Ranges by Class**:
- **Destroyers**: 80-160 grid slots, 150-300 tons
- **Cruisers**: 150-350 grid slots, 300-600 tons
- **Battleships**: 200-500 grid slots, 400-800 tons (less weight due to heavy armor)
- **Carriers**: 300-700 grid slots, 500-1000 tons (aircraft + ordnance dominant)
- **Submarines**: 40-120 grid slots, 80-200 tons (extremely cramped)

#### 4. Port Storage (Limited, Per-Port)
Players have **limited storage at each port** to prevent hoarding:

**Per-Port Warehouse**:
- **Limited capacity**: Each port has 500-1000 grid slots (prevents infinite hoarding)
- **Separate inventories**: Storage at Port A is different from Port B
- **Trading gameplay**: Must physically transport goods between ports for profit
- **Strategic decisions**: Which ports to use as storage hubs?

**No Account Bank**:
- **No universal storage** shared across all ships/ports
- Forces meaningful choices about what to keep/sell
- Creates "full warehouse" pressure to use or sell items
- Encourages trading and economy participation

**Transfer Mechanics**:
- **Drag-and-drop**: Move items between ship and current port
- **Organization tools**: Sort by type, weight, value, size
- **Auto-stack**: Combine partial stacks automatically

---

## Unified Ship Inventory - Item Types

**IMPORTANT**: Ships have **ONE single inventory** shared by all items. There are NO separate magazines, fuel tanks, or module bays. Players must manage ammunition, fuel, modules, loot, and cargo all in the same grid space and weight budget.

### Item Type Reference

This section describes the different **types of items** that occupy the unified inventory, not separate storage areas.

---

### 1. Ammunition

#### **Main Battery Shells**
**Grid Size & Weight**:
- **Small caliber (4-6 inch)**: 1x1 grid slot, 0.05 tons each, stack to 100
- **Medium caliber (8-10 inch)**: 1x1 grid slot, 0.15 tons each, stack to 50
- **Large caliber (12-14 inch)**: 1x2 grid slots, 0.5 tons each, stack to 50
- **Super-heavy caliber (16-18 inch)**: 1x2 grid slots, 1.0 ton each, stack to 50
- **Caliber compatibility**: All guns of same caliber share ammunition pool
- **Shell types**: AP, HE, SAP variants stack separately

**Example Loadout (USS Fletcher - T3 Destroyer, 120 grid slots, 200 tons)**:
- 5-inch AP: 200 shells (2 stacks = 2 grid slots, 10 tons)
- 5-inch HE: 200 shells (2 stacks = 2 grid slots, 10 tons)
- **Total shells: 4 grid slots, 20 tons**

**High-Tier Example (USS Iowa - T5 Battleship, 300 grid slots, 500 tons)**:
- 16-inch AP shells: 100 rounds (2 stacks = 4 grid slots, 100 tons)
- 16-inch HE shells: 50 rounds (1 stack = 2 grid slots, 50 tons)
- 5-inch secondary HE: 200 rounds (2 stacks = 2 grid slots, 10 tons)
- **Total shells: 8 grid slots, 160 tons** (weight-constrained, not grid-constrained)

#### **Torpedoes**
**Grid Size & Weight**:
- **Standard torpedoes** (destroyers, submarines): 1x3 grid slots, 2 tons each
- **Long Lance torpedoes** (IJN special): 1x4 grid slots, 3 tons each
- **Aerial torpedoes** (carrier aircraft): 1x3 grid slots, 1.5 tons each
- **No stacking**: Each torpedo occupies full grid space individually

**Example (USS Fletcher - T3 Destroyer, 120 grid slots, 200 tons)**:
  - 10 torpedo tubes (equipped, don't use cargo)
  - 6 reload torpedoes in cargo (18 grid slots, 12 tons)
  - Total ammunition: 16 torpedoes available per sortie

#### **Anti-Aircraft Ammunition**
**Organization**: Automatic consumption from magazine
- **AA shells**: 1x1 slots, stack to 500 rounds per stack
- **High consumption rate**: 100-300 rounds per air engagement
- **Auto-supply**: AA guns pull from magazine automatically during combat
- **Example (Light Cruiser AA loadout)**:
  - 2,000 rounds 40mm Bofors (4 stacks = 4 slots)
  - 5,000 rounds 20mm Oerlikon (10 stacks = 10 slots)

#### **Depth Charges (Anti-Submarine Warfare)**
**Organization**: Individual weapons, stackable to 20
- **Depth charge size**: 1x2 grid slots per stack
- **ASW destroyers**: Typically carry 40-60 depth charges (4-6 slots)
- **Pattern drops**: Expend 4-8 charges per attack run

#### **Aircraft Ordnance (Carriers Only)**
**Grid Size & Weight**:
- **500-lb bombs**: 1x1 slots, 0.25 tons each, stack to 20
- **1,000-lb bombs**: 1x2 slots, 0.5 tons each, stack to 10
- **Aerial torpedoes**: 1x3 slots, 1.5 tons each, no stacking
- **Rockets**: 1x1 slots, 0.1 tons each, stack to 50
- **Carrier ordnance management**: Pre-loaded onto aircraft before launch, stored in unified cargo

**Example (USS Essex - T5 Fleet Carrier, 500 grid slots, 700 tons)**:
  - 200x 500-lb bombs (10 stacks = 10 grid slots, 50 tons)
  - 100x 1,000-lb bombs (10 stacks = 20 grid slots, 50 tons)
  - 60 aerial torpedoes (180 grid slots, 90 tons)

---

### 2. Consumables & Equipment

#### **Damage Control Consumables**
**Cooldown-based items with limited charges**:
- **Damage Control Party**: Instant fire/flood extinguish (90-second cooldown, infinite uses)
- **Repair Party**: Hull repair over time (120-second cooldown, 3 charges per sortie)
- **Engine Boost**: Temporary speed increase (180-second cooldown, 2 charges)
- **Smoke Generator**: Deploy smoke screen (160-second cooldown, 3 charges)

**Inventory Impact**: Consumables don't occupy cargo space (built-in ship systems), but require **fuel** to operate:
- Each consumable use consumes 5-10 fuel units
- Limits consumable spam during prolonged engagements

#### **Countermeasure Equipment**
**Active defensive systems**:
- **Chaff Launchers**: Radar jamming (slots: 2x2, 20 charges)
- **Flares**: IR decoys for homing torpedoes (slots: 1x1, 50 charges)
- **Sonar Decoys**: Deploy false acoustic signatures (slots: 2x3, 10 charges)

---

### 3. Modules & Equipment

#### **Module System - Installed or Not**
Modules have **only two possible states**:
- **Installed**: Module is equipped on the ship, fully functional, occupies a module slot (NOT cargo space)
- **Not Installed**: Module is stored in ship's cargo hold or port warehouse

**Critical Rules**:
- **Cannot swap mid-mission**: Module changes can ONLY be done at port
- **Loot modules**: Finding a module as loot requires bringing it back to port to install
- **No hot-swapping**: Once you leave port, your modules are locked until you return

#### **Ship Module Slots - Size-Specific**
Each ship has predefined **module slots** with specific size requirements:
- **Radar Slot**: 1x1 (starter radar) OR 3x3 (advanced radar)
- **Engine Slot**: 2x3 (standard engine) OR 3x4 (upgraded engine)
- **Fire Control Slot**: 2x2 (basic) OR 3x3 (advanced)
- **Secondary Systems**: Various sizes (1x1 to 2x2)

**Slot matching requirement**:
- A 1x1 radar slot can ONLY fit 1x1 radars
- A 2x3 engine slot can ONLY fit 2x3 engines
- Cannot install oversized modules in smaller slots
- Cannot install undersized modules in larger slots (no adapters)

#### **Module Grid Sizes & Weights**
When stored in cargo (not installed):
- **Starter Radar** (1x1): 1x1 grid slots, 2 tons
- **Advanced Radar** (3x3): 3x3 grid slots, 12 tons
- **Fire Control** (2x2): 2x2 grid slots, 8 tons
- **Standard Engine** (2x3): 2x3 grid slots, 15 tons
- **Upgraded Engine** (3x4): 3x4 grid slots, 25 tons
- **Turret Module** (varies): 2x2 to 4x4, 10-30 tons

**Carrying uninstalled modules**:
- Modules in cargo use grid space AND weight capacity
- Heavy modules can significantly reduce weight budget
- Players might loot valuable modules but lack cargo space to carry them

---

### 4. Resources & Trade Goods

#### **Fuel**
**Critical resource for extended operations**:
- **Fuel capacity**: Dedicated fuel tank (not cargo space)
- **Destroyer fuel tanks**: 500-1,000 units (10-20 hours operation)
- **Battleship fuel tanks**: 2,000-5,000 units (40-100 hours operation)
- **Carrier fuel tanks**: 3,000-8,000 units (60-160 hours operation + aircraft operations)
- **Submarine fuel tanks**: 400-1,200 units (8-24 hours operation)

**Fuel consumption**:
- **Transit speed**: 5-10 fuel units/hour at cruising speed
- **Combat speed**: 15-30 fuel units/hour at flank speed
- **Aircraft operations (carriers)**: +10 fuel units per wing launch
- **Consumable use**: 5-10 fuel units per consumable activation

#### **Repair Materials**
**Portable repair supplies**:
- **Steel Plates**: 2x2 slots, used for hull repairs (10 plates = 1,000 HP repair)
- **Electrical Components**: 1x1 slots, used for module repairs
- **Damage Control Supplies**: 2x1 slots, improves fire/flood repair effectiveness

**Strategic use**:
- Can perform **field repairs** at friendly ports (not home port)
- Carrying repair materials reduces cargo capacity but enables extended operations
- High-tier players carry minimal repair supplies, rely on extraction discipline

#### **Trade Goods & Loot**
**Extraction-based economy items**:
- **Resource Crates**: 2x2 to 4x4 slots depending on value
- **Intelligence Documents**: 1x1 slots (high value, low weight)
- **Salvaged Modules**: Variable sizes (2x2 to 6x6)
- **Rare Materials**: 1x1 to 2x2 slots (precious metals, advanced alloys)

**Loot priority system**:
- Players must decide what to keep when cargo full
- Can **jettison cargo** mid-combat to reduce weight (lost forever)
- Extraction tension: "Do I drop ammunition to carry more loot?"

---

### 5. Crew Cards

#### **Crew Card Storage**
**Physical items representing sailors**:
- **Active crew**: Assigned to ship, don't occupy cargo (crew quarters)
- **Reserve crew**: Occupy cargo space (1 slot per crew card)
- **Recruitment cards**: New sailors recruited at ports (stored in cargo until assigned)

**Crew capacity limits**:
- **Destroyer**: 50-125 active crew positions
- **Cruiser**: 100-250 active crew positions
- **Battleship**: 150-300 active crew positions
- **Carrier**: 200-400 active crew positions (includes aviation personnel)

**Reserve crew carrying**:
- Players can carry **backup crew cards** for high-stakes operations
- Reserve crew occupy 1 cargo slot per card
- If active crew member dies (permadeath at T6+), can **promote reserve crew** at port
- Strategic choice: Carry insurance crew vs. cargo capacity

**Example (T8 Battleship with 250 active crew)**:
- 250 active crew (no cargo space)
- 20 reserve crew cards (20 cargo slots)
- Protects against permadeath crew losses during high-risk operations

---

## Port Storage System

### 1. Warehouse (Ship-Specific Storage)

#### **Unlimited Grid Space**
- **Per-ship storage**: Each ship has dedicated unlimited warehouse at home port
- **Organization**: Same grid system as ship inventory
- **Access**: Only accessible when ship is docked at home port
- **Purpose**: Long-term ammunition stockpiles, module collection, spare crew

#### **Transfer Mechanics**
- **Drag-and-drop**: Move items between ship and warehouse
- **Auto-stack**: Click to automatically combine partial stacks
- **Quick-load presets**: Save ammunition loadouts for quick pre-mission prep
- **Weight warnings**: UI shows when ship is over-capacity

### 2. Account Bank (Universal Storage)

#### **Shared Across All Ships**
- **Account-wide**: All player ships can access same bank
- **Unlimited capacity**: No grid limit
- **Transfer between ships**: Move modules/crew/loot between different ships
- **Global access**: Available at any friendly port (not just home port)

**Strategic uses**:
- Transfer high-value loot from combat ship to trader ship
- Share elite crew cards between ships
- Store rare modules for future ship upgrades

### 3. Module Workshop

#### **Module Modification Station**
- **Upgrade modules**: Improve stats using resources + credits
- **Repair damaged modules**: Restore modules damaged during combat
- **Module crafting**: Combine components to create advanced modules
- **Research tree**: Unlock new module types through R&D

---

## Tactical Loadout Examples

### Destroyer Loadout (USS Fletcher - T3)
**Total Cargo Capacity**: 120 grid slots

**Combat-Focused Loadout**:
- 5-inch AP shells: 300 rounds (300 slots) ❌ OVERFLOW
- 5-inch HE shells: 200 rounds (200 slots) ❌ OVERFLOW

**Balanced Loadout**:
- 5-inch AP shells: 150 rounds (150 slots) ❌ OVERFLOW
- 5-inch HE shells: 100 rounds (100 slots)
- Torpedoes (reloads): 6 (36 slots) ❌ OVERFLOW
- Depth charges: 40 (4 slots)
- Repair materials: 5 steel plates (20 slots)
- **Total: 160 slots - OVER CAPACITY**

**Optimized Combat Loadout**:
- 5-inch AP shells: 100 rounds (100 slots)
- 5-inch HE shells: 80 rounds (80 slots)
- Torpedoes (reloads): 4 (24 slots)
- Depth charges: 20 (2 slots)
- Fuel: Full tank (500 units - dedicated fuel tank, not cargo)
- **Total: 106/120 slots - 14 slots free for loot**

**Extraction-Focused Loadout** (After successful loot run):
- 5-inch HE shells: 50 rounds (50 slots) - Minimal defensive ammo
- Torpedoes (reloads): 0 (0 slots) - All fired
- Salvaged modules: 2x high-value radars (18 slots)
- Resource crates: 8 crates (32 slots)
- Intelligence documents: 10 (10 slots)
- **Total: 110/120 slots - Racing to extract**

---

### Battleship Loadout (USS Iowa - T5)
**Total Cargo Capacity**: 350 grid slots

**Full Combat Loadout**:
- 16-inch AP shells: 80 rounds (480 slots) ❌ OVERFLOW
- 16-inch HE shells: 40 rounds (240 slots) ❌ OVERFLOW
- 5-inch secondary: 300 rounds (300 slots) ❌ OVERFLOW

**Realistic Combat Loadout**:
- 16-inch AP shells: 60 rounds (360 slots) ❌ OVERFLOW

**Optimized Loadout**:
- 16-inch AP shells: 40 rounds (240 slots)
- 16-inch HE shells: 20 rounds (120 slots)
- 5-inch secondary HE: 150 rounds (150 slots)
- AA ammunition: 1,000 rounds (2 slots - highly compressed)
- Repair materials: 10 steel plates (40 slots)
- Fuel: Full tank (4,000 units)
- **Total: 342/350 slots - 8 slots free**

**Strategic considerations**:
- Battleships are **ammunition-limited** due to massive shell size
- 60 total main battery rounds = 20 salvos (9 guns × 3 rounds per salvo)
- Must conserve ammunition, avoid wasteful fire
- Heavily penalizes poor gunnery (stat-based accuracy matters!)

---

### Carrier Loadout (USS Essex - T5)
**Total Capacity**: 500 grid slots, 700 tons weight capacity

**Balanced Air Wing Loadout**:
- 30 fighters (F6F Hellcat): 270 slots (3x3 each), 150 tons
- 20 dive bombers (SBD Dauntless): 240 slots (3x4 each), 120 tons
- 20 torpedo bombers (TBF Avenger): 240 slots (3x4 each), 140 tons
- **Aircraft subtotal: 750 slots, 410 tons** ❌ OVER GRID CAPACITY

**Optimized Balanced Loadout**:
- 20 fighters: 180 slots (3x3 each), 100 tons
- 12 dive bombers: 144 slots (3x4 each), 72 tons
- 12 torpedo bombers: 144 slots (3x4 each), 84 tons
- 200x 500-lb bombs: 10 slots (10 stacks), 50 tons
- 50x 1,000-lb bombs: 10 slots (5 stacks), 25 tons
- 30 aerial torpedoes: 90 slots, 45 tons
- Fuel: 1,000 units (10 slots), 10 tons
- **Total: 478/500 slots, 386/700 tons** ✅ 22 slots free

**Strike-Heavy Loadout** (Offensive operation):
- 12 fighters: 108 slots, 60 tons (reduced CAP)
- 18 dive bombers: 216 slots, 108 tons
- 18 torpedo bombers: 216 slots, 126 tons
- 400x 500-lb bombs: 20 slots, 100 tons
- 100x 1,000-lb bombs: 20 slots, 50 tons
- 60 aerial torpedoes: 180 slots, 90 tons
- Fuel: 800 units (8 slots), 8 tons
- **Total: 568/500 slots** ❌ OVER CAPACITY - Must reduce aircraft

**Strike-Heavy (Adjusted)**:
- 10 fighters: 90 slots, 50 tons
- 15 dive bombers: 180 slots, 90 tons
- 15 torpedo bombers: 180 slots, 105 tons
- 300x 500-lb bombs: 15 slots, 75 tons
- 80x 1,000-lb bombs: 16 slots, 40 tons
- 50 aerial torpedoes: 150 slots, 75 tons
- Fuel: 800 units (8 slots), 8 tons
- **Total: 489/500 slots, 443/700 tons** ✅ 11 slots free

---

## Weight & Performance Impact

### Speed Penalties by Load Percentage

**Optimal Load (0-80% capacity)**:
- **Speed**: 100% (no penalty)
- **Acceleration**: 100%
- **Turn rate**: 100%
- **Fuel efficiency**: 100%

**Heavy Load (80-100% capacity)**:
- **Speed**: 95% (-5% max speed)
- **Acceleration**: 90% (-10% slower acceleration)
- **Turn rate**: 95% (-5% turn rate)
- **Fuel efficiency**: 110% (+10% fuel consumption)

**Over-Capacity (100-120%)**:
- **Speed**: 85% (-15% max speed)
- **Acceleration**: 70% (-30% slower acceleration)
- **Turn rate**: 85% (-15% turn rate)
- **Fuel efficiency**: 125% (+25% fuel consumption)
- **Warning**: Ship lists visually, HUD shows over-capacity warning

**Extreme Over-Capacity (120%+)**:
- **Speed**: 75% (-25% max speed)
- **Acceleration**: 50% (-50% slower acceleration)
- **Turn rate**: 75% (-25% turn rate)
- **Fuel efficiency**: 150% (+50% fuel consumption)
- **Critical**: Ship severely listing, combat effectiveness impaired
- **Extraction risk**: Extremely vulnerable, can't outrun pursuers

### Unbalanced Cargo Effects

**Port/Starboard Imbalance**:
- Ships visually list to heavier side (3-8° tilt)
- Turn rate penalty: -5% when turning into heavy side, +5% when turning away
- UI indicator shows cargo balance status
- **Solution**: Redistribute cargo or use ballast tanks (consumes 50 fuel units to auto-balance)

---

## Extraction Mechanics & Inventory Tension

### 1. Combat Damage Reduces Capacity

**Module destruction reduces usable cargo space**:
- **Magazine fire**: 10-30% cargo capacity lost (ammunition destroyed)
- **Hull flooding**: 5-15% cargo capacity lost (compartments sealed)
- **Structural damage**: Cannot access damaged cargo holds until repaired

**Example scenario**:
- USS Fletcher starts with 120 slots
- Takes magazine hit → loses 20 slots
- Effective capacity: 100 slots
- Must jettison 20 slots of cargo to continue operating

### 2. Mid-Combat Cargo Decisions

**Jettison cargo to reduce weight**:
- **Emergency speed boost**: Drop heavy cargo to increase speed by 10-15%
- **Irreversible**: Jettisoned items are lost forever
- **Priority decisions**: Drop ammunition? Loot? Modules?
- **Tactical use**: Dump empty shell casings (abstract representation) for minor speed boost

**Example scenario (Extraction under fire)**:
- Heavy cruiser loaded with 280/300 slots (loot + ammunition)
- Engaged by two destroyers during extraction
- Speed: 85% (heavy load penalty)
- Decision: Drop 50 slots of loot to reach 230/300 (optimal load)
- Result: Speed increases to 100%, successfully extracts with reduced loot

### 3. Permadeath & Cargo Loss

**Tier-based cargo loss on death**:
- **T1-T5**: Ship recovered, 20-40% cargo lost (randomized)
- **T6**: 10% ship permadeath, full cargo loss on permadeath
- **T7**: 20% ship permadeath, full cargo loss on permadeath
- **T8**: 40% ship permadeath, full cargo loss on permadeath
- **T9**: 60% ship permadeath, full cargo loss on permadeath
- **T10**: 100% ship permadeath, ALL cargo permanently lost

**Creates meaningful risk/reward**:
- High-value loot operations become high-stakes gambling
- Players must weigh "one more engagement" vs. "extract now"
- Extraction tension is highest when cargo hold is full

---

## Crew Stat Integration

### Engineer Classification - Inventory Efficiency

**Repair Speed Stat (7-50)** affects:
- **Module installation time** (at port): Stat 7 = +25% time, Stat 50 = -60% time
- **Cargo loading speed** (at port): Stat 7 = +25% time, Stat 50 = -60% time
- **Field repair material effectiveness**: Stat 50 makes repair materials 105% more effective

### Scavenger/Salvage Classification (If Implemented)

**Potential future crew classification**:
- **Loot Identification**: Higher stat = identify valuable loot faster
- **Salvage Efficiency**: Reduces time to salvage wrecks
- **Cargo Optimization**: Tetris-style auto-arrange cargo for better space usage
- **Weight Distribution**: Auto-balance cargo to prevent listing

---

## UI/UX Design Considerations

### Inventory Grid Interface

**Visual clarity**:
- **Grid overlay**: Clear demarcation of slots
- **Item icons**: Recognizable silhouettes for quick identification
- **Color coding**: Ammunition (red), modules (blue), loot (yellow), crew (green)
- **Stack numbers**: Display stack count on stackable items
- **Weight bar**: Shows current load percentage with color coding (green/yellow/red)

**Quality-of-life features**:
- **Auto-sort**: Sort by type, size, value
- **Quick-stack**: Combine all partial stacks with one click
- **Search/filter**: Find specific items quickly
- **Loadout presets**: Save and load predefined ammunition loadouts
- **Comparison tooltips**: Hover to compare module stats

### In-Combat Inventory Awareness

**Minimal HUD elements**:
- **Ammunition counter**: Current magazine count for active weapon
- **Torpedo counter**: Remaining torpedoes (equipped + reloads)
- **Weight indicator**: Small bar showing cargo load percentage
- **Capacity warning**: Red indicator when approaching/exceeding capacity

**Full inventory access disabled in combat**:
- Cannot reorganize cargo during combat
- Can only jettison cargo (emergency button)
- Prevents inventory micro-management during action

---

## Strategic Depth & Player Decisions

### Pre-Mission Loadout Planning

**Question players must answer**:
1. **Ammunition focus**: AP-heavy for battleship hunting, or HE-heavy for destroyers?
2. **Consumable count**: Carry extra repair materials for extended operations?
3. **Module insurance**: Bring backup radar for electronic warfare zones?
4. **Crew reserves**: Carry reserve crew cards for permadeath protection (T6+)?
5. **Loot capacity**: Leave cargo space free for extraction loot?

### Mid-Mission Adaptability

**Dynamic decision-making**:
- **Ammunition conservation**: Realize you're running low, switch to selective fire
- **Cargo triage**: Loot priority when cargo fills up mid-mission
- **Weight management**: Drop non-essential items to improve combat performance
- **Emergency extraction**: Jettison everything except fuel to escape

### Post-Combat Extraction

**Extraction risk calculation**:
- **High-value cargo**: Valuable loot increases incentive to extract immediately
- **Ammunition depletion**: Low ammunition forces extraction even if cargo not full
- **Damaged ship**: Reduced capacity makes extraction urgent
- **Enemy presence**: Must weigh "loot one more wreck" vs. "extract now"

---

## Integration with Other Systems

### Combat Systems Integration
- **Ammunition consumption** tracked in real-time during gunnery
- **Torpedo tube reloads** pull from cargo inventory
- **Module damage** can destroy cargo (magazine explosions)
- **AA ammunition** auto-consumed during air defense

### Extraction System Integration
- **Cargo capacity** determines loot potential
- **Weight penalties** affect escape speed
- **Permadeath risk** creates cargo loss tension
- **Jettison mechanics** enable emergency escapes

### Economy System Integration
- **Trade goods** require cargo capacity
- **Resource transport** missions involve cargo optimization
- **Port trading** uses port storage system
- **Module market** requires inventory space for purchases

### Progression System Integration
- **Module unlocks** require inventory space to carry
- **Crew recruitment** needs cargo space for crew cards
- **Ship upgrades** may increase base cargo capacity
- **Tier progression** unlocks larger cargo holds

---

## Cross-Reference Documents

**Related Core Gameplay**:
- [[Crew-Management]] - Crew card storage and reserve crew mechanics
- [[Crew-Skills]] - Engineer stats affecting inventory efficiency
- [[Ship-Physics]] - Weight/capacity effects on ship performance

**Related Combat Systems**:
- [[Damage-Model]] - Module damage affecting cargo capacity
- [[Surface-Combat]] - Ammunition consumption mechanics
- [[Carrier-Operations]] - Aircraft and ordnance storage
- [[Submarine-Warfare]] - Limited cargo capacity constraints

**Related Extraction/Economy** (Future documents):
- Extraction-Mechanics - Cargo loss on death, jettison tactics
- Economy-Overview - Trade goods, loot values, port trading
- Progression-System - Cargo capacity unlocks, module progression

---

## Implementation Priority

**Phase 2 Development Focus**:

**Priority 1 - Core Inventory System**:
1. Grid-based inventory UI with drag-and-drop
2. Ship cargo hold capacity by class/tier
3. Ammunition storage and consumption tracking
4. Weight/volume effects on ship performance
5. Port warehouse unlimited storage

**Priority 2 - Cargo Management**:
6. Module storage and swapping at port
7. Crew card inventory system
8. Loot/trade goods inventory
9. Jettison cargo mechanics
10. Over-capacity warnings and penalties

**Priority 3 - Advanced Features**:
11. Loadout preset saving/loading
12. Auto-balance cargo weight
13. Tetris auto-arrange algorithms
14. Advanced inventory filters/search
15. Module workshop integration

**Critical Success Factors**:
- Intuitive drag-and-drop interface feels responsive
- Weight/capacity penalties are noticeable but not punishing
- Pre-mission loadout decisions feel meaningful
- Extraction cargo tension creates memorable "do I stay or go?" moments
- System integrates seamlessly with combat ammunition consumption

---

This comprehensive inventory system creates strategic depth through meaningful pre-mission planning, mid-combat resource awareness, and extraction-phase tension where every slot in your cargo hold could mean the difference between profit and permadeath.
