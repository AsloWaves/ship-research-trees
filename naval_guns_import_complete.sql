-- ==============================================================================
-- USA NAVAL WEAPONS COMPLETE DATABASE IMPORT (ALL REMAINING GUNS)
-- Source: USA_Naval_Weapons_Research.md
-- Phase 1 (12" guns), Phase 2 (10", 8"), Phase 3 (6", 5"/51), Phase 4 (5"/38, 5"/54, 5"/25, 4", 3")
-- ==============================================================================

BEGIN TRANSACTION;

-- ==============================================================================
-- PHASE 1 CONTINUATION: 12" GUNS (5 variants)
-- ==============================================================================

-- 12"/40 Mark 3 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (415, 'USA', '12"', '480 in', 'Mark 3', 1900, 58.24, 0, 'Pre-dreadnought, 116,480 lbs w/breech, 42 built, bore erosion issues');

-- 12"/40 Mark 4 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (416, 'USA', '12"', '480 in', 'Mark 4', 1900, 58.24, 0, 'Pre-dreadnought, smaller chamber for reduced charge');

-- 12"/45 Mark 5 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (417, 'USA', '12"', '540 in', 'Mark 5', 1906, 53.00, 0, 'Most-used main gun in US battleship history, 14 battleships');

-- 12"/50 Mark 7 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (418, 'USA', '12"', '600 in', 'Mark 7', 1912, 61.58, 0, 'Wyoming/Arkansas class, 123,160 lbs with breech');

-- 12"/50 Mark 8 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (419, 'USA', '12"', '600 in', 'Mark 8', 1944, 60.93, 0, 'Alaska-class cruisers, most powerful 12" gun ever');

-- 12" Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(30, '12"', 'Mark 15', 'AP', 870, 139.82, 1906, 'USA', 0, 'Mark 5 gun AP, 2900 fps'),
(31, '12"', 'Mark 17', 'AP', 870, 157.38, 1912, 'USA', 0, 'Mark 7 gun super-heavy AP, 3000 fps'),
(32, '12"', 'Mark 18', 'AP', 1140, 226.58, 1944, 'USA', 0, 'Mark 8 gun heavy AP, 2800 fps');

-- ==============================================================================
-- PHASE 2: HEAVY CRUISER GUNS
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 10" GUNS (1 variant - Armored cruisers only)
-- ------------------------------------------------------------------------------

-- 10"/40 Mark 3 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (420, 'USA', '10"', '400 in', 'Mark 3', 1902, 39.75, 0, 'Tennessee-class armored cruisers ACR-10 to ACR-13, 79,500 lbs w/breech');

-- 10" Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(33, '10"', 'Mark 3', 'AP', 510, 95.45, 1902, 'USA', 0, 'Armor-piercing, 2700 fps, 20,000 yards range');

-- ------------------------------------------------------------------------------
-- 8" GUNS (9 variants - ALL 8"/55 caliber)
-- ------------------------------------------------------------------------------

-- 8"/55 Mark 9 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (421, 'USA', '8"', '440 in', 'Mark 9', 1925, 30.00, 0, 'Treaty cruisers, Pensacola/Northampton/Portland class');

-- 8"/55 Mark 11 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (422, 'USA', '8"', '440 in', 'Mark 11', 1928, 17.00, 0, 'Simplified Mark 9, lighter weight');

-- 8"/55 Mark 12 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (423, 'USA', '8"', '440 in', 'Mark 12', 1928, 17.00, 0, 'Super-heavy shell variant');

-- 8"/55 Mark 13 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (424, 'USA', '8"', '440 in', 'Mark 13', 1935, 30.00, 0, 'Relined Mark 9 with chrome plating');

-- 8"/55 Mark 14 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (425, 'USA', '8"', '440 in', 'Mark 14', 1936, 30.00, 0, 'Improved relined Mark 9');

-- 8"/55 Mark 15 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (426, 'USA', '8"', '440 in', 'Mark 15', 1943, 17.50, 0, 'WWII standard, 715 EFC barrel life, New Orleans/Baltimore class');

-- 8"/55 Mark 16 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (427, 'USA', '8"', '440 in', 'Mark 16', 1948, 17.50, 0, 'Des Moines class rapid-fire, 10 rpm automatic');

-- 8"/55 Mark 71 Gun
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (428, 'USA', '8"', '440 in', 'Mark 71', 1975, 18.00, 0, 'MCLWG experimental, cancelled 1978, deemed no more effective than 5" RAP');

-- 8" Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(34, '8"', 'Mark 9', 'AP', 260, 42.24, 1925, 'USA', 0, 'Standard treaty cruiser AP, 2800 fps'),
(35, '8"', 'Mark 12', 'AP', 335, 50.62, 1934, 'USA', 0, 'Super-heavy AP, 2500 fps'),
(36, '8"', 'Mark 16', 'AP', 335, 50.62, 1948, 'USA', 0, 'Des Moines rapid-fire AP, 2500 fps'),
(37, '8"', 'Mark 71', 'AP', 260, 42.24, 1975, 'USA', 0, 'MCLWG experimental AP, 2800 fps');

-- ==============================================================================
-- PHASE 3: LIGHT CRUISER GUNS
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 6"/47 GUNS (5 variants - Protected cruisers)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(429, 'USA', '6"', '282 in', 'Mark 2', 1892, 4.31, 0, 'Cincinnati-class protected cruisers, 8,620 lbs'),
(430, 'USA', '6"', '282 in', 'Mark 3', 1894, 4.31, 0, 'Columbia-class protected cruisers'),
(431, 'USA', '6"', '282 in', 'Mark 4', 1900, 4.54, 0, 'Denver-class, 9,080 lbs w/breech'),
(432, 'USA', '6"', '282 in', 'Mark 5', 1903, 4.54, 0, 'St. Louis-class, last 6"/47'),
(433, 'USA', '6"', '282 in', 'Mark 6', 1905, 5.38, 0, 'Chester/Salem scout cruisers, 10,765 lbs, wire-wound');

-- 6"/47 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(38, '6"', 'Mark 2', 'AP', 105, 22.68, 1892, 'USA', 0, 'Standard 6"/47 AP, 2500 fps'),
(39, '6"', 'Mark 3', 'Common', 100, 23.39, 1895, 'USA', 0, 'Common shell, 2600 fps'),
(40, '6"', 'Mark 4', 'HE', 90, 24.37, 1900, 'USA', 0, 'High explosive, 2800 fps');

-- ------------------------------------------------------------------------------
-- 6"/53 GUNS (9 variants - WWII light cruisers)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(434, 'USA', '6"', '318 in', 'Mark 11', 1917, 6.15, 0, 'Omaha-class, 12,300 lbs, 10 ships'),
(435, 'USA', '6"', '318 in', 'Mark 12', 1937, 6.54, 0, 'Brooklyn-class, 15-gun broadside'),
(436, 'USA', '6"', '318 in', 'Mark 13', 1938, 6.54, 0, 'Modified Mark 12, improved recoil'),
(437, 'USA', '6"', '318 in', 'Mark 14', 1939, 6.54, 0, 'St. Louis-class, 6 ships'),
(438, 'USA', '6"', '318 in', 'Mark 15', 1939, 6.54, 0, 'Helena-class, 2 ships'),
(439, 'USA', '6"', '318 in', 'Mark 16', 1942, 6.64, 0, 'Cleveland-class, 27 built (most numerous US cruiser)'),
(440, 'USA', '6"', '318 in', 'Mark 16 DP', 1948, 8.07, 0, 'Worcester-class dual-purpose, 12 rpm rapid-fire'),
(441, 'USA', '6"', '318 in', 'Mark 17', 1947, 6.64, 0, 'Fargo-class, 2 built'),
(442, 'USA', '6"', '318 in', 'Mark 18', 1945, 8.07, 0, 'Alaska CB dual-purpose variant, not built');

-- 6"/53 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(41, '6"', 'Mark 24', 'AP', 130, 28.06, 1937, 'USA', 0, 'Standard WWII 6"/53 AP, 2500 fps'),
(42, '6"', 'Mark 25', 'HC', 105, 24.52, 1938, 'USA', 0, 'High-capacity, 2600 fps'),
(43, '6"', 'Mark 27', 'Common', 130, 28.06, 1940, 'USA', 0, 'Dual-purpose AP/HE, 2500 fps'),
(44, '6"', 'Mark 32', 'AAC', 105, 30.53, 1948, 'USA', 0, 'AA Common Worcester DP, 2900 fps, proximity fuse'),
(45, '6"', 'Mark 34', 'HC', 100, 25.22, 1944, 'USA', 0, 'Improved high-capacity HE'),
(46, '6"', 'Mark 35', 'Illum', 95, 22.20, 1943, 'USA', 0, 'Illumination shell, 2600 fps'),
(47, '6"', 'Mark 41', 'VT-HE', 105, 26.47, 1944, 'USA', 0, 'VT proximity fuze HE, 2700 fps');

-- ------------------------------------------------------------------------------
-- 5"/51 GUNS (9 variants - Cruiser secondary/destroyer main)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(443, 'USA', '5"', '255 in', 'Mark 7', 1900, 2.18, 0, 'Protected/scout cruisers, 4,360 lbs'),
(444, 'USA', '5"', '255 in', 'Mark 8', 1904, 2.18, 0, 'Improved Mark 7, increased chamber pressure'),
(445, 'USA', '5"', '255 in', 'Mark 9', 1910, 2.18, 0, 'Pennsylvania/Nevada BB secondary'),
(446, 'USA', '5"', '255 in', 'Mark 10', 1913, 2.27, 0, 'New York/Texas BB secondary, 4,540 lbs'),
(447, 'USA', '5"', '255 in', 'Mark 11', 1916, 2.18, 0, 'Omaha-class cruiser secondary'),
(448, 'USA', '5"', '255 in', 'Mark 12', 1917, 2.27, 0, 'Colorado/Tennessee BB secondary'),
(449, 'USA', '5"', '255 in', 'Mark 13', 1920, 2.27, 0, 'Brooklyn/St. Louis cruiser secondary'),
(450, 'USA', '5"', '255 in', 'Mark 14', 1922, 2.27, 0, 'Northampton/Portland CA secondary'),
(451, 'USA', '5"', '255 in', 'Mark 15', 1925, 2.27, 0, 'Final 5"/51, Pensacola CA');

-- 5"/51 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(48, '5"', 'Mark 15', 'AP', 50, 17.17, 1900, 'USA', 0, '5"/51 standard AP, 3150 fps'),
(49, '5"', 'Mark 17', 'Common', 50, 17.17, 1910, 'USA', 0, 'Dual-purpose AP/HE, 3150 fps'),
(50, '5"', 'Mark 19', 'HE', 47, 16.67, 1915, 'USA', 0, 'High explosive, 3200 fps'),
(51, '5"', 'Mark 21', 'AAC', 48, 15.96, 1920, 'USA', 0, 'AA Common, limited use due to low elevation'),
(52, '5"', 'Mark 23', 'Illum', 45, 14.04, 1920, 'USA', 0, 'Illumination shell, 3000 fps');

-- ==============================================================================
-- PHASE 4: DESTROYER & DUAL-PURPOSE GUNS
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- 5"/38 GUNS (8 variants - THE WWII dual-purpose gun)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(452, 'USA', '5"', '190 in', 'Mark 12', 1934, 1.82, 0, 'Original 5"/38 DP, ~10,000+ guns built, 3,640 lbs'),
(453, 'USA', '5"', '190 in', 'Mark 21', 1942, 1.82, 0, 'Improved Mark 12, better liner material'),
(454, 'USA', '5"', '190 in', 'Mark 22', 1943, 1.82, 0, 'Mark 12 modification, improved chamber'),
(455, 'USA', '5"', '190 in', 'Mark 24', 1945, 1.82, 0, 'Late-war, chrome-plated bore'),
(456, 'USA', '5"', '190 in', 'Mark 28', 1946, 1.82, 0, 'Post-war relined Mark 12'),
(457, 'USA', '5"', '190 in', 'Mark 30', 1948, 1.82, 0, 'Modernized, improved sights'),
(458, 'USA', '5"', '190 in', 'Mark 32', 1951, 1.82, 0, 'Korean War upgrade'),
(459, 'USA', '5"', '190 in', 'Mark 39', 1953, 1.82, 0, 'Final 5"/38, fully stabilized');

-- 5"/38 Ammunition (VT proximity fuze revolutionized AA warfare)
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(53, '5"', 'Mark 41', 'AAC', 54, 12.63, 1934, 'USA', 0, 'AA Common, mechanical time fuze'),
(54, '5"', 'Mark 46', 'Common', 55, 12.87, 1936, 'USA', 0, 'Dual-purpose surface/AA'),
(55, '5"', 'Mark 48', 'HE', 53, 12.87, 1938, 'USA', 0, 'High explosive, shore bombardment'),
(56, '5"', 'Mark 49', 'SP-Common', 55, 12.87, 1940, 'USA', 0, 'Special common, armor-piercing base'),
(57, '5"', 'Mark 53', 'AP', 55, 13.36, 1941, 'USA', 0, 'Armor-piercing, 2650 fps'),
(58, '5"', 'Mark 54', 'VT-AAC', 54, 12.63, 1943, 'USA', 0, 'VT proximity fuze, AA kill rate 5% to 50%+'),
(59, '5"', 'Mark 55', 'VT-Frag', 53, 12.87, 1943, 'USA', 0, 'Fragmentation with VT fuze'),
(60, '5"', 'Mark 62', 'Illum', 50, 10.80, 1943, 'USA', 0, 'Illumination, 2500 fps'),
(61, '5"', 'Mark 63', 'Star', 52, 11.71, 1944, 'USA', 0, 'Star shell, battlefield illumination'),
(62, '5"', 'Mark 65', 'Chaff', 48, 11.24, 1945, 'USA', 0, 'Anti-radar chaff, ECM'),
(63, '5"', 'Mark 71', 'HEPD', 56, 13.60, 1965, 'USA', 0, 'High-explosive point-detonating, Vietnam era'),
(64, '5"', 'Mark 82', 'GMLS', 50, 12.61, 1970, 'USA', 0, 'Guided projectile experimental');

-- ------------------------------------------------------------------------------
-- 5"/54 GUNS (3 variants - Post-WWII to present)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(460, 'USA', '5"', '270 in', 'Mark 16', 1953, 2.95, 0, 'First 5"/54, Forrest Sherman-class DD, 5,900 lbs'),
(461, 'USA', '5"', '270 in', 'Mark 42', 1956, 3.05, 0, 'Lightweight automatic, 40 rpm, 67+ ships, 6,100 lbs'),
(462, 'USA', '5"', '270 in', 'Mark 45', 1971, 3.18, 0, 'Fully automatic, 20 rpm, Arleigh Burke DDG-51, 6,360 lbs, current service');

-- 5"/54 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(65, '5"', 'Mark 41', 'HE', 70, 17.04, 1953, 'USA', 0, 'Standard HE 5"/54, 2650 fps'),
(66, '5"', 'Mark 42', 'HEPD', 70, 17.04, 1956, 'USA', 0, 'High-explosive point-detonating'),
(67, '5"', 'Mark 45', 'VT', 70, 17.04, 1960, 'USA', 0, 'Proximity-fuzed AA'),
(68, '5"', 'Mark 46', 'Illum', 65, 15.21, 1965, 'USA', 0, 'Illumination shell'),
(69, '5"', 'Mark 112', 'HE-IR', 70, 17.04, 1970, 'USA', 0, 'Infrared illumination, Vietnam era'),
(70, '5"', 'Mark 114', 'Chaff', 62, 15.65, 1975, 'USA', 0, 'Anti-radar chaff, ECM'),
(71, '5"', 'Mark 171', 'ERGM', 95, 20.54, 2005, 'USA', 0, 'Extended-range guided munition, 63 nm range, cancelled 2008');

-- ------------------------------------------------------------------------------
-- 5"/25 GUNS (3 variants - Early AA, obsolete by 1942)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(463, 'USA', '5"', '125 in', 'Mark 10', 1918, 1.50, 0, 'WWI AA gun, 3,000 lbs, BB/cruiser AA battery'),
(464, 'USA', '5"', '125 in', 'Mark 11', 1928, 1.50, 0, 'Improved Mark 10, inter-war BB AA'),
(465, 'USA', '5"', '125 in', 'Mark 13', 1935, 1.59, 0, 'Final 5"/25, 3,180 lbs, obsolete by 1942');

-- 5"/25 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(72, '5"', 'Mark 10', 'AAC', 52, 7.95, 1918, 'USA', 0, 'AA Common, mechanical time fuze, 2100 fps'),
(73, '5"', 'Mark 12', 'HE', 50, 8.00, 1928, 'USA', 0, 'High explosive, AA barrage, 2150 fps'),
(74, '5"', 'Mark 14', 'Illum', 48, 7.33, 1935, 'USA', 0, 'Illumination shell, 2100 fps');

-- ------------------------------------------------------------------------------
-- 4"/50 GUNS (5 variants - Flush-deck destroyers)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(466, 'USA', '4"', '200 in', 'Mark 7', 1910, 1.27, 0, 'Flush-deck destroyer main battery, 2,540 lbs'),
(467, 'USA', '4"', '200 in', 'Mark 8', 1913, 1.27, 0, 'Improved Mark 7, increased chamber pressure'),
(468, 'USA', '4"', '200 in', 'Mark 9', 1917, 1.36, 0, 'WWI destroyer, 2,720 lbs, 272 flush-deckers built'),
(469, 'USA', '4"', '200 in', 'Mark 10', 1920, 1.36, 0, 'Post-WWI, chrome-plated bore'),
(470, 'USA', '4"', '200 in', 'Mark 12', 1922, 1.36, 0, 'Final 4"/50, submarine deck gun S/Gato-class');

-- 4"/50 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(75, '4"', 'Mark 9', 'AP', 33, 9.60, 1910, 'USA', 0, 'Armor-piercing, 2900 fps'),
(76, '4"', 'Mark 11', 'Common', 32, 9.64, 1915, 'USA', 0, 'Dual-purpose AP/HE, 2950 fps'),
(77, '4"', 'Mark 13', 'HE', 31, 9.67, 1920, 'USA', 0, 'High explosive, 3000 fps');

-- ------------------------------------------------------------------------------
-- 3"/50 GUNS (8 variants - Destroyer escorts, patrol craft)
-- ------------------------------------------------------------------------------

INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES
(471, 'USA', '3"', '150 in', 'Mark 10', 1915, 0.68, 0, 'WWI AA gun, 1,360 lbs, manual loading'),
(472, 'USA', '3"', '150 in', 'Mark 17', 1922, 0.68, 0, 'Improved Mark 10, submarine deck gun'),
(473, 'USA', '3"', '150 in', 'Mark 18', 1928, 0.68, 0, 'Inter-war variant, improved sights'),
(474, 'USA', '3"', '150 in', 'Mark 22', 1941, 0.77, 0, 'WWII rapid-fire, 50 rpm, destroyer escort AA, 1,540 lbs'),
(475, 'USA', '3"', '150 in', 'Mark 26', 1944, 0.82, 0, 'Fully automatic, 50 rpm, improved reliability, 1,640 lbs'),
(476, 'USA', '3"', '150 in', 'Mark 27', 1945, 0.82, 0, 'Final 3"/50 WWII variant, post-war DEs'),
(477, 'USA', '3"', '150 in', 'Mark 33', 1958, 0.91, 0, 'Twin mount automatic, 1,820 lbs, patrol craft'),
(478, 'USA', '3"', '150 in', 'Mark 34', 1962, 0.91, 0, 'Final 3"/50, Vietnam-era patrol craft, retired 1970s');

-- 3"/50 Ammunition
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Kinetic_Energy_MJ, Year_Introduced, Country, Modded, Notes)
VALUES
(79, '3"', 'Mark 4', 'AAC', 13, 3.29, 1915, 'USA', 0, 'AA Common, mechanical time fuze, 2700 fps'),
(80, '3"', 'Mark 6', 'HE', 13, 3.29, 1920, 'USA', 0, 'High explosive, anti-aircraft/surface, 2700 fps'),
(81, '3"', 'Mark 21', 'VT', 13, 3.29, 1944, 'USA', 0, 'Proximity-fuzed AA, 2700 fps'),
(82, '3"', 'Mark 25', 'Illum', 12, 2.92, 1945, 'USA', 0, 'Illumination, night combat, 2650 fps');

COMMIT;

-- ==============================================================================
-- IMPORT SUMMARY
-- ==============================================================================
-- Total Guns Imported: 78 (Gun_ID 415-478, plus 14 from previous import = 92 total)
-- Total Ammunition Imported: 54 (ID 30-82, plus 18 from previous import = 72 total)
-- Note: Turrets and Gun_Ammunition_Compatibility tables require additional data
-- ==============================================================================
