#!/usr/bin/env python3
"""Analyze completeness by Type → Country → Subtype"""

from pathlib import Path
from collections import defaultdict
import re

def extract_completeness(content):
    """Extract completeness level from YAML"""
    match = re.search(r'completeness:\s*(stub|partial|complete)', content)
    return match.group(1) if match else None

def analyze_section(root, section_name, path_pattern):
    """Analyze a specific section (Ships, Aircraft, Weapons)"""

    results = defaultdict(lambda: defaultdict(lambda: {
        'total': 0,
        'complete': 0,
        'partial': 0,
        'stub': 0,
        'no_tracking': 0
    }))

    for filepath in root.glob(path_pattern):
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Parse path to get country and type
            parts = filepath.relative_to(root).parts

            if section_name == "Ships":
                # Ships/Destroyers/Germany/Z1.md
                if len(parts) >= 3:
                    ship_type = parts[1]
                    country = parts[2]

                    completeness = extract_completeness(content)
                    results[ship_type][country]['total'] += 1

                    if completeness == 'complete':
                        results[ship_type][country]['complete'] += 1
                    elif completeness == 'partial':
                        results[ship_type][country]['partial'] += 1
                    elif completeness == 'stub':
                        results[ship_type][country]['stub'] += 1
                    else:
                        results[ship_type][country]['no_tracking'] += 1

            elif section_name == "Aircraft":
                # Aircraft/Germany/Land-Fighter/F-104G.md
                if len(parts) >= 3:
                    country = parts[1]
                    aircraft_type = parts[2]

                    completeness = extract_completeness(content)
                    results[aircraft_type][country]['total'] += 1

                    if completeness == 'complete':
                        results[aircraft_type][country]['complete'] += 1
                    elif completeness == 'partial':
                        results[aircraft_type][country]['partial'] += 1
                    elif completeness == 'stub':
                        results[aircraft_type][country]['stub'] += 1
                    else:
                        results[aircraft_type][country]['no_tracking'] += 1

            elif section_name == "Weapons":
                # Weapons/Torpedoes/British/18inch Mark V.md
                if len(parts) >= 3:
                    weapon_type = parts[1]
                    country = parts[2]

                    completeness = extract_completeness(content)
                    results[weapon_type][country]['total'] += 1

                    if completeness == 'complete':
                        results[weapon_type][country]['complete'] += 1
                    elif completeness == 'partial':
                        results[weapon_type][country]['partial'] += 1
                    elif completeness == 'stub':
                        results[weapon_type][country]['stub'] += 1
                    else:
                        results[weapon_type][country]['no_tracking'] += 1
        except:
            pass

    return results

def print_section_summary(section_name, results):
    """Print summary for a section"""
    print("\n" + "=" * 80)
    print(f"{section_name.upper()} - COMPLETENESS BY TYPE AND NATION")
    print("=" * 80)

    # Get all unique countries
    all_countries = set()
    for type_data in results.values():
        all_countries.update(type_data.keys())
    all_countries = sorted(all_countries)

    # Print each type
    for item_type in sorted(results.keys()):
        print(f"\n### {item_type}")
        print("-" * 80)

        # Header
        print(f"{'Country':<20} {'Total':>8} {'Complete':>10} {'Partial':>10} {'Stub':>8} {'%Complete':>12}")
        print("-" * 80)

        # Data for each country
        type_total = 0
        type_complete = 0

        for country in all_countries:
            if country in results[item_type]:
                data = results[item_type][country]
                total = data['total']
                complete = data['complete']
                partial = data['partial']
                stub = data['stub']

                pct = (complete / total * 100) if total > 0 else 0

                print(f"{country:<20} {total:>8} {complete:>10} {partial:>10} {stub:>8} {pct:>11.1f}%")

                type_total += total
                type_complete += complete

        # Type totals
        type_pct = (type_complete / type_total * 100) if type_total > 0 else 0
        print("-" * 80)
        print(f"{'TOTAL':<20} {type_total:>8} {type_complete:>10} {'':>10} {'':>8} {type_pct:>11.1f}%")

def print_nation_comparison(section_name, results):
    """Print nation-by-nation comparison"""
    print("\n" + "=" * 80)
    print(f"{section_name.upper()} - NATION COMPARISON")
    print("=" * 80)

    # Aggregate by nation
    nation_totals = defaultdict(lambda: {'total': 0, 'complete': 0, 'types': set()})

    for item_type, countries in results.items():
        for country, data in countries.items():
            nation_totals[country]['total'] += data['total']
            nation_totals[country]['complete'] += data['complete']
            nation_totals[country]['types'].add(item_type)

    # Print comparison
    print(f"\n{'Nation':<20} {'Total Files':>12} {'Complete':>12} {'%Complete':>12} {'Type Coverage':>15}")
    print("-" * 80)

    for country in sorted(nation_totals.keys()):
        data = nation_totals[country]
        pct = (data['complete'] / data['total'] * 100) if data['total'] > 0 else 0
        type_count = len(data['types'])

        print(f"{country:<20} {data['total']:>12} {data['complete']:>12} {pct:>11.1f}% {type_count:>15}")

    # Overall
    overall_total = sum(d['total'] for d in nation_totals.values())
    overall_complete = sum(d['complete'] for d in nation_totals.values())
    overall_pct = (overall_complete / overall_total * 100) if overall_total > 0 else 0

    print("-" * 80)
    print(f"{'OVERALL':<20} {overall_total:>12} {overall_complete:>12} {overall_pct:>11.1f}%")

def identify_gaps(section_name, results):
    """Identify gaps where nations have significantly fewer files"""
    print("\n" + "=" * 80)
    print(f"{section_name.upper()} - CONTENT GAPS ANALYSIS")
    print("=" * 80)

    # Calculate average files per nation per type
    type_averages = {}

    for item_type, countries in results.items():
        if not countries:
            continue

        totals = [data['total'] for data in countries.values()]
        avg = sum(totals) / len(totals)
        max_count = max(totals)
        min_count = min(totals)

        type_averages[item_type] = {
            'avg': avg,
            'max': max_count,
            'min': min_count,
            'countries': countries
        }

    # Find gaps (nations with < 50% of average)
    print("\nTypes with significant nation gaps (some nations < 50% of average):")
    print("-" * 80)

    gaps_found = False
    for item_type, stats in sorted(type_averages.items()):
        avg = stats['avg']

        gaps = []
        for country, data in stats['countries'].items():
            if data['total'] < (avg * 0.5) and avg > 5:  # Only flag if average > 5 files
                gaps.append((country, data['total'], avg))

        if gaps:
            gaps_found = True
            print(f"\n{item_type}:")
            print(f"  Average: {avg:.1f} files | Max: {stats['max']} | Min: {stats['min']}")
            print(f"  Nations below 50% of average:")
            for country, count, avg_val in gaps:
                print(f"    - {country}: {count} files ({count/avg_val*100:.1f}% of average)")

    if not gaps_found:
        print("\n✅ No significant gaps found! All nations have reasonable coverage.")

    # Identify completely missing types for nations
    print("\n" + "-" * 80)
    print("Missing Types by Nation:")
    print("-" * 80)

    # Get all types and all nations
    all_types = set(results.keys())
    all_nations = set()
    for countries in results.values():
        all_nations.update(countries.keys())

    missing_found = False
    for nation in sorted(all_nations):
        nation_types = set()
        for item_type, countries in results.items():
            if nation in countries:
                nation_types.add(item_type)

        missing = all_types - nation_types
        if missing:
            missing_found = True
            print(f"\n{nation}: Missing {len(missing)} type(s)")
            for missing_type in sorted(missing):
                print(f"  - {missing_type}")

    if not missing_found:
        print("\n✅ All nations have coverage in all types!")

def main():
    root = Path.cwd()

    print("=" * 80)
    print("COMPREHENSIVE COMPLETENESS ANALYSIS")
    print("Type -> Country -> Subtype Breakdown")
    print("=" * 80)

    # Analyze each major section
    sections = [
        ("Ships", "Ships/**/*.md"),
        ("Aircraft", "Aircraft/**/*.md"),
        ("Weapons", "Weapons/**/*.md")
    ]

    for section_name, pattern in sections:
        results = analyze_section(root, section_name, pattern)

        if results:
            print_section_summary(section_name, results)
            print_nation_comparison(section_name, results)
            identify_gaps(section_name, results)
        else:
            print(f"\n[WARNING] No data found for {section_name}")

    # Overall repository summary
    print("\n" + "=" * 80)
    print("OVERALL REPOSITORY SUMMARY")
    print("=" * 80)

    total_files = 0
    complete_files = 0

    for filepath in root.rglob("*.md"):
        if any(skip in str(filepath) for skip in ['_Templates', '_Scripts', '_Reports', '_Archive']):
            continue

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            completeness = extract_completeness(content)
            if completeness:
                total_files += 1
                if completeness == 'complete':
                    complete_files += 1
        except:
            pass

    overall_pct = (complete_files / total_files * 100) if total_files > 0 else 0

    print(f"\nTotal files tracked: {total_files}")
    print(f"Complete files: {complete_files}")
    print(f"Overall completion: {overall_pct:.1f}%")

    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == '__main__':
    main()
