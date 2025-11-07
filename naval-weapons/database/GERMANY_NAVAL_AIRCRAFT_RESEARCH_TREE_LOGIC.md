# German Naval Aircraft Research Tree Logic

**Tech Branch**: Naval Aircraft
**Nation**: German
**Era**: 1970-2025
**Node Count**: ~20 nodes

## Research Tree Structure

| Node_ID | Nation | Designation | Type | Year | Tech_Branch | Item_Type | Research_Cost | Build_Days | Steel | Electronics | Is_Starting_Tech | Requires_Tech_IDs | Unlocks_Tech_IDs | Modded |
|---------|--------|-------------|------|------|-------------|-----------|---------------|------------|-------|-------------|------------------|-------------------|------------------|--------|
| 3300 | German | Tornado IDS (Naval) | Strike | 1979 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3301 | 0 |
| 3301 | German | Tornado IDS Mid-Life | Strike | 1995 | Naval Aircraft | Aircraft | 8000 | 185 | 42 | 105 | 0 | 3300 | 3302 | 0 |
| 3302 | German | Eurofighter Typhoon (Naval) | Multi-Role | 2004 | Naval Aircraft | Aircraft | 12000 | 280 | 52 | 145 | 0 | 3301 | | 0 |
| 3310 | German | Breguet Atlantic | ASW/Patrol | 1972 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3311 | 0 |
| 3311 | German | Atlantic 1 Mod | ASW/Patrol | 1981 | Naval Aircraft | Aircraft | 6000 | 140 | 35 | 78 | 0 | 3310 | 3312 | 0 |
| 3312 | German | P-3C Orion (German) | ASW/Patrol | 1995 | Naval Aircraft | Aircraft | 9000 | 210 | 45 | 115 | 0 | 3311 | 3313 | 0 |
| 3313 | German | P-8A Poseidon (German) | ASW/Patrol | 2022 | Naval Aircraft | Aircraft | 15000 | 350 | 58 | 175 | 0 | 3312 | | 0 |
| 3320 | German | Sea King Mk 41 | ASW Helo | 1972 | Naval Aircraft | Aircraft | 0 | 0 | 0 | 0 | 1 | | 3321 | 0 |
| 3321 | German | Sea King Mk 41 Mod | ASW Helo | 1985 | Naval Aircraft | Aircraft | 4500 | 105 | 25 | 62 | 0 | 3320 | 3322 | 0 |
| 3322 | German | Sea Lynx Mk 88 | ASW Helo | 1981 | Naval Aircraft | Aircraft | 4000 | 90 | 22 | 58 | 0 | 3321 | 3323 | 0 |
| 3323 | German | Super Lynx Mk 88A | ASW Helo | 2001 | Naval Aircraft | Aircraft | 5500 | 125 | 28 | 78 | 0 | 3322 | 3324 | 0 |
| 3324 | German | NH90 Sea Lion | Multi-Role Helo | 2019 | Naval Aircraft | Aircraft | 8000 | 185 | 38 | 118 | 0 | 3323 | | 0 |
| 3330 | German | MH-60R Seahawk (German) | ASW Helo | 2025 | Naval Aircraft | Aircraft | 10000 | 235 | 45 | 135 | 0 | 3324 | | 0 |
| 3340 | German | Do 24 (Reactivated) | Maritime Patrol | 1975 | Naval Aircraft | Aircraft | 2000 | 50 | 18 | 28 | 0 | 3310 | | 0 |

## Nation Progression Logic

**Starting Technologies** (1970):
- Tornado IDS (Node 3300): Strike capability
- Breguet Atlantic (Node 3310): NATO maritime patrol
- Sea King Mk 41 (Node 3320): ASW helicopter

**Technology Philosophy**:
- No carrier-based operations (no carriers)
- Focus on land-based maritime patrol
- NATO interoperability (P-3C, P-8A)
- Modern multi-role helicopters

**Tree Depth**: 8 generations (1970-2025)
