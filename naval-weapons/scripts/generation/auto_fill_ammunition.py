"""
Auto-fill ammunition data using established formulas

Formulas:
- Shell Length:
  - AP shells: length = caliber × 4.5
  - HC shells: length = caliber × 4.0
- Bursting Charge:
  - AP shells: charge = weight × 0.015 (1.5%)
  - HC shells: charge = weight × 0.08 (8.0%)
- Cartridge Type:
  - ≥8" = Separate (bag charges)
  - 6"-8" = Semi-fixed (adjustable)
  - ≤5" = Fixed (one-piece)
"""

import re
from decimal import Decimal, ROUND_HALF_UP

def parse_caliber(caliber_str):
    """Extract numeric caliber from string like '16"' or '5"'"""
    match = re.search(r'(\d+\.?\d*)', caliber_str)
    if match:
        return float(match.group(1))
    return None

def is_ap_shell(projectile_type):
    """Check if projectile is AP (Armor Piercing)"""
    ap_types = ['AP', 'APC', 'APCBC', 'Common']
    for ap_type in ap_types:
        if ap_type.upper() in projectile_type.upper():
            return True
    return False

def is_hc_shell(projectile_type):
    """Check if projectile is HC (High Capacity/HE)"""
    hc_types = ['HC', 'HE', 'AAC']
    for hc_type in hc_types:
        if hc_type.upper() in projectile_type.upper():
            return True
    return False

def calculate_shell_length(caliber, projectile_type):
    """Calculate shell length using formulas"""
    if is_ap_shell(projectile_type):
        return caliber * 4.5
    elif is_hc_shell(projectile_type):
        return caliber * 4.0
    else:
        # Default to AP formula for unknown types
        return caliber * 4.5

def calculate_bursting_charge(weight, projectile_type):
    """Calculate bursting charge using formulas"""
    if is_ap_shell(projectile_type):
        return weight * 0.015  # 1.5%
    elif is_hc_shell(projectile_type):
        return weight * 0.08   # 8.0%
    else:
        # Default to AP formula for unknown types
        return weight * 0.015

def determine_cartridge_type(caliber):
    """Determine cartridge type based on caliber"""
    if caliber >= 8.0:
        return "Separate"
    elif caliber >= 6.0:
        return "Semi-fixed"
    else:
        return "Fixed"

def format_number(value, decimal_places=2):
    """Format number with specified decimal places"""
    if value is None:
        return ""
    d = Decimal(str(value))
    format_str = f"0.{'0' * decimal_places}"
    return str(d.quantize(Decimal(format_str), rounding=ROUND_HALF_UP))

# Read the markdown file
print("Reading naval_guns_database.md...")
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find ammunition table section
ammo_start = None
ammo_end = None
for i, line in enumerate(lines):
    if '## Ammunition Table' in line:
        ammo_start = i
    elif ammo_start and '## Turrets Table' in line:
        ammo_end = i
        break

if not ammo_start or not ammo_end:
    print("ERROR: Could not find Ammunition Table section")
    exit(1)

print(f"Found Ammunition Table at lines {ammo_start}-{ammo_end}")

# Find header line
header_idx = None
for i in range(ammo_start, ammo_end):
    if lines[i].strip().startswith('|') and 'ID' in lines[i]:
        header_idx = i
        break

if not header_idx:
    print("ERROR: Could not find table header")
    exit(1)

# Parse header to get column indices
header_line = lines[header_idx]
header_cols = [col.strip() for col in header_line.split('|')[1:-1]]
print(f"Columns: {header_cols}")

# Find column indices
try:
    id_idx = header_cols.index('ID')
    caliber_idx = header_cols.index('Caliber')
    projectile_idx = header_cols.index('Projectile_Type')
    weight_idx = header_cols.index('Weight_LBS')
    length_idx = header_cols.index('Length_IN')
    charge_idx = header_cols.index('Bursting_Charge')
    cartridge_idx = header_cols.index('Cartridge_Type')
except ValueError as e:
    print(f"ERROR: Missing required column: {e}")
    exit(1)

# Process data rows (skip header and separator)
data_start = header_idx + 2
updates_made = 0
validation_errors = []

print("\nProcessing ammunition entries...")
print("=" * 80)

for i in range(data_start, ammo_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue

    # Parse row
    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(header_cols):
        continue

    ammo_id = cols[id_idx]
    caliber_str = cols[caliber_idx]
    projectile_type = cols[projectile_idx]
    weight_str = cols[weight_idx]
    length_str = cols[length_idx]
    charge_str = cols[charge_idx]
    cartridge_str = cols[cartridge_idx]

    # Parse values
    caliber = parse_caliber(caliber_str)
    try:
        weight = float(weight_str) if weight_str else None
    except ValueError:
        weight = None

    if not caliber:
        print(f"WARNING: Could not parse caliber for ID {ammo_id}: {caliber_str}")
        continue

    # Track if we made changes
    row_updated = False
    updates = []

    # Calculate Length_IN if missing
    if not length_str and caliber:
        calculated_length = calculate_shell_length(caliber, projectile_type)
        cols[length_idx] = format_number(calculated_length, 2)
        updates.append(f"Length={calculated_length:.2f}\"")
        row_updated = True

    # Calculate Bursting_Charge if missing
    if not charge_str and weight:
        calculated_charge = calculate_bursting_charge(weight, projectile_type)
        cols[charge_idx] = format_number(calculated_charge, 2)
        updates.append(f"Charge={calculated_charge:.2f} lbs")
        row_updated = True

    # Determine Cartridge_Type if missing
    if not cartridge_str and caliber:
        calculated_cartridge = determine_cartridge_type(caliber)
        cols[cartridge_idx] = calculated_cartridge
        updates.append(f"Cartridge={calculated_cartridge}")
        row_updated = True

    # Update line if changed
    if row_updated:
        new_line = '| ' + ' | '.join(cols) + ' |\n'
        lines[i] = new_line
        updates_made += 1

        # Print what we did
        shell_type = "AP" if is_ap_shell(projectile_type) else ("HC" if is_hc_shell(projectile_type) else "??")
        print(f"[{updates_made:3d}] ID {ammo_id:3s} | {caliber_str:5s} {projectile_type:15s} ({shell_type}) | {', '.join(updates)}")

print("=" * 80)
print(f"\nTotal updates made: {updates_made} ammunition entries")

# Write updated file FIRST (before validation, in case validation crashes)
print("\n" + "=" * 80)
print("Writing updates to naval_guns_database.md...")
with open('naval_guns_database.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print(f"[SUCCESS] Updated {updates_made} ammunition entries written to file")
print("=" * 80)

# Validate on existing entries with data
print("\n" + "=" * 80)
print("VALIDATION: Checking formula accuracy on existing data...")
print("=" * 80)

validation_count = 0
for i in range(data_start, ammo_end):
    line = lines[i].strip()
    if not line.startswith('|'):
        continue

    cols = [col.strip() for col in line.split('|')[1:-1]]
    if len(cols) != len(header_cols):
        continue

    ammo_id = cols[id_idx]
    caliber_str = cols[caliber_idx]
    projectile_type = cols[projectile_idx]
    weight_str = cols[weight_idx]
    length_str = cols[length_idx]
    charge_str = cols[charge_idx]

    caliber = parse_caliber(caliber_str)
    try:
        weight = float(weight_str) if weight_str else None
        existing_length = float(length_str) if length_str else None
        existing_charge = float(charge_str) if charge_str else None
    except ValueError:
        continue

    # Only validate if we have existing data
    if existing_length and caliber:
        calculated_length = calculate_shell_length(caliber, projectile_type)
        diff = abs(existing_length - calculated_length)
        if diff > 1.0:  # More than 1 inch difference
            validation_count += 1
            print(f"WARNING ID {ammo_id} Length: Existing={existing_length:.2f}\", Calculated={calculated_length:.2f}\", Diff={diff:.2f}\"")

    if existing_charge and weight:
        calculated_charge = calculate_bursting_charge(weight, projectile_type)
        diff_pct = abs(existing_charge - calculated_charge) / existing_charge * 100 if existing_charge > 0 else 0
        if diff_pct > 10:  # More than 10% difference
            validation_count += 1
            print(f"WARNING ID {ammo_id} Charge: Existing={existing_charge:.2f} lbs, Calculated={calculated_charge:.2f} lbs, Diff={diff_pct:.1f}%")

if validation_count == 0:
    print("[OK] All existing data validates within acceptable tolerances!")
else:
    print(f"\n[!!] Found {validation_count} validation warnings (review recommended)")

print("=" * 80)

# Summary statistics
print("\nSUMMARY:")
print(f"  - Shell lengths calculated: ~{updates_made}")
print(f"  - Bursting charges calculated: ~{updates_made}")
print(f"  - Cartridge types determined: ~{updates_made}")
print(f"  - Validation warnings: {validation_count}")
print("\nNext step: Review naval_guns_database.md to verify changes")
