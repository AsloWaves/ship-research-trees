# Carrier Operations System - Comprehensive Air Power Management

**Document Type**: Combat System Design
**Status**: 📋 PLANNED (Phase 2 Priority)
**Tags**: [planned, phase2, combat-systems, carriers, aircraft, air-warfare]
**Priority**: HIGH
**Last Updated**: 2025-01-17

---

## Document Purpose

This document details the complete carrier operations system for Fathoms Deep, covering aircraft management, flight deck operations, squadron command, air-to-air combat, strike coordination, and carrier vulnerability in extraction-based gameplay.

---

## The Carrier Experience

Command a floating airbase projecting power across hundreds of kilometers while managing complex flight operations, resource logistics, and multi-domain threats. Carrier gameplay balances strategic positioning, tactical air operations, and vulnerable extraction phases.

**Key Challenges**:
- Complex multi-squadron coordination
- Resource-intensive operations (fuel, ammunition, aircraft)
- Vulnerable to submarines and surface ambush
- High-stakes extraction with valuable aircraft inventory
- Crew-intensive operations requiring specialized personnel

---

## Carrier Tier Progression & Class Types

### Unlock Requirements

**Carrier Access** requires completion of T5 Destroyer and 150,000 credits + Advanced Naval Command Certification. This ensures players have proven naval combat competence before commanding the most complex vessel type.

**Why Carriers Require T5 Destroyer:**
1. **Complexity**: Multi-domain operations require advanced tactical understanding
2. **High Cost**: Carriers are expensive to operate and devastating to lose
3. **Crew Intensive**: Requires 200+ trained crew members
4. **Strategic Value**: Carriers change battlefield dynamics, require mature gameplay

---

### Carrier Tier Structure (T1-T10)

#### **Tier 1-3 Carriers - Escort & Light Carriers**

**Ship Types**: CVE (Escort Carriers), CVL (Light Carriers)

**Example Ships**:
- **T1**: USS Bogue (CVE), HMS Audacity (CVE) - Basic escort carriers
- **T2**: USS Independence (CVL), HMS Unicorn (CVL) - Light fleet carriers
- **T3**: USS Sangamon (CVE), HMS Activity (CVL) - Advanced escort carriers

**Characteristics**:
- **Aircraft Capacity**: 20-40 aircraft in 3-4 wings
- **Operational Role**: Convoy escort, ASW operations, limited strike capability
- **Learning Focus**: Basic air operations, carrier positioning, resource management
- **Crew Requirements**: 100-150 crew members
- **Vulnerability**: Moderate armor, can survive some mistakes

---

#### **Tier 4-6 Carriers - Fleet Carriers**

**Ship Types**: CV (Fleet Carriers)

**Example Ships**:
- **T4**: HMS Ark Royal (CV), IJN Ryujo (CV)
- **T5**: USS Essex (CV), HMS Illustrious (CV), IJN Shokaku (CV) ← Mid-tier reference ships
- **T6**: USS Midway (CV), HMS Audacious (CV)

**Characteristics**:
- **Aircraft Capacity**: 50-80 aircraft in 4-6 wings
- **Operational Role**: Fleet operations, major strikes, air superiority
- **Complexity**: Full multi-domain operations, coordinated strike packages
- **Crew Requirements**: 200-250 crew members
- **Vulnerability**: Heavy AA defenses but still vulnerable to coordinated attacks

---

#### **Tier 7-9 Carriers - Super Carriers**

**Ship Types**: CVA (Attack Carriers), CVN (Nuclear - if extending to early Cold War)

**Example Ships**:
- **T7**: USS Forrestal-class concepts (late 1940s designs)
- **T8**: Advanced fleet carriers with enhanced capability
- **T9**: Ultimate WWII-era carrier technology

**Characteristics**:
- **Aircraft Capacity**: 80-100+ aircraft in 6-8 wings
- **Operational Role**: Theater-level air power projection, multi-carrier coordination
- **Advanced Features**: Enhanced radar, improved deck operations, superior damage control
- **Crew Requirements**: 250-300 crew members
- **Risk**: Ship/crew card permadeath begins at T6 (10%), escalates to 60% at T9

---

#### **Tier 10 Carriers - Apex Carriers**

**Ship Types**: Ultimate carriers, nation-specific supercarriers

**Example Ships**:
- USS United States (CV-58) concept
- IJN Shinano (converted super-battleship to carrier)
- HMS Malta-class supercarrier concept
- KMS Graf Zeppelin II (advanced concept)

**Characteristics**:
- **Aircraft Capacity**: 100-120+ aircraft in 8-10 wings
- **Operational Role**: Server-defining air power, strategic dominance
- **Ultimate Features**: Maximum range, best aircraft, elite crew required
- **Crew Requirements**: 300+ crew members
- **FULL PERMADEATH**: 100% ship and crew loss on destruction
- **Server Impact**: T10 carrier operations become server-wide events

---

### Carrier Type Comparison

| Tier | Type | Aircraft | Wings | Crew | Cost | Death Risk | Best For |
|------|------|----------|-------|------|------|------------|----------|
| T1-T3 | CVE/CVL | 20-40 | 3-4 | 100-150 | Low | 0% | Learning, convoy escort |
| T4-T6 | CV | 50-80 | 4-6 | 200-250 | Med | 0-10% | Fleet operations |
| T7-T9 | CVA | 80-100 | 6-8 | 250-300 | High | 20-60% | Strategic strikes |
| T10 | Super CV | 100-120 | 8-10 | 300+ | Extreme | 100% | Elite dominance |

---

### Tier-Based Capability Scaling

**Aircraft Variety by Tier**:
- **T1-T3**: Basic aircraft (F4F Wildcat, SBD Dauntless, TBD Devastator)
- **T4-T6**: Standard aircraft (F6F Hellcat, SBD Dauntless, TBF Avenger) ← Reference tier
- **T7-T9**: Advanced aircraft (F8F Bearcat, SB2C Helldiver, AD Skyraider concepts)
- **T10**: Ultimate aircraft (early jet fighters, advanced bombers)

**Operational Range by Tier**:
- **T1-T3**: 50-100km effective range (coastal operations)
- **T4-T6**: 100-150km effective range (open ocean operations)
- **T7-T9**: 150-200km effective range (strategic range)
- **T10**: 200-300km effective range (theater-level power projection)

**Resource Consumption Scaling**:
- **T1-T3**: Low fuel/ammunition costs, forgiving for new carrier players
- **T4-T6**: Moderate costs, must manage resources carefully
- **T7-T9**: High costs, expensive operations requiring profitable missions
- **T10**: Extreme costs, every sortie must justify expenditure

---

### Carrier Progression Path Example

**Recommended Learning Path** (200-400 hours to T10 carrier):
1. **Complete T5 Destroyer** (100+ hours) - Prerequisite
2. **T1-T2 Escort Carriers** (20 hours) - Learn basic air operations
3. **T3 Light Carrier** (30 hours) - Advanced air tactics
4. **T4-T5 Fleet Carriers** (50 hours) - Multi-domain operations mastery
5. **T6-T7 Super Carriers** (80 hours) - Elite operations with permadeath risk
6. **T8-T9 Advanced Carriers** (100 hours) - High-stakes strategic operations
7. **T10 Apex Carrier** (150+ hours) - Ultimate achievement

**Note**: The following mechanics (Movement Controls, Aircraft Management, etc.) apply to ALL carrier tiers, but scale in complexity and capability as tier increases.

---

## Carrier Movement Controls - Strategic Positioning

### Semi-Auto Movement - Precision Maneuvering

**Use Case**: Combat situations requiring precise positioning and immediate course changes

**Control Features**:
- **Waypoint Setting**: Right-click to set navigation waypoints with immediate response
- **Speed Control**: F key (increase speed) / V key (decrease speed) for manual throttle management
- **Continuous Movement**: Ship maintains last bearing and speed after reaching waypoint
- **Course Correction**: Must actively set new waypoints to change direction

**Tactical Applications**:
- Maintaining optimal distance from enemy surface ships (80-120km)
- Quick course changes to avoid submarine threats
- Precise positioning for aircraft recovery operations

#### **Example Scenario: USS Hornet Operating in Contested Pacific Waters**

USS Hornet detects German surface raiders approaching from northwest. Captain switches to Semi-Auto, sets series of waypoints to maintain 90km separation while keeping into-wind heading for aircraft operations. Manual speed control allows optimization of fuel consumption while maintaining tactical flexibility.

---

### Auto Movement - Operational Efficiency

**Use Case**: Long-range transit and sustained flight operations

**Control Features**:
- **Single Waypoint**: Right-click sets destination with automatic pathfinding and speed optimization
- **Automatic Speed**: Ship calculates optimal speed for fuel efficiency and arrival timing
- **Full Stop**: Automatically stops upon reaching destination to conserve fuel
- **Hands-Free Operation**: Frees player attention for complex aircraft management

**Strategic Benefits**: Allows focus on air operations during extended missions

#### **Example Scenario: HMS Ark Royal Long-Range Transit**

HMS Ark Royal sets Auto-movement waypoint 200km northeast to intercept Italian convoy. Auto-speed maintains 18 knots for optimal fuel consumption. Captain focuses on preparing 3 torpedo bomber wings and 2 fighter escort wings while ship transits autonomously. Upon arrival, switches to Semi-Auto for tactical maneuvering during air operations.

---

## Aircraft Wing Management System - Air Power Coordination

### Pre-Flight Preparation - Mission Planning Phase

#### **Wing Configuration by Carrier Class**

**Note**: The following examples represent **T5 Fleet Carriers** (mid-tier reference ships). Lower tier carriers (T1-T4) have fewer wings and reduced aircraft capacity, while higher tier carriers (T6-T10) have more wings and greater capacity.

**USS Essex-Class (T5 USA Fleet Carrier)**: 6 Available Wings
- **Wing 1-2**: Fighter squadrons (F6F Hellcat) - 12 aircraft each
- **Wing 3-4**: Dive bomber squadrons (SBD Dauntless) - 12 aircraft each
- **Wing 5-6**: Torpedo bomber squadrons (TBF Avenger) - 12 aircraft each
- **Total**: Maximum operational flexibility with 72 aircraft

**HMS Illustrious-Class (T5 UK Fleet Carrier)**: 4 Available Wings
- **Wing 1**: Fighter squadron (Seafire) - 16 aircraft
- **Wing 2**: Fighter-bomber squadron (Seafire FB) - 12 aircraft
- **Wing 3-4**: Torpedo bomber squadrons (Swordfish/Barracuda) - 12 aircraft each
- **Total**: Balanced operations with 52 aircraft

**IJN Shokaku-Class (T5 Japan Fleet Carrier)**: 5 Available Wings
- **Wing 1**: Fighter squadron (A6M Zero) - 18 aircraft
- **Wing 2**: Fighter-bomber squadron (A6M with bombs) - 12 aircraft
- **Wing 3-4**: Dive bomber squadrons (D3A Val) - 15 aircraft each
- **Wing 5**: Torpedo bomber squadron (B5N Kate) - 18 aircraft
- **Total**: Aggressive strike capability with 78 aircraft

**Tier Scaling Examples**:
- **T1 Escort Carrier** (USS Bogue): 3 wings, 20-30 total aircraft
- **T3 Light Carrier** (USS Independence): 4 wings, 40-50 total aircraft
- **T7 Super Carrier** (Advanced design): 7 wings, 90-100 total aircraft
- **T10 Apex Carrier** (Ultimate): 8-10 wings, 120+ total aircraft

---

### Crew Assignment & Specialization

#### **Crew Requirements Scale by Carrier Tier**

**Tier-Based Crew Scaling**:
- **T1-T3 Carriers**: 100-150 total crew (smaller escort/light carriers)
- **T4-T6 Carriers**: 200-250 total crew (fleet carriers) ← Examples below reference this tier
- **T7-T9 Carriers**: 250-300 total crew (super carriers)
- **T10 Carriers**: 300+ total crew (apex carriers)

**Required Crew Positions per Wing** (7-50 Stat System):
- **Squadron Leader** (Fighter/Bomber Pilot): Affects wing accuracy and coordination (Dogfighting/Accuracy stat 7-50)
- **Flight Leader** (Fighter/Bomber Pilot): Reduces preparation time (stat-based efficiency)
- **Wingmen**: Standard pilots - 6-10 additional crew per wing
- **Ground Crew** (Engineer classification): Affects preparation speed and reliability (Repair Speed stat 7-50)

**Crew Stat Impact Examples** (applies to all tiers):
- **Fighter Pilot Dogfighting stat 50** (legendary): +97% air-to-air effectiveness, +70% coordination, -60% prep time
- **Bomber Pilot Accuracy stat 50** (legendary): +97% bombing accuracy, -60% prep time
- **Engineer Repair Speed stat 50** (legendary): -60% preparation time, +105% aircraft reliability
- **Rookie stats 7-10**: -25% to -15% accuracy, +35% to +15% fuel consumption, higher loss rates

**Tier-Based Crew Complexity**:
- **T1-T3**: Simpler crew management, fewer specializations needed
- **T4-T6**: Moderate complexity, specialized crew beneficial
- **T7-T10**: High complexity, elite specialized crew essential for survival

---

## Inventory Requirements - Tetris Logistics

### Aircraft Storage System

**Physical Aircraft Inventory Management**:
- **F6F Hellcat**: 2x3 inventory spaces (6 slots) - Medium fighter
- **SBD Dauntless**: 2x4 inventory spaces (8 slots) - Dive bomber
- **TBF Avenger**: 3x4 inventory spaces (12 slots) - Large torpedo bomber
- **A6M Zero**: 2x2 inventory spaces (4 slots) - Compact fighter

**Storage Optimization Example**:

USS Enterprise (60-slot aircraft inventory) optimally carries:
- 6 Hellcats (36 slots)
- 2 Dauntless (16 slots)
- 1 Avenger (8 slots)
- **Total**: 54/60 slots used, 6 spare slots for salvaged aircraft or replacement parts

---

### Aviation Resource Management

#### **Fuel Types & Consumption**

**Aviation Fuel Options**:
- **100-Octane Aviation Gasoline**: 2-4 fuel units per flight hour per aircraft
- **High-Performance Fuel**: 3-6 fuel units per hour, +15% aircraft performance
- **Emergency Fuel**: 1 unit per hour, -25% performance, risk of engine failure

#### **Ammunition Storage (Tetris Inventory)**

**Ordnance Inventory Items**:
- **250lb Bombs**: 1x2 slots each, general purpose munitions
- **500lb Bombs**: 2x2 slots each, heavy anti-ship ordnance
- **Aerial Torpedoes**: 2x4 slots each, devastating ship-killers
- **.50 Cal Ammunition**: 1x1 slots, bulk fighter ammunition
- **20mm Cannon Shells**: 1x2 slots, heavy fighter ammunition

#### **Maintenance Supplies**

**Essential Maintenance Items**:
- **Engine Parts**: 2x2 slots, critical for sustained operations
- **Structural Components**: 1x3 slots, airframe repairs
- **Electronics**: 1x1 slots, radio and navigation equipment
- **Hydraulic Fluid**: 1x1 slots, landing gear and flight controls

---

## Launch Preparation System - Deck Operations

### Preparation Time Factors

**Base Preparation Times** (experienced crew):
- **Fighter Wing**: 8 minutes - Simple armament, quick turnaround
- **Dive Bomber Wing**: 12 minutes - Complex bomb loading procedures
- **Torpedo Bomber Wing**: 15 minutes - Delicate torpedo installation

**Modifying Factors**:
- **Crew Stats** (Engineer Repair Speed stat 7-50): Stat 50 reduces time by ~60%, stat 7 increases by 25%
- **Aircraft Condition**: Well-maintained aircraft -20% time, damaged aircraft +100% time
- **Weather Conditions**: Rough seas +50% time, calm conditions -10% time
- **Combat Stress**: Under fire +30% preparation time

**Launch Limitation Examples**:
- **Essex-Class**: 3 wings simultaneously ready (large deck capacity)
- **Illustrious-Class**: 2 wings simultaneously ready (armored deck limits)
- **Shokaku-Class**: 4 wings simultaneously ready (efficient operations)

---

### Queue Management Scenarios

**Priority System**:
1. **Emergency CAP (Combat Air Patrol)**: Immediate launch for carrier defense
2. **Coordinated Strike**: All wings launched simultaneously for maximum impact
3. **Routine Operations**: Standard mission launches with proper sequencing
4. **Recovery Operations**: Landing aircraft always have priority over launches

#### **Example Operation: HMS Illustrious Major Strike**

HMS Illustrious prepares major strike against Italian battleship:
1. **Wing 1 (Fighters)** and **Wing 3 (Torpedo bombers)** set to "Ready" status
2. **Wing 2 (Fighter-bombers)** queued for launch after Wing 1 clears deck
3. **Wing 4** remains in reserve for carrier defense
4. **Total coordination time**: 20 minutes from decision to all wings airborne

---

## Flight Operations - Tactical Air Command

### Aircraft Control Interface - Squadron Command

#### **Wing Selection & Command**

**Control Hierarchy**:
- **Tab Cycling**: Quickly switch between active wings for rapid command changes
- **Wing Status Display**: Real-time fuel, ammunition, damage, and morale status
- **Formation Commands**: Loose formation (speed), tight formation (accuracy), combat spread
- **Altitude Control**: Low-level (stealth), medium altitude (balanced), high altitude (range)

---

### Advanced Waypoint System

**Waypoint Types**:
- **Navigation Waypoint**: Simple movement command
- **Search Pattern**: Automated reconnaissance sweeps
- **Attack Waypoint**: Designated strike coordinates with attack parameters
- **Rally Point**: Regrouping location after attack completion
- **Emergency Landing**: Alternate carrier or land base for damaged aircraft

**Attack Parameter Configuration**:
- **Approach Vector**: Direction of attack run (crucial for torpedo drops)
- **Attack Altitude**: High altitude (accuracy) vs. Low altitude (surprise)
- **Coordination Timing**: Simultaneous strikes vs. Sequential attacks
- **Escape Route**: Pre-planned withdrawal path after attack

---

### Tactical Scenarios

#### **Scenario 1: Coordinated Strike on Enemy Battleship**
**Target**: KMS Bismarck at 85km range

**Strike Coordination**:
1. **Fighter Wing**: Launched first, establishes air superiority 20km ahead of target
2. **Dive Bomber Wing**: High altitude approach from southeast, attack run from sun
3. **Torpedo Wing**: Low altitude approach from northwest, coordinated with dive bombers
4. **Timing**: Fighters engage escorts, dive bombers attack at T+0, torpedoes attack at T+30 seconds
5. **Result**: Overwhelmed defenses, multiple hits, successful extraction

---

#### **Scenario 2: Defensive Combat Air Patrol**
**Threat**: Incoming Japanese air raid detected at 40km

**Defensive Operations**:
1. **Emergency Launch**: 2 fighter wings scrambled in 6 minutes
2. **Intercept Course**: Fighters vectored to intercept 25km from carrier
3. **Engagement**: 18 Zeros vs. 16 Hellcats, numerical disadvantage but superior aircraft
4. **Defensive Success**: 12 enemy aircraft shot down, 3 friendly losses, carrier protected

---

## Communication & Range Management

### Radio Equipment Tiers

**Basic Radio Suite** (Standard Equipment):
- **Control Range**: 50km radius - adequate for local operations
- **Clarity**: Clear communication within 30km, static beyond
- **Aircraft Capacity**: Control 4 wings simultaneously

**Advanced Communication Array** (Module Upgrade):
- **Control Range**: 100km radius - extended operational reach
- **Clarity**: Clear communication throughout range
- **Aircraft Capacity**: Control 6 wings simultaneously
- **Special Features**: Automatic weather updates, enemy position reports

**Long-Range Communication System** (Rare Module):
- **Control Range**: 200km radius - strategic operations capability
- **Enhanced Features**: Coordinate with other carriers, relay intelligence
- **Aircraft Capacity**: Control 8 wings, coordinate multi-carrier operations

---

### Out-of-Range Operations

**Autonomous Behavior Programming**:
- **Last Order Continuation**: Aircraft continue last received command
- **Combat Protocols**: Engage targets of opportunity within mission parameters
- **Return Protocols**: Automatic return when fuel reaches 25% capacity
- **Emergency Procedures**: Return immediately if heavily damaged

**Strategic Risk/Reward**:

Pushing aircraft to maximum range yields better targets but risks losing valuable squadrons and experienced crew if communication is severed.

---

## Landing Operations - Deck Management Crisis

### Deck State Conflicts

**Critical Decision Points**:
- **Returning Aircraft vs. Ready Strikes**: Cancel prepared launch or force aircraft to wait?
- **Emergency Landing vs. Scheduled Recovery**: Damaged aircraft override normal procedures?
- **Fuel Crisis Management**: Multiple wings returning with low fuel simultaneously

#### **Resource Competition Example: USS Lexington**

USS Lexington has 2 wings ready to launch major strike while 3 damaged wings return with minimal fuel. Player must choose:
- **Option A**: Launch strike and risk losing returning aircraft
- **Option B**: Abort mission to save experienced crews

---

### Landing Queue Priority System

**Priority Levels**:
1. **Emergency Fuel** (<10% remaining): Immediate landing clearance
2. **Battle Damage**: Structural damage requiring immediate attention
3. **Mission Critical**: High-value intelligence or captured enemy pilot
4. **Standard Recovery**: Normal mission completion landing

#### **Fuel Management Drama**

Wing 3 (Torpedo bombers) circles carrier with 5% fuel while Wing 1 (Fighters) clears deck after emergency landing. Wing 5 (Dive bombers) also returning with 8% fuel. Player must rapidly coordinate deck operations to prevent loss of 30+ aircraft and crew.

---

## Resource Management - Operational Sustainability

### Aviation Fuel Economics

**Consumption Rates by Mission Type**:
- **Combat Air Patrol**: 2 fuel units per hour - defensive operations
- **Reconnaissance**: 3 fuel units per hour - extended search patterns
- **Strike Missions**: 4-6 fuel units per hour - high-performance combat operations
- **Extended Range**: 8+ fuel units per hour - maximum range operations

**Fuel Planning Example**:

HMS Ark Royal (500 fuel units) plans 8-hour patrol mission with 4 wings:
- **Conservative estimate**: 4 wings × 8 hours × 3 units = 96 fuel units for routine patrol
- **Combat operations**: 200+ fuel units for high-intensity operations
- **Reserve requirement**: Maintain 25% fuel reserve for emergencies

---

### Ammunition Expenditure & Resupply

**Combat Consumption Rates**:
- **Fighter Engagement**: 50-200 rounds per combat, depending on pilot skill and enemy resistance
- **Bombing Missions**: 100% ordnance expended per mission (single-use bombs/torpedoes)
- **Strafing Runs**: 100-500 rounds per attack depending on target type

**Resupply Challenges**:
- **Port-Based Resupply**: Full ammunition available at friendly major ports
- **At-Sea Resupply**: Supply ships can transfer basic ammunition only
- **Captured Munitions**: Enemy ammunition requires modification, reduced effectiveness
- **Emergency Operations**: Must return to port when ammunition depleted

---

### Maintenance & Aircraft Attrition

**Maintenance Requirements**:
- **Routine Maintenance**: 1 maintenance unit per 10 flight hours
- **Combat Damage**: 2-5 maintenance units per damaged aircraft
- **Engine Overhaul**: 10 maintenance units per 100 flight hours
- **Emergency Repairs**: Field repairs possible but reduce aircraft performance

**Aircraft Loss Factors**:
- **Combat Losses**: Shot down by enemy fighters or AA fire (permanent loss)
- **Operational Losses**: Engine failure, weather, navigation errors (10-15% of total losses)
- **Landing Accidents**: Deck crashes, especially in rough weather (aircraft repairable but crew at risk)

---

## Crew & Equipment Dependencies - Human Factors

### Crew Stats Impact on Operations (7-50 Stat System)

**Preparation Speed by Crew Stats** (Engineer Repair Speed stat 7-50):
- **Legendary Crew (Repair Speed stat 50)**: 40% of base preparation time, +105% aircraft performance
- **Expert Crew (Repair Speed stat 35)**: 60% of base preparation time, +60% aircraft performance
- **Baseline Crew (Repair Speed stat 15)**: 100% of base preparation time, standard performance
- **Rookie Crew (Repair Speed stat 7)**: 125% of base preparation time, -25% aircraft performance

**Crew Specialization Benefits**:
- **Fighter Specialists** (Fighter Pilot Dogfighting stat 7-50): +0% air-to-air at stat 15 (baseline), up to +97% at stat 50 (legendary)
- **Bomber Specialists** (Bomber Pilot Accuracy stat 7-50): +0% bombing accuracy at stat 15 (baseline), up to +97% at stat 50 (legendary)
- **All-Around Crew**: Balanced performance across all mission types (moderate stats in all classifications)

---

### Advanced Equipment Integration

**Communication Range Modules**:
- **Basic Radio**: 50km control radius, adequate for coastal operations
- **Long-Range Communications**: 100km radius, enables deep-ocean operations
- **Fleet Command Suite**: 200km radius, coordinate multiple carrier operations

#### **Strategic Equipment Example**

USS Enterprise with Long-Range Communications can coordinate with USS Hornet 150km away, launching simultaneous strikes from different vectors against Japanese fleet, overwhelming enemy defenses through superior coordination.

---

## Carrier Vulnerability & Risk Management

### Tier-Based Risk Scaling

**Carrier Value = Massive Target**:
- **T1-T4 Carriers**: Moderate threat level, full ship recovery on death
- **T5 Carriers**: High-value target, sailor casualties but 0% permadeath, last completely safe tier
- **T6-T9 Carriers**: 10-60% ship/crew card permadeath risk, hunted aggressively by players
- **T10 Carriers**: 100% PERMADEATH (ship + all crew cards), server-wide alerts when detected

**Visibility and Detection**:
- High-tier carriers attract attention across vast distances (100-200km+ detection range)
- T9-T10 carriers create server-wide awareness due to their strategic importance
- Operating high-tier carriers in any waters creates massive risk due to their visibility
- **Risk Management**: High-tier carriers always face extreme attention regardless of location

---

### High-Stakes Extraction Scenarios

**Carrier Vulnerability Phases** (applies to all tiers):
1. **Launch Phase**: Stationary target during aircraft launch operations
2. **Recovery Phase**: Predictable course and speed during landing operations
3. **Refueling Phase**: Vulnerable to submarine attack during support ship rendezvous

#### **Example Crisis: USS Wasp Under Submarine Threat**

USS Wasp launching strike against Japanese convoy when German U-boat detected at 8km range. Player must choose:
- **Option A**: Complete aircraft launch (5 minutes vulnerability)
- **Option B**: Emergency course change (aborting mission, losing prepared strike)

Torpedo track detected - 60 seconds to impact. Emergency dive course saves carrier but 2 aircraft crash during aborted landing.

---

### Multi-Domain Threat Response

**Threat Integration Management**:
- **Surface Threats**: Enemy destroyers approaching at high speed - aircraft can attack but carrier must maintain distance
- **Submarine Threats**: Underwater contacts requiring immediate course changes - disrupts flight operations
- **Air Threats**: Enemy bombers approaching - must launch fighters while protecting recovery operations

#### **Complex Tactical Scenario: HMS Illustrious Under Simultaneous Threats**

HMS Illustrious (T5 Fleet Carrier) operating 90km off Norway faces simultaneous threats:
- **German surface ships** approaching from east
- **U-boat contact** to south
- **Ju-88 bombers** inbound from north
- **2 wings returning** low on fuel

**Required Coordination**:
1. Fighters to intercept bombers
2. Course change to avoid submarine
3. Maintain sufficient distance from surface ships
4. Manage fuel crisis for returning aircraft

---

## Cross-Reference Documents

**Related Combat Systems**:
- [Combat-Overview.md](Combat-Overview.md) - Multi-domain warfare philosophy
- [Surface-Combat.md](Surface-Combat.md) - Surface ship integration
- [Submarine-Warfare.md](Submarine-Warfare.md) - Anti-submarine threats
- [Damage-Model.md](Damage-Model.md) - Aircraft damage mechanics

**Related Game Systems**:
- Ship Progression System (GDD Core)
- Module Customization System (GDD Core)
- Crew Training System (GDD Core)
- Resource Management System (GDD Core)

---

## Implementation Notes

**Phase 2 Priority Features**:
1. Wing-based aircraft management system
2. Waypoint-based aircraft control
3. Launch and recovery deck operations
4. Resource management (fuel, ammunition, maintenance)
5. Crew specialization and experience
6. Multi-domain threat integration

**Critical Success Factors**:
- Intuitive aircraft control accessible to new players
- Depth for veteran players through optimization
- Meaningful resource management creates strategic decisions
- Carrier vulnerability creates extraction tension
- Scale from T1 escort carriers to T10 supercarriers

This comprehensive carrier operations system scales from T1 escort carriers (basic air operations) through T10 apex carriers (theater-level air dominance). Success requires mastering strategic positioning, multi-domain threat management, resource logistics, crew expertise, and tactical coordination in high-stakes extraction-based gameplay.
