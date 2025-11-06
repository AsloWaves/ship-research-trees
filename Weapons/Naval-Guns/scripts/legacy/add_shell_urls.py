import csv
import re

# Comprehensive shell URL mapping with all found URLs
shell_urls = {
    # Already known from previous searches
    "3.94\" Mle 1930 AP": "https://www.notion.so/2750ddf7bbe581bb9e53fc4e0b10be37",
    "3.94\" Mle 1930 HE": "https://www.notion.so/2750ddf7bbe58139aa2ef454cbb4d85d",
    "8\" Mark VIIIa SAPC": "https://www.notion.so/2750ddf7bbe5814fb28ed96718122d74",
    "15\" Mk 5 AP": "https://www.notion.so/2750ddf7bbe58129acd9ddb6e25bc31b",
    "6\" Mk 4 HE": "https://www.notion.so/2750ddf7bbe58111bbb3e74cfd72306e",
    "8\" Mk 21 AP": "https://www.notion.so/2750ddf7bbe58141bda6f5c8f0ec3c6f",
    "6\" Mark XXIII AP": "https://www.notion.so/2750ddf7bbe58117a159c32e3318d517",
    "14\" B-37 AP": "https://www.notion.so/2750ddf7bbe58123938ce327de84a8c3",
    "15\" Mark IVa HE": "https://www.notion.so/2750ddf7bbe58138a05df4806015283c",
    "15\" Mark XIIa AP": "https://www.notion.so/2750ddf7bbe5813ba17fd9d6d45be167",
    "6\" Mark XII AP": "https://www.notion.so/2750ddf7bbe5810dbba6f1f8e3ec7655",
    "15\" Mark I AP": "https://www.notion.so/2750ddf7bbe581138d2af1891cf11d04",
    "8\" M1924 AP": "https://www.notion.so/2750ddf7bbe5816ca933d59e189bc833",
    "5\" Type 0 HE": "https://www.notion.so/2750ddf7bbe5819b909efa7f6160051e",
    "8\" Mark VIII HE": "https://www.notion.so/2750ddf7bbe581c0821aeb44672ce902",
    "16\" Mk 8 AP": "https://www.notion.so/2750ddf7bbe581c6bc7bebe5711a09e7",
    "18\" Mark II AP": "https://www.notion.so/2750ddf7bbe581d29d4ac239fc891e19",
    "6\" B-38 HE": "https://www.notion.so/2750ddf7bbe581d4ab99d1de99f6ad56",
    "14\" Mark VII HE": "https://www.notion.so/2750ddf7bbe581dc86f5fad05ae0d23c",
    "6.7\" Coastal AP": "https://www.notion.so/2750ddf7bbe5817984ddf029addcf963",
    "6\" Mk 35 HE": "https://www.notion.so/2750ddf7bbe581a5a76aefe80d8c32bd",
    "6\" M1930 HE": "https://www.notion.so/2750ddf7bbe581aa823be96a84ece9c5",
    "18\" Mark II HE": "https://www.notion.so/2750ddf7bbe581abb670ef358c5745b8",
    "8\" Mark VIII AP": "https://www.notion.so/2750ddf7bbe5817c833dd8fd07766753",
    "6\" Mark XII HE": "https://www.notion.so/2750ddf7bbe581b1873bf09ced89358f",
    "5\" Mk 54 HE": "https://www.notion.so/2750ddf7bbe581fa8506c0e6e9ef8244",
    "15\" M1934 AP": "https://www.notion.so/2750ddf7bbe581179dc2db0260c59bcd",
    "6.7\" Coastal HE": "https://www.notion.so/2750ddf7bbe581229e5cf86d6e7b780e",
    "16\" Mark I HE": "https://www.notion.so/2750ddf7bbe5812ea3c5da35e76b1600",
    "3\" Type 3 HE": "https://www.notion.so/2750ddf7bbe5813883feee5e7d650a6e",
    "16\" Mark I AP": "https://www.notion.so/2750ddf7bbe58183bdecd3f14e410a00",
    "16\" B-37 AP": "https://www.notion.so/2750ddf7bbe5818593efd2b76f5fd732",
    "14.96\" Mle 1936 AP": "https://www.notion.so/2750ddf7bbe581e1a3dcc987ef3236ed",
    "13.0\" Mle 1931 AP": "https://www.notion.so/2750ddf7bbe5818f94a4faa5b000c895",
    "8\" SK C/34 AP": "https://www.notion.so/2750ddf7bbe58144ad81d7d97e763c89",
    "16.1\" Type 91 AP": "https://www.notion.so/2750ddf7bbe58145b235df131fa2f4ee",
    "7.64\" Mle 1893 HE": "https://www.notion.so/2750ddf7bbe58164ac0fed391a712971",
    "14.96\" M1935 AP": "https://www.notion.so/2750ddf7bbe58119a9feccb6523e3460",
    "15\" Mark XIIa Supercharge AP": "https://www.notion.so/2750ddf7bbe58133844ac7e8aea15647",
    "4.5\" QF Mark I-IV HE": "https://www.notion.so/2750ddf7bbe5819e9b7defb6ae683fa4",
    "14.57\" Mle 1915 Heavy HE": "https://www.notion.so/2750ddf7bbe581f2b988ff9f2a6b0945",

    # Newly found from search
    "13.4\" M1912 AP": "https://www.notion.so/2750ddf7bbe5811ba176ea45c2dc0ab1",
    "12.6\" M1909 AP": "https://www.notion.so/2750ddf7bbe581d58253cb7351d0ba1c",
    "14\" Mark VIIb AP": "https://www.notion.so/2750ddf7bbe581c8a414d8144260e725",
    "4.5\" QF Mark I-IV AP": "https://www.notion.so/2750ddf7bbe581f8b24eeec826afb6ec",
    "4.7\" SK L/50 AP": "https://www.notion.so/2750ddf7bbe5811d9abaf8efca6719f6",
    "4.7\" QF Mark IX/XII AP": "https://www.notion.so/2750ddf7bbe581b8a48dd229b634a36a",
    "18.1\" Type 94 AP": "https://www.notion.so/2750ddf7bbe581cbabe6e94c4a25ab47"
}

print(f"Processing Gun_Variants_Updated.csv with {len(shell_urls)} shell URLs...")

# Read the Gun Variants CSV
gun_rows = []
updates_made = 0
shells_found = 0
shells_not_found = 0

with open('D:/Research/Gun_Variants_Updated.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '')

        if compatible_shells and compatible_shells.strip():
            # Split shell names and add URLs where available
            shell_names = [name.strip() for name in compatible_shells.split(',')]
            updated_shells = []

            for shell_name in shell_names:
                if shell_name in shell_urls:
                    # Format: "Shell Name (URL)"
                    url = shell_urls[shell_name]
                    formatted_shell = f"{shell_name} ({url})"
                    updated_shells.append(formatted_shell)
                    shells_found += 1
                else:
                    # Keep shell name as-is if no URL found
                    updated_shells.append(shell_name)
                    shells_not_found += 1
                    if shell_name not in ["", " "]:  # Don't print empty strings
                        print(f"  No URL found for: {shell_name}")

            if len(updated_shells) > 0:
                row['Compatible_Shells'] = ', '.join(updated_shells)
                updates_made += 1

        gun_rows.append(row)

# Write the updated CSV
output_file = 'D:/Research/Gun_Variants_With_URLs.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(gun_rows)

print(f"\nSummary:")
print(f"  Total guns processed: {len(gun_rows)}")
print(f"  Guns with shell updates: {updates_made}")
print(f"  Shells with URLs found: {shells_found}")
print(f"  Shells without URLs: {shells_not_found}")
print(f"\nUpdated file saved to: {output_file}")

# Show example of updated format
print(f"\nExample of updated format (3.9\" gun):")
for row in gun_rows:
    if "3.9" in row.get('Gun_Variant', ''):
        print(f"  {row['Gun_Variant']}: {row['Compatible_Shells']}")
        break