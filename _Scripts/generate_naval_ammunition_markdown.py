#!/usr/bin/env python3
"""
Generate markdown files for all naval ammunition in the database.
Creates individual markdown files organized by nation in Weapons/Naval-Guns/Ammunition/[Nation]/ directories.
"""

import sqlite3
import os
from pathlib import Path

# Database path
DB_PATH = Path("Weapons/Naval-Guns/database/naval_guns.db")

# Output directory base
OUTPUT_BASE = Path("Weapons/Naval-Guns/Ammunition")

# Projectile type descriptions
PROJECTILE_TYPES = {
    "AP": "Armor-Piercing",
    "HC": "High Capacity",
    "HE": "High Explosive",
    "SAP": "Semi-Armor-Piercing",
    "Common": "Common Shell",
    "Illumination": "Illumination Round",
    "Practice": "Practice Round"
}

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

def generate_ammunition_markdown(ammo):
    """Generate markdown content for ammunition."""

    # Extract data
    ammo_id = ammo['Ammunition_ID']
    country = ammo['Country'] or "Unknown"
    caliber = ammo['Caliber'] or "Unknown"
    mark = ammo['Mark_Designation'] or ""
    projectile_type = ammo['Projectile_Type'] or "Unknown"
    weight = ammo['Weight_LBS']
    length = ammo['Length_IN']
    bursting_charge = ammo['Bursting_Charge']
    kinetic_energy = ammo['Kinetic_Energy_MJ']
    cartridge_type = ammo['Cartridge_Type'] or ""
    year = ammo['Year_Introduced']
    notes = ammo['Notes'] or ""

    # Build designation
    designation = f"{caliber} {mark} ({projectile_type})".strip()

    # Get projectile type full name
    projectile_full = PROJECTILE_TYPES.get(projectile_type, projectile_type)

    # Build service life
    if year:
        service_life = f"{year}-Present"
    else:
        service_life = "Unknown"

    # Build tags
    tags = []
    tags.append(f"{caliber}".replace('"', 'inch').lower())
    tags.append(projectile_type.lower())
    if mark:
        tags.append(mark.lower().replace(" ", "-"))
    tags.append(country.lower())
    tags.append("ammunition")

    # Build YAML frontmatter
    yaml = f"""---
designation: {caliber} {mark}
ammunition_id: {ammo_id}
nation: {country}
caliber: {caliber}
mark: {mark if mark else "N/A"}
projectile_type: {projectile_type}
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
    md += f"**Ammunition ID**: {ammo_id}  \n"
    md += f"**Nation**: {country}  \n"
    md += f"**Caliber**: {caliber}  \n"
    md += f"**Mark/Designation**: {mark}  \n"
    md += f"**Projectile Type**: {projectile_full} ({projectile_type})  \n"
    if year:
        md += f"**Year Introduced**: {year}  \n"
    if cartridge_type:
        md += f"**Cartridge Type**: {cartridge_type}  \n"
    md += "\n"

    # Physical Specifications
    md += "## Physical Specifications\n\n"
    if weight:
        md += f"- **Projectile Weight**: {format_value(weight, ' lbs')}  \n"
    if length:
        md += f"- **Length**: {format_value(length, ' inches')}  \n"
    if bursting_charge:
        md += f"- **Bursting Charge**: {format_value(bursting_charge, ' lbs')}  \n"
    md += "\n"

    # Performance
    md += "## Performance\n\n"
    if kinetic_energy:
        md += f"- **Kinetic Energy**: {format_value(kinetic_energy, ' MJ')}  \n"

    # Calculate bursting charge percentage if we have both values
    if weight and bursting_charge and weight > 0:
        bc_pct = (bursting_charge / weight) * 100
        md += f"- **Bursting Charge %**: {bc_pct:.1f}%  \n"

    md += "\n"

    # Compatible Guns
    md += "## Compatible Guns\n\n"
    md += f"This ammunition is compatible with naval guns of {caliber} caliber.  \n"
    md += "See guns database for detailed compatibility information.  \n\n"

    # Notes
    if notes:
        md += "## Notes\n\n"
        md += f"{notes}\n\n"

    return md

def main():
    """Generate all ammunition markdown files."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all ammunition
    cursor.execute("SELECT * FROM Ammunition ORDER BY Country, Caliber, Projectile_Type, Mark_Designation")
    ammo_list = cursor.fetchall()

    print(f"Found {len(ammo_list)} ammunition types in database")

    # Track statistics
    stats = {}

    # Generate markdown for each ammunition
    for ammo in ammo_list:
        country = ammo['Country'] or "Unknown"
        caliber = ammo['Caliber'] or "Unknown"
        mark = ammo['Mark_Designation'] or ""
        proj_type = ammo['Projectile_Type'] or "Unknown"

        # Create nation directory
        nation_dir = OUTPUT_BASE / country
        nation_dir.mkdir(parents=True, exist_ok=True)

        # Create filename
        filename_base = f"{caliber}-{mark}-{proj_type}"
        filename = sanitize_filename(filename_base) + ".md"
        filepath = nation_dir / filename

        # Generate markdown content
        markdown = generate_ammunition_markdown(ammo)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Update stats
        key = f"{country} ({proj_type})"
        if key not in stats:
            stats[key] = 0
        stats[key] += 1

        print(f"  Created: {filepath}")

    conn.close()

    # Print summary
    print("\n=== Generation Complete ===")
    print(f"Total ammunition types: {len(ammo_list)}")
    for key, count in sorted(stats.items()):
        print(f"  {key}: {count} types")

if __name__ == "__main__":
    main()
