#!/usr/bin/env python3
"""
Generate markdown files for all aircraft in the database.
Creates individual markdown files organized by nation in Aircraft/[Nation]/ directories.
"""

import sqlite3
import os
from pathlib import Path

# Database path
DB_PATH = Path("Aircraft/aircraft.db")

# Output directory base
OUTPUT_BASE = Path("Aircraft")

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

def generate_aircraft_markdown(aircraft):
    """Generate markdown content for an aircraft."""

    # Extract data
    designation = aircraft['designation'] or "Unknown"
    common_name = aircraft['common_name'] or ""
    nation = aircraft['nation'] or "Unknown"
    manufacturer = aircraft['manufacturer'] or "Unknown"
    primary_role = aircraft['primary_role'] or "Unknown"
    year_introduced = aircraft['year_introduced']
    year_retired = aircraft['year_retired']

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
    tags = [primary_role.lower().replace(" ", "-")]
    if common_name:
        tags.append(common_name.lower().replace(" ", "-"))
    if manufacturer:
        tags.append(manufacturer.lower().replace(" ", "-"))
    tags.append(nation.lower().replace(" ", "-"))
    if aircraft['catapult_compatible'] or aircraft['arresting_hook']:
        tags.append("carrier-based")
    if aircraft['night_capable']:
        tags.append("night-capable")
    if aircraft['radar_equipped']:
        tags.append("radar-equipped")

    # Build YAML frontmatter
    yaml = f"""---
designation: {designation}
common_name: {common_name if common_name else "N/A"}
nation: {nation}
type: {primary_role}
manufacturer: {manufacturer}
introduced: {year_introduced if year_introduced else "Unknown"}
retired: {year_retired if year_retired else "Active"}
service_life: {service_life}
status: {aircraft['aircraft_status'] or 'Production'}
tags: [{', '.join(tags)}]
---

"""

    # Build markdown content
    md = yaml
    md += f"# {title}\n\n"

    # Overview section
    md += "## Overview\n\n"
    md += f"**Nation**: {nation}  \n"
    md += f"**Manufacturer**: {manufacturer}  \n"
    md += f"**Role**: {primary_role}"
    if aircraft['secondary_role']:
        md += f", {aircraft['secondary_role']}"
    md += "  \n"
    md += f"**Service Life**: {service_life}  \n"
    if aircraft['total_produced']:
        md += f"**Total Produced**: {aircraft['total_produced']:,}  \n"
    md += "\n"

    # Physical Specifications
    md += "## Physical Specifications\n\n"
    md += f"- **Length**: {format_value(aircraft['length_ft'], ' ft')}  \n"
    md += f"- **Wingspan**: {format_value(aircraft['wingspan_ft'], ' ft')}"
    if aircraft['wingspan_folded_ft']:
        md += f" ({format_value(aircraft['wingspan_folded_ft'], ' ft')} folded)"
    md += "  \n"
    md += f"- **Height**: {format_value(aircraft['height_ft'], ' ft')}  \n"
    if aircraft['deck_footprint_sq_ft']:
        md += f"- **Deck Footprint**: {format_value(aircraft['deck_footprint_sq_ft'], ' sq ft')}  \n"
    if aircraft['hangar_footprint_sq_ft']:
        md += f"- **Hangar Footprint**: {format_value(aircraft['hangar_footprint_sq_ft'], ' sq ft')}  \n"
    md += f"- **Empty Weight**: {format_value(aircraft['empty_weight_tons'], ' tons')}  \n"
    md += f"- **Max Weight**: {format_value(aircraft['max_weight_tons'], ' tons')}  \n"
    md += "\n"

    # Performance
    md += "## Performance\n\n"
    md += f"- **Cruise Speed**: {format_value(aircraft['cruise_speed_knots'], ' knots')}  \n"
    md += f"- **Max Speed**: {format_value(aircraft['max_speed_knots'], ' knots')}  \n"
    md += f"- **Stall Speed**: {format_value(aircraft['stall_speed_knots'], ' knots')}  \n"
    md += f"- **Service Ceiling**: {format_value(aircraft['service_ceiling_ft'], ' ft')}  \n"
    if aircraft['climb_rate_fpm']:
        md += f"- **Climb Rate**: {format_value(aircraft['climb_rate_fpm'], ' ft/min')}  \n"
    md += f"- **Range**: {format_value(aircraft['range_nm'], ' nm')}  \n"
    if aircraft['ferry_range_nm']:
        md += f"- **Ferry Range**: {format_value(aircraft['ferry_range_nm'], ' nm')}  \n"
    if aircraft['maneuverability_rating']:
        md += f"- **Maneuverability Rating**: {aircraft['maneuverability_rating']}/10  \n"
    md += "\n"

    # Carrier Operations
    carrier_capable = aircraft['catapult_compatible'] or aircraft['arresting_hook']
    if carrier_capable:
        md += "## Carrier Operations\n\n"
        md += f"- **Catapult Compatible**: {format_boolean(aircraft['catapult_compatible'])}  \n"
        md += f"- **Arresting Hook**: {format_boolean(aircraft['arresting_hook'])}  \n"
        if aircraft['arresting_gear_strength_required']:
            md += f"- **Arresting Gear Required**: {aircraft['arresting_gear_strength_required']}  \n"
        if aircraft['min_takeoff_ft_no_catapult']:
            md += f"- **Takeoff Distance (No Catapult)**: {format_value(aircraft['min_takeoff_ft_no_catapult'], ' ft')}  \n"
        if aircraft['min_takeoff_ft_with_catapult']:
            md += f"- **Takeoff Distance (With Catapult)**: {format_value(aircraft['min_takeoff_ft_with_catapult'], ' ft')}  \n"
        if aircraft['min_landing_ft']:
            md += f"- **Landing Distance**: {format_value(aircraft['min_landing_ft'], ' ft')}  \n"
        md += "\n"

    # Armament
    md += "## Armament\n\n"
    if aircraft['gun_armament']:
        md += f"**Guns**: {aircraft['gun_armament']}"
        if aircraft['gun_ammunition_rounds']:
            md += f" ({aircraft['gun_ammunition_rounds']:,} rounds)"
        md += "  \n\n"

    if aircraft['hardpoints']:
        md += f"**Hardpoints**: {aircraft['hardpoints']}  \n"
        md += f"**Max Ordnance Weight**: {format_value(aircraft['max_ordnance_weight_lbs'], ' lbs')}  \n\n"

        md += "**Compatible Ordnance**:  \n"
        if aircraft['bomb_types_compatible']:
            md += f"- Bombs: {aircraft['bomb_types_compatible']}  \n"
        if aircraft['torpedo_compatible']:
            md += "- Torpedoes: Compatible  \n"
        if aircraft['rocket_compatible']:
            md += "- Rockets: Compatible  \n"
        if aircraft['missile_compatible']:
            md += "- Missiles: Compatible  \n"
        md += "\n"

    if aircraft['typical_loadout_description']:
        md += f"**Typical Loadout**: {aircraft['typical_loadout_description']}  \n\n"

    # Crew & Operations
    md += "## Crew & Operations\n\n"
    md += f"- **Crew Size**: {aircraft['crew_size']}  \n"
    if aircraft['crew_positions']:
        md += f"- **Crew Positions**: {aircraft['crew_positions']}  \n"
    md += f"- **Night Capable**: {format_boolean(aircraft['night_capable'])}  \n"
    md += f"- **All-Weather Capable**: {format_boolean(aircraft['all_weather_capable'])}  \n"
    if aircraft['min_visibility_required_miles']:
        md += f"- **Minimum Visibility**: {format_value(aircraft['min_visibility_required_miles'], ' miles')}  \n"
    if aircraft['max_crosswind_knots']:
        md += f"- **Max Crosswind**: {format_value(aircraft['max_crosswind_knots'], ' knots')}  \n"
    md += "\n"

    # Electronics
    if aircraft['radar_equipped'] or aircraft['electronic_warfare']:
        md += "## Electronics & Sensors\n\n"
        if aircraft['radar_equipped']:
            md += f"- **Radar**: {aircraft['radar_type'] or 'Equipped'}"
            if aircraft['radar_range_nm']:
                md += f" ({format_value(aircraft['radar_range_nm'], ' nm')} range)"
            md += "  \n"
        if aircraft['electronic_warfare']:
            md += f"- **Electronic Warfare**: {aircraft['ew_capabilities'] or 'Equipped'}  \n"
        if aircraft['fire_control_generation']:
            md += f"- **Fire Control Generation**: {aircraft['fire_control_generation']}  \n"
        md += "\n"

    # Fuel System
    md += "## Fuel System\n\n"
    md += f"- **Fuel Capacity**: {format_value(aircraft['fuel_capacity_gallons'], ' gallons')}  \n"
    if aircraft['fuel_consumption_cruise_gph']:
        md += f"- **Cruise Consumption**: {format_value(aircraft['fuel_consumption_cruise_gph'], ' gph')}  \n"
    if aircraft['fuel_consumption_combat_gph']:
        md += f"- **Combat Consumption**: {format_value(aircraft['fuel_consumption_combat_gph'], ' gph')}  \n"
    if aircraft['optimal_cruise_altitude_ft']:
        md += f"- **Optimal Cruise Altitude**: {format_value(aircraft['optimal_cruise_altitude_ft'], ' ft')}  \n"
    md += "\n"

    # Game Statistics
    md += "## Game Statistics\n\n"
    md += f"- **Hit Points**: {aircraft['hit_points']}  \n"
    md += f"- **Critical Resistance**: {aircraft['critical_resistance_pct']}%  \n"
    if aircraft['armor_rating']:
        md += f"- **Armor Rating**: {aircraft['armor_rating']}  \n"
    md += f"- **Defense Rating**: {aircraft['defense_rating']}  \n"
    md += f"- **Visibility Rating**: {aircraft['visibility_rating']}  \n"
    md += f"- **Reliability Rating**: {aircraft['reliability_rating']}  \n"
    if aircraft['maintenance_hours_per_flight_hour']:
        md += f"- **Maintenance**: {format_value(aircraft['maintenance_hours_per_flight_hour'], ' hours per flight hour')}  \n"
    md += "\n"

    # Notes
    if aircraft['notes']:
        md += "## Notes\n\n"
        md += f"{aircraft['notes']}\n\n"

    return md

def main():
    """Generate all aircraft markdown files."""

    # Connect to database
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Get all aircraft
    cursor.execute("SELECT * FROM aircraft ORDER BY nation, year_introduced, designation")
    aircraft_list = cursor.fetchall()

    print(f"Found {len(aircraft_list)} aircraft in database")

    # Track statistics
    stats = {}

    # Generate markdown for each aircraft
    for aircraft in aircraft_list:
        nation = aircraft['nation'] or "Unknown"
        designation = aircraft['designation']

        # Create nation directory
        nation_dir = OUTPUT_BASE / nation
        nation_dir.mkdir(exist_ok=True)

        # Create filename
        filename = sanitize_filename(designation) + ".md"
        filepath = nation_dir / filename

        # Generate markdown content
        markdown = generate_aircraft_markdown(aircraft)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        # Update stats
        if nation not in stats:
            stats[nation] = 0
        stats[nation] += 1

        print(f"  Created: {filepath}")

    conn.close()

    # Print summary
    print("\n=== Generation Complete ===")
    print(f"Total aircraft: {len(aircraft_list)}")
    for nation, count in sorted(stats.items()):
        print(f"  {nation}: {count} aircraft")

if __name__ == "__main__":
    main()
