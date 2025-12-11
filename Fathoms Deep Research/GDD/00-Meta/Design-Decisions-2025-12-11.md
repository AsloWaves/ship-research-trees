---
title: Design Decisions Log - December 11, 2025
category: meta
description: Record of design questions resolved through Q&A session
version: 1.0
date: 2025-12-11
tags: [decisions, Q&A, design, confirmed]
---

# Design Decisions Log - December 11, 2025

This document records all design decisions made during the Q&A session on December 11, 2025. These decisions are now authoritative for the GDD.

---

## Summary

**Total Questions Resolved**: 40+
**Categories Covered**: 7
**Phase 2 Blockers Resolved**: 4/4 (all critical blockers cleared)

---

## Combat Fundamentals

### Fire Control Failure (Q3)
**Question**: When a ship's Fire Control module is destroyed mid-combat, what happens to the current firing solution?
**Decision**: **Gradual decay (accelerated)**
- Solution degrades at 2-3× normal rate until FC restored
- Not instant collapse, not frozen
- Creates urgency to repair without instant punishment

### Ammunition System (Q10)
**Question**: How does ammunition work during extended combat?
**Decision**: **Cargo-only system**
- All ammo stored in cargo grid
- Turrets draw directly from cargo with reload delay
- No separate magazine system
- See [[Ammunition-System]] for full details

### Ammunition Stacking
**Question**: How are ammunition items structured in cargo?
**Decision**: **Stacking by caliber**
- All shells of same caliber stack (e.g., 50 shells per 1×1 slot)
- Stack size varies by shell size (bigger = fewer per stack)

### Ammo Empty Behavior
**Question**: What happens when turret has no matching ammo?
**Decision**: **Manual switch required**
- Player must manually switch to different ammo type
- Turret disabled (red indicator) until switched or resupplied
- No auto-switch to prevent automation cheese

### Accuracy Cap (Q9)
**Question**: Can gun accuracy exceed 100%?
**Decision**: **Soft cap with logarithmic diminishing returns**
- Bonuses above 100% provide reduced benefit
- Example: 110% → 102% effective, 120% → 103.5%, 130% → 104.5%
- Prevents "god builds" while rewarding investment

### Magazine Detonation (Q4)
**Question**: When does magazine detonation roll occur?
**Decision**: **Per penetrating hit to magazine/cargo**
- Each shell that penetrates armor and reaches cargo triggers roll
- Base chance very low (0.01 or ~1%)
- Chance increases slightly with more ammo in cargo
- Creates risk/reward for ammo loadout

---

## Crew System

### Crew Classifications (Q11)
**Question**: What classifications exist beyond basic types?
**Decision**: **8+ classes with sub-specializations**
- **Gunnery Branch**: Main Battery → Secondary → Fire Control → Torpedo
- **Engineering Branch**: Propulsion → Damage Control → Repair
- **Operations Branch**: Radar → Sonar → Comms → Navigation
- **Aviation Branch**: Pilot → Deck Crew → Air Control
- Total: 18 classifications (confirmed in [[Crew-Skills]])

### Morale System (Q13)
**Question**: Does morale system exist?
**Decision**: **No morale - zero-morale design confirmed**
- Crew performance is entirely stat-based
- No morale penalties from casualties
- Simpler balance, predictable performance

### Casualty Timing (Q13/C1)
**Question**: Are casualties applied real-time or post-battle?
**Decision**: **Real-time (immediate effect)**
- Sailor count drops instantly when damage occurs
- Efficiency degrades during battle
- Creates pressure to protect crew stations

### Cross-Training (Q16)
**Question**: Can Gunner retrain as Engineer?
**Decision**: **Full respec (costly)**
- Can reset classification for significant credit cost
- Stats preserved, classification changes
- Not free - discourages constant switching

### Cross-Ship Efficiency (Q12)
**Question**: Does destroyer crew operate battleship turret with penalty?
**Decision**: **No penalty**
- Crew can operate any module they have classification for
- Ship class is irrelevant to crew assignment
- Makes elite crew truly valuable

### Crew Stat Generation (Q14)
**Decision**: **Confirmed from [[Crew-Skills]]**
- 7-15 starting range per attribute
- Navy Field-style randomization
- 50 cap at max level
- No nationality effect on stats

### Casualty Visual Feedback
**Question**: What happens when crew killed during combat?
**Decision**: **Station goes red/disabled**
- When crew drops below threshold, station shows critical state
- Disabled stations cannot operate
- Clear visual feedback of combat damage

---

## Permadeath System

### Crew Recovery (Q49)
**Question**: Is there any recovery window for permadead crew?
**Decision**: **Insurance-based recovery only**
- No timed retrieval window
- Only recoverable if crew was insured
- Uninsured crews are gone forever
- See [[Insurance-System]]

### Wreck Persistence
**Question**: How long do wrecks remain for salvage?
**Decision**: **1-4 hours**
- Short window for immediate salvage
- Creates urgency and PvP hotspots
- Varies by ship size and conditions

### Death Announcements (Q51)
**Question**: Are permadeath events announced publicly?
**Decision**: **Private (no broadcast)**
- Only involved parties know
- No server-wide announcement
- No kill feed notification
- Creates uncertainty and prevents targeted hunting

### Permadeath Roll Type (Q2/C2)
**Question**: Is the roll per-crew-card or ship-wide?
**Decision**: **Per-card roll**
- Each crew card rolls independently
- T6=10%, T7=25%, T8=50%, T9=75%, T10=100%
- Some cards may survive while others die

### Survivor State (Q53)
**Question**: What condition are surviving crews in?
**Decision**: **50% sailor casualties**
- Cards that pass permadeath roll still lose half their sailors
- Must replenish sailors at port
- Significant but not permanent loss

---

## Insurance System

### Insurance Providers
**Question**: Who provides insurance?
**Decision**: **NPC + Player-run dual system**
- NPC companies provide baseline coverage
- Player guilds can offer competitive rates
- Creates economic gameplay

### Premium Cost
**Question**: What determines insurance cost?
**Decision**: **Crew level-based scaling**
- Higher level crews cost more to insure
- Level 100 crew = ~10× Level 10 cost
- Creates meaningful economic decision

### Claim Result
**Question**: What happens when you claim insurance?
**Decision**: **Same stats/level, different identity**
- Get new crew card with same stats and level
- New random name and portrait
- Service history reset
- Preserves investment, loses "character"

### Claim Processing
**Question**: Is there a waiting period?
**Decision**: **Days (real-time)**
- Claims take real-world days to process
- Creates meaningful downtime after major losses
- Unlimited coverage (no claim limits)

### Cargo Insurance (Q58)
**Question**: Can cargo be insured?
**Decision**: **No cargo insurance**
- Cargo is never insurable
- Losing cargo is always permanent
- Maintains extraction tension

---

## Module System

### Quality-to-Efficiency (Q35)
**Question**: How does 70-130% quality affect efficiency?
**Decision**: **Direct multiplier**
- 70% quality = 70% of base stats
- 130% quality = 130% of base stats
- Simple and clear value hierarchy

### Module Redundancy (Q30)
**Question**: Do multiple identical modules provide redundancy?
**Decision**: **No redundancy**
- Each module operates independently
- Losing one doesn't affect others
- No backup activation

### Cascade Damage (Q31)
**Question**: Does damage cascade to adjacent modules?
**Decision**: **No cascade (isolated damage)**
- Each module takes damage independently
- No chain reactions
- Predictable damage patterns

### Module Warm-Up (Q33)
**Question**: Is there warm-up time for new installations?
**Decision**: **No warm-up**
- All modules installed in port
- Combat-ready immediately after installation
- No fire delay for fresh installations

### Cross-Nation Equipment (Q34)
**Question**: Can different nation modules be installed?
**Decision**: **Freely interchangeable**
- Any module fits any compatible mount
- Nation is cosmetic only
- No cross-nation penalty

### Armor System (Q36)
**Question**: Can armor sections be stacked?
**Decision**: **Navy Field style allocation**
- Select zone (Belt/Side/Turrets)
- Define armor type and thickness
- Apply allocation - not module stacking
- Thickness determines protection

### Emergency Repair
**Question**: How does emergency repair work on destroyed modules?
**Decision**: **Restores % functionality**
- Percentage restored depends on consumable tier
- Not full restoration
- Temporary combat fix

### Salvage Quality
**Question**: How do functionality and quality interact for salvage?
**Decision**: **Functionality is temporary quality loss**
- Low functionality = low effective quality until repaired
- Repair restores to original quality
- Quality is inherent, functionality is condition

---

## Detection System

### Shadow Misidentification (Q19)
**Question**: Can misidentification be corrected in real-time?
**Decision**: **Initial ID is locked**
- First detection sets the shadow
- Does NOT auto-correct with better equipment
- Only visual confirmation (Phase 3+) reveals truth

### Phase vs Solution (Q20)
**Question**: What happens to solution when target changes phase?
**Decision**: **Solution independent of phase**
- Detection phase and firing solution are separate systems
- Phase affects acquisition, not solution maintenance
- Once you have solution, phase changes don't break it

### Contact Memory
**Question**: How long does contact persist after losing target?
**Decision**: **Instant fade (no memory)**
- Contact marker disappears immediately
- No "last known position" marker
- No stale indicator
- Makes escape meaningful

### Bearing Distribution (Q21)
**Question**: What distribution for bearing randomization?
**Decision**: **Uniform distribution**
- Equal chance anywhere within bearing arc
- Cannot assume center is more accurate
- Creates genuine uncertainty

### Radar vs Submarines (I9)
**Question**: Can radar detect submerged submarines?
**Decision**: **No**
- Radar cannot detect submerged subs
- Must use sonar/hydrophone
- Creates asymmetric detection advantage

### Shared Intel (Q28)
**Question**: When allies share contacts, whose data shows?
**Decision**: **Best data wins**
- System compares all observers
- Most accurate identification shown to all
- Encourages fleet coordination

### Sensor Toggle (Q25)
**Question**: Is there cooldown on radar/sonar on/off?
**Decision**: **5-10 second cooldown**
- Prevents "ping spam" tactics
- Creates commitment to sensor activation
- Radar: 5 sec both ways
- Active Sonar: 5 sec off, 10 sec on (warm-up)

### Visual Through Smoke (Q24)
**Question**: Can visual detection occur through smoke?
**Decision**: **No visual through smoke/weather**
- Smoke screens completely block visual
- Heavy weather has similar effect
- Radar remains effective through smoke

---

## Economy System

### RP/Credits Conversion (Q38)
**Question**: Can RP and Credits be exchanged?
**Decision**: **No conversion (separate economies)**
- RP for research/unlocks only
- Credits for purchases/services
- Cannot exchange between them

### NPC Market Prices (Q40)
**Question**: How are NPC prices determined?
**Decision**: **Supply/demand simulation**
- Prices fluctuate based on regional supply
- Player purchases affect prices
- Dynamic economy, trade arbitrage possible

### Transaction Taxes (Q44)
**Question**: Where do market taxes go?
**Decision**: **Split (port owner + nation)**
- Partial to port owner (guild)
- Partial to nation treasury
- Incentivizes both port control and faction loyalty

### Resource Decay
**Question**: Do stored items decay over time?
**Decision**: **No decay (permanent storage)**
- Items stored indefinitely
- No degradation over time
- Hoarding allowed

### Black Market (Q41)
**Question**: Where are black markets?
**Decision**: **Hidden locations (must discover)**
- Secret coordinates
- Word of mouth or exploration to find
- Not available at every port

### Trade Automation (Q48)
**Question**: Can trade routes be automated?
**Decision**: **Guild convoy system only**
- Guilds can establish automated trade between owned ports
- Individual players must manually trade
- Creates guild economic advantage

### Intel Valuation (Q42)
**Question**: How is intelligence value determined?
**Decision**: **Relevance-based pricing**
- Value based on freshness and strategic importance
- Dynamic pricing, not fixed values
- Recent intel worth more

### Production Ownership (Q47)
**Question**: Can players own production facilities?
**Decision**: **Guild-owned facilities**
- Guilds can own/operate production
- Manufacture for members or sell
- Individual ownership not mentioned

---

## Multiplayer System

### Fleet Radar Sharing (Q65)
**Question**: Is radar data auto-shared with allies?
**Decision**: **Range-limited sharing**
- Auto-share within radio range (~20km)
- Beyond that, manual transmission needed
- Creates tactical depth for fleet cohesion

### War Grouping (Q69)
**Question**: Can players from warring nations group?
**Decision**: **No grouping during war**
- Cannot party with enemy nation during active war
- Enforces faction loyalty
- War is meaningful

### PvP Flagging (Q70)
**Question**: Can players indicate peaceful intent?
**Decision**: **Always PvP enabled**
- Open world is always PvP
- No safe flag system
- Trust no one

### Guild Size (Q67)
**Question**: What's maximum guild size?
**Decision**: **Large (500+ members)**
- Mega-guilds possible
- Enables EVE-style organizations
- Can dominate regions

### Diplomacy Control (Q68)
**Question**: How do diplomatic states change?
**Decision**: **Dev-controlled + auto-escalation**
- Developers set state through events/story
- Too much PvP between nations auto-escalates
- Combined approach

### Guild Sharing
**Question**: What can guilds share among members?
**Decision**: **Full sharing including ships**
- Shared guild bank
- Guild warehouse for equipment
- Guild-owned ships members can use
- Community assets

### Voice Range (Q66)
**Question**: Does voice bypass the 2km text limit?
**Decision**: **Equipment-dependent**
- Voice range depends on radio module quality
- Better equipment = longer range
- Upgradeable communication

### Guild Alliances
**Question**: Can guilds form formal alliances?
**Decision**: **Yes, full alliance system**
- Formal alliances with shared intel
- Non-aggression pacts
- Joint operations support

---

## Combat Miscellaneous

### Submarine Depths (Q7)
**Question**: Are depths specific values or categories?
**Decision**: **Category-based with limitations**
- Categories: Surface, Periscope, Shallow, Deep, Crush
- Limited by ocean depth (can't go deeper than seafloor)
- Limited by hull type (max safe depth varies)

### Ramming Damage (Q8)
**Question**: Is ramming damage symmetric?
**Decision**: **Asymmetric by class/size**
- Larger ship takes less damage
- Destroyer ramming BB = DD destroyed, BB scratched
- Size matters

### Friendly Fire
**Question**: How is friendly fire handled?
**Decision**: **Full friendly fire (always on)**
- Your shells damage allies
- Fire discipline matters
- Realistic and punishing

### Aircraft Fuel Empty
**Question**: What happens when aircraft runs out of fuel?
**Decision**: **Plane lost, pilot crew loses sailors**
- Aircraft is destroyed (ditched at sea)
- Pilot crew card survives
- Pilot card loses sailors (not the card itself)
- Punishes poor fuel management without permadeating pilot

---

## Documents Updated

The following GDD documents were updated with confirmed decisions:

1. **TODO.md** - Marked 40+ items as resolved
2. **Ammunition-System.md** - NEW document created
3. **Insurance-System.md** - NEW document created
4. **Detection-System.md** - Added 8 confirmation blocks
5. **Permadeath-System.md** - Updated percentages, added recovery/wreck sections

---

## Cross-References

- [[TODO]] - Master task list
- [[Ammunition-System]] - Full ammo mechanics
- [[Insurance-System]] - Full insurance mechanics
- [[Detection-System]] - Detection mechanics
- [[Permadeath-System]] - Permadeath mechanics
- [[Crew-Skills]] - Crew stat system
- [[Crew-Module-Mechanics]] - Crew-module interaction

---

*This log should be referenced when questions arise about design intent. All decisions are binding unless superseded by a later decision log.*
