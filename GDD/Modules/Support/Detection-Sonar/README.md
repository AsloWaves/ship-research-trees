# Detection-Sonar Module Variants

Comprehensive sonar module system with cone/sweep mechanics for Fathoms Deep.

## Overview

This directory contains 14 sonar variants spanning 1915-1970+, from basic WWI hydrophones to advanced Cold War omnidirectional systems and towed arrays.

## File Index

### Core Mechanics
- **_Sonar-Mechanics.md** - Complete sonar detection mechanics documentation

### Legacy Files (Moved)
- **Hydrophone.md** - Original hydrophone module (moved from parent)
- **Active-Sonar.md** - Original active sonar module (moved from parent)

---

## Passive Sonar / Hydrophones (SON-001 to SON-004)

**Characteristics**: Bearing-only detection, completely stealthy, no active pinging

| Module ID | File | Nation | Era | Range | Notes |
|-----------|------|--------|-----|-------|-------|
| SON-001 | Hydrophone-Basic.md | Universal | 1915+ | 3km | Basic omnidirectional, WWI-era |
| SON-002 | Hydrophone-GHG.md | Germany | 1935+ | 5km | Superior 24-element array, U-boat standard |
| SON-003 | Hydrophone-JP.md | USA | 1940+ | 4km | 16-element submarine array |
| SON-004 | Hydrophone-Type93.md | Japan | 1940+ | 3.5km | Basic 12-element, limited capability |

**Gameplay**: All passive sonars provide bearing-only information. Must triangulate with movement or multiple ships to determine range. Target never knows you're listening.

---

## Active Sonar - Searchlight Pattern (SON-005 to SON-007)

**Characteristics**: Narrow beam, manual aim required, bearing AND range

| Module ID | File | Nation | Era | Range | Beam | Notes |
|-----------|------|--------|-----|-------|------|-------|
| SON-005 | ASDIC-Type123.md | UK | 1935+ | 1.5km | 20° | Early ASDIC, manual aim |
| SON-006 | Sonar-QC.md | USA | 1940+ | 2.5km | 25° | Improved range, wider beam |
| SON-007 | ASDIC-Type127.md | UK | 1942+ | 2km | 15° | Depth-finding capability |

**Gameplay**: Operator must manually aim narrow beam and search sectors. Easy to miss contacts outside beam. Alerts target when pinging. Best for final attack approach.

---

## Active Sonar - Scanning Pattern (SON-008 to SON-011)

**Characteristics**: Automatic sweep, forward arc coverage, bearing AND range

| Module ID | File | Nation | Era | Range | Arc | Sweep Time | Notes |
|-----------|------|--------|-----|-------|-----|------------|-------|
| SON-008 | ASDIC-Type144.md | UK | 1940+ | 3km | 150° | 5 sec | WWII standard, automatic |
| SON-009 | ASDIC-Type147.md | UK | 1943+ | 4km | 160° | 4 sec | Hedgehog/Squid compatible |
| SON-010 | Sonar-QGB.md | USA | 1943+ | 4km | 180° | 4.5 sec | Full forward hemisphere |
| SON-011 | Sonar-Type3.md | Japan | 1942+ | 2.5km | 120° | 6 sec | Limited arc, slower |

**Gameplay**: Automatic sweeping eliminates manual aiming. Forward arc only - no rear coverage. Contacts updated each sweep. Alerts target when pinging.

---

## Modern Sonar (SON-012 to SON-014)

**Characteristics**: Advanced electronics, long range, sophisticated processing

| Module ID | File | Nation | Era | Range | Coverage | Notes |
|-----------|------|--------|-----|-------|----------|-------|
| SON-012 | Sonar-SQS4.md | USA | 1955+ | 8km active / 12km passive | 240° scanning | Early Cold War, 3-sec sweep |
| SON-013 | Sonar-SQS26.md | USA | 1960+ | 15km active / 20km passive | 360° omni | True omnidirectional, bow dome |
| SON-014 | Sonar-Towed-Array.md | USA | 1970+ | 30km passive only | 360° passive | Extreme range, passive only |

**Gameplay**: Cold War systems offer dramatic range and coverage improvements. SQS-26 has no blind spots. Towed array provides extreme passive range but requires deployment time.

---

## Module ID Assignments

- **SON-001 to SON-004**: Passive Hydrophones
- **SON-005 to SON-007**: Active Searchlight Pattern
- **SON-008 to SON-011**: Active Scanning Pattern
- **SON-012 to SON-014**: Modern Sonar Systems

---

## Coverage Pattern Quick Reference

### Searchlight (Manual Aim)
```
         /|\  Narrow beam
        / | \  (15-25°)
       /  |  \ Must manually
      /   |   \ aim and sweep
```
**Use Case**: Final attack approach, precise ranging

### Scanning (Automatic Forward Arc)
```
       \    |    /
        \   |   /  Forward arc
         \  |  /   (120-180°)
          \ | /    Automatic
          [Ship]
```
**Use Case**: Convoy escort, general patrol

### Omnidirectional
```
       \    |    /
        \   |   /  360° coverage
      ---[Ship]--- All directions
        /   |   \  simultaneously
       /    |    \
```
**Use Case**: Maximum situational awareness, no blind spots

### Towed Array
```
    [Ship]
      |
      |  ~~~~~~~~  300m cable
      |
    [Array]  <--- Passive only
```
**Use Case**: Extreme-range passive detection, strategic patrol

---

## Tactical Decision Matrix

### When to Use Passive
- Initial search (don't alert enemy)
- Long-range detection
- Submarine vs submarine combat
- When trying to remain hidden
- Towed array for extreme range

### When to Use Active
- Attack run (need range for weapons)
- Target already alerted
- Depth charge/torpedo attack
- Lost contact, need to reacquire
- Final approach with Hedgehog/Squid

### Speed Considerations
- **Best Detection**: 0-10 knots
- **Good Detection**: 10-15 knots
- **Degraded**: 15-20 knots
- **Poor**: 20-25 knots
- **Minimal**: 25+ knots (towed array must retrieve)

---

## Historical Progression

**WWI Era (1915-1920)**
- Basic hydrophones (bearing only)
- Passive listening only
- Range: 3km

**Interwar (1920-1939)**
- First active ASDIC (searchlight pattern)
- Manual aim required
- Range: 1.5-2km active

**WWII (1940-1945)**
- Automatic scanning sonars
- Forward arc coverage
- Depth-finding variants
- Range: 3-4km active

**Early Cold War (1950-1960)**
- Wide-arc scanning (240°)
- Digital processing begins
- Range: 8km active

**Cold War (1960-1970)**
- True omnidirectional systems
- Bow dome arrays
- Range: 15km active

**Modern (1970+)**
- Towed arrays
- Extreme passive range
- Range: 30km+ passive

---

## Integration Notes

All sonar modules use consistent YAML frontmatter with:
- Coverage mechanics (scan_pattern, cone_angle, sweep_arc, sweep_time)
- Performance specs (ranges, depth, resolution, accuracy)
- Physical characteristics (weight, power, crew, reliability)
- Limitations (speed penalty, thermal layers, min range)

This allows consistent gameplay implementation across all variants.
