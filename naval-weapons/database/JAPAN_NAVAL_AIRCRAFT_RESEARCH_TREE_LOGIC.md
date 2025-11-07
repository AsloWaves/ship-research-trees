# Japanese Naval Aircraft Research Tree Logic

**Tech Branch**: Naval Aircraft
**Nation**: Japanese
**Era**: 1940-2025
**Node Count**: ~40 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 3400 | Japanese | A5M Claude | Fighter | 1940 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3401 | 0 |
| 3401 | Japanese | A6M2 Zero | Fighter | 1940 | Naval Aircraft | Aircraft | 2000 | 50 | 12 | 18 | 0 | 3400 | 3402 | 0 |
| 3402 | Japanese | A6M3 Zero | Fighter | 1942 | Naval Aircraft | Aircraft | 2500 | 60 | 15 | 22 | 0 | 3401 | 3403 | 0 |
| 3403 | Japanese | A6M5 Zero | Fighter | 1943 | Naval Aircraft | Aircraft | 3000 | 70 | 18 | 28 | 0 | 3402 | 3404 | 0 |
| 3404 | Japanese | J2M Raiden (Jack) | Interceptor | 1943 | Naval Aircraft | Aircraft | 3500 | 80 | 20 | 32 | 0 | 3403 | 3405 | 0 |
| 3405 | Japanese | N1K2-J Shiden-Kai (George) | Fighter | 1944 | Naval Aircraft | Aircraft | 4000 | 90 | 22 | 38 | 0 | 3404 | 3410 | 0 |
| 3410 | Japanese | P-1 | Maritime Patrol | 2013 | Naval Aircraft | Aircraft | 12000 | 280 | 52 | 145 | 0 | 3405 | 3411 | 0 |
| 3411 | Japanese | P-1 Mod 2 | Maritime Patrol | 2022 | Naval Aircraft | Aircraft | 13500 | 310 | 55 | 158 | 0 | 3410 | | 0 |
| 3412 | Japanese | P-3C Orion (JMSDF) | ASW/Patrol | 1982 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3413 | 0 |
| 3413 | Japanese | P-3C Update III (JMSDF) | ASW/Patrol | 1995 | Naval Aircraft | Aircraft | 8000 | 185 | 42 | 105 | 0 | 3412 | 3410 | 0 |
| 3420 | Japanese | D3A Val | Dive Bomber | 1940 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3421 | 0 |
| 3421 | Japanese | D4Y Suisei (Judy) | Dive Bomber | 1942 | Naval Aircraft | Aircraft | 2500 | 60 | 15 | 22 | 0 | 3420 | 3422 | 0 |
| 3422 | Japanese | B7A Ryusei (Grace) | Strike | 1944 | Naval Aircraft | Aircraft | 3500 | 80 | 20 | 32 | 0 | 3421 | 3430 | 0 |
| 3430 | Japanese | F-35B Lightning II (JMSDF) | V/STOL Stealth | 2024 | Naval Aircraft | Aircraft | 20000 | 450 | 68 | 220 | 0 | 3422 | | 0 |
| 3440 | Japanese | B5N Kate | Torpedo Bomber | 1940 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3441 | 0 |
| 3441 | Japanese | B6N Tenzan (Jill) | Torpedo Bomber | 1943 | Naval Aircraft | Aircraft | 2500 | 60 | 15 | 22 | 0 | 3440 | 3442 | 0 |
| 3442 | Japanese | P2V Neptune (JMSDF) | ASW/Patrol | 1958 | Naval Aircraft | Aircraft | 4000 | 90 | 25 | 48 | 0 | 3441 | 3443 | 0 |
| 3443 | Japanese | PS-1 | ASW Flying Boat | 1971 | Naval Aircraft | Aircraft | 5500 | 125 | 32 | 68 | 0 | 3442 | 3444 | 0 |
| 3444 | Japanese | US-2 | SAR Flying Boat | 2007 | Naval Aircraft | Aircraft | 7000 | 165 | 38 | 92 | 0 | 3443 | | 0 |
| 3450 | Japanese | HSS-2 Sea King (JMSDF) | ASW Helo | 1965 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3451 | 0 |
| 3451 | Japanese | SH-3A Sea King (JMSDF) | ASW Helo | 1974 | Naval Aircraft | Aircraft | 4000 | 90 | 22 | 52 | 0 | 3450 | 3452 | 0 |
| 3452 | Japanese | SH-60J Seahawk | ASW Helo | 1991 | Naval Aircraft | Aircraft | 6000 | 140 | 32 | 78 | 0 | 3451 | 3453 | 0 |
| 3453 | Japanese | SH-60K Seahawk | ASW Helo | 2006 | Naval Aircraft | Aircraft | 8000 | 185 | 38 | 108 | 0 | 3452 | 3454 | 0 |
| 3454 | Japanese | SH-60K(Kai) | ASW Helo | 2015 | Naval Aircraft | Aircraft | 9000 | 210 | 42 | 122 | 0 | 3453 | | 0 |
| 3460 | Japanese | MCH-101 | Multi-Role Helo | 2008 | Naval Aircraft | Aircraft | 7500 | 175 | 38 | 98 | 0 | 3453 | 3461 | 0 |
| 3461 | Japanese | MCH-101 Mod 2 | Multi-Role Helo | 2018 | Naval Aircraft | Aircraft | 8500 | 195 | 42 | 112 | 0 | 3460 | | 0 |
| 3470 | Japanese | OH-6D | Observation Helo | 1978 | Naval Aircraft | Aircraft | 1500 | 35 | 10 | 22 | 0 | 3451 | 3471 | 0 |
| 3471 | Japanese | OH-1 Ninja | Observation Helo | 1999 | Naval Aircraft | Aircraft | 3000 | 70 | 15 | 42 | 0 | 3470 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940):
- A5M Claude (Node 3400): Early fighter → Zero lineage
- D3A Val (Node 3420): Dive bomber → strike aircraft
- B5N Kate (Node 3440): Torpedo bomber → ASW transition
- P-3C Orion (Node 3412): Post-war ASW patrol
- HSS-2 Sea King (Node 3450): ASW helicopter → Seahawk

**WWII to Modern Gap**:
- No carrier fixed-wing aircraft 1945-2024 (post-war constitution)
- Focus shifted to helicopters and land-based maritime patrol
- F-35B marks return to carrier-capable fighters (2024)

**Indigenous Development**:
- P-1 maritime patrol aircraft (2013) replaces P-3C
- US-2/PS-1 amphibious SAR aircraft
- SH-60K indigenous Seahawk variant

**Tree Depth**: 12 generations (1940-2025)
