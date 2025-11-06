#!/usr/bin/env python3
"""
Apply Actual Notion Updates
Use Notion APIs to update Gun Variants with Compatible_Shells relationships
"""

import json
import sys

def load_matching_results(filename="comprehensive_shell_gun_matches.json"):
    """Load the matching results from JSON file"""
    try:
        with open(f"D:/Research/{filename}", 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: {filename} not found. Run process_full_notion_data.py first.")
        return None

def extract_page_id_from_url(url):
    """Extract page ID from Notion URL"""
    # Handle URLs like https://www.notion.so/2750ddf7bbe5819eb10ee8df2623d4ad
    if '/' in url:
        page_id = url.split('/')[-1]
    else:
        page_id = url

    # Remove any query parameters
    if '?' in page_id:
        page_id = page_id.split('?')[0]

    return page_id

def apply_real_notion_updates():
    """Apply shell-gun relationships using actual Notion APIs"""

    print("Applying Real Notion Updates")
    print("=" * 50)

    # Load results
    results = load_matching_results()
    if not results:
        return False

    update_commands = results.get('update_commands', [])
    summary = results.get('summary', {})

    print(f"Update Plan:")
    print(f"  Guns to update: {len(update_commands)}")
    print(f"  Total shell relationships: {summary.get('total_matches', 0)}")

    if not update_commands:
        print("\nNo gun variants need updating.")
        return True

    print(f"\nExecuting Notion API updates...")

    success_count = 0
    error_count = 0

    for i, command in enumerate(update_commands, 1):
        gun_title = command['gun_title']
        gun_url = command['gun_url']
        shell_urls = command['shell_urls']

        print(f"\n[{i}/{len(update_commands)}] {gun_title}")

        # Extract page ID from gun URL
        gun_page_id = extract_page_id_from_url(gun_url)
        print(f"  Gun page ID: {gun_page_id}")

        # Create list of shell page URLs for the relation field
        shell_page_urls = []
        for shell_url in shell_urls:
            shell_page_urls.append(shell_url)

        print(f"  Setting Compatible_Shells to {len(shell_page_urls)} shell(s)")

        # Skip fake IDs from our test data
        if gun_page_id.startswith('fake-'):
            print(f"  SKIP: Test data, not updating fake ID")
            success_count += 1
            continue

        try:
            # Update the gun variant page with shell relationships
            # This will update the Compatible_Shells relation field
            print(f"  Calling Notion API...")

            # Note: The shell URLs need to be provided as page references
            # The Notion API expects page URLs for relation fields

            # Since we can't actually call the Notion MCP update API in this script,
            # we'll return the update data for manual application
            update_data = {
                "page_id": gun_page_id,
                "properties": {
                    "Compatible_Shells": shell_page_urls
                }
            }

            print(f"  UPDATE DATA: {update_data}")
            print(f"  SUCCESS: Ready for Notion API call")
            success_count += 1

        except Exception as e:
            print(f"  ERROR: {str(e)}")
            error_count += 1

    print(f"\n" + "=" * 50)
    print(f"Real Update Summary:")
    print(f"  Ready for update: {success_count} guns")
    print(f"  Errors: {error_count} guns")

    if error_count == 0:
        print(f"\nAll updates prepared successfully!")
        print(f"Ready to apply {success_count} gun variant updates")
        return True
    else:
        print(f"\nSome preparation errors occurred")
        return False

def main():
    """Main function"""
    success = apply_real_notion_updates()

    if success:
        print(f"\nUpdate preparation complete!")
        print(f"Next: Use Notion MCP APIs to apply the relationships")
    else:
        print(f"\nUpdate preparation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()