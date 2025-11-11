#!/usr/bin/env python3
"""
Fix USA Ship Tree Canvas paths to match actual directory structure
"""

import json
import re

# Load the USA canvas
canvas_path = "C:/Research/Ships/USA/USA Ship Tree.canvas"
print(f"Loading USA canvas from: {canvas_path}")

with open(canvas_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data['nodes'])} nodes and {len(data['edges'])} edges")

# Count replacements
replacements_made = 0

# Fix file paths in nodes
for node in data['nodes']:
    if node.get('type') == 'file' and 'file' in node:
        original_path = node['file']

        # Replace "USA/USA [Category]/" with "USA/[Category]/"
        new_path = original_path
        new_path = new_path.replace('USA/USA Cruisers/', 'USA/Cruisers/')
        new_path = new_path.replace('USA/USA Battleships/', 'USA/Battleships/')
        new_path = new_path.replace('USA/USA Carriers/', 'USA/Carriers/')
        new_path = new_path.replace('USA/USA Destroyers/', 'USA/Destroyers/')
        new_path = new_path.replace('USA/USA Submarines/', 'USA/Submarines/')
        new_path = new_path.replace('USA/USA Transports Amphibious/', 'USA/Transports-Amphibious/')

        if new_path != original_path:
            node['file'] = new_path
            replacements_made += 1
            if replacements_made <= 3:  # Show first 3 examples
                print(f"  Fixed: {original_path} -> {new_path}")

print(f"\nTotal replacements made: {replacements_made}")

# Save the corrected canvas
with open(canvas_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1)

print(f"Saved corrected canvas to: {canvas_path}")

# Verify a few paths exist
print("\nVerifying sample paths:")
import os
sample_nodes = [n for n in data['nodes'] if n.get('type') == 'file'][:5]
for node in sample_nodes:
    file_path = f"C:/Research/Ships/{node['file']}"
    exists = os.path.exists(file_path)
    status = "✓ EXISTS" if exists else "✗ NOT FOUND"
    print(f"  {status}: {node['file']}")

print("\n✓ USA canvas paths fixed!")
