import sqlite3

conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

# Major missing battleship guns
missing_guns = [
    {
        'designation': '46 cm/45 (18.1") Type 94',
        'caliber_inches': 18.1,
        'barrel_length': 45,
        'country': 'Japan',
        'ships': 'Yamato and Musashi',
        'max_range_yards': 45275,
        'muzzle_velocity': 2559,
        'rate_of_fire': 1.5,
        'year_introduced': 1941
    },
    {
        'designation': '41 cm/45 (16.1") Type 88/Type 3',
        'caliber_inches': 16.1,
        'barrel_length': 45,
        'country': 'Japan',
        'ships': 'Nagato and Mutsu',
        'max_range_yards': 42345,
        'muzzle_velocity': 2559,
        'rate_of_fire': 1.5,
        'year_introduced': 1920
    },
    {
        'designation': '38 cm/47 (15") SK C/34',
        'caliber_inches': 14.96,
        'barrel_length': 47,
        'country': 'Germany',
        'ships': 'Bismarck and Tirpitz',
        'max_range_yards': 39890,
        'muzzle_velocity': 2690,
        'rate_of_fire': 2.5,
        'year_introduced': 1940
    },
    {
        'designation': '40.6 cm/50 (16") B-37',
        'caliber_inches': 16.0,
        'barrel_length': 50,
        'country': 'Russia',
        'ships': 'Sovetsky Soyuz class (incomplete)',
        'max_range_yards': 49870,
        'muzzle_velocity': 2690,
        'rate_of_fire': 2.0,
        'year_introduced': 1940
    }
]

# Ammunition for each gun
ammunition_data = {
    '46 cm/45 (18.1") Type 94': [
        {'type': 'Type 91 AP', 'weight_lbs': 3219, 'explosive_lbs': 77.2, 'velocity_fps': 2559},
        {'type': 'Type 0 HE', 'weight_lbs': 2998, 'explosive_lbs': 143.3, 'velocity_fps': 2559}
    ],
    '41 cm/45 (16.1") Type 88/Type 3': [
        {'type': 'Type 91 AP', 'weight_lbs': 2249, 'explosive_lbs': 59.4, 'velocity_fps': 2559},
        {'type': 'Type 0 HE', 'weight_lbs': 2069, 'explosive_lbs': 110.2, 'velocity_fps': 2559}
    ],
    '38 cm/47 (15") SK C/34': [
        {'type': 'Psgr L/4.4 AP', 'weight_lbs': 1764, 'explosive_lbs': 40.0, 'velocity_fps': 2690},
        {'type': 'Spr.Gr. L/4.7 HE', 'weight_lbs': 1102, 'explosive_lbs': 154.3, 'velocity_fps': 2788}
    ],
    '40.6 cm/50 (16") B-37': [
        {'type': 'B-37 AP', 'weight_lbs': 2375, 'explosive_lbs': 55.1, 'velocity_fps': 2690},
        {'type': 'OF-45 HE', 'weight_lbs': 2205, 'explosive_lbs': 121.5, 'velocity_fps': 2690}
    ]
}

def calculate_ke_mj(weight_lbs, velocity_fps):
    """Calculate kinetic energy in megajoules"""
    weight_kg = weight_lbs * 0.453592
    velocity_ms = velocity_fps * 0.3048
    ke_joules = 0.5 * weight_kg * velocity_ms ** 2
    return round(ke_joules / 1_000_000, 3)

added_guns = 0
added_ammo = 0

for gun in missing_guns:
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
          gun['ships'], gun['max_range_yards'], gun['muzzle_velocity'],
          gun['rate_of_fire'], gun['year_introduced']))

    gun_id = cursor.lastrowid
    added_guns += 1
    print(f"[ADD] Gun {gun_id}: {gun['designation']} ({gun['country']})")

    # Add ammunition
    if gun['designation'] in ammunition_data:
        for ammo in ammunition_data[gun['designation']]:
            ke_mj = calculate_ke_mj(ammo['weight_lbs'], ammo['velocity_fps'])
            max_range = gun['max_range_yards']

            cursor.execute("""
                INSERT INTO ammunition (gun_id, shell_type, weight_lbs, kinetic_megajoules,
                                       explosive_lbs, max_range_yards, country)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (gun_id, ammo['type'], ammo['weight_lbs'], ke_mj,
                  ammo['explosive_lbs'], max_range, gun['country']))

            added_ammo += 1
            print(f"      + {ammo['type']}: {ammo['weight_lbs']} lbs, {ke_mj} MJ")

conn.commit()
conn.close()

print(f"\n{'=' * 80}")
print(f"Added {added_guns} guns and {added_ammo} ammunition types")
