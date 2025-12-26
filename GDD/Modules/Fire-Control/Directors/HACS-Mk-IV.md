---
module_id: FCS-DIR-003
name: HACS Mk IV
category: fire-control
subcategory: director
type: high-angle-aa
era: 1938
nation: UK
manufacturer: Vickers-Armstrong

# Physical
weight_kg: 5200
height_m: 2.1
crew: 5
armored: true
armor_mm: 12

# Optical
rangefinder_base_m: 4.57
rangefinder_type: coincidence
magnification: 15x
optical_range_km: 12

# Tracking
elevation_range: 0 to +80
train_rate_deg_s: 20
elevation_rate_deg_s: 15
stabilization: 2-axis

tags: [director, high-angle, uk, royal-navy, wwii, aa-defense]
---

# HACS Mk IV (High Angle Control System)

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | HACS Mk IV |
| **Nation** | United Kingdom |
| **Era** | 1938-1950s |
| **Type** | High-Angle (AA Only) |
| **Manufacturer** | Vickers-Armstrong |

## Description

The High Angle Control System (HACS) was the Royal Navy's dedicated anti-aircraft fire control solution. Unlike the American dual-purpose approach, the British separated surface and AA fire control, with HACS handling high-angle engagements exclusively.

**Key Innovation**: Dedicated AA design with tachymetric computing - measuring target rate of change for lead prediction.

## Physical Specifications

| Specification | Value |
|--------------|-------|
| Weight | 5,200 kg (11,500 lbs) |
| Height | 2.1 m (6.9 ft) |
| Crew | 5 |
| Armor | 12mm splinter protection |
| Rangefinder | 4.57m (15 ft) UB-7 |
| Magnification | 15x |

## Optical Performance

| Parameter | Value |
|-----------|-------|
| Rangefinder Base | 4.57m |
| Optical Range (Aircraft) | 12,000m |
| Slant Range Accuracy | ±80m at 8km |
| Bearing Accuracy | ±0.25° |
| Elevation Accuracy | ±0.3° |

## Tracking Performance

| Parameter | Value |
|-----------|-------|
| Elevation Range | 0° to +80° |
| Train Rate | 20°/sec |
| Elevation Rate | 15°/sec |
| Stabilization | 2-axis (roll, pitch) |
| Tracking Type | Tachymetric |

## Tachymetric Principle

HACS used rate-aided tracking:
1. Measure target bearing and elevation
2. Measure RATE of change in both axes
3. Predict future position based on rates
4. Calculate lead angle and fuze time

**Advantage**: Handles crossing targets smoothly
**Disadvantage**: Assumes constant target motion

## HACS vs American Mk 37

| Feature | HACS Mk IV | Mk 37 |
|---------|------------|-------|
| Surface Fire | No | Yes |
| AA Fire | Yes | Yes |
| Max Elevation | +80° | +85° |
| Train Rate | 20°/sec | 30°/sec |
| Stabilization | 2-axis | 3-axis |
| Radar Integration | Type 285 | Mk 4/12/22 |
| Weight | 5.2 tons | 8.2 tons |

HACS was lighter and simpler, but Mk 37 was more capable.

## Integration

The HACS connected to:
- **HACS Table** - Mechanical AA computer
- **Type 285 Radar** (from 1941) - FC radar
- **4.5" Twin Mounts** - Primary AA weapons
- **4" Twin Mounts** - Secondary AA

## Crew Stations

| Station | Role |
|---------|------|
| Director Layer | Elevation tracking |
| Director Trainer | Bearing tracking |
| Range Operator | Rangefinder operation |
| Rate Officer | Rate computation oversight |
| Control Officer | Overall command |

## Combat Record

**Battle of Crete (May 1941)**
HACS-equipped cruisers engaged waves of Luftwaffe aircraft. While losses were heavy, AA fire prevented even higher casualties. HMS Fiji and HMS Gloucester expended enormous quantities of ammunition under HACS direction.

**Arctic Convoys (1942-1943)**
HACS proved effective against level bombers and torpedo aircraft in the harsh conditions. Type 285 radar integration improved low-visibility performance.

**Mediterranean Operations (1942-1943)**
HACS-directed AA fire defended against Italian and German air attacks. The system's reliability in hot, dusty conditions exceeded expectations.

## Variants

| Model | Era | Changes |
|-------|-----|---------|
| HACS Mk I | 1930 | Original, no radar |
| HACS Mk II | 1934 | Improved computer |
| HACS Mk III | 1936 | Better stabilization |
| HACS Mk IV | 1938 | Radar-ready |
| HACS Mk V | 1942 | Full radar integration |

## Limitations

### Surface Engagement
HACS could not engage surface targets effectively:
- Low maximum depression (-5° practical)
- No surface fire control computer
- Separate DCT required for surface work

### Dive Bombers
Steep-diving aircraft challenged the tachymetric system:
- Rate changes during dive
- Prediction becomes inaccurate
- Required manual override

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| AA Accuracy Bonus | +30% | High-angle fire |
| Surface Accuracy | None | Not designed for surface |
| Tracking Speed | Good | 20°/sec |
| Stabilization | Good | 2-axis |
| Radar Integration | Yes | Type 285 |
| Weather Penalty | -25% | With radar |

## Advantages
- Lighter than Mk 37
- Dedicated AA optimization
- Good tracking rates
- Reliable mechanism
- Effective radar integration

## Disadvantages
- AA only (no surface capability)
- Slower than Mk 37
- 2-axis stabilization only
- Tachymetric limitations vs. dive bombers

## Ships Equipped
- All RN cruisers (1-2 directors)
- RN battleships (2-4 directors)
- RN carriers (2-4 directors)
- Large RN destroyers (1 director)

## Cross-References
- [[/GDD/Modules/Support/Detection-Radar/Radar-FC-Type284|Type 284/285 Radar]]
- [[Computers/HACS-Table|HACS Computing Table]]
- [[Directors/DCT-Mk-II|DCT Mk II (Surface Director)]]

---
*HACS represented the British approach to AA fire control - specialized and effective, but requiring separate systems for surface work.*
