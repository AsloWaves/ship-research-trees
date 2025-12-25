# Tetris Fitting Mechanics

**Status**: 📋 IN DEVELOPMENT
**Tags**: [core-mechanics, inventory, fitting, tetris-system, phase2]
**Priority**: HIGH (foundational system)
**Last Updated**: 2025-12-10

---

## Overview

Fathoms Deep uses multiple grid-based inventory systems inspired by Escape from Tarkov's spatial inventory and Navy Field's ship management. This document defines the mechanics for all grid-based systems and clarifies how they differ from each other.

**Three Distinct Grid Systems:**

| System | Type | Purpose | Grid Style |
|--------|------|---------|------------|
| **Ship Cargo** | True Tetris | Mission inventory (ammo, fuel, loot) | Freeform placement, rotation, partitions |
| **Port/Drydock Storage** | True Tetris | Between-mission storage | Rectangle grid, same mechanics as cargo |
| **Equipment Slots** | Slot-Matching | Ship fitting (modules, turrets) | Fixed slots with dimension requirements |

---

## Part 1: Equipment Slot System (Slot-Matching)

### Core Concept

Equipment slots are **NOT freeform Tetris placement**. Each ship has fixed, numbered slots with specific grid dimensions. Modules must **exactly match** the slot dimension to install.

```
EQUIPMENT SLOT MATCHING
=======================

Slot Dimension → Module Dimension (MUST BE EXACT MATCH)

Example: USS Iowa Battleship
├── Main Battery Slot A: [3x4] → Accepts ONLY 3x4 turrets
├── Main Battery Slot B: [3x4] → Accepts ONLY 3x4 turrets
├── Main Battery Slot C: [3x4] → Accepts ONLY 3x4 turrets
├── Secondary Slots 1-10: [1x2] → Accepts ONLY 1x2 mounts
├── AA Slots 1-40: [1x1] → Accepts ONLY 1x1 AA guns
├── Engine Slots 1-4: [2x3] → Accepts ONLY 2x3 engines
├── Radar Slot: [2x2] → Accepts ONLY 2x2 radar
└── Support Slots 1-8: [Various] → Each has fixed dimension
```

### Why Slot-Matching?

**Design Goal**: Prevent "cheese" builds where players install inappropriate equipment.

| Problem | Solution |
|---------|----------|
| Battleship with 40 destroyer guns | 3x4 main battery slots only accept 3x4 turrets |
| Destroyer with battleship radar | Destroyer radar slots are 1x1, battleship radar is 3x3 |
| Mixing incompatible equipment | Slot dimensions enforce ship-appropriate modules |

### Equipment Slot Validation

When a player attempts to install a module:

```
VALIDATION ORDER
================

Step 1: GRID DIMENSION CHECK
  └── Module dimension == Slot dimension?
      ├── YES → Continue to Step 2
      └── NO → RED HIGHLIGHT (Cannot Install)

Step 2: WEIGHT CHECK (Module)
  └── Module weight ≤ Slot weight capacity?
      ├── YES → Module installs successfully
      └── NO → RED HIGHLIGHT (Too Heavy)

Step 3: CREW ASSIGNMENT (Optional)
  └── Player drags crew card to module
      └── Module weight + Crew weight ≤ Slot weight capacity?
          ├── YES → Crew assigned, module operational
          └── NO → RED HIGHLIGHT (Crew Too Heavy)

Note: Module can be installed without crew (Step 2 passes)
      but will be NON-FUNCTIONAL until crew assigned (Step 3)
```

### Equipment Slot Categories

Ships have slots in these categories, each with dimension requirements:

**Weapon Hardpoints** (External, visible on ship sprite):
- Main Battery Slots: Large turrets (2x2 to 4x4 typical)
- Secondary Battery Slots: Medium guns (1x2 to 2x2 typical)
- Tertiary/AA Slots: Small mounts (1x1 typical)
- Torpedo Tube Slots: Torpedo launchers (1x3 typical)
- Wing Slots: Aircraft squadrons (carriers/seaplane ships)

**Internal System Slots** (Not visible externally):
- Engine Slots: Propulsion systems (2x3 to 3x4 typical)
- Support Slots: Crew welfare, damage control (1x1 to 2x3 typical)
- Misc Slots: Universal equipment (various sizes)

### Slot Assignment Per Ship

Slot counts and dimensions are **assigned per individual ship**, not per class:

```
Example: Two T5 Destroyers with Different Layouts

USS Fletcher:
- Main Battery: 5 slots [1x2 each]
- Torpedo Tubes: 2 slots [1x3 each]
- AA Mounts: 10 slots [1x1 each]
- Engine Slots: 2 slots [2x2 each]
- Support: 4 slots [1x1, 1x1, 1x2, 1x2]

USS Sumner:
- Main Battery: 6 slots [1x2 each] ← More guns
- Torpedo Tubes: 2 slots [1x3 each]
- AA Mounts: 12 slots [1x1 each] ← More AA
- Engine Slots: 2 slots [2x3 each] ← Larger engines
- Support: 3 slots [1x2, 1x2, 2x2] ← Fewer but larger

This allows national flavor and balance adjustments:
- IJN destroyers: More torpedo slots, fewer gun slots
- USN destroyers: Balanced loadouts
- RN destroyers: More AA, less torpedoes
```

---

## Part 2: Wing Slot System (Aircraft)

### Core Concept

Carriers and seaplane-equipped ships have **Wing Slots** for aircraft squadrons. These function similarly to turret hardpoints but hold aircraft stacks instead of weapons.

```
WING SLOT STRUCTURE
===================

Wing Slot Properties:
├── Aircraft Capacity: Max planes in this slot (stack limit)
├── Weight Capacity: Aircraft stack weight + Pilot crew weight
├── Slot Type: UNIVERSAL (any aircraft type)
└── Crew Requirement: Pilot crew card (Aviation classification)
```

### Universal Wing Slots

All wing slots are **universal** - players choose their air group composition:

```
USS Essex (T5 Fleet Carrier):
- Wing Slot 1: Universal, 12 aircraft max, 45 ton capacity
- Wing Slot 2: Universal, 12 aircraft max, 45 ton capacity
- Wing Slot 3: Universal, 10 aircraft max, 40 ton capacity
- Wing Slot 4: Universal, 10 aircraft max, 40 ton capacity

Player Composition Options:
A) Balanced: 12 fighters, 12 fighters, 10 dive bombers, 10 torp bombers
B) Fighter Heavy: 12 fighters × 4 slots = 44 fighters (all escort, no strike)
C) Strike Heavy: 12 torp bombers × 4 slots (glass cannon, no CAP)

Player choice, player consequences.
```

### Wing Slot Weight Calculation

Following the weight-based fitting philosophy:

```
WING SLOT WEIGHT CHECK
======================

Wing_Capacity ≥ Aircraft_Stack_Weight + Pilot_Crew_Weight

Example Calculation:
Wing Slot Capacity: 45 tons

Aircraft Stack: 10× F6F Hellcat fighters
  └── 1.5 tons each × 10 = 15 tons

Pilot Crew Card: Level 60 Fighter Pilot
  └── Sailor count at L60: ~255 sailors
  └── Weight: 255 × 0.1 × (1 + 60/100) = 40.8 tons

Total: 15 + 40.8 = 55.8 tons
Result: EXCEEDS 45 ton capacity → RED HIGHLIGHT

Solutions:
A) Use fewer aircraft: 8× F6F = 12 tons → 12 + 40.8 = 52.8 tons (still over)
B) Use lower-level pilot: L30 pilot = 127 × 0.1 × 1.3 = 16.5 tons
   └── 15 + 16.5 = 31.5 tons → FITS ✓
C) Use lighter aircraft: 10× lighter fighter variant
```

**Design Note**: Wing slot capacities should be tuned during balance testing to ensure reasonable pilot levels can be used with full squadrons.

### Pilot Crew Integration

Pilots use the standard crew-module efficiency system:

```
SQUADRON EFFICIENCY
===================

Efficiency = Sailor_Factor × Stat_Factor

Sailor_Factor = Surviving_Pilots / Max_Pilots
  └── Represents: Pilots lost in combat reduce squadron effectiveness
  └── As planes are shot down, "sailors" (pilots) are lost

Stat_Factor = 1.0 + ((Primary_Stat - 15) × 0.02)
  └── Aviation classification uses: Air Combat, Bombing, Torpedo Attack

Example:
Fighter Wing with Level 80 Pilot (Air Combat stat: 35)
- Full squadron: 255/255 sailors = 100% Sailor_Factor
- Stat_Factor: 1.0 + ((35 - 15) × 0.02) = 1.40
- Efficiency: 100% × 1.40 = 140% (excellent dogfighting)

After losing 6 of 12 planes (proportional pilot loss ~50%):
- Sailor_Factor: 127/255 = ~50%
- Efficiency: 50% × 1.40 = 70% (degraded but still functional)
```

### Reserve Aircraft in Cargo

Spare aircraft can be stored in the **cargo grid** for mid-mission replacement:

```
AIRCRAFT REPLACEMENT FLOW
=========================

During Mission:
1. Squadron in Wing Slot 2 loses 4 planes (8 → 4 remaining)
2. Player has 6 reserve fighters in cargo grid
3. At any time (not during active combat), player can:
   └── Open fitting screen → Drag 4 fighters from cargo → Wing Slot 2
4. Squadron restored to 8 planes
5. Cargo now has 2 reserve fighters remaining

Restrictions:
- Cannot swap aircraft during active combat (cooldown period)
- Replacement aircraft come from cargo, not thin air
- Pilot crew card stays assigned (surviving pilots)
- Dead pilots (sailors) are NOT restored by adding planes
```

### Aircraft Ordnance

Aircraft ordnance (bombs, torpedoes for planes) is stored in the **cargo grid**, not wing slots:

```
CARRIER LOADOUT STRUCTURE
=========================

Wing Slots:
├── Wing 1: 12× F6F Hellcat (fighters - no ordnance needed)
├── Wing 2: 10× SBD Dauntless (dive bombers - need bombs)
├── Wing 3: 10× TBF Avenger (torpedo bombers - need torpedoes)
└── Wing 4: 8× F4U Corsair (fighter-bombers - need bombs)

Cargo Grid:
├── Aircraft Ordnance:
│   ├── 200× 500-lb bombs (10 stacks × 1x1 = 10 cells, 50 tons)
│   ├── 50× 1,000-lb bombs (5 stacks × 1x2 = 10 cells, 25 tons)
│   └── 40× aerial torpedoes (8 stacks × 1x3 = 24 cells, 60 tons)
├── Ship Fuel: 400 units (4 stacks = 4 cells, 40 tons)
├── Plane Fuel: 500 units (5 stacks = 5 cells, 40 tons)
├── Reserve Aircraft: 6× F6F (stored as 2x3 item, 9 tons)
└── Loot Space: ~50 cells remaining

Trade-offs:
- More ordnance = fewer sorties before running out
- Less ordnance = more loot capacity
- Reserve aircraft compete with bombs for cargo space
```

### Seaplane-Equipped Ships

Non-carriers with catapults use the same wing slot system:

```
Seaplane-Equipped Ships:

Heavy Cruiser (e.g., USS Indianapolis):
- Wing Slot 1: 4 aircraft max, 15 ton capacity (catapult)
- Wing Slot 2: 4 aircraft max, 15 ton capacity (catapult)
- Accepts: Scout floatplanes only (OS2U Kingfisher, etc.)

Battleship (e.g., USS Iowa):
- Wing Slot 1: 3 aircraft max, 12 ton capacity
- Wing Slot 2: 3 aircraft max, 12 ton capacity
- Accepts: Scout floatplanes only

Seaplane Tender (e.g., USS Curtiss):
- Wing Slots 1-6: 6 aircraft max each, 25 ton capacity
- Accepts: Any floatplane type (scouts, fighters, bombers)
- Total: Up to 36 floatplanes operational
```

---

## Part 3: Ship Cargo Grid (True Tetris)

### Core Concept

The ship cargo grid is a **true Tetris-style spatial inventory**. Items have physical dimensions and must be placed in available grid space.

```
CARGO GRID PROPERTIES
=====================

Dual Constraints:
├── Grid Cells: Spatial capacity (how many cells available)
└── Weight Limit: Tonnage capacity (hard cap at 100%)

Both must be satisfied:
- Can fill grid but be under weight limit (bulky light items)
- Can hit weight limit with grid space remaining (heavy compact items)
- EFT-style optimization: Balance weight vs. space
```

### Grid Dimensions by Ship

Each ship has individually assigned cargo capacity:

```
CARGO CAPACITY EXAMPLES (not final values)
==========================================

Destroyers: 80-160 grid cells, 150-300 tons
├── USS Fletcher: 120 cells, 200 tons
├── IJN Fubuki: 100 cells, 180 tons (less cargo, more torpedoes)
└── HMS Tribal: 130 cells, 220 tons (larger hull)

Cruisers: 150-350 grid cells, 300-600 tons
├── USS Cleveland: 200 cells, 400 tons
├── IJN Mogami: 180 cells, 350 tons
└── HMS Belfast: 220 cells, 450 tons

Battleships: 200-500 grid cells, 400-800 tons
├── USS Iowa: 300 cells, 500 tons
├── IJN Yamato: 350 cells, 600 tons
└── HMS Vanguard: 280 cells, 480 tons

Carriers: 300-700 grid cells, 500-1000 tons
├── USS Essex: 500 cells, 700 tons
├── IJN Shokaku: 450 cells, 650 tons
└── HMS Illustrious: 400 cells, 600 tons (armored, less capacity)
```

### Item Dimensions & Stacking

Items occupy grid space based on physical size:

```
ITEM SIZE REFERENCE
===================

Ammunition:
├── Small shells (4-6"): 1x1, stack to 100
├── Medium shells (8-10"): 1x1, stack to 50
├── Large shells (12-14"): 1x2, stack to 50
├── Super-heavy shells (16-18"): 1x2, stack to 50
├── Torpedoes: 1x3, stack to 5
├── Long Lance torpedoes: 1x4, stack to 5
├── AA ammunition: 1x1, stack to 500
└── Depth charges: 1x2, stack to 20

Fuel:
├── Ship fuel: 1x1, stack to 100 units
└── Plane fuel: 1x1, stack to 100 units

Aircraft (in cargo, not wing slots):
├── Fighters: 3x3
├── Dive bombers: 3x4
├── Torpedo bombers: 3x4
└── Scout planes: 2x3

Modules (uninstalled, in cargo):
├── Small modules: 1x1 to 2x2
├── Medium modules: 2x2 to 2x3
├── Large modules: 3x3 to 3x4
└── Turrets: 2x2 to 4x4

Other:
├── Crew cards: 2x2 each
├── Wallet (crew container): 2x2 (holds 10x25 internal grid)
├── Resource crates: 2x2 to 4x4
├── Intelligence documents: 1x1
└── Repair kits: 1x1 to 2x2
```

### Stack Footprint Rule

**Critical**: Stack size does NOT affect grid footprint.

```
STACKING RULE
=============

1 shell = Same grid size as 100 shells

Example: 5-inch HE Shells (1x1, stacks to 100)
├── 1 shell: Occupies 1x1, weighs 0.05 tons
├── 50 shells: Occupies 1x1, weighs 2.5 tons
└── 100 shells: Occupies 1x1, weighs 5 tons

The WEIGHT changes, the GRID FOOTPRINT does not.

This creates the EFT-style optimization:
- Heavy items: Hit weight cap before grid cap
- Light items: Hit grid cap before weight cap
- Strategy: Balance your loadout for both constraints
```

### Item Rotation

All non-square items can be rotated:

```
ROTATION MECHANICS
==================

R Key: Rotate item 90° clockwise

Examples:
├── 1x3 torpedo → Rotates to 3x1 torpedo
├── 2x3 engine → Rotates to 3x2 engine
├── 3x4 bomber → Rotates to 4x3 bomber

Square items (1x1, 2x2, 3x3, 4x4):
└── Rotation has no effect (optional, can skip)

Rotation allows:
- Fitting items into awkward spaces
- Optimizing grid packing efficiency
- Solving the "Tetris puzzle" when cargo is nearly full
```

### Grid Shape Evolution

**Phase 1 (Launch)**: Standard rectangle grids for all ships

**Phase 2+ (Future)**: Partitioned and irregular grids

```
FUTURE GRID SHAPES (Ships Only)
===============================

Partitioned Grid:
┌───────────────┬─────────┐
│               │         │
│   Main Cargo  │ Armory  │
│   (General)   │ (Ammo)  │
│               │         │
├───────────────┴─────────┤
│      Forward Hold       │
│      (Limited Access)   │
└─────────────────────────┘

Irregular Hull Shape:
      ┌───────┐
    ┌─┘       └─┐
  ┌─┘           └─┐
  │    Cargo     │
  │    Hold      │
  └─┬───────────┬┘
    └───────────┘

Benefits:
- Thematic (cargo follows hull shape)
- Strategic (choose what goes where)
- Like EFT backpack varieties
```

---

## Part 4: Port Storage Grid

### Core Concept

Port storage uses the **same Tetris mechanics** as ship cargo but with larger capacity and standard rectangle shape.

```
PORT STORAGE PROPERTIES
=======================

Grid Shape: Standard rectangle (all ports)
Capacity by Port Tier:
├── T1-T3 Ports: 500 grid cells
├── T4-T7 Ports: 750 grid cells
└── T8-T10 Ports: 1000 grid cells

Per-Port Storage:
- Each port has SEPARATE storage
- No universal/shared account storage
- Must physically transport items between ports
```

### Storage Contents

Port storage accepts the same items as ship cargo:

```
PORT STORAGE CONTENTS
=====================

├── Ammunition stockpiles
├── Fuel reserves
├── Uninstalled modules and turrets
├── Crew cards (loose or in wallets)
├── Loot and trade goods
├── Resource crates
└── Any other cargo-type items

NOT stored in port storage:
├── Ships (use Drydock instead)
├── Equipped modules (attached to ships)
└── Assigned crew cards (on ship duty roster)
```

### Transfer Mechanics

```
TRANSFER FLOW
=============

Ship ↔ Port Storage:
1. Dock at port
2. Open inventory screen (split view: ship cargo | port storage)
3. Drag items between ship cargo and port storage
4. Items transfer instantly (no time delay)

Restrictions:
- Can only access port storage when docked at THAT port
- Cannot remotely access other ports' storage
- Ship must have grid space + weight capacity to load items
```

---

## Part 5: Drydock Storage Grid

### Core Concept

Drydock is a **separate Tetris grid** for storing inactive ships. Ships are treated as large items with their own grid dimensions.

```
DRYDOCK PROPERTIES
==================

Grid Shape: Standard rectangle
Capacity: Similar to port storage (adjustable)
Per-Port: Each port has separate drydock
Contents: Ships only (not cargo items)
```

### Ship Dimensions in Drydock

Ships occupy grid space based on their physical size:

```
SHIP GRID SIZES (Approximate, per-ship assigned)
================================================

PT Boats / Small Craft: 1x3 to 2x4
Destroyers: 2x5 to 3x6
Light Cruisers: 3x6 to 3x7
Heavy Cruisers: 3x7 to 4x8
Battlecruisers: 4x8 to 4x9
Battleships: 4x9 to 4x10
Carriers: 4x10 (largest)
Submarines: 1x4 to 2x6

Note: Exact sizes assigned per individual ship design,
not standardized by class. A large destroyer might be
bigger than a small light cruiser.
```

### Drydock Management

```
DRYDOCK WORKFLOW
================

Storing a Ship:
1. Dock active ship at port
2. Open drydock interface
3. Drag ship from "Active" slot to drydock grid
4. Ship becomes inactive (stored as grid item)
5. Can now activate a different ship or build new one

Activating a Ship:
1. Open drydock interface
2. Drag ship from drydock grid to "Active" slot
3. Previous active ship (if any) moves to drydock
4. New ship ready for customization and departure

Ship Cargo When Drydocked:
- Ship retains its cargo inventory
- Can access drydocked ship's cargo via port interface
- Can transfer items between drydocked ships and port storage
```

### Multi-Ship Strategy

```
DRYDOCK STRATEGIC USE
=====================

Fleet Composition:
├── Active: USS Iowa (battleship for current mission)
├── Drydocked: USS Fletcher (destroyer for convoy escort)
├── Drydocked: USS Essex (carrier for air operations)
└── Drydocked: Gato-class (submarine for patrol missions)

Switching Ships:
- Different missions require different ships
- Keep specialized ships drydocked at strategic ports
- Quick-swap before missions based on objectives

Port Hoarding Prevention:
- Drydock capacity limits ships per port
- If full, must sell/scuttle ships or relocate to other ports
- Encourages using ships, not just collecting them
```

---

## Part 6: Weight System Integration

### Universal Weight Rules

Weight applies to ALL grid systems:

```
WEIGHT APPLICATION
==================

Ship Cargo:
├── Hard cap at 100% weight capacity
├── Cannot exceed (items won't load)
├── Performance penalties at 80%+ load
└── See Inventory-System.md for penalty tiers

Equipment Slots:
├── Module weight + Crew weight ≤ Slot capacity
├── Checked before installation
└── See Crew-Module-Mechanics.md for crew weight formula

Wing Slots:
├── Aircraft stack weight + Pilot weight ≤ Wing capacity
├── Same validation as equipment slots
└── Pilot weight = Sailor_Count × 0.1 × (1 + Level/100)

Port Storage:
├── No weight limit (grid-only constraint)
└── Weight is tracked but doesn't restrict storage

Drydock:
├── No weight limit
└── Ships stored as items (their tonnage is abstracted)
```

### Weight Display in UI

```
WEIGHT INDICATORS
=================

Ship Cargo Screen:
┌─────────────────────────────────────────────┐
│ Weight: 185t / 200t (92.5%)                 │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░ [HEAVY LOAD -12% SPEED]│
│ Grid: 84 / 120 cells (70%)                  │
└─────────────────────────────────────────────┘

Color Coding:
├── Green (0-50%): Optimal
├── Light Green (50-80%): Minor penalties
├── Yellow (80-95%): Moderate penalties
├── Orange (95-100%): Heavy penalties
└── Red (100%): HARD CAP - Cannot add more

Equipment Slot:
┌─────────────────────────────────────────────┐
│ Main Battery Slot A [3x4]                   │
│ Capacity: 120t                              │
│ Module: 16"/50 Mk.7 (85t)                  │
│ Crew: Level 90 Gunner (91t)                │
│ Total: 176t → ❌ EXCEEDS CAPACITY          │
└─────────────────────────────────────────────┘
```

---

## Part 7: System Interactions

### Workflow: Full Ship Fitting

```
COMPLETE FITTING WORKFLOW
=========================

At Port:

1. EQUIPMENT FITTING (Slot-Matching)
   ├── Select ship in drydock or build new
   ├── Install modules to equipment slots
   │   └── Dimension match + Weight check
   ├── Assign crew cards to modules
   │   └── Weight check (module + crew)
   ├── Install aircraft to wing slots (carriers)
   │   └── Weight check (aircraft + pilot)
   └── Result: Ship is combat-ready

2. CARGO LOADING (True Tetris)
   ├── Open cargo grid
   ├── Load ammunition (shells, torpedoes)
   ├── Load fuel (ship fuel, plane fuel)
   ├── Load consumables (repair kits, etc.)
   ├── Load aircraft ordnance (carriers)
   ├── Leave space for loot
   └── Result: Ship provisioned for mission

3. DEPARTURE
   └── Undock and begin mission

During Mission:

4. COMBAT & EXTRACTION
   ├── Ammunition consumed from cargo
   ├── Fuel consumed from cargo
   ├── Loot picked up into cargo (Tetris placement)
   ├── Reserve aircraft moved to wing slots if needed
   └── Jettison cargo if emergency escape required

Return to Port:

5. UNLOADING (True Tetris)
   ├── Transfer loot from ship cargo to port storage
   ├── Sell loot or store for later
   ├── Restock ammunition and fuel
   └── Ready for next mission

6. SHIP MANAGEMENT
   ├── Store current ship in drydock
   ├── Activate different ship for different mission
   └── Transfer items between drydocked ships
```

### Item Flow Diagram

```
ITEM FLOW BETWEEN SYSTEMS
=========================

                    ┌─────────────┐
                    │   MARKET    │
                    │  (Buy/Sell) │
                    └──────┬──────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────┐
│                   PORT STORAGE                       │
│            (Tetris Grid - Rectangle)                │
│  [Ammo] [Modules] [Loot] [Crew Cards] [Fuel]       │
└───────────────────────┬─────────────────────────────┘
                        │
           ┌────────────┼────────────┐
           │            │            │
           ▼            ▼            ▼
    ┌──────────┐ ┌──────────┐ ┌──────────────┐
    │ DRYDOCK  │ │ACTIVE    │ │   FITTING    │
    │(Ships as │ │SHIP      │ │   SCREEN     │
    │ items)   │ │CARGO     │ │(Equipment    │
    │          │ │(Tetris)  │ │ Slots)       │
    └──────────┘ └────┬─────┘ └──────────────┘
                      │
                      ▼
              ┌───────────────┐
              │   AT SEA      │
              │ (Mission)     │
              │               │
              │ Loot → Cargo  │
              │ Ammo consumed │
              │ Fuel consumed │
              └───────────────┘
```

---

## Cross-Reference Documents

**Related Ship Customization:**
- [[Module-System]] - Equipment slot details, module categories
- [[Ship-Fitting-UI]] - Visual interface for fitting screens
- [[Module-Dependencies]] - Weight-based fitting validation

**Related Core Gameplay:**
- [[Inventory-System]] - Cargo grid mechanics (comprehensive)
- [[Crew-Module-Mechanics]] - Crew weight and efficiency formulas
- [[Crew-Management]] - Crew card storage and wallet system

**Related Combat Systems:**
- [[Carrier-Operations]] - Air operations gameplay
- [[Surface-Combat]] - Ammunition consumption

**Related Economy:**
- [[Extraction-Mechanics]] - Cargo loss on death, loot mechanics

---

## Summary

| System | Grid Type | Placement Style | Constraints |
|--------|-----------|-----------------|-------------|
| **Equipment Slots** | Fixed slots with dimensions | Exact dimension match | Dimension + Weight |
| **Wing Slots** | Fixed slots with capacity | Any aircraft type | Weight (aircraft + pilot) |
| **Ship Cargo** | Freeform Tetris | Place anywhere, rotate | Grid cells + Weight |
| **Port Storage** | Freeform Tetris | Place anywhere, rotate | Grid cells only |
| **Drydock** | Freeform Tetris | Ships as items | Grid cells only |

**Design Philosophy**: The Tetris systems create meaningful decisions at every level - what modules fit your ship, how much ammo to bring, how much loot space to reserve, and which ships to keep at which ports. Combined with the extraction-based economy, every grid cell and every ton of capacity becomes a strategic choice.

---

*Document created: 2025-12-10*
