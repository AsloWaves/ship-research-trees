---
module_id: BRG-017
name: Amphibious Command Bridge
category: bridge
subcategory: amphibious
era: 1942-present
slot_type: bridge
weight: 60000
power_draw: 200
crew_required: 60
tags: [bridge, amphibious, command, landing, marines]
---

# Amphibious Command Bridge

## Overview

| Attribute | Value |
|-----------|-------|
| **Module ID** | BRG-017 |
| **Era** | 1942-Present |
| **Weight** | 60,000 kg |
| **Power Draw** | 200 kW |
| **Crew Required** | 60 |

## Description

Specialized command facility for amphibious operations, integrating naval command with ground force coordination. Features extensive communications for ship-to-shore control, beach status monitoring, landing craft management, and close air support coordination.

## UI Features Enabled

| Feature | Status | Notes |
|---------|--------|-------|
| Compass Display | Accurate | Standard |
| Speed Indicator | Accurate | Standard |
| Heading Indicator | Accurate | Standard |
| Minimap | Enhanced | Beach overlay |
| Contacts Display | Full | Air/surface/ground |
| Beach Status | Yes | Landing progress |
| Landing Craft Track | Yes | All boats tracked |
| Team Chat | Multi-net | Naval + ground |
| Air Support | Yes | CAS coordination |
| Fire Support | Yes | NGFS control |

## Fog of War

- **Naval Visibility**: Standard radar coverage
- **Beach Visibility**: Shore fire control parties
- **Air Coordination**: CAP and CAS integration

## Special Features

### Joint Operations Center
Coordinates:
- Naval gunfire support
- Close air support
- Landing craft waves
- Beach logistics

### Shore Fire Control
- Links with SFCP (Shore Fire Control Party)
- Targets for naval guns
- Danger close coordination
- Fire mission management

### Landing Craft Control
- Wave scheduling
- Beach assignment
- Retraction timing
- Casualty evacuation

### Air Support Integration
- CAS request processing
- CAP coordination
- Helicopter control
- Medevac management

## Operational Displays

| Display | Function |
|---------|----------|
| Beach Status Board | Landing progress |
| Landing Craft Plot | All boats tracked |
| Fire Support Plot | Active missions |
| Air Status Board | Aircraft allocation |
| Communication Net | Multi-channel status |

## Communication Nets

| Net | Purpose |
|-----|---------|
| Ship-Shore | Ground forces |
| Fire Support | NGFS coordination |
| Air Control | CAS/CAP |
| Logistics | Supply flow |
| Medical | Casualty evacuation |
| Command | Senior officers |

## Landing Phase Support

### Pre-Landing
- Naval gunfire prep
- Air strikes
- UDT coordination
- Wave marshaling

### Assault Phase
- Wave timing control
- Fire support shifts
- Beach status monitoring
- Reserve commitment

### Build-up Phase
- Logistics flow
- Beach expansion
- Fire support on-call
- Perimeter coordination

## Damage Resistance

```
Priority Target: High value
Protection: Moderate
Redundancy: Multiple stations
Backup: Can transfer to alternate
```

## Historical Development

| Era | Capability |
|-----|------------|
| 1942-1944 | Basic radio coordination |
| 1944-1945 | Integrated command ships |
| 1945-1960 | Helicopter integration |
| 1960-1980 | Computer-assisted |
| 1980-present | Digital integration |

## Historical Notes

Amphibious command evolved from ad-hoc arrangements at Guadalcanal to purpose-built AGC command ships by 1944. At Iwo Jima and Okinawa, command ships like USS Eldorado coordinated thousands of landing craft, hundreds of aircraft, and dozens of fire support ships. Modern amphibious command ships like USS Blue Ridge can coordinate joint operations involving all services across a theater of operations.

## Suitable Ships

- Amphibious command ships (AGC/LCC)
- Amphibious assault ships (LHA/LHD)
- Large amphibious transport docks (LPD)

## Prerequisites

Requires:
- [[Combat-Information-Center]] or better
- Multiple communication systems
- Large planning spaces
