#!/usr/bin/env python3
"""
Analyze markdown file distribution by nation across all categories.
"""

import os
from collections import defaultdict

def count_files_by_nation(base_path, nations):
    """Count markdown files for each nation in a directory."""
    counts = {}
    for nation in nations:
        nation_path = os.path.join(base_path, nation)
        if os.path.exists(nation_path):
            count = sum(1 for root, dirs, files in os.walk(nation_path)
                       for f in files if f.endswith('.md'))
            counts[nation] = count
        else:
            # Try alternative naming (space vs hyphen)
            alt_nation = nation.replace(' ', '-') if ' ' in nation else nation.replace('-', ' ')
            alt_path = os.path.join(base_path, alt_nation)
            if os.path.exists(alt_path):
                count = sum(1 for root, dirs, files in os.walk(alt_path)
                           for f in files if f.endswith('.md'))
                counts[nation] = count
            else:
                counts[nation] = 0
    return counts

def main():
    base = r"D:\Research"

    # Define nations to check
    ship_nations = ['USA', 'Great Britain', 'Japan', 'Germany']
    aircraft_nations = ['USA', 'Great Britain', 'Japan', 'Germany']
    weapon_nations = ['USA', 'British', 'German', 'Japanese', 'French', 'Soviet', 'Russian', 'Chinese']

    print("=" * 70)
    print("NAVAL WARFARE RESEARCH DATABASE - NATION ANALYSIS")
    print("=" * 70)

    # Ships
    print("\nSHIPS (by Nation)")
    print("-" * 70)
    ships_path = os.path.join(base, "Ships")
    ship_counts = count_files_by_nation(ships_path, ship_nations)
    total_ships = sum(ship_counts.values())
    for nation, count in sorted(ship_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total_ships * 100) if total_ships > 0 else 0
        print(f"  {nation:20s}: {count:4d} ({pct:5.1f}%)")
    print(f"  {'TOTAL':20s}: {total_ships:4d}")

    # Carrier Aircraft (from aircraft.db)
    print("\nCARRIER AIRCRAFT (from aircraft.db)")
    print("-" * 70)
    aircraft_path = os.path.join(base, "Aircraft")
    aircraft_counts = count_files_by_nation(aircraft_path, aircraft_nations)
    total_aircraft = sum(aircraft_counts.values())
    for nation, count in sorted(aircraft_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total_aircraft * 100) if total_aircraft > 0 else 0
        print(f"  {nation:20s}: {count:4d} ({pct:5.1f}%)")
    print(f"  {'TOTAL':20s}: {total_aircraft:4d}")

    # Naval Aircraft
    print("\nNAVAL AIRCRAFT (carrier-based)")
    print("-" * 70)
    naval_aircraft_path = os.path.join(base, "Aircraft", "Naval")
    if os.path.exists(naval_aircraft_path):
        naval_aircraft_count = sum(1 for f in os.listdir(naval_aircraft_path) if f.endswith('.md'))
        print(f"  {'All Nations':20s}: {naval_aircraft_count:4d}")

    # Ground Aircraft
    print("\nGROUND AIRCRAFT (land-based)")
    print("-" * 70)
    ground_aircraft_path = os.path.join(base, "Aircraft", "Ground")
    if os.path.exists(ground_aircraft_path):
        ground_aircraft_count = sum(1 for f in os.listdir(ground_aircraft_path) if f.endswith('.md'))
        print(f"  {'All Nations':20s}: {ground_aircraft_count:4d}")

    # Aircraft Weapons
    print("\nAIRCRAFT WEAPONS")
    print("-" * 70)
    weapons_base = os.path.join(base, "Weapons", "Aircraft-Weapons")
    categories = ['Bombs', 'Missiles', 'Rockets', 'Torpedoes', 'Depth-Charges', 'Mines', 'Practice-Munitions']
    for category in categories:
        cat_path = os.path.join(weapons_base, category)
        if os.path.exists(cat_path):
            count = sum(1 for f in os.listdir(cat_path) if f.endswith('.md'))
            print(f"  {category:20s}: {count:4d}")

    # Naval Guns
    print("\nNAVAL GUNS & AMMUNITION")
    print("-" * 70)
    guns_base = os.path.join(base, "Weapons", "Naval-Guns")
    gun_types = [('Guns', 'USA'), ('Ammunition', 'USA'), ('Turrets', 'USA')]
    for gun_type, nation in gun_types:
        type_path = os.path.join(guns_base, gun_type, nation)
        if os.path.exists(type_path):
            count = sum(1 for f in os.listdir(type_path) if f.endswith('.md'))
            print(f"  {gun_type:20s}: {count:4d} (USA only)")

    # Torpedoes
    print("\nNAVAL TORPEDOES")
    print("-" * 70)
    torpedoes_path = os.path.join(base, "Weapons", "Torpedoes")
    torpedo_counts = count_files_by_nation(torpedoes_path, ['USA', 'British', 'German', 'Japanese'])
    total_torpedoes = sum(torpedo_counts.values())
    for nation, count in sorted(torpedo_counts.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total_torpedoes * 100) if total_torpedoes > 0 else 0
        print(f"  {nation:20s}: {count:4d} ({pct:5.1f}%)")
    print(f"  {'TOTAL':20s}: {total_torpedoes:4d}")

    # Missiles
    print("\nNAVAL MISSILES")
    print("-" * 70)
    missiles_path = os.path.join(base, "Weapons", "Missiles")
    if os.path.exists(missiles_path):
        missile_nations = [d for d in os.listdir(missiles_path)
                          if os.path.isdir(os.path.join(missiles_path, d))]
        missile_counts = {}
        for nation in missile_nations:
            nation_path = os.path.join(missiles_path, nation)
            count = sum(1 for f in os.listdir(nation_path) if f.endswith('.md'))
            missile_counts[nation] = count
        total_missiles = sum(missile_counts.values())
        for nation, count in sorted(missile_counts.items(), key=lambda x: x[1], reverse=True):
            pct = (count / total_missiles * 100) if total_missiles > 0 else 0
            print(f"  {nation:20s}: {count:4d} ({pct:5.1f}%)")
        print(f"  {'TOTAL':20s}: {total_missiles:4d}")

    # Bombs
    print("\nNAVAL BOMBS")
    print("-" * 70)
    bombs_path = os.path.join(base, "Weapons", "Bombs")
    if os.path.exists(bombs_path):
        bomb_nations = [d for d in os.listdir(bombs_path)
                       if os.path.isdir(os.path.join(bombs_path, d)) and d != 'Research-Trees']
        bomb_counts = {}
        for nation in bomb_nations:
            nation_path = os.path.join(bombs_path, nation)
            count = sum(1 for f in os.listdir(nation_path) if f.endswith('.md'))
            bomb_counts[nation] = count
        total_bombs = sum(bomb_counts.values())
        for nation, count in sorted(bomb_counts.items(), key=lambda x: x[1], reverse=True):
            pct = (count / total_bombs * 100) if total_bombs > 0 else 0
            print(f"  {nation:20s}: {count:4d} ({pct:5.1f}%)")
        print(f"  {'TOTAL':20s}: {total_bombs:4d}")

    # Summary by nation
    print("\n" + "=" * 70)
    print("SUMMARY BY NATION")
    print("=" * 70)

    nation_totals = defaultdict(int)

    # Add ships
    for nation, count in ship_counts.items():
        nation_totals[nation] += count

    # Add carrier aircraft
    for nation, count in aircraft_counts.items():
        nation_totals[nation] += count

    # Add torpedoes (map names)
    for nation, count in torpedo_counts.items():
        mapped = nation.replace('British', 'Great Britain').replace('German', 'Germany').replace('Japanese', 'Japan')
        nation_totals[mapped] += count

    # Add missiles
    if os.path.exists(missiles_path):
        for nation, count in missile_counts.items():
            mapped = nation.replace('British', 'Great Britain').replace('German', 'Germany').replace('Japanese', 'Japan')
            nation_totals[mapped] += count

    # Add bombs
    if os.path.exists(bombs_path):
        for nation, count in bomb_counts.items():
            mapped = nation.replace('British', 'Great Britain').replace('German', 'Germany').replace('Japanese', 'Japan')
            nation_totals[mapped] += count

    grand_total = sum(nation_totals.values())

    print("\nPrimary Nations (Ships + Aircraft + Torpedoes + Missiles + Bombs):")
    for nation, count in sorted(nation_totals.items(), key=lambda x: x[1], reverse=True):
        pct = (count / grand_total * 100) if grand_total > 0 else 0
        print(f"  {nation:20s}: {count:4d} files ({pct:5.1f}%)")

    print(f"\n  USA-only systems: {83 + 72 + 1700} files (Naval Guns: 83, Ammo: 72, Turrets: 1700)")
    print(f"  Multi-nation systems: {142 + 144 + 147} files (Aircraft Weapons: 142, Naval Aircraft: 144, Ground Aircraft: 147)")

    print("\n" + "=" * 70)
    print("RESEARCH GAP ANALYSIS")
    print("=" * 70)

    print("\nMajor Gaps:")
    print("  - Great Britain: Only", ship_counts.get('Great Britain', 0), "ships vs USA's", ship_counts.get('USA', 0))
    print("  - Japan: Only", ship_counts.get('Japan', 0), "ships vs USA's", ship_counts.get('USA', 0))
    print("  - Germany: Only", ship_counts.get('Germany', 0), "ships")
    print("  - Naval Guns: USA only (no British, German, or Japanese guns yet)")
    print("  - Aircraft: All nations underrepresented (113 total vs thousands of real designs)")

    print("\nMinor Gaps:")
    print("  - France: 0 entries (major naval power missing)")
    print("  - Italy: 0 entries (significant WW2 navy)")
    print("  - Soviet Union/Russia: Only in missiles (no ships, aircraft, or torpedoes)")

    print("\nWell-Covered Areas:")
    print("  - USA Ships: Comprehensive (500+)")
    print("  - Torpedoes: Balanced across 4 nations")
    print("  - Missiles: Good coverage (6+ nations)")
    print("  - Naval Bombs: Reasonable coverage (4 nations)")

    print("\n" + "=" * 70)
    print("RECOMMENDED RESEARCH PRIORITIES")
    print("=" * 70)

    print("\n1. GREAT BRITAIN - Expand ship coverage")
    print("   Current: ~150 ships | Target: 300+ ships")
    print("   Focus: Royal Navy (most powerful navy 1800-1945)")
    print("   Priority: HIGH - Major gap in a primary naval power")

    print("\n2. JAPAN - Expand ship coverage")
    print("   Current: ~100 ships | Target: 200+ ships")
    print("   Focus: Imperial Japanese Navy (major Pacific power)")
    print("   Priority: HIGH - Essential for Pacific War coverage")

    print("\n3. NAVAL GUNS - Add British, German, Japanese")
    print("   Current: USA only (83 guns) | Target: +200 guns")
    print("   Focus: Add QF 4.7\", BL 15\", 15cm SK C/28, Type 3 127mm, etc.")
    print("   Priority: VERY HIGH - Critical gap in weapons systems")

    print("\n4. GERMANY - Expand ship coverage")
    print("   Current: ~50 ships | Target: 150+ ships")
    print("   Focus: Kriegsmarine (WW1 High Seas Fleet + WW2)")
    print("   Priority: MEDIUM - Important but smaller navy")

    print("\n5. FRANCE - Begin collection")
    print("   Current: 0 ships | Target: 150+ ships")
    print("   Focus: Marine Nationale (3rd largest navy pre-WW2)")
    print("   Priority: MEDIUM - Major historical naval power")

    print("\n6. ITALY - Begin collection")
    print("   Current: 0 ships | Target: 100+ ships")
    print("   Focus: Regia Marina (significant Mediterranean power)")
    print("   Priority: LOW-MEDIUM - Regional importance")

    print("\n7. AIRCRAFT - Expand all nations")
    print("   Current: 404 total | Target: 1000+ aircraft")
    print("   Focus: Add more variants, post-war jets, modern aircraft")
    print("   Priority: MEDIUM - Good baseline but could expand")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
