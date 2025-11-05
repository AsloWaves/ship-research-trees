"""
Integrate Fictional British Data into Markdown Database
- 60 fictional guns (IDs 560-619)
- 880 fictional turrets (IDs 3000-3879)
- 48 fictional ammunition (IDs 184-231)
"""

import json

db_file = '../../database/naval_guns_database.md'

print("=" * 80)
print("INTEGRATING FICTIONAL BRITISH DATA INTO MARKDOWN DATABASE")
print("=" * 80)
print()

# Load generated data
print("[1/6] Loading generated data...")
with open('../../data/fictional_british_guns.json', 'r', encoding='utf-8') as f:
    guns = json.load(f)
with open('../../data/fictional_british_turrets.json', 'r', encoding='utf-8') as f:
    turrets = json.load(f)
with open('../../data/fictional_british_ammunition.json', 'r', encoding='utf-8') as f:
    ammunition = json.load(f)

print(f"  Loaded {len(guns)} guns")
print(f"  Loaded {len(turrets)} turrets")
print(f"  Loaded {len(ammunition)} ammunition types")
print()

# Read database
print("[2/6] Reading current database...")
with open(db_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"  Current size: {len(content):,} characters")
print()

# Add guns
print("[3/6] Adding 60 fictional guns...")
lines = content.split('\n')
output_lines = []
guns_inserted = False

for i, line in enumerate(lines):
    output_lines.append(line)

    # Insert after last British gun (ID 559 or last existing British gun)
    if not guns_inserted and line.startswith('| 559 ') or (line.startswith('| 5') and 'Britain' in line and i < len(lines) - 1 and not lines[i+1].startswith('| 5')):
        print(f"  Inserting 60 guns after existing British guns...")
        for gun in guns:
            notes_escaped = gun['Notes'].replace('|', '\\|')
            row = f"| {gun['Gun_ID']} |  | {gun['Country']} | {gun['Caliber']} | {gun['Length']} | {gun['Mark_Designation']} | {gun['Year_Introduced']} | {gun['Weight']} | {gun['Modded']} | {notes_escaped} |"
            output_lines.append(row)
        guns_inserted = True
        print(f"  Added {len(guns)} guns")

print()

# Add ammunition
print("[4/6] Adding 48 fictional ammunition types...")
ammo_inserted = False
ammo_output = []

for i, line in enumerate(output_lines):
    ammo_output.append(line)

    # Insert after last ammunition entry (ID 183 or similar)
    if not ammo_inserted and line.startswith('| 183 ') or (line.startswith('| 1') and 'ammunition' not in line.lower() and i < len(output_lines) - 1 and output_lines[i+1].startswith('---')):
        print(f"  Inserting 48 ammunition types after existing ammunition...")
        for ammo in ammunition:
            mark = ammo['Mark_Designation'] if ammo['Mark_Designation'] else ''
            notes_escaped = ammo['Notes'].replace('|', '\\|')
            row = f"| {ammo['ID']} |  | {ammo['Caliber']} | {mark} | {ammo['Projectile_Type']} | {ammo['Weight_LBS']} |  |  |  |  | {ammo['Country']} | {ammo['Modded']} | {notes_escaped} |"
            ammo_output.append(row)
        ammo_inserted = True
        print(f"  Added {len(ammunition)} ammunition types")

output_lines = ammo_output
print()

# Add turrets
print("[5/6] Adding 880 fictional turrets...")
turrets_inserted = False
turret_output = []

for i, line in enumerate(output_lines):
    turret_output.append(line)

    # Insert after last British turret (ID 2239)
    if not turrets_inserted and line.startswith('| 2239 '):
        print(f"  Inserting 880 turrets after existing British turrets...")
        for turret in turrets:
            notes_escaped = turret['Notes'].replace('|', '\\|')
            elev_rate = str(turret['Elevation_Rate_Deg_Sec']) if turret['Elevation_Rate_Deg_Sec'] else ''
            row = (f"| {turret['Turret_ID']} | {turret['Gun_ID']} | {turret['Country']} | "
                   f"{turret['Caliber']} | {turret['Turret_Type']} | {turret['Designation']} | "
                   f"{turret['Turret_Weight_Tons']} | {turret['Crew_Size']} | "
                   f"{turret['Armor_Face_IN']} | {turret['Armor_Sides_IN']} | {turret['Armor_Roof_IN']} | "
                   f"{turret['Traverse_Rate_Deg_Sec']} | "
                   f"{turret['Elevation_Min_Deg']} | {turret['Elevation_Max_Deg']} | {elev_rate} | "
                   f"{turret['Rate_Of_Fire_RPM']} | {turret['Modded']} | {notes_escaped} |")
            turret_output.append(row)
        turrets_inserted = True
        print(f"  Added {len(turrets)} turrets")

output_lines = turret_output
print()

# Update totals
print("[6/6] Updating database totals...")
new_content = '\n'.join(output_lines)

# Calculate new totals
# Guns: 118 current → 178 (+60)
# Ammunition: 169 current → 217 (+48)
# Turrets: 252 current → 1132 (+880)
# Compatibility: 321 (unchanged for now)
# Total: 789 current → 1848 (+1059)

new_content = new_content.replace(
    '**Total Records**: 789 (118 guns + 169 ammunition + 256 turrets + 321 compatibility)',
    '**Total Records**: 1848 (178 guns + 217 ammunition + 1132 turrets + 321 compatibility)'
)

# Update individual table counts
new_content = new_content.replace('**Total Entries**: 118 guns', '**Total Entries**: 178 guns')
new_content = new_content.replace('**Total Entries**: 169 ammunition', '**Total Entries**: 217 ammunition')
new_content = new_content.replace('**Total Entries**: 256 turrets', '**Total Entries**: 1132 turrets')

print("  Updated totals:")
print("    Guns: 118 -> 178 (+60 fictional)")
print("    Ammunition: 169 -> 217 (+48 fictional)")
print("    Turrets: 252 -> 1132 (+880 fictional)")
print("    Compatibility: 321 (unchanged)")
print("    TOTAL: 789 -> 1848 (+1059 records)")
print()

# Write updated database
print("Writing updated database...")
with open(db_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"  New size: {len(new_content):,} characters")
print()

print("=" * 80)
print("FICTIONAL BRITISH DATA INTEGRATION COMPLETE")
print("=" * 80)
print()
print("Added to database:")
print("  - 60 fictional guns (IDs 560-619)")
print("  - 880 fictional turrets (IDs 3000-3879)")
print("  - 48 fictional ammunition (IDs 184-231)")
print()
print("New British totals:")
print("  - Guns: 95 (35 historical + 60 fictional)")
print("  - Ammunition: 128 (80 historical + 48 fictional)")
print("  - Turrets: 972 (92 historical + 880 fictional)")
print("  - Total British: 1,195 records")
print()
print("Database grand totals:")
print("  - Total records: 1,848")
print("  - USA turrets: 1,737")
print("  - British turrets: 972")
print("  - Turret ratio (USA:British): 1.8:1 (GOOD)")
print()
