"""
Analyze naval_guns_database.md for data completeness
"""

def analyze_table_section(lines, start_marker, end_marker):
    """Extract and analyze a table section"""
    in_section = False
    table_lines = []

    for line in lines:
        if start_marker in line:
            in_section = True
        elif end_marker in line:
            break
        elif in_section:
            table_lines.append(line)

    return table_lines

def parse_markdown_table(table_lines):
    """Parse markdown table into list of dicts"""
    # Find the header line
    header_idx = None
    for i, line in enumerate(table_lines):
        if line.strip().startswith('|') and 'Gun_ID' in line or 'ID' in line or 'Turret_ID' in line:
            header_idx = i
            break

    if header_idx is None:
        return [], []

    # Parse header
    header = [col.strip() for col in table_lines[header_idx].split('|')[1:-1]]

    # Skip separator line
    data_start = header_idx + 2

    # Parse data rows
    rows = []
    for line in table_lines[data_start:]:
        if line.strip().startswith('|'):
            cols = [col.strip() for col in line.split('|')[1:-1]]
            if len(cols) == len(header):
                row = dict(zip(header, cols))
                rows.append(row)

    return header, rows

def count_empty_fields(rows, field_name):
    """Count empty or missing values in a field"""
    if not rows:
        return 0, 0

    total = len(rows)
    empty = sum(1 for row in rows if not row.get(field_name, '').strip())
    filled = total - empty
    return filled, empty

# Read the file
with open('naval_guns_database.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=" * 80)
print("NAVAL GUNS DATABASE - COMPLETENESS ANALYSIS")
print("=" * 80)
print()

# Analyze Guns Table
guns_section = analyze_table_section(lines, "## Guns Table", "## Ammunition Table")
guns_header, guns_data = parse_markdown_table(guns_section)

if guns_data:
    print(f"GUNS TABLE - {len(guns_data)} entries")
    print("-" * 80)
    for field in guns_header:
        filled, empty = count_empty_fields(guns_data, field)
        pct = (filled / len(guns_data) * 100) if guns_data else 0
        status = "OK" if empty == 0 else "!!"
        print(f"  [{status}] {field:20s}: {filled:3d}/{len(guns_data):3d} filled ({pct:5.1f}%) - {empty:3d} empty")
    print()

# Analyze Ammunition Table
ammo_section = analyze_table_section(lines, "## Ammunition Table", "## Turrets Table")
ammo_header, ammo_data = parse_markdown_table(ammo_section)

if ammo_data:
    print(f"AMMUNITION TABLE - {len(ammo_data)} entries")
    print("-" * 80)
    for field in ammo_header:
        filled, empty = count_empty_fields(ammo_data, field)
        pct = (filled / len(ammo_data) * 100) if ammo_data else 0
        status = "OK" if empty == 0 else "!!"
        print(f"  [{status}] {field:20s}: {filled:3d}/{len(ammo_data):3d} filled ({pct:5.1f}%) - {empty:3d} empty")
    print()

# Analyze Turrets Table
turrets_section = analyze_table_section(lines, "## Turrets Table", "## Gun Ammunition Compatibility")
turrets_header, turrets_data = parse_markdown_table(turrets_section)

if turrets_data:
    print(f"TURRETS TABLE - {len(turrets_data)} entries")
    print("-" * 80)
    for field in turrets_header:
        filled, empty = count_empty_fields(turrets_data, field)
        pct = (filled / len(turrets_data) * 100) if turrets_data else 0
        status = "OK" if empty == 0 else "!!"
        print(f"  [{status}] {field:20s}: {filled:3d}/{len(turrets_data):3d} filled ({pct:5.1f}%) - {empty:3d} empty")
    print()

# Analyze Compatibility Table
compat_section = analyze_table_section(lines, "## Gun Ammunition Compatibility", "## Data Completeness")
compat_header, compat_data = parse_markdown_table(compat_section)

if compat_data:
    print(f"COMPATIBILITY TABLE - {len(compat_data)} entries")
    print("-" * 80)
    for field in compat_header:
        filled, empty = count_empty_fields(compat_data, field)
        pct = (filled / len(compat_data) * 100) if compat_data else 0
        status = "OK" if empty == 0 else "!!"
        print(f"  [{status}] {field:20s}: {filled:3d}/{len(compat_data):3d} filled ({pct:5.1f}%) - {empty:3d} empty")
    print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total Guns:          {len(guns_data)}")
print(f"Total Ammunition:    {len(ammo_data)}")
print(f"Total Turrets:       {len(turrets_data)}")
print(f"Total Compatibilities: {len(compat_data)}")
print()
