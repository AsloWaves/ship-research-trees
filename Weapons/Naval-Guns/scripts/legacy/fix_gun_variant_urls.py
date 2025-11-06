import csv
import re

print("Fixing Gun Variants URLs with correct Notion shell URLs...")

# Comprehensive URL mapping based on Notion search results
CORRECT_SHELL_URLS = {
    # French shells
    "13.4\" M1912 AP": "https://www.notion.so/2750ddf7bbe581d89d91de1591b4f246",
    "13.39\" Mle 1912 AP": "https://www.notion.so/2750ddf7bbe58150ad2fff03fa1e1d95",
    "13.39\" Mle 1912 HE": "https://www.notion.so/2750ddf7bbe5816e9a51ce07e6d211f1",
    "14.96\" M1935 AP": "https://www.notion.so/2750ddf7bbe58151b8ecfcbbae274249",
    "14.96\" Mle 1936 AP": "https://www.notion.so/2750ddf7bbe58162bfbdd33909e02b6d",
    "14.96\" Mle 1936 HE": "https://www.notion.so/2750ddf7bbe581389188c9dd452ce3f4",
    "14.96\" Mle 1936 Jean Bart AP": "https://www.notion.so/2750ddf7bbe581aabcfefa1c6e1ce239",
    "14.96\" Mle 1936 Jean Bart HE": "https://www.notion.so/2750ddf7bbe5810e8cf6e2565600d538",
    "13\" Mle 1930* AP": "https://www.notion.so/2750ddf7bbe581be9fb6e38ee89f1a65",
    "13\" Mle 1930* HE": "https://www.notion.so/2750ddf7bbe581998f4be2febb4d61dc",
    "13.4\" Mle 1930* HE": "https://www.notion.so/2750ddf7bbe581169663e35ccff66d63",
    "13.0\" Mle 1931 AP": "https://www.notion.so/2750ddf7bbe5816fa97fcb33d762710c",
    "13.0\" Mle 1931 HE": "https://www.notion.so/2750ddf7bbe581aba314cfc0f7ac3a11",
    "5.98\" Mle 1930 AP": "https://www.notion.so/2750ddf7bbe5812c81edecae290cc53f",
    "5.98\" Mle 1930 HE": "https://www.notion.so/2750ddf7bbe581068efee04eebef46de",
    "5.98\" Mle 1930 SAP": "https://www.notion.so/2750ddf7bbe58167895bf22ce41a37ad",
    "8.0\" Mle 1936 AP": "https://www.notion.so/2750ddf7bbe5813eaaf7cb28f0d344d1",
    "8.0\" Mle 1931 AP": "https://www.notion.so/2750ddf7bbe581478833e4b86b472c36",
    "8.0\" Mle 1931 HE": "https://www.notion.so/2750ddf7bbe58106acfcd3a1f0abd1ef",
    "8.0\" Mle 1931 SAP": "https://www.notion.so/2750ddf7bbe581788d6bc70630e2bf7f",
    "3.94\" Mle 1930 AP": "https://www.notion.so/2750ddf7bbe5812eb304c83828bfdbda",
    "3.94\" Mle 1930 HE": "https://www.notion.so/2750ddf7bbe58133a735e2a660cb9a34",
    "5.46\" Mle 1929 HE": "https://www.notion.so/2750ddf7bbe58104a0aece562047f9a1",

    # British shells
    "15\" Mk 5 AP": "https://www.notion.so/2750ddf7bbe58117b36ef6dcbca7a856",
    "15\" Mark XIIa AP": "https://www.notion.so/2750ddf7bbe581c2a869e96712d8e960",
    "15\" Mark IVa HE": "https://www.notion.so/2750ddf7bbe581c89129ef96d4263816",
    "15\" Mark I AP": "https://www.notion.so/2750ddf7bbe581c6a7bdf75dac598110",
    "6\" Mk 4 HE": "https://www.notion.so/2750ddf7bbe5814d9e9acefcba7a8d5e",
    "6\" Mark XXIII AP": "https://www.notion.so/2750ddf7bbe581cab64fc69802e6e199",
    "6\" Mark XII AP": "https://www.notion.so/2750ddf7bbe58130a4a1e797d7c630b9",
    "8\" Mark VIIIa SAPC": "https://www.notion.so/2750ddf7bbe581f09a4fd1f09cd79224",
    "8\" Mark VIII AP": "https://www.notion.so/2750ddf7bbe581e1974ed5ba8a93509f",
    "12\" Mark X AP": "https://www.notion.so/2750ddf7bbe581469adee8bc2091454b",
    "12\" Mark X HE": "https://www.notion.so/2750ddf7bbe5816d996af4d394aa3b49",
    "12\" Mark I* AP": "https://www.notion.so/2750ddf7bbe5818a9963c64c8c6e7fac",
    "12\" Mark I* HE": "https://www.notion.so/2750ddf7bbe581839acee0630a11da36",
    "14\" Mark VII HE": "https://www.notion.so/2750ddf7bbe581f3afd9ef95169eff46",
    "14\" Mark VIIb AP": "https://www.notion.so/2750ddf7bbe58131a5d7e920def395a2",
    "16\" Mark I AP": "https://www.notion.so/2750ddf7bbe58145a5d6c1835be51712",
    "16\" Mark I HE": "https://www.notion.so/2750ddf7bbe581be813bf8cb67354dec",
    "18\" Mark II AP": "https://www.notion.so/2750ddf7bbe5810784e9e73f4212c702",
    "13.5\" Mk 5 AP": "https://www.notion.so/2750ddf7bbe581649039d4fc063282fe",
    "13.5\" Mark V AP": "https://www.notion.so/2750ddf7bbe581b097f5c5cee328ab19",

    # US shells
    "8\" Mk 21 AP": "https://www.notion.so/2750ddf7bbe581a08486faa3a5ec29b9",
    "16\" Mk 8 AP": "https://www.notion.so/2750ddf7bbe581079a2bd435d0c6bfe2",
    "5\" Mk 54 HE": "https://www.notion.so/2750ddf7bbe581fb80a0e139ce6ba9a1",

    # Soviet shells
    "8\" B-34 AP": "https://www.notion.so/2750ddf7bbe581869cedd1adc926af97",
    "14\" B-37 AP": "https://www.notion.so/2750ddf7bbe581f1ae44c72812f5a757",
    "12\" B-40* AP": "https://www.notion.so/2750ddf7bbe581e3bf92dc23f1cef08a",
    "12\" B-40* HE": "https://www.notion.so/2750ddf7bbe581799ce9f3dc82862a69",
    "14\" B-40* HE": "https://www.notion.so/2750ddf7bbe581789c35c7660cf13c53",
    "14\" B-40* AP": "https://www.notion.so/2750ddf7bbe581e3bf92dc23f1cef08a",
    "15\" B-40* AP": "https://www.notion.so/2750ddf7bbe581ef8380feff8390f599",
    "15\" B-40* HE": "https://www.notion.so/2750ddf7bbe581a996deceb0ab00b9e2",
    "16\" B-40* HE": "https://www.notion.so/2750ddf7bbe581e58bf3e0040e0ca8a7",
    "18\" B-40* AP": "https://www.notion.so/2750ddf7bbe581729f39cc884a80574e",
    "18\" B-40* HE": "https://www.notion.so/2750ddf7bbe581bb9190d59ee98ffb7d",
    "6\" B-40* AP": "https://www.notion.so/2750ddf7bbe581a08ff6e373af811b56",
    "5.1\" B-40* AP": "https://www.notion.so/2750ddf7bbe581d8a832dd101d373aed",

    # Japanese shells
    "8\" Type 91 AP": "https://www.notion.so/2750ddf7bbe581b69fdcdecafa3de079",
    "5\" Type 0 HE": "https://www.notion.so/2750ddf7bbe581e4baf4ef0dbe4b7a6e",
    "14\" Type 3* AP": "https://www.notion.so/2750ddf7bbe58104896ae2647b154683",
    "14\" Type 3* HE": "https://www.notion.so/2750ddf7bbe581a9bd72df6d0e7d98e8",
    "18\" Type 3* AP": "https://www.notion.so/2750ddf7bbe581edb5d3eb987207af0e",

    # Italian shells
    "8\" M1924 AP": "https://www.notion.so/2750ddf7bbe58102a196d54a49d9dfc2",
    "4.7\" M1928 HE": "https://www.notion.so/2750ddf7bbe581b8b22dd715f5e2ec24",
    "12.6\" M1909 AP": "https://www.notion.so/2750ddf7bbe581d186f8e3385a84d86e",
    "15\" M1934 AP": "https://www.notion.so/2750ddf7bbe581e492e3eff1f2b69a7d",

    # German shells
    "14.96\" L/50* AP": "https://www.notion.so/2750ddf7bbe581a1a87cc0f98ae13e72",
    "14.96\" L/50* HE": "https://www.notion.so/2750ddf7bbe581b1aa76ee7304040b79",
    "18\" L/50* AP": "https://www.notion.so/2750ddf7bbe5817289d9cb44a6536d18",
    "20\" L/50* HE": "https://www.notion.so/2750ddf7bbe58173af6adb128c935466",

    # Various fake shells with * marker
    "5\" Mk 16* AP": "https://www.notion.so/2750ddf7bbe581198049f32f7e8489b7",
    "6\" Mk 16* AP": "https://www.notion.so/2750ddf7bbe5815c8232fa4ea0d95b23",
    "8\" Mk 16* HE": "https://www.notion.so/2750ddf7bbe5818db7fadb5ef43180d5",
    "12\" Mk 16* AP": "https://www.notion.so/2750ddf7bbe581159167fd188eebd2ba",
    "14\" Mk 16* HE": "https://www.notion.so/2750ddf7bbe5811aae46ec545afd9a7d",
    "15\" Model 42* AP": "https://www.notion.so/2750ddf7bbe581128a79d4288c9daaae",
    "15\" Model 42* HE": "https://www.notion.so/2750ddf7bbe5812f807af25c792226e5",
    "16\" L/50* AP": "https://www.notion.so/2750ddf7bbe581db9a74c3d690048805",
    "18\" Mk 16* AP": "https://www.notion.so/2750ddf7bbe581a399a9da9e7db7c059",
    "18\" Mk 16* HE": "https://www.notion.so/2750ddf7bbe581f09e0ccdb948773eb2",
    "14\" M1916* AP": "https://www.notion.so/2750ddf7bbe5815cb1eced53700da6f0",
    "14\" M1940* AP": "https://www.notion.so/2750ddf7bbe5816480e9ee066a88a6cc",
    "14\" M1940* HE": "https://www.notion.so/2750ddf7bbe5813ebcf6ee2be0dc222f",
    "6\" M1934* AP": "https://www.notion.so/2750ddf7bbe5818eb510d20f86efbcf8",
}

def fix_shell_url(shell_reference):
    """Fix a shell reference with the correct URL"""
    # Check if it already has a URL
    if '(https://' in shell_reference and ')' in shell_reference:
        # Extract shell name and current URL
        shell_name = shell_reference.split(' (https://')[0].strip()

        # Check if we have the correct URL
        if shell_name in CORRECT_SHELL_URLS:
            correct_url = CORRECT_SHELL_URLS[shell_name]
            return f"{shell_name} ({correct_url})"
        else:
            # Return without URL if we don't have correct one
            return shell_name
    else:
        # No URL, check if we can add one
        shell_name = shell_reference.strip()
        if shell_name in CORRECT_SHELL_URLS:
            correct_url = CORRECT_SHELL_URLS[shell_name]
            return f"{shell_name} ({correct_url})"
        else:
            return shell_name

# Read and fix gun variants
print("Reading Gun Variants Database...")
gun_rows = []
fixes_made = 0
total_shells_processed = 0

with open('D:/Research/Complete_Gun_Variants_Database.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        compatible_shells = row.get('Compatible_Shells', '')

        if compatible_shells:
            # Split shell references
            shell_parts = compatible_shells.split(', ')
            fixed_shells = []

            for shell_part in shell_parts:
                total_shells_processed += 1
                original_shell = shell_part.strip()
                fixed_shell = fix_shell_url(original_shell)

                if fixed_shell != original_shell:
                    fixes_made += 1
                    print(f"  Fixed: {original_shell} -> {fixed_shell}")

                fixed_shells.append(fixed_shell)

            # Update the row
            row['Compatible_Shells'] = ', '.join(fixed_shells)

        gun_rows.append(row)

# Write fixed database
output_file = 'D:/Research/Complete_Gun_Variants_Database_Fixed_URLs.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(gun_rows)

print(f"\nFix Summary:")
print(f"  Total gun variants: {len(gun_rows)}")
print(f"  Total shell references processed: {total_shells_processed}")
print(f"  URLs fixed: {fixes_made}")
print(f"  Shells with correct URLs: {len([url for url in CORRECT_SHELL_URLS.values() if url])}")
print(f"\nFixed database saved to: {output_file}")