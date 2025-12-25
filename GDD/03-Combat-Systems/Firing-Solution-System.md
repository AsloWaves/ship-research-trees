---
title: Firing Solution System
category: combat-systems
description: Authoritative mechanics for fire control targeting solutions, buildup, degradation, and accuracy
version: 1.0
last_updated: 2025-12-11
status: implemented
tags: [combat, fire-control, targeting, accuracy, formulas, authoritative]
---

# Firing Solution System

> **AUTHORITATIVE DOCUMENT**: This document supersedes firing solution mechanics in Detection-System.md and Ballistics-Gunnery-Mechanics.md. Those documents should reference this one for solution calculations.

## Design Philosophy

The firing solution represents your ship's fire control system's ability to predict where shells need to land to hit a moving target. Unlike simple "lock-on" systems in arcade games, Fathoms Deep models the realistic complexity of naval fire control:

1. **Solutions are Earned** - You can't just point and shoot; you need time to calculate
2. **Solutions are Fragile** - Maneuvers by either ship degrade your solution
3. **Equipment Matters** - Fire control technology dramatically affects capability
4. **Patience is Rewarded** - Waiting for a good solution vs. spray-and-pray

---

## Core Concept: The Living Solution

The firing solution is a **continuously calculated percentage** (0-100%) representing how accurately your fire control system can predict target position. It changes every moment based on:

- Your fire control equipment quality
- Target tracking stability
- Your own ship's maneuvers
- Environmental conditions
- Sensor contact quality

```
Current_Solution = Previous_Solution + (Buildup_Rate - Degradation_Rate) × Time_Delta
```

---

## Solution States

### Visual Indicator

| Solution Range | UI Color | Bar Fill | Tactical Meaning |
|----------------|----------|----------|------------------|
| 0-25% | Red | 0-25% | **NO FIRE** - Wasting ammunition |
| 26-50% | Orange | 26-50% | **SUPPRESSION** - Area denial only |
| 51-75% | Yellow | 51-75% | **MARGINAL** - Reasonable hit chance |
| 76-90% | Light Green | 76-90% | **GOOD** - Effective engagement |
| 91-100% | Bright Green | 91-100% | **OPTIMAL** - Fire for effect |

### Solution-to-Accuracy Modifier

This table defines how solution quality affects your hit probability:

| Solution % | Accuracy Modifier | Reasoning |
|------------|-------------------|-----------|
| 0-10% | ×0.10 | Blind fire - almost no chance |
| 11-25% | ×0.25 | Very poor - minimal calculation |
| 26-50% | ×0.50 | Developing - basic prediction |
| 51-75% | ×0.75 | Good - solid fire control |
| 76-90% | ×0.90 | Excellent - refined calculation |
| 91-100% | ×1.00 | Perfect - maximum system capability |

**Continuous Formula:**
```
If Solution <= 50%:
    Accuracy_Modifier = Solution × 0.01  (linear: 0% = 0.0, 50% = 0.5)

If Solution > 50%:
    Accuracy_Modifier = 0.50 + (Solution - 50) × 0.01  (linear: 51% = 0.51, 100% = 1.0)
```

---

## Fire Control Equipment Tiers

Equipment tier determines both buildup rate and maximum achievable solution.

### Tier Definitions

| Tier | Equipment Name | Era | Example Systems |
|------|----------------|-----|-----------------|
| **Basic** | Manual Fire Control | Pre-1920 | Optical sights, manual rangefinding, voice orders |
| **Standard** | Mechanical Fire Control | 1920-1940 | Fire control directors, mechanical computers |
| **Advanced** | Electro-Mechanical | 1940-1960 | Radar fire control, analog computers, Mark 37/Mark 68 |
| **Modern** | Digital Fire Control | 1960+ | Digital computers, automatic tracking, Aegis |

### Buildup Rates

How fast solution builds when tracking a stable target in Phase 3+:

| Equipment Tier | Base Buildup Rate | Notes |
|----------------|-------------------|-------|
| **Basic** | +1%/sec | Very slow; requires continuous stable tracking |
| **Standard** | +3%/sec | Mechanical calculation assists |
| **Advanced** | +6%/sec | Electro-mechanical computers |
| **Modern** | +12%/sec | Digital processing, automatic tracking |

### Solution Caps

Maximum achievable solution regardless of conditions:

| Equipment Tier | Maximum Solution | Reasoning |
|----------------|------------------|-----------|
| **Basic** | 60% | Manual methods can only estimate, never precise |
| **Standard** | 80% | Mechanical computers improve significantly |
| **Advanced** | 95% | Radar ranging + analog computers approach perfection |
| **Modern** | 100% | Digital systems can achieve theoretical maximum |

**Design Note**: Even with perfect conditions and unlimited time, Basic equipment cannot exceed 60% solution. This represents the fundamental limitation of human estimation vs. mechanical calculation.

---

## Buildup Modifiers

These modifiers affect the buildup rate (multiplicative with base rate):

### Fire Control Enhancements

| Enhancement | Buildup Modifier | Requirements |
|-------------|------------------|--------------|
| Fire Control Radar Lock | +50% | FC radar module + target locked |
| Optical Rangefinder Active | +25% | Rangefinder module + visual contact |
| Radar Ranging (no lock) | +15% | Search radar providing range data |
| Fire Control Director | +10% | Director tower module installed |

### Target Behavior

| Target Condition | Buildup Modifier |
|------------------|------------------|
| Stationary (0 knots) | +30% |
| Steady course (no turn) | +20% |
| Constant speed (±2 knots) | +15% |
| Predictable zigzag pattern | +5% |

### Environmental

| Condition | Buildup Modifier |
|-----------|------------------|
| Calm seas (State 0-2) | +10% |
| Clear visibility | +5% |

### Combined Buildup Example

```
Equipment: Advanced (+6%/sec base)
Modifiers:
  + FC Radar Lock: +50%
  + Target steady course: +20%
  + Calm seas: +10%

Effective_Buildup = 6%/sec × (1 + 0.50 + 0.20 + 0.10)
                 = 6%/sec × 1.80
                 = 10.8%/sec

Time to 95% cap from 0%: 95 / 10.8 = ~9 seconds
```

---

## Degradation Mechanics

Degradation occurs continuously and subtracts from buildup. If degradation exceeds buildup, solution drops.

### Your Ship Movement

| Action | Degradation Rate | Duration |
|--------|------------------|----------|
| Steady course & speed | 0%/sec | - |
| Minor course correction (<10°) | -1%/sec | While turning |
| Moderate turn (10-30°) | -3%/sec | While turning |
| Hard turn (>30°) | -6%/sec | While turning |
| Emergency/evasive maneuver | -10%/sec | While maneuvering + 3 sec after |
| Speed change (±5 knots) | -2%/sec | For 5 seconds |
| Speed change (±10+ knots) | -4%/sec | For 8 seconds |

### Target Movement

| Target Action | Degradation Rate |
|---------------|------------------|
| Steady course & speed | 0%/sec |
| Minor course change (<10°) | -2%/sec |
| Moderate turn (10-30°) | -5%/sec |
| Hard turn (>30°) | -10%/sec |
| Speed change (±5 knots) | -3%/sec |
| Speed change (±10+ knots) | -6%/sec |
| Evasive zigzag pattern | -8%/sec |
| Erratic maneuvering | -12%/sec |

### Contact Quality

| Condition | Degradation Rate |
|-----------|------------------|
| Full contact (Phase 4) | 0%/sec |
| Good contact (Phase 3) | 0%/sec |
| Degrading contact | -3%/sec |
| Target entering smoke | -8%/sec |
| Target in smoke screen | -15%/sec |
| Radar contact only (no visual) | -1%/sec |
| Losing radar contact | -10%/sec |
| Losing visual contact | -8%/sec |
| Complete contact loss | -25%/sec |

### Environmental Degradation

| Condition | Degradation Rate |
|-----------|------------------|
| Moderate seas (State 3-4) | -1%/sec |
| Heavy seas (State 5-6) | -3%/sec |
| Storm conditions (State 7+) | -6%/sec |
| Radar jamming active | -5%/sec |
| Chaff/decoys in area | -3%/sec |

---

## Net Solution Change Formula

```
Net_Change = (Base_Buildup × Buildup_Modifiers) - Total_Degradation

New_Solution = Current_Solution + (Net_Change × Time_Delta)
New_Solution = Clamp(New_Solution, 0, Equipment_Cap)
```

---

## Worked Examples

### Example A: Stable Battleship Engagement

**Scenario**: USS Iowa (Advanced fire control) engaging IJN Yamato at 20km

**Conditions**:
- Both ships: Steady course, constant speed
- Weather: Calm seas, clear day
- Fire control radar: Locked

**Calculation**:
```
Base Buildup: +6%/sec (Advanced)
  + FC Radar Lock: +50% = +3%/sec
  + Target steady: +20% = +1.2%/sec
  + Calm seas: +10% = +0.6%/sec
Total Buildup: +10.8%/sec

Degradation:
  Your movement: 0%/sec (steady)
  Target movement: 0%/sec (steady)
  Contact: 0%/sec (full)
Total Degradation: 0%/sec

Net Change: +10.8%/sec
Time to 95% cap: 8.8 seconds

Result: Perfect firing conditions - wait 9 seconds, then fire with 95% solution
```

### Example B: Destroyer Knife Fight

**Scenario**: USS Fletcher (Standard fire control) vs IJN Fubuki at 5km

**Conditions**:
- Both ships: Maneuvering aggressively
- Fletcher: Hard turn, full speed
- Fubuki: Moderate turns, erratic speed changes

**Calculation**:
```
Base Buildup: +3%/sec (Standard)
  + No radar lock (too close/fast)
  + Target NOT steady: 0%
Total Buildup: +3%/sec

Degradation:
  Your hard turn: -6%/sec
  Target moderate turn: -5%/sec
  Target speed changes: -6%/sec
Total Degradation: -17%/sec

Net Change: +3 - 17 = -14%/sec

Result: Solution DROPPING rapidly at -14%/sec!
Current 60% solution → 0% in 4.3 seconds

Tactical Choice: Stabilize course to shoot, or keep maneuvering to survive
```

### Example C: Cruiser vs Smoke Screen

**Scenario**: HMS Belfast (Advanced) engaging German destroyer making smoke

**Conditions**:
- Belfast: Steady course
- Target: Entering smoke screen

**Calculation**:
```
Base Buildup: +6%/sec (Advanced)
  + Target NOT steady: 0%
  + Radar searching smoke: +15% = +0.9%/sec
Total Buildup: +6.9%/sec

Degradation:
  Your movement: 0%/sec (steady)
  Target in smoke: -15%/sec
Total Degradation: -15%/sec

Net Change: +6.9 - 15 = -8.1%/sec

Result: Solution collapsing at -8.1%/sec
80% solution → 0% in 9.9 seconds

Tactical Options:
  1. Fire immediately at current solution (diminishing)
  2. Close range to regain visual
  3. Switch to radar-only tracking (reduces degradation)
```

### Example D: Basic Equipment Limitation

**Scenario**: Pre-WWI battleship with Basic fire control

**Conditions**:
- Perfect conditions: calm seas, steady target, good visibility
- Optical rangefinder active

**Calculation**:
```
Base Buildup: +1%/sec (Basic)
  + Rangefinder: +25% = +0.25%/sec
  + Target steady: +20% = +0.2%/sec
  + Calm seas: +10% = +0.1%/sec
Total Buildup: +1.55%/sec

Degradation: 0%/sec (perfect conditions)

Net Change: +1.55%/sec
Time to 60% cap: 38.7 seconds

Result: Even with PERFECT conditions, takes 39 seconds to reach maximum
Maximum solution: 60% = ×0.60 accuracy modifier

Compare to Advanced: 9 seconds to 95% = ×0.95 accuracy modifier
```

---

## Special Mechanics

### Manual Rangefinding (Basic Equipment)

Ships with Basic fire control can use manual rangefinding to improve accuracy:

1. **Player Action**: Manually estimate range using crosshairs
2. **Accuracy Check**: Compare estimate to actual range
3. **Bonus Applied**: If within ±10%, gain +15% solution immediately
4. **Cooldown**: 10 seconds between manual ranging attempts

This gives skilled players a way to overcome Basic equipment limitations through active play.

### Solution Lock

Once solution reaches 90%+, it becomes "locked" with reduced degradation:

- **Locked Degradation**: All degradation rates reduced by 50%
- **Lock Break**: Drops below 80% OR target executes hard maneuver OR contact lost

This prevents frustrating solution "hunting" at high values where small movements cause constant fluctuation.

### Salvo Timing

Firing a salvo temporarily freezes solution at current value:

- **Freeze Duration**: Equal to shell flight time
- **Reason**: Shells are "in the air" calculated against that solution
- **Next Salvo**: Uses new (updated) solution

This prevents the unrealistic tactic of firing salvos in rapid succession hoping one catches favorable solution fluctuation.

---

## Fire Control Module Integration

Fire control modules provide the equipment tier and additional bonuses:

### Module-to-Tier Mapping

| Module ID | Module Name | Tier | Base Buildup | Cap |
|-----------|-------------|------|--------------|-----|
| FC-001 | Basic Rangefinder | Basic | +1%/sec | 60% |
| FC-002 | Coincidence Rangefinder | Basic+ | +1.5%/sec | 65% |
| FC-003 | Fire Control Director | Standard | +3%/sec | 80% |
| FC-004 | Analog Fire Computer | Standard+ | +4%/sec | 85% |
| FC-005 | Radar Fire Control | Advanced | +6%/sec | 95% |
| FC-006 | Digital Fire Control | Modern | +12%/sec | 100% |

### Stacking Rules

- **Base tier**: Determined by highest fire control module installed
- **Multiple modules**: Best module determines tier; others provide +0.5%/sec each (max +1.5%)
- **Radar integration**: Requires separate radar module for radar bonuses

---

## Detection System Integration

The Firing Solution System depends on Detection Phase:

| Detection Phase | Solution Capability |
|-----------------|---------------------|
| Phase 1 (Direction only) | Cannot build solution |
| Phase 2 (Shadow) | Cannot build solution (target not identified) |
| Phase 3 (Visible) | Solution builds normally |
| Phase 4 (Full Detail) | Solution builds with +10% bonus |

**Blind Fire**: Firing at Phase 1-2 contacts uses fixed 5% accuracy (no solution calculation).

---

## Gunnery Integration

The solution modifier feeds directly into the hit probability formula:

```
Hit_Probability = Base_Accuracy
                  × Solution_Modifier      ← FROM THIS SYSTEM
                  × Range_Modifier
                  × Fire_Control_Modifier
                  × Target_Speed_Modifier
                  × Shooter_Movement_Modifier
                  × Weather_Modifier
                  × Crew_Skill_Modifier
                  × Targeting_Mode_Modifier
```

See [[Ballistics-Gunnery-Mechanics]] for the complete hit probability calculation.

---

## Balance Rationale

### Why These Rates?

**Basic (1%/sec, 60% cap)**:
- Pre-WWI ships had no fire control computers
- Manual rangefinding was error-prone
- Even with perfect conditions, significant inaccuracy
- Creates strong upgrade incentive

**Standard (3%/sec, 80% cap)**:
- Interwar mechanical computers improved significantly
- Ford Mark 37 director revolutionized US Navy gunnery
- Still limited by analog calculation speed
- Meaningful improvement over Basic

**Advanced (6%/sec, 95% cap)**:
- WWII radar fire control was revolutionary
- Night fighting became possible
- Near-perfect accuracy achievable
- Represents peak WWII technology

**Modern (12%/sec, 100% cap)**:
- Digital computers process instantly
- Automatic tracking removes human delay
- Only limited by sensor precision
- Theoretical maximum achievable

### Why Degradation Matters

Degradation creates tactical decisions:
- **Stand and Fight**: Maintain course for accuracy, accept vulnerability
- **Dodge and Weave**: Sacrifice accuracy for survivability
- **Smoke and Mirrors**: Force enemy to lose solution

Without degradation, combat becomes static - whoever sees first wins. With degradation, maneuvering matters throughout the engagement.

---

## Implementation Notes

### Update Frequency

```csharp
// Update solution every 0.1 seconds for smooth display
private float solutionUpdateInterval = 0.1f;

// Recalculate buildup/degradation every 0.5 seconds (performance)
private float modifierRecalcInterval = 0.5f;
```

### Display Smoothing

Solution bar should animate smoothly, not jump:
- **Lerp Rate**: 5× actual change rate
- **Color Transitions**: Fade between states over 0.5 seconds

### Network Sync

- Solution is **server-authoritative**
- Client predicts locally for responsive UI
- Server corrects with ~100ms tolerance
- Large discrepancies trigger immediate sync

---

## Cross-References

- [[Detection-System]] - Detection phases and contact information
- [[Ballistics-Gunnery-Mechanics]] - Hit probability formula using solution
- [[../Modules/Fire-Control/_Fire-Control-Overview]] - Fire control module stats
- [[../Modules/Bridge/_Bridge-Modules-Index]] - Bridge tier capabilities
- [[Combat-Overview]] - Overall combat system context

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-11 | Initial authoritative document; resolved contradictions between Detection-System.md and Ballistics-Gunnery.md |

---

*This document provides the authoritative firing solution mechanics for Fathoms Deep. Other documents should reference this for solution calculations.*
