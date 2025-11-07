#!/usr/bin/env python3
"""
Generate individual markdown files for naval missiles from markdown table database.
Parses naval_missiles_database.md and creates one file per missile.
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

def parse_missile_row(row):
    """Parse a table row into missile data dictionary."""
    fields = [f.strip() for f in row.split('|')]

    if len(fields) < 24:  # Need at least 24 fields
        return None

    missile = {
        'missile_id': fields[1],
        'country': fields[2],
        'designation': fields[3],
        'nato_codename': fields[4],
        'type': fields[5],
        'role': fields[6],
        'year_introduced': fields[7],
        'diameter_in': fields[8],
        'length_ft': fields[9],
        'wingspan_ft': fields[10],
        'weight_lbs': fields[11],
        'warhead_lbs': fields[12],
        'warhead_type': fields[13],
        'max_speed_mach': fields[14],
        'max_range_nm': fields[15],
        'min_range_nm': fields[16],
        'max_altitude_ft': fields[17],
        'min_altitude_ft': fields[18],
        'propulsion': fields[19],
        'guidance': fields[20],
        'launch_platform': fields[21],
        'modded': fields[22],
        'notes': fields[23]
    }

    if not missile['missile_id'] or not missile['missile_id'].isdigit():
        return None

    return missile

def generate_missile_markdown(missile):
    """Generate markdown content for a missile."""
    designation = missile['designation']
    country = missile['country']
    missile_type = missile['type']
    missile_id = missile['missile_id']
    year = missile['year_introduced']
    nato_codename = missile['nato_codename']
    role = missile['role']

    # Create service life
    service_life = f"{year}-Present" if year else "Unknown"

    # Create tags
    tags = []
    tags.append(f"missile")
    tags.append(f"{missile_type.lower().replace(' ', '-')}")
    tags.append(f"{country.lower()}")
    if designation:
        tag = designation.lower().replace(' ', '-').replace('/', '-').replace('"', 'inch')
        tags.append(tag)

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
missile_id: {missile_id}
nation: {country}
type: {missile_type}
role: {role if role else 'N/A'}
introduced: {year if year else 'Unknown'}
service_life: {service_life}
tags: [{', '.join(tags)}]
---

# {designation}

## Overview

**Missile ID**: {missile_id}
**Nation**: {country}
**Type**: {missile_type}
**Role**: {role if role else 'N/A'}
"""

    if nato_codename:
        yaml += f"**NATO Codename**: {nato_codename}  \n"

    yaml += f"**Year Introduced**: {year if year else 'Unknown'}  \n"

    # Physical Specifications
    yaml += "\n## Physical Specifications\n\n"

    if missile['diameter_in']:
        yaml += f"- **Diameter**: {missile['diameter_in']}\"  \n"
    if missile['length_ft']:
        yaml += f"- **Length**: {missile['length_ft']} ft  \n"
    if missile['wingspan_ft']:
        yaml += f"- **Wingspan**: {missile['wingspan_ft']} ft  \n"
    if missile['weight_lbs']:
        yaml += f"- **Weight**: {missile['weight_lbs']} lbs  \n"

    # Warhead
    yaml += "\n## Warhead\n\n"

    if missile['warhead_lbs']:
        yaml += f"- **Warhead Weight**: {missile['warhead_lbs']} lbs  \n"
    if missile['warhead_type']:
        yaml += f"- **Warhead Type**: {missile['warhead_type']}  \n"

    # Performance
    yaml += "\n## Performance\n\n"

    if missile['max_speed_mach']:
        yaml += f"- **Maximum Speed**: Mach {missile['max_speed_mach']}  \n"
    if missile['max_range_nm']:
        yaml += f"- **Maximum Range**: {missile['max_range_nm']} nm  \n"
    if missile['min_range_nm']:
        yaml += f"- **Minimum Range**: {missile['min_range_nm']} nm  \n"
    if missile['max_altitude_ft']:
        yaml += f"- **Maximum Altitude**: {missile['max_altitude_ft']} ft  \n"
    if missile['min_altitude_ft']:
        yaml += f"- **Minimum Altitude**: {missile['min_altitude_ft']} ft  \n"

    # Propulsion & Guidance
    yaml += "\n## Propulsion & Guidance\n\n"

    if missile['propulsion']:
        yaml += f"- **Propulsion**: {missile['propulsion']}  \n"
    if missile['guidance']:
        yaml += f"- **Guidance**: {missile['guidance']}  \n"

    # Launch Platform
    if missile['launch_platform']:
        yaml += f"\n## Launch Platforms\n\n{missile['launch_platform']}  \n"

    # Notes
    if missile['notes']:
        yaml += f"\n## Notes\n\n{missile['notes']}  \n"

    yaml += "\n"
    return yaml

def main():
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_missiles_database.md"
    output_base = r"D:\Research\Weapons\Missiles"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Parse missile entries
    missiles = []
    for line in lines:
        if re.match(r'^\|\s*\d+\s*\|', line):
            missile = parse_missile_row(line)
            if missile:
                missiles.append(missile)

    print(f"Found {len(missiles)} missiles to process")

    # Group by nation
    by_nation = {}
    for missile in missiles:
        nation = missile['country']
        if nation not in by_nation:
            by_nation[nation] = []
        by_nation[nation].append(missile)

    # Generate markdown files
    total_created = 0
    for nation, nation_missiles in by_nation.items():
        nation_dir = os.path.join(output_base, nation)
        os.makedirs(nation_dir, exist_ok=True)

        print(f"\n{nation}: {len(nation_missiles)} missiles")

        for missile in nation_missiles:
            designation = missile['designation']
            filename_base = f"{designation}"
            filename = sanitize_filename(filename_base) + ".md"
            filepath = os.path.join(nation_dir, filename)

            md_content = generate_missile_markdown(missile)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            total_created += 1

    print(f"\n✅ Created {total_created} missile markdown files")
    print(f"📁 Location: {output_base}/[Nation]/")

if __name__ == "__main__":
    main()
