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
# Converting naval aircraft research nodes to detailed database entries
# Estimating specifications based on type, year, and designation
| 3000 | USA | F4F Wildcat | 1940 | Fighter | 38.0 | 28.5 | 8000 | 4960 | 290 | 250 | 30000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3001 | USA | F4F-4 Wildcat | 1942 | Fighter | 38.0 | 28.5 | 8200 | 5084 | 306 | 280 | 31000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3002 | USA | F6F Hellcat | 1943 | Fighter | 42.8 | 32.1 | 8300 | 5146 | 314 | 295 | 31500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3003 | USA | F6F-5 Hellcat | 1944 | Fighter | 42.8 | 32.1 | 8400 | 5208 | 322 | 310 | 32000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3004 | USA | F8F Bearcat | 1945 | Fighter | 35.5 | 26.6 | 8500 | 5270 | 330 | 325 | 32500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3010 | USA | F9F Panther | 1949 | Jet Fighter | 38.0 | 41.8 | 30000 | 18600 | 600 | 395 | 44800 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3011 | USA | F9F-5 Panther | 1950 | Jet Fighter | 38.0 | 41.8 | 30000 | 18600 | 612 | 400 | 45000 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3012 | USA | F9F-8 Cougar | 1954 | Jet Fighter | 34.5 | 38.0 | 30000 | 18600 | 660 | 420 | 45800 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3013 | USA | F11F Tiger | 1956 | Jet Fighter | 31.6 | 34.8 | 30000 | 18600 | 684 | 430 | 46200 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3014 | USA | F8U Crusader | 1957 | Jet Fighter | 35.6 | 39.2 | 30000 | 18600 | 696 | 435 | 46400 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3015 | USA | F8U-2 Crusader | 1960 | Jet Fighter | 35.6 | 39.2 | 30000 | 18600 | 732 | 450 | 47000 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3020 | USA | F-4B Phantom II | 1962 | Multi-Role | 38.4 | 63.0 | 61650 | 38223 | 1470 | 466 | 47400 | Turbojet | 2 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3021 | USA | F-4J Phantom II | 1966 | Multi-Role | 38.4 | 63.0 | 61650 | 38223 | 1470 | 498 | 48200 | Turbojet | 2 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3022 | USA | F-4S Phantom II | 1978 | Multi-Role | 38.4 | 63.0 | 61650 | 38223 | 1470 | 594 | 50600 | Turbofan | 2 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3030 | USA | F-14A Tomcat | 1974 | Interceptor | 64.0 | 62.8 | 74350 | 46097 | 1240 | 520 | 49800 | Turbofan | 2 | 2 | 14500 | Fleet air defense interceptor | 1 | 0 |
| 3031 | USA | F-14A+ Tomcat | 1988 | Interceptor | 64.0 | 62.8 | 74350 | 46097 | 1240 | 590 | 52600 | Turbofan | 2 | 2 | 14500 | Fleet air defense interceptor | 1 | 0 |
| 3032 | USA | F-14D Tomcat | 1991 | Interceptor | 64.0 | 62.8 | 74350 | 46097 | 1240 | 605 | 53200 | Turbofan | 2 | 2 | 14500 | Fleet air defense interceptor | 1 | 0 |
| 3040 | USA | F/A-18A Hornet | 1983 | Multi-Role | 40.4 | 56.0 | 41500 | 25730 | 1008 | 634 | 51600 | Turbofan | 2 | 1 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3041 | USA | F/A-18C Hornet | 1987 | Multi-Role | 40.4 | 56.0 | 43500 | 26970 | 1056 | 666 | 52400 | Turbofan | 2 | 1 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3042 | USA | F/A-18E Super Hornet | 1999 | Multi-Role | 40.4 | 60.2 | 66000 | 40920 | 1190 | 762 | 54800 | Turbofan | 2 | 1 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3043 | USA | F/A-18F Super Hornet | 2001 | Multi-Role | 40.4 | 60.2 | 66000 | 40920 | 1190 | 778 | 55200 | Turbofan | 2 | 1 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3044 | USA | F/A-18E/F Block III | 2019 | Multi-Role | 44.8 | 60.2 | 59500 | 36890 | 1440 | 850 | 58800 | Turbofan | 2 | 1 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3050 | USA | F-35C Lightning II | 2019 | Stealth Fighter | 38.0 | 28.5 | 13500 | 8370 | 410 | 1435 | 39000 | Turbofan | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3051 | USA | F-35C Block 4 | 2025 | Stealth Fighter | 38.0 | 28.5 | 13500 | 8370 | 410 | 1525 | 39000 | Turbofan | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3060 | USA | SBD Dauntless | 1940 | Dive Bomber | 41.5 | 41.5 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Dive bomber | 1 | 0 |
| 3061 | USA | SBD-5 Dauntless | 1943 | Dive Bomber | 41.5 | 41.5 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Dive bomber | 1 | 0 |
| 3062 | USA | SB2C Helldiver | 1943 | Dive Bomber | 49.8 | 49.8 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Dive bomber | 1 | 0 |
| 3063 | USA | AD Skyraider | 1946 | Attack | 50.0 | 38.8 | 18400 | 11408 | 358 | 610 | 35150 | Piston radial | 1 | 1 | 15100 | Strike/attack aircraft | 1 | 0 |
| 3064 | USA | AD-6 Skyraider | 1953 | Attack | 50.0 | 38.8 | 21200 | 13144 | 414 | 680 | 36200 | Piston radial | 1 | 1 | 15800 | Strike/attack aircraft | 1 | 0 |
| 3070 | USA | A-4 Skyhawk | 1956 | Attack | 27.5 | 42.2 | 22400 | 13888 | 438 | 710 | 36650 | Piston radial | 1 | 1 | 16100 | Strike/attack aircraft | 1 | 0 |
| 3071 | USA | A-4E Skyhawk | 1962 | Attack | 27.5 | 42.2 | 24800 | 15376 | 486 | 770 | 37550 | Piston radial | 1 | 1 | 16700 | Strike/attack aircraft | 1 | 0 |
| 3072 | USA | A-4M Skyhawk | 1970 | Attack | 27.5 | 42.2 | 28000 | 17360 | 550 | 850 | 38750 | Piston radial | 1 | 1 | 17500 | Strike/attack aircraft | 1 | 0 |
| 3073 | USA | A-6A Intruder | 1963 | Attack | 53.0 | 54.8 | 25200 | 15624 | 494 | 780 | 37700 | Piston radial | 1 | 2 | 16800 | Strike/attack aircraft | 1 | 0 |
| 3074 | USA | A-6E Intruder | 1970 | Attack | 53.0 | 54.8 | 28000 | 17360 | 550 | 850 | 38750 | Piston radial | 1 | 2 | 17500 | Strike/attack aircraft | 1 | 0 |
| 3075 | USA | A-6E TRAM | 1979 | Attack | 53.0 | 54.8 | 31600 | 19592 | 622 | 940 | 40100 | Piston radial | 1 | 1 | 18400 | Strike/attack aircraft | 1 | 0 |
| 3076 | USA | A-7 Corsair II | 1967 | Attack | 38.7 | 36.8 | 26800 | 16616 | 526 | 820 | 38300 | Piston radial | 1 | 1 | 17200 | Strike/attack aircraft | 1 | 0 |
| 3077 | USA | A-7E Corsair II | 1969 | Attack | 38.7 | 36.8 | 27600 | 17112 | 542 | 840 | 38600 | Piston radial | 1 | 1 | 17400 | Strike/attack aircraft | 1 | 0 |
| 3080 | USA | TBF Avenger | 1942 | Torpedo Bomber | 54.1 | 54.1 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Torpedo bomber | 1 | 0 |
| 3081 | USA | TBM-3 Avenger | 1944 | Torpedo Bomber | 54.1 | 54.1 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Torpedo bomber | 1 | 0 |
| 3082 | USA | S-2 Tracker | 1954 | ASW | 69.6 | 80.0 | 49000 | 30380 | 270 | 790 | 25800 | Turboprop | 2 | 4 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3083 | USA | S-2E Tracker | 1962 | ASW | 69.6 | 80.0 | 57000 | 35340 | 310 | 870 | 27400 | Turboprop | 2 | 4 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3084 | USA | S-3A Viking | 1974 | ASW | 68.6 | 53.3 | 69000 | 42780 | 370 | 990 | 29800 | Turboprop | 2 | 2 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3085 | USA | S-3B Viking | 1987 | ASW | 68.6 | 53.3 | 82000 | 50840 | 435 | 1120 | 32400 | Turboprop | 2 | 2 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3086 | USA | P-3C Orion | 1969 | ASW/Patrol | 99.6 | 116.8 | 142000 | 88040 | 345 | 1200 | 28800 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3087 | USA | P-3C Update III | 1984 | ASW/Patrol | 99.6 | 116.8 | 142000 | 88040 | 420 | 1200 | 31800 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3088 | USA | P-8A Poseidon | 2013 | ASW/Patrol | 123.5 | 129.5 | 189200 | 117304 | 490 | 1200 | 37600 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3089 | USA | P-8A Block II | 2020 | ASW/Patrol | 123.5 | 129.5 | 189200 | 117304 | 490 | 1200 | 39000 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3090 | USA | E-1 Tracer | 1958 | AEW | 69.6 | 69.6 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Airborne early warning | 1 | 0 |
| 3091 | USA | E-2A Hawkeye | 1964 | AEW | 80.6 | 80.6 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Airborne early warning | 1 | 0 |
| 3092 | USA | E-2C Hawkeye | 1973 | AEW | 80.6 | 80.6 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Airborne early warning | 1 | 0 |
| 3093 | USA | E-2C Group II | 2000 | AEW | 80.6 | 80.6 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Airborne early warning | 1 | 0 |
| 3094 | USA | E-2D Advanced Hawkeye | 2014 | AEW | 80.6 | 80.6 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Airborne early warning | 1 | 0 |
| 3095 | USA | EA-6A Intruder | 1965 | EW | 53.0 | 53.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 2 | 0 | Electronic warfare | 1 | 0 |
| 3096 | USA | EA-6B Prowler | 1971 | EW | 53.0 | 53.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 2 | 0 | Electronic warfare | 1 | 0 |
| 3097 | USA | EA-6B ICAP II | 1989 | EW | 53.0 | 53.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Electronic warfare | 1 | 0 |
| 3098 | USA | EA-18G Growler | 2009 | EW | 44.8 | 44.8 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Electronic warfare | 1 | 0 |
| 3100 | USA | RF-8G Crusader | 1965 | Recon | 60.0 | 60.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 0 | Reconnaissance | 1 | 0 |
| 3101 | USA | RA-5C Vigilante | 1962 | Recon | 53.0 | 53.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 0 | Reconnaissance | 1 | 0 |
| 3102 | USA | F-14 TARPS | 1981 | Recon | 60.0 | 60.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 0 | Reconnaissance | 1 | 0 |
| 3103 | USA | F/A-18 ATARS | 1996 | Recon | 60.0 | 60.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 0 | Reconnaissance | 1 | 0 |
| 3110 | USA | SH-3 Sea King | 1961 | ASW Helo | 90.0 | 103.5 | 56000 | 34720 | 305 | 860 | 27200 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3111 | USA | SH-3H Sea King | 1974 | ASW Helo | 90.0 | 103.5 | 69000 | 42780 | 370 | 990 | 29800 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3112 | USA | SH-60B Seahawk | 1984 | ASW Helo | 90.0 | 103.5 | 79000 | 48980 | 420 | 1090 | 31800 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3113 | USA | SH-60F Seahawk | 1989 | ASW Helo | 90.0 | 103.5 | 84000 | 52080 | 445 | 1140 | 32800 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3114 | USA | MH-60R Seahawk | 2006 | Multi-Role Helo | 40.0 | 44.0 | 53000 | 32860 | 1284 | 818 | 56200 | Turbofan | 1 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3115 | USA | MH-60R Block II | 2020 | Multi-Role Helo | 40.0 | 44.0 | 60000 | 37200 | 1452 | 850 | 59000 | Turbofan | 1 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3116 | USA | MH-60S Knighthawk | 2002 | Utility Helo | 53.7 | 45.6 | 18300 | 11346 | 180 | 350 | 14200 | Turboshaft | 1 | 2 | 4000 | Utility helicopter | 1 | 0 |
| 3120 | USA | MQ-25 Stingray | 2021 | UAV Tanker | 75.0 | 75.0 | 51000 | 31620 | 350 | 500 | 40000 | Turbofan | 1 | 0 | 0 | Unmanned aerial refueling | 1 | 0 |
| 3200 | British | Sea Hurricane | 1941 | Fighter | 40.0 | 30.0 | 8100 | 5022 | 298 | 265 | 30500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3201 | British | Seafire Mk III | 1943 | Fighter | 36.8 | 27.6 | 8300 | 5146 | 314 | 295 | 31500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3202 | British | Seafire Mk XV | 1945 | Fighter | 36.8 | 27.6 | 8500 | 5270 | 330 | 325 | 32500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3210 | British | Sea Fury | 1947 | Fighter | 38.4 | 28.8 | 8700 | 5394 | 346 | 355 | 33500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3211 | British | Attacker | 1951 | Jet Fighter | 36.9 | 40.6 | 30000 | 18600 | 624 | 405 | 45200 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3212 | British | Sea Hawk | 1953 | Jet Fighter | 39.0 | 42.9 | 30000 | 18600 | 648 | 415 | 45600 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3213 | British | Sea Venom | 1954 | Jet Fighter | 42.8 | 47.1 | 30000 | 18600 | 660 | 420 | 45800 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3214 | British | Scimitar | 1958 | Jet Fighter | 37.1 | 40.8 | 30000 | 18600 | 708 | 440 | 46600 | Turbojet | 1 | 1 | 8000 | Carrier jet fighter | 1 | 0 |
| 3215 | British | Sea Vixen | 1959 | Jet Fighter | 50.0 | 55.0 | 30000 | 18600 | 720 | 445 | 46800 | Turbojet | 1 | 2 | 8000 | Carrier jet fighter | 1 | 0 |
| 3220 | British | Phantom FG.1 | 1968 | Multi-Role | 38.4 | 63.0 | 61650 | 38223 | 1470 | 514 | 48600 | Turbojet | 2 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3221 | British | Phantom FGR.2 | 1969 | Multi-Role | 38.4 | 63.0 | 61650 | 38223 | 1470 | 522 | 48800 | Turbojet | 2 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3230 | British | Sea Harrier FRS.1 | 1978 | V/STOL | 40.0 | 40.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | V/STOL carrier operations | 1 | 0 |
| 3231 | British | Sea Harrier FA.2 | 1993 | V/STOL | 40.0 | 40.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | V/STOL carrier operations | 1 | 0 |
| 3240 | British | F-35B Lightning II | 2018 | V/STOL Stealth | 40.0 | 40.0 | 70000 | 43400 | 1200 | 550 | 50000 | Turbofan | 2 | 1 | 18000 | 5th generation stealth multi-role | 1 | 0 |
| 3241 | British | F-35B Block 4 | 2025 | V/STOL Stealth | 40.0 | 40.0 | 70000 | 43400 | 1200 | 550 | 50000 | Turbofan | 2 | 1 | 18000 | 5th generation stealth multi-role | 1 | 0 |
| 3250 | British | Swordfish | 1940 | Torpedo Bomber | 45.5 | 45.5 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Torpedo bomber | 1 | 0 |
| 3251 | British | Barracuda | 1943 | Torpedo Bomber | 49.1 | 49.1 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Torpedo bomber | 1 | 0 |
| 3252 | British | Firefly | 1944 | Strike | 41.1 | 39.0 | 17600 | 10912 | 342 | 590 | 34850 | Piston radial | 2 | 1 | 14900 | Strike/attack aircraft | 1 | 0 |
| 3253 | British | Wyvern | 1953 | Strike | 44.0 | 41.8 | 21200 | 13144 | 414 | 680 | 36200 | Piston radial | 2 | 1 | 15800 | Strike/attack aircraft | 1 | 0 |
| 3254 | British | Buccaneer S.1 | 1962 | Strike | 44.0 | 63.4 | 24800 | 15376 | 486 | 770 | 37550 | Piston radial | 2 | 2 | 16700 | Strike/attack aircraft | 1 | 0 |
| 3255 | British | Buccaneer S.2 | 1965 | Strike | 44.0 | 63.4 | 26000 | 16120 | 510 | 800 | 38000 | Piston radial | 2 | 2 | 17000 | Strike/attack aircraft | 1 | 0 |
| 3260 | British | Gannet AS.1 | 1955 | ASW | 54.3 | 62.4 | 50000 | 31000 | 275 | 800 | 26000 | Turboprop | 2 | 4 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3261 | British | Gannet AS.4 | 1959 | ASW | 54.3 | 62.4 | 54000 | 33480 | 295 | 840 | 26800 | Turboprop | 2 | 4 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3262 | British | Nimrod MR.1 | 1969 | ASW/Patrol | 114.8 | 126.8 | 64000 | 39680 | 345 | 940 | 28800 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3263 | British | Nimrod MR.2 | 1979 | ASW/Patrol | 114.8 | 126.8 | 74000 | 45880 | 395 | 1040 | 30800 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3264 | British | Nimrod MRA.4 | 2010 | ASW/Patrol | 114.8 | 126.8 | 105000 | 65100 | 490 | 1350 | 37000 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3265 | British | P-8A Poseidon (RAF) | 2020 | ASW/Patrol | 123.5 | 129.5 | 189200 | 117304 | 490 | 1200 | 39000 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3270 | British | Gannet AEW.3 | 1960 | AEW | 60.0 | 60.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 5 | 0 | Airborne early warning | 1 | 0 |
| 3271 | British | Sea King AEW.2 | 1982 | AEW Helo | 60.0 | 51.0 | 15300 | 9486 | 153 | 260 | 12200 | Turboshaft | 1 | 2 | 4000 | Airborne early warning | 1 | 0 |
| 3272 | British | Merlin HM.2 | 2014 | ASW Helo | 90.0 | 103.5 | 109000 | 67580 | 490 | 1390 | 37800 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3280 | British | Wasp HAS.1 | 1963 | ASW Helo | 90.0 | 103.5 | 58000 | 35960 | 315 | 880 | 27600 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3281 | British | Lynx HAS.2 | 1976 | ASW Helo | 90.0 | 103.5 | 71000 | 44020 | 380 | 1010 | 30200 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3282 | British | Lynx HMA.8 | 1995 | ASW Helo | 90.0 | 103.5 | 90000 | 55800 | 475 | 1200 | 34000 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3283 | British | Wildcat HMA.2 | 2015 | Multi-Role Helo | 40.0 | 44.0 | 57500 | 35650 | 1392 | 850 | 58000 | Turbofan | 1 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3300 | German | Tornado IDS (Naval) | 1979 | Strike | 45.0 | 42.8 | 31600 | 19592 | 622 | 940 | 40100 | Piston radial | 2 | 1 | 18400 | Strike/attack aircraft | 1 | 0 |
| 3301 | German | Tornado IDS Mid-Life | 1995 | Strike | 45.0 | 42.8 | 38000 | 23560 | 650 | 1100 | 42500 | Piston radial | 2 | 1 | 20000 | Strike/attack aircraft | 1 | 0 |
| 3302 | German | Eurofighter Typhoon (Naval) | 2004 | Multi-Role | 35.9 | 52.3 | 52000 | 32240 | 1260 | 802 | 55800 | Turbofan | 2 | 1 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3310 | German | Breguet Atlantic | 1972 | ASW/Patrol | 119.1 | 137.0 | 67000 | 41540 | 360 | 970 | 29400 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3311 | German | Atlantic 1 Mod | 1981 | ASW/Patrol | 119.1 | 137.0 | 76000 | 47120 | 405 | 1060 | 31200 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3312 | German | P-3C Orion (German) | 1995 | ASW/Patrol | 99.6 | 116.8 | 142000 | 88040 | 475 | 1200 | 34000 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3313 | German | P-8A Poseidon (German) | 2022 | ASW/Patrol | 123.5 | 129.5 | 189200 | 117304 | 490 | 1200 | 39400 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3320 | German | Sea King Mk 41 | 1972 | ASW Helo | 90.0 | 103.5 | 67000 | 41540 | 360 | 970 | 29400 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3321 | German | Sea King Mk 41 Mod | 1985 | ASW Helo | 90.0 | 103.5 | 80000 | 49600 | 425 | 1100 | 32000 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3322 | German | Sea Lynx Mk 88 | 1981 | ASW Helo | 90.0 | 103.5 | 76000 | 47120 | 405 | 1060 | 31200 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3323 | German | Super Lynx Mk 88A | 2001 | ASW Helo | 90.0 | 103.5 | 96000 | 59520 | 490 | 1260 | 35200 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3324 | German | NH90 Sea Lion | 2019 | Multi-Role Helo | 40.0 | 44.0 | 59500 | 36890 | 1440 | 850 | 58800 | Turbofan | 1 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3330 | German | MH-60R Seahawk (German) | 2025 | ASW Helo | 90.0 | 103.5 | 120000 | 74400 | 490 | 1500 | 40000 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3340 | German | Do 24 (Reactivated) | 1975 | Maritime Patrol | 40.0 | 40.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Naval aviation | 1 | 0 |
| 3400 | Japanese | A5M Claude | 1940 | Fighter | 38.0 | 28.5 | 8000 | 4960 | 290 | 250 | 30000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3401 | Japanese | A6M2 Zero | 1940 | Fighter | 39.4 | 29.5 | 8000 | 4960 | 290 | 250 | 30000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3402 | Japanese | A6M3 Zero | 1942 | Fighter | 39.4 | 29.5 | 8200 | 5084 | 306 | 280 | 31000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3403 | Japanese | A6M5 Zero | 1943 | Fighter | 39.4 | 29.5 | 8300 | 5146 | 314 | 295 | 31500 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3404 | Japanese | J2M Raiden (Jack) | 1943 | Interceptor | 40.0 | 44.0 | 21500 | 13330 | 528 | 365 | 43600 | Turbojet | 2 | 1 | 14500 | Fleet air defense interceptor | 1 | 0 |
| 3405 | Japanese | N1K2-J Shiden-Kai (George) | 1944 | Fighter | 39.4 | 29.5 | 8400 | 5208 | 322 | 310 | 32000 | Piston radial | 1 | 1 | 2000 | Carrier fighter | 1 | 0 |
| 3410 | Japanese | P-1 | 2013 | Maritime Patrol | 40.0 | 40.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Naval aviation | 1 | 0 |
| 3411 | Japanese | P-1 Mod 2 | 2022 | Maritime Patrol | 40.0 | 40.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Naval aviation | 1 | 0 |
| 3412 | Japanese | P-3C Orion (JMSDF) | 1982 | ASW/Patrol | 99.6 | 116.8 | 142000 | 88040 | 410 | 1200 | 31400 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3413 | Japanese | P-3C Update III (JMSDF) | 1995 | ASW/Patrol | 99.6 | 116.8 | 142000 | 88040 | 475 | 1200 | 34000 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3420 | Japanese | D3A Val | 1940 | Dive Bomber | 47.5 | 47.5 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Dive bomber | 1 | 0 |
| 3421 | Japanese | D4Y Suisei (Judy) | 1942 | Dive Bomber | 37.8 | 37.8 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Dive bomber | 1 | 0 |
| 3422 | Japanese | B7A Ryusei (Grace) | 1944 | Strike | 47.3 | 44.9 | 17600 | 10912 | 342 | 590 | 34850 | Piston radial | 2 | 1 | 14900 | Strike/attack aircraft | 1 | 0 |
| 3430 | Japanese | F-35B Lightning II (JMSDF) | 2024 | V/STOL Stealth | 40.0 | 40.0 | 70000 | 43400 | 1200 | 550 | 50000 | Turbofan | 2 | 1 | 18000 | 5th generation stealth multi-role | 1 | 0 |
| 3440 | Japanese | B5N Kate | 1940 | Torpedo Bomber | 50.9 | 50.9 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Torpedo bomber | 1 | 0 |
| 3441 | Japanese | B6N Tenzan (Jill) | 1943 | Torpedo Bomber | 48.8 | 48.8 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Torpedo bomber | 1 | 0 |
| 3442 | Japanese | P2V Neptune (JMSDF) | 1958 | ASW/Patrol | 103.3 | 118.8 | 53000 | 32860 | 290 | 830 | 26600 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3443 | Japanese | PS-1 | 1971 | ASW Flying Boat | 108.8 | 125.1 | 66000 | 40920 | 355 | 960 | 29200 | Turboprop | 4 | 10 | 20000 | Anti-submarine warfare patrol | 1 | 0 |
| 3444 | Japanese | US-2 | 2007 | SAR Flying Boat | 40.0 | 40.0 | 30000 | 18600 | 500 | 500 | 40000 | Piston radial | 2 | 1 | 8000 | Search and rescue | 1 | 0 |
| 3450 | Japanese | HSS-2 Sea King (JMSDF) | 1965 | ASW Helo | 69.6 | 80.0 | 60000 | 37200 | 325 | 900 | 28000 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3451 | Japanese | SH-3A Sea King (JMSDF) | 1974 | ASW Helo | 90.0 | 103.5 | 69000 | 42780 | 370 | 990 | 29800 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3452 | Japanese | SH-60J Seahawk | 1991 | ASW Helo | 90.0 | 103.5 | 86000 | 53320 | 455 | 1160 | 33200 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3453 | Japanese | SH-60K Seahawk | 2006 | ASW Helo | 90.0 | 103.5 | 101000 | 62620 | 490 | 1310 | 36200 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3454 | Japanese | SH-60K(Kai) | 2015 | ASW Helo | 90.0 | 103.5 | 110000 | 68200 | 490 | 1400 | 38000 | Turboshaft | 1 | 2 | 4000 | ASW helicopter | 1 | 0 |
| 3460 | Japanese | MCH-101 | 2008 | Multi-Role Helo | 40.0 | 44.0 | 54000 | 33480 | 1308 | 834 | 56600 | Turbofan | 1 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3461 | Japanese | MCH-101 Mod 2 | 2018 | Multi-Role Helo | 40.0 | 44.0 | 59000 | 36580 | 1428 | 850 | 58600 | Turbofan | 1 | 2 | 17750 | Multi-role fighter/attack | 1 | 0 |
| 3470 | Japanese | OH-6D | 1978 | Observation Helo | 26.4 | 22.4 | 14700 | 9114 | 147 | 240 | 11800 | Turboshaft | 1 | 2 | 4000 | Observation helicopter | 1 | 0 |
| 3471 | Japanese | OH-1 Ninja | 1999 | Observation Helo | 26.4 | 22.4 | 17850 | 11067 | 178 | 345 | 13900 | Turboshaft | 1 | 2 | 4000 | Observation helicopter | 1 | 0 |

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
