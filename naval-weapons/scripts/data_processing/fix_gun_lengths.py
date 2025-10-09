#!/usr/bin/env python3
"""
Fix Gun Length format: Convert absolute inches to /## caliber format
Example: 18" gun with 864" barrel = 864 / 18 = 48 → "/48"
"""

import sqlite3
import re

# Connect to database
conn = sqlite3.connect('D:\\Research\\naval_guns.db')
cursor = conn.cursor()

# Get all guns with absolute length format
cursor.execute("SELECT Gun_ID, Caliber, Length FROM Guns WHERE Gun_ID >= 401")
guns = cursor.fetchall()

sql_updates = []
sql_updates.append('-- Fix Gun Length format: absolute inches → /## caliber')
sql_updates.append('BEGIN TRANSACTION;')
sql_updates.append('')

for gun_id, caliber, length in guns:
    # Extract caliber number (e.g., "18\"" → 18)
    caliber_match = re.match(r'(\d+(?:\.\d+)?)"', caliber)
    if not caliber_match:
        print(f"Warning: Could not parse caliber '{caliber}' for Gun_ID {gun_id}")
        continue

    caliber_num = float(caliber_match.group(1))

    # Extract barrel length (e.g., "864 in" → 864)
    length_match = re.match(r'(\d+(?:\.\d+)?)\s*in', length)
    if not length_match:
        print(f"Warning: Could not parse length '{length}' for Gun_ID {gun_id}")
        continue

    barrel_length = float(length_match.group(1))

    # Calculate caliber length
    caliber_length = int(round(barrel_length / caliber_num))

    # Format as /##
    new_length = f"/{caliber_length}"

    sql_updates.append(f"UPDATE Guns SET Length = '{new_length}' WHERE Gun_ID = {gun_id}; -- {caliber} {barrel_length}\" = /{caliber_length}")

sql_updates.append('')
sql_updates.append('COMMIT;')

# Write SQL file
output_file = 'D:\\Research\\fix_gun_lengths.sql'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(sql_updates))

print(f"Generated {output_file}")
print(f"Total guns to fix: {len([u for u in sql_updates if u.startswith('UPDATE')])}")

conn.close()
