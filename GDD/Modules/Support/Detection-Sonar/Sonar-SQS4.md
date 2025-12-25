---
module_id: SON-012
name: Sonar SQS-4
category: support
subcategory: detection-sonar
sonar_type: active
era: 1955
nation: USA
slot_type: support

# Coverage Mechanics
scan_pattern: scanning
cone_angle: 10           # degrees per beam
sweep_arc: 240           # degrees total (forward + beam)
sweep_time: 3            # seconds per sweep
modes: [passive, active]
default_mode: passive

# Performance
detection_range_active: 8    # km
detection_range_passive: 12  # km (bearing only)
depth_capability: 400        # meters max depth detection
resolution: 40               # meters
bearing_accuracy: 1          # degrees

# Physical
hull_mounted: true
weight: 5200
crew_required: 3
reliability: 92

# Limitations
own_speed_penalty: true
thermal_layer_blocked: true
min_range: 100

tags: [sonar, active, sqs-4, usa, usn, scanning, cold-war, modern]
---

# Sonar SQS-4

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | SQS-4 Scanning Sonar |
| **Nation** | United States |
| **Type** | Active/Passive |
| **Scan Pattern** | Wide-Arc Scanning |
| **Era** | 1955+ |

## Coverage Pattern
```
Pattern:          Wide-Arc Automatic Scanning
Beam Width:       10°
Sweep Arc:        240° (forward + beams)
Sweep Time:       3 seconds per complete sweep
Coverage:         Near-omnidirectional forward
```

```
    \      |      /
     \     |     /
  120°\    |    /120°
       \   |   /
        \  |  /
         \ | /
          [Ship]

   240° Wide Coverage
   Rapid 3-Second Sweep
```

## Detection Performance

### Active Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (modern) | 8km | Excellent range, clear detection |
| Submarine (snorkeling) | 7km | Strong echo |
| Submarine (creeping) | 6km | Good detection even quiet |
| Submarine (stopped) | 4km | Detectable at significant range |
| Submarine (deep) | 8km | Excellent deep capability (400m) |
| Torpedo | 3km | Reliable torpedo detection |
| Mine | 1.5km | Can detect moored mines |

### Passive Mode
| Target | Range | Notes |
|--------|-------|-------|
| Submarine (diesel) | 12km | Bearing only, exceptional sensitivity |
| Submarine (electric) | 6km | Bearing only, excellent quiet detection |
| Nuclear submarine | 15km | Bearing only, very loud machinery |
| Surface ship | 20km | Bearing only, extreme range |

## Speed Penalty
| Own Speed | Detection Modifier |
|-----------|-------------------|
| Stopped | 100% |
| 10 knots | 92% |
| 15 knots | 84% |
| 20 knots | 74% |
| 25 knots | 62% |
| 30+ knots | 48% |

## Operation
### Passive Mode
Advanced hydrophone arrays provide exceptional passive detection range. The SQS-4's passive capability often exceeds active range, making it ideal for initial detection without alerting targets.

### Active Mode - Wide-Arc Rapid Scanning
**REVOLUTIONARY COVERAGE**: The SQS-4 scans a massive 240-degree arc (120° each side of bow), providing near-complete forward and beam coverage. Only the rear 120° arc is unmonitored.

**Advanced Features**:
- **Rapid Sweep**: 3-second full sweep (twice as fast as WWII sonars)
- **Narrow Beam**: 10° beam provides excellent resolution
- **Deep Detection**: Tracks submarines to 400m depth
- **Digital Processing**: Early computer-aided target tracking
- **Multiple Contacts**: Tracks many targets simultaneously

**How It Works**:
1. 240° automatic sweep in 3 seconds
2. 10° pencil beam with powerful transmitter
3. Digital signal processing reduces false contacts
4. Automatic target tracking maintains contact data
5. Displays all contacts with range, bearing, and movement

**Alert Radius**: When you ping, submarines can hear you at 16km (2x your detection range).

### Post-War Technology
The SQS-4 represents the first generation of post-WWII sonar, incorporating transistorized electronics, improved transducers, and early digital processing. These advances dramatically improved performance over wartime systems.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 5,200 kg |
| Crew | 3 operators |
| Reliability | 92% |
| Beam Width | 10° |
| Sweep Arc | 240° |
| Sweep Time | 3 seconds |
| Max Depth | 400m |
| Processing | Analog/Digital hybrid |

## Historical Notes

The SQS-4 entered service in 1955 as the US Navy's first post-WWII scanning sonar system. Designed for Cold War ASW against Soviet submarines, the SQS-4 represented a quantum leap over WWII-era systems. Its 8km active range doubled WWII capabilities, while the 240-degree coverage and 3-second sweep provided unprecedented situational awareness.

The system equipped American destroyers and destroyer escorts through the late 1950s and early 1960s. Its digital processing reduced false contacts from biologics (whales, fish schools), while automatic target tracking allowed operators to monitor multiple submarines simultaneously. The SQS-4's ability to detect submarines at 400m depth countered Soviet deep-diving boats.

The SQS-4's main limitation was that it remained a scanning system rather than truly omnidirectional. The rear 120° arc was unmonitored, allowing clever submarines to approach from astern. This limitation drove development of the omnidirectional SQS-26 in the 1960s.

Despite eventual replacement by more advanced systems, the SQS-4 represented a critical step in sonar evolution, bridging WWII technology and modern omnidirectional systems.

## Tactical Tips
- Massive 240° coverage provides near-complete forward hemisphere
- Only rear 120° arc is unmonitored
- 3-second rapid sweep provides near-real-time tracking
- Exceptional passive range (12km) - use for initial detection
- 8km active range doubles WWII capability
- Can track submarines to extreme depth (400m)
- Digital processing reduces whale/fish false contacts
- Multiple target tracking allows complex engagements
- High reliability (92%) for Cold War operations
- Best combined with ASROC for long-range attack
- Passive mode often exceeds active range
- Speed penalty less severe than WWII sonars
