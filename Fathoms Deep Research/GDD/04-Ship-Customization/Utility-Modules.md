# Utility Modules

**Status**: 📋 PLANNED (Phase 2/3 feature)
**Tags**: [planned, phase2, ship-customization, modules, support-systems]
**Priority**: HIGH (essential ship systems)
**Related Systems**: [Module System](Module-System.md), [Technology Integration](Technology-Integration.md), [Combat System](../02-Core-Systems/Combat-System.md)

---

## Overview

Utility modules represent the non-weapon systems that define ship capabilities beyond raw firepower. These modules fall into two primary categories:

**Support Slots**: Crew welfare, engineering support, and logistics modules
**Misc Slots**: Detection, electronics, fire control, and specialized systems

All utility modules require appropriate crew cards to function and integrate with the ship's overall weight and space constraints.

---

## Support Slot Modules

**Slot Characteristics:**
- **Variable Sizes**: Equipment slot sizes 1x1, 1x2, 2x2, 2x3, 3x3 depending on ship design (NOT cargo grid cells, see [[Module-System]])
- **Quantity**: Scales with ship size (Destroyers: 3-8 slots, Battleships: 18-24 slots)
- **Accepts**: Support modules ONLY (crew welfare, engineering support, logistics)
- **Crew Requirement**: Varies by support module type (typically Engineer or Support crew)

---

## Crew Welfare Modules

### Crew Quarters

**Sizes**: 1x2 (Basic), 2x2 (Improved), 2x3 (Luxury)

**Effects:**
- **Basic**: +5 morale, stable morale decay
- **Improved**: +10 morale, +5% crew efficiency
- **Luxury**: +20 morale, +10% crew efficiency, +1 morale/hour at sea

**Specifications:**
- **Weight**: 15 tons (Basic), 25 tons (Improved), 40 tons (Luxury)
- **Crew**: 1 Support crew card required
- **Strategic Use**: Essential for long-range operations (7+ days at sea)

**Installation Notes:**
- Only one Crew Quarters module allowed per ship
- Larger ships should prioritize Improved or Luxury variants
- Morale bonuses stack with other welfare modules

---

### Mess Hall

**Sizes**: 1x2 (Galley), 2x2 (Mess Hall), 2x3 (Officer's Mess)

**Effects:**
- **Galley**: +5 morale, basic food preparation
- **Mess Hall**: +10 morale, +5% crew efficiency
- **Officer's Mess**: +15 morale, +10% officer efficiency, improved crew coordination

**Specifications:**
- **Weight**: 12 tons (Galley), 22 tons (Mess Hall), 35 tons (Officer's Mess)
- **Crew**: 1 Support crew card required
- **Strategic Use**: Morale maintenance during extended deployments

**Synergies:**
- Stacks with Refrigeration Unit for extended voyage capability
- Officer's Mess improves command crew efficiency

---

### Medical Bay/Hospital

**Sizes**: 1x2 (Sick Bay), 2x3 (Medical Bay), 3x3 (Hospital)

**Effects:**
- **Sick Bay**: +10% crew injury recovery rate, treat 1 wounded
- **Medical Bay**: +25% crew injury recovery, treat 2 wounded simultaneously
- **Hospital**: +50% crew injury recovery, treat 5 wounded, surgery capability

**Specifications:**
- **Weight**: 10 tons (Sick Bay), 28 tons (Medical Bay), 50 tons (Hospital)
- **Crew**: 1 Medic crew card required (Medic class unlocked via research)
- **Strategic Use**: Critical for high-tier combat zones with crew casualty risk

**Gameplay Mechanics:**
- Wounded crew cards operate at reduced efficiency until healed
- Medical facilities accelerate recovery time
- Hospital required for severe injuries (revive crew cards downed in combat)
- Medic crew class unlocked via Research Tree (Mid-game progression)

---

### Recreation Room

**Size**: 1x2 (Basic), 2x2 (Advanced)

**Effects:**
- **Basic**: +10 morale, +5% crew efficiency during voyages >3 days
- **Advanced**: +15 morale, +10% efficiency, reduces morale decay rate by 50%

**Specifications:**
- **Weight**: 18 tons (Basic), 30 tons (Advanced)
- **Crew**: 1 Support crew card required
- **Strategic Use**: Long-range extraction missions, extended combat operations

**Morale Decay Mechanics:**
- Base morale decay: -2 morale per day at sea
- Recreation Room (Basic): Reduces decay to -1 morale/day
- Recreation Room (Advanced): Reduces decay to -1 morale/day AND provides passive regeneration

---

## Engineering Support Modules

### Damage Control Station

**Sizes**: 1x2 (Basic), 2x2 (Advanced), 2x3 (Elite)

**Effects:**
- **Basic**: +10% fire suppression speed
- **Advanced**: +25% fire suppression, +10% flooding control
- **Elite**: +50% fire/flood control, automatic response systems, reduced crew casualties from damage

**Specifications:**
- **Weight**: 8 tons (Basic), 18 tons (Advanced), 32 tons (Elite)
- **Crew**: 1 Damage Control crew card required
- **Strategic Use**: Essential for high-tier combat, permadeath zone operations

**Damage Control Mechanics:**
- Fire Suppression: Time to extinguish fires in damaged compartments
- Flooding Control: Time to pump water from breached hull sections
- Elite version enables passive automatic response (no manual activation required)

---

### Machine Shop

**Sizes**: 2x2 (Basic), 2x3 (Advanced)

**Effects:**
- **Basic**: Field repairs 25% more effective, can craft basic ammunition if resources available
- **Advanced**: Field repairs 50% more effective, can craft modules/parts, improves repair kit effectiveness

**Specifications:**
- **Weight**: 35 tons (Basic), 55 tons (Advanced)
- **Crew**: 1 Engineer crew card required
- **Strategic Use**: Extended operations far from friendly ports, self-sufficiency

**Crafting Capabilities:**
- Basic: Craft ammunition (requires raw materials in cargo grid, see [[Inventory-System]])
- Advanced: Craft Small Repair Kits, basic modules (1x1, 1x2 equipment slot size)
- Crafting at sea takes 2-5x longer than at port
- Requires blueprints already unlocked
- Crafted items stored in cargo grid

---

### Auxiliary Generator

**Size**: 1x1 (Small), 1x2 (Large)

**Effects:**
- **Small**: Backup power if 1 engine damaged, +5% engine reliability
- **Large**: Backup power if 2 engines damaged, +10% engine reliability, powers emergency systems

**Specifications:**
- **Weight**: 12 tons (Small), 22 tons (Large)
- **Crew**: 1 Engineer crew card required
- **Strategic Use**: Redundancy for critical systems (radar, fire control remain online if engines damaged)

**Emergency Power Systems:**
- Prevents total ship shutdown if all main engines destroyed
- Large variant keeps radar, fire control, and communications online
- 50% speed capability on auxiliary power alone

---

### Fuel Purification System

**Size**: 1x2

**Effects**: +10% fuel efficiency, allows use of lower-grade fuel without engine damage

**Specifications:**
- **Weight**: 15 tons
- **Crew**: 1 Engineer crew card required
- **Strategic Use**: Long-range missions, economic fuel savings

**Fuel Economics:**
- Standard fuel: ₡100 per unit
- Lower-grade fuel: ₡60 per unit (40% cost reduction)
- Without purification system: Lower-grade fuel causes engine damage over time
- With purification system: Lower-grade fuel operates safely + 10% efficiency bonus

---

### Engine Governor

**Size**: 1x1

**Effects**: Toggle between modes:
- **Speed Mode**: +5% max speed, normal fuel consumption
- **Economy Mode**: Normal speed, +15% fuel efficiency

**Specifications:**
- **Weight**: 8 tons
- **Crew**: 1 Engineer crew card required
- **Strategic Use**: Flexibility for different mission phases (speed for combat, economy for transit)

**Mode Switching:**
- Can toggle modes at any time (even during combat)
- 30-second transition time between modes
- Visual indicator on ship UI shows current mode

---

## Storage & Logistics Modules

### Expanded Magazine

**Sizes**: 2x2 (Small), 2x3 (Medium), 3x3 (Large)

**Effects**: Installed in equipment slot (does not occupy cargo grid), increases ammunition stacking capacity
- **Small**: Ammunition stacks +20% larger (e.g., 5-inch shells stack to 120 instead of 100), 40 tons weight
- **Medium**: Ammunition stacks +40% larger (e.g., 5-inch shells stack to 140 instead of 100), 75 tons weight
- **Large**: Ammunition stacks +60% larger (e.g., 5-inch shells stack to 160 instead of 100), 120 tons weight

**Specifications:**
- **Crew**: 1 Support crew card required
- **Strategic Use**: Extended combat operations, more ammunition per cargo grid cell
- **Equipment Slot**: Occupies support module equipment slot (2x2, 2x3, or 3x3 depending on size)

**Ammunition Storage Mechanics:**
- All ammunition stored in unified ship cargo grid (same as other items)
- Expanded Magazine increases stack sizes, NOT grid capacity
- More ammunition per grid cell = better cargo efficiency
- Does not create separate ammunition inventory
- Critical for sustained engagements without increasing cargo grid usage

---

### Refrigeration Unit

**Sizes**: 1x2 (Basic), 2x2 (Advanced)

**Effects:**
- **Basic**: Extends supply lifetime by 100% (food/medical supplies don't spoil), +5 morale
- **Advanced**: Extends supply lifetime by 200%, +10 morale, allows 30+ day voyages

**Specifications:**
- **Weight**: 20 tons (Basic), 35 tons (Advanced)
- **Crew**: 1 Support crew card required
- **Strategic Use**: Long-range operations, crew morale maintenance

**Supply Spoilage Mechanics:**
- Without refrigeration: Supplies spoil after 7 days at sea
- Basic refrigeration: Supplies last 14 days
- Advanced refrigeration: Supplies last 21 days
- Spoiled supplies reduce morale and crew efficiency

---

### Cargo Expansion Module

**Sizes**: 2x2 (Small), 2x3 (Large)

**Effects**: Adds +20-40 grid inventory cells (expands total cargo grid size per [[Inventory-System]])
- **Small**: +20 cells, 50 tons weight penalty (contributes to soft cap, see [[Inventory-System]])
- **Large**: +40 cells, 95 tons weight penalty (contributes to soft cap, see [[Inventory-System]])

**Specifications:**
- **Crew**: 1 Support crew card required
- **Strategic Use**: Trade ships, resource extraction missions, maximizing loot capacity

**Cargo Grid Expansion:**
- Physically expands the tetris-style cargo grid from [[Inventory-System]]
- Allows more loot, resources, and trade goods
- Essential for dedicated extraction/salvage ships
- Weight penalty contributes to ship weight (soft cap penalties apply if over-weight, see [[Inventory-System]])

---

## Specialized Support Modules

### Smoke Generator

**Sizes**: 1x1 (Basic), 1x2 (Advanced)

**Effects**: Deployable smoke screen obscures ship from enemy vision
- **Basic**: 3 charges, 60-second smoke duration, 5-minute cooldown
- **Advanced**: 5 charges, 90-second smoke duration, 3-minute cooldown, larger smoke cloud

**Specifications:**
- **Weight**: 10 tons (Basic), 18 tons (Advanced)
- **Crew**: 1 Support crew card required
- **Refill**: Refillable at port (₡5,000 per charge)
- **Strategic Use**: Evasion during extraction, breaking line of sight, tactical positioning

**Smoke Mechanics:**
- Deploys visual smoke cloud (500m radius Basic, 800m radius Advanced)
- Blocks line of sight for both enemies and allies
- Wind affects smoke drift and duration
- Infrared/radar can still detect ships in smoke (vision only)

---

### Decoy Launcher

**Size**: 1x1

**Effects**: Launches chaff/decoys to confuse radar and torpedoes
- 10 charges per module
- 30% chance to deflect radar-guided weapons
- 20% chance to decoy torpedoes

**Specifications:**
- **Weight**: 8 tons
- **Crew**: 1 Support crew card required
- **Refill**: ₡3,000 per charge
- **Strategic Use**: Defensive countermeasures, high-tier zone survival

**Decoy Mechanics:**
- Active defense (must manually trigger when threat detected)
- Short window for effective deployment (2-3 seconds)
- Limited charges require strategic use
- Most effective against AI-guided weapons

---

### Salvage Equipment

**Sizes**: 2x3 (Basic), 3x3 (Advanced)

**Effects**: Required to salvage wrecks in extraction zones
- **Basic**: Salvage speed 100% (baseline), can salvage common/uncommon modules
- **Advanced**: Salvage speed 200%, can salvage rare/exceptional modules, better loot quality

**Specifications:**
- **Weight**: 60 tons (Basic), 95 tons (Advanced)
- **Crew**: 1 Engineer crew card required
- **Strategic Use**: Dedicated salvage ships, extraction profession, wreck looting

**Salvage Mechanics:**
- Must be within 200m of wreck to initiate salvage
- Salvage time: 30 seconds - 5 minutes depending on wreck size and module rarity
- Advanced equipment doubles salvage speed (15 sec - 2.5 min)
- Salvaged modules may be damaged (20-100% condition)
- Salvaged items stored in ship cargo grid (see [[Inventory-System]] for grid mechanics)

---

### Research Lab (Late-Tier Module)

**Size**: 2x3 (Basic), 3x3 (Advanced)

**Effects:**
- **Basic**: Allows blueprint research at sea (50% slower than port), grants +10% research points
- **Advanced**: Blueprint research at sea (normal speed), +25% research points, can analyze captured enemy equipment

**Specifications:**
- **Weight**: 40 tons (Basic), 70 tons (Advanced)
- **Crew**: 1 Support crew card required (Intelligence specialization)
- **Strategic Use**: Extended operations, faction progression optimization

**Research Capabilities:**
- Blueprint research normally requires port facilities
- Research Lab enables at-sea progression
- Advanced variant can reverse-engineer captured enemy modules
- +Research point bonus applies to all research conducted on ship

---

## Misc Slot Modules

**Slot Characteristics:**
- **Universal Acceptance**: Can accept ANY module type (engines, support, or misc-specific modules)
- **Variable Sizes**: Ship-specific (1x1 to 3x3 possible)
- **Quantity**: Lower than support slots (Destroyers: 2-4, Battleships: 6-12)
- **Crew Requirement**: Varies by module (typically Electronics crew cards)

---

## Detection & Electronics Modules

### Radar Systems

**Sizes**: 1x1 (Basic), 1x2 (Improved), 2x2 (Advanced), 2x3 (Late-War), 3x3 (Experimental)

**Progression Tiers:**
- **Basic Radar**: 30km detection range, basic target tracking
- **Improved Radar**: 50km range, improved accuracy
- **Advanced Radar**: 80km range, multi-target tracking (4 targets)
- **Late-War Integrated**: 120km range, IFF system, 8 targets
- **Experimental AEGIS**: 150km range, full multi-target (12 targets), air defense coordination

**Specifications:**
- **Weight**: 8-50 tons depending on tier
- **Crew**: 1 Radar Operator crew card required (Electronics class)
- **Strategic Use**: Vision control, fire control integration, air defense coordination

**Radar Mechanics:**
- Detection range = sphere around ship
- Targets appear on tactical map in real-time
- IFF (Identify Friend/Foe) distinguishes ally from enemy
- Multi-target tracking enables simultaneous fire control solutions
- See [Technology-Integration.md](Technology-Integration.md) for UI integration

---

### Sonar Systems (Destroyers/Submarines)

**Sizes**: 1x1 (Passive), 1x2 (Active)

**Types:**
- **Passive Sonar**: Detects underwater contacts 5-15km, silent operation
- **Active Sonar**: Detects underwater contacts 15-30km, reveals your position when pinging
- **Advanced Sonar**: Better depth detection, tracks torpedo trajectories, 30km range

**Specifications:**
- **Weight**: 10 tons (Passive), 18 tons (Active), 28 tons (Advanced)
- **Crew**: 1 Radar Operator crew card required
- **Strategic Use**: Anti-submarine warfare, submarine hunting, torpedo defense

**Sonar Mechanics:**
- Passive: Silent detection via listening (enemy engine noise, propeller sounds)
- Active: Emits ping to actively detect submarines (reveals your position)
- Advanced: Can track torpedo trajectories (provides torpedo warning 10-20 sec before impact)
- Depth detection critical for submarine combat

---

### Hydrophones (Submarines)

**Size**: 1x1

**Effects**: Ultra-long-range passive detection (30-50km), detects engine noise and propeller signatures
- Cannot determine exact position, only general bearing and approximate distance
- Silent operation (no active pinging)

**Specifications:**
- **Weight**: 6 tons
- **Crew**: 1 Radar Operator crew card required
- **Strategic Use**: Submarine stealth operations, convoy detection, strategic positioning

**Hydrophone Mechanics:**
- Detects surface ships via acoustic signature
- Cannot detect stationary or drifting ships (no engine noise)
- Poor accuracy (bearing only, distance estimate ±10km)
- Excellent for strategic awareness, poor for tactical combat

---

## Electronic Warfare Modules

### Radar Jammer

**Sizes**: 1x1 (Basic), 1x2 (Advanced)

**Effects:**
- **Basic**: Reduces enemy radar detection range by 20%, interferes with fire control radar (-10% enemy accuracy)
- **Advanced**: Reduces enemy radar detection range by 50%, severe fire control interference (-25% enemy accuracy)
- Active use alerts enemies to your presence

**Specifications:**
- **Weight**: 12 tons (Basic), 22 tons (Advanced)
- **Crew**: 1 Electronics crew card required
- **Strategic Use**: Stealth operations, countering radar-heavy enemies, extraction evasion

**Jamming Mechanics:**
- Toggle on/off at will
- While active: Enemies detect you at reduced range
- Side effect: Broadcasts "jamming signal" revealing general direction
- Trade-off: Harder to detect precisely, but enemies know you're there

---

### Signal Intelligence (SIGINT) Module

**Size**: 1x2

**Effects:**
- Intercepts enemy radio communications
- Detects enemy positions via radio triangulation (rough bearing, 50km range)
- Provides early warning of enemy fleet movements
- Can decode encrypted messages with time delay

**Specifications:**
- **Weight**: 15 tons
- **Crew**: 1 Electronics crew card required (SIGINT specialization)
- **Strategic Use**: Intelligence gathering, fleet coordination, strategic awareness

**SIGINT Capabilities:**
- Passive detection (no emission)
- Reveals enemy chat messages in range (delayed by 30-60 sec)
- Triangulation provides approximate enemy position (±5km accuracy)
- High-level intelligence tool for organized play

---

### Decoy Transmitter

**Size**: 1x1

**Effects:**
- Emits false radar signature (makes ship appear larger/different class)
- 5 charges, refillable at port
- Limited duration (5 minutes per charge)
- Effective against AI, experienced players may detect deception

**Specifications:**
- **Weight**: 8 tons
- **Crew**: 1 Electronics crew card required
- **Refill**: ₡8,000 per charge
- **Strategic Use**: Psychological warfare, bluffing, extraction deception

**Deception Mechanics:**
- Appears as different ship class on enemy radar
- Can make destroyer appear as battleship (intimidation)
- Can make battleship appear as cruiser (ambush)
- Experienced players may notice speed/maneuver inconsistencies

---

## Fire Control & Targeting Modules

### Optical Rangefinder

**Sizes**: 1x1 (Basic), 1x2 (Advanced)

**Effects:**
- **Basic**: +5% accuracy for main battery, works when radar damaged
- **Advanced**: +10% accuracy, better vs small/fast targets, weather-resistant

**Specifications:**
- **Weight**: 6 tons (Basic), 12 tons (Advanced)
- **Crew**: 1 Gunner crew card required (Fire Control specialization)
- **Stacking**: Stacks additively with fire control computers
- **Strategic Use**: Backup targeting, radar-denied environments, destroyer combat

**Rangefinder Mechanics:**
- Optical-only (no electronic signature)
- Works in all weather (Advanced variant resistant to fog/rain)
- Manual crew-operated system (immune to electronic warfare)
- Essential backup if radar/fire control damaged

---

### Fire Control Computer

**Sizes**: 1x1 (Basic Optical), 1x2 (Mechanical), 2x2 (Electronic Analog), 2x3 (Digital), 3x3 (AI-Assisted)

**Progression Tiers:**
- **Basic Optical**: +5% accuracy, 1 target
- **Mechanical**: +15% accuracy, 2 targets
- **Electronic Analog**: +30% accuracy, 4 targets
- **Digital**: +50% accuracy, 8 targets
- **AI-Assisted**: +75% accuracy, 12 targets

**Specifications:**
- **Weight**: 5-50 tons depending on tier
- **Crew**: 1 Gunner crew card required (Fire Control specialization)
- **Strategic Use**: Gunnery accuracy enhancement, multi-target engagements, competitive edge

**Fire Control Integration:**
- Integrates with radar for target tracking
- Calculates lead, drop, and wind compensation automatically
- Multi-target capability allows simultaneous engagement
- See [Technology-Integration.md](Technology-Integration.md) for detailed mechanics

---

### Torpedo Fire Control

**Size**: 1x1

**Effects:**
- Calculates torpedo intercept solutions automatically
- +20% torpedo hit rate vs maneuvering targets
- Can pre-program torpedo spread patterns
- Shows predicted impact points on tactical display

**Specifications:**
- **Weight**: 8 tons
- **Crew**: 1 Torpedoman crew card required
- **Strategic Use**: Torpedo accuracy, destroyer combat effectiveness, submarine lethality

**Torpedo Fire Control:**
- Displays intercept solution overlay on tactical screen
- Accounts for target speed, bearing, and torpedo speed
- Spread patterns: Narrow, Wide, Salvo, Sequential
- Critical for hitting maneuvering targets

---

## Defensive Systems

### Close-In Weapon System (CIWS) (Late-Tier Technology)

**Sizes**: 1x1 (Basic), 1x2 (Advanced)

**Effects:**
- Automated last-ditch defense vs aircraft and missiles
- **Basic**: +30% AA effectiveness within 2km, 500 rounds ammo capacity
- **Advanced**: +50% AA effectiveness within 3km, 1000 rounds, can engage missiles
- Limited ammunition, refillable at port

**Specifications:**
- **Weight**: 15 tons (Basic), 28 tons (Advanced)
- **Crew**: 1 AA Specialist crew card required
- **Refill**: ₡15,000 per ammo reload
- **Strategic Use**: Carrier defense, high-tier zone air threats, missile defense

**CIWS Mechanics:**
- Fully automated (no manual control)
- Engages closest threat automatically
- Ammo pool separate from main AA guns
- Advanced variant intercepts guided missiles (40% success rate)

---

### Torpedo Defense System

**Sizes**: 1x2 (Passive), 2x2 (Active)

**Types:**
- **Passive (Torpedo Nets)**: +20% chance to deflect torpedoes, always active, no ammo
- **Active (Counter-Torpedoes)**: Launches counter-torpedoes to intercept incoming torpedoes (40% intercept chance), 8 charges

**Specifications:**
- **Weight**: 25 tons (Passive), 45 tons (Active)
- **Crew**: 1 Damage Control crew card required
- **Refill**: ₡20,000 per counter-torpedo (Active only)
- **Strategic Use**: Battleship/carrier protection, submarine threat mitigation

**Defense Mechanics:**
- Passive: Automatic chance to deflect incoming torpedoes (RNG-based)
- Active: Manual trigger when torpedo detected (skill-based timing)
- Counter-torpedoes have 2-3 second intercept window
- Limited charges require strategic use (save for multiple torpedo spreads)

---

### Countermeasure Dispenser

**Size**: 1x1

**Effects:**
- Launches chaff vs radar-guided weapons (50% effectiveness)
- Launches flares vs heat-seeking weapons (60% effectiveness, late-war/modern)
- 20 charges total, refillable

**Specifications:**
- **Weight**: 10 tons
- **Crew**: 1 Support crew card required
- **Refill**: ₡2,000 per charge
- **Strategic Use**: Missile defense (if game progresses to guided missile era)

---

## Special Systems

### Submarine Periscope (Submarines Only)

**Size**: 1x1

**Effects:**
- Required for surfaced/periscope depth observation
- **Basic**: Visual observation only, 5km range
- **Advanced**: Integrated rangefinder, 8km range, camera system for intelligence

**Specifications:**
- **Weight**: 4 tons (Basic), 7 tons (Advanced)
- **Crew**: 1 Command crew card required
- **Strategic Use**: Mandatory submarine module, periscope depth operations

---

### Snorkel System (Submarines Only)

**Size**: 1x1

**Effects:**
- Allows diesel engine use while submerged at shallow depth (15m)
- Increases submerged endurance dramatically (10x battery life)
- Slight speed reduction vs surfaced (80% max speed)
- Detectable by radar when snorkeling

**Specifications:**
- **Weight**: 6 tons
- **Crew**: 1 Engineer crew card required
- **Strategic Use**: Extended submerged operations, battery management

---

### Aircraft Catapult Control (Ships with Catapult Hardpoints)

**Size**: 1x1

**Effects:**
- Required to operate aircraft catapults
- Can launch scout planes for reconnaissance
- Provides over-horizon targeting data (+20km fire control range)
- Aircraft return time: 10-20 minutes

**Specifications:**
- **Weight**: 8 tons
- **Crew**: 1 Aviation crew card required
- **Strategic Use**: Battleship/cruiser reconnaissance, spotting for long-range fire

---

### Mining Equipment (Destroyers/Cruisers)

**Sizes**: 2x2 (Basic), 2x3 (Advanced)

**Effects:**
- Allows deployment of naval mines
- **Basic**: Stores 5 mines, basic contact mines
- **Advanced**: Stores 20 mines, magnetic/acoustic mine options
- Mines persist in world for 24 hours real-time or until detonated

**Specifications:**
- **Weight**: 45 tons (Basic), 80 tons (Advanced)
- **Crew**: 1 Torpedoman crew card required
- **Refill**: ₡25,000 per mine
- **Strategic Use**: Area denial, defensive operations, trap setting

---

## Summary & Integration

**Complete Utility Module System Includes:**

✅ **Crew Welfare Modules**: Quarters, Mess Hall, Medical Bay, Recreation Room
✅ **Engineering Support**: Damage Control, Machine Shop, Auxiliary Generator, Fuel Purification, Engine Governor
✅ **Logistics Modules**: Expanded Magazine, Refrigeration, Cargo Expansion
✅ **Specialized Support**: Smoke Generator, Decoy Launcher, Salvage Equipment, Research Lab
✅ **Detection Systems**: Radar, Sonar, Hydrophones
✅ **Electronic Warfare**: Radar Jammer, SIGINT, Decoy Transmitter
✅ **Fire Control**: Optical Rangefinder, Fire Control Computer, Torpedo Fire Control
✅ **Defensive Systems**: CIWS, Torpedo Defense, Countermeasures
✅ **Special Systems**: Submarine Periscope, Snorkel, Aircraft Catapult Control, Mining Equipment

**Integration Points:**
- Module System: All utility modules fit within Support/Misc slot categories
- Technology Integration: Advanced modules transform ship UI and capabilities
- Combat System: Detection, fire control, and defensive modules critical for combat effectiveness
- Crew System: All modules require appropriate crew cards for operation

See [Technology-Integration.md](Technology-Integration.md) for how these modules transform ship capabilities and UI features.

---

**End of Utility Modules Specification**
