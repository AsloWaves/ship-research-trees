import csv
import re
from collections import defaultdict

# Nation mapping between Gun Variants and Shell Specifications
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

def extract_caliber_from_shell(caliber_field):
    """Extract caliber from shell's Caliber field (e.g., '16" Mk 8 AP' -> '16"')"""
    # Handle special cases like 2-pounder
    if 'pounder' in caliber_field:
        match = re.match(r'^([0-9.]+-pounder)', caliber_field)
        if match:
            return match.group(1)

    # Extract caliber (number + inches)
    match = re.match(r'^"?([0-9.]+)"', caliber_field)
    if match:
        return match.group(1) + '"'

    return None

# Read Shell Specifications
shells_by_caliber_nation = defaultdict(list)
print("Reading Shell Specifications...")
with open('D:/Research/Shell_Specifications_Updated.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        caliber = extract_caliber_from_shell(row['Caliber'])
        nation = row['Nation']
        if caliber and nation:
            # Store the full shell name for display
            shell_name = row['Caliber']  # This already has the full format
            shells_by_caliber_nation[(caliber, nation)].append(shell_name)

# Print summary of shells loaded
print(f"\nLoaded shells for {len(shells_by_caliber_nation)} caliber-nation combinations")
for (cal, nat), shells in sorted(shells_by_caliber_nation.items())[:5]:
    print(f"  {cal} {nat}: {len(shells)} shells")

# Read and update Gun Variants
print("\nReading Gun Variants...")
gun_rows = []
matches_made = 0
guns_without_matches = []

with open('D:/Research/Gun Variants 7836a1cffaab4ed4a1c97e8f6cbd49d0_Gun Variants 011ed05f919c4dce8582a36b49e410a8_all.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        gun_caliber = extract_caliber_from_gun(row['Caliber_Length'])
        gun_nation_emoji = row['Nation']

        # Skip if we already have Compatible_Shells filled
        if row['Compatible_Shells'] and row['Compatible_Shells'].strip():
            gun_rows.append(row)
            continue

        if gun_caliber and gun_nation_emoji in NATION_MAP:
            shell_nation = NATION_MAP[gun_nation_emoji]
            matching_shells = shells_by_caliber_nation.get((gun_caliber, shell_nation), [])

            if matching_shells:
                # Format: "Shell Name, Shell Name, ..."
                # For now without URLs - we'll need to get those from Notion
                row['Compatible_Shells'] = ', '.join(matching_shells)
                matches_made += 1
                print(f"Matched {row['Gun_Variant']}: {len(matching_shells)} shells")
            else:
                guns_without_matches.append(f"{row['Gun_Variant']} ({gun_caliber} {shell_nation})")

        gun_rows.append(row)

print(f"\nSummary:")
print(f"  Total guns processed: {len(gun_rows)}")
print(f"  Matches made: {matches_made}")
print(f"  Guns without matches: {len(guns_without_matches)}")

if guns_without_matches[:10]:
    print(f"\nFirst 10 guns without matching shells:")
    for gun in guns_without_matches[:10]:
        print(f"    - {gun}")

# Write updated Gun Variants
output_file = 'D:/Research/Gun_Variants_Updated.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(gun_rows)

print(f"\nUpdated file saved to: {output_file}")
print("\nNote: Shell references added WITHOUT URLs. To add Notion URLs, we'll need to:")
print("    1. Get the URL mapping from Notion")
print("    2. Update the format to include (URL) after each shell name")