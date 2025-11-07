#!/usr/bin/env python3
"""
Generate markdown files for all aircraft weapons in the database.
Creates individual markdown files organized by category in Weapons/Aircraft-Weapons/[Category]/ directories.
"""

import sqlite3
import os
from pathlib import Path

# Database path
DB_PATH = Path("Aircraft/aircraft.db")

# Output directory base
OUTPUT_BASE = Path("Weapons/Aircraft-Weapons")

# Category to directory mapping
CATEGORY_DIRS = {
    "Gravity Bomb": "Bombs",
    "Unguided Rocket": "Rockets",
    "IR Missile": "Missiles",
    "Radar Missile": "Missiles",
    "Anti-Radar Missile": "Missiles",
    "Anti-Ship Missile": "Missiles",
    "Laser-Guided Bomb": "Bombs",
    "GPS-Guided Bomb": "Bombs",
    "Torpedo": "Torpedoes",
    "Depth Charge": "Depth-Charges",
    "Naval Mine": "Mines",
    "Practice Munition": "Practice-Munitions"
}

def sanitize_filename(text):
    """Convert text to safe filename."""
    if not text:
        return "Unknown"
    # Replace unsafe characters
    safe = text.replace("/", "-").replace("\\", "-").replace(":", "-")
    safe = safe.replace("*", "").replace("?", "").replace('"', "")
    safe = safe.replace("<", "").replace(">", "").replace("|", "")
    return safe.strip()

def format_value(value, unit="", default="Unknown"):
    """Format a value with optional unit, handling None."""
    if value is None or value == "":
        return default
    if isinstance(value, float):
        return f"{value:,.1f}{unit}"
    if isinstance(value, int):
        return f"{value:,}{unit}"
    return f"{value}{unit}"

def format_boolean(value, true_text="Yes", false_text="No"):
    """Format boolean value."""
    if value is None:
        return "No"
    return true_text if value else false_text

def generate_weapon_markdown(weapon, category_name):
    """Generate markdown content for a weapon."""

    # Extract data
    designation = weapon['designation'] or "Unknown"
    common_name = weapon['common_name'] or ""
    nation = weapon['nation'] or "Unknown"
    year_introduced = weapon['year_introduced']
    year_retired = weapon['year_retired']

    # Build title
    if common_name:
        title = f"{designation} {common_name}"
    else:
        title = designation

    # Build service life
    if year_introduced and year_retired:
        service_life = f"{year_introduced}-{year_retired}"
    elif year_introduced:
        service_life = f"{year_introduced}-Present"
    else:
        service_life = "Unknown"

    # Build tags
    tags = [category_name.lower().replace(" ", "-")]
    if common_name:
        tags.append(common_name.lower().replace(" ", "-"))
    tags.append(nation.lower().replace(" ", "-"))
    if weapon['requires_radar']:
        tags.append("radar-required")
    if weapon['requires_laser_designator']:
        tags.append("laser-guided")
    if weapon['requires_gps']:
        tags.append("gps-guided")

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
common_name: {common_name if common_name else "N/A"}
nation: {nation}
type: {category_name}
introduced: {year_introduced if year_introduced else "Unknown"}
retired: {year_retired if year_retired else "Active"}
service_life: {service_life}
tags: [{', '.join(tags)}]
---

"""

    # Build markdown content
    md = yaml
    md += f"# {title}\n\n"

    # Overview section
    md += "## Overview\n\n"
    md += f"**Nation**: {nation}  \n"
    md += f"**Category**: {category_name}  \n"
    md += f"**Service Life**: {service_life}  \n"
    md += "\n"

    # Physical Specifications
    md += "## Physical Specifications\n\n"
    md += f"- **Weight**: {format_value(weapon['weight_lbs'], ' lbs')}  \n"
    if weapon['length_ft']:
        md += f"- **Length**: {format_value(weapon['length_ft'], ' ft')}  \n"
    if weapon['diameter_inches']:
        md += f"- **Diameter**: {format_value(weapon['diameter_inches'], ' inches')}  \n"
    md += "\n"

    # Guidance & Requirements
    has_requirements = (weapon['requires_radar'] or weapon['requires_targeting_pod'] or
                       weapon['requires_laser_designator'] or weapon['requires_gps'] or
                       weapon['requires_databus'] or weapon['guidance_type'])

    if has_requirements:
        md += "## Guidance & Requirements\n\n"
        if weapon['guidance_type']:
            md += f"**Guidance Type**: {weapon['guidance_type']}  \n\n"

        md += "**Requirements**:  \n"
        if weapon['requires_radar']:
            md += "- Requires Radar  \n"
        if weapon['requires_targeting_pod']:
            md += "- Requires Targeting Pod  \n"
        if weapon['requires_laser_designator']:
            md += "- Requires Laser Designator  \n"
        if weapon['requires_gps']:
            md += "- Requires GPS  \n"
        if weapon['requires_databus']:
            md += "- Requires Databus  \n"
        if weapon['requires_electrical_interface']:
            md += "- Requires Electrical Interface  \n"
        if weapon['min_fire_control_generation']:
            md += f"- Minimum Fire Control Generation: {weapon['min_fire_control_generation']}  \n"
        md += "\n"

    # Performance
    md += "## Performance\n\n"
    if weapon['range_nm']:
        md += f"- **Range**: {format_value(weapon['range_nm'], ' nm')}  \n"
    if weapon['warhead_lbs']:
        md += f"- **Warhead Weight**: {format_value(weapon['warhead_lbs'], ' lbs')}  \n"
    md += f"- **Damage**: {weapon['damage']}  \n"
    md += f"- **Accuracy Rating**: {weapon['accuracy_rating']}/10  \n"
    md += f"- **Reliability Rating**: {weapon['reliability_rating']}/10  \n"
    md += "\n"

    # Compatible Aircraft
    md += "## Compatible Aircraft\n\n"
    md += "See aircraft database for compatibility information.  \n"
    md += "This weapon can be carried by any aircraft with appropriate hardpoints and fire control generation.  \n"
    md += "\n"

    # Notes
    if weapon['notes']:
        md += "## Notes\n\n"
        md += f"{weapon['notes']}\n\n"

    return md

def main():
    """Generate all weapon markdown files."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get category mapping
    cursor.execute("SELECT id, name FROM weapon_categories")
    categories = {row['id']: row['name'] for row in cursor.fetchall()}

    # Get all weapons
    cursor.execute("SELECT * FROM weapons ORDER BY nation, category_id, year_introduced, designation")
    weapons_list = cursor.fetchall()

    print(f"Found {len(weapons_list)} weapons in database")

    # Track statistics
    stats = {}

    # Generate markdown for each weapon
    for weapon in weapons_list:
        nation = weapon['nation'] or "Unknown"
        designation = weapon['designation']
        category_id = weapon['category_id']
        category_name = categories.get(category_id, "Unknown")

        # Get directory for this category
        category_dir_name = CATEGORY_DIRS.get(category_name, "Other")

        # Create category directory
        category_dir = OUTPUT_BASE / category_dir_name
        category_dir.mkdir(parents=True, exist_ok=True)

        # Create filename (include nation for clarity)
        filename = sanitize_filename(f"{nation}-{designation}") + ".md"
        filepath = category_dir / filename

        # Generate markdown content
        markdown = generate_weapon_markdown(weapon, category_name)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Update stats
        key = f"{category_dir_name} ({nation})"
        if key not in stats:
            stats[key] = 0
        stats[key] += 1

        print(f"  Created: {filepath}")

    conn.close()

    # Print summary
    print("\n=== Generation Complete ===")
    print(f"Total weapons: {len(weapons_list)}")
    for key, count in sorted(stats.items()):
        print(f"  {key}: {count} weapons")

if __name__ == "__main__":
    main()
