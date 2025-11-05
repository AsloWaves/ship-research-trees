#!/usr/bin/env python3
"""
Export naval_guns.db to SQL import script with proper formatting.

This script directly queries the SQLite database and generates clean
SQL INSERT statements with proper escaping.

Usage:
    python export_database_to_sql.py

Output:
    - reimport_database.sql (complete clean import script)
"""

import sqlite3
from pathlib import Path
from typing import List, Tuple, Any


def escape_sql_value(value: Any) -> str:
    """Convert Python value to SQL literal."""
    if value is None:
        return "NULL"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        # Escape single quotes by doubling them
        escaped = value.replace("'", "''")
        return f"'{escaped}'"
    else:
        return f"'{str(value)}'"


def generate_insert_statements(conn: sqlite3.Connection, table_name: str) -> List[str]:
    """Generate INSERT statements for a table."""
    cursor = conn.cursor()

    # Get column names
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]
    cols_str = ", ".join(columns)

    # Get all data
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    statements = []
    for row in rows:
        values = [escape_sql_value(val) for val in row]
        vals_str = ", ".join(values)
        stmt = f"INSERT INTO {table_name} ({cols_str}) VALUES ({vals_str});"
        statements.append(stmt)

    return statements


def main():
    """Main execution function."""
    # Paths
    script_dir = Path(__file__).parent
    db_dir = script_dir.parent.parent / "database"
    db_file = db_dir / "naval_guns.db"
    output_sql = db_dir / "sql" / "imports" / "reimport_database.sql"

    print("Exporting database to SQL...")
    print(f"Source: {db_file}")

    if not db_file.exists():
        print(f"Error: Database not found at {db_file}")
        return 1

    # Connect to database
    conn = sqlite3.Connection(db_file)
    cursor = conn.cursor()

    # Get record counts
    cursor.execute("SELECT COUNT(*) FROM Guns")
    guns_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Ammunition")
    ammo_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Turrets")
    turrets_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM Gun_Ammunition_Compatibility")
    compat_count = cursor.fetchone()[0]

    print(f"\nDatabase contents:")
    print(f"  Guns:           {guns_count}")
    print(f"  Ammunition:     {ammo_count}")
    print(f"  Turrets:        {turrets_count}")
    print(f"  Compatibility:  {compat_count}")
    print(f"  TOTAL:          {guns_count + ammo_count + turrets_count + compat_count}")

    # Generate SQL statements
    print("\nGenerating SQL statements...")

    sql_statements = []

    # Header
    sql_statements.append("-- Naval Guns Database - Complete Re-Import Script")
    sql_statements.append("-- Generated from naval_guns.db")
    sql_statements.append("-- This script clears and repopulates all tables")
    sql_statements.append("--")
    sql_statements.append(f"-- Total records: {guns_count + ammo_count + turrets_count + compat_count}")
    sql_statements.append(f"--   Guns:           {guns_count}")
    sql_statements.append(f"--   Ammunition:     {ammo_count}")
    sql_statements.append(f"--   Turrets:        {turrets_count}")
    sql_statements.append(f"--   Compatibility:  {compat_count}")
    sql_statements.append("--")
    sql_statements.append("")

    # Clear existing data
    sql_statements.append("-- Clear existing data (preserve schema)")
    sql_statements.append("PRAGMA foreign_keys = OFF;")
    sql_statements.append("DELETE FROM Gun_Ammunition_Compatibility;")
    sql_statements.append("DELETE FROM Turrets;")
    sql_statements.append("DELETE FROM Ammunition;")
    sql_statements.append("DELETE FROM Guns;")
    sql_statements.append("")

    # Reset auto-increment
    sql_statements.append("-- Reset auto-increment counters")
    sql_statements.append("DELETE FROM sqlite_sequence WHERE name IN ('Guns', 'Ammunition', 'Turrets', 'Gun_Ammunition_Compatibility');")
    sql_statements.append("")

    # Insert data in dependency order
    print("  Exporting Guns...")
    sql_statements.append("-- Insert Guns")
    sql_statements.extend(generate_insert_statements(conn, "Guns"))
    sql_statements.append("")

    print("  Exporting Ammunition...")
    sql_statements.append("-- Insert Ammunition")
    sql_statements.extend(generate_insert_statements(conn, "Ammunition"))
    sql_statements.append("")

    print("  Exporting Turrets...")
    sql_statements.append("-- Insert Turrets")
    sql_statements.extend(generate_insert_statements(conn, "Turrets"))
    sql_statements.append("")

    print("  Exporting Compatibility...")
    sql_statements.append("-- Insert Gun_Ammunition_Compatibility")
    sql_statements.extend(generate_insert_statements(conn, "Gun_Ammunition_Compatibility"))
    sql_statements.append("")

    # Re-enable foreign keys
    sql_statements.append("-- Re-enable foreign key constraints")
    sql_statements.append("PRAGMA foreign_keys = ON;")
    sql_statements.append("")

    # Write to file
    output_sql.parent.mkdir(parents=True, exist_ok=True)
    with open(output_sql, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sql_statements))

    print(f"\nGenerated: {output_sql}")
    print(f"Total SQL statements: {len([s for s in sql_statements if s and not s.startswith('--')])}")
    print("\nNext steps:")
    print(f"  1. Review: {output_sql.name}")
    print(f"  2. Import: sqlite3 naval_guns.db < {output_sql.name}")
    print(f"  3. Verify: SELECT COUNT(*) FROM Guns;")

    conn.close()
    return 0


if __name__ == "__main__":
    exit(main())
