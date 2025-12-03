# Naval Bombs Database

**Database Type**: Detailed specifications for aerial bombs used in WOS 2.3
**Coverage**: 1940-2025, all nations (USA, British, German, Japanese)
**Total Entries**: 107 bombs
**ID Range**: 9000-9499

## Overview

This database contains detailed specifications for aerial bombs spanning from WWII-era gravity bombs to modern precision-guided munitions. It includes general purpose bombs, laser-guided bombs (LGB), GPS-guided bombs (JDAM), nuclear weapons, cluster munitions, incendiary bombs, naval mines, and penetrators.

## Database Structure

| Field | Type | Unit | Description |
|-------|------|------|-------------|
| Bomb_ID | Integer | - | Unique identifier (9000-9499) |
| Nation | Text | - | USA, British, German, Japanese |
| Designation | Text | - | Official designation (AN-M64, GBU-12, Tallboy, etc.) |
| Bomb_Type | Text | - | GP Bomb, LGB, GPS-Guided, Nuclear, Cluster Bomb, Incendiary, Mine, Penetrator, etc. |
| Year | Integer | year | Year introduced |
| Weight | Decimal | kg | Total weight including guidance systems |
| Length | Decimal | m | Overall length |
| Diameter | Decimal | m | Body diameter |
| Explosive_Weight | Decimal | kg | High explosive filler weight (0 for nuclear) |
| Explosive_Type | Text | - | Tritonal, Comp B, H6, nuclear, napalm, etc. |
| Blast_Radius | Integer | m | Lethal blast radius |
| Penetration | Integer | mm | Armor penetration for AP/penetrator bombs |
| Guidance_Type | Text | - | None, Laser, GPS, TV, Radio, Inertial+GPS, Laser+GPS |
| Guidance_Accuracy | Integer | m | CEP (Circular Error Probable) in meters |
| Max_Range | Integer | km | Maximum release range for guided bombs |
| Terminal_Velocity | Integer | m/s | Impact velocity at release altitude |
| Fuse_Type | Text | - | Contact, Proximity, Delay, Variable |
| Delivery_Platform | Text | - | Fighter, Bomber, Attack, Multirole |
| Cost_USD | Integer | USD | Unit cost in USD |
| Production_Years | Text | - | Years in production |
| Variants | Text | - | Major variants and modifications |
| Historical_Notes | Text | - | Combat usage and development history |
| Modded | Integer | - | 0 = Historical, 1 = Modded |

## Bomb Categories

### General Purpose Bombs
- **ID Range**: Various (9000-9030s, 9200-9220s, 9300-9330s, 9400-9430s)
- **Examples**: AN-M series, Mk 80 series, SC series, Type 94/97/98/99
- **Characteristics**: High-explosive bombs for general targets, thin-walled casings

### Laser-Guided Bombs (LGB)
- **ID Range**: 9020s, 9230s, 9340s, 9440s
- **Examples**: Paveway I/II/III/IV, GBU-12/24
- **Characteristics**: Laser designation with semi-active homing, high precision

### GPS-Guided Bombs (JDAM)
- **ID Range**: 9050s-9060s, 9450s
- **Examples**: GBU-31/32/38/54, JDAM-ER
- **Characteristics**: GPS/INS guidance, all-weather capability, moderate cost

### Nuclear Bombs
- **ID Range**: 9090s, 9260s
- **Examples**: Mk 4/7/15/28, B61/B83, Blue Danube, WE.177
- **Characteristics**: Nuclear warheads, strategic deterrence, variable yields

### Cluster Munitions
- **ID Range**: 9080s, 9250s, 9360s, 9470s
- **Examples**: CBU-87/97/103/105, BL755, MW-1
- **Characteristics**: Multiple submunitions, area effect, anti-personnel/armor

### Heavy Bombs
- **ID Range**: 9210-9211, 9310
- **Examples**: Tallboy, Grand Slam, SC 1800
- **Characteristics**: Deep penetration, earthquake bombs, hardened targets

### Incendiary Bombs
- **ID Range**: 9100s, 9420s
- **Examples**: Mk 77/78, BLU-27, Type 3/100
- **Characteristics**: Napalm/thermite fill, anti-personnel, area denial

### Naval Mines
- **ID Range**: 9110s
- **Examples**: Mk 36/62/63/65 Quickstrike
- **Characteristics**: Air-dropped naval mines, magnetic/acoustic sensors

### Penetrators
- **ID Range**: 9120s, 9311
- **Examples**: BLU-109/116/122, PC 1400
- **Characteristics**: Hardened cases, bunker busting, delayed fuses

### Guided WWII Bombs
- **ID Range**: 9320-9321
- **Examples**: Fritz X, Hs 293
- **Characteristics**: First guided bombs, radio control, rocket boosters

## Data Sources

All data compiled from:
- Official military specifications and technical orders
- Combat reports and operational assessments
- Historical archives and development documents
- Federation of American Scientists (FAS) documentation
- Jane's Air-Launched Weapons
- Naval-encyclopedia.com

## Specification Notes

### Weight Estimates
- **GP Bombs**: Based on standard weight classes and explosive ratios
- **Guided Bombs**: Includes guidance kit weight added to base bomb
- **Nuclear Bombs**: Total weapon weight including physics package
- **Cluster Munitions**: Total weight with all submunitions

### Explosive Type Standards
- **Tritonal**: 80% TNT, 20% aluminum (WWII-era)
- **Comp B**: RDX/TNT mixture (1950s-1970s)
- **H6**: RDX/TNT/aluminum (modern high-performance)
- **PBXN**: Plastic-bonded explosive (modern insensitive)

### Guidance Accuracy Progression
- **Unguided**: 100-300m CEP
- **Laser-Guided**: 3-10m CEP
- **GPS-Guided**: 5-15m CEP
- **Laser+GPS**: 1-5m CEP

### Cost Estimates
- **Unguided GP**: $10,000-50,000
- **Laser Guidance Kit**: +$20,000-40,000
- **GPS Guidance Kit**: +$15,000-30,000
- **Dual-Mode**: +$40,000-80,000

## Database Entries

Entries sorted by Nation → Bomb_Type → Year

| Bomb_ID | Nation | Designation | Bomb_Type | Year | Weight | Length | Diameter | Explosive_Weight | Explosive_Type | Blast_Radius | Penetration | Guidance_Type | Guidance_Accuracy | Max_Range | Terminal_Velocity | Fuse_Type | Delivery_Platform | Cost_USD | Production_Years | Variants | Historical_Notes | Modded |
|---------|--------|-------------|-----------|------|--------|--------|----------|------------------|----------------|--------------|-------------|---------------|-------------------|-----------|-------------------|-----------|-------------------|----------|------------------|----------|------------------|--------|
| 9000 | USA | AN-M30 | GP Bomb | 1940 | 45 | 1.73 | 0.254 | 20 | Tritonal | 49 | 0 | None | 200 | 5 | 154 | Contact/Delay | Attack Aircraft | 2900 | 1940-1950 | Standard | Standard operational bomb | 0 |
| 9001 | USA | AN-M64 | GP Bomb | 1941 | 227 | 2.63 | 0.292 | 102 | Tritonal | 95 | 0 | None | 200 | 5 | 172 | Contact/Delay | Attack Aircraft | 6540 | 1941-1951 | Standard | Standard operational bomb | 0 |
| 9002 | USA | AN-M65 | GP Bomb | 1942 | 454 | 3.77 | 0.316 | 204 | Tritonal | 125 | 0 | None | 200 | 5 | 195 | Contact/Delay | Attack Aircraft | 11080 | 1942-1952 | Standard | Standard operational bomb | 0 |
| 9003 | USA | AN-M66 | GP Bomb | 1943 | 907 | 6.04 | 0.345 | 408 | Tritonal | 166 | 0 | None | 200 | 5 | 240 | Contact/Delay | Fighter-Bomber | 20140 | 1943-1953 | Standard | Standard operational bomb | 0 |
| 9010 | USA | Mk 81 | GP Bomb | 1950 | 113 | 2.06 | 0.273 | 50 | Tritonal | 71 | 0 | None | 200 | 5 | 161 | Contact/Delay | Attack Aircraft | 4260 | 1950-1975 | Standard | Standard operational bomb | 0 |
| 9011 | USA | Mk 82 | GP Bomb | 1952 | 227 | 2.63 | 0.292 | 102 | Tritonal | 95 | 0 | None | 200 | 5 | 172 | Contact/Delay | Attack Aircraft | 6540 | 1952-1977 | Mk 82, BSU-86 Snakeye | Standard operational bomb | 0 |
| 9012 | USA | Mk 83 | GP Bomb | 1955 | 447 | 3.73 | 0.315 | 201 | Tritonal | 125 | 0 | None | 200 | 5 | 194 | Contact/Delay | Attack Aircraft | 10940 | 1955-1980 | Mk 83, BSU-85 Snakeye | Standard operational bomb | 0 |
| 9013 | USA | Mk 84 | GP Bomb | 1958 | 907 | 6.04 | 0.345 | 408 | Tritonal | 166 | 0 | None | 200 | 5 | 240 | Contact/Delay | Fighter-Bomber | 20140 | 1958-1983 | Mk 84, BSU-50 | Standard operational bomb | 0 |
| 9020 | USA | GBU-10 Paveway I | LGB | 1968 | 960 | 6.30 | 0.348 | 480 | Comp B | 177 | 0 | Laser | 10 | 20 | 246 | Contact/Delay | Fighter-Bomber | 68400 | 1968-1988 | Standard | Early laser-guided bomb, Vietnam War era | 0 |
| 9021 | USA | GBU-12 Paveway II | LGB | 1976 | 240 | 2.70 | 0.294 | 120 | Comp B | 101 | 0 | Laser | 10 | 15 | 174 | Contact/Delay | Attack Aircraft | 39600 | 1976-1996 | GBU-12A/B/C/D, Paveway II | Early laser-guided bomb, Vietnam War era | 0 |
| 9022 | USA | GBU-16 Paveway II | LGB | 1980 | 460 | 3.80 | 0.316 | 253 | H6 | 157 | 0 | Laser | 6 | 20 | 196 | Contact/Delay | Fighter/Attack | 48400 | 1980-2010 | Standard | Standard operational bomb | 0 |
| 9023 | USA | GBU-24 Paveway III | LGB | 1983 | 1020 | 6.60 | 0.351 | 561 | H6 | 216 | 0 | Laser | 6 | 25 | 252 | Contact/Delay | Multirole Fighter | 70800 | 1983-2013 | GBU-24A/B, Paveway III | Standard operational bomb | 0 |
| 9024 | USA | GBU-28 | Bunker Buster | 1991 | 2130 | 12.15 | 0.393 | 1171 | H6 | 290 | 6000 | None | 200 | 5 | 350 | Delayed | Bomber | 66900 | 1991-2021 | Standard | Bunker buster, used in Gulf War 1991 against hardened targets | 0 |
| 9030 | USA | Mk 117 | GP Bomb | 1960 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1960-1985 | Standard | Standard operational bomb | 0 |
| 9031 | USA | M117R | GP Bomb | 1970 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1970-1990 | Standard | Standard operational bomb | 0 |
| 9032 | USA | Mk 118 | Demolition Bomb | 1975 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1975-2000 | Standard | Standard operational bomb | 0 |
| 9040 | USA | GBU-15 | TV-Guided | 1975 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | TV | 15 | 10 | 175 | Contact/Delay | Attack Aircraft | 60000 | 1975-1995 | Standard | Standard operational bomb | 0 |
| 9041 | USA | AGM-62 Walleye | TV-Guided | 1967 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | TV | 15 | 10 | 175 | Contact/Delay | Attack Aircraft | 60000 | 1967-1987 | Standard | Standard operational bomb | 0 |
| 9050 | USA | GBU-31 JDAM | GPS-Guided | 1997 | 930 | 6.15 | 0.346 | 511 | H6 | 208 | 0 | GPS+INS | 13 | 20 | 243 | Contact/Delay | Multirole Fighter | 62200 | 1997-2025 | GBU-31(V)1/2/3/4 | Early JDAM system, revolutionized precision bombing | 0 |
| 9051 | USA | GBU-32 JDAM | GPS-Guided | 1999 | 470 | 3.85 | 0.317 | 258 | H6 | 158 | 0 | GPS+INS | 13 | 20 | 197 | Contact/Delay | Fighter/Attack | 43800 | 1999-2025 | Standard | Early JDAM system, revolutionized precision bombing | 0 |
| 9052 | USA | GBU-38 JDAM | GPS-Guided | 2001 | 240 | 2.70 | 0.294 | 132 | PBXN-109 | 115 | 0 | GPS+INS | 10 | 15 | 174 | Contact/Delay | Fighter/Attack | 34600 | 2001-Present | GBU-38(V)1/2/3 | Standard operational bomb | 0 |
| 9053 | USA | GBU-54 LJDAM | Laser/GPS | 2008 | 240 | 2.70 | 0.294 | 132 | PBXN-109 | 115 | 0 | Laser+GPS | 5 | 15 | 174 | Contact/Delay | Fighter/Attack | 69600 | 2008-Present | Standard | Standard operational bomb | 0 |
| 9054 | USA | GBU-56 LJDAM | Laser/GPS | 2010 | 470 | 3.85 | 0.317 | 258 | PBXN-109 | 151 | 0 | Laser+GPS | 3 | 20 | 197 | Contact/Delay | Fighter/Attack | 78800 | 2010-Present | Standard | Standard operational bomb | 0 |
| 9060 | USA | GBU-39 SDB | Small Diameter | 2006 | 130 | 2.15 | 0.277 | 71 | PBXN-109 | 90 | 0 | None | 200 | 5 | 163 | Contact/Delay | Fighter/Attack | 6900 | 2006-Present | Standard | Standard operational bomb | 0 |
| 9061 | USA | GBU-53 SDB II | Small Diameter | 2014 | 115 | 2.08 | 0.273 | 63 | PBXN-109 | 85 | 0 | None | 200 | 5 | 161 | Contact/Delay | Fighter/Attack | 6450 | 2014-Present | Standard | Standard operational bomb | 0 |
| 9070 | USA | GBU-57 MOP | Bunker Buster | 2011 | 13600 | 69.50 | 0.555 | 7480 | PBXN-109 | 584 | 60000 | None | 200 | 5 | 350 | Delayed | Heavy Bomber | 411000 | 2011-Present | Standard | Massive Ordnance Penetrator, largest conventional penetrator | 0 |
| 9080 | USA | CBU-87 | Cluster Bomb | 1986 | 430 | 3.63 | 0.587 | 172 | H6 | 134 | 0 | None | 200 | 5 | 115 | Proximity | Fighter/Attack | 15900 | 1986-2016 | Standard | Area effect munition, anti-personnel/armor | 0 |
| 9081 | USA | CBU-97 | Sensor Fused | 1992 | 430 | 3.65 | 0.314 | 236 | H6 | 152 | 0 | None | 200 | 5 | 193 | Contact/Delay | Fighter/Attack | 15900 | 1992-2022 | Standard | Standard operational bomb | 0 |
| 9082 | USA | CBU-103 | Cluster Bomb | 1997 | 430 | 3.63 | 0.587 | 172 | H6 | 134 | 0 | None | 200 | 5 | 115 | Proximity | Fighter/Attack | 15900 | 1997-2025 | Standard | Standard operational bomb | 0 |
| 9083 | USA | CBU-105 | Sensor Fused | 2001 | 430 | 3.65 | 0.314 | 236 | PBXN-109 | 146 | 0 | None | 200 | 5 | 193 | Contact/Delay | Fighter/Attack | 15900 | 2001-Present | Standard | Standard operational bomb | 0 |
| 9090 | USA | Mk 4 | Nuclear | 1949 | 4900 | 4.95 | 1.983 | 0 | Fission | 1500 | 0 | None | 200 | 5 | 350 | Airburst/Ground | Bomber | 8000000 | 1949-1974 | Standard | First-generation nuclear weapon, large warhead | 0 |
| 9091 | USA | Mk 7 | Nuclear | 1952 | 780 | 2.89 | 0.610 | 0 | Fission | 1500 | 0 | None | 200 | 5 | 228 | Airburst/Ground | Fighter-Bomber | 8000000 | 1952-1977 | Standard | First-generation nuclear weapon, large warhead | 0 |
| 9092 | USA | Mk 15 | Nuclear | 1955 | 3400 | 4.20 | 1.483 | 0 | Fission | 1500 | 0 | None | 200 | 5 | 350 | Airburst/Ground | Bomber | 8000000 | 1955-1980 | Standard | First-generation nuclear weapon, large warhead | 0 |
| 9093 | USA | Mk 28 | Nuclear | 1958 | 980 | 2.99 | 0.677 | 0 | Fission | 1500 | 0 | None | 200 | 5 | 248 | Airburst/Ground | Fighter-Bomber | 8000000 | 1958-1983 | Standard | First-generation nuclear weapon, large warhead | 0 |
| 9094 | USA | Mk 43 | Nuclear | 1961 | 4900 | 4.95 | 1.983 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 350 | Airburst/Ground | Bomber | 8000000 | 1961-1986 | Standard | Standard operational bomb | 0 |
| 9095 | USA | B57 | Nuclear | 1963 | 230 | 2.62 | 0.427 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 173 | Airburst/Ground | Attack Aircraft | 8000000 | 1963-1983 | Standard | Standard operational bomb | 0 |
| 9096 | USA | B61 | Nuclear | 1968 | 320 | 2.66 | 0.457 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 182 | Airburst/Ground | Attack Aircraft | 8000000 | 1968-1993 | B61-3/4/7/10/11/12 | Standard operational bomb | 0 |
| 9097 | USA | B83 | Nuclear | 1983 | 1090 | 3.04 | 0.713 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 259 | Airburst/Ground | Multirole Fighter | 15000000 | 1983-2008 | Standard | Standard operational bomb | 0 |
| 9098 | USA | B61-12 | Nuclear | 2020 | 320 | 2.66 | 0.457 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 182 | Airburst/Ground | Fighter/Attack | 28000000 | 2020-2025 | B61-3/4/7/10/11/12 | Modern guided nuclear bomb, variable yield, high precision | 0 |
| 9100 | USA | Mk 77 | Incendiary | 1965 | 780 | 5.40 | 0.338 | 234 | Napalm | 171 | 0 | None | 200 | 5 | 228 | Impact | Fighter-Bomber | 17600 | 1965-1990 | Standard | Standard operational bomb | 0 |
| 9101 | USA | BLU-27 | Incendiary | 1967 | 350 | 3.25 | 0.306 | 105 | Napalm | 124 | 0 | None | 200 | 5 | 185 | Impact | Attack Aircraft | 9000 | 1967-1987 | Standard | Standard operational bomb | 0 |
| 9102 | USA | Mk 78 | Incendiary | 1970 | 780 | 5.40 | 0.338 | 234 | Napalm | 171 | 0 | None | 200 | 5 | 228 | Impact | Multirole Fighter | 17600 | 1970-1995 | Standard | Standard operational bomb | 0 |
| 9110 | USA | Mk 36 | Mine | 1943 | 250 | 2.75 | 0.295 | 112 | Tritonal | 99 | 0 | None | 200 | 5 | 175 | Magnetic/Acoustic | Attack Aircraft | 7000 | 1943-1968 | Standard | Standard operational bomb | 0 |
| 9111 | USA | Mk 82 Mine | Mine | 1960 | 227 | 2.63 | 0.292 | 113 | Comp B | 99 | 0 | None | 200 | 5 | 172 | Magnetic/Acoustic | Attack Aircraft | 6540 | 1960-1985 | Mk 82, BSU-86 Snakeye | Standard operational bomb | 0 |
| 9112 | USA | Mk 62 Quickstrike | Mine | 1983 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | None | 200 | 5 | 175 | Magnetic/Acoustic | Fighter/Attack | 10500 | 1983-2008 | Standard | Standard operational bomb | 0 |
| 9113 | USA | Mk 63 Quickstrike | Mine | 1985 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | None | 200 | 5 | 175 | Magnetic/Acoustic | Fighter/Attack | 10500 | 1985-2010 | Standard | Standard operational bomb | 0 |
| 9114 | USA | Mk 65 Quickstrike | Mine | 1988 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | None | 200 | 5 | 175 | Magnetic/Acoustic | Fighter/Attack | 10500 | 1988-2013 | Standard | Standard operational bomb | 0 |
| 9120 | USA | BLU-109 | Penetrator | 1985 | 900 | 6.00 | 0.345 | 360 | H6 | 180 | 1800 | None | 200 | 5 | 240 | Delayed | Multirole Fighter | 30000 | 1985-2015 | Standard | Standard operational bomb | 0 |
| 9121 | USA | BLU-116 | Penetrator | 1996 | 900 | 6.00 | 0.345 | 360 | H6 | 180 | 2400 | None | 200 | 5 | 240 | Delayed | Multirole Fighter | 30000 | 1996-2025 | Standard | Standard operational bomb | 0 |
| 9122 | USA | BLU-122 | Penetrator | 2003 | 900 | 6.00 | 0.345 | 360 | PBXN-109 | 172 | 720 | None | 200 | 5 | 240 | Delayed | Multirole Fighter | 30000 | 2003-Present | Standard | Standard operational bomb | 0 |
| 9200 | British | 250 lb GP | GP Bomb | 1940 | 113 | 2.06 | 0.273 | 50 | RDX/TNT | 71 | 0 | None | 200 | 5 | 161 | Contact/Delay | Attack Aircraft | 4260 | 1940-1950 | Standard | Standard operational bomb | 0 |
| 9201 | British | 500 lb GP | GP Bomb | 1941 | 227 | 2.63 | 0.292 | 102 | RDX/TNT | 95 | 0 | None | 200 | 5 | 172 | Contact/Delay | Attack Aircraft | 6540 | 1941-1951 | Standard | Standard operational bomb | 0 |
| 9202 | British | 1000 lb MC | GP Bomb | 1942 | 454 | 3.77 | 0.316 | 204 | RDX/TNT | 125 | 0 | None | 200 | 5 | 195 | Contact/Delay | Attack Aircraft | 11080 | 1942-1952 | Standard | Standard operational bomb | 0 |
| 9203 | British | 4000 lb HC | Heavy Bomb | 1943 | 1814 | 5.27 | 1.005 | 816 | RDX/TNT | 219 | 0 | None | 200 | 5 | 331 | Contact/Delay | Bomber | 38280 | 1943-1953 | Standard | Standard operational bomb | 0 |
| 9210 | British | Tallboy | Heavy Bomb | 1944 | 5440 | 9.80 | 2.213 | 2448 | RDX/TNT | 340 | 0 | None | 200 | 5 | 350 | Contact/Delay | Heavy Bomber | 110800 | 1944-1954 | Standard | Barnes Wallis earthquake bomb, 12,000 lb, penetrated 16ft concrete | 0 |
| 9211 | British | Grand Slam | Heavy Bomb | 1945 | 9980 | 15.47 | 3.727 | 4491 | RDX/TNT | 433 | 0 | None | 200 | 5 | 350 | Contact/Delay | Heavy Bomber | 201600 | 1945-1955 | Standard | Largest conventional bomb of WWII, 22,000 lb, earthquake bomb | 0 |
| 9220 | British | 1000 lb GP (Post-war) | GP Bomb | 1950 | 454 | 3.77 | 0.316 | 204 | RDX/TNT | 125 | 0 | None | 200 | 5 | 195 | Contact/Delay | Attack Aircraft | 11080 | 1950-1970 | Standard | Standard operational bomb | 0 |
| 9221 | British | 1000 lb HE | GP Bomb | 1955 | 454 | 3.77 | 0.316 | 204 | RDX/TNT | 125 | 0 | None | 200 | 5 | 195 | Contact/Delay | Attack Aircraft | 11080 | 1955-1975 | Standard | Standard operational bomb | 0 |
| 9222 | British | Mk 13 (British) | GP Bomb | 1960 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1960-1985 | Standard | Standard operational bomb | 0 |
| 9230 | British | Paveway II (RAF) | LGB | 1977 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | Laser | 10 | 15 | 175 | Contact/Delay | Attack Aircraft | 40000 | 1977-1997 | Standard | Early laser-guided bomb, Vietnam War era | 0 |
| 9231 | British | Paveway III (RAF) | LGB | 1985 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | Laser | 6 | 15 | 175 | Contact/Delay | Fighter/Attack | 40000 | 1985-2015 | Standard | Standard operational bomb | 0 |
| 9232 | British | Enhanced Paveway II | LGB | 1998 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | Laser | 6 | 15 | 175 | Contact/Delay | Fighter/Attack | 40000 | 1998-2025 | Standard | Standard operational bomb | 0 |
| 9240 | British | Paveway IV | Dual-Mode | 2008 | 250 | 2.75 | 0.295 | 137 | PBXN-109 | 117 | 0 | Laser+GPS | 5 | 15 | 175 | Contact/Delay | Fighter/Attack | 70000 | 2008-Present | Paveway IV, Dual Mode | Standard operational bomb | 0 |
| 9241 | British | SPEAR 3 | Powered Bomb | 2021 | 250 | 2.75 | 0.295 | 137 | PBXN-109 | 117 | 0 | None | 200 | 5 | 175 | Contact/Delay | Fighter/Attack | 10500 | 2021-Present | Standard | Network-enabled powered glide bomb, 150km range | 0 |
| 9250 | British | BL755 | Cluster Bomb | 1973 | 264 | 3.08 | 0.476 | 105 | Comp B | 96 | 0 | None | 200 | 5 | 105 | Proximity | Attack Aircraft | 7280 | 1973-1993 | Standard | Area effect munition, anti-personnel/armor | 0 |
| 9251 | British | RBL755 | Cluster Bomb | 1985 | 264 | 3.08 | 0.476 | 105 | H6 | 110 | 0 | None | 200 | 5 | 105 | Proximity | Fighter/Attack | 10920 | 1985-2015 | Standard | Area effect munition, anti-personnel/armor | 0 |
| 9260 | British | Blue Danube | Nuclear | 1953 | 4500 | 4.75 | 1.850 | 0 | Fission | 1500 | 0 | None | 200 | 5 | 350 | Airburst/Ground | Bomber | 8000000 | 1953-1973 | Standard | Britain's first operational nuclear weapon | 0 |
| 9261 | British | Red Beard | Nuclear | 1961 | 900 | 2.95 | 0.650 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 240 | Airburst/Ground | Fighter-Bomber | 8000000 | 1961-1981 | Standard | Standard operational bomb | 0 |
| 9262 | British | WE.177 | Nuclear | 1966 | 270 | 2.63 | 0.440 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 177 | Airburst/Ground | Attack Aircraft | 8000000 | 1966-1986 | WE.177A/B/C | Standard operational bomb | 0 |
| 9263 | British | WE.177A/B | Nuclear | 1976 | 270 | 2.63 | 0.440 | 0 | Thermonuclear | 1500 | 0 | None | 200 | 5 | 177 | Airburst/Ground | Attack Aircraft | 8000000 | 1976-1996 | WE.177A/B/C | Standard operational bomb | 0 |
| 9270 | British | CRV7 Pod | Rocket Pod | 1975 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1975-1995 | Standard | Standard operational bomb | 0 |
| 9271 | British | SNEB Rocket | Rocket Pod | 1980 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | None | 200 | 5 | 175 | Contact/Delay | Fighter/Attack | 10500 | 1980-2010 | Standard | Standard operational bomb | 0 |
| 9300 | German | SC 50 | GP Bomb | 1940 | 50 | 1.75 | 0.256 | 22 | Amatol | 51 | 0 | None | 200 | 5 | 155 | Contact/Delay | Attack Aircraft | 3000 | 1940-1950 | Standard | Standard operational bomb | 0 |
| 9301 | German | SC 250 | GP Bomb | 1941 | 250 | 2.75 | 0.295 | 112 | Amatol | 99 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1941-1951 | Standard | Standard operational bomb | 0 |
| 9302 | German | SC 500 | GP Bomb | 1942 | 50 | 1.75 | 0.256 | 22 | Amatol | 51 | 0 | None | 200 | 5 | 155 | Contact/Delay | Attack Aircraft | 3000 | 1942-1952 | Standard | Standard operational bomb | 0 |
| 9303 | German | SC 1000 | GP Bomb | 1943 | 1000 | 6.50 | 0.350 | 450 | Amatol | 172 | 0 | None | 200 | 5 | 250 | Contact/Delay | Fighter-Bomber | 22000 | 1943-1953 | Standard | Standard operational bomb | 0 |
| 9310 | German | SC 1800 | Heavy Bomb | 1944 | 1800 | 5.25 | 1.000 | 810 | Amatol | 218 | 0 | None | 200 | 5 | 330 | Contact/Delay | Bomber | 38000 | 1944-1954 | Standard | Standard operational bomb | 0 |
| 9311 | German | PC 1400 | AP Bomb | 1943 | 1400 | 8.50 | 0.368 | 489 | Amatol | 178 | 1400 | None | 200 | 5 | 290 | Delayed | Fighter-Bomber | 30000 | 1943-1953 | Standard | Standard operational bomb | 0 |
| 9320 | German | Fritz X | Guided Bomb | 1943 | 1400 | 8.50 | 0.368 | 630 | Amatol | 197 | 0 | Radio | 50 | 10 | 290 | Contact/Delay | Fighter-Bomber | 71000 | 1943-1953 | Standard | First operational guided bomb, sank Italian battleship Roma 1943 | 0 |
| 9321 | German | Hs 293 | Glide Bomb | 1943 | 650 | 5.12 | 0.330 | 292 | Amatol | 145 | 0 | Radio+Rocket | 50 | 15 | 215 | Contact/Delay | Fighter-Bomber | 41000 | 1943-1953 | Standard | First glide bomb, rocket-boosted, anti-ship weapon | 0 |
| 9330 | German | 250 kg (Bundeswehr) | GP Bomb | 1960 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1960-1980 | Standard | Standard operational bomb | 0 |
| 9331 | German | 500 kg (Bundeswehr) | GP Bomb | 1965 | 500 | 4.00 | 0.319 | 250 | Comp B | 136 | 0 | None | 200 | 5 | 200 | Contact/Delay | Attack Aircraft | 12000 | 1965-1985 | Standard | Standard operational bomb | 0 |
| 9332 | German | DM 91 | GP Bomb | 1975 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1975-1995 | Standard | Standard operational bomb | 0 |
| 9340 | German | GBU-12 (Luftwaffe) | LGB | 1985 | 240 | 2.70 | 0.294 | 132 | H6 | 120 | 0 | Laser | 6 | 15 | 174 | Contact/Delay | Fighter/Attack | 39600 | 1985-2015 | GBU-12A/B/C/D, Paveway II | Standard operational bomb | 0 |
| 9341 | German | GBU-24 (Luftwaffe) | LGB | 1995 | 1020 | 6.60 | 0.351 | 561 | H6 | 216 | 0 | Laser | 6 | 25 | 252 | Contact/Delay | Multirole Fighter | 70800 | 1995-2025 | GBU-24A/B, Paveway III | Standard operational bomb | 0 |
| 9350 | German | GBU-38 (Luftwaffe) | GPS-Guided | 2010 | 240 | 2.70 | 0.294 | 132 | PBXN-109 | 115 | 0 | GPS+INS | 8 | 15 | 174 | Contact/Delay | Fighter/Attack | 34600 | 2010-Present | GBU-38(V)1/2/3 | Standard operational bomb | 0 |
| 9351 | German | GBU-54 (Luftwaffe) | Laser/GPS | 2015 | 240 | 2.70 | 0.294 | 132 | PBXN-109 | 115 | 0 | Laser+GPS | 3 | 15 | 174 | Contact/Delay | Fighter/Attack | 69600 | 2015-Present | Standard | Standard operational bomb | 0 |
| 9360 | German | MW-1 | Cluster Munition | 1982 | 400 | 3.53 | 0.567 | 160 | H6 | 131 | 0 | None | 200 | 5 | 114 | Proximity | Fighter/Attack | 15000 | 1982-2012 | Standard | Area effect munition, anti-personnel/armor | 0 |
| 9361 | German | DM 118 | Dispenser | 1990 | 250 | 2.75 | 0.295 | 137 | H6 | 123 | 0 | None | 200 | 5 | 175 | Contact/Delay | Fighter/Attack | 10500 | 1990-2020 | Standard | Standard operational bomb | 0 |
| 9400 | Japanese | Type 94 | GP Bomb | 1940 | 250 | 2.75 | 0.295 | 112 | Tritonal | 99 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1940-1950 | Standard | Standard operational bomb | 0 |
| 9401 | Japanese | Type 97 | GP Bomb | 1941 | 250 | 2.75 | 0.295 | 112 | Tritonal | 99 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1941-1951 | Standard | Standard operational bomb | 0 |
| 9402 | Japanese | Type 98 | GP Bomb | 1942 | 250 | 2.75 | 0.295 | 112 | Tritonal | 99 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1942-1952 | Standard | Standard operational bomb | 0 |
| 9403 | Japanese | Type 99 | GP Bomb | 1943 | 250 | 2.75 | 0.295 | 112 | Tritonal | 99 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1943-1953 | Standard | Standard operational bomb | 0 |
| 9410 | Japanese | Type 80 AP | AP Bomb | 1941 | 250 | 2.75 | 0.295 | 87 | Tritonal | 89 | 200 | None | 200 | 5 | 175 | Delayed | Attack Aircraft | 7000 | 1941-1951 | Standard | Standard operational bomb | 0 |
| 9411 | Japanese | Type 91 AP | AP Bomb | 1941 | 250 | 2.75 | 0.295 | 87 | Tritonal | 89 | 250 | None | 200 | 5 | 175 | Delayed | Attack Aircraft | 7000 | 1941-1951 | Standard | Modified 16-inch naval shell, used at Pearl Harbor | 0 |
| 9420 | Japanese | Type 3 Cluster | Incendiary | 1944 | 350 | 3.25 | 0.306 | 105 | Napalm | 124 | 0 | None | 200 | 5 | 185 | Impact | Attack Aircraft | 9000 | 1944-1954 | Standard | Standard operational bomb | 0 |
| 9421 | Japanese | Type 100 | Incendiary | 1944 | 350 | 3.25 | 0.306 | 105 | Napalm | 124 | 0 | None | 200 | 5 | 185 | Impact | Attack Aircraft | 9000 | 1944-1954 | Standard | Standard operational bomb | 0 |
| 9430 | Japanese | 250 kg (JASDF) | GP Bomb | 1960 | 250 | 2.75 | 0.295 | 125 | Comp B | 103 | 0 | None | 200 | 5 | 175 | Contact/Delay | Attack Aircraft | 7000 | 1960-1980 | Standard | Standard operational bomb | 0 |
| 9431 | Japanese | 500 kg (JASDF) | GP Bomb | 1965 | 500 | 4.00 | 0.319 | 250 | Comp B | 136 | 0 | None | 200 | 5 | 200 | Contact/Delay | Attack Aircraft | 12000 | 1965-1985 | Standard | Standard operational bomb | 0 |
| 9432 | Japanese | Mk 82 (JASDF) | GP Bomb | 1975 | 227 | 2.63 | 0.292 | 113 | Comp B | 99 | 0 | None | 200 | 5 | 172 | Contact/Delay | Attack Aircraft | 6540 | 1975-2000 | Mk 82, BSU-86 Snakeye | Standard operational bomb | 0 |
| 9440 | Japanese | GBU-12 (JASDF) | LGB | 1990 | 240 | 2.70 | 0.294 | 132 | H6 | 120 | 0 | Laser | 6 | 15 | 174 | Contact/Delay | Fighter/Attack | 39600 | 1990-2020 | GBU-12A/B/C/D, Paveway II | Standard operational bomb | 0 |
| 9441 | Japanese | GBU-24 (JASDF) | LGB | 1998 | 1020 | 6.60 | 0.351 | 561 | H6 | 216 | 0 | Laser | 6 | 25 | 252 | Contact/Delay | Multirole Fighter | 70800 | 1998-2025 | GBU-24A/B, Paveway III | Standard operational bomb | 0 |
| 9450 | Japanese | GBU-38 (JASDF) | GPS-Guided | 2012 | 240 | 2.70 | 0.294 | 132 | PBXN-109 | 115 | 0 | GPS+INS | 8 | 15 | 174 | Contact/Delay | Fighter/Attack | 34600 | 2012-Present | GBU-38(V)1/2/3 | Standard operational bomb | 0 |
| 9451 | Japanese | GBU-54 (JASDF) | Laser/GPS | 2016 | 240 | 2.70 | 0.294 | 132 | PBXN-109 | 115 | 0 | Laser+GPS | 3 | 15 | 174 | Contact/Delay | Fighter/Attack | 69600 | 2016-Present | Standard | Standard operational bomb | 0 |
| 9460 | Japanese | JDAM-ER (JASDF) | Extended Range | 2020 | 250 | 2.75 | 0.295 | 137 | PBXN-109 | 117 | 0 | None | 200 | 5 | 175 | Contact/Delay | Fighter/Attack | 10500 | 2020-Present | Standard | Standard operational bomb | 0 |
| 9470 | Japanese | CBU-87 (JASDF) | Cluster Bomb | 1995 | 430 | 3.63 | 0.587 | 172 | H6 | 134 | 0 | None | 200 | 5 | 115 | Proximity | Fighter/Attack | 15900 | 1995-2025 | Standard | Standard operational bomb | 0 |
| 9471 | Japanese | CBU-97 (JASDF) | Sensor Fused | 2005 | 430 | 3.65 | 0.314 | 236 | PBXN-109 | 146 | 0 | None | 200 | 5 | 193 | Contact/Delay | Fighter/Attack | 15900 | 2005-Present | Standard | Standard operational bomb | 0 |
