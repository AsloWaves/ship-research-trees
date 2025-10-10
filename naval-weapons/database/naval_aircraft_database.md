# Naval Aircraft Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 0 (ready for expansion)

---

## Database Contents

- [Aircraft Table](#aircraft-table) - Carrier-based and naval aircraft
- [Armament Table](#armament-table) - Aircraft weapons loadouts
- [Performance Table](#performance-table) - Detailed performance specifications
- [Carrier Compatibility Table](#carrier-compatibility-table) - Aircraft-carrier matching

---

<a name="aircraft-table"></a>
## Aircraft Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Aircraft_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation of origin |
| Designation | VARCHAR(100) | Official designation (e.g., "F/A-18E Super Hornet", "A6M Zero") |
| Nickname | VARCHAR(100) | Common nickname or Allied reporting name |
| Manufacturer | VARCHAR(100) | Aircraft manufacturer |
| Type | VARCHAR(50) | Fighter, Attack, Bomber, Torpedo, Dive Bomber, ASW, AEW, etc. |
| Role | VARCHAR(200) | Primary mission (Air superiority, Strike, ASW, Recon, etc.) |
| Year_Introduced | INT | Year entered service |
| Year_Retired | INT | Year retired from service (null if still active) |
| Crew | INT | Number of crew members |
| Length_FT | DECIMAL(5,2) | Overall length in feet |
| Wingspan_FT | DECIMAL(5,2) | Wingspan in feet (extended for variable sweep) |
| Height_FT | DECIMAL(5,2) | Overall height in feet |
| Wing_Area_SQFT | DECIMAL(7,2) | Wing area in square feet |
| Empty_Weight_LBS | INT | Empty weight in pounds |
| Max_Takeoff_Weight_LBS | INT | Maximum takeoff weight in pounds |
| Engine_Type | VARCHAR(200) | Engine model and type |
| Engine_Count | INT | Number of engines |
| Max_Speed_MPH | INT | Maximum speed in mph |
| Max_Speed_MACH | DECIMAL(4,2) | Maximum speed in Mach (if supersonic) |
| Cruise_Speed_MPH | INT | Typical cruise speed |
| Range_NM | INT | Ferry range in nautical miles |
| Combat_Radius_NM | INT | Combat radius in nautical miles |
| Service_Ceiling_FT | INT | Service ceiling in feet |
| Rate_Of_Climb_FPM | INT | Rate of climb in feet per minute |
| Wing_Loading_PSF | DECIMAL(6,2) | Wing loading in pounds per square foot |
| Thrust_To_Weight | DECIMAL(4,3) | Thrust-to-weight ratio |
| Carrier_Capable | TINYINT | 1 = carrier-capable, 0 = land-based naval |
| Catapult_Capable | TINYINT | 1 = requires catapult, 0 = STOVL/CATOBAR |
| Folding_Wings | TINYINT | 1 = wings fold for storage, 0 = fixed |
| Modded | TINYINT | 0 = historical, 1 = fictional/generated |
| Notes | TEXT | Operational history, variants, significant features |

**Total Entries**: 0 aircraft
**Planned Coverage**: 1910-2025 (WWI seaplanes through modern 5th-gen)
**ID Allocation**:
- USA: 3000-3299 (WWII: 3000-3099, Jet Era: 3100-3199, Modern: 3200-3249, Fictional: 3250-3299)
- British: 3300-3449 (WWII: 3300-3349, Jet: 3350-3399, Modern: 3400-3424, Fictional: 3425-3449)
- Japanese: 3450-3549 (WWII: 3450-3499, Post-war: 3500-3524, Fictional: 3525-3549)
- German: 3550-3599 (WWII: 3550-3579, Post-war: 3580-3589, Fictional: 3590-3599)
- Soviet/Russian: 3600-3699
- French: 3700-3749
- Italian: 3750-3799
- Chinese: 3800-3849
- Other: 3850-3899
- Multi-national: 3900-3999

| Aircraft_ID | Country | Designation | Nickname | Manufacturer | Type | Role | Year_Introduced | Year_Retired | Crew | Length_FT | Wingspan_FT | Height_FT | Wing_Area_SQFT | Empty_Weight_LBS | Max_Takeoff_Weight_LBS | Engine_Type | Engine_Count | Max_Speed_MPH | Max_Speed_MACH | Cruise_Speed_MPH | Range_NM | Combat_Radius_NM | Service_Ceiling_FT | Rate_Of_Climb_FPM | Wing_Loading_PSF | Thrust_To_Weight | Carrier_Capable | Catapult_Capable | Folding_Wings | Modded | Notes |
|-------------|---------|-------------|----------|--------------|------|------|-----------------|--------------|------|-----------|-------------|-----------|----------------|------------------|------------------------|-------------|--------------|---------------|----------------|------------------|----------|------------------|-------------------|-------------------|------------------|------------------|-----------------|------------------|---------------|--------|-------|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

**Example Entries** (for reference - not yet in database):

### USA WWII Naval Aircraft
- **F4F Wildcat** - Early war carrier fighter, Grumman
- **F6F Hellcat** - Most successful US carrier fighter
- **F4U Corsair** - Bent-wing fighter, Marine favorite
- **SBD Dauntless** - Dive bomber, Battle of Midway hero
- **TBF/TBM Avenger** - Torpedo bomber, largest production torpedo aircraft
- **PBY Catalina** - Long-range patrol flying boat

### USA Jet Era (1945-1990)
- **F9F Panther/Cougar** - First US carrier jet to see combat (Korea)
- **F-8 Crusader** - Last gunfighter, supersonic
- **F-4 Phantom II** - Legendary multi-role fighter
- **A-4 Skyhawk** - Lightweight attack, "Heinemann's Hot Rod"
- **A-6 Intruder** - All-weather attack
- **A-7 Corsair II** - Subsonic attack aircraft
- **F-14 Tomcat** - Variable-sweep fleet defense fighter
- **S-3 Viking** - Carrier-based ASW

### USA Modern Era (1990+)
- **F/A-18 Hornet (C/D)** - Multi-role workhorse
- **F/A-18E/F Super Hornet** - Enlarged, more capable Hornet
- **EA-18G Growler** - Electronic warfare variant
- **F-35C Lightning II** - 5th-gen stealth carrier fighter
- **E-2 Hawkeye** - Carrier AEW
- **MH-60 Seahawk** - Multi-role helicopter

### British Naval Aircraft
- **Fairey Swordfish** - Biplane torpedo bomber (sank Bismarck)
- **Fairey Fulmar** - Two-seat carrier fighter
- **Supermarine Seafire** - Navalised Spitfire
- **Fairey Firefly** - Strike fighter
- **Sea Fury** - Last piston-engine fighter
- **Sea Hawk** - Early jet fighter
- **Sea Vixen** - Twin-boom all-weather fighter
- **Buccaneer** - Low-level strike aircraft
- **Sea Harrier** - STOVL fighter (Falklands War)
- **F-35B Lightning II** - STOVL 5th-gen (current)

### Japanese WWII Naval Aircraft
- **A6M Zero** - Legendary carrier fighter, Allied codename "Zeke"
- **D3A Val** - Dive bomber
- **B5N Kate** - Torpedo bomber (Pearl Harbor)
- **D4Y Judy** - Fast dive bomber
- **B6N Jill** - Late-war torpedo bomber
- **J2M Jack** - Interceptor fighter
- **N1K George** - Land-based fighter from floatplane

### Soviet/Russian Naval Aircraft
- **MiG-29K Fulcrum** - Carrier-based multi-role
- **Su-33 Flanker-D** - Carrier-based air superiority
- **Yak-38 Forger** - VTOL fighter
- **Ka-27 Helix** - ASW helicopter

### French Naval Aircraft
- **Étendard IV** - Strike fighter
- **Super Étendard** - Modernized strike fighter (Exocet carrier)
- **Rafale M** - Omni-role carrier fighter

---

<a name="armament-table"></a>
## Armament Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Armament_ID | INT | Primary key |
| Aircraft_ID | INT | Foreign key to aircraft table |
| Loadout_Type | VARCHAR(50) | Air superiority, Strike, ASW, Ferry, etc. |
| Internal_Guns | VARCHAR(200) | Fixed guns/cannons |
| Gun_Rounds | INT | Ammunition capacity |
| Hardpoint_Count | INT | Number of external hardpoints |
| Max_External_Load_LBS | INT | Maximum external stores weight |
| Typical_Loadout | TEXT | Typical weapon loadout description |
| AAM_Capacity | VARCHAR(100) | Air-to-air missile capacity |
| ASM_Capacity | VARCHAR(100) | Air-to-surface missile capacity |
| Bomb_Capacity | VARCHAR(100) | Bomb capacity (type and quantity) |
| Torpedo_Capacity | INT | Number of torpedoes |
| Rocket_Capacity | VARCHAR(100) | Unguided rocket capacity |
| Notes | TEXT | Special weapons, loadout variants |

| Armament_ID | Aircraft_ID | Loadout_Type | Internal_Guns | Gun_Rounds | Hardpoint_Count | Max_External_Load_LBS | Typical_Loadout | AAM_Capacity | ASM_Capacity | Bomb_Capacity | Torpedo_Capacity | Rocket_Capacity | Notes |
|-------------|-------------|--------------|---------------|------------|-----------------|----------------------|-----------------|--------------|--------------|---------------|------------------|-----------------|-------|
| | | | | | | | | | | | | | |

---

<a name="performance-table"></a>
## Performance Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Performance_ID | INT | Primary key |
| Aircraft_ID | INT | Foreign key to aircraft table |
| Configuration | VARCHAR(100) | Clean, Combat, Max takeoff, Ferry |
| Weight_LBS | INT | Configuration weight |
| Max_G_Load | DECIMAL(4,2) | Maximum G-load rating |
| Stall_Speed_Knots | INT | Stall speed in knots |
| Landing_Speed_Knots | INT | Approach/landing speed |
| Takeoff_Distance_FT | INT | Takeoff roll distance |
| Landing_Distance_FT | INT | Landing roll distance |
| Ferry_Range_NM | INT | Maximum ferry range |
| Combat_Radius_NM | INT | Combat radius with typical loadout |
| Endurance_Hours | DECIMAL(4,2) | Loiter endurance |
| Turn_Rate_DEG_SEC | DECIMAL(5,2) | Sustained turn rate |
| Instantaneous_Turn_DEG_SEC | DECIMAL(5,2) | Instantaneous turn rate |
| Notes | TEXT | Performance notes, conditions |

| Performance_ID | Aircraft_ID | Configuration | Weight_LBS | Max_G_Load | Stall_Speed_Knots | Landing_Speed_Knots | Takeoff_Distance_FT | Landing_Distance_FT | Ferry_Range_NM | Combat_Radius_NM | Endurance_Hours | Turn_Rate_DEG_SEC | Instantaneous_Turn_DEG_SEC | Notes |
|----------------|-------------|---------------|------------|------------|-------------------|---------------------|---------------------|---------------------|----------------|------------------|-----------------|-------------------|---------------------------|-------|
| | | | | | | | | | | | | | | |

---

<a name="carrier-compatibility-table"></a>
## Carrier Compatibility Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Compatibility_ID | INT | Primary key |
| Aircraft_ID | INT | Foreign key to aircraft table |
| Carrier_Name | VARCHAR(100) | Aircraft carrier name or class |
| Carrier_Type | VARCHAR(50) | Fleet carrier, Light carrier, Escort carrier, LHA/LHD |
| Launch_Method | VARCHAR(50) | Catapult, Ski-jump, STOVL, CATOBAR, STOBAR |
| Recovery_Method | VARCHAR(50) | Arrested landing, STOVL vertical, Deck landing |
| Max_Aircraft_Aboard | INT | Maximum number of this type aboard |
| Typical_Squadron_Size | INT | Typical squadron size |
| Years_Operational | VARCHAR(50) | Years this combo was operational |
| Notes | TEXT | Special considerations, limitations |

| Compatibility_ID | Aircraft_ID | Carrier_Name | Carrier_Type | Launch_Method | Recovery_Method | Max_Aircraft_Aboard | Typical_Squadron_Size | Years_Operational | Notes |
|------------------|-------------|--------------|--------------|---------------|-----------------|---------------------|-----------------------|-------------------|-------|
| | | | | | | | | | |

---

## Aircraft Categories

### By Era
1. **WWI Era (1910-1918)**
   - Seaplanes, floatplanes, early shipboard aircraft
   - Sopwith Camel, Sopwith Pup (shipboard versions)

2. **Interwar (1919-1938)**
   - Early carrier fighters and torpedo bombers
   - Dive bomber development
   - US: F2F, F3F, TBD Devastator
   - UK: Fairey Flycatcher, Blackburn Ripon
   - Japan: A4N, B4Y

3. **WWII (1939-1945)**
   - Peak of piston-engine carrier aviation
   - USA: F4F, F6F, F4U, SBD, TBM
   - UK: Swordfish, Albacore, Barracuda, Seafire, Sea Fury
   - Japan: A6M, D3A, B5N, D4Y, B6N
   - Germany: Limited carrier aircraft (Graf Zeppelin)

4. **Early Jet Age (1945-1960)**
   - Transition to jets, straight-wing jets
   - USA: F9F, F2H, F7U, F3H
   - UK: Sea Hawk, Attacker, Sea Venom
   - Carrier modifications for jet operations

5. **Supersonic Era (1960-1980)**
   - Mach 2+ fighters, heavy attack aircraft
   - USA: F-4, F-8, A-4, A-6, A-7, F-14
   - UK: Sea Vixen, Buccaneer
   - France: Étendard, Super Étendard
   - USSR: Yak-38

6. **Modern Era (1980-2000)**
   - Multi-role fighters, advanced avionics
   - USA: F/A-18, A-6E, F-14D
   - UK: Sea Harrier FA.2
   - France: Super Étendard Modernisé
   - USSR/Russia: Su-33, MiG-29K

7. **Contemporary Era (2000+)**
   - 5th generation, network-centric, stealth
   - USA: F/A-18E/F, EA-18G, F-35C
   - UK: F-35B
   - France: Rafale M
   - Russia: Su-33 upgraded, MiG-29K/KUB
   - China: J-15, J-35

### By Type
1. **Fighter** - Air superiority, fleet defense
2. **Attack/Strike** - Ground attack, anti-ship
3. **Fighter-Bomber/Multi-role** - Combined capabilities
4. **Torpedo Bomber** - Anti-ship torpedoes (WWII)
5. **Dive Bomber** - Precision bombing (WWII)
6. **ASW (Anti-Submarine Warfare)** - Sub hunting
7. **AEW (Airborne Early Warning)** - Radar picket
8. **EW (Electronic Warfare)** - Jamming, SEAD
9. **Reconnaissance** - Photo/electronic recon
10. **Transport/COD** - Carrier Onboard Delivery
11. **Helicopter** - ASW, transport, SAR, attack

### By Launch/Recovery Method
- **CATOBAR** (Catapult Assisted Take-Off But Arrested Recovery) - US supercarriers, French CdG
- **STOBAR** (Short Take-Off But Arrested Recovery) - Russian, Indian, Chinese carriers with ski-jump
- **STOVL** (Short Take-Off Vertical Landing) - Harrier, F-35B on LHA/LHD
- **STOL** (Short Take-Off and Landing) - Some helicopters, E-2C
- **Conventional** (No catapult, arrested landing) - WWII carriers

---

## Future Expansion Notes

### Priority WWII Aircraft
- **USA**: F4F, F6F, F4U, SBD, TBF/TBM, TBD, PBY
- **UK**: Swordfish, Albacore, Fulmar, Firefly, Seafire, Sea Fury
- **Japan**: A6M, D3A, B5N, D4Y, B6N, A7M, J2M, N1K
- **Germany**: Bf 109T, Ju 87C (Graf Zeppelin aircraft)

### Priority Jet Era (1945-1980)
- **USA**: F9F, F2H, F3H, F-4, F-8, A-4, A-6, A-7, F-14, S-3
- **UK**: Sea Hawk, Sea Venom, Sea Vixen, Buccaneer, Sea Harrier
- **France**: Étendard IV, Super Étendard
- **USSR**: Yak-38

### Priority Modern (1980+)
- **USA**: F/A-18C/D, F/A-18E/F, EA-18G, F-35C, E-2D
- **UK**: Sea Harrier FA.2, F-35B
- **France**: Rafale M, Super Étendard Modernisé
- **Russia**: Su-33, MiG-29K/KUB
- **China**: J-15 Flanker, J-35
- **India**: Tejas Naval, MiG-29K (operated)

---

## Database Status

**Current Status**: Empty - Ready for population
**Target Count**: 500-800 aircraft across all eras and nations
**Priority**: WWII and modern carrier aircraft

**Major Producers**:
1. USA: Largest naval aviation force, continuous carrier operations since 1920s
2. UK: Pioneer of carrier aviation, reduced capability post-Cold War
3. Japan: Dominant WWII carrier force, limited post-war naval aviation
4. France: Independent carrier capability, Rafale M
5. Russia: Limited carrier operations, Su-33/MiG-29K
6. China: Rapidly expanding carrier aviation, J-15/J-35

---

**Last Updated**: October 10, 2025
**Ready for Data Entry**: ✅
