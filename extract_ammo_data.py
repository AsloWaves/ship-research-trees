#!/usr/bin/env python3
"""
Extract Ammunition Cartridge_Type from research file and generate SQL updates
"""

import re
import sqlite3

# Read research file
with open('D:\\Research\\USA_Naval_Weapons_Research.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Connect to database to get current ammunition
conn = sqlite3.connect('D:\\Research\\naval_guns.db')
cursor = conn.cursor()
cursor.execute("SELECT ID, Caliber, Mark_Designation FROM Ammunition WHERE ID >= 12 ORDER BY ID")
ammo_in_db = cursor.fetchall()
conn.close()

# Find all ammunition table sections
ammo_sections = []
lines = content.split('\n')

in_ammo_table = False
table_lines = []

for i, line in enumerate(lines):
    if '### Ammunition Table Data' in line:
        in_ammo_table = True
        table_lines = []
        continue

    if in_ammo_table:
        if line.startswith('|') and not line.startswith('|---'):
            table_lines.append(line)
        elif line.startswith('**') or line.startswith('###') or line.startswith('---'):
            if table_lines:
                ammo_sections.append(table_lines)
            in_ammo_table = False
            table_lines = []

# Parse ammunition data
ammo_data = []
for section in ammo_sections:
    # Skip header row
    for line in section[1:]:
        parts = [p.strip() for p in line.split('|')[1:-1]]
        if len(parts) >= 8 and parts[0] and parts[0] != 'Caliber':
            caliber = parts[0]
            mark = parts[1]
            cartridge_type = parts[7] if len(parts) > 7 else '-'

            # Clean up cartridge type
            if cartridge_type in ['Bag', 'Separate', 'Semi-fixed']:
                ammo_data.append((caliber, mark, cartridge_type))

print(f"Found {len(ammo_data)} ammunition entries with Cartridge_Type")

# Generate SQL updates
sql_updates = []
sql_updates.append('-- Update Ammunition Cartridge_Type from research file')
sql_updates.append('BEGIN TRANSACTION;')
sql_updates.append('')

matched = 0
for ammo_id, db_caliber, db_mark in ammo_in_db:
    # Find matching entry in research data
    for research_cal, research_mark, cart_type in ammo_data:
        if db_caliber == research_cal and db_mark == research_mark:
            sql_updates.append(f"UPDATE Ammunition SET Cartridge_Type = '{cart_type}' WHERE ID = {ammo_id}; -- {db_caliber} {db_mark}")
            matched += 1
            break

sql_updates.append('')
sql_updates.append('COMMIT;')

print(f"Matched {matched} ammunition entries")

# Write SQL file
with open('D:\\Research\\fix_ammo_cartridge_type.sql', 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_updates))

print(f"Generated fix_ammo_cartridge_type.sql")
