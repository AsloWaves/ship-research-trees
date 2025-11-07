-- ============================================================================
-- PHASE 1: RENUMBER EXISTING DATABASE IDs (VERSION 4 - FIX MAPPING ISSUE)
-- ============================================================================
-- Purpose: Renumber with reliable ID mapping using temporary ID columns
-- Fix: Store old IDs temporarily to create reliable mappings
-- Database: naval_guns.db
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
-- STEP 2: RENUMBER GUNS (WITH OLD ID PRESERVED FOR MAPPING)
-- ============================================================================

SELECT '=== Renumbering Guns ===' as Status;

CREATE TABLE Guns_New (
    Gun_ID INTEGER PRIMARY KEY,
    Old_Gun_ID INTEGER,  -- TEMPORARY: for mapping
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

INSERT INTO Guns_New (Gun_ID, Old_Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes)
SELECT
    99 + (SELECT COUNT(*) FROM Guns g2 WHERE g2.Gun_ID <= g1.Gun_ID) as New_Gun_ID,
    g1.Gun_ID as Old_Gun_ID,
    Turret_ID,
    Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes
FROM Guns g1
ORDER BY Gun_ID;

-- Create mapping using the Old_Gun_ID column
CREATE TEMP TABLE Gun_ID_Mapping AS
SELECT Old_Gun_ID, Gun_ID as New_Gun_ID FROM Guns_New;

DROP TABLE Guns;
ALTER TABLE Guns_New RENAME TO Guns;

SELECT 'Guns: ' || COUNT(*) || ' records, new range ' || MIN(Gun_ID) || '-' || MAX(Gun_ID) as Result FROM Guns;

-- ============================================================================
-- STEP 3: RENUMBER AMMUNITION (WITH OLD ID PRESERVED FOR MAPPING)
-- ============================================================================

SELECT '=== Renumbering Ammunition ===' as Status;

CREATE TABLE Ammunition_New (
    Ammunition_ID INTEGER PRIMARY KEY,
    Old_Ammo_ID INTEGER,  -- TEMPORARY: for mapping
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

INSERT INTO Ammunition_New (Ammunition_ID, Old_Ammo_ID, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes)
SELECT
    199 + (SELECT COUNT(*) FROM Ammunition a2 WHERE a2.ID <= a1.ID) as New_Ammo_ID,
    a1.ID as Old_Ammo_ID,
    Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes
FROM Ammunition a1
ORDER BY ID;

-- Create mapping using the Old_Ammo_ID column
CREATE TEMP TABLE Ammo_ID_Mapping AS
SELECT Old_Ammo_ID, Ammunition_ID as New_Ammo_ID FROM Ammunition_New;

DROP TABLE Ammunition;
ALTER TABLE Ammunition_New RENAME TO Ammunition;

SELECT 'Ammunition: ' || COUNT(*) || ' records, new range ' || MIN(Ammunition_ID) || '-' || MAX(Ammunition_ID) as Result FROM Ammunition;

-- ============================================================================
-- STEP 4: RENUMBER TURRETS (WITH OLD ID PRESERVED FOR MAPPING)
-- ============================================================================

SELECT '=== Renumbering Turrets ===' as Status;

CREATE TABLE Turrets_New (
    Turret_ID INTEGER PRIMARY KEY,
    Old_Turret_ID INTEGER,  -- TEMPORARY: for mapping
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

INSERT INTO Turrets_New (Turret_ID, Old_Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes)
SELECT
    299 + (SELECT COUNT(*) FROM Turrets t2 WHERE t2.Turret_ID <= t1.Turret_ID) as New_Turret_ID,
    t1.Turret_ID as Old_Turret_ID,
    Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes
FROM Turrets t1
ORDER BY Turret_ID;

-- Create mapping using the Old_Turret_ID column
CREATE TEMP TABLE Turret_ID_Mapping AS
SELECT Old_Turret_ID, Turret_ID as New_Turret_ID FROM Turrets_New;

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
-- STEP 8: REMOVE TEMPORARY OLD_ID COLUMNS
-- ============================================================================

SELECT '=== Removing temporary Old_ID columns ===' as Status;

-- Guns: Remove Old_Gun_ID
CREATE TABLE Guns_Final (
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

INSERT INTO Guns_Final SELECT Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation,
    Year_Introduced, Weight, Modded, Notes FROM Guns;

DROP TABLE Guns;
ALTER TABLE Guns_Final RENAME TO Guns;

-- Ammunition: Remove Old_Ammo_ID
CREATE TABLE Ammunition_Final (
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

INSERT INTO Ammunition_Final SELECT Ammunition_ID, Turret_ID, Caliber, Mark_Designation, Projectile_Type,
    Weight_LBS, Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type,
    Year_Introduced, Country, Modded, Notes FROM Ammunition;

DROP TABLE Ammunition;
ALTER TABLE Ammunition_Final RENAME TO Ammunition;

-- Turrets: Remove Old_Turret_ID
CREATE TABLE Turrets_Final (
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

INSERT INTO Turrets_Final SELECT Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation,
    Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN,
    Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM, Modded, Notes FROM Turrets;

DROP TABLE Turrets;
ALTER TABLE Turrets_Final RENAME TO Turrets;

SELECT 'Temporary columns removed' as Result;

-- ============================================================================
-- STEP 9: RENUMBER GUN_AMMUNITION_COMPATIBILITY
-- ============================================================================

SELECT '=== Renumbering Gun_Ammunition_Compatibility ===' as Status;

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

-- Use the mapping tables to update foreign keys
-- FILTER OUT INVALID RECORDS: Only migrate compatibility records where both Gun and Ammo exist
SELECT '⚠️  Cleaning ' || (SELECT COUNT(*) FROM Gun_Ammunition_Compatibility WHERE Ammunition_ID NOT IN (SELECT Old_Ammo_ID FROM Ammo_ID_Mapping)) || ' invalid compatibility records (pre-existing data integrity issue)' as Warning;

INSERT INTO Gun_Ammunition_Compatibility_New (Compatibility_ID, Gun_ID, Ammunition_ID,
    Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Barrel_Wear_Per_Round)
SELECT
    5999 + ROW_NUMBER() OVER (ORDER BY c1.Compatibility_ID) as New_Compat_ID,
    (SELECT New_Gun_ID FROM Gun_ID_Mapping WHERE Old_Gun_ID = c1.Gun_ID) as New_Gun_ID,
    (SELECT New_Ammo_ID FROM Ammo_ID_Mapping WHERE Old_Ammo_ID = c1.Ammunition_ID) as New_Ammo_ID,
    Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Barrel_Wear_Per_Round
FROM Gun_Ammunition_Compatibility c1
WHERE c1.Gun_ID IN (SELECT Old_Gun_ID FROM Gun_ID_Mapping)
  AND c1.Ammunition_ID IN (SELECT Old_Ammo_ID FROM Ammo_ID_Mapping)
ORDER BY Compatibility_ID;

DROP TABLE Gun_Ammunition_Compatibility;
ALTER TABLE Gun_Ammunition_Compatibility_New RENAME TO Gun_Ammunition_Compatibility;

SELECT 'Gun_Ammo_Compat: ' || COUNT(*) || ' records, new range ' || MIN(Compatibility_ID) || '-' || MAX(Compatibility_ID) as Result FROM Gun_Ammunition_Compatibility;

-- ============================================================================
-- STEP 10: RECREATE INDEXES
-- ============================================================================

SELECT '=== Recreating indexes ===' as Status;

CREATE INDEX idx_compat_gun ON Gun_Ammunition_Compatibility(Gun_ID);
CREATE INDEX idx_compat_ammo ON Gun_Ammunition_Compatibility(Ammunition_ID);

-- ============================================================================
-- STEP 11: UPDATE AUTOINCREMENT SEQUENCES
-- ============================================================================

SELECT '=== Setting AUTOINCREMENT sequences ===' as Status;

DELETE FROM sqlite_sequence WHERE name IN ('Guns', 'Ammunition', 'Turrets', 'Gun_Ammunition_Compatibility');

INSERT INTO sqlite_sequence (name, seq) VALUES ('Guns', 199);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Ammunition', 299);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Turrets', 2299);
INSERT INTO sqlite_sequence (name, seq) VALUES ('Gun_Ammunition_Compatibility', 6999);

-- ============================================================================
-- STEP 12: VERIFY AND RE-ENABLE FOREIGN KEYS
-- ============================================================================

PRAGMA foreign_keys = ON;

SELECT '=== Verifying integrity ===' as Status;

PRAGMA foreign_key_check;
PRAGMA integrity_check;

-- ============================================================================
-- STEP 13: FINAL VERIFICATION
-- ============================================================================

SELECT '=== FINAL STATE ===' as Status;

SELECT 'Guns' as TableName, COUNT(*) as Records, MIN(Gun_ID) as Min, MAX(Gun_ID) as Max FROM Guns
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
