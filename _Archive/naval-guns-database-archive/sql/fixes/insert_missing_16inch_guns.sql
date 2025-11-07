-- Insert Missing 16" Guns (Gun_IDs 396-400)
-- These guns were skipped during markdown parsing due to extra pipes in Notes field
-- Data extracted from naval_guns_database.md

-- Gun 396: 16"/50 Mark 7 (Iowa-class - famous battleship gun)
INSERT INTO Guns (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    396,
    NULL,
    'USA',
    '16"',
    '/50',
    'Mark 7',
    1943,
    133.952,
    0,
    '16"/50 (40.6 cm) Mark 7 - Possibly the best battleship gun ever put into service. Ships: USS Iowa (BB-61), USS New Jersey (BB-62), USS Missouri (BB-63), USS Wisconsin (BB-64) | Barrel Life: 290-350 ESR | Rate of Fire: 2 rpm | Elevation: -5° to +45° | Weight: 267,904 lbs (with breech) | Rifling: 96 grooves, 1 in 25 twist | Chamber: 27,000 in³ | Source: http://www.navweaps.com/Weapons/WNUS_16-50_mk7.php'
);

-- Gun 397: 16"/45 Mark 1 (Colorado-class)
INSERT INTO Guns (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    397,
    NULL,
    'USA',
    '16"',
    '/45',
    'Mark 1',
    1921,
    117.898,
    0,
    '16"/45 (40.6 cm) Mark 1 - First US 16" naval gun, served on Colorado class battleships. Ships: USS Colorado (BB-45), USS Maryland (BB-46), USS West Virginia (BB-48) | Barrel Life: ~350 rounds | Rate of Fire: 1.5 rpm | Elevation: -5° to +30° | Weight: 235,796 lbs (118 tons with breech), 230,948 lbs (115 tons without breech) | Barrel Length: 720 in (60 ft) bore length | Rifling: 96 grooves, increasing RH 1 in 50 to 1 in 32 | Chamber: 23,506 in³'
);

-- Gun 398: 16"/50 Mark 2/3 (Cancelled - Lexington battlecruisers)
INSERT INTO Guns (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    398,
    NULL,
    'USA',
    '16"',
    '/50',
    'Mark 2/3',
    NULL,
    128.15,
    0,
    '16"/50 (40.6 cm) Mark 2 and Mark 3 - CANCELLED by Washington Naval Treaty 1922. Designed for Lexington (CC-1) battlecruisers and South Dakota (BB-49) battleships. Status: Never entered service - 71 guns completed but ships cancelled | Disposition: Most transferred to US Army coastal defense | Rate of Fire: 2 rpm (designed) | Weight: 128.15 tons (130.2 mt) | Barrel Length: 800 in (66.7 ft) bore length | Rifling: 96 grooves, Mod 0: increasing RH 1 in 50 to 1 in 32, Mod 1: uniform RH 1 in 32 | Chamber: 30,000 in³'
);

-- Gun 399: 16"/45 Mark 5/8 (Modernized Colorado-class)
INSERT INTO Guns (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    399,
    NULL,
    'USA',
    '16"',
    '/45',
    'Mark 5/8',
    1938,
    117.9,
    0,
    '16"/45 (40.6 cm) Mark 5 and Mark 8 - Modernized version of Mark 1 for Colorado class. Mark 5 and Mark 8 differ in rifling and chromium plating. Ships: USS Colorado (BB-45), USS Maryland (BB-46), USS West Virginia (BB-48) rebuilt | Barrel Life: 320 rounds (Mark 5), 395 rounds (Mark 8) | Rate of Fire: 1.5-2 rpm | Limitation: Could NOT fire 2,700 lb super-heavy projectile | Weight: 235,796 lbs (118 tons with breech), 230,948 lbs (115 tons without breech) | Barrel Length: 720 in (60 ft) bore length | Rifling: 96 grooves, Mark 5: increasing RH 1 in 50 to 1 in 32, Mark 8: uniform RH 1 in 25 | Chamber: 23,506 in³'
);

-- Gun 400: 16"/45 Mark 6 (North Carolina & South Dakota-class)
INSERT INTO Guns (Gun_ID, Turret_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    400,
    NULL,
    'USA',
    '16"',
    '/45',
    'Mark 6',
    1941,
    96.16,
    0,
    '16"/45 (40.6 cm) Mark 6 - Lighter, more advanced design than Mark 1. Could fire heavier 2,700 lb super-heavy AP projectile. Ships: USS North Carolina (BB-55) class, USS South Dakota (BB-57) class | Barrel Life: 395 rounds (AP) | Rate of Fire: 2 rpm | Elevation: -5° to +45° | Improvement: Stronger construction allowed use of 2,700 lb Mark 8 AP shell | Weight: 192,310 lbs (96 tons without breech) | Barrel Length: 720 in (60 ft) bore length | Rifling: 96 grooves, uniform RH 1 in 25 (Mod 1/2) | Chamber: 23,195 in³'
);
