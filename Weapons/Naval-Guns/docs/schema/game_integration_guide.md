# Naval Weapons Database - Game Integration Guide

**Version**: 1.0
**Date**: October 2025
**Database**: naval_guns.db

---

## Database Overview

**Current Record Counts**:
- **Guns**: 78 base gun designs
- **Ammunition**: 72 ammunition types
- **Turrets**: 1,700 turret configurations (variants of base guns)
- **Compatibility**: 112 gun-ammunition compatibility records

---

## Game Design Philosophy

### Core Principle: Ammunition Compatibility is Gun-Based

**Key Insight**: A gun fires the same ammunition regardless of turret configuration.

**Example**:
- **Gun**: 16"/50 Mark 7 (Iowa-class battleship gun)
- **Compatible Ammunition**: Mark 8 AP, Mark 13 HC, Mark 14 HC, Mark 23 Nuclear, Mark 19 HE
- **Turret Variants**:
  - Twin Turret (2 barrels, 55 crew)
  - Quad Turret (4 barrels, 105 crew, theoretical design)

All variants fire the same ammunition types. The turret configuration only affects:
- Rate of fire (barrels × base ROF)
- Weight and armor
- Crew requirements
- Traverse/elevation speeds

---

## Database Schema

### Table: `Guns` (78 records)

Base gun designs - the core weapon platform.

```sql
CREATE TABLE Guns (
    Gun_ID INTEGER PRIMARY KEY,
    Country TEXT,
    Caliber TEXT,              -- e.g., "16"", "5""
    Length TEXT,               -- e.g., "/50", "/38"
    Mark_Designation TEXT,     -- e.g., "Mark 7", "Mark 12"
    Year_Introduced INTEGER,
    Weight REAL,               -- Gun weight (tons)
    Modded INTEGER,            -- 0=historical, 1=fictional/modded
    Notes TEXT
);
```

**Game Usage**: Reference table for gun specifications.

---

### Table: `Turrets` (1,700 records)

Turret configurations - what players unlock and equip on ships.

```sql
CREATE TABLE Turrets (
    Turret_ID INTEGER PRIMARY KEY,
    Gun_ID INTEGER,            -- Links to base gun (inherits ammo compatibility)
    Country TEXT,
    Turret_Type TEXT,          -- e.g., "Twin", "Triple", "Quad"
    Designation TEXT,          -- e.g., "16"/50 Mark 7 Twin Turret"
    Turret_Weight_Tons REAL,
    Crew_Size INTEGER,
    Armor_Face_IN REAL,
    Armor_Sides_IN REAL,
    Armor_Roof_IN REAL,
    Traverse_Rate_Deg_Sec REAL,
    Elevation_Min_Deg REAL,
    Elevation_Max_Deg REAL,
    Elevation_Rate_Deg_Sec REAL,
    Rate_Of_Fire_RPM REAL,     -- Total turret ROF (barrels × base ROF)
    Modded INTEGER,
    Notes TEXT,
    FOREIGN KEY (Gun_ID) REFERENCES Guns(Gun_ID)
);
```

**Game Usage**:
- Players unlock turrets (not guns directly)
- Each turret has unique stats (weight, armor, crew, ROF)
- Turret inherits ammunition compatibility from base gun via `Gun_ID`

---

### Table: `Ammunition` (72 records)

Ammunition types - what players acquire and stock in inventory.

```sql
CREATE TABLE Ammunition (
    ID INTEGER PRIMARY KEY,
    Caliber TEXT,              -- e.g., "16"", "5""
    Mark_Designation TEXT,     -- e.g., "Mark 8", "Mark 13"
    Projectile_Type TEXT,      -- e.g., "AP", "HC", "HE", "VT"
    Weight_LBS REAL,
    Length_IN REAL,
    Bursting_Charge REAL,
    Kinetic_Energy_MJ REAL,
    Cartridge_Type TEXT,
    Year_Introduced INTEGER,
    Country TEXT,
    Modded INTEGER,
    Notes TEXT
);
```

**Game Usage**: Player inventory - ammunition types available to use.

---

### Table: `Gun_Ammunition_Compatibility` (112 records)

Links guns to compatible ammunition with ballistic data.

```sql
CREATE TABLE Gun_Ammunition_Compatibility (
    Compatibility_ID INTEGER PRIMARY KEY,
    Gun_ID INTEGER NOT NULL,
    Ammunition_ID INTEGER NOT NULL,
    Notes TEXT,
    Caliber TEXT,
    Muzzle_Velocity_FPS REAL,   -- Performance when fired from this gun
    Muzzle_Velocity_MPS REAL,
    Max_Range_Yards REAL,
    Barrel_Wear_Per_Round REAL,
    FOREIGN KEY (Gun_ID) REFERENCES Guns(Gun_ID),
    FOREIGN KEY (Ammunition_ID) REFERENCES Ammunition(ID),
    UNIQUE(Gun_ID, Ammunition_ID)  -- Prevents duplicate entries
);
CREATE INDEX idx_compat_gun ON Gun_Ammunition_Compatibility(Gun_ID);
CREATE INDEX idx_compat_ammo ON Gun_Ammunition_Compatibility(Ammunition_ID);
```

**Game Usage**: Core compatibility lookup - determines what ammo works with which turrets.

---

## Game Runtime Queries

### Query 1: Find Compatible Ammunition for Equipped Turret

**Scenario**: Player has equipped Turret_ID 10 (16"/50 Mark 7 Twin). Show all compatible ammunition from player inventory.

```sql
-- Query compatible ammunition for a specific turret
SELECT
    a.ID as Ammo_ID,
    a.Caliber,
    a.Mark_Designation,
    a.Projectile_Type,
    a.Weight_LBS,
    gac.Muzzle_Velocity_FPS,
    gac.Max_Range_Yards,
    gac.Barrel_Wear_Per_Round
FROM Turrets t
JOIN Gun_Ammunition_Compatibility gac
    ON t.Gun_ID = gac.Gun_ID
JOIN Ammunition a
    ON gac.Ammunition_ID = a.ID
WHERE t.Turret_ID = ?
  AND a.ID IN (player_inventory_ammo_ids);
```

**Result Example** (Turret_ID = 10):
```
Ammo_ID | Caliber | Mark | Type | Velocity | Range
--------|---------|------|------|----------|---------
1       | 16"     | Mark 8  | AP   | 2500 fps | 42,345 yds
2       | 16"     | Mark 13 | HC   | 2690 fps | 42,080 yds
3       | 16"     | Mark 14 | HC   | 2690 fps | 42,080 yds
4       | 16"     | Mark 23 | Nuclear | 2500 fps | 39,000 yds
5       | 16"     | Mark 19 | HE   | 2690 fps | 42,300 yds
```

**Game Logic**:
1. Player equips turret on ship
2. Query runs to find compatible ammo in inventory
3. Game allows player to select which ammo to load
4. Combat uses selected ammo's stats from compatibility table

---

### Query 2: Show All Turret Variants for a Gun

**Scenario**: Player researching turret options for the 16"/50 Mark 7 gun.

```sql
-- Show all turret configurations for a specific gun
SELECT
    t.Turret_ID,
    t.Designation,
    t.Turret_Type,
    t.Rate_Of_Fire_RPM,
    t.Turret_Weight_Tons,
    t.Crew_Size,
    t.Armor_Face_IN
FROM Turrets t
WHERE t.Gun_ID = ?
ORDER BY t.Rate_Of_Fire_RPM;
```

**Result Example** (Gun_ID = 396):
```
Turret_ID | Designation              | Type  | ROF | Weight | Crew | Armor
----------|--------------------------|-------|-----|--------|------|-------
10        | 16"/50 Mark 7 Twin       | Twin  | 2.0 | 1,200t | 55   | 17"
16        | 16"/50 Mark 7 Quad       | Quad  | 2.0 | 2,400t | 105  | 20"
```

---

### Query 3: Show All Guns That Can Fire Specific Ammunition

**Scenario**: Player found rare "Mark 23 Nuclear" ammunition. Which turrets can use it?

```sql
-- Find all turrets compatible with specific ammunition
SELECT
    t.Turret_ID,
    t.Designation,
    g.Mark_Designation as Gun_Mark,
    gac.Muzzle_Velocity_FPS,
    gac.Max_Range_Yards
FROM Ammunition a
JOIN Gun_Ammunition_Compatibility gac
    ON a.ID = gac.Ammunition_ID
JOIN Guns g
    ON gac.Gun_ID = g.Gun_ID
JOIN Turrets t
    ON g.Gun_ID = t.Gun_ID
WHERE a.ID = ?
ORDER BY t.Designation;
```

---

### Query 4: Get Complete Turret Profile (For Ship Fitting Screen)

**Scenario**: Display all turret information when player is equipping ship.

```sql
-- Complete turret profile with gun and compatible ammo count
SELECT
    t.Turret_ID,
    t.Designation,
    t.Turret_Type,
    t.Turret_Weight_Tons,
    t.Crew_Size,
    t.Rate_Of_Fire_RPM,
    t.Armor_Face_IN,
    t.Traverse_Rate_Deg_Sec,
    t.Elevation_Min_Deg,
    t.Elevation_Max_Deg,
    g.Caliber,
    g.Mark_Designation as Gun_Mark,
    COUNT(DISTINCT gac.Ammunition_ID) as Compatible_Ammo_Types
FROM Turrets t
JOIN Guns g ON t.Gun_ID = g.Gun_ID
LEFT JOIN Gun_Ammunition_Compatibility gac ON g.Gun_ID = gac.Gun_ID
WHERE t.Turret_ID = ?
GROUP BY t.Turret_ID;
```

---

## Data Integrity Notes

### Why 112 Compatibility Records (Not 15,858)?

**Incorrect Approach** (rejected):
- Create compatibility record for every Turret × Ammunition combination
- Results in 15,858 records with massive duplication
- Example: "16"/50 Mark 7 Twin + Mark 8 AP", "16"/50 Mark 7 Quad + Mark 8 AP" (same gun, same ammo, duplicate data)

**Correct Approach** (implemented):
- Create compatibility record for each Gun × Ammunition combination
- 112 records store unique gun-ammo compatibility
- Turrets inherit compatibility via `Gun_ID` foreign key
- Zero data duplication, efficient lookups

### UNIQUE Constraint Rationale

```sql
UNIQUE(Gun_ID, Ammunition_ID)
```

**Purpose**: Prevents accidental duplicate compatibility entries.

**Why This Works**:
- Each gun-ammo pair appears once
- All turret variants of that gun inherit the compatibility
- Database enforces referential integrity

---

## Example Game Flow

### Scenario: Player Engages Enemy Ship

**Ship Equipment**:
- Turret Slot 1: Turret_ID 10 (16"/50 Mark 7 Twin)
- Turret Slot 2: Turret_ID 16 (16"/50 Mark 7 Quad)

**Player Inventory**:
- Mark 8 AP × 100 rounds
- Mark 19 HE × 150 rounds
- Mark 41 AAC × 200 rounds (5" ammo, incompatible)

**Game Logic**:

1. **Load Phase** (before combat):
   ```sql
   -- For each equipped turret, find compatible ammo
   SELECT a.ID, a.Mark_Designation, a.Projectile_Type
   FROM Turrets t
   JOIN Gun_Ammunition_Compatibility gac ON t.Gun_ID = gac.Gun_ID
   JOIN Ammunition a ON gac.Ammunition_ID = a.ID
   WHERE t.Turret_ID IN (10, 16)
     AND a.ID IN (1, 5, 48);  -- Mark 8 AP, Mark 19 HE, Mark 41 AAC
   ```

   **Result**: Mark 8 AP and Mark 19 HE are compatible (both 16")

2. **Player Selection**:
   - Turret 1 (Twin): Load Mark 8 AP (armor-piercing)
   - Turret 2 (Quad): Load Mark 19 HE (high-explosive)

3. **Combat Phase**:
   - Turret 1 fires using Mark 8 AP stats: 2,500 fps, 42,345 yards range
   - Turret 2 fires using Mark 19 HE stats: 2,690 fps, 42,300 yards range
   - Different ROF due to turret config (Twin vs Quad)

---

## Database File Location

```
D:\Research\naval-weapons\database\naval_guns.db
```

**Connection Example** (SQLite):
```python
import sqlite3

conn = sqlite3.connect('naval_guns.db')
cursor = conn.cursor()

# Query compatible ammo for turret
turret_id = 10
cursor.execute('''
    SELECT a.ID, a.Mark_Designation, gac.Muzzle_Velocity_FPS
    FROM Turrets t
    JOIN Gun_Ammunition_Compatibility gac ON t.Gun_ID = gac.Gun_ID
    JOIN Ammunition a ON gac.Ammunition_ID = a.ID
    WHERE t.Turret_ID = ?
''', (turret_id,))

compatible_ammo = cursor.fetchall()
```

---

## Performance Considerations

### Indexed Lookups

The database includes indexes for fast queries:

```sql
CREATE INDEX idx_compat_gun ON Gun_Ammunition_Compatibility(Gun_ID);
CREATE INDEX idx_compat_ammo ON Gun_Ammunition_Compatibility(Ammunition_ID);
```

**Query Performance**:
- Turret → Compatible Ammo: O(log n) via Gun_ID index
- Ammo → Compatible Turrets: O(log n) via Ammunition_ID index
- Both queries use 2 JOINs, <1ms execution time

### Memory Footprint

- **Database Size**: ~2.5 MB
- **Table Sizes**:
  - Guns: 78 rows ≈ 10 KB
  - Ammunition: 72 rows ≈ 15 KB
  - Turrets: 1,700 rows ≈ 300 KB
  - Compatibility: 112 rows ≈ 20 KB

**Game Integration**: Can be loaded entirely into RAM for zero-latency lookups.

---

## Modded Content Support

### `Modded` Flag

All tables include a `Modded INTEGER` column:
- **0** = Historical, verified data
- **1** = Fictional, modded, or speculative

**Use Case**: Allow players to toggle mod content on/off.

```sql
-- Show only historical turrets
SELECT * FROM Turrets WHERE Modded = 0;

-- Include modded content
SELECT * FROM Turrets;  -- No filter needed
```

---

## Future Expansion

### Adding New Content

**New Gun**:
```sql
INSERT INTO Guns (Country, Caliber, Length, Mark_Designation, Year_Introduced, Weight, Modded, Notes)
VALUES ('USA', '20"', '/48', 'Mark 1', 1950, 200.0, 1, 'Theoretical super-heavy battleship gun');
```

**New Ammunition**:
```sql
INSERT INTO Ammunition (Caliber, Mark_Designation, Projectile_Type, Weight_LBS, Modded, Notes)
VALUES ('20"', 'Mark 1', 'AP', 3000.0, 1, 'Theoretical 20-inch armor-piercing shell');
```

**New Compatibility**:
```sql
INSERT INTO Gun_Ammunition_Compatibility (Gun_ID, Ammunition_ID, Muzzle_Velocity_FPS, Max_Range_Yards)
VALUES (479, 82, 2800.0, 50000.0);
```

**New Turret Variant**:
```sql
INSERT INTO Turrets (Gun_ID, Country, Turret_Type, Designation, Rate_Of_Fire_RPM, Turret_Weight_Tons, Crew_Size, Modded)
VALUES (479, 'USA', 'Twin', '20"/48 Mark 1 Twin Turret', 1.5, 1800.0, 75, 1);
```

---

## Summary

✅ **Database is game-ready** - no schema changes needed
✅ **112 compatibility records** - correct, no duplication
✅ **1,700 turrets** - full variant coverage
✅ **Efficient queries** - 2 JOINs for turret → ammo lookup
✅ **Realistic design** - gun determines ammo, turret determines performance
✅ **Mod-friendly** - `Modded` flag for content filtering

**Next Steps**:
1. Integrate database into game engine
2. Implement turret unlock progression system
3. Design ammunition acquisition/crafting mechanics
4. Build ship fitting UI using provided queries
