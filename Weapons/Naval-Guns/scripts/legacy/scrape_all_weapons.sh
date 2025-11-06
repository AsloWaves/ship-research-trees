#!/bin/bash
# Scrape all US naval weapons from NavWeaps.com

URLS_FILE="weapon_urls.txt"
SCRAPER="./scrape_weapon_v2.sh"
LOG_FILE="scrape_log.txt"

# Counter for progress
TOTAL=$(wc -l < "$URLS_FILE")
CURRENT=0
SUCCESS=0
FAILED=0

echo "Starting scrape of $TOTAL weapons..." | tee "$LOG_FILE"
echo "======================================" | tee -a "$LOG_FILE"

while IFS= read -r URL; do
    CURRENT=$((CURRENT + 1))

    # Skip non-gun pages
    if [[ "$URL" == *"Gun_Nomenclature"* ]] || \
       [[ "$URL" == *"Radar"* ]] || \
       [[ "$URL" == *"firing"* ]]; then
        echo "[$CURRENT/$TOTAL] Skipping: $URL" | tee -a "$LOG_FILE"
        continue
    fi

    echo "" | tee -a "$LOG_FILE"
    echo "[$CURRENT/$TOTAL] Processing: $URL" | tee -a "$LOG_FILE"

    # Run scraper and capture result
    if bash "$SCRAPER" "$URL" >> "$LOG_FILE" 2>&1; then
        if grep -q "✓ Data inserted successfully" "$LOG_FILE" | tail -1; then
            SUCCESS=$((SUCCESS + 1))
            echo "  ✓ Success" | tee -a "$LOG_FILE"
        else
            FAILED=$((FAILED + 1))
            echo "  ⚠ Skipped (missing data)" | tee -a "$LOG_FILE"
        fi
    else
        FAILED=$((FAILED + 1))
        echo "  ✗ Failed" | tee -a "$LOG_FILE"
    fi

    # Small delay to be respectful to the server
    sleep 1

done < "$URLS_FILE"

echo "" | tee -a "$LOG_FILE"
echo "======================================" | tee -a "$LOG_FILE"
echo "Scraping complete!" | tee -a "$LOG_FILE"
echo "Total: $TOTAL | Success: $SUCCESS | Failed/Skipped: $FAILED" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "Database summary:" | tee -a "$LOG_FILE"
sqlite3 naval_weapons.db "SELECT COUNT(*) || ' guns in database' FROM guns;" | tee -a "$LOG_FILE"
