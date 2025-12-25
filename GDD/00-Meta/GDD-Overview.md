---
tags: [meta, overview, introduction]
status: 📚 MASTER DOCUMENT
last-updated: 2025-12-24
related: [[Development-Status]], [[Game-Vision]], [[Phase-1-Complete]]
---

# 📚 Fathoms Deep Game Design Document - Master Overview
## Complete Game Vision & Development Roadmap

**Document Purpose**: This is the **master entry point** to the Fathoms Deep Game Design Document. New team members, contributors, and stakeholders should read this document first to understand the complete game vision, architecture, and current state.

---

## 🎮 What is Fathoms Deep?

### Elevator Pitch (30 Seconds)
**Fathoms Deep (FD)** is a massive-scale tactical 2D naval MMO supporting 300+ simultaneous players in persistent WWII ocean theaters. The core gameplay revolves around **Extraction-Based Naval Combat** - venture into dangerous waters to acquire valuable loot through PvPvE combat, then successfully return to friendly ports to secure your gains. **High-stakes permadeath**, multi-national diplomacy, and combined arms warfare (surface ships, aircraft, submarines) create a unique tactical experience where every decision matters.

### Core Concept (2 Minutes)
Fathoms Deep combines:
- **Massive Scale**: 300+ players per server in persistent worlds
- **Extraction Gameplay**: Hunt, Fight, Survive, Extract, Build loop inspired by Escape from Tarkov
- **High-Stakes Risk**: Progressive permadeath (T1-4 safe → T5-9 risky → T10 absolute)
- **Multi-National Politics**: 4 playable nations (USA, UK, Germany, Japan) 
- Possible expansion into (USSR, Italy, France, China)
- **Combined Arms**: Surface ships, carrier aircraft, and submarines
- **Player-Driven Economy**: Trading, crafting, market dynamics
- **Historical Authenticity**: WWII ships to present day, weapons, and naval tactics

**Unique Selling Points**:
1. 300+ player capacity (unprecedented for naval combat)
2. True permadeath with tier-based risk progression
3. Extraction-based economy (loot only secured at port)
4. Dynamic diplomacy (nations shift between peace and war)
5. Combined arms naval warfare (surface + air + submarine)

---

## 📋 Project Information

### Current Status (As of 2025-11-17)

**Version**: 0.3.0-alpha (Phase 3 Development)
**Development Stage**: Phase 1 Complete ✅, Phase 2 In Progress 🚧
**Team**: 1 Developer + Claude Code (AI Assistant)
**Target Platforms**: PC (Windows Primary, macOS/Linux Planned)
**Engine**: Unity 6000.0.55f1 (2D/URP)
**Timeline**: 20+ months from current state to full MMO launch

### Phase Status Overview
- **Phase 1: Foundation** ✅ COMPLETED (January 2025)
  - Ship physics, camera, navigation, ocean, networking, auth, chat, UI
  - 100% of goals achieved, playable movement prototype

- **Phase 2: Combat & Economy** 🚧 IN PROGRESS (0-5%)
  - Surface combat, crew management, module system, economy foundation
  - Target: Q2 2025

- **Phase 3: Advanced Features** 📋 PLANNED
  - Carrier ops, submarine warfare, factions, zones, permadeath, full economy
  - Target: Q4 2025

**Key Milestone**: MVP (Phase 7) = 48 weeks | Full MMO (Phase 9) = 78 weeks

---

## 🎯 Core Gameplay Loop

### "Hunt, Fight, Extract, Survive"

#### 1. Outfitting Phase (At Port)
- Load ship with ammunition, fuel, and supplies
- Fit modules (weapons, armor, utilities)
- Assign crew to stations
- Plan expedition (zone, route, objectives)

#### 2. Hunting Phase (Open Ocean)
- Navigate contested waters
- Scan for valuable targets (players, NPCs, resources)
- Assess threat level and cargo value
- Position for ambush or engage directly

#### 3. Combat Phase (PvPvE Engagement)
- Engage enemies using guns, torpedoes, aircraft
- Sink targets to spawn loot crates
- Manage ship damage and crew casualties
- Decide: Continue hunting or extract early?

#### 4. Extraction Phase (Return to Port)
- Navigate back to friendly port with cargo
- Visible cargo = target for ambushes
- Risk vs reward: Stay longer or extract now?
- Only at port is loot **secured**

#### 5. Progression Phase (Port Services)
- Sell loot for credits and resources
- Repair ship damage
- Replace dead crew
- Upgrade ship systems and modules
- Plan next expedition

**The Stakes**: Die before extraction = lose ALL unextracted loot, risk ship/crew permadeath (tier-dependent)

---

## 🌊 Game World & Scale

### Persistent Ocean Theaters
- **Infinite Ocean**: Procedurally generated, chunk-based world
- **300+ Players**: Massive servers with regional distribution (Edgegap)
- **10 Risk Tiers**: Escalating danger from T1 (safe) to T10 (permadeath guaranteed)
- **4 Nations**: USA, UK, Germany, Japan
- **Dynamic Diplomacy**: Peace/War states shift over time
- **Pirates**: Universal threat, hostile to all factions

### Zone System (T1-T10)
**Tier 1-4 (Safe Waters)**:
- 0% ship loss, 0% crew casualties
- Tutorial and starting zones
- Low rewards, easy enemies
- PvP restricted or low-penalty
- Inventory loss only

**Tier 5 (The Threshold)**:
- 0% ship loss, 30% crew casualties
- Last fully safe tier for ships
- Moderate rewards, balanced risk

**Tier 6-9 (Death Waters)**:
- 30-60% ship loss, 40-60% crew casualties
- High-stakes combat
- Exceptional rewards
- Intense PvPvE

**Tier 10 (The Abyss)**:
- 100% ship & crew permadeath (GUARANTEED)
- Unmatched rewards

---

## ⚓ Ship Classes & Combat

### 6 Primary Ship Classes

**Destroyer (DD)**: Fast, agile, low armor
- **Role**: Scout, torpedo attacks, escort
- **Strengths**: Speed, maneuverability, stealth
- **Weaknesses**: Fragile, low firepower

**Light Cruiser (CL)**: Balanced, versatile
- **Role**: Multi-purpose, anti-air, screening
- **Strengths**: Balanced stats, AA capability
- **Weaknesses**: Jack-of-all-trades

**Heavy Cruiser (CA)**: Powerful guns, moderate armor
- **Role**: Heavy hitting, cruiser combat
- **Strengths**: Firepower, armor
- **Weaknesses**: Slower than DDs/CLs

**Battleship (BB)**: Massive guns, heavy armor, slow
- **Role**: Tank, long-range bombardment
- **Strengths**: Devastating firepower, survivability
- **Weaknesses**: Slow, expensive, large target

**Aircraft Carrier (CV)**: Aircraft operations, vulnerable
- **Role**: Air superiority, reconnaissance, air strikes
- **Strengths**: Range, versatility, spotting
- **Weaknesses**: Weak in direct combat, requires escort

**Submarine (SS)**: Stealth hunter, depth warfare
- **Role**: Ambush attacks, convoy raiding, stealth reconnaissance
- **Strengths**: Invisibility when submerged, devastating torpedo salvos, surprise advantage
- **Weaknesses**: Fragile when surfaced, slow submerged speed, limited underwater vision, vulnerable to depth charges and ASW

### Combat Domains (Phase 3)
1. **Surface Combat**: Ship-to-ship gunfire and torpedoes
2. **Air Combat**: Carrier aircraft vs ships and aircraft
3. **Submarine Warfare**: Underwater stealth, ASW, depth mechanics

---

## 👥 Crew Management System

### Navy Field-Inspired Crew Cards
**Philosophy**: Each crew card represents a **group of sailors** led by a named officer, not just a single individual. Like Navy Field, these cards level up, gain stats, and can lose sailors in combat.

**Crew Card Structure**:
- **Portrait**: Officer character avatar
- **Name**: Procedurally generated or historical officer name
- **Rank**: Ensign → Lieutenant → Captain → Admiral
- **Station**: Helm, Gunnery, Engineering, Repair, Officer
- **Level**: 1-200 progression
- **Sailors Left**: Current number of sailors alive on this card (e.g., 45/50)
- **Stats**: Accuracy, Reload Speed, Morale, Experience

**Crew Stats (Core Performance)**:
- **Accuracy** (50-100%): Hit chance modifier for gunnery/torpedoes
- **Reload Speed** (50-150%): Fire rate modifier for weapons
- **Morale** (0-100%): Overall crew performance multiplier
- **Experience** (0-100%): Increases with combat, affects stat growth

**Sailor Casualties (Replaceable)**:
- Sailors can die in combat, reducing the card's effectiveness
- Lost sailors reduce stats proportionally (e.g., 30/50 sailors = 60% effectiveness)
- Replace lost sailors at ports (restores card to full strength)
- Sailor casualties are NOT permadeath - just damage to the card

**Crew Card Permadeath (Tier-Based Risk)**:
- Entire crew card can be **PERMANENTLY LOST** in battle (officer, levels, all progress)
- Lost cards are gone forever - must recruit and train new cards from Level 1
- T1-T5: 0% chance (completely safe from card permadeath)
- T6: 10% chance to lose crew cards per battle
- T7: 20% chance to lose crew cards
- T8: 40% chance to lose crew cards
- T9: 60% chance to lose crew cards
- T10: 100% crew card loss (all cards guaranteed destroyed)

**Progression**:
- XP earned from combat, missions, sailing time
- Level 1-200 with stat increases per level
- Train crew at ports to improve base stats
- Higher level cards are more valuable (harder to lose high-level veterans)

---

## 📦 Module System (Tetris-Style Ship Fitting)

### "EVE Online meets Tetris"
Visual, spatial ship customization

**Module Categories**:
1. **Weapons**: Main batteries, secondaries, torpedoes, AA guns
2. **Armor**: Belt, deck, turret, reactive armor
3. **Utilities**: Fire control, radar, engines, fuel tanks, repair systems

**Fitting Mechanics**:
- **Ship Grid**: Tetris-style (e.g., 10x20 cells per ship)
- **Drag-and-Drop**: Visual placement with rotation (R key)
- **Weight Limit**: Can't exceed ship tonnage
- **Slot Limits**: Only Weight limits per slot / Slot needs to be filled: 1x1 slot needs 1x1 module, 2x2 slot needs 2x2 module
- **Tech Tier**: Can equip higher-tier modules on lower-tier ships, if they fit

**UI/UX**:
- Top-down ship layout view
- Color-coded modules (weapon, armor, utility)
- Hover for stats and descriptions
- Validation on placement (red = invalid)

---

## 💰 Economy System

### Extraction-Based Economy
**Philosophy**: "Risk vs Reward" - loot only secured at port

### Currency & Resources
**Primary Currency**: Credits (₡)
- Earned: Combat, missions, trading, loot
- Spent: Ships, modules, crew, repairs, ammo

**Secondary Resources** (Phase 3):

**Raw Materials (Basic Crafting)**:
- **Steel**: Ship hulls, armor plating, structural repairs
- **Iron Ore**: Raw material for steel production
- **Aluminum**: Aircraft components, lightweight structures
- **Copper**: Wiring, electronics, communication systems
- **Coal**: Fuel alternative, industrial processes

**Strategic Materials (Advanced Construction)**:
- **Oil**: Fuel for ships, base for many products
- **Chromium**: High-grade armor, special alloys
- **Nickel**: Armor hardening, corrosion resistance
- **Tungsten**: Armor-piercing rounds, hardened components
- **Titanium**: Advanced armor, high-performance modules
- **Rare Earths**: Electronics, advanced sensors, radar components

**Industrial Products (Refined Materials)**:
- **Rubber**: Seals, hoses, shock absorption systems
- **Electronics**: Fire control systems, radar, communication gear
- **Chemicals**: Ammunition propellant, damage control compounds
- **Textiles**: Crew uniforms, tarpaulins, damage control materials
- **Plastics**: Insulation, modern components, storage containers
- **Glass**: Optics, instruments, bridge windows

**Fuel & Energy (Consumables)**:
- **Diesel Fuel**: Modern ship propulsion
- **Aviation Fuel**: Carrier aircraft operations
- **Gunpowder**: Ammunition production, older weapons

**Combat Supplies (High Turnover)**:
- **Ammunition**: Shells for main guns (various calibers)
- **Torpedoes**: Anti-ship weapons (various types)
- **Depth Charges**: Anti-submarine warfare
- **Aircraft Ordnance**: Bombs, rockets for carrier planes
- **Flares**: Illumination, signaling, countermeasures

**Provisions & Crew Supplies (Maintenance)**:
- **Food Rations**: Crew morale and operations
- **Fresh Water**: Essential for long voyages
- **Medical Supplies**: Treat wounded crew, prevent casualties
- **Repair Tools**: Emergency repairs at sea
- **Spare Parts**: Generic components for field repairs

**Luxury & Trade Goods (High Value/Low Weight)**:
- **Tobacco**: Crew morale, trade commodity
- **Alcohol**: Crew morale, high-value trade
- **Coffee**: Crew performance, trade commodity
- **Spices**: Valuable trade goods
- **Sugar**: Provisions, trade commodity
- **Silk**: Luxury trade item

**Intelligence & Strategic Items (Special)**:
- **Naval Charts**: Navigation data, strategic info
- **Intelligence Documents**: Enemy positions, fleet movements
- **Encryption Equipment**: Secure communications
- **Prototype Components**: Experimental technology
- **Salvage Rights**: Legal claim to wrecks/loot

**Resource Uses**:
- Crafting ship modules and weapons
- Repairing battle damage
- Upgrading ship capabilities
- Trading for profit between ports
- Mission/contract requirements
- Guild/faction contributions

### Trading System
**Port Shops**:
- **Shipyard**: Buy/sell ships
- **Armory**: Weapons and modules
- **Crew Office**: Hire and train crew
- **Repair Dock**: Fix damaged hulls and modules
- **Supply Depot**: Ammo, fuel, consumables

**Market Dynamics** (Phase 3):
- Supply and demand pricing
- Regional price differences
- Trading routes (buy low, sell high)
- Player-driven markets

### Loot System
**Loot Mechanics**:
- Sunk ships drop loot crates
- Loot contains: Modules, credits, resources
- Must pick up to claim, loot crates are visible and interactable to all. 
- Only secured when reaching port

**Loot Rarity**:
- **Common** (70%): Basic loot
- **Uncommon** (20%): Mid-tier loot
- **Rare** (8%): High-tier loot
- **Legendary** (2%): Unique items

**Extraction Risk**:
- Visible cargo = target for ambushes
- Die = lose ALL unextracted loot
- High-stakes decision making

---

## 🏴 Faction & Diplomacy

### 4 Playable Nations (Launch)

**United States** 🇺🇸: Powerful carriers, advanced radar
**United Kingdom** 🇬🇧: Balanced fleet, excellent cruisers
**Germany** 🇩🇪: Powerful battleships, U-boats
**Japan** 🇯🇵: Torpedo warfare, fast cruisers

### Potential Future Nations (Post-Launch)
**Soviet Union** 🇷🇺: Tanky cruisers, artillery focus
**Italy** 🇮🇹: Fast ships, good torpedoes
**France** 🇫🇷: Unique designs, strong cruisers
**China** 🇨🇳: Mixed fleet (captured ships)

### Diplomatic States
1. **Peace**: No hostilities, trade allowed
2. **Tensions**: Increased patrols, trade restrictions
3. **Proxy War**: Indirect conflict via missions
4. **War**: Open hostilities
5. **Alliance**: Cooperative, shared resources

### Reputation System
**Scale**: -1000 to +1000 per nation

**Effects**:
- **Friendly** (+500+): Discounts, mission access
- **Neutral** (0): Standard prices
- **Hostile** (-500+): Port denial, higher prices
- **Enemy** (-1000): Attacked on sight

**Gaining/Losing Reputation**:
- Complete missions, sink enemies = gain
- Attack allies, piracy = lose
- Dynamic and consequential

---

## ⚠️ Permadeath System

### Philosophy: "Stakes Matter"
True high-stakes gameplay with progressive risk across **three separate loss mechanics**

### Ship Permadeath (Tier-Based)
- **T1-T5**: 0% ship loss (ships always recover - completely safe)
- **T6**: 10% ship loss chance (first permadeath tier)
- **T7**: 20% ship loss chance
- **T8**: 40% ship loss chance
- **T9**: 60% ship loss chance
- **T10**: 100% ship loss (GUARANTEED PERMADEATH)

### Crew Card Permadeath (Tier-Based, Independent from Ship)
Each crew card (officer + sailors group) rolls separately for permadeath:
- **T1-T5**: 0% crew card loss (completely safe for training)
- **T6**: 10% crew card loss per card (first permadeath tier)
- **T7**: 20% crew card loss per card
- **T8**: 40% crew card loss per card
- **T9**: 60% crew card loss per card
- **T10**: 100% crew card loss (ALL crew cards destroyed)

**Lost crew cards are permanent** - must recruit new Level 1 cards and retrain from scratch

### Sailor Casualties (Damage-Based, Always Active)
Individual sailors die from combat damage **separate from crew card permadeath**:
- Based on damage severity, not tier
- Occurs on **all crew cards** (even surviving cards)
- Reduces crew card effectiveness (e.g., 30/50 sailors = 60% performance)
- **Replaceable at ports for credits** - NOT permanent loss
- Economic pressure without devastating permanent consequences

### Cargo Loss (Always)
- **Unextracted Loot**: ALWAYS lost on death
- **Secured Loot**: Safe in port inventory

### Player Experience
- Clear warnings when undocking with T6+ ships
- Confirmation dialogs when undocking T6+ ships
- Death screens show breakdown of all three loss types
- Memorial system for permanently lost ships and crew cards
- Insurance system to reduce permadeath risk

**Design Goal**: Three-tiered loss system creates meaningful tension while allowing recovery options

---

## 🛠️ Technology Stack

### Core Engine
- **Unity 6000.0.55f1**: Latest features and performance
- **URP 2D Renderer**: Optimized 2D/3D hybrid rendering
- **Unity.Mathematics**: High-performance calculations
- **Burst Compiler**: Native code for physics
- **Job System**: Multi-threaded operations

### Networking
- **Mirror Networking**: 300+ player support
- **KCP Transport**: Reliable UDP for real-time combat
- **Edgegap**: Cloud deployment, low latency
- **Client-Side Prediction**: Smooth multiplayer
- **Server Authority**: Anti-cheat protection

### UI & Input
- **Modern UI Pack (MUIP)**: Professional UI components
- **TextMeshPro**: High-quality text rendering
- **Unity Input System**: Rebindable, multi-device

### Backend
- **JWT Authentication**: Secure login
- **PostgreSQL**: Player data (assumed)
- **Node.js + Express**: Backend API (assumed)

### Development Tools
- **Git + GitHub**: Version control
- **Claude Code**: AI development assistant
- **Visual Studio 2022**: Primary IDE

**Full Details**: See [[Tech-Stack]]

---

## 🎯 Performance Targets

### Client Performance
- **Frame Rate**: 60 FPS minimum (1920x1080)
- **Large Battles**: 45-60 FPS with 100+ ships
- **Memory**: < 6 GB RAM normal, < 8 GB peak
- **Load Times**: < 15 seconds scene transitions

### Server Performance
- **Capacity**: 300+ concurrent players
- **CPU Usage**: < 70% average, < 90% peak
- **Memory**: < 8 GB RAM for 300 players
- **Tick Rate**: 60 Hz physics, 20-30 Hz network

### Network Performance
- **Latency**: < 50ms for 80% of players (Edgegap)
- **Bandwidth**: 50-100 KB/s per client (average)
- **Packet Loss**: < 1%
- **Update Rate**: 20-30 Hz critical systems

**Full Details**: See [[Performance-Targets]]

---

## 🗓️ Development Roadmap

### Phase 1: Foundation ✅ COMPLETED (January 2025)
**Duration**: 8-10 weeks
**Status**: 100% Complete

**Delivered**:
- ✅ Ship physics with 8-speed throttle (5 classes)
- ✅ Camera system (follow, zoom, look-ahead)
- ✅ Multi-waypoint navigation
- ✅ Infinite ocean environment with biomes
- ✅ Multiplayer networking (Mirror + Edgegap)
- ✅ JWT authentication system
- ✅ Chat system (3 channels)
- ✅ Complete UI framework and menus

**Performance**: 120+ FPS in builds, excellent foundation

**Full Retrospective**: See [[Phase-1-Complete]]

---

### Phase 2: Combat & Economy 🚧 IN PROGRESS (0-5%)
**Duration**: 8-12 weeks
**Target**: Q2 2025

**Goals**:
- 🔫 Surface combat system (guns, torpedoes, damage)
- 👥 Crew management (Navy Field-inspired cards)
- 📦 Module system (Tetris-style fitting)
- 💰 Economy foundation (currency, trading, loot)

**Success Criteria**:
- Two players can fight and sink each other
- Crew measurably affects performance
- Module fitting functional
- Economy loop operational

**Current Status**: Design phase, no implementation yet

**Full Work Plan**: See [[Phase-2-InProgress]]

---

### Phase 3: Advanced Features 📋 PLANNED
**Duration**: 16-24 weeks
**Target**: Q4 2025

**Goals**:
- 🚀 Carrier operations (air combat)
- 🔱 Submarine warfare (depth mechanics)
- 🌍 Zone system (T1-T10 risk tiers)
- 🏴 Faction system (4 nations at launch, diplomacy)
- ⚠️ Permadeath implementation
- 💰 Full player-driven economy
- 🌦️ Weather and day/night cycle
- 🎯 Mission and objective system

**Success Criteria**:
- 300 players stable on single server
- All combat domains functional
- Permadeath working correctly
- Full MMO experience complete

**Full Roadmap**: See [[Phase-3-Plan]]

---

### Future Phases (Phase 4-9)
**Timeline**: 12-18 additional months

**Phase 4**: AI & NPC Systems
**Phase 5**: Content Expansion (ships, maps)
**Phase 6**: Social Features (guilds, friends)
**Phase 7**: MVP Release (single-player complete)
**Phase 8**: MMO Infrastructure (distributed servers)
**Phase 9**: Full Launch (300+ player capacity)

**Total Timeline**: 20+ months from Phase 1 to full MMO launch

---

## 📊 Current Capabilities (What You Can Play Now)

### Phase 1 Complete - Playable Now ✅

**Single Player**:
- ✅ Launch game and log in
- ✅ Control ship with realistic naval physics
- ✅ Navigate using waypoint autopilot
- ✅ Explore infinite ocean
- ✅ Camera follows ship smoothly
- ✅ Debug UI shows telemetry

**Multiplayer**:
- ✅ Join Edgegap or local server
- ✅ See other players' ships
- ✅ Chat with other players
- ✅ All single-player features in multiplayer

### Not Yet Available
- ❌ Combat (weapons not implemented)
- ❌ Crew management (Phase 2)
- ❌ Economy/trading (Phase 2-3)
- ❌ Ship customization (Phase 2)
- ❌ Factions/reputation (Phase 3)
- ❌ Permadeath (Phase 3)
- ❌ Carrier/submarine gameplay (Phase 3)

**Expected**: Phase 1 was a movement prototype. Combat and economy come in Phase 2-3.

---

## 🎨 Art & Audio Status

### Current Assets (Phase 1)
- ✅ Ship sprites (5 classes, placeholder quality)
- ✅ Ocean tiles (biome system)
- ✅ UI elements (Modern UI Pack)
- ⚠️ Debug visualizations only

### Planned Assets (Phase 2-3)
- 📋 Combat effects (explosions, fire, smoke)
- 📋 Weapon projectiles and impacts
- 📋 Damage visualization
- 📋 Aircraft sprites
- 📋 Submarine assets
- 📋 Weather effects (rain, fog, storms)

### Audio (Phase 3)
- 📋 FMOD integration
- 📋 3D spatial audio
- 📋 Combat sounds (guns, explosions)
- 📋 Ambient ocean audio
- 📋 Dynamic music system
- 📋 Voice chat (VoIP)

**Current State**: Phase 1 focused on systems, not art. Visual polish comes in Phase 2-3.

---

## 🧪 Testing & Quality Assurance

### Phase 1 Testing ✅
- ✅ Manual testing complete
- ✅ All systems functional
- ✅ 2-5 player multiplayer tested
- ✅ Performance benchmarks met (120+ FPS)

### Phase 2 Testing (Planned)
- 📋 Unit tests for combat calculations
- 📋 Integration tests (multiplayer combat)
- 📋 10-20 player stress tests
- 📋 Balance testing (TTK, economy)

### Phase 3 Testing (Planned)
- 📋 100 player alpha testing
- 📋 300 player beta testing
- 📋 Performance optimization
- 📋 Community feedback integration

**Philosophy**: Test early, test often, iterate based on data

---

## 🌐 Community & Social

### Development Transparency
- **Living GDD**: Updated as project evolves
- **Open Development**: Share progress regularly
- **Community Input**: Feedback shapes design
- **AI-Assisted**: Claude Code accelerates development

### Planned Community Features (Phase 6+)
- Player guilds/fleets
- Friends and party system
- Leaderboards and rankings
- Battle replays and sharing
- Forum integration
- Discord community

### Social Philosophy
**"Build with the community, not just for them"**

---

## 💡 Design Philosophy

### Core Principles

#### 1. Stakes Matter
**"Risk creates meaning"**
- Permadeath makes victory meaningful
- Extraction mechanics create tension
- Every decision has consequences

#### 2. Scale Matters
**"300+ players creates emergent gameplay"**
- Massive battles impossible in small games
- Player-driven politics and economy
- Living, breathing world

#### 3. Skill Matters
**"Tactics over twitch reflexes"**
- Positioning, timing, teamwork
- Knowledge of ship capabilities
- Strategic decision making

#### 4. History Matters
**"WWII authenticity with gameplay focus"**
- Historical ships and nations
- Realistic naval tactics
- Educational but fun

#### 5. Accessibility Matters
**"Inclusive by design"**
- WCAG 2.1 AA compliance
- Rebindable controls
- Multiple input methods
- Clear UI and feedback

---

## 🚧 Development Challenges

### Technical Challenges
1. **300 Player Networking**: Unprecedented scale for naval combat
2. **Combat Synchronization**: Real-time projectile physics in multiplayer
3. **Balance Complexity**: 3 domains, 4 nations (8 potential), 10 tiers
4. **Performance Optimization**: 60 FPS with 100+ ships visible

### Design Challenges
1. **Permadeath Reception**: Will players accept harsh mechanics?
2. **Economy Balance**: Extraction economy must feel fair
3. **New Player Experience**: High skill ceiling, need good onboarding
4. **Content Depth**: Solo dev creating MMO-scale content

### Solo Developer Challenges
1. **Scope Management**: Ambition vs reality
2. **Time Investment**: 20+ month development
3. **Art Assets**: Limited art resources
4. **Testing**: Multiplayer requires community

**Mitigation**: AI assistance (Claude Code), phased development, community involvement

---

## 🔗 Documentation Structure

### Where to Find Information

#### Meta Documents (00-Meta/)
- **[[GDD-Overview]]** (You are here) - Master overview
- [[Development-Status]] - Current progress
- [[Phase-1-Complete]] - Phase 1 retrospective
- [[Phase-2-InProgress]] - Current work plan
- [[Phase-3-Plan]] - Future roadmap

#### Core Concepts (01-Core-Concepts/)
- [[Game-Vision]] - Overall vision and pillars
- [[Target-Audience]] - Player demographics
- [[Extraction-Mechanics]] - Core gameplay loop
- [[Permadeath-System]] - High-stakes design

#### Core Gameplay (02-Core-Gameplay/)
- [[Ship-Physics]] - Naval movement
- [[Camera-System]] - Camera controls
- [[Crew-Management]] - Crew mechanics
- [[Crew-Progression]] - XP and leveling
- [[Crew-Permadeath]] - Crew death mechanics

#### Combat Systems (03-Combat-Systems/)
- [[Combat-Overview]] - Combat design
- [[Surface-Combat]] - Ship-to-ship combat
- [[Carrier-Operations]] - Air combat
- [[Submarine-Warfare]] - Underwater combat
- [[Damage-Model]] - Damage calculations

#### Ships (04-Ships/)
- [[Module-System]] - Tetris inventory
- [[Armor-Configuration]] - Armor systems
- Ship research data: USA (247), Germany (223), GB (188), Japan (160)

#### Aircraft (05-Aircraft/)
- Aircraft research data: USA (178), GB (92), Japan (88), Germany (75)
- [[Research-Trees]] - Tech progression

#### Weapons (06-Weapons/)
- [[Naval-Guns]] - 372 guns, 2,857 turrets
- [[Torpedoes]] - 234 torpedo types
- [[Missiles]] - 202 missile types
- [[Aircraft-Weapons]] - Air-launched ordnance

#### Economy (07-Economy/)
- [[Economy-Overview]] - Economy design
- [[Trading-System]] - Trading mechanics
- [[Resources]] - 257 resource types

#### UI Systems (08-UI-Systems/)
- [[UI-Overview]] - UI architecture
- [[Menu-System]] - Menu implementation

#### Multiplayer (09-Multiplayer/)
- [[Network-Architecture]] - Mirror setup
- [[Authentication]] - JWT login
- [[Chat-System]] - Chat implementation

#### World Design (10-World-Design/)
- [[Ocean-Environment]] - Infinite ocean
- [[Zone-System]] - T1-T10 tiers
- [[Weather-System]] - Weather effects
- [[Map-Layout]] - World structure

#### Faction System (11-Factions/)
- [[Nation-Overview]] - 4 nations (launch)
- [[Reputation-System]] - Standing mechanics
- [[Diplomacy-States]] - Peace/War states

#### Progression (12-Progression/)
- [[Player-Progression]] - XP and leveling
- [[Ship-Unlocks]] - Ship acquisition
- [[Research-Trees]] - Tech progression

#### Technical (13-Technical/)
- [[Tech-Stack]] - All technologies
- [[Performance-Targets]] - Optimization goals

#### Art & Audio (14-Art-Audio/)
- [[Visual-Design]] - Art direction
- [[Audio-Design]] - Sound design
- [[Asset-Pipeline]] - Asset workflow

---

## 🎯 Success Criteria (Overall Project)

### MVP Success (Phase 7)
- ✅ Complete single-player experience
- ✅ All core systems functional
- ✅ 10-20 player multiplayer stable
- ✅ Polished and bug-free
- ✅ Positive community feedback

### Full MMO Success (Phase 9)
- ✅ 300+ players per server stable
- ✅ All combat domains (surface, air, sub)
- ✅ Permadeath working correctly
- ✅ Full economy operational
- ✅ Faction system meaningful
- ✅ 60 FPS with 100+ ships visible
- ✅ < 50ms latency for 80% of players
- ✅ Active, engaged player community

### Commercial Success (Post-Launch)
- ✅ Positive Steam reviews (80%+)
- ✅ Sustainable player base (1000+ CCU)
- ✅ Active community (Discord, forums)
- ✅ Regular content updates
- ✅ Monetization sustainable (if applicable)

---

## 📝 Final Thoughts

### What Makes Fathoms Deep Unique?
1. **Scale**: 300+ player naval battles are unprecedented
2. **Risk**: True permadeath creates meaningful stakes
3. **Extraction**: Hunt, fight, extract loop is unique to naval genre
4. **Combined Arms**: Surface + air + submarine integration
5. **Diplomacy**: Multi-national politics add depth
6. **Historical**: WWII authenticity with tactical gameplay

### Why This Project Matters
Fathoms Deep fills a gap in the market:
- **World of Warships**: Great game, but no extraction or permadeath
- **Navy Field**: Inspiration, but outdated
- **EVE Online**: Similar depth, but in space
- **Escape from Tarkov**: Extraction mechanics, but FPS not naval

**Fathoms Deep combines the best elements into a unique naval MMO.**

### The Vision
**"A living WWII naval world where every battle matters, every decision has consequences, and 300+ players create emergent stories of courage, betrayal, and tactical brilliance."**

### Current Reality Check
- ✅ Phase 1 proves concept is viable
- ✅ Foundation is solid and performant
- 🚧 Phase 2 will make it a game
- 📋 Phase 3 will make it an MMO
- ⏱️ 20+ months of work remain

**It's ambitious. It's achievable. Let's build it.**

---

## 🔗 Quick Links

### Essential Documents
- [[Development-Status]] - Current project state
- [[Phase-2-InProgress]] - What we're building now
- [[Tech-Stack]] - Technologies used
- [[Game-Vision]] - Design pillars

### For New Contributors
1. Read this document (GDD-Overview)
2. Read [[Development-Status]]
3. Check [[Phase-2-InProgress]] for current work
4. Review [[Tech-Stack]] for technical setup
5. Join Discord (if available)

### For Designers
- [[Game-Vision]] - Core design philosophy
- [[Extraction-Mechanics]] - Core loop
- [[Permadeath-System]] - High-stakes design
- [[Combat-Overview]] - Combat systems

### For Programmers
- [[Tech-Stack]] - Full technology list
- [[Network-Architecture]] - Multiplayer setup
- [[Performance-Targets]] - Optimization goals
- Script references in each design doc

### For Artists/Audio
- (Asset requirements TBD in Phase 2)
- Reference: WWII naval photography
- Style: Realistic with gameplay clarity

---

## 📞 Contact & Contribution

### Current Team
- **Lead Developer**: Solo developer + Claude Code (AI)
- **Contributors**: Open to collaboration (Phase 2+)

### How to Contribute (Future)
- **Code**: Submit PRs for review
- **Design**: Propose features in discussions
- **Testing**: Join alpha/beta testing
- **Community**: Build community, create content

### Project Links (TBD)
- GitHub: (Repository link)
- Discord: (Community server)
- Website: (Project page)
- Steam: (Store page, if applicable)

---

## 📊 Document Changelog

### 2025-11-17
- ✅ Created master GDD overview document
- ✅ Consolidated all major game systems
- ✅ Documented current status and roadmap
- ✅ Established documentation structure

### Future Updates
- Phase 2 kickoff updates
- Combat system implementation notes
- Community feedback integration
- Beta testing results

---

**Document Status**: 📚 MASTER DOCUMENT (Living Document)
**Last Updated**: 2025-11-17
**Next Review**: Phase 2 Completion
**Maintained By**: Lead Developer + Community

---

**Welcome to Fathoms Deep. Let's build something extraordinary together.**

⚓ *"In the end, it's not about the ships. It's about the sailors, the battles, and the stories we create."*
