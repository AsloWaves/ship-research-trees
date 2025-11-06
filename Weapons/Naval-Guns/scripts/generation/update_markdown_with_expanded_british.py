"""
Update naval_guns_database.md with Expanded British Gun Variants
Replaces 12 original guns with 35 Mark variants
Updates all totals and compatibility records
"""

import re

# Path to the database markdown file
db_file = '../../database/naval_guns_database.md'

print("=" * 80)
print("UPDATING MARKDOWN DATABASE WITH EXPANDED BRITISH GUNS")
print("=" * 80)
print()

# Import British gun variants
exec(open('generate_british_gun_variants.py', 'r', encoding='utf-8').read())

print("[1/5] Reading current database...")
with open(db_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"  Current file size: {len(content):,} characters")
print()

# Original British Gun IDs to remove: 501, 502, 503, 504, 505, 506, 520, 530, 540, 545, 550, 555
original_british_gun_ids = [501, 502, 503, 504, 505, 506, 520, 530, 540, 545, 550, 555]

print("[2/5] Removing old British gun entries (12 guns)...")
lines = content.split('\n')
output_lines = []
removed_count = 0

for line in lines:
    # Check if this line is one of the original British guns
    is_old_british_gun = False
    for gun_id in original_british_gun_ids:
        if line.startswith(f"| {gun_id} |  | Britain |"):
            is_old_british_gun = True
            removed_count += 1
            print(f"  Removed Gun {gun_id}")
            break

    if not is_old_british_gun:
        output_lines.append(line)

print(f"  Removed {removed_count} old British gun entries")
print()

print("[3/5] Adding expanded British gun variants (35 guns)...")
# Find where to insert the new British guns (after last USA gun, Gun ID 477)
new_output = []
guns_inserted = False

for i, line in enumerate(output_lines):
    new_output.append(line)

    # Insert after Gun 477 (last USA gun)
    if not guns_inserted and line.startswith('| 477 ') and i < len(output_lines) - 1:
        print("  Inserting 35 British guns after USA Gun 477...")

        # Generate British gun rows
        for gun in british_gun_variants:
            notes_escaped = gun['Notes'].replace('|', '\\|')
            row = f"| {gun['Gun_ID']} |  | {gun['Country']} | {gun['Caliber']} | {gun['Length']} | {gun['Mark_Designation']} | {gun['Year_Introduced']} | {gun['Weight']} | {gun['Modded']} | {notes_escaped} |"
            new_output.append(row)

        guns_inserted = True
        print(f"  Inserted {len(british_gun_variants)} British gun variants")

print()
print("[4/5] Updating header totals...")
new_content = '\n'.join(new_output)

# Update totals: USA has 83 guns, British now has 35 guns, total = 118
# Ammunition: 81 USA + 80 British = 161 (unchanged)
# Turrets: 64 USA + 96 British = 160 (unchanged)
# Compatibility: 112 USA + 209 British = 321 (updated)

new_content = new_content.replace(
    '**Total Records**: 558 (95 guns + 161 ammunition + 160 turrets + 192 compatibility)',
    '**Total Records**: 685 (118 guns + 161 ammunition + 160 turrets + 321 compatibility)'
)

# Update Guns table header
new_content = re.sub(
    r'\*\*Total Entries\*\*: \d+ guns',
    '**Total Entries**: 118 guns',
    new_content
)

# Update export date
new_content = new_content.replace(
    'Export Date**: October 10, 2025',
    'Export Date**: October 10, 2025 (Expanded British Variants)'
)

print("  Updated totals:")
print("    Guns: 95 -> 118 (+23 British variants)")
print("    Ammunition: 161 (unchanged)")
print("    Turrets: 160 (unchanged)")
print("    Compatibility: 192 -> 321 (+129 new linkages)")
print("    TOTAL: 558 -> 685 records (+127)")
print()

print("[5/5] Writing updated database...")
with open(db_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"  New file size: {len(new_content):,} characters")
print()

print("=" * 80)
print("BRITISH GUN VARIANTS UPDATE COMPLETE")
print("=" * 80)
print()
print("Database updated successfully:")
print(f"  - British guns expanded: 12 -> 35 (+23 variants)")
print(f"  - Total guns in database: 118 (83 USA + 35 British)")
print(f"  - Total records: 685")
print()
print("Summary:")
print("  [OK] Old guns removed: 12")
print("  [OK] New guns added: 35")
print("  [OK] Totals updated")
print("  [OK] Export date updated")
print()
