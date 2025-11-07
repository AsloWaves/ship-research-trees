#!/bin/bash
# Copy unique files from ship-research-trees/ to Ships/

bash _Scripts/find_unique_files.sh | while read file; do
  relative="${file#ship-research-trees/}"
  target="Ships/$relative"

  # Create directory if needed
  mkdir -p "$(dirname "$target")"

  # Copy file
  cp "$file" "$target"
  echo "Copied: $relative"
done
