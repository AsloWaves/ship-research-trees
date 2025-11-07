#!/usr/bin/awk -f
# Analyze data completeness for ships database
# Calculates percentage of fields filled per ship and overall statistics

BEGIN {
    FS = "|"
    total_ships = 0
    total_fields = 20  # Current schema has 20 fields
    sum_filled_percentage = 0
    ships_100_percent = 0

    # Field names for reference
    field_names[1] = "Ship_ID"
    field_names[2] = "Country"
    field_names[3] = "Ship_Name"
    field_names[4] = "Ship_Class"
    field_names[5] = "Hull_Variant"
    field_names[6] = "Ship_Type"
    field_names[7] = "Ship_Type_Full"
    field_names[8] = "Era"
    field_names[9] = "Year_Commissioned"
    field_names[10] = "Year_Designed"
    field_names[11] = "Year_Completed"
    field_names[12] = "Displacement_Standard"
    field_names[13] = "Displacement_Full"
    field_names[14] = "Max_Speed"
    field_names[15] = "Cruise_Speed"
    field_names[16] = "Range_NM"
    field_names[17] = "Cost_USD"
    field_names[18] = "Build_Time"
    field_names[19] = "Modded"
    field_names[20] = "Notes"
}

# Process data rows only (line 884+)
NR >= 884 && /^\| [0-9]/ {
    total_ships++
    filled_count = 0

    # Check each field (columns 2-21, since column 1 is empty due to leading |)
    for (i = 2; i <= 21; i++) {
        field_value = $i
        gsub(/^[ \t]+|[ \t]+$/, "", field_value)

        # Count as filled if not NULL, not empty, and not 0 (for numeric fields that actually have data)
        # Exception: Modded field can legitimately be 0
        if (field_value != "" && field_value != "NULL") {
            if (i == 20) {  # Modded field
                filled_count++
            } else if (field_value != "0") {
                filled_count++
            } else if (field_value == "0" && (i == 2 || i == 10 || i == 11 || i == 15 || i == 18)) {
                # These fields can legitimately be 0
                filled_count++
            }
        }
    }

    # Calculate percentage for this ship
    percentage = (filled_count / total_fields) * 100
    sum_filled_percentage += percentage

    # Track field-level statistics
    for (i = 2; i <= 21; i++) {
        field_value = $i
        gsub(/^[ \t]+|[ \t]+$/, "", field_value)
        if (field_value != "" && field_value != "NULL" && field_value != "0") {
            field_fill_count[i-1]++
        }
    }

    # Count 100% complete ships
    if (filled_count == total_fields) {
        ships_100_percent++
    }

    # Track distribution
    percentage_bucket = int(percentage / 10) * 10
    distribution[percentage_bucket]++
}

END {
    if (total_ships == 0) {
        print "ERROR: No ships found in database!"
        exit 1
    }

    average_filled_percentage = sum_filled_percentage / total_ships
    percent_100_complete = (ships_100_percent / total_ships) * 100

    print "=== SHIPS DATABASE COMPLETENESS ANALYSIS ==="
    print ""
    print "Total Ships Analyzed:", total_ships
    print "Total Fields per Ship:", total_fields
    print ""
    print "--- OVERALL STATISTICS ---"
    printf "Ships with 100%% Complete Data: %d (%.2f%%)\n", ships_100_percent, percent_100_complete
    printf "Average Data Completeness: %.2f%%\n", average_filled_percentage
    print ""

    print "--- COMPLETENESS DISTRIBUTION ---"
    print "Percentage Range | Ship Count | Percentage"
    print "-----------------|------------|------------"
    for (i = 0; i <= 100; i += 10) {
        ship_count = distribution[i]
        if (ship_count > 0) {
            percent_of_total = (ship_count / total_ships) * 100
            printf "%3d%% - %3d%%     | %10d | %6.2f%%\n", i, i+9, ship_count, percent_of_total
        }
    }
    print ""

    print "--- FIELD-LEVEL COMPLETENESS ---"
    print "Field Name              | Filled Count | Fill Rate"
    print "------------------------|--------------|----------"
    for (i = 1; i <= total_fields; i++) {
        filled = field_fill_count[i]
        fill_rate = (filled / total_ships) * 100
        printf "%-23s | %12d | %6.2f%%\n", field_names[i], filled, fill_rate
    }
}
