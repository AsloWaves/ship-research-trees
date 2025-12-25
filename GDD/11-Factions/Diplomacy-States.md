# Diplomacy States

**Status**: 📋 PLANNED (Phase 3 feature)
**Tags**: [planned, phase3, faction-system, diplomacy, pvpve]
**Priority**: MEDIUM (Phase 3 focus)
**Last Updated**: 2025-11-17

---

## Vision Statement

Dynamic international relations system where nation diplomatic states shift based on server-wide player actions, creating authentic WWII-era tensions with PvPvE mechanics that allow attacking peaceful nations with severe reputation penalties, enabling player-driven political warfare.

---

## Core Diplomatic States

### Three Primary States

**PEACE** (Friendly Relations):
- Nations cooperate and support each other
- Joint operations and shared intelligence
- Economic benefits and trade agreements
- Military coordination against common enemies

**NEUTRAL** (Coexistence):
- Nations tolerate each other without alliance
- Limited cooperation on mutual interests
- Independent operations and no military coordination
- Commercial relations maintained

**WAR** (Active Conflict):
- Nations in open military hostility
- Combat operations actively encouraged
- Economic warfare and blockades
- No diplomatic immunity or protection

---

## Diplomatic State Characteristics

### PEACE State

**Definition**: Allied nations working together against common enemies

**Military Coordination**:
- **Joint Operations**: Multi-nation fleet task forces
- **Shared Intelligence**: Real-time enemy position sharing
- **Mutual Defense**: Automatic cooperation when allied ship attacked
- **Combined Planning**: Coordinated strategic campaigns

**Economic Integration**:
- **Trade Bonuses**: +20% profit on trades between allied ports
- **Resource Sharing**: Preferential pricing on strategic materials
- **Technology Exchange**: Access to allied nation technology (limited)
- **Joint Production**: Cooperative factory operations

**Political Benefits**:
- **Diplomatic Immunity**: Cannot be attacked by allied NPCs
- **Port Access**: Unrestricted access to allied ports
- **Reputation Synergy**: Gain reputation with allies when helping each other
- **Alliance Missions**: Special cooperative missions available

**Example: USA-UK Alliance (PEACE)**:
```
Military Benefits:
- US carriers can operate from British ports
- British destroyers can join US task forces
- Shared radar detection networks
- Combined anti-submarine operations

Economic Benefits:
- US electronics 20% cheaper in British ports
- British fire control systems discounted for US players
- Joint production facilities in allied territories
- Resource sharing during shortages

Political Benefits:
- US players have full access to British military bases
- British players receive US intelligence on Japanese fleet movements
- Reputation gains with one benefit the other (+5 US = +2 UK)
- Joint campaign missions against Germany/Japan

Player Experience:
- Can coordinate large multi-nation fleets (50+ ships)
- Economic stability through allied trade networks
- Strategic depth through combined arms operations
```

**Attacking Allied Ships** (PvPvE freedom with consequences):
```
Despite being at PEACE, players CAN attack allied ships

Immediate Consequences:
- Victim Nation: -20 reputation per ship (betrayal)
- Your Nation: -10 reputation per ship (dishonor)
- Victim's Allies: -10 reputation (attack on friend)

Example: US Player attacks British Destroyer during PEACE
- British Navy: -20 reputation (treachery)
- US Navy: -10 reputation (attacking ally, dishonorable)
- German Navy: +5 reputation (damaged enemy alliance)

Strategic Considerations:
- May be worth it for high-value targets (capturing rare cargo)
- Risk starting diplomatic incident (could trigger alliance breakdown)
- Reputation recovery is expensive and time-consuming
- May be hunted by both US and British players afterward

Design Intent:
- Freedom to attack anyone (PvPvE philosophy)
- Severe consequences prevent casual griefing
- Strategic warfare option for dedicated players
- Enables espionage and false-flag operations
```

---

### NEUTRAL State

**Definition**: Nations with no formal alliance or hostility

**Military Independence**:
- **No Coordination**: Each nation operates independently
- **Self-Defense Only**: Will defend if attacked, but no proactive cooperation
- **Information Silos**: No intelligence sharing
- **Territorial Respect**: Passage allowed through territorial waters (usually)

**Commercial Relations**:
- **Standard Pricing**: No trade bonuses or penalties
- **Open Markets**: Commercial goods freely traded
- **No Restrictions**: Military equipment sales allowed (reputation permitting)
- **Neutral Ports**: Provide sanctuary for all nations

**Political Neutrality**:
- **No Alliance Obligations**: Won't intervene in conflicts involving neutral nations
- **Diplomatic Freedom**: Can negotiate with any nation independently
- **Conflict Avoidance**: Prefers to stay out of wars
- **Economic Focus**: Emphasis on trade and commerce over military action

**Example: USA-Germany at NEUTRAL**:
```
Military Status:
- US and German ships can encounter without automatic hostility
- No NPC attacks unless provoked
- Can pass through same waters without incident
- Neither helps nor hinders the other

Economic Relations:
- US players can purchase German equipment (if reputation allows)
- German players can trade in US ports (if reputation allows)
- Standard market pricing applies
- No trade restrictions beyond reputation gates

Political Status:
- US players won't gain/lose reputation for German actions
- Independent diplomatic channels
- Can negotiate individual trade deals
- Neutral states may become mediators in disputes

Player Experience:
- Can operate in same regions without automatic conflict
- Economic opportunities through neutral trade
- Political flexibility to shift alliances
- Potential for future alliance or war
```

**Attacking Neutral Ships**:
```
Players CAN attack neutral nation ships

Moderate Consequences:
- Victim Nation: -15 reputation per ship
- Your Nation: -5 reputation (poor conduct)
- International Community: -2 reputation (all other nations)

Example: US Player attacks German Cruiser during NEUTRAL
- German Navy: -15 reputation (unprovoked attack)
- US Navy: -5 reputation (dishonorable conduct)
- British Navy: -2 reputation (destabilizing action)
- Japanese Navy: -2 reputation (international concern)

Strategic Considerations:
- Lower penalty than attacking allies (easier to recover)
- May be strategic (denying enemy resources)
- Risk of triggering war between nations
- Economic warfare viable option

Design Intent:
- Gray area between peace and war
- Allows opportunistic attacks with manageable consequences
- Creates tension and uncertainty
- Enables strategic targeting without full war commitment
```

---

### WAR State

**Definition**: Open military hostilities between nations

**Active Combat**:
- **Kill-on-Sight**: NPC forces actively attack enemy players
- **No Quarter**: Combat encouraged and rewarded
- **Territory Denial**: Enemy players denied access to national waters
- **Strategic Objectives**: Capture ports, sink fleets, control resources

**Economic Warfare**:
- **Trade Embargos**: Cannot trade with enemy nation ports
- **Blockades**: Military operations to cut off enemy supply lines
- **Resource Denial**: Target enemy industrial capacity
- **Price Warfare**: Economic manipulation to damage enemy economy

**Total War Mechanics**:
- **Reputation Rewards**: Killing enemy ships grants reputation (no penalty)
- **War Bonds**: Economic incentives to support war effort
- **Strategic Campaigns**: Large-scale multi-week operations
- **Victory Conditions**: War ends when objectives met or negotiated peace

**Example: USA-Japan at WAR**:
```
Military Operations:
- US and Japanese ships engage on sight
- NPC patrols actively hunt enemy players
- Port access completely denied to enemies
- All combat actions rewarded with reputation

Strategic Campaigns:
- US Pacific Campaign: Capture Japanese-held islands
- Japanese Defense: Protect resource-rich territories
- Submarine Warfare: Economic attacks on shipping
- Carrier Battles: Large fleet engagements for territorial control

Economic Impact:
- Japanese oil prices spike (US blockade)
- US electronics scarce in Pacific (Japanese attacks on convoys)
- Black market thrives (smuggling through neutral ports)
- Resource scarcity drives innovation and adaptation

Player Experience:
- Constant combat opportunities (high-intensity gameplay)
- Clear objectives and victory conditions
- Economic warfare as important as military combat
- Large-scale coordinated operations
- Risk of permanent territorial losses

War Duration:
- Minimum 2 weeks (prevents rapid flip-flopping)
- Ends when: Victory conditions met, negotiated peace, or mutual exhaustion
- Post-war cooldown: 1 week before can declare war again
```

**Attacking Enemy Ships (at WAR)**:
```
Full Rewards, No Penalties:

Reputation Gains:
- Your Nation: +5 to +25 reputation (based on ship class)
- Allied Nations: +2 to +5 reputation
- Enemy Nation: -10 to -30 reputation (expected in war)
- Neutral Nations: 0 reputation (understood wartime action)

Example: US Player sinks IJN Battleship during WAR
- US Navy: +15 reputation (major victory)
- British Navy: +5 reputation (allied with US)
- Japanese Navy: -25 reputation (enemy loss)
- German Navy: 0 reputation (not involved in Pacific war)

Additional Rewards:
- Combat pay: 50,000 credits (battleship)
- Salvage rights: 15,000 credits (scrap value)
- War bonds: +10 US Industrial Points
- Recognition: Server-wide announcement for legendary kills

Design Intent:
- War is profitable and rewarding
- Incentivizes participation in national conflicts
- No moral ambiguity (clear enemies)
- Drives server-wide engagement
```

---

## Diplomatic State Transitions

### Peace → War (Declaration of War)

**Trigger Conditions**:

**Automatic War Declaration** (Server-driven event):
```
Condition: 100+ enemy ships sunk in 7-day period
- Server counts cumulative attacks on peaceful/neutral nation
- Threshold reached: Diplomatic incident escalates to war
- Announcement: 24-hour warning before war begins
- Preparation: Players mobilize fleets, stockpile resources

Example: US players sink 120 Japanese ships over 1 week
- Day 7: Threshold reached (100 ships)
- Server Announcement: "Tensions escalate, war imminent"
- Day 8: WAR declared between USA and Japan
- All diplomatic consequences trigger immediately
```

**Player-Driven War Vote**:
```
Mechanism: Players petition their nation for war declaration
- Petition Start: 100 players sign petition
- Voting Period: 7 days for all eligible players to vote
- Vote Requirement: 60% of active players must vote YES
- Declaration: If passed, war begins in 24 hours

Example: US Players want war with Germany
- Week 1: 150 US players sign petition for war with Germany
- Week 2: All US players vote (YES: 65%, NO: 35%)
- Week 3: War declared, 24-hour preparation period
- Week 3 + 1 day: Active warfare begins

Prevents:
- Small groups declaring war arbitrarily
- Griefing through unwanted wars
- Ensures server-wide consensus
```

**Diplomatic Incident Escalation**:
```
Severe Provocation Examples:
- Attack on diplomatic vessel (instant war)
- Unprovoked attack on major fleet (50+ ships)
- Assassination of nation leader NPC
- Sabotage of critical industrial facility

Incident Investigation:
- 48-hour investigation period
- GMs review circumstances
- Determine if intentional or accidental
- Punishment or war declaration

Example: German submarines sink US diplomatic convoy
- Investigation: Intentional attack confirmed
- Diplomatic Options: Reparations or war
- Germany refuses reparations
- Result: War declared within 72 hours
```

### War → Peace (Negotiated Settlement)

**Peace Negotiation Process**:

**Stage 1: Ceasefire Proposal** (Day 1-7):
```
Either Nation Can Propose:
- Must have been at war minimum 14 days
- Proposal submitted to opposing nation leadership (GMs/Vote)
- Terms negotiated:
  - Territory exchanges
  - Reparations (credits or resources)
  - Prisoner exchanges
  - Technology transfers

Example: USA proposes ceasefire with Japan
- War Duration: 45 days
- US Terms: Japan cedes 3 Pacific islands + 500,000 credits
- Japanese Terms: US withdraws blockade + technology exchange
- Negotiation: 7 days of back-and-forth
```

**Stage 2: Player Vote** (Day 8-14):
```
Both Nations Vote on Peace Terms:
- All active players can vote
- Requires 50% approval from BOTH sides
- If approved: Peace treaty signed
- If rejected: War continues

Example: US-Japan peace vote
- US Players: 58% vote YES (approve peace)
- Japanese Players: 52% vote YES (approve peace)
- Result: Peace treaty ratified
- Implementation: 24-hour transition period
```

**Stage 3: Implementation** (Day 15-21):
```
Peace Treaty Takes Effect:
- Territory transfers occur (ports change hands)
- Reparations paid (credits transferred)
- Trade routes reopen
- Diplomatic relations reset to NEUTRAL
- 30-day cooldown before war can be re-declared

Example: US-Japan treaty implementation
- 3 Pacific islands transfer to US control
- Japan pays 500,000 credits to USA
- US Naval blockade ends
- Trade resumes at neutral pricing
- Relations reset to NEUTRAL (0 reputation baseline)
```

**Unconditional Surrender** (Alternative):
```
Victory Condition Met:
- Control 80% of enemy territory
- Sink 75% of enemy fleet
- Control all enemy industrial ports

Immediate Effects:
- War ends immediately
- Winner dictates all terms
- Loser suffers severe consequences
- Long-term strategic implications

Example: USA achieves victory over Japan
- US controls 85% of Pacific territories
- Japanese fleet reduced to 20% strength
- US Dictates Terms:
  - All remaining Japanese territory ceded
  - Massive reparations (2,000,000 credits)
  - Technology transfer (all Japanese research)
  - Japanese players can defect to US (no penalty for 30 days)

Consequences:
- Japan severely weakened for 60 days (recovery period)
- US dominant in Pacific theater
- Potential for Japan resurgence if players rebuild
- Server power balance dramatically shifted
```

---

## PvPvE Mechanics (Core Design Philosophy)

### "Attack Anyone, Anywhere, Anytime"

**Fundamental Rule**: No safe zones except immediate port waters (500m radius)

**Universal PvP Freedom**:
- Can attack any player regardless of nation or diplomatic state
- No mechanically enforced restrictions
- Consequences are reputation and diplomatic, not mechanical
- Enables full political and military sandbox gameplay

**Risk vs Reward Framework**:

**Low Risk, Low Reward** (Attacking enemy at war):
```
Target: Japanese destroyer (USA-Japan at WAR)
Risk: None (legal combat)
Reward: +5 reputation, 3,500 credits, salvage
Consequences: None negative

Strategic Value: Safe reputation gains
```

**Medium Risk, Medium Reward** (Attacking neutral):
```
Target: German cruiser carrying valuable cargo (USA-Germany NEUTRAL)
Risk: -15 German rep, -5 US rep, -2 international
Reward: 15,000 credit cargo, ship salvage
Consequences: Reputation loss, potential war incident

Strategic Value: Profitable if cargo worth > reputation cost
```

**High Risk, High Reward** (Attacking ally):
```
Target: British battleship with experimental radar (USA-UK PEACE)
Risk: -20 British rep, -10 US rep, -10 international, potential bounty
Reward: 50,000 credit radar (normally unobtainable), prestige
Consequences: Severe reputation loss, hunted by both nations, potential diplomatic crisis

Strategic Value: Rare technology acquisition, intelligence value
Decision: Only for players who calculated risk worth reward
```

**Extreme Risk, Extreme Reward** (Attacking national hero):
```
Target: LEGENDARY reputation US carrier (by US player)
Risk: -100 US rep (instant NEMESIS), permanent bounty, possible ban
Reward: None (treason, no strategic value)
Consequences: Character essentially unplayable, hunted by entire server

Strategic Value: None (griefing, not viable strategy)
Design Protection: Extreme penalties prevent this behavior
```

---

## Diplomatic Incident System

### Incident Severity Levels

**Minor Incident** (Single player action, limited impact):
```
Examples:
- Single friendly fire incident (accident)
- Trade dispute (contract breach)
- Navigation conflict (territorial water violation)

Resolution:
- Automatic: Reputation penalty only (-2 to -5)
- No escalation unless repeated
- Diplomatic note sent (warning)

Example: US destroyer accidentally damages British cruiser
- British Navy: -2 reputation (accident forgiven)
- US Navy: -1 reputation (carelessness)
- No further consequences if isolated incident
```

**Moderate Incident** (Multiple players, notable impact):
```
Examples:
- Repeated attacks on allied shipping (3-5 ships)
- Espionage discovered and confirmed
- Sabotage of allied facility

Resolution:
- Investigation: 48-hour GM review
- Diplomatic pressure: Victim nation demands action
- Penalties: -15 reputation, possible temporary sanctions
- Escalation risk: If not addressed, becomes major

Example: German players caught spying in US naval base
- Investigation confirms espionage
- German Navy: -30 reputation (caught red-handed)
- US Navy: Demands reparations or expulsion
- Resolution: Germany pays 100,000 credits, players receive -50 rep penalty
```

**Major Incident** (Nation-level consequences):
```
Examples:
- Unprovoked attack on major fleet (10+ ships)
- Assassination of important NPC
- Large-scale economic warfare
- Breaking major treaty

Resolution:
- International Crisis: 7-day negotiation period
- Potential War: May trigger automatic war declaration
- Severe Penalties: -50 to -100 reputation, bounties, sanctions
- Alliance Strain: Allied nations may distance themselves

Example: Japanese surprise attack on US task force (peacetime)
- 15 US ships sunk
- Major Incident declared
- Negotiations:
  - US demands: 1,000,000 credit reparations or war
  - Japan offers: 500,000 credits + territory concession
  - US accepts: Peace maintained, Japan penalized
  - Alternative: US rejects, triggers war declaration

Consequences:
- Japanese players involved: -75 US reputation (ABHORRED)
- Japanese nation: -30 international reputation
- Alliance strain: UK-Japan relations deteriorate
```

---

## Alliance Systems

### Formal Military Alliances

**Alliance Structure**:

**Major Historical Alliances** (Server default):
```
Allies:
- United States
- United Kingdom
- (Other Allied nations as NPCs)

Axis:
- Germany
- Japan (conditional alliance)
- (Other Axis nations as NPCs)

Default Relations:
- Allied nations: PEACE with each other, WAR with Axis
- Axis nations: PEACE with each other, WAR with Allies
- Can shift based on player actions and diplomatic events
```

**Player-Driven Alliance Shifts**:
```
Mechanism: Nation can vote to leave/join alliance
- Petition: 150 players sign petition
- Vote: 7-day voting period
- Requirement: 70% approval (high threshold for major change)
- Implementation: 14-day transition period

Example: Japan votes to leave Axis, join Allies
- Petition: 200 Japanese players sign
- Vote: 72% approval
- Transition:
  - Week 1-2: Ceasefire with Allies
  - Week 3-4: Peace treaty negotiations
  - Week 5: Full alliance membership
  - Consequences: Germany-Japan relations become HOSTILE

Impact:
- Reshapes entire server power balance
- Historical "what-if" scenarios possible
- Enables dynamic political gameplay
- Requires broad player consensus (prevents trolling)
```

**Alliance Benefits**:

**Military Coordination**:
- +15% effectiveness when fighting alongside allied forces
- Shared victory conditions in campaigns
- Combined arms bonuses (carriers + destroyers, etc.)
- Joint base access and logistics

**Economic Integration**:
- 20% trade bonus between allied ports
- Technology sharing (limited access to allied tech trees)
- Resource pooling during shortages
- Joint production facilities

**Strategic Intelligence**:
- Real-time enemy position sharing
- Coordinated reconnaissance
- Shared codebreaking and intelligence
- Joint strategic planning

---

## Neutral Nations & Safe Havens

### Third-Party Nations (NPC Controlled)

**Major Neutral Powers**:

**Portugal** (Atlantic Neutral Hub):
```
Characteristics:
- Permanently neutral (will not join wars)
- Lisbon as major trading hub
- All nations have access (if reputation allows)
- No military operations allowed in territorial waters

Benefits:
- Safe haven during conflicts
- International trading opportunities
- Black market access
- Diplomatic meeting ground

Enforcement:
- Powerful Portuguese navy prevents combat
- Violators instantly gain -75 Portuguese reputation
- Banned from all Portuguese ports (permanent)
```

**Sweden** (European Neutral):
```
Characteristics:
- Northern European neutral power
- Trades with both Allies and Axis
- Advanced technology available
- Espionage hub (information trading)

Benefits:
- Technology from both sides available
- Safe port in Baltic Sea
- Information marketplace
- Neutral meeting ground
```

**Argentina** (South American Neutral):
```
Characteristics:
- Southern hemisphere safe zone
- Remote from major conflicts
- Supplies both sides
- Potential pirate haven

Benefits:
- Safe harbor far from war zones
- Profitable trade routes
- Low-security environment (smuggling)
```

---

## Diplomatic Victory Conditions

### Long-Term Strategic Goals

**Alliance Victory** (Conditional, server-wide):
```
Victory Conditions:
- Control 70% of strategic territories
- Reduce enemy fleet to 25% strength
- Maintain control for 30 consecutive days

Rewards:
- Massive reputation bonus (+50 all allied nations)
- Economic windfall (500,000 credits per player)
- Unique titles and cosmetics
- 60-day "golden age" economic bonuses

Example: Allies achieve victory over Axis
- Control Pacific and Atlantic theaters
- German/Japanese fleets decimated
- 30-day dominance maintained
- Victory declared, rewards distributed

Post-Victory:
- 60-day recovery period (Axis rebuild)
- Potential for Axis resurgence if players commit
- Server enters "Cold War" phase (tense peace)
- New conflicts emerge from victory spoils
```

---

## Related Documents

- **[Nation-Overview.md](Nation-Overview.md)** - Nation characteristics and relationships
- **[Reputation-System.md](Reputation-System.md)** - How reputation affects diplomatic relations
- **[PvP-Systems.md](../04-Player-Combat/PvP-Overview.md)** - PvPvE combat mechanics
- **[Mission-System.md](../05-Mission-System/Mission-Overview.md)** - Diplomatic missions

---

## Design Notes

### Key Design Principles

1. **Player Freedom**: Can attack anyone, anywhere, anytime (true PvPvE)
2. **Meaningful Consequences**: Diplomatic penalties make choices matter
3. **Dynamic Politics**: Server-wide player actions shape international relations
4. **Historical Authenticity**: WWII-era alliances and tensions
5. **Strategic Depth**: Diplomacy as important as military power

### PvPvE Philosophy

**Why Allow Attacking Allies?**
- **Player Agency**: Maximum freedom in tactical and strategic choices
- **Emergent Gameplay**: Enables espionage, false flags, betrayals
- **Consequence System**: Penalties severe enough to prevent casual griefing
- **Strategic Warfare**: High-value targets may be worth reputation loss
- **Political Intrigue**: Creates authentic wartime paranoia and tension

**Griefing Prevention**:
- Severe reputation penalties for attacking allies (-20 per ship)
- Economic costs (miss out on discounts, pay higher prices)
- Social consequences (hunted by both nations)
- Potential bounties and player retaliation
- GM oversight for systematic griefing

**Design Goal**: Freedom with consequences, not freedom without consequences

### Future Enhancements

- Player-elected nation leaders (diplomatic authority)
- Custom alliance creation (beyond historical alliances)
- Diplomatic missions and espionage gameplay
- Treaty negotiation interface (player-driven terms)
- Diplomatic victory paths (non-military win conditions)
- Historical event system (Pearl Harbor-style server events)
- Cold War mechanics (post-victory tension systems)
