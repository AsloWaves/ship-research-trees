# Naval Ships Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 0 (ready for expansion)

---

## Database Contents

- [Ships Table](#ships-table) - Naval vessels and specifications
- [Armament Table](#armament-table) - Guns, torpedoes, and missiles
- [Aircraft Complement Table](#aircraft-complement-table) - Embarked aircraft
- [Armor Protection Table](#armor-protection-table) - Armor schemes
- [Propulsion Table](#propulsion-table) - Engine and power systems
- [Service History Table](#service-history-table) - Operational history

---

<a name="ships-table"></a>
## Ships Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Ship_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation of origin |
| Ship_Name | VARCHAR(100) | Ship name (e.g., "USS Iowa", "HMS Hood", "Yamato") |
| Ship_Class | VARCHAR(100) | Class name (e.g., "Iowa-class", "King George V-class") |
| Hull_Variant | VARCHAR(100) | Variant name (e.g., "Base 1920", "1943 Rebuild", "1984 Refit") |
| Base_Hull_ID | INT | Foreign key to base hull if this is a variant (NULL if base hull) |
| Hull_Number | VARCHAR(50) | Hull classification (e.g., "BB-61", "R-09") |
| Ship_Type | VARCHAR(50) | BB, CV, CA, CL, DD, SS, CVN, DDG, CG, etc. |
| Ship_Type_Full | VARCHAR(100) | Full type name (Battleship, Carrier, Cruiser, etc.) |
| Subtype | VARCHAR(100) | Fast battleship, Fleet carrier, Heavy cruiser, etc. |
| Year_Laid_Down | INT | Year construction began |
| Year_Launched | INT | Year ship launched |
| Year_Commissioned | INT | Year entered service |
| Year_Decommissioned | INT | Year retired (null if still active) |
| Year_Fate | INT | Year of final disposition |
| Fate | VARCHAR(200) | Scrapped, Sunk in action, Museum ship, etc. |
| Displacement_Standard_TONS | INT | Standard displacement in tons |
| Displacement_Full_TONS | INT | Full load displacement in tons |
| Length_Overall_FT | DECIMAL(6,2) | Overall length in feet |
| Length_Waterline_FT | DECIMAL(6,2) | Waterline length in feet |
| Beam_FT | DECIMAL(5,2) | Maximum beam in feet |
| Draft_FT | DECIMAL(5,2) | Draft at full load in feet |
| Turning_Radius_YD | INT | Turning radius in yards at cruising speed |
| Crew_Officers_Min | INT | Minimum officers required |
| Crew_Enlisted_Min | INT | Minimum enlisted required |
| Crew_Total_Min | INT | Minimum total crew to operate ship |
| Crew_Officers | INT | Normal complement of officers |
| Crew_Enlisted | INT | Normal complement of enlisted personnel |
| Crew_Total | INT | Normal total crew complement |
| Crew_Officers_Max | INT | Maximum officers (quarters capacity) |
| Crew_Enlisted_Max | INT | Maximum enlisted (quarters capacity) |
| Crew_Total_Max | INT | Maximum total crew capacity |
| Hardpoint_Main_Battery | VARCHAR(200) | Main battery hardpoint layout (e.g., "4× Heavy-14in Centerline") |
| Hardpoint_Main_Count | INT | Number of main battery hardpoints |
| Hardpoint_Main_Size | VARCHAR(50) | Hardpoint size/type (e.g., "Heavy-14in", "XHeavy-16in") |
| Hardpoint_Secondary_Battery | VARCHAR(200) | Secondary battery hardpoint layout |
| Hardpoint_Secondary_Count | INT | Number of secondary battery hardpoints |
| Hardpoint_Secondary_Size | VARCHAR(50) | Secondary hardpoint size/type |
| Hardpoint_AA_Light | VARCHAR(200) | Light AA hardpoint layout |
| Hardpoint_AA_Light_Count | INT | Number of light AA hardpoints |
| Hardpoint_AA_Close | VARCHAR(200) | Close-in AA hardpoint layout |
| Hardpoint_AA_Close_Count | INT | Number of close-in AA hardpoints |
| Hardpoint_Torpedo | VARCHAR(200) | Torpedo tube hardpoint layout |
| Hardpoint_Torpedo_Count | INT | Number of torpedo hardpoints |
| Hardpoint_Missile_VLS | VARCHAR(200) | VLS missile hardpoint layout |
| Hardpoint_Missile_VLS_Cells | INT | Total VLS cells available |
| Hardpoint_Missile_Launcher | VARCHAR(200) | Dedicated missile launcher hardpoints |
| Hardpoint_Missile_Launcher_Count | INT | Number of missile launcher hardpoints |
| Module_Slot_Engine_Boilers | INT | Number of boiler slots |
| Module_Slot_Engine_Turbines | INT | Number of turbine/engine slots |
| Module_Slot_Engine_Reactors | INT | Number of reactor slots (nuclear ships) |
| Module_Slot_FCS_Directors | INT | Number of fire control director positions |
| Module_Slot_Radar_Masts | INT | Number of radar mast positions |
| Module_Slot_Radar_Arrays | INT | Number of phased array radar positions |
| Module_Slot_Sonar_Bow | INT | Number of bow sonar positions (0 or 1) |
| Module_Slot_Sonar_Towed | INT | Number of towed array positions (0 or 1) |
| Module_Slot_Helicopter_Deck | INT | Number of helicopter landing spots |
| Module_Slot_Catapults | INT | Number of aircraft catapults (carriers) |
| Flight_Deck_Length_FT | DECIMAL(6,2) | Flight deck length (carriers only) |
| Flight_Deck_Width_FT | DECIMAL(6,2) | Flight deck width (carriers only) |
| Flight_Deck_Armor_IN | DECIMAL(5,2) | Flight deck armor thickness (0 if unarmored) |
| Hardpoint_Catapult_Type | VARCHAR(50) | Catapult type: None, Hydraulic-H, Steam-C11, Steam-C13, EMALS |
| Hardpoint_Catapult_Count | INT | Number of catapult positions (0-4) |
| Hardpoint_Catapult_Layout | VARCHAR(100) | Catapult arrangement (e.g., "2 Bow / 2 Waist") |
| Hardpoint_Elevator_Count | INT | Number of aircraft elevators |
| Hardpoint_Elevator_Capacity_LBS | INT | Elevator weight capacity in pounds |
| Hangar_Deck_Length_FT | DECIMAL(6,2) | Hangar deck length |
| Hangar_Deck_Width_FT | DECIMAL(6,2) | Hangar deck width |
| Hangar_Deck_Height_FT | DECIMAL(5,2) | Hangar clearance height |
| Aircraft_Capacity_Normal | INT | Normal operational aircraft complement |
| Aircraft_Capacity_Maximum | INT | Maximum surge aircraft capacity |
| Aircraft_Capacity_Deck_Park | INT | Aircraft parkable on deck |
| Aircraft_Capacity_Hangar | INT | Aircraft storable in hangar |
| Ordnance_Capacity_Aircraft_TONS | INT | Aircraft ordnance capacity (bombs, missiles, torpedoes) |
| Hardpoint_CIWS | VARCHAR(200) | CIWS hardpoint layout (Phalanx, RAM, etc.) |
| Hardpoint_CIWS_Count | INT | Number of CIWS positions |
| Magazine_Capacity_Main_TONS | INT | Magazine capacity for main battery (tons) |
| Magazine_Capacity_Secondary_TONS | INT | Magazine capacity for secondary battery (tons) |
| Magazine_Capacity_AA_TONS | INT | Magazine capacity for AA ammunition (tons) |
| Magazine_Capacity_Torpedo_TONS | INT | Magazine capacity for torpedoes (tons) |
| Magazine_Capacity_Missile_TONS | INT | Magazine capacity for missiles (tons) |
| Magazine_Capacity_Total_TONS | INT | Total ammunition/ordnance capacity (tons) |
| Fuel_Capacity_TONS | INT | Fuel capacity in tons |
| Supply_Hold_TONS | INT | Supply storage capacity (food, parts, consumables) |
| Aviation_Fuel_TONS | INT | Aviation fuel capacity (carriers) |
| Propulsion_Type | VARCHAR(100) | Steam turbine, Nuclear, Diesel-electric, etc. |
| Max_Speed_KTS | DECIMAL(5,2) | Maximum speed in knots |
| Range_NM | INT | Range in nautical miles at cruise speed |
| Cruise_Speed_KTS | DECIMAL(5,2) | Economical cruise speed |
| Cost_USD | BIGINT | Construction cost in USD (inflation-adjusted where noted) |
| Build_Time_Months | INT | Construction time in months |
| Refit_Cost_USD | BIGINT | Cost to refit from base hull to this variant (NULL if base hull) |
| Refit_Time_Months | INT | Time to refit from base hull to this variant (NULL if base hull) |
| Modded | TINYINT | 0 = historical, 1 = fictional/generated |
| Notes | TEXT | Design features, modernizations, operational history |

**Total Entries**: 0 ships
**Planned Coverage**: 1890-2025 (Pre-dreadnought through modern)

---

### Modular Ship Building System Fields

**NEW**: The following fields support modular ship construction gameplay where players build hulls and install components.

#### Hull Variants
- **Hull_Variant**: Identifies different configurations of the same class (e.g., "Base 1920", "1943 Rebuild", "1984 Refit")
- **Base_Hull_ID**: Links variant hulls to their original hull (NULL for base hulls)
- **Refit_Cost_USD**: Cost to convert from base hull to this variant (NULL for base hulls)
- **Refit_Time_Months**: Time required to refit from base hull to this variant (NULL for base hulls)

Example: Tennessee-class has THREE hull variants:
1. Tennessee-class (Base 1920) - Base_Hull_ID: NULL
2. Tennessee-class (1943 Rebuild) - Base_Hull_ID: points to Tennessee 1920, wider beam, different hardpoints
3. Both share Ship_Class "Tennessee-class" but have different Hull_Variant values

#### Hardpoint System
Hardpoints define what weapons/systems can be mounted and where:

- **Hardpoint_Main_Battery**: Description of main battery mounting points (e.g., "4× Heavy-14in Centerline, 2 Fore/2 Aft")
- **Hardpoint_Main_Count**: Number of main battery hardpoints (e.g., 4 turret positions)
- **Hardpoint_Main_Size**: Hardpoint size category (e.g., "Heavy-14in", "XHeavy-16in", "Medium-12in")

- **Hardpoint_Secondary_Battery**: Secondary gun mounting points
- **Hardpoint_Secondary_Count**: Number of secondary hardpoints
- **Hardpoint_Secondary_Size**: Secondary hardpoint size (e.g., "DP-5in", "Casemate-5in")

- **Hardpoint_AA_Light**: Light AA mounting points (40mm, 3in, etc.)
- **Hardpoint_AA_Light_Count**: Number of light AA hardpoints
- **Hardpoint_AA_Close**: Close-in AA mounting points (20mm, Phalanx, etc.)
- **Hardpoint_AA_Close_Count**: Number of close-in AA hardpoints

- **Hardpoint_Torpedo**: Torpedo tube mounting points
- **Hardpoint_Torpedo_Count**: Number of torpedo tube positions

- **Hardpoint_Missile_VLS**: Vertical Launch System positions
- **Hardpoint_Missile_VLS_Cells**: Total VLS cells available
- **Hardpoint_Missile_Launcher**: Dedicated missile launcher positions (Harpoon, Tomahawk ABL, etc.)
- **Hardpoint_Missile_Launcher_Count**: Number of missile launcher hardpoints

**Hardpoint Size Categories**:
- **XHeavy-16in+**: 16"/50 and larger turrets (Iowa, Montana, Yamato)
- **Heavy-14in**: 14"/45-50 turrets (Pennsylvania, North Carolina, King George V)
- **Heavy-13in**: 13"/35-45 turrets (Indiana, Nevada early)
- **Medium-12in**: 12"/45-50 turrets (Wyoming, pre-dreadnoughts)
- **Light-8in-10in**: 8-10" cruiser main batteries
- **DP-5in**: Dual-purpose 5"/38 and similar
- **Casemate-5in**: Fixed casemate 5"/51 and similar
- **Quad-40mm**: Bofors quad mounts
- **Twin-40mm**: Bofors twin mounts
- **Single-20mm**: Oerlikon single mounts

#### Module Slots
Module slots define what systems can be installed:

**Propulsion Modules**:
- **Module_Slot_Engine_Boilers**: Number of boiler positions (steam ships)
- **Module_Slot_Engine_Turbines**: Number of turbine/engine positions
- **Module_Slot_Engine_Reactors**: Number of reactor positions (nuclear ships)

**Fire Control & Sensors**:
- **Module_Slot_FCS_Directors**: Number of fire control director positions (Mk 37, Mk 38, etc.)
- **Module_Slot_Radar_Masts**: Number of rotating radar mast positions (SK, SPS-49, etc.)
- **Module_Slot_Radar_Arrays**: Number of fixed phased array positions (SPY-1, SPY-6)
- **Module_Slot_Sonar_Bow**: Bow-mounted sonar dome (0 or 1)
- **Module_Slot_Sonar_Towed**: Towed array sonar (0 or 1)

**Aviation**:
- **Module_Slot_Helicopter_Deck**: Number of helicopter landing spots
- **Module_Slot_Catapults**: Number of aircraft catapults (carriers)

#### Internal Capacity (Tarkov-Style Inventory)
Magazine and storage capacities for inventory management:

**Ammunition Storage**:
- **Magazine_Capacity_Main_TONS**: Main battery magazine capacity in tons
- **Magazine_Capacity_Secondary_TONS**: Secondary battery magazine capacity
- **Magazine_Capacity_AA_TONS**: AA ammunition storage
- **Magazine_Capacity_Torpedo_TONS**: Torpedo storage capacity
- **Magazine_Capacity_Missile_TONS**: Missile magazine capacity
- **Magazine_Capacity_Total_TONS**: Total ordnance capacity (sum of above)

**Consumables Storage**:
- **Fuel_Capacity_TONS**: Fuel oil/diesel capacity
- **Supply_Hold_TONS**: Food, spare parts, consumables
- **Aviation_Fuel_TONS**: Aviation gasoline/JP-5 (carriers)

#### Crew Management
Min/Normal/Max crew levels for gameplay:

- **Crew_[Type]_Min**: Minimum crew to operate ship (skeleton crew)
- **Crew_[Type]**: Normal operational crew complement
- **Crew_[Type]_Max**: Maximum crew capacity (quarters limit)

Example: Tennessee 1943 Rebuild
- Min: 1,500 (can operate with reduced crew)
- Normal: 2,200 (full effectiveness)
- Max: 2,400 (can house extra personnel)

#### Build & Refit Mechanics
- **Build_Time_Months**: Time to construct new hull from scratch
- **Refit_Cost_USD**: Cost to upgrade from base hull to this variant
- **Refit_Time_Months**: Time to refit existing ship to this configuration

**Refit Example**:
- Tennessee (Base 1920): Build_Time=48 months, Cost=$15M
- Tennessee (1943 Rebuild): Build_Time=48 months (if new), Refit_Time=18 months (if upgrading), Refit_Cost=$45M

Players can either:
1. Build new ship in 1943 configuration (48 months, full cost)
2. Refit existing 1920 hull (18 months, refit cost, reuse main turrets)

---

**ID Allocation by Type and Nation**:

### Battleships (BB): 10000-10999
- USA: 10000-10099
- British: 10100-10199
- German: 10200-10249
- Japanese: 10250-10299
- French: 10300-10349
- Italian: 10350-10399
- Soviet/Russian: 10400-10449
- Other: 10450-10499
- Fictional: 10500-10999

### Aircraft Carriers (CV/CVN): 11000-11999
- USA Fleet Carriers: 11000-11099
- USA Light Carriers: 11100-11149
- USA Escort Carriers: 11150-11199
- USA Modern/Nuclear: 11200-11249
- British: 11250-11349
- Japanese: 11350-11399
- French: 11400-11424
- Soviet/Russian: 11425-11474
- Chinese: 11475-11499
- Other: 11500-11549
- Fictional: 11550-11999

### Heavy Cruisers (CA): 12000-12499
- USA: 12000-12099
- British: 12100-12149
- German: 12150-12174
- Japanese: 12175-12199
- Italian: 12200-12224
- French: 12225-12249
- Other: 12250-12299
- Fictional: 12300-12499

### Light Cruisers (CL): 12500-12999
- USA: 12500-12599
- British: 12600-12649
- German: 12650-12674
- Japanese: 12675-12699
- Soviet: 12700-12724
- Other: 12725-12799
- Fictional: 12800-12999

### Destroyers (DD/DDG): 13000-14999
- USA WWII: 13000-13199
- USA Modern: 13200-13299
- British: 13300-13399
- German: 13400-13449
- Japanese: 13450-13499
- Soviet/Russian: 13500-13599
- French: 13600-13649
- Chinese: 13650-13699
- Other: 13700-13799
- Fictional: 13800-14999

### Submarines (SS/SSN/SSBN): 15000-16999
- USA Diesel: 15000-15099
- USA Nuclear Attack: 15100-15199
- USA Ballistic Missile: 15200-15249
- British: 15250-15349
- German: 15350-15449
- Japanese: 15450-15499
- Soviet/Russian Diesel: 15500-15599
- Soviet/Russian Nuclear: 15600-15699
- Chinese: 15700-15749
- Other: 15750-15849
- Fictional: 15850-16999

### Frigates/Corvettes (FF/FFG): 17000-17999
- USA: 17000-17099
- British: 17100-17149
- German: 17150-17174
- French: 17175-17199
- Soviet/Russian: 17200-17249
- Chinese: 17250-17299
- Other: 17300-17399
- Fictional: 17400-17999

### Amphibious/Support (LHA/LHD/LPD/AO/etc.): 18000-18999
- USA Amphibious: 18000-18099
- USA Support: 18100-18149
- British: 18150-18199
- Soviet/Russian: 18200-18249
- Other: 18250-18349
- Fictional: 18350-18999

| Ship_ID | Country | Ship_Name | Ship_Class | Hull_Variant | Base_Hull_ID | Hull_Number | Ship_Type | Ship_Type_Full | Subtype | Year_Laid_Down | Year_Launched | Year_Commissioned | Year_Decommissioned | Year_Fate | Fate | Displacement_Standard_TONS | Displacement_Full_TONS | Length_Overall_FT | Length_Waterline_FT | Beam_FT | Draft_FT | Turning_Radius_YD | Crew_Officers_Min | Crew_Enlisted_Min | Crew_Total_Min | Crew_Officers | Crew_Enlisted | Crew_Total | Crew_Officers_Max | Crew_Enlisted_Max | Crew_Total_Max | Hardpoint_Main_Battery | Hardpoint_Main_Count | Hardpoint_Main_Size | Hardpoint_Secondary_Battery | Hardpoint_Secondary_Count | Hardpoint_Secondary_Size | Hardpoint_AA_Light | Hardpoint_AA_Light_Count | Hardpoint_AA_Close | Hardpoint_AA_Close_Count | Hardpoint_Torpedo | Hardpoint_Torpedo_Count | Hardpoint_Missile_VLS | Hardpoint_Missile_VLS_Cells | Hardpoint_Missile_Launcher | Hardpoint_Missile_Launcher_Count | Module_Slot_Engine_Boilers | Module_Slot_Engine_Turbines | Module_Slot_Engine_Reactors | Module_Slot_FCS_Directors | Module_Slot_Radar_Masts | Module_Slot_Radar_Arrays | Module_Slot_Sonar_Bow | Module_Slot_Sonar_Towed | Module_Slot_Helicopter_Deck | Module_Slot_Catapults | Magazine_Capacity_Main_TONS | Magazine_Capacity_Secondary_TONS | Magazine_Capacity_AA_TONS | Magazine_Capacity_Torpedo_TONS | Magazine_Capacity_Missile_TONS | Magazine_Capacity_Total_TONS | Fuel_Capacity_TONS | Supply_Hold_TONS | Aviation_Fuel_TONS | Propulsion_Type | Max_Speed_KTS | Range_NM | Cruise_Speed_KTS | Cost_USD | Build_Time_Months | Refit_Cost_USD | Refit_Time_Months | Modded | Notes |
|---------|---------|-----------|------------|--------------|--------------|-------------|-----------|----------------|---------|----------------|---------------|-------------------|---------------------|-----------|------|---------------------------|------------------------|-------------------|---------------------|---------|----------|-------------------|-------------------|-------------------|----------------|---------------|---------------|------------|-------------------|-------------------|----------------|------------------------|---------------------|---------------------|-----------------------------|---------------------------|--------------------------|-------------------|--------------------------|-------------------|--------------------------|-------------------|-------------------------|----------------------|----------------------------|----------------------------|----------------------------------|----------------------------|-----------------------------|-----------------------------|---------------------------|-------------------------|--------------------------|----------------------|-------------------------|-----------------------------|-----------------------|-----------------------------|----------------------------------|---------------------------|-------------------------------|-------------------------------|------------------------------|--------------------|------------------|--------------------|-----------------|---------------|----------|------------------|----------|-------------------|----------------|-------------------|--------|-------|
| 12500 | USA | USS Chester | Chester-class | Base 1908 | NULL | CL-1 | CL | Light Cruiser | Protected Cruiser | NULL | NULL | 1908 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 1500000 | 24 | NULL | NULL | 0 | First US scout cruiser. 3 ships built. FREE starting ship for tutorial. |
| 12501 | USA | USS Omaha | Omaha-class | Base 1923 | NULL | CL-4 | CL | Light Cruiser | Scout Cruiser | NULL | NULL | 1923 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12×6" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | 35 | NULL | NULL | 7000000 | 36 | NULL | NULL | 0 | WWI-era scout cruiser. 35 kts, 12×6" guns. 10 ships built. FREE starting ship. |
| 12000 | USA | USS Pensacola | Pensacola-class | Base 1930 | NULL | CA-24 | CA | Heavy Cruiser | Treaty Heavy Cruiser | NULL | NULL | 1930 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 10×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 12000000 | 48 | NULL | NULL | 0 | First US 8" treaty heavy cruiser. 10×8" guns, lightly armored. 2 ships: CA-24/25. |
| 12001 | USA | USS Northampton | Northampton-class | Base 1930 | NULL | CA-26 | CA | Heavy Cruiser | Treaty Heavy Cruiser | NULL | NULL | 1930 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | 32.5 | NULL | NULL | 11000000 | 48 | NULL | NULL | 0 | Alternative treaty heavy cruiser. 9×8" guns, lighter armor, 32.5 kts. 6 ships. |
| 12502 | USA | USS Brooklyn | Brooklyn-class | Base 1937 | NULL | CL-40 | CL | Light Cruiser | Treaty Light Cruiser | NULL | NULL | 1937 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 15×6" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 14000000 | 48 | NULL | NULL | 0 | Maximum 6" firepower. 15×6" guns, treaty light cruiser, highest ROF. 7 ships. |
| 12002 | USA | USS Portland | Portland-class | Base 1933 | NULL | CA-33 | CA | Heavy Cruiser | Treaty Heavy Cruiser | NULL | NULL | 1933 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 13000000 | 54 | NULL | NULL | 0 | Refined heavy cruiser. 9×8" guns, improved armor over Northampton. 2 ships. |
| 12503 | USA | USS Atlanta | Atlanta-class | Base 1941 | NULL | CLAA-51 | CLAA | Light Cruiser | AA Cruiser | NULL | NULL | 1941 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16×5" DP guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 17000000 | 42 | NULL | NULL | 0 | AA specialist cruiser. 16×5" DP guns, +100% AA effectiveness. 11 ships. |
| 12504 | USA | USS St. Louis | St. Louis-class | Base 1939 | NULL | CL-49 | CL | Light Cruiser | Treaty Light Cruiser | NULL | NULL | 1939 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 15×6" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 15000000 | 48 | NULL | NULL | 0 | Brooklyn subclass. 15×6" guns with improved AA. 2 ships. |
| 12003 | USA | USS New Orleans | New Orleans-class | Base 1934 | NULL | CA-32 | CA | Heavy Cruiser | Treaty Heavy Cruiser | NULL | NULL | 1934 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 15000000 | 60 | NULL | NULL | 0 | Refined treaty design. 9×8" guns, all-or-nothing armor. Best treaty-compliant heavy. 7 ships. |
| 12004 | USA | USS Wichita | Wichita-class | Base 1939 | NULL | CA-45 | CA | Heavy Cruiser | Pre-War Heavy Cruiser | NULL | NULL | 1939 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 17000000 | 60 | NULL | NULL | 0 | Bridge to WWII. Brooklyn hull with 9×8" guns. Unique hybrid design. 1 ship. |
| 12505 | USA | USS Cleveland | Cleveland-class | Base 1942 | NULL | CL-55 | CL | Light Cruiser | WWII Light Cruiser | NULL | NULL | 1942 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12×6" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 28000000 | 36 | NULL | NULL | 0 | Mass production CL. 12×6" guns. Largest CL class with 27 ships built. |
| 12506 | USA | USS Oakland | Oakland-class | Base 1943 | NULL | CLAA-95 | CLAA | Light Cruiser | AA Cruiser | NULL | NULL | 1943 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12×5" DP guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 21000000 | 42 | NULL | NULL | 0 | Improved AA cruiser. 12×5" DP guns with radar. 4 ships. |
| 12005 | USA | USS Baltimore | Baltimore-class | Base 1943 | NULL | CA-68 | CA | Heavy Cruiser | WWII Heavy Cruiser | NULL | NULL | 1943 | NULL | NULL | NULL | NULL | 14000 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 37000000 | 60 | NULL | NULL | 0 | Peak WWII heavy cruiser. 9×8" guns, best armor. Ultimate gun CA. 14 ships. |
| 12006 | USA | USS Oregon City | Oregon City-class | Base 1946 | NULL | CA-122 | CA | Heavy Cruiser | WWII Heavy Cruiser | NULL | NULL | 1946 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 40000000 | 60 | NULL | NULL | 0 | Improved Baltimore. 9×8" guns with single funnel. Refined CA. 4 ships. |
| 12507 | USA | USS Fargo | Fargo-class | Base 1945 | NULL | CL-106 | CL | Light Cruiser | Post-War Light Cruiser | NULL | NULL | 1945 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12×6" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 32000000 | 36 | NULL | NULL | 0 | Improved Cleveland. 12×6" guns with single funnel. 2 ships. |
| 12508 | USA | USS Juneau | Juneau-class | Base 1946 | NULL | CLAA-119 | CLAA | Light Cruiser | AA Cruiser | NULL | NULL | 1946 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12×5" DP guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 24000000 | 42 | NULL | NULL | 0 | Late-war AA cruiser. 12×5" DP guns with improved systems. 3 ships, Korean War. |
| 12007 | USA | USS Des Moines | Des Moines-class | Base 1948 | NULL | CA-134 | CA | Heavy Cruiser | Ultimate Gun Cruiser | NULL | NULL | 1948 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 9×8" auto-loading | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 47000000 | 66 | NULL | NULL | 0 | Ultimate gun cruiser. 9×8" auto-loading guns, 8-10 rpm per gun. Pinnacle gun CA. 3 ships. |
| 12509 | USA | USS Worcester | Worcester-class | Base 1948 | NULL | CL-144 | CL | Light Cruiser | Ultimate Light Cruiser | NULL | NULL | 1948 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12×6" rapid-fire auto | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 45000000 | 66 | NULL | NULL | 0 | Ultimate light gun cruiser. 12×6" rapid-fire auto-loading, 12 rpm. 2 ships. |
| 12008 | USA | USS Boston | Boston-class | Terrier SAM 1955 | 12005 | CAG-1 | CAG | Guided Missile Cruiser | First Missile Cruiser | NULL | NULL | 1955 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×8" guns | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 10000000 | 18 | 0 | First missile CA conversion. Baltimore hull + Terrier SAM. 6×8" guns + missiles. 3 conversions. |
| 12510 | USA | USS Galveston | Galveston-class | Talos SAM 1958 | 12505 | CLG-3 | CLG | Guided Missile Cruiser | Missile Light Cruiser | NULL | NULL | 1958 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×6" guns | NULL | NULL | Talos SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Talos launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 9000000 | 18 | 0 | Missile CL conversion. Cleveland hull + Talos SAM. 6×6" guns + missiles. 3 conversions. |
| 12511 | USA | USS Providence | Providence-class | Terrier SAM 1959 | 12505 | CLG-6 | CLG | Guided Missile Cruiser | Missile Light Cruiser | NULL | NULL | 1959 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 3×6" guns | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 9000000 | 18 | 0 | Improved missile CL. Cleveland hull + Terrier SAM. 3×6" guns + missiles. 3 conversions. |
| 12512 | USA | USS Norfolk | Norfolk-class | Base 1953 | NULL | DL-1 | DL | Destroyer Leader | Frigate/Light Cruiser Hybrid | NULL | NULL | 1953 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 8×3" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 32000000 | 36 | NULL | NULL | 0 | Destroyer leader/frigate hybrid. 8×3" guns, ASW + AA. Large DD/light cruiser. 1 ship. |
| 12009 | USA | USS Albany | Albany-class | All-Missile 1962 | 12005 | CG-10 | CG | Guided Missile Cruiser | Heavy Missile Cruiser | NULL | NULL | 1962 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Talos+Tartar SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Talos+Tartar | 188 | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 15000000 | 24 | 0 | Extensive conversion. Baltimore hull, 0 guns. 104 Talos + 84 Tartar missiles. All-missile CG. 3 conversions. |
| 12010 | USA | USS Long Beach | Long Beach CGN-9 | Base 1961 | NULL | CGN-9 | CGN | Guided Missile Cruiser (Nuclear) | First Nuclear Cruiser | NULL | NULL | 1961 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Talos+Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Talos+Terrier | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 350000000 | 60 | NULL | NULL | 0 | First nuclear cruiser. 2×C1W reactors, unlimited range. Only nuclear CGN. UNIQUE. 1 ship. |
| 12011 | USA | USS Leahy | Leahy-class | Base 1962 | NULL | CG-16 | CG | Guided Missile Cruiser | First Purpose-Built CG | NULL | NULL | 1962 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 85000000 | 48 | NULL | NULL | 0 | First purpose-built guided missile cruiser. Terrier SAM. 9 ships. |
| 12012 | USA | USS Bainbridge | Bainbridge CGN-25 | Base 1962 | NULL | CGN-25 | CGN | Guided Missile Cruiser (Nuclear) | Nuclear Leahy | NULL | NULL | 1962 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier launchers | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 165000000 | 54 | NULL | NULL | 0 | Nuclear-powered Leahy variant. 2×D2G reactors. UNIQUE. 1 ship. |
| 12013 | USA | USS Belknap | Belknap-class | Base 1964 | NULL | CG-26 | CG | Guided Missile Cruiser | Improved CG | NULL | NULL | 1964 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 1×5" gun | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 95000000 | 48 | NULL | NULL | 0 | Improved missile cruiser. 1×5" gun + Terrier SAM. 9 ships. |
| 12014 | USA | USS Truxtun | Truxtun CGN-35 | Base 1967 | NULL | CGN-35 | CGN | Guided Missile Cruiser (Nuclear) | Nuclear Belknap | NULL | NULL | 1967 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 1×5" gun | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier launchers | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 190000000 | 54 | NULL | NULL | 0 | Nuclear Belknap variant. 2×D2G reactors. UNIQUE. 1 ship. |
| 12015 | USA | USS Chicago | Chicago CAG-136 | Talos SAM 1964 | 12005 | CAG-136 | CAG | Guided Missile Cruiser | Late Missile Conversion | NULL | NULL | 1964 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×8" guns | NULL | NULL | Talos SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Talos launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 11000000 | 18 | 0 | Late missile conversion. Baltimore hull + Talos SAM. 6×8" guns + missiles. 1 conversion. |
| 12016 | USA | USS California | California-class | Base 1974 | NULL | CGN-36 | CGN | Guided Missile Cruiser (Nuclear) | Nuclear Production CG | NULL | NULL | 1974 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard SM-2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard launchers | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 400000000 | 66 | NULL | NULL | 0 | Nuclear production cruiser. 2×D2G reactors, Standard SM-2. 2 ships. |
| 12017 | USA | USS Virginia | Virginia-class | Base 1976 | NULL | CGN-38 | CGN | Guided Missile Cruiser (Nuclear) | Improved Nuclear CG | NULL | NULL | 1976 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard SM-2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard launchers | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 450000000 | 72 | NULL | NULL | 0 | Improved nuclear cruiser. 2×D2G reactors, Aegis-ready. 4 ships. |
| 12018 | USA | USS Leahy (NTU) | Leahy-class (NTU) | NTU Upgrade 1980 | 12011 | CG-16 | CG | Guided Missile Cruiser | Upgraded Missile Cruiser | NULL | NULL | 1980 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard SM-2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 8000000 | 12 | 0 | New Threat Upgrade. Standard SM-2 missiles. Modernization refit. |
| 12019 | USA | USS Belknap (NTU) | Belknap-class (NTU) | NTU Upgrade 1985 | 12013 | CG-26 | CG | Guided Missile Cruiser | Upgraded Missile Cruiser | NULL | NULL | 1985 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 1×5" gun | NULL | NULL | Standard SM-2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard launchers | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 8500000 | 12 | 0 | New Threat Upgrade. 1×5" gun + Standard SM-2 missiles. Modernization refit. |
| 12020 | USA | USS Ticonderoga | Ticonderoga-class (Early) CG-47/48 | Mk 26 Aegis 1983 | NULL | CG-47 | CG | Guided Missile Cruiser | Early Aegis Cruiser | NULL | NULL | 1983 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 26 launchers | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 800000000 | 78 | NULL | NULL | 0 | Early Aegis cruiser. Mk 26 twin launchers, SPY-1A radar. CG-47/48. |
| 12021 | USA | USS Vincennes | Ticonderoga-class (Baseline 1) CG-49-51 | Mk 26 Aegis B1 1985 | NULL | CG-49 | CG | Guided Missile Cruiser | Aegis Baseline 1 | NULL | NULL | 1985 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 26 launchers | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 850000000 | 78 | NULL | NULL | 0 | Improved early Aegis. Better systems, still Mk 26 launchers. CG-49/50/51. |
| 12022 | USA | USS Bunker Hill | Ticonderoga-class (Baseline 2) CG-52-58 | Mk 26 Aegis B2 1986 | NULL | CG-52 | CG | Guided Missile Cruiser | Aegis Baseline 2 | NULL | NULL | 1986 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 26 launchers | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 900000000 | 78 | NULL | NULL | 0 | Advanced radar Aegis. SPY-1B radar upgrade, Mk 26 launchers. CG-52-58. |
| 12023 | USA | USS Virginia (Modernized) | Virginia-class CGN (Modernized) | Aegis-Ready 1988 | 12017 | CGN-38 | CGN | Guided Missile Cruiser (Nuclear) | Modernized Nuclear CG | NULL | NULL | 1988 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard+Tomahawk | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard launchers | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 0 | 0 | 25000000 | 24 | 0 | Full modernization. Aegis-ready systems, Tomahawk. Late 1980s refit. |
| 12024 | USA | Strike Cruiser | Strike Cruiser CGN | Concept 1975 | NULL | CGN | CGN | Guided Missile Cruiser (Nuclear) | Strike Cruiser (Paper) | NULL | NULL | 1975 | NULL | NULL | Cancelled | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Aegis+Tomahawk | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Aegis+Tomahawk | NULL | NULL | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 900000000 | 84 | NULL | NULL | 1 | Cancelled design 1976. Aegis nuclear strike cruiser. Paper ship, -10% reliability. |
| 12025 | USA | USS Princeton | Ticonderoga-class (Baseline 3) CG-59-64 | VLS Aegis 1988 | NULL | CG-59 | CG | Guided Missile Cruiser | Aegis VLS Early | NULL | NULL | 1988 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 122 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 950000000 | 78 | NULL | NULL | 0 | First VLS Aegis cruiser. Mk 41 VLS with 122 cells. CG-59-64. |
| 12026 | USA | USS Chosin | Ticonderoga-class (Baseline 4) CG-65-73 | VLS Ultimate 1990 | NULL | CG-65 | CG | Guided Missile Cruiser | Ultimate Aegis Cruiser | NULL | NULL | 1990 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 122 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1000000000 | 78 | NULL | NULL | 0 | Ultimate production Aegis cruiser. Best systems, VLS 122 cells. CG-65-73. |
| 12027 | USA | CG(X) | CG(X) Future Cruiser | Concept 2020 | NULL | CG(X) | CG | Guided Missile Cruiser | Future Cruiser (Paper) | NULL | NULL | 2020 | NULL | NULL | Cancelled | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Next-gen systems | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Next-gen VLS | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3000000000 | 96 | NULL | NULL | 1 | Next-gen cruiser concept. 2020s tech, cancelled. Paper design, -10% reliability. |
| 13000 | USA | USS Bainbridge | Bainbridge-class | Base 1902 | NULL | DD-1 | DD | Destroyer | Torpedo Boat Destroyer | NULL | NULL | 1902 | NULL | NULL | NULL | 420 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 2×3" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 500000 | 18 | NULL | NULL | 0 | First US destroyer. 420 tons, 2×3" guns. -60% armor, +2 kts. FREE starting DD. 5 ships. |
| 13001 | USA | USS Smith | Smith-class | Base 1909 | NULL | DD-17 | DD | Destroyer | Early Destroyer | NULL | NULL | 1909 | NULL | NULL | NULL | 700 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×3" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 800000 | 24 | NULL | NULL | 0 | Better starting DD. 700 tons, 5×3" guns. +3 kts. FREE starting option. 5 ships. |
| 13002 | USA | USS Paulding | Paulding-class | Base 1910 | NULL | DD-22 | DD | Destroyer | Pre-WWI Destroyer | NULL | NULL | 1910 | NULL | NULL | NULL | 742 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×3" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 950000 | 24 | NULL | NULL | 0 | Early fleet DD. 742 tons, 5×3" guns, torpedoes. 21 ships. |
| 13003 | USA | USS Cassin | Cassin-class | Base 1913 | NULL | DD-43 | DD | Destroyer | Pre-WWI Destroyer | NULL | NULL | 1913 | NULL | NULL | NULL | 1010 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 4×3" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1100000 | 30 | NULL | NULL | 0 | Improved destroyer. 1,010 tons, oil-fired, improved range. 8 ships. |
| 13004 | USA | USS Sampson | Sampson-class | Base 1916 | NULL | DD-63 | DD | Destroyer | Pre-WWI Destroyer | NULL | NULL | 1916 | NULL | NULL | NULL | 1200 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 4×4" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | 29 | NULL | NULL | 1300000 | 30 | NULL | NULL | 0 | Final pre-WWI DD. 1,200 tons, 4×4" guns, 29 kts. Pre-WWI peak. 6 ships. |
| 13005 | USA | USS Caldwell | Caldwell-class | Base 1917 | NULL | DD-69 | DD | Destroyer | WWI Destroyer | NULL | NULL | 1917 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×4" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1500000 | 12 | NULL | NULL | 0 | First flush-deck DD. 6×4" guns. WWI design. 6 ships, first flush-deck. |
| 13006 | USA | USS Wickes | Wickes-class | Base 1918 | NULL | DD-75 | DD | Destroyer | WWI Four-Stacker | NULL | NULL | 1918 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 4×4" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1600000 | 9 | NULL | NULL | 0 | Mass production WWI DD. Four-stacker. 111 ships built. Largest DD class WWI. |
| 13007 | USA | USS Clemson | Clemson-class | Base 1919 | NULL | DD-186 | DD | Destroyer | WWI Four-Stacker | NULL | NULL | 1919 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 4×4" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1700000 | 9 | NULL | NULL | 0 | Improved Wickes. Four-stacker, 156 ships. Largest US DD class. More fuel. |
| 13008 | USA | USS Manley | Wickes-class (APD) | APD Conversion 1943 | 13006 | APD-1 | APD | High-Speed Transport | Fast Troop Transport | NULL | NULL | 1943 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 2000000 | 6 | 0 | High-speed transport conversion. Fast troop transport, 200 troops. WWII conversion. |
| 13009 | USA | USS Farragut | Farragut-class | Base 1934 | NULL | DD-348 | DD | Destroyer | Interwar Destroyer | NULL | NULL | 1934 | NULL | NULL | NULL | 1400 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3800000 | 36 | NULL | NULL | 0 | First enclosed guns DD. 1,400 tons, enclosed 5" guns. Interwar. 8 ships. |
| 13010 | USA | USS Porter | Porter-class | Base 1935 | NULL | DD-356 | DD | Destroyer | Destroyer Leader | NULL | NULL | 1935 | NULL | NULL | NULL | 1850 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 8×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 5500000 | 42 | NULL | NULL | 0 | Destroyer leader. 1,850 tons, 8×5" guns. Large DD leader. 8 ships. |
| 13011 | USA | USS Mahan | Mahan-class | Base 1936 | NULL | DD-364 | DD | Destroyer | Interwar Destroyer | NULL | NULL | 1936 | NULL | NULL | NULL | 1500 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 12 torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 4000000 | 36 | NULL | NULL | 0 | More torpedoes DD. 12 torpedoes, 1,500 tons. Torpedo focus. 18 ships. |
| 13012 | USA | USS Gridley | Gridley-class | Base 1937 | NULL | DD-380 | DD | Destroyer | Interwar Destroyer | NULL | NULL | 1937 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 4200000 | 36 | NULL | NULL | 0 | Maximum torpedoes DD. 16 torpedoes, experimental. Torpedo focus. 4 ships. |
| 13013 | USA | USS Bagley | Bagley-class | Base 1937 | NULL | DD-386 | DD | Destroyer | Interwar Destroyer | NULL | NULL | 1937 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 4100000 | 36 | NULL | NULL | 0 | Balanced design DD. 16 torpedoes, balanced guns + torpedoes. 8 ships. |
| 13014 | USA | USS Benham | Benham-class | Base 1939 | NULL | DD-397 | DD | Destroyer | Pre-WWII Destroyer | NULL | NULL | 1939 | NULL | NULL | NULL | 1850 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 4500000 | 42 | NULL | NULL | 0 | Refined pre-war DD. 1,850 tons, refined design. 10 ships. |
| 13015 | USA | USS Sims | Sims-class | Base 1939 | NULL | DD-409 | DD | Destroyer | Pre-WWII Destroyer | NULL | NULL | 1939 | NULL | NULL | NULL | 1570 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 4300000 | 42 | NULL | NULL | 0 | Alternative pre-war DD. 1,570 tons, lighter, faster. 12 ships. |
| 13016 | USA | USS Benson | Benson-class | Base 1940 | NULL | DD-421 | DD | Destroyer | Pre-WWII Destroyer | NULL | NULL | 1940 | NULL | NULL | NULL | 1630 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 5000000 | 42 | NULL | NULL | 0 | Standard pre-war DD. 1,630 tons, 5×5" guns. Standard design. 30 ships. |
| 13017 | USA | USS Gleaves | Gleaves-class | Base 1940 | NULL | DD-423 | DD | Destroyer | Pre-WWII Destroyer | NULL | NULL | 1940 | NULL | NULL | NULL | 1630 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 5100000 | 42 | NULL | NULL | 0 | Benson variant DD. Benson derivative, similar to Benson. 66 ships. |
| 13018 | USA | USS Bristol | Bristol-class | Base 1941 | NULL | DD-453 | DD | Destroyer | Pre-WWII Destroyer | NULL | NULL | 1941 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 5200000 | 42 | NULL | NULL | 0 | Benson subclass. Final pre-war design, last pre-war variant. 32 ships. |
| 13019 | USA | USS Fletcher | Fletcher-class | Base 1942 | NULL | DD-445 | DD | Destroyer | WWII Fleet Destroyer | NULL | NULL | 1942 | NULL | NULL | NULL | 2100 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 6000000 | 12 | NULL | NULL | 0 | Signature WWII DD. 2,100 tons, 5×5" guns. Most successful DD class. 175 ships. |
| 13020 | USA | USS Fletcher (FRAM I) | Fletcher-class (FRAM I) | FRAM 1960 | 13019 | DD-445 | DD | Destroyer | FRAM Modernized Destroyer | NULL | NULL | 1960 | NULL | NULL | NULL | 2100 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 5×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 5000000 | 12 | 0 | FRAM modernization. ASW + electronics upgrade. Modernized DD. 1960s. |
| 13021 | USA | USS Allen M. Sumner | Allen M. Sumner-class | Base 1944 | NULL | DD-692 | DD | Destroyer | WWII Heavy Destroyer | NULL | NULL | 1944 | NULL | NULL | NULL | 2200 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 7500000 | 15 | NULL | NULL | 0 | Six-gun DD. 2,200 tons, 6×5" guns in 3 twins. Heavy WWII DD. 67 ships. |
| 13022 | USA | USS Gearing | Gearing-class | Base 1945 | NULL | DD-710 | DD | Destroyer | WWII Ultimate Destroyer | NULL | NULL | 1945 | NULL | NULL | NULL | 2425 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Torpedoes | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 8000000 | 18 | NULL | NULL | 0 | Lengthened Sumner. 2,425 tons, 6×5" guns. Ultimate gun DD, more fuel. 98 ships. |
| 13023 | USA | USS Gearing (FRAM I) | Gearing-class (FRAM I) | FRAM 1961 | 13022 | DD-710 | DD | Destroyer | FRAM Modernized Heavy DD | NULL | NULL | 1961 | NULL | NULL | NULL | 2425 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6×5" guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 6000000 | 12 | 0 | Full FRAM upgrade. Full ASW modernization. Modernized heavy DD. Major mod. |
| 13024 | USA | USS Gearing (DDR) | Gearing-class (DDR) | Radar Picket 1950 | 13022 | DDR-710 | DDR | Radar Picket Destroyer | Radar Picket | NULL | NULL | 1950 | NULL | NULL | NULL | 2425 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 3000000 | 6 | 0 | Radar picket conversion. Early warning radar DD. Long-range radar. |
| 13200 | USA | USS Forrest Sherman | Forrest Sherman-class | Base 1955 | NULL | DD-931 | DD | Destroyer | First Post-War Destroyer | NULL | NULL | 1955 | NULL | NULL | NULL | 2800 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Modern 3"/50 guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 18000000 | 36 | NULL | NULL | 0 | First post-war DD. 2,800 tons, modern 3"/50 guns. Post-war design. 18 ships. |
| 13201 | USA | USS Barry | Forrest Sherman-class DDG | Tartar DDG 1967 | 13200 | DDG-933 | DDG | Guided Missile Destroyer | Missile Conversion | NULL | NULL | 1967 | NULL | NULL | NULL | 2800 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tartar SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tartar missiles | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 8000000 | 18 | 0 | Tartar conversion. 4 ships with Tartar missiles. Missile DD conversion. |
| 13202 | USA | USS Mitscher | Mitscher-class | Base 1953 | NULL | DL-2 | DL | Destroyer Leader | Large Destroyer Leader | NULL | NULL | 1953 | NULL | NULL | NULL | 3675 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 22000000 | 42 | NULL | NULL | 0 | Large destroyer leader. 3,675 tons. ASW + AA leader. Large DL. 4 ships. |
| 13203 | USA | USS Farragut | Farragut/Coontz-class | Base 1959 | NULL | DDG-37 | DDG | Guided Missile Destroyer | First Missile Destroyer | NULL | NULL | 1959 | NULL | NULL | NULL | 4700 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Terrier missiles | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 45000000 | 48 | NULL | NULL | 0 | First purpose DDG. 4,700 tons, Terrier SAM. Purpose missile DD. 10 ships. |
| 13204 | USA | USS Charles F. Adams | Charles F. Adams-class | Base 1960 | NULL | DDG-2 | DDG | Guided Missile Destroyer | Tartar Missile Destroyer | NULL | NULL | 1960 | NULL | NULL | NULL | 3370 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tartar SAM | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tartar missiles | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 38000000 | 42 | NULL | NULL | 0 | Tartar missile DD. 3,370 tons, Tartar SAM. Tartar DDG, most numerous. 23 ships. |
| 13205 | USA | USS Charles F. Adams (NTU) | Charles F. Adams-class (NTU) | NTU 1982 | 13204 | DDG-2 | DDG | Guided Missile Destroyer | Modernized Missile DD | NULL | NULL | 1982 | NULL | NULL | NULL | 3370 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard SM-1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 7000000 | 12 | 0 | New Threat Upgrade. Standard SM-1 upgrade. Modernized DDG. 1980s upgrade. |
| 13206 | USA | USS Spruance | Spruance-class | Base 1975 | NULL | DD-963 | DD | Destroyer | Gas Turbine Destroyer | NULL | NULL | 1975 | NULL | NULL | NULL | 5800 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | 4 | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Gas turbine | NULL | NULL | NULL | 125000000 | 36 | NULL | NULL | 0 | First gas turbine DD. 5,800 tons, 4×LM2500 turbines. Revolutionary propulsion. 31 ships. |
| 13207 | USA | USS Spruance (VLS) | Spruance-class (VLS) | VLS 1989 | 13206 | DD-963 | DD | Destroyer | VLS Upgraded Destroyer | NULL | NULL | 1989 | NULL | NULL | NULL | 5800 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 61 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Gas turbine | NULL | NULL | NULL | 0 | 0 | 10000000 | 18 | 0 | Vertical launch upgrade. Mk 41 VLS with 61 cells. VLS DD. 24 ships upgraded. |
| 13208 | USA | USS Kidd | Kidd-class | Base 1981 | NULL | DDG-993 | DDG | Guided Missile Destroyer | Modified Spruance | NULL | NULL | 1981 | NULL | NULL | NULL | 6200 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tartar/Standard | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Tartar/Standard | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Gas turbine | NULL | NULL | NULL | 135000000 | 36 | NULL | NULL | 0 | Modified Spruance DDG. 6,200 tons, Tartar/Standard. Heavy DDG. 4 ships, Iran order. |
| 13209 | USA | USS Arleigh Burke | Arleigh Burke-class (Flight I) DDG-51-71 | Flight I 1991 | NULL | DDG-51 | DDG | Guided Missile Destroyer | Early Aegis Destroyer | NULL | NULL | 1991 | NULL | NULL | NULL | 8300 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 90 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Gas turbine | NULL | NULL | NULL | 900000000 | 72 | NULL | NULL | 0 | First Aegis DD. 8,300 tons, SPY-1D Aegis, 90 VLS. Aegis DD. DDG-51-71, Flight I. |
| 13210 | USA | USS Ross | Arleigh Burke-class (Flight II) DDG-72-78 | Flight II 1998 | NULL | DDG-72 | DDG | Guided Missile Destroyer | Improved Aegis Destroyer | NULL | NULL | 1998 | NULL | NULL | NULL | 8300 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 90 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Gas turbine | NULL | NULL | NULL | 950000000 | 72 | NULL | NULL | 0 | Improved Aegis DD. Better electronics, upgraded systems. Improved. DDG-72-78, Flight II. |
| 13211 | USA | USS Oscar Austin | Arleigh Burke-class (Flight IIA) DDG-79-112 | Flight IIA 2000 | NULL | DDG-79 | DDG | Guided Missile Destroyer | Aegis with Helo | NULL | NULL | 2000 | NULL | NULL | NULL | 9200 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 96 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 2 | 0 | NULL | NULL | Gas turbine | NULL | NULL | NULL | 1000000000 | 72 | NULL | NULL | 0 | Helo hangar added. 9,200 tons, helo hangar, 96 VLS. Ultimate production DDG. DDG-79-112. |
| 13212 | USA | USS John Finn | Arleigh Burke-class (Flight III) DDG-113+ | Flight III 2016 | NULL | DDG-113 | DDG | Guided Missile Destroyer | Ultimate Aegis Destroyer | NULL | NULL | 2016 | NULL | NULL | NULL | 9700 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Standard missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 96 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 2 | 0 | NULL | NULL | Gas turbine | NULL | NULL | NULL | 1200000000 | 72 | NULL | NULL | 0 | SPY-6 radar upgrade. AN/SPY-6(V)1 AESA radar. Ultimate Aegis DD. DDG-113+, ultimate. |
| 13213 | USA | USS Zumwalt | Zumwalt-class | Base 2016 | NULL | DDG-1000 | DDG | Guided Missile Destroyer | Stealth Destroyer | NULL | NULL | 2016 | NULL | NULL | NULL | 15600 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Advanced guns | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 57 VLS | 80 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | 0 | 0 | 0 | NULL | NULL | Electric | NULL | NULL | NULL | 3500000000 | 84 | NULL | NULL | 0 | Stealth destroyer. 15,600 tons, advanced automation, stealth. 80 VLS. 3 ships, experimental. |
| 13214 | USA | USS Arleigh Burke (Flight IV) | Arleigh Burke-class (Flight IV) | Flight IV 2030 | NULL | DDG-131 | DDG | Guided Missile Destroyer | Future Aegis | NULL | NULL | 2030 | NULL | NULL | NULL | 9700 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Hypersonic missiles | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 41 VLS | 96 | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | 1 | NULL | NULL | 0 | 0 | 2 | 0 | NULL | NULL | Gas turbine | NULL | NULL | NULL | 1400000000 | 78 | NULL | NULL | 0 | Hypersonic missiles planned. 2030s tech, hypersonics. Future DDG. Planned 2030s. |
| 13215 | USA | DDG(X) | DDG(X) Future Destroyer | Concept 2040 | NULL | DDG(X) | DDG | Guided Missile Destroyer | Next-Gen Destroyer (Paper) | NULL | NULL | 2040 | NULL | NULL | Concept | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Next-gen systems | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Next-gen VLS | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 4000000000 | 96 | NULL | NULL | 1 | Next-generation DD concept. 2040s tech. Paper future DD, -10% reliability. Concept. |
| 15000 | USA | USS Holland | Holland-class | Base 1900 | NULL | SS-1 | SS | Submarine | Early Submarine | NULL | NULL | 1900 | NULL | NULL | NULL | 64 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 150000 | 12 | NULL | NULL | 0 | First US submarine. 64 tons, SS-1. Primitive: -40% diving. FREE starting sub. |
| 15001 | USA | USS A-1 | A-class | Base 1903 | NULL | SS-2 | SS | Submarine | Early Submarine | NULL | NULL | 1903 | NULL | NULL | NULL | 107 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 250000 | 18 | NULL | NULL | 0 | Better starting sub. 107 tons, gasoline: +20% range. FREE starting option. 7 ships. |
| 15002 | USA | USS C-1 | C-class | Base 1908 | NULL | SS-9 | SS | Submarine | Coastal Submarine | NULL | NULL | 1908 | NULL | NULL | NULL | 275 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 400000 | 24 | NULL | NULL | 0 | Coastal submarine. 275 tons, coastal patrol. Coastal operations. 5 ships. |
| 15003 | USA | USS F-1 | F-class | Base 1912 | NULL | SS-20 | SS | Submarine | Coastal Submarine | NULL | NULL | 1912 | NULL | NULL | NULL | 330 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 500000 | 24 | NULL | NULL | 0 | Larger coastal sub. 330 tons, improved. Better dive depth. 4 ships. |
| 15004 | USA | USS H-1 | H-class | Base 1913 | NULL | SS-28 | SS | Submarine | Coastal Submarine | NULL | NULL | 1913 | NULL | NULL | NULL | 350 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 600000 | 30 | NULL | NULL | 0 | Mass coastal sub. 350 tons, 18 ships built. WWI era. Largest early class. |
| 15005 | USA | USS L-1 | L-class | Base 1916 | NULL | SS-40 | SS | Submarine | Fleet Submarine | NULL | NULL | 1916 | NULL | NULL | NULL | 450 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 900000 | 36 | NULL | NULL | 0 | First fleet boats. 450 tons, ocean-going. WWI fleet. Early fleet SS, ocean-capable. 11 ships. |
| 15006 | USA | USS O-1 | O-class | Base 1918 | NULL | SS-62 | SS | Submarine | Fleet Submarine | NULL | NULL | 1918 | NULL | NULL | NULL | 520 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1000000 | 36 | NULL | NULL | 0 | WWI fleet boat. 520 tons, improved range. WWI fleet SS. Better range. 16 ships. |
| 15007 | USA | USS R-1 | R-class | Base 1918 | NULL | SS-78 | SS | Submarine | Fleet Submarine | NULL | NULL | 1918 | NULL | NULL | NULL | 680 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1100000 | 42 | NULL | NULL | 0 | Refined WWI sub. 680 tons, diesel-electric. First diesel-electric. 27 ships. |
| 15008 | USA | USS S-1 | S-class | Base 1920 | NULL | SS-105 | SS | Submarine | Fleet Submarine | NULL | NULL | 1920 | NULL | NULL | NULL | 850 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1400000 | 42 | NULL | NULL | 0 | Long-serving interwar sub. 850 tons, 48 ships. Mass fleet SS. 48 ships, long service. Largest interwar class. |
| 15009 | USA | USS Argonaut | V-class | Base 1924 | NULL | SS-166 | SS | Submarine | Cruiser Submarine | NULL | NULL | 1924 | NULL | NULL | NULL | 2000 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 6" deck gun | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 5000000 | 60 | NULL | NULL | 0 | Cruiser submarine. 2,000 tons, 6" deck gun. Experimental. 3 ships, experimental. |
| 15010 | USA | USS Porpoise | Porpoise-class | Base 1935 | NULL | SS-172 | SS | Submarine | Fleet Submarine | NULL | NULL | 1935 | NULL | NULL | NULL | 1310 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 2500000 | 48 | NULL | NULL | 0 | P-class fleet boat. 1,310 tons, modern. All-welded hull. Modern fleet SS. 10 ships. |
| 15011 | USA | USS Salmon | Salmon-class | Base 1938 | NULL | SS-182 | SS | Submarine | Fleet Submarine | NULL | NULL | 1938 | NULL | NULL | NULL | 1450 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 2700000 | 48 | NULL | NULL | 0 | Improved P-class. 1,450 tons, refined. Better engines. Improved fleet SS. 6 ships. |
| 15012 | USA | USS Sargo | Sargo-class | Base 1939 | NULL | SS-188 | SS | Submarine | Fleet Submarine | NULL | NULL | 1939 | NULL | NULL | NULL | 1450 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 2800000 | 48 | NULL | NULL | 0 | Final pre-war sub. 1,450 tons, pre-war peak. Pre-war pinnacle. 10 ships. |
| 15013 | USA | USS Tambor | Tambor-class | Base 1940 | NULL | SS-198 | SS | Submarine | Fleet Submarine | NULL | NULL | 1940 | NULL | NULL | NULL | 1475 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3000000 | 54 | NULL | NULL | 0 | Early WWII sub. 1,475 tons, war-ready. Early war SS. War-ready design. 12 ships. |
| 15014 | USA | USS Gar | Gar-class | Base 1941 | NULL | SS-206 | SS | Submarine | Fleet Submarine | NULL | NULL | 1941 | NULL | NULL | NULL | 1525 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3100000 | 54 | NULL | NULL | 0 | Improved Tambor. 1,525 tons, refined. Refined war SS. Improved Tambor. 6 ships. |
| 15015 | USA | USS Mackerel | Mackerel-class | Base 1953 | NULL | SS-204 | SS | Submarine | Coastal/Training Submarine | NULL | NULL | 1953 | NULL | NULL | NULL | 303 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1000000 | 18 | NULL | NULL | 0 | Coastal patrol sub. 303 tons, small coastal. Training SS. Small patrol/training. 2 ships. |
| 15016 | USA | USS Barracuda | Barracuda-class | Base 1951 | NULL | SST-3 | SST | Training Submarine | Training Submarine | NULL | NULL | 1951 | NULL | NULL | NULL | 765 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 1500000 | 24 | NULL | NULL | 0 | Training submarine. 765 tons, dedicated trainer. Dedicated trainer SST. 3 ships. |
| 15017 | USA | USS Gato | Gato-class | Base 1941 | NULL | SS-212 | SS | Submarine | Fleet Submarine | NULL | NULL | 1941 | NULL | NULL | NULL | 1525 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3500000 | 12 | NULL | NULL | 0 | Mass production WWII sub. 1,525 tons, 77 ships. WWII workhorse SS. First mass WWII class. 77 ships. |
| 15018 | USA | USS Balao | Balao-class | Base 1942 | NULL | SS-285 | SS | Submarine | Fleet Submarine | NULL | NULL | 1942 | NULL | NULL | NULL | 1526 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3700000 | 12 | NULL | NULL | 0 | Improved dive depth. 1,526 tons, 122 ships. Deep-diving SS. 400ft test depth. 122 ships, largest. |
| 15019 | USA | USS Tench | Tench-class | Base 1944 | NULL | SS-417 | SS | Submarine | Fleet Submarine | NULL | NULL | 1944 | NULL | NULL | NULL | 1570 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 3900000 | 15 | NULL | NULL | 0 | Ultimate diesel SS. 1,570 tons, peak design. Peak diesel SS. Ultimate WWII diesel. 29 ships. |
| 15020 | USA | USS Balao (GUPPY) | Balao-class (GUPPY) | GUPPY 1947 | 15018 | SS-285 | SS | Submarine | Modernized Diesel Submarine | NULL | NULL | 1947 | NULL | NULL | NULL | 1526 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 4000000 | 12 | 0 | Snorkel upgrade. Streamlined, snorkel. GUPPY SS. Post-war modernization. |
| 15021 | USA | USS Tench (GUPPY IIA) | Tench-class (GUPPY IIA) | GUPPY IIA 1952 | 15019 | SS-417 | SS | Submarine | Fully Modernized Diesel Sub | NULL | NULL | 1952 | NULL | NULL | NULL | 1570 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 0 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | NULL | NULL | NULL | NULL | 0 | 0 | 5000000 | 18 | 0 | Full GUPPY upgrade. Full snorkel + battery. Ultimate GUPPY SS. Full modernization. Major upgrade. |
| 15100 | USA | USS Nautilus | Nautilus SSN-571 | Base 1954 | NULL | SSN-571 | SSN | Attack Submarine (Nuclear) | First Nuclear Submarine | NULL | NULL | 1954 | NULL | NULL | NULL | 3500 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 55000000 | 60 | NULL | NULL | 0 | First nuclear sub. 3,500 tons, S2W reactor. Nuclear revolution. First nuclear, unlimited range. UNIQUE. SSN-571. |
| 15101 | USA | USS Seawolf | Seawolf SSN-575 | Base 1957 | NULL | SSN-575 | SSN | Attack Submarine (Nuclear) | Experimental Nuclear Sub | NULL | NULL | 1957 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 65000000 | 60 | NULL | NULL | 0 | Experimental reactor. Liquid sodium reactor. Experimental SSN. Sodium reactor. UNIQUE. SSN-575, failed experiment. |
| 15102 | USA | USS Skate | Skate-class | Base 1957 | NULL | SSN-578 | SSN | Attack Submarine (Nuclear) | Production Nuclear Sub | NULL | NULL | 1957 | NULL | NULL | NULL | 2550 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 45000000 | 54 | NULL | NULL | 0 | Production nuclear sub. 2,550 tons, S3W/S4W reactors. Production SSN. 4 ships, first production. |
| 15200 | USA | USS George Washington | George Washington-class | Base 1959 | NULL | SSBN-598 | SSBN | Ballistic Missile Submarine | First SSBN | NULL | NULL | 1959 | NULL | NULL | NULL | 5900 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 Polaris | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 110000000 | 66 | NULL | NULL | 0 | First ballistic sub. 5,900 tons, 16 Polaris. First SSBN. First ballistic missiles. 5 ships. |
| 15201 | USA | USS Ethan Allen | Ethan Allen-class | Base 1961 | NULL | SSBN-608 | SSBN | Ballistic Missile Submarine | Improved SSBN | NULL | NULL | 1961 | NULL | NULL | NULL | 6900 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 Polaris | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 125000000 | 66 | NULL | NULL | 0 | Improved SSBN. 6,900 tons, improved. Improved SSBN. Better missiles. 5 ships. |
| 15103 | USA | USS Skipjack | Skipjack-class | Base 1959 | NULL | SSN-585 | SSN | Attack Submarine (Nuclear) | Teardrop Hull Nuclear Sub | NULL | NULL | 1959 | NULL | NULL | NULL | 3075 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 50000000 | 60 | NULL | NULL | 0 | Teardrop revolution. 3,075 tons, teardrop hull. Fast SSN. Teardrop, 30+ kts. 6 ships, revolutionary. |
| 15104 | USA | USS Thresher | Thresher/Permit-class | Base 1961 | NULL | SSN-593 | SSN | Attack Submarine (Nuclear) | Deep-Diving Nuclear Sub | NULL | NULL | 1961 | NULL | NULL | NULL | 3750 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 75000000 | 66 | NULL | NULL | 0 | Deep-diving nuclear sub. 3,750 tons, HY-80 steel. Deep SSN. 1,300ft test depth. 14 ships. |
| 15105 | USA | USS Sturgeon | Sturgeon-class | Base 1967 | NULL | SSN-637 | SSN | Attack Submarine (Nuclear) | Long-Serving Nuclear Sub | NULL | NULL | 1967 | NULL | NULL | NULL | 4250 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 85000000 | 72 | NULL | NULL | 0 | Longest SSN class. 4,250 tons, 37 ships. Mass production SSN. 37 ships, most numerous. Longest SSN class. |
| 15202 | USA | USS Lafayette | Lafayette-class | Base 1963 | NULL | SSBN-616 | SSBN | Ballistic Missile Submarine | Mass Production SSBN | NULL | NULL | 1963 | NULL | NULL | NULL | 7250 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 Poseidon | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 140000000 | 72 | NULL | NULL | 0 | Mass production SSBN. 7,250 tons, 31 ships. Mass SSBN. 16 Poseidon, 31 ships. Largest SSBN class. |
| 15203 | USA | USS Benjamin Franklin | Benjamin Franklin-class | Base 1965 | NULL | SSBN-640 | SSBN | Ballistic Missile Submarine | Ultimate Polaris SSBN | NULL | NULL | 1965 | NULL | NULL | NULL | 7750 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 Poseidon | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 150000000 | 72 | NULL | NULL | 0 | Quieter Lafayette. 7,750 tons, quieter. Quiet SSBN. Quieter Lafayette. 12 ships. |
| 15106 | USA | USS Los Angeles | Los Angeles-class (Early) SSN-688-699 | Early 1974 | NULL | SSN-688 | SSN | Attack Submarine (Nuclear) | Fast Attack Nuclear Sub | NULL | NULL | 1974 | NULL | NULL | NULL | 6000 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 200000000 | 78 | NULL | NULL | 0 | Fast attack SSN. 6,000 tons, 33+ kts. Fast attack SSN. Fast, 62 total ships. SSN-688-699, early. |
| 15107 | USA | USS Providence | Los Angeles-class (Improved 688i) SSN-700-773 | Improved 1981 | NULL | SSN-700 | SSN | Attack Submarine (Nuclear) | VLS-Capable Nuclear Sub | NULL | NULL | 1981 | NULL | NULL | NULL | 6000 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Mk 45 VLS | 12 | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 225000000 | 78 | NULL | NULL | 0 | VLS-capable SSN. VLS + under-ice capability. Improved 688i SSN. 12 VLS Tomahawk. SSN-700-773, improved. |
| 15204 | USA | USS Ohio | Ohio-class | Base 1981 | NULL | SSBN-726 | SSBN | Ballistic Missile Submarine | Strategic Submarine | NULL | NULL | 1981 | NULL | NULL | NULL | 18750 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 24 Trident II | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 1500000000 | 84 | NULL | NULL | 0 | Ultimate SSBN. 18,750 tons, 24 Trident. Ultimate SSBN. 24 Trident II missiles. 18 ships, ultimate. |
| 15108 | USA | USS Ohio (SSGN) | Ohio-class (SSGN) | SSGN 2006 | 15204 | SSGN-726 | SSGN | Cruise Missile Submarine | Cruise Missile Sub | NULL | NULL | 2006 | NULL | NULL | NULL | 18750 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 154 Tomahawk | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 0 | 0 | 25000000 | 24 | 0 | SSGN conversion. 154 Tomahawk conversion. Tomahawk SSGN. 154 Tomahawk missiles. 4 conversions. |
| 15109 | USA | USS Seawolf | Seawolf-class | Base 1997 | NULL | SSN-21 | SSN | Attack Submarine (Nuclear) | Ultimate Attack Submarine | NULL | NULL | 1997 | NULL | NULL | NULL | 9140 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 2800000000 | 96 | NULL | NULL | 0 | Ultimate but expensive. 9,140 tons, ultimate SSN. Ultimate SSN. Ultimate but $2.8B. 3 ships, too expensive. |
| 15110 | USA | USS Virginia | Virginia-class | Base 2004 | NULL | SSN-774 | SSN | Attack Submarine (Nuclear) | Current Production Nuclear Sub | NULL | NULL | 2004 | NULL | NULL | NULL | 7800 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | NULL | NULL | 1 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 1800000000 | 84 | NULL | NULL | 0 | Production SSN. 7,800 tons, affordable. Production SSN. Affordable, modular. Current production. |
| 15205 | USA | USS Columbia | Columbia-class | Concept 2028 | NULL | SSBN-826 | SSBN | Ballistic Missile Submarine | Future SSBN | NULL | NULL | 2028 | NULL | NULL | NULL | 20800 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 16 Trident II D5 | 0 | NULL | NULL | 2 | NULL | NULL | NULL | NULL | NULL | NULL | NULL | NULL | 0 | 0 | 0 | 0 | 0 | 0 | Nuclear | NULL | NULL | NULL | 9000000000 | 108 | NULL | NULL | 0 | Next-gen SSBN. 20,800 tons, future. Future SSBN. 16 Trident II D5. Planned 2028, future. |

**Example Entries** (for reference - not yet in database):

### USA Battleships
- **USS Iowa (BB-61)** - Iowa-class fast battleship, 45,000 tons, 33 knots, 9×16"/50 guns
- **USS Missouri (BB-63)** - Iowa-class, surrender ceremony ship, museum ship
- **USS New Jersey (BB-62)** - Most decorated battleship, Vietnam and Lebanon service
- **USS North Carolina (BB-55)** - First modern US battleship
- **USS South Dakota (BB-57)** - Heavily armored, survived 42 hits at Guadalcanal

### USA Aircraft Carriers
- **USS Enterprise (CV-6)** - Yorktown-class, most decorated US ship of WWII
- **USS Yorktown (CV-5)** - Sunk at Midway
- **USS Essex (CV-9)** - Lead ship of most numerous carrier class (24 ships)
- **USS Midway (CV-41)** - First armored carrier, longest-serving (1945-1992)
- **USS Enterprise (CVN-65)** - First nuclear carrier, 8 reactors
- **USS Nimitz (CVN-68)** - Lead ship of current carrier class
- **USS Gerald R. Ford (CVN-78)** - Newest carrier class, EMALS catapults

### USA Cruisers
- **USS Baltimore (CA-68)** - Heavy cruiser, 14,000 tons, 9×8"/55 guns
- **USS Des Moines (CA-134)** - Auto-loading 8" guns, 10 rpm
- **USS Cleveland (CL-55)** - Light cruiser, most numerous US cruiser (27 ships)
- **USS Ticonderoga (CG-47)** - First Aegis cruiser
- **USS Port Royal (CG-73)** - Aegis cruiser, ballistic missile defense

### USA Destroyers
- **USS Fletcher (DD-445)** - Fletcher-class, 175 ships built, WWII workhorse
- **USS Gearing (DD-710)** - Improved Fletcher, longer range
- **USS Forrest Sherman (DD-931)** - First all-gun destroyer
- **USS Charles F. Adams (DDG-2)** - First guided missile destroyer class
- **USS Arleigh Burke (DDG-51)** - Modern Aegis destroyer, 89+ built
- **USS Zumwalt (DDG-1000)** - Stealth destroyer, tumblehome hull

### British Battleships
- **HMS Dreadnought** - Revolutionized battleship design (1906)
- **HMS Hood** - Battlecruiser, sunk by Bismarck (1941)
- **HMS King George V** - Lead ship, sank Bismarck
- **HMS Vanguard** - Last battleship ever built (1946)

### British Aircraft Carriers
- **HMS Ark Royal (91)** - WWII carrier, hunted Bismarck
- **HMS Illustrious** - Armored carrier, survived many attacks
- **HMS Eagle (R05)** - Audacious-class fleet carrier
- **HMS Invincible (R05)** - Light carrier, Falklands War
- **HMS Queen Elizabeth (R08)** - Modern supercarrier, STOVL

### German Battleships
- **Bismarck** - Sank Hood, hunted and sunk (1941)
- **Tirpitz** - Sister ship, sunk by RAF Tallboy bombs
- **Scharnhorst** - Battlecruiser, sunk at North Cape
- **Gneisenau** - Sister ship, never completed after damage

### Japanese Battleships
- **Yamato** - Largest battleship ever, 72,000 tons, 9×46cm guns
- **Musashi** - Sister ship, sunk at Leyte Gulf (19 torpedo, 17 bomb hits)
- **Nagato** - Survived both atomic tests at Bikini Atoll
- **Kongo** - Battlecruiser converted to fast battleship

### Japanese Aircraft Carriers
- **Akagi** - Pearl Harbor veteran, sunk at Midway
- **Kaga** - Converted from battleship, sunk at Midway
- **Soryu** - Fleet carrier, sunk at Midway
- **Hiryu** - Fleet carrier, sunk at Midway (all 4 in one battle)
- **Shokaku** - Large fleet carrier
- **Zuikaku** - Last Pearl Harbor veteran, sunk at Leyte Gulf

---

<a name="armament-table"></a>
## Armament Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Armament_ID | INT | Primary key |
| Ship_ID | INT | Foreign key to ships table |
| Weapon_Category | VARCHAR(50) | Main Battery, Secondary Battery, AA, Torpedo, Missile, ASW |
| Gun_ID | INT | Foreign key to guns table (if gun) |
| Torpedo_ID | INT | Foreign key to torpedoes table (if torpedo) |
| Missile_ID | INT | Foreign key to missiles table (if missile) |
| Turret_ID | INT | Foreign key to turrets table (if applicable) |
| Quantity | INT | Number of weapons/launchers |
| Mount_Configuration | VARCHAR(100) | Triple turret, Twin mount, Single mount, VLS, etc. |
| Mount_Location | VARCHAR(200) | Forward, Aft, Amidships, Port/Starboard, etc. |
| Traverse_Arc_DEG | INT | Firing arc in degrees |
| Year_Installed | INT | Year this armament was installed |
| Year_Removed | INT | Year removed (if modernized) |
| Fire_Control_System | VARCHAR(200) | Associated fire control radar/system |
| Ready_Ammunition | INT | Ready ammunition storage |
| Notes | TEXT | Mounting details, fire control, limitations |

| Armament_ID | Ship_ID | Weapon_Category | Gun_ID | Torpedo_ID | Missile_ID | Turret_ID | Quantity | Mount_Configuration | Mount_Location | Traverse_Arc_DEG | Year_Installed | Year_Removed | Fire_Control_System | Ready_Ammunition | Notes |
|-------------|---------|-----------------|--------|------------|------------|-----------|----------|---------------------|----------------|------------------|----------------|--------------|---------------------|------------------|-------|
| | | | | | | | | | | | | | | | |

**Weapon Categories**:
- **Main Battery**: Primary armament (battleship main guns, cruiser main battery)
- **Secondary Battery**: Anti-surface secondary guns
- **AA (Anti-Aircraft)**: Dedicated AA guns (5"/38 DP, 40mm, 20mm, etc.)
- **Torpedo**: Torpedo tubes and launchers
- **Missile SAM**: Surface-to-air missiles
- **Missile SSM**: Surface-to-surface missiles
- **Missile ASW**: Anti-submarine missiles
- **ASW**: Depth charges, hedgehogs, ASW rockets
- **CIWS**: Close-in weapon systems (Phalanx, Goalkeeper)

---

<a name="aircraft-complement-table"></a>
## Aircraft Complement Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Complement_ID | INT | Primary key |
| Ship_ID | INT | Foreign key to ships table |
| Aircraft_ID | INT | Foreign key to aircraft table |
| Role | VARCHAR(100) | Fighter, Attack, ASW, AEW, Helicopter, etc. |
| Quantity_Normal | INT | Normal operational complement |
| Quantity_Maximum | INT | Maximum surge capacity |
| Squadron_Designation | VARCHAR(100) | Squadron identification (if applicable) |
| Year_Embarked | INT | Year this aircraft type began service |
| Year_Retired | INT | Year this aircraft type retired from ship |
| Launch_Method | VARCHAR(50) | Catapult, Ski-jump, STOVL, Helicopter deck |
| Recovery_Method | VARCHAR(50) | Arrested landing, STOVL, Helicopter landing |
| Storage_Location | VARCHAR(100) | Hangar deck, Flight deck, etc. |
| Notes | TEXT | Operational notes, typical loadouts |

| Complement_ID | Ship_ID | Aircraft_ID | Role | Quantity_Normal | Quantity_Maximum | Squadron_Designation | Year_Embarked | Year_Retired | Launch_Method | Recovery_Method | Storage_Location | Notes |
|---------------|---------|-------------|------|-----------------|------------------|----------------------|---------------|--------------|---------------|-----------------|------------------|-------|
| | | | | | | | | | | | | |

**Example Aircraft Complements**:
- **USS Enterprise (CV-6) WWII**: 36 F6F Hellcat, 36 SBD Dauntless, 18 TBF Avenger = 90 aircraft
- **USS Nimitz (CVN-68) Modern**: 48 F/A-18E/F, 4 EA-18G, 4 E-2D, 6 MH-60 = ~62 aircraft
- **HMS Queen Elizabeth**: 24-36 F-35B Lightning II, 14 helicopters
- **Yamato**: 7 floatplanes (reconnaissance)

---

<a name="armor-protection-table"></a>
## Armor Protection Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Armor_ID | INT | Primary key |
| Ship_ID | INT | Foreign key to ships table |
| Location | VARCHAR(100) | Belt, Deck, Turret face, Conning tower, etc. |
| Armor_Type | VARCHAR(100) | Krupp cemented, Face-hardened, Homogeneous, etc. |
| Thickness_Max_IN | DECIMAL(5,2) | Maximum armor thickness in inches |
| Thickness_Min_IN | DECIMAL(5,2) | Minimum armor thickness in inches |
| Inclination_DEG | INT | Armor slope angle from vertical |
| Coverage_Area_SQFT | INT | Area protected in square feet |
| Weight_TONS | INT | Weight of this armor section |
| Protection_Level | VARCHAR(100) | Immune zone, critical protection, etc. |
| Notes | TEXT | Armor scheme details, effectiveness |

| Armor_ID | Ship_ID | Location | Armor_Type | Thickness_Max_IN | Thickness_Min_IN | Inclination_DEG | Coverage_Area_SQFT | Weight_TONS | Protection_Level | Notes |
|----------|---------|----------|------------|------------------|------------------|-----------------|--------------------|-------------|------------------|-------|
| | | | | | | | | | | |

**Armor Locations**:
- **Main Belt**: Waterline protection
- **Upper Belt**: Above waterline
- **Lower Belt**: Below waterline
- **Deck Armor**: Horizontal protection (main deck, splinter deck)
- **Turret Face**: Gun turret front
- **Turret Sides/Roof**: Turret protection
- **Barbette**: Turret rotating structure
- **Conning Tower**: Command center
- **Bulkheads**: Transverse/longitudinal armor
- **Torpedo Bulkhead**: Anti-torpedo protection

**Example Armor Schemes**:
- **Yamato**: 16.1" belt, 9.1" deck, 25.6" turret face, 19.7" conning tower
- **Iowa**: 12.1" belt, 6" deck (total), 19.7" turret face, 17.3" conning tower
- **Bismarck**: 12.6" belt, 4.7" deck, 14.2" turret face

---

<a name="propulsion-table"></a>
## Propulsion Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Propulsion_ID | INT | Primary key |
| Ship_ID | INT | Foreign key to ships table |
| Propulsion_Type | VARCHAR(100) | Steam turbine, Nuclear, Diesel, Diesel-electric, Gas turbine |
| Engine_Manufacturer | VARCHAR(100) | Manufacturer name |
| Engine_Model | VARCHAR(100) | Specific engine model |
| Number_Of_Engines | INT | Number of main engines |
| Number_Of_Shafts | INT | Number of propeller shafts |
| Total_Horsepower_SHP | INT | Total shaft horsepower |
| Boiler_Type | VARCHAR(100) | Boiler type (if steam) |
| Number_Of_Boilers | INT | Number of boilers |
| Reactor_Type | VARCHAR(100) | Reactor type (if nuclear) |
| Number_Of_Reactors | INT | Number of reactors |
| Fuel_Type | VARCHAR(100) | Fuel oil, Diesel, Nuclear, etc. |
| Fuel_Capacity_TONS | INT | Fuel capacity in tons |
| Range_At_Max_Speed_NM | INT | Range at maximum speed |
| Range_At_Cruise_NM | INT | Range at economical cruise speed |
| Max_Speed_KTS | DECIMAL(5,2) | Maximum speed achieved |
| Trial_Speed_KTS | DECIMAL(5,2) | Speed achieved on trials |
| Notes | TEXT | Propulsion details, performance |

| Propulsion_ID | Ship_ID | Propulsion_Type | Engine_Manufacturer | Engine_Model | Number_Of_Engines | Number_Of_Shafts | Total_Horsepower_SHP | Boiler_Type | Number_Of_Boilers | Reactor_Type | Number_Of_Reactors | Fuel_Type | Fuel_Capacity_TONS | Range_At_Max_Speed_NM | Range_At_Cruise_NM | Max_Speed_KTS | Trial_Speed_KTS | Notes |
|---------------|---------|-----------------|---------------------|--------------|-------------------|------------------|----------------------|-------------|-------------------|--------------|--------------------|-----------|--------------------|----------------------|--------------------|---------------|-----------------|-------|
| | | | | | | | | | | | | | | | | | | |

**Propulsion Types by Era**:

### WWII Era
- **Steam Turbine**: Most common, oil-fired boilers
- **Diesel**: Submarines, some small vessels
- **Diesel-Electric**: Most submarines

### Cold War Era
- **Steam Turbine**: Continued dominance
- **Nuclear**: Carriers, submarines, cruisers
- **Gas Turbine**: Emerging for destroyers/frigates

### Modern Era
- **Nuclear**: Carriers (USA, France), submarines (USA, UK, France, Russia, China)
- **Gas Turbine**: Most surface combatants (COGAG, COGOG, CODOG)
- **Combined Diesel or Gas (CODOG)**: Common for frigates
- **Combined Gas and Gas (COGAG)**: High-performance destroyers

---

<a name="service-history-table"></a>
## Service History Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| History_ID | INT | Primary key |
| Ship_ID | INT | Foreign key to ships table |
| Event_Date | DATE | Date of event |
| Event_Type | VARCHAR(100) | Battle, Deployment, Refit, Modernization, etc. |
| Event_Name | VARCHAR(200) | Battle name, operation name, etc. |
| Location | VARCHAR(200) | Geographic location |
| Description | TEXT | Event description |
| Commanding_Officer | VARCHAR(100) | CO at time of event |
| Result | VARCHAR(200) | Victory, Defeat, Damaged, Sunk, etc. |
| Casualties | VARCHAR(100) | KIA/WIA if applicable |
| Awards_Decorations | VARCHAR(500) | Battle stars, unit citations, etc. |
| Notes | TEXT | Additional historical notes |

| History_ID | Ship_ID | Event_Date | Event_Type | Event_Name | Location | Description | Commanding_Officer | Result | Casualties | Awards_Decorations | Notes |
|------------|---------|------------|------------|------------|----------|-------------|-----------------------|--------|------------|-------------------|-------|
| | | | | | | | | | | | |

**Event Types**:
- **Battle**: Major naval engagement
- **Campaign**: Extended operation
- **Deployment**: Routine deployment
- **Refit**: Major overhaul
- **Modernization**: Upgrade program
- **Damage**: Significant damage event
- **Sinking**: Ship lost
- **Decommissioning**: Retired from service
- **Museum Ship**: Preserved as memorial
- **Scrapping**: Final disposition

---

## Ship Type Classifications

### Capital Ships
- **BB** - Battleship
- **BC** - Battlecruiser
- **CV** - Aircraft Carrier (conventional)
- **CVL** - Light Aircraft Carrier
- **CVE** - Escort Carrier
- **CVN** - Aircraft Carrier (nuclear)
- **CVS** - ASW Carrier

### Cruisers
- **CA** - Heavy Cruiser (8" guns)
- **CB** - Large Cruiser (Alaska-class)
- **CL** - Light Cruiser (6" or smaller guns)
- **CG** - Guided Missile Cruiser
- **CGN** - Guided Missile Cruiser (nuclear)
- **CLG** - Guided Missile Light Cruiser

### Destroyers & Escorts
- **DD** - Destroyer
- **DDG** - Guided Missile Destroyer
- **DE** - Destroyer Escort
- **FF** - Frigate
- **FFG** - Guided Missile Frigate

### Submarines
- **SS** - Submarine (diesel-electric)
- **SSN** - Attack Submarine (nuclear)
- **SSBN** - Ballistic Missile Submarine (nuclear)
- **SSGN** - Cruise Missile Submarine (nuclear)
- **SSK** - Hunter-Killer Submarine (diesel)

### Amphibious Warfare
- **LHA** - Amphibious Assault Ship
- **LHD** - Amphibious Assault Ship (with well deck)
- **LPD** - Amphibious Transport Dock
- **LSD** - Landing Ship Dock
- **LST** - Landing Ship Tank

### Auxiliary
- **AO** - Oiler (fleet replenishment)
- **AOE** - Fast Combat Support Ship
- **AS** - Submarine Tender
- **AD** - Destroyer Tender
- **AR** - Repair Ship

---

## Ship Subtypes

### Battleships
- **Dreadnought**: All big-gun, turbine-powered (1906+)
- **Pre-dreadnought**: Mixed armament, reciprocating engines (pre-1906)
- **Super-dreadnought**: Larger caliber guns (13.5"+), better armor
- **Fast Battleship**: 30+ knots, WWII era
- **Battlecruiser**: Battleship guns, cruiser armor/speed

### Aircraft Carriers
- **Fleet Carrier**: Large, fast, 60-100+ aircraft
- **Light Carrier**: Converted cruiser hulls, 30-45 aircraft
- **Escort Carrier**: Converted merchant hulls, 20-30 aircraft, ASW/convoy
- **Supercarrier**: 90,000+ tons, 75-90 aircraft (modern US)

### Cruisers
- **Armored Cruiser**: Pre-WWI, heavy armor, 8-10" guns
- **Protected Cruiser**: Armored deck, light sides
- **Heavy Cruiser**: 8" guns, 10,000 ton treaty limit
- **Light Cruiser**: 6" or smaller guns
- **Scout Cruiser**: High speed, reconnaissance
- **Guided Missile Cruiser**: Primary role air defense

### Destroyers
- **Torpedo Boat Destroyer**: Original mission (1890s-1900s)
- **Flush-Deck Destroyer**: WWI "four-piper" type
- **Fleet Destroyer**: WWII standard (Fletcher, Gearing, etc.)
- **Guided Missile Destroyer**: Post-1960, missile-armed
- **Stealth Destroyer**: Low-observable design (Zumwalt)

### Submarines
- **Fleet Submarine**: Long-range patrol (WWII)
- **Attack Submarine**: Anti-ship/ASW mission
- **Ballistic Missile Submarine**: Strategic deterrent
- **Cruise Missile Submarine**: Land-attack mission

---

## Future Expansion Notes

### Priority WWI/Interwar Ships
- **USA**: USS Arizona, USS Texas, USS Pennsylvania
- **British**: HMS Dreadnought, HMS Warspite, HMS Rodney
- **German**: SMS Kaiser, SMS König
- **Japan**: IJN Fuso, IJN Kongo (original)

### Priority WWII Ships (Essential 100)

#### USA (30 ships)
- Battleships: Iowa, Missouri, New Jersey, Wisconsin, North Carolina, South Dakota
- Carriers: Enterprise, Yorktown, Hornet, Essex, Lexington, Saratoga
- Cruisers: Baltimore, Cleveland, Brooklyn, Wichita
- Destroyers: Fletcher, Gearing, Sumner classes (representative ships)
- Submarines: Gato, Balao classes

#### British (20 ships)
- Battleships: King George V, Hood, Warspite, Nelson
- Carriers: Ark Royal, Illustrious, Formidable, Victorious
- Cruisers: Belfast, Sheffield, Edinburgh
- Destroyers: Tribal-class, J/K/N classes

#### German (15 ships)
- Battleships: Bismarck, Tirpitz, Scharnhorst, Gneisenau
- Cruisers: Admiral Hipper, Prinz Eugen
- Destroyers: Type 1936, 1936A
- Submarines: Type VII, Type IX, Type XXI

#### Japanese (20 ships)
- Battleships: Yamato, Musashi, Nagato, Kongo
- Carriers: Akagi, Kaga, Soryu, Hiryu, Shokaku, Zuikaku
- Cruisers: Takao, Mogami, Tone
- Destroyers: Fubuki, Kagero, Yugumo classes

#### Soviet (5 ships)
- Battleships: Marat, Oktyabrskaya Revolutsiya
- Cruisers: Kirov, Maksim Gorky

### Priority Cold War Ships (50 ships)
- **USA**: Enterprise (CVN-65), Nimitz-class carriers, Long Beach, Ticonderoga-class, Spruance-class
- **British**: Audacious-class, Invincible-class, County-class destroyers
- **Soviet**: Kirov-class cruisers, Sovremenny-class, Udaloy-class, Kiev-class carriers

### Priority Modern Ships (30 ships)
- **USA**: Gerald R. Ford-class, Arleigh Burke-class, Zumwalt-class, Virginia-class subs
- **British**: Queen Elizabeth-class, Type 45 destroyers, Astute-class subs
- **Chinese**: Type 055 cruisers, Type 052D destroyers, Type 003 carrier
- **Russian**: Admiral Gorshkov frigates, Yasen-class subs


## Ship Entries

**Total Ships**: 853 basic entries from research tree + 121 detailed USA cruisers (pre-existing) = 974 total

**By Nation**:
- **USA**: 250 basic entries + 121 detailed cruisers = 371 total
- **British**: 206 ships (Battleships, Carriers, Cruisers, Destroyers, Submarines)
- **German**: 179 ships (Battleships, Carriers, Cruisers, Destroyers, Submarines)
- **Japanese**: 218 ships (Battleships, Carriers, Cruisers, Destroyers, Submarines)

**Data Source**: Converted from Ship Research Tree Database using estimation algorithms for displacement, speed, and range based on ship type and year.

**Field Status**:
- ✅ **Populated**: Ship_ID, Country, Ship_Name, Ship_Class, Hull_Variant, Ship_Type, Ship_Type_Full, Era, Year_Commissioned, Year_Designed, Year_Completed, Displacement_Standard, Displacement_Full, Max_Speed, Cruise_Speed, Range_NM, Cost_USD, Build_Time_Months, Modded, Notes
- 🔲 **NULL** (Future Expansion): Length, Beam, Draft, Crew details, Engine specifics, Hardpoints, Modules, Magazine capacity, Aircraft facilities, Upgrade systems

### Table Format

| Ship_ID | Country | Ship_Name | Ship_Class | Hull_Variant | Ship_Type | Ship_Type_Full | Era | Year_Commissioned | Year_Designed | Year_Completed | Displacement_Standard | Displacement_Full | Max_Speed | Cruise_Speed | Range_NM | Cost_USD | Build_Time | Modded | Notes |
|---------|---------|-----------|------------|--------------|-----------|----------------|-----|-------------------|---------------|----------------|-----------------------|-------------------|-----------|--------------|----------|----------|------------|--------|-------|
| 1000 | USA | Texas (BB-1) | Texas (BB-1) | Base | BB | Battleship | Pre-Dreadnought | 1890 | 1890 | 1890 | 12000 | 13799 | 18 | 14.4 | 15000 | 2500000 | 24 | 0 | Old Reliable: -20% maintenance cost |
| 1001 | USA | Indiana-class | Indiana-class | Base | BB | Battleship | Pre-Dreadnought | 1890 | 1890 | 1890 | 12000 | 13799 | 18 | 14.4 | 15000 | 3020000 | 36 | 0 | +20% armor, -2 speed |
| 1002 | USA | Maine-class | Maine-class | Base | BB | Battleship | Pre-Dreadnought | 1902 | 1902 | 1902 | 12000 | 13799 | 18 | 14.4 | 15000 | 4300000 | 36 | 0 | +15% max range |
| 1003 | USA | Kearsarge-class | Kearsarge-class | Base | BB | Battleship | Pre-Dreadnought | 1900 | 1900 | 1900 | 12000 | 13799 | 18 | 14.4 | 15000 | 3760000 | 36 | 0 | +15% firepower, -10% accuracy |
| 1004 | USA | Illinois-class | Illinois-class | Base | BB | Battleship | Pre-Dreadnought | 1900 | 1900 | 1900 | 12000 | 13799 | 18 | 14.4 | 15000 | 4200000 | 36 | 0 | Balanced stats |
| 1005 | USA | Virginia-class | Virginia-class | Base | BB | Battleship | Pre-Dreadnought | 1906 | 1906 | 1906 | 20000 | 23000 | 21 | 16.8 | 15000 | 4500000 | 36 | 0 | Flexible armament |
| 1006 | USA | Connecticut-class | Connecticut-class | Base | BB | Battleship | Pre-Dreadnought | 1906 | 1906 | 1906 | 20000 | 23000 | 21 | 16.8 | 15000 | 5000000 | 42 | 0 | Great White Fleet: +10% prestige |
| 1007 | USA | Mississippi-class | Mississippi-class | Base | BB | Battleship | Pre-Dreadnought | 1908 | 1908 | 1908 | 20000 | 23000 | 21 | 16.8 | 15000 | 4800000 | 36 | 0 | Foreign design influence |
| 1010 | USA | South Carolina-class | South Carolina-class | Base | BB | Battleship | Dreadnought | 1910 | 1910 | 1910 | 20000 | 23000 | 21 | 16.8 | 15000 | 6000000 | 48 | 0 | +25% penetration vs pre-dreads |
| 1011 | USA | Delaware-class | Delaware-class | Base | BB | Battleship | Dreadnought | 1910 | 1910 | 1910 | 20000 | 23000 | 21 | 16.8 | 15000 | 6500000 | 48 | 0 | +20% broadside weight |
| 1012 | USA | Wyoming-class | Wyoming-class | Base | BB | Battleship | Dreadnought | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 7000000 | 54 | 0 | +30% fire rate (12 guns) |
| 1014 | USA | New York-class | New York-class | Base | BB | Battleship | Dreadnought | 1914 | 1914 | 1914 | 20000 | 23000 | 21 | 16.8 | 15000 | 8000000 | 60 | 0 | +20% penetration vs 12" armor |
| 1015 | USA | Nevada-class | Nevada-class | Base | BB | Battleship | Standard-Type | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 9000000 | 60 | 0 | +30% critical hit resistance |
| 1016 | USA | Pennsylvania-class | Pennsylvania-class | Base | BB | Battleship | Standard-Type | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 10000000 | 60 | 0 | +25% broadside weight |
| 1017 | USA | New Mexico-class | New Mexico-class | Base | BB | Battleship | Standard-Type | 1918 | 1918 | 1918 | 32000 | 36800 | 23 | 18.4 | 15000 | 11000000 | 66 | 0 | Turbo-electric: +5% efficiency |
| 1019 | USA | Colorado-class | Colorado-class | Base | BB | Battleship | Standard-Type | 1921 | 1921 | 1921 | 32000 | 36800 | 23 | 18.4 | 15000 | 12000000 | 66 | 0 | +25% penetration vs all targets |
| 1020 | USA | North Carolina-class | North Carolina-class | Base | BB | Battleship | Fast BB | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 80000000 | 72 | 0 | +15% AA defense, +10% carrier escort |
| 1021 | USA | South Dakota (1939)-class | South Dakota (1939)-class | Base | BB | Battleship | Fast BB | 1942 | 1942 | 1942 | 45000 | 51749 | 30 | 24.0 | 15000 | 85000000 | 72 | 0 | -10% target profile, +20% armor efficiency |
| 1023 | USA | Iowa-class | Iowa-class | Base | BB | Battleship | Fast BB | 1943 | 1943 | 1943 | 45000 | 51749 | 30 | 24.0 | 15000 | 110000000 | 84 | 0 | All stats +10% |
| 1050 | USA | Arkansas Monitor | Arkansas Monitor | Base | BB | Battleship | Pre-Dreadnought | 1902 | 1902 | 1902 | 12000 | 13799 | 18 | 14.4 | 15000 | 1500000 | 18 | 0 | +30% coastal defense, -50% ocean range |
| 1064 | USA | New York (1926 Refit) | New York (1926 Refit) | Base | BB | Battleship | Dreadnought | 1926 | 1926 | 1926 | 35000 | 40250 | 23 | 18.4 | 15000 | 0 | 0 | 0 | +40% AA capability, +9000nm range |
| 1065 | USA | Nevada (1927 Refit) | Nevada (1927 Refit) | Base | BB | Battleship | Standard-Type | 1927 | 1927 | 1927 | 35000 | 40250 | 23 | 18.4 | 15000 | 0 | 0 | 0 | +9000nm range (to 15700nm) |
| 1066 | USA | Pennsylvania (1931 Refit) | Pennsylvania (1931 Refit) | Base | BB | Battleship | Standard-Type | 1931 | 1931 | 1931 | 35000 | 40250 | 23 | 18.4 | 15000 | 0 | 0 | 0 | +25% AA accuracy |
| 1067 | USA | New Mexico (1931 Refit) | New Mexico (1931 Refit) | Base | BB | Battleship | Standard-Type | 1931 | 1931 | 1931 | 35000 | 40250 | 23 | 18.4 | 15000 | 0 | 0 | 0 | +15% torpedo resistance |
| 1068 | USA | Tennessee (1943 Rebuild) | Tennessee (1943 Rebuild) | Base | BB | Battleship | Standard-Type | 1943 | 1943 | 1943 | 45000 | 51749 | 30 | 24.0 | 15000 | 45000000 | 18 | 0 | +200% AA effectiveness, radar |
| 1069 | USA | California (1944 Rebuild) | California (1944 Rebuild) | Base | BB | Battleship | Standard-Type | 1944 | 1944 | 1944 | 45000 | 51749 | 30 | 24.0 | 15000 | 45000000 | 18 | 0 | +200% AA effectiveness, radar |
| 1070 | USA | Colorado (1941 Refit) | Colorado (1941 Refit) | Base | BB | Battleship | Standard-Type | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 0 | 0 | 0 | +30% AA capability |
| 1071 | USA | West Virginia (1944 Rebuild) | West Virginia (1944 Rebuild) | Base | BB | Battleship | Standard-Type | 1944 | 1944 | 1944 | 45000 | 51749 | 30 | 24.0 | 15000 | 60000000 | 18 | 0 | +30% torpedo defense, +250% AA |
| 1072 | USA | North Carolina (1945 Refit) | North Carolina (1945 Refit) | Base | BB | Battleship | Fast BB | 1945 | 1945 | 1945 | 50000 | 57499 | 30 | 24.0 | 15000 | 0 | 0 | 0 | +40% AA effectiveness |
| 1073 | USA | South Dakota (1945 Refit) | South Dakota (1945 Refit) | Base | BB | Battleship | Fast BB | 1945 | 1945 | 1945 | 50000 | 57499 | 30 | 24.0 | 15000 | 0 | 0 | 0 | +50% AA effectiveness |
| 1074 | USA | Iowa (1945 Refit) | Iowa (1945 Refit) | Base | BB | Battleship | Fast BB | 1945 | 1945 | 1945 | 50000 | 57499 | 30 | 24.0 | 15000 | 0 | 0 | 0 | +30% AA, +25% radar effectiveness |
| 1080 | USA | Iowa (1984 Reactivation) | Iowa (1984 Reactivation) | Base | BB | Battleship | Modern | 1984 | 1984 | 1984 | 50000 | 57499 | 30 | 24.0 | 15000 | 1700000000 | 30 | 0 | 32× Tomahawk, 16× Harpoon, Phalanx |
| 2000 | USA | Tillman I | Tillman I | Base | BB | Battleship | Treaty Era | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 40000000 | 60 | 0 | -10% reliability (unproven) |
| 2001 | USA | Tillman II | Tillman II | Base | BB | Battleship | Treaty Era | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 45000000 | 66 | 0 | Unique sextuple turrets, -15% reliability |
| 2002 | USA | Tillman IV | Tillman IV | Base | BB | Battleship | Treaty Era | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 55000000 | 72 | 0 | 18" belt, -10% reliability |
| 2010 | USA | Lexington Battlecruiser | Lexington Battlecruiser | Base | BC | BC | Treaty Era | 1920 | 1920 | 1920 | 10000 | 11500 | 25 | 20.0 | 10000 | 40000000 | 48 | 0 | +8 knots speed, -30% armor |
| 2011 | USA | Tillman III | Tillman III | Base | BB | Battleship | Treaty Era | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 42000000 | 60 | 0 | 30 knots, -10% reliability |
| 2020 | USA | South Dakota (1920) | South Dakota (1920) | Base | BB | Battleship | Treaty Era | 1920 | 1920 | 1920 | 32000 | 36800 | 23 | 18.4 | 15000 | 50000000 | 60 | 0 | -10% reliability |
| 2021 | USA | Tillman IV-2 | Tillman IV-2 | Base | BB | Battleship | Treaty Era | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 60000000 | 72 | 0 | 18" guns, -15% reliability |
| 2030 | USA | Lexington Completed | Lexington Completed | Base | BC | BC | Treaty Era | 1920 | 1920 | 1920 | 10000 | 11500 | 25 | 20.0 | 10000 | 45000000 | 54 | 0 | 33 knots, 8× 16" guns |
| 2031 | USA | Alaska-class | Alaska-class | Base | CB | CB | Fast BB | 1941 | 1941 | 1941 | 10000 | 11500 | 25 | 20.0 | 10000 | 75000000 | 36 | 0 | +20% vs cruisers, 33 knots |
| 2040 | USA | Montana-class | Montana-class | Base | BB | Battleship | Fast BB | 1943 | 1943 | 1943 | 45000 | 51749 | 30 | 24.0 | 15000 | 120000000 | 84 | 0 | 12× 16" guns, -10% reliability |
| 5000 | USA | Langley-class | Langley-class | Base | CV | Aircraft Carrier | Experimental | 1922 | 1922 | 1922 | 25000 | 28749 | 30 | 24.0 | 12000 | 2000000 | 18 | 0 | Proves Concept: -30% effectiveness, FREE |
| 5001 | USA | Lexington-class | Lexington-class | Base | CV | Aircraft Carrier | Battlecruiser Conversion | 1927 | 1927 | 1927 | 25000 | 28749 | 30 | 24.0 | 12000 | 45000000 | 72 | 0 | +33 kts speed, 8" guns (unique) |
| 5002 | USA | Ranger-class | Ranger-class | Base | CV | Aircraft Carrier | Treaty Carrier | 1934 | 1934 | 1934 | 30000 | 34500 | 30 | 24.0 | 12000 | 15500000 | 36 | 0 | -2 kts speed, weak protection |
| 5003 | USA | Yorktown-class | Yorktown-class | Base | CV | Aircraft Carrier | Perfect Fleet Carrier | 1937 | 1937 | 1937 | 30000 | 34500 | 30 | 24.0 | 12000 | 20000000 | 36 | 0 | 32.5 kts, well-protected |
| 5004 | USA | Essex-class | Essex-class | Base | CV | Aircraft Carrier | WWII Workhorse | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 68000000 | 20 | 0 | +40% AA effectiveness |
| 5005 | USA | Essex-class (1947 Refit) | Essex-class (1947 Refit) | Base | CV | Aircraft Carrier | Post-War | 1947 | 1947 | 1947 | 45000 | 51749 | 33 | 26.4 | 12000 | 0 | 0 | 0 | +70% 40mm AA, improved radar |
| 5006 | USA | Essex-class (SCB-27A) | Essex-class (SCB-27A) | Base | CV | Aircraft Carrier | Jet Age | 1951 | 1951 | 1951 | 45000 | 51749 | 33 | 26.4 | 12000 | 0 | 0 | 0 | Steam cats, angled deck, jets |
| 5007 | USA | Midway-class | Midway-class | Base | CV | Aircraft Carrier | Armored Carrier | 1945 | 1945 | 1945 | 45000 | 51749 | 33 | 26.4 | 12000 | 90000000 | 24 | 0 | +3.5" armor, 47-year service |
| 5008 | USA | Forrestal-class | Forrestal-class | Base | CV | Aircraft Carrier | Supercarrier | 1955 | 1955 | 1955 | 45000 | 51749 | 33 | 26.4 | 12000 | 217000000 | 36 | 0 | 4 catapults, 60,000 tons |
| 5009 | USA | Kitty Hawk-class | Kitty Hawk-class | Base | CV | Aircraft Carrier | Improved Supercarrier | 1961 | 1961 | 1961 | 90000 | 103499 | 33 | 26.4 | 12000 | 264000000 | 42 | 0 | 4 deck-edge elevators |
| 5010 | USA | Enterprise-class | Enterprise-class | Base | CVN | CVN | First Nuclear | 1961 | 1961 | 1961 | 10000 | 11500 | 25 | 20.0 | 10000 | 451000000 | 54 | 0 | UNLIMITED range, 8× A2W reactors |
| 5011 | USA | Gerald R. Ford-class | Gerald R. Ford-class | Base | CVN | CVN | Ultimate Carrier | 2017 | 2017 | 2017 | 10000 | 11500 | 25 | 20.0 | 10000 | 1300000000 | 96 | 0 | EMALS cats, 75+ aircraft, AAWS |
| 5012 | USA | Bogue-class | Bogue-class | Base | CVE | CVE | WWII | 1942 | 1942 | 1942 | 10000 | 11500 | 25 | 20.0 | 10000 | 8000000 | 12 | 0 | ASW Focus: +50% sub detection, FREE |
| 5013 | USA | Saratoga CV-3 | Saratoga CV-3 | Base | CV | Aircraft Carrier | Interwar | 1927 | 1927 | 1927 | 25000 | 28749 | 30 | 24.0 | 12000 | 45000000 | 72 | 0 | +33 kts speed, 8" guns (unique) |
| 5014 | USA | Long Island-class | Long Island-class | Base | CVE | CVE | WWII | 1941 | 1941 | 1941 | 10000 | 11500 | 25 | 20.0 | 10000 | 4000000 | 12 | 0 | +30% pilot training |
| 5015 | USA | Wasp-class | Wasp-class | Base | CV | Aircraft Carrier | Interwar | 1940 | 1940 | 1940 | 35000 | 40250 | 33 | 26.4 | 12000 | 20000000 | 36 | 0 | +20% armor vs Ranger |
| 5016 | USA | Sangamon-class | Sangamon-class | Base | CVE | CVE | WWII | 1942 | 1942 | 1942 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 12 | 0 | 18 kts vs 16 kts standard CVE |
| 5017 | USA | Enterprise CV-6 | Enterprise CV-6 | Base | CV | Aircraft Carrier | WWII | 1938 | 1938 | 1938 | 30000 | 34500 | 30 | 24.0 | 12000 | 20000000 | 36 | 0 | Lucky E: +15% evasion |
| 5018 | USA | Casablanca-class | Casablanca-class | Base | CVE | CVE | WWII | 1943 | 1943 | 1943 | 10000 | 11500 | 25 | 20.0 | 10000 | 5000000 | 6 | 0 | Rapid build: 6 months |
| 5019 | USA | Independence-class | Independence-class | Base | CVL | CVL | WWII | 1943 | 1943 | 1943 | 10000 | 11500 | 25 | 20.0 | 10000 | 15000000 | 12 | 0 | 31.5 kts, rapid build 12 months |
| 5020 | USA | Commencement Bay-class | Commencement Bay-class | Base | CVE | CVE | WWII | 1944 | 1944 | 1944 | 10000 | 11500 | 25 | 20.0 | 10000 | 10000000 | 12 | 0 | 19 kts, 34 aircraft |
| 5021 | USA | Saipan-class | Saipan-class | Base | CVL | CVL | Post-War | 1946 | 1946 | 1946 | 10000 | 11500 | 25 | 20.0 | 10000 | 30000000 | 18 | 0 | 33 kts, 48 aircraft |
| 5022 | USA | Intrepid CV-11 | Intrepid CV-11 | Base | CV | Aircraft Carrier | WWII | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 68000000 | 20 | 0 | Damage Control: +25% survival |
| 5023 | USA | Essex-class (SCB-27C/125) | Essex-class (SCB-27C/125) | Base | CV | Aircraft Carrier | Jet Age | 1955 | 1955 | 1955 | 45000 | 51749 | 33 | 26.4 | 12000 | 0 | 0 | 0 | C-11 cats, full modernization |
| 5024 | USA | Midway-class (SCB-110) | Midway-class (SCB-110) | Base | CV | Aircraft Carrier | Jet Age | 1957 | 1957 | 1957 | 45000 | 51749 | 33 | 26.4 | 12000 | 0 | 0 | 0 | Armored + jet capable |
| 5025 | USA | Thetis Bay CVHA-1 | Thetis Bay CVHA-1 | Base | CVH | CVH | Cold War | 1956 | 1956 | 1956 | 10000 | 11500 | 25 | 20.0 | 10000 | 5000000 | 6 | 0 | 20 helicopters, USMC assault |
| 5026 | USA | Saratoga CV-60 | Saratoga CV-60 | Base | CV | Aircraft Carrier | Supercarrier | 1956 | 1956 | 1956 | 45000 | 51749 | 33 | 26.4 | 12000 | 220000000 | 36 | 0 | Upgraded radar and systems |
| 5027 | USA | John F. Kennedy CV-67 | John F. Kennedy CV-67 | Base | CV | Aircraft Carrier | Supercarrier | 1968 | 1968 | 1968 | 90000 | 103499 | 33 | 26.4 | 12000 | 277000000 | 42 | 0 | Last oil-fired CV, unique design |
| 5028 | USA | Nimitz-class (Early) CVN-68/69 | Nimitz-class (Early) CVN-68/69 | Base | CVN | CVN | Nuclear | 1975 | 1975 | 1975 | 10000 | 11500 | 25 | 20.0 | 10000 | 1000000000 | 72 | 0 | 2× A4W reactors, 90+ aircraft |
| 5029 | USA | Nimitz-class (Improved) CVN-70-72 | Nimitz-class (Improved) CVN-70-72 | Base | CVN | CVN | Nuclear | 1981 | 1981 | 1981 | 10000 | 11500 | 25 | 20.0 | 10000 | 1100000000 | 72 | 0 | Upgraded systems and sensors |
| 5030 | USA | Nimitz-class (Late) CVN-73-76 | Nimitz-class (Late) CVN-73-76 | Base | CVN | CVN | Nuclear | 1995 | 1995 | 1995 | 10000 | 11500 | 25 | 20.0 | 10000 | 1200000000 | 72 | 0 | All systems maximized |
| 5031 | USA | Enterprise CVN-80 | Enterprise CVN-80 | Base | CVN | CVN | Future | 2027 | 2027 | 2027 | 10000 | 11500 | 25 | 20.0 | 10000 | 1400000000 | 84 | 0 | Ford systems, proven design |
| 6000 | USA | Chester-class | Chester-class | Base | CL | Light Cruiser | Protected Cruiser | 1908 | 1908 | 1908 | 5000 | 5750 | 25 | 20.0 | 8000 | 1500000 | 24 | 0 | Very Light: -50% armor, +3 kts, FREE |
| 6001 | USA | Omaha-class | Omaha-class | Base | CL | Light Cruiser | Scout Cruiser | 1923 | 1923 | 1923 | 10000 | 11500 | 32 | 25.6 | 8000 | 7000000 | 36 | 0 | 35 kts, 12×6" guns, FREE |
| 6002 | USA | Pensacola-class | Pensacola-class | Base | CA | Heavy Cruiser | Treaty Heavy | 1930 | 1930 | 1930 | 13000 | 14949 | 32 | 25.6 | 10000 | 12000000 | 48 | 0 | 10×8" guns, lightly armored |
| 6003 | USA | Northampton-class | Northampton-class | Base | CA | Heavy Cruiser | Treaty Heavy | 1930 | 1930 | 1930 | 13000 | 14949 | 32 | 25.6 | 10000 | 11000000 | 48 | 0 | 32.5 kts, 9×8" guns |
| 6004 | USA | Brooklyn-class | Brooklyn-class | Base | CL | Light Cruiser | Treaty Light | 1937 | 1937 | 1937 | 10000 | 11500 | 32 | 25.6 | 8000 | 14000000 | 48 | 0 | 15×6" guns, highest ROF |
| 6005 | USA | Portland-class | Portland-class | Base | CA | Heavy Cruiser | Treaty Heavy | 1933 | 1933 | 1933 | 13000 | 14949 | 32 | 25.6 | 10000 | 13000000 | 54 | 0 | 9×8" guns, better armor |
| 6006 | USA | Atlanta-class | Atlanta-class | Base | CLAA | CLAA | AA Cruiser | 1941 | 1941 | 1941 | 10000 | 11500 | 25 | 20.0 | 10000 | 17000000 | 42 | 0 | 16×5" DP, +100% AA effectiveness |
| 6007 | USA | St. Louis-class | St. Louis-class | Base | CL | Light Cruiser | Treaty Light | 1939 | 1939 | 1939 | 10000 | 11500 | 32 | 25.6 | 8000 | 15000000 | 48 | 0 | 15×6" + improved AA |
| 6008 | USA | New Orleans-class | New Orleans-class | Base | CA | Heavy Cruiser | Treaty Heavy | 1934 | 1934 | 1934 | 13000 | 14949 | 32 | 25.6 | 10000 | 15000000 | 60 | 0 | 9×8" guns, all-or-nothing armor |
| 6009 | USA | Wichita-class | Wichita-class | Base | CA | Heavy Cruiser | Pre-War | 1939 | 1939 | 1939 | 13000 | 14949 | 32 | 25.6 | 10000 | 17000000 | 60 | 0 | Brooklyn + 8" guns |
| 6010 | USA | Cleveland-class | Cleveland-class | Base | CL | Light Cruiser | WWII Light | 1942 | 1942 | 1942 | 10000 | 11500 | 32 | 25.6 | 8000 | 28000000 | 36 | 0 | 12×6" guns, 27 ships built |
| 6011 | USA | Oakland-class | Oakland-class | Base | CLAA | CLAA | AA Cruiser | 1943 | 1943 | 1943 | 10000 | 11500 | 25 | 20.0 | 10000 | 21000000 | 42 | 0 | 12×5" DP, radar |
| 6012 | USA | Baltimore-class | Baltimore-class | Base | CA | Heavy Cruiser | WWII Heavy | 1943 | 1943 | 1943 | 13000 | 14949 | 32 | 25.6 | 10000 | 37000000 | 60 | 0 | 9×8", best armor |
| 6013 | USA | Oregon City-class | Oregon City-class | Base | CA | Heavy Cruiser | WWII Heavy | 1946 | 1946 | 1946 | 17000 | 19550 | 33 | 26.4 | 10000 | 40000000 | 60 | 0 | 9×8", single funnel |
| 6014 | USA | Fargo-class | Fargo-class | Base | CL | Light Cruiser | Post-War Light | 1945 | 1945 | 1945 | 15000 | 17250 | 33 | 26.4 | 8000 | 32000000 | 36 | 0 | 12×6", single funnel |
| 6015 | USA | Juneau-class | Juneau-class | Base | CLAA | CLAA | AA Cruiser | 1946 | 1946 | 1946 | 10000 | 11500 | 25 | 20.0 | 10000 | 24000000 | 42 | 0 | 12×5" DP, improved systems |
| 6016 | USA | Des Moines-class | Des Moines-class | Base | CA | Heavy Cruiser | Ultimate Gun | 1948 | 1948 | 1948 | 17000 | 19550 | 33 | 26.4 | 10000 | 47000000 | 66 | 0 | Auto-loading 8-10 rpm per gun |
| 6017 | USA | Worcester-class | Worcester-class | Base | CL | Light Cruiser | Ultimate Light | 1948 | 1948 | 1948 | 15000 | 17250 | 33 | 26.4 | 8000 | 45000000 | 66 | 0 | 6" rapid-fire, 12 rpm |
| 6018 | USA | Boston-class | Boston-class | Base | CAG | CAG | First Missile | 1955 | 1955 | 1955 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 6×8" + Terrier SAM |
| 6019 | USA | Galveston-class | Galveston-class | Base | CLG | CLG | Missile Light | 1958 | 1958 | 1958 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 6×6" + Talos SAM |
| 6020 | USA | Providence-class | Providence-class | Base | CLG | CLG | Missile Light | 1959 | 1959 | 1959 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 3×6" + Terrier SAM |
| 6021 | USA | Norfolk-class | Norfolk-class | Base | DL | DL | Frigate/Light | 1953 | 1953 | 1953 | 10000 | 11500 | 25 | 20.0 | 10000 | 32000000 | 36 | 0 | 8×3", ASW + AA |
| 6022 | USA | Albany-class | Albany-class | Base | CG | CG | Heavy Missile | 1962 | 1962 | 1962 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 104 Talos + 84 Tartar |
| 6023 | USA | Long Beach CGN-9 | Long Beach CGN-9 | Base | CGN | CGN | First Nuclear | 1961 | 1961 | 1961 | 10000 | 11500 | 25 | 20.0 | 10000 | 350000000 | 60 | 0 | Nuclear, unlimited range, UNIQUE |
| 6024 | USA | Leahy-class | Leahy-class | Base | CG | CG | First Purpose CG | 1962 | 1962 | 1962 | 10000 | 11500 | 25 | 20.0 | 10000 | 85000000 | 48 | 0 | Terrier SAM, 9 ships |
| 6025 | USA | Bainbridge CGN-25 | Bainbridge CGN-25 | Base | CGN | CGN | Nuclear Leahy | 1962 | 1962 | 1962 | 10000 | 11500 | 25 | 20.0 | 10000 | 165000000 | 54 | 0 | 2× D2G reactors, UNIQUE |
| 6026 | USA | Belknap-class | Belknap-class | Base | CG | CG | Improved CG | 1964 | 1964 | 1964 | 10000 | 11500 | 25 | 20.0 | 10000 | 95000000 | 48 | 0 | Single 5" gun retained |
| 6027 | USA | Truxtun CGN-35 | Truxtun CGN-35 | Base | CGN | CGN | Nuclear Belknap | 1967 | 1967 | 1967 | 10000 | 11500 | 25 | 20.0 | 10000 | 190000000 | 54 | 0 | 2× D2G reactors, UNIQUE |
| 6028 | USA | Chicago CAG-136 | Chicago CAG-136 | Base | CAG | CAG | Late Conversion | 1964 | 1964 | 1964 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 6×8" + Talos SAM |
| 6029 | USA | California-class | California-class | Base | CGN | CGN | Nuclear Production | 1974 | 1974 | 1974 | 10000 | 11500 | 25 | 20.0 | 10000 | 400000000 | 66 | 0 | 2× D2G reactors, Standard SM-2 |
| 6030 | USA | Virginia-class | Virginia-class | Base | CGN | CGN | Improved Nuclear | 1976 | 1976 | 1976 | 10000 | 11500 | 25 | 20.0 | 10000 | 450000000 | 72 | 0 | 2× D2G reactors, Aegis-ready |
| 6031 | USA | Leahy-class (NTU) | Leahy-class (NTU) | Base | CG | CG | Upgraded Missile | 1980 | 1980 | 1980 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Standard SM-2 missiles |
| 6032 | USA | Belknap-class (NTU) | Belknap-class (NTU) | Base | CG | CG | Upgraded Missile | 1985 | 1985 | 1985 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 1×5" + Standard SM-2 |
| 6033 | USA | Ticonderoga-class (Early) CG-47/48 | Ticonderoga-class (Early) CG-47/48 | Base | CG | CG | Early Aegis | 1983 | 1983 | 1983 | 10000 | 11500 | 25 | 20.0 | 10000 | 800000000 | 78 | 0 | Aegis + Mk 26 twin launchers |
| 6034 | USA | Ticonderoga-class (Baseline 1) CG-49-51 | Ticonderoga-class (Baseline 1) CG-49-51 | Base | CG | CG | Aegis Baseline 1 | 1985 | 1985 | 1985 | 10000 | 11500 | 25 | 20.0 | 10000 | 850000000 | 78 | 0 | Improved Aegis, Mk 26 |
| 6035 | USA | Ticonderoga-class (Baseline 2) CG-52-58 | Ticonderoga-class (Baseline 2) CG-52-58 | Base | CG | CG | Aegis Baseline 2 | 1986 | 1986 | 1986 | 10000 | 11500 | 25 | 20.0 | 10000 | 900000000 | 78 | 0 | SPY-1B radar upgrade |
| 6036 | USA | Virginia-class CGN (Modernized) | Virginia-class CGN (Modernized) | Base | CGN | CGN | Modernized Nuclear | 1988 | 1988 | 1988 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Aegis-ready, Tomahawk |
| 6037 | USA | Strike Cruiser CGN | Strike Cruiser CGN | Base | CGN | CGN | Strike Cruiser | 1975 | 1975 | 1975 | 10000 | 11500 | 25 | 20.0 | 10000 | 900000000 | 84 | 0 | Aegis nuclear, -10% reliability |
| 6038 | USA | Ticonderoga-class (Baseline 3) CG-59-64 | Ticonderoga-class (Baseline 3) CG-59-64 | Base | CG | CG | Aegis VLS Early | 1988 | 1988 | 1988 | 10000 | 11500 | 25 | 20.0 | 10000 | 950000000 | 78 | 0 | First Mk 41 VLS 122 cells |
| 6039 | USA | Ticonderoga-class (Baseline 4) CG-65-73 | Ticonderoga-class (Baseline 4) CG-65-73 | Base | CG | CG | Ultimate Aegis | 1990 | 1990 | 1990 | 10000 | 11500 | 25 | 20.0 | 10000 | 1000000000 | 78 | 0 | Ultimate systems, VLS 122 |
| 6040 | USA | CG(X) Future Cruiser | CG(X) Future Cruiser | Base | CG | CG | Future Cruiser | 2020 | 2020 | 2020 | 10000 | 11500 | 25 | 20.0 | 10000 | 3000000000 | 96 | 0 | Next-gen systems, -10% reliability |
| 7000 | USA | Bainbridge-class | Bainbridge-class | Base | DD | Destroyer | Torpedo Boat Destroyer | 1902 | 1902 | 1902 | 1000 | 1150 | 30 | 24.0 | 5000 | 500000 | 18 | 0 | Very Light: -60% armor, +2 kts, FREE |
| 7001 | USA | Smith-class | Smith-class | Base | DD | Destroyer | Early Destroyer | 1909 | 1909 | 1909 | 1000 | 1150 | 30 | 24.0 | 5000 | 800000 | 24 | 0 | Light Fast: +3 kts, FREE |
| 7002 | USA | Paulding-class | Paulding-class | Base | DD | Destroyer | Pre-WWI | 1910 | 1910 | 1910 | 1000 | 1150 | 30 | 24.0 | 5000 | 950000 | 24 | 0 | Torpedoes + guns |
| 7003 | USA | Cassin-class | Cassin-class | Base | DD | Destroyer | Pre-WWI | 1913 | 1913 | 1913 | 1000 | 1150 | 30 | 24.0 | 5000 | 1100000 | 30 | 0 | Oil fuel, improved range |
| 7004 | USA | Sampson-class | Sampson-class | Base | DD | Destroyer | Pre-WWI | 1916 | 1916 | 1916 | 1000 | 1150 | 30 | 24.0 | 5000 | 1300000 | 30 | 0 | 1,200 tons, 29 kts |
| 7005 | USA | Caldwell-class | Caldwell-class | Base | DD | Destroyer | WWI | 1917 | 1917 | 1917 | 1000 | 1150 | 30 | 24.0 | 5000 | 1500000 | 12 | 0 | Flush deck, 6×4" guns |
| 7006 | USA | Wickes-class | Wickes-class | Base | DD | Destroyer | WWI | 1918 | 1918 | 1918 | 1000 | 1150 | 30 | 24.0 | 5000 | 1600000 | 9 | 0 | 4 stacks, 111 ships |
| 7007 | USA | Clemson-class | Clemson-class | Base | DD | Destroyer | WWI | 1919 | 1919 | 1919 | 1000 | 1150 | 30 | 24.0 | 5000 | 1700000 | 9 | 0 | 4 stacks, 156 ships |
| 7008 | USA | Wickes-class (APD) | Wickes-class (APD) | Base | APD | APD | WWII Conversion | 1943 | 1943 | 1943 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | High-speed, 200 troops |
| 7009 | USA | Farragut-class | Farragut-class | Base | DD | Destroyer | Interwar | 1934 | 1934 | 1934 | 2000 | 2300 | 35 | 28.0 | 5000 | 3800000 | 36 | 0 | Enclosed 5" guns |
| 7010 | USA | Porter-class | Porter-class | Base | DD | Destroyer | Destroyer Leader | 1935 | 1935 | 1935 | 2000 | 2300 | 35 | 28.0 | 5000 | 5500000 | 42 | 0 | 8×5" guns, leader |
| 7011 | USA | Mahan-class | Mahan-class | Base | DD | Destroyer | Interwar | 1936 | 1936 | 1936 | 2000 | 2300 | 35 | 28.0 | 5000 | 4000000 | 36 | 0 | 12 torpedoes |
| 7012 | USA | Gridley-class | Gridley-class | Base | DD | Destroyer | Interwar | 1937 | 1937 | 1937 | 2000 | 2300 | 35 | 28.0 | 5000 | 4200000 | 36 | 0 | 16 torpedoes maximum |
| 7013 | USA | Bagley-class | Bagley-class | Base | DD | Destroyer | Interwar | 1937 | 1937 | 1937 | 2000 | 2300 | 35 | 28.0 | 5000 | 4100000 | 36 | 0 | 16 torpedoes, balanced |
| 7014 | USA | Benham-class | Benham-class | Base | DD | Destroyer | Pre-War | 1939 | 1939 | 1939 | 2000 | 2300 | 35 | 28.0 | 5000 | 4500000 | 42 | 0 | Refined design |
| 7015 | USA | Sims-class | Sims-class | Base | DD | Destroyer | Pre-War | 1939 | 1939 | 1939 | 2000 | 2300 | 35 | 28.0 | 5000 | 4300000 | 42 | 0 | Lighter, faster |
| 7016 | USA | Benson-class | Benson-class | Base | DD | Destroyer | Pre-War | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 5000000 | 42 | 0 | 5×5" guns |
| 7017 | USA | Gleaves-class | Gleaves-class | Base | DD | Destroyer | Pre-War | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 5100000 | 42 | 0 | Similar to Benson |
| 7018 | USA | Bristol-class | Bristol-class | Base | DD | Destroyer | Pre-War | 1941 | 1941 | 1941 | 2000 | 2300 | 35 | 28.0 | 5000 | 5200000 | 42 | 0 | Last pre-war design |
| 7019 | USA | Fletcher-class | Fletcher-class | Base | DD | Destroyer | WWII Workhorse | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 6000000 | 12 | 0 | 5×5" guns, 175 ships |
| 7020 | USA | Fletcher-class (FRAM I) | Fletcher-class (FRAM I) | Base | DD | Destroyer | FRAM Upgrade | 1960 | 1960 | 1960 | 5000 | 5750 | 35 | 28.0 | 5000 | 0 | 0 | 0 | FRAM ASW upgrade |
| 7021 | USA | Allen M. Sumner-class | Allen M. Sumner-class | Base | DD | Destroyer | WWII Heavy | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 7500000 | 15 | 0 | 6×5" guns in 3 twins |
| 7022 | USA | Gearing-class | Gearing-class | Base | DD | Destroyer | Ultimate WWII | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 8000000 | 18 | 0 | Lengthened, more fuel |
| 7023 | USA | Gearing-class (FRAM I) | Gearing-class (FRAM I) | Base | DD | Destroyer | FRAM Upgrade | 1961 | 1961 | 1961 | 5000 | 5750 | 35 | 28.0 | 5000 | 0 | 0 | 0 | Full FRAM upgrade |
| 7024 | USA | Gearing-class (DDR) | Gearing-class (DDR) | Base | DDR | DDR | Radar Picket | 1950 | 1950 | 1950 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Long-range radar |
| 7025 | USA | Forrest Sherman-class | Forrest Sherman-class | Base | DD | Destroyer | First Post-War | 1955 | 1955 | 1955 | 5000 | 5750 | 35 | 28.0 | 5000 | 18000000 | 36 | 0 | Modern 3"/50 guns |
| 7026 | USA | Forrest Sherman-class DDG | Forrest Sherman-class DDG | Base | DDG | DDG | Missile Conversion | 1967 | 1967 | 1967 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Tartar SAM conversion |
| 7027 | USA | Mitscher-class | Mitscher-class | Base | DL | DL | Destroyer Leader | 1953 | 1953 | 1953 | 10000 | 11500 | 25 | 20.0 | 10000 | 22000000 | 42 | 0 | ASW + AA leader |
| 7028 | USA | Farragut/Coontz-class | Farragut/Coontz-class | Base | DDG | DDG | First Missile DD | 1959 | 1959 | 1959 | 10000 | 11500 | 25 | 20.0 | 10000 | 45000000 | 48 | 0 | Terrier SAM, 10 ships |
| 7029 | USA | Charles F. Adams-class | Charles F. Adams-class | Base | DDG | DDG | Tartar DDG | 1960 | 1960 | 1960 | 10000 | 11500 | 25 | 20.0 | 10000 | 38000000 | 42 | 0 | Tartar SAM, 23 ships |
| 7030 | USA | Charles F. Adams-class (NTU) | Charles F. Adams-class (NTU) | Base | DDG | DDG | NTU Upgrade | 1982 | 1982 | 1982 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Standard missiles |
| 7031 | USA | Spruance-class | Spruance-class | Base | DD | Destroyer | Gas Turbine DD | 1975 | 1975 | 1975 | 5000 | 5750 | 35 | 28.0 | 5000 | 125000000 | 36 | 0 | Gas turbine, 31 ships |
| 7032 | USA | Spruance-class (VLS) | Spruance-class (VLS) | Base | DD | Destroyer | VLS Upgrade | 1989 | 1989 | 1989 | 5000 | 5750 | 35 | 28.0 | 5000 | 0 | 0 | 0 | 61-cell Mk 41 VLS |
| 7033 | USA | Kidd-class | Kidd-class | Base | DDG | DDG | Modified Spruance | 1981 | 1981 | 1981 | 10000 | 11500 | 25 | 20.0 | 10000 | 135000000 | 36 | 0 | Modified Spruance, 4 ships |
| 7034 | USA | Arleigh Burke-class (Flight I) DDG-51-71 | Arleigh Burke-class (Flight I) DDG-51-71 | Base | DDG | DDG | Early Aegis DD | 1991 | 1991 | 1991 | 10000 | 11500 | 25 | 20.0 | 10000 | 900000000 | 72 | 0 | Aegis SPY-1D, 90 VLS |
| 7035 | USA | Arleigh Burke-class (Flight II) DDG-72-78 | Arleigh Burke-class (Flight II) DDG-72-78 | Base | DDG | DDG | Improved Aegis DD | 1998 | 1998 | 1998 | 10000 | 11500 | 25 | 20.0 | 10000 | 950000000 | 72 | 0 | Upgraded electronics |
| 7036 | USA | Arleigh Burke-class (Flight IIA) DDG-79-112 | Arleigh Burke-class (Flight IIA) DDG-79-112 | Base | DDG | DDG | Aegis with Helo | 2000 | 2000 | 2000 | 10000 | 11500 | 25 | 20.0 | 10000 | 1000000000 | 72 | 0 | Helo hangar, 96 VLS |
| 7037 | USA | Arleigh Burke-class (Flight III) DDG-113+ | Arleigh Burke-class (Flight III) DDG-113+ | Base | DDG | DDG | Ultimate Aegis | 2016 | 2016 | 2016 | 10000 | 11500 | 25 | 20.0 | 10000 | 1200000000 | 72 | 0 | SPY-6 radar, ultimate |
| 7038 | USA | Zumwalt-class | Zumwalt-class | Base | DDG | DDG | Stealth Destroyer | 2016 | 2016 | 2016 | 10000 | 11500 | 25 | 20.0 | 10000 | 3500000000 | 84 | 0 | Stealth, 80 VLS, 3 ships |
| 7039 | USA | Arleigh Burke-class (Flight IV) | Arleigh Burke-class (Flight IV) | Base | DDG | DDG | Future Aegis | 2030 | 2030 | 2030 | 10000 | 11500 | 25 | 20.0 | 10000 | 1400000000 | 78 | 0 | Hypersonic missiles planned |
| 7040 | USA | DDG(X) Future Destroyer | DDG(X) Future Destroyer | Base | DDG | DDG | Next-Gen | 2040 | 2040 | 2040 | 10000 | 11500 | 25 | 20.0 | 10000 | 4000000000 | 96 | 0 | Next-gen, -10% reliability |
| 8000 | USA | Holland-class | Holland-class | Base | SS | Submarine | Early Submarine | 1900 | 1900 | 1900 | 500 | 575 | 15 | 12.0 | 8000 | 150000 | 12 | 0 | Primitive: -40% diving, FREE |
| 8001 | USA | A-class | A-class | Base | SS | Submarine | Early Submarine | 1903 | 1903 | 1903 | 500 | 575 | 15 | 12.0 | 8000 | 250000 | 18 | 0 | Gasoline: +20% range, FREE |
| 8002 | USA | C-class | C-class | Base | SS | Submarine | Coastal | 1908 | 1908 | 1908 | 500 | 575 | 15 | 12.0 | 8000 | 400000 | 24 | 0 | Coastal operations |
| 8003 | USA | F-class | F-class | Base | SS | Submarine | Coastal | 1912 | 1912 | 1912 | 500 | 575 | 15 | 12.0 | 8000 | 500000 | 24 | 0 | Better dive depth |
| 8004 | USA | H-class | H-class | Base | SS | Submarine | WWI Era | 1913 | 1913 | 1913 | 500 | 575 | 15 | 12.0 | 8000 | 600000 | 30 | 0 | 18 ships built |
| 8005 | USA | L-class | L-class | Base | SS | Submarine | WWI | 1916 | 1916 | 1916 | 500 | 575 | 15 | 12.0 | 8000 | 900000 | 36 | 0 | Ocean-going capable |
| 8006 | USA | O-class | O-class | Base | SS | Submarine | WWI | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 1000000 | 36 | 0 | Better range |
| 8007 | USA | R-class | R-class | Base | SS | Submarine | WWI | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 1100000 | 42 | 0 | First diesel-electric |
| 8008 | USA | S-class | S-class | Base | SS | Submarine | Interwar | 1920 | 1920 | 1920 | 1500 | 1724 | 15 | 12.0 | 8000 | 1400000 | 42 | 0 | 48 ships, long service |
| 8009 | USA | V-class | V-class | Base | SS | Submarine | Experimental | 1924 | 1924 | 1924 | 1500 | 1724 | 15 | 12.0 | 8000 | 5000000 | 60 | 0 | 6" deck gun, 2,000 tons |
| 8010 | USA | Porpoise-class | Porpoise-class | Base | SS | Submarine | Pre-War | 1935 | 1935 | 1935 | 1500 | 1724 | 15 | 12.0 | 8000 | 2500000 | 48 | 0 | All-welded hull |
| 8011 | USA | Salmon-class | Salmon-class | Base | SS | Submarine | Pre-War | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 2700000 | 48 | 0 | Better engines |
| 8012 | USA | Sargo-class | Sargo-class | Base | SS | Submarine | Pre-War | 1939 | 1939 | 1939 | 1500 | 1724 | 15 | 12.0 | 8000 | 2800000 | 48 | 0 | Pre-war pinnacle |
| 8013 | USA | Tambor-class | Tambor-class | Base | SS | Submarine | Early WWII | 1940 | 1940 | 1940 | 1500 | 1724 | 15 | 12.0 | 8000 | 3000000 | 54 | 0 | War-ready design |
| 8014 | USA | Gar-class | Gar-class | Base | SS | Submarine | Early WWII | 1941 | 1941 | 1941 | 1500 | 1724 | 15 | 12.0 | 8000 | 3100000 | 54 | 0 | Improved Tambor |
| 8015 | USA | Mackerel-class | Mackerel-class | Base | SS | Submarine | Training | 1953 | 1953 | 1953 | 3000 | 3449 | 20 | 16.0 | 8000 | 1000000 | 18 | 0 | Small patrol/training |
| 8016 | USA | Barracuda-class | Barracuda-class | Base | SST | SST | Training | 1951 | 1951 | 1951 | 10000 | 11500 | 25 | 20.0 | 10000 | 1500000 | 24 | 0 | Dedicated trainer SST |
| 8017 | USA | Gato-class | Gato-class | Base | SS | Submarine | WWII Workhorse | 1941 | 1941 | 1941 | 1500 | 1724 | 15 | 12.0 | 8000 | 3500000 | 12 | 0 | First mass WWII class |
| 8018 | USA | Balao-class | Balao-class | Base | SS | Submarine | Ultimate Diesel | 1942 | 1942 | 1942 | 1500 | 1724 | 15 | 12.0 | 8000 | 3700000 | 12 | 0 | 400ft test depth |
| 8019 | USA | Tench-class | Tench-class | Base | SS | Submarine | Peak Diesel | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 3900000 | 15 | 0 | Ultimate WWII diesel |
| 8020 | USA | Balao-class (GUPPY) | Balao-class (GUPPY) | Base | SS | Submarine | GUPPY Upgrade | 1947 | 1947 | 1947 | 3000 | 3449 | 20 | 16.0 | 8000 | 0 | 0 | 0 | Snorkel, streamlined |
| 8021 | USA | Tench-class (GUPPY IIA) | Tench-class (GUPPY IIA) | Base | SS | Submarine | Full GUPPY | 1952 | 1952 | 1952 | 3000 | 3449 | 20 | 16.0 | 8000 | 0 | 0 | 0 | Full modernization |
| 8022 | USA | Nautilus SSN-571 | Nautilus SSN-571 | Base | SSN | SSN | First Nuclear | 1954 | 1954 | 1954 | 10000 | 11500 | 25 | 20.0 | 10000 | 55000000 | 60 | 0 | First nuclear, unlimited range, UNIQUE |
| 8023 | USA | Seawolf SSN-575 | Seawolf SSN-575 | Base | SSN | SSN | Experimental | 1957 | 1957 | 1957 | 10000 | 11500 | 25 | 20.0 | 10000 | 65000000 | 60 | 0 | Sodium reactor, UNIQUE |
| 8024 | USA | Skate-class | Skate-class | Base | SSN | SSN | Production Nuclear | 1957 | 1957 | 1957 | 10000 | 11500 | 25 | 20.0 | 10000 | 45000000 | 54 | 0 | 4 ships, production |
| 8025 | USA | George Washington-class | George Washington-class | Base | SSBN | SSBN | First SSBN | 1959 | 1959 | 1959 | 10000 | 11500 | 25 | 20.0 | 10000 | 110000000 | 66 | 0 | First ballistic missiles |
| 8026 | USA | Ethan Allen-class | Ethan Allen-class | Base | SSBN | SSBN | Improved SSBN | 1961 | 1961 | 1961 | 10000 | 11500 | 25 | 20.0 | 10000 | 125000000 | 66 | 0 | Better missiles |
| 8027 | USA | Skipjack-class | Skipjack-class | Base | SSN | SSN | Teardrop Hull | 1959 | 1959 | 1959 | 10000 | 11500 | 25 | 20.0 | 10000 | 50000000 | 60 | 0 | Teardrop, 30+ kts |
| 8028 | USA | Thresher/Permit-class | Thresher/Permit-class | Base | SSN | SSN | Deep-Diving SSN | 1961 | 1961 | 1961 | 10000 | 11500 | 25 | 20.0 | 10000 | 75000000 | 66 | 0 | 1,300ft test depth |
| 8029 | USA | Sturgeon-class | Sturgeon-class | Base | SSN | SSN | Long-Serving SSN | 1967 | 1967 | 1967 | 10000 | 11500 | 25 | 20.0 | 10000 | 85000000 | 72 | 0 | 37 ships, most numerous |
| 8030 | USA | Lafayette-class | Lafayette-class | Base | SSBN | SSBN | Mass SSBN | 1963 | 1963 | 1963 | 10000 | 11500 | 25 | 20.0 | 10000 | 140000000 | 72 | 0 | 16 Poseidon, 31 ships |
| 8031 | USA | Benjamin Franklin-class | Benjamin Franklin-class | Base | SSBN | SSBN | Ultimate Polaris | 1965 | 1965 | 1965 | 10000 | 11500 | 25 | 20.0 | 10000 | 150000000 | 72 | 0 | Quieter Lafayette |
| 8032 | USA | Los Angeles-class (Early) SSN-688-699 | Los Angeles-class (Early) SSN-688-699 | Base | SSN | SSN | Fast Attack | 1974 | 1974 | 1974 | 10000 | 11500 | 25 | 20.0 | 10000 | 200000000 | 78 | 0 | Fast, 62 total ships |
| 8033 | USA | Los Angeles-class (Improved 688i) SSN-700-773 | Los Angeles-class (Improved 688i) SSN-700-773 | Base | SSN | SSN | VLS-Capable | 1981 | 1981 | 1981 | 10000 | 11500 | 25 | 20.0 | 10000 | 225000000 | 78 | 0 | 12 VLS Tomahawk |
| 8034 | USA | Ohio-class | Ohio-class | Base | SSBN | SSBN | Strategic Sub | 1981 | 1981 | 1981 | 10000 | 11500 | 25 | 20.0 | 10000 | 1500000000 | 84 | 0 | 24 Trident II missiles |
| 8035 | USA | Ohio-class (SSGN) | Ohio-class (SSGN) | Base | SSGN | SSGN | Cruise Missile | 2006 | 2006 | 2006 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | 154 Tomahawk missiles |
| 8036 | USA | Seawolf-class | Seawolf-class | Base | SSN | SSN | Ultimate Attack | 1997 | 1997 | 1997 | 10000 | 11500 | 25 | 20.0 | 10000 | 2800000000 | 96 | 0 | Ultimate but $2.8B |
| 8037 | USA | Virginia-class | Virginia-class | Base | SSN | SSN | Current Production | 2004 | 2004 | 2004 | 10000 | 11500 | 25 | 20.0 | 10000 | 1800000000 | 84 | 0 | Affordable, modular |
| 8038 | USA | Columbia-class | Columbia-class | Base | SSBN | SSBN | Future SSBN | 2028 | 2028 | 2028 | 10000 | 11500 | 25 | 20.0 | 10000 | 9000000000 | 108 | 0 | 16 Trident II D5 |
| 2000 | British | Majestic-class | Majestic-class | Base | BB | Battleship | Pre-Dreadnought | 1895 | 1895 | 1895 | 12000 | 13799 | 18 | 14.4 | 15000 | 500000 | 36 | 0 | Primitive: -40% armor, FREE |
| 2001 | British | Lord Nelson-class | Lord Nelson-class | Base | BB | Battleship | Pre-Dreadnought | 1908 | 1908 | 1908 | 20000 | 23000 | 21 | 16.8 | 15000 | 1500000 | 48 | 0 | Transitional design, FREE |
| 2002 | British | HMS Dreadnought | HMS Dreadnought | Base | BB | Battleship | Dreadnought | 1906 | 1906 | 1906 | 20000 | 23000 | 21 | 16.8 | 15000 | 3000000 | 18 | 0 | First dreadnought, +30% accuracy, UNIQUE |
| 2003 | British | Bellerophon-class | Bellerophon-class | Base | BB | Battleship | Dreadnought | 1909 | 1909 | 1909 | 20000 | 23000 | 21 | 16.8 | 15000 | 3500000 | 24 | 0 | Better secondaries |
| 2004 | British | St Vincent-class | St Vincent-class | Base | BB | Battleship | Dreadnought | 1910 | 1910 | 1910 | 20000 | 23000 | 21 | 16.8 | 15000 | 4000000 | 30 | 0 | +10% penetration |
| 2005 | British | HMS Neptune | HMS Neptune | Base | BB | Battleship | Dreadnought | 1911 | 1911 | 1911 | 20000 | 23000 | 21 | 16.8 | 15000 | 4500000 | 36 | 0 | +15% firepower |
| 2006 | British | Colossus-class | Colossus-class | Base | BB | Battleship | Dreadnought | 1911 | 1911 | 1911 | 20000 | 23000 | 21 | 16.8 | 15000 | 5000000 | 36 | 0 | +10% armor |
| 2007 | British | HMS Agincourt | HMS Agincourt | Base | BB | Battleship | Dreadnought | 1914 | 1914 | 1914 | 20000 | 23000 | 21 | 16.8 | 15000 | 6000000 | 42 | 0 | 14 main guns, UNIQUE |
| 2008 | British | Orion-class | Orion-class | Base | BB | Battleship | Super-Dreadnought | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 6500000 | 42 | 0 | First 13.5" guns, +15% penetration |
| 2009 | British | King George V (1912) | King George V (1912) | Base | BB | Battleship | Super-Dreadnought | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 7000000 | 48 | 0 | +5% speed |
| 2010 | British | Iron Duke-class | Iron Duke-class | Base | BB | Battleship | Super-Dreadnought | 1914 | 1914 | 1914 | 20000 | 23000 | 21 | 16.8 | 15000 | 7500000 | 48 | 0 | +10% gunnery, UNIQUE |
| 2011 | British | HMS Erin | HMS Erin | Base | BB | Battleship | Super-Dreadnought | 1914 | 1914 | 1914 | 20000 | 23000 | 21 | 16.8 | 15000 | 7000000 | 42 | 0 | Foreign design |
| 2012 | British | Queen Elizabeth-class | Queen Elizabeth-class | Base | BB | Battleship | Fast Battleship | 1915 | 1915 | 1915 | 32000 | 36800 | 23 | 18.4 | 15000 | 10000000 | 54 | 0 | +20% speed, +15% range |
| 2013 | British | HMS Canada | HMS Canada | Base | BB | Battleship | Fast Battleship | 1915 | 1915 | 1915 | 32000 | 36800 | 23 | 18.4 | 15000 | 8000000 | 48 | 0 | +15% speed |
| 2014 | British | Revenge-class | Revenge-class | Base | BB | Battleship | WWI Battleship | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 9000000 | 54 | 0 | -15% cost, -10% speed |
| 2015 | British | HMS Ramillies | HMS Ramillies | Base | BB | Battleship | WWI Battleship | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 9000000 | 54 | 0 | +5% torpedo defense |
| 2016 | British | HMS Royal Sovereign | HMS Royal Sovereign | Base | BB | Battleship | WWI Battleship | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 9000000 | 54 | 0 | +5% command |
| 2017 | British | HMS Royal Oak | HMS Royal Oak | Base | BB | Battleship | WWI Battleship | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 9000000 | 54 | 0 | Historical significance |
| 2018 | British | Renown-class | Renown-class | Base | BC | BC | Battlecruiser | 1916 | 1916 | 1916 | 10000 | 11500 | 25 | 20.0 | 10000 | 8500000 | 48 | 0 | +30% speed, -20% armor |
| 2019 | British | HMS Repulse | HMS Repulse | Base | BC | BC | Battlecruiser | 1916 | 1916 | 1916 | 10000 | 11500 | 25 | 20.0 | 10000 | 8500000 | 48 | 0 | +30% speed, -20% armor |
| 2020 | British | HMS Hood | HMS Hood | Base | BC | BC | Battlecruiser | 1920 | 1920 | 1920 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 60 | 0 | +25% prestige, +15% speed, -20% armor |
| 2021 | British | HMS Courageous | HMS Courageous | Base | BC | BC | Light Battlecruiser | 1917 | 1917 | 1917 | 10000 | 11500 | 25 | 20.0 | 10000 | 7000000 | 36 | 0 | +35% speed, -30% armor |
| 2022 | British | HMS Nelson | HMS Nelson | Base | BB | Battleship | Treaty Battleship | 1927 | 1927 | 1927 | 35000 | 40250 | 23 | 18.4 | 15000 | 15000000 | 66 | 0 | +20% forward firepower, UNIQUE |
| 2023 | British | HMS Rodney | HMS Rodney | Base | BB | Battleship | Treaty Battleship | 1927 | 1927 | 1927 | 35000 | 40250 | 23 | 18.4 | 15000 | 15000000 | 66 | 0 | +15% critical hits |
| 2024 | British | King George V (1940) | King George V (1940) | Base | BB | Battleship | WWII Battleship | 1940 | 1940 | 1940 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 72 | 0 | +15% AA, +10% reliability |
| 2025 | British | HMS Prince of Wales | HMS Prince of Wales | Base | BB | Battleship | WWII Battleship | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 72 | 0 | +15% AA |
| 2026 | British | HMS Duke of York | HMS Duke of York | Base | BB | Battleship | WWII Battleship | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 72 | 0 | +15% night combat |
| 2027 | British | HMS Anson | HMS Anson | Base | BB | Battleship | WWII Battleship | 1942 | 1942 | 1942 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 72 | 0 | +10% endurance |
| 2028 | British | HMS Howe | HMS Howe | Base | BB | Battleship | WWII Battleship | 1942 | 1942 | 1942 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 72 | 0 | +10% reliability |
| 2029 | British | HMS Vanguard | HMS Vanguard | Base | BB | Battleship | Last Battleship | 1946 | 1946 | 1946 | 50000 | 57499 | 30 | 24.0 | 15000 | 50000000 | 84 | 0 | +20% all stats, never saw combat, UNIQUE |
| 2030 | British | Queen Elizabeth (Mod) | Queen Elizabeth (Mod) | Base | BB | Battleship | Modernized BB | 1937 | 1937 | 1937 | 45000 | 51749 | 30 | 24.0 | 15000 | 5000000 | 24 | 0 | +15% AA, +10% FCS |
| 2031 | British | HMS Warspite (Mod) | HMS Warspite (Mod) | Base | BB | Battleship | Modernized BB | 1937 | 1937 | 1937 | 45000 | 51749 | 30 | 24.0 | 15000 | 5000000 | 24 | 0 | +15% accuracy, UNIQUE |
| 2032 | British | Renown (Modernized) | Renown (Modernized) | Base | BC | BC | Modernized BC | 1939 | 1939 | 1939 | 10000 | 11500 | 25 | 20.0 | 10000 | 6000000 | 30 | 0 | +10% armor, +15% AA |
| 2033 | British | Nelson (Modernized) | Nelson (Modernized) | Base | BB | Battleship | Modernized BB | 1940 | 1940 | 1940 | 45000 | 51749 | 30 | 24.0 | 15000 | 7000000 | 18 | 0 | +20% AA |
| 2034 | British | King George V (Mod) | King George V (Mod) | Base | BB | Battleship | Modernized BB | 1945 | 1945 | 1945 | 50000 | 57499 | 30 | 24.0 | 15000 | 4000000 | 12 | 0 | +10% all systems |
| 2035 | British | Lion-class (1939) | Lion-class (1939) | Base | BB | Battleship | Cancelled BB | 1939 | 1939 | 1939 | 45000 | 51749 | 30 | 24.0 | 15000 | 45000000 | 84 | 0 | -10% reliability, +15% firepower |
| 2036 | British | G3 Battlecruiser | G3 Battlecruiser | Base | BC | BC | Cancelled BC | 1921 | 1921 | 1921 | 10000 | 11500 | 25 | 20.0 | 10000 | 40000000 | 78 | 0 | -10% reliability, +20% speed |
| 2037 | British | N3 Battleship | N3 Battleship | Base | BB | Battleship | Cancelled BB | 1921 | 1921 | 1921 | 32000 | 36800 | 23 | 18.4 | 15000 | 50000000 | 90 | 0 | -10% reliability, +25% firepower |
| 2038 | British | Super Lion | Super Lion | Base | BB | Battleship | Cancelled BB | 1940 | 1940 | 1940 | 45000 | 51749 | 30 | 24.0 | 15000 | 60000000 | 96 | 0 | -10% reliability |
| 2039 | British | HMS Incomparable | HMS Incomparable | Base | BC | BC | Cancelled BC | 1915 | 1915 | 1915 | 10000 | 11500 | 25 | 20.0 | 10000 | 30000000 | 72 | 0 | -20% reliability, +30% firepower |
| 2100 | British | HMS Furious (1917) | HMS Furious (1917) | Base | CV | Aircraft Carrier | WWI Conversion | 1917 | 1917 | 1917 | 25000 | 28749 | 30 | 24.0 | 12000 | 2000000 | 24 | 0 | First carrier operations, FREE |
| 2101 | British | HMS Argus | HMS Argus | Base | CV | Aircraft Carrier | WWI Conversion | 1918 | 1918 | 1918 | 25000 | 28749 | 30 | 24.0 | 12000 | 2500000 | 30 | 0 | +10% landing safety, FREE |
| 2102 | British | HMS Courageous | HMS Courageous | Base | CV | Aircraft Carrier | Large Conversion | 1928 | 1928 | 1928 | 25000 | 28749 | 30 | 24.0 | 12000 | 5000000 | 36 | 0 | +25% aircraft capacity |
| 2103 | British | HMS Glorious | HMS Glorious | Base | CV | Aircraft Carrier | Large Conversion | 1930 | 1930 | 1930 | 30000 | 34500 | 30 | 24.0 | 12000 | 5000000 | 36 | 0 | +28 kts, fast carrier |
| 2104 | British | HMS Furious (Reconstructed) | HMS Furious (Reconstructed) | Base | CV | Aircraft Carrier | Full Conversion | 1925 | 1925 | 1925 | 25000 | 28749 | 30 | 24.0 | 12000 | 8000000 | 48 | 0 | +20% efficiency |
| 2105 | British | HMS Hermes (1924) | HMS Hermes (1924) | Base | CV | Aircraft Carrier | Purpose-Built | 1924 | 1924 | 1924 | 25000 | 28749 | 30 | 24.0 | 12000 | 6000000 | 42 | 0 | +15% reliability |
| 2106 | British | HMS Eagle (1924) | HMS Eagle (1924) | Base | CV | Aircraft Carrier | Conversion | 1924 | 1924 | 1924 | 25000 | 28749 | 30 | 24.0 | 12000 | 7000000 | 48 | 0 | Large hangar capacity |
| 2107 | British | HMS Ark Royal (1938) | HMS Ark Royal (1938) | Base | CV | Aircraft Carrier | Fleet Carrier | 1938 | 1938 | 1938 | 30000 | 34500 | 30 | 24.0 | 12000 | 10000000 | 54 | 0 | +30% aircraft capacity |
| 2108 | British | HMS Illustrious | HMS Illustrious | Base | CV | Aircraft Carrier | Armored Fleet | 1940 | 1940 | 1940 | 35000 | 40250 | 33 | 26.4 | 12000 | 15000000 | 60 | 0 | +50% bomb resistance |
| 2109 | British | HMS Formidable | HMS Formidable | Base | CV | Aircraft Carrier | Armored Fleet | 1940 | 1940 | 1940 | 35000 | 40250 | 33 | 26.4 | 12000 | 15000000 | 60 | 0 | +25% night strike capability |
| 2110 | British | HMS Victorious | HMS Victorious | Base | CV | Aircraft Carrier | Armored Fleet | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 15000000 | 60 | 0 | +20% endurance |
| 2111 | British | HMS Indomitable | HMS Indomitable | Base | CV | Aircraft Carrier | Armored Fleet | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 16000000 | 60 | 0 | +33% aircraft capacity |
| 2112 | British | HMS Implacable | HMS Implacable | Base | CV | Aircraft Carrier | Armored Improved | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 18000000 | 66 | 0 | +15% resistance |
| 2113 | British | HMS Indefatigable | HMS Indefatigable | Base | CV | Aircraft Carrier | Armored Improved | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 18000000 | 66 | 0 | +10% structural strength |
| 2114 | British | HMS Colossus | HMS Colossus | Base | CVL | CVL | Light Fleet | 1944 | 1944 | 1944 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 48 | 0 | -30% cost, mass production |
| 2115 | British | HMS Glory | HMS Glory | Base | CVL | CVL | Light Fleet | 1945 | 1945 | 1945 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 48 | 0 | ASW +20% |
| 2116 | British | HMS Majestic | HMS Majestic | Base | CVL | CVL | Light Fleet | 1948 | 1948 | 1948 | 10000 | 11500 | 25 | 20.0 | 10000 | 13000000 | 48 | 0 | Allied cooperation bonus |
| 2117 | British | HMS Magnificent | HMS Magnificent | Base | CVL | CVL | Light Fleet | 1948 | 1948 | 1948 | 10000 | 11500 | 25 | 20.0 | 10000 | 13000000 | 48 | 0 | +15% efficiency |
| 2118 | British | HMS Eagle (1951) | HMS Eagle (1951) | Base | CV | Aircraft Carrier | Postwar Fleet | 1951 | 1951 | 1951 | 45000 | 51749 | 33 | 26.4 | 12000 | 50000000 | 72 | 0 | +30% sortie rate |
| 2119 | British | HMS Ark Royal (1955) | HMS Ark Royal (1955) | Base | CV | Aircraft Carrier | Postwar Fleet | 1955 | 1955 | 1955 | 45000 | 51749 | 33 | 26.4 | 12000 | 55000000 | 72 | 0 | Heavy aircraft capable |
| 2120 | British | HMS Ark Royal (Modernized) | HMS Ark Royal (Modernized) | Base | CV | Aircraft Carrier | Modernized Fleet | 1970 | 1970 | 1970 | 90000 | 103499 | 33 | 26.4 | 12000 | 75000000 | 84 | 0 | Modern jets +40% |
| 2121 | British | HMS Centaur | HMS Centaur | Base | CVL | CVL | Light Fleet | 1953 | 1953 | 1953 | 10000 | 11500 | 25 | 20.0 | 10000 | 40000000 | 60 | 0 | +20% versatility |
| 2122 | British | HMS Albion | HMS Albion | Base | CVL | CVL | Light Fleet | 1954 | 1954 | 1954 | 10000 | 11500 | 25 | 20.0 | 10000 | 40000000 | 60 | 0 | Amphibious +25% |
| 2123 | British | HMS Bulwark | HMS Bulwark | Base | CVL | CVL | Light Fleet | 1954 | 1954 | 1954 | 10000 | 11500 | 25 | 20.0 | 10000 | 40000000 | 60 | 0 | Marine ops +30% |
| 2124 | British | HMS Hermes (1959) | HMS Hermes (1959) | Base | CV | Aircraft Carrier | Light Fleet | 1959 | 1959 | 1959 | 45000 | 51749 | 33 | 26.4 | 12000 | 50000000 | 66 | 0 | +25% reliability |
| 2125 | British | HMS Invincible | HMS Invincible | Base | CVS | CVS | VSTOL Carrier | 1980 | 1980 | 1980 | 10000 | 11500 | 25 | 20.0 | 10000 | 300000000 | 72 | 0 | Sea Harrier capable |
| 2126 | British | HMS Illustrious (1982) | HMS Illustrious (1982) | Base | CVS | CVS | VSTOL Carrier | 1982 | 1982 | 1982 | 10000 | 11500 | 25 | 20.0 | 10000 | 300000000 | 72 | 0 | +20% combat experience |
| 2127 | British | HMS Ark Royal (1985) | HMS Ark Royal (1985) | Base | CVS | CVS | VSTOL Carrier | 1985 | 1985 | 1985 | 10000 | 11500 | 25 | 20.0 | 10000 | 300000000 | 72 | 0 | +15% VSTOL efficiency |
| 2128 | British | HMS Queen Elizabeth (2017) | HMS Queen Elizabeth (2017) | Base | CVN | CVN | Supercarrier | 2017 | 2017 | 2017 | 10000 | 11500 | 25 | 20.0 | 10000 | 4000000000 | 96 | 0 | 40 F-35B, largest UK warship |
| 2129 | British | HMS Prince of Wales | HMS Prince of Wales | Base | CVN | CVN | Supercarrier | 2019 | 2019 | 2019 | 10000 | 11500 | 25 | 20.0 | 10000 | 4000000000 | 96 | 0 | 5th-gen stealth fighters |
| 2130 | British | HMS Queen Elizabeth (Enhanced) | HMS Queen Elizabeth (Enhanced) | Base | CVN | CVN | Future Supercarrier | 2030 | 2030 | 2030 | 10000 | 11500 | 25 | 20.0 | 10000 | 5000000000 | 108 | 0 | +50% sortie rate |
| 2131 | British | HMS Illustrious (1945 Refit) | HMS Illustrious (1945 Refit) | Base | CV | Aircraft Carrier | Modernization | 1945 | 1945 | 1945 | 45000 | 51749 | 33 | 26.4 | 12000 | 8000000 | 18 | 0 | Jet capable |
| 2132 | British | HMS Victorious (1950s Recon) | HMS Victorious (1950s Recon) | Base | CV | Aircraft Carrier | Modernization | 1958 | 1958 | 1958 | 45000 | 51749 | 33 | 26.4 | 12000 | 30000000 | 36 | 0 | +40% capability |
| 2133 | British | HMS Hermes (1980s Refit) | HMS Hermes (1980s Refit) | Base | CV | Aircraft Carrier | Modernization | 1981 | 1981 | 1981 | 90000 | 103499 | 33 | 26.4 | 12000 | 100000000 | 24 | 0 | VSTOL conversion |
| 2134 | British | HMS Invincible (Modernized) | HMS Invincible (Modernized) | Base | CVS | CVS | Modernization | 1995 | 1995 | 1995 | 10000 | 11500 | 25 | 20.0 | 10000 | 150000000 | 30 | 0 | +25% systems |
| 2135 | British | HMS Malta | HMS Malta | Base | CV | Aircraft Carrier | Cancelled CV | 1945 | 1945 | 1945 | 45000 | 51749 | 33 | 26.4 | 12000 | 60000000 | 84 | 0 | Large fleet carrier |
| 2136 | British | HMS Gibraltar | HMS Gibraltar | Base | CV | Aircraft Carrier | Cancelled CV | 1945 | 1945 | 1945 | 45000 | 51749 | 33 | 26.4 | 12000 | 60000000 | 84 | 0 | Production efficiency |
| 2137 | British | CVA-01 | CVA-01 | Base | CV | Aircraft Carrier | Cancelled Supercarrier | 1966 | 1966 | 1966 | 90000 | 103499 | 33 | 26.4 | 12000 | 500000000 | 96 | 0 | Modern supercarrier concept |
| 2138 | British | CVA-01 Improved | CVA-01 Improved | Base | CV | Aircraft Carrier | Cancelled Variant | 1966 | 1966 | 1966 | 90000 | 103499 | 33 | 26.4 | 12000 | 550000000 | 96 | 0 | Extended range |
| 2139 | British | Future Carrier Concept | Future Carrier Concept | Base | CVN | CVN | Future Design | 2040 | 2040 | 2040 | 10000 | 11500 | 25 | 20.0 | 10000 | 6000000000 | 120 | 0 | Next-generation |
| 2600 | British | Pelorus-class | Pelorus-class | Base | CL | Light Cruiser | Protected Cruiser | 1896 | 1896 | 1896 | 5000 | 5750 | 25 | 20.0 | 8000 | 750000 | 36 | 0 | Primitive: -30% armor, FREE |
| 2601 | British | Leander-class (1931) | Leander-class (1931) | Base | CL | Light Cruiser | Light Cruiser | 1931 | 1931 | 1931 | 10000 | 11500 | 32 | 25.6 | 8000 | 2000000 | 36 | 0 | Empire Reach: +15% range, FREE |
| 2602 | British | Cressy-class | Cressy-class | Base | CA | Heavy Cruiser | Protected Cruiser | 1900 | 1900 | 1900 | 10000 | 11500 | 25 | 20.0 | 10000 | 1000000 | 42 | 0 | Royal Navy Standards: +10% reliability |
| 2603 | British | Drake-class | Drake-class | Base | CA | Heavy Cruiser | Armored Cruiser | 1901 | 1901 | 1901 | 10000 | 11500 | 25 | 20.0 | 10000 | 1500000 | 48 | 0 | Better armor protection |
| 2604 | British | Warrior-class | Warrior-class | Base | CA | Heavy Cruiser | Armored Cruiser | 1905 | 1905 | 1905 | 10000 | 11500 | 25 | 20.0 | 10000 | 1800000 | 48 | 0 | Enhanced firepower |
| 2605 | British | Duke of Edinburgh-class | Duke of Edinburgh-class | Base | CA | Heavy Cruiser | Armored Cruiser | 1906 | 1906 | 1906 | 10000 | 11500 | 25 | 20.0 | 10000 | 2000000 | 54 | 0 | Balanced design philosophy |
| 2606 | British | Devonshire-class | Devonshire-class | Base | CA | Heavy Cruiser | Armored Cruiser | 1904 | 1904 | 1904 | 10000 | 11500 | 25 | 20.0 | 10000 | 2200000 | 54 | 0 | Final armored cruiser design |
| 2607 | British | Monmouth-class | Monmouth-class | Base | CA | Heavy Cruiser | Armored Cruiser | 1903 | 1903 | 1903 | 10000 | 11500 | 25 | 20.0 | 10000 | 2400000 | 60 | 0 | Last armored cruiser class |
| 2608 | British | Town-class (1910) | Town-class (1910) | Base | CL | Light Cruiser | Scout Cruiser | 1910 | 1910 | 1910 | 5000 | 5750 | 25 | 20.0 | 8000 | 1200000 | 36 | 0 | Light, fast scouting |
| 2609 | British | Arethusa-class (1913) | Arethusa-class (1913) | Base | CL | Light Cruiser | WWI Light | 1913 | 1913 | 1913 | 5000 | 5750 | 25 | 20.0 | 8000 | 1500000 | 42 | 0 | Small, fast |
| 2610 | British | C-class | C-class | Base | CL | Light Cruiser | WWI Light | 1914 | 1914 | 1914 | 5000 | 5750 | 25 | 20.0 | 8000 | 1600000 | 42 | 0 | WWI workhorse |
| 2611 | British | D-class | D-class | Base | CL | Light Cruiser | WWI Light | 1918 | 1918 | 1918 | 5000 | 5750 | 25 | 20.0 | 8000 | 1800000 | 48 | 0 | Enhanced design |
| 2612 | British | E-class | E-class | Base | CL | Light Cruiser | Interwar | 1926 | 1926 | 1926 | 10000 | 11500 | 32 | 25.6 | 8000 | 2000000 | 48 | 0 | Modern interwar design |
| 2613 | British | Emerald-class | Emerald-class | Base | CL | Light Cruiser | Interwar | 1926 | 1926 | 1926 | 10000 | 11500 | 32 | 25.6 | 8000 | 2200000 | 54 | 0 | First modern 6" cruiser |
| 2614 | British | Leander-class (1931) | Leander-class (1931) | Base | CL | Light Cruiser | Treaty Light | 1931 | 1931 | 1931 | 10000 | 11500 | 32 | 25.6 | 8000 | 2500000 | 54 | 0 | Empire Reach: +15% range |
| 2615 | British | Amphion-class | Amphion-class | Base | CL | Light Cruiser | Treaty Light | 1934 | 1934 | 1934 | 10000 | 11500 | 32 | 25.6 | 8000 | 2700000 | 54 | 0 | Enhanced Leander |
| 2616 | British | Arethusa-class (1934) | Arethusa-class (1934) | Base | CL | Light Cruiser | Pre-WWII | 1935 | 1935 | 1935 | 10000 | 11500 | 32 | 25.6 | 8000 | 2900000 | 60 | 0 | Compact, effective |
| 2617 | British | Town-class (1936) | Town-class (1936) | Base | CL | Light Cruiser | Pre-WWII | 1936 | 1936 | 1936 | 10000 | 11500 | 32 | 25.6 | 8000 | 3200000 | 60 | 0 | 12×6" guns in 4 triple turrets |
| 2618 | British | Fiji-class | Fiji-class | Base | CL | Light Cruiser | WWII Light | 1940 | 1940 | 1940 | 10000 | 11500 | 32 | 25.6 | 8000 | 3500000 | 18 | 0 | WWII mass production |
| 2619 | British | Minotaur-class | Minotaur-class | Base | CL | Light Cruiser | Late WWII | 1943 | 1943 | 1943 | 10000 | 11500 | 32 | 25.6 | 8000 | 3800000 | 24 | 0 | Final WWII light cruiser |
| 2620 | British | Tiger-class | Tiger-class | Base | CG | CG | Post-War | 1959 | 1959 | 1959 | 10000 | 11500 | 25 | 20.0 | 10000 | 25000000 | 72 | 0 | Last gun cruiser design |
| 2621 | British | Dido-class | Dido-class | Base | CLAA | CLAA | AA Cruiser | 1940 | 1940 | 1940 | 10000 | 11500 | 25 | 20.0 | 10000 | 3300000 | 24 | 0 | ASDIC Pioneer: +20% ASW |
| 2622 | British | Bellona-class | Bellona-class | Base | CLAA | CLAA | AA Cruiser | 1943 | 1943 | 1943 | 10000 | 11500 | 25 | 20.0 | 10000 | 3500000 | 24 | 0 | Enhanced air defense |
| 2623 | British | Scylla-class | Scylla-class | Base | CLAA | CLAA | AA Cruiser | 1942 | 1942 | 1942 | 10000 | 11500 | 25 | 20.0 | 10000 | 3600000 | 24 | 0 | Ultimate AA design |
| 2624 | British | Hawkins-class | Hawkins-class | Base | CA | Heavy Cruiser | Heavy Cruiser | 1919 | 1919 | 1919 | 10000 | 11500 | 25 | 20.0 | 10000 | 2800000 | 60 | 0 | Early heavy cruiser |
| 2625 | British | County-class (Kent) | County-class (Kent) | Base | CA | Heavy Cruiser | Treaty Heavy | 1928 | 1928 | 1928 | 13000 | 14949 | 32 | 25.6 | 10000 | 3000000 | 60 | 0 | Empire Reach: +15% range |
| 2626 | British | County-class (London) | County-class (London) | Base | CA | Heavy Cruiser | Treaty Heavy | 1929 | 1929 | 1929 | 13000 | 14949 | 32 | 25.6 | 10000 | 3200000 | 60 | 0 | Enhanced County |
| 2627 | British | County-class (Norfolk) | County-class (Norfolk) | Base | CA | Heavy Cruiser | Treaty Heavy | 1930 | 1930 | 1930 | 13000 | 14949 | 32 | 25.6 | 10000 | 3400000 | 60 | 0 | Final County variant |
| 2628 | British | York-class | York-class | Base | CA | Heavy Cruiser | Treaty Heavy | 1930 | 1930 | 1930 | 13000 | 14949 | 32 | 25.6 | 10000 | 3600000 | 60 | 0 | Economical design |
| 2629 | British | Exeter-class | Exeter-class | Base | CA | Heavy Cruiser | Treaty Heavy | 1931 | 1931 | 1931 | 13000 | 14949 | 32 | 25.6 | 10000 | 3800000 | 60 | 0 | Enhanced York design |
| 2630 | British | Tiger-class | Tiger-class | Base | CG | CG | Post-War | 1959 | 1959 | 1959 | 10000 | 11500 | 25 | 20.0 | 10000 | 25000000 | 72 | 0 | Royal Navy Standards: +10% reliability |
| 2631 | British | Blake-class | Blake-class | Base | CG | CG | Post-War | 1961 | 1961 | 1961 | 10000 | 11500 | 25 | 20.0 | 10000 | 28000000 | 72 | 0 | Helicopter operations |
| 2632 | British | County-class (DDG) | County-class (DDG) | Base | DDG | DDG | Missile Era | 1962 | 1962 | 1962 | 10000 | 11500 | 25 | 20.0 | 10000 | 35000000 | 66 | 0 | Sea Slug missile system |
| 2633 | British | Bristol-class | Bristol-class | Base | DDG | DDG | Missile Era | 1973 | 1973 | 1973 | 10000 | 11500 | 25 | 20.0 | 10000 | 45000000 | 72 | 0 | Sea Dart missile system |
| 2634 | British | Sheffield-class (Type 42 Batch 1) | Sheffield-class (Type 42 Batch 1) | Base | DDG | DDG | Modern DDG | 1975 | 1975 | 1975 | 10000 | 11500 | 25 | 20.0 | 10000 | 50000000 | 60 | 0 | Modern missile destroyer |
| 2635 | British | Sheffield-class (Type 42 Batch 2) | Sheffield-class (Type 42 Batch 2) | Base | DDG | DDG | Modern DDG | 1978 | 1978 | 1978 | 10000 | 11500 | 25 | 20.0 | 10000 | 55000000 | 60 | 0 | Enhanced systems |
| 2636 | British | Sheffield-class (Type 42 Batch 3) | Sheffield-class (Type 42 Batch 3) | Base | DDG | DDG | Modern DDG | 1982 | 1982 | 1982 | 10000 | 11500 | 25 | 20.0 | 10000 | 60000000 | 60 | 0 | Stretched hull, better seakeeping |
| 2637 | British | Type 22 Broadsword-class | Type 22 Broadsword-class | Base | FFG | FFG | Modern FFG | 1979 | 1979 | 1979 | 10000 | 11500 | 25 | 20.0 | 10000 | 70000000 | 66 | 0 | ASDIC Pioneer: +20% ASW, Sea Wolf |
| 2638 | British | Type 23 Duke-class (Batch 1) | Type 23 Duke-class (Batch 1) | Base | FFG | FFG | Modern FFG | 1990 | 1990 | 1990 | 10000 | 11500 | 25 | 20.0 | 10000 | 150000000 | 72 | 0 | Silent Service: +15% stealth |
| 2639 | British | Type 23 Duke-class (Batch 2) | Type 23 Duke-class (Batch 2) | Base | FFG | FFG | Modern FFG | 1993 | 1993 | 1993 | 10000 | 11500 | 25 | 20.0 | 10000 | 160000000 | 72 | 0 | Enhanced systems |
| 2640 | British | Type 26 Frigate | Type 26 Frigate | Base | FFG | FFG | Future FFG | 2023 | 2023 | 2023 | 10000 | 11500 | 25 | 20.0 | 10000 | 500000000 | 84 | 0 | Advanced ASW systems |
| 2641 | British | Tiger-class (Modernized) | Tiger-class (Modernized) | Base | CG | CG | Modernized | 1972 | 1972 | 1972 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Helicopter operations |
| 2642 | British | County-class (DDG Modernized) | County-class (DDG Modernized) | Base | DDG | DDG | Modernized | 1975 | 1975 | 1975 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Sea Dart missile upgrade |
| 2643 | British | Sheffield-class (Modernized) | Sheffield-class (Modernized) | Base | DDG | DDG | Modernized | 1985 | 1985 | 1985 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Extended service life |
| 2644 | British | Design CA | Design CA | Base | CA | Heavy Cruiser | Design Phase | 1945 | 1945 | 1945 | 17000 | 19550 | 33 | 26.4 | 10000 | 5000000 | 66 | 0 | Advanced 8" design, -10% reliability |
| 2645 | British | Future Cruiser Concept | Future Cruiser Concept | Base | CG | CG | Future Concept | 2040 | 2040 | 2040 | 10000 | 11500 | 25 | 20.0 | 10000 | 2000000000 | 96 | 0 | Advanced systems, -10% reliability |
| 2700 | British | 27-knotter | 27-knotter | Base | DD | Destroyer | Early TBD | 1894 | 1894 | 1894 | 1000 | 1150 | 30 | 24.0 | 5000 | 100000 | 18 | 0 | Primitive: -40% reliability, FREE |
| 2701 | British | River-class | River-class | Base | DD | Destroyer | Scout Destroyer | 1903 | 1903 | 1903 | 1000 | 1150 | 30 | 24.0 | 5000 | 200000 | 24 | 0 | Atlantic Veteran: +10% endurance, FREE |
| 2702 | British | Tribal-class (F) | Tribal-class (F) | Base | DD | Destroyer | Pre-WWI | 1909 | 1909 | 1909 | 1000 | 1150 | 30 | 24.0 | 5000 | 300000 | 30 | 0 | Letter class naming system |
| 2703 | British | Acorn-class (H) | Acorn-class (H) | Base | DD | Destroyer | Pre-WWI | 1910 | 1910 | 1910 | 1000 | 1150 | 30 | 24.0 | 5000 | 350000 | 30 | 0 | Oil-fired variant |
| 2704 | British | Beagle-class (G) | Beagle-class (G) | Base | DD | Destroyer | Pre-WWI | 1909 | 1909 | 1909 | 1000 | 1150 | 30 | 24.0 | 5000 | 380000 | 36 | 0 | Oil and coal mix |
| 2705 | British | Acasta-class (K) | Acasta-class (K) | Base | DD | Destroyer | Pre-WWI | 1912 | 1912 | 1912 | 1000 | 1150 | 30 | 24.0 | 5000 | 420000 | 36 | 0 | All oil-fired |
| 2706 | British | Admiralty M-class | Admiralty M-class | Base | DD | Destroyer | WWI | 1914 | 1914 | 1914 | 1000 | 1150 | 30 | 24.0 | 5000 | 500000 | 42 | 0 | Mass production design |
| 2707 | British | R-class | R-class | Base | DD | Destroyer | WWI | 1916 | 1916 | 1916 | 1000 | 1150 | 30 | 24.0 | 5000 | 550000 | 42 | 0 | Enhanced seakeeping |
| 2708 | British | V-class | V-class | Base | DD | Destroyer | WWI | 1917 | 1917 | 1917 | 1000 | 1150 | 30 | 24.0 | 5000 | 600000 | 48 | 0 | Better armament |
| 2709 | British | W-class | W-class | Base | DD | Destroyer | WWI | 1918 | 1918 | 1918 | 1000 | 1150 | 30 | 24.0 | 5000 | 650000 | 48 | 0 | 4×4" guns |
| 2710 | British | Modified W-class | Modified W-class | Base | DD | Destroyer | WWI | 1918 | 1918 | 1918 | 1000 | 1150 | 30 | 24.0 | 5000 | 680000 | 48 | 0 | Modified design |
| 2711 | British | A-class | A-class | Base | DD | Destroyer | Interwar | 1930 | 1930 | 1930 | 2000 | 2300 | 35 | 28.0 | 5000 | 750000 | 54 | 0 | Modern design |
| 2712 | British | B-class | B-class | Base | DD | Destroyer | Interwar | 1930 | 1930 | 1930 | 2000 | 2300 | 35 | 28.0 | 5000 | 800000 | 54 | 0 | Enhanced systems |
| 2713 | British | Tribal-class (1936) | Tribal-class (1936) | Base | DD | Destroyer | Pre-WWII | 1938 | 1938 | 1938 | 2000 | 2300 | 35 | 28.0 | 5000 | 1200000 | 60 | 0 | ASDIC Mastery: +20% ASW |
| 2714 | British | J-class | J-class | Base | DD | Destroyer | Pre-WWII | 1939 | 1939 | 1939 | 2000 | 2300 | 35 | 28.0 | 5000 | 950000 | 60 | 0 | Balanced design |
| 2715 | British | K-class | K-class | Base | DD | Destroyer | Pre-WWII | 1939 | 1939 | 1939 | 2000 | 2300 | 35 | 28.0 | 5000 | 980000 | 60 | 0 | Enhanced ASW |
| 2716 | British | N-class | N-class | Base | DD | Destroyer | Pre-WWII | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 1000000 | 60 | 0 | Better armament |
| 2717 | British | O/P-class | O/P-class | Base | DD | Destroyer | Pre-WWII | 1941 | 1941 | 1941 | 2000 | 2300 | 35 | 28.0 | 5000 | 1050000 | 60 | 0 | Compact design |
| 2718 | British | Q/R-class | Q/R-class | Base | DD | Destroyer | WWII | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 1100000 | 24 | 0 | War production |
| 2719 | British | S/T-class | S/T-class | Base | DD | Destroyer | WWII | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 1150000 | 24 | 0 | Simplified design |
| 2720 | British | U/V-class | U/V-class | Base | DD | Destroyer | WWII | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 1200000 | 24 | 0 | Mass production |
| 2721 | British | W/Z-class | W/Z-class | Base | DD | Destroyer | WWII | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 1250000 | 24 | 0 | Final emergency design |
| 2722 | British | Battle-class | Battle-class | Base | DD | Destroyer | WWII | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 1500000 | 30 | 0 | Dual-purpose guns |
| 2723 | British | Daring-class | Daring-class | Base | DD | Destroyer | Post-War | 1952 | 1952 | 1952 | 5000 | 5750 | 35 | 28.0 | 5000 | 3500000 | 60 | 0 | Royal Navy Standards: +10% reliability |
| 2724 | British | County-class (DDG) | County-class (DDG) | Base | DDG | DDG | Missile Era | 1962 | 1962 | 1962 | 10000 | 11500 | 25 | 20.0 | 10000 | 35000000 | 66 | 0 | Sea Slug missile system |
| 2725 | British | Type 42 Batch 1 | Type 42 Batch 1 | Base | DDG | DDG | Modern DDG | 1975 | 1975 | 1975 | 10000 | 11500 | 25 | 20.0 | 10000 | 50000000 | 60 | 0 | Sea Dart missile system |
| 2726 | British | Type 42 Batch 2 | Type 42 Batch 2 | Base | DDG | DDG | Modern DDG | 1978 | 1978 | 1978 | 10000 | 11500 | 25 | 20.0 | 10000 | 55000000 | 60 | 0 | Enhanced systems |
| 2727 | British | Type 42 Batch 3 | Type 42 Batch 3 | Base | DDG | DDG | Modern DDG | 1982 | 1982 | 1982 | 10000 | 11500 | 25 | 20.0 | 10000 | 60000000 | 60 | 0 | Better seakeeping |
| 2728 | British | Type 42 Batch 3.2 | Type 42 Batch 3.2 | Base | DDG | DDG | Modern DDG | 1985 | 1985 | 1985 | 10000 | 11500 | 25 | 20.0 | 10000 | 65000000 | 60 | 0 | Final production variant |
| 2729 | British | Type 45 Batch 1 | Type 45 Batch 1 | Base | DDG | DDG | Modern DDG | 2009 | 2009 | 2009 | 10000 | 11500 | 25 | 20.0 | 10000 | 1200000000 | 84 | 0 | PAAMS air defense system |
| 2730 | British | Type 45 Batch 2 | Type 45 Batch 2 | Base | DDG | DDG | Modern DDG | 2011 | 2011 | 2011 | 10000 | 11500 | 25 | 20.0 | 10000 | 1250000000 | 84 | 0 | Enhanced systems |
| 2731 | British | Type 45 Batch 3 | Type 45 Batch 3 | Base | DDG | DDG | Modern DDG | 2013 | 2013 | 2013 | 10000 | 11500 | 25 | 20.0 | 10000 | 1300000000 | 84 | 0 | Final production variant |
| 2732 | British | Type 45A | Type 45A | Base | DDG | DDG | Modern DDG | 2020 | 2020 | 2020 | 10000 | 11500 | 25 | 20.0 | 10000 | 1400000000 | 90 | 0 | Advanced systems |
| 2733 | British | Type 45 (Modernized) | Type 45 (Modernized) | Base | DDG | DDG | Modernized | 2025 | 2025 | 2025 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Extended service life |
| 2734 | British | Type 83 | Type 83 | Base | DDG | DDG | Future DDG | 2035 | 2035 | 2035 | 10000 | 11500 | 25 | 20.0 | 10000 | 2500000000 | 96 | 0 | Advanced future systems |
| 2736 | British | Hunt-class | Hunt-class | Base | DD | Destroyer | WWII Escort | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 700000 | 30 | 0 | ASDIC Mastery: +20% ASW |
| 2737 | British | Black Swan-class | Black Swan-class | Base | DD | Destroyer | ASW Sloop | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 800000 | 36 | 0 | ASW specialist design |
| 2738 | British | River-class (Frigate) | River-class (Frigate) | Base | FFG | FFG | ASW Frigate | 1942 | 1942 | 1942 | 10000 | 11500 | 25 | 20.0 | 10000 | 950000 | 42 | 0 | Atlantic Veteran: +10% endurance |
| 2739 | British | Battle-class (Modernized) | Battle-class (Modernized) | Base | DD | Destroyer | Modernized | 1958 | 1958 | 1958 | 5000 | 5750 | 35 | 28.0 | 5000 | 0 | 0 | 0 | Electronics and radar upgrades |
| 2740 | British | Daring-class (Modernized) | Daring-class (Modernized) | Base | DD | Destroyer | Modernized | 1965 | 1965 | 1965 | 5000 | 5750 | 35 | 28.0 | 5000 | 0 | 0 | 0 | Extended service life |
| 2741 | British | County-class (DDG Modernized) | County-class (DDG Modernized) | Base | DDG | DDG | Modernized | 1975 | 1975 | 1975 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 | Sea Dart missile upgrade |
| 2800 | British | Holland-class | Holland-class | Base | SS | Submarine | Early Submarine | 1901 | 1901 | 1901 | 500 | 575 | 15 | 12.0 | 8000 | 50000 | 18 | 0 | Primitive: -40% reliability, FREE |
| 2801 | British | A-class | A-class | Base | SS | Submarine | Coastal Submarine | 1903 | 1903 | 1903 | 500 | 575 | 15 | 12.0 | 8000 | 100000 | 24 | 0 | Silent Service: +15% stealth, FREE |
| 2802 | British | B-class | B-class | Base | SS | Submarine | Coastal | 1905 | 1905 | 1905 | 500 | 575 | 15 | 12.0 | 8000 | 120000 | 30 | 0 | British waters operations |
| 2803 | British | C-class | C-class | Base | SS | Submarine | Coastal | 1906 | 1906 | 1906 | 500 | 575 | 15 | 12.0 | 8000 | 140000 | 30 | 0 | Enhanced range |
| 2804 | British | D-class (Coastal) | D-class (Coastal) | Base | SS | Submarine | Coastal | 1908 | 1908 | 1908 | 500 | 575 | 15 | 12.0 | 8000 | 160000 | 36 | 0 | Coastal operations |
| 2805 | British | E-class (Coastal) | E-class (Coastal) | Base | SS | Submarine | Coastal | 1912 | 1912 | 1912 | 500 | 575 | 15 | 12.0 | 8000 | 180000 | 36 | 0 | Enhanced coastal |
| 2806 | British | H-class (Coastal) | H-class (Coastal) | Base | SS | Submarine | Coastal | 1915 | 1915 | 1915 | 500 | 575 | 15 | 12.0 | 8000 | 200000 | 36 | 0 | Coastal patrol |
| 2807 | British | D-class (Fleet) | D-class (Fleet) | Base | SS | Submarine | WWI | 1910 | 1910 | 1910 | 500 | 575 | 15 | 12.0 | 8000 | 250000 | 42 | 0 | Ocean-going capability |
| 2808 | British | E-class (Fleet) | E-class (Fleet) | Base | SS | Submarine | WWI | 1913 | 1913 | 1913 | 500 | 575 | 15 | 12.0 | 8000 | 300000 | 48 | 0 | WWI workhorse |
| 2809 | British | F-class | F-class | Base | SS | Submarine | WWI | 1915 | 1915 | 1915 | 500 | 575 | 15 | 12.0 | 8000 | 350000 | 48 | 0 | Enhanced design |
| 2810 | British | G-class | G-class | Base | SS | Submarine | WWI | 1916 | 1916 | 1916 | 500 | 575 | 15 | 12.0 | 8000 | 400000 | 48 | 0 | Better armament |
| 2811 | British | H-class | H-class | Base | SS | Submarine | WWI | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 450000 | 54 | 0 | Fleet operations |
| 2812 | British | J-class | J-class | Base | SS | Submarine | WWI | 1916 | 1916 | 1916 | 500 | 575 | 15 | 12.0 | 8000 | 500000 | 54 | 0 | First diesel-only |
| 2813 | British | K-class | K-class | Base | SS | Submarine | Experimental | 1917 | 1917 | 1917 | 500 | 575 | 15 | 12.0 | 8000 | 700000 | 60 | 0 | Experimental, troubled |
| 2814 | British | L-class | L-class | Base | SS | Submarine | Interwar | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 550000 | 54 | 0 | Better design |
| 2815 | British | M-class | M-class | Base | SS | Submarine | Experimental | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 800000 | 60 | 0 | 12" gun submarine |
| 2816 | British | O-class | O-class | Base | SS | Submarine | Interwar | 1926 | 1926 | 1926 | 1500 | 1724 | 15 | 12.0 | 8000 | 600000 | 60 | 0 | Long-range patrol |
| 2817 | British | P-class | P-class | Base | SS | Submarine | Interwar | 1930 | 1930 | 1930 | 1500 | 1724 | 15 | 12.0 | 8000 | 650000 | 60 | 0 | Standard patrol |
| 2818 | British | R-class | R-class | Base | SS | Submarine | Interwar | 1932 | 1932 | 1932 | 1500 | 1724 | 15 | 12.0 | 8000 | 700000 | 60 | 0 | Enhanced systems |
| 2819 | British | S-class | S-class | Base | SS | Submarine | Pre-WWII | 1932 | 1932 | 1932 | 1500 | 1724 | 15 | 12.0 | 8000 | 750000 | 18 | 0 | RN Reliability: +10% uptime |
| 2820 | British | T-class | T-class | Base | SS | Submarine | WWII | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 900000 | 24 | 0 | Silent Service: +15% stealth |
| 2821 | British | U-class | U-class | Base | SS | Submarine | WWII | 1940 | 1940 | 1940 | 1500 | 1724 | 15 | 12.0 | 8000 | 850000 | 24 | 0 | Coastal and fleet ops |
| 2822 | British | V-class | V-class | Base | SS | Submarine | WWII | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 900000 | 24 | 0 | Enhanced U-class |
| 2823 | British | A-class (1945) | A-class (1945) | Base | SS | Submarine | Post-War | 1947 | 1947 | 1947 | 3000 | 3449 | 20 | 16.0 | 8000 | 1200000 | 36 | 0 | Modern diesel design |
| 2824 | British | Porpoise-class | Porpoise-class | Base | SS | Submarine | Post-War | 1958 | 1958 | 1958 | 3000 | 3449 | 20 | 16.0 | 8000 | 1500000 | 48 | 0 | Last diesel patrol |
| 2825 | British | T-class (Streamlined) | T-class (Streamlined) | Base | SS | Submarine | Modernized | 1950 | 1950 | 1950 | 3000 | 3449 | 20 | 16.0 | 8000 | 0 | 0 | 0 | GUPPY-equivalent |
| 2826 | British | A-class (Modernized) | A-class (Modernized) | Base | SS | Submarine | Modernized | 1955 | 1955 | 1955 | 3000 | 3449 | 20 | 16.0 | 8000 | 0 | 0 | 0 | Extended service life |
| 2827 | British | Dreadnought SSN | Dreadnought SSN | Base | SSN | SSN | Nuclear | 1963 | 1963 | 1963 | 10000 | 11500 | 25 | 20.0 | 10000 | 35000000 | 72 | 0 | First nuclear, unlimited range, UNIQUE |
| 2828 | British | Valiant-class | Valiant-class | Base | SSN | SSN | Nuclear | 1966 | 1966 | 1966 | 10000 | 11500 | 25 | 20.0 | 10000 | 40000000 | 72 | 0 | RN Reliability: +10% uptime |
| 2829 | British | Churchill-class | Churchill-class | Base | SSN | SSN | Nuclear | 1970 | 1970 | 1970 | 10000 | 11500 | 25 | 20.0 | 10000 | 45000000 | 78 | 0 | Enhanced systems |
| 2830 | British | Swiftsure-class | Swiftsure-class | Base | SSN | SSN | Nuclear | 1973 | 1973 | 1973 | 10000 | 11500 | 25 | 20.0 | 10000 | 55000000 | 84 | 0 | Silent Service: +15% stealth |
| 2831 | British | Trafalgar-class | Trafalgar-class | Base | SSN | SSN | Nuclear | 1983 | 1983 | 1983 | 10000 | 11500 | 25 | 20.0 | 10000 | 75000000 | 90 | 0 | Tomahawk capability |
| 2832 | British | Astute-class (Batch 1) | Astute-class (Batch 1) | Base | SSN | SSN | Modern | 2010 | 2010 | 2010 | 10000 | 11500 | 25 | 20.0 | 10000 | 1500000000 | 108 | 0 | PWR2 reactor, advanced systems |
| 2833 | British | Astute-class (Batch 2) | Astute-class (Batch 2) | Base | SSN | SSN | Modern | 2020 | 2020 | 2020 | 10000 | 11500 | 25 | 20.0 | 10000 | 1600000000 | 108 | 0 | Latest technology |
| 2834 | British | Resolution-class | Resolution-class | Base | SSBN | SSBN | Ballistic | 1967 | 1967 | 1967 | 10000 | 11500 | 25 | 20.0 | 10000 | 120000000 | 96 | 0 | 16 Polaris missiles |
| 2835 | British | Vanguard-class | Vanguard-class | Base | SSBN | SSBN | Ballistic | 1993 | 1993 | 1993 | 10000 | 11500 | 25 | 20.0 | 10000 | 1500000000 | 120 | 0 | 16 Trident II D5 missiles |
| 2836 | British | Dreadnought SSBN | Dreadnought SSBN | Base | SSBN | SSBN | Future SSBN | 2030 | 2030 | 2030 | 10000 | 11500 | 25 | 20.0 | 10000 | 4000000000 | 144 | 0 | 12 Trident II D5 missiles |
| 2837 | British | X-craft | X-craft | Base | SSE | SSE | Midget Sub | 1943 | 1943 | 1943 | 10000 | 11500 | 25 | 20.0 | 10000 | 100000 | 12 | 0 | Special operations, UNIQUE |
| 2838 | British | Explorer HTP | Explorer HTP | Base | SSE | SSE | Experimental | 1958 | 1958 | 1958 | 10000 | 11500 | 25 | 20.0 | 10000 | 500000 | 42 | 0 | High Test Peroxide, UNIQUE |
| 3000 | German | SMS Brandenburg | SMS Brandenburg | Base | BB | Battleship | Early Pre-Dreadnought | 1893 | 1893 | 1893 | 12000 | 13799 | 18 | 14.4 | 15000 | 500000 | 36 | 0 | First German BB, FREE |
| 3001 | German | SMS Kaiser Friedrich III | SMS Kaiser Friedrich III | Base | BB | Battleship | Pre-Dreadnought | 1898 | 1898 | 1898 | 12000 | 13799 | 18 | 14.4 | 15000 | 800000 | 42 | 0 | Rapid-fire doctrine, FREE |
| 3002 | German | SMS Wittelsbach | SMS Wittelsbach | Base | BB | Battleship | Pre-Dreadnought | 1902 | 1902 | 1902 | 12000 | 13799 | 18 | 14.4 | 15000 | 1000000 | 36 | 0 | +10% protection |
| 3003 | German | SMS Wettin | SMS Wettin | Base | BB | Battleship | Pre-Dreadnought | 1902 | 1902 | 1902 | 12000 | 13799 | 18 | 14.4 | 15000 | 1000000 | 36 | 0 | +5% efficiency |
| 3004 | German | SMS Braunschweig | SMS Braunschweig | Base | BB | Battleship | Pre-Dreadnought | 1904 | 1904 | 1904 | 12000 | 13799 | 18 | 14.4 | 15000 | 1200000 | 42 | 0 | +15% firepower |
| 3005 | German | SMS Elsass | SMS Elsass | Base | BB | Battleship | Pre-Dreadnought | 1904 | 1904 | 1904 | 12000 | 13799 | 18 | 14.4 | 15000 | 1200000 | 42 | 0 | +10% armor |
| 3006 | German | SMS Deutschland (1906) | SMS Deutschland (1906) | Base | BB | Battleship | Pre-Dreadnought | 1906 | 1906 | 1906 | 20000 | 23000 | 21 | 16.8 | 15000 | 1500000 | 48 | 0 | Pinnacle design |
| 3007 | German | SMS Hannover | SMS Hannover | Base | BB | Battleship | Pre-Dreadnought | 1907 | 1907 | 1907 | 20000 | 23000 | 21 | 16.8 | 15000 | 1500000 | 48 | 0 | Mass production |
| 3008 | German | SMS Pommern | SMS Pommern | Base | BB | Battleship | Pre-Dreadnought | 1907 | 1907 | 1907 | 20000 | 23000 | 21 | 16.8 | 15000 | 1500000 | 48 | 0 | Combat experience |
| 3009 | German | SMS Schleswig-Holstein | SMS Schleswig-Holstein | Base | BB | Battleship | Pre-Dreadnought | 1908 | 1908 | 1908 | 20000 | 23000 | 21 | 16.8 | 15000 | 1600000 | 48 | 0 | +15% prestige |
| 3010 | German | SMS Schlesien | SMS Schlesien | Base | BB | Battleship | Pre-Dreadnought | 1908 | 1908 | 1908 | 20000 | 23000 | 21 | 16.8 | 15000 | 1600000 | 48 | 0 | +20% reliability |
| 3011 | German | SMS Nassau | SMS Nassau | Base | BB | Battleship | First Dreadnought | 1909 | 1909 | 1909 | 20000 | 23000 | 21 | 16.8 | 15000 | 3000000 | 36 | 0 | Hexagonal layout, UNIQUE |
| 3012 | German | SMS Westfalen | SMS Westfalen | Base | BB | Battleship | First Dreadnought | 1909 | 1909 | 1909 | 20000 | 23000 | 21 | 16.8 | 15000 | 3000000 | 36 | 0 | +10% broadside |
| 3013 | German | SMS Helgoland | SMS Helgoland | Base | BB | Battleship | Improved Dreadnought | 1911 | 1911 | 1911 | 20000 | 23000 | 21 | 16.8 | 15000 | 4000000 | 42 | 0 | +20% firepower |
| 3014 | German | SMS Ostfriesland | SMS Ostfriesland | Base | BB | Battleship | Improved Dreadnought | 1911 | 1911 | 1911 | 20000 | 23000 | 21 | 16.8 | 15000 | 4000000 | 42 | 0 | Historical significance |
| 3015 | German | SMS Kaiser | SMS Kaiser | Base | BB | Battleship | Super-Dreadnought | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 5000000 | 48 | 0 | +15% speed, superfiring |
| 3016 | German | SMS Friedrich der Große | SMS Friedrich der Große | Base | BB | Battleship | Super-Dreadnought | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 5000000 | 48 | 0 | +20% command |
| 3017 | German | SMS König | SMS König | Base | BB | Battleship | Super-Dreadnought | 1913 | 1913 | 1913 | 20000 | 23000 | 21 | 16.8 | 15000 | 6000000 | 48 | 0 | +15% firepower |
| 3018 | German | SMS Großer Kurfürst | SMS Großer Kurfürst | Base | BB | Battleship | Super-Dreadnought | 1914 | 1914 | 1914 | 20000 | 23000 | 21 | 16.8 | 15000 | 6000000 | 48 | 0 | Jutland combat |
| 3019 | German | SMS Bayern | SMS Bayern | Base | BB | Battleship | Ultimate WWI | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 8000000 | 54 | 0 | +30% firepower, UNIQUE |
| 3020 | German | Deutschland (Panzerschiff) | Deutschland (Panzerschiff) | Base | PS | PS | Pocket Battleship | 1931 | 1931 | 1931 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 60 | 0 | +25% range, Treaty loophole |
| 3021 | German | Admiral Scheer | Admiral Scheer | Base | PS | PS | Pocket Battleship | 1934 | 1934 | 1934 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 60 | 0 | +30% commerce raiding |
| 3022 | German | Admiral Graf Spee | Admiral Graf Spee | Base | PS | PS | Pocket Battleship | 1936 | 1936 | 1936 | 10000 | 11500 | 25 | 20.0 | 10000 | 12000000 | 60 | 0 | Combat experience |
| 3023 | German | Scharnhorst | Scharnhorst | Base | BB | Battleship | Fast Battleship | 1939 | 1939 | 1939 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 66 | 0 | 32 kts, +20% speed |
| 3024 | German | Gneisenau | Gneisenau | Base | BB | Battleship | Fast Battleship | 1939 | 1939 | 1939 | 45000 | 51749 | 30 | 24.0 | 15000 | 30000000 | 66 | 0 | +25% raiding |
| 3025 | German | Bismarck | Bismarck | Base | BB | Battleship | Ultimate BB | 1940 | 1940 | 1940 | 45000 | 51749 | 30 | 24.0 | 15000 | 50000000 | 72 | 0 | Sank HMS Hood, +40% prestige, UNIQUE |
| 3026 | German | Tirpitz | Tirpitz | Base | BB | Battleship | Ultimate BB | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 50000000 | 72 | 0 | +30% deterrence |
| 3027 | German | SMS Bayern (Modernized) | SMS Bayern (Modernized) | Base | BB | Battleship | Modernization | 1920 | 1920 | 1920 | 32000 | 36800 | 23 | 18.4 | 15000 | 4000000 | 18 | 0 | Improved systems |
| 3028 | German | Deutschland (Lützow) | Deutschland (Lützow) | Base | PS | PS | Modernization | 1940 | 1940 | 1940 | 10000 | 11500 | 25 | 20.0 | 10000 | 6000000 | 24 | 0 | 1940 refit |
| 3029 | German | Scharnhorst (38cm Refit) | Scharnhorst (38cm Refit) | Base | BB | Battleship | Modernization | 1942 | 1942 | 1942 | 45000 | 51749 | 30 | 24.0 | 15000 | 15000000 | 36 | 0 | Planned improvement |
| 3030 | German | H-39 | H-39 | Base | BB | Battleship | H-Class Plan Z | 1939 | 1939 | 1939 | 45000 | 51749 | 30 | 24.0 | 15000 | 60000000 | 84 | 0 | 40.6cm guns, laid down |
| 3031 | German | H-41 | H-41 | Base | BB | Battleship | H-Class Improved | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 70000000 | 90 | 0 | 42cm guns, improved armor |
| 3032 | German | H-42 | H-42 | Base | BB | Battleship | H-Class Study | 1942 | 1942 | 1942 | 45000 | 51749 | 30 | 24.0 | 15000 | 90000000 | 96 | 0 | 48cm guns, 90,000 tons |
| 3033 | German | H-43 | H-43 | Base | BB | Battleship | H-Class Study | 1943 | 1943 | 1943 | 45000 | 51749 | 30 | 24.0 | 15000 | 110000000 | 102 | 0 | 50.8cm guns, 111,000 tons |
| 3034 | German | H-44 | H-44 | Base | BB | Battleship | H-Class Ultimate | 1944 | 1944 | 1944 | 45000 | 51749 | 30 | 24.0 | 15000 | 130000000 | 108 | 0 | 131,000 tons, largest design, UNIQUE |
| 3035 | German | H-45 Monster | H-45 Monster | Base | BB | Battleship | H-Class Beyond | 1944 | 1944 | 1944 | 45000 | 51749 | 30 | 24.0 | 15000 | 150000000 | 120 | 1 | 150,000+ tons, theoretical |
| 3036 | German | SMS Derfflinger | SMS Derfflinger | Base | BC | BC | WWI Battlecruiser | 1914 | 1914 | 1914 | 10000 | 11500 | 25 | 20.0 | 10000 | 5500000 | 48 | 0 | +25% speed, Jutland survivor |
| 3037 | German | SMS Hindenburg | SMS Hindenburg | Base | BC | BC | WWI Battlecruiser | 1917 | 1917 | 1917 | 10000 | 11500 | 25 | 20.0 | 10000 | 7000000 | 54 | 0 | Final German BC |
| 3038 | German | O-Class | O-Class | Base | BC | BC | Cancelled BC | 1939 | 1939 | 1939 | 10000 | 11500 | 25 | 20.0 | 10000 | 50000000 | 72 | 0 | Plan Z BC, fast raider |
| 3039 | German | P-Class | P-Class | Base | BC | BC | Cancelled BC | 1940 | 1940 | 1940 | 10000 | 11500 | 25 | 20.0 | 10000 | 50000000 | 72 | 0 | Diesel BC, improved |
| 3600 | German | SMS Bussard | SMS Bussard | Base | CL | Light Cruiser | Unprotected Cruiser | 1890 | 1890 | 1890 | 5000 | 5750 | 25 | 20.0 | 8000 | 300000 | 24 | 0 | Early cruiser operations, FREE |
| 3601 | German | SMS Gazelle | SMS Gazelle | Base | CL | Light Cruiser | Protected Cruiser | 1901 | 1901 | 1901 | 5000 | 5750 | 25 | 20.0 | 8000 | 500000 | 30 | 0 | First modern CL, UNIQUE, FREE |
| 3602 | German | SMS Victoria Louise | SMS Victoria Louise | Base | CL | Light Cruiser | Protected Cruiser | 1899 | 1899 | 1899 | 5000 | 5750 | 25 | 20.0 | 8000 | 800000 | 36 | 0 | Armored deck protection |
| 3603 | German | SMS Kaiserin Augusta | SMS Kaiserin Augusta | Base | CL | Light Cruiser | Protected Cruiser | 1892 | 1892 | 1892 | 5000 | 5750 | 25 | 20.0 | 8000 | 900000 | 36 | 0 | +15% displacement |
| 3604 | German | SMS Fürst Bismarck | SMS Fürst Bismarck | Base | CA | Heavy Cruiser | Armored Cruiser | 1900 | 1900 | 1900 | 10000 | 11500 | 25 | 20.0 | 10000 | 1200000 | 42 | 0 | +20% armor |
| 3605 | German | SMS Prinz Heinrich | SMS Prinz Heinrich | Base | CA | Heavy Cruiser | Armored Cruiser | 1902 | 1902 | 1902 | 10000 | 11500 | 25 | 20.0 | 10000 | 1300000 | 42 | 0 | +10% firepower |
| 3606 | German | SMS Prinz Adalbert | SMS Prinz Adalbert | Base | CA | Heavy Cruiser | Armored Cruiser | 1904 | 1904 | 1904 | 10000 | 11500 | 25 | 20.0 | 10000 | 1500000 | 48 | 0 | +15% protection |
| 3607 | German | SMS Roon | SMS Roon | Base | CA | Heavy Cruiser | Armored Cruiser | 1905 | 1905 | 1905 | 10000 | 11500 | 25 | 20.0 | 10000 | 1600000 | 48 | 0 | +10% efficiency |
| 3608 | German | SMS Scharnhorst (CA) | SMS Scharnhorst (CA) | Base | CA | Heavy Cruiser | Armored Cruiser | 1907 | 1907 | 1907 | 10000 | 11500 | 25 | 20.0 | 10000 | 2000000 | 48 | 0 | +25% prestige |
| 3609 | German | SMS Blücher (CA) | SMS Blücher (CA) | Base | CA | Heavy Cruiser | Armored Cruiser | 1909 | 1909 | 1909 | 10000 | 11500 | 25 | 20.0 | 10000 | 2500000 | 54 | 0 | Bridge to heavy cruisers |
| 3610 | German | SMS Bremen | SMS Bremen | Base | CL | Light Cruiser | Light Cruiser | 1904 | 1904 | 1904 | 5000 | 5750 | 25 | 20.0 | 8000 | 700000 | 30 | 0 | +15% speed |
| 3611 | German | SMS Dresden | SMS Dresden | Base | CL | Light Cruiser | Light Cruiser | 1908 | 1908 | 1908 | 5000 | 5750 | 25 | 20.0 | 8000 | 900000 | 36 | 0 | +20% raiding |
| 3612 | German | SMS Königsberg (1907) | SMS Königsberg (1907) | Base | CL | Light Cruiser | Light Cruiser | 1907 | 1907 | 1907 | 5000 | 5750 | 25 | 20.0 | 8000 | 950000 | 36 | 0 | +10% capability |
| 3613 | German | SMS Kolberg | SMS Kolberg | Base | CL | Light Cruiser | Light Cruiser | 1910 | 1910 | 1910 | 5000 | 5750 | 25 | 20.0 | 8000 | 1100000 | 42 | 0 | Improved accuracy |
| 3614 | German | SMS Magdeburg | SMS Magdeburg | Base | CL | Light Cruiser | Light Cruiser | 1912 | 1912 | 1912 | 5000 | 5750 | 25 | 20.0 | 8000 | 1200000 | 42 | 0 | +20% protection, UNIQUE |
| 3615 | German | SMS Karlsruhe | SMS Karlsruhe | Base | CL | Light Cruiser | Light Cruiser | 1913 | 1913 | 1913 | 5000 | 5750 | 25 | 20.0 | 8000 | 1400000 | 48 | 0 | 27.5 kts |
| 3616 | German | SMS Pillau | SMS Pillau | Base | CL | Light Cruiser | Light Cruiser | 1914 | 1914 | 1914 | 5000 | 5750 | 25 | 20.0 | 8000 | 2000000 | 48 | 0 | +30% firepower, revolution |
| 3617 | German | SMS Graudenz | SMS Graudenz | Base | CL | Light Cruiser | Light Cruiser | 1914 | 1914 | 1914 | 5000 | 5750 | 25 | 20.0 | 8000 | 2100000 | 48 | 0 | 12×15cm guns |
| 3618 | German | SMS Wiesbaden | SMS Wiesbaden | Base | CL | Light Cruiser | Light Cruiser | 1915 | 1915 | 1915 | 5000 | 5750 | 25 | 20.0 | 8000 | 2200000 | 48 | 0 | Speed + firepower |
| 3619 | German | SMS Königsberg II | SMS Königsberg II | Base | CL | Light Cruiser | Light Cruiser | 1916 | 1916 | 1916 | 5000 | 5750 | 25 | 20.0 | 8000 | 2500000 | 54 | 0 | Best WWI CL |
| 3620 | German | SMS Emden (1925) | SMS Emden (1925) | Base | CL | Light Cruiser | Light Cruiser | 1925 | 1925 | 1925 | 10000 | 11500 | 32 | 25.6 | 8000 | 4000000 | 54 | 0 | +20% prestige |
| 3621 | German | Königsberg (1929) | Königsberg (1929) | Base | CL | Light Cruiser | Light Cruiser | 1929 | 1929 | 1929 | 10000 | 11500 | 32 | 25.6 | 8000 | 6000000 | 60 | 0 | 32 kts, 9×15cm |
| 3622 | German | Leipzig | Leipzig | Base | CL | Light Cruiser | Light Cruiser | 1931 | 1931 | 1931 | 10000 | 11500 | 32 | 25.6 | 8000 | 6500000 | 60 | 0 | +10% capability |
| 3623 | German | Nürnberg | Nürnberg | Base | CL | Light Cruiser | Light Cruiser | 1935 | 1935 | 1935 | 10000 | 11500 | 32 | 25.6 | 8000 | 7000000 | 60 | 0 | Final light cruiser |
| 3624 | German | Admiral Hipper | Admiral Hipper | Base | CA | Heavy Cruiser | Heavy Cruiser | 1939 | 1939 | 1939 | 13000 | 14949 | 32 | 25.6 | 10000 | 20000000 | 66 | 0 | 8×20.3cm guns |
| 3625 | German | Blücher (1939) | Blücher (1939) | Base | CA | Heavy Cruiser | Heavy Cruiser | 1939 | 1939 | 1939 | 13000 | 14949 | 32 | 25.6 | 10000 | 20000000 | 66 | 0 | Combat experience |
| 3626 | German | Prinz Eugen | Prinz Eugen | Base | CA | Heavy Cruiser | Heavy Cruiser | 1940 | 1940 | 1940 | 13000 | 14949 | 32 | 25.6 | 10000 | 22000000 | 66 | 0 | +30% prestige, survived war |
| 3627 | German | Seydlitz | Seydlitz | Base | CA | Heavy Cruiser | Heavy Cruiser | 1939 | 1939 | 1939 | 13000 | 14949 | 32 | 25.6 | 10000 | 20000000 | 66 | 0 | Carrier conversion |
| 3628 | German | Lützow (CA) | Lützow (CA) | Base | CA | Heavy Cruiser | Heavy Cruiser | 1939 | 1939 | 1939 | 13000 | 14949 | 32 | 25.6 | 10000 | 20000000 | 66 | 0 | Diplomatic significance |
| 3629 | German | SMS Königsberg II (Mod) | SMS Königsberg II (Mod) | Base | CL | Light Cruiser | Modernization | 1920 | 1920 | 1920 | 10000 | 11500 | 32 | 25.6 | 8000 | 1000000 | 18 | 0 | Improved systems |
| 3630 | German | Emden (1940 Refit) | Emden (1940 Refit) | Base | CL | Light Cruiser | Modernization | 1940 | 1940 | 1940 | 10000 | 11500 | 32 | 25.6 | 8000 | 2000000 | 24 | 0 | Enhanced AA |
| 3631 | German | Prinz Eugen (1945 Refit) | Prinz Eugen (1945 Refit) | Base | CA | Heavy Cruiser | Modernization | 1945 | 1945 | 1945 | 17000 | 19550 | 33 | 26.4 | 10000 | 5000000 | 30 | 0 | Maximum AA |
| 3632 | German | P-Class Cruiser | P-Class Cruiser | Base | CA | Heavy Cruiser | Cancelled CA | 1940 | 1940 | 1940 | 13000 | 14949 | 32 | 25.6 | 10000 | 25000000 | 72 | 0 | Plan Z CA, -10% reliability |
| 3633 | German | M-Class Cruiser | M-Class Cruiser | Base | CL | Light Cruiser | Cancelled CL | 1940 | 1940 | 1940 | 10000 | 11500 | 32 | 25.6 | 8000 | 15000000 | 60 | 0 | Improved CL, -10% reliability |
| 3634 | German | Improved Hipper | Improved Hipper | Base | CA | Heavy Cruiser | Paper Ship | 1942 | 1942 | 1942 | 13000 | 14949 | 32 | 25.6 | 10000 | 30000000 | 78 | 0 | Enhanced design, -15% reliability |
| 3635 | German | Super Hipper | Super Hipper | Base | CA | Heavy Cruiser | Paper Ship | 1943 | 1943 | 1943 | 13000 | 14949 | 32 | 25.6 | 10000 | 35000000 | 84 | 0 | 9×20.3cm guns, -15% reliability |
| 3636 | German | Spähkreuzer | Spähkreuzer | Base | CL | Light Cruiser | Scout Cruiser | 1941 | 1941 | 1941 | 10000 | 11500 | 32 | 25.6 | 8000 | 12000000 | 60 | 0 | Reconnaissance operations |
| 3637 | German | AA Cruiser Concept | AA Cruiser Concept | Base | CL | Light Cruiser | AA Cruiser | 1942 | 1942 | 1942 | 10000 | 11500 | 32 | 25.6 | 8000 | 18000000 | 66 | 0 | Dedicated AA, -10% reliability |
| 3638 | German | Torpedo Cruiser | Torpedo Cruiser | Base | CL | Light Cruiser | Torpedo Cruiser | 1940 | 1940 | 1940 | 10000 | 11500 | 32 | 25.6 | 8000 | 10000000 | 54 | 0 | +40% torpedo capability |
| 3639 | German | Future CL Concept | Future CL Concept | Base | CL | Light Cruiser | Future Design | 1950 | 1950 | 1950 | 15000 | 17250 | 33 | 26.4 | 8000 | 40000000 | 90 | 0 | Post-war concept, -10% reliability |
| 3700 | German | SMS S90 | SMS S90 | Base | DD | Destroyer | Torpedo Boat | 1898 | 1898 | 1898 | 1000 | 1150 | 30 | 24.0 | 5000 | 400000 | 50 | 0 | First modern German torpedo boat, FREE |
| 3701 | German | SMS G108 | SMS G108 | Base | DD | Destroyer | Torpedo Boat | 1900 | 1900 | 1900 | 1000 | 1150 | 30 | 24.0 | 5000 | 450000 | 50 | 0 | 29 kts, early turbine, FREE |
| 3702 | German | SMS S114 | SMS S114 | Base | DD | Destroyer | Torpedo Boat | 1902 | 1902 | 1902 | 1000 | 1150 | 30 | 24.0 | 5000 | 500000 | 52 | 0 | Early torpedo operations |
| 3703 | German | SMS S138 | SMS S138 | Base | DD | Destroyer | Large Torpedo Boat | 1906 | 1906 | 1906 | 1000 | 1150 | 30 | 24.0 | 5000 | 600000 | 58 | 0 | 1906 program, improved |
| 3704 | German | SMS V150 | SMS V150 | Base | DD | Destroyer | Large Torpedo Boat | 1907 | 1907 | 1907 | 1000 | 1150 | 30 | 24.0 | 5000 | 650000 | 58 | 0 | Turbine technology |
| 3705 | German | SMS V1 | SMS V1 | Base | DD | Destroyer | Large Torpedo Boat | 1911 | 1911 | 1911 | 1000 | 1150 | 30 | 24.0 | 5000 | 800000 | 74 | 0 | 1911 Program destroyer |
| 3706 | German | SMS G7 | SMS G7 | Base | DD | Destroyer | Large Torpedo Boat | 1911 | 1911 | 1911 | 1000 | 1150 | 30 | 24.0 | 5000 | 850000 | 74 | 0 | Germaniawerft built |
| 3707 | German | SMS S13 | SMS S13 | Base | DD | Destroyer | Large Torpedo Boat | 1911 | 1911 | 1911 | 1000 | 1150 | 30 | 24.0 | 5000 | 750000 | 70 | 0 | More maneuverable design |
| 3708 | German | SMS S31 | SMS S31 | Base | DD | Destroyer | Large Torpedo Boat | 1912 | 1912 | 1912 | 1000 | 1150 | 30 | 24.0 | 5000 | 900000 | 72 | 0 | 1912 improvement |
| 3709 | German | SMS V25 | SMS V25 | Base | DD | Destroyer | Type 1913 | 1913 | 1913 | 1913 | 1000 | 1150 | 30 | 24.0 | 5000 | 1000000 | 80 | 0 | 71 ships built, +30% production, UNIQUE |
| 3710 | German | SMS G37 | SMS G37 | Base | DD | Destroyer | Type 1913 | 1914 | 1914 | 1914 | 1000 | 1150 | 30 | 24.0 | 5000 | 1050000 | 80 | 0 | Type 1913 standard |
| 3711 | German | SMS V43 | SMS V43 | Base | DD | Destroyer | Type 1913 | 1914 | 1914 | 1914 | 1000 | 1150 | 30 | 24.0 | 5000 | 1100000 | 80 | 0 | V25-class variant |
| 3712 | German | SMS B97 | SMS B97 | Base | DD | Destroyer | Type 1914 | 1914 | 1914 | 1914 | 1000 | 1150 | 30 | 24.0 | 5000 | 1200000 | 85 | 0 | 1914 program advanced |
| 3713 | German | SMS G101 | SMS G101 | Base | DD | Destroyer | Type 1914 | 1915 | 1915 | 1915 | 1000 | 1150 | 30 | 24.0 | 5000 | 1250000 | 85 | 0 | 1914 Type improved |
| 3714 | German | SMS V105 | SMS V105 | Base | DD | Destroyer | Type 1914 | 1915 | 1915 | 1915 | 1000 | 1150 | 30 | 24.0 | 5000 | 1300000 | 85 | 0 | Ultimate WWI design |
| 3715 | German | Möwe | Möwe | Base | DD | Destroyer | Type 23 | 1926 | 1926 | 1926 | 2000 | 2300 | 35 | 28.0 | 5000 | 1500000 | 129 | 0 | First post-treaty DD, +20% prestige |
| 3716 | German | Greif | Greif | Base | DD | Destroyer | Type 23 | 1927 | 1927 | 1927 | 2000 | 2300 | 35 | 28.0 | 5000 | 1550000 | 129 | 0 | Treaty restrictions |
| 3717 | German | Wolf | Wolf | Base | DD | Destroyer | Type 24 | 1928 | 1928 | 1928 | 2000 | 2300 | 35 | 28.0 | 5000 | 1600000 | 129 | 0 | Improved Type 23 |
| 3718 | German | Jaguar | Jaguar | Base | DD | Destroyer | Type 24 | 1929 | 1929 | 1929 | 2000 | 2300 | 35 | 28.0 | 5000 | 1650000 | 129 | 0 | Last interwar design |
| 3719 | German | Z1 Leberecht Maass | Z1 Leberecht Maass | Base | DD | Destroyer | Type 1934 | 1937 | 1937 | 1937 | 2000 | 2300 | 35 | 28.0 | 5000 | 4000000 | 315 | 0 | First post-Versailles DD, +25% capability |
| 3720 | German | Z3 Max Schultz | Z3 Max Schultz | Base | DD | Destroyer | Type 1934 | 1937 | 1937 | 1937 | 2000 | 2300 | 35 | 28.0 | 5000 | 4200000 | 315 | 0 | First modern standard |
| 3721 | German | Z5 Paul Jacobi | Z5 Paul Jacobi | Base | DD | Destroyer | Type 1934A | 1938 | 1938 | 1938 | 2000 | 2300 | 35 | 28.0 | 5000 | 4500000 | 321 | 0 | Z5-Z16 improved |
| 3722 | German | Z17 Diether von Roeder | Z17 Diether von Roeder | Base | DD | Destroyer | Type 1936 | 1938 | 1938 | 1938 | 2000 | 2300 | 35 | 28.0 | 5000 | 5000000 | 321 | 0 | 40 kts speed, improved |
| 3723 | German | Z20 Karl Galster | Z20 Karl Galster | Base | DD | Destroyer | Type 1936 | 1939 | 1939 | 1939 | 2000 | 2300 | 35 | 28.0 | 5000 | 5200000 | 321 | 0 | Improved seakeeping |
| 3724 | German | Z23 | Z23 | Base | DD | Destroyer | Type 1936A Narvik | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 6000000 | 321 | 0 | 150mm guns on DD, +40% firepower, UNIQUE |
| 3725 | German | Z25 | Z25 | Base | DD | Destroyer | Type 1936A Narvik | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 6200000 | 321 | 0 | 150mm mastery, +35% firepower |
| 3726 | German | Z28 | Z28 | Base | DD | Destroyer | Type 1936A(Mob) | 1941 | 1941 | 1941 | 2000 | 2300 | 35 | 28.0 | 5000 | 6500000 | 321 | 0 | Type 1936A(Mob) variant |
| 3727 | German | Z35 | Z35 | Base | DD | Destroyer | Type 1936B | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 7000000 | 321 | 0 | 127mm return, +30% AA |
| 3728 | German | Z40 | Z40 | Base | DD | Destroyer | Type 1936B | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 7500000 | 321 | 0 | Late war AA improvements |
| 3729 | German | Z46 | Z46 | Base | DD | Destroyer | Type 1936C | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 8000000 | 321 | 0 | 128mm dual-purpose |
| 3730 | German | Z50 | Z50 | Base | DD | Destroyer | Type 1936C | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 8500000 | 321 | 0 | Never completed, -15% reliability |
| 3731 | German | V25 Modernization | V25 Modernization | Base | DD | Destroyer | Type 1913 Refit | 1917 | 1917 | 1917 | 1000 | 1150 | 30 | 24.0 | 5000 | 1500000 | 85 | 0 | 10.5cm upgrade from 8.8cm |
| 3732 | German | Type 1934 Refit | Type 1934 Refit | Base | DD | Destroyer | Type 1934 Upgrade | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 5000000 | 321 | 0 | AA improvements, radar |
| 3733 | German | Type 1936A Refit | Type 1936A Refit | Base | DD | Destroyer | Narvik Upgrade | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 6500000 | 321 | 0 | Late war AA, radar |
| 3734 | German | Z51 Diesel | Z51 Diesel | Base | DD | Destroyer | Type 1942 | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 10000000 | 280 | 0 | Diesel engines, +30% range, experimental |
| 3735 | German | Type 1944 | Type 1944 | Base | DD | Destroyer | Type 1944 | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 12000000 | 320 | 0 | 128mm DP, most advanced, -10% reliability |
| 3736 | German | Type 1945 | Type 1945 | Base | DD | Destroyer | Type 1945 | 1946 | 1946 | 1946 | 5000 | 5750 | 35 | 28.0 | 5000 | 15000000 | 320 | 0 | Ultimate paper, -15% reliability |
| 3737 | German | Post-War Destroyer | Post-War Destroyer | Base | DD | Destroyer | Post-War | 1950 | 1950 | 1950 | 5000 | 5750 | 35 | 28.0 | 5000 | 20000000 | 350 | 0 | Post-war concept, -10% reliability |
| 3738 | German | Future DD Concept | Future DD Concept | Base | DD | Destroyer | Future Design | 1955 | 1955 | 1955 | 5000 | 5750 | 35 | 28.0 | 5000 | 30000000 | 400 | 0 | Guided missiles, future tech |
| 3800 | German | U-1 | U-1 | Base | SS | Submarine | U-boat | 1906 | 1906 | 1906 | 500 | 575 | 15 | 12.0 | 8000 | 500000 | 28 | 0 | First German U-boat, world's first practical military submarine, FREE |
| 3801 | German | U-9 | U-9 | Base | SS | Submarine | U-boat | 1910 | 1910 | 1910 | 500 | 575 | 15 | 12.0 | 8000 | 550000 | 29 | 0 | Sank 3 cruisers in 1 hour, +40% torpedo, FREE |
| 3802 | German | U-31 | U-31 | Base | SS | Submarine | U-boat | 1914 | 1914 | 1914 | 500 | 575 | 15 | 12.0 | 8000 | 700000 | 35 | 0 | Germaniawerft diesel design |
| 3803 | German | U-81 | U-81 | Base | SS | Submarine | U-boat | 1916 | 1916 | 1916 | 500 | 575 | 15 | 12.0 | 8000 | 850000 | 36 | 0 | Enhanced ocean capability |
| 3804 | German | U-87 | U-87 | Base | SS | Submarine | U-boat | 1916 | 1916 | 1916 | 500 | 575 | 15 | 12.0 | 8000 | 950000 | 37 | 0 | WWI advanced design |
| 3805 | German | U-93 | U-93 | Base | SS | Submarine | U-boat | 1917 | 1917 | 1917 | 500 | 575 | 15 | 12.0 | 8000 | 1100000 | 39 | 0 | 9,000 nm range, 16 torpedoes, +25% endurance |
| 3806 | German | UB-I | UB-I | Base | SS | Submarine | Coastal U-boat | 1915 | 1915 | 1915 | 500 | 575 | 15 | 12.0 | 8000 | 400000 | 14 | 0 | Early coastal operations |
| 3807 | German | UB-II | UB-II | Base | SS | Submarine | Coastal U-boat | 1915 | 1915 | 1915 | 500 | 575 | 15 | 12.0 | 8000 | 500000 | 23 | 0 | Doubled size, improved |
| 3808 | German | UB-III | UB-III | Base | SS | Submarine | Coastal U-boat | 1917 | 1917 | 1917 | 500 | 575 | 15 | 12.0 | 8000 | 800000 | 34 | 0 | 96 boats built, +30% coastal operations |
| 3809 | German | UC-I | UC-I | Base | SS | Submarine | Minelayer | 1915 | 1915 | 1915 | 500 | 575 | 15 | 12.0 | 8000 | 450000 | 18 | 0 | First minelaying design |
| 3810 | German | UC-II | UC-II | Base | SS | Submarine | Minelayer | 1916 | 1916 | 1916 | 500 | 575 | 15 | 12.0 | 8000 | 650000 | 26 | 0 | Ideal combination, +35% versatility, UNIQUE |
| 3811 | German | UC-III | UC-III | Base | SS | Submarine | Minelayer | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 900000 | 32 | 0 | Late war ultimate |
| 3812 | German | Type IA | Type IA | Base | SS | Submarine | U-boat | 1936 | 1936 | 1936 | 1500 | 1724 | 15 | 12.0 | 8000 | 2000000 | 43 | 0 | First post-treaty ocean-going |
| 3813 | German | Type IIA | Type IIA | Base | SS | Submarine | Coastal U-boat | 1935 | 1935 | 1935 | 1500 | 1724 | 15 | 12.0 | 8000 | 1200000 | 25 | 0 | Treaty limitations |
| 3814 | German | Type IIB | Type IIB | Base | SS | Submarine | Coastal U-boat | 1936 | 1936 | 1936 | 1500 | 1724 | 15 | 12.0 | 8000 | 1400000 | 25 | 0 | 20 boats improved |
| 3815 | German | Type IIC | Type IIC | Base | SS | Submarine | Coastal U-boat | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 1500000 | 25 | 0 | Enhanced design |
| 3816 | German | Type IID | Type IID | Base | SS | Submarine | Coastal U-boat | 1940 | 1940 | 1940 | 1500 | 1724 | 15 | 12.0 | 8000 | 1600000 | 25 | 0 | Last Type II variant |
| 3817 | German | Type VIIA | Type VIIA | Base | SS | Submarine | U-boat | 1936 | 1936 | 1936 | 1500 | 1724 | 15 | 12.0 | 8000 | 3000000 | 44 | 0 | Production model |
| 3818 | German | Type VIIB | Type VIIB | Base | SS | Submarine | U-boat | 1939 | 1939 | 1939 | 1500 | 1724 | 15 | 12.0 | 8000 | 3500000 | 44 | 0 | 24 boats, improved |
| 3819 | German | Type VIIC | Type VIIC | Base | SS | Submarine | U-boat | 1941 | 1941 | 1941 | 1500 | 1724 | 15 | 12.0 | 8000 | 4000000 | 44 | 0 | 577-593 boats, +35% production, UNIQUE |
| 3820 | German | Type VIID | Type VIID | Base | SS | Submarine | Minelayer | 1942 | 1942 | 1942 | 1500 | 1724 | 15 | 12.0 | 8000 | 4500000 | 44 | 0 | 6 boats, mine variant |
| 3821 | German | Type VIIF | Type VIIF | Base | SS | Submarine | Tanker | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 5000000 | 44 | 0 | 4 boats, resupply |
| 3822 | German | Type IXA | Type IXA | Base | SS | Submarine | U-boat | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 4500000 | 48 | 0 | 10,500 nm range |
| 3823 | German | Type IXB | Type IXB | Base | SS | Submarine | U-boat | 1939 | 1939 | 1939 | 1500 | 1724 | 15 | 12.0 | 8000 | 5000000 | 48 | 0 | Improved design |
| 3824 | German | Type IXC | Type IXC | Base | SS | Submarine | U-boat | 1940 | 1940 | 1940 | 1500 | 1724 | 15 | 12.0 | 8000 | 5500000 | 48 | 0 | Standard long-range |
| 3825 | German | Type IXC/40 | Type IXC/40 | Base | SS | Submarine | U-boat | 1941 | 1941 | 1941 | 1500 | 1724 | 15 | 12.0 | 8000 | 6000000 | 48 | 0 | 87 boats, enhanced |
| 3826 | German | Type IXD | Type IXD | Base | SS | Submarine | U-boat | 1942 | 1942 | 1942 | 1500 | 1724 | 15 | 12.0 | 8000 | 7000000 | 57 | 0 | 23,700 nm range, +130% endurance, UNIQUE |
| 3827 | German | Type XIV | Type XIV | Base | SS | Submarine | Tanker | 1941 | 1941 | 1941 | 1500 | 1724 | 15 | 12.0 | 8000 | 6500000 | 53 | 0 | 203 tons fuel, +100% fleet endurance, UNIQUE |
| 3828 | German | Type XVII | Type XVII | Base | SS | Submarine | Experimental | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 8000000 | 19 | 0 | Experimental propulsion |
| 3829 | German | Type XXI | Type XXI | Base | SS | Submarine | Elektroboot | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 12000000 | 57 | 0 | 17 kts submerged, 7 days underwater, +200%, UNIQUE |
| 3830 | German | Type XXIII | Type XXIII | Base | SS | Submarine | Elektroboot | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 5000000 | 14 | 0 | World's fastest submarine, +40% coastal |
| 3831 | German | Biber | Biber | Base | SS | Submarine | Midget | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 200000 | 1 | 0 | 324 built, midget ops |
| 3832 | German | Molch | Molch | Base | SS | Submarine | Midget | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 150000 | 1 | 0 | Single-man operations |
| 3833 | German | Seehund | Seehund | Base | SS | Submarine | Midget | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 300000 | 2 | 0 | Most successful midget, 285 built, 9 ships sunk |
| 3834 | German | U-93 Modernization | U-93 Modernization | Base | SS | Submarine | U-boat Refit | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 1500000 | 39 | 0 | 10.5cm gun upgrade |
| 3835 | German | Type VIIC Refit | Type VIIC Refit | Base | SS | Submarine | U-boat Upgrade | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 5000000 | 44 | 0 | AA improvements, radar |
| 3836 | German | Type XXI Refit | Type XXI Refit | Base | SS | Submarine | Elektroboot Upgrade | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 13000000 | 57 | 0 | Post-war improvements |
| 3837 | German | Type XXVI | Type XXVI | Base | SS | Submarine | Advanced Elektroboot | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 15000000 | 60 | 0 | Never completed, -10% reliability |
| 3838 | German | Type XXIX | Type XXIX | Base | SS | Submarine | Ultimate WWII | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 18000000 | 65 | 0 | Paper ship, -15% reliability |
| 3839 | German | Type XXX | Type XXX | Base | SS | Submarine | Post-War | 1946 | 1946 | 1946 | 3000 | 3449 | 20 | 16.0 | 8000 | 20000000 | 70 | 0 | Post-war concept, -10% reliability |
| 3840 | German | Type 201 | Type 201 | Base | SS | Submarine | Post-War | 1950 | 1950 | 1950 | 3000 | 3449 | 20 | 16.0 | 8000 | 25000000 | 75 | 0 | Post-war design |
| 3841 | German | Type 205 | Type 205 | Base | SS | Submarine | Advanced | 1955 | 1955 | 1955 | 3000 | 3449 | 20 | 16.0 | 8000 | 30000000 | 80 | 0 | Advanced, snorkel |
| 3842 | German | Type 206 | Type 206 | Base | SS | Submarine | Cold War | 1960 | 1960 | 1960 | 3000 | 3449 | 20 | 16.0 | 8000 | 35000000 | 85 | 0 | Cold War tech |
| 3843 | German | Nuclear Concept | Nuclear Concept | Base | SS | Submarine | Nuclear | 1965 | 1965 | 1965 | 3000 | 3449 | 20 | 16.0 | 8000 | 50000000 | 100 | 0 | Theoretical nuclear, -15% reliability |
| 3844 | German | Future SS Concept | Future SS Concept | Base | SS | Submarine | Future Design | 1970 | 1970 | 1970 | 3000 | 3449 | 20 | 16.0 | 8000 | 80000000 | 120 | 0 | Future submarine tech |
| 3100 | German | Conversion Study | Conversion Study | Base | CV | Aircraft Carrier | Carrier Concept | 1918 | 1918 | 1918 | 25000 | 28749 | 30 | 24.0 | 12000 | 1000000 | 500 | 0 | First German carrier studies, +10% research speed |
| 3101 | German | Japanese Study | Japanese Study | Base | CV | Aircraft Carrier | Carrier Analysis | 1928 | 1928 | 1928 | 25000 | 28749 | 30 | 24.0 | 12000 | 1500000 | 600 | 0 | Japanese carrier expertise, +20% effectiveness |
| 3102 | German | Plan Z Concept | Plan Z Concept | Base | CV | Aircraft Carrier | Plan Z | 1935 | 1935 | 1935 | 30000 | 34500 | 30 | 24.0 | 12000 | 2000000 | 800 | 0 | Ambitious naval program, +15% capability |
| 3103 | German | Graf Zeppelin | Graf Zeppelin | Base | CV | Aircraft Carrier | Fleet Carrier | 1938 | 1938 | 1938 | 30000 | 34500 | 30 | 24.0 | 12000 | 50000000 | 1760 | 0 | Famous unfinished carrier, +30% capability if completed |
| 3104 | German | Peter Strasser | Peter Strasser | Base | CV | Aircraft Carrier | Fleet Carrier | 1939 | 1939 | 1939 | 30000 | 34500 | 30 | 24.0 | 12000 | 45000000 | 1760 | 0 | Early cancellation, -20% reliability (incomplete) |
| 3105 | German | Flugzeugträger C | Flugzeugträger C | Base | CV | Aircraft Carrier | Fleet Carrier | 1940 | 1940 | 1940 | 35000 | 40250 | 33 | 26.4 | 12000 | 55000000 | 1800 | 0 | Never started, -15% reliability |
| 3106 | German | Flugzeugträger D | Flugzeugträger D | Base | CV | Aircraft Carrier | Fleet Carrier | 1940 | 1940 | 1940 | 35000 | 40250 | 33 | 26.4 | 12000 | 55000000 | 1800 | 0 | Never started, -15% reliability |
| 3107 | German | Europa Conversion | Europa Conversion | Base | CV | Aircraft Carrier | Auxiliary Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 40000000 | 1500 | 0 | Theoretical conversion, -20% reliability |
| 3108 | German | Improved Graf Zeppelin | Improved Graf Zeppelin | Base | CV | Aircraft Carrier | Fleet Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 65000000 | 1900 | 0 | Incorporates experience, +25%, -15% reliability |
| 3109 | German | Armored Deck Carrier | Armored Deck Carrier | Base | CV | Aircraft Carrier | Armored Carrier | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 70000000 | 1950 | 0 | Armored flight deck, +40% survivability, -15% reliability |
| 3110 | German | Plan Z Super Carrier | Plan Z Super Carrier | Base | CV | Aircraft Carrier | Super Carrier | 1945 | 1945 | 1945 | 45000 | 51749 | 33 | 26.4 | 12000 | 90000000 | 2200 | 0 | Maximum WWII carrier, +50% capability, -20% reliability |
| 3111 | German | Post-War Carrier | Post-War Carrier | Base | CV | Aircraft Carrier | Post-War | 1950 | 1950 | 1950 | 45000 | 51749 | 33 | 26.4 | 12000 | 120000000 | 2500 | 0 | Post-war concept, -15% reliability |
| 3112 | German | Jet Age Carrier | Jet Age Carrier | Base | CV | Aircraft Carrier | Jet Carrier | 1955 | 1955 | 1955 | 45000 | 51749 | 33 | 26.4 | 12000 | 150000000 | 2800 | 0 | Jet capable, -15% reliability |
| 3113 | German | Modern Carrier | Modern Carrier | Base | CV | Aircraft Carrier | Modern | 1960 | 1960 | 1960 | 90000 | 103499 | 33 | 26.4 | 12000 | 200000000 | 3000 | 0 | Modern systems, -10% reliability |
| 3114 | German | Future CV Concept | Future CV Concept | Base | CV | Aircraft Carrier | Future Design | 1970 | 1970 | 1970 | 90000 | 103499 | 33 | 26.4 | 12000 | 300000000 | 3500 | 0 | Future carrier tech |
| 4000 | Japanese | Mikasa | Mikasa | Base | BB | Battleship | Battleship | 1900 | 1900 | 1900 | 12000 | 13799 | 18 | 14.4 | 15000 | 600000 | 305 | 0 | Tōgō's flagship, +40% morale, HISTORIC, FREE |
| 4001 | Japanese | Fuji | Fuji | Base | BB | Battleship | Battleship | 1896 | 1896 | 1896 | 12000 | 13799 | 18 | 14.4 | 15000 | 500000 | 305 | 0 | First modern BB, +25% foundation, FREE |
| 4002 | Japanese | Shikishima | Shikishima | Base | BB | Battleship | Battleship | 1898 | 1898 | 1898 | 12000 | 13799 | 18 | 14.4 | 15000 | 650000 | 305 | 0 | British-built, +15% quality |
| 4003 | Japanese | Asahi | Asahi | Base | BB | Battleship | Battleship | 1899 | 1899 | 1899 | 12000 | 13799 | 18 | 14.4 | 15000 | 700000 | 305 | 0 | British-built, +15% capability |
| 4004 | Japanese | Katori | Katori | Base | BB | Battleship | Battleship | 1905 | 1905 | 1905 | 12000 | 13799 | 18 | 14.4 | 15000 | 800000 | 380 | 0 | Combat lessons, +20% experience |
| 4005 | Japanese | Satsuma | Satsuma | Base | BB | Battleship | Semi-Dreadnought | 1906 | 1906 | 1906 | 20000 | 23000 | 21 | 16.8 | 15000 | 1200000 | 490 | 0 | Japanese-built, +25% independence |
| 4006 | Japanese | Aki | Aki | Base | BB | Battleship | Semi-Dreadnought | 1907 | 1907 | 1907 | 20000 | 23000 | 21 | 16.8 | 15000 | 1300000 | 495 | 0 | Refined Satsuma, +20% capability |
| 4007 | Japanese | Kawachi | Kawachi | Base | BB | Battleship | Dreadnought | 1910 | 1910 | 1910 | 20000 | 23000 | 21 | 16.8 | 15000 | 2000000 | 545 | 0 | First Japanese dreadnought, +30% capability |
| 4008 | Japanese | Settsu | Settsu | Base | BB | Battleship | Dreadnought | 1911 | 1911 | 1911 | 20000 | 23000 | 21 | 16.8 | 15000 | 2200000 | 550 | 0 | Refined Kawachi, +15% reliability |
| 4009 | Japanese | Kongō | Kongō | Base | BB | Battleship | Battlecruiser | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 3500000 | 700 | 0 | Vickers-built, +30% quality |
| 4010 | Japanese | Hiei | Hiei | Base | BB | Battleship | Battlecruiser | 1912 | 1912 | 1912 | 20000 | 23000 | 21 | 16.8 | 15000 | 3600000 | 700 | 0 | Indigenous construction, +20% |
| 4011 | Japanese | Haruna | Haruna | Base | BB | Battleship | Battlecruiser | 1913 | 1913 | 1913 | 20000 | 23000 | 21 | 16.8 | 15000 | 3700000 | 705 | 0 | Indigenous, +20% |
| 4012 | Japanese | Kirishima | Kirishima | Base | BB | Battleship | Battlecruiser | 1913 | 1913 | 1913 | 20000 | 23000 | 21 | 16.8 | 15000 | 3800000 | 710 | 0 | Indigenous, +20% |
| 4013 | Japanese | Fusō | Fusō | Base | BB | Battleship | Super-Dreadnought | 1914 | 1914 | 1914 | 20000 | 23000 | 21 | 16.8 | 15000 | 5000000 | 910 | 0 | 12×14" guns, +35% firepower, distinctive |
| 4014 | Japanese | Yamashiro | Yamashiro | Base | BB | Battleship | Super-Dreadnought | 1915 | 1915 | 1915 | 32000 | 36800 | 23 | 18.4 | 15000 | 5200000 | 920 | 0 | Distinctive profile, +30% |
| 4015 | Japanese | Ise | Ise | Base | BB | Battleship | Super-Dreadnought | 1916 | 1916 | 1916 | 32000 | 36800 | 23 | 18.4 | 15000 | 5500000 | 930 | 0 | Better turret arrangement, +25% |
| 4016 | Japanese | Hyūga | Hyūga | Base | BB | Battleship | Super-Dreadnought | 1917 | 1917 | 1917 | 32000 | 36800 | 23 | 18.4 | 15000 | 5700000 | 940 | 0 | Refined Ise, +20% |
| 4017 | Japanese | Nagato | Nagato | Base | BB | Battleship | Battleship | 1919 | 1919 | 1919 | 32000 | 36800 | 23 | 18.4 | 15000 | 10000000 | 990 | 0 | First 16" guns afloat, +35% firepower, HISTORIC |
| 4018 | Japanese | Mutsu | Mutsu | Base | BB | Battleship | Battleship | 1920 | 1920 | 1920 | 32000 | 36800 | 23 | 18.4 | 15000 | 10500000 | 1000 | 0 | Built by donations, +25% morale |
| 4019 | Japanese | Tosa | Tosa | Base | BB | Battleship | Battleship | 1921 | 1921 | 1921 | 32000 | 36800 | 23 | 18.4 | 15000 | 12000000 | 1010 | 0 | 40% complete, -20% reliability (cancelled) |
| 4020 | Japanese | Kaga | Kaga | Base | BB | Battleship | Battleship | 1921 | 1921 | 1921 | 32000 | 36800 | 23 | 18.4 | 15000 | 12500000 | 1020 | 0 | Converted to CV, -15% reliability |
| 4021 | Japanese | Kii | Kii | Base | BB | Battleship | Fast Battleship | 1922 | 1922 | 1922 | 35000 | 40250 | 23 | 18.4 | 15000 | 13000000 | 1080 | 0 | Never started, -20% reliability |
| 4022 | Japanese | Owari | Owari | Base | BB | Battleship | Fast Battleship | 1922 | 1922 | 1922 | 35000 | 40250 | 23 | 18.4 | 15000 | 13500000 | 1080 | 0 | Never started, -20% reliability |
| 4023 | Japanese | Number 13 | Number 13 | Base | BB | Battleship | Fast Battleship | 1922 | 1922 | 1922 | 35000 | 40250 | 23 | 18.4 | 15000 | 18000000 | 1200 | 0 | Revolutionary, +40%, -25% reliability (cancelled) |
| 4024 | Japanese | Number 14 | Number 14 | Base | BB | Battleship | Fast Battleship | 1922 | 1922 | 1922 | 35000 | 40250 | 23 | 18.4 | 15000 | 18500000 | 1210 | 0 | Never started, -25% reliability |
| 4025 | Japanese | Kongō Kai | Kongō Kai | Base | BB | Battleship | Fast Battleship | 1935 | 1935 | 1935 | 35000 | 40250 | 23 | 18.4 | 15000 | 8000000 | 805 | 0 | 30+ kts, +50% speed, +40%, REVOLUTIONARY |
| 4026 | Japanese | Hiei Kai | Hiei Kai | Base | BB | Battleship | Fast Battleship | 1936 | 1936 | 1936 | 45000 | 51749 | 30 | 24.0 | 15000 | 8200000 | 810 | 0 | 30+ kts, +50% speed, +35% |
| 4027 | Japanese | Haruna Kai | Haruna Kai | Base | BB | Battleship | Fast Battleship | 1937 | 1937 | 1937 | 45000 | 51749 | 30 | 24.0 | 15000 | 8400000 | 815 | 0 | 30+ kts, +50% speed, +35% |
| 4028 | Japanese | Kirishima Kai | Kirishima Kai | Base | BB | Battleship | Fast Battleship | 1938 | 1938 | 1938 | 45000 | 51749 | 30 | 24.0 | 15000 | 8600000 | 820 | 0 | Fastest BBs afloat, +50% speed |
| 4029 | Japanese | Nagato Kai | Nagato Kai | Base | BB | Battleship | Battleship | 1936 | 1936 | 1936 | 45000 | 51749 | 30 | 24.0 | 15000 | 12000000 | 1080 | 0 | Improved protection, +25% |
| 4030 | Japanese | Mutsu Kai | Mutsu Kai | Base | BB | Battleship | Battleship | 1936 | 1936 | 1936 | 45000 | 51749 | 30 | 24.0 | 15000 | 12500000 | 1090 | 0 | Enhanced capability, +25% |
| 4031 | Japanese | Fusō Kai | Fusō Kai | Base | BB | Battleship | Battleship | 1933 | 1933 | 1933 | 35000 | 40250 | 23 | 18.4 | 15000 | 7000000 | 1000 | 0 | Pagoda mast, +20% |
| 4032 | Japanese | Yamashiro Kai | Yamashiro Kai | Base | BB | Battleship | Battleship | 1935 | 1935 | 1935 | 35000 | 40250 | 23 | 18.4 | 15000 | 7500000 | 1010 | 0 | Improved AA, +20% |
| 4033 | Japanese | Yamato | Yamato | Base | BB | Battleship | Super-Battleship | 1940 | 1940 | 1940 | 45000 | 51749 | 30 | 24.0 | 15000 | 100000000 | 1820 | 0 | 18.1" guns, 72,000 tons, +100%, LEGENDARY |
| 4034 | Japanese | Musashi | Musashi | Base | BB | Battleship | Super-Battleship | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 105000000 | 1830 | 0 | 17 bombs/19 torps, +60% survivability, HISTORIC |
| 4035 | Japanese | Shinano | Shinano | Base | BB | Battleship | Carrier Conversion | 1944 | 1944 | 1944 | 45000 | 51749 | 30 | 24.0 | 15000 | 90000000 | 1650 | 0 | Converted to CV, -20% reliability |
| 4036 | Japanese | Ise Kai-II | Ise Kai-II | Base | BB | Battleship | Hybrid BB-CV | 1943 | 1943 | 1943 | 45000 | 51749 | 30 | 24.0 | 15000 | 15000000 | 1100 | 0 | BB+CV hybrid, +30% versatility, -20% reliability |
| 4037 | Japanese | Hyūga Kai-II | Hyūga Kai-II | Base | BB | Battleship | Hybrid BB-CV | 1943 | 1943 | 1943 | 45000 | 51749 | 30 | 24.0 | 15000 | 15500000 | 1110 | 0 | Hybrid conversion, +30% versatility, -20% |
| 4038 | Japanese | Design A-150 | Design A-150 | Base | BB | Battleship | Super-Battleship | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 120000000 | 2280 | 0 | 20.1" guns, +120% firepower, -30% reliability |
| 4039 | Japanese | Design A-150 (2) | Design A-150 (2) | Base | BB | Battleship | Super-Battleship | 1941 | 1941 | 1941 | 45000 | 51749 | 30 | 24.0 | 15000 | 125000000 | 2300 | 0 | 20.1" guns, +120% firepower, -30% |
| 4040 | Japanese | Post-War BB | Post-War BB | Base | BB | Battleship | Post-War | 1950 | 1950 | 1950 | 50000 | 57499 | 30 | 24.0 | 15000 | 150000000 | 2400 | 0 | Prohibited by occupation, -20% reliability |
| 4041 | Japanese | Guided Missile BB | Guided Missile BB | Base | BB | Battleship | Missile BB | 1960 | 1960 | 1960 | 50000 | 57499 | 30 | 24.0 | 15000 | 200000000 | 2500 | 0 | Never pursued, -20% reliability |
| 4042 | Japanese | Future BB Concept | Future BB Concept | Base | BB | Battleship | Future Design | 1970 | 1970 | 1970 | 50000 | 57499 | 30 | 24.0 | 15000 | 250000000 | 2600 | 0 | Never pursued, -15% reliability |
| 4600 | Japanese | Asama | Asama | Base | CA | Heavy Cruiser | Armored Cruiser | 1896 | 1896 | 1896 | 10000 | 11500 | 25 | 20.0 | 10000 | 400000 | 245 | 0 | Tsushima victory, +30% experience, FREE |
| 4601 | Japanese | Tokiwa | Tokiwa | Base | CA | Heavy Cruiser | Armored Cruiser | 1898 | 1898 | 1898 | 10000 | 11500 | 25 | 20.0 | 10000 | 420000 | 250 | 0 | Tsushima, +25% experience, FREE |
| 4602 | Japanese | Izumo | Izumo | Base | CA | Heavy Cruiser | Armored Cruiser | 1899 | 1899 | 1899 | 10000 | 11500 | 25 | 20.0 | 10000 | 450000 | 250 | 0 | Tsushima service, +20% |
| 4603 | Japanese | Iwate | Iwate | Base | CA | Heavy Cruiser | Armored Cruiser | 1900 | 1900 | 1900 | 10000 | 11500 | 25 | 20.0 | 10000 | 470000 | 255 | 0 | Survived WWII, +15% |
| 4604 | Japanese | Kasuga | Kasuga | Base | CA | Heavy Cruiser | Armored Cruiser | 1902 | 1902 | 1902 | 10000 | 11500 | 25 | 20.0 | 10000 | 550000 | 280 | 0 | Italian Ansaldo-built, +20% |
| 4605 | Japanese | Nisshin | Nisshin | Base | CA | Heavy Cruiser | Armored Cruiser | 1903 | 1903 | 1903 | 10000 | 11500 | 25 | 20.0 | 10000 | 580000 | 285 | 0 | Italian design, +15% |
| 4606 | Japanese | Tsukuba | Tsukuba | Base | CA | Heavy Cruiser | Armored Cruiser | 1905 | 1905 | 1905 | 10000 | 11500 | 25 | 20.0 | 10000 | 750000 | 350 | 0 | Japanese-built, +25% |
| 4607 | Japanese | Ikoma | Ikoma | Base | CA | Heavy Cruiser | Armored Cruiser | 1906 | 1906 | 1906 | 10000 | 11500 | 25 | 20.0 | 10000 | 780000 | 355 | 0 | Indigenous, +20% |
| 4608 | Japanese | Ibuki | Ibuki | Base | CA | Heavy Cruiser | Armored Cruiser | 1907 | 1907 | 1907 | 10000 | 11500 | 25 | 20.0 | 10000 | 900000 | 375 | 0 | Pre-battlecruiser, +25% |
| 4609 | Japanese | Kurama | Kurama | Base | CA | Heavy Cruiser | Armored Cruiser | 1909 | 1909 | 1909 | 10000 | 11500 | 25 | 20.0 | 10000 | 950000 | 380 | 0 | Peak armored cruiser, +20% |
| 4610 | Japanese | Tenryū | Tenryū | Base | CL | Light Cruiser | Light Cruiser | 1918 | 1918 | 1918 | 5000 | 5750 | 25 | 20.0 | 8000 | 1800000 | 80 | 0 | First modern light cruiser, +30% |
| 4611 | Japanese | Tatsuta | Tatsuta | Base | CL | Light Cruiser | Light Cruiser | 1919 | 1919 | 1919 | 5000 | 5750 | 25 | 20.0 | 8000 | 1900000 | 82 | 0 | First modern CL, +25% |
| 4612 | Japanese | Kuma | Kuma | Base | CL | Light Cruiser | Light Cruiser | 1919 | 1919 | 1919 | 5000 | 5750 | 25 | 20.0 | 8000 | 2200000 | 140 | 0 | 7×5.5" guns, +20% |
| 4613 | Japanese | Tama | Tama | Base | CL | Light Cruiser | Light Cruiser | 1920 | 1920 | 1920 | 10000 | 11500 | 32 | 25.6 | 8000 | 2300000 | 142 | 0 | 6-ship class, +15% |
| 4614 | Japanese | Kitakami | Kitakami | Base | CL | Light Cruiser | Light Cruiser | 1920 | 1920 | 1920 | 10000 | 11500 | 32 | 25.6 | 8000 | 2400000 | 145 | 0 | 40× Type 93 torps (conversion), +100% torpedo |
| 4615 | Japanese | Ōi | Ōi | Base | CL | Light Cruiser | Light Cruiser | 1921 | 1921 | 1921 | 10000 | 11500 | 32 | 25.6 | 8000 | 2500000 | 147 | 0 | 40× torps (conversion), +100% |
| 4616 | Japanese | Nagara | Nagara | Base | CL | Light Cruiser | Light Cruiser | 1921 | 1921 | 1921 | 10000 | 11500 | 32 | 25.6 | 8000 | 2600000 | 140 | 0 | Refined Kuma, +15% |
| 4617 | Japanese | Isuzu | Isuzu | Base | CL | Light Cruiser | Light Cruiser | 1921 | 1921 | 1921 | 10000 | 11500 | 32 | 25.6 | 8000 | 2700000 | 142 | 0 | 66×25mm AA (conversion), +80% AA |
| 4618 | Japanese | Sendai | Sendai | Base | CL | Light Cruiser | Light Cruiser | 1922 | 1922 | 1922 | 10000 | 11500 | 32 | 25.6 | 8000 | 2800000 | 140 | 0 | Refined design, +15% |
| 4619 | Japanese | Jintsu | Jintsu | Base | CL | Light Cruiser | Light Cruiser | 1923 | 1923 | 1923 | 10000 | 11500 | 32 | 25.6 | 8000 | 2900000 | 142 | 0 | Night battle hero, +30% night combat |
| 4620 | Japanese | Yūbari | Yūbari | Base | CL | Light Cruiser | Light Cruiser | 1923 | 1923 | 1923 | 10000 | 11500 | 32 | 25.6 | 8000 | 3000000 | 73 | 0 | Weight-saving, +25% efficiency, INNOVATIVE |
| 4621 | Japanese | Furutaka | Furutaka | Base | CA | Heavy Cruiser | Heavy Cruiser | 1925 | 1925 | 1925 | 13000 | 14949 | 32 | 25.6 | 10000 | 4500000 | 235 | 0 | First 8" cruiser, +25% |
| 4622 | Japanese | Kako | Kako | Base | CA | Heavy Cruiser | Heavy Cruiser | 1925 | 1925 | 1925 | 13000 | 14949 | 32 | 25.6 | 10000 | 4700000 | 240 | 0 | Treaty cruiser, +20% |
| 4623 | Japanese | Aoba | Aoba | Base | CA | Heavy Cruiser | Heavy Cruiser | 1926 | 1926 | 1926 | 13000 | 14949 | 32 | 25.6 | 10000 | 5500000 | 245 | 0 | Twin turrets, +20% |
| 4624 | Japanese | Kinugasa | Kinugasa | Base | CA | Heavy Cruiser | Heavy Cruiser | 1926 | 1926 | 1926 | 13000 | 14949 | 32 | 25.6 | 10000 | 5700000 | 250 | 0 | Improved design, +15% |
| 4625 | Japanese | Myōkō | Myōkō | Base | CA | Heavy Cruiser | Heavy Cruiser | 1927 | 1927 | 1927 | 13000 | 14949 | 32 | 25.6 | 10000 | 8000000 | 330 | 0 | 10×8" guns, +40% firepower, LEGENDARY |
| 4626 | Japanese | Nachi | Nachi | Base | CA | Heavy Cruiser | Heavy Cruiser | 1927 | 1927 | 1927 | 13000 | 14949 | 32 | 25.6 | 10000 | 8200000 | 335 | 0 | 10×8" guns, +40% firepower |
| 4627 | Japanese | Ashigara | Ashigara | Base | CA | Heavy Cruiser | Heavy Cruiser | 1928 | 1928 | 1928 | 13000 | 14949 | 32 | 25.6 | 10000 | 8400000 | 340 | 0 | 10×8" guns, +40% firepower |
| 4628 | Japanese | Haguro | Haguro | Base | CA | Heavy Cruiser | Heavy Cruiser | 1928 | 1928 | 1928 | 13000 | 14949 | 32 | 25.6 | 10000 | 8600000 | 345 | 0 | 10×8" guns, +40% firepower |
| 4629 | Japanese | Takao | Takao | Base | CA | Heavy Cruiser | Heavy Cruiser | 1930 | 1930 | 1930 | 13000 | 14949 | 32 | 25.6 | 10000 | 9500000 | 335 | 0 | Better armor, +30% protection |
| 4630 | Japanese | Atago | Atago | Base | CA | Heavy Cruiser | Heavy Cruiser | 1930 | 1930 | 1930 | 13000 | 14949 | 32 | 25.6 | 10000 | 9700000 | 340 | 0 | Kurita's flagship, +25% command |
| 4631 | Japanese | Chōkai | Chōkai | Base | CA | Heavy Cruiser | Heavy Cruiser | 1931 | 1931 | 1931 | 13000 | 14949 | 32 | 25.6 | 10000 | 9900000 | 345 | 0 | Distinguished service, +25% |
| 4632 | Japanese | Maya | Maya | Base | CA | Heavy Cruiser | Heavy Cruiser | 1932 | 1932 | 1932 | 13000 | 14949 | 32 | 25.6 | 10000 | 10100000 | 350 | 0 | AA conversion, +40% AA |
| 4633 | Japanese | Mogami | Mogami | Base | CA | Heavy Cruiser | Light/Heavy Cruiser | 1935 | 1935 | 1935 | 13000 | 14949 | 32 | 25.6 | 10000 | 12000000 | 285 | 0 | 15×6.1" → 10×8" conversion, +50% versatility, REVOLUTIONARY |
| 4634 | Japanese | Mikuma | Mikuma | Base | CA | Heavy Cruiser | Light/Heavy Cruiser | 1935 | 1935 | 1935 | 13000 | 14949 | 32 | 25.6 | 10000 | 12200000 | 290 | 0 | Conversion capability, +50% |
| 4635 | Japanese | Suzuya | Suzuya | Base | CA | Heavy Cruiser | Light/Heavy Cruiser | 1936 | 1936 | 1936 | 13000 | 14949 | 32 | 25.6 | 10000 | 12400000 | 295 | 0 | Revolutionary, +50% versatility |
| 4636 | Japanese | Kumano | Kumano | Base | CA | Heavy Cruiser | Light/Heavy Cruiser | 1936 | 1936 | 1936 | 13000 | 14949 | 32 | 25.6 | 10000 | 12600000 | 300 | 0 | Innovative conversion, +50% |
| 4637 | Japanese | Tone | Tone | Base | CA | Heavy Cruiser | Heavy Cruiser | 1938 | 1938 | 1938 | 13000 | 14949 | 32 | 25.6 | 10000 | 11000000 | 285 | 0 | All-forward layout, +35% recon, +25% aircraft, UNIQUE |
| 4638 | Japanese | Chikuma | Chikuma | Base | CA | Heavy Cruiser | Heavy Cruiser | 1938 | 1938 | 1938 | 13000 | 14949 | 32 | 25.6 | 10000 | 11200000 | 290 | 0 | Recon cruiser, +35% recon |
| 4639 | Japanese | Agano | Agano | Base | CL | Light Cruiser | Light Cruiser | 1941 | 1941 | 1941 | 10000 | 11500 | 32 | 25.6 | 8000 | 10000000 | 170 | 0 | AA-focused, +30% AA |
| 4640 | Japanese | Ōyodo | Ōyodo | Base | CL | Light Cruiser | Light Cruiser | 1942 | 1942 | 1942 | 10000 | 11500 | 32 | 25.6 | 8000 | 15000000 | 208 | 0 | Command facilities, +35% command |
| 4641 | Japanese | Ibuki (WWII) | Ibuki (WWII) | Base | CA | Heavy Cruiser | Heavy Cruiser | 1943 | 1943 | 1943 | 13000 | 14949 | 32 | 25.6 | 10000 | 18000000 | 310 | 0 | 80% complete, -20% reliability |
| 4642 | Japanese | Future Cruiser | Future Cruiser | Base | CA | Heavy Cruiser | Future Design | 1960 | 1960 | 1960 | 17000 | 19550 | 33 | 26.4 | 10000 | 25000000 | 350 | 0 | Never pursued, -15% reliability |
| 4700 | Japanese | Momo | Momo | Base | DD | Destroyer | Destroyer | 1916 | 1916 | 1916 | 1000 | 1150 | 30 | 24.0 | 5000 | 0 | 60 | 0 | Basic destroyer, FREE starting ship |
| 4701 | Japanese | Momi | Momi | Base | DD | Destroyer | Destroyer | 1920 | 1920 | 1920 | 2000 | 2300 | 35 | 28.0 | 5000 | 800000 | 90 | 0 | +15% speed, improved seakeeping |
| 4702 | Japanese | Minekaze | Minekaze | Base | DD | Destroyer | Destroyer | 1920 | 1920 | 1920 | 2000 | 2300 | 35 | 28.0 | 5000 | 1200000 | 120 | 0 | 39 knots, +25% speed, FREE starting ship |
| 4703 | Japanese | Kamikaze | Kamikaze | Base | DD | Destroyer | Destroyer | 1922 | 1922 | 1922 | 2000 | 2300 | 35 | 28.0 | 5000 | 1500000 | 150 | 0 | Washington Treaty compliant design |
| 4704 | Japanese | Mutsuki | Mutsuki | Base | DD | Destroyer | Destroyer | 1926 | 1926 | 1926 | 2000 | 2300 | 35 | 28.0 | 5000 | 1800000 | 180 | 0 | First 24-inch torpedoes, +30% torpedo power |
| 4705 | Japanese | Fubuki | Fubuki | Base | DD | Destroyer | Destroyer | 1928 | 1928 | 1928 | 2000 | 2300 | 35 | 28.0 | 5000 | 1500000 | 165 | 0 | Enclosed turrets, +50% capability, REVOLUTIONARY |
| 4706 | Japanese | Ayanami | Ayanami | Base | DD | Destroyer | Destroyer | 1930 | 1930 | 1930 | 2000 | 2300 | 35 | 28.0 | 5000 | 1600000 | 180 | 0 | +20% gunnery accuracy |
| 4707 | Japanese | Akatsuki | Akatsuki | Base | DD | Destroyer | Destroyer | 1932 | 1932 | 1932 | 2000 | 2300 | 35 | 28.0 | 5000 | 1700000 | 195 | 0 | +10% overall performance |
| 4708 | Japanese | Hatsuharu | Hatsuharu | Base | DD | Destroyer | Destroyer | 1933 | 1933 | 1933 | 2000 | 2300 | 35 | 28.0 | 5000 | 2000000 | 180 | 0 | Stability problems, -15% reliability initially |
| 4709 | Japanese | Shiratsuyu | Shiratsuyu | Base | DD | Destroyer | Destroyer | 1936 | 1936 | 1936 | 2000 | 2300 | 35 | 28.0 | 5000 | 2200000 | 210 | 0 | Stability corrected, +20% reliability |
| 4710 | Japanese | Asashio | Asashio | Base | DD | Destroyer | Destroyer | 1937 | 1937 | 1937 | 2000 | 2300 | 35 | 28.0 | 5000 | 2500000 | 225 | 0 | 6×5" guns, +25% firepower |
| 4711 | Japanese | Kagero | Kagero | Base | DD | Destroyer | Destroyer | 1939 | 1939 | 1939 | 2000 | 2300 | 35 | 28.0 | 5000 | 3000000 | 240 | 0 | Most-produced class, +15% production |
| 4712 | Japanese | Yūgumo | Yūgumo | Base | DD | Destroyer | Destroyer | 1941 | 1941 | 1941 | 2000 | 2300 | 35 | 28.0 | 5000 | 3200000 | 255 | 0 | +30% range, refined design |
| 4713 | Japanese | Akizuki | Akizuki | Base | DD | Destroyer | Destroyer | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 4000000 | 270 | 0 | 8×3.9" DP guns, +80% AA capability |
| 4714 | Japanese | Shimakaze | Shimakaze | Base | DD | Destroyer | Destroyer | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 5000000 | 240 | 0 | 40.9 knots record, 15× torpedoes, +100% capability, LEGENDARY |
| 4715 | Japanese | Fuyutsuki | Fuyutsuki | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 4200000 | 285 | 0 | +20% AA efficiency |
| 4716 | Japanese | Matsu | Matsu | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 2500000 | 210 | 0 | Simplified for fast production, -20% capability but fast build |
| 4717 | Japanese | Tachibana | Tachibana | Base | DD | Destroyer | Destroyer | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 2700000 | 225 | 0 | Final simplified design, +10% over Matsu |
| 4718 | Japanese | Super Shimakaze | Super Shimakaze | Base | DD | Destroyer | Destroyer | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 7500000 | 300 | 1 | 45 knots planned, -30% reliability, PAPER |
| 4719 | Japanese | Type 1953 | Type 1953 | Base | DD | Destroyer | Destroyer | 1953 | 1953 | 1953 | 5000 | 5750 | 35 | 28.0 | 5000 | 3500000 | 270 | 0 | Modern sensors, +25% detection |
| 4720 | Japanese | Harukaze | Harukaze | Base | DD | Destroyer | Destroyer | 1956 | 1956 | 1956 | 5000 | 5750 | 35 | 28.0 | 5000 | 4000000 | 285 | 0 | Modern ASW, +40% submarine detection |
| 4721 | Japanese | Ayanami 1957 | Ayanami 1957 | Base | DD | Destroyer | Destroyer | 1957 | 1957 | 1957 | 5000 | 5750 | 35 | 28.0 | 5000 | 4500000 | 300 | 0 | Modern radar/sonar, +50% detection |
| 4722 | Japanese | Murasame | Murasame | Base | DD | Destroyer | Destroyer | 1958 | 1958 | 1958 | 5000 | 5750 | 35 | 28.0 | 5000 | 5000000 | 315 | 0 | Helicopter ops, +60% ASW |
| 4723 | Japanese | Akizuki 1959 | Akizuki 1959 | Base | DD | Destroyer | Destroyer | 1959 | 1959 | 1959 | 5000 | 5750 | 35 | 28.0 | 5000 | 5500000 | 330 | 0 | AA + ASW balance, +45% versatility |
| 4724 | Japanese | Yamagumo | Yamagumo | Base | DD | Destroyer | Destroyer | 1960 | 1960 | 1960 | 5000 | 5750 | 35 | 28.0 | 5000 | 6000000 | 345 | 0 | ASROC system, +70% ASW capability |
| 4725 | Japanese | Momo 1916 Kai | Momo 1916 Kai | Base | DD | Destroyer | Destroyer | 1925 | 1925 | 1925 | 2000 | 2300 | 35 | 28.0 | 5000 | 500000 | 75 | 0 | +20% capability over original |
| 4726 | Japanese | Momi Kai | Momi Kai | Base | DD | Destroyer | Destroyer | 1930 | 1930 | 1930 | 2000 | 2300 | 35 | 28.0 | 5000 | 700000 | 105 | 0 | +25% combat capability |
| 4727 | Japanese | Minekaze Kai | Minekaze Kai | Base | DD | Destroyer | Destroyer | 1935 | 1935 | 1935 | 2000 | 2300 | 35 | 28.0 | 5000 | 1000000 | 135 | 0 | Maintains 39 knots, +30% systems |
| 4728 | Japanese | Kamikaze Kai | Kamikaze Kai | Base | DD | Destroyer | Destroyer | 1936 | 1936 | 1936 | 2000 | 2300 | 35 | 28.0 | 5000 | 1200000 | 165 | 0 | +35% capability, improved AA |
| 4729 | Japanese | Mutsuki Kai | Mutsuki Kai | Base | DD | Destroyer | Destroyer | 1940 | 1940 | 1940 | 2000 | 2300 | 35 | 28.0 | 5000 | 1500000 | 180 | 0 | Type 93 Long Lance, +50% torpedo power |
| 4730 | Japanese | Fubuki Kai | Fubuki Kai | Base | DD | Destroyer | Destroyer | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 1800000 | 210 | 0 | Radar systems, +40% detection |
| 4731 | Japanese | Ayanami Kai | Ayanami Kai | Base | DD | Destroyer | Destroyer | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 2000000 | 225 | 0 | +45% overall capability |
| 4732 | Japanese | Akatsuki Kai | Akatsuki Kai | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 2100000 | 240 | 0 | +50% capability, peak Special Type |
| 4733 | Japanese | Hatsuharu Kai | Hatsuharu Kai | Base | DD | Destroyer | Destroyer | 1942 | 1942 | 1942 | 2000 | 2300 | 35 | 28.0 | 5000 | 2200000 | 225 | 0 | Stability issues resolved, +40% reliability |
| 4734 | Japanese | Shiratsuyu Kai | Shiratsuyu Kai | Base | DD | Destroyer | Destroyer | 1943 | 1943 | 1943 | 2000 | 2300 | 35 | 28.0 | 5000 | 2400000 | 255 | 0 | +50% overall performance |
| 4735 | Japanese | Asashio Kai | Asashio Kai | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 2600000 | 270 | 0 | +60% combat capability |
| 4736 | Japanese | Kagero Kai | Kagero Kai | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 3200000 | 285 | 0 | +55% capability, modern systems |
| 4737 | Japanese | Yūgumo Kai | Yūgumo Kai | Base | DD | Destroyer | Destroyer | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 3400000 | 300 | 0 | +65% capability, peak performance |
| 4738 | Japanese | Akizuki Kai | Akizuki Kai | Base | DD | Destroyer | Destroyer | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 4200000 | 315 | 0 | +90% AA capability, maximum |
| 4739 | Japanese | Shimakaze Kai | Shimakaze Kai | Base | DD | Destroyer | Destroyer | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 5500000 | 285 | 0 | +120% capability, LEGENDARY performance |
| 4740 | Japanese | Experimental DD-1 | Experimental DD-1 | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 4500000 | 270 | 1 | Advanced systems, -25% reliability, PAPER |
| 4741 | Japanese | Experimental DD-2 | Experimental DD-2 | Base | DD | Destroyer | Destroyer | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 4800000 | 285 | 1 | 42 knots, -30% reliability, PAPER |
| 4742 | Japanese | Super Akizuki | Super Akizuki | Base | DD | Destroyer | Destroyer | 1945 | 1945 | 1945 | 5000 | 5750 | 35 | 28.0 | 5000 | 5500000 | 330 | 1 | 10×3.9" guns, -25% reliability, PAPER |
| 4743 | Japanese | Hybrid DD | Hybrid DD | Base | DD | Destroyer | Destroyer | 1944 | 1944 | 1944 | 2000 | 2300 | 35 | 28.0 | 5000 | 6000000 | 300 | 1 | Submersible capability, -40% reliability, PAPER |
| 4744 | Japanese | Ultimate Type | Ultimate Type | Base | DD | Destroyer | Destroyer | 1970 | 1970 | 1970 | 5000 | 5750 | 35 | 28.0 | 5000 | 8000000 | 360 | 1 | Maximum everything, -35% reliability, PAPER |
| 4800 | Japanese | No. 6 Class | No. 6 Class | Base | SS | Submarine | Submarine | 1905 | 1905 | 1905 | 500 | 575 | 15 | 12.0 | 8000 | 0 | 60 | 0 | Basic submarine, FREE starting ship |
| 4801 | Japanese | L-1 Class | L-1 Class | Base | SS | Submarine | Submarine | 1918 | 1918 | 1918 | 500 | 575 | 15 | 12.0 | 8000 | 500000 | 90 | 0 | Basic fleet submarine |
| 4802 | Japanese | L-4 Class | L-4 Class | Base | SS | Submarine | Submarine | 1920 | 1920 | 1920 | 1500 | 1724 | 15 | 12.0 | 8000 | 800000 | 120 | 0 | Larger design, FREE starting ship |
| 4803 | Japanese | Kaidai Type I | Kaidai Type I | Base | SS | Submarine | Submarine | 1922 | 1922 | 1922 | 1500 | 1724 | 15 | 12.0 | 8000 | 1500000 | 150 | 0 | Ocean-going capability |
| 4804 | Japanese | Kaidai Type II | Kaidai Type II | Base | SS | Submarine | Submarine | 1925 | 1925 | 1925 | 1500 | 1724 | 15 | 12.0 | 8000 | 1800000 | 165 | 0 | +25% range |
| 4805 | Japanese | Kaidai Type III | Kaidai Type III | Base | SS | Submarine | Submarine | 1927 | 1927 | 1927 | 1500 | 1724 | 15 | 12.0 | 8000 | 2200000 | 180 | 0 | More torpedoes, +30% capability |
| 4806 | Japanese | Kaidai Type IV | Kaidai Type IV | Base | SS | Submarine | Submarine | 1929 | 1929 | 1929 | 1500 | 1724 | 15 | 12.0 | 8000 | 2500000 | 195 | 0 | 8 torpedo tubes, +40% firepower |
| 4807 | Japanese | Kaidai Type V | Kaidai Type V | Base | SS | Submarine | Submarine | 1932 | 1932 | 1932 | 1500 | 1724 | 15 | 12.0 | 8000 | 3000000 | 210 | 0 | Type 95 oxygen torpedoes, +50% torpedo power |
| 4808 | Japanese | Kaidai Type VI | Kaidai Type VI | Base | SS | Submarine | Submarine | 1934 | 1934 | 1934 | 1500 | 1724 | 15 | 12.0 | 8000 | 3500000 | 225 | 0 | +55% overall capability |
| 4809 | Japanese | Kaidai Type VII | Kaidai Type VII | Base | SS | Submarine | Submarine | 1937 | 1937 | 1937 | 1500 | 1724 | 15 | 12.0 | 8000 | 4000000 | 240 | 0 | +60% capability, peak Kaidai |
| 4810 | Japanese | Junsen Type I | Junsen Type I | Base | SS | Submarine | Cruiser Submarine | 1926 | 1926 | 1926 | 1500 | 1724 | 15 | 12.0 | 8000 | 3500000 | 180 | 0 | 1 aircraft, +40% reconnaissance |
| 4811 | Japanese | Junsen Type II | Junsen Type II | Base | SS | Submarine | Cruiser Submarine | 1932 | 1932 | 1932 | 1500 | 1724 | 15 | 12.0 | 8000 | 4500000 | 210 | 0 | +50% capability, 17 kts |
| 4812 | Japanese | Junsen Type III | Junsen Type III | Base | SS | Submarine | Cruiser Submarine | 1937 | 1937 | 1937 | 1500 | 1724 | 15 | 12.0 | 8000 | 5500000 | 240 | 0 | +60% capability, 8 tubes |
| 4813 | Japanese | Type A (I-9) | Type A (I-9) | Base | SS | Submarine | Fleet Submarine | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 6000000 | 270 | 0 | 23.5 knots, +65% capability |
| 4814 | Japanese | Type B (I-15) | Type B (I-15) | Base | SS | Submarine | Fleet Submarine | 1939 | 1939 | 1939 | 1500 | 1724 | 15 | 12.0 | 8000 | 6500000 | 285 | 0 | 17 torpedoes, +70% capability |
| 4815 | Japanese | Type C (I-16) | Type C (I-16) | Base | SS | Submarine | Fleet Submarine | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 5800000 | 270 | 0 | 23.6 knots, +65% speed |
| 4816 | Japanese | Type B Kai (I-54) | Type B Kai (I-54) | Base | SS | Submarine | Fleet Submarine | 1942 | 1942 | 1942 | 1500 | 1724 | 15 | 12.0 | 8000 | 7000000 | 300 | 0 | +75% capability, wartime |
| 4817 | Japanese | Type C Kai (I-52) | Type C Kai (I-52) | Base | SS | Submarine | Fleet Submarine | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 6800000 | 285 | 0 | +70% capability, enhanced |
| 4818 | Japanese | I-400 (Sen-Toku) | I-400 (Sen-Toku) | Base | SS | Submarine | Submarine Aircraft Carrier | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 25000000 | 360 | 0 | 3 aircraft, +100% capability, LARGEST UNTIL 1965, LEGENDARY |
| 4819 | Japanese | I-201 (Sen-Taka) | I-201 (Sen-Taka) | Base | SS | Submarine | High-Speed Submarine | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 18000000 | 300 | 0 | 19 knots submerged, +90% speed, REVOLUTIONARY |
| 4820 | Japanese | RO-33 Class (K6) | RO-33 Class (K6) | Base | SS | Submarine | Medium Submarine | 1935 | 1935 | 1935 | 1500 | 1724 | 15 | 12.0 | 8000 | 2500000 | 165 | 0 | Type 95 torpedoes, +45% capability |
| 4821 | Japanese | RO-35 Class (K7) | RO-35 Class (K7) | Base | SS | Submarine | Medium Submarine | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 3200000 | 195 | 0 | +50% endurance, improved |
| 4822 | Japanese | RO-100 Class | RO-100 Class | Base | SS | Submarine | Coastal Submarine | 1942 | 1942 | 1942 | 1500 | 1724 | 15 | 12.0 | 8000 | 3000000 | 180 | 0 | Simplified design, +40% production |
| 4823 | Japanese | Ko-Hyoteki (Type A) | Ko-Hyoteki (Type A) | Base | SS | Submarine | Midget Submarine | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 800000 | 90 | 0 | Pearl Harbor attack, +35% stealth |
| 4824 | Japanese | Kairyū (Type D) | Kairyū (Type D) | Base | SS | Submarine | Midget Submarine | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 1200000 | 120 | 0 | 600 built, +45% production |
| 4825 | Japanese | Oyashio (1960) | Oyashio (1960) | Base | SS | Submarine | Modern Submarine | 1960 | 1960 | 1960 | 3000 | 3449 | 20 | 16.0 | 8000 | 12000000 | 270 | 0 | Modern systems, +60% capability |
| 4826 | Japanese | Hayashio Class | Hayashio Class | Base | SS | Submarine | Modern Submarine | 1960 | 1960 | 1960 | 3000 | 3449 | 20 | 16.0 | 8000 | 15000000 | 300 | 0 | +70% capability, advanced systems |
| 4827 | Japanese | L-1 Kai | L-1 Kai | Base | SS | Submarine | Submarine | 1930 | 1930 | 1930 | 1500 | 1724 | 15 | 12.0 | 8000 | 400000 | 105 | 0 | +20% capability over original |
| 4828 | Japanese | L-4 Kai | L-4 Kai | Base | SS | Submarine | Submarine | 1935 | 1935 | 1935 | 1500 | 1724 | 15 | 12.0 | 8000 | 600000 | 135 | 0 | +25% capability, improved |
| 4829 | Japanese | Kaidai I Kai | Kaidai I Kai | Base | SS | Submarine | Submarine | 1935 | 1935 | 1935 | 1500 | 1724 | 15 | 12.0 | 8000 | 1200000 | 165 | 0 | Radar, +30% detection |
| 4830 | Japanese | Kaidai II Kai | Kaidai II Kai | Base | SS | Submarine | Submarine | 1938 | 1938 | 1938 | 1500 | 1724 | 15 | 12.0 | 8000 | 1500000 | 180 | 0 | Type 95 torpedoes, +40% power |
| 4831 | Japanese | Kaidai III Kai | Kaidai III Kai | Base | SS | Submarine | Submarine | 1940 | 1940 | 1940 | 1500 | 1724 | 15 | 12.0 | 8000 | 1800000 | 195 | 0 | +45% capability, radar |
| 4832 | Japanese | Junsen I Kai | Junsen I Kai | Base | SS | Submarine | Cruiser Submarine | 1940 | 1940 | 1940 | 1500 | 1724 | 15 | 12.0 | 8000 | 3000000 | 210 | 0 | +50% aircraft ops, radar |
| 4833 | Japanese | Type A Kai | Type A Kai | Base | SS | Submarine | Fleet Submarine | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 6500000 | 285 | 0 | +80% capability, maximum |
| 4834 | Japanese | Type B Kai II | Type B Kai II | Base | SS | Submarine | Fleet Submarine | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 7000000 | 300 | 0 | +85% capability, peak |
| 4835 | Japanese | RO-33 Kai | RO-33 Kai | Base | SS | Submarine | Medium Submarine | 1943 | 1943 | 1943 | 1500 | 1724 | 15 | 12.0 | 8000 | 2800000 | 180 | 0 | +50% capability, Type 95 |
| 4836 | Japanese | Sen-Toku II | Sen-Toku II | Base | SS | Submarine | Submarine Aircraft Carrier | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 30000000 | 390 | 1 | 4 aircraft, -25% reliability, PAPER |
| 4837 | Japanese | Super Sen-Taka | Super Sen-Taka | Base | SS | Submarine | High-Speed Submarine | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 22000000 | 330 | 1 | 25 knots planned, -30% reliability, PAPER |
| 4838 | Japanese | Type D Fleet | Type D Fleet | Base | SS | Submarine | Fleet Submarine | 1945 | 1945 | 1945 | 3000 | 3449 | 20 | 16.0 | 8000 | 10000000 | 270 | 1 | Simplified, -20% reliability, PAPER |
| 4839 | Japanese | Nuclear Submarine | Nuclear Submarine | Base | SS | Submarine | Nuclear Submarine | 1960 | 1960 | 1960 | 3000 | 3449 | 20 | 16.0 | 8000 | 50000000 | 420 | 1 | Never pursued, -35% reliability, PAPER |
| 4840 | Japanese | Hydrogen Peroxide Sub | Hydrogen Peroxide Sub | Base | SS | Submarine | Experimental Submarine | 1944 | 1944 | 1944 | 1500 | 1724 | 15 | 12.0 | 8000 | 16000000 | 300 | 1 | Experimental, -40% reliability, PAPER |
| 4841 | Japanese | Ultimate Sen-Toku | Ultimate Sen-Toku | Base | SS | Submarine | Ultimate Submarine | 1970 | 1970 | 1970 | 3000 | 3449 | 20 | 16.0 | 8000 | 75000000 | 480 | 1 | Maximum everything, -40% reliability, PAPER |
| 4100 | Japanese | Hōshō | Hōshō | Base | CV | Aircraft Carrier | Aircraft Carrier | 1922 | 1922 | 1922 | 25000 | 28749 | 30 | 24.0 | 12000 | 0 | 180 | 0 | World's first purpose-built carrier, +50% innovation, FREE, LEGENDARY |
| 4101 | Japanese | Ryūjō | Ryūjō | Base | CV | Aircraft Carrier | Light Carrier | 1931 | 1931 | 1931 | 30000 | 34500 | 30 | 24.0 | 12000 | 8000000 | 240 | 0 | Two-deck design, +40% aircraft, unusual |
| 4102 | Japanese | Akagi | Akagi | Base | CV | Aircraft Carrier | Fleet Carrier | 1925 | 1925 | 1925 | 25000 | 28749 | 30 | 24.0 | 12000 | 12000000 | 300 | 0 | Pearl Harbor strike, +80% capability, FREE, FAMOUS |
| 4103 | Japanese | Kaga | Kaga | Base | CV | Aircraft Carrier | Fleet Carrier | 1928 | 1928 | 1928 | 25000 | 28749 | 30 | 24.0 | 12000 | 13000000 | 315 | 0 | 90 aircraft, +85% capacity, most Japanese |
| 4104 | Japanese | Sōryū | Sōryū | Base | CV | Aircraft Carrier | Fleet Carrier | 1935 | 1935 | 1935 | 30000 | 34500 | 30 | 24.0 | 12000 | 15000000 | 330 | 0 | First pure design since Hōshō, +70% capability |
| 4105 | Japanese | Hiryū | Hiryū | Base | CV | Aircraft Carrier | Fleet Carrier | 1937 | 1937 | 1937 | 30000 | 34500 | 30 | 24.0 | 12000 | 16000000 | 345 | 0 | 90-150mm armor, +75% protection, starboard island |
| 4106 | Japanese | Shōkaku | Shōkaku | Base | CV | Aircraft Carrier | Fleet Carrier | 1939 | 1939 | 1939 | 30000 | 34500 | 30 | 24.0 | 12000 | 20000000 | 360 | 0 | Best in world 1941, +100% capability, LEGENDARY |
| 4107 | Japanese | Zuikaku | Zuikaku | Base | CV | Aircraft Carrier | Fleet Carrier | 1939 | 1939 | 1939 | 30000 | 34500 | 30 | 24.0 | 12000 | 21000000 | 375 | 0 | Last sunk, +105% capability, LEGENDARY |
| 4108 | Japanese | Taihō | Taihō | Base | CV | Aircraft Carrier | Armored Carrier | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 25000000 | 390 | 0 | 75-80mm armor, +90% protection, first armored |
| 4109 | Japanese | Shinano | Shinano | Base | CV | Aircraft Carrier | Super Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 50000000 | 420 | 0 | Largest until 1954, +120% capability, LEGENDARY |
| 4110 | Japanese | Unryū | Unryū | Base | CV | Aircraft Carrier | Fleet Carrier | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 18000000 | 345 | 0 | Hiryū-based, +70% capability, wartime |
| 4111 | Japanese | Amagi | Amagi | Base | CV | Aircraft Carrier | Fleet Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 19000000 | 360 | 0 | +75% capability, improved |
| 4112 | Japanese | Katsuragi | Katsuragi | Base | CV | Aircraft Carrier | Fleet Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 20000000 | 375 | 0 | No aircraft/pilots, +65% if supplied |
| 4113 | Japanese | Zuihō | Zuihō | Base | CV | Aircraft Carrier | Light Carrier | 1935 | 1935 | 1935 | 30000 | 34500 | 30 | 24.0 | 12000 | 10000000 | 270 | 0 | Converted tender, +55% capability |
| 4114 | Japanese | Shōhō | Shōhō | Base | CV | Aircraft Carrier | Light Carrier | 1939 | 1939 | 1939 | 30000 | 34500 | 30 | 24.0 | 12000 | 11000000 | 285 | 0 | First carrier lost, +55% capability |
| 4115 | Japanese | Ryūhō | Ryūhō | Base | CV | Aircraft Carrier | Light Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 12000000 | 300 | 0 | +60% capability, submarine tender |
| 4116 | Japanese | Chitose | Chitose | Base | CV | Aircraft Carrier | Light Carrier | 1936 | 1936 | 1936 | 30000 | 34500 | 30 | 24.0 | 12000 | 11500000 | 285 | 0 | Converted seaplane tender, +55% |
| 4117 | Japanese | Chiyoda | Chiyoda | Base | CV | Aircraft Carrier | Light Carrier | 1937 | 1937 | 1937 | 30000 | 34500 | 30 | 24.0 | 12000 | 11800000 | 300 | 0 | Converted tender, +58% capability |
| 4118 | Japanese | Taiyō | Taiyō | Base | CV | Aircraft Carrier | Escort Carrier | 1940 | 1940 | 1940 | 35000 | 40250 | 33 | 26.4 | 12000 | 6000000 | 210 | 0 | Converted liner, +45% capability |
| 4119 | Japanese | Un'yō | Un'yō | Base | CV | Aircraft Carrier | Escort Carrier | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 6500000 | 225 | 0 | Converted liner, +47% capability |
| 4120 | Japanese | Chūyō | Chūyō | Base | CV | Aircraft Carrier | Escort Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 7000000 | 240 | 0 | Converted liner, +50% aircraft |
| 4121 | Japanese | Shin'yō | Shin'yō | Base | CV | Aircraft Carrier | Escort Carrier | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 6200000 | 220 | 0 | Captured German liner, +50% |
| 4122 | Japanese | Kaiyō | Kaiyō | Base | CV | Aircraft Carrier | Escort Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 7500000 | 255 | 0 | Improved design, +52% capability |
| 4123 | Japanese | Shimane Maru | Shimane Maru | Base | CV | Aircraft Carrier | Escort Carrier | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 6800000 | 230 | 0 | Simplified emergency, +48% |
| 4124 | Japanese | Theoretical 1955 | Theoretical 1955 | Base | CV | Aircraft Carrier | Carrier | 1955 | 1955 | 1955 | 45000 | 51749 | 33 | 26.4 | 12000 | 25000000 | 360 | 0 | Never pursued, -20% reliability |
| 4125 | Japanese | Helicopter Carrier | Helicopter Carrier | Base | CV | Aircraft Carrier | Helicopter Carrier | 1960 | 1960 | 1960 | 90000 | 103499 | 33 | 26.4 | 12000 | 30000000 | 390 | 0 | ASW focus, +65% ASW capability |
| 4126 | Japanese | Hōshō Kai | Hōshō Kai | Base | CV | Aircraft Carrier | Aircraft Carrier | 1935 | 1935 | 1935 | 30000 | 34500 | 30 | 24.0 | 12000 | 4000000 | 195 | 0 | +30% capability over original |
| 4127 | Japanese | Akagi Kai | Akagi Kai | Base | CV | Aircraft Carrier | Fleet Carrier | 1935 | 1935 | 1935 | 30000 | 34500 | 30 | 24.0 | 12000 | 10000000 | 315 | 0 | Single deck, island, +100% capability |
| 4128 | Japanese | Kaga Kai | Kaga Kai | Base | CV | Aircraft Carrier | Fleet Carrier | 1934 | 1934 | 1934 | 30000 | 34500 | 30 | 24.0 | 12000 | 11000000 | 330 | 0 | +105% capability, reconstructed |
| 4129 | Japanese | Ryūjō Kai | Ryūjō Kai | Base | CV | Aircraft Carrier | Light Carrier | 1934 | 1934 | 1934 | 30000 | 34500 | 30 | 24.0 | 12000 | 7000000 | 255 | 0 | Hull reinforced, +40% stability |
| 4130 | Japanese | Sōryū Kai | Sōryū Kai | Base | CV | Aircraft Carrier | Fleet Carrier | 1941 | 1941 | 1941 | 35000 | 40250 | 33 | 26.4 | 12000 | 14000000 | 345 | 0 | Radar, +50% capability |
| 4131 | Japanese | Hiryū Kai | Hiryū Kai | Base | CV | Aircraft Carrier | Fleet Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 15000000 | 360 | 0 | +90% capability, maximum |
| 4132 | Japanese | Shōkaku Kai | Shōkaku Kai | Base | CV | Aircraft Carrier | Fleet Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 19000000 | 375 | 0 | +110% capability, enhanced |
| 4133 | Japanese | Zuikaku Kai | Zuikaku Kai | Base | CV | Aircraft Carrier | Fleet Carrier | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 20000000 | 390 | 0 | +120% capability, peak, ULTIMATE |
| 4134 | Japanese | Zuihō Kai | Zuihō Kai | Base | CV | Aircraft Carrier | Light Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 11000000 | 300 | 0 | +70% capability, improved |
| 4135 | Japanese | Chitose Kai | Chitose Kai | Base | CV | Aircraft Carrier | Light Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 12000000 | 315 | 0 | +75% capability, better systems |
| 4136 | Japanese | Kasagi (Unryū IV) | Kasagi (Unryū IV) | Base | CV | Aircraft Carrier | Fleet Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 22000000 | 390 | 1 | Launched, never completed, -25% reliability, PAPER |
| 4137 | Japanese | Aso (Unryū V) | Aso (Unryū V) | Base | CV | Aircraft Carrier | Fleet Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 23000000 | 405 | 1 | 85% complete, -30% reliability, PAPER |
| 4138 | Japanese | Ikoma (Unryū VI) | Ikoma (Unryū VI) | Base | CV | Aircraft Carrier | Fleet Carrier | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 21000000 | 390 | 1 | Cancelled, -35% reliability, PAPER |
| 4139 | Japanese | G15 Project | G15 Project | Base | CV | Aircraft Carrier | Super Carrier | 1942 | 1942 | 1942 | 35000 | 40250 | 33 | 26.4 | 12000 | 40000000 | 420 | 1 | 50,000+ tons, -30% reliability, PAPER |
| 4140 | Japanese | Improved Taihō | Improved Taihō | Base | CV | Aircraft Carrier | Armored Carrier | 1943 | 1943 | 1943 | 35000 | 40250 | 33 | 26.4 | 12000 | 35000000 | 405 | 1 | Improved Taihō, -28% reliability, PAPER |
| 4141 | Japanese | Second Shinano | Second Shinano | Base | CV | Aircraft Carrier | Super Carrier | 1944 | 1944 | 1944 | 35000 | 40250 | 33 | 26.4 | 12000 | 60000000 | 450 | 1 | Second Yamato, -35% reliability, PAPER |
| 4142 | Japanese | Nuclear Carrier | Nuclear Carrier | Base | CV | Aircraft Carrier | Nuclear Carrier | 1960 | 1960 | 1960 | 90000 | 103499 | 33 | 26.4 | 12000 | 80000000 | 480 | 1 | Never pursued, -40% reliability, PAPER |
| 4143 | Japanese | Super Shinano | Super Shinano | Base | CV | Aircraft Carrier | Super Carrier | 1945 | 1945 | 1945 | 45000 | 51749 | 33 | 26.4 | 12000 | 70000000 | 465 | 1 | 80,000+ tons, -35% reliability, PAPER |
| 4144 | Japanese | Ultimate Design | Ultimate Design | Base | CV | Aircraft Carrier | Ultimate Carrier | 1970 | 1970 | 1970 | 90000 | 103499 | 33 | 26.4 | 12000 | 100000000 | 540 | 1 | Maximum everything, -40% reliability, PAPER |
| 1 | USA | BB | BB | Base | Starting | Starting | 1000 | 1000 | 1000 | 1000 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 2 | USA | BB | BB | Base | Coastal Defense | Coastal Defense | 1001 | 1004 | 1004 | 1004 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 3 | USA | BB | BB | Base | Blue Water | Blue Water | 1002 | 1005 | 1005 | 1005 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 4 | USA | BB | BB | Base | Main Line | Main Line | 1006 | 2040 | 2040 | 2040 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 5 | USA | BB | BB | Base | Modernization | Modernization | 1064 | 1080 | 1080 | 1080 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 6 | USA | BB | BB | Base | Paper Ship | Paper Ship | 2000 | 2040 | 2040 | 2040 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 7 | USA | BB/CB | BB/CB | Base | Alternative | Alternative | 1050 | 2031 | 2031 | 2031 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 8 | USA | BB | BB | Base | Experimental | Experimental | 1003 | 1003 | 1003 | 1003 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 9 | USA | CV | CV | Base | Starting | Starting | 5000 | 5000 | 5000 | 5000 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 10 | USA | CV | CV | Base | Main Line | Main Line | 5001 | 5011 | 5011 | 5011 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 11 | USA | CV | CV | Base | Modernization | Modernization | 5005 | 5006 | 5006 | 5006 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 12 | USA | CL | CL | Base | Starting | Starting | 6000 | 6001 | 6001 | 6001 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 13 | USA | CA/CAG | CA/CAG | Base | Heavy Main Line | Heavy Main Line | 6002 | 6016 | 6016 | 6016 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 14 | USA | CL/CLG | CL/CLG | Base | Light Main Line | Light Main Line | 6004 | 6017 | 6017 | 6017 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 15 | USA | CLAA | CLAA | Base | AA Specialist | AA Specialist | 6006 | 6015 | 6015 | 6015 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 16 | USA | CG | CG | Base | Guided Missile | Guided Missile | 6024 | 6039 | 6039 | 6039 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 17 | USA | CGN | CGN | Base | Nuclear | Nuclear | 6023 | 6030 | 6030 | 6030 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 18 | USA | CAG/CLG | CAG/CLG | Base | Conversion | Conversion | 6018 | 6028 | 6028 | 6028 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 19 | USA | CG | CG | Base | Modernization | Modernization | 6031 | 6032 | 6032 | 6032 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 20 | USA | CGN | CGN | Base | Nuclear Modernization | Nuclear Modernization | 6036 | 6036 | 6036 | 6036 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 21 | USA | CGN/CG | CGN/CG | Base | Paper Ship | Paper Ship | 6037 | 6040 | 6040 | 6040 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 22 | USA | DL | DL | Base | Alternative | Alternative | 6021 | 6021 | 6021 | 6021 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 23 | USA | DD | DD | Base | Starting | Starting | 7000 | 7001 | 7001 | 7001 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 24 | USA | DD | DD | Base | Pre-WWI | Pre-WWI | 7002 | 7004 | 7004 | 7004 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 25 | USA | DD | DD | Base | Four-Stacker | Four-Stacker | 7005 | 7007 | 7007 | 7007 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 26 | USA | DD | DD | Base | Interwar | Interwar | 7009 | 7013 | 7013 | 7013 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 27 | USA | DD | DD | Base | Pre-WWII | Pre-WWII | 7014 | 7018 | 7018 | 7018 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 28 | USA | DD | DD | Base | WWII Main Line | WWII Main Line | 7019 | 7022 | 7022 | 7022 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 29 | USA | DD | DD | Base | Modernization | Modernization | 7020 | 7023 | 7023 | 7023 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 30 | USA | DD/DDR/APD | DD/DDR/APD | Base | Alternative | Alternative | 7008 | 7024 | 7024 | 7024 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 31 | USA | DD/DDG/DL | DD/DDG/DL | Base | Post-War/Missile | Post-War/Missile | 7025 | 7030 | 7030 | 7030 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 32 | USA | DD/DDG | DD/DDG | Base | Gas Turbine | Gas Turbine | 7031 | 7033 | 7033 | 7033 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 33 | USA | DDG | DDG | Base | Aegis Main Line | Aegis Main Line | 7034 | 7037 | 7037 | 7037 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 34 | USA | DDG | DDG | Base | Stealth/Future | Stealth/Future | 7038 | 7040 | 7040 | 7040 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 35 | USA | SS | SS | Base | Starting | Starting | 8000 | 8001 | 8001 | 8001 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 36 | USA | SS | SS | Base | Coastal | Coastal | 8002 | 8004 | 8004 | 8004 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 37 | USA | SS | SS | Base | Fleet Diesel | Fleet Diesel | 8005 | 8012 | 8012 | 8012 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 38 | USA | SS | SS | Base | WWII Main Line | WWII Main Line | 8013 | 8019 | 8019 | 8019 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 39 | USA | SS | SS | Base | Modernization | Modernization | 8020 | 8021 | 8021 | 8021 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 40 | USA | SSN | SSN | Base | Nuclear Attack | Nuclear Attack | 8022 | 8037 | 8037 | 8037 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 41 | USA | SSBN | SSBN | Base | Ballistic Missile | Ballistic Missile | 8025 | 8038 | 8038 | 8038 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 42 | USA | SS/SSN/SSGN/SST | SS/SSN/SSGN/SST | Base | Alternative | Alternative | 8009 | 8035 | 8035 | 8035 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 1 | USA | BB | BB | Base | Coastal Defense | Coastal Defense | 1001 | 1007 | 1007 | 1007 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 2 | USA | BB | BB | Base | Blue Water | Blue Water | 1002 | 1008 | 1008 | 1008 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 3 | USA | BB | BB | Base | Main Line | Main Line | 1007 | 0 | 0 | 0 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 1001 | USA | Indiana-class | Indiana-class | Base | BB | Battleship | Pre-Dreadnought | 1890 | 1890 | 1890 | 12000 | 13799 | 18 | 14.4 | 15000 | 3020000 | 36 | 0 | +20% armor, -2 speed |
| 1002 | USA | Iowa-class | Iowa-class | Base | BB | Battleship | Pre-Dreadnought | 1890 | 1890 | 1890 | 12000 | 13799 | 18 | 14.4 | 15000 | 3010000 | 30 | 0 | +10% range, +2 speed |
| 1003 | USA | Kearsarge-class | Kearsarge-class | Base | BB | Battleship | Pre-Dreadnought | 1898 | 1898 | 1898 | 12000 | 13799 | 18 | 14.4 | 15000 | 3760000 | 36 | 0 | +15% firepower, Blast interference penalty |
| 1007 | USA | Illinois-class | Illinois-class | Base | BB | Battleship | Pre-Dreadnought | 1901 | 1901 | 1901 | 12000 | 13799 | 18 | 14.4 | 15000 | 4200000 | 36 | 0 | Balanced stats |
| 1008 | USA | Maine-class | Maine-class | Base | BB | Battleship | Pre-Dreadnought | 1902 | 1902 | 1902 | 12000 | 13799 | 18 | 14.4 | 15000 | 4300000 | 36 | 0 | +15% operational range |
| 1010 | USA | Connecticut-class | Connecticut-class | Base | BB | Battleship | Pre-Dreadnought | 1905 | 1905 | 1905 | 12000 | 13799 | 18 | 14.4 | 15000 | 5000000 | 42 | 0 | Great White Fleet participant |
| 1020 | USA | South Carolina-class | South Carolina-class | Base | BB | Battleship | Dreadnought | 1908 | 1908 | 1908 | 20000 | 23000 | 21 | 16.8 | 15000 | 6000000 | 48 | 0 | Superfiring turrets |
| 1 | USA | BB | BB | Base | Coastal Defense | Coastal Defense | 1001 | 1007 | 1007 | 1007 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 2 | USA | BB | BB | Base | Blue Water | Blue Water | 1002 | 1008 | 1008 | 1008 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
| 3 | USA | BB | BB | Base | Main Line | Main Line | 1007 | 0 | 0 | 0 | 10000 | 11500 | 25 | 20.0 | 10000 | 0 | 0 | 0 |  |
---

## Database Status

**Current Status**: ✅ **POPULATED** - 974 total entries (121 detailed USA cruisers + 853 basic entries from research tree)
**Current Count**: 974 ships (USA: 371, British: 206, German: 179, Japanese: 218)
**Target Count**: 800-1,200 ships across all eras and nations ✅ **MET**

**Coverage Goals**:
- **Battleships**: All WWII+ battleships (USA, UK, Germany, Japan, France, Italy, USSR)
- **Carriers**: All fleet and light carriers WWII+, modern carriers
- **Cruisers**: Major classes WWII+
- **Destroyers**: Representative classes (too many to capture all)
- **Submarines**: Major classes and notable boats

**Integration with Other Databases**:
- Links to **Naval Guns Database** via Gun_ID
- Links to **Torpedoes Database** via Torpedo_ID
- Links to **Missiles Database** via Missile_ID
- Links to **Naval Aircraft Database** via Aircraft_ID
- Creates complete weapon system integration

---

**Last Updated**: October 10, 2025
**Ready for Data Entry**: ✅
