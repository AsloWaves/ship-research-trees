---
module_id: FCS-DIR-001
name: Mk 37 Gun Director
category: fire-control
subcategory: director
type: dual-purpose
era: 1939
nation: USA
manufacturer: Ford Instrument Company

# Physical
weight_kg: 8165
height_m: 2.4
crew: 6
armored: true
armor_mm: 19

# Optical
rangefinder_base_m: 4.57
rangefinder_type: stereoscopic
magnification: 20x
optical_range_km: 18

# Tracking
elevation_range: -15 to +85
train_rate_deg_s: 30
elevation_rate_deg_s: 18
stabilization: 3-axis

tags: [director, dual-purpose, usa, wwii, mk37, excellent, standard]
---

# Mk 37 Gun Director

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | Mk 37 Mod 0/1/2/3 |
| **Nation** | United States |
| **Era** | 1939-1960s |
| **Type** | Dual-Purpose (Surface & AA) |
| **Manufacturer** | Ford Instrument Company |

## Description

The Mk 37 Gun Director was the most successful naval fire control director of WWII, revolutionizing both surface and anti-aircraft gunnery. Its dual-purpose design allowed a single system to engage surface ships at long range and incoming aircraft with equal effectiveness.

**Key Innovation**: True dual-purpose capability with 3-axis stabilization, allowing tracking of high-speed aircraft while ship pitched and rolled.

## Physical Specifications

| Specification | Value |
|--------------|-------|
| Weight | 8,165 kg (18,000 lbs) |
| Height | 2.4 m (7.9 ft) |
| Crew | 6 (2 trainers, 2 pointers, 1 rangefinder operator, 1 director officer) |
| Armor | 19mm splinter protection |
| Rangefinder | 4.57m (15 ft) stereoscopic |
| Magnification | 20x |

## Optical Performance

| Parameter | Value |
|-----------|-------|
| Rangefinder Base | 4.57m (15 ft) |
| Optical Range (Battleship) | 40,000 yards (36.6 km) |
| Optical Range (Cruiser) | 35,000 yards (32 km) |
| Optical Range (Destroyer) | 28,000 yards (25.6 km) |
| Optical Range (Aircraft) | 15,000 yards (13.7 km) |
| Bearing Accuracy | ±0.1° |
| Range Accuracy | ±50m at 20km |

## Tracking Performance

| Parameter | Value |
|-----------|-------|
| Elevation Range | -15° to +85° |
| Train Rate | 30°/sec |
| Elevation Rate | 18°/sec |
| Stabilization | 3-axis (pitch, roll, yaw) |
| Tracking Type | Continuous |

## Integration

The Mk 37 Director connected to:
- **Mk 37 Computer** - Ballistic calculations
- **Mk 4 Radar** (later Mk 12/22) - Fire control radar
- **5"/38 Mounts** - Primary controlled weapons
- **Mk 37 Stable Element** - Gyroscopic reference

**Data Transmission**: Synchro-servo system providing continuous gun orders to all connected mounts.

## Crew Stations

| Station | Role |
|---------|------|
| Director Officer | Overall control, mode selection |
| Pointer (Elevation) | Tracks target vertically |
| Trainer (Bearing) | Tracks target horizontally |
| Rangefinder Operator | Range measurement |
| Cross-Level Operator | Compensates for ship roll |
| Spotter | Observes fall of shot |

## Operating Modes

### Surface Mode
- Full stereoscopic ranging
- Continuous tracking
- Range rate computation
- Lead angle calculation
- Outputs: bearing, elevation, range to Mk 37 computer

### AA Mode
- High-angle tracking (to +85°)
- Slant range computation
- Lead angle for high crossing rates
- Fuze time calculation (with VT fuze override)
- Altitude output for radar slaving

## Combat Record

**Battle of the Philippine Sea (June 1944)**
Mk 37-equipped ships formed the core of Task Force 58's AA defense. The directors tracked Japanese aircraft from detection to destruction, guiding 5"/38 fire with devastating accuracy.

**Naval Battle of Guadalcanal (November 1942)**
USS Washington used Mk 37-directed secondary battery at night, achieving hits on Japanese destroyers under conditions impossible for optical-only fire control.

**Okinawa Kamikaze Defense (1945)**
Mk 37 directors proved decisive against kamikaze attacks, maintaining track on diving aircraft until the final seconds. Ships like USS Laffey survived multiple hits partly due to Mk 37's continuous tracking capability.

## Variants

| Model | Era | Changes |
|-------|-----|---------|
| Mk 37 Mod 0 | 1939 | Original, no radar |
| Mk 37 Mod 1 | 1941 | Mk 4 radar added |
| Mk 37 Mod 2 | 1943 | Mk 12/22 radar |
| Mk 37 Mod 3 | 1944 | Improved stabilization |

## Game Statistics

| Stat | Value | Notes |
|------|-------|-------|
| Accuracy Bonus | +35% | Surface engagements |
| AA Accuracy Bonus | +40% | With radar |
| Tracking Speed | Excellent | 30°/sec train |
| Stabilization | Full | 3-axis gyro |
| Radar Integration | Yes | Mk 4/12/22 |
| Night Capability | Excellent | With radar |

## Advantages
- True dual-purpose (surface AND AA)
- Best stabilization of WWII
- Excellent radar integration
- High tracking rates for aircraft
- Proven combat reliability
- Standardized across USN fleet

## Disadvantages
- Heavy (8+ tons)
- Complex 6-man crew
- Expensive to manufacture
- Power-hungry systems
- Training requirements high

## Ships Equipped
- All USN destroyers (1 director)
- All USN cruisers (2-4 directors)
- All USN battleships (4-6 directors)
- All USN carriers (4 directors)
- Many Allied ships (Lend-Lease)

## Cross-References
- [[Computers/Mk-37-Computer|Mk 37 Computer]]
- [[Integrated/Mk-37-GFCS|Mk 37 GFCS]]
- [[/GDD/Modules/Support/Detection-Radar/Radar-FC-Mk37|Mk 37 Fire Control Radar]]

---
*The Mk 37 Director represents the pinnacle of WWII fire control technology, setting the standard that all other navies attempted to match.*
