-- Apply Research Findings Batch 1 - Turret Data
-- Date: 2025-10-08
-- Source: Web research from NavWeaps, Wikipedia, Naval History sources
-- Updates: Crew size, armor thickness, traverse/elevation rates

BEGIN TRANSACTION;

-- ==============================================================================
-- 16" TURRETS (Iowa class)
-- ==============================================================================

-- Turret_ID 4: Iowa class 16"/50 Mark 7 Triple Turret
UPDATE Turrets
SET Crew_Size = 94,
    Armor_Face_IN = 19.5,
    Armor_Sides_IN = 9.5,
    Armor_Roof_IN = 7.25,
    Traverse_Rate_Deg_Sec = 4.0,
    Elevation_Rate_Deg_Sec = 12.0,
    Notes = 'Iowa class, most powerful US naval turret, 1,708 tons, crew 77-110 (using 94 avg), 19.5" face (17" Class B + 2.5" STS)'
WHERE Turret_ID = 4;

-- ==============================================================================
-- 14" TURRETS
-- ==============================================================================

-- Turret_ID 25: New Mexico class 14"/50 Mark 4 Triple Turret
UPDATE Turrets
SET Armor_Face_IN = 18.0,
    Armor_Sides_IN = 10.0,
    Armor_Roof_IN = 5.0,
    Notes = 'New Mexico/Tennessee class, 18" face, 10" sides, 5" roof, 13" barbette'
WHERE Turret_ID = 25;

-- Turret_ID 26: Tennessee class 14"/50 Mark 6 (Mark 5 in some sources) Triple Turret
UPDATE Turrets
SET Armor_Face_IN = 18.0,
    Armor_Sides_IN = 10.0,
    Armor_Roof_IN = 5.0
WHERE Turret_ID = 26;

-- Turret_ID 22: New York class 14"/45 Mark 1 Twin Turret
UPDATE Turrets
SET Armor_Face_IN = 15.0,
    Notes = 'New York/Texas class, estimated 15" face armor from class specifications'
WHERE Turret_ID = 22;

-- ==============================================================================
-- 13" TURRETS
-- ==============================================================================

-- Turret_ID 27: Indiana class 13"/35 Mark 1 Twin Turret
UPDATE Turrets
SET Armor_Face_IN = 15.0,
    Notes = 'Indiana/Oregon/Massachusetts class, first true US battleships, 15" turret armor, 18" belt'
WHERE Turret_ID = 27;

-- ==============================================================================
-- 12" TURRETS (Alaska class)
-- ==============================================================================

-- Turret_ID 32: Alaska class 12"/50 Mark 8 Triple Turret
UPDATE Turrets
SET Armor_Face_IN = 12.8,
    Armor_Sides_IN = 5.6,
    Armor_Roof_IN = 5.0,
    Notes = 'Alaska class large cruisers, 12.8" face, 5.25-6" sides (avg 5.6"), 5" roof, 510 tons'
WHERE Turret_ID = 32;

-- ==============================================================================
-- 8" TURRETS (Des Moines class)
-- ==============================================================================

-- Turret_ID 37: Des Moines class 8"/55 Mark 16 Triple Turret
UPDATE Turrets
SET Crew_Size = 45,
    Traverse_Rate_Deg_Sec = 5.0,
    Elevation_Rate_Deg_Sec = 8.2,
    Notes = 'Des Moines class rapid-fire, 45 crew per turret, 10 rpm sustained, 451 tons, 125 hp training motor, 25 hp elevation per gun'
WHERE Turret_ID = 37;

COMMIT;

-- ==============================================================================
-- NOTES AND SOURCES
-- ==============================================================================
--
-- Armor Types:
-- - Class A: Face-hardened armor (faces, sides)
-- - Class B: Homogeneous armor (roofs, decks)
-- - STS: Special Treatment Steel (backing plates)
--
-- Turret Crew Estimates:
-- - 16" turrets: 77-150 men (varies by class and configuration)
-- - 14" turrets: 60-100 men (estimated)
-- - 8" turrets: 30-50 men
-- - 6" turrets: 20-35 men
-- - 5" turrets: 6-15 men (mount dependent)
--
-- Traverse/Elevation Rates:
-- - Battleship main battery: 2-5 deg/sec traverse, 4-12 deg/sec elevation
-- - Cruiser main battery: 4-6 deg/sec traverse, 8-12 deg/sec elevation
-- - Dual-purpose mounts: 15-25 deg/sec both axes
--
-- Sources:
-- - Iowa class armor: Wikipedia, NavWeaps, Armament of Iowa-class article
-- - New Mexico/Tennessee armor: Wikipedia battleship class articles
-- - Alaska class: Navy General Board, Wikipedia
-- - Des Moines class: Naval History Magazine, NavWeaps
-- - Indiana class: Naval Encyclopedia, Wikipedia
