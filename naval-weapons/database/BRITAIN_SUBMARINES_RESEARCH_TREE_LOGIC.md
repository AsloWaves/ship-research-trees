# Britain Submarines Research Tree Logic

**Date**: January 2025
**Ship Type**: Submarines (SS, SSN, SSBN)
**Total Nodes**: 39 (2800-2838)

---

## Research Branches Overview

| Branch_ID | Branch_Name | Branch_Description | Start_Node | End_Node | Nodes |
|-----------|-------------|-------------------|------------|----------|-------|
| 40 | Starting | FREE starting submarines, tutorial introduction | 2800 | 2801 | 2 |
| 41 | Coastal | Coastal patrol submarines, British waters | 2802 | 2806 | 5 |
| 42 | Fleet Diesel Main Line | Ocean-going diesel submarines, RN backbone | 2807 | 2819 | 13 |
| 43 | WWII Main Line | WWII fleet submarines, T-class dominance | 2820 | 2824 | 5 |
| 44 | Modernization | GUPPY-equivalent upgrades, cold war extensions | 2825 | 2826 | 2 |
| 45 | Nuclear Attack | Nuclear-powered attack submarines, SSN | 2827 | 2833 | 7 |
| 46 | Ballistic Missile | Nuclear-powered ballistic missile submarines, SSBN | 2834 | 2836 | 3 |
| 47 | Alternative/Experimental | Experimental designs and special purpose | 2837 | 2838 | 2 |

---

## Prerequisites Table Entries

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 500 | 2802 | 2801 | A-class | 1 | NULL | B-class requires A-class (coastal path) |
| 501 | 2807 | 2801 | A-class | 1 | NULL | Fleet D-class requires A-class (fleet path) |
| 502 | 2803 | 2802 | B-class | 1 | NULL | C-class requires B-class |
| 503 | 2804 | 2803 | C-class | 1 | NULL | Coastal D-class requires C-class |
| 504 | 2805 | 2804 | D-class (Coastal) | 1 | NULL | Coastal E-class requires D-class |
| 505 | 2806 | 2805 | E-class (Coastal) | 1 | NULL | H-class requires E-class |
| 506 | 2808 | 2807 | D-class (Fleet) | 1 | NULL | Fleet E-class requires Fleet D-class |
| 507 | 2809 | 2808 | E-class (Fleet) | 1 | NULL | F-class requires E-class |
| 508 | 2810 | 2809 | F-class | 1 | NULL | G-class requires F-class |
| 509 | 2811 | 2810 | G-class | 1 | NULL | H-class requires G-class (fleet variant) |
| 510 | 2811 | 2806 | H-class (Coastal) | 1 | 1 | H-class requires G-class OR coastal H |
| 511 | 2812 | 2811 | H-class | 1 | NULL | J-class requires H-class |
| 512 | 2813 | 2812 | J-class | 1 | NULL | K-class requires J-class |
| 513 | 2814 | 2813 | K-class | 1 | NULL | L-class requires K-class |
| 514 | 2815 | 2814 | L-class | 1 | NULL | M-class requires L-class |
| 515 | 2816 | 2815 | M-class | 1 | NULL | O-class requires M-class |
| 516 | 2817 | 2816 | O-class | 1 | NULL | P-class requires O-class |
| 517 | 2818 | 2817 | P-class | 1 | NULL | R-class requires P-class |
| 518 | 2819 | 2818 | R-class | 1 | NULL | S-class requires R-class |
| 519 | 2820 | 2819 | S-class | 1 | NULL | T-class requires S-class |
| 520 | 2821 | 2820 | T-class | 1 | NULL | U-class requires T-class |
| 521 | 2822 | 2821 | U-class | 1 | NULL | V-class requires U-class |
| 522 | 2823 | 2822 | V-class | 1 | NULL | A-class (1945) requires V-class |
| 523 | 2824 | 2823 | A-class (1945) | 1 | NULL | Porpoise requires A-class (1945) |
| 524 | 2825 | 2820 | T-class | 1 | NULL | T-class Streamlined requires base T-class |
| 525 | 2826 | 2823 | A-class (1945) | 1 | NULL | A-class Modernized requires base A-class |
| 526 | 2827 | 2824 | Porpoise-class | 1 | NULL | Dreadnought requires Porpoise |
| 527 | 2828 | 2827 | Dreadnought SSN | 1 | NULL | Valiant requires Dreadnought |
| 528 | 2829 | 2828 | Valiant-class | 1 | NULL | Churchill requires Valiant |
| 529 | 2830 | 2829 | Churchill-class | 1 | NULL | Swiftsure requires Churchill |
| 530 | 2831 | 2830 | Swiftsure-class | 1 | NULL | Trafalgar requires Swiftsure |
| 531 | 2832 | 2831 | Trafalgar-class | 1 | NULL | Astute Batch 1 requires Trafalgar |
| 532 | 2833 | 2832 | Astute-class (Batch 1) | 1 | NULL | Astute Batch 2 requires Batch 1 |
| 533 | 2834 | 2828 | Valiant-class | 1 | NULL | Resolution requires Valiant (ballistic path) |
| 534 | 2835 | 2834 | Resolution-class | 1 | NULL | Vanguard requires Resolution |
| 535 | 2836 | 2835 | Vanguard-class | 1 | NULL | Dreadnought SSBN requires Vanguard |
| 536 | 2837 | 2820 | T-class | 1 | NULL | X-craft requires T-class (experimental) |
| 537 | 2838 | 2824 | Porpoise-class | 1 | NULL | Explorer requires Porpoise (experimental) |

**Total Prerequisites**: 38 entries

---

## Unlocks Table Entries

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 600 | 2801 | 2802 | B-class | 1 | 1 | A-class unlocks B-class (coastal path) |
| 601 | 2801 | 2807 | D-class (Fleet) | 1 | 1 | A-class unlocks D-class (fleet path) |
| 602 | 2802 | 2803 | C-class | 1 | 1 | B-class unlocks C-class |
| 603 | 2803 | 2804 | D-class (Coastal) | 1 | 1 | C-class unlocks D-class |
| 604 | 2804 | 2805 | E-class (Coastal) | 1 | 1 | Coastal D unlocks E-class |
| 605 | 2805 | 2806 | H-class (Coastal) | 1 | 1 | Coastal E unlocks H-class |
| 606 | 2806 | 2811 | H-class | 1 | 1 | Coastal H unlocks fleet H (alternative path) |
| 607 | 2807 | 2808 | E-class (Fleet) | 1 | 1 | Fleet D unlocks E-class |
| 608 | 2808 | 2809 | F-class | 1 | 1 | Fleet E unlocks F-class |
| 609 | 2809 | 2810 | G-class | 1 | 1 | F-class unlocks G-class |
| 610 | 2810 | 2811 | H-class | 1 | 1 | G-class unlocks H-class |
| 611 | 2811 | 2812 | J-class | 1 | 1 | H-class unlocks J-class |
| 612 | 2812 | 2813 | K-class | 1 | 1 | J-class unlocks K-class |
| 613 | 2813 | 2814 | L-class | 1 | 1 | K-class unlocks L-class |
| 614 | 2814 | 2815 | M-class | 1 | 1 | L-class unlocks M-class |
| 615 | 2815 | 2816 | O-class | 1 | 1 | M-class unlocks O-class |
| 616 | 2816 | 2817 | P-class | 1 | 1 | O-class unlocks P-class |
| 617 | 2817 | 2818 | R-class | 1 | 1 | P-class unlocks R-class |
| 618 | 2818 | 2819 | S-class | 1 | 1 | R-class unlocks S-class |
| 619 | 2819 | 2820 | T-class | 1 | 1 | S-class unlocks T-class |
| 620 | 2820 | 2821 | U-class | 1 | 1 | T-class unlocks U-class |
| 621 | 2820 | 2825 | T-class (Streamlined) | 1 | 2 | T-class unlocks its own modernization |
| 622 | 2820 | 2837 | X-craft | 1 | 3 | T-class unlocks X-craft (experimental) |
| 623 | 2821 | 2822 | V-class | 1 | 1 | U-class unlocks V-class |
| 624 | 2822 | 2823 | A-class (1945) | 1 | 1 | V-class unlocks A-class (1945) |
| 625 | 2823 | 2824 | Porpoise-class | 1 | 1 | A-class (1945) unlocks Porpoise |
| 626 | 2823 | 2826 | A-class (Modernized) | 1 | 2 | A-class (1945) unlocks its own modernization |
| 627 | 2824 | 2827 | Dreadnought SSN | 1 | 1 | Porpoise unlocks Dreadnought (nuclear) |
| 628 | 2824 | 2838 | Explorer HTP | 1 | 2 | Porpoise unlocks Explorer (experimental) |
| 629 | 2827 | 2828 | Valiant-class | 1 | 1 | Dreadnought unlocks Valiant |
| 630 | 2828 | 2829 | Churchill-class | 1 | 1 | Valiant unlocks Churchill |
| 631 | 2828 | 2834 | Resolution-class | 1 | 2 | Valiant unlocks Resolution (ballistic path) |
| 632 | 2829 | 2830 | Swiftsure-class | 1 | 1 | Churchill unlocks Swiftsure |
| 633 | 2830 | 2831 | Trafalgar-class | 1 | 1 | Swiftsure unlocks Trafalgar |
| 634 | 2831 | 2832 | Astute-class (Batch 1) | 1 | 1 | Trafalgar unlocks Astute |
| 635 | 2832 | 2833 | Astute-class (Batch 2) | 1 | 1 | Astute Batch 1 unlocks Batch 2 |
| 636 | 2834 | 2835 | Vanguard-class | 1 | 1 | Resolution unlocks Vanguard |
| 637 | 2835 | 2836 | Dreadnought SSBN | 1 | 1 | Vanguard unlocks Dreadnought SSBN |

**Total Unlocks**: 38 entries

---

## Research Branches Table Entries

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 40 | British | SS | Starting | FREE starting submarines, tutorial introduction | #696969 | 2800 | 2801 | NULL | NULL | Early Submarine | Coastal Submarine | Holland + A-class. FREE starting subs. Holland (1901) primitive, A-class (1903) improved. |
| 41 | British | SS | Coastal | Coastal patrol submarines, British waters operations | #8B4513 | 2802 | 2806 | NULL | NULL | Coastal | Coastal | B → C → D → E → H-class. Coastal patrol submarines. British waters operations. Small, limited range. |
| 42 | British | SS | Fleet Diesel Main Line | Ocean-going diesel submarines, Royal Navy backbone | #1E90FF | 2807 | 2819 | NULL | NULL | WWI | Interwar | D (Fleet) → E → F → G → H → J → K → L → M → O → P → R → S-class. Fleet diesel submarines. Ocean-going capability. RN submarine backbone. |
| 43 | British | SS | WWII Main Line | WWII fleet submarines, T-class dominance | #FFD700 | 2820 | 2824 | 42 | NULL | WWII | Post-War | T → U → V → A-class (1945) → Porpoise. Stems from Fleet Diesel. T-class: 53 boats, most successful British SS. Post-war Porpoise transition class. |
| 44 | British | SS | Modernization | GUPPY-equivalent upgrades, cold war service extensions | #CD853F | 2825 | 2826 | 43 | NULL | Modernized | Modernized | T-class (Streamlined), A-class (Modernized). Stems from WWII Main Line. Streamlined hulls, snorkel equipment. Extended cold war service. |
| 45 | British | SSN | Nuclear Attack | Nuclear-powered attack submarines, unlimited range | #FF1493 | 2827 | 2833 | 43 | NULL | Nuclear | Modern | Dreadnought → Valiant → Churchill → Swiftsure → Trafalgar → Astute (2 batches). Stems from WWII Main Line. Silent Service: +15% stealth. Nuclear revolution. |
| 46 | British | SSBN | Ballistic Missile | Nuclear-powered ballistic missile submarines, deterrent | #9370DB | 2834 | 2836 | 45 | NULL | Ballistic | Future | Resolution → Vanguard → Dreadnought SSBN. Stems from Nuclear Attack. Polaris/Trident deterrent. Continuous at-sea deterrent (CASD). |
| 47 | British | SS/SSE | Alternative/Experimental | Experimental designs and special purpose submarines | #FF8C00 | 2837 | 2838 | 43 | NULL | Experimental | Experimental | X-craft (midget), Explorer (HTP). Stems from WWII Main Line. X-craft: 4-man midget sub. Explorer: hydrogen peroxide experimental. |

**Total Research Branches**: 8 entries

---

## Summary Statistics

- **Total Nodes**: 39 submarine nodes (2800-2838)
- **Total Prerequisites**: 38 entries
- **Total Unlocks**: 38 entries
- **Total Research Branches**: 8 branches
- **Total Database Entries**: 85 entries for British Submarines research tree logic

---

## Unlock Chain Flowchart

```
BRITISH SUBMARINE RESEARCH TREE - NAVYFIELD STYLE
════════════════════════════════════════════════════════════════

TIER 1: STARTING (FREE)
────────────────────────────────────────────────────────────────
    [2800] HOLLAND        [2801] A-CLASS
    Early Submarine        Improved Sub
    FREE, primitive        FREE, 13 ships
                                │
                    ┌───────────┴───────────┐
                    │                       │
TIER 2: COASTAL / FLEET SPLIT
────────────────────────────────────────────────────────────────
                [2802] B-CLASS      [2807] D-CLASS (FLEET)
                Coastal Sub          Fleet Submarine
                    │                       │
                [2803] C-CLASS      [2808] E-CLASS (FLEET)
                Coastal             Fleet
                    │                       │
TIER 3: EARLY DIESEL
────────────────────────────────────────────────────────────────
            [2804] D-CLASS (COASTAL) [2809] F-CLASS
            Coastal D                 Fleet F
                    │                       │
            [2805] E-CLASS (COASTAL) [2810] G-CLASS
            Coastal E                 Fleet G
                    │                       │
TIER 4: WWI ERA
────────────────────────────────────────────────────────────────
                [2806] H-CLASS ◄─────┘
                (Coastal variant)
                    │
                [2811] H-CLASS
                (Fleet variant)
                    │
                [2812] J-CLASS
                WWI Fleet
                    │
TIER 5: INTERWAR DEVELOPMENT
────────────────────────────────────────────────────────────────
                [2813] K-CLASS
                Steam turbine experimental
                    │
                [2814] L-CLASS
                Improved fleet
                    │
                [2815] M-CLASS
                Monitor submarine (12" gun)
                    │
                [2816] O-CLASS
                Overseas patrol
                    │
TIER 6: PRE-WWII
────────────────────────────────────────────────────────────────
                [2817] P-CLASS
                Patrol submarine
                    │
                [2818] R-CLASS
                Improved patrol
                    │
                [2819] S-CLASS
                Medium fleet, 62 boats
                    │
TIER 7: WWII MAIN LINE
────────────────────────────────────────────────────────────────
                [2820] T-CLASS
                53 boats, most successful
                    │
        ┌───────────┼───────────┬───────────┐
        │           │           │           │
    [2825]      [2821]      [2837]         │
    T-CLASS     U-CLASS     X-CRAFT        │
    (STREAMLINED) Fleet    Midget          │
    Modernized    │                        │
                [2822] V-CLASS              │
                Fleet variant               │
                    │                       │
                [2823] A-CLASS (1945)       │
                Post-war diesel             │
                    │                       │
        ┌───────────┴───────────┐           │
        │                       │           │
    [2826]                  [2824]          │
    A-CLASS                 PORPOISE-CLASS  │
    (MODERNIZED)            Transition class│
    Modernized                  │           │
                    ┌───────────┴───────────┘
                    │           │
                [2838]      [2827] DREADNOUGHT SSN
                EXPLORER     First nuclear, PWR
                HTP          1954, unique
                Experimental     │
                            [2828] VALIANT-CLASS
                            Production nuclear
                                │
                    ┌───────────┴───────────┐
                    │                       │
TIER 8: NUCLEAR ERA            [2834] RESOLUTION-CLASS
────────────────────────────   First SSBN, Polaris
                [2829] CHURCHILL-CLASS │
                Improved SSN    [2835] VANGUARD-CLASS
                    │           Trident SSBN
                [2830] SWIFTSURE-CLASS │
                Quiet SSN       [2836] DREADNOUGHT SSBN
                    │           Future SSBN
TIER 9: MODERN NUCLEAR
────────────────────────────────────────────────────────────────
                [2831] TRAFALGAR-CLASS
                Modern attack SSN
                    │
                [2832] ASTUTE-CLASS (BATCH 1)
                Advanced SSN, 4 ships
                    │
TIER 10: CURRENT/FUTURE
────────────────────────────────────────────────────────────────
                [2833] ASTUTE-CLASS (BATCH 2)
                Current production, 3 ships
```

---

**Status**: ✅ British Submarines Research Tree Logic COMPLETE
