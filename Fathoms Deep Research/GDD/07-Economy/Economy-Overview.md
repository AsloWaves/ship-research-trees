# Economy Overview

**Status**: 📋 PLANNED (Phase 3 feature)
**Tags**: [planned, phase3, economy-system]
**Priority**: MEDIUM (Phase 3 focus)
**Last Updated**: 2025-11-17

---

## Vision Statement

Dynamic economic warfare system where resource control, trade route dominance, and market manipulation directly impact extraction mission success, creating wealth disparities that influence combat effectiveness and strategic power projection.

## Core Economic Philosophy

The Fathoms Deep economy is built on **extraction-based resource cycling**:

1. **Extraction**: Players earn resources through combat operations, salvage, and mission rewards
2. **Transportation**: Resources must be returned to port to have value
3. **Processing**: Raw materials converted into usable equipment and supplies
4. **Consumption**: Resources consumed in combat operations, creating continuous demand
5. **Cycling**: The loop restarts, driving player engagement and economic activity

### Key Design Principles

- **No Free Money**: All currency must originate from player actions or NPC economic simulation
- **Risk vs Reward**: Greater risk (longer voyages, combat zones) yields higher profits
- **Player Agency**: Market prices influenced by player supply/demand dynamics
- **Strategic Depth**: Economic warfare as viable as military conquest
- **Extraction Dependency**: All wealth must return to port to be realized

---

## Multi-Tier Currency System

### Primary Currencies

#### Credits (Universal Currency)
**Core Function**: Standard transactions, basic equipment, routine services

**Acquisition Sources**:
- Combat pay from successful engagements
- Mission rewards (500-5,000 credits typical)
- Trading operations between ports
- Salvage recovery operations
- NPC contract completions

**Purchasing Power**:
- Basic modules: 500-5,000 credits
- Standard ammunition: 10-100 credits per unit
- Crew recruitment: 200-2,000 credits per specialist
- Ship purchases: 15,000-500,000 credits depending on tier
  - Example: Fletcher-class destroyer costs 45,000 credits
  - Example: Basic 5-inch turret costs 1,200 credits

**Economic Characteristics**:
- Relatively stable with minor fluctuations
- Influenced by server-wide economic activity
- Primary currency for 80% of transactions
- Accepted universally across all nations

#### Resource Points (Strategic Materials)
**Nation-Specific Types**:
- **US Industrial Points**: Mass production, standardization, industrial equipment
- **British Engineering Points**: Precision systems, radar technology, fire control
- **German Technical Points**: Advanced engineering, submarine tech, experimental systems
- **Japanese Innovation Points**: Carrier aviation, precision metallurgy, advanced torpedoes

**Function**: High-tier equipment, nation-specific technology, premium services

**Acquisition**:
- Faction-specific missions (10-50 points per mission)
- Territorial control bonuses (passive generation)
- Diplomatic achievements and treaties
- Major campaign participation rewards

**Strategic Value**:
- Gates access to each nation's specialized technology
- Cannot be traded between players (account-bound)
- Represents political capital and national loyalty
- Required for progression in nation-specific tech trees

**Usage Example**:
- German Advanced Radar requires 150 German Technical Points + 8,000 credits
- US Carrier aircraft requires 75 US Industrial Points + 12,000 credits

#### Reputation Currency (Political Capital)
**Function**: Invisible currency affecting all economic interactions

**Pricing Influence**:
- **Friendly** (+50 reputation or higher): 15-25% discount on equipment and services
- **Neutral** (-25 to +49 reputation): Standard market pricing
- **Hostile** (-50 to -26 reputation): 30-50% price markup
- **Enemy** (-51 or lower): Access denied or 100%+ markup

**Access Control**:
- Certain equipment/services locked behind reputation thresholds
- Advanced technology requires +75 reputation minimum
- Elite crew recruitment requires +60 reputation
- Restricted port access based on diplomatic standing

**Dynamic Changes**:
- Fluctuates based on combat actions and political choices
- Can be regained through missions and diplomatic actions
- Lost rapidly through hostile actions (-10 per enemy ship sunk)
- Builds slowly through positive interactions (+2-5 per mission)

**Usage Example**:
- Advanced US carrier aircraft require 75+ US Navy reputation + 25 US Industrial Points + 15,000 credits

---

### Specialized Economic Tokens

#### Black Market Tokens (Contraband Currency)
**Acquisition**:
- Illegal piracy operations
- Underground smuggling networks
- Trading with pirate faction
- Captured contraband from enemy ships

**Function**:
- Restricted technology unavailable through legal channels
- Experimental equipment from all nations
- Information brokering and espionage services
- Stolen prototype systems

**Risk Factor**:
- Possession carries reputation penalties if detected by lawful factions (-20 reputation if discovered)
- Trading generates suspicion from national authorities
- Can trigger random inspections at friendly ports
- High reward balances high risk

**Unique Access**:
- Captured enemy technology without reputation requirements
- Cross-nation equipment combinations normally impossible
- Intelligence on enemy fleet movements and plans
- Experimental systems before official release

**Usage Example**:
- Captured German radar technology: 25 Black Market Tokens
- Japanese Long Lance torpedoes (for non-Japanese player): 40 Black Market Tokens

#### Intelligence Credits (Information Currency)
**Function**: Strategic information, enemy ship locations, fleet movement data

**Market Value**:
- Time-sensitive: Value decreases rapidly (50% per hour)
- Relevance-based: Major fleet movements worth 500-2,000 credits
- Verification: Confirmed intelligence worth 3x unverified tips

**Source**:
- Espionage missions and reconnaissance
- Intercepted communications and code-breaking
- Scout plane observation rewards
- NPC informant networks

**Strategic Application**:
- Plan ambushes using enemy position data
- Avoid superior forces through early warning
- Identify high-value targets for extraction missions
- Counter enemy economic operations

**Usage Example**:
- Enemy battleship location and course: 500 Intelligence Credits
- Fleet movement schedule for next 6 hours: 1,200 Intelligence Credits
- Location of unguarded convoy route: 800 Intelligence Credits

---

## Economic Driver Analysis

### Player-Generated Market Pressure

**Supply & Demand Mechanics**:
- **Active Player Base**: 300+ simultaneous players create constant resource demand
- **Consumption Rates**: Combat operations consume 5-15% of server resources daily
- **Production Capacity**: Player industrial capacity must scale with server population
- **Price Elasticity**:
  - Basic goods (steel, oil) remain stable (±10% variance)
  - Premium equipment highly volatile (50-200% variance)
  - Technology items subject to sudden demand spikes

**Market Manipulation Strategies**:
- **Resource Hoarding**: Large corporations stockpile materials before conflicts
  - Can create artificial scarcity, driving prices up 200-400%
  - Counter: NPC nations increase production to stabilize markets
- **Price Fixing**: Cartels coordinate pricing to maximize profits
  - Requires 40%+ market share for effectiveness
  - Risk: Government intervention and reputation penalties
- **Supply Chain Disruption**: Military operations targeting competitor trade routes
  - Economic warfare more profitable than direct combat
  - Strategic impact: Eliminate competition while generating salvage
- **Economic Intelligence**: Gathering information on competitor activities
  - Predict market movements before they occur
  - Position for profit during anticipated conflicts

### AI Nation Economic Simulation

**Realistic Economic Cycles**:
- **Production Capacity**: AI nations produce resources based on controlled territory
  - Industrial ports generate 1,000-5,000 units of strategic resources daily
  - Territory loss directly impacts AI production capacity
  - Players can observe and exploit AI supply chain vulnerabilities

**War Economy Transitions**:
- **Peacetime**: Civilian production (60%) and military production (40%)
- **Wartime**: Shift to 80% military production, consumer goods scarcity
- **Economic Effects**:
  - Civilian goods prices increase 150-300% during war
  - Military equipment becomes more available but lower quality
  - Black market activity increases dramatically

**Trade Route Protection**:
- AI dedicates military resources (15-30% of fleet) to protecting valuable trade routes
- Players can identify and attack poorly defended convoys
- AI adapts: Increases escorts on frequently attacked routes
- Dynamic security creates evolving tactical opportunities

**Economic Recovery**:
- Post-war rebuilding creates temporary resource shortages
- Prices spike 200-400% for construction materials
- Opportunities for traders to profit from scarcity
- Recovery period: 2-4 weeks (in-game time) depending on damage

---

## Resource Categories & Strategic Applications

### Strategic Raw Materials

#### Steel (Foundation Material)
**Production Sources**:
- Controlled industrial ports (passive generation)
- Mining operations in resource zones
- Salvage recovery from destroyed ships
- Trade agreements with NPC nations

**Consumption Applications**:
- **Ship Hulls**:
  - Destroyer: 500 units
  - Cruiser: 1,200 units
  - Battleship: 3,000 units
  - Carrier: 2,500 units
- **Module Construction**:
  - Turrets: 50-200 units depending on caliber
  - Engines: 100-500 units depending on power
  - Armor plating: 25-150 units per section
- **Ammunition**:
  - AP shells: 2 units each
  - HE shells: 1.5 units each
  - Special ammunition: 3-5 units each

**Market Dynamics**:
- Stable baseline demand (±10% variance)
- Spikes during major wars (50-100% price increase)
- Most traded commodity by volume
- Regional availability affects local pricing

**Quality Grades**:
- **Standard Steel**: Baseline performance, widely available
- **Premium Alloys**: 30% performance improvement, 100% price increase
- **Specialized Steel**: Nation-specific formulations with unique bonuses

#### Oil (Energy & Mobility)
**Strategic Value**: Controls operational tempo and strategic mobility

**Consumption Rates**:
- **Ship Operations**: 2-8 units per hour based on:
  - Ship class (destroyers use 2/hr, battleships use 8/hr)
  - Speed setting (cruising vs combat speed)
  - Combat intensity (combat operations use 150% normal rate)
- **Aircraft Operations**: 5-15 units per flight hour
  - Fighters: 5 units/hour
  - Bombers: 10 units/hour
  - Reconnaissance: 7 units/hour
- **Industrial Production**: 10-25 units per production cycle
  - Factories require constant energy supply
  - Production halts if oil supply interrupted

**Supply Chain Vulnerability**:
- Oil tankers are high-value targets for economic warfare
- Single tanker loss can impact faction-wide operations
- Convoy protection critical for maintaining supply lines
- Strategic bombing of oil facilities cripples production

**Regional Availability**:
- **Oil-Rich Regions**: Middle East, Dutch East Indies, Texas
  - 30-50% lower prices
  - High strategic value for territorial control
- **Oil-Poor Regions**: Europe, Japan, Most Islands
  - Import dependent, vulnerable to blockade
  - 50-100% price premium

#### Electronics (Technology Multiplier)
**Advanced Systems**:
- Radar systems (detection and fire control)
- Fire control computers (accuracy enhancement)
- Communications equipment (coordination capability)
- Electronic warfare systems (jamming and deception)

**Scarcity Factor**:
- Most limited resource in game economy
- Highest value-to-weight ratio
- Production requires specialized facilities (distributed across all 4 nations)
- Each nation has electronics production capacity with unique specializations (no single nation monopoly)

**Production Complexity**:
- Requires specialized facilities and skilled technicians
- Production time: 24-48 hours per unit
- Failure rate: 10-15% during manufacturing
- Cannot be mass-produced like other resources

**Combat Acquisition**:
- Capturing intact electronic systems provides significant advantage
- Enemy electronics can be reverse-engineered (requires 5-10 units)
- Salvaged electronics have 50-80% functionality
- High incentive for precision strikes preserving electronics

**Technological Edge**:
- Nations with electronics advantage dominate advanced warfare
- Radar superiority = 30% combat effectiveness increase
- Advanced fire control = 25% accuracy improvement
- Electronic warfare capability = force multiplier in fleet actions

---

## Economic Sinks and Faucets

### Economic Faucets (Money Creation)

**Combat Rewards**:
- Enemy ship destruction: 500-50,000 credits depending on class
- Mission completion: 1,000-25,000 credits
- Salvage operations: 200-10,000 credits per wreck
- Territory control: 100-1,000 credits per hour

**Production Operations**:
- Factory output sold to NPCs
- Resource extraction from controlled territories
- Crafting profit margins (10-30% typical)

**NPC Contracts**:
- Trade agreements provide guaranteed income
- Faction missions with payment guarantees
- Escort duty and protection contracts

### Economic Sinks (Money Removal)

**Operational Costs**:
- Fuel consumption: 50-500 credits per hour of operation
- Ammunition expenditure: 10-100 credits per salvo
- Repair costs: 5-25% of ship value after major damage
- Port fees: 100-500 credits per visit

**Maintenance Requirements**:
- Ship maintenance: 2% of ship value per week
- Crew salaries: 1,000-10,000 credits per month
- Module degradation repairs: 500-5,000 credits

**Transaction Fees**:
- Market trading fee: 5% of transaction value
- Auction house fee: 10% of final sale price
- Black market premium: 20-40% above legal prices
- Currency exchange fees: 2-5% when applicable

**Strategic Investments**:
- Factory construction: 50,000-200,000 credits
- Technology research: 10,000-100,000 credits
- Port upgrades: 25,000-150,000 credits

---

## Nation-Specific Economic Characteristics

### United States (Industrial Supremacy)
**Economic Profile**:
- Highest overall industrial output
- Mass production efficiency (40% cost reduction for standardized items)
- Strong electronics sector
- Reliable supply chains and bulk production

**Economic Advantages**:
- Cheapest basic equipment (20-30% below market average)
- Fastest production times (50% faster than average)
- Most stable currency (5% variance vs 15% average)
- Best logistics infrastructure

**Strategic Trade Items**:
- Liberty ships (cheap transport enabling profitable long-distance trade)
- Mass-produced ammunition (reliable quality, competitive pricing)
- Electronics and radar systems (technological advantage)
- Aircraft carriers and naval aviation systems

### United Kingdom (Precision Engineering)
**Economic Profile**:
- Quality-focused manufacturing
- Advanced fire control and radar technology
- Moderate production capacity
- Premium pricing strategy

**Economic Advantages**:
- Superior accuracy systems (25% performance bonus)
- Best radar technology (30% detection range)
- Modular design (30% faster repairs)
- Global trade network access

**Strategic Trade Items**:
- Fire control systems (accuracy enhancement)
- Radar technology (detection superiority)
- Precision-manufactured components (reliability bonus)
- Anti-submarine warfare equipment

### Japan (Innovation & Efficiency)
**Economic Profile**:
- Precision manufacturing excellence
- Resource-efficient production
- Premium quality focus
- Limited raw material availability

**Economic Advantages**:
- Superior metallurgy (15% armor effectiveness bonus)
- Best carrier aviation (40% efficiency boost)
- Resource efficiency (30% less material consumption)
- High-performance equipment

**Strategic Trade Items**:
- Advanced carrier aircraft (performance superiority)
- Long Lance torpedoes (technological advantage)
- Precision instruments (quality equipment)
- Efficient ship designs

### Germany (Engineering Excellence)
**Economic Profile**:
- Most advanced technology
- Submarine warfare specialization
- Premium pricing for superior performance
- Limited production volume

**Economic Advantages**:
- Best submarine technology (60% effectiveness bonus)
- Advanced experimental systems
- Superior engineering quality
- Breakthrough technology access

**Strategic Trade Items**:
- Type XXI submarines (revolutionary performance)
- Advanced radar and detection systems
- Experimental weapons technology
- Precision-engineered components

---

## Economic Warfare Strategies

### Resource Denial
**Supply Line Interdiction**:
- Target enemy transport ships and convoys
- Each sunk transport removes 5,000-15,000 resource units
- Economic impact exceeds direct military value
- Forces enemy to divert escorts, reducing combat strength

**Industrial Sabotage**:
- Covert operations against enemy production facilities
- Reduces enemy production capacity by 20-50%
- Requires intelligence gathering and special operations
- High risk, high reward strategic option

**Market Manipulation**:
- Coordinate large-scale buying to create artificial scarcity
- Price control through cartel formation
- Economic blockades of enemy trade routes
- Information warfare to destabilize enemy markets

### Economic Intelligence
**Information Gathering**:
- Track competitor resource movements
- Identify supply chain vulnerabilities
- Predict market movements before they occur
- Counter-intelligence to protect own operations

**Strategic Planning**:
- Position assets before conflicts begin
- Stockpile resources during peacetime for wartime profit
- Identify emerging market opportunities
- Coordinate with allies for economic dominance

---

## Port-Based Economic Hubs

### Hub Characteristics

**Industrial Ports**:
- Low raw material prices (20-40% below market)
- High finished goods demand (20-30% above market)
- Production facilities available for player use
- High traffic creates liquid markets

**Military Bases**:
- Premium prices for weapons and ammunition (30-50% above market)
- Restricted access (reputation requirements)
- Advanced technology available
- Strategic information access

**Neutral Ports**:
- Moderate pricing (market average)
- Unrestricted trading for all factions
- High transaction fees (10-15%)
- Safe haven during conflicts

**Combat Zone Ports**:
- Extreme price volatility (±100% variance)
- High risk/reward trading opportunities
- Limited services and facilities
- Valuable for strategic positioning

---

## Implementation Phases

### Phase 3A: Foundation (Months 1-2)
- Basic credit economy implementation
- Simple NPC vendor pricing
- Basic resource types (Steel, Oil, Electronics)
- Port-based trading hubs

### Phase 3B: Market Dynamics (Months 3-4)
- Supply and demand simulation
- Dynamic pricing based on player activity
- Resource Points system for nation-specific items
- Basic auction house functionality

### Phase 3C: Advanced Systems (Months 5-6)
- Black Market and Intelligence Credits
- Economic warfare mechanics
- Player factory ownership
- Advanced market manipulation tools

### Phase 3D: Polish & Balance (Month 7)
- Economic balance tuning
- Anti-exploit measures
- Player feedback integration
- Economic reporting and analytics tools

---

## Related Documents

- **[Trading-System.md](Trading-System.md)** - Player-to-player trading, auction house mechanics
- **[Market-Dynamics.md](Market-Dynamics.md)** - Supply/demand simulation, NPC pricing algorithms
- **[Nation-Overview.md](../09-Faction-System/Nation-Overview.md)** - Nation economic characteristics
- **[Reputation-System.md](../09-Faction-System/Reputation-System.md)** - Economic impact of reputation
- **[Extraction-Missions.md](../05-Mission-System/Extraction-Missions.md)** - How economy drives core gameplay loop

---

## Design Notes

### Key Insights
1. **Extraction-Based Economy**: All wealth must return to port, creating transportation risk and convoy gameplay
2. **Multi-Currency System**: Different currencies serve different purposes, creating strategic depth
3. **Player-Driven Markets**: 300+ player economy creates authentic supply/demand dynamics
4. **Economic Warfare**: Market manipulation and supply line interdiction as viable strategies
5. **Nation Identity**: Economic characteristics reinforce each nation's unique playstyle

### Open Questions
- How to balance economic power between large corporations and solo players?
- What mechanisms prevent complete market monopolization?
- How to ensure new players can enter the economy meaningfully?
- Should there be global economic events that reset market imbalances?

### Future Considerations
- Seasonal economic cycles (winter reduces oil production, summer increases naval activity)
- Economic achievement system (richest players, most profitable trades)
- Player-created contracts and insurance systems
- Dynamic economic news system showing market trends
