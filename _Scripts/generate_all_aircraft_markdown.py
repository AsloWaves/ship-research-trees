#!/usr/bin/env python3
"""
Generate markdown files for naval and ground aircraft from markdown table databases.
Handles: Naval Aircraft (144), Ground Aircraft (147)
"""

import os
import re

def sanitize_filename(name):
    """Convert designation to valid filename."""
    name = name.replace('"', 'inch')
    name = name.replace('/', '-').replace('\\', '-').replace(':', '-')
    name = name.replace('*', '').replace('?', '').replace('<', '').replace('>', '').replace('|', '-')
    return name.strip()

def process_naval_aircraft():
    """Process naval aircraft from naval_aircraft_database.md"""
    input_file = r"D:\Research\Weapons\Naval-Guns\database\naval_aircraft_database.md"
    output_base = r"D:\Research\Aircraft\Naval"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    aircraft = []
    for line in lines:
        if re.match(r'^\|\s*3\d+\s*\|', line):  # Naval aircraft IDs start with 3xxx
            fields = [f.strip() for f in line.split('|')]
            if len(fields) >= 19 and fields[1].isdigit():
                # Based on actual data format observed
                ac = {
                    'id': fields[1], 'country': fields[2], 'designation': fields[3],
                    'year': fields[4], 'type': fields[5], 'wingspan': fields[6],
                    'length': fields[7], 'empty_weight': fields[8], 'max_weight': fields[9],
                    'max_speed': fields[10], 'cruise_speed': fields[11], 'ceiling': fields[12],
                    'engine': fields[13], 'carrier': fields[16], 'role': fields[17]
                }
                aircraft.append(ac)

    created = 0
    os.makedirs(output_base, exist_ok=True)

    for ac in aircraft:
        tags = ['naval-aircraft', ac['type'].lower().replace(' ', '-'), ac['country'].lower()]

        md = f"""---
designation: {ac['designation']}
aircraft_id: {ac['id']}
nation: {ac['country']}
type: {ac['type']}
introduced: {ac['year']}
tags: [{', '.join(tags)}]
---

# {ac['designation']}

## Overview
**Nation**: {ac['country']}
**Type**: {ac['type']}
**Role**: {ac['role']}
**Year**: {ac['year']}

## Physical Specifications
- **Wingspan**: {ac['wingspan']} ft
- **Length**: {ac['length']} ft
- **Empty Weight**: {ac['empty_weight']} lbs
- **Max Takeoff Weight**: {ac['max_weight']} lbs

## Performance
- **Maximum Speed**: {ac['max_speed']} mph
- **Cruise Speed**: {ac['cruise_speed']} mph
- **Service Ceiling**: {ac['ceiling']} ft

## Powerplant
- **Engine**: {ac['engine']}

## Carrier Operations
- **Carrier Capable**: {ac['carrier']}
"""

        filepath = os.path.join(output_base, sanitize_filename(ac['designation']) + ".md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        created += 1

    return created

def process_ground_aircraft():
    """Process ground aircraft from ground_aircraft_database.md"""
    input_file = r"D:\Research\Weapons\Naval-Guns\database\ground_aircraft_database.md"
    output_base = r"D:\Research\Aircraft\Ground"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    aircraft = []
    for line in lines:
        if re.match(r'^\|\s*4\d+\s*\|', line):  # Ground aircraft IDs start with 4xxx
            fields = [f.strip() for f in line.split('|')]
            if len(fields) >= 19 and fields[1].isdigit():
                ac = {
                    'id': fields[1], 'country': fields[2], 'designation': fields[3],
                    'year': fields[4], 'type': fields[5], 'wingspan': fields[6],
                    'length': fields[7], 'empty_weight': fields[8], 'max_weight': fields[9],
                    'max_speed': fields[10], 'cruise_speed': fields[11], 'ceiling': fields[12],
                    'engine': fields[13], 'range': fields[14] if len(fields) > 14 else 'N/A',
                    'role': fields[15] if len(fields) > 15 else 'Multi-role'
                }
                aircraft.append(ac)

    created = 0
    os.makedirs(output_base, exist_ok=True)

    for ac in aircraft:
        tags = ['ground-aircraft', ac['type'].lower().replace(' ', '-'), ac['country'].lower()]

        md = f"""---
designation: {ac['designation']}
aircraft_id: {ac['id']}
nation: {ac['country']}
type: {ac['type']}
introduced: {ac['year']}
tags: [{', '.join(tags)}]
---

# {ac['designation']}

## Overview
**Nation**: {ac['country']}
**Type**: {ac['type']}
**Role**: {ac['role']}
**Year**: {ac['year']}

## Physical Specifications
- **Wingspan**: {ac['wingspan']} ft
- **Length**: {ac['length']} ft
- **Empty Weight**: {ac['empty_weight']} lbs
- **Max Takeoff Weight**: {ac['max_weight']} lbs

## Performance
- **Maximum Speed**: {ac['max_speed']} mph
- **Cruise Speed**: {ac['cruise_speed']} mph
- **Service Ceiling**: {ac['ceiling']} ft
- **Range**: {ac['range']} nm

## Powerplant
- **Engine**: {ac['engine']}
"""

        filepath = os.path.join(output_base, sanitize_filename(ac['designation']) + ".md")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md)
        created += 1

    return created

def main():
    print("Generating aircraft markdown files...")
    print("-" * 50)

    print("\nProcessing naval aircraft...")
    naval_count = process_naval_aircraft()
    print(f"Created {naval_count} naval aircraft files")

    print("\nProcessing ground aircraft...")
    ground_count = process_ground_aircraft()
    print(f"Created {ground_count} ground aircraft files")

    print("\n" + "=" * 50)
    print(f"Total: {naval_count + ground_count} aircraft markdown files created")
    print("=" * 50)

if __name__ == "__main__":
    main()
