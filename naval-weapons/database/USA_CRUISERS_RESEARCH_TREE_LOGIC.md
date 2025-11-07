# USA Cruisers Research Tree Logic

**Date**: October 10, 2025
**Ship Type**: Cruisers (CA, CL, CLAA, CG, CGN, CAG, CLG, DL)
**Total Nodes**: 45 (6000-6044)

---

## Research Branches Overview

| Branch_ID | Branch_Name | Branch_Description | Start_Node | End_Node | Nodes |
|-----------|-------------|-------------------|------------|----------|-------|
| 12 | Starting | FREE starting cruisers, tutorial introduction | 6000 | 6044 | 5 |
| 13 | Heavy Main Line | 8" gun heavy cruisers, treaty era through WWII peak + large cruiser | 6002 | 6016 | 9 |
| 14 | Light Main Line | 6" gun light cruisers, firepower and production focus | 6004 | 6017 | 6 |
| 15 | AA Specialist | Anti-aircraft cruisers with dual-purpose guns | 6006 | 6015 | 3 |
| 16 | Guided Missile | Purpose-built missile cruisers, Aegis systems | 6024 | 6039 | 9 |
| 17 | Nuclear | Nuclear-powered cruisers, unlimited range | 6023 | 6030 | 4 |
| 18 | Conversion | Gun cruiser conversions to missile platforms | 6018 | 6028 | 5 |
| 19 | Modernization | Cold War upgrades with new missile systems | 6031 | 6032 | 2 |
| 20 | Nuclear Modernization | Nuclear cruiser modernizations | 6036 | 6036 | 1 |
| 21 | Paper Ship | Cancelled and conceptual designs | 6037 | 6040 | 2 |
| 22 | Alternative | Unique hybrid destroyer-cruiser designs | 6021 | 6021 | 1 |

---

## Prerequisites Table Entries

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 100 | 6002 | 6001 | Omaha-class | 1 | 1 | Pensacola requires Omaha OR St. Louis (1904) |
| 100b | 6002 | 6042 | St. Louis-class (1904) | 1 | 1 | Pensacola requires Omaha OR St. Louis (1904) |
| 101 | 6003 | 6001 | Omaha-class | 1 | 1 | Northampton requires Omaha OR St. Louis (1904) |
| 101b | 6003 | 6042 | St. Louis-class (1904) | 1 | 1 | Northampton requires Omaha OR St. Louis (1904) |
| 102 | 6004 | 6001 | Omaha-class | 1 | 1 | Brooklyn requires Omaha OR St. Louis (1904) |
| 102b | 6004 | 6042 | St. Louis-class (1904) | 1 | 1 | Brooklyn requires Omaha OR St. Louis (1904) |
| 103 | 6005 | 6002 | Pensacola-class | 1 | 1 | Portland requires Pensacola OR Northampton |
| 104 | 6005 | 6003 | Northampton-class | 1 | 1 | Portland requires Pensacola OR Northampton |
| 105 | 6006 | 6004 | Brooklyn-class | 1 | NULL | Atlanta requires Brooklyn (AA needs CL experience) |
| 106 | 6007 | 6004 | Brooklyn-class | 1 | NULL | St. Louis requires Brooklyn |
| 107 | 6008 | 6005 | Portland-class | 1 | NULL | New Orleans requires Portland |
| 108 | 6009 | 6008 | New Orleans-class | 1 | NULL | Wichita requires New Orleans |
| 109 | 6010 | 6007 | St. Louis-class | 1 | 1 | Cleveland requires St. Louis OR Brooklyn |
| 110 | 6010 | 6004 | Brooklyn-class | 1 | 1 | Cleveland requires St. Louis OR Brooklyn |
| 111 | 6011 | 6006 | Atlanta-class | 1 | NULL | Oakland requires Atlanta |
| 112 | 6012 | 6009 | Wichita-class | 1 | NULL | Baltimore requires Wichita |
| 113 | 6013 | 6012 | Baltimore-class | 1 | NULL | Oregon City requires Baltimore |
| 114 | 6014 | 6010 | Cleveland-class | 1 | NULL | Fargo requires Cleveland |
| 115 | 6015 | 6011 | Oakland-class | 1 | NULL | Juneau requires Oakland |
| 116 | 6016 | 6012 | Baltimore-class | 1 | 1 | Des Moines requires Baltimore, Oregon City, OR Alaska |
| 116b | 6016 | 6041 | Alaska-class | 1 | 1 | Des Moines requires Baltimore, Oregon City, OR Alaska |
| 117 | 6016 | 6013 | Oregon City-class | 1 | 1 | Des Moines requires Baltimore, Oregon City, OR Alaska |
| 118 | 6017 | 6010 | Cleveland-class | 1 | 1 | Worcester requires Cleveland OR Fargo |
| 119 | 6017 | 6014 | Fargo-class | 1 | 1 | Worcester requires Cleveland OR Fargo |
| 120 | 6018 | 6012 | Baltimore-class | 1 | NULL | Boston conversion requires Baltimore |
| 121 | 6019 | 6010 | Cleveland-class | 1 | NULL | Galveston conversion requires Cleveland |
| 122 | 6020 | 6010 | Cleveland-class | 1 | NULL | Providence conversion requires Cleveland |
| 123 | 6021 | 6010 | Cleveland-class | 1 | NULL | Norfolk requires Cleveland (destroyer leader) |
| 124 | 6022 | 6012 | Baltimore-class | 1 | NULL | Albany conversion requires Baltimore |
| 125 | 6023 | 6016 | Des Moines-class | 1 | NULL | Long Beach requires Des Moines (ultimate gun CA) |
| 126 | 6024 | 6016 | Des Moines-class | 1 | 1 | Leahy requires Des Moines OR Worcester |
| 127 | 6024 | 6017 | Worcester-class | 1 | 1 | Leahy requires Des Moines OR Worcester |
| 128 | 6025 | 6023 | Long Beach CGN-9 | 1 | NULL | Bainbridge requires Long Beach AND Leahy |
| 129 | 6025 | 6024 | Leahy-class | 1 | NULL | Bainbridge requires Long Beach AND Leahy |
| 130 | 6026 | 6024 | Leahy-class | 1 | NULL | Belknap requires Leahy |
| 131 | 6027 | 6025 | Bainbridge CGN-25 | 1 | NULL | Truxtun requires Bainbridge AND Belknap |
| 132 | 6027 | 6026 | Belknap-class | 1 | NULL | Truxtun requires Bainbridge AND Belknap |
| 133 | 6028 | 6012 | Baltimore-class | 1 | NULL | Chicago conversion requires Baltimore |
| 134 | 6029 | 6023 | Long Beach CGN-9 | 1 | 1 | California requires Long Beach OR Truxtun |
| 135 | 6029 | 6027 | Truxtun CGN-35 | 1 | 1 | California requires Long Beach OR Truxtun |
| 136 | 6030 | 6029 | California-class | 1 | NULL | Virginia requires California |
| 137 | 6031 | 6024 | Leahy-class | 1 | NULL | Leahy NTU requires base Leahy |
| 138 | 6032 | 6026 | Belknap-class | 1 | NULL | Belknap NTU requires base Belknap |
| 139 | 6033 | 6026 | Belknap-class | 1 | NULL | Ticonderoga Early requires Belknap |
| 140 | 6034 | 6033 | Ticonderoga-class (Early) CG-47/48 | 1 | NULL | Ticonderoga Baseline 1 requires Early |
| 141 | 6035 | 6034 | Ticonderoga-class (Baseline 1) CG-49-51 | 1 | NULL | Ticonderoga Baseline 2 requires Baseline 1 |
| 142 | 6036 | 6030 | Virginia-class | 1 | NULL | Virginia Modernized requires base Virginia |
| 143 | 6037 | 6030 | Virginia-class | 1 | NULL | Strike Cruiser requires Virginia (paper ship) |
| 144 | 6038 | 6035 | Ticonderoga-class (Baseline 2) CG-52-58 | 1 | NULL | Ticonderoga Baseline 3 requires Baseline 2 |
| 145 | 6039 | 6038 | Ticonderoga-class (Baseline 3) CG-59-64 | 1 | NULL | Ticonderoga Baseline 4 requires Baseline 3 |
| 146 | 6040 | 6039 | Ticonderoga-class (Baseline 4) CG-65-73 | 1 | NULL | CG(X) requires Baseline 4 (cancelled future) |
| 147 | 6041 | 6012 | Baltimore-class | 1 | NULL | Alaska requires Baltimore (large cruiser from WWII heavy) |
| 148 | 6042 | 6044 | Tennessee-class | 1 | 1 | St. Louis (1904) requires Tennessee OR Denver |
| 149 | 6042 | 6043 | Denver-class | 1 | 1 | St. Louis (1904) requires Tennessee OR Denver |
| 150 | 6043 | 6000 | Chester-class | 1 | NULL | Denver requires Chester (early protected path) |

**Total Prerequisites**: 55 entries (47 original + 8 new)

---

## Unlocks Table Entries

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 200 | 6001 | 6002 | Pensacola-class | 1 | 1 | Omaha unlocks Pensacola (heavy cruiser path) |
| 201 | 6001 | 6003 | Northampton-class | 1 | 1 | Omaha unlocks Northampton (alternative heavy) |
| 202 | 6001 | 6004 | Brooklyn-class | 1 | 1 | Omaha unlocks Brooklyn (light cruiser path) |
| 203 | 6002 | 6005 | Portland-class | 1 | 1 | Pensacola unlocks Portland |
| 204 | 6003 | 6005 | Portland-class | 1 | 1 | Northampton unlocks Portland |
| 205 | 6004 | 6006 | Atlanta-class | 1 | 2 | Brooklyn unlocks Atlanta (AA specialist) |
| 206 | 6004 | 6007 | St. Louis-class | 1 | 1 | Brooklyn unlocks St. Louis |
| 207 | 6004 | 6010 | Cleveland-class | 1 | 1 | Brooklyn unlocks Cleveland (alternative path) |
| 208 | 6005 | 6008 | New Orleans-class | 1 | 1 | Portland unlocks New Orleans |
| 209 | 6006 | 6011 | Oakland-class | 1 | 1 | Atlanta unlocks Oakland |
| 210 | 6007 | 6010 | Cleveland-class | 1 | 1 | St. Louis unlocks Cleveland |
| 211 | 6008 | 6009 | Wichita-class | 1 | 1 | New Orleans unlocks Wichita |
| 212 | 6009 | 6012 | Baltimore-class | 1 | 1 | Wichita unlocks Baltimore |
| 213 | 6010 | 6014 | Fargo-class | 1 | 1 | Cleveland unlocks Fargo |
| 214 | 6010 | 6017 | Worcester-class | 1 | 1 | Cleveland unlocks Worcester (alternative path) |
| 215 | 6010 | 6019 | Galveston-class | 1 | 2 | Cleveland unlocks Galveston conversion |
| 216 | 6010 | 6020 | Providence-class | 1 | 2 | Cleveland unlocks Providence conversion |
| 217 | 6010 | 6021 | Norfolk-class | 1 | 3 | Cleveland unlocks Norfolk (destroyer leader) |
| 218 | 6011 | 6015 | Juneau-class | 1 | 1 | Oakland unlocks Juneau |
| 219 | 6012 | 6013 | Oregon City-class | 1 | 1 | Baltimore unlocks Oregon City |
| 220 | 6012 | 6016 | Des Moines-class | 1 | 1 | Baltimore unlocks Des Moines (alternative path) |
| 221 | 6012 | 6018 | Boston-class | 1 | 2 | Baltimore unlocks Boston conversion |
| 222 | 6012 | 6022 | Albany-class | 1 | 2 | Baltimore unlocks Albany conversion |
| 223 | 6012 | 6028 | Chicago CAG-136 | 1 | 2 | Baltimore unlocks Chicago conversion |
| 224 | 6013 | 6016 | Des Moines-class | 1 | 1 | Oregon City unlocks Des Moines |
| 225 | 6014 | 6017 | Worcester-class | 1 | 1 | Fargo unlocks Worcester |
| 226 | 6016 | 6023 | Long Beach CGN-9 | 1 | 2 | Des Moines unlocks Long Beach (nuclear path) |
| 227 | 6016 | 6024 | Leahy-class | 1 | 1 | Des Moines unlocks Leahy (missile path) |
| 228 | 6017 | 6024 | Leahy-class | 1 | 1 | Worcester unlocks Leahy (alternative) |
| 229 | 6023 | 6025 | Bainbridge CGN-25 | 1 | 1 | Long Beach unlocks Bainbridge |
| 230 | 6023 | 6029 | California-class | 1 | 1 | Long Beach unlocks California (alternative) |
| 231 | 6024 | 6025 | Bainbridge CGN-25 | 1 | 2 | Leahy unlocks Bainbridge (nuclear variant) |
| 232 | 6024 | 6026 | Belknap-class | 1 | 1 | Leahy unlocks Belknap |
| 233 | 6024 | 6031 | Leahy-class (NTU) | 1 | 2 | Leahy unlocks its own NTU upgrade |
| 234 | 6025 | 6027 | Truxtun CGN-35 | 1 | 1 | Bainbridge unlocks Truxtun |
| 235 | 6026 | 6027 | Truxtun CGN-35 | 1 | 2 | Belknap unlocks Truxtun (nuclear variant) |
| 236 | 6026 | 6032 | Belknap-class (NTU) | 1 | 2 | Belknap unlocks its own NTU upgrade |
| 237 | 6026 | 6033 | Ticonderoga-class (Early) CG-47/48 | 1 | 1 | Belknap unlocks Ticonderoga (Aegis era) |
| 238 | 6027 | 6029 | California-class | 1 | 1 | Truxtun unlocks California |
| 239 | 6029 | 6030 | Virginia-class | 1 | 1 | California unlocks Virginia |
| 240 | 6030 | 6036 | Virginia-class CGN (Modernized) | 1 | 2 | Virginia unlocks its own modernization |
| 241 | 6030 | 6037 | Strike Cruiser CGN | 1 | 3 | Virginia unlocks Strike Cruiser (paper ship) |
| 242 | 6033 | 6034 | Ticonderoga-class (Baseline 1) CG-49-51 | 1 | 1 | Ticonderoga Early unlocks Baseline 1 |
| 243 | 6034 | 6035 | Ticonderoga-class (Baseline 2) CG-52-58 | 1 | 1 | Baseline 1 unlocks Baseline 2 |
| 244 | 6035 | 6038 | Ticonderoga-class (Baseline 3) CG-59-64 | 1 | 1 | Baseline 2 unlocks Baseline 3 |
| 245 | 6038 | 6039 | Ticonderoga-class (Baseline 4) CG-65-73 | 1 | 1 | Baseline 3 unlocks Baseline 4 |
| 246 | 6039 | 6040 | CG(X) Future Cruiser | 1 | 2 | Baseline 4 unlocks CG(X) (cancelled future) |
| 247 | 6000 | 6043 | Denver-class | 1 | 2 | Chester unlocks Denver (peace cruiser alternative) |
| 248 | 6043 | 6042 | St. Louis-class (1904) | 1 | 1 | Denver unlocks St. Louis (1904) |
| 249 | 6044 | 6042 | St. Louis-class (1904) | 1 | 1 | Tennessee unlocks St. Louis (1904) |
| 250 | 6042 | 6002 | Pensacola-class | 1 | 1 | St. Louis (1904) unlocks Pensacola (alternative path) |
| 251 | 6042 | 6003 | Northampton-class | 1 | 1 | St. Louis (1904) unlocks Northampton (alternative path) |
| 252 | 6042 | 6004 | Brooklyn-class | 1 | 1 | St. Louis (1904) unlocks Brooklyn (alternative path) |
| 253 | 6012 | 6041 | Alaska-class | 1 | 2 | Baltimore unlocks Alaska (large cruiser branch) |
| 254 | 6041 | 6016 | Des Moines-class | 1 | 1 | Alaska unlocks Des Moines (merges to ultimate gun) |

**Total Unlocks**: 55 entries (47 original + 8 new)

---

## Research Branches Table Entries

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 12 | USA | CL/ACR | Starting | FREE starting cruisers, tutorial introduction | #696969 | 6000 | 6044 | NULL | NULL | Protected Cruiser | Armored Cruiser | Chester (6000) + Omaha (6001) FREE. Tennessee ACR (6044), Denver (6043), St. Louis 1904 (6042) early alternatives. Protected line: Chester→Denver→St.Louis 1904. Armored line: Tennessee→St.Louis 1904. Both paths bridge to treaty era. |
| 13 | USA | CA/CAG/CB | Heavy Main Line | 8" gun treaty heavy cruisers through WWII peak gun cruisers + large cruiser alternative | #FFD700 | 6002 | 6016 | NULL | NULL | Treaty Heavy | Ultimate Gun | Pensacola → Northampton → Portland → New Orleans → Wichita → Baltimore → (Oregon City OR Alaska CB) → Des Moines. Treaty 8" guns evolving to ultimate auto-loading 8" cruisers. Alaska (6041) provides alternative 12" gun large cruiser path from Baltimore. |
| 14 | USA | CL/CLG | Light Main Line | 6" gun light cruisers, firepower and mass production focus | #1E90FF | 6004 | 6017 | NULL | NULL | Treaty Light | Ultimate Light | Brooklyn → St. Louis → Cleveland → Fargo → Worcester. 15×6" guns (Brooklyn) to rapid-fire auto 6" (Worcester). Mass production emphasis. |
| 15 | USA | CLAA | AA Specialist | Anti-aircraft cruisers with dual-purpose 5" guns | #FF6347 | 6006 | 6015 | 14 | NULL | AA Cruiser | AA Cruiser | Atlanta → Oakland → Juneau. Stems from Light Main Line. 16×5" DP guns for fleet air defense. 18 ships total across 3 classes. |
| 16 | USA | CG | Guided Missile | Purpose-built guided missile cruisers, Aegis systems | #9370DB | 6024 | 6039 | 13, 14 | NULL | First Purpose CG | Ultimate Aegis | Leahy → Belknap → Ticonderoga (4 variants). Stems from both Heavy + Light main lines. First purpose CG to ultimate Aegis. 27 Ticonderogas built. |
| 17 | USA | CGN | Nuclear | Nuclear-powered cruisers, unlimited range | #FF1493 | 6023 | 6030 | 13 | NULL | First Nuclear | Improved Nuclear | Long Beach → Bainbridge → Truxtun → California → Virginia. Stems from Heavy Main Line. 9 nuclear cruisers total. Only Long Beach with C1W reactors, rest D2G. |
| 18 | USA | CAG/CLG | Conversion | Gun cruiser conversions to missile platforms (1950s-1960s) | #8B4513 | 6018 | 6028 | 13, 14 | NULL | First Missile | Late Conversion | Boston, Galveston, Providence, Albany, Chicago. Baltimore + Cleveland conversions. Terrier/Talos SAMs replace guns. Cheaper than building new. |
| 19 | USA | CG | Modernization | Cold War NTU (New Threat Upgrade) with Standard SM-2 missiles | #CD853F | 6031 | 6032 | 16 | NULL | Upgraded Missile | Upgraded Missile | Leahy NTU, Belknap NTU. Stems from Guided Missile branch. 1980s upgrades with Standard SM-2. Extends service life. |
| 20 | USA | CGN | Nuclear Modernization | Nuclear cruiser late-1980s modernizations with Aegis-ready systems | #BA55D3 | 6036 | 6036 | 17 | NULL | Modernized Nuclear | Modernized Nuclear | Virginia (Modernized). 1988 full modernization. Aegis-ready systems + Tomahawk. Extends 1976 design to late Cold War. |
| 21 | USA | CGN/CG | Paper Ship | Cancelled and conceptual cruiser designs | #DC143C | 6037 | 6040 | 16, 17 | NULL | Strike Cruiser | Future Cruiser | Strike Cruiser CGN (1975 cancelled), CG(X) (2020s cancelled). -10% reliability. Strike Cruiser: Aegis + Tomahawk + nuclear. CG(X): Next-gen systems. |
| 22 | USA | DL | Alternative | Destroyer leader / frigate hybrids, niche roles | #FF8C00 | 6021 | 6021 | 14 | NULL | Frigate/Light | Frigate/Light | Norfolk-class. Large DD/light cruiser hybrid. 8×3" guns. ASW + AA focus. 1 ship built. Stems from Light Main Line. |

**Total Research Branches**: 11 entries

---

## Summary Statistics

- **Total Nodes**: 45 cruiser nodes (6000-6044)
- **Total Prerequisites**: 55 entries
- **Total Unlocks**: 55 entries
- **Total Research Branches**: 11 branches
- **Total Database Entries**: 121 entries for USA Cruisers research tree logic

---

## Unlock Chain Flowchart

```
USA CRUISER RESEARCH TREE - NAVYFIELD STYLE (COMPLETE 45 NODES)
════════════════════════════════════════════════════════════════

TIER 1: STARTING ERA (FREE + EARLY PROTECTED/ARMORED)
────────────────────────────────────────────────────────────────
    [6044] TENNESSEE (ACR)    [6000] CHESTER (CL)    [6001] OMAHA (CL)
    Armored Cruiser           Protected Cruiser      Scout Cruiser
    4×10"/40 guns, 1906       2×5" guns, 1908        12×6" guns, 1923
    500K, Pre-dreadnought     FREE, 3 ships          FREE, 10 ships
              │                       │                     │
              │           ┌───────────┼───────────┐         │
              │           │           │           │         │
         [6042]      [6043]                                 │
         ST. LOUIS   DENVER                                 │
         Protected   "Peace                                 │
         14×6" 1904  Cruiser"                              │
         1.5M, semi  10×5" 1903                            │
         armored     500K                                   │
              │           │                                 │
              └─────┬─────┘                                 │
                    │                                       │
                    └───────────────────┬───────────────────┘
                                        │
                        ┌───────────────┼───────────────────┐
                        │               │                   │
TIER 2: TREATY ERA
────────────────────────────────────────────────────────────────
            [6002] PENSACOLA     [6003] NORTHAMPTON    [6004] BROOKLYN
            Heavy CA              Alternative CA         Light CL
            10×8" guns            9×8" guns             15×6" guns
            Treaty heavy          Fast heavy            Max firepower
                    │                     │                  │
                    └──────────┬──────────┘                  │
                               │                             │
TIER 3: REFINED TREATY
────────────────────────────────────────────────────────────────
                    [6005] PORTLAND              [6006] ATLANTA (CLAA)
                    Balanced CA                  AA Specialist
                    9×8" guns                    16×5" DP guns
                    Improved armor               Fleet AA defense
                        │                             │
                        │                   [6007] ST. LOUIS (CL)
                        │                   Brooklyn subclass
                        │                   15×6" + better AA
                        │                             │
TIER 4: PRE-WWII / WWII EARLY
────────────────────────────────────────────────────────────────
            [6008] NEW ORLEANS               [6010] CLEVELAND (CL)
            Peak Treaty CA                   Mass Production
            9×8" guns                        12×6", 27 ships
            All-or-nothing                   Largest CL class
                    │                             │         │
            [6009] WICHITA                        │    [6011] OAKLAND
            Hybrid CA                             │    Improved AA
            Brooklyn + 8"                         │    12×5" DP
                    │                             │         │
TIER 5: WWII PEAK + LARGE CRUISER
────────────────────────────────────────────────────────────────
            [6012] BALTIMORE               [6014] FARGO (CL)
            Ultimate WWII CA                Improved CL
            9×8", best armor                Single funnel
                    │                             │
        ┌───────────┼───────────┐                 │
        │           │           │                 │
    [6013]     [6041]                        [6015] JUNEAU (CLAA)
    OREGON     ALASKA (CB)                   Late AA cruiser
    CITY       LARGE CRUISER                 Korean War
    Single     9×12"/50 guns                      │
    funnel     29,779 tons                        │
    design     2 ships built                      │
        │           │                             │
        └─────┬─────┘                             │
              │                                   │
TIER 6: ULTIMATE GUN / CONVERSIONS
────────────────────────────────────────────────────────────────
            [6016] DES MOINES              [6017] WORCESTER (CL)
            Auto-loading 8"                 Rapid-fire 6"
            8-10 rpm per gun                12 rpm auto
            Ultimate gun CA                 Ultimate light
                    │                             │
        ┌───────────┼───────────┐                 │
        │           │           │                 │
    [6018]      [6022]      [6028]          [6019] [6020]
    BOSTON      ALBANY      CHICAGO         GALVESTON PROVIDENCE
    CAG         CG          CAG             CLG       CLG
    6×8"+       0 guns      6×8"+           6×6"+     3×6"+
    Terrier     Talos+      Talos           Talos     Terrier
                Tartar      1964            1958      1959
                1962        conversion      conversion conversion
                            │
                    [6021] NORFOLK (DL)
                    Destroyer leader
                    8×3" guns
                    ASW + AA hybrid

TIER 7: MISSILE ERA / NUCLEAR
────────────────────────────────────────────────────────────────
            [6024] LEAHY (CG)              [6023] LONG BEACH (CGN)
            First Purpose CG                First Nuclear CG
            Terrier SAM                     2×C1W reactors
            9 ships built                   UNIQUE design
                    │                             │
        ┌───────────┼───────────┐        ┌────────┴────────┐
        │           │           │        │                 │
    [6031]      [6026]      [6025]   [6029]                │
    LEAHY       BELKNAP     BAINBRIDGE CALIFORNIA          │
    (NTU)       Improved    Nuclear     Nuclear            │
    SM-2        CG          Leahy       Production         │
    1980s       1×5" gun    1962        2×D2G              │
                    │           │            │              │
                [6032]      [6027]           │              │
                BELKNAP     TRUXTUN      [6030] VIRGINIA   │
                (NTU)       Nuclear      Improved Nuclear  │
                SM-2        Belknap      4 ships, 1976     │
                1985        1967         Aegis-ready       │
                    │           │            │              │
                    │           │       [6036] [6037]       │
                    │           │       VIRGINIA STRIKE     │
                    │           │       (MOD)   CRUISER     │
                    │           │       Aegis   (Paper)     │
                    │           │       ready   Cancelled   │
                    │           │       1988    1976        │
                    │           │            │              │
                    │           └─────┬──────┘              │
                    │                 │                     │
TIER 8: EARLY AEGIS
────────────────────────────────────────────────────────────────
            [6033] TICONDEROGA (Early) CG-47/48
            Mk 26 twin launchers
            SPY-1A phased array
            First Aegis ships
                        │
TIER 9: AEGIS REFINEMENT
────────────────────────────────────────────────────────────────
            [6034] TICONDEROGA (Baseline 1) CG-49-51
            Improved systems
            Still Mk 26 launchers
                        │
            [6035] TICONDEROGA (Baseline 2) CG-52-58
            SPY-1B radar upgrade
            Better processing
                        │
TIER 10: ULTIMATE AEGIS / FUTURE
────────────────────────────────────────────────────────────────
            [6038] TICONDEROGA (Baseline 3) CG-59-64
            First Mk 41 VLS
            122 cells total
                        │
            [6039] TICONDEROGA (Baseline 4) CG-65-73
            Ultimate production
            VLS 122, best systems
                        │
            [6040] CG(X) FUTURE CRUISER
            2020s cancelled
            Next-gen systems
```

---

**Status**: ✅ USA Cruisers Research Tree Logic COMPLETE
