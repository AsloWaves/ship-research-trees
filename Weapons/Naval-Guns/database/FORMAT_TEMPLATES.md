# Database Format Templates

**Purpose**: Validation templates for all database tables
**Date**: October 2025
**Project**: Naval Weapons Research Database

---

## Table 1: Guns

### Schema
```
Gun_ID              INTEGER PRIMARY KEY (AUTO)
Turret_ID           INTEGER (nullable - usually NULL for guns)
Country             TEXT (REQUIRED)
Caliber             TEXT (REQUIRED)
Length              TEXT (REQUIRED - format: /XX like "/50")
Mark_Designation    TEXT (REQUIRED)
Year_Introduced     INTEGER (REQUIRED - 4-digit year)
Weight              REAL (REQUIRED - in tons)
Modded              INTEGER (REQUIRED - 0 or 1)
Notes               TEXT (REQUIRED - comprehensive)
```

### Template Format
```
Gun_ID: [501-600 range for Britain]
Turret_ID: NULL (guns don't reference turrets)
Country: "Britain"
Caliber: "[X]\"" or "[X.X]\"" (e.g., "15\"", "5.25\"")
Length: "/[XX]" (e.g., "/42", "/50")
Mark_Designation: "Mark [designation]" or "QF Mark [designation]"
Year_Introduced: [YYYY] (1890-1990 range for this project)
Weight: [XX.XX] (in long tons for British guns)
Modded: 0 (historical) or 1 (fictional)
Notes: "[Caliber]/[Length] ([cm]) [Mark] - [Description]. Ships: [ship list]. [Technical specs]. [Historical notes]. Source: [sources]"
```

### Example (Good)
```
Gun_ID: 502
Turret_ID: NULL
Country: Britain
Caliber: 15"
Length: /42
Mark_Designation: Mark I
Year_Introduced: 1915
Weight: 100.0
Modded: 0
Notes: 15"/42 (38.1 cm) Mark I - Most widely used and longest lasting British 15" design. Ships: Queen Elizabeth-class (5 ships), Revenge-class (5 ships), Renown-class (2 ships), HMS Hood, HMS Vanguard. In service 1915-1960. Rate of Fire: 2 rpm. Barrel Life: ~335 full charge firings. Shell weight: 1,938 lbs. Charge: 428 lbs cordite (std), 490 lbs (supercharge). Source: Wikipedia, NavWeaps, War Thunder Wiki, IWM
```

### Required Data Checklist
- [ ] Gun_ID assigned (501-555 for British)
- [ ] Country = "Britain"
- [ ] Caliber in format: X" or X.X"
- [ ] Length in format: /XX
- [ ] Mark_Designation present
- [ ] Year_Introduced (4-digit year)
- [ ] Weight in tons (estimated if exact unknown)
- [ ] Modded flag (0 or 1)
- [ ] Notes include: caliber/length, Mark, description, ships, specs, sources

---

## Table 2: Ammunition

### Schema
```
ID                  INTEGER PRIMARY KEY (AUTO)
Turret_ID           INTEGER (nullable - usually NULL for ammo)
Caliber             TEXT (REQUIRED)
Mark_Designation    TEXT (nullable - some ammo doesn't have marks)
Projectile_Type     TEXT (REQUIRED - AP, APC, APCBC, HE, CPC, SAP, etc.)
Weight_LBS          REAL (REQUIRED - projectile weight in pounds)
Length_IN           REAL (nullable - shell length in inches)
Bursting_Charge     REAL (nullable - explosive charge in pounds)
Kinetic_Energy_MJ   REAL (nullable - kinetic energy in megajoules)
Cartridge_Type      TEXT (nullable - fixed, separate, bagged, etc.)
Year_Introduced     INTEGER (nullable - when ammo introduced)
Country             TEXT (REQUIRED)
Modded              INTEGER (REQUIRED - 0 or 1)
Notes               TEXT (REQUIRED - comprehensive)
```

### Template Format
```
ID: [101-200 range for Britain]
Turret_ID: NULL (ammunition doesn't reference turrets)
Caliber: "[X]\"" (must match gun caliber)
Mark_Designation: "Mark [designation]" or NULL or "[descriptor]"
Projectile_Type: "AP" | "APC" | "APCBC" | "HE" | "CPC" | "SAP" | "VT"
Weight_LBS: [XXXX] (projectile weight in pounds)
Length_IN: [XX.X] (total length in inches, if known)
Bursting_Charge: [XX.X] (explosive charge in pounds, if applicable)
Kinetic_Energy_MJ: [XX.X] (if calculated/known)
Cartridge_Type: "Fixed" | "Separate" | "Bagged" | etc. (if known)
Year_Introduced: [YYYY] (if known)
Country: "Britain"
Modded: 0 (historical) or 1 (fictional)
Notes: "[Caliber] [Mark/descriptor] [Type] shell for [gun]. [Propellant details]. [Muzzle velocity]. [Range]. [Special notes]. Source: [sources]"
```

### Example (Good)
```
ID: 101
Turret_ID: NULL
Caliber: 15"
Mark_Designation: 4crh
Projectile_Type: AP
Weight_LBS: 1920
Length_IN: NULL
Bursting_Charge: NULL
Kinetic_Energy_MJ: NULL
Cartridge_Type: Bagged
Year_Introduced: NULL
Country: Britain
Modded: 0
Notes: Early 4crh (caliber radius head) AP shell for 15"/42 Mark I. Standard cordite charge 428 lbs. Muzzle Velocity: 2,450 fps. Used pre-1937 before 6crh improvements. crh = caliber radius head (ballistic cap shape). Source: NavWeaps, Wikipedia
```

### Required Data Checklist
- [ ] ID assigned (101-200 for British)
- [ ] Country = "Britain"
- [ ] Caliber matches gun caliber format
- [ ] Projectile_Type specified (AP, APC, HE, etc.)
- [ ] Weight_LBS provided
- [ ] Modded flag (0 or 1)
- [ ] Notes include: caliber, type, gun compatibility, propellant, velocity, sources
- [ ] Optional fields filled where data available: Length_IN, Bursting_Charge, Cartridge_Type, Year_Introduced

---

## Table 3: Turrets

### Schema
```
Turret_ID               INTEGER PRIMARY KEY (AUTO)
Gun_ID                  INTEGER (REQUIRED - foreign key to Guns)
Country                 TEXT (REQUIRED)
Caliber                 TEXT (REQUIRED - denormalized for performance)
Turret_Type             TEXT (REQUIRED - Single, Twin, Triple, Quad)
Designation             TEXT (REQUIRED - descriptive name)
Turret_Weight_Tons      REAL (REQUIRED - in tons)
Crew_Size               INTEGER (REQUIRED)
Armor_Face_IN           REAL (REQUIRED - face armor in inches)
Armor_Sides_IN          REAL (REQUIRED - side armor in inches)
Armor_Roof_IN           REAL (REQUIRED - roof armor in inches)
Traverse_Rate_Deg_Sec   REAL (REQUIRED - degrees per second)
Elevation_Min_Deg       REAL (REQUIRED - minimum elevation in degrees)
Elevation_Max_Deg       REAL (REQUIRED - maximum elevation in degrees)
Elevation_Rate_Deg_Sec  REAL (nullable - degrees per second)
Rate_Of_Fire_RPM        REAL (REQUIRED - rounds per minute)
Modded                  INTEGER (REQUIRED - 0 or 1)
Notes                   TEXT (REQUIRED)
```

### Template Format
```
Turret_ID: [2001-2200 range for Britain]
Gun_ID: [501-555] (must match existing gun)
Country: "Britain"
Caliber: "[X]\"" (must match Gun_ID's caliber)
Turret_Type: "Single" | "Twin" | "Triple" | "Quad"
Designation: "[Caliber] Mark [X] [Type]" or descriptive name
Turret_Weight_Tons: [XXX.X] (in tons)
Crew_Size: [XX] (crew members)
Armor_Face_IN: [XX.X] (face armor in inches)
Armor_Sides_IN: [XX.X] (side armor in inches)
Armor_Roof_IN: [XX.X] (roof armor in inches)
Traverse_Rate_Deg_Sec: [X.X] (degrees per second)
Elevation_Min_Deg: [-XX] (negative for depression)
Elevation_Max_Deg: [+XX] (positive for elevation)
Elevation_Rate_Deg_Sec: [X.X] (if known, NULL if unknown)
Rate_Of_Fire_RPM: [X.X] (rounds per minute)
Modded: 0 (historical) or 1 (fictional)
Notes: "HISTORICAL - [details]" or "Fictional - [notes]. Shell: [weight] lbs. [Additional specs]"
```

### Example (Good - Historical)
```
Turret_ID: 2012
Gun_ID: 502
Country: Britain
Caliber: 15"
Turret_Type: Twin
Designation: 15"/42 Mark I Twin (1915)
Turret_Weight_Tons: 750
Crew_Size: 85
Armor_Face_IN: 15
Armor_Sides_IN: 10
Armor_Roof_IN: 6
Traverse_Rate_Deg_Sec: 2.0
Elevation_Min_Deg: -5
Elevation_Max_Deg: 20
Elevation_Rate_Deg_Sec: NULL
Rate_Of_Fire_RPM: 2.0
Modded: 0
Notes: HISTORICAL - Queen Elizabeth-class, Revenge-class. Shell: 1,938 lbs. Revolving weight: 750 tons.
```

### Example (Good - Fictional)
```
Turret_ID: 2011
Gun_ID: 502
Country: Britain
Caliber: 15"
Turret_Type: Single
Designation: 15"/42 Mark I Single
Turret_Weight_Tons: 195
Crew_Size: 40
Armor_Face_IN: 15
Armor_Sides_IN: 10
Armor_Roof_IN: 6
Traverse_Rate_Deg_Sec: 2.5
Elevation_Min_Deg: -5
Elevation_Max_Deg: 30
Elevation_Rate_Deg_Sec: NULL
Rate_Of_Fire_RPM: 1.8
Modded: 1
Notes: Fictional single mount. Shell: 1,938 lbs.
```

### Required Data Checklist
- [ ] Turret_ID assigned (2001-2200 for British)
- [ ] Gun_ID references valid British gun
- [ ] Country = "Britain"
- [ ] Caliber matches Gun_ID's caliber
- [ ] Turret_Type specified (Single/Twin/Triple/Quad)
- [ ] Designation descriptive
- [ ] Turret_Weight_Tons provided
- [ ] Crew_Size provided
- [ ] All armor values provided (Face, Sides, Roof)
- [ ] Traverse_Rate_Deg_Sec provided
- [ ] Elevation_Min_Deg and Elevation_Max_Deg provided
- [ ] Rate_Of_Fire_RPM provided
- [ ] Modded flag (0 for historical, 1 for fictional)
- [ ] Notes indicate historical vs fictional
- [ ] Historical turrets marked "HISTORICAL - [details]"
- [ ] Fictional turrets include "Fictional - [reasoning]"

### Scaling Guidelines for Fictional Turrets
**Weight Scaling** (from Single → larger mounts):
- Single → Twin: ×2.5 to ×3.0
- Twin → Triple: ×1.4 to ×1.5
- Triple → Quad: ×1.3 to ×1.4

**Crew Scaling**:
- Proportional to number of guns and turret complexity
- Single: base crew
- Twin: ~2× single
- Triple: ~2.5-3× single
- Quad: ~3.5-4× single

**Performance Degradation** (larger = slower):
- Traverse Rate: decreases with weight
- Rate of Fire: slightly decreases with more guns
- Elevation Rate: decreases with complexity

---

## Table 4: Gun_Ammunition_Compatibility

### Schema
```
Compatibility_ID        INTEGER PRIMARY KEY (AUTO)
Gun_ID                  INTEGER NOT NULL (foreign key to Guns)
Ammunition_ID           INTEGER NOT NULL (foreign key to Ammunition)
Notes                   TEXT (nullable but recommended)
Caliber                 TEXT (nullable - denormalized)
Muzzle_Velocity_FPS     REAL (nullable but recommended)
Muzzle_Velocity_MPS     REAL (nullable - calculated from FPS)
Max_Range_Yards         REAL (nullable but recommended)
Barrel_Wear_Per_Round   REAL (nullable - wear rate)
UNIQUE(Gun_ID, Ammunition_ID)
```

### Template Format
```
Compatibility_ID: [AUTO]
Gun_ID: [501-555] (British gun)
Ammunition_ID: [101-200] (British ammunition)
Notes: "[Caliber] [ammo type] shell. Propellant: [weight] lbs. [Special notes]. Barrel life: [rounds]. Source: [sources]"
Caliber: "[X]\"" (should match both Gun and Ammunition)
Muzzle_Velocity_FPS: [XXXX] (feet per second)
Muzzle_Velocity_MPS: [XXX.X] (meters per second - calculated)
Max_Range_Yards: [XXXXX] (maximum range in yards)
Barrel_Wear_Per_Round: [X.XXXX] (optional - wear per shot)
```

### Example (Good)
```
Compatibility_ID: AUTO
Gun_ID: 502
Ammunition_ID: 102
Notes: 15" 6crh AP shell with supercharge 490 lbs (1937+). Improved aerodynamics. Vanguard: 37,870 yds with supercharge. Barrel life: ~335 rounds. Source: NavWeaps
Caliber: 15"
Muzzle_Velocity_FPS: 2640
Muzzle_Velocity_MPS: NULL
Max_Range_Yards: 33550
Barrel_Wear_Per_Round: NULL
```

### Required Data Checklist
- [ ] Gun_ID references valid British gun
- [ ] Ammunition_ID references valid British ammunition
- [ ] Caliber matches both gun and ammunition
- [ ] Muzzle_Velocity_FPS provided
- [ ] Max_Range_Yards provided (if known)
- [ ] Notes include: ammo type, propellant, barrel life, sources
- [ ] No duplicate Gun_ID + Ammunition_ID combinations

---

## Validation Process

### Step 1: Verify Guns Table Data
For each gun in british_naval_weapons_research.md:
1. Check Gun_ID is in range 501-555
2. Verify all required fields present
3. Confirm weight is in tons
4. Validate Notes completeness (ships, specs, sources)
5. Confirm Year_Introduced is 1890-1990

### Step 2: Verify Ammunition Table Data
For each ammunition type:
1. Check ID is in range 101-200
2. Verify Caliber matches parent gun
3. Confirm Weight_LBS is provided
4. Validate Projectile_Type is standard (AP, APC, HE, CPC, etc.)
5. Check Notes completeness (propellant, velocity, sources)

### Step 3: Verify Turrets Table Data
For each turret variant:
1. Check Turret_ID is in range 2001-2200
2. Verify Gun_ID exists and is British
3. Confirm Caliber matches Gun_ID's caliber
4. Validate all armor values present
5. Check crew size is reasonable
6. Verify weight scaling follows guidelines
7. Confirm historical turrets marked "HISTORICAL"
8. Validate fictional turrets have reasoning

### Step 4: Verify Gun_Ammunition_Compatibility
For each compatibility record:
1. Verify Gun_ID exists
2. Verify Ammunition_ID exists
3. Check Caliber matches both
4. Confirm Muzzle_Velocity_FPS present
5. Validate Max_Range_Yards present
6. Check no duplicate combinations

---

## Common Issues to Check

### Data Completeness
- [ ] All required fields populated (no NULLs where required)
- [ ] Estimated values noted as such in Notes
- [ ] Sources cited for all data
- [ ] Year ranges appropriate (1890-1990)

### Data Consistency
- [ ] Calibers match across related tables
- [ ] Gun_IDs referenced in Turrets exist in Guns
- [ ] Ammunition_IDs referenced in Compatibility exist in Ammunition
- [ ] Country = "Britain" for all British records

### Data Quality
- [ ] Weights in correct units (tons for guns/turrets, lbs for ammo)
- [ ] Rates of fire reasonable for caliber/era
- [ ] Armor values reasonable for turret type
- [ ] Crew sizes appropriate for turret configuration

### Historical Accuracy
- [ ] Historical guns/turrets marked Modded = 0
- [ ] Fictional variants marked Modded = 1
- [ ] Historical data has source citations
- [ ] Ship names and dates verified where possible

---

## Data Gaps - Acceptable vs Unacceptable

### Acceptable Gaps (can be NULL or estimated)
- Guns: Turret_ID (always NULL for guns)
- Ammunition: Length_IN, Bursting_Charge, Kinetic_Energy_MJ, Cartridge_Type, Year_Introduced
- Turrets: Elevation_Rate_Deg_Sec (if unknown)
- Compatibility: Muzzle_Velocity_MPS (calculated field), Barrel_Wear_Per_Round

### Unacceptable Gaps (must be filled)
- All: Country, Modded, Notes
- Guns: Gun_ID, Caliber, Length, Mark_Designation, Year_Introduced, Weight
- Ammunition: ID, Caliber, Projectile_Type, Weight_LBS
- Turrets: All fields except Elevation_Rate_Deg_Sec
- Compatibility: Gun_ID, Ammunition_ID, Caliber, Muzzle_Velocity_FPS, Max_Range_Yards

---

## Next Steps After Template Validation

1. **Review british_naval_weapons_research.md** against these templates
2. **Document any missing data** in a validation report
3. **Fill data gaps** where possible through additional research
4. **Mark estimated values** clearly in Notes
5. **Create SQL import script** only after validation passes
6. **Import to database** after user approval

