#!/bin/bash
# Enhanced NavWeaps Gun Data Scraper - Version 2
# Handles non-standard designation formats

URL=$1
COUNTRY=${2:-"USA"}
DB="naval_weapons.db"

if [ -z "$URL" ]; then
    echo "Usage: $0 <weapon_url> [country]"
    exit 1
fi

# Download the page
echo "Fetching $URL..."
PAGE=$(curl -s "http://www.navweaps.com/Weapons/$URL")

# Extract key fields
DESIGNATION=$(echo "$PAGE" | grep -oP '<h1>\K[^<]+' | tail -1)
SHIPS=$(echo "$PAGE" | grep -A 1 "Ship Class Used On" | tail -1 | sed 's/<[^>]*>//g; s/^[[:space:]]*//; s/[[:space:]]*$//')
YEAR=$(echo "$PAGE" | grep -A 1 "Date In Service" | tail -1 | sed 's/<[^>]*>//g; s/^[[:space:]]*//; s/[[:space:]]*$//' | grep -oP '\d{4}')
ROF=$(echo "$PAGE" | grep -A 1 "Rate Of Fire" | tail -1 | sed 's/<[^>]*>//g; s/^[[:space:]]*//; s/[[:space:]]*$//' | grep -oP '\d+,?\d+' | head -1 | tr -d ',')
MUZZLE_VEL=$(echo "$PAGE" | grep -i "Muzzle Velocity" -A 5 | grep -oP '\d+,?\d*\s*fps' | head -1 | grep -oP '\d+,?\d*' | tr -d ',')

# Enhanced caliber extraction
# Method 1: Check for mm format FIRST (to catch "20 mm" before extracting "20")
MM_CAL=$(echo "$DESIGNATION" | grep -oP '\d+\.?\d*\s*mm' | grep -oP '\d+\.?\d*' | head -1)
if [ -n "$MM_CAL" ]; then
    CALIBER=$(awk "BEGIN {printf \"%.3f\", $MM_CAL / 25.4}")
else
    # Method 2: Check for cm format BEFORE standard extraction
    CM_CAL=$(echo "$DESIGNATION" | grep -oP '\d+\.?\d*\s*cm' | grep -oP '\d+\.?\d*' | head -1)
    if [ -n "$CM_CAL" ]; then
        CALIBER=$(awk "BEGIN {printf \"%.2f\", $CM_CAL / 2.54}")
    else
        # Method 3: Standard format "16"/50" -> 16.0
        CALIBER=$(echo "$DESIGNATION" | grep -oP '^\d+\.?\d*' | head -1)
    fi
fi

# Method 4: Try extracting from table in page
if [ -z "$CALIBER" ]; then
    CALIBER=$(echo "$PAGE" | grep -A 1 "Caliber" | tail -1 | sed 's/<[^>]*>//g' | grep -oP '\d+\.?\d*' | head -1)
fi

# Enhanced barrel length extraction
# Standard format from designation
BARREL_LENGTH=$(echo "$DESIGNATION" | grep -oP '/\K\d+' | head -1)

# If not in designation, try from table
if [ -z "$BARREL_LENGTH" ]; then
    BARREL_LENGTH=$(echo "$PAGE" | grep -A 1 "Barrel Length" | tail -1 | sed 's/<[^>]*>//g' | grep -oP '\d+' | head -1)
fi

# Country is now passed as parameter $2

# Extract range
MAX_RANGE=$(echo "$PAGE" | grep -i "maximum.*range" -A 3 | grep -oP '\d+,?\d+\s*yards' | head -1 | grep -oP '\d+,?\d+' | tr -d ',')

# Display extracted data
echo "================================"
echo "Designation: $DESIGNATION"
echo "Caliber: $CALIBER inches"
echo "Barrel Length: $BARREL_LENGTH calibers"
echo "Country: $COUNTRY"
echo "Ships: $SHIPS"
echo "Year: $YEAR"
echo "Rate of Fire: $ROF rpm"
echo "Muzzle Velocity: $MUZZLE_VEL fps"
echo "Max Range: $MAX_RANGE yards"
echo "================================"

# Insert into database if required fields present
if [ -n "$DESIGNATION" ] && [ -n "$CALIBER" ]; then
    echo "Inserting into database..."

    # Escape single quotes for SQL
    DESIGNATION_ESC="${DESIGNATION//\'/\'\'}"
    SHIPS_ESC="${SHIPS//\'/\'\'}"
    COUNTRY_ESC="${COUNTRY//\'/\'\'}"

    # Check if already exists
    EXISTS=$(sqlite3 "$DB" "SELECT COUNT(*) FROM guns WHERE designation = '$DESIGNATION_ESC';")

    if [ "$EXISTS" -gt 0 ]; then
        echo "⚠ Already exists, skipping"
    else
        sqlite3 "$DB" <<EOF
INSERT INTO guns (designation, caliber_inches, barrel_length, country, ships, max_range_yards, muzzle_velocity, rate_of_fire, year_introduced)
VALUES ('$DESIGNATION_ESC', $CALIBER, ${BARREL_LENGTH:-NULL}, '$COUNTRY_ESC', '$SHIPS_ESC', ${MAX_RANGE:-NULL}, ${MUZZLE_VEL:-NULL}, ${ROF:-NULL}, ${YEAR:-NULL});
EOF
        echo "✓ Data inserted successfully"
    fi
else
    echo "✗ Missing required fields (Designation or Caliber)"
fi
