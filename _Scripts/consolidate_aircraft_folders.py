#!/usr/bin/env python3
"""Consolidate aircraft folders from 65 to 19 folders"""

import subprocess
import sys
from pathlib import Path
from collections import defaultdict

# Mapping of old folder names to new consolidated folder names
CONSOLIDATION_MAP = {
    # Land Aircraft
    'Land-Fighter': 'Land-Fighter',
    'Land-Air-Superiority': 'Land-Fighter',
    'Land-Interceptor': 'Land-Fighter',
    'Land-Jet-Fighter': 'Land-Fighter',
    'Land-Export-Fighter': 'Land-Fighter',
    'Land-Stealth-Fighter': 'Land-Fighter',

    'Land-Bomber': 'Land-Bomber',
    'Land-Dive-Bomber': 'Land-Bomber',
    'Land-Heavy-Bomber': 'Land-Bomber',
    'Land-Strategic-Bomber': 'Land-Bomber',
    'Land-Supersonic-Bomber': 'Land-Bomber',
    'Land-Stealth-Bomber': 'Land-Bomber',

    'Land-Strike': 'Land-Strike',
    'Land-Close-Air-Support': 'Land-Strike',
    'Land-Multi-Role': 'Land-Strike',
    'Land-Stealth-Multi-Role': 'Land-Strike',

    'Land-Attack-Helo': 'Land-Helicopter',
    'Land-Transport-Helo': 'Land-Helicopter',
    'Land-Heavy-Transport-Helo': 'Land-Helicopter',
    'Land-Utility-Helo': 'Land-Helicopter',
    'Land-Gunship': 'Land-Helicopter',

    'Land-Transport': 'Land-Transport',
    'Land-Strategic-Transport': 'Land-Transport',
    'Land-Tanker': 'Land-Transport',

    'Land-Reconnaissance': 'Land-Reconnaissance',
    'Land-Scout': 'Land-Reconnaissance',
    'Land-EW': 'Land-Reconnaissance',
    'Land-Patrol': 'Land-Reconnaissance',

    'Land-Trainer': 'Land-Trainer',

    'Land-UAV-Attack': 'Land-UAV',
    'Land-UAV-Multi-Role': 'Land-UAV',
    'Land-UAV-Recon': 'Land-UAV',

    'Land-V': 'Land-VTOL',

    # Naval Aircraft
    'Naval-Fighter': 'Naval-Fighter',
    'Naval-All-Weather-Fighter': 'Naval-Fighter',
    'Naval-Interceptor': 'Naval-Fighter',
    'Naval-Jet-Fighter': 'Naval-Fighter',
    'Naval-VSTOL-Fighter': 'Naval-Fighter',
    'Naval-Stealth-Fighter': 'Naval-Fighter',

    'Naval-Dive-Bomber': 'Naval-Bomber',
    'Naval-Torpedo-Bomber': 'Naval-Bomber',
    'Naval-Scout-Bomber': 'Naval-Bomber',

    'Naval-Strike': 'Naval-Strike',
    'Naval-Strike-Fighter': 'Naval-Strike',
    'Naval-Attack': 'Naval-Strike',
    'Naval-Low-Level-Strike': 'Naval-Strike',
    'Naval-Multi-Role': 'Naval-Strike',

    'Naval-ASW': 'Naval-ASW',
    'Naval-ASW-Flying-Boat': 'Naval-ASW',
    'Naval-Maritime-Patrol': 'Naval-ASW',
    'Naval-Patrol': 'Naval-ASW',

    'Naval-ASW-Helo': 'Naval-Helicopter',
    'Naval-Multi-Role-Helo': 'Naval-Helicopter',
    'Naval-Utility-Helo': 'Naval-Helicopter',
    'Naval-Observation-Helo': 'Naval-Helicopter',

    'Naval-AEW': 'Naval-AEW',
    'Naval-AEW-Helo': 'Naval-AEW',

    'Naval-Reconnaissance': 'Naval-Reconnaissance',
    'Naval-Recon': 'Naval-Reconnaissance',
    'Naval-Scout': 'Naval-Reconnaissance',
    'Naval-Fighter-Reconnaissance': 'Naval-Reconnaissance',
    'Naval-EW': 'Naval-Reconnaissance',

    'Naval-SAR-Flying-Boat': 'Naval-SAR',

    'Naval-UAV-Tanker': 'Naval-UAV',

    'Naval-V': 'Naval-VTOL',
}

def run_git_mv(old_path, new_path):
    """Execute git mv command"""
    try:
        cmd = ['git', 'mv', str(old_path), str(new_path)]
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=old_path.parent.parent.parent)
        return result.returncode == 0, result.stderr
    except Exception as e:
        return False, str(e)

def main():
    root = Path.cwd()
    aircraft_root = root / 'Aircraft'

    if not aircraft_root.exists():
        print("[ERROR] Aircraft folder not found")
        return

    print("=" * 70)
    print("CONSOLIDATE AIRCRAFT FOLDERS")
    print("=" * 70)
    print(f"\nReducing from 65 folders to 19 consolidated folders")
    print(f"Using 'git mv' to preserve file history\n")

    # Scan all aircraft files and group by nation and old folder
    moves_needed = defaultdict(list)

    for nation_dir in aircraft_root.iterdir():
        if not nation_dir.is_dir():
            continue

        for type_dir in nation_dir.iterdir():
            if not type_dir.is_dir():
                continue

            old_folder = type_dir.name

            # Check if this folder needs consolidation
            if old_folder in CONSOLIDATION_MAP:
                new_folder = CONSOLIDATION_MAP[old_folder]

                # Only process if folder is changing
                if old_folder != new_folder:
                    # Get all markdown files in this folder
                    for md_file in type_dir.glob('*.md'):
                        old_path = md_file.relative_to(root)
                        new_dir = nation_dir / new_folder
                        new_path = new_dir / md_file.name
                        new_path_rel = new_path.relative_to(root)

                        moves_needed[(nation_dir.name, old_folder, new_folder)].append((old_path, new_path_rel, new_dir))

    # Summary of moves
    print(f"Total moves needed: {sum(len(files) for files in moves_needed.values())} files")
    print(f"Folders being consolidated: {len(moves_needed)} folder groups\n")

    # Show sample
    print("Sample consolidations:")
    for i, ((nation, old, new), files) in enumerate(list(moves_needed.items())[:10]):
        print(f"  {nation}/{old} -> {nation}/{new} ({len(files)} files)")

    if len(moves_needed) > 10:
        print(f"  ... and {len(moves_needed) - 10} more folder consolidations")

    # Ask for confirmation (skip if --yes flag provided)
    if '--yes' not in sys.argv:
        response = input(f"\nProceed with consolidation? (yes/no): ")
        if response.lower() != 'yes':
            print("[CANCELLED] No changes made")
            return
    else:
        print("\n[AUTO-CONFIRMED] Proceeding with consolidation...")

    # Execute moves
    print("\n" + "=" * 70)
    print("EXECUTING MOVES")
    print("=" * 70)

    moved_count = 0
    error_count = 0

    for (nation, old_folder, new_folder), files in moves_needed.items():
        print(f"\n[{nation}] {old_folder} -> {new_folder} ({len(files)} files)")

        # Create destination directory if it doesn't exist
        dest_dir = files[0][2]  # new_dir from first file
        if not dest_dir.exists():
            dest_dir.mkdir(parents=True, exist_ok=True)
            print(f"  [CREATED] {dest_dir.relative_to(root)}")

        # Move files
        for old_path, new_path, _ in files:
            success, error = run_git_mv(root / old_path, root / new_path)
            if success:
                moved_count += 1
                if moved_count <= 20:
                    print(f"  [OK] {old_path.name}")
            else:
                error_count += 1
                print(f"  [ERROR] {old_path}: {error}")

        if len(files) > 20:
            print(f"  ... moved {len(files)} files")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Successfully moved: {moved_count} files")
    print(f"Errors: {error_count} files")

    if error_count == 0:
        print("\n[SUCCESS] All files consolidated successfully!")
        print("\nNext steps:")
        print("  1. Review changes with 'git status'")
        print("  2. Commit changes")
    else:
        print(f"\n[WARNING] {error_count} errors occurred during consolidation")

if __name__ == '__main__':
    main()
