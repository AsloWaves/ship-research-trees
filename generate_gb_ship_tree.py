#!/usr/bin/env python3
"""
Generate Great-Britain Ship Tree Canvas
Creates a chronological ship tree similar to the USA Ship Tree structure
"""

import json
import hashlib
from typing import Dict, List, Tuple

# Ship data organized by category with commissioning years
SHIP_DATA = {
    "Battleships": [
        (1892, "Royal-Sovereign-Class.md"),
        (1895, "Majestic-Class.md"),
        (1899, "Canopus-Class.md"),
        (1901, "Formidable-Class.md"),
        (1903, "Duncan-Class.md"),
        (1905, "King-Edward-VII-Class.md"),
        (1906, "HMS-Dreadnought.md"),
        (1908, "Invincible-Class-Battlecruiser.md"),
        (1908, "Lord-Nelson-Class.md"),
        (1909, "Bellerophon-Class.md"),
        (1909, "St-Vincent-Class.md"),
        (1910, "Colossus-Class.md"),
        (1911, "HMS-Neptune.md"),
        (1911, "Indefatigable-Class-Battlecruiser.md"),
        (1912, "King-George-V-Class-1912.md"),
        (1912, "Lion-Class-Battlecruiser.md"),
        (1912, "Orion-Class.md"),
        (1914, "Erin-Class.md"),
        (1914, "HMS-Tiger-Battlecruiser.md"),
        (1914, "Iron-Duke-Class.md"),
        (1914, "Queen-Elizabeth-Class.md"),
        (1916, "Courageous-Class.md"),
        (1916, "Renown-Class.md"),
        (1916, "Revenge-Class.md"),
        (1920, "HMS-Hood.md"),
        (1927, "Nelson-Class.md"),
        (1940, "King-George-V-Class.md"),
        (1946, "HMS-Vanguard.md"),
        # Cancelled designs at end
        (1922, "G3-Battlecruiser.md"),
        (1920, "HMS-Incomparable-Proposal.md"),
        (1942, "Lion-Class-1939.md"),
        (1922, "N3-Battleship.md"),
    ],
    "Carriers": [
        (1917, "HMS-Furious.md"),
        (1918, "HMS-Argus.md"),
        (1924, "HMS-Eagle-1924.md"),
        (1924, "HMS-Hermes-1924.md"),
        (1938, "HMS-Ark-Royal-1938.md"),
        (1940, "Illustrious-Class.md"),
        (1942, "Activity-Class.md"),
        (1942, "Attacker-Class.md"),
        (1943, "Ruler-Class.md"),
        (1944, "Colossus-Class-Carrier.md"),
        (1944, "Implacable-Class.md"),
        (1951, "Audacious-Class.md"),
        (1953, "Centaur-Class.md"),
        (1955, "Majestic-Class.md"),
        (1925, "Courageous-Class-Carriers.md"),  # Estimated date
        (1980, "Invincible-Class.md"),
        (2017, "Queen-Elizabeth-Class-Carrier.md"),
        # Cancelled
        (1970, "CVA-01.md"),
        (1945, "Malta-Class-Cancelled.md"),
        (1943, "Project-Habakkuk.md"),
    ],
    "Cruisers": [
        (1878, "Comus-Class.md"),
        (1878, "Iris-Class.md"),
        (1882, "Leander-Class-1882.md"),
        (1885, "Mersey-Class.md"),
        (1888, "Orlando-Class.md"),
        (1892, "Blake-Class.md"),
        (1893, "Edgar-Class.md"),
        (1897, "Eclipse-Class.md"),
        (1897, "Pelorus-Class.md"),
        (1897, "Powerful-Class.md"),
        (1898, "Diadem-Class.md"),
        (1898, "Highflyer-Class.md"),
        (1901, "Cressy-Class.md"),
        (1902, "Challenger-Class.md"),
        (1902, "Drake-Class.md"),
        (1903, "Monmouth-Class.md"),
        (1905, "Adventure-Class.md"),
        (1905, "Devonshire-Class.md"),
        (1906, "Duke-of-Edinburgh-Class.md"),
        (1906, "Warrior-Class.md"),
        (1908, "Minotaur-Class-AC.md"),
        (1914, "Arethusa-Class-1914.md"),
        (1914, "Caroline-Class.md"),
        (1915, "Calliope-Class.md"),
        (1916, "Cambrian-Class.md"),
        (1916, "Centaur-Class-1916.md"),
        (1917, "Caledon-Class.md"),
        (1917, "Ceres-Class.md"),
        (1918, "Carlisle-Class.md"),
        (1918, "Danae-Class.md"),
        (1919, "Hawkins-Class.md"),
        (1926, "Emerald-Class.md"),
        (1928, "County-Class-Cruiser.md"),
        (1930, "York-Class.md"),
        (1933, "Leander-Class.md"),
        (1935, "Arethusa-Class-1935.md"),
        (1936, "Amphion-Class.md"),
        (1937, "Town-Class-Cruiser.md"),
        (1940, "Crown-Colony-Class-Cruiser.md"),
        (1940, "Dido-Class.md"),
        (1944, "Minotaur-Class-1945.md"),
        (1945, "Lion-Class-Cancelled.md"),  # Cancelled
        (1950, "Minotaur-Conversions-Cancelled.md"),  # Cancelled
        (1951, "Neptune-Conversions.md"),
        (1959, "Tiger-Helicopter-Cruisers.md"),
        (1973, "Bristol-Type-82.md"),
    ],
    "Destroyers": [
        (1893, "Daring-Class-TBD.md"),
        (1893, "Ferret-Class.md"),
        (1893, "Havock-Class.md"),
        (1894, "27-Knotter.md"),
        (1903, "River-Class.md"),
        (1906, "Cricket-Class.md"),
        (1907, "Tribal-Class-1907.md"),
        (1909, "Beagle-Class.md"),
        (1910, "Acheron-Class.md"),
        (1910, "Acorn-Class.md"),
        (1912, "Acasta-Class.md"),
        (1913, "Laforey-Class.md"),
        (1914, "M-Class.md"),
        (1916, "R-Class.md"),
        (1917, "V-Class.md"),
        (1917, "V-and-W-Class.md"),
        (1918, "S-Class.md"),
        (1918, "W-Class.md"),
        (1919, "Modified-W-Class.md"),
        (1926, "Amazon-Type.md"),
        (1926, "Ambuscade-Type.md"),
        (1927, "A-Class.md"),
        (1929, "B-Class.md"),
        (1931, "C-D-E-Class.md"),
        (1934, "F-G-H-I-Class.md"),
        (1938, "Tribal-Class-1936.md"),
        (1939, "J-K-N-Class.md"),
        (1940, "Hunt-Class.md"),
        (1940, "L-M-Class-Destroyer.md"),
        (1940, "Town-Class-Destroyer.md"),
        (1941, "O-P-Class.md"),
        (1941, "Q-R-Class.md"),
        (1942, "S-T-Class-WWII.md"),
        (1943, "U-V-Class-WWII.md"),
        (1943, "W-Z-Class-WWII.md"),
        (1944, "Battle-Class.md"),
        (1944, "C-Class-WWII.md"),
        (1944, "G-Class-WWII.md"),
        (1947, "Weapon-Class.md"),
        (1952, "Daring-Class-1949.md"),
        (1962, "County-Class-DDG.md"),
        (1975, "Type-42-Destroyer.md"),
        (1981, "Type-43-Destroyer.md"),
        (2009, "Type-45-Destroyer.md"),
        (2030, "Type-83-Destroyer.md"),
    ],
    "Submarines": [
        (1901, "Holland-Class.md"),
        (1903, "A-Class-Submarine.md"),
        (1905, "B-Class-Submarine.md"),
        (1906, "C-Class-Submarine.md"),
        (1910, "D-Class-Submarine.md"),
        (1913, "E-Class-Submarine.md"),
        (1915, "F-Class-Submarine.md"),
        (1915, "H-Class-Submarine.md"),
        (1916, "G-Class-Submarine.md"),
        (1916, "J-Class-Submarine.md"),
        (1917, "K-Class-Submarine.md"),
        (1918, "L-Class-Submarine.md"),
        (1918, "M-Class-Submarine.md"),
        (1918, "R-Class-Submarine.md"),
        (1925, "HMS-X1.md"),
        (1929, "Odin-Class-Submarine.md"),
        (1930, "Parthian-Class-Submarine.md"),
        (1932, "S-Class-Submarine.md"),
        (1938, "T-Class-Submarine.md"),
        (1942, "X-Class-Midget.md"),
        (1945, "Amphion-Class-Submarine.md"),
        (1958, "Porpoise-Class-Submarine.md"),
        (1961, "Oberon-Class-Submarine.md"),
        (1963, "Dreadnought-Class-SSN.md"),
        (1966, "Valiant-Class-SSN.md"),
        (1967, "Resolution-Class-SSBN.md"),
        (1970, "Churchill-Class-SSN.md"),
        (1973, "Swiftsure-Class-SSN.md"),
        (1983, "Trafalgar-Class-SSN.md"),
        (1990, "Upholder-Class-Submarine.md"),
        (1993, "Vanguard-Class-SSBN.md"),
        (2010, "Astute-Class.md"),
        (2030, "SSN-AUKUS.md"),
        (2031, "Dreadnought-Class-SSBN.md"),
    ],
    "Transports-Amphibious": [
        (1940, "HMS-Glengyle-LSI.md"),
        (1941, "LCT-Mark-4-Class.md"),
        (1942, "LST-2-Class-Lend-Lease.md"),
        (1943, "Boxer-Class-LST.md"),
        (1943, "LCI-L-Class-Lend-Lease.md"),
        (1944, "LST-3-Class.md"),
        (1963, "Round-Table-Class-LSL.md"),
        (1998, "HMS-Ocean-LPH.md"),
        (2003, "Albion-Class-LPD.md"),
        (2006, "Bay-Class-LSD.md"),
    ],
}

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
    """Generate a 16-character hex ID similar to Obsidian's format"""
    return hashlib.md5(seed.encode()).hexdigest()[:16]

def year_to_x(year: int) -> int:
    """Convert year to X coordinate (chronological left-to-right)"""
    # Start at x=0 for 1878, scale to ~300px per year
    return (year - 1878) * 300

def create_file_node(category: str, filename: str, year: int, x: int, y: int) -> Dict:
    """Create a file node"""
    # Map category names to folder names (actual directory structure)
    folder_map = {
        "Battleships": "Battleships",
        "Carriers": "Carriers",
        "Cruisers": "Cruisers",
        "Destroyers": "Destroyers",
        "Submarines": "Submarines",
        "Transports-Amphibious": "Transports-Amphibious",
    }

    file_path = f"Great-Britain/{folder_map[category]}/{filename}"
    node_id = generate_id(f"GB-{category}-{filename}-{year}")

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

def generate_canvas() -> Dict:
    """Generate the complete canvas structure"""
    nodes = []
    edges = []

    # Track node IDs for creating edges
    node_ids_by_ship = {}

    # Process each category
    for category, ships in SHIP_DATA.items():
        # Sort ships by year
        ships_sorted = sorted(ships, key=lambda x: x[0])

        base_y = Y_BANDS[category]

        # Track Y offsets for ships in same year (create rows)
        year_counts = {}

        for year, filename in ships_sorted:
            # Calculate X position based on year
            x = year_to_x(year)

            # If multiple ships in same year, stack them vertically
            if year not in year_counts:
                year_counts[year] = 0
            else:
                year_counts[year] += 1

            # Alternate above/below the base line for same-year ships
            if year_counts[year] % 2 == 0:
                y = base_y + (year_counts[year] // 2) * VERTICAL_SPACING
            else:
                y = base_y - ((year_counts[year] + 1) // 2) * VERTICAL_SPACING

            # Create node
            node = create_file_node(category, filename, year, x, y)
            nodes.append(node)

            # Track node ID
            ship_key = f"{category}/{filename}"
            node_ids_by_ship[ship_key] = node["id"]

    # Create group nodes for each category
    for category in SHIP_DATA.keys():
        ships = SHIP_DATA[category]
        if not ships:
            continue

        years = [s[0] for s in ships]
        min_year = min(years)
        max_year = max(years)

        # Calculate group bounds
        group_x = year_to_x(min_year) - 50
        group_y = Y_BANDS[category] - 800
        group_width = year_to_x(max_year) - year_to_x(min_year) + NODE_WIDTH + 100
        group_height = 1800  # Enough to contain vertically stacked ships

        group = create_group_node(category, group_x, group_y, group_width, group_height)
        nodes.append(group)

    # Create evolutionary connection edges
    # Define some key evolutionary connections
    connections = [
        # Battleships
        ("Battleships/HMS-Dreadnought.md", "Battleships/Bellerophon-Class.md"),
        ("Battleships/Bellerophon-Class.md", "Battleships/St-Vincent-Class.md"),
        ("Battleships/St-Vincent-Class.md", "Battleships/Colossus-Class.md"),
        ("Battleships/Colossus-Class.md", "Battleships/Orion-Class.md"),
        ("Battleships/Orion-Class.md", "Battleships/King-George-V-Class-1912.md"),
        ("Battleships/King-George-V-Class-1912.md", "Battleships/Iron-Duke-Class.md"),
        ("Battleships/Iron-Duke-Class.md", "Battleships/Queen-Elizabeth-Class.md"),
        ("Battleships/Queen-Elizabeth-Class.md", "Battleships/Revenge-Class.md"),
        ("Battleships/Revenge-Class.md", "Battleships/Nelson-Class.md"),
        ("Battleships/Nelson-Class.md", "Battleships/King-George-V-Class.md"),
        ("Battleships/King-George-V-Class.md", "Battleships/HMS-Vanguard.md"),

        # Battlecruisers line
        ("Battleships/Invincible-Class-Battlecruiser.md", "Battleships/Indefatigable-Class-Battlecruiser.md"),
        ("Battleships/Indefatigable-Class-Battlecruiser.md", "Battleships/Lion-Class-Battlecruiser.md"),
        ("Battleships/Lion-Class-Battlecruiser.md", "Battleships/HMS-Hood.md"),

        # Carriers
        ("Carriers/HMS-Furious.md", "Carriers/HMS-Argus.md"),
        ("Carriers/HMS-Argus.md", "Carriers/HMS-Hermes-1924.md"),
        ("Carriers/HMS-Hermes-1924.md", "Carriers/HMS-Ark-Royal-1938.md"),
        ("Carriers/HMS-Ark-Royal-1938.md", "Carriers/Illustrious-Class.md"),
        ("Carriers/Illustrious-Class.md", "Carriers/Implacable-Class.md"),
        ("Carriers/Implacable-Class.md", "Carriers/Audacious-Class.md"),
        ("Carriers/Audacious-Class.md", "Carriers/Invincible-Class.md"),
        ("Carriers/Invincible-Class.md", "Carriers/Queen-Elizabeth-Class-Carrier.md"),

        # Destroyers
        ("Destroyers/Havock-Class.md", "Destroyers/27-Knotter.md"),
        ("Destroyers/27-Knotter.md", "Destroyers/River-Class.md"),
        ("Destroyers/Tribal-Class-1907.md", "Destroyers/Beagle-Class.md"),
        ("Destroyers/V-and-W-Class.md", "Destroyers/A-Class.md"),
        ("Destroyers/A-Class.md", "Destroyers/B-Class.md"),
        ("Destroyers/B-Class.md", "Destroyers/C-D-E-Class.md"),
        ("Destroyers/Tribal-Class-1936.md", "Destroyers/Battle-Class.md"),
        ("Destroyers/Battle-Class.md", "Destroyers/Daring-Class-1949.md"),
        ("Destroyers/Daring-Class-1949.md", "Destroyers/County-Class-DDG.md"),
        ("Destroyers/County-Class-DDG.md", "Destroyers/Type-42-Destroyer.md"),
        ("Destroyers/Type-42-Destroyer.md", "Destroyers/Type-45-Destroyer.md"),
        ("Destroyers/Type-45-Destroyer.md", "Destroyers/Type-83-Destroyer.md"),

        # Submarines
        ("Submarines/Holland-Class.md", "Submarines/A-Class-Submarine.md"),
        ("Submarines/A-Class-Submarine.md", "Submarines/B-Class-Submarine.md"),
        ("Submarines/B-Class-Submarine.md", "Submarines/C-Class-Submarine.md"),
        ("Submarines/C-Class-Submarine.md", "Submarines/D-Class-Submarine.md"),
        ("Submarines/D-Class-Submarine.md", "Submarines/E-Class-Submarine.md"),
        ("Submarines/S-Class-Submarine.md", "Submarines/T-Class-Submarine.md"),
        ("Submarines/T-Class-Submarine.md", "Submarines/Amphion-Class-Submarine.md"),
        ("Submarines/Porpoise-Class-Submarine.md", "Submarines/Oberon-Class-Submarine.md"),
        ("Submarines/Dreadnought-Class-SSN.md", "Submarines/Valiant-Class-SSN.md"),
        ("Submarines/Valiant-Class-SSN.md", "Submarines/Churchill-Class-SSN.md"),
        ("Submarines/Churchill-Class-SSN.md", "Submarines/Swiftsure-Class-SSN.md"),
        ("Submarines/Swiftsure-Class-SSN.md", "Submarines/Trafalgar-Class-SSN.md"),
        ("Submarines/Trafalgar-Class-SSN.md", "Submarines/Astute-Class.md"),
        ("Submarines/Astute-Class.md", "Submarines/SSN-AUKUS.md"),

        # SSBNs
        ("Submarines/Resolution-Class-SSBN.md", "Submarines/Vanguard-Class-SSBN.md"),
        ("Submarines/Vanguard-Class-SSBN.md", "Submarines/Dreadnought-Class-SSBN.md"),
    ]

    # Create edges for defined connections
    for from_ship, to_ship in connections:
        if from_ship in node_ids_by_ship and to_ship in node_ids_by_ship:
            edge = create_edge(node_ids_by_ship[from_ship], node_ids_by_ship[to_ship])
            edges.append(edge)

    return {
        "nodes": nodes,
        "edges": edges
    }

if __name__ == "__main__":
    print("Generating Great-Britain Ship Tree Canvas...")
    canvas = generate_canvas()

    output_file = "C:/Research/Ships/Great-Britain/Great-Britain Ship Tree.canvas"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(canvas, f, indent=1)

    print(f"Generated canvas with {len(canvas['nodes'])} nodes and {len(canvas['edges'])} edges")
    print(f"Output: {output_file}")
