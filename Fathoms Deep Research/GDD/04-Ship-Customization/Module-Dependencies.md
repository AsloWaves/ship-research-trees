# Module Dependencies & Integration

**Document Type**: Core Mechanics Implementation
**Status**: Active Development
**Tags**: [mechanics, modules, dependencies, integration, weight]
**Last Updated**: 2025-01-17

---

## Overview

This document defines how modules depend on and interact with each other, creating a coherent system of equipment progression and tactical choice. Understanding dependencies is crucial for effective ship fitting.

**Design Philosophy:**
1. **If It Fits, It Works** - Weight is the universal constraint. A modern radar on a 1900s destroyer? If the mount can handle the weight, go for it.
2. **Logical Dependencies** - Modules that need other modules to function (e.g., Decryption needs SIGINT)
3. **Weight Constraints** - Mount weight capacity and ship tonnage limit configurations
4. **Crew Requirements** - Modules install without crew but won't function until manned
5. **Synergy Rewards** - Complementary modules provide bonus effects
6. **Graceful Degradation** - Losing a dependency reduces effectiveness but doesn't always disable

---

## Dependency Types

### Hard Dependencies

Module CANNOT function without prerequisite. Will not activate in combat.

```
Hard_Dependency:
  Module A [REQUIRES] Module B
  Without B: Module A displays "Missing Dependency" and does not function
  Example: Decryption Module requires Radio Intercept Standard OR SIGINT Suite
```

### Soft Dependencies

Module functions at reduced effectiveness without prerequisite.

```
Soft_Dependency:
  Module A [ENHANCED BY] Module B
  Without B: Module A functions at X% effectiveness
  Example: Fire Control Director enhanced by Radar (+30% accuracy when paired)
```

### Exclusive Dependencies

Only one module of this type can be active at a time.

```
Exclusive_Dependency:
  Module A [EXCLUSIVE WITH] Module B
  Cannot install both: Only one bridge type at a time
  Example: CIC Bridge and Director Bridge are mutually exclusive
```

---

## Bridge Dependency Chain

The bridge is the master controller for many ship capabilities.

### Bridge Tier → UI Features

| Bridge Type | Era | Compass | Minimap | Lead Indicator | Contact Info | Voice Comms |
|-------------|-----|---------|---------|----------------|--------------|-------------|
| Open Bridge | 1890+ | Basic | None | None | Visual only | Flags only |
| Enclosed Bridge | 1910+ | Accurate | None | None | Visual only | Flags only |
| Interwar Bridge | 1920+ | Accurate | None | Basic | Visual | Flags/Lamp |
| Director Bridge | 1920+ | Accurate | None | **YES** | Visual+ | Radio capable |
| CIC Bridge | 1940+ | Accurate | **RADAR** | Advanced | All contacts | Voice radio |
| Modern Bridge | 1970+ | Digital | Enhanced | Auto | Auto-track | Encrypted |

### Bridge → Module Unlocks

```
Open_Bridge:
  ALLOWS: Basic visual equipment only
  BLOCKS: All radar integration, data link, advanced fire control

Enclosed_Bridge:
  ALLOWS: Basic radar (no integration), basic fire control
  BLOCKS: Radar minimap, data link

Director_Bridge:
  ALLOWS: Fire Control Directors, Basic radar integration
  UNLOCKS: Lead indicator display
  BLOCKS: Full radar minimap, data link

CIC_Bridge:
  ALLOWS: Full radar integration, voice radio integration
  UNLOCKS: Radar minimap, all contact types visible
  BLOCKS: Nothing significant

Modern_Bridge:
  ALLOWS: All systems
  UNLOCKS: Automated tracking, encrypted comms, data link
```

### Bridge Dependency Examples

| Module | Minimum Bridge Required | Effect Without |
|--------|------------------------|----------------|
| Fire Control Director | Director Bridge | Cannot display lead indicator |
| Radar (Surface Search) | Enclosed Bridge | Functions, but no map integration |
| Radar (Fire Control) | Director Bridge | Radar works, FC bonus reduced 50% |
| Data Link 11 | CIC Bridge | Cannot install |
| Data Link 16 | Modern Bridge | Cannot install |
| SIGINT Suite | Enclosed Bridge | Functions normally |
| Auto-Fire Control | CIC Bridge | Cannot activate auto-mode |

---

## Detection System Dependencies

### Radar Module Chain

```
Basic_Search_Radar
  REQUIRES: Enclosed+ Bridge
  PROVIDES: Basic surface detection (visual cone ping)

Fire_Control_Radar
  REQUIRES: Director+ Bridge
  REQUIRES: Fire Control Director
  PROVIDES: +15% accuracy bonus, radar-assisted ranging

Air_Search_Radar
  REQUIRES: CIC+ Bridge
  PROVIDES: Air contact detection (long range)

Track_While_Scan
  REQUIRES: Modern Bridge
  REQUIRES: Fire Control Radar
  PROVIDES: Multiple simultaneous targets

Dependency_Diagram:
                    Basic_Search_Radar
                           |
              ┌────────────┼────────────┐
              ↓            ↓            ↓
        Fire_Control   Air_Search   Surface_Search
              |            |         (enhanced)
              ↓            ↓
        Track_While_Scan ←─┘
              |
              ↓
        Cooperative_Engagement
```

### Sonar Module Chain

```
Passive_Hydrophone
  REQUIRES: None
  PROVIDES: Submarine detection (bearing only)

Active_Sonar
  REQUIRES: Enclosed+ Bridge
  PROVIDES: Submarine detection (bearing + range), alerts target

Variable_Depth_Sonar
  REQUIRES: Active Sonar
  REQUIRES: CIC+ Bridge
  PROVIDES: Below-layer submarine detection

Towed_Array
  REQUIRES: Passive Hydrophone
  REQUIRES: Speed < 15 knots
  PROVIDES: Long-range passive detection

Dependency_Diagram:
        Passive_Hydrophone ────→ Towed_Array
              |
              ↓
        Active_Sonar
              |
              ↓
        Variable_Depth_Sonar
```

### SIGINT Module Chain

```
Radio_Intercept_Basic (EW-007)
  REQUIRES: None
  PROVIDES: TBS voice intercept (30 km)

Radio_Intercept_Standard (EW-008)
  REQUIRES: Enclosed+ Bridge
  PROVIDES: HF/VHF intercept (75 km), Direction Finding

SIGINT_Suite (EW-009)
  REQUIRES: CIC+ Bridge
  PROVIDES: Full spectrum intercept (150 km), Data Link detection

Decryption_Module (EW-010)
  REQUIRES: Radio_Intercept_Standard OR SIGINT_Suite
  PROVIDES: Message decryption capability

Dependency_Diagram:
        Radio_Intercept_Basic
              |
              ↓
        Radio_Intercept_Standard ────┐
              |                      │
              ↓                      ↓
        SIGINT_Suite ──────────→ Decryption_Module
```

---

## Fire Control Dependencies

### Main Battery Fire Control

```
Rangefinder (Basic)
  REQUIRES: Gunner crew card
  PROVIDES: +5% accuracy

Coincidence_Rangefinder
  REQUIRES: Rangefinder
  PROVIDES: +10% accuracy (replaces basic bonus)

Fire_Control_Director
  REQUIRES: Director+ Bridge
  REQUIRES: Coincidence Rangefinder
  PROVIDES: +15% accuracy, lead indicator

Analog_Fire_Control_Computer
  REQUIRES: Fire Control Director
  REQUIRES: CIC+ Bridge
  PROVIDES: +20% accuracy, improved prediction

Radar_Fire_Control
  REQUIRES: Analog FC Computer
  REQUIRES: Fire Control Radar
  PROVIDES: +30% accuracy, night fighting capability

Digital_Fire_Control
  REQUIRES: Modern Bridge
  REQUIRES: Radar Fire Control
  PROVIDES: +40% accuracy, automatic engagement mode

Dependency_Chain (Linear):
  Rangefinder → Coincidence → Director → Analog → Radar_FC → Digital_FC
```

### Combined Arms Bonuses

When multiple fire control elements work together:

| Combination | Bonus |
|-------------|-------|
| Director + Radar | +5% additional accuracy |
| Radar FC + Air Search | Can engage air targets at extended range |
| Digital FC + Data Link | Cooperative fire control with allies |
| Multiple Rangefinders | Backup if one damaged |

---

## Communication Dependencies

### Voice Communication Chain

```
Signal_Flags
  REQUIRES: None
  PROVIDES: Visual text communication (5 km, daylight)

Signal_Lamp_Basic
  REQUIRES: None
  PROVIDES: Visual text communication (15 km, any light)

Signal_Lamp_Advanced
  REQUIRES: Signal Lamp Basic experience
  PROVIDES: Directional communication (20 km, 15° beam)

Wireless_HF
  REQUIRES: Enclosed+ Bridge
  PROVIDES: Long-range text (500+ km)

Radio_TBS
  REQUIRES: Director+ Bridge
  PROVIDES: Voice communication (20 km), Vision Sharing

Radio_VHF
  REQUIRES: CIC+ Bridge
  PROVIDES: Multi-channel voice (50 km), Vision Sharing

Radio_UHF_Encrypted
  REQUIRES: Modern Bridge
  PROVIDES: Secure voice (30 km), cannot be intercepted

Data_Link_11
  REQUIRES: CIC Bridge
  REQUIRES: Radio VHF
  PROVIDES: Automated sensor sharing (300 km)

Data_Link_16
  REQUIRES: Modern Bridge
  REQUIRES: Radio UHF Encrypted
  PROVIDES: Real-time tactical data (300 km)
```

### Communication Security Hierarchy

| System | Can Be Intercepted By | Cannot Be Intercepted |
|--------|----------------------|----------------------|
| Signal Flags | Visual observation | Electronic means |
| Signal Lamp | Visual observation (in beam) | Electronic means |
| Wireless HF | Radio Intercept Standard+ | - |
| Radio TBS | Radio Intercept Basic+ | - |
| Radio VHF | Radio Intercept Standard+ | - |
| Radio UHF | SIGINT Suite only | Basic intercept |
| Data Link 11 | SIGINT Suite (detection only) | Content |
| Data Link 16 | SIGINT Suite (detection only) | Content |

---

## Electronic Warfare Dependencies

### Active EW Chain

```
Radar_Warning_Receiver (Basic)
  REQUIRES: None
  PROVIDES: Alerts when illuminated by radar

RWR_Advanced
  REQUIRES: RWR Basic
  REQUIRES: Enclosed+ Bridge
  PROVIDES: Identifies radar type, threat library

ESM_Suite
  REQUIRES: RWR Advanced
  REQUIRES: CIC+ Bridge
  PROVIDES: Passive detection of all emissions (300+ km)

Noise_Jammer
  REQUIRES: Enclosed+ Bridge
  PROVIDES: Masks ship from radar (-30% enemy accuracy)

Deceptive_Jammer
  REQUIRES: CIC+ Bridge
  REQUIRES: ESM Suite
  PROVIDES: Creates false targets, missile seduction

ECM_Suite
  REQUIRES: Modern Bridge
  REQUIRES: ESM Suite
  REQUIRES: Deceptive Jammer
  PROVIDES: Automated EW, AI-assisted threat response
```

### Chaff/Decoy Chain

```
Chaff_Launcher_Manual
  REQUIRES: None
  PROVIDES: Manual chaff deployment, missile defense

Chaff_Launcher_Auto
  REQUIRES: RWR Basic
  PROVIDES: Automatic chaff on missile lock

Decoy_Launcher
  REQUIRES: ESM Suite
  PROVIDES: Active decoys, improved seduction
```

---

## Propulsion Dependencies

### Engine Configuration

```
Engine_Type_Restrictions:
  Destroyer_Slot: Only accepts Destroyer-class engines
  Cruiser_Slot: Only accepts Cruiser-class engines
  Battleship_Slot: Only accepts Battleship-class engines

Speed_Calculation:
  Max_Speed = Base_Hull_Speed × Engine_Modifier × Weight_Modifier

  Where:
  - Engine_Modifier = Σ(Installed_Engine_Output) / Required_Engine_Output
  - Weight_Modifier = Design_Displacement / Actual_Displacement
```

### Auxiliary Systems

```
Repair_Crew_Module
  REQUIRES: Engineer crew card
  PROVIDES: Faster engine repair (+50%)

Damage_Control_Module
  REQUIRES: None
  PROVIDES: +1 damage control party
```

---

## Weight-Based Fitting System

### Core Principle: If It Fits, It Works

There are **no era restrictions** on module installation. When a player unlocks a ship hull, they can technically mount ANY module on it—as long as the physics work.

### Mount Weight Capacity

Every turret mount and module slot has a **weight capacity** that determines what can be installed:

```
Mount_Check:
  Mount_Weight_Capacity = Maximum weight the mount can support
  Module_Total_Weight = Module_Weight + (Crew_Weight × Crew_Required)

  IF Module_Total_Weight > Mount_Weight_Capacity THEN
    Module CANNOT be installed (too heavy for mount)
  ELSE
    Module installs successfully
```

### Crew Weight Factor

Crew members take up space and add weight. Each crew station adds approximately:

| Crew Type | Weight per Person |
|-----------|------------------|
| Standard Crew | 100 kg |
| Officer | 120 kg (gear) |
| Specialist | 150 kg (equipment) |

**Example**: A modern radar requiring 4 specialist crew adds 600 kg to its total weight.

### Module Without Crew

Players CAN install a module even if they don't have enough crew:

```
Crew_Installation_Rules:
  Module installs: Always (if weight fits)
  Module functions: Only when properly crewed

  Partially_Crewed: Module functions at reduced effectiveness
  No_Crew: Module is installed but completely non-functional
```

This allows players to:
- Plan ahead by installing equipment for future crews
- Make tactical decisions about which systems to man
- Sacrifice one system's crew to bolster another in emergencies

### Why No Era Restrictions?

**Gameplay Reasoning:**
- Rewards clever players who save for advanced equipment
- Creates interesting asymmetric combat (old ship + new tech vs new ship + old tech)
- Allows "Project Ship" builds where players upgrade beloved vessels
- Naturally balanced by economics (advanced modules are expensive)

**Physics Balance:**
- Heavy modern equipment may not fit on small destroyer mounts
- Large ships can support heavier, more advanced systems
- Weight penalties affect speed and handling if overloaded

---

## Weight Dependency System

### Weight Budget

```
Weight_Check:
  Design_Displacement = Ship hull maximum capacity
  Current_Displacement = Hull + Modules + Ammunition + Fuel + Crew + Cargo

  IF Current > Design × 1.10 THEN
    Ship is overweight (penalties apply)

  IF Current > Design × 1.25 THEN
    Ship cannot deploy (too heavy to operate safely)
```

### Overweight Penalties

| Overweight % | Speed Penalty | Stability Penalty | Flood Risk |
|--------------|---------------|-------------------|------------|
| 0-5% | -2% | None | None |
| 5-10% | -5% | -5% | +10% |
| 10-15% | -10% | -10% | +25% |
| 15-20% | -20% | -20% | +50% |
| 20-25% | -30% | -30% | +100% |
| 25%+ | CANNOT DEPLOY | - | - |

### Weight Optimization

```
Optimization_Strategy:
  Heavy_Hitter: Maximum weapons, minimal support
  - Pro: Maximum firepower
  - Con: Limited sustainability, fewer damage control options

  Balanced: Standard loadout, moderate support
  - Pro: Adaptable
  - Con: No specialization bonus

  Survivable: Reduced weapons, maximum support
  - Pro: Longest operational endurance
  - Con: Reduced combat effectiveness
```

---

## Crew Dependencies

### Module → Crew Requirements

Every module requires specific crew types:

| Module Category | Required Crew Type | Per-Module Count |
|-----------------|-------------------|------------------|
| Main Battery | Gunner | 1 per turret |
| Secondary Battery | Gunner | 1 per mount |
| AA Battery | AA Specialist | 1 per 2-4 mounts |
| Torpedo Tubes | Torpedoman | 1 per mount |
| Engine | Engineer | 1 per engine |
| Fire Control | Fire Control | 1 per director |
| Radar | Electronics | 1 per radar |
| SIGINT | SIGINT Operator | 2-4 per suite |
| Damage Control | Damage Control | 1-2 per party |
| Bridge | Various | Captain + Officers |

### Under-Crewed Penalties

```
Crew_Efficiency:
  Fully_Crewed (100%): Module operates at full effectiveness
  Under_Crewed (75%): -15% effectiveness
  Under_Crewed (50%): -35% effectiveness
  Under_Crewed (25%): -60% effectiveness
  No_Crew (0%): Module inactive
```

---

## Synergy Bonuses

### Complementary Module Sets

When specific modules are installed together, bonus effects apply:

| Module Combination | Synergy Bonus |
|-------------------|---------------|
| Fire Control Director + Fire Control Radar | +5% accuracy (stacks with individual bonuses) |
| SIGINT Suite + Decryption Module | +20% decryption speed, auto-handoff |
| CIC Bridge + Data Link 11 | Automated contact sharing |
| ESM Suite + Deceptive Jammer | +15% jamming effectiveness |
| Multiple Rangefinders | Redundancy (backup if one destroyed) |
| Radar + Fire Control + CIC | Full integration: +10% overall accuracy |

### National Equipment Bonuses

Equipment from the same nation as the ship provides bonuses:

| Nation | National Bonus |
|--------|---------------|
| USA | +10% radar effectiveness |
| UK | +10% ASW effectiveness |
| Japan | +10% night combat |
| Germany | +10% reliability |
| France | +5% speed, +5% detection |
| Italy | +15% speed |

---

## Dependency Failure Modes

### What Happens When Dependencies Fail

| Failure Type | Effect |
|--------------|--------|
| Hard Dependency Lost | Module stops functioning immediately |
| Soft Dependency Lost | Module functions at reduced effectiveness |
| Power Lost | Module powers down, can restart when power restored |
| Crew Lost | Module effectiveness reduced proportionally |
| Bridge Downgraded | Higher-tier features unavailable |

### Example Failure Cascade

```
Scenario: CIC Bridge damaged (reverts to basic bridge functionality)

Immediate_Effects:
- Radar minimap disabled
- Advanced fire control features disabled
- Data Link goes offline
- Auto-fire control disabled

Cascade_Effects:
- Fire Control Radar loses integration bonus (-15% accuracy)
- SIGINT Suite continues functioning (only needs Enclosed Bridge)
- ECM Suite loses automated response

Result: Ship can still fight but with 1940s-era effectiveness
```

---

## Implementation Notes

### For Programmers

1. **Dependency Graph**: Implement as directed acyclic graph (DAG)
2. **Real-time Validation**: Check dependencies when modules change
3. **Graceful Degradation**: Soft dependencies reduce effectiveness, don't disable
4. **UI Feedback**: Show dependency status (green/yellow/red) in fitting screen
5. **Cascade Calculation**: When dependency fails, recalculate all dependent modules

### Fitting Screen Requirements

**Must Display:**
- Mount weight capacity vs module weight (+ crew weight)
- Ship tonnage budget (used/max)
- Crew requirements (assigned/needed)
- Module dependency status
- Synergy bonuses active
- Warning if module installed but non-functional (missing crew)

### Validation Order

1. Mount weight check (module + crew weight vs mount capacity)
2. Ship tonnage check (total weight vs displacement)
3. Hard dependencies check
4. Crew availability check (warn if insufficient, allow anyway)
5. Bridge requirements check (for UI features)
6. Soft dependencies check (calculate effectiveness)
7. Synergy bonuses calculation

---

## Cross-Reference Documents

**Related Systems:**
- [[Module-System]] - Core module installation mechanics
- [[Detection-System]] - How detection modules work
- [[Ballistics-Gunnery-Mechanics]] - Fire control integration
- [[Bridge modules]] - Bridge tier capabilities

**Module Documentation:**
- [[Modules/Support/Electronic-Warfare/README]] - EW module dependencies
- [[Modules/Support/Communications/README]] - Communication dependencies
- [[Modules/Bridge/README]] - Bridge capabilities

---

## Summary: Key Dependencies

### Critical Chains to Remember

1. **Fire Control**: Rangefinder → Director → Computer → Radar FC
2. **Detection**: Bridge Tier → Radar Integration → Minimap
3. **SIGINT**: Intercept → SIGINT Suite → Decryption
4. **Communication**: Bridge Tier → Radio Type → Data Link
5. **EW**: RWR → ESM → ECM Suite

### Most Common Fitting Mistakes

1. Installing module too heavy for mount (module + crew exceeds capacity)
2. Exceeding ship tonnage (speed/stability penalties)
3. Installing modules without crew (non-functional until manned)
4. Installing Data Link without CIC Bridge
5. Installing Decryption without Intercept system

---

*This document provides the framework for module interactions. Specific values may be adjusted during balance testing.*
