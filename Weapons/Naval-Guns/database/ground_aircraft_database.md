# Ground-Based Military Aircraft Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 0 (ready for expansion)

---

## Database Contents

- [Aircraft Table](#aircraft-table) - Land-based military aircraft
- [Armament Table](#armament-table) - Aircraft weapons loadouts
- [Performance Table](#performance-table) - Detailed performance specifications
- [Base Operations Table](#base-operations-table) - Runway requirements and operational data

---

<a name="aircraft-table"></a>
## Aircraft Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Aircraft_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation of origin |
| Designation | VARCHAR(100) | Official designation (e.g., "F-15C Eagle", "Bf 109G", "MiG-29") |
| Nickname | VARCHAR(100) | Common nickname or NATO reporting name |
| Manufacturer | VARCHAR(100) | Aircraft manufacturer |
| Type | VARCHAR(50) | Fighter, Bomber, Attack, Interceptor, Multi-role, etc. |
| Role | VARCHAR(200) | Primary mission (Air superiority, CAS, Strategic bombing, etc.) |
| Generation | VARCHAR(20) | Fighter generation (1st through 5th+) for jets |
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
| Stealth_Capable | TINYINT | 1 = stealth features, 0 = conventional |
| Supercruise_Capable | TINYINT | 1 = supersonic without afterburner, 0 = no |
| STOL_Capable | TINYINT | 1 = short takeoff and landing, 0 = conventional |
| Modded | TINYINT | 0 = historical, 1 = fictional/generated |
| Notes | TEXT | Operational history, variants, significant features |

**Total Entries**: 0 aircraft
**Planned Coverage**: 1914-2025 (WWI through 5th gen+)
**ID Allocation**:
- USA: 4000-4399 (WWI: 4000-4019, WWII: 4020-4099, Early Jet: 4100-4149, Vietnam: 4150-4199, Modern: 4200-4299, Fictional: 4300-4399)
- British: 4400-4549 (WWI: 4400-4419, WWII: 4420-4479, Jet: 4480-4529, Fictional: 4530-4549)
- German: 4550-4699 (WWI: 4550-4569, WWII: 4570-4629, Post-war: 4630-4679, Fictional: 4680-4699)
- Soviet/Russian: 4700-4899 (WWII: 4700-4749, Cold War: 4750-4849, Modern: 4850-4879, Fictional: 4880-4899)
- Japanese: 4900-4999 (WWII: 4900-4959, Post-war: 4960-4979, Fictional: 4980-4999)
- French: 5000-5099
- Italian: 5100-5149
- Chinese: 5150-5249
- Israeli: 5250-5299
- Other Nations: 5300-5399
- Multi-national: 5400-5499

| Aircraft_ID | Country | Designation | Nickname | Manufacturer | Type | Role | Generation | Year_Introduced | Year_Retired | Crew | Length_FT | Wingspan_FT | Height_FT | Wing_Area_SQFT | Empty_Weight_LBS | Max_Takeoff_Weight_LBS | Engine_Type | Engine_Count | Max_Speed_MPH | Max_Speed_MACH | Cruise_Speed_MPH | Range_NM | Combat_Radius_NM | Service_Ceiling_FT | Rate_Of_Climb_FPM | Wing_Loading_PSF | Thrust_To_Weight | Stealth_Capable | Supercruise_Capable | STOL_Capable | Modded | Notes |
|-------------|---------|-------------|----------|--------------|------|------|------------|-----------------|--------------|------|-----------|-------------|-----------|----------------|------------------|------------------------|-------------|--------------|---------------|----------------|------------------|----------|------------------|-------------------|-------------------|------------------|------------------|-----------------|---------------------|--------------|--------|-------|
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

**Example Entries** (for reference - not yet in database):

### USA WWI Aircraft
- **Sopwith Camel** (US-built) - Highly maneuverable fighter
- **SPAD XIII** (US-built) - Sturdy fighter used by US squadrons
- **DH-4** - Liberty Plane, US-built bomber

### USA WWII Aircraft
- **P-51 Mustang** - Long-range escort fighter, legendary performance
- **P-47 Thunderbolt** - Heavy fighter-bomber, "Jug"
- **P-38 Lightning** - Twin-boom fighter, high altitude
- **F4U Corsair** (land-based) - Also used by Marines from land bases
- **B-17 Flying Fortress** - Heavy bomber, daylight precision
- **B-24 Liberator** - Heavy bomber, most-produced US aircraft
- **B-29 Superfortress** - Strategic bomber, atomic bomber
- **P-40 Warhawk** - Early war fighter, Flying Tigers
- **P-39 Airacobra** - Mid-engine fighter

### USA Jet Age (1945-1990)
- **F-86 Sabre** - Korean War jet fighter
- **F-100 Super Sabre** - First supersonic fighter
- **F-104 Starfighter** - Mach 2 interceptor
- **F-105 Thunderchief** - Strike fighter, Vietnam workhorse
- **F-4 Phantom II** - Legendary multi-role (also naval)
- **F-111 Aardvark** - Variable-sweep bomber
- **F-15 Eagle** - Air superiority fighter, undefeated
- **F-16 Fighting Falcon** - Lightweight multi-role
- **A-10 Thunderbolt II** - Close air support, tank killer
- **B-52 Stratofortress** - Strategic bomber, still in service

### USA Modern Era (1990+)
- **F-22 Raptor** - 5th gen stealth air superiority
- **F-35A Lightning II** - 5th gen multi-role stealth
- **F-15EX Eagle II** - Modernized F-15
- **B-2 Spirit** - Stealth strategic bomber
- **B-1B Lancer** - Supersonic strategic bomber
- **A-10C Thunderbolt II** - Upgraded Warthog

### British WWI Aircraft
- **Sopwith Camel** - Most successful WWI fighter
- **Sopwith Pup** - Agile fighter
- **SE.5a** - Sturdy fighter
- **Bristol F.2 Fighter** - Two-seat fighter

### British WWII Aircraft
- **Supermarine Spitfire** - Iconic fighter, Battle of Britain
- **Hawker Hurricane** - Workhorse fighter
- **Avro Lancaster** - Heavy bomber
- **De Havilland Mosquito** - "Wooden Wonder" multi-role
- **Hawker Typhoon** - Ground attack fighter
- **Hawker Tempest** - Fast fighter, V-1 hunter

### British Jet Era
- **Gloster Meteor** - First Allied operational jet
- **English Electric Lightning** - Supersonic interceptor
- **Hawker Hunter** - Transonic fighter
- **Harrier GR.3/GR.7** - V/STOL ground attack
- **Tornado GR.1/GR.4** - Variable-sweep strike
- **Typhoon FGR.4** - Modern multi-role, Eurofighter

### German WWI Aircraft
- **Fokker Dr.I** - Triplane, Red Baron
- **Fokker D.VII** - Best WWI fighter
- **Albatros D.V** - Scout fighter
- **Pfalz D.III** - Fighter

### German WWII Aircraft
- **Bf 109** - Most-produced fighter ever
- **Fw 190** - Excellent fighter-bomber
- **Me 262** - First operational jet fighter
- **He 111** - Medium bomber
- **Ju 87 Stuka** - Dive bomber
- **Ju 88** - Versatile bomber
- **Me 163 Komet** - Rocket-powered interceptor
- **Me 410** - Heavy fighter

### German Post-War
- **Tornado IDS/ECR** - Panavia multi-role (German participation)
- **Typhoon** - Eurofighter (German participation)
- **F-4F Phantom II** - German-operated variant

### Soviet WWII Aircraft
- **Yak-3** - Lightweight fighter
- **Yak-9** - Most-produced Soviet fighter
- **La-5/La-7** - Radial-engine fighters
- **Il-2 Shturmovik** - Ground attack, most-produced military aircraft ever
- **Pe-2** - Dive bomber
- **Tu-2** - Medium bomber

### Soviet/Russian Jet Era
- **MiG-15** - Korean War jet fighter
- **MiG-17** - Improved MiG-15
- **MiG-21 Fishbed** - Most-produced supersonic fighter
- **MiG-23 Flogger** - Variable-sweep fighter
- **MiG-25 Foxbat** - Mach 3 interceptor
- **MiG-29 Fulcrum** - Modern multi-role
- **MiG-31 Foxhound** - Long-range interceptor
- **Su-7/Su-17 Fitter** - Ground attack
- **Su-24 Fencer** - Strike bomber
- **Su-25 Frogfoot** - Close air support
- **Su-27 Flanker** - Air superiority, highly maneuverable
- **Su-30/Su-35** - Multi-role Flanker variants
- **Tu-22M Backfire** - Strategic bomber

### Soviet/Russian Modern
- **Su-57 Felon** - 5th gen stealth fighter
- **Su-34 Fullback** - Strike fighter
- **MiG-35** - Advanced Fulcrum

### Japanese WWII Aircraft
- **A6M Zero** (land-based variants) - Also used from land bases
- **Ki-43 Oscar** - Army fighter
- **Ki-61 Tony** - Inline-engine fighter
- **Ki-84 Frank** - Late-war high-performance fighter
- **Ki-100** - Radial-engine variant of Tony
- **J2M Raiden (Jack)** - Interceptor
- **N1K Shiden (George)** - Land-based from floatplane design
- **G4M Betty** - Medium bomber
- **Ki-21 Sally** - Heavy bomber

### French Aircraft
- **Mirage III** - Delta-wing fighter
- **Mirage F1** - Multi-role fighter
- **Mirage 2000** - Modern delta-wing multi-role
- **Rafale** - Omni-role 4.5 gen (also naval variant)
- **Super Étendard** - Strike fighter

### Chinese Aircraft
- **J-7** (MiG-21 copy) - Chinese-built Fishbed
- **J-8** - Interceptor
- **J-10** - Modern multi-role
- **J-11** (Su-27 copy) - Chinese Flanker
- **J-16** - Strike fighter
- **J-20** - 5th gen stealth fighter
- **JH-7** - Fighter-bomber

### Israeli Aircraft
- **Kfir** - Mirage variant with US engine
- **Lavi** - Cancelled 4th gen fighter (prototype)
- Operated: F-15I, F-16I, F-35I (heavily modified US aircraft)

---

<a name="armament-table"></a>
## Armament Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Armament_ID | INT | Primary key |
| Aircraft_ID | INT | Foreign key to aircraft table |
| Loadout_Type | VARCHAR(50) | Air superiority, Strike, CAS, Interdiction, etc. |
| Internal_Guns | VARCHAR(200) | Fixed guns/cannons |
| Gun_Rounds | INT | Ammunition capacity |
| Internal_Bay_LBS | INT | Internal weapons bay capacity (stealth aircraft) |
| Hardpoint_Count | INT | Number of external hardpoints |
| Max_External_Load_LBS | INT | Maximum external stores weight |
| Max_Total_Ordnance_LBS | INT | Total weapons capacity |
| Typical_Loadout | TEXT | Typical weapon loadout description |
| AAM_Capacity | VARCHAR(100) | Air-to-air missile capacity |
| AGM_Capacity | VARCHAR(100) | Air-to-ground missile capacity |
| Bomb_Capacity | VARCHAR(100) | Bomb capacity (type and quantity) |
| Rocket_Capacity | VARCHAR(100) | Unguided rocket capacity |
| Guided_Munitions | VARCHAR(200) | Precision-guided munitions compatibility |
| Notes | TEXT | Special weapons, loadout variants |

| Armament_ID | Aircraft_ID | Loadout_Type | Internal_Guns | Gun_Rounds | Internal_Bay_LBS | Hardpoint_Count | Max_External_Load_LBS | Max_Total_Ordnance_LBS | Typical_Loadout | AAM_Capacity | AGM_Capacity | Bomb_Capacity | Rocket_Capacity | Guided_Munitions | Notes |
|-------------|-------------|--------------|---------------|------------|------------------|-----------------|----------------------|------------------------|-----------------|--------------|--------------|---------------|-----------------|------------------|-------|
| | | | | | | | | | | | | | | | |

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
| Max_G_Load_Positive | DECIMAL(4,2) | Maximum positive G-load rating |
| Max_G_Load_Negative | DECIMAL(4,2) | Maximum negative G-load rating |
| Stall_Speed_Knots | INT | Stall speed in knots |
| Landing_Speed_Knots | INT | Approach/landing speed |
| Takeoff_Distance_FT | INT | Takeoff roll distance |
| Landing_Distance_FT | INT | Landing roll distance |
| Ferry_Range_NM | INT | Maximum ferry range |
| Combat_Radius_NM | INT | Combat radius with typical loadout |
| Endurance_Hours | DECIMAL(4,2) | Loiter endurance |
| Turn_Rate_DEG_SEC | DECIMAL(5,2) | Sustained turn rate |
| Instantaneous_Turn_DEG_SEC | DECIMAL(5,2) | Instantaneous turn rate |
| Supercruise_Speed_MACH | DECIMAL(4,2) | Supercruise speed (if capable) |
| Combat_Ceiling_FT | INT | Combat ceiling |
| Acceleration_0_To_Mach_SEC | INT | Time to reach max speed |
| Notes | TEXT | Performance notes, conditions |

| Performance_ID | Aircraft_ID | Configuration | Weight_LBS | Max_G_Load_Positive | Max_G_Load_Negative | Stall_Speed_Knots | Landing_Speed_Knots | Takeoff_Distance_FT | Landing_Distance_FT | Ferry_Range_NM | Combat_Radius_NM | Endurance_Hours | Turn_Rate_DEG_SEC | Instantaneous_Turn_DEG_SEC | Supercruise_Speed_MACH | Combat_Ceiling_FT | Acceleration_0_To_Mach_SEC | Notes |
|----------------|-------------|---------------|------------|---------------------|---------------------|-------------------|---------------------|---------------------|---------------------|----------------|------------------|-----------------|-------------------|---------------------------|------------------------|-------------------|-----------------------------|-------|
| | | | | | | | | | | | | | | | | | | |

---

<a name="base-operations-table"></a>
## Base Operations Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Operations_ID | INT | Primary key |
| Aircraft_ID | INT | Foreign key to aircraft table |
| Min_Runway_Length_FT | INT | Minimum runway length required |
| Optimal_Runway_Length_FT | INT | Optimal runway length |
| Runway_Surface | VARCHAR(100) | Concrete, Asphalt, Grass, Unpaved |
| Hot_Refuel_Capable | TINYINT | 1 = can refuel with engine running, 0 = no |
| Forward_Base_Capable | TINYINT | 1 = can operate from austere fields, 0 = requires prepared base |
| Air_Refuel_Capable | TINYINT | 1 = aerial refueling capable, 0 = no |
| Turnaround_Time_MIN | INT | Typical ground turnaround time |
| Maintenance_Hours_Per_Flight_Hour | DECIMAL(5,2) | Maintenance ratio |
| Typical_Base_Type | VARCHAR(100) | Main operating base, Forward operating base, etc. |
| Ground_Support_Requirements | TEXT | Special ground equipment needed |
| Notes | TEXT | Operational considerations |

| Operations_ID | Aircraft_ID | Min_Runway_Length_FT | Optimal_Runway_Length_FT | Runway_Surface | Hot_Refuel_Capable | Forward_Base_Capable | Air_Refuel_Capable | Turnaround_Time_MIN | Maintenance_Hours_Per_Flight_Hour | Typical_Base_Type | Ground_Support_Requirements | Notes |
|---------------|-------------|----------------------|--------------------------|----------------|--------------------|-----------------------|--------------------|--------------------|-----------------------------------|-------------------|-----------------------------|-------|
| | | | | | | | | | | | | |

---

## Aircraft Categories

### By Era
1. **WWI (1914-1918)**
   - Biplanes, early monoplanes
   - Machine gun armament
   - Wood and fabric construction

2. **Interwar (1919-1938)**
   - Transition to all-metal construction
   - Monoplane fighters
   - Development of dive bombers

3. **WWII (1939-1945)**
   - Peak of piston-engine aviation
   - High-altitude fighters
   - Heavy strategic bombers
   - Introduction of jets (Me 262, Meteor)

4. **Early Jet Age (1945-1955)**
   - Subsonic and transonic jets
   - Korean War generation
   - First swept-wing jets

5. **Supersonic Era (1955-1970)**
   - Mach 2+ capability
   - Century Series (F-100 through F-106)
   - First Soviet supersonic fighters

6. **3rd Generation (1960-1980)**
   - Multi-role capability
   - Beyond visual range missiles
   - Vietnam War generation
   - F-4 Phantom, MiG-21, Mirage

7. **4th Generation (1975-2000)**
   - Fly-by-wire, relaxed stability
   - Look-down/shoot-down radar
   - All-aspect missiles
   - F-15, F-16, MiG-29, Su-27, Mirage 2000

8. **4.5 Generation (1990-2010)**
   - Advanced avionics, AESA radar
   - Precision strike
   - Network-centric warfare
   - F-15E, F/A-18E/F, Su-35, Rafale, Typhoon

9. **5th Generation (2005+)**
   - Stealth/low observability
   - Sensor fusion
   - Supercruise
   - F-22, F-35, Su-57, J-20

### By Type
1. **Fighter** - Air-to-air combat specialist
2. **Interceptor** - High-speed, high-altitude defense
3. **Multi-role/Fighter-Bomber** - Combined air-to-air and air-to-ground
4. **Attack/Strike** - Ground attack specialist
5. **Close Air Support (CAS)** - Direct support of ground troops
6. **Bomber** - Strategic/tactical bombing
7. **Reconnaissance** - Photo/electronic intelligence
8. **Electronic Warfare** - Jamming, SEAD/DEAD
9. **Transport** - Cargo and personnel
10. **Trainer** - Pilot training

### By Role
- **Air Superiority** - Dominating airspace (F-15C, Su-27)
- **Multi-role** - All missions (F-16, F/A-18, Rafale)
- **Strike** - Deep interdiction (F-111, Su-24, Tornado)
- **CAS** - Ground support (A-10, Su-25)
- **Strategic Bombing** - Long-range strikes (B-52, Tu-95)
- **SEAD/DEAD** - Suppression/Destruction of Enemy Air Defenses (F-16CJ, EA-18G)
- **Reconnaissance** - Intelligence gathering (SR-71, MiG-25R)

---

## Fighter Generations (Jets Only)

### 1st Generation (1945-1955)
- **Characteristics**: Subsonic/transonic, straight wings, gun armament
- **Examples**: F-80, MiG-15, Meteor, F-84, F-86

### 2nd Generation (1955-1960)
- **Characteristics**: Supersonic, swept wings, early missiles
- **Examples**: F-100, MiG-19, F-104, F-105

### 3rd Generation (1960-1970)
- **Characteristics**: Mach 2+, semi-active radar missiles, limited multi-role
- **Examples**: F-4, MiG-21, Mirage III, F-105

### 4th Generation (1970-1990)
- **Characteristics**: Fly-by-wire, beyond visual range, multi-role, high maneuverability
- **Examples**: F-15, F-16, F/A-18, MiG-29, Su-27, Mirage 2000, Tornado

### 4.5 Generation (1990-2010)
- **Characteristics**: AESA radar, advanced avionics, precision strike, partial stealth
- **Examples**: F-15E, F/A-18E/F, Su-35, Rafale, Typhoon, Gripen NG

### 5th Generation (2005+)
- **Characteristics**: Stealth, sensor fusion, supercruise, advanced networking
- **Examples**: F-22, F-35, Su-57, J-20, J-35

### 6th Generation (Future)
- **Characteristics**: Loyal wingman drones, AI assistance, directed energy weapons, hypersonic
- **Examples**: NGAD (USA), Tempest (UK), FCAS (France/Germany)

---

## Future Expansion Notes

### Priority WWI Aircraft
- **Fokker Dr.I, D.VII** (German)
- **Sopwith Camel, SE.5a** (British)
- **SPAD XIII** (French, used by USA)
- **Albatros D.V** (German)

### Priority WWII Aircraft (Essential 50)
- **USA**: P-51, P-47, P-38, F4U, B-17, B-24, B-29, P-40
- **UK**: Spitfire, Hurricane, Lancaster, Mosquito, Typhoon
- **Germany**: Bf 109, Fw 190, Me 262, Ju 87, He 111
- **USSR**: Yak-3, Yak-9, La-5/7, Il-2, Pe-2
- **Japan**: Zero, Ki-43, Ki-84, J2M, N1K

### Priority Jet Era (Essential 40)
- **USA**: F-86, F-4, F-15, F-16, A-10, B-52, F-111
- **USSR**: MiG-15, MiG-21, MiG-29, Su-27, Su-25
- **UK**: Lightning, Hunter, Harrier, Tornado, Typhoon
- **France**: Mirage III, Mirage 2000, Rafale

### Priority Modern (Essential 20)
- **USA**: F-22, F-35A, B-2, F-15EX
- **Russia**: Su-35, Su-57, MiG-35
- **China**: J-20, J-10, J-16
- **Europe**: Typhoon, Rafale, Gripen E

---

## Database Status

**Current Status**: Empty - Ready for population
**Target Count**: 800-1,200 aircraft across all eras and nations
**Priority**: WWII fighters, Cold War jets, modern 4th/5th gen

**Major Producers**:
1. USA: Largest air force, continuous innovation from WWI to present
2. USSR/Russia: Robust design philosophy, export success
3. UK: Early innovation, reduced post-Cold War
4. Germany: Dominant WWI/WWII, partner in modern programs
5. France: Independent capability, export success
6. China: Rapid modernization, indigenous designs
7. Japan: WWII prominence, limited post-war

---

**Last Updated**: October 10, 2025
**Ready for Data Entry**: ✅
