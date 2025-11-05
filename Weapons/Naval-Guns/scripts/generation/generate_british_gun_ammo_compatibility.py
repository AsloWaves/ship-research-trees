"""
Generate Gun-Ammunition Compatibility for Expanded British Guns
Links 35 gun variants to 80 ammunition types

Strategy: Match guns to ammunition by caliber
- Multiple gun variants share the same ammunition types
- Compatibility records link Gun_ID to Ammunition_ID
"""

import sys

# Import gun variants
exec(open('generate_british_gun_variants.py', 'r', encoding='utf-8').read())

# Import ammunition data
exec(open('generate_complete_british_ammunition.py', 'r', encoding='utf-8').read())
exec(open('generate_british_fictional_ammunition.py', 'r', encoding='utf-8').read())

# Combine all ammunition
all_ammunition = ammunition_data + fictional_ammunition

print("=" * 80)
print("GENERATING GUN-AMMUNITION COMPATIBILITY")
print("=" * 80)
print()
print(f"Guns to link:        {len(british_gun_variants)}")
print(f"Ammunition types:    {len(all_ammunition)}")
print()

# Build compatibility records
compatibility_records = []
compatibility_id = 10081  # Start after existing 10001-10080

# Group ammunition by caliber for easy lookup
ammo_by_caliber = {}
for ammo in all_ammunition:
    cal = ammo['Caliber']
    if cal not in ammo_by_caliber:
        ammo_by_caliber[cal] = []
    ammo_by_caliber[cal].append(ammo)

print("Ammunition available by caliber:")
for cal in sorted(ammo_by_caliber.keys()):
    print(f"  {cal:8s}: {len(ammo_by_caliber[cal])} ammunition types")
print()

# Generate compatibility records
print("Generating compatibility records...")
for gun in british_gun_variants:
    gun_id = gun['Gun_ID']
    gun_cal = gun['Caliber']
    gun_mark = gun['Mark_Designation']

    # Find matching ammunition for this caliber
    if gun_cal in ammo_by_caliber:
        for ammo in ammo_by_caliber[gun_cal]:
            compat = {
                'Compatibility_ID': compatibility_id,
                'Gun_ID': gun_id,
                'Ammunition_ID': ammo['Ammunition_ID'],
                'Caliber': gun_cal,
                'Muzzle_Velocity_FPS': ammo['Muzzle_Velocity_FPS'],
                'Muzzle_Velocity_MPS': ammo['Muzzle_Velocity_MPS'],
                'Max_Range_Yards': ammo['Max_Range_Yards'],
                'Notes': f"{gun_cal} {gun_mark} + {ammo['Projectile_Type']} - {ammo['Notes']}"
            }
            compatibility_records.append(compat)
            compatibility_id += 1

print(f"Generated {len(compatibility_records)} compatibility records")
print(f"Compatibility IDs: 10081-{compatibility_id - 1}")
print()

# Statistics
print("Compatibility breakdown by caliber:")
compat_by_cal = {}
for compat in compatibility_records:
    cal = compat['Caliber']
    if cal not in compat_by_cal:
        compat_by_cal[cal] = 0
    compat_by_cal[cal] += 1

for cal in sorted(compat_by_cal.keys()):
    print(f"  {cal:8s}: {compat_by_cal[cal]:3d} compatibility records")
print()

# Verify all guns have ammunition
guns_with_ammo = set([c['Gun_ID'] for c in compatibility_records])
guns_without_ammo = [g for g in british_gun_variants if g['Gun_ID'] not in guns_with_ammo]

if guns_without_ammo:
    print("[WARNING] Guns without ammunition:")
    for gun in guns_without_ammo:
        print(f"  Gun {gun['Gun_ID']}: {gun['Caliber']} {gun['Mark_Designation']}")
else:
    print("[OK] All guns have ammunition linkages")
print()

# Generate SQL INSERT statements
sql_output_file = '../../database/sql/insert_british_gun_ammo_compatibility.sql'

with open(sql_output_file, 'w', encoding='utf-8') as f:
    f.write("""-- ================================================================================
-- BRITISH GUN-AMMUNITION COMPATIBILITY - EXPANDED DATABASE
-- ================================================================================
-- Links 35 gun variants to 80 ammunition types
-- Compatibility IDs: 10081 and up
-- Previous IDs: 10001-10080 (original 12 guns)
-- ================================================================================

""")

    for compat in compatibility_records:
        notes_escaped = compat['Notes'].replace("'", "''")
        f.write(f"INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Notes)\n")
        f.write(f"VALUES ({compat['Compatibility_ID']}, {compat['Gun_ID']}, {compat['Ammunition_ID']}, '{compat['Caliber']}', {compat['Muzzle_Velocity_FPS']}, {compat['Muzzle_Velocity_MPS']}, {compat['Max_Range_Yards']}, '{notes_escaped}');\n\n")

print(f"SQL file generated: {sql_output_file}")
print()

# Also generate markdown summary
md_output_file = '../../data/BRITISH_GUN_VARIANTS_SUMMARY.md'

with open(md_output_file, 'w', encoding='utf-8') as f:
    f.write("""# British Naval Gun Variants - Complete Summary

## Database Expansion

**Original Database**: 12 British guns (one per caliber)
**Expanded Database**: 35 British guns (all Mark variants)
**Growth**: +23 guns (+192%)

## Comparison with USA Database

| Navy | Guns | Strategy |
|------|------|----------|
| **USA** | 83 | Every Mark variant documented |
| **British** | 35 | All Mark variants documented |
| **Ratio** | 2.4:1 | USA has more 5" variants (15 variants across /51, /38, /54, /25 calibers) |

## Gun Variants by Caliber

""")

    for cal in sorted(ammo_by_caliber.keys(), key=lambda x: float(x.replace('"', '').replace('.', '')), reverse=True):
        guns_in_cal = [g for g in british_gun_variants if g['Caliber'] == cal]
        f.write(f"### {cal} Guns ({len(guns_in_cal)} variants)\n\n")
        for gun in guns_in_cal:
            f.write(f"- **{gun['Mark_Designation']}** (Gun_ID {gun['Gun_ID']}, {gun['Year_Introduced']}): {gun['Notes'][:100]}...\n")
        f.write(f"\n**Ammunition**: {len(ammo_by_caliber[cal])} types available\n")
        f.write(f"**Compatibility Records**: {compat_by_cal.get(cal, 0)} gun-ammo combinations\n\n")

    f.write(f"""
## Compatibility Statistics

- **Total Compatibility Records**: {len(compatibility_records)}
- **Compatibility ID Range**: 10081-{compatibility_id - 1}
- **Previous Compatibility IDs**: 10001-10080 (original 12 guns)

## Database Totals

| Category | Count | Notes |
|----------|-------|-------|
| **Guns** | 35 | All historical Mark variants |
| **Ammunition** | 80 | 30 historical + 50 fictional |
| **Turrets** | 96 | 31 historical + 65 fictional |
| **Compatibility** | {len(compatibility_records)} | New expanded linkages |
| **TOTAL** | {35 + 80 + 96 + len(compatibility_records)} | Complete British database |

## Files Generated

1. `insert_british_gun_variants.sql` - 35 gun INSERT statements
2. `insert_british_gun_ammo_compatibility.sql` - {len(compatibility_records)} compatibility records
3. This summary document

## Next Steps

1. Update naval_guns_database.md with new gun variants
2. Replace old compatibility records with expanded set
3. Verify all linkages in database
4. Test queries across full British dataset

Generated: October 2025
""")

print(f"Summary document generated: {md_output_file}")
print()
print("=" * 80)
print("COMPATIBILITY GENERATION COMPLETE")
print("=" * 80)
print()
print(f"Total new records: {len(compatibility_records)}")
print("Status: READY FOR DATABASE UPDATE")
print()
