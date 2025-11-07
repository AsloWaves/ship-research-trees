#!/usr/bin/awk -f
# Extract unique ship classes from naval_ships_database.md
# Usage: awk -f extract_ship_classes.awk naval_ships_database.md

BEGIN {
    FS = "|"
}

# Only process lines starting from the actual data table (line 884+)
# Match data rows (start with | followed by number)
NR >= 884 && /^\| [0-9]/ {
    # Extract Ship_Class field (field 4 in actual table)
    ship_class = $4

    # Trim whitespace
    gsub(/^[ \t]+|[ \t]+$/, "", ship_class)

    # Skip empty, very short entries, or header
    if (ship_class != "" && ship_class != "Ship_Class" && length(ship_class) > 2) {
        print ship_class
    }
}
