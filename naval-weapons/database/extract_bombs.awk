#!/usr/bin/awk -f
# Extract bomb research nodes from research tree logic files
# Converts research tree format to ship_research_tree_database format

BEGIN {
    FS = "|"
    OFS = "|"
    in_table = 0
}

# Detect table start
/^\| Node_ID/ {
    in_table = 1
    next
}

# Detect separator line
/^\|-+/ {
    next
}

# Process data rows
/^\| [0-9]/ {
    if (in_table) {
        # Strip whitespace from all fields
        for (i = 1; i <= NF; i++) {
            gsub(/^[ \t]+|[ \t]+$/, "", $i)
        }

        node_id = $2
        nation = $3
        designation = $4
        bomb_type = $5
        year = $6
        tech_branch = $7
        item_type = $8
        research_cost = $9
        research_days = $10
        steel = $11
        electronics = $12
        is_starting = $13
        requires = $14
        unlocks = $15
        modded = $16

        # Skip empty rows
        if (node_id == "" || node_id == "Node_ID") next

        # Convert research days to research months (divide by 30, round up)
        research_months = int((research_days + 29) / 30)
        if (research_months == 0 && research_days > 0) research_months = 1

        # Build months = research months
        build_months = research_months

        # Build cost = 2x research cost
        build_cost = research_cost * 2

        # Maintenance cost = 5% of build cost per year
        maintenance_cost = int(build_cost * 0.05)

        # Crew = 0 (bombs don't have crew)
        crew = 0

        # Output in ship_research_tree_database format
        printf "| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n",
            node_id, nation, designation, bomb_type, year, tech_branch, item_type,
            research_cost, research_months, build_cost, build_months,
            maintenance_cost, steel, electronics, crew,
            is_starting, requires, unlocks, modded
    }
}

# Reset table flag on empty line or new section
/^$/ || /^#/ {
    in_table = 0
}
