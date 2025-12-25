# Weapons Modules Overview
**Category**: Weapons
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Weapon modules are the primary means of dealing damage to enemy ships. They include main guns, secondary batteries, anti-aircraft systems, torpedoes, depth charges, and missiles.

---

## Weapon Types

### Main Guns
Primary armament for surface combat.

| Caliber Range | Ship Types | Role |
|---------------|------------|------|
| 5" - 6" | DD, CL | Rapid fire, destroyer killer |
| 6" - 8" | CL, CA | Cruiser combat |
| 12" - 16" | BB, BC | Capital ship combat |
| 16" - 18" | BB | Heavy battleship |

**Key Stats**:
- Caliber (inches)
- Barrel Length (calibers)
- Rate of Fire (RPM)
- Range (km)
- Shell Weight (kg)
- Turret Weight (tons)
- Crew Required

### Secondary Guns
Anti-surface and dual-purpose weapons.

| Type | Role |
|------|------|
| Casemate Guns | Fixed broadside weapons |
| Dual-Purpose | Surface + AA capability |
| Secondary Turrets | Enclosed secondaries |

### Anti-Aircraft Guns
Defense against aircraft.

| Type | Caliber | Role |
|------|---------|------|
| Heavy AA | 3" - 5" | Long-range AA |
| Medium AA | 37mm - 40mm | Medium-range AA |
| Light AA | 20mm - 25mm | Close-in defense |

### Torpedoes
High-damage ship killers.

| Type | Platform | Notes |
|------|----------|-------|
| Surface Tubes | DD, CL, CA | Deck-mounted launchers |
| Submarine Tubes | SS | Bow and stern tubes |
| Fixed Tubes | PT, DD | Non-reloadable |

**Key Stats**:
- Torpedo Caliber (mm)
- Tubes per Mount
- Reload Time
- Torpedo Range (km)
- Torpedo Speed (knots)
- Warhead Size (kg)

### Depth Charges
Anti-submarine weapons.

| Type | Delivery |
|------|----------|
| Stern Racks | Roll-off deployment |
| K-Guns | Side-throwing projectors |
| Hedgehog | Forward-throwing mortar |
| Squid | Advanced ASW mortar |

### Missiles (T8+)
Guided weapons for late-era ships.

| Type | Target |
|------|--------|
| Anti-Ship | Surface targets |
| SAM | Aircraft |
| ASROC | Submarines |
| Cruise | Land/ship targets |

---

## Module Template

Each weapon module file should include:

```markdown
# [Weapon Name]
**Type**: [Main Gun / Secondary / AA / Torpedo / etc.]
**Nation**: [Origin country]
**Tier**: T[X]
**Era**: [Pre-Radar / Early Radar / WWII Peak / Post-War / AEGIS]

## Specifications
| Stat | Value |
|------|-------|
| Caliber | X" |
| Barrel Length | X calibers |
| Rate of Fire | X RPM |
| Range | X km |
| Shell Weight | X kg |
| Muzzle Velocity | X m/s |

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Gunner | X | X |
| Loader | X | X |

## Module Stats
| Stat | Value |
|------|-------|
| Weight | X tons |
| Slot Type | [Hardpoint / Internal] |
| Slot Size | [S / M / L / XL] |

## Installation Requirements
- Ship Class: [DD / CL / CA / BB / CV]
- Minimum Tier: TX
- Technology: [Era requirement]

## Historical Notes
[Brief historical context]

## Ships Using This Weapon
- [[Ships/Nation/ShipName]]
```

---

## Weapons by Nation

### United States
- [[5in-38-cal-Mk12]] - Standard destroyer/cruiser gun
- [[5in-54-cal-Mk42]] - Post-war dual purpose
- [[6in-47-cal-Mk16]] - Cleveland-class cruisers
- [[8in-55-cal-Mk15]] - Heavy cruiser main battery
- [[16in-50-cal-Mk7]] - Iowa-class battleships
- [More to be added...]

### Great Britain
- [[4.7in-45-cal-QF-MkXII]] - Destroyer main gun
- [[6in-50-cal-BL-MkXXIII]] - Light cruiser
- [[8in-50-cal-BL-MkVIII]] - County-class cruisers
- [[14in-45-cal-BL-MkVII]] - King George V class
- [[15in-42-cal-BL-MkI]] - Queen Elizabeth class
- [More to be added...]

### Japan
- [[5in-40-cal-Type89]] - Standard destroyer gun
- [[6.1in-60-cal-Type3]] - Mogami light cruiser
- [[8in-50-cal-Type2]] - Heavy cruiser
- [[14in-45-cal-Type41]] - Kongo class
- [[18.1in-45-cal-Type94]] - Yamato class
- [More to be added...]

### Germany
- [[5.9in-55-cal-SK-C28]] - Light cruiser
- [[8in-60-cal-SK-C34]] - Admiral Hipper class
- [[11in-52-cal-SK-C34]] - Deutschland class
- [[15in-52-cal-SK-C34]] - Bismarck class
- [More to be added...]

---

## Weapons by Tier

### T1-T3 (Pre-Radar)
- Basic optical fire control
- Slower rate of fire
- Shorter effective range

### T4-T5 (Early Radar)
- Radar-assisted ranging
- Improved accuracy

### T6-T7 (WWII Peak)
- Advanced fire control
- VT fuzes for AA
- High rate of fire

### T8-T9 (Post-War)
- Automated loading
- Missile systems
- Advanced targeting

### T10 (AEGIS)
- Fully automated
- Integrated combat systems
- Precision guided weapons

---

## Cross-References

- [[04-Ship-Customization/Module-System]] - Module mechanics
- [[03-Combat-Systems/Surface-Combat]] - Gun combat
- [[03-Combat-Systems/Carrier-Operations]] - AA defense
- [[03-Combat-Systems/Submarine-Warfare]] - ASW weapons
- [[Modules/Fire-Control/_Fire-Control-Overview]] - Targeting systems

---

*Category created: 2025-12-03*
