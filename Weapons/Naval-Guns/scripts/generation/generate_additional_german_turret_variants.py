"""
Generate Additional German Turret Variants
Current: 976 turrets (9.76 per gun)
Target: 2,100 turrets (21 per gun to match USA ratio)
Need: 1,124 additional turrets

Variants to generate:
1. Armor Variants: LA (Light), HA (Heavy), XHA (Extra-Heavy)
2. Role Variants: AA (AA-Optimized), Surf (Surface), CD (Coastal Defense)
3. Mount Variants: Shld (Shielded), Enc (Enclosed), Cas (Casemate)
"""

import json

# Load existing German turrets
with open('../../data/german_turrets.json', 'r', encoding='utf-8') as f:
    base_turrets = json.load(f)

print(f"Loaded {len(base_turrets)} existing German turrets")
print(f"Target: 2,100 turrets")
print(f"Need to generate: ~{2100 - len(base_turrets)} additional turrets")
print()

additional_turrets = []
turret_id = 4976  # Continue from last ID

# ============================================================================
# VARIANT DEFINITIONS
# ============================================================================

armor_variants = {
    'LA': {  # Light Armor
        'name': 'Light Armor',
        'weight_mult': 0.85,
        'armor_mult': 0.7,
        'traverse_mult': 1.15,
        'rof_mult': 1.05,
        'notes_suffix': 'light armor, increased speed'
    },
    'HA': {  # Heavy Armor
        'name': 'Heavy Armor',
        'weight_mult': 1.20,
        'armor_mult': 1.4,
        'traverse_mult': 0.85,
        'rof_mult': 0.95,
        'notes_suffix': 'heavy armor, extra protection'
    },
    'XHA': {  # Extra-Heavy Armor
        'name': 'Extra-Heavy Armor',
        'weight_mult': 1.35,
        'armor_mult': 1.7,
        'traverse_mult': 0.75,
        'rof_mult': 0.90,
        'notes_suffix': 'extra-heavy armor, maximum protection'
    }
}

role_variants = {
    'AA': {  # AA-Optimized
        'name': 'AA-Optimized',
        'weight_mult': 1.05,
        'traverse_mult': 1.25,
        'elev_max_override': 85,
        'elev_rate_mult': 1.3,
        'rof_mult': 1.1,
        'notes_suffix': 'AA-optimized, high elevation'
    },
    'Surf': {  # Surface-Optimized
        'name': 'Surface-Optimized',
        'weight_mult': 1.10,
        'traverse_mult': 0.9,
        'elev_max_override': 35,
        'rof_mult': 1.05,
        'armor_mult': 1.1,
        'notes_suffix': 'surface combat optimized'
    },
    'CD': {  # Coastal Defense
        'name': 'Coastal Defense',
        'weight_mult': 1.25,
        'traverse_mult': 0.4,
        'armor_mult': 1.3,
        'rof_mult': 0.85,
        'notes_suffix': 'coastal defense, limited traverse'
    }
}

mount_variants = {
    'Shld': {  # Shielded
        'name': 'Shielded',
        'weight_mult': 0.95,
        'armor_mult': 0.6,
        'traverse_mult': 1.1,
        'rof_mult': 1.05,
        'notes_suffix': 'gun shield mount'
    },
    'Enc': {  # Enclosed
        'name': 'Enclosed',
        'weight_mult': 1.15,
        'armor_mult': 1.2,
        'traverse_mult': 0.95,
        'crew_mult': 1.05,
        'notes_suffix': 'fully enclosed turret'
    },
    'Cas': {  # Casemate
        'name': 'Casemate',
        'weight_mult': 0.80,
        'armor_mult': 1.15,
        'traverse_mult': 0.3,
        'elev_max_override': 25,
        'notes_suffix': 'casemate mount, fixed'
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

def should_generate_armor_variant(turret, variant_code):
    """Determine if armor variant is applicable"""
    cal = get_caliber_value(turret['Caliber'])

    # All calibers can have armor variants, but:
    # - Very small calibers (<3cm) don't benefit from XHA
    # - Very large calibers (>30cm) always have heavy armor, so LA makes less sense

    if variant_code == 'LA':
        return cal < 30  # Light armor makes sense for smaller guns
    elif variant_code == 'HA':
        return True  # Heavy armor works for all
    elif variant_code == 'XHA':
        return cal >= 10  # Extra-heavy only for medium+ calibers
    return True

def should_generate_role_variant(turret, variant_code):
    """Determine if role variant is applicable"""
    cal = get_caliber_value(turret['Caliber'])

    if variant_code == 'AA':
        # AA-optimized makes sense for ≤20cm guns
        return cal <= 20
    elif variant_code == 'Surf':
        # Surface-optimized makes sense for ≥12cm guns
        return cal >= 12
    elif variant_code == 'CD':
        # Coastal defense makes sense for ≥15cm guns
        return cal >= 15
    return True

def should_generate_mount_variant(turret, variant_code):
    """Determine if mount variant is applicable"""
    cal = get_caliber_value(turret['Caliber'])

    if variant_code == 'Shld':
        # Shield mounts for small-medium guns
        return 3 <= cal <= 15
    elif variant_code == 'Enc':
        # Enclosed for all sizes
        return True
    elif variant_code == 'Cas':
        # Casemate for medium-large guns
        return cal >= 10
    return True

def create_variant_turret(base_turret, variant_type, variant_code, variant_config):
    """Create a variant turret from base turret"""
    global turret_id

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
# GENERATE VARIANTS
# ============================================================================

print("Generating armor variants...")
armor_count = 0
for base_turret in base_turrets:
    for variant_code, variant_config in armor_variants.items():
        if should_generate_armor_variant(base_turret, variant_code):
            additional_turrets.append(
                create_variant_turret(base_turret, 'armor', variant_code, variant_config)
            )
            armor_count += 1

print(f"  Generated {armor_count} armor variant turrets")
print()

print("Generating role variants...")
role_count = 0
for base_turret in base_turrets:
    for variant_code, variant_config in role_variants.items():
        if should_generate_role_variant(base_turret, variant_code):
            additional_turrets.append(
                create_variant_turret(base_turret, 'role', variant_code, variant_config)
            )
            role_count += 1

print(f"  Generated {role_count} role variant turrets")
print()

print("Generating mount variants...")
mount_count = 0
for base_turret in base_turrets:
    for variant_code, variant_config in mount_variants.items():
        if should_generate_mount_variant(base_turret, variant_code):
            additional_turrets.append(
                create_variant_turret(base_turret, 'mount', variant_code, variant_config)
            )
            mount_count += 1

print(f"  Generated {mount_count} mount variant turrets")
print()

# ============================================================================
# COMBINE AND SAVE
# ============================================================================

all_turrets = base_turrets + additional_turrets

print("=" * 80)
print("ADDITIONAL GERMAN TURRET VARIANTS GENERATED")
print("=" * 80)
print()
print(f"Base turrets: {len(base_turrets)}")
print(f"Additional variants: {len(additional_turrets)}")
print(f"  - Armor variants: {armor_count}")
print(f"  - Role variants: {role_count}")
print(f"  - Mount variants: {mount_count}")
print(f"Total turrets: {len(all_turrets)}")
print(f"Turrets per gun: {len(all_turrets) / 100:.2f}")
print(f"Target achieved: {len(all_turrets) >= 2100}")
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

# Variant type distribution
print("Variant distribution:")
variant_types = {}
for turret in additional_turrets:
    # Extract variant code from designation
    parts = turret['Designation'].split()
    if len(parts) > 0:
        variant = parts[-1]
        if variant not in variant_types:
            variant_types[variant] = 0
        variant_types[variant] += 1

for variant in sorted(variant_types.keys()):
    print(f"  {variant}: {variant_types[variant]} turrets")
print()

print("=" * 80)
print("READY FOR DATABASE INTEGRATION")
print("=" * 80)
