# Aircraft Modules Overview
**Category**: Aircraft / Aviation
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Aircraft modules enable carriers and seaplane-equipped ships to operate aircraft. This includes hangars, catapults, arresting gear, and aviation fuel systems. These modules are essential for carrier gameplay.

---

## Aircraft Module Types

### Hangars
Aircraft storage and maintenance.

| Type | Capacity | Notes |
|------|----------|-------|
| Open Hangar | Low | Exposed to weather |
| Enclosed Hangar | Medium | Protected, standard |
| Armored Hangar | High | Protected from bombs |

**Hangar Stats**:
- Aircraft Capacity
- Maintenance Speed (ready time)
- Protection Level
- Fire Suppression

### Catapults
Aircraft launch systems.

| Type | Era | Aircraft Weight |
|------|-----|-----------------|
| None | All | Deck run only |
| Hydraulic | T3+ | Light aircraft |
| Steam | T5+ | Medium aircraft |
| EMALS | T10 | All aircraft |

**Catapult Stats**:
- Launch Rate (aircraft per minute)
- Maximum Aircraft Weight
- Crew Required

### Arresting Gear
Aircraft recovery systems.

| Type | Era | Notes |
|------|-----|-------|
| None | T1-T3 | Deck landing only |
| Wire System | T4+ | Standard carrier |
| Barricade | T4+ | Emergency barrier |
| Angled Deck | T8+ | Simultaneous ops |

**Arresting Stats**:
- Recovery Rate (aircraft per minute)
- Maximum Aircraft Weight
- Failure Chance (crash on deck)

### Aviation Fuel
Aircraft fuel storage and handling.

| Type | Capacity | Notes |
|------|----------|-------|
| Basic Avgas Tank | Low | Small capacity |
| Standard Avgas | Medium | Standard carrier |
| Protected Avgas | High | Armored, fire suppressed |

**Fuel Stats**:
- Fuel Capacity (sorties)
- Transfer Rate (refuel speed)
- Fire Risk (explosion chance if hit)

### Elevators
Move aircraft between hangar and flight deck.

| Type | Speed | Notes |
|------|-------|-------|
| Single | Slow | One aircraft at a time |
| Dual | Medium | Two elevators |
| Deck-Edge | Fast | External, faster cycling |

---

## Aircraft Operations

### Launch Cycle
```
Aircraft in Hangar
      │
      ▼
Arm & Fuel (Hangar) ──► Time based on crew skill
      │
      ▼
Elevator to Deck ──► Time based on elevator type
      │
      ▼
Position on Catapult/Deck
      │
      ▼
LAUNCH ──► Catapult reduces takeoff time
```

### Recovery Cycle
```
Aircraft Returns
      │
      ▼
Approach & Land ──► Arresting gear catches
      │
      ▼
Clear Deck
      │
      ▼
Elevator to Hangar ──► Time based on elevator type
      │
      ▼
Rearm & Refuel ──► Ready for next sortie
```

---

## Module Template

```markdown
# [Aircraft Module Name]
**Type**: [Hangar / Catapult / Arresting Gear / Aviation Fuel]
**Nation**: [Origin country]
**Tier**: T[X]

## Specifications
| Stat | Value |
|------|-------|
| [Primary Stat] | X |
| Crew Required | X |
| Weight | X tons |

## Aircraft Compatibility
| Aircraft Type | Compatible |
|---------------|------------|
| Fighters | [Yes/No] |
| Torpedo Bombers | [Yes/No] |
| Dive Bombers | [Yes/No] |
| Scouts | [Yes/No] |

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Flight Deck Crew | X | X |
| Hangar Crew | X | X |

## Installation Requirements
- Ship Class: CV, CVL, CVE, Seaplane Tender
- Slot Type: Internal / Deck
- Slot Size: [L / XL]

## Historical Notes
[Brief historical context]
```

---

## Aircraft Modules by Nation

### United States
- [[Hangar-Essex-Class]] - Standard fleet carrier
- [[H-4-Hydraulic-Catapult]] - Light catapult
- [[H-8-Steam-Catapult]] - Heavy catapult
- [[Mk-4-Arresting-Gear]] - Standard recovery
- [More to be added...]

### Japan
- [[Hangar-Shokaku-Class]] - Fleet carrier
- [[Kure-Type-Catapult]] - Standard catapult
- [More to be added...]

### Great Britain
- [[Hangar-Illustrious-Class]] - Armored carrier
- [[BH-III-Catapult]] - Standard RN catapult
- [More to be added...]

---

## Cross-References

- [[03-Combat-Systems/Carrier-Operations]] - Air operations gameplay
- [[02-Core-Gameplay/AI-NPC-System]] - Carrier AI brain
- [[04-Ship-Customization/Module-System]] - Module mechanics

---

*Category created: 2025-12-03*
