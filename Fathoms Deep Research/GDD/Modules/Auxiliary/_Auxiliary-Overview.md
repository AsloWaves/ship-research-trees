# Auxiliary Modules Overview
**Category**: Auxiliary
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Auxiliary modules provide support systems that keep the ship running. This includes electrical generators, pumps, winches, and other systems that don't fit neatly into other categories but are essential for ship operation.

---

## Auxiliary Types

### Generators
Electrical power generation.

| Type | Era | Output |
|------|-----|--------|
| Steam Turbine Generator | T1+ | Medium |
| Diesel Generator | T3+ | High efficiency |
| Gas Turbine Generator | T8+ | High output |
| Nuclear Generator | T9+ | Very high |

**Generator Stats**:
- Power Output (kW)
- Fuel Consumption
- Weight (tons)
- Noise Level (submarine detection risk)

### Power Requirements
Modules require electrical power to operate.

| System | Typical Power Draw |
|--------|-------------------|
| Radar | 50-200 kW |
| Fire Control | 30-100 kW |
| Sonar | 20-80 kW |
| Communications | 10-50 kW |
| Lighting | 20-50 kW |
| Weapons (powered) | 50-500 kW |

**Power Mechanics**:
```
Total Power Required = Sum of all active systems
If Required > Generated: Systems start failing
Priority: Life support > Propulsion > Weapons > Sensors
```

### Pumps
Fluid transfer systems.

| Type | Function |
|------|----------|
| Bilge Pump | Remove flooding |
| Fuel Transfer | Move fuel between tanks |
| Fire Main | Water for firefighting |
| Ballast Pump | Submarine/trim control |

### Winches & Cranes
Cargo and equipment handling.

| Type | Function |
|------|----------|
| Anchor Windlass | Anchor handling |
| Cargo Crane | Load/unload cargo |
| Boat Davit | Launch/recover boats |
| Aircraft Crane | Handle seaplanes |

### Refrigeration
Food and ammunition storage.

| Type | Function |
|------|----------|
| Provisions Cold Storage | Food preservation |
| Magazine Cooling | Ammunition safety |
| Air Conditioning | Crew comfort (affects morale) |

---

## Power Management

### Power Balance
Ships must generate enough power for all systems.

| Status | Effect |
|--------|--------|
| Surplus | All systems operational |
| Balanced | Normal operation |
| Deficit | Systems shut down by priority |
| Critical | Emergency power only |

### Emergency Power
When main power fails:
- Battery backup for critical systems
- Emergency diesel generators
- Limited duration operation

---

## Module Template

```markdown
# [Auxiliary Module Name]
**Type**: [Generator / Pump / Winch / etc.]
**Nation**: [Origin country]
**Tier**: T[X]

## Specifications
| Stat | Value |
|------|-------|
| [Primary Output] | X |
| Fuel Consumption | X units/hour |
| Weight | X tons |
| Noise Level | [Low/Medium/High] |

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Engineer | X | X |

## Installation Requirements
- Ship Class: [All / Specific]
- Slot Type: Internal
- Slot Size: [S / M / L]

## Historical Notes
[Brief historical context]
```

---

## Auxiliary Modules by Type

### Generators
- [[150kW-Steam-Generator]] - Small ship standard
- [[500kW-Diesel-Generator]] - Destroyer standard
- [[1000kW-Turbo-Generator]] - Cruiser/battleship
- [[2000kW-Ship-Service-Generator]] - Capital ship
- [More to be added...]

### Pumps
- [[500-GPM-Bilge-Pump]] - Standard bilge
- [[1000-GPM-Fire-Main]] - Firefighting
- [[Fuel-Transfer-Pump]] - Fuel management
- [More to be added...]

### Miscellaneous
- [[Standard-Anchor-Windlass]] - Anchor handling
- [[Cargo-Boom-5-Ton]] - Light cargo
- [[Provisions-Refrigerator]] - Food storage
- [More to be added...]

---

## Cross-References

- [[Modules/Engines/_Engines-Overview]] - Primary power source
- [[Modules/Utilities/_Utilities-Overview]] - Related systems
- [[04-Ship-Customization/Module-System]] - Module mechanics
- [[03-Combat-Systems/Damage-Model]] - Power loss effects

---

*Category created: 2025-12-03*
