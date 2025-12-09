# Communications Modules

Communications systems enable coordination between ships, aircraft, and shore stations. From visual flag signals to satellite data links, these modules represent the evolution of naval command and control over 130+ years of naval warfare.

## Module Overview

| Module ID | Name | Era | Type | Range | Key Feature |
|-----------|------|-----|------|-------|-------------|
| COM-001 | Signal Flags | All | Visual | 5 km | Universal, daylight only |
| COM-002 | Signal Lamp | 1890+ | Visual | 15 km | Night capable, Morse |
| COM-003 | Flag Semaphore | 1890+ | Visual | 3 km | Fastest visual method |
| COM-004 | Wireless HF | 1910+ | Radio | 500+ km | First over-horizon radio |
| COM-005 | Wireless VLF | 1920+ | Radio | 2000+ km | Submarine communication |
| COM-006 | Radio TBS | 1942+ | Voice | 20 km | First voice radio (USA) |
| COM-007 | Radio VHF | 1950+ | Voice | 50 km | Post-war multi-channel |
| COM-008 | Radio UHF | 1960+ | Voice | 30 km | Secure encrypted tactical |
| COM-009 | SATCOM | 1970+ | Satellite | Global | Worldwide communications |
| COM-010 | Link 11 | 1960+ | Data | 300 km | First tactical data link |
| COM-011 | Link 16 | 1990+ | Data | 300 km | Modern secure data link |
| COM-012 | IFF Transponder | 1940+ | ID | 400 km | Friend or Foe identification |

## Vision Sharing Capability

**Vision sharing** allows allied ships to see each other's radar contacts, creating a combined tactical picture. This revolutionized naval warfare.

### Systems That Enable Vision Sharing:
- **Voice Radio (COM-006, COM-007, COM-008)**: Real-time contact sharing via voice
- **Satellite Communications (COM-009)**: Global vision sharing
- **Tactical Data Links (COM-010, COM-011)**: Automated sensor fusion

### Systems That DO NOT Share Vision:
- **Visual Signals (COM-001, COM-002, COM-003)**: Manual text messages only
- **Wireless Telegraph (COM-004, COM-005)**: Text-based reports only
- **IFF Transponder (COM-012)**: Identification data only

## Communication Types

### Visual Signaling (1890+)
Visual systems require line of sight and are limited by weather and visibility.

**[[Signal-Flags]] (COM-001)**
- Range: 5 km
- Speed: Slow (15-30 sec per signal)
- Era: All eras (universal standard)
- Notes: Daylight only, cannot be jammed, no power required
- Use Case: Basic coordination, ceremonial, radio silence operations

**[[Signal-Lamp]] (COM-002)**
- Range: 15 km
- Speed: Medium (5-10 sec per message)
- Era: 1890+
- Notes: Night capable, Morse code, point-to-point
- Use Case: Night operations, radio silence, covert communication

**[[Semaphore]] (COM-003)**
- Range: 3 km
- Speed: Fast (3-5 sec per message)
- Era: 1890+
- Notes: Fastest visual method, daylight only, tiring for operator
- Use Case: Quick tactical updates, formation changes, urgent messages

### Wireless Telegraph (1900-1945)
First over-the-horizon communication using Morse code.

**[[Wireless-HF]] (COM-004)**
- Range: 500+ km
- Speed: Slow (5-15 sec delay)
- Era: 1910+
- Notes: Text messages, Morse code, can be intercepted
- Use Case: Long-range coordination, fleet orders, intelligence reports

**[[Wireless-VLF]] (COM-005)**
- Range: 2000+ km
- Speed: Very slow (30-60 sec per message)
- Era: 1920+
- Notes: Penetrates water (submarine communication), global range
- Use Case: Submarine command, strategic orders, shore-to-fleet

### Voice Radio (1930-1970)
Real-time voice communication enabled tactical coordination.

**[[Radio-TBS]] (COM-006)**
- Range: 20 km
- Speed: Instant
- Era: 1942+ (USA)
- **Vision Sharing: YES**
- Notes: VHF voice, clear audio, line of sight only
- Use Case: Task force coordination, first true fleet voice communication

**[[Radio-VHF]] (COM-007)**
- Range: 50 km
- Speed: Instant
- Era: 1950+
- **Vision Sharing: YES**
- Notes: Multiple channels, improved reliability, solid-state electronics
- Use Case: Post-war fleet operations, multi-channel coordination

**[[Radio-UHF]] (COM-008)**
- Range: 30 km
- Speed: Instant
- Era: 1960+
- **Vision Sharing: YES**
- Notes: Encrypted, frequency hopping, anti-jam, secure tactical
- Use Case: Modern secure tactical coordination, special operations

### Modern Communications (1960+)
Satellite and data link systems enable global coordination.

**[[Radio-SATCOM]] (COM-009)**
- Range: Global
- Speed: Fast (slight satellite delay)
- Era: 1970+
- **Vision Sharing: YES**
- Notes: Beyond line of sight, weather affected, satellite dependent
- Use Case: Strategic coordination, multi-theater operations, shore command

### Tactical Data Links (1960+)
Automated digital exchange of tactical information.

**[[DataLink-Link11]] (COM-010)**
- Range: 300 km
- Speed: Slow (12-sec updates)
- Era: 1960+
- **Vision Sharing: YES (Automated)**
- Notes: First tactical data link, automated sensor sharing, HF/UHF
- Use Case: Fleet air defense, coordinated engagements, ASW coordination

**[[DataLink-Link16]] (COM-011)**
- Range: 300 km (LOS), global (via SATCOM)
- Speed: Very fast (sub-second updates)
- Era: 1990+
- **Vision Sharing: YES (Real-time)**
- Notes: Modern standard, 238 kbps, frequency hopping, encrypted
- Use Case: Network-centric warfare, cooperative engagement, comprehensive tactical picture

### Identification Systems (1940+)

**[[IFF-Transponder]] (COM-012)**
- Range: 400 km
- Speed: Instant
- Era: 1940+
- Notes: Automated friend-or-foe identification, prevents fratricide
- Use Case: Combat identification, air defense, beyond-visual-range engagement

## Era Progression

### Pre-WWI (Before 1900)
- Signal Flags only
- Visual range communication only
- Formation coordination primitive

### WWI Era (1900-1920)
- **Wireless Telegraph** revolutionizes naval warfare
- First over-horizon communication
- Battle of Jutland demonstrates radio warfare

### Interwar (1920-1940)
- VLF enables submarine communication
- Visual signals remain important
- Radio discipline develops

### WWII (1940-1945)
- **Voice Radio (TBS)** transforms tactics
- IFF prevents fratricide
- Real-time tactical coordination enabled

### Cold War (1950-1990)
- Multi-channel VHF/UHF radios
- **Link 11** first tactical data link
- Satellite communications deployed
- Encrypted secure communications

### Modern Era (1990+)
- **Link 16** enables network-centric warfare
- Global SATCOM coverage
- Real-time sensor fusion
- Cooperative engagement capability

## Communication Architecture

Modern naval forces use layered communication architecture:

### Local Tactical (0-50 km)
- **VHF/UHF Voice Radio**: Instant voice coordination
- **Link 16**: Real-time tactical data
- **IFF**: Automated identification

### Regional Coordination (50-300 km)
- **Link 11/16**: Tactical data sharing
- **HF Voice**: Over-horizon coordination
- **VHF/UHF Extended**: Via aircraft relay

### Strategic/Global (300+ km)
- **SATCOM**: Worldwide voice and data
- **VLF**: Submarine communication
- **HF Radio**: Long-distance coordination

### Backup Systems
- **Signal Lamp**: Radio silence, jamming
- **Flag Signals**: Universal fallback
- **Semaphore**: Quick urgent messages

## Multiplayer Implications

### Without Communications
- Each ship operates independently
- No coordination possible
- Cannot share sensor data
- High fratricide risk

### With Basic Communications (Flags, Lamps)
- Manual coordination possible
- Slow message exchange
- Visual range only
- Time delays in coordination

### With Voice Radio (TBS, VHF, UHF)
- Real-time voice coordination
- **Vision sharing enabled**
- Allied radar contacts visible
- Fleet operations possible

### With Data Links (Link 11/16)
- **Automated vision sharing**
- Computer-fused tactical picture
- Coordinated engagements
- Network-centric warfare
- Cooperative engagement capability

## Gameplay Considerations

### Era-Appropriate Tactics

**Pre-Radio Era (Before 1910):**
- Ships must stay in visual contact
- Flag signals coordinate maneuvers
- Limited tactical flexibility
- Formation discipline critical

**Radio Era (1910-1940):**
- Over-horizon coordination possible
- Text-based tactical updates
- Delayed information sharing
- Radio discipline important

**Voice Radio Era (1940-1990):**
- Real-time voice coordination
- Vision sharing transforms tactics
- Fleet operates as integrated force
- Electronic warfare becomes critical

**Data Link Era (1990+):**
- Automated sensor fusion
- Perfect situational awareness
- Cooperative engagement
- Information dominance

### Communication Security

**Unsecure Systems (COM-001 to COM-007):**
- Enemy can intercept
- Radio silence necessary for stealth
- Direction finding reveals position
- Code words for added security

**Secure Systems (COM-008, COM-011):**
- Encrypted communications
- Frequency hopping resists jamming
- Enemy cannot understand traffic
- Enables aggressive tactics

### Balance Mechanisms

**Range Limitations:**
- Visual: 3-15 km
- Tactical Radio: 20-50 km
- Data Link: 300 km
- SATCOM: Global

**Update Rates:**
- Visual: 3-30 seconds
- Voice: Instant
- Link 11: 12 seconds
- Link 16: Sub-second

**Vulnerabilities:**
- Visual: Weather, night, line-of-sight
- Radio: Jamming, interception
- SATCOM: Weather, satellite availability
- Data Link: GPS dependency, bandwidth limits

## Technical Notes

### Communication Frequencies

- **VLF**: 3-30 kHz (submarine communication)
- **HF**: 3-30 MHz (over-horizon)
- **VHF**: 30-300 MHz (line-of-sight tactical)
- **UHF**: 300 MHz - 3 GHz (secure tactical)
- **SHF**: 3-30 GHz (SATCOM)

### Data Rates

- Visual Signals: ~2-10 words/minute
- Morse Code: 10-30 words/minute
- Link 11: 1.4-2.25 kbps
- Link 16: 238 kbps
- SATCOM: 1+ Mbps

### Power Requirements

- Visual Signals: 0-2 kW
- Voice Radio: 3-5 kW
- Data Links: 6-8 kW
- SATCOM: 4-6 kW
- VLF Transmitter: 50+ kW

## Related Systems

### Bridge Modules
Communications integrate with bridge systems:
- **Open Bridge**: Visual signals only
- **Enclosed Bridge**: Radio capable
- **Director Bridge**: Voice radio integration
- **CIC Bridge**: Data link integration
- **Modern Bridge**: Full network integration

### Sensor Integration
Communications share sensor data:
- **Radar**: Tracks shared via data link
- **Sonar**: Contact reports via voice/data
- **ESM**: Emissions data shared
- **Visual**: Contact reports via any method

### Weapons Integration
Communications enable coordinated fires:
- **IFF**: Prevents fratricide
- **Data Link**: Target assignment
- **Voice**: Fire control coordination
- **CEC**: Cooperative engagement

## Historical Evolution Summary

**1890s**: Visual signals only (flags, lamps)
**1900s**: Wireless telegraph enables over-horizon coordination
**1920s**: VLF enables submarine communication
**1940s**: Voice radio and IFF transform tactical warfare
**1960s**: Encrypted UHF and Link 11 tactical data link
**1970s**: SATCOM provides global reach
**1990s**: Link 16 enables network-centric warfare
**2000s+**: Comprehensive sensor fusion and cooperative engagement

Each era's communication capabilities fundamentally shaped naval tactics and strategy. Ships without era-appropriate communications cannot compete effectively.

## Additional Files

The Communications directory also contains:
- **Encrypted-Comms.md**: Encryption systems for secure communications
- **Satellite-Comms.md**: Additional SATCOM documentation
- **Voice-Radio-HF.md**: HF voice radio systems

(Note: Some files may represent alternative implementations or historical variants not part of the main COM-001 to COM-012 series)

---

## Quick Reference Table

| Need | Recommended System | Module ID |
|------|-------------------|-----------|
| Basic coordination (any era) | Signal Flags | COM-001 |
| Night operations (pre-radio) | Signal Lamp | COM-002 |
| Quick urgent messages | Semaphore | COM-003 |
| Long-range coordination (WWI) | Wireless HF | COM-004 |
| Submarine communication | Wireless VLF | COM-005 |
| WWII fleet operations | Radio TBS | COM-006 |
| Post-war multi-channel | Radio VHF | COM-007 |
| Secure tactical (modern) | Radio UHF | COM-008 |
| Global coordination | SATCOM | COM-009 |
| Automated data sharing (early) | Link 11 | COM-010 |
| Network-centric warfare | Link 16 | COM-011 |
| Prevent fratricide | IFF Transponder | COM-012 |

## Vision Sharing Quick Reference

Systems that enable real-time allied sensor sharing:
- COM-006: Radio TBS (20 km, voice)
- COM-007: Radio VHF (50 km, voice)
- COM-008: Radio UHF (30 km, secure voice)
- COM-009: SATCOM (global, voice + data)
- COM-010: Link 11 (300 km, automated data)
- COM-011: Link 16 (300 km, real-time data)

These systems fundamentally change gameplay by enabling true fleet operations with shared tactical awareness.
