---
module_id: COM-009
name: SATCOM (Satellite Communications)
category: support
subcategory: communications
era: 1970+
nation: USA/NATO
slot_type: support
weight: 250
crew_required: 1

# Performance
range: global                  # unlimited range
data_rate: fast
reliability: 92                # percentage (satellite dependent)
security: high

# Capabilities
voice_capable: true
text_capable: true
data_capable: true             # automated sharing
vision_sharing: true           # shares fog of war

# Requirements
line_of_sight: false           # satellite relay
weather_affected: true         # heavy weather can degrade
crew_required: 1

tags: [communications, satellite, global, secure, modern]
---

# SATCOM (Satellite Communications)

## Overview
| Attribute | Value |
|-----------|-------|
| **Module ID** | COM-009 |
| **Era** | 1970+ |
| **Range** | Global |
| **Type** | Satellite Communications |

## Description

Satellite Communications (SATCOM) provides beyond-line-of-sight voice, data, and text communication via military communications satellites. Using microwave frequencies (typically UHF or SHF), SATCOM enables ships to communicate globally without relying on atmospheric propagation or line of sight. A ship in the Indian Ocean can coordinate in real-time with headquarters in Washington or task forces in the Mediterranean.

SATCOM revolutionized naval operations by enabling true global command and control. Modern naval SATCOM uses multiple satellite constellations (DSCS, UFO, WGS) providing redundant, secure, high-bandwidth connections. The system supports voice, data, video, and email, enabling comprehensive information sharing across vast distances.

## Effect on Multiplayer

**This module enables:**
- Global voice communication with allied players (any range)
- Vision sharing: **Yes** - Allied radar contacts appear globally
- Voice chat: **Yes** - Secure global voice
- Text messages: **Yes** - Email and text messaging
- Data sharing: **Yes** - Automated tactical data exchange
- Strategic coordination across map
- Shore command integration
- Video conferencing (1990+)

**Global Coordination:**

SATCOM enables capabilities impossible with radio:
- Coordinate across entire map
- Contact shore command/headquarters
- Multi-theater operations
- Strategic planning in real-time
- Intelligence distribution
- Weather updates from global sources
- Navigation updates (GPS augmentation)

**Beyond Line of Sight:**
Ships over the horizon can coordinate as if adjacent. Carrier groups in different oceans share intelligence. Shore commands direct global operations in real-time.

## Performance

| Condition | Effect |
|-----------|--------|
| Clear weather | Full capability (global range) |
| Rain/Heavy clouds | Degraded signal (10-20% loss) |
| Storm | Significant degradation (50% loss) |
| Night | No effect (24/7 operation) |
| Enemy jamming | Difficult but possible (uplink vulnerable) |
| Satellite availability | Critical - depends on constellation health |

## Satellite Systems

| Era | System | Coverage | Bandwidth |
|-----|--------|----------|-----------|
| 1970s | Fleet SATCOM | Regional | Low (voice + low-rate data) |
| 1980s | DSCS | Global | Medium (voice + moderate data) |
| 1990s | UFO | Global | High (voice + high-rate data) |
| 2000s | WGS | Global | Very High (video + massive data) |

Modern ships use multiple SATCOM systems for redundancy.

## Communication Capabilities

**Voice:**
- Secure voice channels
- Conference calling
- Priority override for emergencies
- Crystal clear quality (no atmospheric noise)

**Data:**
- Tactical data exchange (Link 16 over SATCOM)
- Email and messaging
- File transfer
- Intelligence reports
- Weather data
- Navigation updates

**Video (1990+):**
- Video conferencing
- UAV video feeds
- Reconnaissance imagery
- Battle damage assessment

## Tactical Use

1. **Strategic Coordination**: Multi-theater operations
2. **Intelligence Distribution**: Real-time intel sharing
3. **Command and Control**: Shore-to-ship direction
4. **Coalition Operations**: Coordinate allied forces globally
5. **Logistics**: Supply coordination across oceans
6. **Emergency Communication**: When all else fails
7. **Submarine Communication**: Surface submarines can use SATCOM
8. **Special Operations**: Covert ops coordination

## Advantages

**Revolutionary Capabilities:**
- Global range (unlimited practical range)
- Beyond line of sight
- High bandwidth (can carry data/video)
- Reliable (no atmospheric propagation issues)
- Secure (encrypted links)
- Multiple channels
- 24/7 availability

**Strategic Benefits:**
- Coordinate forces worldwide
- Real-time intelligence sharing
- Shore command integration
- Weather/navigation data
- Coalition coordination
- Rapid response to crises

## Limitations

- Requires satellites (vulnerable to ASAT weapons)
- Weather affects signal (heavy rain/storm)
- Latency (slight delay from satellite relay, ~250ms)
- Satellite capacity limited (bandwidth sharing)
- Expensive (high cost per bandwidth)
- Visible uplink (antenna radiates, can be detected)
- Jamming possible (uplink vulnerable)
- Nuclear EMP could destroy satellites

## Historical Notes

Naval SATCOM began in the 1960s with experimental systems, becoming operational in the 1970s with Fleet SATCOM. Early systems provided limited voice and low-rate data, but revolutionized naval operations by enabling global coordination.

The Falklands War (1982) demonstrated SATCOM's value. British task force 8,000 miles from UK maintained real-time communication with London, coordinating strategy, receiving intelligence, and maintaining secure command. Without SATCOM, the UK could not have conducted modern joint operations at such distance.

Gulf War (1991) saw massive SATCOM use. Coalition naval forces coordinated Tomahawk strikes, shared radar pictures via Link 16 over SATCOM, and maintained continuous communication with command authorities. The bandwidth demand exceeded available satellite capacity, highlighting the need for improved systems.

Modern SATCOM (WGS constellation, 2000s+) provides enormous bandwidth. Ships can transmit full-motion video, massive data files, and maintain continuous tactical data links. A destroyer can share its entire radar picture with headquarters, receive UAV feeds, and participate in video conferences simultaneously.

## Vulnerabilities

**Anti-Satellite Warfare:**
- Satellites vulnerable to kinetic kill vehicles
- Electronic jamming of satellites possible
- Cyber attacks on satellite control systems
- Nuclear EMP destroys electronics in orbit

**Electronic Warfare:**
- Uplink jamming (enemy jams your transmission to satellite)
- Downlink jamming (jams satellite transmission to you)
- Meaconing (false satellite signals)

**Environmental:**
- Heavy rain attenuates signal
- Solar storms disrupt electronics
- Space debris could damage satellites

**Operational Security:**
- Uplink radiates energy (detectable)
- Direction-finding possible
- Transmission reveals ship presence

## Comparison to Other Systems

**vs VHF/UHF Radio:**
- Global range (vs 30-50 km)
- Beyond line of sight
- Higher bandwidth
- Slight latency (satellite relay)
- Weather affected (rain)
- Satellite dependent

**vs HF Radio:**
- More reliable (no ionosphere dependency)
- Higher bandwidth (can carry video)
- Secure by design
- Global coverage more consistent
- Satellite dependent (HF independent)

**vs Subsurface Systems:**
- Requires surface antenna (submarine must surface)
- Cannot penetrate water (VLF can)
- Much higher bandwidth when available

## Modern Integration

**Network-Centric Warfare:**

SATCOM enables network-centric operations:
- Real-time tactical picture sharing
- Distributed sensor fusion
- Coordinated fires across domains
- Intelligence-driven operations
- Rapid decision cycles

**Combined Arms:**
- Navy coordinates with Air Force (global link)
- Joint targeting via SATCOM data
- Shore bombardment coordinated with ground forces
- Special operations integration

## Upgrade Path

- [[DataLink-Link16]] - Often uses SATCOM as bearer for beyond-LOS
- [[Encrypted-Comms]] - Enhanced encryption for classified communications
- Commercial SATCOM - Augment military satellites with commercial capacity

## Compatible With

- CIC Bridge (full integration)
- Modern Bridge (full integration)
- Aegis Combat System (integrated)
- All modern sensors (data sharing)
- Data Link systems (uses SATCOM for beyond-LOS)
- IFF systems (coordinate identification)
- GPS (navigation integration)

## Multiple SATCOM Systems

**Redundancy:**

Modern ships carry multiple SATCOM terminals:
- Primary: WGS (Wideband Global SATCOM)
- Secondary: UFO (Ultra High Frequency Follow-On)
- Tertiary: Commercial SATCOM (Inmarsat, etc.)
- Emergency: Portable SATCOM units

If primary fails (jamming, satellite loss, weather), secondary systems provide backup.

## Game Balance Notes

SATCOM represents the pinnacle of communications technology - global, secure, high-bandwidth. It enables strategic-level coordination and networked warfare. Ships with SATCOM can share sensor data globally, coordinate with forces anywhere, and receive strategic intelligence in real-time.

The global range means SATCOM-equipped ships can coordinate regardless of map position. A carrier group in one corner and a submarine in another can share tactical data as if co-located. This enables powerful combined operations but requires balancing limitations:

**Balance Mechanisms:**

1. **Weather Degradation**: Heavy weather reduces capability, forcing reliance on backup systems
2. **Satellite Capacity**: Limited bandwidth prevents unlimited use
3. **Latency**: 250ms delay prevents some real-time applications
4. **Vulnerability**: ASAT weapons can destroy satellites (major strategic event)
5. **Detection**: Uplink radiation reveals ship presence to ESM
6. **Jamming**: Uplink/downlink vulnerable to powerful jamming

**Gameplay Impact:**

Players with SATCOM gain major advantages:
- Coordinate without range limits
- Share intelligence globally
- Receive orders from shore command (AI or player)
- Access global weather/intelligence data

Players without SATCOM are limited to local coordination (VHF/UHF range). This creates clear era distinction: WWII ships fight with local coordination, modern ships with global networking.

The satellite dependency creates interesting strategic warfare. Destroying enemy satellites (ASAT weapons) degrades their C4I significantly. Protecting your satellites becomes strategic priority. This adds a space warfare dimension to naval combat.

Nuclear war would destroy most satellites (EMP), forcing fallback to HF radio and creating "post-SATCOM" scenario where modern ships must operate with 1960s-level communications. This creates interesting "what if" scenarios for gameplay.
