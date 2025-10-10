"""
Generate British gun-ammunition compatibility records in SQL-ready format
Adds proper fields and calculates derived values
"""

import re

# Compatibility data from research
compatibility_data = [
    {
        'Gun_ID': 502,
        'Ammunition_ID': 101,
        'Caliber': '15"',
        'Muzzle_Velocity_FPS': 2450.0,
        'Max_Range_Yards': 33550.0,  # Standard elevation 30°
        'Notes': '15"/42 Mark I + 4crh AP shell, standard charge (428 lbs cordite)'
    },
    {
        'Gun_ID': 502,
        'Ammunition_ID': 102,
        'Caliber': '15"',
        'Muzzle_Velocity_FPS': 2640.0,
        'Max_Range_Yards': 37870.0,  # Vanguard with supercharge
        'Notes': '15"/42 Mark I + 6crh AP shell, supercharge (490 lbs cordite)'
    },
    {
        'Gun_ID': 502,
        'Ammunition_ID': 103,
        'Caliber': '15"',
        'Muzzle_Velocity_FPS': 2640.0,
        'Max_Range_Yards': 37870.0,
        'Notes': '15"/42 Mark I + Mark XIIIa APC (6crh + 4crh ballistic cap), supercharge'
    },
    {
        'Gun_ID': 502,
        'Ammunition_ID': 104,
        'Caliber': '15"',
        'Muzzle_Velocity_FPS': 2640.0,
        'Max_Range_Yards': 37870.0,
        'Notes': '15"/42 Mark I + Mark XVIIb APC (superior penetration, Cardonald manufacture)'
    },
    {
        'Gun_ID': 502,
        'Ammunition_ID': 105,
        'Caliber': '15"',
        'Muzzle_Velocity_FPS': 2450.0,
        'Max_Range_Yards': 33550.0,
        'Notes': '15"/42 Mark I + HE shell, standard charge'
    },
    {
        'Gun_ID': 502,
        'Ammunition_ID': 106,
        'Caliber': '15"',
        'Muzzle_Velocity_FPS': 2450.0,
        'Max_Range_Yards': 33550.0,
        'Notes': '15"/42 Mark I + CPC (Common Pointed Capped - semi-AP), standard charge'
    },
    {
        'Gun_ID': 504,
        'Ammunition_ID': 110,
        'Caliber': '14"',
        'Muzzle_Velocity_FPS': 2483.0,
        'Max_Range_Yards': 36000.0,  # Estimated @ 40° elevation
        'Notes': '14"/45 Mark VII + Mark VIIB APC shell (338.3 lbs cordite, 39.8 lbs bursting charge)'
    },
    {
        'Gun_ID': 504,
        'Ammunition_ID': 111,
        'Caliber': '14"',
        'Muzzle_Velocity_FPS': 2400.0,
        'Max_Range_Yards': 36000.0,  # Estimated @ 40° elevation
        'Notes': '14"/45 Mark VII + HE shell (338.3 lbs cordite, 107 lbs explosive)'
    },
]

# Calculate Muzzle_Velocity_MPS from FPS (1 fps = 0.3048 m/s)
for record in compatibility_data:
    record['Muzzle_Velocity_MPS'] = round(record['Muzzle_Velocity_FPS'] * 0.3048, 1)

# Generate markdown table
print()
print("## BRITISH GUN-AMMUNITION COMPATIBILITY TABLE")
print()
print("**Format**: SQL-ready markdown table for import")
print()
print("| Compatibility_ID | Gun_ID | Ammunition_ID | Notes | Caliber | Muzzle_Velocity_FPS | Muzzle_Velocity_MPS | Max_Range_Yards | Barrel_Wear_Per_Round |")
print("|------------------|--------|---------------|-------|---------|---------------------|---------------------|-----------------|-----------------------|")

compat_id_start = 10001  # British compatibility starts at 10001 (USA ends at ~15858)

for i, record in enumerate(compatibility_data):
    compat_id = compat_id_start + i
    gun_id = record['Gun_ID']
    ammo_id = record['Ammunition_ID']
    notes = record['Notes']
    caliber = record['Caliber']
    mv_fps = record['Muzzle_Velocity_FPS']
    mv_mps = record['Muzzle_Velocity_MPS']
    max_range = record['Max_Range_Yards']
    barrel_wear = ''  # Optional field, leave empty for now

    print(f"| {compat_id} | {gun_id} | {ammo_id} | {notes} | {caliber} | {mv_fps} | {mv_mps} | {max_range} | {barrel_wear} |")

print()
print(f"**Total Records**: {len(compatibility_data)}")
print()
print("**Notes**:")
print("- Compatibility_ID starts at 10001 (British range)")
print("- Muzzle_Velocity_MPS calculated from FPS (×0.3048)")
print("- Max_Range_Yards based on historical data and estimated elevation")
print("- Barrel_Wear_Per_Round optional (not yet researched)")
print()
print("**Status**: [OK] Ready for SQL import")
print()

# Also generate insert statements for quick reference
print()
print("## SQL INSERT STATEMENTS (Optional)")
print()
print("```sql")
for i, record in enumerate(compatibility_data):
    compat_id = compat_id_start + i
    gun_id = record['Gun_ID']
    ammo_id = record['Ammunition_ID']
    notes = record['Notes'].replace("'", "''")  # Escape single quotes
    caliber = record['Caliber']
    mv_fps = record['Muzzle_Velocity_FPS']
    mv_mps = record['Muzzle_Velocity_MPS']
    max_range = record['Max_Range_Yards']

    print(f"INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)")
    print(f"  VALUES ({compat_id}, {gun_id}, {ammo_id}, '{notes}', '{caliber}', {mv_fps}, {mv_mps}, {max_range});")

print("```")
print()
