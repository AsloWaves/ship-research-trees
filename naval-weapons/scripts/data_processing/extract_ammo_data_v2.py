#!/usr/bin/env python3
"""
Extract Ammunition Cartridge_Type from research file and generate SQL updates
Version 2: Handle Mark designation variations
"""

import re
import sqlite3

# Read research file
with open('D:\\Research\\USA_Naval_Weapons_Research.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Connect to database
conn = sqlite3.connect('D:\\Research\\naval_guns.db')
cursor = conn.cursor()
cursor.execute("SELECT ID, Caliber, Mark_Designation, Projectile_Type FROM Ammunition WHERE ID >= 12 ORDER BY ID")
ammo_in_db = cursor.fetchall()
conn.close()

# Extract ammunition data from research file
ammo_research = []
in_ammo_table = False

for i, line in enumerate(lines):
    if '### Ammunition Table Data' in line:
        in_ammo_table = True
        continue

    if in_ammo_table and line.startswith('|') and not line.startswith('|---'):
        parts = [p.strip() for p in line.split('|')[1:-1]]

        # Skip header row
        if len(parts) >= 8 and parts[0] and parts[0] != 'Caliber':
            caliber = parts[0]
            mark_designation = parts[1]
            projectile_type = parts[2]
            cartridge_type = parts[7]

            # Only keep if cartridge type is valid
            if cartridge_type in ['Bag', 'Separate', 'Semi-fixed']:
                ammo_research.append({
                    'caliber': caliber,
                    'mark': mark_designation,
                    'projectile': projectile_type,
                    'cartridge': cartridge_type
                })

    if in_ammo_table and (line.startswith('**') or line.startswith('###') or line.startswith('---')):
        in_ammo_table = False

print(f"Found {len(ammo_research)} ammunition entries in research file")

# Generate SQL updates
sql_updates = []
sql_updates.append('-- Update Ammunition Cartridge_Type from research file')
sql_updates.append('BEGIN TRANSACTION;')
sql_updates.append('')

matched = 0
unmatched = []

for ammo_id, db_caliber, db_mark, db_projectile in ammo_in_db:
    matched_entry = None

    # Try exact match first
    for entry in ammo_research:
        if (entry['caliber'] == db_caliber and
            entry['mark'] == db_mark and
            entry['projectile'] == db_projectile):
            matched_entry = entry
            break

    # Try matching without projectile type in mark
    if not matched_entry:
        for entry in ammo_research:
            # Handle cases like "Mark 9 AP" in research vs "Mark 9" in DB
            research_mark_base = entry['mark'].replace(' AP', '').replace(' HC', '').replace(' HE', '').replace(' Common', '')
            if (entry['caliber'] == db_caliber and
                research_mark_base == db_mark and
                entry['projectile'] == db_projectile):
                matched_entry = entry
                break

    if matched_entry:
        sql_updates.append(f"UPDATE Ammunition SET Cartridge_Type = '{matched_entry['cartridge']}' WHERE ID = {ammo_id}; -- {db_caliber} {db_mark} {db_projectile}")
        matched += 1
    else:
        unmatched.append((ammo_id, db_caliber, db_mark, db_projectile))

sql_updates.append('')
sql_updates.append('COMMIT;')

print(f"Matched {matched}/{len(ammo_in_db)} ammunition entries")
print(f"Unmatched: {len(unmatched)}")

if unmatched:
    print("\nUnmatched entries (will need manual research):")
    for ammo_id, cal, mark, proj in unmatched[:10]:
        print(f"  ID {ammo_id}: {cal} {mark} {proj}")

# Write SQL file
with open('D:\\Research\\fix_ammo_cartridge_type.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_updates))

print(f"\nGenerated fix_ammo_cartridge_type.sql")
