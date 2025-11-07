#!/bin/bash

# Script to remove the bare --- delimiter from line 4 of all transport files
DIR="D:\Research\ship-research-trees\USA\USA Transports Amphibious"
cd "$DIR"

fixed=0

echo "Fixing YAML delimiter in all transport/amphibious class files..."
echo ""

for file in *.md; do
    # Check if line 4 is exactly "---"
    line4=$(sed -n '4p' "$file")

    if [[ "$line4" == "---" ]]; then
        # Remove line 4 (the bare --- delimiter)
        sed -i '4d' "$file"
        echo "✓ Fixed: $file"
        ((fixed++))
    fi
done

echo ""
echo "Fixed $fixed files"
