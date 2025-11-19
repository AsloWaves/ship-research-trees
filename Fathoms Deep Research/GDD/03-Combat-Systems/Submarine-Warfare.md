# Submarine Warfare System

**Document Type**: Combat System Design
**Status**: 📋 PLANNED (Phase 2 Priority)
**Tags**: [planned, phase2, combat-systems, submarines, stealth, depth-mechanics]
**Priority**: HIGH
**Last Updated**: 2025-01-17

---

## Document Purpose

This document details the complete submarine warfare system for Fathoms Deep, covering depth mechanics in 2D, periscope operations, sonar systems, torpedo combat from depth, oxygen/battery management, and anti-submarine warfare (ASW) for surface ships.

---

## Submarine Warfare Philosophy

Stealth-based naval combat emphasizing patience, resource management, and precise positioning where one successful torpedo attack can change the course of battle, but detection means almost certain destruction.

**Core Principles**:
- **Patience Over Aggression**: Hours of stalking for minutes of action
- **Resource Conservation**: Every action depletes limited battery, air, and torpedo resources
- **3D Positioning Mastery**: Horizontal movement + depth control creates complex tactical space
- **High Risk/High Reward**: One submarine can sink ships worth 10x its value
- **Asymmetric Warfare**: Weakest in direct confrontation, deadliest from ambush

---

## Submarine Tier Progression & Class Differentiation

### Unlock Requirements

- **Prerequisite**: T4 Destroyer completion + 75,000 credits + Advanced Underwater Warfare Certification
- **Reasoning**: Submarines require mastery of 3D positioning, patience, and resource management that builds on destroyer fundamentals
- **Entry Barrier**: Moderate - prevents inexperienced players from accessing high-risk stealth warfare

---

## Complete Submarine Line: T1-T10 Progression

The submarine line progresses through three distinct class categories, each with unique tactical roles and operational characteristics. Unlike surface ships that differentiate into multiple parallel lines, submarines follow a single unified progression that evolves from coastal defense to oceanic predator.

---

### T1-T3: Coastal Submarines (SS) - Learning Phase

**Primary Role**: Coastal defense, harbor operations, submarine fundamentals

#### **T1: Early Coastal Submarine**
- **Historical Examples**: USS S-1 (SS-105), HMS H-class, Type UB-I
- **Crew**: 20-25 sailors
- **Displacement**: 150-300 tons surfaced
- **Speed**: 10 knots surfaced, 5 knots submerged
- **Range**: 50-100km operational radius from base
- **Dive Depth**: Maximum 50 meters
- **Armament**: 2-3 torpedo tubes, 4-6 torpedoes total
- **Endurance**: 24-48 hours submerged (battery limitations)
- **Death Penalty**: 0% permadeath - full ship recovery on death
- **Unlock Cost**: 15,000 credits
- **Operational Focus**: Basic dive/surface mechanics, torpedo fundamentals, short-range patrols

#### **T2: Improved Coastal Submarine**
- **Historical Examples**: USS S-42 (SS-153), HMS L-class, Type UB-III
- **Crew**: 25-30 sailors
- **Displacement**: 300-500 tons surfaced
- **Speed**: 12 knots surfaced, 6 knots submerged
- **Range**: 100-150km operational radius
- **Dive Depth**: Maximum 60 meters
- **Armament**: 4 torpedo tubes, 8-10 torpedoes total
- **Endurance**: 48-72 hours submerged
- **Death Penalty**: 0% permadeath
- **Unlock Cost**: 30,000 credits
- **Operational Focus**: Extended operations, multiple target engagements, depth control mastery

#### **T3: Advanced Coastal Submarine**
- **Historical Examples**: USS Barracuda (SS-163), HMS Porpoise-class, Type II
- **Crew**: 30-35 sailors
- **Displacement**: 500-800 tons surfaced
- **Speed**: 14 knots surfaced, 7 knots submerged
- **Range**: 150-250km operational radius
- **Dive Depth**: Maximum 80 meters
- **Armament**: 4-6 torpedo tubes, 12-14 torpedoes total
- **Endurance**: 72-96 hours submerged
- **Death Penalty**: 0% permadeath
- **Unlock Cost**: 60,000 credits
- **Operational Focus**: Transition to fleet operations, convoy harassment, extended patrols

**Coastal Submarine Characteristics**:
- **Tactical Role**: Harbor defense, short-range patrols, training platforms
- **Strengths**: Low cost, fast construction, minimal crew requirements, forgiving gameplay
- **Weaknesses**: Limited range, shallow dive depth, small torpedo capacity, vulnerable in open ocean
- **Best Use**: T0-T2 zones, coastal defense, new submarine commanders learning mechanics
- **Economic Profile**: Cheap to build/operate, minimal resource risk, ideal for experimentation

---

### T4-T6: Fleet Submarines (SS) - Competitive Operations

**Primary Role**: Commerce raiding, convoy interdiction, long-range operations

#### **T4: Early Fleet Submarine** 🔓 *Unlocks Submarine Line Access*
- **Historical Examples**: USS Gato (SS-212), HMS Triton, Type VII
- **Crew**: 35-45 sailors
- **Displacement**: 1,000-1,500 tons surfaced
- **Speed**: 16 knots surfaced, 8 knots submerged
- **Range**: 400-600km operational radius
- **Dive Depth**: Maximum 100 meters
- **Armament**: 6 torpedo tubes (4 bow, 2 stern), 16-20 torpedoes total
- **Endurance**: 5-7 days submerged (with snorkeling)
- **Death Penalty**: 0% permadeath (final learning tier)
- **Unlock Cost**: 120,000 credits
- **Operational Focus**: Commerce warfare, convoy hunting, multi-day patrols

#### **T5: Standard Fleet Submarine**
- **Historical Examples**: USS Balao (SS-285), HMS Tiptoe, Type VII-C
- **Crew**: 45-55 sailors
- **Displacement**: 1,500-1,800 tons surfaced
- **Speed**: 18 knots surfaced, 9 knots submerged
- **Range**: 600-800km operational radius
- **Dive Depth**: Maximum 120 meters
- **Armament**: 10 torpedo tubes (6 bow, 4 stern), 20-24 torpedoes total
- **Endurance**: 7-10 days submerged
- **Death Penalty**: 0% permadeath
- **Unlock Cost**: 250,000 credits
- **Operational Focus**: Extended commerce raiding, fleet reconnaissance, wolfpack operations

#### **T6: Advanced Fleet Submarine** ⚠️ *Permadeath Risk Begins*
- **Historical Examples**: USS Tench (SS-417), HMS Acheron, Type IX-C
- **Crew**: 55-65 sailors
- **Displacement**: 1,800-2,200 tons surfaced
- **Speed**: 20 knots surfaced, 10 knots submerged
- **Range**: 800-1,200km operational radius
- **Dive Depth**: Maximum 150 meters
- **Armament**: 10 torpedo tubes, 24-28 torpedoes total, deck gun option
- **Endurance**: 10-14 days submerged
- **Death Penalty**: 10% ship/crew card permadeath - first permadeath tier
- **Unlock Cost**: 500,000 credits
- **Operational Focus**: Long-range interdiction, strategic chokepoint denial, high-value target hunting

**Fleet Submarine Characteristics**:
- **Tactical Role**: Commerce warfare, convoy interdiction, fleet screening, reconnaissance
- **Strengths**: Extended endurance, significant torpedo capacity, moderate speed, operational flexibility
- **Weaknesses**: Larger detection signature than coastal subs, higher operating costs, slower dive times
- **Best Use**: T2-T4 zones, convoy routes, strategic chokepoints, wolfpack operations
- **Economic Profile**: Moderate construction costs, significant operating expenses, profitable commerce raiding

---

### T7-T9: Attack Submarines (SSA) - Elite Predators

**Primary Role**: Capital ship hunting, strategic operations, high-stakes combat

#### **T7: Early Attack Submarine**
- **Historical Examples**: USS Tang (SS-563), HMS Dreadnought, Type XXI
- **Crew**: 65-75 sailors
- **Displacement**: 2,200-2,500 tons surfaced
- **Speed**: 22 knots surfaced, 12 knots submerged
- **Range**: 1,200-1,600km operational radius
- **Dive Depth**: Maximum 200 meters
- **Armament**: 8-10 torpedo tubes, 28-32 torpedoes, advanced fire control
- **Endurance**: 14-21 days submerged
- **Death Penalty**: 20% ship/crew card permadeath
- **Unlock Cost**: 1,000,000 credits
- **Operational Focus**: Capital ship assassination, carrier hunting, extraction denial

#### **T8: Advanced Attack Submarine**
- **Historical Examples**: USS Nautilus (SSN-571 diesel concept), HMS Valiant, Type XXVI
- **Crew**: 75-85 sailors
- **Displacement**: 2,500-3,000 tons surfaced
- **Speed**: 24 knots surfaced, 14 knots submerged
- **Range**: 1,600-2,000km operational radius
- **Dive Depth**: Maximum 250 meters
- **Armament**: 10 torpedo tubes, 32-36 torpedoes, guided torpedo capability
- **Endurance**: 21-30 days submerged
- **Death Penalty**: 40% ship/crew card permadeath
- **Unlock Cost**: 2,500,000 credits
- **Operational Focus**: Strategic interdiction, extraction route domination, fleet-killer operations

#### **T9: Elite Attack Submarine**
- **Historical Examples**: Advanced diesel-electric concepts, Project 611/613 equivalents
- **Crew**: 85-95 sailors
- **Displacement**: 3,000-3,500 tons surfaced
- **Speed**: 26 knots surfaced, 16 knots submerged
- **Range**: 2,000-2,500km operational radius
- **Dive Depth**: Maximum 300 meters
- **Armament**: 12 torpedo tubes, 36-40 torpedoes, advanced acoustic homing
- **Endurance**: 30-45 days submerged
- **Death Penalty**: 60% ship/crew card permadeath
- **Unlock Cost**: 5,000,000 credits
- **Operational Focus**: Strategic denial, capital ship elimination, server-level threat

**Attack Submarine Characteristics**:
- **Tactical Role**: Capital ship hunting, strategic chokepoint control, extraction denial, fleet elimination
- **Strengths**: Superior speed, deep diving capability, massive torpedo capacity, advanced sensors
- **Weaknesses**: Enormous construction costs, high crew requirements, major economic loss on death
- **Best Use**: T4-T5 zones, capital ship ambush, extraction routes, high-stakes operations
- **Economic Profile**: Extremely expensive, high-risk/high-reward gameplay, server-defining presence

---

### T10: Ultimate Submarine (SSA) - Apex Predator 💀 *FULL PERMADEATH*

#### **T10: Strategic Attack Submarine**
- **Historical Examples**: Hypothetical advanced designs, nuclear concepts adapted to diesel-electric
- **Crew**: 95-110 sailors
- **Displacement**: 3,500-4,000 tons surfaced
- **Speed**: 28 knots surfaced, 18 knots submerged
- **Range**: 2,500+ km operational radius (limited only by supplies)
- **Dive Depth**: Maximum 350 meters (crush depth gameplay at 400m)
- **Armament**: 12-14 torpedo tubes, 40-50 torpedoes, guided/homing torpedoes, advanced mine-laying
- **Endurance**: 45-60 days submerged
- **Death Penalty**: 100% FULL PERMADEATH - ship, crew, and all equipment permanently lost
- **Unlock Cost**: 10,000,000+ credits
- **Construction Time**: 250-300 hours real-time (can be accelerated with resources)
- **Operational Focus**: Strategic dominance, server control, extraction denial, capital ship elimination

**T10 Unique Capabilities**:
- **Server-Wide Detection Alerts**: When a T10 submarine enters a zone, all players receive notifications
- **Strategic Impact**: Can single-handedly deny extraction routes or control strategic chokepoints
- **Ultimate Predator**: Capable of sinking any ship class including T10 carriers and battleships
- **Stealth Supremacy**: Nearly undetectable even to advanced ASW measures when properly operated
- **Economic Warfare**: Operating a T10 submarine is economic warfare - both for the operator and targets

**T10 Operational Reality**:
- Most T10 submarines spend weeks in port due to massive operating costs
- Deployment is a server-wide event that changes strategic calculations
- Losses are catastrophic - represents 300-500 hours of player investment
- Elite crews required - any mistake at this tier is likely permadeath
- Insurance systems inadequate - T10 submarines are uninsurable due to value

---

## Submarine Class Comparison Table

| Tier | Class Type | Example Ship | Crew | Torpedoes | Range | Dive Depth | Speed (Sub) | Death Risk | Best Use |
|------|------------|--------------|------|-----------|-------|------------|-------------|------------|----------|
| T1 | Coastal SS | USS S-1 | 20-25 | 4-6 | 50-100km | 50m | 5kt | 0% | Coastal defense, learning |
| T2 | Coastal SS | USS S-42 | 25-30 | 8-10 | 100-150km | 60m | 6kt | 0% | Extended coastal ops |
| T3 | Coastal SS | USS Barracuda | 30-35 | 12-14 | 150-250km | 80m | 7kt | 0% | Transition to fleet ops |
| T4 | Fleet SS | USS Gato | 35-45 | 16-20 | 400-600km | 100m | 8kt | 0% | Commerce warfare basics |
| T5 | Fleet SS | USS Balao | 45-55 | 20-24 | 600-800km | 120m | 9kt | 0% | Standard fleet operations |
| T6 | Fleet SS | USS Tench | 55-65 | 24-28 | 800-1,200km | 150m | 10kt | 10% | Long-range interdiction |
| T7 | Attack SSA | USS Tang | 65-75 | 28-32 | 1,200-1,600km | 200m | 12kt | 20% | Capital ship hunting |
| T8 | Attack SSA | USS Nautilus | 75-85 | 32-36 | 1,600-2,000km | 250m | 14kt | 40% | Strategic interdiction |
| T9 | Attack SSA | Advanced | 85-95 | 36-40 | 2,000-2,500km | 300m | 16kt | 60% | Fleet elimination |
| T10 | Attack SSA | Strategic | 95-110 | 40-50 | 2,500+ km | 350m | 18kt | 100% | Strategic dominance |

---

## Tier-Based Capability Scaling

### Stealth & Detection Scaling

#### **T1-T3: Basic Stealth** (Coastal Operations)
- **Surface Detection**: 8-12km range
- **Periscope Detection**: Visible to alert surface ships at 2-4km
- **Submerged Detection**: Hydrophone detection at 4-6km (active operations)
- **Dive Speed**: 90-120 seconds to periscope depth
- **Silent Running**: Reduces detection by 25-35%

#### **T4-T6: Standard Stealth** (Fleet Operations)
- **Surface Detection**: 10-14km range
- **Periscope Detection**: Visible to experienced observers at 1.5-3km
- **Submerged Detection**: Hydrophone detection at 3-5km (active operations)
- **Dive Speed**: 60-90 seconds to periscope depth
- **Silent Running**: Reduces detection by 35-50%

#### **T7-T9: Advanced Stealth** (Attack Operations)
- **Surface Detection**: 12-16km range
- **Periscope Detection**: Difficult to spot even at 1-2km
- **Submerged Detection**: Hydrophone detection at 2-4km (active operations)
- **Dive Speed**: 45-60 seconds to periscope depth
- **Silent Running**: Reduces detection by 50-65%

#### **T10: Ultimate Stealth** (Strategic Operations)
- **Surface Detection**: 14-18km range
- **Periscope Detection**: Nearly invisible unless actively searched
- **Submerged Detection**: Hydrophone detection at 1-3km (extremely difficult)
- **Dive Speed**: 30-45 seconds to periscope depth (emergency capability)
- **Silent Running**: Reduces detection by 65-80%

---

### Torpedo Effectiveness Scaling

#### **T1-T3: Basic Torpedoes**
- **Type**: Contact detonation only, unguided
- **Range**: 3-5km maximum
- **Speed**: 30-35 knots
- **Damage**: Effective against T1-T4 ships, limited against capital ships
- **Reload Time**: 180-240 seconds per tube
- **Accuracy**: Requires precise manual aiming, no fire control assistance

#### **T4-T6: Standard Torpedoes**
- **Type**: Contact and magnetic influence detonation
- **Range**: 5-8km maximum
- **Speed**: 35-40 knots
- **Damage**: Effective against T3-T7 ships, moderate against capital ships
- **Reload Time**: 120-180 seconds per tube
- **Accuracy**: Basic fire control computer assistance

#### **T7-T9: Advanced Torpedoes**
- **Type**: Pattern-running torpedoes, acoustic homing (late models)
- **Range**: 8-12km maximum
- **Speed**: 40-45 knots
- **Damage**: Effective against T5-T9 ships, significant capital ship threat
- **Reload Time**: 90-120 seconds per tube
- **Accuracy**: Advanced fire control, target motion analysis

#### **T10: Ultimate Torpedoes**
- **Type**: Acoustic homing, wire-guided, pattern-running
- **Range**: 12-15km maximum
- **Speed**: 45-50 knots
- **Damage**: Capable of sinking any ship class including T10 capital ships
- **Reload Time**: 60-90 seconds per tube
- **Accuracy**: Automated fire control, multi-target tracking, guided munitions

---

### Endurance & Resource Efficiency Scaling

#### **T1-T3: Limited Endurance**
- **Patrol Duration**: 1-2 game sessions (2-6 hours)
- **Battery Life**: 24-72 hours submerged (in-game time)
- **Air Supply**: 12-24 hours without surfacing
- **Resource Costs**: Minimal - cheap torpedoes, low fuel consumption
- **Resupply Frequency**: After every patrol

#### **T4-T6: Moderate Endurance**
- **Patrol Duration**: 2-4 game sessions (6-12 hours)
- **Battery Life**: 72-168 hours submerged
- **Air Supply**: 24-48 hours without surfacing
- **Resource Costs**: Moderate - standard torpedoes, reasonable fuel costs
- **Resupply Frequency**: Every 2-3 patrols

#### **T7-T9: Extended Endurance**
- **Patrol Duration**: 4-8 game sessions (12-24 hours)
- **Battery Life**: 168-360 hours submerged
- **Air Supply**: 48-96 hours without surfacing
- **Resource Costs**: High - advanced torpedoes, significant fuel consumption
- **Resupply Frequency**: Every 3-5 patrols (if they survive)

#### **T10: Strategic Endurance**
- **Patrol Duration**: 8-12+ game sessions (24-48+ hours)
- **Battery Life**: 360-720 hours submerged
- **Air Supply**: 96-144 hours without surfacing
- **Resource Costs**: Extreme - guided torpedoes, massive fuel consumption
- **Resupply Frequency**: Major logistics operation every successful patrol

---

## Submarine Progression Philosophy & Time Investment

### Complete Path to T10 Submarine (150-300 hours to T10 Attack Submarine)

**T1-T3: Coastal Submarine Foundation** (15-30 hours total)
- **T1**: 5-8 hours - Basic dive/surface, simple torpedo attacks
- **T2**: 5-10 hours - Depth control mastery, resource management basics
- **T3**: 5-12 hours - Extended operations, multi-target engagements

**T4-T6: Fleet Submarine Competency** (40-80 hours total)
- **T4**: 10-20 hours - Commerce warfare fundamentals, convoy hunting
- **T5**: 12-25 hours - Wolfpack coordination, extended patrols
- **T6**: 18-35 hours - High-stakes operations, permadeath risk introduction

**T7-T9: Attack Submarine Mastery** (60-120 hours total)
- **T7**: 20-40 hours - Capital ship hunting, strategic operations
- **T8**: 20-40 hours - Extraction denial, server-level impact
- **T9**: 20-40 hours - Elite predator status, major economic warfare

**T10: Strategic Submarine Achievement** (35-70 hours)
- **T10**: 35-70 hours - Server dominance, strategic influence, ultimate risk

**Additional Time Factors**:
- **Crew Training**: Additional 20-40 hours for elite crew development
- **Equipment Grinding**: 15-30 hours for advanced torpedo upgrades and sensors
- **Economic Preparation**: Time spent generating credits for construction costs
- **Loss Recovery**: Time spent rebuilding after permadeath losses (T6+)

---

### Submarine Unique Characteristics

**Asymmetric Warfare Specialists**:
- Submarines excel at attacking high-value targets with minimal risk (when played well)
- One successful torpedo spread can sink ships worth 10x the submarine's value
- Perfect for patient, tactical players who enjoy stealth gameplay
- Can deny entire zones through mere presence - psychological warfare

**High Skill Ceiling**:
- Mistakes are less forgiving than surface ships (detection often means death)
- Requires mastery of 3D positioning (horizontal movement + depth control)
- Resource management is critical (air, battery, fuel all constantly depleting)
- Rewards planning and patience over aggressive action
- Split-second decisions between attacking and escaping

**Extraction Denial Role**:
- Submarines are the ultimate extraction-phase threat
- Damaged surface ships are vulnerable to submarine ambushes during withdrawal
- Submarines can patrol extraction routes and hunt loaded cargo ships
- T8-T10 submarines in extraction corridors create server-wide tension
- Can wait submerged for hours near extraction zones

**Strategic Impact**:
- High-tier submarines change server meta - players alter routes to avoid submarine zones
- T9-T10 submarines can deny entire regions simply through presence
- Economic warfare specialists - forcing enemies to spend on ASW measures
- Intelligence gathering - passive sonar provides fleet movement data
- Server-defining presence at T10 - affects all strategic planning

---

## Advanced Depth Control Mechanics

### Three-Layer Depth Management System

**Reference Note**: The following detailed mechanics apply to ALL submarine tiers, but scale in complexity, capability, and consequence as tier increases. Examples throughout reference **T4-T6 submarines (mid-tier standards)** unless otherwise noted.

---

#### **Surface Operations**

**Operational Characteristics**:
- **Maximum Speed**: 18-22 knots depending on submarine class
- **Full Visibility**: 360° visual range, fog of war at normal distance
- **Vulnerability**: Exposed to all weapons - naval gunfire, aircraft bombs, ramming
- **Resource Benefits**: Automatic air replenishment, diesel engine battery charging
- **Detection Range**: Visible to all enemy units at maximum detection distances

**Surface Tactical Applications**:
- **High-Speed Transit**: Covering large distances quickly during safe periods
- **Emergency Escape**: Outrun slow surface ships when detected
- **Night Operations**: Reduced visual detection under darkness
- **Resource Replenishment**: Recharge critical systems during safe periods

---

#### **Torpedo Depth (Periscope Depth)**

**Operational Characteristics**:
- **Moderate Speed**: 8-12 knots, optimal balance of stealth and mobility
- **Limited Visibility**: Periscope-based observation with extended fog-of-war penetration
- **Partial Concealment**: Difficult aircraft detection, vulnerable to experienced surface observers
- **Combat Optimal**: Ideal depth for torpedo attacks and target acquisition
- **Detection Risk**: Periscope potentially visible to alert surface ships

**Periscope Depth Tactical Applications**:
- **Attack Runs**: Primary combat depth for torpedo launches
- **Target Observation**: Visual identification and tracking
- **Course Plotting**: Calculating firing solutions
- **Limited Exposure**: Balancing observation needs with stealth

---

#### **Deep Dive Operations**

**Operational Characteristics**:
- **Minimum Speed**: 3-6 knots, maximum stealth priority
- **Maximum Concealment**: Nearly undetectable to early-war aircraft and surface ships
- **Limited Combat**: Cannot fire torpedoes effectively, emergency depth only
- **High Resource Cost**: Increased battery consumption due to life support requirements
- **Emergency Depth**: Last resort when detected or under attack

**Deep Dive Tactical Applications**:
- **Evasion**: Escape from depth charge attacks
- **Stealth Transit**: Move through heavily patrolled areas undetected
- **Ambush Positioning**: Silent approach to intercept points
- **Survival**: Wait out surface ship searches

---

### Advanced Depth Change Mechanics & Tactical Applications

#### **Depth Transition Timing & Vulnerabilities**

**Diving Sequence** (Surface → Torpedo Depth):
- **Phase 1** (0-30 seconds): Ballast tanks flooding, submarine vulnerable to ramming
- **Phase 2** (30-60 seconds): Partial submersion, conning tower visible, artillery vulnerable
- **Phase 3** (60-90 seconds): Full submersion achieved, periscope depth attained
- **Emergency Dive**: 45-second sequence with increased noise signature

**Deep Diving Sequence** (Torpedo → Deep):
- **Standard Dive**: 120 seconds, silent running maintained
- **Emergency Deep Dive**: 60 seconds, high noise signature, emergency battery consumption
- **Tactical Considerations**: Cannot attack during transition, vulnerable window

---

### Depth Control Combat Scenarios

#### **Scenario 1: Emergency Dive Under Air Attack**
**Submarine**: U-552 (T4 Type VII fleet submarine) spotted by RAF Coastal Command at 12km range

**Emergency Response**:
1. **Detection**: Aircraft spotted approaching at high speed, bombs visible
2. **Immediate Response**: Emergency dive initiated, 45-second timer started
3. **Vulnerability Window**: Submarine partially submerged when bombs drop
4. **Near Miss**: Depth charges explode 50 meters away, minor hull damage
5. **Deep Dive**: Continue to maximum depth, wait for aircraft departure
6. **Tactical Result**: Escaped destruction, but battery drained to 60%, mission timing affected

---

#### **Scenario 2: Periscope Depth Attack Run**
**Submarine**: USS Drum (T5 Balao-class fleet submarine) approaching Japanese convoy at night

**Attack Sequence**:
1. **Approach Phase**: Surface speed 20 knots, close to 8km range
2. **Final Approach**: Dive to torpedo depth, reduce to 6 knots for stealth
3. **Target Acquisition**: Periscope sweep reveals 3 cargo ships + 2 destroyer escorts
4. **Attack Position**: Maneuver to intercept lead cargo ship's course
5. **Firing Solution**: Calculate torpedo spread for maximum damage probability
6. **Post-Attack**: Immediate deep dive to avoid destroyer depth charge attack

---

## Advanced Periscope Operations & Intelligence Gathering

### Periscope Risk/Reward Management

#### **Observation Window Mechanics**

**Periscope Exposure Levels**:
- **Quick Sweep** (5-10 seconds): Basic bearing information, minimal detection risk
- **Target Assessment** (15-30 seconds): Ship identification, course/speed estimate, moderate risk
- **Extended Observation** (30-60 seconds): Detailed intelligence, high detection risk
- **Continuous Surveillance** (60+ seconds): Maximum information, almost certain detection

---

### Advanced Intelligence Gathering

**Target Classification System**:
- **Silhouette Recognition**: Identify ship class by profile and superstructure
- **Speed Estimation**: Calculate target velocity by observation timing
- **Course Prediction**: Determine future position for torpedo firing solution
- **Escort Analysis**: Count and classify defensive ships, assess threat level
- **Formation Analysis**: Understand convoy organization and protective screen

#### **Intelligence Gathering Example: U-99 Shadowing British Convoy**
**Scenario**: Night convoy observation, maintaining 6km distance

**Intelligence Collection**:
1. **Initial Contact**: Passive sonar detects multiple ships, bearing 270°
2. **Periscope Assessment**: 15-second sweep reveals 8 ships in formation
3. **Classification Phase**: Extended 45-second observation identifies:
   - 6 cargo vessels (3 large tankers, 3 medium freighters)
   - 2 escort destroyers (HMS Icarus-class)
   - Formation speed: 8 knots, zigzag pattern every 4 minutes
4. **Tactical Intelligence**: Convoy following predictable route change schedule
5. **Attack Preparation**: Calculate optimal intercept position based on zigzag timing

---

## Periscope Detection & Counter-Detection

### Enemy Detection Probability

**Detection Factors**:
- **Periscope Exposure Time**: Longer exposure dramatically increases detection chance
- **Weather Conditions**: Calm seas make periscope wake more visible
- **Enemy Experience**: Veteran lookouts 300% more effective than green crew
- **Distance**: Detection probability decreases exponentially with range
- **Time of Day**: Periscope visible against dawn/dusk sky backdrop

**Detection Avoidance Tactics**:
- **Minimize Exposure**: Use brief sweeps with compass bearings
- **Weather Advantage**: Extend periscope during rough seas when wake is concealed
- **Tactical Timing**: Observe during enemy watch changes or high-activity periods
- **Multiple Positions**: Change position between observations to prevent pattern recognition

---

## Advanced Torpedo Combat System

### Torpedo Ballistics & Firing Solutions

#### **Torpedo Performance Characteristics**

**Torpedo Speed vs Range Trade-offs**:
- **High Speed Setting** (45 knots): 4km maximum range, 3-minute travel time, high cavitation
- **Medium Speed Setting** (35 knots): 8km maximum range, 6-minute travel time, moderate stealth
- **Low Speed Setting** (25 knots): 12km maximum range, 12-minute travel time, maximum stealth
- **Wake Visibility**: Faster settings create more visible torpedo wakes

---

### Advanced Firing Solution Mathematics

**Triangle of Interception Calculation**:
- **Target Course & Speed**: Estimate from periscope observation
- **Torpedo Speed & Range**: Selected based on tactical situation
- **Submarine Position**: Current location and movement capability
- **Firing Angle**: Optimal 90° angle-on-the-bow for maximum damage
- **Lead Calculation**: Predict target position at torpedo impact time

#### **Complex Firing Solution Example: U-505 vs SS Empire Trader**
**Target**: Large cargo ship, 12 knots, course 045°, range 6km

**Firing Solution Calculation**:
1. **Target Analysis**: Ship length 150m, estimated displacement 8,000 tons
2. **Speed Selection**: Medium speed (35 knots) for balance of range and stealth
3. **Travel Time Calculation**: 6km at 35 knots = 6.2 minutes torpedo travel
4. **Target Movement**: Ship will travel 1.24km during torpedo flight
5. **Lead Calculation**: Aim point 1.24km ahead of current position on course 045°
6. **Firing Solution**: Launch 4-torpedo spread to account for targeting errors
7. **Success Probability**: 65% chance of at least one hit with spread pattern

---

## Multi-Torpedo Attack Patterns

### Torpedo Spread Configurations

**Spread Pattern Options**:
- **Single Shot**: Maximum stealth, conserve ammunition, high-confidence targets only
- **Double Shot**: Backup torpedo for high-value targets, moderate ammunition usage
- **Fan Spread**: 3-4 torpedoes with different courses to cover target maneuvering
- **Salvo Attack**: All tubes fired simultaneously for maximum damage potential

#### **Fan Spread Tactical Example: USS Wahoo Attacking Japanese Destroyer**
**Target**: IJN Fubuki, 28 knots, zigzagging every 60 seconds

**Fan Spread Execution**:
1. **Tactical Problem**: Fast, maneuvering target with unpredictable course changes
2. **Solution**: 4-torpedo fan spread covering 30° arc ahead of target
3. **Torpedo Allocation**:
   - Torpedo 1: Aimed at current course projection
   - Torpedo 2: 10° starboard of projected course
   - Torpedo 3: 10° port of projected course
   - Torpedo 4: 20° starboard for extreme maneuver coverage
4. **Result**: Target zigs into torpedo 3's path, hit amidships, destroyer sunk
5. **Ammunition Cost**: 4 of 16 torpedoes expended for critical target elimination

---

## Advanced Resource Management & Endurance Operations

### Life Support Systems Management

#### **Air Supply Consumption Calculations**

**Oxygen Consumption Rates**:
- **Surface Operations**: Unlimited air via snorkel/direct intake
- **Submerged Standard**: 2 air units per hour for basic crew survival
- **Submerged Combat**: 3 air units per hour during high-stress operations
- **Deep Dive Emergency**: 4 air units per hour due to compressed air systems
- **Critical Reserve**: 12 hours minimum air supply must be maintained

---

### Battery Power Management System

**Power Consumption by Depth & Activity**:
- **Surface Operations**: Battery charging via diesel engines (+5 units/hour)
- **Torpedo Depth Cruising**: -3 battery units per hour
- **Torpedo Depth Combat**: -5 battery units per hour (systems active)
- **Deep Dive Operations**: -7 battery units per hour (life support intensive)
- **Sonar Operations**: Additional -2 battery units per hour when active

#### **Extended Operation Example: U-boats Patrolling Convoy Routes**
**Mission Duration**: 72 hours, 2,400km patrol area

**Resource Management**:
1. **Resource Planning**: Start with 100% air (48 hours), 100% battery (20 hours submerged)
2. **Day 1 Operations**: 16 hours submerged, 8 hours surface charging
   - Battery: 80% remaining after charging cycle
   - Air: 100% maintained through surface periods
   - Fuel: 85% remaining after 24 hours mixed operations
3. **Day 2-3 Resource Crisis**: Enemy aircraft force extended submersion
   - 40 hours continuous underwater operations required
   - Air: Critical levels, must surface despite detection risk
   - Battery: Emergency deep cycle, performance degraded
   - **Decision**: Risk surface exposure vs. crew asphyxiation

---

## Fuel & Logistics Management

### Fuel Consumption by Operations

**Operational Fuel Usage**:
- **Surface Transit**: 8 fuel units per hour at maximum speed
- **Surface Charging**: 6 fuel units per hour while stationary (battery charging)
- **Submerged Operations**: No fuel consumption (battery powered)
- **Emergency Operations**: +50% fuel consumption under combat stress

#### **Strategic Fuel Planning: Long-Range Patrol Mission**
**Mission Parameters**: 5,000km round trip, 14-day patrol

**Fuel Budget**:
1. **Fuel Capacity**: 280 fuel units maximum capacity
2. **Transit Requirement**: 2,000km each way = 200 fuel units for transit
3. **Patrol Operations**: 80 fuel units remaining for 10-day operational patrol
4. **Contingency Reserve**: 40 fuel units for emergency/combat situations
5. **Operational Limit**: 4 fuel units per day patrol operations, limits activity

---

## Advanced Sonar Systems & Acoustic Warfare

### Sonar Technology Integration & Tactical Applications

#### **Passive Sonar Contact Classification**

**Sound Signature Recognition**:
- **Engine Type Identification**: Diesel, steam, electric motor recognition
- **Ship Size Estimation**: Propeller cavitation patterns indicate displacement
- **Speed Calculation**: Propeller revolution rate analysis
- **Course Estimation**: Doppler shift analysis for bearing change
- **Range Estimation**: Sound intensity levels (experienced sonar operators only)

---

### Active Sonar Tactical Decision Matrix

**Active Sonar Usage Scenarios**:
- **Safe Navigation**: Shallow waters, reef navigation, obstacle avoidance
- **Target Confirmation**: Verify passive sonar contacts when stealth less critical
- **Counter-Detection**: Locate enemy submarines in mutual detection scenarios
- **Emergency Situations**: Navigation when periscope impossible, critical intelligence

#### **Active Sonar Risk Assessment: U-boat in Convoy Hunting Grounds**
**Situation**: Multiple passive contacts, unclear target priority

**Risk/Benefit Analysis**:
1. **Tactical Dilemma**: 4 passive contacts detected, need target classification
2. **Risk Analysis**: Active sonar will reveal submarine position to all contacts
3. **Benefit Assessment**: Accurate range/bearing for optimal torpedo positioning
4. **Decision Factors**:
   - Enemy escort experience level (veteran crews have passive sonar)
   - Time pressure (convoy moving out of intercept range)
   - Battery life (can submarine maintain pursuit if detected)
5. **Tactical Decision**: Single active ping to classify largest contact, accept detection risk

---

## Counter-Sonar & Stealth Operations

### Silent Running Procedures

**Noise Reduction Measures**:
- **Machinery Isolation**: Non-essential systems powered down
- **Crew Movement**: Minimal activity, soft-soled shoes, whispered communications
- **Speed Reduction**: Lower prop speed reduces cavitation noise
- **Deep Positioning**: Greater depth reduces surface ship detection capability
- **Natural Masking**: Use ocean thermal layers and noise sources for concealment

#### **Silent Running Scenario: Type VII U-boat Evading Destroyer**
**Situation**: Detected by HMS Icarus, depth charges dropped 200m away

**Silent Running Execution**:
1. **Immediate Response**: Emergency deep dive to 120 meters, silent running initiated
2. **System Shutdown**: Non-essential electronics powered down, crew frozen in positions
3. **Passive Tracking**: Monitor destroyer's propeller noise for course changes
4. **Endurance Challenge**: Maintain silence for 3 hours until destroyer departs
5. **Resource Impact**:
   - Battery: Drained to 40% during silent running
   - Air: Consumed to critical levels (8 hours remaining)
   - Crew Morale: Stress reduces effectiveness by 15% for following operations

---

## Submarine Tactical Scenarios - Stealth Warfare Mastery

### Wolf Pack Coordination Operations

#### **Multi-Submarine Attack Coordination**
**Formation**: 3-Submarine Wolf Pack vs. Allied Convoy
**Submarines**: U-552 (T4), U-99 (T4), U-47 (T4 Type VII fleet submarines) vs. 12-ship convoy with 4 escorts

**Phase 1 - Detection & Shadowing** (Range: 20km, Day 1):
1. **Initial Contact**: U-552 detects convoy via passive sonar at extreme range
2. **Contact Report**: Radio transmission to pack leader (risks detection)
3. **Pack Coordination**: U-99 and U-47 vector toward intercept positions
4. **Shadowing**: Maintain 15km distance, track convoy course changes
5. **Intelligence Gathering**: 24-hour observation period to learn escort patterns

**Phase 2 - Positioning** (Day 2, Night Operations):
1. **Attack Formation**:
   - U-552: Forward position, convoy's starboard bow
   - U-99: Convoy's port beam, 8km range
   - U-47: Convoy's stern, cleanup position
2. **Coordination Timing**: Simultaneous attack at 0200 hours
3. **Communication**: Final positioning via brief radio bursts
4. **Weather Factor**: Rough seas provide cover but complicate torpedo accuracy

**Phase 3 - Coordinated Attack** (0200-0215 hours):
1. **U-552 Opening**: Fires 4-torpedo spread at lead tanker and cargo ship
   - Results: Tanker hit and sinking, cargo ship damaged but operational
2. **U-99 Follow-up**: Targets 2 largest remaining cargo vessels
   - Results: Both ships hit, 1 sinking immediately, 1 listing heavily
3. **U-47 Cleanup**: Attacks damaged ships and attempts escort engagement
   - Results: Finishes off damaged cargo ship, misses destroyer
4. **Escort Response**: 4 destroyers scatter to hunt submarines

**Phase 4 - Evasion & Extraction** (0215-0800 hours):
1. **U-552**: Detected by HMS Icarus, forced to deep dive, 6-hour evasion
2. **U-99**: Escapes undetected, shadows remaining convoy ships
3. **U-47**: Engaged by 2 destroyers, forced to emergency surface, surrenders
4. **Final Assessment**: 4 ships sunk, 1 submarine lost, tactical victory with heavy cost

---

### Solo Submarine Infiltration Mission

#### **Mission: USS Nautilus (T8 Advanced Attack Submarine) Infiltrating Japanese Harbor**
**Objective**: Reconnaissance and opportunity attack in Truk Lagoon

**Approach Phase** (72 hours underwater approach):
1. **Deep Transit**: 150-hour journey at deep depth to avoid air patrols
2. **Resource Management**: Critical air/battery conservation during approach
3. **Intelligence**: Passive sonar mapping of harbor defenses and ship positions
4. **Risk Assessment**: Multiple destroyer patrols, shallow water navigation hazards

**Infiltration Phase** (Night penetration of harbor defenses):
1. **Surface Reconnaissance**: Brief periscope survey of harbor entrance
2. **Defense Analysis**:
   - 2 destroyers patrolling harbor mouth
   - Anti-submarine nets partially deployed
   - Searchlight coverage every 3 minutes
3. **Penetration Route**: Follow fishing boat through net opening
4. **Stealth Requirements**: Silent running at minimum depth

**Target Assessment Phase** (Interior harbor operations):
1. **High-Value Targets Identified**:
   - IJN Yamato: Anchored 2km from harbor center
   - 2 Heavy cruisers: Moored at naval facility
   - 4 Cargo ships: Loading fuel and ammunition
   - 1 Aircraft carrier: Undergoing repairs
2. **Tactical Decision**: Single attack run vs. multiple smaller attacks
3. **Ammunition Planning**: 6 torpedoes available, must maximize damage
4. **Escape Route**: Pre-planned withdrawal through northern channel

**Attack Phase** (Maximum damage concentration):
1. **Target Selection**: Focus on Yamato (strategic priority) and carrier
2. **Firing Solution**:
   - 4 torpedoes at Yamato: Fan spread, maximum damage potential
   - 2 torpedoes at carrier: Insurance shots for secondary target
3. **Attack Execution**: All torpedoes fired within 90 seconds
4. **Results**:
   - Yamato: 3 hits, severe flooding, out of action 6 months
   - Carrier: 1 hit, moderate damage, repairs extended 3 months

**Extraction Phase** (High-speed escape under pursuit):
1. **Immediate Response**: Emergency surface, maximum speed toward exit
2. **Pursuit**: 6 destroyers converging from all directions
3. **Evasion Tactics**: Emergency dive in channel, use harbor confusion
4. **Escape Success**: Cleared harbor during chaos, successful extraction
5. **Strategic Impact**: Major Japanese naval operations disrupted for months

---

## Anti-Submarine Warfare (ASW) for Surface Ships

### ASW Detection Methods

**Surface Ship Detection Systems**:
- **Visual Detection**: Periscope sightings, surfaced submarines, torpedo wakes
- **Sonar Detection**: Passive hydrophones, active sonar pinging
- **Radar Detection**: Surface and snorkel detection
- **Aircraft Spotting**: Aerial reconnaissance identifies submarine positions

**ASW Weapons**:
- **Depth Charges**: Area-effect underwater explosions
- **Hedgehog**: Forward-throwing anti-submarine mortar
- **Torpedoes**: Anti-submarine homing torpedoes (late war)
- **Ramming**: Emergency last-resort tactic

---

### Depth Charge Mechanics

**Depth Charge Deployment**:
- **Dropped from stern**: Roll off back of ship
- **Projected from mortars**: K-gun launchers throw charges to sides
- **Depth setting**: Pre-set to explode at specific depth
- **Pattern drops**: Multiple charges create lethal area

**Damage Mechanics**:
- **Direct hit**: Catastrophic damage, likely sinking
- **Near miss (<50m)**: Heavy damage, flooding, module damage
- **Proximity (<100m)**: Moderate damage, crew casualties
- **Distant (<200m)**: Light damage, crew morale impact

---

## Cross-Reference Documents

**Related Combat Systems**:
- [Combat-Overview.md](Combat-Overview.md) - Multi-domain warfare integration
- [Surface-Combat.md](Surface-Combat.md) - ASW operations for destroyers
- [Carrier-Operations.md](Carrier-Operations.md) - Anti-submarine air patrols
- [Damage-Model.md](Damage-Model.md) - Submarine damage mechanics

**Related Game Systems**:
- Ship Progression System (GDD Core)
- Module Customization System (GDD Core)
- Crew Training System (GDD Core)
- Resource Management System (GDD Core)

---

## Implementation Notes

**Phase 2 Priority Features**:
1. Three-layer depth control system
2. Periscope operations with detection risk
3. Torpedo firing solutions and spreads
4. Resource management (air, battery, fuel)
5. Passive and active sonar systems
6. Silent running and stealth mechanics
7. ASW depth charge mechanics

**Critical Success Factors**:
- Stealth gameplay rewards patience and planning
- Resource management creates constant tension
- 3D positioning mastery separates skilled players
- High-risk/high-reward asymmetric warfare
- Extraction denial creates strategic server impact
- Scale from T1 coastal subs to T10 strategic threats

This comprehensive submarine warfare system transforms stealth combat from basic hide-and-seek into sophisticated underwater operations requiring resource management, tactical patience, intelligence gathering, and precise execution where every decision carries life-or-death consequences in extraction-based gameplay.
