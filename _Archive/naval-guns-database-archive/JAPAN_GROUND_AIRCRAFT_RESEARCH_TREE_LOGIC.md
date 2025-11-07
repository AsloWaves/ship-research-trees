# Japanese Ground Aircraft Research Tree Logic

**Tech Branch**: Ground Aircraft
**Nation**: Japanese
**Era**: 1940-2025
**Node Count**: ~45 nodes

## Research Tree Structure (Condensed)

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 4400 | Japanese | A6M Zero | Fighter | 1940 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4401 | 0 |
| 4401 | Japanese | Ki-43 Hayabusa (Oscar) | Fighter | 1941 | Ground Aircraft | Aircraft | 2000 | 50 | 12 | 18 | 0 | 4400 | 4402 | 0 |
| 4402 | Japanese | Ki-61 Hien (Tony) | Fighter | 1943 | Ground Aircraft | Aircraft | 2500 | 60 | 15 | 22 | 0 | 4401 | 4403 | 0 |
| 4403 | Japanese | Ki-84 Hayate (Frank) | Fighter | 1944 | Ground Aircraft | Aircraft | 3000 | 70 | 18 | 28 | 0 | 4402 | 4410 | 0 |
| 4410 | Japanese | F-86F Sabre (JASDF) | Jet Fighter | 1956 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4411 | 0 |
| 4411 | Japanese | F-104J Starfighter | Interceptor | 1962 | Ground Aircraft | Aircraft | 6500 | 150 | 38 | 72 | 0 | 4410 | 4412 | 0 |
| 4412 | Japanese | F-4EJ Phantom II | Multi-Role | 1971 | Ground Aircraft | Aircraft | 9000 | 210 | 48 | 105 | 0 | 4411 | 4413 | 0 |
| 4413 | Japanese | F-4EJ Kai | Multi-Role | 1984 | Ground Aircraft | Aircraft | 9500 | 220 | 50 | 115 | 0 | 4412 | 4420 | 0 |
| 4420 | Japanese | F-15J Eagle | Air Superiority | 1981 | Ground Aircraft | Aircraft | 12000 | 280 | 55 | 135 | 0 | 4413 | 4421 | 0 |
| 4421 | Japanese | F-15J(M) Kai | Air Superiority | 2004 | Ground Aircraft | Aircraft | 13000 | 300 | 58 | 148 | 0 | 4420 | 4430 | 0 |
| 4430 | Japanese | F-2A | Multi-Role | 2000 | Ground Aircraft | Aircraft | 11000 | 260 | 52 | 138 | 0 | 4421 | 4431 | 0 |
| 4431 | Japanese | F-2B | Multi-Role | 2002 | Ground Aircraft | Aircraft | 11500 | 270 | 54 | 145 | 0 | 4430 | 4440 | 0 |
| 4440 | Japanese | F-35A Lightning II (JASDF) | Stealth Multi-Role | 2018 | Ground Aircraft | Aircraft | 22000 | 510 | 75 | 245 | 0 | 4431 | 4441 | 0 |
| 4441 | Japanese | F-15EX (JASDF) | Multi-Role | 2024 | Ground Aircraft | Aircraft | 16000 | 375 | 65 | 185 | 0 | 4440,4421 | | 0 |
| 4450 | Japanese | C-1 | Transport | 1974 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4451 | 0 |
| 4451 | Japanese | C-2 | Transport | 2017 | Ground Aircraft | Aircraft | 10000 | 235 | 52 | 142 | 0 | 4450 | | 0 |
| 4452 | Japanese | C-130H Hercules (JASDF) | Transport | 1981 | Ground Aircraft | Aircraft | 6000 | 140 | 38 | 78 | 0 | 4450 | 4453 | 0 |
| 4453 | Japanese | KC-767 | Tanker | 2008 | Ground Aircraft | Aircraft | 9500 | 220 | 52 | 128 | 0 | 4452 | | 0 |
| 4460 | Japanese | UH-1H (JASDF) | Utility Helo | 1973 | Ground Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 4461 | 0 |
| 4461 | Japanese | UH-60J Black Hawk | Utility Helo | 1992 | Ground Aircraft | Aircraft | 5500 | 125 | 30 | 72 | 0 | 4460 | 4462 | 0 |
| 4462 | Japanese | UH-60J Kai | Utility Helo | 2012 | Ground Aircraft | Aircraft | 6500 | 150 | 34 | 88 | 0 | 4461 | | 0 |
| 4470 | Japanese | AH-1S Cobra (JASDF) | Attack Helo | 1978 | Ground Aircraft | Aircraft | 4500 | 105 | 24 | 58 | 0 | 4460 | 4471 | 0 |
| 4471 | Japanese | AH-64D Apache (JASDF) | Attack Helo | 2006 | Ground Aircraft | Aircraft | 9000 | 210 | 48 | 125 | 0 | 4470 | | 0 |
| 4480 | Japanese | CH-47J Chinook | Transport Helo | 1986 | Ground Aircraft | Aircraft | 5500 | 125 | 32 | 72 | 0 | 4460 | 4481 | 0 |
| 4481 | Japanese | CH-47JA Chinook | Transport Helo | 2001 | Ground Aircraft | Aircraft | 6500 | 150 | 36 | 85 | 0 | 4480 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940):
- A6M Zero (Node 4400): WWII fighter lineage
- F-86F Sabre (Node 4410): Post-war jet fighter restart
- C-1 (Node 4450): Indigenous transport aircraft
- UH-1H (Node 4460): Utility helicopter lineage

**Indigenous Development**:
- F-2 (2000): Indigenous fighter-bomber development
- C-2 (2017): Indigenous strategic transport

**Tree Depth**: 13 generations (1940-2025)
