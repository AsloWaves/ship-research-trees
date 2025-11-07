#!/usr/bin/env python3
"""
Generate markdown files for all naval turrets in the database.
Creates individual markdown files organized by nation in Weapons/Naval-Guns/Turrets/[Nation]/ directories.
"""

import sqlite3
import os
from pathlib import Path

# Database path
DB_PATH = Path("Weapons/Naval-Guns/database/naval_guns.db")

# Output directory base
OUTPUT_BASE = Path("Weapons/Naval-Guns/Turrets")

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

def generate_turret_markdown(turret):
    """Generate markdown content for a turret."""

    # Extract data
    turret_id = turret['Turret_ID']
    gun_id = turret['Gun_ID']
    country = turret['Country'] or "Unknown"
    caliber = turret['Caliber'] or "Unknown"
    turret_type = turret['Turret_Type'] or "Unknown"
    designation = turret['Designation'] or f"{caliber} {turret_type} Turret"
    weight = turret['Turret_Weight_Tons']
    crew = turret['Crew_Size']
    armor_face = turret['Armor_Face_IN']
    armor_sides = turret['Armor_Sides_IN']
    armor_roof = turret['Armor_Roof_IN']
    traverse_rate = turret['Traverse_Rate_Deg_Sec']
    elev_min = turret['Elevation_Min_Deg']
    elev_max = turret['Elevation_Max_Deg']
    elev_rate = turret['Elevation_Rate_Deg_Sec']
    rof = turret['Rate_Of_Fire_RPM']
    notes = turret['Notes'] or ""

    # Build service life (would need year data)
    service_life = "Unknown"

    # Build tags
    tags = []
    tags.append(f"{caliber}".replace('"', 'inch').lower())
    tags.append(turret_type.lower().replace(" ", "-"))
    tags.append(country.lower())
    tags.append("turret")

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
turret_id: {turret_id}
gun_id: {gun_id if gun_id else "N/A"}
nation: {country}
caliber: {caliber}
turret_type: {turret_type}
tags: [{', '.join(tags)}]
---

"""

    # Build markdown content
    md = yaml
    md += f"# {designation}\n\n"

    # Overview section
    md += "## Overview\n\n"
    md += f"**Turret ID**: {turret_id}  \n"
    if gun_id:
        md += f"**Gun ID**: {gun_id} (See Guns database)  \n"
    md += f"**Nation**: {country}  \n"
    md += f"**Caliber**: {caliber}  \n"
    md += f"**Turret Type**: {turret_type}  \n"
    md += "\n"

    # Physical Specifications
    md += "## Physical Specifications\n\n"
    if weight:
        md += f"- **Turret Weight**: {format_value(weight, ' tons')}  \n"
    if crew:
        md += f"- **Crew Size**: {crew} personnel  \n"
    md += "\n"

    # Armor Protection
    has_armor = armor_face or armor_sides or armor_roof
    if has_armor:
        md += "## Armor Protection\n\n"
        if armor_face:
            md += f"- **Face Armor**: {format_value(armor_face, ' inches')}  \n"
        if armor_sides:
            md += f"- **Side Armor**: {format_value(armor_sides, ' inches')}  \n"
        if armor_roof:
            md += f"- **Roof Armor**: {format_value(armor_roof, ' inches')}  \n"
        md += "\n"

    # Performance
    md += "## Performance\n\n"
    if traverse_rate:
        md += f"- **Traverse Rate**: {format_value(traverse_rate, ' °/sec')}  \n"
    if elev_min is not None and elev_max is not None:
        md += f"- **Elevation Range**: {format_value(elev_min, '°')} to {format_value(elev_max, '°')}  \n"
    elif elev_max is not None:
        md += f"- **Maximum Elevation**: {format_value(elev_max, '°')}  \n"
    if elev_rate:
        md += f"- **Elevation Rate**: {format_value(elev_rate, ' °/sec')}  \n"
    if rof:
        md += f"- **Rate of Fire**: {format_value(rof, ' rounds/min')}  \n"
    md += "\n"

    # Associated Gun
    md += "## Associated Gun\n\n"
    if gun_id:
        md += f"This turret is associated with Gun ID {gun_id}.  \n"
        md += f"See the Guns database for specifications of the {caliber} gun.  \n"
    else:
        md += f"This turret houses {caliber} naval guns.  \n"
        md += "See the Guns database for compatible gun specifications.  \n"
    md += "\n"

    # Compatible Ammunition
    md += "## Compatible Ammunition\n\n"
    md += f"Uses ammunition for {caliber} caliber guns.  \n"
    md += "See the Ammunition database for compatible shells.  \n\n"

    # Notes
    if notes:
        md += "## Notes\n\n"
        md += f"{notes}\n\n"

    return md

def main():
    """Generate all turret markdown files."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all turrets
    cursor.execute("SELECT * FROM Turrets ORDER BY Country, Caliber, Turret_Type, Designation")
    turrets_list = cursor.fetchall()

    print(f"Found {len(turrets_list)} turrets in database")

    # Track statistics
    stats = {}

    # Generate markdown for each turret
    for i, turret in enumerate(turrets_list, 1):
        country = turret['Country'] or "Unknown"
        caliber = turret['Caliber'] or "Unknown"
        turret_type = turret['Turret_Type'] or "Unknown"
        designation = turret['Designation'] or f"{caliber} {turret_type}"
        turret_id = turret['Turret_ID']

        # Create nation directory
        nation_dir = OUTPUT_BASE / country
        nation_dir.mkdir(parents=True, exist_ok=True)

        # Create filename - use turret ID to ensure uniqueness
        filename_base = f"{turret_id}-{caliber}-{turret_type}"
        filename = sanitize_filename(filename_base) + ".md"
        filepath = nation_dir / filename

        # Generate markdown content
        markdown = generate_turret_markdown(turret)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Update stats
        key = f"{country}"
        if key not in stats:
            stats[key] = 0
        stats[key] += 1

        # Progress indicator every 100 turrets
        if i % 100 == 0:
            print(f"  Progress: {i}/{len(turrets_list)} turrets ({(i/len(turrets_list)*100):.1f}%)")

    conn.close()

    # Print summary
    print("\n=== Generation Complete ===")
    print(f"Total turrets: {len(turrets_list)}")
    for key, count in sorted(stats.items()):
        print(f"  {key}: {count} turrets")

if __name__ == "__main__":
    main()
