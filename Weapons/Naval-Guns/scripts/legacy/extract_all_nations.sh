#!/bin/bash
# Extract weapon URLs from all nations on NavWeaps.com

OUTPUT_FILE="all_nations_weapons.txt"
> "$OUTPUT_FILE"  # Clear file

# Define nation codes and full names
declare -A NATIONS=(
    ["WNBR"]="Britain"
    ["WNGER"]="Germany"
    ["WNJAP"]="Japan"
    ["WNFR"]="France"
    ["WNIT"]="Italy"
    ["WNARG"]="Argentina"
    ["WNBZL"]="Brazil"
    ["WNCHL"]="Chile"
    ["WNFIN"]="Finland"
    ["WNIND"]="India"
    ["WNNOR"]="Norway"
    ["WNPRC"]="China"
    ["WNUS"]="USA"
)

echo "Extracting weapon URLs from all nations..."
echo "=========================================="

TOTAL_WEAPONS=0

for CODE in "${!NATIONS[@]}"; do
    COUNTRY="${NATIONS[$CODE]}"
    MAIN_PAGE="${CODE}_Main.php"

    echo ""
    echo "Processing $COUNTRY ($CODE)..."

    # Fetch and extract weapon URLs
    URLS=$(curl -s "http://www.navweaps.com/Weapons/$MAIN_PAGE" | \
           grep -oP 'href="'${CODE}'[^"]+\.php"' | \
           sed 's/href="//; s/"$//' | \
           grep -v 'Main.php' | \
           grep -v 'Gun_Nomenclature' | \
           grep -v 'Radar' | \
           grep -v 'firing' | \
           sort -u)

    COUNT=$(echo "$URLS" | grep -c "^${CODE}")

    if [ $COUNT -gt 0 ]; then
        echo "  Found $COUNT weapons"

        # Add to output file with country prefix
        echo "$URLS" | while read -r URL; do
            echo "$COUNTRY|$URL" >> "$OUTPUT_FILE"
        done

        TOTAL_WEAPONS=$((TOTAL_WEAPONS + COUNT))
    else
        echo "  No weapons found"
    fi
done

echo ""
echo "=========================================="
echo "Total weapons found: $TOTAL_WEAPONS"
echo "Saved to: $OUTPUT_FILE"
