---
tags: [planned, phase5, multiplayer, moderation, anti-cheat]
status: 📋 PLANNED
phase: Phase 5 - MMO Scale
priority: CRITICAL
last-updated: 2025-12-22
---

# Moderation & Anti-Cheat System

## Overview

The Moderation & Anti-Cheat System protects the game's integrity, ensures fair play, and maintains a healthy community environment. This system combines automated detection, player reporting, and human moderation to prevent cheating, exploits, harassment, and toxic behavior.

**Core Philosophy**: Fair play is non-negotiable. A single cheater can destroy hundreds of hours of legitimate player investment. Prevention is better than detection, but detection must be swift and punishment certain.

## Implementation Status

**Status**: 📋 PLANNED
**Phase**: Phase 5 - MMO Scale
**Dependencies**: [[Network-Architecture]], [[Authentication]], [[Chat-System]], [[Economy-System]]
**Priority**: CRITICAL - Essential for MMO integrity

---

## Design Specification

### Anti-Cheat Systems

#### Server-Authoritative Validation

**Core Principle**: Client is NEVER trusted. All game-critical calculations happen server-side.

**Validated Server-Side**:
- Ship position and movement
- Damage calculations
- Resource acquisition
- Inventory transactions
- Combat results
- Experience gains
- Currency changes

**Client Responsibilities** (can be validated):
- Input commands
- Camera position
- UI state
- Visual effects

**Validation Checks**:
- **Movement Validation**: Speed limits, turning rates, collision
- **Damage Validation**: Range, line-of-sight, ammunition count
- **Resource Validation**: Acquisition rate limits, source verification
- **Transaction Validation**: Balance checks, ownership verification

---

#### Cheat Detection Systems

**Speed Hacks**:
- Server tracks ship position deltas
- Flag accounts moving faster than theoretical maximum
- Automatic kick + investigation on repeated violations

**Teleportation Detection**:
- Position history tracking (server-side)
- Large position jumps flagged
- Rubber-banding for minor desync, ban for impossible jumps

**Damage Manipulation**:
- All damage calculated server-side
- Client damage reports compared to server calculations
- Discrepancies trigger investigation

**Economy Exploits**:
- Transaction rate limiting
- Unusual wealth accumulation flagged
- Item duplication detection (unique IDs)
- Market manipulation detection (price patterns)

**Aim Assistance**:
- Hit rate statistical analysis
- Impossible accuracy patterns detected
- Time-to-target analysis

---

#### Automated Detection

**Behavioral Analysis**:
- Machine learning model trained on legitimate play patterns
- Flags statistical outliers for human review
- Adapts to new cheat methods over time

**Heuristic Rules**:
- Hard-coded limits that cannot be exceeded
- Immediate action on clear violations
- Threshold alerts for suspicious patterns

**Detection Tiers**:
| Tier | Confidence | Action |
|------|------------|--------|
| 1 - Suspicious | Low | Silent logging, manual review queue |
| 2 - Probable | Medium | Temporary restriction, priority review |
| 3 - Certain | High | Automatic temporary ban, fast-track review |
| 4 - Definitive | 100% | Permanent ban, no appeal |

---

### Moderation Systems

#### Player Reporting

**Report Categories**:
- **Cheating**: Speed hacks, damage hacks, exploits
- **Harassment**: Targeted abuse, stalking, griefing
- **Inappropriate Content**: Offensive names, chat violations
- **Bug Abuse**: Exploiting known bugs for advantage
- **Real Money Trading**: Selling in-game items/currency

**Report Interface**:
- Right-click player → Report
- Category selection (required)
- Description field (optional, 500 char max)
- Evidence attachment (screenshots, last 5 minutes of chat)

**Report Handling**:
- Automated prioritization based on report volume and severity
- Reports against same player aggregated
- False report detection (report spammers flagged)

---

#### Chat Moderation

**Automated Filters**:
- **Profanity Filter**: Configurable by player (on by default)
- **Slur Detection**: Zero tolerance, automatic mute + report
- **Spam Detection**: Repeated messages, character spam
- **Advertising Detection**: External links, RMT sites
- **Language Detection**: Route to appropriate moderator

**Moderation Actions**:
| Violation | First Offense | Second | Third |
|-----------|---------------|--------|-------|
| Mild profanity | Warning | 1-hour mute | 24-hour mute |
| Slurs/hate speech | 24-hour mute | 7-day mute | Permanent mute |
| Spam | 10-min mute | 1-hour mute | 24-hour mute |
| Advertising | 24-hour mute | 7-day ban | Permanent ban |
| Threats | Immediate review | 7-day ban | Permanent ban |

---

#### Grief Prevention

**Griefing Definitions**:
- **Spawn Camping**: Repeatedly killing players at spawn/port exits
- **Seal Clubbing**: High-tier players hunting low-tier exclusively
- **Blocking**: Intentionally blocking port entrances/exits
- **Kill Stealing**: Repeatedly taking others' kills (PvE)
- **Stream Sniping**: Targeting streamers using external info

**Anti-Grief Measures**:
- **Spawn Protection**: 60-second immunity when leaving port
- **Reputation Penalties**: Heavy rep loss for attacking much lower tiers
- **Blocking Prevention**: Ships phase through stationary obstacles at ports
- **Kill Credit**: Damage-based credit (not last-hit)

**Repeated Griefing**:
- First offense: Warning
- Second offense: 24-hour combat restriction
- Third offense: 7-day ban
- Pattern behavior: Permanent ban

---

### Punishment System

#### Penalty Tiers

**Tier 1 - Warning**:
- In-game notification
- Logged to account history
- No gameplay impact
- Educational about rules

**Tier 2 - Restriction**:
- Chat mute (1 hour to permanent)
- Trade restriction (1-7 days)
- Combat restriction (1-24 hours)
- Leaderboard removal

**Tier 3 - Temporary Ban**:
- 24 hours to 30 days
- Full account access denied
- Progress frozen (no decay)
- Appeal available

**Tier 4 - Permanent Ban**:
- Account terminated
- Associated accounts investigated
- Hardware/IP flagged
- No appeal for cheat bans

---

#### Appeal System

**Eligible Appeals**:
- Tier 2-3 punishments
- NOT eligible: Tier 4 cheat bans, confirmed RMT

**Appeal Process**:
1. Submit appeal via website (not in-game)
2. Provide account details and explanation
3. Review by different moderator than original
4. Response within 72 hours
5. Final decision communicated via email

**Appeal Outcomes**:
- **Upheld**: Punishment stands
- **Reduced**: Severity lowered
- **Overturned**: Punishment removed, account restored
- **Escalated**: Further review by senior staff

---

### Moderation Tools

#### Admin Panel Features

**Player Lookup**:
- Account history (all characters)
- Punishment history
- Report history (filed and received)
- Login/IP history
- Economic transaction log
- Chat log search

**Real-Time Tools**:
- Server-wide announcements
- Individual player messaging
- Invisible observation mode
- Teleport to player location
- Force disconnect

**Punishment Application**:
- Quick-action buttons for common violations
- Custom duration and notes
- Evidence attachment
- Audit trail for all actions

---

#### Moderator Hierarchy

**Community Moderators** (Volunteers):
- Chat moderation only
- Mute capability (max 24 hours)
- Report escalation
- No account access

**Junior Game Masters**:
- Full chat moderation
- Tier 1-2 punishments
- Player investigation (read-only)
- Escalation to seniors

**Senior Game Masters**:
- Tier 1-3 punishments
- Full investigation tools
- Appeal review
- Policy interpretation

**Lead Moderators** (Staff):
- Tier 1-4 punishments
- Policy creation
- Moderator oversight
- Appeal final decisions

---

## Technical Requirements

### Server Infrastructure
- Central moderation database (cross-server)
- Real-time alert system for high-severity issues
- Log storage (90-day retention minimum)
- Evidence archival system

### Integration Points
- Authentication service (ban enforcement)
- Chat service (filter integration)
- Game servers (validation hooks)
- Website (appeal portal)

### Performance Considerations
- Validation must not add latency
- Detection runs asynchronously
- Log writes are buffered
- Alert system is priority queued

---

## Success Metrics

### Anti-Cheat Effectiveness
- **Detection Rate**: 95%+ of cheats detected within 24 hours
- **False Positive Rate**: <0.1% of legitimate players flagged
- **Time to Ban**: <4 hours from detection to action (automated)
- **Cheat Prevalence**: <0.5% of active players cheating

### Community Health
- **Report Response Time**: <24 hours for Tier 3+ violations
- **Toxic Incident Rate**: <5% of sessions include reported behavior
- **Appeal Overturn Rate**: <10% (indicates accurate initial judgment)
- **Player Satisfaction**: 80%+ feel game is fair

---

## Cross-References
- [[Network-Architecture]] - Server authority model
- [[Authentication]] - Account security
- [[Chat-System]] - Chat moderation integration
- [[Economy-System]] - Economic exploit prevention
- [[Reputation-System]] - Griefing penalties

---

## Changelog
- **2025-12-22**: Initial document creation from GitHub issue alignment
