# Combat Overview - Multi-Domain Warfare System

**Document Type**: Combat System Design
**Status**: 📋 PLANNED (Phase 2 Priority)
**Tags**: [planned, phase2, combat-systems, multi-domain]
**Priority**: HIGH
**Last Updated**: 2025-01-17

---

## Document Purpose

This document provides a high-level overview of Fathoms Deep's multi-domain combat philosophy, covering the integration of surface warfare, carrier air operations, and submarine combat into a cohesive extraction-based naval combat system.

---

## Core Combat Philosophy

Combat in Fathoms Deepbalances **accessibility** (assisted targeting, clear feedback) with **mastery** (manual aiming, module optimization, tactical positioning). The hybrid damage model rewards both precision shooting (critical hits, module damage) and sustained pressure (HP attrition). Multi-domain warfare creates rock-paper-scissors dynamics where submarines threaten battleships, destroyers hunt submarines, and aircraft strike all surface vessels.

### Design Principles

**Extraction-Based Tension**:
- Every combat engagement is a risk/reward calculation
- Death means potential loss of valuable cargo and modules
- Players must decide when to fight and when to flee
- Successful extraction requires tactical awareness and resource management

**Multi-Domain Integration**:
- Surface ships engage in gun and torpedo duels
- Carriers project air power across hundreds of kilometers
- Submarines hunt from stealth, threatening high-value targets
- Each domain has unique mechanics but integrates seamlessly

**Skill-Based Progression**:
- New players can contribute with assisted targeting
- Advanced players master manual fire control for accuracy bonuses
- Tactical positioning and resource management separate skilled from casual players
- Crew specialization and ship optimization provide depth

---

## Multi-Domain Combat Roles

### Surface Vessels - Gun and Torpedo Combat

#### **Aircraft Carriers** - Mobile Airbases
**Operational Philosophy**: Project air power across vast oceanic distances, control air superiority

- **Example Ships**: USS Essex, HMS Ark Royal, IJN Shokaku, KMS Graf Zeppelin
- **Primary Armament**: 50-100+ aircraft in multiple squadrons
- **Secondary Armament**: AA guns, limited surface weapons
- **Tactical Role**: Stay 50-100km from surface combat, launch coordinated air strikes
- **Vulnerability**: Massive target, minimal armor, catastrophic if sunk
- **Crew Requirements**: 200+ crew members, specialized aviation personnel
- **Example Operation**: USS Enterprise launches 24 dive bombers and 18 torpedo bombers against Japanese fleet at 80km range while defended by 36 fighters

#### **Battleships** - Heavy Assault Platforms
**Operational Philosophy**: Deliver overwhelming firepower, tank massive damage, dominate surface engagements

- **Example Ships**: USS Iowa, HMS King George V, IJN Yamato, KMS Bismarck
- **Primary Armament**: 6-9 guns (14"-18" caliber), devastating long-range firepower
- **Secondary Armament**: 8-20 medium guns (5"-8"), extensive AA suite
- **Tactical Role**: Anchor battle lines, engage enemy capital ships, shore bombardment
- **Strengths**: Massive armor, enormous firepower, intimidation factor
- **Crew Requirements**: 150-200 crew, specialized gunnery teams
- **Example Engagement**: KMS Bismarck engages HMS Hood at 22km range - single salvo penetrates magazine, causing catastrophic explosion

#### **Heavy Cruisers** - Balanced Combat Platforms
**Operational Philosophy**: Independent operations, convoy escort, cruiser warfare

- **Example Ships**: USS Baltimore, HMS Kent, IJN Takao, KMS Admiral Hipper
- **Primary Armament**: 6-9 guns (8"-10" caliber), excellent range and accuracy
- **Secondary Armament**: 6-12 medium guns (5"-6"), torpedo tubes, AA guns
- **Tactical Role**: Long-range patrol, escort duties, independent raids
- **Balance**: Good armor, speed, firepower - no major weaknesses
- **Crew Requirements**: 100-150 crew, versatile specialists
- **Example Mission**: HMS Kent escorts convoy through U-boat infested waters, engages surface raiders while directing destroyer screen

#### **Light Cruisers** - Fast Multi-Role Platforms
**Operational Philosophy**: Fast response, anti-destroyer work, squadron leadership

- **Example Ships**: USS Atlanta, HMS Dido, IJN Sendai, KMS Leipzig
- **Primary Armament**: 8-16 guns (5"-6" caliber), high rate of fire
- **Secondary Armament**: Torpedo tubes, extensive AA capability
- **Tactical Role**: Destroyer leader, AA escort, fast reconnaissance
- **Advantages**: High speed, rapid-fire guns, excellent AA protection
- **Crew Requirements**: 75-125 crew, emphasis on fire control

#### **Destroyers** - Fast Attack & Anti-Submarine
**Operational Philosophy**: Torpedo attacks, submarine hunting, escort screening

- **Example Ships**: USS Fletcher, HMS Tribal, IJN Fubuki, KMS Z-23
- **Primary Armament**: 4-6 guns (4"-5" caliber), 6-12 torpedo tubes
- **Secondary Armament**: Depth charges, sonar, AA guns
- **Tactical Role**: Torpedo runs, sub hunting, convoy escort, smoke screens
- **Capabilities**: Highest speed, stealth torpedo attacks, ASW operations
- **Crew Requirements**: 50-75 crew, emphasis on torpedo and sonar specialists
- **Example Tactic**: USS Fletcher makes high-speed torpedo run against Japanese cruiser column under cover of smoke screen

---

### Submarine Warfare - Stealth Operations

#### **Attack Submarines** - Stealth Commerce Raiders
**Operational Philosophy**: Unseen predator, strike from stealth, disrupt enemy supply lines

- **Example Ships**: USS Gato (T4), HMS T-class (T4), IJN I-400 (T5-T6), KMS U-boat Type VII (T4)
- **Primary Armament**: 6-10 torpedo tubes, 10-24 torpedo capacity
- **Secondary Armament**: Deck gun (88mm-127mm), AA guns
- **Tactical Role**: Commerce raiding, fleet screening, special operations
- **Stealth Advantage**: Nearly undetectable when submerged properly
- **Crew Requirements**: 40-80 crew, specialized submarine operations
- **Example Hunt**: U-552 (T4 Type VII) stalks British convoy for 6 hours, positions for perfect torpedo spread, sinks 3 merchants before diving deep to escape destroyers

#### **Fleet Submarines** - Long-Range Strategic Platforms
**Operational Philosophy**: Extended operations far from base, strategic reconnaissance

- **Example Ships**: USS Balao, IJN I-class, KMS U-boat Type IX
- **Enhanced Capabilities**: Extended range, larger torpedo load, advanced sensors
- **Special Operations**: Mine laying, commando insertion, intelligence gathering
- **Example Mission**: USS Wahoo penetrates Japanese harbor, plants mines, conducts reconnaissance, evades multiple patrol boats during extraction

---

### Carrier Aviation - Projected Power

#### **Fighter Aircraft** - Air Superiority
**Operational Philosophy**: Control airspace, intercept enemy aircraft, escort friendly strikes

- **Example Aircraft**: F6F Hellcat, Spitfire Seafire, A6M Zero, Bf 109T
- **Primary Role**: Dogfighting, bomber interception, CAP (Combat Air Patrol)
- **Armament**: Machine guns, cannons, limited bomb capacity
- **Tactical Usage**: Establish air superiority before bomber strikes
- **Example Engagement**: 12 Hellcats intercept 18 Zero escort fighters, clearing path for torpedo bomber attack

#### **Dive Bombers** - Precision Strike Aircraft
**Operational Philosophy**: Accurate attacks on enemy ships, precision targeting

- **Example Aircraft**: SBD Dauntless, Ju 87 Stuka, D3A Val
- **Primary Role**: Anti-ship strikes, precision bombing
- **Armament**: 1000-1600lb bombs, defensive machine guns
- **Attack Pattern**: High altitude approach, steep diving attack, pull-out
- **Example Attack**: 18 Dauntless dive bombers attack Japanese carrier Akagi, 3 direct hits cause fatal damage

#### **Torpedo Bombers** - Ship Killers
**Operational Philosophy**: Devastating low-level attacks, coordinated strikes

- **Example Aircraft**: TBF Avenger, Swordfish, B5N Kate, He 111
- **Primary Role**: Anti-ship torpedo attacks, level bombing
- **Armament**: Aerial torpedoes, mines, heavy bombs
- **Attack Pattern**: Low-level approach, torpedo drop at close range
- **Vulnerability**: Slow, vulnerable to fighters and AA fire
- **Example Strike**: 24 Avengers coordinate with dive bombers, simultaneous attack overwhelms enemy AA defenses

---

## Multi-Domain Integration Examples

### Scenario 1: Carrier Task Force vs. Battleship Squadron
**Force Composition**: USS Enterprise (CV) + 2 cruisers vs. KMS Tirpitz (BB) + 3 destroyers

**Tactical Execution**:
1. Enterprise launches 60 aircraft while staying 80km away
2. Tirpitz uses AA fire and fighter CAP to defend
3. Cruisers provide additional AA support and surface backup
4. Destroyers attempt torpedo runs if aircraft penetrate defenses

**Key Decision Points**:
- Carrier must maintain safe distance while controlling aircraft
- Battleship must prioritize AA defense vs. surface engagement
- Cruisers balance air defense with anti-torpedo screening
- Destroyers risk exposure for high-value torpedo attacks

---

### Scenario 2: Submarine Wolf Pack vs. Convoy
**Force Composition**: 3 German U-boats vs. 8 merchant ships + 4 escort destroyers

**Tactical Execution**:
1. U-boats coordinate positions around convoy route
2. Lead boat makes contact, shadows while others position
3. Simultaneous attack from multiple directions
4. Escorts respond with depth charges while merchants scatter

**Key Decision Points**:
- Wolf pack must maintain coordination without revealing position
- Convoy escorts must protect high-value targets while hunting submarines
- Merchants must balance escape speed with formation discipline
- U-boats must extract before reinforcements arrive

---

### Scenario 3: Large-Scale War Zone Operations
**Scale**: Dynamic 100+ player battles during Japan-USA war state

**Operational Dynamics**:
- No player limits - battles can involve 100+ ships simultaneously
- Players join/leave combat freely based on personal goals
- Core game loop unchanged - hunt, fight, extract valuable loot
- Nations generate diversionary missions to reduce server load:
  - "Raid Australian supply convoys 500km south"
  - "Intercept German commerce raiders in Atlantic"
  - "Mine laying operations near enemy ports"

**Strategic Choices**:
- Players choose: join massive battle for glory/risk or pursue profitable side missions
- Server management through mission distribution, not artificial caps
- Example: 80 players fighting over valuable wreck site while 40 others pursue scattered resource/convoy missions

---

## Combat Flow: Engagement to Extraction

### Phase 1: Detection & Approach
**Initial Contact**:
- Visual detection (ship silhouettes)
- Radar contact (electronic detection)
- Sonar contact (submarine warfare)
- Aircraft spotting (carrier reconnaissance)

**Decision Point**: Engage or Avoid?
- Assess enemy strength vs. your capabilities
- Consider cargo value and permadeath risk
- Evaluate escape routes and reinforcement possibilities

---

### Phase 2: Engagement
**Surface Combat**:
- Gunnery duels with predictive targeting
- Torpedo launches for devastating damage
- Module damage reduces combat effectiveness
- Fire and flooding threaten ship survival

**Air Combat**:
- Fighter sweeps clear enemy aircraft
- Bomber strikes coordinate for maximum damage
- AA defenses protect capital ships
- Aircraft attrition affects carrier effectiveness

**Submarine Combat**:
- Stealth positioning for optimal torpedo angle
- Depth management to avoid detection
- Resource conservation (battery, air, torpedoes)
- Evasion after attack to survive counterattack

---

### Phase 3: Damage Control & Adaptation
**System Failures**:
- Turrets destroyed reduce firepower
- Engine damage limits maneuverability
- Fire control damage reduces accuracy
- Flooding threatens ship stability

**Tactical Adaptation**:
- Crew reassignment to functional systems
- Emergency repairs restore partial capability
- Formation changes to protect damaged vessels
- Retreat decisions based on survivability assessment

---

### Phase 4: Victory or Retreat
**Extraction Decisions**:
- Successful engagement: Collect loot, assess damage, plan safe extraction
- Failed engagement: Emergency retreat, jettison cargo if necessary, reach safe zone
- Partial success: Salvage what you can, minimize additional losses

**Post-Combat Risks**:
- Damaged ships vulnerable to opportunistic attacks
- Limited ammunition restricts defensive capability
- Reduced speed makes extraction dangerous
- Permadeath zones make damaged ships high-risk targets

---

## Rock-Paper-Scissors Dynamics

### Submarines Threaten Battleships
**Asymmetric Advantage**:
- Submarines fire devastating torpedoes from stealth
- Battleships too slow to effectively evade
- Limited depth charge capability on capital ships
- Single torpedo spread can cripple or sink battleship

**Counterplay**:
- Battleship escort destroyers provide ASW screening
- Active sonar detection reveals submarine positions
- Zigzag patterns complicate torpedo solutions
- Shallow water limits submarine depth advantage

---

### Destroyers Hunt Submarines
**Hunter-Killer Advantage**:
- High speed allows rapid response to contacts
- Depth charges devastate submarines
- Advanced sonar detects submerged threats
- Maneuverability allows precise depth charge placement

**Counterplay**:
- Submarines dive deep to evade depth charges
- Silent running reduces detection range
- Torpedo counterstrike before diving
- Use thermal layers to break sonar contact

---

### Aircraft Strike All Surface Vessels
**Air Power Superiority**:
- Carriers strike from beyond gun range
- Bombers overwhelm AA defenses with coordinated attacks
- Torpedo bombers devastate even battleships
- Fighters intercept enemy aircraft

**Counterplay**:
- Concentrated AA fire damages attacking aircraft
- Fighter CAP intercepts bombers before attack
- Evasive maneuvering reduces hit probability
- Shoot down carrier aircraft to deplete resource pool

---

### Cruisers Balance All Threats
**Versatility Advantage**:
- Good AA defenses vs aircraft
- Speed and firepower vs destroyers
- Torpedoes threaten battleships
- Sonar capability vs submarines

**Weakness**:
- No overwhelming advantage in any domain
- Vulnerable to focused attacks
- Medium armor penetrated by battleship AP
- Citadel vulnerability to precise strikes

---

## Tier-Based Combat Scaling

### T1-T5: Learning Phase (0% Ship/Crew Card Permadeath)
**Combat Characteristics**:
- Forgiving mechanics allow experimentation
- Basic weapon systems with simple interfaces
- Slower pace allows tactical learning
- Full ship/crew card recovery on death encourages aggressive learning
- Sailor casualties occur but are replaceable

**Focus Areas**:
- Basic gunnery and torpedo mechanics
- Damage control fundamentals
- Formation tactics and positioning
- Resource management basics
- Crew card leveling without permadeath risk

---

### T6-T7: First Permadeath Tiers (10-20% Ship/Crew Card Permadeath)
**Combat Characteristics**:
- Standard WWII-era technology
- Balanced capabilities across all ship classes
- Meaningful ship/crew card permadeath risk begins at T6
- Economic viability requires successful engagements
- Insurance becomes important consideration

**Focus Areas**:
- Advanced gunnery with manual fire control
- Multi-domain coordination
- Crew card specialization optimization
- Risk management and extraction planning
- Backup crew card development

---

### T8-T9: Elite Operations (40-60% Ship/Crew Card Permadeath)
**Combat Characteristics**:
- Advanced late-war and post-war technology
- Superior sensors and fire control systems
- Very high ship/crew card permadeath risk creates extreme tension
- Every engagement is calculated risk/reward
- Elite assets genuinely at risk

**Focus Areas**:
- Perfect execution required for survival
- Elite crew card coordination and specialization
- Advanced tactical maneuvers
- Strategic resource conservation
- Asset preservation strategies

---

### T10: Apex Combat (100% Ship/Crew Card Permadeath - GUARANTEED LOSS)
**Combat Characteristics**:
- Ultimate capabilities across all systems
- Server-wide alerts when T10 ships engage
- Catastrophic economic loss on death
- Strategic deterrence through reputation alone

**Focus Areas**:
- Flawless tactical execution
- Server-level strategic impact
- Ultimate resource optimization
- Risk avoidance through superior intelligence

---

## Combat Feedback Systems

### Visual Feedback
**Hit Indicators**:
- Shell splashes show near misses
- Hit markers indicate successful strikes
- Critical hit effects show module damage
- Fire and flooding animations display ongoing damage

**Damage States**:
- Turrets visibly destroyed when disabled
- Smoke from damaged modules
- List and flooding visual effects
- Aircraft crash and explosion effects

---

### Audio Feedback
**Combat Sounds**:
- Shell impacts with varying intensity
- Explosion sounds scaled to damage
- Crew voice lines report critical events
- Warning klaxons for flooding/fire

**Ambient Audio**:
- Engine sounds indicate ship condition
- Aircraft engine sounds for air operations
- Sonar pings and torpedo warnings
- Radio communications for coordination

---

### UI Feedback
**Damage Display**:
- HP bar shows total ship health
- Module status indicators
- Ammunition counters
- Resource gauges (fuel, battery, air)

**Tactical Information**:
- Minimap shows detected contacts
- Range indicators for weapons
- Fire control solutions
- Torpedo trajectories

---

## Combat Balancing Principles

### Fair Combat
**Player vs Player**:
- Same damage models for all players
- No artificial stat advantages
- Tier matchmaking prevents seal clubbing
- Skill-based progression rewards mastery

**Player vs NPC**:
- NPCs use identical systems as players
- Difficulty through equipment and tactics
- Learnable AI patterns
- Consistent damage calculations

---

### Asymmetric Warfare
**Ship Class Balance**:
- Every class has strengths and weaknesses
- No single "best" ship class
- Combined arms doctrine encouraged
- Solo and group play both viable

**Tactical Depth**:
- Manual control provides accuracy bonuses
- Module optimization creates specializations
- Crew stats (7-50 system) enhance capabilities: Accuracy, Reload, Repair Speed, Fire Fighting, etc.
- Positioning and tactics matter more than raw stat numbers

---

## Cross-Reference Documents

**Detailed System Documents**:
- [Surface-Combat.md](Surface-Combat.md) - Complete surface warfare mechanics
- [Carrier-Operations.md](Carrier-Operations.md) - Full air warfare system
- [Submarine-Warfare.md](Submarine-Warfare.md) - Depth mechanics and stealth combat
- [Damage-Model.md](Damage-Model.md) - Penetration and critical hit systems

**Related Systems**:
- Ship Progression System (GDD Core)
- Crew Management System (GDD Core)
- Module Customization System (GDD Core)
- Extraction and Permadeath System (GDD Core)

---

## Implementation Priority

**Phase 2 Development Focus**:
1. Core damage model implementation
2. Basic gunnery and torpedo mechanics
3. Multi-domain threat integration
4. Combat feedback systems
5. Balance testing and iteration

**Critical Success Factors**:
- Accessible to new players, rewarding for veterans
- Distinct feel for each combat domain
- Meaningful consequences create tension
- Extraction-based gameplay drives all combat decisions
