# Surface Ship Combat System

**Document Type**: Combat System Design
**Status**: 📋 PLANNED (Phase 2 Priority)
**Tags**: [planned, phase2, combat-systems, surface-warfare, gunnery, torpedoes]
**Priority**: HIGH
**Last Updated**: 2025-01-17

---

## Document Purpose

This document details the complete surface ship combat system for Fathoms Deep, covering advanced gunnery control, ballistics physics, torpedo mechanics, fire control systems, and tactical surface warfare scenarios.

---

## Surface Ship Tier Progression Overview

### Destroyer Line (T1-T10) - Universal Starting Path

**ALL PLAYERS START HERE** - Mandatory foundation before accessing other ship types.

#### **T1-T3 Destroyers - Learning Phase**
- **Example Ships**: USS Porter (T1), USS Mahan (T2), USS Fletcher (T3)
- **Characteristics**: Fast (30-35 knots), fragile, torpedo-focused
- **Crew**: 50-75 crew members
- **Learning Focus**: Speed management, torpedo tactics, evasion, positioning
- **Death Penalty**: 0% permadeath, full ship recovery (safe anywhere on map)
- **Typical Operations**: Safe learning waters, patrol missions, escort duty

#### **T4-T6 Destroyers - Skill Development**
- **Unlock Gates**: T4 = Cruisers/Subs unlock, T5 = Carriers/BBs unlock
- **Example Ships**: USS Gearing (T4), USS Sumner (T5), Advanced concepts (T6)
- **Characteristics**: Enhanced firepower, better survivability
- **Crew**: 75-100 crew members
- **Death Penalty**: T4-T5 = 0% permadeath (safe), T6 = 10% ship/crew card permadeath risk begins
- **Typical Operations**: Contested waters, fleet screening, convoy attacks

#### **T7-T10 Destroyers - Elite Operations**
- **Example Ships**: Post-war destroyer concepts
- **Characteristics**: Maximum speed, advanced sensors, elite firepower
- **Crew**: 100-125 crew members
- **Death Penalty**: T7=20%, T8=40%, T9=60%, T10=100% ship/crew card permadeath
- **Typical Operations**: Deep hostile territory, high-stakes fleet battles, elite reconnaissance

---

### Cruiser Line (T1-T10) - Unlocked at Destroyer T4

#### **T1-T3 Cruisers - Foundation**
- **Light Cruisers**: USS Brooklyn (T1), USS Cleveland (T2), USS Worcester (T3)
- **Heavy Cruisers**: USS Pensacola (T1), USS New Orleans (T2), USS Baltimore (T3)
- **Characteristics**: Balanced combat, versatile operations
- **Crew**: 75-150 crew members
- **Firepower**: 8-15 guns (6"-8" caliber)
- **Role**: Independent operations, convoy escort

#### **T4-T6 Cruisers - Competitive Play**
- **Example Ships**: USS Des Moines (T4), Advanced concepts (T5-T6)
- **Characteristics**: Superior firepower, good armor
- **Crew**: 150-200 crew members
- **Death Penalty**: T6 = 10% ship/crew card permadeath
- **Role**: Fleet support, surface combat dominance

#### **T7-T10 Cruisers - Ultimate Cruisers**
- **Example Ships**: Super-cruiser concepts, missile cruiser prototypes (T10)
- **Characteristics**: Maximum firepower for cruiser class
- **Crew**: 200-250 crew members
- **Death Penalty**: 40-100% permadeath (T10 = full)
- **Role**: Fleet command, multi-domain coordination

---

### Battleship Line (T1-T10) - Unlocked at Destroyer T5

#### **T1-T3 Battleships - Dreadnoughts**
- **Example Ships**: USS Wyoming (T1), USS New York (T2), USS Nevada (T3)
- **Characteristics**: Heavy armor, slow speed, devastating firepower
- **Crew**: 150-200 crew members
- **Main Armament**: 8-12 guns (12"-14" caliber)
- **Role**: Line of battle, shore bombardment

#### **T4-T6 Battleships - Fast Battleships**
- **Example Ships**: USS North Carolina (T4), USS Iowa (T5), USS Montana (T6)
- **Characteristics**: Speed + firepower, balanced design
- **Crew**: 200-250 crew members
- **Main Armament**: 9-12 guns (14"-16" caliber)
- **Death Penalty**: T6 = 10% ship/crew card permadeath
- **Role**: Fleet flagship, capital ship duels

#### **T7-T10 Battleships - Super Battleships**
- **Example Ships**: IJN Yamato equivalent (T7), Advanced designs (T8-T9), Ultimate concepts (T10)
- **Characteristics**: Maximum armor, devastating guns (18"+ caliber)
- **Crew**: 250-300+ crew members
- **Main Armament**: 9-12 guns (16"-20" caliber concepts)
- **Death Penalty**: 40-100% permadeath (T10 = full)
- **Role**: Strategic deterrence, server-defining presence

---

### Surface Ship Class Comparison

| Ship Type | Tier | Speed | Armor | Firepower | Crew | Unlock | Best For |
|-----------|------|-------|-------|-----------|------|--------|----------|
| Destroyer | T1-T10 | V.Fast | Weak | Med | 50-125 | Start | Learning, torpedoes, scouting |
| Light Cruiser | T1-T10 | Fast | Light | Med | 75-200 | DD T4 | AA escort, fast response |
| Heavy Cruiser | T1-T10 | Med | Med | High | 100-250 | DD T4 | Balanced combat, independent ops |
| Fast BB | T1-T10 | Med | Heavy | V.High | 150-250 | DD T5 | Fleet operations, prestige |
| Super BB | T7-T10 | Slow | V.Heavy | Extreme | 250-300+ | DD T5 | Strategic dominance |

---

### Tier-Based Combat Capability Scaling

**Firepower Progression**:
- **T1-T3**: Basic WWII-era gunnery
- **T4-T6**: Standard WWII peak performance (Reference tier for examples below)
- **T7-T9**: Advanced late-war and immediate post-war technology
- **T10**: Ultimate concepts, early guided munitions

**Detection & Systems**:
- **T1-T3**: Visual + basic radar
- **T4-T6**: Advanced radar, improved fire control
- **T7-T9**: Superior sensors, early electronic warfare
- **T10**: Ultimate detection, advanced countermeasures

**Resource Efficiency**:
- **T1-T3**: Cheap operations, forgiving ammunition consumption
- **T4-T6**: Moderate costs, must manage resources
- **T7-T9**: Expensive operations, every shot matters
- **T10**: Extreme costs, economic warfare becomes critical

**Note**: The following detailed mechanics (gunnery, ballistics, damage control, etc.) apply to ALL surface ship tiers, but scale in complexity, capability, and consequence as tier increases. Examples reference T4-T6 ships (mid-tier standards) unless otherwise noted.

---

## Advanced Gunnery Control System

### Multi-Battery Target Assignment Interface

#### **Gun Battery Organization**

**Battery Classification by Function**:
- **Main Battery**: Primary armament (10-16 inch guns) - maximum firepower, long reload
- **Secondary Battery**: Anti-ship weapons (4-8 inch guns) - balanced rate of fire and damage
- **Tertiary Battery**: Anti-aircraft/light ship weapons (20mm-40mm) - rapid fire, limited damage

**Individual Battery Control System**:
- **Independent Target Assignment**: Each battery section assigned separate targets simultaneously
- **Target Queue Management**: Pre-assign backup targets for automatic engagement after primary destroyed
- **Priority Override**: Emergency targets can interrupt current firing solutions
- **Range Optimization**: System suggests optimal battery for target range and type

---

### Advanced Firing Coordination Examples

#### **USS Iowa (T5 Battleship) Multi-Target Engagement**
**Target Scenario**: Japanese destroyer squadron (3 ships) advancing at 30 knots

**Firing Coordination**:
1. **Main Battery** (9x16-inch): Assigned to lead destroyer (IJN Fubuki) at 18km range
2. **Secondary Battery** (8x5-inch): Assigned to second destroyer (IJN Akatsuki) at 14km range
3. **Tertiary Battery** (20x40mm): Assigned to third destroyer (IJN Inazuma) at 8km range
4. **Firing Solution**: Staggered engagement maximizes damage while main guns reload

---

#### **HMS Hood vs KMS Bismarck Engagement** (T5 Battlecruiser vs T5 Battleship)
**Range**: 22km, closing at combined 45 knots

**Engagement Sequence**:
1. **Fire Control Calculation**: 34-second shell flight time at current range
2. **Target Prediction**: Bismarck will advance 520 meters during shell flight
3. **Aiming Point**: Player clicks 520 meters ahead of Bismarck's current position
4. **Salvo Timing**: 8x15-inch shells coordinate for simultaneous impact
5. **Result Assessment**: 3 hits, 2 penetrations, significant flooding damage

---

## Dynamic Firing Modes & Tactical Applications

### Predictive Auto-Engagement Mode

**Intelligent Fire Control System**:
- **Movement Prediction Algorithm**: System calculates target future position based on current course/speed
- **Range Finding**: Continuous range updates with lead time calculations
- **Optimal Firing Window**: Guns fire when target enters maximum damage probability zone
- **Conservation Settings**: Ammunition expenditure limits to prevent depletion

#### **Auto-Mode Tactical Scenario: USS Fletcher vs German E-boat**
**Target**: Schnellboot S-100 at 6km range, zigzagging at 35 knots

**Auto-Engagement Execution**:
1. **Fire Control Solution**: 5-inch guns auto-calculate intercept course
2. **Prediction Algorithm**: Adjusts for target's evasive maneuvers every 2 seconds
3. **Ammunition Selection**: Auto-switches to HE for maximum damage against light hull
4. **Sustained Engagement**: Maintains fire for 8 minutes, expending 147 rounds
5. **Combat Result**: Target destroyed, 23% main ammunition remaining

---

### Precision Manual Fire Control

**Coordinate-Based Targeting System**:
- **Geographic Targeting**: Click exact water coordinates for precise fire placement
- **Space Bar Volley Fire**: Coordinated firing of all selected batteries at designated point
- **Area Denial Tactics**: Saturate water areas to force enemy course changes
- **Suppressive Fire**: Prevent enemy from maintaining optimal firing positions

#### **Manual Control Tactical Scenario: KMS Scharnhorst vs HMS Renown**
**Visibility**: 8km due to fog, enemy position uncertain

**Manual Targeting Execution**:
1. **Intelligence Estimate**: Renown last detected bearing 270°, estimated range 12km
2. **Prediction Firing**: Player clicks coordinates 800m ahead of estimated position
3. **Salvo Coordination**: All 9x11-inch guns fire simultaneously via Space bar
4. **Observation**: Shell splashes reveal Renown's actual position 400m north of estimate
5. **Follow-up Salvo**: Adjusted fire achieves 2 hits, forcing Renown to turn away

---

## Advanced Target Prioritization & Threat Assessment

### Dynamic Target Value System

**Threat Assessment Matrix**:
- **Immediate Danger**: Ships currently firing at you (red priority)
- **Capability Threat**: Ships with superior firepower but not yet engaged (orange priority)
- **Opportunity Target**: Damaged ships or high-value cargo vessels (yellow priority)
- **Secondary Threat**: Support vessels and scouts (green priority)

#### **Priority Decision Example: HMS Warspite Surrounded by German Task Force**
**Contact Report**: KMS Tirpitz (battleship), 2x destroyers, 1x supply ship

**Priority Assignment**:
1. **Tirpitz**: Immediate threat (16km range) - assigned Main Battery priority
2. **Destroyer 1**: Currently firing torpedoes (8km) - assigned Secondary Battery
3. **Destroyer 2**: Approaching rapidly (12km) - assigned Tertiary Battery
4. **Supply Ship**: High loot value but no threat - queued as secondary target
5. **Tactical Decision**: Focus fire eliminates destroyers first, then battleship duel

---

## Ballistics & Advanced Combat Physics

### Realistic Shell Flight Mechanics

#### **Shell Travel Time by Range & Caliber**

**Flight Time Examples**:
- **5-inch Gun at 8km**: 12-second flight time - manageable target prediction
- **11-inch Gun at 15km**: 28-second flight time - requires accurate movement prediction
- **16-inch Gun at 25km**: 42-second flight time - extreme prediction difficulty
- **Close Range (<3km)**: Near-instantaneous impact, ideal for maneuvering battles

#### **Combat Application: USS North Carolina vs KMS Scharnhorst**
**Range**: 28km, shell flight time 48 seconds

**Extreme Range Engagement**:
1. **Target Analysis**: Scharnhorst maintaining 25 knots, steady course 090°
2. **Prediction Calculation**: Target will travel 600 meters during shell flight
3. **Environmental Factors**: 15-knot crosswind, slight sea swell affecting gunnery
4. **Firing Solution**: Aim 650 meters ahead to compensate for wind drift
5. **Combat Result**: 6 shells fired, 1 hit achieved, 17% accuracy at extreme range

---

### Advanced Armor Penetration Mechanics

#### **Penetration Physics by Impact Angle**

**Impact Angle Effects**:
- **Direct Fire (0-30° impact)**: Maximum penetration, effective against side armor
- **Oblique Impact (30-60° impact)**: Reduced penetration, chance of ricochet
- **Plunging Fire (60-90° impact)**: Maximum deck penetration, reduced side armor effectiveness
- **Ricochet Mechanics**: Shells can bounce off armor and strike secondary locations

#### **Armor Engagement Example: HMS King George V vs KMS Bismarck**
**Range**: 16km closing to 8km

**Long Range Phase** (16km):
- Plunging fire trajectory, 65° impact angle
- Shells target deck armor (300mm), penetration marginal
- 4 hits scored, minimal damage to vital areas

**Close Range Phase** (8km):
- Direct fire trajectory, 15° impact angle
- Shells target side armor (320mm), penetration excellent
- 7 hits scored, massive damage to magazines and engineering

---

## Environmental Combat Factors

### Weather Impact on Gunnery Accuracy

**Weather Condition Effects**:
- **Calm Seas**: +15% accuracy bonus, stable firing platform
- **Moderate Seas**: Standard accuracy, slight rolling affects timing
- **Rough Seas**: -25% accuracy penalty, severe gun platform movement
- **Storm Conditions**: -40% accuracy penalty, reduced visibility and stability
- **Night Combat**: -30% accuracy penalty, limited visual target identification

#### **Weather Combat Scenario: USS Massachusetts in North Atlantic Storm**
**Conditions**: 40-knot winds, 8-meter waves, visibility 2km

**Storm Combat Execution**:
1. **Target Acquisition**: German cruiser spotted at 5km range through rain squalls
2. **Gunnery Challenges**: Ship rolling 15° each direction, affecting gun laying
3. **Firing Window**: Must time salvos for when ship rolls level (3-second window)
4. **Ammunition Conservation**: Reduced accuracy requires careful shot placement
5. **Combat Result**: 45 rounds expended for 3 hits, but target forced to retreat

---

## Advanced Detection & Intelligence Systems

### Layered Detection Network

#### **Visual Detection Ranges by Ship Type**
**Clear Weather, Daylight Ranges**:
- **Battleships**: Visible 18-22km (large profile, heavy smoke)
- **Cruisers**: Visible 14-18km (moderate size, medium smoke)
- **Destroyers**: Visible 8-12km (small profile, light smoke)
- **Submarines**: Visible 2-4km when surfaced (minimal profile)
- **Aircraft**: Visible 25-35km (high contrast against sky)

---

### Advanced Radar Integration

**Radar Technology Progression**:
- **Early Radar (1940)**: 30km range, bearing only, poor resolution
- **Improved Radar (1942)**: 50km range, bearing + rough distance, weather resistant
- **Advanced Radar (1944)**: 80km range, precise positioning, target classification
- **Late-War Radar (1945)**: 120km range, multiple target tracking, fire control integration

#### **Radar Combat Application: USS Fletcher Night Engagement**
**Scenario**: Pitch black night, no visual contacts

**Radar-Directed Engagement**:
1. **Radar Contact**: 3 ships detected at 24km, bearing 045°
2. **Classification**: Advanced radar identifies 2 cruisers, 1 destroyer formation
3. **Fire Control Solution**: Radar provides continuous target updates for gunnery
4. **Tactical Advantage**: Enemy has no radar, unaware of Fletcher's presence
5. **Engagement Result**: Surprise attack achieves 8 hits before enemy can respond

---

## Intelligence Gathering & Reconnaissance

### Aircraft Spotting Integration

**Spotting Aircraft Benefits**:
- **Extended Vision**: Aircraft provide reconnaissance 50km beyond ship's visual range
- **Target Designation**: Spotted targets automatically appear in fire control system
- **Damage Assessment**: Post-engagement battle damage reports from aerial observation
- **Course Prediction**: Aircraft track enemy movement for improved firing solutions

#### **Spotting Example: HMS Rodney Engages Italian Fleet**
**Scenario**: Mediterranean, visibility 12km due to haze

**Aerial Reconnaissance Engagement**:
1. **Aircraft Launch**: Walrus seaplane launched for reconnaissance sweep
2. **Contact Report**: "3 Italian cruisers, bearing 180°, range 28km, speed 22 knots"
3. **Fire Control Update**: Target data automatically fed to gunnery computers
4. **Long-Range Engagement**: 16-inch guns engage at 26km using aircraft spotting
5. **Results**: 12 hits scored over 20 minutes, 1 cruiser sunk, 2 damaged

---

## Resource Management & Logistics

### Advanced Ammunition Management

#### **Caliber-Based Logistics System**

**Ammunition Compatibility Examples**:
- **5-inch/38 caliber**: Used by single, twin, and twin DP (dual-purpose) mounts
- **6-inch/47 caliber**: Compatible with single, twin, and triple turret configurations
- **14-inch/45 caliber**: Shared between twin and triple main battery turrets
- **Automatic Compatibility**: Game automatically supplies correct ammunition to all guns of same caliber

---

### Ammunition Type Tactical Selection

#### **Shell Type Combat Applications**

**Armor Piercing (AP) Shells**:
- **Purpose**: Maximum penetration against heavily armored targets
- **Effective Against**: Battleships, heavy cruisers, fortified positions
- **Example Usage**: HMS Hood engaging KMS Prinz Eugen - AP shells selected for penetrating 8-inch armor belt

**High Explosive (HE) Shells**:
- **Purpose**: Maximum damage against lightly armored targets and personnel
- **Effective Against**: Destroyers, aircraft, unarmored structures
- **Example Usage**: USS Fletcher vs Japanese destroyer - HE shells cause massive superstructure damage

**Anti-Aircraft (AA/Flak) Shells**:
- **Purpose**: Timed fuses create air burst patterns against aircraft
- **Effective Against**: Bombers, torpedo planes, reconnaissance aircraft
- **Example Usage**: HMS Illustrious under Stuka attack - 4.5-inch guns using time-fused AA shells

---

### Ammunition Expenditure & Conservation

**Combat Consumption Rates**:
- **Main Battery Engagement**: 8-15 rounds per minute (battleship main guns)
- **Secondary Battery Sustained Fire**: 25-40 rounds per minute per gun
- **Anti-Aircraft Defense**: 100-300 rounds per engagement per gun
- **Total Combat Load**: Typically 2-3 hours sustained combat before resupply required

#### **Conservation Tactics Example: USS South Dakota in Prolonged Engagement**
**Scenario**: 6-hour running battle with Japanese surface force

**Ammunition Management**:
1. **Initial Contact**: Full rate of fire, 120 main battery rounds expended in 45 minutes
2. **Ammunition Assessment**: 60% main battery remaining, must conserve for critical targets
3. **Tactical Adjustment**: Reduce to single gun salvos for ranging, full salvos only for assured hits
4. **Final Phase**: Last 20 main battery rounds saved for enemy battleship
5. **Outcome**: Successful extraction with enough ammunition to defeat final threat

---

## Torpedo Combat System

### Torpedo Performance Characteristics

**Torpedo Types**:
- **Standard Torpedoes**: 35-40 knots, 8km range, moderate damage
- **Long Lance (Japanese)**: 40-50 knots, 20km range, devastating damage
- **Acoustic Homing**: 25 knots, 5km range, tracks target propeller noise

**Damage Potential**:
- **Single Hit**: 15,000-40,000 HP damage (devastating to all ship types)
- **Flooding**: 100% flood chance, catastrophic damage over time
- **Module Damage**: High chance of engine/rudder destruction
- **Magazine Detonation**: 5% chance on citadel penetration

---

### Torpedo Launch Mechanics

**Launch Requirements**:
- **Speed Window**: Target must be within torpedo speed envelope
- **Range Calculation**: Account for torpedo travel time and target movement
- **Spread Pattern**: Fan spread covers target maneuvering options
- **Stealth Considerations**: Torpedo wakes visible, reveals position

#### **Torpedo Attack Example: USS Fletcher Torpedo Run**
**Target**: Japanese heavy cruiser at 8km, speed 22 knots

**Torpedo Attack Execution**:
1. **Approach**: High-speed run under smoke screen cover
2. **Launch Position**: Achieve 90° angle-on-bow for maximum hit probability
3. **Spread Pattern**: 6 torpedoes in fan spread covering 15° arc
4. **Launch Timing**: Fire at 6km range, 4-minute torpedo travel time
5. **Result**: 2 torpedo hits, cruiser crippled and flooding

---

## Tactical Combat Scenarios - Surface Warfare Mastery

### Wolf Pack Surface Engagement

#### **Formation: 3-Ship German Destroyer Squadron vs. Royal Navy Convoy**
**Ships**: KMS Z23, Z32, Z37 vs. 6 merchants + 2 escort destroyers

**Phase 1 - Approach** (Range: 15km, Night conditions):
1. **Formation Setup**: Line abreast, 2km spacing, radar silence maintained
2. **Intelligence**: Convoy detected via hydrophone, estimated speed 12 knots
3. **Tactical Plan**: Simultaneous attack from different bearings
4. **Coordination**: Hand signals only, maintain radio silence

**Phase 2 - Initial Contact** (Range: 8km):
1. **Detection**: British escorts spot German force on radar
2. **Enemy Response**: Escorts turn to intercept, merchants scatter
3. **German Reaction**: Z23 engages lead escort, Z32 and Z37 pursue merchants
4. **Weapon Selection**: HE shells for destroyers, AP for merchant engines

**Phase 3 - Running Battle** (Range: 3-12km, 45-minute engagement):
1. **Z23 vs HMS Icarus**: Close-range gun duel, both ships heavily damaged
2. **Z32 vs Merchant Fleet**: Sinks 2 cargo vessels, damages 1 tanker
3. **Z37 vs HMS Intrepid**: British destroyer forced to retreat with engine damage
4. **Casualty Report**: Z23 22% casualties, Z32 8% casualties, Z37 15% casualties

**Phase 4 - Extraction Decision**:
1. **Mission Assessment**: 3 merchants sunk, 2 escorts damaged, primary objective achieved
2. **Damage Evaluation**: Z23 speed reduced to 24 knots, limiting formation speed
3. **Tactical Situation**: Royal Navy reinforcements 45 minutes away
4. **Command Decision**: Withdraw immediately vs. pursue remaining merchants
5. **Risk Factors**: Dawn approaching, air cover for convoy possible

---

### Capital Ship Duel - Battleship vs Battlecruiser

#### **Engagement: USS Iowa vs IJN Kongo in Guadalcanal Waters**
**Range**: Starting at 22km, closing to 8km over 90 minutes

**Opening Phase** (Range: 22km, Visibility: 15km):
1. **Detection**: Both ships spotted simultaneously by aircraft
2. **Fire Control**: Advanced radar vs. optical rangefinding
3. **Initial Salvos**: 9x16-inch vs 8x14-inch, 35-second flight times
4. **Gunnery Results**: Iowa 2 hits from 12 shots, Kongo 0 hits from 10 shots

**Mid-Range Phase** (Range: 15km, Closing at combined 35 knots):
1. **Tactical Maneuvering**: Iowa maintains range advantage, Kongo closes for torpedo attack
2. **Hit Exchange**: Iowa achieves 6 hits, Kongo achieves 3 hits
3. **Damage Assessment**:
   - Iowa: Minor deck damage, 1 secondary turret disabled
   - Kongo: Major flooding, speed reduced to 22 knots, 1 main turret destroyed
4. **Tactical Shift**: Kongo attempts to break off, Iowa pursues

**Close-Range Phase** (Range: 8km, Kongo attempting withdrawal):
1. **Gunnery Advantage**: Reduced flight time increases hit probability
2. **Penetration Success**: Iowa's heavier shells penetrate Kongo's armor effectively
3. **Critical Hits**:
   - Iowa: Destroys Kongo's forward magazine, massive explosion
   - Kongo: Achieves engine room hit on Iowa, speed reduced to 20 knots
4. **Final Phase**: Kongo's crew abandons ship, Iowa rescues survivors

**Strategic Implications**:
- **Experience Gained**: Iowa's crew gains elite status from successful engagement
- **Resource Cost**: Iowa expends 60% main battery ammunition
- **Extraction Success**: Iowa safely returns to base despite damage
- **Intelligence Value**: Captured Japanese naval codes provide strategic advantage

---

## Damage Control Operations

### Progressive Damage System

**Module Degradation Levels**:

**Turret Damage Progression**:
1. **Fully Operational** (100%): Maximum rate of fire, full accuracy
2. **Light Damage** (75%): Reduced rate of fire, slight accuracy penalty
3. **Moderate Damage** (50%): Significant rate reduction, notable accuracy loss
4. **Heavy Damage** (25%): Single gun operation only, poor accuracy
5. **Destroyed** (0%): Turret completely non-functional, requires major repair

---

### Critical Damage Control Scenarios

#### **Engineering Spaces Damage**

**System Failures**:
- **Engine Room Flooding**: Speed reduction, eventual dead in water
- **Boiler Damage**: Power loss affects turret traverse and fire control systems
- **Fuel System Hits**: Fire danger, reduced operational range
- **Steering Damage**: Ship becomes difficult or impossible to maneuver

#### **Emergency Damage Control: HMS Prince of Wales Under Air Attack**
**Situation**: Multiple torpedo hits, severe flooding, list developing

**Damage Control Response**:
1. **Immediate Assessment**: Damage Control UI shows 3 compartments flooded
2. **Priority Repair**: Counter-flooding ordered to correct 12° list
3. **System Evaluation**: Port engine destroyed, starboard engine operational at 60%
4. **Speed Reduction**: Maximum speed reduced from 29 to 18 knots
5. **Combat Effectiveness**: Can still fight but must avoid close-range engagement
6. **Extraction Decision**: Withdraw to port or continue mission with reduced capability?

---

## Crew Management Under Fire

### Personnel Casualty System

**Crew Status Categories**:
- **Combat Ready**: Full effectiveness, no penalties
- **Light Casualties**: 10-15% effectiveness reduction, manageable losses
- **Heavy Casualties**: 25-40% effectiveness reduction, significant impact on operations
- **Critical Casualties**: 50%+ effectiveness reduction, major operational limitations

#### **Crew Reassignment: USS Atlanta After Air Attack**
**Casualties**: 40% crew casualties, 6 gun mounts damaged

**Crew Management Response**:
1. **Damage Assessment**: 8x5-inch guns operational, 4x5-inch guns destroyed
2. **Crew Reallocation**: Survivors from destroyed mounts assigned to remaining guns
3. **Effectiveness Impact**: Remaining guns operate at 85% efficiency due to mixed crews
4. **Repair Priority**: Engineering crew assigned to restore power before gun repairs
5. **Combat Capability**: Ship retains 60% of original firepower with reduced accuracy

---

## Advanced Tactical Considerations

### Range Management

**Engagement Range Optimization**:
- **Long Range (>20km)**: Battleship advantage, plunging fire
- **Medium Range (10-20km)**: Balanced engagements, all ship types effective
- **Short Range (<10km)**: Destroyer advantage, torpedo threat maximum
- **Knife Fight (<5km)**: High-risk, high-reward, rapid fire advantage

---

### Formation Tactics

**Line Ahead**:
- Maximum forward firepower concentration
- Vulnerable to flanking maneuvers
- Best for pursuit or retreat

**Line Abreast**:
- Maximum broadside firepower
- Good for sweeping formations
- Vulnerable to concentrated fire

**Echelon Formation**:
- Balanced offense and defense
- Flexible positioning
- Allows rapid formation changes

---

## Cross-Reference Documents

**Related Combat Systems**:
- [Combat-Overview.md](Combat-Overview.md) - Multi-domain warfare philosophy
- [Carrier-Operations.md](Carrier-Operations.md) - Air power integration
- [Submarine-Warfare.md](Submarine-Warfare.md) - Anti-submarine warfare
- [Damage-Model.md](Damage-Model.md) - Detailed damage mechanics

**Related Game Systems**:
- Ship Progression System (GDD Core)
- Module Customization System (GDD Core)
- Crew Training System (GDD Core)
- Resource Management System (GDD Core)

---

## Implementation Notes

**Phase 2 Priority Features**:
1. Multi-battery target assignment system
2. Realistic ballistics with shell travel time
3. Armor penetration mechanics
4. Weather effects on gunnery
5. Damage control and crew management
6. Torpedo launch and tracking systems

**Critical Success Factors**:
- Accessible auto-targeting for new players
- Skill-based manual targeting rewards
- Tactical depth through positioning and timing
- Resource management creates strategic decisions
- Extraction tension drives all combat choices
