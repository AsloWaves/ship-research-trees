---
title: Radar Detection Mechanics
category: modules
subcategory: detection-radar
description: How radar coverage, cones, and sweep patterns work
tags: [radar, detection, mechanics, fog-of-war]
---

# Radar Detection Mechanics

> Radar modules vary not just in range, but in HOW they scan. This creates meaningful choices between coverage area, update speed, and operator control.

## Coverage Types

### 1. Rotating/Sweep Radar
The antenna rotates continuously, scanning 360° over time.

```
Coverage:        360° (full circle)
Update Rate:     One detection per rotation (4-15 seconds)
Pros:            Sees all directions
Cons:            Slow updates, target can move between sweeps
Best For:        General surveillance, convoy escort
```

**Gameplay**: Contacts appear on minimap but position updates only when the sweep passes them. Fast targets may "jump" between updates.

### 2. Sector Scan Radar
Antenna sweeps back and forth across a limited arc.

```
Coverage:        60-120° arc
Update Rate:     2-4x faster than full rotation
Pros:            Faster updates in chosen direction
Cons:            Blind spots outside sector
Best For:        Known threat direction, pursuit
```

**Gameplay**: Player chooses which direction to focus. Better tracking in that arc, but vulnerable from flanks.

### 3. Directional/Searchlight Radar
Narrow beam that must be manually aimed.

```
Coverage:        15-35° cone
Update Rate:     Continuous in that direction
Pros:            Best tracking, longest range in beam
Cons:            Very limited coverage, requires operator attention
Best For:        Fire control, tracking specific target
```

**Gameplay**: Player (or AI) must actively aim the radar. Excellent for gunnery but can lose targets easily.

### 4. Fixed Array (Modern)
Multiple fixed antenna elements, electronically steered.

```
Coverage:        360° simultaneous (multiple arrays)
Update Rate:     Near-instantaneous
Pros:            No blind spots, very fast
Cons:            Expensive, heavy, modern only
Best For:        AEGIS-type integrated combat
```

**Gameplay**: Best radar type but only available on modern ships.

---

## Operation Modes

### Auto Mode
- Radar operates automatically
- Consistent rotation/sweep
- No player input needed
- Default for most radars

### Manual Mode
- Player controls radar direction
- Can focus on specific contacts
- Requires attention
- Better tracking when used well

### Sector Lock
- Lock radar to specific arc (e.g., "Forward 90°")
- Automated within that sector
- Good compromise between auto and manual

---

## Detection Factors

| Factor | Effect |
|--------|--------|
| **Range** | Maximum detection distance |
| **Cone Width** | Area covered per sweep |
| **Rotation Speed** | How often area is updated |
| **Resolution** | Ability to distinguish close contacts |
| **Sea Clutter** | Performance in rough weather |
| **Target Size** | Larger = easier to detect |

---

## Radar Stats Template

Each radar module has:

```yaml
# Coverage
scan_type: rotating | sector | directional | fixed_array
cone_angle: 360        # degrees (360 = full rotation)
rotation_speed: 6      # seconds per full rotation
sector_options: [90, 120, 180]  # available sector modes

# Performance
detection_range: 35    # km
resolution: 500        # meters (minimum separation to distinguish)
accuracy: 90           # % bearing accuracy
height_finding: false  # can determine altitude?

# Operation
modes: [auto, manual, sector]
default_mode: auto
crew_required: 2

# Limitations
min_range: 500         # meters (too close to detect)
weather_penalty: 15    # % range reduction in storms
sea_clutter: moderate  # low/moderate/high
```

---

## Tactical Implications

### Sweep Radar (360°)
- Good for: Patrol, escort, general awareness
- Weakness: Fast torpedo boats can close between sweeps
- Counter: Multiple radar ships cover each other's gaps

### Sector Scan
- Good for: Chasing fleeing enemy, known threat direction
- Weakness: Ambush from unexpected direction
- Counter: Pair with lookouts covering other arcs

### Directional (Fire Control)
- Good for: Gunnery accuracy, tracking priority target
- Weakness: Single-target focus, lose big picture
- Counter: Dedicated fire control radar + separate search radar

---

## Historical Examples

| Radar | Type | Cone | Rotation | Notes |
|-------|------|------|----------|-------|
| Type 271 | Rotating | 360° | 8 sec | UK surface search |
| SG | Rotating | 360° | 6 sec | US standard |
| SC | Rotating | 360° | 4 sec | US air search |
| Mk 37 FCS | Directional | 20° | Manual | US fire control |
| Type 22 | Sector | 120° | 4 sec | IJN surface |
| FuMO 25 | Rotating | 360° | 10 sec | German surface |

---

## Integration with Fog of War

1. **Your radar** expands YOUR visibility circle
2. **Sweep pattern** determines WHEN you see contacts
3. **Cone angle** determines WHERE you can see
4. **Communication modules** let you SHARE what you see
5. **Enemy RWR** detects your radar transmissions

---

## Counters

| Counter | Effect |
|---------|--------|
| **Radar Warning Receiver** | Know when you're being scanned |
| **Radar Jammer** | Reduce enemy radar effectiveness |
| **Chaff** | Create false contacts |
| **Terrain** | Islands block radar |
| **Weather** | Heavy rain reduces range |
| **Stealth** | Reduced radar cross-section (modern) |
