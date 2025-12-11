# Turret Mechanics
**Category**: Combat Systems
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-10

---

## Overview

Turret mechanics govern how ship-mounted weapons traverse, elevate, reload, and interact with crew efficiency. This system bridges the gap between the Module System (weapon hardpoints) and the Ballistics-Gunnery mechanics (hit probability), defining the operational characteristics that affect combat effectiveness.

**Design Philosophy**: Turrets should feel weighty and realistic without becoming tedious. Players should feel the difference between fast-traversing destroyer guns and slow-moving battleship turrets, while crew skill meaningfully impacts performance.

**Important Notes**:
- All specific turret values (traverse speed, reload time, elevation limits, etc.) are defined in each **Turret ScriptableObject (SO)**, not in this document
- This document describes the **mechanics** of how turrets work, not specific stats
- Turrets follow the **One Crew Card Per Module** rule per [[Crew-Module-Mechanics]]

---

## Turret Configuration Types

### By Mount Style

| Mount Type | Traverse Arc | Protection Level | Crew Exposure | Typical Use |
|------------|--------------|------------------|---------------|-------------|
| **Enclosed Turret** | 270°-360° | Armored (0.2x) | Low | Main battery |
| **Open Mount** | 360° | Exposed (2.0x) | High | Secondary/AA |
| **Casemate** | 60°-120° | Protected (0.5x) | Medium | Secondary |
| **Barbette** | 270°-300° | Semi-Protected (1.0x) | Medium | Heavy secondary |
| **Wing Turret** | 180° (per side) | Armored (0.2x) | Low | Early BB designs |

### By Barrel Count

| Configuration | Dispersion Modifier | Notes |
|---------------|---------------------|-------|
| **Single** | 1.0x | Baseline |
| **Twin** | 1.05x | Standard |
| **Triple** | 1.10x | Wider dispersion |
| **Quad** | 1.15x | Widest dispersion |

*Note: Reload time and other modifiers are defined per-turret in Turret SOs*

### By Purpose

| Type | Elevation Range | Primary Target | Fire Control | Examples |
|------|-----------------|----------------|--------------|----------|
| **Surface Only** | -5° to +30° | Ships | Surface FC | 16"/45 Mk6 |
| **Dual-Purpose (DP)** | -10° to +85° | Ships + Aircraft | Unified FC | 5"/38 Mk12 |
| **AA Only** | +0° to +90° | Aircraft | AA FC | 40mm Bofors |
| **ASW** | Fixed | Submarines | Sonar | Hedgehog |

---

## Traverse & Elevation Mechanics

### Core Properties (Defined in Turret SO)

Each Turret SO defines:
- **Traverse Speed** (°/sec) - How fast the turret rotates horizontally
- **Elevation Speed** (°/sec) - How fast the turret adjusts vertical angle
- **Min/Max Elevation** (degrees) - Vertical range of motion
- **Traverse Arc** (degrees) - Horizontal range of motion (may include blind spots)

### Traverse/Elevation Modifiers

**Effective Speed** = `Base_Speed (from SO) × Crew_Efficiency × Damage_Factor × Power_Factor`

| Factor | Source | Notes |
|--------|--------|-------|
| **Base Speed** | Turret SO | Specific to each turret type |
| **Crew Efficiency** | [[Crew-Module-Mechanics]] | Based on Gunner's stat and sailor count |
| **Damage Factor** | See Damage States below | 1.0 → 0.25 as turret degrades |
| **Power Factor** | Ship power system | 1.0 normal, reduced if engines damaged |

### Bearing Restrictions

Some turret positions have blind spots due to superstructure:

| Position | Typical Restriction | Notes |
|----------|---------------------|-------|
| **Forward Superfiring** | ~300° arc | Blocked by bridge |
| **Aft Superfiring** | ~300° arc | Blocked by funnel |
| **Wing Turrets** | ~180° arc | One side only |
| **Casemates** | 60-120° arc | Fixed broadside |

*Specific arcs defined per ship hull design*

---

## Reload Mechanics

### Core Reload Properties (Defined in Turret SO)

Each Turret SO defines:
- **Base Reload Time** (seconds) - Time between salvos at full efficiency
- **Ready Ammunition** (rounds) - Fast-access ammo before magazine resupply needed

### Reload Modifiers

**Effective Reload Time** = `Base_Reload (from SO) / Crew_Efficiency × Damage_Factor × Ammo_Factor`

| Factor | Source | Notes |
|--------|--------|-------|
| **Base Reload** | Turret SO | Specific to each turret type |
| **Crew Efficiency** | [[Crew-Module-Mechanics]] | Based on Gunner's Reload stat and sailor count |
| **Damage Factor** | See Damage States | 1.0 → 2.5 (at 25% state) |
| **Ammo Factor** | `1.0` standard, `1.2` switching types | Penalty for changing ammo type |

*Per Crew-Module-Mechanics: `Final_Reload = Base_Reload / Efficiency`*

### Ready Ammunition

Turrets maintain ready ammunition for rapid initial fire (defined in Turret SO):

**Ready Rack Depletion**: After ready rounds expended, reload time increases by 50% until magazine resupply completes (resupply time also defined per turret).

---

## Turret Crew System

### One Crew Card Per Turret

Per [[Crew-Module-Mechanics]], each turret module has exactly **one crew slot** that accepts a single Gunner crew card.

```
Turret_Crew_Rules:
  - Each turret has ONE crew slot
  - Crew card must be Gunner classification (or Neutral with -20% penalty)
  - Crew card weight + Turret weight must fit mount capacity
  - Turrets without assigned crew are NON-FUNCTIONAL
  - Turrets with 0 sailors remaining are NON-FUNCTIONAL but crew card stays assigned
```

### Crew Stats Affecting Turret Performance

| Gunner Stat | Turret Effect | Per Crew-Module-Mechanics |
|-------------|---------------|---------------------------|
| **Accuracy** (Primary) | Shell Spread | `Final_Spread = Base_Spread × (2.0 - Efficiency)` |
| **Reload** (Primary) | Fire Rate | `Final_Reload = Base_Reload / Efficiency` |
| **Range** (Secondary) | Max Effective Range | `Final_Range = Base_Range × Efficiency` |

### Sailor Count as Casualty Buffer

Higher level crew cards have more sailors, allowing them to absorb casualties while maintaining performance:

| Crew Level | Max Sailors | Casualty Resilience |
|------------|-------------|---------------------|
| Level 1 | 10 | Very fragile |
| Level 50 | 255 | Moderate buffer |
| Level 100 | 455 | Large buffer |
| Level 200 | 705 | Maximum resilience |

When sailors are lost, efficiency drops proportionally (Sailor_Factor = Current/Max).

---

## Damage States & Effects

### Turret Damage Progression

From [[Surface-Combat]]:

| Damage State | HP Remaining | Traverse | Reload | Accuracy | Visual |
|--------------|--------------|----------|--------|----------|--------|
| **Operational** | 100-76% | 100% | 100% | 100% | Normal |
| **Damaged** | 75-51% | 75% | 80% | 90% | Smoke |
| **Heavy Damage** | 50-26% | 50% | 60% | 75% | Fire/sparks |
| **Critical** | 25-1% | 25% | 40% | 50% | Heavy damage |
| **Destroyed** | 0% | 0% | 0% | 0% | Wrecked |

### Damage Types vs Turrets

| Damage Type | Turret Effect | Crew Casualty Risk |
|-------------|---------------|-------------------|
| **HE** | External damage, exposed crew | High (1.5x) |
| **AP** | Penetration → magazine risk | Low (0.3x) |
| **SAP** | Balanced damage | Medium (0.8x) |
| **Fire** | Gradual damage, magazine risk | Medium |
| **Flooding** | Minimal (above waterline) | Low |

### Turret Jamming

Turrets can jam when hit, temporarily disabling traverse/elevation:

| Hit Location | Jam Chance | Jam Duration |
|--------------|------------|--------------|
| **Turret Ring** | 30% | 15-45 sec |
| **Elevation Gear** | 20% | 10-30 sec |
| **Traverse Motor** | 25% | 10-30 sec |
| **Barbette** | 15% | 30-60 sec |

**Jam Repair**: Crew automatically attempts repair. Time reduced by Engineer skill of damage control parties.

### Magazine Detonation

Critical overpenetrating hits to turret barbette can cause magazine detonation (extremely rare):

| Condition | Detonation Chance | Result |
|-----------|-------------------|--------|
| **AP overpenetration to barbette** | 0.05-0.10% | Catastrophic |
| **Fire reaching magazine** | Slow escalation | Catastrophic if not controlled |
| **Magazine flooding (manual)** | Prevents detonation | Turret permanently disabled |

**Catastrophic Detonation**: Destroys turret completely, causes major hull damage, high crew casualties.

*Note: This is an extremely rare event. Most hits will not penetrate to magazine depth.*

---

## Heat & Barrel Wear

### Sustained Fire Heat

Continuous firing generates heat affecting accuracy:

| Shots Fired | Heat Level | Spread Penalty | Notes |
|-------------|------------|----------------|-------|
| **1-5** | Cold | 0% | Normal |
| **6-10** | Warm | +2% | Minimal effect |
| **11-20** | Hot | +5% | Barrel expansion |
| **21-30** | Very Hot | +10% | Significant |
| **31+** | Overheated | +20% | Risk of turret damage |

**Cooling Rate**: Heat decreases by 2 levels per 30 seconds of non-firing.

### Barrel Wear → Turret Damage

Barrel wear is abstracted into the turret damage system rather than tracked separately:

- Sustained heavy fire accumulates turret HP damage over time
- Represents wear on barrel rifling, breach mechanisms, and fire control
- Repaired at port as part of normal turret repair (no separate barrel replacement)
- Encourages tactical fire discipline to preserve turret condition

---

## Turret Targeting & Fire Control

### Target Acquisition

Time to acquire new target:

| Fire Control Era | Acquisition Time | Notes |
|------------------|------------------|-------|
| **Pre-Radar (T1-T3)** | 8-15 sec | Optical only |
| **Early Radar (T4-T5)** | 5-10 sec | Radar-assisted |
| **WWII Peak (T6-T7)** | 3-6 sec | Integrated FC |
| **Post-War (T8-T9)** | 1-3 sec | Computer-assisted |
| **AEGIS (T10)** | 0.5-1 sec | Fully automated |

### Multi-Battery Targeting

From [[Surface-Combat]]:

| Targeting Mode | Spread Modifier | Rate of Fire | Use Case |
|----------------|-----------------|--------------|----------|
| **Concentrated** | 1.0x | Normal | Single dangerous target |
| **Split** | 1.15x per target | Normal | Multiple targets |
| **Rapid** | 1.20x | +20% | Overwhelming fire |
| **Deliberate** | 0.90x | -20% | Long-range precision |

*Note: These affect shell spread pattern, not arcade hit probability. Player must still aim correctly.*

### Turret Assignment

Players assign turret groups to targets:
- **Main Battery**: Primary target (usually largest threat)
- **Secondary Battery**: Secondary targets (escorts, aircraft)
- **AA Battery**: Aircraft priority
- **Torpedo Battery**: Best torpedo solution

---

## Ammunition Handling

### Ammunition Types (Quick Reference)

| Type | vs Armor | vs Structure | Crew Damage | Special |
|------|----------|--------------|-------------|---------|
| **AP** | Excellent | Poor | 0.3x | Penetration |
| **SAP** | Good | Good | 0.8x | Balanced |
| **HE** | Poor | Excellent | 1.5x | Fire chance |
| **AA** | N/A | N/A | N/A | Proximity fuze |
| **Star Shell** | N/A | N/A | N/A | Illumination |

### Ammunition Switching

| Current → New | Switch Time | Notes |
|---------------|-------------|-------|
| **Same Type** | 0 sec | No penalty |
| **Different Type** | +20% reload | One reload cycle |
| **Special (Star/AA)** | +30% reload | Loading adjustment |

---

## Integration with Other Systems

### Module System Integration
- Turrets are Weapon Hardpoints (L, XL slots)
- Crew cards assigned to turret positions
- Turret efficiency = Module efficiency formula

### Ballistics Integration
- Traverse/elevation determine if turret can bear on target
- Crew skill affects shell spread, not arcade hit chance
- Player must aim correctly; spread determines pattern around aim point
- See [[Ballistics-Gunnery-Mechanics]] for full spread calculations

### Crew System Integration
- Station vulnerability applies to turret crew
- Enclosed turrets: Armored (0.2x casualty)
- Open mounts: Exposed (2.0x casualty)

### Damage Integration
- Turret damage states from Surface-Combat
- Fire/flooding can reach turret positions
- Magazine detonation uses crew casualty calculations

---

## Historical Accuracy Notes

### Real-World References (For Database Guidance)

Actual turret values are defined in the Turret SO database. These historical values serve as reference for data entry:

| Weapon | Nation | Historical Traverse | Historical Reload | Notes |
|--------|--------|---------------------|-------------------|-------|
| **5"/38 Mk12** | USA | 25°/sec | 6 sec | Excellent DP |
| **4.7" Mk XII** | UK | 20°/sec | 8 sec | Standard DD |
| **12.7cm Type 89** | Japan | 16°/sec | 8 sec | DP mount |
| **10.5cm SK C/33** | Germany | 12°/sec | 5 sec | DP flak |
| **16"/50 Mk7** | USA | 4°/sec | 30 sec | Iowa-class |
| **15"/42 Mk I** | UK | 2°/sec | 36 sec | QE-class |
| **46cm Type 94** | Japan | 2°/sec | 40 sec | Yamato-class |

*Many turrets are already defined in the database with historically-researched values.*

### Design Simplifications

For gameplay purposes, the following simplifications are made:
1. **Loading angle**: All turrets can load at any elevation (real: some required return to fixed angle)
2. **Flash protection**: Abstracted into magazine detonation chance
3. **Training gear types**: Electric/hydraulic differences abstracted to tier
4. **Ammunition supply**: Simplified to ready rack + magazine
5. **Barrel wear**: Abstracted into turret damage system (no separate barrel replacement)

---

## Cross-References

- [[Surface-Combat]] - Combat flow, damage states
- [[Ballistics-Gunnery-Mechanics]] - Hit probability, dispersion
- [[Module-System]] - Hardpoint types, crew assignment
- [[Crew-Progression]] - Efficiency formula
- [[Crew-Management]] - Crew card assignment
- [[Modules/Weapons/_Weapons-Overview]] - Weapon types
- [[Modules/Fire-Control/_Fire-Control-Overview]] - Targeting systems

---

*Document created: 2025-12-10*
