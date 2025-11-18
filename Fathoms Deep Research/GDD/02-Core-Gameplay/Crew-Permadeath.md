---
tags: [planned, phase2, crew-management, permadeath, high-stakes, navy-field-inspired]
status: 📋 PLANNED
phase: Phase 2
priority: HIGH
last-updated: 2025-11-17
---

# Crew Permadeath System

## Overview
The Crew Permadeath System introduces high-stakes consequences to naval combat by putting veteran crew cards at risk of permanent loss when ships are destroyed in high-tier battles. This extraction-game-inspired mechanic creates meaningful risk/reward decisions, where months of crew investment can be lost in a single battle. A retrieval system softens the blow by allowing players (or other players) to recover "dead" crews within time windows, creating emergent gameplay around corpse running and ransom negotiations.

## Implementation Status
**Status**: 📋 PLANNED (designed but not implemented)
**Phase**: Phase 2 - Core Gameplay Systems
**Scripts**: TBD (pending implementation)
**Priority**: HIGH (critical to stakes and player engagement)

---

## Design Specification

### Core Philosophy
Crew permadeath serves multiple design goals:
1. **Stakes Creation**: High-tier combat has real consequences beyond ship repair costs
2. **Investment Protection**: Low-tier zones remain safe for crew training
3. **Emergent Gameplay**: Retrieval mechanics create player-to-player interactions
4. **Risk/Reward Balance**: Higher rewards in dangerous zones justified by crew death risk
5. **Anti-Zerging**: T10 battles require serious commitment (100% crew loss)

**Key Design Pillars:**
- **Tier-Based Scaling**: Crew card permadeath risk increases with battle tier (0/0/0/0/0/10/20/40/60/100%)
- **Independent Rolls**: Each crew card rolls separately for permadeath
- **Separate from Sailor Casualties**: Sailor deaths (replaceable) are distinct from crew card permadeath (permanent)
- **Level-Agnostic**: Level 1 and Level 200 crew cards have identical permadeath chances
- **Retrieval Window**: "Dead" crew cards can be recovered within time limits
- **Player-to-Player Retrieval**: Other players can rescue crew cards for rewards
- **No Retrieval in T10**: Highest tier has permanent, unrecoverable losses

### Key Features
- **Crew Card Permadeath by Tier**: 0% (T1-T5), 10% (T6), 20% (T7), 40% (T8), 60% (T9), 100% (T10)
- **Retrieval Timer System**: 15-60 minute windows based on zone danger
- **Death Location Markers**: Map markers show retrieval locations
- **Player Retrieval Profession**: New playstyle focused on crew card recovery
- **Ransom Negotiations**: Player-to-player negotiations for crew card return
- **Backup Crew Strategy**: Multiple crew card sets for risk management
- **Strategic Investment Decisions**: Elite crew cards only on large, valuable ships
- **Sailor Casualties Separate**: Individual sailor deaths (replaceable) happen regardless of card survival

### User Experience
Players accept crew card permadeath risk when entering T6+ battles. Upon ship destruction, crew cards roll independently for permadeath. Surviving cards transfer to the player's barracks; "dead" cards are marked at the death location with a retrieval timer. Players can return to recover their own crew cards or watch as other players retrieve them for ransom. T10 battles offer no retrieval - all crew cards are permanently lost on ship destruction.

**Note**: Sailor casualties (individual sailors dying on crew cards) are a separate system and occur based on damage severity, not tier-based permadeath rolls. Lost sailors reduce crew card effectiveness but can be replaced at ports.

**Crew Card Permadeath Flow:**
1. Ship destroyed in T6+ battle
2. Each crew card rolls for permadeath (10/20/40/60/100% based on tier)
3. Surviving crew cards automatically return to player barracks
4. "Dead" crew cards marked at death location on map
5. Retrieval timer begins (15-60 minutes based on zone)
6. Original player can return to location to recover crew cards
7. Other players can retrieve crew cards for rewards/ransom
8. Timer expiration = permanent crew card loss
9. T10 exception: No retrieval possible, all crew cards instantly lost

---

## Technical Implementation

### Current Implementation
**Not yet implemented** - This section is a design specification for Phase 2 development.

### Key Components

#### Death Conditions & Risk Scaling

**Tier-Based Crew Card Permadeath Chance:**
```
T1-T5 (Safe Zones):
- Crew card permadeath chance: 0%
- All crew cards always survive ship destruction
- Perfect for crew card training and low-risk operations
- Sailor casualties still occur (replaceable damage)

T6 (First Permadeath Tier):
- Crew card permadeath chance: 10% per card (independent rolls)
- First tier where crew cards face permanent loss risk
- Significant psychological barrier for players
- Retrieval possible (15-60 minute windows)

T7 (Escalating Risk):
- Crew card permadeath chance: 20% per card
- Risk doubles from T6
- Retrieval still possible

T8 (High Stakes):
- Crew card permadeath chance: 40% per card
- Substantial risk to veteran crew cards
- High-value targets for retrieval profession

T9 (Extreme Risk):
- Crew card permadeath chance: 60% per card
- More likely to lose crew cards than keep them
- Only for serious expeditions

T10 (Ultimate Permadeath Tier):
- Crew card permadeath chance: 100% (all crew cards destroyed)
- NO RETRIEVAL POSSIBLE
- Permanent, unrecoverable loss
- Highest stakes combat in the game
```

**Crew Card Permadeath Roll Mechanics:**
```
When ship destroyed at T6-T9:
1. For each crew card on ship:
   - Roll random 0.0-1.0 against tier threshold
   - T6: If roll < 0.10 → crew card "dies" (marked for retrieval)
   - T7: If roll < 0.20 → crew card "dies"
   - T8: If roll < 0.40 → crew card "dies"
   - T9: If roll < 0.60 → crew card "dies"
   - Otherwise → crew card survives (returns to barracks)

2. Independent rolls mean statistical variance:
   - Ship with 6 crew cards destroyed in T8
   - Expected losses: 6 × 0.40 = 2.4 cards
   - Actual losses: 0-6 cards (statistical distribution)
   - Possible to lose 0 cards (lucky, ~4.7% chance)
   - Possible to lose all 6 cards (unlucky, ~0.4% chance)

3. Level does NOT affect survival chance:
   - Level 1 crew card: Same % permadeath chance as tier
   - Level 200 elite crew card: Same % permadeath chance as tier
   - Investment time/cost irrelevant to permadeath probability

4. Sailor casualties are SEPARATE:
   - Even surviving crew cards lose sailors based on damage
   - Lost sailors reduce card effectiveness
   - Replaceable at ports for credits
```

**T10 Exception:**
```
When ship destroyed at T10:
1. All crew cards instantly destroyed (no rolls, 100% permadeath)
2. No retrieval markers created
3. Permanent loss immediately
4. No recovery possible under any circumstances

Strategic Impact:
- T10 battles reserved for most serious players
- Requires dedicated T10 crew card sets (separate from main crews)
- Creates "T10 crew economy" of cheaper, expendable crew cards
- Or use backup Level 100-150 crew cards instead of Level 200 elites
```

#### Strategic Impact on Gameplay

**Investment Risk Assessment:**
```
Level 200 Elite Gunner Value:
- Time investment: 300-400 hours combat grinding
- Credit investment: 1.5-2B credits (hybrid leveling approach)
- Specialization unlocks: 50M+ credits
- Total value: ~2,000+ hours or 2B+ credits equivalent

Death in T8 Battle:
- 30% chance to lose entire investment
- 70% chance to survive and continue use
- Expected value: 0.30 × 2B = 600M credit risk per battle

Player Decision Matrix:
- Use elite crew for 130% efficiency? (high performance, high risk)
- Use backup Level 100 crew for 115% efficiency? (lower performance, lower risk)
- Stay in T7 zones where risk is lower? (safer, lower rewards)
```

**Backup Crew Strategy:**
```
Veteran players maintain multiple crew sets:

Primary Elite Set (Levels 150-200):
- Used on most valuable ships
- Reserved for critical missions
- Maximum performance
- High permadeath risk

Secondary Backup Set (Levels 100-150):
- Used on secondary ships
- Daily operations and farming
- Good performance (100-115% efficiency)
- Moderate permadeath risk

Tertiary Expendable Set (Levels 50-100):
- Used on high-risk missions
- T10 operations
- Acceptable performance (85-100% efficiency)
- Low emotional attachment if lost

This creates "crew insurance" through redundancy
```

#### Retrieval & Rescue System

**Death Location Mechanics:**
```
When crew card "dies" in T5-T9 battle:
1. Death location marked on map with coordinates
2. Retrieval timer starts based on zone danger level
3. Marker visible to:
   - Original owner (always)
   - Allied faction players (optional setting)
   - All players (optional setting, more rewards for risk)
4. Marker shows:
   - Number of crew cards retrievable
   - Time remaining on retrieval timer
   - Zone danger level
   - Original owner (optional, for ransom negotiations)
```

**Retrieval Timer by Zone:**
```
Safe Zones (T1-T4):
- Retrieval timer: 60 minutes real-time
- Low enemy presence
- Easy recovery for original player
- Low risk for retrieval professionals

Contested Zones (T5-T6):
- Retrieval timer: 30 minutes real-time
- Moderate enemy presence
- Challenging recovery
- Medium risk for retrieval professionals

Hostile Zones (T7-T9):
- Retrieval timer: 15 minutes real-time
- High enemy presence
- Difficult recovery requiring speed/stealth
- High risk for retrieval professionals

Permadeath Zones (T10):
- Retrieval timer: N/A (no retrieval possible)
- Permanent loss immediately
- Creates ultimate stakes
```

**Original Player Retrieval:**
```
Player's own ship destroyed in T7 zone:
1. Respawn at nearest port or extraction point
2. Check death location marker on map
3. Calculate: Can I get there in 15 minutes?
4. Decision factors:
   - Distance to death location
   - Enemy presence in area
   - Value of dead crews
   - Risk of losing retrieval ship + crews
   - Alternative: let other player retrieve for ransom

Example "Corpse Run":
- Ship destroyed 8km from friendly port
- 4 crew cards dead (2 Level 150s, 2 Level 100s)
- 15-minute timer active
- Equip fast destroyer with cheap backup crews
- Rush to location, dodge enemy patrols
- Reach death marker with 3 minutes remaining
- Retrieve all 4 crews successfully
- Return to port, avoid further combat
- Net result: Saved ~1B+ credits of crew investment
```

**Player-to-Player Retrieval System:**
```
Retrieval Profession Mechanics:
1. Other players can see death location markers
2. Travel to death location before timer expires
3. Retrieve dead crew cards
4. Crew cards transferred to retriever's possession
5. Original owner notified of retrieval
6. Negotiation phase begins

Ransom Negotiation:
- Retriever contacts original owner
- Offers to return crews for payment
- Original owner can:
  a) Pay ransom (get crews back)
  b) Refuse ransom (crews sold on market by retriever)
  c) Negotiate alternative compensation (future favors, alliance, etc.)

Retrieval Rewards (if owner doesn't pay ransom):
- Base reward: 10-25% of crew card's training value
- Example: Level 150 crew (1.5B value) = 150-375M credit base reward
- Can sell retrieved crews on player market
- Reputation gain with crew's nation
- Special retrieval missions with bonus rewards
```

**Retrieval Gameplay Examples:**
```
Scenario 1: Friendly Retrieval
- German player destroys British ship in T8 zone
- 5 British crew cards marked for retrieval
- German player retrieves crews
- Contacts British player: "I have your crews, 100M for return"
- British player pays 100M ransom
- Crews returned, both players profit (retriever gets 100M, owner saves 1B+ value)

Scenario 2: Hostile Retrieval
- Player A loses T9 battleship, 3 elite crews dead
- Player B (enemy faction) retrieves crews
- Demands 500M ransom
- Player A refuses (too expensive)
- Player B sells crews on market for 300M
- Player A must re-level new crews (loses 400+ hours investment)

Scenario 3: Retrieval Profession
- Player C specializes in retrieval operations
- Monitors death markers in T7-T8 zones
- Uses fast, cheap ships to minimize risk
- Averages 3-5 retrievals per play session
- Earns 200-500M credits per session
- Builds reputation as reliable retriever
- Some players pay retainer fees for priority retrieval
```

### Configuration

**Tunable Parameters:**
```
// Crew Card Permadeath Chances by Tier
T1_PERMADEATH_CHANCE = 0.0 (0% - completely safe)
T2_PERMADEATH_CHANCE = 0.0 (0% - completely safe)
T3_PERMADEATH_CHANCE = 0.0 (0% - completely safe)
T4_PERMADEATH_CHANCE = 0.0 (0% - completely safe)
T5_PERMADEATH_CHANCE = 0.0 (0% - last safe tier)
T6_PERMADEATH_CHANCE = 0.10 (10% - first permadeath tier)
T7_PERMADEATH_CHANCE = 0.20 (20% per crew card, independent)
T8_PERMADEATH_CHANCE = 0.40 (40% per crew card, independent)
T9_PERMADEATH_CHANCE = 0.60 (60% per crew card, independent)
T10_PERMADEATH_CHANCE = 1.0 (100% - all crew cards destroyed)

// Retrieval Timers
SAFE_ZONE_RETRIEVAL_TIME = 3600 seconds (60 minutes - T1-T5)
CONTESTED_ZONE_RETRIEVAL_TIME = 1800 seconds (30 minutes - T6-T7)
HOSTILE_ZONE_RETRIEVAL_TIME = 900 seconds (15 minutes - T8-T9)
T10_RETRIEVAL_TIME = 0 seconds (no retrieval possible)

// Retrieval Rewards
BASE_RETRIEVAL_REWARD_MIN = 0.10 (10% of crew card value)
BASE_RETRIEVAL_REWARD_MAX = 0.25 (25% of crew card value)
RETRIEVAL_REPUTATION_GAIN = 100 points per crew card

// Ransom System
RANSOM_NEGOTIATION_TIME = 300 seconds (5 minutes)
MAX_RANSOM_HISTORY = 50 negotiations (for reputation tracking)

// Sailor Casualties (Separate System)
SAILOR_CASUALTY_BASE_RATE = varies by damage severity
SAILOR_CASUALTY_REPLACEABLE = true (pay credits at port)
```

---

## Integration Points

### Depends On
- [[Crew-Management]] - Base crew card system
- [[Crew-Progression]] - Crew value calculations for ransoms
- [[Combat-System]] - Ship destruction triggers death rolls
- [[Map-System]] - Death location markers and zone classification
- [[Economy-System]] - Ransom payments and retrieval rewards
- [[Reputation-System]] - Retrieval profession reputation

### Used By
- [[Player-Progression]] - Permadeath creates long-term stakes
- [[Faction-Warfare]] - Cross-faction retrieval dynamics
- [[Player-Trading]] - Retrieved crew market
- [[Social-Systems]] - Ransom negotiations and alliances

---

## Example Scenarios

### Scenario 1: First Permadeath Experience
**Captain Murphy enters T6 for first time**

**Setup:**
- New to T6 combat tier (first permadeath tier)
- Ship has 6 crew cards: 2 Level 75 Gunners, 1 Level 70 Engineer, 1 Level 60 AA, 2 Level 50 support
- Total investment: ~150 hours combat + 200M credits
- First battle in crew card permadeath zone

**Battle Outcome:**
- Ship destroyed in T6 battle
- Crew card permadeath rolls execute (10% chance per card):
  - Gunner A: Roll 0.42 → Survives (≥0.10) ✓
  - Gunner B: Roll 0.08 → Dies (<0.10) ⚠️ CREW CARD LOST
  - Engineer: Roll 0.65 → Survives (≥0.10) ✓
  - AA Specialist: Roll 0.89 → Survives (≥0.10) ✓
  - Support A: Roll 0.05 → Dies (<0.10) ⚠️ CREW CARD LOST
  - Support B: Roll 0.51 → Survives (≥0.10) ✓
- Sailor casualties also occur on surviving cards (separate rolls, replaceable)

**Result:**
- 4 crew cards survive, return to barracks immediately
- 2 crew cards destroyed, marked at death location for retrieval
- 30-minute retrieval timer starts (contested zone)
- Death location: 6km from nearest friendly port

**Player Decision:**
- Option A: Corpse run (risky, 30 min window)
  - Equip fast ship with backup crew cards
  - Rush to location, retrieve 2 "dead" crew cards
  - Risk: Losing retrieval ship + backup crew cards
  - Reward: Save 80 hours + 100M credits investment

- Option B: Accept losses (safe)
  - Let timer expire
  - Permanently lose 2 crew cards (must recruit new Level 1 cards)
  - Re-level new crew cards from scratch
  - Avoid additional risk

**Choice:** Murphy attempts corpse run
- Reaches location with 8 minutes remaining
- Successfully retrieves both crew cards
- Returns to port safely
- Replaces lost sailors on surviving cards (50M credits)
- **Emotional impact: First crew card permadeath experience, high stakes realized**

### Scenario 2: Elite Crew Loss
**Captain Yamamoto loses T8 battleship**

**Setup:**
- Veteran player with elite crew roster
- Main battery crew: Level 180 Master Gunnery Officer (400+ hours, 5M credits invested)
- Secondary crews: Level 150-170 (200-300 hours each)
- Total ship crew value: ~10B credits equivalent

**Battle Outcome:**
- Ship destroyed in intense T8 battle
- Crew card permadeath rolls execute (40% chance per card):
  - Level 180 Master Gunner: Roll 0.27 → Dies (<0.40) ⚠️💀 CARD DESTROYED
  - Level 170 Fire Control: Roll 0.54 → Survives (≥0.40) ✓
  - Level 165 Heavy Gunner: Roll 0.71 → Survives (≥0.40) ✓
  - Level 160 Engineer: Roll 0.12 → Dies (<0.40) ⚠️ CARD DESTROYED
  - Level 155 Damage Control: Roll 0.88 → Survives (≥0.40) ✓
  - Level 150 AA Master: Roll 0.45 → Survives (≥0.40) ✓
  - Level 150 Electronics: Roll 0.19 → Dies (<0.40) ⚠️ CARD DESTROYED
  - Level 145 Command: Roll 0.63 → Survives (≥0.40) ✓
- Sailor casualties also occur on surviving cards (separate damage-based rolls)

**Result:**
- 5 crew cards survive (still valuable, 145-170 range)
- 3 crew cards destroyed, marked at death location for retrieval:
  - Level 180 Master Gunner (flagship crew card, months of work)
  - Level 160 Engineer (critical crew card)
  - Level 150 Electronics
- 15-minute retrieval timer (hostile zone)
- Death location: 12km from friendly port, enemy-controlled waters

**Player Decision:**
- Distance too far for 15-minute window
- Enemy patrol activity too high
- **Cannot personally retrieve**

**Watches helplessly as timer expires:**
- Minute 5: Enemy player spotted near death marker
- Minute 8: Enemy player retrieves all 3 crews
- Minute 10: Ransom negotiation request received
  - Demand: 800M credits for all 3 crews
  - Alternative: 500M for just the Level 180 Master Gunner

**Yamamoto's Choice:**
- Pays 500M to recover Level 180 Master Gunner (irreplaceable)
- Lets Enemy keep Level 160 Engineer and Level 150 Electronics
- **Total loss: 500M credits + 2 high-level crews (~250 hours investment)**

**Aftermath:**
- Re-levels new Engineer from Level 100 backup (50 hours grinding)
- Re-levels new Electronics from scratch (80 hours grinding)
- **Emotional impact: Months of investment lost in one battle**
- **Behavioral change: More cautious in T8, uses backup crews for risky missions**

### Scenario 3: Retrieval Profession Success
**Captain Mueller runs retrieval operations**

**Setup:**
- Specialized retrieval player
- Operates fast, cheap T6 destroyer (minimal crew investment)
- Monitors death markers in T7-T8 zones
- Has built reputation as fair retriever (reasonable ransoms)

**Session Activity:**

**Retrieval 1 (30 minutes into session):**
- Spots death marker: 4 crews, T7 zone, 12 minutes remaining
- Rushes to location, avoids enemy patrol
- Retrieves 4 crews (2 Level 120s, 2 Level 100s)
- Contacts original owner (British player)
- Negotiates: 150M for all 4 crews (fair price)
- Owner pays, crews returned
- **Profit: 150M credits, 15 minutes work**

**Retrieval 2 (1 hour into session):**
- Death marker in hostile waters: 2 crews, T8 zone, 8 minutes remaining
- Very risky location (enemy territory)
- Decides to attempt anyway (high-value crews visible)
- Retrieves 2 Level 180 elite crews under fire
- Escapes with 15% hull damage
- Contacts owner: "I have your Level 180s, 600M total or 350M each"
- Owner (Captain Schmidt) refuses (too expensive)
- Mueller sells on player market for 800M total
- **Profit: 800M credits, 25 minutes work, high risk**

**Retrieval 3 (2 hours into session):**
- Easy retrieval in contested zone: 3 crews, 25 minutes remaining
- Retrieves 3 Level 60-80 crews (mid-tier value)
- Owner pays 80M ransom quickly
- **Profit: 80M credits, 10 minutes work**

**Session Total:**
- **Time invested:** 2 hours gameplay
- **Profit:** 1,030M credits
- **Risk:** Lost 15% hull on one retrieval (20K repair cost)
- **Net profit:** 1,010M credits in 2 hours
- **Reputation gain:** +700 retrieval reputation points
- **Player satisfaction:** Emergent gameplay, profitable profession

### Scenario 4: T10 Ultimate Stakes
**Captain Lee attempts first T10 battle**

**Setup:**
- Experienced T9 player, ready for T10
- Dilemma: Which crews to bring?
  - Option A: Elite Level 180-200 crews (maximum performance)
  - Option B: Backup Level 120-150 crews (acceptable performance)

**Risk Assessment:**
- T10 = 100% crew death, no retrieval
- Elite crews: 2B+ credits value, 500+ hours investment
- Backup crews: 500M credits value, 150 hours investment
- Performance difference: ~10-15% efficiency gap

**Decision:** Use backup Level 120-150 crews
- Sacrifice 10% performance for crew preservation
- Keep elite crews safe for T9 operations
- **Rationale:** Elite crew loss not worth marginal performance gain

**Battle Outcome:**
- Ship destroyed in T10 battle
- **All 8 crew cards instantly die (100% death chance)**
- No retrieval markers created
- Permanent loss immediately

**Total Loss:**
- 8 crews (Levels 120-150)
- ~500M credits equivalent
- ~150-200 hours investment
- **Emotional impact: Significant but acceptable (backup crews)**

**If Elite Crews Used Instead:**
- Would have lost 2B+ credits equivalent
- Would have lost 500+ hours investment
- Performance gain: 10-15% (not worth it)
- **Validates decision to use backup crews**

**Behavioral Outcome:**
- Develops "T10 crew set" of expendable Level 100-120 crews
- Never brings elite crews to T10
- Creates separate progression path: Elite crews for T7-T9, backups for T10
- **System working as intended: T10 has ultimate stakes**

### Scenario 5: Retrieval Drama
**Captain Schmidt (Germany) dies in T7 zone**

**Initial Situation:**
- German battleship destroyed in British-controlled T7 waters
- 6 crew cards on ship, 4 fail death rolls (4 dead, 2 survive)
- Dead crews: 2 Level 150 Gunners, 1 Level 140 Engineer, 1 Level 120 AA
- 15-minute retrieval timer
- Location: Deep in hostile British waters, 20km from German port

**Schmidt's Attempt:**
- Equips fast T5 cruiser with backup crews
- Attempts corpse run despite 20km distance
- 10 minutes remaining: Intercepted by British destroyer patrol
- Forced to flee or risk losing cruiser + backup crews
- **Abandons retrieval attempt**

**Player Mueller Enters:**
- German player Mueller spots retrieval marker
- Closer location (8km away)
- Equips stealth-focused ship
- 8 minutes remaining on timer

**Mueller's Retrieval:**
- Races to location, activates smoke screen
- Dodges British patrol using radar evasion
- Reaches death marker with 3 minutes remaining
- Retrieves all 4 crew cards successfully
- **High-stakes escape:**
  - British battleship spots him
  - Engaged while trying to escape
  - Takes 40% hull damage
  - Smoke screen expires, uses speed to outrun
  - Reaches German port with 8% hull remaining
  - **Successful retrieval under fire**

**Negotiation Phase:**
- Mueller contacts Schmidt: "I have your 4 crews, barely made it out alive"
- Shows battle damage screenshots (40% hull damage proof)
- Schmidt grateful: "What's your price?"
- Mueller: "Fair price: 200M for all 4, or I can sell on market for ~300M"
- Schmidt appreciates fairness: "Done, 200M + 50M bonus for the risk you took"
- **Final deal: 250M credits**

**Outcome:**
- Schmidt saves 4 high-level crews (~300 hours, 800M value)
- Mueller earns 250M for 20 minutes of high-risk gameplay
- Both players benefit from retrieval system
- **Emergent gameplay: Player cooperation under fire, fair negotiations**
- Schmidt adds Mueller to friends list, future alliance potential

---

## Known Issues
- **None (design phase)** - Not yet implemented

## Future Enhancements
- **Crew Insurance System**: Optional insurance purchased before battle (pays out if crew dies)
- **Retrieval Beacons**: Consumable items that extend retrieval timers (+5-10 minutes)
- **Retrieval Contracts**: Pre-arrange retrieval agreements with other players
- **Faction Retrieval Services**: NPC retrieval option (expensive, guaranteed)
- **Death Statistics**: Track crew survival rates, retrieval success rates
- **Memorial System**: Players can create memorials for permanently lost elite crews
- **Retrieval Leaderboards**: Track most successful retrieval professionals
- **Black Market Crews**: Stolen crews (not ransomed) marked as "hot" (discounted but risky)

---

## Cross-References
- [[Crew-Management]] - Base crew card system and structure
- [[Crew-Progression]] - Crew investment value calculations
- [[Crew-Specialization]] - Elite crew specializations at risk
- [[Combat-System]] - Ship destruction triggers death rolls
- [[Economy-System]] - Ransom payments and retrieval rewards
- [[Player-Trading]] - Retrieved crew marketplace
- [[Reputation-System]] - Retrieval profession reputation
- [[Faction-Warfare]] - Cross-faction retrieval dynamics

---

## Testing

### Test Coverage
- [ ] Death roll probability distribution (30% chance per card)
- [ ] Retrieval timer countdown accuracy
- [ ] Death location marker visibility
- [ ] Player-to-player retrieval mechanics
- [ ] Ransom negotiation system
- [ ] T10 instant death (100% loss, no retrieval)
- [ ] Edge cases (timer expiration, retriever death, etc.)
- [ ] Statistical variance over 1000+ ship destructions

### Test Results
Not yet implemented - testing pending Phase 2 development.

---

## Changelog
- **2025-11-17**: Initial design document created from GDD_Updated-1.md (lines 162-516)
