"""
Generate DP/SP/Open mount variants for British turrets (3-6" caliber range)
Following USA database pattern
"""

import re

# Read the British research file
with open('../../data/british_naval_weapons_research.md', 'r', encoding='utf-8') as f:
    content = f.read()

print("=" * 80)
print("BRITISH TURRET VARIANTS GENERATION (DP/SP/OPEN)")
print("=" * 80)
print()

# Parse existing turrets
turrets = []
turret_sections = re.findall(r'## (.+?) Turrets \(Gun_ID (\d+)\)(.*?)(?=##|$)', content, re.DOTALL)

for section_name, gun_id, section_content in turret_sections:
    # Find turret table rows
    rows = re.findall(r'\| (\d+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', section_content)

    for row in rows:
        turret_id, turret_type, weight, crew, armor, traverse, elevation, rof, modded = row
        turrets.append({
            'Turret_ID': int(turret_id.strip()),
            'Gun_ID': int(gun_id),
            'Type': turret_type.strip(),
            'Weight': weight.strip(),
            'Crew': crew.strip(),
            'Armor': armor.strip(),
            'Traverse': traverse.strip(),
            'Elevation': elevation.strip(),
            'ROF': rof.strip(),
            'Modded': modded.strip()
        })

print(f"Loaded {len(turrets)} existing turrets")
print()

# Identify guns that should get DP/SP/Open variants (3-6" caliber)
# Gun IDs: 530 (6"), 540 (5.25"), 545 (4.7"), 550 (4.5"), 555 (4")
variant_guns = {
    530: {'caliber': '6"', 'name': '6"/50 Mark XXIII', 'dp_sp_open': True},
    540: {'caliber': '5.25"', 'name': '5.25"/50 Mark I', 'dp_sp_open': True},  # Already DP, but add SP/Open
    545: {'caliber': '4.7"', 'name': '4.7"/45 Mark IX/XII', 'dp_sp_open': True},
    550: {'caliber': '4.5"', 'name': '4.5"/45 Mark V', 'dp_sp_open': True},
    555: {'caliber': '4"', 'name': '4"/45 QF Mark V/XVI', 'dp_sp_open': True}
}

# Get base turrets for each gun (use existing Single/Twin/Triple/Quad as templates)
base_turrets = {}
for gun_id in variant_guns.keys():
    base_turrets[gun_id] = [t for t in turrets if t['Gun_ID'] == gun_id]

print("Base turrets by gun:")
for gun_id, gun_turrets in base_turrets.items():
    print(f"  Gun {gun_id} ({variant_guns[gun_id]['name']}): {len(gun_turrets)} base turrets")
print()

# Generate new variants
new_turrets = []
next_turret_id = 2200  # Start after existing British turrets (2001-2115)

# DP/SP scaling factors (from USA database)
dp_weight_mult = 1.15
dp_traverse_mult = 0.9
dp_elevation_rate_mult = 1.3
dp_elevation_max = 85.0

sp_weight_mult = 0.90
sp_traverse_mult = 1.1
sp_elevation_rate_mult = 0.8
sp_elevation_max = 40.0

open_weight_mult = 0.55
open_traverse_mult = 1.5
open_elevation_rate_mult = 1.5
open_crew_mult = 0.7
open_armor = '0.25/0/0'

print("GENERATING DP VARIANTS (High-angle AA capable)")
print("-" * 80)

dp_count = 0
for gun_id, gun_turrets in base_turrets.items():
    gun_name = variant_guns[gun_id]['name']

    # Skip 5.25" DP variants (already DP designed)
    if gun_id == 540:
        print(f"  Gun {gun_id} ({gun_name}): Skipping DP (already dual-purpose)")
        continue

    # Skip 4" DP variants (already high-angle AA)
    if gun_id == 555:
        print(f"  Gun {gun_id} ({gun_name}): Skipping DP (already HA/AA)")
        continue

    for base in gun_turrets:
        # Skip if already a special variant
        if 'Mark' in base['Type'] or 'HA' in base['Type']:
            continue

        # Parse values
        try:
            base_weight = float(base['Weight'].strip())
            base_crew = int(base['Crew'].strip())
            base_traverse = float(base['Traverse'].strip())
            elevation_parts = base['Elevation'].strip().split('/')
            elevation_min = float(elevation_parts[0])

            # Parse elevation rate if present
            elevation_rate = 0.0
            if base['Elevation'].count('/') > 1:
                # Format might be: -5/+70 or similar
                pass

            # Create DP variant
            dp_turret = {
                'Turret_ID': next_turret_id,
                'Gun_ID': gun_id,
                'Type': f"{base['Type']} DP",
                'Weight': round(base_weight * dp_weight_mult, 1),
                'Crew': base_crew,  # Same crew
                'Armor': base['Armor'],  # Same armor
                'Traverse': round(base_traverse * dp_traverse_mult, 1),
                'Elevation': f"{elevation_min}/{dp_elevation_max}",
                'ROF': base['ROF'],  # Same ROF
                'Modded': '1',
                'Notes': f"Dual-purpose variant of Turret {base['Turret_ID']} - high-angle AA capable"
            }

            new_turrets.append(dp_turret)
            dp_count += 1
            next_turret_id += 1

            if dp_count <= 5:
                print(f"  Turret {dp_turret['Turret_ID']}: {gun_name} {dp_turret['Type']} | Weight: {dp_turret['Weight']}T | Elev: {dp_turret['Elevation']}")

        except (ValueError, IndexError) as e:
            print(f"  WARNING: Could not parse Turret {base['Turret_ID']}: {e}")
            continue

print(f"  ... generated {dp_count} DP variants")
print()

print("GENERATING SP VARIANTS (Surface-only, faster)")
print("-" * 80)

sp_count = 0
for gun_id, gun_turrets in base_turrets.items():
    gun_name = variant_guns[gun_id]['name']

    for base in gun_turrets:
        # Skip if already a special variant
        if 'Mark' in base['Type'] or 'HA' in base['Type'] or 'DP' in base['Type']:
            continue

        # Parse values
        try:
            base_weight = float(base['Weight'].strip())
            base_crew = int(base['Crew'].strip())
            base_traverse = float(base['Traverse'].strip())
            elevation_parts = base['Elevation'].strip().split('/')
            elevation_min = float(elevation_parts[0])

            # Create SP variant
            sp_turret = {
                'Turret_ID': next_turret_id,
                'Gun_ID': gun_id,
                'Type': f"{base['Type']} SP",
                'Weight': round(base_weight * sp_weight_mult, 1),
                'Crew': base_crew,  # Same crew
                'Armor': base['Armor'],  # Same armor
                'Traverse': round(base_traverse * sp_traverse_mult, 1),
                'Elevation': f"{elevation_min}/{sp_elevation_max}",
                'ROF': base['ROF'],  # Same ROF
                'Modded': '1',
                'Notes': f"Single-purpose surface variant of Turret {base['Turret_ID']} - lighter, faster traverse"
            }

            new_turrets.append(sp_turret)
            sp_count += 1
            next_turret_id += 1

            if sp_count <= 5:
                print(f"  Turret {sp_turret['Turret_ID']}: {gun_name} {sp_turret['Type']} | Weight: {sp_turret['Weight']}T | Elev: {sp_turret['Elevation']}")

        except (ValueError, IndexError) as e:
            print(f"  WARNING: Could not parse Turret {base['Turret_ID']}: {e}")
            continue

print(f"  ... generated {sp_count} SP variants")
print()

print("GENERATING OPEN MOUNT VARIANTS (Minimal armor, very light)")
print("-" * 80)

open_count = 0
for gun_id, gun_turrets in base_turrets.items():
    gun_name = variant_guns[gun_id]['name']

    # Only 3-5" guns get open mounts
    if gun_id == 530:  # Skip 6" (too large for open mounts)
        print(f"  Gun {gun_id} ({gun_name}): Skipping Open (too large)")
        continue

    for base in gun_turrets:
        # Skip if already a special variant
        if 'Mark' in base['Type'] or 'HA' in base['Type'] or 'DP' in base['Type'] or 'SP' in base['Type']:
            continue

        # Parse values
        try:
            base_weight = float(base['Weight'].strip())
            base_crew = int(base['Crew'].strip())
            base_traverse = float(base['Traverse'].strip())
            elevation_parts = base['Elevation'].strip().split('/')
            elevation_min = float(elevation_parts[0])
            elevation_max = float(elevation_parts[1].replace('+', ''))

            # Create Open mount variant
            open_turret = {
                'Turret_ID': next_turret_id,
                'Gun_ID': gun_id,
                'Type': f"{base['Type']} Open Mount",
                'Weight': round(base_weight * open_weight_mult, 1),
                'Crew': int(base_crew * open_crew_mult),
                'Armor': open_armor,
                'Traverse': round(base_traverse * open_traverse_mult, 1),
                'Elevation': f"{elevation_min}/{elevation_max}",  # Keep original elevation
                'ROF': base['ROF'],  # Same ROF
                'Modded': '1',
                'Notes': f"Open mount variant of Turret {base['Turret_ID']} - minimal armor, light weight, fast traverse"
            }

            new_turrets.append(open_turret)
            open_count += 1
            next_turret_id += 1

            if open_count <= 5:
                print(f"  Turret {open_turret['Turret_ID']}: {gun_name} {open_turret['Type']} | Weight: {open_turret['Weight']}T | Crew: {open_turret['Crew']}")

        except (ValueError, IndexError) as e:
            print(f"  WARNING: Could not parse Turret {base['Turret_ID']}: {e}")
            continue

print(f"  ... generated {open_count} Open mount variants")
print()

print("=" * 80)
print(f"GENERATION COMPLETE")
print("=" * 80)
print()
print(f"Total new turret variants: {len(new_turrets)}")
print(f"  DP variants:   {dp_count}")
print(f"  SP variants:   {sp_count}")
print(f"  Open mounts:   {open_count}")
print()
print(f"New Turret ID range: 2200-{next_turret_id-1}")
print()

# Save to file
output_file = '../../data/british_turret_variants_generated.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# British Turret Variants - DP/SP/Open Mount\n\n")
    f.write(f"**Generated**: {len(new_turrets)} new turret variants\n")
    f.write(f"**Turret ID Range**: 2200-{next_turret_id-1}\n\n")
    f.write("---\n\n")

    # Group by gun
    for gun_id in sorted(variant_guns.keys()):
        gun_variants = [t for t in new_turrets if t['Gun_ID'] == gun_id]
        if not gun_variants:
            continue

        gun_name = variant_guns[gun_id]['name']
        f.write(f"## {gun_name} (Gun_ID {gun_id})\n\n")

        # Write table
        f.write("| Turret_ID | Type | Weight (tons) | Crew | Armor (F/S/R in) | Traverse (°/s) | Elevation | ROF (rpm) | Modded | Notes |\n")
        f.write("|-----------|------|---------------|------|------------------|----------------|-----------|-----------|--------|-------|\n")

        for turret in gun_variants:
            f.write(f"| {turret['Turret_ID']} | {turret['Type']} | {turret['Weight']} | {turret['Crew']} | {turret['Armor']} | {turret['Traverse']} | {turret['Elevation']} | {turret['ROF']} | {turret['Modded']} | {turret['Notes']} |\n")

        f.write("\n")

print(f"[SUCCESS] Saved to: {output_file}")
print()
