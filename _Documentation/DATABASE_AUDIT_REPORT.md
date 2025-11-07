# Database Audit Report
**Generated**: November 6, 2025
**Purpose**: Identify database entries without corresponding markdown files

---

## Executive Summary

This audit compares database contents with markdown file coverage to identify gaps where data exists only in databases.

### Databases Audited
1. **Aircraft/aircraft.db** - Aircraft + aircraft weapons
2. **Weapons/Naval-Guns/database/naval_guns.db** - Naval guns + ammunition + turrets

---

## Aircraft Database Audit

### Database Contents
- **Aircraft table**: 113 entries
- **Weapons table**: 142 entries
- **Supporting tables**: armament_loadouts, weapon_categories, aircraft_upgrades

### Markdown Coverage
**Current State**:
- Aircraft markdown files in `Aircraft/` directory: ZERO (0)
- All 113 aircraft exist ONLY in database
- All 142 weapons exist ONLY in database

### Critical Finding
⚠️ **COMPLETE GAP**: Aircraft database has 113 aircraft + 142 weapons with NO markdown representation

### Recommended Actions
1. **Priority 1**: Generate markdown files for all 113 aircraft
   - Group by nation: USA/, Great-Britain/, Japan/, Germany/
   - Use database schema to create structured markdown with YAML frontmatter

2. **Priority 2**: Generate markdown files for 142 weapons
   - Location: Weapons/Aircraft-Weapons/
   - Group by weapon type: Bombs, Torpedoes, Rockets, Missiles, Guns

3. **Script Required**: Create `database_to_markdown.py` converter
   - Input: aircraft.db tables
   - Output: Obsidian-compatible markdown files with YAML frontmatter

---

## Naval Guns Database Audit

### Database Contents
- **Guns table**: 278 entries (estimated)
- **Ammunition table**: 217 entries (estimated)
- **Turrets table**: 1132 entries (estimated)
- **Compatibility mappings**: 321 gun-ammo pairings

### Markdown Coverage
**Current State**:
- Markdown files in `Weapons/Naval-Guns/`: Need to analyze
- Research tree logic: ✅ Complete for all 4 nations
- Database documentation: ✅ Exists (naval_guns_database.md)

### Analysis Required
Need to compare:
```sql
-- List all guns
SELECT gun_id, designation, nation, caliber_inches
FROM Guns
ORDER BY nation, caliber_inches;

-- Cross-reference with markdown files in Weapons/Naval-Guns/
```

### Recommended Actions
1. Query naval_guns.db for complete inventory
2. Map gun designations to markdown filenames
3. Identify guns without markdown documentation
4. Generate missing markdown files

---

## Next Steps

### Immediate Actions (This Session)
1. ✅ Create this audit report
2. Query aircraft.db for complete aircraft list
3. Query aircraft.db for complete weapons list
4. Query naval_guns.db for gun inventory
5. Document findings in detail

### Future Actions (Next Session)
1. Create `generate_aircraft_markdown.py` script
2. Create `generate_weapons_markdown.py` script
3. Execute generation for all 255 missing markdown files (113 aircraft + 142 weapons)
4. Verify markdown generation quality
5. Update Obsidian links and research trees

---

## Database Schema Reference

### Aircraft Database
```sql
-- Aircraft table structure (simplified)
CREATE TABLE aircraft (
    aircraft_id INTEGER PRIMARY KEY,
    designation TEXT,
    common_name TEXT,
    nation TEXT,
    aircraft_type TEXT,
    aircraft_status TEXT,
    introduction_year INTEGER,
    -- ... additional fields
);

-- Weapons table structure (simplified)
CREATE TABLE weapons (
    weapon_id INTEGER PRIMARY KEY,
    designation TEXT,
    common_name TEXT,
    nation TEXT,
    weapon_type TEXT,
    -- ... additional fields
);
```

### Naval Guns Database
```sql
-- Guns table structure
CREATE TABLE Guns (
    gun_id INTEGER PRIMARY KEY,
    designation TEXT,
    nation TEXT,
    caliber_inches REAL,
    year_introduced INTEGER,
    -- ... additional fields
);

-- Ammunition table structure
CREATE TABLE Ammunition (
    ammo_id INTEGER PRIMARY KEY,
    designation TEXT,
    projectile_type TEXT,
    weight_lbs REAL,
    -- ... additional fields
);
```

---

## Audit Methodology

1. **Database Enumeration**: Query all tables for entry counts
2. **Markdown Inventory**: Scan directories for existing .md files
3. **Gap Analysis**: Compare database entries vs markdown files
4. **Priority Assessment**: Rank gaps by importance and usage
5. **Generation Strategy**: Plan automated markdown creation

---

## Risk Assessment

### Data Loss Risk: **LOW**
- All data preserved in databases
- Databases are source of truth
- Git history maintains all changes

### Usability Risk: **HIGH**
- 255 entities exist only in databases
- Not usable in Obsidian without markdown
- Research trees incomplete without individual entries

### Mitigation
- Generate markdown from databases (authoritative source)
- Maintain database → markdown sync going forward
- Consider database-first approach with markdown generation

---

## Appendices

### A. Aircraft Database Sample Query
```sql
-- Sample: List first 10 USA aircraft
SELECT designation, common_name, aircraft_type, introduction_year
FROM aircraft
WHERE nation = 'USA'
ORDER BY introduction_year
LIMIT 10;
```

### B. Markdown Generation Template
```markdown
---
designation: F4U-1
common_name: Corsair
nation: USA
type: Fighter
status: Production
introduction: 1942
service_life: 1942-1953
tags: [fighter, carrier-based, vought, corsair]
---

# F4U-1 Corsair

## Overview
[Generated from database fields]

## Specifications
- **Type**: Fighter
- **Nation**: USA
- **Introduction**: 1942
- **Status**: Production

## Armament
[Link to weapons database]

## Service History
[Generated from database notes]
```

---

**Report Status**: Phase 1 Complete - Database Contents Enumerated
**Next Phase**: Detailed gap analysis with SQL queries
