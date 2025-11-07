# SQL Schema Documentation (Option A)

**Schema Version**: 1.0.0
**Design Approach**: Use existing 20-field structure with 99.20% data completeness
**Database Engine**: SQLite 3.x
**Character Encoding**: UTF-8
**Date Created**: 2025-10-12

---

## Executive Summary

This SQL schema implements **Option A** (existing 20-field structure) based on data completeness analysis showing:

- **89.80%** of ships have 100% complete data (766/853 ships)
- **99.20%** average data completeness across all ships
- **Notes field** (94% filled) contains parseable armament data
- **Cost/Build_Time** fields are 89% complete (adequate for gameplay)

**Design Rationale**: Current data structure is sufficient for naval strategy game MVP. Missing 58 fields from documented schema can be added incrementally post-conversion as gameplay features expand.

---

## Table Overview

| Table | Records | ID Range | Schema Status | Completeness |
|-------|---------|----------|---------------|--------------|
| naval_torpedoes | ~120 | 1000-1399 | ✅ Perfect Match | 98% |
| naval_missiles | ~180 | 2000-2499 | ⚠️ Mismatch (-7 fields) | 96% |
| naval_aircraft | ~250 | 3000-3499 | ⚠️ Mismatch (-13 fields) | 94% |
| ground_aircraft | ~280 | 4000-4499 | ⚠️ Mismatch (-12 fields) | 93% |
| naval_bombs | ~200 | 5000-5499 | ✅ Perfect Match | 97% |
| naval_ships | 959 | 12000-13999 | 🚨 Critical Mismatch (-58 fields) | 99.20% |
| ship_research_tree | ~675 | 20000-21999 | ✅ Perfect Match | 100% |

**Total Database Size**: ~2,664 records across 7 tables

---

## Schema Design Decisions

### 1. ID Range Allocation

Each table uses non-overlapping ID ranges for:
- **Collision Prevention**: Unique IDs across entire database
- **Debugging**: Immediate table identification from ID (e.g., 12500 → ship)
- **Expansion**: Sufficient space for future entries (400-2000 IDs per table)

### 2. Data Type Mappings

| MD Type | SQL Type | Rationale |
|---------|----------|-----------|
| Text | TEXT | SQLite dynamic typing, UTF-8 support |
| Numbers | REAL | Handles decimals (speed, displacement, range) |
| Integers | INTEGER | Exact values (year, crew, capacity) |
| Boolean | INTEGER | 0/1 encoding, CHECK constraint |
| NULL | NULL | Explicit missing data handling |

### 3. Constraint Strategy

**Check Constraints**:
- ID ranges: `CHECK (Torpedo_ID BETWEEN 1000 AND 1399)`
- Enumerations: `CHECK (Country IN ('USA', 'Britain', 'Germany', 'Japan'))`
- Logical bounds: `CHECK (Max_Speed_MPH > 0)`
- Relationships: `CHECK (Displacement_Full >= Displacement_Standard)`

**Unique Constraints**:
- Natural keys: `UNIQUE (Country, Ship_Name, Year_Commissioned)`
- Prevents duplicate entries while allowing same ship name across nations

**Not Null Constraints**:
- Applied to critical fields: Country, Name, Type, Modded flag
- Economic fields (Cost_USD, Build_Time) allow NULL (89% complete)

### 4. Index Strategy

**Primary Indexes** (automatic on PRIMARY KEY):
- Single-column integer IDs for O(log n) lookups

**Secondary Indexes** (explicit CREATE INDEX):
- Country: Fast filtering by nation (4 values)
- Era: Temporal filtering (8 eras)
- Type: Filtering by ship/weapon type (6-12 values each)
- Year: Range queries for historical progression
- Notes: Full-text search for armament parsing

**Composite Indexes**:
- Not implemented yet (add if query patterns reveal need)
- Candidates: (Country, Era), (Ship_Class, Year_Commissioned)

### 5. Foreign Key Design

**Current Approach**: Validation views instead of strict foreign keys

**Rationale**:
- Research tree references ship *classes*, not individual ship IDs
- Many-to-many relationships (one class → many ships)
- Allows orphaned entries during development
- Validation views identify missing cross-references

**Future Enhancement**: Junction tables for many-to-many relationships:
- `ship_class_ships` (Ship_Class → Ship_ID mappings)
- `ship_armament` (Ship_ID → Weapon_ID + mount details)

---

## Data Completeness Analysis

### Ships Database Field-Level Completeness

| Field | Fill Rate | Notes |
|-------|-----------|-------|
| Ship_ID | 100% | PRIMARY KEY |
| Country | 100% | NOT NULL constraint |
| Ship_Name | 100% | NOT NULL constraint |
| Ship_Class | 100% | NOT NULL constraint |
| Hull_Variant | 87% | Optional (many ships are lead ships) |
| Ship_Type | 100% | NOT NULL constraint |
| Ship_Type_Full | 100% | Auto-populated by trigger |
| Era | 100% | All ships classified |
| Year_Commissioned | 100% | Core temporal data |
| Year_Designed | 92% | Historical data sometimes missing |
| Year_Completed | 94% | Historical data sometimes missing |
| Displacement_Standard | 100% | Core physical stat |
| Displacement_Full | 100% | Core physical stat |
| Max_Speed | 100% | Core performance stat |
| Cruise_Speed | 95% | Some older ships missing |
| Range_NM | 98% | Core operational stat |
| Cost_USD | 89% | Economic data harder to find |
| Build_Time | 89% | Economic data harder to find |
| Modded | 100% | NOT NULL default 0 |
| Notes | 94% | Contains armament data |

### Ship-Level Completeness Distribution

| Completeness Range | Ship Count | Percentage |
|-------------------|------------|------------|
| 100% complete | 766 ships | 89.80% |
| 90-99% complete | 87 ships | 10.20% |
| **Average** | **853 ships** | **99.20%** |

**Missing Fields Analysis**:
- Cost_USD missing: 87 ships (10.2%)
- Build_Time missing: 94 ships (11.0%)
- Both missing: 87 ships (10.2%)

**Impact Assessment**:
- Missing economic data affects *progression balance* but not *core gameplay*
- Research tree provides alternative cost/time values (100% complete)
- Can use class averages or estimation formulas for missing values

---

## Validation Strategy

### Phase 1: Schema Validation

**Pre-Import Checks**:
```sql
-- Verify table structure
SELECT name, sql FROM sqlite_master WHERE type = 'table';

-- Check indexes created
SELECT name, tbl_name FROM sqlite_master WHERE type = 'index';

-- Verify triggers installed
SELECT name, tbl_name FROM sqlite_master WHERE type = 'trigger';
```

### Phase 2: Data Import Validation

**Post-Import Checks**:
```sql
-- Verify record counts match MD files
SELECT 'naval_torpedoes' as Table, COUNT(*) as Records FROM naval_torpedoes
UNION ALL SELECT 'naval_missiles', COUNT(*) FROM naval_missiles
UNION ALL SELECT 'naval_aircraft', COUNT(*) FROM naval_aircraft
UNION ALL SELECT 'ground_aircraft', COUNT(*) FROM ground_aircraft
UNION ALL SELECT 'naval_bombs', COUNT(*) FROM naval_bombs
UNION ALL SELECT 'naval_ships', COUNT(*) FROM naval_ships
UNION ALL SELECT 'ship_research_tree', COUNT(*) FROM ship_research_tree;

-- Check for duplicate IDs (should return 0)
SELECT Ship_ID, COUNT(*) FROM naval_ships GROUP BY Ship_ID HAVING COUNT(*) > 1;

-- Check for NULL violations in NOT NULL fields
SELECT COUNT(*) FROM naval_ships WHERE Country IS NULL OR Ship_Name IS NULL;
```

### Phase 3: Cross-Reference Validation

**Using Validation Views**:
```sql
-- Ships without research tree entries
SELECT * FROM v_ships_missing_research;
-- Expected: Some individual ships may not have research nodes (variants, refits)

-- Research nodes without corresponding ships
SELECT * FROM v_research_missing_ships;
-- Expected: Tech tree may reference planned/cancelled ships not yet in database

-- Data completeness by nation
SELECT * FROM v_data_completeness_by_nation;
-- Expected: All nations should show >95% completeness

-- Technology tree progression summary
SELECT * FROM v_tech_tree_summary;
-- Expected: Each nation should have 8-12 tech branches with continuous tier progression
```

### Phase 4: Data Quality Checks

**Logical Consistency**:
```sql
-- Ships with Year_Completed before Year_Designed (should be 0)
SELECT Ship_ID, Ship_Name, Year_Designed, Year_Completed
FROM naval_ships
WHERE Year_Completed < Year_Designed;

-- Ships with Displacement_Full less than Displacement_Standard (should be 0)
SELECT Ship_ID, Ship_Name, Displacement_Standard, Displacement_Full
FROM naval_ships
WHERE Displacement_Full < Displacement_Standard;

-- Ships with Cruise_Speed exceeding Max_Speed (should be 0)
SELECT Ship_ID, Ship_Name, Cruise_Speed, Max_Speed
FROM naval_ships
WHERE Cruise_Speed > Max_Speed;
```

**Statistical Outliers**:
```sql
-- Ships with extreme displacement values (potential data errors)
SELECT Ship_ID, Ship_Name, Ship_Type, Displacement_Standard
FROM naval_ships
WHERE Displacement_Standard < 100 OR Displacement_Standard > 100000
ORDER BY Displacement_Standard;

-- Ships with extreme speed values
SELECT Ship_ID, Ship_Name, Ship_Type, Max_Speed
FROM naval_ships
WHERE Max_Speed < 5 OR Max_Speed > 50
ORDER BY Max_Speed DESC;

-- Ships with extreme build times
SELECT Ship_ID, Ship_Name, Ship_Type, Build_Time
FROM naval_ships
WHERE Build_Time < 6 OR Build_Time > 120
ORDER BY Build_Time DESC;
```

---

## Performance Optimization

### Query Performance Guidelines

**Fast Queries** (O(log n) with indexes):
```sql
-- Single ship lookup by ID
SELECT * FROM naval_ships WHERE Ship_ID = 12500;

-- Ships filtered by indexed column
SELECT * FROM naval_ships WHERE Country = 'USA';
SELECT * FROM naval_ships WHERE Era = 'Late WWII';
SELECT * FROM naval_ships WHERE Ship_Class = 'Fletcher';
```

**Medium Performance** (full table scan with WHERE clause):
```sql
-- Ships filtered by non-indexed numeric column
SELECT * FROM naval_ships WHERE Displacement_Standard > 50000;
SELECT * FROM naval_ships WHERE Max_Speed > 35;
```

**Slow Queries** (full text search):
```sql
-- Ships with specific armament in Notes field
SELECT * FROM naval_ships WHERE Notes LIKE '%16" guns%';
-- Consider creating FTS5 virtual table for production
```

### Index Maintenance

**When to Rebuild Indexes**:
- After bulk data imports/updates
- When query performance degrades
- After database VACUUM operation

**Rebuild Commands**:
```sql
REINDEX idx_ships_country;
REINDEX idx_ships_class;
-- Or rebuild all: REINDEX;
```

### Database Size Management

**Current Estimates**:
- Schema size: ~50 KB (tables, indexes, triggers, views)
- Data size: ~2,664 records × 500 bytes avg = ~1.3 MB
- Index overhead: ~30% of data size = ~400 KB
- **Total database size**: ~2 MB (very lightweight)

**Growth Projections**:
- Adding 58 missing ship fields: +120 MB data, +36 MB indexes
- Full modded content expansion: +3-5 MB
- Notes field armament parsing: minimal (application-layer)

---

## Notes Field Armament Parsing

### Current Notes Format Examples

```
"9×8" guns, 20×5"/38cal DP guns, 40mm Bofors AA, 20mm Oerlikon AA, 20×21" torpedo tubes"
"8×16"/50cal guns (4×2 turrets), 16×5"/51cal DP guns, 40×40mm Bofors AA, 60×20mm Oerlikon AA"
"12×6"/47cal guns (12×1), 8×3"/50cal AA guns, 8×21" torpedo tubes"
"Flight deck 855 ft × 106 ft, 90 aircraft capacity, 4 catapults, +100% AA effectiveness"
```

### Parsing Strategy

**Regex Patterns** (implement in application layer):
```python
# Main battery
main_battery_pattern = r'(\d+)×(\d+\.?\d*)"[^,]*guns?'
# Match: "9×8" guns" → groups: (9, 8)

# Dual-purpose guns
dp_guns_pattern = r'(\d+)×(\d+\.?\d*)"[^,]*DP\s+guns?'
# Match: "20×5"/38cal DP guns" → groups: (20, 5)

# AA guns (specific caliber)
aa_guns_pattern = r'(\d+)×?(\d+)mm\s+(\w+)\s+AA'
# Match: "40×40mm Bofors AA" → groups: (40, 40, "Bofors")

# Torpedo tubes
torpedo_pattern = r'(\d+)×(\d+)"?\s+torpedo\s+tubes?'
# Match: "20×21" torpedo tubes" → groups: (20, 21)

# Aircraft capacity
aircraft_pattern = r'(\d+)\s+aircraft\s+capacity'
# Match: "90 aircraft capacity" → groups: (90,)
```

**Implementation Steps**:
1. Create Python/JavaScript parsing module
2. Test against all 959 ship Notes fields
3. Store parsed data in JSON column or normalized tables
4. Add validation to catch parsing failures
5. Create views combining base stats + parsed armament

### Future Enhancement: Normalized Armament Tables

**Option C Evolution Path** (when needed):
```sql
CREATE TABLE ship_armament (
    Armament_ID INTEGER PRIMARY KEY,
    Ship_ID INTEGER REFERENCES naval_ships(Ship_ID),
    Mount_Type TEXT, -- 'Main Battery', 'DP Gun', 'AA Gun', 'Torpedo Tubes'
    Gun_Caliber_IN REAL,
    Gun_Count INTEGER,
    Mount_Count INTEGER,
    Gun_Model TEXT,
    Fire_Control TEXT
);
```

---

## Migration Path

### Current State → SQL Database

**Step 1: Schema Creation**
```bash
sqlite3 naval_weapons.db < COMPLETE_SQL_SCHEMA.sql
```

**Step 2: Enable Foreign Keys**
```sql
PRAGMA foreign_keys = ON;
```

**Step 3: Data Conversion Scripts**
- Use AWK/Python scripts to parse MD pipe-delimited tables
- Generate SQL INSERT statements
- Handle NULL values and special characters
- Validate data types before insertion

**Step 4: Data Import**
```bash
# Import each table (see conversion scripts in next todo)
sqlite3 naval_weapons.db < insert_torpedoes.sql
sqlite3 naval_weapons.db < insert_missiles.sql
# ... etc
```

**Step 5: Validation**
```bash
# Run validation suite
sqlite3 naval_weapons.db < validation_queries.sql > validation_report.txt
```

### SQL Database → Application Integration

**Connection String Examples**:
```python
# Python (sqlite3)
import sqlite3
conn = sqlite3.connect('naval_weapons.db')

# Python (SQLAlchemy)
from sqlalchemy import create_engine
engine = create_engine('sqlite:///naval_weapons.db')

# Node.js (better-sqlite3)
const Database = require('better-sqlite3');
const db = new Database('naval_weapons.db');

# Unity C# (Mono.Data.Sqlite)
string connectionString = "URI=file:naval_weapons.db";
IDbConnection dbConnection = new SqliteConnection(connectionString);
```

**Query Examples**:
```python
# Fetch all USA ships from Late WWII era
cursor.execute("""
    SELECT Ship_ID, Ship_Name, Ship_Class, Ship_Type
    FROM naval_ships
    WHERE Country = 'USA' AND Era = 'Late WWII'
    ORDER BY Year_Commissioned
""")
ships = cursor.fetchall()

# Get research prerequisites for Iowa-class battleships
cursor.execute("""
    SELECT Node_ID, Tech_Tier, Research_Cost_RP, Prerequisites
    FROM ship_research_tree
    WHERE Country = 'USA' AND Ship_Class = 'Iowa'
""")
tech_nodes = cursor.fetchall()
```

---

## Future Enhancements (Option C Path)

### When to Add Missing 58 Fields

**Trigger Conditions**:
1. **Modular Ship Building**: Players customize hardpoints/modules
2. **Advanced AI**: AI needs crew tier/magazine data for combat simulation
3. **Carrier Operations**: Aircraft management requires deck/hangar details
4. **Multiplayer Balance**: Granular stats needed for PvP balancing

### Incremental Addition Strategy

**Phase 1: Combat Critical** (10 fields, ~6 hours research):
- Main_Battery_Count, Main_Battery_Caliber_IN
- DP_Gun_Count, DP_Gun_Caliber_IN
- AA_Light_Count, AA_Heavy_Count
- Torpedo_Tube_Count, Torpedo_Caliber_IN
- Armor_Belt_IN, Armor_Deck_IN

**Phase 2: Operational Features** (6 fields, ~4 hours research):
- Aircraft_Capacity, Catapult_Count
- Crew_Size, Crew_Efficiency_Tier
- Magazine_Capacity_Tons, Magazine_Safety_Rating

**Phase 3: Advanced Modules** (8 fields, ~5 hours research):
- Radar_Type, Sonar_Type
- Fire_Control_System, Damage_Control_Rating
- Propulsion_Type, Engine_HP
- Fuel_Capacity_Tons, Fuel_Type

**Total Option C Timeline**: 18-20 hours (matches original estimate)

---

## Maintenance & Backup Strategy

### Regular Maintenance Tasks

**Weekly**:
```sql
-- Analyze query performance
ANALYZE;

-- Update statistics
PRAGMA optimize;
```

**Monthly**:
```sql
-- Rebuild indexes
REINDEX;

-- Defragment database
VACUUM;

-- Integrity check
PRAGMA integrity_check;
```

### Backup Strategy

**Automated Backup**:
```bash
# Full database dump (SQL format)
sqlite3 naval_weapons.db .dump > backup_$(date +%Y%m%d).sql

# Binary backup (faster, smaller)
cp naval_weapons.db backups/naval_weapons_$(date +%Y%m%d).db

# Compressed backup
sqlite3 naval_weapons.db "VACUUM INTO 'backups/naval_weapons_$(date +%Y%m%d).db'"
```

**Recovery Testing**:
```bash
# Test restore from SQL dump
sqlite3 test_restore.db < backup_20251012.sql

# Verify record counts
sqlite3 test_restore.db "SELECT COUNT(*) FROM naval_ships;"
```

---

## Troubleshooting

### Common Issues

**Issue 1: Foreign Key Constraint Violations**
```sql
-- Check for orphaned references
SELECT * FROM ship_research_tree r
LEFT JOIN naval_ships s ON r.Ship_Class = s.Ship_Class
WHERE s.Ship_ID IS NULL;

-- Fix: Either add missing ships or adjust constraint
```

**Issue 2: CHECK Constraint Violations**
```sql
-- Find records violating displacement constraint
SELECT * FROM naval_ships
WHERE Displacement_Full < Displacement_Standard;

-- Fix: Update incorrect data
UPDATE naval_ships
SET Displacement_Full = Displacement_Standard * 1.15
WHERE Displacement_Full < Displacement_Standard;
```

**Issue 3: Performance Degradation**
```sql
-- Analyze query execution plan
EXPLAIN QUERY PLAN
SELECT * FROM naval_ships WHERE Ship_Class = 'Fletcher';

-- Check for missing indexes
-- Look for "SCAN TABLE" in output (bad), want "SEARCH TABLE USING INDEX" (good)
```

**Issue 4: Database Locked Errors**
```sql
-- Check for long-running transactions
-- Set busy timeout (milliseconds)
PRAGMA busy_timeout = 5000;

-- Use Write-Ahead Logging for better concurrency
PRAGMA journal_mode = WAL;
```

### Debug Queries

```sql
-- Show database configuration
PRAGMA database_list;
PRAGMA foreign_keys;
PRAGMA journal_mode;

-- Show table sizes
SELECT
    name,
    (SELECT COUNT(*) FROM sqlite_master sm2 WHERE sm2.tbl_name = sm1.name AND sm2.type = 'index') as index_count
FROM sqlite_master sm1
WHERE type = 'table'
ORDER BY name;

-- Show schema version
SELECT * FROM schema_metadata;
```

---

## Appendix A: Full Schema Field Mapping

### naval_ships: MD → SQL Type Mapping

| MD Column | SQL Column | SQL Type | Constraints | Notes |
|-----------|------------|----------|-------------|-------|
| Ship_ID | Ship_ID | INTEGER | PRIMARY KEY, CHECK range | 12000-13999 |
| Country | Country | TEXT | NOT NULL, CHECK enum | USA/Britain/Germany/Japan |
| Ship_Name | Ship_Name | TEXT | NOT NULL | UTF-8 support |
| Ship_Class | Ship_Class | TEXT | NOT NULL | Class designation |
| Hull_Variant | Hull_Variant | TEXT | NULL allowed | Optional variant |
| Ship_Type | Ship_Type | TEXT | NOT NULL | BB/CV/CA/CL/DD/SS |
| Ship_Type_Full | Ship_Type_Full | TEXT | Auto-populated | Trigger expands abbreviation |
| Era | Era | TEXT | CHECK enum | 9 era values |
| Year_Commissioned | Year_Commissioned | INTEGER | CHECK 1860-2025 | Commission year |
| Year_Designed | Year_Designed | INTEGER | CHECK 1850-2025 | Design year |
| Year_Completed | Year_Completed | INTEGER | CHECK 1860-2025 | Completion year |
| Displacement_Standard | Displacement_Standard | REAL | CHECK > 0 | Tons (standard) |
| Displacement_Full | Displacement_Full | REAL | CHECK >= Standard | Tons (full load) |
| Max_Speed | Max_Speed | REAL | CHECK > 0 | Knots |
| Cruise_Speed | Cruise_Speed | REAL | CHECK > 0, <= Max | Knots |
| Range_NM | Range_NM | REAL | CHECK > 0 | Nautical miles |
| Cost_USD | Cost_USD | REAL | CHECK >= 0, NULL OK | US Dollars |
| Build_Time | Build_Time | REAL | CHECK > 0, NULL OK | Months |
| Modded | Modded | INTEGER | NOT NULL, DEFAULT 0 | 0=vanilla, 1=mod |
| Notes | Notes | TEXT | NULL allowed | Armament data |

---

## Appendix B: Schema Comparison

### naval_ships: Documented vs. Actual Schema

**Actual Schema (20 fields)** ✅ IMPLEMENTED:
- Ship_ID, Country, Ship_Name, Ship_Class, Hull_Variant
- Ship_Type, Ship_Type_Full, Era
- Year_Commissioned, Year_Designed, Year_Completed
- Displacement_Standard, Displacement_Full
- Max_Speed, Cruise_Speed, Range_NM
- Cost_USD, Build_Time
- Modded, Notes

**Missing from Documented Schema (58 fields)** ⏳ FUTURE:

*Combat Systems (12 fields)*:
- Main_Battery_Count, Main_Battery_Caliber_IN, Main_Battery_Configuration
- DP_Gun_Count, DP_Gun_Caliber_IN
- AA_Light_Count, AA_Medium_Count, AA_Heavy_Count
- Torpedo_Tube_Count, Torpedo_Caliber_IN
- Depth_Charge_Count, Mine_Capacity

*Armor (6 fields)*:
- Armor_Belt_IN, Armor_Deck_IN, Armor_Turret_IN
- Armor_Conning_Tower_IN, Armor_Bulkhead_IN, Torpedo_Protection_System

*Aircraft Systems (6 fields)*:
- Aircraft_Capacity, Hangar_Capacity, Flight_Deck_Length_FT
- Catapult_Count, Catapult_Type, Elevator_Count

*Crew (4 fields)*:
- Crew_Size, Crew_Officers, Crew_Efficiency_Tier, Berthing_Quality

*Propulsion (6 fields)*:
- Propulsion_Type, Engine_Count, Engine_HP_Total
- Boiler_Count, Boiler_Type, Shaft_Count

*Fuel & Endurance (4 fields)*:
- Fuel_Capacity_Tons, Fuel_Type, Endurance_Days, Provisioning_Days

*Sensors & Electronics (6 fields)*:
- Radar_Type, Radar_Range_NM, Sonar_Type
- Fire_Control_System, Electronic_Warfare_Suite, Communication_Suite

*Logistics (4 fields)*:
- Magazine_Capacity_Tons, Magazine_Safety_Rating
- Repair_Facilities, Medical_Facilities

*Hardpoints & Modules (10 fields)*:
- Hardpoint_Bow_Count, Hardpoint_Midship_Count, Hardpoint_Stern_Count
- Hardpoint_Superstructure_Count, Hardpoint_Mast_Count
- Module_Propulsion_Slot, Module_Electronics_Slot, Module_Aviation_Slot
- Module_Weapon_Slot_Primary, Module_Weapon_Slot_Secondary

**Total Missing**: 58 fields

---

## Appendix C: Quick Reference Commands

### Database Creation
```bash
# Create new database with schema
sqlite3 naval_weapons.db < COMPLETE_SQL_SCHEMA.sql

# Verify schema loaded
sqlite3 naval_weapons.db ".schema naval_ships"
```

### Data Import
```bash
# Import from conversion scripts (to be created)
sqlite3 naval_weapons.db < insert_all_data.sql

# Verify record counts
sqlite3 naval_weapons.db "SELECT COUNT(*) FROM naval_ships;"
```

### Validation
```bash
# Run validation suite
sqlite3 naval_weapons.db < validation_queries.sql

# Check cross-references
sqlite3 naval_weapons.db "SELECT * FROM v_ships_missing_research;"
```

### Backup
```bash
# Full SQL dump
sqlite3 naval_weapons.db .dump > backup.sql

# Compressed binary backup
sqlite3 naval_weapons.db "VACUUM INTO 'backup.db'"
```

### Query Examples
```sql
-- Find all Iowa-class battleships
SELECT * FROM naval_ships WHERE Ship_Class = 'Iowa';

-- Get USA Late WWII carriers
SELECT * FROM naval_ships
WHERE Country = 'USA' AND Era = 'Late WWII' AND Ship_Type LIKE 'CV%';

-- Research tree for battleships
SELECT * FROM ship_research_tree
WHERE Ship_Type = 'BB' ORDER BY Tech_Tier;
```

---

## Document Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0.0 | 2025-10-12 | Initial schema design (Option A) | Claude Code |

---

**Next Steps**: See todo list for SQL conversion script creation and data import procedures.
