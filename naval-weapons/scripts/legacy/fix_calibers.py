import sqlite3
import re

conn = sqlite3.connect('D:/Research/naval_weapons.db')
cursor = conn.cursor()

# Get all guns where designation contains " cm" and has inches in parentheses
cursor.execute("""
    SELECT gun_id, designation, caliber_inches
    FROM guns
    WHERE designation LIKE '% cm%'
    ORDER BY gun_id
""")

guns = cursor.fetchall()
updated = 0
skipped = 0

for gun_id, designation, current_caliber in guns:
    # Try to extract inches from designation like "15.5 cm/60 (6.1")"
    # Pattern: look for number in parentheses followed by "
    inch_match = re.search(r'\((\d+\.?\d*)"', designation)

    if inch_match:
        correct_caliber = float(inch_match.group(1))

        # Only update if the current caliber is wrong (stored as cm)
        if abs(current_caliber - correct_caliber) > 0.5:
            cursor.execute("""
                UPDATE guns
                SET caliber_inches = ?
                WHERE gun_id = ?
            """, (correct_caliber, gun_id))

            print(f"[FIX] Gun {gun_id}: {designation}")
            print(f"      {current_caliber}\" -> {correct_caliber}\"")
            updated += 1
        else:
            skipped += 1
    else:
        print(f"[SKIP] Gun {gun_id}: Could not extract caliber from: {designation}")
        skipped += 1

conn.commit()
conn.close()

print(f"\n=== Summary ===")
print(f"Updated: {updated}")
print(f"Skipped: {skipped}")
print(f"Total: {updated + skipped}")
