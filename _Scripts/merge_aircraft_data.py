#!/usr/bin/env python3
"""
Merge detailed data from Unknown aircraft files into categorized (Naval/Land) files.
Preserves the categorized file's YAML frontmatter while adding detailed content.
"""

import os
import re
from pathlib import Path
import shutil

def extract_designation(filepath):
    """Extract designation from YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None

        frontmatter = match.group(1)
        desig_match = re.search(r'^designation:\s*(.+?)$', frontmatter, re.MULTILINE)

        if desig_match:
            designation = desig_match.group(1).strip()
            return designation
        return None
    except Exception as e:
        print(f"Error extracting designation from {filepath}: {e}")
        return None

def parse_file(filepath):
    """Parse file into frontmatter and content sections"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract YAML frontmatter
    match = re.search(r'^(---\s*\n.*?\n---)\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return None, content

    frontmatter = match.group(1)
    body = match.group(2)

    return frontmatter, body

def find_matching_categorized_file(unknown_file, aircraft_dir):
    """Find the categorized file that matches this Unknown file"""
    unknown_designation = extract_designation(unknown_file)
    if not unknown_designation:
        return None

    # Get the nation from the path
    unknown_path = Path(unknown_file)
    nation = unknown_path.parts[1]  # Aircraft/[Nation]/Unknown-*/file.md

    # Search in all Naval-* and Land-* folders for this nation
    nation_dir = aircraft_dir / nation

    for category_dir in nation_dir.iterdir():
        if not category_dir.is_dir():
            continue
        if not (category_dir.name.startswith('Naval-') or category_dir.name.startswith('Land-')):
            continue

        for cat_file in category_dir.glob('*.md'):
            cat_designation = extract_designation(cat_file)
            if not cat_designation:
                continue

            # Match if categorized designation starts with unknown designation
            # e.g., "A6M2" matches "A6M2 Zero"
            if cat_designation.startswith(unknown_designation + ' ') or cat_designation == unknown_designation:
                return cat_file

    return None

def merge_files(unknown_file, categorized_file, dry_run=True):
    """Merge detailed data from Unknown file into categorized file"""

    # Parse both files
    unknown_fm, unknown_body = parse_file(unknown_file)
    cat_fm, cat_body = parse_file(categorized_file)

    if not unknown_fm or not cat_fm:
        print(f"  [ERROR] Could not parse YAML frontmatter")
        return False

    # Keep categorized file's frontmatter (has correct aircraft_id and tags)
    # Use Unknown file's body (has detailed game data)
    merged_content = f"{cat_fm}\n{unknown_body}"

    if dry_run:
        print(f"  -> Would merge into: {categorized_file}")
        return True
    else:
        # Write merged content
        with open(categorized_file, 'w', encoding='utf-8') as f:
            f.write(merged_content)
        print(f"  -> Merged into: {categorized_file}")
        return True

def main():
    aircraft_dir = Path('Aircraft')

    # First, do a dry run to show what will happen
    print("=== DRY RUN: Analyzing Unknown files ===\n")

    unknown_files = []
    for unknown_dir in aircraft_dir.glob('*/Unknown-*'):
        for unknown_file in unknown_dir.glob('*.md'):
            unknown_files.append(unknown_file)

    print(f"Found {len(unknown_files)} Unknown files to process\n")

    matched_count = 0
    unmatched = []

    for unknown_file in unknown_files:
        designation = extract_designation(unknown_file)
        if not designation:
            print(f"[ERROR] {unknown_file}: Could not extract designation")
            unmatched.append(unknown_file)
            continue

        categorized_file = find_matching_categorized_file(unknown_file, aircraft_dir)

        if categorized_file:
            print(f"[OK] {unknown_file.name} ({designation})")
            merge_files(unknown_file, categorized_file, dry_run=True)
            matched_count += 1
        else:
            print(f"[SKIP] {unknown_file.name} ({designation}): No matching categorized file found")
            unmatched.append(unknown_file)

    print(f"\n=== Summary ===")
    print(f"Matched: {matched_count}")
    print(f"Unmatched: {len(unmatched)}")

    if unmatched:
        print(f"\nUnmatched files:")
        for f in unmatched[:10]:
            print(f"  - {f}")
        if len(unmatched) > 10:
            print(f"  ... and {len(unmatched) - 10} more")

    # Ask for confirmation
    print("\n" + "="*60)
    response = input("Proceed with merge? (yes/no): ").strip().lower()

    if response == 'yes':
        print("\n=== EXECUTING MERGE ===\n")

        success_count = 0
        for unknown_file in unknown_files:
            categorized_file = find_matching_categorized_file(unknown_file, aircraft_dir)
            if categorized_file:
                designation = extract_designation(unknown_file)
                print(f"Merging {unknown_file.name} ({designation})...")
                if merge_files(unknown_file, categorized_file, dry_run=False):
                    success_count += 1

        print(f"\nSuccessfully merged {success_count} files")
        print(f"\nNow you can delete Unknown folders or review unmatched files")
    else:
        print("\nMerge cancelled")

if __name__ == '__main__':
    main()
