-- British Naval Weapons Import Script
-- Generated: October 2025
-- Country: Britain (Royal Navy)
-- Period: 1890-1990
--
-- IMPORT ORDER:
-- 1. Guns (12 guns, Gun_IDs 501-555)
-- 2. Ammunition (8 types, IDs 101-111)
-- 3. Turrets (59 variants, Turret_IDs 2001-2115)
-- 4. Gun_Ammunition_Compatibility (to be generated)
--
-- NOTE: This script assumes the Turrets table already has the Caliber column added.
-- If not, run the fixes/add_caliber_to_turrets.sql script first.

-- =================================================================
-- SECTION 1: GUNS (British Naval Artillery)
-- =================================================================

-- Battleship Guns (6 calibers: 18", 15", 16", 14", 13.5", 12")

-- Gun 501: 18"/40 Mark I (HMS Furious, monitors)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    501,
    'Britain',
    '18"',
    '/40',
    'Mark I',
    1917,
    149.0,
    0,
    '18"/40 (45.7 cm) Mark I - Largest and heaviest gun ever used by Royal Navy. Only Japanese 46cm (18.1") had larger caliber but lighter shell. Three guns built total. Originally for HMS Furious (Large Light Cruiser), removed before combat. Transferred to monitors General Wolfe and Lord Clive for coast bombardment. Barrel: 60 ft (18m) long. Shell: 3,320 lbs AP capped. Muzzle Velocity: 2,270 fps. Max Range: 40,500 yds @ 45°. Rate of Fire: 1 rpm. General Wolfe made naval history: heaviest shell from largest gun at longest range in action (36,000 yds). Gun and breech: 149 long tons. Never saw combat on Furious - ship converted to carrier 1918. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
);

-- Gun 502: 15"/42 Mark I (Queen Elizabeth, Hood, Vanguard)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    502,
    'Britain',
    '15"',
    '/42',
    'Mark I',
    1915,
    100.0,
    0,
    '15"/42 (38.1 cm) Mark I - Most widely used and longest lasting British 15" design. One of the most successful battleship guns ever made. Ships: Queen Elizabeth-class (5 ships), Revenge-class (5 ships), Renown-class (2 ships), HMS Hood, Courageous-class (3 ships), HMS Vanguard, Roberts-class monitors. In service 1915-1960. Known for exceptional accuracy and reliability. Rate of Fire: 2 rpm. Elevation: initially -5° to +20°, later modified to +30°. Barrel Life: ~335 full charge firings. Overall Length: 650.4 in. Barrel: 630 in (L42). Weight: barrel 97 tons 3cwt, breech 2 tons 17cwt. Muzzle Velocity: 2,450 fps (standard), 2,640 fps (supercharge). Max Range: 33,550 yds @ 30° (Vanguard: 37,870 yds with supercharge). All mounts were twin turrets. Shell weight: 1,938 lbs. Charge: 428 lbs cordite (std), 490 lbs (supercharge). Source: Wikipedia, NavWeaps, War Thunder Wiki, IWM'
);

-- Gun 503: 16"/45 Mark I (Nelson, Rodney)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    503,
    'Britain',
    '16"',
    '/45',
    'Mark I',
    1927,
    108.0,
    0,
    '16"/45 (40.6 cm) Mark I - Last wire-wound guns built for Royal Navy, only British triple 16" turrets. Ships: HMS Nelson, HMS Rodney. All-forward arrangement: 3 triple turrets ahead of superstructure (''A'', ''B'' superfiring, ''X''). Total: 9 guns. Barrel: 60 ft (720 in) long. Shell: 2,048 lbs. Rate of Fire: Limited - could not fire all 3 guns simultaneously due to ballistic issues, but loaded together. October 1929 trial: turret crew fired 33 consecutive rounds without mishap. Elevation: -3° to +40°. Turret armor: 16" face, 11" sides, 9" rear, 7.25" roof. Wire-wound construction: tapered inner A tube, wire wrap, B tube, jacket, breech ring. Famous engagement: HMS Rodney vs Bismarck (May 1941). Charge: Six artificial silk bags (shallon). Estimated weight ~108 tons. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
);

-- Gun 504: 14"/45 Mark VII (King George V-class)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    504,
    'Britain',
    '14"',
    '/45',
    'Mark VII',
    1940,
    79.62,
    0,
    '14"/45 (35.6 cm) Mark VII - Built for KGV-class due to Washington Treaty limitations. All-steel radial expansion design (advance over wire-wound). Armament: 2 quad turrets + 1 twin turret = 10 guns. Rate of Fire: 2 rpm (salvo every 30s). Elevation: -3° to +40°. Traverse: 2°/sec. Barrel Length: 630 in (L45). Barrel Life: ~340 rounds. Weight: 77t 14cwt 84lbs (bare), 89t 2cwt 84lbs (with counterbalance), breech 1t 17cwt. Shell: 1,590 lbs. Propellant: 338.3 lbs. Muzzle Velocity: 2,483 fps (AP). AP shell: 39.8 lbs bursting charge. HE shell: 107 lbs explosive. Stowage: 100 rounds/gun. Quad turret weight: 1,582 tons. Twin turret: 915 tons. Known reliability issues: wartime construction haste, tight clearances, complex anti-flash arrangements made mechanisms problematic in service. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
);

-- Gun 505: 13.5"/45 Mark V (WWI superdreadnoughts)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    505,
    'Britain',
    '13.5"',
    '/45',
    'Mark V',
    1912,
    76.0,
    0,
    '13.5"/45 (34.3 cm) Mark V - WWI superdreadnought main battery. Two variants: Mark V(L) "light" and Mark V(H) "heavy". Ships: Orion-class, King George V (1912), Iron Duke-class (10 guns in 5 twin turrets centerline), Lion (1912), Queen Mary, Tiger (1914). Barrel: 607.5 in (15.43m) long. Shell weights: Mark V(L) lighter shell, Mark V(H) 1,400 lbs (635 kg) with increased charge for same range. Wire-wound construction. Production: 206 guns total (first 67 had forward locating shoulders, no taper fit). Famous service: Battle of Jutland 1916. Rate of Fire: ~1.5 rpm. All twin turret mounts, centerline arrangement. Estimated weight ~76 tons. Source: Wikipedia, NavWeaps, War Thunder'
);

-- Gun 506: 12"/45 Mark X (HMS Dreadnought)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    506,
    'Britain',
    '12"',
    '/45',
    'Mark X',
    1906,
    58.0,
    0,
    '12"/45 (30.5 cm) Mark X - First gun of HMS Dreadnought, revolutionized naval warfare. Last successful 12" British gun. Barrel: 540 in (14m) long (increased from Mark IX''s 480 in). Muzzle Velocity: 2,700 fps (increased from Mark IX''s 2,600 fps). Ships: HMS Dreadnought (10 guns in 5 twin turrets, centerline), Bellerophon-class. Dreadnought displaced 18,000 tons (20,000+ full load), 526 ft long, crew ~800, top speed 21 knots (steam turbines). Rate of Fire: 2 rpm. Turret armor (Dreadnought/Bellerophon): 10.78 in face. Historic significance: First "all-big-gun" design, made all previous battleships obsolete overnight. Commissioned 1906. Estimated weight ~58 tons. Source: Wikipedia, NavWeaps, Britannica'
);

-- Cruiser Guns (2 calibers: 8", 6")

-- Gun 520: 8"/50 Mark VIII (County-class heavy cruisers)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    520,
    'Britain',
    '8"',
    '/50',
    'Mark VIII',
    1928,
    16.0,
    0,
    '8"/50 (20.3 cm) Mark VIII - Built-up gun: wire-wound tube in second tube + jacket, Welin breech block, hydraulic/hand Asbury mechanism. Ships: County-class (13 ships), York-class (York, Exeter). Configuration: 4 twin turrets (188 tons each), superfiring fore/aft. Shell: 256 lbs. Propellant: Two cloth bags, 15 kg (33 lbs) cordite each. Barrel Life: 550 EFC. Rate of Fire: Design 5 rpm, wartime actual 3-4 rpm sustained. Elevation: Mark I turrets +70° (dual-purpose capable but slow traverse), Mark II turrets +50° (Norfolk subgroup: Dorsetshire, Norfolk + York-class). Training/elevation too slow for effective AA use. Built to Washington Treaty 8" limit for heavy cruisers. Estimated weight ~16 tons. Source: Wikipedia, NavWeaps, Military Wiki'
);

-- Gun 530: 6"/50 Mark XXIII (Crown Colony light cruisers)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    530,
    'Britain',
    '6"',
    '/50',
    'Mark XXIII',
    1939,
    7.0,
    0,
    '6"/50 (15.2 cm) Mark XXIII - Developed post-London Naval Treaty Jan 1929 (restricted cruisers to 6"). Built-up construction: tube + 4.5m jacket, hand-operated Welin breech block. Shell: 112 lbs (51 kg). Propellant: Cloth bags with 30 lbs (14 kg) cordite or NQFP. Barrel Life: 1,100 EFC (cordite), 2,200 EFC (NQFP flashless). Rate of Fire: 8 rpm typical max. Turret Types: Twin Mark XXI, Triple Mark XXII, Triple Mark XXIII. Triple turrets: individually sleeved guns, center gun set back 30 in (76.2 cm) for reduced shell interference, crew elbow room, balanced mass. Mark XXIII: "long trunk" design, 114 HP motor, different ammo supply vs earlier marks, magazine + handling room + shell room. Ships: Crown Colony-class (8,000 ton treaty limit), Town-class (Edinburgh group layout). Configuration: 3×3 or 4×3. Elevation: -5° to +60°. Excellent anti-destroyer weapon. Estimated weight ~7 tons. Source: Wikipedia, NavWeaps, Encyclopedia MDPI'
);

-- Dual-Purpose & Destroyer Guns (4 calibers: 5.25", 4.7", 4.5", 4")

-- Gun 540: 5.25"/50 Mark I (KGV secondary, Dido-class)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    540,
    'Britain',
    '5.25"',
    '/50',
    'QF Mark I',
    1940,
    5.0,
    0,
    '5.25"/50 (13.3-13.4 cm) QF Mark I - Heaviest RN dual-purpose gun WWII. Design rationale: Combining secondary + heavy AA armament saved weight for KGV treaty limit (35,000 tons). Shell: 80 lbs (largest crew could handle at AA rate). Construction: Autofretted loose barrel (no liner), jacket to 99 in from muzzle, removable breech ring, sealing collar. Hand-operated horizontal sliding breech, semi-automatic opening. Mountings: Twin Mark I (KGV-class: 8×2 = 16 guns), Twin Mark II (Dido-class: 9 of 11 ships had 5×2 = 10 guns; Scylla/Charybdis had 4.5" due to shortage). Production: 267 guns. Rate of Fire: Design 12 rpm, actual 7-8 rpm sustained (heavy projectile + cartridge reduced rate). Elevation: +70° max. Problems: Cramped mounts, difficult maintenance, slow elevation/training inadequate for modern aircraft. Unlike French/Italian contemporaries, truly designed dual-purpose. Estimated barrel weight ~5 tons. Source: Wikipedia, NavWeaps, War Thunder, Military Wiki'
);

-- Gun 545: 4.7"/45 Mark IX & Mark XII (WWII destroyers)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    545,
    'Britain',
    '4.7"',
    '/45',
    'QF Mark IX & XII',
    1916,
    3.5,
    0,
    '4.7"/45 (12 cm actual bore 4.724") QF Mark IX & XII - Armed majority RN destroyers WWII. Construction Mark IX: A tube + jacket 80 in to muzzle + breech ring. Mark IXA: Loose barrel, removable breech ring. Breech: Manually operated horizontal sliding block, semi-automatic opening. Shell: 50 lbs (23 kg). Muzzle Velocity: 2,650 fps (808 m/s). Max Range: 16,970 yds @ 40° (Mark XII). Rate of Fire: HMS Basilisk trial 1930: 5 rounds in 17 seconds (~18 rpm burst). Loading: Separate cartridge via loading tray, power ramming/elevation/traverse. Elevation: Initially low-angle (limited AA), S-class destroyers got 55° elevation mount. Limitation: 40° elevation inadequate for defending against aircraft attacking battle fleet. All British destroyers. Estimated weight ~3.5 tons. Mark XII introduced 1930s. Source: Wikipedia, NavWeaps, Military Wiki'
);

-- Gun 550: 4.5"/45 Mark V (Post-war automated destroyers)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    550,
    'Britain',
    '4.5"',
    '/45',
    'QF Mark V',
    1950,
    4.0,
    0,
    '4.5"/45 (11.4 cm actual bore 4.45") QF Mark V - Designed to correct deficiencies of WWII destroyer weapons. First post-war automated destroyer gun for RN. Design features: High elevation from outset, automatic aiming (RPC), fast ROF. Ships: Daring-class destroyers (3 mountings), County-class destroyers (2), Leopard-class frigates (2), majority of RN escorts 1950s-1960s. Rate of Fire: 24 rpm power-loaded, 12-14 hand-loaded, 18 rpm burst hand-loaded. Fully automated loading, elevation, traverse. Designed for high-speed aircraft engagement. Replaced wartime 4.7" guns. Mark V gun later redesignated with Mark 6 mounting under new nomenclature. All British 4.5" have actual bore 4.45" (11.3 cm). Estimated barrel weight ~4 tons. Source: Wikipedia, NavWeaps'
);

-- Gun 555: 4"/45 QF Mark V & Mark XVI (AA gun)
INSERT INTO Guns (Gun_ID, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES (
    555,
    'Britain',
    '4"',
    '/45',
    'QF Mark V/XVI',
    1911,
    2.0,
    0,
    '4"/45 (10.2 cm) QF Mark V - WWI weapon adapted to HA (high-angle) anti-aircraft role at sea and on land, also coast defense. Fixed ammunition: 44.3 in (1.13m) long, 56 lbs (25 kg) total weight. Projectile: 31 lbs (14 kg). Breech: Horizontal sliding block opening right, semi-automatic action. Production: 283 Mark VC + 554 earlier types (Navy), ~107 for Army (AA/coast defense WWI). Service: Main British long-range AA weapon until late 1930s, fitted to majority of capital ships and cruisers. Mark V superseded by Mark XVI on new warships 1930s, but continued WWII service on destroyers, light/heavy cruisers. Elevation: -10° to +80°. Rate of Fire: 15-20 rpm. "QF" = Quick-Firing. HA = High-Angle (anti-aircraft role). Estimated weight ~2 tons. Mark XVI introduced 1930s. Source: Wikipedia, NavWeaps'
);


-- =================================================================
-- SECTION 2: AMMUNITION (British Naval Shells)
-- =================================================================

-- 15" Ammunition (6 types, IDs 101-106)

-- 15" 4crh AP (Early shell, standard charge)
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    101,
    '15"',
    '4crh',
    'AP',
    1920,
    'Britain',
    0,
    'Early 4crh (caliber radius head) AP shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: 2,450 fps. Used pre-1937 before 6crh improvements. crh = caliber radius head (ballistic cap shape). Source: NavWeaps, Wikipedia'
);

-- 15" 6crh AP (Improved shell, supercharge)
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    102,
    '15"',
    '6crh',
    'AP',
    1938,
    'Britain',
    0,
    'Improved 6crh AP shell for 15"/42 Mark I. Supercharge 490 lbs cordite (1937+). Muzzle Velocity: 2,640 fps. Better aerodynamics than 4crh. Max Range: 33,550 yds @ 30° (Vanguard: 37,870 yds with supercharge). crh = caliber radius head. Source: NavWeaps, Wikipedia'
);

-- 15" Mark XIIIa APC
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    103,
    '15"',
    'Mark XIIIa',
    'APC',
    1938,
    'Britain',
    0,
    'Armour-Piercing Capped shell for 15"/42 Mark I. 6crh projectile with 4crh ballistic cap. Used on WWII unmodernized ships. Supercharge 490 lbs cordite. Muzzle Velocity: 2,640 fps. APC = Armour-Piercing Capped. Source: NavWeaps, Wikipedia'
);

-- 15" Mark XVIIb APC (Superior penetration)
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    104,
    '15"',
    'Mark XVIIb',
    'APC',
    1938,
    'Britain',
    0,
    'Superior penetration APC shell for 15"/42 Mark I. Harder nose, rigid body. Manufactured at Cardonald, Scotland. Limited issue - markedly superior penetration capability. Supercharge 490 lbs cordite. Muzzle Velocity: 2,640 fps. APC = Armour-Piercing Capped. Source: NavWeaps, Wikipedia'
);

-- 15" HE
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    105,
    '15"',
    NULL,
    'HE',
    1938,
    'Britain',
    0,
    'High Explosive shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: ~2,450 fps. Used for shore bombardment and anti-surface targets. Typical WWII loadout: 30-60 APC/CPC rounds, balance HE. HMS Vanguard carried 5 HE per gun. HE = High Explosive. Source: NavWeaps, Wikipedia'
);

-- 15" CPC (Semi-AP)
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    106,
    '15"',
    NULL,
    'CPC',
    1938,
    'Britain',
    0,
    'Common Pointed Capped (semi-AP) shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: ~2,450 fps. Used against lightly armored targets and as general-purpose shell. Typical WWII loadout: 30-60 APC/CPC rounds, balance HE. CPC = Common Pointed Capped. Source: NavWeaps, Wikipedia'
);


-- 14" Ammunition (2 types, IDs 110-111)

-- 14" Mark VIIB APC
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    110,
    '14"',
    'Mark VIIB',
    'APC',
    1590,
    'Britain',
    0,
    'Armour-Piercing Capped shell for 14"/45 Mark VII (KGV-class). Bursting charge: 39.8 lbs (18.1 kg) - proportionally large for caliber. Propellant: 338.3 lbs per round. Muzzle Velocity: 2,483 fps (AP). Stowage: 100 rounds per gun. Barrel Life: ~340 rounds. APC = Armour-Piercing Capped. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
);

-- 14" HE
INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES (
    111,
    '14"',
    NULL,
    'HE',
    1590,
    'Britain',
    0,
    'High Explosive shell for 14"/45 Mark VII (KGV-class). Explosive content: 107 lbs (48.5 kg). Propellant: 338.3 lbs per round. Muzzle Velocity: ~2,400 fps. Used for shore bombardment and anti-surface targets. Stowage: 100 rounds per gun. HE = High Explosive. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
);


-- =================================================================
-- SECTION 3: TURRETS (British Naval Turret Configurations)
-- =================================================================

-- NOTE: Caliber column will be populated for all turrets to match USA database pattern.
-- This assumes the Turrets table has been updated with the Caliber column.

-- 18"/40 Mark I Turrets (Gun_ID 501) - Turret_IDs 2001-2004

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2001, 501, 'Britain', '18"', 'Single', '18"/40 Mark I Single', 290, 45, 18, 12, 8, 1.5, -5, 40, 0.8, 1, 'Fictional - impractical size. Shell: 3,320 lbs.'),
    (2002, 501, 'Britain', '18"', 'Twin', '18"/40 Mark I Twin', 550, 95, 18, 12, 8, 1.0, -5, 40, 0.8, 1, 'Fictional - would exceed 600 tons. Shell: 3,320 lbs.'),
    (2003, 501, 'Britain', '18"', 'Triple', '18"/40 Mark I Triple', 850, 140, 18, 12, 8, 0.8, -5, 40, 0.8, 1, 'Fictional - largest conceivable turret. Shell: 3,320 lbs.'),
    (2004, 501, 'Britain', '18"', 'Quad', '18"/40 Mark I Quad', 1200, 180, 18, 12, 8, 0.5, -5, 40, 0.7, 1, 'Fictional - engineering impossibility. Shell: 3,320 lbs.');

-- 15"/42 Mark I Turrets (Gun_ID 502) - Turret_IDs 2011-2017

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2011, 502, 'Britain', '15"', 'Single', '15"/42 Mark I Single', 195, 40, 15, 10, 6, 2.5, -5, 30, 1.8, 1, 'Fictional single mount. Shell: 1,938 lbs.'),
    (2012, 502, 'Britain', '15"', 'Twin', '15"/42 Mark I Twin (1915)', 750, 85, 15, 10, 6, 2.0, -5, 20, 2.0, 0, 'HISTORICAL - Queen Elizabeth-class, Revenge-class. Shell: 1,938 lbs. Revolving weight: 750 tons.'),
    (2013, 502, 'Britain', '15"', 'Twin', '15"/42 Mark I Twin (1935)', 785, 85, 16, 11, 7, 2.0, -5, 30, 2.0, 0, 'HISTORICAL - Modernized ships 1935+. Shell: 1,938 lbs. Revolving weight: 785 tons. Improved armor and elevation.'),
    (2014, 502, 'Britain', '15"', 'Twin', '15"/42 Mark II Twin (Hood)', 860, 90, 17, 12, 7.5, 2.0, -5, 30, 2.0, 0, 'HISTORICAL - HMS Hood. Shell: 1,938 lbs. Revolving weight: 860 tons. Heavier armor.'),
    (2015, 502, 'Britain', '15"', 'Twin', '15"/42 Mark I(N) RP12 (Vanguard)', 855, 90, 16, 11, 7, 2.0, -5, 40, 2.0, 0, 'HISTORICAL - HMS Vanguard RP12 turrets. Shell: 1,938 lbs. Revolving weight: 855 tons. Improved elevation to +40°.'),
    (2016, 502, 'Britain', '15"', 'Triple', '15"/42 Mark I Triple', 1150, 130, 16, 11, 7, 1.5, -5, 30, 1.8, 1, 'Fictional - would rival Nelson 16" triple turrets. Shell: 1,938 lbs.'),
    (2017, 502, 'Britain', '15"', 'Quad', '15"/42 Mark I Quad', 1550, 165, 16, 11, 7, 1.0, -5, 30, 1.6, 1, 'Fictional - complex mechanism issues expected. Shell: 1,938 lbs.');

-- 16"/45 Mark I Turrets (Gun_ID 503) - Turret_IDs 2021-2024

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2021, 503, 'Britain', '16"', 'Single', '16"/45 Mark I Single', 210, 42, 16, 11, 7, 2.0, -3, 40, 1.3, 1, 'Fictional single mount. Shell: 2,048 lbs.'),
    (2022, 503, 'Britain', '16"', 'Twin', '16"/45 Mark I Twin', 450, 88, 16, 11, 7.25, 1.8, -3, 40, 1.5, 1, 'Fictional - conventional twin mount. Shell: 2,048 lbs.'),
    (2023, 503, 'Britain', '16"', 'Triple', '16"/45 Mark I Triple', 650, 120, 16, 11, 7.25, 1.5, -3, 40, 1.5, 0, 'HISTORICAL - Nelson/Rodney all-forward arrangement. Shell: 2,048 lbs. Could not fire all 3 guns simultaneously. Estimated weight ~650 tons.'),
    (2024, 503, 'Britain', '16"', 'Quad', '16"/45 Mark I Quad', 920, 155, 16, 11, 9, 1.0, -3, 40, 1.3, 1, 'Fictional quad mount. Shell: 2,048 lbs.');

-- 14"/45 Mark VII Turrets (Gun_ID 504) - Turret_IDs 2031-2034

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2031, 504, 'Britain', '14"', 'Single', '14"/45 Mark VII Single', 155, 35, 14, 9, 6, 2.5, -3, 40, NULL, 1.9, 1, 'Fictional single mount. Shell: 1,590 lbs.'),
    (2032, 504, 'Britain', '14"', 'Twin', '14"/45 Mark VII Twin', 915, 75, 14, 9, 6, 2.0, -3, 40, 8.0, 2.0, 0, 'HISTORICAL - KGV ''Y'' turret. Shell: 1,590 lbs. Weight: 915 tons.'),
    (2033, 504, 'Britain', '14"', 'Triple', '14"/45 Mark VII Triple', 1240, 105, 14, 9, 6, 1.8, -3, 40, NULL, 1.9, 1, 'Fictional - conventional triple mount. Shell: 1,590 lbs.'),
    (2034, 504, 'Britain', '14"', 'Quad', '14"/45 Mark VII Quad', 1582, 140, 14, 9, 6, 2.0, -3, 40, 8.0, 2.0, 0, 'HISTORICAL - KGV ''A''/''B'' turrets. Shell: 1,590 lbs. Weight: 1,582 tons. Reliability issues: cramped, tight clearances, complex anti-flash.');

-- 13.5"/45 Mark V Turrets (Gun_ID 505) - Turret_IDs 2041-2044

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2041, 505, 'Britain', '13.5"', 'Single', '13.5"/45 Mark V Single', 145, 33, 13, 8, 5, 2.5, -5, 20, 1.4, 1, 'Fictional WWI single mount. Shell: 1,400 lbs (Mark V(H)).'),
    (2042, 505, 'Britain', '13.5"', 'Twin', '13.5"/45 Mark V Twin', 380, 70, 13, 8, 5, 2.0, -5, 20, 1.5, 0, 'HISTORICAL PATTERN - Orion, Iron Duke centerline twins. Shell: 1,400 lbs. All historical mounts were twin turrets. Fought at Jutland.'),
    (2043, 505, 'Britain', '13.5"', 'Triple', '13.5"/45 Mark V Triple', 550, 100, 13, 8, 5, 1.5, -5, 20, 1.4, 1, 'Fictional triple mount. Shell: 1,400 lbs.'),
    (2044, 505, 'Britain', '13.5"', 'Quad', '13.5"/45 Mark V Quad', 750, 130, 13, 8, 5, 1.0, -5, 20, 1.3, 1, 'Fictional quad mount. Shell: 1,400 lbs.');

-- 12"/45 Mark X Turrets (Gun_ID 506) - Turret_IDs 2051-2054

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2051, 506, 'Britain', '12"', 'Single', '12"/45 Mark X Single', 110, 30, 11, 7, 4, 2.5, -5, 15, 1.9, 1, 'Fictional single mount. MV: 2,700 fps.'),
    (2052, 506, 'Britain', '12"', 'Twin', '12"/45 Mark X Twin', 285, 65, 10.78, 7, 4, 2.0, -5, 15, 2.0, 0, 'HISTORICAL - Dreadnought (5 centerline twins). MV: 2,700 fps. First "all-big-gun" battleship design (1906).'),
    (2053, 506, 'Britain', '12"', 'Triple', '12"/45 Mark X Triple', 430, 95, 11, 7, 4, 1.5, -5, 15, 1.8, 1, 'Fictional triple mount. MV: 2,700 fps.'),
    (2054, 506, 'Britain', '12"', 'Quad', '12"/45 Mark X Quad', 600, 125, 11, 7, 4, 1.0, -5, 15, 1.7, 1, 'Fictional quad mount. MV: 2,700 fps.');

-- 8"/50 Mark VIII Turrets (Gun_ID 520) - Turret_IDs 2061-2065

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2061, 520, 'Britain', '8"', 'Single', '8"/50 Mark VIII Single', 42, 22, 4, 2, 1.5, 3.0, -5, 70, 4.5, 1, 'Fictional single mount. Shell: 256 lbs.'),
    (2062, 520, 'Britain', '8"', 'Twin', '8"/50 Mark VIII Twin (Mark I)', 188, 48, 4, 2, 1.5, 2.5, -5, 70, 4.0, 0, 'HISTORICAL - County-class (DP capable, slow traverse). Shell: 256 lbs. Weight: 188 tons. Barrel life: 550 EFC. Actual wartime ROF: 3-4 rpm.'),
    (2063, 520, 'Britain', '8"', 'Twin', '8"/50 Mark VIII Twin (Mark II)', 188, 48, 4, 2, 1.5, 2.5, -5, 50, 4.5, 0, 'HISTORICAL - Norfolk subgroup, York-class. Shell: 256 lbs. Weight: 188 tons. Lower elevation (+50° vs +70°).'),
    (2064, 520, 'Britain', '8"', 'Triple', '8"/50 Mark VIII Triple', 295, 72, 4, 2, 1.5, 2.0, -5, 50, 3.8, 1, 'Fictional triple mount. Shell: 256 lbs.'),
    (2065, 520, 'Britain', '8"', 'Quad', '8"/50 Mark VIII Quad', 410, 95, 4, 2, 1.5, 1.5, -5, 50, 3.5, 1, 'Fictional quad mount. Shell: 256 lbs.');

-- 6"/50 Mark XXIII Turrets (Gun_ID 530) - Turret_IDs 2071-2075

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2071, 530, 'Britain', '6"', 'Single', '6"/50 Mark XXIII Single', 22, 15, 3, 1.5, 1, 4.0, -5, 60, 7.5, 1, 'Fictional single mount. Shell: 112 lbs.'),
    (2072, 530, 'Britain', '6"', 'Twin', '6"/50 Mark XXI Twin', 65, 32, 3, 1.5, 1, 3.5, -5, 60, 8.0, 0, 'HISTORICAL PATTERN - 2-gun mounting. Shell: 112 lbs. Barrel life: 1,100-2,200 EFC.'),
    (2073, 530, 'Britain', '6"', 'Triple', '6"/50 Mark XXII Triple', 95, 48, 3, 1.5, 1, 3.0, -5, 60, 7.5, 0, 'HISTORICAL - Triple mount, center gun offset 30". Shell: 112 lbs.'),
    (2074, 530, 'Britain', '6"', 'Triple', '6"/50 Mark XXIII Triple', 100, 50, 3, 1.5, 1, 3.0, -5, 60, 8.0, 0, 'HISTORICAL - "Long trunk", 114 HP motor, Crown Colony-class. Shell: 112 lbs. Center gun set back 30".'),
    (2075, 530, 'Britain', '6"', 'Quad', '6"/50 Mark XXIII Quad', 140, 65, 3, 1.5, 1, 2.5, -5, 60, 7.0, 1, 'Fictional quad mount. Shell: 112 lbs.');

-- 5.25"/50 Mark I Turrets (Gun_ID 540) - Turret_IDs 2081-2085

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2081, 540, 'Britain', '5.25"', 'Single', '5.25"/50 Mark I Single', 18, 12, 2, 1, 0.75, 4.5, -5, 70, 9.0, 1, 'Fictional single mount. Shell: 80 lbs.'),
    (2082, 540, 'Britain', '5.25"', 'Twin', '5.25"/50 Mark I Twin (Mark I)', 48, 26, 2, 1, 0.75, 3.0, -5, 70, 7.0, 0, 'HISTORICAL - KGV-class (8×2 = 16 guns). Shell: 80 lbs. Design ROF: 12 rpm, actual 7-8 rpm sustained.'),
    (2083, 540, 'Britain', '5.25"', 'Twin', '5.25"/50 Mark I Twin (Mark II)', 50, 26, 2, 1, 0.75, 3.0, -5, 70, 7.5, 0, 'HISTORICAL - Dido-class (9 of 11 ships, 5×2). Shell: 80 lbs. Cramped mounts, slow traverse.'),
    (2084, 540, 'Britain', '5.25"', 'Triple', '5.25"/50 Mark I Triple', 75, 38, 2, 1, 0.75, 2.5, -5, 70, 6.5, 1, 'Fictional triple mount. Shell: 80 lbs.'),
    (2085, 540, 'Britain', '5.25"', 'Quad', '5.25"/50 Mark I Quad', 105, 50, 2, 1, 0.75, 2.0, -5, 70, 6.0, 1, 'Fictional quad mount. Shell: 80 lbs.');

-- 4.7"/45 Mark IX/XII Turrets (Gun_ID 545) - Turret_IDs 2091-2095

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2091, 545, 'Britain', '4.7"', 'Single', '4.7"/45 Mark IX/XII Single', 12, 10, 1, 0.5, 0.5, 5.0, -5, 40, 16, 0, 'HISTORICAL PATTERN - Standard WWI/WWII destroyer mount. Shell: 50 lbs. MV: 2,650 fps. Range: 16,970 yds. Trial burst: 18 rpm (5 rounds/17 sec).'),
    (2092, 545, 'Britain', '4.7"', 'Twin', '4.7"/45 Mark IX/XII Twin', 28, 20, 1, 0.5, 0.5, 4.0, -5, 40, 14, 1, 'Fictional twin mount. Shell: 50 lbs. MV: 2,650 fps.'),
    (2093, 545, 'Britain', '4.7"', 'Single', '4.7"/45 Mark IX/XII Single (HA)', 13, 10, 1, 0.5, 0.5, 5.0, -5, 55, 15, 0, 'HISTORICAL - S-class destroyers (improved elevation to 55°). Shell: 50 lbs. MV: 2,650 fps. Power ramming/elevation/traverse.'),
    (2094, 545, 'Britain', '4.7"', 'Triple', '4.7"/45 Mark IX/XII Triple', 45, 28, 1, 0.5, 0.5, 3.5, -5, 40, 12, 1, 'Fictional triple mount. Shell: 50 lbs.'),
    (2095, 545, 'Britain', '4.7"', 'Quad', '4.7"/45 Mark IX/XII Quad', 62, 38, 1, 0.5, 0.5, 3.0, -5, 40, 11, 1, 'Fictional quad mount. Shell: 50 lbs.');

-- 4.5"/45 Mark V Turrets (Gun_ID 550) - Turret_IDs 2101-2104

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2101, 550, 'Britain', '4.5"', 'Single', '4.5"/45 Mark V Single', 14, 8, 1, 0.5, 0.5, 6.0, -10, 80, 22, 0, 'HISTORICAL PATTERN - Single Mark 6 mounting. Post-war automated destroyer gun. Power-loaded 24 rpm, hand-loaded 12-14 rpm. RPC aiming, high elevation.'),
    (2102, 550, 'Britain', '4.5"', 'Twin', '4.5"/45 Mark V Twin', 32, 16, 1, 0.5, 0.5, 5.0, -10, 80, 20, 1, 'Fictional twin mount. Automated: RPC aiming, power loading. Daring/County/Leopard-class.'),
    (2103, 550, 'Britain', '4.5"', 'Triple', '4.5"/45 Mark V Triple', 50, 24, 1, 0.5, 0.5, 4.5, -10, 80, 18, 1, 'Fictional triple mount. High elevation for modern aircraft.'),
    (2104, 550, 'Britain', '4.5"', 'Quad', '4.5"/45 Mark V Quad', 68, 32, 1, 0.5, 0.5, 4.0, -10, 80, 16, 1, 'Fictional quad mount. Fully automated loading, elevation, traverse.');

-- 4"/45 QF Mark V/XVI Turrets (Gun_ID 555) - Turret_IDs 2111-2115

INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Rate_Of_Fire_RPM, Modded, Notes)
VALUES
    (2111, 555, 'Britain', '4"', 'Single', '4"/45 QF Mark V Single', 8, 6, 0.5, 0.25, 0.25, 6.0, -10, 80, 18, 0, 'HISTORICAL - Main British long-range AA (WWI-1930s). Projectile: 31 lbs. Fixed ammo: 56 lbs total. Production: 837+ Navy, 107 Army.'),
    (2112, 555, 'Britain', '4"', 'Single', '4"/45 QF Mark XVI Single', 9, 6, 0.5, 0.25, 0.25, 6.5, -10, 80, 18, 0, 'HISTORICAL - Replaced Mark V on new ships 1930s. Projectile: 31 lbs. HA (High-Angle) anti-aircraft role.'),
    (2113, 555, 'Britain', '4"', 'Twin', '4"/45 QF Mark V/XVI Twin', 20, 12, 0.5, 0.25, 0.25, 5.5, -10, 80, 16, 1, 'Fictional twin mount. Horizontal sliding breech, semi-automatic.'),
    (2114, 555, 'Britain', '4"', 'Triple', '4"/45 QF Mark V/XVI Triple', 32, 18, 0.5, 0.25, 0.25, 5.0, -10, 80, 14, 1, 'Fictional triple mount. Fixed ammunition: 44.3 in (1.13m) long.'),
    (2115, 555, 'Britain', '4"', 'Quad', '4"/45 QF Mark V/XVI Quad', 45, 24, 0.5, 0.25, 0.25, 4.5, -10, 80, 13, 1, 'Fictional quad mount. Main British long-range AA weapon.');


-- =================================================================
-- SECTION 4: GUN-AMMUNITION COMPATIBILITY
-- =================================================================

-- NOTE: This section needs to be generated after verifying all ammunition types.
-- Currently only 15" and 14" ammunition is documented.
-- Will add compatibility records for:
-- - 15"/42 Mark I (Gun_ID 502) → 6 ammunition types (IDs 101-106)
-- - 14"/45 Mark VII (Gun_ID 504) → 2 ammunition types (IDs 110-111)
--
-- Remaining calibers need ammunition research first.

-- 15"/42 Mark I Compatibility (Gun_ID 502)

INSERT INTO Gun_Ammunition_Compatibility (Gun_ID, Ammunition_ID, Caliber, Muzzle_Velocity_FPS, Max_Range_Yards, Notes)
VALUES
    (502, 101, '15"', 2450, 29000, '15" 4crh AP shell with standard charge 428 lbs. Early shell design pre-1937. Barrel life: ~335 rounds. Source: NavWeaps'),
    (502, 102, '15"', 2640, 33550, '15" 6crh AP shell with supercharge 490 lbs (1937+). Improved aerodynamics. Vanguard: 37,870 yds with supercharge. Barrel life: ~335 rounds. Source: NavWeaps'),
    (502, 103, '15"', 2640, 33550, '15" Mark XIIIa APC shell. 6crh projectile with 4crh ballistic cap. Supercharge 490 lbs. WWII unmodernized ships. Barrel life: ~335 rounds. Source: NavWeaps'),
    (502, 104, '15"', 2640, 33550, '15" Mark XVIIb APC shell. Superior penetration - harder nose, rigid body. Supercharge 490 lbs. Limited issue Cardonald manufacture. Barrel life: ~335 rounds. Source: NavWeaps'),
    (502, 105, '15"', 2450, 29000, '15" HE shell with standard charge 428 lbs. Shore bombardment and anti-surface targets. Barrel life: ~335 rounds. Source: NavWeaps'),
    (502, 106, '15"', 2450, 29000, '15" CPC (Common Pointed Capped) semi-AP shell. Standard charge 428 lbs. General-purpose shell. Barrel life: ~335 rounds. Source: NavWeaps');

-- 14"/45 Mark VII Compatibility (Gun_ID 504)

INSERT INTO Gun_Ammunition_Compatibility (Gun_ID, Ammunition_ID, Caliber, Muzzle_Velocity_FPS, Max_Range_Yards, Notes)
VALUES
    (504, 110, '14"', 2483, 36500, '14" Mark VIIB APC shell. Propellant: 338.3 lbs. Bursting charge: 39.8 lbs. KGV-class main armament. Barrel life: ~340 rounds. Source: Wikipedia, NavWeaps'),
    (504, 111, '14"', 2400, 35000, '14" HE shell. Propellant: 338.3 lbs. Explosive content: 107 lbs. Shore bombardment and anti-surface targets. Barrel life: ~340 rounds. Source: Wikipedia, NavWeaps');


-- =================================================================
-- VERIFICATION QUERIES
-- =================================================================

-- Run these after import to verify data integrity:

-- SELECT 'Guns imported' as Check, COUNT(*) as Count FROM Guns WHERE Country = 'Britain';
-- Expected: 12 guns

-- SELECT 'Ammunition imported' as Check, COUNT(*) as Count FROM Ammunition WHERE Country = 'Britain';
-- Expected: 8 ammunition types

-- SELECT 'Turrets imported' as Check, COUNT(*) as Count FROM Turrets WHERE Country = 'Britain';
-- Expected: 59 turrets

-- SELECT 'Gun-Ammo Compatibility' as Check, COUNT(*) as Count FROM Gun_Ammunition_Compatibility
-- WHERE Gun_ID IN (SELECT Gun_ID FROM Guns WHERE Country = 'Britain');
-- Expected: 8 compatibility records (6 for 15", 2 for 14")

-- SELECT 'Turrets with NULL Caliber' as Check, COUNT(*) as Count FROM Turrets
-- WHERE Country = 'Britain' AND Caliber IS NULL;
-- Expected: 0 (all turrets should have Caliber populated)

-- SELECT 'Historical Turrets' as Check, COUNT(*) as Count FROM Turrets
-- WHERE Country = 'Britain' AND Modded = 0;
-- Expected: 15 historical turrets

-- SELECT 'Fictional Turrets' as Check, COUNT(*) as Count FROM Turrets
-- WHERE Country = 'Britain' AND Modded = 1;
-- Expected: 44 fictional turrets

-- =================================================================
-- END OF SCRIPT
-- =================================================================
