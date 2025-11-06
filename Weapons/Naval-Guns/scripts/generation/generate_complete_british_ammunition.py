"""
Generate complete British ammunition table and compatibility records
Based on research completed for all 10 missing calibers
"""

# Comprehensive ammunition data researched from NavWeaps/Wikipedia
ammunition_data = [
    # ===== 18" AMMUNITION (Gun_ID 501) =====
    {
        'Ammunition_ID': 112,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 3320.0,
        'Muzzle_Velocity_FPS': 2270.0,
        'Max_Range_Yards': 28900.0,  # Standard charge
        'Notes': '18"/40 Mark I APC shell (HMS Furious), 4crh, standard charge',
        'Modded': 0
    },
    {
        'Ammunition_ID': 113,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 3320.0,
        'Muzzle_Velocity_FPS': 2420.0,  # Estimated supercharge
        'Max_Range_Yards': 36900.0,  # Supercharge at 45° elevation
        'Notes': '18"/40 Mark I APC shell, supercharge (690 lbs cordite total)',
        'Modded': 0
    },
    {
        'Ammunition_ID': 114,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'CPC',
        'Projectile_Weight_LBS': 3320.0,
        'Muzzle_Velocity_FPS': 2270.0,
        'Max_Range_Yards': 28900.0,
        'Notes': '18"/40 Mark I CPC (Common Pointed Capped - semi-AP), standard charge',
        'Modded': 0
    },

    # ===== 16" AMMUNITION (Gun_ID 503) =====
    {
        'Ammunition_ID': 115,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 2048.0,
        'Muzzle_Velocity_FPS': 2525.0,  # Operational velocity (reduced from 2700)
        'Max_Range_Yards': 35000.0,  # Estimated at 40° elevation
        'Notes': '16"/45 Mark I AP shell (Nelson/Rodney), reduced velocity due to barrel wear',
        'Modded': 0
    },
    {
        'Ammunition_ID': 116,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 2048.0,
        'Muzzle_Velocity_FPS': 2525.0,
        'Max_Range_Yards': 35000.0,
        'Notes': '16"/45 Mark I HE shell, operational velocity',
        'Modded': 0
    },

    # ===== 13.5" AMMUNITION (Gun_ID 505) =====
    {
        'Ammunition_ID': 117,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1250.0,
        'Muzzle_Velocity_FPS': 2582.0,
        'Max_Range_Yards': 23820.0,  # At 20° elevation
        'Notes': '13.5"/45 Mark V(L) "Light" APC shell (WWI superdreadnoughts, Jutland)',
        'Modded': 0
    },
    {
        'Ammunition_ID': 118,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1400.0,
        'Muzzle_Velocity_FPS': 2491.0,
        'Max_Range_Yards': 23740.0,  # At 20° elevation
        'Notes': '13.5"/45 Mark V(H) "Heavy" APC shell, increased weight variant',
        'Modded': 0
    },
    {
        'Ammunition_ID': 119,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 1250.0,
        'Muzzle_Velocity_FPS': 2582.0,
        'Max_Range_Yards': 23820.0,
        'Notes': '13.5"/45 Mark V(L) "Light" HE shell',
        'Modded': 0
    },

    # ===== 12" AMMUNITION (Gun_ID 506) =====
    {
        'Ammunition_ID': 120,
        'Gun_ID': 506,
        'Caliber': '12"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 850.0,
        'Muzzle_Velocity_FPS': 2725.0,
        'Max_Range_Yards': 20000.0,  # Estimated at 30° elevation
        'Notes': '12"/45 Mark X AP shell (HMS Dreadnought), revolutionary design',
        'Modded': 0
    },
    {
        'Ammunition_ID': 121,
        'Gun_ID': 506,
        'Caliber': '12"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 850.0,
        'Muzzle_Velocity_FPS': 2725.0,
        'Max_Range_Yards': 20000.0,
        'Notes': '12"/45 Mark X HE shell',
        'Modded': 0
    },

    # ===== 8" AMMUNITION (Gun_ID 520) =====
    {
        'Ammunition_ID': 122,
        'Gun_ID': 520,
        'Caliber': '8"',
        'Projectile_Type': 'SAPC',
        'Projectile_Weight_LBS': 256.0,
        'Muzzle_Velocity_FPS': 2725.0,
        'Max_Range_Yards': 30000.0,  # Estimated at 45° elevation
        'Notes': '8"/50 Mark VIII SAPC shell (County-class heavy cruisers), 2x15kg cordite bags',
        'Modded': 0
    },
    {
        'Ammunition_ID': 123,
        'Gun_ID': 520,
        'Caliber': '8"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 256.0,
        'Muzzle_Velocity_FPS': 2725.0,
        'Max_Range_Yards': 30000.0,
        'Notes': '8"/50 Mark VIII HE shell',
        'Modded': 0
    },

    # ===== 6" AMMUNITION (Gun_ID 530) =====
    {
        'Ammunition_ID': 124,
        'Gun_ID': 530,
        'Caliber': '6"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 112.0,
        'Muzzle_Velocity_FPS': 2760.0,
        'Max_Range_Yards': 25480.0,  # At 45° elevation
        'Notes': '6"/50 Mark XXIII AP shell (Crown Colony light cruisers), 14kg cordite charge',
        'Modded': 0
    },
    {
        'Ammunition_ID': 125,
        'Gun_ID': 530,
        'Caliber': '6"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 112.0,
        'Muzzle_Velocity_FPS': 2760.0,
        'Max_Range_Yards': 25480.0,
        'Notes': '6"/50 Mark XXIII HE shell',
        'Modded': 0
    },

    # ===== 5.25" AMMUNITION (Gun_ID 540) =====
    {
        'Ammunition_ID': 126,
        'Gun_ID': 540,
        'Caliber': '5.25"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 80.0,
        'Muzzle_Velocity_FPS': 2672.0,
        'Max_Range_Yards': 24070.0,  # At 45° elevation
        'Notes': '5.25"/50 Mark I HE shell (KGV secondary, Dido-class), dual-purpose',
        'Modded': 0
    },
    {
        'Ammunition_ID': 127,
        'Gun_ID': 540,
        'Caliber': '5.25"',
        'Projectile_Type': 'SAP',
        'Projectile_Weight_LBS': 80.0,
        'Muzzle_Velocity_FPS': 2672.0,
        'Max_Range_Yards': 24070.0,
        'Notes': '5.25"/50 Mark I SAP shell',
        'Modded': 0
    },

    # ===== 4.7" AMMUNITION (Gun_ID 545) =====
    {
        'Ammunition_ID': 128,
        'Gun_ID': 545,
        'Caliber': '4.7"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 50.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 16970.0,  # At 40° elevation
        'Notes': '4.7"/45 Mark IX/XII HE shell (standard WWI/WWII destroyers)',
        'Modded': 0
    },
    {
        'Ammunition_ID': 129,
        'Gun_ID': 545,
        'Caliber': '4.7"',
        'Projectile_Type': 'SAP',
        'Projectile_Weight_LBS': 50.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 16970.0,
        'Notes': '4.7"/45 Mark IX/XII SAP shell',
        'Modded': 0
    },

    # ===== 4.5" AMMUNITION (Gun_ID 550) =====
    {
        'Ammunition_ID': 130,
        'Gun_ID': 550,
        'Caliber': '4.5"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 55.0,
        'Muzzle_Velocity_FPS': 2449.0,
        'Max_Range_Yards': 20750.0,  # Surface target range
        'Notes': '4.5"/45 Mark V HE shell (Daring-class, post-war automated destroyers)',
        'Modded': 0
    },
    {
        'Ammunition_ID': 131,
        'Gun_ID': 550,
        'Caliber': '4.5"',
        'Projectile_Type': 'SAP',
        'Projectile_Weight_LBS': 55.0,
        'Muzzle_Velocity_FPS': 2449.0,
        'Max_Range_Yards': 20750.0,
        'Notes': '4.5"/45 Mark V SAP shell',
        'Modded': 0
    },

    # ===== 4" AMMUNITION (Gun_ID 555) =====
    {
        'Ammunition_ID': 132,
        'Gun_ID': 555,
        'Caliber': '4"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 35.0,
        'Muzzle_Velocity_FPS': 2660.0,
        'Max_Range_Yards': 19850.0,  # At 45° elevation
        'Notes': '4"/45 QF Mark XVI HE shell (primary AA gun), high-angle capable',
        'Modded': 0
    },
    {
        'Ammunition_ID': 133,
        'Gun_ID': 555,
        'Caliber': '4"',
        'Projectile_Type': 'SAP',
        'Projectile_Weight_LBS': 38.25,
        'Muzzle_Velocity_FPS': 2660.0,
        'Max_Range_Yards': 19850.0,
        'Notes': '4"/45 QF Mark XVI SAP shell, heavier projectile',
        'Modded': 0
    },
]

# Calculate Muzzle_Velocity_MPS from FPS (1 fps = 0.3048 m/s)
for record in ammunition_data:
    record['Muzzle_Velocity_MPS'] = round(record['Muzzle_Velocity_FPS'] * 0.3048, 1)

print("=" * 80)
print("BRITISH AMMUNITION RESEARCH - COMPLETE")
print("=" * 80)
print()
print(f"Total ammunition types researched: {len(ammunition_data)}")
print()

# Count by gun
gun_counts = {}
for ammo in ammunition_data:
    gun_id = ammo['Gun_ID']
    if gun_id not in gun_counts:
        gun_counts[gun_id] = 0
    gun_counts[gun_id] += 1

print("Ammunition by gun:")
gun_names = {
    501: '18"/40 Mark I',
    503: '16"/45 Mark I',
    505: '13.5"/45 Mark V',
    506: '12"/45 Mark X',
    520: '8"/50 Mark VIII',
    530: '6"/50 Mark XXIII',
    540: '5.25"/50 Mark I',
    545: '4.7"/45 Mark IX/XII',
    550: '4.5"/45 Mark V',
    555: '4"/45 QF Mark V/XVI'
}

for gun_id in sorted(gun_counts.keys()):
    print(f"  Gun {gun_id} ({gun_names[gun_id]:25s}): {gun_counts[gun_id]:2d} ammunition types")

print()
print("=" * 80)
print("AMMUNITION TABLE (SQL-READY)")
print("=" * 80)
print()

# Print ammunition table
print("| Ammunition_ID | Gun_ID | Caliber | Projectile_Type | Weight (lbs) | Muzzle_Velocity_FPS | Muzzle_Velocity_MPS | Max_Range_Yards | Modded | Notes |")
print("|---------------|--------|---------|-----------------|--------------|---------------------|---------------------|-----------------|--------|-------|")

for ammo in ammunition_data:
    print(f"| {ammo['Ammunition_ID']:3d} | {ammo['Gun_ID']:3d} | {ammo['Caliber']:6s} | {ammo['Projectile_Type']:6s} | {ammo['Projectile_Weight_LBS']:8.1f} | {ammo['Muzzle_Velocity_FPS']:8.1f} | {ammo['Muzzle_Velocity_MPS']:8.1f} | {ammo['Max_Range_Yards']:8.0f} | {ammo['Modded']:1d} | {ammo['Notes']} |")

print()
print("=" * 80)
print("COMPATIBILITY RECORDS GENERATION")
print("=" * 80)
print()

# Generate compatibility records (one per ammunition)
compat_id_start = 10009  # Continue from existing 8 records (10001-10008)

print("| Compatibility_ID | Gun_ID | Ammunition_ID | Caliber | Muzzle_Velocity_FPS | Muzzle_Velocity_MPS | Max_Range_Yards | Notes |")
print("|------------------|--------|---------------|---------|---------------------|---------------------|-----------------|-------|")

compatibility_records = []
for i, ammo in enumerate(ammunition_data):
    compat_id = compat_id_start + i
    compatibility_records.append({
        'Compatibility_ID': compat_id,
        'Gun_ID': ammo['Gun_ID'],
        'Ammunition_ID': ammo['Ammunition_ID'],
        'Caliber': ammo['Caliber'],
        'Muzzle_Velocity_FPS': ammo['Muzzle_Velocity_FPS'],
        'Muzzle_Velocity_MPS': ammo['Muzzle_Velocity_MPS'],
        'Max_Range_Yards': ammo['Max_Range_Yards'],
        'Notes': ammo['Notes']
    })

    print(f"| {compat_id:5d} | {ammo['Gun_ID']:3d} | {ammo['Ammunition_ID']:3d} | {ammo['Caliber']:6s} | {ammo['Muzzle_Velocity_FPS']:8.1f} | {ammo['Muzzle_Velocity_MPS']:8.1f} | {ammo['Max_Range_Yards']:8.0f} | {ammo['Notes']} |")

print()
print(f"Total compatibility records: {len(compatibility_records)}")
print(f"Compatibility ID range: {compat_id_start}-{compat_id_start + len(compatibility_records) - 1}")
print()

print("=" * 80)
print("SQL INSERT STATEMENTS")
print("=" * 80)
print()

print("-- AMMUNITION INSERTS")
print()
for ammo in ammunition_data:
    notes_escaped = ammo['Notes'].replace("'", "''")
    print(f"INSERT INTO Ammunition (Ammunition_ID, Caliber, Projectile_Type, Projectile_Weight_LBS, Notes, Modded)")
    print(f"  VALUES ({ammo['Ammunition_ID']}, '{ammo['Caliber']}', '{ammo['Projectile_Type']}', {ammo['Projectile_Weight_LBS']}, '{notes_escaped}', {ammo['Modded']});")

print()
print("-- COMPATIBILITY INSERTS")
print()
for compat in compatibility_records:
    notes_escaped = compat['Notes'].replace("'", "''")
    print(f"INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Notes)")
    print(f"  VALUES ({compat['Compatibility_ID']}, {compat['Gun_ID']}, {compat['Ammunition_ID']}, '{compat['Caliber']}', {compat['Muzzle_Velocity_FPS']}, {compat['Muzzle_Velocity_MPS']}, {compat['Max_Range_Yards']}, '{notes_escaped}');")

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print(f"[OK] Ammunition researched:          {len(ammunition_data)} types")
print(f"[OK] Compatibility records generated: {len(compatibility_records)} records")
print(f"[OK] Gun coverage:                    {len(gun_counts)}/10 guns (100%)")
print()
print("Status: COMPLETE - Ready for database import")
print()
