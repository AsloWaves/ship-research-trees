#!/usr/bin/env python3
"""Analyze incomplete files to understand what data is missing"""

from pathlib import Path
import re

def analyze_file(filepath):
    """Analyze what data a file has and what's missing"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        lines = len(content.split('\n'))

        # Check what sections/fields exist
        has_yaml = '---\n' in content
        has_class_name = 'class_name:' in content or 'designation:' in content
        has_specs = any(field in content for field in ['displacement', 'length', 'speed', 'wingspan', 'weight', 'caliber'])
        has_armament = any(field in content for field in ['main_guns', 'armament', 'weapons', 'missiles'])
        has_history = any(keyword in content.lower() for keyword in ['served', 'combat', 'battle', 'commissioned', 'war', 'operation'])

        # Check for completeness field
        completeness = 'stub' if lines < 30 else ('partial' if lines < 60 else 'complete')
        if 'completeness: stub' in content:
            completeness = 'stub'
        elif 'completeness: partial' in content:
            completeness = 'partial'

        # Count YAML fields
        yaml_fields = 0
        if has_yaml:
            yaml_match = re.search(r'---\n(.*?)\n---', content, re.DOTALL)
            if yaml_match:
                yaml_content = yaml_match.group(1)
                yaml_fields = yaml_content.count(':')

        return {
            'lines': lines,
            'completeness': completeness,
            'has_yaml': has_yaml,
            'yaml_fields': yaml_fields,
            'has_class_name': has_class_name,
            'has_specs': has_specs,
            'has_armament': has_armament,
            'has_history': has_history,
            'body_lines': lines - 20 if lines > 20 else 0  # Rough estimate of body content
        }
    except:
        return None

def categorize_file(filepath):
    """Determine file category"""
    path_str = str(filepath).replace('\\', '/')
    if '/Ships/' in path_str:
        return 'Ships'
    elif '/Aircraft/' in path_str:
        return 'Aircraft'
    elif '/Weapons/' in path_str:
        return 'Weapons'
    return 'Other'

root = Path.cwd()

# Find incomplete files
incomplete_files = []
for filepath in root.rglob('*.md'):
    if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
        continue

    path_str = str(filepath).replace('\\', '/')
    if '/Ships/' in path_str or '/Aircraft/' in path_str or '/Weapons/' in path_str:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'completeness: stub' in content or 'completeness: partial' in content:
                incomplete_files.append(filepath)
        except:
            pass

print(f"Found {len(incomplete_files)} incomplete files\n")

# Analyze sample of each type
stub_samples = []
partial_samples = []

for filepath in incomplete_files[:100]:  # Sample first 100
    result = analyze_file(filepath)
    if result:
        result['file'] = str(filepath.relative_to(root))
        result['category'] = categorize_file(filepath)

        if result['completeness'] == 'stub':
            stub_samples.append(result)
        elif result['completeness'] == 'partial':
            partial_samples.append(result)

# Report on stubs
print("=" * 70)
print("STUB FILES ANALYSIS (< 30 lines)")
print("=" * 70)
print(f"\nSample size: {len(stub_samples)} files")

if stub_samples:
    avg_lines = sum(s['lines'] for s in stub_samples) / len(stub_samples)
    avg_yaml_fields = sum(s['yaml_fields'] for s in stub_samples) / len(stub_samples)

    has_yaml_pct = sum(1 for s in stub_samples if s['has_yaml']) / len(stub_samples) * 100
    has_specs_pct = sum(1 for s in stub_samples if s['has_specs']) / len(stub_samples) * 100
    has_armament_pct = sum(1 for s in stub_samples if s['has_armament']) / len(stub_samples) * 100
    has_history_pct = sum(1 for s in stub_samples if s['has_history']) / len(stub_samples) * 100

    print(f"Average lines: {avg_lines:.1f}")
    print(f"Average YAML fields: {avg_yaml_fields:.1f}")
    print(f"\nContent presence:")
    print(f"  - Has YAML: {has_yaml_pct:.1f}%")
    print(f"  - Has specifications: {has_specs_pct:.1f}%")
    print(f"  - Has armament: {has_armament_pct:.1f}%")
    print(f"  - Has history: {has_history_pct:.1f}%")

    print(f"\nCategory breakdown:")
    for category in ['Ships', 'Aircraft', 'Weapons']:
        count = sum(1 for s in stub_samples if s['category'] == category)
        print(f"  - {category}: {count} files")

    print(f"\nSample files:")
    for sample in stub_samples[:5]:
        print(f"  - {sample['file']}")
        print(f"    {sample['lines']} lines, {sample['yaml_fields']} YAML fields")

# Report on partials
print("\n" + "=" * 70)
print("PARTIAL FILES ANALYSIS (30-59 lines)")
print("=" * 70)
print(f"\nSample size: {len(partial_samples)} files")

if partial_samples:
    avg_lines = sum(s['lines'] for s in partial_samples) / len(partial_samples)
    avg_yaml_fields = sum(s['yaml_fields'] for s in partial_samples) / len(partial_samples)

    has_yaml_pct = sum(1 for s in partial_samples if s['has_yaml']) / len(partial_samples) * 100
    has_specs_pct = sum(1 for s in partial_samples if s['has_specs']) / len(partial_samples) * 100
    has_armament_pct = sum(1 for s in partial_samples if s['has_armament']) / len(partial_samples) * 100
    has_history_pct = sum(1 for s in partial_samples if s['has_history']) / len(partial_samples) * 100

    print(f"Average lines: {avg_lines:.1f}")
    print(f"Average YAML fields: {avg_yaml_fields:.1f}")
    print(f"\nContent presence:")
    print(f"  - Has YAML: {has_yaml_pct:.1f}%")
    print(f"  - Has specifications: {has_specs_pct:.1f}%")
    print(f"  - Has armament: {has_armament_pct:.1f}%")
    print(f"  - Has history: {has_history_pct:.1f}%")

    print(f"\nCategory breakdown:")
    for category in ['Ships', 'Aircraft', 'Weapons']:
        count = sum(1 for s in partial_samples if s['category'] == category)
        print(f"  - {category}: {count} files")

    print(f"\nSample files:")
    for sample in partial_samples[:5]:
        print(f"  - {sample['file']}")
        print(f"    {sample['lines']} lines, {sample['yaml_fields']} YAML fields")

print("\n" + "=" * 70)
print("RECOMMENDATIONS")
print("=" * 70)
print()
print("Based on this analysis, here's what incomplete files typically need:")
print()
