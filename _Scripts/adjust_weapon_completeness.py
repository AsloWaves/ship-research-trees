#!/usr/bin/env python3
"""Adjust completeness thresholds for weapon files"""

import re
from pathlib import Path

def recalculate_completeness(filepath, line_count):
    """Recalculate completeness with weapon-appropriate thresholds"""
    # Weapon thresholds (more lenient than ships/aircraft)
    if line_count < 20:
        return 'stub'
    elif line_count < 40:
        return 'partial'
    else:
        return 'complete'

def update_completeness_field(filepath, new_completeness, dry_run=True):
    """Update completeness field in YAML frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find and replace completeness field
        pattern = r'(completeness:\s*)(stub|partial|complete)'
        match = re.search(pattern, content)

        if match:
            old_completeness = match.group(2)

            if old_completeness != new_completeness:
                new_content = re.sub(pattern, r'\g<1>' + new_completeness, content)

                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                return (old_completeness, new_completeness)

        return None
    except Exception as e:
        return None

def main():
    root = Path.cwd()

    print("=" * 70)
    print("ADJUST WEAPON COMPLETENESS THRESHOLDS")
    print("=" * 70)
    print("\nNew thresholds for weapons:")
    print("  - stub: < 20 lines (was < 30)")
    print("  - partial: 20-39 lines (was 30-59)")
    print("  - complete: 40+ lines (was 60+)")

    # Find all weapon files
    weapon_files = []
    for filepath in root.rglob('*.md'):
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
            continue

        path_str = str(filepath).replace('\\', '/')
        if '/Weapons/' in path_str:
            weapon_files.append(filepath)

    print(f"\nFound {len(weapon_files)} weapon files")

    # Analyze changes needed
    changes_needed = []
    for filepath in weapon_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            line_count = len(content.split('\n'))
            new_completeness = recalculate_completeness(filepath, line_count)

            # Check if completeness field exists and needs update
            match = re.search(r'completeness:\s*(stub|partial|complete)', content)
            if match:
                old_completeness = match.group(1)
                if old_completeness != new_completeness:
                    changes_needed.append((filepath, old_completeness, new_completeness, line_count))
        except:
            pass

    print(f"\n## Changes needed: {len(changes_needed)} files")

    # Count by type of change
    stub_to_partial = sum(1 for _, old, new, _ in changes_needed if old == 'stub' and new == 'partial')
    stub_to_complete = sum(1 for _, old, new, _ in changes_needed if old == 'stub' and new == 'complete')
    partial_to_complete = sum(1 for _, old, new, _ in changes_needed if old == 'partial' and new == 'complete')

    print(f"\nBreakdown:")
    print(f"  - stub -> partial: {stub_to_partial} files")
    print(f"  - stub -> complete: {stub_to_complete} files")
    print(f"  - partial -> complete: {partial_to_complete} files")

    print(f"\nSample files (first 10):")
    for filepath, old, new, lines in changes_needed[:10]:
        print(f"  - {filepath.relative_to(root)}")
        print(f"    {old} -> {new} ({lines} lines)")

    # Ask for confirmation
    response = input(f"\nApply changes to {len(changes_needed)} files? (yes/no): ")

    if response.lower() != 'yes':
        print("[CANCELLED] No changes made")
        return

    # Apply changes
    print("\n## Applying changes...")
    updated_count = 0

    for filepath, old_completeness, new_completeness, line_count in changes_needed:
        result = update_completeness_field(filepath, new_completeness, dry_run=False)
        if result:
            updated_count += 1
            if updated_count <= 10:
                print(f"[OK] {filepath.relative_to(root)}: {result[0]} -> {result[1]}")

    if updated_count > 10:
        print(f"... and {updated_count - 10} more files")

    print(f"\n[OK] Updated {updated_count} weapon files")

    # Summary of final state
    print("\n" + "=" * 70)
    print("FINAL COMPLETENESS SUMMARY")
    print("=" * 70)

    stub_count = 0
    partial_count = 0
    complete_count = 0

    for filepath in weapon_files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'completeness: stub' in content:
                stub_count += 1
            elif 'completeness: partial' in content:
                partial_count += 1
            elif 'completeness: complete' in content:
                complete_count += 1
        except:
            pass

    total = stub_count + partial_count + complete_count
    print(f"\nWeapon files with completeness tracking:")
    print(f"  - stub: {stub_count} files ({100*stub_count/total:.1f}%)")
    print(f"  - partial: {partial_count} files ({100*partial_count/total:.1f}%)")
    print(f"  - complete: {complete_count} files ({100*complete_count/total:.1f}%)")
    print(f"  - Total: {total} files")

if __name__ == '__main__':
    main()
