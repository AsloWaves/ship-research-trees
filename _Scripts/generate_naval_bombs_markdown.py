#!/usr/bin/env python3
"""
Generate individual markdown files for naval bombs from markdown table database.
Parses naval_bombs_database.md and creates one file per bomb.
Note: These are naval/ship-launched bombs, separate from aircraft-launched bombs already in Aircraft-Weapons.
"""

import os
import re

def sanitize_filename(name):
    """Convert designation to valid filename."""
    name = name.replace('"', 'inch')
    name = name.replace('/', '-')
    name = name.replace('\\', '-')
    name = name.replace(':', '-')
    name = name.replace('*', '')
    name = name.replace('?', '')
    name = name.replace('<', '')
    name = name.replace('>', '')
    name = name.replace('|', '-')
    return name.strip()

def parse_bomb_row(row):
    """Parse a table row into bomb data dictionary."""
    fields = [f.strip() for f in row.split('|')]

    if len(fields) < 24:  # Need at least 24 fields
        return None

    bomb = {
        'bomb_id': fields[1],
        'nation': fields[2],
        'designation': fields[3],
        'bomb_type': fields[4],
        'year': fields[5],
        'weight': fields[6],
        'length': fields[7],
        'diameter': fields[8],
        'explosive_weight': fields[9],
        'explosive_type': fields[10],
        'blast_radius': fields[11],
        'penetration': fields[12],
        'guidance_type': fields[13],
        'guidance_accuracy': fields[14],
        'max_range': fields[15],
        'terminal_velocity': fields[16],
        'fuse_type': fields[17],
        'delivery_platform': fields[18],
        'cost_usd': fields[19],
        'production_years': fields[20],
        'variants': fields[21],
        'historical_notes': fields[22],
        'modded': fields[23]
    }

    if not bomb['bomb_id'] or not bomb['bomb_id'].isdigit():
        return None

    return bomb

def generate_bomb_markdown(bomb):
    """Generate markdown content for a bomb."""
    designation = bomb['designation']
    nation = bomb['nation']
    bomb_type = bomb['bomb_type']
    bomb_id = bomb['bomb_id']
    year = bomb['year']

    # Create service life
    service_life = bomb['production_years'] if bomb['production_years'] else f"{year}-Present"

    # Create tags
    tags = []
    tags.append(f"bomb")
    tags.append(f"naval-bomb")
    tags.append(f"{bomb_type.lower().replace(' ', '-')}")
    tags.append(f"{nation.lower()}")
    if designation:
        tag = designation.lower().replace(' ', '-').replace('/', '-').replace('"', 'inch')
        tags.append(tag)

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
bomb_id: {bomb_id}
nation: {nation}
type: {bomb_type}
introduced: {year if year else 'Unknown'}
service_life: {service_life}
tags: [{', '.join(tags)}]
---

# {designation}

## Overview

**Bomb ID**: {bomb_id}
**Nation**: {nation}
**Type**: {bomb_type}
**Year Introduced**: {year if year else 'Unknown'}
**Production Years**: {bomb['production_years'] if bomb['production_years'] else 'N/A'}
"""

    # Physical Specifications
    yaml += "\n## Physical Specifications\n\n"

    if bomb['weight']:
        yaml += f"- **Weight**: {bomb['weight']} lbs  \n"
    if bomb['length']:
        yaml += f"- **Length**: {bomb['length']} ft  \n"
    if bomb['diameter']:
        yaml += f"- **Diameter**: {bomb['diameter']} ft  \n"

    # Explosive Specifications
    yaml += "\n## Explosive Specifications\n\n"

    if bomb['explosive_weight']:
        yaml += f"- **Explosive Weight**: {bomb['explosive_weight']} lbs  \n"
    if bomb['explosive_type']:
        yaml += f"- **Explosive Type**: {bomb['explosive_type']}  \n"
    if bomb['blast_radius']:
        yaml += f"- **Blast Radius**: {bomb['blast_radius']} ft  \n"
    if bomb['penetration']:
        yaml += f"- **Penetration**: {bomb['penetration']} inches  \n"

    # Guidance & Performance
    yaml += "\n## Guidance & Performance\n\n"

    if bomb['guidance_type']:
        yaml += f"- **Guidance Type**: {bomb['guidance_type']}  \n"
    if bomb['guidance_accuracy']:
        yaml += f"- **Guidance Accuracy**: {bomb['guidance_accuracy']} ft CEP  \n"
    if bomb['max_range']:
        yaml += f"- **Maximum Range**: {bomb['max_range']} nm  \n"
    if bomb['terminal_velocity']:
        yaml += f"- **Terminal Velocity**: {bomb['terminal_velocity']} ft/s  \n"

    # Fuse & Delivery
    yaml += "\n## Fuse & Delivery\n\n"

    if bomb['fuse_type']:
        yaml += f"- **Fuse Type**: {bomb['fuse_type']}  \n"
    if bomb['delivery_platform']:
        yaml += f"- **Delivery Platform**: {bomb['delivery_platform']}  \n"

    # Variants & Cost
    if bomb['variants']:
        yaml += f"\n## Variants\n\n{bomb['variants']}  \n"

    if bomb['cost_usd']:
        yaml += f"\n## Cost\n\n**Unit Cost**: ${bomb['cost_usd']:,} USD  \n"

    # Historical Notes
    if bomb['historical_notes']:
        yaml += f"\n## Historical Notes\n\n{bomb['historical_notes']}  \n"

    yaml += "\n"
    return yaml

def main():
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_bombs_database.md"
    output_base = r"D:\Research\Weapons\Bombs"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Parse bomb entries
    bombs = []
    for line in lines:
        if re.match(r'^\|\s*9\d+\s*\|', line):  # Bombs start with 9xxx IDs
            bomb = parse_bomb_row(line)
            if bomb:
                bombs.append(bomb)

    print(f"Found {len(bombs)} naval bombs to process")

    # Group by nation
    by_nation = {}
    for bomb in bombs:
        nation = bomb['nation']
        if nation not in by_nation:
            by_nation[nation] = []
        by_nation[nation].append(bomb)

    # Generate markdown files
    total_created = 0
    for nation, nation_bombs in by_nation.items():
        nation_dir = os.path.join(output_base, nation)
        os.makedirs(nation_dir, exist_ok=True)

        print(f"\n{nation}: {len(nation_bombs)} bombs")

        for bomb in nation_bombs:
            designation = bomb['designation']
            filename_base = f"{designation}"
            filename = sanitize_filename(filename_base) + ".md"
            filepath = os.path.join(nation_dir, filename)

            md_content = generate_bomb_markdown(bomb)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            total_created += 1

    print(f"\n✅ Created {total_created} naval bomb markdown files")
    print(f"📁 Location: {output_base}/[Nation]/")

if __name__ == "__main__":
    main()
