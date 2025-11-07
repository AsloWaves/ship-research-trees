#!/usr/bin/env python3
"""
Find and analyze duplicate markdown files in the repository.
Generates a report showing:
- Which files are duplicated
- Where the duplicates are located
- Content differences
- Recommendations on which to keep
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import hashlib

def get_md5(filepath):
    """Get MD5 hash of file content"""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def extract_yaml_frontmatter(filepath):
    """Extract YAML frontmatter from a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check for YAML frontmatter
        match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
        if match:
            return match.group(1)

        # Check for YAML in code block
        match = re.search(r'^```yaml\s*\n---\s*\n(.*?)\n---\s*\n```', content, re.DOTALL | re.MULTILINE)
        if match:
            return match.group(1)

        return None
    except:
        return None

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

def get_file_stats(filepath):
    """Get basic file statistics"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return {
            'lines': len(content.split('\n')),
            'chars': len(content),
            'has_game_stats': '## Game Statistics' in content,
            'has_notes': '## Notes' in content,
            'yaml_format': check_yaml_format(filepath)
        }
    except:
        return None

def find_all_duplicates(root_dir):
    """Find all duplicate .md files by filename"""
    files_by_name = defaultdict(list)

    for filepath in Path(root_dir).rglob('*.md'):
        # Skip templates
        if '_Templates' in str(filepath):
            continue
        if '_Scripts' in str(filepath):
            continue

        filename = filepath.name
        files_by_name[filename].append(filepath)

    # Filter to only duplicates
    duplicates = {name: paths for name, paths in files_by_name.items() if len(paths) > 1}

    return duplicates

def analyze_duplicate_group(filename, filepaths):
    """Analyze a group of duplicate files"""
    analysis = {
        'filename': filename,
        'count': len(filepaths),
        'locations': [],
        'same_content': False,
        'recommended_keep': None,
        'reason': ''
    }

    # Get info for each file
    file_infos = []
    md5_hashes = []

    for filepath in filepaths:
        md5 = get_md5(filepath)
        stats = get_file_stats(filepath)

        info = {
            'path': str(filepath),
            'relative_path': str(filepath.relative_to(Path.cwd())),
            'md5': md5,
            'stats': stats
        }
        file_infos.append(info)
        md5_hashes.append(md5)

    analysis['locations'] = file_infos

    # Check if all have same content
    if len(set(md5_hashes)) == 1:
        analysis['same_content'] = True
        analysis['recommended_keep'] = file_infos[0]['relative_path']
        analysis['reason'] = 'All files identical - keep any, delete others'
    else:
        # Different content - need to decide which to keep
        # Prefer: proper YAML format > longer content > has game stats

        scores = []
        for info in file_infos:
            score = 0
            if info['stats']:
                # Proper YAML format gets highest priority
                if info['stats']['yaml_format'] == 'proper':
                    score += 1000
                elif info['stats']['yaml_format'] == 'code_block':
                    score += 500

                # More content is better
                score += info['stats']['lines']

                # Having game stats is good
                if info['stats']['has_game_stats']:
                    score += 200

                # Having notes is good
                if info['stats']['has_notes']:
                    score += 100

            scores.append((score, info))

        # Sort by score descending
        scores.sort(reverse=True, key=lambda x: x[0])

        best = scores[0][1]
        analysis['recommended_keep'] = best['relative_path']

        reasons = []
        if best['stats'] and best['stats']['yaml_format'] == 'proper':
            reasons.append('proper YAML format')
        if best['stats'] and best['stats']['has_game_stats']:
            reasons.append('has game statistics')
        if best['stats']:
            reasons.append(f"{best['stats']['lines']} lines")

        analysis['reason'] = 'Best format and content: ' + ', '.join(reasons)

    return analysis

def main():
    root = Path.cwd()

    print("Finding duplicate .md files...")
    duplicates = find_all_duplicates(root)

    print(f"\nFound {len(duplicates)} duplicate filenames ({sum(len(paths) for paths in duplicates.values())} total files)")

    # Analyze each duplicate group
    analyses = []
    for filename, filepaths in sorted(duplicates.items()):
        analysis = analyze_duplicate_group(filename, filepaths)
        analyses.append(analysis)

    # Generate report
    report_path = Path.cwd() / '_Reports' / 'DUPLICATE_FILES_ANALYSIS.md'
    report_path.parent.mkdir(exist_ok=True)

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('# Duplicate Files Analysis Report\n\n')
        f.write(f'**Total Duplicate Filenames:** {len(duplicates)}\n\n')
        f.write(f'**Total Files Involved:** {sum(len(paths) for paths in duplicates.values())}\n\n')

        # Categorize duplicates
        same_content = [a for a in analyses if a['same_content']]
        different_content = [a for a in analyses if not a['same_content']]

        f.write(f'**Identical Content:** {len(same_content)} groups (safe to delete duplicates)\n\n')
        f.write(f'**Different Content:** {len(different_content)} groups (need manual review)\n\n')

        f.write('---\n\n')

        # Same content duplicates
        f.write('## Identical Content Duplicates (Safe to Delete)\n\n')
        f.write('These files have identical content. Keep one, delete others.\n\n')

        for analysis in same_content:
            f.write(f'### {analysis["filename"]} ({analysis["count"]} copies)\n\n')
            f.write('**Locations:**\n')
            for loc in analysis['locations']:
                f.write(f'- `{loc["relative_path"]}`\n')
            f.write(f'\n**Recommendation:** Keep `{analysis["recommended_keep"]}`, delete others\n\n')

        # Different content duplicates
        f.write('\n---\n\n')
        f.write('## Different Content Duplicates (Need Review)\n\n')
        f.write('These files have different content. Review and merge/decide.\n\n')

        for analysis in different_content:
            f.write(f'### {analysis["filename"]} ({analysis["count"]} versions)\n\n')
            f.write('**Versions:**\n\n')
            for loc in analysis['locations']:
                stats = loc['stats']
                if stats:
                    f.write(f'- `{loc["relative_path"]}`\n')
                    f.write(f'  - Lines: {stats["lines"]}, YAML: {stats["yaml_format"]}, ')
                    f.write(f'Game Stats: {"Yes" if stats["has_game_stats"] else "No"}, ')
                    f.write(f'Notes: {"Yes" if stats["has_notes"] else "No"}\n')

            f.write(f'\n**Recommended Keep:** `{analysis["recommended_keep"]}`\n')
            f.write(f'**Reason:** {analysis["reason"]}\n\n')

    print(f'\nReport generated: {report_path}')
    print(f'\nSummary:')
    print(f'  - Identical content: {len(same_content)} groups')
    print(f'  - Different content: {len(different_content)} groups')
    print(f'  - Total files that can be deleted: {sum(a["count"]-1 for a in same_content)}')

    return analyses

if __name__ == '__main__':
    main()
