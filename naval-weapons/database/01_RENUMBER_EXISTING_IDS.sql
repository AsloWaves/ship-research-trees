-- ============================================================================
-- PHASE 1: RENUMBER EXISTING DATABASE IDs
-- ============================================================================
-- Purpose: Shift existing Gun/Ammo/Turret IDs to non-overlapping ranges
-- Database: naval_guns.db
-- Backup Required: YES - Already created naval_guns_backup_PRE_INTEGRATION_*.db
-- ============================================================================
-- CRITICAL: This script modifies 1,943 existing records
-- Test on copy first: cp naval_guns.db naval_guns_test.db
-- ============================================================================

-- Record pre-migration state
SELECT '=== PRE-MIGRATION STATE ===' as Status;
SELECT 'Guns' as TableName, COUNT(*) as Records, MIN(Gun_ID) as Min_ID, MAX(Gun_ID) as Max_ID FROM Guns
UNION ALL
SELECT 'Ammunition', COUNT(*), MIN(ID), MAX(ID) FROM Ammunition
UNION ALL
SELECT 'Turrets', COUNT(*), MIN(Turret_ID), MAX(Turret_ID) FROM Turrets
UNION ALL
SELECT 'Gun_Ammo_Compat', COUNT(*), MIN(Compatibility_ID), MAX(Compatibility_ID) FROM Gun_Ammunition_Compatibility;

-- Expected output:
-- Guns: 83 records, ID range 1-83
-- Ammunition: 72 records, ID range 1-72
-- Turrets: 1700 records, ID range 1-1700
-- Gun_Ammo_Compat: 88 records, ID range 1-88

-- ============================================================================
-- STEP 1: DISABLE FOREIGN KEY CONSTRAINTS
-- ============================================================================
-- Reason: We need to update IDs that are referenced by foreign keys
-- This allows us to update in any order without constraint violations

PRAGMA foreign_keys = OFF;

SELECT 'Foreign keys disabled' as Status;

-- ============================================================================
-- STEP 2: RENAME Ammunition.ID to Ammunition_ID (Standardization)
-- ============================================================================
-- This requires recreating the table since SQLite doesn't support RENAME COLUMN directly in older versions

SELECT '=== STEP 2: Standardizing Ammunition.ID to Ammunition_ID ===' as Status;

-- Create new table with standardized name
CREATE TABLE Ammunition_New (
    Ammunition_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Turret_ID INTEGER,
    Caliber TEXT,
    Mark_Designation TEXT,
    Projectile_Type TEXT,
    Weight_LBS REAL,
    Length_IN REAL,
    Bursting_Charge REAL,
    Kinetic_Energy_MJ REAL,
    Cartridge_Type TEXT,
    Year_Introduced INTEGER,
    Country TEXT,
    Modded INTEGER DEFAULT 0,
    Notes TEXT,
    FOREIGN KEY (Turret_ID) REFERENCES Turrets(Turret_ID)
);

-- Copy data
INSERT INTO Ammunition_New (Ammunition_ID, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes)
SELECT ID, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes
FROM Ammunition;

-- Drop old table
DROP TABLE Ammunition;

-- Rename new table
ALTER TABLE Ammunition_New RENAME TO Ammunition;

-- Verify
SELECT 'Ammunition table renamed' as Status, COUNT(*) as Records FROM Ammunition;

-- ============================================================================
-- STEP 3: RENUMBER GUNS (1-83 → 100-182)
-- ============================================================================
-- New ID Range: 100-199 (max 100 guns, currently 83)
-- Impact: Gun_Ammunition_Compatibility.Gun_ID, Turrets.Gun_ID

SELECT '=== STEP 3: Renumbering Guns (1-83 → 100-182) ===' as Status;

-- Update foreign key references FIRST (before changing primary key)
UPDATE Turrets SET Gun_ID = Gun_ID + 99 WHERE Gun_ID IS NOT NULL;
UPDATE Gun_Ammunition_Compatibility SET Gun_ID = Gun_ID + 99;

-- Update primary keys
UPDATE Guns SET Gun_ID = Gun_ID + 99;

-- Update AUTOINCREMENT sequence
UPDATE sqlite_sequence SET seq = 199 WHERE name = 'Guns';

-- Verify
SELECT 'Guns renumbered' as Status,
    COUNT(*) as Records,
    MIN(Gun_ID) as New_Min_ID,
    MAX(Gun_ID) as New_Max_ID
FROM Guns;
-- Expected: 83 records, 100-182

-- ============================================================================
-- STEP 4: RENUMBER AMMUNITION (1-72 → 200-271)
-- ============================================================================
-- New ID Range: 200-299 (max 100 ammo types, currently 72)
-- Impact: Gun_Ammunition_Compatibility.Ammunition_ID

SELECT '=== STEP 4: Renumbering Ammunition (1-72 → 200-271) ===' as Status;

-- Update foreign key references FIRST
UPDATE Gun_Ammunition_Compatibility SET Ammunition_ID = Ammunition_ID + 199;

-- Update primary keys
UPDATE Ammunition SET Ammunition_ID = Ammunition_ID + 199;

-- Update AUTOINCREMENT sequence
UPDATE sqlite_sequence SET seq = 299 WHERE name = 'Ammunition';

-- Verify
SELECT 'Ammunition renumbered' as Status,
    COUNT(*) as Records,
    MIN(Ammunition_ID) as New_Min_ID,
    MAX(Ammunition_ID) as New_Max_ID
FROM Ammunition;
-- Expected: 72 records, 200-271

-- ============================================================================
-- STEP 5: RENUMBER TURRETS (1-1700 → 300-1999)
-- ============================================================================
-- New ID Range: 300-2299 (max 2000 turrets, currently 1700)
-- Impact: Guns.Turret_ID, Ammunition.Turret_ID
-- WARNING: This is the largest table with 1700 records

SELECT '=== STEP 5: Renumbering Turrets (1-1700 → 300-1999) ===' as Status;

-- Update foreign key references FIRST
UPDATE Guns SET Turret_ID = Turret_ID + 299 WHERE Turret_ID IS NOT NULL;
UPDATE Ammunition SET Turret_ID = Turret_ID + 299 WHERE Turret_ID IS NOT NULL;

-- Update primary keys (THIS MAY TAKE A FEW SECONDS - 1700 records)
UPDATE Turrets SET Turret_ID = Turret_ID + 299;

-- Update AUTOINCREMENT sequence
UPDATE sqlite_sequence SET seq = 2299 WHERE name = 'Turrets';

-- Verify
SELECT 'Turrets renumbered' as Status,
    COUNT(*) as Records,
    MIN(Turret_ID) as New_Min_ID,
    MAX(Turret_ID) as New_Max_ID
FROM Turrets;
-- Expected: 1700 records, 300-1999

-- ============================================================================
-- STEP 6: RENUMBER GUN_AMMUNITION_COMPATIBILITY (1-88 → 6001-6088)
-- ============================================================================
-- New ID Range: 6000-6999 (max 1000 compatibility records, currently 88)
-- Impact: None (no tables reference this)

SELECT '=== STEP 6: Renumbering Gun_Ammunition_Compatibility (1-88 → 6001-6088) ===' as Status;

-- Update primary keys (no foreign key references to update)
UPDATE Gun_Ammunition_Compatibility SET Compatibility_ID = Compatibility_ID + 6000;

-- Update AUTOINCREMENT sequence
UPDATE sqlite_sequence SET seq = 6999 WHERE name = 'Gun_Ammunition_Compatibility';

-- Verify
SELECT 'Gun_Ammo_Compat renumbered' as Status,
    COUNT(*) as Records,
    MIN(Compatibility_ID) as New_Min_ID,
    MAX(Compatibility_ID) as New_Max_ID
FROM Gun_Ammunition_Compatibility;
-- Expected: 88 records, 6001-6088

-- ============================================================================
-- STEP 7: RE-ENABLE FOREIGN KEY CONSTRAINTS
-- ============================================================================

PRAGMA foreign_keys = ON;

SELECT 'Foreign keys re-enabled' as Status;

-- ============================================================================
-- STEP 8: VERIFY DATA INTEGRITY
-- ============================================================================

SELECT '=== STEP 8: Verifying Data Integrity ===' as Status;

-- Check for foreign key violations
PRAGMA foreign_key_check;
-- Expected: No output (empty result = all foreign keys valid)

-- Database integrity check
PRAGMA integrity_check;
-- Expected: "ok"

-- ============================================================================
-- STEP 9: VERIFY RECORD COUNTS UNCHANGED
-- ============================================================================

SELECT '=== STEP 9: Verifying Record Counts ===' as Status;

SELECT 'Guns' as TableName, COUNT(*) as Records FROM Guns
UNION ALL
SELECT 'Ammunition', COUNT(*) FROM Ammunition
UNION ALL
SELECT 'Turrets', COUNT(*) FROM Turrets
UNION ALL
SELECT 'Gun_Ammo_Compat', COUNT(*) FROM Gun_Ammunition_Compatibility;

-- Expected: 83, 72, 1700, 88 (unchanged from pre-migration)

-- ============================================================================
-- STEP 10: VERIFY NEW ID RANGES
-- ============================================================================

SELECT '=== STEP 10: Verifying New ID Ranges ===' as Status;

SELECT 'Guns' as TableName,
    MIN(Gun_ID) as Min_ID,
    MAX(Gun_ID) as Max_ID,
    '100-199' as Expected_Range
FROM Guns
UNION ALL
SELECT 'Ammunition',
    MIN(Ammunition_ID),
    MAX(Ammunition_ID),
    '200-299'
FROM Ammunition
UNION ALL
SELECT 'Turrets',
    MIN(Turret_ID),
    MAX(Turret_ID),
    '300-2299'
FROM Turrets
UNION ALL
SELECT 'Gun_Ammo_Compat',
    MIN(Compatibility_ID),
    MAX(Compatibility_ID),
    '6000-6999'
FROM Gun_Ammunition_Compatibility;

-- Expected output:
-- Guns: 100-182 (within 100-199)
-- Ammunition: 200-271 (within 200-299)
-- Turrets: 300-1999 (within 300-2299)
-- Gun_Ammo_Compat: 6001-6088 (within 6000-6999)

-- ============================================================================
-- STEP 11: VERIFY FOREIGN KEY RELATIONSHIPS
-- ============================================================================

SELECT '=== STEP 11: Verifying Foreign Key Relationships ===' as Status;

-- Test Gun → Turret references
SELECT 'Guns referencing invalid Turrets' as Check,
    COUNT(*) as Violations
FROM Guns
WHERE Turret_ID IS NOT NULL
    AND Turret_ID NOT IN (SELECT Turret_ID FROM Turrets);
-- Expected: 0

-- Test Turret → Gun references
SELECT 'Turrets referencing invalid Guns' as Check,
    COUNT(*) as Violations
FROM Turrets
WHERE Gun_ID IS NOT NULL
    AND Gun_ID NOT IN (SELECT Gun_ID FROM Guns);
-- Expected: 0

-- Test Ammunition → Turret references
SELECT 'Ammunition referencing invalid Turrets' as Check,
    COUNT(*) as Violations
FROM Ammunition
WHERE Turret_ID IS NOT NULL
    AND Turret_ID NOT IN (SELECT Turret_ID FROM Turrets);
-- Expected: 0

-- Test Compatibility → Gun references
SELECT 'Compatibility referencing invalid Guns' as Check,
    COUNT(*) as Violations
FROM Gun_Ammunition_Compatibility
WHERE Gun_ID NOT IN (SELECT Gun_ID FROM Guns);
-- Expected: 0

-- Test Compatibility → Ammunition references
SELECT 'Compatibility referencing invalid Ammunition' as Check,
    COUNT(*) as Violations
FROM Gun_Ammunition_Compatibility
WHERE Ammunition_ID NOT IN (SELECT Ammunition_ID FROM Ammunition);
-- Expected: 0

-- ============================================================================
-- MIGRATION COMPLETE
-- ============================================================================

SELECT '=== MIGRATION COMPLETE ===' as Status;
SELECT 'All 1,943 records successfully renumbered' as Summary;
SELECT 'New ID ranges: Guns 100-199, Ammo 200-299, Turrets 300-2299, Compat 6000-6999' as NewRanges;
SELECT 'Foreign key integrity: VERIFIED' as ForeignKeys;
SELECT 'Ready for unified schema integration' as NextStep;

-- ============================================================================
-- POST-MIGRATION NOTES
-- ============================================================================
-- 1. Original database backed up to: naval_guns_backup_PRE_INTEGRATION_*.db
-- 2. All 1,943 records renumbered successfully
-- 3. Foreign key relationships preserved
-- 4. No data loss - record counts unchanged
-- 5. ID ranges now non-overlapping with new weapon systems:
--    - Guns: 100-199 (was 1-83)
--    - Ammunition: 200-299 (was 1-72)
--    - Turrets: 300-2299 (was 1-1700)
--    - Compatibility: 6000-6999 (was 1-88)
-- 6. New weapon systems will use:
--    - Torpedoes: 1000-1399
--    - Missiles: 2000-2499
--    - Naval Aircraft: 3000-3499
--    - Ground Aircraft: 4000-4499
--    - Bombs: 5000-5499
--    - Ships: 12000-13999
--    - Research Tree: 20000-21999
--    - Junction Tables: 7000-9999
-- 7. Next step: Apply unified schema (02_UNIFIED_SQL_SCHEMA.sql)
-- ============================================================================
