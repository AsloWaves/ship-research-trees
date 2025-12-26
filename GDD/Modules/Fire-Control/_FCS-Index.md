---
title: Fire Control Systems Index
category: modules
subcategory: fire-control
description: Optical directors, mechanical computers, and integrated fire control systems
last_updated: 2025-12-25
tags: [fcs, fire-control, directors, computers, gunnery]
---

# Fire Control Systems

> Fire Control Systems (FCS) are the brains of naval gunnery - the optical, mechanical, and electronic systems that calculate firing solutions and direct guns onto target. From simple optical rangefinders to complex analog computers, FCS technology determined which navy could hit targets at longer range with greater accuracy.

## System Categories

### Directors
Optical aiming devices that track targets and measure range/bearing. The "eyes" of fire control.

| Director | Nation | Era | Purpose | Link |
|----------|--------|-----|---------|------|
| Mk 37 Director | USA | 1939+ | Dual-purpose (surface/AA) | [[Directors/Mk-37-Director]] |
| Mk 38 Director | USA | 1941+ | Main battery (battleships) | [[Directors/Mk-38-Director]] |
| Type 94 Director | Japan | 1939+ | Main battery (Yamato) | [[Directors/Type-94-Director]] |
| Type 89 Director | Japan | 1932+ | High-angle AA | [[Directors/Type-89-Director]] |
| HACS Mk IV | UK | 1938+ | High-angle AA | [[Directors/HACS-Mk-IV]] |
| DCT Mk II | UK | 1935+ | Main battery | [[Directors/DCT-Mk-II]] |
| Kommandogerät C/38K | Germany | 1938+ | Main battery | [[Directors/Kommandogerat-C38K]] |
| SL-8 Director | Germany | 1940+ | AA fire control | [[Directors/SL-8-Director]] |

### Computers
Mechanical and analog devices that calculate ballistic solutions. The "brains" of fire control.

| Computer | Nation | Era | Purpose | Link |
|----------|--------|-----|---------|------|
| Ford Mk 1 Range Keeper | USA | 1930+ | Battleship fire control | [[Computers/Ford-Mk-1-Rangekeeper]] |
| Mk 37 Computer | USA | 1939+ | Dual-purpose ballistics | [[Computers/Mk-37-Computer]] |
| Dreyer Table Mk V | UK | 1918+ | Dreadnought fire control | [[Computers/Dreyer-Table-Mk-V]] |
| Admiralty FCT Mk X | UK | 1936+ | Treaty battleship standard | [[Computers/Admiralty-FCT-Mk-X]] |
| Type 92 Shagekiban | Japan | 1932+ | Main battery computer | [[Computers/Type-92-Shagekiban]] |
| Type 94 Computer | Japan | 1939+ | Yamato main battery | [[Computers/Type-94-Computer]] |
| Basisgerät C/38K | Germany | 1938+ | Surface fire control | [[Computers/Basisgerat-C38K]] |

### Integrated Systems
Complete fire control systems combining directors, computers, and data transmission.

| System | Nation | Era | Application | Link |
|--------|--------|-----|-------------|------|
| Mk 37 GFCS | USA | 1939+ | Dual-purpose standard | [[Integrated/Mk-37-GFCS]] |
| Mk 38 GFCS | USA | 1941+ | Battleship main battery | [[Integrated/Mk-38-GFCS]] |
| Type 98 FCS | Japan | 1938+ | Cruiser main battery | [[Integrated/Type-98-FCS]] |
| AFCT System | UK | 1936+ | Battleship standard | [[Integrated/AFCT-System]] |

### Paper Designs
Systems that were designed but never built, or prototypes that never entered service.

| Design | Nation | Era | Notes | Link |
|--------|--------|-----|-------|------|
| Zielgerät 48 | Germany | 1945 | Advanced analog computer | [[Paper-Designs/Zielgerat-48]] |
| Type 5 FCS | Japan | 1945 | Radar-integrated prototype | [[Paper-Designs/Type-5-FCS]] |
| Mk 57 GFCS | USA | 1945 | Guided missile FC | [[Paper-Designs/Mk-57-GFCS]] |
| STAAG Mk II | UK | 1945 | Automated AA mount | [[Paper-Designs/STAAG-Mk-II]] |

---

## Fire Control Principles

### The Fire Control Problem
To hit a moving target from a moving ship requires solving:
1. **Own ship motion** - Speed, heading, roll, pitch
2. **Target motion** - Speed, heading, range rate
3. **Ballistics** - Shell velocity, drag, drop, wind
4. **Time of flight** - Where target will BE when shell arrives

### Key Measurements
| Input | Source | Accuracy |
|-------|--------|----------|
| Range | Rangefinder/Radar | ±50-200m |
| Bearing | Director | ±0.1-0.5° |
| Target angle | Estimator | ±5-10° |
| Own course/speed | Gyrocompass/pitlog | ±1° / ±0.5kn |

### Output: Firing Solution
The FCS outputs gun orders:
- **Bearing** - Where to point horizontally
- **Elevation** - How high to elevate
- **Fuze setting** - For AA shells

---

## National Characteristics

### United States
**Philosophy**: Systematic, integrated, mass-produced

- **Strengths**: Best radar integration, excellent dual-purpose systems, standardized across fleet
- **Signature System**: Mk 37 GFCS - the most effective dual-purpose system of WWII
- **Innovation**: First effective radar fire control, VT proximity fuzes

### United Kingdom
**Philosophy**: Evolved from WWI experience, separate surface/AA systems

- **Strengths**: Excellent rangefinders, proven in combat, good radar integration
- **Signature System**: HACS for AA, Admiralty FCT for surface
- **Innovation**: Dreyer Table pioneered mechanical fire control

### Japan
**Philosophy**: Optical excellence, massive rangefinders, night fighting focus

- **Strengths**: Best optical rangefinders (15m base!), superb night fire control
- **Signature System**: Type 94 (Yamato), Type 98 (cruisers)
- **Weakness**: Lagged in radar integration

### Germany
**Philosophy**: Precision engineering, stereoscopic optics

- **Strengths**: Excellent optical quality, good mechanical computers
- **Signature System**: Kommandogerät with Basisgerät computer
- **Innovation**: Stereoscopic rangefinders, Rhine-Metall computing

---

## Era Progression

| Era | Technology | Accuracy | Range |
|-----|------------|----------|-------|
| 1890-1905 | Visual aiming | ~5% at 3km | 3-5km |
| 1906-1918 | Rangefinders + basic calculators | ~3% at 10km | 10-15km |
| 1918-1935 | Mechanical computers | ~2% at 15km | 15-25km |
| 1935-1945 | Integrated systems + radar | ~1-2% at 20km | 20-35km |
| 1945-1960 | Radar-only fire control | <1% at 30km | 30-40km |

---

## Cross-References

- [[Support/Detection-Radar/Radar-FC-Mk37|Mk 37 Fire Control Radar]]
- [[Support/Detection-Radar/Radar-FC-Type94|Type 94 Fire Control Radar]]
- [[Support/Detection-Radar/Radar-FC-Type284|Type 284 Fire Control Radar]]
- [[06-Weapons/Naval-Weapons/Naval-Guns/_Complete-Guns-Index|Complete Guns Index]]

---

*Created: 2025-12-25 - Initial FCS documentation*
