"""
Generate Ammunition for Fictional British Guns
Creates ammunition types for new calibers and additional Mark variants
Ammunition IDs: 184-230 (47 new types)
"""

import json

print("=" * 80)
print("GENERATING AMMUNITION FOR FICTIONAL BRITISH GUNS")
print("=" * 80)
print()

fictional_ammunition = []
ammo_id = 184  # Starting after existing ammunition

# ===== NEW CALIBERS =====

# 10" Ammunition (6 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '10"', 'Mark_Designation': 'Mark I', 'Projectile_Type': 'AP', 'Weight_LBS': 500.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '10" Mark I AP shell. Pre-dreadnought era. MV: 2,500 fps. Bursting charge: 8 lbs. Fictional armored cruiser ammunition.'},
    {'ID': ammo_id+1, 'Caliber': '10"', 'Mark_Designation': 'Mark II', 'Projectile_Type': 'APC', 'Weight_LBS': 500.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '10" Mark II APC shell. Improved cap design. MV: 2,650 fps. Bursting charge: 8 lbs. Dreadnought-era heavy cruiser.'},
    {'ID': ammo_id+2, 'Caliber': '10"', 'Mark_Designation': '', 'Projectile_Type': 'HE', 'Weight_LBS': 485.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '10" HE shell. Explosive content: 48 lbs. MV: 2,500 fps. Shore bombardment and anti-surface. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '10"', 'Mark_Designation': 'Mark III', 'Projectile_Type': 'CPC', 'Weight_LBS': 500.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '10" Mark III CPC (Common Pointed Capped) semi-AP. General-purpose shell. MV: 2,500 fps. Bursting charge: 15 lbs. Fictional.'},
    {'ID': ammo_id+4, 'Caliber': '10"', 'Mark_Designation': 'Mark IV', 'Projectile_Type': 'AP', 'Weight_LBS': 500.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '10" Mark IV AP shell. High-velocity variant. MV: 2,800 fps. Improved penetration. Interwar design. Fictional.'},
    {'ID': ammo_id+5, 'Caliber': '10"', 'Mark_Designation': '', 'Projectile_Type': 'SAP', 'Weight_LBS': 490.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '10" SAP (Semi-Armor Piercing). Light armor targets. MV: 2,650 fps. Bursting charge: 18 lbs. Fictional.'}
])
ammo_id += 6

# 9.2" Ammunition (6 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '9.2"', 'Mark_Designation': 'Mark I', 'Projectile_Type': 'AP', 'Weight_LBS': 380.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '9.2" Mark I AP shell. Armored cruiser era. MV: 2,300 fps. Bursting charge: 6 lbs. Wire-wound gun era. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '9.2"', 'Mark_Designation': 'Mark II', 'Projectile_Type': 'APC', 'Weight_LBS': 380.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '9.2" Mark II APC shell. Improved cap. MV: 2,450 fps. Bursting charge: 6 lbs. Pre-dreadnought/dreadnought era. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '9.2"', 'Mark_Designation': '', 'Projectile_Type': 'HE', 'Weight_LBS': 370.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '9.2" HE shell. Explosive content: 35 lbs. MV: 2,300 fps. Anti-surface targets. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '9.2"', 'Mark_Designation': 'Mark III', 'Projectile_Type': 'CPC', 'Weight_LBS': 380.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '9.2" Mark III CPC semi-AP. General-purpose. MV: 2,450 fps. Bursting charge: 12 lbs. Fictional.'},
    {'ID': ammo_id+4, 'Caliber': '9.2"', 'Mark_Designation': 'Mark IV', 'Projectile_Type': 'AP', 'Weight_LBS': 380.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '9.2" Mark IV AP shell. High-velocity WWI variant. MV: 2,600 fps. Improved penetration. Fictional.'},
    {'ID': ammo_id+5, 'Caliber': '9.2"', 'Mark_Designation': '', 'Projectile_Type': 'SAP', 'Weight_LBS': 375.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '9.2" SAP shell. Light cruiser targets. MV: 2,450 fps. Bursting charge: 15 lbs. Fictional.'}
])
ammo_id += 6

# 7.5" Ammunition (6 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '7.5"', 'Mark_Designation': 'Mark I', 'Projectile_Type': 'AP', 'Weight_LBS': 200.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '7.5" Mark I AP shell. Heavy destroyer/light cruiser. MV: 2,800 fps. Bursting charge: 3 lbs. 1920s "super destroyer" concept. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '7.5"', 'Mark_Designation': 'Mark II', 'Projectile_Type': 'APC', 'Weight_LBS': 200.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '7.5" Mark II APC shell. Dual-purpose capable. MV: 2,900 fps. Bursting charge: 3 lbs. 1930s design. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '7.5"', 'Mark_Designation': '', 'Projectile_Type': 'HE', 'Weight_LBS': 195.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '7.5" HE shell. Explosive content: 18 lbs. MV: 2,800 fps. Anti-destroyer and shore bombardment. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '7.5"', 'Mark_Designation': 'Mark III', 'Projectile_Type': 'SAP', 'Weight_LBS': 200.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '7.5" Mark III SAP shell. Light cruiser targets. MV: 2,900 fps. Bursting charge: 8 lbs. Wartime design. Fictional.'},
    {'ID': ammo_id+4, 'Caliber': '7.5"', 'Mark_Designation': '', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 195.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '7.5" HE-VT (proximity fused). Anti-aircraft. MV: 2,800 fps. Post-war development. Fictional.'},
    {'ID': ammo_id+5, 'Caliber': '7.5"', 'Mark_Designation': 'Mark IV', 'Projectile_Type': 'Illum', 'Weight_LBS': 190.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '7.5" Mark IV Illumination shell. Night combat. MV: 2,750 fps. Star shell. Fictional.'}
])
ammo_id += 6

# 5" Ammunition (6 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '5"', 'Mark_Designation': 'Mark I', 'Projectile_Type': 'AP', 'Weight_LBS': 62.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '5" Mark I AP shell. Destroyer/frigate main gun. MV: 2,700 fps. Bursting charge: 1.2 lbs. WWII emergency destroyers. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '5"', 'Mark_Designation': 'Mark II', 'Projectile_Type': 'HE', 'Weight_LBS': 60.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '5" Mark II HE shell. Explosive content: 5.5 lbs. MV: 2,700 fps. Anti-surface and AA. Dual-purpose. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '5"', 'Mark_Designation': 'Mark III', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 60.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '5" Mark III HE-VT (proximity fused). Anti-aircraft. MV: 2,850 fps. Post-war automated loading. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '5"', 'Mark_Designation': 'Mark IV', 'Projectile_Type': 'SAP', 'Weight_LBS': 62.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '5" Mark IV SAP shell. Light targets. MV: 2,850 fps. Bursting charge: 2 lbs. 1950s frigates. Fictional.'},
    {'ID': ammo_id+4, 'Caliber': '5"', 'Mark_Designation': 'Mark V', 'Projectile_Type': 'Illum', 'Weight_LBS': 58.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '5" Mark V Illumination shell. Night operations. MV: 2,650 fps. Star shell. Fictional.'},
    {'ID': ammo_id+5, 'Caliber': '5"', 'Mark_Designation': 'Mark VI', 'Projectile_Type': 'AAC', 'Weight_LBS': 60.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '5" Mark VI AAC (Anti-Aircraft Common). Contact/proximity fused. MV: 2,850 fps. Cold War era. Fictional.'}
])
ammo_id += 6

# 3" Ammunition (4 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '3"', 'Mark_Designation': 'Mark I', 'Projectile_Type': 'HE', 'Weight_LBS': 12.5, 'Country': 'Britain', 'Modded': 1, 'Notes': '3" Mark I HE shell. Light AA/secondary. MV: 2,800 fps. Explosive content: 1.2 lbs. Corvette/sloop weapon. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '3"', 'Mark_Designation': 'Mark II', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 12.5, 'Country': 'Britain', 'Modded': 1, 'Notes': '3" Mark II HE-VT (proximity fused). Anti-aircraft. MV: 2,800 fps. Post-war escorts. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '3"', 'Mark_Designation': 'Mark III', 'Projectile_Type': 'Illum', 'Weight_LBS': 11.5, 'Country': 'Britain', 'Modded': 1, 'Notes': '3" Mark III Illumination shell. Night operations. MV: 2,750 fps. Small star shell. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '3"', 'Mark_Designation': 'Mark IV', 'Projectile_Type': 'AAC', 'Weight_LBS': 12.5, 'Country': 'Britain', 'Modded': 1, 'Notes': '3" Mark IV AAC shell. Anti-aircraft common. MV: 2,800 fps. Cold War frigate weapon. Fictional.'}
])
ammo_id += 4

# ===== ADDITIONAL MARK VARIANTS FOR EXISTING CALIBERS =====

# 16" Additional Variants (2 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '16"', 'Mark_Designation': 'Mark II', 'Projectile_Type': 'APC', 'Weight_LBS': 2120.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '16" Mark II APC shell. Heavier variant for Mark III gun. MV: 2,525 fps. Bursting charge: 45 lbs. Improved penetration. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '16"', 'Mark_Designation': 'Mark III', 'Projectile_Type': 'HE', 'Weight_LBS': 2000.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '16" Mark III HE shell. Explosive content: 150 lbs. MV: 2,500 fps. Shore bombardment. Fictional.'}
])
ammo_id += 2

# 15" Additional Variants (3 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '15"', 'Mark_Designation': 'Mark XIX', 'Projectile_Type': 'APC', 'Weight_LBS': 1938.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '15" Mark XIX APC shell. Post-war improved. Supercharge 490 lbs. MV: 2,670 fps. Superior penetration. Vanguard late-service. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '15"', 'Mark_Designation': 'Mark XX', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 1900.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '15" Mark XX HE-VT shell. Proximity fused. MV: 2,450 fps. Anti-aircraft barrage. Cold War development. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '15"', 'Mark_Designation': 'Mark XXI', 'Projectile_Type': 'Illum', 'Weight_LBS': 1850.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '15" Mark XXI Illumination shell. Night operations. MV: 2,400 fps. Large star shell. Post-war. Fictional.'}
])
ammo_id += 3

# 14" Additional Variants (2 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '14"', 'Mark_Designation': 'Mark VIII', 'Projectile_Type': 'APC', 'Weight_LBS': 1590.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '14" Mark VIII APC shell. Improved Mark VIIB. Bursting charge: 42 lbs. MV: 2,483 fps. Post-war improved penetrator. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '14"', 'Mark_Designation': 'Mark IX', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 1550.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '14" Mark IX HE-VT shell. Proximity fused. Explosive: 110 lbs. MV: 2,400 fps. AA barrage capability. Fictional.'}
])
ammo_id += 2

# 13.5" Additional Variants (2 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '13.5"', 'Mark_Designation': 'Mark VI', 'Projectile_Type': 'APC', 'Weight_LBS': 1400.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '13.5" Mark VI APC shell. Improved cap design. MV: 2,575 fps. Interwar modernization. Bursting charge: 24 lbs. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '13.5"', 'Mark_Designation': 'Mark VII', 'Projectile_Type': 'HE', 'Weight_LBS': 1350.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '13.5" Mark VII HE shell. Explosive content: 95 lbs. MV: 2,500 fps. Shore bombardment. Fictional.'}
])
ammo_id += 2

# 12" Additional Variants (4 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '12"', 'Mark_Designation': 'Mark XIII', 'Projectile_Type': 'APC', 'Weight_LBS': 850.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '12" Mark XIII APC shell. Improved cap. MV: 2,825 fps. Bursting charge: 15 lbs. Dreadnought evolution. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '12"', 'Mark_Designation': 'Mark XIV', 'Projectile_Type': 'HE', 'Weight_LBS': 820.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '12" Mark XIV HE shell. Explosive content: 60 lbs. MV: 2,700 fps. Shore bombardment. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '12"', 'Mark_Designation': 'Mark XV', 'Projectile_Type': 'CPC', 'Weight_LBS': 850.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '12" Mark XV CPC semi-AP. General-purpose. MV: 2,825 fps. Bursting charge: 25 lbs. Interwar. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '12"', 'Mark_Designation': 'Mark XVI', 'Projectile_Type': 'AP', 'Weight_LBS': 850.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '12" Mark XVI AP shell. High-velocity variant. MV: 2,900 fps. Pre-war large cruiser. Improved penetration. Fictional.'}
])
ammo_id += 4

# 8" Additional Variants (3 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '8"', 'Mark_Designation': 'Mark IX', 'Projectile_Type': 'APC', 'Weight_LBS': 256.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '8" Mark IX APC shell. Improved Mark VIII. MV: 2,750 fps. Better penetration. Post-County development. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '8"', 'Mark_Designation': 'Mark X', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 250.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '8" Mark X HE-VT shell. Proximity fused. MV: 2,700 fps. Explosive: 22 lbs. AA capable. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '8"', 'Mark_Designation': 'Mark XI', 'Projectile_Type': 'Illum', 'Weight_LBS': 245.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '8" Mark XI Illumination shell. Night combat. MV: 2,650 fps. Star shell. Fictional.'}
])
ammo_id += 3

# 6" Additional Variants (4 types)
fictional_ammunition.extend([
    {'ID': ammo_id, 'Caliber': '6"', 'Mark_Designation': 'Mark XIX', 'Projectile_Type': 'APC', 'Weight_LBS': 112.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '6" Mark XIX APC shell. Improved penetrator. MV: 2,850 fps. Post-war cruiser ammunition. Fictional.'},
    {'ID': ammo_id+1, 'Caliber': '6"', 'Mark_Designation': 'Mark XX', 'Projectile_Type': 'HE-VT', 'Weight_LBS': 110.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '6" Mark XX HE-VT shell. Proximity fused. MV: 2,760 fps. Explosive: 10 lbs. AA barrage. Fictional.'},
    {'ID': ammo_id+2, 'Caliber': '6"', 'Mark_Designation': 'Mark XXI', 'Projectile_Type': 'SAP', 'Weight_LBS': 112.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '6" Mark XXI SAP shell. Light armor targets. MV: 2,800 fps. Bursting charge: 4 lbs. Fictional.'},
    {'ID': ammo_id+3, 'Caliber': '6"', 'Mark_Designation': 'Mark XXII', 'Projectile_Type': 'Illum', 'Weight_LBS': 105.0, 'Country': 'Britain', 'Modded': 1, 'Notes': '6" Mark XXII Illumination shell. Night operations. MV: 2,700 fps. Star shell. Fictional.'}
])
ammo_id += 4

print(f"Total ammunition types generated: {len(fictional_ammunition)}")
print()

# Group by caliber
by_caliber = {}
for ammo in fictional_ammunition:
    cal = ammo['Caliber']
    if cal not in by_caliber:
        by_caliber[cal] = []
    by_caliber[cal].append(ammo)

print("Breakdown by caliber:")
for caliber in sorted(by_caliber.keys(), key=lambda x: float(x.replace('"', '')), reverse=True):
    print(f"  {caliber}: {len(by_caliber[caliber])} types")

print()
print("Saving ammunition to JSON file...")

# Save to JSON
with open('../../data/fictional_british_ammunition.json', 'w', encoding='utf-8') as f:
    json.dump(fictional_ammunition, f, indent=2)

print("Saved to: ../../data/fictional_british_ammunition.json")
print()

# Generate SQL INSERT statements
print("Generating SQL INSERT statements...")
sql_statements = []

for ammo in fictional_ammunition:
    notes_escaped = ammo['Notes'].replace("'", "''")
    mark = f"'{ammo['Mark_Designation']}'" if ammo['Mark_Designation'] else "NULL"

    sql = f"""INSERT INTO Ammunition (ID, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Country, Modded, Notes)
VALUES ({ammo['ID']}, '{ammo['Caliber']}', {mark}, '{ammo['Projectile_Type']}', {ammo['Weight_LBS']}, '{ammo['Country']}', {ammo['Modded']}, '{notes_escaped}');"""
    sql_statements.append(sql)

with open('../../database/sql/insert_fictional_british_ammunition.sql', 'w', encoding='utf-8') as f:
    f.write("-- Fictional British Naval Ammunition\n")
    f.write("-- Generated: October 10, 2025\n")
    f.write(f"-- Count: {len(fictional_ammunition)} ammunition types\n")
    f.write(f"-- Ammunition IDs: 184-{ammo_id-1}\n")
    f.write("-- All marked as Modded=1 (fictional)\n\n")
    f.write('\n\n'.join(sql_statements))

print("Saved SQL to: ../../database/sql/insert_fictional_british_ammunition.sql")
print()

print("=" * 80)
print("FICTIONAL BRITISH AMMUNITION GENERATION COMPLETE")
print("=" * 80)
print(f"Generated {len(fictional_ammunition)} ammunition types (IDs 184-{ammo_id-1})")
print("All ammunition marked as Modded=1 (fictional)")
print("Ready for compatibility generation (next phase)")
print()
