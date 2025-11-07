# Ship Research Tracking Document

**Created**: 2025-10-12
**Purpose**: Track research progress for Option C Hybrid Approach
**Target**: Add 20 critical fields to 959 ships

---

## Summary Statistics

**Total Ships**: 959 entries
**Total Unique "Classes"**: 782 entries
**Ship-to-Class Ratio**: 1.23 (most "classes" are individual ships)

**Data Structure Reality**:
- Many ships listed as their own "class" (unique builds like carriers, battlecruisers)
- True production classes have 2+ ships
- Need to identify ~50-100 TRUE classes to research, then estimate for unique ships

---

## Research Strategy

### Tier 1: High-Value Production Classes (Research First)
**Impact**: Covers 200+ ships with ~20 class researches

These are mass-production classes with many ships - maximum research efficiency:

| Priority | Class | Expected Ships | Ship Type | Era | Research Value |
|----------|-------|----------------|-----------|-----|----------------|
| 🔥 **1** | Fletcher-class | ~175 | DD | WWII | **CRITICAL** - Largest class |
| 🔥 **2** | Essex-class | ~24 | CV | WWII | **CRITICAL** - Main carrier |
| 🔥 **3** | Cleveland-class | ~27 | CL | WWII | **CRITICAL** - Production CL |
| 🔥 **4** | Baltimore-class | ~14 | CA | WWII | **HIGH** - Main heavy cruiser |
| 🔥 **5** | Iowa-class | 2-4 | BB | WWII | **HIGH** - Famous BB |
| **6** | Gearing-class | ~50 | DD | Late WWII | HIGH - Fletcher successor |
| **7** | Sumner-class | ~60 | DD | WWII | HIGH - Fletcher variant |
| **8** | Ticonderoga-class | ~27 | CG | Modern | HIGH - Aegis cruiser |
| **9** | Los Angeles-class | ~60 | SSN | Modern | HIGH - Production SSN |
| **10** | Spruance-class | ~30 | DD | Modern | MEDIUM - Modern DD |

**Estimated Coverage**: ~450 ships (47% of database) with just 10 class researches!

### Tier 2: Important Historical Classes (Research Second)
**Impact**: Covers ~150 ships with ~30 class researches

| Class | Ships | Type | Era | Notes |
|-------|-------|------|-----|-------|
| Wickes-class | ~110 | DD | WWI | Flush-deck destroyers |
| Clemson-class | ~150 | DD | WWI | Similar to Wickes |
| Pennsylvania-class | 2 | BB | WWI | 14" gun BB |
| North Carolina-class | 2 | BB | WWII | First fast BB |
| South Dakota-class | 4 | BB | WWII | Compact fast BB |
| New Orleans-class | 7 | CA | WWII | Treaty cruiser |
| Brooklyn-class | 7 | CL | WWII | 15×6" guns |
| Independence-class | 9 | CVL | WWII | Light carriers |
| Casablanca-class | 50 | CVE | WWII | Escort carriers |
| Bogue-class | 45 | CVE | WWII | Escort carriers |
| Gato-class | 77 | SS | WWII | Production submarine |
| Balao-class | 122 | SS | WWII | Improved Gato |
| Tench-class | 31 | SS | WWII | Final WWII SS |

### Tier 3: Unique/Famous Ships (Estimate from Similar)
**Impact**: ~200 ships, use estimation algorithms

These are mostly 1-of-a-kind ships or small classes (1-2 ships):
- Pre-dreadnought battleships (1890-1905)
- Dreadnought-era battleships (1906-1920)
- Unique carriers (Lexington, Saratoga, Ranger, etc.)
- Foreign ships (British, German, Japanese)
- Modern unique vessels (Zumwalt, etc.)

**Strategy**: Research 1-2 representative examples per type/era, then estimate similar ships

---

## Research Priority Matrix

### Phase 1: Top 5 CRITICAL Classes (Start Here!)
**Time**: 4-6 hours | **Coverage**: ~260 ships (27% of database)

1. **Fletcher-class DD** → Covers ~175 destroyers
2. **Essex-class CV** → Covers ~24 carriers
3. **Cleveland-class CL** → Covers ~27 light cruisers
4. **Baltimore-class CA** → Covers ~14 heavy cruisers
5. **Iowa-class BB** → Covers 4 battleships + reference for all fast BBs

### Phase 2: Destroyer Classes (Priority)
**Time**: 2-3 hours | **Coverage**: ~280 more DDs

6. Gearing-class (~50 ships)
7. Sumner-class (~60 ships)
8. Wickes-class (~110 ships)
9. Clemson-class (~150 ships - LARGEST CLASS!)
10. Benson-class (~30 ships)

### Phase 3: Carrier Classes
**Time**: 1-2 hours | **Coverage**: ~80 carriers

11. Independence-class CVL (9 ships)
12. Casablanca-class CVE (50 ships)
13. Bogue-class CVE (45 ships)
14. Midway-class CV (3 ships - reference for large carriers)

### Phase 4: Submarine Classes
**Time**: 1-2 hours | **Coverage**: ~230 submarines

15. Gato-class (77 ships)
16. Balao-class (122 ships - LARGEST SUBMARINE CLASS)
17. Tench-class (31 ships)
18. Los Angeles-class SSN (~60 ships)

### Phase 5: Remaining Major Classes
**Time**: 2-3 hours | **Coverage**: ~100 ships

19. Ticonderoga-class CG (27 Aegis cruisers)
20. Spruance-class DD (30 modern destroyers)
21. Virginia-class SSN (modern submarines)
22. Arleigh Burke-class DDG (modern destroyers)

---

## Data Collection Template

For each ship class, collect the following 20 critical fields:

### Hardpoints (8 fields)
- [ ] Hardpoint_Main_Battery (e.g., "5× 5"/38 DP single mounts")
- [ ] Hardpoint_Main_Count (e.g., 5)
- [ ] Hardpoint_Secondary_Battery (e.g., "10× 40mm Bofors quad mounts")
- [ ] Hardpoint_Secondary_Count (e.g., 10)
- [ ] Hardpoint_AA_Light (e.g., "7× 20mm Oerlikon single mounts")
- [ ] Hardpoint_AA_Light_Count (e.g., 7)
- [ ] Hardpoint_Torpedo (e.g., "10× 21" torpedo tubes, 2 quintuple mounts")
- [ ] Hardpoint_Torpedo_Count (e.g., 10)

### Module Slots (4 fields)
- [ ] Module_Slot_Engine_Boilers (e.g., 4)
- [ ] Module_Slot_Engine_Turbines (e.g., 2)
- [ ] Module_Slot_FCS_Directors (e.g., 1)
- [ ] Module_Slot_Radar_Masts (e.g., 2)

### Crew (3 fields)
- [ ] Crew_Total_Min (skeleton crew, ~65% of normal)
- [ ] Crew_Total (normal operational crew)
- [ ] Crew_Total_Max (maximum capacity, ~115% of normal)

### Capacity (2 fields)
- [ ] Magazine_Capacity_Total_TONS
- [ ] Fuel_Capacity_TONS

### Dimensions (3 fields)
- [ ] Length_Overall_FT
- [ ] Beam_FT
- [ ] Draft_FT

---

## Research Sources

### Primary Sources (Most Reliable)
1. **NavWeaps.com** - Comprehensive naval weapons database
   - URL: http://www.navweaps.com/
   - Coverage: Excellent for armament, fire control, dimensions
   - Reliability: Very high (maintained by naval historians)

2. **Wikipedia Ship Class Articles**
   - URL: https://en.wikipedia.org/wiki/[Ship_Class]
   - Coverage: Good for general specs, crew, dimensions
   - Reliability: Medium-High (verify against other sources)

3. **Jane's Fighting Ships** (Historical Editions)
   - Coverage: Excellent for all specifications
   - Reliability: Very high (authoritative reference)
   - Availability: May require library access

### Secondary Sources
4. **Naval-History.net**
   - Good for British ships
   - Operational history focus

5. **Combined Fleet** (combinedfleet.com)
   - Japanese naval vessels
   - Very detailed IJN coverage

6. **German Naval History** (german-navy.de)
   - Kriegsmarine vessels
   - Good technical details

### Fallback Sources
7. **Conway's All The World's Fighting Ships**
   - Book series by era
   - Comprehensive but may need library

8. **GlobalSecurity.org**
   - Modern vessels (post-1945)
   - Good for Cold War and modern ships

---

## Example: Fletcher-class DD Research

**Class**: Fletcher-class destroyer
**Ships**: 175 built (1942-1944)
**Priority**: 🔥 CRITICAL #1

### Hardpoints
- **Main Battery**: 5× 5"/38 caliber dual-purpose guns in single mounts
  - `Hardpoint_Main_Battery`: "5× 5"/38 DP single mounts, 3 fore/2 aft"
  - `Hardpoint_Main_Count`: 5

- **AA Light**: 10× 40mm Bofors (varies, up to 40mm by 1945)
  - `Hardpoint_AA_Light`: "10× 40mm Bofors quad/twin mounts"
  - `Hardpoint_AA_Light_Count`: 10

- **AA Close**: 7× 20mm Oerlikon (early), up to 11× (late war)
  - `Hardpoint_AA_Close`: "7× 20mm Oerlikon single mounts"
  - `Hardpoint_AA_Close_Count`: 7

- **Torpedoes**: 10× 21" torpedo tubes in 2 quintuple mounts
  - `Hardpoint_Torpedo`: "10× 21" torpedo tubes, 2 quintuple mounts amidships"
  - `Hardpoint_Torpedo_Count`: 10

### Modules
- **Boilers**: 4× Babcock & Wilcox boilers
  - `Module_Slot_Engine_Boilers`: 4

- **Turbines**: 2× General Electric geared turbines (2 shafts)
  - `Module_Slot_Engine_Turbines`: 2

- **FCS**: 1× Mk 37 gun director
  - `Module_Slot_FCS_Directors`: 1

- **Radar**: 2× (1× search + 1× fire control)
  - `Module_Slot_Radar_Masts`: 2

### Crew
- **Normal**: 273 officers and enlisted
  - `Crew_Total_Min`: 180 (skeleton crew)
  - `Crew_Total`: 273 (normal)
  - `Crew_Total_Max`: 315 (wartime with extra AA crews)

### Capacity
- **Fuel**: 492 tons fuel oil
  - `Fuel_Capacity_TONS`: 492

- **Magazine**: ~140 tons (estimated, 8% of 2100 ton displacement)
  - `Magazine_Capacity_Total_TONS`: 168

### Dimensions
- **Length**: 376 ft 6 in overall
  - `Length_Overall_FT`: 376.5

- **Beam**: 39 ft 8 in
  - `Beam_FT`: 39.7

- **Draft**: 13 ft 9 in (mean)
  - `Draft_FT`: 13.8

**Sources**:
- NavWeaps: http://www.navweaps.com/index_tech/tech-070.php
- Wikipedia: https://en.wikipedia.org/wiki/Fletcher-class_destroyer
- NavSource: http://www.navsource.org/archives/05idx.htm

---

## Progress Tracking

### Completed Classes: 0/50

| Class | Ships | Status | Researcher | Date | Source |
|-------|-------|--------|------------|------|--------|
| Fletcher-class | 175 | ⏳ Pending | - | - | - |
| Essex-class | 24 | ⏳ Pending | - | - | - |
| Cleveland-class | 27 | ⏳ Pending | - | - | - |
| Baltimore-class | 14 | ⏳ Pending | - | - | - |
| Iowa-class | 4 | ⏳ Pending | - | - | - |
| Gearing-class | 50 | ⏳ Pending | - | - | - |
| Sumner-class | 60 | ⏳ Pending | - | - | - |
| Wickes-class | 110 | ⏳ Pending | - | - | - |
| Clemson-class | 150 | ⏳ Pending | - | - | - |
| Benson-class | 30 | ⏳ Pending | - | - | - |

*(Add more rows as research progresses)*

---

## Estimation Algorithms

For ships without direct research, use these estimation rules:

### Hardpoint Estimation by Type & Era

**Destroyers**:
```yaml
Pre-WWI (1890-1917):
  Main: 4× 3-4" guns
  Torpedoes: 6× 18" tubes

WWI (1917-1920):
  Main: 4× 4" guns
  Torpedoes: 12× 21" tubes

WWII Early (1940-1943):
  Main: 4-5× 5" DP guns
  AA_Light: 4-6× 40mm
  AA_Close: 4-8× 20mm
  Torpedoes: 10× 21" tubes

WWII Late (1944-1945):
  Main: 5× 5" DP guns
  AA_Light: 10× 40mm
  AA_Close: 7-11× 20mm
  Torpedoes: 10× 21" tubes

Modern (1960+):
  Main: 1-2× 5" guns
  Missiles: VLS cells 40-90
  Torpedoes: 6× torpedo tubes (ASW)
```

**Cruisers**:
```yaml
Heavy Cruisers (CA):
  Main: 9× 8" guns (3 triple turrets)
  Secondary: 8-12× 5" DP guns
  AA_Light: 20-40× 40mm (WWII)
  AA_Close: 20-30× 20mm (WWII)

Light Cruisers (CL):
  Main: 12-15× 6" guns (4-5 triple turrets)
  Secondary: 8-12× 5" DP guns
  AA_Light: 20-28× 40mm (WWII)
  AA_Close: 21-28× 20mm (WWII)
```

**Battleships**:
```yaml
Pre-Dreadnought (1890-1905):
  Main: 4× 12-13" guns (2 twin turrets)
  Secondary: 12-16× 6-8" guns

Dreadnought (1906-1920):
  Main: 8-12× 12-14" guns (4-6 twin turrets)
  Secondary: 12-16× 5" guns

Fast Battleship (1940+):
  Main: 9× 16" guns (3 triple turrets)
  Secondary: 20× 5" DP guns
  AA_Light: 60-80× 40mm
  AA_Close: 40-60× 20mm
```

### Module Slot Estimation

**By Propulsion Type**:
```yaml
Steam Turbine:
  Boilers: displacement / 2500 (range 4-24)
  Turbines: 2 (most common) or 4 (large ships)

Example:
  Fletcher DD (2100 tons): 2100/2500 = 0.84 → round to 1, but actual = 4
  Better formula: sqrt(displacement/200)
  Fletcher: sqrt(2100/200) = sqrt(10.5) = 3.24 → 4 boilers ✓
```

**FCS Directors**:
```yaml
By Era:
  Pre-1920: 1 director
  1920-1940: 1-2 directors
  WWII: 2 directors (DD/CL), 3-4 (CA/BB)
  Modern: 1 (integrated systems)
```

**Radar Masts**:
```yaml
By Era:
  Pre-1940: 0 (no radar)
  1940-1945: 1-2 (search + fire control)
  1945-1960: 2-3
  1960+: 1-4 (phased arrays count as 1)
```

### Crew Estimation

**By Displacement**:
```yaml
Formula: crew = displacement × crew_ratio

Destroyer: displacement × 0.13
Cruiser: displacement × 0.10
Battleship: displacement × 0.055
Carrier: displacement × 0.10 (+ air wing ~1500)
Submarine: 50 + (displacement × 0.03)

Example:
  Fletcher DD (2100 tons): 2100 × 0.13 = 273 crew ✓ (actual = 273)
  Iowa BB (57000 tons): 57000 × 0.055 = 3135 crew ✓ (actual ~2700-2800)
```

### Capacity Estimation

**Magazine Capacity**:
```yaml
Formula: displacement × magazine_ratio

Destroyer: displacement × 0.04 (4%)
Cruiser: displacement × 0.05-0.06 (5-6%)
Battleship: displacement × 0.08 (8%)
Carrier: displacement × 0.12 (12%, includes aviation ordnance)
```

**Fuel Capacity**:
```yaml
Formula: range_nm × fuel_consumption_rate / cruise_speed

Approximate fuel consumption:
  DD (2000 tons): 8-10 tons/hour at 15 knots
  CL (10000 tons): 25-35 tons/hour at 15 knots
  CA (10000 tons): 25-35 tons/hour at 15 knots
  BB (35000 tons): 60-70 tons/hour at 15 knots

Cross-check with existing Range_NM field in database!
```

---

## Quality Assurance Checklist

Before marking a class as "Complete", verify:

- [ ] All 20 fields populated
- [ ] Hardpoint counts match historical records
- [ ] Module slots reasonable for ship size/era
- [ ] Crew numbers within expected range
- [ ] Magazine capacity ~4-12% of displacement
- [ ] Fuel capacity supports listed range
- [ ] Dimensions match known values
- [ ] Source documented
- [ ] Spot-check 2-3 individual ships in class

---

## Next Steps

1. ✅ Extract unique ship classes → **COMPLETE** (782 classes identified)
2. 🔄 Create research tracking document → **IN PROGRESS**
3. ⏳ Begin Phase 1 research (Top 5 classes)
4. ⏳ Populate data into database
5. ⏳ Run estimation algorithms for remaining ships
6. ⏳ Validate against reference ships

**Status**: Research tracking system established
**Ready to Begin**: Phase 1 - Top 5 Critical Classes
**Estimated Time**: 18-20 hours total (4-6 hours for Phase 1)

---

**Document Version**: 1.0
**Last Updated**: 2025-10-12
**Maintained By**: Claude Code SuperClaude Framework
