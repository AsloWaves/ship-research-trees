#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import re
import sys
from pathlib import Path

# Set UTF-8 output encoding for Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Load the canvas
canvas_path = r'C:\Research\Weapons\Naval-Weapons\Naval-Weapons Tree.canvas'
print(f"Loading canvas from: {canvas_path}")

with open(canvas_path, 'r', encoding='utf-8') as f:
    canvas = json.load(f)

nodes = canvas['nodes']
edges = canvas.get('edges', [])
print(f"Found {len(nodes)} nodes, {len(edges)} existing edges")

# Extract turret info from file content
def parse_turret_metadata(filepath):
    """Extract caliber, mark, and mount type from turret file metadata"""
    try:
        full_path = Path(r'C:\Research') / filepath
        if not full_path.exists():
            return None

        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract designation from YAML front matter
        # Example: "designation: 5"/38 Mark 24 Single Mount"
        designation_match = re.search(r'designation:\s*(.+)', content)
        if not designation_match:
            return None

        designation = designation_match.group(1).strip()

        # Parse designation: caliber/length Mark ## MountType
        # Pattern 1: With gun length and "Mount" - e.g. "5"/38 Mark 24 Single Mount"
        # Pattern 2: Without gun length, duplicate "Mark Mark", ending with "Turret" - e.g. "5" Mark Mark 11 Single DP Turret"
        # Pattern 3: Without gun length, single "Mark" - e.g. "16" Mark 1 Triple Turret"

        # Try pattern 1 first (with gun length)
        pattern1 = r'(\d+(?:\.\d+)?)"(?:/(\d+))?\s+Mark\s+(\S+)\s+(Single|Twin|Triple|Quad)\s+(?:Mount|Turret)'
        match = re.match(pattern1, designation)

        if not match:
            # Try pattern 2 (duplicate "Mark Mark" without gun length)
            pattern2 = r'(\d+(?:\.\d+)?)"\s+Mark\s+Mark\s+(\S+)\s+(Single|Twin|Triple|Quad)\s'
            match2 = re.match(pattern2, designation)
            if match2:
                caliber, mark, mount = match2.groups()
                return {
                    'caliber': caliber,
                    'length': '',  # No gun length in these designations
                    'mark': mark,
                    'mount': mount,
                    'designation': designation,
                    'path': filepath
                }

        if not match:
            # Try pattern 3 (single "Mark" without gun length)
            pattern3 = r'(\d+(?:\.\d+)?)"\s+Mark\s+(\S+)\s+(Single|Twin|Triple|Quad)\s'
            match3 = re.match(pattern3, designation)
            if match3:
                caliber, mark, mount = match3.groups()
                # Skip "Mark" if it appears (shouldn't happen but just in case)
                if mark != 'Mark':
                    return {
                        'caliber': caliber,
                        'length': '',  # No gun length in these designations
                        'mark': mark,
                        'mount': mount,
                        'designation': designation,
                        'path': filepath
                    }

        if match:
            caliber, length, mark, mount = match.groups()
            return {
                'caliber': caliber,
                'length': length or '',  # May be None for some guns
                'mark': mark,
                'mount': mount,
                'designation': designation,
                'path': filepath
            }
    except Exception as e:
        pass

    return None

# Build turret database
print("\nBuilding turret database from file metadata...")
turrets = {}
turret_lookup = {}  # (caliber, length, mark, mount) -> node_id

# Count USA turret files first
usa_turret_count = sum(1 for n in nodes if n.get('type') == 'file' and 'Naval-Guns/Turrets/USA/' in n.get('file', ''))
print(f"Found {usa_turret_count} USA turret files to process...")

processed = 0
parsed = 0

for node in nodes:
    if node.get('type') == 'file' and 'file' in node:
        filepath = node['file']
        if 'Naval-Guns/Turrets/USA/' in filepath:
            processed += 1
            if processed % 100 == 0:
                print(f"  Processing {processed}/{usa_turret_count}... ({parsed} parsed successfully)")

            info = parse_turret_metadata(filepath)
            if info:
                parsed += 1
                caliber = info['caliber']
                length = info['length']
                mark = info['mark']
                mount = info['mount']

                # Create caliber/length key
                if length:
                    cal_key = f"{caliber}/{length}"
                else:
                    cal_key = caliber

                if cal_key not in turrets:
                    turrets[cal_key] = {}
                if mark not in turrets[cal_key]:
                    turrets[cal_key][mark] = {}

                turrets[cal_key][mark][mount] = {
                    'node_id': node['id'],
                    'path': filepath,
                    'info': info
                }

                # Add to lookup
                turret_lookup[(caliber, length, mark, mount)] = node['id']
            elif processed <= 5:
                # Debug first few failures
                print(f"    DEBUG: Failed to parse {filepath}")

print(f"\nProcessing complete: {processed} files processed, {parsed} turrets parsed successfully")
print(f"Found {len(turrets)} caliber/length variants")
for cal in sorted(turrets.keys(), key=lambda x: (float(x.split('/')[0]), x)):
    print(f"  {cal}\" - {len(turrets[cal])} marks, {sum(len(m) for m in turrets[cal].values())} total turrets")

# Define mark progressions for each caliber/length
# Some files have gun length (e.g., "5/38"), others don't (e.g., just "5")
# We'll define progressions for both formats where applicable

mark_progressions = {
    # 3" guns
    '3/50': ['10', '17', '18', '22', '26', '27', '33', '34'],
    '3': ['10', '17', '18', '22', '26', '27', '33', '34'],

    # 4" guns
    '4/50': ['7', '8', '9', '10', '12'],
    '4': ['7', '8', '9', '10', '12'],

    # 5" guns (multiple gun lengths)
    '5/51': ['7', '8', '9', '10', '11', '12', '13', '14', '15'],
    '5/25': ['10', '11', '13'],
    '5/38': ['12', '21', '22', '24', '28', '30', '32', '37', '39'],
    '5/54': ['16', '42', '45'],
    # Generic 5" for files without gun length - include all marks from all variants
    '5': ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '21', '22', '24', '28', '30', '32', '37', '39', '42', '45'],

    # 6" guns
    '6/47': ['2', '3', '4', '5', '6'],
    '6/53': ['11', '12', '13', '14', '15', '16', '17', '18'],
    '6': ['2', '3', '4', '5', '6', '11', '12', '13', '14', '15', '16', '17', '18'],

    # 8" guns
    '8/55': ['9', '11', '12', '13', '14', '15', '16', '71'],
    '8': ['9', '11', '12', '13', '14', '15', '16', '71'],

    # 10" guns
    '10': ['3'],

    # 12" guns
    '12/45': ['3', '4', '5'],
    '12/50': ['7', '8'],
    '12': ['3', '4', '5', '7', '8'],

    # 13" guns
    '13/45': ['1', '2'],
    '13': ['1', '2'],

    # 14" guns
    '14/45': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
    '14/50': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
    '14': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],

    # 16" guns
    '16/45': ['1', '2', '3', '5', '6'],
    '16/50': ['2', '3', '5', '6', '7', '8'],
    '16': ['1', '2', '2/3', '3', '5', '5/8', '6', '7', '8'],

    # 18" guns
    '18/48': ['1'],
    '18': ['1'],
}

# Mount types in progression order
mount_types = ['Single', 'Twin', 'Triple', 'Quad']

# Generate edges
edge_id_counter = 1
new_edges = []

def add_edge(from_node, to_node, label=""):
    global edge_id_counter
    edge = {
        'id': f'edge_{edge_id_counter:04d}',
        'fromNode': from_node,
        'toNode': to_node
    }
    if label:
        edge['label'] = label
    new_edges.append(edge)
    edge_id_counter += 1
    return edge

# Helper function to get node ID for a specific turret
def get_turret_node(cal_length, mark, mount):
    if cal_length in turrets and mark in turrets[cal_length] and mount in turrets[cal_length][mark]:
        return turrets[cal_length][mark][mount]['node_id']
    return None

# 1. Horizontal Mark Progression edges (for each mount type)
print("\n=== Creating Horizontal Mark Progression Edges ===")
horizontal_count = 0

for cal_length, marks in mark_progressions.items():
    for mount in mount_types:
        for i in range(len(marks) - 1):
            from_mark = marks[i]
            to_mark = marks[i + 1]
            from_node = get_turret_node(cal_length, from_mark, mount)
            to_node = get_turret_node(cal_length, to_mark, mount)
            if from_node and to_node:
                add_edge(from_node, to_node)
                horizontal_count += 1
                print(f"  {cal_length}\" Mk {from_mark} {mount} -> Mk {to_mark} {mount}")

print(f"Created {horizontal_count} horizontal mark progression edges")

# 2. Vertical Mount Type Upgrade edges (within each mark)
print("\n=== Creating Vertical Mount Type Upgrade Edges ===")
vertical_count = 0

for cal_length in turrets:
    for mark in turrets[cal_length]:
        available_mounts = list(turrets[cal_length][mark].keys())
        for i in range(len(mount_types) - 1):
            from_mount = mount_types[i]
            to_mount = mount_types[i + 1]
            if from_mount in available_mounts and to_mount in available_mounts:
                from_node = get_turret_node(cal_length, mark, from_mount)
                to_node = get_turret_node(cal_length, mark, to_mount)
                if from_node and to_node:
                    add_edge(from_node, to_node)
                    vertical_count += 1
                    print(f"  {cal_length}\" Mk {mark}: {from_mount} -> {to_mount}")

print(f"Created {vertical_count} vertical mount upgrade edges")

# 3. Cross-Caliber Strategic Progressions
print("\n=== Creating Cross-Caliber Strategic Progression Edges ===")
strategic_count = 0

# Format: (from_cal_length, from_mark, from_mount, to_cal_length, to_mark, to_mount, label)
# Updated to use generic caliber keys (without gun length) where specific variants aren't available
strategic_paths = [
    # Destroyer Evolution
    ('4', '12', 'Twin', '5', '7', 'Twin', 'Early DD upgrade'),
    ('5', '15', 'Twin', '5', '12', 'Twin', 'Transition to DP'),
    ('5', '39', 'Twin', '5', '16', 'Twin', 'WWII to Cold War'),
    ('5', '42', 'Single', '5', '45', 'Single', 'Modern automation'),

    # Cruiser Branch
    ('5', '15', 'Twin', '6', '6', 'Twin', 'Light cruiser branch'),
    ('6', '6', 'Triple', '6', '11', 'Triple', 'Treaty cruiser upgrade'),
    ('6', '16', 'Triple', '8', '9', 'Triple', 'Heavy cruiser branch'),

    # Battleship Branch
    ('12', '8', 'Triple', '14', '1', 'Triple', 'Dreadnought evolution'),
    ('14', '7', 'Triple', '16', '1', 'Triple', 'Super-battleship upgrade'),
    ('16', '3', 'Triple', '16', '5', 'Triple', 'Fast battleship pinnacle'),
    ('16', '7', 'Triple', '18', '1', 'Triple', 'Ultimate concept'),

    # Additional secondary battery progressions
    ('3', '34', 'Twin', '4', '7', 'Twin', 'Light AA upgrade'),
    ('4', '12', 'Twin', '5', '7', 'Twin', 'Secondary battery upgrade'),

    # Heavy gun progressions
    ('8', '16', 'Triple', '12', '3', 'Triple', 'Pre-dreadnought to dreadnought'),
    ('12', '5', 'Twin', '13', '1', 'Twin', 'Experimental heavy gun'),
    ('13', '2', 'Twin', '14', '1', 'Twin', 'Standard battleship gun'),
]

for path in strategic_paths:
    from_cal, from_mark, from_mount, to_cal, to_mark, to_mount, label = path
    from_node = get_turret_node(from_cal, from_mark, from_mount)
    to_node = get_turret_node(to_cal, to_mark, to_mount)
    if from_node and to_node:
        add_edge(from_node, to_node, label)
        strategic_count += 1
        print(f"  {from_cal}\" Mk {from_mark} {from_mount} -> {to_cal}\" Mk {to_mark} {to_mount} ({label})")
    else:
        print(f"  MISSING: {from_cal}\" Mk {from_mark} {from_mount} -> {to_cal}\" Mk {to_mark} {to_mount}")

print(f"Created {strategic_count} strategic cross-caliber edges")

# Add all new edges to canvas
canvas['edges'] = edges + new_edges

# Save updated canvas
print(f"\nSaving updated canvas...")
with open(canvas_path, 'w', encoding='utf-8') as f:
    json.dump(canvas, f, indent='\t')

print(f"\n=== SUMMARY ===")
print(f"Total edges created: {len(new_edges)}")
print(f"  - Horizontal mark progressions: {horizontal_count}")
print(f"  - Vertical mount upgrades: {vertical_count}")
print(f"  - Strategic cross-caliber: {strategic_count}")
print(f"\nCanvas updated successfully!")
