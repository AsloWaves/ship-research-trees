---
tags: [planned, design, core-gameplay]
status: 📋 PLANNED
phase: Core Development
priority: HIGH
last-updated: 2025-12-03
---

# Mission System

## Overview

The Mission System provides structured objectives that give players direction, purpose, and additional rewards beyond freeform extraction gameplay. Players access missions through **Mission Boards** located at friendly ports, with different mission types offered by various agents representing nations, local authorities, merchant companies, and special event coordinators.

## Implementation Status
**Status**: 📋 PLANNED - Core mission framework design
**Phase**: Core Development
**Priority**: HIGH - Essential for player engagement and progression

---

## 1. Core Design Philosophy

### 1.1 Missions Enhance, Not Replace, Extraction Gameplay

**Critical Principle**: Missions are **optional objectives layered on top** of the core extraction loop. Players can always:
- Undock without any mission
- Ignore active missions mid-expedition
- Complete extraction without mission objectives

Missions provide **structure and rewards** for players who want directed gameplay, but the emergent sandbox extraction experience remains primary.

### 1.2 Risk-Reward Integration

All missions follow the extraction philosophy:
- **Nothing is secured until you return to port**
- Mission rewards only granted upon successful extraction
- Failed extraction = failed mission (with exceptions for repeatable objectives)
- Higher difficulty missions require venturing into more dangerous waters

### 1.3 Player Agency

**Mission Selection Freedom**:
- Players choose which missions to accept
- Multiple missions can be active simultaneously
- Missions can be abandoned (with reputation penalty)
- No forced mission requirements for progression (reputation unlocks gear, not mission gates)

---

## 2. Mission Board System

### 2.1 Port-Based Mission Boards

Each friendly port contains a **Mission Board** interface where players browse and accept available missions.

**Mission Board Location**: Harbor Master's Office (accessible from port services menu)

**Board Refresh Mechanics**:
- **Port Missions**: Refresh every 6 hours (server time)
- **Nation Missions**: Refresh daily at 00:00 UTC
- **Event Missions**: Fixed duration based on event schedule
- **Daily Challenges**: Refresh every 22 hours (personal timer)
- **Weekly Objectives**: Refresh every Monday 00:00 UTC

### 2.2 Mission Board Categories

The Mission Board displays missions organized into tabs:

| Tab | Description | Source |
|-----|-------------|--------|
| **Local** | Missions specific to this port | Port Authority |
| **National** | Faction-wide missions for your nation | Naval Command |
| **Merchant** | Trade and cargo missions | Merchant Alliance |
| **Bounty** | Combat and elimination missions | Naval Intelligence |
| **Salvage** | Exploration and recovery missions | Salvage Guild |
| **Special** | Event and limited-time missions | Event Coordinators |
| **Daily/Weekly** | Personal challenge objectives | Personal Log |

### 2.3 Mission Availability Factors

Missions shown on the board depend on:

**Player Requirements**:
- Captain Rank (minimum rank to accept)
- Nation Standing (reputation threshold)
- Ship Tier (minimum/maximum tier restrictions)
- Skill Prerequisites (specific crew skills for specialized missions)

**Port Factors**:
- Port Tier (larger ports = more missions)
- Port Nation (nation-specific missions)
- Geographic Location (missions relate to nearby waters)
- Current Events (event missions appear globally)

**Dynamic Factors**:
- Server Population (mission quantity scales)
- War State (combat missions increase during conflicts)
- Economic State (trade missions respond to market conditions)
- Recent Player Activity (procedural missions react to world state)

---

## 3. Mission Types

### 3.1 Combat Missions

#### Patrol Duty
**Objective**: Patrol designated sea zones and engage hostile contacts
**Mechanics**:
- Navigate through 2-4 waypoints in sequence
- Engage any enemy contacts encountered (NPC or player)
- Survive patrol route and return to port
- Bonus rewards for number of hostiles eliminated

**Variants**:
- **Sector Patrol**: Patrol specific map grid squares
- **Convoy Route Patrol**: Follow established shipping lane
- **Border Patrol**: Patrol contested zone boundaries
- **Night Patrol**: Patrol during night cycle (reduced visibility, bonus rewards)

**Rewards**: Credits, Naval Reputation, Combat XP, Ammunition Resupply

---

#### Elimination Contracts
**Objective**: Destroy specific targets (NPC convoys, enemy installations, or designated player bounties)
**Mechanics**:
- Target information provided (location, ship type, escort strength)
- Must sink primary target to complete
- Optional: Eliminate escorts for bonus rewards
- Evidence of kill required (wreckage marker, screenshot validation for PvP)

**Variants**:
- **Convoy Interdiction**: Destroy merchant convoy (3-6 ships)
- **Warship Elimination**: Sink designated military vessel
- **Installation Strike**: Destroy coastal defense emplacement
- **Player Bounty**: Eliminate specific player who has committed piracy (PvP only)
- **Ace Hunter**: Eliminate NPC "ace" captain with unique ship (rare, high difficulty)

**Rewards**: Credits, Bounty Hunter Reputation, Rare Equipment Drops, Kill Achievements

---

#### Defensive Operations
**Objective**: Protect friendly assets from enemy attack
**Mechanics**:
- Report to defensive position within time limit
- Defend target for duration (waves of attackers)
- Target must survive at 25%+ HP for mission success
- Partial credit for target survival at lower HP

**Variants**:
- **Port Defense**: Defend friendly port from NPC raid
- **Convoy Escort**: Protect NPC convoy across route
- **Installation Defense**: Protect offshore platform or lighthouse
- **VIP Escort**: Protect specific high-value NPC ship

**Rewards**: Credits, Defense Commendation, Defensive Module Rewards, Crew XP

---

### 3.2 Delivery Missions

#### Cargo Transport
**Objective**: Deliver cargo from origin port to destination port
**Mechanics**:
- Accept cargo at mission port (consumes cargo space)
- Navigate to destination through potentially hostile waters
- Deliver cargo intact (damaged cargo = reduced payout)
- Time bonus for fast delivery

**Variants**:
- **Standard Freight**: Common goods, moderate pay
- **Perishable Cargo**: Time-sensitive (24-hour real-time limit)
- **Fragile Cargo**: Combat damage destroys cargo
- **Oversized Cargo**: Requires minimum cargo capacity
- **Contraband Run**: Illegal goods, high pay, severe reputation loss if caught

**Rewards**: Credits, Merchant Reputation, Trade XP, Delivery Bonuses

---

#### Personnel Transport
**Objective**: Transport NPC passengers between ports
**Mechanics**:
- Passengers board at origin (no cargo space consumed)
- Special requirements (some passengers hate combat, storms, etc.)
- Passenger satisfaction affects payout
- Must dock at correct destination

**Variants**:
- **Military Transfer**: Transport naval officers (no combat restrictions)
- **Civilian Evacuation**: Transport refugees (time-critical, bonus for safety)
- **VIP Transport**: High-value passenger with special demands
- **Prisoner Transport**: Secure prisoner (escape attempt events)
- **Medical Evacuation**: Wounded personnel requiring speed

**Rewards**: Credits, Transport Reputation, Passenger Tips, Special Items

---

#### Supply Runs
**Objective**: Deliver critical supplies to remote locations
**Mechanics**:
- Pick up supplies at major port
- Deliver to remote outpost or fleet position
- Often requires navigating through contested waters
- Supply type affects mission complexity

**Variants**:
- **Fuel Delivery**: Bring fuel to stranded friendly ships
- **Ammunition Resupply**: Deliver ammo to forward operating base
- **Medical Supplies**: Urgent medical delivery (time bonus)
- **Repair Materials**: Deliver repair supplies to damaged fleet
- **Secret Documents**: Deliver intelligence package (must avoid enemy detection)

**Rewards**: Credits, Logistics Reputation, Supply Stockpile Access

---

### 3.3 Exploration Missions

#### Reconnaissance
**Objective**: Scout enemy positions and gather intelligence
**Mechanics**:
- Navigate to designated area without being detected
- "Mark" enemy positions by approaching within radar range
- Collect intelligence data (time spent in area)
- Return to port with gathered intel

**Variants**:
- **Fleet Reconnaissance**: Locate and count enemy fleet composition
- **Port Surveillance**: Observe enemy port activity
- **Minefield Mapping**: Chart hazardous mine locations
- **Weather Station**: Deploy weather buoy at remote location
- **Signal Intelligence**: Intercept enemy radio communications (electronics skill)

**Rewards**: Credits, Intelligence Reputation, Map Reveals, Strategic Information

---

#### Discovery Expeditions
**Objective**: Explore uncharted or dangerous areas
**Mechanics**:
- Navigate to remote location
- Investigate points of interest
- Document findings (automatic upon approach)
- Survive journey home

**Variants**:
- **Shipwreck Investigation**: Locate and explore sunken vessel
- **Island Survey**: Chart unknown island features
- **Derelict Recovery**: Board and investigate abandoned ship
- **Anomaly Investigation**: Investigate reported strange phenomena
- **Historical Site**: Document historical naval battle location

**Rewards**: Credits, Explorer Reputation, Map Markers, Lore Entries, Rare Discoveries

---

### 3.4 Salvage Missions

#### Wreck Salvage
**Objective**: Recover valuable items from shipwrecks
**Mechanics**:
- Navigate to wreck location (often in dangerous waters)
- Salvage operation requires time at location (5-15 minutes)
- Salvage quality depends on crew skills and equipment
- Must extract with salvaged goods

**Variants**:
- **Surface Wreck**: Recently sunk ship, easy access
- **Shallow Wreck**: Requires diving equipment (future feature)
- **Deep Wreck**: Submarine-only access (submarines)
- **Contested Wreck**: Multiple parties racing for salvage
- **Historical Wreck**: Famous ship with unique artifacts

**Rewards**: Salvaged Equipment, Rare Materials, Historical Artifacts, Credits

---

#### Resource Collection
**Objective**: Gather specific resources from the environment
**Mechanics**:
- Navigate to resource-rich areas
- Collect required quantity of resource type
- Often requires specific equipment (fishing gear, mining dredge)
- Resource locations may be contested

**Variants**:
- **Oil Collection**: Gather fuel from offshore wells
- **Mineral Dredging**: Collect rare minerals from seabed
- **Fishing Contract**: Catch specific fish species (quantity)
- **Debris Collection**: Gather floating debris for recycling
- **Research Samples**: Collect water/biological samples for scientists

**Rewards**: Resources, Credits, Research Reputation, Collection Bonuses

---

### 3.5 Escort Missions

#### Convoy Protection
**Objective**: Escort NPC convoy safely to destination
**Mechanics**:
- Meet convoy at designated rendezvous point
- Stay within escort range of convoy ships
- Protect convoy from attacks (NPCs and/or players)
- Convoy reaches destination with minimum ships surviving

**Variants**:
- **Merchant Convoy**: Protect 4-8 merchant ships
- **Troop Transport**: Protect military transports (high value)
- **Tanker Convoy**: Protect fuel convoy (explosive cargo!)
- **Supply Fleet**: Mixed cargo with varying priorities
- **Hospital Ships**: Protect medical vessels (non-combatant rules)

**Rewards**: Credits, Escort Commendation, Crew XP, Reputation

---

#### VIP Protection
**Objective**: Protect specific high-value ship or person
**Mechanics**:
- VIP ship must survive entire journey
- Mission fails if VIP is destroyed
- VIP may have special requirements or route preferences
- Often involves decoy/distraction tactics

**Variants**:
- **Admiral Escort**: Protect flag officer's vessel
- **Diplomat Transport**: Protect neutral diplomat (can't fire first)
- **Research Vessel**: Protect unarmed science ship
- **Treasure Ship**: Protect high-value cargo (attracts pirates)
- **Royal Yacht**: Protect prestigious vessel (reputation critical)

**Rewards**: High Credits, Honor Awards, VIP Favor (special unlocks)

---

### 3.6 Hunt/Bounty Missions

#### Player Bounties
**Objective**: Eliminate specific player who has accumulated criminal reputation
**Mechanics**:
- Target player information provided (last known location, ship type)
- Must personally deliver killing blow or be in combat group
- Target may have bodyguards or allies
- Bounty only paid if you extract after kill

**Availability**: Only active when player has committed piracy/war crimes
**Restrictions**: Cannot bounty hunt members of own nation

**Rewards**: Bounty Payout (scales with target's crimes), Bounty Hunter Reputation

---

#### NPC Ace Hunts
**Objective**: Locate and destroy legendary NPC captains with unique ships
**Mechanics**:
- Ace location hints provided (region, time patterns)
- Ace ships are powerful (mini-boss tier)
- Aces have unique combat behavior and tactics
- May require multiple players to defeat

**Variants**:
- **Pirate Lord**: Infamous NPC pirate captain
- **Enemy Ace**: Legendary enemy nation captain
- **Ghost Ship**: Mysterious vessel with supernatural reputation
- **Rogue Admiral**: Defected officer with powerful stolen ship

**Rewards**: Rare Equipment (unique drops), High Credits, Achievement Titles

---

### 3.7 Storyline Missions

#### Campaign Chapters
**Objective**: Multi-part mission chains telling larger narratives
**Mechanics**:
- Unlock through reputation milestones
- Each chapter requires completing previous chapter
- Mix of mission types within chain
- Culminates in climactic final mission

**Chains Available**:
- **National Pride**: Your nation's main campaign (20 missions)
- **Merchant Prince**: Rise through merchant ranks (15 missions)
- **Pirate Hunter**: Eliminate pirate threat (12 missions)
- **The Deep**: Submarine-focused campaign (10 missions)
- **Wings of the Fleet**: Carrier operations campaign (10 missions)

**Rewards**: Unique Ships, Exclusive Cosmetics, Title Unlocks, Campaign Completion Bonus

---

#### Historical Operations
**Objective**: Participate in recreations of famous naval battles
**Mechanics**:
- Available during historical anniversary events
- Large-scale battles with many players
- Historical briefing provided
- Outcome may differ from history based on player performance

**Examples**:
- **Operation Torch** (November): North African landings support
- **D-Day Operations** (June): Normandy naval support
- **Midway Anniversary** (June): Carrier battle recreation
- **Pearl Harbor Memorial** (December): Defensive scenario

**Rewards**: Historical Camouflage, Commemorative Flags, Event Currency

---

### 3.8 Economic Missions

#### Market Manipulation
**Objective**: Influence market prices through strategic trading
**Mechanics**:
- Buy/sell specific quantities at designated ports
- Affects server-wide market prices (temporarily)
- Competes against other players doing same mission
- Profit sharing based on market impact

**Variants**:
- **Bull Market**: Drive up prices of commodity
- **Bear Market**: Crash prices of commodity
- **Arbitrage**: Exploit price differences between ports
- **Cornering**: Accumulate monopoly position

**Rewards**: Market Profits, Trader Reputation, Economic Achievement

---

#### Trade Route Establishment
**Objective**: Complete specific trade routes to unlock permanent benefits
**Mechanics**:
- Complete series of deliveries along route
- Each completion adds to route progress
- Route permanently unlocked at 100% completion
- Unlocked routes provide passive bonuses

**Benefits of Unlocked Routes**:
- Reduced port fees along route
- Priority docking at route ports
- Trade route NPC traffic (ambient ships)
- Route-specific missions become available

**Rewards**: Route Unlock, Merchant Reputation, Passive Income

---

## 4. Mission Agents

### 4.1 Agent Types

Different agents offer different mission categories:

| Agent | Location | Mission Types | Reputation Track |
|-------|----------|---------------|------------------|
| **Harbor Master** | All Ports | Local missions, Port services | Port Standing |
| **Naval Command** | Military Ports | Combat, Patrol, Defense | Naval Rank |
| **Merchant Guild** | Trade Ports | Delivery, Trade, Transport | Merchant Standing |
| **Intelligence Office** | Capital Ports | Recon, Espionage, Bounty | Intelligence Clearance |
| **Salvage Guild** | Industrial Ports | Salvage, Collection, Exploration | Salvager Reputation |
| **Pirate Contact** | Neutral Ports | Smuggling, Contraband, Raids | Underworld Reputation |

### 4.2 Agent Levels

Similar to EVE Online, agents have levels determining mission difficulty:

| Agent Level | Captain Rank Req | Ship Tier Range | Reward Multiplier |
|-------------|------------------|-----------------|-------------------|
| Level 1 | Rank 1+ | T1-T3 | 1.0x |
| Level 2 | Rank 10+ | T2-T5 | 1.5x |
| Level 3 | Rank 25+ | T4-T7 | 2.5x |
| Level 4 | Rank 40+ | T6-T9 | 4.0x |
| Level 5 | Rank 60+ | T8-T10 | 6.0x |

### 4.3 Agent Standing

Your standing with individual agents affects:
- Mission availability (higher standing = better missions)
- Mission rewards (standing bonus up to +20%)
- Priority for limited missions
- Exclusive agent-specific mission chains

**Gaining Agent Standing**:
- Complete missions from that agent
- Gift valuable items to agent
- Complete faction reputation milestones

---

## 5. Daily & Weekly Challenges

### 5.1 Daily Challenges

**Structure**: Three tiers of daily objectives

| Tier | Requirement | Reward |
|------|-------------|--------|
| **Tier 1** | Easy objective | 50 Credits, 100 XP |
| **Tier 2** | Medium objective (requires Tier 1) | 150 Credits, 250 XP |
| **Tier 3** | Hard objective (requires Tier 2) | 500 Credits, 500 XP, Item |

**Example Daily Chains**:
- **Combat**: Deal 5,000 damage → Sink 3 ships → Sink 1 ship of higher tier
- **Trade**: Complete 1 delivery → Earn 1,000 trade credits → Deliver fragile cargo
- **Exploration**: Visit 3 ports → Scout 2 zones → Discover 1 point of interest

**Daily Refresh**: 22 hours after last completion (not fixed time)

### 5.2 Weekly Objectives

**Structure**: Larger objectives spanning the week

| Objective Type | Example | Reward |
|----------------|---------|--------|
| **Combat Weekly** | Sink 25 enemy ships | 5,000 Credits, Rare Module |
| **Trade Weekly** | Complete 15 deliveries | 4,000 Credits, Trade Crate |
| **Exploration Weekly** | Visit 20 unique ports | 3,000 Credits, Map Pack |
| **Mixed Weekly** | Complete 10 missions of any type | 6,000 Credits, Rare Module |

**Weekly Refresh**: Monday 00:00 UTC

### 5.3 Monthly Objectives

**Structure**: Long-term goals with significant rewards

| Objective Type | Requirement | Reward |
|----------------|-------------|--------|
| **Monthly Combat** | Sink 100 ships, Complete 20 combat missions | Unique Ship Skin |
| **Monthly Trade** | Earn 100,000 trade credits | Merchant Title + Cosmetic |
| **Monthly Explorer** | Discover 50 POIs | Explorer Badge + Map |
| **Monthly All-Rounder** | Complete 50 missions total | 10,000 Credits, Unique Cosmetic |

---

## 6. Event Missions

### 6.1 Seasonal Events

**Major Events** (Quarterly):
- **Spring Offensive** (March-April): Combat-focused event
- **Summer Trade Fair** (June-July): Economic event
- **Autumn Harvest** (September-October): Collection event
- **Winter War** (December-January): Large-scale PvP event

**Event Structure**:
- Event missions available for 4-6 weeks
- Progressive rewards for participation
- Limited-time cosmetics and ships
- Community goals with server-wide rewards

### 6.2 Historical Commemorations

**Anniversary Events** (Annual):
- Pearl Harbor Memorial (December 7)
- D-Day Anniversary (June 6)
- VE Day (May 8)
- VJ Day (August 15)
- Battle of Midway (June 4-7)

**Structure**:
- Special historical missions during event period
- Historical briefings and educational content
- Unique rewards (camouflage, flags, emblems)
- Respectful treatment of historical events

### 6.3 Dynamic World Events

**Procedural Events** (Random):
- **Pirate Uprising**: Increased pirate activity in region
- **Merchant Boom**: Double trade rewards for limited time
- **Storm Season**: Weather challenges with bonus rewards
- **Arms Race**: Combat focus with equipment rewards
- **Treasure Fleet**: High-value NPCs spawning

**Trigger Conditions**:
- Player activity patterns
- Server population
- Economic conditions
- Random chance (weighted by time since last event)

---

## 7. Mission Rewards

### 7.1 Reward Types

| Reward Type | Description |
|-------------|-------------|
| **Credits** | Primary currency for ships, equipment, repairs |
| **Reputation** | Standing with nations, agents, factions |
| **Experience** | Captain XP, Crew XP, Skill XP |
| **Equipment** | Modules, weapons, ammunition |
| **Resources** | Crafting materials, fuel, supplies |
| **Cosmetics** | Skins, flags, emblems, titles |
| **Ships** | Rare/unique vessels (storyline rewards) |

### 7.2 Reward Scaling

Rewards scale based on:
- **Mission Difficulty**: Higher tier = higher rewards
- **Agent Level**: Level 5 agents pay 6x Level 1
- **Standing Bonus**: Up to +20% for high standing
- **First-Time Bonus**: +50% for mission first completion
- **Speed Bonus**: Up to +25% for fast completion
- **Efficiency Bonus**: Extra for no damage taken, all objectives complete

### 7.3 Bonus Objectives

Most missions have optional bonus objectives:
- **Speed Run**: Complete within time limit
- **Flawless**: Complete without taking damage
- **Overkill**: Exceed kill requirements
- **Discovery**: Find hidden objective
- **Mercy**: Complete without killing (where applicable)

---

## 8. Mission Failure & Abandonment

### 8.1 Failure Conditions

**Mission Fails When**:
- Player ship is destroyed (extraction failure)
- Primary objective becomes impossible
- Time limit expires (if applicable)
- Protected target is destroyed

**Failure Consequences**:
- No mission rewards granted
- Small reputation penalty with agent (-1 to -5)
- Cooldown before retrying same mission (1 hour)
- Cargo/items from mission lost (if any)

### 8.2 Mission Abandonment

**Abandoning Active Mission**:
- Can be done at any time from mission log
- Reputation penalty: -5 to -15 (based on mission difficulty)
- Cooldown: 2 hours before accepting from same agent
- No penalty for abandoning before leaving port

**Strategic Abandonment**:
- Sometimes smart to abandon unwinnable mission
- Reputation can be rebuilt through successful missions
- Emergency logout does NOT auto-abandon (mission persists)

---

## 9. Procedural Mission Generation

### 9.1 Dynamic Mission System

The system generates missions based on:

**World State Factors**:
- Recent player activity in area
- NPC convoy schedules
- Current weather patterns
- Economic supply/demand
- War state between nations

**Player Factors**:
- Player's ship tier and type
- Player's reputation standings
- Player's recent mission history
- Player's skill specializations

### 9.2 Mission Templates

Procedural missions combine:

**Mission Template**: Base structure (patrol, delivery, elimination, etc.)
**Location Slot**: Procedurally selected appropriate location
**Target Slot**: Appropriate NPC or objective for location
**Reward Slot**: Scaled rewards for difficulty
**Modifier Slot**: Optional complexity (time limit, bonus objectives)

**Example Generation**:
```
Template: Convoy Interdiction
Location: Sector B-7 (determined by trade route analysis)
Target: 4x Merchant Freighter + 2x Escort Destroyer
Reward: 2,500 Credits, +3 Combat Rep (scaled for T5 mission)
Modifier: Night operation (+25% rewards, reduced visibility)
```

### 9.3 Mission Pool Refresh

**Pool Mechanics**:
- Each port maintains mission pool (8-15 missions)
- Pool refreshes partially every 6 hours
- 2-4 missions replaced per refresh
- High-demand missions may reappear
- Player-completed missions don't reappear for 24 hours (personal cooldown)

---

## 10. UI/UX Design

### 10.1 Mission Board Interface

**Main Elements**:
```
+--------------------------------------------------+
|  MISSION BOARD - Port of [Port Name]             |
+--------------------------------------------------+
| [Local] [National] [Merchant] [Bounty] [Event]   |
+--------------------------------------------------+
|  +----------------------------------------------+|
|  | [!] Convoy Escort - Level 3                  ||
|  |     Escort merchant convoy to Sector D-4     ||
|  |     Reward: 1,500 Credits, +5 Escort Rep     ||
|  |     Tier Req: T4-T7 | Time: 45 min           ||
|  |     [ACCEPT] [DETAILS]                       ||
|  +----------------------------------------------+|
|  | [ ] Patrol Duty - Level 2                    ||
|  |     Patrol sectors A-1 through A-4           ||
|  |     Reward: 800 Credits, +3 Naval Rep        ||
|  |     Tier Req: T2-T5 | Time: 30 min           ||
|  |     [ACCEPT] [DETAILS]                       ||
|  +----------------------------------------------+|
|  | ...                                          ||
+--------------------------------------------------+
|  Active Missions: 2/5 | Daily Progress: 1/3     |
+--------------------------------------------------+
```

### 10.2 Active Mission Tracker

**HUD Element**: Minimal display during gameplay
- Current objective text
- Progress indicator (3/5 ships destroyed)
- Time remaining (if applicable)
- Quick-view expansion on hover

**Full Mission Log**: Accessible from pause menu
- All active missions with full details
- Objective checklist
- Reward preview
- Abandon option

### 10.3 Mission Completion Flow

1. **Objective Complete**: Notification appears
2. **Extraction Required**: Reminder that rewards require port return
3. **Port Arrival**: Mission completion popup
4. **Reward Screen**: Detailed breakdown of all rewards
5. **Next Mission Suggestion**: Related missions highlighted

---

## 11. Integration with Game Systems

### 11.1 Extraction Mechanics Integration

**Critical**: All missions respect extraction rules
- Mission rewards only granted at friendly port
- Failed extraction = failed mission
- Cargo from missions occupies ship inventory
- Mission waypoints visible on navigation

### 11.2 Reputation System Integration

**Cross-References**: [[Reputation-System]]

- Missions grant reputation with issuing faction
- High reputation unlocks better missions
- Some missions require minimum reputation
- Mission failure penalizes reputation

### 11.3 Economy Integration

**Cross-References**: [[Economy-Overview]], [[Trading-System]]

- Trade missions affect market prices
- Mission rewards follow economic balance
- Contraband missions risk reputation
- Economic events spawn special missions

### 11.4 Combat System Integration

**Cross-References**: [[Combat-Overview]], [[Surface-Combat]]

- Combat missions track kills accurately
- Damage dealt/received tracked for objectives
- Ship tier requirements enforced
- Crew casualties count toward objectives (protect missions)

---

## 12. Balancing Considerations

### 12.1 Mission Economy

**Target Earnings**:
- Level 1 missions: 100-300 Credits (30 min equivalent)
- Level 3 missions: 500-1,500 Credits (45 min equivalent)
- Level 5 missions: 2,000-6,000 Credits (60 min equivalent)

**Comparison to Freeform**:
- Missions should provide ~20% better rewards than equivalent freeform activity
- This compensates for restricted objectives
- Freeform remains viable for experienced players

### 12.2 Time Investment

**Target Completion Times**:
- Quick missions: 15-30 minutes
- Standard missions: 30-60 minutes
- Extended missions: 1-2 hours
- Campaign chapters: 2-4 hours cumulative

### 12.3 Difficulty Curve

**New Player Missions** (Level 1):
- Simple objectives (single location, clear target)
- Low risk zones (T1-T3 waters)
- Forgiving time limits
- High success rate expected (80%+)

**Veteran Missions** (Level 5):
- Complex multi-stage objectives
- High risk zones (T8-T10 waters)
- Tight requirements
- Challenge-focused (50% success rate)

---

## 13. Port-Tier Difficulty System

### 13.1 Design Philosophy

**Mission difficulty is determined by PORT TIER, not player choice.** Players naturally progress through difficulty by accessing higher-tier ports as they advance.

### 13.2 Port Tier Mission Scaling

| Port Tier | Mission Difficulty | Ship Tier Range | Reward Range | Typical Missions |
|-----------|-------------------|-----------------|--------------|------------------|
| **Tier 1** (Starter) | Beginner | T1-T2 | 50-200 Credits | Tutorial, basic patrols |
| **Tier 2** (Minor) | Easy | T1-T3 | 100-400 Credits | Local patrols, simple deliveries |
| **Tier 3** (Regional) | Normal | T2-T5 | 300-800 Credits | Zone patrols, convoy escort |
| **Tier 4** (Major) | Moderate | T3-T6 | 600-1,500 Credits | Multi-zone operations |
| **Tier 5** (Capital) | Hard | T4-T8 | 1,200-3,000 Credits | Strategic missions, campaigns |
| **Tier 6** (Fleet HQ) | Expert | T6-T9 | 2,500-5,000 Credits | High-value targets, deep ops |
| **Tier 7** (Command) | Elite | T7-T10 | 4,000-8,000 Credits | Critical operations |
| **Tier 8** (Strategic) | Legendary | T8-T10 | 6,000-15,000 Credits | War-decisive missions |

### 13.3 Mission Pool by Port Tier

**Lower Tier Ports** (T1-T3):
- More local missions (single zone operations)
- Focus on defensive and patrol content
- Higher proportion of delivery missions
- Limited combat elimination missions
- Tutorial and training missions available

**Mid Tier Ports** (T4-T5):
- Balanced mission variety
- Multi-zone operations appear
- Convoy escort and protection missions
- Storyline campaign missions unlock
- Fleet coordination missions begin

**Higher Tier Ports** (T6-T8):
- Strategic operations dominate
- Multi-stage complex missions
- Territory control missions
- High-risk deep penetration operations
- Ace hunts and elite bounties

### 13.4 Natural Difficulty Progression

**New Player Path**:
1. Start at T1 port → only see beginner missions
2. Progress to T2-T3 ports → gradual difficulty increase
3. Unlock higher tier ports through reputation → harder missions available
4. Player controls difficulty by choosing where to mission from

**Veteran Player Access**:
- Can return to low-tier ports for relaxed play
- High-tier ports always offer challenge
- No artificial gating beyond port access
- Reputation unlocks port access, not mission difficulty toggles

---

## 14. Squadron & Fleet Missions

### 14.1 Group Mission Philosophy

**Core Design**: Any player can form a group of any size to tackle missions. Group missions exist in the open world alongside solo content.

**Group Types**:
- **Ad-hoc Groups**: 2+ players formed spontaneously, no requirements
- **Guilds**: Formal organizations with structure, benefits, and persistent membership
- **Cross-Nation Groups**: Players from Friendly/Neutral nations can group together

**No Matchmaking**: Players form groups organically and head out when ready.

### 14.2 Group Mission Categories

#### Coordinated Patrols (2-6 Players)
**Objective**: Patrol larger areas with distributed coverage
**Mechanics**:
- Multiple patrol routes assigned (one per ship)
- Bonus for simultaneous completion
- Shared threat response (alert system)
- Combined rewards distributed to all participants

**Variants**:
- **Sector Sweep**: Cover 4-6 zones with different ships
- **Convoy Route Security**: Multiple ships patrol same shipping lane
- **Border Patrol Network**: Coordinated coverage of contested boundaries

**Rewards**: Per-player Credits + Group Completion Bonus (20%)

---

#### Strike Operations (4-12 Players)
**Objective**: Coordinate attack on high-value target
**Mechanics**:
- Primary target requires multiple ships to defeat
- Support objectives (escorts, defenses) assigned to different players
- Timing coordination for maximum effect
- Phase-based objectives

**Variants**:
- **Convoy Destruction**: Coordinated attack on large NPC convoy
- **Installation Assault**: Destroy fortified enemy position
- **Fleet Engagement**: Take on NPC battle group
- **Port Raid**: Strike enemy port facilities (not capture)

**Rewards**: High Credits, Equipment Drops, Reputation, Rare Salvage

---

#### Defense Operations (4-20 Players)
**Objective**: Protect friendly asset from coordinated enemy attack
**Mechanics**:
- Defensive perimeter must be maintained
- Waves of attackers with escalating difficulty
- Bonus for minimal defender losses
- Partial rewards for partial success

**Variants**:
- **Port Defense**: Protect port from NPC fleet attack
- **Convoy Shield**: Escort large convoy through dangerous waters
- **Fleet Anchorage Defense**: Protect friendly ships at anchor
- **Installation Protection**: Defend offshore platform or lighthouse

**Rewards**: Credits, Defense Medals, Module Rewards, Crew XP

---

#### Strategic Operations (10-50+ Players)
**Objective**: Large-scale operations affecting territory or war state
**Mechanics**:
- Multiple simultaneous objectives across wide area
- Role-based assignments (carrier, surface, submarine groups)
- Success/failure affects server-wide territory control
- Requires guild coordination (extremely difficult without)

**Variants**:
- **Beachhead Assault**: Support amphibious landing operations
- **Channel Control**: Dominate strategic waterway
- **Supply Interdiction**: Mass convoy destruction campaign
- **Fleet Action**: Decisive naval battle for territory control

**Rewards**: Massive Credits, Territory Influence, Unique Titles, Historical Recognition

---

### 14.3 Group Reward Distribution

**Equal Distribution** (Default):
- All participants receive equal base rewards
- Bonus pool divided equally
- Simple and fair for casual groups

**Contribution-Based** (Optional for Guilds):
- Damage dealt affects reward share
- Objective completion weighted
- More complex but rewards active participation

**Group Size Scaling**:
- 2-4 players: 100% rewards each
- 5-8 players: 90% rewards each (slight efficiency)
- 9-15 players: 80% rewards each
- 16+ players: 70% rewards each (encourages right-sizing)

### 14.4 Cross-Nation Group Missions

**Allowed When**: Nations are at PEACE or NEUTRAL diplomatic state

**Mechanics**:
- Any nation member can join if diplomatic state allows
- Reputation gains go to each player's home nation
- If diplomatic state changes to WAR during mission:
  - Mission continues but no new cross-nation members
  - No PvP within mission group (temporary cease-fire)
  - Rewards reduced by 50% if completed during war state

**Restrictions**:
- Cannot group with nations at WAR with your nation
- Pirates cannot join national groups (always hostile)
- Nation-specific missions cannot be cross-nation

---

## 15. Ship-Class Specific Missions

### 15.1 Submarine Missions

**Availability**: Unlocks at T4 Submarine (requires destroyer experience first)

#### Silent Patrol
**Objective**: Patrol hostile waters without detection
**Mechanics**:
- Navigate through enemy-patrolled zones submerged
- Detection = mission failure
- Mark enemy positions using periscope (brief surfacing)
- Time limit on battery/oxygen forces surface intervals

**Success Criteria**:
- Complete patrol route undetected
- Mark 3+ enemy positions
- Return to port without being engaged

**Rewards**: Intelligence Reputation, Stealth Bonuses, Credits

---

#### Convoy Interdiction (Wolf Pack)
**Objective**: Destroy convoy ships from torpedo ambush
**Mechanics**:
- Convoy route provided (estimated time/location)
- Position for optimal torpedo attack
- Multiple attack runs possible with reload time
- Escorts will hunt if detected

**Variants**:
- **Solo Hunt**: Single submarine vs small convoy
- **Wolf Pack** (2-4 subs): Coordinated multi-angle attack
- **Fleet Submarine Support**: Submarines support surface fleet attack

**Rewards**: Credits per tonnage sunk, Submarine Ace Reputation

---

#### Deep Reconnaissance
**Objective**: Gather intelligence in heavily defended waters
**Mechanics**:
- Navigate to fortified enemy position
- Observe and record ship movements (periscope)
- Photograph installations (periscope module)
- Escape without detection

**Rewards**: Intelligence Credits, Map Reveals, Strategic Information

---

#### Minelaying Operations
**Objective**: Deploy mines in enemy shipping lanes
**Mechanics**:
- Carry mine payload (reduces torpedoes)
- Navigate to designated minelaying zone
- Deploy mines while submerged (slow process)
- Extract before patrol discovers

**Rewards**: Credits per mine deployed, Bonus for ships sunk by mines (delayed)

---

#### Rescue Operations
**Objective**: Recover personnel from dangerous waters
**Mechanics**:
- Navigate to crash/sinking site
- Surface to recover survivors
- Vulnerable while surfaced
- Transport survivors to friendly port

**Targets**:
- Downed pilots from carrier battles
- Survivors from sunk friendly ships
- Stranded operatives/agents
- Escaped prisoners of war

**Rewards**: Rescue Commendation, Humanitarian Reputation, Crew (sometimes)

---

### 15.2 Carrier Missions

**Availability**: Unlocks after Sims-Class Destroyer research

#### Combat Air Patrol (CAP)
**Objective**: Maintain fighter coverage over friendly fleet/area
**Mechanics**:
- Launch and maintain fighter patrols
- Intercept incoming enemy aircraft
- Rotate squadrons to maintain coverage
- Duration-based success

**Rewards**: Air Defense Reputation, Credits, Aircraft XP

---

#### Strike Package Delivery
**Objective**: Launch coordinated air strike on enemy target
**Mechanics**:
- Plan strike package (bombers + fighter escort)
- Navigate carrier to launch range
- Execute strike on target
- Recover aircraft (losses affect rewards)

**Targets**:
- Enemy carrier (high difficulty)
- Surface fleet concentrations
- Port installations
- Coastal defenses

**Rewards**: High Credits, Strike Reputation, Equipment

---

#### Search and Destroy
**Objective**: Locate and destroy enemy fleet using carrier air power
**Mechanics**:
- Launch scout aircraft to search zones
- Locate enemy fleet position
- Launch strike before enemy escapes
- Success requires finding AND destroying

**Rewards**: Fleet Destruction Bonus, Intelligence Reputation

---

#### Fleet Air Defense
**Objective**: Protect friendly fleet from enemy air attack
**Mechanics**:
- Maintain CAP over protected fleet
- Scramble additional fighters when attack detected
- Coordinate with friendly AA fire
- Success measured by friendly ships surviving

**Rewards**: Defense Credits, Fleet Protection Medal

---

#### Aircraft Ferry
**Objective**: Transport aircraft to distant friendly carrier/base
**Mechanics**:
- Load aircraft at origin (special cargo)
- Navigate to destination
- Deliver aircraft safely
- Bonus for no losses

**Rewards**: Logistics Credits, Ferry Pilot Reputation

---

### 15.3 Destroyer Missions

#### Anti-Submarine Warfare (ASW)
**Objective**: Hunt and destroy enemy submarines
**Mechanics**:
- Patrol area with active sonar
- Detect submarine contacts
- Attack with depth charges
- Confirm kill

**Variants**:
- **Hunter-Killer**: Solo ASW patrol
- **Screen Duty**: Protect larger ships from sub threat
- **Sub Hunter Pack** (2-4 DDs): Coordinated ASW sweep

**Rewards**: ASW Reputation, Submarine bounties, Credits

---

#### Torpedo Attack Run
**Objective**: Close with enemy capital ships for torpedo attack
**Mechanics**:
- Approach enemy formation
- Survive defensive fire
- Launch torpedoes at optimal range
- Extract before destruction

**High Risk/Reward**:
- Destroyers are fragile vs capital ships
- Successful torpedo hit = massive damage
- Glory or death mission profile

**Rewards**: High Credits if successful, Combat Reputation

---

### 15.4 Capital Ship Missions

#### Bombardment Support
**Objective**: Provide gunfire support for ground operations
**Mechanics**:
- Navigate to bombardment position
- Engage designated shore targets
- Maintain station under fire
- Complete fire missions

**Rewards**: Support Credits, Bombardment Reputation

---

#### Fleet Flagship
**Objective**: Lead fleet formation in major engagement
**Mechanics**:
- Serve as command ship for NPC fleet
- Direct fleet movements (limited AI commands)
- Engage enemy fleet
- Success = fleet objective completion

**Rewards**: Command Reputation, High Credits, Leadership Medals

---

## 16. Pirate & Outlaw Missions

### 16.1 The Fallen Captain Path

**Core Design**: Players cannot START as pirates. They must "fall" to pirate status through criminal actions that damage their reputation with their home nation.

**Becoming an Outlaw**:
1. **Warning Phase** (-25 to -49 reputation with home nation):
   - Warning messages about criminal status
   - Reduced services at home nation ports
   - Bounty system becomes active against you

2. **Outlaw Phase** (-50 to -74 reputation):
   - Barred from most home nation ports
   - Pirate contacts become available
   - Access to pirate missions
   - Can still dock at neutral ports

3. **Full Pirate** (-75 or lower with ALL nations):
   - Hostile with all national ports
   - Full access to pirate haven
   - All pirate missions available
   - "Pirate Lord" progression path

### 16.2 Pirate Haven & Ports

**The Pirate Haven**: Central lawless port accessible to all players
- Located in neutral waters (map corner)
- No national affiliation
- All services available (at premium prices)
- Pirate mission board

**Pirate Outposts**: Smaller pirate ports scattered in each theater
- Located in remote areas
- Basic services only
- Local pirate missions
- Temporary refuge for outlaws

### 16.3 Pirate Mission Types

#### Raid Missions
**Objective**: Attack and loot merchant vessels
**Mechanics**:
- Hunt merchant convoys in designated area
- Disable and board ships (not sink - capture cargo)
- Escape before navy response
- Sell loot at pirate port

**Variants**:
- **Merchant Hunter**: Solo raiding operations
- **Convoy Ambush**: Coordinated pirate fleet attack
- **Port Raid**: Strike weakly defended port facilities

**Rewards**: Stolen Cargo (varies), Pirate Reputation

---

#### Smuggling Operations
**Objective**: Transport contraband between ports
**Mechanics**:
- Pick up illegal cargo at pirate/neutral port
- Navigate through patrolled waters undetected
- Deliver to black market contact
- Avoid customs inspection

**Contraband Types**:
- Weapons (selling to enemies)
- Restricted technology
- Stolen goods
- Banned substances

**Rewards**: High Credits, Underworld Reputation

---

#### Blockade Running
**Objective**: Break through naval blockade with cargo
**Mechanics**:
- Cargo must reach blockaded port
- Navigate through enemy fleet cordon
- Speed and evasion prioritized
- Combat discouraged (risk cargo)

**Rewards**: Blockade Runner Reputation, Premium Delivery Fee

---

#### Pirate Lord Bounties
**Objective**: Eliminate rival pirate captains
**Mechanics**:
- Target: Another pirate NPC or player
- Information on target's habits/locations
- Must personally eliminate
- Claim their territory/reputation

**Rewards**: Pirate Authority, Territory Control, Credits

---

#### Protection Racket
**Objective**: "Protect" NPC merchants for payment
**Mechanics**:
- Establish presence in shipping lane
- NPC merchants pay "protection" fee
- Actually protect them from other pirates/NPCs
- Failure to protect = no payment

**Rewards**: Regular Credits (passive), Underworld Reputation

---

### 16.4 Redemption Path

**Returning to Legitimate Status**:
- Complete anti-piracy missions (ironic but effective)
- Pay "amnesty" fee to nation (expensive)
- Complete special "redemption" mission chain
- Reputation slowly rebuilds over time

**Amnesty Costs**:
- Minor Outlaw (-25 to -49): 10,000 Credits
- Full Outlaw (-50 to -74): 50,000 Credits
- Pirate (-75 to -89): 200,000 Credits + mission chain
- Pirate Lord (-90 to -100): 500,000 Credits + lengthy mission chain

**Permanent Record**: Even after redemption, some nations may remember your past (reduced max reputation cap with affected nations).

---

## 17. Tutorial & New Captain Missions

### 17.1 Tutorial Philosophy

**Design Principle**: Tutorial happens IN the main world, not a separate instance. New players experience the real game from moment one - just like Escape from Tarkov.

**Sink or Swim**:
- No hand-holding or protected zones
- Real rewards from tutorial missions
- Real risks (though T1-T5 have no permadeath)
- Learning through doing and failing

### 17.2 New Captain Mission Chain

These missions are available at T1 ports and designed to teach core mechanics:

#### Mission 1: First Voyage
**Objective**: Successfully undock and return to port
**Teaches**: Basic navigation, port docking, extraction concept
**Mechanics**:
- Undock from starting port
- Navigate to nearby waypoint
- Return to any friendly port
**Reward**: 100 Credits, "Sea Legs" achievement

---

#### Mission 2: Navigation Basics
**Objective**: Visit 3 locations and return
**Teaches**: Map reading, waypoints, fuel management
**Mechanics**:
- Visit Waypoint A, B, C in order
- Monitor fuel consumption
- Return before running out
**Reward**: 150 Credits, Navigation Chart

---

#### Mission 3: First Contact
**Objective**: Detect and observe enemy ship without engaging
**Teaches**: Radar/spotting, threat assessment, avoiding combat
**Mechanics**:
- Locate NPC patrol ship
- Approach within observation range
- Identify ship type
- Escape without being targeted
**Reward**: 200 Credits, Binoculars Module

---

#### Mission 4: First Blood
**Objective**: Engage and sink enemy vessel
**Teaches**: Combat basics, weapon systems, damage
**Mechanics**:
- Engage designated NPC target (weak T1 ship)
- Sink the target
- Survive the engagement
**Reward**: 300 Credits, Basic Ammunition Pack

---

#### Mission 5: Spoils of War
**Objective**: Salvage cargo from defeated enemy
**Teaches**: Looting, cargo space, inventory management
**Mechanics**:
- Defeat enemy ship
- Approach wreckage
- Collect floating cargo
- Return to port with cargo
**Reward**: 400 Credits + salvaged cargo value

---

#### Mission 6: The Trade Route
**Objective**: Complete a delivery mission
**Teaches**: Trade missions, cargo transport, route planning
**Mechanics**:
- Accept cargo at Port A
- Deliver to Port B
- Time limit (generous)
**Reward**: 350 Credits, Merchant contact unlocked

---

#### Mission 7: Under Fire
**Objective**: Take damage and perform emergency repairs
**Teaches**: Damage control, repair mechanics, crew assignments
**Mechanics**:
- Intentionally take damage from weak enemy
- Use repair supplies to fix damage
- Return to port
**Reward**: 300 Credits, Repair Kit

---

#### Mission 8: Crew Management
**Objective**: Assign crew to stations and observe effects
**Teaches**: Crew system, station assignments, skill bonuses
**Mechanics**:
- Assign crew to specific stations
- Complete simple task showing crew benefit
- Understand crew XP gain
**Reward**: 400 Credits, Recruit Crew Card

---

#### Mission 9: Upgrade Path
**Objective**: Install a module on your ship
**Teaches**: Module system, fitting, weight management
**Mechanics**:
- Purchase or receive module
- Install at port
- Use module in combat/navigation
**Reward**: 500 Credits, Basic Module

---

#### Mission 10: Graduation
**Objective**: Complete multi-stage operation combining all skills
**Teaches**: Full gameplay loop integration
**Mechanics**:
- Navigate to target zone
- Defeat enemy patrol
- Salvage valuable cargo
- Avoid stronger NPC patrol
- Return to port
**Reward**: 1,000 Credits, "New Captain" Title, T2 Port Access

---

### 17.3 Ongoing Onboarding

**Feature Unlock Tutorials**: As players progress, new tutorial missions appear when features unlock:

| Feature Unlock | Tutorial Mission |
|----------------|------------------|
| T4 Destroyer (Submarine access) | "Introduction to the Deep" - Basic submarine ops |
| Carrier Research | "Wings of the Fleet" - Carrier tutorial chain |
| First T6 Ship | "High Stakes" - Permadeath awareness mission |
| Radar Module | "Electronic Eyes" - Radar operation tutorial |
| Reputation threshold | "Political Awareness" - Diplomacy tutorial |

**No Forced Tutorials**: All tutorials are missions - players can skip them but miss rewards.

---

## 18. Territory & War Missions

### 18.1 Territory Control System

**Controlled Areas**:
- Core national territory (never changes hands)
- Fringe ports (can change control)
- Resource outposts (can change control)
- Staging points (NPC fleet bases, separate from player ports)

**Area of Influence**: Each port/outpost has visible influence radius on map showing "war boundaries."

### 18.2 How Territory Changes

**Influence Points**: Each controlled area has an influence score (0-1000)
- Starts at 500 (neutral control)
- >750 = Controlled by Nation A
- <250 = Controlled by Nation B
- 250-750 = Contested

**Player Actions Affecting Influence**:

| Action | Influence Change |
|--------|------------------|
| Sink enemy player ship in zone | +5 toward your nation |
| Sink enemy NPC patrol in zone | +2 toward your nation |
| Complete mission in zone | +3 toward your nation |
| Raid enemy convoy in zone | +10 toward your nation |
| Lose your ship in zone | -3 toward your nation |
| Failed mission in zone | -2 toward your nation |

### 18.3 Territory Mission Types

#### Zone Influence Operations
**Objective**: Shift control toward your nation
**Mechanics**:
- Operate in contested zone
- Complete sub-objectives (patrols, eliminations, escorts)
- Cumulative influence gain
- Success = zone shifts toward your nation

**Variants**:
- **Zone Patrol**: Maintain presence in contested area
- **Convoy Protection**: Defend friendly convoys in zone
- **Convoy Raiding**: Attack enemy convoys in zone
- **Port Blockade**: Prevent enemy port operations

**Rewards**: Credits, War Reputation, Territory Medals

---

#### Strategic Target Destruction
**Objective**: Destroy key enemy installation affecting zone control
**Mechanics**:
- Target: Coastal defense, radar station, supply depot
- Heavy defenses require planning
- Success causes large influence swing (+50-100)
- Respawns after time period

**Rewards**: High Credits, Strategic Commendation, Zone Control Bonus

---

#### Supply Line Interdiction
**Objective**: Cut enemy supply routes to weaken zone control
**Mechanics**:
- Destroy X supply convoys along route
- Each convoy destroyed weakens enemy influence
- Cumulative mission (tracks over time)
- Complete when supply threshold met

**Rewards**: Interdiction Medal, Credits per convoy, Influence bonus

---

#### Outpost Assault
**Objective**: Participate in capture of enemy outpost
**Mechanics**:
- Large-scale operation (10+ players typical)
- Multiple objectives (destroy defenses, sink garrison, capture point)
- Success flips outpost control
- Failure results in casualties and cooldown

**Rewards**: Massive Credits, Territory Control, Unique Titles

---

### 18.4 Political Tension System

**Actions Create Tension**: Even during PEACE, player actions create diplomatic tension:

| Action | Tension Effect |
|--------|---------------|
| Sink enemy nation ship | +1 Tension, -10 Rep with enemy, -5 Rep with home nation* |
| Raid enemy convoy | +2 Tension, -15 Rep with enemy |
| Complete anti-enemy mission | +0.5 Tension |
| Trade with enemy | -0.5 Tension |
| Complete joint mission with ally | -1 Tension |

*Home nation loses rep because they didn't authorize the attack

**Tension Thresholds**:
- 0-25: Peace (normal relations)
- 26-50: Strained (reduced cooperation)
- 51-75: Hostile (preparing for war)
- 76-100: WAR (diplomatic state changes)

**NPC Nations React**: When tension rises, NPC nation decides:
- "Worth going to war?" (based on military/economic factors)
- May declare war even if one player caused all tension
- Players can intentionally cause wars through provocation

### 18.5 Port Access After Control Change

**When Port Changes Hands**:
- Players of losing nation lose access immediately
- Inventory stored at port is NOT lost (inaccessible until recapture)
- Alternative: Pay smugglers to extract inventory (expensive, risky)
- Port services now serve new controlling nation

---

## 19. Crew Training Missions

### 19.1 Training Mission Philosophy

**Purpose**: Missions designed specifically to level crew skills efficiently while providing useful gameplay.

**XP Bonus**: Training missions provide +50% crew XP compared to normal missions.

### 19.2 Skill-Specific Training Missions

#### Gunnery Training
**Objective**: Destroy target ships using specific weapon tactics
**Teaches/Trains**: Gunnery skill, accuracy, reload speed
**Mechanics**:
- Target practice against weak NPCs
- Score based on accuracy, hits, damage
- Chain multiple engagements

**XP Bonus**: Gunnery skill +50% XP
**Rewards**: Credits, Gunnery Training Manual (consumable XP item)

---

#### Engineering Drills
**Objective**: Maintain ship under stress conditions
**Teaches/Trains**: Engineering skill, efficiency, repair speed
**Mechanics**:
- Complete voyage with intentional ship degradation
- Manage power distribution
- Execute emergency repairs
- Optimize fuel consumption

**XP Bonus**: Engineering skill +50% XP
**Rewards**: Credits, Engineering Certification

---

#### Damage Control Exercises
**Objective**: Survive heavy damage and perform repairs
**Teaches/Trains**: Damage Control skill, crew survival, fire fighting
**Mechanics**:
- Engage enemies, deliberately take damage
- Manage multiple damage types (fire, flooding, structural)
- Keep ship operational throughout
- Complete mission without sinking

**XP Bonus**: Damage Control skill +50% XP
**Rewards**: Credits, DC Equipment

---

#### Navigation Certification
**Objective**: Complete complex navigation challenge
**Teaches/Trains**: Navigation skill, fuel efficiency, route planning
**Mechanics**:
- Navigate through hazardous waters
- Visit multiple checkpoints in order
- Time pressure but fuel limited
- Weather complications

**XP Bonus**: Navigation skill +50% XP
**Rewards**: Credits, Advanced Charts

---

#### Combat Maneuvers
**Objective**: Execute specific tactical maneuvers in combat
**Teaches/Trains**: Evasion skill, positioning, tactical awareness
**Mechanics**:
- Face superior enemy
- Use cover, positioning, and maneuver to survive
- Complete specific tactical objectives (crossing T, torpedo evasion, etc.)
- Escape successfully

**XP Bonus**: Tactics skill +50% XP
**Rewards**: Credits, Tactics Handbook

---

#### AA Defense Training
**Objective**: Defend against air attack
**Teaches/Trains**: AA Gunnery skill, aircraft tracking, defensive positioning
**Mechanics**:
- Survive waves of attacking aircraft
- Score based on aircraft destroyed
- Protect designated target (optional)

**XP Bonus**: AA Gunnery skill +50% XP
**Rewards**: Credits, AA Equipment

---

### 19.3 Leadership Training (Captain XP)

#### Command School
**Objective**: Lead multi-ship formation in operation
**Teaches/Trains**: Captain leadership abilities
**Mechanics**:
- Command 2-4 NPC escort ships
- Direct formation through combat
- Protect or attack with coordinated action
- Success based on fleet performance

**XP Bonus**: Captain XP +100% (rare)
**Rewards**: Command Medal, Leadership Manual

---

### 19.4 Training Mission Availability

**Location**: All ports have basic training missions
**Advanced Training**: Higher-tier ports offer advanced skill training
**Cooldowns**: Each training mission has 24-hour cooldown per character
**Prerequisites**: Some training requires minimum skill level (can't train Advanced Gunnery until Basic Gunnery level 5)

---

## 20. Future Enhancements

### 20.1 Player-Created Missions (Post-Launch)

**Concept**: Players can create bounties and contracts for other players
- Post bounty on enemy player (costs credits)
- Create cargo contract (player-to-player delivery)
- Form escort requests (hire protection)
- Guild contracts (recurring missions for guild members)

### 20.2 Dynamic War Campaigns (Post-Launch)

**Concept**: Server-wide narrative campaigns affecting all players
- Month-long operations with persistent progress
- Daily mission contributions affect campaign outcome
- Historical battles recreated with player participation
- Server-unique outcomes creating divergent histories

### 20.3 Legendary Mission Chains (Post-Launch)

**Concept**: Epic multi-session quest lines for dedicated players
- 20-50 mission chains spanning months
- Narrative-driven with unique characters
- Exclusive rewards (unique ships, titles, abilities)
- Account-bound (not tradeable)

---

## 21. Cross-References

- [[Extraction-Mechanics]] - Core gameplay loop missions enhance
- [[Reputation-System]] - Standing requirements and rewards
- [[Economy-Overview]] - Economic impact of missions
- [[Port-Locations]] - Where mission boards are located
- [[Zone-System]] - Difficulty zones affecting mission placement
- [[Combat-Overview]] - Combat mission mechanics
- [[Crew-Progression]] - XP rewards for crew
- [[Submarine-Warfare]] - Submarine mission mechanics
- [[Carrier-Operations]] - Carrier mission mechanics
- [[Diplomacy-States]] - Territory and war state mechanics
- [[Nation-Overview]] - Pirate faction and national relations

---

## 22. Research Sources

This mission system design draws from analysis of:
- [Escape from Tarkov Task System](https://escapefromtarkov.fandom.com/wiki/Quests) - Quest structure, trader reputation, elimination/pickup/discover types
- [World of Warships Combat Missions](https://worldofwarships.com/en/news/game-guides/combat-missions-made-clear/) - Daily challenges, event missions, directive chains
- [EVE Online Agent Missions](https://wiki.eveuniversity.org/Missions) - Agent levels, security/distribution/mining types, storyline missions
- [Sea of Thieves Voyages](https://seaofthieves.wiki.gg/wiki/Voyages) - Trading company structure, voyage types, reputation tracks
- [Hunt: Showdown Contracts](https://huntshowdown.fandom.com/wiki/Game_Modes) - Bounty extraction mechanics, PvPvE integration
- [War Thunder Events](https://wiki.warthunder.com/mechanics/944-regular-events) - Research point systems, daily/special tasks
- [MMO Quest Design Theory](https://www.gamedeveloper.com/design/7-mmo-quest-types-and-how-to-use-them) - Kill/escort/gather/delivery quest archetypes

---

## Changelog
- **2025-12-03**: Initial document creation - comprehensive mission system design
- **2025-12-03**: Major expansion adding:
  - Section 13: Port-Tier Difficulty System
  - Section 14: Squadron & Fleet Missions
  - Section 15: Ship-Class Specific Missions (Submarine, Carrier, Destroyer, Capital)
  - Section 16: Pirate & Outlaw Missions (Fallen Captain path)
  - Section 17: Tutorial & New Captain Missions
  - Section 18: Territory & War Missions
  - Section 19: Crew Training Missions
  - Removed battle pass/premium currency references (single currency: Credits only)
