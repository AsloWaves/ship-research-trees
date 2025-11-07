#!/usr/bin/env python3
"""
Categorize Unknown aircraft files by checking for carrier-based indicators
and moving them to proper Naval-* or Land-* folders.
"""

import os
import re
from pathlib import Path
import shutil

def analyze_file(filepath):
    """Analyze file to determine if naval or land-based"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check tags for carrier-based indicator
        if 'carrier-based' in content.lower():
            return 'Naval'

        # Check for carrier operations section
        if 'carrier operations' in content.lower():
            return 'Naval'

        # Check for arresting hook
        if 'arresting hook' in content.lower():
            return 'Naval'

        # Check for catapult
        if 'catapult' in content.lower():
            return 'Naval'

        # Check nation - if UK/British and has "Sea " in name
        if 'nation: UK' in content or 'nation: British' in content:
            if 'Sea ' in content or 'sea-' in content.lower():
                return 'Naval'

        # Default to Land for everything else
        return 'Land'

    except Exception as e:
        print(f"Error analyzing {filepath}: {e}")
        return None

def get_aircraft_type(filepath):
    """Extract aircraft type from Unknown-* folder name"""
    path_parts = Path(filepath).parts
    for part in path_parts:
        if part.startswith('Unknown-'):
            return part.replace('Unknown-', '')
    return None

def update_frontmatter(filepath, domain):
    """Add proper naval-aircraft or ground-aircraft tag to frontmatter"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the tags line
    tag_to_add = 'naval-aircraft' if domain == 'Naval' else 'ground-aircraft'

    # Check if tag already exists
    if tag_to_add in content:
        return content

    # Add the tag to existing tags
    def add_tag(match):
        tags = match.group(1)
        # Check if already has the tag
        if tag_to_add in tags:
            return match.group(0)
        # Add tag at the beginning
        return f'tags: [{tag_to_add}, {tags}]'

    updated = re.sub(r'tags:\s*\[(.*?)\]', add_tag, content)

    return updated

def main():
    aircraft_dir = Path('Aircraft')

    print("=== Analyzing Unknown aircraft files ===\n")

    categorization = {}

    for unknown_dir in aircraft_dir.glob('*/Unknown-*'):
        for unknown_file in unknown_dir.glob('*.md'):
            domain = analyze_file(unknown_file)
            aircraft_type = get_aircraft_type(unknown_file)

            if domain and aircraft_type:
                categorization[unknown_file] = (domain, aircraft_type)
                print(f"{domain:5} - {aircraft_type:25} - {unknown_file.name}")

    print(f"\n=== Summary ===")
    naval_count = sum(1 for d, _ in categorization.values() if d == 'Naval')
    land_count = sum(1 for d, _ in categorization.values() if d == 'Land')
    print(f"Naval: {naval_count}")
    print(f"Land: {land_count}")
    print(f"Total: {len(categorization)}")

    response = input("\nProceed with categorization? (yes/no): ").strip().lower()

    if response == 'yes':
        print("\n=== Categorizing files ===\n")

        for unknown_file, (domain, aircraft_type) in categorization.items():
            nation = unknown_file.parts[1]  # Aircraft/[Nation]/Unknown-*/file.md

            # Create target directory
            target_dir = aircraft_dir / nation / f"{domain}-{aircraft_type}"
            target_dir.mkdir(parents=True, exist_ok=True)

            # Update frontmatter with proper tag
            updated_content = update_frontmatter(unknown_file, domain)

            # Write updated content to new location
            target_file = target_dir / unknown_file.name
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"Moved: {unknown_file.name} -> {nation}/{domain}-{aircraft_type}/")

            # Delete original
            unknown_file.unlink()

        print(f"\nSuccessfully categorized {len(categorization)} files")

        # Clean up empty Unknown folders
        print("\nCleaning up empty Unknown folders...")
        for unknown_dir in aircraft_dir.glob('*/Unknown-*'):
            if not any(unknown_dir.iterdir()):
                print(f"  Removing empty: {unknown_dir}")
                unknown_dir.rmdir()

        print("\nCategorization complete!")
    else:
        print("\nCategorization cancelled")

if __name__ == '__main__':
    main()
