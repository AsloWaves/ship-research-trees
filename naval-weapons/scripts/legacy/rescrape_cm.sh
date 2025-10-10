#!/bin/bash
# Re-scrape cm weapons with corrected conversion

grep "cm" all_nations_weapons.txt | while read line; do
    COUNTRY=$(echo "$line" | cut -d'|' -f1)
    URL=$(echo "$line" | cut -d'|' -f2)

    echo "Processing: $COUNTRY - $URL"
    bash scrape_weapon_v2.sh "$URL" "$COUNTRY" 2>&1 | grep -E "(✓|✗|Caliber:|Already exists)"
    sleep 0.3
done

echo ""
echo "Re-scrape complete. Checking database..."
sqlite3 naval_weapons.db "SELECT COUNT(*) || ' total guns' FROM guns;"
