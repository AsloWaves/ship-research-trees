---
module_id: RAD-013
name: AN/SPS-49 Air Search Radar
category: support
subcategory: detection-radar
function: air_search
era: 1975
nation: USA
slot_type: support

# Coverage Mechanics
scan_type: rotating
cone_angle: 360          # degrees (360 for full rotation)
rotation_speed: 2        # seconds per full rotation
sector_options: [90, 120, 180, 270]
modes: [auto, manual, sector, track-while-scan]
default_mode: auto

# Performance
detection_range: 250     # km (for aircraft)
accuracy: 98             # % bearing accuracy
resolution: 200          # meters (distinguish close contacts)
update_rate: 2           # seconds between detections
height_finding: true     # can determine altitude

# Physical
weight: 18000
crew_required: 1
reliability: 94

# Limitations
min_range: 500           # meters
weather_penalty: 5       # % range loss
sea_clutter: very_low

tags: [radar, air_search, usa, modern, 1970s, long_range]
---

# AN/SPS-49 Air Search Radar

## Overview
| Attribute | Value |
|-----------|-------|
| **Designation** | AN/SPS-49(V) |
| **Nation** | United States |
| **Era** | 1975+ |
| **Function** | Long-Range Air Search |
| **Scan Type** | Rotating 360° |

## Coverage Pattern
```
Scan Type:        Rotating 360° (very fast)
Cone Angle:       360° (full coverage)
Rotation Speed:   2 seconds per sweep
Coverage:         Complete hemispheric air coverage to 250+ km
Update Rate:      Aircraft position updates every 2 seconds
Height Finding:   YES - determines altitude automatically
```

**Visual Pattern:**
```
        N
        |
   NW   |   NE          250 km detection range
     \  |  /
      \ | /               Detects aircraft at extreme range
W -----+-----E          Fast rotation provides near-real-time tracking
      / | \             Altitude determination included
     /  |  \
   SW   |   SE
        |
        S

Sweep: ========> (2 seconds for full rotation)
Track-While-Scan: Continuously tracks multiple targets
```

## Detection Performance
| Target Type | Range | Notes |
|-------------|-------|-------|
| Heavy Bomber (high) | 250 km | Maximum detection range |
| Fighter (high) | 220 km | Excellent long-range detection |
| Fighter (low) | 180 km | Even low-altitude targets visible |
| Cruise Missile (high) | 150 km | Anti-shipping missile warning |
| Cruise Missile (low) | 80 km | Sea-skimmer detection |
| Helicopter | 120 km | Rotorcraft clearly visible |
| Stealth Aircraft | 100 km | Reduced but still detectable |
| Battleship (surface) | 40 km | Incidental surface detection |

## Operation Modes
### Auto Mode
Radar rotates continuously at 2-second intervals, automatically detecting and tracking all air contacts within 250 km. Computer processing distinguishes aircraft from clutter, assigns track numbers, and maintains continuous plots. Minimal operator intervention required.

### Manual Mode
Operator can adjust scan parameters, focus on specific contacts, or designate priority tracks. The sophisticated computer system allows manual refinement of automatic tracking. Rarely needed for routine operations.

### Sector Mode
Restricts scan to selected arc (90°, 120°, 180°, or 270°). Update rate improves to sub-second intervals in focused sector. Used when defending against known threat axis or when coordinating with other radar platforms.

### Track-While-Scan (TWS)
The SPS-49's most advanced feature: continuously tracks dozens of targets simultaneously while maintaining search pattern. Each target receives automatic track number, altitude, speed, and heading. CIC displays show comprehensive air picture without operator input.

## Specifications
| Spec | Value |
|------|-------|
| Weight | 18,000 kg |
| Crew Required | 1 (computer-assisted) |
| Reliability | 94% |
| Frequency | L-band (1-2 GHz) |
| Antenna Type | Large planar array |
| Display | Multiple CIC consoles |
| ECCM | Advanced jamming resistance |

## Advantages
- Exceptional range (250 km) provides 15-20 minutes warning
- Very fast 2-second rotation enables near-real-time tracking
- Height-finding capability determines altitude automatically
- Track-While-Scan tracks dozens of targets simultaneously
- Outstanding accuracy (98%) for engagement coordination
- Advanced computer processing filters clutter automatically
- Very high reliability (94%) - consistently operational
- Excellent ECCM (Electronic Counter-Counter Measures) resistance
- Can detect stealth aircraft (reduced range)
- Integrates with NTDS/Link systems for data sharing
- Single operator due to automation
- Low weather penalty (5%)

## Disadvantages
- Very heavy (18,000 kg) - requires substantial mounting structure
- Extremely high power consumption (280 kW)
- Large radar cross-section visible from long distances
- Expensive and complex system
- Requires computer systems integration
- Limited surface search capability (not optimized for ships)
- Modern era only - not available for WWII/Korea scenarios
- Vulnerable to anti-radiation missiles if emitting

## Historical Notes

The AN/SPS-49 entered US Navy service in 1975 as a replacement for earlier SPS-37 and SPS-43 long-range air search radars. It became the standard air search radar for aircraft carriers, cruisers, destroyers, and amphibious ships throughout the late Cold War and beyond.

During the 1980s, SPS-49 equipped ships formed the outer air defense ring for carrier battle groups. The radar's 250 km range allowed detection of Soviet Tu-22M Backfire bombers and AS-4 Kitchen anti-ship missiles while still far from the task force, providing time to launch interceptors and prepare missile defenses.

In the Persian Gulf (1987-1988) during Operation Earnest Will, SPS-49-equipped ships provided air surveillance protecting reflagged Kuwaiti tankers. The radar's ability to track both aircraft and helicopters in a cluttered littoral environment proved its value in non-traditional warfare scenarios.

During Desert Storm (1991), SPS-49 radars provided comprehensive air picture management, tracking hundreds of friendly aircraft sorties while monitoring for Iraqi air threats. The integration with Link systems meant all coalition ships shared a common air picture.

SPS-49 continued in service through the 1990s-2010s, eventually being supplemented and replaced by more modern phased-array radars like SPY-1. However, many ships retained SPS-49 as a backup or supplementary air search capability even after SPY installation.

The system underwent multiple upgrades (SPS-49A, SPS-49V, etc.) improving reliability, ECCM, and computer processing. The final variants remained in service until the 2020s on some amphibious and auxiliary vessels.

## Tactical Tips
- **Early Warning**: SPS-49's 250 km range provides exceptional warning time. Use every minute to coordinate defenses, launch CAP, and prepare missile systems.
- **Track-While-Scan**: Let the computer do the work. TWS mode tracks 50+ targets automatically. Focus on threat assessment, not manual plotting.
- **CAP Direction**: Vector fighters using precise bearing/range/altitude data. The 98% accuracy enables fighter controllers to provide exact intercepts.
- **Missile Defense**: Detect incoming anti-ship missiles at 80-150 km depending on altitude. This warning is critical for Phalanx and missile systems to engage.
- **Stealth Warning**: Even stealth aircraft appear on SPS-49 at reduced ranges. A "clean" scope doesn't mean no threats - watch for gaps in coverage.
- **Link Integration**: Share SPS-49 data across the battle group via Link. Your detections become everyone's detections - cooperative engagement.
- **EMCON Considerations**: SPS-49's powerful emissions are detectable at extreme ranges. When operating under EMCON (Emissions Control), consider shutting down and relying on passive systems or other ships' data.
- **Sector Focus**: When defending against known threat bearing (e.g., land-based bombers from specific direction), use sector mode for sub-second updates.
- **Weather Advantage**: The minimal 5% weather penalty means SPS-49 works effectively even in severe storms. Use weather to mask approach while maintaining detection.
- **Surface Contacts**: While not optimized for surface search, SPS-49 detects large ships at 40 km. Use it as backup to surface search radars.
- **Helicopter Threats**: The 120 km helicopter detection range is crucial for ASW and anti-ship helicopter defense. Many threats arrive by rotorcraft.
- **Altitude Exploitation**: Height-finding data allows assessment of threat type. High-altitude = bombers, medium = fighters, low = cruise missiles.
- **Reliability Trust**: At 94% reliability, SPS-49 is among the most dependable systems. Build doctrine assuming it will be operational.
- **Computer Maintenance**: The automation requires functional computers. Ensure CDS (Combat Direction System) is operational to exploit SPS-49's capabilities.
