---
tags: [planned, phase2, world-design, open-world]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-18
---

# World Exploration & Risk System

## Overview
The entire game world is fully explorable from day one by all players regardless of ship tier. Risk is determined entirely by **ship tier** (T1-T10), not by location or "zones." Players can sail anywhere with any ship, but higher-tier ships face exponentially greater permadeath risk when destroyed, creating natural risk/reward decisions about which ship to take on each expedition.

**Core Philosophy**: Ship value determines stakes, not location. A T10 battleship is at massive risk everywhere on the map due to 100% permadeath, while a T3 destroyer faces zero permadeath risk anywhere.

## Implementation Status
**Status**: 📋 PLANNED
**Phase**: Phase 2 (Economy & Progression)
**Dependencies**: [[Ocean-Environment]], [[Ship-Progression-System]], [[Economy-System]]
**Priority**: HIGH - Foundation for risk/reward gameplay

---

## Design Specification

### Ship Tier-Based Permadeath System

**Ship Tier Determines All Risk**:
- **T1-T5 ships**: 0% ship/crew card permadeath (completely safe everywhere on map)
- **T6 ships**: 10% permadeath on destruction
- **T7 ships**: 20% permadeath on destruction
- **T8 ships**: 40% permadeath on destruction
- **T9 ships**: 60% permadeath on destruction
- **T10 ships**: 100% permadeath on destruction (GUARANTEED LOSS)

**Key Principle**: Location does NOT modify these percentages. A T8 ship has 40% permadeath risk whether destroyed near home port or deep in enemy waters.

---

## Hidden Area Danger Structure (Design Internal)

**Note**: This structure is NOT advertised to players. It exists for content distribution and NPC scaling, but players discover it organically through exploration.

### Area Danger Levels (Internal Design)

#### Safe Waters (Near Major Ports)
**Design Purpose**: Tutorial area, new player safety

**Characteristics**:
- **NPC Presence**: Minimal - patrol boats, merchant convoys
- **NPC Difficulty**: Easy (T1-T3 equivalent threats)
- **Resource Quality**: Basic - common materials, low-value loot
- **PvP Dynamics**: Port guns protect nearby waters, but not absolute safety
- **Environmental Conditions**: Calm seas, good visibility
- **Mission Availability**: Tutorial missions, basic cargo runs

**Player Experience**: Safe area for learning mechanics with low-tier ships. High-tier ships attract player attention but face no additional penalties.

---

#### Protected Waters (National Territory)
**Design Purpose**: Early progression, T1-T4 ship operations

**Characteristics**:
- **NPC Presence**: Moderate - destroyers, light cruisers, occasional heavy units
- **NPC Difficulty**: Moderate (T3-T5 equivalent threats)
- **Resource Quality**: Common - standard materials, decent loot
- **PvP Dynamics**: Friendly NPC patrols may assist, enemies hunted by NPCs
- **Environmental Conditions**: Occasional weather, moderate visibility
- **Mission Availability**: Standard missions, convoy escorts, patrol duties

**Player Experience**: Relatively safe for progression. T5 ships can farm safely here. T6+ ships become valuable targets.

---

#### Contested Waters (Border Regions)
**Design Purpose**: Mid-tier ship operations, T5-T7 optimal

**Characteristics**:
- **NPC Presence**: Heavy - cruisers, battleships, small fleets
- **NPC Difficulty**: Challenging (T5-T7 equivalent threats)
- **Resource Quality**: Good - valuable materials, quality loot
- **PvP Dynamics**: No NPC protection, all players equal targets
- **Environmental Conditions**: Frequent storms, variable visibility
- **Mission Availability**: Dangerous missions, high-value contracts

**Player Experience**: First area where PvP becomes intense. T6 ships risk 10% permadeath, making encounters meaningful.

---

#### Dangerous Waters (Deep Ocean)
**Design Purpose**: High-tier operations, T7-T9 optimal

**Characteristics**:
- **NPC Presence**: Elite - battleship task forces, carrier groups
- **NPC Difficulty**: Very Challenging (T7-T9 equivalent threats)
- **Resource Quality**: Excellent - rare materials, high-value loot, unique drops
- **PvP Dynamics**: Ruthless - high-value targets hunted aggressively
- **Environmental Conditions**: Harsh weather, night combat, limited visibility
- **Mission Availability**: Elite contracts, strategic objectives, faction warfare

**Player Experience**: High-stakes combat. T8-T9 ships face 40-60% permadeath risk. Only for experienced players with backup ships.

---

#### Enemy Core Waters (Capital Regions)
**Design Purpose**: T10 operations, end-game content

**Characteristics**:
- **NPC Presence**: Overwhelming - super battleships, carrier strike groups, entire fleets
- **NPC Difficulty**: Nightmare (T10 equivalent threats)
- **Resource Quality**: Unmatched - legendary materials, unique items, massive rewards
- **PvP Dynamics**: Total war - everyone vs everyone, no mercy
- **Environmental Conditions**: Apocalyptic - hurricanes, darkness, extreme danger
- **Mission Availability**: Strategic operations, server-defining objectives

**Player Experience**: Ultimate risk environment. T10 ships face 100% guaranteed permadeath. Only bring expendable ships or accept total loss.

---

## Geographic Distribution (Design Internal)

### Map Layout Philosophy
The map is designed with natural risk progression from center (safe) to edges (dangerous), but this is NOT enforced or advertised.

**Core Region (Map Center)**:
- Major faction capitals and primary ports
- Safe/Protected water characteristics
- Naturally attracts new players
- High-tier ships visible but not common

**Mid-Ocean (Between Capitals)**:
- Contested water characteristics
- Natural battlegrounds between factions
- Mixed ship tiers common
- Active PvP hotspots

**Deep Ocean (Map Periphery)**:
- Dangerous water characteristics
- Rare resources and elite NPCs
- High-tier ships more common
- Experienced player territory

**Enemy Capitals (Opposing Faction Centers)**:
- Enemy core water characteristics
- Highest rewards and difficulty
- T10 operations common
- Server events and major battles

---

## Distance-Based Systems

### Respawn Mechanics

**Distance from Nearest Friendly Port**:
- **0-50km**: Respawn at nearest friendly port (fast return)
- **50-150km**: Respawn at nearest major port (moderate return time)
- **150-300km**: Respawn at regional hub port (long return)
- **300km+**: Respawn at home faction capital (very long return)

**Purpose**: Farther from safety = longer recovery time, but NO additional permadeath risk.

---

### Emergency Beacon System

**Beacon Effectiveness by Distance**:

**Near Friendly Ports (0-50km)**:
- **Beacon Range**: 50km effective radius
- **Response Time**: 2-5 minutes
- **Success Rate**: 95% (friendly NPCs/players nearby)
- **Rescue Options**: Multiple responders available

**Mid-Range (50-150km)**:
- **Beacon Range**: 25km effective radius
- **Response Time**: 5-15 minutes
- **Success Rate**: 70% (some friendlies in range)
- **Rescue Options**: Limited responders

**Far from Ports (150-300km)**:
- **Beacon Range**: 10km effective radius
- **Response Time**: 15-30 minutes
- **Success Rate**: 30% (rarely anyone nearby)
- **Rescue Options**: Minimal, player-dependent

**Deep Waters (300km+)**:
- **Beacon Range**: 5km effective radius
- **Response Time**: 30+ minutes (if anyone responds)
- **Success Rate**: 10% (almost never rescued)
- **Rescue Options**: Player mercy only

**Purpose**: Creates tension in remote areas without modifying permadeath rates.

---

### Insurance System

**Ship Tier-Based Insurance**:
- T1-T5: No insurance needed (0% permadeath)
- T6: 30,000 credits (reduces 10% → 5% permadeath)
- T7: 50,000 credits (reduces 20% → 10% permadeath)
- T8: 150,000 credits (reduces 40% → 25% permadeath)
- T9: 300,000 credits (reduces 60% → 40% permadeath)
- T10: 1,000,000+ credits (reduces 100% → 70% permadeath)

**Distance Multiplier** (from insured port):
- **0-100km**: Base insurance cost (1.0x multiplier)
- **100-200km**: +25% cost (1.25x multiplier)
- **200-400km**: +50% cost (1.5x multiplier)
- **400km+**: +100% cost (2.0x multiplier)

**Example**: T8 ship insured at home port (150k credits) but destroyed 350km away = insurance only pays out 50% value due to distance penalty.

**Purpose**: Encourages players to insure before long-range expeditions while keeping base permadeath rates unchanged.

---

## Player Warning Systems

### Undocking Warnings (T6+ Ships)

**Warning Trigger**: When player attempts to undock with T6+ ship

**UI Warning Display**:
```
⚠️ HIGH-RISK SHIP DEPARTURE WARNING ⚠️

You are undocking a [TIER X] [SHIP CLASS]

PERMADEATH RISK: XX% if destroyed in combat
- Ship permanently destroyed: YES (XX% chance)
- All crew cards permanently lost: YES (XX% chance per card)
- Sailor casualties: Always (replaceable at ports)

ESTIMATED VALUE AT RISK:
- Ship replacement cost: XXX,XXX,XXX credits
- Crew cards total investment: XXX hours / XXX,XXX,XXX credits
- Installed modules value: XX,XXX,XXX credits

Insurance available: YES / NO (XXX,XXX credits)

[CONFIRM DEPARTURE] [RETURN TO PORT] [PURCHASE INSURANCE]
```

**Confirmation Required**: Player must explicitly confirm for T8+ ships

**Audio Cue**: Tense music when undocking T9-T10 ships

---

### In-Game Risk Indicators

**Ship HUD Display** (always visible when at sea):
- **Permadeath Risk**: "XX% PERMADEATH" banner at top
- **Distance from Port**: "XXkm from [PORT NAME]"
- **Beacon Effectiveness**: "Rescue chance: XX%"
- **Estimated Return Time**: "Respawn return: XX minutes"

**Purpose**: Constant awareness of ship value and risk without zone boundaries.

---

## NPC Scaling (Design Internal)

### Dynamic NPC Threat Levels

**NPC Spawn Logic**:
- NPCs scale to area danger level (hidden structure)
- NPC difficulty increases with distance from major ports
- Elite NPCs spawn in dangerous/enemy waters
- Tutorial NPCs near safe ports

**NPC Target Selection**:
- NPCs prioritize higher-tier ships as threats
- T10 ships attract aggressive NPC response
- T1-T5 ships often ignored by high-tier NPCs
- Faction-specific targeting (enemy nationals hunted)

**NPC Fleet Composition**:
- Safe waters: Patrol boats, light destroyers
- Protected waters: Destroyer squadrons, cruiser patrols
- Contested waters: Mixed fleets, occasional capital ships
- Dangerous waters: Battleship task forces, carrier groups
- Enemy core: Super-battleships, full naval armadas

**Purpose**: Creates organic difficulty scaling without explicit zones.

---

## Resource Distribution (Design Internal)

### Loot Sources

**Ship Destruction Loot** (Tier-Based):
- **T1-T3 Ships**: Basic materials, common components (10-50k credits value)
- **T4-T6 Ships**: Quality materials, rare components (100-500k credits value)
- **T7-T9 Ships**: Rare materials, elite components (1-5M credits value)
- **T10 Ships**: Legendary materials, unique components (10-50M credits value)

**Mission Loot** (Difficulty-Based):
- **Easy Missions**: Low rewards, safe near ports
- **Medium Missions**: Moderate rewards, contested areas
- **Hard Missions**: High rewards, dangerous areas
- **Elite Missions**: Exceptional rewards, enemy core waters

**Resource Gathering** (Location-Based):
- **Near Ports**: Common resources, low yield
- **Open Ocean**: Quality resources, moderate yield
- **Remote Areas**: Rare resources, high yield
- **Enemy Waters**: Unique resources, exceptional yield

**Salvage Nodes**:
- **Wreckage Sites**: Scattered randomly, higher density in contested/dangerous areas
- **Historical Wrecks**: Rare spawns in deep waters, very high value
- **Debris Fields**: Post-battle areas, temporary high-value gathering

**Purpose**: Better loot farther from safety, but NO permadeath modifiers.

---

## Environmental Conditions (Design Internal)

### Weather Patterns

**Calm Zones** (near ports):
- Clear weather 70% of time
- Light rain/fog occasionally
- Rare storms
- Good visibility

**Variable Zones** (mid-ocean):
- Mixed weather patterns
- Moderate storms common
- Day/night cycles matter
- Reduced visibility

**Harsh Zones** (remote/enemy waters):
- Frequent storms
- Poor visibility common
- Night operations dangerous
- Extreme weather events

**Purpose**: Environmental challenge increases with distance, not permadeath.

---

## PvP Dynamics

### Port Gun Protection

**Major Ports** (faction capitals):
- **Protection Radius**: 10km from port
- **Gun Damage**: Instant destruction for enemy nationals
- **Allied Protection**: Aggressive defense of faction members
- **Warning**: "ENTERING PORT GUN RANGE" at 12km

**Secondary Ports**:
- **Protection Radius**: 5km from port
- **Gun Damage**: High but not instant
- **Allied Protection**: Defensive only
- **Warning**: "PORT DEFENSE ACTIVE"

**Outposts**:
- **Protection Radius**: 2km from port
- **Gun Damage**: Moderate deterrent
- **Allied Protection**: Minimal
- **Warning**: "PORT GUNS ONLINE"

**Open Water** (everywhere else):
- No protection
- All players equal targets
- Ship tier determines value/risk
- Natural PvP battlegrounds

---

## Faction Territory (Design Internal)

### Territorial Control (Hidden System)

**Core Territory** (near faction capitals):
- High friendly NPC presence
- Enemy nationals hunted by NPCs
- Ports numerous and well-protected
- Safe for allied ships

**Border Territory** (between factions):
- Contested control
- Mixed NPC presence
- Neutral zones
- PvP hotspots

**Enemy Territory** (opposing faction centers):
- Hostile NPC presence
- Allied ships hunted
- Few friendly ports
- High risk for deep penetration

**Neutral Waters** (unclaimed ocean):
- No faction control
- Rare NPC presence
- Player-driven dynamics
- Natural hunting grounds

**Purpose**: Creates faction warfare dynamics without explicit zone boundaries.

---

## Strategic Navigation

### Player Decision-Making

**Choosing a Ship for Expedition**:

**T1-T5 Ships (0% Permadeath)**:
- ✅ Safe everywhere on map
- ✅ Can explore freely without risk
- ✅ Perfect for scouting and learning
- ❌ Low combat power
- ❌ Poor loot from ship kills
- ❌ Can't access high-tier missions

**T6-T7 Ships (10-20% Permadeath)**:
- ✅ Good combat power
- ✅ Reasonable risk levels
- ✅ Access to quality missions
- ⚠️ First real permadeath risk
- ⚠️ Attracts PvP attention
- ❌ Still not elite-tier loot

**T8-T9 Ships (40-60% Permadeath)**:
- ✅ Elite combat power
- ✅ Best loot from kills
- ✅ Access to elite missions
- ⚠️ Very high permadeath risk
- ⚠️ Major PvP target
- ⚠️ Massive economic loss if destroyed

**T10 Ships (100% Permadeath)**:
- ✅ Ultimate combat power
- ✅ Legendary loot potential
- ✅ Server-defining presence
- ❌ GUARANTEED TOTAL LOSS if destroyed
- ❌ Entire server hunts you
- ❌ Only bring expendable T10 or accept loss

---

### Expedition Planning

**Risk Assessment Questions**:
1. How far from friendly ports will I travel?
2. What ship tier matches mission difficulty?
3. Can I afford permadeath loss on this ship?
4. Is insurance worth the cost for this expedition?
5. Do I have backup ships if this one is lost?
6. What's my escape plan if ambushed?

**Example Decision Tree**:
- **Farming Credits (low risk)**: T4-T5 ship, stay near ports, 0% permadeath
- **Quality Missions (moderate risk)**: T6-T7 ship, contested areas, insure for safety
- **Elite Operations (high risk)**: T8-T9 ship, dangerous areas, insurance mandatory, backup ships ready
- **Server Events (extreme risk)**: T10 ship, accept total loss, bring expendable builds

---

## Design Philosophy

### Why No Explicit Zones?

**Player Freedom**:
- Entire map explorable immediately
- No artificial barriers
- Player skill/knowledge determines success
- Organic discovery of dangerous areas

**Risk Clarity**:
- Ship tier = risk (simple, clear)
- Location = loot quality (not permadeath)
- No confusing zone penalty stacking
- Players understand exactly what they risk

**Emergent Gameplay**:
- Players create their own "safe" and "dangerous" areas through behavior
- High-tier ship sightings become events
- Natural formation of hunting grounds
- Community-driven risk assessment

**Design Benefits**:
- Simpler system to understand
- No zone boundary exploits
- More immersive (no UI walls)
- Better player agency

---

## Integration with Other Systems

### Depends On
- [[Ocean-Environment]] - Weather and environmental hazards
- [[Ship-Progression-System]] - Ship tier definitions
- [[Economy-System]] - Insurance pricing, loot values
- [[Permadeath-System]] - Ship/crew card loss mechanics
- [[Faction-System]] - Territory control and NPC behavior

### Used By
- [[Extraction-Mechanics]] - Safe return requirements
- [[PvP-Systems]] - Target value calculations
- [[Mission-System]] - Mission difficulty distribution
- [[Resource-Gathering]] - Resource node placement
- [[NPC-Behavior]] - Threat level scaling

---

## Success Metrics

### Player Behavior Indicators
- **Tier Adoption**: 60%+ players progress to T6+ ships
- **Map Exploration**: 80%+ of map visited by player base
- **Risk Assessment**: Players choose appropriate ships for expeditions
- **PvP Engagement**: Active combat in contested/dangerous areas
- **T10 Rarity**: <5% of active ships are T10 (due to 100% permadeath)

### Economic Health
- **Ship Loss Rates**: 5-10% of T6-T9 ships lost per week
- **Insurance Adoption**: 40-60% of high-risk expeditions insured
- **Loot Distribution**: Rare materials obtained from dangerous areas
- **Credit Flow**: Healthy economy from risk/reward balance

### Player Satisfaction
- **Risk Understanding**: 90%+ players understand ship tier = risk
- **Fair Losses**: <5% technical deaths (bugs/lag causing permadeath)
- **Exciting Gameplay**: High-tier ship encounters create memorable moments
- **Progression Feel**: Natural escalation from T1 to T10 operations

---

## Known Design Challenges

### Challenge 1: High-Tier Ship Griefing in Safe Areas
**Problem**: T10 ships camping near newbie ports, seal clubbing

**Mitigation**:
- Port gun ranges extended for T10 ships (auto-aggro radius)
- Reputation penalties for killing T1-T3 ships near safe ports
- Server-wide bounties on griefers
- Insurance fraud detection (intentional death for payout)

---

### Challenge 2: Risk-Averse Players Never Progress
**Problem**: Players stay in T1-T5 ships forever, avoid permadeath content

**Balance**:
- T6+ ships required for best missions/loot
- Social pressure from guilds/factions
- T1-T5 content caps out in progression
- Economic incentives for high-tier operations

---

### Challenge 3: "Where Should I Go?" Confusion
**Problem**: No explicit zones means new players don't know where to start

**Solution**:
- Tutorial missions guide players naturally outward from ports
- NPC dialogue hints at dangerous areas
- Player chat/community sharing of knowledge
- In-game map markers for mission locations (not zone boundaries)
- Veteran player mentorship programs

---

### Challenge 4: Hidden Areas Feel Arbitrary
**Problem**: Players don't understand why some areas are more dangerous

**Justification**:
- NPC density visible (fleets patrol dangerous areas)
- Environmental cues (storms in deep ocean)
- Geographic logic (enemy capitals heavily defended)
- Player word-of-mouth creates organic knowledge
- Mission difficulty descriptions hint at area danger

---

## Future Enhancements

### Planned Features
- **Dynamic Area Control**: Faction warfare shifts territorial boundaries
- **Weather Severity Zones**: Extreme weather in specific regions
- **Seasonal Events**: Temporary high-value areas
- **Player-Claimed Territory**: Guild bases establish safe zones
- **Convoy Systems**: NPC/player convoys create temporary safety

### Potential Additions
- **Fog of War**: Map exploration reveals area dangers
- **Reputation Zones**: Faction-specific safe/hostile areas based on standing
- **Tidal Mechanics**: Time-based area accessibility
- **Underwater Zones**: Submarine-specific dangerous areas

---

## Cross-References
- [[Game-Vision]] - Open-world exploration philosophy
- [[Permadeath-System]] - Ship tier-based risk system
- [[Ship-Progression-System]] - T1-T10 ship definitions
- [[Economy-System]] - Insurance and loot distribution
- [[PvP-Systems]] - Target value and hunting mechanics
- [[Faction-System]] - Territorial control and NPCs
- [[Ocean-Environment]] - Weather and environmental systems

---

## Changelog
- **2025-11-18**: Complete redesign from zone-based to ship-tier-only risk system - removed T0-T5 zone tiers, zone penalties, zone transitions; replaced with distance-based respawn/beacons and hidden area structure for design purposes only
- **2025-11-17**: Initial zone system document created with T0-T5 zone tiers (DEPRECATED)
