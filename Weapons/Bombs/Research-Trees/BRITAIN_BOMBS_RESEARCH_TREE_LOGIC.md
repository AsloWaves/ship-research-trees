# British Bombs Research Tree Logic

**Tech Branch**: Bombs
**Nation**: British
**Era**: 1940-2025
**Node Count**: ~35 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 9200 | British | 250 lb GP | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9201 | 0 |
| 9201 | British | 500 lb GP | GP Bomb | 1941 | Bombs | Bomb | 1500 | 35 | 8 | 12 | 0 | 9200 | 9202 | 0 |
| 9202 | British | 1000 lb MC | GP Bomb | 1942 | Bombs | Bomb | 1800 | 42 | 10 | 15 | 0 | 9201 | 9203 | 0 |
| 9203 | British | 4000 lb HC | Heavy Bomb | 1943 | Bombs | Bomb | 2500 | 58 | 15 | 22 | 0 | 9202 | 9210 | 0 |
| 9210 | British | Tallboy | Heavy Bomb | 1944 | Bombs | Bomb | 4500 | 105 | 28 | 42 | 0 | 9203 | 9211 | 0 |
| 9211 | British | Grand Slam | Heavy Bomb | 1945 | Bombs | Bomb | 6000 | 138 | 38 | 55 | 0 | 9210 | 9220 | 0 |
| 9220 | British | 1000 lb GP (Post-war) | GP Bomb | 1950 | Bombs | Bomb | 2200 | 52 | 12 | 22 | 0 | 9211 | 9221 | 0 |
| 9221 | British | 1000 lb HE | GP Bomb | 1955 | Bombs | Bomb | 2500 | 58 | 14 | 25 | 0 | 9220 | 9222 | 0 |
| 9222 | British | Mk 13 (British) | GP Bomb | 1960 | Bombs | Bomb | 2800 | 65 | 16 | 28 | 0 | 9221 | 9230 | 0 |
| 9230 | British | Paveway II (RAF) | LGB | 1977 | Bombs | Bomb | 6200 | 142 | 32 | 62 | 0 | 9222 | 9231 | 0 |
| 9231 | British | Paveway III (RAF) | LGB | 1985 | Bombs | Bomb | 7500 | 172 | 38 | 78 | 0 | 9230 | 9232 | 0 |
| 9232 | British | Enhanced Paveway II | LGB | 1998 | Bombs | Bomb | 9500 | 218 | 48 | 105 | 0 | 9231 | 9240 | 0 |
| 9240 | British | Paveway IV | Dual-Mode | 2008 | Bombs | Bomb | 13000 | 302 | 62 | 152 | 0 | 9232 | 9241 | 0 |
| 9241 | British | SPEAR 3 | Powered Bomb | 2021 | Bombs | Bomb | 16500 | 382 | 72 | 198 | 0 | 9240 | | 0 |
| 9250 | British | BL755 | Cluster Bomb | 1973 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9251 | 0 |
| 9251 | British | RBL755 | Cluster Bomb | 1985 | Bombs | Bomb | 9500 | 125 | 32 | 65 | 0 | 9250 | | 0 |
| 9260 | British | Blue Danube | Nuclear | 1953 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9261 | 0 |
| 9261 | British | Red Beard | Nuclear | 1961 | Bombs | Bomb | 15000 | 348 | 0 | 208 | 0 | 9260 | 9262 | 0 |
| 9262 | British | WE.177 | Nuclear | 1966 | Bombs | Bomb | 18000 | 418 | 0 | 248 | 0 | 9261 | 9263 | 0 |
| 9263 | British | WE.177A/B | Nuclear | 1976 | Bombs | Bomb | 21000 | 488 | 0 | 295 | 0 | 9262 | | 0 |
| 9270 | British | CRV7 Pod | Rocket Pod | 1975 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9271 | 0 |
| 9271 | British | SNEB Rocket | Rocket Pod | 1980 | Bombs | Bomb | 3500 | 82 | 18 | 42 | 0 | 9270 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940-1953):
- 250 lb GP (Node 9200): WWII bomb lineage
- BL755 (Node 9250): Cluster munitions
- Blue Danube (Node 9260): Nuclear program
- CRV7 Pod (Node 9270): Unguided rockets

**Famous Systems**:
- Tallboy (1944): 12,000 lb earthquake bomb
- Grand Slam (1945): 22,000 lb superbomb
- Paveway IV (2008): Dual-mode GPS/laser guidance
- SPEAR 3 (2021): Network-enabled powered glide bomb

**Tree Depth**: 11 generations (1940-2021)
**Total Nodes**: 22
