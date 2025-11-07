# British Ground Aircraft Research Tree Logic

**Tech Branch**: Ground Aircraft
**Nation**: British
**Era**: 1940-2025
**Node Count**: ~45 nodes

## Research Tree Structure (Condensed)

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 4200 | British | Spitfire Mk I | Fighter | 1940 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4201 | 0 |
| 4201 | British | Spitfire Mk V | Fighter | 1941 | Ground Aircraft | Aircraft | 2200 | 55 | 14 | 22 | 0 | 4200 | 4202 | 0 |
| 4202 | British | Spitfire Mk IX | Fighter | 1942 | Ground Aircraft | Aircraft | 2500 | 60 | 16 | 26 | 0 | 4201 | 4203 | 0 |
| 4203 | British | Spitfire Mk XIV | Fighter | 1944 | Ground Aircraft | Aircraft | 3000 | 70 | 18 | 30 | 0 | 4202 | 4210 | 0 |
| 4210 | British | Meteor F.1 | Jet Fighter | 1944 | Ground Aircraft | Aircraft | 4000 | 90 | 25 | 45 | 0 | 4203 | 4211 | 0 |
| 4211 | British | Meteor F.8 | Jet Fighter | 1950 | Ground Aircraft | Aircraft | 4500 | 105 | 28 | 52 | 0 | 4210 | 4212 | 0 |
| 4212 | British | Hunter F.1 | Jet Fighter | 1954 | Ground Aircraft | Aircraft | 5500 | 125 | 32 | 62 | 0 | 4211 | 4213 | 0 |
| 4213 | British | Lightning F.1 | Interceptor | 1960 | Ground Aircraft | Aircraft | 7000 | 165 | 40 | 82 | 0 | 4212 | 4214 | 0 |
| 4214 | British | Phantom FGR.2 | Multi-Role | 1969 | Ground Aircraft | Aircraft | 9500 | 220 | 50 | 115 | 0 | 4213 | 4220 | 0 |
| 4220 | British | Tornado F.3 | Interceptor | 1986 | Ground Aircraft | Aircraft | 10000 | 235 | 52 | 128 | 0 | 4214 | 4221 | 0 |
| 4221 | British | Typhoon FGR.4 | Multi-Role | 2007 | Ground Aircraft | Aircraft | 14000 | 325 | 62 | 165 | 0 | 4220 | 4222 | 0 |
| 4222 | British | F-35B Lightning II (RAF) | Stealth Multi-Role | 2018 | Ground Aircraft | Aircraft | 20000 | 470 | 72 | 220 | 0 | 4221 | | 0 |
| 4230 | British | Lancaster | Heavy Bomber | 1942 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4231 | 0 |
| 4231 | British | Lincoln | Heavy Bomber | 1945 | Ground Aircraft | Aircraft | 3500 | 80 | 22 | 38 | 0 | 4230 | 4232 | 0 |
| 4232 | British | Canberra B.2 | Bomber | 1951 | Ground Aircraft | Aircraft | 5000 | 115 | 30 | 58 | 0 | 4231 | 4233 | 0 |
| 4233 | British | Vulcan B.1 | Strategic Bomber | 1957 | Ground Aircraft | Aircraft | 8000 | 185 | 48 | 95 | 0 | 4232 | 4234 | 0 |
| 4234 | British | Vulcan B.2 | Strategic Bomber | 1960 | Ground Aircraft | Aircraft | 9000 | 210 | 52 | 108 | 0 | 4233 | | 0 |
| 4240 | British | Harrier GR.1 | V/STOL Attack | 1969 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4241 | 0 |
| 4241 | British | Harrier GR.7 | V/STOL Attack | 1990 | Ground Aircraft | Aircraft | 8000 | 185 | 42 | 108 | 0 | 4240 | 4222 | 0 |
| 4250 | British | C-130K Hercules (RAF) | Transport | 1967 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4251 | 0 |
| 4251 | British | C-130J Hercules (RAF) | Transport | 2000 | Ground Aircraft | Aircraft | 7000 | 165 | 42 | 98 | 0 | 4250 | 4252 | 0 |
| 4252 | British | A400M Atlas | Transport | 2014 | Ground Aircraft | Aircraft | 11000 | 260 | 55 | 145 | 0 | 4251 | | 0 |
| 4260 | British | Apache AH.1 (RAF) | Attack Helo | 2001 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4261 | 0 |
| 4261 | British | Apache AH-64E (RAF) | Attack Helo | 2020 | Ground Aircraft | Aircraft | 10000 | 235 | 50 | 135 | 0 | 4260 | | 0 |
| 4270 | British | Puma HC.1 | Utility Helo | 1971 | Ground Aircraft | Aircraft | 3500 | 80 | 20 | 48 | 0 | 4260 | 4271 | 0 |
| 4271 | British | Merlin HC.3 | Transport Helo | 2001 | Ground Aircraft | Aircraft | 6000 | 140 | 35 | 88 | 0 | 4270 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940):
- Spitfire (Node 4200): WWII fighter → jet transition
- Lancaster (Node 4230): Heavy bomber → strategic bombers
- Harrier GR.1 (Node 4240): V/STOL attack lineage
- C-130K Hercules (Node 4250): Tactical transport
- Apache (Node 4260): Attack helicopter

**Tree Depth**: 11 generations (1940-2025)
