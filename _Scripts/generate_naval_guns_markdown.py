#!/usr/bin/env python3
"""
Generate markdown files for all naval guns in the database.
Creates individual markdown files organized by nation in Weapons/Naval-Guns/Guns/[Nation]/ directories.
"""

import sqlite3
import os
from pathlib import Path

# Database path
DB_PATH = Path("Weapons/Naval-Guns/database/naval_guns.db")

# Output directory base
OUTPUT_BASE = Path("Weapons/Naval-Guns/Guns")

def sanitize_filename(text):
    """Convert text to safe filename."""
    if not text:
        return "Unknown"
    # Replace unsafe characters
    safe = text.replace("/", "-").replace("\\", "-").replace(":", "-")
    safe = safe.replace("*", "").replace("?", "").replace('"', "inch")
    safe = safe.replace("<", "").replace(">", "").replace("|", "")
    return safe.strip()

def format_value(value, unit="", default="Unknown"):
    """Format a value with optional unit, handling None."""
    if value is None or value == "":
        return default
    if isinstance(value, float):
        return f"{value:,.2f}{unit}"
    if isinstance(value, int):
        return f"{value:,}{unit}"
    return f"{value}{unit}"

def parse_notes(notes):
    """Parse the notes field which contains pipe-separated data."""
    if not notes:
        return {}

    data = {}
    parts = notes.split('|')

    for part in parts:
        part = part.strip()
        if ':' in part:
            key, value = part.split(':', 1)
            data[key.strip()] = value.strip()
        elif part and 'Ships:' not in data.get('description', ''):
            # First part is usually the description
            if 'description' not in data:
                data['description'] = part

    return data

def generate_gun_markdown(gun):
    """Generate markdown content for a naval gun."""

    # Extract data
    gun_id = gun['Gun_ID']
    country = gun['Country'] or "Unknown"
    caliber = gun['Caliber'] or "Unknown"
    length = gun['Length'] or ""
    mark = gun['Mark_Designation'] or ""
    year = gun['Year_Introduced']
    weight = gun['Weight']
    notes = gun['Notes'] or ""

    # Build designation
    if length:
        designation = f"{caliber}{length} {mark}".strip()
    else:
        designation = f"{caliber} {mark}".strip()

    # Parse notes for additional data
    parsed_notes = parse_notes(notes)

    # Build service life
    if year:
        service_life = f"{year}-Present"
    else:
        service_life = "Unknown"

    # Build tags
    tags = []
    tags.append(f"{caliber}".replace('"', 'inch').lower())
    if mark:
        tags.append(mark.lower().replace(" ", "-"))
    tags.append(country.lower())
    tags.append("naval-gun")

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
gun_id: {gun_id}
nation: {country}
caliber: {caliber}
length: {length if length else "N/A"}
mark: {mark if mark else "N/A"}
introduced: {year if year else "Unknown"}
service_life: {service_life}
tags: [{', '.join(tags)}]
---

"""

    # Build markdown content
    md = yaml
    md += f"# {designation}\n\n"

    # Overview section
    md += "## Overview\n\n"
    md += f"**Gun ID**: {gun_id}  \n"
    md += f"**Nation**: {country}  \n"
    md += f"**Caliber**: {caliber}  \n"
    if length:
        md += f"**Length**: {length}  \n"
    md += f"**Mark/Designation**: {mark}  \n"
    if year:
        md += f"**Year Introduced**: {year}  \n"
    md += "\n"

    # Description from notes
    if 'description' in parsed_notes:
        md += "## Description\n\n"
        md += f"{parsed_notes['description']}\n\n"

    # Physical Specifications
    md += "## Physical Specifications\n\n"
    if weight:
        md += f"- **Gun Weight**: {format_value(weight, ' tons')}  \n"

    # Add parsed specifications from notes
    for key in ['Weight', 'Barrel Life', 'Rifling', 'Chamber', 'Barrel Length']:
        if key in parsed_notes:
            md += f"- **{key}**: {parsed_notes[key]}  \n"
    md += "\n"

    # Performance
    if 'Rate of Fire' in parsed_notes or 'Elevation' in parsed_notes:
        md += "## Performance\n\n"
        if 'Rate of Fire' in parsed_notes:
            md += f"- **Rate of Fire**: {parsed_notes['Rate of Fire']}  \n"
        if 'Elevation' in parsed_notes:
            md += f"- **Elevation**: {parsed_notes['Elevation']}  \n"
        md += "\n"

    # Ships that used this gun
    if 'Ships' in parsed_notes:
        md += "## Ships\n\n"
        md += f"**Used on**: {parsed_notes['Ships']}\n\n"

    # Compatible Ammunition
    md += "## Compatible Ammunition\n\n"
    md += "See ammunition database for compatible shells for this caliber.  \n"
    md += f"Caliber: {caliber}  \n\n"

    # Source/Reference
    if 'Source' in parsed_notes:
        md += "## References\n\n"
        md += f"- {parsed_notes['Source']}\n\n"

    # Additional Notes
    remaining_notes = []
    for key, value in parsed_notes.items():
        if key not in ['description', 'Weight', 'Barrel Life', 'Rifling', 'Chamber',
                       'Barrel Length', 'Rate of Fire', 'Elevation', 'Ships', 'Source']:
            remaining_notes.append(f"**{key}**: {value}")

    if remaining_notes:
        md += "## Additional Information\n\n"
        for note in remaining_notes:
            md += f"{note}  \n"
        md += "\n"

    return md

def main():
    """Generate all gun markdown files."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all guns
    cursor.execute("SELECT * FROM Guns ORDER BY Country, Year_Introduced, Caliber")
    guns_list = cursor.fetchall()

    print(f"Found {len(guns_list)} guns in database")

    # Track statistics
    stats = {}

    # Generate markdown for each gun
    for gun in guns_list:
        country = gun['Country'] or "Unknown"
        caliber = gun['Caliber'] or "Unknown"
        mark = gun['Mark_Designation'] or ""
        length = gun['Length'] or ""

        # Create nation directory
        nation_dir = OUTPUT_BASE / country
        nation_dir.mkdir(parents=True, exist_ok=True)

        # Create filename
        if length:
            filename_base = f"{caliber}{length}-{mark}"
        else:
            filename_base = f"{caliber}-{mark}"

        filename = sanitize_filename(filename_base) + ".md"
        filepath = nation_dir / filename

        # Generate markdown content
        markdown = generate_gun_markdown(gun)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Update stats
        if country not in stats:
            stats[country] = 0
        stats[country] += 1

        print(f"  Created: {filepath}")

    conn.close()

    # Print summary
    print("\n=== Generation Complete ===")
    print(f"Total guns: {len(guns_list)}")
    for country, count in sorted(stats.items()):
        print(f"  {country}: {count} guns")

if __name__ == "__main__":
    main()
