#!/usr/bin/env python3
"""
Generate markdown files for ALL naval guns from naval_guns_database.md
Handles: USA (683), British (275), German (220), Japanese (300) = 1,478 total
"""

import os
import re

def sanitize_filename(name):
    """Convert designation to valid filename."""
    name = name.replace('"', 'inch')
    name = name.replace('/', '-').replace('\\', '-').replace(':', '-')
    name = name.replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '-')
    return name.strip()

def parse_gun_entry(line):
    """Parse a gun table row."""
    # Split by pipe and strip whitespace
    fields = [f.strip() for f in line.split('|')]

    # Skip if not enough fields or not a data row
    if len(fields) < 10:
        return None

    gun_id = fields[1]

    # Only process gun IDs (numeric)
    if not gun_id or not gun_id.isdigit():
        return None

    gun_id_num = int(gun_id)

    # Filter by ID ranges: USA 300-499, British 500-599, German 600-699, Japanese 700-899
    if gun_id_num < 300 or gun_id_num >= 900:
        return None

    country = fields[3]
    caliber = fields[4]
    length = fields[5]
    mark = fields[6]
    year = fields[7] if fields[7] else 'Unknown'
    weight = fields[8]
    notes = fields[10] if len(fields) > 10 else ''

    # Create full designation
    designation = f"{caliber}{length} {mark}"

    return {
        'id': gun_id,
        'country': country,
        'caliber': caliber,
        'length': length,
        'mark': mark,
        'designation': designation,
        'year': year,
        'weight': weight,
        'notes': notes
    }

def generate_markdown(gun):
    """Generate markdown content for a gun."""
    tags = ['naval-gun', gun['country'].lower()]
    if gun['caliber']:
        tags.append(gun['caliber'].replace('"', 'inch').replace('.', '').lower())

    md = f"""---
designation: {gun['designation']}
gun_id: {gun['id']}
nation: {gun['country']}
caliber: {gun['caliber']}
mark: {gun['mark']}
year: {gun['year']}
tags: [{', '.join(tags)}]
---

# {gun['designation']}

## Overview
**Nation**: {gun['country']}
**Caliber**: {gun['caliber']}
**Length**: {gun['length']}
**Mark**: {gun['mark']}
**Year Introduced**: {gun['year']}

## Specifications
- **Weight**: {gun['weight']} tons
- **Gun ID**: {gun['id']}

## Notes
{gun['notes']}
"""
    return md

def main():
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_guns_database.md"
    output_base = r"D:\Research\Weapons\Naval-Guns\Guns"

    print("Parsing naval_guns_database.md...")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the Guns Table section (lines 19-408)
    guns = []
    in_guns_table = False
    for i, line in enumerate(lines):
        if '## Guns Table' in line:
            in_guns_table = True
            continue
        if in_guns_table and '## Ammunition Table' in line:
            break
        if in_guns_table and line.startswith('|') and not line.startswith('| Gun_ID') and not line.startswith('|---'):
            gun = parse_gun_entry(line)
            if gun:
                guns.append(gun)

    print(f"Found {len(guns)} total gun entries")

    # Count by nation
    nation_counts = {}
    for gun in guns:
        nation = gun['country']
        nation_counts[nation] = nation_counts.get(nation, 0) + 1

    print("\nGuns by nation:")
    for nation, count in sorted(nation_counts.items()):
        print(f"  {nation}: {count}")

    # Generate markdown files
    created = 0
    for gun in guns:
        nation = gun['country']
        nation_dir = os.path.join(output_base, nation)
        os.makedirs(nation_dir, exist_ok=True)

        filename = sanitize_filename(gun['designation']) + ".md"
        filepath = os.path.join(nation_dir, filename)

        md_content = generate_markdown(gun)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)

        created += 1

    print(f"\nCreated {created} naval gun markdown files")
    print("\nBreakdown by nation:")
    for nation, count in sorted(nation_counts.items()):
        nation_dir = os.path.join(output_base, nation)
        actual_count = len([f for f in os.listdir(nation_dir) if f.endswith('.md')])
        print(f"  {nation}: {actual_count} files in {nation_dir}")

if __name__ == "__main__":
    main()
