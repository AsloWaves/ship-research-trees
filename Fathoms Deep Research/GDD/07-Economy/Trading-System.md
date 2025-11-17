# Trading System

**Status**: 📋 PLANNED (Phase 3 feature)
**Tags**: [planned, phase3, economy-system, player-trading]
**Priority**: MEDIUM (Phase 3 focus)
**Last Updated**: 2025-11-17

---

## Vision Statement

Multi-tier trading networks enabling player-to-player commerce, NPC market interactions, auction house systems, and port-based trading hubs that create a living economy driven by 300+ simultaneous players.

---

## Core Trading Mechanics

### Direct Player-to-Player Trading

**Trade Window System**:
- **Face-to-Face Trading**: Players within 500m can initiate direct trades
- **Trade Offer Interface**:
  - Left panel: Player 1 offers (resources, credits, items)
  - Right panel: Player 2 offers
  - Both players must confirm before trade executes
  - 30-second timeout for inactive trades
- **Security Features**:
  - Final confirmation screen showing all items/credits
  - Trade history log (last 50 trades)
  - Fraud reporting system for scam attempts
  - Cannot trade while in combat or damaged

**Trade Limitations**:
- **At Sea Restrictions**:
  - Can only trade basic supplies and credits at sea
  - No ship component trading while underway
  - No bulk cargo transfers (requires port facilities)
- **Port Trading**:
  - Full trading functionality available
  - Can transfer cargo between ships
  - Component and module trading enabled
  - Large bulk transfers possible

**Transaction Security**:
- Automatic trade verification (checks item validity)
- Credit balance confirmation before trade
- Cannot trade stolen or locked items
- 5-minute trade cooldown to prevent rapid fraud

### Mail System Trading

**Asynchronous Trading**:
- **Send Items via Mail**:
  - Attach items and credits to mail messages
  - Recipient must be online to receive high-value items (>10,000 credits)
  - 7-day expiration, items returned to sender
  - 1% transaction fee for mail-based trades
- **Use Cases**:
  - Corporate material distribution to members
  - Long-distance trading without meeting
  - Payment for services rendered
  - Gift and reward distribution

**Security Measures**:
- Cannot send more than 50,000 credits via single mail
- High-value items (>25,000 credit value) require confirmation
- Trade history logged for dispute resolution
- Mail can be intercepted by pirates (if sender's ship destroyed en route)

---

## Port-Based Trading Hubs

### Local Port Markets

**Port Market Characteristics**:
Each port has unique market characteristics based on:
- **Port Type**: Industrial, Military, Trading, Resource Extraction
- **Regional Economy**: Local supply and demand
- **Faction Control**: Nation controlling port affects available goods
- **War Status**: Conflict disrupts supply and increases prices

#### Industrial Ports
**Hamburg Example** (German Industrial Port):

**Local Advantages**:
- German modules 20% below market average
- Advanced engineering components available
- High-quality steel production (premium alloys)
- Specialized submarine equipment

**Resource Needs**:
- High demand for rare metals (30% above market)
- Electronics shortage (50% above market)
- Constant steel demand (10% above market)

**Security Status**:
- Occasional Allied air raids (5% chance daily)
- Affects port operations (temporarily closes market)
- Price spikes during raid warnings

**Player Opportunities**:
- Import electronics from captured sources (high profit margins)
- Export German engineering to neutral markets (political risk)
- Establish local production using German expertise
- Trade with submarine fleet (high demand for torpedoes and electronics)

**Example Trade Route**:
```
Buy: German advanced radar (8,000 credits in Hamburg)
Transport to: Neutral port (1,500km, moderate risk)
Sell: German advanced radar (14,000 credits at neutral port)
Profit: 6,000 credits (75% margin) minus transport costs
Risk: 10% chance of interception by British patrols
```

#### Military Bases
**Pearl Harbor Example** (US Military Base):

**Local Advantages**:
- US military equipment at 15% discount (reputation required)
- Advanced aircraft and carrier systems available
- Bulk ammunition at military pricing
- Priority repair and refit services

**Restricted Access**:
- Requires +50 US Navy reputation for full market access
- Advanced technology requires +75 reputation
- Experimental systems require +90 reputation
- Enemy factions completely barred

**Premium Pricing**:
- Weapons and ammunition at 30% premium (military quality)
- Advanced radar and electronics at 40% premium
- Carrier aircraft at 50% premium (elite systems)

**Strategic Value**:
- Access to latest US technology
- Intelligence on US fleet movements
- Mission opportunities for reputation gain
- Safe harbor during Pacific operations

#### Neutral Ports
**Lisbon Example** (Portuguese Neutral Port):

**Market Characteristics**:
- Moderate pricing (global market average)
- Unrestricted trading (all factions welcome)
- High transaction fees (10-15% on all trades)
- No reputation requirements

**Trading Opportunities**:
- Cross-faction trading hub (Germans and British both present)
- International arbitrage opportunities
- Information exchange (Intelligence Credits valuable here)
- Black market access (contraband available discreetly)

**Security Features**:
- No combat allowed in port waters (enforced by Portuguese navy)
- Safe haven during conflicts
- Diplomatic immunity for traders
- Cannot be blockaded by any faction

**Strategic Role**:
- Currency exchange between factions
- Technology transfer via third parties
- Espionage and intelligence gathering
- Refugee for ships fleeing combat

#### Combat Zone Ports
**Tobruk Example** (Contested North African Port):

**Extreme Volatility**:
- Prices fluctuate ±100% based on military situation
- Control changes hands frequently (affects available goods)
- Supply shortages common (scarcity drives prices)
- High-risk, high-reward trading

**Operational Challenges**:
- Port facilities frequently damaged (limited services)
- Supply convoys often intercepted (causing shortages)
- Air raids common (20% chance daily)
- Constant military activity

**Trading Opportunities**:
- Desperate demand for ammunition (300% markup possible)
- Food and medical supplies critical (200% markup)
- Fuel shortages create opportunities (400% markup during siege)
- Salvage operations highly profitable

**Risk vs Reward**:
- High profit margins (100-400%)
- High risk of ship loss (30% per visit)
- Limited services and facilities
- Strategic positioning for military operations

---

## Regional Trade Networks

### Cross-Regional Arbitrage

**Price Differentials**:
- Same goods vary 50-200% between regions
- Driven by local supply/demand imbalances
- Information lag creates opportunities (market conditions not immediately known)
- Distance and risk justify price differences

**Transport Economics**:
- **Distance**: Longer routes = higher fuel costs (2-8 oil per hour)
- **Route Danger**: High-risk routes justify higher markup
- **Cargo Capacity**: Larger ships more efficient but higher risk
- **Time Sensitivity**: Fast ships can exploit temporary price spikes

### Example Trade Routes

#### Pacific Theatre Commerce
**Route**: Japanese electronics from Truk to US West Coast

**Step-by-Step Analysis**:

1. **Purchase Point** (Truk):
   - Japanese electronics: 800 credits per unit
   - Local surplus (Japanese production hub)
   - Stable pricing (±5% daily variance)
   - Bulk purchase discounts available (10% for 100+ units)

2. **Transport Challenge**:
   - **Distance**: 2,000km through submarine-infested waters
   - **Duration**: 40 hours at cruising speed
   - **Fuel Cost**: 200 units oil (400 credits)
   - **Route Security**:
     - High submarine activity (15% encounter chance)
     - US convoy routes offer some protection
     - Night travel reduces detection risk (by 40%)

3. **Market Intelligence**:
   - US West Coast paying 1,400 credits per unit
   - Demand driven by carrier operations in Pacific
   - Price stable for next 48 hours (intelligence report)
   - Competing traders on same route (affects timing)

4. **Risk Assessment**:
   - 15% chance of submarine attack during transit
   - 5% chance of severe weather delaying arrival
   - 3% chance of market price collapse before arrival
   - Insurance available (100 credits per unit, 80% coverage)

5. **Profit Calculation**:
   ```
   Purchase: 800 credits/unit × 100 units = 80,000 credits
   Transport: 400 credits (fuel) + 50 credits (port fees) = 450 credits
   Insurance: 100 credits/unit × 100 units = 10,000 credits

   Revenue: 1,400 credits/unit × 100 units = 140,000 credits

   Gross Profit: 140,000 - 80,000 - 450 - 10,000 = 49,550 credits
   Net Margin: 56% (assuming safe arrival)

   Risk-Adjusted Profit: 49,550 × 0.85 (arrival probability) = 42,118 credits
   Time Investment: 40 hours
   Hourly Rate: 1,053 credits/hour
   ```

6. **Optimization Strategies**:
   - Travel in convoy (reduces risk to 8%)
   - Night operations (reduces detection by 40%)
   - Route variation (avoid predictable patterns)
   - Forward market intelligence (predict price movements)

#### Atlantic Trade Triangle
**Multi-Stop Route**: UK → USA → Brazil → UK

**Leg 1: UK to USA**:
- Export: British radar systems (high demand in USA)
- Purchase Price: 2,500 credits per unit (London)
- Sale Price: 4,200 credits per unit (New York)
- Profit: 1,700 credits per unit (68% margin)
- Risk: 20% U-boat encounter chance

**Leg 2: USA to Brazil**:
- Export: US industrial machinery (needed for Brazilian development)
- Purchase Price: 5,000 credits per unit (New York)
- Sale Price: 8,500 credits per unit (Rio de Janeiro)
- Profit: 3,500 credits per unit (70% margin)
- Risk: 10% submarine encounter chance (South Atlantic safer)

**Leg 3: Brazil to UK**:
- Export: Brazilian rubber (critical British war material)
- Purchase Price: 300 credits per unit (Rio de Janeiro)
- Sale Price: 800 credits per unit (London)
- Profit: 500 credits per unit (167% margin)
- Risk: 25% U-boat encounter chance (North Atlantic dangerous)

**Total Route Economics**:
```
Total Distance: 18,000km
Total Duration: 12 days (288 hours)
Fuel Cost: 2,400 units oil (4,800 credits)
Port Fees: 1,500 credits
Insurance: 15,000 credits

Total Revenue: 196,000 credits (from all three legs)
Total Costs: 155,000 credits (goods) + 4,800 (fuel) + 1,500 (fees) + 15,000 (insurance) = 176,300 credits
Net Profit: 19,700 credits
Profit Margin: 11% (but three trades in one voyage)
Risk-Adjusted Profit: 19,700 × 0.55 (combined arrival probability) = 10,835 credits
```

---

## Auction House System

### Dynamic Auction Mechanics

**Auction Types**:
1. **Standard Auction**: Highest bidder wins (7-day listing)
2. **Buy Now**: Instant purchase at fixed price
3. **Dutch Auction**: Price decreases over time until someone buys
4. **Blind Auction**: Sealed bids, highest wins (used for rare items)

**Listing Requirements**:
- **Listing Fee**: 100 credits + 2% of starting bid (non-refundable)
- **Minimum Bid**: Seller sets reserve price
- **Auction Duration**: 1, 3, or 7 days
- **Item Location**: Must be in port to list (cannot list cargo at sea)

**Bidding Mechanics**:
- **Bid Increments**:
  - <1,000 credits: 50 credit increments
  - 1,000-10,000 credits: 500 credit increments
  - >10,000 credits: 1,000 credit increments
- **Automatic Bidding**: Set maximum bid, system auto-bids for you
- **Last-Minute Bidding**: Auction extends 5 minutes if bid in final minute
- **Proxy Bidding**: Can authorize corp members to bid on your behalf

**Transaction Fees**:
- **Seller Fee**: 10% of final sale price
- **Buyer Fee**: None (paid by seller)
- **Failed Sale**: If reserve not met, 50% listing fee refunded
- **Canceled Auction**: Full forfeit of listing fee (anti-manipulation)

### Rare Equipment Auctions

#### Example: Captured KMS Bismarck
**Auction Event Details**:

**Item Description**:
- **Ship**: Legendary German battleship
- **Status**: Battle-damaged but salvageable
- **Hull Integrity**: 45% (requires extensive repairs)
- **Unique Advantages**:
  - German engineering (+15% armor effectiveness)
  - Superior armor design (historical accuracy)
  - Prestige symbol (famous ship)
  - Access to German technology tree

**Auction Parameters**:
- **Opening Bid**: 500,000 credits (standard battleship cost)
- **Reserve Price**: 800,000 credits (set by seller)
- **Auction Duration**: 7 days
- **Auction Type**: Standard (highest bidder wins)

**Repair Requirements**:
- **Cost**: 200,000 credits for hull repairs
- **Time**: 3 months in major shipyard
- **Materials**: 5,000 units steel, 500 units electronics
- **Expertise**: Requires German engineers (+50,000 credit bonus if non-German owner)

**Bidding Competition**:
- 12 major players/corporations participating
- Opening bid: 500,000 credits (Individual player)
- Mid-auction: 750,000 credits (German industrial corporation)
- Final hour: Bidding war between 3 richest entities
- Last-minute bid: 1,250,000 credits (German corporation)
- **Final Sale**: 1,250,000 credits

**Strategic Impact**:
- Buyer gains access to German technology
- Prestige symbol for corporation
- Can be used as flagship for propaganda purposes
- Potential to reverse-engineer German engineering

**Post-Auction Analysis**:
```
Purchase Price: 1,250,000 credits
Repair Costs: 250,000 credits (with German expertise)
Total Investment: 1,500,000 credits

Equivalent New Battleship: 600,000 credits
Premium Paid: 900,000 credits (for prestige and technology access)

Strategic Value: Priceless (access to German tech tree)
Prestige Value: High (famous ship recognition)
Combat Value: Standard battleship +15% armor bonus
```

#### Example: Elite Ace Pilot
**Auction Details**:

**Crew Member**: Commander Hans "Eagle" Müller
- **Skills**:
  - Air Combat +50 (maximum skill)
  - Torpedo Bombing +45
  - Dive Bombing +40
  - Leadership +35
- **Experience**: 500 combat missions, 75 confirmed kills
- **Special Abilities**:
  - "Eagle Eye" passive (10% detection range)
  - "Precision Strike" active (25% accuracy bonus once per battle)

**Auction Parameters**:
- Opening Bid: 25,000 credits
- Final Sale: 185,000 credits
- Competition: 8 carrier-focused players

**Strategic Value**:
- Immediate combat effectiveness boost
- Training bonus for other pilots (+20% learning speed)
- Morale boost for crew (psychological advantage)
- Rare skill combination unavailable elsewhere

---

## Resource Futures Markets

### Strategic Resource Speculation

**Futures Contract System**:
- **Contract Type**: Agreement to buy/sell resources at future date for fixed price
- **Contract Duration**: 7, 14, or 30 days
- **Delivery Location**: Specified port(s)
- **Settlement**: Physical delivery or cash settlement

**Speculation Strategies**:

#### Pre-War Stockpiling
**Scenario**: Intelligence suggests USA and Japan tensions escalating

**Strategy**:
1. **Analysis**: War will increase demand for steel and oil by 200-300%
2. **Action**: Purchase steel futures at current prices (50 credits/unit)
3. **Investment**: 100,000 credits for 2,000 units (30-day contract)
4. **War Begins**: Steel prices spike to 140 credits/unit
5. **Settlement**: Sell contracted steel at market price
6. **Profit**: (140 - 50) × 2,000 = 180,000 credits profit (180% return)

**Risks**:
- War doesn't materialize (futures expire worthless or at loss)
- Unexpected peace treaty tanks prices
- Competitor speculation drives up futures prices
- Delivery disrupted by military action

#### Seasonal Demand Patterns
**Observation**: Winter reduces oil production, summer increases naval activity

**Strategy**:
1. **Summer**: Buy oil futures for winter delivery (low prices)
2. **Winter**: Sell oil at premium when production drops
3. **Annual Cycle**: Repeat predictable pattern

**Example Cycle**:
```
Summer Oil Price: 30 credits/unit
Winter Oil Price: 55 credits/unit
Futures Cost (summer purchase): 32 credits/unit

Investment: 50,000 credits (1,562 units)
Winter Sale: 55 × 1,562 = 85,910 credits
Profit: 35,910 credits (72% return over 6 months)
```

#### Technology Transition Speculation
**Scenario**: Rumor of new radar technology requiring rare metals

**Strategy**:
1. **Intelligence**: Gather information on upcoming technology
2. **Analysis**: New radar will require 10 units electronics + 5 units rare metals
3. **Speculation**: Buy rare metal futures before demand spike
4. **Technology Release**: Rare metals spike 300%
5. **Settlement**: Sell at inflated prices

**Example**:
```
Rare Metal Price (pre-announcement): 200 credits/unit
Rare Metal Price (post-announcement): 800 credits/unit

Futures Purchase: 50 units @ 210 credits = 10,500 credits
Market Sale: 50 units @ 800 credits = 40,000 credits
Profit: 29,500 credits (281% return)

Risk: Rumor false, technology delayed, alternative materials used
```

---

## Corporate & Alliance Trading

### Trade Alliances

**Mutual Resource Sharing**:
- **Structure**: 5-20 players form trading cooperative
- **Benefits**:
  - Bulk purchase discounts (10-20% based on volume)
  - Shared intelligence on market conditions
  - Mutual defense of trade routes
  - Coordinated market manipulation

**Alliance Example**: Pacific Industrial Consortium
- **Members**: 8 major players controlling Pacific trade routes
- **Market Control**: 60% of Pacific electronics trade, 40% of raw materials
- **Strategy**:
  - Standardized pricing (prevents internal competition)
  - Resource sharing during shortages
  - Combined fleet protects trade routes
  - Political influence through economic power

**Economic Benefits**:
```
Solo Trader Electronics Price: 800 credits/unit
Alliance Bulk Price: 640 credits/unit (20% discount)

Solo Trader Annual Profit: 500,000 credits
Alliance Member Annual Profit: 850,000 credits (70% increase)

Additional Benefits:
- Trade route protection (reduces losses by 40%)
- Market intelligence (predicts movements 3 days early)
- Political influence (affects NPC nation policies)
```

### Corporate Material Distribution

**Internal Trading Systems**:
- **Corporation Warehouse**: Shared storage for members
- **Requisition System**: Members request materials at cost
- **Production Sharing**: Coordinate manufacturing to eliminate waste
- **Strategic Stockpiles**: Emergency reserves for major operations

**Distribution Example**:
```
Corporation: "Atlantic Fleet Command"
Members: 25 active players
Weekly Resource Needs: 50,000 units steel, 15,000 units oil, 2,000 units electronics

Centralized Purchasing:
- Bulk discount: 15% on all materials
- Warehouse storage: Central depot in New York
- Distribution: Weekly convoys to members
- Cost: Shared among members (reduces individual burden by 40%)

Individual Cost (if buying solo): 12,000 credits/week
Corporation Member Cost: 7,200 credits/week (40% savings)
```

---

## Trading UI/UX Design

### Market Interface

**Main Market View**:
- **Left Panel**: Resource categories and filters
- **Center Panel**: Available items with price, quantity, location
- **Right Panel**: Player inventory and credits

**Filtering Options**:
- Resource type (steel, oil, electronics, etc.)
- Price range (custom min/max)
- Location (current port, region, global)
- Seller type (player, NPC, auction)
- Quality grade (standard, premium, experimental)

### Trade Window

**Direct Trading Interface**:
```
╔══════════════════════════════════════════════════════════╗
║            TRADE WITH: PLAYER_NAME                       ║
╠══════════════════════════════════════════════════════════╣
║  YOUR OFFER              │         THEIR OFFER           ║
║                          │                               ║
║  [Item Slot 1]           │         [Item Slot 1]         ║
║  [Item Slot 2]           │         [Item Slot 2]         ║
║  [Item Slot 3]           │         [Item Slot 3]         ║
║  ...                     │         ...                   ║
║                          │                               ║
║  Credits: [_______]      │         Credits: [_______]    ║
║                          │                               ║
║  [✓ Confirm] [✗ Cancel]  │  [✓ Confirm] [✗ Cancel]       ║
╚══════════════════════════════════════════════════════════╝
```

### Auction House Interface

**Search and Browse**:
- **Search Bar**: Keyword search for specific items
- **Category Filters**: Ship components, resources, crew, ships, special items
- **Sort Options**: Price (low to high), Time remaining, Most bids
- **View Modes**: List view, Grid view, Detailed view

**Individual Auction View**:
```
╔══════════════════════════════════════════════════════════╗
║  AUCTION: Rare Item Name                                 ║
╠══════════════════════════════════════════════════════════╣
║  [Item Image/3D Preview]                                 ║
║                                                          ║
║  Current Bid: 125,000 credits                            ║
║  Time Remaining: 2d 14h 32m                              ║
║  Number of Bids: 7                                       ║
║                                                          ║
║  Seller: PLAYER_NAME (98% positive feedback)             ║
║  Location: Pearl Harbor                                  ║
║                                                          ║
║  Description:                                            ║
║  [Seller's description of item...]                       ║
║                                                          ║
║  Your Bid: [_______] credits                             ║
║  Or: [Set Maximum Bid: _______] (auto-bid)               ║
║                                                          ║
║  [Place Bid]  [Watch Auction]  [Ask Question]            ║
╚══════════════════════════════════════════════════════════╝
```

---

## Anti-Fraud and Security Measures

### Scam Prevention

**Automated Checks**:
- **Item Verification**: System validates all items exist and are tradeable
- **Credit Validation**: Confirms buyer has sufficient funds
- **Ownership Check**: Verifies seller owns items being traded
- **Lock Status**: Prevents trading stolen or mission-locked items

**Player Reputation**:
- **Feedback System**: Buyers and sellers rate each transaction (1-5 stars)
- **Dispute Resolution**: GMs investigate reported scams
- **Fraud Penalties**: Confirmed scammers receive:
  - 7-day trade ban
  - -50 reputation with all factions
  - Permanent mark on player profile
  - Potential account suspension for repeat offenses

### Market Manipulation Protection

**Anti-Cornering Measures**:
- **Purchase Limits**: Cannot buy more than 30% of available supply in single transaction
- **Price Bands**: Automatic circuit breakers if prices move >50% in 1 hour
- **Whale Alerts**: System monitors large transactions for market manipulation
- **Government Intervention**: NPC nations can release reserves to stabilize markets

**Exploit Prevention**:
- **Trade Cooldowns**: 5-minute cooldown between trades with same player
- **Audit Trails**: All transactions logged and monitored
- **Suspicious Activity Flags**: Automated detection of unusual patterns
- **Manual Review**: GMs investigate flagged transactions

---

## Related Documents

- **[Economy-Overview.md](Economy-Overview.md)** - Overall economic design and currency systems
- **[Market-Dynamics.md](Market-Dynamics.md)** - Supply/demand mechanics and pricing algorithms
- **[Nation-Overview.md](../09-Faction-System/Nation-Overview.md)** - Nation-specific trading advantages
- **[Port-System.md](../06-Extraction-Mechanics/Port-System.md)** - Port facilities and trading infrastructure

---

## Design Notes

### Key Design Principles
1. **Transparency**: Players should understand why prices are what they are
2. **Opportunity**: Multiple viable trading strategies (arbitrage, speculation, production)
3. **Risk/Reward**: Profitable trades involve meaningful risk
4. **Player Agency**: Players shape the economy through collective actions
5. **Anti-Frustration**: Systems prevent unfair exploitation and scams

### Future Enhancements
- Player-owned shops in major ports (permanent stalls)
- Escrow services for large transactions (neutral third party)
- Trade caravans with NPC escort services
- Commodity futures exchange with advanced financial instruments
- Insurance marketplace (players can insure each other's cargo)
