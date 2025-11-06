import csv
import re
from collections import defaultdict

print("Updating Gun Variants to include fake shells...")

# Nation mapping
NATION_MAP = {
    '🇫🇷 French': 'French',
    '🇩🇪 German': 'German',
    '🇬🇧 British': 'British',
    '🇮🇹 Italian': 'Italian',
    '🇯🇵 Japanese': 'Japanese',
    '🇷🇺 Soviet': 'Soviet',
    '🇺🇸 United States': 'US',
    '🇪🇸 Spain': 'Spain',
    '🇦🇹 Austria-Hungary': 'Austria-Hungary',
    '🇧🇷 Brazil': 'Brazil',
    '🇳🇱 Netherlands': 'Netherlands'
}

def extract_caliber_from_gun(caliber_length):
    """Extract caliber from gun's Caliber_Length field (e.g., '16"/45' -> '16"')"""
    if not caliber_length:
        return None

    # Handle special cases like 2-pounder
    if 'pounder' in caliber_length:
        match = re.match(r'^([0-9.]+-pounder)', caliber_length)
        if match:
            return match.group(1)

    # Extract caliber before the slash for standard format
    match = re.match(r'^"?([0-9.]+)"', caliber_length)
    if match:
        return match.group(1) + '"'

    return None

# Read fake shells and create mapping
print("Reading fake shells...")
fake_shells_by_caliber_nation = defaultdict(list)

with open('D:/Research/Fake_Shells_To_Import.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        caliber_full = row.get('Caliber', '').strip()
        nation = row.get('Nation', '').strip()

        if caliber_full and nation:
            # Extract base caliber
            caliber_match = re.match(r'^([0-9.]+\"|[0-9.]+-pounder)', caliber_full)
            if caliber_match:
                base_caliber = caliber_match.group(1)
                fake_shells_by_caliber_nation[(base_caliber, nation)].append(caliber_full)

print(f"Found {len(fake_shells_by_caliber_nation)} fake shell caliber-nation combinations")

# Read existing shells for completeness
existing_shells_by_caliber_nation = defaultdict(list)

with open('D:/Research/Shell_Specifications_Updated.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        caliber_full = row.get('Caliber', '').strip()
        nation = row.get('Nation', '').strip()

        if caliber_full and nation:
            caliber_match = re.match(r'^([0-9.]+\"|[0-9.]+-pounder)', caliber_full)
            if caliber_match:
                base_caliber = caliber_match.group(1)
                existing_shells_by_caliber_nation[(base_caliber, nation)].append(caliber_full)

print(f"Found {len(existing_shells_by_caliber_nation)} existing shell caliber-nation combinations")

# Combine all shells
all_shells_by_caliber_nation = defaultdict(list)
for key, shells in existing_shells_by_caliber_nation.items():
    all_shells_by_caliber_nation[key].extend(shells)
for key, shells in fake_shells_by_caliber_nation.items():
    all_shells_by_caliber_nation[key].extend(shells)

print(f"Total combined: {len(all_shells_by_caliber_nation)} caliber-nation combinations")

# Read and update Gun Variants
print("Reading Gun Variants...")
gun_rows = []
updates_made = 0
guns_matched = 0

with open('D:/Research/Complete_Gun_Variants_Database.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        gun_caliber = extract_caliber_from_gun(row['Caliber_Length'])
        gun_nation_emoji = row['Nation']

        if gun_caliber and gun_nation_emoji in NATION_MAP:
            shell_nation = NATION_MAP[gun_nation_emoji]

            # Check if gun already has compatible shells
            existing_shells = row['Compatible_Shells']

            if not existing_shells or not existing_shells.strip():
                # Gun has no shells, add them
                matching_shells = all_shells_by_caliber_nation.get((gun_caliber, shell_nation), [])

                if matching_shells:
                    # Add shells WITHOUT URLs for fake shells (since they're not in Notion yet)
                    formatted_shells = []
                    for shell in matching_shells:
                        # Check if it's a fake shell (has *)
                        if '*' in shell:
                            formatted_shells.append(shell)  # No URL for fake shells
                        else:
                            # This is a real shell, but we don't have its URL here
                            formatted_shells.append(shell)  # No URL for now

                    row['Compatible_Shells'] = ', '.join(formatted_shells)
                    updates_made += 1
                    guns_matched += 1
                    print(f"Updated {row['Gun_Variant']}: added {len(matching_shells)} shells")
            else:
                # Gun already has shells
                guns_matched += 1

        gun_rows.append(row)

# Write updated Gun Variants
output_file = 'D:/Research/Complete_Gun_Variants_Database_Updated.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(gun_rows)

print(f"\nSummary:")
print(f"  Total guns processed: {len(gun_rows)}")
print(f"  New updates made: {updates_made}")
print(f"  Total guns with shells: {guns_matched}")
print(f"  Guns still without shells: {len(gun_rows) - guns_matched}")
print(f"\nUpdated file saved to: {output_file}")

# Also replace the original Complete_Gun_Variants_Database.csv
import shutil
shutil.copy2(output_file, 'D:/Research/Complete_Gun_Variants_Database.csv')
print(f"Updated Complete_Gun_Variants_Database.csv")

print(f"\nNOTE: Fake shells are included but without URLs since they need to be imported into Notion first.")
print(f"After importing the shells into Notion, you can run the URL matching script again.")