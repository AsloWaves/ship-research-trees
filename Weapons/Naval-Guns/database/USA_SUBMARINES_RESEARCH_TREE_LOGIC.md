# USA Submarines Research Tree Logic

**Date**: October 10, 2025
**Ship Type**: Submarines (SS, SSN, SSBN, SSGN, SST, SSK)
**Total Nodes**: 39 (8000-8038)

---

## Research Branches Overview

| Branch_ID | Branch_Name | Branch_Description | Start_Node | End_Node | Nodes |
|-----------|-------------|-------------------|------------|----------|-------|
| 35 | Starting | FREE starting submarines, tutorial introduction | 8000 | 8001 | 2 |
| 36 | Coastal | Small coastal patrol submarines, limited range | 8002 | 8004 | 3 |
| 37 | Fleet Diesel | WWI/Interwar ocean-going diesel fleet submarines | 8005 | 8012 | 8 |
| 38 | WWII Main Line | Gato, Balao, Tench - WWII mass production diesel submarines | 8013 | 8019 | 7 |
| 39 | Modernization | GUPPY snorkel upgrades, Cold War diesel modernizations | 8020 | 8021 | 2 |
| 40 | Nuclear Attack | Nuclear-powered attack submarines, unlimited range | 8022 | 8037 | 12 |
| 41 | Ballistic Missile | Strategic ballistic missile submarines (SSBN) | 8025 | 8038 | 6 |
| 42 | Alternative | Experimental designs, training subs, cruise missile conversions | 8009 | 8035 | 4 |

---

## Prerequisites Table Entries

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 193 | 8002 | 8001 | A-class | 1 | 1 | C-class requires Holland OR A-class |
| 194 | 8002 | 8000 | Holland-class | 1 | 1 | C-class requires Holland OR A-class |
| 195 | 8003 | 8002 | C-class | 1 | NULL | F-class requires C-class |
| 196 | 8004 | 8003 | F-class | 1 | NULL | H-class requires F-class |
| 197 | 8005 | 8004 | H-class | 1 | NULL | L-class requires H-class (first fleet) |
| 198 | 8006 | 8005 | L-class | 1 | NULL | O-class requires L-class |
| 199 | 8007 | 8006 | O-class | 1 | NULL | R-class requires O-class |
| 200 | 8008 | 8007 | R-class | 1 | NULL | S-class requires R-class |
| 201 | 8009 | 8007 | R-class | 1 | NULL | V-class requires R-class (experimental cruiser) |
| 202 | 8010 | 8008 | S-class | 1 | NULL | Porpoise requires S-class (pre-war) |
| 203 | 8011 | 8010 | Porpoise-class | 1 | NULL | Salmon requires Porpoise |
| 204 | 8012 | 8011 | Salmon-class | 1 | NULL | Sargo requires Salmon |
| 205 | 8013 | 8012 | Sargo-class | 1 | NULL | Tambor requires Sargo (WWII begins) |
| 206 | 8014 | 8013 | Tambor-class | 1 | NULL | Gar requires Tambor |
| 207 | 8015 | 8004 | H-class | 1 | NULL | Mackerel requires H-class (training) |
| 208 | 8016 | 8015 | Mackerel-class | 1 | NULL | Barracuda requires Mackerel (SST) |
| 209 | 8017 | 8014 | Gar-class | 1 | 1 | Gato requires Gar OR Tambor |
| 210 | 8017 | 8013 | Tambor-class | 1 | 1 | Gato requires Gar OR Tambor |
| 211 | 8018 | 8017 | Gato-class | 1 | NULL | Balao requires Gato |
| 212 | 8019 | 8018 | Balao-class | 1 | NULL | Tench requires Balao |
| 213 | 8020 | 8018 | Balao-class | 1 | NULL | Balao GUPPY requires base Balao |
| 214 | 8021 | 8019 | Tench-class | 1 | NULL | Tench GUPPY requires base Tench |
| 215 | 8022 | 8019 | Tench-class | 1 | NULL | Nautilus requires Tench (nuclear leap) |
| 216 | 8023 | 8022 | Nautilus SSN-571 | 1 | NULL | Seawolf SSN-575 requires Nautilus (experimental) |
| 217 | 8024 | 8022 | Nautilus SSN-571 | 1 | NULL | Skate requires Nautilus (production) |
| 218 | 8025 | 8024 | Skate-class | 1 | NULL | George Washington requires Skate (ballistic) |
| 219 | 8026 | 8025 | George Washington-class | 1 | NULL | Ethan Allen requires George Washington |
| 220 | 8027 | 8024 | Skate-class | 1 | NULL | Skipjack requires Skate (teardrop) |
| 221 | 8028 | 8027 | Skipjack-class | 1 | NULL | Thresher/Permit requires Skipjack |
| 222 | 8029 | 8028 | Thresher/Permit-class | 1 | NULL | Sturgeon requires Thresher/Permit |
| 223 | 8030 | 8026 | Ethan Allen-class | 1 | NULL | Lafayette requires Ethan Allen |
| 224 | 8031 | 8030 | Lafayette-class | 1 | NULL | Benjamin Franklin requires Lafayette |
| 225 | 8032 | 8029 | Sturgeon-class | 1 | NULL | Los Angeles Early requires Sturgeon |
| 226 | 8033 | 8032 | Los Angeles-class (Early) SSN-688-699 | 1 | NULL | Los Angeles 688i requires Early |
| 227 | 8034 | 8031 | Benjamin Franklin-class | 1 | NULL | Ohio SSBN requires Benjamin Franklin |
| 228 | 8035 | 8034 | Ohio-class | 1 | NULL | Ohio SSGN requires base Ohio |
| 229 | 8036 | 8033 | Los Angeles-class (Improved 688i) SSN-700-773 | 1 | NULL | Seawolf requires LA 688i |
| 230 | 8037 | 8036 | Seawolf-class | 1 | NULL | Virginia requires Seawolf |
| 231 | 8038 | 8034 | Ohio-class | 1 | NULL | Columbia requires Ohio (future SSBN) |

**Total Prerequisites**: 39 entries

---

## Unlocks Table Entries

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 293 | 8000 | 8002 | C-class | 1 | 1 | Holland unlocks C-class |
| 294 | 8001 | 8002 | C-class | 1 | 1 | A-class unlocks C-class |
| 295 | 8002 | 8003 | F-class | 1 | 1 | C-class unlocks F-class |
| 296 | 8003 | 8004 | H-class | 1 | 1 | F-class unlocks H-class |
| 297 | 8004 | 8005 | L-class | 1 | 1 | H-class unlocks L-class (first fleet) |
| 298 | 8004 | 8015 | Mackerel-class | 1 | 3 | H-class unlocks Mackerel (training) |
| 299 | 8005 | 8006 | O-class | 1 | 1 | L-class unlocks O-class |
| 300 | 8006 | 8007 | R-class | 1 | 1 | O-class unlocks R-class |
| 301 | 8007 | 8008 | S-class | 1 | 1 | R-class unlocks S-class |
| 302 | 8007 | 8009 | V-class | 1 | 3 | R-class unlocks V-class (cruiser sub) |
| 303 | 8008 | 8010 | Porpoise-class | 1 | 1 | S-class unlocks Porpoise (pre-war) |
| 304 | 8010 | 8011 | Salmon-class | 1 | 1 | Porpoise unlocks Salmon |
| 305 | 8011 | 8012 | Sargo-class | 1 | 1 | Salmon unlocks Sargo |
| 306 | 8012 | 8013 | Tambor-class | 1 | 1 | Sargo unlocks Tambor (WWII begins) |
| 307 | 8013 | 8014 | Gar-class | 1 | 1 | Tambor unlocks Gar |
| 308 | 8013 | 8017 | Gato-class | 1 | 1 | Tambor unlocks Gato (alternative) |
| 309 | 8014 | 8017 | Gato-class | 1 | 1 | Gar unlocks Gato |
| 310 | 8015 | 8016 | Barracuda-class | 1 | 1 | Mackerel unlocks Barracuda (SST) |
| 311 | 8017 | 8018 | Balao-class | 1 | 1 | Gato unlocks Balao |
| 312 | 8018 | 8019 | Tench-class | 1 | 1 | Balao unlocks Tench |
| 313 | 8018 | 8020 | Balao-class (GUPPY) | 1 | 2 | Balao unlocks GUPPY upgrade |
| 314 | 8019 | 8021 | Tench-class (GUPPY IIA) | 1 | 2 | Tench unlocks GUPPY IIA upgrade |
| 315 | 8019 | 8022 | Nautilus SSN-571 | 1 | 1 | Tench unlocks Nautilus (nuclear leap) |
| 316 | 8022 | 8023 | Seawolf SSN-575 | 1 | 3 | Nautilus unlocks Seawolf (experimental) |
| 317 | 8022 | 8024 | Skate-class | 1 | 1 | Nautilus unlocks Skate (production) |
| 318 | 8024 | 8025 | George Washington-class | 1 | 2 | Skate unlocks George Washington (ballistic) |
| 319 | 8024 | 8027 | Skipjack-class | 1 | 1 | Skate unlocks Skipjack (teardrop) |
| 320 | 8025 | 8026 | Ethan Allen-class | 1 | 1 | George Washington unlocks Ethan Allen |
| 321 | 8026 | 8030 | Lafayette-class | 1 | 1 | Ethan Allen unlocks Lafayette |
| 322 | 8027 | 8028 | Thresher/Permit-class | 1 | 1 | Skipjack unlocks Thresher/Permit |
| 323 | 8028 | 8029 | Sturgeon-class | 1 | 1 | Thresher/Permit unlocks Sturgeon |
| 324 | 8029 | 8032 | Los Angeles-class (Early) SSN-688-699 | 1 | 1 | Sturgeon unlocks LA Early |
| 325 | 8030 | 8031 | Benjamin Franklin-class | 1 | 1 | Lafayette unlocks Benjamin Franklin |
| 326 | 8031 | 8034 | Ohio-class | 1 | 1 | Benjamin Franklin unlocks Ohio |
| 327 | 8032 | 8033 | Los Angeles-class (Improved 688i) SSN-700-773 | 1 | 1 | LA Early unlocks 688i |
| 328 | 8033 | 8036 | Seawolf-class | 1 | 1 | LA 688i unlocks Seawolf |
| 329 | 8034 | 8035 | Ohio-class (SSGN) | 1 | 2 | Ohio unlocks SSGN conversion |
| 330 | 8034 | 8038 | Columbia-class | 1 | 2 | Ohio unlocks Columbia (future) |
| 331 | 8036 | 8037 | Virginia-class | 1 | 1 | Seawolf unlocks Virginia |

**Total Unlocks**: 39 entries

---

## Research Branches Table Entries

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 35 | USA | SS | Starting | FREE starting submarines, tutorial introduction | #696969 | 8000 | 8001 | NULL | NULL | Early Submarine | Early Submarine | Holland + A-class. FREE starting ships. Holland (1900) first US submarine SS-1, A-class (1903) better option. 64-107 tons. |
| 36 | USA | SS | Coastal | Small coastal patrol submarines, limited range | #8B4513 | 8002 | 8004 | NULL | NULL | Coastal | Coastal | C → F → H. Stems from Starting. 275-350 tons. Coastal patrol only. H-class: 18 ships, largest early class. Limited range. |
| 37 | USA | SS | Fleet Diesel | WWI/Interwar ocean-going diesel fleet submarines | #1E90FF | 8005 | 8012 | 36 | NULL | WWI Fleet | Pre-War Peak | L → O → R → S → Porpoise → Salmon → Sargo. Stems from Coastal. Ocean-going capability. 450-1,450 tons. S-class: 48 ships, long-serving. Pre-war pinnacle: Sargo. |
| 38 | USA | SS | WWII Main Line | Gato, Balao, Tench - WWII mass production diesel submarines | #DC143C | 8013 | 8019 | 37 | NULL | Early WWII | Peak Diesel | Tambor → Gar → Gato → Balao → Tench. Stems from Fleet Diesel. 228 total ships (77 Gato + 122 Balao + 29 Tench). Most successful submarine classes. Balao: 400ft test depth. |
| 39 | USA | SS | Modernization | GUPPY snorkel upgrades, Cold War diesel modernizations | #CD853F | 8020 | 8021 | 38 | NULL | GUPPY Upgrade | Full GUPPY | Balao GUPPY, Tench GUPPY IIA. Stems from WWII Main Line. 1947-1952 snorkel + streamlining upgrades. GUPPY = Greater Underwater Propulsion Power Program. Extends service life. |
| 40 | USA | SSN | Nuclear Attack | Nuclear-powered attack submarines, unlimited range | #FF1493 | 8022 | 8037 | 38 | NULL | Nuclear Revolution | Current Production | Nautilus → Skate → Skipjack → Thresher/Permit → Sturgeon → LA Early → LA 688i → Seawolf → Virginia. Stems from WWII. Revolutionary unlimited range. Teardrop hull (Skipjack). 62 LA-class total. Current production: Virginia. |
| 41 | USA | SSBN | Ballistic Missile | Strategic ballistic missile submarines, nuclear deterrent | #9370DB | 8025 | 8038 | 40 | NULL | First SSBN | Future SSBN | George Washington → Ethan Allen → Lafayette → Benjamin Franklin → Ohio → Columbia. Stems from Nuclear Attack. Strategic nuclear deterrent. 16-24 ICBMs. 31 Lafayette-class largest. Columbia: future 2028. |
| 42 | USA | SS/SSN/SSGN/SST | Alternative | Experimental designs, training subs, cruise missile conversions | #FF8C00 | 8009 | 8035 | 37, 36, 40, 41 | NULL | Cruiser Sub | Cruise Missile | V-class cruiser sub, Mackerel/Barracuda training, Seawolf SSN-575 experimental, Ohio SSGN. Multiple stems. V-class: 6" deck gun, experimental. Seawolf: failed sodium reactor. Ohio SSGN: 154 Tomahawk. |

**Total Research Branches**: 8 entries

---

## Summary Statistics

- **Total Nodes**: 39 submarine nodes (8000-8038)
- **Total Prerequisites**: 39 entries
- **Total Unlocks**: 39 entries
- **Total Research Branches**: 8 branches
- **Total Database Entries**: 86 entries for USA Submarines research tree logic

---

## Unlock Chain Flowchart

```
USA SUBMARINE RESEARCH TREE - NAVYFIELD STYLE
════════════════════════════════════════════════════════════════

TIER 1: STARTING (FREE)
────────────────────────────────────────────────────────────────
        [8000] HOLLAND         [8001] A-CLASS
        First US sub, SS-1      Better starting
        64 tons, FREE           107 tons, FREE
                    │                     │
                    └──────────┬──────────┘
                               │
TIER 2: COASTAL
────────────────────────────────────────────────────────────────
                    [8002] C-CLASS
                    275 tons, coastal patrol
                               │
                    [8003] F-CLASS
                    330 tons, improved
                               │
                    [8004] H-CLASS           [8015] MACKEREL
                    350 tons, 18 ships       Training (1953)
                               │                     │
TIER 3: FLEET DIESEL (WWI/INTERWAR)                 │
────────────────────────────────────────────────────────────────
                    [8005] L-CLASS                  │
                    First fleet boats               │
                               │                     │
                    [8006] O-CLASS                  │
                    WWI fleet boat                  │
                               │                     │
                    [8007] R-CLASS          [8009] V-CLASS
                    Diesel-electric         Cruiser sub
                               │            (Experimental)
                    [8008] S-CLASS
                    48 ships, long-serving
                               │
TIER 4: PRE-WAR
────────────────────────────────────────────────────────────────
                    [8010] PORPOISE                 │
                    P-class, modern                 │
                               │                     │
                    [8011] SALMON           [8016] BARRACUDA
                    Improved                Training SST
                               │
                    [8012] SARGO
                    Pre-war peak
                               │
TIER 5: EARLY WWII
────────────────────────────────────────────────────────────────
                    [8013] TAMBOR
                    Early WWII
                               │
                    [8014] GAR
                    Improved Tambor
                               │
TIER 6: WWII MAIN LINE
────────────────────────────────────────────────────────────────
                    [8017] GATO
                    77 ships, workhorse
                               │
                    [8018] BALAO         [8020] BALAO GUPPY
                    122 ships, deep       Snorkel upgrade
                               │          (Modernization)
                    [8019] TENCH
                    29 ships, peak diesel
                            │       │
                    [8021]  │       │
                    TENCH   │       │
                    GUPPY   │       │
                            │       │
TIER 7: NUCLEAR REVOLUTION
────────────────────────────────────────────────────────────────
                    [8022] NAUTILUS SSN-571
                    First nuclear, unlimited range
                            │               │
                    [8023] SEAWOLF  [8024] SKATE
                    Experimental    Production nuclear
                    sodium reactor  4 ships
                                    │               │
                    [8025] GEORGE WASHINGTON [8027] SKIPJACK
                    First SSBN, 16 Polaris   Teardrop hull
                                    │               │
                    [8026] ETHAN ALLEN      [8028] THRESHER/PERMIT
                    Improved SSBN           Deep-diving HY-80
                                    │               │
TIER 8: MASS PRODUCTION
────────────────────────────────────────────────────────────────
                    [8030] LAFAYETTE        [8029] STURGEON
                    31 ships, mass SSBN     37 ships, long-serving
                                    │               │
                    [8031] BENJAMIN FRANKLIN
                    Quieter Lafayette       │
                                    │               │
TIER 9: MODERN ERA
────────────────────────────────────────────────────────────────
                    [8034] OHIO             [8032] LOS ANGELES (EARLY)
                    18 ships, 24 Trident    Fast attack, 33+ kts
                            │       │               │
                    [8035]  │   [8038]      [8033] LOS ANGELES (688i)
                    OHIO    │   COLUMBIA    VLS + under-ice
                    SSGN    │   Future
                    154     │   (2028)              │
                    Tomahawk│                       │
                            │               [8036] SEAWOLF
                            │               Ultimate but $2.8B
                                                    │
TIER 10: CURRENT/FUTURE
────────────────────────────────────────────────────────────────
                                            [8037] VIRGINIA
                                            Current production
```

---

**Status**: ✅ USA Submarines Research Tree Logic COMPLETE
