#!/usr/bin/env python3
"""
Standardize field names across all markdown files.

Field Standardizations:
- boats_built → ships_built
- speed_knots/speed_max → speed_design + speed_trial
- Preserve existing speed_design and speed_trial
- Document changes in report
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def standardize_file(filepath, dry_run=True):
    """
    Standardize field names in a single file.
    Returns dict of changes made.
    """
    changes = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Standardization 1: boats_built → ships_built
        if re.search(r'\bboats_built:', content):
            content = re.sub(r'\bboats_built:', 'ships_built:', content)
            changes.append('boats_built → ships_built')

        # Standardization 2: speed_knots → speed_design (only if speed_design doesn't exist)
        if re.search(r'\bspeed_knots:', content) and not re.search(r'\bspeed_design:', content):
            content = re.sub(r'\bspeed_knots:', 'speed_design:', content)
            changes.append('speed_knots → speed_design')

        # Standardization 3: speed_max → speed_trial (only if used alone without speed_design)
        # This is more complex - only rename if there's no speed_design
        if re.search(r'\bspeed_max:', content) and not re.search(r'\bspeed_design:', content):
            content = re.sub(r'\bspeed_max:', 'speed_design:', content)
            changes.append('speed_max → speed_design (no design speed found)')
        elif re.search(r'\bspeed_max:', content) and re.search(r'\bspeed_design:', content):
            # If both exist, rename speed_max to speed_trial
            content = re.sub(r'\bspeed_max:', 'speed_trial:', content)
            changes.append('speed_max → speed_trial')

        # Write back if changes were made
        if changes and not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

        return changes

    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return []

def scan_field_usage():
    """Scan all files to see current field usage"""
    root = Path.cwd()
    field_counts = defaultdict(int)

    for filepath in root.rglob('*.md'):
        # Skip templates, scripts, reports, archive
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Archive', '_Reports']):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Count field occurrences
            if 'boats_built:' in content:
                field_counts['boats_built'] += 1
            if 'ships_built:' in content:
                field_counts['ships_built'] += 1
            if 'speed_knots:' in content:
                field_counts['speed_knots'] += 1
            if 'speed_design:' in content:
                field_counts['speed_design'] += 1
            if 'speed_max:' in content:
                field_counts['speed_max'] += 1
            if 'speed_trial:' in content:
                field_counts['speed_trial'] += 1
            if 'decommissioned:' in content:
                field_counts['decommissioned'] += 1
            if 'sunk:' in content:
                field_counts['sunk'] += 1
            if 'scrapped:' in content:
                field_counts['scrapped'] += 1

        except:
            pass

    return field_counts

def main():
    print("=" * 70)
    print("FIELD STANDARDIZATION")
    print("=" * 70)

    # Step 1: Scan current field usage
    print("\n## Step 1: Scan current field usage")
    field_counts = scan_field_usage()

    print("\nCurrent field usage:")
    print(f"  boats_built: {field_counts['boats_built']} files")
    print(f"  ships_built: {field_counts['ships_built']} files")
    print(f"  speed_knots: {field_counts['speed_knots']} files")
    print(f"  speed_design: {field_counts['speed_design']} files")
    print(f"  speed_max: {field_counts['speed_max']} files")
    print(f"  speed_trial: {field_counts['speed_trial']} files")
    print(f"  decommissioned: {field_counts['decommissioned']} files")
    print(f"  sunk: {field_counts['sunk']} files")
    print(f"  scrapped: {field_counts['scrapped']} files")

    # Step 2: Standardize all files
    print("\n## Step 2: Standardize field names")

    root = Path.cwd()
    files_changed = 0
    total_changes = defaultdict(int)

    # First pass: dry run to see what would change
    print("\n[DRY RUN] Scanning for changes...")

    for filepath in root.rglob('*.md'):
        # Skip templates, scripts, reports, archive
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Archive', '_Reports']):
            continue

        changes = standardize_file(filepath, dry_run=True)

        if changes:
            files_changed += 1
            for change in changes:
                total_changes[change] += 1

    print(f"\nWould change {files_changed} files:")
    for change, count in sorted(total_changes.items()):
        print(f"  {change}: {count} files")

    # Ask for confirmation
    print("\n" + "=" * 70)
    response = input(f"Apply these changes to {files_changed} files? (yes/no): ")

    if response.lower() != 'yes':
        print("[CANCELLED] No changes made")
        return

    # Second pass: actually make the changes
    print("\nApplying changes...")
    files_changed = 0

    for filepath in root.rglob('*.md'):
        # Skip templates, scripts, reports, archive
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Archive', '_Reports']):
            continue

        changes = standardize_file(filepath, dry_run=False)

        if changes:
            files_changed += 1
            print(f"[OK] {filepath.relative_to(root)}: {', '.join(changes)}")

    # Generate report
    report_path = Path.cwd() / '_Reports' / 'FIELD_STANDARDIZATION.md'

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('# Field Standardization Report\n\n')
        f.write(f'**Files Changed:** {files_changed}\n\n')
        f.write('## Changes Applied\n\n')
        for change, count in sorted(total_changes.items()):
            f.write(f'- {change}: {count} files\n')
        f.write('\n## New Field Usage After Standardization\n\n')
        f.write('Run `scan_field_usage()` again to see updated counts.\n')

    print(f"\n[OK] Standardization complete: {files_changed} files changed")
    print(f"[OK] Report generated: {report_path}")

if __name__ == '__main__':
    main()
