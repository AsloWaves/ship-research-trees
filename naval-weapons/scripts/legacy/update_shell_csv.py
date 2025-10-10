import csv

# Read the CSV file
input_file = 'D:/Research/Shell Specifications Database 882bda05f300440084c5b62c88cf9c33_all.csv'
output_file = 'D:/Research/Shell_Specifications_Updated.csv'

rows = []
with open(input_file, 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames

    for row in reader:
        # Extract values
        caliber = row['Caliber']
        mark = row['Mark_Designation']
        shell_type = row['Type']

        # Clean up caliber - remove existing mark and type if present
        # Remove everything after the first space or after quotes
        if '"' in caliber:
            # Extract just the caliber measurement
            import re
            # Match patterns like 16.5", 15", 8", 2-pounder
            match = re.match(r'^([0-9.]+"|[0-9.]+-pounder)', caliber)
            if match:
                base_caliber = match.group(1)
            else:
                base_caliber = caliber.split()[0] if ' ' in caliber else caliber
        else:
            base_caliber = caliber.split()[0] if ' ' in caliber else caliber

        # Build the new caliber format: caliber + mark + type
        new_caliber = f'{base_caliber} {mark} {shell_type}'

        # Update the row
        row['Caliber'] = new_caliber
        rows.append(row)

# Write the updated CSV
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"Updated {len(rows)} rows")
print(f"Output saved to: {output_file}")