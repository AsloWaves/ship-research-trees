#!/usr/bin/env python3
"""
Generate Japan and Germany Ship Tree Canvases
Creates chronological ship trees similar to USA and Great-Britain
"""

import json
import hashlib
import os
from typing import Dict, List, Tuple

# Read chronological data from text files
def read_chronological_data(filepath: str) -> Dict[str, List[Tuple[int, str]]]:
    """Parse chronological list file and return organized ship data"""
    data = {
        "Battleships": [],
        "Carriers": [],
        "Cruisers": [],
        "Destroyers": [],
        "Submarines": [],
        "Transports-Amphibious": []
    }

    current_category = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.endswith(':') and line[:-1] in data:
                if line.endswith(':'):
                    current_category = line[:-1]
                continue

            if current_category and line.startswith('- ') and ': ' in line:
                # Parse: "- filename.md: year"
                parts = line[2:].split(': ')
                if len(parts) == 2:
                    filename, year_str = parts
                    try:
                        year = int(year_str)
                        data[current_category].append((year, filename))
                    except ValueError:
                        print(f"Warning: Invalid year '{year_str}' for {filename}")

    return data

# Y-coordinate bands for each category
Y_BANDS = {
    "Battleships": -4500,
    "Cruisers": -700,
    "Destroyers": 2200,
    "Carriers": 5100,
    "Submarines": 7800,
    "Transports-Amphibious": 10500,
}

# Spacing constants
NODE_WIDTH = 400
NODE_HEIGHT = 400
HORIZONTAL_SPACING = 500
VERTICAL_SPACING = 300

def generate_id(seed: str) -> str:
    """Generate a 16-character hex ID"""
    return hashlib.md5(seed.encode()).hexdigest()[:16]

def year_to_x(year: int, start_year: int = 1890) -> int:
    """Convert year to X coordinate"""
    return (year - start_year) * 200  # 200px per year

def create_file_node(nation: str, category: str, filename: str, year: int, x: int, y: int) -> Dict:
    """Create a file node"""
    file_path = f"Ships/{nation}/{category}/{filename}"
    node_id = generate_id(f"{nation}-{category}-{filename}-{year}")

    return {
        "id": node_id,
        "type": "file",
        "file": file_path,
        "x": x,
        "y": y,
        "width": NODE_WIDTH,
        "height": NODE_HEIGHT
    }

def create_group_node(label: str, x: int, y: int, width: int, height: int) -> Dict:
    """Create a group node"""
    node_id = generate_id(f"GROUP-{label}")
    return {
        "id": node_id,
        "type": "group",
        "x": x,
        "y": y,
        "width": width,
        "height": height,
        "label": label
    }

def create_edge(from_id: str, to_id: str) -> Dict:
    """Create an edge between two nodes"""
    edge_id = generate_id(f"EDGE-{from_id}-{to_id}")
    return {
        "id": edge_id,
        "fromNode": from_id,
        "fromSide": "right",
        "toNode": to_id,
        "toSide": "left"
    }

def generate_canvas(nation: str, ship_data: Dict[str, List[Tuple[int, str]]]) -> Dict:
    """Generate canvas for a nation"""
    nodes = []
    edges = []
    node_ids_by_ship = {}

    # Determine start year based on earliest ship
    all_years = [year for ships in ship_data.values() for year, _ in ships if ships]
    start_year = min(all_years) if all_years else 1890

    print(f"\n{nation}: Start year = {start_year}, Total ships = {sum(len(s) for s in ship_data.values())}")

    # Process each category
    for category, ships in ship_data.items():
        if not ships:
            continue

        ships_sorted = sorted(ships, key=lambda x: x[0])
        base_y = Y_BANDS[category]

        # Track Y offsets for ships in same year
        year_counts = {}

        for year, filename in ships_sorted:
            x = year_to_x(year, start_year)

            # Handle multiple ships in same year
            if year not in year_counts:
                year_counts[year] = 0
            else:
                year_counts[year] += 1

            # Alternate above/below the base line
            if year_counts[year] % 2 == 0:
                y = base_y + (year_counts[year] // 2) * VERTICAL_SPACING
            else:
                y = base_y - ((year_counts[year] + 1) // 2) * VERTICAL_SPACING

            # Create node
            node = create_file_node(nation, category, filename, year, x, y)
            nodes.append(node)

            # Track node ID
            ship_key = f"{category}/{filename}"
            node_ids_by_ship[ship_key] = node["id"]

    # Create group nodes
    for category, ships in ship_data.items():
        if not ships:
            continue

        years = [y for y, _ in ships]
        min_year = min(years)
        max_year = max(years)

        group_x = year_to_x(min_year, start_year) - 50
        group_y = Y_BANDS[category] - 800
        group_width = year_to_x(max_year, start_year) - year_to_x(min_year, start_year) + NODE_WIDTH + 100
        group_height = 1800

        group = create_group_node(category, group_x, group_y, group_width, group_height)
        nodes.append(group)

    return {
        "nodes": nodes,
        "edges": edges
    }

# Generate both canvases
print("=" * 60)
print("GENERATING JAPAN & GERMANY SHIP TREE CANVASES")
print("=" * 60)

# Japan
print("\nProcessing JAPAN...")
japan_data = read_chronological_data("C:/Research/Japan_Ships_Chronological_List.txt")
japan_canvas = generate_canvas("Japan", japan_data)
japan_output = "C:/Research/Ships/Japan/Japan Ship Tree.canvas"
with open(japan_output, 'w', encoding='utf-8') as f:
    json.dump(japan_canvas, f, indent=1)
print(f"[OK] Japan canvas created: {len(japan_canvas['nodes'])} nodes, {len(japan_canvas['edges'])} edges")

# Germany
print("\nProcessing GERMANY...")
germany_data = read_chronological_data("C:/Research/Germany_Ships_Chronological_List.txt")
germany_canvas = generate_canvas("Germany", germany_data)
germany_output = "C:/Research/Ships/Germany/Germany Ship Tree.canvas"
with open(germany_output, 'w', encoding='utf-8') as f:
    json.dump(germany_canvas, f, indent=1)
print(f"[OK] Germany canvas created: {len(germany_canvas['nodes'])} nodes, {len(germany_canvas['edges'])} edges")

print("\n" + "=" * 60)
print("CANVAS GENERATION COMPLETE")
print("=" * 60)
