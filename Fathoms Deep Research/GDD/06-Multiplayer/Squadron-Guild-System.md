---
tags: [planned, design, multiplayer, social]
status: 📋 PLANNED
phase: Core Development
priority: HIGH
last-updated: 2025-12-03
---

# Squadron & Guild System

## Overview

The Squadron & Guild System provides two layers of player organization: **Squadrons** (ad-hoc groups that persist across missions and port visits) and **Fleets** (persistent guild-like organizations with structure, benefits, and long-term goals). This dual system accommodates both casual players wanting flexible group play and dedicated players seeking organized competitive content.

## Implementation Status
**Status**: 📋 PLANNED - Social organization framework
**Phase**: Core Development
**Priority**: HIGH - Essential for MMO social structure

---

## 1. Design Philosophy

### 1.1 Two-Tier Organization

**Squadrons** (Ad-hoc Groups):
- Persist across missions, port visits, and activities
- Any size from 2 to unlimited players
- No registration or commitment required
- Form instantly, stay grouped until members leave or log out
- Cross-nation compatible (if diplomatic state allows)

**Fleets** (Persistent Guilds):
- Permanent organizations with identity
- Formal structure with ranks and permissions
- Persistent benefits and progression
- Headquarters with upgradable facilities
- Long-term goals and achievements

### 1.2 Core Principles

**Freedom of Association**:
- Players can group with anyone, anytime
- No forced grouping or matchmaking
- Organic social connections valued over systems
- Cross-nation play encouraged (when diplomatically possible)

**Meaningful Organization**:
- Fleets provide tangible benefits worth the commitment
- Structure scales with fleet size
- Leadership tools enable coordination
- Investment grows over time

**No Pay-to-Win**:
- All fleet benefits achievable through gameplay
- No premium fleet features
- Cosmetic customization available
- Effort, not money, determines fleet power

---

## 2. Squadrons (Ad-hoc Groups)

### 2.1 Squadron Formation

**Creating a Squadron**:
1. Right-click any player → "Invite to Squadron"
2. Or: Open social menu → "Create Squadron" → Invite players
3. Or: Accept invitation from another player
4. Squadron forms instantly upon first acceptance

**Joining a Squadron**:
- Accept direct invitation
- Request to join (if squadron is set to "open")
- No application process or waiting period

**Squadron Settings** (Set by Leader):
- **Open**: Anyone can join
- **Invite Only**: Requires invitation (default)
- **Private**: Hidden from player lists

### 2.2 Squadron Size

**No Hard Limit**: Squadrons can theoretically contain any number of players.

**Practical Considerations**:
- 2-4 players: Easy coordination, voice chat sufficient
- 5-12 players: Moderate coordination, needs squadron leader
- 13-25 players: Complex coordination, multiple sub-leaders helpful
- 26-50 players: Difficult without formal structure, Fleet recommended
- 50+ players: Extremely difficult without Fleet infrastructure

**Why No Limit?**
- Real naval operations involve many ships
- Players should self-organize based on capability
- Natural friction prevents abuse (hard to coordinate large groups without tools)
- Fleet system provides tools for large-scale organization

### 2.3 Squadron Features

**Shared Information**:
- Squadron members visible on map (distinct icon)
- Shared enemy contacts (radar/visual contacts shared)
- Health bars visible for squadron members
- Voice chat integration (proximity + squadron channel)

**Combat Coordination**:
- Squadron target marking (mark targets for focus fire)
- Formation indicators (optional visual guides)
- Shared mission objectives (if on same mission)
- Friendly fire warnings (visual indicator before shooting ally)

**Resource Sharing** (Optional, Toggleable):
- Ammunition transfer (alongside in calm waters)
- Fuel transfer (alongside in calm waters)
- Repair assistance (bonus to repair when nearby)
- Crew rescue (recover crew from sunk squadron members)

### 2.4 Squadron Leadership

**Squadron Leader**:
- First player to create squadron, or designated
- Can invite/kick members
- Can promote others to Leader (transfer leadership)
- Can set squadron settings (open/invite/private)
- Can disband squadron

**Squadron Officers** (Optional):
- Designated by Leader
- Can invite new members
- Cannot kick members or disband
- Useful for large squadrons

**Leadership Transfer**:
- Leader can promote any member to Leader
- If Leader disconnects for 10+ minutes, auto-transfers to oldest Officer
- If no Officers, transfers to longest-serving member

### 2.5 Cross-Nation Squadrons

**Allowed When**: Nations are at PEACE or NEUTRAL diplomatic state

**Formation**:
- Any player from compatible nation can be invited
- Squadron nation is "Mixed" (no single nation affiliation)
- Individual reputation/rewards go to each player's home nation

**Restrictions**:
- Cannot include nations at WAR with each other
- Cannot include Pirates with any national player
- If diplomatic state changes to WAR during squadron:
  - Warning issued to all members
  - Players from now-hostile nations auto-removed after 5 minutes
  - No combat between removed members during grace period

**Benefits**:
- Access to each nation's port (via squadron member escort)
- Shared intelligence across national boundaries
- Combined strengths of different national ship designs

### 2.6 Squadron Dissolution

**Automatic Dissolution**:
- Last member leaves or logs out
- All members disconnect for 30+ minutes
- Squadron naturally ends when empty

**Manual Dissolution**:
- Leader selects "Disband Squadron"
- All members notified
- Immediate dissolution

**What Doesn't End a Squadron**:
- Completing a mission (squadron persists)
- Returning to port (squadron persists)
- Changing ships (squadron persists)
- Brief disconnections (5-minute grace period)

---

## 3. Fleets (Persistent Guilds)

### 3.1 Fleet Creation

**Requirements to Create**:
- Captain Rank 10 or higher
- 10,000 Credits (creation fee)
- No current Fleet membership
- Unique Fleet name (server-wide)

**Creation Process**:
1. Visit Fleet Registry Office (available at Capital ports)
2. Pay creation fee
3. Choose Fleet name (3-24 characters, no profanity)
4. Design Fleet emblem (from available templates)
5. Set initial Fleet policies
6. Become Founder and Admiral (Fleet leader)

### 3.2 Fleet Identity

**Fleet Name**:
- Unique across server
- Cannot be changed (except by support request)
- Displayed on member nameplates
- Visible in combat

**Fleet Tag** (Abbreviation):
- 2-5 characters
- Displayed in brackets before player name: [TAG] PlayerName
- Unique across server

**Fleet Emblem**:
- Custom design from modular components
- Colors: 2 primary, 1 accent
- Displayed on:
  - Fleet Headquarters
  - Member ship flags (optional)
  - UI elements
  - Promotional materials

**Fleet Motto**:
- Optional tagline (50 characters max)
- Displayed on Fleet info panel

### 3.3 Fleet Membership

**Joining a Fleet**:
- Apply through Fleet Registry
- Direct invitation from Officer+
- Accept invitation in social menu
- Only one Fleet membership at a time

**Membership Limits**:
| Fleet Level | Max Members |
|-------------|-------------|
| Level 1 | 50 |
| Level 2 | 100 |
| Level 3 | 150 |
| Level 4 | 200 |
| Level 5 | 300 |
| Level 6+ | 500 |

**Leaving a Fleet**:
- Voluntary departure at any time
- No penalty for leaving
- Cannot rejoin same Fleet for 7 days (cooldown)
- Personal contributions remain with Fleet

### 3.4 Fleet Ranks

**Default Rank Structure** (Customizable Names):

| Rank | Default Name | Permissions |
|------|--------------|-------------|
| 1 | Admiral | Full control, cannot be removed |
| 2 | Vice Admiral | All permissions except disband |
| 3 | Commodore | Invite, kick juniors, promote/demote juniors, manage HQ |
| 4 | Captain | Invite, kick Ensigns only, access Officer facilities |
| 5 | Commander | Invite, access advanced facilities |
| 6 | Lieutenant | Access standard facilities, participate in Fleet missions |
| 7 | Ensign | Basic access, probationary period |

**Permission Categories**:
- **Administrative**: Invite, Kick, Promote, Demote, Edit Info
- **Financial**: Access Treasury, Spend Fleet Credits, Set Taxes
- **Facility**: Access/Upgrade HQ buildings, Manage resources
- **Operational**: Create Fleet missions, Lead Fleet operations
- **Communication**: Post announcements, Manage chat channels

**Custom Ranks**:
- Admirals can rename ranks
- Can create up to 3 additional custom ranks
- Custom ranks slot between existing ranks
- Each custom rank has configurable permissions

### 3.5 Fleet Treasury

**Fleet Credits**:
- Earned through Fleet activities
- Used for HQ upgrades and Fleet services
- Cannot be converted to personal credits

**Earning Fleet Credits**:
| Activity | Fleet Credits Earned |
|----------|---------------------|
| Member completes mission | 10% of mission reward |
| Member sinks enemy ship | 50 per ship |
| Fleet mission completion | 500-5,000 (varies) |
| Territory control bonus | 100/hour per controlled point |
| Fleet war victory | 10,000 per war won |

**Member Tax** (Optional):
- Fleet can set tax rate (0-20%)
- Tax deducted from mission rewards
- Goes directly to Fleet Treasury
- Members see tax amount before accepting missions

**Treasury Permissions**:
- View balance: All members
- Withdraw: Admiral, Vice Admiral only
- Spend on upgrades: Admiral, Vice Admiral, Commodore

### 3.6 Fleet Headquarters

**HQ Location**:
- Must be placed at a friendly port
- Fleet purchases HQ slot (one-time cost)
- HQ provides facilities and bonuses
- Can be relocated (expensive)

**HQ Facilities**:

#### Dock Complex (Ship Services)
| Level | Bonus | Upgrade Cost |
|-------|-------|--------------|
| 1 | -5% repair costs | 5,000 FC |
| 2 | -10% repair costs | 15,000 FC |
| 3 | -15% repair costs | 40,000 FC |
| 4 | -20% repair costs | 100,000 FC |
| 5 | -25% repair costs | 250,000 FC |

#### Shipyard (Purchasing)
| Level | Bonus | Upgrade Cost |
|-------|-------|--------------|
| 1 | -3% ship purchase cost | 10,000 FC |
| 2 | -6% ship purchase cost | 30,000 FC |
| 3 | -9% ship purchase cost | 80,000 FC |
| 4 | -12% ship purchase cost | 200,000 FC |
| 5 | -15% ship purchase cost | 500,000 FC |

#### Academy (Training)
| Level | Bonus | Upgrade Cost |
|-------|-------|--------------|
| 1 | +5% crew XP | 8,000 FC |
| 2 | +10% crew XP | 25,000 FC |
| 3 | +15% crew XP | 60,000 FC |
| 4 | +20% crew XP | 150,000 FC |
| 5 | +25% crew XP | 400,000 FC |

#### Intelligence Office (Information)
| Level | Bonus | Upgrade Cost |
|-------|-------|--------------|
| 1 | Extended radar range +5% | 12,000 FC |
| 2 | Extended radar range +10% | 35,000 FC |
| 3 | Extended radar range +10%, enemy Fleet ships marked | 90,000 FC |
| 4 | Extended radar range +15%, enemy Fleet ships marked | 220,000 FC |
| 5 | Extended radar range +15%, enemy Fleet ships + cargo visible | 550,000 FC |

#### Armory (Combat)
| Level | Bonus | Upgrade Cost |
|-------|-------|--------------|
| 1 | -5% ammunition cost | 10,000 FC |
| 2 | -10% ammunition cost | 30,000 FC |
| 3 | -10% ammo cost, +5% ammo capacity | 75,000 FC |
| 4 | -15% ammo cost, +5% ammo capacity | 180,000 FC |
| 5 | -15% ammo cost, +10% ammo capacity | 450,000 FC |

#### War Room (Coordination)
| Level | Bonus | Upgrade Cost |
|-------|-------|--------------|
| 1 | Fleet mission board unlocked | 15,000 FC |
| 2 | +10% Fleet mission rewards | 45,000 FC |
| 3 | +15% Fleet mission rewards, strategic map | 110,000 FC |
| 4 | +20% Fleet mission rewards, strategic map, NPC support | 280,000 FC |
| 5 | +25% Fleet mission rewards, all coordination tools | 700,000 FC |

### 3.7 Fleet Levels

Fleet Level increases based on total activity:

| Fleet Level | XP Required | Unlocks |
|-------------|-------------|---------|
| 1 | 0 | Basic HQ, 50 members |
| 2 | 10,000 | 100 members, Level 2 facilities |
| 3 | 35,000 | 150 members, Level 3 facilities, Fleet wars |
| 4 | 80,000 | 200 members, Level 4 facilities, Alliance formation |
| 5 | 150,000 | 300 members, Level 5 facilities |
| 6 | 250,000 | 500 members, all features |
| 7 | 400,000 | Prestige rewards, unique cosmetics |
| 8 | 600,000 | Legendary status, historical recognition |
| 9 | 900,000 | Elite rewards |
| 10 | 1,500,000 | Maximum prestige, unique title "Grand Fleet" |

**Earning Fleet XP**:
- Member activity (missions, combat, trade)
- Fleet mission completion
- Territory control
- Fleet war victories
- Achievement unlocks

---

## 4. Fleet Operations

### 4.1 Fleet Missions

**Exclusive to Fleets**: These missions require Fleet membership to access.

#### Fleet Patrol Operations
- **Size**: 4-20 Fleet members
- **Objective**: Patrol designated zone with Fleet ships
- **Duration**: 1-4 hours
- **Rewards**: Fleet Credits, individual rewards, Fleet XP

#### Fleet Strike Operations
- **Size**: 8-30 Fleet members
- **Objective**: Coordinate attack on high-value target
- **Duration**: 2-6 hours
- **Rewards**: High Fleet Credits, rare equipment, Fleet XP

#### Fleet Defense Operations
- **Size**: 10-50 Fleet members
- **Objective**: Defend Fleet HQ or controlled territory
- **Duration**: Varies (defensive response)
- **Rewards**: Territory retention, Fleet Credits

#### Fleet Convoy Operations
- **Size**: 6-24 Fleet members
- **Objective**: Organize and protect large cargo convoy
- **Duration**: 2-4 hours
- **Rewards**: Trade profits, Fleet Credits, merchant reputation

### 4.2 Fleet Wars

**Declaration**:
- Requires Fleet Level 3+
- Costs 5,000 Fleet Credits to declare
- 24-hour warning period before war begins
- Both Fleets notified

**War Mechanics**:
- All members of warring Fleets can attack each other freely
- No reputation loss for killing war enemy
- War score tracks kills, captures, territory
- War lasts until:
  - One Fleet surrenders
  - Time limit (7 days default)
  - Score threshold reached

**War Score**:
| Action | Points |
|--------|--------|
| Sink enemy Fleet member | +10 |
| Sink enemy T6+ ship | +20 |
| Capture enemy cargo | +5 per 100t |
| Control contested point | +50/hour |
| Destroy enemy HQ facility | +100 |

**War Victory Rewards**:
- 10,000 Fleet Credits
- War trophy (cosmetic display)
- Fleet XP bonus
- Bragging rights and historical record

**War Defeat Consequences**:
- No permanent losses
- 7-day cooldown before new war
- Morale debuff (minor) for 3 days

### 4.3 Alliances

**Formation** (Requires Fleet Level 4+):
- Admiral initiates alliance invitation
- Target Fleet Admiral must accept
- Alliance forms with both Fleets as members
- Up to 5 Fleets per Alliance

**Alliance Benefits**:
- Allied Fleet members appear as friendly (green on map)
- Shared enemy intelligence
- Cannot declare war on allied Fleets
- Joint operations for massive events
- Alliance chat channel

**Alliance Governance**:
- Each Fleet retains independence
- Executive Fleet (rotating or voted) coordinates Alliance
- Alliance decisions require majority Fleet Admiral approval
- Alliances can declare war on other Alliances

---

## 5. Social Features

### 5.1 Communication

**Squadron Chat**:
- Temporary channel for squadron duration
- Voice chat integration (optional)
- Tactical callouts support

**Fleet Chat Channels**:
- General (all members)
- Officer (rank-restricted)
- Operations (mission coordination)
- Custom channels (up to 5)

**Alliance Chat**:
- Cross-Fleet communication
- Alliance announcements
- Joint operation coordination

### 5.2 Roster Management

**Member List**:
- Online/offline status
- Current location (zone)
- Current ship/activity
- Rank and join date
- Contribution statistics

**Activity Tracking**:
- Last online date
- Missions completed (weekly/monthly/total)
- Ships sunk
- Credits earned
- Territory captured

**Inactive Member Handling**:
- After 30 days inactive: Warning flag
- After 60 days inactive: Auto-demoted to Ensign
- After 90 days inactive: Can be auto-removed (if enabled)

### 5.3 Recruitment

**Fleet Recruitment Board**:
- Public listing (optional)
- Description and requirements
- Application process

**Recruitment Posting**:
```
Fleet Name: [Name]
Tag: [TAG]
Level: [1-10]
Members: [X/Max]
Focus: [PvP/PvE/Trade/Social]
Requirements: [Text]
Description: [Text]
```

**Application Review**:
- Players apply through Fleet Registry
- Officers+ can view applications
- Accept/Reject with optional message
- Application history tracked

### 5.4 Events & Scheduling

**Fleet Calendar**:
- Schedule operations in advance
- Set reminders for members
- Track participation
- Recurring events support

**Event Types**:
- Fleet Operations (missions)
- Training Sessions
- Social Events
- War Preparations
- Territory Control

**RSVP System**:
- Members indicate availability
- Minimum attendance requirements
- Waitlist for popular events

---

## 6. Fleet Competition

### 6.1 Fleet Leaderboards

**Categories**:
- Total Fleet XP
- Weekly Activity
- Ships Sunk (PvP)
- Territory Controlled
- Trade Volume
- War Record

**Rankings**:
- Server-wide rankings
- Regional rankings (by theater)
- Seasonal rankings (resets monthly)

### 6.2 Fleet Achievements

**Achievement Categories**:

**Growth Achievements**:
- First 10 Members
- First 50 Members
- First 100 Members
- Max Membership

**Combat Achievements**:
- First Fleet Kill
- 100 Enemy Ships Sunk
- 1,000 Enemy Ships Sunk
- Fleet War Victory
- Alliance War Victory

**Economic Achievements**:
- First HQ Facility
- All Facilities Level 3
- All Facilities Level 5
- 1,000,000 Fleet Credits Earned

**Territory Achievements**:
- First Territory Controlled
- Control 5 Points Simultaneously
- Hold Territory for 30 Days
- Capture Enemy HQ Region

### 6.3 Seasonal Competition

**Fleet Seasons** (3 months each):
- Spring Campaign (March-May)
- Summer Offensive (June-August)
- Autumn Maneuvers (September-November)
- Winter War (December-February)

**Seasonal Rewards**:
- Top 10 Fleets: Unique cosmetics, titles
- Top 50 Fleets: Seasonal cosmetics
- All participating Fleets: Participation rewards

---

## 7. Cross-System Integration

### 7.1 Mission System Integration

**Cross-Reference**: [[Mission-System]]

- Fleet missions available at War Room
- Squadron members share mission progress
- Fleet completion bonuses for group missions
- Fleet reputation tracked separately

### 7.2 Territory System Integration

**Cross-Reference**: [[Mission-System#Territory-War-Missions]]

- Fleet can claim territory control
- HQ location provides territorial bonus
- Fleet wars affect territory control
- Alliance territory shared

### 7.3 Reputation System Integration

**Cross-Reference**: [[Reputation-System]]

- Fleet actions don't affect personal reputation
- Fleet has separate reputation with nations
- High Fleet reputation unlocks exclusive missions
- Low Fleet reputation restricts port access for Fleet operations

### 7.4 Economy Integration

**Cross-Reference**: [[Economy-Overview]]

- Fleet Treasury separate from personal funds
- Fleet trade convoys (bulk operations)
- Fleet contracts with NPCs
- Economic warfare through trade manipulation

---

## 8. Technical Considerations

### 8.1 Data Storage

**Squadron Data** (Persistent while active):
- Stored in server memory while squadron exists
- Persists across missions and port visits
- Lightweight structure, dissolves when all members leave/logout

**Fleet Data** (Persistent):
- Database storage required
- Member roster
- Treasury balance
- Facility levels
- Activity logs
- Achievement progress

### 8.2 Scalability

**Squadron Scalability**:
- Unlimited squadrons per server
- No cross-server squadrons
- Minimal server load

**Fleet Scalability**:
- 500 members max per Fleet
- 5 Fleets per Alliance
- Cross-server Fleets possible (future)

### 8.3 Anti-Abuse Measures

**Squadron Abuse Prevention**:
- Cannot squadron with players you've recently attacked
- Friendly fire still possible (discourages trolling)
- Report system for squadron griefing

**Fleet Abuse Prevention**:
- 7-day rejoin cooldown
- Fleet creation cost prevents spam
- Activity requirements for leadership
- Vote system for Admiral removal (future)

---

## 9. UI/UX Design

### 9.1 Squadron UI

**Squadron Panel** (In-Game):
```
+----------------------------------+
| SQUADRON (5 Members)             |
+----------------------------------+
| [Leader] PlayerOne      [DD T5]  |
|          Health: ████████░░ 80%  |
| [Member] PlayerTwo      [CA T4]  |
|          Health: ██████████ 100% |
| [Member] PlayerThree    [BB T6]  |
|          Health: ████░░░░░░ 40%  |
| [Member] PlayerFour     [CV T5]  |
|          Health: ██████████ 100% |
| [Member] PlayerFive     [SS T4]  |
|          Health: ███████░░░ 70%  |
+----------------------------------+
| [Invite] [Settings] [Leave]      |
+----------------------------------+
```

### 9.2 Fleet UI

**Fleet Overview Panel**:
```
+------------------------------------------------+
| [TAG] FLEET NAME                    Level 5    |
| "Fleet Motto Here"                             |
+------------------------------------------------+
| Members: 156/300     Online: 23                |
| Fleet Credits: 125,450                         |
| Territory: 3 points controlled                 |
+------------------------------------------------+
| [Roster] [HQ] [Missions] [Wars] [Settings]     |
+------------------------------------------------+
```

**Fleet HQ Panel**:
```
+------------------------------------------------+
| FLEET HEADQUARTERS - Port of [Location]        |
+------------------------------------------------+
| FACILITIES                                      |
| +------------------------------------------+   |
| | Dock Complex     [████░] Level 4         |   |
| | -20% repair costs                        |   |
| | Upgrade: 250,000 FC                      |   |
| +------------------------------------------+   |
| | Shipyard         [███░░] Level 3         |   |
| | -9% ship purchase cost                   |   |
| | Upgrade: 200,000 FC                      |   |
| +------------------------------------------+   |
| | Academy          [████░] Level 4         |   |
| | +20% crew XP                             |   |
| | Upgrade: 400,000 FC                      |   |
| +------------------------------------------+   |
| | ...                                      |   |
+------------------------------------------------+
```

---

## 10. Future Enhancements

### 10.1 Cross-Server Fleets (Post-Launch)

- Fleets span multiple server instances
- Unified roster and treasury
- Coordinated operations across servers

### 10.2 Fleet Capitals (Post-Launch)

- Massive fleet-owned ships
- Require coordinated crew
- Serve as mobile HQ
- Unique gameplay experience

### 10.3 Political System (Post-Launch)

- Fleet influence on server politics
- Voting on server-wide decisions
- Economic control through fleet coordination
- Player-driven governance

---

## 11. Cross-References

- [[Mission-System]] - Fleet and Squadron mission integration
- [[Reputation-System]] - Fleet reputation tracking
- [[Economy-Overview]] - Fleet Treasury and economics
- [[Diplomacy-States]] - Cross-nation grouping rules
- [[Chat-System]] - Communication integration
- [[Network-Architecture]] - Technical implementation

---

## 12. Research Sources

This system design draws from analysis of:
- [EVE Online Corporations](https://wiki.eveuniversity.org/Corporations) - Corporation structure, alliances, sovereignty
- [World of Warships Clans](https://worldofwarships.com/) - Naval Base system, clan benefits
- [Sea of Thieves Alliances](https://seaofthieves.fandom.com/wiki/Player_Alliances) - Ad-hoc alliance formation
- [Guild Wars 2 Guilds](https://wiki.guildwars2.com/wiki/Guild) - Multi-guild membership, guild halls
- [FFXIV Free Companies](https://na.finalfantasyxiv.com/) - Company progression, housing
- [MMO Guild Design Theory](https://www.gamedeveloper.com/) - Rank systems, permissions, social structures

---

## Changelog
- **2025-12-03**: Initial document creation - comprehensive squadron and guild system design
