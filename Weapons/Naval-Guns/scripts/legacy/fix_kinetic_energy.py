import sqlite3

conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

def calculate_ke_mj(weight_lbs, velocity_fps):
    """Calculate kinetic energy in megajoules using correct physics"""
    if not weight_lbs or not velocity_fps:
        return None

    # Convert to SI units
    weight_kg = weight_lbs * 0.453592
    velocity_ms = velocity_fps * 0.3048

    # KE = 0.5 * m * v^2 (in joules)
    ke_joules = 0.5 * weight_kg * velocity_ms ** 2

    # Convert to megajoules
    return round(ke_joules / 1_000_000, 3)

# Get all ammunition with weight and velocity data
cursor.execute("""
    SELECT a.ammo_id, a.weight_lbs, g.muzzle_velocity, a.kinetic_megajoules
    FROM ammunition a
    JOIN guns g ON a.gun_id = g.gun_id
    WHERE a.weight_lbs IS NOT NULL AND g.muzzle_velocity IS NOT NULL
""")

ammunition = cursor.fetchall()
updated_count = 0
error_count = 0

print(f"Recalculating kinetic energy for {len(ammunition)} ammunition records...")
print("=" * 80)

for ammo_id, weight_lbs, velocity_fps, old_ke in ammunition:
    new_ke = calculate_ke_mj(weight_lbs, velocity_fps)

    if new_ke is not None:
        cursor.execute("""
            UPDATE ammunition
            SET kinetic_megajoules = ?
            WHERE ammo_id = ?
        """, (new_ke, ammo_id))

        updated_count += 1

        if updated_count <= 10:  # Show first 10
            print(f"Ammo ID {ammo_id}: {old_ke:.2f} MJ -> {new_ke:.2f} MJ (change: {new_ke - old_ke:.2f} MJ)")
    else:
        error_count += 1

conn.commit()

# Verify results
cursor.execute("""
    SELECT
        COUNT(*) as total,
        MIN(kinetic_megajoules) as min_ke,
        ROUND(AVG(kinetic_megajoules), 2) as avg_ke,
        MAX(kinetic_megajoules) as max_ke
    FROM ammunition
    WHERE kinetic_megajoules IS NOT NULL
""")

stats = cursor.fetchone()

conn.close()

print(f"\n{'=' * 80}")
print(f"Update Complete!")
print(f"Updated: {updated_count}")
print(f"Errors: {error_count}")
print(f"\nNew Statistics:")
print(f"  Min KE: {stats[1]:.2f} MJ")
print(f"  Avg KE: {stats[2]:.2f} MJ")
print(f"  Max KE: {stats[3]:.2f} MJ")
