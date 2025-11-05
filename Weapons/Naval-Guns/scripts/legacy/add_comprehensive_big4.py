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

# Comprehensive Big 4 guns including concept, never-built, pre-dreadnought, and light AA
comprehensive_guns = [
    # ========== CONCEPT/NEVER-BUILT GUNS ==========
    {
        'designation': '18"/47 (45.7 cm) Mark A (Test Gun)',
        'caliber_inches': 18.0,
        'barrel_length': 47,
        'country': 'USA',
        'ships': 'Test gun (never deployed)',
        'muzzle_velocity': 2400,
        'year_introduced': 1920,
        'note': 'Concept/Test'
    },
    {
        'designation': '50.8 cm/XX (20") H-44 Class',
        'caliber_inches': 20.0,
        'barrel_length': 50,
        'country': 'Germany',
        'ships': 'H-44 class (never built)',
        'year_introduced': 1941,
        'note': 'Concept/Never Built'
    },
    {
        'designation': '51 cm/45 (20.1") Type A-150',
        'caliber_inches': 20.1,
        'barrel_length': 45,
        'country': 'Japan',
        'ships': 'A-150 Super Yamato (never built)',
        'year_introduced': 1941,
        'note': 'Concept/Never Built'
    },

    # ========== PRE-DREADNOUGHT GUNS ==========
    {
        'designation': '24 cm/40 (9.4") SK L/40',
        'caliber_inches': 9.4,
        'barrel_length': 40,
        'country': 'Germany',
        'ships': 'Kaiser Friedrich III, Wittelsbach, Fürst Bismarck',
        'year_introduced': 1894,
        'note': 'Pre-Dreadnought'
    },
    {
        'designation': '28 cm/40 (11") SK L/40',
        'caliber_inches': 11.0,
        'barrel_length': 40,
        'country': 'Germany',
        'ships': 'Braunschweig, Deutschland class',
        'year_introduced': 1904,
        'note': 'Pre-Dreadnought'
    },

    # ========== LIGHT AA GUNS ==========
    {
        'designation': '40 mm/60 Bofors L/60 Mark 1',
        'caliber_inches': 1.575,
        'barrel_length': 56.25,
        'country': 'USA',
        'ships': 'All US warships WWII',
        'muzzle_velocity': 2890,
        'rate_of_fire': 120.0,
        'year_introduced': 1941,
        'note': 'Light AA'
    },
    {
        'designation': '40 mm/60 Bofors L/60 Mark VII',
        'caliber_inches': 1.575,
        'barrel_length': 56.25,
        'country': 'Britain',
        'ships': 'All British warships WWII',
        'muzzle_velocity': 2789,
        'rate_of_fire': 120.0,
        'year_introduced': 1941,
        'note': 'Light AA'
    },
    {
        'designation': '40 mm/60 (4 cm) FlaK 28',
        'caliber_inches': 1.575,
        'barrel_length': 56.25,
        'country': 'Germany',
        'ships': 'Kriegsmarine vessels (captured)',
        'muzzle_velocity': 2822,
        'rate_of_fire': 120.0,
        'year_introduced': 1942,
        'note': 'Light AA/Captured'
    },
    {
        'designation': '20 mm/70 Oerlikon Mark 4',
        'caliber_inches': 0.787,
        'barrel_length': 70,
        'country': 'USA',
        'ships': 'All US warships WWII',
        'muzzle_velocity': 2720,
        'rate_of_fire': 320.0,
        'year_introduced': 1941,
        'note': 'Light AA'
    },
    {
        'designation': '20 mm/70 Oerlikon Mark 5',
        'caliber_inches': 0.787,
        'barrel_length': 70,
        'country': 'Britain',
        'ships': 'All British warships WWII',
        'muzzle_velocity': 2720,
        'rate_of_fire': 320.0,
        'year_introduced': 1941,
        'note': 'Light AA'
    },
    {
        'designation': '20 mm/65 Type 99 Mark 2',
        'caliber_inches': 0.787,
        'barrel_length': 65,
        'country': 'Japan',
        'ships': 'IJN warships WWII',
        'muzzle_velocity': 2625,
        'rate_of_fire': 490.0,
        'year_introduced': 1941,
        'note': 'Light AA'
    }
]

# Ammunition data for each gun
ammunition_data = {
    '18"/47 (45.7 cm) Mark A (Test Gun)': [
        {'type': 'Super Heavy AP', 'weight_lbs': 3850, 'explosive_lbs': 77.0, 'velocity_fps': 2400}
    ],
    '50.8 cm/XX (20") H-44 Class': [
        {'type': 'APC (Estimated)', 'weight_lbs': 4630, 'explosive_lbs': 154.0, 'velocity_fps': 2625}
    ],
    '51 cm/45 (20.1") Type A-150': [
        {'type': 'Type AP', 'weight_lbs': 4300, 'explosive_lbs': 89.0, 'velocity_fps': 2559},
        {'type': 'Type HE', 'weight_lbs': 4097, 'explosive_lbs': 189.0, 'velocity_fps': 2559}
    ],
    '24 cm/40 (9.4") SK L/40': [
        {'type': 'APC', 'weight_lbs': 492, 'explosive_lbs': 23.8, 'velocity_fps': 2133},
        {'type': 'HE', 'weight_lbs': 463, 'explosive_lbs': 54.0, 'velocity_fps': 2133}
    ],
    '28 cm/40 (11") SK L/40': [
        {'type': 'APC', 'weight_lbs': 661, 'explosive_lbs': 28.7, 'velocity_fps': 2822},
        {'type': 'HE', 'weight_lbs': 617, 'explosive_lbs': 67.3, 'velocity_fps': 2822}
    ],
    '40 mm/60 Bofors L/60 Mark 1': [
        {'type': 'HE-T M81', 'weight_lbs': 1.98, 'explosive_lbs': 0.15, 'velocity_fps': 2890},
        {'type': 'AP-T M81A1', 'weight_lbs': 1.98, 'explosive_lbs': 0.09, 'velocity_fps': 2890}
    ],
    '40 mm/60 Bofors L/60 Mark VII': [
        {'type': 'HE Mk II', 'weight_lbs': 1.98, 'explosive_lbs': 0.15, 'velocity_fps': 2789}
    ],
    '40 mm/60 (4 cm) FlaK 28': [
        {'type': 'HE', 'weight_lbs': 1.98, 'explosive_lbs': 0.15, 'velocity_fps': 2822}
    ],
    '20 mm/70 Oerlikon Mark 4': [
        {'type': 'HE-T', 'weight_lbs': 0.287, 'explosive_lbs': 0.04, 'velocity_fps': 2720}
    ],
    '20 mm/70 Oerlikon Mark 5': [
        {'type': 'HE-T', 'weight_lbs': 0.287, 'explosive_lbs': 0.04, 'velocity_fps': 2720}
    ],
    '20 mm/65 Type 99 Mark 2': [
        {'type': 'HE', 'weight_lbs': 0.287, 'explosive_lbs': 0.036, 'velocity_fps': 2625}
    ]
}

# Special ammunition for existing guns
special_ammunition = [
    {
        'gun_designation': '16"/50 (40.6 cm) Mark 7',
        'shell_type': 'W23 "Katie" Nuclear',
        'weight_lbs': 1700,
        'kinetic_mj': None,  # Nuclear yield, not kinetic
        'explosive_lbs': None,  # 15-20 kiloton nuclear yield
        'max_range_yards': 25000,
        'country': 'USA',
        'note': 'Nuclear shell, 15-20 KT yield, 1956-1962'
    }
]

added_guns = 0
added_ammo = 0
added_special = 0

print("Adding Comprehensive Big 4 Naval Guns...")
print("=" * 80)

for gun in comprehensive_guns:
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
    category = gun.get('note', 'Standard')
    print(f"[ADD] Gun {gun_id}: {gun['designation']} ({gun['country']}) [{category}]")

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

# Add special ammunition for existing guns
print(f"\n{'=' * 80}")
print("Adding Special/Experimental Ammunition...")
print("=" * 80)

for spec_ammo in special_ammunition:
    # Find the gun
    cursor.execute("SELECT gun_id, max_range_yards FROM guns WHERE designation = ?",
                   (spec_ammo['gun_designation'],))
    result = cursor.fetchone()

    if not result:
        print(f"[SKIP] Gun not found: {spec_ammo['gun_designation']}")
        continue

    gun_id, gun_range = result

    # Check if this special ammo already exists
    cursor.execute("""
        SELECT ammo_id FROM ammunition
        WHERE gun_id = ? AND shell_type = ?
    """, (gun_id, spec_ammo['shell_type']))

    if cursor.fetchone():
        print(f"[SKIP] Ammo already exists: {spec_ammo['shell_type']}")
        continue

    cursor.execute("""
        INSERT INTO ammunition (gun_id, shell_type, weight_lbs, kinetic_megajoules,
                               explosive_lbs, max_range_yards, country)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (gun_id, spec_ammo['shell_type'], spec_ammo['weight_lbs'],
          spec_ammo['kinetic_mj'], spec_ammo['explosive_lbs'],
          spec_ammo.get('max_range_yards', gun_range), spec_ammo['country']))

    added_special += 1
    print(f"[ADD] Special: {spec_ammo['shell_type']} for {spec_ammo['gun_designation']}")
    if spec_ammo.get('note'):
        print(f"      Note: {spec_ammo['note']}")

conn.commit()

# Show summary statistics
print(f"\n{'=' * 80}")
print(f"Added {added_guns} guns, {added_ammo} standard ammunition types, {added_special} special ammunition")
print(f"\nFinal Database Totals:")

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
print(f"\nBig 4 Final Breakdown:")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]} guns")

# Show gun categories
print(f"\nGun Categories Added:")
cursor.execute("""
    SELECT designation, country, year_introduced
    FROM guns
    WHERE gun_id > (SELECT MAX(gun_id) - ? FROM guns)
    ORDER BY year_introduced
""", (added_guns,))

categories = {'Concept/Never Built': 0, 'Pre-Dreadnought': 0, 'Light AA': 0}
for designation, country, year in cursor.fetchall():
    if 'never built' in designation.lower() or 'test gun' in designation.lower() or 'h-44' in designation.lower() or 'a-150' in designation.lower():
        categories['Concept/Never Built'] += 1
    elif year < 1906:
        categories['Pre-Dreadnought'] += 1
    elif 'bofors' in designation.lower() or 'oerlikon' in designation.lower() or 'flak' in designation.lower():
        categories['Light AA'] += 1

for category, count in categories.items():
    if count > 0:
        print(f"  {category}: {count} guns")

conn.close()
