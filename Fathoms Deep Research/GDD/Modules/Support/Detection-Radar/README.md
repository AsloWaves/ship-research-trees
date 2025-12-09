---
title: Radar Detection Systems Index
category: modules
subcategory: detection-radar
description: All radar modules organized by function
last_updated: 2025-12-09
---

# Radar Detection Systems

> Radar revolutionized naval warfare from 1940 onward. This index covers all radar types from early WWII sets to modern phased arrays.

## How Radar Works in Game

See [[_Radar-Mechanics]] for full details on:
- **Coverage types**: Rotating, Sector, Directional, Fixed Array
- **Operation modes**: Auto, Manual, Sector Lock
- **Detection factors**: Range, cone width, rotation speed, resolution

---

## Radar Categories

### Surface Search Radar
Long-range detection of ships. Essential for night combat and beyond-visual-range awareness.

| Module | Nation | Era | Range | Scan Type | Key Feature |
|--------|--------|-----|-------|-----------|-------------|
| [[Radar-Surface-Type271]] | UK | 1941 | 25km | Rotating 8s | First effective shipboard radar |
| [[Radar-Surface-SG]] | USA | 1942 | 35km | Rotating 6s | **Best WWII surface radar** |
| [[Radar-Surface-Type22]] | Japan | 1942 | 28km | Sector 120° | Focused forward arc |
| [[Radar-Surface-FuMO25]] | Germany | 1942 | 20km | Rotating 10s | Mattress antenna |

### Air Search Radar
Long-range detection of aircraft. Critical for carrier task forces and convoy defense.

| Module | Nation | Era | Range | Scan Type | Key Feature |
|--------|--------|-----|-------|-----------|-------------|
| [[Radar-Air-Type79]] | UK | 1940 | 80km | Rotating 10s | First operational naval radar |
| [[Radar-Air-SK]] | USA | 1942 | 120km | Rotating 8s | **Long-range air warning** |
| [[Radar-Air-Type21]] | Japan | 1943 | 60km | Rotating 12s | Late-war improvement |
| [[Radar-Air-FuMO80]] | Germany | 1944 | 70km | Rotating 10s | Berlin radar variant |

### Fire Control Radar
Precision tracking for gunnery. Directional beams provide accuracy for weapons solutions.

| Module | Nation | Era | Range | Beam | Key Feature |
|--------|--------|-----|-------|------|-------------|
| [[Radar-FC-Type284]] | UK | 1941 | 14km | 20° | Surface FC |
| [[Radar-FC-Mk37]] | USA | 1941 | 18km | 25° | **Dual-purpose (surface + AA)** |
| [[Radar-FC-Type94]] | Japan | 1944 | 12km | 30° | Late-war FC |
| [[Radar-FC-FuMO27]] | Germany | 1943 | 15km | 22° | U-boat FC variant |

---

## Radar Progression by Era

### Early War (1940-1941)
- UK leads with Type 79 air search and Type 271 surface
- USA developing SG, deploying limited sets
- Japan/Germany: Limited radar, primarily optical

### Mid War (1942-1943)
- **USA SG radar** becomes standard, decisive in night battles
- UK improves with Type 273 (navigation) and Type 277 (height-finding)
- Japan deploys Type 22, but production limited
- Germany focuses on U-boat radar (FuMO series)

### Late War (1944-1945)
- US radar advantage overwhelming
- Japan/Germany introduce FC radars but too late, too few
- Combined radar systems (search + FC) standard on Allied ships

---

## Coverage Pattern Reference

### Rotating (360°)
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  ← Full rotation
      / | \
     /  |  \
   SW   |   SE
        |
        S
```
- **Surface Search**: Typical pattern
- **Pro**: Sees all directions
- **Con**: Slow updates (4-15 seconds)

### Sector Scan (60-180°)
```
         N
        /|\
       / | \
      /  |  \
     /   |   \
W --+----+----+-- E
    ^         ^
    |---------|
    Sector Arc
```
- **Pro**: Faster updates in chosen direction
- **Con**: Blind spots outside sector

### Directional (15-35°)
```
         N
         |
         |     ← Narrow Beam
     ----+---------> Target
         |
         |
```
- **Fire Control**: Manual aim at specific target
- **Pro**: Continuous tracking, highest accuracy
- **Con**: Only one target, requires cueing

---

## National Characteristics

### United States
- **Best surface radar** (SG at 35km)
- **Best FC radar** (Mk 37 dual-purpose)
- Fast rotation, high reliability
- Excellent production numbers

### United Kingdom
- **First operational radar** (Type 79)
- Good all-around performance
- Pioneered centimetric (10cm) radar
- Critical for winning Battle of Atlantic

### Japan
- **Late adoption** (1942+)
- Sector-scan preference (Type 22)
- Limited production, inconsistent quality
- Relied more on night-fighting optical skills

### Germany
- **U-boat focus** (FuMO series)
- Good individual designs, poor production
- Surface fleet had limited radar
- Advanced concepts but lost technology race

---

## Radar vs Fog of War

| System | Effect on Your View |
|--------|---------------------|
| **No Radar** | Visual range only (~20km clear day, less in poor conditions) |
| **Surface Search** | Contacts appear on minimap out to radar range |
| **Air Search** | Aircraft appear on minimap (requires CIC bridge) |
| **Fire Control** | Enables radar-directed gunnery at tracked target |

---

## Counter-Measures

| Counter | Effect |
|---------|--------|
| **Radar Warning Receiver** | Know when radar is scanning you |
| **Noise Jammer** | Degrades enemy radar range |
| **Chaff** | Creates false contacts |
| **Terrain Masking** | Islands block radar |
| **Weather** | Rain/storms reduce range |

---

## Cross-References

- [[_Radar-Mechanics]] - Full mechanics documentation
- [[../Detection-Sonar/README]] - Sonar systems
- [[../Detection-Visual/README]] - Visual detection
- [[../Electronic-Warfare/README]] - ECM and RWR
- [[../../Bridge/Combat-Information-Center]] - CIC (radar display integration)

---

*Created: 2025-12-09 - Module expansion with cone/sweep variants*
