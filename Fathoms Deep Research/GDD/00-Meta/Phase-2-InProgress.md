---
tags: [meta, roadmap, current-work]
status: 🚧 IN PROGRESS
phase: Phase 2
start-date: 2025-01
target-completion: 2025-Q2
last-updated: 2025-12-10
related: [[Development-Status]], [[Phase-1-Complete]], [[Phase-3-Plan]]
---

# 🚧 Phase 2: Combat & Economy Foundation
## Current Development Phase - IN PROGRESS

**Phase Duration**: January 2025 - Q2 2025 (Estimated 8-12 weeks)
**Status**: 0-5% Complete 🚧
**Goal**: Implement core combat mechanics, crew management, and economy foundation

---

## 📊 Phase 2 Overview

### Mission Statement
**"Make ships fight, make crews matter, make economy work"**

Phase 2 transforms Fathoms Deep from a movement prototype into a functional naval combat game. This phase delivers the **core gameplay loop**: Hunt, Fight, Extract, Survive.

### Why Phase 2 is Critical
Phase 1 built the foundation. Phase 2 builds the **game**. Without combat, crew, and economy, Fathoms Deep is just ships sailing in circles. This phase makes it **fun**.

---

## 🎯 Phase 2 Goals

### Primary Objectives (Must Complete)
1. 🔫 **Surface Combat System** - Ships can fight and sink each other
2. 👥 **Crew Management** - Navy Field-inspired crew cards
3. 📦 **Module System** - Tetris-style ship fitting
4. 💰 **Economy Foundation** - Currency, trading, loot basics

### Secondary Objectives (Nice to Have)
5. 🎯 **AI Enemies** - Basic NPC ships for PvE
6. 📊 **Damage Visualization** - Visual feedback for damage
7. 🏆 **Basic Progression** - Ship unlocks and crew XP
8. 🔊 **Combat Audio** - Weapon sounds and explosions (basic)

### Success Criteria
- ✅ Two players can fight and sink each other
- ✅ Crew affects ship performance measurably
- ✅ Players can buy/sell modules and ships
- ✅ Combat feels satisfying and tactical
- ✅ Economy loop functional (earn → spend → upgrade)

---

## 🗓️ Phase 2 Timeline

### Estimated Duration: 8-12 Weeks
**Start**: January 2025
**Target Completion**: Q2 2025

### Week-by-Week Breakdown

#### Weeks 1-2: Combat System Design & Prototyping
**Status**: 📋 NOT STARTED

**Tasks**:
- [ ] Finalize ballistics model (shell flight, gravity, drag)
- [ ] Design damage calculation system
- [ ] Prototype basic gun turret
- [ ] Create weapon firing UI/controls
- [ ] Test projectile pooling system

**Deliverables**:
- Combat system design document
- Basic projectile test scene
- Weapon firing prototype

**Blockers**:
- Need to finalize hit detection approach (raycast vs projectile)
- Decide on damage model complexity (simple vs realistic)

---

#### Weeks 3-4: Damage Model & Ship Combat
**Status**: 📋 NOT STARTED

**Tasks**:
- [ ] Implement ship health system
- [ ] Create module damage mechanics
- [ ] Build damage visualization (hit effects, fire, smoke)
- [ ] Implement ship sinking mechanics
- [ ] Network synchronization for combat

**Deliverables**:
- Ships can take damage
- Visual feedback for damage states
- Sinking animation/sequence
- Combat synced in multiplayer

**Blockers**:
- Depends on Week 1-2 combat prototype
- Need art assets for damage effects

---

#### Weeks 5-6: Crew Management System
**Status**: 📋 NOT STARTED

**Tasks**:
- [ ] Design crew database schema
- [ ] Create crew card UI (Navy Field style)
- [ ] Implement crew stats system (accuracy, reload, morale)
- [ ] Build crew assignment to ship stations
- [ ] Create crew progression (XP, leveling)
- [ ] Implement crew permadeath mechanics

**Deliverables**:
- Crew management UI functional
- Crew affects ship performance
- Crew can level up
- Crew can die permanently

**Blockers**:
- Need backend database schema
- Complex UI work required
- Balancing crew impact on gameplay

---

#### Weeks 7-8: Module System & Ship Fitting
**Status**: 📋 NOT STARTED

**Tasks**:
- [ ] Design Tetris-style inventory UI
- [ ] Implement drag-and-drop module placement
- [ ] Create module database (guns, armor, utilities)
- [ ] Build ship fitting validation (weight, slots)
- [ ] Add module stats and effects
- [ ] Implement module damage in combat

**Deliverables**:
- Tetris inventory UI functional
- Players can fit modules to ships
- Modules affect ship performance
- Module configurations saved

**Blockers**:
- Complex UI/UX design required
- Need extensive module database
- Balancing module stats

---

#### Weeks 9-10: Economy Foundation
**Status**: 📋 NOT STARTED

**Tasks**:
- [ ] Implement currency system (credits, materials)
- [ ] Create basic shop UI
- [ ] Build buy/sell functionality
- [ ] Implement loot drop system
- [ ] Add loot pickup mechanics
- [ ] Create basic market prices

**Deliverables**:
- Players can earn currency from combat
- Players can buy/sell ships and modules
- Loot drops from sunk ships
- Basic trading functional

**Blockers**:
- Need economy balancing (prices, earnings)
- Backend API for transactions
- Inventory system integration

---

#### Weeks 11-12: Integration, Polish & Testing
**Status**: 📋 NOT STARTED

**Tasks**:
- [ ] Integrate all Phase 2 systems
- [ ] Balance combat (damage, TTK, ranges)
- [ ] Polish UI and feedback
- [ ] Multiplayer stress testing (10-20 players)
- [ ] Bug fixing and optimization
- [ ] Create Phase 2 demo build

**Deliverables**:
- All systems integrated and working
- Combat balanced and fun
- Playable Phase 2 demo
- Bug-free (major issues resolved)

**Blockers**:
- Depends on all prior weeks
- Need community testers
- Performance optimization required

---

## 🔫 System Breakdown: Surface Combat

### Combat System Requirements
**Status**: 📋 PLANNED

### Weapon Types (Phase 2)
1. **Naval Guns** (Primary Focus)
   - Main battery (large caliber)
   - Secondary battery (medium caliber)
   - AA guns (anti-aircraft - basic)
   - Ballistics simulation (shell flight)

2. **Torpedoes** (Stretch Goal)
   - Surface-launched torpedoes
   - Straight-line travel
   - High damage, slow reload
   - Limited range

3. **Depth Charges** (Phase 3)
   - Anti-submarine warfare
   - Deferred to submarine implementation

### Weapon Mechanics
**Ballistics Model**:
- Projectile flight simulation (not raycast)
- Gravity and drag calculations
- Travel time based on range
- Shell velocity and arc

**Firing Mechanics**:
- Manual aiming (mouse control)
- Turret rotation limits
- Reload times per weapon
- Ammo tracking (finite ammunition)

**Accuracy System**:
- Base accuracy per gun
- Crew skill modifiers
- Range penalties
- Movement penalties (firing while turning)

**Damage Calculation**:
- Penetration vs armor thickness
- Critical hits (random chance)
- Module-specific damage
- Overpenetration mechanics

### Combat UI
- **Crosshair**: Aiming reticle
- **Range Finder**: Distance to target
- **Fire Control**: Weapon selection
- **Ammo Counter**: Shells remaining
- **Reload Timer**: Visual feedback

---

## 👥 System Breakdown: Crew Management

### Crew System Architecture
**Status**: 📋 PLANNED

### Crew Card System (Navy Field Inspired)
**Design Philosophy**: Crew are **individuals**, not generic stats.

**Crew Card Structure**:
- **Portrait**: Character avatar
- **Name**: Procedurally generated or historical
- **Rank**: Ensign, Lieutenant, Captain, Admiral
- **Station**: Helm, Gunnery, Engineering, Repair
- **Stats**: Accuracy, Reload Speed, Morale, Experience
- **Level**: 1-50 progression
- **Traits**: Unique bonuses (e.g., "Sharpshooter", "Engineer")

### Crew Stats & Effects
**Station Types**:
1. **Helmsman**: Turn rate, acceleration
2. **Gunner**: Accuracy, reload speed
3. **Engineer**: Speed, fuel efficiency
4. **Repair**: Damage control, fire suppression
5. **Officer**: Overall morale, bonus effects

**Stat Impact**:
- **Accuracy** (50-100%): Hit chance modifier
- **Reload Speed** (50-150%): Fire rate modifier
- **Morale** (0-100%): Overall performance multiplier
- **Experience** (0-100%): Unlocks traits and bonuses

### Crew Progression
**Leveling System**:
- XP earned from combat, missions, sailing
- Level 1-50 progression
- Stat increases per level
- Trait unlocks at milestones (10, 25, 50)

**Permadeath Mechanics**:
- Tier 1-4: Low casualty risk (0-20%)
- Tier 5: 30% casualty chance
- Tier 6-9: 40-60% casualty chance
- Tier 10: 100% permadeath (all crew lost)

**Crew Management**:
- Assign crew to stations
- Swap crew between ships
- Hire new crew at ports
- Train crew to improve stats
- Replace casualties

### Crew Database Schema
**Backend Data Structure**:
```json
{
  "crewId": "uuid",
  "playerId": "uuid",
  "name": "John Smith",
  "rank": "Lieutenant",
  "station": "Gunnery",
  "level": 15,
  "experience": 45000,
  "stats": {
    "accuracy": 85,
    "reloadSpeed": 120,
    "morale": 90
  },
  "traits": ["Sharpshooter", "Veteran"],
  "assignedShip": "ship-uuid",
  "status": "alive" // alive, injured, dead
}
```

---

## 📦 System Breakdown: Module System

### Tetris-Style Inventory
**Status**: 📋 PLANNED

### Design Philosophy
**"EVE Online meets Tetris"** - Visual, spatial ship fitting

### Module Types
1. **Weapons**:
   - Main battery turrets (4-8 slots)
   - Secondary batteries (2-4 slots)
   - Torpedo tubes (2-3 slots)
   - AA guns (1-2 slots)

2. **Armor**:
   - Belt armor (side protection)
   - Deck armor (top protection)
   - Turret armor (weapon protection)
   - Reactive armor (advanced)

3. **Utilities**:
   - Fire control systems (accuracy bonus)
   - Radar (detection range)
   - Engine upgrades (speed boost)
   - Fuel tanks (range extension)
   - Repair systems (damage control)

### Fitting Mechanics
**Ship Grid System**:
- Each ship has a Tetris-style grid (e.g., 10x20 cells)
- Modules occupy multiple cells (various shapes)
- Rotate modules to fit (R key)
- Drag-and-drop placement

**Constraints**:
- **Mount Weight Limit**: Each mount has a weight capacity (module + crew weight must fit)
- **Ship Tonnage**: Total module weight can't exceed ship's displacement
- **Slot Limits**: Max weapons per category (physical hardpoints)
- **Crew Requirement**: Module installs without crew, but won't function until properly manned

**Design Philosophy**: If it fits, it works. A 1900s destroyer with a modern radar? If the mount can handle the weight (module + crew), go for it. No artificial era restrictions—just physics.

**UI/UX**:
- Visual ship layout (top-down view)
- Color-coded modules (weapon, armor, utility)
- Drag from inventory to ship grid
- Hover for module stats
- Validation on placement (red = invalid)

### Module Stats
**Example: Main Battery Turret**
```json
{
  "moduleId": "main-battery-381mm",
  "name": "381mm/45 Mark I",
  "type": "weapon",
  "tier": 7,
  "size": "4x2" // Tetris shape
  "weight": 1200, // tons
  "stats": {
    "damage": 850,
    "penetration": 680,
    "range": 25000, // meters
    "reload": 30, // seconds
    "accuracy": 75
  },
  "cost": 450000 // credits
}
```

---

## 💰 System Breakdown: Economy Foundation

### Economy Philosophy
**Status**: 📋 PLANNED

**Design Goal**: "Risk vs Reward" extraction gameplay

### Currency System
**Primary Currency**: **Credits** (₡)
- Earned from: Combat, missions, trading, loot
- Spent on: Ships, modules, crew, repairs, ammo

**Secondary Resources** (Phase 3):
- Steel, Oil, Chromium, etc.
- Used for crafting and upgrades

### Trading System
**Port Shops**:
- **Shipyard**: Buy/sell ships
- **Armory**: Buy/sell weapons and modules
- **Crew Office**: Hire crew, train crew
- **Repair Dock**: Repair damage
- **Supply Depot**: Buy ammo, fuel, consumables

**Price Dynamics** (Phase 2 - Static):
- Fixed prices per item
- No market dynamics yet (Phase 3)

**Buy/Sell Ratio**:
- Sell price = 70% of buy price
- Prevents exploit loops

### Loot System
**Loot Drops**:
- Sunk enemy ships drop loot crates
- Loot contains: Modules, credits, materials
- Loot floats at sink location
- Players must pick up to claim

**Extraction Mechanics**:
- Loot only secured when returning to port
- Die before port = lose all loot
- Risk vs reward gameplay loop

**Loot Rarity**:
- **Common** (70%): Low-tier modules, small credits
- **Uncommon** (20%): Mid-tier modules, moderate credits
- **Rare** (8%): High-tier modules, large credits
- **Legendary** (2%): Unique modules, massive credits

### Economy Loop
1. **Outfitting**: Spend credits on ammo, fuel, loadout
2. **Hunting**: Sail to combat zones
3. **Combat**: Fight enemies, earn loot
4. **Extraction**: Return to port with loot
5. **Trading**: Sell loot, buy upgrades
6. **Repeat**: Better gear → harder zones → more loot

---

## 🧪 Testing & Validation Plan

### Phase 2 Testing Strategy

#### Unit Testing (Automated)
**Status**: 📋 PLANNED

**Test Coverage**:
- [ ] Ballistics calculations (trajectory, hit detection)
- [ ] Damage calculations (penetration, armor)
- [ ] Crew stat modifiers
- [ ] Economy transactions (buy/sell validation)
- [ ] Module weight/slot validation

#### Integration Testing
**Status**: 📋 PLANNED

**Test Scenarios**:
- [ ] Combat in multiplayer (2 players fighting)
- [ ] Crew affects combat performance
- [ ] Module fitting saves/loads correctly
- [ ] Economy transactions persist
- [ ] Loot drops and pickup work

#### Multiplayer Testing
**Status**: 📋 PLANNED

**Test Cases**:
- [ ] 2-5 player combat (small battle)
- [ ] 10-20 player stress test
- [ ] Combat synchronization (no desync)
- [ ] Loot pickup race conditions
- [ ] Economy transaction conflicts

#### Balance Testing
**Status**: 📋 PLANNED

**Metrics to Validate**:
- [ ] Time to Kill (TTK): 30-90 seconds ideal
- [ ] Combat range: 5-15km optimal
- [ ] Crew impact: 20-40% performance variance
- [ ] Economy earn rate: 50k-200k credits per hour
- [ ] Module cost vs effectiveness

---

## 📊 Current Progress Tracking

### System Completion Status

#### 🔫 Combat Systems (0%)
```
Weapon Framework:     ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Damage Model:         ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Combat UI:            ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
AI Enemies:           ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
```

#### 👥 Crew Management (0%)
```
Crew Database:        ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Crew UI:              ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Crew Stats System:    ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Crew Progression:     ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Permadeath:           ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
```

#### 📦 Module System (0%)
```
Tetris UI:            ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Module Database:      ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Fitting Validation:   ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Module Effects:       ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
```

#### 💰 Economy Foundation (0%)
```
Currency System:      ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Trading UI:           ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Loot System:          ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
Economy Balance:      ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪ ⚪  0%
```

**Overall Phase 2**: 0-5% Complete

---

## 🚧 Current Blockers

### Critical Blockers
1. **Combat System Design** - Need to finalize ballistics model
   - Decision: Raycast vs projectile simulation?
   - Decision: Simple vs realistic damage model?
   - **Impact**: Blocks Weeks 1-4

2. **Crew Database Schema** - Backend database design needed
   - Need to design crew data structure
   - Decide on crew stat ranges
   - **Impact**: Blocks Week 5-6

3. **Module UI Complexity** - Tetris inventory is complex
   - Significant UI/UX work required
   - Drag-and-drop with rotation
   - **Impact**: Blocks Week 7-8

4. **Economy Balancing** - Prices and earn rates undefined
   - Need to balance economy loop
   - Test earn rates and costs
   - **Impact**: Blocks Week 9-10

### Resource Blockers
1. **Art Assets** - Need combat visual effects
   - Damage effects (fire, smoke, explosions)
   - Weapon projectiles
   - Loot crate models

2. **Audio Assets** - Combat sounds needed
   - Weapon fire sounds
   - Explosion sounds
   - Ambient combat audio

3. **Testing Resources** - Need community testers
   - Multiplayer testing requires players
   - Balance testing needs data
   - Solo dev can't test MP alone

---

## 🎯 Phase 2 Success Metrics

### Must Achieve (Critical)
- ✅ Two players can engage in combat
- ✅ Ships can be sunk
- ✅ Crew measurably affects performance
- ✅ Module fitting functional
- ✅ Economy loop operational (earn → spend)

### Should Achieve (Important)
- ✅ Combat feels satisfying and tactical
- ✅ TTK balanced (30-90 seconds)
- ✅ Crew UI intuitive and clear
- ✅ Module fitting easy to understand
- ✅ Economy balanced (no exploits)

### Nice to Have (Stretch)
- ✅ Basic AI enemies
- ✅ Combat audio
- ✅ Crew progression visible
- ✅ Loot rarity system
- ✅ Visual damage feedback

---

## 🔗 Phase 2 Dependencies

### Depends On (Phase 1) ✅
- ✅ Ship physics and controls
- ✅ Multiplayer networking
- ✅ Ocean environment
- ✅ UI framework
- ✅ Authentication system

### Required For (Phase 3)
- 📋 Combat mechanics (enables PvPvE)
- 📋 Crew system (enables permadeath)
- 📋 Economy foundation (enables trading)
- 📋 Module system (enables progression)

---

## 🗓️ Next Immediate Actions

### This Week (Week 1)
- [ ] Begin combat system design document
- [ ] Research ballistics implementations (other games)
- [ ] Prototype basic projectile system
- [ ] Design weapon database schema
- [ ] Create combat system flowchart

### Next Week (Week 2)
- [ ] Finalize combat design document
- [ ] Implement basic gun turret
- [ ] Create weapon firing input controls
- [ ] Test projectile pooling
- [ ] Begin damage model design

### Next 2 Weeks (Weeks 3-4)
- [ ] Implement damage model
- [ ] Create ship health system
- [ ] Build damage visualization
- [ ] Network combat synchronization
- [ ] Initial multiplayer combat testing

---

## 📚 Research & References

### Combat System References
- **World of Warships**: Ballistics and damage model
- **War Thunder**: Realistic penetration mechanics
- **Dreadnoughts**: Arcade naval combat feel

### Crew System References
- **Navy Field**: Crew card system (primary inspiration)
- **FTL**: Crew station mechanics
- **XCOM**: Permadeath and progression

### Module System References
- **EVE Online**: Ship fitting UI and complexity
- **Escape from Tarkov**: Tetris inventory
- **Resident Evil 4**: Spatial inventory management

### Economy References
- **Escape from Tarkov**: Extraction-based economy
- **EVE Online**: Player-driven markets
- **Hunt: Showdown**: Risk vs reward loot

---

## 🔗 Related Documentation

### Phase Documents
- [[Phase-1-Complete]] - Previous phase retrospective
- [[Phase-3-Plan]] - Next phase roadmap
- [[Development-Status]] - Overall project status

### Design Documents
- [[Combat-Overview]] - Combat system design
- [[Crew-Management]] - Crew system details
- [[Crew-Module-Mechanics]] - Crew-module interaction mechanics ✅
- [[Module-System]] - Ship fitting mechanics
- [[Module-Dependencies]] - Module requirements and weight-based fitting ✅
- [[Economy-Overview]] - Economy design
- [[Surface-Combat]] - Weapon mechanics

### Technical Documents
- [[Tech-Stack]] - Development technologies
- [[Performance-Targets]] - Performance goals
- [[Network-Architecture]] - Multiplayer infrastructure

---

## 📝 Phase 2 Notes

### Development Philosophy
**"Build the Fun First"** - Prioritize gameplay over features

**Priorities**:
1. Combat must feel satisfying (juice, feedback, impact)
2. Crew must be meaningful (not just numbers)
3. Economy must enable progression (earn → spend → upgrade)
4. Multiplayer must be stable (no desyncs or exploits)

### Solo Developer Reality
- Can't build everything perfectly
- Focus on core systems
- Iterate and improve
- Get feedback early

### Risk Management
- Combat is most complex system yet
- UI/UX is time-consuming
- Balancing requires testing
- Multiplayer adds complexity

**Mitigation**:
- Start simple, add complexity iteratively
- Prototype early, test often
- Get community feedback
- Use AI assistant (Claude Code) effectively

---

**Phase 2 Status**: 🚧 IN PROGRESS (0-5%)
**Next Milestone**: Combat Prototype (Weeks 1-2)
**Estimated Completion**: Q2 2025
**Team Confidence**: MODERATE (Complex systems ahead)

*"Phase 1 was the foundation. Phase 2 is the game."*
