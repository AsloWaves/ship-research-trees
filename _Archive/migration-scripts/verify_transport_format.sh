#!/bin/bash

# Verification script for transport/amphibious class files
DIR="D:\Research\ship-research-trees\USA\USA Transports Amphibious"
cd "$DIR"

correct=0
incorrect=0
declare -a incorrect_files

echo "=== FORMAT VERIFICATION REPORT ==="
echo ""

for file in *.md; do
    issues=""

    # Read first 10 lines
    line1=$(sed -n '1p' "$file")
    line2=$(sed -n '2p' "$file")
    line3=$(sed -n '3p' "$file")
    line4=$(sed -n '4p' "$file")

    # Check line 1: Should start with #
    if [[ ! "$line1" =~ ^#[[:space:]] ]]; then
        issues="${issues}- Line 1: Missing title (# Class Name)\n"
    fi

    # Check line 2: Should be blank
    if [[ -n "$line2" ]]; then
        issues="${issues}- Line 2: Not blank\n"
    fi

    # Check line 3: Should be ```yaml
    if [[ "$line3" != '```yaml' ]]; then
        issues="${issues}- Line 3: Missing \`\`\`yaml fence (found: '$line3')\n"
    fi

    # Check line 4: Should NOT be bare ---
    if [[ "$line4" == '---' ]]; then
        issues="${issues}- Line 4: Has bare --- delimiter (should start YAML content)\n"
    fi

    # Check for Overview section before closing ```
    if grep -q "^## Overview" "$file"; then
        first_overview=$(grep -n "^## Overview" "$file" | head -1 | cut -d: -f1)
        closing_fence=$(grep -n '^```$' "$file" | head -1 | cut -d: -f1)

        if [[ -n "$closing_fence" ]] && [[ $first_overview -lt $closing_fence ]]; then
            issues="${issues}- Has '## Overview' before closing \`\`\` (line $first_overview)\n"
        fi
    fi

    # Check if there's a closing ``` fence
    if ! grep -q '^```$' "$file"; then
        issues="${issues}- Missing closing \`\`\` fence\n"
    fi

    if [[ -z "$issues" ]]; then
        ((correct++))
    else
        ((incorrect++))
        incorrect_files+=("$file")
        echo "❌ $file"
        echo -e "$issues"
    fi
done

echo ""
echo "=== SUMMARY ==="
echo "✅ Correct format: $correct files"
echo "❌ Incorrect format: $incorrect files"
echo ""

if [[ $incorrect -gt 0 ]]; then
    echo "Files with issues:"
    for file in "${incorrect_files[@]}"; do
        echo "  - $file"
    done
fi
