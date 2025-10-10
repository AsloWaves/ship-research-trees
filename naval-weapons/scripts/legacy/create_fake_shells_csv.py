import csv
import re

# Based on the comprehensive analysis, create fake shells with realistic data
print("Creating fake shells CSV for import...")

# Template for shell data based on existing shells
shell_templates = {
    # Realistic values based on caliber and type
    'small_caliber': {  # 3-5"
        'AP': {'weight': 55, 'velocity': 2650, 'ke': 0.9, 'explosive': 0, 'burster': 0},
        'HE': {'weight': 55, 'velocity': 2650, 'ke': 0.9, 'explosive': 11, 'burster': 4.4}
    },
    'medium_caliber': {  # 6-8"
        'AP': {'weight': 275, 'velocity': 2800, 'ke': 5.2, 'explosive': 0, 'burster': 0},
        'HE': {'weight': 275, 'velocity': 2800, 'ke': 5.2, 'explosive': 125, 'burster': 13.1}
    },
    'large_caliber': {  # 12-16"
        'AP': {'weight': 1938, 'velocity': 2500, 'ke': 25.0, 'explosive': 0, 'burster': 0},
        'HE': {'weight': 1938, 'velocity': 2500, 'ke': 25.0, 'explosive': 850, 'burster': 48.5}
    },
    'super_heavy': {  # 18-20"
        'AP': {'weight': 3200, 'velocity': 2400, 'ke': 45.0, 'explosive': 0, 'burster': 0},
        'HE': {'weight': 3200, 'velocity': 2400, 'ke': 45.0, 'explosive': 1200, 'burster': 70.0}
    }
}

# Mark designations by nation
mark_patterns = {
    'British': 'Mark VII*',
    'US': 'Mk 16*',
    'German': 'L/50*',
    'French': 'Mle 1930*',
    'Soviet': 'B-40*',
    'Japanese': 'Type 3*',
    'Italian': 'M1934*',
    'Spanish': 'Mod 1930*',
    'Netherlands': 'Model 42*',
    'Austria-Hungary': 'M1916*',
    'Brazil': 'M1940*'
}

# Special features by nation
special_features = {
    'British': 'Projected design*',
    'US': 'Theoretical development*',
    'German': 'Planned specification*',
    'French': 'Design study*',
    'Soviet': 'Project shell*',
    'Japanese': 'Concept design*',
    'Italian': 'Proposed model*',
    'Spanish': 'Hypothetical shell*',
    'Netherlands': 'Study project*',
    'Austria-Hungary': 'Pre-war design*',
    'Brazil': 'Export variant*'
}

def get_shell_template(caliber_num):
    """Determine shell template based on caliber size"""
    if caliber_num <= 5.5:
        return 'small_caliber'
    elif caliber_num <= 8.5:
        return 'medium_caliber'
    elif caliber_num <= 16.5:
        return 'large_caliber'
    else:
        return 'super_heavy'

def extract_caliber_number(caliber_str):
    """Extract numeric caliber from string like '16\"' """
    match = re.match(r'^([0-9.]+)', caliber_str.replace('"', ''))
    if match:
        return float(match.group(1))
    return 16.0  # default

# Read the recommendations file to get exact shells needed
shells_to_create = []

with open('D:/Research/shell_creation_recommendations.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

    reading_shells = False
    for line in lines:
        line = line.strip()
        if line.startswith("SHELLS TO CREATE:"):
            reading_shells = True
            continue
        elif line.startswith("ORPHAN SHELLS:"):
            reading_shells = False
            break

        if reading_shells and line and not line.startswith("-"):
            # Parse line like: 18" Soviet AP* - No shells exist for 3 gun variant(s)
            parts = line.split(' - ')
            if len(parts) >= 2:
                shell_info = parts[0].strip()
                shell_parts = shell_info.split()
                if len(shell_parts) >= 3:
                    caliber = shell_parts[0]
                    nation = shell_parts[1]
                    shell_type = shell_parts[2].replace('*', '')

                    shells_to_create.append({
                        'caliber': caliber,
                        'nation': nation,
                        'type': shell_type
                    })

print(f"Found {len(shells_to_create)} shells to create")

# Create the CSV data
csv_rows = []
csv_headers = ['Caliber', 'Burster_lbs', 'Explosive_Dmg', 'KE_MJ', 'Mark_Designation', 'Nation', 'Special_Features', 'Type', 'Velocity_fps', 'Weight_lbs']

for shell in shells_to_create:
    caliber = shell['caliber']
    nation = shell['nation']
    shell_type = shell['type']

    # Get caliber number for template selection
    caliber_num = extract_caliber_number(caliber)
    template_key = get_shell_template(caliber_num)
    template = shell_templates[template_key][shell_type]

    # Build shell name: caliber + mark + type + *
    mark = mark_patterns.get(nation, 'Mark I*')
    shell_name = f"{caliber} {mark} {shell_type}"

    csv_row = {
        'Caliber': shell_name,
        'Burster_lbs': template['burster'],
        'Explosive_Dmg': template['explosive'],
        'KE_MJ': template['ke'],
        'Mark_Designation': mark,
        'Nation': nation,
        'Special_Features': special_features.get(nation, 'Fictional shell*'),
        'Type': shell_type,
        'Velocity_fps': template['velocity'],
        'Weight_lbs': template['weight']
    }

    csv_rows.append(csv_row)

# Write CSV file
output_file = 'D:/Research/Fake_Shells_To_Import.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=csv_headers)
    writer.writeheader()
    writer.writerows(csv_rows)

print(f"\nCreated {len(csv_rows)} fake shells")
print(f"CSV saved to: {output_file}")

# Show examples by nation
print(f"\nExamples by nation:")
by_nation = {}
for row in csv_rows:
    nation = row['Nation']
    if nation not in by_nation:
        by_nation[nation] = []
    by_nation[nation].append(row['Caliber'])

for nation, shells in by_nation.items():
    print(f"  {nation}: {len(shells)} shells")
    for shell in shells[:2]:  # Show first 2
        print(f"    - {shell}")
    if len(shells) > 2:
        print(f"    ... and {len(shells) - 2} more")

print(f"\nReady for import into Notion Shell Specifications database!")
print(f"All shells marked with * to indicate they are fake/projected designs")