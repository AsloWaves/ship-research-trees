"""
Analyze which guns have which turret configurations
Identify gaps for generating fictional variants
"""

import re
from collections import defaultdict

def parse_caliber(text):
    """Extract caliber from text"""
    match = re.search(r'(\d+\.?\d*)"', text)
    if match:
        return match.group(1)
    return None

def parse_mark(text):
    """Extract Mark designation"""
    # Look for "Mark X" patterns
    match = re.search(r'Mark\s+(\S+)', text, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

# Read database
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find guns section
guns_start = None
guns_end = None
for i, line in enumerate(lines):
    if '## Guns Table' in line:
        guns_start = i
    elif guns_start and '## Ammunition Table' in line:
        guns_end = i
        break

# Parse guns
guns_header_idx = None
for i in range(guns_start, guns_end):
    if lines[i].strip().startswith('|') and 'Gun_ID' in lines[i]:
        guns_header_idx = i
        break

guns_header = [col.strip() for col in lines[guns_header_idx].split('|')[1:-1]]
gun_id_idx = guns_header.index('Gun_ID')
caliber_idx = guns_header.index('Caliber')
mark_idx = guns_header.index('Mark_Designation')
modded_idx = guns_header.index('Modded')

guns = {}
guns_data_start = guns_header_idx + 2

for i in range(guns_data_start, guns_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(guns_header):
        continue

    gun_id = cols[gun_id_idx]
    caliber = cols[caliber_idx]
    mark = cols[mark_idx]
    modded = cols[modded_idx]

    # Only include non-modded guns for generation
    if modded == '0':
        key = f"{caliber} {mark}"
        guns[gun_id] = {
            'id': gun_id,
            'caliber': caliber,
            'mark': mark,
            'key': key
        }

# Find turrets section
turrets_start = None
turrets_end = None
for i, line in enumerate(lines):
    if '## Turrets Table' in line:
        turrets_start = i
    elif turrets_start and '## Gun Ammunition Compatibility' in line:
        turrets_end = i
        break

# Parse turrets
turrets_header_idx = None
for i in range(turrets_start, turrets_end):
    if lines[i].strip().startswith('|') and 'Turret_ID' in lines[i]:
        turrets_header_idx = i
        break

turrets_header = [col.strip() for col in lines[turrets_header_idx].split('|')[1:-1]]
turret_gun_id_idx = turrets_header.index('Gun_ID')
turret_type_idx = turrets_header.index('Turret_Type')
turret_modded_idx = turrets_header.index('Modded')

# Track which guns have which turret types
gun_turret_coverage = defaultdict(set)
turrets_data_start = turrets_header_idx + 2

for i in range(turrets_data_start, turrets_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(turrets_header):
        continue

    gun_id = cols[turret_gun_id_idx]
    turret_type = cols[turret_type_idx].lower()
    modded = cols[turret_modded_idx]

    # Normalize turret type
    if 'single' in turret_type:
        config = 'Single'
    elif 'twin' in turret_type or 'double' in turret_type or 'dual' in turret_type:
        config = 'Twin'
    elif 'triple' in turret_type:
        config = 'Triple'
    elif 'quad' in turret_type:
        config = 'Quad'
    else:
        config = 'Unknown'

    gun_turret_coverage[gun_id].add(config)

# Analyze coverage
print("=" * 80)
print("GUN-TURRET CONFIGURATION COVERAGE ANALYSIS")
print("=" * 80)
print()

all_configs = {'Single', 'Twin', 'Triple', 'Quad'}
missing_configs = []

for gun_id, gun_data in sorted(guns.items(), key=lambda x: (x[1]['caliber'], x[1]['mark'])):
    caliber = gun_data['caliber']
    mark = gun_data['mark']
    existing = gun_turret_coverage.get(gun_id, set())
    missing = all_configs - existing

    if missing:
        status_str = "  ".join([f"{c:6s}" + ("[Y]" if c in existing else "[N]") for c in ['Single', 'Twin', 'Triple', 'Quad']])
        print(f"Gun {gun_id:3s} | {caliber:5s} Mark {mark:10s} | {status_str} | Missing: {', '.join(sorted(missing))}")

        for config in sorted(missing):
            missing_configs.append({
                'gun_id': gun_id,
                'caliber': caliber,
                'mark': mark,
                'config': config,
                'key': gun_data['key']
            })

print()
print("=" * 80)
print(f"SUMMARY: {len(missing_configs)} turret configurations need to be generated")
print("=" * 80)

# Group by configuration type
by_config = defaultdict(list)
for item in missing_configs:
    by_config[item['config']].append(item)

for config in ['Single', 'Twin', 'Triple', 'Quad']:
    if config in by_config:
        print(f"\n{config} turrets to generate: {len(by_config[config])}")
        for item in by_config[config][:5]:  # Show first 5
            print(f"  - {item['caliber']} Mark {item['mark']} (Gun ID {item['gun_id']})")
        if len(by_config[config]) > 5:
            print(f"  ... and {len(by_config[config]) - 5} more")

# Save missing configs for generation script
import json
with open('missing_turret_configs.json', 'w') as f:
    json.dump(missing_configs, f, indent=2)

print()
print("=" * 80)
print("Missing configurations saved to: missing_turret_configs.json")
print("=" * 80)
