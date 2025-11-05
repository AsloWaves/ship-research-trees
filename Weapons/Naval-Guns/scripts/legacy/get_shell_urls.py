import csv
import re
from collections import defaultdict

# Read Gun_Variants_Updated.csv and extract all unique shell names
print("Extracting shell names from Gun_Variants_Updated.csv...")
unique_shells = set()

with open('D:/Research/Gun_Variants_Updated.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '')
        if compatible_shells and compatible_shells.strip():
            # Split by comma and clean up shell names
            shell_names = [name.strip() for name in compatible_shells.split(',')]
            for shell in shell_names:
                if shell:
                    unique_shells.add(shell)

print(f"Found {len(unique_shells)} unique shell names:")
for shell in sorted(unique_shells):
    print(f"  - {shell}")

# Create mapping for common shell name variations
shell_search_mapping = {}
for shell in unique_shells:
    # Extract the core part for searching (remove quotes, spaces, etc.)
    search_term = shell.replace('"', '').strip()
    shell_search_mapping[shell] = search_term

print(f"\nShell search mapping created with {len(shell_search_mapping)} entries")
print("Next step: Search Notion for each shell to get URLs")