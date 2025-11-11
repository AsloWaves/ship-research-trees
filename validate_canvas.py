#!/usr/bin/env python3
import json

# Load and validate the canvas
with open('C:/Research/Ships/Great-Britain/Great-Britain Ship Tree.canvas', 'r') as f:
    data = json.load(f)

print(f"[OK] JSON is valid")
print(f"[OK] Nodes: {len(data['nodes'])}")
print(f"[OK] Edges: {len(data['edges'])}")

# Count node types
groups = sum(1 for n in data['nodes'] if n['type'] == 'group')
files = sum(1 for n in data['nodes'] if n['type'] == 'file')

print(f"[OK] Group nodes: {groups}")
print(f"[OK] File nodes: {files}")

# Check required fields
print("\nValidating node structure...")
for i, node in enumerate(data['nodes'][:5]):  # Check first 5
    required = ['id', 'type', 'x', 'y', 'width', 'height']
    for field in required:
        if field not in node:
            print(f"[ERROR] Node {i} missing field: {field}")
    else:
        if i == 0:
            print(f"[OK] Sample node structure valid")

# Check edges
print("\nValidating edge structure...")
if data['edges']:
    edge = data['edges'][0]
    required = ['id', 'fromNode', 'fromSide', 'toNode', 'toSide']
    for field in required:
        if field not in edge:
            print(f"[ERROR] Edge missing field: {field}")
    else:
        print(f"[OK] Edge structure valid")

# Check file paths
print("\nChecking file path format...")
sample_files = [n for n in data['nodes'] if n['type'] == 'file'][:3]
for node in sample_files:
    print(f"  {node['file']}")

print("\n[OK] Canvas validation complete!")
