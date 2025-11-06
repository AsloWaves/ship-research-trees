#!/bin/bash
# Re-scrape affected countries to restore deleted weapons

echo "Re-scraping Germany, Japan, France, and Britain..."

grep -E "^(Germany|Japan|France|Britain)" all_nations_weapons.txt | while read line; do
    COUNTRY=$(echo "$line" | cut -d'|' -f1)
    URL=$(echo "$line" | cut -d'|' -f2)

    bash scrape_weapon_v2.sh "$URL" "$COUNTRY" > /dev/null 2>&1

    # Small delay
    sleep 0.2
done

echo "Re-scrape complete!"
sqlite3 naval_weapons.db "SELECT country, COUNT(*) as count FROM guns GROUP BY country ORDER BY count DESC;"
echo ""
sqlite3 naval_weapons.db "SELECT COUNT(*) || ' total guns' FROM guns;"
