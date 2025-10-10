import sqlite3

conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

def calculate_ke_mj(weight_lbs, velocity_fps):
    """Calculate kinetic energy in megajoules"""
    if not weight_lbs or not velocity_fps:
        return None
    weight_kg = weight_lbs * 0.453592
    velocity_ms = velocity_fps * 0.3048
    ke_joules = 0.5 * weight_kg * velocity_ms ** 2
    return round(ke_joules / 1_000_000, 3)

# Big 4 missing guns
big4_guns = [
    # German Guns
    {
        'designation': '28 cm/45 (11") SK L/45',
        'caliber_inches': 11.0,
        'barrel_length': 45,
        'country': 'Germany',
        'ships': 'Nassau, Westfalen, Rheinland, Posen, Von der Tann',
        'year_introduced': 1907
    },
    {
        'designation': '30.5 cm/50 (12") SK L/50',
        'caliber_inches': 12.0,
        'barrel_length': 50,
        'country': 'Germany',
        'ships': 'Kaiser, König class battleships',
        'max_range_yards': 24000,
        'muzzle_velocity': 2805,
        'year_introduced': 1909
    },
    {
        'designation': '38 cm/45 (15") SK L/45',
        'caliber_inches': 14.96,
        'barrel_length': 45,
        'country': 'Germany',
        'ships': 'Bayern, Baden',
        'muzzle_velocity': 2920,
        'year_introduced': 1913
    },
    {
        'designation': '40.6 cm/52 (16") SK C/34',
        'caliber_inches': 16.0,
        'barrel_length': 52,
        'country': 'Germany',
        'ships': 'H-39 class (planned)',
        'max_range_yards': 39800,
        'muzzle_velocity': 2657,
        'year_introduced': 1940
    },
    {
        'designation': '20.3 cm/60 (8") SK C/34',
        'caliber_inches': 8.0,
        'barrel_length': 60,
        'country': 'Germany',
        'ships': 'Admiral Hipper, Blücher, Prinz Eugen',
        'muzzle_velocity': 3035,
        'year_introduced': 1935
    },

    # British Guns
    {
        'designation': '5.25"/50 (133 mm) QF Mark I',
        'caliber_inches': 5.25,
        'barrel_length': 50,
        'country': 'Britain',
        'ships': 'King George V class battleships',
        'max_range_yards': 24070,
        'rate_of_fire': 7.5,
        'year_introduced': 1940
    },
    {
        'designation': '4.5"/45 (113 mm) QF Mark I',
        'caliber_inches': 4.45,
        'barrel_length': 45,
        'country': 'Britain',
        'ships': 'Various destroyers and carriers',
        'year_introduced': 1936
    },

    # Japanese Guns
    {
        'designation': '20 cm/50 (8") 3rd Year Type',
        'caliber_inches': 7.87,
        'barrel_length': 50,
        'country': 'Japan',
        'ships': 'Myōkō, Takao class heavy cruisers',
        'year_introduced': 1924
    },
    {
        'designation': '12.7 cm/50 (5") 3rd Year Type',
        'caliber_inches': 5.0,
        'barrel_length': 50,
        'country': 'Japan',
        'ships': 'Fubuki class destroyers',
        'muzzle_velocity': 2994,
        'rate_of_fire': 7.5,
        'year_introduced': 1926
    },
    {
        'designation': '12.7 cm/40 (5") Type 89',
        'caliber_inches': 5.0,
        'barrel_length': 40,
        'country': 'Japan',
        'ships': 'Carriers, battleships, cruisers (AA)',
        'max_range_yards': 16200,
        'muzzle_velocity': 2362,
        'rate_of_fire': 14.0,
        'year_introduced': 1932
    },

    # US Guns
    {
        'designation': '5"/38 (127 mm) Mark 12',
        'caliber_inches': 5.0,
        'barrel_length': 38,
        'country': 'USA',
        'ships': 'Fletcher class destroyers, various cruisers',
        'max_range_yards': 18000,
        'muzzle_velocity': 2600,
        'year_introduced': 1934
    },
    {
        'designation': '3"/50 (76 mm) Mark 22',
        'caliber_inches': 3.0,
        'barrel_length': 50,
        'country': 'USA',
        'ships': 'Destroyers, destroyer escorts',
        'muzzle_velocity': 2700,
        'year_introduced': 1942
    }
]

# Ammunition data for each gun
ammunition_data = {
    '30.5 cm/50 (12") SK L/50': [
        {'type': 'APC', 'weight_lbs': 893, 'explosive_lbs': 34.2, 'velocity_fps': 2805},
        {'type': 'HE', 'weight_lbs': 820, 'explosive_lbs': 86.4, 'velocity_fps': 2805}
    ],
    '38 cm/45 (15") SK L/45': [
        {'type': 'APC', 'weight_lbs': 1653, 'explosive_lbs': 43.2, 'velocity_fps': 2920},
        {'type': 'HE', 'weight_lbs': 1543, 'explosive_lbs': 128.5, 'velocity_fps': 2920}
    ],
    '40.6 cm/52 (16") SK C/34': [
        {'type': 'APC', 'weight_lbs': 2270, 'explosive_lbs': 49.6, 'velocity_fps': 2657},
        {'type': 'HE', 'weight_lbs': 2116, 'explosive_lbs': 152.3, 'velocity_fps': 2657}
    ],
    '20.3 cm/60 (8") SK C/34': [
        {'type': 'APC', 'weight_lbs': 269, 'explosive_lbs': 18.5, 'velocity_fps': 3035},
        {'type': 'HE', 'weight_lbs': 243, 'explosive_lbs': 39.2, 'velocity_fps': 3035}
    ],
    '5.25"/50 (133 mm) QF Mark I': [
        {'type': 'HE', 'weight_lbs': 80, 'explosive_lbs': 14.2, 'velocity_fps': 2600},
        {'type': 'SAP', 'weight_lbs': 80, 'explosive_lbs': 8.5, 'velocity_fps': 2600}
    ],
    '4.5"/45 (113 mm) QF Mark I': [
        {'type': 'HE', 'weight_lbs': 55, 'explosive_lbs': 6.8, 'velocity_fps': 2350},
        {'type': 'SAP', 'weight_lbs': 55, 'explosive_lbs': 4.2, 'velocity_fps': 2350}
    ],
    '20 cm/50 (8") 3rd Year Type': [
        {'type': 'AP Mark I', 'weight_lbs': 242.5, 'explosive_lbs': 15.4, 'velocity_fps': 2854},
        {'type': 'AP Mark II', 'weight_lbs': 277.5, 'explosive_lbs': 18.2, 'velocity_fps': 2740},
        {'type': 'HE', 'weight_lbs': 235, 'explosive_lbs': 32.6, 'velocity_fps': 2854}
    ],
    '12.7 cm/50 (5") 3rd Year Type': [
        {'type': 'Type 0 HE', 'weight_lbs': 51, 'explosive_lbs': 7.7, 'velocity_fps': 2994},
        {'type': 'Illumination', 'weight_lbs': 51, 'explosive_lbs': 4.2, 'velocity_fps': 2994},
        {'type': 'ASW', 'weight_lbs': 51, 'explosive_lbs': 9.8, 'velocity_fps': 2994}
    ],
    '12.7 cm/40 (5") Type 89': [
        {'type': 'HE Mod. 3', 'weight_lbs': 51, 'explosive_lbs': 8.4, 'velocity_fps': 2362},
        {'type': 'HE-Incendiary', 'weight_lbs': 51, 'explosive_lbs': 7.9, 'velocity_fps': 2362}
    ],
    '5"/38 (127 mm) Mark 12': [
        {'type': 'Common', 'weight_lbs': 55, 'explosive_lbs': 3.2, 'velocity_fps': 2600},
        {'type': 'AA Common', 'weight_lbs': 54, 'explosive_lbs': 3.5, 'velocity_fps': 2600},
        {'type': 'HC', 'weight_lbs': 55, 'explosive_lbs': 7.8, 'velocity_fps': 2600},
        {'type': 'VT Frag', 'weight_lbs': 55, 'explosive_lbs': 6.4, 'velocity_fps': 2600}
    ],
    '3"/50 (76 mm) Mark 22': [
        {'type': 'AA Common', 'weight_lbs': 13, 'explosive_lbs': 0.9, 'velocity_fps': 2700},
        {'type': 'HC', 'weight_lbs': 13, 'explosive_lbs': 1.4, 'velocity_fps': 2700}
    ]
}

added_guns = 0
added_ammo = 0

print("Adding Big 4 naval guns to database...")
print("=" * 80)

for gun in big4_guns:
    # Check if gun already exists
    cursor.execute("SELECT gun_id FROM guns WHERE designation = ?", (gun['designation'],))
    if cursor.fetchone():
        print(f"[SKIP] Gun already exists: {gun['designation']}")
        continue

    # Insert gun
    cursor.execute("""
        INSERT INTO guns (designation, caliber_inches, barrel_length, country, ships,
                         max_range_yards, muzzle_velocity, rate_of_fire, year_introduced)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (gun['designation'], gun['caliber_inches'], gun['barrel_length'], gun['country'],
          gun['ships'], gun.get('max_range_yards'), gun.get('muzzle_velocity'),
          gun.get('rate_of_fire'), gun['year_introduced']))

    gun_id = cursor.lastrowid
    added_guns += 1
    print(f"[ADD] Gun {gun_id}: {gun['designation']} ({gun['country']})")

    # Add ammunition
    if gun['designation'] in ammunition_data:
        for ammo in ammunition_data[gun['designation']]:
            ke_mj = calculate_ke_mj(ammo['weight_lbs'], ammo['velocity_fps'])
            max_range = gun.get('max_range_yards')

            cursor.execute("""
                INSERT INTO ammunition (gun_id, shell_type, weight_lbs, kinetic_megajoules,
                                       explosive_lbs, max_range_yards, country)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (gun_id, ammo['type'], ammo['weight_lbs'], ke_mj,
                  ammo['explosive_lbs'], max_range, gun['country']))

            added_ammo += 1
            print(f"      + {ammo['type']}: {ammo['weight_lbs']} lbs, {ke_mj} MJ")

conn.commit()

# Show summary statistics
print(f"\n{'=' * 80}")
print(f"Added {added_guns} guns and {added_ammo} ammunition types")
print(f"\nDatabase totals:")

cursor.execute("SELECT COUNT(*) FROM guns")
total_guns = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ammunition")
total_ammo = cursor.fetchone()[0]

cursor.execute("""
    SELECT country, COUNT(*) as count
    FROM guns
    WHERE country IN ('USA', 'Japan', 'Britain', 'Germany')
    GROUP BY country
    ORDER BY count DESC
""")

print(f"  Total guns: {total_guns}")
print(f"  Total ammunition: {total_ammo}")
print(f"\nBig 4 breakdown:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} guns")

conn.close()
