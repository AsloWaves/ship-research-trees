#!/bin/bash
# ============================================================================
# MASTER MD → SQL CONVERSION SCRIPT
# ============================================================================
# Purpose: Convert all 7 MD databases to SQL and create SQLite database
# Dependencies: awk, sqlite3
# Output: naval_weapons.db (SQLite database)
# ============================================================================

set -e  # Exit on any error
set -u  # Exit on undefined variable

# Color output for terminal
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Configuration
DB_NAME="naval_weapons.db"
SCHEMA_FILE="COMPLETE_SQL_SCHEMA.sql"
BACKUP_DIR="backups"

# Create backup directory
mkdir -p "$BACKUP_DIR"

echo -e "${BLUE}============================================================================${NC}"
echo -e "${BLUE}NAVAL WEAPONS DATABASE CONVERSION${NC}"
echo -e "${BLUE}============================================================================${NC}"
echo ""

# ============================================================================
# Step 1: Backup existing database if it exists
# ============================================================================

if [ -f "$DB_NAME" ]; then
    BACKUP_FILE="$BACKUP_DIR/naval_weapons_$(date +%Y%m%d_%H%M%S).db"
    echo -e "${YELLOW}[1/7] Backing up existing database...${NC}"
    cp "$DB_NAME" "$BACKUP_FILE"
    echo -e "${GREEN}✓ Backup created: $BACKUP_FILE${NC}"
    echo ""
else
    echo -e "${YELLOW}[1/7] No existing database found, creating new...${NC}"
    echo ""
fi

# ============================================================================
# Step 2: Create fresh database with schema
# ============================================================================

echo -e "${YELLOW}[2/7] Creating database schema...${NC}"

if [ ! -f "$SCHEMA_FILE" ]; then
    echo -e "${RED}✗ ERROR: Schema file not found: $SCHEMA_FILE${NC}"
    exit 1
fi

# Remove old database to start fresh
rm -f "$DB_NAME"

# Create schema
sqlite3 "$DB_NAME" < "$SCHEMA_FILE"

# Verify tables created
TABLE_COUNT=$(sqlite3 "$DB_NAME" "SELECT COUNT(*) FROM sqlite_master WHERE type='table';")
echo -e "${GREEN}✓ Database created with $TABLE_COUNT tables${NC}"
echo ""

# ============================================================================
# Step 3: Convert MD files to SQL INSERT statements
# ============================================================================

echo -e "${YELLOW}[3/7] Converting MD files to SQL...${NC}"

# Define database files and their conversion scripts
declare -A DATABASES
DATABASES=(
    ["naval_torpedoes_database.md"]="convert_torpedoes_to_sql.awk"
    ["naval_missiles_database.md"]="convert_missiles_to_sql.awk"
    ["naval_aircraft_database.md"]="convert_naval_aircraft_to_sql.awk"
    ["ground_aircraft_database.md"]="convert_ground_aircraft_to_sql.awk"
    ["naval_bombs_database.md"]="convert_bombs_to_sql.awk"
    ["naval_ships_database.md"]="convert_ships_to_sql.awk"
    ["ship_research_tree_database.md"]="convert_research_tree_to_sql.awk"
)

CONVERSION_SUCCESS=0
CONVERSION_FAILED=0

for MD_FILE in "${!DATABASES[@]}"; do
    AWK_SCRIPT="${DATABASES[$MD_FILE]}"
    SQL_OUTPUT="$(basename "$MD_FILE" .md)_insert.sql"

    echo -n "  Converting $MD_FILE... "

    if [ ! -f "$MD_FILE" ]; then
        echo -e "${RED}✗ NOT FOUND${NC}"
        CONVERSION_FAILED=$((CONVERSION_FAILED + 1))
        continue
    fi

    if [ ! -f "$AWK_SCRIPT" ]; then
        echo -e "${YELLOW}⚠ AWK script not found: $AWK_SCRIPT (skipping)${NC}"
        CONVERSION_FAILED=$((CONVERSION_FAILED + 1))
        continue
    fi

    # Run conversion
    if awk -f "$AWK_SCRIPT" "$MD_FILE" > "$SQL_OUTPUT" 2>&1; then
        RECORD_COUNT=$(grep -c "^INSERT INTO" "$SQL_OUTPUT" || echo "0")
        echo -e "${GREEN}✓ ($RECORD_COUNT records)${NC}"
        CONVERSION_SUCCESS=$((CONVERSION_SUCCESS + 1))
    else
        echo -e "${RED}✗ FAILED${NC}"
        CONVERSION_FAILED=$((CONVERSION_FAILED + 1))
    fi
done

echo ""
echo -e "${GREEN}✓ Converted $CONVERSION_SUCCESS/$((CONVERSION_SUCCESS + CONVERSION_FAILED)) databases${NC}"
echo ""

# ============================================================================
# Step 4: Import SQL data into database
# ============================================================================

echo -e "${YELLOW}[4/7] Importing data into database...${NC}"

IMPORT_SUCCESS=0
IMPORT_FAILED=0

for SQL_FILE in *_insert.sql; do
    if [ ! -f "$SQL_FILE" ]; then
        continue
    fi

    echo -n "  Importing $SQL_FILE... "

    if sqlite3 "$DB_NAME" < "$SQL_FILE" 2>&1; then
        echo -e "${GREEN}✓${NC}"
        IMPORT_SUCCESS=$((IMPORT_SUCCESS + 1))
    else
        echo -e "${RED}✗ FAILED${NC}"
        IMPORT_FAILED=$((IMPORT_FAILED + 1))
    fi
done

echo ""
echo -e "${GREEN}✓ Imported $IMPORT_SUCCESS files${NC}"
if [ "$IMPORT_FAILED" -gt 0 ]; then
    echo -e "${RED}✗ Failed imports: $IMPORT_FAILED${NC}"
fi
echo ""

# ============================================================================
# Step 5: Verify data import
# ============================================================================

echo -e "${YELLOW}[5/7] Verifying data import...${NC}"

# Query record counts from database
echo ""
sqlite3 "$DB_NAME" <<EOF
.mode column
.headers on
SELECT 'naval_torpedoes' as Table, COUNT(*) as Records FROM naval_torpedoes
UNION ALL SELECT 'naval_missiles', COUNT(*) FROM naval_missiles
UNION ALL SELECT 'naval_aircraft', COUNT(*) FROM naval_aircraft
UNION ALL SELECT 'ground_aircraft', COUNT(*) FROM ground_aircraft
UNION ALL SELECT 'naval_bombs', COUNT(*) FROM naval_bombs
UNION ALL SELECT 'naval_ships', COUNT(*) FROM naval_ships
UNION ALL SELECT 'ship_research_tree', COUNT(*) FROM ship_research_tree;
EOF

echo ""
TOTAL_RECORDS=$(sqlite3 "$DB_NAME" "SELECT
    (SELECT COUNT(*) FROM naval_torpedoes) +
    (SELECT COUNT(*) FROM naval_missiles) +
    (SELECT COUNT(*) FROM naval_aircraft) +
    (SELECT COUNT(*) FROM ground_aircraft) +
    (SELECT COUNT(*) FROM naval_bombs) +
    (SELECT COUNT(*) FROM naval_ships) +
    (SELECT COUNT(*) FROM ship_research_tree);")

echo -e "${GREEN}✓ Total records in database: $TOTAL_RECORDS${NC}"
echo ""

# ============================================================================
# Step 6: Run validation queries
# ============================================================================

echo -e "${YELLOW}[6/7] Running validation checks...${NC}"
echo ""

# Check for duplicate IDs (should be 0)
echo "  Checking for duplicate IDs..."
DUP_COUNT=$(sqlite3 "$DB_NAME" "
    SELECT COUNT(*) FROM (
        SELECT Ship_ID FROM naval_ships GROUP BY Ship_ID HAVING COUNT(*) > 1
    );")

if [ "$DUP_COUNT" -eq 0 ]; then
    echo -e "${GREEN}  ✓ No duplicate Ship IDs found${NC}"
else
    echo -e "${RED}  ✗ WARNING: Found $DUP_COUNT duplicate Ship IDs${NC}"
fi

# Check for NULL violations in NOT NULL fields
echo "  Checking for NULL violations..."
NULL_COUNT=$(sqlite3 "$DB_NAME" "
    SELECT COUNT(*) FROM naval_ships WHERE Country IS NULL OR Ship_Name IS NULL OR Ship_Class IS NULL;")

if [ "$NULL_COUNT" -eq 0 ]; then
    echo -e "${GREEN}  ✓ No NULL violations in required fields${NC}"
else
    echo -e "${RED}  ✗ WARNING: Found $NULL_COUNT NULL violations${NC}"
fi

# Check cross-references (ships without research entries)
echo "  Checking cross-references..."
MISSING_RESEARCH=$(sqlite3 "$DB_NAME" "SELECT COUNT(*) FROM v_ships_missing_research;")

if [ "$MISSING_RESEARCH" -eq 0 ]; then
    echo -e "${GREEN}  ✓ All ship classes have research tree entries${NC}"
else
    echo -e "${YELLOW}  ⚠ Found $MISSING_RESEARCH ship classes without research entries${NC}"
    echo "    (This may be expected for variants and individual ships)"
fi

echo ""
echo -e "${GREEN}✓ Validation complete${NC}"
echo ""

# ============================================================================
# Step 7: Optimize database and generate statistics
# ============================================================================

echo -e "${YELLOW}[7/7] Optimizing database...${NC}"

# Run ANALYZE to update statistics
sqlite3 "$DB_NAME" "ANALYZE;"

# Run VACUUM to compact database
sqlite3 "$DB_NAME" "VACUUM;"

# Get final database size
DB_SIZE=$(du -h "$DB_NAME" | cut -f1)

echo -e "${GREEN}✓ Database optimized${NC}"
echo -e "${GREEN}✓ Final database size: $DB_SIZE${NC}"
echo ""

# ============================================================================
# Summary Report
# ============================================================================

echo -e "${BLUE}============================================================================${NC}"
echo -e "${BLUE}CONVERSION SUMMARY${NC}"
echo -e "${BLUE}============================================================================${NC}"
echo ""
echo -e "Database file: ${GREEN}$DB_NAME${NC}"
echo -e "Total records: ${GREEN}$TOTAL_RECORDS${NC}"
echo -e "Database size: ${GREEN}$DB_SIZE${NC}"
echo ""
echo -e "Conversions: ${GREEN}$CONVERSION_SUCCESS succeeded${NC}, ${RED}$CONVERSION_FAILED failed${NC}"
echo -e "Imports: ${GREEN}$IMPORT_SUCCESS succeeded${NC}, ${RED}$IMPORT_FAILED failed${NC}"
echo ""

if [ "$CONVERSION_FAILED" -eq 0 ] && [ "$IMPORT_FAILED" -eq 0 ] && [ "$DUP_COUNT" -eq 0 ] && [ "$NULL_COUNT" -eq 0 ]; then
    echo -e "${GREEN}✓ ALL CHECKS PASSED - DATABASE READY FOR USE${NC}"
else
    echo -e "${YELLOW}⚠ WARNINGS DETECTED - REVIEW VALIDATION RESULTS${NC}"
fi

echo ""
echo -e "${BLUE}============================================================================${NC}"

# ============================================================================
# Generate validation report
# ============================================================================

REPORT_FILE="validation_report_$(date +%Y%m%d_%H%M%S).txt"

echo "Generating validation report: $REPORT_FILE"

sqlite3 "$DB_NAME" <<EOF > "$REPORT_FILE"
.mode column
.headers on
.output '$REPORT_FILE'

SELECT '=== NAVAL WEAPONS DATABASE VALIDATION REPORT ===' as Report;
SELECT 'Generated: ' || datetime('now') as Timestamp;
SELECT '' as Blank;

SELECT '--- RECORD COUNTS ---' as Section;
SELECT 'naval_torpedoes' as Table, COUNT(*) as Records FROM naval_torpedoes
UNION ALL SELECT 'naval_missiles', COUNT(*) FROM naval_missiles
UNION ALL SELECT 'naval_aircraft', COUNT(*) FROM naval_aircraft
UNION ALL SELECT 'ground_aircraft', COUNT(*) FROM ground_aircraft
UNION ALL SELECT 'naval_bombs', COUNT(*) FROM naval_bombs
UNION ALL SELECT 'naval_ships', COUNT(*) FROM naval_ships
UNION ALL SELECT 'ship_research_tree', COUNT(*) FROM ship_research_tree;

SELECT '' as Blank;
SELECT '--- DATA COMPLETENESS BY NATION ---' as Section;
SELECT * FROM v_data_completeness_by_nation;

SELECT '' as Blank;
SELECT '--- SHIPS MISSING RESEARCH TREE ENTRIES ---' as Section;
SELECT * FROM v_ships_missing_research LIMIT 20;

SELECT '' as Blank;
SELECT '--- RESEARCH NODES MISSING SHIPS ---' as Section;
SELECT * FROM v_research_missing_ships LIMIT 20;

.quit
EOF

echo -e "${GREEN}✓ Validation report saved: $REPORT_FILE${NC}"
echo ""

# ============================================================================
# Cleanup temporary files (optional)
# ============================================================================

read -p "Delete temporary SQL insert files? (y/N) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -f *_insert.sql
    echo -e "${GREEN}✓ Temporary files deleted${NC}"
else
    echo "Temporary files retained for debugging"
fi

echo ""
echo -e "${GREEN}Done! Database ready at: $DB_NAME${NC}"
