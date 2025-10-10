import csv
import re
import time
from collections import defaultdict

# Shell names from the Gun_Variants_Updated.csv (without the ones that already have URLs)
shells_to_search = [
    "12.6\" M1909 AP",
    "13.0\" Mle 1931 AP",
    "13.0\" Mle 1931 HE",
    "13.4\" M1912 AP",
    "14\" B-37 AP",
    "14\" Mark VII HE",
    "14\" Mark VIIb AP",
    "14\" Mk 16 AP",
    "14.57\" Mle 1915 Heavy HE",
    "14.57\" Mle 1915 Railway AP",
    "14.57\" Mle 1915 Railway HE",
    "14.57\" Mle 1915 Super HE",
    "14.96\" M1935 AP",
    "14.96\" Mle 1936 AP",
    "14.96\" Mle 1936 HE",
    "14.96\" Mle 1936 Jean Bart AP",
    "14.96\" Mle 1936 Jean Bart HE",
    "15\" M1934 AP",
    "15\" Mark I AP",
    "15\" Mark IVa HE",
    "15\" Mark XIIa AP",
    "15\" Mark XIIa Supercharge AP",
    "15\" Mk 5 AP",
    "15\" SK C/34 AP",
    "16\" B-37 AP",
    "16\" Mark I AP",
    "16\" Mark I HE",
    "16\" Mk 8 AP",
    "16.1\" Type 91 AP",
    "16.5\" SK C/34 AP",
    "18\" Mark II AP",
    "18\" Mark II HE",
    "18.1\" Type 94 AP",
    "2-pounder Mk 8 AP",
    "3\" Type 3 HE",
    "3.5\" SK C/35 AP",
    "3.5\" SK C/35 HE",
    "3.5\" SK L/45 HE",
    "3.7\" SK C/30 HE",
    "4.5\" QF Mark I-IV AP",
    "4.5\" QF Mark I-IV HE",
    "4.5\" QF Mark I-IV SAP",
    "4.7\" Mk 6 HE",
    "4.7\" QF Mark IX/XII AP",
    "4.7\" QF Mark IX/XII HE",
    "4.7\" QF Mark IX/XII SAP",
    "4.7\" SK L/50 AP",
    "4.7\" SK L/50 HE",
    "5\" Mk 54 HE",
    "5\" SK C/34 AP",
    "5\" SK C/34 HE",
    "5\" Type 0 HE",
    "5.1\" B-13 HE",
    "5.1\" M1932 HE",
    "5.25\" QF Mark I AP",
    "5.25\" QF Mark I HE",
    "5.25\" QF Mark I SAP",
    "5.46\" Mle 1929 HE",
    "5.9\" SK C/25 AP",
    "5.9\" SK C/25 HE",
    "5.9\" SK C/28 AP",
    "5.9\" SK C/28 HE",
    "5.9\" SK L/45 AP",
    "5.9\" SK L/45 HE",
    "6\" B-38 HE",
    "6\" M1930 HE",
    "6\" Mark VII/VIII AP",
    "6\" Mark VII/VIII Common",
    "6\" Mark VII/VIII HE",
    "6\" Mark XII AP",
    "6\" Mark XII HE",
    "6\" Mark XXIII AP",
    "6\" Mk 35 HE",
    "6\" Mk 4 HE",
    "6.7\" Coastal AP",
    "6.7\" Coastal HE",
    "7.64\" Mle 1893 AP",
    "7.64\" Mle 1893 HE",
    "7.64\" Mle 1913 HE",
    "7.64\" Mle 1913 SAPC",
    "8\" M1924 AP",
    "8\" Mark VIII AP",
    "8\" Mark VIII HE",
    "8\" Mark VIIIa SAPC",
    "8\" Mk 21 AP",
    "8\" SK C/34 AP",
    "8\" SK C/34 HE",
    "8\" SK C/34 SAP",
    "9.4\" SK L/40 AP",
    "9.4\" SK L/40 HE",
    "9.45\" Mle 1902 AP",
    "9.45\" Mle 1902 HE",
    "9.45\" Mle 1902 SAP"
]

# Manual URL mapping from the search results we already have
known_urls = {
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
    "14.57\" Mle 1915 Heavy HE": "https://www.notion.so/2750ddf7bbe581f2b988ff9f2a6b0945"
}

print(f"Found {len(known_urls)} known URLs from search results")
print(f"Need to find URLs for {len(shells_to_search)} shells")

# Create shell URL mapping file
shell_url_mapping = {}
shell_url_mapping.update(known_urls)

print(f"Total mapped shells: {len(shell_url_mapping)}")

# Save the mapping to a file for the next script
with open('D:/Research/shell_url_mapping.txt', 'w', encoding='utf-8') as f:
    for shell, url in shell_url_mapping.items():
        f.write(f"{shell}|{url}\n")

print("Shell URL mapping saved to shell_url_mapping.txt")

# Show missing shells
missing_shells = []
for shell in shells_to_search:
    if shell not in known_urls:
        missing_shells.append(shell)

print(f"\nMissing URLs for {len(missing_shells)} shells:")
for shell in missing_shells[:10]:  # Show first 10
    print(f"  - {shell}")
if len(missing_shells) > 10:
    print(f"  ... and {len(missing_shells) - 10} more")