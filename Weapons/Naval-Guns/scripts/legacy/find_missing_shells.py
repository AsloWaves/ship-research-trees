import csv
import re
from collections import defaultdict

# Read Gun_Variants_With_URLs.csv and extract ALL shell references
print("Analyzing Gun_Variants_With_URLs.csv for missing shells...")

all_shell_references = set()
shells_with_urls = set()
shells_without_urls = set()

with open('D:/Research/Gun_Variants_With_URLs.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '')
        if compatible_shells and compatible_shells.strip():
            # Split by comma and process each shell
            shell_entries = [shell.strip() for shell in compatible_shells.split(',')]

            for shell_entry in shell_entries:
                if shell_entry:
                    # Check if shell has URL in parentheses
                    if '(https://' in shell_entry:
                        # Extract shell name before the URL
                        shell_name = shell_entry.split(' (https://')[0].strip()
                        shells_with_urls.add(shell_name)
                        all_shell_references.add(shell_name)
                    else:
                        # Shell without URL
                        shell_name = shell_entry.strip()
                        shells_without_urls.add(shell_name)
                        all_shell_references.add(shell_name)

print(f"Found {len(all_shell_references)} total unique shell references")
print(f"  - {len(shells_with_urls)} shells have URLs")
print(f"  - {len(shells_without_urls)} shells are missing")

# Read existing Shell_Specifications_Updated.csv to see what we already have
existing_shells = set()
print(f"\nReading existing Shell_Specifications_Updated.csv...")

try:
    with open('D:/Research/Shell_Specifications_Updated.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            caliber = row.get('Caliber', '').strip()
            if caliber:
                existing_shells.add(caliber)

    print(f"Found {len(existing_shells)} existing shells in database")
except FileNotFoundError:
    print("Shell_Specifications_Updated.csv not found!")

# Find shells that are referenced but don't exist in database
missing_shells = []
for shell in shells_without_urls:
    if shell not in existing_shells:
        missing_shells.append(shell)

print(f"\nMissing shells that need to be created: {len(missing_shells)}")

# Group missing shells by nation and caliber for analysis
nation_pattern = r'(French|German|British|Italian|Japanese|Soviet|US|Spain|Austria-Hungary|Brazil|Netherlands)'
missing_by_nation = defaultdict(list)

for shell in sorted(missing_shells):
    # Try to determine nation from shell name patterns
    if 'Mle' in shell or 'M19' in shell and 'M1924' not in shell:
        nation = 'French'
    elif 'SK' in shell or 'L/' in shell:
        nation = 'German'
    elif 'QF' in shell or 'Mark' in shell or 'Mk' in shell:
        nation = 'British'
    elif 'M19' in shell or 'Mk' in shell and ('21' in shell or '54' in shell):
        nation = 'US'
    elif 'Type' in shell:
        nation = 'Japanese'
    elif 'B-' in shell:
        nation = 'Soviet'
    elif 'M1930' in shell and 'Mle' not in shell:
        nation = 'Italian'
    else:
        nation = 'Unknown'

    missing_by_nation[nation].append(shell)

print(f"\nMissing shells by nation:")
for nation, shells in missing_by_nation.items():
    print(f"  {nation}: {len(shells)} shells")
    for shell in shells[:5]:  # Show first 5
        print(f"    - {shell}")
    if len(shells) > 5:
        print(f"    ... and {len(shells) - 5} more")

# Save missing shells list for creating fake entries
with open('D:/Research/missing_shells_list.txt', 'w', encoding='utf-8') as f:
    f.write("Missing Shells That Need to be Created:\n\n")
    for nation, shells in missing_by_nation.items():
        f.write(f"{nation}:\n")
        for shell in shells:
            f.write(f"  - {shell}\n")
        f.write("\n")

print(f"\nMissing shells list saved to: missing_shells_list.txt")
print(f"Next step: Create fake shell entries for these {len(missing_shells)} missing shells")

# Also save just the shell names for easy processing
with open('D:/Research/missing_shells_only.txt', 'w', encoding='utf-8') as f:
    for shell in sorted(missing_shells):
        f.write(f"{shell}\n")

print(f"Shell names only saved to: missing_shells_only.txt")