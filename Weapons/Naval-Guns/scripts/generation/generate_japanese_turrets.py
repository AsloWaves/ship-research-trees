"""
Generate German Naval Turrets (IDs 6100-4999)
Target: ~1,000 turrets for 100 German guns

Turret Types:
- Base: Single, Twin, Triple, Quad (4 per gun)
- Tactical Variants: DP, SP, Open (for applicable calibers)

Total: 100 guns × 10 turrets/gun = 1,000 turrets
"""

import json

# Load German guns
with open('../../data/fictional_german_guns.json', 'r', encoding='utf-8') as f:
    fictional_guns = json.load(f)

# Historical guns (IDs 700-722) - simplified list
historical_guns = []
for gun_id in range(800, 817):
    historical_guns.append({'Gun_ID': gun_id})

all_guns = historical_guns + fictional_guns
print(f"Loaded {len(all_guns)} German guns (IDs 700-799)")
print()

turrets = []
turret_id = 6100

# Turret type multipliers (from British system)
type_multipliers = {
    'Single': {'weight': 1.0, 'crew': 1.0, 'traverse': 1.2, 'rof': 1.1, 'armor_mult': 1.0},
    'Twin': {'weight': 2.3, 'crew': 2.2, 'traverse': 0.7, 'rof': 0.95, 'armor_mult': 1.1},
    'Triple': {'weight': 3.8, 'crew': 3.5, 'traverse': 0.5, 'rof': 0.85, 'armor_mult': 1.2},
    'Quad': {'weight': 5.2, 'crew': 4.8, 'traverse': 0.35, 'rof': 0.75, 'armor_mult': 1.3},
}

# Tactical variant multipliers
tactical_variants = {
    'DP': {  # Dual-Purpose (high-angle AA)
        'weight_mult': 1.15,
        'crew_mult': 1.1,
        'traverse_mult': 0.9,
        'elev_min': -10,
        'elev_max': 85,
        'rof_mult': 0.95,
        'armor_mult': 1.0,
        'notes': 'Dual-Purpose, high-angle AA capable'
    },
    'SP': {  # Surface-Purpose (faster, lighter)
        'weight_mult': 0.9,
        'crew_mult': 0.95,
        'traverse_mult': 1.15,
        'elev_min': -5,
        'elev_max': 35,
        'rof_mult': 1.05,
        'armor_mult': 0.9,
        'notes': 'Surface-Purpose, faster traverse, lower elevation'
    },
    'Open': {  # Open Mount (minimal armor)
        'weight_mult': 0.7,
        'crew_mult': 0.9,
        'traverse_mult': 1.25,
        'elev_min': -10,
        'elev_max': 45,
        'rof_mult': 1.1,
        'armor_mult': 0.5,
        'notes': 'Open Mount, minimal armor, light weight'
    }
}

def get_caliber_config(caliber):
    """Get turret configuration based on caliber"""
    # Parse caliber to get numeric value
    cal_str = caliber.replace('cm', '').replace('mm', '').replace('"', '')
    try:
        cal_value = float(cal_str)
    except:
        cal_value = 15.0  # Default

    # Battleship calibers (33cm+)
    if cal_value >= 33:
        return {
            'base_weight': cal_value * 3.2,
            'crew': int(cal_value * 0.7),
            'armor_face': cal_value * 0.45,
            'armor_sides': cal_value * 0.35,
            'armor_roof': cal_value * 0.25,
            'traverse_rate': 3.5,
            'elev_min': -5,
            'elev_max': 40,
            'elev_rate': 6.0,
            'rof': 2.5
        }
    # Heavy cruiser calibers (20-32cm)
    elif cal_value >= 20:
        return {
            'base_weight': cal_value * 2.8,
            'crew': int(cal_value * 0.65),
            'armor_face': cal_value * 0.4,
            'armor_sides': cal_value * 0.3,
            'armor_roof': cal_value * 0.2,
            'traverse_rate': 5.0,
            'elev_min': -5,
            'elev_max': 45,
            'elev_rate': 7.0,
            'rof': 4.0
        }
    # Light cruiser / Destroyer calibers (12-19cm)
    elif cal_value >= 12:
        return {
            'base_weight': cal_value * 2.5,
            'crew': int(cal_value * 0.6),
            'armor_face': cal_value * 0.35,
            'armor_sides': cal_value * 0.25,
            'armor_roof': cal_value * 0.15,
            'traverse_rate': 8.0,
            'elev_min': -8,
            'elev_max': 50,
            'elev_rate': 10.0,
            'rof': 8.0
        }
    # Dual-purpose calibers (8-11cm)
    elif cal_value >= 8:
        return {
            'base_weight': cal_value * 2.2,
            'crew': int(cal_value * 0.5),
            'armor_face': cal_value * 0.3,
            'armor_sides': cal_value * 0.2,
            'armor_roof': cal_value * 0.1,
            'traverse_rate': 12.0,
            'elev_min': -10,
            'elev_max': 80,
            'elev_rate': 15.0,
            'rof': 15.0
        }
    # Light AA calibers (3-7cm)
    elif cal_value >= 3:
        return {
            'base_weight': cal_value * 1.8,
            'crew': max(int(cal_value * 0.4), 4),
            'armor_face': cal_value * 0.2,
            'armor_sides': cal_value * 0.15,
            'armor_roof': cal_value * 0.05,
            'traverse_rate': 20.0,
            'elev_min': -10,
            'elev_max': 85,
            'elev_rate': 25.0,
            'rof': 30.0
        }
    # Very light AA (<3cm)
    else:
        return {
            'base_weight': cal_value * 1.5,
            'crew': max(int(cal_value * 0.3), 2),
            'armor_face': cal_value * 0.1,
            'armor_sides': cal_value * 0.08,
            'armor_roof': 0.0,
            'traverse_rate': 30.0,
            'elev_min': -10,
            'elev_max': 90,
            'elev_rate': 35.0,
            'rof': 50.0
        }

def create_turret(gun_id, caliber, turret_type, variant=None):
    """Create a turret with calculated specifications"""
    global turret_id

    config = get_caliber_config(caliber)
    mult = type_multipliers[turret_type]

    # Calculate base specifications
    weight = round(config['base_weight'] * mult['weight'], 2)
    crew = max(int(config['crew'] * mult['crew']), 2)
    armor_face = round(config['armor_face'] * mult['armor_mult'], 2)
    armor_sides = round(config['armor_sides'] * mult['armor_mult'], 2)
    armor_roof = round(config['armor_roof'] * mult['armor_mult'], 2)
    traverse = round(config['traverse_rate'] * mult['traverse'], 2)
    elev_min = config['elev_min']
    elev_max = config['elev_max']
    elev_rate = config['elev_rate']
    rof = round(config['rof'] * mult['rof'], 2)

    # Base designation
    type_german = {
        'Single': 'Einzellafette',
        'Twin': 'Doppellafette',
        'Triple': 'Drillingsafette',
        'Quad': 'Vierlingsafette'
    }
    designation = f"{caliber} {type_german[turret_type]}"
    notes = f"{caliber} {turret_type} turret, German design"

    # Apply tactical variant modifications
    if variant:
        var_config = tactical_variants[variant]
        weight = round(weight * var_config['weight_mult'], 2)
        crew = max(int(crew * var_config['crew_mult']), 2)
        traverse = round(traverse * var_config['traverse_mult'], 2)
        elev_min = var_config['elev_min']
        elev_max = var_config['elev_max']
        rof = round(rof * var_config['rof_mult'], 2)
        armor_face = round(armor_face * var_config['armor_mult'], 2)
        armor_sides = round(armor_sides * var_config['armor_mult'], 2)
        armor_roof = round(armor_roof * var_config['armor_mult'], 2)

        designation = f"{designation} {variant}"
        notes = f"{caliber} {turret_type} {variant} - {var_config['notes']}"

    turret = {
        'Turret_ID': turret_id,
        'Gun_ID': gun_id,
        'Country': 'Japan',
        'Caliber': caliber,
        'Turret_Type': turret_type,
        'Designation': designation,
        'Turret_Weight_Tons': weight,
        'Crew_Size': crew,
        'Armor_Face_IN': armor_face,
        'Armor_Sides_IN': armor_sides,
        'Armor_Roof_IN': armor_roof,
        'Traverse_Rate_Deg_Sec': traverse,
        'Elevation_Min_Deg': elev_min,
        'Elevation_Max_Deg': elev_max,
        'Elevation_Rate_Deg_Sec': elev_rate,
        'Rate_Of_Fire_RPM': rof,
        'Modded': 1,  # All turrets are generated/modded
        'Notes': notes
    }

    turret_id += 1
    return turret

# ============================================================================
# GENERATE TURRETS
# ============================================================================

print("Generating German turrets...")
print()

# For each gun, generate base turrets + tactical variants
for gun in all_guns:
    gun_id = gun['Gun_ID']

    # Determine caliber (need to load from research data for historical guns)
    if gun_id < 817:
        # Historical gun - assign caliber based on ID ranges
        if gun_id == 700:
            caliber = '40.6cm'
        elif gun_id <= 702:
            caliber = '38cm'
        elif gun_id <= 705:
            caliber = '28cm'
        elif gun_id <= 707:
            caliber = '20.3cm'
        elif gun_id <= 711:
            caliber = '15cm'
        elif gun_id <= 713:
            caliber = '12.8cm'
        elif gun_id <= 716:
            caliber = '10.5cm'
        elif gun_id <= 718:
            caliber = '8.8cm'
        elif gun_id <= 720:
            caliber = '3.7cm'
        else:
            caliber = '2cm'
    else:
        # Fictional gun - get from data
        caliber = gun.get('Caliber', '15cm')

    # Generate 4 base turret types
    for turret_type in ['Single', 'Twin', 'Triple', 'Quad']:
        turrets.append(create_turret(gun_id, caliber, turret_type))

    # Generate tactical variants for applicable calibers
    # Parse caliber to determine if variants should be generated
    cal_str = caliber.replace('cm', '').replace('mm', '').replace('"', '')
    try:
        cal_value = float(cal_str)
    except:
        cal_value = 15.0

    # Only generate variants for smaller calibers (<=20cm)
    if cal_value <= 20:
        for turret_type in ['Single', 'Twin', 'Triple']:
            for variant in ['DP', 'SP', 'Open']:
                turrets.append(create_turret(gun_id, caliber, turret_type, variant))

print(f"Generated {len(turrets)} turrets (IDs 6100-{turret_id-1})")
print()

# ============================================================================
# SAVE OUTPUT
# ============================================================================

print("=" * 80)
print("GERMAN TURRET GENERATION COMPLETE")
print("=" * 80)
print()
print(f"Total turrets generated: {len(turrets)}")
print(f"Turret ID range: 4000-{turret_id-1}")
print()

# Save as JSON
output_file = '../../data/japanese_turrets.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(turrets, f, indent=2, ensure_ascii=False)

print(f"Saved to: {output_file}")
print()

# Generate SQL INSERT statements (first 100 lines due to size)
sql_output = '../../data/japanese_turrets.sql'
with open(sql_output, 'w', encoding='utf-8') as f:
    f.write(f"-- German Naval Turrets (IDs 6100-{turret_id-1})\n")
    f.write(f"-- Total: {len(turrets)} turrets\n\n")
    f.write("INSERT INTO turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, "
            "Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, "
            "Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec, "
            "Rate_Of_Fire_RPM, Modded, Notes)\nVALUES\n")

    for i, turret in enumerate(turrets):
        notes_escaped = turret['Notes'].replace("'", "''")
        designation_escaped = turret['Designation'].replace("'", "''")
        comma = ',' if i < len(turrets) - 1 else ';'

        f.write(f"  ({turret['Turret_ID']}, {turret['Gun_ID']}, '{turret['Country']}', "
                f"'{turret['Caliber']}', '{turret['Turret_Type']}', '{designation_escaped}', "
                f"{turret['Turret_Weight_Tons']}, {turret['Crew_Size']}, "
                f"{turret['Armor_Face_IN']}, {turret['Armor_Sides_IN']}, {turret['Armor_Roof_IN']}, "
                f"{turret['Traverse_Rate_Deg_Sec']}, "
                f"{turret['Elevation_Min_Deg']}, {turret['Elevation_Max_Deg']}, {turret['Elevation_Rate_Deg_Sec']}, "
                f"{turret['Rate_Of_Fire_RPM']}, {turret['Modded']}, '{notes_escaped}'){comma}\n")

print(f"SQL INSERT statements saved to: {sql_output}")
print()

# Summary statistics
turret_types = {}
calibers = {}
for turret in turrets:
    ttype = turret['Turret_Type']
    cal = turret['Caliber']
    if ttype not in turret_types:
        turret_types[ttype] = 0
    if cal not in calibers:
        calibers[cal] = 0
    turret_types[ttype] += 1
    calibers[cal] += 1

print("Turret type distribution:")
for ttype in sorted(turret_types.keys()):
    print(f"  {ttype}: {turret_types[ttype]} turrets")
print()

print("Caliber distribution (top 15):")
sorted_calibers = sorted(calibers.items(), key=lambda x: x[1], reverse=True)
for cal, count in sorted_calibers[:15]:
    print(f"  {cal}: {count} turrets")
print()

print("=" * 80)
print("READY FOR DATABASE INTEGRATION")
print("=" * 80)
