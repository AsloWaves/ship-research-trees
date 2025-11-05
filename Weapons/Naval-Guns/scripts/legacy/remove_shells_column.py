import csv

print("Removing Compatible_Shells column from Gun Variants database...")

# Read gun variants and exclude the Compatible_Shells column
gun_rows = []
new_headers = []

with open('D:/Research/Complete_Gun_Variants_Database.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    original_headers = reader.fieldnames

    # Create new headers without Compatible_Shells
    new_headers = [header for header in original_headers if header != 'Compatible_Shells']

    print(f"Original columns: {len(original_headers)}")
    print(f"New columns: {len(new_headers)}")
    print(f"Removed: Compatible_Shells")

    for row in reader:
        # Create new row without Compatible_Shells column
        new_row = {header: row[header] for header in new_headers}
        gun_rows.append(new_row)

# Write clean database without Compatible_Shells column
output_file = 'D:/Research/Gun_Variants_No_Shells_Column.csv'
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=new_headers)
    writer.writeheader()
    writer.writerows(gun_rows)

print(f"\nClean Database Summary:")
print(f"  Total gun variants: {len(gun_rows)}")
print(f"  Compatible_Shells column: REMOVED")
print(f"  Columns remaining: {len(new_headers)}")
print(f"  Ready for Notion import: Yes")
print(f"\nColumn list:")
for i, header in enumerate(new_headers, 1):
    print(f"  {i}. {header}")
print(f"\nClean database saved to: {output_file}")
print(f"\nYou can add the Compatible_Shells column manually in Notion after import.")