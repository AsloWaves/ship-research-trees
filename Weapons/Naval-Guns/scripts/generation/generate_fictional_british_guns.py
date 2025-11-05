"""
Generate 60 Fictional British Naval Guns
Expands British gun database to match USA detail level
Gun IDs: 560-619
"""

# Gun specifications by caliber
fictional_guns = []

# 18" Guns (+2 variants) - Gun IDs 560-561
fictional_guns.extend([
    {
        'Gun_ID': 560,
        'Country': 'Britain',
        'Caliber': '18"',
        'Length': '/42',
        'Mark_Designation': 'Mark II',
        'Year_Introduced': 1920,
        'Weight': 145.0,
        'Modded': 1,
        'Notes': '18"/42 Mark II - Improved Mark I with lighter construction. Proposed for G3 battlecruiser (cancelled). Wire-wound barrel, improved chamber design. Shell: 3,320 lbs. MV: 2,350 fps. Weight reduction: 4 tons vs Mark I. Never built due to Washington Naval Treaty 1922. Theoretical range: 42,000 yds @ 45°. Fictional - design study only.'
    },
    {
        'Gun_ID': 561,
        'Country': 'Britain',
        'Caliber': '18"',
        'Length': '/45',
        'Mark_Designation': 'Mark III',
        'Year_Introduced': 1941,
        'Weight': 152.0,
        'Modded': 1,
        'Notes': '18"/45 Mark III - Wartime experimental design. All-steel radial expansion construction (no wire-wound). Shell: 3,450 lbs super-heavy AP. MV: 2,500 fps. Longer barrel for increased velocity. Proposed for Lion-class battleships (1939 design, cancelled 1944). Range: 44,500 yds @ 45°. Fictional - never progressed beyond design stage.'
    }
])

# 16" Guns (+3 variants) - Gun IDs 562-564
fictional_guns.extend([
    {
        'Gun_ID': 562,
        'Country': 'Britain',
        'Caliber': '16"',
        'Length': '/45',
        'Mark_Designation': 'Mark II',
        'Year_Introduced': 1932,
        'Weight': 110.0,
        'Modded': 1,
        'Notes': '16"/45 Mark II - Post-Nelson design study. Improved wire-wound construction, lighter weight. Shell: 2,048 lbs. MV: 2,575 fps (50 fps improvement). Proposed for cancelled 1930s battleship designs. Weight: 110 tons (2 tons lighter). Barrel life: 350 rounds (improved). Fictional - remained design study.'
    },
    {
        'Gun_ID': 562,
        'Country': 'Britain',
        'Caliber': '16"',
        'Length': '/45',
        'Mark_Designation': 'Mark III',
        'Year_Introduced': 1938,
        'Weight': 112.0,
        'Modded': 1,
        'Notes': '16"/45 Mark III - Pre-war modernization of Mark I. All-steel construction (abandoning wire-wound). Shell: 2,120 lbs heavier AP. MV: 2,525 fps. Improved barrel life: 380 rounds. Proposed for pre-war Lion-class battleships. Similar construction to 14" Mark VII. Fictional - design evolved into other projects.'
    },
    {
        'Gun_ID': 564,
        'Country': 'Britain',
        'Caliber': '16"',
        'Length': '/45',
        'Mark_Designation': 'Mark IV',
        'Year_Introduced': 1943,
        'Weight': 109.0,
        'Modded': 1,
        'Notes': '16"/45 Mark IV - Wartime production variant. Simplified Mark III for faster production. Shell: 2,048 lbs. MV: 2,525 fps. Reduced machining complexity, standardized tooling with 14" Mark VII. Proposed for 1943 Lion-class construction. Weight: 109 tons. Fictional - Lion-class cancelled before production.'
    }
])

# 15" Guns (+4 variants) - Gun IDs 565-568
fictional_guns.extend([
    {
        'Gun_ID': 565,
        'Country': 'Britain',
        'Caliber': '15"',
        'Length': '/42',
        'Mark_Designation': 'Mark II',
        'Year_Introduced': 1925,
        'Weight': 98.5,
        'Modded': 1,
        'Notes': '15"/42 Mark II - 1920s modernization of Mark I. Improved chamber design for supercharge from outset. Shell: 1,938 lbs. MV: 2,670 fps with supercharge (30 fps improvement). Barrel life: 350 rounds (improved vs 335). Proposed for Hood-class follow-ons. Weight: 98.5 tons (1.5 tons lighter). Fictional - interwar budget cuts.'
    },
    {
        'Gun_ID': 566,
        'Country': 'Britain',
        'Caliber': '15"',
        'Length': '/42',
        'Mark_Designation': 'Mark III',
        'Year_Introduced': 1930,
        'Weight': 100.0,
        'Modded': 1,
        'Notes': '15"/42 Mark III - Treaty-compliant variant. Designed to be easily upgraded to 16". Shell: 1,938 lbs. MV: 2,640 fps. Interchangeable parts with 16" Mark I where possible. Proposed for 1930s treaty battleship designs. All-steel construction prototype. Fictional - 14" chosen instead for KGV.'
    },
    {
        'Gun_ID': 567,
        'Country': 'Britain',
        'Caliber': '15"',
        'Length': '/45',
        'Mark_Designation': 'Mark IV',
        'Year_Introduced': 1938,
        'Weight': 105.0,
        'Modded': 1,
        'Notes': '15"/45 Mark IV - Pre-war improved design. Longer barrel: L/45 vs L/42. Shell: 1,938 lbs. MV: 2,750 fps (supercharge). Range: 39,000 yds @ 40°. All-steel radial expansion construction. Proposed for 1937 Lion-class battleships. Weight: 105 tons. Barrel life: 320 rounds. Fictional - 14" chosen for KGV, 16" for Lion.'
    },
    {
        'Gun_ID': 568,
        'Country': 'Britain',
        'Caliber': '15"',
        'Length': '/42',
        'Mark_Designation': 'Mark V',
        'Year_Introduced': 1942,
        'Weight': 99.0,
        'Modded': 1,
        'Notes': '15"/42 Mark V - Wartime production variant. Simplified Mark I for faster production. Shell: 1,938 lbs. MV: 2,640 fps. Reduced peacetime machining standards, maintained performance. Proposed for emergency battleship construction 1942-1943. Weight: 99 tons. Fictional - resources allocated to other programs.'
    }
])

# 14" Guns (+3 variants) - Gun IDs 569-571
fictional_guns.extend([
    {
        'Gun_ID': 569,
        'Country': 'Britain',
        'Caliber': '14"',
        'Length': '/45',
        'Mark_Designation': 'Mark VIII',
        'Year_Introduced': 1943,
        'Weight': 78.5,
        'Modded': 1,
        'Notes': '14"/45 Mark VIII - Improved reliability variant of Mark VII. Addressed KGV-class mechanism issues: increased clearances, simplified anti-flash arrangements, improved loading cycle. Shell: 1,590 lbs. MV: 2,483 fps. Weight: 78.5 tons. ROF: 2.5 rpm (improved from 2 rpm). Fictional - wartime lessons applied.'
    },
    {
        'Gun_ID': 570,
        'Country': 'Britain',
        'Caliber': '14"',
        'Length': '/45',
        'Mark_Designation': 'Mark IX',
        'Year_Introduced': 1944,
        'Weight': 75.0,
        'Modded': 1,
        'Notes': '14"/45 Mark IX - Lightweight variant. Weight reduction through improved metallurgy. Shell: 1,590 lbs. MV: 2,483 fps. Weight: 75 tons (4.6 tons lighter than Mark VII). Proposed for emergency battleship construction. Maintained strength through autofrettage. Barrel life: 340 rounds. Fictional - war ended before production.'
    },
    {
        'Gun_ID': 571,
        'Country': 'Britain',
        'Caliber': '14"',
        'Length': '/50',
        'Mark_Designation': 'Mark X',
        'Year_Introduced': 1955,
        'Weight': 82.0,
        'Modded': 1,
        'Notes': '14"/50 Mark X - Cold War modernization. Longer barrel L/50 vs L/45. Shell: 1,590 lbs. MV: 2,650 fps (167 fps improvement). Range: 38,500 yds @ 45°. Proposed for 1950s Vanguard modernization. Improved barrel life: 400 rounds. Fictional - guided missiles made large guns obsolete.'
    }
])

# 13.5" Guns (+2 variants) - Gun IDs 572-573
fictional_guns.extend([
    {
        'Gun_ID': 572,
        'Country': 'Britain',
        'Caliber': '13.5"',
        'Length': '/45',
        'Mark_Designation': 'Mark VI',
        'Year_Introduced': 1925,
        'Weight': 74.0,
        'Modded': 1,
        'Notes': '13.5"/45 Mark VI - Interwar modernization of Mark V. Improved chamber for higher-velocity loads. Shell: 1,400 lbs. MV: 2,575 fps (75 fps improvement). Proposed for Iron Duke-class modernization (1920s). Wire-wound construction maintained. Barrel life: 280 rounds. Fictional - scrapped instead of modernized.'
    },
    {
        'Gun_ID': 573,
        'Country': 'Britain',
        'Caliber': '13.5"',
        'Length': '/50',
        'Mark_Designation': 'Mark VII',
        'Year_Introduced': 1918,
        'Weight': 82.0,
        'Modded': 1,
        'Notes': '13.5"/50 Mark VII - Experimental high-velocity variant. Longer barrel L/50 vs L/45. Shell: 1,400 lbs. MV: 2,700 fps. Range: 32,000 yds @ 30°. Late-WWI experimental design. All-steel construction trial. Weight: 82 tons. Never entered service. Fictional - superseded by 15" development.'
    }
])

# 12" Guns (+6 variants) - Gun IDs 574-579
fictional_guns.extend([
    {
        'Gun_ID': 574,
        'Country': 'Britain',
        'Caliber': '12"',
        'Length': '/50',
        'Mark_Designation': 'Mark XIII',
        'Year_Introduced': 1912,
        'Weight': 62.0,
        'Modded': 1,
        'Notes': '12"/50 Mark XIII - Post-Dreadnought evolution. Consolidated best features of Marks XI/XI*/XII. Shell: 850 lbs. MV: 2,825 fps. Improved barrel life: 280 rounds (vs 200 for Mark XI). Proposed for 1912-1913 battleship designs. Weight: 62 tons. Fictional - 13.5" chosen instead.'
    },
    {
        'Gun_ID': 575,
        'Country': 'Britain',
        'Caliber': '12"',
        'Length': '/50',
        'Mark_Designation': 'Mark XIV',
        'Year_Introduced': 1916,
        'Weight': 63.0,
        'Modded': 1,
        'Notes': '12"/50 Mark XIV - WWI improved variant. Higher-velocity chamber design. Shell: 850 lbs. MV: 2,900 fps (75 fps improvement). Range: 28,500 yds @ 30°. Proposed for WWI emergency battleships. Wire-wound construction. Barrel life: 260 rounds. Fictional - 15" production prioritized.'
    },
    {
        'Gun_ID': 576,
        'Country': 'Britain',
        'Caliber': '12"',
        'Length': '/50',
        'Mark_Designation': 'Mark XV',
        'Year_Introduced': 1925,
        'Weight': 60.0,
        'Modded': 1,
        'Notes': '12"/50 Mark XV - Interwar modernization. Improved metallurgy, reduced weight. Shell: 850 lbs. MV: 2,825 fps. Weight: 60 tons (2 tons lighter). Proposed for pre-dreadnought modernization 1920s. All-steel construction trial. Fictional - ships scrapped instead.'
    },
    {
        'Gun_ID': 577,
        'Country': 'Britain',
        'Caliber': '12"',
        'Length': '/50',
        'Mark_Designation': 'Mark XVI',
        'Year_Introduced': 1938,
        'Weight': 61.5,
        'Modded': 1,
        'Notes': '12"/50 Mark XVI - Pre-WWII variant. Modernized design for light battleships/heavy cruisers. Shell: 850 lbs. MV: 2,850 fps. All-steel radial expansion construction. Proposed for large cruiser designs (1937-1938). Weight: 61.5 tons. Fictional - treaty limits prevented construction.'
    },
    {
        'Gun_ID': 578,
        'Country': 'Britain',
        'Caliber': '12"',
        'Length': '/45',
        'Mark_Designation': 'Mark XVII',
        'Year_Introduced': 1942,
        'Weight': 56.0,
        'Modded': 1,
        'Notes': '12"/45 Mark XVII - Wartime emergency variant. Shorter barrel for faster production. Shell: 850 lbs. MV: 2,700 fps. Range: 25,000 yds @ 30°. Proposed for emergency cruiser/monitor construction 1942. Weight: 56 tons. Simplified tooling. Fictional - not built.'
    },
    {
        'Gun_ID': 579,
        'Country': 'Britain',
        'Caliber': '12"',
        'Length': '/50',
        'Mark_Designation': 'Mark XVIII',
        'Year_Introduced': 1950,
        'Weight': 60.5,
        'Modded': 1,
        'Notes': '12"/50 Mark XVIII - Post-war variant. Improved barrel life through chromium plating. Shell: 850 lbs. MV: 2,825 fps. Barrel life: 350 rounds (improved). Proposed for cruiser designs 1950s. Weight: 60.5 tons. Fictional - missiles replaced large guns.'
    }
])

# 10" Guns (+4 variants) - NEW CALIBER - Gun IDs 580-583
fictional_guns.extend([
    {
        'Gun_ID': 580,
        'Country': 'Britain',
        'Caliber': '10"',
        'Length': '/40',
        'Mark_Designation': 'Mark I',
        'Year_Introduced': 1901,
        'Weight': 42.0,
        'Modded': 1,
        'Notes': '10"/40 Mark I - Pre-dreadnought era heavy cruiser gun. Wire-wound construction. Shell: 500 lbs. MV: 2,500 fps. Range: 18,000 yds @ 30°. Proposed for armored cruisers 1900-1905. Twin turrets. Weight: 42 tons. Fictional - 9.2" chosen instead for armored cruisers.'
    },
    {
        'Gun_ID': 581,
        'Country': 'Britain',
        'Caliber': '10"',
        'Length': '/45',
        'Mark_Designation': 'Mark II',
        'Year_Introduced': 1907,
        'Weight': 46.0,
        'Modded': 1,
        'Notes': '10"/45 Mark II - Dreadnought-era variant. Longer barrel for improved velocity. Shell: 500 lbs. MV: 2,650 fps. Range: 20,500 yds @ 30°. Proposed for battle cruiser secondary armament. Wire-wound construction. Weight: 46 tons. ROF: 2.5 rpm. Fictional - 9.2" continued in service.'
    },
    {
        'Gun_ID': 582,
        'Country': 'Britain',
        'Caliber': '10"',
        'Length': '/45',
        'Mark_Designation': 'Mark III',
        'Year_Introduced': 1916,
        'Weight': 47.0,
        'Modded': 1,
        'Notes': '10"/45 Mark III - WWI heavy cruiser variant. Higher-velocity chamber. Shell: 500 lbs. MV: 2,700 fps. Range: 22,000 yds @ 30°. Proposed for WWI cruiser construction. Wire-wound, improved barrel life: 240 rounds. Weight: 47 tons. Fictional - 9.2" remained standard.'
    },
    {
        'Gun_ID': 583,
        'Country': 'Britain',
        'Caliber': '10"',
        'Length': '/50',
        'Mark_Designation': 'Mark IV',
        'Year_Introduced': 1928,
        'Weight': 50.0,
        'Modded': 1,
        'Notes': '10"/50 Mark IV - Interwar modernization. Longer barrel L/50. Shell: 500 lbs. MV: 2,800 fps. Range: 24,500 yds @ 30°. Proposed for large cruiser designs 1920s. All-steel construction. Weight: 50 tons. ROF: 3 rpm. Fictional - 8" became treaty standard.'
    }
])

# Continue with remaining calibers...
print(f"Generated {len(fictional_guns)} fictional British guns so far...")
print("Continuing with remaining calibers...")

# I'll create the full script - this is getting long, so let me organize it better
