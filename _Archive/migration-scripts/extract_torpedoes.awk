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
        gsub(/^[ \t]+|[ \t]+$/, "", $2)
        gsub(/^[ \t]+|[ \t]+$/, "", $3)
        gsub(/^[ \t]+|[ \t]+$/, "", $4)
        gsub(/^[ \t]+|[ \t]+$/, "", $5)
        gsub(/^[ \t]+|[ \t]+$/, "", $6)
        gsub(/^[ \t]+|[ \t]+$/, "", $7)
        gsub(/^[ \t]+|[ \t]+$/, "", $8)
        gsub(/^[ \t]+|[ \t]+$/, "", $9)
        gsub(/^[ \t]+|[ \t]+$/, "", $10)
        gsub(/^[ \t]+|[ \t]+$/, "", $11)
        
        node_id = $2
        country = $3
        designation = $4
        type = $5
        tier = $6
        year = $7
        research_cost = $8
        build_days = $9
        design = $10
        notes = $11
        
        if (node_id == "" || node_id !~ /^[0-9]+$/) next
        
        research_months = int((build_days + 29) / 30)
        build_months = research_months
        build_cost = research_cost * 2
        is_starting = (research_cost == 0) ? 1 : 0
        
        printf "| %s | %s | %s | %s | Torpedoes | %s | Torpedo | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |\n", node_id, country, designation, type, tier, year, is_starting, research_cost, research_months, build_cost, build_months, design, notes, type " Torpedo", "", design
    }
}

/^---$/ { in_table = 0 }
/^##/ { in_table = 0 }
