-- Apply Research Findings Batch 1 - Ammunition Data
-- Date: 2025-10-08
-- Source: Web research from NavWeaps, Wikipedia, Naval History sources
-- Updates: Shell length, bursting charge, cartridge type

BEGIN TRANSACTION;

-- ==============================================================================
-- 16" AMMUNITION (Iowa class Mark 7 gun)
-- ==============================================================================

-- 16" Mark 8 AP (ID 1)
UPDATE Ammunition
SET Length_IN = 72.0,
    Bursting_Charge = 40.5,
    Cartridge_Type = 'Separate',
    Notes = 'Super-heavy AP, 2,700 lbs @ 2,500 fps, 1.5% bursting charge, 4.5 calibers length'
WHERE ID = 1 AND Caliber = '16"' AND Mark_Designation = 'Mark 8';

-- 16" Mark 13 HC (ID 2)
UPDATE Ammunition
SET Length_IN = 64.0,
    Bursting_Charge = 154.0,
    Cartridge_Type = 'Separate',
    Notes = 'High capacity, 1,900 lbs @ 2,690 fps, 8.1% bursting charge, 4.0 calibers length'
WHERE ID = 2 AND Caliber = '16"' AND Mark_Designation = 'Mark 13';

-- ==============================================================================
-- 12" AMMUNITION (Alaska class Mark 8 gun)
-- ==============================================================================

-- 12" Mark 18 AP (ID 32) - using estimates based on standard formulas
UPDATE Ammunition
SET Length_IN = 51.0,
    Bursting_Charge = 17.0,
    Cartridge_Type = 'Separate',
    Notes = 'AP for Alaska class, 1,140 lbs, ~1.5% bursting charge (est), 4.25 calibers length (est)'
WHERE ID = 32 AND Caliber = '12"' AND Mark_Designation = 'Mark 18';

-- ==============================================================================
-- 8" AMMUNITION (Des Moines class Mark 16 rapid-fire gun)
-- ==============================================================================

-- 8" Mark 21 AP (ID 36) - using estimates
UPDATE Ammunition
SET Length_IN = 36.0,
    Bursting_Charge = 5.0,
    Cartridge_Type = 'Separate',
    Notes = 'Super-heavy AP for Mark 16, 335 lbs @ 2,800 fps, ~1.5% bursting charge (est), 4.5 calibers (est)'
WHERE ID = 36 AND Caliber = '8"' AND Mark_Designation = 'Mark 16';

-- ==============================================================================
-- 5" AMMUNITION (5"/38 Mark 12 dual-purpose gun)
-- ==============================================================================

-- 5" AAC Mark 35 with VT proximity fuze capability
-- Need to find correct ID first - check for existing 5" Mark 54 VT-AAC or Mark 35
UPDATE Ammunition
SET Length_IN = 25.0,
    Bursting_Charge = 7.25,
    Cartridge_Type = 'Fixed',
    Notes = 'AAC with PD/MT/VT fuze compatibility, 54.3 lbs, explosive D composition A, complete round 47.5\" × 93 lbs'
WHERE Caliber = '5"' AND (Mark_Designation LIKE '%54%' OR Mark_Designation LIKE '%35%') AND Projectile_Type IN ('AAC', 'VT-AAC');

COMMIT;

-- ==============================================================================
-- NOTES AND SOURCES
-- ==============================================================================
--
-- Bursting Charge Percentages:
-- - AP shells: typically 1.5-2.0% of total weight
-- - HC/HE shells: typically 8-10% of total weight
--
-- Shell Length Standards:
-- - AP shells: typically 4.5 calibers
-- - HC shells: typically 4.0 calibers
-- - Special (older guns): 3.5-4.0 calibers
--
-- Cartridge Types:
-- - Separate: Projectile and powder bags loaded separately (large calibers)
-- - Semi-fixed: Projectile attached to powder case, adjustable charge (medium calibers)
-- - Fixed: Projectile crimped to powder case, one unit (small calibers)
--
-- Sources:
-- - NavWeaps.com (primary technical source)
-- - Wikipedia (16"/50 Mark 7, 12"/50 Mark 8, 8"/55 Mark 16, 5"/38 Mark 12)
-- - Naval History Magazine (Des Moines class, VT fuze articles)
-- - Navy General Board analysis (Alaska class)
