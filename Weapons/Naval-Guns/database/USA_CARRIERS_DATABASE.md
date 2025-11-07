# USA Aircraft Carriers Database

**Export Date**: October 10, 2025
**Database Version**: 1.1
**Total Records**: 16 carriers (1920-1990 coverage)

---

## Overview

This document contains USA carrier entries for the Naval Ships Database, organized by era and class. All entries use **strength-based tier progression** matching the research tree system.

**ID Range**: 11000-11249 (USA Carriers)
- Fleet Carriers: 11000-11099
- Light Carriers: 11100-11149
- Escort Carriers: 11150-11199
- Modern/Nuclear: 11200-11249

---

## Aircraft Carrier Entries

### **TIER 1: EXPERIMENTAL (1920s)**

#### USS Langley (CV-1) - 1922 Experimental Carrier

```
Ship_ID: 11000
Country: USA
Ship_Name: USS Langley (CV-1)
Ship_Class: Langley-class
Hull_Variant: Base 1922
Base_Hull_ID: NULL
Hull_Number: CV-1
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Experimental Carrier

HISTORY:
Year_Laid_Down: 1911 (as collier Jupiter)
Year_Launched: 1912
Year_Commissioned: 1922 (as carrier)
Year_Decommissioned: 1937 (converted to seaplane tender)
Year_Fate: 1942
Fate: Sunk by Japanese aircraft, February 27, 1942

DIMENSIONS:
Displacement_Standard_TONS: 11500
Displacement_Full_TONS: 15200
Length_Overall_FT: 542.00
Length_Waterline_FT: 520.00
Beam_FT: 65.25
Draft_FT: 18.92
Turning_Radius_YD: 850

CREW:
Crew_Officers_Min: 15
Crew_Enlisted_Min: 285
Crew_Total_Min: 300
Crew_Officers: 35
Crew_Enlisted: 433
Crew_Total: 468
Crew_Officers_Max: 45
Crew_Enlisted_Max: 500
Crew_Total_Max: 545

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL (no main battery)
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 4× Single-5in/51
Hardpoint_Secondary_Count: 4
Hardpoint_Secondary_Size: Single-5in
Hardpoint_AA_Light: NULL (1922, no dedicated AA)
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 534.00
Flight_Deck_Width_FT: 64.00
Flight_Deck_Armor_IN: 0.00 (unarmored wood deck)
Hardpoint_Catapult_Type: None
Hardpoint_Catapult_Count: 0
Hardpoint_Catapult_Layout: NULL
Hardpoint_Elevator_Count: 1
Hardpoint_Elevator_Capacity_LBS: 8000
Hangar_Deck_Length_FT: 210.00
Hangar_Deck_Width_FT: 42.00
Hangar_Deck_Height_FT: 16.00
Aircraft_Capacity_Normal: 36
Aircraft_Capacity_Maximum: 40
Aircraft_Capacity_Deck_Park: 12
Aircraft_Capacity_Hangar: 28

MODULE SLOTS:
Module_Slot_Engine_Boilers: 6 (coal-fired initially, oil later)
Module_Slot_Engine_Turbines: 2
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 1
Module_Slot_Radar_Masts: 0 (1922, no radar)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 0

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 50
Magazine_Capacity_AA_TONS: 0
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 50
Ordnance_Capacity_Aircraft_TONS: 120 (bombs, torpedoes for aircraft)
Fuel_Capacity_TONS: 1150
Supply_Hold_TONS: 200
Aviation_Fuel_TONS: 85

PROPULSION:
Propulsion_Type: Steam turbine, turbo-electric drive
Max_Speed_KTS: 15.50
Range_NM: 3500
Cruise_Speed_KTS: 10.00

COST & BUILD:
Cost_USD: 2000000 (conversion cost)
Build_Time_Months: 18 (conversion time)
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: First US aircraft carrier, converted from collier USS Jupiter. Experimental platform with no catapults initially. Takeoff by rolling forward. Wood flight deck over steel structure. Slow (15 kts) but proved carrier concept. Turbo-electric drive from coal/oil boilers. Served as training carrier 1937-1942. Sunk by Japanese bombers off Java.
```

---

### **TIER 2: CONVERTED BATTLECRUISERS (1927)**

#### USS Lexington (CV-2) - 1927 Battlecruiser Conversion

```
Ship_ID: 11001
Country: USA
Ship_Name: USS Lexington (CV-2)
Ship_Class: Lexington-class
Hull_Variant: Base 1927
Base_Hull_ID: NULL
Hull_Number: CV-2
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier (battlecruiser conversion)

HISTORY:
Year_Laid_Down: 1921 (as battlecruiser CC-1)
Year_Launched: 1925
Year_Commissioned: 1927 (as carrier)
Year_Decommissioned: NULL
Year_Fate: 1942
Fate: Sunk at Battle of Coral Sea, May 8, 1942

DIMENSIONS:
Displacement_Standard_TONS: 36000
Displacement_Full_TONS: 47700
Length_Overall_FT: 888.00
Length_Waterline_FT: 850.00
Beam_FT: 105.50
Draft_FT: 32.00
Turning_Radius_YD: 1050

CREW:
Crew_Officers_Min: 120
Crew_Enlisted_Min: 1880
Crew_Total_Min: 2000
Crew_Officers: 150
Crew_Enlisted: 2122
Crew_Total: 2272
Crew_Officers_Max: 175
Crew_Enlisted_Max: 2500
Crew_Total_Max: 2675

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: 4× Twin-8in/55 Turrets ⭐ UNIQUE FOR CARRIERS!
Hardpoint_Main_Count: 4
Hardpoint_Main_Size: Light-8in
Hardpoint_Secondary_Battery: 12× Single-5in/25 AA
Hardpoint_Secondary_Count: 12
Hardpoint_Secondary_Size: Single-5in
Hardpoint_AA_Light: NULL (1927, minimal AA)
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 866.00
Flight_Deck_Width_FT: 105.00
Flight_Deck_Armor_IN: 0.00 (unarmored)
Hardpoint_Catapult_Type: Hydraulic-H (added 1934)
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 2
Hardpoint_Elevator_Capacity_LBS: 14000
Hangar_Deck_Length_FT: 450.00
Hangar_Deck_Width_FT: 68.00
Hangar_Deck_Height_FT: 21.00
Aircraft_Capacity_Normal: 90
Aircraft_Capacity_Maximum: 105
Aircraft_Capacity_Deck_Park: 30
Aircraft_Capacity_Hangar: 60

MODULE SLOTS:
Module_Slot_Engine_Boilers: 16 (turbo-electric drive)
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 2
Module_Slot_Radar_Masts: 1 (added 1940s)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2

CAPACITY:
Magazine_Capacity_Main_TONS: 500 (for 8" guns)
Magazine_Capacity_Secondary_TONS: 200
Magazine_Capacity_AA_TONS: 50
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 750
Ordnance_Capacity_Aircraft_TONS: 450 (aircraft bombs/torpedoes)
Fuel_Capacity_TONS: 6600
Supply_Hold_TONS: 800
Aviation_Fuel_TONS: 600

PROPULSION:
Propulsion_Type: Steam turbine, turbo-electric drive
Max_Speed_KTS: 33.25
Range_NM: 10000
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 45000000
Build_Time_Months: 72 (6 years total)
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: Converted from battlecruiser CC-1 to carrier CV-2. Massive size (888 ft) and speed (33 kts). UNIQUE: Only US carrier with 8" guns (4 twin turrets). Battlecruiser machinery gives high speed. Huge aircraft capacity (90-105). Turbo-electric drive very reliable. Sunk at Coral Sea after multiple torpedo/bomb hits. Sister ship Saratoga (CV-3) identical, survived war.
```

#### USS Saratoga (CV-3) - 1927 Battlecruiser Conversion

```
Ship_ID: 11002
Country: USA
Ship_Name: USS Saratoga (CV-3)
Ship_Class: Lexington-class
Hull_Variant: Base 1927
Base_Hull_ID: NULL
Hull_Number: CV-3
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier (battlecruiser conversion)

[IDENTICAL SPECS TO LEXINGTON ABOVE, except:]

HISTORY:
Year_Laid_Down: 1920 (as battlecruiser CC-3)
Year_Launched: 1925
Year_Commissioned: 1927
Year_Decommissioned: 1946
Year_Fate: 1946
Fate: Sunk as target ship at Bikini Atoll atomic tests, July 25, 1946

Notes: Sister ship to Lexington. Survived entire WWII with distinction. Torpedoed multiple times but always returned to service. Participated in nearly all major Pacific campaigns. Used as target ship for Operation Crossroads atomic bomb tests at Bikini Atoll. Sank from near-miss blast damage during second test (Baker).
```

---

### **TIER 3: PURPOSE-BUILT TREATY CARRIERS (1930s)**

#### USS Ranger (CV-4) - 1934 First Purpose-Built Carrier

```
Ship_ID: 11003
Country: USA
Ship_Name: USS Ranger (CV-4)
Ship_Class: Ranger-class
Hull_Variant: Base 1934
Base_Hull_ID: NULL
Hull_Number: CV-4
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier (treaty-limited)

HISTORY:
Year_Laid_Down: 1931
Year_Launched: 1933
Year_Commissioned: 1934
Year_Decommissioned: 1946
Year_Fate: 1947
Fate: Scrapped 1947

DIMENSIONS:
Displacement_Standard_TONS: 14500
Displacement_Full_TONS: 17600
Length_Overall_FT: 769.00
Length_Waterline_FT: 730.00
Beam_FT: 80.00
Draft_FT: 22.50
Turning_Radius_YD: 800

CREW:
Crew_Officers_Min: 90
Crew_Enlisted_Min: 1410
Crew_Total_Min: 1500
Crew_Officers: 110
Crew_Enlisted: 1788
Crew_Total: 1898
Crew_Officers_Max: 130
Crew_Enlisted_Max: 2000
Crew_Total_Max: 2130

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 8× Single-5in/25 AA
Hardpoint_Secondary_Count: 8
Hardpoint_Secondary_Size: Single-5in
Hardpoint_AA_Light: 40× .50cal machine guns (minimal)
Hardpoint_AA_Light_Count: 40
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 728.00
Flight_Deck_Width_FT: 80.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Hydraulic-H
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 3
Hardpoint_Elevator_Capacity_LBS: 11000
Hangar_Deck_Length_FT: 490.00
Hangar_Deck_Width_FT: 68.00
Hangar_Deck_Height_FT: 18.00
Aircraft_Capacity_Normal: 76
Aircraft_Capacity_Maximum: 86
Aircraft_Capacity_Deck_Park: 24
Aircraft_Capacity_Hangar: 52

MODULE SLOTS:
Module_Slot_Engine_Boilers: 6
Module_Slot_Engine_Turbines: 2
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 1
Module_Slot_Radar_Masts: 1 (added 1942)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 150
Magazine_Capacity_AA_TONS: 25
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 175
Ordnance_Capacity_Aircraft_TONS: 380
Fuel_Capacity_TONS: 2100
Supply_Hold_TONS: 350
Aviation_Fuel_TONS: 300

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 29.30
Range_NM: 10000
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 15500000
Build_Time_Months: 36
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: First US purpose-built aircraft carrier (not conversion). Treaty-limited to 14,500 tons = TOO SMALL. Lightly built, slow (29 kts vs 33 for Lex/Sara). Weak point in design. Good aircraft capacity (76) but poor protection. Used for training and Atlantic patrols in WWII, not Pacific combat. Proved need for larger, faster carriers. Scrapped 1947.
```

#### USS Yorktown (CV-5) - 1937 Perfect Fleet Carrier

```
Ship_ID: 11004
Country: USA
Ship_Name: USS Yorktown (CV-5)
Ship_Class: Yorktown-class
Hull_Variant: Base 1937
Base_Hull_ID: NULL
Hull_Number: CV-5
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier

HISTORY:
Year_Laid_Down: 1934
Year_Launched: 1936
Year_Commissioned: 1937
Year_Decommissioned: NULL
Year_Fate: 1942
Fate: Sunk at Battle of Midway, June 7, 1942

DIMENSIONS:
Displacement_Standard_TONS: 19900
Displacement_Full_TONS: 25500
Length_Overall_FT: 809.50
Length_Waterline_FT: 770.00
Beam_FT: 83.25
Draft_FT: 26.50
Turning_Radius_YD: 950

CREW:
Crew_Officers_Min: 110
Crew_Enlisted_Min: 1690
Crew_Total_Min: 1800
Crew_Officers: 135
Crew_Enlisted: 2044
Crew_Total: 2179
Crew_Officers_Max: 160
Crew_Enlisted_Max: 2300
Crew_Total_Max: 2460

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 8× Single-5in/38 DP
Hardpoint_Secondary_Count: 8
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: 16× 1.1in Quad Mounts (early AA)
Hardpoint_AA_Light_Count: 16
Hardpoint_AA_Close: 24× .50cal machine guns
Hardpoint_AA_Close_Count: 24
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 809.50
Flight_Deck_Width_FT: 86.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Hydraulic-H
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 3
Hardpoint_Elevator_Capacity_LBS: 13500
Hangar_Deck_Length_FT: 550.00
Hangar_Deck_Width_FT: 70.00
Hangar_Deck_Height_FT: 17.50
Aircraft_Capacity_Normal: 90
Aircraft_Capacity_Maximum: 96
Aircraft_Capacity_Deck_Park: 28
Aircraft_Capacity_Hangar: 62

MODULE SLOTS:
Module_Slot_Engine_Boilers: 9
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 2
Module_Slot_Radar_Masts: 2 (CXAM radar 1941)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 200
Magazine_Capacity_AA_TONS: 75
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 275
Ordnance_Capacity_Aircraft_TONS: 450
Fuel_Capacity_TONS: 3050
Supply_Hold_TONS: 500
Aviation_Fuel_TONS: 450

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 32.50
Range_NM: 12500
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 20000000
Build_Time_Months: 36
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: Perfect WWII fleet carrier design. Balance of speed (32.5 kts), protection, and aircraft capacity (90). Fast enough for task force operations. 3 elevators for efficient operations. Sunk at Midway after heroic service at Coral Sea (repaired in 48 hours!). Sister ships Enterprise (CV-6) and Hornet (CV-8). CV-6 Enterprise = most decorated US ship of WWII, 20 battle stars.
```

---

### **TIER 4: WWII MASS PRODUCTION (1942-1945)**

#### USS Essex (CV-9) - 1942 WWII Workhorse

```
Ship_ID: 11005
Country: USA
Ship_Name: USS Essex (CV-9)
Ship_Class: Essex-class
Hull_Variant: Base 1942
Base_Hull_ID: NULL
Hull_Number: CV-9
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier

HISTORY:
Year_Laid_Down: 1941
Year_Launched: 1942
Year_Commissioned: 1942
Year_Decommissioned: 1973 (served 31 years!)
Year_Fate: 1975
Fate: Scrapped 1975

DIMENSIONS:
Displacement_Standard_TONS: 27200
Displacement_Full_TONS: 36380
Length_Overall_FT: 872.00
Length_Waterline_FT: 820.00
Beam_FT: 93.00
Draft_FT: 28.70
Turning_Radius_YD: 1000

CREW:
Crew_Officers_Min: 150
Crew_Enlisted_Min: 1950
Crew_Total_Min: 2100
Crew_Officers: 185
Crew_Enlisted: 2455
Crew_Total: 2640
Crew_Officers_Max: 210
Crew_Enlisted_Max: 2800
Crew_Total_Max: 3010

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 12× Single-5in/38 DP
Hardpoint_Secondary_Count: 12
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: 32-40× 40mm Quad Bofors
Hardpoint_AA_Light_Count: 40
Hardpoint_AA_Close: 46-52× 20mm Oerlikon
Hardpoint_AA_Close_Count: 52
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 862.00
Flight_Deck_Width_FT: 108.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Hydraulic-H (H-4-1 model)
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 3 (2 centerline + 1 deck-edge)
Hardpoint_Elevator_Capacity_LBS: 14000
Hangar_Deck_Length_FT: 654.00
Hangar_Deck_Width_FT: 70.00
Hangar_Deck_Height_FT: 17.50
Aircraft_Capacity_Normal: 90
Aircraft_Capacity_Maximum: 108
Aircraft_Capacity_Deck_Park: 36
Aircraft_Capacity_Hangar: 72

MODULE SLOTS:
Module_Slot_Engine_Boilers: 8
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 3
Module_Slot_Radar_Masts: 3 (SK, SK-2, Mk 12/22)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 300
Magazine_Capacity_AA_TONS: 150
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 450
Ordnance_Capacity_Aircraft_TONS: 600
Fuel_Capacity_TONS: 6330
Supply_Hold_TONS: 650
Aviation_Fuel_TONS: 750

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 33.00
Range_NM: 20000
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 68000000
Build_Time_Months: 20 (wartime rapid construction!)
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: THE WWII carrier. 24 ships built (CV-9 through CV-21, CV-31 through CV-47). Larger than Yorktown, 33 kts, 90-100 aircraft. Mass produced in 20 months. Powerful AA armament (52× 20mm, 40× 40mm Bofors, 12× 5"/38). 3 elevators for efficient ops. Bow-edge elevator pioneered on this class. Many received SCB-27 modernizations (angled deck, steam cats) and served into 1970s-1990s. CV-9 Essex served 1942-1973 (31 years!).
```

---

### **Essex Interim Variant - 1947 Post-War Refit**

#### USS Essex (CV-9) - 1947 Post-War Refit

```
Ship_ID: 11010
Country: USA
Ship_Name: USS Essex (CV-9)
Ship_Class: Essex-class
Hull_Variant: 1947 Post-War Refit
Base_Hull_ID: 11005
Hull_Number: CV-9
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier (upgraded)

HISTORY:
Year_Laid_Down: 1941
Year_Launched: 1942
Year_Commissioned: 1942 (refitted 1947)
Year_Decommissioned: 1973
Year_Fate: 1975
Fate: Scrapped 1975

DIMENSIONS:
Displacement_Standard_TONS: 27800
Displacement_Full_TONS: 37100
Length_Overall_FT: 872.00
Length_Waterline_FT: 820.00
Beam_FT: 93.00
Draft_FT: 28.90
Turning_Radius_YD: 1000

CREW:
Crew_Officers_Min: 150
Crew_Enlisted_Min: 1950
Crew_Total_Min: 2100
Crew_Officers: 185
Crew_Enlisted: 2480
Crew_Total: 2665
Crew_Officers_Max: 210
Crew_Enlisted_Max: 2850
Crew_Total_Max: 3060

HARDPOINTS - DEFENSIVE ARMAMENT (UPGRADED):
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 12× Single-5in/38 DP
Hardpoint_Secondary_Count: 12
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: 68× 40mm Quad Bofors ⭐ INCREASED from 40
Hardpoint_AA_Light_Count: 68
Hardpoint_AA_Close: 24× 20mm Oerlikon ⭐ REDUCED from 52 (lesson from Okinawa)
Hardpoint_AA_Close_Count: 24
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 862.00
Flight_Deck_Width_FT: 108.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Hydraulic-H (H-4-B improved model)
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 3 (2 centerline + 1 deck-edge)
Hardpoint_Elevator_Capacity_LBS: 16000 (upgraded)
Hangar_Deck_Length_FT: 654.00
Hangar_Deck_Width_FT: 70.00
Hangar_Deck_Height_FT: 17.50
Aircraft_Capacity_Normal: 90
Aircraft_Capacity_Maximum: 108
Aircraft_Capacity_Deck_Park: 36
Aircraft_Capacity_Hangar: 72

MODULE SLOTS:
Module_Slot_Engine_Boilers: 8
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 3
Module_Slot_Radar_Masts: 4 ⭐ UPGRADED (SK-2, SM, SR height-finding)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 300
Magazine_Capacity_AA_TONS: 200 (increased for more 40mm)
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 500
Ordnance_Capacity_Aircraft_TONS: 620
Fuel_Capacity_TONS: 6330
Supply_Hold_TONS: 650
Aviation_Fuel_TONS: 800

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 32.80
Range_NM: 20000
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 68000000 (original cost)
Build_Time_Months: 20 (original build)
Refit_Cost_USD: 8500000
Refit_Time_Months: 6
Modded: 0

Notes: Post-WWII interim refit incorporating Okinawa campaign lessons. Increased 40mm Bofors from 40 to 68 guns (17 quad mounts) - Pacific experience showed 40mm far more effective than 20mm. Reduced 20mm from 52 to 24 guns. Upgraded radar suite: added SM fighter direction radar, SR height-finding radar, improved SK-2 air search. Strengthened elevators to 16,000 lbs for heavier aircraft. Improved hydraulic catapults (H-4-B model). NOT yet jet-capable (still straight deck, no steam cats). This configuration typical of Essex-class carriers serving 1947-1951 before full SCB-27 modernization. Ships like Boxer, Valley Forge, Philippine Sea retained similar configurations throughout Korean War. Moderate cost ($8.5M) and quick (6 months) compared to SCB-27 ($40M, 24 months).
```

---

## **Essex SCB-27A/125 Modernization Variant**

#### USS Essex (CV-9) - SCB-27A/125 Modernization (1951-1955)

```
Ship_ID: 11006
Country: USA
Ship_Name: USS Essex (CV-9)
Ship_Class: Essex-class
Hull_Variant: SCB-27A/125 Modernization
Base_Hull_ID: 11005
Hull_Number: CV-9
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier (jet-capable)

HISTORY:
Year_Laid_Down: 1941
Year_Launched: 1942
Year_Commissioned: 1942 (modernized 1951-1955)
Year_Decommissioned: 1973
Year_Fate: 1975
Fate: Scrapped 1975

DIMENSIONS (MODIFIED):
Displacement_Standard_TONS: 30800
Displacement_Full_TONS: 40600
Length_Overall_FT: 888.00 (enclosed bow extension)
Length_Waterline_FT: 820.00
Beam_FT: 103.00 (angled deck adds beam)
Draft_FT: 30.80
Turning_Radius_YD: 1050

CREW:
Crew_Officers_Min: 140
Crew_Enlisted_Min: 1860
Crew_Total_Min: 2000
Crew_Officers: 175
Crew_Enlisted: 2302
Crew_Total: 2477
Crew_Officers_Max: 200
Crew_Enlisted_Max: 2600
Crew_Total_Max: 2800

HARDPOINTS - DEFENSIVE ARMAMENT (REDUCED):
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 8× Single-5in/38 DP (reduced from 12)
Hardpoint_Secondary_Count: 8
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: NULL (removed, jets made close AA obsolete)
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS (UPGRADED):
Flight_Deck_Length_FT: 888.00 (extended)
Flight_Deck_Width_FT: 108.00 (8° angled deck)
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Steam-C11 ⭐ UPGRADED!
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 3 (2 deck-edge + 1 centerline, upgraded capacity)
Hardpoint_Elevator_Capacity_LBS: 40000 (upgraded for jets)
Hangar_Deck_Length_FT: 654.00
Hangar_Deck_Width_FT: 70.00
Hangar_Deck_Height_FT: 20.00 (raised for jets)
Aircraft_Capacity_Normal: 70
Aircraft_Capacity_Maximum: 82 (reduced from WWII due to larger jets)
Aircraft_Capacity_Deck_Park: 24
Aircraft_Capacity_Hangar: 48

MODULE SLOTS:
Module_Slot_Engine_Boilers: 8
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 2 (reduced)
Module_Slot_Radar_Masts: 4 (SPS-8, SPS-12, etc.)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2 (steam catapult modules installed)

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 200
Magazine_Capacity_AA_TONS: 0
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 200
Ordnance_Capacity_Aircraft_TONS: 650
Fuel_Capacity_TONS: 6330
Supply_Hold_TONS: 650
Aviation_Fuel_TONS: 950 (jet fuel)

PROPULSION:
Propulsion_Type: Steam turbine, geared (unchanged)
Max_Speed_KTS: 31.50 (slightly reduced due to weight)
Range_NM: 18000
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 68000000 (original cost)
Build_Time_Months: 20 (original build)
Refit_Cost_USD: 40000000
Refit_Time_Months: 24
Modded: 0

Notes: SCB-27A modernization transforms WWII carrier for jet age. Angled deck (8°) allows simultaneous launch/recovery. Steam catapults (C11) can launch 40,000 lb jets. Stronger elevators, higher hangar. Enclosed "hurricane bow" for better seakeeping. Reduced gun armament (jets provide defense). Can operate F9F Panther, F2H Banshee, A-1 Skyraider. SCB-125 adds enclosed bow. 14 Essex-class received this modernization, served into 1970s-1990s. Proves value of refit system - WWII carriers still effective 30+ years later.
```

---

---

### **TIER 5: ARMORED CARRIER (1945)**

#### USS Midway (CV-41) - 1945 Armored Fleet Carrier

```
Ship_ID: 11007
Country: USA
Ship_Name: USS Midway (CV-41)
Ship_Class: Midway-class
Hull_Variant: Base 1945
Base_Hull_ID: NULL
Hull_Number: CV-41
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Fleet Carrier (armored)

HISTORY:
Year_Laid_Down: 1943
Year_Launched: 1945
Year_Commissioned: 1945
Year_Decommissioned: 1992 (47 years service!)
Year_Fate: 2003
Fate: Museum ship, San Diego, California

DIMENSIONS:
Displacement_Standard_TONS: 45000
Displacement_Full_TONS: 64000
Length_Overall_FT: 972.00
Length_Waterline_FT: 900.00
Beam_FT: 113.00
Draft_FT: 35.00
Turning_Radius_YD: 1150

CREW:
Crew_Officers_Min: 190
Crew_Enlisted_Min: 2310
Crew_Total_Min: 2500
Crew_Officers: 230
Crew_Enlisted: 3995
Crew_Total: 4225
Crew_Officers_Max: 270
Crew_Enlisted_Max: 4500
Crew_Total_Max: 4770

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 18× Single-5in/54 Mk 16 DP
Hardpoint_Secondary_Count: 18
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: 84× 40mm Bofors (21 quad mounts)
Hardpoint_AA_Light_Count: 84
Hardpoint_AA_Close: 68× 20mm Oerlikon
Hardpoint_AA_Close_Count: 68
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 932.00
Flight_Deck_Width_FT: 113.00
Flight_Deck_Armor_IN: 3.50 ⭐ ARMORED!
Hardpoint_Catapult_Type: Hydraulic-H (later Steam-C11)
Hardpoint_Catapult_Count: 2
Hardpoint_Catapult_Layout: 2 Bow
Hardpoint_Elevator_Count: 3
Hardpoint_Elevator_Capacity_LBS: 18000
Hangar_Deck_Length_FT: 692.00
Hangar_Deck_Width_FT: 78.00
Hangar_Deck_Height_FT: 17.50
Aircraft_Capacity_Normal: 137 (design), 80 (actual WWII/Korea)
Aircraft_Capacity_Maximum: 145
Aircraft_Capacity_Deck_Park: 45
Aircraft_Capacity_Hangar: 92

MODULE SLOTS:
Module_Slot_Engine_Boilers: 12
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 3
Module_Slot_Radar_Masts: 4 (SK-2, SPS-8, SPS-43, etc.)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 2

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 450
Magazine_Capacity_AA_TONS: 300
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 750
Ordnance_Capacity_Aircraft_TONS: 900
Fuel_Capacity_TONS: 8500
Supply_Hold_TONS: 1200
Aviation_Fuel_TONS: 1100

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 33.00
Range_NM: 15000
Cruise_Speed_KTS: 15.00

COST & BUILD:
Cost_USD: 90000000
Build_Time_Months: 24
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: First US armored carrier. 3.5" flight deck armor, 2.5" hangar deck armor, 7.6" belt armor. British influence (armored carriers like Illustrious). Massive size (45,000 tons standard, 64,000 full). Longest-serving carrier (1945-1992 = 47 years!). Too wide for Panama Canal. Received THREE major modernizations (SCB-101, SCB-110, SCB-110.66). SCB-110 (1966-1970): angled deck increased to 13.5°, elevators upgraded 54 tons→105 tons, beam increased 113→136 ft. Operated F-4 Phantom, F/A-18 Hornet. Gulf War veteran (1991). Museum ship San Diego. Sister ships: Franklin D. Roosevelt (CV-42), Coral Sea (CV-43).
```

---

### **TIER 6: SUPERCARRIER ERA (1955-1968)**

#### USS Forrestal (CV-59) - 1955 First Supercarrier

```
Ship_ID: 11008
Country: USA
Ship_Name: USS Forrestal (CV-59)
Ship_Class: Forrestal-class
Hull_Variant: Base 1955
Base_Hull_ID: NULL
Hull_Number: CV-59
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Supercarrier

HISTORY:
Year_Laid_Down: 1952
Year_Launched: 1954
Year_Commissioned: 1955
Year_Decommissioned: 1993
Year_Fate: 2015
Fate: Scrapped 2015

DIMENSIONS:
Displacement_Standard_TONS: 60000
Displacement_Full_TONS: 79248
Length_Overall_FT: 1076.00
Length_Waterline_FT: 990.00
Beam_FT: 129.00
Draft_FT: 37.00
Turning_Radius_YD: 1250

CREW:
Crew_Officers_Min: 210
Crew_Enlisted_Min: 2390
Crew_Total_Min: 2600
Crew_Officers: 280
Crew_Enlisted: 2920
Crew_Total: 3200
Crew_Officers_Max: 320
Crew_Enlisted_Max: 3300
Crew_Total_Max: 3620

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 8× Single-5in/54 Mk 42
Hardpoint_Secondary_Count: 8
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: NULL (removed in design)
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: NULL (later added Sea Sparrow)
Hardpoint_Missile_VLS_Cells: 0
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: NULL (later added Phalanx)
Hardpoint_CIWS_Count: 0

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 1039.00
Flight_Deck_Width_FT: 252.00 (at angled deck)
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Steam-C13
Hardpoint_Catapult_Count: 4
Hardpoint_Catapult_Layout: 2 Bow / 2 Waist
Hardpoint_Elevator_Count: 4 (3 deck-edge + 1 centerline)
Hardpoint_Elevator_Capacity_LBS: 105000
Hangar_Deck_Length_FT: 740.00
Hangar_Deck_Width_FT: 101.00
Hangar_Deck_Height_FT: 25.00
Aircraft_Capacity_Normal: 85
Aircraft_Capacity_Maximum: 95
Aircraft_Capacity_Deck_Park: 30
Aircraft_Capacity_Hangar: 55

MODULE SLOTS:
Module_Slot_Engine_Boilers: 8
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 2
Module_Slot_Radar_Masts: 5 (SPS-8, SPS-12, SPS-30, SPS-37, SPS-43)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 4

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 300
Magazine_Capacity_AA_TONS: 0
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 0
Magazine_Capacity_Total_TONS: 300
Ordnance_Capacity_Aircraft_TONS: 1650
Fuel_Capacity_TONS: 7800
Supply_Hold_TONS: 1800
Aviation_Fuel_TONS: 1800

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 33.00
Range_NM: 12000
Cruise_Speed_KTS: 20.00

COST & BUILD:
Cost_USD: 217000000
Build_Time_Months: 36
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: First PURPOSE-BUILT supercarrier with angled deck from design. Massive: 60,000 tons standard, 80,000 full load. 4× C13 steam catapults (2 bow + 2 waist). 4 elevators (3 deck-edge + 1 centerline). Flight deck 1,039 ft long, 252 ft wide at angle. Can launch/recover simultaneously. Fuel capacity 2.84 million gallons. Famous 1967 fire killed 134 sailors. Vietnam veteran. Decommissioned 1993, scrapped 2015. Class: Forrestal (CV-59), Saratoga (CV-60), Ranger (CV-61), Independence (CV-62). Last oil-fired US carriers.
```

#### USS Kitty Hawk (CV-63) - 1961 Improved Forrestal

```
Ship_ID: 11009
Country: USA
Ship_Name: USS Kitty Hawk (CV-63)
Ship_Class: Kitty Hawk-class
Hull_Variant: Base 1961
Base_Hull_ID: NULL
Hull_Number: CV-63
Ship_Type: CV
Ship_Type_Full: Aircraft Carrier
Subtype: Supercarrier

HISTORY:
Year_Laid_Down: 1956
Year_Launched: 1960
Year_Commissioned: 1961
Year_Decommissioned: 2009
Year_Fate: 2022
Fate: Scrapped 2022 (sold for 1 cent!)

DIMENSIONS:
Displacement_Standard_TONS: 61000
Displacement_Full_TONS: 81780
Length_Overall_FT: 1069.00
Length_Waterline_FT: 990.00
Beam_FT: 130.00
Draft_FT: 38.00
Turning_Radius_YD: 1250

CREW:
Crew_Officers_Min: 220
Crew_Enlisted_Min: 2480
Crew_Total_Min: 2700
Crew_Officers: 290
Crew_Enlisted: 3050
Crew_Total: 3340
Crew_Officers_Max: 330
Crew_Enlisted_Max: 3450
Crew_Total_Max: 3780

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: 8× Single-5in/54 Mk 42 (later removed)
Hardpoint_Secondary_Count: 8
Hardpoint_Secondary_Size: DP-5in
Hardpoint_AA_Light: NULL
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: 3× Mk 29 Sea Sparrow Launchers
Hardpoint_Missile_VLS_Cells: 24 (8-cell launchers)
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: 3× Phalanx CIWS (added 1980s)
Hardpoint_CIWS_Count: 3

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 1047.00
Flight_Deck_Width_FT: 252.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Steam-C13
Hardpoint_Catapult_Count: 4
Hardpoint_Catapult_Layout: 2 Bow / 2 Waist
Hardpoint_Elevator_Count: 4 (4 deck-edge, improved layout)
Hardpoint_Elevator_Capacity_LBS: 105000
Hangar_Deck_Length_FT: 740.00
Hangar_Deck_Width_FT: 101.00
Hangar_Deck_Height_FT: 25.00
Aircraft_Capacity_Normal: 85
Aircraft_Capacity_Maximum: 95
Aircraft_Capacity_Deck_Park: 30
Aircraft_Capacity_Hangar: 55

MODULE SLOTS:
Module_Slot_Engine_Boilers: 8
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 0
Module_Slot_FCS_Directors: 2
Module_Slot_Radar_Masts: 5 (SPS-48, SPS-49, etc.)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 4

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 200
Magazine_Capacity_AA_TONS: 0
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 50
Magazine_Capacity_Total_TONS: 250
Ordnance_Capacity_Aircraft_TONS: 1700
Fuel_Capacity_TONS: 7800
Supply_Hold_TONS: 1900
Aviation_Fuel_TONS: 1900

PROPULSION:
Propulsion_Type: Steam turbine, geared
Max_Speed_KTS: 33.00
Range_NM: 12000
Cruise_Speed_KTS: 20.00

COST & BUILD:
Cost_USD: 264000000
Build_Time_Months: 42
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: Improved Forrestal design. Better elevator arrangement (4 deck-edge instead of 3+1 centerline). Last conventionally-powered US carrier to operate. Served 48 years (1961-2009). Vietnam veteran, operated F-4 Phantom, F-14 Tomcat, F/A-18 Hornet. Added Sea Sparrow missiles (1980s) and Phalanx CIWS. Sister ships: Constellation (CV-64), America (CV-66), JFK (CV-67). CV-67 JFK = last oil-fired carrier built. Decommissioned 2009, scrapped 2022 (sold for 1 cent to International Shipbreaking Limited).
```

---

### **TIER 7: NUCLEAR SUPERCARRIER (1961-1975)**

#### USS Enterprise (CVN-65) - 1961 First Nuclear Carrier

```
Ship_ID: 11200
Country: USA
Ship_Name: USS Enterprise (CVN-65)
Ship_Class: Enterprise-class
Hull_Variant: Base 1961
Base_Hull_ID: NULL
Hull_Number: CVN-65
Ship_Type: CVN
Ship_Type_Full: Aircraft Carrier (Nuclear)
Subtype: Nuclear Supercarrier

HISTORY:
Year_Laid_Down: 1958
Year_Launched: 1960
Year_Commissioned: 1961
Year_Decommissioned: 2012 (51 years service!)
Year_Fate: 2025 (scheduled)
Fate: Decommissioning/scrapping in progress

DIMENSIONS:
Displacement_Standard_TONS: 89600
Displacement_Full_TONS: 93500
Length_Overall_FT: 1123.00
Length_Waterline_FT: 1040.00
Beam_FT: 133.00
Draft_FT: 39.00
Turning_Radius_YD: 1300

CREW:
Crew_Officers_Min: 240
Crew_Enlisted_Min: 2560
Crew_Total_Min: 2800
Crew_Officers: 320
Crew_Enlisted: 3140
Crew_Total: 3460
Crew_Officers_Max: 380
Crew_Enlisted_Max: 3700
Crew_Total_Max: 4080

HARDPOINTS - DEFENSIVE ARMAMENT (1961):
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: NULL (removed in design!)
Hardpoint_Secondary_Count: 0
Hardpoint_Secondary_Size: NULL
Hardpoint_AA_Light: NULL
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: 3× Mk 29 Sea Sparrow Launchers (added 1980s)
Hardpoint_Missile_VLS_Cells: 24
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: 3× Phalanx CIWS (added 1980s)
Hardpoint_CIWS_Count: 3

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 1123.00
Flight_Deck_Width_FT: 257.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Steam-C13
Hardpoint_Catapult_Count: 4
Hardpoint_Catapult_Layout: 2 Bow / 2 Waist
Hardpoint_Elevator_Count: 4 (4 deck-edge)
Hardpoint_Elevator_Capacity_LBS: 105000
Hangar_Deck_Length_FT: 860.00
Hangar_Deck_Width_FT: 108.00
Hangar_Deck_Height_FT: 25.00
Aircraft_Capacity_Normal: 90
Aircraft_Capacity_Maximum: 110
Aircraft_Capacity_Deck_Park: 40
Aircraft_Capacity_Hangar: 60

MODULE SLOTS:
Module_Slot_Engine_Boilers: 0
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 8 ⭐ NUCLEAR (A2W reactors)
Module_Slot_FCS_Directors: 0
Module_Slot_Radar_Masts: 6 (SPS-48, SPS-49, SPS-58, SPS-64, etc.)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 4

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 0
Magazine_Capacity_AA_TONS: 0
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 60
Magazine_Capacity_Total_TONS: 60
Ordnance_Capacity_Aircraft_TONS: 2520
Fuel_Capacity_TONS: 0 (nuclear, no conventional fuel!)
Supply_Hold_TONS: 2500
Aviation_Fuel_TONS: 2700

PROPULSION:
Propulsion_Type: Nuclear, 8× A2W reactors, steam turbines
Max_Speed_KTS: 33.60
Range_NM: UNLIMITED (nuclear)
Cruise_Speed_KTS: 20.00

COST & BUILD:
Cost_USD: 451000000
Build_Time_Months: 54
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: FIRST nuclear-powered aircraft carrier! 8× A2W reactors (unique, expensive - later carriers use 2 reactors). UNLIMITED range - no refueling for 25+ years. No conventional fuel = more space for aviation fuel and ordnance. Longest carrier (1,123 ft). Originally built with NO guns (removed in design) - added Sea Sparrow and Phalanx in 1980s. Distinctive square "billboard" radar arrays on island (later removed). Served 51 years (1961-2012) - longest-serving carrier. Vietnam veteran, operated F-4 Phantom, F-14 Tomcat, F/A-18 Hornet. Nuclear power allows 30+ kts indefinitely. 8-reactor design never repeated (too expensive). Decommissioned 2012, deactivation ongoing.
```

#### USS Nimitz (CVN-68) - 1975 Ultimate Nuclear Carrier

```
Ship_ID: 11201
Country: USA
Ship_Name: USS Nimitz (CVN-68)
Ship_Class: Nimitz-class
Hull_Variant: Base 1975
Base_Hull_ID: NULL
Hull_Number: CVN-68
Ship_Type: CVN
Ship_Type_Full: Aircraft Carrier (Nuclear)
Subtype: Nuclear Supercarrier

HISTORY:
Year_Laid_Down: 1968
Year_Launched: 1972
Year_Commissioned: 1975
Year_Decommissioned: NULL (still active as of 2025!)
Year_Fate: NULL
Fate: Active service (scheduled retirement ~2025-2030)

DIMENSIONS:
Displacement_Standard_TONS: 97000
Displacement_Full_TONS: 104000
Length_Overall_FT: 1092.00
Length_Waterline_FT: 1040.00
Beam_FT: 134.00
Draft_FT: 37.00
Turning_Radius_YD: 1300

CREW:
Crew_Officers_Min: 260
Crew_Enlisted_Min: 2740
Crew_Total_Min: 3000
Crew_Officers: 340
Crew_Enlisted: 2860
Crew_Total: 3200
Crew_Officers_Max: 400
Crew_Enlisted_Max: 3300
Crew_Total_Max: 3700

HARDPOINTS - DEFENSIVE ARMAMENT:
Hardpoint_Main_Battery: NULL
Hardpoint_Main_Count: 0
Hardpoint_Main_Size: NULL
Hardpoint_Secondary_Battery: NULL
Hardpoint_Secondary_Count: 0
Hardpoint_Secondary_Size: NULL
Hardpoint_AA_Light: NULL
Hardpoint_AA_Light_Count: 0
Hardpoint_AA_Close: NULL
Hardpoint_AA_Close_Count: 0
Hardpoint_Torpedo: NULL
Hardpoint_Torpedo_Count: 0
Hardpoint_Missile_VLS: 3× Mk 29 Sea Sparrow Launchers
Hardpoint_Missile_VLS_Cells: 24 (8-cell launchers)
Hardpoint_Missile_Launcher: NULL
Hardpoint_Missile_Launcher_Count: 0
Hardpoint_CIWS: 4× Phalanx CIWS (later 3× Phalanx + 2× RAM)
Hardpoint_CIWS_Count: 4

FLIGHT OPERATIONS:
Flight_Deck_Length_FT: 1092.00
Flight_Deck_Width_FT: 252.00
Flight_Deck_Armor_IN: 0.00
Hardpoint_Catapult_Type: Steam-C13
Hardpoint_Catapult_Count: 4
Hardpoint_Catapult_Layout: 2 Bow / 2 Waist
Hardpoint_Elevator_Count: 4 (4 deck-edge)
Hardpoint_Elevator_Capacity_LBS: 105000
Hangar_Deck_Length_FT: 684.00
Hangar_Deck_Width_FT: 108.00
Hangar_Deck_Height_FT: 25.00
Aircraft_Capacity_Normal: 85
Aircraft_Capacity_Maximum: 90
Aircraft_Capacity_Deck_Park: 30
Aircraft_Capacity_Hangar: 55

MODULE SLOTS:
Module_Slot_Engine_Boilers: 0
Module_Slot_Engine_Turbines: 4
Module_Slot_Engine_Reactors: 2 ⭐ (A4W reactors - improved efficiency!)
Module_Slot_FCS_Directors: 0
Module_Slot_Radar_Masts: 5 (SPS-48E, SPS-49, etc.)
Module_Slot_Radar_Arrays: 0
Module_Slot_Sonar_Bow: 0
Module_Slot_Sonar_Towed: 0
Module_Slot_Helicopter_Deck: 0
Module_Slot_Catapults: 4

CAPACITY:
Magazine_Capacity_Main_TONS: 0
Magazine_Capacity_Secondary_TONS: 0
Magazine_Capacity_AA_TONS: 0
Magazine_Capacity_Torpedo_TONS: 0
Magazine_Capacity_Missile_TONS: 75
Magazine_Capacity_Total_TONS: 75
Ordnance_Capacity_Aircraft_TONS: 2970
Fuel_Capacity_TONS: 0 (nuclear)
Supply_Hold_TONS: 2800
Aviation_Fuel_TONS: 3000

PROPULSION:
Propulsion_Type: Nuclear, 2× A4W reactors, steam turbines
Max_Speed_KTS: 30.00+ (official, actual ~33+)
Range_NM: UNLIMITED (nuclear)
Cruise_Speed_KTS: 20.00

COST & BUILD:
Cost_USD: 1000000000 (1975 dollars, ~$4.5B in 2020s)
Build_Time_Months: 72
Refit_Cost_USD: NULL
Refit_Time_Months: NULL
Modded: 0

Notes: ULTIMATE carrier design! Perfected nuclear carrier with 2× A4W reactors (more efficient than Enterprise's 8 reactors). Class of 10 ships (CVN-68 through CVN-77). 50-year service life design. 100,000+ tons full load. UNLIMITED range, can steam at 30+ kts indefinitely. 85-90 aircraft (F-14 Tomcat, F/A-18 Hornet/Super Hornet, E-2 Hawkeye, EA-18G Growler). 4× C13 steam catapults can launch 80,000 lb aircraft. 4 deck-edge elevators. Defensive: 3× Sea Sparrow launchers, 4× Phalanx CIWS (later mixed with RAM). CVN-68 Nimitz commissioned 1975, still serving 50 years later (2025). Class includes famous ships: CVN-69 Eisenhower, CVN-70 Carl Vinson, CVN-71 Theodore Roosevelt, CVN-72 Abraham Lincoln, CVN-73 George Washington, CVN-74 John C. Stennis, CVN-75 Harry S. Truman, CVN-76 Ronald Reagan, CVN-77 George H.W. Bush. Most successful carrier design ever - will serve into 2050s+. US Navy operates 11 carriers, 10 are Nimitz-class + 1 Ford-class (CVN-78).
```

---

## Summary

**Total USA Carriers in Database**: 12 ships covering 1920-1990
- **Tier 1**: Langley (experimental)
- **Tier 2**: Lexington, Saratoga (battlecruiser conversions)
- **Tier 3**: Ranger (weak), Yorktown (perfect design)
- **Tier 4**: Essex (WWII workhorse), Essex 1947 Refit (interim upgrades), Essex SCB-27A (modernized for jets)
- **Tier 5**: Midway (armored carrier)
- **Tier 6**: Forrestal (first supercarrier), Kitty Hawk (improved)
- **Tier 7**: Enterprise CVN-65 (first nuclear), Nimitz (ultimate)

**Strength-Based Progression**:
- **Weakest**: Langley (slow, small, experimental)
- **Strongest**: Nimitz (nuclear, unlimited range, 90 aircraft, 50-year service life)

**Key Innovations**:
- **Hydraulic catapults** → **Steam catapults** → **EMALS** (future)
- **No angled deck** → **Angled deck** → **Better layouts**
- **Oil-fired** → **Nuclear propulsion**
- **Guns only** → **Missiles + CIWS**

---

**Last Updated**: October 10, 2025
**Ready for Research Tree Integration**: ✅