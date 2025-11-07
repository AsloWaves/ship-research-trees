#!/usr/bin/env python3
"""
Reorganize Aircraft/ directory to Nation → Type pattern
Based on YAML frontmatter: nation, type, and tags (naval-aircraft vs ground-aircraft)
"""

import os
import re
import shutil
from pathlib import Path

def extract_frontmatter(filepath):
    """Extract nation, type, and domain from YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract YAML frontmatter
        match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None, None, None

        frontmatter = match.group(1)

        # Extract nation (use word boundary or start of line to avoid matching 'designation')
        nation_match = re.search(r'^nation:\s*(\S+)', frontmatter, re.MULTILINE)
        nation = nation_match.group(1) if nation_match else None

        # Extract type
        type_match = re.search(r'^type:\s*(.+?)$', frontmatter, re.MULTILINE)
        aircraft_type = type_match.group(1).strip() if type_match else None

        # Extract domain (naval vs ground) from tags
        tags_match = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
        if tags_match:
            tags = tags_match.group(1)
            if 'naval-aircraft' in tags:
                domain = 'Naval'
            elif 'ground-aircraft' in tags:
                domain = 'Land'
            else:
                domain = 'Unknown'
        else:
            domain = 'Unknown'

        return nation, aircraft_type, domain
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None, None, None

def normalize_nation(nation):
    """Normalize nation names to standard format"""
    if not nation:
        return 'Unknown'
    nation = nation.strip()
    mapping = {
        'USA': 'USA',
        'Japanese': 'Japan',
        'Japan': 'Japan',
        'British': 'Great-Britain',
        'UK': 'Great-Britain',
        'German': 'Germany',
        'Germany': 'Germany',
    }
    return mapping.get(nation, nation)

def normalize_type(aircraft_type):
    """Normalize aircraft type names"""
    if not aircraft_type:
        return 'Unknown'
    # Remove extra spaces and normalize
    return aircraft_type.strip().replace(' ', '-')

def main():
    aircraft_dir = Path('Aircraft')

    # Process Naval and Ground directories
    for domain_folder in ['Naval', 'Ground']:
        domain_path = aircraft_dir / domain_folder
        if not domain_path.exists():
            continue

        print(f"\nProcessing {domain_folder}...")

        for aircraft_file in domain_path.glob('*.md'):
            nation, aircraft_type, detected_domain = extract_frontmatter(aircraft_file)

            if not nation or not aircraft_type:
                print(f"  Skipping {aircraft_file.name} - missing metadata")
                continue

            # Normalize names
            normalized_nation = normalize_nation(nation)
            aircraft_type = normalize_type(aircraft_type)

            # Use folder domain if detected domain is Unknown
            if detected_domain == 'Unknown':
                detected_domain = 'Naval' if domain_folder == 'Naval' else 'Land'

            # Create target directory: Aircraft/Nation/Domain-Type/
            target_dir = aircraft_dir / normalized_nation / f"{detected_domain}-{aircraft_type}"
            target_dir.mkdir(parents=True, exist_ok=True)

            # Move file
            target_file = target_dir / aircraft_file.name
            print(f"  Moving {aircraft_file.name} -> {normalized_nation}/{detected_domain}-{aircraft_type}/")
            shutil.move(str(aircraft_file), str(target_file))

    # Also process existing nation folders (Germany, Japan, UK, USA)
    for nation_folder in ['Germany', 'Japan', 'UK', 'USA']:
        nation_path = aircraft_dir / nation_folder
        if not nation_path.exists():
            continue

        print(f"\nProcessing {nation_folder} folder...")

        for aircraft_file in nation_path.glob('*.md'):
            nation, aircraft_type, domain = extract_frontmatter(aircraft_file)

            if not aircraft_type or not domain:
                print(f"  Skipping {aircraft_file.name} - missing metadata")
                continue

            # Normalize
            normalized_nation = normalize_nation(nation) if nation else normalize_nation(nation_folder)
            aircraft_type = normalize_type(aircraft_type)

            # Create target directory
            target_dir = aircraft_dir / normalized_nation / f"{domain}-{aircraft_type}"
            target_dir.mkdir(parents=True, exist_ok=True)

            # Move file
            target_file = target_dir / aircraft_file.name
            print(f"  Moving {aircraft_file.name} -> {normalized_nation}/{domain}-{aircraft_type}/")
            shutil.move(str(aircraft_file), str(target_file))

    print("\nAircraft reorganization complete!")

    # Clean up empty directories
    print("\nCleaning up empty directories...")
    for folder in ['Naval', 'Ground', 'Germany', 'Japan', 'UK', 'USA']:
        folder_path = aircraft_dir / folder
        if folder_path.exists() and not any(folder_path.iterdir()):
            print(f"  Removing empty: {folder}")
            folder_path.rmdir()

if __name__ == '__main__':
    main()
