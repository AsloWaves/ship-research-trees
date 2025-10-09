"""
Generate all missing turret configurations for each gun
Create fictional variants (single, twin, triple, quad) based on existing turrets or patterns
"""

import json
import re

# Load missing configs
with open('missing_turret_configs.json', 'r') as f:
    missing_configs = json.load(f)

# Read database to get existing turret data and find next turret ID
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find turrets section
turrets_start = None
turrets_end = None
for i, line in enumerate(lines):
    if '## Turrets Table' in line:
        turrets_start = i
    elif turrets_start and '## Gun Ammunition Compatibility' in line:
        turrets_end = i
        break

# Parse existing turrets to find reference turrets and max ID
turrets_header_idx = None
for i in range(turrets_start, turrets_end):
    if lines[i].strip().startswith('|') and 'Turret_ID' in lines[i]:
        turrets_header_idx = i
        break

turrets_header = [col.strip() for col in lines[turrets_header_idx].split('|')[1:-1]]
turrets_data_start = turrets_header_idx + 2

# Parse existing turrets for reference data
existing_turrets = {}
max_turret_id = 0

for i in range(turrets_data_start, turrets_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(turrets_header):
        continue

    turret_data = dict(zip(turrets_header, cols))
    turret_id = int(turret_data['Turret_ID'])
    gun_id = turret_data['Gun_ID']

    max_turret_id = max(max_turret_id, turret_id)

    # Store for reference
    if gun_id not in existing_turrets:
        existing_turrets[gun_id] = []
    existing_turrets[gun_id].append(turret_data)

print(f"Max existing turret ID: {max_turret_id}")
print(f"Will generate turret IDs starting from: {max_turret_id + 1}")
print()

# Barrel count mapping
barrel_counts = {'Single': 1, 'Twin': 2, 'Triple': 3, 'Quad': 4}

# Weight scaling factors (from analysis of existing data)
weight_scaling = {'Single': 0.45, 'Twin': 0.75, 'Triple': 1.0, 'Quad': 1.35}

# Crew scaling (from our formulas)
crew_base_per_barrel = {
    '18"': 32, '16"': 32, '14"': 32, '13"': 28, '12"': 28,
    '10"': 15, '8"': 15, '6"': 12, '5"': 9, '4"': 6, '3"': 3
}
crew_efficiency = {'Single': 1.0, 'Twin': 1.8, 'Triple': 2.5, 'Quad': 3.2}

# Traverse rate adjustment (heavier = slower)
traverse_base = {'Single': 1.3, 'Twin': 1.0, 'Triple': 0.75, 'Quad': 0.60}

def parse_turret_type(turret_type_str):
    """Extract turret configuration from string"""
    turret_type_str = turret_type_str.lower()
    if 'single' in turret_type_str:
        return 'Single'
    elif 'twin' in turret_type_str or 'double' in turret_type_str or 'dual' in turret_type_str:
        return 'Twin'
    elif 'triple' in turret_type_str:
        return 'Triple'
    elif 'quad' in turret_type_str:
        return 'Quad'
    return 'Single'

def estimate_crew(caliber, config):
    """Estimate crew based on caliber and configuration"""
    base = crew_base_per_barrel.get(caliber, 9)
    efficiency = crew_efficiency[config]
    return int(round(base * efficiency))

def estimate_armor(caliber):
    """Estimate armor based on caliber"""
    cal_num = float(caliber.replace('"', ''))
    if cal_num >= 16:
        return 17.0, 9.5, 7.0
    elif cal_num >= 14:
        return 16.0, 8.8, 4.8
    elif cal_num >= 12:
        return 13.0, 7.2, 3.9
    elif cal_num >= 8:
        return 6.0, 3.3, 1.8
    elif cal_num >= 6:
        return 3.5, 1.9, 1.1
    elif cal_num >= 5:
        return 1.5, 0.8, 0.4
    else:
        return 0.5, 0.3, 0.1

def estimate_traverse_rate(caliber, weight, config):
    """Estimate traverse rate"""
    cal_num = float(caliber.replace('"', ''))
    if cal_num <= 3:
        base_rate = 25.0
    elif cal_num <= 6:
        base_rate = 10.0
    elif cal_num <= 10:
        base_rate = 5.0
    else:
        base_rate = 4.0

    # Adjust for weight
    if weight > 0:
        weight_factor = (1000 / weight) ** 0.3
        base_rate *= weight_factor

    # Adjust for configuration
    base_rate *= traverse_base[config]

    return round(max(0.5, min(30.0, base_rate)), 1)

def estimate_elevation_rate(traverse_rate, caliber):
    """Estimate elevation rate"""
    cal_num = float(caliber.replace('"', ''))
    if cal_num >= 12:
        return round(traverse_rate * 2.5, 1)
    elif cal_num >= 6:
        return round(traverse_rate * 1.5, 1)
    else:
        return round(traverse_rate * 0.9, 1)

# Generate new turrets
new_turrets = []
next_id = max_turret_id + 1

print("=" * 80)
print("GENERATING FICTIONAL TURRET VARIANTS")
print("=" * 80)
print()

for config_data in missing_configs:
    gun_id = config_data['gun_id']
    caliber = config_data['caliber']
    mark = config_data['mark']
    config = config_data['config']

    # Find reference turret (same gun, any existing config)
    reference_turrets = existing_turrets.get(gun_id, [])

    if reference_turrets:
        # Use first available as reference
        ref = reference_turrets[0]
        ref_config = parse_turret_type(ref['Turret_Type'])
        ref_weight = float(ref['Turret_Weight_Tons']) if ref['Turret_Weight_Tons'] else 100.0
        ref_crew = int(ref['Crew_Size']) if ref['Crew_Size'] else estimate_crew(caliber, ref_config)
        ref_armor_face = float(ref['Armor_Face_IN']) if ref['Armor_Face_IN'] else estimate_armor(caliber)[0]
        ref_armor_sides = float(ref['Armor_Sides_IN']) if ref['Armor_Sides_IN'] else estimate_armor(caliber)[1]
        ref_armor_roof = float(ref['Armor_Roof_IN']) if ref['Armor_Roof_IN'] else estimate_armor(caliber)[2]
        ref_traverse = float(ref['Traverse_Rate_Deg_Sec']) if ref['Traverse_Rate_Deg_Sec'] else 4.0

        # Scale reference turret to new configuration
        # Weight scales with barrel count
        scale_factor = weight_scaling[config] / weight_scaling[ref_config]
        new_weight = round(ref_weight * scale_factor, 1)

        # Crew scales with configuration
        new_crew = estimate_crew(caliber, config)

        # Armor stays same (doesn't change with barrel count)
        new_armor_face = ref_armor_face
        new_armor_sides = ref_armor_sides
        new_armor_roof = ref_armor_roof

        # Traverse rate adjusts for weight
        new_traverse = estimate_traverse_rate(caliber, new_weight, config)
        new_elevation = estimate_elevation_rate(new_traverse, caliber)

    else:
        # No reference turret, estimate everything
        new_weight = 100.0 * weight_scaling[config]
        new_crew = estimate_crew(caliber, config)
        new_armor_face, new_armor_sides, new_armor_roof = estimate_armor(caliber)
        new_traverse = estimate_traverse_rate(caliber, new_weight, config)
        new_elevation = estimate_elevation_rate(new_traverse, caliber)

    # Create new turret entry
    new_turret = {
        'Turret_ID': str(next_id),
        'Gun_ID': gun_id,
        'Country': 'USA',
        'Turret_Type': config,
        'Designation': f'{caliber} Mark {mark} {config} Turret',
        'Turret_Weight_Tons': str(new_weight),
        'Crew_Size': str(new_crew),
        'Armor_Face_IN': str(new_armor_face),
        'Armor_Sides_IN': str(new_armor_sides),
        'Armor_Roof_IN': str(new_armor_roof),
        'Traverse_Rate_Deg_Sec': str(new_traverse),
        'Elevation_Min_Deg': '-5.0',
        'Elevation_Max_Deg': '45.0',
        'Elevation_Rate_Deg_Sec': str(new_elevation),
        'Rate_Of_Fire_RPM': '2.0',
        'Modded': '1',
        'Notes': f'Fictional {config.lower()} turret variant for {caliber} Mark {mark}. Generated from patterns.'
    }

    new_turrets.append(new_turret)
    next_id += 1

    print(f"[{len(new_turrets):3d}] ID {new_turret['Turret_ID']:4s} | Gun {gun_id:3s} | {caliber:5s} Mark {mark:10s} | {config:6s} | Crew={new_crew:3d}, Weight={new_weight:6.1f}T")

print()
print("=" * 80)
print(f"Generated {len(new_turrets)} fictional turret variants")
print("=" * 80)
print()

# Insert new turrets into database
print("Inserting new turrets into database...")

# Find insertion point (just before the compatibility table)
insert_point = turrets_end - 1

# Format new turret rows
new_lines = []
for turret in new_turrets:
    row = '| ' + ' | '.join([turret[col] for col in turrets_header]) + ' |\n'
    new_lines.append(row)

# Insert into lines
lines = lines[:insert_point] + new_lines + lines[insert_point:]

# Write back to file
with open('naval_guns_database.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"[SUCCESS] Added {len(new_turrets)} turrets to naval_guns_database.md")
print("=" * 80)

# Summary by configuration
from collections import Counter
config_counts = Counter([t['Turret_Type'] for t in new_turrets])

print("\nSUMMARY BY CONFIGURATION:")
for config in ['Single', 'Twin', 'Triple', 'Quad']:
    print(f"  {config:6s}: {config_counts[config]:3d} turrets generated")

print()
print("All new turrets marked as Modded=1 (fictional)")
print("Next step: Verify database integrity with analyze_completeness.py")
