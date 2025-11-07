#!/usr/bin/env python3
"""Identify priority weapons that need historical content"""

from pathlib import Path
import re

def extract_year(content):
    """Extract introduction year from file"""
    match = re.search(r'introduced:\s*(\d{4})', content)
    return int(match.group(1)) if match else None

def is_famous_weapon(filepath, content):
    """Check if weapon is historically significant"""
    filename = filepath.stem.lower()
    content_lower = content.lower()

    # Famous torpedoes
    famous_torpedoes = [
        'type 93', 'long lance', 'mark 14', 'mark 48', 'g7',
        'whitehead', 'mk 46', 'mk 48', 'spearfish', 'tigerfish'
    ]

    # Famous missiles
    famous_missiles = [
        'harpoon', 'tomahawk', 'exocet', 'sea sparrow', 'standard',
        'phoenix', 'aim-', 'rim-', 'agm-', 'bgm-'
    ]

    # Famous guns (less applicable to turrets, but keep for main guns)
    famous_guns = [
        '16-inch', '18-inch', '14-inch', 'yamato', 'bismarck'
    ]

    for weapon in famous_torpedoes + famous_missiles + famous_guns:
        if weapon in filename or weapon in content_lower:
            return True

    return False

def main():
    root = Path.cwd()

    print("=" * 70)
    print("IDENTIFY PRIORITY WEAPONS FOR CONTENT EXPANSION")
    print("=" * 70)

    # Find all partial weapon files
    partial_weapons = {
        'Torpedoes': [],
        'Missiles': [],
        'Naval Guns': [],
        'Other': []
    }

    for filepath in root.rglob('*.md'):
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if 'completeness: partial' in content:
                path_str = str(filepath).replace('\\', '/')

                info = {
                    'path': filepath,
                    'year': extract_year(content),
                    'famous': is_famous_weapon(filepath, content),
                    'line_count': len(content.split('\n'))
                }

                if '/Torpedoes/' in path_str:
                    partial_weapons['Torpedoes'].append(info)
                elif '/Missiles/' in path_str:
                    partial_weapons['Missiles'].append(info)
                elif '/Naval-Guns/' in path_str:
                    partial_weapons['Naval Guns'].append(info)
                else:
                    partial_weapons['Other'].append(info)
        except:
            pass

    # Summary
    print("\nPartial Files by Category:")
    for cat, files in partial_weapons.items():
        print(f"  {cat}: {len(files)} files")

    # Priority identification
    print("\n" + "=" * 70)
    print("PRIORITY WEAPONS FOR EXPANSION")
    print("=" * 70)

    priority_weapons = []

    # Add all famous weapons
    for cat, files in partial_weapons.items():
        for info in files:
            if info['famous']:
                priority_weapons.append((cat, info))

    # Add early weapons (pre-1920) from torpedoes and missiles
    for cat in ['Torpedoes', 'Missiles']:
        for info in partial_weapons[cat]:
            if info['year'] and info['year'] < 1920 and not info['famous']:
                priority_weapons.append((cat, info))

    # Add WWII-era weapons (1939-1945)
    for cat in ['Torpedoes', 'Missiles']:
        for info in partial_weapons[cat]:
            if info['year'] and 1939 <= info['year'] <= 1945 and not info['famous']:
                priority_weapons.append((cat, info))

    # Add modern weapons (post-1990)
    for cat in ['Torpedoes', 'Missiles']:
        for info in partial_weapons[cat]:
            if info['year'] and info['year'] >= 1990 and not info['famous']:
                priority_weapons.append((cat, info))

    # Remove duplicates
    seen = set()
    unique_priority = []
    for cat, info in priority_weapons:
        if str(info['path']) not in seen:
            seen.add(str(info['path']))
            unique_priority.append((cat, info))

    print(f"\nTotal priority weapons identified: {len(unique_priority)}")

    # Show breakdown
    priority_by_cat = {}
    for cat, info in unique_priority:
        priority_by_cat[cat] = priority_by_cat.get(cat, 0) + 1

    print("\nBreakdown by category:")
    for cat, count in priority_by_cat.items():
        print(f"  {cat}: {count} files")

    # Show samples
    print("\n" + "=" * 70)
    print("SAMPLE PRIORITY WEAPONS (first 20)")
    print("=" * 70)

    for i, (cat, info) in enumerate(unique_priority[:20]):
        famous_marker = " [FAMOUS]" if info['famous'] else ""
        year_str = f" ({info['year']})" if info['year'] else ""
        print(f"{i+1}. [{cat}] {info['path'].stem}{year_str}{famous_marker}")
        print(f"   {str(info['path'].relative_to(root))}")

    if len(unique_priority) > 20:
        print(f"\n... and {len(unique_priority) - 20} more priority weapons")

    # Recommendation
    print("\n" + "=" * 70)
    print("RECOMMENDATION")
    print("=" * 70)
    print(f"\nIdentified {len(unique_priority)} priority weapons for content expansion.")
    print("\nThese include:")
    print("  - Famous/historically significant weapons")
    print("  - Early weapons (pre-1920)")
    print("  - WWII-era weapons (1939-1945)")
    print("  - Modern weapons (post-1990)")
    print("\nRecommended approach:")
    print("  1. Use WebSearch/WebFetch to research top 50-100 weapons")
    print("  2. Add brief historical notes (1-3 paragraphs)")
    print("  3. Focus on service history, combat usage, significance")
    print(f"\nNote: Naval Gun turrets ({len(partial_weapons['Naval Guns'])} files)")
    print("      are mostly complete and don't need historical expansion.")

if __name__ == '__main__':
    main()
