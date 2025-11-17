---
tags: [planned, design, core-concepts]
status: 📋 PLANNED
phase: Vision/Foundation
priority: HIGH
last-updated: 2025-11-17
---

# Target Audience

## Overview
This document defines the primary and secondary audiences for Fathoms Deep, including demographic profiles, player motivations, psychographic characteristics, and how our design decisions align with target player preferences.

## Implementation Status
**Status**: 📋 PLANNED - Audience definition for design guidance
**Phase**: Vision/Foundation
**Priority**: HIGH - Informs all design decisions

---

## Primary Demographics

### Core Target Profile
**Age Range**: 18-35 years old

**Rationale**: This demographic has:
- Disposable income for optional purchases
- Time investment capability (10-30 hours/week)
- Experience with complex game systems
- Comfort with competitive multiplayer
- Historical knowledge/interest in WWII

**Gaming Background**: 500+ hours in competitive/strategic games

**Typical Gaming History:**
- Competitive multiplayer experience (CS:GO, League of Legends, Dota 2)
- Strategic/tactical games (XCOM, Total War series, Paradox grand strategy)
- MMO experience (World of Warcraft, Eve Online, Albion Online)
- Extraction shooters (Escape from Tarkov, Hunt: Showdown)
- Naval games (World of Warships, War Thunder Naval, Atlantic Fleet)

**Platform**: PC gamers with mid-to-high spec systems

**Technical Requirements:**
- Comfortable with keyboard/mouse controls
- Owns gaming PC capable of running modern titles
- Stable internet connection for persistent multiplayer
- Willingness to engage with complex UI systems

**Time Investment**: 10-30 hours per week gaming availability

**Session Patterns:**
- **Weekday evenings**: 1-2 hour sessions (5-10 hours/week)
- **Weekend sessions**: 3-5 hour marathon sessions (6-10 hours/week)
- **Flexible scheduling**: Can commit to squadron operations
- **Long-term engagement**: Months to years of active play expected

---

## Player Motivations (Bartle Taxonomy)

### Achievers (40% - Largest Segment)
**Core Drive**: Accumulation, progression, and visible accomplishments

**What They Want:**
- Ship collection across all nations and tiers
- Crew progression and skill development
- Leaderboard rankings and competitive standing
- Rare module and equipment acquisition
- Reputation advancement across multiple nations
- Personal achievement milestones

**How We Serve Them:**
- **Deep progression systems**: 10 ship tiers per nation, extensive crew skills
- **Collection mechanics**: Hundreds of ships, modules, and equipment pieces
- **Achievement tracking**: Statistics, leaderboards, reputation systems
- **Visible status symbols**: Rare ships and modules that demonstrate accomplishment
- **Long-term goals**: Tier 10 ships and veteran crews require sustained effort

**Design Priorities:**
- Clear progression paths with visible milestones
- Meaningful differences between tiers and equipment
- Collection UI that showcases accumulated assets
- Achievement systems that reward completion

### Killers (30% - Second Largest Segment)
**Core Drive**: Competition, dominance, and defeating other players

**What They Want:**
- PvP combat superiority and tactical mastery
- Extraction denial (preventing enemy players from escaping)
- Reputation as skilled captain
- Piracy and aggressive playstyles
- High-stakes battles with meaningful victories
- Outplaying opponents through skill and strategy

**How We Serve Them:**
- **PvPvE combat**: Always-possible engagement across all zones
- **Extraction mechanics**: Opportunities to hunt laden enemies
- **Permadeath stakes**: Victories over high-tier ships are meaningful
- **Tactical depth**: Skill expression through positioning and timing
- **Pirate gameplay**: Dedicated hostile playstyle option
- **Reputation systems**: Become feared/respected combatant

**Design Priorities:**
- Balanced combat systems that reward skill
- Meaningful consequences for combat victories/defeats
- Hunting mechanics for finding valuable targets
- Fair engagement rules while allowing aggressive play

### Explorers (20% - Third Segment)
**Core Drive**: Discovery, optimization, and system mastery

**What They Want:**
- Historical ship discovery and authentication
- Optimal build theory-crafting (ship modules, crew skills)
- Map mastery and route optimization
- Hidden mechanics and interactions
- Economic optimization and trading routes
- Comprehensive understanding of all systems

**How We Serve Them:**
- **Complex ship customization**: Tetris-style module fitting
- **Deep crew systems**: Skill trees and specialization options
- **Large persistent world**: Exploration and route planning
- **Historical accuracy**: Authentic ships and equipment to discover
- **Economic systems**: Market analysis and trading optimization
- **Emergent mechanics**: Complex interactions to master

**Design Priorities:**
- Systems depth that rewards research and experimentation
- Historical documentation and ship information
- Market data and economic transparency
- Build variety and viable alternative strategies

### Socializers (10% - Smallest Primary Segment)
**Core Drive**: Interaction, cooperation, and community building

**What They Want:**
- Squadron/fleet coordination
- Server politics and diplomacy
- Trading networks and economic cooperation
- Mentoring new players
- Community events and gatherings
- Lasting friendships and relationships

**How We Serve Them:**
- **Squadron systems**: Fleet coordination and shared objectives
- **Multi-nation diplomacy**: Complex political landscape
- **Trading mechanics**: Economic cooperation opportunities
- **Communication systems**: Voice chat, text chat, signaling
- **Reputation networks**: Social capital through trustworthiness
- **Server communities**: Persistent worlds create lasting relationships

**Design Priorities:**
- Social features that facilitate cooperation
- Communication tools for coordination
- Group content that requires teamwork
- Community recognition systems

---

## Psychographic Profile

### Core Psychological Traits

#### 1. Enjoys High-Stakes Decision-Making
**Characteristic**: Thrives under pressure when decisions have meaningful consequences

**Manifestations:**
- Actively seeks challenging situations
- Values games where choices matter
- Enjoys risk/reward calculation
- Comfortable with possibility of loss

**Why This Matters**: Our permadeath and extraction mechanics require constant high-stakes decision-making. Players must decide:
- When to engage vs. retreat
- How much risk to accept for potential reward
- Whether to save crew or secure cargo
- Which expeditions to attempt based on risk tolerance

**Design Alignment**: Graduated risk system (Tiers 1-10) lets players opt into appropriate challenge levels. Lower tiers teach decision-making, higher tiers demand mastery.

#### 2. Values Skill Expression Over Luck
**Characteristic**: Prefers games where mastery and execution determine outcomes

**Manifestations:**
- Studies game systems deeply
- Practices to improve performance
- Appreciates fair competition
- Frustrated by RNG-dominated games

**Why This Matters**: Our tactical combat prioritizes:
- Positioning and maneuvering over reflexes
- Resource management and planning
- Knowledge of ship strengths/weaknesses
- Crew management and specialization

**Design Alignment**: Minimize random elements in core gameplay. When RNG exists (critical hits, penetration), ensure players can influence probabilities through skill (targeting, ammunition selection, positioning).

#### 3. Appreciates Historical Authenticity
**Characteristic**: Values educational content and simulation depth

**Manifestations:**
- Interested in WWII history
- Enjoys authentic ship designs
- Appreciates attention to detail
- Willing to learn complex systems

**Why This Matters**: Historical accuracy creates:
- Immersive atmosphere
- Educational value
- Respect for subject matter
- Community of history enthusiasts

**Design Alignment**: Authentic ship specifications, historical theaters, period-appropriate equipment. Balance simulation detail with gameplay accessibility.

#### 4. Willing to Accept Loss and Learning Curves
**Characteristic**: Views failures as learning opportunities rather than frustrations

**Manifestations:**
- Patient with complex games
- Analytical about mistakes
- Persistent through initial difficulty
- Values long-term mastery

**Why This Matters**: Permadeath and extraction mechanics create:
- Meaningful losses that teach lessons
- Initial difficulty that rewards persistence
- Long learning curve from Tier 1 to Tier 10
- Respect for other players who achieve mastery

**Design Alignment**: Graduated difficulty, clear feedback systems, educational lower tiers, optional higher-tier challenges.

#### 5. Seeks Long-Term Progression Goals
**Characteristic**: Motivated by enduring accomplishments and sustained engagement

**Manifestations:**
- Plays games for months/years
- Sets personal long-term goals
- Values permanent progression
- Enjoys ongoing community participation

**Why This Matters**: MMO persistence creates:
- Permanent ship and crew collection
- Reputation systems that build over time
- Server communities with lasting relationships
- Economic empires and political influence

**Design Alignment**: Multiple progression paths (ships, crews, reputation, economy), long-term goals that require sustained play, permanent accomplishments despite permadeath risk.

---

## Secondary Audiences

### History Enthusiasts
**Who They Are**: WWII naval warfare aficionados seeking authentic experiences

**Motivations:**
- Historical accuracy and ship authenticity
- Educational content about naval warfare
- Living history through gameplay
- Collecting famous ships (Yamato, Bismarck, Enterprise, etc.)

**How We Attract Them:**
- Historically accurate ship designs and specifications
- Documentation and historical context for all vessels
- Famous battles and theaters as playable locations
- Period-appropriate communication and UI

**Overlap with Primary Audience**: Often also Achievers (ship collection) or Explorers (historical research)

### MMO Veterans
**Who They Are**: Players from Eve Online, Albion Online, and similar persistent-world games

**Motivations:**
- Persistent world with player-driven economy
- High-stakes PvP with meaningful loss
- Complex social dynamics and politics
- Long-term progression and mastery

**How We Attract Them:**
- Extraction mechanics similar to Albion's full-loot zones
- Permadeath stakes like Eve's ship loss
- Squadron/corporation systems for organization
- Market-driven economy with player trading

**Overlap with Primary Audience**: Often Achievers or Killers with high time investment

### Tactical Gamers
**Who They Are**: Fans of XCOM, Total War, tactical strategy games

**Motivations:**
- Deep tactical combat systems
- Resource management and planning
- Turn-based or deliberate pacing
- Outsmarting opponents through strategy

**How We Attract Them:**
- Tactical naval combat with positioning emphasis
- Crew management similar to XCOM squad management
- Strategic resource allocation (ammunition, fuel, supplies)
- Multiple viable tactical approaches

**Overlap with Primary Audience**: Often Achievers or Explorers who value system mastery

### Simulation Fans
**Who They Are**: DCS World, IL-2 Sturmovik players wanting naval combat

**Motivations:**
- Realistic combat mechanics
- Detailed ship systems and damage modeling
- Authentic historical equipment
- Skill-based competitive play

**How We Attract Them:**
- Detailed damage modeling (armor penetration, fire, flooding)
- Realistic ship handling and ballistics
- Historical accuracy in ship specifications
- Complex systems management (damage control, repairs)

**Overlap with Primary Audience**: Often Killers who value skill expression or Explorers who value system depth

---

## Anti-Audience (Who This Game Is NOT For)

### Casual Mobile Gamers
**Why Not:**
- Time commitment too high (60-90 minute sessions)
- Complexity too demanding
- Permadeath too punishing
- PC-only platform

### Pure Arcade Action Players
**Why Not:**
- Pacing too slow and deliberate
- Emphasis on tactics over reflexes
- Long-term progression over instant gratification
- Strategic planning required

### Risk-Averse Players
**Why Not:**
- Permadeath mechanics create anxiety
- Extraction system means nothing secured until return
- PvPvE means constant threat
- Losses have meaningful consequences

### Solo-Only Players
**Why Not:**
- MMO environment requires social interaction
- Squadron play advantageous at high tiers
- Server politics affect gameplay
- Community engagement expected

---

## Player Journey Mapping

### New Player (Tiers 1-3, Weeks 1-4)
**Psychological State**: Curious but overwhelmed

**Key Experiences:**
- Learning basic combat mechanics
- First successful extraction
- First ship upgrade
- Joining first squadron

**Design Needs:**
- Clear tutorials and guidance
- Forgiving low-tier gameplay
- Immediate positive reinforcement
- Accessible entry ships

**Retention Goals**: 60% after first week, 50% after first month

### Engaged Player (Tiers 4-6, Months 1-3)
**Psychological State**: Confident and exploring options

**Key Experiences:**
- First permadeath threat (Tier 5)
- First high-value extraction
- Specializing ship and crew builds
- Active squadron participation

**Design Needs:**
- Build variety and experimentation
- Challenging but achievable goals
- Social integration opportunities
- Clear progression path

**Retention Goals**: 70% month-over-month retention

### Veteran Player (Tiers 7-10, Months 3+)
**Psychological State**: Mastery-focused and community-invested

**Key Experiences:**
- High-stakes Tier 9-10 expeditions
- Server reputation and recognition
- Economic empire or combat dominance
- Mentoring newer players

**Design Needs:**
- Endgame content that remains challenging
- Status recognition and respect
- Community leadership opportunities
- New goals and achievements

**Retention Goals**: 80%+ long-term retention

---

## Market Sizing

### Total Addressable Market (TAM)
**Estimate**: 50 million PC gamers interested in strategic/tactical multiplayer games

**Sources:**
- World of Warships: ~15 million registered players
- Eve Online: ~300,000 active players
- Escape from Tarkov: ~10 million copies sold
- War Thunder: ~40 million registered players

### Serviceable Addressable Market (SAM)
**Estimate**: 5 million players interested in hardcore tactical naval combat

**Criteria:**
- Active PC gamers
- Interest in WWII/naval warfare
- Tolerance for permadeath mechanics
- 10+ hours/week gaming availability
- Willingness to pay for premium game

### Serviceable Obtainable Market (SOM)
**Year 1 Goal**: 50,000-100,000 active players
**Year 3 Goal**: 250,000-500,000 active players

**Rationale**:
- Niche but underserved market
- Direct competitors have significant weaknesses
- Extraction mechanics appeal to growing genre
- MMO persistence creates lasting engagement

---

## Monetization Alignment

### What Our Audience Will Pay For

**Acceptable:**
- Premium account (convenience, faster progression)
- Cosmetic ship skins and crew customization
- Additional port slots for ship collection
- Historical documentation and educational content
- Quality-of-life features (UI customization, market tools)

**Unacceptable:**
- Pay-to-win ships or modules
- Permadeath insurance that bypasses risk
- Exclusive competitive advantages
- Loot boxes with random progression items

**Philosophy**: Our audience values fairness and skill expression. Monetization must support the game without creating advantages for paying players.

---

## Community Engagement Strategy

### Primary Communities
- **Discord**: Main communication hub for squadrons and server coordination
- **Reddit**: Strategy discussion, build sharing, game updates
- **Twitch/YouTube**: Streaming and content creation for tactical gameplay
- **Forums**: Long-form strategy guides and historical discussions

### Content Creator Support
Our audience includes:
- **Strategy content creators**: Detailed guides and optimization
- **Historical creators**: Documentary-style ship reviews
- **Competitive streamers**: High-stakes expeditions and PvP
- **Educational streamers**: New player tutorials and squadron training

### Developer Communication
Our audience expects:
- Transparent development updates
- Active community engagement
- Data-driven balance decisions
- Responsiveness to feedback

---

## Cross-References
- [[Game-Vision]] - Overall design philosophy alignment
- [[Competitive-Positioning]] - How we attract target audience away from competitors
- [[Extraction-Mechanics]] - Core loop designed for target player motivations
- [[Permadeath-System]] - Risk tolerance and challenge seeking alignment
- [[Monetization-Strategy]] - Revenue approach respecting audience values

---

## Research & Validation

### Player Surveys
- [ ] Survey existing naval game players about desired features
- [ ] Test permadeath tolerance across age demographics
- [ ] Validate time investment expectations
- [ ] Assess price sensitivity for premium features

### Competitive Analysis
- [ ] Analyze World of Warships player complaints
- [ ] Study Eve Online retention patterns
- [ ] Research Tarkov player motivations
- [ ] Identify underserved niches in naval gaming

### Playtesting Feedback
- [ ] Early alpha with core target demographic
- [ ] Difficulty curve validation across player types
- [ ] Retention tracking through progression tiers
- [ ] Community formation and social dynamics observation

---

## Future Enhancements
- **Expanded Demographics**: Consider 35-50 age bracket as game matures
- **Regional Audiences**: Localization for European and Asian markets
- **Accessibility Features**: Options for players with disabilities
- **Casual Mode**: Lower-stakes gameplay for broader audience

---

## Changelog
- **2025-11-17**: Initial document creation - extracted from GDD_Updated-1.md lines 114-149
