# Britain Cruisers Research Tree Logic

**Date**: January 2025
**Ship Type**: Cruisers (CL, CA, CG, CLAA)
**Total Nodes**: 46 (2600-2645)

---

## Research Branches Overview

| Branch_ID | Branch_Name | Branch_Description | Start_Node | End_Node | Nodes |
|-----------|-------------|-------------------|------------|----------|-------|
| 23 | Starting | FREE starting cruisers, tutorial introduction | 2600 | 2601 | 2 |
| 24 | Protected/Armored Main Line | Protected and armored cruisers, pre-dreadnought era | 2602 | 2607 | 6 |
| 25 | Light Cruiser Main Line | Light cruisers from WWI through WWII, Royal Navy backbone | 2608 | 2620 | 13 |
| 26 | AA Specialist | Anti-aircraft cruisers with dual-purpose guns | 2621 | 2623 | 3 |
| 27 | Heavy Cruiser | 8" gun treaty heavy cruisers, County-class | 2624 | 2629 | 6 |
| 28 | Post-War/Guided Missile | Cold War missile cruisers and modern destroyers | 2630 | 2640 | 11 |
| 29 | Modernization | Cold War modernizations and upgrades | 2641 | 2643 | 3 |
| 30 | Paper Ship | Cancelled and conceptual designs | 2644 | 2645 | 2 |

---

## Prerequisites Table Entries

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 300 | 2602 | 2601 | Leander-class | 1 | NULL | Cressy requires Leander (protected path) |
| 301 | 2608 | 2601 | Leander-class | 1 | NULL | Town requires Leander (light path) |
| 302 | 2624 | 2601 | Leander-class | 1 | NULL | Hawkins requires Leander (heavy path) |
| 303 | 2603 | 2602 | Cressy-class | 1 | NULL | Drake requires Cressy |
| 304 | 2604 | 2603 | Drake-class | 1 | NULL | Warrior requires Drake |
| 305 | 2605 | 2604 | Warrior-class | 1 | NULL | Duke of Edinburgh requires Warrior |
| 306 | 2606 | 2605 | Duke of Edinburgh-class | 1 | NULL | Devonshire requires Duke of Edinburgh |
| 307 | 2607 | 2606 | Devonshire-class | 1 | NULL | Monmouth requires Devonshire |
| 308 | 2609 | 2608 | Town-class (1910) | 1 | NULL | Arethusa requires Town |
| 309 | 2610 | 2609 | Arethusa-class (1913) | 1 | NULL | C-class requires Arethusa |
| 310 | 2611 | 2610 | C-class | 1 | NULL | D-class requires C-class |
| 311 | 2612 | 2611 | D-class | 1 | NULL | E-class requires D-class |
| 312 | 2613 | 2612 | E-class | 1 | NULL | Emerald requires E-class |
| 313 | 2614 | 2613 | Emerald-class | 1 | NULL | Leander (1931) requires Emerald |
| 314 | 2615 | 2614 | Leander-class (1931) | 1 | NULL | Amphion requires Leander (1931) |
| 315 | 2616 | 2615 | Amphion-class | 1 | NULL | Arethusa (1934) requires Amphion |
| 316 | 2617 | 2616 | Arethusa-class (1934) | 1 | NULL | Town (1936) requires Arethusa (1934) |
| 317 | 2618 | 2617 | Town-class (1936) | 1 | NULL | Fiji requires Town (1936) |
| 318 | 2619 | 2618 | Fiji-class | 1 | NULL | Minotaur requires Fiji |
| 319 | 2621 | 2618 | Fiji-class | 1 | NULL | Dido requires Fiji (AA specialist) |
| 320 | 2622 | 2621 | Dido-class | 1 | NULL | Bellona requires Dido |
| 321 | 2623 | 2622 | Bellona-class | 1 | NULL | Scylla requires Bellona |
| 322 | 2625 | 2624 | Hawkins-class | 1 | NULL | County (Kent) requires Hawkins |
| 323 | 2626 | 2625 | County-class (Kent) | 1 | NULL | County (London) requires Kent |
| 324 | 2627 | 2626 | County-class (London) | 1 | NULL | County (Norfolk) requires London |
| 325 | 2628 | 2627 | County-class (Norfolk) | 1 | NULL | York requires Norfolk |
| 326 | 2629 | 2628 | York-class | 1 | NULL | Exeter requires York |
| 327 | 2630 | 2619 | Minotaur-class | 1 | 1 | Tiger requires Minotaur OR Exeter |
| 328 | 2630 | 2629 | Exeter-class | 1 | 1 | Tiger requires Minotaur OR Exeter |
| 329 | 2631 | 2630 | Tiger-class | 1 | NULL | Blake requires Tiger |
| 330 | 2632 | 2631 | Blake-class | 1 | NULL | County (DDG) requires Blake |
| 331 | 2633 | 2632 | County-class (DDG) | 1 | NULL | Bristol requires County DDG |
| 332 | 2634 | 2633 | Bristol-class | 1 | NULL | Sheffield requires Bristol |
| 333 | 2635 | 2634 | Sheffield-class (Type 42 Batch 1) | 1 | NULL | Type 42 Batch 2 requires Batch 1 |
| 334 | 2636 | 2635 | Sheffield-class (Type 42 Batch 2) | 1 | NULL | Type 42 Batch 3 requires Batch 2 |
| 335 | 2637 | 2636 | Sheffield-class (Type 42 Batch 3) | 1 | NULL | Type 22 requires Type 42 Batch 3 |
| 336 | 2638 | 2637 | Type 22 Broadsword-class | 1 | NULL | Type 23 Batch 1 requires Type 22 |
| 337 | 2639 | 2638 | Type 23 Duke-class (Batch 1) | 1 | NULL | Type 23 Batch 2 requires Batch 1 |
| 338 | 2640 | 2639 | Type 23 Duke-class (Batch 2) | 1 | NULL | Type 26 requires Type 23 Batch 2 |
| 339 | 2641 | 2630 | Tiger-class | 1 | NULL | Tiger Modernized requires base Tiger |
| 340 | 2642 | 2632 | County-class (DDG) | 1 | NULL | County Modernized requires base County DDG |
| 341 | 2643 | 2634 | Sheffield-class (Type 42 Batch 1) | 1 | NULL | Sheffield Modernized requires base Sheffield |
| 342 | 2644 | 2629 | Exeter-class | 1 | NULL | Design CA requires Exeter (paper ship) |
| 343 | 2645 | 2640 | Type 26 Frigate | 1 | NULL | Future Cruiser requires Type 26 (paper ship) |

**Total Prerequisites**: 44 entries

---

## Unlocks Table Entries

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 400 | 2601 | 2602 | Cressy-class | 1 | 1 | Leander unlocks Cressy (protected path) |
| 401 | 2601 | 2608 | Town-class (1910) | 1 | 1 | Leander unlocks Town (light path) |
| 402 | 2601 | 2624 | Hawkins-class | 1 | 1 | Leander unlocks Hawkins (heavy path) |
| 403 | 2602 | 2603 | Drake-class | 1 | 1 | Cressy unlocks Drake |
| 404 | 2603 | 2604 | Warrior-class | 1 | 1 | Drake unlocks Warrior |
| 405 | 2604 | 2605 | Duke of Edinburgh-class | 1 | 1 | Warrior unlocks Duke of Edinburgh |
| 406 | 2605 | 2606 | Devonshire-class | 1 | 1 | Duke of Edinburgh unlocks Devonshire |
| 407 | 2606 | 2607 | Monmouth-class | 1 | 1 | Devonshire unlocks Monmouth |
| 408 | 2608 | 2609 | Arethusa-class (1913) | 1 | 1 | Town unlocks Arethusa |
| 409 | 2609 | 2610 | C-class | 1 | 1 | Arethusa unlocks C-class |
| 410 | 2610 | 2611 | D-class | 1 | 1 | C-class unlocks D-class |
| 411 | 2611 | 2612 | E-class | 1 | 1 | D-class unlocks E-class |
| 412 | 2612 | 2613 | Emerald-class | 1 | 1 | E-class unlocks Emerald |
| 413 | 2613 | 2614 | Leander-class (1931) | 1 | 1 | Emerald unlocks Leander (1931) |
| 414 | 2614 | 2615 | Amphion-class | 1 | 1 | Leander (1931) unlocks Amphion |
| 415 | 2615 | 2616 | Arethusa-class (1934) | 1 | 1 | Amphion unlocks Arethusa (1934) |
| 416 | 2616 | 2617 | Town-class (1936) | 1 | 1 | Arethusa (1934) unlocks Town (1936) |
| 417 | 2617 | 2618 | Fiji-class | 1 | 1 | Town (1936) unlocks Fiji |
| 418 | 2618 | 2619 | Minotaur-class | 1 | 1 | Fiji unlocks Minotaur |
| 419 | 2618 | 2621 | Dido-class | 1 | 2 | Fiji unlocks Dido (AA specialist) |
| 420 | 2619 | 2630 | Tiger-class | 1 | 1 | Minotaur unlocks Tiger |
| 421 | 2621 | 2622 | Bellona-class | 1 | 1 | Dido unlocks Bellona |
| 422 | 2622 | 2623 | Scylla-class | 1 | 1 | Bellona unlocks Scylla |
| 423 | 2624 | 2625 | County-class (Kent) | 1 | 1 | Hawkins unlocks Kent |
| 424 | 2625 | 2626 | County-class (London) | 1 | 1 | Kent unlocks London |
| 425 | 2626 | 2627 | County-class (Norfolk) | 1 | 1 | London unlocks Norfolk |
| 426 | 2627 | 2628 | York-class | 1 | 1 | Norfolk unlocks York |
| 427 | 2628 | 2629 | Exeter-class | 1 | 1 | York unlocks Exeter |
| 428 | 2629 | 2630 | Tiger-class | 1 | 1 | Exeter unlocks Tiger (alternative path) |
| 429 | 2629 | 2644 | Design CA | 1 | 2 | Exeter unlocks Design CA (paper ship) |
| 430 | 2630 | 2631 | Blake-class | 1 | 1 | Tiger unlocks Blake |
| 431 | 2630 | 2641 | Tiger-class (Modernized) | 1 | 2 | Tiger unlocks its own modernization |
| 432 | 2631 | 2632 | County-class (DDG) | 1 | 1 | Blake unlocks County DDG |
| 433 | 2632 | 2633 | Bristol-class | 1 | 1 | County DDG unlocks Bristol |
| 434 | 2632 | 2642 | County-class (DDG Modernized) | 1 | 2 | County DDG unlocks its own modernization |
| 435 | 2633 | 2634 | Sheffield-class (Type 42 Batch 1) | 1 | 1 | Bristol unlocks Sheffield |
| 436 | 2634 | 2635 | Sheffield-class (Type 42 Batch 2) | 1 | 1 | Type 42 Batch 1 unlocks Batch 2 |
| 437 | 2634 | 2643 | Sheffield-class (Modernized) | 1 | 2 | Sheffield unlocks its own modernization |
| 438 | 2635 | 2636 | Sheffield-class (Type 42 Batch 3) | 1 | 1 | Type 42 Batch 2 unlocks Batch 3 |
| 439 | 2636 | 2637 | Type 22 Broadsword-class | 1 | 1 | Type 42 Batch 3 unlocks Type 22 |
| 440 | 2637 | 2638 | Type 23 Duke-class (Batch 1) | 1 | 1 | Type 22 unlocks Type 23 |
| 441 | 2638 | 2639 | Type 23 Duke-class (Batch 2) | 1 | 1 | Type 23 Batch 1 unlocks Batch 2 |
| 442 | 2639 | 2640 | Type 26 Frigate | 1 | 1 | Type 23 Batch 2 unlocks Type 26 |
| 443 | 2640 | 2645 | Future Cruiser Concept | 1 | 2 | Type 26 unlocks Future Cruiser (paper ship) |

**Total Unlocks**: 44 entries

---

## Research Branches Table Entries

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 23 | British | CL | Starting | FREE starting cruisers, tutorial introduction | #696969 | 2600 | 2601 | NULL | NULL | Protected Cruiser | Light Cruiser | Pelorus + Leander. FREE starting ships. Pelorus (1896) 2nd class protected, Leander (1931) better modern CL. |
| 24 | British | CA | Protected/Armored Main Line | Protected and armored cruisers, pre-dreadnought era evolution | #8B4513 | 2602 | 2607 | NULL | NULL | Protected Cruiser | Armored Cruiser | Cressy → Drake → Warrior → Duke of Edinburgh → Devonshire → Monmouth. Pre-dreadnought armored cruisers. 9.2" to 7.5" guns. |
| 25 | British | CL | Light Cruiser Main Line | Light cruisers from WWI through WWII, Royal Navy backbone | #1E90FF | 2608 | 2620 | NULL | NULL | WWI Light | WWII Peak | Town (1910) → Arethusa → C/D/E → Emerald → Leander → Amphion → Arethusa (1934) → Town (1936) → Fiji → Minotaur. 6" guns, mass production, convoy escort. |
| 26 | British | CLAA | AA Specialist | Anti-aircraft cruisers with dual-purpose 5.25" guns | #FF6347 | 2621 | 2623 | 25 | NULL | AA Cruiser | AA Cruiser | Dido → Bellona → Scylla. Stems from Light Main Line. 10×5.25" DP guns for fleet air defense. 16 ships total. |
| 27 | British | CA | Heavy Cruiser | 8" gun treaty heavy cruisers, County-class evolution | #FFD700 | 2624 | 2629 | NULL | NULL | Treaty Heavy | Improved Heavy | Hawkins → County (Kent/London/Norfolk) → York → Exeter. 8" treaty cruisers. County-class 13 ships. Empire reach and seakeeping. |
| 28 | British | CG/DDG | Post-War/Guided Missile | Cold War missile cruisers and modern destroyers | #9370DB | 2630 | 2640 | 25, 27 | NULL | Post-War | Modern | Tiger → Blake → County DDG → Bristol → Sheffield (Type 42) → Type 22 → Type 23 → Type 26. Stems from both Light + Heavy. Gun to missile evolution. Sea Dart, Sea Wolf systems. |
| 29 | British | CG/DDG | Modernization | Cold War modernizations and upgrades | #CD853F | 2641 | 2643 | 28 | NULL | Modernized | Modernized | Tiger (Modernized), County (Modernized), Sheffield (Modernized). Stems from Post-War branch. Extended service life upgrades. |
| 30 | British | CA/CG | Paper Ship | Cancelled and conceptual cruiser designs | #DC143C | 2644 | 2645 | 27, 28 | NULL | Design Phase | Future Concept | Design CA, Future Cruiser Concept. -10% reliability. Stems from Heavy + Post-War. Advanced systems and unproven technology. |

**Total Research Branches**: 8 entries

---

## Summary Statistics

- **Total Nodes**: 46 cruiser nodes (2600-2645)
- **Total Prerequisites**: 44 entries
- **Total Unlocks**: 44 entries
- **Total Research Branches**: 8 branches
- **Total Database Entries**: 96 entries for British Cruisers research tree logic

---

## Unlock Chain Flowchart

```
BRITISH CRUISER RESEARCH TREE - NAVYFIELD STYLE
════════════════════════════════════════════════════════════════

TIER 1: STARTING (FREE)
────────────────────────────────────────────────────────────────
    [2600] PELORUS         [2601] LEANDER (1931)
    Protected Cruiser       Light Cruiser
    FREE, 11 ships          FREE, 8 ships
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
TIER 2: PRE-DREADNOUGHT ERA / WWI LIGHT
────────────────────────────────────────────────────────────────
    [2602] CRESSY          [2608] TOWN (1910)     [2624] HAWKINS
    Armored Cruiser         Scout Cruiser          Heavy Cruiser
    2×9.2" guns             8×6" guns              7×7.5" guns
        │                       │                       │
    [2603] DRAKE           [2609] ARETHUSA            │
    Improved Armored        WWI Light                  │
        │                       │                       │
TIER 3: ARMORED EVOLUTION / WWI MAIN
────────────────────────────────────────────────────────────────
    [2604] WARRIOR         [2610] C-CLASS         [2625] COUNTY (KENT)
    Improved Armor          WWI Standard            8" Treaty CA
        │                       │                   13 ships total
    [2605] DUKE OF ED.     [2611] D-CLASS              │
    Enhanced Armament       WWI Improved                │
        │                       │                       │
TIER 4: LATE ARMORED / INTERWAR LIGHT
────────────────────────────────────────────────────────────────
    [2606] DEVONSHIRE      [2612] E-CLASS         [2626] COUNTY (LONDON)
    Final Armored           WWI Peak                Improved County
        │                       │                       │
    [2607] MONMOUTH        [2613] EMERALD         [2627] COUNTY (NORFOLK)
    Last Armored            First 6" Modern         Final County
                                │                       │
TIER 5: TREATY ERA
────────────────────────────────────────────────────────────────
                        [2614] LEANDER (1931)     [2628] YORK
                        Treaty Light               Reduced CA
                        8×6" guns                  6×8" guns
                            │                       │
                        [2615] AMPHION         [2629] EXETER
                        Improved Leander            Improved York
                            │                       │
TIER 6: PRE-WWII / EARLY WWII
────────────────────────────────────────────────────────────────
                        [2616] ARETHUSA (1934)      │
                        Enhanced Light               │
                            │                        │
                        [2617] TOWN (1936)           │
                        12×6" guns                   │
                            │                        │
TIER 7: WWII PEAK
────────────────────────────────────────────────────────────────
                        [2618] FIJI ─────────────────┴───┐
                        Colony-class                     │
                        12×6" guns                       │
                            │                            │
                ┌───────────┴───────────┐                │
                │                       │                │
            [2619] MINOTAUR        [2621] DIDO          │
            Late WWII               AA Cruiser          │
            10×5.25" DP             10×5.25" DP         │
                │                       │               │
                │                   [2622] BELLONA      │
                │                   Improved AA         │
                │                       │               │
                │                   [2623] SCYLLA       │
                │                   Final AA            │
                │                                       │
TIER 8: POST-WAR GUN
────────────────────────────────────────────────────────────────
                [2630] TIGER ◄──────────────────────────┘
                Post-War Gun
                4×6", 6×3" AA
                    │
        ┌───────────┼───────────┐
        │           │           │
    [2641]      [2631]          │
    TIGER       BLAKE           │
    (Mod)       Improved Tiger  │
    Helo ops        │           │
                    │           │
TIER 9: EARLY MISSILE / MODERN
────────────────────────────────────────────────────────────────
                [2632] COUNTY (DDG)
                First Missile Destroyer
                Sea Slug SAM, 4 ships
                    │
        ┌───────────┼───────────┐
        │           │           │
    [2642]      [2633]          │
    COUNTY      BRISTOL         │
    (Mod)       Improved DDG    │
    Sea Dart        │           │
                    │           │
                [2634] SHEFFIELD (Type 42 Batch 1)
                Sea Dart SAM
                    │
        ┌───────────┼───────────┐
        │           │           │
    [2643]      [2635]          │
    SHEFFIELD   TYPE 42         │
    (Mod)       (Batch 2)       │
    Upgraded        │           │
                    │           │
                [2636] TYPE 42 (Batch 3)
                Final Sea Dart
                    │           │
TIER 10: MODERN / FUTURE
────────────────────────────────────────────────────────────────
                [2637] TYPE 22 BROADSWORD
                ASW Frigate, Sea Wolf
                    │
                [2638] TYPE 23 DUKE (Batch 1)
                Modern Frigate, Stealth
                    │
                [2639] TYPE 23 DUKE (Batch 2)
                Improved Type 23
                    │
                [2640] TYPE 26
                Next-Generation Frigate
                    │
                [2645] FUTURE CRUISER
                Concept design (Paper)

PAPER SHIPS BRANCH
────────────────────────────────────────────────────────────────
        [2644] DESIGN CA
        Cancelled CA design
        From Exeter
```

---

**Status**: ✅ British Cruisers Research Tree Logic COMPLETE
