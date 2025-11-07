BEGIN {
    FS = "|"
    OFS = "|"
    print "# Processing ships from research tree database..."
}

/^\| [0-9]/ {
    # Extract and trim fields
    node_id = $2; gsub(/^[ \t]+|[ \t]+$/, "", node_id)
    country = $3; gsub(/^[ \t]+|[ \t]+$/, "", country)

    # Skip prerequisite/relationship entries (they have numbers in country field)
    if (country ~ /^[0-9]+$/) next
    ship_class = $4; gsub(/^[ \t]+|[ \t]+$/, "", ship_class)
    ship_type = $5; gsub(/^[ \t]+|[ \t]+$/, "", ship_type)
    tech_branch = $6; gsub(/^[ \t]+|[ \t]+$/, "", tech_branch)
    tech_tier = $7; gsub(/^[ \t]+|[ \t]+$/, "", tech_tier)
    era = $8; gsub(/^[ \t]+|[ \t]+$/, "", era)
    year = $9; gsub(/^[ \t]+|[ \t]+$/, "", year)
    is_starting = $10; gsub(/^[ \t]+|[ \t]+$/, "", is_starting)
    cost = $13; gsub(/^[ \t]+|[ \t]+$/, "", cost)
    build_time = $14; gsub(/^[ \t]+|[ \t]+$/, "", build_time)
    design = $15; gsub(/^[ \t]+|[ \t]+$/, "", design)
    notes = $18; gsub(/^[ \t]+|[ \t]+$/, "", notes)
    
    # Estimate displacement based on type and year
    disp = 10000
    if (ship_type == "BB") {
        if (year < 1906) disp = 12000
        else if (year < 1915) disp = 20000
        else if (year < 1922) disp = 32000
        else if (year < 1936) disp = 35000
        else if (year < 1945) disp = 45000
        else disp = 50000
    } else if (ship_type == "CV") {
        if (year < 1930) disp = 25000
        else if (year < 1940) disp = 30000
        else if (year < 1945) disp = 35000
        else if (year < 1960) disp = 45000
        else disp = 90000
    } else if (ship_type == "CA") {
        if (year < 1920) disp = 10000
        else if (year < 1945) disp = 13000
        else disp = 17000
    } else if (ship_type == "CL") {
        if (year < 1920) disp = 5000
        else if (year < 1945) disp = 10000
        else disp = 15000
    } else if (ship_type == "DD") {
        if (year < 1920) disp = 1000
        else if (year < 1945) disp = 2000
        else disp = 5000
    } else if (ship_type == "SS") {
        if (year < 1920) disp = 500
        else if (year < 1945) disp = 1500
        else disp = 3000
    }
    
    # Estimate speed
    speed = 25
    if (ship_type == "BB") {
        if (year < 1906) speed = 18
        else if (year < 1915) speed = 21
        else if (year < 1936) speed = 23
        else speed = 30
    } else if (ship_type == "CV") {
        if (year < 1940) speed = 30
        else speed = 33
    } else if (ship_type == "CA" || ship_type == "CL") {
        if (year < 1920) speed = 25
        else if (year < 1945) speed = 32
        else speed = 33
    } else if (ship_type == "DD") {
        if (year < 1920) speed = 30
        else speed = 35
    } else if (ship_type == "SS") {
        if (year < 1945) speed = 15
        else speed = 20
    }
    
    # Estimate range
    range = 10000
    if (ship_type == "BB") range = 15000
    else if (ship_type == "CV") range = 12000
    else if (ship_type == "CA") range = 10000
    else if (ship_type == "CL") range = 8000
    else if (ship_type == "DD") range = 5000
    else if (ship_type == "SS") range = 8000
    
    # Ship type full name
    type_full = ship_type
    if (ship_type == "BB") type_full = "Battleship"
    else if (ship_type == "CV") type_full = "Aircraft Carrier"
    else if (ship_type == "CA") type_full = "Heavy Cruiser"
    else if (ship_type == "CL") type_full = "Light Cruiser"
    else if (ship_type == "DD") type_full = "Destroyer"
    else if (ship_type == "SS") type_full = "Submarine"
    
    # Modded flag (0 = historical)
    modded = 0
    if (notes ~ /PAPER/ || notes ~ /Fictional/ || notes ~ /theoretical/) modded = 1
    
    # Output basic ship entry with essential fields (20 fields)
    # Ship_ID | Country | Ship_Name | Ship_Class | Hull_Variant | Ship_Type | Ship_Type_Full | Era |
    # Year_Commissioned | Year_Designed | Year_Completed | Displacement_Standard | Displacement_Full |
    # Max_Speed | Cruise_Speed | Range_NM | Cost_USD | Build_Time | Modded | Notes
    printf "| %d | %s | %s | %s | Base | %s | %s | %s | %d | %d | %d | %d | %d | %d | %.1f | %d | %d | %d | %d | %s |\n",
        node_id, country, ship_class, ship_class, ship_type, type_full, era,
        year, year, year, disp, int(disp * 1.15), speed, speed * 0.8, range,
        cost, build_time, modded, notes
}
