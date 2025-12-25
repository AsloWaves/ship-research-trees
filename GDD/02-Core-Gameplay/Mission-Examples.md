---
tags: [planned, design, core-gameplay, reference]
status: 📋 PLANNED
phase: Core Development
priority: MEDIUM
last-updated: 2025-12-03
---

# Mission Examples Reference

## Overview

This document provides concrete example missions across all mission categories defined in [[Mission-System]]. Each example includes mission name, tier, objectives, rewards, and narrative context. These examples serve as templates for procedural generation and hand-crafted content.

## Implementation Status
**Status**: 📋 PLANNED - Reference document for mission content
**Phase**: Core Development
**Priority**: MEDIUM - Content examples for development

---

## 1. Combat Missions

### 1.1 Patrol Missions

#### "Dawn Watch" (T2 - Easy)
**Port**: Any T2 Minor Port
**Type**: Sector Patrol
**Description**: Local fishing boats report suspicious activity in the morning hours. Patrol the coastal waters and report any hostile contacts.
**Objectives**:
- Navigate to Waypoint Alpha (5km from port)
- Patrol Grid C-7 for 10 minutes
- Return to port and file report
**Bonus**: Engage any hostiles encountered (+100 Credits per kill)
**Rewards**: 200 Credits, +3 Naval Reputation, 50 Combat XP
**Time Limit**: 45 minutes

---

#### "Shipping Lane Sentinel" (T3 - Normal)
**Port**: Any T3 Regional Port
**Type**: Convoy Route Patrol
**Description**: Merchant vessels along Route 7 have reported increased pirate activity. Maintain presence along the shipping lane to deter attacks.
**Objectives**:
- Travel to Route 7 Start Point
- Patrol waypoints A→B→C→D (12km total)
- Respond to any distress signals
- Complete full patrol route
**Bonus**:
- Save merchant vessel from attack: +500 Credits
- Sink pirate vessel: +200 Credits each
**Rewards**: 650 Credits, +5 Naval Reputation, +3 Merchant Reputation, 100 Combat XP
**Time Limit**: 60 minutes

---

#### "Contested Waters" (T5 - Hard)
**Port**: Capital Ports
**Type**: Border Patrol
**Description**: The frontier with [Enemy Nation] remains tense. Intelligence suggests enemy forces are probing our defensive perimeter. Show the flag and engage any hostile incursions.
**Objectives**:
- Proceed to Border Sector Delta-9
- Establish patrol pattern covering 3 grid squares
- Identify and report all contacts
- Engage hostile warships (T4+ enemy forces expected)
- Maintain patrol for 20 minutes minimum
**Bonus**:
- Sink enemy destroyer: +500 Credits
- Sink enemy cruiser: +1,000 Credits
- No damage taken: +25% reward bonus
**Rewards**: 2,200 Credits, +8 Naval Reputation, 250 Combat XP
**Ship Requirement**: T4-T8
**Time Limit**: 90 minutes

---

#### "Midnight Vigil" (T4 - Moderate)
**Port**: T4 Major Ports
**Type**: Night Patrol
**Description**: Enemy submarines have been spotted operating under cover of darkness. Conduct night patrol operations in Sector Echo.
**Objectives**:
- Depart port after 20:00 game time
- Navigate to Sector Echo without running lights
- Complete patrol circuit (4 waypoints)
- Use active sonar at designated checkpoints
- Return before dawn (06:00)
**Special Conditions**: Reduced visibility, navigation hazard active
**Bonus**: Detect submarine contact: +400 Credits
**Rewards**: 1,100 Credits, +6 Naval Reputation, 150 Combat XP, Night Operations Medal
**Time Limit**: Must complete during night cycle

---

### 1.2 Elimination Missions

#### "Wolfpack Hunters" (T3 - Normal)
**Port**: T3 Regional Ports
**Type**: Convoy Interdiction
**Description**: A small enemy supply convoy has been spotted heading toward their forward operating base. Intercept and destroy before they can reinforce enemy positions.
**Target**:
- 3x Cargo Freighters (T2)
- 2x Patrol Boats (T1)
**Objectives**:
- Intercept convoy in Grid F-4
- Sink all cargo vessels (primary)
- Eliminate escorts (optional)
- Extract to friendly port
**Intelligence**: Convoy travels at 12 knots, estimated arrival at F-4 between 14:00-15:00
**Rewards**: 800 Credits, +5 Combat Reputation, Ammunition Crate (x50 rounds)
**Time Window**: 3-hour availability

---

#### "The Iron Coffin" (T5 - Hard)
**Port**: T5 Capital Ports
**Type**: Warship Elimination
**Description**: Enemy heavy cruiser "Stahlgeist" has been terrorizing our merchant fleet. Naval Command has authorized a strike mission. Sink her.
**Target**:
- Heavy Cruiser "Stahlgeist" (T6 NPC, Elite)
- 2x Destroyer Escorts (T4)
**Objectives**:
- Locate target fleet (last seen Grid H-12)
- Sink the Stahlgeist (primary objective)
- Extract successfully
**Intelligence**: Target has heavy armor, recommend torpedo attack or capital ship engagement
**Special**: Target will attempt to flee if outmatched - pursue and destroy
**Rewards**: 3,500 Credits, +12 Combat Reputation, Rare Module Drop (guaranteed), "Cruiser Killer" Achievement
**Ship Requirement**: T5-T9 recommended
**Failure Consequence**: Mission available again in 24 hours

---

#### "Coastal Thunder" (T4 - Moderate)
**Port**: T4 Major Ports (Coastal)
**Type**: Installation Strike
**Description**: Enemy coastal battery at Point Razor has been shelling our shipping. Neutralize the installation.
**Target**: Coastal Defense Battery (Fixed Installation)
**Defenses**:
- 4x 6" guns (can hit at 8km)
- 2x Patrol Boats (respawn every 5 minutes)
- Minefield (outer approach)
**Objectives**:
- Approach Point Razor
- Destroy gun emplacements (4 targets)
- Destroy ammunition depot (1 target, secondary)
- Extract without being sunk
**Tactical Note**: Attack from the east to avoid minefield. Battery has blind spot at 15° from shore.
**Rewards**: 1,600 Credits, +8 Combat Reputation, Strategic Operations Medal
**Ship Requirement**: T4+ with adequate firepower

---

#### "Blood Money" (T5 - Hard)
**Port**: T5+ Ports (Naval Intelligence)
**Type**: Player Bounty
**Description**: Captain [PlayerName] has been declared an enemy of the state for piracy against civilian vessels. Bring them to justice - permanent.
**Target**: Player Captain [Generated Name] - Last seen near [Location]
**Ship Type**: [Player's actual ship - e.g., "Fletcher-class Destroyer"]
**Crimes**: 15 merchant vessels raided, 3 friendly captains killed
**Bounty**: 5,000 Credits (dead), 7,500 Credits (captured cargo delivered)
**Objectives**:
- Locate target player
- Sink their vessel
- Extract to claim bounty
**Special Rules**:
- Must deliver killing blow (or be in squadron that does)
- No reward if target scuttles
- Target is aware of bounty (they receive notification)
**Rewards**: Bounty payout, +15 Bounty Hunter Reputation, "Manhunter" progress
**Availability**: Until target is eliminated or clears criminal record

---

#### "Ghost of the Pacific" (T6 - Elite)
**Port**: T6 Fleet HQ Ports
**Type**: NPC Ace Hunt
**Description**: The legendary Captain Yamamoto Rei, known as the "Ghost of the Pacific," commands a modified battlecruiser that has sunk over 40 of our vessels. Intelligence has narrowed her hunting grounds. End her reign of terror.
**Target**:
- "Shinigami" (Modified Kongo-class, T8 Boss)
- 2x Elite Destroyer Escorts (T5)
**Known Tactics**:
- Prefers night engagements
- Uses islands for ambush
- Will not engage superior numbers (will flee and return later)
**Location Hints**:
- Operates in Solomon Islands region
- Frequently patrols Grid J-7 through K-9
- Resupplies at hidden anchorage (unknown location)
**Objectives**:
- Hunt and locate the Shinigami
- Sink the Ghost of the Pacific
- Recover her battle flag (proof of kill)
**Rewards**:
- 8,000 Credits
- Unique Module: "Ghost's Optics" (+15% night visibility)
- Title: "Ghostslayer"
- +25 Ace Hunter Reputation
**Recommendation**: 4+ player squadron advised
**Respawn**: 7 days after elimination

---

### 1.3 Defensive Missions

#### "Harbor Guard" (T2 - Easy)
**Port**: T2 Minor Ports
**Type**: Port Defense
**Description**: Intelligence reports a small pirate raid approaching. Defend the harbor until reinforcements arrive.
**Scenario**:
- Wave 1: 3x Pirate Boats (T1) - 2 minutes after start
- Wave 2: 2x Pirate Corvettes (T2) - 5 minutes after start
- Wave 3: 1x Pirate Raider (T3) + 2x Boats - 8 minutes after start
**Objectives**:
- Defend harbor entrance for 12 minutes
- Port facilities must survive above 50% HP
- Sink attacking forces
**Bonus**: Port survives above 80%: +200 Credits
**Rewards**: 350 Credits, +4 Defense Reputation, 75 Combat XP
**Available**: When "Pirate Activity" event is active in region

---

#### "Shepherd's Duty" (T4 - Moderate)
**Port**: T4 Major Ports
**Type**: Convoy Escort (Defense variant)
**Description**: Tanker convoy TK-117 is carrying critical fuel supplies to our forward bases. Enemy forces will attempt to intercept. Protect the convoy at all costs.
**Convoy Composition**:
- 4x Fleet Oilers (T3, slow, very valuable)
- 2x Escort Destroyers (T3 NPC allies)
**Route**: Port of Origin → Waypoint Alpha → Waypoint Beta → Destination (25km)
**Expected Threats**:
- Submarine ambush at Waypoint Alpha
- Surface raiders near Waypoint Beta
- Possible air attack (if carrier operations active)
**Objectives**:
- Escort convoy to destination
- At least 2 oilers must survive
- All 4 oilers survive: Full reward
- 3 oilers survive: 75% reward
- 2 oilers survive: 50% reward
**Rewards**: 1,400 Credits (full), +7 Escort Reputation, Logistics Medal
**Ship Requirement**: T3-T7
**Time Limit**: Route should take 45-60 minutes

---

#### "Hold the Line" (T6 - Elite)
**Port**: T6 Fleet HQ
**Type**: Installation Defense
**Description**: Forward Operating Base Trident is under sustained enemy assault. Reinforce the defenders and hold until the main fleet arrives.
**Installation**: FOB Trident (Offshore Platform)
- 6 defensive gun positions
- Radar installation
- Supply depot
**Assault Force**:
- Phase 1: 4x Destroyers, 6x Patrol Boats (20 minutes)
- Phase 2: 2x Cruisers, 4x Destroyers (15 minutes)
- Phase 3: 1x Battleship, 2x Cruisers, 4x Destroyers (25 minutes)
**Objectives**:
- Defend FOB Trident for 60 minutes
- Installation must survive above 25% HP
- Survive all three assault phases
**Victory Conditions**:
- Total Victory (FOB > 75%): 6,000 Credits, Elite Defense Medal
- Victory (FOB > 50%): 4,000 Credits, Defense Medal
- Pyrrhic Victory (FOB > 25%): 2,500 Credits
- Defeat (FOB < 25%): Mission Failed
**Rewards**: See Victory Conditions, +15 Defense Reputation
**Recommendation**: Squadron of 6+ players
**Availability**: Appears during "Enemy Offensive" events

---

## 2. Delivery Missions

### 2.1 Cargo Transport

#### "Fresh Catch" (T1 - Beginner)
**Port**: T1 Starter Ports
**Type**: Standard Freight
**Description**: The fishermen's cooperative needs their catch delivered to the mainland market before it spoils.
**Cargo**: Fresh Fish (50 tons, perishable)
**Route**: Starter Port → Regional Market (8km)
**Objectives**:
- Load cargo at dock
- Deliver to destination within 2 hours
- Cargo must arrive above 80% condition
**Hazards**: Minimal (T1 waters, light traffic)
**Rewards**: 75 Credits, +2 Merchant Reputation, 25 Trade XP
**Cargo Space Required**: 50 tons minimum

---

#### "Medical Emergency" (T3 - Normal)
**Port**: T3 Regional Ports
**Type**: Perishable Cargo (Time Critical)
**Description**: Outbreak of illness at remote island settlement. Medical supplies desperately needed.
**Cargo**: Medical Supplies (30 tons, fragile, time-critical)
**Route**: Regional Hospital Port → Island Settlement (18km through contested waters)
**Time Limit**: 45 minutes (real-time)
**Objectives**:
- Load medical cargo
- Deliver within time limit
- Cargo must arrive above 90% condition (fragile)
**Hazards**: Pirate activity reported along route
**Time Bonus**:
- Under 30 minutes: +200 Credits
- Under 20 minutes: +400 Credits
**Rewards**: 600 Credits (base), +6 Merchant Reputation, +4 Local Standing, 100 Trade XP
**Failure Note**: Settlement suffers if failed (narrative consequence)

---

#### "Black Gold Run" (T4 - Moderate)
**Port**: T4 Industrial Ports
**Type**: Oversized Cargo
**Description**: The refinery at Port Valdez needs crude oil shipment. Your vessel has been chartered for the hazardous journey through contested waters.
**Cargo**: Crude Oil (500 tons, hazardous)
**Route**: Oil Platform Gamma → Port Valdez Refinery (32km)
**Special Conditions**:
- Cargo is flammable (fire damage = explosion risk)
- Cannot exceed 18 knots (cargo stability)
- Route passes through Contested Zone
**Objectives**:
- Load oil at platform
- Navigate to refinery without incident
- Deliver full cargo (no spillage)
**Hazards**:
- Enemy patrols in Zone F
- Known submarine activity
- Weather may degrade
**Rewards**: 1,800 Credits, +8 Merchant Reputation, Tanker Operations Badge
**Ship Requirement**: Cargo capacity 500+ tons
**Time Limit**: 3 hours

---

#### "Forbidden Freight" (T5 - Hard)
**Port**: Neutral/Pirate Ports
**Type**: Contraband Run
**Description**: A "business associate" needs certain goods moved discretely. No questions asked. High pay, higher risk.
**Cargo**: [Contraband] (100 tons, hidden compartment)
**Route**: Pirate Haven → Neutral Port Marcus (45km through national waters)
**Special Conditions**:
- If stopped by patrol, cargo will be discovered
- Discovery = immediate combat or surrender
- Surrender = loss of cargo, -25 national reputation, fine
**Objectives**:
- Load contraband cargo
- Navigate through national waters undetected
- Deliver to contact at Port Marcus
- Avoid all patrol inspections
**Risk Factor**:
- 30% chance of patrol encounter per zone crossed
- Patrol ships will demand inspection
- Options: Submit (caught), Flee (combat), Bribe (50% chance, costs 500 Credits)
**Rewards**: 4,000 Credits, +10 Underworld Reputation, -5 National Reputation (even if successful)
**Failure Consequence**: Cargo confiscated, -25 Reputation, possible bounty

---

### 2.2 Personnel Transport

#### "Shore Leave Express" (T2 - Easy)
**Port**: T2 Minor Ports (Military)
**Type**: Military Transfer
**Description**: Navy personnel require transport to their new duty station. Safe passage expected but stay alert.
**Passengers**: 12 Naval Personnel
**Route**: Minor Naval Base → Regional Command (15km)
**Objectives**:
- Board passengers at origin
- Transport to destination
- Passengers prefer minimal combat exposure
**Passenger Satisfaction**:
- No combat: 100% tip
- Brief combat (< 5 minutes): 75% tip
- Extended combat: 50% tip
- Passenger casualty: Mission Failed
**Rewards**: 250 Credits + 50 Credits tip (max), +3 Military Transport Reputation
**Special**: Passengers provide combat assistance if attacked

---

#### "The Last Voyage Home" (T3 - Normal)
**Port**: T3 Regional Ports (Civilian)
**Type**: Civilian Evacuation
**Description**: The island settlement is being evacuated due to imminent enemy occupation. These civilians are counting on you.
**Passengers**: 45 Civilians (women, children, elderly)
**Route**: Evacuation Point → Safe Harbor (22km through active combat zone)
**Special Conditions**:
- Civilians panic during combat (-10% satisfaction per engagement)
- Cannot return fire first (civilian vessel rules)
- Enemy SHOULD NOT target civilian transport (but pirates might)
**Objectives**:
- Board all civilians within 15-minute window
- Transport safely to destination
- Minimize trauma (combat exposure)
**Rewards**:
- 750 Credits base
- Humanitarian Medal
- +8 Civilian Reputation
- +5 National Reputation
**Bonus**: Zero combat exposure: "Guardian Angel" achievement
**Failure Note**: Civilian casualties have severe reputation consequences

---

#### "Precious Cargo" (T5 - Hard)
**Port**: T5 Capital Ports (Diplomatic)
**Type**: VIP Transport
**Description**: Ambassador Yoshida requires discrete transport to neutral territory for sensitive negotiations. His safety is paramount. His demands are... extensive.
**VIP**: Ambassador Yoshida (+ 4 staff)
**Route**: Capital → Neutral Port (55km, multiple route options)
**VIP Requirements**:
- Cabin temperature maintained (engineering check)
- No rough seas (route planning required)
- Absolutely no combat (will abort mission if engaged)
- Specific meal schedule (time management)
**Objectives**:
- Board VIP party
- Navigate smoothest possible route
- Avoid ALL hostile contact
- Arrive on schedule (3-hour window)
- Keep VIP satisfaction above 75%
**Satisfaction Factors**:
- Combat encounter: -30%
- Rough weather: -10% per hour
- Engine problems: -15%
- Smooth journey: +5% per hour
- Early arrival: +10%
**Rewards**:
- 3,500 Credits (if satisfaction > 90%)
- 2,500 Credits (if satisfaction 75-89%)
- 1,500 Credits (if satisfaction < 75%)
- Diplomatic Courier Badge
- Ambassador's Favor (unlocks exclusive missions)
**Failure**: Satisfaction below 50% or VIP death = Mission Failed, -20 Diplomatic Reputation

---

### 2.3 Supply Runs

#### "Fuel Run" (T3 - Normal)
**Port**: T3+ Fuel Depot Ports
**Type**: Fuel Delivery
**Description**: Destroyer Squadron 7 is stranded in Grid K-3 after extended operations depleted their fuel reserves. Deliver emergency resupply.
**Cargo**: Naval Fuel (200 tons)
**Route**: Fuel Depot → Grid K-3 Rendezvous (28km)
**Objectives**:
- Load fuel cargo
- Rendezvous with stranded squadron
- Transfer fuel (10-minute operation alongside)
- Return to friendly port
**Complications**:
- Squadron is in enemy patrol range
- Must complete transfer before patrol returns
- Fuel cargo is flammable
**Rewards**: 900 Credits, +6 Logistics Reputation, Fleet Support Medal
**Time Pressure**: Patrol estimated to return in 90 minutes

---

#### "Operation Mailbag" (T4 - Moderate)
**Port**: T4 Intelligence Ports
**Type**: Secret Documents
**Description**: Classified intelligence must reach forward command before the offensive begins. Interception would be catastrophic.
**Cargo**: Intelligence Briefcase (1 ton, must not be captured)
**Route**: Intelligence HQ → Forward Command (40km through enemy territory)
**Special Conditions**:
- If boarded/captured, documents fall into enemy hands
- Must scuttle ship rather than surrender
- Radio silence required (no distress calls)
**Objectives**:
- Receive documents (briefing included)
- Navigate to Forward Command
- Deliver documents to Commander Hayes
- Confirm delivery receipt
**Failure Modes**:
- Captured: Catastrophic failure, -50 Intelligence Reputation, war impact
- Scuttled: Acceptable failure, -10 Intelligence Reputation
- Delivered: Success
**Rewards**: 2,200 Credits, +12 Intelligence Reputation, Secret Clearance upgrade
**Ship Requirement**: T3-T6 (larger ships draw attention)

---

## 3. Exploration Missions

### 3.1 Reconnaissance

#### "Eyes on Yokosuka" (T4 - Moderate)
**Port**: T4+ Intelligence Office
**Type**: Port Surveillance
**Description**: Naval Intelligence requires current information on enemy fleet composition at Yokosuka Naval Base. Observe and report without being detected.
**Target**: Yokosuka Naval Base (Enemy Port)
**Objectives**:
- Navigate to observation position (2km from port)
- Remain undetected
- Photograph/record ships in harbor (5-minute observation)
- Identify ship classes (automatic upon observation)
- Extract without alerting defenses
**Detection Risk**:
- Patrol boats circle every 8 minutes
- Radar coverage to 4km from port
- Visual sentries (reduced at night)
**Rewards**: 1,400 Credits, +10 Intelligence Reputation, Strategic Map Update
**Bonus**: Identify capital ship (battleship/carrier): +500 Credits
**Night Bonus**: 25% increased rewards for night operation

---

#### "Mapping the Minefield" (T3 - Normal)
**Port**: T3 Regional Ports
**Type**: Minefield Mapping
**Description**: Enemy minefields block our access to Strait of Torres. Chart a safe passage through.
**Target Area**: Strait of Torres (Grid D-6 to D-8)
**Objectives**:
- Enter minefield perimeter
- Navigate slowly (< 8 knots) through field
- Mark mine positions (automatic when within 200m)
- Chart minimum 80% of field
- Extract safely
**Risk Factor**:
- Contact with mine = heavy damage or sinking
- Slow speed required for detection
- Enemy patrols aware of area
**Rewards**: 850 Credits, +7 Navigator Reputation, Minefield Charts (tradeable item)
**Bonus**: 100% charted: +300 Credits, "Minefield Master" achievement
**Recommendation**: Shallow-draft vessels reduce risk

---

### 3.2 Discovery

#### "The Lost Convoy" (T3 - Normal)
**Port**: T3 Regional Ports (Salvage Guild)
**Type**: Shipwreck Investigation
**Description**: Convoy PQ-17 went down in a storm three weeks ago. The insurance company wants confirmation of sinking locations. Families want closure.
**Target Area**: Storm Gulf (Grid M-4 to M-6)
**Known Information**:
- 6 ships lost (3 freighters, 2 tankers, 1 escort)
- Approximate sinking locations from last radio contact
- Scattered debris field expected
**Objectives**:
- Locate wreck sites (minimum 4 of 6)
- Photograph each wreck
- Recover ship logs if accessible (bonus)
- Return documentation to port
**Rewards**:
- 100 Credits per wreck found
- +3 Explorer Reputation per wreck
- Ship log recovery: +150 Credits each
- All 6 found: "Convoy Finder" achievement
**Time Limit**: None (wreck sites persist)

---

#### "Uncharted Paradise" (T2 - Easy)
**Port**: T2 Minor Ports
**Type**: Island Survey
**Description**: Reports of an uncharted island in Sector B-9. The Cartographer's Guild wants it properly surveyed and mapped.
**Target**: Unknown Island (approximately Grid B-9)
**Objectives**:
- Locate the island
- Circumnavigate completely (chart coastline)
- Identify 3 key features (beaches, harbors, hazards)
- Name the island (player choice, subject to approval)
**Discovery Points**:
- Fresh water source: +100 Credits
- Natural harbor: +150 Credits
- Mineral deposits: +200 Credits
- Dangerous wildlife: +50 Credits (warning marker)
- Ancient ruins: +300 Credits
**Rewards**: 300 Credits base + discovery bonuses, +5 Explorer Reputation
**Special**: Island naming rights (if first to complete)

---

#### "Ghost Ship of Sector 7" (T5 - Hard)
**Port**: T5 Capital Ports (Salvage Guild)
**Type**: Anomaly Investigation
**Description**: Multiple captains report seeing a phantom vessel in Sector 7. Lights at night, no radio response, vanishes when approached. Command wants answers.
**Target**: Unknown Vessel (Sector 7, sporadic appearances)
**Known Information**:
- Appears between 22:00-04:00
- Resembles pre-war cargo vessel
- Does not respond to radio hails
- Disappears when ships close within 500m
**Objectives**:
- Patrol Sector 7 during night hours
- Locate the anomaly
- Approach within 200m (requires stealth approach)
- Document findings (automatic)
- Report to Intelligence
**Possible Outcomes**:
- Derelict vessel (salvage opportunity)
- Enemy spy ship (combat encounter)
- Navigation hazard (gas leak causing hallucinations)
- Actual supernatural event? (cosmetic reward)
**Rewards**: 2,500 Credits, +15 Explorer Reputation, "Ghost Hunter" title
**Mystery**: Outcome varies - adds replayability

---

## 4. Salvage Missions

### 4.1 Wreck Salvage

#### "Easy Pickings" (T2 - Easy)
**Port**: T2 Minor Ports (Salvage Guild)
**Type**: Surface Wreck
**Description**: Freighter "Morning Star" ran aground on the reef last week. She's still above water but abandoned. Salvage what you can.
**Wreck**: Morning Star (Cargo Freighter, T2)
**Location**: Reef Point, 6km from port
**Salvage Available**:
- General Cargo (150 tons, 3 Credits/ton)
- Ship Fittings (25 tons, 8 Credits/ton)
- Fuel Reserves (50 tons, 5 Credits/ton)
- Captain's Safe (1 ton, 500 Credits - rare chance)
**Objectives**:
- Navigate to wreck site
- Conduct salvage operations (15 minutes minimum)
- Load salvage into cargo hold
- Return to port
**Salvage Efficiency**: Based on crew skill + time invested
**Rewards**: Salvaged value + 150 Credits bonus, +4 Salvager Reputation
**Competition**: Other players may race to salvage site

---

#### "The Richter Fortune" (T5 - Hard)
**Port**: T5 Capital Ports (Salvage Guild)
**Type**: Historical Wreck
**Description**: The passenger liner "Richter" sank in 1939 carrying wealthy passengers fleeing the war. Her purser's vault has never been recovered. You have the coordinates.
**Wreck**: SS Richter (Luxury Liner, T6)
**Location**: Deep water Grid H-11 (submarine-accessible depths)
**Known Contents**:
- Gold bullion (unknown quantity)
- Jewelry and valuables
- Historical documents
- Personal effects (family reward available)
**Objectives**:
- Locate precise wreck position
- Conduct deep salvage (requires submarine OR diving equipment)
- Recover valuables from purser's vault
- Return artifacts to Salvage Guild
**Challenges**:
- Depth requires special equipment
- Multiple compartments to search
- Time-limited dive operations
- Possible competitor interference
**Rewards**:
- Variable based on recovery (estimated 5,000-15,000 Credits)
- Historical Artifacts (museum value)
- +20 Salvager Reputation
- "Treasure Hunter" achievement
**Note**: One-time mission per server - once recovered, permanently completed

---

### 4.2 Resource Collection

#### "Black Gold Harvest" (T3 - Normal)
**Port**: T3 Industrial Ports
**Type**: Oil Collection
**Description**: The offshore well at Platform Delta has excess production. Collect the overflow and deliver to the refinery.
**Resource**: Crude Oil
**Target Quantity**: 300 tons
**Location**: Platform Delta, Grid E-5
**Objectives**:
- Navigate to Platform Delta
- Connect to loading system
- Collect oil cargo (loading rate: 50 tons per 5 minutes)
- Transport to Refinery Port
**Hazards**:
- Platform is isolated (no nearby support)
- Occasional pirate interest in fuel shipments
- Weather can interrupt loading operations
**Rewards**: 750 Credits + fuel value, +5 Industrial Reputation
**Ship Requirement**: 300+ ton cargo capacity, fuel handling equipment

---

#### "The Fisher King" (T2 - Easy)
**Port**: T2 Fishing Ports
**Type**: Fishing Contract
**Description**: The Seafood Co-op needs 50 tons of fresh tuna for an export order. You have the gear; bring us the catch.
**Resource**: Bluefin Tuna
**Target Quantity**: 50 tons
**Fishing Grounds**: Tuna Alley (Grid C-2 to C-4)
**Objectives**:
- Navigate to fishing grounds
- Deploy fishing gear
- Catch tuna (rate depends on crew skill + equipment)
- Return with catch before spoilage
**Fishing Mechanics**:
- Base rate: 10 tons per 15 minutes
- Skilled crew: +50% rate
- Premium gear: +25% rate
- Weather affects catch rates
**Rewards**: 400 Credits, +4 Merchant Reputation, Fishing XP
**Time Limit**: Catch spoils after 4 hours (real-time)

---

## 5. Escort Missions

### 5.1 Convoy Protection

#### "Milk Run" (T2 - Easy)
**Port**: T2 Minor Trade Ports
**Type**: Small Merchant Convoy
**Description**: Three merchant vessels need escort to the next port. Light opposition expected. Good training mission.
**Convoy**:
- 3x Small Freighters (T1)
**Route**: Port Origin → Port Destination (12km)
**Expected Threats**:
- 2x Pirate Boats (T1) - single encounter
**Objectives**:
- Rendezvous with convoy at departure point
- Escort through route
- Defend against any attacks
- All ships arrive: Full reward
- 2 ships arrive: 66% reward
- 1 ship arrives: 33% reward
**Rewards**: 300 Credits, +3 Escort Reputation, 50 Combat XP

---

#### "Operation Torch Run" (T5 - Hard)
**Port**: T5 Military Ports
**Type**: Troop Transport Escort
**Description**: The assault on Normandy requires massive troop movements. Protect the transport fleet at all costs. History depends on it.
**Convoy**:
- 6x Troop Transports (T4, 500 soldiers each)
- 4x Supply Ships (T3)
- 2x Hospital Ships (T3, non-combatant)
**Allied Escorts**: 4x AI Destroyers (T4)
**Route**: Staging Area → Beach Approach (35km)
**Expected Threats**:
- Phase 1: Submarine ambush (2x subs)
- Phase 2: E-boat attack (8x fast attack boats)
- Phase 3: Air attack (12 aircraft)
- Phase 4: Surface raiders (2x destroyers)
**Objectives**:
- All troop transports must survive
- At least 3 supply ships must survive
- Hospital ships must survive (war crime if lost to player action)
**Victory Conditions**:
- Perfect Score (all survive): 4,500 Credits
- Success (6 transports survive): 3,000 Credits
- Partial (4-5 transports survive): 1,500 Credits
- Failure (3 or fewer transports): Mission Failed
**Rewards**: See Victory Conditions, +12 Escort Reputation, Campaign Medal
**Note**: Historical operation event - available during D-Day anniversary

---

### 5.2 VIP Protection

#### "The Diplomat's Voyage" (T4 - Moderate)
**Port**: T4 Capital Ports
**Type**: VIP Escort
**Description**: Ambassador Sterling is traveling to peace negotiations. Enemy elements may attempt to sabotage the talks by eliminating him. Don't let that happen.
**VIP**: Ambassador Sterling aboard yacht "Serenity" (T3, unarmed)
**Route**: Capital → Neutral Port (45km through contested waters)
**Known Threats**:
- Enemy agents aware of mission
- 2-3 assassination attempts expected
- Unknown attack vectors
**Objectives**:
- Rendezvous with Serenity at departure
- Maintain escort position (within 500m)
- Defend against all attacks
- VIP must survive
**Attack Types** (random selection):
- Submarine torpedo ambush
- Surface raiders (fast attack boats)
- Mines laid on route
- Air attack (if carrier operations active)
**Rewards**: 2,500 Credits, +10 Diplomatic Reputation, VIP Escort Medal
**Failure Consequence**: Ambassador's death = -30 Diplomatic Reputation, war impact

---

## 6. Squadron & Fleet Missions

### 6.1 Small Group Operations (2-6 Players)

#### "Wolfpack Alpha" (T4 - Moderate)
**Port**: T4 Military Ports
**Type**: Coordinated Patrol
**Required**: 3-4 players (destroyers preferred)
**Description**: Form a hunter-killer group and sweep Sector Nine for enemy submarines. Coordinate your search pattern.
**Objectives**:
- Each player assigned separate search zone
- Detect and report submarine contacts
- Coordinate attack on detected submarines
- Sink at least 2 enemy submarines
**Coordination Bonuses**:
- Simultaneous detection bonus: +200 Credits each
- Kill assist bonus: +100 Credits
- Full sweep completion: +500 Credits
**Rewards (per player)**: 1,200 Credits, +8 ASW Reputation, 200 Combat XP
**Time Limit**: 90 minutes

---

#### "Supply Interdiction" (T5 - Hard)
**Port**: T5 Capital Ports
**Type**: Coordinated Ambush
**Required**: 4-6 players (mixed fleet)
**Description**: Major enemy supply convoy departing tonight. We have their route. Set up ambush positions and destroy as much as possible.
**Target Convoy**:
- 8x Cargo Ships (T3-T4)
- 6x Destroyer Escorts (T4)
- 2x Cruiser Escorts (T5)
**Tactical Plan**:
- Position 1: Forward scouts (fast ships)
- Position 2: Ambush element (main striking force)
- Position 3: Rear guard (cut off retreat)
**Objectives**:
- Sink at least 5 cargo ships
- Sink all escorts for bonus
- Extract with surviving squadron members
**Rewards (per player)**:
- 2,000 Credits base
- +200 Credits per cargo ship above 5
- +300 Credits per escort destroyed
- +15 Combat Reputation
**Squadron Bonus**: All members survive: +500 Credits each

---

### 6.2 Large Fleet Operations (10-50+ Players)

#### "Operation Hammer" (T6 - Elite)
**Port**: T6 Fleet HQ (Guild coordination required)
**Type**: Fleet Strike
**Required**: 15-25 players (full fleet composition)
**Description**: Enemy fleet concentration at Rabaul threatens our entire theater. Command has authorized a major strike. This is it.
**Target**: Rabaul Naval Base
**Enemy Forces**:
- 2x Battleships (T8)
- 4x Cruisers (T6-T7)
- 8x Destroyers (T5)
- 2x Carriers (T7)
- Port defenses (batteries, patrol boats)
**Recommended Fleet Composition**:
- 4x Battleships/Battlecruisers (main strike)
- 6x Cruisers (screening)
- 8x Destroyers (ASW/torpedo attack)
- 4x Carriers (air support)
- 3x Submarines (reconnaissance/ambush)
**Phases**:
1. Approach (submarine reconnaissance)
2. Air strike (neutralize carriers)
3. Surface engagement (main fleet battle)
4. Withdrawal (protect damaged ships)
**Objectives**:
- Sink both enemy battleships
- Sink at least 1 carrier
- Destroy port facilities
- Extract with 60% of fleet surviving
**Rewards (per player)**:
- Base: 4,000 Credits
- Victory bonus: +2,000 Credits
- Ship destruction bonuses variable
- +25 Combat Reputation
- "Operation Hammer" participant medal
**Territory Effect**: Success shifts regional influence by +150 points
**Note**: Requires Guild coordination. Available weekly.

---

## 7. Ship-Class Specific Missions

### 7.1 Submarine Missions

#### "Silent Running" (T4 - Moderate)
**Port**: Submarine Pens
**Type**: Silent Patrol
**Ship Required**: Any submarine T4+
**Description**: Transit the narrow strait undetected. Enemy ASW forces patrol constantly. One ping and you're dead.
**Objectives**:
- Enter Strait of Messina from south
- Transit entire strait (15km) submerged
- No detection alerts triggered
- Exit north and surface in friendly waters
**Detection Hazards**:
- 4x ASW destroyers (active sonar)
- 2x patrol aircraft (visual detection if surfaced)
- Hydrophone stations (detect engine noise)
**Stealth Mechanics**:
- Battery management (limited underwater time)
- Noise discipline (speed affects detection)
- Thermal layers (use depth to hide)
**Rewards**: 1,500 Credits, +10 Submarine Reputation, "Silent Service" medal
**Bonus**: Zero detection events: +500 Credits

---

#### "Torpedo Alley" (T5 - Hard)
**Port**: Submarine Pens
**Type**: Convoy Interdiction
**Ship Required**: Submarine T5+
**Description**: Fat convoy heading through the Channel. You're the only asset in position. Make every torpedo count.
**Target Convoy**:
- 6x Large Freighters (T4, 10,000 tons each)
- 4x Tankers (T4, 15,000 tons each)
- 5x Destroyer Escorts (T4, aggressive ASW)
**Objectives**:
- Intercept convoy in Grid K-7
- Sink minimum 30,000 tons of shipping
- Survive and extract
**Tactical Considerations**:
- Standard torpedo load: 12-16 depending on class
- Reload time: 2 minutes per tube
- Escorts will depth charge on detection
- Night attack reduces visual detection
**Rewards**:
- 100 Credits per 1,000 tons sunk
- Perfect attack (all torpedoes hit): +1,000 Credits
- +15 Submarine Ace Reputation
- Tonnage war contribution
**Achievement**: Sink 50,000 tons: "Torpedo Terror" title

---

### 7.2 Carrier Missions

#### "Combat Air Patrol" (T5 - Moderate)
**Port**: Carrier-capable ports
**Type**: Fleet Air Defense
**Ship Required**: Any carrier T5+
**Description**: Provide air cover for Task Force 58 during transit through enemy waters. Keep the skies clear.
**Protected Assets**: Task Force 58 (6 ships, AI controlled)
**Mission Duration**: 90 minutes
**Enemy Air Attacks**:
- Wave 1 (15 min): 8x torpedo bombers
- Wave 2 (35 min): 12x dive bombers
- Wave 3 (60 min): 6x torpedo + 8x dive bombers
- Wave 4 (75 min): 16x mixed attack
**Objectives**:
- Launch and maintain CAP
- Intercept all attack waves
- Task Force must survive with 4+ ships
**Air Wing Management**:
- Fighter squadron rotation
- Ammunition rearming
- Damaged aircraft recovery
**Rewards**: 2,500 Credits, +12 Carrier Reputation, "Shield of the Fleet" medal
**Victory Conditions**:
- Perfect (6 ships survive, <10% aircraft losses): 4,000 Credits
- Success (4+ ships survive): 2,500 Credits
- Partial (2-3 ships survive): 1,000 Credits

---

#### "Alpha Strike" (T6 - Hard)
**Port**: Fleet anchorages
**Type**: Carrier Strike Mission
**Ship Required**: Fleet carrier T6+
**Description**: Enemy battleship group located. Launch full strike package and neutralize the threat.
**Target Fleet**:
- 1x Battleship (T7, primary target)
- 2x Cruisers (T6, AA screens)
- 4x Destroyers (T5, ASW/AA)
**Required Strike Package**:
- Torpedo bombers (recommended 12+)
- Dive bombers (recommended 8+)
- Fighter escort (recommended 6+)
**Objectives**:
- Plan strike route (avoid detection)
- Launch coordinated attack
- Sink the battleship
- Recover aircraft
**Success Metrics**:
- Battleship sunk: Mission complete
- Battleship + 1 cruiser: Excellent
- Full fleet destroyed: Perfect
**Aircraft Losses**:
- Expected: 20-30%
- Acceptable: Up to 50%
- Excessive: 50%+ (reduces rewards)
**Rewards**:
- Battleship kill: 3,000 Credits
- Per escort destroyed: +400 Credits
- Low losses bonus: +1,000 Credits
- +20 Carrier Reputation

---

### 7.3 Destroyer Missions

#### "Tin Can Alley" (T4 - Moderate)
**Port**: Naval bases
**Type**: Torpedo Attack
**Ship Required**: Destroyer T4+
**Description**: Enemy cruiser squadron anchored for resupply. Night torpedo attack authorized. Get in, launch, get out.
**Target**:
- 2x Heavy Cruisers (T6)
- Light defenses (reduced at night)
**Mission Profile**:
- Approach at night (reduced detection)
- Close to effective torpedo range (4km optimal)
- Launch spread of torpedoes
- Retreat at full speed
**Objectives**:
- Successfully launch torpedoes at cruisers
- Score at least 2 torpedo hits
- Escape without being sunk
**Risk Factor**:
- Cruiser secondary batteries lethal to destroyers
- Detection = heavy fire
- Must balance range vs accuracy
**Rewards**: 1,800 Credits, +10 Surface Combat Reputation, "Tin Can Hero" achievement
**Bonus**: Sink both cruisers: +1,500 Credits, "Cruiser Slayer" title

---

#### "Sub Hunter" (T4 - Moderate)
**Port**: ASW bases
**Type**: Anti-Submarine Warfare
**Ship Required**: Destroyer with sonar T4+
**Description**: Enemy submarine reported harassing our shipping in Grid F-3. Hunt it down.
**Target**: Enemy submarine (T5, skilled captain)
**Search Area**: 16 square km grid
**Objectives**:
- Search assigned grid
- Detect submarine contact
- Attack and confirm kill
- Report to command
**ASW Mechanics**:
- Active sonar (reveals position, alerts sub)
- Passive sonar (slower detection, stealthy)
- Depth charge patterns
- Hedgehog attacks (if equipped)
**Target Behavior**:
- Submarine will evade
- May launch torpedo counterattack
- Uses thermal layers and wrecks for hiding
**Rewards**: 1,200 Credits, +8 ASW Reputation, Submarine kill confirmation
**Bonus**: No damage taken: +400 Credits

---

### 7.4 Capital Ship Missions

#### "Shore Bombardment Support" (T5 - Moderate)
**Port**: Fleet anchorage
**Type**: Fire Support
**Ship Required**: Cruiser or Battleship T5+
**Description**: Marines hitting Red Beach at 0600. They need naval gunfire support on the defensive positions.
**Target Area**: Beach defensive positions
**Fire Missions**:
1. Pre-landing bombardment (targets marked)
2. On-call fire support (as requested)
3. Counter-battery fire (respond to enemy artillery)
**Objectives**:
- Arrive at fire support position by 0545
- Complete pre-landing bombardment
- Respond to fire support requests (6 minimum)
- Maintain station until marines secure beachhead (60 min)
**Ammunition Management**:
- Limited main gun ammunition
- Must balance accuracy vs volume
- Resupply available but time-consuming
**Rewards**: 2,200 Credits, +10 Fire Support Reputation, Marine Corps Commendation
**Bonus**: All fire missions effective: +800 Credits

---

#### "Line of Battle" (T6 - Elite)
**Port**: Fleet HQ
**Type**: Fleet Action Command
**Ship Required**: Battleship T7+
**Description**: Serve as flagship for Battle Group Omega. Lead the fleet into combat against enemy main force.
**Your Command**:
- Your battleship (flag)
- 2x AI battleships (T6)
- 4x AI cruisers (T5)
- 6x AI destroyers (T4)
**Enemy Force**:
- 3x Battleships (T7)
- 3x Cruisers (T6)
- 8x Destroyers (T5)
**Command Interface**:
- Direct fleet formations
- Assign targets
- Call for maneuvers
- Coordinate retreat if needed
**Objectives**:
- Engage enemy fleet
- Sink at least 2 enemy battleships
- Preserve 50% of your fleet
**Command Ratings**:
- Decisive Victory (all enemies sunk, 75%+ fleet survives): 6,000 Credits
- Victory (2+ BBs sunk, 50%+ fleet survives): 4,000 Credits
- Pyrrhic Victory (objectives met, heavy losses): 2,000 Credits
**Rewards**: See ratings, +20 Command Reputation, Fleet Action Medal
**Special**: Unlocks advanced command missions

---

## 8. Pirate Missions

### 8.1 Raiding Missions

#### "Easy Prey" (T3 - Normal)
**Port**: Pirate Outposts
**Type**: Merchant Raid
**Reputation Required**: Outlaw (-50 or lower)
**Description**: Fat merchant running solo through the straits. Easy pickings. Don't damage the cargo too much.
**Target**: Solo Freighter (T3, 200 tons cargo)
**Objectives**:
- Intercept target in designated zone
- Disable ship (reduce to 25% HP)
- Board and capture cargo
- Escape before navy response
**Boarding Mechanics**:
- Pull alongside disabled ship
- 5-minute boarding operation
- Transfer cargo to your hold
- Can choose to sink or release victim
**Rewards**: Stolen cargo value (estimated 600-1,200 Credits), +5 Pirate Reputation
**Navy Response**: Patrol arrives 10 minutes after combat starts

---

#### "The Big Score" (T5 - Hard)
**Port**: Pirate Haven
**Type**: Treasure Ship Raid
**Reputation Required**: Full Pirate (-75 or lower)
**Description**: Colonial treasure galleon sailing for the homeland. Escorted but vulnerable. This is the haul of a lifetime.
**Target**:
- Treasure Ship "Golden Empire" (T5, heavily laden)
- 4x Naval Escort (T4 destroyers)
**Cargo Value**: 15,000-25,000 Credits in gold and valuables
**Objectives**:
- Intercept convoy
- Sink or drive off escorts
- Capture treasure ship intact
- Escape with cargo
**Tactical Challenge**:
- Escorts are aggressive and skilled
- Treasure ship will attempt to flee
- Damaging treasure ship destroys cargo
- Navy reinforcements en route
**Rewards**:
- Full cargo capture: 15,000-25,000 Credits
- Partial capture: Proportional
- +20 Pirate Reputation
- "Treasure Hunter" achievement
**Risk**: Failed raid = bounty increased significantly

---

### 8.2 Smuggling Missions

#### "Border Run" (T4 - Moderate)
**Port**: Neutral Ports
**Type**: Contraband Smuggling
**Reputation Required**: Outlaw (-25 or lower)
**Description**: Certain goods are... restricted in the Empire. But very valuable. Get them across the border.
**Cargo**: Weapons (75 tons, military equipment)
**Route**: Neutral Port → Resistance Contact (30km through Imperial waters)
**Objectives**:
- Load contraband (hidden compartments)
- Navigate through patrol routes
- Avoid inspection or evade pursuit
- Deliver to contact
**Patrol Encounters**:
- 40% chance per zone crossed
- Inspection: 75% detection chance
- Bribe option: 300 Credits (50% success)
- Flee option: Combat likely
**Rewards**: 2,500 Credits, +8 Underworld Reputation
**Failure Consequences**: Cargo seized, -20 National Reputation, possible bounty

---

### 8.3 Redemption Missions

#### "Atonement" (T4 - Moderate)
**Port**: Neutral Ports (Amnesty Office)
**Type**: Redemption - Anti-Piracy
**Reputation Required**: Outlaw status + completed amnesty payment
**Description**: You want back in. Prove it. Hunt the pirates you once sailed with. Bring us Captain Blackwood.
**Target**: Pirate Captain Blackwood (former associate)
**Location**: Tortuga approaches
**Objectives**:
- Locate Captain Blackwood
- Defeat in combat
- Capture or kill (capture pays more)
- Return to Amnesty Office
**Moral Choice**:
- Former comrades may try to talk you down
- Other pirates will be hostile
- Blackwood offers bribe to fake his death
**Rewards**:
- Kill: 1,500 Credits, +15 National Reputation
- Capture: 2,500 Credits, +25 National Reputation
- "Reformed Pirate" progress
**Note**: First of 5-mission redemption chain

---

## 9. Tutorial Missions (Full Chain)

### 9.1 New Captain Tutorial Chain

#### Tutorial Mission 1: "First Steps"
**Description**: Welcome to the Navy, Captain. Let's see if you can find your way out of the harbor.
**Objectives**:
1. Access the helm controls
2. Undock from port
3. Navigate to the green waypoint (500m)
4. Return to port and dock
**Teaches**: Basic controls, docking, extraction concept
**Reward**: 50 Credits, "First Voyage" badge

---

#### Tutorial Mission 2: "Reading the Seas"
**Description**: Navigation is survival. Learn to read your instruments.
**Objectives**:
1. Open the navigation map
2. Plot course to Waypoint Alpha
3. Navigate using compass heading
4. Identify the lighthouse on approach
5. Return to port
**Teaches**: Map, compass, visual navigation
**Reward**: 75 Credits, Navigation Tutorial completion

---

#### Tutorial Mission 3: "Know Your Enemy"
**Description**: Out there, you'll encounter hostiles. Learn to identify them before they identify you.
**Objectives**:
1. Proceed to observation zone
2. Use binoculars to spot patrol boat
3. Identify ship class and nation
4. Avoid detection (maintain 2km distance)
5. Return and report
**Teaches**: Spotting, identification, stealth
**Reward**: 100 Credits, Binoculars module

---

#### Tutorial Mission 4: "Baptism of Fire"
**Description**: Theory only gets you so far. Time to pull the trigger.
**Objectives**:
1. Engage the target drone
2. Score hits with main guns
3. Sink the target
4. Return to port
**Teaches**: Combat basics, weapon systems, hit feedback
**Reward**: 150 Credits, 50 rounds ammunition

---

#### Tutorial Mission 5: "Spoils of War"
**Description**: Never leave loot behind. Learn to profit from victory.
**Objectives**:
1. Sink the pirate vessel
2. Approach the wreckage
3. Collect floating cargo
4. Return cargo to port
**Teaches**: Looting, cargo, inventory
**Reward**: 200 Credits + cargo value

---

## 10. Territory & War Missions

### 10.1 Zone Control

#### "Sector Dominance" (T4 - Moderate)
**Port**: Border Ports
**Type**: Zone Influence
**Description**: Sector J-5 is contested. Establish our dominance through sustained presence and combat superiority.
**Zone**: Sector J-5 (Contested)
**Objectives**:
- Operate in zone for minimum 30 minutes
- Sink 3+ enemy vessels
- Complete 2 sub-objectives (patrol points)
- Generate +25 influence toward your nation
**Sub-objectives**:
- Destroy enemy patrol at checkpoint
- Escort friendly convoy through zone
- Plant navigation buoy
- Destroy enemy supply cache
**Rewards**: 1,200 Credits, +8 War Reputation, Territory medal
**Territory Effect**: +25 influence points if successful

---

#### "Outpost Assault: Firebase Charlie" (T6 - Elite)
**Port**: Forward Operating Bases
**Type**: Outpost Capture
**Required**: 8+ players (squadron/fleet)
**Description**: Firebase Charlie controls the strait. It's time to take it.
**Target**: Firebase Charlie (Enemy Outpost)
**Defenses**:
- 4x Gun batteries
- 2x Torpedo platforms
- Minefield approach
- Garrison: 6x patrol boats, 2x destroyers
- Reinforcement response: 15 minutes
**Phases**:
1. Mine clearing
2. Battery suppression
3. Garrison elimination
4. Point capture (5-minute hold)
5. Defense against counter-attack
**Objectives**:
- Destroy all fixed defenses
- Eliminate garrison
- Hold capture point for 5 minutes
- Survive counter-attack
**Rewards (per player)**: 3,500 Credits, +18 War Reputation, Assault medal
**Territory Effect**: Outpost flips to your nation (+100 influence)

---

## 11. Event Missions

### 11.1 Historical Events

#### "Remember Pearl Harbor" (December 7)
**Type**: Annual Historical Event
**Description**: On this day, we remember. Participate in the defense of Pearl Harbor recreation.
**Scenario**: You are defending Pearl Harbor during the Japanese attack
**Waves**:
- Wave 1: Torpedo bomber attack on Battleship Row
- Wave 2: Dive bomber attack on airfields (AA defense)
- Wave 3: Second wave assault
**Objectives**:
- Survive the attack
- Shoot down enemy aircraft
- Protect as many ships as possible
**Historical Note**: Educational briefing about the actual events
**Rewards**:
- Participation: Commemorative flag
- 10+ aircraft kills: "Remember Pearl Harbor" medal
- Survive all waves: 1,000 Credits
**Availability**: December 7th only

---

#### "D-Day: Operation Neptune" (June 6)
**Type**: Annual Historical Event
**Description**: The largest amphibious operation in history. Support the landings.
**Scenarios**:
- **Minesweeping**: Clear channels for landing craft
- **Shore Bombardment**: Suppress beach defenses
- **Escort Duty**: Protect transport ships
- **PT Boat Action**: Fast attack craft operations
**Objectives**: Role-dependent (see above)
**Historical Note**: Educational content about Operation Overlord
**Rewards**:
- Participation: D-Day commemorative badge
- Mission completion: 1,500 Credits
- Perfect score: "Neptune Hero" title
**Availability**: June 6th week

---

### 11.2 Seasonal Events

#### "Winter War: Arctic Convoy" (December-January)
**Type**: Seasonal Event Mission
**Description**: The Arctic convoys must get through. Brave the cold, the enemy, and the sea.
**Convoy**: PQ-17 (8 merchant ships)
**Route**: Iceland → Murmansk (extended route)
**Challenges**:
- Extreme weather (-25% visibility)
- U-boat wolf packs
- Luftwaffe air attacks
- Equipment freezing (random malfunctions)
**Objectives**:
- Escort convoy to destination
- Minimum 4 ships must arrive
- Survive arctic conditions
**Rewards**:
- Event currency: 500 Winter Marks
- Unique camouflage: Arctic White
- +15 Convoy Reputation
**Event Duration**: 6 weeks

---

## 12. Crew Training Missions

### 12.1 Skill Training

#### "Gunnery Qualification" (T3 - Normal)
**Port**: Training Facilities
**Type**: Gunnery Training
**Description**: Complete gunnery trials to certify your crew's accuracy.
**Objectives**:
1. Hit 10 stationary targets
2. Hit 5 moving targets
3. Score 3 critical hits
4. Complete timed engagement (8 targets in 2 minutes)
**Scoring**:
- Accuracy rating determines XP bonus
- 90%+ accuracy: A rating
- 75-89%: B rating
- 60-74%: C rating
**Rewards**:
- 400 Credits
- Gunnery skill +50% XP for 24 hours
- Rating badge
**Cooldown**: 24 hours

---

#### "Damage Control Drill" (T4 - Moderate)
**Port**: Training Facilities
**Type**: Damage Control Training
**Description**: Your ship will take damage. Learn to survive it.
**Scenario**: Controlled damage exercises
**Phases**:
1. Fire suppression (3 fires to extinguish)
2. Flood containment (compartment flooding)
3. Systems repair (engine/steering damage)
4. Combined emergency (all at once)
**Objectives**:
- Complete all phases
- Maintain ship above 50% HP
- Repair to 75% HP after combined phase
**Rewards**:
- 600 Credits
- Damage Control skill +50% XP for 24 hours
- Damage Control qualification
**Cooldown**: 24 hours

---

## 13. Cross-References

- [[Mission-System]] - Parent document with full mission framework
- [[Squadron-Guild-System]] - Group mission coordination
- [[Reputation-System]] - Mission reputation rewards
- [[Economy-Overview]] - Mission economics
- [[Submarine-Warfare]] - Submarine mission details
- [[Carrier-Operations]] - Carrier mission details

---

## Changelog
- **2025-12-03**: Initial document creation - comprehensive mission examples
