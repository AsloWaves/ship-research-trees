#!/usr/bin/env python3
"""
Validate all markdown files against templates.
Generate compliance report showing which files match template standards.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def check_yaml_format(filepath):
    """Check YAML frontmatter format"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Proper format: starts with --- and ends with ---
        if content.strip().startswith('---\n') and '\n---\n' in content:
            return 'proper'

        # Code block format (not ideal)
        if '```yaml' in content:
            return 'code_block'

        return 'none'
    except:
        return 'error'

def count_lines(filepath):
    """Count lines in file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except:
        return 0

def check_required_sections(filepath, required_sections):
    """Check if file has required section headers"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        missing = []
        for section in required_sections:
            if f'## {section}' not in content:
                missing.append(section)

        return missing
    except:
        return required_sections

def validate_ship(filepath):
    """Validate ship file against template"""
    required_sections = ['Overview', 'Specifications', 'Performance', 'Armament']

    yaml_format = check_yaml_format(filepath)
    lines = count_lines(filepath)
    missing_sections = check_required_sections(filepath, required_sections)

    issues = []
    if yaml_format != 'proper':
        issues.append(f'YAML format: {yaml_format} (should be proper)')
    if lines < 40:
        issues.append(f'Too short: {lines} lines (expected 60-100)')
    if lines > 150:
        issues.append(f'Too long: {lines} lines (expected 60-100)')
    if missing_sections:
        issues.append(f'Missing sections: {", ".join(missing_sections)}')

    return {
        'compliant': len(issues) == 0,
        'yaml_format': yaml_format,
        'lines': lines,
        'missing_sections': missing_sections,
        'issues': issues
    }

def validate_aircraft(filepath):
    """Validate aircraft file against template"""
    required_sections = ['Overview', 'Physical Specifications', 'Performance', 'Armament']

    yaml_format = check_yaml_format(filepath)
    lines = count_lines(filepath)
    missing_sections = check_required_sections(filepath, required_sections)

    issues = []
    if yaml_format != 'proper':
        issues.append(f'YAML format: {yaml_format} (should be proper)')
    if lines < 50:
        issues.append(f'Too short: {lines} lines (expected 80-120, may be incomplete)')
    if missing_sections:
        issues.append(f'Missing sections: {", ".join(missing_sections)}')

    return {
        'compliant': len(issues) == 0,
        'yaml_format': yaml_format,
        'lines': lines,
        'missing_sections': missing_sections,
        'issues': issues
    }

def validate_weapon(filepath):
    """Validate weapon file against template"""
    required_sections = ['Overview', 'Specifications']

    yaml_format = check_yaml_format(filepath)
    lines = count_lines(filepath)
    missing_sections = check_required_sections(filepath, required_sections)

    issues = []
    if yaml_format != 'proper':
        issues.append(f'YAML format: {yaml_format} (should be proper)')
    if lines < 20:
        issues.append(f'Too short: {lines} lines (expected 30-50)')
    if missing_sections:
        issues.append(f'Missing sections: {", ".join(missing_sections)}')

    return {
        'compliant': len(issues) == 0,
        'yaml_format': yaml_format,
        'lines': lines,
        'missing_sections': missing_sections,
        'issues': issues
    }

def main():
    root = Path.cwd()

    print("=" * 70)
    print("FILE VALIDATION AND COMPLIANCE REPORT")
    print("=" * 70)

    # Categorize files
    ships = []
    aircraft = []
    weapons = []

    # Find all markdown files
    for filepath in root.rglob('*.md'):
        # Skip templates, scripts, reports, archive
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
            continue

        # Categorize by path (handle both / and \ for Windows)
        path_str = str(filepath).replace('\\', '/')
        if '/Ships/' in path_str and '/Overviews/' not in path_str:
            ships.append(filepath)
        elif '/Aircraft/' in path_str and '/Research-Trees/' not in path_str:
            aircraft.append(filepath)
        elif '/Weapons/' in path_str and '/Research-Trees/' not in path_str:
            weapons.append(filepath)

    print(f"\nFiles found:")
    print(f"  Ships: {len(ships)}")
    print(f"  Aircraft: {len(aircraft)}")
    print(f"  Weapons: {len(weapons)}")
    print(f"  Total: {len(ships) + len(aircraft) + len(weapons)}")

    # Validate each category
    print("\n## Validating Ships...")
    ship_results = []
    for filepath in ships:
        result = validate_ship(filepath)
        result['file'] = str(filepath.relative_to(root))
        ship_results.append(result)

    print("\n## Validating Aircraft...")
    aircraft_results = []
    for filepath in aircraft:
        result = validate_aircraft(filepath)
        result['file'] = str(filepath.relative_to(root))
        aircraft_results.append(result)

    print("\n## Validating Weapons...")
    weapon_results = []
    for filepath in weapons:
        result = validate_weapon(filepath)
        result['file'] = str(filepath.relative_to(root))
        weapon_results.append(result)

    # Calculate compliance stats
    ship_compliant = sum(1 for r in ship_results if r['compliant'])
    aircraft_compliant = sum(1 for r in aircraft_results if r['compliant'])
    weapon_compliant = sum(1 for r in weapon_results if r['compliant'])

    total_files = len(ships) + len(aircraft) + len(weapons)
    total_compliant = ship_compliant + aircraft_compliant + weapon_compliant

    print(f"\n## Compliance Summary")
    if len(ships) > 0:
        print(f"Ships: {ship_compliant}/{len(ships)} ({100*ship_compliant/len(ships):.1f}%)")
    if len(aircraft) > 0:
        print(f"Aircraft: {aircraft_compliant}/{len(aircraft)} ({100*aircraft_compliant/len(aircraft):.1f}%)")
    if len(weapons) > 0:
        print(f"Weapons: {weapon_compliant}/{len(weapons)} ({100*weapon_compliant/len(weapons):.1f}%)")
    if total_files > 0:
        print(f"TOTAL: {total_compliant}/{total_files} ({100*total_compliant/total_files:.1f}%)")

    # Generate detailed report
    report_path = Path.cwd() / '_Reports' / 'VALIDATION_COMPLIANCE_REPORT.md'

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write('# Validation and Compliance Report\n\n')
        f.write(f'**Generated:** {Path(__file__).name}\n\n')
        f.write(f'**Total Files Validated:** {total_files}\n\n')

        # Summary table
        f.write('## Compliance Summary\n\n')
        f.write('| Category | Compliant | Total | Percentage |\n')
        f.write('|----------|-----------|-------|------------|\n')
        f.write(f'| Ships | {ship_compliant} | {len(ships)} | {100*ship_compliant/len(ships):.1f}% |\n')
        f.write(f'| Aircraft | {aircraft_compliant} | {len(aircraft)} | {100*aircraft_compliant/len(aircraft):.1f}% |\n')
        f.write(f'| Weapons | {weapon_compliant} | {len(weapons)} | {100*weapon_compliant/len(weapons):.1f}% |\n')
        f.write(f'| **TOTAL** | **{total_compliant}** | **{total_files}** | **{100*total_compliant/total_files:.1f}%** |\n\n')

        # Issue breakdown
        f.write('## Issue Breakdown\n\n')

        yaml_issues = sum(1 for r in ship_results + aircraft_results + weapon_results if r['yaml_format'] != 'proper')
        short_files = sum(1 for r in ship_results if r['lines'] < 40) + sum(1 for r in aircraft_results if r['lines'] < 50)
        missing_sections_count = sum(1 for r in ship_results + aircraft_results + weapon_results if r['missing_sections'])

        f.write(f'- **YAML Format Issues**: {yaml_issues} files\n')
        f.write(f'- **Too Short**: {short_files} files (likely incomplete)\n')
        f.write(f'- **Missing Sections**: {missing_sections_count} files\n\n')

        # Non-compliant files
        f.write('## Non-Compliant Files\n\n')

        f.write('### Ships\n\n')
        non_compliant_ships = [r for r in ship_results if not r['compliant']]
        if non_compliant_ships:
            for result in non_compliant_ships[:50]:  # Limit to first 50
                f.write(f'- `{result["file"]}` ({result["lines"]} lines)\n')
                for issue in result['issues']:
                    f.write(f'  - {issue}\n')
        else:
            f.write('All ships compliant! ✅\n')

        f.write(f'\n**Total Ships Non-Compliant:** {len(non_compliant_ships)}\n\n')

        f.write('### Aircraft\n\n')
        non_compliant_aircraft = [r for r in aircraft_results if not r['compliant']]
        if non_compliant_aircraft:
            for result in non_compliant_aircraft[:50]:
                f.write(f'- `{result["file"]}` ({result["lines"]} lines)\n')
                for issue in result['issues']:
                    f.write(f'  - {issue}\n')
        else:
            f.write('All aircraft compliant! ✅\n')

        f.write(f'\n**Total Aircraft Non-Compliant:** {len(non_compliant_aircraft)}\n\n')

        f.write('### Weapons\n\n')
        non_compliant_weapons = [r for r in weapon_results if not r['compliant']]
        if non_compliant_weapons:
            for result in non_compliant_weapons[:50]:
                f.write(f'- `{result["file"]}` ({result["lines"]} lines)\n')
                for issue in result['issues']:
                    f.write(f'  - {issue}\n')
        else:
            f.write('All weapons compliant! ✅\n')

        f.write(f'\n**Total Weapons Non-Compliant:** {len(non_compliant_weapons)}\n\n')

        # Incomplete files (for Phase 5)
        f.write('## Incomplete Files (For Phase 5 Flagging)\n\n')
        incomplete = [r for r in ship_results + aircraft_results if r['lines'] < 50]
        f.write(f'**Total Potentially Incomplete Files:** {len(incomplete)}\n\n')

        for result in incomplete[:100]:  # First 100
            f.write(f'- `{result["file"]}` ({result["lines"]} lines)\n')

    print(f'\n[OK] Report generated: {report_path}')

    return {
        'ships': ship_results,
        'aircraft': aircraft_results,
        'weapons': weapon_results,
        'total_compliant': total_compliant,
        'total_files': total_files
    }

if __name__ == '__main__':
    main()
