-- ============================================================================
-- PHASE 1: RENUMBER EXISTING DATABASE IDs (VERSION 3 - CURRENT STATE)
-- ============================================================================
-- Purpose: Renumber from CURRENT state (IDs may not start at 1)
-- Approach: Calculate offsets based on current MIN/MAX, then create new tables
-- Database: naval_guns.db (current state, not assuming IDs start at 1)
-- ============================================================================

BEGIN TRANSACTION;

-- ============================================================================
-- STEP 1: ANALYZE CURRENT STATE
-- ============================================================================

SELECT '=== CURRENT DATABASE STATE ===' as Status;

SELECT 'Guns' as TableName,
    COUNT(*) as Records,
    MIN(Gun_ID) as Current_Min,
    MAX(Gun_ID) as Current_Max,
    100 as Target_Min,
    100 + COUNT(*) - 1 as Target_Max
FROM Guns;

SELECT 'Ammunition' as TableName,
    COUNT(*) as Records,
    MIN(ID) as Current_Min,
    MAX(ID) as Current_Max,
    200 as Target_Min,
    200 + COUNT(*) - 1 as Target_Max
FROM Ammunition;

SELECT 'Turrets' as TableName,
    COUNT(*) as Records,
    MIN(Turret_ID) as Current_Min,
    MAX(Turret_ID) as Current_Max,
    300 as Target_Min,
    300 + COUNT(*) - 1 as Target_Max
FROM Turrets;

SELECT 'Gun_Ammo_Compat' as TableName,
    COUNT(*) as Records,
    MIN(Compatibility_ID) as Current_Min,
    MAX(Compatibility_ID) as Current_Max,
    6000 as Target_Min,
    6000 + COUNT(*) - 1 as Target_Max
FROM Gun_Ammunition_Compatibility;

PRAGMA foreign_keys = OFF;

-- ============================================================================
-- STEP 2: RENUMBER GUNS
-- ============================================================================
-- Strategy: Create mapping table, use ROW_NUMBER() equivalent to assign sequential IDs

SELECT '=== Renumbering Guns ===' as Status;

-- Create new table
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

-- Insert with new sequential IDs starting at 100
-- Use a subquery with ROWID to create sequential numbering
INSERT INTO Guns_New (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes)
SELECT
    99 + (SELECT COUNT(*) FROM Guns g2 WHERE g2.Gun_ID <= g1.Gun_ID) as New_Gun_ID,
    Turret_ID,
    Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes
FROM Guns g1
ORDER BY Gun_ID;

-- Create mapping for later foreign key updates
CREATE TEMP TABLE Gun_ID_Mapping AS
SELECT
    g_old.Gun_ID as Old_Gun_ID,
    g_new.Gun_ID as New_Gun_ID
FROM Guns g_old
JOIN Guns_New g_new ON
    g_old.Country = g_new.Country AND
    g_old.Caliber = g_new.Caliber AND
    g_old.Mark_Designation = g_new.Mark_Designation;

-- Drop old and rename
DROP TABLE Guns;
ALTER TABLE Guns_New RENAME TO Guns;

SELECT 'Guns: ' || COUNT(*) || ' records, new range ' || MIN(Gun_ID) || '-' || MAX(Gun_ID) as Result FROM Guns;

-- ============================================================================
-- STEP 3: RENUMBER AMMUNITION (WITH STANDARDIZED NAME)
-- ============================================================================

SELECT '=== Renumbering Ammunition ===' as Status;

-- Create new table
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

-- Insert with new sequential IDs starting at 200
INSERT INTO Ammunition_New (Ammunition_ID, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes)
SELECT
    199 + (SELECT COUNT(*) FROM Ammunition a2 WHERE a2.ID <= a1.ID) as New_Ammo_ID,
    Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes
FROM Ammunition a1
ORDER BY ID;

-- Create mapping for later foreign key updates
CREATE TEMP TABLE Ammo_ID_Mapping AS
SELECT
    a_old.ID as Old_Ammo_ID,
    a_new.Ammunition_ID as New_Ammo_ID
FROM Ammunition a_old
JOIN Ammunition_New a_new ON
    a_old.Country = a_new.Country AND
    a_old.Caliber = a_new.Caliber AND
    a_old.Mark_Designation = a_new.Mark_Designation;

-- Drop old and rename
DROP TABLE Ammunition;
ALTER TABLE Ammunition_New RENAME TO Ammunition;

SELECT 'Ammunition: ' || COUNT(*) || ' records, new range ' || MIN(Ammunition_ID) || '-' || MAX(Ammunition_ID) as Result FROM Ammunition;

-- ============================================================================
-- STEP 4: RENUMBER TURRETS
-- ============================================================================

SELECT '=== Renumbering Turrets ===' as Status;

-- Create new table
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

-- Insert with new sequential IDs starting at 300
INSERT INTO Turrets_New (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes)
SELECT
    299 + (SELECT COUNT(*) FROM Turrets t2 WHERE t2.Turret_ID <= t1.Turret_ID) as New_Turret_ID,
    Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes
FROM Turrets t1
ORDER BY Turret_ID;

-- Create mapping for later foreign key updates
CREATE TEMP TABLE Turret_ID_Mapping AS
SELECT
    t_old.Turret_ID as Old_Turret_ID,
    t_new.Turret_ID as New_Turret_ID
FROM Turrets t_old
JOIN Turrets_New t_new ON
    t_old.Country = t_new.Country AND
    t_old.Caliber = t_new.Caliber AND
    t_old.Designation = t_new.Designation;

-- Drop old and rename
DROP TABLE Turrets;
ALTER TABLE Turrets_New RENAME TO Turrets;

SELECT 'Turrets: ' || COUNT(*) || ' records, new range ' || MIN(Turret_ID) || '-' || MAX(Turret_ID) as Result FROM Turrets;

-- ============================================================================
-- STEP 5: UPDATE FOREIGN KEY REFERENCES IN GUNS
-- ============================================================================

SELECT '=== Updating Guns.Turret_ID ===' as Status;

UPDATE Guns SET Turret_ID = (
    SELECT New_Turret_ID FROM Turret_ID_Mapping WHERE Old_Turret_ID = Guns.Turret_ID
)
WHERE Turret_ID IS NOT NULL;

SELECT 'Updated ' || changes() || ' Guns.Turret_ID references' as Result;

-- ============================================================================
-- STEP 6: UPDATE FOREIGN KEY REFERENCES IN AMMUNITION
-- ============================================================================

SELECT '=== Updating Ammunition.Turret_ID ===' as Status;

UPDATE Ammunition SET Turret_ID = (
    SELECT New_Turret_ID FROM Turret_ID_Mapping WHERE Old_Turret_ID = Ammunition.Turret_ID
)
WHERE Turret_ID IS NOT NULL;

SELECT 'Updated ' || changes() || ' Ammunition.Turret_ID references' as Result;

-- ============================================================================
-- STEP 7: UPDATE FOREIGN KEY REFERENCES IN TURRETS
-- ============================================================================

SELECT '=== Updating Turrets.Gun_ID ===' as Status;

UPDATE Turrets SET Gun_ID = (
    SELECT New_Gun_ID FROM Gun_ID_Mapping WHERE Old_Gun_ID = Turrets.Gun_ID
)
WHERE Gun_ID IS NOT NULL;

SELECT 'Updated ' || changes() || ' Turrets.Gun_ID references' as Result;

-- ============================================================================
-- STEP 8: RENUMBER GUN_AMMUNITION_COMPATIBILITY
-- ============================================================================

SELECT '=== Renumbering Gun_Ammunition_Compatibility ===' as Status;

-- Create new table
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

-- Insert with new sequential IDs starting at 6000 AND updated foreign keys
INSERT INTO Gun_Ammunition_Compatibility_New (Compatibility_ID, Gun_ID, Ammunition_ID,
    Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Barrel_Wear_Per_Round)
SELECT
    5999 + (SELECT COUNT(*) FROM Gun_Ammunition_Compatibility c2 WHERE c2.Compatibility_ID <= c1.Compatibility_ID) as New_Compat_ID,
    (SELECT New_Gun_ID FROM Gun_ID_Mapping WHERE Old_Gun_ID = c1.Gun_ID) as New_Gun_ID,
    (SELECT New_Ammo_ID FROM Ammo_ID_Mapping WHERE Old_Ammo_ID = c1.Ammunition_ID) as New_Ammo_ID,
    Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Barrel_Wear_Per_Round
FROM Gun_Ammunition_Compatibility c1
ORDER BY Compatibility_ID;

-- Drop old and rename
DROP TABLE Gun_Ammunition_Compatibility;
ALTER TABLE Gun_Ammunition_Compatibility_New RENAME TO Gun_Ammunition_Compatibility;

SELECT 'Gun_Ammo_Compat: ' || COUNT(*) || ' records, new range ' || MIN(Compatibility_ID) || '-' || MAX(Compatibility_ID) as Result FROM Gun_Ammunition_Compatibility;

-- ============================================================================
-- STEP 9: RECREATE INDEXES
-- ============================================================================

SELECT '=== Recreating indexes ===' as Status;

CREATE INDEX idx_compat_gun ON Gun_Ammunition_Compatibility(Gun_ID);
CREATE INDEX idx_compat_ammo ON Gun_Ammunition_Compatibility(Ammunition_ID);

-- ============================================================================
-- STEP 10: UPDATE AUTOINCREMENT SEQUENCES
-- ============================================================================

SELECT '=== Setting AUTOINCREMENT sequences ===' as Status;

DELETE FROM sqlite_sequence WHERE name IN ('Guns', 'Ammunition', 'Turrets', 'Gun_Ammunition_Compatibility');

INSERT INTO sqlite_sequence (name, seq) VALUES ('Guns', 199);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Ammunition', 299);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Turrets', 2299);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Gun_Ammunition_Compatibility', 6999);

-- ============================================================================
-- STEP 11: VERIFY AND RE-ENABLE FOREIGN KEYS
-- ============================================================================

PRAGMA foreign_keys = ON;

SELECT '=== Verifying integrity ===' as Status;

PRAGMA foreign_key_check;
PRAGMA integrity_check;

-- ============================================================================
-- STEP 12: FINAL VERIFICATION
-- ============================================================================

SELECT '=== FINAL STATE ===' as Status;

SELECT 'Guns' as Table, COUNT(*) as Records, MIN(Gun_ID) as Min, MAX(Gun_ID) as Max FROM Guns
UNION ALL
SELECT 'Ammunition', COUNT(*), MIN(Ammunition_ID), MAX(Ammunition_ID) FROM Ammunition
UNION ALL
SELECT 'Turrets', COUNT(*), MIN(Turret_ID), MAX(Turret_ID) FROM Turrets
UNION ALL
SELECT 'Gun_Ammo_Compat', COUNT(*), MIN(Compatibility_ID), MAX(Compatibility_ID) FROM Gun_Ammunition_Compatibility;

-- Verify all foreign keys are valid
SELECT 'Foreign Key Checks:' as ValidationStep;
SELECT 'Guns → Turrets violations: ' || COUNT(*) as Result
FROM Guns WHERE Turret_ID IS NOT NULL AND Turret_ID NOT IN (SELECT Turret_ID FROM Turrets);

SELECT 'Turrets → Guns violations: ' || COUNT(*) as Result
FROM Turrets WHERE Gun_ID IS NOT NULL AND Gun_ID NOT IN (SELECT Gun_ID FROM Guns);

SELECT 'Ammo → Turrets violations: ' || COUNT(*) as Result
FROM Ammunition WHERE Turret_ID IS NOT NULL AND Turret_ID NOT IN (SELECT Turret_ID FROM Turrets);

SELECT 'Compat → Guns violations: ' || COUNT(*) as Result
FROM Gun_Ammunition_Compatibility WHERE Gun_ID NOT IN (SELECT Gun_ID FROM Guns);

SELECT 'Compat → Ammo violations: ' || COUNT(*) as Result
FROM Gun_Ammunition_Compatibility WHERE Ammunition_ID NOT IN (SELECT Ammunition_ID FROM Ammunition);

COMMIT;

SELECT '=== ✓ MIGRATION COMPLETE ===' as Status;
SELECT 'All records renumbered to non-overlapping ranges' as Summary;
SELECT 'Guns: 100-199 | Ammo: 200-299 | Turrets: 300-2299 | Compat: 6000-6999' as NewRanges;
SELECT 'Ready for unified database schema' as NextStep;

-- ============================================================================
-- DROP TEMPORARY MAPPING TABLES (cleanup)
-- ============================================================================
DROP TABLE IF EXISTS Gun_ID_Mapping;
DROP TABLE IF EXISTS Ammo_ID_Mapping;
DROP TABLE IF EXISTS Turret_ID_Mapping;
