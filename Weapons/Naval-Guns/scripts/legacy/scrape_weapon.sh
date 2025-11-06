#!/bin/bash
# NavWeaps Gun Data Scraper

URL=$1
DB="naval_weapons.db"

if [ -z "$URL" ]; then
    echo "Usage: $0 <weapon_url>"
    exit 1
fi

# Download the page
echo "Fetching $URL..."
PAGE=$(curl -s "http://www.navweaps.com/Weapons/$URL")

# Extract key fields using grep and sed
DESIGNATION=$(echo "$PAGE" | grep -oP '<h1>\K[^<]+' | tail -1)
SHIPS=$(echo "$PAGE" | grep -A 1 "Ship Class Used On" | tail -1 | sed 's/<[^>]*>//g; s/^[[:space:]]*//; s/[[:space:]]*$//')
YEAR=$(echo "$PAGE" | grep -A 1 "Date In Service" | tail -1 | sed 's/<[^>]*>//g; s/^[[:space:]]*//; s/[[:space:]]*$//' | grep -oP '\d{4}')
ROF=$(echo "$PAGE" | grep -A 1 "Rate Of Fire" | tail -1 | sed 's/<[^>]*>//g; s/^[[:space:]]*//; s/[[:space:]]*$//' | grep -oP '[\d.]+')
MUZZLE_VEL=$(echo "$PAGE" | grep -i "Muzzle Velocity" -A 5 | grep -oP '\d+,?\d*\s*fps' | head -1 | grep -oP '\d+,?\d*' | tr -d ',')

# Extract caliber from designation (e.g., "16"/50" -> 16.0)
CALIBER=$(echo "$DESIGNATION" | grep -oP '^\d+\.?\d*' | head -1)

# Extract barrel length in calibers (e.g., "16"/50" -> 50)
BARREL_LENGTH=$(echo "$DESIGNATION" | grep -oP '/\K\d+' | head -1)

# Extract country
COUNTRY="USA"

# Extract range - look for "Maximum Range"
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

# Insert into database if all required fields are present
if [ -n "$DESIGNATION" ] && [ -n "$CALIBER" ]; then
    echo "Inserting into database..."
    sqlite3 "$DB" <<EOF
INSERT INTO guns (designation, caliber_inches, barrel_length, country, ships, max_range_yards, muzzle_velocity, rate_of_fire, year_introduced)
VALUES ('$DESIGNATION', $CALIBER, ${BARREL_LENGTH:-NULL}, '$COUNTRY', '$SHIPS', ${MAX_RANGE:-NULL}, ${MUZZLE_VEL:-NULL}, ${ROF:-NULL}, ${YEAR:-NULL});
EOF
    echo "✓ Data inserted successfully"
else
    echo "✗ Missing required fields, skipping database insert"
fi
