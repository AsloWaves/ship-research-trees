---
module_id: BRG-T09
name: Light Carrier Island
category: bridge
subcategory: carrier
era: 1940-1965
slot_type: bridge
weight: 15000
crew_required: 20
tags: [bridge, carrier, CVL, CVE, island, flight-operations, compact]
---

# Light Carrier Island

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-T09 |
| **Era** | 1940-1965 |
| **Weight** | 15,000 kg |
| **Crew Required** | 20 |

## Description

A compact carrier island designed for light carriers (CVL) and escort carriers (CVE). Provides essential flight control, navigation, and ship control in a smaller package than fleet carrier islands. Emphasizes economy and simplicity while maintaining core flight operations capability. The reduced size allows smaller carriers to operate effectively without the weight and crew penalty of full-size carrier islands.

This bridge represents the minimum viable carrier command structure: Primary Flight Control (Pri-Fly), basic navigation bridge, minimal flag facilities, and flight deck direction capability. Everything non-essential is omitted to save weight and topside space.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Accurate | Gyrocompass standard |
| Speed Indicator | Accurate | Critical for flight ops |
| Heading Indicator | Accurate | Wind-over-deck calculations |
| Minimap | Radar | If installed (standard 1943+) |
| Contacts Display | Good | Aircraft tracking priority |
| Range Display | Basic | Simple rangefinder |
| Lead Indicator | If Available | AA fire control |
| Team Chat | Voice Radio | Essential for CAP coordination |
| Detection Warning | If Available | IFF standard 1943+ |
| **Flight Operations** | **Essential** | Primary function |
| **Aircraft Status** | **Yes** | Ready/spotted/airborne display |
| **Deck Status** | **Yes** | Spotting, landing clear, barriers |

## Fog of War

- **Base Visibility**: Good (elevated island position)
- **Max Contacts Tracked**: 15 (emphasis on air contacts)
- **Link Capability**: Full radio - CAP coordination essential
- **Information Quality**: Good - air operations focus
- **Night Operations**: Good with radar, difficult without
- **Aircraft Control**: Can control 6-12 aircraft (CVE: 18-28, CVL: 30-45)
- **Fleet Coordination**: Basic - not designed for task force command

## Compatibility

### Supported Detection Modules
- Air search radar (essential, 1942+)
- Surface search radar (standard, 1942+)
- Height-finding radar (desirable, 1943+)
- IFF interrogator (standard, 1943+)
- Optical rangefinders (basic)

### Supported Communications
- TBS voice radio (essential)
- Fighter direction radio (essential)
- Aircraft radio nets (essential)
- Fleet tactical radio
- Air-to-ship communications
- Emergency frequencies

### Supported Flight Operations
- Flight deck crew coordination
- Catapult control (if fitted)
- Arresting gear status
- Deck barriers
- Aircraft spotting displays
- Hangar deck coordination
- Aviation fuel management indicators

### Supported Weapons Systems
- Light AA batteries (5-inch/38, 40mm, 20mm)
- AA fire control directors (basic)
- No heavy guns (not needed on carriers)

## Special Features

### Primary Flight Control (Pri-Fly)
- Flight deck control position
- Landing signals officer (LSO) coordination
- Aircraft launch/recovery control
- Deck spotting status
- Barrier and arresting gear control
- Crash crew coordination
- FOD (Foreign Object Debris) watch

### Compact Design
- Minimal island footprint
- Reduced weight vs fleet carrier island
- Smaller crew requirement
- Essential functions only
- More flight deck space available
- Simplified construction

### Fighter Direction Capability
- Basic CAP (Combat Air Patrol) control
- Air contact vectoring
- Simple intercept control
- Not as sophisticated as fleet carrier CIC
- Adequate for CVE/CVL air groups

### Ship Control Integration
- Navigation bridge integrated
- Engine control
- Damage control coordination
- Reduced to essentials
- Flight ops take priority over all else

## Stats

```
Command Efficiency: 75% (adequate for light carrier)
Weather Vulnerability: Low (enclosed)
Night Operations: Radar-dependent, challenging
Damage Resistance: Low (lightweight, critical structure)
Navigation Accuracy: Excellent (precise wind/speed needed)
Flight Operations Capability: Good (essential ops only)
Fleet Carrier Operations: No (limited air group)
Fighter Direction: Basic (adequate for CVE/CVL)
AA Coordination: Good (self-defense priority)
Economy: Good (vs fleet carrier island)
```

## Historical Notes

Light carrier islands evolved from two different needs:

**Light Carriers (CVL)**: Converted cruiser hulls (USS Independence-class) needed carrier capabilities on a cruiser-size hull. The island was compact but sophisticated, including full flight control, navigation, and AA coordination. Nine CVLs served in the fast carrier task forces, operating 30-45 aircraft each.

**Escort Carriers (CVE)**: Built on merchant hulls or purpose-built, CVEs were the minimum viable carrier. The island was tiny - sometimes just a small deckhouse with Pri-Fly and minimal navigation bridge. CVE missions varied:
- ASW patrol (Atlantic)
- Convoy escort
- Amphibious support
- Aircraft ferry
- Training carrier

### CVL Examples

**USS Independence (CVL-22)** and sisters:
- Converted Cleveland-class cruiser hull
- Compact island, starboard side
- Full flight operations capability
- SK air search radar
- 30-45 aircraft
- Fast carrier task force operations

**HMS Colossus** (British light carrier):
- Purpose-built CVL
- Larger than Independence-class
- Better habitability
- Post-war service into 1960s
- Some served in other navies to 1990s

### CVE Examples

**USS Bogue (CVE-9)** class:
- Diesel-electric merchant conversion
- Very small island
- 24-28 aircraft
- Atlantic ASW patrols
- Simple but effective

**USS Casablanca (CVE-55)** class:
- Purpose-built escort carrier
- Smallest viable carrier island
- 27-28 aircraft
- Mass-produced (50 built)
- Supported Pacific landings

**"Jeep Carriers"** (nickname for CVEs):
The tiny CVE islands became legendary. Officers joked you could see the entire ship from Pri-Fly. The compact design meant cramped conditions, but CVEs proved effective at many missions. At Samar (1944), CVEs with their minimal islands and small air groups helped defeat a Japanese battleship force.

### Island Damage Examples

**USS Ommaney Bay (CVE-79)**: Kamikaze hit island, January 1945. Fire spread rapidly, ship abandoned and scuttled. Demonstrated vulnerability of carrier islands - they contain critical command and control functions.

**USS Franklin (CV-13)**: While a fleet carrier, Franklin's island was heavily damaged by bombs in March 1945. Ship survived but demonstrated importance of island survivability.

## Suitable Ships

### Primary Users
- Light Carriers (CVL): Converted cruiser or purpose-built
- Escort Carriers (CVE): Converted merchant or purpose-built
- Training Carriers
- Aircraft Transports (with flight operations)

### Specific Examples

**United States**
- Independence-class CVL (9 ships)
- Casablanca-class CVE (50 ships)
- Bogue-class CVE (45 ships, many to UK)
- Sangamon-class CVE (4 ships, converted oilers)
- Commencement Bay-class CVE (19 ships, most advanced)

**United Kingdom**
- Colossus-class CVL (10 ships)
- Attacker/Ruler-class CVE (Lend-Lease)
- Nairana/Vindex-class CVE

**Japan**
- Zuiho-class CVL
- Ryujo (small carrier)
- Chitose-class CVL (converted seaplane carriers)

### Not Suitable
- Fleet carriers (need full Carrier-Island-WWII or Modern)
- Battleships/cruisers (wrong type)
- Amphibious carriers (specialized island needed)

## Prerequisites

### Technology Required
- Gyrocompass (accurate wind calculation)
- Air search radar (1942+ essential)
- Radio communications (multiple nets)
- Flight deck control systems
- Catapult controls (if fitted)
- Arresting gear controls

### Infrastructure
- Carrier construction experience
- Flight deck systems
- Aircraft handling equipment
- Multiple radio installations
- Radar installation

### Crew Training
- Naval aviators (air boss, LSO)
- Navigation specialists
- Radar operators
- Fighter direction officers
- Flight deck crew coordination
- Damage control (special emphasis)

## Upgrade Options

### Equipment Additions
Can be enhanced with:
- Improved radar systems (SPS series, 1950s+)
- Better fighter direction equipment
- IFF improvements
- Additional radio nets
- CIC space (limited)
- Improved AA fire control

### Modernization Paths
- Jet aircraft operations → Strengthened deck, steam catapults
- Angled deck conversion → Major flight ops improvement
- Mirror landing system → Better recovery rates
- Modern electronics → [[Carrier-Island-Modern]] (major upgrade)

### Cold War Upgrades
Many CVLs/CVEs served into 1950s-1960s with upgrades:
- Jet capability (limited)
- Improved radar
- Better communications
- Helicopter operations (CVE specialty)

## Operational Considerations

### Advantages
- Economical vs fleet carrier
- Adequate for CVE/CVL air groups
- Lighter weight
- Lower crew requirement
- Simpler construction
- Mass-production capable (CVE)
- Proven effective design

### Limitations
- Cannot handle large air groups
- Limited fighter direction
- No fleet command capability
- Minimal redundancy
- Vulnerable to damage
- Cramped working conditions
- Limited CIC capability

### Tactical Impact
CVLs with this island served in fast carrier task forces alongside fleet carriers. They provided additional aircraft, especially fighters, without requiring another fleet carrier's resources. CVEs served as ASW hunters, convoy escorts, and amphibious support, their small islands adequate for these missions.

### Mission Profiles

**CVL - Fast Carrier Operations**
- Fighter cover
- Scout bombing
- Torpedo attacks
- CAP for task force
- Strike missions
- Integrated with CV operations

**CVE - ASW Patrol (Atlantic)**
- Hunter-killer groups
- Convoy escort
- Submarine hunting
- TBM Avenger operations
- Prolonged patrol

**CVE - Amphibious Support (Pacific)**
- Close air support
- CAP over beaches
- Observation aircraft
- Medical evacuation
- Replacement aircraft ferry

**CVE - Training**
- Carrier qualification
- LSO training
- Flight deck crew training
- Safer than using fleet carriers

## Maintenance Requirements

```
Gyrocompass: Calibration every 90 days
Flight Deck Equipment: Daily inspection
Radar Systems: Daily checks, weekly maintenance
Radio Equipment: Daily checks, multiple nets
Catapults (if fitted): Daily inspection
Arresting Gear: After every recovery, daily inspection
Barriers: Daily testing
Wind/Speed Indicators: Continuous accuracy critical
```

## Damage Effects

### Light Damage (1-25% HP)
- Equipment damage
- Some radio/radar casualties
- Flight ops may continue with reduced efficiency
- Repair possible at sea

### Moderate Damage (26-50% HP)
- Significant island structure damage
- Radar possibly destroyed
- Flight control compromised
- May need to suspend flight ops
- Heavy casualties possible

### Heavy Damage (51-75% HP)
- Island heavily damaged
- Flight operations impossible
- Navigation from emergency position
- Heavy casualties
- Major repair needed

### Critical Damage (76-100% HP)
- Island destroyed or collapsed
- Flight operations impossible
- Ship control from emergency position
- Catastrophic casualties
- Possible mission kill even if ship survives

### Fire Risk
Carrier islands are especially vulnerable to:
- Kamikaze hits (common target)
- Bomb hits (island stands out)
- Aviation fuel fires spreading from deck
- Ammunition explosions in island structure

## Real-World Examples

### USS Princeton (CVL-23)
- Independence-class light carrier
- Bomb hit October 1944, Leyte Gulf
- Fire spread throughout ship
- Magazine explosion destroyed stern
- Abandoned and sunk
- Demonstrated CVL vulnerability

### USS St. Lo (CVE-63)
- Casablanca-class escort carrier
- First ship sunk by kamikaze (October 1944, Leyte Gulf)
- Hit on flight deck, bomb penetrated to hangar
- Catastrophic explosion
- Sank in 30 minutes
- CVE fragility demonstrated

### USS White Plains (CVE-66)
- Casablanca-class escort carrier
- Battle off Samar (October 1944)
- Survived despite being targeted by Japanese battleships
- Small island made poor target
- Effective AA fire coordination
- CVE toughness demonstrated

### HMS Vindex (D15)
- British escort carrier
- Atlantic ASW operations
- Effective submarine hunter
- Small island proved adequate for mission
- Survived war

---

## Cross-References

- [[Carrier-Island-WWII]] - Fleet carrier island (larger)
- [[Carrier-Island-Modern]] - Modern carrier island
- [[Combat-Information-Center]] - CIC integration
- [[Light-Cruiser-Bridge]] - Similar size class, different role
- Flight deck modules
- Aviation fuel modules

---

*Part of the Ship-Type Specialized Bridges series - Carrier variant*
