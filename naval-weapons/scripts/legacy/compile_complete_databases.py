import csv
import shutil

print("Compiling complete databases for import...")

# ============================================================================
# 1. COMPILE COMPLETE SHELL SPECIFICATIONS DATABASE
# ============================================================================

print("\n1. Compiling Complete Shell Specifications Database...")

# Read existing shells
existing_shells = []
with open('D:/Research/Shell_Specifications_Updated.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    for row in reader:
        existing_shells.append(row)

print(f"   - Existing shells: {len(existing_shells)}")

# Read fake shells
fake_shells = []
with open('D:/Research/Fake_Shells_To_Import.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        fake_shells.append(row)

print(f"   - Fake shells to add: {len(fake_shells)}")

# Combine all shells
all_shells = existing_shells + fake_shells

# Write complete shell database
complete_shell_file = 'D:/Research/Complete_Shell_Specifications_Database.csv'
with open(complete_shell_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(all_shells)

print(f"   - Complete shell database: {len(all_shells)} total shells")
print(f"   - Saved to: {complete_shell_file}")

# ============================================================================
# 2. COMPILE COMPLETE GUN VARIANTS DATABASE
# ============================================================================

print("\n2. Compiling Complete Gun Variants Database...")

# The Gun_Variants_With_URLs.csv already has the complete gun database with URLs
# Just copy it to a clearly named file

gun_source = 'D:/Research/Gun_Variants_With_URLs.csv'
gun_destination = 'D:/Research/Complete_Gun_Variants_Database.csv'

shutil.copy2(gun_source, gun_destination)

# Count guns
gun_count = 0
with open(gun_destination, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        gun_count += 1

print(f"   - Complete gun database: {gun_count} total gun variants")
print(f"   - Saved to: {gun_destination}")

# ============================================================================
# 3. GENERATE IMPORT SUMMARY
# ============================================================================

print("\n3. Generating Import Summary...")

# Analyze shell database composition
real_shells = len(existing_shells)
fake_shells_count = len(fake_shells)
total_shells = len(all_shells)

# Analyze gun database
guns_with_shells = 0
guns_without_shells = 0

with open(gun_destination, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '').strip()
        if compatible_shells:
            guns_with_shells += 1
        else:
            guns_without_shells += 1

# Count shells with URLs vs without
shells_with_urls = 0
shells_without_urls = 0

for shell in all_shells:
    caliber = shell.get('Caliber', '')
    # Check if this shell appears in gun references with URL
    # For now, assume fake shells won't have URLs initially
    if '*' in caliber:
        shells_without_urls += 1
    else:
        shells_with_urls += 1  # Most real shells should have URLs from our earlier work

# Create summary report
summary_file = 'D:/Research/Database_Import_Summary.txt'
with open(summary_file, 'w', encoding='utf-8') as f:
    f.write("DATABASE IMPORT SUMMARY\n")
    f.write("=" * 50 + "\n\n")

    f.write("SHELL SPECIFICATIONS DATABASE:\n")
    f.write("-" * 30 + "\n")
    f.write(f"Real shells (existing):     {real_shells:3d}\n")
    f.write(f"Fake shells (created):      {fake_shells_count:3d}\n")
    f.write(f"Total shells:               {total_shells:3d}\n")
    f.write(f"File: Complete_Shell_Specifications_Database.csv\n\n")

    f.write("GUN VARIANTS DATABASE:\n")
    f.write("-" * 30 + "\n")
    f.write(f"Total gun variants:         {gun_count:3d}\n")
    f.write(f"Guns with shell links:      {guns_with_shells:3d}\n")
    f.write(f"Guns without shell links:   {guns_without_shells:3d}\n")
    f.write(f"File: Complete_Gun_Variants_Database.csv\n\n")

    f.write("IMPORT INSTRUCTIONS:\n")
    f.write("-" * 30 + "\n")
    f.write("1. Import Complete_Shell_Specifications_Database.csv into Shell Specifications\n")
    f.write("2. Import Complete_Gun_Variants_Database.csv into Gun Variants\n")
    f.write("3. All fake shells are marked with * in their names\n")
    f.write("4. Gun variants have proper shell links with URLs where available\n")
    f.write("5. Nation-specific compatibility enforced throughout\n\n")

    f.write("POST-IMPORT VERIFICATION:\n")
    f.write("-" * 30 + "\n")
    f.write("- Verify all gun variants have compatible shells listed\n")
    f.write("- Check that shell links work properly in Notion\n")
    f.write("- Confirm fake shells are properly marked with *\n")
    f.write("- Test nation-specific compatibility (no cross-nation shells)\n")

print(f"   - Import summary saved to: {summary_file}")

# ============================================================================
# 4. FINAL STATISTICS
# ============================================================================

print(f"\n" + "=" * 60)
print(f"COMPILATION COMPLETE!")
print(f"=" * 60)
print(f"")
print(f"📊 SHELL DATABASE:")
print(f"   Real shells:     {real_shells:3d}")
print(f"   Fake shells:     {fake_shells_count:3d}")
print(f"   Total shells:    {total_shells:3d}")
print(f"")
print(f"🔫 GUN DATABASE:")
print(f"   Total guns:      {gun_count:3d}")
print(f"   With shells:     {guns_with_shells:3d}")
print(f"   Without shells:  {guns_without_shells:3d}")
print(f"")
print(f"📁 FILES READY FOR IMPORT:")
print(f"   1. Complete_Shell_Specifications_Database.csv")
print(f"   2. Complete_Gun_Variants_Database.csv")
print(f"   3. Database_Import_Summary.txt")
print(f"")
print(f"🎯 IMPORT ORDER: Import shells first, then guns!")

# Show examples of fake shells
print(f"\nExample fake shells created:")
fake_examples = 0
for shell in all_shells:
    if '*' in shell.get('Caliber', '') and fake_examples < 5:
        caliber = shell.get('Caliber', '')
        nation = shell.get('Nation', '')
        print(f"   - {caliber} ({nation})")
        fake_examples += 1