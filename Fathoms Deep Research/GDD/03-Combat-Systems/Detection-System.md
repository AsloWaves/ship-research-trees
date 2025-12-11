---
title: Detection System Mechanics
category: combat-systems
description: Comprehensive mechanics for visual, radar, and sonar detection with mathematical formulas
version: 1.0
last_updated: 2025-12-09
tags: [detection, mechanics, formulas, fog-of-war, visual, radar, sonar]
---

# Detection System Mechanics

> Detection is the foundation of naval combat. You cannot fight what you cannot see. This document defines precisely how ships detect each other and what information becomes available at each stage.

## Design Philosophy

The detection system creates meaningful gameplay through:

1. **Asymmetric Information** - You never have complete knowledge
2. **Equipment Choices Matter** - Better sensors = better awareness
3. **Era Progression** - Technology dramatically changes detection
4. **Risk/Reward** - Active sensors reveal your position
5. **Team Coordination** - Share what you see with allies

---

## Core Detection Formula

All detection uses this fundamental calculation:

```
Effective_Detection_Range = Base_Range
                            × Target_Size_Modifier
                            × Environmental_Modifier
                            × Equipment_Modifier
                            × Crew_Skill_Modifier
```

### Base Range by Detection Type

| Detection Type | Daylight Base | Night Base | Notes |
|----------------|---------------|------------|-------|
| **Visual (Naked Eye)** | 8 km | 1 km | Horizon limited |
| **Visual (Binoculars)** | 15 km | 2 km | 7x magnification |
| **Visual (Director Tower)** | 20 km | 3 km | Elevated + optics |
| **Rangefinder 1m** | 8 km | 0 km | Range only, no detection |
| **Rangefinder 9m** | 25 km | 0 km | Battleship standard |
| **Rangefinder 15m** | 35 km | 0 km | Super-battleship |
| **Searchlight 36"** | N/A | 5 km | Reveals YOUR position |
| **Searchlight 60"** | N/A | 8 km | Heavy illumination |
| **Radar (Surface)** | 20-50 km | Same | Unaffected by light |
| **Radar (Air Search)** | 60-120 km | Same | Detects aircraft |
| **Hydrophone (Passive)** | 3-8 km | Same | Bearing only |
| **Active Sonar** | 1.5-15 km | Same | Reveals YOUR position |

---

## Target Size Modifiers

Larger ships are easier to detect:

| Ship Type | Size Modifier | Visual Signature | Radar Cross-Section |
|-----------|---------------|------------------|---------------------|
| **Battleship (BB)** | 1.5× | Massive superstructure | Very Large |
| **Aircraft Carrier (CV)** | 1.6× | Island + flight deck | Very Large |
| **Heavy Cruiser (CA)** | 1.2× | Large superstructure | Large |
| **Light Cruiser (CL)** | 1.1× | Medium superstructure | Medium-Large |
| **Destroyer (DD)** | 1.0× (baseline) | Moderate | Medium |
| **Destroyer Escort (DE)** | 0.9× | Small | Small-Medium |
| **Submarine (surfaced)** | 0.7× | Low profile | Small |
| **Submarine (snorkel)** | 0.3× | Snorkel only | Very Small |
| **Submarine (periscope)** | 0.1× | Periscope tip | Minimal |
| **Submarine (submerged)** | 0× (visual) | Invisible | N/A (sonar only) |
| **PT Boat (PT)** | 0.5× | Very small | Small |
| **Merchant (large)** | 1.3× | High profile | Large |
| **Merchant (small)** | 0.8× | Low profile | Medium |

### Smoke/Camouflage Modifiers

| Condition | Visual Modifier | Radar Modifier |
|-----------|-----------------|----------------|
| **Normal** | 1.0× | 1.0× |
| **Making Smoke** | 0.3× | 1.0× (radar unaffected) |
| **In Smoke Screen** | 0.1× | 1.0× |
| **Dazzle Camouflage** | 0.85× | 1.0× |
| **Low Visibility Paint** | 0.9× | 1.0× |

---

## Environmental Modifiers

### Weather Effects

| Condition | Visual | Radar | Sonar | Notes |
|-----------|--------|-------|-------|-------|
| **Clear Day** | 1.0× | 1.0× | 1.0× | Baseline |
| **Overcast** | 0.9× | 1.0× | 1.0× | Slight visual reduction |
| **Light Rain** | 0.7× | 0.9× | 0.95× | Rain reduces radar |
| **Heavy Rain** | 0.4× | 0.7× | 0.9× | Significant degradation |
| **Fog (Light)** | 0.5× | 1.0× | 1.0× | Radar advantage |
| **Fog (Dense)** | 0.2× | 0.95× | 1.0× | Radar essential |
| **Storm** | 0.3× | 0.5× | 0.6× | All degraded |
| **Snow/Sleet** | 0.4× | 0.6× | 0.9× | Radar degraded |
| **Night (Clear)** | 0.15× | 1.0× | 1.0× | Moon provides some light |
| **Night (Overcast)** | 0.05× | 1.0× | 1.0× | Nearly blind |
| **Night + Fog** | 0.02× | 0.95× | 1.0× | Radar critical |

### Sea State Effects

| Sea State | Description | Visual | Radar | Sonar |
|-----------|-------------|--------|-------|-------|
| **0** | Calm (mirror) | 1.0× | 1.0× | 1.0× |
| **1** | Rippled | 1.0× | 1.0× | 1.0× |
| **2** | Smooth wavelets | 1.0× | 0.98× | 0.98× |
| **3** | Slight (0.5-1.25m) | 0.95× | 0.95× | 0.95× |
| **4** | Moderate (1.25-2.5m) | 0.9× | 0.9× | 0.9× |
| **5** | Rough (2.5-4m) | 0.8× | 0.8× | 0.8× |
| **6** | Very Rough (4-6m) | 0.6× | 0.7× | 0.7× |
| **7** | High (6-9m) | 0.4× | 0.5× | 0.5× |
| **8+** | Very High/Phenomenal | 0.2× | 0.3× | 0.3× |

### Thermal Layer Effects (Sonar Only)

| Condition | Active Sonar | Passive Sonar | Counter |
|-----------|--------------|---------------|---------|
| **No Layer** | 1.0× | 1.0× | N/A |
| **Shallow Layer (50m)** | 0.7× below | 0.6× below | VDS |
| **Deep Layer (150m)** | 0.5× below | 0.4× below | VDS |
| **Multiple Layers** | 0.3× deep | 0.2× deep | Towed Array |

---

## Detection Phases

Detection isn't binary - contacts progress through visual stages as they move from deep in the fog of war toward your ship. Equipment quality affects both the **range** at which each phase triggers and the **quality of information** revealed.

**Fog of War Terminology:**
- **Inside Fog of War** = Outside your detection circle (cannot see)
- **Inside Your Circle** = Outside the fog of war (can see)

---

### Phase 1: Distant Contact (Deep in Fog of War)

**Location:** Target is far outside your visible circle, deep in the fog of war.

**Visual:** Nothing visible on screen - the target ship does not render.

**UI Indicator:** A directional indicator appears showing the rough direction of the contact.

| Equipment Level | Direction Accuracy | Range Information |
|-----------------|-------------------|-------------------|
| **Basic (Pre-1920)** | Wide arc (±30°), randomized within band | None |
| **Standard (1920-1940)** | Moderate arc (±15°), some randomization | None |
| **Advanced (1940+)** | Narrow arc (±8°) | Approximate range band |
| **Modern (1960+)** | Precise bearing (±3°) | Estimated range |

**Design Note:** Direction is randomized within the arc so players cannot simply aim at the center of the band to find the target. This creates uncertainty and rewards closing to improve detection.

---

### Phase 2: Emerging Contact (Edge of Detection)

**Location:** Target is approaching the edge of your detection circle.

**Visual:** A shadow or oval silhouette begins to emerge from the fog of war. The closer the target gets, the more defined the shadow becomes.

| Equipment Level | Shadow Behavior | Transition Point |
|-----------------|-----------------|------------------|
| **Basic** | Vague shadow, only visible at edge of circle | Shadow remains until fully inside circle |
| **Standard** | Clearer shadow, earlier appearance | Shadow transitions to sprite at circle edge |
| **Advanced** | Defined shadow with size indication | Earlier sprite transition |
| **Modern** | Shadow includes heading indicator | Very early sprite transition |

**Stealth/Camouflage:** Stealth affects detection in two ways:

1. **Delayed Shadow Appearance** - High-stealth targets may not trigger Phase 2 until much closer than normal, or skip it entirely for maximum surprise:

| Stealth Level | Phase 2 Trigger | Effect |
|---------------|-----------------|--------|
| Normal | 1.0× base range | Standard shadow appearance |
| Low Profile | 0.7× base range | Shadow appears 30% closer |
| Stealthy | 0.5× base range | Shadow appears 50% closer |
| Very Stealthy | 0.3× base range | Shadow appears very late |
| Maximum Stealth | Skip Phase 2 | No shadow - sprite appears suddenly |

2. **Extended Shadow Duration** - Some ships remain as silhouettes even after crossing inside the detection circle:

| Condition | Shadow Extension |
|-----------|------------------|
| Low-profile ships (submarines, PT boats) | +50% shadow duration |
| Camouflage paint schemes | +20% shadow duration |
| Electronic warfare / radar absorption | +30% shadow duration |
| Night operations without illumination | +40% shadow duration |
| Combined effects | Stack multiplicatively |

**Shadow Shape & Misidentification:**

Shadow size provides a *hint* about ship size, but is deliberately imprecise - historically, misidentification was extremely common (destroyers mistaken for cruisers, escort carriers for fleet carriers, etc.).

**Shadow Size Determination:**
```
Displayed_Shadow_Size = Actual_Size + Random_Variance

Random_Variance = Roll(-Variance_Range, +Variance_Range)

Variance_Range by Equipment:
- Basic: ±2 size categories (very unreliable)
- Standard: ±1 size category (somewhat reliable)
- Advanced: ±0.5 size category (mostly accurate)
- Modern: ±0.25 size category (highly accurate)
```

**Size Categories (1-6 scale):**
| Category | Size Value | Ship Types |
|----------|------------|------------|
| Tiny | 1 | PT boats, midget submarines |
| Small | 2 | Destroyers, submarines, corvettes |
| Medium | 3 | Light cruisers, destroyer leaders |
| Large | 4 | Heavy cruisers, light carriers |
| Very Large | 5 | Battleships, fleet carriers |
| Massive | 6 | Super-battleships (Yamato), supercarriers |

**Example Misidentification (Basic Equipment):**
- Actual target: Destroyer (Size 2)
- Variance range: ±2
- Possible roll: +2
- Displayed shadow: Size 4 (Large) → Player sees "cruiser-sized" shadow
- Result: Player may prepare for cruiser fight, surprised when destroyer appears

**Example Accurate Detection (Advanced Equipment):**
- Actual target: Destroyer (Size 2)
- Variance range: ±0.5
- Possible roll: +0.3
- Displayed shadow: Size 2.3 → Rounds to Size 2 (Small)
- Result: Player correctly anticipates destroyer

**Shadow Refinement:** As the target gets closer (deeper into Phase 2), the shadow size becomes more accurate:
```
Effective_Variance = Base_Variance × (Distance_to_Phase3 / Phase2_Range)
```
This means the shadow "settles" toward actual size as the target approaches Phase 3.

**Historical Misidentifications:**
- Battle of Samar: Japanese misidentified escort carriers as fleet carriers, destroyers as cruisers
- Battle of Savo Island: Allied forces misidentified Japanese cruisers approaching
- Many night battles: Friendly fire due to misidentification
- Submarine contacts: Surface ships frequently misidentified as submarines and vice versa

---

### Phase 3: Visible Contact (Inside Circle)

**Location:** Target has crossed inside your detection circle - outside the fog of war.

**Visual:** The actual ship sprite becomes visible, replacing the shadow.

| Equipment Level | Sprite Quality | Additional Information |
|-----------------|----------------|------------------------|
| **Basic** | Blurry/indistinct sprite | Ship type only (BB/CA/DD/etc.) |
| **Standard** | Clear sprite | Ship type + general heading |
| **Advanced** | Clear sprite + visible guns | Ship class + firing solution begins calculating |
| **Modern** | High detail sprite | Ship class + nationality + solution calculates faster |

**Firing Solution:** Advanced and Modern systems begin calculating a firing solution at this phase. See [[#Firing Solution Quality]] for the complete dynamic solution system - solution is a "living number" affected by both ships' movement.

**Gun Visibility by Equipment:**

| Equipment | What Player Sees |
|-----------|------------------|
| **Basic** | Sprite only - no gun details. Must recognize ship visually. |
| **Standard** | Sprite + turret positions visible. No caliber info. |
| **Advanced** | Sprite + turrets + approximate caliber (Small/Medium/Large) |
| **Modern** | Sprite + turrets + caliber + turret rotation direction |

**Practical Impact:**
- Basic/Standard players must learn to recognize ship silhouettes to know what they're facing
- A player might see "that looks like a battleship sprite" but won't know if it has 14" or 16" guns until Advanced equipment or Phase 4
- Turret rotation (which way guns are pointing) only visible with Modern equipment - critical for knowing if you're being targeted

---

### Phase 4: Full Contact (Close Range / Locked)

**Location:** Target is at close range OR player has achieved targeting lock.

**Visual:** Full ship detail with all visual information rendered.

| Equipment Level | Information Displayed |
|-----------------|----------------------|
| **Basic** | Turret details + health bar |
| **Standard** | Above + ship class name + speed category |
| **Advanced** | Above + precise speed + heading + player name |
| **Modern** | Above + damage state + module status + predicted course |

**Information Breakdown:**

| Data | Basic | Standard | Advanced | Modern |
|------|-------|----------|----------|--------|
| Health Bar | ✓ | ✓ | ✓ | ✓ |
| Turret Details | ✓ | ✓ | ✓ | ✓ |
| Ship Class | - | ✓ | ✓ | ✓ |
| Speed Category | - | ✓ | ✓ | ✓ |
| Precise Speed | - | - | ✓ | ✓ |
| Heading (degrees) | - | - | ✓ | ✓ |
| Player Name | - | - | ✓ | ✓ |
| Damage State | - | - | - | ✓ |
| Module Status | - | - | - | ✓ |
| Predicted Course | - | - | - | ✓ |

---

### Phase Transition Ranges

The range at which each phase triggers depends on equipment and conditions:

```
Phase_Trigger_Range = Base_Detection_Range × Phase_Multiplier × Equipment_Modifier

Phase Multipliers:
- Phase 1 (Distant): 1.5× base range (earliest warning)
- Phase 2 (Emerging): 1.0× base range (at detection edge)
- Phase 3 (Visible): 0.7× base range (inside circle)
- Phase 4 (Full): 0.4× base range OR targeting lock achieved
```

**Example:** Ship with 20km base detection range:
- Phase 1 triggers at 30km (distant contact indicator)
- Phase 2 triggers at 20km (shadow emerges)
- Phase 3 triggers at 14km (sprite visible)
- Phase 4 triggers at 8km (full information)

---

### Losing Contact

When a target moves back outside detection range or breaks lock:

| Phase Lost From | Result |
|-----------------|--------|
| Phase 4 → 3 | Full info fades, sprite remains |
| Phase 3 → 2 | Sprite fades to shadow |
| Phase 2 → 1 | Shadow fades, direction indicator only |
| Phase 1 → Lost | Contact marker disappears after delay |

**Contact Memory:** Last known position/heading displayed with "stale" indicator for:
- Basic: 30 seconds
- Standard: 60 seconds
- Advanced: 120 seconds
- Modern: 300 seconds (5 minutes)

---

### Firing Solution Quality

> **See [[Firing-Solution-System]] for the authoritative, complete firing solution mechanics.**
> The section below provides a summary; the full document resolves all formula contradictions.

The firing solution is a **living number** that constantly fluctuates based on both your ship's movement and the target's movement. Even a 100% solution can degrade if conditions change.

```
Solution_Change_Per_Second = Buildup_Rate - Degradation_Rate

Current_Solution = Previous_Solution + Solution_Change_Per_Second
(Clamped between 0% and Equipment_Cap)
```

#### Solution Buildup

Solution builds when tracking a target in Phase 3+:

| Equipment Level | Base Buildup Rate | Requirements |
|-----------------|-------------------|--------------|
| Basic | +0%/sec (manual only) | Must use rangefinder manually |
| Standard | +2%/sec | Continuous visual/radar contact |
| Advanced | +5%/sec | Continuous contact + fire control lock |
| Modern | +10%/sec | Automatic tracking systems |

**Buildup Modifiers:**
| Condition | Buildup Modifier |
|-----------|------------------|
| Fire control radar locked | +50% buildup rate |
| Optical rangefinder active | +25% buildup rate |
| Target on steady course | +20% buildup rate |
| Target at constant speed | +20% buildup rate |
| Calm seas (State 0-2) | +10% buildup rate |

#### Solution Degradation (Continuous)

Degradation is calculated every second and SUBTRACTED from buildup:

**Your Ship Movement:**
| Action | Degradation Rate |
|--------|------------------|
| Steady course & speed | 0%/sec |
| Minor course correction (<10°) | -1%/sec |
| Moderate turn (10-30°) | -3%/sec |
| Hard turn (>30°) | -6%/sec |
| Speed change (±5 knots) | -2%/sec |
| Speed change (±10+ knots) | -4%/sec |
| Evasive maneuvers | -8%/sec |

**Target Movement:**
| Action | Degradation Rate |
|--------|------------------|
| Steady course & speed | 0%/sec |
| Minor course change (<10°) | -2%/sec |
| Moderate turn (10-30°) | -5%/sec |
| Hard turn (>30°) | -10%/sec |
| Speed change (±5 knots) | -3%/sec |
| Speed change (±10+ knots) | -6%/sec |
| Evasive zigzag pattern | -12%/sec |

**External Factors:**
| Condition | Degradation Rate |
|-----------|------------------|
| Target entering smoke | -8%/sec |
| Target in smoke screen | -15%/sec (solution collapses fast) |
| Radar interference/jamming | -5%/sec |
| Heavy weather (State 6+) | -3%/sec |
| Losing radar contact | -10%/sec |
| Losing visual contact | -10%/sec |
| Complete contact loss | -25%/sec |

#### Solution Examples

**Example A: Stable Engagement**
```
Your ship: Steady course, steady speed (0%/sec degradation)
Target: Steady course, steady speed (0%/sec degradation)
Equipment: Advanced (+5%/sec buildup)
Fire control radar: Locked (+50% = +7.5%/sec total buildup)

Net change: +7.5%/sec
Time to 95% cap: ~13 seconds
Result: Excellent firing conditions
```

**Example B: Maneuvering Battle**
```
Your ship: Moderate turn (-3%/sec)
Target: Hard turn + speed change (-10% + -6% = -16%/sec)
Equipment: Advanced (+5%/sec buildup)
Fire control radar: Locked (+50% = +7.5%/sec total buildup)

Net change: +7.5 - 3 - 16 = -11.5%/sec
Result: Solution DROPPING rapidly - hold fire or stabilize!
```

**Example C: Target Uses Smoke**
```
Your ship: Steady (0%/sec)
Target: Enters smoke screen (-15%/sec)
Equipment: Standard (+2%/sec buildup)

Net change: +2 - 15 = -13%/sec
Result: Solution collapsing! Switch to radar or close range.
```

#### Solution Quality Effects

| Solution % | Accuracy Mod | Visual Indicator | Tactical Meaning |
|------------|--------------|------------------|------------------|
| 0-25% | 0.5× | Red/empty bar | Don't fire - wasting ammo |
| 26-50% | 0.7× | Orange/partial | Spray and pray |
| 51-75% | 0.85× | Yellow/half | Reasonable chance to hit |
| 76-90% | 0.95× | Light green | Good firing conditions |
| 91-100% | 1.0× | Bright green/full | Optimal - fire for effect |

#### Solution Cap by Equipment

Even under perfect conditions, equipment limits maximum solution:

| Equipment | Max Solution | Reason |
|-----------|--------------|--------|
| Basic | 50% | Manual ranging, no computer assistance |
| Standard | 75% | Mechanical fire control, limited calculation |
| Advanced | 95% | Electro-mechanical computers, radar ranging |
| Modern | 100% | Digital fire control, automatic tracking |

#### Maintaining Solution

Tips for keeping solution high:
1. **Steady your ship** before firing - course/speed changes hurt your solution
2. **Wait for target to steady** - maneuvering targets are hard to hit
3. **Use smoke offensively** - pop smoke to break THEIR solution on you
4. **Upgrade fire control** - better equipment = faster buildup, higher cap
5. **Coordinate with allies** - one ship spots, another fires from stable position

---

## Detection by Type

### Visual Detection

```
Visual_Range = Base_Visual
               × Elevation_Bonus
               × Weather_Modifier
               × Target_Size
               × Lookout_Skill

Elevation_Bonus = 1 + (Observer_Height_meters / 50)
```

**Elevation Examples:**
| Position | Height | Bonus |
|----------|--------|-------|
| Bridge (DD) | 10m | 1.2× |
| Bridge (CA) | 15m | 1.3× |
| Crow's Nest | 25m | 1.5× |
| Pagoda Top (BB) | 40m | 1.8× |

**Lookout Skill Levels:**
| Skill | Modifier | Notes |
|-------|----------|-------|
| Green | 0.7× | Inexperienced |
| Average | 1.0× | Baseline |
| Trained | 1.15× | Standard navy |
| Expert | 1.3× | Veteran lookouts |
| Elite | 1.5× | Japanese night-trained |

### Radar Detection

See [[../Modules/Support/Detection-Radar/_Radar-Mechanics|Radar Mechanics]] for detailed radar operations.

```
Radar_Range = Module_Base_Range
              × Weather_Modifier
              × Target_RCS
              × Electronic_Warfare_Modifier

Target_RCS (Radar Cross Section):
- Battleship: 1.5×
- Carrier: 1.6×
- Cruiser: 1.1-1.2×
- Destroyer: 1.0×
- Submarine (surfaced): 0.4×
- PT Boat: 0.3×
```

**Radar Sweep Timing:**
- Contact appears when sweep passes target
- Fast targets may "jump" between sweeps
- Sector scan: 2-4× faster updates in chosen direction
- Fire control radar: Continuous tracking in narrow beam

### Sonar Detection

See [[../Modules/Support/Detection-Sonar/_Sonar-Mechanics|Sonar Mechanics]] for detailed sonar operations.

**Passive Sonar (Hydrophone):**
```
Passive_Range = Base_Range
                × Target_Noise_Level
                × Own_Speed_Penalty
                × Sea_State_Modifier
                × Thermal_Layer_Modifier

Target_Noise_Level:
- Submarine (silent): 0.3×
- Submarine (creeping): 0.5×
- Submarine (normal): 1.0×
- Submarine (flank): 1.5×
- Surface ship (slow): 1.2×
- Surface ship (cruising): 1.5×
- Surface ship (flank): 2.0×

Own_Speed_Penalty:
- Stopped: 1.0×
- 5 knots: 0.9×
- 10 knots: 0.7×
- 15 knots: 0.5×
- 20+ knots: 0.3×
```

**Active Sonar:**
```
Active_Range = Base_Range
               × Sea_State_Modifier
               × Thermal_Layer_Modifier
               × Own_Speed_Penalty (reduced effect)

Active reveals YOUR position to target!
```

---

## Equipment Integration

### Bridge Tier → Detection Features

Bridge tier determines what phases you can access and the quality of information at each phase:

| Bridge Tier | Equipment Level | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Radar Minimap |
|-------------|-----------------|---------|---------|---------|---------|---------------|
| Open (1890) | Basic | Wide arc only | Vague shadow | Blurry sprite | Turrets + HP only | None |
| Enclosed (1910) | Basic | Wide arc only | Vague shadow | Blurry sprite | Turrets + HP only | None |
| Interwar (1920) | Standard | Moderate arc | Clear shadow | Clear sprite | + Class + Speed | None |
| Director (1925) | Standard | Moderate arc | Clear shadow | Clear sprite + guns | + Class + Speed | None |
| CIC (1940) | Advanced | Narrow arc + range | Defined shadow | Clear + solution | + Full data | Yes |
| Modern (1970) | Modern | Precise bearing | Shadow + heading | High detail + fast solution | + Everything | Enhanced |

**Key Differences by Bridge:**

| Feature | Basic Bridges | Standard Bridges | Advanced Bridges | Modern Bridges |
|---------|---------------|------------------|------------------|----------------|
| Direction accuracy | ±30° randomized | ±15° | ±8° + range band | ±3° + range |
| Shadow size variance | ±2 categories (unreliable) | ±1 category | ±0.5 category | ±0.25 category |
| Shadow clarity | Vague oval | Clear oval | Defined + sized | + Heading indicator |
| Sprite detail | Blurry | Clear | Clear + guns visible | High detail |
| Solution buildup | None (manual) | 2%/sec (75% cap) | 5%/sec (95% cap) | 10%/sec (100% cap) |
| Phase 4 info | HP + turrets | + Class + speed category | + Precise speed/heading | + Everything |
| Auto-tracking | No | No | Yes (manual lock) | Yes (auto) |

### Module Stacking Rules

**Multiple Lookouts:**
```
Combined_Range = Best_Lookout_Range × (1 + 0.1 × Additional_Lookouts)
Maximum bonus: +30% (3 additional lookouts)
```

**Multiple Radars:**
- Each radar operates independently
- Best range from each type applies
- Fire control radar requires separate lock

**Multiple Sonars:**
- Passive: Ranges add (for triangulation)
- Active: Best range applies
- Cannot run active and passive simultaneously at full effectiveness

---

## Communication and Sharing

Detection is only as good as your ability to share it. Communication in Fathoms Deep is **tactical** - every method has trade-offs between range, security, and interception risk.

---

### Communication Methods

#### Local Chat (Text)

Default text communication with NO modules required.

| Property | Value |
|----------|-------|
| Range | ~2 km radius around sender |
| Who Sees | **EVERYONE in range** - allies AND enemies |
| Security | None - completely open |
| Use Case | Desperation, taunting, local coordination |

**Warning:** If an enemy ship is within 2km, they will see your local chat messages!

---

#### Signal Light (Visual)

Directional light beam communication - like a lighthouse beam.

**Basic Signal Lamp:**
| Property | Value |
|----------|-------|
| Range | 5-15 km (depends on lamp size) |
| Beam Width | 30° cone |
| Who Sees | Anyone inside the beam cone |
| Security | Cannot be intercepted UNLESS enemy is in beam path |
| Detection Info | Bearing only |
| Message Type | Flash to get attention (no text) |

**Advanced Signal Lamp:**
| Property | Value |
|----------|-------|
| Range | 10-20 km |
| Beam Width | 15° cone (more focused) |
| Who Sees | Anyone inside the beam cone |
| Security | Cannot be intercepted UNLESS enemy is in beam path |
| Detection Info | Bearing + ship type |
| Message Type | Text message visible only to players in beam |

**Tactical Considerations:**
- Aim your light beam AWAY from enemies
- If enemy ship is between you and ally, they may intercept the beam
- Night operations: Light beam is visible to everyone as a visual effect (reveals YOUR position)
- Day operations: Less visible but still detectable at close range

```
Light_Interception:
- Enemy INSIDE beam cone: Sees full message
- Enemy OUTSIDE beam: Sees nothing (unless they see the light source itself)
- Cannot be intercepted electronically
```

---

#### Voice Chat (In-Game Voice)

Spatial voice communication following realistic rules.

**Local Voice (No Module):**
| Property | Value |
|----------|-------|
| Range | ~1 km radius |
| Who Hears | Everyone in range - allies AND enemies |
| Security | None |
| Use Case | Close-range coordination, yelling at nearby ships |

**Directional Voice (With Module):**
| Property | Value |
|----------|-------|
| Range | 3-5 km |
| Direction | Cone toward target ship |
| Who Hears | Ships in voice cone direction |
| Security | Enemies in cone can hear |

---

#### Radio Communication

Electronic communication - longer range but can be INTERCEPTED.

**TBS (Talk Between Ships) - Voice Radio:**
| Property | Value |
|----------|-------|
| Range | 20 km |
| Who Receives | All allied ships with TBS in range |
| Security | **CAN BE INTERCEPTED** by enemies with radio intercept modules |
| Detection Info | Full Phase 1-2 data |
| Interception | Enemy hears voice but may not understand coded messages |

**Fleet Radio (HF/VHF):**
| Property | Value |
|----------|-------|
| Range | 50 km |
| Who Receives | All allied ships with compatible radio |
| Security | **CAN BE INTERCEPTED** by enemies with signals intelligence |
| Detection Info | Full Phase 1-3 data |
| Interception | Text appears garbled unless enemy has decryption |

**Secure Radio (UHF/Encrypted):**
| Property | Value |
|----------|-------|
| Range | 30 km |
| Who Receives | Allied ships with matching encryption |
| Security | Harder to intercept - requires advanced SIGINT |
| Detection Info | Full Phase 1-3 data |
| Interception | Enemy knows transmission occurred but content encrypted |

---

#### Data Link (Modern)

Digital tactical data sharing.

| Property | Value |
|----------|-------|
| Range | 100 km |
| Who Receives | All ships with compatible data link |
| Security | **CAN BE INTERCEPTED** with advanced electronic warfare |
| Detection Info | Full Phase 1-4 data (automatic sharing) |
| Update Rate | Real-time (1 second delay) |
| Interception | Requires dedicated SIGINT module + decryption capability |

---

### Interception & Signals Intelligence

Enemies can intercept your communications with the right equipment:

| Your Comm Type | Enemy Module Required | What Enemy Gets |
|----------------|----------------------|-----------------|
| Local Chat | None (just be nearby) | Full text |
| Signal Light | None (just be in beam) | Full message |
| Local Voice | None (just be nearby) | Full voice |
| TBS Radio | Radio Intercept (Basic) | Voice audio |
| Fleet Radio | Radio Intercept (Standard) | Garbled text |
| Secure Radio | SIGINT Suite | Knows transmission occurred |
| Data Link | SIGINT Suite + Decryption | Partial data (if decrypted) |

**Counter-Intelligence:**
- Use signal lights when enemy positions are known (aim away from them)
- Maintain radio silence when enemy SIGINT suspected
- Use pre-arranged signals/codes that enemies can't understand
- Data link gives away your presence to SIGINT-equipped enemies

---

### Detection Info Sharing

| Communication Type | Detection Detail Shared |
|--------------------|------------------------|
| Signal Light (Basic) | Bearing only |
| Signal Light (Advanced) | Bearing + type |
| TBS Voice | Phase 1-2 (direction, shadow size) |
| Fleet Radio | Phase 1-3 (+ sprite identification) |
| Data Link | Phase 1-4 (full tactical picture) |

### Shared Information & Misidentification

**Critical Rule:** When you share detection info, allies receive YOUR assessment - including any misidentification errors.

```
Shared contacts use the SENDER's detection data:
- Shadow size (including variance roll errors)
- Direction accuracy (sender's equipment level)
- Phase level (sender's current phase)

Allies accept this as FACT until they can detect the contact themselves.
```

**When Allies Override Shared Data:**
- When ally enters their own Phase 2 range → They roll their own shadow size
- When ally enters Phase 3 → They see actual sprite (truth revealed)
- Better-equipped ally detecting same contact → Can share corrected info

**Gameplay Implications:**
| Scenario | Result |
|----------|--------|
| You misidentify DD as CA, radio your fleet | Fleet prepares for cruiser until someone sees it themselves |
| Scout has Basic equipment, reports "battleship" | Fleet commits based on potentially wrong intel |
| Enemy intercepts your radio | Enemy knows your assessment (even if wrong!) |
| Signal light to ally | Secure unless enemy is in beam path |

---

### Group/Fleet Communication Requirements

**Without Modules:**
- Local chat only (2km, everyone sees)
- Local voice only (1km, everyone hears)
- Signal light if lamp equipped

**With Radio Module:**
- TBS/Fleet radio to allied ships in range
- Subject to interception

**With Data Link Module:**
- Automatic real-time detection sharing
- Subject to interception

**Secure Fleet Coordination Requires:**
- Encrypted radio modules on all ships
- Or careful signal light communication
- Or pre-arranged rendezvous points

---

### Triangulation (Passive Sonar)

```
If 2+ ships have passive sonar bearing to same contact:
- Bearing intersection = estimated position
- Accuracy improves with separation angle
- Best accuracy: 60-90° angle between ships
- Poor accuracy: < 30° or > 150° angle
- Requires communication between ships to compare bearings
```

---

## Electronic Warfare Effects

### Radar Warning Receiver (RWR)

```
RWR_Detection_Range = Enemy_Radar_Range × 1.5

When enemy radar scans you:
- Basic RWR: Alert + approximate bearing
- Advanced RWR: Alert + bearing + radar type identification
```

### Radar Jamming

```
Jammed_Radar_Range = Normal_Range × Jamming_Modifier

Jamming_Modifier = 1 - (Jammer_Power / Radar_Power)

Noise Jammer: 0.5-0.7× range reduction
Deceptive Jammer: False contacts appear
```

### Chaff/Decoys

```
Chaff creates false radar contact for:
- Duration: 30-120 seconds (wind dependent)
- RCS: 1.0-2.0× (ship-equivalent signature)
- Movement: Drifts with wind
```

---

## Worked Examples

### Example 1: Visual Detection - Phase Progression with Misidentification

**Scenario:** Japanese destroyer (Fubuki-class) with Standard bridge searching for US cruiser (Brooklyn-class)

**Equipment:**
- Binocular lookout stations (15 km base)
- Expert lookouts (+1.3× skill)
- Director tower (+1.3× elevation from 20m height)
- Standard bridge (±15° direction, ±1 size variance, clear sprite)

**Conditions:**
- Clear day (1.0×)
- Sea State 3 (0.95×)

**Target:**
- Light cruiser (Size 3 - Medium, 1.1× detection modifier, Normal stealth)

**Base Detection Range Calculation:**
```
Base Range = 15 km × 1.3 (skill) × 1.3 (elevation) × 1.0 (weather) × 0.95 (sea) × 1.1 (size)
Base Range = 26.5 km
```

**Shadow Size Roll (at Phase 2 entry):**
```
Actual Size: 3 (Light Cruiser - Medium)
Standard Bridge Variance: ±1 category
Roll: +0.7 (random within range)
Displayed Shadow Size: 3.7 → Rounds to 4 (Large)
Result: Player sees "Heavy Cruiser-sized" shadow!
```

**Phase Trigger Distances:**
```
Phase 1 (Distant): 26.5 × 1.5 = 39.75 km → Direction indicator appears (±15° arc)
Phase 2 (Emerging): 26.5 × 1.0 = 26.5 km → Shadow emerges (LARGE - misidentified!)
Phase 3 (Visible): 26.5 × 0.7 = 18.5 km → Actual sprite visible, solution builds at 2%/sec
Phase 4 (Full): 26.5 × 0.4 = 10.6 km → Class name + speed category shown
```

**Timeline (target approaching at 20 knots):**
| Distance | Phase | What Player Sees | Reality |
|----------|-------|------------------|---------|
| 40 km | None | Nothing | - |
| 35 km | 1 | Direction indicator (±15° arc) | - |
| 26 km | 2 | **Large oval shadow** (Size 4) | Actually Size 3 |
| 22 km | 2 | Shadow settling toward Size 3.4 | Refinement occurring |
| 18 km | 3 | Brooklyn-class sprite visible - **"Oh, it's a light cruiser!"** | Truth revealed |
| 18 km + 38 sec | 3 | Solution reaches 75% cap | - |
| 10 km | 4 | "Brooklyn-class" label, "Fast" speed | Full info |

**Gameplay Impact:** The Japanese player spent 8km (about 12 minutes at 20 knots) preparing for a heavy cruiser engagement, possibly adjusting tactics. Upon seeing the actual sprite, they realize it's "only" a light cruiser - good news in this case!

---

### Example 2: Radar Detection - Stealth Target

**Scenario:** US destroyer (Fletcher-class) with CIC bridge hunting surfaced submarine at night

**Equipment:**
- SG radar (35 km base range)
- CIC bridge (Advanced: ±8° direction, defined shadow, solution builds 5%/sec)

**Conditions:**
- Night, overcast (radar unaffected)
- Sea State 2 (0.98×)

**Target:**
- Surfaced submarine (0.4× RCS)
- Low Profile stealth (0.7× Phase 2 trigger)

**Base Detection Range:**
```
Base Range = 35 km × 0.98 (sea) × 0.4 (RCS) = 13.7 km
```

**Phase Trigger Distances (with stealth modifier):**
```
Phase 1: 13.7 × 1.5 = 20.6 km → Narrow direction indicator (±8°) + range band
Phase 2: 13.7 × 1.0 × 0.7 (stealth) = 9.6 km → Shadow appears LATE due to low profile
Phase 3: 13.7 × 0.7 = 9.6 km → Sprite visible (same as Phase 2!)
Phase 4: 13.7 × 0.4 = 5.5 km → Full submarine data
```

**Stealth Effect:** The submarine's low profile means Phase 2 and Phase 3 trigger at nearly the same distance - the shadow barely appears before the sprite does. This gives the sub more surprise.

**Solution Timeline:**
- At 9.6 km: Sprite appears, solution starts at 0%
- 19 seconds later: Solution reaches 95% cap (Advanced bridge)
- Fletcher can fire with good accuracy

---

### Example 3: Sonar Hunt - Phase Limitations

**Scenario:** British corvette with Basic bridge hunting U-boat

**Equipment:**
- ASDIC Type 144 (3 km base active range)
- Basic bridge (wide arc, vague shadow, blurry sprite, 50% solution cap)

**Conditions:**
- Own speed: 10 knots (0.85× active)
- Sea State 4 (0.9×)
- No thermal layer

**Target:**
- U-boat at periscope depth (0.1× visual, normal sonar)
- Very Stealthy (0.3× Phase 2 trigger)

**Active Sonar Range:**
```
Base Range = 3 km × 0.85 (speed) × 0.9 (sea) = 2.3 km
```

**Phase Progression:**
```
Phase 1: 2.3 × 1.5 = 3.45 km → Wide direction arc (±30°, randomized!)
Phase 2: 2.3 × 1.0 × 0.3 (stealth) = 0.69 km → Vague shadow appears VERY late
Phase 3: 2.3 × 0.7 = 1.6 km → Blurry submarine sprite
Phase 4: 2.3 × 0.4 = 0.92 km → HP bar visible (but only HP + turrets with Basic!)
```

**The Problem:**
- Basic bridge gives only ±30° direction with randomization
- Very Stealthy submarine's shadow doesn't appear until 690m!
- Basic bridge caps solution at 50% - poor accuracy even with lock
- Corvette must get dangerously close to attack effectively

**Solution:** Upgrade to better bridge, or coordinate with multiple ships to triangulate the wide bearing arcs.

---

### Example 4: Maximum Stealth Ambush

**Scenario:** PT boat with Maximum Stealth lying in wait

**Attacker:** PT-109 (0.5× base size, Maximum Stealth)

**Defender:** Japanese destroyer with Standard bridge, 15km visual base range

**Detection Against PT Boat:**
```
Base Range = 15 km × 0.5 (PT size) = 7.5 km

Phase 1: 7.5 × 1.5 = 11.25 km → Direction indicator
Phase 2: SKIPPED (Maximum Stealth) → No shadow warning!
Phase 3: 7.5 × 0.7 = 5.25 km → PT sprite suddenly appears
Phase 4: 7.5 × 0.4 = 3 km → Full info
```

**Ambush Result:** The destroyer gets a direction indicator at 11km, but the PT boat appears as a sprite at 5.25km with NO shadow warning. By the time the destroyer sees the actual PT boat, torpedoes may already be in the water.

This is how stealth creates tactical surprise.

---

## Balance Notes

### Design Intent

1. **Visual limitations** create value for radar technology
2. **Radar emissions** create counter-play through RWR
3. **Active sonar alert** creates submarine gameplay depth
4. **Weather** creates dynamic gameplay variation
5. **Equipment choices** create meaningful ship customization
6. **Team coordination** rewards communication investment

### Tuning Parameters

These values can be adjusted for game balance:

| Parameter | Current | Range | Effect |
|-----------|---------|-------|--------|
| Night visual penalty | 0.15× | 0.05-0.25 | How blind at night |
| Radar weather penalty | 0.7× heavy rain | 0.5-0.9 | Weather impact on radar |
| Sonar speed penalty | 0.7× at 10kts | 0.5-0.9 | Speed vs detection trade-off |
| Smoke screen visual | 0.1× | 0.05-0.2 | Smoke effectiveness |
| Classification threshold | 1.5× range | 1.2-2.0 | How close for details |

---

## Implementation Notes

### Performance Considerations

```csharp
// Detection checks should be optimized:
// - Only check ships within maximum possible range
// - Use spatial partitioning (quadtree) for range queries
// - Stagger detection updates (not every frame)
// - Cache environmental modifiers (update on weather change)
```

### Update Frequency

| Check Type | Frequency | Notes |
|------------|-----------|-------|
| Visual detection | 1/second | Low CPU cost |
| Radar sweep | Per rotation | Depends on radar type |
| Sonar ping | Per sweep | 3-6 second intervals |
| Classification | On detection | One-time check |
| Fire control | 10/second | High precision needed |

### Data Structures

```yaml
Contact:
  id: unique_identifier
  detection_phase: 1-4
  detection_source: visual|radar|sonar
  bearing: degrees
  range: meters (if known)
  range_band: close|medium|far (if range unknown)
  ship_type: category (if classified)
  ship_class: specific (if identified)
  heading: degrees (if tracked)
  speed: knots (if tracked)
  solution_quality: 0-100%
  last_update: timestamp
  tracking_duration: seconds
```

---

## Cross-References

- [[../Modules/Support/Detection-Radar/_Radar-Mechanics|Radar Mechanics]] - Detailed radar operations
- [[../Modules/Support/Detection-Sonar/_Sonar-Mechanics|Sonar Mechanics]] - Detailed sonar operations
- [[../Modules/Support/Detection-Visual/README|Visual Detection]] - Lookout and rangefinder equipment
- [[../Modules/Support/Communications/README|Communications]] - Sharing detection with allies
- [[../Modules/Support/Electronic-Warfare/README|Electronic Warfare]] - Countering enemy detection
- [[../Modules/Bridge/_Bridge-Modules-Index|Bridge Modules]] - UI features by bridge tier
- [[Gunnery-Mechanics|Gunnery Mechanics]] - Using detection for targeting

---

*This document provides the mathematical foundation for the detection system. Individual equipment modules provide their specific base values, which feed into these formulas.*
