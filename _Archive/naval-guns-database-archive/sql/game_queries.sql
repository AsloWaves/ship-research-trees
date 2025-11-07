-- Naval Weapons Database - Game Integration SQL Queries
-- Version: 1.0
-- Date: October 2025
-- Database: naval_guns.db

-- ============================================================
-- QUERY 1: Find Compatible Ammunition for Equipped Turret
-- ============================================================
-- Use Case: Player equipped turret, show compatible ammo from inventory
-- Input: turret_id (INTEGER), player_inventory_ammo_ids (LIST)
-- Output: Ammunition list with ballistic stats

SELECT
    a.ID as Ammo_ID,
    a.Caliber,
    a.Mark_Designation,
    a.Projectile_Type,
    a.Weight_LBS,
    a.Kinetic_Energy_MJ,
    gac.Muzzle_Velocity_FPS,
    gac.Muzzle_Velocity_MPS,
    gac.Max_Range_Yards,
    gac.Barrel_Wear_Per_Round,
    gac.Notes as Combat_Notes
FROM Turrets t
JOIN Gun_Ammunition_Compatibility gac
    ON t.Gun_ID = gac.Gun_ID
JOIN Ammunition a
    ON gac.Ammunition_ID = a.ID
WHERE t.Turret_ID = :turret_id
  AND a.ID IN (:player_inventory_ammo_ids)
ORDER BY a.Projectile_Type, a.Mark_Designation;

-- Example: Turret_ID = 10 (16"/50 Mark 7 Twin)
-- Returns: Mark 8 AP, Mark 13 HC, Mark 14 HC, Mark 23 Nuclear, Mark 19 HE


-- ============================================================
-- QUERY 2: Show All Turret Variants for a Gun
-- ============================================================
-- Use Case: Research/tech tree UI showing turret options for a gun
-- Input: gun_id (INTEGER)
-- Output: List of turret variants with stats

SELECT
    t.Turret_ID,
    t.Designation,
    t.Turret_Type,
    t.Rate_Of_Fire_RPM,
    t.Turret_Weight_Tons,
    t.Crew_Size,
    t.Armor_Face_IN,
    t.Armor_Sides_IN,
    t.Armor_Roof_IN,
    t.Traverse_Rate_Deg_Sec,
    t.Elevation_Min_Deg,
    t.Elevation_Max_Deg,
    t.Modded,
    t.Notes
FROM Turrets t
WHERE t.Gun_ID = :gun_id
ORDER BY
    CASE t.Turret_Type
        WHEN 'Single' THEN 1
        WHEN 'Twin' THEN 2
        WHEN 'Triple' THEN 3
        WHEN 'Quad' THEN 4
        ELSE 5
    END,
    t.Rate_Of_Fire_RPM;

-- Example: Gun_ID = 396 (16"/50 Mark 7)
-- Returns: Twin and Quad turret variants


-- ============================================================
-- QUERY 3: Find All Turrets Compatible with Specific Ammunition
-- ============================================================
-- Use Case: Player acquired rare ammo, show which turrets can use it
-- Input: ammunition_id (INTEGER)
-- Output: List of compatible turrets

SELECT
    t.Turret_ID,
    t.Designation,
    t.Turret_Type,
    g.Caliber,
    g.Mark_Designation as Gun_Mark,
    t.Rate_Of_Fire_RPM,
    gac.Muzzle_Velocity_FPS,
    gac.Max_Range_Yards,
    t.Modded
FROM Ammunition a
JOIN Gun_Ammunition_Compatibility gac
    ON a.ID = gac.Ammunition_ID
JOIN Guns g
    ON gac.Gun_ID = g.Gun_ID
JOIN Turrets t
    ON g.Gun_ID = t.Gun_ID
WHERE a.ID = :ammunition_id
ORDER BY t.Designation;

-- Example: Ammunition_ID = 4 (Mark 23 Nuclear)
-- Returns: All 16"/50 Mark 7 turret variants


-- ============================================================
-- QUERY 4: Get Complete Turret Profile (Ship Fitting Screen)
-- ============================================================
-- Use Case: Display full turret info when equipping ship
-- Input: turret_id (INTEGER)
-- Output: Complete turret stats with gun info and ammo count

SELECT
    t.Turret_ID,
    t.Designation,
    t.Turret_Type,
    t.Turret_Weight_Tons,
    t.Crew_Size,
    t.Rate_Of_Fire_RPM,
    t.Armor_Face_IN,
    t.Armor_Sides_IN,
    t.Armor_Roof_IN,
    t.Traverse_Rate_Deg_Sec,
    t.Elevation_Min_Deg,
    t.Elevation_Max_Deg,
    t.Elevation_Rate_Deg_Sec,
    g.Caliber,
    g.Length,
    g.Mark_Designation as Gun_Mark,
    g.Year_Introduced as Gun_Year,
    COUNT(DISTINCT gac.Ammunition_ID) as Compatible_Ammo_Types,
    t.Modded,
    t.Notes
FROM Turrets t
JOIN Guns g ON t.Gun_ID = g.Gun_ID
LEFT JOIN Gun_Ammunition_Compatibility gac ON g.Gun_ID = gac.Gun_ID
WHERE t.Turret_ID = :turret_id
GROUP BY t.Turret_ID;

-- Example: Turret_ID = 10
-- Returns: Full profile with 5 compatible ammo types


-- ============================================================
-- QUERY 5: List All Ammunition Types for a Caliber
-- ============================================================
-- Use Case: Filter ammunition by caliber (e.g., show only 16" shells)
-- Input: caliber (TEXT)
-- Output: Ammunition list

SELECT
    a.ID,
    a.Caliber,
    a.Mark_Designation,
    a.Projectile_Type,
    a.Weight_LBS,
    a.Kinetic_Energy_MJ,
    a.Year_Introduced,
    a.Modded,
    a.Notes,
    COUNT(DISTINCT gac.Gun_ID) as Compatible_Guns
FROM Ammunition a
LEFT JOIN Gun_Ammunition_Compatibility gac
    ON a.ID = gac.Ammunition_ID
WHERE a.Caliber = :caliber
GROUP BY a.ID
ORDER BY a.Projectile_Type, a.Mark_Designation;

-- Example: Caliber = '16"'
-- Returns: All 16-inch ammunition types with compatibility count


-- ============================================================
-- QUERY 6: Get Ship Loadout Summary
-- ============================================================
-- Use Case: Display ship's complete turret loadout with loaded ammo
-- Input: ship_turret_slots (JSON/TABLE with turret_id and loaded_ammo_id)
-- Output: Complete loadout summary

-- Assuming ship_turret_slots temporary table:
-- CREATE TEMP TABLE ship_loadout (
--     slot_number INTEGER,
--     turret_id INTEGER,
--     loaded_ammo_id INTEGER
-- );

SELECT
    sl.slot_number,
    t.Designation as Turret_Name,
    t.Turret_Type,
    t.Rate_Of_Fire_RPM,
    a.Mark_Designation as Loaded_Ammo,
    a.Projectile_Type,
    gac.Muzzle_Velocity_FPS,
    gac.Max_Range_Yards,
    (t.Rate_Of_Fire_RPM * 60) as Rounds_Per_Minute_Per_Turret
FROM ship_loadout sl
JOIN Turrets t ON sl.turret_id = t.Turret_ID
JOIN Ammunition a ON sl.loaded_ammo_id = a.ID
JOIN Gun_Ammunition_Compatibility gac
    ON t.Gun_ID = gac.Gun_ID
    AND a.ID = gac.Ammunition_ID
ORDER BY sl.slot_number;


-- ============================================================
-- QUERY 7: Find Best Ammunition for Role
-- ============================================================
-- Use Case: Suggest best ammo for equipped turret by combat role
-- Input: turret_id, role ('anti-armor', 'bombardment', 'anti-air')
-- Output: Recommended ammunition ranked by suitability

SELECT
    a.ID as Ammo_ID,
    a.Mark_Designation,
    a.Projectile_Type,
    a.Kinetic_Energy_MJ,
    gac.Muzzle_Velocity_FPS,
    gac.Max_Range_Yards,
    CASE
        WHEN :role = 'anti-armor' THEN
            CASE a.Projectile_Type
                WHEN 'AP' THEN 100
                WHEN 'APC' THEN 90
                WHEN 'APCBC' THEN 85
                ELSE 0
            END
        WHEN :role = 'bombardment' THEN
            CASE a.Projectile_Type
                WHEN 'HE' THEN 100
                WHEN 'HC' THEN 90
                WHEN 'AAC' THEN 80
                ELSE 0
            END
        WHEN :role = 'anti-air' THEN
            CASE a.Projectile_Type
                WHEN 'VT' THEN 100
                WHEN 'AAC' THEN 90
                WHEN 'HE' THEN 70
                ELSE 0
            END
    END as Role_Suitability_Score
FROM Turrets t
JOIN Gun_Ammunition_Compatibility gac ON t.Gun_ID = gac.Gun_ID
JOIN Ammunition a ON gac.Ammunition_ID = a.ID
WHERE t.Turret_ID = :turret_id
  AND Role_Suitability_Score > 0
ORDER BY Role_Suitability_Score DESC, a.Kinetic_Energy_MJ DESC;


-- ============================================================
-- QUERY 8: Calculate Ship Firepower Rating
-- ============================================================
-- Use Case: Calculate total ship firepower based on equipped turrets
-- Input: ship_turret_ids (LIST)
-- Output: Firepower metrics

SELECT
    COUNT(*) as Total_Turrets,
    SUM(t.Rate_Of_Fire_RPM) as Combined_RPM,
    AVG(t.Turret_Weight_Tons) as Avg_Turret_Weight,
    SUM(t.Crew_Size) as Total_Crew,
    COUNT(DISTINCT g.Caliber) as Unique_Calibers,
    GROUP_CONCAT(DISTINCT g.Caliber) as Calibers_List
FROM Turrets t
JOIN Guns g ON t.Gun_ID = g.Gun_ID
WHERE t.Turret_ID IN (:ship_turret_ids);


-- ============================================================
-- QUERY 9: Search Turrets by Criteria
-- ============================================================
-- Use Case: Research screen with filters
-- Input: min_caliber, max_weight, min_rof, country, modded_filter
-- Output: Filtered turret list

SELECT
    t.Turret_ID,
    t.Designation,
    t.Country,
    g.Caliber,
    t.Turret_Type,
    t.Rate_Of_Fire_RPM,
    t.Turret_Weight_Tons,
    t.Crew_Size,
    t.Year_Introduced,
    t.Modded
FROM Turrets t
JOIN Guns g ON t.Gun_ID = g.Gun_ID
WHERE 1=1
  AND (CAST(REPLACE(g.Caliber, '"', '') AS REAL) >= :min_caliber OR :min_caliber IS NULL)
  AND (t.Turret_Weight_Tons <= :max_weight OR :max_weight IS NULL)
  AND (t.Rate_Of_Fire_RPM >= :min_rof OR :min_rof IS NULL)
  AND (t.Country = :country OR :country IS NULL)
  AND (t.Modded = :modded_filter OR :modded_filter IS NULL)
ORDER BY
    CAST(REPLACE(g.Caliber, '"', '') AS REAL) DESC,
    t.Rate_Of_Fire_RPM DESC;


-- ============================================================
-- QUERY 10: Get Ammunition Inventory Usage Report
-- ============================================================
-- Use Case: Show which turrets can use player's current ammo stock
-- Input: player_inventory_ammo_ids (LIST)
-- Output: Usage report

SELECT
    a.ID as Ammo_ID,
    a.Caliber,
    a.Mark_Designation,
    a.Projectile_Type,
    COUNT(DISTINCT g.Gun_ID) as Compatible_Guns,
    COUNT(DISTINCT t.Turret_ID) as Compatible_Turrets,
    GROUP_CONCAT(DISTINCT g.Caliber || ' ' || g.Mark_Designation) as Gun_List
FROM Ammunition a
JOIN Gun_Ammunition_Compatibility gac ON a.ID = gac.Ammunition_ID
JOIN Guns g ON gac.Gun_ID = g.Gun_ID
JOIN Turrets t ON g.Gun_ID = t.Gun_ID
WHERE a.ID IN (:player_inventory_ammo_ids)
GROUP BY a.ID
ORDER BY Compatible_Turrets DESC, a.Caliber;


-- ============================================================
-- DATABASE STATISTICS
-- ============================================================

-- Total record counts
SELECT
    'Guns' as Table_Name,
    COUNT(*) as Record_Count,
    COUNT(CASE WHEN Modded = 1 THEN 1 END) as Modded_Count,
    COUNT(CASE WHEN Modded = 0 THEN 1 END) as Historical_Count
FROM Guns
UNION ALL
SELECT
    'Ammunition',
    COUNT(*),
    COUNT(CASE WHEN Modded = 1 THEN 1 END),
    COUNT(CASE WHEN Modded = 0 THEN 1 END)
FROM Ammunition
UNION ALL
SELECT
    'Turrets',
    COUNT(*),
    COUNT(CASE WHEN Modded = 1 THEN 1 END),
    COUNT(CASE WHEN Modded = 0 THEN 1 END)
FROM Turrets
UNION ALL
SELECT
    'Compatibility',
    COUNT(*),
    0,
    COUNT(*)
FROM Gun_Ammunition_Compatibility;


-- Caliber distribution
SELECT
    g.Caliber,
    COUNT(DISTINCT g.Gun_ID) as Guns,
    COUNT(DISTINCT t.Turret_ID) as Turrets,
    COUNT(DISTINCT a.ID) as Ammunition_Types
FROM Guns g
LEFT JOIN Turrets t ON g.Gun_ID = t.Gun_ID
LEFT JOIN Gun_Ammunition_Compatibility gac ON g.Gun_ID = gac.Gun_ID
LEFT JOIN Ammunition a ON gac.Ammunition_ID = a.ID
GROUP BY g.Caliber
ORDER BY CAST(REPLACE(g.Caliber, '"', '') AS REAL) DESC;
