"""
Add final 8 German ammunition types to reach 100 total (IDs 392-399)
"""

import json

# Load existing ammunition
with open('../../data/german_ammunition.json', 'r', encoding='utf-8') as f:
    ammunition = json.load(f)

print(f"Current count: {len(ammunition)} ammunition types (IDs 300-391)")
print("Adding 8 more types to reach 100 total...")
print()

# Add 8 final ammunition types (IDs 392-399)
final_ammo = [
    {
        'ID': 392,
        'Caliber': '2cm',
        'Mark_Designation': 'Pzgr. Patr. 40',
        'Projectile_Type': 'AP',
        'Weight_LBS': 0.23,
        'Country': 'Germany',
        'Modded': 0,
        'Notes': '2cm tungsten-core AP, anti-aircraft/anti-boat'
    },
    {
        'ID': 393,
        'Caliber': '40.6cm',
        'Mark_Designation': 'Spr.Gr. L/4.6 Bdz',
        'Projectile_Type': 'HE-BF',
        'Weight_LBS': 2200,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '40.6cm base-fuze HE variant, H-class proposal'
    },
    {
        'ID': 394,
        'Caliber': '33cm',
        'Mark_Designation': 'P.Spr.Gr. L/4.4',
        'Projectile_Type': 'APC',
        'Weight_LBS': 1212,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '33cm APC variant, battlecruiser, improved cap'
    },
    {
        'ID': 395,
        'Caliber': '30cm',
        'Mark_Designation': 'Spr.Gr. L/4.5 Kz',
        'Projectile_Type': 'HE',
        'Weight_LBS': 882,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '30cm nose-fuze HE, super-cruiser, 400 kg'
    },
    {
        'ID': 396,
        'Caliber': '24cm',
        'Mark_Designation': 'Üb.Gr.',
        'Projectile_Type': 'Practice',
        'Weight_LBS': 529,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '24cm practice shell, large cruiser training'
    },
    {
        'ID': 397,
        'Caliber': '21cm',
        'Mark_Designation': 'Spr.Gr. L/4.8 Kz',
        'Projectile_Type': 'HE',
        'Weight_LBS': 353,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '21cm nose-fuze HE, P-class, 160 kg'
    },
    {
        'ID': 398,
        'Caliber': '18cm',
        'Mark_Designation': 'Br.Spr.Gr.',
        'Projectile_Type': 'SAP',
        'Weight_LBS': 221,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '18cm semi-AP, cruiser combat, 100 kg'
    },
    {
        'ID': 399,
        'Caliber': '17cm',
        'Mark_Designation': 'Leuchtspr.Gr.',
        'Projectile_Type': 'Illum',
        'Weight_LBS': 135,
        'Country': 'Germany',
        'Modded': 1,
        'Notes': '17cm star shell, secondary battery illumination'
    }
]

# Add to existing ammunition
ammunition.extend(final_ammo)

print(f"Added 8 ammunition types:")
for ammo in final_ammo:
    print(f"  ID {ammo['ID']}: {ammo['Caliber']} {ammo['Projectile_Type']} - {ammo['Mark_Designation']}")
print()

# Save updated file
with open('../../data/german_ammunition.json', 'w', encoding='utf-8') as f:
    json.dump(ammunition, f, indent=2, ensure_ascii=False)

print(f"Total ammunition: {len(ammunition)} (IDs 300-399)")
print()
print("=" * 80)
print("GERMAN AMMUNITION COMPLETE: 100 types")
print("Breakdown: 35 historical + 65 fictional = 100 ammunition types")
print("=" * 80)
