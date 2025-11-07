#!/bin/bash
# Apply field standardization to all markdown files

echo "==================================================================="
echo "FIELD STANDARDIZATION - Auto-apply"
echo "==================================================================="

# Find all .md files (excluding _Templates, _Scripts, _Reports, _Archive)
echo "Finding files to standardize..."

# Count files before
boats_count=$(grep -rl "^boats_built:" Ships/ Aircraft/ Weapons/ 2>/dev/null | wc -l)
speed_knots_count=$(grep -rl "^speed_knots:" Ships/ 2>/dev/null | wc -l)

echo ""
echo "Files to change:"
echo "  boats_built → ships_built: $boats_count files"
echo "  speed_knots → speed_design: $speed_knots_count files"
echo ""

# Apply changes using sed
echo "Applying changes..."

# Change boats_built → ships_built
find Ships/ Aircraft/ Weapons/ -name "*.md" -type f 2>/dev/null | while read file; do
    if grep -q "^boats_built:" "$file"; then
        sed -i 's/^boats_built:/ships_built:/g' "$file"
        echo "[OK] boats_built → ships_built: $file"
    fi
done

# Change speed_knots → speed_design
find Ships/ -name "*.md" -type f 2>/dev/null | while read file; do
    if grep -q "^speed_knots:" "$file"; then
        sed -i 's/^speed_knots:/speed_design:/g' "$file"
        echo "[OK] speed_knots → speed_design: $file"
    fi
done

echo ""
echo "==================================================================="
echo "STANDARDIZATION COMPLETE"
echo "==================================================================="

# Count files after
boats_after=$(grep -rl "^boats_built:" Ships/ Aircraft/ Weapons/ 2>/dev/null | wc -l)
ships_after=$(grep -rl "^ships_built:" Ships/ Aircraft/ Weapons/ 2>/dev/null | wc -l)
speed_knots_after=$(grep -rl "^speed_knots:" Ships/ 2>/dev/null | wc -l)
speed_design_after=$(grep -rl "^speed_design:" Ships/ 2>/dev/null | wc -l)

echo ""
echo "After standardization:"
echo "  boats_built: $boats_after files (should be 0)"
echo "  ships_built: $ships_after files"
echo "  speed_knots: $speed_knots_after files (should be 0)"
echo "  speed_design: $speed_design_after files"
