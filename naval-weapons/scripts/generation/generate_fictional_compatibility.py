"""
Generate compatibility entries for fictional turrets
Links fictional turrets to the same ammunition as their base guns
"""

import re

# Read database
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find compatibility section
compat_start = None
compat_end = None
for i, line in enumerate(lines):
    if '## Gun Ammunition Compatibility' in line:
        compat_start = i
    elif compat_start and '## Data Completeness' in line:
        compat_end = i
        break

# Parse existing compatibility entries
compat_header_idx = None
for i in range(compat_start, compat_end):
    if lines[i].strip().startswith('|') and 'Compatibility_ID' in lines[i]:
        compat_header_idx = i
        break

compat_header = [col.strip() for col in lines[compat_header_idx].split('|')[1:-1]]
compat_data_start = compat_header_idx + 2

# Parse existing compatibility data
gun_ammo_map = {}  # gun_id -> list of ammo entries
max_compat_id = 0

for i in range(compat_data_start, compat_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(compat_header):
        continue

    compat_data = dict(zip(compat_header, cols))
    compat_id = int(compat_data['Compatibility_ID'])
    gun_id = compat_data['Gun_ID']

    max_compat_id = max(max_compat_id, compat_id)

    if gun_id not in gun_ammo_map:
        gun_ammo_map[gun_id] = []
    gun_ammo_map[gun_id].append(compat_data)

print(f"Found {len(gun_ammo_map)} guns with compatibility data")
print(f"Max compatibility ID: {max_compat_id}")
print()

# Find turrets section to get fictional turrets
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

# Parse fictional turrets (Modded=1)
fictional_turrets = []

for i in range(turrets_data_start, turrets_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(turrets_header):
        continue

    turret_data = dict(zip(turrets_header, cols))

    if turret_data['Modded'] == '1':
        fictional_turrets.append({
            'turret_id': turret_data['Turret_ID'],
            'gun_id': turret_data['Gun_ID'],
            'designation': turret_data['Designation']
        })

print(f"Found {len(fictional_turrets)} fictional turrets")
print()

# Generate compatibility entries for fictional turrets
new_compat_entries = []
next_compat_id = max_compat_id + 1

print("=" * 80)
print("GENERATING COMPATIBILITY ENTRIES FOR FICTIONAL TURRETS")
print("=" * 80)
print()

for turret in fictional_turrets:
    gun_id = turret['gun_id']
    turret_id = turret['turret_id']

    # Get ammunition entries for this gun
    if gun_id in gun_ammo_map:
        ammo_entries = gun_ammo_map[gun_id]

        # Create compatibility entry for each ammunition type
        for ammo_entry in ammo_entries:
            new_entry = {
                'Compatibility_ID': str(next_compat_id),
                'Gun_ID': gun_id,
                'Ammunition_ID': ammo_entry['Ammunition_ID'],
                'Notes': f"Fictional turret {turret_id} compatibility",
                'Caliber': ammo_entry['Caliber'],
                'Muzzle_Velocity_FPS': ammo_entry['Muzzle_Velocity_FPS'],
                'Muzzle_Velocity_MPS': ammo_entry['Muzzle_Velocity_MPS'],
                'Max_Range_Yards': ammo_entry['Max_Range_Yards'],
                'Barrel_Wear_Per_Round': ammo_entry['Barrel_Wear_Per_Round']
            }

            new_compat_entries.append(new_entry)
            next_compat_id += 1

        print(f"[{len(new_compat_entries):4d}] Turret {turret_id:4s} | Gun {gun_id:3s} | {len(ammo_entries)} ammunition types")
    else:
        print(f"WARNING: Gun {gun_id} has no ammunition compatibility data")

print()
print("=" * 80)
print(f"Generated {len(new_compat_entries)} compatibility entries")
print("=" * 80)
print()

# Insert new compatibility entries into database
print("Inserting new compatibility entries into database...")

# Find insertion point (just before Data Completeness section)
insert_point = compat_end - 1

# Format new compatibility rows
new_lines = []
for entry in new_compat_entries:
    row = '| ' + ' | '.join([entry[col] for col in compat_header]) + ' |\n'
    new_lines.append(row)

# Insert into lines
lines = lines[:insert_point] + new_lines + lines[insert_point:]

# Write back to file
with open('naval_guns_database.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"[SUCCESS] Added {len(new_compat_entries)} compatibility entries to naval_guns_database.md")
print("=" * 80)

# Summary
print("\nSUMMARY:")
print(f"  - Fictional turrets processed: {len(fictional_turrets)}")
print(f"  - New compatibility entries: {len(new_compat_entries)}")
print(f"  - Average ammunition types per gun: {len(new_compat_entries) / len(fictional_turrets) if fictional_turrets else 0:.1f}")
print()
print("Next step: Verify with analyze_completeness.py")
