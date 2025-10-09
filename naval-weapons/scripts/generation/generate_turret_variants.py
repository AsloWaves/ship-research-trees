"""
Generate additional turret variants:
1. Dual Purpose (DP) vs Single Purpose (SP) - for 3", 4", 5", 6" guns
2. Armored vs Open mount variants - for 3", 4", 5" guns

DP variants: High elevation (85°), optimized for AA
SP variants: Standard elevation (45°), optimized for surface targets
Open variants: Minimal armor, lighter, faster traverse
Armored variants: Standard armor, crew protection
"""

import re

# Read database
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

turrets_header_idx = None
for i in range(turrets_start, turrets_end):
    if lines[i].strip().startswith('|') and 'Turret_ID' in lines[i]:
        turrets_header_idx = i
        break

turrets_header = [col.strip() for col in lines[turrets_header_idx].split('|')[1:-1]]
turrets_data_start = turrets_header_idx + 2

# Parse existing turrets
existing_turrets = []
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
    max_turret_id = max(max_turret_id, turret_id)
    existing_turrets.append(turret_data)

print(f"Found {len(existing_turrets)} existing turrets")
print(f"Max turret ID: {max_turret_id}")
print()

# Parse caliber from designation
def parse_caliber_num(designation):
    """Extract numeric caliber"""
    match = re.search(r'(\d+\.?\d*)"', designation)
    if match:
        return float(match.group(1))
    return None

# Identify turrets suitable for variants
dp_sp_candidates = []  # 3-6" guns suitable for DP/SP variants
armored_open_candidates = []  # 3-5" guns suitable for armored/open variants

for turret in existing_turrets:
    caliber = parse_caliber_num(turret['Designation'])
    if not caliber:
        continue

    designation = turret['Designation']
    turret_id = turret['Turret_ID']
    gun_id = turret['Gun_ID']

    # Skip if already has DP in name
    if 'DP' in designation.upper():
        continue

    # DP/SP candidates: 3-6" guns
    if 3.0 <= caliber <= 6.0:
        dp_sp_candidates.append(turret)

    # Armored/Open candidates: 3-5" guns
    if 3.0 <= caliber <= 5.0:
        # Check if it's not already an "open" mount designation
        if 'Open' not in designation and 'Pedestal' not in designation:
            armored_open_candidates.append(turret)

print(f"DP/SP variant candidates: {len(dp_sp_candidates)} turrets (3-6\" guns)")
print(f"Armored/Open variant candidates: {len(armored_open_candidates)} turrets (3-5\" guns)")
print()

# Generate variants
new_turrets = []
next_id = max_turret_id + 1

print("=" * 80)
print("GENERATING TURRET VARIANTS")
print("=" * 80)
print()

# 1. Generate DP variants (high elevation, AA capable)
print("PHASE 1: DUAL PURPOSE (DP) VARIANTS")
print("-" * 80)

for base_turret in dp_sp_candidates:
    caliber = parse_caliber_num(base_turret['Designation'])

    # Create DP variant (if not already DP)
    if 'DP' not in base_turret['Designation'].upper():
        dp_variant = base_turret.copy()
        dp_variant['Turret_ID'] = str(next_id)
        dp_variant['Designation'] = base_turret['Designation'].replace('Turret', 'DP Turret')

        # DP modifications
        dp_variant['Elevation_Max_Deg'] = '85.0'  # High elevation for AA

        # Slightly heavier (DP fire control systems)
        base_weight = float(base_turret['Turret_Weight_Tons'])
        dp_variant['Turret_Weight_Tons'] = str(round(base_weight * 1.15, 1))

        # Slightly slower traverse (heavier)
        base_traverse = float(base_turret['Traverse_Rate_Deg_Sec'])
        dp_variant['Traverse_Rate_Deg_Sec'] = str(round(base_traverse * 0.9, 1))

        # Higher elevation rate (optimized for AA)
        base_elev_rate = float(base_turret['Elevation_Rate_Deg_Sec'])
        dp_variant['Elevation_Rate_Deg_Sec'] = str(round(base_elev_rate * 1.3, 1))

        dp_variant['Modded'] = '1'
        dp_variant['Notes'] = f"Dual-purpose variant of {base_turret['Turret_ID']} with high elevation for AA capability. Generated variant."

        new_turrets.append(dp_variant)
        next_id += 1

        print(f"[{len(new_turrets):3d}] ID {dp_variant['Turret_ID']:4s} | {caliber:.1f}\" DP variant | Elev=85°, Weight={dp_variant['Turret_Weight_Tons']}T")

print(f"\nGenerated {len(new_turrets)} DP variants")
print()

# 2. Generate SP variants (standard elevation, surface optimized)
print("PHASE 2: SINGLE PURPOSE (SP) VARIANTS")
print("-" * 80)

sp_count_start = len(new_turrets)

for base_turret in dp_sp_candidates:
    caliber = parse_caliber_num(base_turret['Designation'])

    # Create SP variant (surface-only, lower elevation)
    if 'SP' not in base_turret['Designation'].upper() and 'DP' not in base_turret['Designation'].upper():
        sp_variant = base_turret.copy()
        sp_variant['Turret_ID'] = str(next_id)
        sp_variant['Designation'] = base_turret['Designation'].replace('Turret', 'SP Turret')

        # SP modifications
        sp_variant['Elevation_Max_Deg'] = '40.0'  # Lower elevation, surface targets only

        # Lighter (no AA systems)
        base_weight = float(base_turret['Turret_Weight_Tons'])
        sp_variant['Turret_Weight_Tons'] = str(round(base_weight * 0.90, 1))

        # Faster traverse (lighter)
        base_traverse = float(base_turret['Traverse_Rate_Deg_Sec'])
        sp_variant['Traverse_Rate_Deg_Sec'] = str(round(base_traverse * 1.1, 1))

        # Lower elevation rate (not needed for AA)
        base_elev_rate = float(base_turret['Elevation_Rate_Deg_Sec'])
        sp_variant['Elevation_Rate_Deg_Sec'] = str(round(base_elev_rate * 0.8, 1))

        sp_variant['Modded'] = '1'
        sp_variant['Notes'] = f"Single-purpose surface variant of {base_turret['Turret_ID']}, lighter and faster. Generated variant."

        new_turrets.append(sp_variant)
        next_id += 1

        print(f"[{len(new_turrets):3d}] ID {sp_variant['Turret_ID']:4s} | {caliber:.1f}\" SP variant | Elev=40°, Weight={sp_variant['Turret_Weight_Tons']}T")

sp_count = len(new_turrets) - sp_count_start
print(f"\nGenerated {sp_count} SP variants")
print()

# 3. Generate Open mount variants (minimal armor, light, fast)
print("PHASE 3: OPEN MOUNT VARIANTS")
print("-" * 80)

open_count_start = len(new_turrets)

for base_turret in armored_open_candidates:
    caliber = parse_caliber_num(base_turret['Designation'])

    # Skip if weight is already very light (likely already open mount)
    base_weight = float(base_turret['Turret_Weight_Tons'])
    if base_weight < 15:  # Very light, probably already open
        continue

    # Create Open mount variant
    open_variant = base_turret.copy()
    open_variant['Turret_ID'] = str(next_id)
    open_variant['Designation'] = base_turret['Designation'].replace('Turret', 'Open Mount').replace('Mount', 'Open Mount')

    # Open mount modifications
    # Minimal armor
    open_variant['Armor_Face_IN'] = '0.25'  # Gun shield only
    open_variant['Armor_Sides_IN'] = '0.0'   # No side armor
    open_variant['Armor_Roof_IN'] = '0.0'    # No roof

    # Much lighter (no turret structure)
    open_variant['Turret_Weight_Tons'] = str(round(base_weight * 0.55, 1))

    # Much faster traverse
    base_traverse = float(base_turret['Traverse_Rate_Deg_Sec'])
    open_variant['Traverse_Rate_Deg_Sec'] = str(round(base_traverse * 1.5, 1))

    # Faster elevation
    base_elev_rate = float(base_turret['Elevation_Rate_Deg_Sec'])
    open_variant['Elevation_Rate_Deg_Sec'] = str(round(base_elev_rate * 1.5, 1))

    # Lower crew (no enclosed turret crew)
    base_crew = int(base_turret['Crew_Size'])
    open_variant['Crew_Size'] = str(max(3, int(base_crew * 0.7)))

    open_variant['Modded'] = '1'
    open_variant['Notes'] = f"Open mount variant of {base_turret['Turret_ID']}, minimal armor, lighter and faster. Generated variant."

    new_turrets.append(open_variant)
    next_id += 1

    print(f"[{len(new_turrets):3d}] ID {open_variant['Turret_ID']:4s} | {caliber:.1f}\" Open Mount | Weight={open_variant['Turret_Weight_Tons']}T, Armor=0.25\"")

open_count = len(new_turrets) - open_count_start
print(f"\nGenerated {open_count} Open Mount variants")
print()

# 4. Generate Armored variants (for guns that had open mounts)
print("PHASE 4: ARMORED MOUNT VARIANTS")
print("-" * 80)

armored_count_start = len(new_turrets)

# Find existing open mounts and create armored versions
for base_turret in existing_turrets:
    caliber = parse_caliber_num(base_turret['Designation'])
    if not caliber or not (3.0 <= caliber <= 5.0):
        continue

    designation = base_turret['Designation']

    # If it's an open mount, create armored version
    if 'Open' in designation or 'Pedestal' in designation:
        # Skip if very heavy (already armored)
        base_weight = float(base_turret['Turret_Weight_Tons'])
        if base_weight > 40:
            continue

        armored_variant = base_turret.copy()
        armored_variant['Turret_ID'] = str(next_id)
        armored_variant['Designation'] = designation.replace('Open', 'Enclosed').replace('Pedestal', 'Enclosed')

        # Armored modifications
        # Proper armor (caliber-based)
        if caliber >= 5:
            face_armor = 2.0
        elif caliber >= 4:
            face_armor = 1.5
        else:
            face_armor = 1.0

        armored_variant['Armor_Face_IN'] = str(face_armor)
        armored_variant['Armor_Sides_IN'] = str(round(face_armor * 0.6, 1))
        armored_variant['Armor_Roof_IN'] = str(round(face_armor * 0.4, 1))

        # Heavier
        armored_variant['Turret_Weight_Tons'] = str(round(base_weight * 1.7, 1))

        # Slower traverse
        base_traverse = float(base_turret['Traverse_Rate_Deg_Sec'])
        armored_variant['Traverse_Rate_Deg_Sec'] = str(round(base_traverse * 0.7, 1))

        # Slower elevation
        base_elev_rate = float(base_turret['Elevation_Rate_Deg_Sec'])
        armored_variant['Elevation_Rate_Deg_Sec'] = str(round(base_elev_rate * 0.7, 1))

        # More crew (enclosed turret)
        base_crew = int(base_turret['Crew_Size'])
        armored_variant['Crew_Size'] = str(int(base_crew * 1.3))

        armored_variant['Modded'] = '1'
        armored_variant['Notes'] = f"Enclosed armored variant of {base_turret['Turret_ID']}, crew protection, heavier. Generated variant."

        new_turrets.append(armored_variant)
        next_id += 1

        print(f"[{len(new_turrets):3d}] ID {armored_variant['Turret_ID']:4s} | {caliber:.1f}\" Armored | Weight={armored_variant['Turret_Weight_Tons']}T, Armor={face_armor}\"")

armored_count = len(new_turrets) - armored_count_start
print(f"\nGenerated {armored_count} Armored variants")
print()

print("=" * 80)
print(f"Total new variants generated: {len(new_turrets)}")
print("=" * 80)
print()

# Insert new turrets into database
print("Inserting new turret variants into database...")

# Find insertion point (just before compatibility table)
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

print(f"[SUCCESS] Added {len(new_turrets)} turret variants to naval_guns_database.md")
print("=" * 80)

print("\nSUMMARY BY TYPE:")
dp_count = sp_count_start
print(f"  Dual Purpose (DP):   {dp_count:3d} variants")
print(f"  Single Purpose (SP): {sp_count:3d} variants")
print(f"  Open Mount:          {open_count:3d} variants")
print(f"  Armored/Enclosed:    {armored_count:3d} variants")
print(f"  TOTAL:               {len(new_turrets):3d} variants")
print()
print("All variants marked as Modded=1")
print("Next step: Generate compatibility for new variants")
