# Pre-SQL Conversion Validation Report

**Date**: 2025
**Purpose**: Comprehensive validation before converting MD databases to SQL
**Total Databases**: 7 (6 weapon systems + 1 research tree)

## Executive Summary

| Database | Entries | Fields (Actual) | ID Range | Schema Status | Data Quality | SQL Ready |
|----------|---------|-----------------|----------|---------------|--------------|-----------|
| Ships | 959 | 20 (78 doc) | Various | 🚨 MISMATCH | ⏳ Pending | ⏳ No |
| Torpedoes | 236 | 18 | 1000-1399 | ✅ Match | ⚠️ Notes issue | ⏳ No |
| Missiles | 192 | 17 (24 doc) | 2000-2499 | 🚨 MISMATCH | ⏳ Pending | ⏳ No |
| Naval Aircraft | 144 | 19 (32 doc) | 3000-3499 | 🚨 MISMATCH | ⏳ Pending | ⏳ No |
| Ground Aircraft | 147 | 19 (31 doc) | 4000-4499 | 🚨 MISMATCH | ⏳ Pending | ⏳ No |
| Bombs | 107 | 23 | 9000-9499 | ✅ Match | ⏳ Pending | ⏳ No |
| Research Tree | ~675 | 18 | All ranges | ✅ Match | ⏳ Pending | ⏳ No |
| **TOTAL** | **2,454** | - | - | **4 MISMATCH** | - | **🚨 No** |

## Database Schemas

### 1. Torpedoes Database (naval_torpedoes_database.md)

**Entry Count**: 236 torpedoes
**ID Range**: 1000-1399
**Field Count**: 18 fields

**Schema**:
```
Torpedo_ID | Country | Designation | Type | Year_Introduced |
Diameter_IN | Length_FT | Weight_LBS | Warhead_LBS | Warhead_Type |
Max_Speed_KTS | Max_Range_YDS | Running_Depth_FT | Propulsion |
Guidance | Launch_Platform | Modded | Notes
```

**Field Analysis**:
- ✅ Primary Key: Torpedo_ID (unique identifiers)
- ✅ Foreign Key Ready: Compatible with research tree
- ✅ Data Types: Mixed (INT, DECIMAL, VARCHAR, TEXT)
- ✅ Nullable Fields: Notes (TEXT), others required
- ⚠️ **Issue**: Notes column contains numbers (not descriptive notes)

**Sample Entry Validation**:
```
ID: 1000
Country: USA
Designation: Whitehead Torpedo (1890)
Type: Steam
Year: 1890
Diameter: 18.0 inches
Length: 15.0 feet
Weight: 38880 lbs
Warhead: 300 lbs (Guncotton)
Speed: 33.5 knots
Range: 2500 yards
Depth: 15-50 feet
Propulsion: Steam turbine, wet-heater
Guidance: Straight-running (gyroscope)
Platform: Surface ships, submarines
Modded: 0
Notes: 0 (should be descriptive text!)
```

**SQL Readiness**: ⚠️ **ISSUES FOUND**
- Notes field contains numbers instead of text
- Need to verify all numeric fields are properly formatted
- Need to check for special characters in text fields

### 2. Missiles Database (naval_missiles_database.md)

**Entry Count**: 192 missiles
**ID Range**: 2000-2499
**Field Count**: 17 actual (24 documented)

**Schema Mismatch**: 🚨 **CRITICAL**
- **Documented Schema** (24 fields): Includes NATO_Codename, Wingspan_FT, Warhead_Type, Min_Range_NM, Max_Altitude_FT, Min_Altitude_FT, Notes
- **Actual Schema** (17 fields): Missile_ID, Country, Designation, Type, Year_Introduced, Diameter_IN, Length_FT, Weight_LBS, Warhead_LBS, Max_Speed_MACH, Max_Range_NM, Propulsion, Guidance, Launch_Platform, Subtype, Modded, Source_Type
- **Missing Fields** (7): NATO_Codename, Wingspan_FT, Warhead_Type, Min_Range_NM, Max_Altitude_FT, Min_Altitude_FT, Notes
- **Impact**: 29% of documented schema missing from actual data

### 3. Naval Aircraft Database (naval_aircraft_database.md)

**Entry Count**: 144 aircraft
**ID Range**: 3000-3499
**Field Count**: 19 actual (32 documented)

**Schema Mismatch**: 🚨 **CRITICAL**
- **Documented Schema** (32 fields): Comprehensive aircraft specifications including Nickname, Manufacturer, Year_Retired, Crew, Height_FT, Wing_Area_SQFT, Max_Speed_MACH, Range_NM, Rate_Of_Climb_FPM, Wing_Loading_PSF, Thrust_To_Weight, Catapult_Capable, Folding_Wings
- **Actual Schema** (19 fields): Aircraft_ID, Country, Designation, Year_Introduced, Type, Length_FT, Wingspan_FT, Empty_Weight_LBS, Max_Takeoff_Weight_LBS, Max_Speed_MPH, Cruise_Speed_MPH, Combat_Radius_NM, Service_Ceiling_FT, Engine_Type, Engine_Count, Carrier_Capable, Role, Modded, Notes
- **Missing Fields** (13): Nickname, Manufacturer, Year_Retired, Crew, Height_FT, Wing_Area_SQFT, Max_Speed_MACH, Range_NM, Rate_Of_Climb_FPM, Wing_Loading_PSF, Thrust_To_Weight, Catapult_Capable, Folding_Wings
- **Impact**: 41% of documented schema missing from actual data

### 4. Ground Aircraft Database (ground_aircraft_database.md)

**Entry Count**: 147 aircraft
**ID Range**: 4000-4499
**Field Count**: 19 actual (31 documented)

**Schema Mismatch**: 🚨 **CRITICAL**
- **Documented Schema** (31 fields): Comprehensive ground aircraft specs including Nickname, Manufacturer, Generation, Year_Retired, Height_FT, Wing_Area_SQFT, Max_Speed_MACH, Range_NM, Rate_Of_Climb_FPM, Wing_Loading_PSF, Thrust_To_Weight, Stealth_Capable, Supercruise_Capable, STOL_Capable
- **Actual Schema** (19 fields): Aircraft_ID, Country, Designation, Year_Introduced, Type, Length_FT, Wingspan_FT, Empty_Weight_LBS, Max_Takeoff_Weight_LBS, Max_Speed_MPH, Cruise_Speed_MPH, Combat_Radius_NM, Service_Ceiling_FT, Engine_Type, Engine_Count, Carrier_Capable, Role, Modded, Notes
- **Missing Fields** (12): Nickname, Manufacturer, Generation, Year_Retired, Height_FT, Wing_Area_SQFT, Max_Speed_MACH, Range_NM, Rate_Of_Climb_FPM, Wing_Loading_PSF, Thrust_To_Weight, Stealth_Capable, Supercruise_Capable, STOL_Capable
- **Impact**: 39% of documented schema missing from actual data

### 5. Bombs Database (naval_bombs_database.md)

**Entry Count**: 107 bombs
**ID Range**: 9000-9499
**Field Count**: 23 fields

**Schema**:
```
Bomb_ID | Nation | Designation | Bomb_Type | Year |
Weight | Length | Diameter | Explosive_Weight | Explosive_Type |
Blast_Radius | Penetration | Guidance_Type | Guidance_Accuracy | Max_Range |
Terminal_Velocity | Fuse_Type | Delivery_Platform | Cost_USD | Production_Years |
Variants | Historical_Notes | Modded
```

**Field Analysis**:
- ✅ Primary Key: Bomb_ID (unique identifiers)
- ✅ Foreign Key Ready: Compatible with research tree
- ✅ Data Types: Mixed (INT, DECIMAL, VARCHAR, TEXT)
- ✅ Comprehensive: Most complete schema with historical context
- ✅ Well-structured: Cost, production years, variants included

**Sample Entry Validation**:
```
ID: 9000
Nation: USA
Designation: AN-M30
Type: GP Bomb
Year: 1940
Weight: 45 kg
Length: 1.73 m
Diameter: 0.254 m
Explosive Weight: 20 kg (Tritonal)
Blast Radius: 49 m
Penetration: 0 mm
Guidance: None
Accuracy: 200 m CEP
Range: 5 km
Terminal Velocity: 154 m/s
Fuse: Contact/Delay
Platform: Attack Aircraft
Cost: $2,900
Production: 1940-1950
Variants: Standard
Notes: Standard operational bomb
Modded: 0
```

**SQL Readiness**: ✅ **GOOD QUALITY**
- Well-structured data
- Comprehensive specifications
- Historical context included
- Cost and production data present

### 6. Ships Database (naval_ships_database.md)

**Entry Count**: 959 ships
**ID Range**: 10000-18999 (by type: BB 10000-10999, CV 11000-11999, CA 12000-12499, CL 12500-12999, DD 13000-14999, SS 15000-16999)
**Field Count**: 20 actual (78 documented)

**Schema Mismatch**: 🚨🚨 **MOST CRITICAL**
- **Documented Schema** (78 fields): Extremely comprehensive modular ship building system including:
  - Basic identification (6 fields): Ship_ID, Country, Ship_Name, Ship_Class, Hull_Variant, Base_Hull_ID
  - Construction/service dates (6 fields)
  - Physical dimensions (7 fields): Displacement, Length, Beam, Draft, Turning_Radius
  - Crew management (9 fields): Officers/Enlisted/Total for Min/Normal/Max tiers
  - Hardpoint system (12 fields): Main Battery, Secondary Battery, AA (Light/Close), Torpedoes, Missiles (VLS/Launchers)
  - Module slots (11 fields): Engines (Boilers/Turbines/Reactors), FCS, Radar, Sonar, Helicopters, Catapults
  - Internal capacity (10 fields): Magazine capacity by type, Fuel, Supplies, Aviation fuel
  - Carrier facilities (12 fields): Flight deck, Catapults, Elevators, Hangar, Aircraft capacity
  - Build/refit mechanics (5 fields)

- **Actual Schema** (20 fields): Ship_ID, Country, Ship_Name, Ship_Class, Hull_Variant, Ship_Type, Ship_Type_Full, Era, Year_Commissioned, Year_Designed, Year_Completed, Displacement_Standard, Displacement_Full, Max_Speed, Cruise_Speed, Range_NM, Cost_USD, Build_Time, Modded, Notes

- **Missing Fields** (58 fields):
  - All hardpoint specifications (12 fields)
  - All module slots (11 fields)
  - Crew tier management (9 fields)
  - Magazine capacity breakdown (7 fields)
  - Carrier-specific facilities (12 fields)
  - Detailed physical dimensions (7 fields: Length, Beam, Draft, Turning_Radius, etc.)

- **Impact**: 74% of documented schema missing - **WORST MISMATCH** of all databases

### 7. Research Tree Database (ship_research_tree_database.md)

**Entry Count**: ~675 nodes (204 Research Nodes + ~220 Prerequisites + ~220 Unlocks + 31 Research Branches)
**ID Range**: All weapon system ranges (1000-9499)
**Field Count**: 18 fields (matches documented schema)

**Schema Status**: ✅ **PERFECT MATCH**

**Actual Schema** (18 fields):
```
Node_ID | Country | Ship_Class | Ship_Type | Tech_Branch | Tech_Tier |
Era | Year_Available | Is_Starting_Tech | Research_Cost_RP | Research_Time_Months |
Build_Cost_USD | Build_Time_Months | Design_Philosophy | Historical_Context |
Gameplay_Role | Special_Ability | Notes
```

**Purpose**: Links all weapon systems in tech tree progression
**Critical**: Must maintain referential integrity with all other databases

**Outstanding Validation**:
- Need to verify all Ship_Class references exist in Ships Database
- Need to check dependency chains are valid (Prerequisites table)
- Need to verify no circular dependencies (Unlocks table)

## Critical Issues Identified

### Issue #1: Schema Mismatches 🚨🚨 **CRITICAL**
**Severity**: CRITICAL
**Description**: 4 out of 7 databases have significant schema mismatches between documented schema definitions and actual data structure
**Impact**:
- Cannot convert to SQL using documented schemas as-is
- Must decide: use simplified actual schema OR populate missing fields
- Ships database has 58 missing fields (74% of documented schema)
- Total 90+ missing fields across all mismatched databases
**Affected Databases**:
- Missiles: 24 documented → 17 actual (29% mismatch)
- Naval Aircraft: 32 documented → 19 actual (41% mismatch)
- Ground Aircraft: 31 documented → 19 actual (39% mismatch)
- Ships: 78 documented → 20 actual (74% mismatch) **WORST**
**Recommendation**: **BLOCKING ISSUE**
- Decision required: Which schema to use for SQL conversion?
  - Option A: Use simplified actual schema (faster, data exists)
  - Option B: Populate missing fields to match documented schema (complete, time-consuming)
  - Option C: Hybrid approach (populate critical fields only)

### Issue #2: Torpedoes Notes Field 🚨
**Severity**: Medium
**Description**: Notes field contains numbers (0-24) instead of descriptive text
**Impact**: Loss of historical/operational context
**Recommendation**:
- Investigate original data source
- Determine if numbers are codes or placeholders
- Consider migrating to proper descriptive notes

### Issue #3: Cross-Database Validation ⚠️
**Severity**: High
**Description**: Research tree references not validated
**Impact**: Potential foreign key violations in SQL
**Recommendation**: Verify all Node_IDs in research tree exist in weapon databases

## Recommended Actions

### Phase 1: Schema Analysis ✅ COMPLETE

**Critical Finding**: 4 out of 7 databases have **schema mismatches** between documented schema and actual data structure!

| Database | Documented Fields | Actual Fields | Status | Mismatch Impact |
|----------|-------------------|---------------|--------|-----------------|
| 1. Torpedoes | 18 | 18 | ✅ Match | None - schema accurate |
| 2. Missiles | 24 | 17 | 🚨 MISMATCH | Missing 7 fields: NATO_Codename, Wingspan_FT, Warhead_Type, Min_Range_NM, Max_Altitude_FT, Min_Altitude_FT, Notes |
| 3. Naval Aircraft | 32 | 19 | 🚨 MISMATCH | Missing 13 fields: Nickname, Manufacturer, Year_Retired, Crew, Height_FT, Wing_Area_SQFT, Max_Speed_MACH, Range_NM, Rate_Of_Climb_FPM, Wing_Loading_PSF, Thrust_To_Weight, Catapult_Capable, Folding_Wings |
| 4. Ground Aircraft | 31 | 19 | 🚨 MISMATCH | Missing 12 fields: Nickname, Manufacturer, Generation, Year_Retired, Height_FT, Wing_Area_SQFT, Max_Speed_MACH, Range_NM, Rate_Of_Climb_FPM, Wing_Loading_PSF, Thrust_To_Weight, Stealth_Capable, Supercruise_Capable, STOL_Capable |
| 5. Bombs | 23 | 23 | ✅ Match | None - schema accurate |
| 6. Ships | 78 | 20 | 🚨🚨 CRITICAL | **Missing 58 fields!** Including: hardpoints (12 fields), modules (11 fields), crew tiers (9 fields), magazine capacity (7 fields), carrier facilities (12 fields), armor, propulsion details |
| 7. Research Tree | 18 | 18 | ✅ Match | None - schema accurate |

**Summary**:
- ✅ **3 databases match**: Torpedoes, Bombs, Research Tree
- 🚨 **4 databases have mismatches**: Missiles (-7 fields), Naval Aircraft (-13 fields), Ground Aircraft (-12 fields), Ships (-58 fields)
- **Total Missing Fields**: 90+ fields across 4 databases
- **Impact**: CRITICAL - Cannot convert to SQL using documented schemas without deciding which schema to use

### Phase 2: Data Quality Check (Priority: HIGH)
1. Sample 10 random entries from each database
2. Verify no empty required fields
3. Check numeric fields for valid ranges
4. Check text fields for SQL injection characters
5. Verify date/year fields (1900-2025)

### Phase 3: Cross-Reference Validation (Priority: CRITICAL)
1. Extract all Node_IDs from research tree
2. Verify each Node_ID exists in appropriate weapon database
3. Check Requires_Tech_IDs point to valid nodes
4. Check Unlocks_Tech_IDs point to valid nodes
5. Identify orphaned nodes

### Phase 4: SQL Schema Design (Priority: MEDIUM)
1. Design normalized table structures
2. Define primary keys and foreign keys
3. Define indexes for performance
4. Define constraints (UNIQUE, NOT NULL, CHECK)
5. Design lookup tables (nations, weapon_types)

### Phase 5: Conversion Script Development (Priority: MEDIUM)
1. Choose conversion approach (AWK, Python, SQL)
2. Handle escape characters
3. Handle NULL values
4. Transaction handling
5. Error recovery

### Phase 6: Test Conversion (Priority: LOW)
1. Convert small sample (10-20 entries per database)
2. Verify data integrity
3. Test foreign key constraints
4. Test queries and joins

### Phase 7: Full Conversion (Priority: LOW)
1. Convert all databases
2. Verify entry counts match
3. Spot-check random entries
4. Performance testing

### Phase 8: Optimization (Priority: LOW)
1. Create indexes
2. Analyze query performance
3. Optimize slow queries
4. Document final schema

## Questions for User

Before proceeding with SQL conversion, we should answer:

1. **Data Quality**: Should we fix the torpedoes Notes field issue first?
2. **Schema Consistency**: Do all databases follow similar patterns?
3. **SQL Database Type**: MySQL, PostgreSQL, SQLite, or other?
4. **Normalization Level**: Fully normalized or denormalized for performance?
5. **Lookup Tables**: Should we create separate tables for nations, weapon types, etc.?
6. **Historical Data**: Should we preserve historical notes and context?
7. **Conversion Approach**: AWK scripts (fast) or Python (flexible)?

## Next Steps

**Recommendation**: Complete Phase 1 (Schema Analysis) for all databases before proceeding to SQL conversion.

**Immediate Actions**:
1. Extract and document schemas for Missiles, Aircraft, Ships databases
2. Investigate torpedoes Notes field issue
3. Verify bomb database data quality (sample check)
4. Design initial SQL schema based on findings

**Timeline Estimate**:
- Phase 1 (Schema Analysis): 1-2 hours
- Phase 2 (Data Quality): 2-3 hours
- Phase 3 (Cross-Reference): 2-3 hours
- Phase 4-8 (SQL Conversion): 4-6 hours
- **Total**: 9-14 hours of work

## Conclusion

**Current Status**: 🚨 **NOT READY for SQL Conversion**

**CRITICAL BLOCKING ISSUE**: Schema Mismatches
- 4 out of 7 databases have documented schemas that don't match actual data
- 90+ fields documented but not present in actual data
- Ships database worst: 78 documented → 20 actual (74% mismatch)

**Decision Required Before Proceeding**:

**Option A: Use Simplified Actual Schema** (Recommended for speed)
- ✅ Pros: Data exists, fast conversion, no data population needed
- ❌ Cons: Less comprehensive, missing advanced fields like hardpoints/modules
- ⏱️ Time: ~2-3 hours to SQL-ready

**Option B: Populate Missing Fields**
- ✅ Pros: Complete database matching documented specs
- ❌ Cons: Requires manual data population for 90+ fields
- ⏱️ Time: ~40-60 hours (research + data entry)

**Option C: Hybrid Approach**
- ✅ Pros: Balance between completeness and speed
- Populate critical fields (hardpoints, modules, crew) ~20 fields
- Leave optional fields (performance details) for future
- ⏱️ Time: ~10-15 hours

**Other Blocking Issues**:
- Torpedoes Notes field contains numbers instead of text
- Cross-reference validation not performed

**Recommended Path Forward**:
1. **User Decision**: Choose Option A, B, or C for schema approach
2. Fix torpedoes Notes field issue (30 min)
3. Validate cross-references (2-3 hours)
4. Design SQL schema based on chosen option (1-2 hours)
5. Proceed with conversion

**Estimated Time to SQL-Ready**:
- Option A: 4-6 hours
- Option B: 44-65 hours
- Option C: 14-20 hours

---

**Report Generated**: 2025
**Next Update**: After Phase 1 completion
