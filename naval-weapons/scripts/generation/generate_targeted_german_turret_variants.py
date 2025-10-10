"""
Generate Targeted German Turret Variants
Current: 976 turrets (9.76 per gun)
Target: 2,100 turrets (21 per gun)
Need: EXACTLY 1,124 additional turrets

Strategy: Generate 1-2 variants per turret, but only for ~55-60% of base turrets
"""

import json
import random

# Set seed for reproducibility
random.seed(42)

# Load existing German turrets
with open('../../data/german_turrets.json', 'r', encoding='utf-8') as f:
    base_turrets = json.load(f)

target_total = 2100
target_additional = target_total - len(base_turrets)

print(f"Loaded {len(base_turrets)} existing German turrets")
print(f"Target total: {target_total} turrets (21 per gun)")
print(f"Need to generate: EXACTLY {target_additional} additional turrets")
print()

additional_turrets = []
turret_id = 4976

# ============================================================================
# VARIANT DEFINITIONS
# ============================================================================

all_variants = {
    'LA': {
        'name': 'Light Armor',
        'weight_mult': 0.85,
        'armor_mult': 0.7,
        'traverse_mult': 1.15,
        'rof_mult': 1.05,
        'notes_suffix': 'light armor'
    },
    'HA': {
        'name': 'Heavy Armor',
        'weight_mult': 1.20,
        'armor_mult': 1.4,
        'traverse_mult': 0.85,
        'rof_mult': 0.95,
        'notes_suffix': 'heavy armor'
    },
    'AA': {
        'name': 'AA-Optimized',
        'weight_mult': 1.05,
        'traverse_mult': 1.25,
        'elev_max_override': 85,
        'elev_rate_mult': 1.3,
        'rof_mult': 1.1,
        'notes_suffix': 'AA-optimized'
    },
    'Surf': {
        'name': 'Surface',
        'weight_mult': 1.10,
        'traverse_mult': 0.9,
        'elev_max_override': 35,
        'rof_mult': 1.05,
        'armor_mult': 1.1,
        'notes_suffix': 'surface combat'
    },
    'Shld': {
        'name': 'Shielded',
        'weight_mult': 0.95,
        'armor_mult': 0.6,
        'traverse_mult': 1.1,
        'rof_mult': 1.05,
        'notes_suffix': 'shield mount'
    },
    'Enc': {
        'name': 'Enclosed',
        'weight_mult': 1.15,
        'armor_mult': 1.2,
        'traverse_mult': 0.95,
        'crew_mult': 1.05,
        'notes_suffix': 'enclosed'
    },
    'CD': {
        'name': 'Coastal',
        'weight_mult': 1.25,
        'traverse_mult': 0.4,
        'armor_mult': 1.3,
        'rof_mult': 0.85,
        'notes_suffix': 'coastal defense'
    }
}

def get_caliber_value(caliber):
    """Extract numeric caliber value"""
    cal_str = caliber.replace('cm', '').replace('mm', '').replace('"', '')
    try:
        return float(cal_str)
    except:
        return 15.0

def get_applicable_variants(turret):
    """Get list of variants that make sense for this turret"""
    cal = get_caliber_value(turret['Caliber'])
    variants = []

    # All can have LA, HA, Enc
    variants.extend(['LA', 'HA', 'Enc'])

    # Small-medium calibers can have AA
    if cal <= 20:
        variants.append('AA')

    # Medium-large calibers can have Surf
    if cal >= 12:
        variants.append('Surf')

    # Large calibers can have CD
    if cal >= 15:
        variants.append('CD')

    # Small calibers can have Shld
    if cal <= 15:
        variants.append('Shld')

    return variants

def create_variant_turret(base_turret, variant_code):
    """Create a variant turret"""
    global turret_id

    variant_config = all_variants[variant_code]
    new_turret = base_turret.copy()
    new_turret['Turret_ID'] = turret_id
    turret_id += 1

    # Apply multipliers
    new_turret['Turret_Weight_Tons'] = round(
        base_turret['Turret_Weight_Tons'] * variant_config.get('weight_mult', 1.0), 2
    )
    new_turret['Armor_Face_IN'] = round(
        base_turret['Armor_Face_IN'] * variant_config.get('armor_mult', 1.0), 2
    )
    new_turret['Armor_Sides_IN'] = round(
        base_turret['Armor_Sides_IN'] * variant_config.get('armor_mult', 1.0), 2
    )
    new_turret['Armor_Roof_IN'] = round(
        base_turret['Armor_Roof_IN'] * variant_config.get('armor_mult', 1.0), 2
    )
    new_turret['Traverse_Rate_Deg_Sec'] = round(
        base_turret['Traverse_Rate_Deg_Sec'] * variant_config.get('traverse_mult', 1.0), 2
    )

    if 'elev_max_override' in variant_config:
        new_turret['Elevation_Max_Deg'] = variant_config['elev_max_override']

    if 'elev_rate_mult' in variant_config:
        new_turret['Elevation_Rate_Deg_Sec'] = round(
            base_turret['Elevation_Rate_Deg_Sec'] * variant_config['elev_rate_mult'], 2
        )

    new_turret['Rate_Of_Fire_RPM'] = round(
        base_turret['Rate_Of_Fire_RPM'] * variant_config.get('rof_mult', 1.0), 2
    )

    if 'crew_mult' in variant_config:
        new_turret['Crew_Size'] = max(int(base_turret['Crew_Size'] * variant_config['crew_mult']), 2)

    # Update designation and notes
    new_turret['Designation'] = f"{base_turret['Designation']} {variant_code}"
    new_turret['Notes'] = f"{base_turret['Notes']} - {variant_config['notes_suffix']}"

    return new_turret

# ============================================================================
# GENERATE EXACT NUMBER OF VARIANTS
# ============================================================================

print("Generating targeted variants...")
print()

# Create pool of possible variants
variant_pool = []
for base_turret in base_turrets:
    applicable = get_applicable_variants(base_turret)
    for variant_code in applicable:
        variant_pool.append((base_turret, variant_code))

print(f"Total possible variants: {len(variant_pool)}")
print(f"Selecting {target_additional} variants...")
print()

# Randomly select exactly the number we need
selected = random.sample(variant_pool, target_additional)

# Generate the selected variants
variant_counts = {}
for base_turret, variant_code in selected:
    new_turret = create_variant_turret(base_turret, variant_code)
    additional_turrets.append(new_turret)

    if variant_code not in variant_counts:
        variant_counts[variant_code] = 0
    variant_counts[variant_code] += 1

# ============================================================================
# COMBINE AND SAVE
# ============================================================================

all_turrets = base_turrets + additional_turrets

print("=" * 80)
print("TARGETED GERMAN TURRET VARIANTS GENERATED")
print("=" * 80)
print()
print(f"Base turrets: {len(base_turrets)}")
print(f"Additional variants: {len(additional_turrets)}")
print(f"Total turrets: {len(all_turrets)}")
print(f"Turrets per gun: {len(all_turrets) / 100:.2f}")
print()
print(f"[OK] Target achieved: {len(all_turrets)} turrets (target: {target_total})")
print()

print("Variant distribution:")
for variant_code in sorted(variant_counts.keys()):
    print(f"  {variant_code}: {variant_counts[variant_code]} turrets")
print()

# Save combined turrets
output_file = '../../data/german_turrets_complete.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_turrets, f, indent=2, ensure_ascii=False)

print(f"Saved to: {output_file}")
print()

# Generate SQL
sql_output = '../../data/german_turrets_additional.sql'
with open(sql_output, 'w', encoding='utf-8') as f:
    f.write(f"-- Additional German Naval Turrets (IDs {4976}-{turret_id-1})\n")
    f.write(f"-- Total: {len(additional_turrets)} additional turrets\n\n")
    f.write("INSERT INTO turrets (Turret_ID, Gun_ID, Country, Caliber, Turret_Type, Designation, "
            "Turret_Weight_Tons, Crew_Size, Armor_Face_IN, Armor_Sides_IN, Armor_Roof_IN, "
            "Traverse_Rate_Deg_Sec, Elevation_Min_Deg, Elevation_Max_Deg, Elevation_Rate_Deg_Sec, "
            "Rate_Of_Fire_RPM, Modded, Notes)\nVALUES\n")

    for i, turret in enumerate(additional_turrets):
        notes_escaped = turret['Notes'].replace("'", "''")
        designation_escaped = turret['Designation'].replace("'", "''")
        comma = ',' if i < len(additional_turrets) - 1 else ';'

        f.write(f"  ({turret['Turret_ID']}, {turret['Gun_ID']}, '{turret['Country']}', "
                f"'{turret['Caliber']}', '{turret['Turret_Type']}', '{designation_escaped}', "
                f"{turret['Turret_Weight_Tons']}, {turret['Crew_Size']}, "
                f"{turret['Armor_Face_IN']}, {turret['Armor_Sides_IN']}, {turret['Armor_Roof_IN']}, "
                f"{turret['Traverse_Rate_Deg_Sec']}, "
                f"{turret['Elevation_Min_Deg']}, {turret['Elevation_Max_Deg']}, {turret['Elevation_Rate_Deg_Sec']}, "
                f"{turret['Rate_Of_Fire_RPM']}, {turret['Modded']}, '{notes_escaped}'){comma}\n")

print(f"SQL saved to: {sql_output}")
print()

print("=" * 80)
print("READY FOR DATABASE INTEGRATION")
print("=" * 80)
