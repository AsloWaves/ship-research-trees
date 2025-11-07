#!/bin/bash
# Find files in ship-research-trees/ that don't exist in Ships/

find ship-research-trees/ -type f -name "*.md" | while read file; do
  relative="${file#ship-research-trees/}"
  if [ ! -f "Ships/$relative" ]; then
    echo "$file"
  fi
done
