"""Quick Japanese Ammunition Generation - 100 types (IDs 400-499)"""
import json

ammunition = []
ammo_id = 400

# Historical ammunition (30 types)
historical = [
    {'cal': '46cm', 'mark': 'Type 91 AP', 'type': 'APC', 'wt': 3219, 'notes': '46cm Type 91 AP shell, 1,460 kg, Yamato'},
    {'cal': '46cm', 'mark': 'Type 91 Sanshiki', 'type': 'AAC', 'wt': 2998, 'notes': '46cm Sanshiki AA shell, beehive round'},
    {'cal': '46cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 3197, 'notes': '46cm HE shell, 1,450 kg'},
    {'cal': '41cm', 'mark': 'Type 88 AP', 'type': 'APC', 'wt': 2249, 'notes': '41cm Type 88 AP shell, Nagato'},
    {'cal': '41cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 2182, 'notes': '41cm HE shell, 990 kg'},
    {'cal': '36cm', 'mark': 'Type 91 AP', 'type': 'APC', 'wt': 1485, 'notes': '36cm Type 91 AP shell, Kongo'},
    {'cal': '36cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 1455, 'notes': '36cm HE shell, 660 kg'},
    {'cal': '20.3cm', 'mark': 'Type 91 AP', 'type': 'APC', 'wt': 277, 'notes': '20.3cm Type 91 AP, heavy cruisers'},
    {'cal': '20.3cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 274, 'notes': '20.3cm HE shell'},
    {'cal': '15.5cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 123, 'notes': '15.5cm HE shell, Mogami'},
    {'cal': '15.5cm', 'mark': 'Type 91 AP', 'type': 'AP', 'wt': 123, 'notes': '15.5cm AP shell'},
    {'cal': '15cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 100, 'notes': '15cm HE shell'},
    {'cal': '14cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 84, 'notes': '14cm HE shell'},
    {'cal': '12.7cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 51.7, 'notes': '12.7cm HE shell, destroyers'},
    {'cal': '12.7cm', 'mark': 'Type 0 AAC', 'type': 'AAC', 'wt': 50.7, 'notes': '12.7cm AA common shell'},
    {'cal': '12.7cm', 'mark': 'Type 91 AP', 'type': 'AP', 'wt': 51.7, 'notes': '12.7cm AP shell'},
    {'cal': '12cm', 'mark': 'Type 0 HE', 'type': 'HE', 'wt': 45, 'notes': '12cm HE shell'},
    {'cal': '10cm', 'mark': 'Type 98 HE', 'type': 'HE', 'wt': 28.7, 'notes': '10cm HE shell, Akizuki'},
    {'cal': '10cm', 'mark': 'Type 98 AAC', 'type': 'AAC', 'wt': 28.7, 'notes': '10cm AA common shell'},
    {'cal': '8cm', 'mark': 'Type 98 HE', 'type': 'HE', 'wt': 13.2, 'notes': '8cm HE shell'},
    {'cal': '7.7cm', 'mark': 'Type 88 HE', 'type': 'HE', 'wt': 13.2, 'notes': '7.7cm HE shell'},
    {'cal': '25mm', 'mark': 'Type 96 HE', 'type': 'HE', 'wt': 0.55, 'notes': '25mm HE shell'},
    {'cal': '25mm', 'mark': 'Type 96 AP-T', 'type': 'AP', 'wt': 0.55, 'notes': '25mm AP tracer'},
    {'cal': '13.2mm', 'mark': 'Type 93 Ball', 'type': 'Ball', 'wt': 0.11, 'notes': '13.2mm ball round'},
    {'cal': '13.2mm', 'mark': 'Type 93 AP', 'type': 'AP', 'wt': 0.11, 'notes': '13.2mm AP round'},
    {'cal': '46cm', 'mark': 'Practice', 'type': 'Practice', 'wt': 3219, 'notes': '46cm practice shell'},
    {'cal': '41cm', 'mark': 'Practice', 'type': 'Practice', 'wt': 2249, 'notes': '41cm practice shell'},
    {'cal': '36cm', 'mark': 'Practice', 'type': 'Practice', 'wt': 1485, 'notes': '36cm practice shell'},
    {'cal': '20.3cm', 'mark': 'Practice', 'type': 'Practice', 'wt': 277, 'notes': '20.3cm practice shell'},
    {'cal': '15.5cm', 'mark': 'Practice', 'type': 'Practice', 'wt': 123, 'notes': '15.5cm practice shell'},
]

for ammo in historical:
    ammunition.append({
        'ID': ammo_id, 'Caliber': ammo['cal'], 'Mark_Designation': ammo['mark'],
        'Projectile_Type': ammo['type'], 'Weight_LBS': ammo['wt'], 'Country': 'Japan',
        'Modded': 0, 'Notes': ammo['notes']
    })
    ammo_id += 1

# Fictional ammunition (70 types)
fictional_cals = ['51cm','50cm','48cm','45cm','43cm','40cm','38cm','35cm','33cm','30.5cm','30cm','28cm',
                  '25.4cm','24cm','23cm','22cm','21cm','19cm','18cm','17cm','16cm','13.5cm','13cm',
                  '11.5cm','11cm','9.5cm','9cm','7.6cm','7.5cm','6cm','5cm','4.7cm','45mm','40mm','37mm']

count = 0
for cal in fictional_cals:
    if count >= 70:
        break
    cal_val = float(cal.replace('cm','').replace('mm',''))
    if 'mm' in cal:
        est_wt = cal_val * 0.02
    else:
        est_wt = (cal_val ** 2) * 8

    # Large calibers get AP+HE
    if cal_val >= 15 or (cal_val < 5 and 'cm' in cal):
        ammunition.extend([
            {'ID': ammo_id, 'Caliber': cal, 'Mark_Designation': 'Type 5 AP', 'Projectile_Type': 'APC',
             'Weight_LBS': round(est_wt, 2), 'Country': 'Japan', 'Modded': 1, 'Notes': f'{cal} Type 5 AP shell'},
            {'ID': ammo_id+1, 'Caliber': cal, 'Mark_Designation': 'Type 5 HE', 'Projectile_Type': 'HE',
             'Weight_LBS': round(est_wt*0.95, 2), 'Country': 'Japan', 'Modded': 1, 'Notes': f'{cal} Type 5 HE shell'}
        ])
        ammo_id += 2
        count += 2
    else:
        ammunition.append({
            'ID': ammo_id, 'Caliber': cal, 'Mark_Designation': 'Type 5 HE', 'Projectile_Type': 'HE',
            'Weight_LBS': round(est_wt, 2), 'Country': 'Japan', 'Modded': 1, 'Notes': f'{cal} Type 5 HE shell'
        })
        ammo_id += 1
        count += 1

# Save
with open('../../data/japanese_ammunition.json', 'w', encoding='utf-8') as f:
    json.dump(ammunition, f, indent=2)

print(f"Generated {len(ammunition)} Japanese ammunition types (IDs 400-{ammo_id-1})")
print(f"Historical: 30, Fictional: {len(ammunition)-30}")
print("READY FOR TURRET GENERATION")
