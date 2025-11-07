# USA New Cruiser Classes - INSERT Statements and Logic

**Date**: October 25, 2025
**Purpose**: Complete the USA Cruisers Research Tree with 4 missing classes (6041-6044)
**Total New Nodes**: 4 classes

---

## INSERT Statements for Ships Research Tree Table

### Format
```
| Node_ID | Country | Ship_Class | Ship_Type | Branch_Name | Tier | Era | Year_Commissioned | Is_Free | Research_Cost | Build_Time_Months | Purchase_Cost | Crew_Size | Short_Description | Full_Description | Ship_Title | Special_Ability | Notes |
```

### New Classes (6041-6044)

```markdown
| 6041 | USA | Alaska-class | CB | Heavy Main Line | 5 | Large Cruiser | 1944 | 0 | 20000 | 48 | 55000000 | 72 | Large cruiser | 9×12"/50 guns, battlecruiser concept | Large Cruiser | 12" guns, +50% vs light armor | 2 ships, CB-1/2, alternative heavy path |
| 6042 | USA | St. Louis-class (1904) | CL | Starting | 1 | Protected Cruiser | 1906 | 0 | 2000 | 18 | 1500000 | 30 | Semi-armored cruiser | 14×6"/50 guns, protected + belt | Semi-Armored CL | Protected + belt armor | 3 ships, bridge to modern cruisers |
| 6043 | USA | Denver-class | CL | Starting | 1 | Protected Cruiser | 1904 | 0 | 1500 | 18 | 500000 | 24 | Peace cruiser | 10×5"/50 guns, gunboat duties | Peace Cruiser | Slow (16 kts), colonial duties | 6 ships, gunboat role |
| 6044 | USA | Tennessee-class | ACR | Starting | 1 | Armored Cruiser | 1906 | 0 | 2500 | 24 | 2000000 | 36 | Armored cruiser | 4×10"/40 guns, pre-dreadnought | Armored Cruiser | 10" guns, heavy armor | 4 ships, ACR-10 to ACR-13 |
```

---

## Prerequisites Table Entries

**New Prerequisites** (4 entries):

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 147 | 6041 | 6012 | Baltimore-class | 1 | NULL | Alaska requires Baltimore (large cruiser from WWII heavy) |
| 148 | 6042 | 6044 | Tennessee-class | 1 | 1 | St. Louis (1904) requires Tennessee OR Denver |
| 149 | 6042 | 6043 | Denver-class | 1 | 1 | St. Louis (1904) requires Tennessee OR Denver |
| 150 | 6043 | 6000 | Chester-class | 1 | NULL | Denver requires Chester (early protected path) |

**Updated Prerequisites** (modify existing):

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 100 (MODIFY) | 6002 | 6001 | Omaha-class | 1 | 1 | Pensacola requires Omaha OR St. Louis (1904) |
| 100b (NEW) | 6002 | 6042 | St. Louis-class (1904) | 1 | 1 | Pensacola requires Omaha OR St. Louis (1904) |
| 101 (MODIFY) | 6003 | 6001 | Omaha-class | 1 | 1 | Northampton requires Omaha OR St. Louis (1904) |
| 101b (NEW) | 6003 | 6042 | St. Louis-class (1904) | 1 | 1 | Northampton requires Omaha OR St. Louis (1904) |
| 102 (MODIFY) | 6004 | 6001 | Omaha-class | 1 | 1 | Brooklyn requires Omaha OR St. Louis (1904) |
| 102b (NEW) | 6004 | 6042 | St. Louis-class (1904) | 1 | 1 | Brooklyn requires Omaha OR St. Louis (1904) |
| 116 (MODIFY) | 6016 | 6012 | Baltimore-class | 1 | 1 | Des Moines requires Baltimore, Oregon City, OR Alaska |
| 116b (NEW) | 6016 | 6041 | Alaska-class | 1 | 1 | Des Moines requires Baltimore, Oregon City, OR Alaska |

**Total Prerequisites**: 47 + 8 new = 55 entries

---

## Unlocks Table Entries

**New Unlocks** (8 entries):

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 247 | 6000 | 6043 | Denver-class | 1 | 2 | Chester unlocks Denver (peace cruiser alternative) |
| 248 | 6043 | 6042 | St. Louis-class (1904) | 1 | 1 | Denver unlocks St. Louis (1904) |
| 249 | 6044 | 6042 | St. Louis-class (1904) | 1 | 1 | Tennessee unlocks St. Louis (1904) |
| 250 | 6042 | 6002 | Pensacola-class | 1 | 1 | St. Louis (1904) unlocks Pensacola (alternative path) |
| 251 | 6042 | 6003 | Northampton-class | 1 | 1 | St. Louis (1904) unlocks Northampton (alternative path) |
| 252 | 6042 | 6004 | Brooklyn-class | 1 | 1 | St. Louis (1904) unlocks Brooklyn (alternative path) |
| 253 | 6012 | 6041 | Alaska-class | 1 | 2 | Baltimore unlocks Alaska (large cruiser branch) |
| 254 | 6041 | 6016 | Des Moines-class | 1 | 1 | Alaska unlocks Des Moines (merges to ultimate gun) |

**Total Unlocks**: 47 + 8 new = 55 entries

---

## Research Branches Table Updates

**New Branch** (if using separate branch):

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 23 | USA | CB | Large Cruiser | 12" gun battlecruiser-type cruisers | #FF69B4 | 6041 | 6041 | 13 | 13 | Large Cruiser | Large Cruiser | Alaska-class only. Branches from Heavy Main Line (13), merges back. 2 ships built. |

**Updated Branches**:

| Branch_ID | Branch_Name | Notes Update |
|-----------|-------------|--------------|
| 12 | Starting | NOW INCLUDES: Chester (6000), Omaha (6001), Tennessee ACR (6044), Denver (6043), St. Louis 1904 (6042) |
| 13 | Heavy Main Line | NOW INCLUDES: Alaska (6041) as alternative branch point from Baltimore |

---

## Detailed Class Specifications

### 6041: Alaska-class (CB - Large Cruiser)

**Historical Context**: Designed to counter Japanese large cruisers and operate independently. Only 2 completed (Alaska CB-1, Guam CB-2) before cancellation. Hawaii (CB-3) 82% complete when cancelled.

**Specifications**:
- **Displacement**: 29,779 tons standard, 34,253 tons full load
- **Dimensions**: 808'6" × 91'1" × 31'10"
- **Speed**: 33 knots (150,000 SHP)
- **Main Battery**: 9×12"/50 Mark 8 guns (3 triple turrets)
- **Secondary**: 12×5"/38 DP guns (6 twin mounts)
- **AA**: 56×40mm, 34×20mm
- **Armor**: 9" belt, 4" deck, 12.8" turret face
- **Crew**: 1,517
- **Aircraft**: 4×floatplanes, 2 catapults

**Game Stats**:
- **Research Cost**: 20,000 RP
- **Build Time**: 48 months
- **Purchase Cost**: $55,000,000
- **Crew**: 72
- **Special Ability**: "12" guns, +50% vs light armor"
- **Unlock**: Requires Baltimore, unlocks Des Moines

**Unlock Path**: Baltimore (6012) → Alaska (6041) → Des Moines (6016)

---

### 6042: St. Louis-class (1904) - Protected/Semi-Armored Cruiser

**Historical Context**: Transition design between protected cruisers and modern light cruisers. Featured both armored deck AND thin waterline belt. St. Louis, Milwaukee, Charleston.

**Specifications**:
- **Displacement**: 9,700 tons
- **Dimensions**: 426'6" × 66' × 22'6"
- **Speed**: 22 knots
- **Main Battery**: 14×6"/50 guns (4 single forward/aft, 10 casemate)
- **Secondary**: 18×3"/50 guns
- **Armor**: 2" belt, 2.5" deck (protected + belt)
- **Crew**: 673

**Game Stats**:
- **Research Cost**: 2,000 RP
- **Build Time**: 18 months
- **Purchase Cost**: $1,500,000
- **Crew**: 30
- **Special Ability**: "Protected + belt armor"
- **Unlock**: Requires Tennessee OR Denver, unlocks Pensacola/Northampton/Brooklyn

**Unlock Path**: Tennessee/Denver → St. Louis (1904) → Treaty Era Cruisers

---

### 6043: Denver-class - Protected Cruiser ("Peace Cruiser")

**Historical Context**: Slow, lightly armed cruisers for colonial gunboat duties. Denver, Des Moines, Chattanooga, Galveston, Tacoma, Cleveland. Called "peace cruisers" - too slow for combat.

**Specifications**:
- **Displacement**: 3,200 tons
- **Dimensions**: 308'9" × 44' × 17'
- **Speed**: 16 knots (SLOW!)
- **Main Battery**: 10×5"/50 guns
- **Secondary**: 8×6-pdr guns
- **Armor**: 2" deck (protected only)
- **Crew**: 331

**Game Stats**:
- **Research Cost**: 1,500 RP
- **Build Time**: 18 months
- **Purchase Cost**: $500,000
- **Crew**: 24
- **Special Ability**: "Slow (16 kts), colonial duties"
- **Unlock**: Requires Chester, unlocks St. Louis (1904)

**Unlock Path**: Chester (6000) → Denver (6043) → St. Louis (1904)

---

### 6044: Tennessee-class (ACR - Armored Cruiser)

**Historical Context**: Last US armored cruisers. ACR-10 Tennessee (later Memphis), ACR-11 Washington (Seattle), ACR-12 North Carolina (Charlotte), ACR-13 Montana (Missoula). Renamed to free state names for battleships.

**Specifications**:
- **Displacement**: 14,500 tons
- **Dimensions**: 504'6" × 72'11" × 25'
- **Speed**: 22 knots
- **Main Battery**: 4×10"/40 guns (2 twin turrets)
- **Secondary**: 16×6"/50 guns
- **Armor**: 5" belt, 9.5" turret, 2" deck
- **Crew**: 859

**Game Stats**:
- **Research Cost**: 2,500 RP
- **Build Time**: 24 months
- **Purchase Cost**: $2,000,000
- **Crew**: 36
- **Special Ability**: "10" guns, heavy armor"
- **Unlock**: FREE starter (alternative), unlocks St. Louis (1904)

**Unlock Path**: Tennessee (6044) → St. Louis (1904) → Treaty Era

---

## Summary Statistics

**Total USA Cruiser Nodes**: 45 (6000-6044) ✅ COMPLETE

**Node Distribution**:
- Tier 1 Starting: 6 nodes (6000, 6001, 6042, 6043, 6044, + paths)
- Tier 2-4 Treaty/Pre-WWII: 12 nodes
- Tier 5-6 WWII/Ultimate Gun: 10 nodes (including 6041 Alaska)
- Tier 7-10 Missile/Nuclear/Aegis: 17 nodes

**New Branches Added**:
- Large Cruiser branch (6041)
- Enhanced Starting Era with armored/protected variety (6042-6044)

**Prerequisites**: 55 total (47 original + 8 new)
**Unlocks**: 55 total (47 original + 8 new)
**Research Branches**: 12 total (11 original + 1 new Large Cruiser branch)

---

## Integration Checklist

- [x] CREATE INSERT statements for 4 new classes
- [x] DEFINE prerequisite logic (what's required)
- [x] DEFINE unlock logic (what they unlock)
- [x] UPDATE research branches
- [x] ADD historical specifications
- [x] VERIFY flowchart placement
- [ ] ADD to INSERT_CRUISERS_DESTROYERS_SUBMARINES.md
- [ ] UPDATE USA_CRUISERS_RESEARCH_TREE_LOGIC.md prerequisite tables
- [ ] UPDATE USA_CRUISERS_RESEARCH_TREE_LOGIC.md unlock tables
- [ ] UPDATE USA_CRUISERS_RESEARCH_TREE_LOGIC.md branch tables
- [ ] TEST unlock chains for logic errors

---

**Status**: ✅ NEW CLASSES COMPLETE - Ready for database integration
