"""
Update fictional turret compatibility notes to be more descriptive
Instead of "Fictional turret 56 compatibility", use format like:
"5"/38 Mark 12 DP Turret + Mark 41 AAC shell"
"""

import re

# Read database
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find turrets section to get turret designations
turrets_start = None
turrets_end = None
for i, line in enumerate(lines):
    if '## Turrets Table' in line:
        turrets_start = i
    elif turrets_start and '## Gun Ammunition Compatibility' in line:
        turrets_end = i
        break

# Parse turrets to get ID -> Designation mapping
turrets_header_idx = None
for i in range(turrets_start, turrets_end):
    if lines[i].strip().startswith('|') and 'Turret_ID' in lines[i]:
        turrets_header_idx = i
        break

turrets_header = [col.strip() for col in lines[turrets_header_idx].split('|')[1:-1]]
turrets_data_start = turrets_header_idx + 2

turret_designations = {}
for i in range(turrets_data_start, turrets_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(turrets_header):
        continue

    turret_data = dict(zip(turrets_header, cols))
    turret_id = turret_data['Turret_ID']
    designation = turret_data['Designation']
    turret_designations[turret_id] = designation

print(f"Loaded {len(turret_designations)} turret designations")

# Find ammunition section to get ammo designations
ammo_start = None
ammo_end = None
for i, line in enumerate(lines):
    if '## Ammunition Table' in line:
        ammo_start = i
    elif ammo_start and '## Turrets Table' in line:
        ammo_end = i
        break

# Parse ammunition to get ID -> Designation mapping
ammo_header_idx = None
for i in range(ammo_start, ammo_end):
    if lines[i].strip().startswith('|') and 'ID' in lines[i]:
        ammo_header_idx = i
        break

ammo_header = [col.strip() for col in lines[ammo_header_idx].split('|')[1:-1]]
ammo_data_start = ammo_header_idx + 2

ammo_designations = {}
for i in range(ammo_data_start, ammo_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    # Don't check column count - Notes field may contain pipes
    if len(cols) < 6:  # Need at least first 6 columns
        continue

    # Parse first few columns only (Notes field may have pipes)
    ammo_id = cols[0].strip()  # ID
    # skip Turret_ID (cols[1])
    caliber = cols[2]  # Caliber
    mark = cols[3]  # Mark_Designation
    proj_type = cols[4]  # Projectile_Type

    # Remove caliber prefix from mark if present (e.g., "6" Mark 24" -> "Mark 24")
    mark_clean = re.sub(r'^\d+[./]?\d*"\s+', '', mark)

    # Create short designation
    ammo_designation = f"{mark_clean} {proj_type}"  # Simpler format, caliber already in turret name
    ammo_designations[ammo_id] = ammo_designation

print(f"Loaded {len(ammo_designations)} ammunition designations")
print()

# Find compatibility section
compat_start = None
compat_end = None
for i, line in enumerate(lines):
    if '## Gun Ammunition Compatibility' in line:
        compat_start = i
    elif compat_start and '## Data Completeness' in line:
        compat_end = i
        break

# Parse compatibility entries
compat_header_idx = None
for i in range(compat_start, compat_end):
    if lines[i].strip().startswith('|') and 'Compatibility_ID' in lines[i]:
        compat_header_idx = i
        break

compat_header = [col.strip() for col in lines[compat_header_idx].split('|')[1:-1]]
compat_data_start = compat_header_idx + 2

# Find column indices
notes_idx = compat_header.index('Notes')
gun_id_idx = compat_header.index('Gun_ID')
ammo_id_idx = compat_header.index('Ammunition_ID')

# Update compatibility notes
updates_count = 0
for i in range(compat_data_start, compat_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue

    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(compat_header):
        continue

    notes = cols[notes_idx]
    ammo_id = cols[ammo_id_idx].strip()

    # Check if note contains turret designation + ammunition (fictional turret pattern)
    # Pattern: "Turret Name + Ammunition Name"
    if ' + ' in notes and (
        'Turret' in notes or 'Mount' in notes or 'DP' in notes or 'SP' in notes or 'Open' in notes
    ):
        # Get ammunition designation
        if ammo_id in ammo_designations:
            ammo_desig = ammo_designations[ammo_id]

            # Check if ammo already has the correct format (no caliber prefix)
            # Extract current ammo part from note
            match = re.search(r' \+ (.+)$', notes)
            if match:
                current_ammo = match.group(1)

                # Only update if current ammo has caliber prefix or is placeholder
                if (re.match(r'^\d+[./]?\d*"\s+', current_ammo) or
                    current_ammo.startswith('Ammo ') or
                    current_ammo.startswith('Shell ')):

                    # Replace the ammunition part
                    new_note = re.sub(r' \+ .+$', f' + {ammo_desig}', notes)

                    # Replace the note in the line
                    cols[notes_idx] = new_note
                    new_line = '| ' + ' | '.join(cols) + ' |\n'
                    lines[i] = new_line
                    updates_count += 1

                    if updates_count <= 10:
                        print(f"[{updates_count:4d}] Updated: {notes[:60]:60s} -> {new_note[:70]}")

print()
print("=" * 80)
print(f"Updated {updates_count} compatibility notes")
print("=" * 80)

# Write back to file
with open('naval_guns_database.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print()
print("[SUCCESS] naval_guns_database.md updated with descriptive compatibility notes")
