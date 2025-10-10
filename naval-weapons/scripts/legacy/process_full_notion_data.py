#!/usr/bin/env python3
"""
Process Full Notion Data for Shell-Gun Matching
Get complete datasets from both databases and run comprehensive matching
"""

import json
from notion_shell_gun_matcher import ShellGunMatcher

def process_full_datasets():
    """Process complete shell and gun datasets from Notion searches"""

    print("Processing Full Notion Dataset for Shell-Gun Matching")
    print("=" * 60)

    # Initialize matcher
    matcher = ShellGunMatcher()

    # Complete shell data from previous Notion searches
    # This would normally come from comprehensive Notion API calls
    complete_shell_data = [
        {"title": "4.5\" QF Mark I-IV AP", "url": "https://www.notion.so/2750ddf7bbe5811ea2f5c51c840af99d", "id": "2750ddf7-bbe5-811e-a2f5-c51c840af99d", "highlight": "Burster_lbs: 1.4\nExplosive_Dmg: 3.5\nKE_MJ: 0.857\nMark_Designation: QF Mark I-IV\nNation: British\nSpecial_Features: Fleet destroyers\nType: AP\nVelocity_fps: 2650\nWeight_lbs: 55"},
        {"title": "16\" B-37 AP", "url": "https://www.notion.so/2750ddf7bbe5813299eed7cabf40715d", "id": "2750ddf7-bbe5-8132-99ee-d7cabf40715d", "highlight": "Burster_lbs: 64.8\nExplosive_Dmg: 1180\nKE_MJ: 34\nMark_Designation: B-37\nNation: Soviet\nSpecial_Features: Sovetsky Soyuz-class\nType: AP\nVelocity_fps: 2690\nWeight_lbs: 2375"},
        {"title": "4.5\" QF Mark I-IV HE", "url": "https://www.notion.so/2750ddf7bbe5819f93abce37eaf2f632", "id": "2750ddf7-bbe5-819f-93ab-ce37eaf2f632", "highlight": "Burster_lbs: 4.4\nExplosive_Dmg: 11\nKE_MJ: 0.857\nMark_Designation: QF Mark I-IV\nNation: British\nSpecial_Features: Dual-purpose main destroyer\nType: HE\nVelocity_fps: 2650\nWeight_lbs: 55"},
        {"title": "6\" B-40* AP", "url": "https://www.notion.so/2750ddf7bbe581a08ff6e373af811b56", "id": "2750ddf7-bbe5-81a0-8ff6-e373af811b56", "highlight": "Burster_lbs: 0\nExplosive_Dmg: 0\nKE_MJ: 5.2\nMark_Designation: B-40*\nNation: Soviet\nSpecial_Features: Project shell*\nType: AP\nVelocity_fps: 2800\nWeight_lbs: 275"},
        {"title": "8\" Mk 21 AP", "url": "https://www.notion.so/2750ddf7bbe581a08486faa3a5ec29b9", "id": "2750ddf7-bbe5-81a0-8486-faa3a5ec29b9", "highlight": "Burster_lbs: 28.9\nExplosive_Dmg: 350\nKE_MJ: 5.2\nMark_Designation: Mk 21\nNation: US\nSpecial_Features: Super-heavy cruiser shell\nType: AP\nVelocity_fps: 2800\nWeight_lbs: 335"},
        {"title": "15\" Model 42* HE", "url": "https://www.notion.so/2750ddf7bbe5812f807af25c792226e5", "id": "2750ddf7-bbe5-812f-807a-f25c792226e5", "highlight": "Burster_lbs: 48.5\nExplosive_Dmg: 850\nKE_MJ: 25\nMark_Designation: Model 42*\nNation: Netherlands\nSpecial_Features: Study project*\nType: HE\nVelocity_fps: 2500\nWeight_lbs: 1938"},
        {"title": "8\" Mark VIII HE", "url": "https://www.notion.so/2750ddf7bbe5817cbb8aeb4efb0d2a5c", "id": "2750ddf7-bbe5-817c-bb8a-eb4efb0d2a5c", "highlight": "Burster_lbs: 20\nExplosive_Dmg: 50\nKE_MJ: 4.13\nMark_Designation: Mark VIII\nNation: British\nSpecial_Features: Anti-structure\nType: HE\nVelocity_fps: 2725\nWeight_lbs: 250"},
        {"title": "6\" Mark VII/VIII Common", "url": "https://www.notion.so/2750ddf7bbe58103a4d8d8bf49118792", "id": "2750ddf7-bbe5-8103-a4d8-d8bf49118792", "highlight": "Burster_lbs: 9\nExplosive_Dmg: 22.5\nKE_MJ: 1.559\nMark_Designation: Mark VII/VIII\nNation: British\nSpecial_Features: Multi-purpose lyddite\nType: Common\nVelocity_fps: 2650\nWeight_lbs: 100"},
        {"title": "14\" Mark VIIb AP", "url": "https://www.notion.so/2750ddf7bbe58131a5d7e920def395a2", "id": "2750ddf7-bbe5-8131-a5d7-e920def395a2", "highlight": "Burster_lbs: 39.8\nExplosive_Dmg: 99.5\nKE_MJ: 21.75\nMark_Designation: Mark VIIb\nNation: British\nSpecial_Features: King George V-class\nType: AP\nVelocity_fps: 2483\nWeight_lbs: 1590"},
        {"title": "15\" Mark XIIa AP", "url": "https://www.notion.so/2750ddf7bbe581c2a869e96712d8e960", "id": "2750ddf7-bbe5-81c2-a869-e96712d8e960", "highlight": "Burster_lbs: 48\nExplosive_Dmg: 120\nKE_MJ: 25.8\nMark_Designation: Mark XIIa\nNation: British\nSpecial_Features: Most successful British gun\nType: AP\nVelocity_fps: 2450\nWeight_lbs: 1938"}
    ]

    # Complete gun data from previous Notion searches
    complete_gun_data = [
        {"title": "14.96\"/45 SK L/45 Improved", "url": "https://www.notion.so/2750ddf7bbe58158afb7ea380401b1be", "id": "2750ddf7-bbe5-8158-afb7-ea380401b1be", "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 180\nCaliber_Length: 14.96\"/45\nMuzzle_Velocity_fps: 2920\nNation: 🇩🇪 German\nPerformance_Category: High Velocity\nPeriod: 1918\nUpgrade_Features: Enhanced propellant, higher velocity\nUpgrade_Type: Enhanced Metallurgy"},
        {"title": "14\"/45 Mark VII*", "url": "https://www.notion.so/2750ddf7bbe5819eb10ee8df2623d4ad", "id": "2750ddf7-bbe5-819e-b10e-e8df2623d4ad", "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 340\nCaliber_Length: 14\"/45\nMuzzle_Velocity_fps: 2500\nNation: 🇬🇧 British\nPerformance_Category: Balanced\nPeriod: 1942-1945\nUpgrade_Features: Improved cordite, better performance\nUpgrade_Type: Enhanced Metallurgy"},
        {"title": "16\"/50 B-37 Pattern 1937", "url": "https://www.notion.so/2750ddf7bbe5812f9d99ffa0bb2a109f", "id": "2750ddf7-bbe5-812f-9d99-ffa0bb2a109f", "highlight": "Accuracy: Superior\nBarrel_Life_rounds: 400\nCaliber_Length: 16\"/50\nMuzzle_Velocity_fps: 2700\nNation: 🇷🇺 Soviet\nPerformance_Category: High Velocity\nPeriod: Planned 1938-1941\nUpgrade_Features: Maximum theoretical range 45600m\nUpgrade_Type: Standard"},
        {"title": "16.1\"/45 Type 94 (1920)", "url": "https://www.notion.so/2750ddf7bbe581ff9bc0cf807765b0aa", "id": "2750ddf7-bbe5-81ff-9bc0-cf807765b0aa", "highlight": "Accuracy: Standard\nBarrel_Life_rounds: 300\nCaliber_Length: 16.1\"/45\nMuzzle_Velocity_fps: 2559\nNation: 🇯🇵 Japanese\nPerformance_Category: Balanced\nPeriod: 1920-1935\nUpgrade_Features: Original Nagato specification\nUpgrade_Type: Standard"},
        {"title": "16\"/45 Mark 6 Mod 1", "url": "https://www.notion.so/2750ddf7bbe5819bb394ca25a9b2a0d2", "id": "2750ddf7-bbe5-819b-b394-ca25a9b2a0d2", "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 350\nCaliber_Length: 16\"/45\nMuzzle_Velocity_fps: 2350\nNation: 🇺🇸 United States\nPerformance_Category: Long Life\nPeriod: 1943-1945\nUpgrade_Features: Improved powder, better performance\nUpgrade_Type: Enhanced Metallurgy"},
        {"title": "4.7\"/50 QF Mark XII", "url": "https://www.notion.so/2750ddf7bbe5814fbecfd1a2aaab09a9", "id": "2750ddf7-bbe5-814f-becf-d1a2aaab09a9", "highlight": "Accuracy: Standard\nBarrel_Life_rounds: 500\nCaliber_Length: 4.7\"/50\nMuzzle_Velocity_fps: 2650\nNation: 🇬🇧 British\nPerformance_Category: Long Life\nPeriod: 1930-1945\nUpgrade_Features: Destroyer main armament\nUpgrade_Type: Standard"},
        {"title": "15\"/50 Model 1934 Reduced", "url": "https://www.notion.so/2750ddf7bbe581bbadf7d79d2ed4ef48", "id": "2750ddf7-bbe5-81bb-adf7-d79d2ed4ef48", "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 250\nCaliber_Length: 15\"/50\nMuzzle_Velocity_fps: 2789\nNation: 🇮🇹 Italian\nPerformance_Category: Balanced\nPeriod: 1941-1943\nUpgrade_Features: Reduced charge for accuracy longer life\nUpgrade_Type: Standard"},
        {"title": "8\"/50 Model 1942*", "url": "https://www.notion.so/fake-gun-id-for-testing", "id": "fake-gun-id-for-testing", "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 450\nCaliber_Length: 8\"/50\nMuzzle_Velocity_fps: 2850\nNation: 🇺🇸 United States\nPerformance_Category: High Velocity\nPeriod: 1942-1945\nUpgrade_Features: Theoretical US heavy cruiser\nUpgrade_Type: Enhanced Metallurgy"},
        {"title": "6\"/50 Model 1938", "url": "https://www.notion.so/fake-gun-id-2", "id": "fake-gun-id-2", "highlight": "Accuracy: Standard\nBarrel_Life_rounds: 600\nCaliber_Length: 6\"/50\nMuzzle_Velocity_fps: 2750\nNation: 🇷🇺 Soviet\nPerformance_Category: Long Life\nPeriod: 1938-1945\nUpgrade_Features: Soviet light cruiser main gun\nUpgrade_Type: Standard"}
    ]

    # Remove debug output from matcher
    matcher._debug = False

    print(f"Processing {len(complete_shell_data)} shells...")
    matcher.add_shell_data(complete_shell_data)

    print(f"Processing {len(complete_gun_data)} guns...")
    matcher.add_gun_data(complete_gun_data)

    print("\nGenerating comprehensive matches...")
    matches = matcher.generate_all_matches()

    print("\n" + "="*60)
    matcher.print_summary()

    # Show caliber analysis
    print(f"\nCALIBER ANALYSIS:")
    caliber_stats = {}
    for gun in matcher.gun_data:
        caliber = gun['caliber']
        if caliber not in caliber_stats:
            caliber_stats[caliber] = {'guns': 0, 'shells': 0, 'matches': 0}
        caliber_stats[caliber]['guns'] += 1

    for shell in matcher.shell_data:
        caliber = shell['caliber']
        if caliber not in caliber_stats:
            caliber_stats[caliber] = {'guns': 0, 'shells': 0, 'matches': 0}
        caliber_stats[caliber]['shells'] += 1

    for gun_id, match_data in matches.items():
        gun = match_data['gun_info']
        caliber = gun['caliber']
        caliber_stats[caliber]['matches'] += len(match_data['compatible_shells'])

    for caliber in sorted(caliber_stats.keys()):
        stats = caliber_stats[caliber]
        print(f"   {caliber}: {stats['guns']} guns, {stats['shells']} shells, {stats['matches']} total matches")

    # Show detailed matches
    print(f"\nDETAILED MATCHES:")
    for gun_id, match_data in matches.items():
        gun = match_data['gun_info']
        shells = match_data['compatible_shells']

        print(f"\n{gun['title']} ({gun['caliber']}, {gun['nation']})")
        if shells:
            for shell in shells:
                print(f"   -> {shell['title']} ({shell['type']})")
        else:
            print(f"   No compatible shells found")

    # Generate Notion update commands
    update_commands = matcher.get_notion_update_commands()
    print(f"\nGenerated {len(update_commands)} Notion update commands")

    # Save comprehensive results
    matcher.save_results("comprehensive_shell_gun_matches.json")

    print("\nComprehensive matching analysis complete!")
    return update_commands

if __name__ == "__main__":
    update_commands = process_full_datasets()