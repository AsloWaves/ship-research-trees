#!/usr/bin/env python3
"""
Fix both canvas paths to include Ships/ prefix for Obsidian
"""

import json
import os

def fix_canvas(canvas_path, prefix_to_add):
    """Fix paths in a canvas by adding the Ships/ prefix"""
    print(f"\nProcessing: {canvas_path}")

    with open(canvas_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"Loaded {len(data['nodes'])} nodes and {len(data['edges'])} edges")

    replacements_made = 0

    # Fix file paths in nodes
    for node in data['nodes']:
        if node.get('type') == 'file' and 'file' in node:
            original_path = node['file']

            # Only fix if it doesn't already start with Ships/
            if not original_path.startswith('Ships/'):
                new_path = f"Ships/{original_path}"
                node['file'] = new_path
                replacements_made += 1
                if replacements_made <= 3:  # Show first 3 examples
                    print(f"  Fixed: {original_path} -> {new_path}")

    print(f"Total replacements made: {replacements_made}")

    # Save the corrected canvas
    with open(canvas_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1)

    print(f"Saved corrected canvas")

    # Verify a few paths exist
    print("Verifying sample paths:")
    sample_nodes = [n for n in data['nodes'] if n.get('type') == 'file'][:3]
    for node in sample_nodes:
        file_path = f"C:/Research/{node['file']}"
        exists = os.path.exists(file_path)
        status = "[OK]" if exists else "[ERROR]"
        print(f"  {status}: {node['file']}")

    return replacements_made

# Fix both canvases
gb_canvas = "C:/Research/Ships/Great-Britain/Great-Britain Ship Tree.canvas"
usa_canvas = "C:/Research/Ships/USA/USA Ship Tree.canvas"

gb_fixes = fix_canvas(gb_canvas, "Ships/")
usa_fixes = fix_canvas(usa_canvas, "Ships/")

print(f"\n{'='*60}")
print("SUMMARY:")
print(f"  Great-Britain canvas: {gb_fixes} paths fixed")
print(f"  USA canvas: {usa_fixes} paths fixed")
print(f"{'='*60}")
print("\nAll canvas paths now correctly prefixed with 'Ships/'")
