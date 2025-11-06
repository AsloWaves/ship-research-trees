"""
Generate Turrets for 60 Fictional British Guns
Creates comprehensive turret variants for each gun
Turret IDs: 3000-4999 (allocating 2000 IDs for expansion)
"""

import json

# Load the fictional guns
with open('../../data/fictional_british_guns.json', 'r', encoding='utf-8') as f:
    fictional_guns = json.load(f)

print("=" * 80)
print("GENERATING TURRETS FOR 60 FICTIONAL BRITISH GUNS")
print("=" * 80)
print()

# Turret generation parameters by caliber category
def get_turret_config(caliber):
    """Get turret configuration based on caliber"""
    cal_num = float(caliber.replace('"', ''))

    if cal_num >= 12.0:  # Heavy guns (18"-12")
        return {
            'types': ['Single', 'Twin', 'Triple', 'Quad'],
            'variants': ['DP', 'SP'],  # No Open for heavy guns
            'base_armor': {'face': cal_num, 'sides': cal_num * 0.7, 'roof': cal_num * 0.5},
            'base_crew_single': int(cal_num * 2.5),
            'base_weight_single': cal_num * 15
        }
    elif cal_num >= 6.0:  # Medium guns (10"-6")
        return {
            'types': ['Single', 'Twin', 'Triple', 'Quad'],
            'variants': ['DP', 'SP', 'Open'],
            'base_armor': {'face': cal_num * 0.8, 'sides': cal_num * 0.4, 'roof': cal_num * 0.25},
            'base_crew_single': int(cal_num * 2),
            'base_weight_single': cal_num * 10
        }
    else:  # Light guns (5.25"-3")
        return {
            'types': ['Single', 'Twin', 'Triple', 'Quad'],
            'variants': ['DP', 'SP', 'Open'],
            'base_armor': {'face': cal_num * 0.5, 'sides': cal_num * 0.25, 'roof': cal_num * 0.15},
            'base_crew_single': int(cal_num * 1.5),
            'base_weight_single': cal_num * 5
        }

# Calculate turret specifications
def calculate_turret_specs(gun, turret_type, variant=None):
    """Calculate realistic turret specifications"""
    config = get_turret_config(gun['Caliber'])
    cal_num = float(gun['Caliber'].replace('"', ''))

    # Base multipliers by turret type
    type_multipliers = {
        'Single': {'weight': 1.0, 'crew': 1.0, 'traverse': 1.0, 'rof': 1.0},
        'Twin': {'weight': 2.3, 'crew': 2.2, 'traverse': 0.7, 'rof': 0.95},
        'Triple': {'weight': 3.5, 'crew': 3.2, 'traverse': 0.55, 'rof': 0.9},
        'Quad': {'weight': 4.8, 'crew': 4.2, 'traverse': 0.45, 'rof': 0.85}
    }

    mult = type_multipliers[turret_type]

    # Base specifications
    weight = config['base_weight_single'] * mult['weight']
    crew = int(config['base_crew_single'] * mult['crew'])
    armor_face = config['base_armor']['face']
    armor_sides = config['base_armor']['sides']
    armor_roof = config['base_armor']['roof']
    traverse = (6.0 / cal_num) * mult['traverse']  # Smaller guns traverse faster
    elev_min = -5
    elev_max = 40  # Default surface engagement
    rof = (60 / cal_num) * mult['rof']  # Smaller guns fire faster

    # Variant modifications
    variant_suffix = ""
    modded = 1  # All fictional turrets are modded

    if variant == 'DP':  # Dual-Purpose (high-angle AA capable)
        elev_max = 85
        weight *= 1.15  # Heavier for AA mechanisms
        traverse *= 0.9  # Slightly slower
        armor_face *= 1.0  # Same armor
        variant_suffix = " DP"
        notes = f"Dual-purpose high-angle variant. Elevation: {elev_max}°. AA capable."
    elif variant == 'SP':  # Surface-Purpose (lighter, faster)
        elev_max = 40
        weight *= 0.9  # Lighter
        traverse *= 1.1  # Faster traverse
        armor_face *= 0.9  # Slightly less armor
        armor_sides *= 0.9
        variant_suffix = " SP"
        notes = f"Surface-purpose variant. Lighter armor, faster traverse."
    elif variant == 'Open':  # Open Mount (minimal armor)
        weight *= 0.55  # Much lighter
        traverse *= 1.5  # Much faster
        armor_face = 0.25  # Minimal shield only
        armor_sides = 0.0
        armor_roof = 0.0
        crew = int(crew * 0.7)  # Fewer crew
        variant_suffix = " Open Mount"
        notes = f"Open mount variant. Minimal armor, very light, fast traverse."
    else:  # Base variant
        notes = f"Standard {turret_type} mounting. Shell: {gun['Mark_Designation']}."

    # Build designation
    designation = f"{gun['Caliber']}{gun['Length']} {gun['Mark_Designation']} {turret_type}{variant_suffix}"

    return {
        'weight': round(weight, 1),
        'crew': max(crew, 4),  # Minimum 4 crew
        'armor_face': round(armor_face, 1),
        'armor_sides': round(armor_sides, 1),
        'armor_roof': round(armor_roof, 1),
        'traverse': round(traverse, 1),
        'elev_min': elev_min,
        'elev_max': elev_max,
        'rof': round(rof, 1),
        'designation': designation,
        'notes': notes,
        'modded': modded
    }

# Generate all turrets
all_turrets = []
turret_id = 3000  # Starting ID for new turrets

for gun in fictional_guns:
    config = get_turret_config(gun['Caliber'])
    gun_turrets = []

    # Generate base turret types
    for turret_type in config['types']:
        specs = calculate_turret_specs(gun, turret_type)

        turret = {
            'Turret_ID': turret_id,
            'Gun_ID': gun['Gun_ID'],
            'Country': 'Britain',
            'Caliber': gun['Caliber'],
            'Turret_Type': turret_type,
            'Designation': specs['designation'],
            'Turret_Weight_Tons': specs['weight'],
            'Crew_Size': specs['crew'],
            'Armor_Face_IN': specs['armor_face'],
            'Armor_Sides_IN': specs['armor_sides'],
            'Armor_Roof_IN': specs['armor_roof'],
            'Traverse_Rate_Deg_Sec': specs['traverse'],
            'Elevation_Min_Deg': specs['elev_min'],
            'Elevation_Max_Deg': specs['elev_max'],
            'Elevation_Rate_Deg_Sec': None,  # Not specified
            'Rate_Of_Fire_RPM': specs['rof'],
            'Modded': specs['modded'],
            'Notes': specs['notes']
        }

        all_turrets.append(turret)
        gun_turrets.append(turret)
        turret_id += 1

    # Generate variant turrets
    for variant in config['variants']:
        for turret_type in config['types']:
            specs = calculate_turret_specs(gun, turret_type, variant)

            turret = {
                'Turret_ID': turret_id,
                'Gun_ID': gun['Gun_ID'],
                'Country': 'Britain',
                'Caliber': gun['Caliber'],
                'Turret_Type': f"{turret_type} {variant}",
                'Designation': specs['designation'],
                'Turret_Weight_Tons': specs['weight'],
                'Crew_Size': specs['crew'],
                'Armor_Face_IN': specs['armor_face'],
                'Armor_Sides_IN': specs['armor_sides'],
                'Armor_Roof_IN': specs['armor_roof'],
                'Traverse_Rate_Deg_Sec': specs['traverse'],
                'Elevation_Min_Deg': specs['elev_min'],
                'Elevation_Max_Deg': specs['elev_max'],
                'Elevation_Rate_Deg_Sec': None,
                'Rate_Of_Fire_RPM': specs['rof'],
                'Modded': specs['modded'],
                'Notes': specs['notes']
            }

            all_turrets.append(turret)
            gun_turrets.append(turret)
            turret_id += 1

    print(f"Gun {gun['Gun_ID']} ({gun['Caliber']} {gun['Mark_Designation']}): {len(gun_turrets)} turrets")

print()
print(f"Total turrets generated: {len(all_turrets)}")
print(f"Turret ID range: 3000-{turret_id-1}")
print()

# Save to JSON
print("Saving turrets to JSON file...")
with open('../../data/fictional_british_turrets.json', 'w', encoding='utf-8') as f:
    json.dump(all_turrets, f, indent=2)

print("Saved to: ../../data/fictional_british_turrets.json")
print()

# Generate SQL INSERT statements
print("Generating SQL INSERT statements...")
sql_statements = []

for turret in all_turrets:
    notes_escaped = turret['Notes'].replace("'", "''")
    elev_rate = f"{turret['Elevation_Rate_Deg_Sec']}" if turret['Elevation_Rate_Deg_Sec'] else "NULL"

    sql = f"""INSERT INTO Turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec, Rate_Of_Fire_RPM, Modded, Notes)
VALUES ({turret['Turret_ID']}, {turret['Gun_ID']}, '{turret['Country']}', '{turret['Caliber']}', '{turret['Turret_Type']}', '{turret['Designation']}', {turret['Turret_Weight_Tons']}, {turret['Crew_Size']}, {turret['Armor_Face_IN']}, {turret['Armor_Sides_IN']}, {turret['Armor_Roof_IN']}, {turret['Traverse_Rate_Deg_Sec']}, {turret['Elevation_Min_Deg']}, {turret['Elevation_Max_Deg']}, {elev_rate}, {turret['Rate_Of_Fire_RPM']}, {turret['Modded']}, '{notes_escaped}');"""
    sql_statements.append(sql)

with open('../../database/sql/insert_fictional_british_turrets.sql', 'w', encoding='utf-8') as f:
    f.write("-- Fictional British Naval Turrets\n")
    f.write("-- Generated: October 10, 2025\n")
    f.write(f"-- Count: {len(all_turrets)} turrets\n")
    f.write(f"-- Turret IDs: 3000-{turret_id-1}\n")
    f.write("-- All marked as Modded=1 (fictional)\n\n")
    f.write('\n\n'.join(sql_statements))

print("Saved SQL to: ../../database/sql/insert_fictional_british_turrets.sql")
print()

# Statistics
print("=" * 80)
print("STATISTICS")
print("=" * 80)
print()

by_caliber = {}
for turret in all_turrets:
    cal = turret['Caliber']
    if cal not in by_caliber:
        by_caliber[cal] = 0
    by_caliber[cal] += 1

print("Turrets by caliber:")
for caliber in sorted(by_caliber.keys(), key=lambda x: float(x.replace('"', '')), reverse=True):
    print(f"  {caliber}: {by_caliber[caliber]} turrets")

print()
print("=" * 80)
print("FICTIONAL BRITISH TURRETS GENERATION COMPLETE")
print("=" * 80)
print(f"Generated {len(all_turrets)} turrets for 60 fictional guns")
print("All turrets marked as Modded=1 (fictional)")
print("Ready for ammunition generation (next phase)")
print()
