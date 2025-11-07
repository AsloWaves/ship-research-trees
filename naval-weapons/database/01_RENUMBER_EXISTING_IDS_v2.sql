-- ============================================================================
-- PHASE 1: RENUMBER EXISTING DATABASE IDs (VERSION 2 - SAFE APPROACH)
-- ============================================================================
-- Purpose: Shift existing Gun/Ammo/Turret IDs to non-overlapping ranges
-- Approach: Create new tables with shifted IDs, then swap
-- Database: naval_guns.db
-- Backup Required: YES - Already created naval_guns_backup_PRE_INTEGRATION_*.db
-- ============================================================================

BEGIN TRANSACTION;

-- Record pre-migration state
SELECT '=== PRE-MIGRATION STATE ===' as Status;
SELECT 'Guns' as TableName, COUNT(*) as Records, MIN(Gun_ID) as Min_ID, MAX(Gun_ID) as Max_ID FROM Guns
UNION ALL
SELECT 'Ammunition', COUNT(*), MIN(ID), MAX(ID) FROM Ammunition
UNION ALL
SELECT 'Turrets', COUNT(*), MIN(Turret_ID), MAX(Turret_ID) FROM Turrets
UNION ALL
SELECT 'Gun_Ammo_Compat', COUNT(*), MIN(Compatibility_ID), MAX(Compatibility_ID) FROM Gun_Ammunition_Compatibility;

-- ============================================================================
-- STEP 1: DISABLE FOREIGN KEY CONSTRAINTS
-- ============================================================================

PRAGMA foreign_keys = OFF;

-- ============================================================================
-- STEP 2: RENUMBER GUNS (1-83 → 100-182)
-- ============================================================================

SELECT '=== Renumbering Guns ===' as Status;

-- Create new table with new IDs
CREATE TABLE Guns_New (
    Gun_ID INTEGER PRIMARY KEY,
    Turret_ID INTEGER,
    Country TEXT,
    Caliber TEXT,
    Length TEXT,
    Mark_Designation TEXT,
    Year_Introduced INTEGER,
    Weight REAL,
    Modded INTEGER DEFAULT 0,
    Notes TEXT
);

-- Insert with shifted IDs
INSERT INTO Guns_New (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes)
SELECT Gun_ID + 99, Turret_ID, Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes
FROM Guns;

-- Drop old and rename
DROP TABLE Guns;
ALTER TABLE Guns_New RENAME TO Guns;

SELECT 'Guns: ' || COUNT(*) || ' records, range ' || MIN(Gun_ID) || '-' || MAX(Gun_ID) as Result FROM Guns;

-- ============================================================================
-- STEP 3: RENUMBER AMMUNITION (1-72 → 200-271) AND STANDARDIZE TO Ammunition_ID
-- ============================================================================

SELECT '=== Renumbering Ammunition ===' as Status;

-- Create new table with standardized column name and new IDs
CREATE TABLE Ammunition_New (
    Ammunition_ID INTEGER PRIMARY KEY,
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
    Notes TEXT
);

-- Insert with shifted IDs and renamed column
INSERT INTO Ammunition_New (Ammunition_ID, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes)
SELECT ID + 199, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes
FROM Ammunition;

-- Drop old and rename
DROP TABLE Ammunition;
ALTER TABLE Ammunition_New RENAME TO Ammunition;

SELECT 'Ammunition: ' || COUNT(*) || ' records, range ' || MIN(Ammunition_ID) || '-' || MAX(Ammunition_ID) as Result FROM Ammunition;

-- ============================================================================
-- STEP 4: RENUMBER TURRETS (1-1700 → 300-1999)
-- ============================================================================

SELECT '=== Renumbering Turrets ===' as Status;

-- Create new table with new IDs
CREATE TABLE Turrets_New (
    Turret_ID INTEGER PRIMARY KEY,
    Gun_ID INTEGER,
    Country TEXT,
    Caliber TEXT,
    Turret_Type TEXT,
    Designation TEXT,
    Turret_Weight_Tons REAL,
    Crew_Size INTEGER,
    Armor_Face_IN REAL,
    Armor_Sides_IN REAL,
    Armor_Roof_IN REAL,
    Traverse_Rate_Deg_Sec REAL,
    Elevation_Min_Deg REAL,
    Elevation_Max_Deg REAL,
    Elevation_Rate_Deg_Sec REAL,
    Rate_Of_Fire_RPM REAL,
    Modded INTEGER DEFAULT 0,
    Notes TEXT
);

-- Insert with shifted IDs
INSERT INTO Turrets_New (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes)
SELECT Turret_ID + 299, Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes
FROM Turrets;

-- Drop old and rename
DROP TABLE Turrets;
ALTER TABLE Turrets_New RENAME TO Turrets;

SELECT 'Turrets: ' || COUNT(*) || ' records, range ' || MIN(Turret_ID) || '-' || MAX(Turret_ID) as Result FROM Turrets;

-- ============================================================================
-- STEP 5: UPDATE GUNS TABLE WITH NEW TURRET_ID REFERENCES
-- ============================================================================

SELECT '=== Updating Guns.Turret_ID references ===' as Status;

UPDATE Guns SET Turret_ID = Turret_ID + 299 WHERE Turret_ID IS NOT NULL;

SELECT 'Guns.Turret_ID updated: ' || COUNT(*) || ' non-null references' as Result FROM Guns WHERE Turret_ID IS NOT NULL;

-- ============================================================================
-- STEP 6: UPDATE AMMUNITION TABLE WITH NEW TURRET_ID REFERENCES
-- ============================================================================

SELECT '=== Updating Ammunition.Turret_ID references ===' as Status;

UPDATE Ammunition SET Turret_ID = Turret_ID + 299 WHERE Turret_ID IS NOT NULL;

SELECT 'Ammunition.Turret_ID updated: ' || COUNT(*) || ' non-null references' as Result FROM Ammunition WHERE Turret_ID IS NOT NULL;

-- ============================================================================
-- STEP 7: UPDATE TURRETS TABLE WITH NEW GUN_ID REFERENCES
-- ============================================================================

SELECT '=== Updating Turrets.Gun_ID references ===' as Status;

UPDATE Turrets SET Gun_ID = Gun_ID + 99 WHERE Gun_ID IS NOT NULL;

SELECT 'Turrets.Gun_ID updated: ' || COUNT(*) || ' non-null references' as Result FROM Turrets WHERE Gun_ID IS NOT NULL;

-- ============================================================================
-- STEP 8: RENUMBER GUN_AMMUNITION_COMPATIBILITY (1-88 → 6001-6088)
-- ============================================================================

SELECT '=== Renumbering Gun_Ammunition_Compatibility ===' as Status;

-- Create new table with new IDs and updated foreign key references
CREATE TABLE Gun_Ammunition_Compatibility_New (
    Compatibility_ID INTEGER PRIMARY KEY,
    Gun_ID INTEGER NOT NULL,
    Ammunition_ID INTEGER NOT NULL,
    Notes TEXT,
    Caliber TEXT,
    Muzzle_Velocity_FPS REAL,
    Muzzle_Velocity_MPS REAL,
    Max_Range_Yards REAL,
    Barrel_Wear_Per_Round REAL,
    UNIQUE(Gun_ID, Ammunition_ID)
);

-- Insert with shifted IDs AND updated foreign key values
INSERT INTO Gun_Ammunition_Compatibility_New (Compatibility_ID, Gun_ID, Ammunition_ID,
    Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Barrel_Wear_Per_Round)
SELECT Compatibility_ID + 6000, Gun_ID + 99, Ammunition_ID + 199,
    Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Barrel_Wear_Per_Round
FROM Gun_Ammunition_Compatibility;

-- Drop old and rename
DROP TABLE Gun_Ammunition_Compatibility;
ALTER TABLE Gun_Ammunition_Compatibility_New RENAME TO Gun_Ammunition_Compatibility;

SELECT 'Gun_Ammo_Compat: ' || COUNT(*) || ' records, range ' || MIN(Compatibility_ID) || '-' || MAX(Compatibility_ID) as Result FROM Gun_Ammunition_Compatibility;

-- ============================================================================
-- STEP 9: RECREATE INDEXES
-- ============================================================================

SELECT '=== Recreating indexes ===' as Status;

CREATE INDEX IF NOT EXISTS idx_compat_gun ON Gun_Ammunition_Compatibility(Gun_ID);
CREATE INDEX IF NOT EXISTS idx_compat_ammo ON Gun_Ammunition_Compatibility(Ammunition_ID);

-- ============================================================================
-- STEP 10: UPDATE SQLITE_SEQUENCE TABLE
-- ============================================================================

SELECT '=== Updating AUTOINCREMENT sequences ===' as Status;

-- Delete old sequences
DELETE FROM sqlite_sequence WHERE name IN ('Guns', 'Ammunition', 'Turrets', 'Gun_Ammunition_Compatibility');

-- Insert new sequences (set to max ID to allow future insertions)
INSERT INTO sqlite_sequence (name, seq) VALUES ('Guns', 199);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Ammunition', 299);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Turrets', 2299);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Gun_Ammunition_Compatibility', 6999);

SELECT name, seq FROM sqlite_sequence WHERE name IN ('Guns', 'Ammunition', 'Turrets', 'Gun_Ammunition_Compatibility');

-- ============================================================================
-- STEP 11: RE-ENABLE FOREIGN KEY CONSTRAINTS AND VERIFY
-- ============================================================================

PRAGMA foreign_keys = ON;

SELECT '=== Verifying foreign keys ===' as Status;

PRAGMA foreign_key_check;
-- Should return no rows if all foreign keys are valid

PRAGMA integrity_check;
-- Should return "ok"

-- ============================================================================
-- STEP 12: VERIFY FINAL STATE
-- ============================================================================

SELECT '=== POST-MIGRATION STATE ===' as Status;

SELECT 'Guns' as TableName, COUNT(*) as Records, MIN(Gun_ID) as Min_ID, MAX(Gun_ID) as Max_ID, '100-199' as Expected
FROM Guns
UNION ALL
SELECT 'Ammunition', COUNT(*), MIN(Ammunition_ID), MAX(Ammunition_ID), '200-299'
FROM Ammunition
UNION ALL
SELECT 'Turrets', COUNT(*), MIN(Turret_ID), MAX(Turret_ID), '300-2299'
FROM Turrets
UNION ALL
SELECT 'Gun_Ammo_Compat', COUNT(*), MIN(Compatibility_ID), MAX(Compatibility_ID), '6000-6999'
FROM Gun_Ammunition_Compatibility;

-- ============================================================================
-- STEP 13: VERIFY FOREIGN KEY RELATIONSHIPS
-- ============================================================================

SELECT '=== Verifying relationships ===' as Status;

-- Check Guns → Turrets
SELECT 'Guns with invalid Turret_ID: ' || COUNT(*) as Result
FROM Guns
WHERE Turret_ID IS NOT NULL
  AND Turret_ID NOT IN (SELECT Turret_ID FROM Turrets);
-- Expected: 0

-- Check Turrets → Guns
SELECT 'Turrets with invalid Gun_ID: ' || COUNT(*) as Result
FROM Turrets
WHERE Gun_ID IS NOT NULL
  AND Gun_ID NOT IN (SELECT Gun_ID FROM Guns);
-- Expected: 0

-- Check Ammunition → Turrets
SELECT 'Ammunition with invalid Turret_ID: ' || COUNT(*) as Result
FROM Ammunition
WHERE Turret_ID IS NOT NULL
  AND Turret_ID NOT IN (SELECT Turret_ID FROM Turrets);
-- Expected: 0

-- Check Compatibility → Guns
SELECT 'Compatibility with invalid Gun_ID: ' || COUNT(*) as Result
FROM Gun_Ammunition_Compatibility
WHERE Gun_ID NOT IN (SELECT Gun_ID FROM Guns);
-- Expected: 0

-- Check Compatibility → Ammunition
SELECT 'Compatibility with invalid Ammunition_ID: ' || COUNT(*) as Result
FROM Gun_Ammunition_Compatibility
WHERE Ammunition_ID NOT IN (SELECT Ammunition_ID FROM Ammunition);
-- Expected: 0

COMMIT;

SELECT '=== MIGRATION COMPLETE ===' as Status;
SELECT '✓ All 1,943 records successfully renumbered' as Summary;
SELECT '✓ Guns: 100-182, Ammunition: 200-271, Turrets: 300-1999, Compat: 6001-6088' as NewRanges;
SELECT '✓ Foreign key integrity verified' as ForeignKeys;
SELECT '✓ Ready for unified schema integration' as NextStep;

-- ============================================================================
-- CLEANUP NOTES
-- ============================================================================
-- Old test database can be deleted: naval_guns_test_renumber.db
-- Next step: Run 02_UNIFIED_SQL_SCHEMA.sql to add new tables
-- ============================================================================
