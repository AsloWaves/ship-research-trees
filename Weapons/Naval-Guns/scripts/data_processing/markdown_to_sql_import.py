#!/usr/bin/env python3
"""
Parse naval_guns_database.md and generate SQL import script.

This script reads the markdown database export and generates a complete
SQL import script with proper escaping and NULL handling.

Usage:
    python markdown_to_sql_import.py

Output:
    - import_from_markdown.sql (complete import script)
    - import_summary.txt (statistics and validation)
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional


def escape_sql_string(value: str) -> str:
    """Escape single quotes for SQL strings."""
    if value is None:
        return "NULL"
    # Replace single quotes with two single quotes for SQL escaping
    return value.replace("'", "''")


def parse_markdown_value(value: str) -> Optional[str]:
    """Parse markdown cell value, converting empty strings to NULL."""
    value = value.strip()
    if value == "" or value == "NULL" or value.lower() == "null":
        return None
    return value


def parse_table_section(content: str, start_marker: str, end_marker: str) -> List[Dict[str, Optional[str]]]:
    """
    Extract and parse a table section from markdown content.

    Args:
        content: Full markdown content
        start_marker: Section header to find (e.g., "## Guns Table")
        end_marker: Next section header (e.g., "## Ammunition Table")

    Returns:
        List of dictionaries, one per row
    """
    # Find the section
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"Warning: Could not find section '{start_marker}'")
        return []

    # Find the end of section
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        section = content[start_idx:]
    else:
        section = content[start_idx:end_idx]

    # Split into lines
    lines = section.split('\n')

    # Find the header line (starts with |)
    header_line = None
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith('|') and '|' in line[1:]:
            header_line = line
            header_idx = i
            break

    if not header_line:
        print(f"Warning: Could not find table header in section '{start_marker}'")
        return []

    # Parse header columns
    headers = [col.strip() for col in header_line.split('|')[1:-1]]  # Skip first/last empty

    # Skip separator line (the one with dashes)
    data_start_idx = header_idx + 2

    # Parse data rows
    rows = []
    for line in lines[data_start_idx:]:
        line = line.strip()
        if not line or not line.startswith('|'):
            continue
        if line.count('|') < len(headers):
            continue  # Skip malformed lines

        # Split and parse values
        values = [parse_markdown_value(val) for val in line.split('|')[1:-1]]

        # Create row dictionary
        if len(values) == len(headers):
            row = dict(zip(headers, values))
            rows.append(row)

    return rows


def generate_insert_statement(table_name: str, rows: List[Dict[str, Optional[str]]]) -> List[str]:
    """Generate SQL INSERT statements for a table."""
    if not rows:
        return []

    statements = []
    columns = list(rows[0].keys())

    for row in rows:
        # Build values list
        values = []
        for col in columns:
            val = row.get(col)
            if val is None:
                values.append("NULL")
            elif col in ["Gun_ID", "Turret_ID", "ID", "Compatibility_ID", "Ammunition_ID",
                         "Year_Introduced", "Modded", "Crew_Size"]:
                # Integer fields
                values.append(val if val else "NULL")
            elif col in ["Weight", "Weight_LBS", "Length_IN", "Bursting_Charge", "Kinetic_Energy_MJ",
                         "Turret_Weight_Tons", "Armor_Face_IN", "Armor_Sides_IN", "Armor_Roof_IN",
                         "Traverse_Rate_Deg_Sec", "Elevation_Min_Deg", "Elevation_Max_Deg",
                         "Elevation_Rate_Deg_Sec", "Rate_Of_Fire_RPM", "Muzzle_Velocity_FPS",
                         "Muzzle_Velocity_MPS", "Max_Range_Yards", "Barrel_Wear_Per_Round"]:
                # Numeric fields (REAL)
                values.append(val if val else "NULL")
            else:
                # Text fields
                values.append(f"'{escape_sql_string(val)}'")

        # Build INSERT statement
        cols_str = ", ".join(columns)
        vals_str = ", ".join(values)
        statement = f"INSERT INTO {table_name} ({cols_str}) VALUES ({vals_str});"
        statements.append(statement)

    return statements


def main():
    """Main execution function."""
    # Paths
    script_dir = Path(__file__).parent
    db_dir = script_dir.parent.parent / "database"
    md_file = db_dir / "naval_guns_database.md"
    output_sql = db_dir / "sql" / "imports" / "import_from_markdown.sql"
    summary_file = script_dir / "import_summary.txt"

    print("Reading markdown database export...")
    if not md_file.exists():
        print(f"Error: Could not find {md_file}")
        return 1

    content = md_file.read_text(encoding='utf-8')
    print(f"Read {len(content):,} characters from {md_file.name}")

    # Parse each table section
    print("\nParsing tables...")

    guns = parse_table_section(content, "## Guns Table", "## Ammunition Table")
    print(f"  Guns: {len(guns)} records")

    ammunition = parse_table_section(content, "## Ammunition Table", "## Turrets Table")
    print(f"  Ammunition: {len(ammunition)} records")

    turrets = parse_table_section(content, "## Turrets Table", "## Gun Ammunition Compatibility Table")
    print(f"  Turrets: {len(turrets)} records")

    compatibility = parse_table_section(content, "## Gun Ammunition Compatibility Table", "## Data Completeness")
    print(f"  Compatibility: {len(compatibility)} records")

    # Generate SQL statements
    print("\nGenerating SQL statements...")

    sql_statements = []

    # Header comments
    sql_statements.append("-- Import script generated from naval_guns_database.md")
    sql_statements.append("-- Generated by markdown_to_sql_import.py")
    sql_statements.append("--")
    sql_statements.append(f"-- Total records: {len(guns) + len(ammunition) + len(turrets) + len(compatibility)}")
    sql_statements.append(f"--   Guns: {len(guns)}")
    sql_statements.append(f"--   Ammunition: {len(ammunition)}")
    sql_statements.append(f"--   Turrets: {len(turrets)}")
    sql_statements.append(f"--   Compatibility: {len(compatibility)}")
    sql_statements.append("--")
    sql_statements.append("")

    # Performance optimizations
    sql_statements.append("-- Performance optimizations for bulk import")
    sql_statements.append("PRAGMA foreign_keys = OFF;")
    sql_statements.append("BEGIN TRANSACTION;")
    sql_statements.append("")

    # Clear existing data
    sql_statements.append("-- Clear existing data (preserve schema)")
    sql_statements.append("DELETE FROM Gun_Ammunition_Compatibility;")
    sql_statements.append("DELETE FROM Turrets;")
    sql_statements.append("DELETE FROM Ammunition;")
    sql_statements.append("DELETE FROM Guns;")
    sql_statements.append("")

    # Reset auto-increment counters
    sql_statements.append("-- Reset auto-increment counters")
    sql_statements.append("DELETE FROM sqlite_sequence WHERE name IN ('Guns', 'Ammunition', 'Turrets', 'Gun_Ammunition_Compatibility');")
    sql_statements.append("")

    # Insert data in correct order (respect foreign keys)
    sql_statements.append("-- Insert Guns (no foreign key dependencies)")
    sql_statements.extend(generate_insert_statement("Guns", guns))
    sql_statements.append("")

    sql_statements.append("-- Insert Ammunition (no foreign key dependencies)")
    sql_statements.extend(generate_insert_statement("Ammunition", ammunition))
    sql_statements.append("")

    sql_statements.append("-- Insert Turrets (references Guns)")
    sql_statements.extend(generate_insert_statement("Turrets", turrets))
    sql_statements.append("")

    sql_statements.append("-- Insert Gun_Ammunition_Compatibility (references Guns and Ammunition)")
    sql_statements.extend(generate_insert_statement("Gun_Ammunition_Compatibility", compatibility))
    sql_statements.append("")

    # Commit transaction and re-enable foreign keys
    sql_statements.append("-- Commit transaction and re-enable constraints")
    sql_statements.append("COMMIT;")
    sql_statements.append("PRAGMA foreign_keys = ON;")
    sql_statements.append("")

    # Write SQL file
    output_sql.parent.mkdir(parents=True, exist_ok=True)
    with open(output_sql, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_statements))

    print(f"\nGenerated SQL import script: {output_sql}")
    print(f"   Total SQL statements: {len([s for s in sql_statements if s and not s.startswith('--')])}")

    # Write summary
    summary = []
    summary.append("Naval Guns Database - Markdown Import Summary")
    summary.append("=" * 60)
    summary.append("")
    summary.append(f"Source File: {md_file.name}")
    summary.append(f"Output SQL: {output_sql.name}")
    summary.append("")
    summary.append("Records Parsed:")
    summary.append(f"  Guns:           {len(guns):,}")
    summary.append(f"  Ammunition:     {len(ammunition):,}")
    summary.append(f"  Turrets:        {len(turrets):,}")
    summary.append(f"  Compatibility:  {len(compatibility):,}")
    summary.append(f"  TOTAL:          {len(guns) + len(ammunition) + len(turrets) + len(compatibility):,}")
    summary.append("")
    summary.append("Sample Data:")
    if guns:
        summary.append(f"  First Gun: {guns[0].get('Caliber')} {guns[0].get('Mark_Designation')}")
        summary.append(f"  Last Gun:  {guns[-1].get('Caliber')} {guns[-1].get('Mark_Designation')}")
    if ammunition:
        summary.append(f"  First Ammo: {ammunition[0].get('Caliber')} {ammunition[0].get('Mark_Designation')}")
    if turrets:
        summary.append(f"  First Turret: {turrets[0].get('Designation')}")

    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary))

    print(f"Summary written: {summary_file}")
    print("")
    print("Next steps:")
    print(f"   1. Review: {output_sql}")
    print(f"   2. Import: sqlite3 naval_guns.db < {output_sql}")
    print(f"   3. Verify: SELECT COUNT(*) FROM Guns;")

    return 0


if __name__ == "__main__":
    exit(main())
