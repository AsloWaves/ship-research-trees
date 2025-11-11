#!/usr/bin/env python3
"""
Add missing ship files to Great-Britain and Germany canvases
"""
import json
import re
from pathlib import Path

# Y-coordinate bands for each category
CATEGORY_Y_COORDS = {
    "Battleships": -4500,
    "Carriers": 5100,
    "Cruisers": -700,
    "Destroyers": 2200,
    "Submarines": 7800,
    "Transports-Amphibious": 10500,
}

# Missing files to add
MISSING_SHIPS = {
    "Great-Britain": {
        "Battleships": ["G3-Battlecruiser.md", "HMS-Incomparable-Proposal.md", "Lion-Class-1939.md", "N3-Battleship.md"],
        "Carriers": ["Courageous-Class-Carriers.md", "Malta-Class-Cancelled.md", "Project-Habakkuk.md"],
        "Destroyers": ["Type-83-Destroyer.md"],
        "Submarines": ["SSN-AUKUS.md"],
    },
    "Germany": {
        "Battleships": ["Ersatz-Yorck-Class.md", "H-Class.md", "L-20-e-α-Class.md", "Mackensen-Class.md", "O-Class.md"],
        "Destroyers": ["Type-1934-Refit.md", "Type-1936A-Refit.md", "V25-Modernization.md"],
    }
}

def extract_year_from_file(filepath):
    """Extract commissioned year or era year from ship file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for commissioned: field
    commissioned_match = re.search(r'^commissioned:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
    if commissioned_match:
        commissioned_value = commissioned_match.group(1).strip()

        # If it's a valid year, use it
        year_match = re.search(r'\b(1[0-9]{3}|20[0-9]{2})\b', commissioned_value)
        if year_match and commissioned_value.lower() not in ['never', 'none', 'n/a', 'cancelled']:
            return int(year_match.group(1))

    # If no valid commissioned date, look for era: field
    era_match = re.search(r'^era:\s*(.+)$', content, re.MULTILINE | re.IGNORECASE)
    if era_match:
        era_value = era_match.group(1).strip()
        # Extract earliest 4-digit year from era
        year_match = re.search(r'\b(1[0-9]{3}|20[0-9]{2})\b', era_value)
        if year_match:
            return int(year_match.group(1))

    # Fallback: look for any 4-digit year in the content
    year_match = re.search(r'\b(19[0-9]{2}|20[0-9]{2})\b', content)
    if year_match:
        return int(year_match.group(1))

    return None

def year_to_x(year, nation):
    """Convert year to X coordinate"""
    if nation == "Great-Britain":
        return (year - 1878) * 300
    elif nation == "Germany":
        return (year - 1890) * 300
    return year * 300

def get_next_node_id(existing_nodes):
    """Generate next available node ID"""
    if not existing_nodes:
        return "0000000000000001"

    # Find highest ID
    max_id = 0
    for node in existing_nodes:
        try:
            node_id_int = int(node['id'], 16)
            max_id = max(max_id, node_id_int)
        except:
            pass

    return f"{max_id + 1:016x}"

def add_missing_ships(nation, canvas_path, ships_by_category):
    """Add missing ships to canvas"""
    print(f"\nProcessing {nation}...")

    # Read existing canvas
    with open(canvas_path, 'r', encoding='utf-8') as f:
        canvas = json.load(f)

    nodes_added = 0

    # Process each category
    for category, filenames in ships_by_category.items():
        if not filenames:
            continue

        print(f"  Adding {len(filenames)} ships to {category}...")

        for filename in filenames:
            # Build file path
            file_path = f"C:/Research/Ships/{nation}/{category}/{filename}"

            # Extract year
            year = extract_year_from_file(file_path)
            if year is None:
                print(f"    WARNING: Could not extract year from {filename}, skipping")
                continue

            # Calculate position
            x = year_to_x(year, nation)
            y = CATEGORY_Y_COORDS[category]

            # Create node
            node_id = get_next_node_id(canvas['nodes'])
            node = {
                "id": node_id,
                "type": "file",
                "file": f"Ships/{nation}/{category}/{filename}",
                "x": x,
                "y": y,
                "width": 400,
                "height": 400
            }

            canvas['nodes'].append(node)
            nodes_added += 1
            try:
                print(f"    + {filename} ({year}) at x={x}")
            except UnicodeEncodeError:
                print(f"    + [ship with special chars] ({year}) at x={x}")

    # Update group bounds for each category
    print(f"  Updating category group bounds...")
    for category in ships_by_category.keys():
        # Find all file nodes in this category
        category_nodes = [n for n in canvas['nodes']
                          if n.get('type') == 'file' and category in n.get('file', '')]

        if not category_nodes:
            continue

        # Find min/max X
        min_x = min(n['x'] for n in category_nodes)
        max_x = max(n['x'] for n in category_nodes)

        # Find group node for this category
        y = CATEGORY_Y_COORDS[category]
        group_nodes = [n for n in canvas['nodes']
                       if n.get('type') == 'group' and n.get('y') == y - 50]

        if group_nodes:
            group_node = group_nodes[0]
            group_node['x'] = min_x - 50
            group_node['width'] = (max_x - min_x) + 500
            print(f"    Updated {category} group bounds")

    # Write updated canvas
    with open(canvas_path, 'w', encoding='utf-8') as f:
        json.dump(canvas, f, indent=2)

    print(f"  [OK] Added {nodes_added} ships to canvas")
    return nodes_added

# Process each nation
print("=" * 60)
print("ADDING MISSING SHIPS TO CANVASES")
print("=" * 60)

total_added = 0

for nation, ships_by_category in MISSING_SHIPS.items():
    canvas_path = f"C:/Research/Ships/{nation}/{nation} Ship Tree.canvas"
    added = add_missing_ships(nation, canvas_path, ships_by_category)
    total_added += added

print("\n" + "=" * 60)
print(f"COMPLETE: {total_added} ships added to canvases")
print("=" * 60)
