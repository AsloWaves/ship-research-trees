# Technology Integration

**Status**: 📋 PLANNED (Phase 2/3 feature)
**Tags**: [planned, phase2, ship-customization, technology, ui-transformation]
**Priority**: HIGH (defines ship capabilities)
**Related Systems**: [Utility Modules](Utility-Modules.md), [Module System](Module-System.md), [Combat System](../02-Core-Systems/Combat-System.md)

---

## Overview

Technology Integration describes how installing specific modules fundamentally transforms ship capabilities and UI functionality. Unlike simple stat bonuses, technology modules unlock entirely new gameplay features, visual elements, and tactical options.

**Core Principle:**
Technology progression spans **1936-2025**, mirroring real naval evolution from WWII through modern era. Ships without radar operate blind beyond visual range, fire control computers dramatically improve accuracy, and electronic warfare creates entirely new tactical dimensions.

---

## Technology Tiers & Eras

### Pre-Radar Era (T1-T3)

**Available Technologies:**
- Optical Rangefinders
- Basic Fire Control (mechanical)
- Visual spotting only
- Manual gunnery calculations

**Gameplay Characteristics:**
- Limited detection range (visual horizon: 15-20km)
- Manual target leading required
- No IFF (Identify Friend/Foe)
- Heavy reliance on player skill

---

### Early Radar Era (T4-T5)

**New Technologies:**
- Basic Radar (30-50km range)
- Mechanical Fire Control Computers
- Passive Sonar (submarines/destroyers)
- Basic Communications

**Gameplay Transformation:**
- Radar contact beyond visual range
- Semi-automated fire solutions
- Submarine detection capability
- Coordinated fleet operations

---

### Advanced Radar Era (T6-T7)

**New Technologies:**
- Advanced Radar (80km range)
- Electronic Analog Fire Control
- Active Sonar
- Radar Jamming
- SIGINT (Signal Intelligence)

**Gameplay Transformation:**
- Multi-target tracking
- Electronic warfare begins
- Long-range fire control
- Intelligence gathering capabilities

---

### Late-War/Modern Era (T8-T10)

**New Technologies:**
- Experimental AEGIS (150km range)
- AI-Assisted Fire Control
- Advanced Sonar with torpedo tracking
- CIWS (Close-In Weapon System)
- Comprehensive EW (Electronic Warfare)

**Gameplay Transformation:**
- Full situational awareness
- 12-target simultaneous engagement
- Missile defense (if applicable)
- Complete electronic warfare suite

---

## Radar Technology Integration

### No Radar Installed

**Ship Capabilities:**
- **Detection Range**: Visual horizon only (15-20km depending on weather)
- **Tactical Map**: Shows only visually spotted enemies
- **Target Tracking**: Manual visual tracking
- **IFF**: None (must identify targets visually)
- **Fire Control**: Manual lead calculations only

**UI Elements:**
- Tactical map shows fog of war beyond visual range
- No target tracking brackets
- No range/bearing data on unspotted targets
- Minimap limited to 20km radius

**Strategic Implications:**
- Extreme vulnerability to radar-equipped enemies
- Ambush tactics viable (can't be detected at range)
- Lower tier combat (T1-T3) balanced around no radar

---

### Basic Radar (30km)

**Module**: Basic Radar System (1x1, 8 tons, ₡150,000)

**Ship Capabilities:**
- **Detection Range**: 30km sphere around ship
- **Tactical Map**: Shows radar contacts as red dots
- **Target Tracking**: Basic position updates (5-second refresh)
- **IFF**: None (all contacts appear hostile)
- **Fire Control**: Radar data feeds into manual calculations

**UI Elements:**
- Tactical map extends to 30km
- Radar contacts appear as simple red dots
- Range/bearing data displayed
- Radar overlay on minimap (green circle showing coverage)

**Strategic Implications:**
- First detection range advantage
- Can spot enemies before they spot you (if they lack radar)
- Limited info (no IFF, slow refresh rate)

---

### Improved Radar (50km)

**Module**: Improved Radar System (1x2, 15 tons, ₡450,000)

**Ship Capabilities:**
- **Detection Range**: 50km sphere
- **Tactical Map**: Radar contacts with basic ship class identification
- **Target Tracking**: Improved updates (2-second refresh)
- **IFF**: Basic friend/foe distinction
- **Fire Control**: Radar feeds into fire control computer

**UI Elements:**
- Tactical map extends to 50km
- Radar contacts show ship type icons (DD, CL, BB, etc.)
- IFF markers (green = ally, red = enemy, yellow = unknown)
- Improved radar overlay with coverage ring

**Strategic Implications:**
- Significant detection advantage
- Can identify ship classes at range
- Better situational awareness for fleet coordination

---

### Advanced Radar (80km)

**Module**: Advanced Radar System (2x2, 28 tons, ₡1,200,000)

**Ship Capabilities:**
- **Detection Range**: 80km sphere
- **Tactical Map**: Full target info (class, heading, speed estimate)
- **Target Tracking**: Real-time updates (1-second refresh)
- **IFF**: Full friend/foe with faction identification
- **Fire Control**: Integrated multi-target tracking (4 targets)
- **Multi-Target Engagement**: Can engage 4 targets simultaneously

**UI Elements:**
- Tactical map extends to 80km
- Radar contacts show detailed info tooltips
- Target vector indicators (heading/speed arrows)
- Multi-target selection brackets
- Fire control integration overlay

**Strategic Implications:**
- Dominant detection capability
- Can track and engage multiple targets
- Essential for high-tier fleet combat
- Counter: Radar jamming becomes viable

---

### Late-War Integrated Radar (120km)

**Module**: Late-War Integrated Radar (2x3, 40 tons, ₡3,500,000)

**Ship Capabilities:**
- **Detection Range**: 120km sphere
- **Tactical Map**: Full situational awareness
- **Target Tracking**: Real-time with prediction (0.5-second refresh)
- **IFF**: Complete identification with player names
- **Fire Control**: Integrated 8-target tracking
- **Air Defense Coordination**: Coordinates AA defenses automatically
- **Surface Search**: Distinguishes surface vs. air contacts

**UI Elements:**
- Tactical map extends to 120km
- Predicted target paths shown as dotted lines
- Air contacts shown separately from surface
- AA defense zone indicators
- Fleet coordination data sharing

**Strategic Implications:**
- Near-complete battlefield awareness
- Can coordinate fleet air defense
- Essential for carrier operations
- Vulnerable to advanced EW (jamming)

---

### Experimental AEGIS (150km)

**Module**: Experimental AEGIS System (3x3, 50 tons, ₡8,000,000)

**Ship Capabilities:**
- **Detection Range**: 150km sphere (maximum possible)
- **Tactical Map**: Complete omniscience within range
- **Target Tracking**: Real-time with AI prediction
- **IFF**: Full identification with threat assessment
- **Fire Control**: 12-target simultaneous engagement
- **Multi-Role**: Surface, air, and submarine detection
- **Threat Assessment**: AI prioritizes targets by danger level
- **Electronic Warfare**: Integrated counter-jamming

**UI Elements:**
- Tactical map extends to 150km
- AI threat assessment overlays (priority targets highlighted)
- Integrated fire control solutions displayed
- Multi-role contact classification (surface/air/sub)
- Counter-jamming indicators
- Fleet data-link sharing

**Strategic Implications:**
- Ultimate situational awareness
- Can engage entire enemy fleets simultaneously
- Essential for T10 permadeath zones
- Extremely expensive and heavy (weight penalty)
- Prime target for enemy EW attacks

---

## Fire Control Technology Integration

### No Fire Control System

**Ship Capabilities:**
- **Manual Aiming**: Player must manually lead targets
- **No Accuracy Bonus**: Base accuracy only (50-60%)
- **Single Target**: Focus on one target at a time
- **Visual Aids**: Basic reticle only

**UI Elements:**
- Simple aiming reticle
- No lead indicators
- No hit probability display
- Manual range estimation

**Strategic Implications:**
- High skill ceiling (expert players can outperform AI)
- Vulnerable to automated systems
- Cost-effective for skilled players

---

### Basic Optical Rangefinder (+5% Accuracy)

**Module**: Optical Rangefinder (1x1, 6 tons, ₡80,000)

**Ship Capabilities:**
- **Accuracy Bonus**: +5% hit chance
- **Range Estimation**: Automatic range calculation
- **Lead Indicator**: Basic lead marker (requires manual adjustment)
- **Weather Resistant**: Works when radar damaged/jammed

**UI Elements:**
- Range display to target
- Basic lead indicator circle
- Hit probability percentage

**Strategic Implications:**
- Simple accuracy improvement
- Immune to electronic warfare
- Backup system if radar fails
- Stacks with electronic fire control

---

### Mechanical Fire Control Computer (+15% Accuracy)

**Module**: Mechanical Fire Control (1x2, 12 tons, ₡350,000)

**Ship Capabilities:**
- **Accuracy Bonus**: +15% hit chance
- **Automated Lead**: Computer calculates lead automatically
- **2-Target Tracking**: Can track 2 targets with switch delay
- **Ballistic Calculations**: Accounts for shell drop and wind

**UI Elements:**
- Automated lead indicator (dynamic adjustment)
- Hit probability for current target
- Target switch button (5-second recalculation delay)
- Wind/weather impact display

**Strategic Implications:**
- Significant accuracy improvement
- Reduces player skill requirement
- Still vulnerable to jamming
- Essential for mid-tier combat

---

### Electronic Analog Fire Control (+30% Accuracy)

**Module**: Electronic Analog Fire Control (2x2, 25 tons, ₡1,500,000)

**Ship Capabilities:**
- **Accuracy Bonus**: +30% hit chance
- **Radar Integration**: Uses radar data for perfect range/bearing
- **4-Target Tracking**: Simultaneous tracking with instant switching
- **Predictive Aiming**: Accounts for target acceleration/turning
- **Salvo Optimization**: Calculates optimal salvo timing

**UI Elements:**
- Multi-target tracking brackets (4 targets)
- Predicted target paths shown
- Salvo timer indicator (optimal firing window)
- Fire solution quality meter (green = optimal, red = poor)

**Strategic Implications:**
- Dramatic accuracy improvement
- Essential for competitive play
- Requires radar for full effectiveness
- Vulnerable to radar jamming

---

### Digital Fire Control (+50% Accuracy)

**Module**: Digital Fire Control (2x3, 38 tons, ₡4,500,000)

**Ship Capabilities:**
- **Accuracy Bonus**: +50% hit chance
- **Full Radar Integration**: Perfect tracking integration
- **8-Target Tracking**: Engage up to 8 targets with priority queue
- **AI Prediction**: Predicts target maneuvers (evasive action detection)
- **Optimal Firing Solutions**: Computer calculates perfect firing windows
- **Automatic Turret Assignment**: AI assigns turrets to priority targets

**UI Elements:**
- 8-target tracking with priority indicators
- AI-predicted maneuver paths (dotted yellow lines)
- Optimal firing window indicators (green bars)
- Automatic turret assignment display
- Fire solution quality for all tracked targets

**Strategic Implications:**
- Near-perfect accuracy (player skill less important)
- Can engage entire enemy formations
- Essential for T8+ combat
- Extremely vulnerable to electronic warfare
- High cost/weight trade-off

---

### AI-Assisted Fire Control (+75% Accuracy)

**Module**: AI-Assisted Fire Control (3x3, 50 tons, ₡10,000,000)

**Ship Capabilities:**
- **Accuracy Bonus**: +75% hit chance (near-maximum)
- **AEGIS Integration**: Full sensor fusion with AEGIS radar
- **12-Target Tracking**: Maximum simultaneous engagement
- **Full AI Automation**: Can engage targets with minimal player input
- **Threat Assessment**: AI prioritizes targets by danger level
- **Evasion Detection**: Predicts enemy maneuvers with 80% accuracy
- **Counter-Battery**: Automatically returns fire when fired upon

**UI Elements:**
- 12-target tracking with AI threat assessment
- Full automation toggle (AI engages automatically)
- Threat priority indicators (1-12 ranking)
- Predicted impact points for all salvos
- Counter-battery indicators
- Fire mission queue (AI manages firing sequence)

**Strategic Implications:**
- Ultimate fire control capability
- Reduces player workload dramatically (focus on tactics)
- Essential for T10 permadeath survival
- Extremely expensive (₡10M + weight penalty)
- Prime target for enemy electronic warfare

---

## Electronic Warfare Integration

### No EW Systems

**Ship Status:**
- **Fully Visible**: Detectable by all enemy sensors at maximum range
- **No Countermeasures**: Vulnerable to all guided weapons
- **No Intelligence**: Cannot detect enemy electronic emissions

**Strategic Implications:**
- Sitting duck for radar-equipped enemies
- No defensive options against missiles/guided torpedoes
- Standard for low-tier combat (T1-T3)

---

### Radar Jammer (Basic)

**Module**: Basic Radar Jammer (1x1, 12 tons, ₡400,000)

**Effects:**
- **Enemy Detection Range**: Reduced by 20%
- **Fire Control Interference**: -10% enemy accuracy
- **Side Effect**: Broadcasts jamming signal (reveals general direction)

**UI Integration:**
- Toggle button on main UI
- Jamming status indicator (green = active, gray = inactive)
- Enemy fire control disruption indicator

**Strategic Implications:**
- First electronic warfare capability
- Trade-off: Harder to detect precisely, but enemies know you're there
- Effective against AI, less effective against skilled players
- Reveals your presence (can't ambush while jamming)

---

### Radar Jammer (Advanced)

**Module**: Advanced Radar Jammer (1x2, 22 tons, ₡1,200,000)

**Effects:**
- **Enemy Detection Range**: Reduced by 50%
- **Fire Control Interference**: -25% enemy accuracy
- **Multi-Band Jamming**: Affects multiple radar frequencies
- **Side Effect**: Still broadcasts jamming signal

**UI Integration:**
- Advanced jamming control panel
- Multi-band frequency selection
- Enemy radar types detected and jammed indicator

**Strategic Implications:**
- Significant detection reduction
- Severe enemy accuracy penalty
- Can selectively jam specific radar types
- Essential for extraction escapes

---

### Signal Intelligence (SIGINT) Module

**Module**: SIGINT Module (1x2, 15 tons, ₡800,000)

**Effects:**
- **Radio Intercept**: Intercepts enemy communications
- **Triangulation**: Detects enemy positions via radio emissions (±5km accuracy)
- **Early Warning**: Detects enemy fleet movements 50km out
- **Message Decoding**: Can decode encrypted messages (30-60 sec delay)

**UI Integration:**
- SIGINT panel showing intercepted messages
- Enemy position triangulation markers (approximate)
- Fleet movement indicators
- Communication intercept log

**Strategic Implications:**
- High-level intelligence tool
- Reveals enemy chat messages in range
- Critical for organized fleet play
- Passive (no emissions, undetectable)

---

### Decoy Transmitter

**Module**: Decoy Transmitter (1x1, 8 tons, ₡300,000)

**Effects:**
- **False Radar Signature**: Appears as different ship class
- **5 Charges**: Limited use, refillable
- **Duration**: 5 minutes per charge
- **Effectiveness**: High vs. AI, moderate vs. players

**UI Integration:**
- Decoy activation button
- Current decoy signature display (showing as what ship class)
- Charges remaining indicator
- Duration timer

**Strategic Implications:**
- Psychological warfare tool
- Make destroyer appear as battleship (intimidation)
- Make battleship appear as cruiser (ambush)
- Experienced players detect via speed/maneuver analysis

---

## Sonar & Submarine Detection Integration

### No Sonar

**Ship Capabilities:**
- **Submarine Detection**: None (blind to submarines)
- **Torpedo Warning**: None (torpedoes appear when close)
- **Underwater Contacts**: Invisible

**Strategic Implications:**
- Completely vulnerable to submarine attacks
- Must rely on visual spotting (periscope sightings)
- Standard for non-ASW ships

---

### Passive Sonar

**Module**: Passive Sonar (1x1, 10 tons, ₡200,000)

**Ship Capabilities:**
- **Detection Range**: 5-15km (engine noise dependent)
- **Detection Type**: Passive acoustic listening
- **Stealthy**: Does not reveal ship position
- **Limitations**: Cannot detect stationary submarines

**UI Integration:**
- Sonar display showing acoustic contacts
- Bearing-only indicators (no precise position)
- Engine noise intensity meter
- Submarine contact icons (red submarine symbol)

**Strategic Implications:**
- First submarine detection capability
- Silent operation (doesn't alert submarines)
- Limited range and accuracy
- Essential for destroyers in ASW role

---

### Active Sonar

**Module**: Active Sonar (1x2, 18 tons, ₡450,000)

**Ship Capabilities:**
- **Detection Range**: 15-30km (active ping)
- **Detection Type**: Active acoustic emission
- **Precise Location**: Reveals exact submarine position
- **Side Effect**: Reveals ship position to all submarines in range

**UI Integration:**
- Active ping button
- Sonar display with precise submarine positions
- Ping cooldown timer (30 seconds)
- Warning: "Active ping will reveal your position"

**Strategic Implications:**
- High-range submarine detection
- Trade-off: Reveals your position when pinging
- Tactical decision: When to go active vs. passive
- Essential for submarine hunting

---

### Advanced Sonar

**Module**: Advanced Sonar (2x2, 28 tons, ₡1,500,000)

**Ship Capabilities:**
- **Detection Range**: 30km (active), 20km (passive)
- **Depth Detection**: Shows submarine depth
- **Torpedo Tracking**: Tracks incoming torpedoes (10-20 sec warning)
- **Multi-Contact**: Tracks up to 8 submarines simultaneously
- **Passive Mode**: Enhanced passive detection (less reliant on active pinging)

**UI Integration:**
- Advanced sonar display with 3D depth visualization
- Torpedo warning indicators (incoming threat alerts)
- Multi-contact tracking brackets
- Depth gauge for each submarine contact

**Strategic Implications:**
- Ultimate ASW capability
- Torpedo warning allows evasive maneuvers
- Can track multiple submarine threats
- Essential for high-tier anti-submarine warfare

---

## Special System Integration

### Aircraft Catapult System

**Requirements:**
- Aircraft Catapult hardpoint on ship
- Aircraft Catapult Control module (1x1, 8 tons, ₡350,000)
- Aviation crew card assigned

**Ship Capabilities:**
- **Scout Plane Launch**: Deploy reconnaissance aircraft
- **Flight Duration**: 10-20 minutes (returns automatically)
- **Reconnaissance Range**: +20km detection radius from aircraft position
- **Over-Horizon Spotting**: Provides targeting data for long-range fire

**UI Integration:**
- Aircraft launch button
- Aircraft position on tactical map (blue plane icon)
- Flight time remaining indicator
- Reconnaissance data overlay (extended radar coverage)
- Spotting bonus indicator for fire control

**Strategic Implications:**
- Extends detection range dramatically
- Essential for battleship long-range gunnery
- Vulnerable to enemy fighters (if carrier operations implemented)
- Tactical reconnaissance capability

---

### Mining Equipment System

**Module**: Mining Equipment (2x2 Basic, 2x3 Advanced)

**Ship Capabilities:**
- **Mine Deployment**: Lay naval mines in water
- **Mine Types**: Contact (basic), Magnetic, Acoustic (advanced)
- **Mine Capacity**: 5 mines (basic), 20 mines (advanced)
- **Persistence**: Mines remain 24 hours real-time

**UI Integration:**
- Mine deployment interface
- Mine type selection (contact/magnetic/acoustic)
- Mines remaining indicator
- Mine field markers on tactical map (friendly mines only)
- Warning indicators when entering mined areas

**Strategic Implications:**
- Area denial capability
- Defensive operations (protect extraction zones)
- Trap setting (ambush chokepoints)
- Psychological warfare (enemies must navigate cautiously)

---

### Salvage Equipment System

**Module**: Salvage Equipment (2x3 Basic, 3x3 Advanced)

**Ship Capabilities:**
- **Wreck Salvage**: Loot modules from destroyed ships
- **Salvage Speed**: 100% (basic), 200% (advanced)
- **Module Quality**: Common/Uncommon (basic), Rare/Exceptional (advanced)
- **Range**: Must be within 200m of wreck

**UI Integration:**
- Salvage interface (shows wreck contents)
- Salvage progress bar
- Module quality indicators
- Salvage speed multiplier display
- Wreck location indicators on tactical map

**Strategic Implications:**
- Core extraction gameplay mechanic
- Dedicated salvage ships maximize loot
- Advanced equipment = better loot quality
- Risk/reward: Time spent salvaging = vulnerability

---

## Technology Progression Paths

### Early-Game Technology Path (T1-T3)

**Recommended Module Sequence:**
1. Optical Rangefinder (₡80K) - Immediate accuracy boost
2. Basic Radar (₡150K) - First detection range advantage
3. Mechanical Fire Control (₡350K) - Significant accuracy improvement
4. Damage Control Station Basic (₡120K) - Combat survivability

**Total Investment**: ~₡700K
**Gameplay Transformation**: From manual play to semi-automated systems

---

### Mid-Game Technology Path (T4-T6)

**Recommended Module Sequence:**
1. Improved Radar (₡450K) - Extended detection + IFF
2. Electronic Analog Fire Control (₡1.5M) - Multi-target capability
3. Advanced Sonar (₡1.5M) - ASW capability (if destroyer/ASW role)
4. Basic Radar Jammer (₡400K) - First EW capability
5. Auxiliary Generator Large (₡250K) - System redundancy

**Total Investment**: ~₡4.1M
**Gameplay Transformation**: From basic combat to multi-target engagements + EW

---

### Late-Game Technology Path (T7-T9)

**Recommended Module Sequence:**
1. Advanced Radar (₡1.2M) - 80km detection + 4-target tracking
2. Digital Fire Control (₡4.5M) - 8-target engagement
3. Advanced Sonar (₡1.5M) - Full ASW + torpedo warning
4. Advanced Radar Jammer (₡1.2M) - Serious EW capability
5. SIGINT Module (₡800K) - Intelligence gathering
6. CIWS Basic (₡600K) - Missile/aircraft defense

**Total Investment**: ~₡9.8M
**Gameplay Transformation**: Near-complete battlefield control

---

### End-Game Technology Path (T10+)

**Recommended Module Sequence:**
1. Experimental AEGIS (₡8M) - Maximum detection + 12-target tracking
2. AI-Assisted Fire Control (₡10M) - Ultimate accuracy + automation
3. Advanced Sonar (₡1.5M) - If not already equipped
4. Advanced Radar Jammer (₡1.2M) - If not already equipped
5. CIWS Advanced (₡1.2M) - Maximum point defense
6. Torpedo Defense Active (₡800K) - Counter-torpedo capability

**Total Investment**: ~₡22.7M
**Gameplay Transformation**: Complete technological superiority

---

## Technology Counter-Play

### Countering Radar Advantage

**Without Radar:**
- Use terrain (islands, fog) to close range undetected
- Ambush tactics at visual range
- Speed and agility to evade detection

**With Radar Jammer:**
- Reduce enemy detection range
- Interfere with fire control accuracy
- Trade-off: Reveals your presence via jamming signal

**With Decoy Transmitter:**
- Appear as different ship class
- Psychological intimidation or deception
- Limited duration (5 min per charge)

---

### Countering Fire Control Advantage

**Manual Evasion:**
- Unpredictable maneuvering defeats predictive fire control
- Skilled players can dodge AI-predicted shots
- High speed and agility essential

**Radar Jamming:**
- Disrupts fire control computer data feed
- Reduces enemy accuracy significantly
- Forces enemy to manual targeting

**Smoke Screens:**
- Breaks line of sight (fire control requires vision)
- Temporary escape option
- Repositioning opportunity

---

### Countering Electronic Warfare

**Optical Systems:**
- Optical Rangefinder immune to jamming
- Visual spotting bypasses radar jamming
- Backup systems critical for high-tier combat

**Multiple Sensors:**
- Redundant radar systems
- Sonar as backup for radar jamming
- SIGINT to detect enemy positions via radio

**Counter-EW Technology:**
- AEGIS has integrated counter-jamming
- Advanced systems resist jamming effects
- Technology arms race

---

## Summary & Integration

**Complete Technology Integration System Includes:**

✅ **Radar Technology**: 5 tiers (None → AEGIS) fundamentally transforming detection
✅ **Fire Control Technology**: 6 tiers (Manual → AI-Assisted) dramatically improving accuracy
✅ **Electronic Warfare**: Jamming, SIGINT, decoys creating tactical depth
✅ **Sonar Technology**: Passive, Active, Advanced enabling ASW operations
✅ **Special Systems**: Aircraft catapults, mining, salvage expanding gameplay roles
✅ **UI Transformation**: Each technology tier adds new UI elements and capabilities
✅ **Counter-Play Mechanics**: Technology advantages can be countered with skill/tactics

**Integration Points:**
- Utility Modules: Defines available technology modules
- Module System: Technology modules fit within Misc slot constraints
- Combat System: Technology directly impacts combat effectiveness
- Ship Fitting UI: Technology modules visible in fitting interface
- Economy System: Technology progression drives major credit expenditure

**Progression Philosophy:**
Technology modules create clear power progression while maintaining counterplay opportunities through skill, tactics, and opposing technologies.

---

**End of Technology Integration Specification**
