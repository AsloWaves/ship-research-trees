# Research & Unlock System

**Status**: 📋 IN DEVELOPMENT
**Tags**: [core-mechanics, progression, research, unlocks, war-thunder-inspired, phase2]
**Priority**: HIGH (foundational progression system)
**Last Updated**: 2025-12-10

---

## Overview

Fathoms Deep uses a War Thunder-inspired research system where players earn **Research Points (RP)** through gameplay and allocate them to unlock ships, turrets, and modules. Unlike traditional MMOs, this system emphasizes:

- **Active Progression**: RP earned through combat and extraction, not time-gated
- **Player Agency**: Manual RP allocation to chosen research targets
- **Hull-Only Ships**: Ships unlock as bare hulls - modules researched separately
- **Nation-Specific**: RP earned on USN ships only applies to USN research
- **Build OR Buy**: Unlocked items can be built (resources + time) or purchased (market)

**Core Design Philosophy**: Players should fully understand the game before reaching T5 (gateway to Battleships/Carriers and first permadeath tier for destroyers).

---

## Part 1: Research Points (RP)

### What Are Research Points?

RP is the currency used to unlock ships, turrets, and modules. RP is:
- **Earned through gameplay** (combat, extraction, missions)
- **Nation-specific** (USN RP only works on USN tree)
- **Manually allocated** (player chooses what to research)
- **Non-expiring** (can be saved indefinitely)
- **Account-wide within nation** (not per-ship)

### RP Generation

RP is generated through various in-game actions:

#### Combat Actions

| Action | Base RP | Notes |
|--------|---------|-------|
| Damage dealt (per 1,000 HP) | 1 RP | Scales with damage output |
| Ship kill (Assist) | 5 RP | Participated in kill (dealt damage) |
| Ship kill (Solo) | 15 RP | Final blow + majority damage |
| Aircraft shot down | 2 RP | AA defense contribution |
| Torpedo hit | 5 RP | Skill-based weapon reward |
| Citadel hit | 3 RP bonus | Precision gunnery bonus |
| Critical hit (module destroyed) | 2 RP bonus | Tactical targeting |

#### Survival & Extraction

| Action | Base RP | Notes |
|--------|---------|-------|
| Successful extraction | 10 RP | Made it back to port alive |
| Extraction with valuable loot | +5 RP per item | Rare modules, blueprints, etc. |
| Survived combat engagement | 3 RP | Participated in battle, lived |
| Escaped pursuit | 5 RP | Evaded enemy after being spotted |

#### Discovery & Intelligence

| Action | Base RP | Notes |
|--------|---------|-------|
| New area discovered | 5 RP | First visit to map zone |
| Enemy fleet reported | 1 RP | Intel contribution (spotted enemy) |
| Wreck salvaged | 2 RP | Extraction gameplay |
| Intel delivered to port | 3 RP | Brought back intelligence items |

#### Mission Completion

| Action | Base RP | Notes |
|--------|---------|-------|
| Mission completed (Easy) | 10 RP | Basic missions |
| Mission completed (Medium) | 25 RP | Standard difficulty |
| Mission completed (Hard) | 50 RP | High difficulty |
| Convoy escort successful | 20 RP | Team coordination |
| Objective captured | 15 RP | Area control |

### Ship Tier RP Multiplier

Higher-tier ships generate more RP to compensate for higher research costs:

| Ship Tier | RP Multiplier |
|-----------|---------------|
| T1-T2 | 1.0x |
| T3-T4 | 1.1x |
| T5-T6 | 1.25x |
| T7-T8 | 1.35x |
| T9 | 1.45x |
| T10 | 1.5x |

**Example**: A T7 destroyer earns a solo kill:
- Base RP: 15
- T7 Multiplier: 1.35x
- Earned: 15 × 1.35 = 20.25 → 20 RP

### RP Pool Management

```
RP POOL MECHANICS
=================

Earning RP:
├── Combat/Extraction actions generate RP
├── RP goes into single nation-specific pool
├── USN gameplay → USN RP pool
├── IJN gameplay → IJN RP pool (if unlocked)
└── Pools are completely separate

Allocating RP:
├── Open Research Tree at port
├── Select research target (ship, turret, or module)
├── Click "Allocate RP" button
├── Manually enter amount to allocate
├── RP deducted from pool, added to research progress
└── Can allocate to multiple targets over time

Research Completion:
├── When allocated RP reaches threshold
├── Item unlocks (can now build or purchase)
├── No free item provided - must acquire separately
└── Next items in tree become visible
```

---

## Part 2: Research Trees

### Three Separate Tree Types

Players research three distinct categories, each with its own tree:

| Tree Type | Contents | Structure |
|-----------|----------|-----------|
| **Ship Tree** | Hull designs by class | Linear + Branching |
| **Turret Tree** | Weapon systems | Linear progression |
| **Module Tree** | Equipment (radar, engines, etc.) | Category-based |

All trees are **nation-specific** - USN has its own ship/turret/module trees, IJN has separate trees, etc.

### Tree Visibility

**Fog of War Design**: Players can only see:
- Currently researched items
- **Next immediate unlocks** (adjacent in tree)
- Everything else is hidden

This creates:
- Discovery and anticipation
- Prevents overwhelming new players
- Encourages exploration of the tree
- Can be changed to full visibility later if desired

### Ship Research Tree Structure

Ship trees combine linear progression with branching paths:

```
USA DESTROYER TREE EXAMPLE (Simplified)
=======================================

Bainbridge-Class (STARTER - FREE)
       │
       ▼
Truxtun-Class
       │
   ┌───┴───┐
   ▼       ▼
Smith    Cassin
   │       │
   └───┬───┘
       ▼
   O'Brien-Class
       │
   ┌───┴───┐
   ▼       ▼
Tucker  Sampson
   │       │
   ▼       ▼
[continues branching...]
       │
       ▼
   Sims-Class ◄─── KEY NODE (Gateway to CV/BB)
       │
   ┌───┴───┐
   ▼       ▼
Benson  [→ Carriers]
   │    [→ Battleships]
   ▼
Gleaves
   │
[continues to modern destroyers...]
   │
   ▼
Zumwalt-Class (END OF LINE)
```

### Ship Tree Categories (USA Example)

Based on the USA Ship Tree canvas:

| Category | Ships | Starting Point | End Point |
|----------|-------|----------------|-----------|
| **Destroyers** | ~30 | Bainbridge | Zumwalt |
| **Submarines** | ~50 | F-Class | SSN-X |
| **Cruisers** | ~25 | Early cruisers | Ticonderoga |
| **Battleships** | ~20 | Indiana-Class | Montana |
| **Carriers** | ~25 | Langley | Gerald R. Ford |
| **Transports** | Various | Cargo ships | Assault ships |

### Cross-Category Prerequisites

Some ship categories require research in other categories first:

```
CATEGORY UNLOCK REQUIREMENTS
============================

Destroyers:
└── Available immediately (starter ship)

Submarines:
└── Research [TBD destroyer] to unlock submarine tree

Carriers:
└── Research Sims-Class Destroyer first
└── Then Langley-Class becomes available

Battleships:
└── Research Sims-Class Destroyer first
└── Then early battleship line becomes available

Transports:
└── [TBD requirements]
```

### Turret Research Tree

Turrets have their own research progression, separate from ships:

```
USA MAIN GUN TREE EXAMPLE
=========================

3-inch/50 (Starter)
       │
       ▼
4-inch/50
       │
       ▼
5-inch/38 ◄─── Standard DD armament
       │
   ┌───┴───┐
   ▼       ▼
5"/54   6-inch/47
   │       │
   ▼       ▼
[DD guns] [CL guns]
           │
           ▼
       8-inch/55 ◄─── Heavy cruiser
           │
           ▼
       12-inch
           │
           ▼
       14-inch
           │
           ▼
       16-inch/45 ◄─── Battleship standard
           │
           ▼
       16-inch/50 (Iowa)
           │
           ▼
       18-inch (Montana, theoretical)
```

### Module Research Tree

Modules are organized by category, each with progression:

```
USA MODULE TREE CATEGORIES
==========================

RADAR:
├── Basic Radar (30km) → Improved (50km) → Advanced (80km)
├── Late-War Integrated (120km) → AEGIS (150km)
└── Each requires previous in line

FIRE CONTROL:
├── Optical Rangefinder → Mechanical FC → Electronic Analog
├── Digital FC → AI-Assisted FC
└── Linear progression

SONAR:
├── Passive Sonar → Active Sonar → Advanced Sonar
└── Linear progression

ENGINES:
├── Steam Turbine (Basic) → Steam Turbine (Improved)
├── Diesel → Diesel (High-Performance)
├── Nuclear (requires late submarine/carrier research)
└── Multiple paths based on propulsion type

DAMAGE CONTROL:
├── Basic DC Station → Improved DC → Advanced DC
└── Linear progression

ELECTRONICS/EW:
├── Basic Jammer → Advanced Jammer
├── SIGINT Module
├── Decoy Transmitter
└── Multiple parallel paths
```

---

## Part 3: Research Costs

### Fixed RP Costs

Each item has a fixed RP cost regardless of how it's researched:

#### Ship Hull Costs (Examples)

| Tier | Ship Example | RP Cost |
|------|--------------|---------|
| T1 | Bainbridge-Class | FREE (Starter) |
| T2 | Truxtun-Class | 2,500 RP |
| T3 | Wickes-Class | 8,000 RP |
| T4 | Farragut-Class | 25,000 RP |
| T5 | Sims-Class | 75,000 RP |
| T6 | Fletcher-Class | 150,000 RP |
| T7 | Gearing-Class | 300,000 RP |
| T8 | Forrest Sherman-Class | 500,000 RP |
| T9 | Spruance-Class | 800,000 RP |
| T10 | Arleigh Burke-Class | 1,200,000 RP |

**Note**: These are placeholder values for design reference. Final balancing TBD.

#### Turret Costs (Examples)

| Caliber | Turret Example | RP Cost |
|---------|----------------|---------|
| 3-inch | 3"/50 | FREE (Starter) |
| 4-inch | 4"/50 | 1,500 RP |
| 5-inch | 5"/38 Twin | 10,000 RP |
| 6-inch | 6"/47 Triple | 35,000 RP |
| 8-inch | 8"/55 Triple | 80,000 RP |
| 12-inch | 12"/50 Triple | 150,000 RP |
| 14-inch | 14"/45 Triple | 250,000 RP |
| 16-inch | 16"/50 Triple (Iowa) | 400,000 RP |

#### Module Costs (Examples)

| Category | Module | RP Cost |
|----------|--------|---------|
| Radar | Basic Radar | 5,000 RP |
| Radar | Advanced Radar | 50,000 RP |
| Radar | AEGIS | 200,000 RP |
| Fire Control | Mechanical FC | 15,000 RP |
| Fire Control | Digital FC | 100,000 RP |
| Engine | Steam Turbine (Improved) | 20,000 RP |
| Engine | Nuclear Reactor | 300,000 RP |

---

## Part 4: Acquisition After Research

### Research Unlocks, Doesn't Provide

**Critical Distinction**: Completing research **unlocks** the item - it does NOT give you a free copy.

```
RESEARCH COMPLETION FLOW
========================

Research Complete:
├── Item blueprint/design unlocked
├── Player can now ACQUIRE the item
├── Two acquisition paths:
│   ├── BUILD: Resources + Time at shipyard
│   └── BUY: Purchase from market (players or NPCs)
└── Must choose one to obtain item
```

### Building Items

Players can build unlocked items at port:

```
BUILDING REQUIREMENTS
=====================

Ships:
├── Researched hull unlocked
├── Required resources (steel, aluminum, electronics, etc.)
├── Build time (hours to days depending on tier)
├── Port with shipyard capability
└── Credits for labor/facilities

Turrets:
├── Researched turret unlocked
├── Required resources (steel, ordnance components)
├── Shorter build time than ships
└── Credits for labor

Modules:
├── Researched module unlocked
├── Required resources (varies by module type)
├── Shortest build time
└── Credits for labor
```

### Purchasing Items

Alternatively, players can buy from the market:

```
MARKET PURCHASE
===============

Sources:
├── Player Market: Other players selling built items
├── NPC Vendors: Fixed stock, standard pricing
└── Black Market: Any nation's equipment (200-400% markup)

Advantages:
├── Instant acquisition (no build time)
├── Can buy higher-quality RNG rolls from players
└── Access to items you haven't researched (Black Market)

Disadvantages:
├── More expensive than building
├── Dependent on market availability
└── Black Market has heavy markup
```

### Ships Come Hull-Only

**Important**: Researched ships are **bare hulls** with NO equipment:

```
HULL-ONLY SHIPS
===============

When you research/build Fletcher-Class:
├── You get: Empty Fletcher hull
├── You DON'T get: Turrets, radar, engines, etc.
└── You MUST: Equip from your existing inventory OR research/build modules

Equipment Sources:
├── Research turrets/modules in their respective trees
├── Build or buy turrets/modules
├── Use ANY compatible equipment you already own
├── Salvage from wrecks (extraction gameplay)
└── Buy from market

Flexibility:
├── Can put ANY fitting turret on ANY ship (if it fits)
├── Not locked to "Fletcher's 5-inch guns"
├── 1920s destroyer with 1980s radar? If it fits, it works!
└── Weight-based fitting is only restriction
```

---

## Part 5: Blueprints (Rare Loot)

### What Are Blueprints?

Blueprints are **extremely rare loot drops** that provide instant research completion:

```
BLUEPRINT MECHANICS
===================

Finding Blueprints:
├── Drop from high-value targets
├── Found in rare cargo
├── Salvaged from wrecks
├── Extremely low drop rate
└── High-tier zones have better chances

Using Blueprints:
├── Instantly unlocks specific ship/turret/module
├── Consumes the blueprint (one-time use)
├── CANNOT continue research from that point
├── Must bring regular research to that node to progress further
└── Skips RP cost for that specific item only

Trading Blueprints:
├── Can be sold on player market
├── Can be sold to NPC traders
├── High value trade goods
└── Strategic decision: Use or sell?
```

### Blueprint Limitation

```
BLUEPRINT RESEARCH BLOCKING
===========================

Example: Player finds "Iowa-Class Blueprint"
├── Uses blueprint → Iowa-Class instantly unlocked
├── Player can build/buy Iowa-Class immediately
├── BUT: Cannot research Montana-Class (next in line)
├── WHY: Iowa research node shows 0/400,000 RP (not researched)
└── SOLUTION: Must earn RP and research Iowa normally to unlock Montana

Design Intent:
├── Blueprints provide shortcuts, not free progression
├── Players can't skip entire research lines
├── Still rewards rare find with immediate access
└── Maintains research engagement
```

---

## Part 6: Nation System

### Starting Nation

New players choose a **starting nation** during account creation:

```
NATION SELECTION
================

Account Creation:
├── Select starting nation (USA, Japan, Germany, UK, etc.)
├── Receive starter ship for that nation
├── RP earned goes to that nation's pool
└── Research that nation's trees

Starter Package (USA Example):
├── Bainbridge-Class Destroyer (hull)
├── Basic starter turrets (3"/50)
├── Basic modules (starter radar, basic engine)
├── Full crew complement for all positions
├── Ammunition and supplies for first sorties
└── Small credit balance
```

### Nation Switching

Players can access other nations, but with restrictions:

```
NATION SWITCHING MECHANICS
==========================

Separate Characters:
├── Each nation is a SEPARATE character
├── Same account, same username
├── Username displays nation tag: "[USN] PlayerName"
├── RP pools completely separate
├── Inventories completely separate
└── Ships/crew completely separate

Time Gate:
├── After logging out of one nation
├── 1-HOUR COOLDOWN before switching nations
├── Prevents intel exploitation
└── Example: Can't spot convoy on USN, switch to Germany, intercept

Intel Protection:
├── Ship positions take time (travel)
├── Switching nations could reveal enemy fleet locations
├── Time gate prevents "spy switching"
└── Strategic intel remains valuable
```

### Why Time-Gated Switching?

```
INTEL EXPLOITATION SCENARIO (PREVENTED)
=======================================

Without Time Gate:
1. Player logs in as USA
2. Sees large USN convoy heading toward German waters
3. Logs out of USA
4. Immediately logs in as Germany
5. Positions submarine directly in convoy's path
6. Ambushes convoy with perfect intel

With 1-Hour Time Gate:
1. Player logs in as USA
2. Sees large USN convoy heading toward German waters
3. Logs out of USA
4. Must wait 1 hour before accessing Germany
5. Convoy has moved significantly in 1 hour
6. Intel is now stale - ambush much harder

Result: Intel gathering and fleet positioning remain strategic
```

---

## Part 7: Crew XP System

### Separate from RP

Crew XP is **completely separate** from Research Points:

| System | Currency | Purpose | Earned By |
|--------|----------|---------|-----------|
| Research | RP | Unlock ships/turrets/modules | Player actions |
| Crew | XP | Level up crew cards | Crew-specific actions |

### Crew XP Generation

Each crew type earns XP through relevant actions:

| Crew Type | XP-Generating Actions | XP Rate |
|-----------|----------------------|---------|
| **Gunner** | Firing main/secondary battery, hitting targets, ship kills | 1 XP per salvo, +5 per hit, +20 per kill |
| **AA Specialist** | Engaging aircraft, shooting down planes | 1 XP per engagement, +10 per aircraft |
| **Torpedoman** | Launching torpedoes, scoring torpedo hits | 2 XP per launch, +25 per hit |
| **Engineer** | Ship in motion, speed changes, emergency maneuvers | 1 XP per 10 min at sea, +5 per maneuver |
| **Damage Control** | Extinguishing fires, stopping floods, repairs | 5 XP per fire, 3 XP per flood |
| **Electronics** | Radar contacts detected, fire control solutions | 1 XP per target tracked, +3 per solution |
| **Aviation** | Launching aircraft, completing sorties, strikes | 5 XP per launch, +15 per successful strike |
| **Command** | Passive ship-wide | 0.5 XP per 10 min × active crew count |

**Note**: For complete crew mechanics, see [[Crew-Module-Mechanics]] and [[Crew-Progression]].

---

## Part 8: Progression Timing

### Target Time Estimates

Design goal: Players should understand the game before reaching T5.

```
PROGRESSION TIMING TARGETS
==========================

Destroyer Line (Hull Research Only):
├── Bainbridge → T2: ~2-4 hours
├── T2 → T3: ~6-10 hours
├── T3 → T4: ~15-25 hours
├── T4 → T5 (Sims): ~30-50 hours
└── Total to T5: ~50-90 hours (few days of active play)

With Turret + Module Research:
├── Add 50-100% more time
├── T1 → T5 with full loadout: ~100-180 hours
└── Players deeply understand game by T5

Full Tree Completion:
├── All USA destroyers: ~500+ hours
├── All USA ships (all categories): ~2000+ hours
├── Not intended to be "completed"
└── Meaningful long-term progression
```

### Why This Pacing?

```
PROGRESSION PHILOSOPHY
======================

T1-T4 (Learning Phase):
├── No permadeath (safe to learn)
├── Slower progression encourages mastery
├── Players learn all game systems
├── Mistakes are recoverable
└── By T5, players are competent captains

T5 (Gateway):
├── First permadeath tier for destroyers
├── Gateway to carriers and battleships
├── Significant investment required to reach
├── Players who reach T5 understand consequences
└── Meaningful achievement

T6+ (Veteran Phase):
├── Increasing stakes with each tier
├── Faster RP gain (tier multiplier)
├── But higher RP costs balance it
├── Progression slows naturally
└── End-game is about mastery, not unlocks
```

---

## Part 9: Research UI

### Port Research Screen

```
RESEARCH INTERFACE
==================

Research Panel (Port Only):
┌─────────────────────────────────────────────────────────┐
│ RESEARCH                                    USN RP: 45,230│
├─────────────────────────────────────────────────────────┤
│ [Ships] [Turrets] [Modules]  ◄── Category tabs          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     [Truxtun]──>[Smith]                                │
│         │                                               │
│     [CURRENT: Cassin-Class]                            │
│     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░ 70%                       │
│     17,500 / 25,000 RP                                  │
│     [ALLOCATE RP]                                       │
│         │                                               │
│     [???]──>[???]  ◄── Next items (fog of war)         │
│                                                         │
└─────────────────────────────────────────────────────────┘

Allocation Interface:
┌─────────────────────────────────────────────────────────┐
│ ALLOCATE RP TO: Cassin-Class                           │
├─────────────────────────────────────────────────────────┤
│ Current Progress: 17,500 / 25,000 RP                   │
│ Remaining: 7,500 RP needed                              │
│                                                         │
│ Available RP: 45,230                                    │
│ Amount to Allocate: [_______] RP                       │
│                                                         │
│ [ALLOCATE ALL]  [ALLOCATE]  [CANCEL]                   │
└─────────────────────────────────────────────────────────┘
```

### Research Completion

```
RESEARCH COMPLETE NOTIFICATION
==============================

┌─────────────────────────────────────────────────────────┐
│ ★ RESEARCH COMPLETE ★                                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│        [Image: Cassin-Class Destroyer]                 │
│                                                         │
│         CASSIN-CLASS DESTROYER                         │
│              UNLOCKED                                   │
│                                                         │
│   You can now BUILD or PURCHASE this ship!             │
│                                                         │
│   [VIEW IN SHIPYARD]  [VIEW ON MARKET]  [CLOSE]        │
│                                                         │
│   NEXT AVAILABLE RESEARCH:                              │
│   └── Paulding-Class (25,000 RP)                       │
│   └── Aylwin-Class (25,000 RP)                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Part 10: Integration Points

### Related Systems

```
SYSTEM DEPENDENCIES
===================

Research System Depends On:
├── Combat System (generates RP through combat)
├── Extraction System (RP bonuses for extraction)
├── Mission System (mission completion RP)
└── Economy System (credits for building/purchasing)

Research System Feeds Into:
├── Ship Acquisition (unlocks hulls)
├── Module System (unlocks equipment)
├── Tetris Fitting (modules must fit ship slots)
├── Crew System (crew assigned to researched modules)
└── Economy (built/purchased items enter economy)

Parallel Systems:
├── Crew XP (separate from RP, same gameplay generates both)
├── Crew Specialization (levels and unlocks within crew)
└── Nation Reputation (future system)
```

---

## Cross-Reference Documents

**Related Progression:**
- [[Crew-Progression]] - Crew XP earning and leveling
- [[Crew-Specialization]] - Crew classification trees

**Related Ship Customization:**
- [[Module-System]] - Module acquisition and installation
- [[Tetris-Fitting-Mechanics]] - Equipment slot matching
- [[Module-Dependencies]] - Weight-based fitting

**Related Core Gameplay:**
- [[Crew-Module-Mechanics]] - Crew-module efficiency
- [[Inventory-System]] - Storing unlocked items
- [[Extraction-Mechanics]] - Blueprint drops, loot

**Related Economy:**
- [[Economy-Overview]] - Building costs, market pricing
- [[Trading-System]] - Player market for blueprints/items

---

## Summary

| Aspect | Design Decision |
|--------|-----------------|
| **RP Earning** | Combat, extraction, missions + tier multiplier |
| **RP Pool** | Single pool per nation, manual allocation |
| **Tree Structure** | Linear + branching, fog of war visibility |
| **Separate Trees** | Ships, Turrets, Modules (all nation-specific) |
| **Ships** | Hull-only, no modules included |
| **Acquisition** | Build (resources + time) OR Buy (market) |
| **Blueprints** | Rare loot, instant unlock, consumed on use |
| **Nations** | Start with one, others behind 1-hour switch gate |
| **Timing** | ~50-90 hours to T5 (hulls only), longer with modules |

**Design Philosophy**: Players earn progression through gameplay, not time. By the time they reach T5 and face permadeath, they've invested enough to understand the stakes.

---

*Document created: 2025-12-10*
