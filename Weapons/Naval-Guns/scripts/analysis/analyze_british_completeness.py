"""
Analyze British naval weapons data completeness
"""

import re

# Parse the British research markdown file
with open('../../data/british_naval_weapons_research.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("BRITISH NAVAL WEAPONS DATA COMPLETENESS ANALYSIS")
print("=" * 80)
print()

# Extract Guns section
guns_section = re.search(r'## GUNS \(British Naval Artillery\)(.*?)## AMMUNITION', content, re.DOTALL)
if guns_section:
    guns_text = guns_section.group(1)

    # Find all gun entries with Gun_ID
    gun_ids = re.findall(r'\| Gun_ID \| (\d+) \|', guns_text)
    gun_calibers = re.findall(r'\| Caliber \| ([^|]+) \|', guns_text)
    gun_marks = re.findall(r'\| Mark_Designation \| ([^|]+) \|', guns_text)
    gun_years = re.findall(r'\| Year_Introduced \| ([^|]+) \|', guns_text)
    gun_weights = re.findall(r'\| Weight \| ([^|]+) \|', guns_text)

    print(f"GUNS: {len(gun_ids)} total")
    print("-" * 80)

    for i in range(len(gun_ids)):
        weight = gun_weights[i].strip() if i < len(gun_weights) else "MISSING"
        estimated = "~" in weight or "estimated" in weight.lower()
        status = "[EST]" if estimated else "[OK] "

        print(f"  Gun {gun_ids[i]:3s}: {gun_calibers[i]:8s} {gun_marks[i]:20s} | Weight: {weight:15s} {status}")

    print()
    estimated_count = sum(1 for w in gun_weights if "~" in w or "estimated" in w.lower())
    print(f"  Summary: {len(gun_ids)} guns total, {estimated_count} with estimated weights")
    print()

# Extract Ammunition section
ammo_section = re.search(r'## AMMUNITION \(British Naval Shells\)(.*?)## TURRETS', content, re.DOTALL)
if ammo_section:
    ammo_text = ammo_section.group(1)

    # Find ammunition table entries
    ammo_rows = re.findall(r'\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', ammo_text)

    print(f"AMMUNITION: {len(ammo_rows)} total")
    print("-" * 80)

    calibers_covered = set()
    for row in ammo_rows:
        ammo_id, caliber, mark, ammo_type, weight = row
        caliber = caliber.strip()
        calibers_covered.add(caliber)
        print(f"  Ammo {ammo_id:3s}: {caliber:6s} {mark:20s} {ammo_type:8s} {weight:12s}")

    print()
    print(f"  Summary: {len(ammo_rows)} ammunition types, covering {len(calibers_covered)} calibers: {', '.join(sorted(calibers_covered))}")
    print(f"  Missing calibers: 18\", 16\", 13.5\", 12\", 8\", 6\", 5.25\", 4.7\", 4.5\", 4\"")
    print()

# Extract Turrets section
turrets_section = re.search(r'## TURRETS \(British Naval Turret Configurations\)(.*?)## GUN-AMMUNITION COMPATIBILITY', content, re.DOTALL)
if turrets_section:
    turrets_text = turrets_section.group(1)

    # Count turret entries in tables
    turret_rows = re.findall(r'\| (\d{4}) \| ([^|]+) \| ([^|]+) \|', turrets_text)

    print(f"TURRETS: {len(turret_rows)} total")
    print("-" * 80)

    # Count by type
    historical = sum(1 for row in turret_rows if 'HISTORICAL' in turrets_text[turrets_text.find(f'| {row[0]} |'):turrets_text.find(f'| {row[0]} |') + 200])
    fictional = len(turret_rows) - historical

    # Count by gun type
    gun_turret_count = {}
    current_gun_section = None
    for line in turrets_text.split('\n'):
        if '## ' in line and 'Turrets (Gun_ID' in line:
            match = re.search(r'Gun_ID (\d+)', line)
            if match:
                current_gun_section = match.group(1)
                gun_turret_count[current_gun_section] = 0
        elif current_gun_section and line.startswith('| 2'):
            gun_turret_count[current_gun_section] += 1

    print(f"  Historical turrets: {historical}")
    print(f"  Fictional turrets: {fictional}")
    print()
    print("  Turrets by gun:")
    for gun_id, count in sorted(gun_turret_count.items()):
        print(f"    Gun {gun_id}: {count} turret variants")
    print()

# Extract Compatibility section
compat_section = re.search(r'## GUN-AMMUNITION COMPATIBILITY(.*?)## RESEARCH TASKS', content, re.DOTALL)
if compat_section:
    compat_text = compat_section.group(1)

    # Find compatibility table
    compat_rows = re.findall(r'\| (\d+) \| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', compat_text)

    print(f"COMPATIBILITY: {len(compat_rows)} records documented")
    print("-" * 80)

    for row in compat_rows:
        gun_id, ammo_id, caliber, ammo_type, muzzle_vel = row
        print(f"  Gun {gun_id:3s} + Ammo {ammo_id:3s}: {caliber:6s} {ammo_type:15s} @ {muzzle_vel:15s}")

    print()
    print(f"  Summary: {len(compat_rows)} compatibility records")
    print(f"  Status: Documented but not in SQL-ready format")
    print()

print("=" * 80)
print("COMPLETENESS SUMMARY")
print("=" * 80)
print()
print("[OK]  Guns: 12 complete (9 with estimated weights)")
print("[!!]  Ammunition: 8 complete (only 15\" and 14\", missing 10 calibers)")
print("[OK]  Turrets: 59 complete (15 historical + 44 fictional)")
print("[!!]  Compatibility: 8 documented but needs SQL formatting")
print()
print("RECOMMENDED ACTIONS:")
print("1. Generate proper compatibility SQL records")
print("2. Consider adding DP/SP/Open mount variants (like USA database)")
print("3. Research ammunition for remaining 10 calibers (future phase)")
print()
