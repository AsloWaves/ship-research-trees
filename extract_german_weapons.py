import json
import os

# Read the source canvas file
with open(r'D:\Research\Weapons\Naval-Weapons\Naval-Weapons Tree.canvas', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract nodes
nodes = data.get('nodes', [])
edges = data.get('edges', [])

# Categories for German weapons
categories = {
    'Turrets': [],
    'Torpedoes': [],
    'Missiles': [],
    'Bombs': []
}

# Map weapon types to categories
type_mapping = {
    'Naval-Guns': 'Turrets',
    'Torpedoes': 'Torpedoes',
    'Missiles': 'Missiles',
    'Bombs': 'Bombs'
}

# Extract German weapon nodes
german_node_ids = set()
for node in nodes:
    if node.get('type') == 'file':
        file_path = node.get('file', '')
        # Check if it's a German weapon
        if '/German/' in file_path or '/Germany/' in file_path:
            # Determine category
            for weapon_type, category in type_mapping.items():
                if weapon_type in file_path:
                    categories[category].append(node)
                    german_node_ids.add(node['id'])
                    break

# Function to create canvas with repositioned nodes
def create_canvas(weapon_type, nodes_list):
    if not nodes_list:
        return None

    # Sort nodes by original x position to maintain order
    nodes_list.sort(key=lambda n: n.get('x', 0))

    # Create new nodes with repositioned coordinates
    new_nodes = []
    x_pos = 0
    y_pos = 0
    spacing = 450  # 400px card + 50px gap

    for i, node in enumerate(nodes_list):
        new_node = node.copy()
        new_node['x'] = x_pos
        new_node['y'] = y_pos
        new_nodes.append(new_node)
        x_pos += spacing

    # Create canvas structure
    canvas = {
        "nodes": new_nodes,
        "edges": []
    }

    return canvas

# Create output directory
output_dir = r'D:\Research\Canvases'
os.makedirs(os.path.join(output_dir, 'Naval-Turrets'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'Naval-Torpedoes'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'Naval-Missiles'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'Naval-Bombs'), exist_ok=True)

# Output paths
output_files = {
    'Turrets': r'D:\Research\Canvases\Naval-Turrets\German-Naval-Turrets-Tree.canvas',
    'Torpedoes': r'D:\Research\Canvases\Naval-Torpedoes\German-Naval-Torpedoes-Tree.canvas',
    'Missiles': r'D:\Research\Canvases\Naval-Missiles\German-Naval-Missiles-Tree.canvas',
    'Bombs': r'D:\Research\Canvases\Naval-Bombs\German-Naval-Bombs-Tree.canvas'
}

# Create and save canvas files
results = {}
for category, nodes_list in categories.items():
    canvas = create_canvas(category, nodes_list)
    if canvas:
        output_path = output_files[category]
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(canvas, f, indent='\t', ensure_ascii=False)
        results[category] = len(nodes_list)
        print(f'{category}: {len(nodes_list)} weapons extracted')
    else:
        results[category] = 0
        print(f'{category}: No weapons found')

print(f'\nTotal German weapons extracted: {sum(results.values())}')
print(f'\nCanvas files created in:')
for category, path in output_files.items():
    if results[category] > 0:
        print(f'  {path}')
