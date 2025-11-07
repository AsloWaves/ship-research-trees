-- Apply Research Findings Batch 2 - Ammunition Data
-- Date: 2025-10-08
-- Source: Web research from NavWeaps, Wikipedia, Naval History sources
-- Updates: 3"/50 Mark 22 and 18"/48 Mark 1 ammunition data

BEGIN TRANSACTION;

-- ==============================================================================
-- 3" AMMUNITION (3"/50 Mark 22 dual-purpose gun)
-- ==============================================================================

-- 3" Mark 4 AAC (ID 79) - Anti-aircraft common
UPDATE Ammunition
SET Length_IN = 11.0,
    Bursting_Charge = 0.81,
    Cartridge_Type = 'Fixed',
    Notes = 'AA round for Mark 22, 13 lbs, 0.81 lbs bursting charge, 2,700 fps, complete round 34 lbs'
WHERE ID = 79 AND Caliber = '3"' AND Mark_Designation = 'Mark 4';

-- 3" Mark 6 HE (ID 80) - High explosive
UPDATE Ammunition
SET Length_IN = 11.0,
    Bursting_Charge = 1.27,
    Cartridge_Type = 'Fixed',
    Notes = 'HC round for Mark 22, 13 lbs, 1.27 lbs bursting charge, 2,700 fps, complete round 34 lbs'
WHERE ID = 80 AND Caliber = '3"' AND Mark_Designation = 'Mark 6';

-- ==============================================================================
-- 18" AMMUNITION (18"/48 Mark 1 experimental gun)
-- ==============================================================================

-- 18" Mark 1 AP (ID 12) - Super-heavy armor-piercing
UPDATE Ammunition
SET Length_IN = 81.0,
    Bursting_Charge = 58.0,
    Cartridge_Type = 'Separate',
    Notes = 'Super Heavy AP, 3,850 lbs @ 2,400 fps, ~1.5% bursting charge (est), 4.5 calibers length (est), designed but never manufactured for 18" caliber'
WHERE ID = 12 AND Caliber = '18"' AND Mark_Designation = 'Mark 1';

-- 18" Mark 2 HE (ID 13) - High explosive
UPDATE Ammunition
SET Length_IN = 72.0,
    Bursting_Charge = 272.0,
    Cartridge_Type = 'Separate',
    Notes = 'HE shell, 3,400 lbs, ~8% bursting charge (est), 4.0 calibers length (est), designed but never manufactured for 18" caliber'
WHERE ID = 13 AND Caliber = '18"' AND Mark_Designation = 'Mark 2';

COMMIT;

-- ==============================================================================
-- NOTES AND SOURCES
-- ==============================================================================
--
-- 3"/50 Mark 22:
-- - Used on destroyer escorts and other small warships
-- - Dual-purpose (surface and anti-aircraft)
-- - Fixed ammunition (projectile crimped to powder case)
-- - Sources: NavWeaps, Wikipedia, USS Slater archives
--
-- 18"/48 Mark 1:
-- - Experimental gun, never completed in 18" caliber
-- - Washington Naval Treaty (1922) prohibited guns >16"
-- - Prototype relined and finished as 16"/56 Mark 4
-- - Ammunition designed but never manufactured
-- - Bursting charges estimated using standard 1.5% (AP) and 8% (HE) formulas
-- - Sources: Wikipedia, NavWeaps, Naval History forums
--
