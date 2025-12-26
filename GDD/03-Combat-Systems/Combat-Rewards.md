---
tags: [planned, phase2, combat, rewards, ui]
status: PLANNED
phase: Phase 2 - Combat & Economy
priority: MEDIUM
last-updated: 2025-12-22
---

# Combat Rewards & Battle Results System

## Overview

The Combat Rewards System provides immediate feedback after combat encounters, displaying battle performance, damage statistics, kills, assists, and loot obtained. This is a mid-expedition results screen that appears after significant combat events, distinct from the [[Extraction-Mechanics]] which handles end-of-expedition processing at ports.

**Core Philosophy**: Immediate gratification and clear feedback on combat performance. Players should understand exactly what they accomplished, what rewards they earned, and how their actions contributed to victory or defeat.

## Implementation Status

**Status**: PLANNED
**Phase**: Phase 2 - Combat & Economy
**Dependencies**: [[Damage-Model]], [[Loot-System]], [[Crew-System]], [[Economy-System]]
**Priority**: MEDIUM - Important for player feedback loop

---

## Design Specification

### Battle Results Trigger Conditions

#### When Results Screen Appears

**Enemy Ship Destroyed**:
- Player dealt final blow OR
- Player dealt >25% of total damage AND was in combat range

**PvP Combat Concluded**:
- Enemy player ship destroyed
- Enemy player surrendered
- Combat disengaged (5+ minutes no hostilities)

**Fleet Battle Concluded**:
- All enemy fleet ships destroyed/retreated
- Flagship destroyed (ends battle regardless of remaining ships)
- Time limit reached (30 min max battle duration)

**Convoy/Mission Combat**:
- Protected convoy reaches destination
- Convoy destroyed
- All attackers eliminated

---

### Battle Results Screen Layout

#### Header Section

**Battle Summary Banner**:
- Victory/Defeat/Draw status (large, prominent)
- Battle duration (MM:SS format)
- Battle type indicator (Skirmish, Fleet Battle, Convoy Defense, etc.)
- Date/Time stamp

---

#### Performance Statistics Panel

**Damage Statistics**:
| Stat | Description | Display |
|------|-------------|---------|
| Total Damage Dealt | All damage to enemy ships | 45,230 |
| Hull Damage | Damage to hull specifically | 32,100 (71%) |
| Module Damage | Damage to enemy modules | 8,430 (19%) |
| Crew Casualties Inflicted | Enemy crew killed by your fire | 47 |
| Fires Started | Number of fires ignited | 3 |
| Flooding Caused | Flooding compartments created | 2 |

**Accuracy Statistics**:
| Stat | Description | Display |
|------|-------------|---------|
| Shots Fired | Total rounds expended | 234 |
| Hits | Rounds that connected | 156 |
| Accuracy | Hit percentage | 66.7% |
| Critical Hits | Penetrating/module hits | 23 |
| Citadel Hits | Magazine/engine room hits | 2 |

**Defensive Statistics**:
| Stat | Description | Display |
|------|-------------|---------|
| Damage Received | Total damage taken | 12,450 |
| Damage Blocked | Armor deflections | 8,200 |
| Repairs Made | HP restored during battle | 3,100 |
| Fires Extinguished | Fires put out | 1 |
| Flooding Controlled | Flooding compartments sealed | 1 |

---

#### Kill/Assist Breakdown

**Kills Section**:
```
KILLS (3)
├── [T5] USS Johnston (Destroyer) - 2,450 XP
│   └── Final blow + 78% damage contribution
├── [T4] Transport Vessel - 850 XP
│   └── Final blow + 100% damage contribution
└── [T6] Patrol Boat - 1,200 XP
    └── Final blow + 45% damage contribution
```

**Assists Section**:
```
ASSISTS (2)
├── [T7] Heavy Cruiser - 1,800 XP
│   └── 32% damage contribution (Ally: PlayerName got kill)
└── [T5] Supply Ship - 600 XP
    └── 15% damage contribution (Ally: PlayerName2 got kill)
```

**Kill Credit Formula**:
- **Kill**: Final blow OR >50% damage contribution
- **Assist**: 10-50% damage contribution
- **No Credit**: <10% damage contribution

---

#### Rewards Panel

**Experience Rewards**:
| Source | Amount | Modifier |
|--------|--------|----------|
| Base Combat XP | 4,500 | - |
| Kill Bonus | 2,200 | +49% |
| Assist Bonus | 800 | +18% |
| Damage Bonus | 1,100 | +24% |
| First Blood | 500 | +11% |
| **Total XP** | **9,100** | - |

**Credit Rewards**:
| Source | Amount | Modifier |
|--------|--------|----------|
| Combat Earnings | 12,000 | - |
| Bounty Claims | 5,000 | (if applicable) |
| Salvage Rights | 3,500 | - |
| Mission Bonus | 8,000 | (if mission) |
| **Total Credits** | **28,500** | - |

**Reputation Changes**:
- Faction A: +150 (Combat contribution)
- Faction B: -50 (Enemy faction penalty)
- Pirate Notoriety: +25 (if applicable)

---

#### Loot Obtained Panel

**Salvage from Battle**:
```
SALVAGE COLLECTED
├── Steel Plates (x45) - 2,250 credits
├── Copper Wiring (x12) - 1,800 credits
├── Ammunition Crates (x8) - 4,000 credits
├── [RARE] Naval Rangefinder - 15,000 credits
└── [EPIC] Experimental Engine Parts - 45,000 credits

Total Salvage Value: 68,050 credits
Cargo Space Used: 23/50 units
```

**Auto-Loot Settings**:
- Common materials: Auto-collect (toggleable)
- Rare+ items: Manual confirmation
- Cargo full: Priority queue (highest value first)

---

### Battle Modifiers & Bonuses

#### Combat Performance Bonuses

**Skill-Based Bonuses**:
| Achievement | Bonus | Trigger |
|-------------|-------|---------|
| First Blood | +500 XP | First kill of the battle |
| Devastating Strike | +200 XP | >50% enemy HP in single salvo |
| Double Strike | +300 XP | Two kills within 30 seconds |
| Kraken | +1000 XP | 5+ kills in single battle |
| Confederate | +400 XP | Damage 6+ enemy ships |
| High Caliber | +600 XP | >30% of team's total damage |
| Dreadnought | +500 XP | Survive with <10% HP |
| Fireproof | +300 XP | Extinguish 3+ fires |

**Teamwork Bonuses** (Fleet battles):
| Achievement | Bonus | Trigger |
|-------------|-------|---------|
| Spotter | +200 XP | Target you spotted was killed by ally |
| Defender | +300 XP | Kill enemy attacking ally with <25% HP |
| Fleet Support | +400 XP | Heal/repair allies for 10,000+ HP |

---

#### Penalties & Deductions

**Friendly Fire**:
- Warning at 1,000 damage to allies
- -10% rewards at 5,000 damage
- -50% rewards at 10,000 damage
- Battle rewards forfeit at 20,000+ damage

**Desertion**:
- Leave battle early (within 5 min of combat): -75% rewards
- AFK detection (2+ min no actions): -50% rewards

**Team Kill**:
- Killing allied ship: No rewards + reputation penalty

---

### Post-Battle Options

#### Action Buttons

**Continue Expedition**:
- Return to open ocean
- Keep all loot in cargo
- Repair available at next port

**Salvage More**:
- Spend additional time at wreck sites
- Risk: Other players may arrive
- Reward: Additional loot rolls

**Report Battle** (PvP):
- Flag suspicious behavior
- Submit for review
- Does not affect rewards

**Share Results**:
- Screenshot to clipboard
- Share to Discord (if linked)
- Save to battle history

---

### Battle History & Statistics

#### Personal Battle Log

**Recent Battles** (Last 50):
- Date/time
- Battle type
- Outcome
- Ship used
- XP/Credits earned
- Notable achievements

**Lifetime Statistics**:
- Total battles
- Win rate
- Average damage
- Kill/Death ratio
- Favorite ship
- Best performance records

---

### Special Battle Types

#### Convoy Battles

**Additional Metrics**:
- Cargo protected/lost value
- Convoy ships surviving
- Escort performance rating

**Bonus Structure**:
- Full convoy survival: +50% rewards
- >75% survival: +25% rewards
- <50% survival: No bonus

---

#### Fleet Battles (Guild Wars)

**Additional Metrics**:
- Contribution to team damage %
- Strategic objectives captured
- Flagship protection/destruction

**Guild Rewards**:
- Guild XP contribution
- Territory influence gain
- Guild treasury contribution

---

#### Historical Recreations (Events)

**Event-Specific Metrics**:
- Historical accuracy bonus
- Event-specific achievements
- Limited-time reward eligibility

---

## Technical Requirements

### Server Systems
- Battle instance tracking
- Real-time damage logging
- Kill/assist attribution
- Loot generation and distribution
- Anti-cheat validation

### Client Systems
- Results screen UI
- Statistics visualization
- Animation and effects
- Sound design for victory/defeat
- Screenshot functionality

### Data Requirements
- Battle event logging
- Player statistics aggregation
- Historical battle records
- Leaderboard integration

---

## Success Metrics

### Player Engagement
- **Results Screen View Time**: 15-30 seconds average
- **Share Rate**: 5%+ of battles shared
- **Return Rate**: 80%+ continue expedition after battle

### System Accuracy
- **Attribution Accuracy**: 99.9%+ correct kill/assist credit
- **Reward Calculation**: 100% accurate with audit trail
- **Loot Distribution**: Fair RNG with verification

---

## Cross-References
- [[Damage-Model]] - Damage calculation source data
- [[Loot-System]] - Salvage generation
- [[Extraction-Mechanics]] - End-of-expedition processing (different system)
- [[Economy-System]] - Credit rewards integration
- [[Reputation-System]] - Faction standing changes
- [[Achievement-System]] - Combat achievements

---

## Changelog
- **2025-12-22**: Initial document creation from GitHub issue alignment
