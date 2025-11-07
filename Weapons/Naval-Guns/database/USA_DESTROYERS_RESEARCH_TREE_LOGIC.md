# USA Destroyers Research Tree Logic

**Date**: October 10, 2025
**Ship Type**: Destroyers (DD, DDG, DDR, APD, DL)
**Total Nodes**: 42 (7000-7041)

---

## Research Branches Overview

| Branch_ID | Branch_Name | Branch_Description | Start_Node | End_Node | Nodes |
|-----------|-------------|-------------------|------------|----------|-------|
| 23 | Starting | FREE starting destroyers, tutorial introduction | 7000 | 7001 | 2 |
| 24 | Pre-WWI | Early torpedo boat destroyers, pre-WWI fleet destroyers | 7002 | 7004 | 3 |
| 25 | Four-Stacker | WWI flush-deck mass production, four-stack destroyers | 7005 | 7007 | 3 |
| 26 | Interwar | Treaty-era destroyers, balanced gun-torpedo designs | 7009 | 7013 | 5 |
| 27 | Pre-WWII | Late 1930s refined designs leading to WWII standard | 7014 | 7018 | 5 |
| 28 | WWII Main Line | Fletcher, Sumner, Gearing - WWII mass production workhorses | 7019 | 7022 | 4 |
| 29 | Modernization | FRAM I/II ASW upgrades, Cold War modernizations | 7020 | 7023 | 2 |
| 30 | Alternative | High-speed transports (APD), radar pickets (DDR), niche roles | 7008 | 7024 | 2 |
| 31 | Post-War/Missile | First post-war designs, transition to guided missiles | 7025 | 7030 | 6 |
| 32 | Gas Turbine | Revolutionary gas turbine propulsion, Spruance-class | 7031 | 7033 | 3 |
| 33 | Aegis Main Line | Arleigh Burke-class progression through all flights | 7034 | 7037 | 4 |
| 34 | Stealth/Future | Stealth destroyer and future concepts | 7038 | 7040 | 3 |

---

## Prerequisites Table Entries

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 147 | 7002 | 7001 | Smith-class | 1 | 1 | Paulding requires Bainbridge OR Smith |
| 148 | 7002 | 7000 | Bainbridge-class | 1 | 1 | Paulding requires Bainbridge OR Smith |
| 149 | 7003 | 7002 | Paulding-class | 1 | NULL | Cassin requires Paulding |
| 150 | 7004 | 7003 | Cassin-class | 1 | NULL | Sampson requires Cassin |
| 151 | 7005 | 7004 | Sampson-class | 1 | NULL | Caldwell requires Sampson (first flush-deck) |
| 152 | 7006 | 7005 | Caldwell-class | 1 | NULL | Wickes requires Caldwell |
| 153 | 7007 | 7006 | Wickes-class | 1 | NULL | Clemson requires Wickes |
| 154 | 7008 | 7006 | Wickes-class | 1 | 1 | Wickes APD requires Wickes OR Clemson |
| 155 | 7008 | 7007 | Clemson-class | 1 | 1 | Wickes APD requires Wickes OR Clemson |
| 156 | 7009 | 7007 | Clemson-class | 1 | NULL | Farragut requires Clemson (interwar gap) |
| 157 | 7010 | 7009 | Farragut-class | 1 | NULL | Porter requires Farragut (leader variant) |
| 158 | 7011 | 7009 | Farragut-class | 1 | NULL | Mahan requires Farragut |
| 159 | 7012 | 7011 | Mahan-class | 1 | NULL | Gridley requires Mahan (torpedo focus) |
| 160 | 7013 | 7011 | Mahan-class | 1 | 1 | Bagley requires Mahan OR Gridley |
| 161 | 7013 | 7012 | Gridley-class | 1 | 1 | Bagley requires Mahan OR Gridley |
| 162 | 7014 | 7013 | Bagley-class | 1 | 1 | Benham requires Bagley OR Porter |
| 163 | 7014 | 7010 | Porter-class | 1 | 1 | Benham requires Bagley OR Porter |
| 164 | 7015 | 7013 | Bagley-class | 1 | NULL | Sims requires Bagley |
| 165 | 7016 | 7014 | Benham-class | 1 | 1 | Benson requires Benham OR Sims |
| 166 | 7016 | 7015 | Sims-class | 1 | 1 | Benson requires Benham OR Sims |
| 167 | 7017 | 7016 | Benson-class | 1 | NULL | Gleaves requires Benson (variant) |
| 168 | 7018 | 7016 | Benson-class | 1 | NULL | Bristol requires Benson (subclass) |
| 169 | 7019 | 7017 | Gleaves-class | 1 | 1 | Fletcher requires Gleaves OR Bristol |
| 170 | 7019 | 7018 | Bristol-class | 1 | 1 | Fletcher requires Gleaves OR Bristol |
| 171 | 7020 | 7019 | Fletcher-class | 1 | NULL | Fletcher FRAM requires base Fletcher |
| 172 | 7021 | 7019 | Fletcher-class | 1 | NULL | Sumner requires Fletcher |
| 173 | 7022 | 7021 | Allen M. Sumner-class | 1 | NULL | Gearing requires Sumner |
| 174 | 7023 | 7022 | Gearing-class | 1 | NULL | Gearing FRAM requires base Gearing |
| 175 | 7024 | 7022 | Gearing-class | 1 | NULL | Gearing DDR requires base Gearing |
| 176 | 7025 | 7022 | Gearing-class | 1 | NULL | Forrest Sherman requires Gearing (post-war) |
| 177 | 7026 | 7025 | Forrest Sherman-class | 1 | NULL | Forrest Sherman DDG requires base |
| 178 | 7027 | 7010 | Porter-class | 1 | NULL | Mitscher requires Porter (large leader) |
| 179 | 7028 | 7025 | Forrest Sherman-class | 1 | 1 | Farragut DDG requires Forrest Sherman OR Mitscher |
| 180 | 7028 | 7027 | Mitscher-class | 1 | 1 | Farragut DDG requires Forrest Sherman OR Mitscher |
| 181 | 7029 | 7028 | Farragut/Coontz-class | 1 | NULL | Charles F. Adams requires Farragut DDG |
| 182 | 7030 | 7029 | Charles F. Adams-class | 1 | NULL | Adams NTU requires base Adams |
| 183 | 7031 | 7029 | Charles F. Adams-class | 1 | NULL | Spruance requires Adams (gas turbine leap) |
| 184 | 7032 | 7031 | Spruance-class | 1 | NULL | Spruance VLS requires base Spruance |
| 185 | 7033 | 7031 | Spruance-class | 1 | NULL | Kidd requires Spruance (modified) |
| 186 | 7034 | 7033 | Kidd-class | 1 | NULL | Arleigh Burke F1 requires Kidd (Aegis) |
| 187 | 7035 | 7034 | Arleigh Burke-class (Flight I) DDG-51-71 | 1 | NULL | Burke F2 requires F1 |
| 188 | 7036 | 7035 | Arleigh Burke-class (Flight II) DDG-72-78 | 1 | NULL | Burke F2A requires F2 |
| 189 | 7037 | 7036 | Arleigh Burke-class (Flight IIA) DDG-79-112 | 1 | NULL | Burke F3 requires F2A |
| 190 | 7038 | 7036 | Arleigh Burke-class (Flight IIA) DDG-79-112 | 1 | NULL | Zumwalt requires Burke F2A (stealth) |
| 191 | 7039 | 7037 | Arleigh Burke-class (Flight III) DDG-113+ | 1 | NULL | Burke F4 requires F3 (future) |
| 192 | 7040 | 7037 | Arleigh Burke-class (Flight III) DDG-113+ | 1 | NULL | DDG(X) requires F3 (paper ship) |

**Total Prerequisites**: 46 entries

---

## Unlocks Table Entries

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 247 | 7000 | 7002 | Paulding-class | 1 | 1 | Bainbridge unlocks Paulding |
| 248 | 7001 | 7002 | Paulding-class | 1 | 1 | Smith unlocks Paulding |
| 249 | 7002 | 7003 | Cassin-class | 1 | 1 | Paulding unlocks Cassin |
| 250 | 7003 | 7004 | Sampson-class | 1 | 1 | Cassin unlocks Sampson |
| 251 | 7004 | 7005 | Caldwell-class | 1 | 1 | Sampson unlocks Caldwell (flush-deck) |
| 252 | 7005 | 7006 | Wickes-class | 1 | 1 | Caldwell unlocks Wickes |
| 253 | 7006 | 7007 | Clemson-class | 1 | 1 | Wickes unlocks Clemson |
| 254 | 7006 | 7008 | Wickes-class (APD) | 1 | 2 | Wickes unlocks APD conversion |
| 255 | 7007 | 7008 | Wickes-class (APD) | 1 | 2 | Clemson unlocks APD conversion |
| 256 | 7007 | 7009 | Farragut-class | 1 | 1 | Clemson unlocks Farragut (interwar) |
| 257 | 7009 | 7010 | Porter-class | 1 | 2 | Farragut unlocks Porter (leader) |
| 258 | 7009 | 7011 | Mahan-class | 1 | 1 | Farragut unlocks Mahan |
| 259 | 7010 | 7027 | Mitscher-class | 1 | 2 | Porter unlocks Mitscher (large leader) |
| 260 | 7011 | 7012 | Gridley-class | 1 | 2 | Mahan unlocks Gridley (torpedo) |
| 261 | 7011 | 7013 | Bagley-class | 1 | 1 | Mahan unlocks Bagley |
| 262 | 7012 | 7013 | Bagley-class | 1 | 1 | Gridley unlocks Bagley |
| 263 | 7013 | 7014 | Benham-class | 1 | 1 | Bagley unlocks Benham |
| 264 | 7013 | 7015 | Sims-class | 1 | 1 | Bagley unlocks Sims (alternative) |
| 265 | 7010 | 7014 | Benham-class | 1 | 1 | Porter unlocks Benham |
| 266 | 7014 | 7016 | Benson-class | 1 | 1 | Benham unlocks Benson |
| 267 | 7015 | 7016 | Benson-class | 1 | 1 | Sims unlocks Benson |
| 268 | 7016 | 7017 | Gleaves-class | 1 | 1 | Benson unlocks Gleaves |
| 269 | 7016 | 7018 | Bristol-class | 1 | 1 | Benson unlocks Bristol |
| 270 | 7017 | 7019 | Fletcher-class | 1 | 1 | Gleaves unlocks Fletcher |
| 271 | 7018 | 7019 | Fletcher-class | 1 | 1 | Bristol unlocks Fletcher |
| 272 | 7019 | 7020 | Fletcher-class (FRAM I) | 1 | 2 | Fletcher unlocks FRAM upgrade |
| 273 | 7019 | 7021 | Allen M. Sumner-class | 1 | 1 | Fletcher unlocks Sumner |
| 274 | 7021 | 7022 | Gearing-class | 1 | 1 | Sumner unlocks Gearing |
| 275 | 7022 | 7023 | Gearing-class (FRAM I) | 1 | 2 | Gearing unlocks FRAM upgrade |
| 276 | 7022 | 7024 | Gearing-class (DDR) | 1 | 2 | Gearing unlocks DDR conversion |
| 277 | 7022 | 7025 | Forrest Sherman-class | 1 | 1 | Gearing unlocks Forrest Sherman |
| 278 | 7025 | 7026 | Forrest Sherman-class DDG | 1 | 2 | Forrest Sherman unlocks DDG conversion |
| 279 | 7025 | 7028 | Farragut/Coontz-class | 1 | 1 | Forrest Sherman unlocks Farragut DDG |
| 280 | 7027 | 7028 | Farragut/Coontz-class | 1 | 1 | Mitscher unlocks Farragut DDG |
| 281 | 7028 | 7029 | Charles F. Adams-class | 1 | 1 | Farragut DDG unlocks Adams |
| 282 | 7029 | 7030 | Charles F. Adams-class (NTU) | 1 | 2 | Adams unlocks NTU upgrade |
| 283 | 7029 | 7031 | Spruance-class | 1 | 1 | Adams unlocks Spruance (gas turbine) |
| 284 | 7031 | 7032 | Spruance-class (VLS) | 1 | 2 | Spruance unlocks VLS upgrade |
| 285 | 7031 | 7033 | Kidd-class | 1 | 2 | Spruance unlocks Kidd (modified) |
| 286 | 7033 | 7034 | Arleigh Burke-class (Flight I) DDG-51-71 | 1 | 1 | Kidd unlocks Burke F1 (Aegis) |
| 287 | 7034 | 7035 | Arleigh Burke-class (Flight II) DDG-72-78 | 1 | 1 | Burke F1 unlocks F2 |
| 288 | 7035 | 7036 | Arleigh Burke-class (Flight IIA) DDG-79-112 | 1 | 1 | Burke F2 unlocks F2A |
| 289 | 7036 | 7037 | Arleigh Burke-class (Flight III) DDG-113+ | 1 | 1 | Burke F2A unlocks F3 |
| 290 | 7036 | 7038 | Zumwalt-class | 1 | 2 | Burke F2A unlocks Zumwalt (stealth) |
| 291 | 7037 | 7039 | Arleigh Burke-class (Flight IV) | 1 | 2 | Burke F3 unlocks F4 (future) |
| 292 | 7037 | 7040 | DDG(X) Future Destroyer | 1 | 3 | Burke F3 unlocks DDG(X) (paper) |

**Total Unlocks**: 46 entries

---

## Research Branches Table Entries

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 23 | USA | DD | Starting | FREE starting destroyers, tutorial introduction | #696969 | 7000 | 7001 | NULL | NULL | Early Destroyer | Early Destroyer | Bainbridge + Smith. FREE starting ships. Bainbridge (1902) first US destroyer, Smith (1909) better option. |
| 24 | USA | DD | Pre-WWI | Early torpedo boat destroyers, pre-WWI fleet progression | #8B4513 | 7002 | 7004 | NULL | NULL | Pre-WWI | Pre-WWI | Paulding → Cassin → Sampson. 700-1,200 tons. Oil-fired boilers, improved range. Final pre-WWI designs. |
| 25 | USA | DD | Four-Stacker | WWI flush-deck mass production, four-stack destroyers | #FFD700 | 7005 | 7007 | 24 | NULL | WWI | WWI | Caldwell → Wickes → Clemson. Stems from Pre-WWI. Flush deck design. 267 ships total (111 Wickes + 156 Clemson). Largest DD classes. |
| 26 | USA | DD | Interwar | Treaty-era destroyers, balanced gun-torpedo designs | #1E90FF | 7009 | 7013 | 25 | NULL | Interwar | Interwar | Farragut → Mahan → Gridley/Bagley. Stems from Four-Stacker. Enclosed guns, improved seakeeping. Torpedo focus (12-16 tubes). |
| 27 | USA | DD | Pre-WWII | Late 1930s refined designs leading to WWII standard | #9370DB | 7014 | 7018 | 26 | NULL | Pre-War | Pre-War | Benham → Sims → Benson → Gleaves → Bristol. Stems from Interwar. Refined pre-war designs. Bridge to Fletcher. |
| 28 | USA | DD | WWII Main Line | Fletcher, Sumner, Gearing - WWII mass production workhorses | #DC143C | 7019 | 7022 | 27 | NULL | WWII Workhorse | Ultimate WWII | Fletcher → Sumner → Gearing. Stems from Pre-WWII. 175 Fletcher + 67 Sumner + 98 Gearing = 340 ships. Most successful DD classes. |
| 29 | USA | DD | Modernization | FRAM I/II ASW upgrades, Cold War modernizations | #CD853F | 7020 | 7023 | 28 | NULL | FRAM Upgrade | FRAM Upgrade | Fletcher FRAM, Gearing FRAM. Stems from WWII Main Line. 1960s ASW modernizations. DASH helicopter, ASROC, new sonars. Extends service life 15+ years. |
| 30 | USA | DD/DDR/APD | Alternative | High-speed transports (APD), radar pickets (DDR), niche roles | #FF8C00 | 7008 | 7024 | 25, 28 | NULL | WWII Conversion | Radar Picket | Wickes APD, Gearing DDR. Stems from Four-Stacker and WWII lines. APD: 200 troops. DDR: early warning radar. Niche conversions. |
| 31 | USA | DD/DDG/DL | Post-War/Missile | First post-war designs, transition to guided missiles | #BA55D3 | 7025 | 7030 | 28 | NULL | First Post-War | NTU Upgrade | Forrest Sherman → Farragut DDG → Adams → Adams NTU. Stems from WWII. First post-war all-gun (Sherman) to first missile DDG (Farragut). 3"/50 guns to Tartar SAM. |
| 32 | USA | DD/DDG | Gas Turbine | Revolutionary gas turbine propulsion, Spruance-class era | #00CED1 | 7031 | 7033 | 31 | NULL | Gas Turbine DD | Modified Spruance | Spruance → Spruance VLS → Kidd. Stems from Post-War/Missile. First gas turbine DD (4× LM2500). 31 Spruance + 4 Kidd. Revolutionary propulsion. |
| 33 | USA | DDG | Aegis Main Line | Arleigh Burke-class progression through all flights | #FF1493 | 7034 | 7037 | 32 | NULL | Early Aegis DD | Ultimate Aegis | Burke F1 → F2 → F2A → F3. Stems from Gas Turbine. SPY-1D Aegis. Flight I-III: 89+ ships. Most numerous Aegis destroyer. Ultimate production DDG. |
| 34 | USA | DDG | Stealth/Future | Stealth destroyer and future next-generation concepts | #696969 | 7038 | 7040 | 33 | NULL | Stealth | Future | Zumwalt → Burke F4 → DDG(X). Stems from Aegis. Zumwalt: 3 ships, stealth, tumblehome. Burke F4 & DDG(X): future/paper designs. |

**Total Research Branches**: 12 entries

---

## Summary Statistics

- **Total Nodes**: 42 destroyer nodes (7000-7041)
- **Total Prerequisites**: 46 entries
- **Total Unlocks**: 46 entries
- **Total Research Branches**: 12 branches
- **Total Database Entries**: 104 entries for USA Destroyers research tree logic

---

## Unlock Chain Flowchart

```
USA DESTROYER RESEARCH TREE - NAVYFIELD STYLE
════════════════════════════════════════════════════════════════

TIER 1: STARTING (FREE)
────────────────────────────────────────────────────────────────
        [7000] BAINBRIDGE       [7001] SMITH
        First US DD              Better Starting DD
        420 tons, FREE           700 tons, FREE
                    │                     │
                    └──────────┬──────────┘
                               │
TIER 2: PRE-WWI
────────────────────────────────────────────────────────────────
                    [7002] PAULDING
                    742 tons, 5×3" guns
                               │
                    [7003] CASSIN
                    1,010 tons, oil-fired
                               │
                    [7004] SAMPSON
                    1,200 tons, 4×4" guns
                               │
TIER 3: WWI FOUR-STACKERS
────────────────────────────────────────────────────────────────
                    [7005] CALDWELL
                    First flush-deck, 6×4"
                               │
                    [7006] WICKES           [7008] WICKES APD
                    111 ships                Fast transport
                               │                     │
                    [7007] CLEMSON              (Alternative)
                    156 ships, largest
                               │
TIER 4: INTERWAR
────────────────────────────────────────────────────────────────
                    [7009] FARRAGUT
                    Enclosed guns, 1,400 tons
                        │           │
                        │      [7010] PORTER
                        │      Leader, 8×5" guns
                        │           │
                    [7011] MAHAN
                    12 torpedoes
                        │       │
                        │   [7012] GRIDLEY
                        │   16 torpedoes max
                        │       │
                    [7013] BAGLEY
                    Balanced design
                               │
TIER 5: PRE-WWII
────────────────────────────────────────────────────────────────
                [7014] BENHAM       [7015] SIMS
                Refined             Lighter
                        │               │
                        └───────┬───────┘
                                │
                        [7016] BENSON
                        Standard 5×5"
                            │       │
                    [7017] GLEAVES  [7018] BRISTOL
                    Benson variant  Benson subclass
                            │           │
TIER 6: WWII MAIN LINE
────────────────────────────────────────────────────────────────
                        [7019] FLETCHER
                        175 ships, ultimate WWII
                            │       │
                    [7020] FLETCHER [7021] SUMNER
                    FRAM upgrade    6×5" guns, 67 ships
                    (Modernization)         │
                                    [7022] GEARING
                                    98 ships, lengthened
                                    │       │       │
                            [7023]  │   [7024]    │
                            GEARING │   GEARING   │
                            FRAM    │   DDR       │
                                    │             │
TIER 7: POST-WAR / MISSILE ERA
────────────────────────────────────────────────────────────────
                    [7025] FORREST SHERMAN     [7027] MITSCHER
                    First post-war DD          Large DL leader
                            │                       │
                    [7026] SHERMAN DDG              │
                    Tartar conversion               │
                            │                       │
                            └───────┬───────────────┘
                                    │
                        [7028] FARRAGUT/COONTZ DDG
                        First purpose missile DD, 10 ships
                                    │
                        [7029] CHARLES F. ADAMS
                        Tartar DDG, 23 ships
                                │       │
                        [7030] ADAMS    │
                        (NTU)           │
TIER 8: GAS TURBINE ERA
────────────────────────────────────────────────────────────────
                        [7031] SPRUANCE
                        Gas turbine, 31 ships
                            │       │
                    [7032]  │   [7033] KIDD
                    SPRUANCE│   Modified, 4 ships
                    (VLS)   │
                            │
TIER 9: AEGIS MAIN LINE
────────────────────────────────────────────────────────────────
                    [7034] ARLEIGH BURKE (Flight I)
                    DDG-51-71, Aegis SPY-1D, 90 VLS
                                │
                    [7035] BURKE (Flight II)
                    DDG-72-78, improved systems
                                │
                    [7036] BURKE (Flight IIA)
                    DDG-79-112, helo hangar, 96 VLS
                            │       │
                    [7037]  │   [7038] ZUMWALT
                    BURKE F3│   Stealth, 3 ships
                    SPY-6   │
                            │
TIER 10: FUTURE
────────────────────────────────────────────────────────────────
            [7039] BURKE (Flight IV)    [7040] DDG(X)
            Hypersonics planned          Next-gen concept
            2030s                        Paper design
```

---

**Status**: ✅ USA Destroyers Research Tree Logic COMPLETE
