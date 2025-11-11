#!/usr/bin/env python3
"""
Regenerate Great-Britain, Japan, and Germany ship tree canvases
with uncommissioned ships included from chronological lists
"""
import json
import re
from typing import Dict, List, Tuple

# Y-coordinate bands for each category
CATEGORY_Y_COORDS = {
    "Battleships": -4500,
    "Carriers": 5100,
    "Cruisers": -700,
    "Destroyers": 2200,
    "Submarines": 7800,
    "Transports-Amphibious": 10500,
}

# Category display names
CATEGORY_LABELS = {
    "Battleships": "Battleships",
    "Carriers": "Aircraft Carriers",
    "Cruisers": "Cruisers",
    "Destroyers": "Destroyers",
    "Submarines": "Submarines",
    "Transports-Amphibious": "Transports & Amphibious Warfare Ships",
}

def read_chronological_list(filepath: str) -> Dict[str, List[Tuple[str, int]]]:
    """Read chronological list and return ships by category"""
    ships_by_category = {}
    current_category = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            # Skip empty lines and headers
            if not line or line.startswith('=') or line.startswith('Total') or line.startswith('Date Range'):
                continue

            # Check for category headers (ends with colon, might have dashes)
            if line.endswith(':') or re.match(r'^[A-Z].*-+$', line):
                # Extract category name
                category = line.rstrip(':').rstrip('-').strip()
                # Normalize category name
                if category in ['Battleships', 'Carriers', 'Cruisers', 'Destroyers', 'Submarines', 'Transports-Amphibious']:
                    current_category = category
                    if current_category not in ships_by_category:
                        ships_by_category[current_category] = []
            elif line and current_category and ': ' in line:
                # Parse: "filename.md: year"
                parts = line.split(': ')
                if len(parts) == 2:
                    filename = parts[0]
                    try:
                        year = int(parts[1])
                        ships_by_category[current_category].append((filename, year))
                    except ValueError:
                        pass

    return ships_by_category

def year_to_x(year: int, nation: str) -> int:
    """Convert year to X coordinate"""
    if nation == "Great-Britain":
        # Range: 1878-2031 (153 years)
        return (year - 1878) * 300
    elif nation == "Japan":
        # Range: 1886-2022 (136 years)
        return (year - 1886) * 300
    elif nation == "Germany":
        # Range: 1890-1975 (85 years)
        return (year - 1890) * 300
    return year * 300

def create_file_node(nation: str, category: str, filename: str, year: int, node_id: str) -> Dict:
    """Create a file node"""
    x = year_to_x(year, nation)
    y = CATEGORY_Y_COORDS[category]

    # Proper file path format
    file_path = f"Ships/{nation}/{category}/{filename}"

    return {
        "id": node_id,
        "type": "file",
        "file": file_path,
        "x": x,
        "y": y,
        "width": 400,
        "height": 400
    }

def create_group_node(category: str, x: int, y: int, width: int, height: int, node_id: str) -> Dict:
    """Create a category group node"""
    return {
        "id": node_id,
        "type": "group",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "label": CATEGORY_LABELS[category]
    }

def generate_canvas(nation: str, ships_by_category: Dict[str, List[Tuple[str, int]]]) -> Dict:
    """Generate complete canvas JSON"""
    nodes = []
    node_counter = 0

    # Create file nodes for each category
    for category in ["Battleships", "Carriers", "Cruisers", "Destroyers", "Submarines", "Transports-Amphibious"]:
        if category not in ships_by_category or not ships_by_category[category]:
            continue

        ships = ships_by_category[category]

        # Track min/max X for group bounds
        min_x = float('inf')
        max_x = float('-inf')

        # Create file nodes
        for filename, year in ships:
            node_id = f"{node_counter:016x}"
            node_counter += 1

            x = year_to_x(year, nation)
            min_x = min(min_x, x)
            max_x = max(max_x, x)

            node = create_file_node(nation, category, filename, year, node_id)
            nodes.append(node)

        # Create group node
        group_id = f"{node_counter:016x}"
        node_counter += 1

        y = CATEGORY_Y_COORDS[category]
        group_x = min_x - 50
        group_width = (max_x - min_x) + 500

        group_node = create_group_node(category, group_x, y - 50, group_width, 500, group_id)
        nodes.append(group_node)

    return {
        "nodes": nodes,
        "edges": []
    }

# Process each nation
nations = {
    "Great-Britain": "C:/Research/Great-Britain_Ships_Chronological_List.txt",
    "Japan": "C:/Research/Japan_Ships_Chronological_List.txt",
    "Germany": "C:/Research/Germany_Ships_Chronological_List.txt",
}

print("=" * 60)
print("REGENERATING SHIP TREE CANVASES")
print("=" * 60)

for nation, list_filepath in nations.items():
    print(f"\nProcessing {nation}...")

    # Read chronological list
    ships_by_category = read_chronological_list(list_filepath)

    # Count ships
    total_ships = sum(len(ships) for ships in ships_by_category.values())
    print(f"  Total ships: {total_ships}")

    for category, ships in ships_by_category.items():
        print(f"    {category}: {len(ships)} ships")

    # Generate canvas
    canvas = generate_canvas(nation, ships_by_category)

    # Write canvas file
    canvas_path = f"C:/Research/Ships/{nation}/{nation} Ship Tree.canvas"
    with open(canvas_path, 'w', encoding='utf-8') as f:
        json.dump(canvas, f, indent=2)

    print(f"  [OK] Canvas created: {len(canvas['nodes'])} nodes")

print("\n" + "=" * 60)
print("ALL CANVASES REGENERATED")
print("=" * 60)
