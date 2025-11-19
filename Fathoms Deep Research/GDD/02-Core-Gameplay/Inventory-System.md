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
- **Standard torpedoes** (destroyers, submarines): 1x3 grid slots, 2 tons each, **stack to 5**
- **Long Lance torpedoes** (IJN special): 1x4 grid slots, 3 tons each, **stack to 5**
- **Aerial torpedoes** (carrier aircraft): 1x3 grid slots, 1.5 tons each, **stack to 5**
- **Limited stacking**: Small stacks due to physical size

**Example (USS Fletcher - T3 Destroyer, 120 grid slots, 200 tons)**:
  - 10 torpedo tubes (equipped, don't use cargo)
  - 10 reload torpedoes in cargo (2 stacks of 5 = 6 grid slots, 20 tons)
  - Total ammunition: 20 torpedoes available per sortie

#### **Anti-Aircraft Ammunition**
**Organization**: Automatic consumption from cargo inventory
- **AA shells**: 1x1 slots, stack to 500 rounds per stack
- **High consumption rate**: 100-300 rounds per air engagement
- **Auto-supply**: AA guns pull from cargo automatically during combat
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
**Grid Size & Weight** (stored in unified inventory, NOT dedicated tanks):
- **Ship Fuel**: 1x1 grid slots, 0.1 tons each, **stack to 100 units**
- **Plane Fuel** (carriers only): 1x1 grid slots, 0.08 tons each, **stack to 100 units**
- **Critical resource**: Must carry enough for mission duration + safety margin
- **Consumes cargo space**: Every fuel stack reduces loot capacity

**Fuel Consumption Rates**:
- **Transit speed**: 5-10 ship fuel units/hour at cruising speed
- **Combat speed**: 15-30 ship fuel units/hour at flank speed
- **Aircraft operations (carriers)**: 10 plane fuel units per wing launch
- **Consumable use**: 5-10 ship fuel units per consumable activation

**Example Loadouts by Ship Type**:
- **Destroyer** (10-hour mission): 200 ship fuel (2 stacks = 2 grid slots, 20 tons)
- **Battleship** (10-hour mission): 400 ship fuel (4 stacks = 4 grid slots, 40 tons)
- **Carrier** (10-hour mission): 400 ship fuel + 500 plane fuel (9 stacks = 9 grid slots, 80 tons)
- **Submarine** (20-hour patrol): 400 ship fuel (4 stacks = 4 grid slots, 40 tons)

**Strategic Considerations**:
- **Fuel vs. cargo trade-off**: More fuel = less loot capacity
- **Run out of fuel**: Ship becomes dead in water, requires rescue/towing
- **Carriers need TWO fuel types**: Ship fuel (for movement) + Plane fuel (for aircraft)

#### **Repair Materials**
**Portable repair supplies**:
- **Steel Plates**: 2x2 slots, used for hull repairs (10 plates = 1,000 HP repair)
- **Electrical Components**: 1x1 slots, used for module repairs
- **Damage Control Supplies**: 2x1 slots, improves fire/flood repair effectiveness

**Strategic use**:
- Can perform **field repairs** at any friendly port
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

### 5. Crew Cards & Currency

#### **Wallet Item - OPTIONAL Space-Saving Container**
**Grid Size & Weight**:
- **Wallet**: 2x2 grid slots, 1 ton
- **Opens into**: 50x50 internal inventory (2,500 slots dedicated to crew cards and currency)
- **Restrictions**: ONLY accepts crew cards (2x2 each) and currency
- **Purchased item**: Players buy wallets when they can afford them (not starter equipment)

**Why Use Wallets?**
- **Massive space savings**: 50 crew cards loose = 200 slots vs. 1 wallet = 4 slots
- **Port-to-port transfers**: Transport large crew card collections efficiently
- **Inventory optimization**: Free up ship/port inventory space for other items

**Without Wallet** (Starting players):
- Crew cards stored loose as 2x2 items in ship cargo or port storage
- Must balance crew cards with ammunition, modules, fuel, loot in limited inventory
- Example: Destroyer with 120 slots, 9 crew cards = 36 slots, leaves 84 for ammo/fuel/loot

**With Wallet** (Purchased):
- Same 9 crew cards in wallet = 4 slots (2x2 wallet), leaves 116 slots free
- Can transport 40+ crew cards in single wallet (4 slots vs. 160 slots loose)
- Essential for players with large crew card collections or frequent port transfers

**Wallet Mechanics**:
- **Storage locations**: Can be in ship cargo, port storage, or drydocked ship inventory
- **Open/close interface**: Click wallet to view 50x50 internal grid
- **Drag-and-drop**: Move crew cards in/out of wallet freely
- **Not for backup crew**: Cannot swap crew mid-mission, so carrying extra crew only useful for port relocations

#### **Crew Card System**
**Crew Card Properties**:
- **Grid Size**: 2x2 slots per crew card
- **Weight**: 0.1 tons per card (negligible)
- **Storage Locations**:
  - Loose in ship cargo inventory
  - Loose in port storage inventory
  - Inside wallet (optional, saves space: 2x2 wallet holds 50x50 worth of cards)
- **Active Crew**: Assigned crew don't occupy ANY inventory space (in crew quarters)

**Port Configuration Views** (Accessible only while docked):

**Equipment View**:
- Install/remove modules and turrets on ship hardpoints
- Examples: Main battery turrets, AA mounts, radar modules, torpedo tubes, engine modules, damage control systems
- Empty hardpoints cannot accept crew assignments

**Crew View**:
- Assign crew cards from port storage or wallet to equipment slots
- **Workflow Options**:
  - **Without wallet**: Drag crew card from port storage → equipment slot in Crew View
  - **With wallet**: Open wallet in port storage → drag crew card from wallet → equipment slot
- **Assignment Validation**:
  - Equipment slot HAS module installed → Crew card MUST match module type (e.g., gunner → turret, radar operator → radar)
  - Equipment slot EMPTY (no module installed) → Any crew card can occupy slot (no type validation)
- **Port-only changes**: Cannot swap crew or equipment at sea (locked until next port visit)

**Crew Card Types & Equipment Matching**:
- **Gunnery Crew**: Assigned to turret modules (main battery, secondary battery)
- **AA Crew**: Assigned to AA gun mounts
- **Torpedo Crew**: Assigned to torpedo tube modules
- **Radar Operators**: Assigned to radar/sonar modules
- **Engineers**: Assigned to engine modules
- **Damage Control**: Assigned to damage control stations
- **Bridge Officers**: Assigned to bridge positions (fire control, navigation, command)

**Crew Capacity Limits** (equipment-based positions):
- **Destroyer**: 50-75 equipment slots
- **Cruiser**: 75-150 equipment slots
- **Battleship**: 150-200 equipment slots
- **Carrier**: 200-300 equipment slots (includes flight deck positions)

#### **Currency System**
**Credits**:
- **Storage**: Physical currency stored inside wallet inventory
- **Stack size**: 10,000 credits per stack (1 slot), negligible weight
- **Port trading**: Spend credits at any port for modules, ammunition, crew recruitment, repairs
- **Transfer between ports**: Carry wallet in ship cargo to transport currency

**Example Usage - Player A (No Wallet, Early Game)**:
- Destroyer with 9 crew slots, player has 14 total crew cards (9 active + 5 extras)
- **Port Storage**: 5 unassigned crew cards stored loose (5 × 2x2 = 20 slots used)
- Wants to relocate to new port 500km away
- **Loading**: Drags 5 crew cards from port storage → ship cargo (20 slots + ammo + fuel = full inventory)
- Sails to new port
- **Unloading**: Drags 5 crew cards from ship cargo → new port storage

**Example Usage - Player B (With Wallet, Late Game)**:
- Battleship with 150 crew slots, player has 40+ crew cards amassed over time
- Wants to relocate entire crew card collection to forward port
- **Purchases wallet** (2x2 item) for 50,000 credits
- **Loading Phase**:
  - Opens wallet in port storage
  - Drags all 40 crew cards from port storage → wallet internal inventory (40 × 2x2 = 160 slots compressed to 4 slots)
  - Transfers wallet (4 slots) from port storage → battleship cargo
- Sails to new port with wallet in cargo (4 slots vs. 160 slots loose)
- **Unloading**: Transfers wallet from battleship cargo → new port storage
- **Ship Switching**:
  - Opens port drydock, transfers battleship to drydock (inactive)
  - Builds new cruiser, sets as active ship
  - **Equipment View**: Installs turrets/modules on cruiser
  - **Crew View**:
    - Recruits 5 new crew cards at port (added loose to port storage)
    - Opens wallet in port storage
    - Drags existing crew cards from wallet → cruiser equipment slots
    - Drags new crew cards from port storage → cruiser equipment slots

---

## Port Storage System

### 1. Port Storage (Per-Port Inventory)

#### **Limited Grid Space (500-1000 Slots Per Port)**
- **Per-port storage**: Each port has 500-1000 grid slots (prevents infinite hoarding)
- **Separate inventories**: Storage at Port A is completely separate from Port B
- **Organization**: Same grid system as ship inventory (drag-and-drop interface)
- **Access**: Only accessible when docked at that specific port
- **Purpose**: Long-term storage for ammunition, modules, crew cards (loose or in wallets), loot, fuel
- **Strategic pressure**: Full warehouse forces decisions to use/sell items or relocate to new port

**What Gets Stored**:
- Ammunition stockpiles for pre-mission loadouts
- Spare modules and turrets
- Crew cards (loose 2x2 items or organized in wallets)
- Wallets (containing crew cards + currency)
- Trade goods and extracted loot
- Fuel reserves

#### **Transfer Mechanics**
- **Drag-and-drop**: Move items between active ship cargo ↔ port storage
- **Auto-stack**: Click to automatically combine partial stacks
- **Quick-load presets**: Save ammunition/fuel loadouts for quick pre-mission prep
- **Weight warnings**: UI shows when ship is over-capacity during loading
- **No cross-port transfer**: Must physically sail items from Port A to Port B

**Port Relocation Workflow**:
1. Load items from Port A storage → ship cargo
2. Sail ship to Port B
3. Unload items from ship cargo → Port B storage
4. Wallets enable efficient bulk transport (40 crew cards = 4 slots vs. 160 slots)

### 2. Drydock System (Multi-Ship Management)

#### **Multiple Ships Per Port**
- **Active ship**: Currently equipped ship (takes to sea)
- **Drydocked ships**: Inactive ships stored at port (unlimited per port)
- **Ship switching**: Change which ship is active at port

**Drydock Transfer Mechanics**:
- **Ship-to-ship transfers**: Move items between active ship ↔ drydocked ships
- **Example**: Transfer elite modules from inactive battleship to new cruiser
- **Port storage hub**: Both active and drydocked ships can access port storage
- **No restrictions**: Freely transfer ammunition, modules, crew cards between ships at same port

**Example Workflow**:
1. Dock battleship at Port A
2. Transfer battleship to drydock (becomes inactive)
3. Build new destroyer at Port A, set as active ship
4. Open drydock interface: Transfer radar module from battleship → destroyer
5. Access port storage: Load ammunition from port → destroyer cargo
6. Undock destroyer (battleship remains drydocked at Port A)

### 3. Module Workshop

#### **Module Modification Station**
- **Upgrade modules**: Improve stats using resources + credits
- **Repair damaged modules**: Restore modules damaged during combat
- **Module crafting**: Combine components to create advanced modules
- **Research tree**: Unlock new module types through R&D

---

## Tactical Loadout Examples

### Destroyer Loadout (USS Fletcher - T3)
**Total Cargo Capacity**: 120 grid slots, 200 tons weight capacity

**Combat-Focused Loadout** (Ammunition-heavy, impractical example):
- 5-inch AP shells: 300 rounds (3 stacks = 3 slots, 15 tons)
- 5-inch HE shells: 200 rounds (2 stacks = 2 slots, 10 tons)
- Torpedoes (reloads): 20 (4 stacks of 5 = 4 slots of 1x3 = 12 grid cells, 40 tons)
- Ship fuel: 200 units (2 stacks = 2 slots, 20 tons)
- **Total: 9/120 slots (19 grid cells), 85/200 tons** ✅ Space efficient but limited utility

**Balanced Loadout**:
- 5-inch AP shells: 150 rounds (2 stacks: 100+50 = 2 slots, 7.5 tons)
- 5-inch HE shells: 150 rounds (2 stacks: 100+50 = 2 slots, 7.5 tons)
- Torpedoes (reloads): 10 (2 stacks of 5 = 2 slots of 1x3 = 6 grid cells, 20 tons)
- Depth charges: 40 (2 stacks of 20 = 2 slots of 1x2 = 4 grid cells, 8 tons)
- Repair materials: 5 steel plates (5 slots of 2x2 = 20 grid cells, 10 tons)
- Ship fuel: 200 units (2 stacks = 2 slots, 20 tons)
- **Total: 12 stacks (52 grid cells), 73/200 tons** ✅ 68 slots free for loot

**Optimized Combat Loadout** (Recommended):
- 5-inch AP shells: 100 rounds (1 stack = 1 slot, 5 tons)
- 5-inch HE shells: 100 rounds (1 stack = 1 slot, 5 tons)
- Torpedoes (reloads): 10 (2 stacks of 5 = 2 slots of 1x3 = 6 grid cells, 20 tons)
- Depth charges: 20 (1 stack = 1 slot of 1x2 = 2 grid cells, 4 tons)
- Ship fuel: 200 units (2 stacks = 2 slots, 20 tons)
- **Total: 7 stacks (12 grid cells), 54/200 tons** ✅ 108 slots free for loot

**Extraction-Focused Loadout** (After successful loot run):
- 5-inch HE shells: 50 rounds (1 partial stack = 1 slot, 2.5 tons) - Minimal defensive ammo
- Torpedoes (reloads): 0 (0 slots) - All fired
- Ship fuel: 100 units (1 stack = 1 slot, 10 tons) - Enough to reach port
- Salvaged modules: 2x high-value radars (2 slots of 3x3 = 18 grid cells, 24 tons)
- Resource crates: 8 crates (8 slots of 2x2 = 32 grid cells, 16 tons)
- Intelligence documents: 10 (10 slots of 1x1 = 10 grid cells, 1 ton)
- **Total: 22 stacks/items (73 grid cells), 53.5/200 tons** ✅ Racing to extract with valuable loot

---

### Battleship Loadout (USS Iowa - T5)
**Total Capacity**: 300 grid slots, 500 tons weight capacity

**Optimized Combat Loadout**:
- 16-inch AP shells: 100 rounds (2 stacks of 1x2 = 4 grid cells, 100 tons)
- 16-inch HE shells: 50 rounds (1 stack of 1x2 = 2 grid cells, 50 tons)
- 5-inch secondary HE: 200 rounds (2 stacks of 1x1 = 2 grid cells, 10 tons)
- AA ammunition: 1,000 rounds (2 stacks of 1x1 = 2 grid cells, 2 tons)
- Repair materials: 10 steel plates (10 items of 2x2 = 40 grid cells, 10 tons)
- Ship fuel: 400 units (4 stacks of 1x1 = 4 grid cells, 40 tons)
- **Total: 54 grid cells, 212/500 tons** ✅ 246 grid slots free for loot

**Weight-Constrained Alternative** (more ammunition):
- 16-inch AP shells: 200 rounds (4 stacks of 1x2 = 8 grid cells, 200 tons)
- 16-inch HE shells: 100 rounds (2 stacks of 1x2 = 4 grid cells, 100 tons)
- 5-inch secondary HE: 200 rounds (2 stacks of 1x1 = 2 grid cells, 10 tons)
- Ship fuel: 400 units (4 stacks of 1x1 = 4 grid cells, 40 tons)
- **Total: 18 grid cells, 350/500 tons** ⚠️ Heavy load (70% weight capacity)

**Strategic considerations**:
- Battleships are **weight-constrained** due to massive shell weight (1 ton each for 16-inch)
- 150 total main battery rounds = 50 salvos (9 guns × 3 rounds per salvo)
- Grid space abundant, but weight limits ammunition drastically
- Heavy ammunition loads reduce speed by 5-10%
- Must conserve ammunition or accept reduced mobility

---

### Carrier Loadout (USS Essex - T5)
**Total Capacity**: 500 grid slots, 700 tons weight capacity

**Balanced Air Wing Loadout** (Too many aircraft - demonstration of overflow):
- 30 fighters (F6F Hellcat): 30 items of 3x3 = 270 grid cells, 150 tons
- 20 dive bombers (SBD Dauntless): 20 items of 3x4 = 240 grid cells, 120 tons
- 20 torpedo bombers (TBF Avenger): 20 items of 3x4 = 240 grid cells, 140 tons
- **Aircraft subtotal: 750 grid cells, 410 tons** ❌ OVER GRID CAPACITY

**Optimized Balanced Loadout**:
- 20 fighters: 20 items of 3x3 = 180 grid cells, 100 tons
- 12 dive bombers: 12 items of 3x4 = 144 grid cells, 72 tons
- 12 torpedo bombers: 12 items of 3x4 = 144 grid cells, 84 tons
- 200x 500-lb bombs: 10 stacks of 1x1 = 10 grid cells, 50 tons
- 50x 1,000-lb bombs: 5 stacks of 1x2 = 10 grid cells, 25 tons
- 30 aerial torpedoes: 6 stacks of 1x3 = 18 grid cells, 45 tons
- Ship fuel: 400 units (4 stacks of 1x1 = 4 grid cells), 40 tons
- Plane fuel: 500 units (5 stacks of 1x1 = 5 grid cells), 40 tons
- **Total: 515 grid cells (overflowing by 15), 456/700 tons** ⚠️ Need to reduce aircraft by 2

**Strike-Heavy Loadout** (Offensive operation):
- 10 fighters: 10 items of 3x3 = 90 grid cells, 50 tons
- 16 dive bombers: 16 items of 3x4 = 192 grid cells, 96 tons
- 16 torpedo bombers: 16 items of 3x4 = 192 grid cells, 112 tons
- 300x 500-lb bombs: 15 stacks of 1x1 = 15 grid cells, 75 tons
- 80x 1,000-lb bombs: 8 stacks of 1x2 = 16 grid cells, 40 tons
- 50 aerial torpedoes: 10 stacks of 1x3 = 30 grid cells, 75 tons
- Ship fuel: 400 units (4 stacks of 1x1 = 4 grid cells), 40 tons
- Plane fuel: 600 units (6 stacks of 1x1 = 6 grid cells), 48 tons
- **Total: 545 grid cells (overflowing by 45), 536/700 tons** ⚠️ Need to reduce aircraft by ~4-5

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
- **Warning**: HUD shows over-capacity warning (red weight indicator)

**Extreme Over-Capacity (120%+)**:
- **Speed**: 75% (-25% max speed)
- **Acceleration**: 50% (-50% slower acceleration)
- **Turn rate**: 75% (-25% turn rate)
- **Fuel efficiency**: 150% (+50% fuel consumption)
- **Critical**: Combat effectiveness severely impaired, difficult to maneuver
- **Extraction risk**: Extremely vulnerable, can't outrun pursuers

---

## Extraction Mechanics & Inventory Tension

### 1. Combat Damage Reduces Capacity

**Module destruction reduces usable cargo space**:
- **Ammunition fire**: 10-30% cargo capacity lost (ammunition destroyed in cargo hold)
- **Hull flooding**: 5-15% cargo capacity lost (compartments sealed)
- **Structural damage**: Cannot access damaged cargo holds until repaired

**Example scenario**:
- USS Fletcher starts with 120 slots
- Takes cargo hold hit → ammunition fire destroys 20 slots worth of items
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

**Cargo Loss - Always 100% on Death (All Tiers)**:
When your ship sinks, **ALL cargo is permanently lost** regardless of tier:
- Ammunition in cargo hold
- Fuel reserves
- Loot and trade goods
- Uninstalled modules stored in cargo
- **Loose crew cards in cargo** (not assigned to equipment)

**Ship/Equipment Recovery by Tier**:

**T1-T5 (0% Ship Permadeath - Learning Phase)**:
- Ship automatically recovered at last port departed from
- Equipped modules recovered (turrets, radar, engines, etc.)
- Assigned crew cards recovered (crew in equipment slots)
- **Cargo lost: 100%** (ammunition, fuel, loot, loose crew cards)

**T6-T10 (10-100% Ship Permadeath - Risk Zones)**:
Ship permadeath check determines recovery:
- **T6**: 10% chance ship permanently lost
- **T7**: 20% chance ship permanently lost
- **T8**: 40% chance ship permanently lost
- **T9**: 60% chance ship permanently lost
- **T10**: 100% chance ship permanently lost (GUARANTEED)

**If permadeath check FAILS (ship survives check)**:
- Ship recovered via insurance at last port
- Equipped modules recovered
- Assigned crew cards recovered

**If permadeath check SUCCEEDS (ship permanently lost)**:
- Ship permanently destroyed (must rebuy)
- Equipped modules permanently lost
- Assigned crew cards permanently lost

**In BOTH cases**: All cargo lost 100% (ammunition, fuel, loot, loose crew cards)

---

**Creates meaningful risk/reward**:
- **Every death means cargo loss**: Even T1-T5 "safe" tiers lose all loot/ammunition on death
- **High-tier permadeath risk**: T6+ ships risk losing the ship itself plus equipped modules/crew
- **Loose crew cards are vulnerable**: Crew cards in cargo (not assigned) are lost with cargo
- **Extraction tension**: Players must weigh "one more engagement" vs. "extract now with cargo intact"
- **T10 operations**: Catastrophic - guaranteed ship loss, all cargo lost, equipped modules/crew lost

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

---

## UI/UX Design Considerations

### Inventory Grid Interface

**Visual clarity**:
- **Grid overlay**: Clear demarcation of slots
- **Item icons**: Recognizable silhouettes for quick identification
- **Color coding**: Ammunition (red), modules (blue), loot (yellow)
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
- **Ammunition counter**: Current ammunition count for active weapon
- **Torpedo counter**: Remaining torpedoes (equipped + reloads in cargo)
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
2. **Fuel vs. cargo**: Carry extra fuel for extended operations, or maximize loot capacity?
3. **Weight budget**: Prioritize heavy ammunition (weight-limited) or light cargo (grid-limited)?
4. **Carriers only**: Ship fuel vs. plane fuel ratio - long transit or heavy air operations?
5. **Loot capacity**: Leave cargo space free for extraction loot, or go combat-heavy?

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
- **Module damage** can destroy cargo (ammunition explosions in cargo hold)
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
- **Crew recruitment** adds crew cards to port storage (can be stored loose or in wallet, assigned to equipment via Crew View at port)
- **Ship upgrades** may increase base cargo capacity and equipment slots
- **Tier progression** unlocks larger cargo holds and more equipment positions

---

## Cross-Reference Documents

**Related Core Gameplay**:
- [[Crew-Management]] - Wallet system, crew card storage, Equipment View, and Crew View assignment mechanics
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
5. Port warehouse limited storage (500-1000 slots per port, no account bank)

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
