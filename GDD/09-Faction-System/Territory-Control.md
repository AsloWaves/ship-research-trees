---
tags: [planned, phase5, faction-system, territory, guilds]
status: 📋 PLANNED
phase: Phase 5 - MMO Scale
priority: HIGH
last-updated: 2025-12-22
---

# Territory Control System

## Overview

The Territory Control System enables player guilds (fleets/clans) to capture, hold, and develop strategic locations across the game world. Controlling territory provides economic benefits, strategic advantages, and server-wide prestige while creating meaningful large-scale PvP objectives.

**Core Philosophy**: Territory is valuable because it provides tangible benefits, but holding it requires active defense and investment - creating dynamic, contested frontlines that shift based on player activity.

## Implementation Status

**Status**: 📋 PLANNED
**Phase**: Phase 5 - MMO Scale
**Dependencies**: [[Guild-System]], [[Economy-System]], [[PvP-Systems]], [[Zone-System]]
**Priority**: HIGH - Core MMO feature for end-game content

---

## Design Specification

### Capturable Territory Types

#### Strategic Ports
**Description**: Major ports that can be contested and controlled by guilds

**Capture Mechanics**:
- **Siege Window**: 2-hour vulnerability windows (scheduled by defenders)
- **Capture Objective**: Destroy port defenses, hold control point for 30 minutes
- **Defense Mechanics**: NPC garrison + player defenders during siege
- **Minimum Attackers**: 10 players required to initiate siege

**Control Benefits**:
- **Tax Revenue**: 5-10% of all NPC trades at port go to controlling guild
- **Docking Fees**: Set custom docking fees for non-allied players
- **Market Control**: Priority listing on marketplace, reduced fees
- **Repair Discounts**: 25% discount on repairs for guild members
- **Spawn Point**: Guild members can respawn at controlled port

**Upkeep Costs**:
- **Daily Maintenance**: 50,000-200,000 credits (based on port tier)
- **Garrison Salary**: NPC defenders require ongoing payment
- **Infrastructure Repairs**: Siege damage must be repaired

---

#### Resource Nodes
**Description**: Valuable resource extraction points in the open ocean

**Types**:
- **Oil Fields**: Fuel production nodes
- **Salvage Sites**: Rare material recovery
- **Fishing Grounds**: Food/consumable production
- **Mining Platforms**: Metal ore extraction

**Capture Mechanics**:
- **No Siege Windows**: Always contestable (24/7)
- **Capture Method**: Destroy defending fleet, hold area for 15 minutes
- **Defense**: Player patrols only (no NPC garrison)

**Control Benefits**:
- **Resource Production**: Automatic resource generation (daily)
- **Exclusive Access**: Only controlling guild can harvest
- **Strategic Denial**: Deny resources to enemies

**Upkeep Costs**:
- **Patrol Commitment**: Must defend actively or lose control
- **No Daily Fee**: But requires player time investment

---

#### Strategic Chokepoints
**Description**: Narrow passages that control maritime traffic

**Examples**:
- Canal passages
- Strait entrances
- Island chains
- Harbor approaches

**Capture Mechanics**:
- **Fortification Building**: Construct defensive emplacements
- **Control Duration**: Must hold for 24 hours to claim
- **Contested State**: Multiple guilds can fight for same chokepoint

**Control Benefits**:
- **Toll Collection**: Charge passage fees to non-allied players
- **Intelligence**: See all ships passing through
- **Ambush Advantage**: Defensive bonuses in controlled waters
- **Blockade Capability**: Deny passage entirely (reputation consequences)

---

### Territory Warfare Mechanics

#### Siege System

**Declaration Phase**:
1. Attacker declares siege intent (24-hour warning to defenders)
2. Attacker pays siege declaration fee (100,000-500,000 credits)
3. Siege window is set (within defender's configured 2-hour vulnerability)
4. Server-wide announcement of upcoming siege

**Preparation Phase** (24 hours):
- Defenders can reinforce garrison
- Defenders can call allies for support
- Attackers gather fleet and resources
- Both sides can position scouts

**Siege Phase** (2 hours max):
- **Phase 1: Outer Defenses** (30 min) - Destroy harbor batteries
- **Phase 2: Inner Harbor** (30 min) - Eliminate garrison fleet
- **Phase 3: Control Point** (30 min hold required) - Capture command center
- **Victory**: Attackers hold control point for 30 continuous minutes
- **Defense Victory**: Timer expires with defenders holding

**Post-Siege**:
- 72-hour cooldown before territory can be sieged again
- Losing defenders cannot reclaim for 7 days
- Infrastructure damage affects territory benefits until repaired

---

#### Territory Influence System

**Influence Generation**:
- **Presence**: Guild ships in territory generate influence over time
- **Combat**: Winning battles in territory grants influence
- **Trade**: Economic activity increases influence
- **Missions**: Completing missions in territory grants influence

**Influence Decay**:
- Undefended territories lose influence daily
- Enemy activity accelerates influence loss
- Minimum 30% influence required to maintain control

**Influence Thresholds**:
- **100%**: Full control, maximum benefits
- **70%**: Contested status, reduced benefits
- **50%**: Vulnerable, can be attacked without siege
- **30%**: Control lost, reverts to neutral

---

### Guild Requirements

#### Territory Limits

| Guild Size | Max Territories | Port Limit |
|------------|-----------------|------------|
| Small (10-25) | 2 | 0 |
| Medium (25-50) | 5 | 1 |
| Large (50-100) | 10 | 2 |
| Mega (100+) | 20 | 5 |

#### Prerequisite Achievements
- **First Territory**: Guild Level 5, 500,000 credits in treasury
- **Strategic Port**: Guild Level 10, successful siege participation
- **Chokepoint**: Control 3 other territories first

---

### Territory Development

#### Upgradeable Structures

**Port Territories**:
- **Shipyard**: Unlock ship construction at controlled port
- **Drydock**: Faster/cheaper repairs
- **Warehouse**: Increased storage capacity
- **Market**: Better trade prices
- **Fortress**: Stronger siege defenses

**Resource Nodes**:
- **Extraction Efficiency**: +25/50/75% resource generation
- **Storage Silos**: Accumulate resources between collections
- **Defensive Platforms**: NPC defenders for resource nodes

**Chokepoints**:
- **Watchtowers**: Extended detection range
- **Coastal Batteries**: NPC artillery emplacements
- **Mining Fields**: Defensive mines (consumable)

---

## Technical Requirements

### Server Systems
- Territory ownership database
- Siege scheduling and state machine
- Influence calculation (hourly updates)
- Upkeep deduction (daily)
- Benefit application (real-time)

### Client Systems
- Territory map overlay (shows ownership)
- Siege UI (timers, objectives, participant list)
- Guild territory management panel
- Influence visualization

### Multiplayer Considerations
- Large-scale battle support (50+ players)
- Siege instance creation for performance
- Cross-shard territory (if multiple servers)

---

## Integration with Other Systems

### Depends On
- [[Guild-System]] - Guild structure and permissions
- [[Economy-System]] - Upkeep, taxes, development costs
- [[PvP-Systems]] - Combat mechanics during sieges
- [[Zone-System]] - Territory boundaries

### Used By
- [[Global-Economy]] - Territory affects market prices
- [[Reputation-System]] - Territory actions affect standing
- [[Mission-System]] - Territory-based missions
- [[Leaderboards]] - Territory control rankings

---

## Success Metrics

### Engagement Targets
- **Territory Contests**: 10+ sieges per week server-wide
- **Participation**: 40% of max-level guilds control territory
- **Defense Rate**: 50-60% of sieges successfully defended
- **Turnover**: Average territory held 2-4 weeks

### Economic Health
- **Upkeep Balance**: Territory profitable but requires management
- **Investment ROI**: Break-even in 2-4 weeks of control
- **Resource Distribution**: Territory doesn't monopolize resources

---

## Cross-References
- [[Guild-System]] - Guild management and permissions
- [[Economy-System]] - Credits and resource economy
- [[PvP-Systems]] - Player combat mechanics
- [[Zone-System]] - World structure and boundaries
- [[Large-Scale-Battles]] - Performance for big fights

---

## Changelog
- **2025-12-22**: Initial document creation from GitHub issue alignment
