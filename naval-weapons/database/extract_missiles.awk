BEGIN {
    FS = "|"
    OFS = "|"
    in_table = 0
}

/^\| Node_ID/ {
    in_table = 1
    next
}

/^\|[-\s]+\|/ {
    if (in_table) next
}

/^\| [0-9]/ {
    if (in_table) {
        # Extract and clean fields
        gsub(/^[ \t]+|[ \t]+$/, "", $2)  # Node_ID
        gsub(/^[ \t]+|[ \t]+$/, "", $3)  # Nation
        gsub(/^[ \t]+|[ \t]+$/, "", $4)  # Designation
        gsub(/^[ \t]+|[ \t]+$/, "", $5)  # Type
        gsub(/^[ \t]+|[ \t]+$/, "", $6)  # Year
        gsub(/^[ \t]+|[ \t]+$/, "", $7)  # Tech_Branch
        gsub(/^[ \t]+|[ \t]+$/, "", $8)  # Item_Type
        gsub(/^[ \t]+|[ \t]+$/, "", $9)  # Research_Cost
        gsub(/^[ \t]+|[ \t]+$/, "", $10) # Build_Days
        gsub(/^[ \t]+|[ \t]+$/, "", $11) # Steel
        gsub(/^[ \t]+|[ \t]+$/, "", $12) # Electronics
        gsub(/^[ \t]+|[ \t]+$/, "", $13) # Is_Starting_Tech
        gsub(/^[ \t]+|[ \t]+$/, "", $14) # Requires_Tech_IDs
        gsub(/^[ \t]+|[ \t]+$/, "", $15) # Unlocks_Tech_IDs
        gsub(/^[ \t]+|[ \t]+$/, "", $16) # Modded

        node_id = $2
        nation = $3
        designation = $4
        type = $5
        year = $6
        tech_branch = $7
        item_type = $8
        research_cost = $9
        build_days = $10
        steel = $11
        electronics = $12
        is_starting = $13
        requires = $14
        unlocks = $15
        modded = $16

        # Skip if not missile entry
        if (tech_branch != "Missiles") next

        # Convert build days to months (30 days = 1 month, round up)
        research_months = int((build_days + 29) / 30)
        build_months = research_months

        # Build cost = research cost * 2
        build_cost = research_cost * 2

        # Set starting tech flag
        is_starting_tech = (research_cost == 0) ? 1 : 0

        # Format output for ship_research_tree_database schema
        printf "| %s | %s | %s | %s | Missiles | %s | Missile | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n", \
            node_id, nation, designation, year, type, \
            research_cost, research_months, build_cost, build_months, \
            steel, electronics, 0, 0, \
            is_starting_tech, requires, unlocks
    }
}
