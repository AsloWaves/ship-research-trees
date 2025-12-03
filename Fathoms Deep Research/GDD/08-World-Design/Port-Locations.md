---
tags: [planned, phase2-3, world-design, ports]
status: 📋 PLANNED
phase: Phase 2-3
priority: MEDIUM-HIGH
last-updated: 2025-11-17
---

# Port Locations

## Overview
Port Locations define the network of naval bases, harbors, and anchorages throughout the game world. Ports serve as safe havens, economic centers, repair facilities, and strategic objectives. The port system includes major naval bases (home ports), standard ports (forward operations), contested ports (frontline), and temporary anchorages (player-created). Each port offers different services, facilities, and strategic value based on its tier and faction control.

**IMPORTANT**: Port tiers (Tier 0-3) describe port FACILITY LEVELS, not visible zones. Players see ports as safe havens - they don't see "zone boundaries" on the map.

**Core Philosophy**: Ports are the economic and strategic lifeblood of naval warfare, providing sanctuary, supplies, and staging areas for operations.

## Implementation Status
**Status**: 📋 PLANNED
**Phase**: Phase 2-3 (World Building & Economy)
**Dependencies**: [[Map-Layout]], [[Zone-System]], [[Economy-System]], [[Territory-Control]]
**Priority**: MEDIUM-HIGH - Essential for player progression and economy

---

## Design Specification

### Port Classification System

#### By Security Level
- **Tier 0 Ports**: Core national waters, maximum security
- **Tier 1 Ports**: Protected territorial waters, high security
- **Tier 2 Ports**: Contested borders, moderate security
- **Tier 3 Ports**: Disputed areas, minimal security
- **Temporary Anchorages**: No fixed security, player-created

#### By Faction Control
- **Faction-Controlled**: 100% owned by single faction
- **Contested**: 25-75% control, can change hands
- **Neutral**: Non-aligned ports serving all factions (for a price)
- **Captured**: Recently taken ports, unstable control

#### By Size and Importance
- **Major Naval Bases**: Capital ship construction, full services
- **Standard Ports**: Regular ship construction, most services
- **Forward Bases**: Resupply and repairs only
- **Minor Outposts**: Basic supplies, limited facilities
- **Hidden Anchorages**: Secret player bases, minimal facilities

---

## Port Services & Facilities

### Core Services (All Ports)

#### Safe Zone Protection
**Mechanism**: No-combat zones around ports

**Protection Radius by Port Tier**:
- **Tier 0 Major Naval Bases**: 50 km radius
  - Weapons automatically disabled in zone
  - Attacking players face overwhelming NPC response
  - Instant destruction for violators
- **Tier 1 Standard Ports**: 25 km radius
  - Combat discouraged but possible at edges
  - NPC patrols respond within 2-3 minutes
  - Penalties for safe zone violations
- **Tier 2 Forward Bases**: 10 km radius
  - Minimal protection, still considered "port waters"
  - Limited NPC response
  - Small penalties for violations
- **Tier 3 Outposts**: 5 km radius
  - Token protection only
  - Sporadic NPC presence
  - No violation penalties

**Safe Zone Violations**:
- **First Offense**: Faction reputation penalty (-1000)
- **Second Offense**: Temporary ban from all faction ports (24 hours)
- **Third Offense**: Permanent ban from faction ports (requires reputation restoration quest)
- **Attacking Same Faction**: Severe penalties, possible account action

#### Docking and Berthing
**Mechanism**: Ships must dock to access port services

**Docking Mechanics**:
- **Automatic Docking**: Enter port zone, press "Dock" (F key)
- **Docking Time**: 30 seconds to 2 minutes (depends on ship size)
- **Berth Assignment**: Automatic assignment to appropriate berth
  - Destroyers: Standard piers
  - Cruisers: Deep-water piers
  - Battleships: Capital ship berths
  - Carriers: Specialized carrier berths
  - Submarines: Submarine pens
- **Docking Fees**: Based on ship tier and port type
  - T0 Ports: No fee for home nation
  - T1 Ports: 100-500 credits based on ship tier
  - T2 Ports: 500-2000 credits
  - Neutral Ports: 2x normal fees

**Undocking**:
- Instant undocking available
- Ship spawns at port entrance (outside safe zone by 100m)
- Cannot undock during port assault (T2-T3 ports)

#### Ship Storage (Drydock)
**Mechanism**: Players can store multiple ships at ports

**Storage Capacity by Port Tier**:
- **T0 Major Naval Bases**: Unlimited ship storage
- **T1 Standard Ports**: 10 ships maximum
- **T2 Forward Bases**: 5 ships maximum
- **T3 Outposts**: 1 ship maximum (current ship only)

**Storage Features**:
- **Ship Preservation**: Stored ships don't decay or require maintenance
- **Loadout Saving**: Ship configuration saved with ship
- **Crew Assignment**: Crew remains assigned to stored ships
- **Cross-Port Access**: Ships can be transferred between ports (24 hour transfer time)
- **Storage Fees**: Monthly storage fee based on ship tier
  - T1-T3 ships: 1,000 credits/month
  - T4-T6 ships: 5,000 credits/month
  - T7-T9 ships: 25,000 credits/month
  - T10 ships: 100,000 credits/month

### Repair Facilities

#### Damage Repair
**Mechanism**: Restore ship HP and module damage

**Repair Speed by Port Tier**:
- **T0 Major Naval Bases**: Instant repair (magical drydock)
- **T1 Standard Ports**: 75% efficiency (1 hour for full repair)
- **T2 Forward Bases**: 50% efficiency (2 hours for full repair)
- **T3 Outposts**: 25% efficiency (4 hours for full repair)

**Repair Costs**:
- **Hull Damage**: 10 credits per 1% HP (T1 ship) scaling up to 1,000 credits per 1% (T10 ship)
- **Module Damage**: 25% of module purchase price to repair
- **Crew Injuries**: 500-5,000 credits per injured crew member
- **Economic Modifiers**:
  - Home nation ports: -20% cost
  - Neutral ports: +50% cost
  - Enemy captured ports: +100% cost

**Repair Resources**:
- Repairs consume resources (steel, components)
- Players can supply own materials for reduced costs
- Ports can run out of repair materials if overused

#### Module Replacement
**Mechanism**: Replace destroyed modules

**Module Installation**:
- **Installation Time**: 10 minutes to 2 hours (depends on module complexity)
- **Installation Cost**: 10% of module purchase price
- **Requirements**: Port must have appropriate facilities
  - Main guns: Requires gun turret crane
  - Engines: Requires engine shop
  - Radar: Requires electronics workshop
  - Aircraft: Requires carrier facilities

**Available Modules by Port Tier**:
- **T0 Ports**: All modules T1-T10
- **T1 Ports**: Modules T1-T7
- **T2 Ports**: Modules T1-T5
- **T3 Ports**: Basic modules only (T1-T3)

### Supply and Resupply

#### Ammunition Resupply
**Mechanism**: Reload expended ammunition

**Resupply Speed**:
- **T0 Ports**: Instant resupply
- **T1 Ports**: 5 minutes per 10% ammunition
- **T2 Ports**: 10 minutes per 10% ammunition
- **T3 Ports**: 20 minutes per 10% ammunition

**Ammunition Costs**:
- **Standard Shells**: 10 credits per shell (scaling by caliber)
- **Armor-Piercing**: 25 credits per shell
- **High-Explosive**: 20 credits per shell
- **Torpedoes**: 500-2,000 credits per torpedo
- **Depth Charges**: 100 credits per depth charge
- **Anti-Aircraft Ammunition**: 5 credits per shell

**Economic Modifiers**:
- Home nation: -20% cost
- High faction standing: Additional -10% cost
- Neutral ports: +50% cost
- Wartime shortages: +100% cost (dynamic)

#### Fuel Resupply
**Mechanism**: Refill fuel tanks

**Fuel Costs**:
- **Standard Oil**: 5 credits per unit
- **High-Octane Aviation Fuel**: 15 credits per unit
- **Diesel (Submarines)**: 7 credits per unit

**Refueling Speed**:
- **T0 Ports**: Instant refueling
- **T1 Ports**: 2 minutes per 10% fuel
- **T2 Ports**: 5 minutes per 10% fuel
- **T3 Ports**: 10 minutes per 10% fuel

**Fuel Availability**:
- Ports can run out of fuel if supply lines disrupted
- Fuel prices increase during shortages
- Convoy missions replenish port fuel supplies

#### Provisions and Supplies
**Mechanism**: Restock crew food, medical supplies, spare parts

**Supply Types**:
- **Food**: Maintains crew morale, 1,000 credits per week supply
- **Medical Supplies**: Treats injuries, 2,000 credits to restock
- **Spare Parts**: Emergency repairs at sea, 5,000 credits to restock
- **Luxury Goods**: Boosts morale, 10,000 credits (optional)

**Supply Importance**:
- Ships without food suffer morale penalties (-10% performance)
- Ships without medical supplies cannot treat crew injuries at sea
- Ships without spare parts cannot make emergency repairs
- Long-range operations require careful supply planning

### Ship Construction

#### Shipyard Facilities
**Mechanism**: Construct new ships from resources

**Construction Availability by Port Tier**:
- **T0 Major Naval Bases**:
  - All ship types T1-T10
  - Super battleships and fleet carriers
  - Experimental prototypes
- **T1 Standard Ports**:
  - Ship types T1-T7
  - Standard battleships and carriers
  - Cruisers and destroyers
- **T2 Forward Bases**:
  - Ship types T1-T5 only
  - Destroyers and light cruisers
  - Submarines
- **T3 Outposts**:
  - No construction facilities

**Construction Time**:
- **T1-T3 Destroyers**: 1-2 hours
- **T4-T6 Cruisers**: 4-8 hours
- **T7-T9 Battleships**: 12-24 hours
- **T10 Super Battleships**: 48 hours
- **Carriers**: 16-36 hours (by tier)

**Construction Requirements**:
- Resources (steel, components, fuel)
- Construction fee (credits)
- Shipyard availability (queue system if busy)
- Nation technology unlocked

#### Ship Upgrades
**Mechanism**: Upgrade existing ships to higher tiers (limited)

**Upgrade System**:
- **Hull Refits**: Upgrade T4 destroyer to T5 destroyer (same class, next tier)
- **Modernization**: Add modern modules to older ships
- **Repair and Restore**: Restore damaged hulls to combat readiness

**Upgrade Costs**:
- 50% of new ship construction cost
- Requires original ship + resources
- 6-12 hour upgrade time
- Only available at T0-T1 ports

### Economic Services

#### Marketplace
**Mechanism**: Player-to-player trading

**Market Features**:
- **Buy Orders**: Players list items for sale
- **Sell Orders**: Players list items wanted to buy
- **Auction House**: Rare items sold to highest bidder
- **Market Tax**: 5-10% transaction fee (varies by port)

**Tradeable Items**:
- Resources (steel, fuel, rare materials)
- Modules and equipment
- Ships (pre-built ships can be sold)
- Intelligence (maps, enemy positions)
- Crew members (recruited crew for sale)

**Market Availability by Port Tier**:
- **T0 Ports**: Full marketplace, auction house
- **T1 Ports**: Standard marketplace, no auctions
- **T2 Ports**: Basic trading, high transaction fees
- **T3 Ports**: No marketplace

#### Port Storage System
**Mechanism**: Limited storage at each port for resources, modules, ammunition, crew cards, currency, and trade goods

**Port Storage Capacity** (Per-Port, Separate Inventories):
- **T1-T3 Ports**: 500 grid cells storage capacity
- **T4-T7 Ports**: 750 grid cells storage capacity
- **T8-T10 Ports**: 1000 grid cells storage capacity

**Key Rules**:
- **Separate per port**: Storage at Port A is completely separate from Port B
- **No account bank**: No universal storage shared across all ports
- **Physical transport only**: Resources must be physically transported via ship cargo between ports
- **Player teleportation**: Players can teleport between ports (character only), but items cannot
- **Grid-based system**: Same Tetris-style inventory as ship cargo (items occupy grid cells based on size)

**What Can Be Stored**:
- Ammunition stockpiles (shells, torpedoes, depth charges)
- Spare modules and turrets (uninstalled equipment)
- Crew cards (loose 2x2 items or organized in wallets)
- Wallets (containing crew cards + physical currency for compression)
- Trade goods and extracted loot
- Fuel reserves
- Repair materials
- Physical currency (stored as items in inventory or in wallets)

**Port Services**:
- **Insurance Policies**: Purchase insurance for ships (ship tier-based, distance multiplier)
- **Drydock Storage**: Store inactive ships at port (ships retain their cargo/modules)

**Storage Fees**:
- First 100 grid cells: Free
- Additional capacity: 50 credits per 10 grid cells per month
- Full warehouse forces decisions: sell items, transfer to drydocked ship, or relocate to different port

#### Black Market
**Mechanism**: Illegal trading for rare items

**Black Market Availability**:
- **T2-T3 Ports**: Black market hidden in port districts
- **Neutral Ports**: Major black market hub
- **Contested Ports**: Active black markets (risky)

**Black Market Goods**:
- Experimental modules (not yet released)
- Enemy faction technology
- Stolen goods (from raiding)
- Intelligence documents
- Illegal upgrades (bypass restrictions)

**Black Market Risks**:
- Faction reputation penalties if caught
- No guarantees on quality
- Higher prices (2x-5x normal)
- Risk of scams or faulty equipment

### Intelligence and Information

#### Reconnaissance Office
**Mechanism**: Purchase intelligence reports

**Intelligence Types**:
- **Enemy Fleet Movements**: Last known positions of enemy fleets (1 hour delay)
- **Convoy Schedules**: NPC convoy routes and timings
- **Resource Spawns**: Locations of rare resource nodes
- **Zone Control**: Real-time territorial control percentages
- **Weather Forecasts**: 6-hour weather predictions

**Intelligence Costs**:
- **Basic Reports**: 1,000 credits
- **Detailed Reports**: 5,000 credits
- **Real-Time Tracking**: 25,000 credits (1 hour duration)

#### Mission Briefing Room
**Mechanism**: Accept and turn in missions

**Mission Types Available**:
- Zone-appropriate missions (see [[Zone-System]])
- Faction-specific missions (nation-based)
- Player-created contracts (bounty board)
- Dynamic event missions (server-wide campaigns)

**Mission Rewards Collected Here**:
- Credits and experience
- Resources and equipment
- Faction reputation
- Special mission tokens

### Crew Management

#### Recruitment Office
**Mechanism**: Hire new crew members

**Crew Availability**:
- **T0 Ports**: All crew specializations, high skill caps
- **T1 Ports**: Common specializations, moderate skill
- **T2 Ports**: Basic crew only, low skill
- **T3 Ports**: No recruitment facilities

**Crew Costs**:
- **Basic Crew**: 500 credits per crew member
- **Specialized Crew**: 2,000-10,000 credits (pilots, engineers, radar operators)
- **Veteran Crew**: 25,000+ credits (pre-leveled, rare)

**Crew Pool**:
- Crew randomly generated with skill ratings
- Higher-tier ports have better crew quality
- Refresh rate: New crew available every 6 hours

#### Training Facilities
**Mechanism**: Train crew in specializations

**Training Programs**:
- **Cross-Training**: Teach crew secondary skills (1 week, 5,000 credits)
- **Specialization**: Advanced training in primary skill (2 weeks, 10,000 credits)
- **Leadership**: Train officers (4 weeks, 25,000 credits)

**Training Availability**:
- **T0 Ports**: Full training facilities, all specializations
- **T1 Ports**: Basic training only
- **T2-T3 Ports**: No training facilities

#### Medical Facilities
**Mechanism**: Treat injured crew members

**Medical Services**:
- **Injury Treatment**: Restore injured crew (1,000-10,000 credits per crew)
- **Rehabilitation**: Speed up injury recovery (50% time reduction, 5,000 credits)
- **Resurrection**: Revive dead crew if recovered quickly (50,000 credits, 24 hour window)

**Medical Availability**:
- **T0 Ports**: Advanced medical facilities, all services
- **T1 Ports**: Standard medical facilities, basic services
- **T2 Ports**: Field hospitals, injury treatment only
- **T3 Ports**: No medical facilities

### Social and Guild Services

#### Officer's Club
**Mechanism**: Social hub for players

**Club Features**:
- **Voice Chat Lounge**: In-game voice chat rooms
- **Mission Board**: Player-created missions and bounties
- **Guild Recruitment**: Find or advertise for guilds
- **Leaderboards**: View top players and guilds
- **Historical Records**: Server event history, famous battles

**Club Availability**:
- All T0-T1 ports have Officer's Clubs
- Premium clubs in major ports (cosmetic benefits)

#### Guild Headquarters
**Mechanism**: Guild management and operations

**Guild Services** (T0 Ports Only):
- **Guild Bank**: Shared resource storage
- **Guild Contracts**: Guild-specific missions
- **Fleet Operations**: Coordinate large-scale operations
- **Guild Territory**: View and manage guild-controlled zones
- **Guild Upgrades**: Purchase guild-wide benefits

**Guild Requirements**:
- Minimum 10 guild members
- Guild registration fee: 100,000 credits
- Monthly maintenance: 50,000 credits

---

## Port Types and Examples

### Major Naval Bases (Tier 0)

#### Pearl Harbor (USA)
**Location**: Hawaii, Central Pacific
**Faction**: USA
**Area Type**: Core National Waters

**Facilities**:
- ✓ Advanced carrier repair facilities
- ✓ Submarine base and dry docks
- ✓ Battleship construction yards
- ✓ Aviation fuel depot (largest in Pacific)
- ✓ Major supply depot (unlimited supplies)
- ✓ Full marketplace and auction house
- ✓ Training academy (all specializations)
- ✓ Guild headquarters support

**Services**:
- Ship construction: T1-T10, all types
- Instant repairs and resupply
- Unlimited storage (drydock)
- Banking and resource vaults (10,000 capacity)
- Intelligence office (Pacific theater)
- Officer's Club and social hub

**Strategic Value**:
- USA Pacific command center
- Staging point for all Pacific operations
- Primary respawn point for USA players
- Economic hub for USA faction

**Safe Zone**: 50 km radius

---

#### Scapa Flow (UK)
**Location**: Orkney Islands, Scotland
**Faction**: UK
**Area Type**: Core National Waters

**Facilities**:
- ✓ Home Fleet anchorage
- ✓ Secure deep-water anchorage
- ✓ Capital ship repair yards
- ✓ Battleship construction (UK battleships)
- ✓ Anti-submarine warfare center
- ✓ Arctic convoy staging area

**Services**:
- Ship construction: T1-T10, specializing in battleships
- Instant repairs and resupply
- Unlimited storage
- Banking and resource vaults
- Intelligence office (Atlantic theater)
- Officer's Club

**Strategic Value**:
- Royal Navy command center
- Most secure anchorage in Europe
- Arctic convoy departure point
- Primary respawn for UK players

**Safe Zone**: 50 km radius

---

#### Tokyo Bay (Japan)
**Location**: Japan Home Islands
**Faction**: Japan
**Area Type**: Core National Waters

**Facilities**:
- ✓ Japanese naval headquarters
- ✓ Advanced shipbuilding yards
- ✓ Super-battleship construction (Yamato-class)
- ✓ Carrier development center
- ✓ Submarine pens
- ✓ Aviation development centers

**Services**:
- Ship construction: T1-T10, specializing in carriers and super-battleships
- Instant repairs and resupply
- Unlimited storage
- Banking and resource vaults
- Intelligence office (Pacific theater)
- Officer's Club

**Strategic Value**:
- Imperial Japanese Navy headquarters
- Combined Fleet anchorage
- Technological development center
- Primary respawn for Japan players

**Safe Zone**: 50 km radius

---

#### Kiel Canal (Germany)
**Location**: Northern Germany
**Faction**: Germany
**Area Type**: Core National Waters

**Facilities**:
- ✓ U-boat construction pens
- ✓ Baltic Sea access
- ✓ Naval headquarters
- ✓ Submarine academy
- ✓ Torpedo development center
- ✓ Surface fleet construction

**Services**:
- Ship construction: T1-T10, specializing in submarines and surface raiders
- Instant repairs and resupply
- Unlimited storage
- Banking and resource vaults
- Intelligence office (Atlantic theater)
- Officer's Club

**Strategic Value**:
- Kriegsmarine command center
- U-boat operations headquarters
- Baltic Sea control
- Primary respawn for Germany players

**Safe Zone**: 50 km radius

---

### Standard Ports (Tier 1)

#### Midway Island (USA)
**Location**: North Pacific
**Faction**: USA
**Area Type**: Protected Territorial Waters

**Facilities**:
- ✓ Forward refueling station
- ✓ Basic repair facilities (75% efficiency)
- ✓ Early warning radar station
- ✓ Airfield (patrol aircraft)
- ✓ Small supply depot

**Services**:
- Ship construction: T1-T6 destroyers and cruisers
- Standard repairs (1 hour for full repair)
- Storage: 10 ships
- Basic marketplace
- Intelligence reports (regional)
- Crew recruitment (basic crew)

**Strategic Value**:
- Critical refueling point for trans-Pacific operations
- Early warning station against Japanese expansion
- Forward staging for carrier operations

**Safe Zone**: 25 km radius

---

#### Gibraltar (UK)
**Location**: Mediterranean entrance
**Faction**: UK
**Area Type**: Protected Territorial Waters

**Facilities**:
- ✓ Strategic fortress
- ✓ Submarine base
- ✓ Supply depot
- ✓ Repair facilities
- ✓ Aircraft carrier operations support

**Services**:
- Ship construction: T1-T7, all types
- Standard repairs
- Storage: 10 ships
- Full marketplace
- Intelligence office (Mediterranean focus)
- Crew recruitment

**Strategic Value**:
- Controls Mediterranean access from Atlantic
- Critical chokepoint
- Force H headquarters
- Mediterranean operations staging

**Safe Zone**: 25 km radius

---

#### Truk Lagoon (Japan)
**Location**: Caroline Islands
**Faction**: Japan
**Area Type**: Protected Territorial Waters

**Facilities**:
- ✓ Massive fleet anchorage
- ✓ Forward repair facilities
- ✓ Submarine base
- ✓ Supply depot
- ✓ Carrier support facilities

**Services**:
- Ship construction: T1-T7, specializing in carriers
- Standard repairs
- Storage: 10 ships
- Basic marketplace
- Intelligence reports
- Crew recruitment

**Strategic Value**:
- "Gibraltar of the Pacific"
- Forward operating base for Japanese fleet
- Controls Caroline Islands
- Carrier operations hub

**Safe Zone**: 25 km radius

---

### Forward Bases (Tier 2)

#### Wake Island (USA)
**Location**: Central Pacific
**Faction**: Contested (USA/Japan)
**Area Type**: Contested Border Waters

**Facilities**:
- ✓ Forward operating base
- ✓ Contested supply depot
- ✓ Temporary repair facilities (50% efficiency)
- ✓ Basic airstrip

**Services**:
- Ship construction: T1-T5 destroyers only
- Slow repairs (2 hours for full repair)
- Storage: 5 ships
- No marketplace (resource trading only)
- No intelligence services
- No crew recruitment

**Strategic Value**:
- Frontline base
- High-value contested territory
- Can change hands during combat
- Forward supply point

**Safe Zone**: 10 km radius

**Contested Port Mechanics**:
- Control changes based on zone control percentage
- Facilities unavailable during assault (30 minute lockout)
- Capturing port grants faction-wide bonuses

---

#### Malta (UK)
**Location**: Central Mediterranean
**Faction**: UK (heavily contested)
**Area Type**: Contested Border Waters

**Facilities**:
- ✓ Fortress island
- ✓ Submarine base
- ✓ Limited repair facilities (under siege)
- ✓ Small supply cache

**Services**:
- No ship construction (under siege)
- Limited repairs (50% efficiency, resource shortages)
- Storage: 5 ships
- No marketplace
- Intelligence reports (Mediterranean)
- No crew recruitment

**Strategic Value**:
- Strategic pivot point in Mediterranean
- Submarine operations base
- Convoy waypoint (critical resupply)
- Heavily besieged by Axis forces

**Safe Zone**: 10 km radius

**Siege Mechanics**:
- Port under constant threat
- Convoys required to resupply port (player missions)
- If convoys fail, port services degrade
- Major faction victory if captured by Axis

---

### Minor Outposts (Tier 3)

#### Bear Island Weather Station
**Location**: Barents Sea, Arctic
**Faction**: Neutral (contested)
**Area Type**: Disputed Ocean Areas

**Facilities**:
- ✓ Weather station
- ✓ Basic supply cache
- ✓ Temporary anchorage

**Services**:
- No ship construction
- Emergency repairs only (25% efficiency)
- Storage: 1 ship (current ship only)
- No marketplace
- Weather forecasting (specialized intelligence)
- No crew services

**Strategic Value**:
- Arctic convoy waypoint
- Weather intelligence critical for operations
- Forward observation post
- Minimal strategic value but useful utility

**Safe Zone**: 5 km radius

---

### Neutral Ports

#### Lisbon (Portugal)
**Location**: Atlantic coast, Iberian Peninsula
**Faction**: Neutral (serves all factions)
**Area Type**: Neutral Waters (safe haven for all factions)

**Facilities**:
- ✓ Neutral port (all factions welcome)
- ✓ Black market hub
- ✓ Repair facilities
- ✓ Supply depot
- ✓ Information brokers

**Services**:
- No ship construction (neutral)
- Standard repairs (2x cost for all factions)
- Storage: 5 ships
- Black market (major hub)
- Intelligence for sale (all theaters)
- Crew recruitment (expensive, neutral crews)

**Strategic Value**:
- Safe trading hub for all factions
- Black market center
- Espionage and intelligence trading
- Refuge for players fleeing combat

**Safe Zone**: 25 km radius (enforced for all factions)

**Neutral Port Rules**:
- Combat strictly forbidden (auto-destruction for violators)
- All factions pay premium prices (+50%)
- No faction missions available
- Black market thrives (illegal goods)
- Intelligence trading (sell enemy positions)

---

### Temporary Anchorages (Player-Created)

#### Hidden Coves and Remote Anchorages
**Location**: Varies (player-established)
**Faction**: Player-controlled
**Area Type**: Lawless Waters (dangerous, unpatrolled areas)

**Facilities**:
- ✓ Basic anchorage (player-built)
- ✓ Secret supply cache (player-stocked)
- ✓ Hidden coordinates (secret location)

**Services**:
- No ship construction
- Player-supplied repairs (if resources stocked)
- Storage: Based on player investment
- Secret marketplace (guild members only)
- No NPC services

**Strategic Value**:
- Secret staging areas for raids
- Hidden resource caches
- Guild operations bases
- Can be discovered and raided by enemies

**Safe Zone**: None (PvP enabled)

**Player Anchorage Mechanics**:
- Players can establish hidden bases in dangerous, unpatrolled waters
- Requires significant resource investment
- Must be defended from discovery
- Can be raided and destroyed
- Provides strategic advantage for guilds

---

## Port Ownership and Territory Control

### Control Mechanics

#### Faction Control (0-100%)
**Mechanism**: Ports tied to zone control percentage

**Control Thresholds**:
- **100% Control**: Full faction ownership
  - All services available
  - Lowest prices
  - NPC patrols protect port
- **75-99% Control**: Dominant faction
  - All services available
  - Standard prices
  - Regular patrols
- **50-74% Control**: Contested
  - Most services available
  - Increased prices (+25%)
  - Sporadic patrols
- **25-49% Control**: Losing control
  - Limited services
  - High prices (+50%)
  - Minimal patrols
- **0-24% Control**: Enemy capture imminent
  - Emergency services only
  - Extreme prices (+100%)
  - No patrols

#### Port Assault Mechanics
**Mechanism**: Players can assault and capture T2-T3 ports

**Assault Process**:
1. **Declaration**: Attacking faction declares assault (1 hour warning)
2. **Mobilization**: Defenders receive alert, can mobilize defenses
3. **Battle Phase**: 2-hour battle window
   - Attackers must destroy port defenses
   - Defenders must repel attackers
4. **Capture Timer**: If attackers win, 30-minute capture timer starts
   - Attackers must maintain presence
   - Defenders can counterattack
5. **Control Transfer**: If timer completes, port changes hands
6. **Defense Phase**: New owners must defend for 2 hours (vulnerable period)

**Assault Rewards**:
- **Attackers**:
  - Massive reputation gain
  - Loot from port supplies
  - Territory control bonus
  - Server-wide recognition
- **Defenders**:
  - Reputation for successful defense
  - Economic bonuses for protecting port
  - Faction-wide morale boost

**Port Defenses**:
- **Coastal Batteries**: NPC-controlled shore guns
- **Defensive Fleet**: NPC garrison fleet
- **Minefields**: Surrounding mine barriers
- **Air Defenses**: Anti-aircraft batteries

### Port Upgrades (Guild System)

#### Guild Port Investment
**Mechanism**: Guilds can invest in port upgrades

**Upgrade Types**:
- **Enhanced Defenses**: Stronger coastal batteries, more NPC garrison
- **Economic Improvements**: Larger marketplace, better trading prices
- **Facility Expansion**: Faster repairs, more storage capacity
- **Intelligence Network**: Better reconnaissance, enemy tracking

**Upgrade Costs**:
- **Minor Upgrades**: 100,000 credits, 1 week construction
- **Major Upgrades**: 1,000,000 credits, 4 weeks construction
- **Ultimate Upgrades**: 10,000,000 credits, 12 weeks construction

**Guild Benefits**:
- Guild members get discounts at upgraded ports
- Guild reputation increases
- Port provides passive income to guild
- Strategic dominance in region

---

## Port Services by Nation

### USA Port Characteristics
**Specializations**: Industrial capacity, carrier operations, mass production

**Service Bonuses**:
- **Carrier Repairs**: 50% faster carrier repairs
- **Mass Production**: 25% discount on T4-T6 cruisers and destroyers
- **Industrial Supply**: Abundant standard resources
- **Crew Quality**: High-quality engineering and damage control crews

**Example Ports**: Pearl Harbor, New York, Norfolk, San Diego

---

### UK Port Characteristics
**Specializations**: Capital ship expertise, convoy support, radar technology

**Service Bonuses**:
- **Battleship Repairs**: 50% faster battleship repairs
- **Radar Modules**: 25% discount on radar and detection equipment
- **Convoy Escorts**: Enhanced convoy mission rewards
- **Crew Quality**: Superior navigation and officer crews

**Example Ports**: Scapa Flow, Portsmouth, Liverpool, Gibraltar

---

### Japan Port Characteristics
**Specializations**: Carrier aviation, super-battleships, torpedo technology

**Service Bonuses**:
- **Carrier Aviation**: 50% faster carrier aircraft repairs and rearming
- **Super-Battleship Support**: Yamato-class construction and maintenance
- **Torpedo Technology**: 25% discount on torpedo weapons and upgrades
- **Crew Quality**: Elite aviation and torpedo crews

**Example Ports**: Tokyo Bay, Truk Lagoon, Kure, Yokosuka

---

### Germany Port Characteristics
**Specializations**: Submarine warfare, surface raiders, engineering excellence

**Service Bonuses**:
- **U-Boat Support**: 50% faster submarine repairs and torpedo rearming
- **Surface Raider Repairs**: Enhanced repairs for heavy cruisers and battleships
- **Engineering Excellence**: 25% discount on engine and propulsion upgrades
- **Crew Quality**: Superior submarine and engineering crews

**Example Ports**: Kiel, Wilhelmshaven, Brest, Hamburg

---

## Economic Impact of Ports

### Supply and Demand
**Mechanism**: Port prices fluctuate based on activity

**Price Factors**:
- **Convoy Success**: Successful convoys reduce prices (-10% per successful convoy)
- **Blockades**: Enemy blockades increase prices (+50% during blockade)
- **Resource Scarcity**: War consumption depletes supplies
- **Player Activity**: High demand increases prices

### Trade Routes
**Mechanism**: NPC convoys establish trade routes between ports

**Trade Route Benefits**:
- Ports connected by trade routes share resource pools
- Prices equalize between connected ports
- Convoy missions maintain trade routes
- Disrupted routes cause price spikes

**Major Trade Routes**:
- **Trans-Atlantic**: New York ↔ Liverpool (critical for UK)
- **Pacific Supply**: Pearl Harbor ↔ Midway ↔ Wake Island
- **Mediterranean**: Gibraltar ↔ Malta ↔ Alexandria
- **Arctic Convoys**: Scapa Flow ↔ Murmansk (via Bear Island)

### Economic Warfare
**Mechanism**: Disrupting enemy supply lines

**Economic Attack Methods**:
- **Convoy Raiding**: Sink enemy convoys to disrupt supply
- **Port Blockades**: Prevent ships from entering/leaving ports
- **Resource Denial**: Capture resource-rich zones
- **Market Manipulation**: Flood market with cheap goods or buy up critical supplies

**Economic Victory Conditions**:
- Enemy faction unable to afford repairs (resource starvation)
- Port facilities degraded from lack of supplies
- Mass economic protests (NPC morale collapse)

---

## Cross-References

### Related Systems
- [[Zone-System]] - Port locations relate to danger gradients (edges=safe, center=dangerous)
- [[Map-Layout]] - Geographic location of all ports
- [[Economy-System]] - Port services drive economy
- [[Territory-Control]] - Port ownership and control mechanics
- [[Mission-Generation-System]] - Ports generate missions
- [[Ship-Progression-System]] - Ports enable ship construction and upgrades

### Related Documents
- [[Resource-Distribution]] - Ports are resource distribution hubs
- [[Convoy-System]] - Convoys supply ports
- [[PvP-Combat-System]] - Port assault mechanics
- [[Guild-System]] - Guild port investments and control

---

## Design Decisions

### Why Safe Zones Around Ports?
**Decision**: No-combat zones around ports

**Reasoning**:
- Prevents spawn camping and griefing
- Allows safe access to services
- Creates predictable safe havens
- Enables social interaction without combat threat
- Balances risk/reward (leave safe zone for rewards)

### Why Tiered Port Services?
**Decision**: Higher tier ports have better services

**Reasoning**:
- Encourages progression toward advanced areas
- Creates strategic value for ports
- Balances convenience with risk (safe ports = long travel)
- Drives territorial control gameplay (control best ports)
- Creates economic centers vs. frontier outposts

### Why Contested Ports Can Change Hands?
**Decision**: T2-T3 ports can be captured

**Reasoning**:
- Creates dynamic world where territory shifts
- Provides endgame content (port assaults)
- Rewards organized guild play
- Creates server-wide strategic campaigns
- Prevents static, boring world state

### Why Include Neutral Ports?
**Decision**: Neutral ports serve all factions (at premium)

**Reasoning**:
- Provides refuge for players between faction operations
- Creates black market economy
- Allows intelligence trading between factions
- Enables cross-faction social interaction
- Historical authenticity (Lisbon was WWII neutral port)

---

## Future Enhancements

### Phase 2 Additions
- **Port Assault System**: Full implementation of contested port mechanics
- **Guild Port Investment**: Guild upgrade system
- **Dynamic Pricing**: Advanced supply/demand economics
- **Port Reputation**: Individual reputation with each port

### Phase 3 Additions
- **Port Bombardment**: Shore bombardment damages port facilities
- **Amphibious Assaults**: Combined land/sea port capture
- **Port Civilians**: NPC population affects morale and economy
- **Port Sabotage**: Covert operations to disrupt enemy ports

---

**Status**: 📋 Comprehensive port system design ready for implementation
**Dependencies**: Map Layout, Zone System, Economy System, Territory Control
**Next Steps**: Implement T0 home ports first, expand to T1-T3 as zones are added
