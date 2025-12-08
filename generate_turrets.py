#!/usr/bin/env python3
"""
Turret Generation Script for UK, Germany, Japan
Creates MD files for turret configurations based on gun data
"""

import os
import re
import glob

# Turret ID counters for each nation (using requested format: UK-XXXX, DE-XXXX, JP-XXXX)
NATION_CONFIG = {
    'Britain': {'prefix': 'UK', 'start_id': 1000, 'folder': 'Britain'},
    'Germany': {'prefix': 'DE', 'start_id': 1000, 'folder': 'Germany'},
    'Japan': {'prefix': 'JP', 'start_id': 1000, 'folder': 'Japan'}
}

# Turret type multipliers for specifications (based on historical data)
TURRET_CONFIGS = {
    'Single': {
        'weight_mult': 0.35,  # Single turret ~35% of quad weight
        'crew_mult': 0.3,
        'armor_face': 0.8,
        'armor_side': 0.6,
        'armor_roof': 0.5
    },
    'Twin': {
        'weight_mult': 0.55,  # Twin ~55% of quad
        'crew_mult': 0.5,
        'armor_face': 0.9,
        'armor_side': 0.7,
        'armor_roof': 0.6
    },
    'Triple': {
        'weight_mult': 0.8,  # Triple ~80% of quad
        'crew_mult': 0.75,
        'armor_face': 1.0,
        'armor_side': 0.85,
        'armor_roof': 0.75
    },
    'Quad': {
        'weight_mult': 1.0,
        'crew_mult': 1.0,
        'armor_face': 1.0,
        'armor_side': 1.0,
        'armor_roof': 1.0
    }
}

# Base specifications by caliber (in inches) - researched values
CALIBER_BASE_SPECS = {
    # Main battery (15"+)
    18: {'base_weight': 2500, 'crew': 95, 'face': 18, 'side': 12, 'roof': 8, 'traverse': 2, 'elev_range': (-3, 30), 'elev_rate': 5, 'rof': 1.5},
    16: {'base_weight': 1600, 'crew': 80, 'face': 16, 'side': 10, 'roof': 7, 'traverse': 2.5, 'elev_range': (-3, 40), 'elev_rate': 6, 'rof': 2},
    15: {'base_weight': 800, 'crew': 75, 'face': 15, 'side': 9, 'roof': 6, 'traverse': 2, 'elev_range': (-5, 30), 'elev_rate': 5, 'rof': 2},
    14: {'base_weight': 1550, 'crew': 70, 'face': 15, 'side': 9, 'roof': 6, 'traverse': 2, 'elev_range': (-3, 40), 'elev_rate': 8, 'rof': 2},
    # Heavy cruiser (8-13")
    13.5: {'base_weight': 600, 'crew': 55, 'face': 12, 'side': 8, 'roof': 5, 'traverse': 3, 'elev_range': (-5, 35), 'elev_rate': 6, 'rof': 2.5},
    12: {'base_weight': 450, 'crew': 50, 'face': 11, 'side': 7, 'roof': 4.5, 'traverse': 3, 'elev_range': (-5, 30), 'elev_rate': 6, 'rof': 2.5},
    10: {'base_weight': 250, 'crew': 40, 'face': 8, 'side': 5, 'roof': 3, 'traverse': 4, 'elev_range': (-5, 35), 'elev_rate': 8, 'rof': 3},
    9.2: {'base_weight': 200, 'crew': 35, 'face': 6, 'side': 4, 'roof': 2.5, 'traverse': 4, 'elev_range': (-5, 35), 'elev_rate': 8, 'rof': 3},
    8: {'base_weight': 180, 'crew': 30, 'face': 5, 'side': 3, 'roof': 2, 'traverse': 5, 'elev_range': (-5, 45), 'elev_rate': 10, 'rof': 4},
    7.5: {'base_weight': 150, 'crew': 28, 'face': 4.5, 'side': 2.5, 'roof': 1.8, 'traverse': 5, 'elev_range': (-5, 45), 'elev_rate': 10, 'rof': 4.5},
    # Light cruiser (5-6")
    6: {'base_weight': 90, 'crew': 22, 'face': 4, 'side': 2, 'roof': 1.5, 'traverse': 6, 'elev_range': (-5, 60), 'elev_rate': 12, 'rof': 8},
    5.25: {'base_weight': 75, 'crew': 20, 'face': 2, 'side': 1.5, 'roof': 1, 'traverse': 8, 'elev_range': (-5, 70), 'elev_rate': 15, 'rof': 8},
    5: {'base_weight': 50, 'crew': 15, 'face': 1.5, 'side': 1, 'roof': 0.75, 'traverse': 10, 'elev_range': (-5, 85), 'elev_rate': 15, 'rof': 12},
    # Secondary/AA (3-4.7")
    4.7: {'base_weight': 25, 'crew': 12, 'face': 1, 'side': 0.5, 'roof': 0.4, 'traverse': 12, 'elev_range': (-5, 80), 'elev_rate': 18, 'rof': 12},
    4.5: {'base_weight': 22, 'crew': 10, 'face': 0.8, 'side': 0.4, 'roof': 0.3, 'traverse': 14, 'elev_range': (-5, 85), 'elev_rate': 20, 'rof': 15},
    4: {'base_weight': 15, 'crew': 8, 'face': 0.6, 'side': 0.3, 'roof': 0.2, 'traverse': 15, 'elev_range': (-5, 80), 'elev_rate': 20, 'rof': 15},
    3: {'base_weight': 5, 'crew': 5, 'face': 0.4, 'side': 0.2, 'roof': 0.1, 'traverse': 20, 'elev_range': (-5, 85), 'elev_rate': 25, 'rof': 20},
}

# Metric caliber mapping (cm to inches approx)
METRIC_TO_INCH = {
    # German calibers
    48: 18.9, 42: 16.5, 40.6: 16, 38: 15, 33: 13, 30: 11.8, 28: 11, 24: 9.4,
    21: 8.3, 20.3: 8, 18: 7.1, 17: 6.7, 15: 5.9, 13.5: 5.3, 12.8: 5, 12.7: 5,
    12: 4.7, 11.5: 4.5, 10.5: 4.1, 10: 3.9, 9: 3.5, 8.8: 3.5, 7.5: 3,
    6: 2.4, 5: 2, 4: 1.6, 3.7: 1.5, 3: 1.2, 2.5: 1, 2: 0.8, 1.5: 0.6,
    # Japanese calibers
    51: 20, 50: 19.7, 46: 18.1, 45: 17.7, 43: 16.9, 41: 16.1, 40: 15.7,
    38: 15, 36: 14.2, 35.6: 14, 35: 13.8, 30.5: 12, 28: 11, 25.4: 10,
    23: 9.1, 22: 8.7, 19: 7.5, 16: 6.3, 14: 5.5, 13.5: 5.3, 13: 5.1,
    11: 4.3, 8: 3.1, 7.7: 3, 7.6: 3, 7.5: 3, 4.7: 1.9, 2.5: 1, 2: 0.8,
    1.5: 0.6, 1.3: 0.5,
}


def parse_caliber(caliber_str):
    """Parse caliber string to numeric value in inches"""
    caliber_str = caliber_str.strip()

    # Handle inch format: 15", 5.25", etc
    if '"' in caliber_str:
        return float(caliber_str.replace('"', ''))

    # Handle metric (cm): 38cm, 20.3cm, etc
    if 'cm' in caliber_str.lower():
        cm_val = float(caliber_str.lower().replace('cm', ''))
        return METRIC_TO_INCH.get(cm_val, cm_val / 2.54)

    # Handle mm: 25mm
    if 'mm' in caliber_str.lower():
        mm_val = float(caliber_str.lower().replace('mm', ''))
        return mm_val / 25.4

    # Try to parse as number (assume inches for British, cm for others)
    try:
        val = float(caliber_str)
        if val > 30:  # Probably mm
            return val / 25.4
        elif val > 20:  # Probably cm
            return val / 2.54
        return val
    except:
        return 5.0  # Default


def get_base_specs(caliber_inches):
    """Get base specifications for a caliber"""
    # Find closest matching caliber
    closest = min(CALIBER_BASE_SPECS.keys(), key=lambda x: abs(x - caliber_inches))
    return CALIBER_BASE_SPECS[closest].copy()


def read_gun_file(filepath):
    """Read gun file and extract data"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {}
    # Extract YAML frontmatter
    yaml_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if yaml_match:
        yaml_content = yaml_match.group(1)
        for line in yaml_content.split('\n'):
            if ':' in line:
                key, val = line.split(':', 1)
                data[key.strip()] = val.strip().strip('"\'')

    # Extract notes for additional data
    notes_match = re.search(r'## Notes\s*\n(.+)', content, re.DOTALL)
    if notes_match:
        data['notes'] = notes_match.group(1).strip()

    return data


def generate_turret_content(gun_data, turret_type, turret_id, nation_prefix):
    """Generate turret MD file content"""
    designation = gun_data.get('designation', 'Unknown')
    gun_id = gun_data.get('gun_id', '0')
    nation = gun_data.get('nation', 'Unknown')
    caliber = gun_data.get('caliber', '5"')
    mark = gun_data.get('mark', 'Unknown')
    year = gun_data.get('year', 'Unknown')
    notes = gun_data.get('notes', '')

    # Parse caliber
    caliber_inches = parse_caliber(caliber)

    # Get base specs and apply turret type multipliers
    base = get_base_specs(caliber_inches)
    config = TURRET_CONFIGS[turret_type]

    weight = round(base['base_weight'] * config['weight_mult'], 2)
    crew = max(3, round(base['crew'] * config['crew_mult']))
    face_armor = round(base['face'] * config['armor_face'], 2)
    side_armor = round(base['side'] * config['armor_side'], 2)
    roof_armor = round(base['roof'] * config['armor_roof'], 2)
    traverse = base['traverse']
    elev_min, elev_max = base['elev_range']
    elev_rate = base['elev_rate']
    rof = base['rof']

    # Create turret designation
    turret_designation = f"{caliber} {mark} {turret_type} Turret"

    # Create tags
    cal_tag = caliber.replace('"', 'inch').replace('cm', 'cm').replace('.', '-').lower()
    nation_tag = nation.lower()
    type_tag = turret_type.lower()

    # Determine if specs are estimated
    completeness = "estimated"
    est_note = "Specifications estimated based on caliber and historical patterns."

    # Check if notes contain actual turret data
    if notes:
        notes_lower = notes.lower()
        if 'turret' in notes_lower and ('tons' in notes_lower or 'rpm' in notes_lower):
            completeness = "partial"
            est_note = "Some specifications from historical sources, others estimated."

    content = f'''---
designation: {turret_designation}
turret_id: {nation_prefix}-{turret_id}
gun_id: {gun_id}
nation: {nation}
caliber: {caliber}
turret_type: {turret_type}
tags: [{cal_tag}, {type_tag}, {nation_tag}, turret]
completeness: {completeness}
---

# {turret_designation}

## Overview

**Turret ID**: {nation_prefix}-{turret_id}
**Gun ID**: {gun_id} (See Guns database)
**Nation**: {nation}
**Caliber**: {caliber}
**Turret Type**: {turret_type}

## Physical Specifications

- **Turret Weight**: {weight:.2f} tons
- **Crew Size**: {crew} personnel

## Armor Protection

- **Face Armor**: {face_armor:.2f} inches
- **Side Armor**: {side_armor:.2f} inches
- **Roof Armor**: {roof_armor:.2f} inches

## Performance

- **Traverse Rate**: {traverse:.2f} deg/sec
- **Elevation Range**: {elev_min:.2f}deg to {elev_max:.2f}deg
- **Elevation Rate**: {elev_rate:.2f} deg/sec
- **Rate of Fire**: {rof:.2f} rounds/min/gun

## Associated Gun

This turret mounts the {designation} gun.
See Gun ID {gun_id} in the Guns database for weapon specifications.

## Compatible Ammunition

Uses ammunition for {caliber} caliber guns.
See the Ammunition database for compatible shells.

## Notes

{est_note}

'''
    return content


def generate_turrets_for_nation(nation, guns_path, turrets_path):
    """Generate all turret files for a nation"""
    config = NATION_CONFIG[nation]
    prefix = config['prefix']
    current_id = config['start_id']

    gun_files = glob.glob(os.path.join(guns_path, '*.md'))
    turret_types = ['Single', 'Twin', 'Triple', 'Quad']

    created = 0
    for gun_file in sorted(gun_files):
        gun_data = read_gun_file(gun_file)

        for turret_type in turret_types:
            content = generate_turret_content(gun_data, turret_type, current_id, prefix)

            # Create filename (sanitize for filesystem)
            caliber = gun_data.get('caliber', '5inch').replace('"', 'inch').replace('/', '-')
            mark = gun_data.get('mark', 'Unknown').replace(' ', '-').replace('/', '-')
            # Remove invalid filename characters
            for char in ['*', '?', '<', '>', '|', ':', '\\', '/', '(', ')', '"', "'"]:
                caliber = caliber.replace(char, '')
                mark = mark.replace(char, '')
            filename = f"{prefix}-{current_id}-{caliber}-{mark}-{turret_type}.md"
            filepath = os.path.join(turrets_path, filename)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            current_id += 1
            created += 1

    return created


def main():
    base_path = "D:/Research/Weapons/Naval-Weapons/Naval-Guns"

    for nation in ['Japan']:  # Britain and Germany already done
        guns_path = os.path.join(base_path, 'Guns', nation)
        turrets_path = os.path.join(base_path, 'Turrets', nation)

        if not os.path.exists(guns_path):
            print(f"Guns path not found: {guns_path}")
            continue

        os.makedirs(turrets_path, exist_ok=True)

        count = generate_turrets_for_nation(nation, guns_path, turrets_path)
        print(f"{nation}: Created {count} turret files")


if __name__ == '__main__':
    main()
