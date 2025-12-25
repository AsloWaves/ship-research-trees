---
tags: [planned, design, core-concepts]
status: 📋 PLANNED
phase: Vision/Foundation
priority: HIGH
last-updated: 2025-11-17
---

# Game Vision

## Overview
Fathoms Deep is a massive-scale tactical 2D naval MMO that combines the high-stakes extraction mechanics of Escape from Tarkov with authentic WWII naval warfare. This document defines the core vision, player fantasy, and emotional pillars that drive all design decisions.

## Implementation Status
**Status**: 📋 PLANNED - Core vision document for design philosophy
**Phase**: Vision/Foundation
**Priority**: HIGH - Foundational design document

---

## The Vision

### Core Vision Statement
**Fathoms Deep is a massive-scale tactical 2D naval MMO supporting 300+ simultaneous players in persistent ocean theaters. The core gameplay revolves around Extraction-Based Naval Combat** - venture into dangerous waters to acquire valuable loot (modules, turrets, crew, resources) through PvPvE combat or resource extraction, then successfully return to friendly ports to secure your gains.

### What Makes This Game Unique
Fathoms Deep fills a market gap that no existing game occupies: **tactical WWII naval combat with extraction mechanics, crew RPG systems, and massive-scale MMO persistence**. We combine:

- **Tactical Depth**: Positioning, timing, and resource management over reflexes
- **High-Stakes Risk**: Permadeath mechanics that make every decision meaningful
- **Historical Authenticity**: WWII ships, weapons, and theaters with simulation accuracy
- **MMO Scale**: 300+ player persistent worlds with complex political dynamics
- **Extraction Mechanics**: Nothing is secured until you return to friendly port

---

## Player Fantasy - "The Captain's Journey"

### Core Fantasy
*"I am a naval captain in WWII, commanding my ship and crew through dangerous waters. Every decision matters. Every battle is earned. Every successful return home is a triumph."*

This isn't about being a superhero or unstoppable force. It's about being a **skilled commander** who:
- Makes calculated decisions under pressure
- Earns every victory through tactical mastery
- Accepts meaningful losses that inform future strategy
- Builds lasting reputation through consistent performance
- Commands crew who grow, learn, and potentially die under their leadership

### The Captain's Emotional Journey
Players should feel like they're living the experience of a WWII naval commander:

**Before Combat:**
- Anticipation during ship outfitting
- Strategic planning of routes and objectives
- Tension building as you leave safe harbor
- Awareness that "anything could happen out there"

**During Combat:**
- Adrenaline rush of tactical execution
- Pride in crew skill expression
- Anxiety over damage and crew casualties
- Satisfaction of outplaying opponents

**After Combat:**
- Relief when safely returning to port
- Triumph when securing valuable loot
- Grief when losing crew or ship
- Determination to improve and return stronger

---

## Emotional Pillars

### 1. Tension & Release
**Design Goal**: Create a rhythm of building anxiety followed by cathartic relief.

**Tension Sources:**
- Venturing into hostile waters with valuable cargo
- Spotting enemy contacts on the horizon
- Taking hull damage that threatens extraction
- Fuel/ammunition running low far from safety
- Crew casualties reducing combat effectiveness

**Release Moments:**
- Successful return to friendly port
- Securing valuable loot to ship inventory
- Completing difficult objectives
- Surviving against overwhelming odds
- Leveling up crew or ships after extraction

**Implementation Philosophy**: The extraction mechanics are the core tension generator. Nothing is safe until you dock at friendly port. Even a dominant victory means nothing if you sink on the way home.

### 2. Mastery & Growth
**Design Goal**: Create deep skill expression and visible progression.

**Mastery Dimensions:**
- **Tactical Mastery**: Reading situations, positioning, timing attacks
- **Ship Knowledge**: Understanding strengths/weaknesses of all vessels
- **Crew Management**: Optimizing crew assignments and skills
- **Economic Mastery**: Trading, looting priorities, resource management
- **Political Acumen**: Navigating multi-nation diplomacy and reputation

**Progression Visibility:**
- Unlock higher tier ships (1-10)
- Develop specialized crew with unique skills
- Build reputation across multiple nations
- Accumulate rare modules and equipment
- Earn recognition from other players

**Long-Term Goals**: Players should always have meaningful objectives:
- Short-term: Complete next expedition successfully
- Medium-term: Acquire specific ship or module
- Long-term: Master Tier 10 ships, dominate server politics

### 3. Meaningful Loss
**Design Goal**: Make losses sting to make victories rewarding.

**What Players Can Lose:**
- Ships (Tier 6-10 permadeath)
- Crew members (escalating casualty chances)
- Valuable cargo and loot
- Reputation with nations
- Time investment in failed expeditions

**Why Loss Matters:**
- **Stakes**: Without real loss, victories feel hollow
- **Drama**: Close calls and desperate survival create stories
- **Learning**: Losses teach better tactics and risk management
- **Community**: Shared losses bond players and squadrons
- **Respect**: Players who achieve greatness despite permadeath earn genuine admiration

**Balancing Philosophy**: Loss should never feel arbitrary or unfair. Players should always understand what went wrong and how to improve. The permadeath system is graduated (Tiers 1-5 safe, 6-9 escalating permadeath risk, 10 guaranteed loss) so players opt into appropriate risk levels.

### 4. Earned Respect
**Design Goal**: Reputation should reflect skill, not just time investment.

**How Respect is Earned:**
- Surviving high-tier expeditions consistently
- Executing brilliant tactical victories
- Building successful squadrons and alliances
- Accumulating rare ships and crews despite permadeath
- Contributing to server politics and economy
- Teaching and mentoring newer captains

**Anti-Patterns We Avoid:**
- Pay-to-win mechanics that bypass skill
- Time-based rewards that don't require mastery
- Participation trophies that diminish achievement
- Guaranteed progression that removes challenge

**Implementation**: The permadeath system ensures that high-tier accomplishments are genuinely impressive. A captain with multiple Tier 9-10 ships has survived real danger, not just ground hours.

### 5. Historical Immersion
**Design Goal**: Make players feel connected to WWII naval history.

**Immersion Elements:**
- Authentic ship designs and specifications
- Historical weapons, modules, and equipment
- Accurate geographic theaters (Pacific, Atlantic, Mediterranean)
- Period-appropriate UI and communication systems
- Famous ships and naval battles as reference points

**Narrative Framework:**
- Players fight alongside historical vessels
- Battles occur in famous locations (Pearl Harbor, Midway, etc.)
- Multi-nation dynamics reflect historical alliances/conflicts
- Technology progression follows WWII timeline (1939-1945)

**Accessibility Balance**: Historical accuracy should enhance immersion without creating barriers to entry. We prioritize:
- **Authentic feel** over rigid simulation
- **Tactical gameplay** over perfect physics
- **Player stories** over scripted narratives
- **Accessible interface** over overwhelming complexity

---

## Session Arc Design

### Typical Session Structure (60-90 minutes)

**Phase 1: Planning & Anticipation (0-5 minutes)**
- Review available ships and crew
- Select expedition objectives (economic, combat, exploration)
- Load ammunition, fuel, supplies
- Plan routes through contested waters
- **Emotional State**: Excitement, anticipation, strategic thinking

**Phase 2: Hunting & Opportunity (5-25 minutes)**
- Navigate toward objectives
- Scan radar for contacts
- Assess targets and threats
- Position for optimal engagement
- Manage fuel and ammunition reserves
- **Emotional State**: Tension building, tactical awareness, opportunity assessment

**Phase 3: Combat Execution (25-40 minutes)**
- Engage enemy vessels or resource points
- Execute tactical maneuvers
- Manage damage control and crew
- Acquire loot and cargo
- Evaluate extraction feasibility
- **Emotional State**: Adrenaline, focus, tactical execution, risk calculation

**Phase 4: Extraction Under Pressure (40-70 minutes)**
- Navigate toward friendly port with cargo
- Evade or fight pursuing enemies
- Manage damaged systems and casualties
- Deal with fuel/ammunition scarcity
- Final approach to safe harbor
- **Emotional State**: Maximum tension, anxiety, desperate survival

**Phase 5: Victory & Progression (70-80 minutes)**
- Secure cargo at friendly port
- Sell loot and resources
- Repair ship and heal crew
- Upgrade modules and skills
- Plan next expedition
- **Emotional State**: Relief, triumph, satisfaction, planning excitement

### Session Flexibility
Unlike session-based games, Fathoms Deep allows:
- **Safe logout** in friendly ports or designated safe zones
- **Flexible time commitment** (30-minute quick raids to 3-hour epic expeditions)
- **Persistent progress** that survives logouts
- **Asynchronous squadron coordination** for players with different schedules

---

## Genre & Style

### Primary Genre
**Naval Combat MMO / Tactical Strategy**

Core gameplay loop focused on:
- Tactical positioning and maneuvering
- Resource management (ammunition, fuel, supplies)
- Risk assessment and decision-making
- Multi-ship coordination in squadron play

### Secondary Elements
- **Extraction Shooter**: Nothing secured until return to port
- **Survival**: Limited resources, permadeath threat
- **RPG Progression**: Crew skills, ship unlocks, reputation systems
- **Player-Driven Economy**: Trading, looting, resource gathering

### Art Style

**Visual Direction:**
- **Perspective**: 2D top-down isometric view for tactical clarity
- **Ship Detail**: Detailed, historically-accurate ship sprites with visible damage
- **UI Philosophy**: Clean, information-dense tactical interface inspired by naval charts
- **Color Palette**: Muted military colors (grays, blues, greens) with high-contrast tactical overlays
- **Historical Accuracy**: Ships, uniforms, equipment authentic to 1939-1945 period

**UI Mood:**
- Professional military aesthetic
- Chart-room/command center feeling
- Clear information hierarchy
- Minimal visual clutter during combat

### Mood & Tone

**Atmosphere:**
- Tense and methodical, punctuated by intense combat
- Serious military tone without being dour
- Respect for historical context
- Focus on player skill and mastery

**Pacing:**
- Slow-burn tension building to climactic moments
- Strategic planning phases alternate with action sequences
- Longer engagement windows than arcade shooters
- Time to think and execute tactics

**Narrative Approach:**
- Player-driven stories within historical framework
- Emergent narratives from multiplayer interactions
- Server politics and reputation create ongoing storylines
- Historical context provides background, not scripts

**Accessibility Philosophy:**
- Easy to learn, hard to master
- Scalable complexity (simple surface gameplay, deep optimization)
- Clear feedback systems for learning
- Forgiving low tiers, challenging high tiers

---

## Core Gameplay Pillars

### Pillar 1: Tactical Combat
**Philosophy**: Reward positioning, timing, and resource management over reflexes and twitch skills.

**Key Elements:**
- Turn-based or slow real-time combat (not arcade action)
- Line-of-sight and radar mechanics
- Ammunition types and penetration calculations
- Damage control and crew management
- Multi-domain warfare (air, surface, submarine)

### Pillar 2: Risk Management
**Philosophy**: Every expedition requires calculated risk assessment and meaningful choices.

**Key Elements:**
- Permadeath tier system (1-10 graduated risk)
- Cargo value vs. survival priority decisions
- Route planning through dangerous waters
- Supply management (fuel, ammunition, repairs)
- Reputation consequences for aggressive actions

### Pillar 3: Progression Systems
**Philosophy**: Multiple paths to mastery and accomplishment.

**Progression Dimensions:**
- **Economic**: Trading, resource gathering, market manipulation
- **Military**: Ship unlocks, module collection, combat mastery
- **Diplomatic**: Reputation with multiple nations, port access
- **Exploratory**: Map knowledge, optimal routes, hidden opportunities
- **Crew Development**: Skill trees, specializations, veteran crews

### Pillar 4: Social Dynamics
**Philosophy**: Multiplayer interactions create emergent gameplay and lasting stories.

**Social Systems:**
- Squadron/fleet coordination
- Server politics and nation diplomacy
- Trading networks and economic alliances
- Reputation systems affecting interactions
- Piracy and anti-piracy operations

---

## Design Philosophy Principles

### 1. Player Agency Over Scripted Content
Players create their own stories through meaningful choices. We provide the framework (persistent world, risk/reward systems, multiplayer dynamics) and let players fill it with emergent narrative.

### 2. Skill Expression at All Levels
From tactical positioning to economic optimization to political maneuvering, players should always have ways to demonstrate mastery and outplay others through knowledge and execution.

### 3. Consequences Create Meaning
Permadeath, reputation systems, and extraction mechanics ensure that player decisions have lasting impact. Victories matter because losses are possible.

### 4. Historical Authenticity Serves Gameplay
We respect WWII history and ship accuracy, but prioritize fun and tactical depth. Simulation detail should enhance gameplay, not constrain it.

### 5. Accessibility Through Graduated Challenge
Lower tiers should be forgiving and educational. Higher tiers should demand mastery. Players opt into appropriate challenge levels based on skill and risk tolerance.

### 6. Respect Player Time and Investment
While permadeath exists, players should never feel like their time was wasted. Even failed expeditions teach valuable lessons. Progression systems balance risk with meaningful advancement opportunities.

---

## Success Metrics

### Player Engagement
- **Average session length**: 60-90 minutes
- **Sessions per week**: 5-10 for engaged players
- **Player retention**: 40%+ after 30 days

### Emotional Resonance
- **Memorable moments**: Players share stories of dramatic extractions, losses, victories
- **Community bonding**: Squadrons form lasting relationships
- **Streamer appeal**: Tense gameplay creates compelling content

### Mastery Progression
- **Skill improvement visible**: Players clearly progress from Tier 1 to Tier 10
- **Build diversity**: Multiple viable approaches to ship and crew configuration
- **Meta evolution**: Player-discovered tactics and strategies

### Economic Health
- **Active trading**: Player-driven economy with dynamic pricing
- **Loot cycling**: Extraction mechanics ensure constant item circulation
- **Balanced risk/reward**: Higher-tier expeditions genuinely more profitable

---

## Cross-References
- [[Target-Audience]] - Who we're building this game for
- [[Competitive-Positioning]] - How we differentiate from competitors
- [[Extraction-Mechanics]] - Core gameplay loop implementation
- [[Permadeath-System]] - Risk/reward balance and tier progression
- [[Multi-Nation-Diplomacy]] - Server politics and reputation systems
- [[Session-Structure]] - Detailed session flow and pacing

---

## Future Enhancements
- **Narrative Events**: Historical scenarios and server-wide campaigns
- **Faction Warfare**: Guild vs. guild territory control
- **Advanced Diplomacy**: Player-negotiated treaties and alliances
- **Expanded Theaters**: Additional geographic regions and battles
- **Documentary Integration**: Educational content about WWII naval history

---

## Changelog
- **2025-11-17**: Initial document creation - extracted from GDD_Updated-1.md lines 20-159
