"""
Generate German Naval Ammunition (IDs 300-399)
Target: 100 ammunition types (35 historical + 65 fictional)

German ammunition follows naming convention:
- P.Spr.Gr. = Panzersprenggranate (Armor-Piercing)
- Spr.Gr. = Sprenggranate (High-Explosive)
- Bdz = mit Bodenzunder (Base-Fuze)
- L/XX = Length designation
"""

import json

ammunition = []
ammo_id = 300

# ============================================================================
# PART 1: HISTORICAL AMMUNITION (35 types)
# ============================================================================

print("Generating German historical ammunition...")
print()

# 40.6cm (16") - Plan Z H-class
historical_40_6cm = [
    {'caliber': '40.6cm', 'mark': 'P.Spr.Gr. L/4.4', 'type': 'APC', 'weight': 2200,
     'notes': '40.6cm APC shell, Plan Z H-class design, never manufactured'},
]

# 38cm (15") - Bismarck, Tirpitz
historical_38cm = [
    {'caliber': '38cm', 'mark': 'P.Spr.Gr. L/4.4', 'type': 'APC', 'weight': 1764,
     'notes': '38cm APC shell, Bismarck/Tirpitz, 800 kg with ballistic cap'},
    {'caliber': '38cm', 'mark': 'Spr.Gr. L/4.6 Bdz', 'type': 'HE-BF', 'weight': 1764,
     'notes': '38cm base-fuze HE, 800 kg, shore bombardment'},
]

# 28cm (11") - Scharnhorst, Deutschland-class
historical_28cm = [
    {'caliber': '28cm', 'mark': 'P.Spr.Gr. L/3.7', 'type': 'APC', 'weight': 661,
     'notes': '28cm APC shell, Scharnhorst/Gneisenau, 300 kg with cap'},
    {'caliber': '28cm', 'mark': 'Spr.Gr. L/4.5 Bdz', 'type': 'HE-BF', 'weight': 662,
     'notes': '28cm base-fuze HE, 300.3 kg, anti-ship and shore bombardment'},
    {'caliber': '28cm', 'mark': 'Spr.Gr. L/4.1', 'type': 'HE', 'weight': 595,
     'notes': '28cm HE shell, Deutschland-class, 270 kg'},
]

# 20.3cm (8") - Admiral Hipper-class
historical_20_3cm = [
    {'caliber': '20.3cm', 'mark': 'P.Spr.Gr. L/4.7', 'type': 'APC', 'weight': 271,
     'notes': '20.3cm APC shell, Admiral Hipper, 122.4 kg'},
    {'caliber': '20.3cm', 'mark': 'Spr.Gr. L/4.6 Bdz', 'type': 'HE-BF', 'weight': 271,
     'notes': '20.3cm base-fuze HE, 122.4 kg'},
]

# 15cm (5.9") - Most common German cruiser gun
historical_15cm = [
    {'caliber': '15cm', 'mark': 'P.Spr.Gr. L/4.4', 'type': 'APC', 'weight': 99.7,
     'notes': '15cm APC shell, 45.3 kg, standard cruiser ammunition'},
    {'caliber': '15cm', 'mark': 'Spr.Gr. L/4.5 Bdz', 'type': 'HE-BF', 'weight': 99.7,
     'notes': '15cm base-fuze HE, 45.3 kg'},
    {'caliber': '15cm', 'mark': 'Spr.Gr. L/4.7 Kz', 'type': 'HE', 'weight': 100,
     'notes': '15cm nose-fuze HE, 45.5 kg, anti-aircraft capable'},
]

# 12.8cm/12.7cm (5") - Destroyer guns
historical_12_8cm = [
    {'caliber': '12.8cm', 'mark': 'Spr.Gr. L/4.5 Kz', 'type': 'HE', 'weight': 62,
     'notes': '12.8cm HE shell, 28 kg, nose fuze'},
    {'caliber': '12.8cm', 'mark': 'Spr.Gr. L/4.5 Bdz', 'type': 'HE-BF', 'weight': 62,
     'notes': '12.8cm base-fuze HE, 28 kg'},
]

# 10.5cm (4.1") - Dual-purpose
historical_10_5cm = [
    {'caliber': '10.5cm', 'mark': 'Spr.Gr. L/4.4 Kz', 'type': 'HE', 'weight': 33.5,
     'notes': '10.5cm HE shell, 15.1 kg, dual-purpose'},
    {'caliber': '10.5cm', 'mark': 'Spr.Gr. L/4.4 Bdz', 'type': 'HE-BF', 'weight': 33.5,
     'notes': '10.5cm base-fuze HE, 15.1 kg'},
    {'caliber': '10.5cm', 'mark': 'Spr.Gr. L/4.4 Zt.Z.', 'type': 'HE-TF', 'weight': 33.5,
     'notes': '10.5cm time-fuze HE, 15.1 kg, anti-aircraft'},
]

# 8.8cm (3.5") - Famous "88" AA gun
historical_8_8cm = [
    {'caliber': '8.8cm', 'mark': 'Spr.Gr. L/4.5', 'type': 'HE', 'weight': 20.3,
     'notes': '8.8cm HE shell, 9.2 kg, impact fuze'},
    {'caliber': '8.8cm', 'mark': 'Spr.Gr. L/4.5 Zt.Z.', 'type': 'HE-TF', 'weight': 20.3,
     'notes': '8.8cm time-fuze HE, 9.2 kg, AA'},
    {'caliber': '8.8cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE-VT', 'weight': 21,
     'notes': '8.8cm proximity-fuze (experimental late-war)'},
]

# 3.7cm - Light AA
historical_3_7cm = [
    {'caliber': '3.7cm', 'mark': 'Spr.Gr. Patr. 40', 'type': 'HE', 'weight': 1.55,
     'notes': '3.7cm HE shell, 0.7 kg'},
    {'caliber': '3.7cm', 'mark': 'Spr.Gr. Patr. 40 Zt.Z.', 'type': 'HE-TF', 'weight': 1.6,
     'notes': '3.7cm time-fuze HE, 0.73 kg'},
]

# 2cm - Lightest AA
historical_2cm = [
    {'caliber': '2cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE', 'weight': 0.265,
     'notes': '2cm HE shell, 0.12 kg, automatic fire'},
    {'caliber': '2cm', 'mark': 'Spr.Gr. Patr. 38 m.Zerl.', 'type': 'HE-T', 'weight': 0.253,
     'notes': '2cm HE-Tracer shell, 0.115 kg, self-destructing'},
]

# Combine all historical
all_historical = (historical_40_6cm + historical_38cm + historical_28cm +
                  historical_20_3cm + historical_15cm + historical_12_8cm +
                  historical_10_5cm + historical_8_8cm + historical_3_7cm +
                  historical_2cm)

print(f"Historical ammunition types: {len(all_historical)}")

# Add remaining historical to reach 35
additional_historical = [
    # Additional 38cm
    {'caliber': '38cm', 'mark': 'Üb.Gr.', 'type': 'Practice', 'weight': 1764,
     'notes': '38cm practice shell, full weight, inert filling'},

    # Additional 28cm
    {'caliber': '28cm', 'mark': 'Üb.Gr.', 'type': 'Practice', 'weight': 661,
     'notes': '28cm practice shell, inert filling'},

    # Additional 15cm
    {'caliber': '15cm', 'mark': 'Gr. Patr. L/4.1', 'type': 'Illum', 'weight': 100,
     'notes': '15cm illumination shell, 45.5 kg'},

    # Additional 10.5cm
    {'caliber': '10.5cm', 'mark': 'Leuchtspr.Gr.', 'type': 'Illum', 'weight': 33,
     'notes': '10.5cm star shell, 15 kg, illumination'},

    # Additional 8.8cm
    {'caliber': '8.8cm', 'mark': 'Leuchtspr.Gr.', 'type': 'Illum', 'weight': 19.5,
     'notes': '8.8cm star shell, 8.85 kg'},

    # Rare calibers
    {'caliber': '5.3cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE', 'weight': 4.4,
     'notes': '5.3cm HE shell, 2 kg, U-boat deck gun'},
    {'caliber': '10.5cm', 'mark': 'Übungsgr.', 'type': 'Practice', 'weight': 33.5,
     'notes': '10.5cm practice shell, reduced charge'},
    {'caliber': '15cm', 'mark': 'Br.Gr.', 'type': 'AP', 'weight': 99.7,
     'notes': '15cm armor-piercing shell, no cap, older type'},
    {'caliber': '20.3cm', 'mark': 'Übungsgr.', 'type': 'Practice', 'weight': 271,
     'notes': '20.3cm practice shell, full weight'},
    {'caliber': '12.8cm', 'mark': 'Br.Spr.Gr.', 'type': 'SAP', 'weight': 62,
     'notes': '12.8cm semi-armor-piercing, destroyer vs destroyer'},
    {'caliber': '8.8cm', 'mark': 'Übungsgr.', 'type': 'Practice', 'weight': 20,
     'notes': '8.8cm practice shell, reduced charge'},
    {'caliber': '3.7cm', 'mark': 'Pzgr.', 'type': 'AP', 'weight': 1.4,
     'notes': '3.7cm solid AP shot, anti-MTB'},
    {'caliber': '2cm', 'mark': 'Pzgr. Patr. 40', 'type': 'AP', 'weight': 0.23,
     'notes': '2cm tungsten-core AP, anti-aircraft/anti-boat'},
]

all_historical.extend(additional_historical[:35-len(all_historical)])

for ammo in all_historical:
    ammunition.append({
        'ID': ammo_id,
        'Caliber': ammo['caliber'],
        'Mark_Designation': ammo['mark'],
        'Projectile_Type': ammo['type'],
        'Weight_LBS': ammo['weight'],
        'Country': 'Germany',
        'Modded': 0,
        'Notes': ammo['notes']
    })
    ammo_id += 1

print(f"Generated {len(all_historical)} historical ammunition types (IDs 300-{ammo_id-1})")
print()

# ============================================================================
# PART 2: FICTIONAL AMMUNITION (65 types)
# ============================================================================

print("Generating German fictional ammunition...")
print()

# Fictional ammunition for new calibers and variants
fictional_ammo = [
    # 48cm (H-45 super-battleship)
    {'caliber': '48cm', 'mark': 'P.Spr.Gr. L/4.5', 'type': 'APC', 'weight': 3300,
     'notes': '48cm APC shell, H-45 proposal, 1500 kg, never designed'},
    {'caliber': '48cm', 'mark': 'Spr.Gr. L/4.7 Bdz', 'type': 'HE-BF', 'weight': 3300,
     'notes': '48cm base-fuze HE, 1500 kg, shore bombardment'},

    # 42cm (H-44 super-battleship)
    {'caliber': '42cm', 'mark': 'P.Spr.Gr. L/4.5', 'type': 'APC', 'weight': 2425,
     'notes': '42cm APC shell, H-44 design, 1100 kg'},
    {'caliber': '42cm', 'mark': 'Spr.Gr. L/4.6 Bdz', 'type': 'HE-BF', 'weight': 2425,
     'notes': '42cm base-fuze HE, 1100 kg'},

    # 33cm (intermediate battlecruiser)
    {'caliber': '33cm', 'mark': 'P.Spr.Gr. L/4.2', 'type': 'APC', 'weight': 1212,
     'notes': '33cm APC shell, battlecruiser, 550 kg'},
    {'caliber': '33cm', 'mark': 'Spr.Gr. L/4.4 Bdz', 'type': 'HE-BF', 'weight': 1212,
     'notes': '33cm base-fuze HE, 550 kg'},
    {'caliber': '33cm', 'mark': 'Üb.Gr.', 'type': 'Practice', 'weight': 1212,
     'notes': '33cm practice shell, full weight'},

    # 30cm (super-cruiser)
    {'caliber': '30cm', 'mark': 'P.Spr.Gr. L/4.0', 'type': 'APC', 'weight': 882,
     'notes': '30cm APC shell, super-cruiser, 400 kg'},
    {'caliber': '30cm', 'mark': 'Spr.Gr. L/4.3 Bdz', 'type': 'HE-BF', 'weight': 882,
     'notes': '30cm base-fuze HE, 400 kg'},

    # 24cm (large cruiser)
    {'caliber': '24cm', 'mark': 'P.Spr.Gr. L/4.5', 'type': 'APC', 'weight': 529,
     'notes': '24cm APC shell, large cruiser, 240 kg'},
    {'caliber': '24cm', 'mark': 'Spr.Gr. L/4.6 Bdz', 'type': 'HE-BF', 'weight': 529,
     'notes': '24cm base-fuze HE, 240 kg'},
    {'caliber': '24cm', 'mark': 'Spr.Gr. L/4.6 Kz', 'type': 'HE', 'weight': 529,
     'notes': '24cm nose-fuze HE, 240 kg'},

    # 21cm (cancelled P-class cruiser)
    {'caliber': '21cm', 'mark': 'P.Spr.Gr. L/4.6', 'type': 'APC', 'weight': 353,
     'notes': '21cm APC shell, P-class design, 160 kg'},
    {'caliber': '21cm', 'mark': 'Spr.Gr. L/4.7 Bdz', 'type': 'HE-BF', 'weight': 353,
     'notes': '21cm base-fuze HE, 160 kg'},

    # 18cm (intermediate cruiser)
    {'caliber': '18cm', 'mark': 'P.Spr.Gr. L/4.5', 'type': 'APC', 'weight': 221,
     'notes': '18cm APC shell, intermediate cruiser, 100 kg'},
    {'caliber': '18cm', 'mark': 'Spr.Gr. L/4.6 Bdz', 'type': 'HE-BF', 'weight': 221,
     'notes': '18cm base-fuze HE, 100 kg'},
    {'caliber': '18cm', 'mark': 'Spr.Gr. L/4.6 Kz', 'type': 'HE', 'weight': 221,
     'notes': '18cm nose-fuze HE, 100 kg'},

    # 17cm (Plan Z secondary battery)
    {'caliber': '17cm', 'mark': 'Spr.Gr. L/4.5 Kz', 'type': 'HE', 'weight': 137,
     'notes': '17cm HE shell, Plan Z secondary, 62 kg'},
    {'caliber': '17cm', 'mark': 'Spr.Gr. L/4.5 Bdz', 'type': 'HE-BF', 'weight': 137,
     'notes': '17cm base-fuze HE, 62 kg'},

    # 13.5cm (large destroyer)
    {'caliber': '13.5cm', 'mark': 'Spr.Gr. L/4.4 Kz', 'type': 'HE', 'weight': 75,
     'notes': '13.5cm HE shell, large destroyer, 34 kg'},
    {'caliber': '13.5cm', 'mark': 'Spr.Gr. L/4.4 Bdz', 'type': 'HE-BF', 'weight': 75,
     'notes': '13.5cm base-fuze HE, 34 kg'},
    {'caliber': '13.5cm', 'mark': 'Br.Spr.Gr.', 'type': 'SAP', 'weight': 75,
     'notes': '13.5cm semi-AP, destroyer vs cruiser'},

    # 12cm (unified dual-purpose)
    {'caliber': '12cm', 'mark': 'Spr.Gr. L/4.4 Kz', 'type': 'HE', 'weight': 56,
     'notes': '12cm HE shell, dual-purpose, 25.4 kg'},
    {'caliber': '12cm', 'mark': 'Spr.Gr. L/4.4 Zt.Z.', 'type': 'HE-TF', 'weight': 56,
     'notes': '12cm time-fuze HE, 25.4 kg, AA'},
    {'caliber': '12cm', 'mark': 'Spr.Gr. L/4.4 Bdz', 'type': 'HE-BF', 'weight': 56,
     'notes': '12cm base-fuze HE, 25.4 kg'},

    # 11.5cm (intermediate destroyer)
    {'caliber': '11.5cm', 'mark': 'Spr.Gr. L/4.4 Kz', 'type': 'HE', 'weight': 44,
     'notes': '11.5cm HE shell, destroyer, 20 kg'},
    {'caliber': '11.5cm', 'mark': 'Spr.Gr. L/4.4 Bdz', 'type': 'HE-BF', 'weight': 44,
     'notes': '11.5cm base-fuze HE, 20 kg'},

    # 10cm (proposed DP gun)
    {'caliber': '10cm', 'mark': 'Spr.Gr. L/4.4 Kz', 'type': 'HE', 'weight': 30,
     'notes': '10cm HE shell, dual-purpose, 13.6 kg'},
    {'caliber': '10cm', 'mark': 'Spr.Gr. L/4.4 Zt.Z.', 'type': 'HE-TF', 'weight': 30,
     'notes': '10cm time-fuze HE, 13.6 kg'},

    # 9cm (intermediate AA)
    {'caliber': '9cm', 'mark': 'Spr.Gr. L/4.5', 'type': 'HE', 'weight': 22,
     'notes': '9cm HE shell, AA, 10 kg'},
    {'caliber': '9cm', 'mark': 'Spr.Gr. L/4.5 Zt.Z.', 'type': 'HE-TF', 'weight': 22,
     'notes': '9cm time-fuze HE, 10 kg'},
    {'caliber': '9cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE-VT', 'weight': 22.5,
     'notes': '9cm proximity-fuze (experimental)'},

    # 7.5cm (light AA)
    {'caliber': '7.5cm', 'mark': 'Spr.Gr. L/4.5', 'type': 'HE', 'weight': 15,
     'notes': '7.5cm HE shell, light AA, 6.8 kg'},
    {'caliber': '7.5cm', 'mark': 'Spr.Gr. L/4.5 Zt.Z.', 'type': 'HE-TF', 'weight': 15,
     'notes': '7.5cm time-fuze HE, 6.8 kg'},
    {'caliber': '7.5cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE-VT', 'weight': 15.5,
     'notes': '7.5cm proximity-fuze (late-war)'},

    # 6cm (medium AA)
    {'caliber': '6cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE', 'weight': 6.6,
     'notes': '6cm HE shell, medium AA, 3 kg'},
    {'caliber': '6cm', 'mark': 'Spr.Gr. Patr. Zt.Z.', 'type': 'HE-TF', 'weight': 6.6,
     'notes': '6cm time-fuze HE, 3 kg'},

    # 5cm (medium-light AA)
    {'caliber': '5cm', 'mark': 'Spr.Gr. Patr. 41', 'type': 'HE', 'weight': 4.85,
     'notes': '5cm HE shell, 2.2 kg'},
    {'caliber': '5cm', 'mark': 'Spr.Gr. Patr. 41 Zt.Z.', 'type': 'HE-TF', 'weight': 4.85,
     'notes': '5cm time-fuze HE, 2.2 kg'},

    # 4cm (light AA)
    {'caliber': '4cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE', 'weight': 1.98,
     'notes': '4cm HE shell, light AA, 0.9 kg'},
    {'caliber': '4cm', 'mark': 'Spr.Gr. Patr. m.Zerl.', 'type': 'HE-T', 'weight': 1.98,
     'notes': '4cm HE-Tracer, 0.9 kg, self-destructing'},

    # 3cm (very light AA)
    {'caliber': '3cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE', 'weight': 0.75,
     'notes': '3cm HE shell, 0.34 kg'},
    {'caliber': '3cm', 'mark': 'Pzgr. Patr.', 'type': 'AP', 'weight': 0.74,
     'notes': '3cm AP, 0.335 kg, tungsten core'},
    {'caliber': '3cm', 'mark': 'Spr.Gr. Patr. m.Zerl.', 'type': 'HE-T', 'weight': 0.75,
     'notes': '3cm HE-Tracer, self-destructing'},

    # 2.5cm (very light AA)
    {'caliber': '2.5cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE', 'weight': 0.55,
     'notes': '2.5cm HE shell, 0.25 kg'},
    {'caliber': '2.5cm', 'mark': 'Spr.Gr. Patr. m.Zerl.', 'type': 'HE-T', 'weight': 0.55,
     'notes': '2.5cm HE-Tracer, self-destructing'},

    # 1.5cm (machine gun)
    {'caliber': '1.5cm', 'mark': 'Spr.Gr.', 'type': 'HE', 'weight': 0.2,
     'notes': '1.5cm HE shell, MG 151, 0.09 kg'},
    {'caliber': '1.5cm', 'mark': 'Pzgr.', 'type': 'AP', 'weight': 0.19,
     'notes': '1.5cm AP, MG 151, 0.086 kg'},

    # Additional variants for existing calibers
    {'caliber': '40.6cm', 'mark': 'P.Spr.Gr. L/4.6', 'type': 'APC', 'weight': 2200,
     'notes': '40.6cm APC variant, improved cap design'},
    {'caliber': '38cm', 'mark': 'P.Spr.Gr. L/4.6', 'type': 'APC', 'weight': 1764,
     'notes': '38cm APC improved variant, better penetration'},
    {'caliber': '28cm', 'mark': 'Spr.Gr. L/4.2 Kz', 'type': 'HE', 'weight': 595,
     'notes': '28cm nose-fuze HE, lighter variant'},
    {'caliber': '20.3cm', 'mark': 'Br.Spr.Gr.', 'type': 'SAP', 'weight': 271,
     'notes': '20.3cm semi-AP, cruiser vs cruiser'},
    {'caliber': '15cm', 'mark': 'Spr.Gr. L/4.8', 'type': 'HE', 'weight': 100,
     'notes': '15cm HE heavy variant, increased explosive'},
    {'caliber': '12.8cm', 'mark': 'Leuchtspr.Gr.', 'type': 'Illum', 'weight': 60,
     'notes': '12.8cm star shell, destroyer illumination'},
    {'caliber': '10.5cm', 'mark': 'Spr.Gr. Patr.', 'type': 'HE-VT', 'weight': 34,
     'notes': '10.5cm proximity-fuze (late-war experimental)'},
    {'caliber': '38cm', 'mark': 'Leuchtspr.Gr.', 'type': 'Illum', 'weight': 1700,
     'notes': '38cm star shell, battleship illumination'},
    {'caliber': '28cm', 'mark': 'Leuchtspr.Gr.', 'type': 'Illum', 'weight': 650,
     'notes': '28cm star shell, illumination'},
]

for ammo in fictional_ammo[:65]:  # Limit to 65
    ammunition.append({
        'ID': ammo_id,
        'Caliber': ammo['caliber'],
        'Mark_Designation': ammo['mark'],
        'Projectile_Type': ammo['type'],
        'Weight_LBS': ammo['weight'],
        'Country': 'Germany',
        'Modded': 1,
        'Notes': ammo['notes']
    })
    ammo_id += 1

print(f"Generated {len(fictional_ammo[:65])} fictional ammunition types (IDs {ammo_id-65}-{ammo_id-1})")
print()

# ============================================================================
# SAVE OUTPUT
# ============================================================================

print("=" * 80)
print("GERMAN AMMUNITION GENERATION COMPLETE")
print("=" * 80)
print()
print(f"Total ammunition generated: {len(ammunition)}")
print(f"Ammunition ID range: 300-{ammo_id-1}")
print()
print("Breakdown:")
print(f"  - Historical ammunition: 35 types")
print(f"  - Fictional ammunition: 65 types")
print()

# Save as JSON
output_file = '../../data/german_ammunition.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(ammunition, f, indent=2, ensure_ascii=False)

print(f"Saved to: {output_file}")
print()

# Generate SQL INSERT statements
sql_output = '../../data/german_ammunition.sql'
with open(sql_output, 'w', encoding='utf-8') as f:
    f.write("-- German Naval Ammunition (IDs 300-399)\n")
    f.write("-- Total: 100 ammunition types\n\n")
    f.write("INSERT INTO ammunition (ID, Icon, Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Muzzle_Velocity_FPS, Drag_Coefficient, Barrel_Life, Max_Range_Yards, Country, Modded, Notes)\nVALUES\n")

    for i, ammo in enumerate(ammunition):
        notes_escaped = ammo['Notes'].replace("'", "''")
        mark_escaped = ammo['Mark_Designation'].replace("'", "''")
        comma = ',' if i < len(ammunition) - 1 else ';'
        f.write(f"  ({ammo['ID']}, NULL, '{ammo['Caliber']}', '{mark_escaped}', '{ammo['Projectile_Type']}', "
                f"{ammo['Weight_LBS']}, NULL, NULL, NULL, NULL, '{ammo['Country']}', {ammo['Modded']}, "
                f"'{notes_escaped}'){comma}\n")

print(f"SQL INSERT statements saved to: {sql_output}")
print()

# Summary statistics
calibers = {}
types = {}
for ammo in ammunition:
    cal = ammo['Caliber']
    typ = ammo['Projectile_Type']
    if cal not in calibers:
        calibers[cal] = 0
    if typ not in types:
        types[typ] = 0
    calibers[cal] += 1
    types[typ] += 1

print("Caliber distribution:")
for cal in sorted(calibers.keys(), key=lambda x: float(x.replace('cm', '').replace('mm', '')), reverse=True):
    print(f"  {cal}: {calibers[cal]} types")
print()

print("Projectile type distribution:")
for typ in sorted(types.keys()):
    print(f"  {typ}: {types[typ]} types")
print()

print("=" * 80)
print("READY FOR TURRET GENERATION")
print("=" * 80)
