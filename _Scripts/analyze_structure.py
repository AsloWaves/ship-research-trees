#!/usr/bin/env python3
"""Analyze file structures to understand markdown section usage"""

from pathlib import Path

def analyze_structure(filepath):
    """Check what structure type a file uses"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Count markdown sections (## headers)
        markdown_sections = content.count('\n## ')

        # Check if has YAML
        has_yaml = '---\n' in content

        # Check if has bold headers in body (**Header:**)
        has_bold_headers = '**' in content

        return {
            'markdown_sections': markdown_sections,
            'has_yaml': has_yaml,
            'has_bold_headers': has_bold_headers
        }
    except:
        return None

root = Path.cwd()
structure_counts = {
    'yaml_only': 0,  # YAML + bold headers, no markdown sections
    'markdown_sections': 0,  # Has markdown sections (1+)
    'hybrid': 0,  # Has both markdown sections and YAML
    'no_yaml': 0  # No YAML at all
}

all_files = []
for filepath in root.rglob('*.md'):
    if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
        continue
    path_str = str(filepath).replace('\\', '/')
    if '/Ships/' in path_str or '/Aircraft/' in path_str or '/Weapons/' in path_str:
        all_files.append(filepath)

for filepath in all_files:
    result = analyze_structure(filepath)
    if result:
        if not result['has_yaml']:
            structure_counts['no_yaml'] += 1
        elif result['markdown_sections'] == 0:
            structure_counts['yaml_only'] += 1
        else:
            structure_counts['markdown_sections'] += 1
            if result['has_yaml']:
                structure_counts['hybrid'] += 1

print(f"Total files analyzed: {len(all_files)}\n")
print("Structure Types:")
print(f"  YAML-only (no markdown sections): {structure_counts['yaml_only']}")
print(f"  With markdown sections: {structure_counts['markdown_sections']}")
print(f"    - Hybrid (YAML + sections): {structure_counts['hybrid']}")
print(f"  No YAML at all: {structure_counts['no_yaml']}")
