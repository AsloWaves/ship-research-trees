---
module_id: COM-010
name: Tactical Data Link 11
category: support
subcategory: communications
era: 1960+
nation: USA/NATO
slot_type: support
weight: 400
power_draw: 8
crew_required: 2

# Performance
range: 300                     # km (HF mode)
data_rate: slow                # 1364/2250 bps
reliability: 85                # percentage
security: medium

# Capabilities
voice_capable: false
text_capable: false
data_capable: true             # automated sharing
vision_sharing: true           # shares fog of war automatically

# Requirements
line_of_sight: false           # uses HF radio
weather_affected: true         # atmospheric conditions affect HF
crew_required: 2

tags: [communications, datalink, link11, automated, tactical]
---

# Tactical Data Link 11

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-010 |
| **Era** | 1960+ |
| **Range** | 300 km |
| **Type** | Tactical Data Link (Automated) |

## Description

Link 11 is the first standardized tactical data link system, enabling automated exchange of tactical information between ships, aircraft, and shore stations. Unlike voice radio requiring human operators to verbally report contacts, Link 11 automatically transmits and receives digitized radar tracks, IFF data, and tactical information. Ships equipped with Link 11 share a common tactical picture - all participants see the same radar contacts, tracks, and threat assessments.

Developed in the 1960s and operational by the early 1970s, Link 11 uses HF or UHF radio to transmit data in a time-division multiple access format. Each participant gets assigned time slots to transmit tracks, and the system automatically correlates tracks from multiple sensors into a single unified picture. This creates true "network-centric" warfare decades before the term existed.

## Effect on Multiplayer

**This module enables:**
- Automated tactical picture sharing with allies
- Vision sharing: **Yes** - ALL allied radar contacts appear automatically
- Voice chat: No - Data only (pair with voice radio)
- Text messages: No - Automated data only
- Automatic track correlation
- IFF data sharing
- Threat assessment sharing
- No human operator needed (automated)

**Revolutionary Capability:**

Link 11 fundamentally changes naval warfare:

**Without Link 11:**
- Each ship sees only own radar contacts
- Manual voice reports required
- Time delays in sharing information
- Human error in reporting
- Difficult to maintain common picture

**With Link 11:**
- Automatic sharing of all tracks
- Real-time tactical picture for all participants
- Computer correlation removes duplicates
- IFF automatically shared
- Everyone sees same picture

**Automated Operation:**
Link 11 is "set and forget" - once configured, it automatically transmits your tracks and receives allied tracks. No human intervention needed. Operators monitor but don't manually input data.

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full range (300 km HF, 300 km UHF-LOS) |
| Rain/Fog | No effect on UHF, slight effect on HF |
| Night | Improved HF range (ionosphere) |
| Enemy jamming | Can be jammed (requires counter-measures) |
| Atmospheric storms | HF mode affected |
| Beyond horizon | HF mode works, UHF requires relay |

## Data Transmission

**Link 11 Transmits:**
- Radar tracks (position, course, speed, altitude)
- IFF data (friend/foe/unknown identification)
- Electronic warfare data (jamming sources, radar emissions)
- Weapons status (missiles fired, targets engaged)
- Platform status (damage, fuel, weapons remaining)
- Tactical commands (from command ship)

**Update Rate:**
- HF mode: Every 12 seconds per track (slow)
- UHF mode: Every 6 seconds per track (faster)
- High-interest tracks: Priority updates
- Low-interest tracks: Lower update rate

**Data Rate:**
- 1364 bps (bits per second) or 2250 bps
- Very slow by modern standards
- Sufficient for tactical tracks (not video or high-res data)

## Network Organization

**Net Control Station (NCS):**
- One ship designated as net control
- Coordinates time slots for participants
- Maintains network discipline
- Typically flagship or Aegis cruiser

**Participating Units (PU):**
- All other ships in network
- Assigned time slots by NCS
- Transmit tracks during assigned slots
- Receive all network data

**Rolling Reference Point:**
- Common navigation reference
- Ensures track correlation accuracy
- Updated periodically

## Tactical Use

1. **Air Defense**: Shared air picture for coordinated CAP/AAW
2. **Surface Warfare**: Common surface picture for coordinated engagements
3. **ASW**: Share submarine contacts and prosecution
4. **Missile Defense**: Coordinated fleet air defense
5. **Strike Coordination**: Shared targeting for strikes
6. **Force Protection**: Early warning shared across force
7. **Search and Rescue**: Coordinate SAR efforts

## Advantages

**First Automated Tactical Data:**
- No voice reporting needed (automated)
- Real-time tactical picture
- Consistent data format (computer processed)
- Track correlation (removes duplicates)
- Beyond line of sight (HF mode)
- NATO standard (allied interoperability)

**Tactical Benefits:**
- Everyone sees same picture
- Faster decision making
- Coordinated engagements
- Reduced fratricide risk
- Better situational awareness
- Computer-aided threat assessment

## Limitations

- Slow data rate (1364/2250 bps)
- 12-second update cycle (HF mode)
- Limited to tactical tracks (no voice/video)
- Complex to configure (network setup required)
- Requires dedicated operators (2 crew)
- Can be jammed (vulnerable to ECM)
- HF mode subject to atmospheric conditions
- Heavy equipment (400 kg)
- High power requirement (8 kW)

## Historical Notes

Link 11 development began in the late 1950s as NATO sought to standardize tactical data exchange. The system became operational in the early 1970s, first aboard US Navy carriers and Aegis cruisers, then expanded to NATO allies.

The system proved its worth during Cold War operations. Carrier battle groups using Link 11 could maintain comprehensive air pictures across hundreds of miles. Each ship's radar contributed to the common picture, and fighter aircraft received target vectors from the ship with best track.

Gulf War (1991) saw extensive Link 11 use. Coalition naval forces shared tactical data, enabling coordinated Tomahawk strikes and air defense. The common tactical picture allowed ships to coordinate beyond visual range.

Link 11's main limitation - slow data rate - became apparent in modern high-intensity warfare. Tracking hundreds of contacts with 12-second updates stressed the system. This drove development of Link 16 (1990s) with much higher data rates. However, Link 11 remained in service as it works beyond line of sight (using HF), while Link 16 is primarily line-of-sight.

## Technical Details

**Transmission Modes:**
- HF mode: 3-30 MHz, beyond horizon, 300+ km range
- UHF mode: 300+ MHz, line of sight, 200+ km range

**Time Division Multiple Access:**
- Network time divided into frames (12-24 seconds)
- Each frame divided into time slots
- Each participant assigned specific slots
- Precise timing synchronization required

**Message Formats:**
- J-series messages (standardized NATO)
- J3.2: Initial track report
- J3.3: Precise position report
- J3.5: IFF/SIF report
- J3.7: Electronic warfare report
- J12: Command and control messages

## Comparison to Other Systems

**vs Voice Radio:**
- Automated (no voice reporting needed)
- Standardized data format
- Computer processed (consistent)
- Slower than urgent voice report
- Cannot convey nuance/context
- Better for sustained operations

**vs Link 16:**
- Much slower (1-2 kbps vs 238 kbps)
- Beyond horizon capable (Link 16 mostly LOS)
- Older technology (1960s vs 1990s)
- Lower data accuracy
- Less jam resistant
- Still widely deployed

**vs Manual Plotting:**
- Infinitely faster
- More accurate
- Automated correlation
- Real-time updates
- Requires equipment (manual is backup)

## Upgrade Path

- [[DataLink-Link16]] - Modern high-speed data link (1990+)
- [[Radio-SATCOM]] - Can carry Link 11 data beyond horizon
- [[IFF-Transponder]] - Enhanced when integrated with Link 11

## Compatible With

- CIC Bridge (required for full utilization)
- Modern Bridge (full integration)
- Aegis Combat System (designed for Link 11)
- SPY-1 Radar (feeds tracks to Link 11)
- Modern fire control systems (receive Link 11 tracks)
- Voice radio systems (complementary)
- IFF systems (share IFF data via Link 11)

## Network Management

**Establishing Link 11 Net:**

1. **Net Configuration**: NCS assigns participating units
2. **Time Synchronization**: All units sync precision clocks
3. **Slot Assignment**: Each unit assigned transmit slots
4. **Reference Point**: Establish common navigation reference
5. **Net Entry**: Units join net in sequence
6. **Monitor**: Operators watch data quality and network health

**Maintaining Net Quality:**
- Monitor signal strength
- Watch for timing errors
- Identify and remove bad data
- Adjust power levels as needed
- Coordinate frequency changes
- Restart net if corrupted

## Game Balance Notes

Link 11 represents the transition from manual coordination to automated networking. It provides major tactical advantage by automatically sharing the complete tactical picture. All allied players with Link 11 see combined sensor coverage without manual reporting.

**Gameplay Impact:**

Link 11 enables:
- Automatic vision sharing (all allied radar contacts)
- Track correlation (computer removes duplicates)
- IFF sharing (friend/foe data automatic)
- Coordinated engagements (all see same targets)

The 12-second update rate creates interesting gameplay. Tracks update every 12 seconds (in HF mode), so fast-moving targets may appear slightly delayed. This is authentic to real Link 11 and creates tactical consideration - modern threats move significantly in 12 seconds.

The beyond-horizon capability (HF mode) distinguishes Link 11 from later Link 16, which is primarily line-of-sight. Link 11 ships can coordinate across the map (300+ km), while Link 16 requires closer proximity or SATCOM relay.

**Balance Mechanisms:**

1. **Update Delay**: 12-second updates (not instant)
2. **Jamming Vulnerable**: Can be jammed by ECM
3. **Network Setup**: Requires time to establish net
4. **Limited Bandwidth**: Can become saturated in high-target environment
5. **Equipment Weight**: 400 kg, 8 kW - significant burden

**Era Distinction:**
- 1960s-1980s: Link 11 provides decisive advantage
- 1990s+: Link 16 superior for high-intensity warfare
- Link 11 remains useful for beyond-horizon coordination

The automated nature means players don't manually report contacts - the computer does it. This simulates the revolution in naval warfare when computers took over data sharing. Players focus on tactical decisions rather than information management.
