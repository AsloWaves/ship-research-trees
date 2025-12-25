# German Bombs Research Tree Logic

**Tech Branch**: Bombs
**Nation**: German
**Era**: 1940-2025
**Node Count**: ~28 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 9300 | German | SC 50 | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9301 | 0 |
| 9301 | German | SC 250 | GP Bomb | 1941 | Bombs | Bomb | 1500 | 35 | 8 | 12 | 0 | 9300 | 9302 | 0 |
| 9302 | German | SC 500 | GP Bomb | 1942 | Bombs | Bomb | 1800 | 42 | 10 | 15 | 0 | 9301 | 9303 | 0 |
| 9303 | German | SC 1000 | GP Bomb | 1943 | Bombs | Bomb | 2200 | 52 | 12 | 18 | 0 | 9302 | 9310 | 0 |
| 9310 | German | SC 1800 | Heavy Bomb | 1944 | Bombs | Bomb | 3500 | 82 | 18 | 28 | 0 | 9303 | 9311 | 0 |
| 9311 | German | PC 1400 | AP Bomb | 1943 | Bombs | Bomb | 4000 | 92 | 22 | 35 | 0 | 9303 | 9320 | 0 |
| 9320 | German | Fritz X | Guided Bomb | 1943 | Bombs | Bomb | 9500 | 125 | 28 | 55 | 0 | 9311 | 9321 | 0 |
| 9321 | German | Hs 293 | Glide Bomb | 1943 | Bombs | Bomb | 9800 | 135 | 32 | 62 | 0 | 9320 | 9330 | 0 |
| 9330 | German | 250 kg (Bundeswehr) | GP Bomb | 1960 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9331 | 0 |
| 9331 | German | 500 kg (Bundeswehr) | GP Bomb | 1965 | Bombs | Bomb | 2500 | 58 | 14 | 22 | 0 | 9330 | 9332 | 0 |
| 9332 | German | DM 91 | GP Bomb | 1975 | Bombs | Bomb | 3000 | 70 | 18 | 28 | 0 | 9331 | 9340 | 0 |
| 9340 | German | GBU-12 (Luftwaffe) | LGB | 1985 | Bombs | Bomb | 6200 | 142 | 32 | 62 | 0 | 9332 | 9341 | 0 |
| 9341 | German | GBU-24 (Luftwaffe) | LGB | 1995 | Bombs | Bomb | 7500 | 172 | 38 | 78 | 0 | 9340 | 9350 | 0 |
| 9350 | German | GBU-38 (Luftwaffe) | GPS-Guided | 2010 | Bombs | Bomb | 12000 | 278 | 62 | 138 | 0 | 9341 | 9351 | 0 |
| 9351 | German | GBU-54 (Luftwaffe) | Laser/GPS | 2015 | Bombs | Bomb | 13500 | 312 | 68 | 155 | 0 | 9350 | | 0 |
| 9360 | German | MW-1 | Cluster Munition | 1982 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9361 | 0 |
| 9361 | German | DM 118 | Dispenser | 1990 | Bombs | Bomb | 6500 | 150 | 38 | 72 | 0 | 9360 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940-1982):
- SC 50 (Node 9300): WWII bomb lineage
- 250 kg Bundeswehr (Node 9330): Post-war restart
- MW-1 (Node 9360): NATO-era cluster munitions

**WWII Innovation**:
- Fritz X (1943): First operational guided bomb (radio-controlled)
- Hs 293 (1943): First glide bomb with rocket booster
- PC 1400: Armor-piercing for ships

**NATO Integration**:
- Post-1960: Adoption of NATO standard bombs
- 1985+: US Paveway and JDAM integration

**Tree Depth**: 10 generations (1940-2015)
**Total Nodes**: 17
