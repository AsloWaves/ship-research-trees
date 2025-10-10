"""
Generate comprehensive fictional British ammunition
Creative Mark designations following Royal Navy conventions
"""

# Fictional ammunition generation - comprehensive variants
fictional_ammunition = [

    # ===== 18"/40 MARK I (Gun_ID 501) - HMS FURIOUS =====
    # Super-Heavy penetration variant
    {
        'Ammunition_ID': 134,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 3800.0,
        'Muzzle_Velocity_FPS': 2100.0,
        'Max_Range_Yards': 27000.0,
        'Notes': '18"/40 Mark IIa "Dreadnought" APC - super-heavy penetration shell, sacrifices velocity for mass',
        'Modded': 1
    },
    # High-velocity variant
    {
        'Ammunition_ID': 135,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 2900.0,
        'Muzzle_Velocity_FPS': 2600.0,
        'Max_Range_Yards': 32000.0,
        'Notes': '18"/40 Mark IIb "Thunderer" HV-APC - high-velocity variant, flatter trajectory',
        'Modded': 1
    },
    # Experimental maximum charge
    {
        'Ammunition_ID': 136,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 3320.0,
        'Muzzle_Velocity_FPS': 2550.0,
        'Max_Range_Yards': 38500.0,
        'Notes': '18"/40 Mark III Experimental - maximum charge (750 lbs cordite), extreme range',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 137,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 3200.0,
        'Muzzle_Velocity_FPS': 2300.0,
        'Max_Range_Yards': 29500.0,
        'Notes': '18"/40 Mark IV HE/HC - high-capacity explosive, 550 lbs bursting charge',
        'Modded': 1
    },
    # Late-war improvement
    {
        'Ammunition_ID': 138,
        'Gun_ID': 501,
        'Caliber': '18"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 3320.0,
        'Muzzle_Velocity_FPS': 2420.0,
        'Max_Range_Yards': 37200.0,
        'Notes': '18"/40 Mark Va APCBC - late-war ballistic cap, improved penetration at range',
        'Modded': 1
    },

    # ===== 16"/45 MARK I (Gun_ID 503) - NELSON/RODNEY =====
    # Super-heavy
    {
        'Ammunition_ID': 139,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 2400.0,
        'Muzzle_Velocity_FPS': 2350.0,
        'Max_Range_Yards': 33500.0,
        'Notes': '16"/45 Mark IIa "Nelson Heavy" APC - super-heavy shell, improved penetration',
        'Modded': 1
    },
    # Improved (fix barrel wear issue)
    {
        'Ammunition_ID': 140,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 2048.0,
        'Muzzle_Velocity_FPS': 2700.0,
        'Max_Range_Yards': 38000.0,
        'Notes': '16"/45 Mark IIb "Rodney Improved" - improved barrel lining, full velocity without wear',
        'Modded': 1
    },
    # High-velocity light
    {
        'Ammunition_ID': 141,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 1800.0,
        'Muzzle_Velocity_FPS': 2850.0,
        'Max_Range_Yards': 40000.0,
        'Notes': '16"/45 Mark III "Velocity" - lightweight high-velocity shell, extreme range',
        'Modded': 1
    },
    # APCBC late-war
    {
        'Ammunition_ID': 142,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 2048.0,
        'Muzzle_Velocity_FPS': 2525.0,
        'Max_Range_Yards': 35500.0,
        'Notes': '16"/45 Mark IVa APCBC - late-war ballistic cap design, better penetration',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 143,
        'Gun_ID': 503,
        'Caliber': '16"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 2000.0,
        'Muzzle_Velocity_FPS': 2550.0,
        'Max_Range_Yards': 35200.0,
        'Notes': '16"/45 Mark V HE/HC - high-capacity explosive, 320 lbs bursting charge',
        'Modded': 1
    },

    # ===== 15"/42 MARK I (Gun_ID 502) - QUEEN ELIZABETH/HOOD/VANGUARD =====
    # Super-heavy
    {
        'Ammunition_ID': 144,
        'Gun_ID': 502,
        'Caliber': '15"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 2100.0,
        'Muzzle_Velocity_FPS': 2500.0,
        'Max_Range_Yards': 36000.0,
        'Notes': '15"/42 Mark XVIII "Jutland" APC - super-heavy shell, maximum penetration',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 145,
        'Gun_ID': 502,
        'Caliber': '15"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1750.0,
        'Muzzle_Velocity_FPS': 2750.0,
        'Max_Range_Yards': 39000.0,
        'Notes': '15"/42 Mark XIX "Hood" HV-APC - high-velocity light shell, long range',
        'Modded': 1
    },
    # Post-war experimental
    {
        'Ammunition_ID': 146,
        'Gun_ID': 502,
        'Caliber': '15"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 1938.0,
        'Muzzle_Velocity_FPS': 2680.0,
        'Max_Range_Yards': 38200.0,
        'Notes': '15"/42 Mark XXa "Vanguard Experimental" - post-war superior ballistic cap',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 147,
        'Gun_ID': 502,
        'Caliber': '15"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 1900.0,
        'Muzzle_Velocity_FPS': 2480.0,
        'Max_Range_Yards': 34000.0,
        'Notes': '15"/42 Mark XXI HE/HC - high-capacity explosive, 280 lbs bursting charge',
        'Modded': 1
    },

    # ===== 14"/45 MARK VII (Gun_ID 504) - KING GEORGE V =====
    # Super-heavy
    {
        'Ammunition_ID': 148,
        'Gun_ID': 504,
        'Caliber': '14"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1750.0,
        'Muzzle_Velocity_FPS': 2350.0,
        'Max_Range_Yards': 34500.0,
        'Notes': '14"/45 Mark VIIIa "King George" APC - super-heavy variant, improved penetration',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 149,
        'Gun_ID': 504,
        'Caliber': '14"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1450.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 38000.0,
        'Notes': '14"/45 Mark VIIIb HV-APC - high-velocity shell, extended range',
        'Modded': 1
    },
    # Late-war APCBC
    {
        'Ammunition_ID': 150,
        'Gun_ID': 504,
        'Caliber': '14"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 1590.0,
        'Muzzle_Velocity_FPS': 2483.0,
        'Max_Range_Yards': 36500.0,
        'Notes': '14"/45 Mark IXa APCBC - late-war improved ballistic cap, superior penetration',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 151,
        'Gun_ID': 504,
        'Caliber': '14"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 1580.0,
        'Muzzle_Velocity_FPS': 2450.0,
        'Max_Range_Yards': 36200.0,
        'Notes': '14"/45 Mark X HE/HC - high-capacity explosive, 130 lbs bursting charge',
        'Modded': 1
    },

    # ===== 13.5"/45 MARK V (Gun_ID 505) - WWI SUPERDREADNOUGHTS =====
    # Super-heavy
    {
        'Ammunition_ID': 152,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1550.0,
        'Muzzle_Velocity_FPS': 2400.0,
        'Max_Range_Yards': 23000.0,
        'Notes': '13.5"/45 Mark VI(SH) "Orion" - super-heavy post-Jutland design',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 153,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 1150.0,
        'Muzzle_Velocity_FPS': 2700.0,
        'Max_Range_Yards': 25500.0,
        'Notes': '13.5"/45 Mark VII HV - high-velocity interwar improvement',
        'Modded': 1
    },
    # Post-WWI improved
    {
        'Ammunition_ID': 154,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 1400.0,
        'Muzzle_Velocity_FPS': 2520.0,
        'Max_Range_Yards': 24200.0,
        'Notes': '13.5"/45 Mark VIII APCBC - 1920s ballistic cap retrofit, "Iron Duke Improved"',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 155,
        'Gun_ID': 505,
        'Caliber': '13.5"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 1250.0,
        'Muzzle_Velocity_FPS': 2600.0,
        'Max_Range_Yards': 24000.0,
        'Notes': '13.5"/45 Mark IX HE/HC - improved high-explosive, 180 lbs bursting charge',
        'Modded': 1
    },

    # ===== 12"/45 MARK X (Gun_ID 506) - HMS DREADNOUGHT =====
    # Super-heavy
    {
        'Ammunition_ID': 156,
        'Gun_ID': 506,
        'Caliber': '12"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 950.0,
        'Muzzle_Velocity_FPS': 2600.0,
        'Max_Range_Yards': 21500.0,
        'Notes': '12"/45 Mark XIa "Dreadnought Heavy" - super-heavy interwar variant',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 157,
        'Gun_ID': 506,
        'Caliber': '12"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 750.0,
        'Muzzle_Velocity_FPS': 2900.0,
        'Max_Range_Yards': 23000.0,
        'Notes': '12"/45 Mark XIb HV - high-velocity lightweight shell, 1920s design',
        'Modded': 1
    },
    # Interwar APCBC
    {
        'Ammunition_ID': 158,
        'Gun_ID': 506,
        'Caliber': '12"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 850.0,
        'Muzzle_Velocity_FPS': 2750.0,
        'Max_Range_Yards': 21000.0,
        'Notes': '12"/45 Mark XII APCBC - interwar ballistic cap modernization',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 159,
        'Gun_ID': 506,
        'Caliber': '12"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 850.0,
        'Muzzle_Velocity_FPS': 2750.0,
        'Max_Range_Yards': 20500.0,
        'Notes': '12"/45 Mark XIII HE/HC - improved high-explosive, 120 lbs bursting charge',
        'Modded': 1
    },

    # ===== 8"/50 MARK VIII (Gun_ID 520) - COUNTY-CLASS HEAVY CRUISERS =====
    # Super-heavy
    {
        'Ammunition_ID': 160,
        'Gun_ID': 520,
        'Caliber': '8"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 280.0,
        'Muzzle_Velocity_FPS': 2600.0,
        'Max_Range_Yards': 29000.0,
        'Notes': '8"/50 Mark IX "County" APC - heavy shell for improved penetration',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 161,
        'Gun_ID': 520,
        'Caliber': '8"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 230.0,
        'Muzzle_Velocity_FPS': 2900.0,
        'Max_Range_Yards': 32000.0,
        'Notes': '8"/50 Mark X HV - high-velocity shell, extended range for cruiser duels',
        'Modded': 1
    },
    # Late-war improved
    {
        'Ammunition_ID': 162,
        'Gun_ID': 520,
        'Caliber': '8"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 256.0,
        'Muzzle_Velocity_FPS': 2750.0,
        'Max_Range_Yards': 30500.0,
        'Notes': '8"/50 Mark XIa APCBC - late-war ballistic cap, "Kent Improved"',
        'Modded': 1
    },
    # Improved HE
    {
        'Ammunition_ID': 163,
        'Gun_ID': 520,
        'Caliber': '8"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 256.0,
        'Muzzle_Velocity_FPS': 2750.0,
        'Max_Range_Yards': 30200.0,
        'Notes': '8"/50 Mark XII HE/HC - improved high-explosive, 35 lbs bursting charge',
        'Modded': 1
    },

    # ===== 6"/50 MARK XXIII (Gun_ID 530) - CROWN COLONY LIGHT CRUISERS =====
    # Super-heavy
    {
        'Ammunition_ID': 164,
        'Gun_ID': 530,
        'Caliber': '6"',
        'Projectile_Type': 'APC',
        'Projectile_Weight_LBS': 125.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 24500.0,
        'Notes': '6"/50 Mark XXIVa "Fiji" APC - heavy shell for improved penetration',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 165,
        'Gun_ID': 530,
        'Caliber': '6"',
        'Projectile_Type': 'AP',
        'Projectile_Weight_LBS': 100.0,
        'Muzzle_Velocity_FPS': 2950.0,
        'Max_Range_Yards': 27000.0,
        'Notes': '6"/50 Mark XXIVb HV - high-velocity lightweight, extended range',
        'Modded': 1
    },
    # Late-war improved
    {
        'Ammunition_ID': 166,
        'Gun_ID': 530,
        'Caliber': '6"',
        'Projectile_Type': 'APCBC',
        'Projectile_Weight_LBS': 112.0,
        'Muzzle_Velocity_FPS': 2800.0,
        'Max_Range_Yards': 26000.0,
        'Notes': '6"/50 Mark XXVa APCBC - late-war ballistic cap design',
        'Modded': 1
    },
    # VT-fused HE
    {
        'Ammunition_ID': 167,
        'Gun_ID': 530,
        'Caliber': '6"',
        'Projectile_Type': 'HE-VT',
        'Projectile_Weight_LBS': 112.0,
        'Muzzle_Velocity_FPS': 2760.0,
        'Max_Range_Yards': 25480.0,
        'Notes': '6"/50 Mark XXVI HE-VT - proximity-fused HE for AA use, "Ceylon Special"',
        'Modded': 1
    },

    # ===== 5.25"/50 MARK I (Gun_ID 540) - KGV SECONDARY / DIDO-CLASS =====
    # VT-fused HE (primary improvement)
    {
        'Ammunition_ID': 168,
        'Gun_ID': 540,
        'Caliber': '5.25"',
        'Projectile_Type': 'HE-VT',
        'Projectile_Weight_LBS': 80.0,
        'Muzzle_Velocity_FPS': 2672.0,
        'Max_Range_Yards': 24070.0,
        'Notes': '5.25"/50 Mark II HE-VT - proximity-fused AA shell, "Dido Special"',
        'Modded': 1
    },
    # Improved SAP
    {
        'Ammunition_ID': 169,
        'Gun_ID': 540,
        'Caliber': '5.25"',
        'Projectile_Type': 'SAPC',
        'Projectile_Weight_LBS': 80.0,
        'Muzzle_Velocity_FPS': 2672.0,
        'Max_Range_Yards': 24070.0,
        'Notes': '5.25"/50 Mark IIIa SAPC - improved semi-armor-piercing with cap',
        'Modded': 1
    },
    # Experimental high-velocity
    {
        'Ammunition_ID': 170,
        'Gun_ID': 540,
        'Caliber': '5.25"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 70.0,
        'Muzzle_Velocity_FPS': 2850.0,
        'Max_Range_Yards': 26000.0,
        'Notes': '5.25"/50 Mark IV "King George" HV - experimental lightweight high-velocity',
        'Modded': 1
    },
    # Supercharge
    {
        'Ammunition_ID': 171,
        'Gun_ID': 540,
        'Caliber': '5.25"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 80.0,
        'Muzzle_Velocity_FPS': 2800.0,
        'Max_Range_Yards': 25500.0,
        'Notes': '5.25"/50 Mark Va Supercharge - overcharge for maximum range',
        'Modded': 1
    },

    # ===== 4.7"/45 MARK IX/XII (Gun_ID 545) - WWI/WWII DESTROYERS =====
    # VT-fused HE
    {
        'Ammunition_ID': 172,
        'Gun_ID': 545,
        'Caliber': '4.7"',
        'Projectile_Type': 'HE-VT',
        'Projectile_Weight_LBS': 50.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 16970.0,
        'Notes': '4.7"/45 Mark XIIIa HE-VT - proximity-fused AA shell, "Tribal Special"',
        'Modded': 1
    },
    # Improved SAP
    {
        'Ammunition_ID': 173,
        'Gun_ID': 545,
        'Caliber': '4.7"',
        'Projectile_Type': 'SAPC',
        'Projectile_Weight_LBS': 50.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 16970.0,
        'Notes': '4.7"/45 Mark XIVa SAPC - improved semi-armor-piercing with cap',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 174,
        'Gun_ID': 545,
        'Caliber': '4.7"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 45.0,
        'Muzzle_Velocity_FPS': 2800.0,
        'Max_Range_Yards': 18500.0,
        'Notes': '4.7"/45 Mark XV HV - high-velocity lightweight, extended range',
        'Modded': 1
    },
    # Late-war experimental
    {
        'Ammunition_ID': 175,
        'Gun_ID': 545,
        'Caliber': '4.7"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 50.0,
        'Muzzle_Velocity_FPS': 2750.0,
        'Max_Range_Yards': 17500.0,
        'Notes': '4.7"/45 Mark XVI "Battle" - late-war improved HE, Battle-class destroyers',
        'Modded': 1
    },

    # ===== 4.5"/45 MARK V (Gun_ID 550) - POST-WAR AUTOMATED DESTROYERS =====
    # VT-fused HE
    {
        'Ammunition_ID': 176,
        'Gun_ID': 550,
        'Caliber': '4.5"',
        'Projectile_Type': 'HE-VT',
        'Projectile_Weight_LBS': 55.0,
        'Muzzle_Velocity_FPS': 2449.0,
        'Max_Range_Yards': 20750.0,
        'Notes': '4.5"/45 Mark VIa HE-VT - proximity-fused AA shell, "Daring Special"',
        'Modded': 1
    },
    # Improved SAP
    {
        'Ammunition_ID': 177,
        'Gun_ID': 550,
        'Caliber': '4.5"',
        'Projectile_Type': 'SAPC',
        'Projectile_Weight_LBS': 55.0,
        'Muzzle_Velocity_FPS': 2449.0,
        'Max_Range_Yards': 20750.0,
        'Notes': '4.5"/45 Mark VIb SAPC - improved semi-armor-piercing with cap',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 178,
        'Gun_ID': 550,
        'Caliber': '4.5"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 48.0,
        'Muzzle_Velocity_FPS': 2650.0,
        'Max_Range_Yards': 22500.0,
        'Notes': '4.5"/45 Mark VII HV - high-velocity lightweight, 1950s design',
        'Modded': 1
    },
    # Experimental maximum
    {
        'Ammunition_ID': 179,
        'Gun_ID': 550,
        'Caliber': '4.5"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 55.0,
        'Muzzle_Velocity_FPS': 2550.0,
        'Max_Range_Yards': 21500.0,
        'Notes': '4.5"/45 Mark VIII Experimental - automated loading optimized, maximum ROF',
        'Modded': 1
    },

    # ===== 4"/45 QF MARK V/XVI (Gun_ID 555) - PRIMARY AA GUN =====
    # VT-fused HE (most important)
    {
        'Ammunition_ID': 180,
        'Gun_ID': 555,
        'Caliber': '4"',
        'Projectile_Type': 'HE-VT',
        'Projectile_Weight_LBS': 35.0,
        'Muzzle_Velocity_FPS': 2660.0,
        'Max_Range_Yards': 19850.0,
        'Notes': '4"/45 QF Mark XVII HE-VT - proximity-fused AA shell, superior AA performance',
        'Modded': 1
    },
    # Improved SAP
    {
        'Ammunition_ID': 181,
        'Gun_ID': 555,
        'Caliber': '4"',
        'Projectile_Type': 'SAPC',
        'Projectile_Weight_LBS': 40.0,
        'Muzzle_Velocity_FPS': 2600.0,
        'Max_Range_Yards': 19500.0,
        'Notes': '4"/45 QF Mark XVIIIa SAPC - improved semi-armor-piercing with cap',
        'Modded': 1
    },
    # High-velocity
    {
        'Ammunition_ID': 182,
        'Gun_ID': 555,
        'Caliber': '4"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 31.0,
        'Muzzle_Velocity_FPS': 2800.0,
        'Max_Range_Yards': 21000.0,
        'Notes': '4"/45 QF Mark XIX HV - high-velocity lightweight for AA use',
        'Modded': 1
    },
    # Late-war improved
    {
        'Ammunition_ID': 183,
        'Gun_ID': 555,
        'Caliber': '4"',
        'Projectile_Type': 'HE',
        'Projectile_Weight_LBS': 35.0,
        'Muzzle_Velocity_FPS': 2700.0,
        'Max_Range_Yards': 20200.0,
        'Notes': '4"/45 QF Mark XXa "Carlisle" - improved HE, better fragmentation pattern',
        'Modded': 1
    },
]

# Calculate Muzzle_Velocity_MPS from FPS
for record in fictional_ammunition:
    record['Muzzle_Velocity_MPS'] = round(record['Muzzle_Velocity_FPS'] * 0.3048, 1)

print("=" * 80)
print("BRITISH FICTIONAL AMMUNITION GENERATION")
print("=" * 80)
print()
print(f"Total fictional ammunition: {len(fictional_ammunition)}")
print()

# Count by gun
gun_counts = {}
for ammo in fictional_ammunition:
    gun_id = ammo['Gun_ID']
    if gun_id not in gun_counts:
        gun_counts[gun_id] = 0
    gun_counts[gun_id] += 1

print("Fictional ammunition by gun:")
gun_names = {
    501: '18"/40 Mark I',
    502: '15"/42 Mark I',
    503: '16"/45 Mark I',
    504: '14"/45 Mark VII',
    505: '13.5"/45 Mark V',
    506: '12"/45 Mark X',
    520: '8"/50 Mark VIII',
    530: '6"/50 Mark XXIII',
    540: '5.25"/50 Mark I',
    545: '4.7"/45 Mark IX/XII',
    550: '4.5"/45 Mark V',
    555: '4"/45 QF Mark V/XVI'
}

for gun_id in sorted(gun_counts.keys()):
    print(f"  Gun {gun_id} ({gun_names[gun_id]:25s}): {gun_counts[gun_id]:2d} fictional types")

print()

# Count by type
type_counts = {}
for ammo in fictional_ammunition:
    ptype = ammo['Projectile_Type']
    if ptype not in type_counts:
        type_counts[ptype] = 0
    type_counts[ptype] += 1

print("Fictional ammunition by projectile type:")
for ptype in sorted(type_counts.keys()):
    print(f"  {ptype:10s}: {type_counts[ptype]:2d} types")

print()
print("=" * 80)
print("AMMUNITION TABLE (SQL-READY)")
print("=" * 80)
print()

# Print ammunition table
print("| Ammunition_ID | Gun_ID | Caliber | Projectile_Type | Weight (lbs) | Muzzle_Velocity_FPS | Muzzle_Velocity_MPS | Max_Range_Yards | Modded | Notes |")
print("|---------------|--------|---------|-----------------|--------------|---------------------|---------------------|-----------------|--------|-------|")

for ammo in fictional_ammunition:
    print(f"| {ammo['Ammunition_ID']:3d} | {ammo['Gun_ID']:3d} | {ammo['Caliber']:6s} | {ammo['Projectile_Type']:10s} | {ammo['Projectile_Weight_LBS']:8.1f} | {ammo['Muzzle_Velocity_FPS']:8.1f} | {ammo['Muzzle_Velocity_MPS']:8.1f} | {ammo['Max_Range_Yards']:8.0f} | {ammo['Modded']:1d} | {ammo['Notes']} |")

print()
print("=" * 80)
print("COMPATIBILITY RECORDS GENERATION")
print("=" * 80)
print()

# Generate compatibility records
compat_id_start = 10031  # Continue from existing 30 records (10001-10030)

print("| Compatibility_ID | Gun_ID | Ammunition_ID | Caliber | Muzzle_Velocity_FPS | Muzzle_Velocity_MPS | Max_Range_Yards | Notes |")
print("|------------------|--------|---------------|---------|---------------------|---------------------|-----------------|-------|")

compatibility_records = []
for i, ammo in enumerate(fictional_ammunition):
    compat_id = compat_id_start + i
    compatibility_records.append({
        'Compatibility_ID': compat_id,
        'Gun_ID': ammo['Gun_ID'],
        'Ammunition_ID': ammo['Ammunition_ID'],
        'Caliber': ammo['Caliber'],
        'Muzzle_Velocity_FPS': ammo['Muzzle_Velocity_FPS'],
        'Muzzle_Velocity_MPS': ammo['Muzzle_Velocity_MPS'],
        'Max_Range_Yards': ammo['Max_Range_Yards'],
        'Notes': ammo['Notes']
    })

    print(f"| {compat_id:5d} | {ammo['Gun_ID']:3d} | {ammo['Ammunition_ID']:3d} | {ammo['Caliber']:6s} | {ammo['Muzzle_Velocity_FPS']:8.1f} | {ammo['Muzzle_Velocity_MPS']:8.1f} | {ammo['Max_Range_Yards']:8.0f} | {ammo['Notes'][:60]}... |")

print()
print(f"Total compatibility records: {len(compatibility_records)}")
print(f"Compatibility ID range: {compat_id_start}-{compat_id_start + len(compatibility_records) - 1}")
print()

print("=" * 80)
print("SQL INSERT STATEMENTS")
print("=" * 80)
print()

print("-- FICTIONAL AMMUNITION INSERTS")
print()
for ammo in fictional_ammunition:
    notes_escaped = ammo['Notes'].replace("'", "''")
    print(f"INSERT INTO Ammunition (Ammunition_ID, Caliber, Projectile_Type, Projectile_Weight_LBS, Notes, Modded)")
    print(f"  VALUES ({ammo['Ammunition_ID']}, '{ammo['Caliber']}', '{ammo['Projectile_Type']}', {ammo['Projectile_Weight_LBS']}, '{notes_escaped}', {ammo['Modded']});")

print()
print("-- FICTIONAL COMPATIBILITY INSERTS")
print()
for compat in compatibility_records:
    notes_escaped = compat['Notes'].replace("'", "''")
    print(f"INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards, Notes)")
    print(f"  VALUES ({compat['Compatibility_ID']}, {compat['Gun_ID']}, {compat['Ammunition_ID']}, '{compat['Caliber']}', {compat['Muzzle_Velocity_FPS']}, {compat['Muzzle_Velocity_MPS']}, {compat['Max_Range_Yards']}, '{notes_escaped}');")

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print()
print(f"[OK] Fictional ammunition generated:     {len(fictional_ammunition)} types")
print(f"[OK] Fictional compatibility records:    {len(compatibility_records)} records")
print(f"[OK] Gun coverage:                        {len(gun_counts)}/12 guns ({len(gun_counts)*100//12}%)")
print()
print("COMBINED TOTALS (Historical + Fictional):")
print(f"  Historical ammunition:   30 types (IDs 101-133)")
print(f"  Fictional ammunition:    {len(fictional_ammunition)} types (IDs 134-183)")
print(f"  TOTAL AMMUNITION:        {30 + len(fictional_ammunition)} types")
print()
print(f"  Historical compatibility: 30 records (IDs 10001-10030)")
print(f"  Fictional compatibility:  {len(compatibility_records)} records (IDs 10031-{10031 + len(compatibility_records) - 1})")
print(f"  TOTAL COMPATIBILITY:      {30 + len(compatibility_records)} records")
print()
print("Status: COMPLETE - Ready for database import")
print()
