import json
import re
from pathlib import Path

# Read the canvas file
canvas_path = r"C:\Research\Weapons\Naval-Weapons\Naval-Weapons Tree.canvas"
with open(canvas_path, 'r', encoding='utf-8') as f:
    canvas_data = json.load(f)

print(f"Total nodes: {len(canvas_data['nodes'])}")

# Cache for file content to extract mark numbers
file_mark_cache = {}

def get_mark_from_file(file_path):
    """Read file and extract mark number from designation field"""
    if file_path in file_mark_cache:
        return file_mark_cache[file_path]

    full_path = Path(r"C:\Research") / file_path
    if not full_path.exists():
        return None

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Look for designation with various patterns:
            # - "3" Mark 10" or "3" Mark Mark 10"
            # - "16"/45 Mark 5/8" (extract first mark)
            # - "5"/38 Mark 30"

            # Try pattern 1: Simple Mark X or Mark Mark X
            match = re.search(r'designation:\s*\d+"\s*Mark\s+(?:Mark\s+)?(\d+)', content, re.IGNORECASE)
            if match:
                mark = int(match.group(1))
                file_mark_cache[file_path] = mark
                return mark

            # Try pattern 2: caliber/length Mark X/Y (like "16"/45 Mark 5/8")
            match = re.search(r'designation:\s*\d+"/\d+\s+Mark\s+(\d+)', content, re.IGNORECASE)
            if match:
                mark = int(match.group(1))
                file_mark_cache[file_path] = mark
                return mark

            # Try pattern 3: Just Mark X anywhere in the designation
            match = re.search(r'designation:.*?Mark\s+(\d+)', content, re.IGNORECASE)
            if match:
                mark = int(match.group(1))
                file_mark_cache[file_path] = mark
                return mark
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    file_mark_cache[file_path] = None
    return None

# Extract caliber, mark, and mount type from filename and file content
def parse_turret_info(node):
    """Parse turret info from filename and file content"""
    file_path = node.get('file', '')
    filename = Path(file_path).stem

    # Extract caliber (e.g., "3inch", "5inch", "16inch")
    caliber_match = re.search(r'(\d+)inch', filename)
    if not caliber_match:
        return None, None, None
    caliber = int(caliber_match.group(1))

    # Extract mark number from file content
    mark = get_mark_from_file(file_path)
    if mark is None:
        return caliber, None, None

    # Extract mount type from filename
    mount_type = None
    if 'Single' in filename:
        mount_type = 'Single'
    elif 'Twin' in filename or 'Double' in filename:
        mount_type = 'Twin'
    elif 'Triple' in filename:
        mount_type = 'Triple'
    elif 'Quad' in filename:
        mount_type = 'Quad'

    return caliber, mark, mount_type

# Define era colors based on mark numbers and calibers
def get_era_color(caliber, mark):
    """Determine era color based on caliber and mark"""
    # Color "1": 1900s-1920s (10", 12", early 14")
    if caliber == 10:
        return "1"
    if caliber == 12 and mark <= 5:
        return "1"
    if caliber == 14 and mark <= 1:
        return "1"

    # Color "2": 1930s
    if caliber == 3 and mark == 10:
        return "2"
    if caliber == 5 and mark <= 10:
        return "2"
    if caliber == 6 and mark <= 10:
        return "2"
    if caliber == 8 and mark <= 10:
        return "2"
    if caliber == 14 and mark in [1, 2, 3, 4]:
        return "2"

    # Color "3": 1940s
    if caliber == 5 and mark in [11, 12, 37]:
        return "3"
    if caliber == 6 and 11 <= mark <= 15:
        return "3"
    if caliber == 16 and mark in [2, 3, 5, 8]:
        return "3"

    # Color "4": 1950s-1970s
    if caliber == 5 and mark in [39, 42]:
        return "4"
    if caliber == 8 and mark == 71:
        return "4"

    # Color "5": 1980s-2000s
    if caliber == 5 and mark == 45:
        return "5"
    if caliber == 3 and mark in [33, 34]:
        return "5"

    # Default to color "3" (most common era)
    return "3"

# Caliber tier Y positions
caliber_tiers = {
    3: 100,
    4: 2100,
    5: 4100,
    6: 6100,
    8: 8100,
    10: 10100,
    12: 12100,
    13: 14100,
    14: 16100,
    16: 18100,
    18: 20100
}

# Mount type Y offsets within tier
mount_offsets = {
    'Single': 0,
    'Twin': 450,
    'Triple': 900,
    'Quad': 1350
}

# Starting X position and spacing
start_x = 730
mark_spacing = 450

# Separate turret nodes from other nodes
turret_nodes = []
other_nodes = []

for node in canvas_data['nodes']:
    file_path = node.get('file', '')
    if 'Naval-Guns/Turrets/USA/' in file_path:
        turret_nodes.append(node)
    else:
        other_nodes.append(node)

print(f"Turret nodes: {len(turret_nodes)}")
print(f"Other nodes: {len(other_nodes)}")

# Parse and organize turrets by caliber and mark
turrets_by_caliber_mark = {}
unparsed_count = 0

for node in turret_nodes:
    caliber, mark, mount_type = parse_turret_info(node)
    if caliber is None or mark is None or mount_type is None:
        unparsed_count += 1
        continue

    if caliber not in turrets_by_caliber_mark:
        turrets_by_caliber_mark[caliber] = {}
    if mark not in turrets_by_caliber_mark[caliber]:
        turrets_by_caliber_mark[caliber][mark] = []

    turrets_by_caliber_mark[caliber][mark].append({
        'node': node,
        'mount_type': mount_type
    })

print(f"Unparsed nodes: {unparsed_count}")
print(f"Parsed calibers: {sorted(turrets_by_caliber_mark.keys())}")

# Reposition turret nodes
repositioned_count = 0
for caliber in sorted(turrets_by_caliber_mark.keys()):
    if caliber not in caliber_tiers:
        print(f"Warning: No tier defined for caliber {caliber}")
        continue

    tier_y = caliber_tiers[caliber]
    marks = sorted(turrets_by_caliber_mark[caliber].keys())

    print(f"Caliber {caliber}: {len(marks)} marks - {marks}")

    for mark_idx, mark in enumerate(marks):
        mark_x = start_x + (mark_idx * mark_spacing)
        turrets = turrets_by_caliber_mark[caliber][mark]

        for turret in turrets:
            node = turret['node']
            mount_type = turret['mount_type']

            # Calculate position
            node['x'] = mark_x
            node['y'] = tier_y + mount_offsets[mount_type]

            # Set color based on era (special handling for Quad)
            if mount_type == 'Quad':
                node['color'] = "6"
            else:
                node['color'] = get_era_color(caliber, mark)

            # Set size
            node['width'] = 400
            node['height'] = 400

            repositioned_count += 1

print(f"Repositioned {repositioned_count} turret nodes")

# Update other weapon groups positions
group_positions = {
    'Bombs': 23000,
    'Missiles': 24680,
    'Torpedoes': 26360,
    'Naval-Guns-Ammunition': 28040,
    'Naval-Guns-Guns': 29720
}

# First, update group nodes
for node in other_nodes:
    if node['type'] == 'group':
        label = node.get('label', '')
        for group_name, y_pos in group_positions.items():
            if group_name in label:
                old_y = node['y']
                node['y'] = y_pos
                print(f"Moved group '{label}' from Y={old_y} to Y={y_pos}")
                break

# Update turret group node
for node in other_nodes:
    if node['type'] == 'group' and 'Turrets' in node.get('label', ''):
        node['x'] = 680
        node['y'] = 0
        node['width'] = 9300
        node['height'] = 22400
        node['label'] = "Naval-Guns-Turrets (USA Research Tree)"
        print(f"Updated turret group: {node['label']}")
        break

# Reassemble nodes
canvas_data['nodes'] = turret_nodes + other_nodes

# Write back to file
with open(canvas_path, 'w', encoding='utf-8') as f:
    json.dump(canvas_data, f, indent='\t')

print(f"\nCanvas updated successfully!")
print(f"Total nodes: {len(canvas_data['nodes'])}")
