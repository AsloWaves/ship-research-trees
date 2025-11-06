"""
Generate Selective German Turret Variants
Current: 976 turrets (9.76 per gun)
Target: 2,100 turrets (21 per gun to match USA ratio)
Need: ~1,124 additional turrets

Strategy: Only generate 1-2 variant types per base turret
- Large calibers (≥20cm): Armor variants only (LA, HA)
- Medium calibers (10-19cm): Role variants (AA, Surf) + 1 mount variant (Enc)
- Small calibers (≤9cm): Mount variants (Shld, Enc) + Role (AA)
"""

import json

# Load existing German turrets
with open('../../data/german_turrets.json', 'r', encoding='utf-8') as f:
    base_turrets = json.load(f)

print(f"Loaded {len(base_turrets)} existing German turrets")
print(f"Target: ~2,100 turrets")
print(f"Need to generate: ~{2100 - len(base_turrets)} additional turrets")
print()

additional_turrets = []
turret_id = 4976  # Continue from last ID

# ============================================================================
# VARIANT DEFINITIONS (same as before)
# ============================================================================

armor_variants = {
    'LA': {
        'name': 'Light Armor',
        'weight_mult': 0.85,
        'armor_mult': 0.7,
        'traverse_mult': 1.15,
        'rof_mult': 1.05,
        'notes_suffix': 'light armor, increased speed'
    },
    'HA': {
        'name': 'Heavy Armor',
        'weight_mult': 1.20,
        'armor_mult': 1.4,
        'traverse_mult': 0.85,
        'rof_mult': 0.95,
        'notes_suffix': 'heavy armor, extra protection'
    }
}

role_variants = {
    'AA': {
        'name': 'AA-Optimized',
        'weight_mult': 1.05,
        'traverse_mult': 1.25,
        'elev_max_override': 85,
        'elev_rate_mult': 1.3,
        'rof_mult': 1.1,
        'notes_suffix': 'AA-optimized, high elevation'
    },
    'Surf': {
        'name': 'Surface-Optimized',
        'weight_mult': 1.10,
        'traverse_mult': 0.9,
        'elev_max_override': 35,
        'rof_mult': 1.05,
        'armor_mult': 1.1,
        'notes_suffix': 'surface combat optimized'
    }
}

mount_variants = {
    'Shld': {
        'name': 'Shielded',
        'weight_mult': 0.95,
        'armor_mult': 0.6,
        'traverse_mult': 1.1,
        'rof_mult': 1.05,
        'notes_suffix': 'gun shield mount'
    },
    'Enc': {
        'name': 'Enclosed',
        'weight_mult': 1.15,
        'armor_mult': 1.2,
        'traverse_mult': 0.95,
        'crew_mult': 1.05,
        'notes_suffix': 'fully enclosed turret'
    }
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_caliber_value(caliber):
    """Extract numeric caliber value"""
    cal_str = caliber.replace('cm', '').replace('mm', '').replace('"', '')
    try:
        return float(cal_str)
    except:
        return 15.0

def get_variants_for_turret(turret):
    """Determine which variants to generate for this turret"""
    cal = get_caliber_value(turret['Caliber'])
    variants_to_generate = []

    # Large calibers (≥20cm): 2 armor variants = 2 per turret
    if cal >= 20:
        variants_to_generate.extend([
            ('armor', 'LA'),
            ('armor', 'HA')
        ])

    # Medium calibers (10-19cm): 2 role + 1 mount = 3 per turret
    elif cal >= 10:
        variants_to_generate.extend([
            ('role', 'AA'),
            ('role', 'Surf'),
            ('mount', 'Enc')
        ])

    # Small calibers (≤9cm): 2 mount + 1 role = 3 per turret
    else:
        variants_to_generate.extend([
            ('mount', 'Shld'),
            ('mount', 'Enc'),
            ('role', 'AA')
        ])

    return variants_to_generate

def create_variant_turret(base_turret, variant_type, variant_code):
    """Create a variant turret from base turret"""
    global turret_id

    # Get variant config
    if variant_type == 'armor':
        variant_config = armor_variants[variant_code]
    elif variant_type == 'role':
        variant_config = role_variants[variant_code]
    elif variant_type == 'mount':
        variant_config = mount_variants[variant_code]
    else:
        return None

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
# GENERATE SELECTIVE VARIANTS
# ============================================================================

print("Generating selective variants based on caliber...")
print()

variant_counts = {'armor': 0, 'role': 0, 'mount': 0}

for base_turret in base_turrets:
    variants = get_variants_for_turret(base_turret)

    for variant_type, variant_code in variants:
        new_turret = create_variant_turret(base_turret, variant_type, variant_code)
        if new_turret:
            additional_turrets.append(new_turret)
            variant_counts[variant_type] += 1

# ============================================================================
# COMBINE AND SAVE
# ============================================================================

all_turrets = base_turrets + additional_turrets

print("=" * 80)
print("SELECTIVE GERMAN TURRET VARIANTS GENERATED")
print("=" * 80)
print()
print(f"Base turrets: {len(base_turrets)}")
print(f"Additional variants: {len(additional_turrets)}")
print(f"  - Armor variants: {variant_counts['armor']}")
print(f"  - Role variants: {variant_counts['role']}")
print(f"  - Mount variants: {variant_counts['mount']}")
print(f"Total turrets: {len(all_turrets)}")
print(f"Turrets per gun: {len(all_turrets) / 100:.2f}")
print()

# Compare to target
target_ratio = 21.0
actual_ratio = len(all_turrets) / 100
if actual_ratio >= target_ratio * 0.9 and actual_ratio <= target_ratio * 1.1:
    print(f"✓ Target achieved: {actual_ratio:.2f} turrets/gun (target: {target_ratio})")
else:
    print(f"Target: {target_ratio} turrets/gun")
    print(f"Actual: {actual_ratio:.2f} turrets/gun")
    diff = int((target_ratio - actual_ratio) * 100)
    if diff > 0:
        print(f"Need {diff} more turrets to reach target")
    else:
        print(f"Exceeded target by {-diff} turrets")
print()

# Save combined turrets
output_file = '../../data/german_turrets_complete.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_turrets, f, indent=2, ensure_ascii=False)

print(f"Saved complete turret set to: {output_file}")
print()

# Generate SQL for additional turrets only
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

print(f"SQL for additional turrets saved to: {sql_output}")
print()

print("=" * 80)
print("READY FOR DATABASE INTEGRATION")
print("=" * 80)
