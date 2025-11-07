#!/usr/bin/env python3
"""
Cleanup duplicate files based on analysis report.

Strategy:
1. Delete entire _Archive/ folder (old structure from pre-reorganization)
2. Find and handle remaining duplicates in main structure
3. Delete files with "bad" formats (like Bismarck-Battleship.md vs Bismarck-Class.md)
"""

import os
import shutil
from pathlib import Path
import re

def check_yaml_format(filepath):
    """Check if file has properly formatted YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Proper format: starts with ---
        if content.strip().startswith('---'):
            return 'proper'

        # Code block format
        if '```yaml' in content[:100]:
            return 'code_block'

        return 'none'
    except:
        return 'error'

def delete_archive_folder():
    """Delete the entire _Archive folder"""
    archive_path = Path.cwd() / '_Archive'

    if not archive_path.exists():
        print("No _Archive folder found")
        return 0

    # Count files before deleting
    file_count = sum(1 for _ in archive_path.rglob('*.md'))

    print(f"Deleting _Archive folder containing {file_count} .md files...")

    try:
        shutil.rmtree(archive_path)
        print(f"[OK] Deleted _Archive/ folder ({file_count} files)")
        return file_count
    except Exception as e:
        print(f"[ERROR] Could not delete _Archive/: {e}")
        return 0

def find_bad_format_duplicates():
    """
    Find files where a -Class version and a -Battleship/-Carrier/etc version both exist.
    The -Class version is preferred, so delete the other.
    """
    root = Path.cwd()
    deletions = []

    # Patterns to check
    type_suffixes = ['-Battleship', '-Carrier', '-Cruiser', '-Destroyer', '-Submarine', '-Ship']

    # Find all .md files
    all_files = {}
    for filepath in root.rglob('*.md'):
        # Skip templates, scripts, archive
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Archive', '_Reports']):
            continue

        filename = filepath.stem  # filename without .md
        folder = filepath.parent

        key = (folder, filename)
        all_files[key] = filepath

    # Now check for duplicates where we have both "Name-Class" and "Name-Type"
    checked = set()

    for (folder, filename), filepath in all_files.items():
        if filename in checked:
            continue

        # Check if this ends with -Class
        if filename.endswith('-Class'):
            base_name = filename[:-6]  # Remove '-Class'

            # Check if there's a version with -Battleship, -Carrier, etc.
            for suffix in type_suffixes:
                alt_name = base_name + suffix
                alt_key = (folder, alt_name)

                if alt_key in all_files:
                    # Found a duplicate! Prefer -Class version
                    class_file = filepath
                    type_file = all_files[alt_key]

                    # Read both files to make sure we're making the right choice
                    class_format = check_yaml_format(class_file)
                    type_format = check_yaml_format(type_file)

                    # Get file sizes
                    class_lines = sum(1 for _ in open(class_file, encoding='utf-8'))
                    type_lines = sum(1 for _ in open(type_file, encoding='utf-8'))

                    deletions.append({
                        'keep': str(class_file.relative_to(root)),
                        'delete': str(type_file.relative_to(root)),
                        'reason': f'{filename} preferred (Class format), {alt_name} has {type_lines} lines vs {class_lines}'
                    })

                    checked.add(filename)
                    checked.add(alt_name)

    return deletions

def execute_deletions(deletions, dry_run=False):
    """Execute the file deletions"""
    root = Path.cwd()

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Processing {len(deletions)} duplicate files...")

    for item in deletions:
        delete_path = root / item['delete']

        if dry_run:
            print(f"[DRY RUN] Would delete: {item['delete']}")
            print(f"          Keeping: {item['keep']}")
            print(f"          Reason: {item['reason']}")
        else:
            try:
                if delete_path.exists():
                    delete_path.unlink()
                    print(f"[DELETED] {item['delete']}")
                else:
                    print(f"[SKIP] File not found: {item['delete']}")
            except Exception as e:
                print(f"[ERROR] Could not delete {item['delete']}: {e}")

def main():
    print("=" * 70)
    print("DUPLICATE FILE CLEANUP")
    print("=" * 70)

    # Step 1: Delete _Archive folder
    print("\n## Step 1: Delete _Archive folder")
    archive_deleted = delete_archive_folder()

    # Step 2: Find bad format duplicates (like Bismarck-Battleship vs Bismarck-Class)
    print("\n## Step 2: Find bad format duplicates in main structure")
    bad_duplicates = find_bad_format_duplicates()

    if bad_duplicates:
        print(f"\nFound {len(bad_duplicates)} bad format duplicates:")
        for item in bad_duplicates:
            print(f"  - Delete: {item['delete']}")
            print(f"    Keep: {item['keep']}")
            print(f"    Reason: {item['reason']}")
            print()

        # Ask for confirmation
        response = input(f"\nDelete these {len(bad_duplicates)} files? (yes/no): ")
        if response.lower() == 'yes':
            execute_deletions(bad_duplicates, dry_run=False)
        else:
            print("[CANCELLED] No files deleted")
    else:
        print("No bad format duplicates found in main structure")

    # Summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Archive folder deleted: {archive_deleted} files")
    print(f"Bad format duplicates found: {len(bad_duplicates)}")
    print(f"Total files cleaned up: {archive_deleted + len(bad_duplicates)}")

if __name__ == '__main__':
    main()
