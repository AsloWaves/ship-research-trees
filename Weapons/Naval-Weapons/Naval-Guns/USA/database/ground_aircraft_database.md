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

**Total Entries**: 147 aircraft
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
| Node_ID | Nation | Designation | Year | Type | Wingspan_ft | Length_ft | Max_Weight_lbs | Empty_Weight_lbs | Max_Speed_kts | Cruise_Speed_kts | Service_Ceiling_ft | Engine_Type | Num_Engines | Crew | Combat_Radius_nm | Role | Is_Modded | Modded |
|---------|--------|-------------|------|------|-------------|-----------|----------------|------------------|---------------|------------------|-------------------|-------------|-------------|------|------------------|------|-----------|--------|
| 4000 | USA | P-38 Lightning | 1941 | Fighter | 52.0 | 59.8 | 8500 | 5100 | 310 | 217 | 35200 | Piston | 2 | 1 | 208 | Air superiority | 1 | 1 |
| 4001 | USA | P-38J Lightning | 1943 | Fighter | 52.0 | 59.8 | 9500 | 5700 | 330 | 230 | 35600 | Piston | 2 | 1 | 224 | Air superiority | 1 | 0 |
| 4002 | USA | P-47 Thunderbolt | 1942 | Fighter | 40.9 | 47.0 | 9000 | 5400 | 320 | 224 | 35400 | Piston | 1 | 1 | 216 | Air superiority | 1 | 0 |
| 4003 | USA | P-47D Thunderbolt | 1944 | Fighter | 40.9 | 47.0 | 10000 | 6000 | 340 | 237 | 35800 | Piston | 1 | 1 | 232 | Air superiority | 1 | 0 |
| 4004 | USA | P-51 Mustang | 1943 | Fighter | 37.0 | 42.5 | 9500 | 5700 | 437 | 305 | 35600 | Piston | 1 | 1 | 224 | Air superiority | 1 | 0 |
| 4010 | USA | P-80 Shooting Star | 1945 | Jet Fighter | 38.9 | 44.7 | 15000 | 9000 | 550 | 385 | 45000 | Turbojet | 1 | 1 | 240 | Air superiority | 1 | 0 |
| 4011 | USA | F-84 Thunderjet | 1947 | Jet Fighter | 36.5 | 42.0 | 15800 | 9480 | 590 | 413 | 45300 | Turbojet | 1 | 1 | 256 | Air superiority | 1 | 0 |
| 4012 | USA | F-86 Sabre | 1949 | Jet Fighter | 37.1 | 42.7 | 20357 | 12214 | 687 | 480 | 45600 | Turbojet | 1 | 1 | 272 | Air superiority | 1 | 0 |
| 4013 | USA | F-100 Super Sabre | 1954 | Jet Fighter | 37.1 | 42.7 | 34832 | 20899 | 864 | 604 | 46350 | Turbojet | 1 | 1 | 312 | Air superiority | 1 | 0 |
| 4014 | USA | F-104 Starfighter | 1958 | Interceptor | 21.9 | 24.1 | 38800 | 23280 | 1450 | 1014 | 49600 | Turbofan | 1 | 1 | 370 | Air defense, interception | 1 | 0 |
| 4015 | USA | F-105 Thunderchief | 1958 | Strike | 37.4 | 41.1 | 38800 | 23280 | 980 | 686 | 40000 | Turbofan | 1 | 1 | 400 | Ground attack, strike missions | 1 | 0 |
| 4016 | USA | F-111 Aardvark | 1967 | Strike | 37.9 | 41.6 | 44200 | 26520 | 1070 | 749 | 40000 | Turbofan | 1 | 1 | 400 | Ground attack, strike missions | 1 | 0 |
| 4020 | USA | F-4C Phantom II | 1963 | Multi-Role | 37.6 | 41.4 | 61800 | 37080 | 1030 | 721 | 50600 | Turbofan | 1 | 1 | 445 | Air-to-air and air-to-ground | 1 | 0 |
| 4021 | USA | F-4E Phantom II | 1967 | Multi-Role | 37.9 | 41.6 | 61800 | 37080 | 1070 | 749 | 51400 | Turbofan | 1 | 1 | 505 | Air-to-air and air-to-ground | 1 | 0 |
| 4022 | USA | F-5 Freedom Fighter | 1963 | Export Fighter | 41.9 | 48.2 | 19500 | 11700 | 530 | 371 | 39600 | Piston | 1 | 1 | 384 | Multi-purpose operations | 1 | 0 |
| 4023 | USA | F-5E Tiger II | 1972 | Export Fighter | 44.6 | 51.3 | 24000 | 14400 | 620 | 434 | 41400 | Piston | 1 | 1 | 456 | Multi-purpose operations | 1 | 0 |
| 4030 | USA | F-15A Eagle | 1976 | Air Superiority | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 2 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4031 | USA | F-15C Eagle | 1979 | Air Superiority | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 2 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4032 | USA | F-15E Strike Eagle | 1988 | Multi-Role | 42.8 | 47.1 | 81000 | 48600 | 1280 | 896 | 55600 | Turbofan | 2 | 2 | 1100 | Air-to-air and air-to-ground | 1 | 0 |
| 4033 | USA | F-15EX Eagle II | 2021 | Multi-Role | 42.8 | 47.1 | 81000 | 48600 | 1610 | 1127 | 62200 | Turbofan | 2 | 2 | 1100 | Air-to-air and air-to-ground | 1 | 0 |
| 4040 | USA | F-16A Fighting Falcon | 1978 | Multi-Role | 32.8 | 36.1 | 42300 | 25380 | 1320 | 923 | 53600 | Turbofan | 1 | 1 | 340 | Air-to-air and air-to-ground | 1 | 0 |
| 4041 | USA | F-16C Block 30 | 1984 | Multi-Role | 32.8 | 36.1 | 42300 | 25380 | 1320 | 923 | 54800 | Turbofan | 1 | 1 | 340 | Air-to-air and air-to-ground | 1 | 0 |
| 4042 | USA | F-16C Block 52 | 1991 | Multi-Role | 32.8 | 36.1 | 42300 | 25380 | 1320 | 923 | 56200 | Turbofan | 1 | 1 | 340 | Air-to-air and air-to-ground | 1 | 0 |
| 4043 | USA | F-16V Viper | 2015 | Multi-Role | 32.8 | 36.1 | 42300 | 25380 | 1320 | 923 | 61000 | Turbofan | 1 | 1 | 340 | Air-to-air and air-to-ground | 1 | 0 |
| 4050 | USA | F-22A Raptor | 2005 | Stealth Fighter | 44.5 | 64.5 | 83500 | 50100 | 1500 | 1050 | 59000 | Turbofan | 2 | 1 | 590 | Air superiority, strike missions | 1 | 0 |
| 4051 | USA | F-35A Lightning II | 2016 | Stealth Multi-Role | 35.0 | 50.8 | 73600 | 44160 | 1200 | 840 | 61200 | Turbofan | 2 | 1 | 1240 | Air-to-air and air-to-ground | 1 | 0 |
| 4060 | USA | B-17 Flying Fortress | 1941 | Heavy Bomber | 103.9 | 67.5 | 65500 | 39300 | 900 | 630 | 40250 | Piston | 4 | 10 | 830 | Tactical bombing | 1 | 1 |
| 4061 | USA | B-17G Flying Fortress | 1943 | Heavy Bomber | 103.9 | 67.5 | 65500 | 39300 | 900 | 630 | 40750 | Piston | 4 | 10 | 890 | Tactical bombing | 1 | 0 |
| 4062 | USA | B-24 Liberator | 1941 | Heavy Bomber | 110.0 | 71.5 | 52000 | 31200 | 550 | 385 | 40250 | Piston | 1 | 2 | 830 | Tactical bombing | 1 | 0 |
| 4063 | USA | B-29 Superfortress | 1944 | Heavy Bomber | 141.3 | 91.8 | 141100 | 84660 | 550 | 385 | 41000 | Piston | 8 | 11 | 1600 | Tactical bombing | 1 | 0 |
| 4070 | USA | B-36 Peacemaker | 1949 | Strategic Bomber | 110.8 | 72.0 | 197000 | 118200 | 322 | 225 | 42250 | Turbojet | 1 | 3 | 1920 | Strategic bombing, long-range strike | 1 | 0 |
| 4071 | USA | B-47 Stratojet | 1951 | Strategic Bomber | 116.0 | 75.4 | 203000 | 121800 | 580 | 406 | 42750 | Turbojet | 4 | 3 | 2080 | Strategic bombing, long-range strike | 1 | 0 |
| 4072 | USA | B-52 Stratofortress | 1955 | Strategic Bomber | 185.0 | 120.2 | 488000 | 292800 | 560 | 392 | 43750 | Turbojet | 8 | 5 | 4480 | Strategic bombing, long-range strike | 1 | 0 |
| 4073 | USA | B-52H Stratofortress | 1961 | Strategic Bomber | 185.0 | 120.2 | 488000 | 292800 | 560 | 392 | 45250 | Turbojet | 8 | 5 | 4480 | Strategic bombing, long-range strike | 1 | 0 |
| 4074 | USA | B-58 Hustler | 1960 | Supersonic Bomber | 56.8 | 36.9 | 90000 | 54000 | 410 | 287 | 45000 | Turbojet | 1 | 3 | 1400 | Tactical bombing | 1 | 0 |
| 4075 | USA | FB-111A | 1969 | Strategic Bomber | 137.0 | 89.0 | 477000 | 286200 | 900 | 630 | 47250 | Turbojet | 4 | 4 | 3100 | Strategic bombing, long-range strike | 1 | 0 |
| 4080 | USA | B-1B Lancer | 1986 | Strategic Bomber | 137.0 | 89.0 | 477000 | 286200 | 900 | 630 | 50000 | Turbofan | 4 | 4 | 3100 | Strategic bombing, long-range strike | 1 | 0 |
| 4081 | USA | B-2A Spirit | 1997 | Stealth Bomber | 42.0 | 60.9 | 164000 | 98400 | 550 | 385 | 57400 | Turbofan | 4 | 1 | 2510 | Tactical bombing | 1 | 0 |
| 4082 | USA | B-21 Raider | 2025 | Stealth Bomber | 42.0 | 60.9 | 220000 | 132000 | 550 | 385 | 63000 | Turbofan | 4 | 1 | 3350 | Tactical bombing | 1 | 0 |
| 4090 | USA | A-10A Thunderbolt II | 1977 | Close Air Support | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Multi-purpose operations | 1 | 1 |
| 4091 | USA | A-10C Thunderbolt II | 2007 | Close Air Support | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4092 | USA | AC-130H Spectre | 1972 | Gunship | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4093 | USA | AC-130U Spooky | 1995 | Gunship | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4094 | USA | AC-130J Ghostrider | 2015 | Gunship | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4100 | USA | C-47 Skytrain | 1941 | Transport | 104.8 | 78.6 | 43000 | 25800 | 186 | 130 | 33100 | Turbofan | 4 | 4 | 930 | Cargo transport, airlift | 1 | 1 |
| 4101 | USA | C-54 Skymaster | 1942 | Transport | 105.6 | 79.2 | 46000 | 27600 | 192 | 134 | 33200 | Turbofan | 4 | 4 | 960 | Cargo transport, airlift | 1 | 0 |
| 4102 | USA | C-119 Flying Boxcar | 1950 | Transport | 100.4 | 75.3 | 70000 | 42000 | 240 | 168 | 34000 | Turbofan | 4 | 4 | 1200 | Cargo transport, airlift | 1 | 0 |
| 4103 | USA | C-130A Hercules | 1956 | Transport | 100.4 | 75.3 | 175000 | 105000 | 276 | 193 | 34600 | Turboprop | 4 | 4 | 1380 | Cargo transport, airlift | 1 | 0 |
| 4104 | USA | C-130H Hercules | 1974 | Transport | 100.4 | 75.3 | 175000 | 105000 | 384 | 268 | 36400 | Turboprop | 4 | 4 | 1920 | Cargo transport, airlift | 1 | 0 |
| 4105 | USA | C-130J Super Hercules | 1999 | Transport | 100.4 | 75.3 | 175000 | 105000 | 534 | 373 | 38900 | Turboprop | 4 | 4 | 2670 | Cargo transport, airlift | 1 | 0 |
| 4110 | USA | C-141 Starlifter | 1965 | Strategic Transport | 130.0 | 97.5 | 115000 | 69000 | 330 | 230 | 35500 | Turbofan | 4 | 4 | 1650 | Cargo transport, airlift | 1 | 0 |
| 4111 | USA | C-5A Galaxy | 1970 | Strategic Transport | 136.0 | 102.0 | 130000 | 78000 | 360 | 251 | 36000 | Turbofan | 4 | 4 | 1800 | Cargo transport, airlift | 1 | 0 |
| 4112 | USA | C-5M Super Galaxy | 2009 | Strategic Transport | 182.8 | 137.1 | 247000 | 148200 | 594 | 415 | 39900 | Turbofan | 4 | 4 | 2970 | Cargo transport, airlift | 1 | 0 |
| 4113 | USA | C-17 Globemaster III | 1995 | Strategic Transport | 166.0 | 124.5 | 585000 | 351000 | 510 | 357 | 38500 | Turbofan | 4 | 4 | 2550 | Cargo transport, airlift | 1 | 0 |
| 4120 | USA | UH-1 Iroquois | 1959 | Utility Helo | 48.0 | 62.4 | 14800 | 8880 | 119 | 83 | 14950 | Turboshaft | 2 | 2 | 147 | Troop transport, utility | 1 | 1 |
| 4121 | USA | UH-1H Huey | 1967 | Utility Helo | 48.0 | 62.4 | 16400 | 9840 | 127 | 88 | 15350 | Turboshaft | 2 | 2 | 171 | Troop transport, utility | 1 | 0 |
| 4122 | USA | UH-60A Black Hawk | 1979 | Utility Helo | 53.7 | 69.8 | 23500 | 14100 | 159 | 111 | 15950 | Turboshaft | 2 | 2 | 207 | Troop transport, utility | 1 | 0 |
| 4123 | USA | UH-60M Black Hawk | 2006 | Utility Helo | 53.7 | 69.8 | 23500 | 14100 | 159 | 111 | 17300 | Turboshaft | 2 | 2 | 288 | Troop transport, utility | 1 | 0 |
| 4130 | USA | AH-1 Cobra | 1967 | Attack Helo | 41.4 | 53.8 | 32800 | 19680 | 605 | 423 | 15350 | Turboshaft | 2 | 1 | 370 | Close air support, ground attack | 1 | 0 |
| 4131 | USA | AH-64A Apache | 1986 | Attack Helo | 45.2 | 58.8 | 40400 | 24240 | 890 | 623 | 16300 | Turboshaft | 2 | 1 | 560 | Close air support, ground attack | 1 | 0 |
| 4132 | USA | AH-64D Longbow Apache | 1997 | Attack Helo | 47.4 | 61.6 | 44800 | 26880 | 1055 | 738 | 16850 | Turboshaft | 2 | 1 | 670 | Close air support, ground attack | 1 | 0 |
| 4133 | USA | AH-64E Guardian | 2011 | Attack Helo | 50.2 | 65.3 | 50400 | 30240 | 1265 | 885 | 17550 | Turboshaft | 2 | 1 | 810 | Close air support, ground attack | 1 | 0 |
| 4140 | USA | CH-47A Chinook | 1962 | Heavy Transport Helo | 121.6 | 91.2 | 106000 | 63600 | 312 | 218 | 35200 | Turbofan | 4 | 4 | 1560 | Cargo transport, airlift | 1 | 1 |
| 4141 | USA | CH-47D Chinook | 1982 | Heavy Transport Helo | 137.6 | 103.2 | 166000 | 99600 | 432 | 302 | 37200 | Turbofan | 4 | 4 | 2160 | Cargo transport, airlift | 1 | 0 |
| 4142 | USA | CH-47F Chinook | 2007 | Heavy Transport Helo | 157.6 | 118.2 | 241000 | 144600 | 582 | 407 | 39700 | Turbofan | 4 | 4 | 2910 | Cargo transport, airlift | 1 | 0 |
| 4150 | USA | U-2A Dragon Lady | 1957 | Reconnaissance | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Electronic warfare, reconnaissance | 1 | 1 |
| 4151 | USA | U-2R Dragon Lady | 1967 | Reconnaissance | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Electronic warfare, reconnaissance | 1 | 0 |
| 4152 | USA | SR-71 Blackbird | 1966 | Reconnaissance | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Electronic warfare, reconnaissance | 1 | 0 |
| 4153 | USA | RQ-4 Global Hawk | 2001 | UAV Recon | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Electronic warfare, reconnaissance | 1 | 0 |
| 4154 | USA | MQ-9 Reaper | 2007 | UAV Attack | 49.4 | 54.3 | 48800 | 29280 | 1205 | 843 | 40000 | Piston | 1 | 1 | 770 | Close air support, ground attack | 1 | 0 |
| 4155 | USA | MQ-9B Sky Guardian | 2020 | UAV Multi-Role | 40.5 | 44.6 | 76000 | 45600 | 1600 | 1120 | 62000 | Turbofan | 1 | 1 | 1300 | Air-to-air and air-to-ground | 1 | 0 |
| 4160 | USA | KC-135 Stratotanker | 1957 | Tanker | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Aerial refueling | 1 | 0 |
| 4161 | USA | KC-10 Extender | 1981 | Tanker | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Aerial refueling | 1 | 0 |
| 4162 | USA | KC-46 Pegasus | 2019 | Tanker | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Aerial refueling | 1 | 0 |
| 4200 | British | Spitfire Mk I | 1940 | Fighter | 36.1 | 41.5 | 8000 | 4800 | 378 | 264 | 35000 | Piston | 1 | 1 | 200 | Air superiority | 1 | 1 |
| 4201 | British | Spitfire Mk V | 1941 | Fighter | 36.1 | 41.5 | 8500 | 5100 | 378 | 264 | 35200 | Piston | 1 | 1 | 208 | Air superiority | 1 | 0 |
| 4202 | British | Spitfire Mk IX | 1942 | Fighter | 36.1 | 41.5 | 9000 | 5400 | 378 | 264 | 35400 | Piston | 1 | 1 | 216 | Air superiority | 1 | 0 |
| 4203 | British | Spitfire Mk XIV | 1944 | Fighter | 36.1 | 41.5 | 10000 | 6000 | 378 | 264 | 35800 | Piston | 1 | 1 | 232 | Air superiority | 1 | 0 |
| 4210 | British | Meteor F.1 | 1944 | Jet Fighter | 37.2 | 42.8 | 20000 | 12000 | 600 | 420 | 44850 | Turbojet | 2 | 1 | 232 | Air superiority | 1 | 0 |
| 4211 | British | Meteor F.8 | 1950 | Jet Fighter | 37.2 | 42.8 | 20000 | 12000 | 600 | 420 | 45750 | Turbojet | 2 | 1 | 280 | Air superiority | 1 | 0 |
| 4212 | British | Hunter F.1 | 1954 | Jet Fighter | 33.8 | 38.9 | 24000 | 14400 | 730 | 510 | 46350 | Turbojet | 1 | 1 | 312 | Air superiority | 1 | 0 |
| 4213 | British | Lightning F.1 | 1960 | Interceptor | 34.8 | 38.3 | 40000 | 24000 | 1500 | 1050 | 50000 | Turbofan | 2 | 1 | 400 | Air defense, interception | 1 | 0 |
| 4214 | British | Phantom FGR.2 | 1969 | Multi-Role | 38.0 | 41.7 | 45400 | 27240 | 1090 | 763 | 51800 | Turbofan | 1 | 1 | 535 | Air-to-air and air-to-ground | 1 | 0 |
| 4220 | British | Tornado F.3 | 1986 | Interceptor | 39.1 | 43.0 | 61700 | 37020 | 1590 | 1113 | 55200 | Turbofan | 1 | 2 | 790 | Air defense, interception | 1 | 0 |
| 4221 | British | Typhoon FGR.4 | 2007 | Multi-Role | 35.9 | 39.5 | 52000 | 31200 | 1320 | 923 | 59400 | Turbofan | 2 | 1 | 1105 | Air-to-air and air-to-ground | 1 | 0 |
| 4222 | British | F-35B Lightning II (RAF) | 2018 | Stealth Multi-Role | 35.0 | 50.8 | 74800 | 44880 | 1200 | 840 | 61600 | Turbofan | 2 | 1 | 1270 | Air-to-air and air-to-ground | 1 | 0 |
| 4230 | British | Lancaster | 1942 | Heavy Bomber | 102.0 | 66.3 | 72000 | 43200 | 266 | 186 | 40500 | Piston | 1 | 3 | 860 | Tactical bombing | 1 | 1 |
| 4231 | British | Lincoln | 1945 | Heavy Bomber | 120.0 | 78.0 | 60000 | 36000 | 290 | 203 | 41250 | Piston | 1 | 3 | 950 | Tactical bombing | 1 | 0 |
| 4232 | British | Canberra B.2 | 1951 | Bomber | 63.9 | 41.5 | 72000 | 43200 | 338 | 236 | 42750 | Turbojet | 1 | 3 | 1130 | Tactical bombing | 1 | 0 |
| 4233 | British | Vulcan B.1 | 1957 | Strategic Bomber | 111.0 | 72.2 | 204000 | 122400 | 580 | 406 | 44250 | Turbojet | 4 | 5 | 2560 | Strategic bombing, long-range strike | 1 | 0 |
| 4234 | British | Vulcan B.2 | 1960 | Strategic Bomber | 111.0 | 72.2 | 204000 | 122400 | 580 | 406 | 45000 | Turbojet | 4 | 5 | 2800 | Strategic bombing, long-range strike | 1 | 0 |
| 4240 | British | Harrier GR.1 | 1969 | V/STOL Attack | 25.3 | 27.8 | 33600 | 20160 | 635 | 444 | 40000 | Piston | 1 | 1 | 390 | Close air support, ground attack | 1 | 1 |
| 4241 | British | Harrier GR.7 | 1990 | V/STOL Attack | 25.3 | 27.8 | 42000 | 25200 | 950 | 665 | 40000 | Piston | 1 | 1 | 600 | Close air support, ground attack | 1 | 0 |
| 4250 | British | C-130K Hercules (RAF) | 1967 | Transport | 100.4 | 75.3 | 175000 | 105000 | 342 | 239 | 35700 | Turboprop | 4 | 4 | 1710 | Cargo transport, airlift | 1 | 1 |
| 4251 | British | C-130J Hercules (RAF) | 2000 | Transport | 100.4 | 75.3 | 175000 | 105000 | 540 | 378 | 39000 | Turboprop | 4 | 4 | 2700 | Cargo transport, airlift | 1 | 0 |
| 4252 | British | A400M Atlas | 2014 | Transport | 139.1 | 104.3 | 310000 | 186000 | 624 | 436 | 40400 | Turboprop | 4 | 4 | 3120 | Cargo transport, airlift | 1 | 0 |
| 4260 | British | Apache AH.1 (RAF) | 2001 | Attack Helo | 48.2 | 62.7 | 46400 | 27840 | 1115 | 780 | 17050 | Turboshaft | 2 | 1 | 710 | Close air support, ground attack | 1 | 1 |
| 4261 | British | Apache AH-64E (RAF) | 2020 | Attack Helo | 52.0 | 67.6 | 54000 | 32400 | 1400 | 979 | 18000 | Turboshaft | 2 | 1 | 900 | Close air support, ground attack | 1 | 0 |
| 4270 | British | Puma HC.1 | 1971 | Utility Helo | 49.2 | 64.0 | 17200 | 10320 | 131 | 91 | 15550 | Turboshaft | 2 | 2 | 183 | Troop transport, utility | 1 | 0 |
| 4271 | British | Merlin HC.3 | 2001 | Transport Helo | 152.8 | 114.6 | 223000 | 133800 | 546 | 382 | 39100 | Turbofan | 4 | 4 | 2730 | Cargo transport, airlift | 1 | 0 |
| 4300 | German | Bf 109E | 1940 | Fighter | 32.5 | 37.4 | 8000 | 4800 | 398 | 278 | 35000 | Piston | 1 | 1 | 200 | Air superiority | 1 | 1 |
| 4301 | German | Bf 109F | 1941 | Fighter | 32.5 | 37.4 | 8500 | 5100 | 398 | 278 | 35200 | Piston | 1 | 1 | 208 | Air superiority | 1 | 0 |
| 4302 | German | Bf 109G | 1942 | Fighter | 32.5 | 37.4 | 9000 | 5400 | 398 | 278 | 35400 | Piston | 1 | 1 | 216 | Air superiority | 1 | 0 |
| 4303 | German | Fw 190A | 1941 | Fighter | 34.5 | 39.7 | 8500 | 5100 | 310 | 217 | 35200 | Piston | 1 | 1 | 208 | Air superiority | 1 | 0 |
| 4304 | German | Fw 190D | 1944 | Fighter | 34.5 | 39.7 | 10000 | 6000 | 340 | 237 | 35800 | Piston | 1 | 1 | 232 | Air superiority | 1 | 0 |
| 4310 | German | CL-13 Sabre (German) | 1955 | Jet Fighter | 37.1 | 42.7 | 19000 | 11400 | 750 | 525 | 46500 | Turbojet | 1 | 1 | 320 | Air superiority | 1 | 1 |
| 4311 | German | F-104G Starfighter | 1960 | Interceptor | 21.9 | 24.1 | 40000 | 24000 | 1450 | 1014 | 50000 | Turbofan | 1 | 1 | 400 | Air defense, interception | 1 | 0 |
| 4312 | German | F-4F Phantom II | 1973 | Multi-Role | 38.1 | 42.0 | 61800 | 37080 | 1130 | 791 | 52600 | Turbofan | 1 | 1 | 595 | Air-to-air and air-to-ground | 1 | 0 |
| 4320 | German | Tornado IDS | 1979 | Strike | 45.7 | 50.3 | 61700 | 37020 | 1490 | 1043 | 40000 | Turbofan | 1 | 2 | 400 | Ground attack, strike missions | 1 | 0 |
| 4321 | German | Eurofighter Typhoon | 2004 | Multi-Role | 35.9 | 39.5 | 52000 | 31200 | 1320 | 923 | 58800 | Turbofan | 2 | 1 | 1060 | Air-to-air and air-to-ground | 1 | 0 |
| 4322 | German | F-35A Lightning II (Luftwaffe) | 2024 | Stealth Multi-Role | 35.0 | 50.8 | 78400 | 47040 | 1200 | 840 | 62800 | Turbofan | 2 | 1 | 1360 | Air-to-air and air-to-ground | 1 | 0 |
| 4330 | German | Ju 87 Stuka | 1940 | Dive Bomber | 45.3 | 29.4 | 50000 | 30000 | 250 | 175 | 40000 | Piston | 1 | 3 | 800 | Tactical bombing | 1 | 1 |
| 4331 | German | Ju 88 | 1940 | Bomber | 65.6 | 42.6 | 50000 | 30000 | 250 | 175 | 40000 | Piston | 1 | 3 | 800 | Tactical bombing | 1 | 0 |
| 4332 | German | He 111 | 1941 | Bomber | 74.0 | 48.1 | 52000 | 31200 | 258 | 180 | 40250 | Piston | 1 | 3 | 830 | Tactical bombing | 1 | 0 |
| 4340 | German | Tornado ECR | 1990 | EW/Recon | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Electronic warfare, reconnaissance | 1 | 0 |
| 4350 | German | C-160 Transall | 1967 | Transport | 100.4 | 75.3 | 112400 | 67440 | 342 | 239 | 35700 | Turboprop | 4 | 4 | 1710 | Cargo transport, airlift | 1 | 1 |
| 4351 | German | A400M (Luftwaffe) | 2014 | Transport | 139.1 | 104.3 | 310000 | 186000 | 624 | 436 | 40400 | Turboprop | 4 | 4 | 3120 | Cargo transport, airlift | 1 | 0 |
| 4360 | German | CH-53G | 1973 | Transport Helo | 130.4 | 97.8 | 139000 | 83400 | 378 | 264 | 36300 | Turbofan | 4 | 4 | 1890 | Cargo transport, airlift | 1 | 1 |
| 4361 | German | CH-53GA | 1989 | Transport Helo | 143.2 | 107.4 | 187000 | 112200 | 474 | 331 | 37900 | Turbofan | 4 | 4 | 2370 | Cargo transport, airlift | 1 | 0 |
| 4362 | German | NH90 (Luftwaffe) | 2019 | Utility Helo | 52.1 | 67.7 | 26800 | 16080 | 179 | 125 | 17950 | Turboshaft | 2 | 2 | 327 | Troop transport, utility | 1 | 0 |
| 4370 | German | UH-1D (Luftwaffe) | 1967 | Utility Helo | 48.0 | 62.4 | 16400 | 9840 | 127 | 88 | 15350 | Turboshaft | 2 | 2 | 171 | Troop transport, utility | 1 | 0 |
| 4371 | German | Tiger UHT | 2005 | Attack Helo | 49.0 | 63.7 | 48000 | 28800 | 1175 | 822 | 17250 | Turboshaft | 2 | 1 | 750 | Close air support, ground attack | 1 | 0 |
| 4400 | Japanese | A6M Zero | 1940 | Fighter | 39.4 | 45.3 | 8000 | 4800 | 351 | 245 | 35000 | Piston | 1 | 1 | 200 | Air superiority | 1 | 1 |
| 4401 | Japanese | Ki-43 Hayabusa (Oscar) | 1941 | Fighter | 35.8 | 41.2 | 8500 | 5100 | 310 | 217 | 35200 | Piston | 1 | 1 | 208 | Air superiority | 1 | 0 |
| 4402 | Japanese | Ki-61 Hien (Tony) | 1943 | Fighter | 39.4 | 45.3 | 9500 | 5700 | 330 | 230 | 35600 | Piston | 1 | 1 | 224 | Air superiority | 1 | 0 |
| 4403 | Japanese | Ki-84 Hayate (Frank) | 1944 | Fighter | 36.1 | 41.5 | 10000 | 6000 | 340 | 237 | 35800 | Piston | 1 | 1 | 232 | Air superiority | 1 | 0 |
| 4410 | Japanese | F-86F Sabre (JASDF) | 1956 | Jet Fighter | 37.1 | 42.7 | 20357 | 12214 | 687 | 480 | 46650 | Turbojet | 1 | 1 | 328 | Air superiority | 1 | 1 |
| 4411 | Japanese | F-104J Starfighter | 1962 | Interceptor | 21.9 | 24.1 | 41200 | 24720 | 1450 | 1014 | 50400 | Turbofan | 1 | 1 | 430 | Air defense, interception | 1 | 0 |
| 4412 | Japanese | F-4EJ Phantom II | 1971 | Multi-Role | 38.0 | 41.9 | 61800 | 37080 | 1110 | 777 | 52200 | Turbofan | 1 | 1 | 565 | Air-to-air and air-to-ground | 1 | 0 |
| 4413 | Japanese | F-4EJ Kai | 1984 | Multi-Role | 38.7 | 42.6 | 61800 | 37080 | 1240 | 868 | 54800 | Turbofan | 1 | 1 | 760 | Air-to-air and air-to-ground | 1 | 0 |
| 4420 | Japanese | F-15J Eagle | 1981 | Air Superiority | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 2 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4421 | Japanese | F-15J(M) Kai | 2004 | Air Superiority | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 2 | 1 | 400 | Multi-purpose operations | 1 | 0 |
| 4430 | Japanese | F-2A | 2000 | Multi-Role | 36.1 | 39.7 | 50000 | 30000 | 1400 | 979 | 58000 | Turbofan | 1 | 1 | 1000 | Air-to-air and air-to-ground | 1 | 0 |
| 4431 | Japanese | F-2B | 2002 | Multi-Role | 36.1 | 39.7 | 50000 | 30000 | 1420 | 993 | 58400 | Turbofan | 1 | 1 | 1030 | Air-to-air and air-to-ground | 1 | 0 |
| 4440 | Japanese | F-35A Lightning II (JASDF) | 2018 | Stealth Multi-Role | 35.0 | 50.8 | 74800 | 44880 | 1200 | 840 | 61600 | Turbofan | 2 | 1 | 1270 | Air-to-air and air-to-ground | 1 | 0 |
| 4441 | Japanese | F-15EX (JASDF) | 2024 | Multi-Role | 42.8 | 47.1 | 81000 | 48600 | 1640 | 1148 | 62800 | Turbofan | 2 | 2 | 1100 | Air-to-air and air-to-ground | 1 | 0 |
| 4450 | Japanese | C-1 | 1974 | Transport | 100.4 | 75.3 | 142000 | 85200 | 384 | 268 | 36400 | Turbofan | 4 | 4 | 1920 | Cargo transport, airlift | 1 | 1 |
| 4451 | Japanese | C-2 | 2017 | Transport | 144.5 | 108.4 | 271000 | 162600 | 642 | 449 | 40700 | Turbofan | 4 | 4 | 3210 | Cargo transport, airlift | 1 | 0 |
| 4452 | Japanese | C-130H Hercules (JASDF) | 1981 | Transport | 100.4 | 75.3 | 175000 | 105000 | 426 | 298 | 37100 | Turboprop | 4 | 4 | 2130 | Cargo transport, airlift | 1 | 0 |
| 4453 | Japanese | KC-767 | 2008 | Tanker | 40.0 | 44.0 | 25000 | 15000 | 400 | 280 | 40000 | Piston | 1 | 1 | 400 | Aerial refueling | 1 | 0 |
| 4460 | Japanese | UH-1H (JASDF) | 1973 | Utility Helo | 48.0 | 62.4 | 17600 | 10560 | 133 | 93 | 15650 | Turboshaft | 2 | 2 | 189 | Troop transport, utility | 1 | 1 |
| 4461 | Japanese | UH-60J Black Hawk | 1992 | Utility Helo | 53.7 | 69.8 | 23500 | 14100 | 159 | 111 | 16600 | Turboshaft | 2 | 2 | 246 | Troop transport, utility | 1 | 0 |
| 4462 | Japanese | UH-60J Kai | 2012 | Utility Helo | 53.7 | 69.8 | 23500 | 14100 | 159 | 111 | 17600 | Turboshaft | 2 | 2 | 306 | Troop transport, utility | 1 | 0 |
| 4470 | Japanese | AH-1S Cobra (JASDF) | 1978 | Attack Helo | 43.6 | 56.7 | 37200 | 22320 | 770 | 539 | 15900 | Turboshaft | 2 | 1 | 480 | Close air support, ground attack | 1 | 0 |
| 4471 | Japanese | AH-64D Apache (JASDF) | 2006 | Attack Helo | 49.2 | 64.0 | 48400 | 29040 | 1190 | 833 | 17300 | Turboshaft | 2 | 1 | 760 | Close air support, ground attack | 1 | 0 |
| 4480 | Japanese | CH-47J Chinook | 1986 | Transport Helo | 140.8 | 105.6 | 178000 | 106800 | 456 | 319 | 37600 | Turbofan | 4 | 4 | 2280 | Cargo transport, airlift | 1 | 0 |
| 4481 | Japanese | CH-47JA Chinook | 2001 | Transport Helo | 152.8 | 114.6 | 223000 | 133800 | 546 | 382 | 39100 | Turbofan | 4 | 4 | 2730 | Cargo transport, airlift | 1 | 0 |

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
