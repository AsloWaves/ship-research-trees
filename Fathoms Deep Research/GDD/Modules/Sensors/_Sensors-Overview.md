# Sensors Modules Overview
**Category**: Sensors
**Status**: 📋 IN DEVELOPMENT
**Last Updated**: 2025-12-03

---

## Overview

Sensor modules provide detection and awareness capabilities. They determine what enemies you can see, how far away, and how accurately. Sensors are critical for both offensive targeting and defensive awareness.

---

## Sensor Types

### Radar

| Type | Function | Era |
|------|----------|-----|
| Air Search | Detect aircraft at long range | T4+ |
| Surface Search | Detect ships, navigation | T4+ |
| Fire Control | Provide targeting data | T5+ |
| Height Finding | Determine aircraft altitude | T6+ |
| Combined | Multi-function radar | T8+ |

**Radar Stats**:
- Detection Range (km)
- Accuracy (%)
- Update Rate (seconds)
- Power Required (kW)
- Weight (tons)
- Detectability (can enemy detect your radar?)

### Sonar

| Type | Function | Era |
|------|----------|-----|
| Active Sonar | Ping for submarine detection | T4+ |
| Passive Sonar | Listen for engine noise | T3+ |
| Depth Sonar | Determine submarine depth | T5+ |
| Variable Depth | Towed array, better detection | T7+ |

**Sonar Stats**:
- Detection Range (km)
- Depth Range (m)
- Accuracy (bearing/range)
- Active Ping Detectability
- Power Required (kW)

### Hydrophones
Passive listening devices (pre-sonar and supplement).

| Type | Era | Notes |
|------|-----|-------|
| Hull-Mounted | T1+ | Basic listening |
| Towed | T5+ | Reduced self-noise |
| Directional | T4+ | Bearing determination |

### Optics
Visual detection and ranging.

| Type | Function | Era |
|------|----------|-----|
| Binoculars | Basic observation | T1+ |
| Rangefinder | Optical range measurement | T1+ |
| Director | Fire control optics | T2+ |
| Night Vision | Low-light observation | T7+ |

**Optics Stats**:
- Magnification
- Range (effective visual range)
- Accuracy (ranging precision)
- Weather Penalty (reduced in poor visibility)

---

## Detection Mechanics

### Detection Range Formula

```
Effective Range = Base Range × Weather Modifier × Target Size Modifier × Crew Skill
```

### Detection Factors

| Factor | Effect |
|--------|--------|
| Target Size | Larger ships easier to detect |
| Target Speed | Moving ships easier to detect |
| Weather | Rain/fog reduces visual/radar range |
| Sea State | Rough seas affect sonar |
| Emissions | Active radar/radio reveals position |

---

## Technology Progression

### T1-T3 (Pre-Radar)
- Optical rangefinders only
- Basic hydrophones
- Rely on visual lookouts
- Limited night capability

### T4-T5 (Early Radar)
- First air/surface search radars
- Basic sonar systems
- Radar still unreliable
- Visual backup essential

### T6-T7 (WWII Peak)
- Reliable radar systems
- Advanced fire control radar
- Active/passive sonar
- Radar-directed AA

### T8-T9 (Post-War)
- Powerful search radars
- Helicopter-dipping sonar
- Electronic warfare
- Over-the-horizon detection

### T10 (AEGIS)
- Phased array radar
- Integrated sensor fusion
- Automated threat detection
- Satellite links

---

## Module Template

```markdown
# [Sensor Name]
**Type**: [Radar / Sonar / Optics / etc.]
**Nation**: [Origin country]
**Tier**: T[X]

## Specifications
| Stat | Value |
|------|-------|
| Detection Range | X km |
| Accuracy | X% |
| Update Rate | X seconds |
| Power Required | X kW |
| Weight | X tons |

## Detection Capabilities
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | X km | |
| Cruiser | X km | |
| Destroyer | X km | |
| Submarine (surfaced) | X km | |
| Submarine (periscope) | X km | |
| Aircraft | X km | |

## Crew Requirements
| Crew Type | Count | Min Level |
|-----------|-------|-----------|
| Radar Operator | X | X |

## Installation Requirements
- Ship Class: [DD / CL / CA / BB / CV / SS]
- Minimum Tier: TX
- Slot Type: [Hardpoint / Internal]
- Slot Size: [S / M / L]

## Historical Notes
[Brief historical context]
```

---

## Sensors by Nation

### United States
- [[SC-2-Air-Search-Radar]] - Early air search
- [[SG-Surface-Search-Radar]] - Standard surface radar
- [[Mk37-Fire-Control-Radar]] - Main battery FCS
- [[QC-Sonar]] - Standard destroyer sonar
- [More to be added...]

### Great Britain
- [[Type-271-Surface-Radar]] - Centimetric radar
- [[Type-279-Air-Search]] - Early air warning
- [[ASDIC-Type-144]] - Standard sonar
- [More to be added...]

### Japan
- [[Type-21-Air-Search]] - Early Japanese radar
- [[Type-22-Surface-Search]] - Surface radar
- [[Type-93-Hydrophone]] - Passive listening
- [More to be added...]

### Germany
- [[FuMO-21-Radar]] - Early search radar
- [[GHG-Hydrophone]] - Submarine listening
- [[S-Gerät-Sonar]] - Active sonar
- [More to be added...]

---

## Cross-References

- [[04-Ship-Customization/Module-System]] - Module mechanics
- [[04-Ship-Customization/Technology-Integration]] - Radar era requirements
- [[02-Core-Gameplay/AI-NPC-System]] - Detection mechanics
- [[Modules/Fire-Control/_Fire-Control-Overview]] - Targeting systems
- [[03-Combat-Systems/Submarine-Warfare]] - Sonar usage

---

*Category created: 2025-12-03*
