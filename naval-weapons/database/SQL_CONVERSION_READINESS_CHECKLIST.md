# SQL Conversion Readiness Checklist

**Date**: 2025
**Status**: Pre-Conversion Validation Phase

## Database Inventory

### Weapon Systems Databases

| Database File | Entries | Size | ID Range | Status |
|--------------|---------|------|----------|--------|
| naval_ships_database.md | 959 | 275 KB | Various | ⏳ To Review |
| naval_torpedoes_database.md | 236 | 54 KB | 1000-1399 | ⏳ To Review |
| naval_missiles_database.md | 192 | 54 KB | 2000-2499 | ⏳ To Review |
| naval_aircraft_database.md | 144 | 38 KB | 3000-3499 | ⏳ To Review |
| ground_aircraft_database.md | 147 | 44 KB | 4000-4499 | ⏳ To Review |
| naval_bombs_database.md | 107 | 29 KB | 9000-9499 | ⏳ To Review |
| **TOTAL** | **1,785** | **494 KB** | - | - |

### Research Tree Database

| Database File | Entries | Size | Status |
|--------------|---------|------|--------|
| ship_research_tree_database.md | ~2,070 | TBD | ⏳ To Review |

## Validation Checklist

### 1. Schema Consistency ⏳

**Task**: Verify all databases have consistent field structures

- [ ] Check column count consistency
- [ ] Verify field naming conventions
- [ ] Check data type compatibility
- [ ] Identify nullable vs. non-nullable fields
- [ ] Check for special characters or encoding issues

### 2. Data Quality ⏳

**Task**: Sample entries from each database for quality validation

- [ ] Torpedoes: Check 5-10 random entries
- [ ] Missiles: Check 5-10 random entries
- [ ] Naval Aircraft: Check 5-10 random entries
- [ ] Ground Aircraft: Check 5-10 random entries
- [ ] Bombs: Check 5-10 random entries
- [ ] Ships: Check 5-10 random entries

**Validation Points**:
- No empty required fields
- Numeric fields contain valid numbers
- Text fields properly escaped
- Date/year fields in valid range
- Foreign key references valid

### 3. ID Range Validation ⏳

**Task**: Verify no ID conflicts across systems

- [ ] Torpedoes: 1000-1399 (check for overlaps)
- [ ] Missiles: 2000-2499 (check for overlaps)
- [ ] Naval Aircraft: 3000-3499 (check for overlaps)
- [ ] Ground Aircraft: 4000-4499 (check for overlaps)
- [ ] Ships/Carriers: 5000-8999 (check for overlaps)
- [ ] Bombs: 9000-9499 (check for overlaps)

### 4. Cross-Reference Validation ⏳

**Task**: Verify research tree dependencies are valid

- [ ] Check Requires_Tech_IDs point to existing nodes
- [ ] Check Unlocks_Tech_IDs point to existing nodes
- [ ] Verify no circular dependencies
- [ ] Check orphaned nodes (no path from starting tech)

### 5. Field-Specific Validation ⏳

**Task**: Validate specific field types

**Numeric Fields**:
- [ ] Weight/Displacement > 0
- [ ] Year between 1900-2025
- [ ] Speed > 0
- [ ] Range > 0
- [ ] Cost >= 0

**Text Fields**:
- [ ] No SQL injection characters (', ", ;)
- [ ] No unescaped special characters
- [ ] Consistent naming conventions
- [ ] No trailing/leading whitespace

**Boolean/Flag Fields**:
- [ ] Modded: 0 or 1 only
- [ ] Is_Starting_Tech: 0 or 1 only

### 6. Completeness Check ⏳

**Task**: Ensure all planned data is present

- [ ] All nations represented (USA, British, German, Japanese)
- [ ] All eras covered (1940-2025)
- [ ] All weapon types included
- [ ] No gaps in progression trees

### 7. SQL Schema Design ⏳

**Task**: Design SQL table structures

**Tables Needed**:
- [ ] ships (naval_ships_database)
- [ ] torpedoes (naval_torpedoes_database)
- [ ] missiles (naval_missiles_database)
- [ ] naval_aircraft (naval_aircraft_database)
- [ ] ground_aircraft (ground_aircraft_database)
- [ ] bombs (naval_bombs_database)
- [ ] research_tree (ship_research_tree_database)
- [ ] nations (lookup table)
- [ ] weapon_types (lookup table)

**Relationships**:
- [ ] Define foreign keys
- [ ] Define indexes for performance
- [ ] Define constraints (unique, not null, check)

### 8. Conversion Script Planning ⏳

**Task**: Plan conversion approach

**Options**:
1. AWK scripts (similar to existing converters)
2. Python scripts (more flexible)
3. Direct SQL INSERT statements
4. CSV intermediate format + SQL LOAD

**Considerations**:
- [ ] Handle escape characters
- [ ] Handle NULL values
- [ ] Handle multi-line text fields
- [ ] Transaction handling
- [ ] Error recovery

## Issues Log

### Critical Issues 🚨
*None identified yet*

### Warnings ⚠️
*None identified yet*

### Notes 📝
*Add notes during validation*

## Next Steps

1. **Complete Validation** (Steps 1-6 above)
2. **Design SQL Schema** (Step 7)
3. **Create Conversion Scripts** (Step 8)
4. **Test Conversion** (small dataset)
5. **Full Conversion** (all data)
6. **Verification** (compare counts, spot checks)
7. **Indexing & Optimization** (performance tuning)

## Sign-Off

- [ ] Data validation complete
- [ ] Schema design approved
- [ ] Conversion scripts tested
- [ ] Ready for SQL conversion

---

**Next Action**: Start with Step 1 - Schema Consistency Check
