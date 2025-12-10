---
module_id: RAD-004
name: FuMO 25 Surface Search Radar
category: support
subcategory: detection-radar
function: surface_search
era: 1942
nation: Germany
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360          # degrees (360 for full rotation)
rotation_speed: 10       # seconds per full rotation
sector_options: [90, 120, 180]
modes: [auto, manual, sector]
default_mode: auto

# Performance
detection_range: 22      # km
accuracy: 82             # % bearing accuracy
resolution: 500          # meters (distinguish close contacts)
update_rate: 10          # seconds between detections
height_finding: false

# Physical
weight: 4600
crew_required: 2
reliability: 72

# Limitations
min_range: 600           # meters
weather_penalty: 15      # % range loss
sea_clutter: moderate

tags: [radar, surface_search, germany, wwii, 1942, kriegsmarine]
---

# FuMO 25 Surface Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | FuMO 25 (Funkmessortung) |
| **Nation** | Kriegsmarine (Germany) |
| **Era** | 1942+ |
| **Function** | Surface Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360°
Cone Angle:       360° (full coverage)
Rotation Speed:   10 seconds per sweep
Coverage:         Complete all-around coverage
Update Rate:      Contact position updates every 10 seconds
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE
     \  |  /
      \ | /
W -----+-----E  (Antenna rotates continuously)
      / | \
     /  |  \
   SW   |   SE
        |
        S

Sweep: ----> (10 seconds for full rotation)
Slower rotation = longer gaps between updates
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Battleship | 22 km | Solid detection at maximum range |
| Cruiser | 20 km | Reliable tracking |
| Destroyer | 17 km | Good against smaller vessels |
| Submarine (surfaced) | 12 km | Adequate for surface U-boats |
| MTB/PT Boat | 8 km | Small craft detectable |
| Periscope | 3 km | Difficult, calm seas only |

## Operation Modes
### Auto Mode
Antenna rotates continuously at 10-second intervals. The slow rotation means contacts update less frequently than Allied equivalents, creating opportunities for fast-moving targets to close between sweeps. Best for general patrol and convoy escort.

### Manual Mode
Operator can pause or slow rotation to study specific contacts. The FuMO 25's display requires more interpretation than Allied PPI scopes, so manual mode often used when multiple contacts appear in the same general bearing.

### Sector Mode
Restricts antenna sweep to a selected arc (90°, 120°, or 180°). Update rate improves to 4-5 seconds in focused sector. Recommended when threat axis is known, such as defending against torpedo boat attacks from a specific direction.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 4,600 kg |
| Crew Required | 2 |
| Reliability | 72% |
| Frequency | 9.5 cm (S-band) |
| Antenna Type | Rotating dipole array |
| Display | A-scope and plan display |

## Advantages
- Full 360° rotating coverage
- Adequate range for surface engagements (22 km)
- Moderate weight suitable for destroyers and larger
- Reasonable power consumption
- Can guide fire control radars to targets
- Works in Arctic and Baltic conditions
- Better than having no radar at all

## Disadvantages
- Slow 10-second rotation makes it lag behind Allied sets
- Lower reliability (72%) than American SG or British Type 271
- Display technology inferior to Allied PPI scopes
- Moderate range inferior to US SG (35 km)
- Resolution struggles with close formations
- Production limited by Kriegsmarine priorities
- Relatively large minimum range (600m)
- Operator interpretation required for accurate ranging

## Historical Notes

The FuMO 25 (Funkmessortungsgerät 25) represented Germany's mid-war effort to equip surface ships with effective radar. While German naval radar development lagged behind the Allies, the FuMO 25 provided Kriegsmarine vessels with at least some nighttime and poor-weather detection capability.

Introduced in 1942, the FuMO 25 equipped destroyers, torpedo boats, and some auxiliary vessels. Larger ships like cruisers and battleships received the more powerful FuMO 26/27 sets. The system saw action in the Arctic convoys, the Channel, and the Baltic.

During Operation Cerberus (the "Channel Dash" of February 1942), Scharnhorst and Gneisenau's FuMO radars detected British coastal forces, contributing to the squadron's successful breakout. In Arctic convoy battles, FuMO-equipped destroyers provided early warning of approaching Allied escorts, though often too late for German commanders to exploit.

The slow 10-second rotation proved problematic against British MTBs and MGBs operating in the Channel. Fast coastal forces could close 300-400 meters between sweeps, often getting inside torpedo range before German crews could effectively engage. This led to doctrinal emphasis on combining radar with searchlights and star shells.

Production was hampered by Allied bombing of electronics factories and competition for resources with U-boat priorities. By 1944, many surviving surface vessels had degraded or non-functional FuMO sets due to lack of spare parts and trained technicians.

## Tactical Tips
- **Compensate for Slow Rotation**: The 10-second update cycle is the FuMO 25's biggest weakness. When contacts appear, assume they've moved 300-500m closer than displayed if they're fast vessels.
- **Arctic Advantage**: FuMO 25 performs well in extreme cold where optical lookouts struggle. In Arctic convoy actions, trust your radar over freezing, exhausted lookouts.
- **Channel Defense**: When defending against British MTBs, use sector mode focused on likely approach vectors. The 4-5 second update rate is crucial against fast attackers.
- **Baltic Operations**: In confined Baltic waters, the moderate range is actually adequate. Use the radar to navigate through islands and sandbanks at night.
- **Fire Control Cueing**: The FuMO 25's primary value is finding targets for your fire control radars. Once you detect a contact, immediately cue your FuMO 27 or optical directors.
- **Multiple Contacts**: When several returns appear on the display, switch to manual mode and study the situation for 20-30 seconds before making tactical decisions.
- **Combine with Passive Detection**: Use hydrophones or RWR (if available) to supplement radar. If you hear propellers or detect enemy radar but see nothing on FuMO 25, check your blind spots.
- **Weather Operations**: FuMO 25's moderate sea clutter performance means it works acceptably in North Sea/Baltic conditions. Don't expect miracles in heavy seas, but it's usable.
- **Raid Commerce**: For armed merchant raiders operating in open ocean, FuMO 25 provides detection range advantage over unequipped Allied freighters. Use it to detect targets beyond horizon.
