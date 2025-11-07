-- Reorder Turrets Table Columns
-- Move Caliber column to appear before Turret_Type
-- SQLite doesn't support column reordering, so we recreate the table

-- Step 1: Create new table with desired column order
CREATE TABLE Turrets_New (
    Turret_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Gun_ID INTEGER,
    Country TEXT,
    Caliber TEXT,           -- MOVED: Now before Turret_Type
    Turret_Type TEXT,
    Designation TEXT,
    Turret_Weight_Tons REAL,
    Crew_Size INTEGER,
    Armor_Face_IN REAL,
    Armor_Sides_IN REAL,
    Armor_Roof_IN REAL,
    Traverse_Rate_Deg_Sec REAL,
    Elevation_Min_Deg REAL,
    Elevation_Max_Deg REAL,
    Elevation_Rate_Deg_Sec REAL,
    Rate_Of_Fire_RPM REAL,
    Modded INTEGER DEFAULT 0,
    Notes TEXT,
    FOREIGN KEY (Gun_ID) REFERENCES Guns(Gun_ID)
);

-- Step 2: Copy all data from old table to new table (with correct column order)
INSERT INTO Turrets_New (
    Turret_ID,
    Gun_ID,
    Country,
    Caliber,
    Turret_Type,
    Designation,
    Turret_Weight_Tons,
    Crew_Size,
    Armor_Face_IN,
    Armor_Sides_IN,
    Armor_Roof_IN,
    Traverse_Rate_Deg_Sec,
    Elevation_Min_Deg,
    Elevation_Max_Deg,
    Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM,
    Modded,
    Notes
)
SELECT
    Turret_ID,
    Gun_ID,
    Country,
    Caliber,
    Turret_Type,
    Designation,
    Turret_Weight_Tons,
    Crew_Size,
    Armor_Face_IN,
    Armor_Sides_IN,
    Armor_Roof_IN,
    Traverse_Rate_Deg_Sec,
    Elevation_Min_Deg,
    Elevation_Max_Deg,
    Elevation_Rate_Deg_Sec,
    Rate_Of_Fire_RPM,
    Modded,
    Notes
FROM Turrets;

-- Step 3: Drop old table
DROP TABLE Turrets;

-- Step 4: Rename new table to original name
ALTER TABLE Turrets_New RENAME TO Turrets;

-- Step 5: Verify record count
SELECT 'Migration complete. Record count:' as Status, COUNT(*) as Count FROM Turrets;
