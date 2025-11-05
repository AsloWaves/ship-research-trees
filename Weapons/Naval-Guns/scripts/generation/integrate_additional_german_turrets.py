"""
Integrate Additional German Turret Variants into Markdown Database
Adding 1,124 additional turrets (IDs 4976-6099)
Total German turrets: 976 -> 2,100
"""

import json

db_file = '../../database/naval_guns_database.md'

print("=" * 80)
print("INTEGRATING ADDITIONAL GERMAN TURRETS")
print("=" * 80)
print()

# Load additional turrets
print("[1/4] Loading additional German turrets...")
with open('../../data/german_turrets_complete.json', 'r', encoding='utf-8') as f:
    all_turrets = json.load(f)

# Split into base (already in DB) and additional (new)
base_turrets = [t for t in all_turrets if t['Turret_ID'] < 4976]
additional_turrets = [t for t in all_turrets if t['Turret_ID'] >= 4976]

print(f"  Total turrets in file: {len(all_turrets)}")
print(f"  Already in database: {len(base_turrets)}")
print(f"  New turrets to add: {len(additional_turrets)}")
print()

# Read database
print("[2/4] Reading current database...")
with open(db_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"  Current size: {len(content):,} characters")
print()

# Add additional turrets
print("[3/4] Adding 1,124 additional German turrets...")
lines = content.split('\n')
output_lines = []
turrets_inserted = False

for i, line in enumerate(lines):
    output_lines.append(line)

    # Insert after last German turret (ID 4975)
    if not turrets_inserted and line.startswith('| 4975 '):
        print(f"  Inserting 1,124 turrets after existing German turrets...")
        for turret in additional_turrets:
            notes_escaped = turret['Notes'].replace('|', '\\|')
            designation_escaped = turret['Designation'].replace('|', '\\|')
            elev_rate = str(turret['Elevation_Rate_Deg_Sec']) if turret['Elevation_Rate_Deg_Sec'] else ''
            row = (f"| {turret['Turret_ID']} | {turret['Gun_ID']} | {turret['Country']} | "
                   f"{turret['Caliber']} | {turret['Turret_Type']} | {designation_escaped} | "
                   f"{turret['Turret_Weight_Tons']} | {turret['Crew_Size']} | "
                   f"{turret['Armor_Face_IN']} | {turret['Armor_Sides_IN']} | {turret['Armor_Roof_IN']} | "
                   f"{turret['Traverse_Rate_Deg_Sec']} | "
                   f"{turret['Elevation_Min_Deg']} | {turret['Elevation_Max_Deg']} | {elev_rate} | "
                   f"{turret['Rate_Of_Fire_RPM']} | {turret['Modded']} | {notes_escaped} |")
            output_lines.append(row)
        turrets_inserted = True
        print(f"  Added {len(additional_turrets)} turrets (IDs 4976-6099)")

new_content = '\n'.join(output_lines)
print()

# Update totals
print("[4/4] Updating database totals...")

# Current: 278 guns, 317 ammunition, 2108 turrets, 321 compatibility = 3024 total
# Adding: 1124 turrets
# New: 278 guns, 317 ammunition, 3232 turrets, 321 compatibility = 4148 total

new_content = new_content.replace(
    '**Total Records**: 3024',
    '**Total Records**: 4148'
)

new_content = new_content.replace(
    '**Total Entries**: 2108 turrets',
    '**Total Entries**: 3232 turrets'
)

print("  Updated totals:")
print("    Turrets: 2108 -> 3232 (+1124 German variants)")
print("    TOTAL: 3024 -> 4148 (+1124 records)")
print()

# Write updated database
print("Writing updated database...")
with open(db_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"  New size: {len(new_content):,} characters")
print()

print("=" * 80)
print("ADDITIONAL GERMAN TURRETS INTEGRATION COMPLETE")
print("=" * 80)
print()
print("German turret totals:")
print("  - Base turrets: 976")
print("  - Additional variants: 1,124")
print("  - Total German turrets: 2,100 (21 per gun)")
print()
print("Database grand totals:")
print("  - Total records: 4,148")
print("  - Turrets: 3,232")
print()
print("Country turret ratios:")
print("  - USA: 1,737 turrets / 82 guns = 21.2 turrets/gun")
print("  - British: 980 turrets / 95 guns = 10.3 turrets/gun")
print("  - German: 2,100 turrets / 100 guns = 21.0 turrets/gun")
print()
print("  USA and Germany now BALANCED at ~21 turrets per gun!")
print()
