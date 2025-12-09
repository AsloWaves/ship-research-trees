#!/usr/bin/env python3
"""
Update chronological lists with uncommissioned ships
"""

# Uncommissioned ships by nation and category with era years
UNCOMMISSIONED = {
    "USA": {
        "Battleships": [
            (1916, "Tillman-Maximum-Battleships.md"),
            (1920, "South-Dakota-Class-1920.md"),
            (1920, "Lexington-Class-Battlecruiser.md"),
            (1943, "Montana-Class.md"),
        ],
        "Carriers": [
            (1949, "United-States-Class-CVA-58.md"),
            (1970, "CVV-Medium-Carrier.md"),  # 1970s → 1970
            (1975, "Sea-Control-Ship-SCS.md"),
        ],
        "Cruisers": [
            (1964, "Typhon-DLGN-Frigate.md"),
            (1970, "Strike-Cruiser-CSGN.md"),  # 1970s → 1970
        ],
    },
    "Great-Britain": {
        "Cruisers": [
            (1946, "Lion-Class-Cancelled.md"),
            (1950, "Neptune-Conversions.md"),  # 1950s → 1950
            (1950, "Minotaur-Conversions-Cancelled.md"),  # 1950s → 1950
        ],
        "Destroyers": [
            (1944, "G-Class-WWII.md"),
            (1981, "Type-43-Destroyer.md"),
        ],
        "Carriers": [
            (1966, "CVA-01.md"),
        ],
    },
    "Japan": {
        "Battleships": [
            (1920, "Tosa-Class.md"),
            (1920, "Amagi-Class.md"),
            (1938, "A-150-Super-Yamato.md"),
        ],
        "Cruisers": [
            (1942, "Ibuki-Class.md"),
        ],
        "Carriers": [
            (1943, "Ibuki (carrier conversion).md"),
        ],
    },
    "Germany": {
        "Battleships": [
            (1939, "H-39-Battleship.md"),
            (1939, "O-Class-Battlecruiser.md"),
            (1939, "P-Class-Battlecruiser.md"),
            (1941, "H-41-Battleship.md"),
            (1942, "H-42-Battleship.md"),
            (1943, "H-43-Battleship.md"),
            (1944, "H-44-Battleship.md"),
            (1945, "H-45-Monster-Battleship.md"),
        ],
        "Carriers": [
            (1918, "Conversion-Study-Carrier.md"),
            (1928, "Japanese-Study-Carrier.md"),
            (1935, "Plan-Z-Concept-Carrier.md"),
            (1936, "Graf-Zeppelin-Carrier.md"),
            (1938, "Peter-Strasser-Carrier.md"),
            (1940, "Flugzeugtraeger-C-Carrier.md"),
            (1940, "Flugzeugtraeger-D-Carrier.md"),
            (1942, "Europa-Conversion-Carrier.md"),
            (1943, "Improved-Graf-Zeppelin-Carrier.md"),
            (1944, "Armored-Deck-Carrier.md"),
            (1945, "Plan-Z-Super-Carrier.md"),
            (1950, "Post-War-Carrier.md"),
            (1955, "Jet-Age-Carrier.md"),
            (1960, "Modern-Carrier.md"),
            (1970, "Future-CV-Concept-Carrier.md"),
        ],
        "Cruisers": [
            (1936, "Seydlitz-Heavy-Cruiser-Class.md"),
            (1938, "P-Class-Cruiser.md"),
            (1938, "M-Class-Cruiser.md"),
            (1940, "AA-Cruiser-Concept.md"),
            (1940, "Torpedo-Cruiser-Concept.md"),
            (1940, "Super-Hipper-Class.md"),
            (1940, "Spähkreuzer-Class.md"),
            (1940, "Improved-Hipper-Class.md"),
            (1945, "Future-CL-Concept.md"),
        ],
        "Destroyers": [
            (1944, "Z46-Class.md"),
            (1944, "Z51-Diesel-Class.md"),
            (1944, "Type-1944-Destroyer.md"),
            (1945, "Z50-Class.md"),
            (1946, "Type-1945-Destroyer.md"),
            (1950, "Post-War-Destroyer.md"),
            (1955, "Future-DD-Concept.md"),
        ],
        "Submarines": [
            (1945, "Type-XXVI-Submarine.md"),
            (1945, "Type-XXIX-Submarine.md"),
            (1946, "Type-XXX-Submarine.md"),
            (1965, "Nuclear-Concept-Submarine.md"),
            (1970, "Future-SS-Concept-Submarine.md"),
        ],
    },
}

def read_existing_list(filepath):
    """Read existing chronological list and parse it"""
    data = {}
    current_category = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # Check for category headers
            if line.endswith(':') and not line.startswith('-'):
                current_category = line[:-1]
                if current_category not in data:
                    data[current_category] = []
            elif line.startswith('- ') and ': ' in line:
                # Parse: "- filename.md: year"
                parts = line[2:].split(': ')
                if len(parts) == 2:
                    filename, year_str = parts
                    try:
                        year = int(year_str)
                        data[current_category].append((year, filename))
                    except ValueError:
                        pass

    return data

def merge_ships(existing, uncommissioned):
    """Merge existing and uncommissioned ships, sort by year"""
    merged = {}

    # Get all categories
    all_categories = set(existing.keys()) | set(uncommissioned.keys())

    for category in all_categories:
        ships = []

        # Add existing ships
        if category in existing:
            ships.extend(existing[category])

        # Add uncommissioned ships
        if category in uncommissioned:
            ships.extend(uncommissioned[category])

        # Sort by year, then filename
        ships.sort(key=lambda x: (x[0], x[1]))
        merged[category] = ships

    return merged

def write_chronological_list(filepath, nation, data):
    """Write updated chronological list"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"{nation.upper()} SHIPS:\n\n")

        # Write in specific order
        category_order = ["Battleships", "Carriers", "Cruisers", "Destroyers", "Submarines", "Transports-Amphibious"]

        for category in category_order:
            if category in data and data[category]:
                f.write(f"{category}:\n")
                for year, filename in data[category]:
                    f.write(f"- {filename}: {year}\n")
                f.write("\n")

# Process each nation (skip USA - user will add manually)
nations = {
    "Great-Britain": "C:/Research/GB_Ships_Chronological_List.txt",
    "Japan": "C:/Research/Japan_Ships_Chronological_List.txt",
    "Germany": "C:/Research/Germany_Ships_Chronological_List.txt",
}

print("=" * 60)
print("UPDATING CHRONOLOGICAL LISTS WITH UNCOMMISSIONED SHIPS")
print("=" * 60)

for nation, filepath in nations.items():
    print(f"\nProcessing {nation}...")

    # Read existing
    existing = read_existing_list(filepath)
    uncommissioned = UNCOMMISSIONED.get(nation, {})

    # Count additions
    total_added = sum(len(ships) for ships in uncommissioned.values())

    # Merge
    merged = merge_ships(existing, uncommissioned)

    # Write
    write_chronological_list(filepath, nation, merged)

    # Count totals
    total_ships = sum(len(ships) for ships in merged.values())
    print(f"  Added: {total_added} uncommissioned ships")
    print(f"  Total: {total_ships} ships")

print("\n" + "=" * 60)
print("CHRONOLOGICAL LISTS UPDATED")
print("=" * 60)
