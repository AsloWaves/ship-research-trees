#!/usr/bin/env python3
"""
Reorganize Weapons/Aircraft-Weapons/ to add nation subfolders
Current: Weapons/Aircraft-Weapons/Bombs/USA-AN-M30.md
Target: Weapons/Aircraft-Weapons/Bombs/USA/AN-M30.md
"""

import os
import shutil
from pathlib import Path

def normalize_nation(nation_code):
    """Normalize nation codes to full names"""
    mapping = {
        'UK': 'Great-Britain',
        'USA': 'USA',
        'US': 'USA',
        'Japan': 'Japan',
        'Japanese': 'Japan',
        'Germany': 'Germany',
        'German': 'Germany',
        'GER': 'Germany',
    }
    return mapping.get(nation_code, nation_code)

def main():
    base_dir = Path('Weapons/Aircraft-Weapons')

    # Process each weapon type folder
    for weapon_type_dir in base_dir.iterdir():
        if not weapon_type_dir.is_dir():
            continue

        print(f"\nProcessing {weapon_type_dir.name}/...")

        # Process each file
        for weapon_file in weapon_type_dir.glob('*.md'):
            filename = weapon_file.name

            # Extract nation prefix (format: "NATION-Weapon Name.md")
            if '-' in filename:
                parts = filename.split('-', 1)
                nation_code = parts[0]
                weapon_name = parts[1]  # Includes .md extension

                # Normalize nation
                nation = normalize_nation(nation_code)

                # Create nation subfolder
                nation_dir = weapon_type_dir / nation
                nation_dir.mkdir(exist_ok=True)

                # Move file
                target_file = nation_dir / weapon_name
                print(f"  {filename} -> {nation}/{weapon_name}")
                shutil.move(str(weapon_file), str(target_file))
            else:
                print(f"  Skipping {filename} (no nation prefix found)")

    print("\nAircraft-Weapons reorganization complete!")

if __name__ == '__main__':
    main()
