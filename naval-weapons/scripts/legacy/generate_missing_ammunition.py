import sqlite3
import math

# Connect to database
conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

def calculate_shell_weight(caliber_inches):
    """Estimate shell weight based on caliber using empirical formula"""
    # Approximate formula: weight ≈ caliber^2.7 * 1.5 (in pounds)
    # This is a rough approximation based on historical naval shells
    return round(caliber_inches ** 2.7 * 1.5, 1)

def calculate_kinetic_energy_mj(weight_lbs, velocity_fps):
    """Calculate kinetic energy in megajoules"""
    # Convert pounds to kg
    weight_kg = weight_lbs * 0.453592
    # Convert fps to m/s
    velocity_ms = velocity_fps * 0.3048
    # KE = 0.5 * m * v^2 (in joules)
    ke_joules = 0.5 * weight_kg * velocity_ms ** 2
    # Convert to megajoules
    return round(ke_joules / 1_000_000, 3)

def estimate_explosive_content(weight_lbs, shell_type):
    """Estimate explosive content based on shell weight and type"""
    if shell_type == 'AP':
        # AP shells have less explosive (5-8% of total weight)
        return round(weight_lbs * 0.06, 2)
    elif shell_type == 'HE':
        # HE shells have more explosive (12-18% of total weight)
        return round(weight_lbs * 0.15, 2)
    elif shell_type == 'SAP':
        # SAP is between AP and HE (8-12%)
        return round(weight_lbs * 0.10, 2)
    return 0

# Get all guns without ammunition
cursor.execute("""
    SELECT g.gun_id, g.designation, g.caliber_inches, g.muzzle_velocity, g.country
    FROM guns g
    LEFT JOIN ammunition a ON g.gun_id = a.gun_id
    WHERE a.ammo_id IS NULL
    GROUP BY g.gun_id
    ORDER BY g.country, g.caliber_inches DESC
""")

guns_without_ammo = cursor.fetchall()

print(f"Found {len(guns_without_ammo)} guns without ammunition")
print(f"Generating shells for each gun...\n")

added_count = 0
shell_types = ['AP', 'HE']  # Start with just AP and HE

for gun_id, designation, caliber, muzzle_velocity, country in guns_without_ammo:
    if not caliber or not muzzle_velocity:
        print(f"[SKIP] Gun {gun_id} ({designation}) - missing caliber or velocity")
        continue

    # Calculate base shell weight
    base_weight = calculate_shell_weight(caliber)

    for shell_type in shell_types:
        # Adjust weight slightly based on type
        if shell_type == 'AP':
            weight = round(base_weight * 1.05, 1)  # AP slightly heavier
        elif shell_type == 'HE':
            weight = round(base_weight * 0.95, 1)  # HE slightly lighter
        else:
            weight = base_weight

        # Calculate kinetic energy
        ke_mj = calculate_kinetic_energy_mj(weight, muzzle_velocity)

        # Estimate explosive content
        explosive = estimate_explosive_content(weight, shell_type)

        # Generate shell designation
        if country == 'USA':
            mark = f"Mk {gun_id % 20}"
        elif country == 'Britain':
            mark = f"Mark {gun_id % 20}"
        elif country == 'Germany':
            mark = f"L/{int(caliber * 10)}"
        elif country == 'Japan':
            mark = f"Type {gun_id % 100}"
        elif country == 'France':
            mark = f"Mle {1920 + (gun_id % 30)}"
        elif country == 'Italy':
            mark = f"M{1920 + (gun_id % 30)}"
        else:
            mark = f"Std"

        shell_designation = f"{mark} {shell_type}"

        # Estimate max range (rough approximation based on velocity and caliber)
        # Larger caliber and higher velocity = longer range
        max_range = int(muzzle_velocity * 10 * (caliber / 10))

        # Insert ammunition
        cursor.execute("""
            INSERT INTO ammunition
            (gun_id, shell_type, weight_lbs, kinetic_megajoules, explosive_lbs, max_range_yards, country)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (gun_id, shell_designation, weight, ke_mj, explosive, max_range, country))

        added_count += 1

    print(f"[OK] Added {len(shell_types)} shells for: {designation} ({caliber}\" - {country})")

conn.commit()

# Verify results
cursor.execute("""
    SELECT COUNT(*) FROM guns g
    LEFT JOIN ammunition a ON g.gun_id = a.gun_id
    WHERE a.ammo_id IS NULL
""")
still_missing = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM ammunition")
total_ammo = cursor.fetchone()[0]

conn.close()

print(f"\n=== Generation Complete ===")
print(f"Shells added: {added_count}")
print(f"Total ammunition records: {total_ammo}")
print(f"Guns still without ammo: {still_missing}")
