---
tags: [planned, phase2, world-design, zones]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-17
---

# Zone System

## Overview
The Zone System divides the game world into six distinct tier levels (T0-T5) that create a risk/reward progression framework for ship tiers T1-T10. This system is the backbone of the game's PvP, resource distribution, and territorial control mechanics, ensuring that player progression naturally guides them from safe waters to increasingly dangerous zones as they acquire more powerful ships.

**Core Philosophy**: Higher tier ships face exponentially greater danger even in lower tier zones due to their value, insurance costs, and attractiveness as targets.

## Implementation Status
**Status**: 📋 PLANNED
**Phase**: Phase 2 (Economy & Progression)
**Dependencies**: [[Ocean-Environment]], [[Ship-Progression-System]], [[Economy-System]]
**Priority**: HIGH - Foundation for risk/reward gameplay

---

## Design Specification

### Zone vs Ship Tier Relationship

**Critical Distinction**: Zone tiers (T0-T5) are **separate** from ship tiers (T1-T10).

- **Zone Tiers**: Define environmental danger level, NPC presence, and territorial control
- **Ship Tiers**: Define ship power, value, insurance cost, and target attractiveness
- **Relationship**: Higher tier ships face MORE danger in ANY zone due to their value

**Example**: A T10 battleship in a T1 zone is still a massive target worth hunting, even though the zone is "protected."

---

## Zone Classification System

### Tier 0 - Core National Waters (SAFEST)

**Purpose**: New player sanctuary and safe haven for all nations

#### Characteristics
- **Ship Access**: Optimal for T1-T4 ships, T5-T10 allowed but overkill
- **Protection Level**: MAXIMUM - Overwhelming NPC fleet presence
- **Enemy Presence**: Enemy players face instant destruction from NPC forces
- **Death Penalty**: None for T1-T4 ships in home nation waters
- **PvP Status**: Completely disabled, safe zones enforced

#### Locations
- **USA**: Pearl Harbor inner harbor, San Diego Naval Base, New York Harbor
- **UK**: Scapa Flow anchorage, Portsmouth Naval Base, Plymouth Sound
- **Japan**: Tokyo Bay inner waters, Yokosuka Naval Base, Kure Harbor
- **Germany**: Kiel Canal, Wilhelmshaven Base, Hamburg inner port

#### Facilities & Services
- **Repair Facilities**: Advanced repair yards, instant damage restoration
- **Supply Access**: Full access to all T1-T5 resources and equipment
- **Economic Benefits**: Lowest market prices (20% below standard)
- **Training Programs**: New player tutorials, gunnery ranges, navigation courses
- **Drydock Services**: Ship customization, module installation, crew training

#### Resources Available
- **Resource Tiers**: Common materials only (steel, oil, basic ammunition)
- **Purpose**: Sufficient for T1-T5 ship construction and progression
- **Extraction**: No extraction required, direct purchase from NPC vendors
- **Respawn Rate**: Unlimited supply, never depleted

#### Perfect For
- **New Players**: Learning game mechanics without risk
- **Ship Testing**: Testing new builds and loadouts safely
- **Crew Training**: Training new crew members to higher skill levels
- **Safe Gathering**: Low-tier resource farming for beginners
- **Social Hub**: Player meetup points, guild recruitment, trading

#### Strategic Value
- **Territory Control**: 100% faction control, unchangeable
- **Spawn Points**: Primary respawn locations after death
- **Economic Center**: Main trading hubs and marketplaces
- **Fleet Assembly**: Staging area for coordinated operations

---

### Tier 1 - Protected Territorial Waters

**Purpose**: Transition zone from safety to contested waters

#### Characteristics
- **Ship Access**: Optimal for T3-T6 ships, safe for T1-T2, risky for T7-T10
- **Protection Level**: Strong faction presence with regular patrols
- **Enemy Presence**: Enemy infiltration possible but heavily contested
- **Risk Scaling**: T7-T10 ships are high-value targets even with protection
- **PvP Status**: Enabled, but NPC reinforcements respond quickly

#### Locations
- **USA**: Hawaiian Islands outer waters, Midway approach, Wake Island perimeter
- **UK**: English Channel, North Sea convoy routes, Gibraltar approach
- **Japan**: Truk Lagoon outer anchorage, Rabaul perimeter, Okinawa waters
- **Germany**: Baltic Sea, Norwegian coastal waters, Bay of Biscay

#### NPC Patrol Strength
- **Composition**: 3-5 destroyer patrols, 1-2 light cruisers
- **Response Time**: 2-3 minutes to distress calls
- **Effectiveness**: Can defeat solo T5-T7 attackers, struggle against T8+
- **Spawn Frequency**: Continuous patrols every 5-7 minutes

#### Facilities & Services
- **Repair Facilities**: Standard naval repair docks (75% efficiency vs T0)
- **Supply Points**: Regular supply depots with T1-T6 equipment
- **Economic Benefits**: 10% price reduction for home nation
- **Forward Bases**: Temporary forward operating bases for resupply
- **Intelligence**: Radar coverage, enemy position reports

#### Resources Available
- **Resource Tiers**: Common + uncommon materials
- **Examples**: Chromium, tungsten, advanced ammunition, radar components
- **Purpose**: Required for T5-T6 ship progression
- **Extraction**: Light extraction missions, minimal risk
- **Respawn Rate**: Moderate (30 minute respawn cycles)

#### Missions Available
- **Convoy Escorts**: Protect merchant ships through territorial waters (Low Risk)
- **Patrol Missions**: Scout for enemy infiltrators (Low Risk)
- **Anti-Submarine**: Hunt enemy submarines in protected waters (Medium Risk)
- **Reconnaissance**: Survey contested border areas (Medium Risk)

#### Strategic Value
- **Territory Control**: 75-90% faction control depending on war state
- **Buffer Zone**: Protects core waters from direct assault
- **Training Ground**: Safe-ish environment for T3-T6 players to learn PvP
- **Economic Flow**: Major shipping lanes for NPC convoys

---

### Tier 2 - Contested Border Waters

**Purpose**: Active combat zone with shifting control and moderate risk

#### Characteristics
- **Ship Access**: Optimal for T4-T7 ships, dangerous for T8-T10
- **Protection Level**: Mixed control with shifting battle lines
- **NPC Presence**: Moderate from multiple factions, unreliable protection
- **Risk Scaling**: T8+ ships attract aggressive players and NPC attention
- **PvP Status**: Full PvP with limited NPC interference

#### Locations
- **Pacific**: Philippine Sea, Solomon Islands, Marshall Islands
- **Atlantic**: Mid-Atlantic Gap, Iceland-Faroe corridor, Azores region
- **Mediterranean**: Central Mediterranean, Sicilian Channel, Aegean Sea
- **Arctic**: Bear Island region, Jan Mayen approaches, Barents Sea

#### Combat Intensity
- **Player Activity**: Moderate to High (20-40% of server population)
- **Engagement Frequency**: Every 15-30 minutes
- **Average Battle Size**: 3-8 ships per engagement
- **Typical Encounters**: Small task forces, solo raiders, convoy intercepts

#### Facilities & Services
- **Repair Facilities**: Limited facilities requiring supply management
- **Supply Points**: Forward supply caches (must be restocked by convoys)
- **Economic Benefits**: None - neutral pricing
- **Temporary Bases**: Capturable outposts that can change hands
- **Intelligence**: Limited radar coverage, sporadic updates

#### Resources Available
- **Resource Tiers**: Uncommon + rare materials
- **Examples**: High-grade steel, advanced electronics, armor plating, fire control systems
- **Purpose**: Required for T7-T8 ship progression
- **Extraction**: Moderate risk extraction missions
- **Respawn Rate**: Slow (1 hour respawn cycles)

#### Missions Available
- **Border Patrol**: Scout shifting battle lines (Medium Risk)
- **Supply Interdiction**: Attack enemy supply convoys (High Risk)
- **Territory Capture**: Secure temporary bases (High Risk)
- **Wreck Salvage**: Recover equipment from recent battles (Medium Risk)

#### Strategic Value
- **Territory Control**: 25-50% control, highly dynamic
- **Contested Resources**: High-value resources draw constant conflict
- **Strategic Positioning**: Control of chokepoints affects theater control
- **Front Line**: Active war zone where territorial control shifts daily

---

### Tier 3 - Disputed Ocean Areas

**Purpose**: High-risk, high-reward zones with no safety guarantees

#### Characteristics
- **Ship Access**: Optimal for T5-T8 ships, T9-T10 face extreme danger
- **Protection Level**: No guaranteed faction protection
- **Control**: Dynamic based on recent battles and player activity
- **Risk Scaling**: T9-T10 ships hunted aggressively by players and NPCs
- **PvP Status**: Unrestricted PvP, no NPC protection

#### Locations
- **Pacific**: Open Pacific shipping lanes, Coral Sea, Bismarck Sea
- **Atlantic**: Denmark Strait, Florida Straits, Cape Verde Basin
- **Mediterranean**: Libyan coast, Cretan waters, Turkish straits
- **Arctic**: Norwegian Sea, Greenland Sea, White Sea approaches

#### Combat Intensity
- **Player Activity**: High (30-50% of server population)
- **Engagement Frequency**: Constant (multiple simultaneous battles)
- **Average Battle Size**: 5-15 ships per engagement
- **Typical Encounters**: Multi-faction battles, organized raids, piracy

#### Facilities & Services
- **Repair Facilities**: None - mobile repair ships only
- **Supply Points**: Temporary mobile supply points (player-operated)
- **Economic Benefits**: None - must bring own supplies
- **Bases**: No permanent bases, only temporary anchorages
- **Intelligence**: No radar, only visual contact

#### Resources Available
- **Resource Tiers**: Rare + very rare materials
- **Examples**: Titanium alloys, experimental radar, advanced fire control, prototype weapons
- **Purpose**: Required for T9 ship progression, highly valuable
- **Extraction**: High-risk extraction requiring escort
- **Respawn Rate**: Very slow (2-3 hour respawn cycles)

#### Missions Available
- **Deep Water Patrols**: Hunt enemy raiders (Very High Risk)
- **Resource Extraction**: Mine rare materials under fire (Very High Risk)
- **Fleet Actions**: Coordinate large-scale battles (Very High Risk)
- **Wreck Recovery**: Salvage T7-T8 wrecks for technology (High Risk)

#### Strategic Value
- **Territory Control**: 0-25% control, chaotic and unpredictable
- **High-Value Resources**: Only source of rare materials
- **Strategic Wrecks**: Battle sites contain salvageable high-tier equipment
- **PvP Hotspot**: Attracts competitive players seeking challenges

---

### Tier 4 - Deep Ocean International Waters

**Purpose**: Lawless frontier with maximum risk and maximum reward

#### Characteristics
- **Ship Access**: Optimal for T6-T9 ships, T10 ships are massive targets
- **Protection Level**: ZERO - Complete free-for-all PvP environment
- **NPC Presence**: None - pure player vs. player combat
- **Risk Scaling**: T10 ships broadcast their presence, attract server-wide attention
- **PvP Status**: Complete lawlessness, no rules or restrictions

#### Locations
- **Pacific**: Mid-Pacific void, International Date Line, remote atolls
- **Atlantic**: Mid-Atlantic Ridge, South Atlantic isolation, Cape of Good Hope
- **Indian Ocean**: Deep Indian Ocean, Bay of Bengal, Arabian Sea
- **Southern Ocean**: Antarctic waters, extreme south latitudes

#### Combat Intensity
- **Player Activity**: Moderate (15-30% of server population, but hardcore players)
- **Engagement Frequency**: Unpredictable (can go hours without contact, then sudden chaos)
- **Average Battle Size**: 2-20 ships (extremes from solo to massive brawls)
- **Typical Encounters**: Ambushes, resource claim battles, T10 hunting parties

#### Facilities & Services
- **Repair Facilities**: NONE - must return to T2 zones or use mobile repair
- **Supply Points**: NONE - must bring all supplies
- **Economic Benefits**: NONE
- **Bases**: Secret player-established caches (can be raided)
- **Intelligence**: NONE - total isolation

#### Resources Available
- **Resource Tiers**: Very rare + legendary materials
- **Examples**: Experimental alloys, prototype technology, rare earth elements, enemy faction secrets
- **Purpose**: Essential for T10 ship progression and premium modules
- **Extraction**: Extreme risk, often requires fleet operations
- **Respawn Rate**: Extremely slow (6-12 hour respawn cycles)

#### Missions Available
- **Technology Recovery**: Salvage experimental equipment (Extreme Risk)
- **Deep Sea Mining**: Extract rare earth elements (Extreme Risk)
- **Enemy Hunting**: Track and eliminate high-value targets (Extreme Risk)
- **Secret Operations**: Classified missions with extraordinary rewards (Extreme Risk)

#### Strategic Value
- **Territory Control**: NONE - no nation controls these waters
- **Ultimate Resources**: Only source of legendary materials
- **Reputation Building**: Successful operations grant massive prestige
- **Economic Dominance**: Control of resources creates economic power

#### T10 Ship Mechanics in T4 Zones
When a T10 ship enters a T4 zone:
- **Server Alert**: All players within 3 zone radius receive notification
- **Bounty System**: Automatic bounty placed on T10 ship (proportional to value)
- **Hunter Coordination**: Players can coordinate via faction channels
- **High Stakes**: T10 ship death = complete permadeath

---

### Tier 5 - Enemy Core Waters (MOST DANGEROUS)

**Purpose**: Deep enemy territory, suicide missions, ultimate challenges

#### Characteristics
- **Ship Access**: Suicide mission for T1-T7, manageable for T8, T9-T10 = server event
- **Hostility Level**: MAXIMUM - Overwhelming enemy fleet presence
- **NPC Forces**: Continuous patrols, rapid response fleets, coastal defenses
- **Player Response**: Enemy players coordinate defense of home waters
- **T10 Impact**: T10 ship entering T5 zone triggers server-wide alert and response

#### Locations
- **Enemy USA**: Deep in Pearl Harbor, San Francisco Bay, New York Inner Harbor
- **Enemy UK**: Thames Estuary, Liverpool inner port, Belfast harbor
- **Enemy Japan**: Tokyo Bay depths, Hiroshima harbor, Nagasaki inner waters
- **Enemy Germany**: Hamburg inner port, Berlin canal system, Bremen docks

#### Combat Intensity
- **Player Activity**: EXTREME (enemy faction mobilizes)
- **Engagement Frequency**: Immediate and continuous
- **Average Response**: 10-30 ships within 5 minutes
- **NPC Response**: Multiple battleships, carriers, destroyer flotillas

#### Facilities & Services
- **Repair Facilities**: NONE - enemy port facilities require capture
- **Supply Points**: NONE - all facilities are hostile
- **Economic Benefits**: NONE
- **Bases**: Must destroy or capture enemy installations
- **Intelligence**: Enemy radar and detection at maximum effectiveness

#### Resources Available
- **Resource Tiers**: Legendary + exotic materials
- **Examples**: National secrets, prototype super-weapons, command codes, ultimate technology
- **Purpose**: T10 progression, unique legendary items
- **Extraction**: Nearly impossible without major fleet operation
- **Respawn Rate**: Once per server cycle (24 hours)

#### Missions Available
- **Covert Infiltration**: Submarine infiltration missions (Near-Impossible Risk)
- **Port Assault**: Coordinate massive fleet assault (Near-Impossible Risk)
- **Intelligence Theft**: Steal enemy nation secrets (Near-Impossible Risk)
- **Assassination**: Eliminate high-value NPC targets (Near-Impossible Risk)

#### Strategic Value
- **Territory Control**: 100% enemy control, nearly impossible to contest
- **Ultimate Challenge**: Pinnacle of difficulty for elite players
- **Legendary Rewards**: Unique items and achievements only available here
- **Propaganda Victory**: Successful raids grant massive faction-wide bonuses

#### T10 Ship Mechanics in T5 Zones
When a T10 ship enters enemy T5 zone:
- **Faction-Wide Alert**: Entire enemy faction receives emergency notification
- **NPC Fleet Response**: Capital ships sortie from port (battleships, carriers)
- **Player Mobilization**: Enemy players receive massive rewards for defense
- **Historical Event**: Engagement is recorded in server history
- **Ultimate Stakes**: Success = legendary status, failure = total loss

---

## Resource Distribution by Zone

### Tier 0-1 Zones: Common Materials
**Resources**: Steel, oil, basic ammunition, standard equipment
- **Availability**: Unlimited supply from NPC vendors
- **Purpose**: T1-T5 ship construction and basic modules
- **Acquisition**: Direct purchase or low-risk gathering missions
- **Economic Impact**: Base price materials, stable market

### Tier 2-3 Zones: Uncommon + Rare Materials
**Resources**: Chromium, tungsten, advanced electronics, armor plating, fire control systems
- **Availability**: Limited spawn nodes, contested extraction sites
- **Purpose**: T6-T8 ship construction and advanced modules
- **Acquisition**: Extraction missions, convoy raids, salvage operations
- **Economic Impact**: Fluctuating prices based on zone control

### Tier 4-5 Zones: Very Rare + Legendary Materials
**Resources**: Titanium alloys, experimental tech, rare earth elements, prototype weapons, national secrets
- **Availability**: Extremely rare spawn nodes, single-source locations
- **Purpose**: T9-T10 ship construction, premium modules, legendary items
- **Acquisition**: High-risk extraction, fleet operations, enemy territory raids
- **Economic Impact**: Extreme prices, player-controlled markets

### Forced Progression Through Dangerous Waters
**Design Principle**: Players CANNOT reach T9-T10 without entering T4-T5 zones.

**Progression Bottleneck**:
- **T1-T5 Ships**: Can be fully constructed with T0-T1 zone resources (safe progression)
- **T6-T8 Ships**: REQUIRE T2-T3 zone resources (moderate risk required)
- **T9-T10 Ships**: REQUIRE T4-T5 zone resources (extreme risk required)

**Economic Scarcity**:
- T4-T5 resources cannot be purchased from NPCs
- Player trading exists but at extreme markup (500-1000% premium)
- Most players must extract resources themselves to afford progression

---

## Ship Tier vs Zone Danger Scaling

### Risk Matrix

| Ship Tier | T0 Zone | T1 Zone | T2 Zone | T3 Zone | T4 Zone | T5 Zone |
|-----------|---------|---------|---------|---------|---------|---------|
| T1-T2     | Safe    | Safe    | Low Risk | Med Risk | High Risk | Suicide |
| T3-T4     | Safe    | Safe    | Low Risk | Med Risk | High Risk | Suicide |
| T5-T6     | Safe    | Safe    | Med Risk | High Risk | V.High Risk | Near Suicide |
| T7-T8     | Target  | Target  | High Risk | V.High Risk | Extreme Risk | Certain Death |
| T9-T10    | Target  | Target  | V.High Risk | Extreme Risk | Certain Death | Apocalypse |

### Low Tier Ships in High Tier Zones
**Strategy**: Cheap ships in dangerous zones for resource gathering

**Advantages**:
- Low insurance costs make losses acceptable
- T1-T4 ships have full recovery on death (no ship loss)
- Small ship = smaller target, easier to evade
- Cheap to replace if destroyed

**Disadvantages**:
- Limited cargo capacity (fewer resources per trip)
- Vulnerable to any hostile ship
- Cannot defend themselves effectively
- Slow extraction rates

**Best Use Case**: Solo resource runners gathering rare materials in T4 zones

### High Tier Ships in Low Tier Zones
**Strategy**: Powerful ships in safe zones (usually ineffective)

**Why It Fails**:
- **Target Painting**: T10 ships are tracked server-wide even in T1 zones
- **Insurance Costs**: Operating high-tier ships costs massive insurance premiums
- **Unprofitable**: T1 zone resources don't justify T10 ship operational costs
- **Seal Clubbing Prevention**: T7+ ships in T0-T1 zones attract organized hunting parties
- **Reputation Loss**: Attacking low-tier players in safe zones causes faction penalties

**Exception**: Legitimate reasons for T10 in T1:
- Escorting new guild members
- Returning to home port for repairs
- Ceremonial duties or social events

### Optimal Zone Matching
**Game Design Goal**: Natural guidance toward appropriate zones

**Recommended Pairings**:
- **T1-T3 ships → T0-T1 zones**: Learning, safe grinding, beginner PvP
- **T4-T6 ships → T2-T3 zones**: Progression, profit, competitive play
- **T7-T9 ships → T3-T4 zones**: High-end competitive play, resource extraction
- **T10 ships → T4-T5 zones**: Elite operations, maximum stakes gameplay

**Risk/Reward Optimization**:
Each pairing provides optimal balance between:
- Resource availability
- Insurance costs
- Combat effectiveness
- Profit margins
- Player skill requirements

---

## Dynamic Zone Control System

### Control Percentage (0-100%)
**Mechanism**: Real-time calculation of faction dominance in zone

**Factors Affecting Control**:
- **Player Presence**: Number of faction players in zone
- **Recent Battles**: Win/loss ratio in last 24 hours
- **Strategic Points**: Control of key locations and bases
- **NPC Reinforcements**: Faction convoy success rates
- **Time of Day**: Activity levels vary by time zone

**Control Decay**:
- Undefended zones gradually become neutral (1% per hour)
- Contested zones shift toward active faction (2-5% per hour)
- Enemy presence prevents control gain

### Control Benefits by Percentage

**0-25% Control (Enemy Territory)**:
- No benefits
- Enemy receives full benefits
- High risk to be present

**25-50% Control (Contested)**:
- 10% cost reduction at temporary bases
- Limited NPC patrols (25% effectiveness)
- Shared radar coverage (50% range)
- Occasional convoy support

**50-75% Control (Friendly Territory)**:
- 20% cost reduction at supply points
- Regular NPC patrols (50% effectiveness)
- Full radar coverage
- Regular convoy support

**75-100% Control (Dominated Territory)**:
- 30% cost reduction at all facilities
- Strong NPC patrols (100% effectiveness)
- Advanced radar and intelligence
- Constant convoy support
- Priority mission rewards

### Capture Mechanics
**Strategic Point System**: 50 major locations across all theaters

**Capture Process**:
1. **Initial Assault**: Players attack strategic point
2. **Defensive Response**: NPCs and players defend
3. **Control Timer**: 30-minute timer to maintain presence
4. **Capture Confirmation**: Point converts to attacking faction
5. **Defense Phase**: New owner must defend for 2 hours

**High-Value Targets**:
- **Major Naval Bases**: 10% zone control per base
- **Resource Nodes**: 5% zone control + resource access
- **Chokepoints**: 7% zone control + tactical advantage
- **Supply Depots**: 3% zone control + economic benefits

### Coalition System
**Alliance Benefits**: Allied nations can share territory benefits

**Coalition Mechanics**:
- **Shared Intelligence**: Radar coverage shared between allies
- **Combined Defense**: NPC forces cooperate in defense
- **Resource Sharing**: Reduced trade restrictions between allies
- **Coordinated Offensives**: Joint operations receive bonuses

**Example**: UK and USA players in Atlantic share convoy escort missions and radar coverage.

---

## Weather and Environmental Hazards by Zone

### Weather System Integration
Weather patterns vary by zone and geographic location.

**Zone-Specific Weather**:
- **T0 Zones**: Calm, predictable weather (safe for beginners)
- **T1 Zones**: Occasional storms (minor visibility penalties)
- **T2 Zones**: Frequent weather changes (tactical considerations)
- **T3 Zones**: Severe weather common (navigation challenges)
- **T4 Zones**: Extreme weather (dangerous sea states)
- **T5 Zones**: Unpredictable, hazardous weather (adds to danger)

### Environmental Hazards

**Minefields** (All Zones):
- **T0-T1**: Cleared by NPC minesweepers regularly
- **T2-T3**: Active minefields near contested points
- **T4-T5**: Dense minefields in enemy waters

**Ice Fields** (Arctic Theater):
- **T0-T1**: Ice-free channels maintained
- **T2-T3**: Seasonal ice requiring icebreaker support
- **T4-T5**: Permanent ice pack, extreme navigation difficulty

**Reef Systems** (Pacific Theater):
- **T0-T1**: Marked navigation channels
- **T2-T3**: Uncharted reefs create hazards
- **T4-T5**: Dangerous coral reefs hide ambush points

**Coastal Fortifications** (Near Land):
- **T0**: Friendly coastal guns protect faction waters
- **T1**: Light coastal defense batteries
- **T2-T3**: Heavy coastal guns in contested areas
- **T5**: Overwhelming coastal defense in enemy home waters

---

## Permadeath Mechanics by Zone

### Zone-Based Death Penalty Modifiers

**Important**: Zone penalties are **additional modifiers** that stack on top of ship tier-based permadeath rates. Operating deeper in enemy territory increases risk beyond base ship tier penalties.

**Base System Recap**:
- Ship/Crew Card Permadeath: Tier-based (0/0/0/0/0/10/20/40/60/100% for T1-T10 ships)
- Sailor Casualties: Damage-based (replaceable at ports)
- Module Destruction: Tier/damage-based

**Zone Modifiers Add Additional Risk**:

**T0 Zones**: No additional penalties
- Death mechanics follow standard ship tier penalties only
- Respawn at nearest friendly port

**T1 Zones**: Minor penalties
- +5% additional module destruction chance
- Respawn at nearest friendly port

**T2 Zones**: Moderate penalties
- +10% additional module destruction chance
- +5% additional sailor casualty rate (more sailors die from damage)
- Respawn at nearest T1 port

**T3 Zones**: High penalties
- +20% additional module destruction chance
- +10% additional sailor casualty rate
- Respawn at nearest T2 port (long return trip)

**T4 Zones**: Severe penalties
- +30% additional module destruction chance
- +20% additional sailor casualty rate
- +10% additional ship/crew card permadeath chance (stacks with ship tier)
- Respawn at home faction T0 port (very long return)

**T5 Zones**: Maximum penalties
- +50% additional module destruction chance
- +40% additional sailor casualty rate
- +25% additional ship/crew card permadeath chance (stacks with ship tier)
- T10 ships in T5 zones = guaranteed permadeath (100% base + zone penalty)
- Respawn at home faction T0 port
- Faction reputation penalty for death in enemy waters

**Example Stacking**:
- T8 ship (40% base permadeath) destroyed in T4 zone (+10% zone penalty) = **50% total permadeath chance**
- T9 ship (60% base permadeath) destroyed in T5 zone (+25% zone penalty) = **85% total permadeath chance**
- T6 ship (10% base permadeath) destroyed in T0 zone (no penalty) = **10% total permadeath chance**

### Emergency Beacon Range by Zone

**T0-T1 Zones**:
- Beacon Range: 50km
- Response Time: 2-5 minutes
- Success Rate: 95%

**T2-T3 Zones**:
- Beacon Range: 25km
- Response Time: 5-15 minutes
- Success Rate: 70%

**T4-T5 Zones**:
- Beacon Range: 10km
- Response Time: 15-30 minutes (if anyone responds)
- Success Rate: 30%

---

## Zone Transition Mechanics

### Crossing Zone Boundaries

**Visual Indicators**:
- **HUD Warning**: "Entering Tier 3 Zone - Contested Waters"
- **Map Color**: Zone borders clearly marked on map
- **Audio Cue**: Ominous music shift when entering dangerous zones
- **Water Color**: Ocean Environment system shifts biome colors

**Grace Period**:
- 30-second grace period when entering higher-tier zone
- Players can retreat without combat if they turn back immediately
- Used to prevent accidental incursions

**Transit Zones**:
- Some zones have "transit corridors" with reduced danger
- Used for safe passage through contested areas
- Still risky but less than open zone

### Zone-Hopping Strategy
**Tactics**: Using zone boundaries for tactical advantage

**Border Fighting**:
- Engage enemies near zone boundary
- Retreat to safer zone when outmatched
- NPCs stop pursuit at zone borders (players don't)

**Ambush Points**:
- Contested zone borders are natural ambush locations
- Players entering dangerous zones are vulnerable
- High-traffic areas attract PvP activity

**Escape Routes**:
- Smart players plan escape routes to safer zones
- Fast ships can flee to T1 zones when threatened
- Submarine can submerge and retreat undetected

---

## Dynamic Mission Generation by Zone

### Zone-Appropriate Missions

**T0 Zones**:
- Tutorial missions (new players)
- Ship testing and crew training
- Social missions (escort VIPs, diplomatic missions)

**T1 Zones**:
- Convoy escort (low risk)
- Anti-submarine patrol
- Reconnaissance missions
- Courier missions (deliver supplies)

**T2 Zones**:
- Border patrol (scout enemy activity)
- Supply interdiction (attack enemy convoys)
- Territory capture (secure temporary bases)
- Wreck salvage (recover recent battle wrecks)

**T3 Zones**:
- Deep water patrol (hunt enemy raiders)
- Resource extraction (mine rare materials)
- Fleet actions (coordinate large battles)
- Technology recovery (salvage high-tier equipment)

**T4 Zones**:
- Rare resource extraction (extreme risk)
- Enemy hunting (track high-value targets)
- Secret operations (classified missions)
- Deep sea exploration (discover hidden locations)

**T5 Zones**:
- Covert infiltration (submarine missions)
- Port assault (coordinate massive fleet operations)
- Intelligence theft (steal enemy secrets)
- Assassination (eliminate high-value NPC leaders)

### Mission Reward Scaling
**Risk = Reward Formula**

**Base Reward Multipliers by Zone**:
- T0: 1x base reward
- T1: 1.5x base reward
- T2: 3x base reward
- T3: 6x base reward
- T4: 12x base reward
- T5: 25x base reward

**Additional Multipliers**:
- Ship tier used (higher = more reward)
- Mission difficulty (complex objectives = more reward)
- Enemy activity (more enemies = more reward)
- Success rate (rare successes = more reward)

---

## Cross-References

### Related Systems
- [[Ocean-Environment]] - Provides visual representation of zones via biome system
- [[Ship-Progression-System]] - Ship tiers interact directly with zone risk levels
- [[Economy-System]] - Resource distribution and pricing tied to zones
- [[PvP-Combat-System]] - Zone tier determines PvP rules and intensity
- [[Territory-Control]] - Zone control mechanics and benefits
- [[Mission-Generation-System]] - Dynamic mission creation based on zone
- [[Weather-System]] - Zone-specific weather patterns and hazards

### Related Documents
- [[Map-Layout]] - Geographic distribution of zones across theaters
- [[Port-Locations]] - Port facilities and services by zone
- [[Weather-System]] - Environmental hazards by zone
- [[Permadeath-System]] - Death penalties modified by zone tier

---

## Design Decisions

### Why 6 Zone Tiers Instead of 10?
**Decision**: Use 6 zone tiers (T0-T5) for 10 ship tiers (T1-T10)

**Reasoning**:
- Simpler mental model for players
- Allows multiple ship tiers to share zones
- Creates overlap (T5 ships work in T1-T3 zones)
- Prevents excessive zone fragmentation
- Easier territorial control visualization

### Why Separate Zone and Ship Tiers?
**Decision**: Zone tier ≠ Ship tier

**Reasoning**:
- Allows low-tier ships to venture into high-tier zones (risk/reward)
- Makes high-tier ships valuable targets everywhere
- Prevents "level-based" matchmaking (boring)
- Creates organic player distribution across zones
- Supports diverse playstyles (cautious vs. aggressive)

### Why Forced Progression Through Dangerous Zones?
**Decision**: T9-T10 resources only in T4-T5 zones

**Reasoning**:
- Prevents safe grinding to max level
- Creates meaningful risk for top-tier ships
- Drives PvP interaction
- Rewards skilled players
- Creates "earning" progression vs. "time-based" progression

### Why No Safe T10 Zones?
**Decision**: T10 ships always at risk, even in T1 zones

**Reasoning**:
- Prevents T10 dominance without risk
- Makes T10 ships rare and prestigious
- Creates server-wide events when T10s fight
- Prevents "end-game stagnation"
- Encourages using T7-T9 ships for daily gameplay

---

## Future Enhancements

### Phase 2 Additions
- **Dynamic Zone Boundaries**: Zones shift based on war progress
- **Seasonal Zones**: Ice coverage changes in Arctic, monsoons in Pacific
- **Player-Created Zones**: Large guilds can establish territory
- **Special Event Zones**: Limited-time high-reward zones appear

### Phase 3 Additions
- **Zone Weather Integration**: Weather affects zone danger levels
- **NPC Fleet Movements**: Large NPC fleets transit between zones
- **Economic Blockades**: Control zones to blockade enemy resources
- **Persistent Zone Damage**: Wrecks and damage persist in zones

---

**Status**: 📋 Comprehensive design ready for Phase 2 implementation
**Dependencies**: Requires Ocean Environment (implemented), Economy System, Ship Progression
**Next Steps**: Technical design document, prototype zone boundary system
