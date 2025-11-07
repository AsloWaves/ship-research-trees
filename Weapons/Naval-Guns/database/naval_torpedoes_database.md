# Naval Torpedoes Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 0 (ready for expansion)

---

## Database Contents

- [Torpedoes Table](#torpedoes-table) - Naval torpedo systems
- [Torpedo Warheads Table](#torpedo-warheads-table) - Warhead specifications
- [Launch Systems Table](#launch-systems-table) - Torpedo tube and launcher configurations

---

<a name="torpedoes-table"></a>
## Torpedoes Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Torpedo_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation of origin (USA, British, German, Japanese, etc.) |
| Designation | VARCHAR(100) | Official designation/mark (e.g., "Mark 48 Mod 7", "Type 93", "G7es") |
| Type | VARCHAR(50) | Torpedo type (Steam, Electric, Wakeless, Acoustic, Wire-guided, Homing) |
| Year_Introduced | INT | Year entered service |
| Diameter_IN | DECIMAL(5,2) | Diameter in inches |
| Length_FT | DECIMAL(6,2) | Total length in feet |
| Weight_LBS | DECIMAL(8,2) | Total weight in pounds |
| Warhead_LBS | DECIMAL(7,2) | Warhead weight in pounds |
| Warhead_Type | VARCHAR(50) | Explosive type (TNT, Torpex, HBX, etc.) |
| Max_Speed_KTS | DECIMAL(5,1) | Maximum speed in knots |
| Max_Range_YDS | INT | Maximum range in yards |
| Running_Depth_FT | VARCHAR(50) | Operating depth range (e.g., "10-40") |
| Propulsion | VARCHAR(100) | Propulsion system (steam turbine, electric motor, etc.) |
| Guidance | VARCHAR(100) | Guidance system (straight-running, acoustic, wire, active/passive sonar) |
| Launch_Platform | VARCHAR(200) | Compatible platforms (surface ships, submarines, aircraft) |
| Modded | TINYINT | 0 = historical, 1 = fictional/generated |
| Notes | TEXT | Additional information, ships used, performance notes |

**Total Entries**: 0 torpedoes
**Planned Coverage**: 1890-1990
**ID Allocation**:
- USA: 1000-1099
- British: 1100-1199
- German: 1200-1299
- Japanese: 1300-1399
- Soviet: 1400-1499
- French: 1500-1599
- Italian: 1600-1699

| Torpedo_ID | Country | Designation | Type | Year_Introduced | Diameter_IN | Length_FT | Weight_LBS | Warhead_LBS | Warhead_Type | Max_Speed_KTS | Max_Range_YDS | Running_Depth_FT | Propulsion | Guidance | Launch_Platform | Modded | Notes |
|------------|---------|-------------|------|-----------------|-------------|-----------|------------|-------------|--------------|---------------|---------------|------------------|------------|----------|-----------------|--------|-------|
| | | | | | | | | | | | | | | | | | |
| 1000 | USA | Whitehead Torpedo (1890) | Steam | 1890 | 18.0 | 15.0 | 38880 | 300 | Guncotton | 33.5 | 2500 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 0 |
| 1001 | USA | Howell Torpedo | Flywheel | 1889 | 18.0 | 14.9 | 38621 | 300 | Guncotton | 25.0 | 2900 | 15-50 | Flywheel energy storage | Straight-running (gyroscope) | Surface ships, submarines | 0 | 1 |
| 1002 | USA | Whitehead Mark 1 | Steam | 1892 | 18.0 | 15.2 | 39398 | 300 | Guncotton | 33.8 | 2800 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1003 | USA | Bliss-Leavitt Mark 1 | Steam | 1904 | 18.0 | 16.4 | 42509 | 300 | Guncotton | 35.6 | 4600 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1004 | USA | Bliss-Leavitt Mark 3 | Steam | 1908 | 18.0 | 16.8 | 43546 | 300 | Guncotton | 36.2 | 5200 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1005 | USA | Mark 7 | Steam | 1912 | 21.0 | 17.2 | 60682 | 560 | Guncotton | 36.8 | 5800 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1006 | USA | Mark 8 | Steam | 1915 | 21.0 | 17.5 | 61740 | 575 | TNT | 37.2 | 6250 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1007 | USA | Mark 9 | Steam | 1916 | 21.0 | 17.6 | 62093 | 580 | TNT | 37.4 | 6400 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1008 | USA | Mark 10 | Steam | 1920 | 21.0 | 18.0 | 63504 | 600 | TNT | 38.0 | 7000 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1009 | USA | Mark 11 | Steam | 1922 | 21.0 | 18.2 | 64210 | 610 | TNT | 38.3 | 7300 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1010 | USA | Mark 12 | Steam | 1927 | 21.0 | 18.7 | 65974 | 635 | TNT | 39.0 | 8050 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1011 | USA | Mark 13 (Early) | Steam | 1938 | 21.0 | 19.8 | 69854 | 690 | TNT | 40.7 | 9700 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1012 | USA | Mark 14 Mod 0 | Steam | 1931 | 21.0 | 19.1 | 67385 | 655 | TNT | 39.6 | 8650 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1013 | USA | Mark 15 Mod 0 | Steam | 1938 | 21.0 | 19.8 | 69854 | 690 | TNT | 40.7 | 9700 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1014 | USA | Mark 14 Mod 3 (Depth Fix) | Steam | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 41.3 | 10300 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1015 | USA | Mark 14 Mod 4 (Magnetic Fix) | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | Torpex | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1016 | USA | Mark 14 Mod 5 (Contact Fix) | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | Torpex | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1017 | USA | Mark 13 Mod 1 (Improved) | Steam | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 41.3 | 10300 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1018 | USA | Mark 13 Mod 2 (Final) | Steam | 1944 | 21.0 | 22.4 | 79027 | 720 | Torpex | 41.6 | 10600 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1019 | USA | Mark 15 Mod 3 | Steam | 1944 | 21.0 | 22.4 | 79027 | 720 | Torpex | 41.6 | 10600 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1020 | USA | Mark 16 | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | Torpex | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1021 | USA | Mark 17 | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | Torpex | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1022 | USA | Mark 18 | Electric | 1943 | 21.0 | 22.4 | 79027 | 715 | Torpex | 28.9 | 8600 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1023 | USA | Mark 24 "Fido" | Acoustic | 1943 | 21.0 | 23.1 | 81673 | 715 | Torpex | 30.0 | 5000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 8 |
| 1024 | USA | Mark 27 | Acoustic | 1945 | 21.0 | 23.2 | 82026 | 725 | Torpex | 30.4 | 5600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 7 |
| 1025 | USA | Mark 28 | Acoustic | 1946 | 21.0 | 23.3 | 82202 | 730 | Torpex | 30.6 | 5900 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 8 |
| 1026 | USA | Mark 32 | Electric | 1946 | 21.0 | 22.4 | 79027 | 730 | Torpex | 29.8 | 9200 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 9 |
| 1027 | USA | Mark 35 | Acoustic | 1949 | 21.0 | 23.4 | 82732 | 745 | Torpex | 31.2 | 6800 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1028 | USA | Mark 37 | Acoustic | 1956 | 21.0 | 23.8 | 83966 | 780 | Torpex | 32.6 | 8900 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1029 | USA | Mark 39 (Mod Mark 37) | Acoustic | 1957 | 21.0 | 23.9 | 84143 | 785 | Torpex | 32.8 | 9200 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1030 | USA | Mark 41 | Acoustic | 1957 | 21.0 | 23.9 | 84143 | 785 | Torpex | 32.8 | 9200 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1031 | USA | Mark 43 | Acoustic | 1961 | 21.0 | 24.1 | 84848 | 805 | HBX | 33.6 | 10400 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 9 |
| 1032 | USA | Mark 44 | Acoustic | 1962 | 21.0 | 24.1 | 85025 | 810 | HBX | 33.8 | 10700 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1033 | USA | Mark 45 ASTOR | Nuclear | 1963 | 21.0 | 22.4 | 79027 | 815 | HBX | 37.3 | 10300 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 16 |
| 1034 | USA | Mark 46 Mod 0 | Acoustic | 1965 | 21.0 | 24.2 | 85554 | 825 | HBX | 34.4 | 11600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1035 | USA | Mark 46 Mod 1 | Acoustic | 1967 | 21.0 | 24.4 | 85907 | 835 | HBX | 34.8 | 12200 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 9 |
| 1036 | USA | Mark 46 Mod 2 | Acoustic | 1972 | 21.0 | 22.5 | 79380 | 860 | HBX | 35.8 | 13700 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 9 |
| 1037 | USA | Mark 46 Mod 5 | Acoustic | 1979 | 21.0 | 22.5 | 79380 | 895 | HBX | 37.2 | 15800 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1038 | USA | Mark 48 Mod 0 | Wire-Guided | 1972 | 21.0 | 22.5 | 79380 | 860 | HBX | 47.1 | 23500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 18 |
| 1039 | USA | Mark 48 Mod 1 | Wire-Guided | 1975 | 21.0 | 22.5 | 79380 | 875 | HBX | 48.0 | 25000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 16 |
| 1040 | USA | Mark 48 Mod 3 | Wire-Guided | 1977 | 21.0 | 22.5 | 79380 | 885 | HBX | 48.6 | 26000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 16 |
| 1041 | USA | Mark 48 ADCAP (Mod 4) | Wire-Guided | 1985 | 21.0 | 22.5 | 79380 | 900 | HBX | 51.0 | 30000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 20 |
| 1042 | USA | Mark 48 ADCAP (Mod 5) | Wire-Guided | 1988 | 21.0 | 22.5 | 79380 | 900 | HBX | 51.9 | 31500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 18 |
| 1043 | USA | Mark 48 ADCAP (Mod 6) | Wire-Guided | 1990 | 21.0 | 22.5 | 79380 | 900 | HBX | 52.5 | 32500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 20 |
| 1044 | USA | Mark 50 | Acoustic | 1989 | 21.0 | 22.5 | 79380 | 900 | HBX | 39.2 | 18800 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 14 |
| 1045 | USA | Mark 46 Mod 5A(S) | Acoustic | 1987 | 21.0 | 22.5 | 79380 | 900 | HBX | 38.8 | 18200 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1046 | USA | Mark 46 NEARTIP Mod 5A/S | Acoustic | 1989 | 21.0 | 22.5 | 79380 | 900 | HBX | 39.2 | 18800 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1047 | USA | Mark 37C | Acoustic | 1960 | 21.0 | 24.0 | 84672 | 800 | HBX | 33.4 | 10100 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1048 | USA | Mark 48 Mod 4 (Export) | Wire-Guided | 1986 | 21.0 | 22.5 | 79380 | 900 | HBX | 51.3 | 30500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 18 |
| 1049 | USA | Mark 60 CAPTOR | Mine-Torpedo | 1979 | 21.0 | 22.5 | 79380 | 895 | HBX | 38.9 | 11900 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 16 |
| 1050 | USA | ALWT (Advanced Lightweight) | Acoustic | 1985 | 21.0 | 22.5 | 79380 | 900 | HBX | 38.4 | 17600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 18 |
| 1051 | USA | Mark 51 | Acoustic | 1960 | 21.0 | 24.0 | 84672 | 800 | HBX | 33.4 | 10100 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1052 | USA | Mark 52 | Electric | 1965 | 21.0 | 22.4 | 79027 | 825 | HBX | 35.5 | 13000 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 14 |
| 1053 | USA | Mark 53 | Wire-Guided | 1970 | 21.0 | 22.5 | 79380 | 850 | HBX | 46.5 | 22500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 16 |
| 1054 | USA | Mark 25 "Atomic Astor" | Nuclear | 1945 | 21.0 | 22.4 | 79027 | 725 | Torpex | 35.5 | 8500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 24 |
| 1055 | USA | Mark 30 | Exercise | 1945 | 21.0 | 22.4 | 79027 | 725 | Torpex | 35.5 | 8500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1056 | USA | Mark 33 | Exercise | 1946 | 21.0 | 22.4 | 79027 | 730 | Torpex | 35.6 | 8600 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1057 | USA | Mark 34 | Exercise | 1950 | 21.0 | 22.4 | 79027 | 750 | Torpex | 36.0 | 9000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1058 | USA | Mark 36 | Exercise | 1955 | 21.0 | 22.4 | 79027 | 775 | Torpex | 36.5 | 9500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1059 | USA | Mark 40 | Exercise | 1958 | 21.0 | 22.4 | 79027 | 790 | Torpex | 36.8 | 9800 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1060 | USA | MK-59 | Exercise | 1970 | 21.0 | 22.5 | 79380 | 850 | HBX | 38.0 | 11000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1061 | USA | MK-48 EXTORP | Exercise | 1980 | 21.0 | 22.5 | 79380 | 900 | HBX | 39.0 | 12000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 8 |
| 1100 | British | Whitehead Torpedo (Original) | Compressed Air | 1866 | 18.0 | 12.6 | 32659 | 300 | Guncotton | 27.6 | 800 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 0 |
| 1101 | British | Whitehead Mark I | Compressed Air | 1871 | 18.0 | 13.1 | 33955 | 300 | Guncotton | 28.1 | 1100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 1 |
| 1102 | British | Whitehead Mark II | Compressed Air | 1876 | 18.0 | 13.6 | 35251 | 300 | Guncotton | 28.6 | 1600 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1103 | British | Whitehead Mark III | Compressed Air | 1882 | 18.0 | 14.2 | 36806 | 300 | Guncotton | 29.2 | 2200 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1104 | British | Whitehead Mark IV | Steam | 1886 | 18.0 | 14.6 | 37843 | 300 | Guncotton | 32.9 | 1900 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1105 | British | 18" Mark V | Steam | 1895 | 18.0 | 15.5 | 40176 | 300 | Guncotton | 34.2 | 3250 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1106 | British | 18" Mark VI | Steam | 1900 | 18.0 | 16.0 | 41472 | 300 | Guncotton | 35.0 | 4000 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1107 | British | 21" Mark I | Steam | 1908 | 18.0 | 16.8 | 43546 | 300 | Guncotton | 36.2 | 5200 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1108 | British | 21" Mark II | Steam | 1914 | 21.0 | 17.4 | 61387 | 570 | Guncotton | 37.1 | 6100 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1109 | British | 18" Mark VII | Steam | 1915 | 18.0 | 17.5 | 45360 | 300 | TNT | 37.2 | 6250 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1110 | British | 21" Mark III | Steam | 1916 | 21.0 | 17.6 | 62093 | 580 | TNT | 37.4 | 6400 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1111 | British | 21" Mark IV | Steam | 1918 | 21.0 | 17.8 | 62798 | 590 | TNT | 37.7 | 6700 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1112 | British | 18" Mark VIII | Steam | 1918 | 18.0 | 17.8 | 46138 | 300 | TNT | 37.7 | 6700 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1113 | British | 21" Mark V | Steam | 1920 | 21.0 | 18.0 | 63504 | 600 | TNT | 38.0 | 7000 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1114 | British | 21" Mark VI | Steam | 1925 | 21.0 | 18.5 | 65268 | 625 | TNT | 38.8 | 7750 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1115 | British | 21" Mark VII | Steam | 1928 | 21.0 | 18.8 | 66326 | 640 | TNT | 39.2 | 8200 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1116 | British | 21" Mark VIII | Steam | 1927 | 21.0 | 18.7 | 65974 | 635 | TNT | 39.0 | 8050 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1117 | British | 21" Mark VIII** | Steam | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 41.3 | 10300 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1118 | British | 21" Mark IX | Steam | 1930 | 21.0 | 19.0 | 67032 | 650 | TNT | 39.5 | 8500 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1119 | British | 21" Mark IX** | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1120 | British | 18" Mark X | Aerial | 1932 | 18.0 | 19.2 | 49766 | 300 | TNT | 34.2 | 7200 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1121 | British | 18" Mark XI | Aerial | 1935 | 18.0 | 19.5 | 50544 | 300 | TNT | 34.5 | 7500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1122 | British | 18" Mark XII | Aerial | 1938 | 18.0 | 19.8 | 51322 | 300 | TNT | 34.8 | 7800 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1123 | British | 18" Mark XV (Aerial) | Aerial | 1943 | 18.0 | 20.0 | 51840 | 300 | TNT | 35.3 | 3300 | 15-50 | Unknown | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 5 |
| 1124 | British | 21" Mark X | Steam | 1935 | 21.0 | 19.5 | 68796 | 675 | TNT | 40.2 | 9250 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1125 | British | 21" Mark XI | Steam | 1937 | 21.0 | 19.7 | 69502 | 685 | TNT | 40.5 | 9550 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1126 | British | 21" Mark XII | Steam | 1939 | 21.0 | 19.9 | 70207 | 695 | TNT | 40.9 | 9850 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1127 | British | 21" Mark XIII | Oxygen (Experimental) | 1935 | 21.0 | 19.5 | 68796 | 675 | TNT | 34.5 | 7500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 12 |
| 1128 | British | 21" Mark XIV | Electric | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 28.9 | 8600 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1129 | British | 21" Mark XV (Sub) | Steam | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 41.3 | 10300 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1130 | British | 21" Mark XVI | Electric | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 29.2 | 8800 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1131 | British | 21" Mark XVII | Hydrogen Peroxide | 1945 | 21.0 | 22.4 | 79027 | 725 | TNT | 35.5 | 8500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 9 |
| 1132 | British | Mark 18 | Acoustic | 1946 | 21.0 | 23.3 | 82202 | 730 | TNT | 30.6 | 5900 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 8 |
| 1133 | British | Mark 19 | Acoustic | 1948 | 21.0 | 23.4 | 82555 | 740 | TNT | 31.0 | 6500 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 8 |
| 1134 | British | Mark 20 | Acoustic | 1955 | 21.0 | 23.8 | 83790 | 775 | TNT | 32.4 | 8600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1135 | British | Mark 20S | Acoustic | 1957 | 21.0 | 23.9 | 84143 | 785 | TNT | 32.8 | 9200 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 9 |
| 1136 | British | Mark 21 | Electric | 1948 | 21.0 | 22.4 | 79027 | 740 | TNT | 30.4 | 9600 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 9 |
| 1137 | British | Mark 22 | Acoustic | 1952 | 21.0 | 23.6 | 83261 | 760 | TNT | 31.8 | 7700 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1138 | British | Mark 23 | Acoustic | 1959 | 21.0 | 23.9 | 84496 | 795 | TNT | 33.2 | 9800 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1139 | British | Mark 24 Tigerfish Mod 0 | Wire-Guided | 1974 | 21.0 | 22.5 | 79380 | 870 | HBX | 47.7 | 24500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 16 |
| 1140 | British | Mark 24 Tigerfish Mod 1 | Wire-Guided | 1980 | 21.0 | 22.5 | 79380 | 900 | HBX | 49.5 | 27500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 14 |
| 1141 | British | Mark 24 Tigerfish Mod 2 | Wire-Guided | 1986 | 21.0 | 22.5 | 79380 | 900 | HBX | 51.3 | 30500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 15 |
| 1142 | British | Stingray Mod 0 | Acoustic | 1983 | 21.0 | 22.5 | 79380 | 900 | HBX | 38.0 | 17000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1143 | British | Stingray Mod 1 | Acoustic | 1988 | 21.0 | 22.5 | 79380 | 900 | HBX | 39.0 | 18500 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1144 | British | Spearfish | Wire-Guided | 1988 | 21.0 | 22.5 | 79380 | 900 | HBX | 51.9 | 31500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 20 |
| 1145 | British | Spearfish Mod 1 | Wire-Guided | 1992 | 21.0 | 22.5 | 79380 | 900 | HBX | 53.1 | 33500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 18 |
| 1146 | British | Mark 20E | Acoustic | 1960 | 21.0 | 24.0 | 84672 | 800 | HBX | 33.4 | 10100 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 9 |
| 1147 | British | Mark 23E | Acoustic | 1965 | 21.0 | 24.2 | 85554 | 825 | HBX | 34.4 | 11600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1148 | British | Mark 24 Tiger Mk 1 (Export) | Wire-Guided | 1978 | 21.0 | 22.5 | 79380 | 890 | HBX | 48.9 | 26500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 14 |
| 1149 | British | Sting Ray Export | Acoustic | 1985 | 21.0 | 22.5 | 79380 | 900 | HBX | 38.4 | 17600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1150 | British | Practice Torpedo Mark I | Exercise | 1910 | 21.0 | 17.0 | 59976 | 0 | Guncotton | 32.0 | 5000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 1 |
| 1151 | British | Practice Torpedo Mark II | Exercise | 1925 | 21.0 | 18.5 | 65268 | 0 | TNT | 33.5 | 6500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1152 | British | Exercise Torpedo Mark III | Exercise | 1945 | 21.0 | 22.4 | 79027 | 725 | TNT | 35.5 | 8500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1153 | British | Mark 20 Exercise | Exercise | 1960 | 21.0 | 22.4 | 79027 | 800 | HBX | 37.0 | 10000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1154 | British | Tigerfish Exercise | Exercise | 1980 | 21.0 | 22.5 | 79380 | 900 | HBX | 39.0 | 12000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1155 | British | Spearfish Exercise | Exercise | 1990 | 21.0 | 22.5 | 79380 | 900 | HBX | 40.0 | 13000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1156 | British | Mark 25 | Rocket | 1950 | 21.0 | 22.4 | 79027 | 750 | TNT | 36.0 | 9000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 14 |
| 1157 | British | Mk 30 "Grog" | Nuclear | 1955 | 21.0 | 22.4 | 79027 | 775 | TNT | 36.5 | 9500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 20 |
| 1200 | German | Schwarzkopf Torpedo C/73 | Compressed Air | 1873 | 18.0 | 13.3 | 34474 | 300 | Guncotton | 28.3 | 1300 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 0 |
| 1201 | German | Schwarzkopf C/81 | Compressed Air | 1881 | 18.0 | 14.1 | 36547 | 300 | Guncotton | 29.1 | 2100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 1 |
| 1202 | German | Schwarzkopf C/88 | Steam | 1888 | 18.0 | 14.8 | 38362 | 300 | Guncotton | 33.2 | 2200 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1203 | German | C/91 | Steam | 1891 | 18.0 | 15.1 | 39139 | 300 | Guncotton | 33.6 | 2650 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1204 | German | C/96 | Steam | 1896 | 18.0 | 15.6 | 40435 | 300 | Guncotton | 34.4 | 3400 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1205 | German | C/03 | Steam | 1903 | 18.0 | 16.3 | 42250 | 300 | Guncotton | 35.5 | 4450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1206 | German | C/06 | Steam | 1906 | 18.0 | 16.6 | 43027 | 300 | Guncotton | 35.9 | 4900 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1207 | German | C/06D | Steam | 1910 | 21.0 | 17.0 | 59976 | 550 | Guncotton | 36.5 | 5500 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1208 | German | C/09 | Steam | 1909 | 18.0 | 16.9 | 43805 | 300 | Guncotton | 36.4 | 5350 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1209 | German | C/12 | Steam | 1912 | 21.0 | 17.2 | 60682 | 560 | Guncotton | 36.8 | 5800 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1210 | German | G6 | Steam | 1915 | 21.0 | 17.5 | 61740 | 575 | TNT | 37.2 | 6250 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1211 | German | G7 (WWI) | Steam | 1916 | 21.0 | 17.6 | 62093 | 580 | TNT | 37.4 | 6400 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1212 | German | H7 | Steam | 1917 | 21.0 | 17.7 | 62446 | 585 | TNT | 37.5 | 6550 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1213 | German | H8 | Steam | 1918 | 21.0 | 17.8 | 62798 | 590 | TNT | 37.7 | 6700 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1214 | German | G7 (1928) | Steam | 1928 | 21.0 | 18.8 | 66326 | 640 | TNT | 39.2 | 8200 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1215 | German | G7a (Prototype) | Steam | 1934 | 21.0 | 19.4 | 68443 | 670 | TNT | 40.1 | 9100 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1216 | German | G7e (Prototype) | Electric | 1936 | 21.0 | 19.6 | 69149 | 680 | TNT | 26.8 | 7200 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 9 |
| 1217 | German | G7a (TI) | Steam | 1939 | 21.0 | 19.9 | 70207 | 695 | TNT | 40.9 | 9850 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1218 | German | G7e (TII) | Electric | 1940 | 21.0 | 22.4 | 79027 | 700 | TNT | 28.0 | 8000 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1219 | German | G7a (TI) Mod 1 | Steam | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 41.3 | 10300 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1220 | German | G7e (TII) Mod 1 | Electric | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 28.6 | 8400 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1221 | German | G7es (TIII) | Electric | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 28.9 | 8600 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 8 |
| 1222 | German | G7e (TIIIa) | Electric | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 28.9 | 8600 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1223 | German | G7a (TI) Final | Steam | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 41.6 | 10600 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1224 | German | T5 Zaunkönig (Wren) | Acoustic | 1943 | 21.0 | 23.1 | 81673 | 715 | TNT | 30.0 | 5000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1225 | German | T5 Zaunkönig II | Acoustic | 1944 | 21.0 | 23.2 | 81850 | 720 | TNT | 30.2 | 5300 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 9 |
| 1226 | German | T11 | Acoustic | 1944 | 21.0 | 23.2 | 81850 | 720 | TNT | 30.2 | 5300 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1227 | German | T4 Falke (Falcon) | Acoustic | 1943 | 21.0 | 23.1 | 81673 | 715 | TNT | 30.0 | 5000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1228 | German | T10 | Acoustic | 1943 | 21.0 | 23.1 | 81673 | 715 | TNT | 30.0 | 5000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1229 | German | LuT (Lagenunabhängiger Torpedo) | Pattern | 1942 | 21.0 | 22.4 | 79027 | 710 | TNT | 35.2 | 8200 | 15-50 | Unknown | Pattern-running (circular/zigzag) | Surface ships, submarines | 0 | 9 |
| 1230 | German | FAT (Flächenabsuchender Torpedo) | Pattern | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 35.3 | 8300 | 15-50 | Unknown | Pattern-running (circular/zigzag) | Surface ships, submarines | 0 | 9 |
| 1231 | German | G7ut Steinwal (Stone Whale) | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1232 | German | G7a(T) | Steam | 1943 | 21.0 | 22.4 | 79027 | 715 | TNT | 41.5 | 10450 | 15-50 | Steam turbine, wet-heater | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1233 | German | G7v Dachshund | Electric | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 29.2 | 8800 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 8 |
| 1234 | German | G7eT1 | Electric | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 29.2 | 8800 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1235 | German | G7e/T12 | Hydrogen Peroxide | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 35.4 | 8400 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 14 |
| 1236 | German | Zaunkönig Draht (T6) | Wire-Guided | 1944 | 21.0 | 22.5 | 79380 | 720 | TNT | 38.7 | 9500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 16 |
| 1237 | German | Spinne (Spider) | Acoustic | 1945 | 21.0 | 23.2 | 82026 | 725 | TNT | 30.4 | 5600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1238 | German | G7e/T13 | Acoustic | 1945 | 21.0 | 23.2 | 82026 | 725 | TNT | 30.4 | 5600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 11 |
| 1239 | German | Seal DM1 | Acoustic | 1960 | 21.0 | 24.0 | 84672 | 800 | HBX | 33.4 | 10100 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 10 |
| 1240 | German | Seal DM2 | Acoustic | 1965 | 21.0 | 24.2 | 85554 | 825 | HBX | 34.4 | 11600 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1241 | German | SUT (Surface and Underwater Target) | Wire-Guided | 1967 | 21.0 | 22.5 | 79380 | 835 | HBX | 45.6 | 21000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships (destroyers, cruisers) | 0 | 16 |
| 1242 | German | SUT Mod 1 | Wire-Guided | 1970 | 21.0 | 22.5 | 79380 | 850 | HBX | 46.5 | 22500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 15 |
| 1243 | German | AEG Seal Mod 2 | Acoustic | 1972 | 21.0 | 22.5 | 79380 | 860 | HBX | 35.8 | 13700 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1244 | German | G7 Übung (Exercise) | Exercise | 1936 | 21.0 | 19.6 | 69149 | 680 | TNT | 34.6 | 7600 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1245 | German | G7e Übung | Exercise | 1940 | 21.0 | 22.4 | 79027 | 700 | TNT | 35.0 | 8000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1246 | German | Seal Exercise | Exercise | 1965 | 21.0 | 22.4 | 79027 | 825 | HBX | 37.5 | 10500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1247 | German | SUT Exercise | Exercise | 1975 | 21.0 | 22.5 | 79380 | 875 | HBX | 38.5 | 11500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1248 | German | T7 Adler (Eagle) | Acoustic | 1944 | 21.0 | 23.2 | 81850 | 720 | TNT | 30.2 | 5300 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 14 |
| 1249 | German | T8 Wren | Acoustic | 1944 | 21.0 | 23.2 | 81850 | 720 | TNT | 30.2 | 5300 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 13 |
| 1250 | German | T14 | Rocket | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 35.4 | 8400 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 18 |
| 1251 | German | G7e/T15 Walter | HTP | 1945 | 21.0 | 22.4 | 79027 | 725 | TNT | 35.5 | 8500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 20 |
| 1252 | German | Barracuda | Nuclear | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 35.4 | 8400 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 24 |
| 1253 | German | Dackel (Dachshund II) | Electric | 1945 | 21.0 | 22.4 | 79027 | 725 | TNT | 29.5 | 9000 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 10 |
| 1300 | Japanese | Type 28 No.1 | Compressed Air | 1895 | 18.0 | 15.5 | 40176 | 300 | Guncotton | 30.5 | 3500 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 0 |
| 1301 | Japanese | Type 31 | Compressed Air | 1898 | 18.0 | 15.8 | 40954 | 300 | Guncotton | 30.8 | 3800 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1302 | Japanese | Type 34 | Compressed Air | 1901 | 18.0 | 16.1 | 41731 | 300 | Guncotton | 31.1 | 4100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1303 | Japanese | Type 38 | Compressed Air | 1905 | 18.0 | 16.5 | 42768 | 300 | Guncotton | 31.5 | 4500 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 4 |
| 1304 | Japanese | Type 43 Year 2 | Compressed Air | 1910 | 21.0 | 17.0 | 59976 | 550 | Guncotton | 32.0 | 5000 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1305 | Japanese | Type 44 Year 3 | Compressed Air | 1911 | 21.0 | 17.1 | 60329 | 555 | Guncotton | 32.1 | 5100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 5 |
| 1306 | Japanese | Type 6 (Submarine) | Compressed Air | 1917 | 21.0 | 17.7 | 62446 | 585 | TNT | 32.7 | 5700 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Submarines | 0 | 6 |
| 1307 | Japanese | Type 8 No.1 | Compressed Air | 1919 | 21.0 | 17.9 | 63151 | 595 | TNT | 32.9 | 5900 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1308 | Japanese | Type 8 No.2 | Compressed Air | 1920 | 21.0 | 18.0 | 63504 | 600 | TNT | 33.0 | 6000 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1309 | Japanese | Type 8 No.4 | Alcohol | 1922 | 21.0 | 18.2 | 64210 | 610 | TNT | 38.3 | 7300 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1310 | Japanese | Type 89 | Alcohol | 1929 | 21.0 | 18.9 | 66679 | 645 | TNT | 39.4 | 8350 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 8 |
| 1311 | Japanese | Type 90 (24-inch) | Alcohol | 1930 | 24.0 | 19.0 | 87552 | 900 | TNT | 39.5 | 8500 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 9 |
| 1312 | Japanese | Oxygen Torpedo Prototype | Oxygen | 1931 | 24.0 | 29.5 | 135936 | 900 | TNT | 48.8 | 34000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 12 |
| 1313 | Japanese | Type 90 Mod 1 | Oxygen | 1932 | 24.0 | 29.5 | 135936 | 900 | TNT | 48.9 | 34500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 10 |
| 1314 | Japanese | Type 90 Mod 2 | Oxygen | 1933 | 24.0 | 29.5 | 135936 | 900 | TNT | 49.0 | 35000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 11 |
| 1315 | Japanese | Type 93 Model 1 (Mod 1) | Oxygen | 1933 | 24.0 | 29.5 | 135936 | 900 | TNT | 49.0 | 35000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 14 |
| 1316 | Japanese | Type 93 Model 1 (Mod 2) | Oxygen | 1935 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.2 | 36000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 15 |
| 1317 | Japanese | Type 93 Model 2 (Mod 3) | Oxygen | 1938 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.5 | 37500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 16 |
| 1318 | Japanese | Type 93 Model 3 (Mod 3) | Oxygen | 1943 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.0 | 40000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 16 |
| 1319 | Japanese | Type 93 Pure Oxygen Mk3 | Oxygen | 1944 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.1 | 40500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 17 |
| 1320 | Japanese | Type 95 Mod 1 | Oxygen | 1935 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.2 | 36000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Submarines | 0 | 13 |
| 1321 | Japanese | Type 95 Mod 2 | Oxygen | 1938 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.5 | 37500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Submarines | 0 | 14 |
| 1322 | Japanese | Type 95 Mod 3 | Oxygen | 1942 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.9 | 39500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Submarines | 0 | 15 |
| 1323 | Japanese | Type 97 Mod 1 | Alcohol | 1933 | 24.0 | 19.3 | 88934 | 900 | TNT | 40.0 | 8950 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 10 |
| 1324 | Japanese | Type 97 Mod 2 | Alcohol | 1936 | 24.0 | 19.6 | 90317 | 900 | Type 97 | 40.4 | 9400 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 11 |
| 1325 | Japanese | Type 91 Mod 1 | Compressed Air | 1931 | 24.0 | 19.1 | 88013 | 900 | TNT | 34.1 | 2100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 10 |
| 1326 | Japanese | Type 91 Mod 2 | Compressed Air | 1941 | 24.0 | 24.8 | 114278 | 900 | Type 97 | 35.1 | 3100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 12 |
| 1327 | Japanese | Type 91 Mod 3 | Compressed Air | 1943 | 24.0 | 24.8 | 114278 | 900 | TNT | 35.3 | 3300 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 13 |
| 1328 | Japanese | Type 91 Mod 4 | Compressed Air | 1944 | 24.0 | 24.8 | 114278 | 900 | TNT | 35.4 | 3400 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 14 |
| 1329 | Japanese | Type 89 (Submarine) | Alcohol | 1932 | 21.0 | 19.2 | 67738 | 660 | TNT | 39.8 | 8800 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Submarines | 0 | 8 |
| 1330 | Japanese | Type 92 Mod 1 | Alcohol | 1935 | 21.0 | 19.5 | 68796 | 675 | Type 97 | 40.2 | 9250 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 9 |
| 1331 | Japanese | Type 92 Mod 2 | Alcohol | 1938 | 21.0 | 19.8 | 69854 | 690 | Type 97 | 40.7 | 9700 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 10 |
| 1332 | Japanese | Type 96 | Alcohol | 1936 | 21.0 | 19.6 | 69149 | 680 | Type 97 | 40.4 | 9400 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 8 |
| 1333 | Japanese | Type 97 (18-inch) | Alcohol | 1937 | 24.0 | 19.7 | 90778 | 900 | Type 97 | 40.5 | 9550 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 7 |
| 1334 | Japanese | Type 2 Mod 1 | Oxygen | 1942 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.9 | 39500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 12 |
| 1335 | Japanese | Type 2 Mod 2 | Oxygen | 1943 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.0 | 40000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 13 |
| 1336 | Japanese | Kaiten Type 1 | Oxygen | 1944 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.1 | 40500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Kaiten human torpedo (suicide weapon) | 0 | 15 |
| 1337 | Japanese | Kaiten Type 2 | Oxygen | 1944 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.1 | 40500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Kaiten human torpedo (suicide weapon) | 0 | 16 |
| 1338 | Japanese | Kaiten Type 4 | Oxygen | 1945 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.2 | 41000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Kaiten human torpedo (suicide weapon) | 0 | 17 |
| 1339 | Japanese | Type 43 (Acoustic Homing) | Acoustic | 1943 | 21.0 | 23.1 | 81673 | 715 | TNT | 30.0 | 5000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 14 |
| 1340 | Japanese | Type 43 Mod 1 | Acoustic | 1944 | 21.0 | 23.2 | 81850 | 720 | TNT | 30.2 | 5300 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 15 |
| 1341 | Japanese | Type 44 | Acoustic | 1944 | 21.0 | 23.2 | 81850 | 720 | TNT | 30.2 | 5300 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 16 |
| 1342 | Japanese | Type 45 Mod 1 | Wire-Guided | 1945 | 21.0 | 22.5 | 79380 | 725 | TNT | 39.0 | 10000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 17 |
| 1343 | Japanese | Type 72 | Electric | 1960 | 21.0 | 22.4 | 79027 | 800 | HBX | 34.0 | 12000 | 15-50 | Battery-electric motor | Straight-running (gyroscope) | Surface ships, submarines | 0 | 12 |
| 1344 | Japanese | Type 73 | Wire-Guided | 1967 | 21.0 | 22.5 | 79380 | 835 | HBX | 45.6 | 21000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 18 |
| 1345 | Japanese | Type 80 Mod 1 | Wire-Guided | 1970 | 21.0 | 22.5 | 79380 | 850 | HBX | 46.5 | 22500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 20 |
| 1346 | Japanese | Type 1 Land-Attack | Oxygen | 1942 | 24.0 | 29.5 | 135936 | 900 | Type 97 | 49.9 | 39500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 13 |
| 1347 | Japanese | Type 4 (Cruiser) | Oxygen | 1943 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.0 | 40000 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 14 |
| 1348 | Japanese | Type 6 (Battleship) | Oxygen | 1944 | 24.0 | 29.5 | 135936 | 900 | TNT | 50.1 | 40500 | 15-50 | Pure oxygen (Kerosene + O2) | Straight-running (gyroscope) | Surface ships, submarines | 0 | 15 |
| 1349 | Japanese | Type 44 Practice | Training | 1911 | 21.0 | 17.1 | 60329 | 0 | Guncotton | 32.1 | 5100 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 2 |
| 1350 | Japanese | Type 45 Practice | Training | 1920 | 21.0 | 18.0 | 63504 | 0 | TNT | 33.0 | 6000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 3 |
| 1351 | Japanese | Type 93 Practice | Training | 1935 | 24.0 | 19.5 | 89856 | 0 | Type 97 | 34.5 | 7500 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 6 |
| 1352 | Japanese | Type 91 Practice | Training | 1935 | 24.0 | 19.5 | 89856 | 0 | Type 97 | 34.5 | 2500 | 15-50 | Unknown | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 5 |
| 1353 | Japanese | Type 89 Export | Alcohol | 1936 | 21.0 | 19.6 | 69149 | 680 | Type 97 | 40.4 | 9400 | 15-50 | Alcohol-fueled burner | Straight-running (gyroscope) | Surface ships, submarines | 0 | 8 |
| 1354 | Japanese | Type 91 (Thailand) | Compressed Air | 1941 | 24.0 | 24.8 | 114278 | 900 | Type 97 | 35.1 | 3100 | 15-50 | Compressed air engine | Straight-running (gyroscope) | Aircraft (carrier-based) | 0 | 9 |
| 1355 | Japanese | Type 5 Mine-Layer | Special | 1940 | 21.0 | 22.4 | 79027 | 700 | Type 97 | 35.0 | 8000 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 10 |
| 1356 | Japanese | Type 3 ASW | Acoustic | 1943 | 21.0 | 23.1 | 81673 | 715 | TNT | 30.0 | 5000 | 15-50 | Electric motor | Passive acoustic homing | Surface ships, submarines | 0 | 12 |
| 1357 | Japanese | Type 7 (Depth Charge) | Special | 1944 | 21.0 | 22.4 | 79027 | 720 | TNT | 35.4 | 8400 | 15-50 | Unknown | Straight-running (gyroscope) | Surface ships, submarines | 0 | 10 |
| 1358 | Japanese | Type 89 Mod 1 (JMSDF) | Wire-Guided | 1975 | 21.0 | 22.5 | 79380 | 875 | HBX | 48.0 | 25000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 20 |
| 1359 | Japanese | GRX-2 Prototype | Wire-Guided | 1978 | 21.0 | 22.5 | 79380 | 890 | HBX | 48.9 | 26500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 21 |
| 1360 | Japanese | GRX-3 Advanced | Wire-Guided | 1980 | 21.0 | 22.5 | 79380 | 900 | HBX | 49.5 | 27500 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 22 |
| 1361 | Japanese | Type 89 Mod 2 | Wire-Guided | 1985 | 21.0 | 22.5 | 79380 | 900 | HBX | 51.0 | 30000 | 15-50 | Thermal (Otto fuel II) | Wire-guided + active/passive sonar | Surface ships, submarines | 0 | 23 |

**Example Entries** (for reference - not yet in database):

### USA Torpedoes
- **Mark 48 Mod 7** - Modern wire-guided acoustic homing torpedo, submarines
- **Mark 14** - WWII submarine torpedo (infamous for detonator problems)
- **Mark 15** - WWII surface ship torpedo
- **Mark 13** - WWII air-launched torpedo

### British Torpedoes
- **Mark VIII** - WWI/WWII submarine torpedo
- **Mark IX** - WWII surface ship torpedo
- **Mark XII** - Destroyer torpedo
- **Spearfish** - Modern wire-guided heavyweight

### German Torpedoes
- **G7a (TI)** - Steam torpedo, WWI/WWII
- **G7e (TII)** - Electric torpedo, wakeless
- **G7es (TIII)** - Pattern-running torpedo
- **Zaunkönig (T5)** - Acoustic homing torpedo

### Japanese Torpedoes
- **Type 93 "Long Lance"** - Oxygen-fueled, longest range torpedo of WWII
- **Type 95** - Submarine torpedo
- **Type 91** - Air-launched torpedo (Pearl Harbor)
- **Type 97** - Destroyer torpedo

---

<a name="torpedo-warheads-table"></a>
## Torpedo Warheads Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Warhead_ID | INT | Primary key |
| Torpedo_ID | INT | Foreign key to torpedoes table |
| Designation | VARCHAR(100) | Warhead designation |
| Explosive_Type | VARCHAR(50) | TNT, Torpex, HBX-3, Composition B, etc. |
| Weight_LBS | DECIMAL(7,2) | Total warhead weight |
| Explosive_Weight_LBS | DECIMAL(7,2) | Net explosive weight |
| TNT_Equivalent_LBS | DECIMAL(7,2) | TNT equivalent for comparison |
| Fuze_Type | VARCHAR(100) | Contact, magnetic, acoustic, proximity |
| Blast_Radius_FT | DECIMAL(6,1) | Effective blast radius |
| Armor_Penetration_IN | DECIMAL(5,1) | Armor penetration capability |
| Notes | TEXT | Additional information |

| Warhead_ID | Torpedo_ID | Designation | Explosive_Type | Weight_LBS | Explosive_Weight_LBS | TNT_Equivalent_LBS | Fuze_Type | Blast_Radius_FT | Armor_Penetration_IN | Notes |
|------------|------------|-------------|----------------|------------|----------------------|-------------------|-----------|-----------------|----------------------|-------|
| | | | | | | | | | | |

---

<a name="launch-systems-table"></a>
## Launch Systems Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Launcher_ID | INT | Primary key |
| Country | VARCHAR(50) | Nation |
| Designation | VARCHAR(100) | Launcher designation |
| Type | VARCHAR(50) | Fixed tubes, trainable tubes, drop chutes, aircraft rack |
| Torpedo_Diameter_IN | DECIMAL(5,2) | Compatible torpedo diameter |
| Tube_Count | INT | Number of tubes/rails in mount |
| Reload_Time_MIN | DECIMAL(5,1) | Reload time in minutes |
| Traverse_Range_DEG | INT | Traverse range (null for fixed/drop) |
| Platform_Type | VARCHAR(100) | Surface ship, submarine, aircraft |
| Year_Introduced | INT | Year entered service |
| Weight_TONS | DECIMAL(6,2) | System weight in tons |
| Modded | TINYINT | 0 = historical, 1 = fictional |
| Notes | TEXT | Ships/platforms used on |

| Launcher_ID | Country | Designation | Type | Torpedo_Diameter_IN | Tube_Count | Reload_Time_MIN | Traverse_Range_DEG | Platform_Type | Year_Introduced | Weight_TONS | Modded | Notes |
|-------------|---------|-------------|------|---------------------|------------|-----------------|-------------------|---------------|-----------------|-------------|--------|-------|
| | | | | | | | | | | | | |

---

## Future Expansion Notes

### Historical Priority Torpedoes
1. **USA**: Mark 48, Mark 46, Mark 14, Mark 15, Mark 13 (air), Mark 37
2. **British**: Mark VIII, Mark IX, Spearfish, Tigerfish, Stingray
3. **German**: G7a, G7e, T5 Zaunkönig, T11, G7es
4. **Japanese**: Type 93 Long Lance, Type 95, Type 91 (air), Type 89
5. **Soviet**: Type 53, Type 65, VA-111 Shkval, SET-65

### Torpedo Categories
- **Heavyweight** (21"-24"): Submarine-launched, long range, large warheads
- **Lightweight** (12"-18"): ASW, air-launched, shorter range
- **Midweight** (16"-19"): Versatile, surface/sub launch
- **Supercavitating** (Modern): Extremely high speed, rocket-propelled

### Propulsion Types
- **Steam**: Wet-heater, alcohol/oxygen (early WWI-WWII)
- **Electric**: Battery-powered, wakeless (WWII onward)
- **Oxygen**: Pure oxygen fuel (Japanese Type 93)
- **Thermal**: Otto fuel, monopropellant (modern)
- **Rocket**: Supercavitating torpedoes (Shkval)

### Guidance Systems
- **Straight-running**: Gyroscope, no homing
- **Pattern-running**: Circular/zigzag search patterns
- **Acoustic Passive**: Homes on target noise
- **Acoustic Active**: Active sonar pinging
- **Wire-guided**: Controlled from launch platform
- **Wake-homing**: Follows ship wake signature

---

## Database Status

**Current Status**: Empty - Ready for population
**Target Count**: 300-500 torpedoes across all nations
**Priority**: Historical WWII and modern systems

---

**Last Updated**: October 10, 2025
**Ready for Data Entry**: ✅
