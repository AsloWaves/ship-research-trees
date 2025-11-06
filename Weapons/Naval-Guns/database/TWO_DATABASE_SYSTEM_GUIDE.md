# Two Database System Guide
## Ships Database + Research Tree Database Integration

**Date**: October 10, 2025
**Purpose**: Explain how the two-database system works together

---

## 🎯 System Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    PLAYER GAME INTERFACE                       │
└────────────────────┬───────────────────────┬───────────────────┘
                     │                       │
                     │                       │
          ┌──────────▼──────────┐  ┌─────────▼──────────┐
          │  RESEARCH TREE DB   │  │   SHIPS DB         │
          │  (Unlock Logic)     │  │   (Stats & Specs)  │
          └──────────┬──────────┘  └─────────┬──────────┘
                     │                       │
                     │   Linked by          │
                     │   Ship_Class         │
                     │   field              │
                     │                       │
                     └───────────┬───────────┘
                                 │
                         ┌───────▼────────┐
                         │  GAME ENGINE   │
                         │  (Queries both)│
                         └────────────────┘
```

---

## 📊 Two Databases - Clear Separation

### **Database 1: Ships Database** 📈
**File**: `naval_ships_database.md`

**Purpose**: Store ship **specifications, statistics, and historical data**

**Contains**:
- Ship_ID (primary key)
- Ship_Name (e.g., "USS Iowa")
- Ship_Class (e.g., "Iowa-class")
- Displacement, dimensions, speed, range
- Armor values
- Crew complement
- Armament (guns, torpedoes, missiles)
- Aircraft complement
- Propulsion systems
- Service history
- **No research tree logic**

**Example Entry**:
```markdown
| Ship_ID | Country | Ship_Name | Ship_Class | Displacement_Tons | Main_Guns | Speed_KTS |
|---------|---------|-----------|------------|-------------------|-----------|-----------|
| 10001 | USA | USS Indiana | Indiana-class | 10288 | 4× 13"/35 | 15 |
| 10002 | USA | USS Massachusetts | Indiana-class | 10288 | 4× 13"/35 | 15 |
| 10004 | USA | USS Iowa | Iowa-class | 11410 | 4× 12"/40 | 17 |
```

---

### **Database 2: Research Tree Database** 🌲
**File**: `ship_research_tree_database.md`

**Purpose**: Manage **research progression, prerequisites, and unlock chains**

**Contains** (4 tables):

#### 1. **Research_Nodes** - Main progression nodes
- Node_ID (primary key)
- Ship_Class (links to Ships DB)
- Research_Cost_RP
- Research_Time_Months
- Tech_Branch, Tech_Tier
- Is_Starting_Tech
- **No ship stats**

#### 2. **Prerequisites** - What must be researched first
- Node_ID (what's being unlocked)
- Requires_Node_ID (what's required)
- AND/OR logic support

#### 3. **Unlocks** - What this unlocks
- Node_ID (what's completed)
- Unlocks_Node_ID (what becomes available)

#### 4. **Research_Branches** - Tech tree branches
- Branch definitions
- Branch colors, descriptions
- Start/end nodes

**Example Entries**:

**Research Nodes**:
```markdown
| Node_ID | Ship_Class | Research_Cost_RP | Research_Time_Months | Tech_Branch | Tech_Tier | Is_Starting_Tech |
|---------|------------|------------------|---------------------|-------------|-----------|------------------|
| 1001 | Indiana-class | 5000 | 12 | Coastal Defense | 1 | 1 |
| 1002 | Iowa-class | 8000 | 18 | Blue Water | 1 | 1 |
| 1003 | Kearsarge-class | 10000 | 24 | Coastal Defense | 2 | 0 |
```

**Prerequisites**:
```markdown
| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class |
|-----------------|---------|------------------|---------------------|
| 1 | 1003 | 1001 | Indiana-class |
```
*"Kearsarge requires Indiana"*

**Unlocks**:
```markdown
| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class |
|-----------|---------|-----------------|-------------------|
| 1 | 1001 | 1003 | Kearsarge-class |
```
*"Indiana unlocks Kearsarge"*

---

## 🔗 How They Link Together

### **Common Field: Ship_Class**

Both databases use **Ship_Class** as the linking field:

**Ships Database**:
```
Ship_Class = "Indiana-class"
    ├─ USS Indiana (BB-1)
    ├─ USS Massachusetts (BB-2)
    └─ USS Oregon (BB-3)
```

**Research Tree Database**:
```
Node_ID = 1001
Ship_Class = "Indiana-class"
Research_Cost_RP = 5000
```

### **Query Example**:

```sql
-- Player researches Node 1001 (Indiana-class)
-- Game needs to show:
--   1. What ships can now be built
--   2. Their specifications

SELECT
  s.Ship_ID,
  s.Ship_Name,
  s.Displacement_Tons,
  s.Main_Guns,
  s.Speed_KTS,
  rn.Research_Cost_RP
FROM Research_Nodes rn
JOIN Ships s ON rn.Ship_Class = s.Ship_Class
WHERE rn.Node_ID = 1001;

-- Returns: USS Indiana, Massachusetts, Oregon with full stats
```

---

## 🎮 Game Flow Example

### Scenario: Player starts new game (1890)

**Step 1: Game loads available research**
```sql
SELECT * FROM Research_Nodes
WHERE Is_Starting_Tech = 1
  AND Country = 'USA'
  AND Ship_Type = 'BB';

-- Returns: Node 1001 (Indiana), Node 1002 (Iowa)
```

**Step 2: Player chooses to research Indiana-class**
```
Cost: 5,000 RP
Time: 12 months
Action: Start research timer
```

**Step 3: Research completes (12 months later)**
```sql
-- Mark node as researched
INSERT INTO player_researched_nodes (node_id) VALUES (1001);

-- Check what unlocks
SELECT Unlocks_Node_ID, Unlocks_Ship_Class
FROM Unlocks
WHERE Node_ID = 1001;

-- Returns: Node 1003 (Kearsarge-class)
-- Display notification: "Kearsarge-class unlocked!"
```

**Step 4: Player wants to build a ship**
```sql
-- Get all ships from researched classes
SELECT s.*
FROM Ships s
WHERE s.Ship_Class IN (
  SELECT rn.Ship_Class
  FROM Research_Nodes rn
  JOIN player_researched_nodes p ON rn.Node_ID = p.node_id
);

-- Returns: Indiana, Massachusetts, Oregon (all Indiana-class)
-- Player can now build any of these ships
```

**Step 5: Player builds USS Indiana**
```
Build Cost: $3,020,000
Build Time: 36 months
Action: Start construction
```

---

## 📋 Data Flow Diagram

```
PLAYER ACTION: "Research Indiana-class"
         │
         ▼
┌─────────────────────────┐
│  Research Tree DB       │
│  Query: Node 1001       │
│  Cost: 5,000 RP         │
│  Time: 12 months        │
└───────────┬─────────────┘
            │
            │ Research completes
            ▼
┌─────────────────────────┐
│  Research Tree DB       │
│  Check Unlocks table    │
│  → Kearsarge unlocked   │
└───────────┬─────────────┘
            │
            │ Player wants to build
            ▼
┌─────────────────────────┐
│  Ships DB               │
│  Query: Ship_Class =    │
│    "Indiana-class"      │
│  → Returns 3 ships      │
└───────────┬─────────────┘
            │
            │ Player selects USS Indiana
            ▼
┌─────────────────────────┐
│  Ships DB               │
│  Get full specs:        │
│  • Displacement: 10,288t│
│  • Guns: 4× 13"/35      │
│  • Speed: 15 knots      │
│  • Build cost: $3.02M   │
│  • Build time: 36 mo    │
└─────────────────────────┘
            │
            ▼
     SHIP CONSTRUCTED
```

---

## 🔍 Why This Separation?

### **Advantages of Two-Database System**

1. **Clean Separation of Concerns**
   - Ships DB = "What are the specs?"
   - Research Tree DB = "How do I unlock it?"

2. **Flexible Research Paths**
   - Multiple classes can unlock same ship
   - OR logic (Illinois OR Maine → Connecticut)
   - AND logic (Indiana AND Kearsarge → Illinois)

3. **Easy to Modify**
   - Change research costs without touching ship stats
   - Add new research branches without modifying ships
   - Balance gameplay separately from historical accuracy

4. **Multiple Ships Per Class**
   - One research node (Indiana-class)
   - Multiple ships (Indiana, Massachusetts, Oregon)
   - Research once, build many

5. **Historical vs Gameplay**
   - Ships DB = historically accurate stats
   - Research Tree DB = balanced gameplay progression

6. **Easy Queries**
   - "What can I research?" → Research Tree DB only
   - "What are the stats?" → Ships DB only
   - "What can I build?" → Join both databases

---

## 📊 Example: Two Branches Converge

### Research Tree Logic

```
BRANCH 1: Coastal Defense          BRANCH 2: Blue Water
    │                                   │
    ▼                                   ▼
[1001] Indiana-class              [1002] Iowa-class
    │                                   │
    │ Unlocks                           │ Unlocks
    ▼                                   ▼
[1003] Kearsarge-class            [1008] Maine-class
    │                                   │
    └────────────┬──────────────────────┘
                 │ Both unlock
                 ▼
         [1007] Illinois-class
    (Requires Indiana AND Kearsarge)
```

### Prerequisites Table Shows This:

```markdown
| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required |
|-----------------|---------|------------------|---------------------|-------------|
| 2 | 1007 | 1001 | Indiana-class | 1 |
| 3 | 1007 | 1003 | Kearsarge-class | 1 |
```

**Game Logic**:
- Player has Indiana (1001) ✅
- Player does NOT have Kearsarge (1003) ❌
- **Illinois is still locked** 🔒

Player researches Kearsarge:
- Player has Indiana (1001) ✅
- Player has Kearsarge (1003) ✅
- **Illinois unlocks!** 🔓

---

## 🎯 Implementation Checklist

### Database Setup
- [x] Create Ships Database schema
- [x] Create Research Tree Database schema
- [x] Define Ship_Class as linking field
- [ ] Populate USA battleship nodes (1890-1900)
- [ ] Populate USA battleship ships (1890-1900)
- [ ] Test queries for unlock logic
- [ ] Test queries for ship stats retrieval

### Game Integration
- [ ] Implement RP generation system
- [ ] Implement research timer
- [ ] Implement prerequisite checking
- [ ] Implement unlock notifications
- [ ] Implement build menu filtering
- [ ] Implement branch visualization

---

## 📚 Summary

### **Ships Database**
- **What**: Ship specifications and statistics
- **Fields**: Displacement, speed, guns, armor, crew, etc.
- **Purpose**: Historical accuracy, combat calculations
- **One entry per ship**: USS Indiana, USS Massachusetts, etc.

### **Research Tree Database**
- **What**: Research progression and unlock logic
- **Fields**: Prerequisites, unlocks, RP costs, branches
- **Purpose**: Gameplay balance, tech tree navigation
- **One entry per class**: Indiana-class (unlocks 3 ships)

### **Link**
- Both use **Ship_Class** field
- Research Tree → Ships: "I researched Indiana-class, show me buildable ships"
- Ships → Research Tree: "I want Iowa, what research is needed?"

---

## ✅ Benefits

✅ **Separation of concerns** - Stats vs progression logic
✅ **Flexible research paths** - Complex branching/merging
✅ **Easy to balance** - Modify costs without touching stats
✅ **Scalable** - Easy to add new nations, eras, branches
✅ **Clean queries** - Efficient game logic
✅ **Historical accuracy** - Ships DB stays factual
✅ **Gameplay fun** - Research Tree balances gameplay

---

**Status**: ✅ System architecture complete
**Ready for**: Population of USA battleship data (1890-1900)
**Next Step**: Create first 5-10 research nodes with full integration

**Created**: October 10, 2025
