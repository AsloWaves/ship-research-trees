#!/usr/bin/env python3
"""Find files with YAML format issues"""

import os
from pathlib import Path

def check_yaml_format(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.strip().startswith('---\n') and '\n---\n' in content:
            return 'proper'
        if content.startswith('# ') and '\n\n---\n' in content and '\n---\n' in content:
            return 'proper'
        if '```yaml' in content:
            return 'code_block'
        return 'none'
    except:
        return 'error'

root = Path.cwd()
bad_files = []

for filepath in root.rglob('*.md'):
    if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
        continue
    path_str = str(filepath).replace('\\', '/')
    if '/Ships/' in path_str or '/Aircraft/' in path_str or '/Weapons/' in path_str:
        yaml_format = check_yaml_format(filepath)
        if yaml_format != 'proper':
            bad_files.append((str(filepath.relative_to(root)), yaml_format))

print(f'Files with YAML format issues: {len(bad_files)}\n')
for file, fmt in bad_files:
    print(f'{file}: {fmt}')
