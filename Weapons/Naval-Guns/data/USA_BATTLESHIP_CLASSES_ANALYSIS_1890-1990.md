# USA Battleship Classes Analysis: 1890-1990
## Game Design Selection & Evolutionary Tree

**Date**: October 10, 2025
**Purpose**: Identify which battleship classes have meaningful game design differences and map their evolutionary connections for research tree implementation

---

## 📋 Complete USA Battleship Class List (1890-1945)

### Pre-Dreadnought Era (1890-1910)

| Class | Ships | Commissioned | Main Guns | Displacement | Speed | Key Features |
|-------|-------|--------------|-----------|--------------|-------|--------------|
| **Texas** | 1 | 1892 | 2×12"/35 | 6,315t | 17.8 kts | Second-class BB, obsolete design |
| **Indiana** | 3 | 1895-1896 | 4×13"/35 | 10,288t | 15 kts | First true US BBs, low freeboard |
| **Kearsarge** | 2 | 1900 | 4×13"/35 + 8"/35 superimposed | 11,540t | 16 kts | Failed superimposed turret experiment |
| **Illinois** | 3 | 1900-1901 | 4×13"/35 | 11,565t | 17 kts | Improved Indiana design |
| **Maine** | 3 | 1902-1904 | 4×12"/40 | 12,846t | 18 kts | Return to 12" guns, better range |
| **Virginia** | 5 | 1906 | 4×12"/40 + 8×8"/45 | 14,948t | 19 kts | Mixed armament |
| **Connecticut** | 6 | 1906-1908 | 4×12"/45 + 8×8"/45 | 16,000t | 18 kts | Largest pre-dreadnought class |
| **Mississippi** | 2 | 1908 | 4×12"/45 + 8×8"/45 | 13,000t | 17 kts | Built for Greece, repurchased |

### Dreadnought Era (1910-1920)

| Class | Ships | Commissioned | Main Guns | Displacement | Speed | Key Features |
|-------|-------|--------------|-----------|--------------|-------|--------------|
| **South Carolina** | 2 | 1910 | 8×12"/45 (4 twin) | 16,000t | 18.5 kts | **First US dreadnoughts**, all centerline |
| **Delaware** | 2 | 1910 | 10×12"/45 (5 twin) | 20,380t | 21 kts | More guns, higher speed |
| **Florida** | 2 | 1911 | 10×12"/45 (5 twin) | 21,825t | 21 kts | Similar to Delaware |
| **Wyoming** | 2 | 1912 | 12×12"/50 (6 twin) | 26,000t | 20.5 kts | **Most 12" guns ever on US BB** |
| **New York** | 2 | 1914 | 10×14"/45 (5 twin) | 27,000t | 21 kts | **First 14" guns**, revolutionary jump |

### Standard-Type Era (1916-1923)

| Class | Ships | Commissioned | Main Guns | Displacement | Speed | Key Features |
|-------|-------|--------------|-----------|--------------|-------|--------------|
| **Nevada** | 2 | 1916 | 10×14"/45 (2 triple, 2 twin) | 27,500t | 21 kts | **First Standard-type**, all-or-nothing armor |
| **Pennsylvania** | 2 | 1916 | 12×14"/45 (4 triple) | 31,400t | 21 kts | More guns, all triple turrets |
| **New Mexico** | 3 | 1918-1919 | 12×14"/50 (4 triple) | 32,000t | 21 kts | Improved guns, turbo-electric drive |
| **Tennessee** | 2 | 1920-1921 | 12×14"/50 (4 triple) | 32,300t | 21 kts | Similar to New Mexico |
| **Colorado** | 3 | 1921-1923 | 8×16"/45 (4 twin) | 32,600t | 21 kts | **First 16" guns**, fewer but bigger |

### Fast Battleship Era (1941-1944)

| Class | Ships | Commissioned | Main Guns | Displacement | Speed | Key Features |
|-------|-------|--------------|-----------|--------------|-------|--------------|
| **North Carolina** | 2 | 1941 | 9×16"/45 (3 triple) | 44,800t | 28 kts | **First fast BBs**, treaty design |
| **South Dakota** | 4 | 1942 | 9×16"/45 (3 triple) | 44,519t | 27.5 kts | Compact, best treaty BB design |
| **Iowa** | 4 | 1943-1944 | 9×16"/45 (3 triple) | 57,540t | **33 kts** | Ultimate US BBs, **reactivated 1980s** |

**Total**: 21 distinct classes, 59 battleships built

---

## 🎮 Game Design Analysis: Which Classes to Include?

### Selection Criteria

A class should be included if it has **at least one** of:
1. ✅ **Different gun caliber** (12" vs 13" vs 14" vs 16")
2. ✅ **Different gun count** (major increase/decrease)
3. ✅ **Revolutionary innovation** (dreadnought, all-or-nothing armor, fast BB)
4. ✅ **Different design philosophy** (coastal defense vs blue water vs standard-type)
5. ✅ **Significant speed change** (15-17 kts → 18-21 kts → 27-28 kts → 33 kts)
6. ✅ **Historical significance** (famous ships, major battles)
7. ✅ **Unique features** (superimposed turrets, reactivation for modern era)

### Classes to **INCLUDE** (18 selected)

#### Tier 1: Pre-Dreadnought Era (8 classes)
| Class | Why Include | Game Role |
|-------|-------------|-----------|
| **Texas** | First US BB, historical baseline | Tutorial/starting ship |
| **Indiana** ⭐ | First true BBs, design template | Core early-game BB |
| **Kearsarge** | Failed superimposed turrets, unique design | Experimental branch |
| **Illinois** | Improved Indiana, evolutionary step | Linear progression |
| **Maine** | Different gun philosophy (4×12" vs 4×13") | Alternative branch |
| **Virginia** | Mixed armament era | Transitional design |
| **Connecticut** ⭐ | Peak pre-dreadnought, largest class | Pre-dreadnought ultimate |
| **Mississippi** | Final pre-dreadnought | Bridge to dreadnought era |

#### Tier 2: Dreadnought Revolution (5 classes)
| Class | Why Include | Game Role |
|-------|-------------|-----------|
| **South Carolina** ⭐ | **Revolutionary**: First dreadnought | Game-changing unlock |
| **Delaware** | More guns (10 vs 8) | Incremental improvement |
| **Wyoming** | **Most 12" guns** (12 guns) | Firepower specialist |
| **New York** ⭐ | **Revolutionary**: First 14" guns | Major caliber jump |
| **Nevada** ⭐ | **Revolutionary**: First Standard-type | New design philosophy |

#### Tier 3: Standard-Type Mastery (3 classes)
| Class | Why Include | Game Role |
|-------|-------------|-----------|
| **Pennsylvania** | More guns (12 vs 10) | Standard-type improved |
| **New Mexico** | Better guns (14"/50 vs 14"/45) | Standard-type refined |
| **Colorado** ⭐ | **Revolutionary**: First 16" guns | Ultimate pre-treaty |

#### Tier 4: Fast Battleship Era (3 classes)
| Class | Why Include | Game Role |
|-------|-------------|-----------|
| **North Carolina** ⭐ | **Revolutionary**: First fast BB (28 kts) | New era begins |
| **South Dakota** | Best treaty design, compact | Optimized fast BB |
| **Iowa** ⭐⭐⭐ | **Ultimate US BB**: 33 kts, 1980s reactivation | End-game superweapon |

**⭐ = Major research milestone**

---

### Classes to **MERGE/EXCLUDE** (3 classes)

| Class | Reason to Exclude | Merge Into |
|-------|-------------------|------------|
| **Florida** | Too similar to Delaware (same guns, same speed) | **Delaware-class** (combine as single node) |
| **Tennessee** | Too similar to New Mexico (same guns, same specs) | **New Mexico-class** (combine as single node) |

**Result**: 18 unique research nodes representing distinct gameplay experiences

---

## 🌳 Evolutionary Research Tree Structure

### Branch Architecture

```
PRE-DREADNOUGHT ERA (1890-1908)
═════════════════════════════════

    [START: Texas 1892]
           │
           │ First true battleships
           ▼
    [Indiana-class 1895] ──────────┐
    Coastal Defense                │
    4×13"/35, 15 kts               │
           │                        │
           │                        │ PARALLEL BRANCHES
           ▼                        │
    [Kearsarge-class 1900]         │
    Experimental Turrets           │
    (Dead-end branch)              │
                                    │
                           [Maine-class 1902]
                           Alternative Design
                           4×12"/40, 18 kts
                                    │
           ┌────────────────────────┴────────────────────┐
           │                                             │
           ▼                                             ▼
    [Illinois-class 1900]                      [Virginia-class 1906]
    Improved Indiana                           Mixed Armament
    4×13"/35, 17 kts                          4×12"/40 + 8×8"/45
           │                                             │
           │                                             │
           └────────────────┬────────────────────────────┘
                            │
                            │ Both paths converge
                            ▼
                   [Connecticut-class 1906]
                   Peak Pre-Dreadnought
                   4×12"/45 + 8×8"/45, 18 kts
                            │
                            │
                            ▼
                   [Mississippi-class 1908]
                   Final Pre-Dreadnought
                   4×12"/45 + 8×8"/45


DREADNOUGHT REVOLUTION (1910-1916)
═══════════════════════════════════

    [Mississippi-class] → REQUIRED
            │
            │ ⚡ REVOLUTIONARY UNLOCK
            │
            ▼
    [South Carolina-class 1910] ⭐⭐⭐
    FIRST DREADNOUGHT
    8×12"/45 all-centerline, all-big-gun concept
            │
            │ Linear progression
            ▼
    [Delaware-class 1910]
    More Guns
    10×12"/45, 21 kts
            │
            │
            ▼
    [Wyoming-class 1912]
    Maximum 12" Firepower
    12×12"/50, 20.5 kts
            │
            │ ⚡ CALIBER REVOLUTION
            ▼
    [New York-class 1914] ⭐⭐
    FIRST 14" GUNS
    10×14"/45, 21 kts
            │
            │ ⚡ DESIGN REVOLUTION
            ▼
    [Nevada-class 1916] ⭐⭐⭐
    FIRST STANDARD-TYPE
    All-or-nothing armor
    10×14"/45, 21 kts


STANDARD-TYPE ERA (1916-1923)
══════════════════════════════

    [Nevada-class] → Foundation
            │
            │ Linear progression
            ▼
    [Pennsylvania-class 1916]
    More Firepower
    12×14"/45 (all triple turrets)
            │
            │
            ▼
    [New Mexico-class 1918]
    Refined Standard-Type
    12×14"/50, turbo-electric
            │
            │ ⚡ CALIBER REVOLUTION
            ▼
    [Colorado-class 1921] ⭐⭐
    FIRST 16" GUNS
    8×16"/45, 21 kts
            │
            │ Treaty pause (1923-1936)
            │ Washington Naval Treaty
            │
            │ ⚡ SPEED REVOLUTION
            ▼


FAST BATTLESHIP ERA (1941-1944)
════════════════════════════════

    [Colorado-class] → Required
            │
            │ 18-year gap (treaty era)
            │
            ▼
    [North Carolina-class 1941] ⭐⭐⭐
    FIRST FAST BATTLESHIP
    9×16"/45, 28 kts
    Treaty-limited design
            │
            │
            ▼
    [South Dakota-class 1942]
    Optimized Treaty Design
    9×16"/45, 27.5 kts, compact
            │
            │
            ▼
    [Iowa-class 1943] ⭐⭐⭐⭐
    ULTIMATE US BATTLESHIP
    9×16"/45, 33 kts
    Reactivated 1980s (Tomahawk missiles)
            │
            │ EXTENDS TO 1990
            │
            └─────> [END GAME]


KEARSARGE EXPERIMENTAL BRANCH (Dead-end)
═════════════════════════════════════════

    [Indiana-class] → Required
            │
            │ Alternative path
            ▼
    [Kearsarge-class 1900] 🔬
    EXPERIMENTAL DESIGN
    Superimposed turrets (13"/35 + 8"/35)

    ❌ DEAD END - Failed experiment
    Does NOT unlock further research

    Gameplay: Cheaper research, unique ability,
              but leads nowhere
```

---

## 🎯 Research Node Recommendations

### Starting Technologies (1890s)
```markdown
| Node_ID | Ship_Class | Research_Cost_RP | Notes |
|---------|------------|------------------|-------|
| 1000 | Texas | 0 | FREE starting ship |
| 1001 | Indiana-class | 5,000 | Primary starting research |
| 1002 | Maine-class | 5,000 | Alternative starting research |
```

### Revolutionary Milestones (Major Unlocks)
```markdown
| Node_ID | Ship_Class | Research_Cost_RP | Why Revolutionary |
|---------|------------|------------------|-------------------|
| 1010 | South Carolina-class | 25,000 | Dreadnought revolution |
| 1014 | New York-class | 18,000 | First 14" guns |
| 1015 | Nevada-class | 20,000 | Standard-type concept |
| 1019 | Colorado-class | 22,000 | First 16" guns |
| 1020 | North Carolina-class | 35,000 | Fast battleship revolution |
| 1023 | Iowa-class | 50,000 | Ultimate battleship |
```

### Experimental Branch (Risk/Reward)
```markdown
| Node_ID | Ship_Class | Research_Cost_RP | Special Rules |
|---------|------------|------------------|---------------|
| 1003 | Kearsarge-class | 3,000 | CHEAP but dead-end |
```
**Gameplay**: Players can research Kearsarge cheaply for early advantage, but it doesn't unlock anything further. Trade-off decision.

---

## 📊 Design Philosophy Branches

### Branch 1: Conservative Evolution Path
```
Texas → Indiana → Illinois → Connecticut → Mississippi
→ South Carolina → Delaware → Wyoming
→ Nevada → Pennsylvania → New Mexico → Colorado
→ North Carolina → South Dakota → Iowa
```
**Philosophy**: Follow mainstream USN design evolution
**Advantages**: Safe, predictable progression
**Research Cost**: ~200,000 RP total

### Branch 2: Alternative Caliber Path
```
Texas → Maine → Virginia → Connecticut → Mississippi
→ South Carolina → Delaware → Wyoming
→ Nevada → Pennsylvania → New Mexico → Colorado
→ North Carolina → South Dakota → Iowa
```
**Philosophy**: Start with 12" guns instead of 13", emphasizing range
**Advantages**: Different early-game experience, same end-game
**Research Cost**: ~200,000 RP total

### Branch 3: Experimental Risk Path
```
Texas → Indiana → Kearsarge (DEAD END)
Player must backtrack to Illinois to continue
```
**Philosophy**: Try experimental design, pay price later
**Advantages**: Cheap early research, unique ship
**Disadvantages**: Wasted RP if pursuing full tree

---

## 🔧 Game Balance Recommendations

### Research Point Costs by Era

**Pre-Dreadnought Era (1890-1908)**: 5,000-12,000 RP per class
- Texas: 0 (free)
- Indiana, Maine: 5,000
- Kearsarge: 3,000 (experimental discount)
- Illinois, Virginia: 8,000
- Connecticut: 10,000
- Mississippi: 12,000

**Dreadnought Era (1910-1916)**: 15,000-25,000 RP per class
- South Carolina: 25,000 (revolutionary)
- Delaware: 15,000
- Wyoming: 18,000
- New York: 20,000 (14" guns)
- Nevada: 22,000 (Standard-type)

**Standard-Type Era (1916-1923)**: 18,000-25,000 RP per class
- Pennsylvania: 18,000
- New Mexico: 20,000
- Colorado: 25,000 (16" guns)

**Fast Battleship Era (1941-1944)**: 30,000-50,000 RP per class
- North Carolina: 35,000 (revolutionary)
- South Dakota: 30,000
- Iowa: 50,000 (ultimate)

**Total RP to Complete Tree**: ~320,000 RP

### Build Costs & Times

**Pre-Dreadnoughts**: $3-6M, 24-48 months
**Dreadnoughts**: $6-12M, 36-60 months
**Standard-Types**: $10-15M, 48-72 months
**Fast Battleships**: $80-110M, 60-84 months

---

## 🎖️ Special Abilities & Bonuses

### Class-Based Bonuses

| Class | Special Ability | Gameplay Effect |
|-------|----------------|-----------------|
| **Texas** | Old Reliable | -20% maintenance cost |
| **Indiana** | Coastal Fortress | +20% coastal defense, -10% blue water |
| **Kearsarge** | Experimental Design | +15% firepower, -10% accuracy (blast interference) |
| **Maine** | Long Range Specialist | +15% max range |
| **Connecticut** | Fleet Flagship | +10% fleet coordination |
| **South Carolina** | All-Big-Gun | +25% penetration vs pre-dreadnoughts |
| **Wyoming** | Maximum Firepower | 12 guns = +30% fire rate |
| **New York** | 14" Advantage | +20% penetration vs 12" armor |
| **Nevada** | All-or-Nothing | +30% critical hit resistance |
| **Colorado** | 16" Monster | +25% penetration vs all targets |
| **North Carolina** | Fast Escort | +15% AA defense, +10% carrier escort bonus |
| **South Dakota** | Compact Warrior | -10% target profile |
| **Iowa** | Ultimate Warrior | All stats +10%, **1980s Tomahawk missiles** |

### Ship-Specific Bonuses

| Ship | Historical Event | Bonus |
|------|------------------|-------|
| **USS Oregon (BB-3)** | Great voyage around Cape Horn | +20% endurance, ignore 1 refit |
| **USS New York (BB-34)** | WWI Atlantic convoy duty | +15% ASW capability |
| **USS Nevada (BB-36)** | Only BB to get underway at Pearl Harbor | +25% damage control |
| **USS West Virginia (BB-48)** | Sunk and raised at Pearl Harbor | +30% torpedo defense (rebuilt) |
| **USS South Dakota (BB-57)** | Naval Battle of Guadalcanal | +20% night combat |
| **USS Missouri (BB-63)** | Japanese surrender ceremony | +10% all stats (prestige) |
| **USS New Jersey (BB-62)** | Most combat missions | +15% accuracy |
| **USS Wisconsin (BB-64)** | Rammed by USS Eaton, got new bow | +20% collision resistance |

---

## 🌐 Historical Timeline & Availability

### Era 1: New Steel Navy (1890-1908)
**Available**: Texas, Indiana, Kearsarge, Illinois, Maine, Virginia, Connecticut, Mississippi
**Context**: Spanish-American War (1898), Great White Fleet (1907)

### Era 2: Dreadnought Revolution (1910-1916)
**Available**: South Carolina, Delaware, Wyoming, New York, Nevada
**Context**: WWI (1914-1918), naval arms race

### Era 3: Standard-Type Era (1916-1923)
**Available**: Pennsylvania, New Mexico, Colorado
**Context**: WWI conclusion, Washington Naval Treaty (1922)

### Era 4: Treaty Limitations (1923-1936)
**Available**: None (construction pause)
**Context**: Washington & London Naval Treaties limit construction

### Era 5: Fast Battleship Era (1937-1945)
**Available**: North Carolina, South Dakota, Iowa
**Context**: WWII, Pacific Theater, carrier escort missions

### Era 6: Cold War Reactivation (1980-1992)
**Available**: Iowa-class ONLY (modernized)
**Context**: Reagan's 600-ship Navy, Tomahawk missiles, Persian Gulf

---

## 📈 Progression Metrics

### Combat Power Growth
```
Era 1 (1890):  100 power (Texas)
Era 1 (1900):  250 power (Indiana)
Era 2 (1910):  500 power (South Carolina - dreadnought)
Era 2 (1914):  700 power (New York - 14" guns)
Era 3 (1921):  1000 power (Colorado - 16" guns)
Era 5 (1943):  1500 power (Iowa - 33 kts)
Era 6 (1988):  2000 power (Iowa - Tomahawk missiles)
```

**Total Power Growth**: 100 → 2000 (20x increase over century)

---

## ✅ Summary: Final Class Selection

**18 Research Nodes** spanning **98 years** (1892-1990):

### Pre-Dreadnought (8 nodes)
1. Texas (1892)
2. Indiana-class (1895)
3. Kearsarge-class (1900) - Experimental branch
4. Illinois-class (1900)
5. Maine-class (1902) - Alternative branch
6. Virginia-class (1906)
7. Connecticut-class (1906)
8. Mississippi-class (1908)

### Dreadnought Era (5 nodes)
9. South Carolina-class (1910) ⚡
10. Delaware-class (1910)
11. Wyoming-class (1912)
12. New York-class (1914) ⚡
13. Nevada-class (1916) ⚡

### Standard-Type (3 nodes)
14. Pennsylvania-class (1916)
15. New Mexico-class (1918)
16. Colorado-class (1921) ⚡

### Fast Battleship (3 nodes)
17. North Carolina-class (1941) ⚡
18. Iowa-class (1943) ⚡⚡ (extends to 1992)

**⚡ = Revolutionary unlock (7 major milestones)**

---

**Status**: ✅ Analysis complete
**Ready for**: Research Tree Database population
**Total Classes**: 18 unique gameplay experiences
**Total RP Required**: ~320,000 RP
**Timeline Covered**: 1890-1990 (100 years)

**Next Step**: Populate `ship_research_tree_database.md` with these 18 classes

**Created**: October 10, 2025
