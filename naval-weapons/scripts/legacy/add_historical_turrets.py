import sqlite3

conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

# Comprehensive historical turret data for Big 4 nations
historical_turrets = [
    # ========== US NAVY BATTLESHIP TURRETS ==========
    {
        'designation': 'Mark 7 Triple Turret (16"/50)',
        'guns_per_turret': 3,
        'elevation_max': 45.0,
        'elevation_min': -5.0,
        'traverse_speed': 4.0,
        'weight_tons': 2500.0,
        'gun_designation': '16"/50 (40.6 cm) Mark 7',
        'ships': 'Iowa, New Jersey, Missouri, Wisconsin (Iowa class); Montana class (planned)'
    },
    {
        'designation': 'Mark 6 Triple Turret (16"/45)',
        'guns_per_turret': 3,
        'elevation_max': 45.0,
        'elevation_min': -5.0,
        'traverse_speed': 4.0,
        'weight_tons': 1426.0,
        'gun_designation': '16"/45 (40.6 cm) Mark 6',
        'ships': 'North Carolina, Washington (North Carolina class); South Dakota class'
    },
    {
        'designation': 'Mark 1/5 Twin Turret (16"/45)',
        'guns_per_turret': 2,
        'elevation_max': 30.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 800.0,
        'gun_designation': '16"/45 (40.6 cm) Mark 1',
        'ships': 'Colorado, Maryland, West Virginia (Colorado class)'
    },
    {
        'designation': '14"/50 Triple Turret',
        'guns_per_turret': 3,
        'elevation_max': 30.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 600.0,
        'gun_designation': '14"/50 (35.6 cm) Mark 7, Mark 11 and Mark B',
        'ships': 'New Mexico, Tennessee classes'
    },
    {
        'designation': '14"/45 Triple Turret',
        'guns_per_turret': 3,
        'elevation_max': 30.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 550.0,
        'gun_designation': '14"/45 (35.6 cm) Marks 1, 2, 3 and 5',
        'ships': 'Pennsylvania, Nevada, New York classes'
    },
    {
        'designation': '12"/50 Twin Turret',
        'guns_per_turret': 2,
        'elevation_max': 20.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 400.0,
        'gun_designation': '12"/50 (30.5 cm) Mark 7',
        'ships': 'Wyoming class'
    },

    # US Heavy Cruiser Turrets
    {
        'designation': '8"/55 Triple Turret Mark 12',
        'guns_per_turret': 3,
        'elevation_max': 41.0,
        'elevation_min': -5.0,
        'traverse_speed': 5.0,
        'weight_tons': 170.0,
        'gun_designation': '8"/55 (20.3 cm) Marks 12 and 15',
        'ships': 'Baltimore, Wichita, Tuscaloosa classes'
    },
    {
        'designation': '8"/55 Triple Turret Mark 16',
        'guns_per_turret': 3,
        'elevation_max': 41.0,
        'elevation_min': -5.0,
        'traverse_speed': 10.0,
        'weight_tons': 156.5,
        'gun_designation': '8"/55 (20.3 cm) RF Mark 16',
        'ships': 'Des Moines class (auto-loading)'
    },

    # US Destroyer/Light Cruiser Turrets
    {
        'designation': '5"/38 Twin DP Turret',
        'guns_per_turret': 2,
        'elevation_max': 85.0,
        'elevation_min': -15.0,
        'traverse_speed': 25.0,
        'weight_tons': 34.6,
        'gun_designation': '5"/38 (12.7 cm) Mark 12',
        'ships': 'Fletcher, Gearing classes; cruisers (dual-purpose)'
    },

    # ========== ROYAL NAVY TURRETS ==========
    {
        'designation': 'Mark III Quadruple Turret (14")',
        'guns_per_turret': 4,
        'elevation_max': 40.0,
        'elevation_min': -3.0,
        'traverse_speed': 2.0,
        'weight_tons': 1582.0,
        'gun_designation': '14-inch (35.6 cm) Mark VII',
        'ships': 'King George V class (A, X, Y turrets)'
    },
    {
        'designation': 'Mark III Twin Turret (14")',
        'guns_per_turret': 2,
        'elevation_max': 40.0,
        'elevation_min': -3.0,
        'traverse_speed': 2.0,
        'weight_tons': 915.0,
        'gun_designation': '14-inch (35.6 cm) Mark VII',
        'ships': 'King George V class (B turret only)'
    },
    {
        'designation': 'Mark I Triple Turret (16")',
        'guns_per_turret': 3,
        'elevation_max': 40.0,
        'elevation_min': -3.0,
        'traverse_speed': 2.0,
        'weight_tons': 1500.0,
        'gun_designation': '16"/45 (40.6 cm) Mark I',
        'ships': 'Nelson, Rodney'
    },
    {
        'designation': 'Mark I Twin Turret (15")',
        'guns_per_turret': 2,
        'elevation_max': 20.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 750.0,
        'gun_designation': '15-inch (38.1 cm) Mark I',
        'ships': 'Queen Elizabeth, Royal Sovereign, Vanguard classes'
    },

    # British Heavy Cruiser Turrets
    {
        'designation': 'Mark VIII Twin Turret (8")',
        'guns_per_turret': 2,
        'elevation_max': 70.0,
        'elevation_min': -5.0,
        'traverse_speed': 6.0,
        'weight_tons': 190.0,
        'gun_designation': '8"/50 (20.3 cm) Mark VIII',
        'ships': 'Kent, London, Norfolk, York classes'
    },

    # British Light Cruiser Turrets
    {
        'designation': 'QF 5.25" Twin DP Turret',
        'guns_per_turret': 2,
        'elevation_max': 70.0,
        'elevation_min': -5.0,
        'traverse_speed': 10.0,
        'weight_tons': 81.0,
        'gun_designation': '5.25"/50 (133 mm) QF Mark I',
        'ships': 'King George V class (secondary); Dido class cruisers'
    },

    # ========== KRIEGSMARINE TURRETS ==========
    {
        'designation': 'Drh LC/34 Twin Turret (38cm)',
        'guns_per_turret': 2,
        'elevation_max': 30.0,
        'elevation_min': -5.5,
        'traverse_speed': 5.4,
        'weight_tons': 1050.0,
        'gun_designation': '38 cm/47 (15") SK C/34',
        'ships': 'Bismarck, Tirpitz'
    },
    {
        'designation': 'Drh LC/28 Triple Turret (28cm)',
        'guns_per_turret': 3,
        'elevation_max': 40.0,
        'elevation_min': -8.0,
        'traverse_speed': 5.4,
        'weight_tons': 1050.0,
        'gun_designation': '28 cm/45 (11") SK L/45',
        'ships': 'Scharnhorst, Gneisenau'
    },
    {
        'designation': 'Drh L C/1913 Twin Turret (38cm)',
        'guns_per_turret': 2,
        'elevation_max': 16.0,
        'elevation_min': -5.0,
        'traverse_speed': 4.0,
        'weight_tons': 800.0,
        'gun_designation': '38 cm/45 (15") SK L/45',
        'ships': 'Bayern, Baden'
    },
    {
        'designation': 'Drh L C/1909 Twin Turret (30.5cm)',
        'guns_per_turret': 2,
        'elevation_max': 13.5,
        'elevation_min': -5.0,
        'traverse_speed': 4.0,
        'weight_tons': 650.0,
        'gun_designation': '30.5 cm/50 (12") SK L/50',
        'ships': 'Kaiser, Konig classes'
    },

    # German Heavy Cruiser Turrets
    {
        'designation': 'Drh LC/34 Twin Turret (20.3cm)',
        'guns_per_turret': 2,
        'elevation_max': 37.0,
        'elevation_min': -10.0,
        'traverse_speed': 8.0,
        'weight_tons': 265.0,
        'gun_designation': '20.3 cm/60 (8") SK C/34',
        'ships': 'Admiral Hipper, Blucher, Prinz Eugen'
    },

    # ========== IMPERIAL JAPANESE NAVY TURRETS ==========
    {
        'designation': 'Type 94 Triple Turret (46cm)',
        'guns_per_turret': 3,
        'elevation_max': 45.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 2750.0,
        'gun_designation': '46 cm/45 (18.1") Type 94',
        'ships': 'Yamato, Musashi'
    },
    {
        'designation': 'Type 88 Twin Turret (41cm)',
        'guns_per_turret': 2,
        'elevation_max': 43.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 1050.0,
        'gun_designation': '41 cm/45 (16.1") Type 88/Type 3',
        'ships': 'Nagato, Mutsu'
    },
    {
        'designation': 'Vickers Twin Turret (14")',
        'guns_per_turret': 2,
        'elevation_max': 33.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 650.0,
        'gun_designation': '14"/45 (35.6 cm) Vickers Mark "A"',
        'ships': 'Kongo, Hiei, Haruna, Kirishima; Fuso, Yamashiro; Ise'
    },

    # Japanese Heavy Cruiser Turrets
    {
        'designation': '3rd Year Type Twin Turret (20cm)',
        'guns_per_turret': 2,
        'elevation_max': 70.0,
        'elevation_min': -5.0,
        'traverse_speed': 6.0,
        'weight_tons': 154.0,
        'gun_designation': '20 cm/50 3rd Year Type',
        'ships': 'Myoko, Takao, Mogami classes (before refit)'
    },

    # Japanese Destroyer/Light Cruiser Turrets
    {
        'designation': 'Type 89 Twin DP Turret (12.7cm)',
        'guns_per_turret': 2,
        'elevation_max': 90.0,
        'elevation_min': -8.0,
        'traverse_speed': 16.0,
        'weight_tons': 33.5,
        'gun_designation': '12.7 cm/40 (5") Type 89',
        'ships': 'Various destroyers and secondary batteries'
    },

    # ========== CONCEPT/EXPERIMENTAL TURRETS ==========
    {
        'designation': 'Mark A Test Turret (18"/47)',
        'guns_per_turret': 2,
        'elevation_max': 40.0,
        'elevation_min': -3.0,
        'traverse_speed': 2.0,
        'weight_tons': 3000.0,
        'gun_designation': '18"/47 (45.7 cm) Mark A (Test Gun)',
        'ships': 'Test gun only, never deployed'
    },
    {
        'designation': 'H-44 Twin Turret (50.8cm)',
        'guns_per_turret': 2,
        'elevation_max': 30.0,
        'elevation_min': -5.5,
        'traverse_speed': 4.0,
        'weight_tons': 3500.0,
        'gun_designation': '50.8 cm/XX (20") H-44 Class',
        'ships': 'H-44 class (never built)'
    },
    {
        'designation': 'A-150 Triple Turret (51cm)',
        'guns_per_turret': 3,
        'elevation_max': 45.0,
        'elevation_min': -5.0,
        'traverse_speed': 2.0,
        'weight_tons': 3200.0,
        'gun_designation': '51 cm/45 (20.1") Type A-150',
        'ships': 'A-150 Super Yamato (never built)'
    },
]

added_turrets = 0
added_linkages = 0
skipped_turrets = 0

print("Adding Historical Turrets to Database...")
print("=" * 80)

for turret_data in historical_turrets:
    # Check if turret already exists
    cursor.execute("SELECT turret_id FROM turrets WHERE designation = ?",
                   (turret_data['designation'],))
    if cursor.fetchone():
        print(f"[SKIP] Turret already exists: {turret_data['designation']}")
        skipped_turrets += 1
        continue

    # Find the gun_id for this turret
    cursor.execute("SELECT gun_id FROM guns WHERE designation = ?",
                   (turret_data['gun_designation'],))
    gun_result = cursor.fetchone()

    if not gun_result:
        print(f"[ERROR] Gun not found for turret: {turret_data['designation']}")
        print(f"        Looking for gun: {turret_data['gun_designation']}")
        continue

    gun_id = gun_result[0]

    # Insert turret
    cursor.execute("""
        INSERT INTO turrets (designation, guns_per_turret, elevation_max, elevation_min,
                            traverse_speed, weight_tons)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (turret_data['designation'], turret_data['guns_per_turret'],
          turret_data['elevation_max'], turret_data['elevation_min'],
          turret_data['traverse_speed'], turret_data['weight_tons']))

    turret_id = cursor.lastrowid
    added_turrets += 1

    # Link turret to gun
    cursor.execute("""
        INSERT INTO turret_guns (turret_id, gun_id, quantity)
        VALUES (?, ?, ?)
    """, (turret_id, gun_id, turret_data['guns_per_turret']))

    added_linkages += 1

    # Show progress
    print(f"[ADD] Turret {turret_id}: {turret_data['designation']}")
    print(f"      {turret_data['guns_per_turret']} x {turret_data['gun_designation'][:50]}")
    print(f"      {turret_data['weight_tons']:.0f} tons | Elev: {turret_data['elevation_min']}° to {turret_data['elevation_max']}° | Traverse: {turret_data['traverse_speed']}°/s")
    print(f"      Ships: {turret_data['ships'][:60]}")
    print()

conn.commit()

# Summary statistics
print("=" * 80)
print(f"Turret Addition Complete!")
print(f"Added: {added_turrets} turrets")
print(f"Skipped: {skipped_turrets} (already exist)")
print(f"Linkages: {added_linkages} turret-gun relationships")

# Show totals
cursor.execute("SELECT COUNT(*) FROM turrets")
total_turrets = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM turret_guns")
total_linkages = cursor.fetchone()[0]

print(f"\nFinal Database Statistics:")
print(f"  Total Turrets: {total_turrets}")
print(f"  Total Turret-Gun Linkages: {total_linkages}")

# Show turrets by country
print(f"\nTurrets by Gun Country:")
cursor.execute("""
    SELECT g.country, COUNT(DISTINCT t.turret_id) as turret_count
    FROM turrets t
    JOIN turret_guns tg ON t.turret_id = tg.turret_id
    JOIN guns g ON tg.gun_id = g.gun_id
    WHERE g.country IN ('USA', 'Britain', 'Germany', 'Japan')
    GROUP BY g.country
    ORDER BY turret_count DESC
""")

for country, count in cursor.fetchall():
    print(f"  {country}: {count} turrets")

# Verify ammunition linkage through guns
print(f"\n" + "=" * 80)
print("Verifying Turret -> Gun -> Ammunition Linkage")
print("=" * 80)

cursor.execute("""
    SELECT t.designation, t.guns_per_turret, g.designation as gun_name,
           COUNT(DISTINCT a.ammo_id) as ammo_types
    FROM turrets t
    JOIN turret_guns tg ON t.turret_id = tg.turret_id
    JOIN guns g ON tg.gun_id = g.gun_id
    LEFT JOIN ammunition a ON g.gun_id = a.gun_id
    GROUP BY t.turret_id
    HAVING ammo_types > 0
    ORDER BY t.turret_id
    LIMIT 10
""")

print("\nSample Turret-Gun-Ammunition Linkages:")
for turret, guns_per, gun_name, ammo_count in cursor.fetchall():
    print(f"  {turret[:45]:<45} | {guns_per} guns | {ammo_count} ammo types")

conn.close()
print(f"\n" + "=" * 80)
print("Historical Turret Database Complete!")
