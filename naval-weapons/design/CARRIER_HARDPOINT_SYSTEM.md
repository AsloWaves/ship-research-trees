# Aircraft Carrier Hardpoint & Module System

**Document Version**: 1.0
**Date**: October 10, 2025

---

## Overview

Aircraft carriers have **fundamentally different hardpoint systems** compared to battleships. The primary "weapon" is the **flight deck and aircraft complement**, not gun turrets.

---

## Key Differences from Battleships

| Feature | Battleships | Aircraft Carriers |
|---------|-------------|-------------------|
| **Primary Weapon** | Main battery turrets | Embarked aircraft |
| **Offensive Capability** | Gun caliber & number | Aircraft capacity & type |
| **Main Hardpoints** | Turret positions | Flight deck + catapults + elevators |
| **Secondary Battery** | 5"/38 DP guns | 5"/38 DP guns (similar) |
| **Unique Systems** | Heavy armor belt | Flight deck, hangar deck, aviation fuel |
| **Critical Modules** | FCS directors | Catapults, arresting gear, elevators |

---

## Carrier-Specific Hardpoint Categories

### 1. Flight Operations Hardpoints

**Flight Deck**
- **Flight_Deck_Length_FT**: Usable flight deck length
- **Flight_Deck_Width_FT**: Maximum flight deck width
- **Flight_Deck_Area_SQFT**: Total flight deck area
- **Flight_Deck_Armor_IN**: Armored deck thickness (0 for unarmored)

**Catapults**
- **Hardpoint_Catapult_Type**: "Hydraulic-H", "Steam-C11", "Steam-C13", "EMALS", "None"
- **Hardpoint_Catapult_Count**: Number of catapult positions (0-4)
- **Hardpoint_Catapult_Layout**: "2 Bow / 2 Waist", "2 Bow", "None"

**Arresting Gear**
- **Hardpoint_Arresting_Wire_Count**: Number of arresting wires (typically 3-4)
- **Hardpoint_Arresting_Gear_Type**: "Mk 7", "Advanced Recovery System"

**Aircraft Elevators**
- **Hardpoint_Elevator_Count**: Number of aircraft elevators (1-4)
- **Hardpoint_Elevator_Capacity_LBS**: Weight capacity per elevator
- **Hardpoint_Elevator_Layout**: "2 Deck-Edge + 1 Centerline", "3 Centerline"

**Hangar Deck**
- **Hangar_Deck_Length_FT**: Hangar length
- **Hangar_Deck_Width_FT**: Hangar width
- **Hangar_Deck_Height_FT**: Hangar clearance height
- **Hangar_Capacity_Aircraft**: Maximum aircraft in hangar

### 2. Defensive Armament Hardpoints

**Carriers have NO main battery** (except Lexington-class with 8" guns)

**Secondary Battery** (surface defense)
- **Hardpoint_Secondary_Battery**: "8× Twin-5in/38 DP Mounts"
- **Hardpoint_Secondary_Count**: Number of 5"/38 or similar mounts
- **Hardpoint_Secondary_Size**: "DP-5in", "Twin-5in"

**Anti-Aircraft Battery**
- **Hardpoint_AA_Light**: "40mm Quad Bofors Positions"
- **Hardpoint_AA_Light_Count**: Number of 40mm positions
- **Hardpoint_AA_Close**: "20mm Oerlikon Positions"
- **Hardpoint_AA_Close_Count**: Number of 20mm positions

**Modern Missiles** (1980s+ refits)
- **Hardpoint_Missile_VLS**: "Mk 29 Sea Sparrow Launchers"
- **Hardpoint_Missile_VLS_Cells**: Number of Sea Sparrow cells
- **Hardpoint_CIWS**: "Phalanx CIWS Positions"
- **Hardpoint_CIWS_Count**: Number of Phalanx mounts

### 3. Aviation Support Modules

**Fuel & Ordnance**
- **Aviation_Fuel_Capacity_TONS**: Aviation fuel (AVGAS, JP-5)
- **Ordnance_Capacity_TONS**: Bombs, missiles, torpedoes for aircraft
- **Magazine_Capacity_AA_TONS**: Ship's AA gun ammunition
- **Magazine_Capacity_Total_TONS**: Total ordnance

**Aircraft Capacity**
- **Aircraft_Capacity_Normal**: Normal operational complement
- **Aircraft_Capacity_Maximum**: Maximum surge capacity
- **Aircraft_Capacity_Deck_Park**: Aircraft parkable on deck
- **Aircraft_Capacity_Hangar**: Aircraft storable in hangar

### 4. Carrier-Specific Module Slots

**Flight Operations Modules**
- **Module_Slot_Catapults**: Number of catapult positions (0-4)
- **Module_Slot_Arresting_Gear**: Number of arresting gear sets (1-2)
- **Module_Slot_Elevators**: Number of elevator positions (1-4)
- **Module_Slot_Optical_Landing_System**: Fresnel lens, IFLOLS positions

**Radar & Sensors**
- **Module_Slot_Air_Search_Radar**: Long-range air search (SK, SPS-49, etc.)
- **Module_Slot_Surface_Search_Radar**: Surface search radar
- **Module_Slot_Fire_Control_Radar**: Gun fire control (Mk 37, etc.)
- **Module_Slot_TACAN**: Tactical air navigation beacon

**Propulsion** (same as battleships)
- **Module_Slot_Engine_Boilers**: Boiler positions (oil-fired carriers)
- **Module_Slot_Engine_Turbines**: Turbine positions
- **Module_Slot_Engine_Reactors**: Reactor positions (nuclear carriers)

---

## Hardpoint Examples by Carrier Class

### USS Langley (CV-1) - 1922 Experimental
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 534
- Flight_Deck_Width_FT: 64
- Hardpoint_Catapult_Type: "None" (no catapults initially)
- Hardpoint_Catapult_Count: 0
- Hardpoint_Elevator_Count: 1 (single centerline elevator)
- Hangar_Capacity_Aircraft: 36
- Aircraft_Capacity_Normal: 36

DEFENSIVE ARMAMENT:
- Hardpoint_Secondary_Battery: "4× Single-5in/51"
- Hardpoint_Secondary_Count: 4
- No AA beyond rifles initially

MODULE SLOTS:
- Module_Slot_Catapults: 0
- Module_Slot_Elevators: 1
- Module_Slot_Engine_Boilers: 6 (coal-fired initially)
- Module_Slot_Engine_Turbines: 2

NOTES: Experimental platform, slow (15 kts), converted collier
```

### USS Lexington (CV-2) - 1927 Converted Battlecruiser
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 866
- Flight_Deck_Width_FT: 105
- Hardpoint_Catapult_Type: "Hydraulic-H" (1930s refit)
- Hardpoint_Catapult_Count: 2
- Hardpoint_Elevator_Count: 2
- Hangar_Capacity_Aircraft: 90
- Aircraft_Capacity_Normal: 90

DEFENSIVE ARMAMENT (UNIQUE FOR CARRIERS):
- Hardpoint_Main_Battery: "4× Twin-8in/55 Turrets" ⭐ UNIQUE!
- Hardpoint_Main_Count: 4
- Hardpoint_Main_Size: "Light-8in"
- Hardpoint_Secondary_Battery: "12× Single-5in/25 AA"
- Hardpoint_Secondary_Count: 12

MODULE SLOTS:
- Module_Slot_Catapults: 2
- Module_Slot_Elevators: 2
- Module_Slot_Engine_Boilers: 16 (turbo-electric drive)
- Module_Slot_Engine_Turbines: 4

NOTES: Massive size, 33 kts, can fight surface ships with 8" guns
```

### USS Yorktown (CV-5) - 1937 Fleet Carrier
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 809
- Flight_Deck_Width_FT: 86
- Hardpoint_Catapult_Type: "Hydraulic-H"
- Hardpoint_Catapult_Count: 2
- Hardpoint_Elevator_Count: 3
- Hangar_Capacity_Aircraft: 90
- Aircraft_Capacity_Normal: 90

DEFENSIVE ARMAMENT:
- Hardpoint_Secondary_Battery: "8× Single-5in/38 DP"
- Hardpoint_Secondary_Count: 8
- Hardpoint_AA_Light: "16× 1.1in Quad Mounts" (early AA)
- Hardpoint_AA_Light_Count: 16

MODULE SLOTS:
- Module_Slot_Catapults: 2
- Module_Slot_Elevators: 3
- Module_Slot_Engine_Boilers: 9
- Module_Slot_Engine_Turbines: 4

NOTES: Perfect WWII fleet carrier design, 32.5 kts
```

### USS Essex (CV-9) - 1942 WWII Workhorse
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 862
- Flight_Deck_Width_FT: 108
- Hardpoint_Catapult_Type: "Hydraulic-H" (H-4-1 model)
- Hardpoint_Catapult_Count: 2
- Hardpoint_Elevator_Count: 3 (2 centerline + 1 deck-edge)
- Hangar_Capacity_Aircraft: 100
- Aircraft_Capacity_Normal: 90-100

DEFENSIVE ARMAMENT (1942 Configuration):
- Hardpoint_Secondary_Battery: "12× Single-5in/38 DP"
- Hardpoint_Secondary_Count: 12
- Hardpoint_AA_Light: "32-40× 40mm Quad Bofors"
- Hardpoint_AA_Light_Count: 40
- Hardpoint_AA_Close: "46-52× 20mm Oerlikon"
- Hardpoint_AA_Close_Count: 52

MODULE SLOTS:
- Module_Slot_Catapults: 2 (upgradeable to steam cats)
- Module_Slot_Elevators: 3
- Module_Slot_Engine_Boilers: 8
- Module_Slot_Engine_Turbines: 4

MODERNIZATION POTENTIAL:
- SCB-27A: Angled deck, steam catapults, new elevators
- SCB-125: Enclosed bow, hurricane bow
```

### USS Essex (CV-9) - SCB-27A/125 Modernization (1951-1955)
```
FLIGHT OPERATIONS (UPGRADED):
- Flight_Deck_Length_FT: 888 (extended bow)
- Flight_Deck_Width_FT: 108 (angled deck: 8° angle)
- Hardpoint_Catapult_Type: "Steam-C11" ⭐ UPGRADED
- Hardpoint_Catapult_Count: 2 (C11 steam catapults)
- Hardpoint_Elevator_Count: 3 (2 deck-edge + 1 centerline)
- Aircraft_Capacity_Normal: 70-80 (larger jets)

DEFENSIVE ARMAMENT (REDUCED):
- Hardpoint_Secondary_Battery: "8× Single-5in/38 DP"
- Hardpoint_Secondary_Count: 8 (reduced from 12)
- Hardpoint_AA_Light: Removed (jet age, no close defense needed)

MODULE SLOTS:
- Module_Slot_Catapults: 2 (steam catapult module installed)
- Module_Slot_Elevators: 3 (upgraded capacity)
- Module_Slot_Radar_Masts: 4 (SPS-8, SPS-12, etc.)

NOTES: Can launch jets, angled deck for safer landings
```

### USS Midway (CV-41) - 1945 Armored Carrier
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 932
- Flight_Deck_Width_FT: 113
- Flight_Deck_Armor_IN: 3.5 ⭐ ARMORED!
- Hardpoint_Catapult_Type: "Hydraulic-H" (later Steam-C11)
- Hardpoint_Catapult_Count: 2
- Hardpoint_Elevator_Count: 3
- Hangar_Capacity_Aircraft: 137 (design), 80 (actual)
- Aircraft_Capacity_Normal: 70-80

DEFENSIVE ARMAMENT:
- Hardpoint_Secondary_Battery: "18× Single-5in/54 DP"
- Hardpoint_Secondary_Count: 18
- Hardpoint_AA_Light: "84× 40mm Bofors"
- Hardpoint_AA_Light_Count: 84

ARMOR:
- Flight_Deck_Armor: 3.5"
- Hangar_Deck_Armor: 2.5"
- Belt_Armor: 7.6"

NOTES: Heavily armored, multiple massive modernizations (SCB-101, SCB-110)
```

### USS Forrestal (CV-59) - 1955 First Supercarrier
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 1,039
- Flight_Deck_Width_FT: 252 (at widest, angled deck)
- Hardpoint_Catapult_Type: "Steam-C13" ⭐ POWERFUL
- Hardpoint_Catapult_Count: 4 (2 bow + 2 waist)
- Hardpoint_Catapult_Layout: "2 Bow / 2 Waist"
- Hardpoint_Elevator_Count: 4 (3 deck-edge + 1 centerline)
- Aircraft_Capacity_Normal: 85-90

DEFENSIVE ARMAMENT:
- Hardpoint_Secondary_Battery: "8× Single-5in/54 Mk 42"
- Hardpoint_Secondary_Count: 8

MODULE SLOTS:
- Module_Slot_Catapults: 4
- Module_Slot_Elevators: 4
- Module_Slot_Engine_Boilers: 8
- Module_Slot_Engine_Turbines: 4

NOTES: First purpose-built angled deck supercarrier
```

### USS Enterprise (CVN-65) - 1961 First Nuclear Carrier
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 1,123
- Flight_Deck_Width_FT: 257 (at widest)
- Hardpoint_Catapult_Type: "Steam-C13"
- Hardpoint_Catapult_Count: 4
- Hardpoint_Elevator_Count: 4
- Aircraft_Capacity_Normal: 90

DEFENSIVE ARMAMENT (1961):
- No guns initially! (removed in design)

DEFENSIVE ARMAMENT (1980s Refit):
- Hardpoint_Missile_VLS: "3× Mk 29 Sea Sparrow Launchers"
- Hardpoint_Missile_VLS_Cells: 24 (8-cell launchers)
- Hardpoint_CIWS: "3× Phalanx CIWS"
- Hardpoint_CIWS_Count: 3

MODULE SLOTS:
- Module_Slot_Catapults: 4
- Module_Slot_Elevators: 4
- Module_Slot_Engine_Reactors: 8 ⭐ NUCLEAR (A2W reactors)
- Module_Slot_Radar_Masts: 6 (SPS-48, SPS-49, etc.)

PROPULSION:
- Unlimited range (nuclear)
- No refueling for 25 years

NOTES: First nuclear carrier, unique 8-reactor design
```

### USS Nimitz (CVN-68) - 1975 Ultimate Carrier
```
FLIGHT OPERATIONS:
- Flight_Deck_Length_FT: 1,092
- Flight_Deck_Width_FT: 252
- Hardpoint_Catapult_Type: "Steam-C13"
- Hardpoint_Catapult_Count: 4
- Hardpoint_Elevator_Count: 4
- Aircraft_Capacity_Normal: 85-90

DEFENSIVE ARMAMENT:
- Hardpoint_Missile_VLS: "3× Mk 29 Sea Sparrow Launchers"
- Hardpoint_Missile_VLS_Cells: 24
- Hardpoint_CIWS: "4× Phalanx CIWS" (later 3× Phalanx + 2× RAM)
- Hardpoint_CIWS_Count: 4

MODULE SLOTS:
- Module_Slot_Catapults: 4
- Module_Slot_Elevators: 4
- Module_Slot_Engine_Reactors: 2 ⭐ (A4W reactors - more efficient)
- Module_Slot_Radar_Masts: 5

PROPULSION:
- 2× A4W reactors (260,000 shp)
- Unlimited range
- 30+ kts

NOTES: Perfected nuclear carrier design, 50-year service life
```

---

## Carrier Module Categories

### Flight Operations Modules
1. **Catapult Type**: Hydraulic-H, Steam-C11, Steam-C13, EMALS
2. **Arresting Gear**: Mk 7, Advanced Recovery System
3. **Elevators**: Weight capacity, location (centerline, deck-edge)
4. **Optical Landing System**: Fresnel lens, IFLOLS

### Aircraft Systems Modules
1. **Air Search Radar**: SK, SK-2, SPS-8, SPS-48, SPS-49
2. **TACAN**: Tactical air navigation beacon
3. **CCA Radar**: Carrier Controlled Approach
4. **Datalink**: Link 4, Link 16 (modern)

### Defensive Systems Modules
1. **Gun Fire Control**: Mk 37, Mk 56 directors
2. **Missile Systems**: Sea Sparrow, RAM
3. **CIWS**: Phalanx (modern)
4. **ECM/Decoys**: Chaff, flares, SLQ-32

---

## Carrier Hardpoint Size Categories

### Flight Deck Sizes
- **Small**: <600 ft (Langley, escort carriers)
- **Medium**: 600-800 ft (Ranger, Independence-class CVL)
- **Large**: 800-900 ft (Yorktown, Essex, Midway)
- **Supercarrier**: 900-1,100 ft (Forrestal, Enterprise, Nimitz)

### Catapult Types
- **None**: Pre-1930 carriers (takeoff roll only)
- **Hydraulic-H**: 1930s-1950s (H-2-1, H-4-1 models)
- **Steam-C11**: 1950s modernizations (can launch 40,000 lb jets)
- **Steam-C13**: 1960s+ supercarriers (can launch 80,000 lb aircraft)
- **EMALS**: 2010s+ (electromagnetic, Ford-class)

### Aircraft Capacity Categories
- **Light**: 20-40 aircraft (escort carriers, CVL)
- **Fleet**: 70-90 aircraft (Essex, Midway, Forrestal)
- **Supercarrier**: 85-100 aircraft (Nimitz, Ford)

---

## Refit Mechanics for Carriers

### Major Modernization Programs

**SCB-27 Modernization (Essex-class)**
- **Base Hull**: Essex (1942)
- **Modernized Hull**: Essex SCB-27A (1951-1955)
- **Changes**:
  - Angled deck added (8°)
  - Steam catapults replace hydraulic
  - New elevators (higher capacity)
  - Stronger flight deck (jet operations)
  - Enclosed hurricane bow
- **Refit_Cost**: $40M-$50M
- **Refit_Time**: 18-24 months
- **New Capabilities**: Can operate jets

**SCB-101/110 Modernization (Midway-class)**
- **Base Hull**: Midway (1945)
- **Modernized Hull**: Midway SCB-110 (1966-1970)
- **Changes**:
  - Angled deck extended to 13.5°
  - Larger elevators (54 tons → 105 tons)
  - Beam increased 113 ft → 136 ft
  - Displacement +20,000 tons
  - New island structure
- **Refit_Cost**: $200M
- **Refit_Time**: 36 months
- **New Capabilities**: Can operate F-4 Phantom

---

## Gameplay Implementation

### Player Progression Example

**Early Game**:
1. Research **Langley** (experimental, 36 aircraft)
2. Build Langley hull
3. Install basic aircraft (F3F fighters, TBD torpedo bombers)
4. Operate with limitations (slow, small capacity)

**Mid Game**:
1. Research **Essex-class** (90 aircraft, 33 kts)
2. Build Essex hull with 1942 configuration
3. Install SBD Dauntless, F6F Hellcat modules
4. Later: Research **SCB-27A modernization**
5. Refit Essex to SCB-27A (angled deck, steam cats)
6. Now can install jet aircraft (F9F Panther)

**Late Game**:
1. Research **Nimitz-class** (nuclear, 90 aircraft)
2. Build Nimitz hull
3. Install 2× A4W reactor modules (never refuel)
4. Install F-14 Tomcat, F/A-18 Hornet modules
5. Install Phalanx CIWS modules

---

## Summary

**Carriers are defined by**:
- **Flight deck size** (determines aircraft capacity)
- **Catapult type** (determines what aircraft can launch)
- **Elevator capacity** (determines aircraft weight limits)
- **Speed** (fleet carriers need 30+ kts to keep up with task force)
- **Defensive armament** (AA guns, later missiles)

**No main battery hardpoints** (except Lexington-class unique 8" guns)

**Progression is about**:
- Bigger flight decks → more aircraft
- Better catapults → heavier aircraft (jets)
- Nuclear propulsion → unlimited range

---

**Last Updated**: October 10, 2025
**Status**: Ready for Database Implementation
