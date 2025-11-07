#!/usr/bin/env python3
"""
Master script to generate all weapon markdown files from markdown table databases.
Handles: Torpedoes (236), Missiles (192), Naval Bombs (107)
"""

import os
import re

def sanitize_filename(name):
    """Convert designation to valid filename."""
    name = name.replace('"', 'inch')
    name = name.replace('/', '-').replace('\\', '-').replace(':', '-')
    name = name.replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '-')
    return name.strip()

def process_torpedoes():
    """Process torpedoes from naval_torpedoes_database.md"""
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_torpedoes_database.md"
    output_base = r"D:\Research\Weapons\Torpedoes"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    torpedoes = []
    for line in lines:
        if re.match(r'^\|\s*\d+\s*\|', line):
            fields = [f.strip() for f in line.split('|')]
            if len(fields) >= 19 and fields[1].isdigit():
                torp = {
                    'id': fields[1], 'country': fields[2], 'designation': fields[3],
                    'type': fields[4], 'year': fields[5], 'diameter': fields[6],
                    'length': fields[7], 'weight': fields[8], 'warhead_lbs': fields[9],
                    'warhead_type': fields[10], 'speed': fields[11], 'range': fields[12],
                    'depth': fields[13], 'propulsion': fields[14], 'guidance': fields[15],
                    'platform': fields[16], 'notes': fields[18]
                }
                torpedoes.append(torp)

    created = 0
    for torp in torpedoes:
        nation_dir = os.path.join(output_base, torp['country'])
        os.makedirs(nation_dir, exist_ok=True)

        tags = ['torpedo', torp['type'].lower().replace(' ', '-'), torp['country'].lower()]

        md = f"""---
designation: {torp['designation']}
torpedo_id: {torp['id']}
nation: {torp['country']}
type: {torp['type']}
introduced: {torp['year']}
tags: [{', '.join(tags)}]
---

# {torp['designation']}

## Overview
**Nation**: {torp['country']}
**Type**: {torp['type']}
**Year**: {torp['year']}

## Specifications
- **Diameter**: {torp['diameter']}\"
- **Length**: {torp['length']} ft
- **Weight**: {torp['weight']} lbs
- **Warhead**: {torp['warhead_lbs']} lbs {torp['warhead_type']}
- **Speed**: {torp['speed']} knots
- **Range**: {torp['range']} yards
- **Depth**: {torp['depth']} ft

## Propulsion & Guidance
- **Propulsion**: {torp['propulsion']}
- **Guidance**: {torp['guidance']}
- **Platform**: {torp['platform']}

## Notes
{torp['notes']}
"""

        filepath = os.path.join(nation_dir, sanitize_filename(torp['designation']) + ".md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        created += 1

    return created

def process_missiles():
    """Process missiles from naval_missiles_database.md"""
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_missiles_database.md"
    output_base = r"D:\Research\Weapons\Missiles"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    missiles = []
    for line in lines:
        if re.match(r'^\|\s*2\d+\s*\|', line):  # Missiles start with 2xxx
            fields = [f.strip() for f in line.split('|')]
            if len(fields) >= 17 and fields[1].isdigit():
                miss = {
                    'id': fields[1], 'country': fields[2], 'designation': fields[3],
                    'type': fields[4], 'year': fields[5], 'diameter': fields[6],
                    'length': fields[7], 'range': fields[8], 'warhead': fields[9],
                    'speed': fields[10], 'max_range': fields[11], 'guidance': fields[12],
                    'propulsion': fields[13], 'target': fields[14], 'platform': fields[15]
                }
                missiles.append(miss)

    created = 0
    for miss in missiles:
        nation_dir = os.path.join(output_base, miss['country'])
        os.makedirs(nation_dir, exist_ok=True)

        tags = ['missile', miss['type'].lower().replace(' ', '-'), miss['country'].lower()]

        md = f"""---
designation: {miss['designation']}
missile_id: {miss['id']}
nation: {miss['country']}
type: {miss['type']}
introduced: {miss['year']}
tags: [{', '.join(tags)}]
---

# {miss['designation']}

## Overview
**Nation**: {miss['country']}
**Type**: {miss['type']}
**Year**: {miss['year']}

## Specifications
- **Diameter**: {miss['diameter']}\"
- **Length**: {miss['length']} ft
- **Warhead**: {miss['warhead']} lbs
- **Speed**: Mach {miss['speed']}
- **Range**: {miss['max_range']} nm

## System
- **Propulsion**: {miss['propulsion']}
- **Guidance**: {miss['guidance']}
- **Target**: {miss['target']}
- **Platform**: {miss['platform']}
"""

        filepath = os.path.join(nation_dir, sanitize_filename(miss['designation']) + ".md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        created += 1

    return created

def process_bombs():
    """Process naval bombs from naval_bombs_database.md"""
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_bombs_database.md"
    output_base = r"D:\Research\Weapons\Bombs"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    bombs = []
    for line in lines:
        if re.match(r'^\|\s*9\d+\s*\|', line):  # Bombs start with 9xxx
            fields = [f.strip() for f in line.split('|')]
            if len(fields) >= 24 and fields[1].isdigit():
                bomb = {
                    'id': fields[1], 'nation': fields[2], 'designation': fields[3],
                    'type': fields[4], 'year': fields[5], 'weight': fields[6],
                    'length': fields[7], 'diameter': fields[8], 'explosive_wt': fields[9],
                    'explosive_type': fields[10], 'blast_radius': fields[11],
                    'guidance': fields[13], 'fuse': fields[17], 'platform': fields[18],
                    'notes': fields[22]
                }
                bombs.append(bomb)

    created = 0
    for bomb in bombs:
        nation_dir = os.path.join(output_base, bomb['nation'])
        os.makedirs(nation_dir, exist_ok=True)

        tags = ['bomb', 'naval-bomb', bomb['type'].lower().replace(' ', '-'), bomb['nation'].lower()]

        md = f"""---
designation: {bomb['designation']}
bomb_id: {bomb['id']}
nation: {bomb['nation']}
type: {bomb['type']}
introduced: {bomb['year']}
tags: [{', '.join(tags)}]
---

# {bomb['designation']}

## Overview
**Nation**: {bomb['nation']}
**Type**: {bomb['type']}
**Year**: {bomb['year']}

## Specifications
- **Weight**: {bomb['weight']} lbs
- **Length**: {bomb['length']} ft
- **Diameter**: {bomb['diameter']} ft
- **Explosive**: {bomb['explosive_wt']} lbs {bomb['explosive_type']}
- **Blast Radius**: {bomb['blast_radius']} ft

## System
- **Guidance**: {bomb['guidance']}
- **Fuse**: {bomb['fuse']}
- **Platform**: {bomb['platform']}

## Notes
{bomb['notes']}
"""

        filepath = os.path.join(nation_dir, sanitize_filename(bomb['designation']) + ".md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        created += 1

    return created

def main():
    print("Generating weapon markdown files...")
    print("-" * 50)

    print("\nProcessing torpedoes...")
    torp_count = process_torpedoes()
    print(f"Created {torp_count} torpedo files")

    print("\nProcessing missiles...")
    miss_count = process_missiles()
    print(f"Created {miss_count} missile files")

    print("\nProcessing naval bombs...")
    bomb_count = process_bombs()
    print(f"Created {bomb_count} bomb files")

    print("\n" + "=" * 50)
    print(f"Total: {torp_count + miss_count + bomb_count} markdown files created")
    print("=" * 50)

if __name__ == "__main__":
    main()
