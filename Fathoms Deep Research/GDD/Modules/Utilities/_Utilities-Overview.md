# Utilities Modules Overview
**Category**: Utilities
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Utility modules provide support functions that keep the ship operational. This includes damage control, repair systems, medical facilities, and storage. These modules don't deal damage but are essential for survival.

---

## Utility Types

### Damage Control
Systems that prevent and mitigate damage.

| Type | Function |
|------|----------|
| Fire Suppression | Extinguish fires |
| Flooding Control | Pump out water |
| Damage Repair | Patch hull breaches |
| Emergency Power | Backup electrical |

**Damage Control Stats**:
- Fire Suppression Rate (% per second)
- Flooding Pump Rate (tons per minute)
- Repair Speed (HP per minute)
- Crew Required

### Repair Systems
At-sea repair capability.

| Type | Repairs |
|------|---------|
| Hull Repair | Structural damage |
| Machinery Repair | Engine/systems |
| Weapon Repair | Disabled weapons |
| Electrical Repair | Power systems |

**Repair Stats**:
- Repair Rate (HP/min)
- Maximum Repairable (% of total)
- Resource Cost (repair materials)
- Crew Required

### Medical Facilities
Crew treatment and recovery.

| Type | Function |
|------|----------|
| First Aid Station | Basic treatment |
| Sick Bay | Standard medical |
| Surgery | Major treatment |
| Hospital Ship | Full medical (support ships) |

**Medical Stats**:
- Treatment Rate (crew per minute)
- Recovery Bonus (%)
- Casualty Prevention (% chance to save)

### Storage
Cargo and resource storage.

| Type | Contents |
|------|----------|
| Ammunition Magazine | Shell storage |
| Fuel Bunkers | Fuel storage |
| Cargo Hold | Trade goods |
| Provisions | Food/supplies |
| Repair Materials | Repair resources |

**Storage Stats**:
- Capacity (units)
- Protection (explosion risk for ammo)
- Access Speed (load/unload rate)

---

## Damage Control Mechanics

### Fire Fighting
```
Fire Spread Rate - Fire Suppression Rate = Net Fire Change
```

| Fire Level | Effect |
|------------|--------|
| None | Normal operation |
| Minor | -5% efficiency nearby |
| Moderate | -15% efficiency, spreading |
| Major | -30% efficiency, heavy damage |
| Uncontrolled | Ship loss imminent |

### Flooding Control
```
Water Intake - Pump Rate = Net Flooding
```

| Flooding Level | Effect |
|----------------|--------|
| None | Normal operation |
| Minor | -5% speed |
| Moderate | -15% speed, listing |
| Major | -30% speed, capsizing risk |
| Critical | Ship sinking |

---

## Module Template

```markdown
# [Utility Module Name]
**Type**: [Damage Control / Repair / Medical / Storage]
**Nation**: [Origin country]
**Tier**: T[X]

## Specifications
| Stat | Value |
|------|-------|
| [Primary Stat] | X |
| Crew Required | X |
| Power Required | X kW |
| Weight | X tons |

## Effectiveness
[Specific capability details]

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Damage Control | X | X |

## Installation Requirements
- Ship Class: [All / Specific]
- Slot Type: Internal
- Slot Size: [S / M / L]

## Historical Notes
[Brief historical context]
```

---

## Utilities by Nation

### United States
- [[Mk-I-Damage-Control-Station]] - Standard DC
- [[1000-GPM-Bilge-Pump]] - Flooding control
- [[Standard-Sick-Bay]] - Medical facility
- [More to be added...]

### General (All Nations)
- [[Basic-Fire-Suppression]] - T1 fire fighting
- [[Standard-Damage-Control]] - T3 DC station
- [[Advanced-Damage-Control]] - T6 DC station
- [[Repair-Workshop]] - At-sea repairs
- [More to be added...]

---

## Cross-References

- [[03-Combat-Systems/Damage-Model]] - How damage works
- [[04-Ship-Customization/Module-System]] - Module mechanics
- [[02-Core-Gameplay/Crew-Management]] - Crew casualties
- [[Modules/Auxiliary/_Auxiliary-Overview]] - Related systems

---

*Category created: 2025-12-03*
