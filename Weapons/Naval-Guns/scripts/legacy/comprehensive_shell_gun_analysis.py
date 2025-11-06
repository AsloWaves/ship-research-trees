import csv
import re
from collections import defaultdict

print("ULTRATHINK: Comprehensive Shell-Gun Variant Relationship Analysis")
print("=" * 80)

# ============================================================================
# PHASE 1: INVENTORY BOTH DATABASES
# ============================================================================

print("\nPHASE 1: Database Inventory")
print("-" * 40)

# Read Shell Database - get caliber-nation-type combinations
shell_inventory = {}  # caliber -> nation -> types[]
shell_names = set()

with open('D:/Research/Shell_Specifications_Updated.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        caliber_full = row.get('Caliber', '').strip()
        nation = row.get('Nation', '').strip()

        if caliber_full and nation:
            # Extract base caliber (e.g., "16\" Mk 8 AP" -> "16\"")
            caliber_match = re.match(r'^([0-9.]+\"|[0-9.]+-pounder)', caliber_full)
            if caliber_match:
                base_caliber = caliber_match.group(1)

                # Extract shell type (AP, HE, SAP, etc.)
                shell_type = 'Unknown'
                if ' AP' in caliber_full:
                    shell_type = 'AP'
                elif ' HE' in caliber_full:
                    shell_type = 'HE'
                elif ' SAP' in caliber_full:
                    shell_type = 'SAP'
                elif ' SAPC' in caliber_full:
                    shell_type = 'SAPC'
                elif ' Common' in caliber_full:
                    shell_type = 'Common'

                # Build inventory
                if base_caliber not in shell_inventory:
                    shell_inventory[base_caliber] = {}
                if nation not in shell_inventory[base_caliber]:
                    shell_inventory[base_caliber][nation] = set()

                shell_inventory[base_caliber][nation].add(shell_type)
                shell_names.add(caliber_full)

print(f"Shell Database: {len(shell_names)} total shells")

# Count caliber-nation combinations in shell database
shell_combos = set()
for caliber, nations in shell_inventory.items():
    for nation in nations:
        shell_combos.add((caliber, nation))

print(f"Shell Database: {len(shell_combos)} caliber-nation combinations")

# Read Gun Variants Database - get caliber-nation combinations
gun_inventory = {}  # caliber -> nation -> count
gun_names = set()

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

with open('D:/Research/Gun_Variants_With_URLs.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        gun_variant = row.get('Gun_Variant', '').strip()
        caliber_length = row.get('Caliber_Length', '').strip()
        nation_emoji = row.get('Nation', '').strip()

        if gun_variant and caliber_length and nation_emoji in NATION_MAP:
            nation = NATION_MAP[nation_emoji]

            # Extract base caliber from gun (e.g., "16\"/45" -> "16\"")
            caliber_match = re.match(r'^\"?([0-9.]+)\"', caliber_length)
            if caliber_match:
                base_caliber = caliber_match.group(1) + '"'

                if base_caliber not in gun_inventory:
                    gun_inventory[base_caliber] = {}
                if nation not in gun_inventory[base_caliber]:
                    gun_inventory[base_caliber][nation] = 0

                gun_inventory[base_caliber][nation] += 1
                gun_names.add(gun_variant)

print(f"Gun Database: {len(gun_names)} total gun variants")

# Count caliber-nation combinations in gun database
gun_combos = set()
for caliber, nations in gun_inventory.items():
    for nation in nations:
        gun_combos.add((caliber, nation))

print(f"Gun Database: {len(gun_combos)} caliber-nation combinations")

# ============================================================================
# PHASE 2: GAP ANALYSIS
# ============================================================================

print(f"\nPHASE 2: Gap Analysis")
print("-" * 40)

# Find caliber-nation combinations that exist in guns but not in shells
guns_without_shells = gun_combos - shell_combos
shells_without_guns = shell_combos - gun_combos

print(f"Gun combinations WITHOUT matching shells: {len(guns_without_shells)}")
for caliber, nation in sorted(guns_without_shells):
    gun_count = gun_inventory[caliber][nation]
    print(f"  - {caliber} {nation}: {gun_count} gun variant(s)")

print(f"\nShell combinations WITHOUT matching guns: {len(shells_without_guns)}")
for caliber, nation in sorted(shells_without_guns):
    shell_types = shell_inventory[caliber][nation]
    print(f"  - {caliber} {nation}: {len(shell_types)} shell type(s) {list(shell_types)}")

# ============================================================================
# PHASE 3: SHELL TYPE COVERAGE ANALYSIS
# ============================================================================

print(f"\nPHASE 3: Shell Type Coverage Analysis")
print("-" * 40)

# For each gun caliber-nation combo, check what shell types are available
coverage_gaps = []

for caliber, nation in sorted(gun_combos):
    if (caliber, nation) in shell_combos:
        available_types = shell_inventory[caliber][nation]
        gun_count = gun_inventory[caliber][nation]

        # Check for essential shell types
        has_ap = 'AP' in available_types
        has_he = 'HE' in available_types
        has_sap = 'SAP' in available_types or 'SAPC' in available_types

        missing_types = []
        if not has_ap:
            missing_types.append('AP')
        if not has_he:
            missing_types.append('HE')

        if missing_types:
            coverage_gaps.append({
                'caliber': caliber,
                'nation': nation,
                'gun_count': gun_count,
                'available': list(available_types),
                'missing': missing_types
            })

print(f"Shell type coverage gaps: {len(coverage_gaps)}")
for gap in coverage_gaps:
    print(f"  - {gap['caliber']} {gap['nation']}: has {gap['available']}, missing {gap['missing']} ({gap['gun_count']} guns)")

# ============================================================================
# PHASE 4: NAME MATCHING ANALYSIS
# ============================================================================

print(f"\nPHASE 4: Shell Name Matching Analysis")
print("-" * 40)

# Get shells referenced in gun variants without URLs
referenced_shells_without_urls = set()

with open('D:/Research/Gun_Variants_With_URLs.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '')
        if compatible_shells and compatible_shells.strip():
            shell_entries = [shell.strip() for shell in compatible_shells.split(',')]
            for shell_entry in shell_entries:
                if shell_entry and '(https://' not in shell_entry:
                    referenced_shells_without_urls.add(shell_entry.strip())

print(f"Shells referenced by guns but missing URLs: {len(referenced_shells_without_urls)}")

# Check if these shells exist in database with different names
name_mismatches = []
for ref_shell in referenced_shells_without_urls:
    exact_match = ref_shell in shell_names
    if not exact_match:
        # Look for similar shells
        close_matches = []
        for db_shell in shell_names:
            ref_clean = ref_shell.replace('"', '').replace('  ', ' ').strip()
            db_clean = db_shell.replace('"', '').replace('  ', ' ').strip()

            if ref_clean.lower() in db_clean.lower() or db_clean.lower() in ref_clean.lower():
                close_matches.append(db_shell)

        name_mismatches.append({
            'referenced': ref_shell,
            'close_matches': close_matches
        })

print(f"Potential name mismatches: {len(name_mismatches)}")
for mismatch in name_mismatches[:10]:
    print(f"  Referenced: '{mismatch['referenced']}'")
    if mismatch['close_matches']:
        for match in mismatch['close_matches'][:2]:
            print(f"    Similar: '{match}'")
    else:
        print(f"    No similar shells found")

# ============================================================================
# PHASE 5: RECOMMENDATIONS
# ============================================================================

print(f"\nPHASE 5: Recommendations")
print("-" * 40)

# Calculate what needs to be created
shells_to_create = []

# 1. Create shells for gun combinations without any shells
for caliber, nation in guns_without_shells:
    gun_count = gun_inventory[caliber][nation]
    shells_to_create.append({
        'caliber': caliber,
        'nation': nation,
        'types': ['AP', 'HE'],  # Create basic AP and HE
        'reason': f'No shells exist for {gun_count} gun variant(s)',
        'fake': True
    })

# 2. Create missing shell types for existing combinations
for gap in coverage_gaps:
    for missing_type in gap['missing']:
        shells_to_create.append({
            'caliber': gap['caliber'],
            'nation': gap['nation'],
            'types': [missing_type],
            'reason': f'Missing {missing_type} for {gap["gun_count"]} gun variant(s)',
            'fake': True
        })

print(f"SHELLS TO CREATE: {len(shells_to_create)}")
shells_by_nation = defaultdict(list)
for shell in shells_to_create:
    shells_by_nation[shell['nation']].extend(shell['types'])
    print(f"  - {shell['caliber']} {shell['nation']} {', '.join(shell['types'])}: {shell['reason']}")

print(f"\nSUMMARY BY NATION:")
for nation, types in shells_by_nation.items():
    print(f"  {nation}: {len(types)} shell types to create")

print(f"\nORPHAN SHELLS (exist but no guns use them): {len(shells_without_guns)}")
print("These shells could be kept for historical completeness or removed if cleanup desired.")

# Save recommendations
with open('D:/Research/shell_creation_recommendations.txt', 'w', encoding='utf-8') as f:
    f.write("COMPREHENSIVE SHELL-GUN ANALYSIS RECOMMENDATIONS\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"SHELLS TO CREATE: {len(shells_to_create)}\n")
    f.write("-" * 30 + "\n")
    for shell in shells_to_create:
        for shell_type in shell['types']:
            f.write(f"{shell['caliber']} {shell['nation']} {shell_type}* - {shell['reason']}\n")

    f.write(f"\nORPHAN SHELLS: {len(shells_without_guns)}\n")
    f.write("-" * 30 + "\n")
    for caliber, nation in sorted(shells_without_guns):
        shell_types = shell_inventory[caliber][nation]
        f.write(f"{caliber} {nation}: {list(shell_types)}\n")

print(f"\nDetailed recommendations saved to: shell_creation_recommendations.txt")