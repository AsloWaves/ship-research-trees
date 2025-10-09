"""
Analyze existing turret data to find patterns for estimation
"""

import re

def parse_caliber(designation):
    """Extract caliber from turret designation"""
    match = re.search(r'(\d+\.?\d*)"', designation)
    if match:
        return float(match.group(1))
    return None

def parse_turret_type(turret_type):
    """Normalize turret type"""
    turret_type = turret_type.lower()
    if 'single' in turret_type:
        return 'Single'
    elif 'twin' in turret_type or 'double' in turret_type:
        return 'Twin'
    elif 'triple' in turret_type:
        return 'Triple'
    elif 'quad' in turret_type:
        return 'Quad'
    return 'Unknown'

# Read the file
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find turrets table section
turrets_start = None
turrets_end = None
for i, line in enumerate(lines):
    if '## Turrets Table' in line:
        turrets_start = i
    elif turrets_start and '## Gun Ammunition Compatibility' in line:
        turrets_end = i
        break

# Find header
header_idx = None
for i in range(turrets_start, turrets_end):
    if lines[i].strip().startswith('|') and 'Turret_ID' in lines[i]:
        header_idx = i
        break

# Parse header
header_line = lines[header_idx]
header_cols = [col.strip() for col in header_line.split('|')[1:-1]]

# Get column indices
turret_id_idx = header_cols.index('Turret_ID')
designation_idx = header_cols.index('Designation')
turret_type_idx = header_cols.index('Turret_Type')
weight_idx = header_cols.index('Turret_Weight_Tons')
crew_idx = header_cols.index('Crew_Size')
armor_face_idx = header_cols.index('Armor_Face_IN')
armor_sides_idx = header_cols.index('Armor_Sides_IN')
armor_roof_idx = header_cols.index('Armor_Roof_IN')
traverse_idx = header_cols.index('Traverse_Rate_Deg_Sec')
elevation_rate_idx = header_cols.index('Elevation_Rate_Deg_Sec')

# Parse data
data_start = header_idx + 2
turrets = []

for i in range(data_start, turrets_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue

    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(header_cols):
        continue

    turret = {
        'id': cols[turret_id_idx],
        'designation': cols[designation_idx],
        'type': parse_turret_type(cols[turret_type_idx]),
        'type_raw': cols[turret_type_idx],
        'weight': float(cols[weight_idx]) if cols[weight_idx] else None,
        'crew': int(cols[crew_idx]) if cols[crew_idx] else None,
        'armor_face': float(cols[armor_face_idx]) if cols[armor_face_idx] else None,
        'armor_sides': float(cols[armor_sides_idx]) if cols[armor_sides_idx] else None,
        'armor_roof': float(cols[armor_roof_idx]) if cols[armor_roof_idx] else None,
        'traverse': float(cols[traverse_idx]) if cols[traverse_idx] else None,
        'elevation_rate': float(cols[elevation_rate_idx]) if cols[elevation_rate_idx] else None,
        'caliber': parse_caliber(cols[designation_idx])
    }
    turrets.append(turret)

print("=" * 80)
print("TURRET DATA ANALYSIS - EXISTING DATA PATTERNS")
print("=" * 80)
print()

# Analyze by caliber and type
print("CREW SIZE ANALYSIS (18 of 60 filled)")
print("-" * 80)
crew_data = [t for t in turrets if t['crew'] is not None]
print(f"Found {len(crew_data)} turrets with crew data:\n")

# Group by caliber
by_caliber = {}
for t in crew_data:
    cal = t['caliber']
    if cal:
        if cal not in by_caliber:
            by_caliber[cal] = []
        by_caliber[cal].append(t)

for cal in sorted(by_caliber.keys(), reverse=True):
    print(f"{cal}\" guns ({len(by_caliber[cal])} turrets):")
    for t in by_caliber[cal]:
        print(f"  ID {t['id']:3s} | {t['type']:6s} | Crew: {t['crew']:3d} | Weight: {t['weight']:6.1f}T | {t['designation']}")
    print()

# Analyze crew per gun barrel
print("\nCREW PER GUN BARREL RATIO:")
print("-" * 80)
barrel_count = {'Single': 1, 'Twin': 2, 'Triple': 3, 'Quad': 4}
for t in crew_data:
    if t['type'] in barrel_count:
        crew_per_barrel = t['crew'] / barrel_count[t['type']]
        print(f"ID {t['id']:3s} | {t['caliber']:4.1f}\" {t['type']:6s} | {t['crew']:3d} crew / {barrel_count[t['type']]} guns = {crew_per_barrel:.1f} per barrel")

print("\n" + "=" * 80)
print("ARMOR DATA ANALYSIS")
print("-" * 80)
armor_data = [t for t in turrets if t['armor_face'] is not None or t['armor_sides'] is not None or t['armor_roof'] is not None]
print(f"Found {len(armor_data)} turrets with any armor data:\n")

by_caliber_armor = {}
for t in armor_data:
    cal = t['caliber']
    if cal:
        if cal not in by_caliber_armor:
            by_caliber_armor[cal] = []
        by_caliber_armor[cal].append(t)

for cal in sorted(by_caliber_armor.keys(), reverse=True):
    print(f"{cal}\" guns ({len(by_caliber_armor[cal])} turrets):")
    for t in by_caliber_armor[cal]:
        face = f"{t['armor_face']:.1f}\"" if t['armor_face'] else "???"
        sides = f"{t['armor_sides']:.1f}\"" if t['armor_sides'] else "???"
        roof = f"{t['armor_roof']:.1f}\"" if t['armor_roof'] else "???"
        print(f"  ID {t['id']:3s} | {t['type']:6s} | Armor: F={face:6s} S={sides:6s} R={roof:6s} | {t['designation']}")
    print()

# Analyze armor ratios
print("\nARMOR THICKNESS RATIOS (Face : Sides : Roof):")
print("-" * 80)
for t in armor_data:
    if t['armor_face'] and t['armor_sides'] and t['armor_roof']:
        face = t['armor_face']
        sides = t['armor_sides']
        roof = t['armor_roof']
        # Normalize to face = 100
        ratio_s = (sides / face * 100) if face > 0 else 0
        ratio_r = (roof / face * 100) if face > 0 else 0
        print(f"ID {t['id']:3s} | {t['caliber']:4.1f}\" {t['type']:6s} | {face:5.1f}:{sides:5.1f}:{roof:5.1f} = 100:{ratio_s:.0f}:{ratio_r:.0f} | {t['designation']}")

print("\n" + "=" * 80)
print("TRAVERSE/ELEVATION RATE ANALYSIS")
print("-" * 80)
rate_data = [t for t in turrets if t['traverse'] is not None or t['elevation_rate'] is not None]
print(f"Found {len(rate_data)} turrets with rate data:\n")

for t in rate_data:
    trav = f"{t['traverse']:.1f}°/s" if t['traverse'] else "???"
    elev = f"{t['elevation_rate']:.1f}°/s" if t['elevation_rate'] else "???"
    print(f"ID {t['id']:3s} | {t['caliber']:4.1f}\" {t['type']:6s} | Traverse: {trav:8s} Elevation: {elev:8s} | {t['designation']}")

print("\n" + "=" * 80)
print("MISSING DATA BY CALIBER")
print("-" * 80)

# Group all turrets by caliber
all_by_caliber = {}
for t in turrets:
    cal = t['caliber']
    if cal:
        if cal not in all_by_caliber:
            all_by_caliber[cal] = []
        all_by_caliber[cal].append(t)

for cal in sorted(all_by_caliber.keys(), reverse=True):
    turret_list = all_by_caliber[cal]
    total = len(turret_list)

    crew_count = sum(1 for t in turret_list if t['crew'] is not None)
    armor_count = sum(1 for t in turret_list if t['armor_face'] is not None)
    rate_count = sum(1 for t in turret_list if t['traverse'] is not None)

    print(f"{cal:4.1f}\" - {total:2d} turrets | Crew: {crew_count:2d}/{total:2d} | Armor: {armor_count:2d}/{total:2d} | Rates: {rate_count:2d}/{total:2d}")

print("\n" + "=" * 80)
print("RECOMMENDATION: RESEARCH TARGETS")
print("-" * 80)
print("Priority turrets to research (high-value, commonly referenced):")
print()

# Identify key turrets to research (large calibers, complete data)
priority_calibers = [16.0, 14.0, 8.0, 5.0, 3.0]  # Major US naval gun calibers
for cal in priority_calibers:
    if cal in all_by_caliber:
        missing_turrets = [t for t in all_by_caliber[cal] if t['crew'] is None or t['armor_face'] is None]
        if missing_turrets:
            print(f"{cal}\" guns - {len(missing_turrets)} turrets need data:")
            for t in missing_turrets[:3]:  # Show top 3
                crew_status = "OK" if t['crew'] else "MISSING"
                armor_status = "OK" if t['armor_face'] else "MISSING"
                rate_status = "OK" if t['traverse'] else "MISSING"
                print(f"  ID {t['id']:3s} | Crew:{crew_status:7s} Armor:{armor_status:7s} Rates:{rate_status:7s} | {t['designation']}")
            if len(missing_turrets) > 3:
                print(f"  ... and {len(missing_turrets) - 3} more")
            print()

print("=" * 80)
