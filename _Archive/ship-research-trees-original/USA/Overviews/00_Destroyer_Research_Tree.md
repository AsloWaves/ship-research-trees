# US Navy Destroyer Research Tree (1902-Present)

## Era Overview

| Era | Years | Key Innovation | Classes |
|-----|-------|----------------|---------|
| **Early Destroyers** | 1902-1917 | Coal→Oil, Turbines | 9 classes |
| **WWI Flush-Deckers** | 1917-1922 | Mass production, Flush deck | 3 classes (267 ships!) |
| **Interwar Treaty** | 1934-1943 | 5"/38 dual-purpose guns | 8 classes |
| **WWII** | 1942-1952 | Large hulls, Heavy AA | 3 classes (331 ships!) |
| **Post-WWII** | 1953-1959 | High-pressure steam, Destroyer leaders | 3 classes |
| **Guided Missile** | 1960-1964 | SAM systems, Terrier/Tartar | 2 classes |
| **Gas Turbine** | 1975-1983 | Gas turbines, VLS | 2 classes |
| **Aegis Era** | 1991-Present | Phased array radar, BMD | 2 classes |

**Total:** 32 major classes, ~1,200+ destroyers built

## Production Summary

| Type | Classes | Total Ships | Peak Era |
|------|---------|-------------|----------|
| Early Destroyers | 9 | ~100 ships | 1902-1917 |
| WWI Flush-Deckers | 3 | 267 ships | 1917-1922 (Clemson: 156) |
| Interwar Treaty | 8 | ~160 ships | 1934-1943 |
| WWII Destroyers | 3 | 331 ships | 1942-1952 (Fletcher: 175) |
| Post-WWII Conventional | 3 | ~50 ships | 1953-1959 |
| Guided Missile | 2 | ~33 ships | 1960-1964 |
| Gas Turbine | 2 | 35 ships | 1975-1983 |
| Aegis Era | 2 | 92+ ships | 1991-Present (Arleigh Burke: 89+) |
| **Grand Total** | **32** | **~1,068+** | **122 years** |

## Research Tree Diagram

```mermaid
graph TD
    %% ============================================================
    %% BRANCH 1: FLEET DESTROYER MAIN LINE (Left Side)
    %% ============================================================
    BAIN[Bainbridge DD-1 1902<br/>FIRST US DESTROYER<br/>FREE<br/>420 tons, 5x3in]
    BAIN --> SMITH[Smith DD-17 1909<br/>FIRST TURBINES<br/>Last coal-fired]
    SMITH --> PAUL[Paulding DD-22 1910<br/>FIRST OIL-FIRED<br/>21 ships]
    PAUL --> CASS[Cassin DD-43 1913<br/>4-inch guns<br/>8 ships]
    CASS --> OBR[O'Brien DD-51 1914<br/>21-INCH TORPEDOES<br/>6 ships]
    OBR --> SAMP[Sampson DD-63 1916<br/>FIRST AA GUNS<br/>6 ships]

    %% WWI Mass Production
    SAMP --> WICK[Wickes DD-75 1917<br/>FLUSH-DECK<br/>111 SHIPS]
    WICK --> CLEM[Clemson DD-186 1919<br/>WWI ULTIMATE<br/>156 SHIPS<br/>LARGEST CLASS EVER]

    %% Treaty Era
    CLEM --> FARR[Farragut DD-348 1934<br/>TREATY ERA<br/>5in/38 dual-purpose<br/>8 ships]
    FARR --> MAHA[Mahan DD-364 1936<br/>12 torpedoes<br/>18 ships]
    MAHA --> GRID[Gridley DD-380 1937<br/>16 torpedoes max<br/>4 ships]
    GRID --> BENS[Benson DD-421 1940<br/>Quintuple torpedoes<br/>30 ships]
    BENS --> GLEAV[Gleaves DD-423 1940<br/>850F steam<br/>66 SHIPS]

    %% WWII Mass Production
    GLEAV --> FLET[Fletcher DD-445 1942<br/>WWII WORKHORSE<br/>175 SHIPS<br/>LEGENDARY]
    FLET --> SUMN[Allen M. Sumner DD-692 1943<br/>TWIN 5in MOUNTS<br/>58 ships]
    SUMN --> GEAR[Gearing DD-710 1945<br/>WWII ULTIMATE<br/>98 ships<br/>Extended Sumner]

    %% Post-WWII Conventional
    GEAR --> SHER[Forrest Sherman DD-931 1955<br/>5in/54 guns<br/>1200 psi steam<br/>18 ships]

    %% Modern Multi-Role
    SHER --> SPRU[Spruance DD-963 1975<br/>GAS TURBINES<br/>VLS cells<br/>31 ships]
    SPRU --> BURKF1[Arleigh Burke Flight I 1991<br/>AEGIS SYSTEM<br/>SPY-1D radar<br/>21 ships]
    BURKF1 --> BURKF2[Arleigh Burke Flight II 1998<br/>Improved<br/>7 ships]
    BURKF2 --> BURKF2A[Arleigh Burke Flight IIA 2000<br/>Helicopter hangar<br/>34 ships]
    BURKF2A --> BURKF3[Arleigh Burke Flight III 2023<br/>ULTIMATE DESTROYER<br/>SPY-6 AESA radar<br/>Future]

    %% ============================================================
    %% BRANCH 2: GUIDED MISSILE DESTROYER LINE (Middle)
    %% ============================================================
    GEAR --> FRAM[Gearing FRAM II 1960s<br/>MISSILE CONVERSION<br/>Tartar/ASROC retrofit]
    FRAM --> GYATT[Gyatt DDG-1 1956<br/>FIRST MISSILE DD<br/>Terrier experimental<br/>1 ship]
    GYATT --> ADAM[Charles F. Adams DDG-2 1960<br/>TARTAR SAM<br/>Mk 13 launcher<br/>23 SHIPS]
    ADAM --> ADAM14[Adams DDG-14 1963<br/>Improved AAW<br/>Export success]
    ADAM14 --> KIDD[Kidd DDG-993 1981<br/>AAW SPRUANCE<br/>Built for Iran<br/>4 ships]
    KIDD --> ZUM[Zumwalt DDG-1000 2016<br/>STEALTH DESTROYER<br/>155mm AGS<br/>3 ships]
    ZUM --> DDGX[DDG-X 2030s<br/>FUTURE ULTIMATE<br/>Next generation<br/>Hypersonics]

    %% ============================================================
    %% BRANCH 3: DESTROYER LEADER / LARGE DESTROYER LINE (Right)
    %% ============================================================
    CLEM --> PORT[Porter DD-356 1936<br/>DESTROYER LEADER<br/>8x5in guns<br/>1,850 tons, 8 ships]
    PORT --> SOMER[Somers DD-381 1937<br/>Large leader<br/>8x5in guns<br/>5 ships]
    SOMER --> GLEAV2[Gleaves DD-423 1940<br/>Late treaty<br/>Merge point]

    GEAR --> NORF[Norfolk DL-1 1953<br/>FIRST DESTROYER LEADER<br/>5,600 tons<br/>Experimental]
    NORF --> MITS[Mitscher DL-2 1953<br/>Large leader<br/>3,675 tons<br/>4 ships]
    MITS --> COON[Farragut/Coontz DDG-37 1960<br/>TERRIER MISSILES<br/>5,800 tons<br/>10 ships]
    COON --> LEAHY[Leahy CG-16 1962<br/>LARGE MISSILE SHIP<br/>Twin Terrier<br/>8,200 tons, 9 ships]
    LEAHY --> BELK[Belknap CG-26 1964<br/>MISSILE CRUISER<br/>5in/54 + Terrier<br/>9 ships]
    BELK --> CAL[California CGN-36 1974<br/>NUCLEAR CRUISER<br/>Twin Mk 13<br/>2 ships]
    CAL --> TICO1[Ticonderoga CG-47 1983<br/>AEGIS CRUISER<br/>Mk 26 launchers<br/>5 ships]
    TICO1 --> TICO2[Ticonderoga CG-52 1986<br/>VLS FROM START<br/>Mk 41 VLS<br/>22 SHIPS]
    TICO2 --> CGX[CG-X Future<br/>ULTIMATE CRUISER<br/>Next generation<br/>Planned]

    %% Cross-branch alternatives
    GLEAV2 -.-> FLET
    KIDD -.-> BURKF1
    ADAM -.-> SPRU

    %% ============================================================
    %% STYLING
    %% ============================================================

    %% First destroyer
    style BAIN fill:#FFD700,stroke:#333,stroke-width:3px,color:#000

    %% WWI mass production
    style WICK fill:#0f0,stroke:#333,stroke-width:2px,color:#000
    style CLEM fill:#0f0,stroke:#333,stroke-width:3px,color:#000

    %% WWII legendary
    style FLET fill:#0f0,stroke:#333,stroke-width:4px,color:#000
    style GEAR fill:#0ff,stroke:#333,stroke-width:2px,color:#000

    %% First guided missile
    style GYATT fill:#f90,stroke:#333,stroke-width:2px,color:#000
    style ADAM fill:#0ff,stroke:#333,stroke-width:3px,color:#000

    %% Gas turbines
    style SPRU fill:#f0f,stroke:#333,stroke-width:3px,color:#000

    %% Aegis revolution
    style BURKF1 fill:#0ff,stroke:#333,stroke-width:3px,color:#000
    style TICO1 fill:#f90,stroke:#333,stroke-width:3px,color:#000

    %% Ultimate endgame
    style BURKF3 fill:#00f,stroke:#333,stroke-width:4px,color:#fff
    style DDGX fill:#00f,stroke:#333,stroke-width:4px,color:#fff
    style CGX fill:#00f,stroke:#333,stroke-width:4px,color:#fff

    %% Stealth
    style ZUM fill:#9370DB,stroke:#333,stroke-width:3px,color:#fff
```

## Major Milestones

### Technological Firsts

| Achievement | Class | Year |
|-------------|-------|------|
| **First US destroyers** | Bainbridge | 1902 |
| **First turbines** | Smith | 1909 |
| **First oil-fired** | Paulding | 1910 |
| **First 21-inch torpedoes** | O'Brien | 1914 |
| **First AA guns** | Sampson | 1916 |
| **First flush-deck** | Caldwell | 1917 |
| **Largest class ever** | Clemson | 1919 (156 ships) |
| **First 5-inch/38 guns** | Farragut | 1934 |
| **Most numerous wartime** | Fletcher | 1942 (175 ships) |
| **First twin mounts** | Allen M. Sumner | 1943 |
| **First 5-inch/54 guns** | Forrest Sherman | 1955 |
| **First guided missiles** | Farragut/Coontz | 1960 |
| **First gas turbines** | Spruance | 1975 |
| **First Aegis system** | Arleigh Burke | 1991 |
| **First stealth destroyer** | Zumwalt | 2016 |

## Timeline

```mermaid
graph LR
    A[1902<br/>Bainbridge<br/>First destroyer] --> B[1909<br/>Smith<br/>First turbines]
    B --> C[1910<br/>Paulding<br/>First oil-fired]
    C --> D[1916<br/>Sampson<br/>First AA guns]
    D --> E[1918<br/>Wickes<br/>111 ships]
    E --> F[1919<br/>Clemson<br/>156 ships]
    F --> G[1934<br/>Farragut<br/>5-inch/38 guns]
    G --> H[1942<br/>Fletcher<br/>175 ships]
    H --> I[1943<br/>Sumner<br/>Twin mounts]
    I --> J[1955<br/>Forrest Sherman<br/>5-inch/54 guns]
    J --> K[1960<br/>Farragut DDG<br/>First missiles]
    K --> L[1975<br/>Spruance<br/>Gas turbines]
    L --> M[1991<br/>Arleigh Burke<br/>Aegis system]
    M --> N[2016<br/>Zumwalt<br/>Stealth]

    style A fill:#f9f,stroke:#333,stroke-width:4px
    style F fill:#ff0,stroke:#333,stroke-width:4px
    style H fill:#0f0,stroke:#333,stroke-width:4px
    style M fill:#00f,stroke:#fff,stroke-width:4px,color:#fff
```

---

## Key Technological Innovations

### Propulsion Evolution
1. **1902-1909**: Coal-fired, Triple-expansion engines
2. **1909**: First turbines ([[Smith-Class]])
3. **1910**: Oil-fired boilers ([[Paulding-Class]])
4. **1934**: Superheated steam ([[Farragut-Class]])
5. **1953**: 1200 psi high-pressure ([[Forrest Sherman-Class]])
6. **1975**: Gas turbines ([[Spruance-Class]])
7. **2016**: Integrated electric ([[Zumwalt-Class]])

### Armament Evolution
1. **1902**: 2× 3"/50 guns
2. **1913**: 4× 4"/50 guns ([[Cassin-Class]])
3. **1916**: First AA guns ([[Sampson-Class]])
4. **1934**: 5"/38 dual-purpose ([[Farragut-Class]])
5. **1943**: Twin 5" mounts ([[Allen M. Sumner-Class]])
6. **1955**: 5"/54 guns ([[Forrest Sherman-Class]])
7. **1960**: Guided missiles ([[Farragut-Coontz-Class]])
8. **1975**: VLS cells ([[Spruance-Class]])
9. **1991**: Aegis + 90-96 VLS ([[Arleigh Burke-Class]])

### Fire Control Evolution
1. **1902-1934**: Manual optical sights
2. **1934**: Mark 33 GFCS ([[Farragut-Class]])
3. **1939**: Mark 37 GFCS with computer ([[Sims-Class]])
4. **1942**: Radar fire control ([[Fletcher-Class]])
5. **1960**: Missile fire control ([[Farragut-Coontz-Class]])
6. **1991**: Aegis Combat System ([[Arleigh Burke-Class]])

---

## Production Numbers (Top 10)

| Rank | Class | Ships | Years | Notes |
|------|-------|-------|-------|-------|
| 1 | [[Clemson-Class]] | 156 | 1919-22 | Largest ever |
| 2 | [[Fletcher-Class]] | 175 | 1942-44 | Most numerous wartime |
| 3 | [[Wickes-Class]] | 111 | 1918-21 | WWI mass production |
| 4 | [[Gearing-Class]] | 98 | 1945-52 | Extended Sumner |
| 5 | [[Arleigh Burke-Class]] | 89+ | 1991-Present | Still building |
| 6 | [[Gleaves-Class]] | 66 | 1940-43 | WWII workhorse |
| 7 | [[Allen M. Sumner-Class]] | 58 | 1943-46 | Twin mounts |
| 8 | [[Spruance-Class]] | 31 | 1975-83 | Gas turbines |
| 9 | [[Benson-Class]] | 30 | 1940-43 | Quintuple torpedoes |
| 10 | [[Charles F. Adams-Class]] | 23 | 1960-64 | Tartar DDG |

---

## Research Links by Era

### Early Destroyers (1902-1917)
- [[USA/USA Cruisers/Bainbridge-Class]] (DD-1, 1902) - First US destroyers
- [[USA/USA Cruisers/Truxtun-Class]] (DD-14, 1902)
- [[Smith-Class]] (DD-17, 1909) - **First turbines, last coal**
- [[Paulding-Class]] (DD-22, 1910) - **First oil-fired**
- [[Cassin-Class]] (DD-43, 1913) - First 4" guns
- [[Aylwin-Class]] (DD-47, 1913)
- [[O'Brien-Class]] (DD-51, 1914) - **First 21" torpedoes**
- [[Tucker-Class]] (DD-57, 1915) - First geared turbines
- [[Sampson-Class]] (DD-63, 1916) - **First AA guns**

### WWI Flush-Deckers (1917-1922)
- [[Caldwell-Class]] (DD-69, 1917) - First flush-deck
- [[Wickes-Class]] (DD-75, 1918) - **111 ships**
- [[Clemson-Class]] (DD-186, 1919) - **156 ships, largest class ever**

### Interwar Treaty Ships (1934-1943)
- [[Farragut-Class]] (DD-348, 1934) - **First 5"/38 dual-purpose**
- [[Mahan-Class]] (DD-364, 1936) - 12 torpedoes
- [[Gridley-Class]] (DD-380, 1937) - 16 torpedoes (max)
- [[Bagley-Class]] (DD-386, 1937)
- [[Benham-Class]] (DD-397, 1939) - 3 boilers
- [[Sims-Class]] (DD-409, 1939) - **Mark 37 FCS**
- [[Benson-Class]] (DD-421, 1940) - Quintuple torpedoes
- [[Gleaves-Class]] (DD-423, 1940) - 850°F steam

### WWII Destroyers (1942-1952)
- [[Fletcher-Class]] (DD-445, 1942) - **175 ships, legendary**
- [[Allen M. Sumner-Class]] (DD-692, 1943) - **Twin gun mounts**
- [[Gearing-Class]] (DD-710, 1945) - Extended Sumner, **98 ships**

### Post-WWII Conventional (1953-1959)
- [[Norfolk-Class]] (DL-1, 1953) - **Experimental destroyer leader, 1 ship**
- [[Mitscher-Class]] (DL-2 to DL-5, 1953-1954) - **Destroyer leaders, 2 converted to DDG**
- [[Forrest Sherman-Class]] (DD-931, 1955) - **5"/54 guns, 1200 psi**

### Guided Missile Age (1960-1964)
- [[Farragut-Coontz-Class]] (DDG-37, 1960) - **Terrier SAM**
- [[Charles F. Adams-Class]] (DDG-2, 1960) - **Tartar SAM, 23 ships**

### Gas Turbine Era (1975-1983)
- [[Spruance-Class]] (DD-963, 1975) - **Gas turbines, VLS, 31 ships**
- [[Kidd-Class]] (DDG-993, 1981-1982) - **AAW variant, built for Iran, 4 ships**

### Aegis Era (1991-Present)
- [[Arleigh Burke-Class]] (DDG-51, 1991) - **Aegis, 89+ ships, still building**
- [[Zumwalt-Class]] (DDG-1000, 2016) - **Stealth, 3 ships only**

---

## Comparison by Era

### Displacement Growth
| Era | Typical | Example |
|-----|---------|---------|
| Early (1902-17) | 420-1,225t | Bainbridge 420t |
| WWI (1917-22) | 1,154-1,190t | Wickes 1,154t |
| Treaty (1934-43) | 1,500-1,630t | Farragut 1,500t |
| WWII (1942-52) | 2,050-2,616t | Fletcher 2,050t |
| Post-WWII (1955-59) | 2,800-4,050t | Sherman 2,800t |
| DDG (1960-64) | 3,370-5,648t | Adams 3,370t |
| Gas Turbine (1975-83) | 8,040-9,600t | Spruance 8,040t |
| Aegis (1991-Present) | 8,315-15,995t | Burke 8,315t |

### Speed Trend
- **1902-1918**: 29-35 knots
- **1918-1943**: 35-37 knots (peak)
- **1943-Present**: 30-35 knots (slower but more capable)

### Main Battery Evolution
- **1902-1913**: 2-5× 3" guns
- **1913-1934**: 4-5× 4" guns
- **1934-1955**: 4-6× 5"/38 guns
- **1955-1960**: 1-3× 5"/54 guns
- **1960-Present**: 1-2× 5"/54 or 5"/62 guns + missiles

---

**Tree:** Master Research Tree | **Classes:** 32 | **Ships:** ~1,068+

#destroyer #us-navy #research-tree #complete #1902-present #all-classes #evolution
