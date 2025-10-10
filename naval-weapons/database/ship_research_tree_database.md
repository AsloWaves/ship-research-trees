# Ship Research Tree Database

**Export Date**: October 10, 2025
**Database Version**: 1.0
**Total Records**: 135 (47 Research Nodes + 40 Prerequisites + 40 Unlocks + 8 Research Branches)

---

## Database Purpose

This database manages the **research progression and unlock logic** for naval ship development. It is **separate from the Ships Database** to maintain clean separation of concerns:

- **Ships Database** = Ship specifications, stats, historical data
- **Research Tree Database** = Research progression, prerequisites, unlock chains

**Progression Philosophy**: This tree uses **strength-based progression** where tiers represent combat power increases rather than strict chronological order. Players progress from weakest (Tier 1 pre-dreadnoughts) to strongest (Tier 9 super battleship Montana), with meaningful choices at each tier where ships offer similar power levels.

---

## Database Contents

- [Research Nodes Table](#research-nodes-table) - Main research progression nodes
- [Prerequisites Table](#prerequisites-table) - What must be researched first
- [Unlocks Table](#unlocks-table) - What this research unlocks
- [Research Branches Table](#research-branches-table) - Tech tree branch definitions

---

<a name="research-nodes-table"></a>
## Research Nodes Table

**Schema Definition**:

| Field | Type | Description |
|-------|------|-------------|
| Node_ID | INT | Primary key, unique identifier |
| Country | VARCHAR(50) | Nation (USA, British, German, Japanese) |
| Ship_Class | VARCHAR(100) | Ship class name (links to Ships Database) |
| Ship_Type | VARCHAR(50) | BB, CV, CA, CL, DD, SS, etc. |
| Tech_Branch | VARCHAR(100) | Branch name (e.g., "Coastal Defense", "Blue Water", "Main Line") |
| Tech_Tier | INT | Tier in progression (1=starting, 2=early, 3=mid, etc.) |
| Era | VARCHAR(50) | Pre-Dreadnought, Dreadnought, Treaty Era, Fast BB, Modern, etc. |
| Year_Available | INT | Historical year this tech becomes available |
| Is_Starting_Tech | TINYINT | 1 = available at game start, 0 = must research |
| Research_Cost_RP | INT | Research Points required to unlock |
| Research_Time_Months | INT | Months required to complete research |
| Build_Cost_USD | BIGINT | Cost to build one ship of this class |
| Build_Time_Months | INT | Months to construct one ship |
| Design_Philosophy | VARCHAR(200) | Brief design concept (Armor, Speed, Firepower, etc.) |
| Historical_Context | TEXT | Why this class was developed |
| Gameplay_Role | VARCHAR(200) | Role in game (Tank, DPS, Scout, etc.) |
| Special_Ability | VARCHAR(200) | Unique ability or bonus |
| Notes | TEXT | Additional research tree information |

**Total Entries**: 47 nodes (USA Battleships complete)
**ID Allocation**:
- USA: 1000-1999 (47 battleship nodes used)
- British: 2000-2999
- German: 3000-3999
- Japanese: 4000-4999
**Paper Ship IDs**: 2000-2999 within USA range

| Node_ID | Country | Ship_Class | Ship_Type | Tech_Branch | Tech_Tier | Era | Year_Available | Is_Starting_Tech | Research_Cost_RP | Research_Time_Months | Build_Cost_USD | Build_Time_Months | Design_Philosophy | Historical_Context | Gameplay_Role | Special_Ability | Notes |
|---------|---------|------------|-----------|-------------|-----------|-----|----------------|------------------|------------------|---------------------|----------------|-------------------|-------------------|-------------------|---------------|-----------------|-------|
| 1000 | USA | Texas (BB-1) | BB | Starting | 1 | Pre-Dreadnought | 1890 | 1 | 0 | 0 | 2500000 | 24 | Second-class BB | First US battleship, experimental design | Tutorial Ship | Old Reliable: -20% maintenance cost | FREE starting ship |
| 1001 | USA | Indiana-class | BB | Coastal Defense | 1 | Pre-Dreadnought | 1890 | 1 | 5000 | 12 | 3020000 | 36 | Heavy armor + firepower | Naval Act of 1890, first true US battleships | Coastal Fortress | +20% armor, -2 speed | Low freeboard limits seakeeping |
| 1002 | USA | Maine-class | BB | Blue Water | 1 | Pre-Dreadnought | 1902 | 1 | 5000 | 12 | 4300000 | 36 | Long range specialist | Alternative 12" gun philosophy | Power Projection | +15% max range | Emphasizes range over armor |
| 1003 | USA | Kearsarge-class | BB | Experimental | 2 | Pre-Dreadnought | 1900 | 0 | 3000 | 8 | 3760000 | 36 | Experimental firepower | Superimposed turret experiment (failed) | Experimental DPS | +15% firepower, -10% accuracy | DEAD END - blast interference |
| 1004 | USA | Illinois-class | BB | Coastal Defense | 2 | Pre-Dreadnought | 1900 | 0 | 8000 | 18 | 4200000 | 36 | Improved Indiana | Lessons from Indiana operational experience | Balanced BB | Balanced stats | Improved freeboard design |
| 1005 | USA | Virginia-class | BB | Main Line | 2 | Pre-Dreadnought | 1906 | 0 | 8000 | 18 | 4500000 | 36 | Mixed armament era | Transitional design philosophy | Mixed Role | Flexible armament | 12" + 8" guns |
| 1006 | USA | Connecticut-class | BB | Main Line | 2 | Pre-Dreadnought | 1906 | 0 | 10000 | 24 | 5000000 | 42 | Peak pre-dreadnought | Largest pre-dreadnought class, Great White Fleet | Elite Pre-Dread | Great White Fleet: +10% prestige | 6 ships, most numerous class |
| 1007 | USA | Mississippi-class | BB | Main Line | 2 | Pre-Dreadnought | 1908 | 0 | 12000 | 30 | 4800000 | 36 | Final pre-dreadnought | Originally built for Greece, repurchased | Bridge Ship | Foreign design influence | Last pre-dreadnought design |
| 1010 | USA | South Carolina-class | BB | Main Line | 3 | Dreadnought | 1910 | 0 | 25000 | 48 | 6000000 | 48 | All big-gun revolution | First US dreadnought, superfiring turrets | Revolutionary | +25% penetration vs pre-dreads | Makes pre-dreads obsolete |
| 1011 | USA | Delaware-class | BB | Main Line | 3 | Dreadnought | 1910 | 0 | 15000 | 36 | 6500000 | 48 | More guns | 10× 12" guns vs 8× | Firepower Increase | +20% broadside weight | 5 twin turrets |
| 1012 | USA | Wyoming-class | BB | Main Line | 3 | Dreadnought | 1912 | 0 | 18000 | 42 | 7000000 | 54 | Maximum 12" firepower | Most 12" guns on US BB ever | Maximum Firepower | +30% fire rate (12 guns) | 6 twin turrets |
| 1014 | USA | New York-class | BB | Main Line | 4 | Dreadnought | 1914 | 0 | 20000 | 48 | 8000000 | 60 | First 14" guns | Revolutionary caliber jump | Penetration Specialist | +20% penetration vs 12" armor | Quantum leap in firepower |
| 1015 | USA | Nevada-class | BB | Main Line | 5 | Standard-Type | 1916 | 0 | 22000 | 48 | 9000000 | 60 | All-or-nothing armor | First Standard-type, new armor scheme | Tank | +30% critical hit resistance | Revolutionary armor philosophy |
| 1016 | USA | Pennsylvania-class | BB | Main Line | 5 | Standard-Type | 1916 | 0 | 18000 | 36 | 10000000 | 60 | More firepower | 12× 14" guns in all triple turrets | Heavy Firepower | +25% broadside weight | 4 triple turrets |
| 1017 | USA | New Mexico-class | BB | Main Line | 5 | Standard-Type | 1918 | 0 | 20000 | 42 | 11000000 | 66 | Refined Standard-type | Improved guns, turbo-electric drive | Refined BB | Turbo-electric: +5% efficiency | Best Standard-type design |
| 1019 | USA | Colorado-class | BB | Main Line | 6 | Standard-Type | 1921 | 0 | 25000 | 48 | 12000000 | 66 | First 16" guns | Ultimate pre-treaty battleship | Heavy Hitter | +25% penetration vs all targets | Largest guns in US inventory |
| 1020 | USA | North Carolina-class | BB | Main Line | 7 | Fast BB | 1941 | 0 | 35000 | 60 | 80000000 | 72 | First fast BB | Revolutionary 28-knot design, treaty limited | Fast Tank | +15% AA defense, +10% carrier escort | Breaks speed barrier |
| 1021 | USA | South Dakota (1939)-class | BB | Main Line | 7 | Fast BB | 1942 | 0 | 30000 | 48 | 85000000 | 72 | Optimized treaty design | Compact, best protection per ton | Armored Brawler | -10% target profile, +20% armor efficiency | Most efficient treaty BB |
| 1023 | USA | Iowa-class | BB | Main Line | 8 | Fast BB | 1943 | 0 | 50000 | 72 | 110000000 | 84 | Ultimate battleship | 33 knots, longest US BBs ever | Ultimate Warrior | All stats +10% | Pinnacle of BB design |
| 1050 | USA | Arkansas Monitor | BB | Alternative | 2 | Pre-Dreadnought | 1902 | 0 | 2000 | 6 | 1500000 | 18 | Coastal defense monitor | Small, cheap coastal defender | Coastal Specialist | +30% coastal defense, -50% ocean range | Alternative budget path |
| 1064 | USA | New York (1926 Refit) | BB | Modernization | 4 | Dreadnought | 1926 | 0 | 7000 | 12 | 0 | 0 | Modernization program | Coal to oil, improved AA | Upgraded 14" BB | +40% AA capability, +9000nm range | Refit only, not buildable new |
| 1065 | USA | Nevada (1927 Refit) | BB | Modernization | 5 | Standard-Type | 1927 | 0 | 8000 | 12 | 0 | 0 | Modernization program | New boilers, extended range | Upgraded Standard | +9000nm range (to 15700nm) | Refit only |
| 1066 | USA | Pennsylvania (1931 Refit) | BB | Modernization | 5 | Standard-Type | 1931 | 0 | 6000 | 12 | 0 | 0 | Fire control upgrade | Improved FCS and AA | Upgraded AA | +25% AA accuracy | Refit only |
| 1067 | USA | New Mexico (1931 Refit) | BB | Modernization | 5 | Standard-Type | 1931 | 0 | 6000 | 12 | 0 | 0 | Protection improvement | Enhanced armor scheme | Improved Protection | +15% torpedo resistance | Refit only |
| 1068 | USA | Tennessee (1943 Rebuild) | BB | Modernization | 6 | Standard-Type | 1943 | 0 | 16000 | 18 | 45000000 | 18 | Pearl Harbor rebuild | Complete reconstruction after Pearl | Modern Standard | +200% AA effectiveness, radar | Major rebuild, widened hull |
| 1069 | USA | California (1944 Rebuild) | BB | Modernization | 6 | Standard-Type | 1944 | 0 | 16000 | 18 | 45000000 | 18 | Pearl Harbor rebuild | Complete reconstruction | Modern Standard | +200% AA effectiveness, radar | Similar to Tennessee rebuild |
| 1070 | USA | Colorado (1941 Refit) | BB | Modernization | 6 | Standard-Type | 1941 | 0 | 8000 | 12 | 0 | 0 | Pre-war upgrade | AA and fire control improvements | Upgraded 16" BB | +30% AA capability | Refit only |
| 1071 | USA | West Virginia (1944 Rebuild) | BB | Modernization | 6 | Standard-Type | 1944 | 0 | 22000 | 18 | 60000000 | 18 | Ultimate rebuild | Sunk by 7 torpedoes, completely rebuilt | Ultimate Standard | +30% torpedo defense, +250% AA | Most extensive reconstruction ever |
| 1072 | USA | North Carolina (1945 Refit) | BB | Modernization | 7 | Fast BB | 1945 | 0 | 10000 | 6 | 0 | 0 | Wartime AA upgrade | Enhanced AA battery to 96+ guns | AA Platform | +40% AA effectiveness | Refit only |
| 1073 | USA | South Dakota (1945 Refit) | BB | Modernization | 7 | Fast BB | 1945 | 0 | 10000 | 6 | 0 | 0 | Wartime AA upgrade | Enhanced AA to 145 guns | Maximum AA | +50% AA effectiveness | Most AA guns on US BB |
| 1074 | USA | Iowa (1945 Refit) | BB | Modernization | 8 | Fast BB | 1945 | 0 | 12000 | 6 | 0 | 0 | Wartime upgrades | Enhanced AA and radar | Modern Iowa | +30% AA, +25% radar effectiveness | Refit only |
| 1080 | USA | Iowa (1984 Reactivation) | BB | Modernization | 8 | Modern | 1984 | 0 | 75000 | 36 | 1700000000 | 30 | Reagan 600-ship Navy | Tomahawk missiles, Phalanx, modern electronics | Modern Battleship | 32× Tomahawk, 16× Harpoon, Phalanx | Extends to 1992, ultimate refit |
| 2000 | USA | Tillman I | BB | Paper Ship | 5 | Treaty Era | 1917 | 0 | 14000 | 36 | 40000000 | 60 | Standard Maximum | 70,000-ton maximum battleship study | Paper Tank | -10% reliability (unproven) | Never built, theoretical design |
| 2001 | USA | Tillman II | BB | Paper Ship | 5 | Treaty Era | 1917 | 0 | 18000 | 42 | 45000000 | 66 | Sextuple Turret | 24× 16" in 4 sextuple turrets | Paper Madness | Unique sextuple turrets, -15% reliability | Most guns ever designed |
| 2002 | USA | Tillman IV | BB | Paper Ship | 5 | Treaty Era | 1917 | 0 | 20000 | 48 | 55000000 | 72 | Ultimate Maximum | 80,000-ton, 18" belt armor | Paper Fortress | 18" belt, -10% reliability | Largest design |
| 2010 | USA | Lexington Battlecruiser | BC | Paper Ship | 6 | Treaty Era | 1920 | 0 | 20000 | 42 | 40000000 | 48 | Fast raider | 35-knot battlecruiser, converted to CV | Fast Glass Cannon | +8 knots speed, -30% armor | Speed vs armor tradeoff |
| 2011 | USA | Tillman III | BB | Paper Ship | 5 | Treaty Era | 1917 | 0 | 15000 | 36 | 42000000 | 60 | Fast Maximum | 30-knot, 63,500-ton design | Paper Fast BB | 30 knots, -10% reliability | Speed emphasis |
| 2020 | USA | South Dakota (1920) | BB | Paper Ship | 6 | Treaty Era | 1920 | 0 | 25000 | 48 | 50000000 | 60 | Treaty victim | Ultimate Standard-type, cancelled by treaty | Paper Standard | -10% reliability | Cancelled 1922 |
| 2021 | USA | Tillman IV-2 | BB | Paper Ship | 5 | Treaty Era | 1917 | 0 | 25000 | 54 | 60000000 | 72 | 18-inch Monster | 15× 18" guns, largest caliber | Paper Super-Heavy | 18" guns, -15% reliability | Largest guns ever designed for USN |
| 2030 | USA | Lexington Completed | BC | Paper Ship | 6 | Treaty Era | 1920 | 0 | 22000 | 48 | 45000000 | 54 | What-if completion | If Lexington stayed as battlecruiser | What-If BC | 33 knots, 8× 16" guns | Alternative history |
| 2031 | USA | Alaska-class | CB | Alternative | 7 | Fast BB | 1941 | 0 | 18000 | 36 | 75000000 | 36 | Large Cruiser | Battlecruiser in all but name, 9× 12" guns | Cruiser Killer | +20% vs cruisers, 33 knots | 2 built, 4 cancelled |
| 2040 | USA | Montana-class | BB | Paper Ship | 9 | Fast BB | 1943 | 0 | 60000 | 84 | 120000000 | 84 | Super battleship | 12× 16" guns, ultimate design | Paper Ultimate | 12× 16" guns, -10% reliability | Cancelled July 1943, Iowa successor. Ultimate battleship. Could receive hypothetical modernization. |

---

<a name="prerequisites-table"></a>
## Prerequisites Table

**Schema Definition**:

Defines what must be researched before a node becomes available. Allows multiple prerequisites (AND logic).

| Field | Type | Description |
|-------|------|-------------|
| Prerequisite_ID | INT | Primary key |
| Node_ID | INT | Foreign key to Research_Nodes (the node being unlocked) |
| Requires_Node_ID | INT | Foreign key to Research_Nodes (required prerequisite) |
| Requires_Ship_Class | VARCHAR(100) | Ship class name (human-readable) |
| Is_Required | TINYINT | 1 = MUST have (AND), 0 = optional (OR) |
| Alternative_Group | INT | For OR logic: nodes in same group are alternatives |
| Notes | TEXT | Special prerequisite conditions |

**Logic Examples**:
- **Simple prerequisite**: Node 1003 (Kearsarge) requires Node 1001 (Indiana)
- **Multiple prerequisites (AND)**: Node 1007 (Illinois) requires BOTH Node 1001 (Indiana) AND Node 1003 (Kearsarge)
- **Alternative prerequisites (OR)**: Node 1010 (Connecticut) requires Node 1007 (Illinois) OR Node 1008 (Maine)

| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 1 | 1003 | 1001 | Indiana-class | 1 | NULL | Kearsarge requires Indiana |
| 2 | 1004 | 1001 | Indiana-class | 1 | NULL | Illinois requires Indiana |
| 3 | 1005 | 1002 | Maine-class | 1 | NULL | Virginia requires Maine |
| 4 | 1006 | 1004 | Illinois-class | 1 | 1 | Connecticut requires Illinois OR Virginia |
| 5 | 1006 | 1005 | Virginia-class | 1 | 1 | Connecticut requires Illinois OR Virginia (alternative) |
| 6 | 1007 | 1006 | Connecticut-class | 1 | NULL | Mississippi requires Connecticut |
| 7 | 1010 | 1007 | Mississippi-class | 1 | NULL | South Carolina requires Mississippi |
| 8 | 1011 | 1010 | South Carolina-class | 1 | NULL | Delaware requires South Carolina |
| 9 | 1012 | 1011 | Delaware-class | 1 | NULL | Wyoming requires Delaware |
| 10 | 1014 | 1012 | Wyoming-class | 1 | NULL | New York requires Wyoming |
| 11 | 1015 | 1014 | New York-class | 1 | NULL | Nevada requires New York (14" guns unlock Standard-type) |
| 12 | 1016 | 1015 | Nevada-class | 1 | NULL | Pennsylvania requires Nevada |
| 13 | 1017 | 1016 | Pennsylvania-class | 1 | NULL | New Mexico requires Pennsylvania |
| 14 | 1019 | 1017 | New Mexico-class | 1 | NULL | Colorado requires New Mexico |
| 15 | 1020 | 1019 | Colorado-class | 1 | NULL | North Carolina requires Colorado (18-year gap) |
| 16 | 1021 | 1020 | North Carolina-class | 1 | NULL | South Dakota requires North Carolina |
| 17 | 1023 | 1021 | South Dakota (1939)-class | 1 | NULL | Iowa requires South Dakota |
| 18 | 1050 | 1000 | Texas (BB-1) | 1 | NULL | Arkansas Monitor requires Texas |
| 19 | 1064 | 1014 | New York-class | 1 | NULL | New York Refit requires base New York |
| 20 | 1065 | 1015 | Nevada-class | 1 | NULL | Nevada Refit requires base Nevada |
| 21 | 1066 | 1016 | Pennsylvania-class | 1 | NULL | Pennsylvania Refit requires base Pennsylvania |
| 22 | 1067 | 1017 | New Mexico-class | 1 | NULL | New Mexico Refit requires base New Mexico |
| 23 | 1068 | 1017 | New Mexico-class | 1 | NULL | Tennessee Rebuild requires Tennessee base (New Mexico-class group) |
| 24 | 1069 | 1017 | New Mexico-class | 1 | NULL | California Rebuild requires California base (New Mexico-class group) |
| 25 | 1070 | 1019 | Colorado-class | 1 | NULL | Colorado Refit requires base Colorado |
| 26 | 1071 | 1019 | Colorado-class | 1 | NULL | West Virginia Rebuild requires West Virginia base (Colorado-class group) |
| 27 | 1072 | 1020 | North Carolina-class | 1 | NULL | North Carolina Refit requires base North Carolina |
| 28 | 1073 | 1021 | South Dakota (1939)-class | 1 | NULL | South Dakota Refit requires base South Dakota |
| 29 | 1074 | 1023 | Iowa-class | 1 | NULL | Iowa 1945 Refit requires base Iowa |
| 30 | 1080 | 1023 | Iowa-class | 1 | NULL | Iowa 1984 Reactivation requires base Iowa |
| 31 | 2000 | 1015 | Nevada-class | 1 | NULL | Tillman I available after Standard-type unlocked |
| 32 | 2001 | 1015 | Nevada-class | 1 | NULL | Tillman II available after Standard-type unlocked |
| 33 | 2002 | 1015 | Nevada-class | 1 | NULL | Tillman IV available after Standard-type unlocked |
| 34 | 2010 | 1015 | Nevada-class | 1 | NULL | Lexington BC available after Standard-type unlocked |
| 35 | 2011 | 1015 | Nevada-class | 1 | NULL | Tillman III available after Standard-type unlocked |
| 36 | 2020 | 1019 | Colorado-class | 1 | NULL | South Dakota 1920 available after 16" guns |
| 37 | 2021 | 1015 | Nevada-class | 1 | NULL | Tillman IV-2 available after Standard-type unlocked |
| 38 | 2030 | 2010 | Lexington Battlecruiser | 1 | NULL | Lexington Completed is alternative to BC path |
| 39 | 2031 | 1020 | North Carolina-class | 1 | NULL | Alaska available with fast battleships |
| 40 | 2040 | 1023 | Iowa-class | 1 | NULL | Montana requires Iowa (cancelled design) |

**Example Entries**:

```markdown
| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 1 | 1003 | 1001 | Indiana-class | 1 | NULL | Kearsarge requires Indiana |
| 2 | 1007 | 1001 | Indiana-class | 1 | NULL | Illinois requires Indiana AND Kearsarge |
| 3 | 1007 | 1003 | Kearsarge-class | 1 | NULL | Illinois requires Indiana AND Kearsarge |
| 4 | 1010 | 1007 | Illinois-class | 1 | 1 | Connecticut requires Illinois OR Maine |
| 5 | 1010 | 1008 | Maine-class | 1 | 1 | Connecticut requires Illinois OR Maine |
```

---

<a name="unlocks-table"></a>
## Unlocks Table

**Schema Definition**:

Defines what becomes available after researching a node. Allows multiple unlocks.

| Field | Type | Description |
|-------|------|-------------|
| Unlock_ID | INT | Primary key |
| Node_ID | INT | Foreign key to Research_Nodes (the node being completed) |
| Unlocks_Node_ID | INT | Foreign key to Research_Nodes (what becomes available) |
| Unlocks_Ship_Class | VARCHAR(100) | Ship class name (human-readable) |
| Auto_Unlock | TINYINT | 1 = unlocks immediately, 0 = player must choose |
| Unlock_Priority | INT | Order of unlock display (1=highest priority) |
| Notes | TEXT | Special unlock conditions |

| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 1 | 1000 | 1050 | Arkansas Monitor | 1 | 2 | Texas unlocks Arkansas Monitor (budget alternative) |
| 2 | 1001 | 1003 | Kearsarge-class | 1 | 1 | Indiana unlocks Kearsarge (direct evolution) |
| 3 | 1001 | 1004 | Illinois-class | 1 | 1 | Indiana unlocks Illinois (direct evolution) |
| 4 | 1002 | 1005 | Virginia-class | 1 | 1 | Maine unlocks Virginia (Blue Water branch) |
| 5 | 1004 | 1006 | Connecticut-class | 1 | 1 | Illinois unlocks Connecticut (main line convergence) |
| 6 | 1005 | 1006 | Connecticut-class | 1 | 1 | Virginia unlocks Connecticut (alternative path) |
| 7 | 1006 | 1007 | Mississippi-class | 1 | 1 | Connecticut unlocks Mississippi |
| 8 | 1007 | 1010 | South Carolina-class | 1 | 1 | Mississippi unlocks South Carolina (Dreadnought revolution) |
| 9 | 1010 | 1011 | Delaware-class | 1 | 1 | South Carolina unlocks Delaware |
| 10 | 1011 | 1012 | Wyoming-class | 1 | 1 | Delaware unlocks Wyoming |
| 11 | 1012 | 1014 | New York-class | 1 | 1 | Wyoming unlocks New York (14" gun leap) |
| 12 | 1014 | 1015 | Nevada-class | 1 | 1 | New York unlocks Nevada (Standard-type begins) |
| 13 | 1014 | 1064 | New York (1926 Refit) | 1 | 2 | New York unlocks its own refit |
| 14 | 1015 | 1016 | Pennsylvania-class | 1 | 1 | Nevada unlocks Pennsylvania |
| 15 | 1015 | 1065 | Nevada (1927 Refit) | 1 | 2 | Nevada unlocks its own refit |
| 16 | 1015 | 2000 | Tillman I | 1 | 3 | Nevada unlocks Tillman I (paper ship) |
| 17 | 1015 | 2001 | Tillman II | 1 | 3 | Nevada unlocks Tillman II (paper ship) |
| 18 | 1015 | 2002 | Tillman IV | 1 | 3 | Nevada unlocks Tillman IV (paper ship) |
| 19 | 1015 | 2010 | Lexington Battlecruiser | 1 | 3 | Nevada unlocks Lexington BC (paper ship) |
| 20 | 1015 | 2011 | Tillman III | 1 | 3 | Nevada unlocks Tillman III (paper ship) |
| 21 | 1015 | 2021 | Tillman IV-2 | 1 | 3 | Nevada unlocks Tillman IV-2 18" (paper ship) |
| 22 | 1016 | 1017 | New Mexico-class | 1 | 1 | Pennsylvania unlocks New Mexico |
| 23 | 1016 | 1066 | Pennsylvania (1931 Refit) | 1 | 2 | Pennsylvania unlocks its own refit |
| 24 | 1017 | 1019 | Colorado-class | 1 | 1 | New Mexico unlocks Colorado (16" gun leap) |
| 25 | 1017 | 1067 | New Mexico (1931 Refit) | 1 | 2 | New Mexico unlocks its own refit |
| 26 | 1017 | 1068 | Tennessee (1943 Rebuild) | 1 | 2 | New Mexico unlocks Tennessee rebuild |
| 27 | 1017 | 1069 | California (1944 Rebuild) | 1 | 2 | New Mexico unlocks California rebuild |
| 28 | 1019 | 1020 | North Carolina-class | 1 | 1 | Colorado unlocks North Carolina (Fast BB era) |
| 29 | 1019 | 1070 | Colorado (1941 Refit) | 1 | 2 | Colorado unlocks its own refit |
| 30 | 1019 | 1071 | West Virginia (1944 Rebuild) | 1 | 2 | Colorado unlocks West Virginia rebuild |
| 31 | 1019 | 2020 | South Dakota (1920) | 1 | 3 | Colorado unlocks South Dakota 1920 (paper ship) |
| 32 | 1020 | 1021 | South Dakota (1939)-class | 1 | 1 | North Carolina unlocks South Dakota |
| 33 | 1020 | 1072 | North Carolina (1945 Refit) | 1 | 2 | North Carolina unlocks its own refit |
| 34 | 1020 | 2031 | Alaska-class | 1 | 3 | North Carolina unlocks Alaska (large cruiser) |
| 35 | 1021 | 1023 | Iowa-class | 1 | 1 | South Dakota unlocks Iowa (pinnacle BB) |
| 36 | 1021 | 1073 | South Dakota (1945 Refit) | 1 | 2 | South Dakota unlocks its own refit |
| 37 | 1023 | 1074 | Iowa (1945 Refit) | 1 | 2 | Iowa unlocks 1945 wartime refit |
| 38 | 1023 | 1080 | Iowa (1984 Reactivation) | 1 | 2 | Iowa unlocks 1984 missile reactivation |
| 39 | 1023 | 2040 | Montana-class | 1 | 3 | Iowa unlocks Montana (cancelled super-BB) |
| 40 | 2010 | 2030 | Lexington Completed | 1 | 1 | Lexington BC unlocks completed variant (what-if) |

**Example Entries**:

```markdown
| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 1 | 1001 | 1003 | Kearsarge-class | 1 | 1 | Indiana unlocks Kearsarge |
| 2 | 1001 | 1007 | Illinois-class | 0 | 2 | Indiana partially unlocks Illinois (needs Kearsarge too) |
| 3 | 1003 | 1007 | Illinois-class | 1 | 1 | Kearsarge completes unlock of Illinois |
| 4 | 1002 | 1008 | Maine-class | 1 | 1 | Iowa unlocks Maine |
```

---

<a name="research-branches-table"></a>
## Research Branches Table

**Schema Definition**:

Defines major technology branches (tech tree "lanes" or "paths").

| Field | Type | Description |
|-------|------|-------------|
| Branch_ID | INT | Primary key |
| Country | VARCHAR(50) | Nation |
| Ship_Type | VARCHAR(50) | BB, CV, CA, CL, DD, SS, etc. |
| Branch_Name | VARCHAR(100) | Branch name (e.g., "Coastal Defense", "Blue Water") |
| Branch_Description | TEXT | Philosophy and design approach |
| Branch_Color | VARCHAR(20) | Display color in UI (hex code) |
| Start_Node_ID | INT | Foreign key to first node in branch |
| End_Node_ID | INT | Foreign key to final node in branch (or NULL if ongoing) |
| Branch_Parent | INT | Foreign key to parent branch (if splits from another) |
| Merge_Into_Branch | INT | Foreign key to branch this merges into |
| Era_Start | VARCHAR(50) | Starting era |
| Era_End | VARCHAR(50) | Ending era |
| Notes | TEXT | Branch history and characteristics |

| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 1 | USA | BB | Starting | First US battleship, tutorial introduction | #696969 | 1000 | 1000 | NULL | NULL | Pre-Dreadnought | Pre-Dreadnought | Texas (BB-1) standalone. Free starting ship. Can branch to Arkansas Monitor alternative. |
| 2 | USA | BB | Coastal Defense | Heavy armor, maximum firepower, short-range coastal fortress philosophy | #8B4513 | 1001 | 1004 | NULL | 4 | Pre-Dreadnought | Pre-Dreadnought | Indiana → Kearsarge (experimental) → Illinois. Low freeboard, heavy protection. Merges into Main Line at Connecticut. |
| 3 | USA | BB | Blue Water | Speed, range, ocean-going capability, power projection philosophy | #1E90FF | 1002 | 1005 | NULL | 4 | Pre-Dreadnought | Pre-Dreadnought | Maine → Virginia. Better seakeeping, tactical flexibility. Merges into Main Line at Connecticut. |
| 4 | USA | BB | Main Line | Unified battleship development combining lessons from both pre-dreadnought branches, leading to ultimate super battleship | #FFD700 | 1006 | 2040 | 2, 3 | NULL | Pre-Dreadnought | Fast BB | Connecticut → Mississippi → South Carolina (dreadnought) → ... → Iowa → Montana. Primary progression path from 1905 to 1943, culminating in ultimate super battleship. |
| 5 | USA | BB | Modernization | Refits, rebuilds, and modernizations of existing battleship classes | #9370DB | 1064 | 1080 | 4 | NULL | Dreadnought | Modern | All refit variants from New York 1926 to Iowa 1984. Stems from Main Line ships. Cheaper than building new. |
| 6 | USA | BB | Paper Ship | Unbuilt designs, cancelled projects, theoretical maximum battleships | #DC143C | 2000 | 2040 | 4 | NULL | Treaty Era | Fast BB | Tillman I-IV, South Dakota 1920, Lexington BC, Montana. -10% to -15% reliability penalties. -30% research cost. |
| 7 | USA | BB/CB | Alternative | Alternative design philosophies, experimental concepts, niche roles | #FF8C00 | 1050 | 2031 | 1 | NULL | Pre-Dreadnought | Fast BB | Arkansas Monitor (budget), Alaska-class (large cruiser). Independent development paths. |
| 8 | USA | BB | Experimental | Failed experiments and dead-end designs that influenced later development | #A9A9A9 | 1003 | 1003 | 2 | 4 | Pre-Dreadnought | Pre-Dreadnought | Kearsarge-class superimposed turret experiment. DEAD END but unlocks Illinois. Blast interference issues. |

**Example Entries**:

```markdown
| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 1 | USA | BB | Coastal Defense | Heavy armor, maximum firepower, coastal operations | #8B4513 | 1001 | 1007 | NULL | 3 | Pre-Dreadnought | Pre-Dreadnought | Fortress at sea concept |
| 2 | USA | BB | Blue Water | Speed, range, ocean-going capability | #1E90FF | 1002 | 1008 | NULL | 3 | Pre-Dreadnought | Pre-Dreadnought | Power projection philosophy |
| 3 | USA | BB | Main Line | Unified battleship development post-1900 | #FFD700 | 1007 | NULL | NULL | NULL | Pre-Dreadnought | Modern | Convergence of both branches |
```

---

## Example: USA Battleship Research Tree (1890-1910)

### Research Nodes

```markdown
| Node_ID | Country | Ship_Class | Ship_Type | Tech_Branch | Tech_Tier | Era | Year_Available | Is_Starting_Tech | Research_Cost_RP | Research_Time_Months | Build_Cost_USD | Build_Time_Months | Design_Philosophy | Historical_Context | Gameplay_Role | Special_Ability | Notes |
|---------|---------|------------|-----------|-------------|-----------|-----|----------------|------------------|------------------|---------------------|----------------|-------------------|-------------------|-------------------|---------------|-----------------|-------|
| 1001 | USA | Indiana-class | BB | Coastal Defense | 1 | Pre-Dreadnought | 1890 | 1 | 5000 | 12 | 3020000 | 36 | Heavy armor + firepower | First true US battleships, Naval Act of 1890 | Tank/Fortress | +20% armor, -2 speed | Low freeboard limits seakeeping |
| 1002 | USA | Iowa-class | BB | Blue Water | 1 | Pre-Dreadnought | 1890 | 1 | 8000 | 18 | 3010000 | 30 | Speed + range | Improved seakeeping for ocean ops | Balanced Cruiser | +10% range, +2 speed | Better freeboard design |
| 1003 | USA | Kearsarge-class | BB | Coastal Defense | 2 | Pre-Dreadnought | 1898 | 0 | 10000 | 24 | 3760000 | 36 | Experimental firepower | Superimposed turret experiment | Heavy DPS | +15% firepower, Blast interference penalty | Unique double-turret design |
| 1007 | USA | Illinois-class | BB | Main Line | 3 | Pre-Dreadnought | 1901 | 0 | 12000 | 30 | 4200000 | 36 | Refined orthodox | Lessons learned from both branches | Balanced BB | Balanced stats | Branch convergence point |
| 1008 | USA | Maine-class | BB | Blue Water | 2 | Pre-Dreadnought | 1902 | 0 | 12000 | 30 | 4300000 | 36 | Ocean-going refined | Final pre-dreadnought design | Power Projection | +15% operational range | Last pre-Dreadnought |
| 1010 | USA | Connecticut-class | BB | Main Line | 3 | Pre-Dreadnought | 1905 | 0 | 15000 | 36 | 5000000 | 42 | Ultimate pre-dreadnought | Refined all lessons | Elite Pre-Dread | Great White Fleet participant | Bridge to Dreadnought era |
| 1020 | USA | South Carolina-class | BB | Main Line | 4 | Dreadnought | 1908 | 0 | 25000 | 48 | 6000000 | 48 | All big-gun revolution | First US dreadnought response | Revolution | Superfiring turrets | Makes pre-dreads obsolete |
```

### Prerequisites

```markdown
| Prerequisite_ID | Node_ID | Requires_Node_ID | Requires_Ship_Class | Is_Required | Alternative_Group | Notes |
|-----------------|---------|------------------|---------------------|-------------|-------------------|-------|
| 1 | 1003 | 1001 | Indiana-class | 1 | NULL | Kearsarge requires Indiana |
| 2 | 1007 | 1001 | Indiana-class | 1 | NULL | Illinois requires Indiana AND Kearsarge (both branches) |
| 3 | 1007 | 1003 | Kearsarge-class | 1 | NULL | Illinois requires Indiana AND Kearsarge (both branches) |
| 4 | 1008 | 1002 | Iowa-class | 1 | NULL | Maine requires Iowa |
| 5 | 1010 | 1007 | Illinois-class | 1 | 1 | Connecticut requires Illinois OR Maine |
| 6 | 1010 | 1008 | Maine-class | 1 | 1 | Connecticut requires Illinois OR Maine (alternative) |
| 7 | 1020 | 1010 | Connecticut-class | 1 | NULL | South Carolina requires Connecticut |
```

### Unlocks

```markdown
| Unlock_ID | Node_ID | Unlocks_Node_ID | Unlocks_Ship_Class | Auto_Unlock | Unlock_Priority | Notes |
|-----------|---------|-----------------|-------------------|-------------|-----------------|-------|
| 1 | 1001 | 1003 | Kearsarge-class | 1 | 1 | Indiana unlocks Kearsarge (direct evolution) |
| 2 | 1001 | 1007 | Illinois-class | 0 | 2 | Indiana partially unlocks Illinois (needs Kearsarge too) |
| 3 | 1003 | 1007 | Illinois-class | 1 | 1 | Kearsarge completes Illinois unlock |
| 4 | 1002 | 1008 | Maine-class | 1 | 1 | Iowa unlocks Maine (direct evolution) |
| 5 | 1002 | 1010 | Connecticut-class | 0 | 2 | Iowa partially unlocks Connecticut (Maine also works) |
| 6 | 1007 | 1010 | Connecticut-class | 1 | 1 | Illinois unlocks Connecticut |
| 7 | 1008 | 1010 | Connecticut-class | 1 | 1 | Maine unlocks Connecticut |
| 8 | 1010 | 1020 | South Carolina-class | 1 | 1 | Connecticut unlocks Dreadnought era |
```

### Research Branches

```markdown
| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Branch_Color | Start_Node_ID | End_Node_ID | Branch_Parent | Merge_Into_Branch | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|--------------|---------------|-------------|---------------|-------------------|-----------|---------|-------|
| 1 | USA | BB | Coastal Defense | Heavy armor, maximum firepower, short-range coastal operations. Fortress at sea philosophy. | #8B4513 | 1001 | 1007 | NULL | 3 | Pre-Dreadnought | Pre-Dreadnought | Indiana → Kearsarge → Illinois. Low speed, heavy protection. |
| 2 | USA | BB | Blue Water | Speed, range, ocean-going capability. Power projection philosophy. | #1E90FF | 1002 | 1008 | NULL | 3 | Pre-Dreadnought | Pre-Dreadnought | Iowa → Maine. Better seakeeping, tactical flexibility. |
| 3 | USA | BB | Main Line | Unified battleship development combining lessons from both branches. | #FFD700 | 1007 | NULL | NULL | NULL | Pre-Dreadnought | Modern | Illinois → Connecticut → Dreadnoughts → Fast BBs → Iowa reactivations (1990) |
```

---

## Visual Research Tree Representation

```
USA BATTLESHIP RESEARCH TREE - STRENGTH-BASED PROGRESSION
═══════════════════════════════════════════════════════════════

TIER 1: WEAKEST - PRE-DREADNOUGHTS (Starting Ships)
────────────────────────────────────────────────────────────────
                        [1000] TEXAS (BB-1)
                        FREE Starting Ship
                        2× 12" guns, 12 kts
                                │
                    ┌───────────┴───────────┐
                    │                       │
            [1001] INDIANA           [1002] MAINE
            Coastal Fortress         Blue Water
            4× 13" guns              4× 12" guns
            15 kts, Heavy armor      17 kts, Better range

TIER 2: EARLY PRE-DREAD (Choice Points)
────────────────────────────────────────────────────────────────
                    ┌───────────┴───────────┐
                    │                       │
            [1004] ILLINOIS          [1005] VIRGINIA
            Orthodox design          Mixed armament
            4× 13" guns              4× 12" + 8× 8"
                    │                       │
                    └───────────┬───────────┘
                                │
                        [1006] CONNECTICUT
                        Peak Pre-Dreadnought
                                │
                        [1007] MISSISSIPPI

TIER 3: DREADNOUGHT REVOLUTION
────────────────────────────────────────────────────────────────
                    [1010] SOUTH CAROLINA
                    All Big-Gun Revolution
                    8× 12" guns, superfiring
                                │
                    ┌───────────┴───────────┐
                    │                       │
            [1011] DELAWARE          [1012] WYOMING
            10× 12" guns             12× 12" guns

TIER 4: SUPER-DREADNOUGHT
────────────────────────────────────────────────────────────────
                        [1014] NEW YORK
                        First 14" Guns
                        10× 14"/45 guns

TIER 5: STANDARD-TYPE BBs
────────────────────────────────────────────────────────────────
                    ┌───────────┴───────────┬───────────┐
                    │                       │           │
            [1015] NEVADA        [1016] PENNSYLVANIA  [1017] NEW MEXICO
            All-or-Nothing       12× 14" guns         Turbo-electric
                                                            │
                                        ┌───────────────────┼────────────┐
                                        │                   │            │
                                    Tillman I-IV       Lexington BC   (Paper Ships)

TIER 6: 16" GUN BATTLESHIPS
────────────────────────────────────────────────────────────────
                        [1019] COLORADO
                        First 16" Guns
                        8× 16"/45 guns

TIER 7: FAST BATTLESHIPS
────────────────────────────────────────────────────────────────
                    ┌───────────┴───────────┐
                    │                       │
        [1020] NORTH CAROLINA      [1021] SOUTH DAKOTA (1939)
        9× 16"/45, 28 kts          9× 16"/45, 27.5 kts

TIER 8: ULTIMATE BATTLESHIP
────────────────────────────────────────────────────────────────
                        [1023] IOWA
                        Pinnacle Design
                        9× 16"/50, 33 kts
                                │
                    ┌───────────┴───────────┐
                    │                       │
            [1074] IOWA 1945        [1080] IOWA 1984
            Wartime refit           Missile reactivation
                                          │
                                          │
TIER 9: SUPER BATTLESHIP
────────────────────────────────────────────────────────────────
                        [2040] MONTANA
                        Super Battleship
                        12× 16"/50 guns
                        Ultimate firepower


PROGRESSION NOTES:
════════════════════════════════════════════════════════════════
- Each tier represents significant combat power increase
- Player has choices at each tier where ships are similarly strong
- Modernizations branch off base ships (cheaper, requires original)
- Paper ships available mid-tree for experimental builds
- Montana at Tier 9 as ultimate goal after Iowa
```

---

## Query Examples (Game Logic)

### 1. Check if player can research a node

```sql
-- Can player research Kearsarge-class (Node 1003)?
-- Check: Does player have all required prerequisites?

SELECT p.Node_ID, p.Requires_Ship_Class, p.Is_Required
FROM Prerequisites p
WHERE p.Node_ID = 1003
  AND p.Is_Required = 1
  AND p.Requires_Node_ID NOT IN (
    SELECT researched_node_id FROM player_researched_nodes
  );

-- If result is empty, player has all prerequisites ✅
-- If result has rows, player missing those prerequisites ❌
```

### 2. Get all available research options

```sql
-- What can the player research right now?

SELECT n.*
FROM Research_Nodes n
WHERE n.Node_ID NOT IN (
    SELECT researched_node_id FROM player_researched_nodes
  )
  AND n.Node_ID NOT IN (
    -- Exclude nodes with unmet prerequisites
    SELECT p.Node_ID
    FROM Prerequisites p
    WHERE p.Is_Required = 1
      AND p.Requires_Node_ID NOT IN (
        SELECT researched_node_id FROM player_researched_nodes
      )
  );
```

### 3. Get what a node unlocks

```sql
-- Player just researched Indiana (Node 1001), what unlocks?

SELECT u.Unlocks_Node_ID, u.Unlocks_Ship_Class, n.Research_Cost_RP
FROM Unlocks u
JOIN Research_Nodes n ON u.Unlocks_Node_ID = n.Node_ID
WHERE u.Node_ID = 1001
  AND u.Auto_Unlock = 1;

-- Returns: Kearsarge-class (Node 1003)
```

### 4. Get branch progression

```sql
-- Show player's progress in Coastal Defense branch

SELECT n.Ship_Class, n.Tech_Tier, n.Research_Cost_RP,
       CASE
         WHEN pr.researched_node_id IS NOT NULL THEN 'Researched'
         ELSE 'Locked'
       END AS Status
FROM Research_Nodes n
LEFT JOIN player_researched_nodes pr ON n.Node_ID = pr.researched_node_id
WHERE n.Country = 'USA'
  AND n.Ship_Type = 'BB'
  AND n.Tech_Branch = 'Coastal Defense'
ORDER BY n.Tech_Tier;
```

---

## Integration with Ships Database

### Linking the Two Databases

**Research Tree Database** references ship classes by name:
- `Ship_Class` field in Research_Nodes table

**Ships Database** has matching class names:
- `Ship_Class` field in Ships table

**Join Example**:

```sql
-- Get full ship stats for all researched nodes

SELECT
  rn.Node_ID,
  rn.Ship_Class,
  rn.Research_Cost_RP,
  s.Displacement_Standard_TONS,
  s.Max_Speed_KTS,
  s.Main_Armament
FROM Research_Nodes rn
JOIN Ships s ON rn.Ship_Class = s.Ship_Class
WHERE rn.Node_ID IN (SELECT researched_node_id FROM player_researched_nodes);
```

---

## Game Mechanics Integration

### Research Points (RP) System

**RP Generation**:
- Base income: 500 RP/month
- Naval base bonus: +100 RP/month per major base
- Battle victory: +500-2,000 RP
- Research building: +200 RP/month

**RP Costs (Strength-Based Tier Scale)**:
- Tier 1 (Weakest - Starting Pre-dreads): 0-5,000 RP
- Tier 2 (Early Pre-dreads): 2,000-12,000 RP
- Tier 3 (Dreadnought Revolution): 15,000-25,000 RP
- Tier 4 (Super-Dreadnought): 7,000-20,000 RP
- Tier 5 (Standard-Type 14"): 6,000-22,000 RP
- Tier 6 (16" Gun BBs): 8,000-25,000 RP
- Tier 7 (Fast Battleships): 10,000-35,000 RP
- Tier 8 (Ultimate Iowa): 12,000-75,000 RP
- Tier 9 (Super Battleship Montana): 60,000 RP

**Tier Strength Definitions**:
- Tier 1: 6,000-10,000 tons, 12"-13" guns, 12-17 kts
- Tier 2: 11,000-16,000 tons, 12"-13" guns, improved designs
- Tier 3: 16,000-27,000 tons, all 12" big-gun dreadnoughts
- Tier 4: 27,000 tons, first 14" guns (major caliber jump)
- Tier 5: 28,000-32,000 tons, 14" guns, all-or-nothing armor
- Tier 6: 32,000 tons, first 16" guns (major caliber jump)
- Tier 7: 35,000-38,000 tons, 16" guns, 27-28 kts (fast BBs)
- Tier 8: 45,000-57,000 tons, 16"/50 guns, 33 kts (ultimate)
- Tier 9: 60,000+ tons, 12× 16"/50 guns (super battleship)

### Research Time

**Time Scale**:
- Fast research: 6-12 months
- Normal research: 12-24 months
- Slow research: 24-48 months
- Revolutionary: 48-72 months

**Time Reduction Bonuses**:
- Research lab: -20% time
- Captured enemy blueprints: -30% time
- Allied tech sharing: -15% time

---

## Database Status

**Current Status**: USA Battleships COMPLETE ✅
**Target Count**: 100-200 research nodes per nation
**Priority**: USA battleships 1890-1990 ✅ COMPLETED

**Coverage Plan**:
- ✅ **USA Battleships: 47 nodes (1890-1990) - COMPLETE - STRENGTH-BASED PROGRESSION**
  - 9 Tiers (Tier 1 weakest → Tier 9 strongest)
  - 18 base classes (Texas through Iowa)
  - 12 modernization/refit variants
  - 9 paper ships (Tillman, Montana, South Dakota 1920, Lexington BC)
  - 8 experimental/alternative designs
  - 8 research branches defined
  - 40 prerequisite relationships
  - 40 unlock relationships
  - **Montana at Tier 9 as ultimate super battleship goal**
- ⏳ USA Carriers: 20-30 nodes (1920-1990) - PENDING
- ⏳ USA Cruisers: 20-25 nodes (1890-1990) - PENDING
- ⏳ USA Destroyers: 25-30 nodes (1902-1990) - PENDING
- ⏳ USA Submarines: 20-25 nodes (1900-1990) - PENDING

**Repeat for**: British, German, Japanese

---

## Future Enhancements

### Possible Additional Tables

1. **Research_Modifiers** - Temporary bonuses (espionage, treaties)
2. **Research_Events** - Historical events affecting research (Pearl Harbor, etc.)
3. **Research_Branches_Rivalry** - Competing design philosophies
4. **Player_Research_Progress** - Save game data

### Advanced Features

1. **Parallel Research**: Research multiple nodes simultaneously
2. **Research Sharing**: Allied nations share tech
3. **Espionage**: Steal enemy research progress
4. **Prototype Systems**: Test ships before full research
5. **Design Bureaus**: Different designers affect stats

---

**Last Updated**: October 10, 2025
**Status**: ✅ USA BATTLESHIP RESEARCH TREE COMPLETE

**Integration**: Works alongside Ships Database via Ship_Class field

**Statistics**:
- 47 Research Nodes (1890-1990 coverage)
- 40 Prerequisites (complex unlock logic with AND/OR support)
- 40 Unlocks (automatic unlock chains)
- 8 Research Branches (Starting, Coastal Defense, Blue Water, Main Line, Modernization, Paper Ship, Alternative, Experimental)
- Total: 135 database entries
