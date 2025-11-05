"""
Add Missing British Data to Markdown Database
- 8 missing ammunition types (IDs 101-106, 110-111)
- 96 turrets (56 base + 40 tactical variants, IDs 2001-2115 + 2200-2239)
"""

import re

# Path to the database markdown file
db_file = '../../database/naval_guns_database.md'

print("=" * 80)
print("ADDING MISSING BRITISH DATA TO MARKDOWN DATABASE")
print("=" * 80)
print()

# ===== MISSING AMMUNITION DATA (8 types) =====
missing_ammunition = [
    # 15" Ammunition (IDs 101-106)
    {
        'Ammunition_ID': 101,
        'Caliber': '15"',
        'Mark_Designation': '4crh',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 1920.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'Early 4crh (caliber radius head) AP shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: 2,450 fps. Used pre-1937 before 6crh improvements. crh = caliber radius head (ballistic cap shape). Source: NavWeaps, Wikipedia'
    },
    {
        'Ammunition_ID': 102,
        'Caliber': '15"',
        'Mark_Designation': '6crh',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 1938.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'Improved 6crh AP shell for 15"/42 Mark I. Supercharge 490 lbs cordite (1937+). Muzzle Velocity: 2,640 fps. Better aerodynamics than 4crh. Max Range: 33,550 yds @ 30° (Vanguard: 37,870 yds with supercharge). crh = caliber radius head. Source: NavWeaps, Wikipedia'
    },
    {
        'Ammunition_ID': 103,
        'Caliber': '15"',
        'Mark_Designation': 'Mark XIIIa',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1938.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'Armour-Piercing Capped shell for 15"/42 Mark I. 6crh projectile with 4crh ballistic cap. Used on WWII unmodernized ships. Supercharge 490 lbs cordite. Muzzle Velocity: 2,640 fps. APC = Armour-Piercing Capped. Source: NavWeaps, Wikipedia'
    },
    {
        'Ammunition_ID': 104,
        'Caliber': '15"',
        'Mark_Designation': 'Mark XVIIb',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1938.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'Superior penetration APC shell for 15"/42 Mark I. Harder nose, rigid body. Manufactured at Cardonald, Scotland. Limited issue - markedly superior penetration capability. Supercharge 490 lbs cordite. Muzzle Velocity: 2,640 fps. APC = Armour-Piercing Capped. Source: NavWeaps, Wikipedia'
    },
    {
        'Ammunition_ID': 105,
        'Caliber': '15"',
        'Mark_Designation': '',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 1938.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'High Explosive shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: ~2,450 fps. Used for shore bombardment and anti-surface targets. Typical WWII loadout: 30-60 APC/CPC rounds, balance HE. HMS Vanguard carried 5 HE per gun. HE = High Explosive. Source: NavWeaps, Wikipedia'
    },
    {
        'Ammunition_ID': 106,
        'Caliber': '15"',
        'Mark_Designation': '',
        'Projectile_Type': 'CPC',
        'Projectile_Weight_LBS': 1938.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'Common Pointed Capped (semi-AP) shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: ~2,450 fps. Used against lightly armored targets and as general-purpose shell. Typical WWII loadout: 30-60 APC/CPC rounds, balance HE. CPC = Common Pointed Capped. Source: NavWeaps, Wikipedia'
    },
    # 14" Ammunition (IDs 110-111)
    {
        'Ammunition_ID': 110,
        'Caliber': '14"',
        'Mark_Designation': 'Mark VIIB',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1590.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'Armour-Piercing Capped shell for 14"/45 Mark VII (KGV-class). Bursting charge: 39.8 lbs (18.1 kg) - proportionally large for caliber. Propellant: 338.3 lbs per round. Muzzle Velocity: 2,483 fps (AP). Stowage: 100 rounds per gun. Barrel Life: ~340 rounds. APC = Armour-Piercing Capped. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
    },
    {
        'Ammunition_ID': 111,
        'Caliber': '14"',
        'Mark_Designation': '',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 1590.0,
        'Country': 'Britain',
        'Modded': 0,
        'Notes': 'High Explosive shell for 14"/45 Mark VII (KGV-class). Explosive content: 107 lbs (48.5 kg). Propellant: 338.3 lbs per round. Muzzle Velocity: ~2,400 fps. Used for shore bombardment and anti-surface targets. Stowage: 100 rounds per gun. HE = High Explosive. Source: Wikipedia, NavWeaps, Naval Encyclopedia'
    },
]

print("[1/7] Reading current database...")
with open(db_file, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"  Current file size: {len(content):,} characters")
print()

# ===== PARSE BASE TURRETS FROM SQL FILE =====
print("[2/7] Parsing base turrets from SQL file...")
sql_file = '../../database/sql/import_british_naval_weapons.sql'
with open(sql_file, 'r', encoding='utf-8') as f:
    sql_content = f.read()

# Extract turret INSERT statements using regex
turret_pattern = re.compile(
    r'\((\d+),\s*(\d+),\s*\'([^\']+)\',\s*\'([^\']+)\',\s*\'([^\']+)\',\s*\'([^\']+)\',\s*'
    r'([\d.]+),\s*(\d+),\s*'
    r'([\d.]+),\s*([\d.]+),\s*([\d.]+),\s*'
    r'([\d.]+),\s*'
    r'(-?\d+),\s*(\d+),\s*'
    r'(?:([\d.]+),\s*)?'  # Optional Elevation_Rate_Deg_Sec
    r'([\d.]+),\s*([01]),\s*'
    r'\'([^\']+)\'\)',
    re.MULTILINE
)

base_turrets = []
for match in turret_pattern.finditer(sql_content):
    turret_id = int(match.group(1))
    gun_id = int(match.group(2))
    country = match.group(3)
    caliber = match.group(4)
    turret_type = match.group(5)
    designation = match.group(6)
    weight = float(match.group(7))
    crew = int(match.group(8))
    armor_face = float(match.group(9))
    armor_sides = float(match.group(10))
    armor_roof = float(match.group(11))
    traverse = float(match.group(12))
    elev_min = int(match.group(13))
    elev_max = int(match.group(14))
    elev_rate = match.group(15)  # May be None
    rof = float(match.group(16))
    modded = int(match.group(17))
    notes = match.group(18)

    base_turrets.append({
        'Turret_ID': turret_id,
        'Gun_ID': gun_id,
        'Country': country,
        'Caliber': caliber,
        'Turret_Type': turret_type,
        'Designation': designation,
        'Turret_Weight_Tons': weight,
        'Crew_Size': crew,
        'Armor_Face_IN': armor_face,
        'Armor_Sides_IN': armor_sides,
        'Armor_Roof_IN': armor_roof,
        'Traverse_Rate_Deg_Sec': traverse,
        'Elevation_Min_Deg': elev_min,
        'Elevation_Max_Deg': elev_max,
        'Elevation_Rate_Deg_Sec': elev_rate,
        'Rate_Of_Fire_RPM': rof,
        'Modded': modded,
        'Notes': notes
    })

print(f"  Parsed {len(base_turrets)} base turrets from SQL file")
print()

# ===== PARSE TACTICAL VARIANTS FROM MARKDOWN FILE =====
print("[3/7] Parsing tactical variant turrets from generated file...")
tactical_file = '../../data/british_turret_variants_generated.md'
with open(tactical_file, 'r', encoding='utf-8') as f:
    tactical_content = f.read()

# Parse tactical variants from markdown table
tactical_turrets = []
current_gun_id = None

# Map caliber to Gun_ID
caliber_to_gun_id = {
    '6"': 530,
    '5.25"': 540,
    '4.7"': 545,
    '4.5"': 550,
    '4"': 555
}

# Parse markdown tables
for line in tactical_content.split('\n'):
    # Detect gun section headers
    if 'Gun_ID' in line:
        for cal, gid in caliber_to_gun_id.items():
            if cal in line:
                current_gun_id = gid
                break

    # Parse table rows
    if line.startswith('| ') and not ('Turret_ID' in line or '---' in line):
        parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove empty first/last
        if len(parts) >= 10 and parts[0].isdigit():
            turret_id = int(parts[0])
            turret_type = parts[1]
            weight = float(parts[2])
            crew = int(parts[3])
            armor_parts = parts[4].split('/')
            armor_face = float(armor_parts[0])
            armor_sides = float(armor_parts[1])
            armor_roof = float(armor_parts[2])
            traverse = float(parts[5])
            elev_parts = parts[6].split('/')
            elev_min = float(elev_parts[0])
            elev_max = float(elev_parts[1])
            rof = float(parts[7])
            modded = int(parts[8])
            notes = parts[9]

            # Get caliber from gun_id
            for cal, gid in caliber_to_gun_id.items():
                if gid == current_gun_id:
                    caliber = cal
                    break

            # Construct designation from type
            designation = f"{caliber}/50 {turret_type}"

            tactical_turrets.append({
                'Turret_ID': turret_id,
                'Gun_ID': current_gun_id,
                'Country': 'Britain',
                'Caliber': caliber,
                'Turret_Type': turret_type,
                'Designation': designation,
                'Turret_Weight_Tons': weight,
                'Crew_Size': crew,
                'Armor_Face_IN': armor_face,
                'Armor_Sides_IN': armor_sides,
                'Armor_Roof_IN': armor_roof,
                'Traverse_Rate_Deg_Sec': traverse,
                'Elevation_Min_Deg': int(elev_min),
                'Elevation_Max_Deg': int(elev_max),
                'Elevation_Rate_Deg_Sec': None,
                'Rate_Of_Fire_RPM': rof,
                'Modded': modded,
                'Notes': notes
            })

print(f"  Parsed {len(tactical_turrets)} tactical variant turrets")
print()

# Combine all turrets
all_turrets = base_turrets + tactical_turrets
print(f"  Total turrets to add: {len(all_turrets)} (56 base + 40 tactical)")
print()

# ===== ADD AMMUNITION TO DATABASE =====
print("[4/7] Adding 8 missing British ammunition types (IDs 101-106, 110-111)...")
lines = content.split('\n')
output_lines = []
ammo_inserted = False

i = 0
while i < len(lines):
    line = lines[i]
    output_lines.append(line)

    # Insert missing ammunition after the Ammunition table header before ID 112
    if not ammo_inserted and '## Ammunition Table' in line:
        # Find the table header row
        while i < len(lines) - 1:
            i += 1
            output_lines.append(lines[i])
            if lines[i].startswith('|---'):
                break

        # Now insert the 8 missing ammunition types
        print(f"  Inserting 8 ammunition types before ID 112...")
        for ammo in missing_ammunition:
            mark = ammo['Mark_Designation'] if ammo['Mark_Designation'] else ''
            notes_escaped = ammo['Notes'].replace('|', '\\|')
            row = f"| {ammo['Ammunition_ID']} | {ammo['Caliber']} | {mark} | {ammo['Projectile_Type']} | {ammo['Projectile_Weight_LBS']} |  |  |  |  | {ammo['Country']} | {ammo['Modded']} | {notes_escaped} |"
            output_lines.append(row)

        ammo_inserted = True

    i += 1

print(f"  Added {len(missing_ammunition)} ammunition types")
print()

# ===== ADD TURRETS TO DATABASE =====
print("[5/7] Adding 96 British turrets to database...")
turrets_inserted = False
turret_output = []

i = 0
while i < len(turret_output := output_lines):
    line = output_lines[i]

    # Insert turrets after the Turrets table header, after the last USA turret
    if not turrets_inserted and '## Turrets Table' in line:
        # Find the table header row
        j = i
        while j < len(output_lines) - 1:
            j += 1
            if output_lines[j].startswith('|---'):
                # Skip to find the last turret entry (look for next section or end)
                k = j + 1
                last_turret_line = k
                while k < len(output_lines):
                    if output_lines[k].startswith('| ') and output_lines[k].split('|')[1].strip().isdigit():
                        last_turret_line = k
                    elif output_lines[k].startswith('## '):
                        # Found next section
                        break
                    k += 1

                # Insert turrets after last turret line
                print(f"  Inserting {len(all_turrets)} British turrets...")
                new_output = output_lines[:last_turret_line + 1]

                for turret in all_turrets:
                    notes_escaped = turret['Notes'].replace('|', '\\|')
                    elev_rate = str(turret['Elevation_Rate_Deg_Sec']) if turret['Elevation_Rate_Deg_Sec'] else ''
                    row = (f"| {turret['Turret_ID']} | {turret['Gun_ID']} | {turret['Country']} | "
                           f"{turret['Caliber']} | {turret['Turret_Type']} | {turret['Designation']} | "
                           f"{turret['Turret_Weight_Tons']} | {turret['Crew_Size']} | "
                           f"{turret['Armor_Face_IN']} | {turret['Armor_Sides_IN']} | {turret['Armor_Roof_IN']} | "
                           f"{turret['Traverse_Rate_Deg_Sec']} | "
                           f"{turret['Elevation_Min_Deg']} | {turret['Elevation_Max_Deg']} | {elev_rate} | "
                           f"{turret['Rate_Of_Fire_RPM']} | {turret['Modded']} | {notes_escaped} |")
                    new_output.append(row)

                new_output.extend(output_lines[last_turret_line + 1:])
                output_lines = new_output
                turrets_inserted = True
                break

        if turrets_inserted:
            break

    i += 1

print(f"  Added {len(all_turrets)} turrets")
print()

# ===== UPDATE DATABASE TOTALS =====
print("[6/7] Updating database totals...")
new_content = '\n'.join(output_lines)

# Update ammunition count: 161 -> 169 (+8)
# Update turret count: 160 -> 256 (+96)
# Update total: 685 -> 789 (+104)

new_content = new_content.replace(
    '**Total Records**: 685 (118 guns + 161 ammunition + 160 turrets + 321 compatibility)',
    '**Total Records**: 789 (118 guns + 169 ammunition + 256 turrets + 321 compatibility)'
)

# Update Ammunition table entry count
new_content = re.sub(
    r'\*\*Total Entries\*\*: 161 ammunition',
    '**Total Entries**: 169 ammunition',
    new_content
)

# Update Turrets table entry count
new_content = re.sub(
    r'\*\*Total Entries\*\*: 160 turrets',
    '**Total Entries**: 256 turrets',
    new_content
)

print("  Updated totals:")
print("    Ammunition: 161 -> 169 (+8 missing types)")
print("    Turrets: 160 -> 256 (+96 British turrets)")
print("    TOTAL: 685 -> 789 (+104 records)")
print()

# ===== WRITE UPDATED DATABASE =====
print("[7/7] Writing updated database...")
with open(db_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"  New file size: {len(new_content):,} characters")
print()

print("=" * 80)
print("MISSING BRITISH DATA ADDITION COMPLETE")
print("=" * 80)
print()
print("Added to database:")
print("  - 8 missing ammunition types (IDs 101-106, 110-111)")
print("  - 96 British turrets (IDs 2001-2115 + 2200-2239)")
print()
print("New totals:")
print("  British: 35 guns + 80 ammo + 96 turrets + 209 compatibility = 420 records")
print("  USA: 82 guns + 81 ammo + 1,736 turrets + 112 compatibility = 2,011 records")
print("  Total database: 789 records")
print()
