import sqlite3
import random

conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

def calculate_ke_mj(weight_lbs, velocity_fps):
    """Calculate kinetic energy in megajoules"""
    weight_kg = weight_lbs * 0.453592
    velocity_ms = velocity_fps * 0.3048
    ke_joules = 0.5 * weight_kg * velocity_ms ** 2
    return round(ke_joules / 1_000_000, 3)

# Get recently added Big 4 guns
cursor.execute("""
    SELECT g.gun_id, g.designation, g.country, g.muzzle_velocity,
           a.ammo_id, a.shell_type, a.weight_lbs, a.kinetic_megajoules
    FROM guns g
    JOIN ammunition a ON g.gun_id = a.gun_id
    WHERE g.country IN ('USA', 'Japan', 'Britain', 'Germany')
    AND g.gun_id >= 386
    ORDER BY g.gun_id, a.ammo_id
""")

results = cursor.fetchall()

print("Verifying Big 4 naval gun additions...")
print("=" * 80)

errors = 0
verified = 0

for gun_id, designation, country, muzzle_vel, ammo_id, shell_type, weight, db_ke in results:
    if weight and muzzle_vel:
        calc_ke = calculate_ke_mj(weight, muzzle_vel)
        diff = abs(calc_ke - db_ke)

        status = "[OK]" if diff < 0.01 else "[ERROR]"

        if diff < 0.01:
            verified += 1
        else:
            errors += 1
            print(f"{status} Ammo {ammo_id}: {designation} - {shell_type}")
            print(f"  Weight: {weight} lbs, Velocity: {muzzle_vel} fps")
            print(f"  DB: {db_ke} MJ, Calculated: {calc_ke} MJ, Diff: {diff} MJ")

        if verified <= 10:  # Show first 10 successful verifications
            if diff < 0.01:
                print(f"{status} {designation} - {shell_type}: {db_ke} MJ (verified)")

# Show summary statistics for Big 4
cursor.execute("""
    SELECT
        g.country,
        COUNT(DISTINCT g.gun_id) as guns,
        COUNT(a.ammo_id) as ammo,
        ROUND(AVG(a.kinetic_megajoules), 2) as avg_ke,
        MAX(a.kinetic_megajoules) as max_ke
    FROM guns g
    JOIN ammunition a ON g.gun_id = a.gun_id
    WHERE g.country IN ('USA', 'Japan', 'Britain', 'Germany')
    GROUP BY g.country
    ORDER BY avg_ke DESC
""")

stats = cursor.fetchall()

print(f"\n{'=' * 80}")
print(f"Verification Complete!")
print(f"Verified: {verified}")
print(f"Errors: {errors}")
print(f"Error Rate: {(errors/(verified+errors)*100):.1f}%")

print(f"\nBig 4 Statistics:")
print(f"{'Country':<12} {'Guns':<8} {'Ammo':<8} {'Avg KE (MJ)':<15} {'Max KE (MJ)':<15}")
print("-" * 60)
for country, guns, ammo, avg_ke, max_ke in stats:
    print(f"{country:<12} {guns:<8} {ammo:<8} {avg_ke:<15} {max_ke:<15}")

# Show top 5 most powerful Big 4 guns
cursor.execute("""
    SELECT
        g.designation,
        g.country,
        a.shell_type,
        a.weight_lbs,
        g.muzzle_velocity,
        a.kinetic_megajoules
    FROM guns g
    JOIN ammunition a ON g.gun_id = a.gun_id
    WHERE g.country IN ('USA', 'Japan', 'Britain', 'Germany')
    ORDER BY a.kinetic_megajoules DESC
    LIMIT 5
""")

print(f"\nTop 5 Most Powerful Big 4 Guns:")
print(f"{'Gun':<40} {'Country':<10} {'Shell':<20} {'KE (MJ)':<10}")
print("-" * 80)
for designation, country, shell_type, weight, velocity, ke in cursor.fetchall():
    print(f"{designation:<40} {country:<10} {shell_type:<20} {ke:<10}")

conn.close()
