# Reputation System

**Status**: 📋 PLANNED (Phase 3 feature)
**Tags**: [planned, phase3, faction-system, reputation]
**Priority**: MEDIUM (Phase 3 focus)
**Last Updated**: 2025-11-17

---

## Vision Statement

Multi-faceted reputation framework where player actions dynamically affect standing with nations, creating meaningful consequences for diplomatic choices, combat behavior, and economic activities that directly impact access to ports, equipment, missions, and pricing.

---

## Core Reputation Mechanics

### Reputation Scale

**Numerical Range**: -100 to +100

**Reputation Categories**:
```
+90 to +100: LEGENDARY      ⭐⭐⭐⭐⭐ (National Hero)
+75 to +89:  EXALTED        ⭐⭐⭐⭐   (Honored Ally)
+50 to +74:  REVERED        ⭐⭐⭐     (Trusted Friend)
+25 to +49:  FRIENDLY       ⭐⭐       (Welcomed Visitor)
  0 to +24:  NEUTRAL        ⭐         (Acceptable)
-24 to  -1:  UNFRIENDLY     ☆         (Tolerated)
-49 to -25:  HOSTILE        ✗         (Unwelcome)
-74 to -50:  HATED          ✗✗        (Enemy)
-89 to -75:  ABHORRED       ✗✗✗       (Shoot on Sight)
-100 to -90: NEMESIS        ☠         (War Criminal)
```

**Visual Representation**:
- Reputation bar showing current standing
- Numerical value displayed (e.g., +67)
- Category label (e.g., "REVERED with US Navy")
- Progress bar to next category threshold
- Recent changes log (last 10 reputation events)

---

## Starting Reputation

### Character Creation

**Chosen Nation** (Starting Home):
- **Base Reputation**: +50 (REVERED)
- **Reasoning**: Born and raised in nation, loyal citizen
- **Benefits**: Immediate access to most services and ports
- **Growth Path**: Clear path to EXALTED and LEGENDARY status

**Other Major Nations**:
- **Base Reputation**: 0 (NEUTRAL)
- **Reasoning**: Unknown foreigner, no history of cooperation or conflict
- **Benefits**: Basic commercial access, no military access
- **Growth Path**: Can improve through missions and diplomatic actions

**Pirate Faction**:
- **Base Reputation**: -50 (HATED)
- **Reasoning**: Pirates threaten all lawful nations
- **Consequences**: Hostile encounters with pirate NPCs
- **Cannot Improve**: Pirate reputation locked at -50 minimum (unless you become pirate)

**If Choosing Pirate Faction**:
- **All Nations**: -75 (ABHORRED)
- **Pirates**: +50 (REVERED among outlaws)
- **Reasoning**: Chosen life of piracy, hostile to law and order
- **Consequences**: Permanent outcast from civilized society

---

## Reputation Gain Methods

### Combat Actions

**Destroying Enemy Ships** (Based on diplomatic state):

**At War with Target Nation**:
```
Enemy Destroyer Sunk:
- Home Nation: +5 reputation (defending nation)
- Enemy Nation: -10 reputation (attacking their forces)
- Allied Nations: +2 reputation (supporting alliance)
- Neutral Nations: 0 reputation (no opinion on conflict)

Enemy Cruiser Sunk:
- Home Nation: +8 reputation
- Enemy Nation: -15 reputation
- Allied Nations: +3 reputation

Enemy Battleship Sunk:
- Home Nation: +15 reputation (major victory)
- Enemy Nation: -25 reputation (significant loss)
- Allied Nations: +5 reputation
- Neutral Nations: -2 reputation (destabilizing action)

Example: US Player sinks IJN Battleship during USA-Japan war
- US Navy: +15 (war hero)
- Japanese Navy: -25 (enemy of state)
- British Navy: +5 (US allied with UK)
- German Navy: 0 (neutral to conflict)
```

**Destroying Peaceful Nation Ships** (No war declared):
```
Attack on Peaceful Nation:
- Victim Nation: -20 reputation (unprovoked attack)
- Victim's Allies: -10 reputation (attack on friend)
- Home Nation: -5 reputation (dishonorable conduct)
- Pirates: +3 reputation (lawless behavior)

Example: US Player sinks British Destroyer (peacetime)
- British Navy: -20 (betrayal)
- US Navy: -5 (dishonorable American)
- German Navy: +2 (enemy of enemy)
- Pirates: +3 (pirate-like behavior)

Consequences:
- Can turn previously friendly nation hostile
- Risk starting diplomatic incident
- Economic penalties in multiple nations
```

**Destroying Pirate Ships**:
```
Pirate Destroyer Sunk:
- All Nations: +3 reputation (protecting commerce)
- Pirates: -15 reputation (you're their enemy)

Pirate "Legendary" Ship Sunk:
- All Nations: +10 reputation (major threat eliminated)
- Pirates: -50 reputation (you killed their hero)

Benefits:
- Low-risk reputation gain (no diplomatic consequences)
- All nations appreciate anti-piracy efforts
- Good for rebuilding damaged reputation
```

### Mission Completion

**Faction-Specific Missions**:

**Low-Level Missions** (Tier 1-2):
```
Patrol Mission:
- Issuing Nation: +2 reputation
- Rewards: 1,500 credits + reputation

Escort Convoy:
- Issuing Nation: +3 reputation
- Rewards: 2,500 credits + reputation

Anti-Submarine Patrol:
- Issuing Nation: +4 reputation
- Rewards: 3,000 credits + reputation
```

**Mid-Level Missions** (Tier 3-4):
```
Strike Enemy Port:
- Issuing Nation: +8 reputation
- Enemy Nation: -12 reputation
- Rewards: 12,000 credits + reputation

Reconnaissance Operation:
- Issuing Nation: +6 reputation
- Rewards: 8,000 credits + reputation + intelligence

Fleet Support:
- Issuing Nation: +10 reputation
- Allied Nation: +3 reputation
- Rewards: 15,000 credits + reputation
```

**High-Level Missions** (Tier 5-6):
```
Major Fleet Engagement:
- Issuing Nation: +20 reputation
- Allied Nations: +8 reputation
- Enemy Nations: -30 reputation
- Rewards: 50,000 credits + reputation + special equipment

Strategic Campaign:
- Issuing Nation: +30 reputation (multi-week operation)
- Rewards: 100,000 credits + reputation + unique rewards

Legendary Mission:
- Issuing Nation: +50 reputation (once per player career)
- Rewards: Legendary ship, massive credits, national recognition
```

**Repeatable Daily Missions**:
```
Daily Patrol: +1 reputation (max once per day)
Weekly Objective: +5 reputation (max once per week)
Monthly Campaign: +15 reputation (max once per month)

Prevents Exploitation:
- Diminishing returns on repetition
- Time gates prevent grinding
- Encourages diverse activities
```

### Economic Contributions

**Trade Contracts**:

**Supplying Nation with Resources**:
```
Small Contract (10,000 credits value):
- Issuing Nation: +1 reputation per contract
- Frequency: Can complete multiple times per week

Medium Contract (50,000 credits value):
- Issuing Nation: +3 reputation per contract
- Frequency: Once per week maximum

Large Contract (200,000 credits value):
- Issuing Nation: +10 reputation per contract
- Frequency: Once per month maximum

Example: British Admiralty Steel Contract
- Deliver 500 tons steel monthly
- British Navy: +10 reputation per delivery
- Annual total: +120 reputation (through trade alone)
```

**Factory Production Supporting War Effort**:
```
Running Factory in Nation Territory:
- Home Nation: +2 reputation per week (passive generation)
- Reasoning: Supporting national economy and war production

Example: US Player operates steel mill in Pearl Harbor
- Produces 2,000 units steel per week
- 70% sold to US Navy at contract prices
- US Navy: +2 reputation per week passively
- Annual passive gain: +104 reputation (just from operating business)
```

**Economic Warfare Against Enemies**:
```
Disrupting Enemy Supply Lines:
- Home Nation: +5 reputation per major convoy sunk
- Enemy Nation: -15 reputation
- Economic impact more valuable than tactical victory

Example: German U-boat sinks British convoy (8 merchants)
- German Navy: +5 reputation (strategic success)
- British Navy: -15 reputation (damaging war effort)
```

### Diplomatic Actions

**Assisting Allied Players**:
```
Rescuing Friendly Player:
- Saved Player's Nation: +2 reputation
- Your Nation: +1 reputation (good conduct)

Example: British player saves sinking US destroyer
- US Navy: +2 reputation (gratitude)
- British Navy: +1 reputation (upholding alliance)
```

**Sharing Intelligence**:
```
Providing Strategic Intelligence:
- Receiving Nation: +5 reputation per valuable intelligence
- Quality matters: Accurate, timely, actionable information

Example: Scout reports enemy battleship position
- US Navy: +5 reputation (intelligence leads to successful ambush)
```

**Participating in Joint Operations**:
```
Multi-Nation Fleet Operation:
- All Participating Nations: +8 reputation
- Success Bonus: Additional +5 reputation

Example: US-UK joint convoy escort mission
- US Navy: +8 reputation (cooperation)
- British Navy: +8 reputation (allied operation)
- If successful: Additional +5 each
```

---

## Reputation Loss Methods

### Combat Violations

**Attacking Peaceful Nations**:

**Unprovoked Attack on Friendly Nation** (+25 or higher):
```
Single Ship Destroyed:
- Victim Nation: -20 reputation (betrayal)
- Victim's Allies: -10 reputation (attack on friend)
- Your Nation: -10 reputation (dishonor to flag)
- Neutral Nations: -5 reputation (untrustworthy)

Multiple Ships Destroyed (3+ in single incident):
- Victim Nation: -50 reputation (act of war)
- Victim's Allies: -25 reputation (severe provocation)
- Your Nation: -20 reputation (war crime potential)

Example: US Player attacks British convoy (peacetime)
- British Navy: -20 per ship (up to -100 total)
- US Navy: -10 per ship (dishonorable conduct)
- German Navy: +5 (pleased enemy attacked)
```

**Attacking Neutral Nations** (-24 to +24):
```
Single Ship Destroyed:
- Victim Nation: -15 reputation
- Your Nation: -3 reputation (poor conduct)
- International Community: -2 reputation (all nations)

Strategic Rationale:
- May attack neutrals but consequences are severe
- Economic warfare against neutral traders possible
- Risk vs reward: Is target worth reputation loss?
```

**Friendly Fire**:
```
Accidental Damage to Friendly Ship:
- Damaged Ship's Nation: -2 reputation (accident)
- Forgiven if: Immediate apology and compensation

Destroying Friendly Ship:
- Victim Nation: -30 reputation (severe negligence or treachery)
- Your Nation: -15 reputation (incompetence or betrayal)
- May trigger friendly fire investigation (GM review)

Repeated Friendly Fire (3+ incidents):
- All Nations: -50 reputation (marked as incompetent or treasonous)
- Potential suspension from faction missions
```

### Mission Failures

**Abandoning Missions**:
```
Accepting Mission but Abandoning:
- Issuing Nation: -5 reputation (unreliable)
- Repeat Abandonment (3+ times): -15 reputation (blacklisted from faction missions)

Mission Failure (genuine attempt):
- Issuing Nation: -1 reputation (understood that missions can fail)
- No severe penalty for trying and failing

Example: Accept convoy escort, leave halfway through
- US Navy: -5 reputation (unreliable contractor)
- Three abandonments: -15 reputation total, temporarily blocked from missions
```

**Sabotaging Allied Operations**:
```
Intentional Mission Sabotage:
- Issuing Nation: -50 reputation (traitor)
- Allied Nations: -25 reputation (untrustworthy)
- Enemy Nations: +10 reputation (if they benefit)

Investigation:
- Requires GM review for intentional sabotage determination
- Clear evidence needed (unlikely to be false positive)
- Severe consequences if confirmed
```

### Diplomatic Incidents

**Breaking Trade Agreements**:
```
Failing Contract Delivery:
- Contract Issuer: -10 reputation (breach of contract)
- Economic consequences: Blacklisted from future contracts (30 days)

Example: Accept British steel contract, fail to deliver
- British Navy: -10 reputation
- Cannot accept British contracts for 30 days
```

**Espionage Discovery**:
```
Caught Spying on Nation:
- Target Nation: -30 reputation (espionage is serious offense)
- Your Nation: 0 reputation (spying is expected in war)

Example: US player caught gathering intelligence in German port
- German Navy: -30 reputation (spy discovered)
- US Navy: 0 reputation (intelligence gathering is part of war)
```

**Smuggling and Black Market Activity**:
```
Caught with Contraband:
- Discovering Nation: -20 reputation (illegal trade)
- Pirate Faction: +5 reputation (pirate-friendly behavior)

Detection Chance:
- Friendly Nation Ports: 5% inspection chance
- Neutral Ports: 2% inspection chance
- Enemy Ports: 25% inspection chance (high security)

Example: German player caught with stolen British radar in US port
- US Navy: -20 reputation (trafficking stolen military equipment)
- British Navy: -15 reputation (possessing stolen British technology)
- Pirates: +5 reputation (engaged in black market)
```

---

## Reputation Consequences

### Port Access

**LEGENDARY (+90 to +100)**:
- **Access**: Unrestricted access to all nation ports including secret military bases
- **Services**: Priority docking, VIP treatment, fastest repairs
- **Pricing**: 30% discount on all services and equipment
- **Exclusive**: Access to experimental technology and prototype testing
- **Prestige**: NPCs salute, special visual recognition

**EXALTED (+75 to +89)**:
- **Access**: Full access to military ports and advanced facilities
- **Services**: Priority scheduling for repairs and refits
- **Pricing**: 25% discount on all services and equipment
- **Equipment**: Access to advanced military technology
- **Missions**: Elite missions available, highest pay and rewards

**REVERED (+50 to +74)**:
- **Access**: Access to most military ports (except highest security)
- **Services**: Standard military support and logistics
- **Pricing**: 15% discount on services and equipment
- **Equipment**: Access to military-grade equipment
- **Missions**: Advanced missions available

**FRIENDLY (+25 to +49)**:
- **Access**: Commercial ports and minor military bases
- **Services**: Standard civilian services available
- **Pricing**: 5% discount on basic services
- **Equipment**: Limited military equipment access
- **Missions**: Standard missions available

**NEUTRAL (0 to +24)**:
- **Access**: Major commercial ports only
- **Services**: Basic services at standard pricing
- **Pricing**: No discounts, market rates
- **Equipment**: Civilian equipment only
- **Missions**: Basic civilian contracts only

**UNFRIENDLY (-1 to -24)**:
- **Access**: Limited to neutral ports (national ports denied)
- **Services**: Basic services only, may be refused
- **Pricing**: 10% markup on all services
- **Equipment**: Restricted, basic items only
- **Missions**: No faction missions available

**HOSTILE (-25 to -49)**:
- **Access**: Denied from all national ports
- **Services**: Refused service at allied ports
- **Pricing**: 30% markup if service provided at neutral ports
- **Equipment**: Cannot purchase nation-specific items
- **Missions**: Hunted by nation NPCs (patrol encounters)

**HATED (-50 to -74)**:
- **Access**: Denied from all ports (including neutral if allied)
- **Services**: Refused by most vendors
- **Pricing**: 50% markup if somehow service obtained
- **Equipment**: Complete embargo
- **Missions**: Active bounty on player (NPC hunters)

**ABHORRED (-75 to -89)**:
- **Access**: Shoot-on-sight orders in national waters
- **Services**: Complete denial of all services
- **Pricing**: N/A (no services available)
- **Equipment**: N/A (no trade possible)
- **Missions**: Large bounty, elite NPC hunters deployed

**NEMESIS (-90 to -100)**:
- **Access**: Kill-on-sight orders, permanent enemy status
- **Services**: Completely blacklisted
- **Pricing**: N/A
- **Equipment**: N/A
- **Missions**: Massive bounty, multiple hunter groups active
- **Special**: May trigger special "Most Wanted" event

---

### Equipment & Technology Access

**Technology Gates** (Minimum reputation required):

**Basic Equipment** (No reputation requirement):
- Standard ship hulls (T1-T2)
- Basic weapons (low-tier guns, torpedoes)
- Standard engines and propulsion
- Basic armor and structure

**Military Equipment** (+25 Reputation minimum):
- Military ship hulls (T3-T4)
- Advanced weaponry (mid-tier systems)
- Military-grade engines
- Fire control systems (basic)

**Advanced Technology** (+50 Reputation minimum):
- Advanced ship hulls (T5)
- High-tier weapons systems
- Advanced radar and electronics
- Superior fire control computers
- Specialized ammunition types

**Elite Systems** (+75 Reputation minimum):
- Legendary ship hulls (T6)
- Experimental weapons
- Cutting-edge radar and sonar
- Electronic warfare systems
- Prototype technology

**Experimental Technology** (+90 Reputation minimum):
- Prototype ships (pre-production models)
- Breakthrough weapons systems
- Classified technology
- Nation's most advanced systems
- One-of-a-kind equipment

**Example: US Navy Technology Tree**:
```
No Reputation:
- USS Porter (T1 DD)
- Basic 5-inch guns
- Standard engines

+25 Reputation:
- USS Fletcher (T3 DD)
- USS Atlanta (T3 CL)
- Advanced 5-inch guns
- Basic radar systems

+50 Reputation:
- USS Baltimore (T4 CA)
- USS Essex (T4 CV)
- 8-inch guns
- Advanced radar
- Fire control computers

+75 Reputation:
- USS Iowa (T5 BB)
- USS Midway (T5 CV)
- 16-inch guns
- Advanced AA systems
- Electronic warfare

+90 Reputation:
- USS Enterprise (T6 CV - Legendary)
- Experimental proximity fuses
- Prototype jet aircraft
- Advanced electronic warfare
- Classified systems
```

---

### Pricing Modifiers

**Formula**:
```
Final Price = Base Price × (1 + Reputation Modifier) × Regional Modifier

Reputation Modifiers:
+90 to +100 (LEGENDARY):     -30%
+75 to +89  (EXALTED):       -25%
+50 to +74  (REVERED):       -15%
+25 to +49  (FRIENDLY):      -5%
  0 to +24  (NEUTRAL):        0%
 -1 to -24  (UNFRIENDLY):    +10%
-25 to -49  (HOSTILE):       +30%
-50 to -74  (HATED):         +50%
-75 to -100 (ABHORRED+):     +100% (if service available at all)
```

**Example: Destroyer Purchase**:
```
Base Cost: USS Fletcher (T3 DD) = 45,000 credits

At Different Reputation Levels:
LEGENDARY (+95):  45,000 × 0.70 = 31,500 credits (-30%)
EXALTED (+80):    45,000 × 0.75 = 33,750 credits (-25%)
REVERED (+60):    45,000 × 0.85 = 38,250 credits (-15%)
FRIENDLY (+35):   45,000 × 0.95 = 42,750 credits (-5%)
NEUTRAL (+10):    45,000 × 1.00 = 45,000 credits (base)
UNFRIENDLY (-10): 45,000 × 1.10 = 49,500 credits (+10%)
HOSTILE (-35):    45,000 × 1.30 = 58,500 credits (+30%)
HATED (-60):      45,000 × 1.50 = 67,500 credits (+50% if sold at all)

Price Difference: 36,000 credits between LEGENDARY and HATED
Savings Motivation: Incentivizes maintaining high reputation
```

**Cumulative Savings Over Career**:
```
Average Player Equipment Purchases (over 1 year):
- Ships: 5 ships × 50,000 credits average = 250,000 credits
- Modules: 50 modules × 5,000 credits = 250,000 credits
- Ammunition: 1,000 resupplies × 500 credits = 500,000 credits
- Repairs: 100 repairs × 3,000 credits = 300,000 credits
- Total Spending: 1,300,000 credits per year

Reputation Savings:
LEGENDARY (-30%): Saves 390,000 credits per year
EXALTED (-25%):   Saves 325,000 credits per year
REVERED (-15%):   Saves 195,000 credits per year

Economic Incentive:
- Maintaining high reputation provides massive economic advantage
- 390,000 credit annual savings enables purchasing additional ships
- "Free" equipment through reputation discount
```

---

### Mission Availability

**Mission Tiers by Reputation**:

**LEGENDARY (+90 to +100)**:
- **Elite Campaign Missions**: Major strategic operations (100,000+ credit rewards)
- **Classified Operations**: Espionage and special forces missions
- **Command Roles**: Lead multi-player fleet operations
- **Experimental Testing**: Test prototype equipment for nation

**EXALTED (+75 to +89)**:
- **Advanced Strike Missions**: High-value target elimination (50,000+ credits)
- **Strategic Reconnaissance**: Deep penetration intelligence gathering
- **Fleet Command**: Command NPC battle groups
- **VIP Escort**: Protect high-value national assets

**REVERED (+50 to +74)**:
- **Combat Patrol**: Standard military operations (15,000 credits)
- **Convoy Escort**: Protect merchant convoys (12,000 credits)
- **Strike Missions**: Attack enemy installations (20,000 credits)
- **Training Operations**: Help train NPC crews (8,000 credits)

**FRIENDLY (+25 to +49)**:
- **Patrol Missions**: Basic security patrols (5,000 credits)
- **Transport Missions**: Move materials between ports (6,000 credits)
- **Scout Missions**: Reconnaissance of known areas (4,000 credits)

**NEUTRAL (0 to +24)**:
- **Civilian Contracts**: Non-military trade missions (2,000 credits)
- **Merchant Escort**: Protect civilian shipping (3,000 credits)
- **Delivery Missions**: Transport goods (1,500 credits)

**UNFRIENDLY or Lower (-1 and below)**:
- **No Faction Missions**: Denied from all national missions
- **Bounty Hunted**: May have bounties placed by nation
- **Pirate Missions Only**: If have pirate rep, can accept their missions

---

## Reputation Recovery

### Rebuilding Damaged Reputation

**Natural Decay** (Negative reputation slowly improves):
```
Passive Recovery Rate:
-1 to -49:   +1 reputation per week (just stop being hostile)
-50 to -74:  +0.5 reputation per week (longer recovery)
-75 to -100: +0.25 reputation per week (very slow, deep betrayal)

Reasoning: Time heals wounds, but serious betrayals take years to forgive

Example: Player at -60 reputation (HATED)
- Week 1: -60 → -59.5
- Week 52 (1 year): -60 → -34 (HOSTILE, but improving)
- Year 2: -34 → -8 (UNFRIENDLY, nearly recovered)
```

**Active Recovery Methods**:

**Anti-Piracy Operations** (Fastest recovery for most nations):
```
Pirate Destroyer Sunk:
- All Nations: +3 reputation
- No diminishing returns: Can repeat indefinitely
- Safest recovery method: Pirates always hostile anyway

Recovery Timeline:
From -50 (HATED) to 0 (NEUTRAL):
- Need: +50 reputation gain
- Method: Sink 17 pirate destroyers
- Time Investment: ~20 hours of active piracy hunting
```

**Humanitarian Missions**:
```
Rescuing Civilians:
- All Nations: +2 reputation (helping innocent people)
- Disaster Relief: +5 reputation (major humanitarian effort)
- Medical Supply Delivery: +3 reputation

Example: Player performs disaster relief mission
- Damaged Nation: +10 reputation (direct help)
- All Nations: +5 reputation (humanitarian recognition)
- Pirates: -2 reputation (you're too soft)
```

**Financial Reparations**:
```
Compensation for Past Actions:
- Pay 100,000 credits to injured nation: +10 reputation
- Maximum: Can buy +30 reputation total (300,000 credits)
- Diminishing Returns: Each purchase costs 20% more

Formula:
First Payment: 100,000 credits = +10 reputation
Second Payment: 120,000 credits = +10 reputation
Third Payment: 144,000 credits = +10 reputation

Total: 364,000 credits for +30 reputation
Use Case: Fast reputation recovery for wealthy players
```

**Diplomatic Missions**:
```
Special Reputation Recovery Missions:
- Available at NEUTRAL (0 reputation)
- "Prove Your Loyalty" mission series
- 5-mission arc: Each grants +10 reputation
- Total: +50 reputation upon completion

Requirements:
- Must be at 0 or positive reputation to start
- Cannot have active bounties
- Must complete all 5 missions (no abandonment)

Timeline:
- 1 mission per week (5 weeks total)
- Fast track: Complete all 5 missions in 5 weeks
- Outcome: Go from NEUTRAL (0) to REVERED (+50)
```

**Defection Recovery** (Special case):
```
Defector Reputation Cap:
- Former Nation: Maximum reputation -50 (permanent traitor mark)
- Cannot fully recover relationship with betrayed nation
- Other nations: Normal reputation system applies

Example: US player defects to Japan
- US Navy: Can only recover to -50 maximum (permanent distrust)
- Japanese Navy: Normal progression from -25 to +100
```

---

## Reputation Display & UI

### Player Interface

**Reputation Tab in Player Menu**:
```
╔══════════════════════════════════════════════════════════════╗
║                     REPUTATION STATUS                        ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  United States Navy:        ⭐⭐⭐⭐  EXALTED (+82)           ║
║  [████████████████████░░░░░░] 82/90 to LEGENDARY            ║
║  Recent: +5 (Enemy BB Sunk), +8 (Strike Mission)            ║
║                                                              ║
║  Royal Navy:                ⭐⭐⭐   REVERED (+58)           ║
║  [████████████░░░░░░░░░░░░░] 58/75 to EXALTED              ║
║  Recent: +3 (Convoy Escort), +2 (Allied Operation)          ║
║                                                              ║
║  Imperial Japanese Navy:    ✗✗     HATED (-62)              ║
║  [████████████░░░░░░░░░░░░░] -62/-50 to HOSTILE            ║
║  Recent: -10 (Destroyer Sunk), -15 (Cruiser Sunk)           ║
║                                                              ║
║  Kriegsmarine:              ✗✗✗    ABHORRED (-78)           ║
║  [██████████████░░░░░░░░░░░] -78/-75 recovering slowly     ║
║  Recent: -25 (Battleship Sunk), -10 (U-boat Sunk)           ║
║                                                              ║
║  Pirates:                   ✗✗     HATED (-55)              ║
║  [████████████░░░░░░░░░░░░░] -55 (expected, at war)        ║
║  Recent: +3 (Pirate Sunk), +3 (Pirate Sunk)                 ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

[View Detailed History] [Reputation Recovery Options]
```

**Reputation Change Notifications**:
```
🟢 REPUTATION GAINED 🟢
US Navy: +8
Reason: Successfully completed Strike Mission
New Reputation: EXALTED (+82/100)
Progress: 8/10 to LEGENDARY

Benefits Updated:
• Port Access: No change (already full access)
• Pricing: No change (25% discount maintained)
• Missions: Elite missions remain available
```

```
🔴 REPUTATION LOST 🔴
British Navy: -20
Reason: Sank HMS Destroyer (unprovoked attack)
New Reputation: FRIENDLY (+38/100)
Dropped from REVERED tier

Consequences:
• Port Access: Lost access to 3 military bases
• Pricing: Discount reduced from 15% to 5%
• Missions: Advanced missions no longer available
• Warning: Allied with US (-10 reputation pending)
```

---

## Anti-Exploitation Measures

### Reputation Farming Prevention

**Diminishing Returns**:
```
Same Activity Repeated:
First Instance: Full reputation gain
2nd-5th Instance: 75% reputation gain
6th-10th Instance: 50% reputation gain
11th+ Instance: 25% reputation gain

Resets: Weekly reset on Sunday server time

Example: Farming pirate destroyers
1st Pirate: +3 reputation
5th Pirate: +2.25 reputation
10th Pirate: +1.5 reputation
20th Pirate: +0.75 reputation
```

**Mission Cooldowns**:
```
Same Mission Type:
- Cannot repeat same mission twice in 6 hours
- Mission reputation reward: First completion only
- Subsequent completions: Credit rewards only

Example: Patrol Mission
- First completion: +2 reputation + 1,500 credits
- Second completion (same day): 1,500 credits only
- Next day: Reputation reward available again
```

**Multi-Accounting Detection**:
```
System monitors:
- IP addresses (multiple accounts same IP flagged)
- Suspicious trading patterns (funneling reputation)
- Coordinated actions (obvious alt account cooperation)

Penalties:
- Account suspension
- Reputation reset to 0
- Potential permanent ban
```

---

## Related Documents

- **[Nation-Overview.md](Nation-Overview.md)** - Nation characteristics and starting reputations
- **[Diplomacy-States.md](Diplomacy-States.md)** - How reputation affects diplomatic relationships
- **[Economy-Overview.md](../07-Economy/Economy-Overview.md)** - Economic impact of reputation
- **[Mission-System.md](../05-Mission-System/Mission-Overview.md)** - Missions affected by reputation

---

## Design Notes

### Key Design Principles
1. **Meaningful Consequences**: Reputation affects gameplay in tangible ways (access, pricing, missions)
2. **Player Agency**: Actions have clear and predictable reputation impact
3. **Recovery Possible**: Even severe reputation damage can be recovered (with effort)
4. **Risk vs Reward**: Players can choose to sacrifice reputation for tactical advantage
5. **Anti-Exploitation**: Systems prevent reputation farming and gaming

### Future Enhancements
- Reputation leaderboards (most honored, most notorious)
- Special titles and cosmetics for reputation milestones
- Reputation-based events (hero missions for LEGENDARY players)
- Dynamic reputation quests (custom recovery paths based on player history)
- Faction-specific reputation benefits (unique rewards per nation)
