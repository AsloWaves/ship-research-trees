-- Apply Research Findings Batch 2 - Turret Data
-- Date: 2025-10-08
-- Source: Web research from NavWeaps, Wikipedia, Naval History sources
-- Updates: 3"/50 Mark 22 turret data

BEGIN TRANSACTION;

-- ==============================================================================
-- 3" TURRETS (3"/50 Mark 22)
-- ==============================================================================

-- Turret_ID 62: 3"/50 Mark 22 Twin Mount
UPDATE Turrets
SET Crew_Size = 6,
    Traverse_Rate_Deg_Sec = 30.0,
    Elevation_Rate_Deg_Sec = 24.0,
    Notes = '3"/50 Mark 22 dual-purpose mount, crew 5-7 (using 6 avg), 30 deg/sec traverse, 24 deg/sec elevation, open mount (no armor), power-driven automatic loader'
WHERE Turret_ID = 62;

-- ==============================================================================
-- 18" TURRETS (18"/48 Mark 1)
-- ==============================================================================

-- Turret_ID 21: 18"/48 Mark 1 Triple Turret
-- NO UPDATE - Turret was never built (design sketches only)
-- Notes field already indicates this is experimental/never completed

COMMIT;

-- ==============================================================================
-- NOTES AND SOURCES
-- ==============================================================================
--
-- 3"/50 Mark 22 Mount:
-- - Dual-purpose (surface and anti-aircraft)
-- - Open mount (no armor protection)
-- - Power-driven automatic loader
-- - Elevation range: -15° to +85°
-- - Used on destroyer escorts, patrol frigates, and other small warships
-- - Sources: NavWeaps, Wikipedia, USS Slater archives
--
-- 18"/48 Mark 1 Turret:
-- - Never built - only design sketches exist (2-gun and 3-gun turrets studied in 1938)
-- - Gun prototype was halfway completed when Washington Naval Treaty prohibited >16" guns
-- - Prototype was relined and finished as 16"/56 Mark 4 gun
-- - Never fired in original 18" configuration
-- - No crew, armor, or performance data available
-- - Sources: Wikipedia, NavWeaps, Naval History forums
--
