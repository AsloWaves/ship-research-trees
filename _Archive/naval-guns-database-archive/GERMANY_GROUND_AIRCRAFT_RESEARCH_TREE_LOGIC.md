# German Ground Aircraft Research Tree Logic

**Tech Branch**: Ground Aircraft
**Nation**: German
**Era**: 1940-2025
**Node Count**: ~50 nodes

## Research Tree Structure (Condensed)

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 4300 | German | Bf 109E | Fighter | 1940 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4301 | 0 |
| 4301 | German | Bf 109F | Fighter | 1941 | Ground Aircraft | Aircraft | 2000 | 50 | 12 | 18 | 0 | 4300 | 4302 | 0 |
| 4302 | German | Bf 109G | Fighter | 1942 | Ground Aircraft | Aircraft | 2500 | 60 | 15 | 22 | 0 | 4301 | 4303 | 0 |
| 4303 | German | Fw 190A | Fighter | 1941 | Ground Aircraft | Aircraft | 2500 | 60 | 15 | 22 | 0 | 4302 | 4304 | 0 |
| 4304 | German | Fw 190D | Fighter | 1944 | Ground Aircraft | Aircraft | 3000 | 70 | 18 | 28 | 0 | 4303 | 4310 | 0 |
| 4310 | German | CL-13 Sabre (German) | Jet Fighter | 1955 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4311 | 0 |
| 4311 | German | F-104G Starfighter | Interceptor | 1960 | Ground Aircraft | Aircraft | 6500 | 150 | 38 | 72 | 0 | 4310 | 4312 | 0 |
| 4312 | German | F-4F Phantom II | Multi-Role | 1973 | Ground Aircraft | Aircraft | 9000 | 210 | 48 | 105 | 0 | 4311 | 4320 | 0 |
| 4320 | German | Tornado IDS | Strike | 1979 | Ground Aircraft | Aircraft | 10000 | 235 | 52 | 125 | 0 | 4312 | 4321 | 0 |
| 4321 | German | Eurofighter Typhoon | Multi-Role | 2004 | Ground Aircraft | Aircraft | 14000 | 325 | 62 | 165 | 0 | 4320 | 4322 | 0 |
| 4322 | German | F-35A Lightning II (Luftwaffe) | Stealth Multi-Role | 2024 | Ground Aircraft | Aircraft | 22000 | 510 | 75 | 245 | 0 | 4321 | | 0 |
| 4330 | German | Ju 87 Stuka | Dive Bomber | 1940 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4331 | 0 |
| 4331 | German | Ju 88 | Bomber | 1940 | Ground Aircraft | Aircraft | 2500 | 60 | 16 | 24 | 0 | 4330 | 4332 | 0 |
| 4332 | German | He 111 | Bomber | 1941 | Ground Aircraft | Aircraft | 2500 | 60 | 16 | 24 | 0 | 4331 | 4340 | 0 |
| 4340 | German | Tornado ECR | EW/Recon | 1990 | Ground Aircraft | Aircraft | 9000 | 210 | 48 | 122 | 0 | 4320 | | 0 |
| 4350 | German | C-160 Transall | Transport | 1967 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4351 | 0 |
| 4351 | German | A400M (Luftwaffe) | Transport | 2014 | Ground Aircraft | Aircraft | 11000 | 260 | 55 | 145 | 0 | 4350 | | 0 |
| 4360 | German | CH-53G | Transport Helo | 1973 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4361 | 0 |
| 4361 | German | CH-53GA | Transport Helo | 1989 | Ground Aircraft | Aircraft | 5000 | 115 | 28 | 68 | 0 | 4360 | 4362 | 0 |
| 4362 | German | NH90 (Luftwaffe) | Utility Helo | 2019 | Ground Aircraft | Aircraft | 7500 | 175 | 38 | 108 | 0 | 4361 | | 0 |
| 4370 | German | UH-1D (Luftwaffe) | Utility Helo | 1967 | Ground Aircraft | Aircraft | 3000 | 70 | 18 | 42 | 0 | 4360 | 4371 | 0 |
| 4371 | German | Tiger UHT | Attack Helo | 2005 | Ground Aircraft | Aircraft | 8500 | 195 | 45 | 118 | 0 | 4370 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940):
- Bf 109E (Node 4300): WWII fighter → post-war NATO jets
- Ju 87 Stuka (Node 4330): Dive bomber lineage
- CL-13 Sabre (Node 4310): Post-war jet fighter restart
- C-160 Transall (Node 4350): European transport cooperation
- CH-53G (Node 4360): Heavy transport helicopter

**Tree Depth**: 12 generations (1940-2025)
