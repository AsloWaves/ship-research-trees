#!/bin/bash
# Scrape all nations' naval weapons from NavWeaps.com

URLS_FILE="all_nations_weapons.txt"
SCRAPER="./scrape_weapon_v2.sh"
LOG_FILE="scrape_all_nations_log.txt"
DB="naval_weapons.db"

# Counter for progress
TOTAL=$(wc -l < "$URLS_FILE")
CURRENT=0
SUCCESS=0
FAILED=0

echo "Starting scrape of $TOTAL weapons from all nations..." | tee "$LOG_FILE"
echo "======================================" | tee -a "$LOG_FILE"

while IFS='|' read -r COUNTRY URL; do
    CURRENT=$((CURRENT + 1))

    # Skip empty lines
    if [ -z "$URL" ]; then
        continue
    fi

    echo "" | tee -a "$LOG_FILE"
    echo "[$CURRENT/$TOTAL] $COUNTRY: $URL" | tee -a "$LOG_FILE"

    # Run scraper and capture result
    if bash "$SCRAPER" "$URL" "$COUNTRY" >> "$LOG_FILE" 2>&1; then
        if grep -q "✓ Data inserted successfully" "$LOG_FILE" | tail -1; then
            SUCCESS=$((SUCCESS + 1))
            echo "  ✓ Success" | tee -a "$LOG_FILE"
        else
            FAILED=$((FAILED + 1))
            echo "  ⚠ Skipped (missing data or duplicate)" | tee -a "$LOG_FILE"
        fi
    else
        FAILED=$((FAILED + 1))
        echo "  ✗ Failed" | tee -a "$LOG_FILE"
    fi

    # Small delay to be respectful to the server
    sleep 0.5

done < "$URLS_FILE"

echo "" | tee -a "$LOG_FILE"
echo "======================================" | tee -a "$LOG_FILE"
echo "Scraping complete!" | tee -a "$LOG_FILE"
echo "Total: $TOTAL | Success: $SUCCESS | Failed/Skipped: $FAILED" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "Database summary:" | tee -a "$LOG_FILE"
sqlite3 "$DB" "SELECT country, COUNT(*) as count FROM guns GROUP BY country ORDER BY count DESC;" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
sqlite3 "$DB" "SELECT COUNT(*) || ' total guns in database' FROM guns;" | tee -a "$LOG_FILE"
