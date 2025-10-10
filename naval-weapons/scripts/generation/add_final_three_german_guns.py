"""
Add final 3 German guns to reach 100 total (IDs 797-799)
"""

import json

# Load existing fictional guns
with open('../../data/fictional_german_guns.json', 'r', encoding='utf-8') as f:
    guns = json.load(f)

print(f"Current count: {len(guns)} guns (IDs 723-796)")
print("Adding 3 more guns to reach 100 total...")
print()

# Add 3 final guns (IDs 797-799)
final_guns = [
    {
        'Gun_ID': 797,
        'Country': 'Germany',
        'Caliber': '40.6cm',
        'Length': '/45',
        'Mark_Designation': 'SK C/36',
        'Year_Introduced': 1937,
        'Weight': 115.0,
        'Modded': 1,
        'Notes': '40.6cm/45 SK C/36 - Early H-class proposal, shorter barrel'
    },
    {
        'Gun_ID': 798,
        'Country': 'Germany',
        'Caliber': '6cm',
        'Length': '/60',
        'Mark_Designation': 'SK C/40',
        'Year_Introduced': 1940,
        'Weight': 0.65,
        'Modded': 1,
        'Notes': '6cm/60 SK C/40 - Medium AA gun, between 5cm and 7.5cm'
    },
    {
        'Gun_ID': 799,
        'Country': 'Germany',
        'Caliber': '1.5cm',
        'Length': '/65',
        'Mark_Designation': 'MG 151',
        'Year_Introduced': 1940,
        'Weight': 0.042,
        'Modded': 1,
        'Notes': '1.5cm/65 MG 151 - Very light AA machine gun, naval adaptation'
    }
]

# Add to existing guns
guns.extend(final_guns)

print(f"Added 3 guns:")
for gun in final_guns:
    print(f"  ID {gun['Gun_ID']}: {gun['Caliber']} {gun['Length']} {gun['Mark_Designation']}")
print()

# Save updated file
with open('../../data/fictional_german_guns.json', 'w', encoding='utf-8') as f:
    json.dump(guns, f, indent=2, ensure_ascii=False)

print(f"Total fictional guns: {len(guns)} (IDs 723-799)")
print()
print("=" * 80)
print("GERMAN FICTIONAL GUNS COMPLETE: 77 guns")
print("Total German guns: 23 historical + 77 fictional = 100 guns")
print("=" * 80)
