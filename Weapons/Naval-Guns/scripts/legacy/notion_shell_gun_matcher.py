#!/usr/bin/env python3
"""
Notion Shell to Gun Variant Matcher
Implements caliber and nation-specific matching logic for connecting shells to gun variants
"""

import re
import json
from typing import Dict, List, Tuple, Set

class ShellGunMatcher:
    def __init__(self):
        # Nation mapping from emoji flags to text names
        self.nation_mapping = {
            '🇬🇧 British': 'British',
            '🇺🇸 United States': 'US',
            '🇷🇺 Soviet': 'Soviet',
            '🇯🇵 Japanese': 'Japanese',
            '🇩🇪 German': 'German',
            '🇫🇷 French': 'French',
            '🇮🇹 Italian': 'Italian',
            '🇦🇹 Austria-Hungary': 'Austria-Hungary',
            '🇪🇸 Spain': 'Spain',
            '🇳🇱 Netherlands': 'Netherlands',
            '🇧🇷 Brazil': 'Brazil'
        }

        # Reverse mapping for lookup
        self.text_to_flag = {v: k for k, v in self.nation_mapping.items()}

        self.shell_data = []
        self.gun_data = []
        self.matches = {}

    def extract_caliber_from_gun(self, caliber_length: str) -> str:
        """
        Extract caliber from Caliber_Length field
        Examples:
        - "16\"/50" → "16\""
        - "14.96\"/45" → "14.96\""
        - "18.1\"/45" → "18.1\""
        """
        pattern = r'^([0-9.]+)"'
        match = re.match(pattern, caliber_length)
        if match:
            return f'{match.group(1)}"'
        return caliber_length  # Fallback to original

    def normalize_nation(self, nation_text: str) -> str:
        """
        Convert nation flag text to standard text format
        """
        return self.nation_mapping.get(nation_text, nation_text)

    def extract_caliber_from_shell(self, shell_caliber: str) -> str:
        """
        Extract caliber from shell Caliber field
        Usually already in correct format like "16\"", "8\"", etc.
        """
        return shell_caliber

    def add_shell_data(self, shells: List[Dict]):
        """Add shell data from Notion search results"""
        for shell in shells:
            if 'highlight' in shell and shell['highlight']:
                data = self.parse_notion_data(shell['highlight'])

                # Check if we have Caliber in the title (since shells use title as caliber)
                caliber = None
                if 'Caliber' in data:
                    caliber = data['Caliber']
                else:
                    # Extract caliber from title (e.g., "16\" B-37 AP" -> "16\"")
                    caliber_match = re.match(r'^([0-9.]+)"', shell['title'])
                    if caliber_match:
                        caliber = f'{caliber_match.group(1)}"'

                if 'Nation' in data and caliber:
                    shell_info = {
                        'title': shell['title'],
                        'url': shell['url'],
                        'id': shell['id'],
                        'caliber': caliber,
                        'nation': data['Nation'],
                        'type': data.get('Type', 'Unknown'),
                        'mark_designation': data.get('Mark_Designation', ''),
                        'raw_data': data
                    }
                    self.shell_data.append(shell_info)

    def add_gun_data(self, guns: List[Dict]):
        """Add gun variant data from Notion search results"""
        for gun in guns:
            if 'highlight' in gun and gun['highlight']:
                data = self.parse_notion_data(gun['highlight'])
                if 'Nation' in data and 'Caliber_Length' in data:
                    gun_info = {
                        'title': gun['title'],
                        'url': gun['url'],
                        'id': gun['id'],
                        'caliber': self.extract_caliber_from_gun(data['Caliber_Length']),
                        'nation': self.normalize_nation(data['Nation']),
                        'period': data.get('Period', ''),
                        'upgrade_type': data.get('Upgrade_Type', ''),
                        'raw_data': data
                    }
                    self.gun_data.append(gun_info)

    def parse_notion_data(self, highlight: str) -> Dict:
        """Parse highlight data from Notion search results"""
        data = {}
        lines = highlight.strip().split('\n')
        for line in lines:
            if ':' in line:
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
        return data

    def find_compatible_shells(self, gun_info: Dict) -> List[Dict]:
        """
        Find shells compatible with a specific gun variant
        Matches on:
        1. Exact caliber match
        2. Same nation (no cross-nation compatibility)
        """
        compatible = []
        gun_caliber = gun_info['caliber']
        gun_nation = gun_info['nation']

        print(f"\nFinding shells for {gun_info['title']}")
        print(f"   Gun caliber: {gun_caliber}")
        print(f"   Gun nation: {gun_nation}")

        for shell in self.shell_data:
            shell_caliber = shell['caliber']
            shell_nation = shell['nation']

            # Check caliber match
            caliber_match = shell_caliber == gun_caliber

            # Check nation match (strict - no cross-nation)
            nation_match = shell_nation == gun_nation

            if caliber_match and nation_match:
                compatible.append(shell)
                print(f"   MATCH: {shell['title']} ({shell_caliber}, {shell_nation})")
            elif caliber_match and not nation_match:
                print(f"   REJECT: {shell['title']} ({shell_caliber}, {shell_nation}) - Nation mismatch")

        return compatible

    def generate_all_matches(self) -> Dict:
        """Generate all shell-to-gun matches"""
        print("Generating shell-to-gun matches with nation-specific compatibility...")

        for gun in self.gun_data:
            compatible_shells = self.find_compatible_shells(gun)
            self.matches[gun['id']] = {
                'gun_info': gun,
                'compatible_shells': compatible_shells,
                'shell_count': len(compatible_shells)
            }

        return self.matches

    def print_summary(self):
        """Print matching summary"""
        print(f"\nMATCHING SUMMARY")
        print(f"   Shells analyzed: {len(self.shell_data)}")
        print(f"   Guns analyzed: {len(self.gun_data)}")
        print(f"   Guns with matches: {len([m for m in self.matches.values() if m['shell_count'] > 0])}")
        print(f"   Guns without matches: {len([m for m in self.matches.values() if m['shell_count'] == 0])}")

        # Nation breakdown
        nation_stats = {}
        for gun in self.gun_data:
            nation = gun['nation']
            if nation not in nation_stats:
                nation_stats[nation] = {'guns': 0, 'shells': 0}
            nation_stats[nation]['guns'] += 1

        for shell in self.shell_data:
            nation = shell['nation']
            if nation not in nation_stats:
                nation_stats[nation] = {'guns': 0, 'shells': 0}
            nation_stats[nation]['shells'] += 1

        print(f"\nNATION BREAKDOWN:")
        for nation, stats in sorted(nation_stats.items()):
            print(f"   {nation}: {stats['guns']} guns, {stats['shells']} shells")

    def get_notion_update_commands(self) -> List[Dict]:
        """Generate Notion API update commands"""
        update_commands = []

        for gun_id, match_data in self.matches.items():
            if match_data['shell_count'] > 0:
                # Create list of shell page URLs for relation field
                shell_urls = [shell['url'] for shell in match_data['compatible_shells']]

                update_command = {
                    'gun_url': match_data['gun_info']['url'],
                    'gun_id': gun_id,
                    'gun_title': match_data['gun_info']['title'],
                    'shell_urls': shell_urls,
                    'shell_count': len(shell_urls)
                }
                update_commands.append(update_command)

        return update_commands

    def save_results(self, filename: str = "shell_gun_matches.json"):
        """Save matching results to JSON file"""
        results = {
            'summary': {
                'shells_analyzed': len(self.shell_data),
                'guns_analyzed': len(self.gun_data),
                'total_matches': sum(m['shell_count'] for m in self.matches.values()),
                'guns_with_matches': len([m for m in self.matches.values() if m['shell_count'] > 0])
            },
            'matches': self.matches,
            'update_commands': self.get_notion_update_commands()
        }

        with open(f"D:/Research/{filename}", 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)

        print(f"\nResults saved to: D:/Research/{filename}")

if __name__ == "__main__":
    print("Shell-Gun Matcher Initialized")
    print("Ready to process Notion data...")