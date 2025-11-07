# Britain Destroyers Research Tree Logic

**Date**: January 2025
**Ship Type**: Destroyers (DD, DDG, FFG)
**Total Nodes**: 42 (2700-2741)

---

## Research Branches Overview

| Branch_ID | Branch_Name | Branch_Description | Start_Node | End_Node | Nodes |
|-----------|-------------|-------------------|------------|----------|-------|
| 31 | Starting | FREE starting destroyers, tutorial introduction | 2700 | 2701 | 2 |
| 32 | Pre-WWI | Early torpedo boat destroyers, alphabetical naming begins | 2702 | 2705 | 4 |
| 33 | WWI Main Line | WWI fleet destroyers, mass production | 2706 | 2710 | 5 |
| 34 | Interwar Standard | Interwar destroyers, alphabetical naming system | 2711 | 2717 | 7 |
| 35 | WWII Emergency | WWII emergency flotillas, war production | 2718 | 2722 | 5 |
| 36 | Post-War | Post-war destroyers and guided missile destroyers | 2723 | 2729 | 7 |
| 37 | Modern | Modern air defense destroyers, Type 45 | 2730 | 2735 | 6 |
| 38 | Alternative | Escort destroyers and frigates, ASW focus | 2736 | 2738 | 3 |
| 39 | Modernization | Cold War modernizations and FRAM upgrades | 2739 | 2741 | 3 |

---

## Prerequisites Table Entries

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 400 | 2702 | 2701 | River-class | 1 | NULL | Tribal requires River (pre-WWI path) |
| 401 | 2703 | 2702 | Tribal-class (F) | 1 | NULL | Acorn requires Tribal |
| 402 | 2704 | 2703 | Acorn-class (H) | 1 | NULL | Beagle requires Acorn |
| 403 | 2705 | 2704 | Beagle-class (G) | 1 | NULL | Acasta requires Beagle |
| 404 | 2706 | 2705 | Acasta-class (K) | 1 | NULL | Admiralty M requires Acasta |
| 405 | 2707 | 2706 | Admiralty M-class | 1 | NULL | R-class requires M-class |
| 406 | 2708 | 2707 | R-class | 1 | NULL | V-class requires R-class |
| 407 | 2709 | 2708 | V-class | 1 | NULL | W-class requires V-class |
| 408 | 2710 | 2709 | W-class | 1 | NULL | Modified W requires W-class |
| 409 | 2711 | 2710 | Modified W-class | 1 | NULL | A-class requires Modified W |
| 410 | 2712 | 2711 | A-class | 1 | NULL | B-class requires A-class |
| 411 | 2713 | 2712 | B-class | 1 | NULL | Tribal (1936) requires B-class |
| 412 | 2714 | 2713 | Tribal-class (1936) | 1 | NULL | J-class requires Tribal (1936) |
| 413 | 2715 | 2714 | J-class | 1 | NULL | K-class requires J-class |
| 414 | 2716 | 2715 | K-class | 1 | NULL | N-class requires K-class |
| 415 | 2717 | 2716 | N-class | 1 | NULL | O/P-class requires N-class |
| 416 | 2718 | 2717 | O/P-class | 1 | NULL | Q/R-class requires O/P |
| 417 | 2719 | 2718 | Q/R-class | 1 | NULL | S/T-class requires Q/R |
| 418 | 2720 | 2719 | S/T-class | 1 | NULL | U/V-class requires S/T |
| 419 | 2721 | 2720 | U/V-class | 1 | NULL | W/Z-class requires U/V |
| 420 | 2722 | 2721 | W/Z-class | 1 | NULL | Battle-class requires W/Z |
| 421 | 2723 | 2722 | Battle-class | 1 | NULL | Daring requires Battle |
| 422 | 2724 | 2723 | Daring-class | 1 | NULL | County DDG requires Daring |
| 423 | 2725 | 2724 | County-class (DDG) | 1 | NULL | Type 42 Batch 1 requires County DDG |
| 424 | 2726 | 2725 | Type 42 Batch 1 | 1 | NULL | Type 42 Batch 2 requires Batch 1 |
| 425 | 2727 | 2726 | Type 42 Batch 2 | 1 | NULL | Type 42 Batch 3 requires Batch 2 |
| 426 | 2728 | 2727 | Type 42 Batch 3 | 1 | NULL | Type 42 Batch 3.2 requires Batch 3 |
| 427 | 2729 | 2728 | Type 42 Batch 3.2 | 1 | NULL | Type 45 Batch 1 requires Type 42 Batch 3.2 |
| 428 | 2730 | 2729 | Type 45 Batch 1 | 1 | NULL | Type 45 Batch 2 requires Batch 1 |
| 429 | 2731 | 2730 | Type 45 Batch 2 | 1 | NULL | Type 45 Batch 3 requires Batch 2 |
| 430 | 2732 | 2731 | Type 45 Batch 3 | 1 | NULL | Type 45A requires Batch 3 |
| 431 | 2733 | 2732 | Type 45A | 1 | NULL | Type 45 Modernized requires Type 45A |
| 432 | 2734 | 2733 | Type 45 Modernized | 1 | NULL | Type 83 requires Type 45 Modernized |
| 433 | 2736 | 2713 | Tribal-class (1936) | 1 | NULL | Hunt requires Tribal (alternative) |
| 434 | 2737 | 2736 | Hunt-class | 1 | NULL | Black Swan requires Hunt |
| 435 | 2738 | 2737 | Black Swan-class | 1 | NULL | River frigate requires Black Swan |
| 436 | 2739 | 2722 | Battle-class | 1 | NULL | Battle Modernized requires base Battle |
| 437 | 2740 | 2723 | Daring-class | 1 | NULL | Daring Modernized requires base Daring |
| 438 | 2741 | 2724 | County-class (DDG) | 1 | NULL | County Modernized requires base County DDG |

**Total Prerequisites**: 39 entries

---

## Unlocks Table Entries

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 500 | 2701 | 2702 | Tribal-class (F) | 1 | 1 | River unlocks Tribal (pre-WWI) |
| 501 | 2702 | 2703 | Acorn-class (H) | 1 | 1 | Tribal unlocks Acorn |
| 502 | 2703 | 2704 | Beagle-class (G) | 1 | 1 | Acorn unlocks Beagle |
| 503 | 2704 | 2705 | Acasta-class (K) | 1 | 1 | Beagle unlocks Acasta |
| 504 | 2705 | 2706 | Admiralty M-class | 1 | 1 | Acasta unlocks Admiralty M |
| 505 | 2706 | 2707 | R-class | 1 | 1 | M-class unlocks R-class |
| 506 | 2707 | 2708 | V-class | 1 | 1 | R-class unlocks V-class |
| 507 | 2708 | 2709 | W-class | 1 | 1 | V-class unlocks W-class |
| 508 | 2709 | 2710 | Modified W-class | 1 | 1 | W-class unlocks Modified W |
| 509 | 2710 | 2711 | A-class | 1 | 1 | Modified W unlocks A-class |
| 510 | 2711 | 2712 | B-class | 1 | 1 | A-class unlocks B-class |
| 511 | 2712 | 2713 | Tribal-class (1936) | 1 | 1 | B-class unlocks Tribal (1936) |
| 512 | 2713 | 2714 | J-class | 1 | 1 | Tribal (1936) unlocks J-class |
| 513 | 2713 | 2736 | Hunt-class | 1 | 2 | Tribal (1936) unlocks Hunt (alternative) |
| 514 | 2714 | 2715 | K-class | 1 | 1 | J-class unlocks K-class |
| 515 | 2715 | 2716 | N-class | 1 | 1 | K-class unlocks N-class |
| 516 | 2716 | 2717 | O/P-class | 1 | 1 | N-class unlocks O/P |
| 517 | 2717 | 2718 | Q/R-class | 1 | 1 | O/P unlocks Q/R |
| 518 | 2718 | 2719 | S/T-class | 1 | 1 | Q/R unlocks S/T |
| 519 | 2719 | 2720 | U/V-class | 1 | 1 | S/T unlocks U/V |
| 520 | 2720 | 2721 | W/Z-class | 1 | 1 | U/V unlocks W/Z |
| 521 | 2721 | 2722 | Battle-class | 1 | 1 | W/Z unlocks Battle |
| 522 | 2722 | 2723 | Daring-class | 1 | 1 | Battle unlocks Daring |
| 523 | 2722 | 2739 | Battle-class (Modernized) | 1 | 2 | Battle unlocks its own modernization |
| 524 | 2723 | 2724 | County-class (DDG) | 1 | 1 | Daring unlocks County DDG |
| 525 | 2723 | 2740 | Daring-class (Modernized) | 1 | 2 | Daring unlocks its own modernization |
| 526 | 2724 | 2725 | Type 42 Batch 1 | 1 | 1 | County DDG unlocks Type 42 |
| 527 | 2724 | 2741 | County-class (DDG Modernized) | 1 | 2 | County DDG unlocks its own modernization |
| 528 | 2725 | 2726 | Type 42 Batch 2 | 1 | 1 | Type 42 Batch 1 unlocks Batch 2 |
| 529 | 2726 | 2727 | Type 42 Batch 3 | 1 | 1 | Type 42 Batch 2 unlocks Batch 3 |
| 530 | 2727 | 2728 | Type 42 Batch 3.2 | 1 | 1 | Type 42 Batch 3 unlocks Batch 3.2 |
| 531 | 2728 | 2729 | Type 45 Batch 1 | 1 | 1 | Type 42 Batch 3.2 unlocks Type 45 |
| 532 | 2729 | 2730 | Type 45 Batch 2 | 1 | 1 | Type 45 Batch 1 unlocks Batch 2 |
| 533 | 2730 | 2731 | Type 45 Batch 3 | 1 | 1 | Type 45 Batch 2 unlocks Batch 3 |
| 534 | 2731 | 2732 | Type 45A | 1 | 1 | Type 45 Batch 3 unlocks Type 45A |
| 535 | 2732 | 2733 | Type 45 Modernized | 1 | 1 | Type 45A unlocks Type 45 Modernized |
| 536 | 2733 | 2734 | Type 83 | 1 | 1 | Type 45 Modernized unlocks Type 83 |
| 537 | 2736 | 2737 | Black Swan-class | 1 | 1 | Hunt unlocks Black Swan |
| 538 | 2737 | 2738 | River-class (Frigate) | 1 | 1 | Black Swan unlocks River frigate |

**Total Unlocks**: 39 entries

---

## Research Branches Table Entries

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 31 | British | DD | Starting | FREE starting destroyers, tutorial introduction | #696969 | 2700 | 2701 | NULL | NULL | Early Torpedo Boat | Scout Destroyer | 27-knotter + River. FREE starting ships. 27-knotter (1894) primitive TBD, River (1903) better modern DD. |
| 32 | British | DD | Pre-WWI | Early torpedo boat destroyers, alphabetical naming begins | #8B4513 | 2702 | 2705 | NULL | NULL | Pre-WWI | Pre-WWI | Tribal (F) → Acorn (H) → Beagle (G) → Acasta (K). Pre-WWI TBD evolution. Letter class naming system begins. |
| 33 | British | DD | WWI Main Line | WWI fleet destroyers, mass production and convoy escort | #1E90FF | 2706 | 2710 | NULL | NULL | WWI | WWI | Admiralty M → R → V → W → Modified W. WWI workhorse destroyers. Mass production for convoy escort. |
| 34 | British | DD | Interwar Standard | Interwar destroyers, alphabetical naming system refined | #FFD700 | 2711 | 2717 | NULL | NULL | Interwar | Pre-WWII | A → B → Tribal (1936) → J → K → N → O/P. Interwar standard DDs. Alphabetical naming system. Tribal (1936) with 8×4.7" guns. |
| 35 | British | DD | WWII Emergency | WWII emergency flotillas, war production and standardization | #FF6347 | 2718 | 2722 | NULL | NULL | WWII | WWII | Q/R → S/T → U/V → W/Z → Battle. WWII emergency flotillas. Emergency war production. Battle-class ultimate WWII DD. |
| 36 | British | DDG | Post-War | Post-war destroyers and guided missile destroyers | #9370DB | 2723 | 2729 | NULL | NULL | Post-War | Modern | Daring → County DDG → Type 42 (3 batches). Post-war to missile destroyers. Sea Slug → Sea Dart evolution. |
| 37 | British | DDG | Modern | Modern air defense destroyers, Type 45 and future | #BA55D3 | 2730 | 2735 | 36 | NULL | Modern | Future | Type 45 (3 batches) → Type 45A → Type 45 Modernized → Type 83. Stems from Post-War. PAAMS air defense system. Type 83 future destroyer. |
| 38 | British | DD/FFG | Alternative | Escort destroyers and frigates, ASW focus | #FF8C00 | 2736 | 2738 | 34 | NULL | WWII | Post-War | Hunt → Black Swan → River (frigate). Stems from Interwar. Escort and convoy protection. ASW specialist designs. |
| 39 | British | DD/DDG | Modernization | Cold War modernizations and FRAM-equivalent upgrades | #CD853F | 2739 | 2741 | 35, 36 | NULL | Modernized | Modernized | Battle, Daring, County modernizations. Stems from WWII/Post-War. Extended service life upgrades. Electronics and missile upgrades. |

**Total Research Branches**: 9 entries

---

## Summary Statistics

- **Total Nodes**: 42 destroyer nodes (2700-2741)
- **Total Prerequisites**: 39 entries
- **Total Unlocks**: 39 entries
- **Total Research Branches**: 9 branches
- **Total Database Entries**: 90 entries for British Destroyers research tree logic

---

## Unlock Chain Flowchart

```
BRITISH DESTROYER RESEARCH TREE - NAVYFIELD STYLE
════════════════════════════════════════════════════════════════

TIER 1: STARTING (FREE)
────────────────────────────────────────────────────────────────
    [2700] 27-KNOTTER      [2701] RIVER-CLASS
    Early TBD               Scout Destroyer
    FREE, primitive         FREE, 8 ships
                                  │
TIER 2: PRE-WWI
────────────────────────────────────────────────────────────────
                        [2702] TRIBAL (F-CLASS)
                        Early Destroyer
                        Letter naming begins
                              │
                        [2703] ACORN (H-CLASS)
                        Improved TBD
                              │
TIER 3: PRE-WWI REFINED
────────────────────────────────────────────────────────────────
                        [2704] BEAGLE (G-CLASS)
                        Pre-WWI Standard
                              │
                        [2705] ACASTA (K-CLASS)
                        Pre-WWI Peak
                              │
TIER 4: WWI MAIN LINE
────────────────────────────────────────────────────────────────
                        [2706] ADMIRALTY M-CLASS
                        WWI Standard
                              │
                        [2707] R-CLASS
                        WWI Improved
                              │
TIER 5: WWI PEAK
────────────────────────────────────────────────────────────────
                        [2708] V-CLASS
                        WWI Advanced
                              │
                        [2709] W-CLASS
                        WWI Peak
                              │
                        [2710] MODIFIED W-CLASS
                        Ultimate WWI
                              │
TIER 6: INTERWAR
────────────────────────────────────────────────────────────────
                        [2711] A-CLASS
                        First Interwar
                              │
                        [2712] B-CLASS
                        Improved Interwar
                              │
TIER 7: PRE-WWII
────────────────────────────────────────────────────────────────
                        [2713] TRIBAL (1936)
                        8×4.7" guns, 16 ships
                              │
                    ┌─────────┴─────────┐
                    │                   │
                [2714] J-CLASS      [2736] HUNT-CLASS
                Standard WWII        Escort Destroyer
                    │                   │
                [2715] K-CLASS      [2737] BLACK SWAN
                Improved             ASW Sloop
                    │                   │
                [2716] N-CLASS      [2738] RIVER (FRIGATE)
                Enhanced             ASW Frigate
                    │
                [2717] O/P-CLASS
                Final Pre-War
                    │
TIER 8: WWII EMERGENCY
────────────────────────────────────────────────────────────────
                [2718] Q/R-CLASS
                Early Emergency
                    │
                [2719] S/T-CLASS
                Emergency Standard
                    │
                [2720] U/V-CLASS
                Emergency Peak
                    │
                [2721] W/Z-CLASS
                Late Emergency
                    │
                [2722] BATTLE-CLASS
                Ultimate WWII DD
                    │
        ┌───────────┴───────────┐
        │                       │
    [2739]                  [2723] DARING-CLASS
    BATTLE (MOD)             Post-War Gun DD
    1950s upgrade               │
                    ┌───────────┴───────────┐
                    │                       │
                [2740]                  [2724] COUNTY (DDG)
                DARING (MOD)             First Missile DD
                1960s upgrade            Sea Slug SAM
                                            │
                            ┌───────────────┴───────────┐
                            │                           │
                        [2741]                      [2725] TYPE 42 BATCH 1
                        COUNTY (MOD)                 Sea Dart DDG
                        Sea Dart upgrade                │
                                                    [2726] TYPE 42 BATCH 2
                                                    Improved Type 42
                                                        │
                                                    [2727] TYPE 42 BATCH 3
                                                    Stretched Hull
                                                        │
                                                    [2728] TYPE 42 BATCH 3.2
                                                    Final Type 42
                                                        │
                                                    [2729] TYPE 45 BATCH 1
                                                    PAAMS System
                                                        │
TIER 10: MODERN / FUTURE
────────────────────────────────────────────────────────────────
                                                    [2730] TYPE 45 BATCH 2
                                                    Improved PAAMS
                                                        │
                                                    [2731] TYPE 45 BATCH 3
                                                    Enhanced Systems
                                                        │
                                                    [2732] TYPE 45A
                                                    Advanced Variant
                                                        │
                                                    [2733] TYPE 45 (MOD)
                                                    Modernized
                                                        │
                                                    [2734] TYPE 83
                                                    Future Destroyer
```

---

**Status**: ✅ British Destroyers Research Tree Logic COMPLETE
