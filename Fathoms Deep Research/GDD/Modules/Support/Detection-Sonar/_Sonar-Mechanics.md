---
title: Sonar Detection Mechanics
category: modules
subcategory: detection-sonar
description: How sonar coverage, ping patterns, and passive/active modes work
tags: [sonar, detection, mechanics, asw, submarines]
---

# Sonar Detection Mechanics

> Sonar modules detect underwater targets. The choice between passive (listening) and active (pinging) creates fundamental tactical decisions.

## Sonar Types

### 1. Passive Sonar (Hydrophones)
Listens for sounds without transmitting.

```
Detection:       Bearing ONLY (no range)
Stealth:         Target doesn't know you're listening
Coverage:        Depends on array type
Best For:        Initial detection, submarines hunting silently
```

**Gameplay**: Shows bearing line to contact, not position. Must triangulate with movement or multiple ships.

### 2. Active Sonar (ASDIC/Sonar)
Transmits ping, listens for echo.

```
Detection:       Bearing AND Range
Stealth:         Target KNOWS you're pinging (hears it)
Coverage:        Cone pattern based on type
Best For:        Attack approach, depth charge targeting
```

**Gameplay**: Shows actual contact position, but target gets warning.

### 3. Variable Depth Sonar (VDS)
Sonar lowered below thermal layers.

```
Detection:       Can detect below thermal layers
Deployment:      Requires slow speed
Coverage:        Similar to hull sonar
Best For:        Finding deep-diving submarines
```

### 4. Towed Array (Modern)
Long passive array towed behind ship.

```
Detection:       Very long range passive
Stealth:         Completely passive
Coverage:        Primarily rear arc
Best For:        Long-range submarine detection
Limitation:      Cannot operate at high speed
```

---

## Coverage Patterns

### Searchlight Sonar (Early)
Narrow beam that must be aimed manually.

```
Cone Angle:      15-25°
Control:         Manual aim required
Update:          Continuous in aimed direction
Weakness:        Very limited coverage
```

**Gameplay**: Operator must sweep manually. Easy to miss contacts.

### Scanning Sonar
Beam sweeps automatically across an arc.

```
Cone Angle:      10-15° beam
Sweep Arc:       120-180° forward
Sweep Time:      3-6 seconds per sweep
Update:          Each time beam passes contact
```

**Gameplay**: Automatic but limited to forward arc. Contacts behind ship not detected.

### Omnidirectional Sonar (Modern)
Multiple elements provide 360° coverage.

```
Coverage:        360° horizontal
Update:          Near-continuous
Resolution:      Good
Availability:    1960s+
```

---

## Passive vs Active Decision

| Factor | Passive | Active |
|--------|---------|--------|
| **Range info** | No | Yes |
| **Bearing info** | Yes | Yes |
| **Alerts target** | No | YES |
| **Range** | Long (listening) | Medium (ping return) |
| **Affected by own noise** | Very much | Less |
| **Thermal layers** | Blocked | Blocked |

### When to Use Passive
- Initial search (don't alert enemy)
- Own submarine hunting
- Long-range detection
- When trying to remain hidden

### When to Use Active
- Attack run (need range for weapons)
- Target already alerted
- Depth charge/torpedo attack
- Lost contact, need to reacquire

---

## Sonar Stats Template

```yaml
# Type
sonar_type: passive | active | vds | towed
hull_mounted: true

# Coverage (Active only)
scan_pattern: searchlight | scanning | omni
cone_angle: 15         # degrees per beam
sweep_arc: 150         # degrees total coverage
sweep_time: 4          # seconds per sweep

# Performance
detection_range_active: 4    # km
detection_range_passive: 8   # km (bearing only)
depth_capability: 200        # meters
resolution: 100              # meters

# Limitations
own_speed_penalty: true      # faster = worse detection
thermal_layer_blocked: true
min_range: 200               # meters (too close)
crew_required: 2
```

---

## Environmental Factors

### Thermal Layers
Water temperature changes create "layers" that block/bend sonar.

```
Effect:          Sonar may not detect targets below layer
Counter:         Variable Depth Sonar (VDS)
Depth:           Varies by location/season (50-200m typical)
```

### Own Ship Noise
Your own propellers and machinery create noise.

```
Stopped:         Best passive detection
Slow (5 kts):    Good detection
Medium (15 kts): Degraded (-30% range)
Fast (25+ kts):  Very degraded (-60% range)
```

### Sea State
Rough seas create noise and bubbles.

```
Calm:            Normal performance
Moderate:        -10% range
Rough:           -25% range
Storm:           -50% range or unusable
```

---

## Historical Sonar Types

### Passive (Hydrophones)
| Model | Nation | Era | Range | Notes |
|-------|--------|-----|-------|-------|
| Type 123 | UK | 1935 | 3km | Early hydrophone |
| JP/JK | USA | 1940 | 4km | Submarine hydrophone |
| GHG | Germany | 1935 | 5km | Excellent passive |

### Active (ASDIC/Sonar)
| Model | Nation | Era | Range | Pattern | Notes |
|-------|--------|-----|-------|---------|-------|
| ASDIC Type 123 | UK | 1935 | 1.5km | Searchlight | Manual aim |
| ASDIC Type 144 | UK | 1940 | 3km | Scanning | Standard WWII |
| ASDIC Type 147 | UK | 1943 | 4km | Scanning | Ahead-throwing |
| QC | USA | 1940 | 2.5km | Searchlight | Early US |
| QGB | USA | 1943 | 4km | Scanning | Improved |
| SQS-4 | USA | 1955 | 8km | Scanning | Post-war |
| SQS-26 | USA | 1960 | 15km | Omni | Bow dome |

---

## Tactical Use

### Submarine Hunting
1. **Passive search** at slow speed (don't alert target)
2. **Detect bearing** to contact
3. **Close range** while maintaining contact
4. **Switch to active** for attack solution
5. **Weapons release** (depth charges/torpedoes)

### Submarine Evasion
1. **Silent running** (minimize own noise)
2. **Go deep** (below thermal layer)
3. **Change course** when hunter pings
4. **Use terrain** (underwater ridges block sonar)

---

## Integration with Fog of War

1. **Passive sonar** shows bearing lines only (like spokes)
2. **Active sonar** shows actual contact positions
3. **Multiple ships** can triangulate passive contacts
4. **Sonar contacts** do NOT appear on minimap without CIC bridge
5. **Submarines** only visible to sonar (not radar when submerged)
