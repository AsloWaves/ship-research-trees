#!/usr/bin/env python3
"""
Run Shell-Gun Matching Analysis
Process Notion data and generate compatible shell-gun relationships
"""

from notion_shell_gun_matcher import ShellGunMatcher

def main():
    print("Starting Shell-Gun Matching Analysis")
    print("=" * 60)

    # Initialize matcher
    matcher = ShellGunMatcher()

    # Sample shell data from Notion search
    shell_data = [
        {
            "title": "4.5\" QF Mark I-IV AP",
            "url": "https://www.notion.so/2750ddf7bbe5811ea2f5c51c840af99d",
            "id": "2750ddf7-bbe5-811e-a2f5-c51c840af99d",
            "highlight": "Burster_lbs: 1.4\nExplosive_Dmg: 3.5\nKE_MJ: 0.857\nMark_Designation: QF Mark I-IV\nNation: British\nSpecial_Features: Fleet destroyers\nType: AP\nVelocity_fps: 2650\nWeight_lbs: 55"
        },
        {
            "title": "16\" B-37 AP",
            "url": "https://www.notion.so/2750ddf7bbe5813299eed7cabf40715d",
            "id": "2750ddf7-bbe5-8132-99ee-d7cabf40715d",
            "highlight": "Burster_lbs: 64.8\nExplosive_Dmg: 1180\nKE_MJ: 34\nMark_Designation: B-37\nNation: Soviet\nSpecial_Features: Sovetsky Soyuz-class\nType: AP\nVelocity_fps: 2690\nWeight_lbs: 2375"
        },
        {
            "title": "8\" Mk 21 AP",
            "url": "https://www.notion.so/2750ddf7bbe581a08486faa3a5ec29b9",
            "id": "2750ddf7-bbe5-81a0-8486-faa3a5ec29b9",
            "highlight": "Burster_lbs: 28.9\nExplosive_Dmg: 350\nKE_MJ: 5.2\nMark_Designation: Mk 21\nNation: US\nSpecial_Features: Super-heavy cruiser shell\nType: AP\nVelocity_fps: 2800\nWeight_lbs: 335"
        },
        {
            "title": "14\" Mark VIIb AP",
            "url": "https://www.notion.so/2750ddf7bbe58131a5d7e920def395a2",
            "id": "2750ddf7-bbe5-8131-a5d7-e920def395a2",
            "highlight": "Burster_lbs: 39.8\nExplosive_Dmg: 99.5\nKE_MJ: 21.75\nMark_Designation: Mark VIIb\nNation: British\nSpecial_Features: King George V-class\nType: AP\nVelocity_fps: 2483\nWeight_lbs: 1590"
        }
    ]

    # Sample gun data from Notion search
    gun_data = [
        {
            "title": "14\"/45 Mark VII*",
            "url": "https://www.notion.so/2750ddf7bbe5819eb10ee8df2623d4ad",
            "id": "2750ddf7-bbe5-819e-b10e-e8df2623d4ad",
            "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 340\nCaliber_Length: 14\"/45\nMuzzle_Velocity_fps: 2500\nNation: 🇬🇧 British\nPerformance_Category: Balanced\nPeriod: 1942-1945\nUpgrade_Features: Improved cordite, better performance\nUpgrade_Type: Enhanced Metallurgy"
        },
        {
            "title": "16\"/50 B-37 Pattern 1937",
            "url": "https://www.notion.so/2750ddf7bbe5812f9d99ffa0bb2a109f",
            "id": "2750ddf7-bbe5-812f-9d99-ffa0bb2a109f",
            "highlight": "Accuracy: Superior\nBarrel_Life_rounds: 400\nCaliber_Length: 16\"/50\nMuzzle_Velocity_fps: 2700\nNation: 🇷🇺 Soviet\nPerformance_Category: High Velocity\nPeriod: Planned 1938-1941\nUpgrade_Features: Maximum theoretical range 45600m\nUpgrade_Type: Standard"
        },
        {
            "title": "16\"/45 Mark 6 Mod 1",
            "url": "https://www.notion.so/2750ddf7bbe5819bb394ca25a9b2a0d2",
            "id": "2750ddf7-bbe5-819b-b394-ca25a9b2a0d2",
            "highlight": "Accuracy: Enhanced\nBarrel_Life_rounds: 350\nCaliber_Length: 16\"/45\nMuzzle_Velocity_fps: 2350\nNation: 🇺🇸 United States\nPerformance_Category: Long Life\nPeriod: 1943-1945\nUpgrade_Features: Improved powder, better performance\nUpgrade_Type: Enhanced Metallurgy"
        }
    ]

    # Process the data
    print("Processing shell data...")
    matcher.add_shell_data(shell_data)

    print("Processing gun data...")
    matcher.add_gun_data(gun_data)

    # Generate matches
    print("\nGenerating caliber and nation-specific matches...")
    matches = matcher.generate_all_matches()

    # Print results
    matcher.print_summary()

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

    # Save results
    matcher.save_results("shell_gun_matching_analysis.json")

    print("\nMatching analysis complete!")
    print("Ready to apply matches to Notion databases.")

if __name__ == "__main__":
    main()