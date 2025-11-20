# Ship Fitting UI

**Status**: 📋 PLANNED (Phase 2/3 feature)
**Tags**: [planned, phase2, ship-customization, ui-ux, interface-design]
**Priority**: HIGH (critical user experience)
**Related Systems**: [Module System](Module-System.md), [Armor Configuration](Armor-Configuration.md), [Utility Modules](Utility-Modules.md)

---

## Overview

The Ship Fitting Interface is a comprehensive multi-screen system allowing players to configure every aspect of their ship: weapons, internal systems, armor, cargo, and loadout presets. The interface emphasizes visual clarity, real-time feedback, and intuitive drag-and-drop interactions.

**Design Principles:**
- **Visual Clarity**: Clear indication of valid/invalid placements
- **Real-Time Feedback**: Instant weight, speed, cost calculations
- **Drag-and-Drop**: Intuitive module/weapon placement
- **Comprehensive Tooltips**: Detailed information on hover
- **Undo/Redo**: Safe experimentation with configuration changes
- **Accessibility**: Colorblind modes, keyboard shortcuts, scalable UI

---

## Interface Architecture

### Multi-Screen Navigation

**5 Primary Screens:**
1. **Weapon Hardpoint View** - Configure turrets and weapon systems
2. **Ship Systems Fitting** - Configure engines, support, and misc modules
3. **Armor Configuration** - Configure armor thickness and material per zone
4. **Cargo Grid Inventory** - Manage tetris-style cargo grid
5. **Loadout Presets** - Save/load complete ship configurations

**Navigation:**
- Tab-based switching at top of interface
- Keyboard shortcuts (1-5 keys) for instant screen switching
- Ctrl+Tab cycles through screens sequentially
- All screens share common bottom panel (ship stats summary)

---

## Screen 1: Weapon Hardpoint View

### Visual Layout

**Left Panel: Ship View (70% width)**
- **3D Ship Sprite**: Top-down view of ship with hardpoints highlighted
- **Non-Rotatable**: Fixed top-down perspective (2D game, no need for rotation)
- **Hardpoint Indicators**: Color-coded circles showing available hardpoint positions
  - **Main Battery**: Large circles (bow, stern, centerline) - Red outline
  - **Secondary Battery**: Medium circles (sides, superstructure) - Orange outline
  - **Tertiary/AA**: Small circles (deck positions) - Yellow outline
  - **Special Hardpoints**: Unique icons (torpedo tubes, catapults) - Blue outline

**Right Panel: Turret Inventory (30% width)**
- **Filter Options**: Dropdown menu (Main Battery, Secondary, AA, Special Weapons)
- **Sort Options**: Dropdown menu (By weight, caliber, damage, fire rate)
- **Turret Cards**: Scrollable list showing:
  - Turret model/name (e.g., "16"/50 Mk.7 Triple Turret")
  - Visual thumbnail (turret sprite)
  - Weight (tons) in large text
  - Damage/ROF stats in small text
  - Crew requirement icon (Gunner symbol)
  - Quality indicator (70-130% color-coded bar)
    - Red (70-85%): Poor quality
    - Yellow (86-95%): Below average
    - White (96-105%): Average
    - Green (106-115%): Above average
    - Blue (116-125%): Excellent
    - Purple (126-130%): Exceptional

**Bottom Panel: Real-Time Stats (100% width)**
- **Firepower Rating**: Aggregated damage output (0-10 scale + exact DPS)
- **AA Rating**: Anti-aircraft effectiveness (0-10 scale)
- **Total Weight**: Hardpoint weight sum (tons)
- **Ship Speed**: Max speed after weight penalties (knots)
- **Warnings**: Over-weight alerts, missing crew alerts (red text)

### Interaction Flow

**Drag-Drop Workflow:**
1. **Select Turret**: Click turret card in right panel
2. **Drag to Hardpoint**: Drag turret over ship view
3. **Visual Feedback**:
   - **Green Circle**: Valid placement (weight OK, crew assigned)
   - **Yellow Circle**: Valid but over-weight warning (speed penalty preview shown)
   - **Red Circle**: Invalid (exceeds weight capacity, no crew, incompatible)
4. **Drop to Install**: Release mouse to install turret
5. **Crew Assignment**: Popup appears: "Assign Gunner crew card to this turret?"
   - Dropdown list of available Gunner crew cards
   - Shows crew level, efficiency %, weight
   - Click to assign or skip (turret operates at 25% efficiency without crew)

**Hover Tooltips:**
- **Hardpoint Hover**: Shows hardpoint capacity, current turret (if any), crew assignment
- **Turret Card Hover**: Shows detailed stats comparison vs. currently installed turret
  - Damage change (green/red arrows)
  - Weight difference
  - ROF comparison
  - Expected efficiency with available crew

**Right-Click Context Menu:**
- **Installed Turret**: Right-click → Remove turret, Replace turret, Reassign crew
- **Empty Hardpoint**: Right-click → View hardpoint details, Lock hardpoint (prevent accidental placement)

### Example Layout (ASCII Representation)

```
┌─────────────────────────────────────────────────────────────────┐
│ WEAPON HARDPOINT CONFIGURATION          [Save] [Reset] [?]      │
│ [Hardpoints] [Systems] [Armor] [Cargo] [Presets]               │
├────────────────────────────────┬────────────────────────────────┤
│                                │ TURRET INVENTORY               │
│    [Ship Top-Down View]        │ ┌──────────────────────────┐  │
│                                │ │ 16"/50 Mk.7 (128%) ⭐    │  │
│    ◉ Main #1 (16"/50 Mk.7)    │ │ [Turret thumbnail]       │  │
│    ◉ Main #2 (16"/50 Mk.7)    │ │ Weight: 285 tons         │  │
│    ◉ Main #3 (EMPTY) ⚠️       │ │ Damage: 12,800 @ 2.5/min │  │
│    ⬤ Secondary #1-8 (5"/38)   │ │ Quality: 128% (Purple)   │  │
│    • AA #1-40 (40mm Bofors)   │ │ [Gunner Required] 👤     │  │
│    ≋ Torpedo #1-2 (Mk.15)     │ └──────────────────────────┘  │
│                                │ [Filter: Main Battery ▼]      │
│                                │ [Sort: By Weight ▼]           │
│                                │                                │
│    [Legend]                    │ ┌──────────────────────────┐  │
│    ◉ = Main Battery            │ │ 16"/45 Mk.6 (102%)       │  │
│    ⬤ = Secondary Battery       │ │ Weight: 270 tons         │  │
│    • = AA Mount                │ │ Damage: 11,500 @ 2.2/min │  │
│    ≋ = Torpedo Tubes           │ │ Quality: 102% (White)    │  │
│                                │ │ [Gunner Required] 👤     │  │
│                                │ └──────────────────────────┘  │
├────────────────────────────────┴────────────────────────────────┤
│ Firepower: 8.5/10 (24,500 DPS) | AA: 6.8/10 | Weight: 2,850t   │
│ Speed: 28kn (-5kn penalty) | Crew: 18/20 assigned               │
│ ⚠️ Warning: Main #3 unassigned (-33% firepower potential)      │
│ [Undo Last Change] [Redo] [Reset All] [Save Configuration]     │
└─────────────────────────────────────────────────────────────────┘
```

### Validation & Warnings

**Real-Time Validation:**
- **Green Checkmark** (✅): All hardpoints valid, crew assigned, within weight limits
- **Yellow Warning** (⚠️): Valid but suboptimal (missing crew, near weight limit)
- **Red Error** (❌): Invalid configuration (exceeds weight, incompatible modules)

**Warning Messages:**
- "Main Battery #3 unassigned - Operates at 25% efficiency without crew"
- "Total weight exceeds ship displacement - Speed reduced by 8 knots"
- "Recommended: Assign Level 90+ Gunner crew for optimal turret performance"

---

## Screen 2: Ship Systems Fitting Screen

### Visual Layout

**Center Panel: Ship Systems Grid (60% width)**
- **Grid-Based Slot Layout**: Ship cross-section showing internal systems
  - **Engine Section** (Left side, Orange background): 2-6 engine bay slots
  - **Support Section** (Center, Blue background): Variable support module slots
  - **Misc Section** (Right side, Purple background): Universal misc slots
- **Color-Coded Slots**:
  - Orange = Engine slots (engines only)
  - Blue = Support slots (support modules only)
  - Purple = Misc slots (universal acceptance)
- **Slot Size Indicators**: Each slot shows size (1x1, 1x2, 2x2, 2x3, 3x3)
- **Installed Modules**: Visual sprites showing installed modules

**Right Panel: Module Inventory (30% width)**
- **Tabbed Categories**: [Engines] [Support] [Misc] [All]
- **Filter Options**: By size (1x1, 1x2, 2x2, etc.), by function, by weight
- **Module Cards**: Similar layout to turret cards
  - Module name and thumbnail
  - Size (grid visual: "2x3" with grid overlay)
  - Weight (tons)
  - Effects (bullet points)
  - Crew requirement icon

**Bottom-Right Sub-Panel: Crew Assignment (20% width)**
- **Crew Card List**: All owned crew cards
- **Filter by Class**: Show only Engineers, Gunners, Support, etc.
- **Crew Cards**: Mini-cards showing:
  - Crew name/level (e.g., "Engineer Lvl 85")
  - Class icon
  - Weight (tons)
  - Efficiency preview (e.g., "100% efficiency on this module")
  - Availability (green = available, gray = already assigned)

**Bottom Panel: Real-Time Stats (100% width)**
- **Speed**: Max speed with current engines (knots)
- **Fuel Efficiency**: km per fuel unit
- **Crew Morale**: Aggregate morale bonus from support modules
- **Total Weight**: All modules + crew weight (tons / max displacement)
- **Warnings**: Over-weight, missing crew, incompatible modules

### Interaction Flow

**Module Installation:**
1. **Select Module**: Click module card in right panel (highlights module)
2. **Drag to Slot**: Drag module over ship systems grid
3. **Size Validation**: Module size must fit slot size
   - 1x1 module can fit 1x1, 2x2, or 3x3 slot (highlights compatible slots green)
   - 2x2 module CANNOT fit 1x1 slot (slot stays red)
4. **Visual Feedback**:
   - **Green Glow**: Compatible slot, valid placement
   - **Yellow Glow**: Compatible but over-weight warning
   - **Red Glow**: Invalid (wrong slot type, size mismatch, weight exceeded)
5. **Drop to Install**: Release mouse to install module
6. **Crew Assignment**: Popup appears with crew card selection dropdown

**Crew Assignment:**
1. **Drag Crew Card**: From crew panel to module's crew slot (small circle on module sprite)
2. **Validation**: Check class compatibility (Engineer → Engine, Support → Support module)
3. **Efficiency Display**: Shows expected efficiency % based on crew level vs. module level
4. **Assign**: Click to confirm assignment

**Slot Filtering:**
- **Hover over Slot**: Highlights all slots of same type
- **Click Slot Type Legend**: Filters module inventory to compatible modules only

### Example Layout (ASCII Representation)

```
┌──────────────────────────────────────────────────────────────────┐
│ SHIP SYSTEMS FITTING                     [Save] [Reset] [?]      │
│ [Hardpoints] [Systems] [Armor] [Cargo] [Presets]                │
├─────────────────────────────────┬────────────────────────────────┤
│ ENGINE BAYS (Orange)            │ MODULE INVENTORY               │
│ ┌───┬───┐ ┌───┬───┐           │ [Engines] [Support] [Misc]     │
│ │ E │ E │ │ E │ E │ (4 bays)  │ ┌────────────────────────┐     │
│ │ 1 │ 2 │ │ 3 │ 4 │           │ │ High-Eff Turbine       │     │
│ │👤│👤│ │👤│👤│ (all crewed)│ │ Size: 2x3   ⚡         │     │
│ └───┴───┘ └───┴───┘           │ │ +32kn, -20% fuel      │     │
│                                 │ │ Weight: 85 tons       │     │
│ SUPPORT SLOTS (Blue)            │ │ [Engineer Required] 👤│     │
│ ┌──┬──┐ ┌──┬──┬──┐            │ └────────────────────────┘     │
│ │S1│S2│ │S3│S4│S5│            │                                │
│ │👤│👤│ │👤│  │  │            │ CREW ASSIGNMENT                │
│ └──┴──┘ └──┴──┴──┘            │ ┌────────────────────────┐     │
│ ┌───┬───┬───┐                 │ │ Module: Engine Bay #1  │     │
│ │ S │ S │ S │ (8 slots)      │ │ Requires: Engineer     │     │
│ │ 6 │ 7 │ 8 │                 │ │ Assigned: Engr Lvl 90  │     │
│ │👤│  │  │                    │ │ Efficiency: 100% ✅    │     │
│ └───┴───┴───┘                 │ │                        │     │
│                                 │ │ [Change Crew]          │     │
│ MISC SLOTS (Purple)             │ │                        │     │
│ ┌──┐ ┌──┐ ┌──┬──┐            │ │ Available Crew:        │     │
│ │M1│ │M2│ │M3│M4│            │ │ - Engr Lvl 85 (450t)  │     │
│ │👤│ │👤│ │👤│  │            │ │ - Engr Lvl 120 (720t) │     │
│ └──┘ └──┘ └──┴──┘            │ │ - Support Lvl 75      │     │
│                                 │ └────────────────────────┘     │
├─────────────────────────────────┴────────────────────────────────┤
│ Speed: 32kn | Fuel Eff: 1.2km/unit | Morale: +25 | Wt: 4,200t   │
│ ✅ All systems operational | 18/20 crew assigned                │
│ ⚠️ Support slots 4-5 empty - No effect on ship performance      │
│ [Undo] [Redo] [Reset] [Save] [Auto-Assign Crew]                │
└──────────────────────────────────────────────────────────────────┘
```

### Auto-Assign Crew Feature

**Smart Crew Assignment:**
- **Auto-Assign Button**: Automatically assigns best-matched crew to modules
- **Algorithm**:
  1. Prioritize exact level matches (crew level = module level)
  2. Assign highest-level crew to highest-tier modules
  3. Ensure class compatibility (Engineer → Engine, Gunner → Turret)
  4. Maximize overall efficiency
- **Result**: All modules crew-assigned optimally
- **Manual Override**: Player can manually reassign after auto-assignment

---

## Screen 3: Armor Configuration

### Visual Layout

**Left Panel: Ship Schematic (60% width)**
- **Side Profile View**: Shows belt armor zones (Forward, Center, Aft)
  - Vertical colored bars showing armor thickness
  - Hover highlights specific zone
- **Top-Down View**: Shows deck armor zones (Forward, Center, Aft)
  - Horizontal colored bars showing armor thickness
- **Structural View**: Shows turret and conning tower armor
  - 3D sprite of turrets/tower with armor thickness overlay
- **Color-Coded Heat Map**: Visual representation of armor thickness
  - Blue = Thin armor (0-2")
  - Green = Moderate armor (2-6")
  - Yellow = Heavy armor (6-12")
  - Red = Maximum armor (12-18")

**Right Panel: Armor Zone Controls (40% width)**
- **9 Armor Zone Control Groups**: One per armor zone
  - Zone Name (e.g., "Forward Deck Armor")
  - Dropdown: Armor Type (RHA, Face-Hardened, Krupp, Terni, Ducol, STS)
  - Text Input: Thickness in inches (0.1" increments)
  - Slider: Quick adjustment (0.5" increments)
  - Increment Buttons: +0.1" / -0.1"
  - MM Equivalent: "(114.3mm)" displayed next to inches
- **Armor Type Legend**: Hover over dropdown shows armor type comparison table

**Bottom Panel: Real-Time Stats (100% width)**
- **Total Armor Weight**: Sum of all zones (tons)
- **Speed Impact**: Max speed reduction from armor weight (knots)
- **Protection Rating**: Aggregate armor effectiveness (0-10 scale)
- **Total Cost**: Credit cost for current armor configuration (₡)
- **Weight Remaining**: Available weight budget after armor (tons)

### Interaction Flow

**Per-Zone Configuration:**
1. **Select Zone**: Click zone on schematic (highlights zone, opens control group)
2. **Choose Armor Type**: Dropdown menu (RHA, Krupp, STS, etc.)
   - Hover shows comparison tooltip (protection coefficient, weight, cost)
3. **Set Thickness**:
   - **Manual Entry**: Type exact value (e.g., "10.5")
   - **Slider**: Drag slider for quick adjustment
   - **Increment Buttons**: Fine-tune with +/- 0.1" buttons
4. **Real-Time Feedback**: Stats update instantly
   - Armor weight recalculates
   - Speed penalty updates
   - Cost updates
   - Visual schematic color changes to reflect new thickness

**Armor Scheme Presets:**
- **Save Custom Scheme**: Button saves current configuration as named preset
  - Text input: "Enter scheme name" (e.g., "Iowa Maximum Protection")
  - Saves all 9 zones + armor types
- **Load Scheme**: Dropdown menu of saved presets
  - Historical refits (e.g., "Iowa 1945 Refit", "Iowa 1952 Modernization")
  - Player-saved presets
  - Community-shared presets (imported via code)
- **Quick Apply**: One-click to apply entire preset

**Validation Warnings:**
- **Red Text**: "Exceeds ship class maximum for Battleship (18.0" max belt)"
- **Yellow Text**: "Approaching weight limit (92% capacity)"
- **Green Text**: "Valid configuration within all limits"

### Example Layout (ASCII Representation)

```
┌──────────────────────────────────────────────────────────────────┐
│ ARMOR CONFIGURATION                      [Save] [Reset] [?]      │
│ [Hardpoints] [Systems] [Armor] [Cargo] [Presets]                │
├─────────────────────────────────┬────────────────────────────────┤
│ [Ship Side Profile View]        │ ARMOR ZONES                    │
│  Color-coded armor thickness    │                                │
│  [Red belt in center]           │ DECK ARMOR                     │
│  [Yellow belt fwd/aft]          │ Forward Deck:                  │
│  [Green deck armor]             │ [RHA ▼] [4.0" (101.6mm)]      │
│                                  │ [─────●─────] +0.1 -0.1       │
│ [Ship Top-Down View]            │ Center Deck:                   │
│  Showing deck armor zones       │ [RHA ▼] [6.0" (152.4mm)]      │
│  [Green fwd/aft]                │ [───────●───] +0.1 -0.1       │
│  [Yellow center]                │ Aft Deck:                      │
│                                  │ [RHA ▼] [4.0" (101.6mm)]      │
│ [Heat Map Legend]               │ [─────●─────] +0.1 -0.1       │
│ Blue  = 0-2"                    │                                │
│ Green = 2-6"                    │ SIDE BELT ARMOR                │
│ Yellow= 6-12"                   │ Forward Belt:                  │
│ Red   = 12-18"                  │ [STS ▼] [10.0" (254.0mm)]     │
│                                  │ [────────●──] +0.1 -0.1       │
│                                  │ Center Belt:                   │
│                                  │ [STS ▼] [12.1" (307.3mm)]     │
│                                  │ [─────────●─] +0.1 -0.1       │
│                                  │ Aft Belt:                      │
│                                  │ [STS ▼] [10.0" (254.0mm)]     │
│                                  │ [────────●──] +0.1 -0.1       │
│                                  │                                │
│                                  │ STRUCTURAL ARMOR               │
│                                  │ Conning Tower:                 │
│                                  │ [STS ▼] [7.25" (184.2mm)]     │
│                                  │ Main Turrets:                  │
│                                  │ [STS ▼] [17.0" (431.8mm)]     │
│                                  │ Secondary Turrets:             │
│                                  │ [STS ▼] [2.5" (63.5mm)]       │
├─────────────────────────────────┴────────────────────────────────┤
│ Armor Weight: 4,850t | Speed: 28kn (-5kn) | Protection: 9.2/10  │
│ Total Cost: ₡8,500,000 | Weight Budget: 2,150t remaining        │
│ [Load Preset ▼] [Save As New Preset] [Export Preset Code]      │
│ ✅ Valid configuration - All zones within ship class limits     │
└──────────────────────────────────────────────────────────────────┘
```

### Armor Type Comparison Tooltip

**Hover over Armor Type Dropdown:**
```
┌─────────────────────────────────────────────────────────┐
│ ARMOR TYPE COMPARISON (for 10" thickness)              │
├─────────────────────────────────────────────────────────┤
│ RHA (Standard)                                          │
│ Protection: 1.0x | Weight: 400t | Cost: ₡1.44M         │
│                                                         │
│ Face-Hardened                                           │
│ Protection: 1.3x AP / 0.8x HE | Weight: 450t | ₡2.02M │
│                                                         │
│ Krupp Cemented (German) ⭐                             │
│ Protection: 1.4x AP / 1.1x HE | Weight: 500t | ₡2.88M │
│                                                         │
│ Terni Steel (Italian)                                   │
│ Protection: 0.9x AP / 1.2x HE | Weight: 320t | ₡1.73M │
│                                                         │
│ Ducol Steel (British)                                   │
│ Protection: 0.85x AP / 1.0x HE | Weight: 280t | ₡1.58M│
│                                                         │
│ STS (US Premium) ⭐                                    │
│ Protection: 1.15x AP / 1.15x HE | Weight: 420t |₡2.59M│
└─────────────────────────────────────────────────────────┘
```

---

## Screen 4: Cargo Grid Inventory

### Visual Layout

**Left Panel: Cargo Grid (70% width)**
- **Tetris-Style Grid**: Ship's cargo hold represented as grid cells
  - Grid dimensions variable based on ship tier and class (total capacity defines layout)
  - Example capacities: T1 destroyers (~80-100 cells), T5 battleships (~300 cells), T10 carriers (~700 cells)
  - Grid layout optimized for ship hull shape (wider for carriers, taller for battleships)
  - Cell size: ~20x20 pixels per cell (scalable based on total grid size)
- **Item Representation**: Visual blocks showing item shapes and sizes
  - Items displayed as colored rectangles occupying multiple cells
  - Item icons/sprites overlay on blocks
- **Color-Coding**:
  - Grey = Empty cells
  - Yellow = Ammunition (shells, torpedoes)
  - Green = Resources (steel, oil, coal)
  - Blue = Modules/equipment
  - Purple = Special items (blueprints, rare loot)
- **Grid Overlay**: Subtle grid lines for cell boundaries

**Right Panel: Item List (30% width)**
- **Owned Items**: All items in port storage not on ship
- **Filter Dropdown**: By type (All, Ammo, Resources, Modules, Special)
- **Sort Dropdown**: By weight, size, value, name
- **Search Bar**: Text search for specific items
- **Item Cards**: Scrollable list showing:
  - Item name and icon
  - Size (e.g., "2x3")
  - Weight (tons)
  - Quantity (if stackable)
  - Value (₡)

**Bottom Panel: Weight Display (100% width)**
- **Current Weight**: Real-time total cargo weight (bold, large text)
- **Max Weight**: Ship's cargo capacity limit
- **Visual Meter**: Progress bar showing weight percentage
  - Green (0-70%): Safe load
  - Yellow (70-90%): Moderate load
  - Red (90-100%): Maximum load
  - Flashing Red (100%+): Over-weight (can't undock)
- **Grid Usage**: X / Y cells occupied (e.g., "128 / 320 cells (40%)")

### Interaction Flow

**Item Placement:**
1. **Select Item**: Click item in right panel item list
2. **Preview Placement**: Item follows mouse cursor over grid
   - Semi-transparent preview shows where item will place
   - Green outline = valid placement (no collision, within grid)
   - Red outline = invalid (collision or out of bounds)
3. **Rotation**: Press R key to rotate item 90° clockwise
   - Item orientation changes (2x3 → 3x2)
   - Preview updates in real-time
4. **Drop to Place**: Click to place item in grid
   - Item snaps to grid cells
   - Weight updates instantly
   - Cell colors update

**Item Management:**
- **Move Item**: Click and drag placed item to new location
- **Remove Item**: Drag item out of grid → returns to item list
- **Stack Items**: Some items stack (ammo, resources) - drag onto existing stack
- **Quick Remove**: Right-click item → "Remove from cargo"

**Auto-Sort Feature:**
- **Auto-Sort Button**: Automatically organizes items efficiently
- **Algorithm**: Tetris solver optimizes item placement
  - Minimizes wasted space
  - Groups similar items together
  - Prioritizes heavy items at bottom (realistic weight distribution)
- **Result**: Optimal grid utilization

**Collision Detection:**
- Items cannot overlap
- Items cannot extend outside grid boundaries
- Real-time validation during drag

### Example Layout (ASCII Representation)

```
┌──────────────────────────────────────────────────────────────────┐
│ CARGO GRID INVENTORY                     [Save] [Reset] [?]      │
│ [Hardpoints] [Systems] [Armor] [Cargo] [Presets]                │
├─────────────────────────────────┬────────────────────────────────┤
│ CARGO GRID (16x20 cells)       │ ITEM LIST                      │
│ ┌─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┬─┐ │ [Filter: All ▼]               │
│ │█│█│ │ │ │ │ │ │ │ │ │ │ │ │ │ [Sort: By Size ▼]             │
│ │█│█│ │▓│▓│▓│ │ │ │ │ │ │ │ │ │ [Search: ______]              │
│ │ │ │ │▓│▓│▓│ │ │ │ │ │ │ │ │ │                                │
│ │ │ │ │▓│▓│▓│ │ │ │ │ │ │ │ │ │ ┌────────────────────────┐    │
│ │ │ │ │ │ │ │ │░│░│ │ │ │ │ │ │ │ 16" AP Shells (100)    │    │
│ │ │ │ │ │ │ │ │░│░│ │ │ │ │ │ │ │ Size: 2x3  Weight: 8t  │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ [Ammo] 💥             │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ Value: ₡50,000         │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └────────────────────────┘    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ ┌────────────────────────┐    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ Steel (500 tons)       │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ Size: 5x4  Weight: 500t│    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ [Resource] 🔩          │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ Value: ₡50,000         │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ └────────────────────────┘    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ ┌────────────────────────┐    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ Advanced Radar (120%)  │    │
│ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ Size: 2x2  Weight: 28t │    │
│ └─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘ │ │ [Module] 📡            │    │
│                                  │ │ Value: ₡1,200,000      │    │
│ Legend:                          │ └────────────────────────┘    │
│ █ = 16" AP Shells (2x2)         │                                │
│ ▓ = Steel Resources (5x4)       │ [Auto-Sort Inventory]          │
│ ░ = Radar Module (2x2)          │ [Load from Port Storage]       │
│                                  │ [Unload All to Port]           │
├─────────────────────────────────┴────────────────────────────────┤
│ Weight: 2,450t / 5,000t (49%) ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ [SAFE]       │
│ Grid Usage: 128 / 320 cells (40%)                                │
│ [Rotate Item: R key] [Undo] [Redo] [Reset Cargo]                │
└──────────────────────────────────────────────────────────────────┘
```

### Weight Management

**Over-Weight Warning System:**
- Real-time weight calculation during item placement
- Color-coded weight indicator:
  - Green (0-80%): Optimal performance
  - Yellow (80-100%): Minor penalty warning (-5% speed)
  - Orange (100-120%): Moderate penalty warning (-15% speed, -30% acceleration)
  - Red (120%+): Severe penalty warning (-25% speed, -50% acceleration)
- Weight display shows: "Current: 2,450t / 2,000t (122% - Severe Penalty)"
- Tooltip on hover: "Over-weight ships suffer speed/acceleration/turn rate penalties. See Inventory System for details."
- **Players CAN undock over-weight** (soft cap with performance penalties, not hard block)

**Weight Optimization Tips:**
- Tooltip shows: "Tip: Remove low-value resources to make room for high-value loot"
- Auto-Sort prioritizes valuable items if weight-constrained

---

## Screen 5: Loadout Presets (Future Feature)

### Visual Layout

**Center Panel: Preset Cards Grid (80% width)**
- **Card-Based Layout**: Saved loadouts displayed as large cards
  - 2-3 cards per row
  - Scrollable vertically
- **Preset Card Contents**:
  - Preset name (large text, editable)
  - Creator name (player who created/imported preset)
  - Rating (1-5 stars, community ratings)
  - Ship class (e.g., "Iowa-class Battleship")
  - Visual thumbnail (ship sprite with loadout icons)
  - Stats summary (Firepower, Speed, Armor, AA ratings 0-10)
  - Cost to Apply (total credit cost for missing modules)
  - Tags (e.g., "AA Build", "Speed Build", "Balanced")

**Right Panel: Preset Details (20% width)**
- **Selected Preset**: Expanded details for clicked preset
  - Full module list (turrets, engines, support, misc)
  - Armor configuration summary
  - Crew requirements (total crew cards needed)
  - Module ownership status:
    - Green checkmark: Already owned
    - Red X: Need to purchase (shows cost)
  - Total cost breakdown

**Bottom Panel: Action Buttons (100% width)**
- [Apply Preset] - One-click application (purchases missing modules)
- [Preview] - Shows what ship will look like
- [Share] - Export preset code for sharing
- [Delete] - Remove preset from library
- [Create New Preset] - Save current configuration as preset

### Interaction Flow

**Saving Preset:**
1. **Configure Ship**: Use Hardpoint/Systems/Armor screens to configure ship
2. **Click "Save As Preset"**: Button appears on any fitting screen
3. **Preset Creation Dialog**:
   - Text input: Preset name (e.g., "Iowa AA Specialist")
   - Text area: Description (optional, markdown supported)
   - Tags: Multi-select (AA Build, Speed, Armor, Balanced, Budget, Premium)
   - Save scope: Private (only you), Public (share with community)
4. **Confirm Save**: Preset appears in Loadout Presets screen

**Loading Preset:**
1. **Click Preset Card**: Selects preset, shows details in right panel
2. **Click "Apply Preset"**:
   - System checks module ownership
   - Displays "Purchase Missing Modules?" dialog:
     - Lists missing modules with costs
     - Total cost summary
     - Options: [Purchase All and Apply] [Cancel]
3. **Confirm Purchase**: Modules purchased, ship configuration applied instantly
4. **Crew Assignment**: Popup: "Assign crew automatically?" [Yes] [No]

**Sharing Preset:**
1. **Click "Share" Button**
2. **Export Dialog**:
   - Generates alphanumeric code (e.g., "IOWA-AA-2F8K9X")
   - Copy to clipboard button
   - QR code (for mobile sharing)
   - "Share to Community" button (uploads to public preset library)
3. **Import Preset**: Button on main screen "Import Preset Code"
   - Paste code → Loads preset into library

### Example Preset Card

```
┌────────────────────────────────────────┐
│ LOADOUT: "Iowa Maximum Firepower"     │
│ By: PlayerName | Rating: ⭐⭐⭐⭐⭐     │
│ [Ship thumbnail with weapon icons]     │
├────────────────────────────────────────┤
│ Turrets: 3x Triple 16"/50 Mk.7 (130%) │
│ Engines: 4x High-Performance Turbines  │
│ Armor: Maximum Protection (STS)        │
│ Support: Damage Control, Medical Bay   │
│ Misc: Advanced Radar, Fire Control     │
├────────────────────────────────────────┤
│ Stats: Firepower 10/10 | Speed 6/10   │
│       Armor 9/10 | AA 7/10             │
├────────────────────────────────────────┤
│ Cost to Apply: ₡12,500,000             │
│ Owned: 18/25 modules ✅                │
│ Missing: 7 modules (₡4,200,000) ❌    │
├────────────────────────────────────────┤
│ [Preview] [Apply] [Share] [Delete]     │
│ Tags: [Firepower] [Armor] [T8] [PvP]  │
└────────────────────────────────────────┘
```

### Community Preset Library

**Browse Community Presets:**
- **Filter Options**:
  - Ship Class (Destroyer, Cruiser, Battleship, Carrier)
  - Tier Range (T1-T3, T4-T6, T7-T10)
  - Build Type (AA, Speed, Armor, Firepower, Budget, Balanced)
  - Rating (4+ stars, 3+ stars, All)
- **Sort Options**:
  - Most Popular (downloads)
  - Highest Rated
  - Newest
  - Most Expensive
  - Cheapest

**Preset Rating System:**
- Players who use preset can rate 1-5 stars
- Comments/reviews (optional)
- Upvote/downvote system
- Creator reputation builds over time

---

## Accessibility & User Experience Features

### Colorblind Modes

**Supported Modes:**
- **Deuteranopia** (Red-Green colorblindness)
- **Protanopia** (Red-Blind)
- **Tritanopia** (Blue-Yellow colorblindness)

**Color Scheme Alternatives:**
- **Standard**: Green (valid), Yellow (warning), Red (invalid)
- **Deuteranopia**: Blue (valid), Orange (warning), Pink (invalid)
- **Protanopia**: Blue (valid), Yellow (warning), Brown (invalid)
- **Tritanopia**: Green (valid), Purple (warning), Red (invalid)

**Additional Indicators:**
- Icons supplement color (✅ checkmark, ⚠️ warning, ❌ error)
- Pattern overlays (stripes for warnings, crosshatch for errors)
- Text labels ("Valid", "Warning", "Invalid")

### Keyboard Shortcuts

**Global Shortcuts:**
- **Ctrl+S**: Save configuration
- **Ctrl+Z**: Undo last change
- **Ctrl+Y / Ctrl+Shift+Z**: Redo
- **Tab**: Switch between screens (cycles 1→2→3→4→5→1)
- **1-5 Keys**: Jump to specific screen (1=Hardpoints, 2=Systems, 3=Armor, 4=Cargo, 5=Presets)
- **Esc**: Close fitting interface (prompts to save if changes made)

**Hardpoint View Shortcuts:**
- **Q/E**: Cycle through hardpoints (forward → back)
- **Delete**: Remove selected turret
- **C**: Open crew assignment dialog

**Systems View Shortcuts:**
- **Q/E**: Cycle through slots
- **R**: Rotate module (before placement)
- **Delete**: Remove selected module
- **C**: Open crew assignment dialog

**Cargo View Shortcuts:**
- **R**: Rotate item (before placement)
- **Ctrl+A**: Auto-sort inventory
- **Delete**: Remove selected item

### Tooltips & Help

**Comprehensive Tooltips:**
- **Hover over ANY element**: Shows detailed tooltip after 0.5 second
- **Tooltip Contents**:
  - Element name and description
  - Current value/status
  - Comparison to baseline (if applicable)
  - Tips/recommendations (if relevant)
  - Related keyboard shortcuts

**Comparison Tooltips:**
- **Hover over Module in Inventory**: Shows stat comparison vs. currently installed module
  - Green arrows (↑): Improvement
  - Red arrows (↓): Downgrade
  - Gray equals (=): No change
- **Side-by-side Stats**: Current module vs. hovered module

**Help Button (?):**
- **Top-Right Corner**: Always visible "?" button
- **Click to Open**: Context-sensitive help dialog
  - Explains current screen
  - Shows relevant tutorials
  - Links to wiki/documentation

### Undo/Redo System

**Change Tracking:**
- Every modification tracked (turret placement, module installation, armor change, cargo placement)
- Unlimited undo history (session-based, resets on save)
- Redo available if undo performed

**Undo Visualization:**
- **Status Bar**: Shows last action (e.g., "Installed 16" Turret on Main #1")
- **Undo Button**: Shows action that will be undone on hover
- **Redo Button**: Shows action that will be redone on hover

**Save Confirmation:**
- **Unsaved Changes Warning**: If user tries to close interface with unsaved changes
  - Dialog: "You have unsaved changes. Save before exiting?"
  - Options: [Save and Exit] [Discard Changes] [Cancel]

---

## Performance Optimization

### Lazy Loading

**Module Lists:**
- Display first 20 modules immediately
- Load additional modules on scroll (infinite scroll)
- Reduces initial load time

**Cargo Grid:**
- Only render visible cells (viewport culling)
- Items outside view not rendered until scrolled into view

### Caching

**Ship Configurations:**
- Cache ship configurations locally (browser storage / app data)
- Instant loading of previously viewed configurations
- Reduce server calls

**Module Database:**
- Cache module stats and images locally
- Update cache periodically (daily)

### Batch Operations

**Apply Multiple Changes:**
- Queue up multiple module installations
- Submit all changes to server in single API call
- Reduces network latency

---

## Summary

**Complete Ship Fitting UI Includes:**

✅ **5 Comprehensive Screens**: Hardpoints, Systems, Armor, Cargo, Presets
✅ **Intuitive Drag-and-Drop**: Visual, real-time feedback on all placements
✅ **Real-Time Validation**: Instant weight, cost, speed calculations
✅ **Detailed Tooltips**: Comprehensive information on hover
✅ **Accessibility Features**: Colorblind modes, keyboard shortcuts, scalable UI
✅ **Auto-Assign Features**: Smart crew assignment, auto-sort inventory
✅ **Loadout Presets**: Save, load, share complete ship configurations
✅ **Undo/Redo System**: Safe experimentation with configurations
✅ **Performance Optimized**: Lazy loading, caching, batch operations

**Integration Points:**
- Module System: UI reflects module slot constraints and compatibility
- Armor Configuration: Visual schematic shows armor zones and thickness
- Utility Modules: All support/misc modules accessible via Systems screen
- Technology Integration: Module effects visible in tooltips and stats

**User Experience Goals:**
- **Clarity**: Always show what is valid/invalid and why
- **Feedback**: Instant response to all actions
- **Flexibility**: Multiple ways to accomplish tasks (drag-drop, keyboard, auto-assign)
- **Safety**: Undo/redo prevents mistakes, save confirmation prevents accidental data loss
- **Accessibility**: Support for diverse player needs (colorblind, keyboard-only, etc.)

---

**End of Ship Fitting UI Specification**
