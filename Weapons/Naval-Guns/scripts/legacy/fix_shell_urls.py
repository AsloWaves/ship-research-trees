import csv
import re
from collections import defaultdict

print("Fixing Shell URLs in Gun Variants Database...")

# First, read the shell database to get correct shell name -> URL mapping
shell_url_map = {}

print("Reading Shell Specifications Database...")
with open('D:/Research/Complete_Shell_Specifications_Database.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        caliber = row.get('Caliber', '').strip()
        if caliber:
            # The shell URLs will need to be obtained from Notion
            # For now, we'll create a placeholder mapping
            shell_url_map[caliber] = None

print(f"Found {len(shell_url_map)} unique shells")

# Known correct URLs from our search results
known_urls = {
    "13.4\" M1912 AP": "https://www.notion.so/2750ddf7bbe581d89d91de1591b4f246",
    "15\" Mk 5 AP": "https://www.notion.so/2750ddf7bbe58117b36ef6dcbca7a856",
    "8\" Mk 21 AP": "https://www.notion.so/2750ddf7bbe581a08486faa3a5ec29b9",
    "8\" Mark VIIIa SAPC": "https://www.notion.so/2750ddf7bbe581f09a4fd1f09cd79224",
    "6\" Mk 4 HE": "https://www.notion.so/2750ddf7bbe5814d9e9acefcba7a8d5e",
    "13.39\" Mle 1912 AP": "https://www.notion.so/2750ddf7bbe58150ad2fff03fa1e1d95",
    "13.39\" Mle 1912 HE": "https://www.notion.so/2750ddf7bbe5816e9a51ce07e6d211f1",
    "5.46\" Mle 1929 HE": "https://www.notion.so/2750ddf7bbe58104a0aece562047f9a1",
    "16\" Mk 8 AP": "https://www.notion.so/2750ddf7bbe581079a2bd435d0c6bfe2",
    "14.96\" Mle 1936 AP": "https://www.notion.so/2750ddf7bbe581f79b52c062e4f6fe4d"
}

# Add more known URLs
shell_url_map.update(known_urls)

# Read gun variants and identify all shell references that need URLs
print("Analyzing Gun Variants for shell references...")
gun_rows = []
shells_needing_urls = set()

with open('D:/Research/Complete_Gun_Variants_Database.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '')

        if compatible_shells:
            # Parse shell references - they can have URLs or not
            shell_parts = compatible_shells.split(', ')

            for shell_part in shell_parts:
                # Check if it has a URL already
                if '(https://' in shell_part and ')' in shell_part:
                    # Extract shell name (everything before the URL)
                    shell_name = shell_part.split(' (https://')[0].strip()
                else:
                    # No URL, this is just the shell name
                    shell_name = shell_part.strip()

                if shell_name and shell_name not in shell_url_map:
                    shells_needing_urls.add(shell_name)

        gun_rows.append(row)

print(f"Found {len(shells_needing_urls)} shells needing URL lookup:")
for shell in sorted(shells_needing_urls):
    print(f"  - {shell}")

print("\nThis script has identified the shells that need URLs.")
print("The URLs need to be obtained from Notion search for each shell.")
print("Manual URL collection required for complete fix.")