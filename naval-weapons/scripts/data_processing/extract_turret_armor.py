#!/usr/bin/env python3
"""
Extract Turret Armor data from research file and generate SQL updates
"""

import re
import sqlite3

# Read research file
with open('D:\\Research\\USA_Naval_Weapons_Research.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Connect to database
conn = sqlite3.connect('D:\\Research\\naval_guns.db')
cursor = conn.cursor()
cursor.execute("SELECT Turret_ID, Designation FROM Turrets WHERE Turret_ID >= 21 ORDER BY Turret_ID")
turrets_in_db = cursor.fetchall()
conn.close()

# Extract turret data from research file
turret_research = []
in_turret_table = False

for i, line in enumerate(lines):
    if '### Turrets Table Data' in line:
        in_turret_table = True
        continue

    if in_turret_table and line.startswith('|') and not line.startswith('|---'):
        parts = [p.strip() for p in line.split('|')[1:-1]]

        # Skip header row and invalid rows
        if (len(parts) >= 15 and parts[0] and
            parts[0] != 'Country' and
            parts[0] != '*NO TURRET DATA*'):

            designation = parts[2]  # Column 2 is Designation
            armor_face = parts[4]   # Column 4 is Armor_Face_IN
            armor_sides = parts[5]  # Column 5 is Armor_Sides_IN
            armor_roof = parts[6]   # Column 6 is Armor_Roof_IN
            turret_weight = parts[3] # Column 3 is Turret_Weight_Tons

            # Only keep if we have valid armor data
            if armor_face not in ['🔍', '-', ''] or armor_sides not in ['🔍', '-', ''] or armor_roof not in ['🔍', '-', '']:
                turret_research.append({
                    'designation': designation,
                    'armor_face': armor_face if armor_face not in ['🔍', '-', ''] else None,
                    'armor_sides': armor_sides if armor_sides not in ['🔍', '-', ''] else None,
                    'armor_roof': armor_roof if armor_roof not in ['🔍', '-', ''] else None,
                    'weight': turret_weight if turret_weight not in ['🔍', '-', ''] else None
                })

    if in_turret_table and (line.startswith('**') or line.startswith('###') or (line.startswith('---') and not line.startswith('|---'))):
        in_turret_table = False

print(f"Found {len(turret_research)} turret entries with armor data in research file")

# Generate SQL updates
sql_updates = []
sql_updates.append('-- Update Turret Armor data from research file')
sql_updates.append('BEGIN TRANSACTION;')
sql_updates.append('')

matched = 0
updates = []

for turret_id, db_designation in turrets_in_db:
    matched_entry = None

    # Try to match by designation
    for entry in turret_research:
        # Normalize designations for comparison
        research_desig_normalized = entry['designation'].replace('  ', ' ').strip()
        db_desig_normalized = db_designation.replace('  ', ' ').strip()

        if research_desig_normalized == db_desig_normalized:
            matched_entry = entry
            break

    if matched_entry:
        update_fields = []
        if matched_entry['armor_face']:
            try:
                armor_face = float(matched_entry['armor_face'])
                update_fields.append(f"Armor_Face_IN = {armor_face}")
            except:
                pass

        if matched_entry['armor_sides']:
            try:
                armor_sides = float(matched_entry['armor_sides'])
                update_fields.append(f"Armor_Sides_IN = {armor_sides}")
            except:
                pass

        if matched_entry['armor_roof']:
            try:
                armor_roof = float(matched_entry['armor_roof'])
                update_fields.append(f"Armor_Roof_IN = {armor_roof}")
            except:
                pass

        if matched_entry['weight']:
            try:
                weight = float(matched_entry['weight'])
                update_fields.append(f"Turret_Weight_Tons = {weight}")
            except:
                pass

        if update_fields:
            sql_updates.append(f"UPDATE Turrets SET {', '.join(update_fields)} WHERE Turret_ID = {turret_id}; -- {db_designation}")
            matched += 1

sql_updates.append('')
sql_updates.append('COMMIT;')

print(f"Matched {matched}/{len(turrets_in_db)} turret entries")

# Write SQL file
with open('D:\\Research\\fix_turret_armor.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_updates))

print(f"Generated fix_turret_armor.sql")
