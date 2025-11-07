
## BRITISH GUN-AMMUNITION COMPATIBILITY TABLE

**Format**: SQL-ready markdown table for import

| Compatibility_ID | Gun_ID | Ammunition_ID | Notes | Caliber | Muzzle_Velocity_FPS | Muzzle_Velocity_MPS | Max_Range_Yards | Barrel_Wear_Per_Round |
|------------------|--------|---------------|-------|---------|---------------------|---------------------|-----------------|-----------------------|
| 10001 | 502 | 101 | 15"/42 Mark I + 4crh AP shell, standard charge (428 lbs cordite) | 15" | 2450.0 | 746.8 | 33550.0 |  |
| 10002 | 502 | 102 | 15"/42 Mark I + 6crh AP shell, supercharge (490 lbs cordite) | 15" | 2640.0 | 804.7 | 37870.0 |  |
| 10003 | 502 | 103 | 15"/42 Mark I + Mark XIIIa APC (6crh + 4crh ballistic cap), supercharge | 15" | 2640.0 | 804.7 | 37870.0 |  |
| 10004 | 502 | 104 | 15"/42 Mark I + Mark XVIIb APC (superior penetration, Cardonald manufacture) | 15" | 2640.0 | 804.7 | 37870.0 |  |
| 10005 | 502 | 105 | 15"/42 Mark I + HE shell, standard charge | 15" | 2450.0 | 746.8 | 33550.0 |  |
| 10006 | 502 | 106 | 15"/42 Mark I + CPC (Common Pointed Capped - semi-AP), standard charge | 15" | 2450.0 | 746.8 | 33550.0 |  |
| 10007 | 504 | 110 | 14"/45 Mark VII + Mark VIIB APC shell (338.3 lbs cordite, 39.8 lbs bursting charge) | 14" | 2483.0 | 756.8 | 36000.0 |  |
| 10008 | 504 | 111 | 14"/45 Mark VII + HE shell (338.3 lbs cordite, 107 lbs explosive) | 14" | 2400.0 | 731.5 | 36000.0 |  |

**Total Records**: 8

**Notes**:
- Compatibility_ID starts at 10001 (British range)
- Muzzle_Velocity_MPS calculated from FPS (×0.3048)
- Max_Range_Yards based on historical data and estimated elevation
- Barrel_Wear_Per_Round optional (not yet researched)

**Status**: [OK] Ready for SQL import


## SQL INSERT STATEMENTS (Optional)

```sql
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10001, 502, 101, '15"/42 Mark I + 4crh AP shell, standard charge (428 lbs cordite)', '15"', 2450.0, 746.8, 33550.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10002, 502, 102, '15"/42 Mark I + 6crh AP shell, supercharge (490 lbs cordite)', '15"', 2640.0, 804.7, 37870.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10003, 502, 103, '15"/42 Mark I + Mark XIIIa APC (6crh + 4crh ballistic cap), supercharge', '15"', 2640.0, 804.7, 37870.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10004, 502, 104, '15"/42 Mark I + Mark XVIIb APC (superior penetration, Cardonald manufacture)', '15"', 2640.0, 804.7, 37870.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10005, 502, 105, '15"/42 Mark I + HE shell, standard charge', '15"', 2450.0, 746.8, 33550.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10006, 502, 106, '15"/42 Mark I + CPC (Common Pointed Capped - semi-AP), standard charge', '15"', 2450.0, 746.8, 33550.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10007, 504, 110, '14"/45 Mark VII + Mark VIIB APC shell (338.3 lbs cordite, 39.8 lbs bursting charge)', '14"', 2483.0, 756.8, 36000.0);
INSERT INTO Gun_Ammunition_Compatibility (Compatibility_ID, Gun_ID, Ammunition_ID, Notes, Caliber, Muzzle_Velocity_FPS, Muzzle_Velocity_MPS, Max_Range_Yards)
  VALUES (10008, 504, 111, '14"/45 Mark VII + HE shell (338.3 lbs cordite, 107 lbs explosive)', '14"', 2400.0, 731.5, 36000.0);
```

