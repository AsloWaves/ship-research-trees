import sqlite3
import csv
import re

# Connect to database
conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

# Country name mapping
country_mapping = {
    'British': 'Britain',
    'US': 'USA',
    'German': 'Germany',
    'Italian': 'Italy',
    'Japanese': 'Japan',
    'Soviet': 'Russia',
    'French': 'France'
}

# Read CSV and import ammunition
with open('D:/Research/Complete_Shell_Specifications_Database.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    imported = 0
    skipped = 0

    for row in reader:
        # Parse caliber from the Caliber column (e.g., '16.5" SK C/34 AP' -> 16.5)
        caliber_str = row['Caliber']
        caliber_match = re.match(r'^(\d+\.?\d*)"', caliber_str)

        if not caliber_match:
            print(f"Skipping - couldn't parse caliber: {caliber_str}")
            skipped += 1
            continue

        caliber_inches = float(caliber_match.group(1))

        # Map nation name
        nation = row['Nation']
        mapped_nation = country_mapping.get(nation, nation)

        # Extract other fields
        shell_type = row['Type']
        mark = row['Mark_Designation']
        weight_lbs = float(row['Weight_lbs']) if row['Weight_lbs'] else None
        ke_mj = float(row['KE_MJ']) if row['KE_MJ'] else None
        explosive_lbs = float(row['Burster_lbs']) if row['Burster_lbs'] else None
        velocity_fps = int(row['Velocity_fps']) if row['Velocity_fps'] else None
        special_features = row.get('Special_Features', '')

        # Find matching gun(s) by caliber and country
        # Allow for small caliber differences (within 0.2 inches)
        cursor.execute("""
            SELECT gun_id, designation, caliber_inches
            FROM guns
            WHERE country = ?
            AND ABS(caliber_inches - ?) < 0.3
            ORDER BY ABS(caliber_inches - ?)
            LIMIT 1
        """, (mapped_nation, caliber_inches, caliber_inches))

        gun_match = cursor.fetchone()

        if gun_match:
            gun_id = gun_match[0]

            # Insert ammunition
            cursor.execute("""
                INSERT INTO ammunition
                (gun_id, shell_type, weight_lbs, kinetic_megajoules, explosive_lbs, max_range_yards, country)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (gun_id, f"{mark} {shell_type}", weight_lbs, ke_mj, explosive_lbs, velocity_fps, mapped_nation))

            imported += 1
            print(f"[OK] Imported {caliber_inches}\" {mark} {shell_type} ({mapped_nation}) -> Gun ID {gun_id} ({gun_match[1]})")
        else:
            print(f"[SKIP] No matching gun found for {caliber_inches}\" {shell_type} ({mapped_nation})")
            skipped += 1

conn.commit()
conn.close()

print(f"\n=== Import Summary ===")
print(f"Imported: {imported}")
print(f"Skipped: {skipped}")
print(f"Total: {imported + skipped}")
