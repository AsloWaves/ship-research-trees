#!/usr/bin/env python3
"""Test script to verify aircraft metadata extraction"""

import re
from pathlib import Path

def extract_frontmatter(filepath):
    """Extract nation, type, and domain from YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None, None, None

        frontmatter = match.group(1)

        # Extract nation
        nation_match = re.search(r'nation:\s*(\S+)', frontmatter)
        nation = nation_match.group(1) if nation_match else None

        # Extract type
        type_match = re.search(r'type:\s*(.+?)$', frontmatter, re.MULTILINE)
        aircraft_type = type_match.group(1).strip() if type_match else None

        # Extract domain (naval vs ground) from tags
        tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
        if tags_match:
            tags = tags_match.group(1)
            if 'naval-aircraft' in tags:
                domain = 'Naval'
            elif 'ground-aircraft' in tags:
                domain = 'Land'
            else:
                domain = 'Unknown'
        else:
            domain = 'Unknown'

        return nation, aircraft_type, domain
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None, None, None

# Test on sample files
test_files = [
    'Aircraft/Naval/A-4 Skyhawk.md',
    'Aircraft/Naval/A6M2 Zero.md',
    'Aircraft/Ground/A-10A Thunderbolt II.md',
    'Aircraft/Japan/A6M2.md',
    'Aircraft/USA/F-14A.md'
]

for test_file in test_files:
    filepath = Path(test_file)
    if filepath.exists():
        nation, aircraft_type, domain = extract_frontmatter(filepath)
        print(f"\n{filepath.name}:")
        print(f"  Nation: {nation}")
        print(f"  Type: {aircraft_type}")
        print(f"  Domain: {domain}")
    else:
        print(f"\n{test_file}: FILE NOT FOUND")
