#!/usr/bin/env python3
"""Categorize incomplete files by type"""

from pathlib import Path

# Find all incomplete files by category
categories = {
    'Ships': [],
    'Aircraft': [],
    'Torpedoes': [],
    'Naval Guns': [],
    'Missiles': [],
    'Other Weapons': []
}

for filepath in Path('.').rglob('*.md'):
    if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'completeness: stub' in content or 'completeness: partial' in content:
            path_str = str(filepath).replace('\\', '/')

            if '/Ships/' in path_str:
                categories['Ships'].append(filepath)
            elif '/Aircraft/' in path_str:
                categories['Aircraft'].append(filepath)
            elif '/Torpedoes/' in path_str:
                categories['Torpedoes'].append(filepath)
            elif '/Naval-Guns/' in path_str:
                categories['Naval Guns'].append(filepath)
            elif '/Missiles/' in path_str:
                categories['Missiles'].append(filepath)
            elif '/Weapons/' in path_str:
                categories['Other Weapons'].append(filepath)
    except:
        pass

print('Incomplete Files by Category:')
print('=' * 50)
for category, files in categories.items():
    print(f'{category}: {len(files)} files')
    if len(files) > 0 and len(files) <= 3:
        for f in files:
            print(f'  - {str(f)}')

print(f'\nTotal: {sum(len(files) for files in categories.values())} files')

# Show sample from each category
print('\n' + '=' * 50)
print('Sample files from each category:')
print('=' * 50)
for category, files in categories.items():
    if files:
        print(f'\n{category} (showing first 3):')
        for f in files[:3]:
            print(f'  {str(f)}')
