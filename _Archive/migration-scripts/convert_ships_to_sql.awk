#!/usr/bin/awk -f
# ============================================================================
# NAVAL SHIPS MD → SQL CONVERSION SCRIPT
# ============================================================================
# Purpose: Convert naval_ships_database.md to SQL INSERT statements
# Input: naval_ships_database.md (pipe-delimited table)
# Output: insert_ships.sql (SQL INSERT statements)
# Schema: 20 fields matching COMPLETE_SQL_SCHEMA.sql naval_ships table
# ============================================================================

BEGIN {
    FS = "|"
    OFS = ""

    # SQL file header
    print "-- ============================================================================"
    print "-- NAVAL SHIPS DATA IMPORT"
    print "-- ============================================================================"
    print "-- Generated from: naval_ships_database.md"
    print "-- Target table: naval_ships"
    print "-- Field count: 20"
    print "-- ID Range: 12000-13999"
    print "-- ============================================================================"
    print ""
    print "-- Begin transaction for performance"
    print "BEGIN TRANSACTION;"
    print ""

    # Track statistics
    ship_count = 0
    error_count = 0
}

# Process data rows only (line 884+)
NR >= 884 && /^\| [0-9]/ {
    ship_count++

    # Extract and trim all fields
    ship_id = $2
    country = $3
    ship_name = $4
    ship_class = $5
    hull_variant = $6
    ship_type = $7
    ship_type_full = $8
    era = $9
    year_commissioned = $10
    year_designed = $11
    year_completed = $12
    displacement_standard = $13
    displacement_full = $14
    max_speed = $15
    cruise_speed = $16
    range_nm = $17
    cost_usd = $18
    build_time = $19
    modded = $20
    notes = $21

    # Trim whitespace from all fields
    gsub(/^[ \t]+|[ \t]+$/, "", ship_id)
    gsub(/^[ \t]+|[ \t]+$/, "", country)
    gsub(/^[ \t]+|[ \t]+$/, "", ship_name)
    gsub(/^[ \t]+|[ \t]+$/, "", ship_class)
    gsub(/^[ \t]+|[ \t]+$/, "", hull_variant)
    gsub(/^[ \t]+|[ \t]+$/, "", ship_type)
    gsub(/^[ \t]+|[ \t]+$/, "", ship_type_full)
    gsub(/^[ \t]+|[ \t]+$/, "", era)
    gsub(/^[ \t]+|[ \t]+$/, "", year_commissioned)
    gsub(/^[ \t]+|[ \t]+$/, "", year_designed)
    gsub(/^[ \t]+|[ \t]+$/, "", year_completed)
    gsub(/^[ \t]+|[ \t]+$/, "", displacement_standard)
    gsub(/^[ \t]+|[ \t]+$/, "", displacement_full)
    gsub(/^[ \t]+|[ \t]+$/, "", max_speed)
    gsub(/^[ \t]+|[ \t]+$/, "", cruise_speed)
    gsub(/^[ \t]+|[ \t]+$/, "", range_nm)
    gsub(/^[ \t]+|[ \t]+$/, "", cost_usd)
    gsub(/^[ \t]+|[ \t]+$/, "", build_time)
    gsub(/^[ \t]+|[ \t]+$/, "", modded)
    gsub(/^[ \t]+|[ \t]+$/, "", notes)

    # Validate Ship_ID
    if (ship_id == "" || ship_id == "Ship_ID") {
        error_count++
        print "-- ERROR: Invalid Ship_ID at line " NR > "/dev/stderr"
        next
    }

    # Build INSERT statement
    printf "INSERT INTO naval_ships ("
    printf "Ship_ID, Country, Ship_Name, Ship_Class, Hull_Variant, "
    printf "Ship_Type, Ship_Type_Full, Era, Year_Commissioned, Year_Designed, "
    printf "Year_Completed, Displacement_Standard, Displacement_Full, Max_Speed, "
    printf "Cruise_Speed, Range_NM, Cost_USD, Build_Time, Modded, Notes"
    printf ") VALUES ("

    # Ship_ID (integer)
    printf "%s, ", ship_id

    # Country (text - quoted)
    printf "'%s', ", sql_escape(country)

    # Ship_Name (text - quoted)
    printf "'%s', ", sql_escape(ship_name)

    # Ship_Class (text - quoted)
    printf "'%s', ", sql_escape(ship_class)

    # Hull_Variant (text - quoted or NULL)
    if (hull_variant == "" || hull_variant == "NULL") {
        printf "NULL, "
    } else {
        printf "'%s', ", sql_escape(hull_variant)
    }

    # Ship_Type (text - quoted)
    printf "'%s', ", sql_escape(ship_type)

    # Ship_Type_Full (text - quoted or NULL)
    if (ship_type_full == "" || ship_type_full == "NULL") {
        printf "NULL, "
    } else {
        printf "'%s', ", sql_escape(ship_type_full)
    }

    # Era (text - quoted)
    printf "'%s', ", sql_escape(era)

    # Year_Commissioned (integer or NULL)
    if (year_commissioned == "" || year_commissioned == "NULL" || year_commissioned == "0") {
        printf "NULL, "
    } else {
        printf "%s, ", year_commissioned
    }

    # Year_Designed (integer or NULL)
    if (year_designed == "" || year_designed == "NULL" || year_designed == "0") {
        printf "NULL, "
    } else {
        printf "%s, ", year_designed
    }

    # Year_Completed (integer or NULL)
    if (year_completed == "" || year_completed == "NULL" || year_completed == "0") {
        printf "NULL, "
    } else {
        printf "%s, ", year_completed
    }

    # Displacement_Standard (real)
    if (displacement_standard == "" || displacement_standard == "NULL") {
        printf "NULL, "
    } else {
        printf "%s, ", displacement_standard
    }

    # Displacement_Full (real)
    if (displacement_full == "" || displacement_full == "NULL") {
        printf "NULL, "
    } else {
        printf "%s, ", displacement_full
    }

    # Max_Speed (real)
    if (max_speed == "" || max_speed == "NULL") {
        printf "NULL, "
    } else {
        printf "%s, ", max_speed
    }

    # Cruise_Speed (real or NULL)
    if (cruise_speed == "" || cruise_speed == "NULL" || cruise_speed == "0") {
        printf "NULL, "
    } else {
        printf "%s, ", cruise_speed
    }

    # Range_NM (real)
    if (range_nm == "" || range_nm == "NULL") {
        printf "NULL, "
    } else {
        printf "%s, ", range_nm
    }

    # Cost_USD (real or NULL)
    if (cost_usd == "" || cost_usd == "NULL" || cost_usd == "0") {
        printf "NULL, "
    } else {
        printf "%s, ", cost_usd
    }

    # Build_Time (real or NULL)
    if (build_time == "" || build_time == "NULL" || build_time == "0") {
        printf "NULL, "
    } else {
        printf "%s, ", build_time
    }

    # Modded (integer - 0 or 1)
    if (modded == "" || modded == "NULL") {
        printf "0, "
    } else {
        printf "%s, ", modded
    }

    # Notes (text - quoted or NULL)
    if (notes == "" || notes == "NULL") {
        printf "NULL"
    } else {
        printf "'%s'", sql_escape(notes)
    }

    printf ");\n"

    # Print progress every 100 ships
    if (ship_count % 100 == 0) {
        print "-- Processed " ship_count " ships..." > "/dev/stderr"
    }
}

END {
    # Commit transaction
    print ""
    print "-- Commit transaction"
    print "COMMIT;"
    print ""

    # Statistics
    print "-- ============================================================================"
    print "-- IMPORT STATISTICS"
    print "-- ============================================================================"
    print "-- Total ships processed: " ship_count
    print "-- Errors encountered: " error_count
    print "-- Success rate: " sprintf("%.2f%%", (ship_count - error_count) / ship_count * 100)
    print "-- ============================================================================"

    # stderr summary
    print "" > "/dev/stderr"
    print "=== CONVERSION COMPLETE ===" > "/dev/stderr"
    print "Ships processed: " ship_count > "/dev/stderr"
    print "Errors: " error_count > "/dev/stderr"
    print "" > "/dev/stderr"
}

# Function to escape single quotes for SQL
function sql_escape(str) {
    # Escape single quotes by doubling them
    gsub(/'/, "''", str)
    # Remove any problematic characters
    gsub(/[\x00-\x08\x0B-\x0C\x0E-\x1F]/, "", str)
    return str
}
