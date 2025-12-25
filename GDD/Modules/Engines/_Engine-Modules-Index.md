---
title: Engine Modules Index
category: modules
slot_type: engine
description: Propulsion systems that determine ship speed, range, and fuel consumption
last_updated: 2025-12-09
tags: [modules, engines, propulsion, progression]
---

# Engine Modules

> Engine Modules determine a ship's speed, acceleration, range, and fuel efficiency. Engine choice fundamentally defines ship character.

## Design Philosophy

Engines evolved dramatically from 1880-present, each generation offering different trade-offs:

| Era | Technology | Character |
|-----|------------|-----------|
| **1880-1920** | Reciprocating Steam | Reliable but slow, coal-hungry |
| **1906-1960** | Steam Turbines | High power, revolutionary speed |
| **1910-Present** | Diesel | Efficient, excellent range |
| **1960-Present** | Gas Turbine | Lightning acceleration, thirsty |
| **1955-Present** | Nuclear | Unlimited range, expensive |

---

## Key Stats

| Stat | Description | Gameplay Impact |
|------|-------------|-----------------|
| **Power Output** | Shaft horsepower (SHP) | Max speed contribution |
| **Efficiency** | Fuel consumption rate | Operating range |
| **Weight** | Mass in tons | Displacement budget |
| **Reliability** | Breakdown resistance | Endurance operations |
| **Noise Level** | Sound signature | Submarine detection |
| **Acceleration** | Time to full power | Tactical agility |

---

## Reciprocating Steam Engines (1880-1920)

*The original warship powerplant. Pistons driven by steam from coal-fired boilers.*

| Module | ID | Power | Ship Class | Era | Key Feature |
|--------|-----|-------|------------|-----|-------------|
| [[Compound-Engine]] | ENG-004 | 3,000 SHP | Early gunboats | 1880-1900 | Very early, inefficient |
| [[Triple-Expansion-Small]] | ENG-001 | 5,000 SHP | Destroyers | 1890-1915 | Standard small ship |
| [[Triple-Expansion-Medium]] | ENG-002 | 15,000 SHP | Cruisers | 1890-1915 | Pre-dreadnought era |
| [[Triple-Expansion-Large]] | ENG-003 | 25,000 SHP | Battleships | 1890-1910 | Maximum reciprocating |

**Characteristics:**
- Coal-fired (requires coaling stations)
- Slow acceleration (5+ minutes to full power)
- Reliable but bulky
- Limited top speed (~18-20 knots for capital ships)

---

## Steam Turbines (1906-1960)

*Revolutionary technology that enabled the Dreadnought era. Spinning turbines replaced reciprocating motion.*

| Module | ID | Power | Ship Class | Era | Key Feature |
|--------|-----|-------|------------|-----|-------------|
| [[Parsons-Turbine]] | ENG-005 | 30,000 SHP | Light cruisers | 1906-1940 | Original turbine design (UK) |
| [[Curtis-Turbine]] | ENG-006 | 35,000 SHP | Destroyers | 1910-1940 | Impulse design (USA) |
| [[Geared-Turbine-Light]] | ENG-007 | 30,000 SHP | Destroyers | 1915-1960 | Fast, efficient |
| [[Geared-Turbine-Heavy]] | ENG-008 | 150,000 SHP | Battleships | 1920-1960 | WWII capital ships |
| [[Turbo-Electric]] | ENG-009 | 60,000 SHP | Battleships | 1915-1945 | USA specialty, excellent handling |

**Characteristics:**
- Oil-fired (cleaner, denser fuel)
- High power-to-weight ratio
- Enabled 30+ knot speeds
- Gearing improved efficiency dramatically

`★ Insight ─────────────────────────────────────`
**Turbo-Electric Drive** was uniquely American - converting turbine power to electricity, then back to shaft power. This seems inefficient but provided unmatched maneuverability. USS Lexington could reverse from full ahead to full astern faster than any turbine ship.
`─────────────────────────────────────────────────`

---

## Diesel Engines (1910-Present)

*Internal combustion engines burning diesel fuel. Dominant for submarines and smaller vessels.*

| Module | ID | Power | Ship Class | Era | Key Feature |
|--------|-----|-------|------------|-----|-------------|
| [[Diesel-Direct]] | ENG-010 | 8,000 SHP | Small craft | 1910+ | Simple, reliable |
| [[Diesel-Electric-Submarine]] | ENG-011 | 5,000 SHP | Submarines | 1920+ | Standard sub propulsion |
| [[MAN-Diesel]] | ENG-012 | 6,000 SHP | U-boats | 1935+ | German excellence |

**Characteristics:**
- Excellent fuel efficiency (2-3x turbines)
- Can run on surface, battery underwater (subs)
- Lower power than turbines
- **Silent running** capability (electric mode)

---

## Modern Propulsion (1950-Present)

*Post-war innovations including gas turbines, combined systems, and nuclear power.*

| Module | ID | Power | Ship Class | Era | Key Feature |
|--------|-----|-------|------------|-----|-------------|
| [[Gas-Turbine]] | ENG-013 | 25,000 SHP | Frigates | 1960+ | Jet engine derivative |
| [[CODAG]] | ENG-014 | Variable | Frigates | 1970+ | Diesel + gas combined |
| [[COGAG]] | ENG-015 | 80,000 SHP | Destroyers | 1980+ | Gas + gas, high performance |
| [[Nuclear-Submarine]] | ENG-016 | 35,000 SHP | SSN/SSBN | 1955+ | S5W type reactor |
| [[Nuclear-Carrier]] | ENG-017 | 280,000 SHP | Carriers | 1960+ | A4W type reactor |

**Characteristics:**
- **Gas Turbine**: Instant power, high fuel consumption
- **Combined Systems**: Best of both worlds
- **Nuclear**: Unlimited range, no fuel logistics

`★ Insight ─────────────────────────────────────`
**CODAG (Combined Diesel and Gas)** runs on efficient diesels for cruising, then lights off gas turbines for combat speed. This gives frigates 15 knots on diesel (quiet, efficient) or 30+ knots on turbines (sprint capability).
`─────────────────────────────────────────────────`

---

## Power vs Ship Type

| Ship Type | Typical Power | Typical Speed |
|-----------|---------------|---------------|
| Patrol Boat | 2,000-5,000 SHP | 25-40 kts |
| Destroyer | 30,000-60,000 SHP | 30-35 kts |
| Cruiser | 60,000-120,000 SHP | 30-33 kts |
| Battleship | 100,000-200,000 SHP | 27-30 kts |
| Carrier | 150,000-280,000 SHP | 30-33 kts |
| Submarine | 3,000-35,000 SHP | 15-25 kts (submerged) |

---

## Fuel Types & Logistics

| Fuel | Era | Range Factor | Logistics |
|------|-----|--------------|-----------|
| **Coal** | 1850-1920 | 1.0x | Coaling stations, dirty |
| **Oil** | 1910-Present | 1.5x | Standard, cleaner |
| **Diesel** | 1910-Present | 2.0x | Most efficient |
| **Nuclear** | 1955-Present | ∞ | 20+ year cores |

---

## Slot Rules

- Ships have **1-4 Engine Slots** depending on size
- Multiple engines **combine** power output
- Mixed engine types allowed (CODAG/COGAG concept)
- Engine era should generally match hull era
- Engine weight affects displacement budget

---

## Special Capabilities

| Capability | Engines | Effect |
|------------|---------|--------|
| **Silent Running** | Diesel-Electric | Submarines can run on battery, very quiet |
| **Instant Reverse** | Turbo-Electric | Exceptional ship handling |
| **Boost Mode** | Gas Turbine | Short-term overpower for sprints |
| **Unlimited Range** | Nuclear | No fuel logistics required |

---

## Historical National Preferences

| Nation | Preference | Notable |
|--------|------------|---------|
| **USA** | Turbo-Electric (early), Gas Turbine (modern) | Lexington class, Arleigh Burke |
| **UK** | Geared Turbines | Pioneered with Dreadnought |
| **Germany** | Diesel excellence | U-boat MAN diesels |
| **Japan** | High-pressure turbines | Shimakaze (40 knots!) |

---

## Related Systems

- [[../Bridge/_Bridge-Modules-Index|Bridge Modules]] - Command integration
- [[../Support/_Support-Modules-Index|Support Modules]] - Power consumers
- [[../../04-Ship-Customization/Ship-Database/_Complete-Ships-Index|Ships Index]] - Ship specifications

---

*Updated: 2025-12-09 - Expanded with national variants and historical context*
