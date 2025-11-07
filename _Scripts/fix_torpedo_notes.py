#!/usr/bin/env python3
"""Remove placeholder numbers from torpedo Notes sections"""

import re
from pathlib import Path

def fix_torpedo_notes(filepath, dry_run=True):
    """Remove single-digit placeholder from Notes section"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Pattern: ## Notes\n<single digit>\n
        # Replace with: ## Notes\n\n(No additional notes available)\n
        pattern = r'(## Notes\s*\n)\d+\s*\n*$'

        if re.search(pattern, content):
            new_content = re.sub(pattern, r'\1\n*No additional historical notes available.*\n', content)

            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

                return True

        return False
    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return False

def main():
    root = Path.cwd()

    print("=" * 70)
    print("FIX TORPEDO PLACEHOLDER NOTES")
    print("=" * 70)

    # Find all torpedo files with placeholder notes
    torpedo_files = []
    for filepath in root.glob('Weapons/Torpedoes/**/*.md'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if re.search(r'## Notes\s*\n\d+\s*\n*$', content):
                torpedo_files.append(filepath)
        except:
            pass

    print(f"\nFound {len(torpedo_files)} torpedo files with placeholder notes")

    # Dry run first
    print("\n## Dry Run - Preview changes...")
    fixed_count = 0
    for filepath in torpedo_files[:5]:  # Show first 5
        if fix_torpedo_notes(filepath, dry_run=True):
            print(f"  - {filepath.relative_to(root)}")
            fixed_count += 1

    if len(torpedo_files) > 5:
        print(f"  ... and {len(torpedo_files) - 5} more files")

    print(f"\nWould fix {len(torpedo_files)} torpedo files")

    # Ask for confirmation
    response = input(f"\nApply changes to {len(torpedo_files)} files? (yes/no): ")

    if response.lower() != 'yes':
        print("[CANCELLED] No changes made")
        return

    # Apply changes
    print("\n## Applying changes...")
    fixed_count = 0

    for filepath in torpedo_files:
        if fix_torpedo_notes(filepath, dry_run=False):
            fixed_count += 1
            if fixed_count <= 10:
                print(f"[OK] {filepath.relative_to(root)}")

    if fixed_count > 10:
        print(f"... and {fixed_count - 10} more files")

    print(f"\n[OK] Fixed {fixed_count} torpedo files")

if __name__ == '__main__':
    main()
