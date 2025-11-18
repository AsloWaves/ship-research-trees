---
tags: [planned, phase2, world-design, geography]
status: 📋 PLANNED
phase: Phase 2
priority: MEDIUM-HIGH
last-updated: 2025-11-17
---

# Map Layout

## Overview
The Map Layout defines the geographic structure of the game world, covering four major naval theaters (Pacific, Atlantic, Mediterranean, and Arctic) based on WWII operational areas. The world is a massive, seamless ocean environment with authentic distances, realistic geography, and historically-inspired strategic locations. The layout supports 300+ players per theater through distributed zones and prevents overcrowding via load balancing.

**Core Philosophy**: Geographical authenticity creates strategic depth, where real naval doctrine and historical tactics remain relevant.

## Implementation Status
**Status**: 📋 PLANNED
**Phase**: Phase 2 (World Building)
**Dependencies**: [[Ocean-Environment]], [[Zone-System]], [[Port-Locations]]
**Priority**: MEDIUM-HIGH - Foundation for all naval operations

---

## Design Specification

### Global Map Framework

#### World Scale
- **World Type**: Massive ocean-based world inspired by WWII Pacific and Atlantic theaters
- **Geographic Accuracy**: Based on historical naval operational areas with gameplay modifications
- **Scale Factor**: 1:10 scale (10 Unity units = 1 real kilometer)
  - Real-world distances compressed for gameplay
  - Travel times balanced for 2-4 hour play sessions
- **Seamless World**: No loading screens between regions, fully persistent

#### World Structure
```
Total World Coverage: ~150 million km² (compressed)
- Pacific Theater: 60 million km²
- Atlantic Theater: 50 million km²
- Mediterranean Theater: 20 million km²
- Arctic Theater: 20 million km²
```

#### Population Management
- **300+ Players per Theater**: Each theater supports independent player populations
- **Dynamic Load Balancing**: Players distributed across active operational areas
- **Instanced High-Value Areas**: Critical locations support multiple simultaneous operations
- **Persistent World Continuity**: Player actions affect persistent world state across all theaters

---

## Pacific Theater

### Overview
**Theme**: Vast distances, carrier warfare, island hopping
**Primary Nations**: USA vs. Japan
**Size**: Largest theater, 60% of total game world

### Strategic Locations

#### USA-Controlled Territory

**Pearl Harbor (Hawaii)**
- **Location**: Central Pacific (21.3°N, 157.9°W)
- **Area Type**: Core National Waters
- **Facilities**:
  - Advanced carrier repair facilities
  - Submarine base
  - Battleship drydocks
  - Aviation fuel depot
  - Major supply depot
- **Strategic Value**: USA Pacific command center, staging point for all Pacific operations
- **Player Services**: Full T1-T10 ship construction, advanced module installation
- **NPC Presence**: Overwhelming fleet presence (20+ battleships, 10+ carriers)

**Midway Island**
- **Location**: North Pacific (28.2°N, 177.4°W)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Forward refueling station
  - Basic repair facilities
  - Early warning radar
  - Airfield (patrol aircraft)
- **Strategic Value**: Critical refueling point, early warning station against Japanese expansion
- **Player Services**: Basic resupply, limited repairs (up to T6 ships)
- **NPC Presence**: Regular destroyer patrols, occasional cruiser presence

**Wake Island**
- **Location**: Central Pacific (19.3°N, 166.6°E)
- **Zone Tier**: T2 (Contested Border Waters)
- **Facilities**:
  - Forward operating base
  - Contested supply depot
  - Temporary repair facilities
- **Strategic Value**: Frontline base, high-value contested territory
- **Player Services**: Forward supply point, contested port (can change hands)
- **NPC Presence**: Mixed USA/Japan presence, constant combat

**Guadalcanal**
- **Location**: Solomon Islands (9.5°S, 160.2°E)
- **Zone Tier**: T2 (Contested Border Waters)
- **Facilities**:
  - Resource-rich supply base
  - Critical airfield (Henderson Field)
  - Basic repair facilities
- **Strategic Value**: Resource extraction site, controls Solomon Islands approach
- **Player Services**: Rare material access, forward base for southern Pacific operations
- **NPC Presence**: Heavy combat zone, frequent fleet actions

#### Japan-Controlled Territory

**Tokyo Bay (Japan Home Islands)**
- **Location**: Western Pacific (35.7°N, 139.8°E)
- **Area Type**: Core National Waters
- **Facilities**:
  - Japanese naval headquarters
  - Advanced shipbuilding yards
  - Super-battleship construction facilities
  - Submarine pens
  - Aviation development centers
- **Strategic Value**: Japan's naval command center, untouchable core territory
- **Player Services**: Full T1-T10 ship construction, experimental Japanese modules
- **NPC Presence**: Overwhelming fleet presence (Combined Fleet anchorage)

**Truk Lagoon (Chuuk)**
- **Location**: Caroline Islands (7.4°N, 151.9°E)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Massive fleet anchorage
  - Forward repair facilities
  - Submarine base
  - Supply depot
- **Strategic Value**: "Gibraltar of the Pacific", forward operating base for Japan
- **Player Services**: Full resupply, carrier repairs, forward staging area
- **NPC Presence**: Major fleet anchorage (battleships, carriers, cruisers)

**Rabaul (New Britain)**
- **Location**: Bismarck Archipelago (4.2°S, 152.2°E)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Major air base
  - Submarine base
  - Forward repair facilities
- **Strategic Value**: Controls Bismarck Archipelago, staging point for Solomon Islands operations
- **Player Services**: Forward resupply, submarine operations
- **NPC Presence**: Heavy air and submarine presence

**Okinawa**
- **Location**: Ryukyu Islands (26.5°N, 128.0°E)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Forward operating base
  - Supply depot
  - Coastal defenses
- **Strategic Value**: Defensive perimeter for Japan home islands
- **Player Services**: Forward resupply, defensive staging area
- **NPC Presence**: Strong defensive patrols

#### Contested Waters

**Philippine Sea**
- **Location**: Between Philippines and Mariana Islands
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - Critical sea lane between Japan and Southern Resource Area
  - Major carrier battle zone
  - Controls access to Philippines
- **Combat Characteristics**: Large-scale carrier battles, submarine operations
- **Resources**: Uncommon to rare materials
- **NPC Activity**: Frequent convoy battles, carrier task forces

**Coral Sea**
- **Location**: Between Australia and Solomon Islands
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - Controls approach to Australia
  - Critical convoy route
- **Combat Characteristics**: Carrier engagements, surface actions
- **Resources**: Rare materials, strategic shipwrecks
- **NPC Activity**: Major fleet actions

**Marshall Islands**
- **Location**: Central Pacific (5-15°N, 160-175°E)
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - Japanese forward defense perimeter
  - USA advance route toward Japan
- **Combat Characteristics**: Island assaults, carrier raids
- **Resources**: Strategic islands with supply caches
- **NPC Activity**: Amphibious operations, carrier strikes

#### Open Pacific Waters

**Mid-Pacific Void**
- **Location**: Central Pacific between Hawaii and Midway
- **Zone Tier**: T3-T4 (Disputed to International Waters)
- **Strategic Value**:
  - Unrestricted submarine operations
  - High-value convoy routes
- **Combat Characteristics**: Submarine warfare, rare surface encounters
- **Resources**: Very rare deep-sea materials
- **NPC Activity**: Minimal, isolated convoys

**International Date Line**
- **Location**: 180° longitude
- **Zone Tier**: T4 (Deep Ocean International Waters)
- **Strategic Value**:
  - Lawless frontier
  - Rare resource spawns
- **Combat Characteristics**: Unpredictable, free-for-all PvP
- **Resources**: Legendary materials
- **NPC Activity**: None

### Pacific Theater Characteristics

**Vast Distances**
- **Pearl Harbor to Tokyo**: 6,200 km (620 Unity units)
- **Travel Time**: 2-4 hours for destroyers, 1-2 hours for fast cruisers
- **Fuel Management**: Critical for long-range operations
- **Refueling Points**: Midway, Wake Island mandatory stops

**Island Hopping Campaign**
- **Strategic Islands**: Chain of atolls and islands for advancement
- **Capture Mechanics**: Control islands to advance front line
- **Supply Lines**: Each captured island requires supply convoys
- **Progressive Control**: USA advances west, Japan defends perimeter

**Carrier Warfare**
- **Open Ocean**: Perfect environment for carrier task forces
- **Long Detection Ranges**: Open waters favor carriers over battleships
- **Aircraft Dominance**: Air superiority critical in Pacific
- **Carrier Battles**: Large-scale carrier vs. carrier engagements

**Submarine Operations**
- **Deep Waters**: Ideal for submarine warfare
- **Convoy Routes**: Rich target environment for submarines
- **ASW Operations**: Anti-submarine warfare central to Pacific strategy
- **Submarine Bases**: Forward submarine pens support operations

---

## Atlantic Theater

### Overview
**Theme**: Convoy warfare, U-boat operations, weather challenges
**Primary Nations**: UK/USA vs. Germany
**Size**: Second largest theater, 33% of game world

### Strategic Locations

#### USA-Controlled Territory

**New York Harbor (USA)**
- **Location**: East Coast USA (40.7°N, 74.0°W)
- **Area Type**: Core National Waters
- **Facilities**:
  - Industrial shipbuilding center
  - Convoy assembly point
  - Major supply depot
  - Repair yards
- **Strategic Value**: Primary convoy departure point, industrial center
- **Player Services**: Full T1-T10 ship construction, convoy mission staging
- **NPC Presence**: Constant convoy departures, heavy escort presence

**Hampton Roads (Norfolk, Virginia)**
- **Location**: East Coast USA (36.9°N, 76.3°W)
- **Area Type**: Core National Waters
- **Facilities**:
  - US Navy Atlantic Fleet base
  - Carrier operations
  - Submarine base
  - Training facilities
- **Strategic Value**: Atlantic Fleet headquarters, carrier operations center
- **Player Services**: Full carrier support, submarine operations
- **NPC Presence**: Major fleet concentration

#### UK-Controlled Territory

**Scapa Flow (Orkney Islands, Scotland)**
- **Location**: North Atlantic (59.0°N, 3.0°W)
- **Area Type**: Core National Waters
- **Facilities**:
  - Home Fleet anchorage
  - Secure deep-water anchorage
  - Major repair facilities
  - Battleship docks
- **Strategic Value**: Royal Navy command center, most secure anchorage
- **Player Services**: Full T1-T10 ship construction, capital ship repairs
- **NPC Presence**: Overwhelming Home Fleet presence (entire British battle fleet)

**Liverpool (England)**
- **Location**: West Coast England (53.4°N, 3.0°W)
- **Area Type**: Core National Waters
- **Facilities**:
  - Major port and industrial center
  - Convoy assembly point
  - Repair yards
- **Strategic Value**: Primary convoy destination from USA
- **Player Services**: Convoy escort rewards, industrial supply
- **NPC Presence**: Constant convoy arrivals

**Gibraltar (British Overseas Territory)**
- **Location**: Southern Spain (36.1°N, 5.4°W)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Strategic fortress
  - Mediterranean gateway
  - Submarine base
  - Supply depot
- **Strategic Value**: Controls Mediterranean access, critical chokepoint
- **Player Services**: Mediterranean operations staging, forward resupply
- **NPC Presence**: Heavy defensive presence, constant patrols

#### Germany-Controlled Territory

**Kiel Canal (Germany)**
- **Location**: Northern Germany (54.3°N, 10.1°E)
- **Area Type**: Core National Waters
- **Facilities**:
  - U-boat construction pens
  - Baltic Sea access
  - Naval headquarters
  - Submarine academy
- **Strategic Value**: U-boat operations center, Baltic Sea control
- **Player Services**: U-boat construction and upgrades, torpedo development
- **NPC Presence**: U-boat fleet staging area

**Brest (Occupied France)**
- **Location**: Western France (48.4°N, 4.5°W)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Atlantic raiding base
  - Surface fleet operations
  - U-boat pens (reinforced concrete)
  - Repair facilities
- **Strategic Value**: Atlantic raiding staging point, forward base against UK
- **Player Services**: Surface raider support, U-boat forward base
- **NPC Presence**: Battleship/cruiser presence, U-boat patrols

**Wilhelmshaven (Germany)**
- **Location**: North Sea (53.5°N, 8.1°E)
- **Area Type**: Core National Waters
- **Facilities**:
  - Major naval base
  - Battleship construction
  - Naval arsenal
- **Strategic Value**: High Seas Fleet base, North Sea control
- **Player Services**: Capital ship construction, North Sea operations
- **NPC Presence**: Major surface fleet concentration

#### Contested Waters

**Mid-Atlantic Gap**
- **Location**: Central Atlantic (40-50°N, 30-40°W)
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - Beyond air cover range
  - U-boat hunting ground
  - Critical convoy route
- **Combat Characteristics**: Submarine vs. convoy warfare
- **Resources**: Convoy wreckage salvage, rare materials
- **NPC Activity**: Constant convoy battles

**Denmark Strait**
- **Location**: Between Iceland and Greenland (66°N, 27°W)
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - German battleship breakout route
  - Critical chokepoint
  - Weather advantage for raiders
- **Combat Characteristics**: Surface warfare, weather concealment
- **Resources**: Strategic shipwrecks (Bismarck, Hood)
- **NPC Activity**: Capital ship engagements

**Bay of Biscay**
- **Location**: Western France coast (45°N, 5°W)
- **Zone Tier**: T2 (Contested Border Waters)
- **Strategic Value**:
  - U-boat transit route
  - Allied air patrol zone
- **Combat Characteristics**: ASW operations, U-boat hunting
- **Resources**: U-boat wreckage, torpedo technology
- **NPC Activity**: Heavy ASW patrols

**North Sea**
- **Location**: Between UK and Germany
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - Controls access to Germany
  - Channel operations
- **Combat Characteristics**: Destroyer actions, minefield warfare
- **Resources**: Mine warfare equipment
- **NPC Activity**: Constant patrol actions

#### Open Atlantic Waters

**Central Atlantic**
- **Location**: Mid-Atlantic (20-40°N, 40-60°W)
- **Zone Tier**: T3-T4 (Disputed to International)
- **Strategic Value**:
  - Major convoy routes
  - Unrestricted submarine operations
- **Combat Characteristics**: Long-range submarine warfare
- **Resources**: Very rare convoy materials
- **NPC Activity**: Sporadic convoys

**South Atlantic**
- **Location**: Below equator
- **Zone Tier**: T4 (Deep Ocean International Waters)
- **Strategic Value**:
  - Isolated raider operations
  - Rare resource zones
- **Combat Characteristics**: Surface raider vs. merchant
- **Resources**: Legendary materials
- **NPC Activity**: Minimal

### Atlantic Theater Characteristics

**Convoy Warfare**
- **Critical Supply Lines**: UK survival depends on Atlantic convoys
- **Convoy System**: Large escorted merchant formations (20-50 ships)
- **Escort Missions**: Players escort convoys for rewards
- **Interdiction**: German players attack convoys for resources

**U-Boat Operations**
- **Wolf Pack Tactics**: Coordinated submarine attacks
- **U-Boat Alley**: Prime hunting ground in Mid-Atlantic
- **ASW Response**: Allied anti-submarine warfare operations
- **Technology War**: Radar vs. stealth constant evolution

**Weather Systems**
- **North Atlantic Storms**: Harsh weather affects all operations
- **Visibility**: Fog and storms provide tactical concealment
- **Seasonal Variations**: Winter storms increase danger
- **Weather Forecasting**: Meteorological stations provide intelligence

**Chokepoint Control**
- **Denmark Strait**: Battleship breakout route
- **English Channel**: Restricted waters, heavy defenses
- **Iceland-Faroe Gap**: ASW barrier
- **Gibraltar**: Mediterranean access control

---

## Mediterranean Theater

### Overview
**Theme**: Enclosed sea warfare, multi-national complexity, combined operations
**Primary Nations**: UK vs. Italy/Germany
**Size**: Smallest major theater, 13% of game world

### Strategic Locations

#### UK-Controlled Territory

**Malta (British Crown Colony)**
- **Location**: Central Mediterranean (35.9°N, 14.5°E)
- **Area Type**: Protected Territorial Waters - Heavily besieged
- **Facilities**:
  - Fortress island
  - Submarine base
  - Critical convoy waypoint
  - Defensive fortifications
- **Strategic Value**: Strategic pivot point controlling central Mediterranean
- **Player Services**: Submarine operations, forward staging under siege
- **NPC Presence**: Defensive garrison, constant supply convoys

**Alexandria (Egypt)**
- **Location**: Eastern Mediterranean (31.2°N, 29.9°E)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Eastern Mediterranean fleet base
  - Desert campaign supply hub
  - Repair facilities
  - Fuel depot
- **Strategic Value**: Controls eastern Mediterranean, supports North Africa campaign
- **Player Services**: Fleet support, desert warfare equipment
- **NPC Presence**: Mediterranean Fleet concentration

**Gibraltar (British Fortress)**
- **Location**: Mediterranean entrance (36.1°N, 5.4°W)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Strategic fortress
  - Mediterranean gateway
  - Submarine base
  - Aircraft carrier operations
- **Strategic Value**: Controls Mediterranean access from Atlantic
- **Player Services**: Mediterranean entry point, forward operations base
- **NPC Presence**: Force H (carrier battle group)

#### Axis-Controlled Territory

**Taranto (Italy)**
- **Location**: Southern Italy (40.5°N, 17.2°E)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - Italian naval headquarters
  - Major fleet anchorage
  - Battleship base
- **Strategic Value**: Italian Navy command center, controls central Mediterranean
- **Player Services**: Italian ship construction, Mediterranean operations
- **NPC Presence**: Italian battle fleet anchorage

**Toulon (Occupied France)**
- **Location**: Southern France (43.1°N, 5.9°E)
- **Area Type**: Protected Territorial Waters
- **Facilities**:
  - French naval base under Axis control
  - Mediterranean fleet base
  - Submarine pens
- **Strategic Value**: Western Mediterranean control, supports North Africa
- **Player Services**: French ship access, western Mediterranean operations
- **NPC Presence**: Axis fleet presence

**Sicily (Italy)**
- **Location**: Central Mediterranean (37.5°N, 14.0°E)
- **Zone Tier**: T2 (Contested Border Waters)
- **Facilities**:
  - Strategic island
  - Airfields
  - Naval facilities
- **Strategic Value**: Controls central Mediterranean, air superiority base
- **Player Services**: Air operations, forward supply
- **NPC Activity**: Heavy air presence

**Crete (Occupied Greece)**
- **Location**: Eastern Mediterranean (35.2°N, 24.9°E)
- **Zone Tier**: T2 (Contested Border Waters)
- **Facilities**:
  - Contested island
  - Airfields
  - Basic naval facilities
- **Strategic Value**: Controls eastern approaches, air base
- **Player Services**: Forward operations, contested port
- **NPC Activity**: Air and naval patrols

#### Contested Waters

**Central Mediterranean**
- **Location**: Between Sicily and Malta
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Strategic Value**:
  - Critical convoy route to Malta
  - Most contested waters
- **Combat Characteristics**: Surface actions, air strikes, submarine warfare
- **Resources**: Rare materials, shipwreck salvage
- **NPC Activity**: Constant convoy battles

**Sicilian Channel**
- **Location**: Between Sicily and Tunisia
- **Zone Tier**: T2 (Contested Border Waters)
- **Strategic Value**:
  - North Africa supply route
  - Malta resupply corridor
- **Combat Characteristics**: Convoy warfare, air attacks
- **Resources**: North Africa supply caches
- **NPC Activity**: Heavy convoy traffic

**Aegean Sea**
- **Location**: Between Greece and Turkey
- **Zone Tier**: T3 (Disputed Ocean Areas)
- **Strategic Value**:
  - Eastern Mediterranean access
  - Strategic islands
- **Combat Characteristics**: Island warfare, commando raids
- **Resources**: Strategic outpost supplies
- **NPC Activity**: Moderate patrol presence

### Mediterranean Theater Characteristics

**Enclosed Sea Warfare**
- **Limited Maneuvering Space**: Concentrated naval operations
- **Land Proximity**: Shore-based aircraft dominate
- **Chokepoints**: Multiple strategic straits and passages
- **No Retreat**: Limited escape routes from combat

**Multi-National Complexity**
- **Italian Navy**: Primary Axis naval force
- **Vichy French**: Neutral but controlled by Axis
- **German Luftwaffe**: Air superiority focus
- **British Mediterranean Fleet**: Outnumbered but skilled

**Air-Sea Integration**
- **Land-Based Aircraft**: Shore aircraft dominate engagements
- **Carrier Operations**: Limited due to air threat
- **Combined Operations**: Air and sea coordination essential
- **Air Superiority**: Critical for surface operations

**Supply Line Warfare**
- **Malta Convoys**: Critical resupply operations
- **North Africa**: Desert campaign supply routes
- **Italian Supply**: Libya and North Africa support
- **Convoy Battles**: Constant supply line warfare

---

## Arctic Theater

### Overview
**Theme**: Extreme weather, convoy operations, surface warfare
**Primary Nations**: UK/USA vs. Germany (Soviet supply routes)
**Size**: Smallest theater, 13% of game world

### Strategic Locations

**Murmansk (Soviet Union)**
- **Location**: Arctic Russia (68.9°N, 33.1°E)
- **Area Type**: Protected Territorial Waters - Neutral but critical
- **Facilities**:
  - Ice-free Arctic port
  - Convoy destination
  - Soviet Northern Fleet base
- **Strategic Value**: Lend-Lease supply destination, only ice-free Arctic port
- **Player Services**: Convoy rewards, Arctic supply access
- **NPC Presence**: Soviet defensive presence

**Scapa Flow (UK)**
- **Location**: Orkney Islands (59.0°N, 3.0°W)
- **Area Type**: Core National Waters
- **Facilities**:
  - Convoy departure point
  - Home Fleet base
- **Strategic Value**: Staging area for Arctic convoys
- **Player Services**: Arctic convoy escort missions
- **NPC Presence**: Home Fleet Arctic convoy escorts

**Bear Island (Norway)**
- **Location**: Barents Sea (74.5°N, 19.0°E)
- **Zone Tier**: T2-T3 (Contested to Disputed)
- **Facilities**:
  - Weather station
  - Early warning post
- **Strategic Value**: Convoy route waypoint, weather intelligence
- **Player Services**: Forward observation post
- **NPC Activity**: Weather patrols, convoy waypoint

**Spitsbergen (Svalbard)**
- **Location**: Arctic Ocean (78.2°N, 15.6°E)
- **Zone Tier**: T3 (Disputed Ocean Areas)
- **Facilities**:
  - Coal mining operations
  - Weather reporting station
  - Strategic observation post
- **Strategic Value**: Arctic operations base, weather intelligence
- **Player Services**: Arctic exploration, extreme weather operations
- **NPC Activity**: Minimal, weather observation

**Jan Mayen Island**
- **Location**: Arctic Ocean (71.0°N, 8.5°W)
- **Zone Tier**: T3 (Disputed Ocean Areas)
- **Facilities**:
  - Meteorological station
  - Radio intercept facility
- **Strategic Value**: Weather forecasting, convoy tracking
- **Player Services**: Intelligence gathering
- **NPC Activity**: Weather patrols

### Arctic Theater Characteristics

**Extreme Weather**
- **Ice Fields**: Seasonal ice coverage blocks passages
- **Polar Night**: Extended darkness provides concealment
- **Storms**: Frequent severe weather affects operations
- **Temperature**: Extreme cold affects crew performance

**Convoy Operations**
- **Lend-Lease Supplies**: Critical supplies to Soviet Union
- **Heavily Escorted**: Large escort forces required
- **High Attrition**: Dangerous convoy routes
- **Strategic Importance**: Maintains Soviet war effort

**Limited Visibility**
- **Fog**: Frequent fog banks provide concealment
- **Storms**: Weather disrupts operations and detection
- **Darkness**: Polar night enables stealth operations
- **Ice**: Ice fields block radar and visibility

**Surface Warfare**
- **German Capital Ships**: Battleships and heavy cruisers hunt convoys
- **Home Fleet Response**: British battleships provide distant cover
- **Destroyer Actions**: Escort vs. destroyer engagements
- **No Carrier Operations**: Weather grounds carrier aircraft

---

## Geographic Features

### Chokepoints and Strategic Straits

**Gibraltar Strait**
- **Width**: 13 km at narrowest
- **Depth**: 300m average
- **Strategic Value**: Mediterranean access control
- **Defenses**: Heavy coastal guns, air patrols, submarine nets

**English Channel**
- **Width**: 34 km at narrowest (Dover Strait)
- **Depth**: 45m average (shallow)
- **Strategic Value**: Invasion route, commerce route
- **Defenses**: Minefields, coastal batteries, constant patrols

**Denmark Strait**
- **Width**: 290 km
- **Depth**: 650m
- **Strategic Value**: Battleship breakout route, weather cover
- **Defenses**: Iceland-based patrols, long-range reconnaissance

**Suez Canal**
- **Length**: 193 km
- **Width**: 200-300m
- **Strategic Value**: Mediterranean-Red Sea connection
- **Defenses**: Heavily defended, controlled passage

**Turkish Straits (Bosporus/Dardanelles)**
- **Width**: 700m-1,200m
- **Depth**: 36-124m
- **Strategic Value**: Black Sea access
- **Defenses**: Neutral Turkey controls passage

### Ocean Depth Features

**Continental Shelves**
- **Depth**: 0-200m
- **Characteristics**: Shallow waters, limited submarine operations
- **Tactical Use**: Mine warfare, coastal defenses, reef navigation

**Deep Ocean Basins**
- **Depth**: 3,000-6,000m
- **Characteristics**: Unrestricted submarine depth
- **Tactical Use**: Submarine hiding, deep-sea resources

**Ocean Trenches**
- **Depth**: 6,000-11,000m
- **Locations**: Pacific (Mariana, Japan Trenches)
- **Tactical Use**: Ultimate submarine depth, legendary resource spawns

**Submarine Canyons**
- **Depth**: Varies, creates channels in continental shelf
- **Characteristics**: Hidden approach routes
- **Tactical Use**: Stealth submarine infiltration

**Seamounts**
- **Depth**: Underwater mountains rising from ocean floor
- **Characteristics**: Navigation hazards, tactical cover
- **Tactical Use**: Ambush points, acoustic interference

### Island Chains

**Pacific Island Chains**
- **Hawaiian Islands**: USA staging area
- **Marshall Islands**: Japanese defensive perimeter
- **Caroline Islands**: Japanese forward bases (Truk)
- **Solomon Islands**: Contested territory (Guadalcanal)
- **Mariana Islands**: Strategic airbase locations

**Atlantic Islands**
- **Azores**: Mid-Atlantic waypoint
- **Iceland**: ASW patrol base
- **Bermuda**: USA forward base
- **Cape Verde**: South Atlantic staging

**Mediterranean Islands**
- **Malta**: Critical fortress island
- **Sicily**: Strategic airbase
- **Crete**: Eastern Mediterranean control
- **Sardinia**: Central Mediterranean position
- **Cyprus**: Eastern outpost

---

## Population Distribution & Load Balancing

### Theater Distribution
**Goal**: Prevent overcrowding, maintain immersive population density

**Theater Capacity**:
- **Pacific**: 300+ players (largest theater)
- **Atlantic**: 300+ players
- **Mediterranean**: 200+ players (smaller theater)
- **Arctic**: 150+ players (specialized theater)

**Dynamic Load Balancing**:
- Players automatically distributed to active operations
- Theater recommendations based on current population
- Incentives to balance populations (mission rewards, resource spawns)

### High-Value Area Instancing
**Problem**: Multiple groups want to do same operation simultaneously

**Solution**: Instanced high-value areas
- **Capital Ship Battles**: Multiple instances of major engagements
- **Port Assaults**: Separate instances for simultaneous operations
- **Critical Missions**: Instance copies for concurrent operations

**Persistent Impact**: Instance results affect main world state
- Successful port assault in instance affects territory control
- Resource extraction affects global resource availability
- Major victories recorded in server history

### Activity Heatmaps
**System**: Real-time visualization of player activity

**Indicators**:
- **Red Zones**: High combat activity (20+ players)
- **Orange Zones**: Moderate activity (10-20 players)
- **Yellow Zones**: Light activity (5-10 players)
- **Blue Zones**: Minimal activity (<5 players)

**Player Tools**:
- View heatmap to find or avoid combat
- Mission generation responds to activity levels
- NPC convoys avoid high-activity zones (or are attracted for contested cargo)

---

## Immersion & Authenticity

### Geographic Authenticity
**Design Philosophy**: Real geography creates real strategic challenges

**Accurate Elements**:
- **Historical Distances**: Realistic travel times between locations
- **Correct Proportions**: Naval bases positioned authentically
- **Strategic Positioning**: Locations placed by historical strategic importance
- **Bathymetric Accuracy**: Ocean depth based on real seafloor mapping

**Gameplay Modifications**:
- **Scale Compression**: 1:10 scale for manageable travel times
- **Strategic Simplification**: Some minor bases omitted for clarity
- **Balanced Resources**: Resource distribution balanced for gameplay

### Cultural Details
**Port Cities**: Authentic national characteristics

**USA Ports**:
- Industrial architecture (New York, Norfolk)
- Modern facilities (1940s era)
- Efficient, organized layouts

**UK Ports**:
- Historic naval architecture (Scapa Flow, Portsmouth)
- Traditional Royal Navy styling
- Fortified defensive positions

**Japan Ports**:
- Japanese naval architecture (Tokyo Bay, Truk)
- Distinctive pagoda-style masts visible on battleships
- Eastern aesthetic details

**Germany Ports**:
- Industrial efficiency (Kiel, Wilhelmshaven)
- Reinforced U-boat pens (Brest)
- Militaristic design

---

## Scale and Distance Reference

### Travel Time Examples
**Assumptions**: Speed = 30 knots (cruiser speed)

| Route | Real Distance | Game Distance | Travel Time |
|-------|---------------|---------------|-------------|
| Pearl Harbor to Tokyo | 6,200 km | 620 units | ~2 hours |
| New York to Liverpool | 5,500 km | 550 units | ~1.8 hours |
| Gibraltar to Alexandria | 3,300 km | 330 units | ~1.1 hours |
| Scapa Flow to Murmansk | 3,000 km | 300 units | ~1 hour |

### Zone Size Reference
**Typical Zone Dimensions**:
- **T0 Zone (Core Waters)**: 50 km radius = 500 unit diameter
- **T1 Zone (Protected Waters)**: 100 km radius = 1000 unit diameter
- **T2 Zone (Contested Waters)**: 200 km radius = 2000 unit diameter
- **T3 Zone (Disputed Waters)**: 300 km radius = 3000 unit diameter
- **T4 Zone (International Waters)**: 500+ km radius = 5000+ unit diameter
- **T5 Zone (Enemy Core)**: 50 km radius = 500 unit diameter

---

## Cross-References

### Related Systems
- [[Zone-System]] - Overlays zone tiers on geographic layout
- [[Port-Locations]] - Detailed port facilities and services
- [[Ocean-Environment]] - Visual representation of map areas
- [[Weather-System]] - Regional weather patterns by geography
- [[Territory-Control]] - Control mechanics for strategic locations
- [[Mission-Generation-System]] - Missions generated based on location

### Related Documents
- [[Biome-System]] - Ocean biomes integrated with geography
- [[Navigation-System]] - Navigation mechanics for travel
- [[Ship-Physics]] - Travel times and fuel consumption
- [[Resource-Distribution]] - Resources tied to geographic locations

---

## Design Decisions

### Why Four Theaters Instead of One Global Map?
**Decision**: Divide world into Pacific, Atlantic, Mediterranean, Arctic theaters

**Reasoning**:
- Prevents player overcrowding in single theater
- Allows 1000+ concurrent players across theaters
- Creates distinct gameplay experiences per theater
- Historical authenticity (real WWII theaters)
- Load balancing and server optimization

### Why 1:10 Scale Compression?
**Decision**: Compress real-world distances to 1:10 scale

**Reasoning**:
- Real-scale travel = 20+ hours Pearl Harbor to Tokyo
- 1:10 scale = 2 hours travel (reasonable for play session)
- Maintains strategic relationships between locations
- Preserves need for fuel management and supply lines
- Balances realism with fun gameplay

### Why Both Seamless World and Instanced Areas?
**Decision**: Hybrid approach with persistent world + instances

**Reasoning**:
- Seamless world creates immersion and emergent encounters
- Instances prevent overcrowding at critical operations
- Best of both worlds: persistent effects + accessible content
- Allows parallel operations without interference
- Maintains world state continuity

### Why Include Arctic Theater?
**Decision**: Add Arctic as fourth theater despite smaller size

**Reasoning**:
- Unique gameplay experience (extreme weather, convoy focus)
- Historical significance (Lend-Lease convoys)
- Provides specialized content for hardcore players
- Different tactical challenges from other theaters
- Balances player population across varied content

---

## Future Enhancements

### Phase 2 Additions
- **Dynamic Coastlines**: Coastal bombardment damages shore installations
- **Port Expansion**: Players can upgrade and expand port facilities
- **Secret Bases**: Hidden player-established bases in remote areas
- **Exploration Rewards**: Undiscovered locations with unique resources

### Phase 3 Additions
- **Seasonal Changes**: Ice coverage changes in Arctic, monsoons affect Pacific
- **Tidal Systems**: Tides affect shallow-water navigation
- **Weather Patterns**: Regional weather systems move across map
- **Dynamic Events**: Historical events recreate famous battles

---

**Status**: 📋 Comprehensive geographic framework ready for implementation
**Dependencies**: Ocean Environment (implemented), Zone System, Port Locations
**Next Steps**: Create detailed map tiles, implement zone boundaries, place port locations
