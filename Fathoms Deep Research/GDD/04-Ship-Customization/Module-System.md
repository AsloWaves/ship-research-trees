# Module System

**Status**: 📋 PLANNED (Phase 2/3 feature)
**Tags**: [planned, phase2, ship-customization, inventory, tetris-system]
**Priority**: HIGH (core progression mechanic)
**Related Systems**: [Crew System](../02-Core-Systems/Crew-System.md), [Combat System](../02-Core-Systems/Combat-System.md), [Economy](../03-Economy/Economy-Overview.md)

---

## Overview

Ship customization in Fathoms Deep follows a **dual-layer system** inspired by Navy Field's slot-based fitting combined with Escape from Tarkov's tetris-style inventory management. Players have complete freedom to configure ships within physical and weight constraints, with no artificial tier restrictions—if you can fit it and crew it, you can use it.

**Core Philosophy:**
- **Weight-Based Balancing**: Module and crew weight naturally limits over-fitting on smaller ships
- **Crew-Module Integration**: Every module requires appropriately classed crew card to function optimally
- **Visual Transparency**: Equipped modules visible on ship sprites, creating tactical intelligence opportunities
- **Economic Depth**: Multiple acquisition paths (crafting, market, salvage, black market) with distinct trade-offs
- **Progressive Complexity**: Simple at low tiers, deep optimization potential at high tiers

---

## Dual Module System Architecture

### Section A: Weapon Hardpoints (Visual 3D Positioning)

**Hardpoint System Overview:**
- **Fixed 3D Positions**: Each ship class has predetermined mounting locations designed into hull structure
- **Visual Integration**: Installed turrets/weapons appear on ship sprite with accurate scale and positioning
- **Drag-Drop Interface**: Players drag turret modules from port storage or ship cargo grid ([[Inventory-System]]) onto hardpoint positions on ship view
- **Tactical Transparency**: Enemy players can identify ship capabilities by visual inspection of equipped turrets

#### Hardpoint Categories

**Main Battery Slots** (Primary armament):
- **Ship-Specific Count**: Destroyers (2-5 slots), Cruisers (3-5 slots), Battleships (3-4 slots)
- **Weight Capacity**: Varies by ship class and design era
- **Compatibility**: Accepts any main battery turret that fits weight/size limits
- **Crew Requirement**: Each main battery slot requires 1 Gunner crew card

**Secondary Battery Slots** (Mid-caliber guns):
- **Purpose**: Anti-destroyer defense, sustained fire support
- **Typical Count**: Cruisers (4-8 slots), Battleships (10-16 slots)
- **Caliber Range**: 4-inch to 6-inch guns typically
- **Crew Requirement**: Each secondary slot requires 1 Gunner crew card

**Tertiary/AA Slots** (Anti-aircraft defense):
- **Purpose**: Aircraft defense, close-range protection
- **High Slot Count**: 8-80+ depending on ship size and era
- **Module Types**: 20mm, 40mm, 5-inch dual-purpose mounts
- **Crew Requirement**: Each AA slot requires 1 AA Specialist crew card

**Special Hardpoints** (Class-specific systems):
- **Torpedo Tubes**: Destroyers (2-4 mounts), Submarines (4-6 tubes)
  - Crew: Torpedoman crew card required
- **Aircraft Catapults**: Cruisers (1-2 catapults), Battleships (2-4), Carriers (2-4)
  - Crew: Aviation crew card required per catapult
  - Requires: Aircraft Catapult Control module in Misc slot
- **Depth Charge Racks**: Destroyers (2-4 racks), Escorts (4-8 racks)
  - Crew: Damage Control crew card
- **Mine Rails**: Destroyers/Cruisers (1-2 rails)
  - Crew: Torpedoman crew card
  - Requires: Mining Equipment module

**Hardpoint Compatibility Rules:**
```
Turret Installation Check:
1. Module Type = Main/Secondary/Tertiary Battery
2. Module Physical Weight ≤ Hardpoint Capacity
3. Crew Card Assigned with matching class (Gunner/AA Specialist)
4. Total ship weight within limits after installation

Result: Green = Valid, Red = Invalid, Yellow = Over-weight warning
```

---

### Section B: Internal Ship Systems (Equipment Slot Fitting)

**Internal System Overview:**
- **Equipment Fitting Slots**: Fixed-size slots within ship's internal structure (distinct from cargo grid cells in [[Inventory-System]])
- **Size Restrictions**: Modules must match slot size (1x1, 1x2, 2x2, 2x3, 3x3, etc.)
- **Category Restrictions**: Engine slots only accept engines, Support slots only accept support modules, Misc slots universal
- **Visual Interface**: Fitting screen shows ship cross-section with slot layout
- **Note**: These are equipment installation slots, NOT cargo storage grid cells

#### Engine Slots

**Slot Characteristics:**
- **Fixed Sizes**: Ship-specific (Small ships: 1x2, Medium ships: 2x3, Large ships: 3x4)
- **Multiple Bays**: Destroyers (2 slots), Cruisers (3 slots), Battleships (4-6 slots)
- **Accepts**: Engine modules ONLY
- **Crew Requirement**: Each engine slot requires 1 Engineer crew card

**Engine Slot Examples by Ship Class:**
| Ship Class | Engine Slots | Slot Size | Total Engine Capacity |
|------------|-------------|-----------|---------------------|
| T3 Destroyer | 2 slots | 1x2 each | Compact engines only |
| T5 Light Cruiser | 3 slots | 2x2 each | Medium engines |
| T7 Battleship | 4 slots | 3x4 each | Large/Heavy-Duty engines |
| T10 Carrier | 4 slots | 3x4 each | Maximum propulsion |

**Engine Configuration Strategy:**
- **Speed Build**: All high-performance engines (max speed, high fuel consumption)
- **Endurance Build**: All heavy-duty engines (moderate speed, excellent fuel economy)
- **Hybrid Build**: Mix of engine types (balanced performance)
- **Redundancy**: Extra engine bays provide backup if engines damaged in combat

**Engine Module Types:**
- Destroyer Engines: 28-38 knots capability, varying fuel efficiency
- Cruiser Engines: 28-38 knots, higher power requirements
- Battleship Engines: 23-32 knots, massive fuel consumption
- Specialized Variants: High-efficiency, experimental high-speed, endurance-optimized

---

#### Support Slots

**Slot Characteristics:**
- **Variable Sizes**: 1x1, 1x2, 2x2, 2x3, 3x3 depending on ship design
- **Quantity**: Scales with ship size (Destroyers: 3-8 slots, Battleships: 18-24 slots)
- **Accepts**: Support modules ONLY (crew welfare, engineering support, logistics)
- **Crew Requirement**: Varies by support module type (typically Engineer or Support crew)

See [Utility-Modules.md](Utility-Modules.md) for detailed support module specifications.

---

#### Misc Slots

**Slot Characteristics:**
- **Universal Acceptance**: Can accept ANY module type (engines, support, or misc-specific modules)
- **Variable Sizes**: Ship-specific (1x1 to 3x3 possible)
- **Quantity**: Lower than support slots (Destroyers: 2-4, Battleships: 6-12)
- **Crew Requirement**: Varies by module (typically Electronics crew cards)

See [Utility-Modules.md](Utility-Modules.md) for detailed misc module specifications.

---

## Module-Crew Integration System

**Core Principle**: Every module requires an appropriately classed crew card to function at optimal efficiency.

### Crew-Module Assignment Mechanics

**Assignment Process:**
1. **Install Module** in ship slot (hardpoint or internal system slot)
2. **Assign Crew Card** to that module's crew slot
3. **Validation Checks**:
   - Crew class matches module type (Gunner → Turret, Engineer → Engine)
   - Crew card not already assigned to another module
   - Crew skill level meets module minimum requirements (if any)
4. **Result**: Module operates at efficiency based on crew level and specialization

**Crew Class → Module Type Compatibility:**

| Module Type | Required Crew Class | Notes |
|-------------|-------------------|-------|
| Main Battery Turret | Gunner | Any gunner works on any caliber |
| Secondary Battery | Gunner | Same crew pool as main battery |
| AA Mount | AA Specialist | Separate class from gunners |
| Torpedo Tubes | Torpedoman | Also operates mine rails |
| Engine | Engineer | Any engineer works on any engine |
| Radar System | Radar Operator (Electronics class) | |
| Sonar System | Radar Operator (Electronics class) | |
| Fire Control System | Gunner (Fire Control specialization) | |
| Damage Control Station | Damage Control (Engineer subclass) | |
| Medical Bay | Medic | Requires research unlock |
| Support Modules | Support Crew | Generic support class |
| Aircraft Catapult | Aviation | Carriers/cruisers/battleships |
| Submarine Periscope | Command | Submarine captains |

### Module Efficiency System

> **Note**: For complete crew-module interaction mechanics, see [[Crew-Module-Mechanics]].

**Core Efficiency Formula:**

Module efficiency combines two factors: **Sailor Factor** (crew survival) and **Stat Factor** (crew skill):

```
Module_Efficiency = Sailor_Factor × Stat_Factor

Where:
  Sailor_Factor = Current_Sailors / Max_Sailors
  Stat_Factor = 1.0 + ((Primary_Stat - 15) × 0.02)

Stat Value → Stat Factor:
  Stat 7:  0.84 (16% penalty)
  Stat 15: 1.00 (baseline)
  Stat 25: 1.20 (+20% bonus)
  Stat 35: 1.40 (+40% bonus)
  Stat 50: 1.70 (+70% bonus, cap)
```

**Key Design Insight**: Modules do NOT have levels. Any crew card can operate any module. Higher-level crews are more effective because they have:
1. **Better stats** (trained over time)
2. **More sailors** (casualty buffer)

**Efficiency Impact by Module Type:**

**Main Battery Turret:**
- **Spread Control**: Efficiency affects shell grouping around aim point
  - 100% efficiency = Base spread
  - 140% efficiency = 40% tighter spread (Accuracy 35 gunner)
  - 50% efficiency = 2x wider spread (heavy casualties)
- **Reload Speed**: Efficiency directly affects reload time
  - 100% efficiency = 30 second base reload
  - 134% efficiency = 22.4 second reload (Reload 32 gunner)
  - 50% efficiency = 60 second reload (casualties)

**Engine:**
- **Max Speed**: Efficiency affects top speed with 70% floor
  - Speed_Mod = 0.7 + (0.3 × Efficiency)
  - 100% efficiency = 100% speed
  - 50% efficiency = 85% speed (floor prevents total loss)
- **Fuel Efficiency**: Higher efficiency = better fuel economy
- **Acceleration**: Efficiency affects time to reach max speed

**Radar System:**
- **Detection Range**: Efficiency % affects maximum detection distance
  - 100% efficiency = Base range
  - 140% efficiency = 140% of base range
  - 50% efficiency = 50% of base range
- **Target Lock Speed**: Higher efficiency = faster target updates

**Damage Control Station:**
- **Fire Suppression Speed**: Efficiency directly affects extinguishing time
- **Flooding Control**: Efficiency affects pumping effectiveness

### Unassigned & Zero-Crew Module Behavior

**Modules without assigned crew are NON-FUNCTIONAL:**
- Main turret with no gunner: Cannot fire
- Engine with no engineer: No propulsion contribution
- Radar with no operator: No detection
- **Warning Indicator**: Red icon on module slot showing "UNMANNED"

**Modules with assigned crew but 0 sailors are NON-FUNCTIONAL:**
- Crew card remains assigned (not destroyed)
- Module displays "CREW WIPED OUT" status
- Can replenish sailors at port to restore function
- Even 1 sailor remaining = minimal function (0.22% for Level 100 crew)

**Strategic Implications:**
- Players must maintain adequate crew roster for all equipped modules
- Higher-level crews absorb casualties better (more sailors)
- Losing sailors in battle creates gradual performance degradation
- Backup crew cards essential for high-tier operations

### Multiple Module Management

**Example: Battleship with 3 Main Turrets and 4 Engines:**
- **Turrets**: Requires 3 Gunner crew cards (one per turret)
- **Engines**: Requires 4 Engineer crew cards (one per engine)
- **Minimum Crew**: 7 specialized crew cards just for turrets and engines
- **Realistic Loadout**: 15-20 crew cards total (includes secondaries, AA, support modules)

**Crew Capacity Limits by Ship Class:**

| Ship Class | Total Crew Card Capacity | Typical Module Count |
|------------|------------------------|-------------------|
| T1 Destroyer | 8-12 crew cards | 5-8 modules |
| T3 Cruiser | 12-18 crew cards | 10-15 modules |
| T5 Battleship | 20-30 crew cards | 18-25 modules |
| T8 Carrier | 25-40 crew cards | 25-35 modules |
| T10 Super Battleship | 30-45 crew cards | 30-40 modules |

**Crew Weight Impact:**
- Each crew card has weight based on sailor count and level
- High-level crew cards can weigh 300-1200 tons
- Must balance crew quality vs. ship weight capacity
- Natural progression: bring veteran crew to larger ships as you tier up

---

## Module Acquisition & Progression

### Acquisition Pathways

**1. Research & Development** (Unlock Path):
- Progressive unlock trees with credit, resource, and time investment
- Permanent blueprint ownership
- Craft unlimited quantities at production cost
- Long-term cost savings (30-70% cheaper than market)
- Example: 16" Iowa gun unlock costs ₡5M + 400 hours research, craft for ₡45K vs. ₡275K market price

**2. Market Purchase** (Direct Purchase Path):
- Buy from NPC vendors or player marketplace
- Immediate access, no research time
- Higher per-unit cost
- No blueprint retention
- Example: Buy 16" Iowa gun instantly for ₡275K without unlocks

**3. Black Market** (Unrestricted Access):
- Purchase any module regardless of nation or unlock status
- 200-400% markup over standard pricing
- Access to enemy nation technology
- Requires black market reputation
- Example: Japanese 18" turret costs ₡450K on black market (vs. ₡150K Japanese vendor price)

**4. Extraction Loot**:
- Salvage modules from defeated enemy ships
- Condition-based value (100% new → 20% broken)
- Damaged modules require repair before use
- High-quality RNG modules (120%+ stats) extremely valuable

**5. Crafting** (Blueprint-Based Production):
- Requires unlocked blueprint + resources + time
- Quality variance: 70-130% base stats (RNG roll)
- Crafting skill improves quality odds
- Progression: Novice → Legendary crafter (eliminates poor quality rolls)

### Quality Variance & Crafting RNG

**Module Quality Mechanics:**
- **RNG Range**: 70-130% of base statistics
- **Distribution**: Bell curve centered on 100%
- **Probability**:
  - 70-85% (Poor): 15% chance
  - 86-95% (Below Average): 20% chance
  - 96-105% (Average): 30% chance
  - 106-115% (Above Average): 20% chance
  - 116-125% (Excellent): 12% chance
  - 126-130% (Exceptional): 3% chance

**Economic Impact:**
- Poor quality: Sells for 50-70% market value
- Exceptional quality: Sells for 180-250% market value, highly sought after
- Players craft multiple modules seeking high-quality rolls
- Exceptional modules become prestige items worth millions

**Crafting Skill Progression:**
- Novice (0-50 crafted): Standard RNG (70-130%)
- Skilled (51-200): Improved RNG (75-130%)
- Expert (201-500): Superior RNG (80-130%)
- Master (501-1000): Optimal RNG (85-130%)
- Legendary (1000+): Ultimate RNG (90-130%) - poor quality eliminated

---

## Installation & Repair Time System

**Reduced Real-Time Timers for Fast-Paced Gameplay:**

Fathoms Deep uses shortened installation and repair timers to keep players engaged and minimize downtime between combat sessions.

### Module Installation Times

**Installation at Port (Friendly Ports Only):**

**Module Source**: Modules can be installed from port storage OR directly from ship cargo grid ([[Inventory-System]])

| Module Size | Installation Time | Concurrent Installation | Examples |
|-------------|------------------|----------------------|----------|
| **Small** | 30 seconds - 2 minutes | Up to 5 simultaneous | AA mounts, sensors, 1x1 modules |
| **Medium** | 2-5 minutes | Up to 3 simultaneous | Secondary turrets, support modules, 1x2 to 2x2 |
| **Large** | 5-15 minutes | Up to 2 simultaneous | Main turrets, engines, 2x3 to 3x3 |
| **Massive** | 10-20 minutes | 1 at a time | Battleship triple 16" turrets, advanced systems |

**Concurrent Installation Mechanics:**
- **Base Capacity**: All ports support 1 concurrent installation by default
- **Hire Shipyard Workers**: Pay fee to unlock additional concurrent slots
  - **Small Port**: ₡5,000 → unlock 2 concurrent slots
  - **Medium Port**: ₡10,000 → unlock 3 concurrent slots
  - **Large Port**: ₡20,000 → unlock 5 concurrent slots
- **Strategic Use**: Install entire ship loadout in parallel (15 minutes vs. 2+ hours sequential)

**Installation Example (T7 Battleship Refit):**
```
Sequential Installation (1 worker):
- 3 main turrets: 15 min each = 45 minutes
- 4 engines: 10 min each = 40 minutes
- 8 support modules: 3 min each = 24 minutes
- 12 AA mounts: 1 min each = 12 minutes
Total: 121 minutes (2 hours 1 minute)

Parallel Installation (5 workers at Large Port):
- Wave 1: 3 main turrets + 2 engines = 15 minutes
- Wave 2: 2 engines + 3 support modules = 10 minutes
- Wave 3: 5 support modules + 5 AA mounts = 3 minutes
- Wave 4: 7 AA mounts = 1 minute
Total: 29 minutes (76% time saved)
```

### Port Repair Times

**At-Port Full Repair (Friendly/Neutral Ports):**

| Damage Severity | Repair Time | Acceleration (2x Cost) | Priority (5x Cost) | Example |
|----------------|-------------|---------------------|-------------------|---------|
| **Minor Module Damage** | 1-5 minutes | 30 sec - 2.5 min | 12 sec - 1 min | Radar 75% HP |
| **Major Module Damage** | 5-15 minutes | 2.5 - 7.5 min | 1 - 3 min | Engine 25% HP |
| **Hull Damage** | 10-30 minutes | 5 - 15 min | 2 - 6 min | 40% hull integrity |
| **Critical Rebuild** | 30 min - 2 hours | 15 min - 1 hour | 6 min - 24 min | Multiple destroyed modules |

**Repair Cost Scaling:**
- **Minor Damage**: ₡5,000 - ₡25,000
- **Major Damage**: ₡50,000 - ₡200,000
- **Hull Damage**: ₡100,000 - ₡500,000
- **Critical Rebuild**: ₡500,000 - ₡3,000,000

**Acceleration Options:**
- **Standard Repair**: Base time, base cost
- **Expedited Repair** (2x cost): 50% time reduction
- **Priority Repair** (5x cost): 75% time reduction

**Example Repair (T8 Battleship Post-Combat):**
```
Standard Repair:
- 2 main turrets (major damage): 10 min each = 20 minutes
- 1 engine (minor damage): 3 minutes
- Hull damage (45% → 100%): 25 minutes
- Total Time: 48 minutes
- Total Cost: ₡850,000

Expedited Repair (2x cost):
- Total Time: 24 minutes
- Total Cost: ₡1,700,000

Priority Repair (5x cost):
- Total Time: 12 minutes
- Total Cost: ₡4,250,000
```

### At-Sea Emergency Repairs

**Field Repair Limitations:**
- **Cannot Fully Repair**: Maximum 75% HP restoration per module
- **Requires Consumables**: Repair Kits consumed from inventory
- **Time-Consuming**: 30 seconds - 2 minutes per repair attempt
- **Cooldown**: 5-10 minutes between repair attempts on same module

**Repair Kit Types:**

**Small Repair Kit** (1x1 inventory):
- **Restores**: 10-25% module HP
- **Repair Time**: 30 seconds
- **Cooldown**: 5 minutes
- **Weight**: 0.5 tons per kit
- **Cost**: ₡5,000 per kit
- **Best For**: Minor damage, quick fixes, AA/secondary systems

**Large Repair Kit** (2x2 inventory):
- **Restores**: 25-50% module HP
- **Repair Time**: 90 seconds
- **Cooldown**: 10 minutes
- **Weight**: 2 tons per kit
- **Cost**: ₡20,000 per kit
- **Best For**: Major damage, main turrets, engines, critical systems

**Emergency Patch** (1x2 inventory):
- **Restores**: Temporary 50% function (degrades over time)
- **Repair Time**: 45 seconds
- **Cooldown**: None (can spam if have kits)
- **Duration**: Module breaks again after 30-60 minutes
- **Weight**: 1 ton per kit
- **Cost**: ₡8,000 per kit
- **Best For**: Emergency situations, temporary fixes to reach port

**Machine Shop Module Bonus:**
- If equipped, all repair kit effectiveness increased by 25-50%
- Small Kit: Restores 12.5-37.5% (instead of 10-25%)
- Large Kit: Restores 31.25-75% (instead of 25-50%)
- Reduces cooldown by 20%

**Example At-Sea Repair (T6 Cruiser Mid-Combat):**
```
Situation: Main turret #2 destroyed (0% HP), need firepower to continue combat

Option 1 (Large Repair Kit):
- Use Large Repair Kit: 90 seconds repair time
- Result: Turret restored to 45% HP (functional but reduced performance)
- Can fire but 55% longer reload, 45% accuracy
- Cooldown: 10 minutes before can repair again

Option 2 (Emergency Patch):
- Use Emergency Patch: 45 seconds repair time
- Result: Turret restored to 50% temporary function
- Can fire normally for 30-60 minutes
- Turret breaks again after timer expires (must use another kit or retreat to port)

Strategic Decision: Emergency patch if close to port (30 min away), Large Kit if extended combat expected
```

---

## Offline Crew Training System

**Passive Progression While Logged Out:**

Fathoms Deep implements an offline training system allowing crew cards to gain experience while players are logged out, reducing grind and rewarding long-term progression.

### Core Training Mechanics

**Offline XP Accumulation:**
- **Accumulation Rate**: 1 XP per 10 minutes offline
- **Maximum Cap**: 300 XP per crew card
- **Cap Duration**: ~50 hours offline (3000 minutes ÷ 60 = 50 hours)
- **Claim Requirement**: Must manually claim XP on login (button/notification prompt)

**Training Assignment System:**

**Pre-Logout Assignment:**
1. **Access Training Interface** at any friendly port before logging out
2. **Select Crew Cards** to train (drag crew cards to training slots)
3. **Choose Skill Track** for each crew card:
   - Gunnery (Main Battery, Secondary, AA specializations)
   - Engineering (Propulsion, Damage Control, Repair)
   - Navigation (Piloting, Chart Reading, Weather Prediction)
   - Electronics (Radar, Sonar, Electronic Warfare)
   - Aviation (Aircraft Operations, Carrier Coordination)
   - Command (Leadership, Tactics, Crisis Management)
4. **Confirm Training** and log out

**Post-Login Claim:**
1. **Login Notification**: "5 crew cards have completed training! 300 XP available."
2. **Click Claim**: XP distributed to trained crew cards
3. **Result**: Each crew card gains 300 XP in assigned skill track

**Per-Crew Card XP:**
- Each crew card assigned to training gets **full 300 XP** (NOT shared)
- If 3 crew cards training → Each gets 300 XP = 900 XP total distributed
- If 10 crew cards training → Each gets 300 XP = 3,000 XP total distributed

**Strategic Implications:**
- Incentive to train multiple crew cards simultaneously
- No penalty for training full crew roster
- Encourages maintaining diverse crew library (gunners, engineers, specialists)

### Premium Account Enhancement

**Premium Account Benefits (Optional Monetization):**
- **Standard Account**: Train up to 5 crew cards simultaneously
- **Premium Account**: Train up to 15 crew cards simultaneously (3x capacity)
- **Elite Premium Account**: Train up to 30 crew cards simultaneously (6x capacity)
- **Premium Bonus**: +50% offline XP accumulation rate (1.5 XP per 10 minutes = 450 XP cap)

**Example Comparison (48 hours offline):**

| Account Type | Crew Trained | XP per Crew | Total XP Gained |
|-------------|--------------|-------------|-----------------|
| Standard | 5 crew | 300 XP | 1,500 XP |
| Premium | 15 crew | 450 XP | 6,750 XP |
| Elite Premium | 30 crew | 450 XP | 13,500 XP |

**Premium Value Proposition:**
- Faster crew development for players with limited playtime
- Supports maintaining multiple ship loadouts (multiple specialized crews)
- Optional (not pay-to-win, just time-saver)

### Training Enhancements

**Training Facility Quality (Port-Based):**

Ports have varying training facility quality, affecting XP gain rates:

| Port Tier | Facility Quality | Offline XP Rate | Cap Increase |
|-----------|-----------------|----------------|--------------|
| T0-T1 (Small Port) | Basic | 1 XP / 10 min | 300 XP (base) |
| T2-T3 (Medium Port) | Improved | 1.2 XP / 10 min | 360 XP |
| T4-T5 (Large Port) | Advanced | 1.5 XP / 10 min | 450 XP |
| T6+ (Capital Port) | Elite | 2 XP / 10 min | 600 XP |

**Strategic Port Selection:**
- Logout at capital ports for maximum training benefit
- Trade-off: Capital ports may be in contested zones (risk vs. reward)
- Long-term players establish "training bases" at high-tier friendly ports

**Naval Academy Module** (Ship Module Enhancement):

**Naval Academy Support Module:**
- **Size**: 2x3 (support slot)
- **Effects**:
  - +50% offline XP bonus (stacks with port bonuses)
  - Allows training 3 additional crew cards beyond account limit
  - Reduces XP cost for classification unlocks by 25%
- **Weight**: 45 tons
- **Crew**: 1 Support crew card required
- **Cost**: ₡850,000 (expensive, late-game module)
- **Strategic Use**: Dedicated training ships, crew development focus

**Combined Bonuses Example:**
```
Premium Account + Capital Port + Naval Academy Module:

Base XP Rate: 1 XP / 10 min
Premium Bonus: +50% (1.5 XP / 10 min)
Capital Port: +100% (3 XP / 10 min)
Naval Academy: +50% of base (3.5 XP / 10 min)

Result: 3.5 XP per 10 minutes = 1,050 XP cap (~50 hours offline)
Training Capacity: 15 (Premium) + 3 (Naval Academy) = 18 crew cards
Total XP Distributed: 18 × 1,050 = 18,900 XP per 50-hour offline period
```

**Skill Books** (Consumable XP Boosters):

**Gunnery Manual** (Consumable Item):
- **Effect**: +500 XP instant grant to Gunnery skill
- **Inventory**: 1x1 slot
- **Weight**: 0.1 tons
- **Cost**: ₡50,000 (NPC vendors), ₡35,000-45,000 (player market)
- **Acquisition**: Mission rewards, salvage drops, crafting
- **Strategic Use**: Fast-track specific skills, push crew over level thresholds

**Available Skill Books:**
- Gunnery Manual (Gunner skill)
- Engineering Handbook (Engineer skill)
- Navigation Charts (Navigator skill)
- Electronics Technical Manual (Electronics skill)
- Aviation Operations Guide (Aviation skill)
- Command Leadership Principles (Command skill)

**Veteran Mentorship System** (Crew-to-Crew Training):

**How It Works:**
1. **Assign Veteran Crew** (Level 50+) as mentor
2. **Assign Rookie Crew** (Level 1-49) as student
3. **Offline Training**: Both assigned to same skill track
4. **XP Distribution**:
   - Veteran: Receives 50% normal XP (150 XP at cap)
   - Rookie: Receives 150% normal XP (450 XP at cap)
5. **Mentorship Bonus**: Rookie gains +50% XP, Veteran sacrifices 50% for teaching

**Strategic Use:**
- Fast-track new crew cards to operational levels
- Utilize high-level crew cards that are near cap (Level 180+)
- Efficient use of offline XP pool

**Example Mentorship Setup:**
```
Mentor: Level 150 Master Gunnery Officer (near level cap, slow progression)
Student: Level 15 Rookie Gunner (needs fast development)

Offline Training (48 hours at T3 Port):
- Normal XP Cap: 360 XP
- Mentor Receives: 180 XP (50% normal) → Level 150 → 150.18 (+0.18 levels)
- Student Receives: 540 XP (150% normal) → Level 15 → 20.4 (+5.4 levels)

Result: Rookie crew rapidly promoted to operational levels, veteran crew still progresses (slower but acceptable)
```

---

## Integration with Other Systems

**Crew System:**
- Module efficiency tied to sailor count and crew stats (see [[Crew-Module-Mechanics]])
- Crew weight impacts total ship weight calculations (mount capacity = module + crew weight)
- Crew cards act as consumable resources with insurance protection
- Generic classifications allow flexibility (Gunner works on any turret type)

**Combat System:**
- Module damage affects ship combat performance in real-time
- HP pool damage system with individual module damage (turrets/engines damaged independently from hull HP)
- Emergency repairs critical for sustained combat operations

**Economy System:**
- Module acquisition drives player economy (crafting, trading, looting)
- Quality variance creates high-value item market
- Insurance system provides economic risk management

**Progression Trees:**
- Module unlocks tied to research tree progression
- Blueprint ownership enables crafting professions
- Specialized modules locked behind faction/nation research

---

## Summary & Future Considerations

**Complete Module System Includes:**

✅ **Dual Module System**: Weapon hardpoints (visual 3D drag-drop) + Internal systems (grid-based slots)
✅ **Comprehensive Module Categories**: 40+ module types across turrets, engines, support, and misc systems
✅ **Crew-Module Integration**: Every module requires appropriately classed crew card for optimal performance
✅ **Quality Variance System**: 70-130% RNG for crafted modules with crafting skill progression
✅ **Reduced Real-Time Timers**: 30 seconds - 20 minutes for installation, 1 minute - 2 hours for repairs
✅ **Offline Training System**: 300 XP per crew card, premium account options, training facility bonuses

**Future Enhancements:**
- Module upgrade paths (improve existing modules vs. replacing)
- Special event modules (limited-time variants)
- Modular refits (historical ship configurations as presets)
- Cross-faction module trading restrictions (black market expansion)

---

**End of Module System Specification**
