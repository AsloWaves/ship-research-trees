# Fire Control Modules Overview
**Category**: Fire Control
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Fire control modules manage targeting, aiming, and accuracy for weapon systems. They link sensors to weapons, compute firing solutions, and direct gunfire. Better fire control = higher hit rates.

---

## Fire Control Types

### Main Battery FCS
Controls main guns on surface ships.

| Component | Function |
|-----------|----------|
| Director | Optical/radar targeting |
| Computer | Ballistic calculations |
| Transmitter | Sends data to turrets |

**FCS Stats**:
- Accuracy Bonus (%)
- Maximum Range (km)
- Target Tracking (how many targets)
- Radar Integration (T4+)
- Rate of Solution (seconds to first accurate shot)

### AA Directors
Anti-aircraft fire control.

| Type | Era | Targets |
|------|-----|---------|
| Optical | T1+ | Manual tracking |
| Radar-Directed | T5+ | Automatic tracking |
| CIWS | T9+ | Automated close-in |

### Torpedo Directors
Torpedo aiming systems.

| Type | Function |
|------|----------|
| Surface TDC | Calculates torpedo lead |
| Submarine TDC | Periscope-integrated targeting |
| Automated | T8+, computer-assisted |

---

## Accuracy Mechanics

### Base Accuracy Formula

```
Hit Chance = Base Accuracy
           × FCS Bonus
           × Crew Skill
           × Range Modifier
           × Weather Modifier
           × Target Speed Modifier
```

### Accuracy Factors

| Factor | Effect |
|--------|--------|
| Range | Accuracy decreases with distance |
| Target Speed | Faster targets harder to hit |
| Own Speed | High speed reduces accuracy |
| Weather | Poor visibility reduces accuracy |
| Target Size | Larger targets easier to hit |
| Crew Skill | Trained crews more accurate |

---

## Technology Progression

### T1-T3 (Pre-Radar)
- Optical rangefinders
- Mechanical computers
- Manual lead calculation
- Limited range effectiveness

### T4-T5 (Early Radar)
- Radar-assisted ranging
- Improved fire control computers
- Better night accuracy

### T6-T7 (WWII Peak)
- Full radar fire control
- VT fuzes for AA
- Automatic tracking
- High accuracy at range

### T8-T9 (Post-War)
- Digital computers
- Automated systems
- Missile guidance
- Multi-target tracking

### T10 (AEGIS)
- Phased array integration
- Fully automated
- Simultaneous engagement
- Near-perfect accuracy

---

## Module Template

```markdown
# [Fire Control System Name]
**Type**: [Main Battery FCS / AA Director / Torpedo Director]
**Nation**: [Origin country]
**Tier**: T[X]

## Specifications
| Stat | Value |
|------|-------|
| Accuracy Bonus | +X% |
| Maximum Range | X km |
| Solution Time | X seconds |
| Targets Tracked | X |
| Radar Integration | [Yes/No] |

## Compatibility
| Weapon Type | Compatible |
|-------------|------------|
| Main Guns | [Yes/No] |
| Secondary Guns | [Yes/No] |
| AA Guns | [Yes/No] |
| Torpedoes | [Yes/No] |

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Fire Control Officer | X | X |
| Plotter | X | X |

## Installation Requirements
- Ship Class: [DD / CL / CA / BB / CV]
- Minimum Tier: TX
- Slot Type: Internal
- Slot Size: [M / L]

## Historical Notes
[Brief historical context]
```

---

## Fire Control by Nation

### United States
- [[Mk37-Director]] - Standard destroyer/cruiser FCS
- [[Mk38-Director]] - Battleship main battery
- [[Mk51-Director]] - Light AA director
- [[Mk56-Director]] - Post-war dual-purpose
- [More to be added...]

### Great Britain
- [[HACS-Mk-IV]] - High Angle Control System
- [[DCT-Mk-III]] - Director Control Tower
- [More to be added...]

### Japan
- [[Type-94-Director]] - Standard IJN FCS
- [[Type-98-Director]] - AA director
- [More to be added...]

### Germany
- [[Basisgerät]] - Rangefinder system
- [[Zieloptik-FCS]] - Fire control optics
- [More to be added...]

---

## Cross-References

- [[Modules/Weapons/_Weapons-Overview]] - Weapon systems
- [[Modules/Sensors/_Sensors-Overview]] - Detection/radar
- [[03-Combat-Systems/Surface-Combat]] - Combat mechanics
- [[04-Ship-Customization/Module-System]] - Module mechanics

---

*Category created: 2025-12-03*
