# US Navy Ship Research Tree - Diagram Completeness Report

**Generated:** October 23, 2025
**Analysis:** Comparison of research tree diagrams vs actual ship class files

## Executive Summary

| Category | Overview Lists | Files Exist | Match % | Status |
|----------|----------------|-------------|---------|---------|
| Battleships | 25 classes | 13 files | 52% | ⚠️ **12 missing** |
| Carriers | 16 classes | 16 files | 100% | ✅ **Complete** |
| Cruisers | 49 classes | 49 files | 100% | ✅ **Complete** |
| Destroyers | 32 classes | 32 files | 100% | ✅ **Complete** |
| Submarines | 62 classes | 61 files | 98% | ⚠️ **1 mismatch** |
| Transports | 50+ classes | 9 files | ~18% | ⚠️ **40+ missing** |

**Overall:** 180 files documented | 233+ classes referenced | ~77% coverage

---

## Category Analysis

### 1. Battleships (USA Battleships/) ⚠️

**Status:** 12 classes missing from filesystem

**Files Present (13):**
1. ✅ Alaska-Class
2. ✅ Colorado-Class
3. ✅ Connecticut-Class
4. ✅ Indiana-Class-BB
5. ✅ Iowa-Class
6. ✅ Lexington-Class-Battlecruiser
7. ✅ Montana-Class
8. ✅ Nevada-Class
9. ✅ North Carolina-Class
10. ✅ South Carolina-Class
11. ✅ South Dakota-Class-1920
12. ✅ South Dakota-Class-BB
13. ✅ Tillman-Maximum-Battleships

**Missing from Filesystem (12):**
- ❌ Iowa-Class-BB-4 (BB-4, 1897)
- ❌ Kearsarge-Class (BB-5/6, 1900)
- ❌ Illinois-Class (BB-7/8, 1901)
- ❌ Maine-Class-BB (BB-10, 1902)
- ❌ Virginia-Class-BB (BB-13 to BB-17, 1906)
- ❌ Delaware-Class (BB-28/29, 1910)
- ❌ Florida-Class (BB-30/31, 1911)
- ❌ Wyoming-Class (BB-32/33, 1912)
- ❌ New York-Class-BB (BB-34/35, 1914)
- ❌ Pennsylvania-Class (BB-38/39, 1916)
- ❌ New Mexico-Class (BB-40/41/42, 1918)
- ❌ Tennessee-Class-BB (BB-43/44, 1920)

**Impact:** Missing 12 of 25 battleship classes (48% incomplete)
- All pre-dreadnought classes except Indiana and Connecticut
- Several important dreadnought classes (Wyoming, Pennsylvania, etc.)
- Some super-dreadnought classes (New Mexico, Tennessee)

---

### 2. Carriers (USA Carriers/) ✅

**Status:** Complete match!

**Files Present (16):**
1. ✅ CVV-Medium-Carrier (cancelled)
2. ✅ Enterprise-Class-CVN
3. ✅ Essex-Class
4. ✅ Forrestal-Class
5. ✅ Gerald R. Ford-Class
6. ✅ Independence-Class
7. ✅ Kitty Hawk-Class
8. ✅ Langley-Class
9. ✅ Lexington-Class-CV
10. ✅ Midway-Class
11. ✅ Nimitz-Class
12. ✅ Ranger-Class
13. ✅ Sea-Control-Ship-SCS (cancelled)
14. ✅ United States-Class-CVA-58 (cancelled)
15. ✅ Wasp-Class-CV
16. ✅ Yorktown-Class-CV

**Analysis:** Perfect alignment between overview and filesystem. All 16 classes (including 3 cancelled designs) are documented.

---

### 3. Cruisers (USA Cruisers/) ✅

**Status:** Complete match!

**Files Present (49):**
All 49 classes referenced in overview diagram have corresponding files. Includes:
- Protected cruisers (1883-1906): 14 classes
- Armored cruisers (1893-1906): 6 classes
- Treaty cruisers (1923-1939): 9 classes
- WWII cruisers (1941-1948): 11 classes
- Missile cruiser conversions (1955-1962): 4 classes
- Guided missile cruisers (1961-1983): 9 classes
- 2 cancelled designs (Typhon-DLGN-Frigate, Strike-Cruiser-CSGN)

**Analysis:** Comprehensive documentation. Complete historical coverage from first steel cruisers (1883) to modern Aegis cruisers (1983).

---

### 4. Destroyers (USA Destroyers/) ✅

**Status:** Complete match!

**Files Present (32):**
All 32 destroyer classes from overview are documented, spanning 1902-2013:
- Early destroyers (1902-1918): 12 classes including flush-deckers
- Interwar destroyers (1934-1940): 10 classes
- WWII destroyers (1942-1945): 3 legendary classes (Fletcher, Sumner, Gearing)
- Cold War destroyers (1954-1975): 5 classes
- Modern destroyers (1991-2013): 2 classes (Arleigh Burke, Zumwalt)

**Analysis:** Complete progression from Bainbridge (1902) through Zumwalt (2013). All major design innovations documented.

---

### 5. Submarines (USA Submarines/) ⚠️

**Status:** Near-complete (1 potential mismatch)

**Files Present (61):**
61 submarine files documented, covering:
- Early submarines (1900-1918): Holland through S-Class
- Interwar submarines (1924-1941): 11 classes
- WWII fleet submarines (1941-1945): Gato, Balao, Tench
- Post-WWII diesel (1946-1959): Tang, Barbel
- Nuclear attack submarines (1954-present): 8 SSN classes
- Ballistic missile submarines (1959-present): 6 SSBN classes
- Experimental submarines: 5 classes (Albacore, X-1, Dolphin, Triton, NR-1)

**Potential Issue:**
- Overview mentions **62 classes**
- Filesystem has **61 files**
- Need to identify which class is missing or if there's a naming discrepancy

**Analysis:** 98% complete. Nearly comprehensive coverage from Holland (1900) to Columbia SSBN (2020s).

---

### 6. Transports Amphibious (USA Transports Amphibious/) ⚠️

**Status:** Severely incomplete

**Files Present (9):**
1. ✅ America-Class-LHA
2. ✅ Ashland-Class-LSD
3. ✅ Charles Lawrence-Class
4. ✅ Haskell-Class
5. ✅ Iwo Jima-Class-LPH
6. ✅ LST-1-Class
7. ✅ San Antonio-Class
8. ✅ Tarawa-Class
9. ✅ Wasp-Class

**Missing:** 40+ classes referenced in overview diagram

**Impact:** Only 18% coverage. Missing most:
- WWII transport classes (AP, APA, AKA series)
- Landing Ship Tank classes (LST variants)
- Landing Ship Medium classes (LSM)
- Landing Craft Infantry classes (LCI)
- Cargo ships (AK, AKA series)
- Dock landing ships (LSD variants)
- Amphibious cargo ships (LKA)

**Analysis:** Critical gap in documentation. Most WWII-era transport and amphibious warfare ships are undocumented.

---

## Recommendations

### Priority 1: Battleships (12 files needed)
Create documentation for missing pre-dreadnought, dreadnought, and super-dreadnought classes. These are historically significant and should be prioritized.

### Priority 2: Transports Amphibious (40+ files needed)
Major gap in documentation. WWII transport and amphibious warfare ships are critical to understanding US naval power projection.

### Priority 3: Submarines (1 file investigation)
Identify the one missing/misnamed submarine class. Should be quick to resolve.

### Priority 4: Verify Completeness
Cross-reference all WikiLinks in overview files against filesystem to ensure no other discrepancies.

---

## Standardization Tasks (Separate from Completeness)

After diagram verification is complete, proceed with YAML standardization:

1. **Displacement Fields:** Change `displacement_normal` → `displacement_standard` (79 files)
2. **Propulsion Power Fields:**
   - Change `propulsion_ihp` → `propulsion_shp` (3 files)
   - Change `propulsion_hp` → `propulsion_shp` (37 files)

**Total files to modify:** 119 files

---

**Report End** | Generated by Claude Code SuperClaude Framework
