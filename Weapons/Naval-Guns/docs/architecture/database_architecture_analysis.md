# Database Architecture Analysis: Single vs. Multi-Country Databases

**Date**: October 2025
**Current Status**: 100% USA content (83 guns, 1,700 turrets, 72 ammunition)
**Question**: Separate databases per country vs. unified database?

---

## Executive Summary

**Recommendation**: **Keep Single Unified Database** with Country filtering

**Rationale**:
- ✅ Cross-country comparisons essential for game balance
- ✅ Negligible performance impact (even with 4 countries = ~10MB)
- ✅ Simpler game code (one connection, simple WHERE filters)
- ✅ Supports multi-national ships and captured weapons
- ✅ Better for modding and future expansion

**Exception Cases** where separate databases make sense:
- Downloadable country packs (DLC model)
- Platform limitations (mobile with extreme storage constraints)
- Licensing restrictions (different publishers per region)

---

## Current Database Status

```
naval_guns.db
├── Guns:           83 (all USA)
├── Ammunition:     72 (all USA)
├── Turrets:      1,700 (all USA)
├── Compatibility: 112
└── Size:         ~2.5 MB
```

**Projected with 4 countries** (USA, Britain, Germany, Japan):
```
Estimated Total:
├── Guns:          ~330 (83 × 4)
├── Ammunition:    ~290 (72 × 4)
├── Turrets:     ~6,800 (1,700 × 4)
├── Compatibility: ~450 (112 × 4)
└── Size:        ~10-12 MB
```

---

## Option A: Single Unified Database (RECOMMENDED)

### Architecture

```
naval_guns.db (10-12 MB)
├── Guns (USA, Britain, Germany, Japan)
├── Ammunition (USA, Britain, Germany, Japan)
├── Turrets (USA, Britain, Germany, Japan)
└── Compatibility (all countries)
```

### Schema (No Changes)

```sql
CREATE TABLE Guns (
    Gun_ID INTEGER PRIMARY KEY,
    Country TEXT,  -- 'USA', 'Britain', 'Germany', 'Japan'
    Caliber TEXT,
    ...
);

CREATE TABLE Turrets (
    Turret_ID INTEGER PRIMARY KEY,
    Gun_ID INTEGER,
    Country TEXT,  -- 'USA', 'Britain', 'Germany', 'Japan'
    Caliber TEXT,
    ...
);
```

### Query Patterns

```sql
-- Filter by country (simple WHERE clause)
SELECT * FROM Turrets WHERE Country = 'USA';

-- Cross-country comparison
SELECT
    Country,
    Caliber,
    AVG(Muzzle_Velocity_FPS) as Avg_Velocity,
    MAX(Max_Range_Yards) as Max_Range
FROM Gun_Ammunition_Compatibility gac
JOIN Guns g ON gac.Gun_ID = g.Gun_ID
WHERE Caliber = '16"'
GROUP BY Country, Caliber
ORDER BY Max_Range DESC;

-- Multi-national ship loadout
SELECT * FROM Turrets
WHERE Turret_ID IN (
    :usa_turret_id,      -- USS Iowa turret
    :britain_turret_id,  -- Vanguard turret (for comparison)
    :japan_turret_id     -- Yamato turret (for comparison)
);
```

### Pros ✅

1. **Cross-Country Comparisons**
   - Compare gun performance across nations easily
   - Essential for game balance and player research
   - Example: "Is Iowa's 16"/50 better than Yamato's 18.1"/45?"

2. **Unified Game Logic**
   - Single database connection
   - Simple WHERE Country = ? filters
   - No complex multi-DB query coordination

3. **Historical Accuracy**
   - Captured weapons (e.g., Japanese ships with US guns post-war)
   - Lend-lease equipment (e.g., British ships with US guns)
   - International arms sales

4. **Performance**
   - 10-12 MB is trivial in 2025 (fits entirely in RAM)
   - SQLite handles this effortlessly (<1ms queries)
   - Indexes work across all countries

5. **Modding & Expansion**
   - Easy to add new countries (just insert rows)
   - Community mods can add nations seamlessly
   - No file juggling for modders

6. **Statistics & Analytics**
   - Global statistics across all nations
   - "Most powerful gun ever made" queries
   - Historical timeline comparisons

7. **Simpler Maintenance**
   - One schema to update
   - One backup file
   - One migration path

### Cons ⚠️

1. **File Size**
   - 10-12 MB (vs 2.5 MB per country)
   - Still negligible by modern standards

2. **"Bloat" Perception**
   - Players who only use USA see other countries' data
   - Reality: 12MB is smaller than most game textures

3. **Mod Conflicts**
   - Two mods modifying same country could conflict
   - Mitigation: Namespace by mod author

### Implementation Example

```python
# Game code - single connection
import sqlite3

db = sqlite3.connect('naval_guns.db')

# Get USA turrets
usa_turrets = db.execute('''
    SELECT * FROM Turrets
    WHERE Country = ?
    ORDER BY Caliber, Designation
''', ('USA',)).fetchall()

# Compare 16" guns across countries
comparison = db.execute('''
    SELECT
        g.Country,
        g.Mark_Designation,
        gac.Muzzle_Velocity_FPS,
        gac.Max_Range_Yards
    FROM Guns g
    JOIN Gun_Ammunition_Compatibility gac ON g.Gun_ID = gac.Gun_ID
    WHERE g.Caliber = '16"'
    ORDER BY gac.Max_Range_Yards DESC
''').fetchall()
```

---

## Option B: Separate Country Databases

### Architecture

```
naval_guns_usa.db     (2.5 MB)
naval_guns_britain.db (2.5 MB)
naval_guns_germany.db (2.5 MB)
naval_guns_japan.db   (2.5 MB)
```

Each database contains identical schema, different data.

### Query Patterns

```python
# Game code - multiple connections
import sqlite3

db_usa = sqlite3.connect('naval_guns_usa.db')
db_britain = sqlite3.connect('naval_guns_britain.db')
db_germany = sqlite3.connect('naval_guns_germany.db')
db_japan = sqlite3.connect('naval_guns_japan.db')

# Get USA turrets (simple)
usa_turrets = db_usa.execute('SELECT * FROM Turrets').fetchall()

# Cross-country comparison (COMPLEX!)
usa_16inch = db_usa.execute(
    "SELECT 'USA' as Country, * FROM Guns WHERE Caliber = '16\"'"
).fetchall()

britain_16inch = db_britain.execute(
    "SELECT 'Britain' as Country, * FROM Guns WHERE Caliber = '16\"'"
).fetchall()

# Manually merge results
all_16inch = usa_16inch + britain_16inch
all_16inch.sort(key=lambda x: x['max_range'], reverse=True)
```

### Pros ✅

1. **Smaller Individual Files**
   - 2.5 MB each instead of 10-12 MB total
   - Easier to distribute as separate downloads

2. **Memory Optimization**
   - Only load countries player is using
   - Useful for extreme low-memory environments

3. **Clean Separation**
   - No cross-country data pollution
   - Each DB is self-contained

4. **Parallel Updates**
   - Different team members can work on different countries
   - Less merge conflict risk

5. **DLC Model**
   - Sell/distribute countries as separate DLC packs
   - "Buy Japan Naval Weapons Pack - $4.99"

### Cons ⚠️

1. **Complex Cross-Country Queries**
   - No SQL JOIN across databases (without ATTACH)
   - Must query each DB separately and merge in code
   - Performance penalty for cross-DB operations

2. **Multi-National Ships**
   - Can't easily model captured weapons
   - Lend-lease equipment requires duplication
   - Historical accuracy compromised

3. **Duplicate Schema**
   - 4 identical schemas to maintain
   - Schema updates must be applied to 4 files
   - Migration scripts run 4 times

4. **Game Code Complexity**
   ```python
   # Managing 4 connections
   dbs = {
       'USA': sqlite3.connect('naval_guns_usa.db'),
       'Britain': sqlite3.connect('naval_guns_britain.db'),
       'Germany': sqlite3.connect('naval_guns_germany.db'),
       'Japan': sqlite3.connect('naval_guns_japan.db'),
   }

   # Every query needs country router
   def get_turrets(country):
       return dbs[country].execute('SELECT * FROM Turrets').fetchall()
   ```

5. **No Global Statistics**
   - "Heaviest gun ever made" requires querying all 4 DBs
   - Performance comparisons require aggregation code

6. **Modding Challenges**
   - Mods must specify which country DB to modify
   - Cross-country mods require touching multiple files
   - Version conflicts multiplied by 4

7. **Backup & Distribution**
   - 4 files to backup
   - 4 files to version
   - 4 files to download/update

### Implementation Example

```python
import sqlite3
from typing import Dict

class MultiCountryDB:
    def __init__(self):
        self.connections = {
            'USA': sqlite3.connect('naval_guns_usa.db'),
            'Britain': sqlite3.connect('naval_guns_britain.db'),
            'Germany': sqlite3.connect('naval_guns_germany.db'),
            'Japan': sqlite3.connect('naval_guns_japan.db'),
        }

    def get_turrets(self, country: str):
        return self.connections[country].execute(
            'SELECT * FROM Turrets'
        ).fetchall()

    def compare_16inch_guns(self):
        """Complex: must query each DB and merge"""
        results = []
        for country, db in self.connections.items():
            guns = db.execute('''
                SELECT * FROM Guns WHERE Caliber = '16"'
            ''').fetchall()
            for gun in guns:
                results.append({'country': country, **gun})

        # Sort merged results
        results.sort(key=lambda x: x['max_range'], reverse=True)
        return results
```

---

## Hybrid Option C: Single DB + Country Indexes

### Architecture

Single database with country-specific indexes for performance.

```sql
-- Create indexes for each country
CREATE INDEX idx_guns_usa ON Guns(Country) WHERE Country = 'USA';
CREATE INDEX idx_guns_britain ON Guns(Country) WHERE Country = 'Britain';
CREATE INDEX idx_guns_germany ON Guns(Country) WHERE Country = 'Germany';
CREATE INDEX idx_guns_japan ON Guns(Country) WHERE Country = 'Japan';

-- Same for other tables
CREATE INDEX idx_turrets_usa ON Turrets(Country) WHERE Country = 'USA';
-- ... etc
```

### Benefits

✅ Single database (all Option A benefits)
✅ Optimized country filtering (near-zero overhead)
✅ Best of both worlds

### Cost

⚠️ Slightly larger DB file (~5-10% overhead for indexes)
⚠️ Minimal maintenance (indexes auto-update)

---

## Decision Matrix

| Criterion | Single DB | Multi-DB | Hybrid |
|-----------|-----------|----------|--------|
| **Cross-country queries** | ✅ Easy | ❌ Complex | ✅ Easy |
| **File size** | ⚠️ 10-12 MB | ✅ 2.5 MB each | ⚠️ 12-15 MB |
| **Game code complexity** | ✅ Simple | ❌ Complex | ✅ Simple |
| **Performance** | ✅ Excellent | ⚠️ Good | ✅ Excellent |
| **Multi-national ships** | ✅ Supported | ❌ Difficult | ✅ Supported |
| **Modding** | ✅ Easy | ⚠️ Moderate | ✅ Easy |
| **DLC distribution** | ⚠️ Harder | ✅ Natural | ⚠️ Harder |
| **Maintenance** | ✅ Single schema | ❌ 4x effort | ✅ Single schema |
| **Backup** | ✅ One file | ❌ 4 files | ✅ One file |

---

## Use Case Analysis

### If Your Game...

**Has cross-nation battles/comparisons** → **Single DB**
- Players need to compare USA vs Japan equipment
- Balance decisions require cross-country data

**Is purely single-nation campaigns** → **Multi-DB (maybe)**
- Each campaign uses only one country
- No cross-country interactions ever

**Includes captured/lend-lease weapons** → **Single DB**
- Historical accuracy requires multi-national data
- Example: Soviet ships with US guns

**Sells country packs as DLC** → **Multi-DB**
- Clean separation for distribution
- Players only download what they buy

**Supports modding** → **Single DB**
- Simpler for mod authors
- Easier to merge community content

**Targets mobile platforms** → **Multi-DB (maybe)**
- Smaller downloads per country pack
- But 10-12 MB is still tiny

---

## Recommended Architecture

### Primary Recommendation: **Single Unified Database**

```
naval_guns.db (10-12 MB with 4 countries)
├── Country column in all tables
├── Optional: Country-specific indexes
└── Simple WHERE Country = ? filters
```

**Rationale**:
1. Game likely needs cross-country comparisons
2. 10-12 MB is negligible in 2025 (smaller than a single texture)
3. Much simpler game code
4. Supports multi-national scenarios
5. Better for modding community

### When to Use Multi-DB Instead

**Only if 2+ of these apply**:
- ✓ DLC/paid country packs business model
- ✓ Absolutely zero cross-country interaction
- ✓ Platform storage constraints (<50MB total)
- ✓ Different publishers per region

---

## Performance Comparison

### Single DB with Country Filter

```sql
-- Query: Get all USA 16" turrets
SELECT * FROM Turrets
WHERE Country = 'USA' AND Caliber = '16"';

-- Performance: <0.5ms (with index)
-- Complexity: O(log n) with index on Country
```

### Multi-DB

```python
# Query: Get all 16" turrets from all countries
results = []
for db in [usa_db, britain_db, germany_db, japan_db]:
    results.extend(db.execute(
        "SELECT * FROM Turrets WHERE Caliber = '16\""
    ).fetchall())

# Performance: ~1-2ms (4 separate queries)
# Complexity: 4x queries + merge overhead
```

**Verdict**: Single DB is faster for cross-country queries, similar speed for single-country.

---

## Migration Path

If you choose **Single DB** (recommended):

1. **No changes needed** - current schema already supports multiple countries
2. **Adding Britain**:
   ```sql
   INSERT INTO Guns (Country, Caliber, Mark_Designation, ...)
   VALUES ('Britain', '15"', 'Mark I', ...);
   ```
3. **Filtering**:
   ```sql
   SELECT * FROM Turrets WHERE Country = 'Britain';
   ```

If you later need **Multi-DB**:

1. **Split existing database**:
   ```bash
   sqlite3 naval_guns.db <<EOF
   ATTACH 'naval_guns_usa.db' AS usa;
   CREATE TABLE usa.Guns AS SELECT * FROM Guns WHERE Country = 'USA';
   # ... repeat for each table and country
   EOF
   ```

2. **Maintain both** (not recommended but possible)

---

## Recommendation Summary

### ✅ **Use Single Unified Database**

**Why:**
- Cross-country comparisons are valuable for gameplay
- 10-12 MB is trivial file size
- Simpler code, easier maintenance
- Future-proof for multi-national content
- Better modding support

**When to reconsider:**
- You're implementing paid DLC country packs
- You absolutely need smallest possible file sizes
- You have zero cross-country gameplay

### 🎯 **Implementation Steps**

1. **Keep current schema** (already perfect)
2. **Add indexes for performance**:
   ```sql
   CREATE INDEX idx_guns_country ON Guns(Country);
   CREATE INDEX idx_turrets_country ON Turrets(Country);
   CREATE INDEX idx_ammunition_country ON Ammunition(Country);
   ```
3. **Filter by country in queries**:
   ```sql
   WHERE Country = ?
   ```
4. **Add countries incrementally** (Britain, Germany, Japan)

---

## Final Verdict

**Keep the single unified database.** The benefits far outweigh the minimal cost of a slightly larger file. Your game will be easier to develop, easier to balance, and more flexible for future features.

**File size is not a concern** - 10-12 MB for the complete database with all 4 major naval powers is smaller than most texture files in modern games.

---

## Questions to Ask Yourself

Before making the final decision:

1. **Will players compare guns across countries?** (Yes → Single DB)
2. **Are you selling country packs as DLC?** (Yes → Maybe Multi-DB)
3. **Do you support multi-national ships?** (Yes → Single DB)
4. **Is 10-12 MB a file size concern?** (No → Single DB)
5. **Do you want simple or complex game code?** (Simple → Single DB)

**Most likely answer: Single Unified Database** ✅
