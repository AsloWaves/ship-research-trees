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

        # Check if file has ```yaml code block wrapper around YAML
        if '```yaml' not in content:
            return []

        # Pattern 1: ```yaml\n---\nYAML content\n---\n```
        # Convert to: ---\nYAML content\n---
        pattern1 = r'(.*?)```yaml\s*\n(---\s*\n.*?\n---)\s*\n```\s*\n(.*)$'
        match1 = re.match(pattern1, content, re.DOTALL)

        if match1:
            before_part = match1.group(1)  # Content before ```yaml
            yaml_part = match1.group(2)    # The --- ... --- block
            body_part = match1.group(3)    # Content after ```

            new_content = f"{before_part}{yaml_part}\n\n{body_part}"

            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

            changes.append('Converted code block YAML (with ---) to proper format')
            return changes

        # Pattern 2: ```yaml\nkey: value\n...\n```  (NO --- delimiters)
        # Convert to: ---\nkey: value\n...\n---
        pattern2 = r'(.*?)```yaml\s*\n(.*?)\n```\s*\n(.*)$'
        match2 = re.match(pattern2, content, re.DOTALL)

        if match2:
            before_part = match2.group(1)  # Content before ```yaml
            yaml_content = match2.group(2)  # The YAML content (no delimiters)
            body_part = match2.group(3)     # Content after ```

            # Add --- delimiters
            new_content = f"{before_part}---\n{yaml_content}\n---\n\n{body_part}"

            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)

            changes.append('Converted code block YAML (no ---) to proper format')
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
