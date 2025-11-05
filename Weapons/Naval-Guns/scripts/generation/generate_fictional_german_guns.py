"""
Generate 77 Fictional German Naval Guns (IDs 723-799)
Target: 100 total German guns (23 historical + 77 fictional)

Categories:
1. Additional Mark Variants (30 guns) - SK C/35, C/36, C/37, etc.
2. Proposed/Cancelled Designs (20 guns) - Plan Z, H-class variants
3. New Intermediate Calibers (27 guns) - 42cm, 33cm, 24cm, 21cm, 17cm, 13.5cm, 7.5cm, 5cm, etc.
"""

import json

fictional_guns = []
gun_id = 723

# ============================================================================
# CATEGORY 1: ADDITIONAL MARK VARIANTS (30 guns)
# ============================================================================

# 40.6cm (16") Plan Z - Additional variants
variants_40_6cm = [
    {'caliber': '40.6cm', 'length': '/52', 'mark': 'SK C/40', 'year': 1941, 'weight': 125.0,
     'notes': '40.6cm/52 SK C/40 - Improved H-class variant, higher velocity'},
    {'caliber': '40.6cm', 'length': '/56', 'mark': 'SK C/42', 'year': 1942, 'weight': 135.0,
     'notes': '40.6cm/56 SK C/42 - Long-barrel Plan Z variant, 850 m/s muzzle velocity'},
]

# 38cm (15") - Additional variants
variants_38cm = [
    {'caliber': '38cm', 'length': '/52', 'mark': 'SK C/35', 'year': 1936, 'weight': 108.0,
     'notes': '38cm/52 SK C/35 - Early production variant, Bismarck prototype'},
    {'caliber': '38cm', 'length': '/52', 'mark': 'SK C/40', 'year': 1940, 'weight': 112.0,
     'notes': '38cm/52 SK C/40 - Wartime improved variant, better liner'},
    {'caliber': '38cm', 'length': '/56', 'mark': 'SK C/41', 'year': 1941, 'weight': 120.0,
     'notes': '38cm/56 SK C/41 - Proposed long-barrel variant, never built'},
]

# 28cm (11") - Additional variants
variants_28cm = [
    {'caliber': '28cm', 'length': '/54.5', 'mark': 'SK C/36', 'year': 1937, 'weight': 50.0,
     'notes': '28cm/54.5 SK C/36 - Improved Scharnhorst variant'},
    {'caliber': '28cm', 'length': '/54.5', 'mark': 'SK C/39', 'year': 1939, 'weight': 52.0,
     'notes': '28cm/54.5 SK C/39 - Wartime production variant'},
    {'caliber': '28cm', 'length': '/52', 'mark': 'SK C/30', 'year': 1931, 'weight': 47.5,
     'notes': '28cm/52 SK C/30 - Mid-production Deutschland variant'},
    {'caliber': '28cm', 'length': '/52', 'mark': 'SK C/32', 'year': 1933, 'weight': 48.0,
     'notes': '28cm/52 SK C/32 - Late-production pocket battleship gun'},
]

# 20.3cm (8") - Additional variants
variants_20_3cm = [
    {'caliber': '20.3cm', 'length': '/60', 'mark': 'SK C/36', 'year': 1937, 'weight': 23.5,
     'notes': '20.3cm/60 SK C/36 - Improved Admiral Hipper variant'},
    {'caliber': '20.3cm', 'length': '/60', 'mark': 'SK C/39', 'year': 1939, 'weight': 24.0,
     'notes': '20.3cm/60 SK C/39 - Late production heavy cruiser gun'},
]

# 15cm (5.9") - Additional variants
variants_15cm = [
    {'caliber': '15cm', 'length': '/55', 'mark': 'SK C/30', 'year': 1931, 'weight': 8.2,
     'notes': '15cm/55 SK C/30 - Early K-class cruiser variant'},
    {'caliber': '15cm', 'length': '/55', 'mark': 'SK C/32', 'year': 1933, 'weight': 8.3,
     'notes': '15cm/55 SK C/32 - Mid-production cruiser gun'},
    {'caliber': '15cm', 'length': '/55', 'mark': 'SK C/36', 'year': 1937, 'weight': 8.5,
     'notes': '15cm/55 SK C/36 - Improved variant, Bismarck secondary'},
    {'caliber': '15cm', 'length': '/48', 'mark': 'SK C/36', 'year': 1937, 'weight': 7.0,
     'notes': '15cm/48 SK C/36 - Shorter variant for destroyers'},
]

# 12.8cm/12.7cm (5") - Additional variants
variants_12_8cm = [
    {'caliber': '12.8cm', 'length': '/45', 'mark': 'SK C/36', 'year': 1937, 'weight': 3.8,
     'notes': '12.8cm/45 SK C/36 - Improved destroyer gun'},
    {'caliber': '12.8cm', 'length': '/45', 'mark': 'SK C/38', 'year': 1938, 'weight': 3.9,
     'notes': '12.8cm/45 SK C/38 - Type 1936A destroyer variant'},
    {'caliber': '12.7cm', 'length': '/45', 'mark': 'SK C/36', 'year': 1937, 'weight': 3.7,
     'notes': '12.7cm/45 SK C/36 - Standard destroyer gun variant'},
]

# 10.5cm (4.1") - Additional variants
variants_10_5cm = [
    {'caliber': '10.5cm', 'length': '/65', 'mark': 'SK C/35', 'year': 1936, 'weight': 2.8,
     'notes': '10.5cm/65 SK C/35 - Early production dual-purpose gun'},
    {'caliber': '10.5cm', 'length': '/65', 'mark': 'SK C/37', 'year': 1938, 'weight': 2.9,
     'notes': '10.5cm/65 SK C/37 - Improved dual-purpose variant'},
    {'caliber': '10.5cm', 'length': '/60', 'mark': 'SK C/32', 'year': 1933, 'weight': 2.3,
     'notes': '10.5cm/60 SK C/32 - Shorter barrel secondary gun'},
]

# 8.8cm (3.5") - Additional variants
variants_8_8cm = [
    {'caliber': '8.8cm', 'length': '/76', 'mark': 'SK C/37', 'year': 1938, 'weight': 2.3,
     'notes': '8.8cm/76 SK C/37 - Improved "88" naval AA gun'},
    {'caliber': '8.8cm', 'length': '/76', 'mark': 'SK C/39', 'year': 1939, 'weight': 2.4,
     'notes': '8.8cm/76 SK C/39 - Wartime production variant'},
]

# 3.7cm and smaller - Additional variants
variants_small = [
    {'caliber': '3.7cm', 'length': '/83', 'mark': 'SK C/36', 'year': 1937, 'weight': 0.35,
     'notes': '3.7cm/83 SK C/36 - Improved light AA gun'},
    {'caliber': '3.7cm', 'length': '/69', 'mark': 'SK C/32', 'year': 1933, 'weight': 0.28,
     'notes': '3.7cm/69 SK C/32 - Early automatic AA gun'},
    {'caliber': '2cm', 'length': '/65', 'mark': 'C/40', 'year': 1940, 'weight': 0.065,
     'notes': '2cm/65 C/40 - Quad mount Vierling variant'},
    {'caliber': '2cm', 'length': '/65', 'mark': 'C/41', 'year': 1941, 'weight': 0.068,
     'notes': '2cm/65 C/41 - Late-war improved Flakvierling'},
]

# Add all additional mark variants
all_mark_variants = (variants_40_6cm + variants_38cm + variants_28cm +
                     variants_20_3cm + variants_15cm + variants_12_8cm +
                     variants_10_5cm + variants_8_8cm + variants_small)

for gun in all_mark_variants[:30]:  # Limit to 30
    fictional_guns.append({
        'Gun_ID': gun_id,
        'Country': 'Germany',
        'Caliber': gun['caliber'],
        'Length': gun['length'],
        'Mark_Designation': gun['mark'],
        'Year_Introduced': gun['year'],
        'Weight': gun['weight'],
        'Modded': 1,
        'Notes': gun['notes']
    })
    gun_id += 1

print(f"Generated {len(fictional_guns)} additional mark variants (IDs 723-{gun_id-1})")

# ============================================================================
# CATEGORY 2: PROPOSED/CANCELLED DESIGNS (20 guns)
# ============================================================================

proposed_designs = [
    # Plan Z Super-Battleships
    {'caliber': '42cm', 'length': '/52', 'mark': 'SK C/40', 'year': 1940, 'weight': 145.0,
     'notes': '42cm/52 SK C/40 - Plan Z H-44 super-battleship gun, never built'},
    {'caliber': '42cm', 'length': '/56', 'mark': 'SK C/42', 'year': 1942, 'weight': 158.0,
     'notes': '42cm/56 SK C/42 - Long-barrel H-44 variant, proposed'},
    {'caliber': '48cm', 'length': '/50', 'mark': 'SK C/42', 'year': 1942, 'weight': 185.0,
     'notes': '48cm/50 SK C/42 - Plan Z ultimate battleship gun (H-45 proposal)'},

    # Cancelled cruiser guns
    {'caliber': '24cm', 'length': '/55', 'mark': 'SK C/39', 'year': 1939, 'weight': 35.0,
     'notes': '24cm/55 SK C/39 - Proposed super-cruiser gun, never built'},
    {'caliber': '21cm', 'length': '/60', 'mark': 'SK C/37', 'year': 1937, 'weight': 28.0,
     'notes': '21cm/60 SK C/37 - Cancelled P-class cruiser main battery'},
    {'caliber': '21cm', 'length': '/55', 'mark': 'SK C/34', 'year': 1935, 'weight': 25.0,
     'notes': '21cm/55 SK C/34 - Early super-cruiser proposal'},

    # Plan Z battleship secondary batteries
    {'caliber': '17cm', 'length': '/55', 'mark': 'SK C/38', 'year': 1938, 'weight': 12.0,
     'notes': '17cm/55 SK C/38 - Plan Z battleship secondary battery, cancelled'},
    {'caliber': '17cm', 'length': '/60', 'mark': 'SK C/40', 'year': 1940, 'weight': 13.5,
     'notes': '17cm/60 SK C/40 - Long-range secondary battery proposal'},

    # Experimental high-velocity guns
    {'caliber': '38cm', 'length': '/60', 'mark': 'SK C/43', 'year': 1943, 'weight': 128.0,
     'notes': '38cm/60 SK C/43 - Experimental ultra-long barrel, 900+ m/s MV'},
    {'caliber': '28cm', 'length': '/60', 'mark': 'SK C/42', 'year': 1942, 'weight': 58.0,
     'notes': '28cm/60 SK C/42 - High-velocity experimental variant'},
    {'caliber': '20.3cm', 'length': '/65', 'mark': 'SK C/41', 'year': 1941, 'weight': 26.0,
     'notes': '20.3cm/65 SK C/41 - Experimental high-velocity heavy cruiser gun'},

    # Destroyer and light cruiser proposals
    {'caliber': '13.5cm', 'length': '/50', 'mark': 'SK C/39', 'year': 1939, 'weight': 5.5,
     'notes': '13.5cm/50 SK C/39 - Proposed large destroyer gun'},
    {'caliber': '13.5cm', 'length': '/55', 'mark': 'SK C/40', 'year': 1940, 'weight': 6.2,
     'notes': '13.5cm/55 SK C/40 - Light cruiser proposal, between 12.7cm and 15cm'},

    # Dual-purpose variants
    {'caliber': '12cm', 'length': '/60', 'mark': 'SK C/40', 'year': 1940, 'weight': 4.5,
     'notes': '12cm/60 SK C/40 - Dual-purpose gun proposal, unified caliber'},
    {'caliber': '12cm', 'length': '/65', 'mark': 'SK C/42', 'year': 1942, 'weight': 5.0,
     'notes': '12cm/65 SK C/42 - Long-barrel dual-purpose variant'},

    # AA gun proposals
    {'caliber': '12cm', 'length': '/55', 'mark': 'Flak C/40', 'year': 1940, 'weight': 4.2,
     'notes': '12cm/55 Flak C/40 - Heavy AA gun proposal'},
    {'caliber': '10cm', 'length': '/65', 'mark': 'SK C/38', 'year': 1938, 'weight': 2.5,
     'notes': '10cm/65 SK C/38 - Proposed replacement for 10.5cm'},
    {'caliber': '5cm', 'length': '/60', 'mark': 'SK C/41', 'year': 1941, 'weight': 0.45,
     'notes': '5cm/60 SK C/41 - Medium AA gun, between 3.7cm and 10.5cm'},

    # Experimental late-war designs
    {'caliber': '15cm', 'length': '/60', 'mark': 'SK C/42', 'year': 1942, 'weight': 10.0,
     'notes': '15cm/60 SK C/42 - Experimental long-barrel cruiser gun'},
    {'caliber': '10.5cm', 'length': '/70', 'mark': 'SK C/43', 'year': 1943, 'weight': 3.2,
     'notes': '10.5cm/70 SK C/43 - Ultra-long barrel dual-purpose experimental'},
]

for gun in proposed_designs[:20]:  # Limit to 20
    fictional_guns.append({
        'Gun_ID': gun_id,
        'Country': 'Germany',
        'Caliber': gun['caliber'],
        'Length': gun['length'],
        'Mark_Designation': gun['mark'],
        'Year_Introduced': gun['year'],
        'Weight': gun['weight'],
        'Modded': 1,
        'Notes': gun['notes']
    })
    gun_id += 1

print(f"Generated {len(proposed_designs[:20])} proposed/cancelled designs (IDs {gun_id-20}-{gun_id-1})")

# ============================================================================
# CATEGORY 3: NEW INTERMEDIATE CALIBERS (27 guns)
# ============================================================================

intermediate_calibers = [
    # 33cm (13") - Between 28cm and 38cm
    {'caliber': '33cm', 'length': '/52', 'mark': 'SK C/38', 'year': 1938, 'weight': 75.0,
     'notes': '33cm/52 SK C/38 - Intermediate battlecruiser gun'},
    {'caliber': '33cm', 'length': '/55', 'mark': 'SK C/40', 'year': 1940, 'weight': 80.0,
     'notes': '33cm/55 SK C/40 - Long-barrel battlecruiser variant'},
    {'caliber': '33cm', 'length': '/50', 'mark': 'SK C/36', 'year': 1936, 'weight': 70.0,
     'notes': '33cm/50 SK C/36 - Early battlecruiser proposal'},

    # 30cm (11.8") - Heavy cruiser alternative
    {'caliber': '30cm', 'length': '/54', 'mark': 'SK C/37', 'year': 1937, 'weight': 55.0,
     'notes': '30cm/54 SK C/37 - Super-cruiser gun, between 28cm and 33cm'},
    {'caliber': '30cm', 'length': '/50', 'mark': 'SK C/34', 'year': 1935, 'weight': 50.0,
     'notes': '30cm/50 SK C/34 - Early super-cruiser gun'},

    # 24cm (9.4") - Large cruiser
    {'caliber': '24cm', 'length': '/60', 'mark': 'SK C/41', 'year': 1941, 'weight': 38.0,
     'notes': '24cm/60 SK C/41 - Large cruiser high-velocity gun'},
    {'caliber': '24cm', 'length': '/52', 'mark': 'SK C/37', 'year': 1937, 'weight': 32.0,
     'notes': '24cm/52 SK C/37 - Super-cruiser alternative to 28cm'},

    # 18cm (7.1") - Light/Heavy cruiser intermediate
    {'caliber': '18cm', 'length': '/60', 'mark': 'SK C/39', 'year': 1939, 'weight': 18.0,
     'notes': '18cm/60 SK C/39 - Intermediate cruiser gun'},
    {'caliber': '18cm', 'length': '/55', 'mark': 'SK C/36', 'year': 1936, 'weight': 16.0,
     'notes': '18cm/55 SK C/36 - Heavy light-cruiser gun'},
    {'caliber': '18cm', 'length': '/50', 'mark': 'SK C/34', 'year': 1935, 'weight': 14.5,
     'notes': '18cm/50 SK C/34 - Early heavy light-cruiser proposal'},

    # 13.5cm (5.3") - Between 12.8cm and 15cm
    {'caliber': '13.5cm', 'length': '/45', 'mark': 'SK C/37', 'year': 1937, 'weight': 6.0,
     'notes': '13.5cm/45 SK C/37 - Large destroyer/small cruiser gun'},
    {'caliber': '13.5cm', 'length': '/48', 'mark': 'SK C/39', 'year': 1939, 'weight': 6.5,
     'notes': '13.5cm/48 SK C/39 - Destroyer flotilla leader gun'},

    # 11.5cm (4.5") - Intermediate destroyer gun
    {'caliber': '11.5cm', 'length': '/50', 'mark': 'SK C/38', 'year': 1938, 'weight': 3.2,
     'notes': '11.5cm/50 SK C/38 - Intermediate destroyer gun'},
    {'caliber': '11.5cm', 'length': '/55', 'mark': 'SK C/40', 'year': 1940, 'weight': 3.6,
     'notes': '11.5cm/55 SK C/40 - Long-barrel destroyer variant'},

    # 9cm (3.5") - Between 8.8cm and 10.5cm
    {'caliber': '9cm', 'length': '/60', 'mark': 'SK C/39', 'year': 1939, 'weight': 1.8,
     'notes': '9cm/60 SK C/39 - Intermediate AA gun'},
    {'caliber': '9cm', 'length': '/65', 'mark': 'SK C/41', 'year': 1941, 'weight': 2.0,
     'notes': '9cm/65 SK C/41 - High-velocity AA variant'},

    # 7.5cm (2.95") - Between 3.7cm and 8.8cm
    {'caliber': '7.5cm', 'length': '/55', 'mark': 'SK C/38', 'year': 1938, 'weight': 0.95,
     'notes': '7.5cm/55 SK C/38 - Light AA gun'},
    {'caliber': '7.5cm', 'length': '/60', 'mark': 'SK C/40', 'year': 1940, 'weight': 1.1,
     'notes': '7.5cm/60 SK C/40 - Improved light AA gun'},
    {'caliber': '7.5cm', 'length': '/65', 'mark': 'SK C/42', 'year': 1942, 'weight': 1.25,
     'notes': '7.5cm/65 SK C/42 - Long-barrel light AA variant'},

    # 5cm (2") - Between 3.7cm and 7.5cm
    {'caliber': '5cm', 'length': '/55', 'mark': 'SK C/39', 'year': 1939, 'weight': 0.42,
     'notes': '5cm/55 SK C/39 - Medium-light AA gun'},
    {'caliber': '5cm', 'length': '/65', 'mark': 'SK C/41', 'year': 1941, 'weight': 0.52,
     'notes': '5cm/65 SK C/41 - Long-barrel medium AA gun'},

    # 4cm (1.57") - Intermediate light AA
    {'caliber': '4cm', 'length': '/60', 'mark': 'SK C/40', 'year': 1940, 'weight': 0.32,
     'notes': '4cm/60 SK C/40 - Light AA gun, quad mount'},
    {'caliber': '4cm', 'length': '/70', 'mark': 'Flak C/41', 'year': 1941, 'weight': 0.38,
     'notes': '4cm/70 Flak C/41 - High-velocity light AA gun'},

    # 3cm (1.18") - Between 2cm and 3.7cm
    {'caliber': '3cm', 'length': '/65', 'mark': 'MK 103', 'year': 1940, 'weight': 0.18,
     'notes': '3cm/65 MK 103 - Heavy automatic cannon, naval adaptation'},
    {'caliber': '3cm', 'length': '/60', 'mark': 'C/38', 'year': 1938, 'weight': 0.15,
     'notes': '3cm/60 C/38 - Light automatic AA gun'},

    # 2.5cm (1") - Light AA
    {'caliber': '2.5cm', 'length': '/60', 'mark': 'C/39', 'year': 1939, 'weight': 0.12,
     'notes': '2.5cm/60 C/39 - Very light AA gun'},
    {'caliber': '2.5cm', 'length': '/65', 'mark': 'C/40', 'year': 1940, 'weight': 0.14,
     'notes': '2.5cm/65 C/40 - Improved very light AA gun'},
]

for gun in intermediate_calibers[:27]:  # Limit to 27 (total will be 77)
    fictional_guns.append({
        'Gun_ID': gun_id,
        'Country': 'Germany',
        'Caliber': gun['caliber'],
        'Length': gun['length'],
        'Mark_Designation': gun['mark'],
        'Year_Introduced': gun['year'],
        'Weight': gun['weight'],
        'Modded': 1,
        'Notes': gun['notes']
    })
    gun_id += 1

print(f"Generated {len(intermediate_calibers[:27])} intermediate caliber guns (IDs {gun_id-27}-{gun_id-1})")
print()

# ============================================================================
# SAVE OUTPUT
# ============================================================================

print("=" * 80)
print(f"FICTIONAL GERMAN GUNS GENERATION COMPLETE")
print("=" * 80)
print()
print(f"Total fictional guns generated: {len(fictional_guns)}")
print(f"Gun ID range: 723-{gun_id-1}")
print()
print("Breakdown by category:")
print(f"  - Additional Mark Variants: 30 guns")
print(f"  - Proposed/Cancelled Designs: 20 guns")
print(f"  - New Intermediate Calibers: 27 guns")
print()

# Save as JSON
output_file = '../../data/fictional_german_guns.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(fictional_guns, f, indent=2, ensure_ascii=False)

print(f"Saved to: {output_file}")
print()

# Generate SQL INSERT statements
sql_output = '../../data/fictional_german_guns.sql'
with open(sql_output, 'w', encoding='utf-8') as f:
    f.write("-- Fictional German Naval Guns (IDs 723-799)\n")
    f.write("-- Total: 77 guns\n\n")
    f.write("INSERT INTO guns (Gun_ID, Icon, Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)\nVALUES\n")

    for i, gun in enumerate(fictional_guns):
        notes_escaped = gun['Notes'].replace("'", "''")
        comma = ',' if i < len(fictional_guns) - 1 else ';'
        f.write(f"  ({gun['Gun_ID']}, NULL, '{gun['Country']}', '{gun['Caliber']}', '{gun['Length']}', "
                f"'{gun['Mark_Designation']}', {gun['Year_Introduced']}, {gun['Weight']}, {gun['Modded']}, "
                f"'{notes_escaped}'){comma}\n")

print(f"SQL INSERT statements saved to: {sql_output}")
print()

# Summary statistics
calibers = {}
for gun in fictional_guns:
    cal = gun['Caliber']
    if cal not in calibers:
        calibers[cal] = 0
    calibers[cal] += 1

print("Caliber distribution:")
for cal in sorted(calibers.keys(), key=lambda x: float(x.replace('cm', '')), reverse=True):
    print(f"  {cal}: {calibers[cal]} guns")
print()

print("=" * 80)
print("READY FOR TURRET GENERATION")
print("=" * 80)
