"""
Add final 6 Japanese guns to reach 100 total (IDs 894-899)
"""

import json

# Load existing fictional guns
with open('../../data/fictional_japanese_guns.json', 'r', encoding='utf-8') as f:
    guns = json.load(f)

print(f"Current count: {len(guns)} guns (IDs 817-893)")
print("Adding 6 more guns to reach 100 total (17 historical + 83 fictional)...")
print()

# Add 6 final guns (IDs 894-899)
final_guns = [
    {
        'Gun_ID': 894,
        'Country': 'Japan',
        'Caliber': '30.5cm',
        'Length': '/50',
        'Mark_Designation': 'Type 5',
        'Year_Introduced': 1945,
        'Weight': 55.0,
        'Modded': 1,
        'Notes': '30.5cm/50 Type 5 - Post-treaty battlecruiser gun'
    },
    {
        'Gun_ID': 895,
        'Country': 'Japan',
        'Caliber': '25.4cm',
        'Length': '/50',
        'Mark_Designation': 'Type 5',
        'Year_Introduced': 1943,
        'Weight': 38.0,
        'Modded': 1,
        'Notes': '25.4cm/50 Type 5 - 10" super-cruiser gun proposal'
    },
    {
        'Gun_ID': 896,
        'Country': 'Japan',
        'Caliber': '22cm',
        'Length': '/50',
        'Mark_Designation': 'Type 4',
        'Year_Introduced': 1941,
        'Weight': 26.0,
        'Modded': 1,
        'Notes': '22cm/50 Type 4 - Large cruiser gun alternative'
    },
    {
        'Gun_ID': 897,
        'Country': 'Japan',
        'Caliber': '7.6cm',
        'Length': '/40',
        'Mark_Designation': 'Type 11',
        'Year_Introduced': 1922,
        'Weight': 1.1,
        'Modded': 0,
        'Notes': '7.6cm/40 Type 11 - WWI destroyer/AA gun'
    },
    {
        'Gun_ID': 898,
        'Country': 'Japan',
        'Caliber': '4.7cm',
        'Length': '/45',
        'Mark_Designation': 'Type 11',
        'Year_Introduced': 1922,
        'Weight': 0.5,
        'Modded': 0,
        'Notes': '4.7cm/45 Type 11 - Light AA gun, sub deck gun'
    },
    {
        'Gun_ID': 899,
        'Country': 'Japan',
        'Caliber': '8cm',
        'Length': '/40',
        'Mark_Designation': 'Type 88',
        'Year_Introduced': 1928,
        'Weight': 1.35,
        'Modded': 0,
        'Notes': '8cm/40 Type 88 - Early AA gun variant'
    }
]

# Add to existing guns
guns.extend(final_guns)

print(f"Added 6 guns:")
for gun in final_guns:
    hist_or_fict = "historical" if gun['Modded'] == 0 else "fictional"
    print(f"  ID {gun['Gun_ID']}: {gun['Caliber']} {gun['Length']} {gun['Mark_Designation']} ({hist_or_fict})")
print()

# Save updated file
with open('../../data/fictional_japanese_guns.json', 'w', encoding='utf-8') as f:
    json.dump(guns, f, indent=2, ensure_ascii=False)

print(f"Total fictional guns: {len(guns)} (IDs 817-899)")
print()
print("=" * 80)
print("JAPANESE GUNS COMPLETE: 100 guns total")
print("  - Historical: 17 guns (IDs 800-816)")
print("  - Fictional: 80 guns (IDs 817-896)")
print("  - Additional Historical: 3 guns (IDs 897-899)")
print("  - Total: 20 historical + 80 fictional = 100 guns")
print("=" * 80)
