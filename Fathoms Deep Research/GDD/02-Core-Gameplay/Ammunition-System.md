---
title: Ammunition System
category: core-gameplay
description: Cargo-based ammunition storage, depletion, and management mechanics
version: 1.0
last_updated: 2025-12-11
tags: [ammunition, combat, cargo, logistics, inventory]
status: CONFIRMED
---

# Ammunition System

> Ammunition is a strategic resource that must be managed carefully. Every shell fired is one less in your cargo hold, and running dry mid-battle can be fatal.

## Design Philosophy

The ammunition system creates meaningful logistics gameplay through:

1. **Strategic Planning** - Load the right ammo types before departure
2. **Cargo Tradeoffs** - Ammo competes with loot space
3. **Combat Tension** - Running low creates pressure to disengage
4. **Risk/Reward** - More ammo = longer fights but higher magazine detonation chance

---

## Core Mechanics

### Cargo-Only Storage

**CONFIRMED**: All ammunition is stored in the cargo grid. There are no separate magazine systems.

```
Ammunition Storage = Cargo Grid Only
- No turret-specific magazines
- All shells stored as cargo items
- Turrets draw directly from cargo with reload delay
```

**Design Rationale**: This creates meaningful logistics decisions. Players must balance:
- Loot capacity vs. combat endurance
- Shell types vs. versatility
- Ammo quantity vs. magazine detonation risk

---

## Ammunition Items

### Stacking by Caliber

**CONFIRMED**: Ammunition stacks by caliber. Stack size varies by shell size.

| Caliber Category | Example Calibers | Stack Size (1x1 slot) | Weight per Stack |
|------------------|------------------|----------------------|------------------|
| Small | 20mm, 40mm AA | 100 shells | Light |
| Light | 3", 4", 5" | 50 shells | Medium |
| Medium | 6", 8" | 30 shells | Heavy |
| Heavy | 10", 12", 14" | 20 shells | Very Heavy |
| Super-Heavy | 15", 16", 18" | 10 shells | Massive |

### Ammunition Types

Each caliber has multiple shell types:

| Shell Type | Code | Primary Use | Special Properties |
|------------|------|-------------|-------------------|
| Armor-Piercing | AP | Capital ships | Penetrates armor, risk of overpenetration |
| High-Explosive | HE | Soft targets | Area damage, fire chance, no penetration |
| Semi-AP | SAP | Cruisers | Balanced penetration and blast |
| AA Common | AAC | Aircraft | Proximity fuze, fragmentation |
| Incendiary | INC | Fire starting | High fire chance, low damage |
| Practice | PRC | Training | Reduced damage, cheaper |

### Cargo Grid Representation

Ammunition items in cargo:
```yaml
Ammunition_Item:
  name: "8-inch AP Shell"
  caliber: 8
  type: AP
  stack_size: 30
  grid_size: 1x1
  weight: 750kg (per stack)
  quality: N/A (ammunition has no quality variance)
```

---

## Combat Usage

### Firing and Depletion

When a turret fires:
1. System checks cargo for matching caliber + type
2. If found: Deduct shells from cargo, fire proceeds
3. If not found: Turret cannot fire (disabled state)

```
Fire_Sequence:
1. Player issues fire command
2. Check: Cargo contains [Caliber] + [Selected_Type]?
   - YES: Deduct shell count, process fire
   - NO: "Out of ammunition" - turret disabled
3. Reload timer begins
4. Repeat from step 1
```

### Ammunition Selection

**CONFIRMED**: Players must manually switch ammunition types.

- Each turret has a selected ammo type (default: AP)
- Player can change selection at any time
- Switching has no delay (instant type change)
- If selected type runs out, turret stops firing
- Player must manually switch to available type

**UI Indication**:
- Green: Selected type available in cargo
- Yellow: Low (< 10 salvos remaining)
- Red: Empty (0 shells of selected type)

### Turret Disabled State

When a turret has no matching ammunition:
- Turret shows red "EMPTY" indicator
- Cannot fire until player switches to available type
- OR player acquires more ammunition (unlikely mid-combat)

---

## Magazine Detonation

### Risk Scaling with Cargo

**CONFIRMED**: Magazine detonation chance scales with ammunition quantity in cargo.

```
Detonation_Trigger:
1. Shell penetrates armor into cargo area
2. Check: Is ammunition present?
   - NO: No detonation risk
   - YES: Roll for detonation

Detonation_Chance = Base_Chance × Ammo_Quantity_Modifier

Base_Chance: 0.01 (1%) - very low
Ammo_Quantity_Modifier: 1.0 + (Ammo_Stacks × 0.001)
```

**Example Calculations**:
| Ammo Stacks | Modifier | Effective Chance |
|-------------|----------|------------------|
| 10 stacks | 1.01× | 1.01% |
| 50 stacks | 1.05× | 1.05% |
| 100 stacks | 1.10× | 1.10% |
| 200 stacks | 1.20× | 1.20% |

**Design Note**: The risk increase is intentionally small. It creates a psychological factor without making heavy ammo loads suicidal.

### Detonation Requirements

For detonation to occur:
1. Shell must penetrate external armor
2. Shell must reach cargo hold area
3. Cargo must contain ammunition
4. Detonation roll must succeed

**Mitigation Strategies**:
- Spread ammunition across multiple cargo zones (if available)
- Bring minimum required ammunition
- Prioritize armor over cargo hold
- Extract early when ammo runs low

---

## Strategic Considerations

### Pre-Mission Planning

**Loadout Questions**:
1. What targets am I expecting? (AP vs HE balance)
2. How long will engagements be? (ammo quantity)
3. How much loot space do I need? (ammo vs cargo tradeoff)
4. Can I resupply mid-mission? (convoy operations)

### Recommended Loadouts by Mission Type

| Mission Type | AP % | HE % | Other | Notes |
|--------------|------|------|-------|-------|
| Convoy Raid | 20% | 70% | 10% AA | Merchants are soft targets |
| Capital Ship Hunt | 70% | 20% | 10% spare | Need penetration |
| Escort Duty | 30% | 40% | 30% AA | Balanced threat response |
| Extraction Run | 40% | 40% | 20% | General purpose, maximize loot space |
| Submarine Hunt | 10% | 50% | 40% DC | Depth charges over guns |

### Mid-Combat Decisions

**Running Low Triggers**:
- < 20% ammo: Consider disengagement
- < 10% ammo: Disengage unless victory certain
- 0% of primary type: Switch types or flee

**Emergency Options**:
1. Switch to secondary ammo type
2. Disengage and extract
3. Call for allied resupply
4. Jettison other cargo to signal surrender (if applicable)

---

## Resupply

### At Port

Full ammunition resupply available at friendly ports:
- Purchase from NPC vendors
- Market prices (supply/demand affected)
- Immediate loading to cargo

### At Sea

Limited resupply options:
- **Allied convoy**: Transfer ammunition between ships (slow process)
- **Capture enemy ship**: Loot enemy ammunition (caliber must match)
- **Supply ship**: Dedicated resupply vessels can transfer at sea

### Resupply Time

```
Transfer_Time = Base_Time × Stack_Count × Ship_Distance_Modifier

Base_Time: 30 seconds per stack
Ship_Distance_Modifier: 1.0 at 100m, 2.0 at 500m
```

---

## Ammunition and Economy

### Cost Factors

Ammunition cost varies by:
- Caliber (larger = more expensive)
- Type (specialty rounds cost more)
- Port supply/demand
- Wartime scarcity

### Price Examples (Baseline)

| Caliber | AP (per stack) | HE (per stack) | Notes |
|---------|----------------|----------------|-------|
| 5" | 500 credits | 400 credits | Common DD ammo |
| 8" | 2,000 credits | 1,600 credits | Cruiser standard |
| 14" | 8,000 credits | 6,000 credits | Battleship |
| 16" | 15,000 credits | 12,000 credits | Super-battleship |

### Economic Pressure

Heavy combat creates significant ammunition costs:
- A battleship salvo might cost 1,000+ credits
- Extended engagements can cost 50,000+ credits in ammo alone
- This creates incentive to win quickly and efficiently

---

## Cross-References

- [[Cargo-System]] - How cargo grid works
- [[Ballistics-Gunnery]] - How shells behave after firing
- [[Damage-Model]] - Penetration and detonation mechanics
- [[Economy-System]] - Ammunition pricing
- [[Extraction-Mechanics]] - Cargo tradeoffs during loot runs

---

## Changelog

- **2025-12-11**: Initial document creation from Q&A session
  - Confirmed: Cargo-only system (no magazines)
  - Confirmed: Stacking by caliber
  - Confirmed: Manual ammo type switching
  - Confirmed: Magazine detonation scales with ammo quantity
