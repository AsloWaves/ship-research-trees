import json
import re
from pathlib import Path

def parse_turret_info_from_file(file_path):
    """Extract caliber and mount type from turret file path."""
    # Example: Weapons/Naval-Weapons/Naval-Guns/Turrets/USA/1000-5inch-Triple.md
    filename = Path(file_path).stem

    # Match pattern: number-caliber-mount
    # e.g., "1000-5inch-Triple" or "100-5inch-Twin"
    pattern = r'^\d+-([^-]+)-(\w+)$'
    match = re.match(pattern, filename)

    if not match:
        return None

    caliber = match.group(1)  # e.g., "3inch", "5inch", "14inch"
    mount = match.group(2)    # e.g., "Single", "Twin", "Triple", "Quad"

    return {
        'caliber': caliber,
        'mount': mount,
        'filename': filename,
        'filepath': file_path
    }

def get_position(node):
    """Get x, y coordinates of a node."""
    return node.get('x', 0), node.get('y', 0)

def is_vertical_edge(from_node, to_node, from_info, to_info):
    """Check if edge is vertical based on coordinates and turret info."""
    if not from_info or not to_info:
        return False

    # Same caliber check
    if from_info['caliber'] != to_info['caliber']:
        return False

    from_x, from_y = get_position(from_node)
    to_x, to_y = get_position(to_node)

    # Vertical edge: Y coordinate changes significantly, X stays roughly the same
    # Allow some X variation (within 100 pixels) for alignment tolerance
    x_diff = abs(to_x - from_x)
    y_diff = abs(to_y - from_y)

    # Vertical if significant Y change and minimal X change
    if y_diff > 300 and x_diff < 150:
        return True

    return False

def is_horizontal_edge(from_node, to_node, from_info, to_info):
    """Check if edge is horizontal based on coordinates."""
    if not from_info or not to_info:
        return False

    from_x, from_y = get_position(from_node)
    to_x, to_y = get_position(to_node)

    # Horizontal edge: X coordinate changes significantly, Y stays roughly the same
    # Allow some Y variation (within 100 pixels) for alignment tolerance
    x_diff = abs(to_x - from_x)
    y_diff = abs(to_y - from_y)

    # Horizontal if significant X change and minimal Y change
    if x_diff > 300 and y_diff < 150:
        return True

    return False

def is_cross_caliber_edge(from_info, to_info):
    """Check if edge connects different calibers (cross-caliber strategic edge)."""
    if not from_info or not to_info:
        return False

    return from_info['caliber'] != to_info['caliber']

def should_keep_edge(edge, nodes_dict):
    """Determine if an edge should be kept based on the filtering rules."""
    from_id = edge.get('fromNode')
    to_id = edge.get('toNode')

    if not from_id or not to_id:
        return False

    # Get node information
    from_node = nodes_dict.get(from_id)
    to_node = nodes_dict.get(to_id)

    if not from_node or not to_node:
        return False

    # Only process turret nodes (file type with turret path)
    from_file = from_node.get('file', '')
    to_file = to_node.get('file', '')

    if 'Turrets' not in from_file or 'Turrets' not in to_file:
        # Keep non-turret edges as-is
        return True

    # Parse turret information
    from_info = parse_turret_info_from_file(from_file)
    to_info = parse_turret_info_from_file(to_file)

    if not from_info or not to_info:
        return True  # Keep edges we can't parse

    # Rule 4: Remove cross-caliber strategic edges
    if is_cross_caliber_edge(from_info, to_info):
        return False

    # Check if it's a vertical or horizontal edge
    is_vert = is_vertical_edge(from_node, to_node, from_info, to_info)
    is_horiz = is_horizontal_edge(from_node, to_node, from_info, to_info)

    # Rule 1: Keep all vertical mount upgrade edges
    if is_vert:
        return True

    # Rule 2 & 3: For horizontal edges, only keep if BOTH are Single mount
    if is_horiz:
        if from_info['mount'] == 'Single' and to_info['mount'] == 'Single':
            return True
        else:
            return False

    # Keep anything else we're not sure about
    return True

def filter_canvas_edges(input_file, output_file):
    """Filter edges in the canvas file according to the specified rules."""
    print(f"Reading canvas file: {input_file}")

    with open(input_file, 'r', encoding='utf-8') as f:
        canvas_data = json.load(f)

    # Create a lookup dictionary for nodes
    nodes_dict = {node['id']: node for node in canvas_data.get('nodes', [])}
    print(f"Total nodes: {len(nodes_dict)}")

    # Get original edges
    original_edges = canvas_data.get('edges', [])
    print(f"Original edges: {len(original_edges)}")

    # Filter edges
    filtered_edges = []
    removed_edges = []
    vertical_count = 0
    horizontal_single_count = 0
    horizontal_other_count = 0
    cross_caliber_count = 0
    non_turret_count = 0

    for edge in original_edges:
        from_id = edge.get('fromNode')
        to_id = edge.get('toNode')

        from_node = nodes_dict.get(from_id)
        to_node = nodes_dict.get(to_id)

        if not from_node or not to_node:
            continue

        from_file = from_node.get('file', '')
        to_file = to_node.get('file', '')

        # Check if both are turret nodes
        if 'Turrets' in from_file and 'Turrets' in to_file:
            from_info = parse_turret_info_from_file(from_file)
            to_info = parse_turret_info_from_file(to_file)

            if from_info and to_info:
                # Check for cross-caliber
                if is_cross_caliber_edge(from_info, to_info):
                    cross_caliber_count += 1
                    removed_edges.append({
                        'from': from_info['filename'],
                        'to': to_info['filename'],
                        'type': 'cross-caliber'
                    })
                    continue

                is_vert = is_vertical_edge(from_node, to_node, from_info, to_info)
                is_horiz = is_horizontal_edge(from_node, to_node, from_info, to_info)

                if is_vert:
                    filtered_edges.append(edge)
                    vertical_count += 1
                elif is_horiz:
                    if from_info['mount'] == 'Single' and to_info['mount'] == 'Single':
                        filtered_edges.append(edge)
                        horizontal_single_count += 1
                    else:
                        horizontal_other_count += 1
                        removed_edges.append({
                            'from': from_info['filename'],
                            'to': to_info['filename'],
                            'type': f"horizontal-{from_info['mount']}"
                        })
                else:
                    # Edge we can't classify - keep it
                    filtered_edges.append(edge)
            else:
                # Can't parse - keep it
                filtered_edges.append(edge)
        else:
            # Keep non-turret edges
            filtered_edges.append(edge)
            non_turret_count += 1

    # Update canvas with filtered edges
    canvas_data['edges'] = filtered_edges

    # Write back to file
    print(f"\nWriting filtered canvas to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(canvas_data, f, indent='\t')

    print(f"\n=== Edge Filtering Summary ===")
    print(f"Original edges: {len(original_edges)}")
    print(f"Vertical mount upgrade edges (kept): {vertical_count}")
    print(f"Horizontal Single mark progression (kept): {horizontal_single_count}")
    print(f"Horizontal other mount removed: {horizontal_other_count}")
    print(f"Cross-caliber edges removed: {cross_caliber_count}")
    print(f"Non-turret edges (kept): {non_turret_count}")
    print(f"Total kept: {len(filtered_edges)}")
    print(f"Total removed: {len(removed_edges)}")

    # Show some examples of removed edges
    if removed_edges:
        print(f"\n=== Sample of Removed Edges ===")
        for i, edge_info in enumerate(removed_edges[:10]):
            print(f"  [{edge_info['type']}] {edge_info['from']} -> {edge_info['to']}")
        if len(removed_edges) > 10:
            print(f"  ... and {len(removed_edges) - 10} more")

    print(f"\nFiltering complete!")

if __name__ == "__main__":
    canvas_file = r"C:\Research\Weapons\Naval-Weapons\Naval-Weapons Tree.canvas"
    filter_canvas_edges(canvas_file, canvas_file)
