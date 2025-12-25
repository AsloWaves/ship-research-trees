# Market Dynamics

**Status**: 📋 PLANNED (Phase 3 feature)
**Tags**: [planned, phase3, economy-system, market-simulation]
**Priority**: MEDIUM (Phase 3 focus)
**Last Updated**: 2025-11-17

---

## Vision Statement

Sophisticated supply and demand simulation creating authentic market dynamics where player actions collectively shape prices, NPC nations respond realistically to economic conditions, and economic warfare strategies directly impact strategic outcomes.

---

## Supply and Demand Framework

### Core Mechanics

**Supply Factors**:
- **Player Production**: Factory output from player-owned facilities
- **NPC Production**: AI nation industrial capacity based on controlled territory
- **Salvage Operations**: Resources recovered from combat operations
- **Import Operations**: Cross-regional trade bringing external supply
- **Strategic Reserves**: NPC nation stockpiles released during crises

**Demand Factors**:
- **Player Consumption**: Combat operations, ship construction, ammunition expenditure
- **NPC Military Needs**: AI fleet operations and military production
- **Construction Projects**: Port upgrades, factory construction, infrastructure development
- **Export Demand**: Other regions purchasing local production
- **War Economy**: Conflict-driven surge in military material demand

### Price Determination Formula

**Base Price Calculation**:
```
Market Price = Base Value × Supply Multiplier × Demand Multiplier × Regional Modifier

Where:
- Base Value: Established cost to produce item
- Supply Multiplier: 0.5 (surplus) to 3.0 (shortage)
- Demand Multiplier: 0.5 (low demand) to 4.0 (crisis demand)
- Regional Modifier: 0.7 (local production) to 2.0 (remote import)
```

**Example: Steel Pricing**:
```
Base Steel Value: 50 credits/unit

Scenario 1: Peacetime, Industrial Port
Supply Multiplier: 0.8 (local production creates surplus)
Demand Multiplier: 1.0 (normal civilian demand)
Regional Modifier: 0.7 (produced locally)
Market Price: 50 × 0.8 × 1.0 × 0.7 = 28 credits/unit

Scenario 2: Wartime, Combat Zone Port
Supply Multiplier: 2.5 (supply lines disrupted)
Demand Multiplier: 3.5 (desperate military demand)
Regional Modifier: 1.8 (must be imported under fire)
Market Price: 50 × 2.5 × 3.5 × 1.8 = 788 credits/unit

Price Difference: 788/28 = 28× markup in crisis vs peacetime
```

---

## Supply Dynamics

### Player Production Systems

**Factory Output Simulation**:

**Steel Mill Example**:
```
Location: Controlled US industrial port
Production Cycle: 6 hours

Input Requirements:
- Iron ore: 2 units
- Coal: 1 unit
- Energy (oil): 3 units
- Labor cost: 100 credits

Output:
- Standard steel: 10 units (base quality)
- OR Premium steel: 8 units (+500 credit investment)

Market Impact:
- Each mill produces 40 units per day
- 50 active mills = 2,000 units daily supply
- Server total demand: 15,000 units daily
- Player production: 13.3% of total supply

Quality Tiers:
- Standard Steel: Base pricing (market average)
- Premium Steel: 50% price premium, 30% performance bonus
- Specialized Alloys: 100% price premium, nation-specific bonuses
```

**Production Efficiency Factors**:
- **Facility Upgrades**: +10% output per upgrade level (max 5 levels)
- **Skilled Workers**: +15% output with expert staff (+20% operating cost)
- **Regional Specialization**: +20% output producing nation-specialty items
- **Power Availability**: -50% output if insufficient oil supply
- **Security**: -30% output if port under attack or blockade

**Supply Curve Behavior**:
- **High Prices**: Incentivize new factory construction (3-week build time)
- **Low Prices**: Cause factory closures (reduce supply, stabilize prices)
- **Equilibrium**: Natural market forces balance supply/demand over 2-4 week cycles

### NPC Nation Production

**AI Economic Simulation**:

**Production Capacity Formula**:
```
Nation Daily Output = (Base Capacity × Territory Control % × Industrial Efficiency)

Base Capacity by Nation:
- USA: 10,000 units/day (highest overall production)
- UK: 6,000 units/day (quality focus, lower volume)
- Germany: 5,000 units/day (advanced tech, limited capacity)
- Japan: 4,000 units/day (efficient but resource-constrained)

Territory Control Impact:
- 100% territory: Full production capacity
- 75% territory: 85% production capacity
- 50% territory: 60% production capacity
- 25% territory: 30% production capacity

Industrial Efficiency:
- Peacetime: 100% efficiency
- Minor War: 90% efficiency (supply chain disruption)
- Major War: 75% efficiency (bombing campaigns, sabotage)
- Crisis: 50% efficiency (severe infrastructure damage)
```

**Example: US Steel Production**:
```
Base Capacity: 10,000 units steel/day
Territory Control: 95% (Pacific islands lost)
War Status: Major War (Atlantic U-boat campaign)
Industrial Efficiency: 80% (moderate disruption)

Daily Output: 10,000 × 0.95 × 0.80 = 7,600 units/day

Previous Peacetime Output: 10,000 units/day
Shortage: 2,400 units/day (24% reduction)
Price Impact: Steel prices increase 35-50%
```

**Dynamic AI Responses**:
- **Production Shifts**: AI redirects capacity to critical shortages
  - During oil shortage: Increase oil production by 30%, reduce steel by 15%
- **Emergency Reserves**: AI releases 5-10% of strategic stockpiles during crisis
- **Trade Agreements**: AI offers contracts to players at premium prices for critical materials
- **Infrastructure Repairs**: AI prioritizes restoring production facilities after attacks

### Salvage and Recovery

**Combat Salvage Operations**:

**Resource Recovery from Destroyed Ships**:
```
Destroyer Wreck:
- Steel Recovery: 200-300 units (40-60% of build cost)
- Electronics: 5-15 units (if salvaged quickly)
- Oil: 10-50 units (remaining fuel)
- Ammunition: 20-100 units (unexploded ordnance)

Battleship Wreck:
- Steel Recovery: 1,000-1,500 units
- Electronics: 50-100 units
- Oil: 100-500 units
- Ammunition: 500-2,000 units

Recovery Factors:
- Time to salvage: Faster = better condition
- Salvage skill: Higher skill = more recovery
- Weather conditions: Storms reduce recovery
- Interference: Enemy presence reduces operation time
```

**Market Impact of Major Naval Battles**:
```
Battle Scenario: 20 ships destroyed in major engagement

Immediate Supply Injection:
- Steel: 8,000 units recovered
- Electronics: 400 units recovered
- Ammunition: 5,000 units recovered

Price Impact (immediate):
- Steel prices drop 15-20% (temporary surplus)
- Electronics drop 5-10% (salvaged electronics lower quality)

Long-term Impact (7 days):
- Prices return to pre-battle levels (salvage absorbed by market)
- Replacement demand drives prices above pre-battle (ship rebuilding)

Net Effect: Short-term price drop, medium-term price spike
```

---

## Demand Dynamics

### Player Consumption Patterns

**Combat Operations Consumption**:

**Average Destroyer (6-hour patrol)**:
```
Oil Consumption: 12 units (2 units/hour)
Ammunition Expenditure: 50 units (light combat)
Repair Materials: 20 units steel (minor damage)

Cost: 12×50 + 50×15 + 20×50 = 600 + 750 + 1,000 = 2,350 credits

Revenue (if successful):
- Combat rewards: 3,500 credits
- Salvage: 1,200 credits
Net Profit: 2,350 credits (before repairs/crew costs)
```

**Fleet Operation (24-hour campaign, 10 ships)**:
```
Total Oil: 10 ships × 4 units/hour × 24 hours = 960 units
Total Ammunition: 10 ships × 200 units = 2,000 units
Total Repairs: 10 ships × 100 units steel = 1,000 units

Cost: 960×50 + 2,000×15 + 1,000×50 = 48,000 + 30,000 + 50,000 = 128,000 credits

Revenue (typical):
- Mission rewards: 80,000 credits
- Salvage: 60,000 credits
Net Loss: -11,000 credits (requires external funding/alliance support)

Strategic Value: Territory control, intelligence, enemy denial
```

**Server-Wide Daily Consumption**:
```
Active Players: 300 simultaneous
Average Play Session: 3 hours
Daily Combat Hours: 900 hours (300 players × 3 hours)

Daily Resource Drain:
- Oil: 3,600 units (4 units/hour average)
- Ammunition: 45,000 units (50 units per engagement)
- Steel: 13,500 units (15 units per engagement for repairs)

Market Impact:
- Constant baseline demand prevents price collapse
- Weekend surge (400 players) drives 30% price increase
- Major events (400+ players) can double prices temporarily
```

### Construction and Infrastructure Demand

**Ship Construction Projects**:

**Destroyer Construction**:
```
Material Requirements:
- Steel: 500 units
- Electronics: 30 units
- Oil: 50 units (construction energy)
- Labor: 5,000 credits

Build Time: 48 hours
Construction Cost: 15,000 credits (materials at market prices)

Market Impact (single construction):
- Minimal (0.03% of daily steel demand)

Market Impact (100 simultaneous constructions):
- Steel demand spike: +3,333 units (22% of daily demand)
- Price increase: 25-35%
- Duration: 48 hours (until ships complete)
```

**Battleship Construction**:
```
Material Requirements:
- Steel: 3,000 units
- Electronics: 200 units
- Oil: 300 units
- Labor: 50,000 credits

Build Time: 14 days
Construction Cost: 180,000 credits

Market Impact (10 simultaneous constructions):
- Steel demand: +2,142 units/day (14% of daily demand)
- Electronics demand: +142 units/day (71% of daily production)
- **Major price impact**: Steel +30%, Electronics +150%
- Duration: 14 days (sustained demand)
```

**Factory Construction Boom**:
```
Scenario: Economic expansion, 20 new factories being built

Material Requirements (per factory):
- Steel: 5,000 units (transported via cargo grid, see [[Inventory-System]])
- Electronics: 500 units (transported via cargo grid)
- Oil: 1,000 units (transported via cargo grid)
- Labor: 100,000 credits

Total Demand (all factories):
- Steel: 100,000 units (6.7 days of total production, requires multiple cargo shipments)
- Electronics: 10,000 units (massive shortage, cargo space constraints)
- Oil: 20,000 units (1.3 days of production, heavy cargo weight)

Market Impact:
- Steel: +100% price increase (severe shortage)
- Electronics: +300% price increase (critical shortage)
- Oil: +50% price increase (moderate shortage)

Duration: 30 days (factory build time)
Economic Strategy: Speculators buy futures before construction announcements
```

### War Economy Surge

**Peacetime vs Wartime Demand**:

**Peacetime Baseline**:
```
Daily Server Consumption:
- Oil: 3,600 units
- Steel: 13,500 units
- Ammunition: 45,000 units
- Electronics: 200 units

Price Stability: ±10% variance
Market Liquidity: High (easy to buy/sell)
Player Activity: Moderate combat, lots of trading
```

**Major War Declaration**:
```
Immediate Impact (Day 1):
- Fleet mobilization: All players preparing for combat
- Ammunition hoarding: Players stockpile 200% normal supply
- Oil demand surge: 150% increase (fleet operations)
- Electronics demand: 250% increase (radar/fire control upgrades)

Price Spikes (within 24 hours):
- Oil: +60% (scarcity from hoarding)
- Steel: +40% (ship repair demand)
- Ammunition: +120% (panic buying)
- Electronics: +200% (critical upgrades)

Market Liquidity: Low (everyone buying, few selling)
```

**Sustained Warfare (Week 2-4)**:
```
Daily Consumption (adjusted):
- Oil: 7,200 units (+100% increase)
- Steel: 27,000 units (+100% increase)
- Ammunition: 135,000 units (+200% increase)
- Electronics: 600 units (+200% increase)

Supply Response:
- Factories running 24/7 (player and NPC)
- Import operations intensify (cross-region trade)
- Salvage operations increase (recovering from battles)
- NPC nations release strategic reserves

Price Stabilization:
- Initial panic subsides (players accept new prices)
- Supply catches up to demand (production increases)
- Prices settle 50-80% above peacetime levels
- New market equilibrium established
```

**Post-War Economic Adjustment**:
```
War Ends (Day 30):
- Immediate demand collapse: Combat operations cease
- Inventory surplus: Players have excess hoarded supplies
- Market flooding: Everyone sells stockpiles simultaneously

Price Crash (within 72 hours):
- Oil: -70% (from war peak, back to peacetime levels)
- Steel: -60% (surplus from reduced combat)
- Ammunition: -80% (massive oversupply from hoarding)
- Electronics: -50% (still needed for repairs, less dramatic crash)

Recovery Phase (Days 30-60):
- Prices stabilize at peacetime baseline
- Economic focus shifts to reconstruction
- Building materials (steel) regain value (infrastructure repairs)
- Market returns to normal trading patterns
```

---

## Regional Market Variations

### Price Differential Factors

**Geographic Distance**:
```
Base Item: Electronics (USA production)

Pricing by Distance from Production:
- USA West Coast (production site): 800 credits/unit
- USA East Coast (+1,000km): 850 credits/unit (+6% transport)
- UK (+5,000km): 1,100 credits/unit (+38% transport + risk)
- Pacific Islands (+3,000km): 1,200 credits/unit (+50% high risk route)
- Japan (+7,000km): 1,400 credits/unit (+75% maximum distance + hostile territory)

Transport Cost Factors:
- Fuel: 2-8 credits per 100km (fuel occupies cargo grid cells, see [[Inventory-System]])
- Insurance: 5-20% of cargo value (risk-based)
- Time: Longer routes = opportunity cost
- Risk: Hostile waters = premium for danger pay
- Cargo Grid Capacity: Ship cargo grid cells limit trade goods volume (see [[Inventory-System]])
```

**Local Supply/Demand Imbalances**:

**Case Study: Tobruk (Combat Zone Port)**:
```
Normal Market Conditions:
- Steel: 50 credits/unit
- Oil: 50 credits/unit
- Ammunition: 15 credits/unit

Tobruk Under Siege (Day 1):
- Steel: 150 credits/unit (+200% - supply lines cut)
- Oil: 250 credits/unit (+400% - critical shortage)
- Ammunition: 60 credits/unit (+300% - desperate demand)

Tobruk Under Siege (Day 7):
- Steel: 300 credits/unit (+500% - complete shortage)
- Oil: 400 credits/unit (+700% - starvation prices)
- Ammunition: 80 credits/unit (+433% - slightly lower as combat intensity reduces)

Strategic Opportunity:
- High-risk convoy breaks through siege
- Delivers 5,000 units oil, 2,000 units ammunition
- Purchase cost: 50,000 credits (peacetime prices)
- Sale revenue: 1,250,000 credits (siege prices)
- Net profit: 1,200,000 credits (2,400% return)
- Risk: 60% chance of convoy destruction
```

**Nation-Specific Specializations**:

**Pricing Advantages by Nation**:
```
German-Controlled Ports:
- Submarine equipment: -40% (specialization bonus)
- Advanced torpedoes: -30% (production expertise)
- Standard goods: Market average
- Allied equipment: +100% (import from enemy territory)

Japanese-Controlled Ports:
- Carrier aircraft: -35% (specialization bonus)
- Precision instruments: -25% (quality manufacturing)
- Standard goods: Market average
- European equipment: +80% (long-distance import)

US-Controlled Ports:
- Electronics: -30% (production leader)
- Mass-produced items: -20% (efficiency advantage)
- Standard goods: -10% (overall industrial capacity)
- Experimental tech: +50% (not specialized in innovation)

UK-Controlled Ports:
- Radar systems: -40% (pioneer advantage)
- Fire control: -30% (precision engineering)
- Standard goods: Market average
- Japanese tech: +90% (cross-Pacific import)
```

---

## NPC Market Mechanics

### AI Trader Behavior

**Dynamic Inventory Management**:

**NPC Vendor Algorithm**:
```
Inventory Restocking:
- Check current stock every 6 hours
- Compare to ideal stock level (based on historical demand)
- Purchase from market if below 50% ideal stock
- Sell to market if above 150% ideal stock

Pricing Strategy:
- Base price = Production cost × 1.15 (15% markup minimum)
- High demand adjustment: +5% per 10% shortage (max +50%)
- Low demand adjustment: -3% per 10% surplus (max -30%)
- Reputation discount: -2% per 10 reputation points above +50
- Reputation penalty: +3% per 10 reputation points below -25

Example: Steel Vendor in Industrial Port
Ideal Stock: 5,000 units
Current Stock: 2,000 units (40% of ideal)
Market Price: 55 credits/unit
Demand: High (combat nearby)

Vendor Pricing: 55 × 1.15 × 1.30 (shortage) = 82 credits/unit
Vendor Restocking: Purchases 3,000 units from market at 55 credits
Vendor Profit Margin: 33% (82-55/82)
```

**Reputation-Based Pricing**:

**Pricing Tiers**:
```
Hostile (-50 reputation):
- Base markup: +50%
- Example: 50 credit item costs 75 credits
- Limited stock access: Can only buy basic items
- No credit: Must pay upfront, no contracts available

Neutral (0 reputation):
- Base markup: Standard market prices
- Example: 50 credit item costs 50 credits
- Full catalog access: All non-restricted items
- Limited credit: Small contracts available

Friendly (+50 reputation):
- Base discount: -15%
- Example: 50 credit item costs 42.5 credits
- Priority access: Reserved stock for loyal customers
- Credit available: Contracts up to 50,000 credits

Allied (+75 reputation):
- Base discount: -25%
- Example: 50 credit item costs 37.5 credits
- Exclusive access: Restricted military items available
- Extensive credit: Contracts up to 200,000 credits
```

### Bulk Contract System

**NPC Nation Trade Agreements**:

**Example: British Admiralty Steel Contract**:
```
Contract Terms:
- Quantity: 500 tons (10,000 units) monthly
- Duration: 6-month commitment
- Price: 40 credits/ton (20% below market average)
- Delivery: Pick up from 3 designated British ports

Requirements:
- Reputation: +50 British Navy reputation (minimum)
- Security: Must maintain reputation throughout contract
- Pickup: Player responsible for transport security

Market Comparison:
- Open market steel: 45-60 credits/unit (volatile)
- Contract steel: 40 credits/unit (stable)
- Savings: 5-20 credits/unit (11-33% discount)

Risk Assessment:
- British ports occasionally under German submarine attack
- 5% monthly chance of port closure during pickup window
- Contract penalty if player fails delivery: -20 reputation

Strategic Value:
- Reliable supply enables consistent production planning
- Price protection from market volatility
- Strengthens diplomatic relations
- Potential for contract renewal with better terms
```

**Player Contract Strategy**:
```
Scenario: Player operates steel mill, needs consistent raw materials

Option 1: Market Purchases
- Price: Volatile (30-70 credits/unit)
- Availability: Subject to shortages
- Total Cost (annual): 540,000 credits (average 45/unit)

Option 2: US Government Contract
- Price: 35 credits/unit (fixed)
- Availability: Guaranteed supply
- Total Cost (annual): 420,000 credits
- Savings: 120,000 credits (22% reduction)
- Requirements: +60 US reputation, 12-month commitment

Decision Factors:
- Risk tolerance: Contract reduces uncertainty
- Reputation investment: Must maintain good standing
- Flexibility: Locked into single supplier
- Strategic planning: Enables accurate profit forecasting
```

---

## Market Manipulation & Economic Warfare

### Large-Scale Market Strategies

**Resource Hoarding (Cornering the Market)**:

**Strategy Execution**:
```
Objective: Control electronics market to drive prices up

Phase 1: Accumulation (Week 1-2)
- Quietly purchase 60% of available electronics
- Use multiple buyers to avoid detection
- Total investment: 800,000 credits (1,000 units @ 800 each)

Phase 2: Supply Restriction (Week 3)
- Withhold product from market
- Electronics shortage becomes apparent
- Price increases to 1,400 credits/unit (+75%)

Phase 3: Profit Taking (Week 4)
- Release 500 units at peak prices
- Revenue: 700,000 credits
- Gross profit: -100,000 credits (so far)

Phase 4: Market Exit (Week 5-6)
- Gradually sell remaining 500 units as market stabilizes
- Average sale price: 1,100 credits/unit
- Final revenue: 550,000 credits
- Total revenue: 1,250,000 credits
- Net profit: 450,000 credits (56% ROI)

Risks:
- NPC nations release strategic reserves (floods market)
- Player coalitions organize boycott
- Government intervention (anti-trust measures)
- Competitor hoarding disrupts strategy
```

**Counter-Manipulation by NPCs**:
```
Detection Threshold: Single entity controls >40% of market supply

AI Response:
1. Strategic Reserve Release (immediate):
   - Dump 20% of national stockpile onto market
   - Floods supply, crashes prices by 30-50%
   - Manipulator forced to sell at loss

2. Production Surge (72 hours):
   - Increase production by 50% for targeted resource
   - Sustained for 30 days
   - Long-term price suppression

3. Import Operations (1 week):
   - AI arranges cross-region imports
   - Brings external supply to break monopoly
   - International pricing competition

4. Political Consequences:
   - Reputation penalty: -30 with affected nation
   - Market access restrictions
   - Increased scrutiny on future transactions

Example: US Government Response to Oil Hoarding
- Player cartel controls 55% of Pacific oil supply
- US releases 500,000 units from strategic petroleum reserve
- Oil prices crash from 100 credits/unit to 45 credits/unit
- Cartel loses 30,000,000 credits in paper value
- Reputation penalty: -40 with USA for market manipulation
```

### Economic Warfare Operations

**Supply Line Interdiction**:

**Operation: Atlantic Commerce Destruction**:
```
Objective: Disrupt British economy by sinking merchant convoys

Strategic Planning:
- Target Identification: British convoy routes carrying 50,000 units resources weekly
- Force Allocation: 5 submarines dedicated to operation
- Duration: 4-week campaign

Week 1 Results:
- Convoys Attacked: 3 of 5
- Ships Sunk: 8 merchant vessels
- Resources Destroyed: 12,000 units (steel, oil, food)
- British Market Impact: Shortages drive prices +35%

Week 2-4 Results:
- Cumulative Ships Sunk: 25 vessels
- Cumulative Resources Destroyed: 38,000 units
- British Market Impact: Severe shortages, prices +120%
- Strategic Effect: British military operations limited by supply constraints

Economic Damage Assessment:
- Direct Value Destroyed: 2,500,000 credits (cargo value)
- Indirect Economic Impact: 8,000,000 credits (price inflation, lost production)
- British War Effort Degradation: -25% naval operations capacity
- Strategic Victory: Economic damage exceeds military value of ships sunk

British Response:
- Convoy escort increase: -15 destroyers from fleet operations
- Route changes: +20% transit time, +30% fuel costs
- Strategic reserves: Released to stabilize prices (temporary)
- Diplomatic pressure: Negotiate anti-submarine cooperation
```

**Industrial Sabotage**:

**Operation: Port Facility Destruction**:
```
Target: Hamburg Industrial Complex (German steel production hub)

Mission Execution:
- Special forces infiltration: 7-day operation
- Primary target: Steel mill (produces 30% of German steel)
- Secondary target: Oil refinery (supports industrial operations)

Successful Sabotage Results:
- Steel production: -60% for 14 days (repair time)
- German steel supply: -18,000 units
- Market impact: German steel prices +250%
- Strategic effect: German ship construction delayed 3 weeks

Economic Damage:
- Direct facility damage: 150,000 credits (repair costs)
- Lost production value: 900,000 credits (14 days × 1,286 units/day × 50 credits)
- Market disruption: 2,000,000 credits (price inflation, supply chain chaos)
- Total economic damage: 3,050,000 credits

Mission Cost:
- Special forces operation: 25,000 credits
- Intelligence gathering: 10,000 credits
- Support assets: 15,000 credits
- Total cost: 50,000 credits

ROI: 6,100% return on economic warfare investment
Strategic Value: Delays German naval expansion, weakens war economy
```

---

## Price Band Systems & Circuit Breakers

### Market Stability Mechanisms

**Automatic Circuit Breakers**:

**Trigger Conditions**:
```
Level 1 Alert: Price moves >30% in 1 hour
- System Warning: "Unusual market activity detected"
- Enhanced Monitoring: Flag large transactions for review
- No trading restrictions: Market continues normally

Level 2 Circuit Breaker: Price moves >50% in 1 hour
- Trading Halt: 15-minute pause for market cooling
- Investigation: Automated review of recent transactions
- Public Announcement: Inform players of price volatility
- Resume Trading: With enhanced oversight

Level 3 Emergency Halt: Price moves >100% in 1 hour
- Extended Halt: 1-hour trading suspension
- GM Investigation: Manual review of potential manipulation
- Reserve Release: NPCs may intervene with supply injection
- Restricted Resume: Possible limits on transaction sizes

Example: Electronics Market Crash
Hour 1: Price drops from 1,200 to 800 credits (-33%)
- Level 1 Alert triggered
- Investigation begins

Hour 2: Price drops to 500 credits (-38% additional)
- Level 2 Circuit Breaker triggered
- 15-minute trading halt
- Investigation reveals: Major war ended, military reducing electronics purchases
- Conclusion: Legitimate market forces, trading resumed

Natural vs Manipulation:
- Natural: Driven by game events (war start/end, major battles)
- Manipulation: Driven by coordinated player actions
- System learns: AI improves detection over time
```

**Price Band Enforcement**:

**Daily Price Limits**:
```
Basic Resources (Steel, Oil):
- Maximum daily movement: ±40% from opening price
- Rationale: Relatively stable commodities

Strategic Resources (Electronics):
- Maximum daily movement: ±75% from opening price
- Rationale: More volatile, subject to sudden demand spikes

Special Items (Ships, Rare Equipment):
- No price limits: Auction-based pricing
- Rationale: Unique items, legitimate wide value ranges

Example: Steel Price Band
Opening Price: 50 credits/unit
Upper Limit: 70 credits/unit (+40%)
Lower Limit: 30 credits/unit (-40%)

If market forces push price to 72 credits:
- Circuit breaker halts trading
- Investigation determines if manipulation or genuine shortage
- If legitimate: Increase daily limit to ±50% temporarily
- If manipulation: Enforce limit, penalize manipulators
```

---

## Market Intelligence & Information Systems

### Economic Data Transparency

**Public Market Information**:
- Current prices for all traded goods (real-time)
- 24-hour trading volume (delayed 1 hour)
- 7-day price charts (historical trends)
- Basic supply/demand indicators (simplified metrics)

**Premium Intelligence** (Requires Intelligence Credits):
- Real-time transaction logs (who bought what, when)
- Regional supply chain data (where goods are moving)
- Factory production schedules (future supply predictions)
- Corporate inventory levels (competitor intelligence)

**Example: Intelligence-Driven Trading**:
```
Public Information (Free):
- Steel price: 50 credits/unit
- 24-hour volume: 25,000 units traded
- 7-day trend: Stable (±5% variance)
- Recommendation: Normal trading conditions

Premium Intelligence (500 Intelligence Credits):
- Major corporation purchased 15,000 units steel in last 6 hours
- 3 new battleships under construction (14-day build time)
- Corporate inventory shows surplus oil, shortage steel
- Regional analysis: Steel demand will increase 40% over next week

Trading Strategy:
- Purchase steel futures immediately (before price spike)
- Invest 100,000 credits at current price (50 credits/unit)
- Wait 7 days for demand to materialize
- Sell at predicted price (70 credits/unit, +40%)
- Profit: 40,000 credits (40% ROI)

Intelligence Investment: 500 credits
Intelligence ROI: 8,000% (40,000 profit / 500 investment)
```

### Economic News System

**Automated Market Reports**:

**Daily Market Summary** (Generated at server reset):
```
═══════════════════════════════════════════════════
GLOBAL MARKET REPORT - November 17, 2025
═══════════════════════════════════════════════════

TOP MOVERS:
▲ Electronics: +45% (1,200 → 1,740 credits/unit)
   Cause: USA-Japan tensions increase radar demand

▼ Steel: -12% (50 → 44 credits/unit)
   Cause: Major salvage operations flood market

◆ Oil: Unchanged (50 credits/unit)
   Market: Stable supply-demand balance

REGIONAL HIGHLIGHTS:
• Pacific Theater: High activity, premium prices
• Atlantic Theater: Stable conditions
• Mediterranean: Combat zone, extreme volatility

STRATEGIC ALERTS:
⚠ UK stockpiling ammunition (expect shortage)
⚠ German submarine production increasing (torpedo demand)
⚠ US carrier task force deploying (aircraft fuel demand)

OPPORTUNITIES:
💰 Hamburg steel surplus (30% below market)
💰 Tobruk desperate for supplies (300% premium)
💰 Black market electronics available (Lisbon)

═══════════════════════════════════════════════════
```

**Event-Driven Alerts**:
```
🚨 MARKET ALERT 🚨
Major Battle in Pacific Theater

20 ships destroyed near Solomon Islands
- Steel surplus expected: Prices may drop 15-20%
- Electronics shortage: Demand for replacements
- Salvage opportunities: High-value wrecks available

Recommended Actions:
- Sell steel before price drop
- Buy electronics before price spike
- Position salvage vessels for recovery operations

Alert Time: 2 hours post-battle
Price Movement Window: 6-12 hours
```

---

## Economic Balance & Tuning

### Economic Health Metrics

**Server Economic Dashboard** (GM/Admin view):
```
Daily Resource Flow:
• Production: 25,000 units
• Consumption: 23,500 units
• Net Surplus: +1,500 units (+6.4% growth)
• Status: ✓ Healthy (growth sustainable)

Price Stability Index:
• Steel: 92/100 (very stable)
• Oil: 88/100 (stable)
• Electronics: 65/100 (moderate volatility)
• Ammunition: 78/100 (stable)
• Status: ✓ Healthy (acceptable volatility)

Wealth Distribution:
• Top 10%: Control 45% of wealth
• Middle 40%: Control 40% of wealth
• Bottom 50%: Control 15% of wealth
• Gini Coefficient: 0.52 (moderate inequality)
• Status: ⚠ Monitor (approaching concentration threshold)

Market Participation:
• Active Traders: 180 players (60% of server)
• Daily Transactions: 2,500 trades
• Average Transaction: 4,500 credits
• Market Liquidity: High
• Status: ✓ Healthy (strong participation)
```

**Intervention Triggers**:
```
Price Volatility Intervention:
- Trigger: Resource volatility >150% for 3+ days
- Action: NPC reserve release, increased production
- Goal: Stabilize prices below 125% volatility

Wealth Concentration Intervention:
- Trigger: Top 5% control >60% of wealth
- Action: Progressive taxation, economic events favoring small players
- Goal: Maintain Gini coefficient below 0.60

Market Liquidity Intervention:
- Trigger: Daily transactions drop below 1,000 trades
- Action: NPC market makers, trade incentives
- Goal: Maintain healthy market activity

New Player Economy:
- Trigger: New player income <50% of veteran income
- Action: Starter bonuses, protected markets, mentorship programs
- Goal: Ensure new player economic viability
```

---

## Related Documents

- **[Economy-Overview.md](Economy-Overview.md)** - Overall economic design philosophy
- **[Trading-System.md](Trading-System.md)** - Player trading mechanics and interfaces
- **[Nation-Overview.md](../11-Factions/Nation-Overview.md)** - Nation economic characteristics
- **[Port-System.md](../06-Extraction-Mechanics/Port-System.md)** - Port-based economic hubs

---

## Design Notes

### Key Insights
1. **Emergent Complexity**: Simple supply/demand rules create authentic market behavior
2. **Player Agency**: 300+ players collectively shape economy through actions
3. **Risk/Reward**: Economic warfare as strategic alternative to military conquest
4. **Market Stability**: Circuit breakers and NPC intervention prevent catastrophic failures
5. **Information Asymmetry**: Intelligence gathering creates competitive advantages

### Future Considerations
- Machine learning for AI trader behavior (adaptive to player strategies)
- Seasonal economic cycles (winter reduces production, summer increases activity)
- Economic achievements and leaderboards (richest traders, best speculators)
- Player-created financial instruments (loans, insurance, derivatives)
- Economic espionage missions (steal competitor intelligence)
