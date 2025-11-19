---
tags: [planned, phase2, core-gameplay, inventory, logistics]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-01-19
---

# Inventory System

## Overview
Tetris-style spatial inventory system providing strategic resource management across ship cargo holds, port storage, and crew organization. The system creates meaningful pre-mission loadout decisions, mid-combat resource awareness, and extraction-phase tension through weight/capacity limits affecting ship performance.

## Implementation Status
**Status**: 📋 **PLANNED** (Phase 2 Priority)
**Phase**: Phase 2
**Scripts**: Not yet implemented
**Priority**: HIGH - Foundational system affecting combat, extraction, economy, and progression

---

## Design Specification

### Core Concept
Fathoms Deep uses a **spatial inventory system** where items occupy grid spaces based on physical size, not arbitrary stack counts. This creates strategic depth in loadout planning, forces meaningful decisions about ammunition vs. cargo capacity, and generates extraction tension when players must choose what loot to keep under fire.

### Key Design Pillars

#### 1. Spatial Tetris Inventory (Not List-Based)
Items occupy physical grid space based on real-world dimensions:
- **5-inch shells**: 1x1 slots, stack to 100 rounds
- **16-inch shells**: 2x3 slots, stack to 20 rounds (massive projectiles)
- **Torpedoes**: 1x6 slots, no stacking (full-size weapons)
- **Aircraft**: 4x8 slots (fighters), 5x10 slots (bombers) - carrier deck space
- **Modules**: Variable sizes (e.g., radar 3x3, turret 4x4)
- **Cargo crates**: 2x2 to 4x4 depending on contents

#### 2. Weight & Volume Affect Performance
Inventory load impacts ship capabilities:
- **Over-capacity**: Ship speed reduced by 5-25% when exceeding optimal load
- **Heavy ammunition loads**: Affects acceleration, not top speed
- **Unbalanced cargo**: Can cause listing (visual effect + slight turn rate penalty)
- **Full extraction**: Heavily loaded ships are slower targets during withdrawal
- **Strategic trade-off**: Combat readiness vs. cargo capacity

#### 3. Ship Class Determines Capacity
Cargo hold size scales with ship class and tier:
- **Destroyers (T1-T10)**: 50-150 grid slots (small, specialized for torpedoes/depth charges)
- **Cruisers (T1-T10)**: 150-300 grid slots (balanced ammunition + moderate cargo)
- **Battleships (T1-T10)**: 200-400 grid slots (massive shell magazines, limited general cargo)
- **Carriers (T1-T10)**: 300-600 grid slots (aircraft + aviation fuel + ordnance)
- **Submarines (T1-T10)**: 40-100 grid slots (extremely limited, torpedo-focused)

#### 4. Port Storage (Unlimited)
Players have unlimited storage at home ports:
- **Warehouse**: Unlimited grid space, ship-specific storage
- **Account Bank**: Shared across all player ships (universal storage)
- **Transfer mechanics**: Drag-and-drop between ship and port
- **Organization tools**: Sort by type, search, auto-stack

---

## Ship Inventory Categories

### 1. Ammunition Storage

#### **Main Battery Shells**
**Organization**: Stored by caliber in dedicated magazines
- **Caliber compatibility**: All guns of same caliber share magazine (e.g., all 5-inch guns pull from same stockpile)
- **Shell types per caliber**: AP, HE, SAP variants stored separately
- **Example loadout (USS Fletcher - T3 Destroyer)**:
  - 5-inch/38 caliber AP: 300 shells (300 slots total)
  - 5-inch/38 caliber HE: 200 shells (200 slots total)
  - Total: 500 grid slots for main battery

**High-Tier Example (USS Iowa - T5 Battleship)**:
- 16-inch AP shells: 100 rounds (600 slots - 2x3 each)
- 16-inch HE shells: 50 rounds (300 slots - 2x3 each)
- 5-inch/38 secondary: 400 rounds (400 slots)
- Total: 1,300 grid slots for guns alone

#### **Torpedoes**
**Organization**: Individual weapons, no stacking
- **Full-size torpedoes**: 1x6 grid slots each
- **Reloads**: Stored in ship's torpedo magazine (limited by ship design)
- **Example (USS Fletcher - T3 Destroyer)**:
  - 10 torpedo tubes (equipped weapons)
  - 6 reload torpedoes (36 grid slots)
  - Total: 16 torpedoes available per sortie

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
**Organization**: Bombs, torpedoes, rockets stored separately
- **500-lb bombs**: 1x2 slots, stack to 10
- **1,000-lb bombs**: 2x2 slots, stack to 5
- **Aerial torpedoes**: 1x4 slots, stack to 5
- **Carrier ammunition management**: Must pre-load aircraft before launch
- **Example (USS Essex - T5 Fleet Carrier)**:
  - 200x 500-lb bombs (40 slots)
  - 100x 1,000-lb bombs (80 slots)
  - 80 aerial torpedoes (64 slots)

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

### 3. Modules & Customization

#### **Module Storage Philosophy**
**Active vs. Reserve Modules**:
- **Equipped modules**: Don't occupy cargo space (installed on ship)
- **Reserve modules**: Occupy cargo space (can be swapped at port)
- **Module swapping**: Can only change modules at port, not mid-sortie
- **Strategic choice**: Carry spare modules for post-battle swaps vs. cargo capacity

#### **Module Size Examples**
- **Fire Control System**: 3x3 slots (10-ton equipment)
- **Radar Module**: 3x3 slots (antenna + electronics)
- **Engine Module**: 6x6 slots (massive machinery replacement)
- **Main Battery Turret**: 4x4 slots per turret (entire gun mount)
- **Secondary Gun Mount**: 2x2 slots
- **Torpedo Tube Bank**: 3x4 slots

#### **Module Carrying Limitations**
**Weight penalties apply**:
- Carrying 1-2 spare modules: -5% ship speed
- Carrying 3-5 spare modules: -15% ship speed
- Carrying 6+ spare modules: -25% ship speed, extremely vulnerable extraction target

**Tactical considerations**:
- **High-tier operations**: Players may carry backup radar if expecting electronic warfare
- **Treasure hunting**: Module cargo space vs. loot capacity trade-off
- **Port runs**: Dedicated "module transport" loadouts with minimal ammunition

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
**Total Cargo Capacity**: 480 grid slots

**Balanced Air Wing Loadout**:
- 24 fighters (F6F Hellcat): 96 slots (4x8 each)
- 18 dive bombers (SBD Dauntless): 90 slots (5x10 each)
- 18 torpedo bombers (TBF Avenger): 90 slots (5x10 each)
- 500-lb bombs: 100 (20 slots)
- 1,000-lb bombs: 50 (40 slots)
- Aerial torpedoes: 40 (32 slots)
- Aviation fuel: 2,000 units (dedicated tank)
- **Total: 368/480 slots - 112 slots free**

**Strike-Heavy Loadout** (Offensive operation):
- 12 fighters: 48 slots (reduced CAP)
- 24 dive bombers: 120 slots
- 24 torpedo bombers: 120 slots
- 500-lb bombs: 200 (40 slots)
- 1,000-lb bombs: 100 (80 slots)
- Aerial torpedoes: 80 (64 slots)
- **Total: 472/480 slots - 8 slots free**

**Defensive Loadout** (Fleet escort):
- 48 fighters: 192 slots (maximum air superiority)
- 6 dive bombers: 30 slots (minimal strike capability)
- 6 torpedo bombers: 30 slots
- 500-lb bombs: 50 (10 slots)
- Aerial torpedoes: 20 (16 slots)
- **Total: 278/480 slots - 202 slots free for loot/supplies**

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
