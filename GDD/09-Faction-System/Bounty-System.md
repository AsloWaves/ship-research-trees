---
tags: [planned, phase4, faction-system, bounty, pvp, criminal]
status: PLANNED
phase: Phase 4 - Advanced Features
priority: HIGH
last-updated: 2025-12-22
---

# Bounty & Criminal System

## Overview

The Bounty & Criminal System creates meaningful consequences for player-versus-player aggression while enabling emergent piracy gameplay. Players who attack others unprovoked accumulate criminal status, while victims and factions can place bounties on aggressors. This system balances PvP freedom with consequences, creating a dynamic risk/reward landscape.

**Core Philosophy**: Freedom with consequences. Players can choose to be pirates, but piracy comes with real costs - bounties, faction hostility, and restricted access to safe zones. Conversely, bounty hunting becomes a viable profession.

## Implementation Status

**Status**: PLANNED
**Phase**: Phase 4 - Advanced Features
**Dependencies**: [[PvP-Systems]], [[Reputation-System]], [[Economy-System]], [[Zone-System]]
**Priority**: HIGH - Essential for PvP balance

---

## Design Specification

### Criminal Status System

#### Aggression Classification

**Lawful Combat** (No criminal penalty):
- Defending against attack (counter-attack within 5 minutes)
- War-declared faction members
- Players with existing bounties (bounty hunting)
- Mutual combat flag enabled (dueling)
- PvP zone combat (designated combat areas)
- Guild war participants

**Criminal Combat** (Penalty applied):
- First strike on neutral player
- Attacking players in safe/trade routes
- Port zone aggression
- Convoy attacks (NPC or player)
- Attacking lower-tier players (seal clubbing)

---

#### Criminal Heat Levels

| Level | Name | Heat Points | Duration | Consequences |
|-------|------|-------------|----------|--------------|
| 0 | Lawful | 0 | - | Full access everywhere |
| 1 | Suspect | 1-99 | 1 hour | NPCs won't defend you |
| 2 | Criminal | 100-499 | 4 hours | Denied port services |
| 3 | Outlaw | 500-999 | 24 hours | Attacked by faction patrols |
| 4 | Pirate Lord | 1000+ | 7 days | Kill-on-sight, max bounty |

**Heat Point Accumulation**:
| Action | Heat Points | Notes |
|--------|-------------|-------|
| Attack neutral player | +50 | Per engagement |
| Kill neutral player | +100 | Stacks with attack |
| Attack lower tier (2+ tiers) | +75 | Seal clubbing penalty |
| Kill lower tier player | +150 | Severe penalty |
| Convoy attack | +25 | Per convoy ship |
| Port zone aggression | +200 | Safe zone violation |
| Escape with cargo theft | +50 | Piracy bonus |

**Heat Decay**:
- Natural decay: -10 points per hour (offline or online)
- Accelerated decay: -25 per hour in lawful faction territory
- Bounty completion: -100 points (completing legitimate contracts)
- No decay while actively committing crimes

---

### Bounty System

#### Bounty Types

**Automatic Bounties** (System-Generated):
- Criminal Level 2+: Minimum 10,000 credits
- Scales with criminal heat: Heat × 100 credits
- Updates automatically with new crimes
- Paid from "Criminal Seizure Fund" (NPC economy)

**Player-Placed Bounties**:
- Minimum: 5,000 credits
- Maximum: 1,000,000 credits per target
- Placed by victim or any player
- Stacks with automatic bounties
- Escrow system (credits held until claimed or expired)

**Faction Bounties**:
- Placed by NPC factions for major offenders
- Higher payouts than player bounties
- Special rewards (faction items, reputation)
- Posted on faction bounty boards

---

#### Bounty Mechanics

**Placing a Bounty**:
1. Open Bounty Board (at any port)
2. Search for player by name
3. Enter bounty amount (escrowed immediately)
4. Optional: Add description/reason
5. Set duration (1 day to 30 days, affects fee)
6. Confirm placement (5% fee to bounty board)

**Bounty Information Visible**:
- Target name and last known ship
- Total bounty amount
- Number of contributors
- Criminal heat level
- Last known region (updated hourly)
- Kill count (crimes committed)

**Bounty Hunting**:
1. View active bounties at Bounty Board
2. Accept contract (optional, provides tracking)
3. Locate and eliminate target
4. Confirm kill (automatic if registered hunter)
5. Collect reward at any port

---

#### Bounty Payouts

**Payout Distribution** (Multiple hunters):
- **Killing Blow**: 50% of bounty
- **Damage Contribution**: 30% split by damage %
- **Spotter Bonus**: 10% to player who found target
- **Board Fee**: 10% retained by system

**Proof of Kill**:
- Automatic for registered bounty hunters
- Kill must occur in valid PvP zone
- Target must be criminal (Heat Level 1+) OR have active bounty
- Anti-exploit: No bounty for killing alts/friends

**Bounty Expiration**:
- Player bounties: Expire after set duration
- 80% refund to placer on expiration
- Automatic bounties: Never expire while criminal
- Faction bounties: Reset monthly with new targets

---

### Piracy Gameplay Loop

#### Becoming a Pirate

**Pirate Path**:
1. **Initiation**: First criminal act, Heat Level 1
2. **Commitment**: Sustained criminal activity, Heat Level 2-3
3. **Notoriety**: High bounty, faction hostility, Heat Level 4
4. **Pirate Lord**: Maximum criminal status, server-wide reputation

**Pirate Benefits**:
- Access to pirate havens (outlaw ports)
- Pirate faction reputation and missions
- Stolen cargo fencing (better rates at pirate ports)
- Pirate-exclusive equipment and ships
- Intimidation bonus (surrender demands more effective)

**Pirate Drawbacks**:
- Denied access to lawful ports
- Higher repair costs (black market)
- Faction patrols actively hunt
- Bounty hunters tracking constantly
- Limited safe zones

---

#### Pirate Havens

**Outlaw Ports**:
- Located in dangerous/remote regions
- No law enforcement
- Full services for criminals
- Higher prices, lower buy rates
- Player-run economy elements

**Haven Services**:
- Repairs (125% normal cost)
- Resupply (ammunition, provisions)
- Black market (fence stolen goods)
- Bounty board (pirate contracts)
- Crew recruitment (outlaw crew available)

---

### Redemption System

#### Clearing Criminal Status

**Time-Based Decay**:
- Heat naturally decays over time
- Faster decay in lawful territory
- Must avoid new crimes

**Active Redemption**:
| Method | Heat Reduction | Requirements |
|--------|----------------|--------------|
| Bounty Hunter Contract | -100 | Kill valid bounty target |
| Convoy Escort | -50 | Successfully protect NPC convoy |
| Faction Missions | -25 to -100 | Complete lawful faction work |
| Bribery | -200 | Pay faction (expensive) |
| Surrender | -500 | Turn self in (jail time) |

**Surrender System**:
- Turn yourself in at any lawful port
- Pay fine: Total bounty × 50%
- Serve "jail time": 1 hour per 100 heat (offline counts)
- Ship impounded (retrievable after sentence)
- Record cleared to Heat Level 0

---

#### Amnesty Events

**Periodic Amnesty** (Live Ops):
- Special events offering mass redemption
- Complete event objectives for heat reduction
- One-time opportunities for pirates to go lawful
- Creates gameplay variety and second chances

---

### Bounty Hunter Profession

#### Hunter Registration

**Requirements**:
- Clean record (Heat Level 0)
- Minimum reputation with lawful faction
- Registration fee: 25,000 credits
- License renewal: Monthly, 5,000 credits

**Hunter Benefits**:
- Access to full bounty information
- Target tracking assistance (region pings)
- Legal protection (no penalty for bounty kills)
- Bounty hunter missions from factions
- Exclusive equipment (tracking modules)

---

#### Hunter Ranks

| Rank | Requirement | Benefits |
|------|-------------|----------|
| Novice | Registration | Basic tracking, public bounties |
| Journeyman | 10 bounties claimed | Enhanced tracking, priority info |
| Expert | 50 bounties, 100K+ claimed | Faction bounties access, bonus % |
| Master | 200 bounties, 1M+ claimed | Exclusive contracts, guild creation |
| Legendary | 500+ bounties | Title, unique rewards, NPC references |

---

### Anti-Exploit Measures

#### Bounty Farming Prevention

**Friend/Alt Protection**:
- No bounty payout for killing:
  - Same IP address (flagged)
  - Guild members
  - Recent trade partners
  - Friends list members
- Suspicious patterns flagged for review

**Minimum Engagement**:
- Target must have dealt or received damage in last 24h
- Prevents "victim" from being paid to die
- AFK kills flagged

**Bounty Washing Prevention**:
- Cannot place bounty on self
- Bounty transfer blocked between alts
- Payout delays for large bounties (1 hour)

---

#### PvP Griefing Prevention

**Seal Clubbing Penalties**:
- 2+ tier difference: Double heat penalty
- 3+ tier difference: Triple heat penalty
- Repeat offenders: Escalating penalties

**Safe Zone Enforcement**:
- Port zones: Instant 200 heat + NPC retaliation
- Trade routes: 150 heat + patrol response
- Newbie zones: Automatic max heat + temp ban

**Combat Logging**:
- Disconnecting during combat: Ship remains for 60s
- Logged ship can be killed
- Full bounty/loot awarded to attacker

---

## Technical Requirements

### Server Systems
- Criminal status tracking database
- Bounty escrow and payout system
- Heat calculation engine
- Cross-server bounty synchronization
- Anti-exploit detection algorithms

### Client Systems
- Bounty board UI
- Criminal status indicator
- Hunter tracking interface
- Surrender/redemption interface
- Wanted poster generation

### Data Requirements
- Player criminal history
- Bounty transaction logs
- Hunter statistics
- Payout audit trail
- Exploit detection patterns

---

## Success Metrics

### System Balance
- **Pirate Population**: 5-15% of active players
- **Bounty Claim Rate**: 60%+ of bounties eventually claimed
- **Redemption Rate**: 40%+ of pirates eventually reform
- **Hunter Activity**: 10%+ of players participate in hunting

### Economy Health
- **Bounty Economy**: Net neutral (payouts ≈ placements)
- **Piracy Profitability**: Slightly above lawful (risk premium)
- **Hunter Profitability**: Sustainable profession

### Player Experience
- **Victim Satisfaction**: 70%+ feel bounty system is fair
- **Pirate Satisfaction**: 80%+ enjoy pirate gameplay loop
- **Hunter Satisfaction**: 75%+ find hunting rewarding

---

## Cross-References
- [[PvP-Systems]] - Combat mechanics for bounty hunting
- [[Reputation-System]] - Faction standing integration
- [[Economy-System]] - Bounty economy and fencing
- [[Zone-System]] - Safe zones and PvP areas
- [[Moderation-System]] - Exploit detection integration
- [[Territory-Control]] - Pirate haven mechanics

---

## Changelog
- **2025-12-22**: Initial document creation from GitHub issue alignment
