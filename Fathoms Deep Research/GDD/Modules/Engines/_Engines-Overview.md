# Propulsion Modules Overview
**Category**: Engines / Propulsion
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Propulsion modules provide the motive power for ships. This includes engines, boilers, propellers, and steering systems. Engine choice significantly affects speed, fuel consumption, and reliability.

---

## Propulsion Types

### Engines

| Type | Era | Characteristics |
|------|-----|-----------------|
| Reciprocating Steam | T1-T4 | Reliable, inefficient, heavy |
| Steam Turbine | T3-T8 | High power, fuel hungry |
| Diesel | T2-T10 | Efficient, good range |
| Diesel-Electric | T4-T10 | Quiet, flexible |
| Gas Turbine | T8-T10 | High power, fast response |
| Nuclear | T9-T10 | Unlimited range, expensive |

### Engine Characteristics

| Stat | Description |
|------|-------------|
| Power Output | Shaft horsepower (SHP) |
| Efficient Consumption | Fuel use at cruise speed |
| Natural Consumption | Fuel use at standard speed |
| Max Consumption | Fuel use at flank speed |
| Weight | Engine weight (tons) |
| Reliability | Breakdown chance |
| Noise | Detection modifier |

### Boilers
Steam generation for steam-powered ships.

| Type | Characteristics |
|------|-----------------|
| Coal-Fired | T1-T3, dirty, labor intensive |
| Oil-Fired | T3-T8, cleaner, more efficient |
| High-Pressure | T5-T8, more power, more maintenance |
| Nuclear Reactor | T9-T10, unlimited steam |

### Propellers
Convert engine power to thrust.

| Type | Effect |
|------|--------|
| Single Screw | Simple, less maneuverable |
| Twin Screw | Standard, good balance |
| Triple Screw | High power, complex |
| Quadruple Screw | Maximum power, capital ships |

**Propeller Stats**:
- Diameter
- Pitch
- Efficiency (%)
- Cavitation threshold

### Rudders
Ship steering systems.

| Type | Characteristics |
|------|-----------------|
| Single Rudder | Standard, simple |
| Twin Rudder | Better maneuverability |
| Semi-Balanced | Reduced steering force |
| Spade Rudder | Modern, efficient |

---

## Fuel System

### Consumption Rates

Each engine has three consumption rates:

| Rate | Usage | Speed |
|------|-------|-------|
| Efficient | Lowest fuel use | ~60% max speed |
| Natural | Balanced | ~80% max speed |
| Maximum | Highest fuel use | 100% max speed |

### Fuel Types

| Fuel | Era | Notes |
|------|-----|-------|
| Coal | T1-T3 | Heavy, dirty, limited range |
| Fuel Oil | T3-T10 | Standard naval fuel |
| Diesel | T2-T10 | Efficient, common |
| Aviation Fuel | T4-T10 | For carriers (separate tank) |

---

## Module Template

```markdown
# [Engine Name]
**Type**: [Steam Turbine / Diesel / etc.]
**Nation**: [Origin country]
**Tier**: T[X]

## Specifications
| Stat | Value |
|------|-------|
| Power Output | X SHP |
| Efficient Consumption | X units/min |
| Natural Consumption | X units/min |
| Maximum Consumption | X units/min |
| Weight | X tons |
| Reliability | X% |
| Noise Level | [Low / Medium / High] |

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Engineer | X | X |
| Stoker | X | X |

## Installation Requirements
- Ship Class: [DD / CL / CA / BB / CV / SS]
- Minimum Tier: TX
- Slot Type: Internal
- Slot Size: [L / XL]

## Performance Curves
[Speed vs Fuel consumption data]

## Historical Notes
[Brief historical context]
```

---

## Engines by Nation

### United States
- [[Westinghouse-Geared-Turbine-T4]] - Standard destroyer
- [[GE-Turbo-Electric-T5]] - Battleship drive
- [[Fairbanks-Morse-Diesel-T6]] - Submarine main
- [More to be added...]

### Great Britain
- [[Parsons-Geared-Turbine-T4]] - Standard RN turbine
- [[Admiralty-3-Drum-Boiler-T5]] - Standard boiler
- [More to be added...]

### Japan
- [[Kanpon-Turbine-T5]] - Standard IJN turbine
- [[Kampon-Boiler-T5]] - High-pressure boiler
- [More to be added...]

### Germany
- [[MAN-Diesel-T5]] - Submarine diesel
- [[Wagner-High-Pressure-Boiler-T6]] - Advanced boiler
- [More to be added...]

---

## Propulsion by Ship Class

| Ship Class | Typical Propulsion | Power Range |
|------------|-------------------|-------------|
| PT Boat | Diesel / Gas Turbine | 1,000-5,000 SHP |
| Destroyer | Steam Turbine | 30,000-70,000 SHP |
| Light Cruiser | Steam Turbine | 75,000-100,000 SHP |
| Heavy Cruiser | Steam Turbine | 100,000-150,000 SHP |
| Battleship | Steam Turbine / Turbo-Electric | 100,000-220,000 SHP |
| Carrier | Steam Turbine | 150,000-280,000 SHP |
| Submarine | Diesel-Electric | 2,000-6,000 SHP (surfaced) |

---

## Cross-References

- [[04-Ship-Customization/Module-System]] - Module mechanics
- [[06-Multiplayer/Save-Reconnection]] - Fuel consumption offline
- [[02-Core-Gameplay/Ship-Physics]] - Movement mechanics
- [[Modules/Auxiliary/_Auxiliary-Overview]] - Generators, fuel systems

---

*Category created: 2025-12-03*
