import json
import re
from pathlib import Path
from collections import defaultdict

def extract_filenames_from_canvas(canvas_path):
    """Extract all .md filenames referenced in a canvas file"""
    with open(canvas_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all file references in the canvas
    pattern = r'"file":"Ships/[^"]+\.md"'
    matches = re.findall(pattern, content)

    filenames = set()
    for match in matches:
        # Extract just the filename from the full path
        filepath = match.split('"file":"')[1].rstrip('"')
        filename = filepath.split('/')[-1]
        filenames.add(filename)

    return sorted(filenames)

def get_all_md_files(base_path):
    """Get all .md files in all subdirectories"""
    base = Path(base_path)
    files = defaultdict(list)

    # Define the subdirectories to check
    subdirs = ['Battleships', 'Carriers', 'Cruisers', 'Destroyers', 'Submarines', 'Transports-Amphibious']

    for subdir in subdirs:
        subdir_path = base / subdir
        if subdir_path.exists():
            for md_file in subdir_path.glob('*.md'):
                files[subdir].append(md_file.name)

    return files

def verify_nation(nation_name, ships_path, canvas_path, output_file):
    """Verify which files are missing from the canvas for a nation"""
    output_file.write(f"\n{'='*80}\n")
    output_file.write(f"VERIFICATION REPORT: {nation_name}\n")
    output_file.write(f"{'='*80}\n")

    # Get all .md files in folders
    folder_files = get_all_md_files(ships_path)
    all_folder_files = set()
    for subdir, files in folder_files.items():
        all_folder_files.update(files)

    # Get all filenames in canvas
    canvas_files = set(extract_filenames_from_canvas(canvas_path))

    # Find missing files
    missing_files = sorted(all_folder_files - canvas_files)

    # Print statistics
    output_file.write(f"\nTotal .md files in folders: {len(all_folder_files)}\n")
    output_file.write(f"Total unique filenames in canvas: {len(canvas_files)}\n")
    output_file.write(f"Missing from canvas: {len(missing_files)}\n")

    # Print missing files by category
    if missing_files:
        output_file.write(f"\n{'-'*80}\n")
        output_file.write("MISSING FILES:\n")
        output_file.write(f"{'-'*80}\n")

        for subdir in ['Battleships', 'Carriers', 'Cruisers', 'Destroyers', 'Submarines', 'Transports-Amphibious']:
            subdir_missing = [f for f in missing_files if f in folder_files.get(subdir, [])]
            if subdir_missing:
                output_file.write(f"\n{subdir}:\n")
                for filename in subdir_missing:
                    full_path = f"{ships_path}\\{subdir}\\{filename}"
                    output_file.write(f"  - {filename}\n")
                    output_file.write(f"    Location: {full_path}\n")
    else:
        output_file.write("\nAll files are present in the canvas!\n")

    # Check for files in canvas but not in folders (should only be Alaska-Class for USA)
    extra_in_canvas = sorted(canvas_files - all_folder_files)
    if extra_in_canvas:
        output_file.write(f"\n{'-'*80}\n")
        output_file.write("FILES IN CANVAS BUT NOT IN FOLDERS:\n")
        output_file.write(f"{'-'*80}\n")
        for filename in extra_in_canvas:
            output_file.write(f"  - {filename}\n")

# Main execution
nations = [
    ("USA", r"C:\Research\Ships\USA", r"C:\Research\Ships\USA\USA Ship Tree.canvas"),
    ("Great-Britain", r"C:\Research\Ships\Great-Britain", r"C:\Research\Ships\Great-Britain\Great-Britain Ship Tree.canvas"),
    ("Japan", r"C:\Research\Ships\Japan", r"C:\Research\Ships\Japan\Japan Ship Tree.canvas"),
    ("Germany", r"C:\Research\Ships\Germany", r"C:\Research\Ships\Germany\Germany Ship Tree.canvas")
]

output_file_path = r"C:\Research\canvas_verification_report.txt"

with open(output_file_path, 'w', encoding='utf-8') as output:
    output.write("COMPREHENSIVE CANVAS FILE VERIFICATION\n")
    output.write("=" * 80 + "\n")
    output.write("Checking which .md files are missing from canvas files\n")
    output.write("=" * 80 + "\n")

    for nation_name, ships_path, canvas_path in nations:
        verify_nation(nation_name, ships_path, canvas_path, output)

    output.write(f"\n{'='*80}\n")
    output.write("VERIFICATION COMPLETE\n")
    output.write(f"{'='*80}\n")

print(f"Verification complete! Report saved to: {output_file_path}")
