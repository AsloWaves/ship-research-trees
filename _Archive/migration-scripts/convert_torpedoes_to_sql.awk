#!/usr/bin/awk -f
# ============================================================================
# NAVAL TORPEDOES MD → SQL CONVERSION SCRIPT
# ============================================================================
# Purpose: Convert naval_torpedoes_database.md to SQL INSERT statements
# Input: naval_torpedoes_database.md (pipe-delimited table)
# Output: insert_torpedoes.sql (SQL INSERT statements)
# Schema: 18 fields matching COMPLETE_SQL_SCHEMA.sql naval_torpedoes table
# ============================================================================

BEGIN {
    FS = "|"
    print "-- ============================================================================"
    print "-- NAVAL TORPEDOES DATA IMPORT"
    print "-- ============================================================================"
    print "BEGIN TRANSACTION;"
    print ""
    record_count = 0
}

# Skip header rows and process data
NR > 2 && /^\| [0-9]/ {
    record_count++

    # Extract fields (adjust column numbers based on actual data)
    torpedo_id = $2
    country = $3
    torpedo_name = $4
    designation = $5
    torpedo_type = $6
    era = $7
    year_introduced = $8
    diameter_in = $9
    length_ft = $10
    weight_lbs = $11
    warhead_lbs = $12
    speed_kts = $13
    range_yds = $14
    depth_ft = $15
    propulsion = $16
    guidance = $17
    modded = $18
    notes = $19

    # Trim whitespace
    for (i = 2; i <= 19; i++) {
        gsub(/^[ \t]+|[ \t]+$/, "", $i)
    }

    # Build INSERT statement
    printf "INSERT INTO naval_torpedoes VALUES ("
    printf "%s, ", torpedo_id
    printf "'%s', ", sql_escape(country)
    printf "'%s', ", sql_escape(torpedo_name)
    printf "%s, ", sql_null_or_quote(designation)
    printf "%s, ", sql_null_or_quote(torpedo_type)
    printf "%s, ", sql_null_or_quote(era)
    printf "%s, ", sql_null_or_int(year_introduced)
    printf "%s, ", sql_null_or_num(diameter_in)
    printf "%s, ", sql_null_or_num(length_ft)
    printf "%s, ", sql_null_or_num(weight_lbs)
    printf "%s, ", sql_null_or_num(warhead_lbs)
    printf "%s, ", sql_null_or_num(speed_kts)
    printf "%s, ", sql_null_or_num(range_yds)
    printf "%s, ", sql_null_or_num(depth_ft)
    printf "%s, ", sql_null_or_quote(propulsion)
    printf "%s, ", sql_null_or_quote(guidance)
    printf "%s, ", (modded == "" || modded == "NULL") ? "0" : modded
    printf "%s", sql_null_or_quote(notes)
    printf ");\n"
}

END {
    print ""
    print "COMMIT;"
    print "-- Total torpedoes processed: " record_count
}

function sql_escape(str) {
    gsub(/'/, "''", str)
    gsub(/[\x00-\x08\x0B-\x0C\x0E-\x1F]/, "", str)
    return str
}

function sql_null_or_quote(val) {
    gsub(/^[ \t]+|[ \t]+$/, "", val)
    if (val == "" || val == "NULL") return "NULL"
    return "'" sql_escape(val) "'"
}

function sql_null_or_num(val) {
    gsub(/^[ \t]+|[ \t]+$/, "", val)
    if (val == "" || val == "NULL" || val == "0") return "NULL"
    return val
}

function sql_null_or_int(val) {
    gsub(/^[ \t]+|[ \t]+$/, "", val)
    if (val == "" || val == "NULL") return "NULL"
    return int(val)
}
