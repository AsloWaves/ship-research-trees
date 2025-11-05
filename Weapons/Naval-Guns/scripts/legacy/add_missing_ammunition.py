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

print("Adding Missing Ammunition...")
print("=" * 80)

# Update 28cm SK L/45 with muzzle velocity and add ammunition
print("\n[UPDATE] 28 cm/45 SK L/45 - Adding muzzle velocity and ammunition")

# The SK L/45 shared ammunition with SK L/50 (665.8 lbs APC)
# SK L/50 had 880 m/s (2,887 fps), SK L/45 slightly lower due to shorter barrel
# Estimate: 2,750 fps for SK L/45
muzzle_velocity = 2750

cursor.execute("""
    UPDATE guns
    SET muzzle_velocity = ?
    WHERE designation = '28 cm/45 (11") SK L/45'
""", (muzzle_velocity,))

print(f"  Updated muzzle velocity: {muzzle_velocity} fps")

# Get the gun_id
cursor.execute("SELECT gun_id FROM guns WHERE designation = ?", ('28 cm/45 (11") SK L/45',))
gun_id = cursor.fetchone()[0]

# Add ammunition (same projectiles as SK L/50, shared cartridge case)
ammunition = [
    {'type': 'APC L/3.2', 'weight_lbs': 665.8, 'explosive_lbs': 28.7, 'velocity_fps': 2750},
    {'type': 'HE', 'weight_lbs': 617, 'explosive_lbs': 67.3, 'velocity_fps': 2750}
]

for ammo in ammunition:
    ke_mj = calculate_ke_mj(ammo['weight_lbs'], ammo['velocity_fps'])

    cursor.execute("""
        INSERT INTO ammunition (gun_id, shell_type, weight_lbs, kinetic_megajoules,
                               explosive_lbs, country)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (gun_id, ammo['type'], ammo['weight_lbs'], ke_mj,
          ammo['explosive_lbs'], 'Germany'))

    print(f"  + {ammo['type']}: {ammo['weight_lbs']} lbs, {ke_mj} MJ")

conn.commit()

# Verify - check guns without ammunition
cursor.execute("""
    SELECT COUNT(*)
    FROM guns g
    WHERE NOT EXISTS (SELECT 1 FROM ammunition a WHERE a.gun_id = g.gun_id)
    AND designation NOT LIKE '%Rocket%'
    AND designation NOT LIKE '%Raketen%'
    AND designation NOT LIKE '%Miscellaneous%'
""")

remaining = cursor.fetchone()[0]

print(f"\n{'=' * 80}")
print(f"Update Complete!")
print(f"Remaining guns without ammo (excluding rockets/misc): {remaining}")

# Show total stats
cursor.execute("SELECT COUNT(*) FROM guns")
total_guns = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ammunition")
total_ammo = cursor.fetchone()[0]

cursor.execute("""
    SELECT COUNT(*)
    FROM guns g
    WHERE EXISTS (SELECT 1 FROM ammunition a WHERE a.gun_id = g.gun_id)
""")
guns_with_ammo = cursor.fetchone()[0]

print(f"\nFinal Database Statistics:")
print(f"  Total Guns: {total_guns}")
print(f"  Total Ammunition: {total_ammo}")
print(f"  Guns with Ammunition: {guns_with_ammo} ({guns_with_ammo/total_guns*100:.1f}%)")

conn.close()
