# Japanese Bombs Research Tree Logic

**Tech Branch**: Bombs
**Nation**: Japanese
**Era**: 1940-2025
**Node Count**: ~30 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 9400 | Japanese | Type 94 | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9401 | 0 |
| 9401 | Japanese | Type 97 | GP Bomb | 1941 | Bombs | Bomb | 1500 | 35 | 8 | 12 | 0 | 9400 | 9402 | 0 |
| 9402 | Japanese | Type 98 | GP Bomb | 1942 | Bombs | Bomb | 1800 | 42 | 10 | 15 | 0 | 9401 | 9403 | 0 |
| 9403 | Japanese | Type 99 | GP Bomb | 1943 | Bombs | Bomb | 2200 | 52 | 12 | 18 | 0 | 9402 | 9410 | 0 |
| 9410 | Japanese | Type 80 AP | AP Bomb | 1941 | Bombs | Bomb | 2500 | 58 | 15 | 22 | 0 | 9401 | 9411 | 0 |
| 9411 | Japanese | Type 91 AP | AP Bomb | 1941 | Bombs | Bomb | 3000 | 70 | 18 | 28 | 0 | 9410 | | 0 |
| 9420 | Japanese | Type 3 Cluster | Incendiary | 1944 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9421 | 0 |
| 9421 | Japanese | Type 100 | Incendiary | 1944 | Bombs | Bomb | 2500 | 58 | 12 | 22 | 0 | 9420 | | 0 |
| 9430 | Japanese | 250 kg (JASDF) | GP Bomb | 1960 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9431 | 0 |
| 9431 | Japanese | 500 kg (JASDF) | GP Bomb | 1965 | Bombs | Bomb | 2500 | 58 | 14 | 22 | 0 | 9430 | 9432 | 0 |
| 9432 | Japanese | Mk 82 (JASDF) | GP Bomb | 1975 | Bombs | Bomb | 2800 | 65 | 16 | 25 | 0 | 9431 | 9440 | 0 |
| 9440 | Japanese | GBU-12 (JASDF) | LGB | 1990 | Bombs | Bomb | 6200 | 142 | 32 | 62 | 0 | 9432 | 9441 | 0 |
| 9441 | Japanese | GBU-24 (JASDF) | LGB | 1998 | Bombs | Bomb | 7500 | 172 | 38 | 78 | 0 | 9440 | 9450 | 0 |
| 9450 | Japanese | GBU-38 (JASDF) | GPS-Guided | 2012 | Bombs | Bomb | 12000 | 278 | 62 | 138 | 0 | 9441 | 9451 | 0 |
| 9451 | Japanese | GBU-54 (JASDF) | Laser/GPS | 2016 | Bombs | Bomb | 13500 | 312 | 68 | 155 | 0 | 9450 | 9460 | 0 |
| 9460 | Japanese | JDAM-ER (JASDF) | Extended Range | 2020 | Bombs | Bomb | 15000 | 348 | 72 | 172 | 0 | 9451 | | 0 |
| 9470 | Japanese | CBU-87 (JASDF) | Cluster Bomb | 1995 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9471 | 0 |
| 9471 | Japanese | CBU-97 (JASDF) | Sensor Fused | 2005 | Bombs | Bomb | 8500 | 195 | 45 | 95 | 0 | 9470 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940-1995):
- Type 94 (Node 9400): WWII bomb lineage
- Type 3 Cluster (Node 9420): Incendiary weapons
- 250 kg JASDF (Node 9430): Post-war restart
- CBU-87 (Node 9470): Cluster munitions

**WWII Period**:
- Type 91 AP: Modified from 16-inch naval shells for ship attacks
- Type 3 Cluster: Anti-personnel incendiary bomblets

**Post-War Development**:
- 1960-1975: US bomb adoption and licensing
- 1990+: Precision-guided munitions integration
- 2020: Latest JDAM variants

**Tree Depth**: 11 generations (1940-2020)
**Total Nodes**: 18
