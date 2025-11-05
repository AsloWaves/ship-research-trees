# Naval_Guns.db - Schema Reference Guide

**Database:** Naval_Guns.db
**Last Updated:** 2025-10-08
**Purpose:** Comprehensive naval weapons research database covering the "Big 4" naval powers (USA, Britain, Germany, Japan) from 1890-1990, including historical and fictional data

---

## Database Overview

### Current Statistics
- **Guns:** 5 (5 historical, 0 fictional)
- **Ammunition:** 11 unique types (11 historical, 0 fictional)
- **Turrets:** 20 (4 historical, 16 fictional)
- **Compatibility Mappings:** 18 gun/ammo combinations

### Scope

**Target Scope (Planned):**
- **Countries:** "Big 4" Naval Powers
  - United States (USA)
  - Great Britain (UK/Britain)
  - Germany (Imperial & Kriegsmarine)
  - Japan (Imperial Japanese Navy)
- **Time Period:** 1890-1990 (100 years of naval warfare evolution)
- **Weapon Types:** All naval guns from battleships, cruisers, destroyers, and smaller vessels
- **Calibers:** From small 3-inch destroyer guns to massive 18.1-inch battleship guns

**Current Implementation:**
Focused on **US 16" naval guns** (1921-1967) as initial dataset:
- Mark 1 (1921) - Colorado class
- Mark 2/3 (cancelled 1922) - Lexington/South Dakota classes
- Mark 5/8 (1938) - Colorado modernized
- Mark 6 (1941) - North Carolina/South Dakota classes
- Mark 7 (1943) - Iowa class

This serves as the foundation for expanding to all Big 4 nations and the full 1890-1990 timeline.

---

## Table Structures

### 1. Guns Table

**Purpose:** Store naval gun specifications

```sql
CREATE TABLE Guns (
    Gun_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Turret_ID INTEGER,                    -- Links to Turrets table (optional)
    Country TEXT,                         -- e.g., "USA", "UK", "Germany"
    Caliber TEXT,                         -- e.g., "16\"", "14\"", "381mm"
    Length TEXT,                          -- Barrel length in calibers, e.g., "/50", "L/52"
    Mark_Designation TEXT,                -- e.g., "Mark 7", "Type 94"
    Year_Introduced INTEGER,              -- Year gun entered service (NULL if cancelled)
    Weight REAL,                          -- Gun weight in tons
    Modded INTEGER DEFAULT 0,             -- 0 = Historical, 1 = Fictional
    Notes TEXT,                           -- Detailed specifications and history
    FOREIGN KEY (Turret_ID) REFERENCES Turrets(Turret_ID)
);
```

**Field Conventions:**
- **Caliber:** Use consistent format - inches with `"` (e.g., `16"`), or metric with unit (e.g., `406mm`)
- **Length:** Use `/XX` for US notation (e.g., `/50` = 50 calibers long)
- **Weight:** Tons (long tons for historical accuracy, specify in Notes if different)
- **Notes:** Include ships used, barrel life, rifling, chamber volume, source URL

**Example Record:**
```sql
Gun_ID: 396
Country: USA
Caliber: 16"
Length: /50
Mark_Designation: Mark 7
Year_Introduced: 1943
Weight: 133.952 tons
Modded: 0
Notes: Ships: USS Iowa (BB-61)... | Barrel Life: 290-350 ESR | Rifling: 96 grooves...
```

---

### 2. Ammunition Table

**Purpose:** Store unique ammunition/projectile specifications (no duplicates)

```sql
CREATE TABLE Ammunition (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Turret_ID INTEGER,                    -- Optional direct turret link
    Caliber TEXT,                         -- e.g., "16\"", "155mm"
    Mark_Designation TEXT,                -- e.g., "Mark 8", "Type 91 AP"
    Projectile_Type TEXT,                 -- e.g., "AP", "HE", "HC", "SAP", "Nuclear"
    Weight_LBS REAL,                      -- Projectile weight in pounds
    Length_IN REAL,                       -- Projectile length in inches
    Bursting_Charge REAL,                 -- Explosive filler in pounds
    Kinetic_Energy_MJ REAL,               -- Kinetic energy in megajoules (calculated)
    Cartridge_Type TEXT,                  -- e.g., "Separate", "Fixed", "Bag"
    Year_Introduced INTEGER,              -- Year ammunition was introduced
    Country TEXT,                         -- Country of origin
    Modded INTEGER DEFAULT 0,             -- 0 = Historical, 1 = Fictional
    Notes TEXT,                           -- Additional details and compatibility notes
    FOREIGN KEY (Turret_ID) REFERENCES Turrets(Turret_ID)
);
```

**Field Conventions:**
- **Projectile_Type:** Standard types: AP, APC, HE, HC, SAP, Common, Shrapnel, Illumination, Practice, Nuclear
- **Weight_LBS:** Projectile only (not including propellant)
- **Kinetic_Energy_MJ:** Calculate using: `KE = 0.5 × mass(kg) × velocity(m/s)² / 1,000,000`
- **Bursting_Charge:** NULL for inert rounds (practice) and nuclear rounds
- **Notes:** Include gun compatibility, limitations, muzzle velocity info

**Example Record:**
```sql
ID: 1
Caliber: 16"
Mark_Designation: Mark 8
Projectile_Type: AP
Weight_LBS: 2700.0
Length_IN: 72.0
Bursting_Charge: 40.9
Kinetic_Energy_MJ: 334.54
Year_Introduced: 1943
Country: USA
Modded: 0
Notes: Super-heavy AP shell | Compatible with Mark 6 and Mark 7 guns
```

**IMPORTANT:** Each unique ammunition type appears ONLY ONCE in this table. Gun-specific data (muzzle velocity, range) goes in the junction table.

---

### 3. Turrets Table

**Purpose:** Store turret/mount specifications

```sql
CREATE TABLE Turrets (
    Turret_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Gun_ID INTEGER,                       -- Links to Guns table
    Country TEXT,                         -- Country of origin
    Turret_Type TEXT,                     -- "Single", "Twin", "Triple", "Quad"
    Designation TEXT,                     -- Full descriptive name
    Turret_Weight_Tons REAL,              -- Total turret weight in tons
    Crew_Size INTEGER,                    -- Number of crew members
    Armor_Face_IN REAL,                   -- Face armor thickness in inches
    Armor_Sides_IN REAL,                  -- Side armor thickness in inches
    Armor_Roof_IN REAL,                   -- Roof armor thickness in inches
    Traverse_Rate_Deg_Sec REAL,           -- Horizontal rotation rate (degrees/sec)
    Elevation_Min_Deg REAL,               -- Minimum elevation (negative = depression)
    Elevation_Max_Deg REAL,               -- Maximum elevation
    Elevation_Rate_Deg_Sec REAL,          -- Vertical movement rate (degrees/sec)
    Rate_Of_Fire_RPM REAL,                -- Rounds per minute (per barrel)
    Modded INTEGER DEFAULT 0,             -- 0 = Historical, 1 = Fictional
    Notes TEXT,                           -- Ships used, design notes
    FOREIGN KEY (Gun_ID) REFERENCES Guns(Gun_ID)
);
```

**Field Conventions:**
- **Turret_Type:** Single, Twin, Triple, Quad, Quintuple
- **Designation:** Include caliber, length, mark, and type (e.g., `16"/50 Mark 7 Triple Turret`)
- **Elevation_Min_Deg:** Negative values for depression (e.g., `-5` = 5° depression)
- **Armor:** Maximum thickness for each section (inches)
- **Notes:** Include ships, design notes, limitations

**Example Record:**
```sql
Turret_ID: 1
Gun_ID: 396 (Mark 7)
Country: USA
Turret_Type: Triple
Designation: 16"/50 Mark 7 Triple Turret
Turret_Weight_Tons: 1708.0
Crew_Size: 77
Armor_Face_IN: 17.5
Traverse_Rate_Deg_Sec: 4.0
Elevation_Min_Deg: -5.0
Elevation_Max_Deg: 45.0
Modded: 0
Notes: Iowa-class main battery turret. Most powerful US naval turret ever built.
```

---

### 4. Gun_Ammunition_Compatibility Table (Junction)

**Purpose:** Link guns to compatible ammunition with gun-specific ballistic performance data

```sql
CREATE TABLE Gun_Ammunition_Compatibility (
    Compatibility_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Gun_ID INTEGER NOT NULL,              -- References Guns(Gun_ID)
    Ammunition_ID INTEGER NOT NULL,       -- References Ammunition(ID)
    Caliber TEXT,                         -- Copy of caliber for readability
    Muzzle_Velocity_FPS REAL,             -- Muzzle velocity in feet/second
    Muzzle_Velocity_MPS REAL,             -- Muzzle velocity in meters/second
    Max_Range_Yards REAL,                 -- Maximum range in yards
    Barrel_Wear_Per_Round REAL,           -- Barrel wear percentage per shot
    Notes TEXT,                           -- Compatibility notes
    FOREIGN KEY (Gun_ID) REFERENCES Guns(Gun_ID),
    FOREIGN KEY (Ammunition_ID) REFERENCES Ammunition(ID),
    UNIQUE(Gun_ID, Ammunition_ID)         -- Prevents duplicate pairings
);
```

**Field Conventions:**
- **Caliber:** Auto-populated from Guns table for easy queries
- **Muzzle_Velocity_FPS/MPS:** Gun-specific velocity (same ammo = different velocities in different guns!)
- **Max_Range_Yards:** Maximum range at optimal elevation for this gun/ammo combination
- **Barrel_Wear_Per_Round:** Percentage (0.25 = 0.25% wear per shot = ~400 round barrel life)
- **Notes:** Compatibility notes (e.g., "Primary armor-piercing round", "Requires modification")

**Example Record:**
```sql
Compatibility_ID: 1
Gun_ID: 396 (Mark 7)
Ammunition_ID: 1 (Mark 8 AP)
Caliber: 16"
Muzzle_Velocity_FPS: 2500
Muzzle_Velocity_MPS: 762
Max_Range_Yards: 42345
Barrel_Wear_Per_Round: 0.33
Notes: Super-heavy AP shell - primary armor-piercing round
```

**Why This Table Exists:**
- Same ammunition fires at **different velocities** from different guns
- Example: Mark 8 AP fires at 2500 fps from Mark 7, but only 2300 fps from Mark 6
- Allows proper ballistic calculations per gun/ammo combination

---

## Database Relationships

```
┌─────────────┐         ┌─────────────────────────────────┐         ┌──────────────┐
│   Turrets   │────────▶│  Guns                          │◀────────│  Ammunition  │
│             │ Gun_ID  │                                 │         │              │
│ (1-to-many) │         │  (Many-to-Many via Junction)   │         │ (Turret_ID)  │
└─────────────┘         └─────────────────────────────────┘         └──────────────┘
                                    │         ▲
                                    │         │
                                    ▼         │
                        ┌───────────────────────────────┐
                        │ Gun_Ammunition_Compatibility  │
                        │        (Junction Table)       │
                        │  - Links guns to ammo         │
                        │  - Stores gun-specific data   │
                        └───────────────────────────────┘
```

**Relationship Types:**
1. **Turrets → Guns:** One-to-many (one turret can have multiple guns in rare cases, e.g., quad mount)
2. **Guns → Ammunition:** Many-to-many (via Gun_Ammunition_Compatibility junction table)
3. **Turrets → Ammunition:** Optional direct link (rarely used, junction table preferred)

---

## Data Entry Guidelines

### Caliber Notation
**Be consistent within each country:**
- **US/UK:** Use inches with quote mark: `16"`, `14"`, `6"`
- **Metric:** Include unit: `406mm`, `381mm`, `155mm`
- **Alternative:** Can also use `16 inch`, `406 mm` (with space)

### Gun Length Notation
- **US:** `/50`, `/45`, `/38` (calibers)
- **European:** `L/52`, `L/45` (calibers)
- **Actual length:** Can include in Notes (e.g., "800 in bore length")

### Weight Units
- **Guns:** Tons (long tons preferred: 2,240 lbs)
- **Ammunition:** Pounds (lbs)
- **Always specify** in Notes if using metric tons or short tons

### Year Fields
- **Year_Introduced:** Year entered service
- **NULL if cancelled** (e.g., Mark 2/3 guns)
- Use earliest date if multiple variants

### Modded Flag
- **0 = Historical:** Real, verified data from authoritative sources
- **1 = Fictional:** Estimated, theoretical, or game/simulation designs

### Notes Field Best Practices
Format notes with `|` separator for easy parsing:
```
Ships: USS Iowa (BB-61), USS Missouri (BB-63) | Barrel Life: 290-350 rounds |
Rifling: 96 grooves, 1 in 25 twist | Chamber: 27,000 in³ |
Source: http://www.navweaps.com/...
```

---

## Common Query Patterns

### 1. Get All Ammunition for a Specific Gun
```sql
SELECT
    a.Mark_Designation,
    a.Projectile_Type,
    a.Weight_LBS,
    c.Muzzle_Velocity_FPS,
    c.Max_Range_Yards
FROM Guns g
JOIN Gun_Ammunition_Compatibility c ON g.Gun_ID = c.Gun_ID
JOIN Ammunition a ON c.Ammunition_ID = a.ID
WHERE g.Mark_Designation = 'Mark 7'
ORDER BY a.Projectile_Type, a.Weight_LBS DESC;
```

### 2. Get All Guns Compatible with Specific Ammunition
```sql
SELECT
    g.Mark_Designation,
    g.Year_Introduced,
    c.Muzzle_Velocity_FPS,
    c.Max_Range_Yards
FROM Ammunition a
JOIN Gun_Ammunition_Compatibility c ON a.ID = c.Ammunition_ID
JOIN Guns g ON c.Gun_ID = g.Gun_ID
WHERE a.Mark_Designation = 'Mark 8'
ORDER BY c.Muzzle_Velocity_FPS DESC;
```

### 3. Get All Ammunition for a Turret (via Gun)
```sql
SELECT
    t.Designation AS Turret,
    a.Mark_Designation AS Ammo,
    a.Projectile_Type,
    c.Muzzle_Velocity_FPS,
    c.Max_Range_Yards
FROM Turrets t
JOIN Guns g ON t.Gun_ID = g.Gun_ID
JOIN Gun_Ammunition_Compatibility c ON g.Gun_ID = c.Gun_ID
JOIN Ammunition a ON c.Ammunition_ID = a.ID
WHERE t.Turret_ID = 1
ORDER BY a.Projectile_Type;
```

### 4. Find Guns by Country and Caliber
```sql
SELECT
    Gun_ID,
    Mark_Designation,
    Year_Introduced,
    Weight,
    Modded
FROM Guns
WHERE Country = 'USA' AND Caliber = '16"'
ORDER BY Year_Introduced;
```

### 5. Get Historical Turrets Only
```sql
SELECT
    Turret_ID,
    Designation,
    Turret_Type,
    Crew_Size,
    Turret_Weight_Tons
FROM Turrets
WHERE Modded = 0
ORDER BY Turret_Weight_Tons DESC;
```

### 6. Compare Same Ammunition Across Different Guns
```sql
SELECT
    c.Caliber,
    g.Mark_Designation AS Gun,
    a.Mark_Designation AS Ammo,
    c.Muzzle_Velocity_FPS,
    c.Max_Range_Yards,
    c.Barrel_Wear_Per_Round
FROM Gun_Ammunition_Compatibility c
JOIN Guns g ON c.Gun_ID = g.Gun_ID
JOIN Ammunition a ON c.Ammunition_ID = a.ID
WHERE a.Mark_Designation = 'Mark 13'
ORDER BY c.Muzzle_Velocity_FPS DESC;
```

### 7. Get Turret Performance Summary
```sql
SELECT
    t.Designation,
    t.Turret_Type,
    g.Mark_Designation AS Gun,
    COUNT(DISTINCT c.Ammunition_ID) AS Ammo_Types,
    AVG(c.Max_Range_Yards) AS Avg_Range,
    MAX(c.Muzzle_Velocity_FPS) AS Max_Velocity
FROM Turrets t
JOIN Guns g ON t.Gun_ID = g.Gun_ID
JOIN Gun_Ammunition_Compatibility c ON g.Gun_ID = c.Gun_ID
WHERE t.Modded = 0
GROUP BY t.Turret_ID
ORDER BY Avg_Range DESC;
```

---

## Calculation Formulas

### Kinetic Energy (MJ)
```
KE = 0.5 × mass(kg) × velocity(m/s)² / 1,000,000

Conversions:
- 1 lb = 0.453592 kg
- 1 fps = 0.3048 m/s
```

**Example:**
- Mark 8 AP: 2700 lbs, 2500 fps
- Mass: 2700 × 0.453592 = 1224.7 kg
- Velocity: 2500 × 0.3048 = 762 m/s
- KE = 0.5 × 1224.7 × 762² / 1,000,000 = **334.54 MJ**

### Barrel Life (from Wear Percentage)
```
Barrel Life (rounds) = 100 / Barrel_Wear_Per_Round

Example:
- Barrel_Wear_Per_Round = 0.33%
- Barrel Life = 100 / 0.33 = 303 rounds
```

### Max Range (Estimated)
Rough estimate based on:
- Muzzle velocity
- Elevation angle
- Projectile weight/drag

**Not calculated** - use historical data when available, estimate for fictional.

---

## Data Quality Checks

### Before Adding New Data
1. **Check for duplicates:** Query by Mark_Designation and Caliber
2. **Verify foreign keys:** Ensure Gun_ID and Ammunition_ID exist
3. **Validate Modded flag:** 0 for historical, 1 for fictional
4. **Confirm units:** Weight in tons, length in inches, velocity in fps

### Validation Queries

**Find guns without ammunition:**
```sql
SELECT g.Gun_ID, g.Mark_Designation
FROM Guns g
LEFT JOIN Gun_Ammunition_Compatibility c ON g.Gun_ID = c.Gun_ID
WHERE c.Compatibility_ID IS NULL;
```

**Find ammunition not linked to any gun:**
```sql
SELECT a.ID, a.Mark_Designation
FROM Ammunition a
LEFT JOIN Gun_Ammunition_Compatibility c ON a.ID = c.Ammunition_ID
WHERE c.Compatibility_ID IS NULL;
```

**Check for missing muzzle velocity:**
```sql
SELECT Gun_ID, Ammunition_ID
FROM Gun_Ammunition_Compatibility
WHERE Muzzle_Velocity_FPS IS NULL;
```

---

## Data Sources

### Primary Sources (Historical Data)
1. **NavWeaps.com** - Most authoritative source for naval weapons (all Big 4 nations)
   - **USA:** `http://www.navweaps.com/Weapons/WNUS_16-50_mk7.php`
   - **Britain:** `http://www.navweaps.com/Weapons/WNBR_15-42_mk1.php`
   - **Germany:** `http://www.navweaps.com/Weapons/WNGER_15-52_skc34.php`
   - **Japan:** `http://www.navweaps.com/Weapons/WNJAP_18-45_t94.php`
2. **Naval_Guns_backup_20251008_133121.db** - Original scraped data
3. **Jane's Fighting Ships** - Historical reference for all navies
4. **Naval technical manuals** - Official specifications (country-specific)

### Estimation Guidelines (Fictional Data)
When creating fictional turrets/guns:
1. **Base on historical data** - Use similar guns as reference
2. **Weight scaling:** Single = 40-45% of twin, Quad = 270-310% of twin
3. **Traverse rate:** Inversely proportional to weight (heavier = slower)
4. **Crew size:** Scales with turret complexity and gun count
5. **Mark as Modded = 1**

---

## Export/Backup Procedures

### Full Database Backup
```bash
# Create timestamped backup
sqlite3 Naval_Guns.db ".backup Naval_Guns_backup_$(date +%Y%m%d_%H%M%S).db"
```

### Export Table to CSV
```bash
sqlite3 -header -csv Naval_Guns.db "SELECT * FROM Guns;" > Guns_export.csv
```

### Export Schema
```bash
sqlite3 Naval_Guns.db ".schema" > schema.sql
```

---

## Current Limitations & Future Expansion

### Current Scope (Phase 1)
- **Countries:** USA only
- **Calibers:** 16" only
- **Time Period:** 1921-1967
- **Total Guns:** 5
- **Total Ammunition:** 11 unique types

### Planned Expansion: "Big 4" Naval Powers (1890-1990)

**Phase 2: USA Complete Coverage**
- **Battleship guns:** 18", 16", 14", 12"
- **Cruiser guns:** 8", 6", 5"
- **Destroyer guns:** 5", 4", 3"
- **Secondary/AA guns:** Various calibers from 3" to 6"
- **Time span:** 1890-1990 (pre-dreadnought through modern era)

**Phase 3: Great Britain**
- **Battleship guns:** 18", 16", 15", 14", 13.5", 12"
- **Cruiser guns:** 9.2", 8", 7.5", 6", 5.25"
- **Destroyer guns:** 4.7", 4.5", 4", 3"
- **Notable weapons:** BL 15"/42 Mark I (Queen Elizabeth), BL 16"/45 Mark I (Nelson)

**Phase 4: Germany**
- **Imperial Navy (1890-1918):** 305mm, 280mm, 240mm, 150mm, 105mm, 88mm
- **Kriegsmarine (1935-1945):** 406mm (planned), 380mm, 283mm, 150mm, 128mm, 105mm, 88mm
- **Notable weapons:** 38cm SK C/34 (Bismarck), 28cm SK C/34 (Scharnhorst)

**Phase 5: Japan**
- **Battleship guns:** 460mm (18.1"), 410mm (16.1"), 356mm (14"), 305mm (12")
- **Cruiser guns:** 203mm (8"), 155mm (6.1"), 140mm (5.5")
- **Notable weapons:** 46cm/45 Type 94 (Yamato - largest naval guns ever), 41cm/45 Type 3 (Nagato)

**Phase 6: Enhanced Data**
- **Ballistics:** Penetration tables, armor effectiveness charts
- **Propellant:** Charge weights, types, and configurations
- **Economics:** Production costs, barrel replacement costs
- **Range tables:** Complete elevation/range/velocity data (may require new table)

### Schema Stability
**Current schema is stable** - no major changes expected. Adding new guns/ammunition uses existing structure.

---

## Quick Reference Summary

| Table | Purpose | Primary Key | Foreign Keys | Unique Constraint |
|-------|---------|-------------|--------------|-------------------|
| **Guns** | Gun specifications | Gun_ID | Turret_ID (optional) | None |
| **Ammunition** | Unique ammunition types | ID | Turret_ID (optional) | None |
| **Turrets** | Turret/mount specs | Turret_ID | Gun_ID | None |
| **Gun_Ammunition_Compatibility** | Gun/ammo ballistics | Compatibility_ID | Gun_ID, Ammunition_ID | (Gun_ID, Ammunition_ID) |

**Key Design Principle:**
- Each ammunition type stored **once** in Ammunition table
- Gun-specific data (velocity, range) stored in **Gun_Ammunition_Compatibility** junction table
- This prevents duplicates and allows accurate gun-specific ballistics

---

**Last Updated:** 2025-10-08
**Schema Version:** 1.0
**Database File:** D:\Research\naval_guns.db
**Expansion Target:** Big 4 Naval Powers (USA, Britain, Germany, Japan) | 1890-1990
