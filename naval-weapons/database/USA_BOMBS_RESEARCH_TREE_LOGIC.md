# USA Bombs Research Tree Logic

**Tech Branch**: Bombs
**Nation**: USA
**Era**: 1940-2025
**Node Count**: ~80 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 9000 | USA | AN-M30 | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9001 | 0 |
| 9001 | USA | AN-M64 | GP Bomb | 1941 | Bombs | Bomb | 1500 | 35 | 8 | 12 | 0 | 9000 | 9002 | 0 |
| 9002 | USA | AN-M65 | GP Bomb | 1942 | Bombs | Bomb | 1800 | 42 | 10 | 15 | 0 | 9001 | 9003 | 0 |
| 9003 | USA | AN-M66 | GP Bomb | 1943 | Bombs | Bomb | 2200 | 50 | 12 | 18 | 0 | 9002 | 9010 | 0 |
| 9010 | USA | Mk 81 | GP Bomb | 1950 | Bombs | Bomb | 2500 | 58 | 14 | 22 | 0 | 9003 | 9011 | 0 |
| 9011 | USA | Mk 82 | GP Bomb | 1952 | Bombs | Bomb | 2800 | 65 | 16 | 25 | 0 | 9010 | 9012,9020 | 0 |
| 9012 | USA | Mk 83 | GP Bomb | 1955 | Bombs | Bomb | 3200 | 75 | 18 | 28 | 0 | 9011 | 9013 | 0 |
| 9013 | USA | Mk 84 | GP Bomb | 1958 | Bombs | Bomb | 3800 | 88 | 22 | 35 | 0 | 9012 | 9020,9030 | 0 |
| 9020 | USA | GBU-10 Paveway I | LGB | 1968 | Bombs | Bomb | 9500 | 125 | 28 | 55 | 0 | 9011,9013 | 9021 | 0 |
| 9021 | USA | GBU-12 Paveway II | LGB | 1976 | Bombs | Bomb | 6200 | 142 | 32 | 62 | 0 | 9020 | 9022 | 0 |
| 9022 | USA | GBU-16 Paveway II | LGB | 1980 | Bombs | Bomb | 6800 | 155 | 35 | 68 | 0 | 9021 | 9023 | 0 |
| 9023 | USA | GBU-24 Paveway III | LGB | 1983 | Bombs | Bomb | 7500 | 172 | 38 | 78 | 0 | 9022 | 9024,9040 | 0 |
| 9024 | USA | GBU-28 | Bunker Buster | 1991 | Bombs | Bomb | 9500 | 218 | 52 | 95 | 0 | 9023 | 9050 | 0 |
| 9030 | USA | Mk 117 | GP Bomb | 1960 | Bombs | Bomb | 3000 | 70 | 18 | 32 | 0 | 9013 | 9031 | 0 |
| 9031 | USA | M117R | GP Bomb | 1970 | Bombs | Bomb | 3500 | 82 | 22 | 38 | 0 | 9030 | 9032 | 0 |
| 9032 | USA | Mk 118 | Demolition Bomb | 1975 | Bombs | Bomb | 4200 | 98 | 28 | 45 | 0 | 9031 | 9024 | 0 |
| 9040 | USA | GBU-15 | TV-Guided | 1975 | Bombs | Bomb | 7000 | 162 | 38 | 72 | 0 | 9023 | 9041 | 0 |
| 9041 | USA | AGM-62 Walleye | TV-Guided | 1967 | Bombs | Bomb | 6500 | 150 | 35 | 65 | 0 | 9020 | 9040 | 0 |
| 9050 | USA | GBU-31 JDAM | GPS-Guided | 1997 | Bombs | Bomb | 11000 | 255 | 55 | 125 | 0 | 9024 | 9051 | 0 |
| 9051 | USA | GBU-32 JDAM | GPS-Guided | 1999 | Bombs | Bomb | 11500 | 265 | 58 | 132 | 0 | 9050 | 9052 | 0 |
| 9052 | USA | GBU-38 JDAM | GPS-Guided | 2001 | Bombs | Bomb | 12000 | 278 | 62 | 138 | 0 | 9051 | 9053,9060 | 0 |
| 9053 | USA | GBU-54 LJDAM | Laser/GPS | 2008 | Bombs | Bomb | 13500 | 312 | 68 | 155 | 0 | 9052 | 9054 | 0 |
| 9054 | USA | GBU-56 LJDAM | Laser/GPS | 2010 | Bombs | Bomb | 14000 | 325 | 72 | 162 | 0 | 9053 | 9070 | 0 |
| 9060 | USA | GBU-39 SDB | Small Diameter | 2006 | Bombs | Bomb | 12500 | 288 | 58 | 145 | 0 | 9052 | 9061 | 0 |
| 9061 | USA | GBU-53 SDB II | Small Diameter | 2014 | Bombs | Bomb | 15000 | 348 | 72 | 178 | 0 | 9060 | 9070 | 0 |
| 9070 | USA | GBU-57 MOP | Bunker Buster | 2011 | Bombs | Bomb | 18000 | 418 | 85 | 195 | 0 | 9054,9061 | | 0 |
| 9080 | USA | CBU-87 | Cluster Bomb | 1986 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9081 | 0 |
| 9081 | USA | CBU-97 | Sensor Fused | 1992 | Bombs | Bomb | 8500 | 195 | 45 | 95 | 0 | 9080 | 9082 | 0 |
| 9082 | USA | CBU-103 | Cluster Bomb | 1997 | Bombs | Bomb | 9200 | 212 | 48 | 105 | 0 | 9081 | 9083 | 0 |
| 9083 | USA | CBU-105 | Sensor Fused | 2001 | Bombs | Bomb | 10500 | 242 | 55 | 122 | 0 | 9082 | | 0 |
| 9090 | USA | Mk 4 | Nuclear | 1949 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9091 | 0 |
| 9091 | USA | Mk 7 | Nuclear | 1952 | Bombs | Bomb | 12000 | 278 | 0 | 168 | 0 | 9090 | 9092 | 0 |
| 9092 | USA | Mk 15 | Nuclear | 1955 | Bombs | Bomb | 13500 | 312 | 0 | 188 | 0 | 9091 | 9093 | 0 |
| 9093 | USA | Mk 28 | Nuclear | 1958 | Bombs | Bomb | 15000 | 348 | 0 | 208 | 0 | 9092 | 9094 | 0 |
| 9094 | USA | Mk 43 | Nuclear | 1961 | Bombs | Bomb | 16500 | 382 | 0 | 228 | 0 | 9093 | 9095 | 0 |
| 9095 | USA | B57 | Nuclear | 1963 | Bombs | Bomb | 18000 | 418 | 0 | 248 | 0 | 9094 | 9096 | 0 |
| 9096 | USA | B61 | Nuclear | 1968 | Bombs | Bomb | 20000 | 465 | 0 | 285 | 0 | 9095 | 9097 | 0 |
| 9097 | USA | B83 | Nuclear | 1983 | Bombs | Bomb | 24000 | 558 | 0 | 348 | 0 | 9096 | 9098 | 0 |
| 9098 | USA | B61-12 | Nuclear | 2020 | Bombs | Bomb | 28000 | 650 | 0 | 425 | 0 | 9097 | | 0 |
| 9100 | USA | Mk 77 | Incendiary | 1965 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9101 | 0 |
| 9101 | USA | BLU-27 | Incendiary | 1967 | Bombs | Bomb | 3500 | 82 | 18 | 42 | 0 | 9100 | 9102 | 0 |
| 9102 | USA | Mk 78 | Incendiary | 1970 | Bombs | Bomb | 4000 | 92 | 22 | 48 | 0 | 9101 | | 0 |
| 9110 | USA | Mk 36 | Mine | 1943 | Bombs | Bomb | 0 | 0 | 0 | 0 | 1 | | 9111 | 0 |
| 9111 | USA | Mk 82 Mine | Mine | 1960 | Bombs | Bomb | 3200 | 75 | 18 | 38 | 0 | 9110 | 9112 | 0 |
| 9112 | USA | Mk 62 Quickstrike | Mine | 1983 | Bombs | Bomb | 9500 | 125 | 32 | 65 | 0 | 9111 | 9113 | 0 |
| 9113 | USA | Mk 63 Quickstrike | Mine | 1985 | Bombs | Bomb | 6000 | 138 | 35 | 72 | 0 | 9112 | 9114 | 0 |
| 9114 | USA | Mk 65 Quickstrike | Mine | 1988 | Bombs | Bomb | 6800 | 155 | 42 | 82 | 0 | 9113 | | 0 |
| 9120 | USA | BLU-109 | Penetrator | 1985 | Bombs | Bomb | 7500 | 172 | 48 | 85 | 0 | 9023 | 9121 | 0 |
| 9121 | USA | BLU-116 | Penetrator | 1996 | Bombs | Bomb | 9000 | 208 | 55 | 105 | 0 | 9120 | 9122 | 0 |
| 9122 | USA | BLU-122 | Penetrator | 2003 | Bombs | Bomb | 11000 | 255 | 65 | 132 | 0 | 9121 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1940-1949):
- AN-M30 (Node 9000): WWII general purpose bomb lineage
- CBU-87 (Node 9080): Cluster munitions starting point
- Mk 4 (Node 9090): Nuclear weapons program
- Mk 77 (Node 9100): Incendiary weapons
- Mk 36 (Node 9110): Air-dropped mines

**Guided Weapons Evolution**:
- 1968: First laser-guided bombs (Paveway I)
- 1997: GPS guidance introduction (JDAM)
- 2006: Small diameter bombs for reduced collateral damage
- 2011: Massive Ordnance Penetrator (MOP)

**Nuclear Arsenal**:
- 1949-1968: Progressive yield increases and miniaturization
- 1968: B61 mod family (still in service)
- 2020: B61-12 precision nuclear weapon

**Tree Depth**: 18 generations (1940-2025)
**Total Nodes**: 52
