# TURRET, AMMUNITION & GUN RESEARCH SYSTEMS
## WOS2.3 Naval MMO - Complete Weapons Economy Design

### EXECUTIVE SUMMARY

**Purpose**: Define complete economic and progression systems for naval gun warfare, including ammunition pricing, research trees, reload mechanics, and engagement profitability.

**Design Philosophy**: Based on Navy Field progression with WOS2.3's 10-tier structure and permadeath risk economics.

**Key Systems**:
1. **Shell Pricing Economy** - Tier-based ammunition costs with type multipliers
2. **Gun Research Trees** - Nation-specific progression from 4" to 20"+ calibers
3. **Reload Mechanics** - Crew skill and module tier impact on fire rate
4. **Ammunition Consumption** - Engagement duration and fire rate calculations
5. **Economic Balance** - Cost/benefit analysis for engagement profitability

---

## 1. AMMUNITION PRICING SYSTEM

### Philosophy

**Core Principle**: Higher tier ships use more expensive ammunition, creating economic pressure that balances with higher-tier loot rewards and permadeath risk.

**Design Goals**:
- Tier 1-4: Ammunition is cheap, encourages aggressive play and learning
- Tier 5-7: Ammunition becomes significant cost factor, requires tactical thinking
- Tier 8-10: Ammunition is extremely expensive, every shot must count (permadeath zones)

### Shell Base Costs by Caliber

**Formula**: Base Cost = (Caliber²) × Tier Multiplier × Type Modifier

**Tier Multipliers**:
```
Tier 1:  0.5x   (Training wheels - very cheap)
Tier 2:  1.0x   (Learning phase - affordable)
Tier 3:  1.5x   (Intermediate - noticeable cost)
Tier 4:  2.5x   (Advanced - careful shooting)
Tier 5:  4.0x   (Expert - ammunition management critical)
Tier 6:  6.0x   (High-end - expensive operations)
Tier 7:  9.0x   (Elite - serious financial commitment)
Tier 8:  14.0x  (Permadeath zone - prohibitive costs)
Tier 9:  22.0x  (Ultimate - elite players only)
Tier 10: 35.0x  (Maximum - every shot is investment)
```

**Shell Type Modifiers**:
```
HE (High Explosive):        1.0x  - Standard cost, anti-structure
AP (Armor Piercing):        1.3x  - Premium cost, anti-armor
Semi-AP/SAP:                1.5x  - Expensive, dual-purpose
Supercharge/Special:        2.0x  - Very expensive, special capabilities
Experimental/Ultimate:      3.0x  - Extremely rare and costly
```

### Complete Shell Pricing Table

**TIER 1 SHIPS** - Training Phase (Destroyers, Light Cruisers)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Notes
---------|----------|----------|----------|------------------------
3"       | 2₡      | 3₡      | 4₡       | Starter destroyers
4"       | 4₡      | 5₡      | 6₡       | Early destroyers
4.5"     | 5₡      | 7₡      | 8₡       | Fleet destroyers
4.7"     | 6₡      | 8₡      | 9₡       | British destroyers
5"       | 7₡      | 9₡      | 11₡      | US destroyers (DP capable)
5.25"    | 8₡      | 10₡     | 12₡      | British dual-purpose
```

**TIER 2 SHIPS** - Early Progression (Light Cruisers, Early Heavy Cruisers)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Notes
---------|----------|----------|----------|------------------------
6"       | 18₡     | 23₡     | 27₡      | Light cruiser standard
6.46"    | 21₡     | 27₡     | 32₡      | French light cruisers
7.64"    | 29₡     | 38₡     | 44₡      | French medium cruisers
8"       | 32₡     | 42₡     | 48₡      | Heavy cruiser standard
```

**TIER 3 SHIPS** - Intermediate (Heavy Cruisers, Early Battlecruisers)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Notes
---------|----------|----------|----------|------------------------
9.45"    | 67₡     | 87₡     | 101₡     | French super cruisers
10"      | 75₡     | 98₡     | 113₡     | Dutch cruisers
12"      | 108₡    | 140₡    | 162₡     | Early battleship/BC
12.6"    | 119₡    | 155₡    | 179₡     | Italian heavy cruisers
13"      | 127₡    | 165₡    | 191₡     | French Dunkerque
13.4"    | 134₡    | 174₡    | 201₡     | French Normandie/Lyon
```

**TIER 4 SHIPS** - Advanced (Battlecruisers, Early Battleships)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Notes
---------|----------|----------|----------|------------------------
13.5"    | 228₡    | 296₡    | 342₡     | British dreadnoughts
14"      | 245₡    | 319₡    | 368₡     | British KGV-class
14.96"   | 280₡    | 364₡    | 420₡     | French Richelieu, German Bayern
15"      | 281₡    | 365₡    | 422₡     | British Queen Elizabeth, Italian
```

**TIER 5 SHIPS** - Expert (Standard Battleships)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Supercharge | Notes
---------|----------|----------|----------|-------------|------------------------
15"      | 450₡    | 585₡    | 675₡     | 900₡       | Critical threshold tier
16"      | 512₡    | 666₡    | 768₡     | 1,024₡     | US Iowa, British G3
16.1"    | 519₡    | 675₡    | 779₡     | 1,038₡     | Japanese Nagato
16.5"    | 545₡    | 709₡    | 818₡     | 1,090₡     | German H-42
```

**TIER 6 SHIPS** - High-End (Super Battleships)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Supercharge | Notes
---------|----------|----------|----------|-------------|------------------------
16"      | 768₡    | 998₡    | 1,152₡   | 1,536₡     | Ship loss risk begins
16.5"    | 817₡    | 1,062₡  | 1,226₡   | 1,634₡     | German H-42
17"      | 867₡    | 1,127₡  | 1,301₡   | 1,734₡     | Rare caliber
18"      | 972₡    | 1,264₡  | 1,458₡   | 1,944₡     | British N3, German H-43
18.1"    | 983₡    | 1,278₡  | 1,475₡   | 1,966₡     | Japanese Yamato
```

**TIER 7 SHIPS** - Elite (Ultimate Battleships)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Ultimate   | Notes
---------|----------|----------|----------|------------|------------------------
18"      | 1,458₡  | 1,895₡  | 2,187₡   | 2,916₡     | Major investment per shot
18.1"    | 1,475₡  | 1,917₡  | 2,213₡   | 2,950₡     | Yamato premium
19"      | 1,624₡  | 2,111₡  | 2,436₡   | 3,248₡     | Experimental designs
20"      | 1,800₡  | 2,340₡  | 2,700₡   | 3,600₡     | German H-44
```

**TIER 8 SHIPS** - Permadeath Warning (Super-Heavy Battleships)
```
Caliber  | HE Cost  | AP Cost  | SAP Cost | Ultimate   | Notes
---------|----------|----------|----------|------------|------------------------
18"      | 2,268₡  | 2,948₡  | 3,402₡   | 4,536₡     | Permadeath zone begins
18.1"    | 2,293₡  | 2,981₡  | 3,440₡   | 4,586₡     | Yamato at risk
19"      | 2,527₡  | 3,285₡  | 3,791₡   | 5,054₡     | Elite operations only
20"      | 2,800₡  | 3,640₡  | 4,200₡   | 5,600₡     | H-44 prohibitive cost
20.1"    | 2,828₡  | 3,676₡  | 4,242₡   | 5,656₡     | Japanese super-Yamato
```

**TIER 9 SHIPS** - Ultimate Risk (Super-Yamato class)
```
Caliber  | HE Cost  | AP Cost  | Ultimate   | Notes
---------|----------|----------|------------|------------------------
18.1"    | 3,606₡  | 4,688₡  | 7,212₡     | Every engagement is gamble
19"      | 3,974₡  | 5,166₡  | 7,948₡     | Extreme financial commitment
20"      | 4,400₡  | 5,720₡  | 8,800₡     | H-44 at extreme tier
20.1"    | 4,444₡  | 5,777₡  | 8,888₡     | Super-Yamato ultimate
21"      | 4,851₡  | 6,306₡  | 9,702₡     | Theoretical maximum
```

**TIER 10 SHIPS** - Full Permadeath (Ultimate Vessels)
```
Caliber  | HE Cost  | AP Cost  | Ultimate   | Notes
---------|----------|----------|------------|------------------------
20"      | 7,000₡  | 9,100₡  | 14,000₡    | Death = total loss
20.1"    | 7,070₡  | 9,191₡  | 14,140₡    | Yamato successor
21"      | 7,717₡  | 10,032₡ | 15,434₡    | Theoretical designs
22"      | 8,470₡  | 11,011₡ | 16,940₡    | Maximum possible caliber
```

### Economic Impact Examples

**Tier 1 Destroyer Engagement** (4.5" guns, 6 barrels)
- 100 rounds fired (average 8-minute battle)
- Cost: 100 rounds × 5₡ HE = 500₡
- Typical loot: 3,000-8,000₡ cargo + modules
- **Profit Margin**: 6-16x return, very profitable

**Tier 5 Battleship Engagement** (15" guns, 8 barrels)
- 64 rounds fired (8 salvos in 16-minute battle)
- Cost: 32 HE (14,400₡) + 32 AP (18,720₡) = 33,120₡
- Typical loot: 80,000-150,000₡ cargo + valuable modules
- **Profit Margin**: 2.5-4.5x return, still profitable but requires skill

**Tier 8 Yamato Engagement** (18.1" guns, 9 barrels)
- 45 rounds fired (5 salvos in 20-minute battle)
- Cost: 20 HE (45,860₡) + 25 AP (74,525₡) = 120,385₡
- Typical loot: 300,000-600,000₡ cargo + rare modules
- **Risk**: 30% ship loss chance on death = potential 50M₡+ total loss
- **Profit Margin**: 2.5-5x IF you survive, but catastrophic loss possible

**Tier 10 Super-Yamato Engagement** (20.1" guns, 9 barrels)
- 27 rounds fired (3 salvos in 15-minute battle, must be precise)
- Cost: 12 HE (84,840₡) + 15 AP (137,865₡) = 222,705₡
- Typical loot: 1,000,000₡+ cargo + ultra-rare modules
- **Risk**: 100% permadeath = ship + crew + modules GONE FOREVER
- **Profit Margin**: Only for elite players with perfect aim and tactics

---

## 2. AMMUNITION CONSUMPTION RATES

### Reload Time Mechanics

**Base Reload Formula**: Base Reload (seconds) = (Caliber in inches) × 2.5

**Crew Skill Modifiers**:
```
Level 1 Neutral Sailor:        +50% reload time (penalty)
Level 20 Gunner:               +15% reload time
Level 55 Veteran Gunner:       Base reload time (100%)
Level 95 Expert Gunner:        -15% reload time (faster)
Level 145 Master Gunner:       -25% reload time
Level 190 Chief Gunner:        -35% reload time (maximum efficiency)
```

**Loading System Modifiers**:
```
Separate Loading:              +0% (baseline for bag charges)
Semi-Fixed Ammunition:         -10% reload time (US/French)
Cased Ammunition:              -15% reload time (German)
Enhanced Mechanisms:           -20% reload time (upgrade variant)
```

**Module Tier Quality**:
```
Standard Gun Variant:          +0% reload
Enhanced Variant:              -8% reload
Superior/Ultimate Variant:     -15% reload
```

### Reload Time Examples

**3" Destroyer Gun** (Base: 7.5 seconds)
```
Crew Level        | Reload Time | RPM    | Rounds/10min
------------------|-------------|--------|-------------
Level 1 Neutral   | 11.25s     | 5.3    | 53
Level 20 Gunner   | 8.6s       | 7.0    | 70
Level 95 Expert   | 6.4s       | 9.4    | 94
Level 190 Chief   | 4.9s       | 12.2   | 122
```

**15" Battleship Gun** (Base: 37.5 seconds)
```
Crew Level        | Reload Time | Rounds/Hour | Typical Engagement
------------------|-------------|-------------|-------------------
Level 1 Neutral   | 56.3s      | 64         | 16 rounds (15min)
Level 20 Gunner   | 43.1s      | 83         | 21 rounds (15min)
Level 95 Expert   | 31.9s      | 113        | 28 rounds (15min)
Level 190 Chief   | 24.4s      | 147        | 37 rounds (15min)
```

**18.1" Yamato Gun** (Base: 45.3 seconds)
```
Crew Level        | Reload Time | Rounds/Hour | Typical Engagement
------------------|-------------|-------------|-------------------
Level 1 Neutral   | 67.9s      | 53         | 13 rounds (15min)
Level 20 Gunner   | 52.1s      | 69         | 17 rounds (15min)
Level 95 Expert   | 38.5s      | 93         | 23 rounds (15min)
Level 190 Chief   | 29.4s      | 122        | 31 rounds (15min)
```

### Engagement Duration by Ship Class

**Destroyer Engagements**: 5-12 minutes average
- **Knife Fight** (< 5km): 3-5 minutes, 30-60 rounds
- **Standard Engagement** (5-12km): 8-10 minutes, 80-120 rounds
- **Long Range** (12-18km): 12-15 minutes, 100-150 rounds

**Light Cruiser Engagements**: 8-15 minutes average
- **Close Range** (< 10km): 5-8 minutes, 60-100 rounds
- **Standard** (10-18km): 10-12 minutes, 100-140 rounds
- **Long Range** (18-25km): 15-20 minutes, 120-180 rounds

**Heavy Cruiser Engagements**: 10-20 minutes average
- **Close Range** (< 12km): 8-12 minutes, 50-80 rounds
- **Standard** (12-20km): 12-18 minutes, 70-120 rounds
- **Long Range** (20-28km): 20-30 minutes, 100-160 rounds

**Battleship Engagements**: 15-30 minutes average
- **Brawl** (< 10km): 10-15 minutes, 40-70 rounds (devastating)
- **Standard** (15-22km): 15-20 minutes, 50-90 rounds
- **Long Range** (22-30km): 25-40 minutes, 60-120 rounds
- **Extreme Range** (> 30km): 40-60 minutes, 80-150 rounds (rare)

### Ammunition Consumption Calculation

**Formula**: Rounds Fired = (Engagement Duration in seconds) / (Reload Time) × (Barrel Count) × (Firing Intensity)

**Firing Intensity Factors**:
```
Conservative (sniping):        0.4x  (40% time spent firing)
Standard (balanced):           0.6x  (60% time spent firing)
Aggressive (sustained fire):   0.8x  (80% time spent firing)
Desperate (maximum rate):      1.0x  (100% sustained fire)
```

**Example**: Tier 5 Iowa-class Battleship
- **Guns**: 9×16" guns (3 triple turrets)
- **Crew**: Level 95 Expert Gunners
- **Reload**: 40s base → 34s with expert crew
- **Engagement**: 18 minutes (1,080 seconds) at standard intensity

Calculation:
- Rounds per barrel = (1,080s / 34s) × 0.6 = 19 rounds
- Total rounds = 19 × 9 barrels = 171 rounds
- Shell mix: 60% AP, 40% HE
- Cost: (103 AP × 666₡) + (68 HE × 512₡) = 68,598₡ + 34,816₡ = **103,414₡**

---

## 3. GUN RESEARCH TREES

### Research Tree Philosophy

**Progression Model**: Based on Navy Field's linear unlocking system, adapted for 10-tier structure

**Nation-Specific Trees**: Each major naval power has unique gun development paths
- **British**: Emphasis on 15" and heavy guns
- **American**: Balanced progression, strong 16" focus
- **Japanese**: Maximum caliber emphasis (18.1"+)
- **German**: Innovation in 15"-20" super-heavy guns
- **French**: Unique calibers (13.4", 14.96", 15")
- **Italian**: Fast-firing 15" guns
- **Soviet**: Limited but powerful 16" development

### Research Progression Structure

**Unlock Mechanism**:
1. **Experience Requirements**: Ship must earn XP in tier-appropriate ships
2. **Credit Cost**: Research unlock fee (separate from module purchase)
3. **Prerequisites**: Previous caliber must be researched
4. **Nation Reputation**: Some advanced guns require faction standing

**Research Costs Formula**: Base Cost = (Caliber³ × 100) × Tier Modifier

### BRITISH GUN RESEARCH TREE

**Tier 1: Destroyer Guns**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
3" QF 12-Pdr Mk I     | 0 (starter) | 0₡           | 200₡       | Free starter gun
4" QF Mk V            | 2,000       | 6,400₡       | 800₡       | WWI destroyer
4.5" QF Mk I-IV       | 5,000       | 9,113₡       | 1,400₡     | Fleet destroyer
4.7" QF Mk IX/XII     | 8,000       | 10,382₡      | 1,800₡     | Tribal-class
5.25" QF Mk I         | 12,000      | 14,469₡      | 2,500₡     | Best DP gun (unlock Tier 2)
```

**Tier 2: Light Cruiser Guns**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
6" Mk VII/VIII        | 18,000      | 21,600₡      | 4,200₡     | Town-class
6" Mk XII             | 25,000      | 21,600₡      | 5,800₡     | Improved pattern
6" Mk XXIII           | 32,000      | 21,600₡      | 7,500₡     | Southampton/Colony (best 6")
8" Mk VIII            | 45,000      | 51,200₡      | 12,000₡    | County-class heavy (unlock Tier 3)
```

**Tier 3: Heavy Cruiser & Early Battleship**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
12" Mk X (2crh)       | 60,000      | 172,800₡     | 35,000₡    | HMS Dreadnought
12" Mk X (4crh)       | 75,000      | 172,800₡     | 42,000₡    | Improved ballistics
13.5" Mk V Heavy      | 95,000      | 245,925₡     | 65,000₡    | Iron Duke, KGV (1911)
13.5" Mk V Light      | 95,000      | 245,925₡     | 68,000₡    | Orion-class (unlock Tier 4)
```

**Tier 4: Standard Battleships**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
14" Mk VII (1940)     | 120,000     | 343,000₡     | 95,000₡    | King George V
14" Mk VII* Enhanced  | 140,000     | 343,000₡     | 115,000₡   | Improved variant
15" Mk I (4crh)       | 165,000     | 421,875₡     | 145,000₡   | Queen Elizabeth
15" Mk I N Rifled     | 185,000     | 421,875₡     | 165,000₡   | 1930s modernization (unlock Tier 5)
```

**Tier 5: Super Dreadnoughts**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
15" Mk XIIa APC       | 210,000     | 421,875₡     | 220,000₡   | Best British gun
15" Mk XIIa Supercharge| 240,000    | 843,750₡     | 280,000₡   | Extended range
16" Mk I AP           | 280,000     | 512,000₡     | 350,000₡   | N3 cancelled (unlock Tier 6)
```

**Tier 6-7: Cancelled Super-Battleships**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
16" Mk II G3          | 320,000     | 512,000₡     | 480,000₡   | G3 battlecruiser
16" Mk II G3 Advanced | 360,000     | 1,024,000₡   | 620,000₡   | Enhanced variant
18" Mk I N3           | 450,000     | 729,000₡     | 850,000₡   | N3 super-battleship
18" Mk I N3 Enhanced  | 520,000     | 1,458,000₡   | 1,100,000₡ | Improved propellant
18" Mk I N3 Ultimate  | 600,000     | 2,187,000₡   | 1,500,000₡ | Ultimate British (max)
```

### AMERICAN GUN RESEARCH TREE

**Tier 1-2: Destroyer & Light Cruiser**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
5"/38 Mk 12 DP        | 12,000      | 12,500₡      | 2,800₡     | Fletcher-class standard
5"/54 Mk 16 DP        | 20,000      | 12,500₡      | 4,500₡     | Post-war improvement
6"/47 Mk 16           | 35,000      | 21,600₡      | 8,500₡     | Brooklyn/Cleveland-class
8"/55 Mk 9            | 55,000      | 51,200₡      | 18,000₡    | Baltimore-class (unlock Tier 3)
```

**Tier 3-4: Heavy Cruiser & Battlecruiser**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
12"/50 Mk 8           | 80,000      | 172,800₡     | 55,000₡    | Alaska-class BC
14"/50 Mk 11          | 110,000     | 343,000₡     | 110,000₡   | New Mexico-class
14"/50 Mk 12          | 135,000     | 343,000₡     | 135,000₡   | Pennsylvania (unlock Tier 4)
```

**Tier 5-7: Standard & Fast Battleships**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
16"/45 Mk 5           | 180,000     | 512,000₡     | 240,000₡   | Colorado-class
16"/45 Mk 6           | 220,000     | 512,000₡     | 310,000₡   | North Carolina
16"/50 Mk 7           | 280,000     | 512,000₡     | 420,000₡   | Iowa-class standard
16"/50 Mk 7 Improved  | 340,000     | 1,024,000₡   | 580,000₡   | Enhanced variant
18"/48 Mk 1 (Montana) | 450,000     | 729,000₡     | 950,000₡   | Cancelled Montana-class (max)
```

### JAPANESE GUN RESEARCH TREE

**Tier 1-2: Destroyer & Light Cruiser**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
5"/50 Type 3          | 12,000      | 12,500₡      | 2,500₡     | Fubuki-class
5.5"/50 Type 41       | 22,000      | 16,638₡      | 6,200₡     | Nagara-class
6.1"/50 3rd Year Type | 38,000      | 22,698₡      | 11,000₡    | Mogami initial
8"/50 Type 3          | 58,000      | 51,200₡      | 22,000₡    | Mogami refit (unlock Tier 3)
```

**Tier 3-4: Heavy Cruiser & Battlecruiser**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
12"/45 Type 3         | 85,000      | 172,800₡     | 60,000₡    | Kongo early
14"/45 Type 41        | 125,000     | 343,000₡     | 125,000₡   | Fuso/Ise-class (unlock Tier 4)
```

**Tier 5-7: Fast Battleships**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
16.1"/45 Type 41      | 200,000     | 519,000₡     | 280,000₡   | Nagato-class
16.1"/45 Type 88      | 260,000     | 519,000₡     | 380,000₡   | Tosa cancelled
16.1"/45 Improved     | 320,000     | 1,038,000₡   | 520,000₡   | Enhanced variant (unlock Tier 6)
```

**Tier 6-10: Super Battleships (Maximum Caliber Focus)**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
18.1"/45 Type 94      | 420,000     | 983,000₡     | 850,000₡   | Yamato standard
18.1"/45 Type 94 Kai  | 520,000     | 1,966,000₡   | 1,200,000₡ | Enhanced Yamato
18.1"/50 Type 98      | 650,000     | 1,966,000₡   | 1,650,000₡ | Super Yamato planned
20.1"/50 Type 100     | 800,000     | 2,828,000₡   | 2,400,000₡ | A-150 design (theoretical max)
```

### GERMAN GUN RESEARCH TREE

**Tier 3-4: WWI Battleships**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
14.96"/45 SK L/45     | 130,000     | 373,248₡     | 130,000₡   | Bayern-class
14.96"/45 Improved    | 155,000     | 746,496₡     | 175,000₡   | Enhanced propellant
15"/47 SK C/34        | 190,000     | 421,875₡     | 240,000₡   | Bismarck standard
15"/47 SK C/34 Mod    | 230,000     | 843,750₡     | 320,000₡   | Enhanced steel (unlock Tier 5)
```

**Tier 5-7: H-Class Designs**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
16"/52 SK C/34        | 290,000     | 512,000₡     | 450,000₡   | H-class standard
16"/52 Adolf Shell    | 350,000     | 1,024,000₡   | 620,000₡   | Light shell long range
16.5"/50 SK C/40      | 420,000     | 545,000₡     | 780,000₡   | H-42 design (unlock Tier 7)
```

**Tier 7-10: Super-Heavy Designs**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
16.5"/50 Enhanced     | 500,000     | 1,090,000₡   | 1,050,000₡ | Advanced steel
18"/48 SK C/42        | 620,000     | 729,000₡     | 1,400,000₡ | H-43 design
18"/48 SK C/42 Improved| 740,000    | 1,458,000₡   | 1,850,000₡ | Enhanced variant
20"/50 SK C/44        | 900,000     | 1,000,000₡   | 2,600,000₡ | H-44 ultimate
20"/50 SK C/44 Advanced| 1,100,000  | 2,000,000₡   | 3,500,000₡ | Experimental (theoretical max)
```

### FRENCH GUN RESEARCH TREE

**Tier 3: Unique French Calibers**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
13"/50 Mle 1931       | 100,000     | 274,625₡     | 85,000₡    | Dunkerque quad
13.4"/52 Mle 1912     | 120,000     | 301,465₡     | 105,000₡   | Normandie original
13.4"/52 Enhanced     | 145,000     | 602,930₡     | 140,000₡   | Improved metallurgy
14.96"/50 Mle 1936    | 175,000     | 418,508₡     | 185,000₡   | Richelieu quad (unlock Tier 4)
```

**Tier 4-5: Fast Battleships**
```
Gun                    | Research XP | Research Cost | Module Cost | Notes
-----------------------|-------------|---------------|-------------|------------------
14.96"/50 Improved    | 215,000     | 837,016₡     | 260,000₡   | Enhanced accuracy
15"/50 Mle 1940       | 270,000     | 421,875₡     | 380,000₡   | Alsace design (planned French max)
```

---

## 4. MODULE UPGRADE SYSTEM

### Turret Module Categories

**Turret Base** - The physical mounting system (purchased separately)
- CFG-XXX designation (Caliber-Function-Nation)
- Single, Twin, Triple, Quad configurations
- Fixed cost regardless of gun variant

**Gun Variant** - The barrel upgrade (this document's focus)
- Determines performance (reload, accuracy, barrel life, velocity)
- Multiple variants per caliber (Standard, Enhanced, Superior, Ultimate)
- Higher tier variants cost more but provide bonuses

**Fire Control Module** - Targeting system (separate research tree)
- Affects accuracy, range calculation, dispersion
- Tiers 1-10 available
- Synergizes with gun tier for maximum effectiveness

### Module Synergy Bonuses

**Perfect Synergy** (All T5 modules on T5 ship)
```
+15% accuracy
+10% reload speed
+20% crew experience gain
-10% ammunition consumption (better efficiency)
```

**Mixed Tiers** (T5 guns, T3 fire control, T5 ship)
```
+5% accuracy (reduced bonus)
+10% reload speed (gun bonus only)
-5% ammunition consumption
```

**Upgrade Path Economics**

Example: Player progressing Iowa-class (Tier 5 ship)

**Stage 1** - Basic fit
- Turret: CFG-16T-US (Base cost: 45,000₡)
- Gun: 16"/50 Mk 7 Standard (Research: 280,000 XP, Module: 420,000₡)
- Fire Control: Mk 38 Basic (Module: 85,000₡)
- **Total Investment**: 550,000₡ + 280,000 XP

**Stage 2** - Mid-upgrade
- Same turrets (no additional cost)
- Gun: 16"/50 Mk 7 Improved (Research: 340,000 XP, Module: 580,000₡)
- Fire Control: Mk 38 Advanced (Module: 145,000₡)
- **Upgrade Cost**: 580,000₡ + 60,000 XP (incremental)

**Stage 3** - Maximum performance
- Same turrets
- Gun: Keep Mk 7 Improved (already best for 16"/50)
- Fire Control: Mk 38 Radar (Module: 280,000₡)
- **Upgrade Cost**: 280,000₡

**Total Progression Cost**: 1,410,000₡ + 340,000 XP

---

## 5. ECONOMIC BALANCE VALIDATION

### Engagement Profitability Analysis

**Tier 1 Destroyer** (Average case)
- **Ammunition Cost**: 500-1,200₡ per engagement
- **Repair Cost**: 200-800₡ (minimal)
- **Average Loot**: 5,000-12,000₡
- **Net Profit**: 3,800-10,500₡ (very safe)
- **Death Risk**: 0% ship loss
- **Conclusion**: Highly profitable, encourages aggressive play

**Tier 5 Battleship** (Average case)
- **Ammunition Cost**: 30,000-100,000₡ per engagement
- **Repair Cost**: 5,000-25,000₡
- **Average Loot**: 80,000-200,000₡
- **Net Profit**: 45,000-165,000₡
- **Death Risk**: 30% crew casualties possible
- **Conclusion**: Profitable but requires tactical thinking

**Tier 8 Yamato** (High-risk scenario)
- **Ammunition Cost**: 120,000-250,000₡ per engagement
- **Repair Cost**: 40,000-120,000₡
- **Average Loot**: 300,000-800,000₡
- **Net Profit**: 140,000-640,000₡ IF successful
- **Death Risk**: 30% ship loss (50M₡+ total loss)
- **Expected Value**: (0.7 × 400,000₡) - (0.3 × 50,000,000₡) = -14,720,000₡
- **Conclusion**: Only for elite players who can win 95%+ of engagements

**Tier 10 Super-Yamato** (Full permadeath)
- **Ammunition Cost**: 220,000-500,000₡ per engagement
- **Repair Cost**: 100,000-300,000₡
- **Average Loot**: 1,000,000-3,000,000₡
- **Net Profit**: 680,000-2,680,000₡ IF successful
- **Death Risk**: 100% FULL PERMADEATH (ship + crew + modules = 100M₡+)
- **Expected Value**: Even 90% win rate = negative EV
- **Conclusion**: For prestige and ultimate challenge only, not economically rational

### Break-Even Analysis

**Minimum Loot Requirements to Profit**:

```
Tier | Ammo Cost | Repair | Min Loot | Avg Engagement | Loot Multiple
-----|-----------|--------|----------|----------------|---------------
T1   | 800₡     | 400₡  | 1,200₡  | 5,000₡        | 4.2x
T2   | 3,500₡   | 1,800₡| 5,300₡  | 15,000₡       | 2.8x
T3   | 15,000₡  | 6,000₡| 21,000₡ | 45,000₡       | 2.1x
T4   | 35,000₡  | 12,000₡| 47,000₡| 95,000₡       | 2.0x
T5   | 65,000₡  | 20,000₡| 85,000₡| 150,000₡      | 1.8x
T6   | 130,000₡ | 45,000₡| 175,000₡| 320,000₡     | 1.8x
T7   | 280,000₡ | 90,000₡| 370,000₡| 650,000₡     | 1.8x
T8   | 550,000₡ | 180,000₡| 730,000₡| 1,200,000₡  | 1.6x
T9   | 1,100,000₡| 380,000₡| 1,480,000₡| 2,400,000₡| 1.6x
T10  | 2,200,000₡| 800,000₡| 3,000,000₡| 5,000,000₡| 1.7x
```

**Risk-Adjusted Returns**:

When factoring in death penalties and ship loss risk:

```
Tier | Profit/Engagement | Death Risk | Expected Loss | Risk-Adj Profit
-----|-------------------|------------|---------------|----------------
T1   | 3,800₡           | 0%        | 0₡           | 3,800₡
T2   | 9,700₡           | 0%        | 0₡           | 9,700₡
T3   | 24,000₡          | 0%        | 0₡           | 24,000₡
T4   | 48,000₡          | 5%        | 2,350₡      | 45,650₡
T5   | 65,000₡          | 10%       | 6,500₡      | 58,500₡
T6   | 145,000₡         | 30%       | 960,000₡    | -815,000₡ *
T7   | 280,000₡         | 30%       | 2,100,000₡  | -1,820,000₡ *
T8   | 470,000₡         | 30%       | 15,000,000₡ | -14,530,000₡ *
T9   | 920,000₡         | 60%       | 55,200,000₡ | -54,280,000₡ *
T10  | 2,000,000₡       | 100%      | 100,000,000₡| -98,000,000₡ *
```

\* Risk-adjusted profit becomes negative at T6+ unless win rate exceeds 95%

### Win Rate Requirements for Profitability

**Formula**: Required Win % = Ship Value / (Ship Value + Average Profit)

```
Tier | Ship Value   | Avg Profit/Win | Required Win % | Skill Level
-----|--------------|----------------|----------------|-------------
T1   | 5,000₡      | 3,800₡        | 10%           | Beginner
T2   | 25,000₡     | 9,700₡        | 28%           | Novice
T3   | 150,000₡    | 24,000₡       | 50%           | Intermediate
T4   | 800,000₡    | 48,000₡       | 70%           | Advanced
T5   | 3,500,000₡  | 65,000₡       | 82%           | Expert
T6   | 12,000,000₡ | 145,000₡      | 89%           | Elite (ship loss risk)
T7   | 28,000,000₡ | 280,000₡      | 92%           | Master
T8   | 50,000,000₡ | 470,000₡      | 95%           | Grandmaster
T9   | 92,000,000₡ | 920,000₡      | 97%           | Legend
T10  | 150,000,000₡| 2,000,000₡    | 99%+          | Ultimate (permadeath)
```

---

## 6. IMPLEMENTATION RECOMMENDATIONS

### Phase 1: Core Systems (Month 1)
1. Implement ammunition pricing table in game database
2. Add shell type selection UI (HE/AP/SAP/Special)
3. Create reload time calculations with crew skill integration
4. Build ammunition consumption tracking per engagement

### Phase 2: Research Trees (Month 2)
1. Implement gun research progression for all 7 nations
2. Add research XP tracking system
3. Create module upgrade interface
4. Build tier prerequisite validation

### Phase 3: Economic Balance (Month 3)
1. Implement loot scaling system based on ship tier
2. Add break-even calculation feedback to players
3. Create engagement profitability statistics
4. Build risk-adjusted return displays

### Phase 4: Advanced Features (Month 4)
1. Module synergy bonus calculations
2. Fire control integration
3. Advanced ammunition types (supercharge, experimental)
4. Economic analysis tools for players

### Testing & Balancing

**Key Metrics to Monitor**:
- Average engagement cost by tier
- Player profit margins by tier
- Win rates required for profitability
- Ammunition consumption rates
- Research progression speed
- Player retention at each tier threshold

**Balance Adjustment Triggers**:
- If T5 profit margins drop below 1.5x → reduce ammunition costs 15%
- If T8+ engagement rate drops below 10% of player base → reduce permadeath penalties
- If research progression stalls at any tier → reduce XP requirements 20%
- If ammunition costs prevent PvP engagement → introduce subsidy/insurance systems

---

## CONCLUSION

This ammunition and gun research system provides:

✅ **Clear Economic Pressure**: Higher tiers have exponentially higher costs, creating meaningful risk/reward decisions

✅ **Crew Skill Integration**: Ties directly into existing crew classification system, making crew investment valuable

✅ **Nation-Specific Flavor**: Each nation has unique research paths reflecting historical development

✅ **Permadeath Deterrent**: T8-T10 ammunition costs are so prohibitive they naturally discourage reckless play in permadeath zones

✅ **Profitable Lower Tiers**: T1-T5 remain highly profitable, encouraging new players and providing safe progression

✅ **Elite Player Challenge**: T6+ requires 90%+ win rates to be economically viable, creating prestige gameplay

**Next Steps**:
1. Review with game economy team
2. Integrate with existing crew system documentation
3. Build database tables and UI mockups
4. Begin Phase 1 implementation
