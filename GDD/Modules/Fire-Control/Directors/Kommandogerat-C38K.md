---
module_id: FCS-DIR-004
name: Kommandogerät C/38K
category: fire-control
subcategory: director
type: main-battery
era: 1938
nation: Germany
manufacturer: Zeiss/Rheinmetall

# Physical
weight_kg: 9500
height_m: 2.8
crew: 8
armored: true
armor_mm: 30

# Optical
rangefinder_base_m: 10.5
rangefinder_type: stereoscopic
magnification: 23x
optical_range_km: 35

# Tracking
elevation_range: -10 to +40
train_rate_deg_s: 6
elevation_rate_deg_s: 4
stabilization: 2-axis

tags: [director, main-battery, germany, kriegsmarine, wwii, stereoscopic, bismarck]
---

# Kommandogerät C/38K

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Kommandogerät C/38K |
| **Nation** | Germany |
| **Era** | 1938-1945 |
| **Type** | Main Battery (Surface) |
| **Manufacturer** | Carl Zeiss Jena / Rheinmetall |

## Description

The Kommandogerät (Command Device) C/38K was the Kriegsmarine's primary main battery fire control director, featuring German excellence in optical engineering. Its stereoscopic rangefinder required exceptional crew training but achieved remarkable accuracy in skilled hands.

**Key Innovation**: Stereoscopic rangefinding - using binocular depth perception rather than coincidence matching for faster, more intuitive ranging.

## Physical Specifications

| Specification | Value |
|--------------|-------|
| Weight | 9,500 kg (20,900 lbs) |
| Height | 2.8 m (9.2 ft) |
| Crew | 8 |
| Armor | 30mm Krupp cemented |
| Rangefinder | 10.5m stereoscopic |
| Magnification | 23x |

## Stereoscopic Rangefinding

Unlike coincidence rangefinders (matching images), stereoscopic systems use natural depth perception:

**How It Works**:
1. Operator views through binocular eyepieces
2. Left/right optical paths separated by 10.5m base
3. Target appears to "float" in 3D space
4. Operator adjusts until target sits at calibration mark
5. Dial reads range directly

**Advantages**:
- Faster than coincidence (3-5 seconds vs 8-10)
- More intuitive operation
- Works better in poor contrast
- Less fatigue on operators

**Disadvantages**:
- Requires exceptional operator training
- Individual ability varies greatly
- Night use more difficult
- Must recalibrate for each operator

## Optical Performance

| Parameter | Value |
|-----------|-------|
| Rangefinder Base | 10.5m |
| Optical Range (Battleship) | 35,000m |
| Optical Range (Cruiser) | 30,000m |
| Optical Range (Destroyer) | 24,000m |
| Bearing Accuracy | ±0.1° |
| Range Accuracy | ±40m at 25km (trained operator) |

## Tracking Performance

| Parameter | Value |
|-----------|-------|
| Elevation Range | -10° to +40° |
| Train Rate | 6°/sec |
| Elevation Rate | 4°/sec |
| Stabilization | 2-axis gyro |
| Tracking Type | Manual follow |

## Integration

The Kommandogerät connected to:
- **Basisgerät C/38K** - Mechanical fire control computer
- **FuMO 27 Radar** (from 1941) - Surface search radar (limited FC use)
- **Main Battery** - 38cm or 28cm turrets
- **Artillery Officer Station** - Command interface

## Crew Stations

| Station | Role |
|---------|------|
| Artillerie-Offizier | Director command |
| Entfernungsmessmann 1 | Primary rangefinder operator |
| Entfernungsmessmann 2 | Backup rangefinder |
| Richtschütze (Seite) | Bearing tracker |
| Richtschütze (Höhe) | Elevation tracker |
| Rechner | Manual computation |
| Beobachter (2) | Spotters |

## Combat Record

**Battle of the Denmark Strait (May 1941)**
Bismarck's Kommandogerät achieved ranging on Hood at 26,500m. The system tracked both Hood and Prince of Wales simultaneously (with secondary director). Famous hit on Hood came at approximately 15km.

**Channel Dash (February 1942)**
Scharnhorst and Gneisenau used their directors to engage RAF bombers and motor torpedo boats during the breakout. The optical systems struggled in poor visibility but FuMO radars provided backup.

**Battle of the North Cape (December 1943)**
Scharnhorst's optical fire control was rendered useless by Arctic darkness. This battle demonstrated the fatal German weakness in radar fire control integration.

## German Optical Philosophy

The Kriegsmarine believed:
1. **Optics are primary** - Radar is backup only
2. **Operator skill matters** - Train intensively
3. **Quality over quantity** - Fewer, better systems
4. **Stereoscopic superiority** - Faster ranging

This philosophy failed when:
- Bad weather negated optical advantage
- Night fighting favored radar
- Well-trained operators were killed and couldn't be replaced

## Radar Integration Failure

Unlike USN/RN integration, German radar-FC integration was poor:

| Issue | Consequence |
|-------|-------------|
| FuMO radars surface-search only | No radar-directed fire control |
| Separate radar/optical crews | Information transfer delays |
| Optical bias in training | Radar underutilized |
| Late FC radar development | FuMO 213 came too late |

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| Accuracy Bonus | +40% | Daylight surface |
| Trained Crew Bonus | +10% | Stereoscopic skill |
| Night Penalty | -50% | No radar FC |
| Weather Penalty | -45% | Optical dependence |
| Tracking Speed | Moderate | 6°/sec |
| AA Capability | Limited | Low elevation |

## Advantages
- Excellent optical quality (Zeiss)
- Fast stereoscopic ranging
- Heavy armor protection
- Good stabilization
- Superb daylight accuracy

## Disadvantages
- Poor radar integration
- Operator training intensive
- Useless at night without radar
- Slow tracking rates
- Surface targets only

## Ships Equipped
- Bismarck (3 directors)
- Tirpitz (3 directors)
- Scharnhorst (3 directors)
- Gneisenau (3 directors)
- Admiral Hipper-class (2 directors)
- Deutschland-class (2 directors)

## Cross-References
- [[Computers/Basisgerat-C38K|Basisgerät C/38K Computer]]
- [[/GDD/Modules/Support/Detection-Radar/Radar-Surface-FuMO25|FuMO 25/27 Radar]]
- [[Directors/SL-8-Director|SL-8 AA Director]]

---
*The Kommandogerät exemplified German optical excellence - superb in daylight, fatally limited in the radar-dominated battles of the late war.*
