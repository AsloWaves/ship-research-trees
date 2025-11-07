# SQL Conversion Implementation Guide

**Version**: 1.0.0
**Option**: A (Existing 20-field structure)
**Status**: Ready for execution
**Estimated Time**: 4-6 hours

---

## Overview

This guide provides step-by-step instructions for converting the naval weapons Markdown databases to SQL format using the automated scripts and schema provided.

**What's Included**:
- ✅ Complete SQL schema (COMPLETE_SQL_SCHEMA.sql)
- ✅ Master conversion script (convert_all_to_sql.sh)
- ✅ Individual AWK conversion scripts (2 of 7 created)
- ✅ Validation views and integrity checks
- ✅ Automated testing and reporting

**What's Still Needed**:
- ⏳ AWK conversion scripts for 5 remaining databases (missiles, naval aircraft, ground aircraft, bombs, research tree)
- ⏳ Schema line number verification for each MD file
- ⏳ Test run and validation

---

## Files Created

### Core SQL Files

| File | Purpose | Status |
|------|---------|--------|
| COMPLETE_SQL_SCHEMA.sql | Full database schema with tables, indexes, views, triggers | ✅ Complete |
| SQL_SCHEMA_DOCUMENTATION.md | Comprehensive schema documentation | ✅ Complete |
| SQL_CONVERSION_GUIDE.md | This file - implementation guide | ✅ Complete |

### Conversion Scripts

| File | Purpose | Status |
|------|---------|--------|
| convert_all_to_sql.sh | Master bash script coordinating all conversions | ✅ Complete |
| convert_ships_to_sql.awk | Ships MD → SQL conversion (959 records) | ✅ Complete |
| convert_torpedoes_to_sql.awk | Torpedoes MD → SQL conversion (~120 records) | ✅ Complete |
| convert_missiles_to_sql.awk | Missiles MD → SQL conversion (~180 records) | ⏳ TODO |
| convert_naval_aircraft_to_sql.awk | Naval aircraft MD → SQL conversion (~250 records) | ⏳ TODO |
| convert_ground_aircraft_to_sql.awk | Ground aircraft MD → SQL conversion (~280 records) | ⏳ TODO |
| convert_bombs_to_sql.awk | Bombs MD → SQL conversion (~200 records) | ⏳ TODO |
| convert_research_tree_to_sql.awk | Research tree MD → SQL conversion (~675 records) | ⏳ TODO |

---

## Prerequisites

### Software Requirements

**Required**:
- SQLite 3.x (`sqlite3` command-line tool)
- GNU AWK 4.x+ (`gawk` or `awk`)
- Bash 4.x+ (Unix shell)

**Optional but Recommended**:
- Git (for version control and backups)
- DB Browser for SQLite (GUI database viewer)
- Python 3.x (for future armament parsing)

### Installation Verification

```bash
# Check SQLite version
sqlite3 --version
# Expected: 3.x.x or higher

# Check AWK version
awk --version
# Expected: GNU Awk 4.x.x or higher

# Check Bash version
bash --version
# Expected: 4.x.x or higher
```

### Windows Compatibility

If running on Windows:
- Install Git Bash (includes bash, awk, sqlite3)
- Or use WSL (Windows Subsystem for Linux)
- Or use Cygwin with required packages

---

## Conversion Process

### Phase 1: Preparation (Estimated: 30 minutes)

**Step 1.1: Verify all MD files are present**

```bash
cd /d/Research/naval-weapons/database

# Check for all 7 MD files
ls -lh *.md | grep database

# Expected files:
# - naval_torpedoes_database.md
# - naval_missiles_database.md
# - naval_aircraft_database.md
# - ground_aircraft_database.md
# - naval_bombs_database.md
# - naval_ships_database.md
# - ship_research_tree_database.md
```

**Step 1.2: Verify schema and scripts are present**

```bash
# Check core files
ls -lh COMPLETE_SQL_SCHEMA.sql
ls -lh convert_all_to_sql.sh
ls -lh convert_*_to_sql.awk
```

**Step 1.3: Make scripts executable**

```bash
chmod +x convert_all_to_sql.sh
chmod +x convert_*.awk
```

**Step 1.4: Create backup of MD files**

```bash
# Create backup directory
mkdir -p md_backups

# Backup all MD files
cp *_database.md md_backups/
echo "Backup created: $(date)" > md_backups/BACKUP_LOG.txt
```

### Phase 2: Complete Remaining AWK Scripts (Estimated: 2-3 hours)

**Why These Are Still Needed**:
The conversion process requires 7 AWK scripts (one per database). Currently, only 2 are complete:
- ✅ convert_ships_to_sql.awk (959 records, 20 fields)
- ✅ convert_torpedoes_to_sql.awk (~120 records, 18 fields)

**Remaining Scripts** (follow torpedo template):
- ⏳ convert_missiles_to_sql.awk (~180 records, 17 fields)
- ⏳ convert_naval_aircraft_to_sql.awk (~250 records, 19 fields)
- ⏳ convert_ground_aircraft_to_sql.awk (~280 records, 19 fields)
- ⏳ convert_bombs_to_sql.awk (~200 records, 23 fields)
- ⏳ convert_research_tree_to_sql.awk (~675 records, 18 fields)

**Template Approach**:
Each AWK script follows the same pattern as `convert_torpedoes_to_sql.awk`:
1. Set field separator to pipe (`FS = "|"`)
2. Skip header rows (usually first 2-3 lines)
3. Extract and trim all fields
4. Build INSERT statement with proper NULL handling
5. Escape single quotes and special characters
6. Print statistics on completion

**Key Differences Per Database**:
- Number of fields varies (17-23 fields)
- Column positions may differ based on MD file structure
- Data row start line may vary (need to verify)

**Creation Steps Per Script**:
1. Open corresponding MD file and identify data start line
2. Count total fields in actual data (not documented schema)
3. Copy convert_torpedoes_to_sql.awk as template
4. Adjust field count and column extractions
5. Update INSERT statement field list
6. Test with first 10 rows

**Verification Method**:
```bash
# Test AWK script on first 10 data rows
awk -f convert_missiles_to_sql.awk naval_missiles_database.md | head -20

# Check for:
# - Valid INSERT statements
# - No AWK errors
# - Proper NULL handling
# - Correct field count
```

### Phase 3: Schema Verification (Estimated: 30 minutes)

**Step 3.1: Verify data row start lines**

Each MD file has a different structure. Need to identify where actual data rows begin:

```bash
# Ships database - currently set to line 884
grep -n "^\| [0-9]" naval_ships_database.md | head -1

# Torpedoes database - currently set to line 3
grep -n "^\| [0-9]" naval_torpedoes_database.md | head -1

# Repeat for each database and update AWK scripts
```

**Step 3.2: Verify field counts match schema**

```bash
# Extract first data row and count fields
awk -F'|' 'NR==884 {print NF}' naval_ships_database.md
# Expected: 22 fields (leading/trailing pipes create empty fields)

# Actual data fields = NF - 2 (subtract empty first and last)
# Ships: 22 - 2 = 20 fields ✅
```

**Step 3.3: Test schema creation**

```bash
# Create test database
sqlite3 test.db < COMPLETE_SQL_SCHEMA.sql

# Verify tables created
sqlite3 test.db ".tables"
# Expected: 7 tables

# Verify indexes created
sqlite3 test.db "SELECT COUNT(*) FROM sqlite_master WHERE type='index';"
# Expected: ~30 indexes

# Verify views created
sqlite3 test.db "SELECT COUNT(*) FROM sqlite_master WHERE type='view';"
# Expected: 5 views

# Cleanup
rm test.db
```

### Phase 4: Conversion Execution (Estimated: 30 minutes)

**Step 4.1: Dry run (test mode)**

```bash
# Run conversion without database creation
./convert_all_to_sql.sh --dry-run

# This will:
# - Generate all *_insert.sql files
# - Show conversion statistics
# - NOT create database yet
```

**Step 4.2: Review generated SQL**

```bash
# Check ships insert file
head -50 naval_ships_database_insert.sql

# Verify:
# - INSERT statements are well-formed
# - Data looks correct
# - NULL handling is proper
# - No syntax errors
```

**Step 4.3: Full conversion**

```bash
# Run full conversion
./convert_all_to_sql.sh

# Expected output:
# [1/7] Backing up existing database... (if exists)
# [2/7] Creating database schema... ✓
# [3/7] Converting MD files to SQL... ✓
# [4/7] Importing data into database... ✓
# [5/7] Verifying data import... ✓
# [6/7] Running validation checks... ✓
# [7/7] Optimizing database... ✓
```

**Step 4.4: Monitor conversion progress**

```bash
# Watch conversion in real-time
tail -f conversion.log

# Check for errors
grep -i "error\|fail" conversion.log
```

### Phase 5: Validation (Estimated: 1 hour)

**Step 5.1: Automatic validation**

The conversion script automatically runs these checks:
- ✅ Record count verification
- ✅ Duplicate ID detection
- ✅ NULL constraint validation
- ✅ Cross-reference checks
- ✅ Data completeness by nation
- ✅ Logical consistency checks

**Step 5.2: Manual validation queries**

```bash
# Connect to database
sqlite3 naval_weapons.db

# Check total records
SELECT
    (SELECT COUNT(*) FROM naval_torpedoes) +
    (SELECT COUNT(*) FROM naval_missiles) +
    (SELECT COUNT(*) FROM naval_aircraft) +
    (SELECT COUNT(*) FROM ground_aircraft) +
    (SELECT COUNT(*) FROM naval_bombs) +
    (SELECT COUNT(*) FROM naval_ships) +
    (SELECT COUNT(*) FROM ship_research_tree) as Total_Records;
-- Expected: ~2664 records

# Check for orphaned ships (ships without research entries)
SELECT * FROM v_ships_missing_research LIMIT 10;

# Check for orphaned research (research without ships)
SELECT * FROM v_research_missing_ships LIMIT 10;

# Verify data completeness
SELECT * FROM v_data_completeness_by_nation;
-- Expected: All nations >95% complete
```

**Step 5.3: Sample data verification**

```bash
# Verify Fletcher-class destroyer data
SELECT * FROM naval_ships WHERE Ship_Class = 'Fletcher' LIMIT 5;

# Verify Iowa-class research tree
SELECT * FROM ship_research_tree WHERE Ship_Class = 'Iowa';

# Verify Mark 14 torpedo
SELECT * FROM naval_torpedoes WHERE Torpedo_Name LIKE '%Mark 14%';
```

**Step 5.4: Review validation report**

```bash
# Open generated validation report
cat validation_report_*.txt

# Check for warnings
grep -i "warning\|error\|fail" validation_report_*.txt
```

### Phase 6: Testing and Optimization (Estimated: 30 minutes)

**Step 6.1: Query performance testing**

```bash
sqlite3 naval_weapons.db <<EOF
.timer on

-- Test indexed queries (should be fast)
SELECT COUNT(*) FROM naval_ships WHERE Country = 'USA';
SELECT * FROM naval_ships WHERE Ship_Class = 'Fletcher';

-- Test full table scans (slower but acceptable)
SELECT * FROM naval_ships WHERE Displacement_Standard > 50000;

-- Test complex joins (validation)
SELECT s.Ship_Name, r.Tech_Tier, r.Research_Cost_RP
FROM naval_ships s
JOIN ship_research_tree r ON s.Ship_Class = r.Ship_Class
WHERE s.Country = 'USA' AND s.Era = 'Late WWII'
LIMIT 10;

.quit
EOF
```

**Step 6.2: Database optimization**

```bash
sqlite3 naval_weapons.db <<EOF
-- Update query planner statistics
ANALYZE;

-- Rebuild all indexes
REINDEX;

-- Compact database
VACUUM;

.quit
EOF
```

**Step 6.3: Backup optimized database**

```bash
# Create production backup
mkdir -p production
cp naval_weapons.db production/naval_weapons_v1.0.0_$(date +%Y%m%d).db

# Create SQL dump for version control
sqlite3 naval_weapons.db .dump > production/naval_weapons_v1.0.0.sql

# Compress for archival
tar -czf production/naval_weapons_v1.0.0.tar.gz naval_weapons.db
```

---

## Validation Checklist

Use this checklist to ensure conversion completed successfully:

### Pre-Conversion

- [ ] All 7 MD files present and readable
- [ ] Schema file (COMPLETE_SQL_SCHEMA.sql) verified
- [ ] All 7 AWK conversion scripts created
- [ ] Scripts are executable (chmod +x)
- [ ] Backup of MD files created

### Conversion

- [ ] Schema creation completed without errors
- [ ] All 7 MD files converted to SQL
- [ ] All 7 SQL files imported successfully
- [ ] Total record count matches expectations (~2664)
- [ ] No duplicate ID violations
- [ ] No NULL constraint violations

### Data Quality

- [ ] Ships: ~959 records imported
- [ ] Torpedoes: ~120 records imported
- [ ] Missiles: ~180 records imported
- [ ] Naval Aircraft: ~250 records imported
- [ ] Ground Aircraft: ~280 records imported
- [ ] Bombs: ~200 records imported
- [ ] Research Tree: ~675 records imported
- [ ] Data completeness >99% for ships
- [ ] All nations represented (USA, Britain, Germany, Japan)

### Cross-References

- [ ] Ships <→ Research Tree links validated
- [ ] No critical orphaned records
- [ ] Tech tree progression is continuous (no gaps in tiers)
- [ ] All starting techs flagged correctly

### Performance

- [ ] Indexed queries execute in <100ms
- [ ] Full table scans complete in <1s
- [ ] Complex joins execute in <500ms
- [ ] Database size is reasonable (~2-5 MB)

### Documentation

- [ ] Validation report generated and reviewed
- [ ] Schema documentation accessible
- [ ] Conversion guide followed completely
- [ ] Backup strategy implemented

---

## Troubleshooting

### Issue: AWK script fails with "backslash not last character"

**Cause**: Windows bash shell mishandling AWK escape sequences

**Solution**:
```bash
# Use separate AWK script files instead of inline commands
# Already implemented in our scripts

# If issue persists, try:
dos2unix convert_*.awk  # Convert line endings
```

### Issue: SQLite reports "foreign key constraint failed"

**Cause**: Referenced records don't exist in parent table

**Solution**:
```bash
# Disable foreign keys temporarily
sqlite3 naval_weapons.db "PRAGMA foreign_keys = OFF;"

# Re-import data

# Re-enable foreign keys
sqlite3 naval_weapons.db "PRAGMA foreign_keys = ON;"

# Identify orphaned records
SELECT * FROM v_ships_missing_research;
SELECT * FROM v_research_missing_ships;
```

### Issue: Duplicate ID errors during import

**Cause**: MD file contains duplicate IDs or ID range overlaps

**Solution**:
```bash
# Find duplicates in MD file
awk -F'|' 'NR>=884 && /^\| [0-9]/ {id=$2; gsub(/^[ \t]+|[ \t]+$/, "", id); print id}' \
  naval_ships_database.md | sort | uniq -d

# Update IDs in MD file before re-import
```

### Issue: Record count mismatch after import

**Cause**: AWK script skipped malformed rows or data start line incorrect

**Solution**:
```bash
# Check AWK script output line count
awk -f convert_ships_to_sql.awk naval_ships_database.md | grep -c "^INSERT INTO"

# Compare to expected count from MD file
grep -c "^\| [0-9]" naval_ships_database.md

# Adjust NR threshold in AWK script if needed
```

### Issue: Notes field contains malformed text

**Cause**: Special characters not properly escaped

**Solution**:
```bash
# Check sql_escape() function in AWK scripts
# Ensure single quotes are doubled: ' → ''
# Ensure control characters are removed

# Test problematic record
awk -F'|' 'NR==1234' naval_ships_database.md
```

### Issue: Database size unexpectedly large

**Cause**: Not vacuumed after import, or indexes not optimized

**Solution**:
```bash
sqlite3 naval_weapons.db <<EOF
-- Compact database
VACUUM;

-- Update statistics
ANALYZE;

-- Check size
.dbinfo
.quit
EOF
```

---

## Post-Conversion Tasks

### Immediate (Required)

1. **Test database in target application**
   - Load database from application code
   - Verify all tables accessible
   - Test sample queries
   - Validate data integrity

2. **Create application layer**
   - Implement Notes field armament parser (Python/JavaScript)
   - Create data access layer (DAO/Repository pattern)
   - Build query abstractions for common operations
   - Add caching layer for frequently accessed data

3. **Set up version control**
   - Add naval_weapons.db to .gitignore (binary file)
   - Commit SQL schema file (COMPLETE_SQL_SCHEMA.sql)
   - Commit conversion scripts (*_to_sql.awk, convert_all_to_sql.sh)
   - Commit documentation (*.md files)

### Short-Term (1-2 weeks)

1. **Implement Notes field parsing**
   - Write regex patterns for armament extraction
   - Test against all 959 ship Notes fields
   - Store parsed data in JSON columns or normalized tables
   - Create views combining base stats + parsed armament

2. **Add missing metadata**
   - Research and populate missing Cost_USD (87 ships, 10%)
   - Research and populate missing Build_Time (94 ships, 11%)
   - Use class averages or estimation formulas

3. **Create additional indexes**
   - Add composite indexes based on query patterns
   - Example: CREATE INDEX idx_ships_country_era ON naval_ships(Country, Era);
   - Example: CREATE INDEX idx_ships_type_tier ON naval_ships(Ship_Type, Tech_Tier);

### Long-Term (Optional - Option C Evolution)

1. **Add advanced combat fields** (Phase 1: 10 fields, ~6 hours)
   - Main_Battery_Count, Main_Battery_Caliber_IN
   - DP_Gun_Count, DP_Gun_Caliber_IN
   - AA_Light_Count, AA_Heavy_Count
   - Torpedo_Tube_Count, Torpedo_Caliber_IN
   - Armor_Belt_IN, Armor_Deck_IN

2. **Add operational fields** (Phase 2: 6 fields, ~4 hours)
   - Aircraft_Capacity, Catapult_Count
   - Crew_Size, Crew_Efficiency_Tier
   - Magazine_Capacity_Tons, Magazine_Safety_Rating

3. **Add module system** (Phase 3: 8 fields, ~5 hours)
   - Radar_Type, Sonar_Type
   - Fire_Control_System, Damage_Control_Rating
   - Propulsion_Type, Engine_HP
   - Fuel_Capacity_Tons, Fuel_Type

**Total Option C Timeline**: 18-20 hours (matches original estimate)

---

## Appendix A: Expected Record Counts

| Database | Expected Records | ID Range | Notes |
|----------|-----------------|----------|-------|
| Torpedoes | ~120 | 1000-1399 | May vary by ±10% |
| Missiles | ~180 | 2000-2499 | Modern weapons |
| Naval Aircraft | ~250 | 3000-3499 | Carrier-based only |
| Ground Aircraft | ~280 | 4000-4499 | Land-based strike aircraft |
| Bombs | ~200 | 5000-5499 | All air-dropped ordnance |
| Ships | 959 | 12000-13999 | Confirmed exact count |
| Research Tree | ~675 | 20000-21999 | 204 research nodes + prerequisites/unlocks |
| **Total** | **~2664** | | ±50 records variation acceptable |

---

## Appendix B: Command Reference

### SQLite Commands

```bash
# Create database from schema
sqlite3 naval_weapons.db < COMPLETE_SQL_SCHEMA.sql

# Import SQL data
sqlite3 naval_weapons.db < insert_data.sql

# List all tables
sqlite3 naval_weapons.db ".tables"

# Show table schema
sqlite3 naval_weapons.db ".schema naval_ships"

# Export to SQL dump
sqlite3 naval_weapons.db ".dump" > export.sql

# Compact database
sqlite3 naval_weapons.db "VACUUM;"

# Database info
sqlite3 naval_weapons.db ".dbinfo"

# Enable column mode
sqlite3 naval_weapons.db ".mode column" ".headers on"

# Run query from file
sqlite3 naval_weapons.db < query.sql
```

### AWK Commands

```bash
# Run AWK conversion script
awk -f convert_ships_to_sql.awk naval_ships_database.md > insert_ships.sql

# Test AWK script on first 10 rows
awk -f convert_ships_to_sql.awk naval_ships_database.md | head -30

# Count INSERT statements generated
awk -f convert_ships_to_sql.awk naval_ships_database.md | grep -c "^INSERT INTO"

# Check for AWK errors
awk -f convert_ships_to_sql.awk naval_ships_database.md 2>&1 | grep -i error
```

### Bash Commands

```bash
# Make script executable
chmod +x convert_all_to_sql.sh

# Run conversion script
./convert_all_to_sql.sh

# Run in background with logging
nohup ./convert_all_to_sql.sh > conversion.log 2>&1 &

# Monitor progress
tail -f conversion.log

# Check exit status
echo $?  # 0 = success, non-zero = error
```

---

## Appendix C: Next Steps Summary

### Current Status
- ✅ Complete SQL schema designed (20-field Option A)
- ✅ Master conversion script created (convert_all_to_sql.sh)
- ✅ 2 of 7 AWK scripts completed (ships, torpedoes)
- ⏳ 5 AWK scripts remaining (missiles, naval aircraft, ground aircraft, bombs, research tree)

### Immediate Next Steps (in order)
1. Create remaining 5 AWK conversion scripts (2-3 hours)
2. Verify data row start lines for all 7 MD files (30 minutes)
3. Test each AWK script with first 10 rows (30 minutes)
4. Run full conversion with convert_all_to_sql.sh (30 minutes)
5. Validate record counts and cross-references (1 hour)
6. Test database in target application (1 hour)

**Total Estimated Time**: 4-6 hours to complete SQL conversion

### Dependencies
- No external dependencies
- All required files are present except 5 AWK scripts
- AWK scripts can be created by following torpedo template

### Success Criteria
- ✅ ~2664 total records imported
- ✅ Zero duplicate ID violations
- ✅ Zero NULL constraint violations
- ✅ Ships: 99.20% data completeness maintained
- ✅ Cross-references validated (ships ↔ research tree)
- ✅ Query performance <100ms for indexed lookups
- ✅ Database size ~2-5 MB

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-12
**Next Review**: After completing remaining AWK scripts
