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
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

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

---

## Database Status

**Current Status**: Empty - Ready for population
**Target Count**: 800-1,200 ships across all eras and nations
**Priority**: WWII capital ships and carriers, modern surface combatants

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
