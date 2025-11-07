#!/usr/bin/env python3
"""
Generate individual markdown files for naval torpedoes from markdown table database.
Parses naval_torpedoes_database.md and creates one file per torpedo.
"""

import os
import re

def sanitize_filename(name):
    """Convert designation to valid filename."""
    # Replace problem characters
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

def parse_torpedo_row(row):
    """Parse a table row into torpedo data dictionary."""
    # Split by pipe and strip whitespace
    fields = [f.strip() for f in row.split('|')]

    # Skip if not enough fields or empty row
    if len(fields) < 19:  # Need at least 19 fields (including leading/trailing empty)
        return None

    # Extract data (skip first and last empty fields from pipe split)
    torpedo = {
        'torpedo_id': fields[1],
        'country': fields[2],
        'designation': fields[3],
        'type': fields[4],
        'year_introduced': fields[5],
        'diameter_in': fields[6],
        'length_ft': fields[7],
        'weight_lbs': fields[8],
        'warhead_lbs': fields[9],
        'warhead_type': fields[10],
        'max_speed_kts': fields[11],
        'max_range_yds': fields[12],
        'running_depth_ft': fields[13],
        'propulsion': fields[14],
        'guidance': fields[15],
        'launch_platform': fields[16],
        'modded': fields[17],
        'notes': fields[18]
    }

    # Skip if ID is empty
    if not torpedo['torpedo_id'] or not torpedo['torpedo_id'].isdigit():
        return None

    return torpedo

def generate_torpedo_markdown(torpedo):
    """Generate markdown content for a torpedo."""
    designation = torpedo['designation']
    country = torpedo['country']
    torpedo_type = torpedo['type']
    torpedo_id = torpedo['torpedo_id']
    year = torpedo['year_introduced']

    # Create service life
    service_life = f"{year}-Present" if year else "Unknown"

    # Create tags
    tags = []
    tags.append(f"torpedo")
    tags.append(f"{torpedo_type.lower().replace(' ', '-')}")
    tags.append(f"{country.lower()}")
    if designation:
        tag = designation.lower().replace(' ', '-').replace('/', '-').replace('"', 'inch')
        tags.append(tag)

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
torpedo_id: {torpedo_id}
nation: {country}
type: {torpedo_type}
introduced: {year if year else 'Unknown'}
service_life: {service_life}
tags: [{', '.join(tags)}]
---

# {designation}

## Overview

**Torpedo ID**: {torpedo_id}
**Nation**: {country}
**Type**: {torpedo_type}
**Year Introduced**: {year if year else 'Unknown'}
"""

    # Physical Specifications
    yaml += "\n## Physical Specifications\n\n"

    if torpedo['diameter_in']:
        yaml += f"- **Diameter**: {torpedo['diameter_in']}\"  \n"
    if torpedo['length_ft']:
        yaml += f"- **Length**: {torpedo['length_ft']} ft  \n"
    if torpedo['weight_lbs']:
        yaml += f"- **Total Weight**: {torpedo['weight_lbs']} lbs  \n"
    if torpedo['warhead_lbs']:
        yaml += f"- **Warhead Weight**: {torpedo['warhead_lbs']} lbs  \n"
    if torpedo['warhead_type']:
        yaml += f"- **Warhead Type**: {torpedo['warhead_type']}  \n"

    # Performance
    yaml += "\n## Performance\n\n"

    if torpedo['max_speed_kts']:
        yaml += f"- **Maximum Speed**: {torpedo['max_speed_kts']} knots  \n"
    if torpedo['max_range_yds']:
        yaml += f"- **Maximum Range**: {torpedo['max_range_yds']} yards  \n"
    if torpedo['running_depth_ft']:
        yaml += f"- **Running Depth**: {torpedo['running_depth_ft']} ft  \n"

    # Propulsion & Guidance
    yaml += "\n## Propulsion & Guidance\n\n"

    if torpedo['propulsion']:
        yaml += f"- **Propulsion**: {torpedo['propulsion']}  \n"
    if torpedo['guidance']:
        yaml += f"- **Guidance**: {torpedo['guidance']}  \n"

    # Launch Platform
    if torpedo['launch_platform']:
        yaml += f"\n## Launch Platforms\n\n{torpedo['launch_platform']}  \n"

    # Notes
    if torpedo['notes']:
        yaml += f"\n## Notes\n\n{torpedo['notes']}  \n"

    yaml += "\n"
    return yaml

def main():
    # Input file
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_torpedoes_database.md"

    # Output directory
    output_base = r"D:\Research\Weapons\Torpedoes"

    # Read input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Parse torpedo entries
    torpedoes = []
    for line in lines:
        # Look for data rows (start with | followed by digit)
        if re.match(r'^\|\s*\d+\s*\|', line):
            torpedo = parse_torpedo_row(line)
            if torpedo:
                torpedoes.append(torpedo)

    print(f"Found {len(torpedoes)} torpedoes to process")

    # Group by nation
    by_nation = {}
    for torpedo in torpedoes:
        nation = torpedo['country']
        if nation not in by_nation:
            by_nation[nation] = []
        by_nation[nation].append(torpedo)

    # Generate markdown files
    total_created = 0
    for nation, nation_torpedoes in by_nation.items():
        # Create nation directory
        nation_dir = os.path.join(output_base, nation)
        os.makedirs(nation_dir, exist_ok=True)

        print(f"\n{nation}: {len(nation_torpedoes)} torpedoes")

        for torpedo in nation_torpedoes:
            # Generate filename
            designation = torpedo['designation']
            torpedo_id = torpedo['torpedo_id']

            # Use designation for filename
            filename_base = f"{designation}"
            filename = sanitize_filename(filename_base) + ".md"
            filepath = os.path.join(nation_dir, filename)

            # Generate markdown content
            md_content = generate_torpedo_markdown(torpedo)

            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(md_content)

            total_created += 1

    print(f"\n✅ Created {total_created} torpedo markdown files")
    print(f"📁 Location: {output_base}/[Nation]/")

if __name__ == "__main__":
    main()
