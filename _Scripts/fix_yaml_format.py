#!/usr/bin/env python3
"""
Auto-fix YAML formatting issues:
1. Convert ```yaml code blocks to proper --- delimited frontmatter
2. Fix section headers that might be inside YAML blocks
3. Add completeness field to incomplete files (Phase 5)
"""

import os
import re
import sys
from pathlib import Path

def fix_yaml_format(filepath, dry_run=True):
    """Convert code block YAML to proper --- delimited frontmatter"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        changes = []

        # Pattern: # Title\n\n```yaml\n---\nYAML content\n---\n```\n\nBody
        # Convert to: # Title\n\n---\nYAML content\n---\n\nBody

        # Check if file has ```yaml code block wrapper around YAML
        if '```yaml' in content[:100] and content.count('```') >= 2:
            # Try to extract the YAML content from the code block
            # Pattern: ```yaml followed by --- ... --- followed by ```
            pattern = r'(.*?)```yaml\s*\n(---\s*\n.*?\n---)\s*\n```\s*\n(.*)$'
            match = re.match(pattern, content, re.DOTALL)

            if match:
                before_part = match.group(1)  # Content before ```yaml (usually # Title\n\n)
                yaml_part = match.group(2)    # The --- ... --- block
                body_part = match.group(3)    # Content after ```

                # Reconstruct with proper format
                new_content = f"{before_part}{yaml_part}\n\n{body_part}"

                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                changes.append('Converted code block YAML to proper --- format')
                return changes

        return []

    except Exception as e:
        print(f"[ERROR] {filepath}: {e}")
        return []

def add_completeness_field(filepath, line_count, dry_run=True):
    """Add completeness field to YAML frontmatter for incomplete files"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine completeness
        if line_count < 30:
            completeness = 'stub'
        elif line_count < 60:
            completeness = 'partial'
        else:
            completeness = 'complete'

        # Only add if file is incomplete and doesn't already have completeness field
        if completeness != 'complete' and 'completeness:' not in content:
            # Find end of YAML frontmatter
            match = re.search(r'^---\s*\n(.*?\n)---', content, re.DOTALL)

            if match:
                yaml_content = match.group(1)

                # Add completeness field before closing ---
                new_yaml = yaml_content.rstrip() + f'\ncompleteness: {completeness}\n'

                new_content = content.replace(match.group(0), f'---\n{new_yaml}---')

                if not dry_run:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)

                return f'Added completeness: {completeness}'

        return None

    except Exception as e:
        return None

def main():
    root = Path.cwd()

    print("=" * 70)
    print("AUTO-FIX FORMATTING ISSUES")
    print("=" * 70)

    # Find all markdown files
    all_files = []
    for filepath in root.rglob('*.md'):
        # Skip templates, scripts, reports, archive
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
            continue

        path_str = str(filepath).replace('\\', '/')
        if '/Ships/' in path_str or '/Aircraft/' in path_str or '/Weapons/' in path_str:
            all_files.append(filepath)

    print(f"\nFound {len(all_files)} files to process")

    # Phase 6: Fix YAML format
    print("\n## Phase 6: Fixing YAML format (code blocks -> proper delimiters)")

    yaml_fixed = 0
    for filepath in all_files:
        changes = fix_yaml_format(filepath, dry_run=True)

        if changes:
            yaml_fixed += 1

    print(f"\nWould fix YAML format in {yaml_fixed} files")

    # Phase 5: Add completeness field to incomplete files
    print("\n## Phase 5: Adding completeness field to incomplete files")

    completeness_added = 0
    stub_count = 0
    partial_count = 0

    for filepath in all_files:
        try:
            line_count = sum(1 for _ in open(filepath, encoding='utf-8'))

            if line_count < 60:  # Potentially incomplete
                result = add_completeness_field(filepath, line_count, dry_run=True)

                if result:
                    completeness_added += 1
                    if 'stub' in result:
                        stub_count += 1
                    elif 'partial' in result:
                        partial_count += 1
        except:
            pass

    print(f"\nWould add completeness field to {completeness_added} files:")
    print(f"  - stub: {stub_count} files (< 30 lines)")
    print(f"  - partial: {partial_count} files (30-59 lines)")

    # Ask for confirmation
    print("\n" + "=" * 70)

    # Check for auto-approve flag
    if '--yes' in sys.argv or '-y' in sys.argv:
        print(f"Auto-approving changes to {yaml_fixed + completeness_added} files")
        response = 'yes'
    else:
        response = input(f"Apply these changes to {yaml_fixed + completeness_added} files? (yes/no): ")

    if response.lower() != 'yes':
        print("[CANCELLED] No changes made")
        return

    # Apply changes
    print("\n## Applying changes...")

    yaml_fixed_actual = 0
    completeness_added_actual = 0

    for filepath in all_files:
        # Fix YAML format
        changes = fix_yaml_format(filepath, dry_run=False)
        if changes:
            yaml_fixed_actual += 1
            print(f"[YAML] {filepath.relative_to(root)}")

        # Add completeness field
        try:
            line_count = sum(1 for _ in open(filepath, encoding='utf-8'))

            if line_count < 60:
                result = add_completeness_field(filepath, line_count, dry_run=False)

                if result:
                    completeness_added_actual += 1
                    print(f"[COMP] {filepath.relative_to(root)}: {result}")
        except:
            pass

    print(f"\n[OK] Fixed YAML format: {yaml_fixed_actual} files")
    print(f"[OK] Added completeness: {completeness_added_actual} files")

if __name__ == '__main__':
    main()
