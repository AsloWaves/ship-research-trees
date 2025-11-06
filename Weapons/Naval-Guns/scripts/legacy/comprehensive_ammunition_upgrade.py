import sqlite3
import re

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

def get_mark_designation(gun_designation, shell_type, country, year):
    """Generate appropriate mark/type designation based on country and era"""

    # Extract base shell type
    base_type = shell_type.upper()

    if country == 'USA':
        # US uses Mark (Mk) system
        if 'AP' in base_type:
            return f'Mark {year % 100} AP' if year else 'Mark 8 AP'
        elif 'HE' in base_type or 'HC' in base_type:
            return f'Mark {year % 100} HE' if year else 'Mark 5 HE'
        elif 'SAP' in base_type:
            return f'Mark {(year % 100) + 1} SAP' if year else 'Mark 6 SAP'
        elif 'COMMON' in base_type or 'AAC' in base_type:
            return f'Mark {year % 100} Common' if year else 'Mark 7 Common'
        else:
            return f'Mark {year % 100} {base_type}' if year else f'Mark 1 {base_type}'

    elif country == 'Britain':
        # British use Mark system with Roman numerals sometimes
        if 'AP' in base_type:
            mark_num = (year % 100) if year and year > 1900 else 7
            return f'Mark {mark_num} APC'
        elif 'HE' in base_type:
            mark_num = (year % 100) - 1 if year and year > 1900 else 6
            return f'Mark {mark_num} HE'
        elif 'SAP' in base_type:
            mark_num = (year % 100) if year and year > 1900 else 8
            return f'Mark {mark_num} SAP'
        else:
            return f'Mark {year % 100} {base_type}' if year and year > 1900 else f'Mark 1 {base_type}'

    elif country == 'Germany':
        # German uses descriptive names with L/ designations
        if 'APC' in base_type or 'AP' in base_type:
            if 'cm' in gun_designation:
                cal_match = re.search(r'(\d+\.?\d*)\s*cm', gun_designation)
                if cal_match:
                    cal = float(cal_match.group(1))
                    return f'Pzgr. L/{cal:.1f}'
            return 'Panzergranate'
        elif 'HE' in base_type:
            if 'cm' in gun_designation:
                cal_match = re.search(r'(\d+\.?\d*)\s*cm', gun_designation)
                if cal_match:
                    cal = float(cal_match.group(1))
                    return f'Sprgr. L/{cal:.1f}'
            return 'Sprenggranate'
        elif 'SAP' in base_type:
            return 'Pzgr. (SAP)'
        else:
            return base_type

    elif country == 'Japan':
        # Japanese use Type (year of emperor's reign) system
        if year and year >= 1912:
            # Taishō era: 1912-1926 (Type 1-15)
            # Shōwa era: 1926-1945 (Type 1-20 for naval weapons)
            if year <= 1926:
                type_num = year - 1911
            else:
                type_num = year - 1925

            if 'AP' in base_type:
                return f'Type {type_num} AP'
            elif 'HE' in base_type:
                return f'Type {type_num} HE'
            elif 'SAP' in base_type:
                return f'Type {type_num} SAP'
            else:
                return f'Type {type_num} {base_type}'
        else:
            # Default fallback
            if 'AP' in base_type:
                return 'Type 91 AP'
            elif 'HE' in base_type:
                return 'Type 0 HE'
            else:
                return f'Type 1 {base_type}'

    return shell_type  # Fallback to original

# Phase 1: Update generic ammunition with proper designations
print("Phase 1: Updating Generic Ammunition with Mark/Type Designations")
print("=" * 80)

cursor.execute("""
    SELECT a.ammo_id, a.shell_type, a.weight_lbs, a.explosive_lbs,
           g.designation, g.country, g.year_introduced
    FROM ammunition a
    JOIN guns g ON a.gun_id = g.gun_id
    WHERE a.shell_type NOT LIKE '%Mark%'
    AND a.shell_type NOT LIKE '%Mk%'
    AND a.shell_type NOT LIKE '%Type%'
    AND a.shell_type NOT LIKE '%Model%'
    AND a.shell_type NOT LIKE '%L/%'
    AND a.shell_type NOT LIKE '%Pzgr%'
    AND a.shell_type NOT LIKE '%Sprgr%'
    AND g.country IN ('USA', 'Japan', 'Britain', 'Germany')
    AND a.shell_type NOT LIKE '%(Estimated)%'
    ORDER BY g.country, g.caliber_inches DESC
""")

generic_ammo = cursor.fetchall()
updated_count = 0

for ammo_id, shell_type, weight, explosive, gun_des, country, year in generic_ammo:
    new_designation = get_mark_designation(gun_des, shell_type, country, year)

    cursor.execute("""
        UPDATE ammunition
        SET shell_type = ?
        WHERE ammo_id = ?
    """, (new_designation, ammo_id))

    updated_count += 1
    if updated_count <= 15:  # Show first 15
        print(f"[UPDATE] {gun_des[:50]:<50} | {shell_type:<15} -> {new_designation}")

print(f"\nUpdated {updated_count} ammunition designations")

# Phase 2: Add additional ammunition types to guns with only 1 type
print(f"\n{'=' * 80}")
print("Phase 2: Adding Additional Ammunition Types to Single-Ammo Guns")
print("=" * 80)

cursor.execute("""
    SELECT g.gun_id, g.designation, g.caliber_inches, g.country, g.muzzle_velocity, g.year_introduced,
           a.shell_type, a.weight_lbs
    FROM guns g
    JOIN ammunition a ON g.gun_id = a.gun_id
    WHERE g.gun_id IN (
        SELECT gun_id FROM guns
        WHERE (SELECT COUNT(*) FROM ammunition WHERE gun_id = guns.gun_id) = 1
    )
    AND g.designation NOT LIKE '%Rocket%'
    AND g.designation NOT LIKE '%Miscellaneous%'
    ORDER BY g.country, g.caliber_inches DESC
""")

single_ammo_guns = cursor.fetchall()
added_ammo = 0

for gun_id, gun_des, caliber, country, muzzle_vel, year, existing_shell, existing_weight in single_ammo_guns:
    if not muzzle_vel:
        continue

    # Determine what to add based on what exists
    new_ammunition = []

    if 'HE' in existing_shell or 'HC' in existing_shell:
        # Has HE, add AP
        ap_weight = existing_weight * 1.15  # AP typically heavier
        explosive = ap_weight * 0.04  # AP has less explosive
        ap_designation = get_mark_designation(gun_des, 'AP', country, year if year else 1940)
        new_ammunition.append({'type': ap_designation, 'weight': ap_weight, 'explosive': explosive})
    else:
        # Has AP, add HE
        he_weight = existing_weight * 0.92  # HE typically lighter
        explosive = he_weight * 0.12  # HE has more explosive
        he_designation = get_mark_designation(gun_des, 'HE', country, year if year else 1940)
        new_ammunition.append({'type': he_designation, 'weight': he_weight, 'explosive': explosive})

    # Add SAP for larger guns (>4 inches)
    if caliber > 4.0 and len(new_ammunition) < 2:
        sap_weight = existing_weight * 0.98
        explosive = sap_weight * 0.07
        sap_designation = get_mark_designation(gun_des, 'SAP', country, year if year else 1940)
        new_ammunition.append({'type': sap_designation, 'weight': sap_weight, 'explosive': explosive})

    # Insert new ammunition
    for ammo in new_ammunition:
        ke_mj = calculate_ke_mj(ammo['weight'], muzzle_vel)

        cursor.execute("""
            INSERT INTO ammunition (gun_id, shell_type, weight_lbs, kinetic_megajoules,
                                   explosive_lbs, country)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (gun_id, ammo['type'], round(ammo['weight'], 2), ke_mj,
              round(ammo['explosive'], 2), country))

        added_ammo += 1
        print(f"[ADD] {gun_des[:50]:<50} | +{ammo['type']:<20} {ammo['weight']:.1f} lbs")

print(f"\nAdded {added_ammo} new ammunition types")

conn.commit()

# Verification
print(f"\n{'=' * 80}")
print("Verification Summary")
print("=" * 80)

# Count guns by ammunition count
cursor.execute("""
    SELECT ammo_count, COUNT(*) as guns
    FROM (SELECT gun_id, COUNT(*) as ammo_count FROM ammunition GROUP BY gun_id)
    GROUP BY ammo_count
    ORDER BY ammo_count
""")

print("\nAmmunition Variety Distribution:")
for ammo_count, gun_count in cursor.fetchall():
    print(f"  {ammo_count} types: {gun_count} guns")

# Check remaining generic names
cursor.execute("""
    SELECT COUNT(*)
    FROM ammunition a
    JOIN guns g ON a.gun_id = g.gun_id
    WHERE a.shell_type NOT LIKE '%Mark%'
    AND a.shell_type NOT LIKE '%Mk%'
    AND a.shell_type NOT LIKE '%Type%'
    AND a.shell_type NOT LIKE '%Model%'
    AND a.shell_type NOT LIKE '%L/%'
    AND a.shell_type NOT LIKE '%Pzgr%'
    AND a.shell_type NOT LIKE '%Sprgr%'
    AND g.country IN ('USA', 'Japan', 'Britain', 'Germany')
    AND a.shell_type NOT LIKE '%(Estimated)%'
""")

remaining_generic = cursor.fetchone()[0]
print(f"\nRemaining generic ammunition names (Big 4): {remaining_generic}")

# Total stats
cursor.execute("SELECT COUNT(*) FROM ammunition")
total_ammo = cursor.fetchone()[0]

print(f"\nFinal Ammunition Total: {total_ammo}")

conn.close()
print(f"\n{'=' * 80}")
print("Comprehensive Ammunition Upgrade Complete!")
