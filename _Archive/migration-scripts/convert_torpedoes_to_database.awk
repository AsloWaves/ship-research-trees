BEGIN {
    FS = "|"
    OFS = "|"
    in_table = 0
}

/^\| Node_ID.*Country/ {
    in_table = 1
    next
}

/^\|[-\s]+\|/ {
    if (in_table) next
}

/^\| [0-9]/ {
    if (in_table) {
        # Extract and clean fields
        gsub(/^[ \t]+|[ \t]+$/, "", $2)   # Node_ID
        gsub(/^[ \t]+|[ \t]+$/, "", $3)   # Country
        gsub(/^[ \t]+|[ \t]+$/, "", $4)   # Ship_Class (Designation)
        gsub(/^[ \t]+|[ \t]+$/, "", $5)   # Ship_Type (Type)
        gsub(/^[ \t]+|[ \t]+$/, "", $6)   # Tech_Branch
        gsub(/^[ \t]+|[ \t]+$/, "", $8)   # Era
        gsub(/^[ \t]+|[ \t]+$/, "", $9)   # Year_Available
        gsub(/^[ \t]+|[ \t]+$/, "", $13)  # Design_Philosophy
        gsub(/^[ \t]+|[ \t]+$/, "", $14)  # Historical_Context
        
        torpedo_id = $2
        country = $3
        designation = $4
        type = $5
        tech_branch = $6
        year = $9
        design = $13
        notes = $14
        
        # Only process torpedo entries
        if (tech_branch != "Torpedoes") next
        if (torpedo_id == "" || torpedo_id !~ /^[0-9]+$/) next
        
        # Estimate specifications based on type, year, and country
        
        # DIAMETER estimation
        if (designation ~ /24-inch|24"/ || country == "Japanese" && (type == "Oxygen" || designation ~ /Type 93|Type 97|Type 91/)) {
            diameter = 24
        } else if (designation ~ /27.5-inch|27.5"/ || designation ~ /Type 6.*Battleship/) {
            diameter = 27.5
        } else if (designation ~ /18-inch|18"/ || year < 1910 || designation ~ /Type 91/) {
            diameter = 18
        } else {
            diameter = 21  # Standard WWII diameter
        }
        
        # LENGTH estimation (feet)
        if (type ~ /Wire-Guided/ || year >= 1970) {
            torp_length = 21 + (diameter - 18) * 0.5
        } else if (type == "Oxygen") {
            torp_length = 29.5
        } else if (type ~ /Acoustic/) {
            torp_length = 23 + (year - 1940) * 0.05
        } else if (year >= 1940) {
            torp_length = 20 + (diameter - 18) * 0.8
        } else {
            torp_length = 15 + (year - 1890) * 0.1
        }
        if (torp_length > 30) torp_length = 30
        if (torp_length < 11) torp_length = 11
        
        # WEIGHT estimation (lbs)
        weight = diameter * diameter * torp_length * 8
        
        # WARHEAD estimation (lbs)
        if (designation ~ /Practice|Training/) {
            warhead = 0
        } else if (diameter >= 24) {
            warhead = 900 + (diameter - 24) * 100
        } else if (diameter == 21) {
            warhead = 600 + (year - 1920) * 5
            if (warhead > 900) warhead = 900
        } else {
            warhead = 300 + (diameter - 18) * 50
        }
        if (warhead < 0) warhead = 0
        
        # WARHEAD TYPE estimation
        if (year < 1915) {
            warhead_type = "Guncotton"
        } else if (year < 1935) {
            warhead_type = "TNT"
        } else if (year < 1943) {
            warhead_type = country == "Japanese" ? "Type 97" : "TNT"
        } else if (year < 1960) {
            warhead_type = country == "USA" ? "Torpex" : "TNT"
        } else {
            warhead_type = "HBX"
        }
        
        # SPEED estimation (knots)
        if (type ~ /Electric|Wakeless/) {
            speed = 28 + (year - 1940) * 0.3
        } else if (type == "Oxygen") {
            speed = 49 + (year - 1933) * 0.1
        } else if (type == "Wire-Guided") {
            speed = 45 + (year - 1965) * 0.3
        } else if (type == "Acoustic") {
            speed = 30 + (year - 1943) * 0.2
        } else if (type ~ /Steam|Alcohol/) {
            speed = 35 + (year - 1900) * 0.15
        } else if (type == "Flywheel") {
            speed = 25
        } else {
            speed = 30 + (year - 1890) * 0.1
        }
        if (speed > 65) speed = 65
        if (speed < 18) speed = 18
        
        # RANGE estimation (yards)
        if (type == "Oxygen") {
            range = 35000 + (year - 1933) * 500
            if (range > 43700) range = 43700
        } else if (type == "Wire-Guided") {
            range = 20000 + (year - 1965) * 500
        } else if (type ~ /Electric|Wakeless/) {
            range = 8000 + (year - 1940) * 200
        } else if (type == "Acoustic") {
            range = 5000 + (year - 1943) * 300
        } else if (type ~ /Steam|Alcohol/) {
            range = 4000 + (year - 1900) * 150
        } else if (designation ~ /Aerial|Type 91/) {
            range = 2000 + (year - 1930) * 100
        } else {
            range = 3000 + (year - 1890) * 100
        }
        if (range < 800) range = 800
        
        # RUNNING DEPTH
        if (designation ~ /Pearl Harbor|Mod 2.*aerial/ || notes ~ /SHALLOW|shallow/) {
            running_depth = "10-40"
        } else {
            running_depth = "15-50"
        }
        
        # PROPULSION
        if (type == "Steam") {
            propulsion = "Steam turbine, wet-heater"
        } else if (type == "Electric" || type == "Wakeless") {
            propulsion = "Battery-electric motor"
        } else if (type == "Oxygen") {
            propulsion = "Pure oxygen (Kerosene + O2)"
        } else if (type == "Alcohol") {
            propulsion = "Alcohol-fueled burner"
        } else if (type == "Flywheel") {
            propulsion = "Flywheel energy storage"
        } else if (type == "Wire-Guided") {
            propulsion = "Thermal (Otto fuel II)"
        } else if (type == "Acoustic") {
            propulsion = "Electric motor"
        } else if (type == "Compressed Air") {
            propulsion = "Compressed air engine"
        } else {
            propulsion = "Unknown"
        }
        
        # GUIDANCE
        if (type ~ /Wire-Guided/) {
            guidance = "Wire-guided + active/passive sonar"
        } else if (type ~ /Acoustic/) {
            guidance = "Passive acoustic homing"
        } else if (type ~ /Pattern/) {
            guidance = "Pattern-running (circular/zigzag)"
        } else {
            guidance = "Straight-running (gyroscope)"
        }
        
        # LAUNCH PLATFORM
        if (designation ~ /Aerial|Type 91/) {
            platform = "Aircraft (carrier-based)"
        } else if (designation ~ /Submarine|Type 95/) {
            platform = "Submarines"
        } else if (designation ~ /Destroyer|Surface/) {
            platform = "Surface ships (destroyers, cruisers)"
        } else if (designation ~ /Kaiten/) {
            platform = "Kaiten human torpedo (suicide weapon)"
        } else {
            platform = "Surface ships, submarines"
        }
        
        # MODDED flag
        modded = (notes ~ /PAPER|Paper|Theoretical|Never built/) ? 1 : 0
        
        # Format output
        printf "| %s | %s | %s | %s | %s | %.1f | %.1f | %.0f | %.0f | %s | %.1f | %d | %s | %s | %s | %s | %d | %s |\n",
            torpedo_id,
            country,
            designation,
            type,
            year,
            diameter,
            torp_length,
            weight,
            warhead,
            warhead_type,
            speed,
            range,
            running_depth,
            propulsion,
            guidance,
            platform,
            modded,
            notes
    }
}

/^---$/ { in_table = 0 }
/^##/ { in_table = 0 }
