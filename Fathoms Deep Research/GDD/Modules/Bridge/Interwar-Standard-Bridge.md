---
module_id: BRG-G04
name: Interwar Standard Bridge
category: bridge
subcategory: surface_combatant
era: 1920-1940
slot_type: bridge
weight: 12000
power_draw: 15
crew_required: 10
tags: [bridge, interwar, standard, gyrocompass, rangefinder]
---

# Interwar Standard Bridge

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-G04 |
| **Era** | 1920-1940 |
| **Weight** | 12,000 kg |
| **Power Draw** | 15 kW |
| **Crew Required** | 10 |

## Description

The refined interwar bridge design representing the mature pre-radar era. Features reliable gyrocompass systems, dedicated chart room with plotting table, rangefinder pedestal integration, and improved internal communications. Fully enclosed with good weather protection and visibility. This bridge represents the peak of optical-era command facilities before radar revolutionized naval warfare.

The design emphasizes proper navigation equipment, comfortable working conditions for extended operations, and integration with optical fire control systems. Most cruisers and capital ships built in the 1920s-1930s featured this type of bridge arrangement.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Accurate | Gyrocompass, no magnetic drift |
| Speed Indicator | Accurate | Pit log and engine telegraph |
| Heading Indicator | Accurate | Gyro-stabilized, ±0.5° accuracy |
| Minimap | Disabled | No radar systems yet |
| Contacts Display | Disabled | Visual range only |
| Range Display | Accurate | If Rangefinder module installed |
| Lead Indicator | Disabled | Requires Director Bridge |
| Team Chat | Basic | If Wireless Telegraph installed |
| Detection Warning | Disabled | No electronic sensors |
| Navigation Plot | Manual | Chart table, parallel rules |

## Fog of War

- **Base Visibility**: Visual range (excellent optics, 15+ km clear day)
- **Max Contacts Tracked**: 10 (dedicated plotting table with trained plotters)
- **Link Capability**: Wireless telegraph (text messages, some delay)
- **Information Quality**: Good position fixes, accurate course tracking
- **Night Operations**: Searchlight dependent, limited capability

## Compatibility

### Supported Detection Modules
- All optical rangefinders
- Stereoscopic rangefinders
- Lookout stations
- Searchlights
- Optical directors

### Supported Communications
- Signal flags
- Signal lamps
- Wireless telegraph
- Voice tubes (internal)
- Ship's telephone system

### Supported Fire Control
- Optical fire control directors
- Mechanical fire control computers
- Manual plotting solutions
- Centralized fire control

### NOT Compatible
- Radar systems (technology not available)
- Digital systems
- Voice radio (early models, not standard)

## Special Features

### Dedicated Chart Room
- Large plotting table
- Parallel rules and dividers
- Multiple chart storage
- Navigation calculations space
- Weather protected chart work

### Rangefinder Integration
- Pedestals for rangefinder operators
- Direct voice pipe to plotting
- Stereoscopic rangefinders supported
- Range data transmitted to fire control

### Improved Communications
- Voice tube network throughout ship
- Engine telegraph system
- Rudder angle indicator
- Revolution counter
- Interior telephone system

### Weather Protection
- Fully enclosed wheelhouse
- Heated interior
- Clear view ports (glass)
- Bridge wings for docking
- Emergency steering position

## Stats

```
Command Efficiency: 85%
Weather Vulnerability: Very Low (fully enclosed, heated)
Night Operations: Moderate (searchlight dependent)
Damage Resistance: Medium (structural steel, some splinter protection)
Navigation Accuracy: High (gyrocompass, accurate plotting)
Fire Control Integration: Good (optical systems)
Crew Comfort: Good (enclosed, heated, proper facilities)
```

## Historical Notes

The interwar period saw bridge designs mature into highly functional command centers. Ships like HMS Hood, USS Pennsylvania (post-1920s refit), and the French Dunkerque-class featured sophisticated bridges with gyrocompass systems, proper chart rooms, and excellent visibility.

These bridges represented the culmination of optical-era design. Captains had accurate navigation data, could integrate rangefinder information effectively, and operate in most weather conditions. The lack of radar meant tactics still depended heavily on visual sighting and searchlights at night.

The Washington Naval Treaty era (1922-1936) saw standardization of bridge equipment across navies. Gyrocompasses became universal, fire control systems more sophisticated, and internal communications improved dramatically from WWI standards.

Many ships built with these bridges received radar retrofits in the late 1930s or during WWII, creating awkward arrangements as the new technology was grafted onto optical-era designs.

## Suitable Ships

### Primary Users
- Light cruisers (6,000-10,000 tons)
- Heavy cruisers (treaty cruisers)
- Large destroyers (flotilla leaders)
- Battleships (smaller/older)
- Armed merchant cruisers

### Era Appropriate
- Treaty cruisers (County, Pensacola, Myoko classes)
- Interwar destroyers (large fleet destroyers)
- Modernized WWI battleships
- New construction battleships (as base bridge)

### Not Recommended
- Small destroyers (use Destroyer Bridge)
- Escorts (too heavy, too much crew)
- Carriers (need specialized island)
- Submarines (wrong type entirely)

## Prerequisites

### Technology Required
- Gyrocompass technology (1920+)
- Electrical power generation (15+ kW)
- Optical fire control systems
- Internal telephone system

### Infrastructure
- Machine shop capability
- Electrical installation
- Optical instrument calibration

### Crew Training
- Navigation school graduates
- Quartermaster training
- Fire control training
- Communications specialization

## Upgrade Options

### Equipment Additions
Can be enhanced with:
- Surface search radar (1940+) → [[Director-Bridge]]
- Fire control radar (1941+)
- Voice radio systems (TBS, 1943+)
- Improved fire control computers
- IFF transponder (1943+)

### Bridge Upgrades
- → [[Director-Bridge]] (adds fire control director integration)
- → [[Combat-Information-Center]] (major modernization, 1943+)
- Add [[Flagship-Bridge]] facilities (if flagship role)

### Downgrade From
- ← [[Enclosed-Bridge]] (earlier, simpler design)
- ← [[Open-Bridge]] (much earlier)

## Operational Considerations

### Advantages
- Excellent navigation accuracy
- Good working conditions
- Weather independent operations
- Solid crew comfort
- Reliable equipment
- Good visibility

### Limitations
- No radar capability
- Visual range only
- Searchlight dependent at night
- No automated fire control
- Manual plotting only
- Limited night effectiveness

### Tactical Impact
Ships with this bridge fight as the interwar navies planned: visual range gun duels with optical fire control. Night combat requires searchlights, creating mutual detection. Successful captains maximize visibility advantages and use superior navigation to gain position.

## Maintenance Requirements

```
Gyrocompass: Calibration every 180 days
Optical Equipment: Clean daily, calibrate weekly
Chart Table: Chart updates per Notice to Mariners
Voice Tubes: Inspect monthly
Windscreens: Polish daily, replace as needed
Electrical Systems: Test weekly
Interior Heating: Seasonal check
```

## Damage Effects

### Light Damage (1-25% HP)
- Broken windscreens
- Voice tube disruption
- Minor electrical faults
- Chart table disorder

### Moderate Damage (26-50% HP)
- Gyrocompass damaged (revert to magnetic)
- Major windscreen loss
- Telephone system failure
- Rangefinder mount damage

### Heavy Damage (51-75% HP)
- Structure compromise
- Flooding in chart room
- Total electrical failure
- Navigation equipment destroyed

### Critical Damage (76-100% HP)
- Bridge uninhabitable
- Must conn from emergency position
- All bridge equipment lost

---

## Cross-References

- [[Enclosed-Bridge]] - Predecessor design
- [[Director-Bridge]] - Next evolution (fire control integration)
- [[Combat-Information-Center]] - Future upgrade (radar era)
- [[Heavy-Cruiser-Bridge]] - Specialized cruiser variant
- [[Flagship-Bridge]] - Flagship enhancement option

---

*Part of the Generic Era Bridges series (BRG-G01 through BRG-G09)*
