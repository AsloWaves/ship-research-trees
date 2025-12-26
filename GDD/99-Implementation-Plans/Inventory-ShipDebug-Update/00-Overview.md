# Inventory & ShipDebugUIManager GDD Standards Update Plan

**Document Version**: 3.0 (Expanded with Full GDD Compliance)
**Created**: 2025-12-10
**Revised**: 2025-12-13
**Status**: Planning Phase - Ready for Implementation
**Scope**: Inventory System, ShipDebugUIManager, Port Integration, Ship Fitting UI

---

## GDD Source Confirmation

**Authoritative Source**: `D:/research/Fathoms Deep Research/GDD/`

**Key Reference Documents**:
| Document | Location | Key Specifications |
|----------|----------|-------------------|
| Tetris-Fitting-Mechanics.md | 04-Ship-Customization/ | THREE grid systems, slot-matching rules, cargo partitions |
| Ship-Fitting-UI.md | 04-Ship-Customization/ | 5 UI screens, layouts, interactions |
| Crew-Module-Mechanics.md | 03-Combat-Systems/ | Efficiency formulas, stat effects |
| Crew-Management.md | 02-Core-Gameplay/ | Crew weight, sailor scaling |
| Inventory-System.md | 02-Core-Gameplay/ | HARD CAP 100%, port storage tiers |
| Module-System.md | 04-Ship-Customization/ | Module categories, slot restrictions |

---

## Critical Corrections from Previous Versions

| Topic | v1.0 (WRONG) | v2.0 (Partial) | v3.0 (COMPLETE) |
|-------|--------------|----------------|-----------------|
| **Equipment Slots** | Tetris-style | Slot-matching | Slot-matching with CATEGORY validation |
| **Weight System** | Soft cap | Hard cap 100% | Hard cap + engine floor 70% |
| **Grid Sizes** | Standardized | Per-ship | Per-ship with partition system |
| **Validation Order** | Dimension only | Dim → Weight | Category → Dimension → Weight → Crew |
| **Efficiency** | Not specified | Formula only | Formula + stat cap (50) + floor |
| **Cargo System** | Basic grid | Tetris | Tetris + partitions + damage |

---

## Executive Summary

This plan outlines comprehensive implementation to bring Inventory and ShipDebugUIManager to full GDD compliance. The implementation is organized into 6 phases plus a pre-phase foundation.

### Key Objectives
1. **Pre-Phase**: Resolve ShipConfigurationSO namespace conflict, establish base structures
2. **Phase 1**: Establish Port as central hub with spawn and fitting restrictions
3. **Phase 2**: Implement slot-matching equipment system (NOT Tetris)
4. **Phase 3**: Implement true Tetris cargo/storage grids with partitions
5. **Phase 4**: Build 5 GDD-compliant Ship Fitting UI screens
6. **Phase 5**: Implement crew assignment with GDD-compliant efficiency formulas
7. **Phase 6**: Add loadout presets, polish ShipDebugUIManager, accessibility

---

## Three Distinct Grid Systems (Core Architecture)

The GDD defines THREE separate grid systems with DIFFERENT mechanics:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ SYSTEM 1: EQUIPMENT SLOTS (Slot-Matching)                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ Purpose: Ship fitting (modules, turrets, engines)                           │
│ Mechanic: Fixed slots with CATEGORY + DIMENSION requirements                │
│ Rule 1: Module CATEGORY must match slot CATEGORY                            │
│ Rule 2: Module DIMENSION must EXACTLY match slot DIMENSION                  │
│ Rule 3: Module WEIGHT + Crew WEIGHT ≤ Slot CAPACITY                         │
│ NOT TETRIS - No freeform placement, no rotation, no collision detection     │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ SYSTEM 2: SHIP CARGO (True Tetris)                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ Purpose: Mission inventory (ammo, fuel, loot, supplies)                     │
│ Mechanic: Freeform placement, rotation (R key), collision detection         │
│ Constraints: DUAL - Grid cells + Weight limit (HARD CAP 100%)               │
│ Partitions: Ammo Magazine, Fuel Bunker, General Cargo, Refrigerated         │
│ Damage: Cargo can be damaged/destroyed by combat, explosion/fire risks      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ SYSTEM 3: PORT/DRYDOCK STORAGE (True Tetris)                                │
├─────────────────────────────────────────────────────────────────────────────┤
│ Purpose: Between-mission storage at ports                                   │
│ Mechanic: Same Tetris mechanics as cargo                                    │
│ Constraints: Grid cells ONLY (no weight limit in storage)                   │
│ Capacity: Tier-based (T1-3: 500, T4-7: 750, T8-10: 1000 cells)              │
│ Separation: Each port has SEPARATE storage, no universal account storage   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Hard Cap Weight System

**CRITICAL GDD RULE**: Ships have a HARD CAP at 100% weight capacity.

```
HARD CAP ENFORCEMENT
====================

At Port (Docked):
├── Cannot add cargo that would exceed 100%
├── Cannot undock if at or above 100%
└── Must offload to meet weight before departure

At Sea (Underway):
├── Cannot pick up cargo that would exceed 100%
├── Cannot loot wrecks if it would exceed 100%
└── NO soft cap penalties - simply blocked

Weight Display Color Bands:
├── Green (0-80%): Optimal operating weight
├── Yellow (80-95%): Near limit, player aware
├── Orange (95-100%): At limit warning
└── Red (100%): HARD CAP - All add operations blocked

Note: This is NOT a penalty system with speed reduction.
Weight penalties from overloading DO NOT EXIST in this design.
The 100% cap is absolute and cannot be exceeded.
```

---

## Phase Structure Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    PRE-PHASE: FOUNDATION                         │
│  Namespace unification, base structures, interfaces, enums      │
│  Estimated: 2-3 days                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 1: PORT INTEGRATION                     │
│  Player spawn → Port, safe zones, fitting restrictions          │
│  Estimated: 3-4 days                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 2: SLOT-MATCHING SYSTEM                 │
│  Equipment slots with category + dimension validation           │
│  Estimated: 4-5 days                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 3: CARGO & STORAGE GRIDS                │
│  True Tetris for cargo with partitions, port storage            │
│  Estimated: 5-6 days                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 4: UI FRAMEWORK                         │
│  5 Ship Fitting screens with full interaction specs             │
│  Estimated: 7-10 days                                           │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 5: CREW & EFFICIENCY                    │
│  Crew assignment, efficiency formulas with caps/floors          │
│  Estimated: 4-5 days                                            │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                    PHASE 6: LOADOUTS & POLISH                    │
│  Preset system, ShipDebugUIManager, accessibility               │
│  Estimated: 5-7 days                                            │
└─────────────────────────────────────────────────────────────────┘

TOTAL ESTIMATED: 30-40 days for full implementation
```

---

## Document Index

| Document | Content |
|----------|---------|
| [01-Pre-Phase-Foundation.md](./01-Pre-Phase-Foundation.md) | ShipConfigurationSO, base structures, interfaces, enums |
| [02-Phase-1-Port-Integration.md](./02-Phase-1-Port-Integration.md) | Port spawn, safe zones, fitting restrictions |
| [03-Phase-2-Slot-Matching.md](./03-Phase-2-Slot-Matching.md) | Equipment slot system with validation |
| [04-Phase-3-Cargo-Storage.md](./04-Phase-3-Cargo-Storage.md) | Tetris cargo grid, port storage, partitions |
| [05-Phase-4-UI-Framework.md](./05-Phase-4-UI-Framework.md) | 5 Ship Fitting screens detailed specs |
| [06-Phase-5-Crew-Efficiency.md](./06-Phase-5-Crew-Efficiency.md) | Crew assignment, efficiency formulas |
| [07-Phase-6-Loadouts-Polish.md](./07-Phase-6-Loadouts-Polish.md) | Loadout presets, ShipDebugUIManager |
| [08-Testing-Requirements.md](./08-Testing-Requirements.md) | Testing requirements by phase |
| [09-File-Manifest.md](./09-File-Manifest.md) | Complete file creation/modification list |

---

## Success Criteria

1. **Three Grid Systems**: Correctly differentiated (slot-matching vs Tetris vs storage)
2. **Hard Cap**: 100% weight cap enforced with zero exceptions
3. **Category Validation**: Equipment slots check category BEFORE dimension
4. **Efficiency Formulas**: Match GDD to ±0.1% precision with cap (50) and floor (70%)
5. **5 UI Screens**: All operational per GDD layout specifications
6. **Performance**: <16ms frame time with full UI open
7. **Port-Only Fitting**: Equipment changes completely blocked at sea
8. **Cargo Partitions**: Ammo/fuel/general properly separated with risk mechanics

---

*Document Version 3.0 - Full GDD Compliance*
*Plan Location: D:/research/Fathoms Deep Research/GDD/99-Implementation-Plans/Inventory-ShipDebug-Update/*
