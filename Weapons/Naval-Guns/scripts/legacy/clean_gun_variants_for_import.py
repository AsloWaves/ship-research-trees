import csv
import re

print("Creating clean Gun Variants database for Notion import...")

def clean_shell_reference(shell_reference):
    """Remove URLs from shell references, keeping only shell names"""
    if '(https://' in shell_reference and ')' in shell_reference:
        # Extract shell name (everything before the URL)
        shell_name = shell_reference.split(' (https://')[0].strip()
        return shell_name
    else:
        # No URL, return as is
        return shell_reference.strip()

# Read and clean gun variants
gun_rows = []
shells_cleaned = 0
total_guns = 0

with open('D:/Research/Complete_Gun_Variants_Database.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        total_guns += 1
        compatible_shells = row.get('Compatible_Shells', '')

        if compatible_shells:
            # Split shell references and clean them
            shell_parts = compatible_shells.split(', ')
            cleaned_shells = []

            for shell_part in shell_parts:
                original_shell = shell_part.strip()
                cleaned_shell = clean_shell_reference(original_shell)

                if cleaned_shell != original_shell:
                    shells_cleaned += 1

                cleaned_shells.append(cleaned_shell)

            # Update the row with cleaned shell names (no URLs)
            row['Compatible_Shells'] = ', '.join(cleaned_shells)

        gun_rows.append(row)

# Write clean database
output_file = 'D:/Research/Gun_Variants_Clean_For_Import.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(gun_rows)

print(f"\nClean Database Summary:")
print(f"  Total gun variants: {total_guns}")
print(f"  Shell URLs removed: {shells_cleaned}")
print(f"  Shell names preserved: Yes")
print(f"  Ready for Notion import: Yes")
print(f"\nClean database saved to: {output_file}")
print(f"\nThis file contains only shell names without URLs.")
print(f"After importing, you can manually link shells in Notion.")