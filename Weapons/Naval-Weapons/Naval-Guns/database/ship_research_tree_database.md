# Ship Research Tree Database

**Export Date**: October 10, 2025
**Database Version**: 2.0 - NavyField Expansion
**Total Records**: ~675 (204 Research Nodes + ~220 Prerequisites + ~220 Unlocks + 31 Research Branches)

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

**Total Entries**: 204 nodes (USA Complete - NavyField Style)
**ID Allocation**:
- USA Battleships: 1000-1999 (47 nodes: 1000-1023, 1050, 1064-1074, 1080, 2000-2040)
- USA Carriers: 5000-5099 (32 nodes: 5000-5031)
- USA Cruisers: 6000-6099 (45 nodes: 6000-6044)
- USA Destroyers: 7000-7099 (42 nodes: 7000-7041)
- USA Submarines: 8000-8099 (38 nodes: 8000-8037)
- British: 2000-2999 (reserved)
- German: 3000-3999 (reserved)
- Japanese: 4000-4999 (reserved)

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
| 5000 | USA | Langley-class | CV | Starting | 1 | Experimental | 1922 | 1 | 0 | 0 | 2000000 | 18 | Experimental carrier | First US carrier, converted collier | Tutorial Carrier | Proves Concept: -30% effectiveness, FREE | FREE starting carrier, slow 15 kts |
| 5001 | USA | Lexington-class | CV | Main Line | 2 | Battlecruiser Conversion | 1927 | 0 | 8000 | 18 | 45000000 | 72 | Fast large carrier | BC converted to CV, 33 kts | Fast Fleet Carrier | +33 kts speed, 8" guns (unique) | Massive, fast, powerful |
| 5002 | USA | Ranger-class | CV | Main Line | 3 | Treaty Carrier | 1934 | 0 | 10000 | 24 | 15500000 | 36 | Treaty-limited | First purpose-built, too small | Budget Carrier | -2 kts speed, weak protection | Cheap but flawed design |
| 5003 | USA | Yorktown-class | CV | Main Line | 4 | Perfect Fleet Carrier | 1937 | 0 | 15000 | 30 | 20000000 | 36 | Perfect fleet carrier | Balance of speed, protection, aircraft | Balanced CV | 32.5 kts, well-protected | Ideal pre-war design |
| 5004 | USA | Essex-class | CV | Main Line | 5 | WWII Workhorse | 1942 | 0 | 18000 | 36 | 68000000 | 20 | Mass production | Largest class ever, 24 ships | Mass Production | +40% AA effectiveness | Rapid 20-month construction |
| 5005 | USA | Essex-class (1947 Refit) | CV | Modernization | 5 | Post-War | 1947 | 0 | 6000 | 6 | 0 | 0 | Interim upgrade | Improved AA and radar, not jet-capable | Upgraded WWII CV | +70% 40mm AA, improved radar | Cheap quick refit vs SCB-27 |
| 5006 | USA | Essex-class (SCB-27A) | CV | Modernization | 6 | Jet Age | 1951 | 0 | 15000 | 18 | 0 | 0 | Jet modernization | Angled deck, steam cats, jet-capable | Jet Carrier | Steam cats, angled deck, jets | $40M, 24 months refit |
| 5007 | USA | Midway-class | CV | Main Line | 6 | Armored Carrier | 1945 | 0 | 25000 | 42 | 90000000 | 24 | Armored carrier | British-influenced, 3.5" flight deck armor | Tank Carrier | +3.5" armor, 47-year service | Longest-serving (1945-1992) |
| 5008 | USA | Forrestal-class | CV | Main Line | 7 | Supercarrier | 1955 | 0 | 35000 | 54 | 217000000 | 36 | First supercarrier | Purpose-built with angled deck | First Supercarrier | 4 catapults, 60,000 tons | Revolutionary design |
| 5009 | USA | Kitty Hawk-class | CV | Main Line | 7 | Improved Supercarrier | 1961 | 0 | 30000 | 48 | 264000000 | 42 | Improved Forrestal | Better elevator layout, last oil-fired | Final Conventional CV | 4 deck-edge elevators | Served 48 years (1961-2009) |
| 5010 | USA | Enterprise-class | CVN | Main Line | 8 | First Nuclear | 1961 | 0 | 50000 | 66 | 451000000 | 54 | First nuclear carrier | 8 reactors, unlimited range | Nuclear Revolution | UNLIMITED range, 8× A2W reactors | 51-year service (1961-2012) |
| 5011 | USA | Gerald R. Ford-class | CVN | Main Line | 10 | Ultimate Carrier | 2017 | 0 | 70000 | 96 | 1300000000 | 96 | Ultimate carrier | EMALS, AAWS, most advanced carrier | Ultimate CV | EMALS cats, 75+ aircraft, AAWS | Most advanced carrier ever |
| 5012 | USA | Bogue-class | CVE | Escort | 1 | WWII | 1942 | 1 | 0 | 0 | 8000000 | 12 | Budget escort carrier | Merchant conversion for ASW/convoy escort | Budget Carrier | ASW Focus: +50% sub detection, FREE | FREE starting CVE, 45 built |
| 5013 | USA | Saratoga CV-3 | CV | Main Line | 2 | Interwar | 1927 | 0 | 8000 | 18 | 45000000 | 72 | Sister to Lexington | Sister ship CV-3, identical specs | Fast Fleet Carrier | +33 kts speed, 8" guns (unique) | Sister to CV-2, alternative |
| 5014 | USA | Long Island-class | CVE | Escort | 2 | WWII | 1941 | 0 | 3000 | 12 | 4000000 | 12 | First escort carrier | First US escort carrier AVG-1 | Training/ASW CVE | +30% pilot training | AVG-1/CVE-1, training role |
| 5015 | USA | Wasp-class | CV | Main Line | 3 | Interwar | 1940 | 0 | 10000 | 24 | 20000000 | 36 | Improved Ranger | Better armor than Ranger | Improved Treaty CV | +20% armor vs Ranger | CV-7, sunk Guadalcanal 1942 |
| 5016 | USA | Sangamon-class | CVE | Escort | 3 | WWII | 1942 | 0 | 4000 | 12 | 12000000 | 12 | Oiler conversion CVE | Fast tanker conversions | Fast CVE | 18 kts vs 16 kts standard CVE | 4 ships, best CVE conversions |
| 5017 | USA | Enterprise CV-6 | CV | Alternative | 4 | WWII | 1938 | 0 | 16000 | 30 | 20000000 | 36 | Most decorated ship | 20 battle stars, most decorated US ship | Legend | Lucky E: +15% evasion | UNIQUE, most decorated WWII ship |
| 5018 | USA | Casablanca-class | CVE | Escort | 4 | WWII | 1943 | 0 | 5000 | 18 | 5000000 | 6 | Mass production CVE | 50 built by Kaiser shipyards | Mass CVE | Rapid build: 6 months | Largest CV class ever, 50 ships |
| 5019 | USA | Independence-class | CVL | Light Carrier | 4 | WWII | 1943 | 0 | 6000 | 18 | 15000000 | 12 | Cleveland conversion | 9 light carriers from CL hulls | Fast Light CV | 31.5 kts, rapid build 12 months | 9 ships, Cleveland CL hulls |
| 5020 | USA | Commencement Bay-class | CVE | Escort | 5 | WWII | 1944 | 0 | 6000 | 18 | 10000000 | 12 | Ultimate CVE | Purpose-built, best escort carriers | Ultimate CVE | 19 kts, 34 aircraft | 19 built, served Korean War |
| 5021 | USA | Saipan-class | CVL | Light Carrier | 5 | Post-War | 1946 | 0 | 8000 | 24 | 30000000 | 18 | Purpose-built CVL | First purpose-built light carrier | Purpose CVL | 33 kts, 48 aircraft | 2 ships, cruiser hulls |
| 5022 | USA | Intrepid CV-11 | CV | Alternative | 5 | WWII | 1943 | 0 | 20000 | 36 | 68000000 | 20 | Famous Essex variant | Kamikaze survivor, museum ship NYC | Tough Essex | Damage Control: +25% survival | UNIQUE, survived 5 kamikazes |
| 5023 | USA | Essex-class (SCB-27C/125) | CV | Modernization | 6 | Jet Age | 1955 | 0 | 18000 | 24 | 0 | 0 | Full jet modernization | C-11 steam cats + full upgrades | Full Jet CV | C-11 cats, full modernization | $50M, 30 months refit |
| 5024 | USA | Midway-class (SCB-110) | CV | Main Line | 6 | Jet Age | 1957 | 0 | 12000 | 18 | 0 | 0 | Angled deck Midway | Angled deck + steam catapults | Modernized Tank CV | Armored + jet capable | Major 12-year refit |
| 5025 | USA | Thetis Bay CVHA-1 | CVH | Alternative | 6 | Cold War | 1956 | 0 | 3000 | 6 | 5000000 | 6 | Helicopter carrier | First US helicopter assault carrier | Helo CVE | 20 helicopters, USMC assault | Experiment, led to LPH/LHA |
| 5026 | USA | Saratoga CV-60 | CV | Main Line | 7 | Supercarrier | 1956 | 0 | 35000 | 54 | 220000000 | 36 | Improved Forrestal | Improved electronics over CV-59 | Improved Supercarrier | Upgraded radar and systems | Forrestal class, ship 4 |
| 5027 | USA | John F. Kennedy CV-67 | CV | Main Line | 7 | Supercarrier | 1968 | 0 | 32000 | 48 | 277000000 | 42 | Modified Kitty Hawk | Smokestacks repositioned aft | Unique CV | Last oil-fired CV, unique design | Modified Kitty Hawk, UNIQUE |
| 5028 | USA | Nimitz-class (Early) CVN-68/69 | CVN | Main Line | 8 | Nuclear | 1975 | 0 | 60000 | 84 | 1000000000 | 72 | Early production Nimitz | First production nuclear carriers | Early Nuclear CV | 2× A4W reactors, 90+ aircraft | CVN-68/69, early production |
| 5029 | USA | Nimitz-class (Improved) CVN-70-72 | CVN | Main Line | 8 | Nuclear | 1981 | 0 | 55000 | 78 | 1100000000 | 72 | Improved systems | Better electronics and radar | Improved Nuclear CV | Upgraded systems and sensors | CVN-70/71/72, improved variant |
| 5030 | USA | Nimitz-class (Late) CVN-73-76 | CVN | Main Line | 9 | Nuclear | 1995 | 0 | 50000 | 72 | 1200000000 | 72 | Late production Nimitz | Full upgrades, best Nimitz variant | Ultimate Nimitz | All systems maximized | CVN-73/74/75/76, ultimate |
| 5031 | USA | Enterprise CVN-80 | CVN | Main Line | 9 | Future | 2027 | 0 | 55000 | 78 | 1400000000 | 84 | Ford derivative | Third Enterprise, Ford technology | Future Ford | Ford systems, proven design | Planned 2027, Ford class |
| 6000 | USA | Chester-class | CL | Starting | 1 | Protected Cruiser | 1908 | 1 | 0 | 0 | 1500000 | 24 | Early protected cruiser | First US scout cruiser | Scout Cruiser | Very Light: -50% armor, +3 kts, FREE | FREE starting cruiser, 3 ships |
| 6001 | USA | Omaha-class | CL | Starting | 1 | Scout Cruiser | 1923 | 1 | 0 | 0 | 7000000 | 36 | Scout cruiser | WWI-era design, 12×6" guns | Fast Scout | 35 kts, 12×6" guns, FREE | FREE starting option, 10 ships |
| 6002 | USA | Pensacola-class | CA | Heavy Main Line | 2 | Treaty Heavy | 1930 | 0 | 8000 | 24 | 12000000 | 48 | First treaty heavy | First 8" treaty cruiser | Early Heavy CA | 10×8" guns, lightly armored | 2 ships, CA-24/25 |
| 6003 | USA | Northampton-class | CA | Heavy Main Line | 2 | Treaty Heavy | 1930 | 0 | 8000 | 24 | 11000000 | 48 | Alternative heavy | 9×8" guns, lighter armor | Fast Heavy CA | 32.5 kts, 9×8" guns | 6 ships, alternative |
| 6004 | USA | Brooklyn-class | CL | Light Main Line | 2 | Treaty Light | 1937 | 0 | 6000 | 24 | 14000000 | 48 | Maximum 6" firepower | 15×6" guns, treaty light cruiser | Light CL | 15×6" guns, highest ROF | 7 ships, firepower focus |
| 6005 | USA | Portland-class | CA | Heavy Main Line | 3 | Treaty Heavy | 1933 | 0 | 10000 | 30 | 13000000 | 54 | Refined heavy | Improved armor over Northampton | Balanced Heavy CA | 9×8" guns, better armor | 2 ships, balanced design |
| 6006 | USA | Atlanta-class | CLAA | AA Specialist | 3 | AA Cruiser | 1941 | 0 | 7000 | 18 | 17000000 | 42 | AA specialist | 16×5" DP guns, AA focus | AA Cruiser | 16×5" DP, +100% AA effectiveness | 11 ships, AA specialist |
| 6007 | USA | St. Louis-class | CL | Light Main Line | 3 | Treaty Light | 1939 | 0 | 6500 | 24 | 15000000 | 48 | Brooklyn subclass | Improved AA over Brooklyn | AA-Enhanced CL | 15×6" + improved AA | 2 ships, Brooklyn variant |
| 6008 | USA | New Orleans-class | CA | Heavy Main Line | 4 | Treaty Heavy | 1934 | 0 | 12000 | 36 | 15000000 | 60 | Refined treaty design | Best treaty-compliant heavy | Peak Treaty CA | 9×8" guns, all-or-nothing armor | 7 ships, treaty pinnacle |
| 6009 | USA | Wichita-class | CA | Heavy Main Line | 4 | Pre-War | 1939 | 0 | 13000 | 36 | 17000000 | 60 | Bridge to WWII | Brooklyn hull + 9×8" guns | Hybrid CA | Brooklyn + 8" guns | 1 ship, unique hybrid |
| 6010 | USA | Cleveland-class | CL | Light Main Line | 4 | WWII Light | 1942 | 0 | 10000 | 30 | 28000000 | 36 | Mass production CL | 27 ships, WWII mass production | Mass CL | 12×6" guns, 27 ships built | Largest CL class |
| 6011 | USA | Oakland-class | CLAA | AA Specialist | 4 | AA Cruiser | 1943 | 0 | 8000 | 24 | 21000000 | 42 | Improved AA | 12×5" DP, improved Atlanta | AA Platform | 12×5" DP, radar | 4 ships, improved AA |
| 6012 | USA | Baltimore-class | CA | Heavy Main Line | 5 | WWII Heavy | 1943 | 0 | 18000 | 42 | 37000000 | 60 | Peak WWII heavy | Best WWII heavy cruiser | Ultimate Gun CA | 9×8", best armor | 14 ships, WWII peak |
| 6013 | USA | Oregon City-class | CA | Heavy Main Line | 5 | WWII Heavy | 1946 | 0 | 16000 | 36 | 40000000 | 60 | Improved Baltimore | Single funnel, improved design | Refined CA | 9×8", single funnel | 4 ships, Baltimore derivative |
| 6014 | USA | Fargo-class | CL | Light Main Line | 5 | Post-War Light | 1945 | 0 | 11000 | 30 | 32000000 | 36 | Improved Cleveland | Single funnel Cleveland | Improved CL | 12×6", single funnel | 2 ships, Cleveland improved |
| 6015 | USA | Juneau-class | CLAA | AA Specialist | 5 | AA Cruiser | 1946 | 0 | 9000 | 24 | 24000000 | 42 | Late-war AA | 12×5" DP, late-war | Late AA Cruiser | 12×5" DP, improved systems | 3 ships, Korean War |
| 6016 | USA | Des Moines-class | CA | Heavy Main Line | 6 | Ultimate Gun | 1948 | 0 | 25000 | 54 | 47000000 | 66 | Ultimate gun cruiser | 9×8" auto-loading, 8-10 rpm | Ultimate Gun CA | Auto-loading 8-10 rpm per gun | 3 ships, pinnacle gun CA |
| 6017 | USA | Worcester-class | CL | Light Main Line | 6 | Ultimate Light | 1948 | 0 | 22000 | 48 | 45000000 | 66 | Ultimate light gun | 12×6" rapid-fire auto | Ultimate CL | 6" rapid-fire, 12 rpm | 2 ships, ultimate light |
| 6018 | USA | Boston-class | CAG | Conversion | 6 | First Missile | 1955 | 0 | 10000 | 18 | 0 | 0 | First missile CA | Baltimore + Terrier SAM | First Missile CA | 6×8" + Terrier SAM | 3 conversions, first missiles |
| 6019 | USA | Galveston-class | CLG | Conversion | 6 | Missile Light | 1958 | 0 | 9000 | 18 | 0 | 0 | Missile CL conversion | Cleveland + Talos SAM | Missile CL | 6×6" + Talos SAM | 3 conversions, CL missile |
| 6020 | USA | Providence-class | CLG | Conversion | 6 | Missile Light | 1959 | 0 | 9000 | 18 | 0 | 0 | Improved missile CL | Cleveland + Terrier SAM | Terrier CL | 3×6" + Terrier SAM | 3 conversions, Terrier |
| 6021 | USA | Norfolk-class | DL | Alternative | 6 | Frigate/Light | 1953 | 0 | 12000 | 30 | 32000000 | 36 | Destroyer leader | Large DD/light cruiser hybrid | DL Hybrid | 8×3", ASW + AA | 1 ship, frigate |
| 6022 | USA | Albany-class | CG | Conversion | 7 | Heavy Missile | 1962 | 0 | 15000 | 24 | 0 | 0 | Extensive conversion | Baltimore, 0 guns, Talos+Tartar | All-Missile CG | 104 Talos + 84 Tartar | 3 conversions, all-missile |
| 6023 | USA | Long Beach CGN-9 | CGN | Nuclear Main Line | 7 | First Nuclear | 1961 | 0 | 28000 | 48 | 350000000 | 60 | First nuclear cruiser | Only nuclear CGN, 2×C1W reactors | Nuclear Cruiser | Nuclear, unlimited range, UNIQUE | 1 ship, first nuclear CG |
| 6024 | USA | Leahy-class | CG | Guided Missile | 7 | First Purpose CG | 1962 | 0 | 18000 | 36 | 85000000 | 48 | First purpose-built | 9 ships, first purpose CG | Purpose CG | Terrier SAM, 9 ships | First purpose-built CG |
| 6025 | USA | Bainbridge CGN-25 | CGN | Nuclear Branch | 7 | Nuclear Leahy | 1962 | 0 | 25000 | 42 | 165000000 | 54 | Nuclear Leahy | Nuclear-powered Leahy variant | Nuclear CG | 2× D2G reactors, UNIQUE | 1 ship, nuclear variant |
| 6026 | USA | Belknap-class | CG | Guided Missile | 7 | Improved CG | 1964 | 0 | 19000 | 36 | 95000000 | 48 | Improved missile CG | 1×5" + Terrier SAM | Improved CG | Single 5" gun retained | 9 ships, improved design |
| 6027 | USA | Truxtun CGN-35 | CGN | Nuclear Branch | 7 | Nuclear Belknap | 1967 | 0 | 26000 | 42 | 190000000 | 54 | Nuclear Belknap | Nuclear Belknap variant | Nuclear CG | 2× D2G reactors, UNIQUE | 1 ship, nuclear variant |
| 6028 | USA | Chicago CAG-136 | CAG | Conversion | 7 | Late Conversion | 1964 | 0 | 11000 | 18 | 0 | 0 | Late missile conversion | Baltimore + Talos, late convert | Late CAG | 6×8" + Talos SAM | 1 conversion, late upgrade |
| 6029 | USA | California-class | CGN | Nuclear Main Line | 8 | Nuclear Production | 1974 | 0 | 35000 | 54 | 400000000 | 66 | Nuclear production | 2 ships, nuclear CG | Nuclear Production CG | 2× D2G reactors, Standard SM-2 | 2 ships, nuclear |
| 6030 | USA | Virginia-class | CGN | Nuclear Main Line | 8 | Improved Nuclear | 1976 | 0 | 38000 | 60 | 450000000 | 72 | Improved nuclear | 4 ships, improved CGN | Improved Nuclear CG | 2× D2G reactors, Aegis-ready | 4 ships, nuclear |
| 6031 | USA | Leahy-class (NTU) | CG | Modernization | 8 | Upgraded Missile | 1980 | 0 | 8000 | 12 | 0 | 0 | New Threat Upgrade | Standard SM-2, NTU upgrade | Modernized CG | Standard SM-2 missiles | Modernization refit |
| 6032 | USA | Belknap-class (NTU) | CG | Modernization | 8 | Upgraded Missile | 1985 | 0 | 8500 | 12 | 0 | 0 | New Threat Upgrade | Standard SM-2, NTU upgrade | Modernized CG | 1×5" + Standard SM-2 | Modernization refit |
| 6033 | USA | Ticonderoga-class (Early) CG-47/48 | CG | Aegis Main Line | 8 | Early Aegis | 1983 | 0 | 45000 | 66 | 800000000 | 78 | Early Aegis | Mk 26 launchers, SPY-1A radar | Early Aegis CG | Aegis + Mk 26 twin launchers | CG-47/48, Mk 26 |
| 6034 | USA | Ticonderoga-class (Baseline 1) CG-49-51 | CG | Aegis Main Line | 9 | Aegis Baseline 1 | 1985 | 0 | 43000 | 60 | 850000000 | 78 | Improved early Aegis | Better systems, still Mk 26 | Aegis B1 CG | Improved Aegis, Mk 26 | CG-49/50/51 |
| 6035 | USA | Ticonderoga-class (Baseline 2) CG-52-58 | CG | Aegis Main Line | 9 | Aegis Baseline 2 | 1986 | 0 | 41000 | 54 | 900000000 | 78 | Advanced radar | SPY-1B radar, Mk 26 | Aegis B2 CG | SPY-1B radar upgrade | CG-52-58 |
| 6036 | USA | Virginia-class CGN (Modernized) | CGN | Nuclear Modernization | 9 | Modernized Nuclear | 1988 | 0 | 25000 | 24 | 0 | 0 | Full modernization | Aegis-ready systems, full upgrade | Modernized Nuclear CG | Aegis-ready, Tomahawk | Late 1980s refit |
| 6037 | USA | Strike Cruiser CGN | CGN | Paper Ship | 9 | Strike Cruiser | 1975 | 0 | 50000 | 72 | 900000000 | 84 | Cancelled design | Aegis + Tomahawk + nuclear | Paper Strike CGN | Aegis nuclear, -10% reliability | Cancelled 1976, paper |
| 6038 | USA | Ticonderoga-class (Baseline 3) CG-59-64 | CG | Aegis Main Line | 10 | Aegis VLS Early | 1988 | 0 | 40000 | 48 | 950000000 | 78 | First VLS | Mk 41 VLS, 122 cells | Aegis VLS CG | First Mk 41 VLS 122 cells | CG-59-64, first VLS |
| 6039 | USA | Ticonderoga-class (Baseline 4) CG-65-73 | CG | Aegis Main Line | 10 | Ultimate Aegis | 1990 | 0 | 38000 | 42 | 1000000000 | 78 | Ultimate production | Best Aegis CG, ultimate production | Ultimate Aegis CG | Ultimate systems, VLS 122 | CG-65-73, ultimate |
| 6040 | USA | CG(X) Future Cruiser | CG | Paper Ship | 10 | Future Cruiser | 2020 | 0 | 60000 | 84 | 3000000000 | 96 | Next-gen cruiser | 2020s tech, cancelled | Paper Future CG | Next-gen systems, -10% reliability | Cancelled, paper design |
| 7000 | USA | Bainbridge-class | DD | Starting | 1 | Torpedo Boat Destroyer | 1902 | 1 | 0 | 0 | 500000 | 18 | First US destroyer | 420 tons, 2×3" guns | Tutorial DD | Very Light: -60% armor, +2 kts, FREE | FREE starting DD, 5 ships |
| 7001 | USA | Smith-class | DD | Starting | 1 | Early Destroyer | 1909 | 1 | 0 | 0 | 800000 | 24 | Better starting DD | 700 tons, 5×3" guns | Scout DD | Light Fast: +3 kts, FREE | FREE starting option, 5 ships |
| 7002 | USA | Paulding-class | DD | Main Line | 2 | Pre-WWI | 1910 | 0 | 3000 | 12 | 950000 | 24 | Early fleet DD | 742 tons, 5×3" guns | Early Fleet DD | Torpedoes + guns | 21 ships |
| 7003 | USA | Cassin-class | DD | Main Line | 2 | Pre-WWI | 1913 | 0 | 3500 | 12 | 1100000 | 30 | Improved destroyer | 1,010 tons, oil-fired | Oil-Fired DD | Oil fuel, improved range | 8 ships |
| 7004 | USA | Sampson-class | DD | Main Line | 2 | Pre-WWI | 1916 | 0 | 4000 | 18 | 1300000 | 30 | Final pre-WWI | 1,200 tons, 4×4" guns | Pre-WWI Peak DD | 1,200 tons, 29 kts | 6 ships |
| 7005 | USA | Caldwell-class | DD | Four-Stacker | 3 | WWI | 1917 | 0 | 5000 | 18 | 1500000 | 12 | First flush-deck | Flush deck design | WWI DD | Flush deck, 6×4" guns | 6 ships, first flush-deck |
| 7006 | USA | Wickes-class | DD | Four-Stacker | 3 | WWI | 1918 | 0 | 5500 | 18 | 1600000 | 9 | Mass production WWI | 111 ships, four-stacker | Mass DD | 4 stacks, 111 ships | Largest DD class WWI |
| 7007 | USA | Clemson-class | DD | Four-Stacker | 3 | WWI | 1919 | 0 | 6000 | 18 | 1700000 | 9 | Improved Wickes | 156 ships, more fuel | Mass WWI DD | 4 stacks, 156 ships | Largest US DD class |
| 7008 | USA | Wickes-class (APD) | APD | Alternative | 3 | WWII Conversion | 1943 | 0 | 2000 | 6 | 0 | 0 | High-speed transport | Fast troop transport conversion | Fast Transport | High-speed, 200 troops | WWII conversion |
| 7009 | USA | Farragut-class | DD | Interwar | 4 | Interwar | 1934 | 0 | 8000 | 24 | 3800000 | 36 | First enclosed guns | 1,400 tons, enclosed guns | Interwar DD | Enclosed 5" guns | 8 ships |
| 7010 | USA | Porter-class | DD | Leader | 4 | Destroyer Leader | 1935 | 0 | 10000 | 30 | 5500000 | 42 | Destroyer leader | 1,850 tons, 8×5" guns | Leader DD | 8×5" guns, leader | 8 ships, large DD |
| 7011 | USA | Mahan-class | DD | Interwar | 4 | Interwar | 1936 | 0 | 8500 | 24 | 4000000 | 36 | More torpedoes | 12 torpedoes, 1,500 tons | Torpedo DD | 12 torpedoes | 18 ships |
| 7012 | USA | Gridley-class | DD | Interwar | 4 | Interwar | 1937 | 0 | 9000 | 24 | 4200000 | 36 | Maximum torpedoes | 16 torpedoes, experimental | Torpedo Focus DD | 16 torpedoes maximum | 4 ships, experimental |
| 7013 | USA | Bagley-class | DD | Interwar | 4 | Interwar | 1937 | 0 | 8800 | 24 | 4100000 | 36 | Balanced design | Balanced torpedoes + guns | Balanced DD | 16 torpedoes, balanced | 8 ships |
| 7014 | USA | Benham-class | DD | Pre-WWII | 5 | Pre-War | 1939 | 0 | 10000 | 30 | 4500000 | 42 | Refined pre-war | 1,850 tons, refined | Pre-War DD | Refined design | 10 ships |
| 7015 | USA | Sims-class | DD | Pre-WWII | 5 | Pre-War | 1939 | 0 | 9500 | 30 | 4300000 | 42 | Alternative pre-war | 1,570 tons, lighter | Light Pre-War DD | Lighter, faster | 12 ships |
| 7016 | USA | Benson-class | DD | Pre-WWII | 5 | Pre-War | 1940 | 0 | 11000 | 30 | 5000000 | 42 | Standard pre-war | 1,630 tons, standard | Standard DD | 5×5" guns | 30 ships |
| 7017 | USA | Gleaves-class | DD | Pre-WWII | 5 | Pre-War | 1940 | 0 | 11000 | 30 | 5100000 | 42 | Benson variant | Benson derivative | Standard Variant DD | Similar to Benson | 66 ships, Benson variant |
| 7018 | USA | Bristol-class | DD | Pre-WWII | 5 | Pre-War | 1941 | 0 | 11500 | 30 | 5200000 | 42 | Benson subclass | Final pre-war variant | Final Pre-War DD | Last pre-war design | 32 ships |
| 7019 | USA | Fletcher-class | DD | WWII Main Line | 6 | WWII Workhorse | 1942 | 0 | 15000 | 36 | 6000000 | 12 | Signature WWII DD | 2,100 tons, 175 ships | Ultimate WWII DD | 5×5" guns, 175 ships | Most successful DD class |
| 7020 | USA | Fletcher-class (FRAM I) | DD | Modernization | 6 | FRAM Upgrade | 1960 | 0 | 5000 | 12 | 0 | 0 | FRAM modernization | ASW + electronics upgrade | Modernized DD | FRAM ASW upgrade | 1960s modernization |
| 7021 | USA | Allen M. Sumner-class | DD | WWII Main Line | 6 | WWII Heavy | 1944 | 0 | 16000 | 36 | 7500000 | 15 | Six-gun DD | 2,200 tons, 6×5" guns | Heavy WWII DD | 6×5" guns in 3 twins | 67 ships |
| 7022 | USA | Gearing-class | DD | WWII Main Line | 6 | Ultimate WWII | 1945 | 0 | 17000 | 36 | 8000000 | 18 | Lengthened Sumner | 2,425 tons, 6×5" guns | Ultimate Gun DD | Lengthened, more fuel | 98 ships |
| 7023 | USA | Gearing-class (FRAM I) | DD | Modernization | 6 | FRAM Upgrade | 1961 | 0 | 6000 | 12 | 0 | 0 | Full FRAM | Full ASW modernization | Modernized Heavy DD | Full FRAM upgrade | Major modernization |
| 7024 | USA | Gearing-class (DDR) | DDR | Alternative | 6 | Radar Picket | 1950 | 0 | 3000 | 6 | 0 | 0 | Radar picket | Early warning radar DD | Radar Picket DD | Long-range radar | Radar picket conversion |
| 7025 | USA | Forrest Sherman-class | DD | Post-War | 7 | First Post-War | 1955 | 0 | 20000 | 42 | 18000000 | 36 | First post-war DD | 2,800 tons, modern design | Post-War DD | Modern 3"/50 guns | 18 ships, first post-war |
| 7026 | USA | Forrest Sherman-class DDG | DDG | Conversion | 7 | Missile Conversion | 1967 | 0 | 8000 | 18 | 0 | 0 | Tartar conversion | 4 ships, Tartar missiles | Missile DD | Tartar SAM conversion | 4 conversions |
| 7027 | USA | Mitscher-class | DL | Leader | 7 | Destroyer Leader | 1953 | 0 | 18000 | 36 | 22000000 | 42 | Large leader | 3,675 tons, leader | Large DD Leader | ASW + AA leader | 4 ships, large DL |
| 7028 | USA | Farragut/Coontz-class | DDG | Guided Missile | 7 | First Missile DD | 1959 | 0 | 25000 | 48 | 45000000 | 48 | First purpose DDG | 4,700 tons, Terrier SAM | Purpose Missile DD | Terrier SAM, 10 ships | 10 ships, first DDG |
| 7029 | USA | Charles F. Adams-class | DDG | Guided Missile | 7 | Tartar DDG | 1960 | 0 | 22000 | 42 | 38000000 | 42 | Tartar missile DD | 3,370 tons, Tartar SAM | Tartar DDG | Tartar SAM, 23 ships | 23 ships, most numerous |
| 7030 | USA | Charles F. Adams-class (NTU) | DDG | Modernization | 7 | NTU Upgrade | 1982 | 0 | 7000 | 12 | 0 | 0 | New Threat Upgrade | Standard SM-1 upgrade | Modernized DDG | Standard missiles | 1980s upgrade |
| 7031 | USA | Spruance-class | DD | Gas Turbine | 8 | Gas Turbine DD | 1975 | 0 | 30000 | 48 | 125000000 | 36 | First gas turbine | 5,800 tons, 4× LM2500 | Gas Turbine DD | Gas turbine, 31 ships | Revolutionary propulsion |
| 7032 | USA | Spruance-class (VLS) | DD | Modernization | 8 | VLS Upgrade | 1989 | 0 | 10000 | 18 | 0 | 0 | Vertical launch | Mk 41 VLS upgrade | VLS DD | 61-cell Mk 41 VLS | 24 ships upgraded |
| 7033 | USA | Kidd-class | DDG | Gas Turbine | 8 | Modified Spruance | 1981 | 0 | 32000 | 48 | 135000000 | 36 | Modified Spruance | 6,200 tons, Tartar/Standard | Heavy DDG | Modified Spruance, 4 ships | 4 ships, Iran order |
| 7034 | USA | Arleigh Burke-class (Flight I) DDG-51-71 | DDG | Aegis | 8 | Early Aegis DD | 1991 | 0 | 40000 | 60 | 900000000 | 72 | First Aegis DD | 8,300 tons, SPY-1D Aegis | Aegis DD | Aegis SPY-1D, 90 VLS | DDG-51-71, Flight I |
| 7035 | USA | Arleigh Burke-class (Flight II) DDG-72-78 | DDG | Aegis | 8 | Improved Aegis DD | 1998 | 0 | 38000 | 54 | 950000000 | 72 | Improved electronics | Better systems | Improved Aegis DD | Upgraded electronics | DDG-72-78, Flight II |
| 7036 | USA | Arleigh Burke-class (Flight IIA) DDG-79-112 | DDG | Aegis | 9 | Aegis with Helo | 2000 | 0 | 36000 | 48 | 1000000000 | 72 | Helo hangar added | 9,200 tons, helo hangar | Ultimate Production DDG | Helo hangar, 96 VLS | DDG-79-112, most numerous |
| 7037 | USA | Arleigh Burke-class (Flight III) DDG-113+ | DDG | Aegis | 9 | Ultimate Aegis | 2016 | 0 | 35000 | 42 | 1200000000 | 72 | SPY-6 radar | AN/SPY-6(V)1 AESA radar | Ultimate Aegis DD | SPY-6 radar, ultimate | DDG-113+, ultimate production |
| 7038 | USA | Zumwalt-class | DDG | Stealth | 9 | Stealth Destroyer | 2016 | 0 | 50000 | 66 | 3500000000 | 84 | Stealth DD | 15,600 tons, advanced automation | Stealth DD | Stealth, 80 VLS, 3 ships | 3 ships, experimental |
| 7039 | USA | Arleigh Burke-class (Flight IV) | DDG | Future | 10 | Future Aegis | 2030 | 0 | 40000 | 48 | 1400000000 | 78 | Hypersonic missiles | 2030s tech, hypersonics | Future DDG | Hypersonic missiles planned | Planned 2030s |
| 7040 | USA | DDG(X) Future Destroyer | DDG | Paper Ship | 10 | Next-Gen | 2040 | 0 | 60000 | 72 | 4000000000 | 96 | Next-generation DD | 2040s tech | Paper Future DD | Next-gen, -10% reliability | Concept, paper design |
| 8000 | USA | Holland-class | SS | Starting | 1 | Early Submarine | 1900 | 1 | 0 | 0 | 150000 | 12 | First US submarine | 64 tons, SS-1 | Tutorial Sub | Primitive: -40% diving, FREE | FREE starting sub, SS-1 |
| 8001 | USA | A-class | SS | Starting | 1 | Early Submarine | 1903 | 1 | 0 | 0 | 250000 | 18 | Better starting sub | 107 tons, 7 built | Scout Sub | Gasoline: +20% range, FREE | FREE starting option, 7 ships |
| 8002 | USA | C-class | SS | Coastal | 2 | Coastal | 1908 | 0 | 2000 | 12 | 400000 | 24 | Coastal submarine | 275 tons, coastal patrol | Coastal SS | Coastal operations | 5 ships |
| 8003 | USA | F-class | SS | Coastal | 2 | Coastal | 1912 | 0 | 2500 | 12 | 500000 | 24 | Larger coastal | 330 tons, improved | Improved Coastal SS | Better dive depth | 4 ships |
| 8004 | USA | H-class | SS | Coastal | 2 | WWI Era | 1913 | 0 | 3000 | 18 | 600000 | 30 | Mass coastal | 350 tons, 18 built | Mass Coastal SS | 18 ships built | Largest early class |
| 8005 | USA | L-class | SS | Fleet Submarine | 3 | WWI | 1916 | 0 | 4000 | 18 | 900000 | 36 | First fleet boats | 450 tons, ocean-going | Early Fleet SS | Ocean-going capable | 11 ships |
| 8006 | USA | O-class | SS | Fleet Submarine | 3 | WWI | 1918 | 0 | 4500 | 18 | 1000000 | 36 | WWI fleet boat | 520 tons, improved range | WWI Fleet SS | Better range | 16 ships |
| 8007 | USA | R-class | SS | Fleet Submarine | 3 | WWI | 1918 | 0 | 5000 | 24 | 1100000 | 42 | Refined WWI | 680 tons, diesel-electric | Diesel-Electric SS | First diesel-electric | 27 ships |
| 8008 | USA | S-class | SS | Fleet Submarine | 3 | Interwar | 1920 | 0 | 6000 | 24 | 1400000 | 42 | Long-serving | 850 tons, 48 ships | Mass Fleet SS | 48 ships, long service | Largest interwar class |
| 8009 | USA | V-class | SS | Cruiser Sub | 4 | Experimental | 1924 | 0 | 8000 | 30 | 5000000 | 60 | Cruiser submarine | 2,000 tons, experimental | Cruiser SS | 6" deck gun, 2,000 tons | 3 ships, experimental |
| 8010 | USA | Porpoise-class | SS | Fleet Submarine | 4 | Pre-War | 1935 | 0 | 7000 | 24 | 2500000 | 48 | P-class fleet boat | 1,310 tons, modern | Modern Fleet SS | All-welded hull | 10 ships |
| 8011 | USA | Salmon-class | SS | Fleet Submarine | 4 | Pre-War | 1938 | 0 | 7500 | 24 | 2700000 | 48 | Improved P-class | 1,450 tons, refined | Improved Fleet SS | Better engines | 6 ships |
| 8012 | USA | Sargo-class | SS | Fleet Submarine | 4 | Pre-War | 1939 | 0 | 8000 | 24 | 2800000 | 48 | Final pre-war | 1,450 tons, pre-war peak | Pre-War Peak SS | Pre-war pinnacle | 10 ships |
| 8013 | USA | Tambor-class | SS | Fleet Submarine | 5 | Early WWII | 1940 | 0 | 9000 | 30 | 3000000 | 54 | Early WWII | 1,475 tons, war-ready | Early War SS | War-ready design | 12 ships |
| 8014 | USA | Gar-class | SS | Fleet Submarine | 5 | Early WWII | 1941 | 0 | 9500 | 30 | 3100000 | 54 | Improved Tambor | 1,525 tons, refined | Refined War SS | Improved Tambor | 6 ships |
| 8015 | USA | Mackerel-class | SS | Coastal | 5 | Training | 1953 | 0 | 3000 | 12 | 1000000 | 18 | Coastal patrol | 303 tons, small coastal | Training SS | Small patrol/training | 2 ships, training |
| 8016 | USA | Barracuda-class | SST | Training | 5 | Training | 1951 | 0 | 3500 | 18 | 1500000 | 24 | Training submarine | 765 tons, dedicated trainer | Training Sub | Dedicated trainer SST | 3 ships, training |
| 8017 | USA | Gato-class | SS | WWII Main Line | 6 | WWII Workhorse | 1941 | 0 | 12000 | 36 | 3500000 | 12 | Mass production | 1,525 tons, 77 ships | WWII Workhorse SS | First mass WWII class | 77 ships, workhorse |
| 8018 | USA | Balao-class | SS | WWII Main Line | 6 | Ultimate Diesel | 1942 | 0 | 13000 | 36 | 3700000 | 12 | Improved dive depth | 1,526 tons, 122 ships | Deep-Diving SS | 400ft test depth | 122 ships, largest |
| 8019 | USA | Tench-class | SS | WWII Main Line | 6 | Peak Diesel | 1944 | 0 | 14000 | 36 | 3900000 | 15 | Ultimate diesel SS | 1,570 tons, peak design | Peak Diesel SS | Ultimate WWII diesel | 29 ships |
| 8020 | USA | Balao-class (GUPPY) | SS | Modernization | 6 | GUPPY Upgrade | 1947 | 0 | 4000 | 12 | 0 | 0 | Snorkel upgrade | Streamlined, snorkel | GUPPY SS | Snorkel, streamlined | Post-war modernization |
| 8021 | USA | Tench-class (GUPPY IIA) | SS | Modernization | 6 | Full GUPPY | 1952 | 0 | 5000 | 18 | 0 | 0 | Full GUPPY upgrade | Full snorkel + battery | Ultimate GUPPY SS | Full modernization | Major upgrade |
| 8022 | USA | Nautilus SSN-571 | SSN | Nuclear Main Line | 7 | First Nuclear | 1954 | 0 | 25000 | 48 | 55000000 | 60 | First nuclear sub | 3,500 tons, S2W reactor | Nuclear Revolution | First nuclear, unlimited range, UNIQUE | SSN-571, first nuclear |
| 8023 | USA | Seawolf SSN-575 | SSN | Alternative | 7 | Experimental | 1957 | 0 | 22000 | 42 | 65000000 | 60 | Experimental reactor | Liquid sodium reactor | Experimental SSN | Sodium reactor, UNIQUE | SSN-575, failed experiment |
| 8024 | USA | Skate-class | SSN | Nuclear Main Line | 7 | Production Nuclear | 1957 | 0 | 20000 | 36 | 45000000 | 54 | Production nuclear | 2,550 tons, S3W/S4W reactors | Production SSN | 4 ships, production | 4 ships, first production |
| 8025 | USA | George Washington-class | SSBN | Ballistic | 7 | First SSBN | 1959 | 0 | 30000 | 54 | 110000000 | 66 | First ballistic | 5,900 tons, 16 Polaris | First SSBN | First ballistic missiles | 5 ships, first SSBN |
| 8026 | USA | Ethan Allen-class | SSBN | Ballistic | 7 | Improved SSBN | 1961 | 0 | 32000 | 54 | 125000000 | 66 | Improved SSBN | 6,900 tons, improved | Improved SSBN | Better missiles | 5 ships |
| 8027 | USA | Skipjack-class | SSN | Nuclear Main Line | 8 | Teardrop Hull | 1959 | 0 | 28000 | 48 | 50000000 | 60 | Teardrop revolution | 3,075 tons, teardrop hull | Fast SSN | Teardrop, 30+ kts | 6 ships, revolutionary |
| 8028 | USA | Thresher/Permit-class | SSN | Nuclear Main Line | 8 | Deep-Diving SSN | 1961 | 0 | 30000 | 54 | 75000000 | 66 | Deep-diving nuclear | 3,750 tons, HY-80 steel | Deep SSN | 1,300ft test depth | 14 ships, deep-diving |
| 8029 | USA | Sturgeon-class | SSN | Nuclear Main Line | 8 | Long-Serving SSN | 1967 | 0 | 32000 | 54 | 85000000 | 72 | Longest SSN class | 4,250 tons, 37 ships | Mass Production SSN | 37 ships, most numerous | Longest SSN class |
| 8030 | USA | Lafayette-class | SSBN | Ballistic | 8 | Mass SSBN | 1963 | 0 | 35000 | 60 | 140000000 | 72 | Mass production SSBN | 7,250 tons, 31 ships | Mass SSBN | 16 Poseidon, 31 ships | Largest SSBN class |
| 8031 | USA | Benjamin Franklin-class | SSBN | Ballistic | 8 | Ultimate Polaris | 1965 | 0 | 37000 | 60 | 150000000 | 72 | Quieter Lafayette | 7,750 tons, quieter | Quiet SSBN | Quieter Lafayette | 12 ships |
| 8032 | USA | Los Angeles-class (Early) SSN-688-699 | SSN | Nuclear Main Line | 9 | Fast Attack | 1974 | 0 | 45000 | 66 | 200000000 | 78 | Fast attack SSN | 6,000 tons, 33+ kts | Fast Attack SSN | Fast, 62 total ships | SSN-688-699, early |
| 8033 | USA | Los Angeles-class (Improved 688i) SSN-700-773 | SSN | Nuclear Main Line | 9 | VLS-Capable | 1981 | 0 | 43000 | 60 | 225000000 | 78 | VLS-capable SSN | VLS + under-ice capability | Improved 688i SSN | 12 VLS Tomahawk | SSN-700-773, improved |
| 8034 | USA | Ohio-class | SSBN | Ballistic | 9 | Strategic Sub | 1981 | 0 | 55000 | 72 | 1500000000 | 84 | Ultimate SSBN | 18,750 tons, 24 Trident | Ultimate SSBN | 24 Trident II missiles | 18 ships, ultimate SSBN |
| 8035 | USA | Ohio-class (SSGN) | SSGN | Cruise Missile | 9 | Cruise Missile | 2006 | 0 | 25000 | 24 | 0 | 0 | SSGN conversion | 154 Tomahawk conversion | Tomahawk SSGN | 154 Tomahawk missiles | 4 conversions |
| 8036 | USA | Seawolf-class | SSN | Nuclear Main Line | 10 | Ultimate Attack | 1997 | 0 | 60000 | 84 | 2800000000 | 96 | Ultimate but expensive | 9,140 tons, ultimate SSN | Ultimate SSN | Ultimate but $2.8B | 3 ships, too expensive |
| 8037 | USA | Virginia-class | SSN | Nuclear Main Line | 10 | Current Production | 2004 | 0 | 50000 | 72 | 1800000000 | 84 | Production SSN | 7,800 tons, affordable | Production SSN | Affordable, modular | Current production |
| 8038 | USA | Columbia-class | SSBN | Ballistic | 10 | Future SSBN | 2028 | 0 | 70000 | 96 | 9000000000 | 108 | Next-gen SSBN | 20,800 tons, future | Future SSBN | 16 Trident II D5 | Planned 2028, future |
| 2000 | British | Majestic-class | BB | Starting | 1 | Pre-Dreadnought | 1895 | 1 | 0 | 0 | 500000 | 36 | Pre-dreadnought BB | 4×12" guns, 14,900 tons | Tutorial BB | Primitive: -40% armor, FREE | FREE starting battleship, 9 ships |
| 2001 | British | Lord Nelson-class | BB | Starting | 1 | Pre-Dreadnought | 1908 | 1 | 0 | 0 | 1500000 | 48 | Last pre-dreadnought | 4×12" + 10×9.2" guns | Scout BB | Transitional design, FREE | FREE starting BB, 2 ships, last pre-dreadnought |
| 2002 | British | HMS Dreadnought | BB | Early Dreadnought | 2 | Dreadnought | 1906 | 0 | 8000 | 18 | 3000000 | 18 | Revolutionary design | 10×12" guns, first all-big-gun | Dreadnought Revolution | First dreadnought, +30% accuracy, UNIQUE | Revolutionized naval warfare, started arms race |
| 2003 | British | Bellerophon-class | BB | Early Dreadnought | 3 | Dreadnought | 1909 | 0 | 12000 | 24 | 3500000 | 24 | Improved Dreadnought | 10×12" guns, 18,800 tons | Improved Dreadnought | Better secondaries | 3 ships, refined design |
| 2004 | British | St Vincent-class | BB | Early Dreadnought | 3 | Dreadnought | 1910 | 0 | 14000 | 30 | 4000000 | 30 | 50-calibre guns | 10×12"/50 guns, more powerful | Powerful Guns | +10% penetration | 3 ships, more powerful main guns |
| 2005 | British | HMS Neptune | BB | Early Dreadnought | 4 | Dreadnought | 1911 | 0 | 16000 | 36 | 4500000 | 36 | First superfiring | 10×12" guns, superfiring turrets | Superfiring Turrets | +15% firepower | First British BB with superfiring turrets |
| 2006 | British | Colossus-class | BB | Early Dreadnought | 4 | Dreadnought | 1911 | 0 | 18000 | 36 | 5000000 | 36 | Increased armor | 10×12" guns, belt armor increased | Armored Dreadnought | +10% armor | 2 ships, improved protection |
| 2007 | British | HMS Agincourt | BB | Early Dreadnought | 4 | Dreadnought | 1914 | 0 | 20000 | 42 | 6000000 | 42 | Unique design | 14×12" guns, ex-Brazilian | Maximum Firepower | 14 main guns, UNIQUE | Originally Brazilian, confiscated 1914 |
| 2008 | British | Orion-class | BB | Super-Dreadnought | 5 | Super-Dreadnought | 1912 | 0 | 22000 | 42 | 6500000 | 42 | First super-dreadnought | 10×13.5" guns, 22,200 tons | Super-Dreadnought | First 13.5" guns, +15% penetration | 4 ships, revolutionary caliber increase |
| 2009 | British | King George V (1912) | BB | Super-Dreadnought | 5 | Super-Dreadnought | 1912 | 0 | 24000 | 48 | 7000000 | 48 | Longer, faster | 10×13.5" guns, 23,400 tons | Refined Super-DD | +5% speed | 4 ships, improved design |
| 2010 | British | Iron Duke-class | BB | Super-Dreadnought | 6 | Super-Dreadnought | 1914 | 0 | 26000 | 48 | 7500000 | 48 | Jutland flagship | 10×13.5" guns, improved secondaries | Jutland Flagship | +10% gunnery, UNIQUE | 4 ships, Grand Fleet flagship at Jutland |
| 2011 | British | HMS Erin | BB | Super-Dreadnought | 6 | Super-Dreadnought | 1914 | 0 | 20000 | 42 | 7000000 | 42 | Ex-Turkish | 10×13.5" guns, confiscated 1914 | Confiscated Ship | Foreign design | Originally Turkish, seized at outbreak of WWI |
| 2012 | British | Queen Elizabeth-class | BB | Fast Battleship | 7 | Fast Battleship | 1915 | 0 | 32000 | 54 | 10000000 | 54 | First fast BB | 8×15" guns, 25 kts, oil-fired | Fast Battleship | +20% speed, +15% range | 5 ships, most successful British BB class |
| 2013 | British | HMS Canada | BB | Fast Battleship | 6 | Fast Battleship | 1915 | 0 | 24000 | 48 | 8000000 | 48 | Ex-Chilean | 10×14" guns, fastest BB (23 kts) | Fast Design | +15% speed | Originally Chilean, purchased 1914 |
| 2014 | British | Revenge-class | BB | WWI Alternative | 7 | WWI Battleship | 1916 | 0 | 30000 | 54 | 9000000 | 54 | Cheaper Queen Elizabeth | 8×15" guns, 21 kts, economical | Economical Design | -15% cost, -10% speed | 5 ships, cheaper alternative to Queen Elizabeth |
| 2015 | British | HMS Ramillies | BB | WWI Alternative | 7 | WWI Battleship | 1917 | 0 | 28000 | 54 | 9000000 | 54 | Revenge-class | Bulge protection added | Bulge Protection | +5% torpedo defense | Revenge-class with bulges |
| 2016 | British | HMS Royal Sovereign | BB | WWI Alternative | 7 | WWI Battleship | 1916 | 0 | 28000 | 54 | 9000000 | 54 | Revenge flagship | Fleet flagship service | Flagship Service | +5% command | Revenge-class flagship |
| 2017 | British | HMS Royal Oak | BB | WWI Alternative | 7 | WWI Battleship | 1916 | 0 | 28000 | 54 | 9000000 | 54 | Revenge-class | Sunk at Scapa Flow 1939 | Scapa Flow Victim | Historical significance | Sunk by U-47 at Scapa Flow, October 1939 |
| 2018 | British | Renown-class | BC | Battlecruiser | 6 | Battlecruiser | 1916 | 0 | 28000 | 48 | 8500000 | 48 | Battlecruiser | 6×15" guns, 32 kts, light armor | Fast Raider | +30% speed, -20% armor | 2 ships, fast capital ships |
| 2019 | British | HMS Repulse | BC | Battlecruiser | 6 | Battlecruiser | 1916 | 0 | 28000 | 48 | 8500000 | 48 | Renown-class | Sunk 1941 with Prince of Wales | Fast BC | +30% speed, -20% armor | Sunk by Japanese aircraft, December 1941 |
| 2020 | British | HMS Hood | BC | Battlecruiser | 8 | Battlecruiser | 1920 | 0 | 40000 | 60 | 12000000 | 60 | Largest battlecruiser | 8×15" guns, 32 kts, 42,670 tons | Iconic Hood | +25% prestige, +15% speed, -20% armor | Largest BC ever built, sunk by Bismarck 1941 |
| 2021 | British | HMS Courageous | BC | Battlecruiser | 5 | Light Battlecruiser | 1917 | 0 | 20000 | 36 | 7000000 | 36 | Light battlecruiser | 4×15" guns, 32 kts, light protection | Light Fast BC | +35% speed, -30% armor | Later converted to aircraft carrier |
| 2022 | British | HMS Nelson | BB | Treaty Era | 8 | Treaty Battleship | 1927 | 0 | 45000 | 66 | 15000000 | 66 | Treaty battleship | 9×16" guns all forward, unique layout | Treaty Innovation | +20% forward firepower, UNIQUE | 2 ships, unique all-forward turret layout |
| 2023 | British | HMS Rodney | BB | Treaty Era | 8 | Treaty Battleship | 1927 | 0 | 45000 | 66 | 15000000 | 66 | Nelson-class | Sank Bismarck 1941 | Bismarck Killer | +15% critical hits | Contributed to sinking Bismarck, May 1941 |
| 2024 | British | King George V (1940) | BB | WWII Modern | 9 | WWII Battleship | 1940 | 0 | 60000 | 72 | 30000000 | 72 | WWII battleship | 10×14" guns, modern design, 5 ships | WWII Ultimate | +15% AA, +10% reliability | 5 ships, treaty-compliant design |
| 2025 | British | HMS Prince of Wales | BB | WWII Modern | 9 | WWII Battleship | 1941 | 0 | 60000 | 72 | 30000000 | 72 | King George V-class | Sunk 1941 with Repulse | WWII Service | +15% AA | Carried Churchill to Atlantic Charter, sunk Dec 1941 |
| 2026 | British | HMS Duke of York | BB | WWII Modern | 9 | WWII Battleship | 1941 | 0 | 60000 | 72 | 30000000 | 72 | King George V-class | Sank Scharnhorst 1943 | Scharnhorst Killer | +15% night combat | Sank Scharnhorst, Battle of North Cape, Dec 1943 |
| 2027 | British | HMS Anson | BB | WWII Modern | 9 | WWII Battleship | 1942 | 0 | 60000 | 72 | 30000000 | 72 | King George V-class | Pacific service | Pacific Service | +10% endurance | KGV-class, Pacific theater service |
| 2028 | British | HMS Howe | BB | WWII Modern | 9 | WWII Battleship | 1942 | 0 | 60000 | 72 | 30000000 | 72 | King George V-class | Final KGV ship | Final KGV | +10% reliability | Last ship of KGV-class completed |
| 2029 | British | HMS Vanguard | BB | Ultimate | 10 | Last Battleship | 1946 | 0 | 80000 | 84 | 50000000 | 84 | Last British BB | 8×15" guns, 44,500 tons, best British BB | Last Battleship | +20% all stats, never saw combat, UNIQUE | Last battleship ever built for Royal Navy |
| 2030 | British | Queen Elizabeth (Mod) | BB | Modernization | 8 | Modernized BB | 1937 | 0 | 15000 | 24 | 5000000 | 24 | 1930s modernization | Improved AA, radar, fire control | Modernized | +15% AA, +10% FCS | Extensive 1930s refit |
| 2031 | British | HMS Warspite (Mod) | BB | Modernization | 8 | Modernized BB | 1937 | 0 | 15000 | 24 | 5000000 | 24 | Extensive refit | Queen Elizabeth-class modernization | Most Battle Honors | +15% accuracy, UNIQUE | Most battle honors of any Royal Navy ship |
| 2032 | British | Renown (Modernized) | BC | Modernization | 8 | Modernized BC | 1939 | 0 | 18000 | 30 | 6000000 | 30 | Major reconstruction | Improved armor, AA, machinery | Rebuilt BC | +10% armor, +15% AA | Major reconstruction 1936-1939 |
| 2033 | British | Nelson (Modernized) | BB | Modernization | 9 | Modernized BB | 1940 | 0 | 20000 | 18 | 7000000 | 18 | WWII refit | Improved AA, radar | WWII Refit | +20% AA | Wartime improvements |
| 2034 | British | King George V (Mod) | BB | Modernization | 9 | Modernized BB | 1945 | 0 | 12000 | 12 | 4000000 | 12 | Post-war refit | Enhanced electronics, AA | Post-War Mod | +10% all systems | Post-WWII modernization |
| 2035 | British | Lion-class (1939) | BB | Paper Ship | 9 | Cancelled BB | 1939 | 0 | 70000 | 84 | 45000000 | 84 | Cancelled design | 9×16" guns, WWII design cancelled | Paper Ship | -10% reliability, +15% firepower | Cancelled due to WWII, never built |
| 2036 | British | G3 Battlecruiser | BC | Paper Ship | 9 | Cancelled BC | 1921 | 0 | 75000 | 78 | 40000000 | 78 | Treaty cancelled | 9×16" guns, revolutionary design | Revolutionary Design | -10% reliability, +20% speed | Cancelled by Washington Treaty |
| 2037 | British | N3 Battleship | BB | Paper Ship | 9 | Cancelled BB | 1921 | 0 | 80000 | 90 | 50000000 | 90 | Largest British design | 9×18" guns, 48,000 tons | Largest Design | -10% reliability, +25% firepower | Cancelled, largest British BB design |
| 2038 | British | Super Lion | BB | Paper Ship | 10 | Cancelled BB | 1940 | 0 | 85000 | 96 | 60000000 | 96 | Improved Lion | Enhanced Lion design | Paper Ship | -10% reliability | Improved Lion-class, never built |
| 2039 | British | HMS Incomparable | BC | Paper Ship | 8 | Cancelled BC | 1915 | 0 | 50000 | 72 | 30000000 | 72 | Fisher's monster | 6×20" guns, extreme design | Monster Cruiser | -20% reliability, +30% firepower | Fisher's extreme battlecruiser concept |
| 2100 | British | HMS Furious (1917) | CV | Starting | 1 | WWI Conversion | 1917 | 1 | 0 | 0 | 2000000 | 24 | Battlecruiser conversion | Forward flight deck only | Pioneer | First carrier operations, FREE | FREE starting CV, forward deck only |
| 2101 | British | HMS Argus | CV | Starting | 1 | WWI Conversion | 1918 | 1 | 0 | 0 | 2500000 | 30 | First flush-deck | 15 aircraft, full-length deck | Flush Deck | +10% landing safety, FREE | FREE starting CV, first flush-deck |
| 2102 | British | HMS Courageous | CV | Early Conversion | 2 | Large Conversion | 1928 | 0 | 10000 | 18 | 5000000 | 36 | Battlecruiser conversion | 22,500 tons, 48 aircraft | Large Conversion | +25% aircraft capacity | Battlecruiser conversion, sunk 1940 |
| 2103 | British | HMS Glorious | CV | Early Conversion | 2 | Large Conversion | 1930 | 0 | 10000 | 18 | 5000000 | 36 | Sister to Courageous | 22,500 tons, 48 aircraft | Speed | +28 kts, fast carrier | Sister to Courageous, sunk 1940 |
| 2104 | British | HMS Furious (Reconstructed) | CV | Full Conversion | 3 | Full Conversion | 1925 | 0 | 15000 | 24 | 8000000 | 48 | Full-length flight deck | 576 ft deck, 36 aircraft, no island | Reconstructed | +20% efficiency | 1921-1925 reconstruction |
| 2105 | British | HMS Hermes (1924) | CV | Early Dedicated | 3 | Purpose-Built | 1924 | 0 | 12000 | 18 | 6000000 | 42 | First purpose-built | 10,850 tons, 20 aircraft | Purpose-Built | +15% reliability | First British purpose-built CV |
| 2106 | British | HMS Eagle (1924) | CV | Early Dedicated | 3 | Conversion | 1924 | 0 | 12000 | 18 | 7000000 | 48 | Converted Chilean BB | 22,600 tons, 21 aircraft | Conversion | Large hangar capacity | Converted from Chilean battleship |
| 2107 | British | HMS Ark Royal (1938) | CV | Early Dedicated | 4 | Fleet Carrier | 1938 | 0 | 20000 | 30 | 10000000 | 54 | First modern fleet | 22,000 tons, 60 aircraft | Modern | +30% aircraft capacity | First modern British fleet carrier |
| 2108 | British | HMS Illustrious | CV | Armored Fleet Main | 6 | Armored Fleet | 1940 | 0 | 35000 | 42 | 15000000 | 60 | Revolutionary armored deck | 3" armored flight deck, 36 aircraft | Armored Deck | +50% bomb resistance | Revolutionary armored flight deck |
| 2109 | British | HMS Formidable | CV | Armored Fleet Main | 6 | Armored Fleet | 1940 | 0 | 35000 | 42 | 15000000 | 60 | Illustrious class | Armored box hangar, 36 aircraft | Taranto | +25% night strike capability | Illustrious class, Taranto veteran |
| 2110 | British | HMS Victorious | CV | Armored Fleet Main | 6 | Armored Fleet | 1941 | 0 | 35000 | 42 | 15000000 | 60 | Illustrious class | Hunted Bismarck, 36 aircraft | Fleet | +20% endurance | Illustrious class, hunted Bismarck |
| 2111 | British | HMS Indomitable | CV | Armored Modified | 6 | Armored Fleet | 1941 | 0 | 35000 | 42 | 16000000 | 60 | Modified Illustrious | 2-deck hangar, 48 aircraft | 2-Deck Hangar | +33% aircraft capacity | Modified Illustrious, 2-deck hangar |
| 2112 | British | HMS Implacable | CV | Armored Improved | 7 | Armored Improved | 1944 | 0 | 40000 | 48 | 18000000 | 66 | Improved armored | 23,000 tons, 54 aircraft | Improved Armor | +15% resistance | Improved armored design |
| 2113 | British | HMS Indefatigable | CV | Armored Improved | 7 | Armored Improved | 1944 | 0 | 40000 | 48 | 18000000 | 66 | Sister to Implacable | 54 aircraft, reinforced armor | Reinforced | +10% structural strength | Sister to Implacable |
| 2114 | British | HMS Colossus | CVL | Light Fleet | 5 | Light Fleet | 1944 | 0 | 25000 | 36 | 12000000 | 48 | Light carrier | 13,190 tons, 48 aircraft | Light Fleet | -30% cost, mass production | Mass-produced light carrier |
| 2115 | British | HMS Glory | CVL | Light Fleet | 5 | Light Fleet | 1945 | 0 | 25000 | 36 | 12000000 | 48 | Colossus class | 10 ships built, 48 aircraft | Escort | ASW +20% | Colossus class, escort carrier |
| 2116 | British | HMS Majestic | CVL | Light Fleet | 5 | Light Fleet | 1948 | 0 | 25000 | 36 | 13000000 | 48 | Modified Colossus | 6 ships, sold to allies | Export | Allied cooperation bonus | Modified Colossus, export success |
| 2117 | British | HMS Magnificent | CVL | Light Fleet | 5 | Light Fleet | 1948 | 0 | 25000 | 36 | 13000000 | 48 | Majestic class | Improved design, 48 aircraft | Improved Light | +15% efficiency | Majestic class improved |
| 2118 | British | HMS Eagle (1951) | CV | Postwar Fleet | 8 | Postwar Fleet | 1951 | 0 | 50000 | 60 | 50000000 | 72 | Audacious class | 36,800 tons, 60 aircraft | Angled Deck | +30% sortie rate | Audacious class, angled deck |
| 2119 | British | HMS Ark Royal (1955) | CV | Postwar Fleet | 8 | Postwar Fleet | 1955 | 0 | 50000 | 60 | 55000000 | 72 | Audacious class | Steam catapults, 50 aircraft | Steam Catapult | Heavy aircraft capable | Audacious class, steam catapults |
| 2120 | British | HMS Ark Royal (Modernized) | CV | Modernized Fleet | 9 | Modernized Fleet | 1970 | 0 | 60000 | 72 | 75000000 | 84 | 1970s refit | Phantom/Buccaneer capable | Phantom Capable | Modern jets +40% | 1970s refit, Phantom capable |
| 2121 | British | HMS Centaur | CVL | Postwar Light | 7 | Light Fleet | 1953 | 0 | 38000 | 48 | 40000000 | 60 | Centaur class | 24,000 tons, 42 aircraft | Postwar Light | +20% versatility | Centaur class light carrier |
| 2122 | British | HMS Albion | CVL | Postwar Light | 7 | Light Fleet | 1954 | 0 | 38000 | 48 | 40000000 | 60 | Centaur class | Commando carrier conversion | Commando | Amphibious +25% | Centaur class, commando carrier |
| 2123 | British | HMS Bulwark | CVL | Postwar Light | 7 | Light Fleet | 1954 | 0 | 38000 | 48 | 40000000 | 60 | Centaur class | Commando carrier | Amphibious | Marine ops +30% | Centaur class, commando carrier |
| 2124 | British | HMS Hermes (1959) | CV | Postwar Light | 8 | Light Fleet | 1959 | 0 | 45000 | 54 | 50000000 | 66 | Improved Centaur | 28,700 tons, last UK conventional | Last Conventional | +25% reliability | Last UK conventional carrier |
| 2125 | British | HMS Invincible | CVS | Through-Deck | 9 | VSTOL Carrier | 1980 | 0 | 55000 | 66 | 300000000 | 72 | Through-deck cruiser | 20,600 tons, Sea Harrier | VSTOL | Sea Harrier capable | Through-deck cruiser, VSTOL |
| 2126 | British | HMS Illustrious (1982) | CVS | Through-Deck | 9 | VSTOL Carrier | 1982 | 0 | 55000 | 66 | 300000000 | 72 | Invincible class | Falklands War, 22 aircraft | Falklands Veteran | +20% combat experience | Invincible class, Falklands War |
| 2127 | British | HMS Ark Royal (1985) | CVS | Through-Deck | 9 | VSTOL Carrier | 1985 | 0 | 55000 | 66 | 300000000 | 72 | Invincible class | Ski-jump, Sea Harrier | Ski-Jump | +15% VSTOL efficiency | Invincible class, ski-jump |
| 2128 | British | HMS Queen Elizabeth (2017) | CVN | Supercarrier | 10 | Supercarrier | 2017 | 0 | 85000 | 102 | 4000000000 | 96 | Modern supercarrier | 65,000 tons, 40 F-35B | Supercarrier | 40 F-35B, largest UK warship | Modern supercarrier, largest UK |
| 2129 | British | HMS Prince of Wales | CVN | Supercarrier | 10 | Supercarrier | 2019 | 0 | 85000 | 102 | 4000000000 | 96 | Queen Elizabeth class | 65,000 tons, F-35B | F-35B Capable | 5th-gen stealth fighters | Queen Elizabeth class |
| 2130 | British | HMS Queen Elizabeth (Enhanced) | CVN | Future Supercarrier | 10 | Future Supercarrier | 2030 | 0 | 90000 | 108 | 5000000000 | 108 | Future enhancement | EMALS, 60 aircraft | EMALS | +50% sortie rate | Future enhancement, EMALS |
| 2131 | British | HMS Illustrious (1945 Refit) | CV | Modernization | 7 | Modernization | 1945 | 0 | 35000 | 42 | 8000000 | 18 | Postwar refit | Improved radar, jet capable | Postwar Refit | Jet capable | Postwar refit, improved systems |
| 2132 | British | HMS Victorious (1950s Recon) | CV | Modernization | 8 | Modernization | 1958 | 0 | 45000 | 54 | 30000000 | 36 | Major reconstruction | Angled deck, steam catapults | Major Reconstruction | +40% capability | Major 1950s reconstruction |
| 2133 | British | HMS Hermes (1980s Refit) | CV | Modernization | 9 | Modernization | 1981 | 0 | 50000 | 60 | 100000000 | 24 | Sea Harrier capable | Ski-jump added | Ski-Jump Added | VSTOL conversion | Ski-jump added, Harrier capable |
| 2134 | British | HMS Invincible (Modernized) | CVS | Modernization | 9 | Modernization | 1995 | 0 | 55000 | 66 | 150000000 | 30 | Extended refit | Improved systems | Extended Refit | +25% systems | Extended 1995 refit |
| 2135 | British | HMS Malta | CV | Paper Ship | 8 | Cancelled CV | 1945 | 0 | 60000 | 72 | 60000000 | 84 | Malta class | 46,900 tons, cancelled 1945 | Malta Class | Large fleet carrier | Cancelled 1945, -10% reliability |
| 2136 | British | HMS Gibraltar | CV | Paper Ship | 8 | Cancelled CV | 1945 | 0 | 60000 | 72 | 60000000 | 84 | Malta class sister | Large fleet carrier, cancelled | Sister Ship | Production efficiency | Malta class, cancelled 1945 |
| 2137 | British | CVA-01 | CV | Paper Ship | 9 | Cancelled Supercarrier | 1966 | 0 | 70000 | 84 | 500000000 | 96 | 1960s supercarrier | 54,500 tons, cancelled 1966 | CVA-01 | Modern supercarrier concept | Cancelled 1966, -15% reliability |
| 2138 | British | CVA-01 Improved | CV | Paper Ship | 9 | Cancelled Variant | 1966 | 0 | 70000 | 84 | 550000000 | 96 | Enhanced CVA-01 | Nuclear propulsion option | Nuclear Option | Extended range | Enhanced CVA-01, -15% reliability |
| 2139 | British | Future Carrier Concept | CVN | Paper Ship | 10 | Future Design | 2040 | 0 | 85000 | 102 | 6000000000 | 120 | Next-generation | 80,000+ tons, EMALS, 2040+ | Future Carrier | Next-generation | Future concept, -10% reliability |
| 2600 | British | Pelorus-class | CL | Starting | 1 | Protected Cruiser | 1896 | 1 | 0 | 0 | 750000 | 36 | 2nd class protected | 2,135 tons, 11 ships | Tutorial CL | Primitive: -30% armor, FREE | FREE starting cruiser |
| 2601 | British | Leander-class (1931) | CL | Starting | 1 | Light Cruiser | 1931 | 1 | 0 | 0 | 2000000 | 36 | Treaty light cruiser | 7,200 tons, 8×6" guns | Scout CL | Empire Reach: +15% range, FREE | FREE starting cruiser, better option |
| 2602 | British | Cressy-class | CA | Protected/Armored | 2 | Protected Cruiser | 1900 | 0 | 5000 | 12 | 1000000 | 42 | Armored cruiser | 12,000 tons, 2×9.2" guns | Early Armored CA | Royal Navy Standards: +10% reliability | 6 ships, armored cruiser |
| 2603 | British | Drake-class | CA | Protected/Armored | 3 | Armored Cruiser | 1901 | 0 | 10000 | 18 | 1500000 | 48 | Improved armored | 14,100 tons, improved armor | Improved Armored CA | Better armor protection | 4 ships |
| 2604 | British | Warrior-class | CA | Protected/Armored | 3 | Armored Cruiser | 1905 | 0 | 12000 | 18 | 1800000 | 48 | Enhanced armament | 13,550 tons, 6×9.2" guns | Enhanced CA | Enhanced firepower | 4 ships |
| 2605 | British | Duke of Edinburgh-class | CA | Protected/Armored | 4 | Armored Cruiser | 1906 | 0 | 15000 | 24 | 2000000 | 54 | Balanced design | 13,550 tons, balanced | Balanced CA | Balanced design philosophy | 2 ships |
| 2606 | British | Devonshire-class | CA | Protected/Armored | 4 | Armored Cruiser | 1904 | 0 | 17000 | 24 | 2200000 | 54 | Late armored | 10,850 tons, 4×7.5" guns | Late Armored CA | Final armored cruiser design | 6 ships |
| 2607 | British | Monmouth-class | CA | Protected/Armored | 4 | Armored Cruiser | 1903 | 0 | 18000 | 24 | 2400000 | 60 | Ultimate armored | 9,800 tons, last armored | Ultimate Armored CA | Last armored cruiser class | 10 ships |
| 2608 | British | Town-class (1910) | CL | Light Main Line | 2 | Scout Cruiser | 1910 | 0 | 6000 | 12 | 1200000 | 36 | WWI scout | 5,400 tons, 8×6" guns | Scout CL | Light, fast scouting | 20 ships, Bristol/Weymouth/Chatham groups |
| 2609 | British | Arethusa-class (1913) | CL | Light Main Line | 3 | WWI Light | 1913 | 0 | 11000 | 18 | 1500000 | 42 | WWI light cruiser | 3,520 tons, 2×6" guns | WWI Light CL | Small, fast | 8 ships |
| 2610 | British | C-class | CL | Light Main Line | 3 | WWI Light | 1914 | 0 | 13000 | 18 | 1600000 | 42 | WWI standard | 4,200 tons, 5×6" guns | Standard WWI CL | WWI workhorse | 28 ships, Caledon/Ceres/Carlisle groups |
| 2611 | British | D-class | CL | Light Main Line | 4 | WWI Light | 1918 | 0 | 16000 | 24 | 1800000 | 48 | WWI improved | 4,650 tons, 6×6" guns | Improved WWI CL | Enhanced design | 8 ships, Danae/Dauntless groups |
| 2612 | British | E-class | CL | Light Main Line | 4 | Interwar | 1926 | 0 | 18000 | 24 | 2000000 | 48 | Interwar light | 7,550 tons, 7×6" guns | Interwar CL | Modern interwar design | 7 ships, Enterprise/Emerald groups |
| 2613 | British | Emerald-class | CL | Light Main Line | 5 | Interwar | 1926 | 0 | 20000 | 30 | 2200000 | 54 | First 6" modern | 7,550 tons, modern 6" | Modern CL | First modern 6" cruiser | 2 ships |
| 2614 | British | Leander-class (1931) | CL | Light Main Line | 5 | Treaty Light | 1931 | 0 | 22000 | 30 | 2500000 | 54 | Treaty light cruiser | 7,200 tons, 8×6" guns | Treaty CL | Empire Reach: +15% range | 8 ships |
| 2615 | British | Amphion-class | CL | Light Main Line | 5 | Treaty Light | 1934 | 0 | 24000 | 30 | 2700000 | 54 | Improved Leander | 7,030 tons, improved | Improved Treaty CL | Enhanced Leander | 4 ships, Perth group |
| 2616 | British | Arethusa-class (1934) | CL | Light Main Line | 6 | Pre-WWII | 1935 | 0 | 26000 | 36 | 2900000 | 60 | Enhanced light | 5,220 tons, 6×6" guns | Enhanced Light CL | Compact, effective | 4 ships |
| 2617 | British | Town-class (1936) | CL | Light Main Line | 6 | Pre-WWII | 1936 | 0 | 28000 | 36 | 3200000 | 60 | Pre-WWII peak | 9,100 tons, 12×6" guns | Pre-War Peak CL | 12×6" guns in 4 triple turrets | 10 ships, Southampton/Gloucester/Edinburgh groups |
| 2618 | British | Fiji-class | CL | Light Main Line | 7 | WWII Light | 1940 | 0 | 32000 | 42 | 3500000 | 18 | Colony-class | 8,000 tons, 12×6" guns | WWII Colony CL | WWII mass production | 11 ships, Colony-class |
| 2619 | British | Minotaur-class | CL | Light Main Line | 7 | Late WWII | 1943 | 0 | 35000 | 42 | 3800000 | 24 | Late WWII light | 8,800 tons, 9×6" guns | Late War CL | Final WWII light cruiser | 3 ships |
| 2620 | British | Tiger-class | CG | Light Main Line | 8 | Post-War | 1959 | 0 | 42000 | 54 | 25000000 | 72 | Post-war gun cruiser | 11,700 tons, 4×6" guns | Post-War Gun CG | Last gun cruiser design | 3 ships, never completed as designed |
| 2621 | British | Dido-class | CLAA | AA Specialist | 7 | AA Cruiser | 1940 | 0 | 30000 | 42 | 3300000 | 24 | AA cruiser | 5,770 tons, 10×5.25" DP | AA Cruiser | ASDIC Pioneer: +20% ASW | 16 ships, fleet air defense |
| 2622 | British | Bellona-class | CLAA | AA Specialist | 7 | AA Cruiser | 1943 | 0 | 33000 | 42 | 3500000 | 24 | Improved AA | 5,770 tons, improved AA | Improved AA Cruiser | Enhanced air defense | 4 ships, Dido subclass |
| 2623 | British | Scylla-class | CLAA | AA Specialist | 7 | AA Cruiser | 1942 | 0 | 34000 | 42 | 3600000 | 24 | Final AA cruiser | 5,770 tons, final AA variant | Final AA Cruiser | Ultimate AA design | Modified Dido variant |
| 2624 | British | Hawkins-class | CA | Heavy Cruiser | 5 | Heavy Cruiser | 1919 | 0 | 21000 | 30 | 2800000 | 60 | WWI heavy | 9,860 tons, 7×7.5" guns | WWI Heavy CA | Early heavy cruiser | 5 ships |
| 2625 | British | County-class (Kent) | CA | Heavy Cruiser | 5 | Treaty Heavy | 1928 | 0 | 24000 | 30 | 3000000 | 60 | Treaty 8" cruiser | 10,000 tons, 8×8" guns | Treaty Heavy CA | Empire Reach: +15% range | 7 ships, Kent group |
| 2626 | British | County-class (London) | CA | Heavy Cruiser | 6 | Treaty Heavy | 1929 | 0 | 26000 | 36 | 3200000 | 60 | Improved County | 10,000 tons, improved | Improved Heavy CA | Enhanced County | 4 ships, London group |
| 2627 | British | County-class (Norfolk) | CA | Heavy Cruiser | 6 | Treaty Heavy | 1930 | 0 | 28000 | 36 | 3400000 | 60 | Final County | 10,000 tons, final variant | Final County CA | Final County variant | 2 ships, Norfolk group |
| 2628 | British | York-class | CA | Heavy Cruiser | 6 | Treaty Heavy | 1930 | 0 | 30000 | 36 | 3600000 | 60 | Reduced CA | 8,250 tons, 6×8" guns | Reduced Heavy CA | Economical design | 2 ships |
| 2629 | British | Exeter-class | CA | Heavy Cruiser | 6 | Treaty Heavy | 1931 | 0 | 32000 | 36 | 3800000 | 60 | Improved York | 8,390 tons, improved York | Improved York CA | Enhanced York design | 1 ship, unique |
| 2630 | British | Tiger-class | CG | Post-War | 8 | Post-War | 1959 | 0 | 40000 | 48 | 25000000 | 72 | Post-war gun cruiser | 11,700 tons, 4×6" + 6×3" | Post-War Gun CG | Royal Navy Standards: +10% reliability | 3 ships, cancelled/converted |
| 2631 | British | Blake-class | CG | Post-War | 8 | Post-War | 1961 | 0 | 42000 | 48 | 28000000 | 72 | Improved Tiger | 12,000 tons, helicopter ops | Helo Cruiser CG | Helicopter operations | 2 ships, Tiger conversion |
| 2632 | British | County-class (DDG) | DDG | Guided Missile | 9 | Missile Era | 1962 | 0 | 48000 | 60 | 35000000 | 66 | First missile destroyer | 6,200 tons, Sea Slug SAM | First Missile DDG | Sea Slug missile system | 8 ships, first British DDG |
| 2633 | British | Bristol-class | DDG | Guided Missile | 9 | Missile Era | 1973 | 0 | 50000 | 60 | 45000000 | 72 | Improved DDG | 7,100 tons, Sea Dart SAM | Improved DDG | Sea Dart missile system | 1 ship, unique design |
| 2634 | British | Sheffield-class (Type 42 Batch 1) | DDG | Guided Missile | 9 | Modern DDG | 1975 | 0 | 45000 | 54 | 50000000 | 60 | Sea Dart DDG | 4,775 tons, Sea Dart | Sea Dart DDG | Modern missile destroyer | 6 ships, Batch 1 |
| 2635 | British | Sheffield-class (Type 42 Batch 2) | DDG | Guided Missile | 9 | Modern DDG | 1978 | 0 | 43000 | 48 | 55000000 | 60 | Improved Type 42 | 4,775 tons, improved | Improved Type 42 | Enhanced systems | 4 ships, Batch 2 |
| 2636 | British | Sheffield-class (Type 42 Batch 3) | DDG | Guided Missile | 9 | Modern DDG | 1982 | 0 | 41000 | 42 | 60000000 | 60 | Final Type 42 | 5,200 tons, stretched hull | Final Type 42 | Stretched hull, better seakeeping | 4 ships, Batch 3 |
| 2637 | British | Type 22 Broadsword-class | FFG | Post-War | 9 | Modern FFG | 1979 | 0 | 38000 | 48 | 70000000 | 66 | ASW frigate | 4,800 tons, Sea Wolf SAM | ASW Frigate | ASDIC Pioneer: +20% ASW, Sea Wolf | 14 ships, 3 batches |
| 2638 | British | Type 23 Duke-class (Batch 1) | FFG | Post-War | 10 | Modern FFG | 1990 | 0 | 48000 | 60 | 150000000 | 72 | Stealth frigate | 4,900 tons, stealth design | Stealth Frigate | Silent Service: +15% stealth | 8 ships, Batch 1 |
| 2639 | British | Type 23 Duke-class (Batch 2) | FFG | Post-War | 10 | Modern FFG | 1993 | 0 | 46000 | 54 | 160000000 | 72 | Improved Type 23 | 4,900 tons, improved | Improved Stealth FFG | Enhanced systems | 8 ships, Batch 2 |
| 2640 | British | Type 26 Frigate | FFG | Post-War | 10 | Future FFG | 2023 | 0 | 52000 | 66 | 500000000 | 84 | Next-gen frigate | 8,000 tons, future ASW | Future ASW Frigate | Advanced ASW systems | 8 ships, current production |
| 2641 | British | Tiger-class (Modernized) | CG | Modernization | 8 | Modernized | 1972 | 0 | 12000 | 24 | 0 | 0 | Helicopter conversion | Sea Cat + 2× Wessex helos | Helo Ops Modernization | Helicopter operations | 2 ships converted |
| 2642 | British | County-class (DDG Modernized) | DDG | Modernization | 9 | Modernized | 1975 | 0 | 15000 | 30 | 0 | 0 | Sea Dart upgrade | Sea Slug to Sea Dart | Sea Dart Modernization | Sea Dart missile upgrade | Selected ships upgraded |
| 2643 | British | Sheffield-class (Modernized) | DDG | Modernization | 9 | Modernized | 1985 | 0 | 13000 | 24 | 0 | 0 | Electronics upgrade | Electronics + ECM upgrade | Electronics Modernization | Extended service life | Mid-life upgrades |
| 2644 | British | Design CA | CA | Paper Ship | 7 | Design Phase | 1945 | 0 | 38000 | 54 | 5000000 | 66 | Cancelled heavy | Improved Exeter design | Paper Heavy CA | Advanced 8" design, -10% reliability | Cancelled post-WWII |
| 2645 | British | Future Cruiser Concept | CG | Paper Ship | 10 | Future Concept | 2040 | 0 | 70000 | 84 | 2000000000 | 96 | Next-gen cruiser | Advanced systems concept | Paper Future CG | Advanced systems, -10% reliability | Conceptual design |
| 2700 | British | 27-knotter | DD | Starting | 1 | Early TBD | 1894 | 1 | 0 | 0 | 100000 | 18 | Early torpedo boat destroyer | 280 tons, primitive | Tutorial DD | Primitive: -40% reliability, FREE | FREE starting destroyer |
| 2701 | British | River-class | DD | Starting | 1 | Scout Destroyer | 1903 | 1 | 0 | 0 | 200000 | 24 | Better starting destroyer | 550 tons, improved | Scout DD | Atlantic Veteran: +10% endurance, FREE | FREE starting destroyer, better option |
| 2702 | British | Tribal-class (F) | DD | Pre-WWI | 2 | Pre-WWI | 1909 | 0 | 5000 | 12 | 300000 | 30 | Letter naming begins | 1,100 tons, letter naming | Pre-WWI DD | Letter class naming system | 12 ships, F-class |
| 2703 | British | Acorn-class (H) | DD | Pre-WWI | 2 | Pre-WWI | 1910 | 0 | 6000 | 12 | 350000 | 30 | Improved TBD | 780 tons, coal-fired | Improved TBD | Oil-fired variant | 20 ships, H-class |
| 2704 | British | Beagle-class (G) | DD | Pre-WWI | 3 | Pre-WWI | 1909 | 0 | 10000 | 18 | 380000 | 36 | Pre-WWI standard | 900 tons, standard | Standard Pre-WWI DD | Oil and coal mix | 16 ships, G-class |
| 2705 | British | Acasta-class (K) | DD | Pre-WWI | 3 | Pre-WWI | 1912 | 0 | 12000 | 18 | 420000 | 36 | Pre-WWI peak | 1,000 tons, peak design | Peak Pre-WWI DD | All oil-fired | 20 ships, K-class |
| 2706 | British | Admiralty M-class | DD | WWI Main | 4 | WWI | 1914 | 0 | 15000 | 24 | 500000 | 42 | WWI standard | 1,000 tons, WWI workhorse | WWI Standard DD | Mass production design | 116 ships, M-class group |
| 2707 | British | R-class | DD | WWI Main | 4 | WWI | 1916 | 0 | 17000 | 24 | 550000 | 42 | WWI improved | 1,035 tons, improved | Improved WWI DD | Enhanced seakeeping | 62 ships, R-class |
| 2708 | British | V-class | DD | WWI Main | 5 | WWI | 1917 | 0 | 19000 | 30 | 600000 | 48 | WWI advanced | 1,090 tons, advanced | Advanced WWI DD | Better armament | 28 ships, V-class |
| 2709 | British | W-class | DD | WWI Main | 5 | WWI | 1918 | 0 | 21000 | 30 | 650000 | 48 | WWI peak | 1,100 tons, peak design | Peak WWI DD | 4×4" guns | 25 ships, W-class |
| 2710 | British | Modified W-class | DD | WWI Main | 5 | WWI | 1918 | 0 | 22000 | 30 | 680000 | 48 | Ultimate WWI | 1,120 tons, ultimate WWI | Ultimate WWI DD | Modified design | 16 ships, Modified W |
| 2711 | British | A-class | DD | Interwar | 5 | Interwar | 1930 | 0 | 23000 | 30 | 750000 | 54 | First interwar | 1,350 tons, modern | First Interwar DD | Modern design | 9 ships, A-class |
| 2712 | British | B-class | DD | Interwar | 5 | Interwar | 1930 | 0 | 24000 | 30 | 800000 | 54 | Improved interwar | 1,360 tons, improved | Improved Interwar DD | Enhanced systems | 9 ships, B-class |
| 2713 | British | Tribal-class (1936) | DD | Interwar | 6 | Pre-WWII | 1938 | 0 | 28000 | 36 | 1200000 | 60 | Heavy destroyer | 1,850 tons, 8×4.7" guns | Heavy DD | ASDIC Mastery: +20% ASW | 16 ships, powerful armament |
| 2714 | British | J-class | DD | Interwar | 6 | Pre-WWII | 1939 | 0 | 26000 | 36 | 950000 | 60 | Standard WWII | 1,690 tons, standard | Standard WWII DD | Balanced design | 8 ships, J-class |
| 2715 | British | K-class | DD | Interwar | 6 | Pre-WWII | 1939 | 0 | 27000 | 36 | 980000 | 60 | Improved standard | 1,690 tons, improved | Improved Standard DD | Enhanced ASW | 8 ships, K-class |
| 2716 | British | N-class | DD | Interwar | 7 | Pre-WWII | 1940 | 0 | 29000 | 42 | 1000000 | 60 | Enhanced destroyer | 1,690 tons, enhanced | Enhanced DD | Better armament | 8 ships, N-class |
| 2717 | British | O/P-class | DD | Interwar | 7 | Pre-WWII | 1941 | 0 | 30000 | 42 | 1050000 | 60 | Final pre-war | 1,540 tons, final pre-war | Final Pre-War DD | Compact design | 16 ships, O/P combined |
| 2718 | British | Q/R-class | DD | WWII Emergency | 7 | WWII | 1942 | 0 | 32000 | 42 | 1100000 | 24 | Early emergency | 1,705 tons, emergency | Early Emergency DD | War production | 16 ships, Q/R combined |
| 2719 | British | S/T-class | DD | WWII Emergency | 7 | WWII | 1943 | 0 | 33000 | 42 | 1150000 | 24 | Emergency standard | 1,710 tons, standard | Emergency Standard DD | Simplified design | 16 ships, S/T combined |
| 2720 | British | U/V-class | DD | WWII Emergency | 8 | WWII | 1943 | 0 | 34000 | 48 | 1200000 | 24 | Emergency peak | 1,710 tons, peak design | Emergency Peak DD | Mass production | 16 ships, U/V combined |
| 2721 | British | W/Z-class | DD | WWII Emergency | 8 | WWII | 1944 | 0 | 35000 | 48 | 1250000 | 24 | Late emergency | 1,710 tons, late war | Late Emergency DD | Final emergency design | 16 ships, W/Z combined |
| 2722 | British | Battle-class | DD | WWII Emergency | 8 | WWII | 1945 | 0 | 38000 | 48 | 1500000 | 30 | Ultimate WWII DD | 2,315 tons, 4×4.5" DP | Ultimate WWII DD | Dual-purpose guns | 24 ships, ultimate design |
| 2723 | British | Daring-class | DD | Post-War | 8 | Post-War | 1952 | 0 | 40000 | 54 | 3500000 | 60 | Post-war gun DD | 2,800 tons, 6×4.5" DP | Post-War Gun DD | Royal Navy Standards: +10% reliability | 8 ships, post-war design |
| 2724 | British | County-class (DDG) | DDG | Post-War | 9 | Missile Era | 1962 | 0 | 48000 | 60 | 35000000 | 66 | First missile DD | 6,200 tons, Sea Slug | First Missile DDG | Sea Slug missile system | 8 ships, first British DDG |
| 2725 | British | Type 42 Batch 1 | DDG | Post-War | 9 | Modern DDG | 1975 | 0 | 45000 | 54 | 50000000 | 60 | Sea Dart DDG | 4,775 tons, Sea Dart | Sea Dart DDG | Sea Dart missile system | 6 ships, Batch 1 |
| 2726 | British | Type 42 Batch 2 | DDG | Post-War | 9 | Modern DDG | 1978 | 0 | 43000 | 48 | 55000000 | 60 | Improved Type 42 | 4,775 tons, improved | Improved Type 42 | Enhanced systems | 4 ships, Batch 2 |
| 2727 | British | Type 42 Batch 3 | DDG | Post-War | 9 | Modern DDG | 1982 | 0 | 41000 | 42 | 60000000 | 60 | Stretched Type 42 | 5,200 tons, stretched | Stretched Type 42 | Better seakeeping | 4 ships, Batch 3 |
| 2728 | British | Type 42 Batch 3.2 | DDG | Post-War | 9 | Modern DDG | 1985 | 0 | 40000 | 42 | 65000000 | 60 | Final Type 42 | 5,200 tons, final variant | Final Type 42 | Final production variant | Enhanced electronics |
| 2729 | British | Type 45 Batch 1 | DDG | Modern | 10 | Modern DDG | 2009 | 0 | 52000 | 66 | 1200000000 | 84 | PAAMS destroyer | 8,500 tons, PAAMS | PAAMS Air Defense | PAAMS air defense system | 3 ships, Batch 1 |
| 2730 | British | Type 45 Batch 2 | DDG | Modern | 10 | Modern DDG | 2011 | 0 | 50000 | 60 | 1250000000 | 84 | Improved PAAMS | 8,500 tons, improved | Improved PAAMS | Enhanced systems | 3 ships, Batch 2 |
| 2731 | British | Type 45 Batch 3 | DDG | Modern | 10 | Modern DDG | 2013 | 0 | 48000 | 54 | 1300000000 | 84 | Enhanced Type 45 | 8,500 tons, enhanced | Enhanced Type 45 | Final production variant | Ships completed |
| 2732 | British | Type 45A | DDG | Modern | 10 | Modern DDG | 2020 | 0 | 50000 | 60 | 1400000000 | 90 | Advanced variant | 8,800 tons, advanced | Advanced Type 45 | Advanced systems | Proposed upgrade |
| 2733 | British | Type 45 (Modernized) | DDG | Modern | 10 | Modernized | 2025 | 0 | 20000 | 36 | 0 | 0 | Life extension | Mid-life upgrade | Modernized Type 45 | Extended service life | Current modernization program |
| 2734 | British | Type 83 | DDG | Modern | 10 | Future DDG | 2035 | 0 | 70000 | 84 | 2500000000 | 96 | Future destroyer | 12,000+ tons, future systems | Future DDG | Advanced future systems | Planned replacement |
| 2736 | British | Hunt-class | DD | Alternative | 7 | WWII Escort | 1940 | 0 | 25000 | 36 | 700000 | 30 | Escort destroyer | 1,050 tons, ASW escort | Escort DD | ASDIC Mastery: +20% ASW | 86 ships, 4 types, convoy escort |
| 2737 | British | Black Swan-class | DD | Alternative | 7 | ASW Sloop | 1943 | 0 | 27000 | 36 | 800000 | 36 | ASW sloop | 1,350 tons, ASW specialist | ASW Sloop | ASW specialist design | 37 ships, Modified Black Swan |
| 2738 | British | River-class (Frigate) | FFG | Alternative | 8 | ASW Frigate | 1942 | 0 | 30000 | 42 | 950000 | 42 | ASW frigate | 1,370 tons, convoy escort | ASW Frigate | Atlantic Veteran: +10% endurance | 57 ships, convoy escort |
| 2739 | British | Battle-class (Modernized) | DD | Modernization | 8 | Modernized | 1958 | 0 | 10000 | 24 | 0 | 0 | 1950s modernization | Electronics upgrade | Modernized Battle | Electronics and radar upgrades | Selected ships upgraded |
| 2740 | British | Daring-class (Modernized) | DD | Modernization | 8 | Modernized | 1965 | 0 | 12000 | 30 | 0 | 0 | 1960s modernization | Electronics + ASW upgrade | Modernized Daring | Extended service life | Mid-life upgrades |
| 2741 | British | County-class (DDG Modernized) | DDG | Modernization | 9 | Modernized | 1975 | 0 | 15000 | 30 | 0 | 0 | Sea Dart upgrade | Sea Slug to Sea Dart | Sea Dart Modernization | Sea Dart missile upgrade | Selected ships upgraded |
| 2800 | British | Holland-class | SS | Starting | 1 | Early Submarine | 1901 | 1 | 0 | 0 | 50000 | 18 | First British submarine | 122 tons, primitive | Tutorial SS | Primitive: -40% reliability, FREE | FREE starting submarine, HM Submarine No. 1 |
| 2801 | British | A-class | SS | Starting | 1 | Coastal Submarine | 1903 | 1 | 0 | 0 | 100000 | 24 | Improved starting sub | 190 tons, improved | Scout SS | Silent Service: +15% stealth, FREE | FREE starting submarine, 13 boats |
| 2802 | British | B-class | SS | Coastal | 2 | Coastal | 1905 | 0 | 2000 | 12 | 120000 | 30 | Coastal submarine | 280 tons, coastal patrol | Coastal SS | British waters operations | 11 boats |
| 2803 | British | C-class | SS | Coastal | 2 | Coastal | 1906 | 0 | 2500 | 12 | 140000 | 30 | Improved coastal | 290 tons, improved | Improved Coastal SS | Enhanced range | 38 boats |
| 2804 | British | D-class (Coastal) | SS | Coastal | 3 | Coastal | 1908 | 0 | 4000 | 18 | 160000 | 36 | Coastal D variant | 495 tons, coastal | Coastal D-class | Coastal operations | 8 boats, coastal variant |
| 2805 | British | E-class (Coastal) | SS | Coastal | 3 | Coastal | 1912 | 0 | 5000 | 18 | 180000 | 36 | Coastal E variant | 660 tons, coastal | Coastal E-class | Enhanced coastal | Coastal variant |
| 2806 | British | H-class (Coastal) | SS | Coastal | 3 | Coastal | 1915 | 0 | 6000 | 18 | 200000 | 36 | WWI coastal | 364 tons, coastal WWI | WWI Coastal SS | Coastal patrol | 22 boats, Holland design |
| 2807 | British | D-class (Fleet) | SS | Fleet Diesel | 3 | WWI | 1910 | 0 | 6000 | 18 | 250000 | 42 | Fleet submarine | 620 tons, ocean-going | Fleet D-class | Ocean-going capability | 8 boats, fleet variant |
| 2808 | British | E-class (Fleet) | SS | Fleet Diesel | 4 | WWI | 1913 | 0 | 8000 | 24 | 300000 | 48 | WWI fleet boat | 660 tons, fleet | Fleet E-class | WWI workhorse | 58 boats, most successful WWI SS |
| 2809 | British | F-class | SS | Fleet Diesel | 4 | WWI | 1915 | 0 | 10000 | 24 | 350000 | 48 | Improved E-class | 525 tons, improved | Improved Fleet SS | Enhanced design | 3 boats |
| 2810 | British | G-class | SS | Fleet Diesel | 4 | WWI | 1916 | 0 | 12000 | 24 | 400000 | 48 | WWI advanced | 700 tons, advanced | Advanced WWI SS | Better armament | 14 boats |
| 2811 | British | H-class | SS | Fleet Diesel | 5 | WWI | 1918 | 0 | 14000 | 30 | 450000 | 54 | Fleet H variant | 423 tons, fleet | Fleet H-class | Fleet operations | 22 boats, Holland design |
| 2812 | British | J-class | SS | Fleet Diesel | 5 | WWI | 1916 | 0 | 16000 | 30 | 500000 | 54 | Fleet submarine | 1,210 tons, large | Large Fleet SS | First diesel-only | 7 boats, diesel-only |
| 2813 | British | K-class | SS | Fleet Diesel | 5 | Experimental | 1917 | 0 | 18000 | 30 | 700000 | 60 | Steam turbine SS | 1,980 tons, steam | Steam SS | Experimental, troubled | 17 boats, steam turbine (failed) |
| 2814 | British | L-class | SS | Fleet Diesel | 5 | Interwar | 1918 | 0 | 17000 | 30 | 550000 | 54 | Improved fleet | 890 tons, improved | Improved Fleet SS | Better design | 34 boats |
| 2815 | British | M-class | SS | Fleet Diesel | 5 | Experimental | 1918 | 0 | 20000 | 30 | 800000 | 60 | Monitor submarine | 1,650 tons, 1×12" gun | Monitor SS | 12" gun submarine | 3 boats, monitor submarine |
| 2816 | British | O-class | SS | Fleet Diesel | 6 | Interwar | 1926 | 0 | 19000 | 36 | 600000 | 60 | Overseas patrol | 1,475 tons, long range | Overseas Patrol SS | Long-range patrol | 9 boats |
| 2817 | British | P-class | SS | Fleet Diesel | 6 | Interwar | 1930 | 0 | 20000 | 36 | 650000 | 60 | Patrol submarine | 1,475 tons, patrol | Patrol SS | Standard patrol | 6 boats |
| 2818 | British | R-class | SS | Fleet Diesel | 6 | Interwar | 1932 | 0 | 21000 | 36 | 700000 | 60 | Improved patrol | 1,475 tons, improved | Improved Patrol SS | Enhanced systems | 10 boats |
| 2819 | British | S-class | SS | Fleet Diesel | 7 | Pre-WWII | 1932 | 0 | 24000 | 42 | 750000 | 18 | Medium fleet SS | 715 tons, standard | Medium Fleet SS | RN Reliability: +10% uptime | 62 boats, medium fleet |
| 2820 | British | T-class | SS | WWII Main | 7 | WWII | 1938 | 0 | 28000 | 42 | 900000 | 24 | Most successful British SS | 1,290 tons, 53 boats | WWII Workhorse SS | Silent Service: +15% stealth | 53 boats, most successful |
| 2821 | British | U-class | SS | WWII Main | 7 | WWII | 1940 | 0 | 26000 | 42 | 850000 | 24 | Fleet submarine | 540 tons, coastal/fleet | Fleet SS | Coastal and fleet ops | 49 boats |
| 2822 | British | V-class | SS | WWII Main | 7 | WWII | 1943 | 0 | 27000 | 42 | 900000 | 24 | Improved U-class | 545 tons, improved | Improved Fleet SS | Enhanced U-class | 22 boats |
| 2823 | British | A-class (1945) | SS | WWII Main | 8 | Post-War | 1947 | 0 | 30000 | 48 | 1200000 | 36 | Post-war diesel | 1,385 tons, modern | Post-War Diesel SS | Modern diesel design | 16 boats |
| 2824 | British | Porpoise-class | SS | WWII Main | 8 | Post-War | 1958 | 0 | 32000 | 48 | 1500000 | 48 | Transition class | 2,030 tons, pre-nuclear | Transition SS | Last diesel patrol | 8 boats, transition to nuclear |
| 2825 | British | T-class (Streamlined) | SS | Modernization | 7 | Modernized | 1950 | 0 | 8000 | 24 | 0 | 0 | Streamlined conversion | Streamlined hull, snorkel | Streamlined T-class | GUPPY-equivalent | 15 boats converted |
| 2826 | British | A-class (Modernized) | SS | Modernization | 8 | Modernized | 1955 | 0 | 10000 | 30 | 0 | 0 | Cold war upgrade | Snorkel + electronics | Modernized A-class | Extended service life | Selected boats upgraded |
| 2827 | British | Dreadnought SSN | SSN | Nuclear Attack | 8 | Nuclear | 1963 | 0 | 30000 | 54 | 35000000 | 72 | First British nuclear | 3,500 tons, S5W reactor | Nuclear Revolution | First nuclear, unlimited range, UNIQUE | SSN-01, first British nuclear |
| 2828 | British | Valiant-class | SSN | Nuclear Attack | 8 | Nuclear | 1966 | 0 | 32000 | 54 | 40000000 | 72 | Production nuclear | 4,500 tons, PWR1 | Production SSN | RN Reliability: +10% uptime | 2 boats, first production |
| 2829 | British | Churchill-class | SSN | Nuclear Attack | 9 | Nuclear | 1970 | 0 | 35000 | 60 | 45000000 | 78 | Improved SSN | 4,500 tons, improved | Improved SSN | Enhanced systems | 3 boats |
| 2830 | British | Swiftsure-class | SSN | Nuclear Attack | 9 | Nuclear | 1973 | 0 | 40000 | 60 | 55000000 | 84 | Quiet nuclear | 4,500 tons, quiet | Quiet SSN | Silent Service: +15% stealth | 6 boats, quieter design |
| 2831 | British | Trafalgar-class | SSN | Nuclear Attack | 9 | Nuclear | 1983 | 0 | 45000 | 66 | 75000000 | 90 | Modern attack SSN | 5,200 tons, modern | Modern Attack SSN | Tomahawk capability | 7 boats |
| 2832 | British | Astute-class (Batch 1) | SSN | Nuclear Attack | 10 | Modern | 2010 | 0 | 55000 | 78 | 1500000000 | 108 | Advanced SSN | 7,400 tons, advanced | Advanced SSN | PWR2 reactor, advanced systems | 4 boats, Batch 1 |
| 2833 | British | Astute-class (Batch 2) | SSN | Nuclear Attack | 10 | Modern | 2020 | 0 | 52000 | 72 | 1600000000 | 108 | Current production | 7,400 tons, current | Current SSN | Latest technology | 3 boats, Batch 2, current |
| 2834 | British | Resolution-class | SSBN | Ballistic | 9 | Ballistic | 1967 | 0 | 50000 | 72 | 120000000 | 96 | First SSBN | 7,500 tons, Polaris | First SSBN | 16 Polaris missiles | 4 boats, first SSBN |
| 2835 | British | Vanguard-class | SSBN | Ballistic | 10 | Ballistic | 1993 | 0 | 60000 | 84 | 1500000000 | 120 | Trident SSBN | 15,900 tons, Trident | Trident SSBN | 16 Trident II D5 missiles | 4 boats, continuous deterrent |
| 2836 | British | Dreadnought SSBN | SSBN | Ballistic | 10 | Future SSBN | 2030 | 0 | 80000 | 108 | 4000000000 | 144 | Future SSBN | 17,200 tons, future | Future SSBN | 12 Trident II D5 missiles | 4 planned, replacement program |
| 2837 | British | X-craft | SSE | Alternative | 7 | Midget Sub | 1943 | 0 | 12000 | 24 | 100000 | 12 | Midget submarine | 30 tons, 4-man crew | Midget SS | Special operations, UNIQUE | 6 operational, midget submarine |
| 2838 | British | Explorer HTP | SSE | Alternative | 8 | Experimental | 1958 | 0 | 15000 | 36 | 500000 | 42 | Experimental HTP | 780 tons, hydrogen peroxide | Experimental SS | High Test Peroxide, UNIQUE | 2 boats, experimental (failed) |
| 3000 | German | SMS Brandenburg | BB | Starting | 1 | Early Pre-Dreadnought | 1893 | 1 | 0 | 0 | 500000 | 36 | First ocean-going BB | 6×28cm guns, first German BB | Pioneer | First German BB, FREE | FREE starting BB, 4 ships |
| 3001 | German | SMS Kaiser Friedrich III | BB | Starting | 1 | Pre-Dreadnought | 1898 | 1 | 0 | 0 | 800000 | 42 | Hail of fire doctrine | 4×24cm guns, rapid-fire | Hail of Fire | Rapid-fire doctrine, FREE | FREE starting BB, 5 ships |
| 3002 | German | SMS Wittelsbach | BB | Pre-Dreadnought Main | 2 | Pre-Dreadnought | 1902 | 0 | 5000 | 12 | 1000000 | 36 | Improved armor | 4×24cm guns, 11,774 tons | Improved Armor | +10% protection | 5 ships, improved design |
| 3003 | German | SMS Wettin | BB | Pre-Dreadnought Main | 2 | Pre-Dreadnought | 1902 | 0 | 5000 | 12 | 1000000 | 36 | Wittelsbach class | 4×24cm guns, improved | Refined Design | +5% efficiency | Wittelsbach class |
| 3004 | German | SMS Braunschweig | BB | Pre-Dreadnought Main | 3 | Pre-Dreadnought | 1904 | 0 | 8000 | 18 | 1200000 | 42 | More powerful | 4×28cm guns, 13,208 tons | More Powerful | +15% firepower | 5 ships, 28cm guns |
| 3005 | German | SMS Elsass | BB | Pre-Dreadnought Main | 3 | Pre-Dreadnought | 1904 | 0 | 8000 | 18 | 1200000 | 42 | Braunschweig class | Improved armor, 4×28cm | Better Protection | +10% armor | Braunschweig class |
| 3006 | German | SMS Deutschland (1906) | BB | Pre-Dreadnought Main | 4 | Pre-Dreadnought | 1906 | 0 | 12000 | 24 | 1500000 | 48 | Last pre-dreadnought | 4×28cm guns, thick armor | Last Pre-Dreadnought | Pinnacle design | 5 ships, last pre-dreadnought |
| 3007 | German | SMS Hannover | BB | Pre-Dreadnought Main | 4 | Pre-Dreadnought | 1907 | 0 | 12000 | 24 | 1500000 | 48 | Deutschland class | 5 ships built | Deutschland Class | Mass production | Deutschland class |
| 3008 | German | SMS Pommern | BB | Pre-Dreadnought Main | 4 | Pre-Dreadnought | 1907 | 0 | 12000 | 24 | 1500000 | 48 | Deutschland class | Sunk at Jutland 1916 | Jutland Veteran | Combat experience | Sunk at Jutland |
| 3009 | German | SMS Schleswig-Holstein | BB | Pre-Dreadnought Main | 4 | Pre-Dreadnought | 1908 | 0 | 12000 | 24 | 1600000 | 48 | Deutschland class | Fired first shots WWII | First Shots WWII | +15% prestige | Fired first shots WWII at Danzig |
| 3010 | German | SMS Schlesien | BB | Pre-Dreadnought Main | 4 | Pre-Dreadnought | 1908 | 0 | 12000 | 24 | 1600000 | 48 | Deutschland class | Last survivor until 1945 | Last Survivor | +20% reliability | Survived to 1945 |
| 3011 | German | SMS Nassau | BB | Early Dreadnought | 5 | First Dreadnought | 1909 | 0 | 18000 | 30 | 3000000 | 36 | First German dreadnought | 12×28cm hexagonal layout | Dreadnought Revolution | Hexagonal layout, UNIQUE | First German dreadnought, 4 ships |
| 3012 | German | SMS Westfalen | BB | Early Dreadnought | 5 | First Dreadnought | 1909 | 0 | 18000 | 30 | 3000000 | 36 | Nassau class | 4 ships, Jutland veteran | Nassau Class | +10% broadside | Nassau class, Jutland veteran |
| 3013 | German | SMS Helgoland | BB | Early Dreadnought | 6 | Improved Dreadnought | 1911 | 0 | 25000 | 36 | 4000000 | 42 | Improved dreadnought | 12×30.5cm guns, improved | 30.5cm Guns | +20% firepower | 4 ships, improved guns |
| 3014 | German | SMS Ostfriesland | BB | Early Dreadnought | 6 | Improved Dreadnought | 1911 | 0 | 25000 | 36 | 4000000 | 42 | Helgoland class | Billy Mitchell tests 1921 | Billy Mitchell | Historical significance | Sunk in bombing tests 1921 |
| 3015 | German | SMS Kaiser | BB | Super-Dreadnought | 7 | Super-Dreadnought | 1912 | 0 | 32000 | 42 | 5000000 | 48 | First turbines | 10×30.5cm superfiring turrets | Turbines | +15% speed, superfiring | 5 ships, first turbines |
| 3016 | German | SMS Friedrich der Große | BB | Super-Dreadnought | 7 | Super-Dreadnought | 1912 | 0 | 32000 | 42 | 5000000 | 48 | Kaiser class | Jutland flagship, Scapa Flow | Jutland Flagship | +20% command | High Seas Fleet flagship |
| 3017 | German | SMS König | BB | Super-Dreadnought | 7 | Super-Dreadnought | 1913 | 0 | 35000 | 48 | 6000000 | 48 | Improved broadside | 10×30.5cm guns | Improved Broadside | +15% firepower | 4 ships, better fire arcs |
| 3018 | German | SMS Großer Kurfürst | BB | Super-Dreadnought | 7 | Super-Dreadnought | 1914 | 0 | 35000 | 48 | 6000000 | 48 | König class | Jutland veteran | König Class | Jutland combat | König class, Jutland |
| 3019 | German | SMS Bayern | BB | Super-Dreadnought | 8 | Ultimate WWI | 1916 | 0 | 45000 | 54 | 8000000 | 54 | Best WWI German BB | 8×38cm guns, most powerful | 38cm Guns | +30% firepower, UNIQUE | Ultimate WWI German BB |
| 3020 | German | Deutschland (Panzerschiff) | PS | Panzerschiffe | 7 | Pocket Battleship | 1931 | 0 | 40000 | 54 | 12000000 | 60 | Diesel pocket BB | 11" guns, commerce raider | Diesel Pioneer | +25% range, Treaty loophole | Diesel, Treaty loophole |
| 3021 | German | Admiral Scheer | PS | Panzerschiffe | 7 | Pocket Battleship | 1934 | 0 | 40000 | 54 | 12000000 | 60 | Most successful raider | Sank 17 merchant ships | Best Raider | +30% commerce raiding | Most successful raider |
| 3022 | German | Admiral Graf Spee | PS | Panzerschiffe | 7 | Pocket Battleship | 1936 | 0 | 40000 | 54 | 12000000 | 60 | Panzerschiff | Scuttled River Plate 1939 | River Plate | Combat experience | Battle of River Plate |
| 3023 | German | Scharnhorst | BB | Fast Battleship | 9 | Fast Battleship | 1939 | 0 | 55000 | 66 | 30000000 | 66 | Fast battleship | 32 kts, 9×28cm guns, Channel Dash | Fast BB | 32 kts, +20% speed | Channel Dash, sank Glorious |
| 3024 | German | Gneisenau | BB | Fast Battleship | 9 | Fast Battleship | 1939 | 0 | 55000 | 66 | 30000000 | 66 | Sister to Scharnhorst | Fast commerce raider | Commerce Raider | +25% raiding | Sister to Scharnhorst |
| 3025 | German | Bismarck | BB | Ultimate | 10 | Ultimate BB | 1940 | 0 | 75000 | 90 | 50000000 | 72 | Largest German BB | Sank HMS Hood, 8×38cm guns | Hood Killer | Sank HMS Hood, +40% prestige, UNIQUE | Largest German BB, legendary |
| 3026 | German | Tirpitz | BB | Ultimate | 10 | Ultimate BB | 1941 | 0 | 75000 | 90 | 50000000 | 72 | Fleet in being | Norway, Tallboy bombs 1944 | Fleet in Being | +30% deterrence | Norway operations, fleet in being |
| 3027 | German | SMS Bayern (Modernized) | BB | Modernization | 8 | Modernization | 1920 | 0 | 40000 | 54 | 4000000 | 18 | Postwar refit | Improved fire control | Postwar Refit | Improved systems | Postwar improvements |
| 3028 | German | Deutschland (Lützow) | PS | Modernization | 8 | Modernization | 1940 | 0 | 45000 | 60 | 6000000 | 24 | 1940 refit | Renamed to Lützow | Renamed Lützow | 1940 refit | Renamed in 1940 |
| 3029 | German | Scharnhorst (38cm Refit) | BB | Modernization | 9 | Modernization | 1942 | 0 | 55000 | 66 | 15000000 | 36 | Planned 38cm upgrade | Never completed | 38cm Upgrade | Planned improvement | Planned gun upgrade |
| 3030 | German | H-39 | BB | H-Class Small | 9 | H-Class Plan Z | 1939 | 0 | 70000 | 84 | 60000000 | 84 | Plan Z H-class | 56,444 tons, 8×40.6cm guns | H-39 Plan Z | 40.6cm guns, laid down | Laid down 1939, cancelled |
| 3031 | German | H-41 | BB | H-Class Small | 9 | H-Class Improved | 1941 | 0 | 75000 | 90 | 70000000 | 90 | Improved H-class | 68,800 tons, 8×42cm guns | H-41 | 42cm guns, improved armor | Design finalized 1941 |
| 3032 | German | H-42 | BB | H-Class Medium | 10 | H-Class Study | 1942 | 0 | 80000 | 96 | 90000000 | 96 | Study project | 90,000 tons, 8×48cm guns | H-42 | 48cm guns, 90,000 tons | Study project only |
| 3033 | German | H-43 | BB | H-Class Medium | 10 | H-Class Study | 1943 | 0 | 85000 | 102 | 110000000 | 102 | Theoretical design | 111,000 tons, 8×50.8cm guns | H-43 | 50.8cm guns, 111,000 tons | Theoretical study |
| 3034 | German | H-44 | BB | H-Class Ultimate | 10 | H-Class Ultimate | 1944 | 0 | 90000 | 108 | 130000000 | 108 | Largest BB design | 131,000 tons, 8×50.8cm guns | H-44 | 131,000 tons, largest design, UNIQUE | Largest battleship ever designed |
| 3035 | German | H-45 Monster | BB | H-Class Ultimate | 10 | H-Class Beyond | 1944 | 0 | 95000 | 120 | 150000000 | 120 | Theoretical monster | 150,000+ tons, extreme concept | H-45 Monster | 150,000+ tons, theoretical | Beyond H-44, extreme concept |
| 3036 | German | SMS Derfflinger | BC | Alternative | 6 | WWI Battlecruiser | 1914 | 0 | 28000 | 42 | 5500000 | 48 | Fast battlecruiser | 8×30.5cm guns, Jutland | Fast BC | +25% speed, Jutland survivor | WWI battlecruiser, Jutland |
| 3037 | German | SMS Hindenburg | BC | Alternative | 7 | WWI Battlecruiser | 1917 | 0 | 35000 | 48 | 7000000 | 54 | Last WWI BC | 8×30.5cm guns, last German BC | Last WWI BC | Final German BC | Last WWI German BC |
| 3038 | German | O-Class | BC | Alternative | 9 | Cancelled BC | 1939 | 0 | 60000 | 72 | 50000000 | 72 | Plan Z BC | 6×38cm guns, fast raider | O-Class | Plan Z BC, fast raider | Cancelled BC program |
| 3039 | German | P-Class | BC | Alternative | 9 | Cancelled BC | 1940 | 0 | 60000 | 72 | 50000000 | 72 | Improved O-class | Diesel engines, 6×38cm | P-Class | Diesel BC, improved | Enhanced O-class |
| 3600 | German | SMS Bussard | CL | Starting | 1 | Unprotected Cruiser | 1890 | 1 | 0 | 0 | 300000 | 24 | Unprotected cruiser | 6×10.5cm guns, early design | Pioneer | Early cruiser operations, FREE | FREE starting CL, 6 ships |
| 3601 | German | SMS Gazelle | CL | Starting | 1 | Protected Cruiser | 1901 | 1 | 0 | 0 | 500000 | 30 | First modern CL | 10×10.5cm guns, modern design | Modern Light | First modern CL, UNIQUE, FREE | FREE starting CL, 10 ships |
| 3602 | German | SMS Victoria Louise | CL | Protected Cruiser | 2 | Protected Cruiser | 1899 | 0 | 5000 | 12 | 800000 | 36 | Last protected | 2×21cm + 8×15cm guns | Protected | Armored deck protection | 5 ships, last protected |
| 3603 | German | SMS Kaiserin Augusta | CL | Protected Cruiser | 2 | Protected Cruiser | 1892 | 0 | 5000 | 12 | 900000 | 36 | Large protected | 12×15cm guns, large | Large Protected | +15% displacement | Large protected cruiser |
| 3604 | German | SMS Fürst Bismarck | CA | Armored Cruiser | 3 | Armored Cruiser | 1900 | 0 | 8000 | 18 | 1200000 | 42 | First armored | 4×24cm + 12×15cm guns | First Armored | +20% armor | First armored cruiser |
| 3605 | German | SMS Prinz Heinrich | CA | Armored Cruiser | 3 | Armored Cruiser | 1902 | 0 | 8000 | 18 | 1300000 | 42 | Improved armored | 2×24cm + 10×15cm guns | Improved Armored | +10% firepower | Improved armored design |
| 3606 | German | SMS Prinz Adalbert | CA | Armored Cruiser | 4 | Armored Cruiser | 1904 | 0 | 12000 | 24 | 1500000 | 48 | Enhanced armor | 4×21cm guns | Enhanced Armor | +15% protection | 2 ships, enhanced armor |
| 3607 | German | SMS Roon | CA | Armored Cruiser | 4 | Armored Cruiser | 1905 | 0 | 12000 | 24 | 1600000 | 48 | Improved design | 4×21cm guns | Improved Design | +10% efficiency | 2 ships, improved |
| 3608 | German | SMS Scharnhorst (CA) | CA | Armored Cruiser | 5 | Armored Cruiser | 1907 | 0 | 15000 | 30 | 2000000 | 48 | Famous Coronel | 8×21cm guns, Coronel/Falklands | Coronel Victory | +25% prestige | Famous Scharnhorst class, 2 ships |
| 3609 | German | SMS Blücher (CA) | CA | Armored Cruiser | 5 | Armored Cruiser | 1909 | 0 | 18000 | 36 | 2500000 | 54 | Transitional design | 12×21cm guns, Dogger Bank | Transitional | Bridge to heavy cruisers | Sunk Dogger Bank 1915 |
| 3610 | German | SMS Bremen | CL | Light WWI Early | 2 | Light Cruiser | 1904 | 0 | 6000 | 12 | 700000 | 30 | First true light | 10×10.5cm guns | True Light | +15% speed | 7 ships, first true CL |
| 3611 | German | SMS Dresden | CL | Light WWI Early | 3 | Light Cruiser | 1908 | 0 | 9000 | 18 | 900000 | 36 | Improved light | 10×10.5cm guns, commerce raider | Commerce Raider | +20% raiding | 2 ships, Dresden operations |
| 3612 | German | SMS Königsberg (1907) | CL | Light WWI Early | 3 | Light Cruiser | 1907 | 0 | 9000 | 18 | 950000 | 36 | Enhanced design | 10×10.5cm guns | Enhanced Light | +10% capability | 4 ships, enhanced |
| 3613 | German | SMS Kolberg | CL | Light WWI Standard | 4 | Light Cruiser | 1910 | 0 | 12000 | 24 | 1100000 | 42 | Improved guns | 12×10.5cm L/45 guns | L/45 Guns | Improved accuracy | 4 ships, improved guns |
| 3614 | German | SMS Magdeburg | CL | Light WWI Standard | 4 | Light Cruiser | 1912 | 0 | 12000 | 24 | 1200000 | 42 | First belt armor | 12×10.5cm guns, waterline belt | Belt Armor | +20% protection, UNIQUE | 4 ships, first waterline belt |
| 3615 | German | SMS Karlsruhe | CL | Light WWI Standard | 5 | Light Cruiser | 1913 | 0 | 15000 | 30 | 1400000 | 48 | Fast light cruiser | 12×10.5cm guns, 27.5 kts | Fast CL | 27.5 kts | 2 ships, high-speed |
| 3616 | German | SMS Pillau | CL | Light WWI Advanced | 6 | Light Cruiser | 1914 | 0 | 20000 | 36 | 2000000 | 48 | First 15cm guns | 8×15cm SK L/45, revolution | 15cm Standard | +30% firepower, revolution | 2 ships, 15cm revolution |
| 3617 | German | SMS Graudenz | CL | Light WWI Advanced | 6 | Light Cruiser | 1914 | 0 | 20000 | 36 | 2100000 | 48 | 15cm armed | 12×15cm guns | Heavy Armed | 12×15cm guns | 2 ships, heavy armed |
| 3618 | German | SMS Wiesbaden | CL | Light WWI Advanced | 6 | Light Cruiser | 1915 | 0 | 22000 | 36 | 2200000 | 48 | Fast 15cm cruiser | 8×15cm guns, 27.5 kts | Fast 15cm | Speed + firepower | 2 ships, fast |
| 3619 | German | SMS Königsberg II | CL | Light WWI Advanced | 7 | Light Cruiser | 1916 | 0 | 25000 | 42 | 2500000 | 54 | Ultimate WWI light | 8×15cm guns, best WWI | Ultimate WWI | Best WWI CL | 4 ships, ultimate WWI |
| 3620 | German | SMS Emden (1925) | CL | Interwar Light | 7 | Light Cruiser | 1925 | 0 | 28000 | 48 | 4000000 | 54 | First post-Versailles | 8×15cm guns, unique design | Post-Versailles | +20% prestige | Unique, first post-treaty |
| 3621 | German | Königsberg (1929) | CL | Interwar Light | 8 | Light Cruiser | 1929 | 0 | 35000 | 54 | 6000000 | 60 | Modern light cruiser | 9×15cm guns, 32 kts | Modern CL | 32 kts, 9×15cm | 3 ships, modern |
| 3622 | German | Leipzig | CL | Interwar Light | 8 | Light Cruiser | 1931 | 0 | 35000 | 54 | 6500000 | 60 | Improved Königsberg | 9×15cm guns | Improved Modern | +10% capability | 2 ships, improved |
| 3623 | German | Nürnberg | CL | Interwar Light | 8 | Light Cruiser | 1935 | 0 | 35000 | 54 | 7000000 | 60 | Enhanced Leipzig | 9×15cm guns, last CL | Last CL | Final light cruiser | Last German light cruiser |
| 3624 | German | Admiral Hipper | CA | Heavy Cruiser | 9 | Heavy Cruiser | 1939 | 0 | 50000 | 66 | 20000000 | 66 | First heavy cruiser | 8×20.3cm guns | Heavy Cruiser | 8×20.3cm guns | Lead ship, 5 planned |
| 3625 | German | Blücher (1939) | CA | Heavy Cruiser | 9 | Heavy Cruiser | 1939 | 0 | 50000 | 66 | 20000000 | 66 | Admiral Hipper class | Sunk Norway 1940 | Norway Operations | Combat experience | Sunk in Norway 1940 |
| 3626 | German | Prinz Eugen | CA | Heavy Cruiser | 9 | Heavy Cruiser | 1940 | 0 | 50000 | 66 | 22000000 | 66 | Most famous | Bismarck escort, survived war | Bismarck Escort | +30% prestige, survived war | Only major German surface ship to survive |
| 3627 | German | Seydlitz | CA | Heavy Cruiser | 9 | Heavy Cruiser | 1939 | 0 | 50000 | 66 | 20000000 | 66 | Incomplete | Carrier conversion planned | Conversion Plan | Carrier conversion | Incomplete, conversion planned |
| 3628 | German | Lützow (CA) | CA | Heavy Cruiser | 9 | Heavy Cruiser | 1939 | 0 | 50000 | 66 | 20000000 | 66 | Sold to USSR | Became Petropavlovsk | Soviet Sale | Diplomatic significance | Sold to USSR incomplete |
| 3629 | German | SMS Königsberg II (Mod) | CL | Modernization | 7 | Modernization | 1920 | 0 | 20000 | 42 | 1000000 | 18 | Postwar refit | Improved systems | Postwar Refit | Improved systems | WWI cruiser modernization |
| 3630 | German | Emden (1940 Refit) | CL | Modernization | 8 | Modernization | 1940 | 0 | 30000 | 54 | 2000000 | 24 | WWII refit | Improved AA | WWII Refit | Enhanced AA | Wartime improvements |
| 3631 | German | Prinz Eugen (1945 Refit) | CA | Modernization | 9 | Modernization | 1945 | 0 | 45000 | 66 | 5000000 | 30 | Late-war refit | Enhanced AA | Late-War Refit | Maximum AA | 1945 configuration |
| 3632 | German | P-Class Cruiser | CA | Paper Ship | 9 | Cancelled CA | 1940 | 0 | 55000 | 72 | 25000000 | 72 | Plan Z heavy | 6×20.3cm guns | P-Class | Plan Z CA, -10% reliability | Cancelled heavy cruiser |
| 3633 | German | M-Class Cruiser | CL | Paper Ship | 9 | Cancelled CL | 1940 | 0 | 50000 | 66 | 15000000 | 60 | Improved light | 8×15cm guns | M-Class | Improved CL, -10% reliability | Cancelled light cruiser |
| 3634 | German | Improved Hipper | CA | Paper Ship | 10 | Paper Ship | 1942 | 0 | 60000 | 78 | 30000000 | 78 | Enhanced Hipper | Enhanced design | Improved Hipper | Enhanced design, -15% reliability | Enhanced Hipper design |
| 3635 | German | Super Hipper | CA | Paper Ship | 10 | Paper Ship | 1943 | 0 | 65000 | 84 | 35000000 | 84 | Enlarged heavy | 9×20.3cm guns | Super Hipper | 9×20.3cm guns, -15% reliability | Ultimate heavy cruiser |
| 3636 | German | Spähkreuzer | CL | Paper Ship | 9 | Scout Cruiser | 1941 | 0 | 45000 | 66 | 12000000 | 60 | Reconnaissance | Scout cruiser concept | Scout | Reconnaissance operations | Scout cruiser concept |
| 3637 | German | AA Cruiser Concept | CL | Paper Ship | 9 | AA Cruiser | 1942 | 0 | 48000 | 66 | 18000000 | 66 | Dedicated AA | AA cruiser design | AA Specialist | Dedicated AA, -10% reliability | AA cruiser design |
| 3638 | German | Torpedo Cruiser | CL | Paper Ship | 8 | Torpedo Cruiser | 1940 | 0 | 40000 | 60 | 10000000 | 54 | Torpedo-armed | Torpedo cruiser concept | Torpedo Armed | +40% torpedo capability | Torpedo cruiser concept |
| 3639 | German | Future CL Concept | CL | Paper Ship | 10 | Future Design | 1950 | 0 | 70000 | 90 | 40000000 | 90 | Post-war concept | Future cruiser | Future Design | Post-war concept, -10% reliability | Future cruiser technology |
| 3700 | German | SMS S90 | DD | Starting | 1 | Torpedo Boat | 1898 | 1 | 0 | 24 | 400000 | 50 | Early torpedo boat | 388 tons, 3×50mm, 3×45cm TT | Pioneer Torpedo Boat | First modern German torpedo boat, FREE | FREE starting DD, 12 ships |
| 3701 | German | SMS G108 | DD | Starting | 1 | Torpedo Boat | 1900 | 1 | 0 | 30 | 450000 | 50 | Improved torpedo boat | 433 tons, 29 kts, turbines | Improved Speed | 29 kts, early turbine, FREE | FREE starting DD, 6 ships |
| 3702 | German | SMS S114 | DD | Early Torpedo Boats | 2 | Torpedo Boat | 1902 | 0 | 5000 | 30 | 500000 | 52 | Coastal torpedo boat | Refined design, 12 ships | Coastal | Early torpedo operations | 12 ships built |
| 3703 | German | SMS S138 | DD | Early Torpedo Boats | 3 | Large Torpedo Boat | 1906 | 0 | 8000 | 36 | 600000 | 58 | Large torpedo boat | 1906 Type, improved size | Large Type | 1906 program, improved | 1906 Type program |
| 3704 | German | SMS V150 | DD | Early Torpedo Boats | 3 | Large Torpedo Boat | 1907 | 0 | 8000 | 36 | 650000 | 58 | Advanced torpedo boat | Turbine-powered, enhanced | Advanced | Turbine technology | Enhanced performance |
| 3705 | German | SMS V1 | DD | WWI Large Torpedo Boats | 4 | Large Torpedo Boat | 1911 | 0 | 12000 | 42 | 800000 | 74 | Large torpedo boat | 573 tons, 2×8.8cm guns | 1911 Program | 1911 Program destroyer | 1911 Program, 74 crew |
| 3706 | German | SMS G7 | DD | WWI Large Torpedo Boats | 4 | Large Torpedo Boat | 1911 | 0 | 12000 | 42 | 850000 | 74 | Germaniawerft design | 573 tons, similar to V1 | Germaniawerft | Germaniawerft built | 1911 Program, G-class |
| 3707 | German | SMS S13 | DD | WWI Large Torpedo Boats | 4 | Large Torpedo Boat | 1911 | 0 | 12000 | 42 | 750000 | 70 | Compact design | Smaller, more maneuverable | Compact | More maneuverable design | 1911 Program, compact |
| 3708 | German | SMS S31 | DD | WWI Large Torpedo Boats | 4 | Large Torpedo Boat | 1912 | 0 | 15000 | 42 | 900000 | 72 | Improved S-class | 1912 refined design | Refined | 1912 improvement | 1912 design evolution |
| 3709 | German | SMS V25 | DD | WWI Main Line | 5 | Type 1913 | 1913 | 0 | 18000 | 48 | 1000000 | 80 | Largest WWI class | 71 ships! 3×10.5cm guns | Mass Production | 71 ships built, +30% production, UNIQUE | Largest German DD class ever, 71 ships |
| 3710 | German | SMS G37 | DD | WWI Main Line | 5 | Type 1913 | 1914 | 0 | 18000 | 48 | 1050000 | 80 | WWI main line | 6×50cm torpedoes | WWI Standard | Type 1913 standard | Type 1913 variant |
| 3711 | German | SMS V43 | DD | WWI Main Line | 5 | Type 1913 | 1914 | 0 | 18000 | 48 | 1100000 | 80 | V25 variant | Type 1913 improved | Type 1913 | V25-class variant | Type 1913 improved |
| 3712 | German | SMS B97 | DD | WWI Advanced | 6 | Type 1914 | 1914 | 0 | 22000 | 54 | 1200000 | 85 | Advanced WWI | 1914 Type design | 1914 Type | 1914 program advanced | 1914 Type program |
| 3713 | German | SMS G101 | DD | WWI Advanced | 6 | Type 1914 | 1915 | 0 | 22000 | 54 | 1250000 | 85 | Late war design | 1914 Type improved | Late War | 1914 Type improved | 1915 late war design |
| 3714 | German | SMS V105 | DD | WWI Advanced | 6 | Type 1914 | 1915 | 0 | 22000 | 54 | 1300000 | 85 | Ultimate WWI | 1914 Type ultimate | Ultimate WWI | Ultimate WWI design | 1914 Type ultimate |
| 3715 | German | Möwe | DD | Interwar Type 23/24 | 3 | Type 23 | 1926 | 0 | 10000 | 36 | 1500000 | 129 | First post-Versailles | 923 tons, bird name | Post-Versailles | First post-treaty DD, +20% prestige | Type 23, 6 bird ships |
| 3716 | German | Greif | DD | Interwar Type 23/24 | 3 | Type 23 | 1927 | 0 | 10000 | 36 | 1550000 | 129 | Type 23 bird | Treaty restrictions, 923 tons | Treaty Bird | Treaty restrictions | Type 23, bird names |
| 3717 | German | Wolf | DD | Interwar Type 23/24 | 4 | Type 24 | 1928 | 0 | 12000 | 42 | 1600000 | 129 | Type 24 predator | 932 tons improved | Type 24 | Improved Type 23 | Type 24, 6 predator ships |
| 3718 | German | Jaguar | DD | Interwar Type 23/24 | 4 | Type 24 | 1929 | 0 | 12000 | 42 | 1650000 | 129 | Type 24 cat | Last treaty boat | Last Treaty | Last interwar design | Type 24, last treaty |
| 3719 | German | Z1 Leberecht Maass | DD | Type 1934/1934A | 6 | Type 1934 | 1937 | 0 | 25000 | 60 | 4000000 | 315 | First modern DD | 3165 tons, 5×127mm guns | Modern Revolution | First post-Versailles DD, +25% capability | Type 1934, 4 ships, Z1-Z4 |
| 3720 | German | Z3 Max Schultz | DD | Type 1934/1934A | 6 | Type 1934 | 1937 | 0 | 25000 | 60 | 4200000 | 315 | Type 1934 | 5×127mm, 38.4 kts | Type 1934 | First modern standard | Type 1934, Z3 |
| 3721 | German | Z5 Paul Jacobi | DD | Type 1934/1934A | 7 | Type 1934A | 1938 | 0 | 30000 | 66 | 4500000 | 321 | Type 1934A | Improved Type 1934, 12 ships | Type 1934A | Z5-Z16 improved | Type 1934A, 12 ships, Z5-Z16 |
| 3722 | German | Z17 Diether von Roeder | DD | Type 1936/1936A | 7 | Type 1936 | 1938 | 0 | 35000 | 66 | 5000000 | 321 | Type 1936 | 1811 tons, 40 kts | Type 1936 | 40 kts speed, improved | Type 1936, 6 ships, Z17-Z22 |
| 3723 | German | Z20 Karl Galster | DD | Type 1936/1936A | 7 | Type 1936 | 1939 | 0 | 35000 | 66 | 5200000 | 321 | Type 1936 improved | Enhanced seakeeping | Enhanced | Improved seakeeping | Type 1936, Z20 |
| 3724 | German | Z23 | DD | Type 1936/1936A | 8 | Type 1936A Narvik | 1940 | 0 | 40000 | 72 | 6000000 | 321 | Revolutionary Narvik | 4×150mm guns, unprecedented! | Narvik Revolution | 150mm guns on DD, +40% firepower, UNIQUE | Type 1936A Narvik, 8 ships, Z23-Z30 |
| 3725 | German | Z25 | DD | Type 1936/1936A | 8 | Type 1936A Narvik | 1940 | 0 | 40000 | 72 | 6200000 | 321 | Narvik class | 150mm gun standard | Narvik Standard | 150mm mastery, +35% firepower | Type 1936A Narvik, Z25 |
| 3726 | German | Z28 | DD | Type 1936/1936A | 8 | Type 1936A(Mob) | 1941 | 0 | 40000 | 72 | 6500000 | 321 | Late Narvik | Mobilization variant | Narvik Mob | Type 1936A(Mob) variant | Type 1936A(Mob), 7 ships |
| 3727 | German | Z35 | DD | Type 1936B/C | 9 | Type 1936B | 1943 | 0 | 50000 | 78 | 7000000 | 321 | Type 1936B | Return to 127mm guns | Balanced Design | 127mm return, +30% AA | Type 1936B, 6 completed, Z35-Z45 |
| 3728 | German | Z40 | DD | Type 1936B/C | 9 | Type 1936B | 1944 | 0 | 50000 | 78 | 7500000 | 321 | Late Type 1936B | Improved AA capability | Enhanced AA | Late war AA improvements | Type 1936B, Z40 |
| 3729 | German | Z46 | DD | Type 1936B/C | 9 | Type 1936C | 1944 | 0 | 55000 | 78 | 8000000 | 321 | Type 1936C | 128mm DP guns planned | Type 1936C | 128mm dual-purpose | Type 1936C, never completed, Z46-Z50 |
| 3730 | German | Z50 | DD | Type 1936B/C | 9 | Type 1936C | 1945 | 0 | 55000 | 78 | 8500000 | 321 | Last Type 1936C | Never completed | Last 1936C | Never completed, -15% reliability | Type 1936C, Z50, never finished |
| 3731 | German | V25 Modernization | DD | Modernization | 7 | Type 1913 Refit | 1917 | 0 | 28000 | 54 | 1500000 | 85 | WWI refit | 10.5cm guns upgrade | WWI Refit | 10.5cm upgrade from 8.8cm | V25-class modernization |
| 3732 | German | Type 1934 Refit | DD | Modernization | 8 | Type 1934 Upgrade | 1942 | 0 | 35000 | 66 | 5000000 | 321 | WWII modernization | Enhanced AA armament | WWII Upgrade | AA improvements, radar | Type 1934 WWII refit |
| 3733 | German | Type 1936A Refit | DD | Modernization | 9 | Narvik Upgrade | 1943 | 0 | 40000 | 72 | 6500000 | 321 | Narvik upgrade | AA and radar improvements | Narvik Upgrade | Late war AA, radar | Narvik-class modernization |
| 3734 | German | Z51 Diesel | DD | Paper Ship | 10 | Type 1942 | 1944 | 0 | 70000 | 84 | 10000000 | 280 | Experimental diesel | Diesel engines for range | Diesel Innovation | Diesel engines, +30% range, experimental | Type 1942, never completed |
| 3735 | German | Type 1944 | DD | Paper Ship | 10 | Type 1944 | 1945 | 0 | 80000 | 90 | 12000000 | 320 | Most advanced | 6×128mm DP guns | Ultimate WWII | 128mm DP, most advanced, -10% reliability | Most advanced WWII design, never built |
| 3736 | German | Type 1945 | DD | Paper Ship | 10 | Type 1945 | 1946 | 0 | 90000 | 96 | 15000000 | 320 | Ultimate paper | Advanced post-war design | Type 1945 | Ultimate paper, -15% reliability | Never built, post-war concept |
| 3737 | German | Post-War Destroyer | DD | Paper Ship | 10 | Post-War | 1950 | 0 | 100000 | 108 | 20000000 | 350 | Future concept | Modern systems | Future Design | Post-war concept, -10% reliability | Theoretical post-war DD |
| 3738 | German | Future DD Concept | DD | Paper Ship | 10 | Future Design | 1955 | 0 | 120000 | 120 | 30000000 | 400 | Advanced design | Guided missiles | Advanced Future | Guided missiles, future tech | Future destroyer technology |
| 3800 | German | U-1 | SS | Starting | 1 | U-boat | 1906 | 1 | 0 | 36 | 500000 | 28 | First German U-boat | Gasoline engine, experimental | Submarine Pioneer | First German U-boat, world's first practical military submarine, FREE | FREE starting SS, world pioneer |
| 3801 | German | U-9 | SS | Starting | 1 | U-boat | 1910 | 1 | 0 | 36 | 550000 | 29 | Early diesel U-boat | Famous triple kill, 1914 | Triple Kill | Sank 3 cruisers in 1 hour, +40% torpedo, FREE | FREE starting SS, triple kill 1914 |
| 3802 | German | U-31 | SS | WWI Ocean-Going | 3 | U-boat | 1914 | 0 | 8000 | 42 | 700000 | 35 | WWI ocean-going | Diesel-powered, Germaniawerft | WWI Ocean | Germaniawerft diesel design | 11 boats built |
| 3803 | German | U-81 | SS | WWI Ocean-Going | 4 | U-boat | 1916 | 0 | 12000 | 48 | 850000 | 36 | Mid-war ocean-going | Enhanced endurance | Mid-War | Enhanced ocean capability | Mid-war improved |
| 3804 | German | U-87 | SS | WWI Ocean-Going | 5 | U-boat | 1916 | 0 | 15000 | 54 | 950000 | 37 | Advanced ocean-going | Improved reliability | Advanced | WWI advanced design | Reliability improved |
| 3805 | German | U-93 | SS | WWI Ocean-Going | 5 | U-boat | 1917 | 0 | 18000 | 54 | 1100000 | 39 | Late WWI ocean | 24 boats, 16 torpedoes, 9,000 nm | Ocean Hunter | 9,000 nm range, 16 torpedoes, +25% endurance | 24 boats, ultimate WWI ocean |
| 3806 | German | UB-I | SS | WWI Coastal | 2 | Coastal U-boat | 1915 | 0 | 5000 | 30 | 400000 | 14 | Small coastal | Early coastal submarine | Coastal | Early coastal operations | Small coastal type |
| 3807 | German | UB-II | SS | WWI Coastal | 3 | Coastal U-boat | 1915 | 0 | 8000 | 36 | 500000 | 23 | Improved coastal | 30 boats, doubled size, 270 tons | Improved Coastal | Doubled size, improved | 30 boats built |
| 3808 | German | UB-III | SS | WWI Coastal | 5 | Coastal U-boat | 1917 | 0 | 18000 | 48 | 800000 | 34 | Advanced coastal | 96 boats, 10 torpedoes | Coastal Master | 96 boats built, +30% coastal operations | 96 boats, advanced coastal |
| 3809 | German | UC-I | SS | WWI Minelaying | 2 | Minelayer | 1915 | 0 | 5000 | 30 | 450000 | 18 | Early minelayer | First minelaying U-boat | Minelayer | First minelaying design | Early minelayer |
| 3810 | German | UC-II | SS | WWI Minelaying | 4 | Minelayer | 1916 | 0 | 12000 | 42 | 650000 | 26 | Advanced minelayer | 64 boats, mine+torpedo combination | Mine+Torpedo | Ideal combination, +35% versatility, UNIQUE | 64 boats, ideal combination |
| 3811 | German | UC-III | SS | WWI Minelaying | 5 | Minelayer | 1918 | 0 | 18000 | 48 | 900000 | 32 | Ultimate WWI minelayer | Late war advanced design | Ultimate Minelayer | Late war ultimate | Late war advanced |
| 3812 | German | Type IA | SS | Interwar Types | 4 | U-boat | 1936 | 0 | 15000 | 48 | 2000000 | 43 | First post-Versailles | 2 boats, experimental | Post-Versailles | First post-treaty ocean-going | 2 boats, experimental |
| 3813 | German | Type IIA | SS | Interwar Types | 3 | Coastal U-boat | 1935 | 0 | 10000 | 36 | 1200000 | 25 | Small coastal | Treaty limitations, 6 boats | Treaty Limited | Treaty limitations | 6 boats built |
| 3814 | German | Type IIB | SS | Interwar Types | 4 | Coastal U-boat | 1936 | 0 | 12000 | 42 | 1400000 | 25 | Improved Type II | 20 boats built | Type II Improved | 20 boats improved | 20 boats built |
| 3815 | German | Type IIC | SS | Interwar Types | 4 | Coastal U-boat | 1938 | 0 | 12000 | 42 | 1500000 | 25 | Enhanced coastal | 8 boats built | Type IIC | Enhanced design | 8 boats built |
| 3816 | German | Type IID | SS | Interwar Types | 4 | Coastal U-boat | 1940 | 0 | 12000 | 42 | 1600000 | 25 | Final Type II | 16 boats built | Final Type II | Last Type II variant | 16 boats built |
| 3817 | German | Type VIIA | SS | Type VII Line | 6 | U-boat | 1936 | 0 | 25000 | 60 | 3000000 | 44 | First Type VII | 10 boats, production model | First Type VII | Production model | 10 boats built |
| 3818 | German | Type VIIB | SS | Type VII Line | 7 | U-boat | 1939 | 0 | 30000 | 66 | 3500000 | 44 | Improved Type VII | 24 boats, larger hull | Type VIIB | 24 boats, improved | 24 boats built |
| 3819 | German | Type VIIC | SS | Type VII Line | 8 | U-boat | 1941 | 0 | 35000 | 72 | 4000000 | 44 | Workhorse U-boat | 577-593 boats! Most numerous ever | Workhorse | 577-593 boats, +35% production, UNIQUE | Most produced submarine ever! |
| 3820 | German | Type VIID | SS | Type VII Line | 8 | Minelayer | 1942 | 0 | 35000 | 72 | 4500000 | 44 | Minelayer variant | 6 boats, enlarged for mines | Minelayer | 6 boats, mine variant | 6 boats minelayer |
| 3821 | German | Type VIIF | SS | Type VII Line | 8 | Tanker | 1943 | 0 | 35000 | 72 | 5000000 | 44 | Tanker variant | 4 boats, supply role | Tanker | 4 boats, resupply | 4 boats tanker |
| 3822 | German | Type IXA | SS | Type IX Line | 7 | U-boat | 1938 | 0 | 30000 | 66 | 4500000 | 48 | Long-range U-boat | 10,500 nm range, 8 boats | Long Range | 10,500 nm range | 8 boats built |
| 3823 | German | Type IXB | SS | Type IX Line | 7 | U-boat | 1939 | 0 | 32000 | 66 | 5000000 | 48 | Improved Type IX | 14 boats built | Type IXB | Improved design | 14 boats built |
| 3824 | German | Type IXC | SS | Type IX Line | 8 | U-boat | 1940 | 0 | 35000 | 72 | 5500000 | 48 | Standard long-range | 54 boats built | Type IXC | Standard long-range | 54 boats built |
| 3825 | German | Type IXC/40 | SS | Type IX Line | 8 | U-boat | 1941 | 0 | 38000 | 72 | 6000000 | 48 | Enhanced Type IX | 87 boats, 11,400 nm range | Enhanced IX | 87 boats, enhanced | 87 boats built |
| 3826 | German | Type IXD | SS | Type IX Line | 9 | U-boat | 1942 | 0 | 45000 | 78 | 7000000 | 57 | Ultra long-range | 23,700 nm range! Unprecedented | Ultra Long Range | 23,700 nm range, +130% endurance, UNIQUE | 30 boats, 23,700 nm range! |
| 3827 | German | Type XIV | SS | Specialized Types | 8 | Tanker | 1941 | 0 | 40000 | 72 | 6500000 | 53 | Tanker Milchkuh | 203 tons extra fuel | Milchkuh | 203 tons fuel, +100% fleet endurance, UNIQUE | 10 boats, Milk Cow tanker |
| 3828 | German | Type XVII | SS | Specialized Types | 9 | Experimental | 1944 | 0 | 55000 | 78 | 8000000 | 19 | Walter HTP | Experimental hydrogen peroxide | Walter HTP | Experimental propulsion | HTP propulsion experimental |
| 3829 | German | Type XXI | SS | Elektroboote | 10 | Elektroboot | 1944 | 0 | 70000 | 84 | 12000000 | 57 | Elektroboot revolution | 17 kts submerged! 118 built | Elektroboot Revolution | 17 kts submerged, 7 days underwater, +200%, UNIQUE | 118 built, revolutionized design |
| 3830 | German | Type XXIII | SS | Elektroboote | 9 | Elektroboot | 1944 | 0 | 50000 | 72 | 5000000 | 14 | Coastal elektroboot | 61 built, fastest submarine | Fastest Submarine | World's fastest submarine, +40% coastal | 61 built, fastest submarine |
| 3831 | German | Biber | SS | Midget Submarines | 6 | Midget | 1944 | 0 | 25000 | 24 | 200000 | 1 | Midget submarine | 324 built, 9m long | Midget | 324 built, midget ops | 324 built, 9m long |
| 3832 | German | Molch | SS | Midget Submarines | 6 | Midget | 1944 | 0 | 25000 | 24 | 150000 | 1 | Single-man midget | Small operations | Single-Man | Single-man operations | Single-man midget |
| 3833 | German | Seehund | SS | Midget Submarines | 7 | Midget | 1944 | 0 | 30000 | 30 | 300000 | 2 | Type XXVII midget | 285 built, most successful | Midget Success | Most successful midget, 285 built, 9 ships sunk | 285 built, Type XXVII, 9 sunk |
| 3834 | German | U-93 Modernization | SS | Modernization | 6 | U-boat Refit | 1918 | 0 | 22000 | 54 | 1500000 | 39 | WWI refit | 10.5cm gun upgrade | WWI Refit | 10.5cm gun upgrade | U-93 modernization |
| 3835 | German | Type VIIC Refit | SS | Modernization | 9 | U-boat Upgrade | 1943 | 0 | 40000 | 72 | 5000000 | 44 | WWII modernization | Enhanced AA, radar | WWII Upgrade | AA improvements, radar | Type VIIC late-war refit |
| 3836 | German | Type XXI Refit | SS | Modernization | 10 | Elektroboot Upgrade | 1945 | 0 | 75000 | 84 | 13000000 | 57 | Elektroboot upgrade | Post-war improvements | Type XXI Upgrade | Post-war improvements | Type XXI upgrade |
| 3837 | German | Type XXVI | SS | Paper Ship | 10 | Advanced Elektroboot | 1945 | 0 | 80000 | 90 | 15000000 | 60 | Advanced elektroboot | Never completed | Type XXVI | Never completed, -10% reliability | Advanced elektroboot, never built |
| 3838 | German | Type XXIX | SS | Paper Ship | 10 | Ultimate WWII | 1945 | 0 | 90000 | 96 | 18000000 | 65 | Ultimate WWII design | Paper ship | Ultimate WWII | Paper ship, -15% reliability | Ultimate WWII paper ship |
| 3839 | German | Type XXX | SS | Paper Ship | 10 | Post-War | 1946 | 0 | 100000 | 102 | 20000000 | 70 | Post-war concept | Advanced design | Post-War | Post-war concept, -10% reliability | Post-war concept |
| 3840 | German | Type 201 | SS | Paper Ship | 10 | Post-War | 1950 | 0 | 110000 | 108 | 25000000 | 75 | Post-war submarine | Modern systems | Type 201 | Post-war design | Theoretical post-war |
| 3841 | German | Type 205 | SS | Paper Ship | 10 | Advanced | 1955 | 0 | 120000 | 114 | 30000000 | 80 | Advanced design | Snorkel, improved | Type 205 | Advanced, snorkel | Advanced design |
| 3842 | German | Type 206 | SS | Paper Ship | 10 | Cold War | 1960 | 0 | 130000 | 120 | 35000000 | 85 | Cold War submarine | Modern technology | Type 206 | Cold War tech | Cold War submarine |
| 3843 | German | Nuclear Concept | SS | Paper Ship | 10 | Nuclear | 1965 | 0 | 150000 | 150 | 50000000 | 100 | Nuclear propulsion | Theoretical | Nuclear | Theoretical nuclear, -15% reliability | Nuclear propulsion concept |
| 3844 | German | Future SS Concept | SS | Paper Ship | 10 | Future Design | 1970 | 0 | 200000 | 180 | 80000000 | 120 | Advanced future | Future technology | Future Design | Future submarine tech | Future submarine technology |
| 3100 | German | Conversion Study | CV | Early Studies | 3 | Carrier Concept | 1918 | 0 | 8000 | 36 | 1000000 | 500 | Early carrier concepts | Post-WWI carrier studies | Early Concepts | First German carrier studies, +10% research speed | Post-WWI theoretical studies |
| 3101 | German | Japanese Study | CV | Early Studies | 4 | Carrier Analysis | 1928 | 0 | 12000 | 42 | 1500000 | 600 | Japanese carrier analysis | Study of Akagi/Kaga designs | Learning from Experts | Japanese carrier expertise, +20% effectiveness | Studied Japanese designs |
| 3102 | German | Plan Z Concept | CV | Early Studies | 5 | Plan Z | 1935 | 0 | 18000 | 48 | 2000000 | 800 | Initial Plan Z carrier | Anglo-German Naval Agreement | Plan Z Initiative | Ambitious naval program, +15% capability | Plan Z carrier initiative |
| 3103 | German | Graf Zeppelin | CV | Graf Zeppelin Class | 8 | Fleet Carrier | 1938 | 0 | 40000 | 108 | 50000000 | 1760 | Famous unfinished carrier | 85% complete, 42 aircraft, 16×15cm guns | 85% Complete | Famous unfinished carrier, +30% capability if completed | 85% complete, never commissioned |
| 3104 | German | Peter Strasser | CV | Graf Zeppelin Class | 7 | Fleet Carrier | 1939 | 0 | 35000 | 96 | 45000000 | 1760 | Second carrier | Construction halted, scrapped 1940 | Halted Construction | Early cancellation, -20% reliability (incomplete) | Construction halted, scrapped |
| 3105 | German | Flugzeugträger C | CV | Plan Z Expansion | 8 | Fleet Carrier | 1940 | 0 | 45000 | 108 | 55000000 | 1800 | Third Plan Z carrier | Never started, Plan Z | Plan Z C | Never started, -15% reliability | Third Plan Z, never started |
| 3106 | German | Flugzeugträger D | CV | Plan Z Expansion | 8 | Fleet Carrier | 1940 | 0 | 45000 | 108 | 55000000 | 1800 | Fourth Plan Z carrier | Never started, Plan Z | Plan Z D | Never started, -15% reliability | Fourth Plan Z, never started |
| 3107 | German | Europa Conversion | CV | Plan Z Expansion | 7 | Auxiliary Carrier | 1942 | 0 | 35000 | 90 | 40000000 | 1500 | Liner conversion concept | Theoretical conversion | Theoretical Conversion | Theoretical conversion, -20% reliability | Liner conversion concept |
| 3108 | German | Improved Graf Zeppelin | CV | Paper Ship | 9 | Fleet Carrier | 1943 | 0 | 55000 | 120 | 65000000 | 1900 | Enhanced design | Paper ship, improved | Lessons Learned | Incorporates experience, +25%, -15% reliability | Enhanced design, paper ship |
| 3109 | German | Armored Deck Carrier | CV | Paper Ship | 9 | Armored Carrier | 1944 | 0 | 60000 | 120 | 70000000 | 1950 | British-style armored deck | Paper ship, armored | British Influence | Armored flight deck, +40% survivability, -15% reliability | Armored deck concept, paper |
| 3110 | German | Plan Z Super Carrier | CV | Paper Ship | 10 | Super Carrier | 1945 | 0 | 75000 | 150 | 90000000 | 2200 | Ultimate WWII design | Paper ship, ultimate | Ultimate Design | Maximum WWII carrier, +50% capability, -20% reliability | Ultimate WWII design, paper |
| 3111 | German | Post-War Carrier | CV | Future Concepts | 10 | Post-War | 1950 | 0 | 90000 | 180 | 120000000 | 2500 | Post-war concept | Theoretical post-war | Post-War | Post-war concept, -15% reliability | Theoretical post-war |
| 3112 | German | Jet Age Carrier | CV | Future Concepts | 10 | Jet Carrier | 1955 | 0 | 110000 | 210 | 150000000 | 2800 | Jet aircraft capable | Theoretical jet age | Jet Age | Jet capable, -15% reliability | Theoretical jet carrier |
| 3113 | German | Modern Carrier | CV | Future Concepts | 10 | Modern | 1960 | 0 | 130000 | 240 | 200000000 | 3000 | Modern systems | Theoretical modern | Modern | Modern systems, -10% reliability | Theoretical modern carrier |
| 3114 | German | Future CV Concept | CV | Future Concepts | 10 | Future Design | 1970 | 0 | 180000 | 300 | 300000000 | 3500 | Advanced future | Future technology | Future Design | Future carrier tech | Future carrier technology |
| 4000 | Japanese | Mikasa | BB | Pre-Dreadnoughts | 1 | Battleship | 1900 | 1 | 0 | 36 | 600000 | 305 | Tsushima flagship | FREE, preserved, Tōgō's flagship, 4×12" guns | Tsushima Victory | Tōgō's flagship, +40% morale, HISTORIC, FREE | Preserved at Yokosuka |
| 4001 | Japanese | Fuji | BB | Pre-Dreadnoughts | 1 | Battleship | 1896 | 1 | 0 | 30 | 500000 | 305 | First modern battleship | FREE, British-built, 2 ships, 4×12" guns | First Modern | First modern BB, +25% foundation, FREE | British-built, 2 ships |
| 4002 | Japanese | Shikishima | BB | Pre-Dreadnoughts | 2 | Battleship | 1898 | 0 | 3000 | 36 | 650000 | 305 | Improved pre-dreadnought | British-built, 2 ships, 4×12" guns | Improved Design | British-built, +15% quality | 2 ships built |
| 4003 | Japanese | Asahi | BB | Pre-Dreadnoughts | 2 | Battleship | 1899 | 0 | 3500 | 36 | 700000 | 305 | Enhanced design | British-built, 1 ship, 4×12" guns | Enhanced | British-built, +15% capability | 1 ship, repair ship WWII |
| 4004 | Japanese | Katori | BB | Pre-Dreadnoughts | 3 | Battleship | 1905 | 0 | 5000 | 42 | 800000 | 380 | Post-Tsushima | 2 ships, British designs, 4×12" guns | Post-Tsushima | Combat lessons, +20% experience | 2 ships built |
| 4005 | Japanese | Satsuma | BB | Pre-Dreadnoughts | 4 | Semi-Dreadnought | 1906 | 0 | 8000 | 48 | 1200000 | 490 | Semi-dreadnought | First Japanese-built, 2 ships, 4×12"+12×10" | First Indigenous | Japanese-built, +25% independence | First major Japanese-built |
| 4006 | Japanese | Aki | BB | Pre-Dreadnoughts | 4 | Semi-Dreadnought | 1907 | 0 | 9000 | 48 | 1300000 | 495 | Improved semi-dreadnought | 2nd Satsuma, refined, 4×12"+12×10" | Refined Design | Refined Satsuma, +20% capability | 2nd Satsuma class |
| 4007 | Japanese | Kawachi | BB | First Dreadnoughts | 5 | Dreadnought | 1910 | 0 | 12000 | 54 | 2000000 | 545 | First dreadnought | First all-big-gun, 2 ships, 12×12" guns | First Dreadnought | First Japanese dreadnought, +30% capability | Magazine explosion 1918 |
| 4008 | Japanese | Settsu | BB | First Dreadnoughts | 5 | Dreadnought | 1911 | 0 | 13000 | 54 | 2200000 | 550 | Improved dreadnought | 2nd Kawachi, refined, 12×12" guns | Improved | Refined Kawachi, +15% reliability | Survived as training ship |
| 4009 | Japanese | Kongō | BB | Kongō Battlecruisers | 6 | Battlecruiser | 1912 | 0 | 16000 | 60 | 3500000 | 700 | Battlecruiser | British-built Vickers, 8×14" guns, 27.5 kts | British Design | Vickers-built, +30% quality | Last Japanese capital ship built abroad |
| 4010 | Japanese | Hiei | BB | Kongō Battlecruisers | 6 | Battlecruiser | 1912 | 0 | 17000 | 60 | 3600000 | 700 | 2nd Kongō | Japanese-built, 8×14" guns, 27.5 kts | Japanese Built | Indigenous construction, +20% | Sunk Guadalcanal 1942 |
| 4011 | Japanese | Haruna | BB | Kongō Battlecruisers | 6 | Battlecruiser | 1913 | 0 | 17500 | 60 | 3700000 | 705 | 3rd Kongō | Japanese-built, 8×14" guns, 27.5 kts | Japanese Built | Indigenous, +20% | Sunk Kure 1945 |
| 4012 | Japanese | Kirishima | BB | Kongō Battlecruisers | 6 | Battlecruiser | 1913 | 0 | 18000 | 60 | 3800000 | 710 | 4th Kongō | Japanese-built, 8×14" guns, 27.5 kts | Japanese Built | Indigenous, +20% | Sunk Guadalcanal 1942 |
| 4013 | Japanese | Fusō | BB | Super-Dreadnoughts | 7 | Super-Dreadnought | 1914 | 0 | 22000 | 66 | 5000000 | 910 | Super-dreadnought | 6 twin turrets, 12×14" guns, pagoda mast | Pagoda Mast | 12×14" guns, +35% firepower, distinctive | Sunk Surigao Strait 1944 |
| 4014 | Japanese | Yamashiro | BB | Super-Dreadnoughts | 7 | Super-Dreadnought | 1915 | 0 | 23000 | 66 | 5200000 | 920 | 2nd Fusō | Distinctive silhouette, 12×14" guns, pagoda | Distinctive | Distinctive profile, +30% | Sunk Surigao Strait 1944 |
| 4015 | Japanese | Ise | BB | Super-Dreadnoughts | 7 | Super-Dreadnought | 1916 | 0 | 24000 | 66 | 5500000 | 930 | Improved Fusō | Better layout, 2 ships, 12×14" guns | Improved Layout | Better turret arrangement, +25% | Later carrier conversion |
| 4016 | Japanese | Hyūga | BB | Super-Dreadnoughts | 7 | Super-Dreadnought | 1917 | 0 | 25000 | 66 | 5700000 | 940 | 2nd Ise | Refined design, 12×14" guns | Refined | Refined Ise, +20% | Later carrier conversion |
| 4017 | Japanese | Nagato | BB | 16-Inch Gun Era | 8 | Battleship | 1919 | 0 | 35000 | 72 | 10000000 | 990 | First 16" guns | World's first 16.1" BB! 8×16.1" guns, 26.7 kts | World's First 16-Inch | First 16" guns afloat, +35% firepower, HISTORIC | Yamamoto's Pearl Harbor flagship |
| 4018 | Japanese | Mutsu | BB | 16-Inch Gun Era | 8 | Battleship | 1920 | 0 | 36000 | 72 | 10500000 | 1000 | 2nd Nagato | Public subscription, 8×16.1" guns | Public Subscription | Built by donations, +25% morale | Magazine explosion 1943 |
| 4019 | Japanese | Tosa | BB | Washington Treaty Cancellations | 8 | Battleship | 1921 | 0 | 38000 | 78 | 12000000 | 1010 | Improved Nagato | Cancelled, Washington Treaty, 10×16.1" guns | Treaty Cancelled | 40% complete, -20% reliability (cancelled) | Used as gunnery target |
| 4020 | Japanese | Kaga | BB | Washington Treaty Cancellations | 8 | Battleship | 1921 | 0 | 39000 | 78 | 12500000 | 1020 | 2nd Tosa | Converted to carrier, 10×16.1" guns | Carrier Conversion | Converted to CV, -15% reliability | Famous carrier at Midway |
| 4021 | Japanese | Kii | BB | Washington Treaty Cancellations | 8 | Fast Battleship | 1922 | 0 | 40000 | 84 | 13000000 | 1080 | Fast battleship | Cancelled, never started, 10×16.1", 29.75 kts | Never Started | Never started, -20% reliability | Cancelled before construction |
| 4022 | Japanese | Owari | BB | Washington Treaty Cancellations | 8 | Fast Battleship | 1922 | 0 | 41000 | 84 | 13500000 | 1080 | 2nd Kii | Cancelled, never started, 10×16.1" guns | Never Started | Never started, -20% reliability | Cancelled before construction |
| 4023 | Japanese | Number 13 | BB | Washington Treaty Cancellations | 9 | Fast Battleship | 1922 | 0 | 50000 | 90 | 18000000 | 1200 | Revolutionary design | 18.1" guns planned, 8×18.1", 30 kts, cancelled | Ten Years Ahead | Revolutionary, +40%, -25% reliability (cancelled) | "Ten years ahead of time" |
| 4024 | Japanese | Number 14 | BB | Washington Treaty Cancellations | 9 | Fast Battleship | 1922 | 0 | 51000 | 90 | 18500000 | 1210 | 2nd Number 13 | 30 kts, 8×18.1" guns, cancelled | Never Built | Never started, -25% reliability | Cancelled Washington Treaty |
| 4025 | Japanese | Kongō Kai | BB | Fast Battleship Conversions | 8 | Fast Battleship | 1935 | 0 | 30000 | 60 | 8000000 | 805 | Fast battleship refit | 30+ knots! 8×14" guns, revolutionary | Fast BB Revolution | 30+ kts, +50% speed, +40%, REVOLUTIONARY | Most extensive BB reconstruction |
| 4026 | Japanese | Hiei Kai | BB | Fast Battleship Conversions | 8 | Fast Battleship | 1936 | 0 | 31000 | 60 | 8200000 | 810 | 2nd Kongō modernized | Fast BB conversion, 8×14" guns, 30+ kts | Fast BB | 30+ kts, +50% speed, +35% | Sunk Guadalcanal 1942 |
| 4027 | Japanese | Haruna Kai | BB | Fast Battleship Conversions | 8 | Fast Battleship | 1937 | 0 | 32000 | 60 | 8400000 | 815 | 3rd Kongō modernized | 30+ knots, 8×14" guns | Fast BB | 30+ kts, +50% speed, +35% | Sunk Kure 1945 |
| 4028 | Japanese | Kirishima Kai | BB | Fast Battleship Conversions | 8 | Fast Battleship | 1938 | 0 | 33000 | 60 | 8600000 | 820 | 4th Kongō modernized | Fastest BBs afloat, 8×14" guns, 30+ kts | Fastest BBs | Fastest BBs afloat, +50% speed | Sunk Guadalcanal 1942 |
| 4029 | Japanese | Nagato Kai | BB | Interwar Modernizations | 9 | Battleship | 1936 | 0 | 40000 | 72 | 12000000 | 1080 | Nagato modernization | Improved armor/AA, 8×16.1" guns | Modernized | Improved protection, +25% | Pearl Harbor flagship |
| 4030 | Japanese | Mutsu Kai | BB | Interwar Modernizations | 9 | Battleship | 1936 | 0 | 41000 | 72 | 12500000 | 1090 | Mutsu modernization | Enhanced capability, 8×16.1" guns | Enhanced | Enhanced capability, +25% | Magazine explosion 1943 |
| 4031 | Japanese | Fusō Kai | BB | Interwar Modernizations | 8 | Battleship | 1933 | 0 | 28000 | 66 | 7000000 | 1000 | Fusō modernization | Reconstructed pagoda mast, 12×14" guns | Reconstructed | Pagoda mast, +20% | Sunk Surigao 1944 |
| 4032 | Japanese | Yamashiro Kai | BB | Interwar Modernizations | 8 | Battleship | 1935 | 0 | 29000 | 66 | 7500000 | 1010 | Yamashiro modernization | Improved AA, 12×14" guns | Improved | Improved AA, +20% | Sunk Surigao 1944 |
| 4033 | Japanese | Yamato | BB | Yamato Class | 10 | Super-Battleship | 1940 | 0 | 100000 | 120 | 100000000 | 1820 | Super-battleship | LARGEST EVER! 18.1" guns, 72,000 tons, 9×18.1" | Largest Ever Built | 18.1" guns, 72,000 tons, +100%, LEGENDARY | Largest battleship ever |
| 4034 | Japanese | Musashi | BB | Yamato Class | 10 | Super-Battleship | 1941 | 0 | 105000 | 120 | 105000000 | 1830 | 2nd Yamato | 17 bombs/19 torpedoes to sink, 9×18.1" guns | Unsinkable Giant | 17 bombs/19 torps, +60% survivability, HISTORIC | Sunk Leyte Gulf 1944 |
| 4035 | Japanese | Shinano | BB | Yamato Class | 10 | Carrier Conversion | 1944 | 0 | 110000 | 90 | 90000000 | 1650 | Carrier conversion | Converted to carrier, Yamato hull | Carrier Conversion | Converted to CV, -20% reliability | Sunk by submarine 1944 |
| 4036 | Japanese | Ise Kai-II | BB | Hybrid Conversions | 9 | Hybrid BB-CV | 1943 | 0 | 45000 | 72 | 15000000 | 1100 | Hybrid carrier-BB | Aft flight deck, 8×14" guns, 22 aircraft | Hybrid Concept | BB+CV hybrid, +30% versatility, -20% reliability | Unique hybrid design |
| 4037 | Japanese | Hyūga Kai-II | BB | Hybrid Conversions | 9 | Hybrid BB-CV | 1943 | 0 | 46000 | 72 | 15500000 | 1110 | 2nd hybrid conversion | 22 aircraft capacity, 8×14" guns, flight deck | Hybrid | Hybrid conversion, +30% versatility, -20% | Never embarked aircraft |
| 4038 | Japanese | Design A-150 | BB | Paper Ships | 10 | Super-Battleship | 1941 | 0 | 120000 | 150 | 120000000 | 2280 | Super Yamato | 20.1" guns! 6×20.1", 90,000 tons, cancelled | Largest Guns Designed | 20.1" guns, +120% firepower, -30% reliability | Largest guns ever designed |
| 4039 | Japanese | Design A-150 (2) | BB | Paper Ships | 10 | Super-Battleship | 1941 | 0 | 125000 | 150 | 125000000 | 2300 | 2nd A-150 | Largest guns designed, 6×20.1" guns | Largest Guns | 20.1" guns, +120% firepower, -30% | 2 guns ordered for testing |
| 4040 | Japanese | Post-War BB | BB | Paper Ships | 10 | Post-War | 1950 | 0 | 150000 | 180 | 150000000 | 2400 | Theoretical post-war | Japan prohibited from BBs | Prohibited | Prohibited by occupation, -20% reliability | Never pursued |
| 4041 | Japanese | Guided Missile BB | BB | Paper Ships | 10 | Missile BB | 1960 | 0 | 180000 | 210 | 200000000 | 2500 | Theoretical modernization | Never pursued | Never Pursued | Never pursued, -20% reliability | Never pursued |
| 4042 | Japanese | Future BB Concept | BB | Paper Ships | 10 | Future Design | 1970 | 0 | 200000 | 240 | 250000000 | 2600 | Theoretical future | Never pursued | Never Pursued | Never pursued, -15% reliability | Never pursued |
| 4600 | Japanese | Asama | CA | Armored Cruisers | 1 | Armored Cruiser | 1896 | 1 | 0 | 30 | 400000 | 245 | Armored cruiser | FREE, British-built, Tsushima, 2×8"+10×6" | Tsushima Service | Tsushima victory, +30% experience, FREE | British-built, Tsushima |
| 4601 | Japanese | Tokiwa | CA | Armored Cruisers | 1 | Armored Cruiser | 1898 | 1 | 0 | 30 | 420000 | 250 | 2nd Asama | FREE, British-built, 2×8"+10×6" guns | Tsushima | Tsushima, +25% experience, FREE | British-built, 2 ships |
| 4602 | Japanese | Izumo | CA | Armored Cruisers | 2 | Armored Cruiser | 1899 | 0 | 2500 | 36 | 450000 | 250 | Improved armored | British-built, Tsushima, 4×8"+14×6" | Improved | Tsushima service, +20% | British-built, 2 ships |
| 4603 | Japanese | Iwate | CA | Armored Cruisers | 2 | Armored Cruiser | 1900 | 0 | 2800 | 36 | 470000 | 255 | 2nd Izumo | British-built, 4×8" guns | Improved | Survived WWII, +15% | British-built, scrapped 1947 |
| 4604 | Japanese | Kasuga | CA | Armored Cruisers | 3 | Armored Cruiser | 1902 | 0 | 4000 | 42 | 550000 | 280 | Italian design | Italian-built Ansaldo, 1×10"+2×8" | Italian | Italian Ansaldo-built, +20% | Italian design, 2 ships |
| 4605 | Japanese | Nisshin | CA | Armored Cruisers | 3 | Armored Cruiser | 1903 | 0 | 4500 | 42 | 580000 | 285 | 2nd Kasuga | Italian-built, unique guns | Italian | Italian design, +15% | Italian Ansaldo-built |
| 4606 | Japanese | Tsukuba | CA | Armored Cruisers | 4 | Armored Cruiser | 1905 | 0 | 6000 | 48 | 750000 | 350 | Large armored cruiser | First Japanese-built, 4×12"+12×6" | First Indigenous | Japanese-built, +25% | Magazine explosion 1917 |
| 4607 | Japanese | Ikoma | CA | Armored Cruisers | 4 | Armored Cruiser | 1906 | 0 | 6500 | 48 | 780000 | 355 | 2nd Tsukuba | Japanese construction, 4×12" guns | Japanese Built | Indigenous, +20% | Scrapped 1924 |
| 4608 | Japanese | Ibuki | CA | Armored Cruisers | 5 | Armored Cruiser | 1907 | 0 | 8000 | 54 | 900000 | 375 | Advanced armored | Pre-battlecruiser, 4×12"+8×8" | Advanced | Pre-battlecruiser, +25% | Scrapped 1923 |
| 4609 | Japanese | Kurama | CA | Armored Cruisers | 5 | Armored Cruiser | 1909 | 0 | 8500 | 54 | 950000 | 380 | 2nd Ibuki | Advanced design, 4×12" guns | Advanced | Peak armored cruiser, +20% | Scrapped 1923 |
| 4610 | Japanese | Tenryū | CL | Early Light Cruisers | 6 | Light Cruiser | 1918 | 0 | 12000 | 48 | 1800000 | 80 | First modern CL | 4×5.5" guns, 33 kts, 2 ships | First Modern | First modern light cruiser, +30% | Sunk December 1942 |
| 4611 | Japanese | Tatsuta | CL | Early Light Cruisers | 6 | Light Cruiser | 1919 | 0 | 12500 | 48 | 1900000 | 82 | 2nd Tenryū | 4×5.5" guns, 33 kts | First Modern | First modern CL, +25% | Sunk March 1944 |
| 4612 | Japanese | Kuma | CL | Early Light Cruisers | 6 | Light Cruiser | 1919 | 0 | 14000 | 54 | 2200000 | 140 | Improved light cruiser | 7×5.5" guns, 36 kts, 6 ships | Improved | 7×5.5" guns, +20% | 6-ship class |
| 4613 | Japanese | Tama | CL | Early Light Cruisers | 6 | Light Cruiser | 1920 | 0 | 14500 | 54 | 2300000 | 142 | 2nd Kuma | 7×5.5" guns, 36 kts | Improved | 6-ship class, +15% | Sunk October 1944 |
| 4614 | Japanese | Kitakami | CL | Early Light Cruisers | 7 | Light Cruiser | 1920 | 0 | 15000 | 54 | 2400000 | 145 | 3rd Kuma | Later torpedo cruiser, 40× torpedoes! | Torpedo Cruiser | 40× Type 93 torps (conversion), +100% torpedo | Converted 1941, 40 torpedoes |
| 4615 | Japanese | Ōi | CL | Early Light Cruisers | 7 | Light Cruiser | 1921 | 0 | 15500 | 54 | 2500000 | 147 | 4th Kuma | Later torpedo cruiser, 40× torpedoes | Torpedo Cruiser | 40× torps (conversion), +100% | Sunk July 1944 |
| 4616 | Japanese | Nagara | CL | Early Light Cruisers | 7 | Light Cruiser | 1921 | 0 | 16000 | 54 | 2600000 | 140 | Improved Kuma | 6 ships, 7×5.5" guns, 36 kts | Refined | Refined Kuma, +15% | 6-ship class |
| 4617 | Japanese | Isuzu | CL | Early Light Cruisers | 7 | Light Cruiser | 1921 | 0 | 16500 | 54 | 2700000 | 142 | 2nd Nagara | Later AA conversion, 8×5"+66×25mm | AA Conversion | 66×25mm AA (conversion), +80% AA | Converted 1944, AA cruiser |
| 4618 | Japanese | Sendai | CL | Early Light Cruisers | 7 | Light Cruiser | 1922 | 0 | 17000 | 54 | 2800000 | 140 | Further improved | 3 ships, 7×5.5" guns, 35 kts | Improved | Refined design, +15% | 3-ship class |
| 4619 | Japanese | Jintsu | CL | Early Light Cruisers | 7 | Light Cruiser | 1923 | 0 | 17500 | 54 | 2900000 | 142 | 2nd Sendai | Night battle famous, searchlight | Night Combat | Night battle hero, +30% night combat | Famous Kolombangara 1943 |
| 4620 | Japanese | Yūbari | CL | Experimental Design | 7 | Light Cruiser | 1923 | 0 | 18000 | 60 | 3000000 | 73 | Experimental design | Hiraga's compact cruiser, 6×5.5" guns | Hiraga's Experiment | Weight-saving, +25% efficiency, INNOVATIVE | Admiral Hiraga's experiment |
| 4621 | Japanese | Furutaka | CA | Early Treaty Cruisers | 7 | Heavy Cruiser | 1925 | 0 | 20000 | 60 | 4500000 | 235 | First treaty cruiser | 6×8" guns, 2 ships, 34.5 kts | First Treaty | First 8" cruiser, +25% | Sunk October 1942 |
| 4622 | Japanese | Kako | CA | Early Treaty Cruisers | 7 | Heavy Cruiser | 1925 | 0 | 21000 | 60 | 4700000 | 240 | 2nd Furutaka | 6×8" guns, treaty cruiser | First Treaty | Treaty cruiser, +20% | First cruiser lost, Aug 1942 |
| 4623 | Japanese | Aoba | CA | Early Treaty Cruisers | 8 | Heavy Cruiser | 1926 | 0 | 24000 | 66 | 5500000 | 245 | Improved Furutaka | 6×8" guns twins, 2 ships, 35 kts | Improved | Twin turrets, +20% | Survived war damaged |
| 4624 | Japanese | Kinugasa | CA | Early Treaty Cruisers | 8 | Heavy Cruiser | 1926 | 0 | 25000 | 66 | 5700000 | 250 | 2nd Aoba | 6×8" guns, improved | Improved | Improved design, +15% | Sunk November 1942 |
| 4625 | Japanese | Myōkō | CA | Myōkō Class | 8 | Heavy Cruiser | 1927 | 0 | 30000 | 72 | 8000000 | 330 | Powerful heavy cruiser | 10×8" guns! 4 ships, 35.5 kts, FAMOUS | Ten 8-Inch Guns | 10×8" guns, +40% firepower, LEGENDARY | Most powerful treaty cruiser |
| 4626 | Japanese | Nachi | CA | Myōkō Class | 8 | Heavy Cruiser | 1927 | 0 | 31000 | 72 | 8200000 | 335 | 2nd Myōkō | 10×8" guns, legendary | Ten 8-Inch | 10×8" guns, +40% firepower | Sunk Manila 1944 |
| 4627 | Japanese | Ashigara | CA | Myōkō Class | 8 | Heavy Cruiser | 1928 | 0 | 32000 | 72 | 8400000 | 340 | 3rd Myōkō | 10×8" guns, "Hungry Wolf" | Ten 8-Inch | 10×8" guns, +40% firepower | "Hungry Wolf," sunk 1945 |
| 4628 | Japanese | Haguro | CA | Myōkō Class | 8 | Heavy Cruiser | 1928 | 0 | 33000 | 72 | 8600000 | 345 | 4th Myōkō | 10×8" guns, distinguished service | Ten 8-Inch | 10×8" guns, +40% firepower | Sunk by destroyers 1945 |
| 4629 | Japanese | Takao | CA | Takao Class | 9 | Heavy Cruiser | 1930 | 0 | 36000 | 72 | 9500000 | 335 | Improved Myōkō | 10×8" guns, better armor, 4 ships | Improved | Better armor, +30% protection | Survived war, scrapped 1946 |
| 4630 | Japanese | Atago | CA | Takao Class | 9 | Heavy Cruiser | 1930 | 0 | 37000 | 72 | 9700000 | 340 | 2nd Takao | Kurita's flagship Leyte, 10×8" guns | Flagship | Kurita's flagship, +25% command | Sunk October 1944 |
| 4631 | Japanese | Chōkai | CA | Takao Class | 9 | Heavy Cruiser | 1931 | 0 | 38000 | 72 | 9900000 | 345 | 3rd Takao | Distinguished service, 10×8" guns | Distinguished | Distinguished service, +25% | Sunk Leyte Gulf 1944 |
| 4632 | Japanese | Maya | CA | Takao Class | 9 | Heavy Cruiser | 1932 | 0 | 39000 | 72 | 10100000 | 350 | 4th Takao | AA conversion 1943, 8×5"+48×25mm | AA Conversion | AA conversion, +40% AA | Sunk October 1944 |
| 4633 | Japanese | Mogami | CA | Mogami Class | 9 | Light/Heavy Cruiser | 1935 | 0 | 45000 | 78 | 12000000 | 285 | Revolutionary design | 15×6.1" CL → 10×8" CA! 4 ships, UNIQUE | Convertible Cruiser | 15×6.1" → 10×8" conversion, +50% versatility, REVOLUTIONARY | Revolutionary conversion capability |
| 4634 | Japanese | Mikuma | CA | Mogami Class | 9 | Light/Heavy Cruiser | 1935 | 0 | 46000 | 78 | 12200000 | 290 | 2nd Mogami | Convertible cruiser, 15×6.1" → 10×8" | Convertible | Conversion capability, +50% | Sunk Midway 1942 |
| 4635 | Japanese | Suzuya | CA | Mogami Class | 9 | Light/Heavy Cruiser | 1936 | 0 | 47000 | 78 | 12400000 | 295 | 3rd Mogami | Revolutionary conversion, 15×6.1" → 10×8" | Convertible | Revolutionary, +50% versatility | Sunk Leyte Gulf 1944 |
| 4636 | Japanese | Kumano | CA | Mogami Class | 9 | Light/Heavy Cruiser | 1936 | 0 | 48000 | 78 | 12600000 | 300 | 4th Mogami | Innovative design, 15×6.1" → 10×8" | Convertible | Innovative conversion, +50% | Sunk November 1944 |
| 4637 | Japanese | Tone | CA | Tone Class | 9 | Heavy Cruiser | 1938 | 0 | 42000 | 72 | 11000000 | 285 | All-forward turrets | 4×8" forward, 6 aircraft, 2 ships, 35 kts | All-Forward Turrets | All-forward layout, +35% recon, +25% aircraft, UNIQUE | Unique all-forward design |
| 4638 | Japanese | Chikuma | CA | Tone Class | 9 | Heavy Cruiser | 1938 | 0 | 43000 | 72 | 11200000 | 290 | 2nd Tone | Reconnaissance cruiser, 4×8" forward | Reconnaissance | Recon cruiser, +35% recon | Sunk Leyte Gulf 1944 |
| 4639 | Japanese | Agano | CL | Wartime Light Cruisers | 9 | Light Cruiser | 1941 | 0 | 40000 | 66 | 10000000 | 170 | Modern light cruiser | 6×6" guns, 4 ships, 35 kts, AA focus | Modern | AA-focused, +30% AA | 4-ship class |
| 4640 | Japanese | Ōyodo | CL | Wartime Light Cruisers | 10 | Light Cruiser | 1942 | 0 | 50000 | 78 | 15000000 | 208 | Fleet flagship | 6×6.1" guns, command ship, 6 aircraft | Fleet Flagship | Command facilities, +35% command | Fleet flagship, survived |
| 4641 | Japanese | Ibuki (WWII) | CA | Late War Designs | 10 | Heavy Cruiser | 1943 | 0 | 55000 | 84 | 18000000 | 310 | Improved heavy cruiser | 80% complete, 10×8" guns, cancelled | 80% Complete | 80% complete, -20% reliability | Cancelled, 80% complete |
| 4642 | Japanese | Future Cruiser | CA | Late War Designs | 10 | Future Design | 1960 | 0 | 70000 | 90 | 25000000 | 350 | Theoretical post-war | Never pursued | Never Pursued | Never pursued, -15% reliability | Never pursued post-war |
| 4700 | Japanese | Momo | DD | Momo Class | 3 | Destroyer | 1916 | 1 | 0 | 30 | 0 | 60 | WWI destroyer | FREE! 21 ships, 4×4.7" guns, 31.5 kts | Early Destroyer | Basic destroyer, FREE starting ship | Early WWI design |
| 4701 | Japanese | Momi | DD | Momi Class | 4 | Destroyer | 1920 | 0 | 5000 | 36 | 800000 | 90 | Improved WWI type | 21 ships, 4×4.7" guns, 36 kts | Improved Design | +15% speed, improved seakeeping | Post-WWI improvement |
| 4702 | Japanese | Minekaze | DD | Minekaze Class | 5 | Destroyer | 1920 | 1 | 8000 | 42 | 1200000 | 120 | Fast destroyer | FREE! 39 kts! 15 ships, 4×4.7" guns, 6 torpedoes | High Speed | 39 knots, +25% speed, FREE starting ship | First high-speed destroyer |
| 4703 | Japanese | Kamikaze | DD | Kamikaze Class | 6 | Destroyer | 1922 | 0 | 10000 | 48 | 1500000 | 150 | Treaty destroyer | 9 ships, 4×4.7" guns, 6 torpedoes, 37.2 kts | Treaty Compliant | Washington Treaty compliant design | Washington Treaty design |
| 4704 | Japanese | Mutsuki | DD | Mutsuki Class | 6 | Destroyer | 1926 | 0 | 12000 | 54 | 1800000 | 180 | First 24" torpedoes | 12 ships, 4×5" guns, 6×24" torpedoes! 33 kts | Type 8 Torpedoes | First 24-inch torpedoes, +30% torpedo power | First 24-inch torpedoes |
| 4705 | Japanese | Fubuki | DD | Fubuki Class | 7 | Destroyer | 1928 | 0 | 15000 | 54 | 1500000 | 165 | SPECIAL TYPE | Revolutionary! 6×5" guns, 9 torpedoes, 34 kts | Special Type Destroyer | Enclosed turrets, +50% capability, REVOLUTIONARY | Revolutionary enclosed turrets |
| 4706 | Japanese | Ayanami | DD | Fubuki Class (II) | 7 | Destroyer | 1930 | 0 | 16000 | 60 | 1600000 | 180 | Improved Special Type | 10 ships (Fubuki II), improved fire control | Improved Fire Control | +20% gunnery accuracy | Improved Special Type variant |
| 4707 | Japanese | Akatsuki | DD | Fubuki Class (III) | 7 | Destroyer | 1932 | 0 | 17000 | 66 | 1700000 | 195 | Refined Special Type | 4 ships (Fubuki III), refined design | Refined Design | +10% overall performance | Final Special Type variant |
| 4708 | Japanese | Hatsuharu | DD | Hatsuharu Class | 8 | Destroyer | 1933 | 0 | 20000 | 60 | 2000000 | 180 | Overloaded design | 6 ships, topheaven initially, 5×5" guns | Topheaven Issue | Stability problems, -15% reliability initially | Initial stability issues |
| 4709 | Japanese | Shiratsuyu | DD | Shiratsuyu Class | 8 | Destroyer | 1936 | 0 | 22000 | 66 | 2200000 | 210 | Improved balance | 10 ships, stability improved, 5×5" guns, 8 torpedoes | Improved Stability | Stability corrected, +20% reliability | Corrected Hatsuharu issues |
| 4710 | Japanese | Asashio | DD | Asashio Class | 8 | Destroyer | 1937 | 0 | 25000 | 72 | 2500000 | 225 | Powerful destroyer | 10 ships, 6×5" guns, 8 torpedoes, 35 kts | Powerful Armament | 6×5" guns, +25% firepower | Strong balanced design |
| 4711 | Japanese | Kagero | DD | Kagero Class | 9 | Destroyer | 1939 | 0 | 30000 | 78 | 3000000 | 240 | Standard wartime | 19 ships, 6×5" guns, 8 torpedoes, 35.5 kts | Standard Design | Most-produced class, +15% production | Most-produced pre-war class |
| 4712 | Japanese | Yūgumo | DD | Yūgumo Class | 9 | Destroyer | 1941 | 0 | 32000 | 84 | 3200000 | 255 | Refined Kagero | 19 ships, improved range, 6×5" guns, 8 torpedoes | Improved Range | +30% range, refined design | Kagero refinement |
| 4713 | Japanese | Akizuki | DD | Akizuki Class | 9 | Destroyer | 1942 | 0 | 40000 | 90 | 4000000 | 270 | AA SPECIALIST | 8×3.9" AA guns! 12 ships, 33 kts | Anti-Aircraft Specialist | 8×3.9" DP guns, +80% AA capability | Dedicated AA destroyer |
| 4714 | Japanese | Shimakaze | DD | Shimakaze Class | 10 | Destroyer | 1942 | 0 | 50000 | 72 | 5000000 | 240 | FASTEST EVER | 40.9 kts! 15 torpedoes, LEGENDARY | Ultimate Speed | 40.9 knots record, 15× torpedoes, +100% capability, LEGENDARY | Fastest destroyer ever built |
| 4715 | Japanese | Fuyutsuki | DD | Akizuki Class (II) | 9 | Destroyer | 1944 | 0 | 42000 | 96 | 4200000 | 285 | Improved Akizuki | 20 ships planned, improved AA, 8×3.9" guns | Improved AA Design | +20% AA efficiency | Late-war AA destroyer |
| 4716 | Japanese | Matsu | DD | Matsu Class | 8 | Destroyer | 1944 | 0 | 28000 | 72 | 2500000 | 210 | Emergency wartime | 18 ships, simplified, 3×5" guns, 4 torpedoes | Emergency Design | Simplified for fast production, -20% capability but fast build | Simplified wartime design |
| 4717 | Japanese | Tachibana | DD | Tachibana Class | 8 | Destroyer | 1945 | 0 | 30000 | 78 | 2700000 | 225 | Final wartime | 14 ships, improved Matsu, 3×5" guns | Final Emergency | Final simplified design, +10% over Matsu | Final wartime design |
| 4718 | Japanese | Super Shimakaze | DD | Super Shimakaze | 10 | Destroyer | 1943 | 0 | 75000 | 90 | 7500000 | 300 | 45 knots planned | PAPER! 45 kts, 15 torpedoes, cancelled | Ultimate Speed Design | 45 knots planned, -30% reliability, PAPER | Cancelled speed record attempt |
| 4719 | Japanese | Type 1953 | DD | Type 1953 | 6 | Destroyer | 1953 | 0 | 35000 | 84 | 3500000 | 270 | Post-war restart | Post-war design, 3×5" guns, modern systems | Post-War Restart | Modern sensors, +25% detection | Post-war Japanese Maritime Self-Defense Force |
| 4720 | Japanese | Harukaze | DD | Harukaze Class | 7 | Destroyer | 1956 | 0 | 40000 | 90 | 4000000 | 285 | First modern DD | 2 ships, 3×5" guns, modern ASW | Modern Design | Modern ASW, +40% submarine detection | First modern JMSDF design |
| 4721 | Japanese | Ayanami 1957 | DD | Ayanami Class | 7 | Destroyer | 1957 | 0 | 45000 | 96 | 4500000 | 300 | Modern destroyer | 2 ships, 4×3" guns, modern systems | Advanced Systems | Modern radar/sonar, +50% detection | Advanced JMSDF destroyer |
| 4722 | Japanese | Murasame | DD | Murasame Class | 8 | Destroyer | 1958 | 0 | 50000 | 102 | 5000000 | 315 | ASW specialist | 3 ships, ASW focus, helicopters | ASW Focus | Helicopter ops, +60% ASW | ASW-focused design |
| 4723 | Japanese | Akizuki 1959 | DD | Akizuki Class | 8 | Destroyer | 1959 | 0 | 55000 | 108 | 5500000 | 330 | Modern AA/ASW | 4 ships, balanced AA/ASW, modern | Balanced Design | AA + ASW balance, +45% versatility | Balanced modern destroyer |
| 4724 | Japanese | Yamagumo | DD | Yamagumo Class | 9 | Destroyer | 1960 | 0 | 60000 | 114 | 6000000 | 345 | Advanced ASW | 3 ships, advanced sonar, ASROC | Advanced ASW | ASROC system, +70% ASW capability | Advanced ASW destroyer |
| 4725 | Japanese | Momo 1916 Kai | DD | Momo Class Retrofit | 4 | Destroyer | 1925 | 0 | 3000 | 36 | 500000 | 75 | Modernized WWI | Retrofitted with improved systems | Basic Retrofit | +20% capability over original | Modernized Momo class |
| 4726 | Japanese | Momi Kai | DD | Momi Class Retrofit | 5 | Destroyer | 1930 | 0 | 4000 | 42 | 700000 | 105 | Upgraded 1920s | Improved fire control, torpedoes | Improved Systems | +25% combat capability | Upgraded Momi class |
| 4727 | Japanese | Minekaze Kai | DD | Minekaze Class Retrofit | 6 | Destroyer | 1935 | 0 | 6000 | 48 | 1000000 | 135 | Modernized speed | Improved engines, modern torpedoes | Speed Maintained | Maintains 39 knots, +30% systems | Modernized Minekaze |
| 4728 | Japanese | Kamikaze Kai | DD | Kamikaze Class Retrofit | 7 | Destroyer | 1936 | 0 | 8000 | 54 | 1200000 | 165 | Treaty era upgrade | Modern fire control, AA improved | Modern Upgrade | +35% capability, improved AA | Upgraded Kamikaze |
| 4729 | Japanese | Mutsuki Kai | DD | Mutsuki Class Retrofit | 7 | Destroyer | 1940 | 0 | 10000 | 60 | 1500000 | 180 | Wartime upgrade | Type 93 torpedoes, improved AA | Type 93 Upgrade | Type 93 Long Lance, +50% torpedo power | Wartime Mutsuki upgrade |
| 4730 | Japanese | Fubuki Kai | DD | Fubuki Class Retrofit | 8 | Destroyer | 1942 | 0 | 12000 | 66 | 1800000 | 210 | Special Type upgrade | Improved AA, radar, Type 93 torpedoes | Radar Equipped | Radar systems, +40% detection | Upgraded Special Type |
| 4731 | Japanese | Ayanami Kai | DD | Fubuki II Retrofit | 8 | Destroyer | 1943 | 0 | 14000 | 72 | 2000000 | 225 | Enhanced Special Type | Enhanced AA, modern systems | Enhanced Systems | +45% overall capability | Enhanced Fubuki II |
| 4732 | Japanese | Akatsuki Kai | DD | Fubuki III Retrofit | 8 | Destroyer | 1944 | 0 | 15000 | 78 | 2100000 | 240 | Refined upgrade | Maximum Special Type upgrade | Maximum Upgrade | +50% capability, peak Special Type | Peak Fubuki III |
| 4733 | Japanese | Hatsuharu Kai | DD | Hatsuharu Class Retrofit | 9 | Destroyer | 1942 | 0 | 18000 | 72 | 2200000 | 225 | Stability perfected | Stability fully corrected, improved systems | Stability Perfected | Stability issues resolved, +40% reliability | Corrected Hatsuharu |
| 4734 | Japanese | Shiratsuyu Kai | DD | Shiratsuyu Class Retrofit | 9 | Destroyer | 1943 | 0 | 20000 | 78 | 2400000 | 255 | Enhanced balance | Enhanced AA, radar, Type 93 | Enhanced Balance | +50% overall performance | Enhanced Shiratsuyu |
| 4735 | Japanese | Asashio Kai | DD | Asashio Class Retrofit | 9 | Destroyer | 1944 | 0 | 22000 | 84 | 2600000 | 270 | Powerful upgrade | Maximum AA upgrade, radar | Maximum Firepower | +60% combat capability | Maximum Asashio upgrade |
| 4736 | Japanese | Kagero Kai | DD | Kagero Class Retrofit | 10 | Destroyer | 1944 | 0 | 28000 | 90 | 3200000 | 285 | Standard upgraded | Radar, improved AA, Type 93 | Standard Upgrade | +55% capability, modern systems | Upgraded standard type |
| 4737 | Japanese | Yūgumo Kai | DD | Yūgumo Class Retrofit | 10 | Destroyer | 1945 | 0 | 30000 | 96 | 3400000 | 300 | Ultimate Kagero | Ultimate upgrade, maximum systems | Ultimate Upgrade | +65% capability, peak performance | Ultimate Kagero refinement |
| 4738 | Japanese | Akizuki Kai | DD | Akizuki Class Retrofit | 10 | Destroyer | 1945 | 0 | 38000 | 102 | 4200000 | 315 | AA ultimate | Maximum AA capability, radar | AA Ultimate | +90% AA capability, maximum | Ultimate AA destroyer |
| 4739 | Japanese | Shimakaze Kai | DD | Shimakaze Class Retrofit | 10 | Destroyer | 1945 | 0 | 55000 | 84 | 5500000 | 285 | Ultimate destroyer | Maximum speed + firepower + torpedoes | Ultimate Performance | +120% capability, LEGENDARY performance | Ultimate destroyer performance |
| 4740 | Japanese | Experimental DD-1 | DD | Experimental Type A | 9 | Destroyer | 1944 | 0 | 45000 | 84 | 4500000 | 270 | Experimental systems | PAPER! Advanced radar, guidance systems | Experimental Tech | Advanced systems, -25% reliability, PAPER | Experimental destroyer concepts |
| 4741 | Japanese | Experimental DD-2 | DD | Experimental Type B | 9 | Destroyer | 1945 | 0 | 48000 | 90 | 4800000 | 285 | Advanced propulsion | PAPER! 42 knots planned, experimental | Advanced Propulsion | 42 knots, -30% reliability, PAPER | Experimental propulsion |
| 4742 | Japanese | Super Akizuki | DD | Super Akizuki Class | 10 | Destroyer | 1945 | 0 | 55000 | 108 | 5500000 | 330 | Ultimate AA | PAPER! 10×3.9" guns, ultimate AA | Ultimate AA Design | 10×3.9" guns, -25% reliability, PAPER | Ultimate AA design |
| 4743 | Japanese | Hybrid DD | DD | Destroyer-Submarine Hybrid | 10 | Destroyer | 1944 | 0 | 60000 | 96 | 6000000 | 300 | Hybrid concept | PAPER! Submersible destroyer concept | Hybrid Technology | Submersible capability, -40% reliability, PAPER | Experimental hybrid concept |
| 4744 | Japanese | Ultimate Type | DD | Ultimate Destroyer | 10 | Destroyer | 1970 | 0 | 80000 | 120 | 8000000 | 360 | Theoretical ultimate | PAPER! All technologies combined | Ultimate Design | Maximum everything, -35% reliability, PAPER | Theoretical ultimate destroyer |
| 4800 | Japanese | No. 6 Class | SS | Early Development | 3 | Submarine | 1905 | 1 | 0 | 30 | 0 | 60 | Early submarine | FREE! 5 subs, 105 tons, 1×45cm torpedo tube | Early Submarine | Basic submarine, FREE starting ship | Pre-WWI design |
| 4801 | Japanese | L-1 Class | SS | Early Development | 4 | Submarine | 1918 | 0 | 5000 | 60 | 500000 | 90 | WWI design | 5 subs, 330 tons, 4 torpedo tubes, 14 kts | WWI Submarine | Basic fleet submarine | WWI era design |
| 4802 | Japanese | L-4 Class | SS | Early Development | 5 | Submarine | 1920 | 1 | 8000 | 90 | 800000 | 120 | Post-WWI | FREE! 3 subs, 620 tons, 4 torpedo tubes, 14.5 kts | Post-WWI Design | Larger design, FREE starting ship | Post-WWI improvement |
| 4803 | Japanese | Kaidai Type I | SS | Kaidai Fleet Submarines | 6 | Submarine | 1922 | 0 | 10000 | 120 | 1500000 | 150 | First fleet type | KD1, 1,100 tons, 6 torpedo tubes, 8×53cm torpedoes | First Fleet Type | Ocean-going capability | First Kaidai design |
| 4804 | Japanese | Kaidai Type II | SS | Kaidai Fleet Submarines | 6 | Submarine | 1925 | 0 | 12000 | 135 | 1800000 | 165 | Improved fleet | KD2, 1,400 tons, improved range | Improved Fleet | +25% range | Improved Kaidai |
| 4805 | Japanese | Kaidai Type III | SS | Kaidai Fleet Submarines | 7 | Submarine | 1927 | 0 | 15000 | 150 | 2200000 | 180 | Enhanced design | KD3, 1,635 tons, 6 torpedo tubes, 14 torpedoes | Enhanced Design | More torpedoes, +30% capability | Enhanced Kaidai |
| 4806 | Japanese | Kaidai Type IV | SS | Kaidai Fleet Submarines | 7 | Submarine | 1929 | 0 | 18000 | 165 | 2500000 | 195 | Further improved | KD4, 1,720 tons, 8 torpedo tubes | More Tubes | 8 torpedo tubes, +40% firepower | Further improved |
| 4807 | Japanese | Kaidai Type V | SS | Kaidai Fleet Submarines | 8 | Submarine | 1932 | 0 | 20000 | 180 | 3000000 | 210 | Pre-war standard | KD5, 1,800 tons, 8 torpedo tubes, Type 95 torpedoes | Type 95 Torpedoes | Type 95 oxygen torpedoes, +50% torpedo power | Type 95 torpedoes |
| 4808 | Japanese | Kaidai Type VI | SS | Kaidai Fleet Submarines | 8 | Submarine | 1934 | 0 | 22000 | 195 | 3500000 | 225 | Advanced fleet | KD6, 1,900 tons, improved performance | Advanced Fleet | +55% overall capability | Advanced Kaidai |
| 4809 | Japanese | Kaidai Type VII | SS | Kaidai Fleet Submarines | 9 | Submarine | 1937 | 0 | 25000 | 210 | 4000000 | 240 | Final Kaidai | KD7, 2,180 tons, peak conventional design | Peak Conventional | +60% capability, peak Kaidai | Final Kaidai type |
| 4810 | Japanese | Junsen Type I | SS | Junsen Cruiser Submarines | 7 | Cruiser Submarine | 1926 | 0 | 15000 | 180 | 3500000 | 180 | Cruiser submarine | J1, 2,135 tons, 1 aircraft, 6 torpedo tubes | Cruiser Submarine | 1 aircraft, +40% reconnaissance | First cruiser submarine |
| 4811 | Japanese | Junsen Type II | SS | Junsen Cruiser Submarines | 8 | Cruiser Submarine | 1932 | 0 | 20000 | 210 | 4500000 | 210 | Improved cruiser | J2, 2,525 tons, 1 aircraft, 17 knots surface | Improved Cruiser | +50% capability, 17 kts | Improved cruiser type |
| 4812 | Japanese | Junsen Type III | SS | Junsen Cruiser Submarines | 9 | Cruiser Submarine | 1937 | 0 | 25000 | 240 | 5500000 | 240 | Advanced cruiser | J3, 2,890 tons, 1 aircraft, 8 torpedo tubes | Advanced Cruiser | +60% capability, 8 tubes | Advanced cruiser type |
| 4813 | Japanese | Type A (I-9) | SS | Type A/B/C Fleet | 9 | Fleet Submarine | 1938 | 0 | 30000 | 270 | 6000000 | 270 | Fleet submarine | 2,934 tons, 1 aircraft, 6 torpedo tubes, 23.5 kts | Fast Fleet Type | 23.5 knots, +65% capability | Type A fleet submarine |
| 4814 | Japanese | Type B (I-15) | SS | Type A/B/C Fleet | 9 | Fleet Submarine | 1939 | 0 | 32000 | 285 | 6500000 | 285 | Standard fleet | 2,584 tons, 1 aircraft, 6 torpedo tubes, 17 torpedoes | Standard Fleet | 17 torpedoes, +70% capability | Type B standard type |
| 4815 | Japanese | Type C (I-16) | SS | Type A/B/C Fleet | 9 | Fleet Submarine | 1938 | 0 | 28000 | 270 | 5800000 | 270 | Fast fleet | 2,184 tons, 1 aircraft, 8 torpedo tubes, 23.6 kts | Fast Design | 23.6 knots, +65% speed | Type C fast type |
| 4816 | Japanese | Type B Kai (I-54) | SS | Type A/B/C Fleet | 9 | Fleet Submarine | 1942 | 0 | 35000 | 300 | 7000000 | 300 | Improved B | 2,607 tons, improved systems, wartime production | Improved Type B | +75% capability, wartime | Improved Type B |
| 4817 | Japanese | Type C Kai (I-52) | SS | Type A/B/C Fleet | 9 | Fleet Submarine | 1943 | 0 | 33000 | 285 | 6800000 | 285 | Improved C | 2,095 tons, enhanced operations | Improved Type C | +70% capability, enhanced | Improved Type C |
| 4818 | Japanese | I-400 (Sen-Toku) | SS | Sen-Toku Aircraft Carriers | 10 | Submarine Aircraft Carrier | 1943 | 0 | 100000 | 360 | 25000000 | 360 | SUBMARINE CARRIER | 122m, 5,900 tons, 3 AIRCRAFT! 8 torpedo tubes, LEGENDARY | Submarine Carrier | 3 aircraft, +100% capability, LARGEST UNTIL 1965, LEGENDARY | Largest submarine until nuclear age |
| 4819 | Japanese | I-201 (Sen-Taka) | SS | Sen-Taka High-Speed | 10 | High-Speed Submarine | 1944 | 0 | 80000 | 300 | 18000000 | 300 | FASTEST EVER | 19 knots submerged! 1,291 tons, 4 torpedo tubes, REVOLUTIONARY | Fastest Submarine | 19 knots submerged, +90% speed, REVOLUTIONARY | Fastest WWII submarine |
| 4820 | Japanese | RO-33 Class (K6) | SS | RO-Class Medium | 7 | Medium Submarine | 1935 | 0 | 18000 | 165 | 2500000 | 165 | Medium submarine | 960 tons, 4 torpedo tubes, 10 Type 95 torpedoes | Medium Type | Type 95 torpedoes, +45% capability | Medium submarine |
| 4821 | Japanese | RO-35 Class (K7) | SS | RO-Class Medium | 8 | Medium Submarine | 1943 | 0 | 22000 | 195 | 3200000 | 195 | Wartime medium | 1,115 tons, improved endurance | Wartime Medium | +50% endurance, improved | Wartime medium type |
| 4822 | Japanese | RO-100 Class | SS | RO-Class Medium | 8 | Coastal Submarine | 1942 | 0 | 20000 | 180 | 3000000 | 180 | Coastal defense | 601 tons, 4 torpedo tubes, simplified | Coastal Defense | Simplified design, +40% production | Coastal defense type |
| 4823 | Japanese | Ko-Hyoteki (Type A) | SS | Midget Submarines | 7 | Midget Submarine | 1938 | 0 | 15000 | 90 | 800000 | 90 | Midget submarine | 46 tons, 2 torpedo tubes, Pearl Harbor attack | Pearl Harbor Type | Pearl Harbor attack, +35% stealth | Midget submarine |
| 4824 | Japanese | Kairyū (Type D) | SS | Midget Submarines | 8 | Midget Submarine | 1945 | 0 | 18000 | 120 | 1200000 | 120 | Improved midget | 19.3 tons, 2 torpedo tubes, 600 built | Mass Production | 600 built, +45% production | Mass-produced midget |
| 4825 | Japanese | Oyashio (1960) | SS | Post-War JMSDF | 8 | Modern Submarine | 1960 | 0 | 40000 | 270 | 12000000 | 270 | Post-war submarine | 1,139 tons, modern sonar, torpedo systems | Post-War Design | Modern systems, +60% capability | Post-war JMSDF |
| 4826 | Japanese | Hayashio Class | SS | Post-War JMSDF | 9 | Modern Submarine | 1960 | 0 | 45000 | 300 | 15000000 | 300 | Advanced JMSDF | 1,450 tons, improved performance | Advanced JMSDF | +70% capability, advanced systems | Advanced JMSDF |
| 4827 | Japanese | L-1 Kai | SS | Retrofit & Upgrade | 5 | Submarine | 1930 | 0 | 3000 | 75 | 400000 | 105 | Modernized WWI | Improved torpedoes, extended service life | Basic Retrofit | +20% capability over original | Modernized L-1 |
| 4828 | Japanese | L-4 Kai | SS | Retrofit & Upgrade | 6 | Submarine | 1935 | 0 | 5000 | 105 | 600000 | 135 | Enhanced post-WWI | Better systems, +25% capability | Enhanced Systems | +25% capability, improved | Enhanced L-4 |
| 4829 | Japanese | Kaidai I Kai | SS | Retrofit & Upgrade | 7 | Submarine | 1935 | 0 | 8000 | 135 | 1200000 | 165 | Upgraded fleet | Improved torpedoes, radar | Radar Equipped | Radar, +30% detection | Upgraded Kaidai I |
| 4830 | Japanese | Kaidai II Kai | SS | Retrofit & Upgrade | 7 | Submarine | 1938 | 0 | 10000 | 150 | 1500000 | 180 | Enhanced KD2 | Type 95 torpedoes, modern systems | Type 95 Upgrade | Type 95 torpedoes, +40% power | Enhanced Kaidai II |
| 4831 | Japanese | Kaidai III Kai | SS | Retrofit & Upgrade | 8 | Submarine | 1940 | 0 | 12000 | 165 | 1800000 | 195 | Modernized KD3 | Radar, improved performance | Modernized Systems | +45% capability, radar | Modernized Kaidai III |
| 4832 | Japanese | Junsen I Kai | SS | Retrofit & Upgrade | 8 | Cruiser Submarine | 1940 | 0 | 15000 | 195 | 3000000 | 210 | Upgraded cruiser | Enhanced aircraft ops, radar | Enhanced Aircraft | +50% aircraft ops, radar | Upgraded Junsen I |
| 4833 | Japanese | Type A Kai | SS | Retrofit & Upgrade | 10 | Fleet Submarine | 1944 | 0 | 28000 | 285 | 6500000 | 285 | Ultimate Type A | Maximum upgrades, radar, improved torpedoes | Ultimate Upgrade | +80% capability, maximum | Ultimate Type A |
| 4834 | Japanese | Type B Kai II | SS | Retrofit & Upgrade | 10 | Fleet Submarine | 1945 | 0 | 30000 | 300 | 7000000 | 300 | Maximum Type B | Peak performance, all upgrades | Maximum Performance | +85% capability, peak | Maximum Type B |
| 4835 | Japanese | RO-33 Kai | SS | Retrofit & Upgrade | 8 | Medium Submarine | 1943 | 0 | 18000 | 180 | 2800000 | 180 | Upgraded medium | Type 95 torpedoes, radar | Medium Upgrade | +50% capability, Type 95 | Upgraded RO-33 |
| 4836 | Japanese | Sen-Toku II | SS | Paper Designs | 10 | Submarine Aircraft Carrier | 1945 | 0 | 120000 | 390 | 30000000 | 390 | Improved I-400 | PAPER! 6,000+ tons, 4 aircraft planned, cancelled | 4 Aircraft Design | 4 aircraft, -25% reliability, PAPER | Improved I-400, cancelled |
| 4837 | Japanese | Super Sen-Taka | SS | Paper Designs | 10 | High-Speed Submarine | 1945 | 0 | 100000 | 330 | 22000000 | 330 | Ultimate speed | PAPER! 25 knots submerged planned, never built | Ultimate Speed | 25 knots planned, -30% reliability, PAPER | Ultimate speed design |
| 4838 | Japanese | Type D Fleet | SS | Paper Designs | 10 | Fleet Submarine | 1945 | 0 | 50000 | 270 | 10000000 | 270 | Simplified fleet | PAPER! Emergency design, cancelled | Emergency Design | Simplified, -20% reliability, PAPER | Emergency design |
| 4839 | Japanese | Nuclear Submarine | SS | Paper Designs | 10 | Nuclear Submarine | 1960 | 0 | 150000 | 420 | 50000000 | 420 | Nuclear power | PAPER! Theoretical nuclear design, never pursued | Nuclear Power | Never pursued, -35% reliability, PAPER | Theoretical nuclear |
| 4840 | Japanese | Hydrogen Peroxide Sub | SS | Paper Designs | 10 | Experimental Submarine | 1944 | 0 | 80000 | 300 | 16000000 | 300 | Walter turbine | PAPER! Experimental propulsion, abandoned | H2O2 Propulsion | Experimental, -40% reliability, PAPER | Walter turbine experiment |
| 4841 | Japanese | Ultimate Sen-Toku | SS | Paper Designs | 10 | Ultimate Submarine | 1970 | 0 | 200000 | 480 | 75000000 | 480 | Theoretical ultimate | PAPER! All technologies combined, never designed | Ultimate Design | Maximum everything, -40% reliability, PAPER | Theoretical ultimate |
| 4100 | Japanese | Hōshō | CV | Early Development | 5 | Aircraft Carrier | 1922 | 1 | 0 | 180 | 0 | 180 | FIRST PURPOSE-BUILT | FREE! World's first purpose-built carrier! 7,470 tons, 21 aircraft | First Purpose-Built | World's first purpose-built carrier, +50% innovation, FREE, LEGENDARY | First purpose-built carrier 1922 |
| 4101 | Japanese | Ryūjō | CV | Early Development | 7 | Light Carrier | 1931 | 0 | 15000 | 240 | 8000000 | 240 | Light carrier | 10,600 tons, 48 aircraft, 29 kts, unusual two-deck design | Unusual Design | Two-deck design, +40% aircraft, unusual | Light carrier, two decks |
| 4102 | Japanese | Akagi | CV | Treaty Conversions | 8 | Fleet Carrier | 1925 | 1 | 20000 | 300 | 12000000 | 300 | Pearl Harbor carrier | FREE! Converted battlecruiser, 36,500 tons, 66 aircraft, FAMOUS | Pearl Harbor Force | Pearl Harbor strike, +80% capability, FREE, FAMOUS | Pearl Harbor carrier |
| 4103 | Japanese | Kaga | CV | Treaty Conversions | 8 | Fleet Carrier | 1928 | 0 | 22000 | 315 | 13000000 | 315 | Pearl Harbor carrier | Converted battleship, 38,200 tons, 90 aircraft (most capacity!) | Highest Capacity | 90 aircraft, +85% capacity, most Japanese | Pearl Harbor, highest capacity |
| 4104 | Japanese | Sōryū | CV | Modern Fleet Carriers | 9 | Fleet Carrier | 1935 | 0 | 30000 | 330 | 15000000 | 330 | First modern design | 15,900 tons, 63 aircraft, 34 kts, first pure design since Hōshō | First Modern | First pure design since Hōshō, +70% capability | First modern purpose-built |
| 4105 | Japanese | Hiryū | CV | Modern Fleet Carriers | 9 | Fleet Carrier | 1937 | 0 | 35000 | 345 | 16000000 | 345 | Improved Sōryū | 17,300 tons, 64 aircraft, better armor (90-150mm), starboard island | Better Armor | 90-150mm armor, +75% protection, starboard island | Improved Sōryū, better armor |
| 4106 | Japanese | Shōkaku | CV | Modern Fleet Carriers | 10 | Fleet Carrier | 1939 | 0 | 45000 | 360 | 20000000 | 360 | BEST JAPANESE CARRIER | 25,675 tons, 72 aircraft, 34 kts, "best in the world" 1941, LEGENDARY | Best Japanese Carrier | Best in world 1941, +100% capability, LEGENDARY | Best Japanese carrier |
| 4107 | Japanese | Zuikaku | CV | Modern Fleet Carriers | 10 | Fleet Carrier | 1939 | 0 | 47000 | 375 | 21000000 | 375 | BEST JAPANESE CARRIER | 25,675 tons, 75 aircraft, last Pearl Harbor carrier sunk, LEGENDARY | Last Pearl Harbor Survivor | Last sunk, +105% capability, LEGENDARY | Last Pearl Harbor carrier sunk |
| 4108 | Japanese | Taihō | CV | Armored Fleet Carriers | 10 | Armored Carrier | 1941 | 0 | 60000 | 390 | 25000000 | 390 | ARMORED CARRIER | 29,300 tons, 75-80mm armored deck! 53 aircraft, torpedoed & exploded | Armored Flight Deck | 75-80mm armor, +90% protection, first armored | First Japanese armored carrier |
| 4109 | Japanese | Shinano | CV | Armored Fleet Carriers | 10 | Super Carrier | 1942 | 0 | 100000 | 420 | 50000000 | 420 | LARGEST CARRIER | 72,800 tons! Largest until USS Forrestal 1954! Converted Yamato-class, LEGENDARY | Largest Carrier | Largest until 1954, +120% capability, LEGENDARY | Largest carrier until 1954 |
| 4110 | Japanese | Unryū | CV | Wartime Emergency | 9 | Fleet Carrier | 1941 | 0 | 40000 | 345 | 18000000 | 345 | Wartime fleet carrier | 17,150 tons, 63 aircraft, Hiryū-based simplified design | Simplified Design | Hiryū-based, +70% capability, wartime | Simplified Hiryū-based |
| 4111 | Japanese | Amagi | CV | Wartime Emergency | 9 | Fleet Carrier | 1942 | 0 | 42000 | 360 | 19000000 | 360 | Unryū II | 18,300 tons, improved Unryū, capsized by airstrike Kure 1945 | Improved Unryū | +75% capability, improved | Improved Unryū type |
| 4112 | Japanese | Katsuragi | CV | Wartime Emergency | 9 | Fleet Carrier | 1943 | 0 | 44000 | 375 | 20000000 | 375 | Unryū III | 17,400 tons, completed but no aircraft/pilots/fuel | Completed Useless | No aircraft/pilots, +65% if supplied | Completed but unusable |
| 4113 | Japanese | Zuihō | CV | Light Fleet Carriers | 8 | Light Carrier | 1935 | 0 | 25000 | 270 | 10000000 | 270 | Light carrier | 11,262 tons, 30 aircraft, converted submarine tender | Light Carrier | Converted tender, +55% capability | Converted submarine tender |
| 4114 | Japanese | Shōhō | CV | Light Fleet Carriers | 8 | Light Carrier | 1939 | 0 | 27000 | 285 | 11000000 | 285 | Light carrier | 11,262 tons, 30 aircraft, sunk Coral Sea (first CV lost) | First CV Loss | First carrier lost, +55% capability | First carrier loss, Coral Sea |
| 4115 | Japanese | Ryūhō | CV | Light Fleet Carriers | 8 | Light Carrier | 1942 | 0 | 30000 | 300 | 12000000 | 300 | Light carrier | 13,360 tons, 31 aircraft, converted submarine tender | Converted Tender | +60% capability, submarine tender | Converted submarine tender |
| 4116 | Japanese | Chitose | CV | Light Fleet Carriers | 8 | Light Carrier | 1936 | 0 | 28000 | 285 | 11500000 | 285 | Light carrier | 11,190 tons, 30 aircraft, converted seaplane tender | Seaplane Conversion | Converted seaplane tender, +55% | Converted seaplane tender |
| 4117 | Japanese | Chiyoda | CV | Light Fleet Carriers | 8 | Light Carrier | 1937 | 0 | 29000 | 300 | 11800000 | 300 | Light carrier | 11,190 tons, 30 aircraft, converted seaplane tender | Seaplane Conversion | Converted tender, +58% capability | Converted seaplane tender |
| 4118 | Japanese | Taiyō | CV | Escort Carriers | 7 | Escort Carrier | 1940 | 0 | 20000 | 210 | 6000000 | 210 | Escort carrier | 17,830 tons, 27 aircraft, converted liner | Liner Conversion | Converted liner, +45% capability | Converted passenger liner |
| 4119 | Japanese | Un'yō | CV | Escort Carriers | 7 | Escort Carrier | 1941 | 0 | 22000 | 225 | 6500000 | 225 | Escort carrier | 17,830 tons, 27 aircraft, converted liner | Liner Conversion | Converted liner, +47% capability | Converted passenger liner |
| 4120 | Japanese | Chūyō | CV | Escort Carriers | 7 | Escort Carrier | 1942 | 0 | 24000 | 240 | 7000000 | 240 | Escort carrier | 17,830 tons, 30 aircraft, converted liner | Liner Conversion | Converted liner, +50% aircraft | Converted passenger liner |
| 4121 | Japanese | Shin'yō | CV | Escort Carriers | 7 | Escort Carrier | 1941 | 0 | 21000 | 220 | 6200000 | 220 | Escort carrier | 17,500 tons, 33 aircraft, captured German liner | Captured Liner | Captured German liner, +50% | Captured German liner |
| 4122 | Japanese | Kaiyō | CV | Escort Carriers | 8 | Escort Carrier | 1943 | 0 | 26000 | 255 | 7500000 | 255 | Improved escort | 13,600 tons, 24 aircraft, converted liner, improved | Improved Escort | Improved design, +52% capability | Improved escort design |
| 4123 | Japanese | Shimane Maru | CV | Escort Carriers | 7 | Escort Carrier | 1944 | 0 | 23000 | 230 | 6800000 | 230 | Emergency escort | 11,800 tons, 24 aircraft, simplified emergency | Emergency Design | Simplified emergency, +48% | Emergency escort design |
| 4124 | Japanese | Theoretical 1955 | CV | Post-War JMSDF | 8 | Carrier | 1955 | 0 | 50000 | 360 | 25000000 | 360 | Post-war theoretical | Post-war carrier concept, never pursued | Post-War Concept | Never pursued, -20% reliability | Post-war concept |
| 4125 | Japanese | Helicopter Carrier | CV | Post-War JMSDF | 9 | Helicopter Carrier | 1960 | 0 | 60000 | 390 | 30000000 | 390 | Helicopter carrier | Modern helicopter operations, ASW focus | Helicopter Ops | ASW focus, +65% ASW capability | Modern helicopter carrier |
| 4126 | Japanese | Hōshō Kai | CV | Retrofit & Upgrade | 6 | Aircraft Carrier | 1935 | 0 | 8000 | 195 | 4000000 | 195 | Modernized first carrier | Improved aircraft ops, extended life | Basic Modernization | +30% capability over original | Modernized Hōshō |
| 4127 | Japanese | Akagi Kai | CV | Retrofit & Upgrade | 9 | Fleet Carrier | 1935 | 0 | 18000 | 315 | 10000000 | 315 | Major rebuild | Single flight deck, island added, +100% capability | Major Rebuild | Single deck, island, +100% capability | Major 1935 rebuild |
| 4128 | Japanese | Kaga Kai | CV | Retrofit & Upgrade | 9 | Fleet Carrier | 1934 | 0 | 19000 | 330 | 11000000 | 330 | Major rebuild | Reconstructed, improved aircraft capacity | Major Reconstruction | +105% capability, reconstructed | Major 1934 rebuild |
| 4129 | Japanese | Ryūjō Kai | CV | Retrofit & Upgrade | 8 | Light Carrier | 1934 | 0 | 12000 | 255 | 7000000 | 255 | Stability improved | Hull reinforced, ballasts added, +40% stability | Stability Fixed | Hull reinforced, +40% stability | 1934 stability upgrade |
| 4130 | Japanese | Sōryū Kai | CV | Retrofit & Upgrade | 10 | Fleet Carrier | 1941 | 0 | 28000 | 345 | 14000000 | 345 | Enhanced operations | Improved systems, radar, +50% capability | Enhanced Systems | Radar, +50% capability | Enhanced operations |
| 4131 | Japanese | Hiryū Kai | CV | Retrofit & Upgrade | 10 | Fleet Carrier | 1942 | 0 | 32000 | 360 | 15000000 | 360 | Ultimate upgrade | Maximum upgrades, radar, improved aircraft | Ultimate Upgrade | +90% capability, maximum | Ultimate upgrade |
| 4132 | Japanese | Shōkaku Kai | CV | Retrofit & Upgrade | 10 | Fleet Carrier | 1943 | 0 | 40000 | 375 | 19000000 | 375 | Enhanced best carrier | Enhanced systems, +60% capability | Enhanced Best | +110% capability, enhanced | Enhanced Shōkaku |
| 4133 | Japanese | Zuikaku Kai | CV | Retrofit & Upgrade | 10 | Fleet Carrier | 1944 | 0 | 42000 | 390 | 20000000 | 390 | Ultimate best carrier | Maximum systems, +70% capability, peak performance | Ultimate Best | +120% capability, peak, ULTIMATE | Ultimate Zuikaku |
| 4134 | Japanese | Zuihō Kai | CV | Retrofit & Upgrade | 9 | Light Carrier | 1943 | 0 | 24000 | 300 | 11000000 | 300 | Enhanced light | Improved aircraft ops, +45% capability | Enhanced Light | +70% capability, improved | Enhanced Zuihō |
| 4135 | Japanese | Chitose Kai | CV | Retrofit & Upgrade | 9 | Light Carrier | 1943 | 0 | 26000 | 315 | 12000000 | 315 | Enhanced conversion | Better systems, +50% capability | Enhanced Conversion | +75% capability, better systems | Enhanced Chitose |
| 4136 | Japanese | Kasagi (Unryū IV) | CV | Paper Designs | 9 | Fleet Carrier | 1943 | 0 | 50000 | 390 | 22000000 | 390 | Unryū class | PAPER! Launched but never completed, scrapped 1947 | Launched Incomplete | Launched, never completed, -25% reliability, PAPER | Launched, never completed |
| 4137 | Japanese | Aso (Unryū V) | CV | Paper Designs | 9 | Fleet Carrier | 1943 | 0 | 52000 | 405 | 23000000 | 405 | Unryū class | PAPER! 85% complete, never finished, scrapped | 85% Complete | 85% complete, -30% reliability, PAPER | 85% complete, scrapped |
| 4138 | Japanese | Ikoma (Unryū VI) | CV | Paper Designs | 9 | Fleet Carrier | 1944 | 0 | 48000 | 390 | 21000000 | 390 | Unryū class | PAPER! Cancelled, scrapped on slip 1946 | Cancelled On Slip | Cancelled, -35% reliability, PAPER | Cancelled, scrapped on slip |
| 4139 | Japanese | G15 Project | CV | Paper Designs | 10 | Super Carrier | 1942 | 0 | 80000 | 420 | 40000000 | 420 | Super carrier | PAPER! 50,000+ tons planned, armored, never built | Super Carrier Design | 50,000+ tons, -30% reliability, PAPER | Super carrier project |
| 4140 | Japanese | Improved Taihō | CV | Paper Designs | 10 | Armored Carrier | 1943 | 0 | 75000 | 405 | 35000000 | 405 | Armored carrier | PAPER! Improved Taihō design, never built | Improved Armored | Improved Taihō, -28% reliability, PAPER | Improved Taihō design |
| 4141 | Japanese | Second Shinano | CV | Paper Designs | 10 | Super Carrier | 1944 | 0 | 120000 | 450 | 60000000 | 450 | Super carrier | PAPER! Second converted Yamato, cancelled | Second Yamato Conversion | Second Yamato, -35% reliability, PAPER | Second converted Yamato |
| 4142 | Japanese | Nuclear Carrier | CV | Paper Designs | 10 | Nuclear Carrier | 1960 | 0 | 150000 | 480 | 80000000 | 480 | Nuclear power | PAPER! Theoretical nuclear carrier, never pursued | Nuclear Power | Never pursued, -40% reliability, PAPER | Theoretical nuclear carrier |
| 4143 | Japanese | Super Shinano | CV | Paper Designs | 10 | Super Carrier | 1945 | 0 | 140000 | 465 | 70000000 | 465 | Ultimate carrier | PAPER! 80,000+ tons planned, never designed | Ultimate Design | 80,000+ tons, -35% reliability, PAPER | Ultimate carrier design |
| 4144 | Japanese | Ultimate Design | CV | Paper Designs | 10 | Ultimate Carrier | 1970 | 0 | 200000 | 540 | 100000000 | 540 | Theoretical ultimate | PAPER! All technologies combined, theoretical | Ultimate Everything | Maximum everything, -40% reliability, PAPER | Theoretical ultimate |

| 1000 | USA | Whitehead Torpedo (1890) | Steam | Torpedoes | 1 | Torpedo | 1890 | 1 | 0 | 0 | 0 | 0 | STARTING | FREE! Licensed from Whitehead, first US torpedo | Steam Torpedo |  | STARTING |
| 1001 | USA | Howell Torpedo | Flywheel | Torpedoes | 2 | Torpedo | 1889 | 0 | 50000 | 1 | 100000 | 1 | EXPERIMENTAL | Unique flywheel propulsion, wakeless, counter-rotating flywheel | Flywheel Torpedo |  | EXPERIMENTAL |
| 1002 | USA | Whitehead Mark 1 | Steam | Torpedoes | 2 | Torpedo | 1892 | 0 | 75000 | 2 | 150000 | 2 | Early Steam | Improved Whitehead design, 18" diameter, limited range | Steam Torpedo |  | Early Steam |
| 1003 | USA | Bliss-Leavitt Mark 1 | Steam | Torpedoes | 3 | Torpedo | 1904 | 0 | 120000 | 2 | 240000 | 2 | Pre-WWI | First successful US-manufactured torpedo, 18" diameter | Steam Torpedo |  | Pre-WWI |
| 1004 | USA | Bliss-Leavitt Mark 3 | Steam | Torpedoes | 3 | Torpedo | 1908 | 0 | 150000 | 2 | 300000 | 2 | Pre-WWI | Improved reliability, 21" diameter introduced | Steam Torpedo |  | Pre-WWI |
| 1005 | USA | Mark 7 | Steam | Torpedoes | 4 | Torpedo | 1912 | 0 | 200000 | 3 | 400000 | 3 | WWI Era | Standard destroyer torpedo, 21" × 21 ft, 400 lbs TNT | Steam Torpedo |  | WWI Era |
| 1006 | USA | Mark 8 | Steam | Torpedoes | 4 | Torpedo | 1915 | 0 | 250000 | 3 | 500000 | 3 | WWI Submarine | First dedicated submarine torpedo, 21" × 16 ft | Steam Torpedo |  | WWI Submarine |
| 1007 | USA | Mark 9 | Steam | Torpedoes | 5 | Torpedo | 1916 | 0 | 300000 | 4 | 600000 | 4 | WWI Heavy | Battleship/cruiser torpedo, 21" × 24 ft, longer range | Steam Torpedo |  | WWI Heavy |
| 1008 | USA | Mark 10 | Steam | Torpedoes | 5 | Torpedo | 1920 | 0 | 350000 | 4 | 700000 | 4 | Post-WWI | Improved Mark 8, better gyroscope, 21" × 16 ft | Steam Torpedo |  | Post-WWI |
| 1009 | USA | Mark 11 | Steam | Torpedoes | 5 | Torpedo | 1922 | 0 | 400000 | 5 | 800000 | 5 | Treaty Era | Surface ship torpedo, wet-heater engine, 3,500 yd range | Steam Torpedo |  | Treaty Era |
| 1010 | USA | Mark 12 | Steam | Torpedoes | 6 | Torpedo | 1927 | 0 | 450000 | 5 | 900000 | 5 | Interwar | Destroyer torpedo, improved speed 36 kts | Steam Torpedo |  | Interwar |
| 1011 | USA | Mark 13 (Early) | Steam | Torpedoes | 6 | Torpedo | 1938 | 0 | 500000 | 4 | 1000000 | 4 | AIR-LAUNCHED | First successful US aerial torpedo, 22.4" × 13.5 ft | Steam Torpedo |  | AIR-LAUNCHED |
| 1012 | USA | Mark 14 Mod 0 | Steam | Torpedoes | 7 | Torpedo | 1931 | 0 | 600000 | 6 | 1200000 | 6 | SUBMARINE PRIMARY | 21" × 20.5 ft, 643 lbs Torpex, DEPTH CONTROL ISSUES | Steam Torpedo |  | SUBMARINE PRIMARY |
| 1013 | USA | Mark 15 Mod 0 | Steam | Torpedoes | 7 | Torpedo | 1938 | 0 | 650000 | 6 | 1300000 | 6 | SURFACE SHIP | Fletcher-class destroyer torpedo, 21" × 24 ft, 825 lbs warhead | Steam Torpedo |  | SURFACE SHIP |
| 1014 | USA | Mark 14 Mod 3 (Depth Fix) | Steam | Torpedoes | 7 | Torpedo | 1942 | 0 | 800000 | 3 | 1600000 | 3 | CRISIS FIX 1/3 | Depth control mechanism fixed, runs at correct depth | Steam Torpedo |  | CRISIS FIX 1/3 |
| 1015 | USA | Mark 14 Mod 4 (Magnetic Fix) | Steam | Torpedoes | 7 | Torpedo | 1943 | 0 | 900000 | 2 | 1800000 | 2 | CRISIS FIX 2/3 | Magnetic exploder deactivated, contact only | Steam Torpedo |  | CRISIS FIX 2/3 |
| 1016 | USA | Mark 14 Mod 5 (Contact Fix) | Steam | Torpedoes | 8 | Torpedo | 1943 | 0 | 1000000 | 2 | 2000000 | 2 | CRISIS RESOLVED | Contact exploder redesigned, FULLY FUNCTIONAL | Steam Torpedo |  | CRISIS RESOLVED |
| 1017 | USA | Mark 13 Mod 1 (Improved) | Steam | Torpedoes | 7 | Torpedo | 1942 | 0 | 700000 | 4 | 1400000 | 4 | Air Torpedo | Drag ring added, drop height increased to 800 ft | Steam Torpedo |  | Air Torpedo |
| 1018 | USA | Mark 13 Mod 2 (Final) | Steam | Torpedoes | 8 | Torpedo | 1944 | 0 | 900000 | 3 | 1800000 | 3 | Air Optimized | Pickle barrel fins, 2,400 yd range, 600 lbs Torpex | Steam Torpedo |  | Air Optimized |
| 1019 | USA | Mark 15 Mod 3 | Steam | Torpedoes | 8 | Torpedo | 1944 | 0 | 1100000 | 5 | 2200000 | 5 | Late-War Surface | Increased speed 45 kts, 6,000 yd range | Steam Torpedo |  | Late-War Surface |
| 1020 | USA | Mark 16 | Steam | Torpedoes | 8 | Torpedo | 1943 | 0 | 950000 | 5 | 1900000 | 5 | Submarine Heavy | Longer range 11,000 yd, slower 46 kts, same warhead | Steam Torpedo |  | Submarine Heavy |
| 1021 | USA | Mark 17 | Steam | Torpedoes | 8 | Torpedo | 1943 | 0 | 850000 | 4 | 1700000 | 4 | Submarine Light | Reduced warhead 300 lbs, 16,000 yd range | Steam Torpedo |  | Submarine Light |
| 1022 | USA | Mark 18 | Electric | Torpedoes | 8 | Torpedo | 1943 | 0 | 1200000 | 6 | 2400000 | 6 | WAKELESS | First US electric torpedo, battery-powered, 29 kts, 4,000 yd | Electric Torpedo |  | WAKELESS |
| 1023 | USA | Mark 24 "Fido" | Acoustic | Torpedoes | 9 | Torpedo | 1943 | 0 | 2000000 | 8 | 4000000 | 8 | FIRST HOMING | Air-dropped ASW, passive acoustic homing, 12 kts, 3,900 ft depth | Acoustic Torpedo |  | FIRST HOMING |
| 1024 | USA | Mark 27 | Acoustic | Torpedoes | 9 | Torpedo | 1945 | 0 | 2200000 | 7 | 4400000 | 7 | Submarine ASW | Submarine-launched acoustic homing, 12 kts | Acoustic Torpedo |  | Submarine ASW |
| 1025 | USA | Mark 28 | Acoustic | Torpedoes | 9 | Torpedo | 1946 | 0 | 2400000 | 8 | 4800000 | 8 | Surface ASW | Surface-launched ASW torpedo, shallow water optimized | Acoustic Torpedo |  | Surface ASW |
| 1026 | USA | Mark 32 | Electric | Torpedoes | 9 | Torpedo | 1946 | 0 | 2600000 | 9 | 5200000 | 9 | Post-War Sub | Improved Mark 18, 35 kts, 8,000 yd range | Electric Torpedo |  | Post-War Sub |
| 1027 | USA | Mark 35 | Acoustic | Torpedoes | 9 | Torpedo | 1949 | 0 | 2800000 | 10 | 5600000 | 10 | Deep ASW | Deep-diving ASW torpedo, 17 kts, active/passive sonar | Acoustic Torpedo |  | Deep ASW |
| 1028 | USA | Mark 37 | Acoustic | Torpedoes | 10 | Torpedo | 1956 | 0 | 3500000 | 12 | 7000000 | 12 | HEAVYWEIGHT | 19" × 11.3 ft, active/passive homing, 26 kts, 11,000 yd | Acoustic Torpedo |  | HEAVYWEIGHT |
| 1029 | USA | Mark 39 (Mod Mark 37) | Acoustic | Torpedoes | 10 | Torpedo | 1957 | 0 | 3200000 | 10 | 6400000 | 10 | Mod 37 | Nuclear warhead variant (W34, 10 kt yield) for ASW | Acoustic Torpedo |  | Mod 37 |
| 1030 | USA | Mark 41 | Acoustic | Torpedoes | 10 | Torpedo | 1957 | 0 | 3300000 | 11 | 6600000 | 11 | ASW Specialist | Air-dropped, 5,500 yd range, wire-guided option | Acoustic Torpedo |  | ASW Specialist |
| 1031 | USA | Mark 43 | Acoustic | Torpedoes | 9 | Torpedo | 1961 | 0 | 3000000 | 9 | 6000000 | 9 | Lightweight | Air/surface launch, 10.75" × 8.3 ft, 4,500 yd range | Acoustic Torpedo |  | Lightweight |
| 1032 | USA | Mark 44 | Acoustic | Torpedoes | 9 | Torpedo | 1962 | 0 | 3100000 | 10 | 6200000 | 10 | ASW Standard | Replaced Mark 43, active/passive sonar, 30 kts | Acoustic Torpedo |  | ASW Standard |
| 1033 | USA | Mark 45 ASTOR | Nuclear | Torpedoes | 10 | Torpedo | 1963 | 0 | 5000000 | 16 | 10000000 | 16 | NUCLEAR ASW | 19" torpedo, W34 warhead, 11 kt yield, ASROC-delivered | Nuclear Torpedo |  | NUCLEAR ASW |
| 1034 | USA | Mark 46 Mod 0 | Acoustic | Torpedoes | 9 | Torpedo | 1965 | 0 | 3400000 | 10 | 6800000 | 10 | LIGHTWEIGHT STANDARD | 12.75" × 8.5 ft, 45 kts, 5,500 yd, active/passive | Acoustic Torpedo |  | LIGHTWEIGHT STANDARD |
| 1035 | USA | Mark 46 Mod 1 | Acoustic | Torpedoes | 9 | Torpedo | 1967 | 0 | 3500000 | 9 | 7000000 | 9 | Improved Seeker | Better shallow water performance, counter-countermeasures | Acoustic Torpedo |  | Improved Seeker |
| 1036 | USA | Mark 46 Mod 2 | Acoustic | Torpedoes | 9 | Torpedo | 1972 | 0 | 3600000 | 9 | 7200000 | 9 | Deep Capable | Increased depth capability to 1,500 ft | Acoustic Torpedo |  | Deep Capable |
| 1037 | USA | Mark 46 Mod 5 | Acoustic | Torpedoes | 10 | Torpedo | 1979 | 0 | 4000000 | 10 | 8000000 | 10 | NEARTIP | Near-Term Improvement Program, digital processing | Acoustic Torpedo |  | NEARTIP |
| 1038 | USA | Mark 48 Mod 0 | Wire-Guided | Torpedoes | 10 | Torpedo | 1972 | 0 | 8000000 | 18 | 16000000 | 18 | HEAVYWEIGHT STANDARD | 21" × 19 ft, wire-guided, active/passive, 55 kts, 38,000 yd | Wire-Guided Torpedo |  | HEAVYWEIGHT STANDARD |
| 1039 | USA | Mark 48 Mod 1 | Wire-Guided | Torpedoes | 10 | Torpedo | 1975 | 0 | 8500000 | 16 | 17000000 | 16 | ADCAP Development | Advanced Capability, improved guidance | Wire-Guided Torpedo |  | ADCAP Development |
| 1040 | USA | Mark 48 Mod 3 | Wire-Guided | Torpedoes | 10 | Torpedo | 1977 | 0 | 9000000 | 16 | 18000000 | 16 | Range Extension | 28,000 yd at 55 kts, 50,000 yd at 40 kts | Wire-Guided Torpedo |  | Range Extension |
| 1041 | USA | Mark 48 ADCAP (Mod 4) | Wire-Guided | Torpedoes | 10 | Torpedo | 1985 | 0 | 12000000 | 20 | 24000000 | 20 | ADVANCED CAPABILITY | Digital guidance, under-ice capable, deeper diving | Wire-Guided Torpedo |  | ADVANCED CAPABILITY |
| 1042 | USA | Mark 48 ADCAP (Mod 5) | Wire-Guided | Torpedoes | 10 | Torpedo | 1988 | 0 | 13000000 | 18 | 26000000 | 18 | Modern Standard | Improved processing, multi-target engagement, 1,200 lb warhead | Wire-Guided Torpedo |  | Modern Standard |
| 1043 | USA | Mark 48 ADCAP (Mod 6) | Wire-Guided | Torpedoes | 10 | Torpedo | 1990 | 0 | 14000000 | 20 | 28000000 | 20 | CURRENT VARIANT | Enhanced countermeasures, shallow water, 65 kts rumored | Wire-Guided Torpedo |  | CURRENT VARIANT |
| 1044 | USA | Mark 50 | Acoustic | Torpedoes | 10 | Torpedo | 1989 | 0 | 6000000 | 14 | 12000000 | 14 | LIGHTWEIGHT ADVANCED | 12.75", stored chemical energy propulsion, 60+ kts | Acoustic Torpedo |  | LIGHTWEIGHT ADVANCED |
| 1045 | USA | Mark 46 Mod 5A(S) | Acoustic | Torpedoes | 10 | Torpedo | 1987 | 0 | 4200000 | 10 | 8400000 | 10 | Surface Variant | Shallow water optimized, surface ship use | Acoustic Torpedo |  | Surface Variant |
| 1046 | USA | Mark 46 NEARTIP Mod 5A/S | Acoustic | Torpedoes | 10 | Torpedo | 1989 | 0 | 4500000 | 11 | 9000000 | 11 | Final Mod 5 | Ultimate Mark 46 variant, digital seeker | Acoustic Torpedo |  | Final Mod 5 |
| 1047 | USA | Mark 37C | Acoustic | Torpedoes | 10 | Torpedo | 1960 | 0 | 3700000 | 12 | 7400000 | 12 | Export Variant | Downgraded Mark 37 for allied navies | Acoustic Torpedo |  | Export Variant |
| 1048 | USA | Mark 48 Mod 4 (Export) | Wire-Guided | Torpedoes | 10 | Torpedo | 1986 | 0 | 10000000 | 18 | 20000000 | 18 | Allied Export | Reduced performance for NATO allies | Wire-Guided Torpedo |  | Allied Export |
| 1049 | USA | Mark 60 CAPTOR | Mine-Torpedo | Torpedoes | 10 | Torpedo | 1979 | 0 | 5000000 | 16 | 10000000 | 16 | ENCAPSULATED | Mark 46 torpedo in mine casing, submarine detection trigger | Mine-Torpedo Torpedo |  | ENCAPSULATED |
| 1050 | USA | ALWT (Advanced Lightweight) | Acoustic | Torpedoes | 10 | Torpedo | 1985 | 0 | 7000000 | 18 | 14000000 | 18 | R&D PROGRAM | Development program (became Mark 50), stored energy | Acoustic Torpedo |  | R&D PROGRAM |
| 1051 | USA | Mark 51 | Acoustic | Torpedoes | 10 | Torpedo | 1960 | 0 | 4000000 | 12 | 8000000 | 12 | CANCELLED | Lightweight ASW, cancelled in favor of Mark 44 | Acoustic Torpedo |  | CANCELLED |
| 1052 | USA | Mark 52 | Electric | Torpedoes | 10 | Torpedo | 1965 | 0 | 4500000 | 14 | 9000000 | 14 | PAPER DESIGN | Improved Mark 48 concept, not produced | Electric Torpedo |  | PAPER DESIGN |
| 1053 | USA | Mark 53 | Wire-Guided | Torpedoes | 10 | Torpedo | 1970 | 0 | 5000000 | 16 | 10000000 | 16 | PROTOTYPE ONLY | Experimental guidance system, 2 built | Wire-Guided Torpedo |  | PROTOTYPE ONLY |
| 1054 | USA | Mark 25 "Atomic Astor" | Nuclear | Torpedoes | 10 | Torpedo | 1945 | 0 | 8000000 | 24 | 16000000 | 24 | CONCEPT | Post-war nuclear torpedo concept, not developed | Nuclear Torpedo |  | CONCEPT |
| 1055 | USA | Mark 30 | Exercise | Torpedoes | 6 | Torpedo | 1945 | 0 | 100000 | 2 | 200000 | 2 | TRAINING | Exercise torpedo, recoverable, no warhead | Exercise Torpedo |  | TRAINING |
| 1056 | USA | Mark 33 | Exercise | Torpedoes | 7 | Torpedo | 1946 | 0 | 120000 | 2 | 240000 | 2 | Mod 30 | Improved recovery system, radio beacon | Exercise Torpedo |  | Mod 30 |
| 1057 | USA | Mark 34 | Exercise | Torpedoes | 8 | Torpedo | 1950 | 0 | 150000 | 3 | 300000 | 3 | Advanced Training | Multiple run capability, self-destruct safety | Exercise Torpedo |  | Advanced Training |
| 1058 | USA | Mark 36 | Exercise | Torpedoes | 9 | Torpedo | 1955 | 0 | 200000 | 4 | 400000 | 4 | Modern Exercise | Electric propulsion, multiple uses, quiet | Exercise Torpedo |  | Modern Exercise |
| 1059 | USA | Mark 40 | Exercise | Torpedoes | 9 | Torpedo | 1958 | 0 | 180000 | 3 | 360000 | 3 | Target Torpedo | Simulates enemy torpedoes for ASW training | Exercise Torpedo |  | Target Torpedo |
| 1060 | USA | MK-59 | Exercise | Torpedoes | 10 | Torpedo | 1970 | 0 | 250000 | 5 | 500000 | 5 | Mark 46 Trainer | Exercise version of Mark 46 for crew training | Exercise Torpedo |  | Mark 46 Trainer |
| 1061 | USA | MK-48 EXTORP | Exercise | Torpedoes | 10 | Torpedo | 1980 | 0 | 500000 | 8 | 1000000 | 8 | Heavyweight Trainer | Full-sized Mark 48 exercise torpedo, no warhead | Exercise Torpedo |  | Heavyweight Trainer |
| 1100 | British | Whitehead Torpedo (Original) | Compressed Air | Torpedoes | 1 | Torpedo | 1866 | 1 | 0 | 0 | 0 | 0 | INVENTOR | FREE! First self-propelled torpedo, 14" × 11 ft, 18 lbs dynamite | Compressed Air Torpedo |  | INVENTOR |
| 1101 | British | Whitehead Mark I | Compressed Air | Torpedoes | 2 | Torpedo | 1871 | 0 | 50000 | 1 | 100000 | 1 | Early RN | Royal Navy adoption, improved gyroscope, 16" diameter | Compressed Air Torpedo |  | Early RN |
| 1102 | British | Whitehead Mark II | Compressed Air | Torpedoes | 2 | Torpedo | 1876 | 0 | 75000 | 2 | 150000 | 2 | RN Standard | 16" × 12 ft, Brotherhood engine, 7 kts, 600 yd range | Compressed Air Torpedo |  | RN Standard |
| 1103 | British | Whitehead Mark III | Compressed Air | Torpedoes | 3 | Torpedo | 1882 | 0 | 120000 | 2 | 240000 | 2 | Colonial Era | 18" diameter introduced, 800 yd range, 67 lbs guncotton | Compressed Air Torpedo |  | Colonial Era |
| 1104 | British | Whitehead Mark IV | Steam | Torpedoes | 3 | Torpedo | 1886 | 0 | 150000 | 2 | 300000 | 2 | Steam Transition | First steam-heated torpedo, 18" × 14 ft, 10 kts | Steam Torpedo |  | Steam Transition |
| 1105 | British | 18" Mark V | Steam | Torpedoes | 4 | Torpedo | 1895 | 0 | 200000 | 3 | 400000 | 3 | Victorian | 18" × 14.5 ft, improved heating, 1,000 yd range, 200 lbs | Steam Torpedo |  | Victorian |
| 1106 | British | 18" Mark VI | Steam | Torpedoes | 4 | Torpedo | 1900 | 0 | 250000 | 3 | 500000 | 3 | Pre-Dreadnought | 18" × 15 ft, 29 kts, 3,000 yd range, destroyer standard | Steam Torpedo |  | Pre-Dreadnought |
| 1107 | British | 21" Mark I | Steam | Torpedoes | 5 | Torpedo | 1908 | 0 | 350000 | 4 | 700000 | 4 | DREADNOUGHT ERA | First 21" torpedo, battleship/cruiser weapon, 5,000 yd | Steam Torpedo |  | DREADNOUGHT ERA |
| 1108 | British | 21" Mark II | Steam | Torpedoes | 5 | Torpedo | 1914 | 0 | 400000 | 4 | 800000 | 4 | WWI Submarine | Submarine torpedo, 21" × 17.7 ft, 35 kts, 10,000 yd | Steam Torpedo |  | WWI Submarine |
| 1109 | British | 18" Mark VII | Steam | Torpedoes | 5 | Torpedo | 1915 | 0 | 300000 | 3 | 600000 | 3 | Destroyer Optimized | Improved Mark VI, 35 kts, 5,000 yd, lighter for destroyers | Steam Torpedo |  | Destroyer Optimized |
| 1110 | British | 21" Mark III | Steam | Torpedoes | 6 | Torpedo | 1916 | 0 | 450000 | 5 | 900000 | 5 | WWI Heavy | Battleship/cruiser torpedo, 21" × 21 ft, heavier warhead 400 lbs | Steam Torpedo |  | WWI Heavy |
| 1111 | British | 21" Mark IV | Steam | Torpedoes | 6 | Torpedo | 1918 | 0 | 500000 | 5 | 1000000 | 5 | Late WWI Sub | Improved Mark II, 40 kts, 5,000 yd, 515 lbs TNT | Steam Torpedo |  | Late WWI Sub |
| 1112 | British | 18" Mark VIII | Steam | Torpedoes | 6 | Torpedo | 1918 | 0 | 400000 | 4 | 800000 | 4 | Destroyer Final | Final 18" variant, 40 kts, 6,000 yd, 176 lbs Amatol | Steam Torpedo |  | Destroyer Final |
| 1113 | British | 21" Mark V | Steam | Torpedoes | 6 | Torpedo | 1920 | 0 | 520000 | 5 | 1040000 | 5 | Post-WWI | Refined Mark IV, better gyroscope, reduced maintenance | Steam Torpedo |  | Post-WWI |
| 1114 | British | 21" Mark VI | Steam | Torpedoes | 7 | Torpedo | 1925 | 0 | 550000 | 6 | 1100000 | 6 | Interwar Standard | Wet-heater engine, 40 kts, 8,000 yd, 750 lbs TNT | Steam Torpedo |  | Interwar Standard |
| 1115 | British | 21" Mark VII | Steam | Torpedoes | 7 | Torpedo | 1928 | 0 | 580000 | 6 | 1160000 | 6 | Surface Ship | Destroyer/cruiser torpedo, improved reliability, 7,000 yd | Steam Torpedo |  | Surface Ship |
| 1116 | British | 21" Mark VIII | Steam | Torpedoes | 8 | Torpedo | 1927 | 0 | 750000 | 7 | 1500000 | 7 | SUBMARINE STANDARD | **Most reliable WWII sub torpedo**, 41 kts, 7,000 yd, 805 lbs Torpex | Steam Torpedo |  | SUBMARINE STANDARD |
| 1117 | British | 21" Mark VIII** | Steam | Torpedoes | 8 | Torpedo | 1942 | 0 | 900000 | 5 | 1800000 | 5 | WARTIME UPGRADE | Burner-cycle engine, 45 kts, 9,000 yd, same warhead, LEGENDARY | Steam Torpedo |  | WARTIME UPGRADE |
| 1118 | British | 21" Mark IX | Steam | Torpedoes | 8 | Torpedo | 1930 | 0 | 700000 | 6 | 1400000 | 6 | SURFACE STANDARD | Destroyer/cruiser primary, 36 kts, 10,500 yd, 750 lbs | Steam Torpedo |  | SURFACE STANDARD |
| 1119 | British | 21" Mark IX** | Steam | Torpedoes | 8 | Torpedo | 1943 | 0 | 850000 | 5 | 1700000 | 5 | Wartime Mod | Improved Mark IX, 41 kts, 13,500 yd, 810 lbs Torpex | Steam Torpedo |  | Wartime Mod |
| 1120 | British | 18" Mark X | Aerial | Torpedoes | 7 | Torpedo | 1932 | 0 | 600000 | 5 | 1200000 | 5 | FIRST AERIAL | First British aerial torpedo, 18" × 17 ft, biplane-launched | Aerial Torpedo |  | FIRST AERIAL |
| 1121 | British | 18" Mark XI | Aerial | Torpedoes | 7 | Torpedo | 1935 | 0 | 650000 | 5 | 1300000 | 5 | Carrier Improved | Swordfish/Albacore torpedo, shrouded prop, stabilizing vanes | Aerial Torpedo |  | Carrier Improved |
| 1122 | British | 18" Mark XII | Aerial | Torpedoes | 8 | Torpedo | 1938 | 0 | 850000 | 6 | 1700000 | 6 | SWORDFISH STANDARD | **Sank Bismarck**, 18" × 17.7 ft, 40 kts, 1,500 yd, 388 lbs Torpex | Aerial Torpedo |  | SWORDFISH STANDARD |
| 1123 | British | 18" Mark XV (Aerial) | Aerial | Torpedoes | 8 | Torpedo | 1943 | 0 | 1000000 | 5 | 2000000 | 5 | Late-War Air | Improved stability, 40 kts, 2,500 yd, Barracuda/Avenger use | Aerial Torpedo |  | Late-War Air |
| 1124 | British | 21" Mark X | Steam | Torpedoes | 8 | Torpedo | 1935 | 0 | 720000 | 6 | 1440000 | 6 | Cruiser Optimized | Heavy cruiser torpedo, 40 kts, 9,000 yd, 750 lbs | Steam Torpedo |  | Cruiser Optimized |
| 1125 | British | 21" Mark XI | Steam | Torpedoes | 8 | Torpedo | 1937 | 0 | 750000 | 6 | 1500000 | 6 | MTB Torpedo | Motor Torpedo Boat weapon, shorter 21" × 17 ft, 40 kts | Steam Torpedo |  | MTB Torpedo |
| 1126 | British | 21" Mark XII | Steam | Torpedoes | 8 | Torpedo | 1939 | 0 | 800000 | 6 | 1600000 | 6 | Destroyer Late | Pre-war destroyer standard, 45 kts, 6,000 yd, 600 lbs | Steam Torpedo |  | Destroyer Late |
| 1127 | British | 21" Mark XIII | Oxygen (Experimental) | Torpedoes | 8 | Torpedo | 1935 | 0 | 1500000 | 12 | 3000000 | 12 | ABANDONED | Oxygen experiment (like Type 93), too dangerous, cancelled | Oxygen (Experimental) Torpedo |  | ABANDONED |
| 1128 | British | 21" Mark XIV | Electric | Torpedoes | 9 | Torpedo | 1943 | 0 | 1200000 | 7 | 2400000 | 7 | WAKELESS | Battery-electric, 8 kts, 4,000 yd, slow but silent, MTB use | Electric Torpedo |  | WAKELESS |
| 1129 | British | 21" Mark XV (Sub) | Steam | Torpedoes | 8 | Torpedo | 1942 | 0 | 950000 | 6 | 1900000 | 6 | Sub Heavy | Heavy warhead variant, 35 kts, 5,000 yd, 900 lbs Torpex | Steam Torpedo |  | Sub Heavy |
| 1130 | British | 21" Mark XVI | Electric | Torpedoes | 9 | Torpedo | 1944 | 0 | 1300000 | 7 | 2600000 | 7 | Silent Hunter | Improved Mark XIV, 12 kts, 5,000 yd, 750 lbs Torpex | Electric Torpedo |  | Silent Hunter |
| 1131 | British | 21" Mark XVII | Hydrogen Peroxide | Torpedoes | 9 | Torpedo | 1945 | 0 | 1800000 | 9 | 3600000 | 9 | EXPERIMENTAL | HTP propulsion, 45 kts, 9,000 yd, unreliable, limited use | Hydrogen Peroxide Torpedo |  | EXPERIMENTAL |
| 1132 | British | Mark 18 | Acoustic | Torpedoes | 9 | Torpedo | 1946 | 0 | 2000000 | 8 | 4000000 | 8 | FIRST HOMING | Passive acoustic homing, ASW torpedo, 17 kts, 5,000 yd | Acoustic Torpedo |  | FIRST HOMING |
| 1133 | British | Mark 19 | Acoustic | Torpedoes | 9 | Torpedo | 1948 | 0 | 2100000 | 8 | 4200000 | 8 | Improved Homing | Better sonar, shallow water optimized, 20 kts | Acoustic Torpedo |  | Improved Homing |
| 1134 | British | Mark 20 | Acoustic | Torpedoes | 9 | Torpedo | 1955 | 0 | 2400000 | 10 | 4800000 | 10 | EARLY GUIDED | Wire-guided option, 20" × 11 ft, passive homing, 30 kts | Acoustic Torpedo |  | EARLY GUIDED |
| 1135 | British | Mark 20S | Acoustic | Torpedoes | 9 | Torpedo | 1957 | 0 | 2500000 | 9 | 5000000 | 9 | Surface Variant | Surface ship-launched Mark 20, ASW optimized | Acoustic Torpedo |  | Surface Variant |
| 1136 | British | Mark 21 | Electric | Torpedoes | 9 | Torpedo | 1948 | 0 | 2200000 | 9 | 4400000 | 9 | Silent Sub | Improved electric, 25 kts, 7,000 yd, wakeless | Electric Torpedo |  | Silent Sub |
| 1137 | British | Mark 22 | Acoustic | Torpedoes | 9 | Torpedo | 1952 | 0 | 2300000 | 10 | 4600000 | 10 | ASW Standard | Helicopter-launched, lightweight 12.75", 25 kts | Acoustic Torpedo |  | ASW Standard |
| 1138 | British | Mark 23 | Acoustic | Torpedoes | 9 | Torpedo | 1959 | 0 | 2600000 | 11 | 5200000 | 11 | Homing Improved | Active/passive sonar, 30 kts, better countermeasures | Acoustic Torpedo |  | Homing Improved |
| 1139 | British | Mark 24 Tigerfish Mod 0 | Wire-Guided | Torpedoes | 10 | Torpedo | 1974 | 0 | 4500000 | 16 | 9000000 | 16 | HEAVYWEIGHT | 21" × 21 ft, wire-guided, active/passive, 35 kts, 29,000 yd | Wire-Guided Torpedo |  | HEAVYWEIGHT |
| 1140 | British | Mark 24 Tigerfish Mod 1 | Wire-Guided | Torpedoes | 10 | Torpedo | 1980 | 0 | 5000000 | 14 | 10000000 | 14 | Improved Guidance | Digital guidance, better shallow water, 40 kts | Wire-Guided Torpedo |  | Improved Guidance |
| 1141 | British | Mark 24 Tigerfish Mod 2 | Wire-Guided | Torpedoes | 10 | Torpedo | 1986 | 0 | 5500000 | 15 | 11000000 | 15 | Final Variant | Enhanced seeker, improved reliability, 35 kts, 39,000 yd | Wire-Guided Torpedo |  | Final Variant |
| 1142 | British | Stingray Mod 0 | Acoustic | Torpedoes | 10 | Torpedo | 1983 | 0 | 3500000 | 12 | 7000000 | 12 | LIGHTWEIGHT | 12.75" × 8.5 ft, shaped-charge warhead, 45 kts, 7,000 yd | Acoustic Torpedo |  | LIGHTWEIGHT |
| 1143 | British | Stingray Mod 1 | Acoustic | Torpedoes | 10 | Torpedo | 1988 | 0 | 3800000 | 11 | 7600000 | 11 | Improved Seeker | Better shallow water, fire-and-forget, helo/surface launch | Acoustic Torpedo |  | Improved Seeker |
| 1144 | British | Spearfish | Wire-Guided | Torpedoes | 10 | Torpedo | 1988 | 0 | 10000000 | 20 | 20000000 | 20 | HEAVYWEIGHT MODERN | **21" × 21 ft, dual propulsion**, 65+ kts, 40,000+ yd, LEGENDARY | Wire-Guided Torpedo |  | HEAVYWEIGHT MODERN |
| 1145 | British | Spearfish Mod 1 | Wire-Guided | Torpedoes | 10 | Torpedo | 1992 | 0 | 11000000 | 18 | 22000000 | 18 | Enhanced | (Future variant beyond 1990 scope, included for completeness) | Wire-Guided Torpedo |  | Enhanced |
| 1146 | British | Mark 20E | Acoustic | Torpedoes | 9 | Torpedo | 1960 | 0 | 2400000 | 9 | 4800000 | 9 | Export Variant | Downgraded Mark 20 for Commonwealth navies | Acoustic Torpedo |  | Export Variant |
| 1147 | British | Mark 23E | Acoustic | Torpedoes | 9 | Torpedo | 1965 | 0 | 2500000 | 10 | 5000000 | 10 | Commonwealth | Export Mark 23, Australian/Canadian use | Acoustic Torpedo |  | Commonwealth |
| 1148 | British | Mark 24 Tiger Mk 1 (Export) | Wire-Guided | Torpedoes | 10 | Torpedo | 1978 | 0 | 4000000 | 14 | 8000000 | 14 | Allied Export | Reduced performance Tigerfish for export | Wire-Guided Torpedo |  | Allied Export |
| 1149 | British | Sting Ray Export | Acoustic | Torpedoes | 10 | Torpedo | 1985 | 0 | 3200000 | 11 | 6400000 | 11 | International | Export Stingray variant, multiple operators | Acoustic Torpedo |  | International |
| 1150 | British | Practice Torpedo Mark I | Exercise | Torpedoes | 6 | Torpedo | 1910 | 0 | 50000 | 1 | 100000 | 1 | TRAINING | Early practice torpedo, recoverable | Exercise Torpedo |  | TRAINING |
| 1151 | British | Practice Torpedo Mark II | Exercise | Torpedoes | 7 | Torpedo | 1925 | 0 | 75000 | 2 | 150000 | 2 | Interwar Training | Improved recovery system, radio beacon | Exercise Torpedo |  | Interwar Training |
| 1152 | British | Exercise Torpedo Mark III | Exercise | Torpedoes | 8 | Torpedo | 1945 | 0 | 100000 | 2 | 200000 | 2 | Post-war Training | Modern exercise torpedo, multiple runs | Exercise Torpedo |  | Post-war Training |
| 1153 | British | Mark 20 Exercise | Exercise | Torpedoes | 9 | Torpedo | 1960 | 0 | 150000 | 3 | 300000 | 3 | Guided Training | Simulates Mark 20 for crew training | Exercise Torpedo |  | Guided Training |
| 1154 | British | Tigerfish Exercise | Exercise | Torpedoes | 10 | Torpedo | 1980 | 0 | 300000 | 5 | 600000 | 5 | Heavy Trainer | Full-sized Tigerfish practice torpedo | Exercise Torpedo |  | Heavy Trainer |
| 1155 | British | Spearfish Exercise | Exercise | Torpedoes | 10 | Torpedo | 1990 | 0 | 500000 | 6 | 1000000 | 6 | Modern Trainer | Spearfish exercise torpedo, no warhead | Exercise Torpedo |  | Modern Trainer |
| 1156 | British | Mark 25 | Rocket | Torpedoes | 9 | Torpedo | 1950 | 0 | 3000000 | 14 | 6000000 | 14 | CANCELLED | Rocket-propelled torpedo concept, not developed | Rocket Torpedo |  | CANCELLED |
| 1157 | British | Mk 30 "Grog" | Nuclear | Torpedoes | 10 | Torpedo | 1955 | 0 | 6000000 | 20 | 12000000 | 20 | PAPER DESIGN | Nuclear torpedo concept, never built | Nuclear Torpedo |  | PAPER DESIGN |
| 1200 | German | Schwarzkopf Torpedo C/73 | Compressed Air | Torpedoes | 1 | Torpedo | 1873 | 1 | 0 | 0 | 0 | 0 | STARTING | FREE! Early German torpedo, licensed Whitehead design | Compressed Air Torpedo |  | STARTING |
| 1201 | German | Schwarzkopf C/81 | Compressed Air | Torpedoes | 2 | Torpedo | 1881 | 0 | 60000 | 1 | 120000 | 1 | Imperial Era | Improved reliability, 14" diameter, 500 yd range | Compressed Air Torpedo |  | Imperial Era |
| 1202 | German | Schwarzkopf C/88 | Steam | Torpedoes | 2 | Torpedo | 1888 | 0 | 90000 | 2 | 180000 | 2 | Pre-Dreadnought | 17.7" diameter, steam heating, 800 yd range | Steam Torpedo |  | Pre-Dreadnought |
| 1203 | German | C/91 | Steam | Torpedoes | 3 | Torpedo | 1891 | 0 | 140000 | 2 | 280000 | 2 | Early Standard | 17.7" × 14.5 ft, improved gyroscope, 1,200 yd | Steam Torpedo |  | Early Standard |
| 1204 | German | C/96 | Steam | Torpedoes | 3 | Torpedo | 1896 | 0 | 170000 | 2 | 340000 | 2 | Torpedo Boat | 17.7" × 16 ft, 27 kts, 1,800 yd, 110 lbs explosive | Steam Torpedo |  | Torpedo Boat |
| 1205 | German | C/03 | Steam | Torpedoes | 4 | Torpedo | 1903 | 0 | 220000 | 3 | 440000 | 3 | Pre-WWI | 17.7" × 18 ft, 32 kts, 3,000 yd, improved propulsion | Steam Torpedo |  | Pre-WWI |
| 1206 | German | C/06 | Steam | Torpedoes | 4 | Torpedo | 1906 | 0 | 270000 | 3 | 540000 | 3 | Dreadnought Era | 19.7" introduced, battleship/cruiser weapon | Steam Torpedo |  | Dreadnought Era |
| 1207 | German | C/06D | Steam | Torpedoes | 5 | Torpedo | 1910 | 0 | 350000 | 4 | 700000 | 4 | Pre-WWI Sub | Submarine variant, 19.7" × 19.7 ft, 4,000 yd | Steam Torpedo |  | Pre-WWI Sub |
| 1208 | German | C/09 | Steam | Torpedoes | 5 | Torpedo | 1909 | 0 | 330000 | 4 | 660000 | 4 | Destroyer | 19.7" × 18 ft, 35 kts, 3,500 yd, 280 lbs | Steam Torpedo |  | Destroyer |
| 1209 | German | C/12 | Steam | Torpedoes | 5 | Torpedo | 1912 | 0 | 380000 | 5 | 760000 | 5 | WWI Standard | 19.7" × 19.7 ft, 36 kts, 5,000 yd, heavier warhead | Steam Torpedo |  | WWI Standard |
| 1210 | German | G6 | Steam | Torpedoes | 6 | Torpedo | 1915 | 0 | 450000 | 5 | 900000 | 5 | EARLY G-SERIES | First "G" designation, 19.7" × 23.6 ft, 6,000 yd | Steam Torpedo |  | EARLY G-SERIES |
| 1211 | German | G7 (WWI) | Steam | Torpedoes | 6 | Torpedo | 1916 | 0 | 500000 | 6 | 1000000 | 6 | WWI U-BOAT | 19.7" (533mm) standardized, 8,000 yd, 357 lbs Hexanite | Steam Torpedo |  | WWI U-BOAT |
| 1212 | German | H7 | Steam | Torpedoes | 6 | Torpedo | 1917 | 0 | 480000 | 5 | 960000 | 5 | Destroyer Variant | 19.7" × 20 ft, faster 40 kts, shorter range 5,000 yd | Steam Torpedo |  | Destroyer Variant |
| 1213 | German | H8 | Steam | Torpedoes | 6 | Torpedo | 1918 | 0 | 520000 | 5 | 1040000 | 5 | Late WWI | Improved H7, 42 kts, 6,000 yd, better reliability | Steam Torpedo |  | Late WWI |
| 1214 | German | G7 (1928) | Steam | Torpedoes | 7 | Torpedo | 1928 | 0 | 600000 | 6 | 1200000 | 6 | Interwar Refined | Post-WWI improved G7, 40 kts, 8,000 yd, 616 lbs TNT | Steam Torpedo |  | Interwar Refined |
| 1215 | German | G7a (Prototype) | Steam | Torpedoes | 7 | Torpedo | 1934 | 0 | 700000 | 7 | 1400000 | 7 | REARMAMENT | Pre-war development, wet-heater engine, 12,000 yd | Steam Torpedo |  | REARMAMENT |
| 1216 | German | G7e (Prototype) | Electric | Torpedoes | 7 | Torpedo | 1936 | 0 | 1200000 | 9 | 2400000 | 9 | ELECTRIC DEVELOPMENT | Battery-powered prototype, wakeless, 30 kts | Electric Torpedo |  | ELECTRIC DEVELOPMENT |
| 1217 | German | G7a (TI) | Steam | Torpedoes | 8 | Torpedo | 1939 | 0 | 950000 | 6 | 1900000 | 6 | U-BOAT STANDARD | **21" (533mm) × 23.5 ft, 44 kts, 13,500 yd**, 617 lbs Sw39a | Steam Torpedo |  | U-BOAT STANDARD |
| 1218 | German | G7e (TII) | Electric | Torpedoes | 8 | Torpedo | 1940 | 0 | 1500000 | 7 | 3000000 | 7 | WAKELESS | **Battery-electric, 28 kts, 11,000 yd**, NO WAKE, 617 lbs | Electric Torpedo |  | WAKELESS |
| 1219 | German | G7a (TI) Mod 1 | Steam | Torpedoes | 8 | Torpedo | 1942 | 0 | 1000000 | 5 | 2000000 | 5 | Improved Steam | Increased range 14,000 yd, improved reliability | Steam Torpedo |  | Improved Steam |
| 1220 | German | G7e (TII) Mod 1 | Electric | Torpedoes | 8 | Torpedo | 1942 | 0 | 1600000 | 6 | 3200000 | 6 | Better Battery | Extended range 12,500 yd, improved endurance | Electric Torpedo |  | Better Battery |
| 1221 | German | G7es (TIII) | Electric | Torpedoes | 8 | Torpedo | 1943 | 0 | 2000000 | 8 | 4000000 | 8 | PATTERN-RUNNING | **Circular/zigzag search**, 22 kts, convoy attacks, INNOVATIVE | Electric Torpedo |  | PATTERN-RUNNING |
| 1222 | German | G7e (TIIIa) | Electric | Torpedoes | 8 | Torpedo | 1943 | 0 | 1700000 | 7 | 3400000 | 7 | Late-War Electric | Improved TII, 30 kts, 14,000 yd, better battery | Electric Torpedo |  | Late-War Electric |
| 1223 | German | G7a (TI) Final | Steam | Torpedoes | 8 | Torpedo | 1944 | 0 | 1100000 | 5 | 2200000 | 5 | Ultimate Steam | Final steam variant, 44 kts, 15,000 yd, optimized | Steam Torpedo |  | Ultimate Steam |
| 1224 | German | T5 Zaunkönig (Wren) | Acoustic | Torpedoes | 9 | Torpedo | 1943 | 0 | 2800000 | 10 | 5600000 | 10 | FIRST ACOUSTIC HOMING | **World's first operational**, passive homing, 24 kts, 5,700 yd | Acoustic Torpedo |  | FIRST ACOUSTIC HOMING |
| 1225 | German | T5 Zaunkönig II | Acoustic | Torpedoes | 9 | Torpedo | 1944 | 0 | 3000000 | 9 | 6000000 | 9 | Improved Homing | Better seeker, counter-countermeasures, 25 kts | Acoustic Torpedo |  | Improved Homing |
| 1226 | German | T11 | Acoustic | Torpedoes | 9 | Torpedo | 1944 | 0 | 3500000 | 12 | 7000000 | 12 | ADVANCED ACOUSTIC | Two-speed, active/passive option, 33 kts, 18,000 yd, LEGENDARY | Acoustic Torpedo |  | ADVANCED ACOUSTIC |
| 1227 | German | T4 Falke (Falcon) | Acoustic | Torpedoes | 9 | Torpedo | 1943 | 0 | 2600000 | 11 | 5200000 | 11 | ANTI-ESCORT | ASW torpedo, homes on destroyer screws, 29 kts | Acoustic Torpedo |  | ANTI-ESCORT |
| 1228 | German | T10 | Acoustic | Torpedoes | 9 | Torpedo | 1943 | 0 | 2700000 | 10 | 5400000 | 10 | Pattern + Homing | Combines pattern-running with acoustic homing | Acoustic Torpedo |  | Pattern + Homing |
| 1229 | German | LuT (Lagenunabhängiger Torpedo) | Pattern | Torpedoes | 8 | Torpedo | 1942 | 0 | 1800000 | 9 | 3600000 | 9 | PROGRAMMABLE | Pre-set search patterns, microswitch programming, convoy weapon | Pattern Torpedo |  | PROGRAMMABLE |
| 1230 | German | FAT (Flächenabsuchender Torpedo) | Pattern | Torpedoes | 8 | Torpedo | 1943 | 0 | 1900000 | 9 | 3800000 | 9 | AREA SEARCH | Zigzag pattern, 30 kts, searches convoy lanes | Pattern Torpedo |  | AREA SEARCH |
| 1231 | German | G7ut Steinwal (Stone Whale) | Steam | Torpedoes | 8 | Torpedo | 1943 | 0 | 1400000 | 7 | 2800000 | 7 | DEEP DIVER | 130m depth capability, anti-escort, 44 kts | Steam Torpedo |  | DEEP DIVER |
| 1232 | German | G7a(T) | Steam | Torpedoes | 8 | Torpedo | 1943 | 0 | 1200000 | 6 | 2400000 | 6 | SURFACE LAUNCH | Destroyer/S-boat variant, surface-optimized | Steam Torpedo |  | SURFACE LAUNCH |
| 1233 | German | G7v Dachshund | Electric | Torpedoes | 8 | Torpedo | 1944 | 0 | 1600000 | 8 | 3200000 | 8 | SLOW HUNT | 14 kts ultra-quiet, 30,000 yd range, stealth attack | Electric Torpedo |  | SLOW HUNT |
| 1234 | German | G7eT1 | Electric | Torpedoes | 8 | Torpedo | 1944 | 0 | 1750000 | 7 | 3500000 | 7 | Surface Electric | Electric wakeless for S-boats and destroyers | Electric Torpedo |  | Surface Electric |
| 1235 | German | G7e/T12 | Hydrogen Peroxide | Torpedoes | 9 | Torpedo | 1944 | 0 | 3200000 | 14 | 6400000 | 14 | EXPERIMENTAL | HTP propulsion, 50 kts, unreliable, few built | Hydrogen Peroxide Torpedo |  | EXPERIMENTAL |
| 1236 | German | Zaunkönig Draht (T6) | Wire-Guided | Torpedoes | 9 | Torpedo | 1944 | 0 | 4000000 | 16 | 8000000 | 16 | PAPER DESIGN | Wire-guided acoustic, prototype only, war ended | Wire-Guided Torpedo |  | PAPER DESIGN |
| 1237 | German | Spinne (Spider) | Acoustic | Torpedoes | 9 | Torpedo | 1945 | 0 | 3500000 | 12 | 7000000 | 12 | PROTOTYPE | Advanced homing, multiple sensors, 1 built | Acoustic Torpedo |  | PROTOTYPE |
| 1238 | German | G7e/T13 | Acoustic | Torpedoes | 9 | Torpedo | 1945 | 0 | 3300000 | 11 | 6600000 | 11 | LATE-WAR | Improved Zaunkönig, active sonar option, few produced | Acoustic Torpedo |  | LATE-WAR |
| 1239 | German | Seal DM1 | Acoustic | Torpedoes | 9 | Torpedo | 1960 | 0 | 3000000 | 10 | 6000000 | 10 | POST-WAR REBUILD | Bundesmarine ASW torpedo, 19.7", NATO compatible | Acoustic Torpedo |  | POST-WAR REBUILD |
| 1240 | German | Seal DM2 | Acoustic | Torpedoes | 10 | Torpedo | 1965 | 0 | 4000000 | 12 | 8000000 | 12 | IMPROVED SEAL | Mod 1 upgrade, wire-guidance option, 35 kts | Acoustic Torpedo |  | IMPROVED SEAL |
| 1241 | German | SUT (Surface and Underwater Target) | Wire-Guided | Torpedoes | 10 | Torpedo | 1967 | 0 | 7000000 | 16 | 14000000 | 16 | MODERN HEAVYWEIGHT | 21" wire-guided, active/passive, 35 kts, 28,000 yd | Wire-Guided Torpedo |  | MODERN HEAVYWEIGHT |
| 1242 | German | SUT Mod 1 | Wire-Guided | Torpedoes | 10 | Torpedo | 1970 | 0 | 7500000 | 15 | 15000000 | 15 | Enhanced | Digital guidance, improved seeker, export success | Wire-Guided Torpedo |  | Enhanced |
| 1243 | German | AEG Seal Mod 2 | Acoustic | Torpedoes | 10 | Torpedo | 1972 | 0 | 4500000 | 12 | 9000000 | 12 | Final Seal | Ultimate Seal variant, active/passive homing | Acoustic Torpedo |  | Final Seal |
| 1244 | German | G7 Übung (Exercise) | Exercise | Torpedoes | 6 | Torpedo | 1936 | 0 | 80000 | 2 | 160000 | 2 | TRAINING | Pre-war practice torpedo, recoverable | Exercise Torpedo |  | TRAINING |
| 1245 | German | G7e Übung | Exercise | Torpedoes | 8 | Torpedo | 1940 | 0 | 120000 | 3 | 240000 | 3 | Electric Trainer | Practice electric torpedo, multiple runs | Exercise Torpedo |  | Electric Trainer |
| 1246 | German | Seal Exercise | Exercise | Torpedoes | 9 | Torpedo | 1965 | 0 | 180000 | 4 | 360000 | 4 | Post-War Training | Bundesmarine exercise torpedo | Exercise Torpedo |  | Post-War Training |
| 1247 | German | SUT Exercise | Exercise | Torpedoes | 10 | Torpedo | 1975 | 0 | 350000 | 6 | 700000 | 6 | Modern Trainer | Full-sized SUT practice torpedo | Exercise Torpedo |  | Modern Trainer |
| 1248 | German | T7 Adler (Eagle) | Acoustic | Torpedoes | 9 | Torpedo | 1944 | 0 | 3800000 | 14 | 7600000 | 14 | CANCELLED | Advanced multi-sensor homing, cancelled before production | Acoustic Torpedo |  | CANCELLED |
| 1249 | German | T8 Wren | Acoustic | Torpedoes | 9 | Torpedo | 1944 | 0 | 3600000 | 13 | 7200000 | 13 | PROTOTYPE | Active/passive sonar, war ended before trials | Acoustic Torpedo |  | PROTOTYPE |
| 1250 | German | T14 | Rocket | Torpedoes | 9 | Torpedo | 1944 | 0 | 4500000 | 18 | 9000000 | 18 | PAPER DESIGN | Rocket-propelled concept, never built | Rocket Torpedo |  | PAPER DESIGN |
| 1251 | German | G7e/T15 Walter | HTP | Torpedoes | 10 | Torpedo | 1945 | 0 | 5000000 | 20 | 10000000 | 20 | EXPERIMENTAL | Walter turbine, 60+ kts, 1 prototype, never operational | HTP Torpedo |  | EXPERIMENTAL |
| 1252 | German | Barracuda | Nuclear | Torpedoes | 10 | Torpedo | 1944 | 0 | 8000000 | 24 | 16000000 | 24 | CONCEPT | Atomic torpedo concept, pure speculation, never designed | Nuclear Torpedo |  | CONCEPT |
| 1253 | German | Dackel (Dachshund II) | Electric | Torpedoes | 9 | Torpedo | 1945 | 0 | 2500000 | 10 | 5000000 | 10 | LIMITED | Extended-range electric, 50,000 yd, few produced | Electric Torpedo |  | LIMITED |
| 1300 | Japanese | Type 28 No.1 | Compressed Air | Torpedoes | 1 | Torpedo | 1895 | 1 | 0 | 0 | 0 | 0 | WHITEHEAD IMPORT | FREE! British Whitehead license, 14" × 12 ft, 18 lbs dynamite | Compressed Air Torpedo |  | WHITEHEAD IMPORT |
| 1301 | Japanese | Type 31 | Compressed Air | Torpedoes | 2 | Torpedo | 1898 | 0 | 50000 | 2 | 100000 | 2 | DOMESTIC COPY | 18" × 16 ft, 88 lbs guncotton, 26 kts, 800 yd | Compressed Air Torpedo |  | DOMESTIC COPY |
| 1302 | Japanese | Type 34 | Compressed Air | Torpedoes | 2 | Torpedo | 1901 | 0 | 75000 | 3 | 150000 | 3 | IMPROVED | 18" × 17 ft, 110 lbs guncotton, 28 kts, 1,000 yd | Compressed Air Torpedo |  | IMPROVED |
| 1303 | Japanese | Type 38 | Compressed Air | Torpedoes | 2 | Torpedo | 1905 | 0 | 100000 | 4 | 200000 | 4 | PRE-WWI | 18" × 18 ft, 132 lbs Shimose, 30 kts, 1,500 yd | Compressed Air Torpedo |  | PRE-WWI |
| 1304 | Japanese | Type 43 Year 2 | Compressed Air | Torpedoes | 3 | Torpedo | 1910 | 0 | 150000 | 5 | 300000 | 5 | WWI EARLY | 21" × 20 ft, 220 lbs Shimose, 32 kts, 3,000 yd, first 21" torpedo | Compressed Air Torpedo |  | WWI EARLY |
| 1305 | Japanese | Type 44 Year 3 | Compressed Air | Torpedoes | 3 | Torpedo | 1911 | 0 | 175000 | 5 | 350000 | 5 | DESTROYER | 21" × 21 ft, 242 lbs Shimose, 34 kts, 4,000 yd | Compressed Air Torpedo |  | DESTROYER |
| 1306 | Japanese | Type 6 (Submarine) | Compressed Air | Torpedoes | 4 | Torpedo | 1917 | 0 | 200000 | 6 | 400000 | 6 | WWI SUBMARINE | 18" × 18 ft, 220 lbs Shimose, 30 kts, 5,000 yd | Compressed Air Torpedo |  | WWI SUBMARINE |
| 1307 | Japanese | Type 8 No.1 | Compressed Air | Torpedoes | 4 | Torpedo | 1919 | 0 | 250000 | 6 | 500000 | 6 | POST-WWI | 21" × 23 ft, 330 lbs Shimose, 36 kts, 6,000 yd | Compressed Air Torpedo |  | POST-WWI |
| 1308 | Japanese | Type 8 No.2 | Compressed Air | Torpedoes | 4 | Torpedo | 1920 | 0 | 275000 | 6 | 550000 | 6 | IMPROVED | 21" × 23 ft, 330 lbs Shimose, 38 kts, 7,000 yd, alcohol fuel | Compressed Air Torpedo |  | IMPROVED |
| 1309 | Japanese | Type 8 No.4 | Alcohol | Torpedoes | 5 | Torpedo | 1922 | 0 | 300000 | 7 | 600000 | 7 | WASHINGTON TREATY | 21" × 23.5 ft, 353 lbs Type 97, 40 kts, 8,000 yd | Alcohol Torpedo |  | WASHINGTON TREATY |
| 1310 | Japanese | Type 89 | Alcohol | Torpedoes | 5 | Torpedo | 1929 | 0 | 350000 | 8 | 700000 | 8 | LATE INTERWAR | 21" × 23.5 ft, 375 lbs Type 97, 42 kts, 10,000 yd | Alcohol Torpedo |  | LATE INTERWAR |
| 1311 | Japanese | Type 90 (24-inch) | Alcohol | Torpedoes | 6 | Torpedo | 1930 | 0 | 500000 | 9 | 1000000 | 9 | LARGE CALIBER | **24" × 29.5 ft**, 660 lbs Type 97, 42 kts, 13,000 yd, prototype | Alcohol Torpedo |  | LARGE CALIBER |
| 1312 | Japanese | Oxygen Torpedo Prototype | Oxygen | Torpedoes | 6 | Torpedo | 1931 | 0 | 800000 | 12 | 1600000 | 12 | OXYGEN EXPERIMENTS | 24" experimental, testing oxygen propulsion, CLASSIFIED | Oxygen Torpedo |  | OXYGEN EXPERIMENTS |
| 1313 | Japanese | Type 90 Mod 1 | Oxygen | Torpedoes | 6 | Torpedo | 1932 | 0 | 1000000 | 10 | 2000000 | 10 | OXYGEN PROOF | 24" × 29.5 ft, oxygen trials successful, 45 kts, 18,000 yd | Oxygen Torpedo |  | OXYGEN PROOF |
| 1314 | Japanese | Type 90 Mod 2 | Oxygen | Torpedoes | 7 | Torpedo | 1933 | 0 | 1200000 | 11 | 2400000 | 11 | PRE-PRODUCTION | 24" × 29.5 ft, 748 lbs Type 97, 46 kts, 22,000 yd, refined | Oxygen Torpedo |  | PRE-PRODUCTION |
| 1315 | Japanese | Type 93 Model 1 (Mod 1) | Oxygen | Torpedoes | 8 | Torpedo | 1933 | 0 | 2000000 | 14 | 4000000 | 14 | INITIAL PRODUCTION | **24" × 29.5 ft**, 1,080 lbs Type 97, 48 kts, 35,000 yd, REVOLUTIONARY | Oxygen Torpedo |  | INITIAL PRODUCTION |
| 1316 | Japanese | Type 93 Model 1 (Mod 2) | Oxygen | Torpedoes | 8 | Torpedo | 1935 | 0 | 2200000 | 15 | 4400000 | 15 | IMPROVED | 24" × 29.5 ft, 1,080 lbs Type 97, 49 kts, 38,000 yd, refined | Oxygen Torpedo |  | IMPROVED |
| 1317 | Japanese | Type 93 Model 2 (Mod 3) | Oxygen | Torpedoes | 9 | Torpedo | 1938 | 0 | 2500000 | 16 | 5000000 | 16 | REFINED | 24" × 29.5 ft, 1,080 lbs Type 97, 50 kts, 40,000 yd, LEGENDARY | Oxygen Torpedo |  | REFINED |
| 1318 | Japanese | Type 93 Model 3 (Mod 3) | Oxygen | Torpedoes | 9 | Torpedo | 1943 | 0 | 2800000 | 16 | 5600000 | 16 | WARTIME | 24" × 29.5 ft, 1,080 lbs Type 97, 51 kts, 40,000 yd, combat optimized | Oxygen Torpedo |  | WARTIME |
| 1319 | Japanese | Type 93 Pure Oxygen Mk3 | Oxygen | Torpedoes | 9 | Torpedo | 1944 | 0 | 3000000 | 17 | 6000000 | 17 | ULTIMATE | **24" × 29.5 ft, 1,080 lbs Type 97, 51 kts, 43,700 yd**, maximum performance | Oxygen Torpedo |  | ULTIMATE |
| 1320 | Japanese | Type 95 Mod 1 | Oxygen | Torpedoes | 8 | Torpedo | 1935 | 0 | 1800000 | 13 | 3600000 | 13 | SUBMARINE OXYGEN | 21" × 29.5 ft, 893 lbs Type 97, 45 kts, 20,000 yd | Oxygen Torpedo |  | SUBMARINE OXYGEN |
| 1321 | Japanese | Type 95 Mod 2 | Oxygen | Torpedoes | 9 | Torpedo | 1938 | 0 | 2000000 | 14 | 4000000 | 14 | IMPROVED | 21" × 29.5 ft, 893 lbs Type 97, 47 kts, 28,000 yd | Oxygen Torpedo |  | IMPROVED |
| 1322 | Japanese | Type 95 Mod 3 | Oxygen | Torpedoes | 9 | Torpedo | 1942 | 0 | 2200000 | 15 | 4400000 | 15 | EXTENDED RANGE | **21" × 29.5 ft, 893 lbs Type 97, 49 kts, 35,000 yd**, LEGENDARY | Oxygen Torpedo |  | EXTENDED RANGE |
| 1323 | Japanese | Type 97 Mod 1 | Alcohol | Torpedoes | 7 | Torpedo | 1933 | 0 | 900000 | 10 | 1800000 | 10 | DESTROYER STANDARD | **24" × 29.5 ft**, 660 lbs Type 97, 52 kts, 20,000 yd | Alcohol Torpedo |  | DESTROYER STANDARD |
| 1324 | Japanese | Type 97 Mod 2 | Alcohol | Torpedoes | 7 | Torpedo | 1936 | 0 | 950000 | 11 | 1900000 | 11 | IMPROVED | 24" × 29.5 ft, 748 lbs Type 97, 52 kts, 22,000 yd | Alcohol Torpedo |  | IMPROVED |
| 1325 | Japanese | Type 91 Mod 1 | Compressed Air | Torpedoes | 7 | Torpedo | 1931 | 0 | 800000 | 10 | 1600000 | 10 | AERIAL TORPEDO | 18" × 17.7 ft, 331 lbs Type 97, 42 kts, 2,200 yd, carrier-based | Compressed Air Torpedo |  | AERIAL TORPEDO |
| 1326 | Japanese | Type 91 Mod 2 | Compressed Air | Torpedoes | 8 | Torpedo | 1941 | 0 | 1200000 | 12 | 2400000 | 12 | PEARL HARBOR | **18" × 17.7 ft, 452 lbs Type 97, 42 kts, 2,200 yd, SHALLOW 40 ft** | Compressed Air Torpedo |  | PEARL HARBOR |
| 1327 | Japanese | Type 91 Mod 3 | Compressed Air | Torpedoes | 8 | Torpedo | 1943 | 0 | 1400000 | 13 | 2800000 | 13 | IMPROVED | 18" × 17.7 ft, 529 lbs Type 97, 41 kts, 2,400 yd, refined | Compressed Air Torpedo |  | IMPROVED |
| 1328 | Japanese | Type 91 Mod 4 | Compressed Air | Torpedoes | 8 | Torpedo | 1944 | 0 | 1500000 | 14 | 3000000 | 14 | LATE WAR | 18" × 17.7 ft, 551 lbs Type 97, 40 kts, 2,600 yd | Compressed Air Torpedo |  | LATE WAR |
| 1329 | Japanese | Type 89 (Submarine) | Alcohol | Torpedoes | 6 | Torpedo | 1932 | 0 | 450000 | 8 | 900000 | 8 | SUBMARINE STANDARD | 21" × 23.5 ft, 660 lbs Type 97, 45 kts, 11,000 yd | Alcohol Torpedo |  | SUBMARINE STANDARD |
| 1330 | Japanese | Type 92 Mod 1 | Alcohol | Torpedoes | 7 | Torpedo | 1935 | 0 | 650000 | 9 | 1300000 | 9 | IMPROVED | 21" × 23.5 ft, 748 lbs Type 97, 46 kts, 13,000 yd | Alcohol Torpedo |  | IMPROVED |
| 1331 | Japanese | Type 92 Mod 2 | Alcohol | Torpedoes | 7 | Torpedo | 1938 | 0 | 700000 | 10 | 1400000 | 10 | REFINED | 21" × 23.5 ft, 772 lbs Type 97, 46 kts, 15,000 yd | Alcohol Torpedo |  | REFINED |
| 1332 | Japanese | Type 96 | Alcohol | Torpedoes | 6 | Torpedo | 1936 | 0 | 500000 | 8 | 1000000 | 8 | COASTAL DEFENSE | 21" × 23.5 ft, 660 lbs Type 97, 42 kts, 11,000 yd, MTB/coastal | Alcohol Torpedo |  | COASTAL DEFENSE |
| 1333 | Japanese | Type 97 (18-inch) | Alcohol | Torpedoes | 6 | Torpedo | 1937 | 0 | 450000 | 7 | 900000 | 7 | SMALL CRAFT | 18" × 18 ft, 420 lbs Type 97, 40 kts, 8,000 yd, MTB variant | Alcohol Torpedo |  | SMALL CRAFT |
| 1334 | Japanese | Type 2 Mod 1 | Oxygen | Torpedoes | 8 | Torpedo | 1942 | 0 | 1600000 | 12 | 3200000 | 12 | MIDGET SUBMARINE | 18" × 18 ft, oxygen fuel, 38 kts, 12,000 yd, Type A midget | Oxygen Torpedo |  | MIDGET SUBMARINE |
| 1335 | Japanese | Type 2 Mod 2 | Oxygen | Torpedoes | 8 | Torpedo | 1943 | 0 | 1800000 | 13 | 3600000 | 13 | IMPROVED | 18" × 18 ft, 420 lbs Type 97, 40 kts, 15,000 yd, Type D midget | Oxygen Torpedo |  | IMPROVED |
| 1336 | Japanese | Kaiten Type 1 | Oxygen | Torpedoes | 9 | Torpedo | 1944 | 0 | 2500000 | 15 | 5000000 | 15 | HUMAN TORPEDO | **24" × 48 ft, 3,418 lbs warhead, 30 kts, 50,000 yd, KAMIKAZE** | Oxygen Torpedo |  | HUMAN TORPEDO |
| 1337 | Japanese | Kaiten Type 2 | Oxygen | Torpedoes | 9 | Torpedo | 1944 | 0 | 2600000 | 16 | 5200000 | 16 | TWO-MAN | 24" × 54 ft, 3,960 lbs warhead, 28 kts, 60,000 yd, kamikaze (never operational) | Oxygen Torpedo |  | TWO-MAN |
| 1338 | Japanese | Kaiten Type 4 | Oxygen | Torpedoes | 9 | Torpedo | 1945 | 0 | 2700000 | 17 | 5400000 | 17 | FINAL VARIANT | 24" × 57 ft, 4,000 lbs warhead, 25 kts, 70,000 yd, kamikaze (prototype only) | Oxygen Torpedo |  | FINAL VARIANT |
| 1339 | Japanese | Type 43 (Acoustic Homing) | Acoustic | Torpedoes | 9 | Torpedo | 1943 | 0 | 2800000 | 14 | 5600000 | 14 | HOMING PROTOTYPE | 21" × 23.5 ft, acoustic homing trials, 35 kts, 10,000 yd, experimental | Acoustic Torpedo |  | HOMING PROTOTYPE |
| 1340 | Japanese | Type 43 Mod 1 | Acoustic | Torpedoes | 9 | Torpedo | 1944 | 0 | 3000000 | 15 | 6000000 | 15 | ACOUSTIC | 21" × 23.5 ft, 660 lbs Type 97, passive homing, 35 kts, 12,000 yd | Acoustic Torpedo |  | ACOUSTIC |
| 1341 | Japanese | Type 44 | Acoustic | Torpedoes | 9 | Torpedo | 1944 | 0 | 3200000 | 16 | 6400000 | 16 | ADVANCED ACOUSTIC | 21" × 23.5 ft, 748 lbs Type 97, passive homing, 38 kts, 15,000 yd | Acoustic Torpedo |  | ADVANCED ACOUSTIC |
| 1342 | Japanese | Type 45 Mod 1 | Wire-Guided | Torpedoes | 9 | Torpedo | 1945 | 0 | 3500000 | 17 | 7000000 | 17 | EXPERIMENTAL | 21" × 23.5 ft, wire guidance trials, never deployed, prototype only | Wire-Guided Torpedo |  | EXPERIMENTAL |
| 1343 | Japanese | Type 72 | Electric | Torpedoes | 9 | Torpedo | 1960 | 0 | 2500000 | 12 | 5000000 | 12 | JMSDF EARLY | 21" × 21 ft, electric, 35 kts, 12,000 yd, defensive weapon | Electric Torpedo |  | JMSDF EARLY |
| 1344 | Japanese | Type 73 | Wire-Guided | Torpedoes | 10 | Torpedo | 1967 | 0 | 5000000 | 18 | 10000000 | 18 | WIRE-GUIDED | 21" × 21 ft, wire-guided, 40 kts, 20,000 yd, modern | Wire-Guided Torpedo |  | WIRE-GUIDED |
| 1345 | Japanese | Type 80 Mod 1 | Wire-Guided | Torpedoes | 10 | Torpedo | 1970 | 0 | 6000000 | 20 | 12000000 | 20 | MODERN | 21" × 21 ft, active/passive sonar, 45 kts, 25,000 yd | Wire-Guided Torpedo |  | MODERN |
| 1346 | Japanese | Type 1 Land-Attack | Oxygen | Torpedoes | 8 | Torpedo | 1942 | 0 | 1800000 | 13 | 3600000 | 13 | SHORE BOMBARDMENT | 24" × 29.5 ft, land attack trials, oxygen fuel, experimental | Oxygen Torpedo |  | SHORE BOMBARDMENT |
| 1347 | Japanese | Type 4 (Cruiser) | Oxygen | Torpedoes | 8 | Torpedo | 1943 | 0 | 2000000 | 14 | 4000000 | 14 | HEAVY CRUISER | 24" × 30 ft, 1,210 lbs warhead, 48 kts, 38,000 yd | Oxygen Torpedo |  | HEAVY CRUISER |
| 1348 | Japanese | Type 6 (Battleship) | Oxygen | Torpedoes | 8 | Torpedo | 1944 | 0 | 2200000 | 15 | 4400000 | 15 | CAPITAL SHIP | **27.5" × 32 ft**, 1,650 lbs warhead, 44 kts, 35,000 yd, Yamato class | Oxygen Torpedo |  | CAPITAL SHIP |
| 1349 | Japanese | Type 44 Practice | Training | Torpedoes | 3 | Torpedo | 1911 | 0 | 50000 | 2 | 100000 | 2 | WWI PRACTICE | 18" × 16 ft, dummy warhead, recoverable, training use | Training Torpedo |  | WWI PRACTICE |
| 1350 | Japanese | Type 45 Practice | Training | Torpedoes | 5 | Torpedo | 1920 | 0 | 100000 | 3 | 200000 | 3 | INTERWAR PRACTICE | 21" × 20 ft, dummy warhead, 30 kts, reusable | Training Torpedo |  | INTERWAR PRACTICE |
| 1351 | Japanese | Type 93 Practice | Training | Torpedoes | 7 | Torpedo | 1935 | 0 | 300000 | 6 | 600000 | 6 | OXYGEN PRACTICE | 24" × 29.5 ft, oxygen fuel, dummy warhead, Type 93 training | Training Torpedo |  | OXYGEN PRACTICE |
| 1352 | Japanese | Type 91 Practice | Training | Torpedoes | 7 | Torpedo | 1935 | 0 | 250000 | 5 | 500000 | 5 | AERIAL PRACTICE | 18" × 17 ft, carrier training, recoverable, dummy warhead | Training Torpedo |  | AERIAL PRACTICE |
| 1353 | Japanese | Type 89 Export | Alcohol | Torpedoes | 6 | Torpedo | 1936 | 0 | 400000 | 8 | 800000 | 8 | EXPORT VERSION | 21" × 23.5 ft, 660 lbs, 42 kts, 10,000 yd, simplified | Alcohol Torpedo |  | EXPORT VERSION |
| 1354 | Japanese | Type 91 (Thailand) | Compressed Air | Torpedoes | 7 | Torpedo | 1941 | 0 | 600000 | 9 | 1200000 | 9 | THAI NAVY | 18" × 17 ft, export aerial torpedo, limited production | Compressed Air Torpedo |  | THAI NAVY |
| 1355 | Japanese | Type 5 Mine-Layer | Special | Torpedoes | 7 | Torpedo | 1940 | 0 | 800000 | 10 | 1600000 | 10 | MINE-LAYING | 21" × 23.5 ft, lays Type 2 mine, submarine-launched | Special Torpedo |  | MINE-LAYING |
| 1356 | Japanese | Type 3 ASW | Acoustic | Torpedoes | 8 | Torpedo | 1943 | 0 | 1500000 | 12 | 3000000 | 12 | ANTI-SUBMARINE | 18" × 18 ft, acoustic homing, 30 kts, anti-submarine role | Acoustic Torpedo |  | ANTI-SUBMARINE |
| 1357 | Japanese | Type 7 (Depth Charge) | Special | Torpedoes | 8 | Torpedo | 1944 | 0 | 1200000 | 10 | 2400000 | 10 | ROCKET ASW | Rocket-propelled depth charge, hybrid torpedo/DC | Special Torpedo |  | ROCKET ASW |
| 1358 | Japanese | Type 89 Mod 1 (JMSDF) | Wire-Guided | Torpedoes | 10 | Torpedo | 1975 | 0 | 7000000 | 20 | 14000000 | 20 | COLD WAR | 21" × 21 ft, active/passive, 50 kts, 30,000 yd | Wire-Guided Torpedo |  | COLD WAR |
| 1359 | Japanese | GRX-2 Prototype | Wire-Guided | Torpedoes | 10 | Torpedo | 1978 | 0 | 8000000 | 21 | 16000000 | 21 | EXPERIMENTAL | 21" × 21 ft, digital guidance, 52 kts, 35,000 yd, trial | Wire-Guided Torpedo |  | EXPERIMENTAL |
| 1360 | Japanese | GRX-3 Advanced | Wire-Guided | Torpedoes | 10 | Torpedo | 1980 | 0 | 9000000 | 22 | 18000000 | 22 | MODERN | 21" × 21 ft, fiber-optic wire, 55 kts, 38,000 yd | Wire-Guided Torpedo |  | MODERN |
| 1361 | Japanese | Type 89 Mod 2 | Wire-Guided | Torpedoes | 10 | Torpedo | 1985 | 0 | 10000000 | 23 | 20000000 | 23 | FINAL INDIGENOUS | 21" × 21 ft, active/passive, 55 kts, 40,000 yd, last domestic design | Wire-Guided Torpedo |  | FINAL INDIGENOUS |
| 2000 | USA | RIM-2 Terrier | 1956 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2001,2010 |
| 2001 | USA | RIM-2C Terrier BT-3 | 1958 | Missiles | SAM | Missile | 2500 | 2 | 5000 | 2 | 15 | 35 | 0 | 0 | 0 | 2000 | 2002 |
| 2002 | USA | RIM-2D Terrier HT-3 | 1961 | Missiles | SAM | Missile | 3000 | 3 | 6000 | 3 | 18 | 42 | 0 | 0 | 0 | 2001 | 2003 |
| 2003 | USA | RIM-2E Terrier (Nuclear) | 1962 | Missiles | SAM | Missile | 4500 | 3 | 9000 | 3 | 20 | 50 | 0 | 0 | 0 | 2002 | 2004 |
| 2004 | USA | RIM-2F Terrier Mod 7 | 1966 | Missiles | SAM | Missile | 3500 | 3 | 7000 | 3 | 22 | 55 | 0 | 0 | 0 | 2003 | 2005 |
| 2005 | USA | RIM-67A Standard MR | 1967 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 25 | 65 | 0 | 0 | 0 | 2004 | 2006,2020 |
| 2006 | USA | RIM-67B Standard ER Block I | 1974 | Missiles | SAM | Missile | 6000 | 5 | 12000 | 5 | 28 | 75 | 0 | 0 | 0 | 2005 | 2007 |
| 2007 | USA | RIM-67C Standard ER Block II | 1981 | Missiles | SAM | Missile | 7000 | 6 | 14000 | 6 | 30 | 85 | 0 | 0 | 0 | 2006 | 2008 |
| 2008 | USA | RIM-67D Standard ER Block IV | 1992 | Missiles | SAM | Missile | 8500 | 7 | 17000 | 7 | 32 | 95 | 0 | 0 | 0 | 2007 | 2009 |
| 2009 | USA | RIM-156A SM-2ER Block IV | 2000 | Missiles | SAM | Missile | 9500 | 8 | 19000 | 8 | 35 | 105 | 0 | 0 | 0 | 2008 | 2025 |
| 2010 | USA | RIM-8 Talos | 1959 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2011 |
| 2011 | USA | RIM-8A Talos Beam Rider | 1960 | Missiles | SAM | Missile | 3500 | 3 | 7000 | 3 | 22 | 45 | 0 | 0 | 0 | 2010 | 2012 |
| 2012 | USA | RIM-8B Talos Semi-Active | 1963 | Missiles | SAM | Missile | 4000 | 4 | 8000 | 4 | 25 | 52 | 0 | 0 | 0 | 2011 | 2013 |
| 2013 | USA | RIM-8D Talos ARM | 1968 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 28 | 60 | 0 | 0 | 0 | 2012 | 2014 |
| 2014 | USA | RIM-8E Talos (Nuclear) | 1965 | Missiles | SAM | Missile | 6000 | 5 | 12000 | 5 | 30 | 68 | 0 | 0 | 0 | 2013 | 2005 |
| 2015 | USA | RIM-24 Tartar | 1963 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2016 |
| 2016 | USA | RIM-24A Tartar Beam Rider | 1964 | Missiles | SAM | Missile | 2000 | 2 | 4000 | 2 | 12 | 30 | 0 | 0 | 0 | 2015 | 2017 |
| 2017 | USA | RIM-24B Tartar Mod 0 | 1967 | Missiles | SAM | Missile | 2500 | 2 | 5000 | 2 | 15 | 38 | 0 | 0 | 0 | 2016 | 2018 |
| 2018 | USA | RIM-24C Tartar Mod 1 | 1970 | Missiles | SAM | Missile | 3000 | 3 | 6000 | 3 | 18 | 45 | 0 | 0 | 0 | 2017 | 2019 |
| 2019 | USA | RIM-66A Standard MR Block I | 1971 | Missiles | SAM | Missile | 4000 | 3 | 8000 | 3 | 20 | 55 | 0 | 0 | 0 | 2018 | 2020 |
| 2020 | USA | RIM-66B Standard MR Block II | 1978 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 22 | 65 | 0 | 0 | 0 | 2019,2005 | 2021 |
| 2021 | USA | RIM-66C Standard MR Block III | 1983 | Missiles | SAM | Missile | 6000 | 5 | 12000 | 5 | 25 | 75 | 0 | 0 | 0 | 2020 | 2022 |
| 2022 | USA | RIM-66E SM-1MR Block VI | 1990 | Missiles | SAM | Missile | 7000 | 5 | 14000 | 5 | 28 | 85 | 0 | 0 | 0 | 2021 | 2023 |
| 2023 | USA | RIM-66M SM-1MR Block VIA | 1995 | Missiles | SAM | Missile | 7500 | 6 | 15000 | 6 | 30 | 92 | 0 | 0 | 0 | 2022 | 2024 |
| 2024 | USA | RIM-161A SM-3 Block IA | 2005 | Missiles | SAM | Missile | 12000 | 10 | 24000 | 10 | 40 | 140 | 0 | 0 | 0 | 2023,2025 | 2026 |
| 2025 | USA | RIM-174A Standard ERAM | 2008 | Missiles | SAM | Missile | 10000 | 9 | 20000 | 9 | 35 | 120 | 0 | 0 | 0 | 2009 | 2024,2027 |
| 2026 | USA | RIM-161B SM-3 Block IB | 2009 | Missiles | SAM | Missile | 13000 | 11 | 26000 | 11 | 42 | 150 | 0 | 0 | 0 | 2024 | 2028 |
| 2027 | USA | RIM-174B Standard ERAM Block II | 2015 | Missiles | SAM | Missile | 11000 | 9 | 22000 | 9 | 38 | 130 | 0 | 0 | 0 | 2025 | 2029 |
| 2028 | USA | RIM-161C SM-3 Block IIA | 2015 | Missiles | SAM | Missile | 14000 | 12 | 28000 | 12 | 45 | 160 | 0 | 0 | 0 | 2026 | 2030 |
| 2029 | USA | RIM-174C Standard ERAM Block III | 2020 | Missiles | SAM | Missile | 12000 | 10 | 24000 | 10 | 40 | 140 | 0 | 0 | 0 | 2027 | 2030 |
| 2030 | USA | RIM-161D SM-3 Block IIB | 2025 | Missiles | SAM | Missile | 15000 | 13 | 30000 | 13 | 48 | 170 | 0 | 0 | 0 | 2028,2029 |  |
| 2031 | USA | RIM-7 Sea Sparrow | 1969 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2032 |
| 2032 | USA | RIM-7E Sea Sparrow Mk 2 | 1976 | Missiles | SAM | Missile | 1800 | 2 | 3600 | 2 | 10 | 25 | 0 | 0 | 0 | 2031 | 2033 |
| 2033 | USA | RIM-7M Sea Sparrow Mk 5 | 1983 | Missiles | SAM | Missile | 2200 | 2 | 4400 | 2 | 12 | 32 | 0 | 0 | 0 | 2032 | 2034 |
| 2034 | USA | RIM-162A ESSM Block I | 2004 | Missiles | SAM | Missile | 4500 | 4 | 9000 | 4 | 18 | 55 | 0 | 0 | 0 | 2033 | 2035 |
| 2035 | USA | RIM-162B ESSM Block II | 2020 | Missiles | SAM | Missile | 5500 | 5 | 11000 | 5 | 20 | 65 | 0 | 0 | 0 | 2034 |  |
| 2040 | USA | RGM-6 Regulus I | 1955 | Missiles | SSM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2041 |
| 2041 | USA | RGM-6D Regulus I (Nuclear) | 1956 | Missiles | SSM | Missile | 3000 | 3 | 6000 | 3 | 25 | 35 | 0 | 0 | 0 | 2040 | 2042 |
| 2042 | USA | RGM-15 Regulus II | 1958 | Missiles | SSM | Missile | 4500 | 4 | 9000 | 4 | 30 | 45 | 0 | 0 | 0 | 2041 | 2043 |
| 2043 | USA | RGM-84A Harpoon Block 1A | 1977 | Missiles | SSM | Missile | 5000 | 4 | 10000 | 4 | 22 | 58 | 0 | 0 | 0 | 2042 | 2044 |
| 2044 | USA | RGM-84C Harpoon Block 1B | 1982 | Missiles | SSM | Missile | 5500 | 5 | 11000 | 5 | 24 | 65 | 0 | 0 | 0 | 2043 | 2045 |
| 2045 | USA | RGM-84D Harpoon Block 1C | 1984 | Missiles | SSM | Missile | 6000 | 5 | 12000 | 5 | 26 | 72 | 0 | 0 | 0 | 2044 | 2046 |
| 2046 | USA | RGM-84F Harpoon Block II | 1998 | Missiles | SSM | Missile | 7500 | 6 | 15000 | 6 | 28 | 85 | 0 | 0 | 0 | 2045 | 2047 |
| 2047 | USA | RGM-84L Harpoon Block II+ | 2008 | Missiles | SSM | Missile | 8500 | 7 | 17000 | 7 | 30 | 95 | 0 | 0 | 0 | 2046 | 2048 |
| 2048 | USA | RGM-84N Harpoon Block II ER | 2016 | Missiles | SSM | Missile | 9500 | 8 | 19000 | 8 | 32 | 105 | 0 | 0 | 0 | 2047 |  |
| 2049 | USA | AGM-119 Penguin Mk 2 | 1989 | Missiles | SSM | Missile | 3500 | 3 | 7000 | 3 | 15 | 45 | 0 | 0 | 0 | 2043 | 2050 |
| 2050 | USA | AGM-119B Penguin Mk 3 | 1995 | Missiles | SSM | Missile | 4000 | 3 | 8000 | 3 | 17 | 52 | 0 | 0 | 0 | 2049 |  |
| 2051 | USA | RGM-109A Tomahawk TLAM-A | 1983 | Missiles | SSM | Missile | 8000 | 6 | 16000 | 6 | 35 | 90 | 0 | 0 | 0 | 2045 | 2052 |
| 2052 | USA | RGM-109B Tomahawk TASM | 1987 | Missiles | SSM | Missile | 8500 | 7 | 17000 | 7 | 36 | 95 | 0 | 0 | 0 | 2051 | 2053 |
| 2053 | USA | RGM-109C Tomahawk TLAM-C | 1993 | Missiles | SSM | Missile | 9000 | 7 | 18000 | 7 | 38 | 100 | 0 | 0 | 0 | 2052 | 2054 |
| 2054 | USA | RGM-109E Tomahawk TLAM-E | 2004 | Missiles | SSM | Missile | 10000 | 8 | 20000 | 8 | 40 | 110 | 0 | 0 | 0 | 2053 | 2055 |
| 2055 | USA | RGM-109H Tomahawk TLAM-N | 2007 | Missiles | SSM | Missile | 11000 | 9 | 22000 | 9 | 42 | 120 | 0 | 0 | 0 | 2054 | 2056 |
| 2056 | USA | RGM-109J Tomahawk Block IV | 2010 | Missiles | SSM | Missile | 12000 | 10 | 24000 | 10 | 44 | 130 | 0 | 0 | 0 | 2055 | 2057 |
| 2057 | USA | RGM-109K Tomahawk Block V | 2019 | Missiles | SSM | Missile | 13500 | 11 | 27000 | 11 | 46 | 145 | 0 | 0 | 0 | 2056 | 2058 |
| 2058 | USA | RGM-109L Tomahawk Block VA | 2021 | Missiles | SSM | Missile | 14000 | 11 | 28000 | 11 | 48 | 152 | 0 | 0 | 0 | 2057 |  |
| 2059 | USA | AGM-158C LRASM | 2018 | Missiles | SSM | Missile | 10000 | 8 | 20000 | 8 | 35 | 125 | 0 | 0 | 0 | 2048,2058 | 2060 |
| 2060 | USA | AGM-158C-2 LRASM Block II | 2024 | Missiles | SSM | Missile | 11500 | 9 | 23000 | 9 | 38 | 138 | 0 | 0 | 0 | 2059 |  |
| 2061 | USA | RUR-4 Weapon Alpha | 1951 | Missiles | ASW | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2062 |
| 2062 | USA | RUR-5 ASROC | 1961 | Missiles | ASW | Missile | 2500 | 2 | 5000 | 2 | 18 | 32 | 0 | 0 | 0 | 2061 | 2063 |
| 2063 | USA | RUR-5A ASROC Mod 4 | 1971 | Missiles | ASW | Missile | 3000 | 3 | 6000 | 3 | 20 | 40 | 0 | 0 | 0 | 2062 | 2064 |
| 2064 | USA | RUR-5B ASROC (Nuclear) | 1962 | Missiles | ASW | Missile | 4500 | 4 | 9000 | 4 | 22 | 48 | 0 | 0 | 0 | 2063 | 2065 |
| 2065 | USA | RUM-139A VL-ASROC | 1993 | Missiles | ASW | Missile | 5500 | 5 | 11000 | 5 | 25 | 65 | 0 | 0 | 0 | 2064 | 2066 |
| 2066 | USA | RUM-139B VL-ASROC Block II | 2008 | Missiles | ASW | Missile | 6500 | 5 | 13000 | 5 | 28 | 75 | 0 | 0 | 0 | 2065 | 2067 |
| 2067 | USA | RUM-139C VL-ASROC Block III | 2020 | Missiles | ASW | Missile | 7500 | 6 | 15000 | 6 | 30 | 85 | 0 | 0 | 0 | 2066 |  |
| 2068 | USA | UUM-44A SUBROC | 1965 | Missiles | ASW | Missile | 4000 | 3 | 8000 | 3 | 20 | 45 | 0 | 0 | 0 | 2063 | 2069 |
| 2069 | USA | UUM-44B SUBROC Mod 1 | 1972 | Missiles | ASW | Missile | 4500 | 4 | 9000 | 4 | 22 | 52 | 0 | 0 | 0 | 2068 | 2070 |
| 2070 | USA | UUM-125A Sea Lance | 1988 | Missiles | ASW | Missile | 6000 | 5 | 12000 | 5 | 28 | 68 | 0 | 0 | 0 | 2069 |  |
| 2071 | USA | RIM-116A RAM Block 0 | 1992 | Missiles | CIWS | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2072 |
| 2072 | USA | RIM-116B RAM Block 1 | 2000 | Missiles | CIWS | Missile | 3000 | 3 | 6000 | 3 | 12 | 48 | 0 | 0 | 0 | 2071 | 2073 |
| 2073 | USA | RIM-116C RAM Block 2 | 2015 | Missiles | CIWS | Missile | 4000 | 3 | 8000 | 3 | 15 | 58 | 0 | 0 | 0 | 2072 | 2074 |
| 2074 | USA | RIM-116D RAM Block 2A | 2020 | Missiles | CIWS | Missile | 4500 | 4 | 9000 | 4 | 17 | 65 | 0 | 0 | 0 | 2073 |  |
| 2075 | USA | Mk 108 Weapon Alfa Rocket | 1959 | Missiles | ASW | Missile | 800 | 1 | 1600 | 1 | 8 | 12 | 0 | 0 | 0 | 2062 | 2076 |
| 2076 | USA | Mk 112 ASROC Rocket | 1963 | Missiles | ASW | Missile | 1000 | 1 | 2000 | 1 | 10 | 15 | 0 | 0 | 0 | 2075 | 2077 |
| 2077 | USA | Mk 113 ASROC Rocket Mod 7 | 1968 | Missiles | ASW | Missile | 1200 | 1 | 2400 | 1 | 12 | 18 | 0 | 0 | 0 | 2076 | 2078 |
| 2078 | USA | RIM-7P Sea Sparrow CIWS | 1980 | Missiles | CIWS | Missile | 2000 | 2 | 4000 | 2 | 10 | 30 | 0 | 0 | 0 | 2032 | 2071 |
| 2079 | USA | SM-6 Block IA Dual I | 2013 | Missiles | SAM | Missile | 10500 | 9 | 21000 | 9 | 36 | 125 | 0 | 0 | 0 | 2025 | 2080 |
| 2080 | USA | SM-6 Block IB Dual II | 2017 | Missiles | SAM | Missile | 11500 | 10 | 23000 | 10 | 38 | 135 | 0 | 0 | 0 | 2079 | 2030 |
| 2090 | USA | BGM-109G GLCM (Nuclear) | 1983 | Missiles | Cruise | Missile | 9000 | 7 | 18000 | 7 | 38 | 92 | 0 | 0 | 0 | 2051 | 2091 |
| 2091 | USA | AGM-86C CALCM | 1996 | Missiles | Cruise | Missile | 8500 | 7 | 17000 | 7 | 35 | 88 | 0 | 0 | 0 | 2090 | 2092 |
| 2092 | USA | AGM-86D CALCM Block II | 2002 | Missiles | Cruise | Missile | 9000 | 7 | 18000 | 7 | 37 | 95 | 0 | 0 | 0 | 2091 | 2093 |
| 2093 | USA | AGM-154A JSOW | 1999 | Missiles | Cruise | Missile | 6000 | 5 | 12000 | 5 | 25 | 70 | 0 | 0 | 0 | 2054 | 2094 |
| 2094 | USA | AGM-154C JSOW-C | 2005 | Missiles | Cruise | Missile | 6500 | 6 | 13000 | 6 | 27 | 78 | 0 | 0 | 0 | 2093 | 2095 |
| 2095 | USA | AGM-154E JSOW-E | 2015 | Missiles | Cruise | Missile | 7000 | 6 | 14000 | 6 | 29 | 85 | 0 | 0 | 0 | 2094 |  |
| 2096 | USA | AGM-129A ACM | 1990 | Missiles | Cruise | Missile | 10000 | 8 | 20000 | 8 | 40 | 105 | 0 | 0 | 0 | 2090 | 2097 |
| 2097 | USA | AGM-129B ACM (Stealth) | 1993 | Missiles | Cruise | Missile | 11000 | 9 | 22000 | 9 | 42 | 115 | 0 | 0 | 0 | 2096 |  |
| 2098 | USA | BGM-109A Gryphon | 1984 | Missiles | Cruise | Missile | 7500 | 6 | 15000 | 6 | 32 | 82 | 0 | 0 | 0 | 2051 | 2099 |
| 2099 | USA | BGM-109B Gryphon Mod 1 | 1987 | Missiles | Cruise | Missile | 8000 | 7 | 16000 | 7 | 34 | 88 | 0 | 0 | 0 | 2098 |  |
| 2100 | USA | AGM-158A JASSM | 2003 | Missiles | Cruise | Missile | 7000 | 6 | 14000 | 6 | 28 | 80 | 0 | 0 | 0 | 2054 | 2101 |
| 2101 | USA | AGM-158B JASSM-ER | 2014 | Missiles | Cruise | Missile | 8000 | 7 | 16000 | 7 | 32 | 92 | 0 | 0 | 0 | 2100 | 2059 |
| 2102 | USA | Conventional Prompt Strike | 2022 | Missiles | Hypersonic | Missile | 15000 | 12 | 30000 | 12 | 50 | 165 | 0 | 0 | 0 | 2058,2060 | 2103 |
| 2103 | USA | CPS Block II | 2025 | Missiles | Hypersonic | Missile | 16500 | 13 | 33000 | 13 | 52 | 175 | 0 | 0 | 0 | 2102 |  |
| 2104 | USA | SSM-N-8A Regulus (Sub) | 1954 | Missiles | Cruise | Missile | 2500 | 2 | 5000 | 2 | 22 | 30 | 0 | 0 | 0 | 2040 | 2105 |
| 2105 | USA | SSM-N-8B Regulus (Improved) | 1957 | Missiles | Cruise | Missile | 3000 | 3 | 6000 | 3 | 24 | 36 | 0 | 0 | 0 | 2104 | 2042 |
| 2106 | USA | RIM-85A Talos ARM | 1969 | Missiles | SAM | Missile | 4500 | 4 | 9000 | 4 | 26 | 58 | 0 | 0 | 0 | 2013 | 2107 |
| 2107 | USA | AGM-78 Standard ARM | 1968 | Missiles | SAM | Missile | 4000 | 4 | 8000 | 4 | 24 | 54 | 0 | 0 | 0 | 2106 | 2108 |
| 2108 | USA | AGM-78D Standard ARM Mod 5 | 1975 | Missiles | SAM | Missile | 4500 | 4 | 9000 | 4 | 26 | 62 | 0 | 0 | 0 | 2107 | 2020 |
| 2109 | USA | RIM-8G Talos ARM Mk 5 | 1972 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 28 | 65 | 0 | 0 | 0 | 2106 | 2014 |
| 2200 | British | Sea Slug Mk 1 | 1961 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2201 |
| 2201 | British | Sea Slug Mk 2 | 1967 | Missiles | SAM | Missile | 3500 | 3 | 7000 | 3 | 25 | 45 | 0 | 0 | 0 | 2200 | 2202 |
| 2202 | British | Sea Slug Mk 3 (Nuclear) | 1970 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 28 | 55 | 0 | 0 | 0 | 2201 | 2210 |
| 2210 | British | Sea Dart GWS.30 | 1973 | Missiles | SAM | Missile | 4500 | 4 | 9000 | 4 | 22 | 60 | 0 | 0 | 0 | 2202 | 2211 |
| 2211 | British | Sea Dart Mod 1 | 1978 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 24 | 68 | 0 | 0 | 0 | 2210 | 2212 |
| 2212 | British | Sea Dart Mod 2 | 1985 | Missiles | SAM | Missile | 5500 | 5 | 11000 | 5 | 26 | 75 | 0 | 0 | 0 | 2211 | 2213 |
| 2213 | British | Sea Dart Mod 3 | 1995 | Missiles | SAM | Missile | 6000 | 5 | 12000 | 5 | 28 | 82 | 0 | 0 | 0 | 2212 | 2214 |
| 2214 | British | Sea Viper Aster 15 | 2009 | Missiles | SAM | Missile | 7500 | 6 | 15000 | 6 | 30 | 100 | 0 | 0 | 0 | 2213 | 2215 |
| 2215 | British | Sea Viper Aster 30 | 2011 | Missiles | SAM | Missile | 8500 | 7 | 17000 | 7 | 32 | 110 | 0 | 0 | 0 | 2214 | 2216 |
| 2216 | British | Sea Viper Block 1NT | 2020 | Missiles | SAM | Missile | 9500 | 8 | 19000 | 8 | 35 | 120 | 0 | 0 | 0 | 2215 |  |
| 2220 | British | Sea Wolf GWS.25 | 1979 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2221 |
| 2221 | British | Sea Wolf GWS.26 VLS | 1990 | Missiles | SAM | Missile | 3500 | 3 | 7000 | 3 | 18 | 55 | 0 | 0 | 0 | 2220 | 2222 |
| 2222 | British | Sea Wolf Mod 1 | 1995 | Missiles | SAM | Missile | 4000 | 3 | 8000 | 3 | 20 | 62 | 0 | 0 | 0 | 2221 | 2223 |
| 2223 | British | CAMM (Sea Ceptor) | 2016 | Missiles | SAM | Missile | 5500 | 5 | 11000 | 5 | 22 | 80 | 0 | 0 | 0 | 2222 | 2224 |
| 2224 | British | CAMM-ER | 2021 | Missiles | SAM | Missile | 6500 | 6 | 13000 | 6 | 24 | 92 | 0 | 0 | 0 | 2223 |  |
| 2230 | British | Bloodhound Mk I | 1958 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2231 |
| 2231 | British | Bloodhound Mk II | 1964 | Missiles | SAM | Missile | 2500 | 2 | 5000 | 2 | 20 | 38 | 0 | 0 | 0 | 2230 | 2232 |
| 2232 | British | Bloodhound Mk III | 1972 | Missiles | SAM | Missile | 3000 | 3 | 6000 | 3 | 22 | 45 | 0 | 0 | 0 | 2231 | 2210 |
| 2240 | British | MM38 Exocet | 1975 | Missiles | SSM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2241 |
| 2241 | British | MM40 Exocet Block 1 | 1981 | Missiles | SSM | Missile | 4500 | 4 | 9000 | 4 | 22 | 58 | 0 | 0 | 0 | 2240 | 2242 |
| 2242 | British | MM40 Exocet Block 2 | 1992 | Missiles | SSM | Missile | 5500 | 5 | 11000 | 5 | 25 | 68 | 0 | 0 | 0 | 2241 | 2243 |
| 2243 | British | MM40 Exocet Block 3 | 2008 | Missiles | SSM | Missile | 6500 | 5 | 13000 | 5 | 28 | 80 | 0 | 0 | 0 | 2242 | 2244 |
| 2244 | British | MM40 Block 3C | 2015 | Missiles | SSM | Missile | 7000 | 6 | 14000 | 6 | 30 | 88 | 0 | 0 | 0 | 2243 | 2245 |
| 2245 | British | Sea Venom ANL | 2020 | Missiles | SSM | Missile | 8000 | 7 | 16000 | 7 | 32 | 100 | 0 | 0 | 0 | 2244 |  |
| 2246 | British | Sea Skua CL834 | 1982 | Missiles | SSM | Missile | 3000 | 3 | 6000 | 3 | 15 | 42 | 0 | 0 | 0 | 2241 | 2247 |
| 2247 | British | Sea Skua Mk 2 | 1990 | Missiles | SSM | Missile | 3500 | 3 | 7000 | 3 | 17 | 48 | 0 | 0 | 0 | 2246 | 2248 |
| 2248 | British | Martlet (Sea Venom Light) | 2021 | Missiles | SSM | Missile | 4500 | 4 | 9000 | 4 | 18 | 58 | 0 | 0 | 0 | 2247 |  |
| 2249 | British | Storm Shadow | 2002 | Missiles | Cruise | Missile | 7000 | 6 | 14000 | 6 | 30 | 85 | 0 | 0 | 0 | 2243 | 2250 |
| 2250 | British | Storm Shadow Block II | 2015 | Missiles | Cruise | Missile | 8000 | 7 | 16000 | 7 | 33 | 95 | 0 | 0 | 0 | 2249 |  |
| 2251 | British | Tomahawk Block IV (UK) | 2008 | Missiles | Cruise | Missile | 10000 | 8 | 20000 | 8 | 38 | 115 | 0 | 0 | 0 | 2243 | 2252 |
| 2252 | British | Tomahawk Block V (UK) | 2021 | Missiles | Cruise | Missile | 11500 | 9 | 23000 | 9 | 42 | 130 | 0 | 0 | 0 | 2251 |  |
| 2260 | British | Ikara GWS.40 | 1968 | Missiles | ASW | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2261 |
| 2261 | British | Ikara Mod 1 | 1973 | Missiles | ASW | Missile | 2500 | 2 | 5000 | 2 | 18 | 35 | 0 | 0 | 0 | 2260 | 2262 |
| 2262 | British | Ikara Mod 2 | 1978 | Missiles | ASW | Missile | 3000 | 3 | 6000 | 3 | 20 | 42 | 0 | 0 | 0 | 2261 | 2263 |
| 2263 | British | Stingray ASW Missile | 1989 | Missiles | ASW | Missile | 4000 | 3 | 8000 | 3 | 22 | 52 | 0 | 0 | 0 | 2262 | 2264 |
| 2264 | British | Sea Urchin ASW | 2005 | Missiles | ASW | Missile | 5000 | 4 | 10000 | 4 | 25 | 65 | 0 | 0 | 0 | 2263 | 2265 |
| 2265 | British | Sea Spear ASW | 2020 | Missiles | ASW | Missile | 6000 | 5 | 12000 | 5 | 28 | 75 | 0 | 0 | 0 | 2264 |  |
| 2300 | German | RIM-24B Tartar (German) | 1969 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2301 |
| 2301 | German | RIM-66A Standard MR (German) | 1975 | Missiles | SAM | Missile | 3500 | 3 | 7000 | 3 | 20 | 52 | 0 | 0 | 0 | 2300 | 2302 |
| 2302 | German | SM-1MR Block VI (German) | 1990 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 25 | 70 | 0 | 0 | 0 | 2301 | 2310 |
| 2310 | German | RAM Block 0 (German) | 1992 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2311 |
| 2311 | German | RAM Block 1 | 2000 | Missiles | SAM | Missile | 3000 | 3 | 6000 | 3 | 12 | 48 | 0 | 0 | 0 | 2310 | 2312 |
| 2312 | German | RAM Block 2 | 2015 | Missiles | SAM | Missile | 4000 | 3 | 8000 | 3 | 15 | 58 | 0 | 0 | 0 | 2311 | 2313 |
| 2313 | German | RAM Block 2A | 2020 | Missiles | SAM | Missile | 4500 | 4 | 9000 | 4 | 17 | 65 | 0 | 0 | 0 | 2312 |  |
| 2314 | German | Sea Sparrow NATO | 1976 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2315 |
| 2315 | German | ESSM Block I (German) | 2005 | Missiles | SAM | Missile | 4000 | 3 | 8000 | 3 | 18 | 55 | 0 | 0 | 0 | 2314 | 2316 |
| 2316 | German | ESSM Block II (German) | 2020 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 20 | 65 | 0 | 0 | 0 | 2315 |  |
| 2317 | German | IRIS-T SLM | 2014 | Missiles | SAM | Missile | 5500 | 5 | 11000 | 5 | 22 | 75 | 0 | 0 | 0 | 2312,2315 | 2318 |
| 2318 | German | IRIS-T SLM Block II | 2022 | Missiles | SAM | Missile | 6500 | 6 | 13000 | 6 | 24 | 85 | 0 | 0 | 0 | 2317 |  |
| 2340 | German | MM38 Exocet (German) | 1977 | Missiles | SSM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2341 |
| 2341 | German | MM40 Exocet Block 2 | 1992 | Missiles | SSM | Missile | 5000 | 4 | 10000 | 4 | 24 | 65 | 0 | 0 | 0 | 2340 | 2342 |
| 2342 | German | MM40 Block 3 (German) | 2010 | Missiles | SSM | Missile | 6000 | 5 | 12000 | 5 | 28 | 78 | 0 | 0 | 0 | 2341 | 2343 |
| 2343 | German | RGM-84 Harpoon (German) | 1985 | Missiles | SSM | Missile | 5500 | 5 | 11000 | 5 | 26 | 70 | 0 | 0 | 0 | 2341 | 2344 |
| 2344 | German | Harpoon Block II (German) | 2000 | Missiles | SSM | Missile | 6500 | 5 | 13000 | 5 | 28 | 82 | 0 | 0 | 0 | 2343 | 2345 |
| 2345 | German | NSM (German) | 2017 | Missiles | SSM | Missile | 8000 | 7 | 16000 | 7 | 32 | 100 | 0 | 0 | 0 | 2344 | 2346 |
| 2346 | German | NSM Block II | 2023 | Missiles | SSM | Missile | 9000 | 7 | 18000 | 7 | 35 | 112 | 0 | 0 | 0 | 2345 |  |
| 2347 | German | Kormoran Mk 1 | 1977 | Missiles | SSM | Missile | 3000 | 3 | 6000 | 3 | 18 | 42 | 0 | 0 | 0 | 2340 | 2348 |
| 2348 | German | Kormoran Mk 2 | 1991 | Missiles | SSM | Missile | 3500 | 3 | 7000 | 3 | 20 | 48 | 0 | 0 | 0 | 2347 | 2349 |
| 2349 | German | IDAS (Sub-Launched) | 2008 | Missiles | SSM | Missile | 4500 | 4 | 9000 | 4 | 22 | 60 | 0 | 0 | 0 | 2348 |  |
| 2360 | German | VL-ASROC (German) | 1995 | Missiles | ASW | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2361 |
| 2361 | German | VL-ASROC Block II (German) | 2010 | Missiles | ASW | Missile | 5500 | 5 | 11000 | 5 | 26 | 68 | 0 | 0 | 0 | 2360 | 2362 |
| 2362 | German | RUM-139C (NATO) | 2022 | Missiles | ASW | Missile | 6500 | 5 | 13000 | 5 | 28 | 78 | 0 | 0 | 0 | 2361 |  |
| 2363 | German | Sea Urchin (License) | 2012 | Missiles | ASW | Missile | 4500 | 4 | 9000 | 4 | 22 | 58 | 0 | 0 | 0 | 2361 | 2362 |
| 2400 | Japanese | RIM-24 Tartar (JMSDF) | 1970 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2401 |
| 2401 | Japanese | RIM-66A Standard MR (JMSDF) | 1978 | Missiles | SAM | Missile | 3500 | 3 | 7000 | 3 | 20 | 52 | 0 | 0 | 0 | 2400 | 2402 |
| 2402 | Japanese | SM-1MR Block VI (JMSDF) | 1990 | Missiles | SAM | Missile | 5000 | 4 | 10000 | 4 | 25 | 70 | 0 | 0 | 0 | 2401 | 2403,2410 |
| 2403 | Japanese | Type 03 Chū-SAM Kai | 2003 | Missiles | SAM | Missile | 6000 | 5 | 12000 | 5 | 28 | 82 | 0 | 0 | 0 | 2402 | 2404 |
| 2404 | Japanese | Type 03 Mod 4 | 2010 | Missiles | SAM | Missile | 7000 | 6 | 14000 | 6 | 30 | 92 | 0 | 0 | 0 | 2403 | 2405 |
| 2405 | Japanese | Type 03 Mod 5 (AESA) | 2017 | Missiles | SAM | Missile | 8000 | 7 | 16000 | 7 | 32 | 105 | 0 | 0 | 0 | 2404 | 2406 |
| 2406 | Japanese | Type 03 Mod 6 | 2024 | Missiles | SAM | Missile | 9000 | 7 | 18000 | 7 | 35 | 118 | 0 | 0 | 0 | 2405 |  |
| 2410 | Japanese | Type 07 VLS SAM | 2007 | Missiles | SAM | Missile | 6500 | 5 | 13000 | 5 | 28 | 85 | 0 | 0 | 0 | 2402 | 2411 |
| 2411 | Japanese | Type 07 Mod 2 | 2015 | Missiles | SAM | Missile | 7500 | 6 | 15000 | 6 | 30 | 95 | 0 | 0 | 0 | 2410 | 2412 |
| 2412 | Japanese | Type 07 Mod 3 (AESA) | 2022 | Missiles | SAM | Missile | 8500 | 7 | 17000 | 7 | 32 | 108 | 0 | 0 | 0 | 2411 |  |
| 2420 | Japanese | RIM-7 Sea Sparrow (JMSDF) | 1981 | Missiles | SAM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2421 |
| 2421 | Japanese | RIM-7M Sea Sparrow (JMSDF) | 1988 | Missiles | SAM | Missile | 2200 | 2 | 4400 | 2 | 12 | 32 | 0 | 0 | 0 | 2420 | 2422 |
| 2422 | Japanese | ESSM Block I (JMSDF) | 2008 | Missiles | SAM | Missile | 4500 | 4 | 9000 | 4 | 18 | 55 | 0 | 0 | 0 | 2421 | 2423 |
| 2423 | Japanese | ESSM Block II (JMSDF) | 2021 | Missiles | SAM | Missile | 5500 | 5 | 11000 | 5 | 20 | 65 | 0 | 0 | 0 | 2422 |  |
| 2424 | Japanese | Type 91 Kai-MANPAD (Naval) | 1995 | Missiles | SAM | Missile | 1500 | 2 | 3000 | 2 | 8 | 22 | 0 | 0 | 0 | 2421 | 2425 |
| 2425 | Japanese | Type 93 SAM (Naval Adaptation) | 2008 | Missiles | SAM | Missile | 2500 | 2 | 5000 | 2 | 10 | 32 | 0 | 0 | 0 | 2424 |  |
| 2440 | Japanese | SSM-1 Type 88 | 1988 | Missiles | SSM | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2441 |
| 2441 | Japanese | SSM-1A Type 88 Mod 1 | 1993 | Missiles | SSM | Missile | 5000 | 4 | 10000 | 4 | 24 | 62 | 0 | 0 | 0 | 2440 | 2442 |
| 2442 | Japanese | SSM-1B Type 90 | 1998 | Missiles | SSM | Missile | 6000 | 5 | 12000 | 5 | 28 | 75 | 0 | 0 | 0 | 2441 | 2443 |
| 2443 | Japanese | Type 12 SSM Block 0 | 2012 | Missiles | SSM | Missile | 7500 | 6 | 15000 | 6 | 32 | 95 | 0 | 0 | 0 | 2442 | 2444 |
| 2444 | Japanese | Type 12 SSM Block 1 | 2018 | Missiles | SSM | Missile | 8500 | 7 | 17000 | 7 | 35 | 108 | 0 | 0 | 0 | 2443 | 2445 |
| 2445 | Japanese | Type 12 SSM Block 2 | 2023 | Missiles | SSM | Missile | 9500 | 8 | 19000 | 8 | 38 | 122 | 0 | 0 | 0 | 2444 |  |
| 2446 | Japanese | ASM-1C | 1987 | Missiles | SSM | Missile | 3500 | 3 | 7000 | 3 | 18 | 45 | 0 | 0 | 0 | 2440 | 2447 |
| 2447 | Japanese | ASM-2 | 1995 | Missiles | SSM | Missile | 4500 | 4 | 9000 | 4 | 22 | 58 | 0 | 0 | 0 | 2446 | 2448 |
| 2448 | Japanese | ASM-3 | 2016 | Missiles | SSM | Missile | 7000 | 6 | 14000 | 6 | 30 | 88 | 0 | 0 | 0 | 2447 | 2449 |
| 2449 | Japanese | ASM-3A (Extended Range) | 2022 | Missiles | SSM | Missile | 8000 | 7 | 16000 | 7 | 32 | 98 | 0 | 0 | 0 | 2448 |  |
| 2450 | Japanese | RGM-84 Harpoon (JMSDF) | 1982 | Missiles | SSM | Missile | 4500 | 4 | 9000 | 4 | 22 | 58 | 0 | 0 | 0 | 2440 | 2451 |
| 2451 | Japanese | Harpoon Block II (JMSDF) | 2005 | Missiles | SSM | Missile | 6000 | 5 | 12000 | 5 | 26 | 75 | 0 | 0 | 0 | 2450 |  |
| 2460 | Japanese | RUR-5 ASROC (JMSDF) | 1977 | Missiles | ASW | Missile | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 2461 |
| 2461 | Japanese | Type 07 VLA | 2007 | Missiles | ASW | Missile | 5500 | 5 | 11000 | 5 | 25 | 68 | 0 | 0 | 0 | 2460 | 2462 |
| 2462 | Japanese | Type 07 VLA Mod 2 | 2018 | Missiles | ASW | Missile | 6500 | 5 | 13000 | 5 | 28 | 78 | 0 | 0 | 0 | 2461 | 2463 |
| 2463 | Japanese | Type 07 VLA Mod 3 | 2024 | Missiles | ASW | Missile | 7500 | 6 | 15000 | 6 | 30 | 88 | 0 | 0 | 0 | 2462 |  |
| 3000 | USA | F4F Wildcat | 1940 | Naval Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3001 |
| 3001 | USA | F4F-4 Wildcat | 1942 | Naval Aircraft | Fighter | Aircraft | 2000 | 2 | 4000 | 2 | 12 | 18 | 0 | 0 | 0 | 3000 | 3002 |
| 3002 | USA | F6F Hellcat | 1943 | Naval Aircraft | Fighter | Aircraft | 3500 | 3 | 7000 | 3 | 18 | 28 | 0 | 0 | 0 | 3001 | 3003 |
| 3003 | USA | F6F-5 Hellcat | 1944 | Naval Aircraft | Fighter | Aircraft | 3800 | 3 | 7600 | 3 | 20 | 32 | 0 | 0 | 0 | 3002 | 3004 |
| 3004 | USA | F8F Bearcat | 1945 | Naval Aircraft | Fighter | Aircraft | 4200 | 3 | 8400 | 3 | 22 | 38 | 0 | 0 | 0 | 3003 | 3010 |
| 3010 | USA | F9F Panther | 1949 | Naval Aircraft | Jet Fighter | Aircraft | 5000 | 4 | 10000 | 4 | 28 | 48 | 0 | 0 | 0 | 3004 | 3011 |
| 3011 | USA | F9F-5 Panther | 1950 | Naval Aircraft | Jet Fighter | Aircraft | 5500 | 4 | 11000 | 4 | 30 | 52 | 0 | 0 | 0 | 3010 | 3012 |
| 3012 | USA | F9F-8 Cougar | 1954 | Naval Aircraft | Jet Fighter | Aircraft | 6000 | 5 | 12000 | 5 | 32 | 58 | 0 | 0 | 0 | 3011 | 3013 |
| 3013 | USA | F11F Tiger | 1956 | Naval Aircraft | Jet Fighter | Aircraft | 6500 | 5 | 13000 | 5 | 35 | 65 | 0 | 0 | 0 | 3012 | 3014 |
| 3014 | USA | F8U Crusader | 1957 | Naval Aircraft | Jet Fighter | Aircraft | 7000 | 6 | 14000 | 6 | 38 | 72 | 0 | 0 | 0 | 3013 | 3015 |
| 3015 | USA | F8U-2 Crusader | 1960 | Naval Aircraft | Jet Fighter | Aircraft | 7500 | 6 | 15000 | 6 | 40 | 78 | 0 | 0 | 0 | 3014 | 3020 |
| 3020 | USA | F-4B Phantom II | 1962 | Naval Aircraft | Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 45 | 95 | 0 | 0 | 0 | 3015 | 3021 |
| 3021 | USA | F-4J Phantom II | 1966 | Naval Aircraft | Multi-Role | Aircraft | 10000 | 8 | 20000 | 8 | 48 | 105 | 0 | 0 | 0 | 3020 | 3022 |
| 3022 | USA | F-4S Phantom II | 1978 | Naval Aircraft | Multi-Role | Aircraft | 11000 | 8 | 22000 | 8 | 50 | 115 | 0 | 0 | 0 | 3021 | 3030 |
| 3030 | USA | F-14A Tomcat | 1974 | Naval Aircraft | Interceptor | Aircraft | 12000 | 10 | 24000 | 10 | 55 | 135 | 0 | 0 | 0 | 3022 | 3031 |
| 3031 | USA | F-14A+ Tomcat | 1988 | Naval Aircraft | Interceptor | Aircraft | 13000 | 10 | 26000 | 10 | 58 | 145 | 0 | 0 | 0 | 3030 | 3032 |
| 3032 | USA | F-14D Tomcat | 1991 | Naval Aircraft | Interceptor | Aircraft | 14000 | 11 | 28000 | 11 | 60 | 155 | 0 | 0 | 0 | 3031 | 3040 |
| 3040 | USA | F/A-18A Hornet | 1983 | Naval Aircraft | Multi-Role | Aircraft | 11000 | 9 | 22000 | 9 | 48 | 125 | 0 | 0 | 0 | 3022,3030 | 3041 |
| 3041 | USA | F/A-18C Hornet | 1987 | Naval Aircraft | Multi-Role | Aircraft | 12000 | 9 | 24000 | 9 | 50 | 135 | 0 | 0 | 0 | 3040 | 3042 |
| 3042 | USA | F/A-18E Super Hornet | 1999 | Naval Aircraft | Multi-Role | Aircraft | 14000 | 11 | 28000 | 11 | 55 | 155 | 0 | 0 | 0 | 3041 | 3043 |
| 3043 | USA | F/A-18F Super Hornet | 2001 | Naval Aircraft | Multi-Role | Aircraft | 14500 | 11 | 29000 | 11 | 57 | 162 | 0 | 0 | 0 | 3042 | 3044 |
| 3044 | USA | F/A-18E/F Block III | 2019 | Naval Aircraft | Multi-Role | Aircraft | 16000 | 12 | 32000 | 12 | 60 | 180 | 0 | 0 | 0 | 3043 | 3050 |
| 3050 | USA | F-35C Lightning II | 2019 | Naval Aircraft | Stealth Fighter | Aircraft | 20000 | 15 | 40000 | 15 | 70 | 220 | 0 | 0 | 0 | 3044 |  |
| 3051 | USA | F-35C Block 4 | 2025 | Naval Aircraft | Stealth Fighter | Aircraft | 22000 | 16 | 44000 | 16 | 72 | 235 | 0 | 0 | 0 | 3050 |  |
| 3060 | USA | SBD Dauntless | 1940 | Naval Aircraft | Dive Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3061 |
| 3061 | USA | SBD-5 Dauntless | 1943 | Naval Aircraft | Dive Bomber | Aircraft | 2200 | 2 | 4400 | 2 | 15 | 22 | 0 | 0 | 0 | 3060 | 3062 |
| 3062 | USA | SB2C Helldiver | 1943 | Naval Aircraft | Dive Bomber | Aircraft | 2800 | 3 | 5600 | 3 | 18 | 28 | 0 | 0 | 0 | 3061 | 3063 |
| 3063 | USA | AD Skyraider | 1946 | Naval Aircraft | Attack | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 35 | 0 | 0 | 0 | 3062 | 3064 |
| 3064 | USA | AD-6 Skyraider | 1953 | Naval Aircraft | Attack | Aircraft | 4000 | 3 | 8000 | 3 | 25 | 42 | 0 | 0 | 0 | 3063 | 3070 |
| 3070 | USA | A-4 Skyhawk | 1956 | Naval Aircraft | Attack | Aircraft | 5000 | 4 | 10000 | 4 | 28 | 52 | 0 | 0 | 0 | 3064 | 3071 |
| 3071 | USA | A-4E Skyhawk | 1962 | Naval Aircraft | Attack | Aircraft | 5500 | 5 | 11000 | 5 | 30 | 58 | 0 | 0 | 0 | 3070 | 3072 |
| 3072 | USA | A-4M Skyhawk | 1970 | Naval Aircraft | Attack | Aircraft | 6000 | 5 | 12000 | 5 | 32 | 65 | 0 | 0 | 0 | 3071 | 3073 |
| 3073 | USA | A-6A Intruder | 1963 | Naval Aircraft | Attack | Aircraft | 7500 | 6 | 15000 | 6 | 42 | 85 | 0 | 0 | 0 | 3071 | 3074 |
| 3074 | USA | A-6E Intruder | 1970 | Naval Aircraft | Attack | Aircraft | 8500 | 7 | 17000 | 7 | 45 | 95 | 0 | 0 | 0 | 3073 | 3075 |
| 3075 | USA | A-6E TRAM | 1979 | Naval Aircraft | Attack | Aircraft | 9500 | 8 | 19000 | 8 | 48 | 108 | 0 | 0 | 0 | 3074 | 3076 |
| 3076 | USA | A-7 Corsair II | 1967 | Naval Aircraft | Attack | Aircraft | 6500 | 5 | 13000 | 5 | 35 | 72 | 0 | 0 | 0 | 3072 | 3077 |
| 3077 | USA | A-7E Corsair II | 1969 | Naval Aircraft | Attack | Aircraft | 7000 | 6 | 14000 | 6 | 38 | 78 | 0 | 0 | 0 | 3076 | 3040 |
| 3080 | USA | TBF Avenger | 1942 | Naval Aircraft | Torpedo Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3081 |
| 3081 | USA | TBM-3 Avenger | 1944 | Naval Aircraft | Torpedo Bomber | Aircraft | 2500 | 2 | 5000 | 2 | 16 | 24 | 0 | 0 | 0 | 3080 | 3082 |
| 3082 | USA | S-2 Tracker | 1954 | Naval Aircraft | ASW | Aircraft | 4000 | 3 | 8000 | 3 | 25 | 45 | 0 | 0 | 0 | 3081 | 3083 |
| 3083 | USA | S-2E Tracker | 1962 | Naval Aircraft | ASW | Aircraft | 4500 | 4 | 9000 | 4 | 28 | 52 | 0 | 0 | 0 | 3082 | 3084 |
| 3084 | USA | S-3A Viking | 1974 | Naval Aircraft | ASW | Aircraft | 8000 | 7 | 16000 | 7 | 45 | 95 | 0 | 0 | 0 | 3083 | 3085 |
| 3085 | USA | S-3B Viking | 1987 | Naval Aircraft | ASW | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 108 | 0 | 0 | 0 | 3084 | 3086 |
| 3086 | USA | P-3C Orion | 1969 | Naval Aircraft | ASW/Patrol | Aircraft | 7500 | 6 | 15000 | 6 | 42 | 88 | 0 | 0 | 0 | 3083 | 3087 |
| 3087 | USA | P-3C Update III | 1984 | Naval Aircraft | ASW/Patrol | Aircraft | 8500 | 7 | 17000 | 7 | 45 | 98 | 0 | 0 | 0 | 3086 | 3088 |
| 3088 | USA | P-8A Poseidon | 2013 | Naval Aircraft | ASW/Patrol | Aircraft | 15000 | 12 | 30000 | 12 | 55 | 165 | 0 | 0 | 0 | 3087 | 3089 |
| 3089 | USA | P-8A Block II | 2020 | Naval Aircraft | ASW/Patrol | Aircraft | 16000 | 13 | 32000 | 13 | 58 | 175 | 0 | 0 | 0 | 3088 |  |
| 3090 | USA | E-1 Tracer | 1958 | Naval Aircraft | AEW | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3091 |
| 3091 | USA | E-2A Hawkeye | 1964 | Naval Aircraft | AEW | Aircraft | 6000 | 5 | 12000 | 5 | 35 | 75 | 0 | 0 | 0 | 3090 | 3092 |
| 3092 | USA | E-2C Hawkeye | 1973 | Naval Aircraft | AEW | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 98 | 0 | 0 | 0 | 3091 | 3093 |
| 3093 | USA | E-2C Group II | 2000 | Naval Aircraft | AEW | Aircraft | 10000 | 8 | 20000 | 8 | 48 | 125 | 0 | 0 | 0 | 3092 | 3094 |
| 3094 | USA | E-2D Advanced Hawkeye | 2014 | Naval Aircraft | AEW | Aircraft | 13000 | 11 | 26000 | 11 | 55 | 155 | 0 | 0 | 0 | 3093 |  |
| 3095 | USA | EA-6A Intruder | 1965 | Naval Aircraft | EW | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 68 | 0 | 0 | 0 | 3073 | 3096 |
| 3096 | USA | EA-6B Prowler | 1971 | Naval Aircraft | EW | Aircraft | 7500 | 6 | 15000 | 6 | 40 | 88 | 0 | 0 | 0 | 3095 | 3097 |
| 3097 | USA | EA-6B ICAP II | 1989 | Naval Aircraft | EW | Aircraft | 9000 | 7 | 18000 | 7 | 45 | 108 | 0 | 0 | 0 | 3096 | 3098 |
| 3098 | USA | EA-18G Growler | 2009 | Naval Aircraft | EW | Aircraft | 13000 | 11 | 26000 | 11 | 52 | 145 | 0 | 0 | 0 | 3097,3043 |  |
| 3100 | USA | RF-8G Crusader | 1965 | Naval Aircraft | Recon | Aircraft | 4500 | 4 | 9000 | 4 | 28 | 58 | 0 | 0 | 0 | 3015 | 3101 |
| 3101 | USA | RA-5C Vigilante | 1962 | Naval Aircraft | Recon | Aircraft | 8000 | 7 | 16000 | 7 | 48 | 98 | 0 | 0 | 0 | 3100 | 3102 |
| 3102 | USA | F-14 TARPS | 1981 | Naval Aircraft | Recon | Aircraft | 9000 | 7 | 18000 | 7 | 50 | 112 | 0 | 0 | 0 | 3101,3030 | 3103 |
| 3103 | USA | F/A-18 ATARS | 1996 | Naval Aircraft | Recon | Aircraft | 10000 | 8 | 20000 | 8 | 52 | 128 | 0 | 0 | 0 | 3102,3041 |  |
| 3110 | USA | SH-3 Sea King | 1961 | Naval Aircraft | ASW Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3111 |
| 3111 | USA | SH-3H Sea King | 1974 | Naval Aircraft | ASW Helo | Aircraft | 4000 | 3 | 8000 | 3 | 22 | 58 | 0 | 0 | 0 | 3110 | 3112 |
| 3112 | USA | SH-60B Seahawk | 1984 | Naval Aircraft | ASW Helo | Aircraft | 6000 | 5 | 12000 | 5 | 32 | 78 | 0 | 0 | 0 | 3111 | 3113 |
| 3113 | USA | SH-60F Seahawk | 1989 | Naval Aircraft | ASW Helo | Aircraft | 6500 | 5 | 13000 | 5 | 35 | 85 | 0 | 0 | 0 | 3112 | 3114 |
| 3114 | USA | MH-60R Seahawk | 2006 | Naval Aircraft | Multi-Role Helo | Aircraft | 9000 | 7 | 18000 | 7 | 42 | 118 | 0 | 0 | 0 | 3113 | 3115 |
| 3115 | USA | MH-60R Block II | 2020 | Naval Aircraft | Multi-Role Helo | Aircraft | 10000 | 8 | 20000 | 8 | 45 | 130 | 0 | 0 | 0 | 3114 |  |
| 3116 | USA | MH-60S Knighthawk | 2002 | Naval Aircraft | Utility Helo | Aircraft | 5500 | 5 | 11000 | 5 | 28 | 72 | 0 | 0 | 0 | 3113 | 3114 |
| 3120 | USA | MQ-25 Stingray | 2021 | Naval Aircraft | UAV Tanker | Aircraft | 12000 | 10 | 24000 | 10 | 45 | 145 | 0 | 0 | 0 | 3044 |  |
| 3200 | British | Sea Hurricane | 1941 | Naval Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3201 |
| 3201 | British | Seafire Mk III | 1943 | Naval Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 25 | 0 | 0 | 0 | 3200 | 3202 |
| 3202 | British | Seafire Mk XV | 1945 | Naval Aircraft | Fighter | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 32 | 0 | 0 | 0 | 3201 | 3210 |
| 3210 | British | Sea Fury | 1947 | Naval Aircraft | Fighter | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 38 | 0 | 0 | 0 | 3202 | 3211 |
| 3211 | British | Attacker | 1951 | Naval Aircraft | Jet Fighter | Aircraft | 4500 | 4 | 9000 | 4 | 28 | 52 | 0 | 0 | 0 | 3210 | 3212 |
| 3212 | British | Sea Hawk | 1953 | Naval Aircraft | Jet Fighter | Aircraft | 5000 | 4 | 10000 | 4 | 30 | 58 | 0 | 0 | 0 | 3211 | 3213 |
| 3213 | British | Sea Venom | 1954 | Naval Aircraft | Jet Fighter | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 65 | 0 | 0 | 0 | 3212 | 3214 |
| 3214 | British | Scimitar | 1958 | Naval Aircraft | Jet Fighter | Aircraft | 6500 | 5 | 13000 | 5 | 38 | 75 | 0 | 0 | 0 | 3213 | 3215 |
| 3215 | British | Sea Vixen | 1959 | Naval Aircraft | Jet Fighter | Aircraft | 7000 | 6 | 14000 | 6 | 40 | 82 | 0 | 0 | 0 | 3214 | 3220 |
| 3220 | British | Phantom FG.1 | 1968 | Naval Aircraft | Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 108 | 0 | 0 | 0 | 3215 | 3221 |
| 3221 | British | Phantom FGR.2 | 1969 | Naval Aircraft | Multi-Role | Aircraft | 9500 | 8 | 19000 | 8 | 50 | 115 | 0 | 0 | 0 | 3220 | 3230 |
| 3230 | British | Sea Harrier FRS.1 | 1978 | Naval Aircraft | V/STOL | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 98 | 0 | 0 | 0 | 3221 | 3231 |
| 3231 | British | Sea Harrier FA.2 | 1993 | Naval Aircraft | V/STOL | Aircraft | 10000 | 8 | 20000 | 8 | 48 | 128 | 0 | 0 | 0 | 3230 | 3240 |
| 3240 | British | F-35B Lightning II | 2018 | Naval Aircraft | V/STOL Stealth | Aircraft | 18000 | 14 | 36000 | 14 | 65 | 205 | 0 | 0 | 0 | 3231 | 3241 |
| 3241 | British | F-35B Block 4 | 2025 | Naval Aircraft | V/STOL Stealth | Aircraft | 20000 | 15 | 40000 | 15 | 68 | 220 | 0 | 0 | 0 | 3240 |  |
| 3250 | British | Swordfish | 1940 | Naval Aircraft | Torpedo Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3251 |
| 3251 | British | Barracuda | 1943 | Naval Aircraft | Torpedo Bomber | Aircraft | 2200 | 2 | 4400 | 2 | 14 | 22 | 0 | 0 | 0 | 3250 | 3252 |
| 3252 | British | Firefly | 1944 | Naval Aircraft | Strike | Aircraft | 2800 | 3 | 5600 | 3 | 18 | 28 | 0 | 0 | 0 | 3251 | 3253 |
| 3253 | British | Wyvern | 1953 | Naval Aircraft | Strike | Aircraft | 4000 | 3 | 8000 | 3 | 25 | 45 | 0 | 0 | 0 | 3252 | 3254 |
| 3254 | British | Buccaneer S.1 | 1962 | Naval Aircraft | Strike | Aircraft | 6000 | 5 | 12000 | 5 | 35 | 72 | 0 | 0 | 0 | 3253 | 3255 |
| 3255 | British | Buccaneer S.2 | 1965 | Naval Aircraft | Strike | Aircraft | 6500 | 5 | 13000 | 5 | 38 | 78 | 0 | 0 | 0 | 3254 | 3230 |
| 3260 | British | Gannet AS.1 | 1955 | Naval Aircraft | ASW | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3261 |
| 3261 | British | Gannet AS.4 | 1959 | Naval Aircraft | ASW | Aircraft | 4500 | 4 | 9000 | 4 | 28 | 58 | 0 | 0 | 0 | 3260 | 3262 |
| 3262 | British | Nimrod MR.1 | 1969 | Naval Aircraft | ASW/Patrol | Aircraft | 7000 | 6 | 14000 | 6 | 42 | 88 | 0 | 0 | 0 | 3261 | 3263 |
| 3263 | British | Nimrod MR.2 | 1979 | Naval Aircraft | ASW/Patrol | Aircraft | 8000 | 7 | 16000 | 7 | 45 | 98 | 0 | 0 | 0 | 3262 | 3264 |
| 3264 | British | Nimrod MRA.4 | 2010 | Naval Aircraft | ASW/Patrol | Aircraft | 12000 | 10 | 24000 | 10 | 52 | 145 | 0 | 0 | 0 | 3263 | 3265 |
| 3265 | British | P-8A Poseidon (RAF) | 2020 | Naval Aircraft | ASW/Patrol | Aircraft | 15000 | 12 | 30000 | 12 | 58 | 175 | 0 | 0 | 0 | 3264 |  |
| 3270 | British | Gannet AEW.3 | 1960 | Naval Aircraft | AEW | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3271 |
| 3271 | British | Sea King AEW.2 | 1982 | Naval Aircraft | AEW Helo | Aircraft | 5000 | 4 | 10000 | 4 | 30 | 68 | 0 | 0 | 0 | 3270 | 3272 |
| 3272 | British | Merlin HM.2 | 2014 | Naval Aircraft | ASW Helo | Aircraft | 9000 | 7 | 18000 | 7 | 45 | 125 | 0 | 0 | 0 | 3271 |  |
| 3280 | British | Wasp HAS.1 | 1963 | Naval Aircraft | ASW Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3281 |
| 3281 | British | Lynx HAS.2 | 1976 | Naval Aircraft | ASW Helo | Aircraft | 4000 | 3 | 8000 | 3 | 22 | 52 | 0 | 0 | 0 | 3280 | 3282 |
| 3282 | British | Lynx HMA.8 | 1995 | Naval Aircraft | ASW Helo | Aircraft | 5500 | 5 | 11000 | 5 | 28 | 72 | 0 | 0 | 0 | 3281 | 3283 |
| 3283 | British | Wildcat HMA.2 | 2015 | Naval Aircraft | Multi-Role Helo | Aircraft | 7500 | 6 | 15000 | 6 | 35 | 98 | 0 | 0 | 0 | 3282 |  |
| 3300 | German | Tornado IDS (Naval) | 1979 | Naval Aircraft | Strike | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3301 |
| 3301 | German | Tornado IDS Mid-Life | 1995 | Naval Aircraft | Strike | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 105 | 0 | 0 | 0 | 3300 | 3302 |
| 3302 | German | Eurofighter Typhoon (Naval) | 2004 | Naval Aircraft | Multi-Role | Aircraft | 12000 | 10 | 24000 | 10 | 52 | 145 | 0 | 0 | 0 | 3301 |  |
| 3310 | German | Breguet Atlantic | 1972 | Naval Aircraft | ASW/Patrol | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3311 |
| 3311 | German | Atlantic 1 Mod | 1981 | Naval Aircraft | ASW/Patrol | Aircraft | 6000 | 5 | 12000 | 5 | 35 | 78 | 0 | 0 | 0 | 3310 | 3312 |
| 3312 | German | P-3C Orion (German) | 1995 | Naval Aircraft | ASW/Patrol | Aircraft | 9000 | 7 | 18000 | 7 | 45 | 115 | 0 | 0 | 0 | 3311 | 3313 |
| 3313 | German | P-8A Poseidon (German) | 2022 | Naval Aircraft | ASW/Patrol | Aircraft | 15000 | 12 | 30000 | 12 | 58 | 175 | 0 | 0 | 0 | 3312 |  |
| 3320 | German | Sea King Mk 41 | 1972 | Naval Aircraft | ASW Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3321 |
| 3321 | German | Sea King Mk 41 Mod | 1985 | Naval Aircraft | ASW Helo | Aircraft | 4500 | 4 | 9000 | 4 | 25 | 62 | 0 | 0 | 0 | 3320 | 3322 |
| 3322 | German | Sea Lynx Mk 88 | 1981 | Naval Aircraft | ASW Helo | Aircraft | 4000 | 3 | 8000 | 3 | 22 | 58 | 0 | 0 | 0 | 3321 | 3323 |
| 3323 | German | Super Lynx Mk 88A | 2001 | Naval Aircraft | ASW Helo | Aircraft | 5500 | 5 | 11000 | 5 | 28 | 78 | 0 | 0 | 0 | 3322 | 3324 |
| 3324 | German | NH90 Sea Lion | 2019 | Naval Aircraft | Multi-Role Helo | Aircraft | 8000 | 7 | 16000 | 7 | 38 | 118 | 0 | 0 | 0 | 3323 |  |
| 3330 | German | MH-60R Seahawk (German) | 2025 | Naval Aircraft | ASW Helo | Aircraft | 10000 | 8 | 20000 | 8 | 45 | 135 | 0 | 0 | 0 | 3324 |  |
| 3340 | German | Do 24 (Reactivated) | 1975 | Naval Aircraft | Maritime Patrol | Aircraft | 2000 | 2 | 4000 | 2 | 18 | 28 | 0 | 0 | 0 | 3310 |  |
| 3400 | Japanese | A5M Claude | 1940 | Naval Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3401 |
| 3401 | Japanese | A6M2 Zero | 1940 | Naval Aircraft | Fighter | Aircraft | 2000 | 2 | 4000 | 2 | 12 | 18 | 0 | 0 | 0 | 3400 | 3402 |
| 3402 | Japanese | A6M3 Zero | 1942 | Naval Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 22 | 0 | 0 | 0 | 3401 | 3403 |
| 3403 | Japanese | A6M5 Zero | 1943 | Naval Aircraft | Fighter | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 28 | 0 | 0 | 0 | 3402 | 3404 |
| 3404 | Japanese | J2M Raiden (Jack) | 1943 | Naval Aircraft | Interceptor | Aircraft | 3500 | 3 | 7000 | 3 | 20 | 32 | 0 | 0 | 0 | 3403 | 3405 |
| 3405 | Japanese | N1K2-J Shiden-Kai (George) | 1944 | Naval Aircraft | Fighter | Aircraft | 4000 | 3 | 8000 | 3 | 22 | 38 | 0 | 0 | 0 | 3404 | 3410 |
| 3410 | Japanese | P-1 | 2013 | Naval Aircraft | Maritime Patrol | Aircraft | 12000 | 10 | 24000 | 10 | 52 | 145 | 0 | 0 | 0 | 3405 | 3411 |
| 3411 | Japanese | P-1 Mod 2 | 2022 | Naval Aircraft | Maritime Patrol | Aircraft | 13500 | 11 | 27000 | 11 | 55 | 158 | 0 | 0 | 0 | 3410 |  |
| 3412 | Japanese | P-3C Orion (JMSDF) | 1982 | Naval Aircraft | ASW/Patrol | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3413 |
| 3413 | Japanese | P-3C Update III (JMSDF) | 1995 | Naval Aircraft | ASW/Patrol | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 105 | 0 | 0 | 0 | 3412 | 3410 |
| 3420 | Japanese | D3A Val | 1940 | Naval Aircraft | Dive Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3421 |
| 3421 | Japanese | D4Y Suisei (Judy) | 1942 | Naval Aircraft | Dive Bomber | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 22 | 0 | 0 | 0 | 3420 | 3422 |
| 3422 | Japanese | B7A Ryusei (Grace) | 1944 | Naval Aircraft | Strike | Aircraft | 3500 | 3 | 7000 | 3 | 20 | 32 | 0 | 0 | 0 | 3421 | 3430 |
| 3430 | Japanese | F-35B Lightning II (JMSDF) | 2024 | Naval Aircraft | V/STOL Stealth | Aircraft | 20000 | 15 | 40000 | 15 | 68 | 220 | 0 | 0 | 0 | 3422 |  |
| 3440 | Japanese | B5N Kate | 1940 | Naval Aircraft | Torpedo Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3441 |
| 3441 | Japanese | B6N Tenzan (Jill) | 1943 | Naval Aircraft | Torpedo Bomber | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 22 | 0 | 0 | 0 | 3440 | 3442 |
| 3442 | Japanese | P2V Neptune (JMSDF) | 1958 | Naval Aircraft | ASW/Patrol | Aircraft | 4000 | 3 | 8000 | 3 | 25 | 48 | 0 | 0 | 0 | 3441 | 3443 |
| 3443 | Japanese | PS-1 | 1971 | Naval Aircraft | ASW Flying Boat | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 68 | 0 | 0 | 0 | 3442 | 3444 |
| 3444 | Japanese | US-2 | 2007 | Naval Aircraft | SAR Flying Boat | Aircraft | 7000 | 6 | 14000 | 6 | 38 | 92 | 0 | 0 | 0 | 3443 |  |
| 3450 | Japanese | HSS-2 Sea King (JMSDF) | 1965 | Naval Aircraft | ASW Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 3451 |
| 3451 | Japanese | SH-3A Sea King (JMSDF) | 1974 | Naval Aircraft | ASW Helo | Aircraft | 4000 | 3 | 8000 | 3 | 22 | 52 | 0 | 0 | 0 | 3450 | 3452 |
| 3452 | Japanese | SH-60J Seahawk | 1991 | Naval Aircraft | ASW Helo | Aircraft | 6000 | 5 | 12000 | 5 | 32 | 78 | 0 | 0 | 0 | 3451 | 3453 |
| 3453 | Japanese | SH-60K Seahawk | 2006 | Naval Aircraft | ASW Helo | Aircraft | 8000 | 7 | 16000 | 7 | 38 | 108 | 0 | 0 | 0 | 3452 | 3454 |
| 3454 | Japanese | SH-60K(Kai) | 2015 | Naval Aircraft | ASW Helo | Aircraft | 9000 | 7 | 18000 | 7 | 42 | 122 | 0 | 0 | 0 | 3453 |  |
| 3460 | Japanese | MCH-101 | 2008 | Naval Aircraft | Multi-Role Helo | Aircraft | 7500 | 6 | 15000 | 6 | 38 | 98 | 0 | 0 | 0 | 3453 | 3461 |
| 3461 | Japanese | MCH-101 Mod 2 | 2018 | Naval Aircraft | Multi-Role Helo | Aircraft | 8500 | 7 | 17000 | 7 | 42 | 112 | 0 | 0 | 0 | 3460 |  |
| 3470 | Japanese | OH-6D | 1978 | Naval Aircraft | Observation Helo | Aircraft | 1500 | 2 | 3000 | 2 | 10 | 22 | 0 | 0 | 0 | 3451 | 3471 |
| 3471 | Japanese | OH-1 Ninja | 1999 | Naval Aircraft | Observation Helo | Aircraft | 3000 | 3 | 6000 | 3 | 15 | 42 | 0 | 0 | 0 | 3470 |  |
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
| 41 | 5001 | 5000 | Langley-class | 1 | NULL | Lexington requires Langley (first carrier experience) |
| 42 | 5002 | 5001 | Lexington-class | 1 | NULL | Ranger requires Lexington |
| 43 | 5003 | 5002 | Ranger-class | 1 | NULL | Yorktown requires Ranger (treaty era lessons) |
| 44 | 5004 | 5003 | Yorktown-class | 1 | NULL | Essex requires Yorktown (pre-war experience) |
| 45 | 5005 | 5004 | Essex-class | 1 | NULL | Essex 1947 Refit requires base Essex |
| 46 | 5006 | 5004 | Essex-class | 1 | NULL | Essex SCB-27A requires base Essex |
| 47 | 5007 | 5004 | Essex-class | 1 | NULL | Midway requires Essex (WWII mass production experience) |
| 48 | 5008 | 5007 | Midway-class | 1 | NULL | Forrestal requires Midway (armored carrier lessons) |
| 49 | 5009 | 5008 | Forrestal-class | 1 | NULL | Kitty Hawk requires Forrestal (supercarrier evolution) |
| 50 | 5010 | 5009 | Kitty Hawk-class | 1 | NULL | Enterprise requires Kitty Hawk (nuclear transition) |
| 51 | 5011 | 5010 | Enterprise-class | 1 | NULL | Nimitz requires Enterprise (nuclear carrier maturation) |
| 100 | 6002 | 6001 | Omaha-class | 1 | NULL | Pensacola requires Omaha (heavy cruiser path) |
| 101 | 6003 | 6001 | Omaha-class | 1 | NULL | Northampton requires Omaha (alternative heavy) |
| 102 | 6004 | 6001 | Omaha-class | 1 | NULL | Brooklyn requires Omaha (light cruiser path) |
| 103 | 6005 | 6002 | Pensacola-class | 1 | 1 | Portland requires Pensacola OR Northampton |
| 104 | 6005 | 6003 | Northampton-class | 1 | 1 | Portland requires Pensacola OR Northampton |
| 105 | 6006 | 6004 | Brooklyn-class | 1 | NULL | Atlanta requires Brooklyn (AA needs CL experience) |
| 106 | 6007 | 6004 | Brooklyn-class | 1 | NULL | St. Louis requires Brooklyn |
| 107 | 6008 | 6005 | Portland-class | 1 | NULL | New Orleans requires Portland |
| 108 | 6009 | 6008 | New Orleans-class | 1 | NULL | Wichita requires New Orleans |
| 109 | 6010 | 6007 | St. Louis-class | 1 | 1 | Cleveland requires St. Louis OR Brooklyn |
| 110 | 6010 | 6004 | Brooklyn-class | 1 | 1 | Cleveland requires St. Louis OR Brooklyn |
| 111 | 6011 | 6006 | Atlanta-class | 1 | NULL | Oakland requires Atlanta |
| 112 | 6012 | 6009 | Wichita-class | 1 | NULL | Baltimore requires Wichita |
| 113 | 6013 | 6012 | Baltimore-class | 1 | NULL | Oregon City requires Baltimore |
| 114 | 6014 | 6010 | Cleveland-class | 1 | NULL | Fargo requires Cleveland |
| 115 | 6015 | 6011 | Oakland-class | 1 | NULL | Juneau requires Oakland |
| 116 | 6016 | 6012 | Baltimore-class | 1 | 1 | Des Moines requires Baltimore OR Oregon City |
| 117 | 6016 | 6013 | Oregon City-class | 1 | 1 | Des Moines requires Baltimore OR Oregon City |
| 118 | 6017 | 6010 | Cleveland-class | 1 | 1 | Worcester requires Cleveland OR Fargo |
| 119 | 6017 | 6014 | Fargo-class | 1 | 1 | Worcester requires Cleveland OR Fargo |
| 120 | 6018 | 6012 | Baltimore-class | 1 | NULL | Boston conversion requires Baltimore |
| 121 | 6019 | 6010 | Cleveland-class | 1 | NULL | Galveston conversion requires Cleveland |
| 122 | 6020 | 6010 | Cleveland-class | 1 | NULL | Providence conversion requires Cleveland |
| 123 | 6021 | 6010 | Cleveland-class | 1 | NULL | Norfolk requires Cleveland (destroyer leader) |
| 124 | 6022 | 6012 | Baltimore-class | 1 | NULL | Albany conversion requires Baltimore |
| 125 | 6023 | 6016 | Des Moines-class | 1 | NULL | Long Beach requires Des Moines (ultimate gun CA) |
| 126 | 6024 | 6016 | Des Moines-class | 1 | 1 | Leahy requires Des Moines OR Worcester |
| 127 | 6024 | 6017 | Worcester-class | 1 | 1 | Leahy requires Des Moines OR Worcester |
| 128 | 6025 | 6023 | Long Beach CGN-9 | 1 | NULL | Bainbridge requires Long Beach AND Leahy |
| 129 | 6025 | 6024 | Leahy-class | 1 | NULL | Bainbridge requires Long Beach AND Leahy |
| 130 | 6026 | 6024 | Leahy-class | 1 | NULL | Belknap requires Leahy |
| 131 | 6027 | 6025 | Bainbridge CGN-25 | 1 | NULL | Truxtun requires Bainbridge AND Belknap |
| 132 | 6027 | 6026 | Belknap-class | 1 | NULL | Truxtun requires Bainbridge AND Belknap |
| 133 | 6028 | 6012 | Baltimore-class | 1 | NULL | Chicago conversion requires Baltimore |
| 134 | 6029 | 6023 | Long Beach CGN-9 | 1 | 1 | California requires Long Beach OR Truxtun |
| 135 | 6029 | 6027 | Truxtun CGN-35 | 1 | 1 | California requires Long Beach OR Truxtun |
| 136 | 6030 | 6029 | California-class | 1 | NULL | Virginia requires California |
| 137 | 6031 | 6024 | Leahy-class | 1 | NULL | Leahy NTU requires base Leahy |
| 138 | 6032 | 6026 | Belknap-class | 1 | NULL | Belknap NTU requires base Belknap |
| 139 | 6033 | 6026 | Belknap-class | 1 | NULL | Ticonderoga Early requires Belknap |
| 140 | 6034 | 6033 | Ticonderoga-class (Early) CG-47/48 | 1 | NULL | Ticonderoga Baseline 1 requires Early |
| 141 | 6035 | 6034 | Ticonderoga-class (Baseline 1) CG-49-51 | 1 | NULL | Ticonderoga Baseline 2 requires Baseline 1 |
| 142 | 6036 | 6030 | Virginia-class | 1 | NULL | Virginia Modernized requires base Virginia |
| 143 | 6037 | 6030 | Virginia-class | 1 | NULL | Strike Cruiser requires Virginia (paper ship) |
| 144 | 6038 | 6035 | Ticonderoga-class (Baseline 2) CG-52-58 | 1 | NULL | Ticonderoga Baseline 3 requires Baseline 2 |
| 145 | 6039 | 6038 | Ticonderoga-class (Baseline 3) CG-59-64 | 1 | NULL | Ticonderoga Baseline 4 requires Baseline 3 |
| 146 | 6040 | 6039 | Ticonderoga-class (Baseline 4) CG-65-73 | 1 | NULL | CG(X) requires Baseline 4 (cancelled future) |
| 147 | 7002 | 7001 | Smith-class | 1 | 1 | Paulding requires Bainbridge OR Smith |
| 148 | 7002 | 7000 | Bainbridge-class | 1 | 1 | Paulding requires Bainbridge OR Smith |
| 149 | 7003 | 7002 | Paulding-class | 1 | NULL | Cassin requires Paulding |
| 150 | 7004 | 7003 | Cassin-class | 1 | NULL | Sampson requires Cassin |
| 151 | 7005 | 7004 | Sampson-class | 1 | NULL | Caldwell requires Sampson (first flush-deck) |
| 152 | 7006 | 7005 | Caldwell-class | 1 | NULL | Wickes requires Caldwell |
| 153 | 7007 | 7006 | Wickes-class | 1 | NULL | Clemson requires Wickes |
| 154 | 7008 | 7006 | Wickes-class | 1 | 1 | Wickes APD requires Wickes OR Clemson |
| 155 | 7008 | 7007 | Clemson-class | 1 | 1 | Wickes APD requires Wickes OR Clemson |
| 156 | 7009 | 7007 | Clemson-class | 1 | NULL | Farragut requires Clemson (interwar gap) |
| 157 | 7010 | 7009 | Farragut-class | 1 | NULL | Porter requires Farragut (leader variant) |
| 158 | 7011 | 7009 | Farragut-class | 1 | NULL | Mahan requires Farragut |
| 159 | 7012 | 7011 | Mahan-class | 1 | NULL | Gridley requires Mahan (torpedo focus) |
| 160 | 7013 | 7011 | Mahan-class | 1 | 1 | Bagley requires Mahan OR Gridley |
| 161 | 7013 | 7012 | Gridley-class | 1 | 1 | Bagley requires Mahan OR Gridley |
| 162 | 7014 | 7013 | Bagley-class | 1 | 1 | Benham requires Bagley OR Porter |
| 163 | 7014 | 7010 | Porter-class | 1 | 1 | Benham requires Bagley OR Porter |
| 164 | 7015 | 7013 | Bagley-class | 1 | NULL | Sims requires Bagley |
| 165 | 7016 | 7014 | Benham-class | 1 | 1 | Benson requires Benham OR Sims |
| 166 | 7016 | 7015 | Sims-class | 1 | 1 | Benson requires Benham OR Sims |
| 167 | 7017 | 7016 | Benson-class | 1 | NULL | Gleaves requires Benson (variant) |
| 168 | 7018 | 7016 | Benson-class | 1 | NULL | Bristol requires Benson (subclass) |
| 169 | 7019 | 7017 | Gleaves-class | 1 | 1 | Fletcher requires Gleaves OR Bristol |
| 170 | 7019 | 7018 | Bristol-class | 1 | 1 | Fletcher requires Gleaves OR Bristol |
| 171 | 7020 | 7019 | Fletcher-class | 1 | NULL | Fletcher FRAM requires base Fletcher |
| 172 | 7021 | 7019 | Fletcher-class | 1 | NULL | Sumner requires Fletcher |
| 173 | 7022 | 7021 | Allen M. Sumner-class | 1 | NULL | Gearing requires Sumner |
| 174 | 7023 | 7022 | Gearing-class | 1 | NULL | Gearing FRAM requires base Gearing |
| 175 | 7024 | 7022 | Gearing-class | 1 | NULL | Gearing DDR requires base Gearing |
| 176 | 7025 | 7022 | Gearing-class | 1 | NULL | Forrest Sherman requires Gearing (post-war) |
| 177 | 7026 | 7025 | Forrest Sherman-class | 1 | NULL | Forrest Sherman DDG requires base |
| 178 | 7027 | 7010 | Porter-class | 1 | NULL | Mitscher requires Porter (large leader) |
| 179 | 7028 | 7025 | Forrest Sherman-class | 1 | 1 | Farragut DDG requires Forrest Sherman OR Mitscher |
| 180 | 7028 | 7027 | Mitscher-class | 1 | 1 | Farragut DDG requires Forrest Sherman OR Mitscher |
| 181 | 7029 | 7028 | Farragut/Coontz-class | 1 | NULL | Charles F. Adams requires Farragut DDG |
| 182 | 7030 | 7029 | Charles F. Adams-class | 1 | NULL | Adams NTU requires base Adams |
| 183 | 7031 | 7029 | Charles F. Adams-class | 1 | NULL | Spruance requires Adams (gas turbine leap) |
| 184 | 7032 | 7031 | Spruance-class | 1 | NULL | Spruance VLS requires base Spruance |
| 185 | 7033 | 7031 | Spruance-class | 1 | NULL | Kidd requires Spruance (modified) |
| 186 | 7034 | 7033 | Kidd-class | 1 | NULL | Arleigh Burke F1 requires Kidd (Aegis) |
| 187 | 7035 | 7034 | Arleigh Burke-class (Flight I) DDG-51-71 | 1 | NULL | Burke F2 requires F1 |
| 188 | 7036 | 7035 | Arleigh Burke-class (Flight II) DDG-72-78 | 1 | NULL | Burke F2A requires F2 |
| 189 | 7037 | 7036 | Arleigh Burke-class (Flight IIA) DDG-79-112 | 1 | NULL | Burke F3 requires F2A |
| 190 | 7038 | 7036 | Arleigh Burke-class (Flight IIA) DDG-79-112 | 1 | NULL | Zumwalt requires Burke F2A (stealth) |
| 191 | 7039 | 7037 | Arleigh Burke-class (Flight III) DDG-113+ | 1 | NULL | Burke F4 requires F3 (future) |
| 192 | 7040 | 7037 | Arleigh Burke-class (Flight III) DDG-113+ | 1 | NULL | DDG(X) requires F3 (paper ship) |
| 193 | 8002 | 8001 | A-class | 1 | 1 | C-class requires Holland OR A-class |
| 194 | 8002 | 8000 | Holland-class | 1 | 1 | C-class requires Holland OR A-class |
| 195 | 8003 | 8002 | C-class | 1 | NULL | F-class requires C-class |
| 196 | 8004 | 8003 | F-class | 1 | NULL | H-class requires F-class |
| 197 | 8005 | 8004 | H-class | 1 | NULL | L-class requires H-class (first fleet) |
| 198 | 8006 | 8005 | L-class | 1 | NULL | O-class requires L-class |
| 199 | 8007 | 8006 | O-class | 1 | NULL | R-class requires O-class |
| 200 | 8008 | 8007 | R-class | 1 | NULL | S-class requires R-class |
| 201 | 8009 | 8007 | R-class | 1 | NULL | V-class requires R-class (experimental cruiser) |
| 202 | 8010 | 8008 | S-class | 1 | NULL | Porpoise requires S-class (pre-war) |
| 203 | 8011 | 8010 | Porpoise-class | 1 | NULL | Salmon requires Porpoise |
| 204 | 8012 | 8011 | Salmon-class | 1 | NULL | Sargo requires Salmon |
| 205 | 8013 | 8012 | Sargo-class | 1 | NULL | Tambor requires Sargo (WWII begins) |
| 206 | 8014 | 8013 | Tambor-class | 1 | NULL | Gar requires Tambor |
| 207 | 8015 | 8004 | H-class | 1 | NULL | Mackerel requires H-class (training) |
| 208 | 8016 | 8015 | Mackerel-class | 1 | NULL | Barracuda requires Mackerel (SST) |
| 209 | 8017 | 8014 | Gar-class | 1 | 1 | Gato requires Gar OR Tambor |
| 210 | 8017 | 8013 | Tambor-class | 1 | 1 | Gato requires Gar OR Tambor |
| 211 | 8018 | 8017 | Gato-class | 1 | NULL | Balao requires Gato |
| 212 | 8019 | 8018 | Balao-class | 1 | NULL | Tench requires Balao |
| 213 | 8020 | 8018 | Balao-class | 1 | NULL | Balao GUPPY requires base Balao |
| 214 | 8021 | 8019 | Tench-class | 1 | NULL | Tench GUPPY requires base Tench |
| 215 | 8022 | 8019 | Tench-class | 1 | NULL | Nautilus requires Tench (nuclear leap) |
| 216 | 8023 | 8022 | Nautilus SSN-571 | 1 | NULL | Seawolf SSN-575 requires Nautilus (experimental) |
| 217 | 8024 | 8022 | Nautilus SSN-571 | 1 | NULL | Skate requires Nautilus (production) |
| 218 | 8025 | 8024 | Skate-class | 1 | NULL | George Washington requires Skate (ballistic) |
| 219 | 8026 | 8025 | George Washington-class | 1 | NULL | Ethan Allen requires George Washington |
| 220 | 8027 | 8024 | Skate-class | 1 | NULL | Skipjack requires Skate (teardrop) |
| 221 | 8028 | 8027 | Skipjack-class | 1 | NULL | Thresher/Permit requires Skipjack |
| 222 | 8029 | 8028 | Thresher/Permit-class | 1 | NULL | Sturgeon requires Thresher/Permit |
| 223 | 8030 | 8026 | Ethan Allen-class | 1 | NULL | Lafayette requires Ethan Allen |
| 224 | 8031 | 8030 | Lafayette-class | 1 | NULL | Benjamin Franklin requires Lafayette |
| 225 | 8032 | 8029 | Sturgeon-class | 1 | NULL | Los Angeles Early requires Sturgeon |
| 226 | 8033 | 8032 | Los Angeles-class (Early) SSN-688-699 | 1 | NULL | Los Angeles 688i requires Early |
| 227 | 8034 | 8031 | Benjamin Franklin-class | 1 | NULL | Ohio SSBN requires Benjamin Franklin |
| 228 | 8035 | 8034 | Ohio-class | 1 | NULL | Ohio SSGN requires base Ohio |
| 229 | 8036 | 8033 | Los Angeles-class (Improved 688i) SSN-700-773 | 1 | NULL | Seawolf requires LA 688i |
| 230 | 8037 | 8036 | Seawolf-class | 1 | NULL | Virginia requires Seawolf |
| 231 | 8038 | 8034 | Ohio-class | 1 | NULL | Columbia requires Ohio (future SSBN) |

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
| 41 | 5000 | 5001 | Lexington-class | 1 | 1 | Langley unlocks Lexington (battlecruiser conversion path) |
| 42 | 5001 | 5002 | Ranger-class | 1 | 1 | Lexington unlocks Ranger (first purpose-built CV) |
| 43 | 5002 | 5003 | Yorktown-class | 1 | 1 | Ranger unlocks Yorktown (perfect fleet carrier) |
| 44 | 5003 | 5004 | Essex-class | 1 | 1 | Yorktown unlocks Essex (WWII mass production) |
| 45 | 5004 | 5005 | Essex-class (1947 Refit) | 1 | 2 | Essex unlocks 1947 post-war refit variant |
| 46 | 5004 | 5006 | Essex-class (SCB-27A) | 1 | 2 | Essex unlocks SCB-27A jet modernization |
| 47 | 5004 | 5007 | Midway-class | 1 | 1 | Essex unlocks Midway (armored carrier path) |
| 48 | 5007 | 5008 | Forrestal-class | 1 | 1 | Midway unlocks Forrestal (first supercarrier) |
| 49 | 5008 | 5009 | Kitty Hawk-class | 1 | 1 | Forrestal unlocks Kitty Hawk (improved supercarrier) |
| 50 | 5009 | 5010 | Enterprise-class | 1 | 1 | Kitty Hawk unlocks Enterprise (nuclear revolution) |
| 51 | 5010 | 5011 | Nimitz-class | 1 | 1 | Enterprise unlocks Nimitz (ultimate carrier design) |
| 200 | 6001 | 6002 | Pensacola-class | 1 | 1 | Omaha unlocks Pensacola (heavy cruiser path) |
| 201 | 6001 | 6003 | Northampton-class | 1 | 1 | Omaha unlocks Northampton (alternative heavy) |
| 202 | 6001 | 6004 | Brooklyn-class | 1 | 1 | Omaha unlocks Brooklyn (light cruiser path) |
| 203 | 6002 | 6005 | Portland-class | 1 | 1 | Pensacola unlocks Portland |
| 204 | 6003 | 6005 | Portland-class | 1 | 1 | Northampton unlocks Portland |
| 205 | 6004 | 6006 | Atlanta-class | 1 | 2 | Brooklyn unlocks Atlanta (AA specialist) |
| 206 | 6004 | 6007 | St. Louis-class | 1 | 1 | Brooklyn unlocks St. Louis |
| 207 | 6004 | 6010 | Cleveland-class | 1 | 1 | Brooklyn unlocks Cleveland (alternative path) |
| 208 | 6005 | 6008 | New Orleans-class | 1 | 1 | Portland unlocks New Orleans |
| 209 | 6006 | 6011 | Oakland-class | 1 | 1 | Atlanta unlocks Oakland |
| 210 | 6007 | 6010 | Cleveland-class | 1 | 1 | St. Louis unlocks Cleveland |
| 211 | 6008 | 6009 | Wichita-class | 1 | 1 | New Orleans unlocks Wichita |
| 212 | 6009 | 6012 | Baltimore-class | 1 | 1 | Wichita unlocks Baltimore |
| 213 | 6010 | 6014 | Fargo-class | 1 | 1 | Cleveland unlocks Fargo |
| 214 | 6010 | 6017 | Worcester-class | 1 | 1 | Cleveland unlocks Worcester (alternative path) |
| 215 | 6010 | 6019 | Galveston-class | 1 | 2 | Cleveland unlocks Galveston conversion |
| 216 | 6010 | 6020 | Providence-class | 1 | 2 | Cleveland unlocks Providence conversion |
| 217 | 6010 | 6021 | Norfolk-class | 1 | 3 | Cleveland unlocks Norfolk (destroyer leader) |
| 218 | 6011 | 6015 | Juneau-class | 1 | 1 | Oakland unlocks Juneau |
| 219 | 6012 | 6013 | Oregon City-class | 1 | 1 | Baltimore unlocks Oregon City |
| 220 | 6012 | 6016 | Des Moines-class | 1 | 1 | Baltimore unlocks Des Moines (alternative path) |
| 221 | 6012 | 6018 | Boston-class | 1 | 2 | Baltimore unlocks Boston conversion |
| 222 | 6012 | 6022 | Albany-class | 1 | 2 | Baltimore unlocks Albany conversion |
| 223 | 6012 | 6028 | Chicago CAG-136 | 1 | 2 | Baltimore unlocks Chicago conversion |
| 224 | 6013 | 6016 | Des Moines-class | 1 | 1 | Oregon City unlocks Des Moines |
| 225 | 6014 | 6017 | Worcester-class | 1 | 1 | Fargo unlocks Worcester |
| 226 | 6016 | 6023 | Long Beach CGN-9 | 1 | 2 | Des Moines unlocks Long Beach (nuclear path) |
| 227 | 6016 | 6024 | Leahy-class | 1 | 1 | Des Moines unlocks Leahy (missile path) |
| 228 | 6017 | 6024 | Leahy-class | 1 | 1 | Worcester unlocks Leahy (alternative) |
| 229 | 6023 | 6025 | Bainbridge CGN-25 | 1 | 1 | Long Beach unlocks Bainbridge |
| 230 | 6023 | 6029 | California-class | 1 | 1 | Long Beach unlocks California (alternative) |
| 231 | 6024 | 6025 | Bainbridge CGN-25 | 1 | 2 | Leahy unlocks Bainbridge (nuclear variant) |
| 232 | 6024 | 6026 | Belknap-class | 1 | 1 | Leahy unlocks Belknap |
| 233 | 6024 | 6031 | Leahy-class (NTU) | 1 | 2 | Leahy unlocks its own NTU upgrade |
| 234 | 6025 | 6027 | Truxtun CGN-35 | 1 | 1 | Bainbridge unlocks Truxtun |
| 235 | 6026 | 6027 | Truxtun CGN-35 | 1 | 2 | Belknap unlocks Truxtun (nuclear variant) |
| 236 | 6026 | 6032 | Belknap-class (NTU) | 1 | 2 | Belknap unlocks its own NTU upgrade |
| 237 | 6026 | 6033 | Ticonderoga-class (Early) CG-47/48 | 1 | 1 | Belknap unlocks Ticonderoga (Aegis era) |
| 238 | 6027 | 6029 | California-class | 1 | 1 | Truxtun unlocks California |
| 239 | 6029 | 6030 | Virginia-class | 1 | 1 | California unlocks Virginia |
| 240 | 6030 | 6036 | Virginia-class CGN (Modernized) | 1 | 2 | Virginia unlocks its own modernization |
| 241 | 6030 | 6037 | Strike Cruiser CGN | 1 | 3 | Virginia unlocks Strike Cruiser (paper ship) |
| 242 | 6033 | 6034 | Ticonderoga-class (Baseline 1) CG-49-51 | 1 | 1 | Ticonderoga Early unlocks Baseline 1 |
| 243 | 6034 | 6035 | Ticonderoga-class (Baseline 2) CG-52-58 | 1 | 1 | Baseline 1 unlocks Baseline 2 |
| 244 | 6035 | 6038 | Ticonderoga-class (Baseline 3) CG-59-64 | 1 | 1 | Baseline 2 unlocks Baseline 3 |
| 245 | 6038 | 6039 | Ticonderoga-class (Baseline 4) CG-65-73 | 1 | 1 | Baseline 3 unlocks Baseline 4 |
| 246 | 6039 | 6040 | CG(X) Future Cruiser | 1 | 2 | Baseline 4 unlocks CG(X) (cancelled future) |
| 247 | 7000 | 7002 | Paulding-class | 1 | 1 | Bainbridge unlocks Paulding |
| 248 | 7001 | 7002 | Paulding-class | 1 | 1 | Smith unlocks Paulding |
| 249 | 7002 | 7003 | Cassin-class | 1 | 1 | Paulding unlocks Cassin |
| 250 | 7003 | 7004 | Sampson-class | 1 | 1 | Cassin unlocks Sampson |
| 251 | 7004 | 7005 | Caldwell-class | 1 | 1 | Sampson unlocks Caldwell (flush-deck) |
| 252 | 7005 | 7006 | Wickes-class | 1 | 1 | Caldwell unlocks Wickes |
| 253 | 7006 | 7007 | Clemson-class | 1 | 1 | Wickes unlocks Clemson |
| 254 | 7006 | 7008 | Wickes-class (APD) | 1 | 2 | Wickes unlocks APD conversion |
| 255 | 7007 | 7008 | Wickes-class (APD) | 1 | 2 | Clemson unlocks APD conversion |
| 256 | 7007 | 7009 | Farragut-class | 1 | 1 | Clemson unlocks Farragut (interwar) |
| 257 | 7009 | 7010 | Porter-class | 1 | 2 | Farragut unlocks Porter (leader) |
| 258 | 7009 | 7011 | Mahan-class | 1 | 1 | Farragut unlocks Mahan |
| 259 | 7010 | 7027 | Mitscher-class | 1 | 2 | Porter unlocks Mitscher (large leader) |
| 260 | 7011 | 7012 | Gridley-class | 1 | 2 | Mahan unlocks Gridley (torpedo) |
| 261 | 7011 | 7013 | Bagley-class | 1 | 1 | Mahan unlocks Bagley |
| 262 | 7012 | 7013 | Bagley-class | 1 | 1 | Gridley unlocks Bagley |
| 263 | 7013 | 7014 | Benham-class | 1 | 1 | Bagley unlocks Benham |
| 264 | 7013 | 7015 | Sims-class | 1 | 1 | Bagley unlocks Sims (alternative) |
| 265 | 7010 | 7014 | Benham-class | 1 | 1 | Porter unlocks Benham |
| 266 | 7014 | 7016 | Benson-class | 1 | 1 | Benham unlocks Benson |
| 267 | 7015 | 7016 | Benson-class | 1 | 1 | Sims unlocks Benson |
| 268 | 7016 | 7017 | Gleaves-class | 1 | 1 | Benson unlocks Gleaves |
| 269 | 7016 | 7018 | Bristol-class | 1 | 1 | Benson unlocks Bristol |
| 270 | 7017 | 7019 | Fletcher-class | 1 | 1 | Gleaves unlocks Fletcher |
| 271 | 7018 | 7019 | Fletcher-class | 1 | 1 | Bristol unlocks Fletcher |
| 272 | 7019 | 7020 | Fletcher-class (FRAM I) | 1 | 2 | Fletcher unlocks FRAM upgrade |
| 273 | 7019 | 7021 | Allen M. Sumner-class | 1 | 1 | Fletcher unlocks Sumner |
| 274 | 7021 | 7022 | Gearing-class | 1 | 1 | Sumner unlocks Gearing |
| 275 | 7022 | 7023 | Gearing-class (FRAM I) | 1 | 2 | Gearing unlocks FRAM upgrade |
| 276 | 7022 | 7024 | Gearing-class (DDR) | 1 | 2 | Gearing unlocks DDR conversion |
| 277 | 7022 | 7025 | Forrest Sherman-class | 1 | 1 | Gearing unlocks Forrest Sherman |
| 278 | 7025 | 7026 | Forrest Sherman-class DDG | 1 | 2 | Forrest Sherman unlocks DDG conversion |
| 279 | 7025 | 7028 | Farragut/Coontz-class | 1 | 1 | Forrest Sherman unlocks Farragut DDG |
| 280 | 7027 | 7028 | Farragut/Coontz-class | 1 | 1 | Mitscher unlocks Farragut DDG |
| 281 | 7028 | 7029 | Charles F. Adams-class | 1 | 1 | Farragut DDG unlocks Adams |
| 282 | 7029 | 7030 | Charles F. Adams-class (NTU) | 1 | 2 | Adams unlocks NTU upgrade |
| 283 | 7029 | 7031 | Spruance-class | 1 | 1 | Adams unlocks Spruance (gas turbine) |
| 284 | 7031 | 7032 | Spruance-class (VLS) | 1 | 2 | Spruance unlocks VLS upgrade |
| 285 | 7031 | 7033 | Kidd-class | 1 | 2 | Spruance unlocks Kidd (modified) |
| 286 | 7033 | 7034 | Arleigh Burke-class (Flight I) DDG-51-71 | 1 | 1 | Kidd unlocks Burke F1 (Aegis) |
| 287 | 7034 | 7035 | Arleigh Burke-class (Flight II) DDG-72-78 | 1 | 1 | Burke F1 unlocks F2 |
| 288 | 7035 | 7036 | Arleigh Burke-class (Flight IIA) DDG-79-112 | 1 | 1 | Burke F2 unlocks F2A |
| 289 | 7036 | 7037 | Arleigh Burke-class (Flight III) DDG-113+ | 1 | 1 | Burke F2A unlocks F3 |
| 290 | 7036 | 7038 | Zumwalt-class | 1 | 2 | Burke F2A unlocks Zumwalt (stealth) |
| 291 | 7037 | 7039 | Arleigh Burke-class (Flight IV) | 1 | 2 | Burke F3 unlocks F4 (future) |
| 292 | 7037 | 7040 | DDG(X) Future Destroyer | 1 | 3 | Burke F3 unlocks DDG(X) (paper) |
| 293 | 8000 | 8002 | C-class | 1 | 1 | Holland unlocks C-class |
| 294 | 8001 | 8002 | C-class | 1 | 1 | A-class unlocks C-class |
| 295 | 8002 | 8003 | F-class | 1 | 1 | C-class unlocks F-class |
| 296 | 8003 | 8004 | H-class | 1 | 1 | F-class unlocks H-class |
| 297 | 8004 | 8005 | L-class | 1 | 1 | H-class unlocks L-class (first fleet) |
| 298 | 8004 | 8015 | Mackerel-class | 1 | 3 | H-class unlocks Mackerel (training) |
| 299 | 8005 | 8006 | O-class | 1 | 1 | L-class unlocks O-class |
| 300 | 8006 | 8007 | R-class | 1 | 1 | O-class unlocks R-class |
| 301 | 8007 | 8008 | S-class | 1 | 1 | R-class unlocks S-class |
| 302 | 8007 | 8009 | V-class | 1 | 3 | R-class unlocks V-class (cruiser sub) |
| 303 | 8008 | 8010 | Porpoise-class | 1 | 1 | S-class unlocks Porpoise (pre-war) |
| 304 | 8010 | 8011 | Salmon-class | 1 | 1 | Porpoise unlocks Salmon |
| 305 | 8011 | 8012 | Sargo-class | 1 | 1 | Salmon unlocks Sargo |
| 306 | 8012 | 8013 | Tambor-class | 1 | 1 | Sargo unlocks Tambor (WWII begins) |
| 307 | 8013 | 8014 | Gar-class | 1 | 1 | Tambor unlocks Gar |
| 308 | 8013 | 8017 | Gato-class | 1 | 1 | Tambor unlocks Gato (alternative) |
| 309 | 8014 | 8017 | Gato-class | 1 | 1 | Gar unlocks Gato |
| 310 | 8015 | 8016 | Barracuda-class | 1 | 1 | Mackerel unlocks Barracuda (SST) |
| 311 | 8017 | 8018 | Balao-class | 1 | 1 | Gato unlocks Balao |
| 312 | 8018 | 8019 | Tench-class | 1 | 1 | Balao unlocks Tench |
| 313 | 8018 | 8020 | Balao-class (GUPPY) | 1 | 2 | Balao unlocks GUPPY upgrade |
| 314 | 8019 | 8021 | Tench-class (GUPPY IIA) | 1 | 2 | Tench unlocks GUPPY IIA upgrade |
| 315 | 8019 | 8022 | Nautilus SSN-571 | 1 | 1 | Tench unlocks Nautilus (nuclear leap) |
| 316 | 8022 | 8023 | Seawolf SSN-575 | 1 | 3 | Nautilus unlocks Seawolf (experimental) |
| 317 | 8022 | 8024 | Skate-class | 1 | 1 | Nautilus unlocks Skate (production) |
| 318 | 8024 | 8025 | George Washington-class | 1 | 2 | Skate unlocks George Washington (ballistic) |
| 319 | 8024 | 8027 | Skipjack-class | 1 | 1 | Skate unlocks Skipjack (teardrop) |
| 320 | 8025 | 8026 | Ethan Allen-class | 1 | 1 | George Washington unlocks Ethan Allen |
| 321 | 8026 | 8030 | Lafayette-class | 1 | 1 | Ethan Allen unlocks Lafayette |
| 322 | 8027 | 8028 | Thresher/Permit-class | 1 | 1 | Skipjack unlocks Thresher/Permit |
| 323 | 8028 | 8029 | Sturgeon-class | 1 | 1 | Thresher/Permit unlocks Sturgeon |
| 324 | 8029 | 8032 | Los Angeles-class (Early) SSN-688-699 | 1 | 1 | Sturgeon unlocks LA Early |
| 325 | 8030 | 8031 | Benjamin Franklin-class | 1 | 1 | Lafayette unlocks Benjamin Franklin |
| 326 | 8031 | 8034 | Ohio-class | 1 | 1 | Benjamin Franklin unlocks Ohio |
| 327 | 8032 | 8033 | Los Angeles-class (Improved 688i) SSN-700-773 | 1 | 1 | LA Early unlocks 688i |
| 328 | 8033 | 8036 | Seawolf-class | 1 | 1 | LA 688i unlocks Seawolf |
| 329 | 8034 | 8035 | Ohio-class (SSGN) | 1 | 2 | Ohio unlocks SSGN conversion |
| 330 | 8034 | 8038 | Columbia-class | 1 | 2 | Ohio unlocks Columbia (future) |
| 331 | 8036 | 8037 | Virginia-class | 1 | 1 | Seawolf unlocks Virginia |

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
| 9 | USA | CV | Starting | First US aircraft carrier, experimental platform proving carrier concept viability | #696969 | 5000 | 5000 | NULL | NULL | Experimental | Experimental | Langley (CV-1) standalone. FREE starting carrier. Slow 15 knots. Converted collier. Proves carrier concept despite limitations. |
| 10 | USA | CV | Main Line | Primary carrier development path from battlecruiser conversions through nuclear supercarriers, culminating in ultimate carrier design | #FFD700 | 5001 | 5011 | NULL | NULL | Battlecruiser Conversion | Ultimate Carrier | Lexington → Ranger → Yorktown → Essex → Midway → Forrestal → Kitty Hawk → Enterprise → Nimitz. Evolution from 33-knot conversions through jet age to nuclear power (1927-1975). Primary progression to ultimate carrier. |
| 11 | USA | CV | Modernization | Essex-class post-war refits and jet age modernizations | #9370DB | 5005 | 5006 | 10 | NULL | Post-War | Jet Age | Essex 1947 Refit → Essex SCB-27A. Post-WWII upgrades: improved AA/radar (1947, $8.5M) to full jet capability with angled deck/steam cats (1951, $40M). Stems from Main Line Essex. Cheaper than building new. |
| 12 | USA | CL | Starting | FREE starting cruisers, tutorial introduction | #696969 | 6000 | 6001 | NULL | NULL | Protected Cruiser | Scout Cruiser | Chester + Omaha. FREE starting ships. Chester (1908) primitive scout, Omaha (1923) better option. |
| 13 | USA | CA/CAG | Heavy Main Line | 8" gun treaty heavy cruisers through WWII peak gun cruisers | #FFD700 | 6002 | 6016 | NULL | NULL | Treaty Heavy | Ultimate Gun | Pensacola → Northampton → Portland → New Orleans → Wichita → Baltimore → Oregon City → Des Moines. Treaty 8" guns evolving to ultimate auto-loading 8" cruisers. |
| 14 | USA | CL/CLG | Light Main Line | 6" gun light cruisers, firepower and mass production focus | #1E90FF | 6004 | 6017 | NULL | NULL | Treaty Light | Ultimate Light | Brooklyn → St. Louis → Cleveland → Fargo → Worcester. 15×6" guns (Brooklyn) to rapid-fire auto 6" (Worcester). Mass production emphasis. |
| 15 | USA | CLAA | AA Specialist | Anti-aircraft cruisers with dual-purpose 5" guns | #FF6347 | 6006 | 6015 | 14 | NULL | AA Cruiser | AA Cruiser | Atlanta → Oakland → Juneau. Stems from Light Main Line. 16×5" DP guns for fleet air defense. 18 ships total across 3 classes. |
| 16 | USA | CG | Guided Missile | Purpose-built guided missile cruisers, Aegis systems | #9370DB | 6024 | 6039 | 13, 14 | NULL | First Purpose CG | Ultimate Aegis | Leahy → Belknap → Ticonderoga (4 variants). Stems from both Heavy + Light main lines. First purpose CG to ultimate Aegis. 27 Ticonderogas built. |
| 17 | USA | CGN | Nuclear | Nuclear-powered cruisers, unlimited range | #FF1493 | 6023 | 6030 | 13 | NULL | First Nuclear | Improved Nuclear | Long Beach → Bainbridge → Truxtun → California → Virginia. Stems from Heavy Main Line. 9 nuclear cruisers total. Only Long Beach with C1W reactors, rest D2G. |
| 18 | USA | CAG/CLG | Conversion | Gun cruiser conversions to missile platforms (1950s-1960s) | #8B4513 | 6018 | 6028 | 13, 14 | NULL | First Missile | Late Conversion | Boston, Galveston, Providence, Albany, Chicago. Baltimore + Cleveland conversions. Terrier/Talos SAMs replace guns. Cheaper than building new. |
| 19 | USA | CG | Modernization | Cold War NTU (New Threat Upgrade) with Standard SM-2 missiles | #CD853F | 6031 | 6032 | 16 | NULL | Upgraded Missile | Upgraded Missile | Leahy NTU, Belknap NTU. Stems from Guided Missile branch. 1980s upgrades with Standard SM-2. Extends service life. |
| 20 | USA | CGN | Nuclear Modernization | Nuclear cruiser late-1980s modernizations with Aegis-ready systems | #BA55D3 | 6036 | 6036 | 17 | NULL | Modernized Nuclear | Modernized Nuclear | Virginia (Modernized). 1988 full modernization. Aegis-ready systems + Tomahawk. Extends 1976 design to late Cold War. |
| 21 | USA | CGN/CG | Paper Ship | Cancelled and conceptual cruiser designs | #DC143C | 6037 | 6040 | 16, 17 | NULL | Strike Cruiser | Future Cruiser | Strike Cruiser CGN (1975 cancelled), CG(X) (2020s cancelled). -10% reliability. Strike Cruiser: Aegis + Tomahawk + nuclear. CG(X): Next-gen systems. |
| 22 | USA | DL | Alternative | Destroyer leader / frigate hybrids, niche roles | #FF8C00 | 6021 | 6021 | 14 | NULL | Frigate/Light | Frigate/Light | Norfolk-class. Large DD/light cruiser hybrid. 8×3" guns. ASW + AA focus. 1 ship built. Stems from Light Main Line. |
| 23 | USA | DD | Starting | FREE starting destroyers, tutorial introduction | #696969 | 7000 | 7001 | NULL | NULL | Early Destroyer | Early Destroyer | Bainbridge + Smith. FREE starting ships. Bainbridge (1902) first US destroyer, Smith (1909) better option. |
| 24 | USA | DD | Pre-WWI | Early torpedo boat destroyers, pre-WWI fleet progression | #8B4513 | 7002 | 7004 | NULL | NULL | Pre-WWI | Pre-WWI | Paulding → Cassin → Sampson. 700-1,200 tons. Oil-fired boilers, improved range. Final pre-WWI designs. |
| 25 | USA | DD | Four-Stacker | WWI flush-deck mass production, four-stack destroyers | #FFD700 | 7005 | 7007 | 24 | NULL | WWI | WWI | Caldwell → Wickes → Clemson. Stems from Pre-WWI. Flush deck design. 267 ships total (111 Wickes + 156 Clemson). Largest DD classes. |
| 26 | USA | DD | Interwar | Treaty-era destroyers, balanced gun-torpedo designs | #1E90FF | 7009 | 7013 | 25 | NULL | Interwar | Interwar | Farragut → Mahan → Gridley/Bagley. Stems from Four-Stacker. Enclosed guns, improved seakeeping. Torpedo focus (12-16 tubes). |
| 27 | USA | DD | Pre-WWII | Late 1930s refined designs leading to WWII standard | #9370DB | 7014 | 7018 | 26 | NULL | Pre-War | Pre-War | Benham → Sims → Benson → Gleaves → Bristol. Stems from Interwar. Refined pre-war designs. Bridge to Fletcher. |
| 28 | USA | DD | WWII Main Line | Fletcher, Sumner, Gearing - WWII mass production workhorses | #DC143C | 7019 | 7022 | 27 | NULL | WWII Workhorse | Ultimate WWII | Fletcher → Sumner → Gearing. Stems from Pre-WWII. 175 Fletcher + 67 Sumner + 98 Gearing = 340 ships. Most successful DD classes. |
| 29 | USA | DD | Modernization | FRAM I/II ASW upgrades, Cold War modernizations | #CD853F | 7020 | 7023 | 28 | NULL | FRAM Upgrade | FRAM Upgrade | Fletcher FRAM, Gearing FRAM. Stems from WWII Main Line. 1960s ASW modernizations. DASH helicopter, ASROC, new sonars. Extends service life 15+ years. |
| 30 | USA | DD/DDR/APD | Alternative | High-speed transports (APD), radar pickets (DDR), niche roles | #FF8C00 | 7008 | 7024 | 25, 28 | NULL | WWII Conversion | Radar Picket | Wickes APD, Gearing DDR. Stems from Four-Stacker and WWII lines. APD: 200 troops. DDR: early warning radar. Niche conversions. |
| 31 | USA | DD/DDG/DL | Post-War/Missile | First post-war designs, transition to guided missiles | #BA55D3 | 7025 | 7030 | 28 | NULL | First Post-War | NTU Upgrade | Forrest Sherman → Farragut DDG → Adams → Adams NTU. Stems from WWII. First post-war all-gun (Sherman) to first missile DDG (Farragut). 3"/50 guns to Tartar SAM. |
| 32 | USA | DD/DDG | Gas Turbine | Revolutionary gas turbine propulsion, Spruance-class era | #00CED1 | 7031 | 7033 | 31 | NULL | Gas Turbine DD | Modified Spruance | Spruance → Spruance VLS → Kidd. Stems from Post-War/Missile. First gas turbine DD (4× LM2500). 31 Spruance + 4 Kidd. Revolutionary propulsion. |
| 33 | USA | DDG | Aegis Main Line | Arleigh Burke-class progression through all flights | #FF1493 | 7034 | 7037 | 32 | NULL | Early Aegis DD | Ultimate Aegis | Burke F1 → F2 → F2A → F3. Stems from Gas Turbine. SPY-1D Aegis. Flight I-III: 89+ ships. Most numerous Aegis destroyer. Ultimate production DDG. |
| 34 | USA | DDG | Stealth/Future | Stealth destroyer and future next-generation concepts | #696969 | 7038 | 7040 | 33 | NULL | Stealth | Future | Zumwalt → Burke F4 → DDG(X). Stems from Aegis. Zumwalt: 3 ships, stealth, tumblehome. Burke F4 & DDG(X): future/paper designs. |
| 35 | USA | SS | Starting | FREE starting submarines, tutorial introduction | #696969 | 8000 | 8001 | NULL | NULL | Early Submarine | Early Submarine | Holland + A-class. FREE starting ships. Holland (1900) first US submarine SS-1, A-class (1903) better option. 64-107 tons. |
| 36 | USA | SS | Coastal | Small coastal patrol submarines, limited range | #8B4513 | 8002 | 8004 | NULL | NULL | Coastal | Coastal | C → F → H. Stems from Starting. 275-350 tons. Coastal patrol only. H-class: 18 ships, largest early class. Limited range. |
| 37 | USA | SS | Fleet Diesel | WWI/Interwar ocean-going diesel fleet submarines | #1E90FF | 8005 | 8012 | 36 | NULL | WWI Fleet | Pre-War Peak | L → O → R → S → Porpoise → Salmon → Sargo. Stems from Coastal. Ocean-going capability. 450-1,450 tons. S-class: 48 ships, long-serving. Pre-war pinnacle: Sargo. |
| 38 | USA | SS | WWII Main Line | Gato, Balao, Tench - WWII mass production diesel submarines | #DC143C | 8013 | 8019 | 37 | NULL | Early WWII | Peak Diesel | Tambor → Gar → Gato → Balao → Tench. Stems from Fleet Diesel. 228 total ships (77 Gato + 122 Balao + 29 Tench). Most successful submarine classes. Balao: 400ft test depth. |
| 39 | USA | SS | Modernization | GUPPY snorkel upgrades, Cold War diesel modernizations | #CD853F | 8020 | 8021 | 38 | NULL | GUPPY Upgrade | Full GUPPY | Balao GUPPY, Tench GUPPY IIA. Stems from WWII Main Line. 1947-1952 snorkel + streamlining upgrades. GUPPY = Greater Underwater Propulsion Power Program. Extends service life. |
| 40 | USA | SSN | Nuclear Attack | Nuclear-powered attack submarines, unlimited range | #FF1493 | 8022 | 8037 | 38 | NULL | Nuclear Revolution | Current Production | Nautilus → Skate → Skipjack → Thresher/Permit → Sturgeon → LA Early → LA 688i → Seawolf → Virginia. Stems from WWII. Revolutionary unlimited range. Teardrop hull (Skipjack). 62 LA-class total. Current production: Virginia. |
| 41 | USA | SSBN | Ballistic Missile | Strategic ballistic missile submarines, nuclear deterrent | #9370DB | 8025 | 8038 | 40 | NULL | First SSBN | Future SSBN | George Washington → Ethan Allen → Lafayette → Benjamin Franklin → Ohio → Columbia. Stems from Nuclear Attack. Strategic nuclear deterrent. 16-24 ICBMs. 31 Lafayette-class largest. Columbia: future 2028. |
| 42 | USA | SS/SSN/SSGN/SST | Alternative | Experimental designs, training subs, cruise missile conversions | #FF8C00 | 8009 | 8035 | 37, 36, 40, 41 | NULL | Cruiser Sub | Cruise Missile | V-class cruiser sub, Mackerel/Barracuda training, Seawolf SSN-575 experimental, Ohio SSGN. Multiple stems. V-class: 6" deck gun, experimental. Seawolf: failed sodium reactor. Ohio SSGN: 154 Tomahawk. |

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
| 4000 | USA | P-38 Lightning | 1941 | Ground Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4001 |
| 4001 | USA | P-38J Lightning | 1943 | Ground Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 25 | 0 | 0 | 0 | 4000 | 4002 |
| 4002 | USA | P-47 Thunderbolt | 1942 | Ground Aircraft | Fighter | Aircraft | 2800 | 3 | 5600 | 3 | 18 | 28 | 0 | 0 | 0 | 4001 | 4003 |
| 4003 | USA | P-47D Thunderbolt | 1944 | Ground Aircraft | Fighter | Aircraft | 3200 | 3 | 6400 | 3 | 20 | 32 | 0 | 0 | 0 | 4002 | 4004 |
| 4004 | USA | P-51 Mustang | 1943 | Ground Aircraft | Fighter | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 35 | 0 | 0 | 0 | 4003 | 4010 |
| 4010 | USA | P-80 Shooting Star | 1945 | Ground Aircraft | Jet Fighter | Aircraft | 4500 | 4 | 9000 | 4 | 28 | 48 | 0 | 0 | 0 | 4004 | 4011 |
| 4011 | USA | F-84 Thunderjet | 1947 | Ground Aircraft | Jet Fighter | Aircraft | 5000 | 4 | 10000 | 4 | 30 | 52 | 0 | 0 | 0 | 4010 | 4012 |
| 4012 | USA | F-86 Sabre | 1949 | Ground Aircraft | Jet Fighter | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 58 | 0 | 0 | 0 | 4011 | 4013 |
| 4013 | USA | F-100 Super Sabre | 1954 | Ground Aircraft | Jet Fighter | Aircraft | 6500 | 5 | 13000 | 5 | 38 | 68 | 0 | 0 | 0 | 4012 | 4014,4020 |
| 4014 | USA | F-104 Starfighter | 1958 | Ground Aircraft | Interceptor | Aircraft | 7000 | 6 | 14000 | 6 | 40 | 75 | 0 | 0 | 0 | 4013 | 4015 |
| 4015 | USA | F-105 Thunderchief | 1958 | Ground Aircraft | Strike | Aircraft | 7500 | 6 | 15000 | 6 | 42 | 82 | 0 | 0 | 0 | 4014 | 4016 |
| 4016 | USA | F-111 Aardvark | 1967 | Ground Aircraft | Strike | Aircraft | 10000 | 8 | 20000 | 8 | 52 | 115 | 0 | 0 | 0 | 4015 | 4030 |
| 4020 | USA | F-4C Phantom II | 1963 | Ground Aircraft | Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 98 | 0 | 0 | 0 | 4013 | 4021 |
| 4021 | USA | F-4E Phantom II | 1967 | Ground Aircraft | Multi-Role | Aircraft | 9500 | 8 | 19000 | 8 | 50 | 105 | 0 | 0 | 0 | 4020 | 4022,4030 |
| 4022 | USA | F-5 Freedom Fighter | 1963 | Ground Aircraft | Export Fighter | Aircraft | 4500 | 4 | 9000 | 4 | 25 | 55 | 0 | 0 | 0 | 4020 | 4023 |
| 4023 | USA | F-5E Tiger II | 1972 | Ground Aircraft | Export Fighter | Aircraft | 5000 | 4 | 10000 | 4 | 28 | 62 | 0 | 0 | 0 | 4022 | 4040 |
| 4030 | USA | F-15A Eagle | 1976 | Ground Aircraft | Air Superiority | Aircraft | 12000 | 10 | 24000 | 10 | 55 | 135 | 0 | 0 | 0 | 4021,4016 | 4031 |
| 4031 | USA | F-15C Eagle | 1979 | Ground Aircraft | Air Superiority | Aircraft | 13000 | 10 | 26000 | 10 | 58 | 145 | 0 | 0 | 0 | 4030 | 4032 |
| 4032 | USA | F-15E Strike Eagle | 1988 | Ground Aircraft | Multi-Role | Aircraft | 14000 | 11 | 28000 | 11 | 60 | 155 | 0 | 0 | 0 | 4031 | 4033 |
| 4033 | USA | F-15EX Eagle II | 2021 | Ground Aircraft | Multi-Role | Aircraft | 16000 | 13 | 32000 | 13 | 65 | 180 | 0 | 0 | 0 | 4032 | 4050 |
| 4040 | USA | F-16A Fighting Falcon | 1978 | Ground Aircraft | Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 42 | 108 | 0 | 0 | 0 | 4023,4030 | 4041 |
| 4041 | USA | F-16C Block 30 | 1984 | Ground Aircraft | Multi-Role | Aircraft | 10000 | 8 | 20000 | 8 | 45 | 120 | 0 | 0 | 0 | 4040 | 4042 |
| 4042 | USA | F-16C Block 52 | 1991 | Ground Aircraft | Multi-Role | Aircraft | 11000 | 9 | 22000 | 9 | 48 | 132 | 0 | 0 | 0 | 4041 | 4043 |
| 4043 | USA | F-16V Viper | 2015 | Ground Aircraft | Multi-Role | Aircraft | 12500 | 10 | 25000 | 10 | 52 | 152 | 0 | 0 | 0 | 4042 | 4050 |
| 4050 | USA | F-22A Raptor | 2005 | Ground Aircraft | Stealth Fighter | Aircraft | 20000 | 16 | 40000 | 16 | 72 | 225 | 0 | 0 | 0 | 4033,4043 | 4051 |
| 4051 | USA | F-35A Lightning II | 2016 | Ground Aircraft | Stealth Multi-Role | Aircraft | 22000 | 17 | 44000 | 17 | 75 | 245 | 0 | 0 | 0 | 4050 |  |
| 4060 | USA | B-17 Flying Fortress | 1941 | Ground Aircraft | Heavy Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4061 |
| 4061 | USA | B-17G Flying Fortress | 1943 | Ground Aircraft | Heavy Bomber | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 35 | 0 | 0 | 0 | 4060 | 4062 |
| 4062 | USA | B-24 Liberator | 1941 | Ground Aircraft | Heavy Bomber | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 35 | 0 | 0 | 0 | 4061 | 4063 |
| 4063 | USA | B-29 Superfortress | 1944 | Ground Aircraft | Heavy Bomber | Aircraft | 5000 | 4 | 10000 | 4 | 32 | 55 | 0 | 0 | 0 | 4062 | 4070 |
| 4070 | USA | B-36 Peacemaker | 1949 | Ground Aircraft | Strategic Bomber | Aircraft | 8000 | 7 | 16000 | 7 | 48 | 92 | 0 | 0 | 0 | 4063 | 4071 |
| 4071 | USA | B-47 Stratojet | 1951 | Ground Aircraft | Strategic Bomber | Aircraft | 7500 | 6 | 15000 | 6 | 45 | 88 | 0 | 0 | 0 | 4070 | 4072 |
| 4072 | USA | B-52 Stratofortress | 1955 | Ground Aircraft | Strategic Bomber | Aircraft | 10000 | 8 | 20000 | 8 | 55 | 115 | 0 | 0 | 0 | 4071 | 4073 |
| 4073 | USA | B-52H Stratofortress | 1961 | Ground Aircraft | Strategic Bomber | Aircraft | 11000 | 9 | 22000 | 9 | 58 | 125 | 0 | 0 | 0 | 4072 | 4080 |
| 4074 | USA | B-58 Hustler | 1960 | Ground Aircraft | Supersonic Bomber | Aircraft | 9000 | 7 | 18000 | 7 | 50 | 105 | 0 | 0 | 0 | 4072 | 4075 |
| 4075 | USA | FB-111A | 1969 | Ground Aircraft | Strategic Bomber | Aircraft | 10500 | 9 | 21000 | 9 | 52 | 118 | 0 | 0 | 0 | 4074,4016 | 4080 |
| 4080 | USA | B-1B Lancer | 1986 | Ground Aircraft | Strategic Bomber | Aircraft | 15000 | 12 | 30000 | 12 | 65 | 165 | 0 | 0 | 0 | 4073,4075 | 4081 |
| 4081 | USA | B-2A Spirit | 1997 | Ground Aircraft | Stealth Bomber | Aircraft | 25000 | 20 | 50000 | 20 | 85 | 280 | 0 | 0 | 0 | 4080 | 4082 |
| 4082 | USA | B-21 Raider | 2025 | Ground Aircraft | Stealth Bomber | Aircraft | 28000 | 22 | 56000 | 22 | 90 | 310 | 0 | 0 | 0 | 4081 |  |
| 4090 | USA | A-10A Thunderbolt II | 1977 | Ground Aircraft | Close Air Support | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4091 |
| 4091 | USA | A-10C Thunderbolt II | 2007 | Ground Aircraft | Close Air Support | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 108 | 0 | 0 | 0 | 4090 |  |
| 4092 | USA | AC-130H Spectre | 1972 | Ground Aircraft | Gunship | Aircraft | 7500 | 6 | 15000 | 6 | 42 | 98 | 0 | 0 | 0 | 4090 | 4093 |
| 4093 | USA | AC-130U Spooky | 1995 | Ground Aircraft | Gunship | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 122 | 0 | 0 | 0 | 4092 | 4094 |
| 4094 | USA | AC-130J Ghostrider | 2015 | Ground Aircraft | Gunship | Aircraft | 11000 | 9 | 22000 | 9 | 52 | 145 | 0 | 0 | 0 | 4093 |  |
| 4100 | USA | C-47 Skytrain | 1941 | Ground Aircraft | Transport | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4101 |
| 4101 | USA | C-54 Skymaster | 1942 | Ground Aircraft | Transport | Aircraft | 2500 | 2 | 5000 | 2 | 18 | 28 | 0 | 0 | 0 | 4100 | 4102 |
| 4102 | USA | C-119 Flying Boxcar | 1950 | Ground Aircraft | Transport | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 42 | 0 | 0 | 0 | 4101 | 4103 |
| 4103 | USA | C-130A Hercules | 1956 | Ground Aircraft | Transport | Aircraft | 5000 | 4 | 10000 | 4 | 32 | 62 | 0 | 0 | 0 | 4102 | 4104 |
| 4104 | USA | C-130H Hercules | 1974 | Ground Aircraft | Transport | Aircraft | 6000 | 5 | 12000 | 5 | 38 | 78 | 0 | 0 | 0 | 4103 | 4105 |
| 4105 | USA | C-130J Super Hercules | 1999 | Ground Aircraft | Transport | Aircraft | 8000 | 7 | 16000 | 7 | 45 | 108 | 0 | 0 | 0 | 4104 | 4110 |
| 4110 | USA | C-141 Starlifter | 1965 | Ground Aircraft | Strategic Transport | Aircraft | 8000 | 7 | 16000 | 7 | 48 | 95 | 0 | 0 | 0 | 4104 | 4111 |
| 4111 | USA | C-5A Galaxy | 1970 | Ground Aircraft | Strategic Transport | Aircraft | 12000 | 10 | 24000 | 10 | 62 | 135 | 0 | 0 | 0 | 4110 | 4112 |
| 4112 | USA | C-5M Super Galaxy | 2009 | Ground Aircraft | Strategic Transport | Aircraft | 14000 | 11 | 28000 | 11 | 68 | 165 | 0 | 0 | 0 | 4111 | 4113 |
| 4113 | USA | C-17 Globemaster III | 1995 | Ground Aircraft | Strategic Transport | Aircraft | 13000 | 11 | 26000 | 11 | 65 | 155 | 0 | 0 | 0 | 4111 | 4105 |
| 4120 | USA | UH-1 Iroquois | 1959 | Ground Aircraft | Utility Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4121 |
| 4121 | USA | UH-1H Huey | 1967 | Ground Aircraft | Utility Helo | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 42 | 0 | 0 | 0 | 4120 | 4122,4130 |
| 4122 | USA | UH-60A Black Hawk | 1979 | Ground Aircraft | Utility Helo | Aircraft | 5000 | 4 | 10000 | 4 | 28 | 68 | 0 | 0 | 0 | 4121 | 4123 |
| 4123 | USA | UH-60M Black Hawk | 2006 | Ground Aircraft | Utility Helo | Aircraft | 6500 | 5 | 13000 | 5 | 32 | 88 | 0 | 0 | 0 | 4122 |  |
| 4130 | USA | AH-1 Cobra | 1967 | Ground Aircraft | Attack Helo | Aircraft | 4000 | 3 | 8000 | 3 | 22 | 52 | 0 | 0 | 0 | 4121 | 4131 |
| 4131 | USA | AH-64A Apache | 1986 | Ground Aircraft | Attack Helo | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 105 | 0 | 0 | 0 | 4130 | 4132 |
| 4132 | USA | AH-64D Longbow Apache | 1997 | Ground Aircraft | Attack Helo | Aircraft | 9500 | 8 | 19000 | 8 | 48 | 128 | 0 | 0 | 0 | 4131 | 4133 |
| 4133 | USA | AH-64E Guardian | 2011 | Ground Aircraft | Attack Helo | Aircraft | 11000 | 9 | 22000 | 9 | 52 | 145 | 0 | 0 | 0 | 4132 |  |
| 4140 | USA | CH-47A Chinook | 1962 | Ground Aircraft | Heavy Transport Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4141 |
| 4141 | USA | CH-47D Chinook | 1982 | Ground Aircraft | Heavy Transport Helo | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 72 | 0 | 0 | 0 | 4140 | 4142 |
| 4142 | USA | CH-47F Chinook | 2007 | Ground Aircraft | Heavy Transport Helo | Aircraft | 7000 | 6 | 14000 | 6 | 38 | 95 | 0 | 0 | 0 | 4141 |  |
| 4150 | USA | U-2A Dragon Lady | 1957 | Ground Aircraft | Reconnaissance | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4151 |
| 4151 | USA | U-2R Dragon Lady | 1967 | Ground Aircraft | Reconnaissance | Aircraft | 7000 | 6 | 14000 | 6 | 38 | 88 | 0 | 0 | 0 | 4150 | 4152 |
| 4152 | USA | SR-71 Blackbird | 1966 | Ground Aircraft | Reconnaissance | Aircraft | 12000 | 10 | 24000 | 10 | 58 | 145 | 0 | 0 | 0 | 4151 | 4153 |
| 4153 | USA | RQ-4 Global Hawk | 2001 | Ground Aircraft | UAV Recon | Aircraft | 10000 | 8 | 20000 | 8 | 45 | 135 | 0 | 0 | 0 | 4152 | 4154 |
| 4154 | USA | MQ-9 Reaper | 2007 | Ground Aircraft | UAV Attack | Aircraft | 8000 | 7 | 16000 | 7 | 38 | 108 | 0 | 0 | 0 | 4153 | 4155 |
| 4155 | USA | MQ-9B Sky Guardian | 2020 | Ground Aircraft | UAV Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 42 | 125 | 0 | 0 | 0 | 4154 |  |
| 4160 | USA | KC-135 Stratotanker | 1957 | Ground Aircraft | Tanker | Aircraft | 6000 | 5 | 12000 | 5 | 38 | 72 | 0 | 0 | 0 | 4072 | 4161 |
| 4161 | USA | KC-10 Extender | 1981 | Ground Aircraft | Tanker | Aircraft | 9000 | 7 | 18000 | 7 | 52 | 118 | 0 | 0 | 0 | 4160 | 4162 |
| 4162 | USA | KC-46 Pegasus | 2019 | Ground Aircraft | Tanker | Aircraft | 11000 | 9 | 22000 | 9 | 58 | 145 | 0 | 0 | 0 | 4161 |  |
| 4200 | British | Spitfire Mk I | 1940 | Ground Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4201 |
| 4201 | British | Spitfire Mk V | 1941 | Ground Aircraft | Fighter | Aircraft | 2200 | 2 | 4400 | 2 | 14 | 22 | 0 | 0 | 0 | 4200 | 4202 |
| 4202 | British | Spitfire Mk IX | 1942 | Ground Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 16 | 26 | 0 | 0 | 0 | 4201 | 4203 |
| 4203 | British | Spitfire Mk XIV | 1944 | Ground Aircraft | Fighter | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 30 | 0 | 0 | 0 | 4202 | 4210 |
| 4210 | British | Meteor F.1 | 1944 | Ground Aircraft | Jet Fighter | Aircraft | 4000 | 3 | 8000 | 3 | 25 | 45 | 0 | 0 | 0 | 4203 | 4211 |
| 4211 | British | Meteor F.8 | 1950 | Ground Aircraft | Jet Fighter | Aircraft | 4500 | 4 | 9000 | 4 | 28 | 52 | 0 | 0 | 0 | 4210 | 4212 |
| 4212 | British | Hunter F.1 | 1954 | Ground Aircraft | Jet Fighter | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 62 | 0 | 0 | 0 | 4211 | 4213 |
| 4213 | British | Lightning F.1 | 1960 | Ground Aircraft | Interceptor | Aircraft | 7000 | 6 | 14000 | 6 | 40 | 82 | 0 | 0 | 0 | 4212 | 4214 |
| 4214 | British | Phantom FGR.2 | 1969 | Ground Aircraft | Multi-Role | Aircraft | 9500 | 8 | 19000 | 8 | 50 | 115 | 0 | 0 | 0 | 4213 | 4220 |
| 4220 | British | Tornado F.3 | 1986 | Ground Aircraft | Interceptor | Aircraft | 10000 | 8 | 20000 | 8 | 52 | 128 | 0 | 0 | 0 | 4214 | 4221 |
| 4221 | British | Typhoon FGR.4 | 2007 | Ground Aircraft | Multi-Role | Aircraft | 14000 | 11 | 28000 | 11 | 62 | 165 | 0 | 0 | 0 | 4220 | 4222 |
| 4222 | British | F-35B Lightning II (RAF) | 2018 | Ground Aircraft | Stealth Multi-Role | Aircraft | 20000 | 16 | 40000 | 16 | 72 | 220 | 0 | 0 | 0 | 4221 |  |
| 4230 | British | Lancaster | 1942 | Ground Aircraft | Heavy Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4231 |
| 4231 | British | Lincoln | 1945 | Ground Aircraft | Heavy Bomber | Aircraft | 3500 | 3 | 7000 | 3 | 22 | 38 | 0 | 0 | 0 | 4230 | 4232 |
| 4232 | British | Canberra B.2 | 1951 | Ground Aircraft | Bomber | Aircraft | 5000 | 4 | 10000 | 4 | 30 | 58 | 0 | 0 | 0 | 4231 | 4233 |
| 4233 | British | Vulcan B.1 | 1957 | Ground Aircraft | Strategic Bomber | Aircraft | 8000 | 7 | 16000 | 7 | 48 | 95 | 0 | 0 | 0 | 4232 | 4234 |
| 4234 | British | Vulcan B.2 | 1960 | Ground Aircraft | Strategic Bomber | Aircraft | 9000 | 7 | 18000 | 7 | 52 | 108 | 0 | 0 | 0 | 4233 |  |
| 4240 | British | Harrier GR.1 | 1969 | Ground Aircraft | V/STOL Attack | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4241 |
| 4241 | British | Harrier GR.7 | 1990 | Ground Aircraft | V/STOL Attack | Aircraft | 8000 | 7 | 16000 | 7 | 42 | 108 | 0 | 0 | 0 | 4240 | 4222 |
| 4250 | British | C-130K Hercules (RAF) | 1967 | Ground Aircraft | Transport | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4251 |
| 4251 | British | C-130J Hercules (RAF) | 2000 | Ground Aircraft | Transport | Aircraft | 7000 | 6 | 14000 | 6 | 42 | 98 | 0 | 0 | 0 | 4250 | 4252 |
| 4252 | British | A400M Atlas | 2014 | Ground Aircraft | Transport | Aircraft | 11000 | 9 | 22000 | 9 | 55 | 145 | 0 | 0 | 0 | 4251 |  |
| 4260 | British | Apache AH.1 (RAF) | 2001 | Ground Aircraft | Attack Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4261 |
| 4261 | British | Apache AH-64E (RAF) | 2020 | Ground Aircraft | Attack Helo | Aircraft | 10000 | 8 | 20000 | 8 | 50 | 135 | 0 | 0 | 0 | 4260 |  |
| 4270 | British | Puma HC.1 | 1971 | Ground Aircraft | Utility Helo | Aircraft | 3500 | 3 | 7000 | 3 | 20 | 48 | 0 | 0 | 0 | 4260 | 4271 |
| 4271 | British | Merlin HC.3 | 2001 | Ground Aircraft | Transport Helo | Aircraft | 6000 | 5 | 12000 | 5 | 35 | 88 | 0 | 0 | 0 | 4270 |  |
| 4300 | German | Bf 109E | 1940 | Ground Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4301 |
| 4301 | German | Bf 109F | 1941 | Ground Aircraft | Fighter | Aircraft | 2000 | 2 | 4000 | 2 | 12 | 18 | 0 | 0 | 0 | 4300 | 4302 |
| 4302 | German | Bf 109G | 1942 | Ground Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 22 | 0 | 0 | 0 | 4301 | 4303 |
| 4303 | German | Fw 190A | 1941 | Ground Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 22 | 0 | 0 | 0 | 4302 | 4304 |
| 4304 | German | Fw 190D | 1944 | Ground Aircraft | Fighter | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 28 | 0 | 0 | 0 | 4303 | 4310 |
| 4310 | German | CL-13 Sabre (German) | 1955 | Ground Aircraft | Jet Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4311 |
| 4311 | German | F-104G Starfighter | 1960 | Ground Aircraft | Interceptor | Aircraft | 6500 | 5 | 13000 | 5 | 38 | 72 | 0 | 0 | 0 | 4310 | 4312 |
| 4312 | German | F-4F Phantom II | 1973 | Ground Aircraft | Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 105 | 0 | 0 | 0 | 4311 | 4320 |
| 4320 | German | Tornado IDS | 1979 | Ground Aircraft | Strike | Aircraft | 10000 | 8 | 20000 | 8 | 52 | 125 | 0 | 0 | 0 | 4312 | 4321 |
| 4321 | German | Eurofighter Typhoon | 2004 | Ground Aircraft | Multi-Role | Aircraft | 14000 | 11 | 28000 | 11 | 62 | 165 | 0 | 0 | 0 | 4320 | 4322 |
| 4322 | German | F-35A Lightning II (Luftwaffe) | 2024 | Ground Aircraft | Stealth Multi-Role | Aircraft | 22000 | 17 | 44000 | 17 | 75 | 245 | 0 | 0 | 0 | 4321 |  |
| 4330 | German | Ju 87 Stuka | 1940 | Ground Aircraft | Dive Bomber | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4331 |
| 4331 | German | Ju 88 | 1940 | Ground Aircraft | Bomber | Aircraft | 2500 | 2 | 5000 | 2 | 16 | 24 | 0 | 0 | 0 | 4330 | 4332 |
| 4332 | German | He 111 | 1941 | Ground Aircraft | Bomber | Aircraft | 2500 | 2 | 5000 | 2 | 16 | 24 | 0 | 0 | 0 | 4331 | 4340 |
| 4340 | German | Tornado ECR | 1990 | Ground Aircraft | EW/Recon | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 122 | 0 | 0 | 0 | 4320 |  |
| 4350 | German | C-160 Transall | 1967 | Ground Aircraft | Transport | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4351 |
| 4351 | German | A400M (Luftwaffe) | 2014 | Ground Aircraft | Transport | Aircraft | 11000 | 9 | 22000 | 9 | 55 | 145 | 0 | 0 | 0 | 4350 |  |
| 4360 | German | CH-53G | 1973 | Ground Aircraft | Transport Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4361 |
| 4361 | German | CH-53GA | 1989 | Ground Aircraft | Transport Helo | Aircraft | 5000 | 4 | 10000 | 4 | 28 | 68 | 0 | 0 | 0 | 4360 | 4362 |
| 4362 | German | NH90 (Luftwaffe) | 2019 | Ground Aircraft | Utility Helo | Aircraft | 7500 | 6 | 15000 | 6 | 38 | 108 | 0 | 0 | 0 | 4361 |  |
| 4370 | German | UH-1D (Luftwaffe) | 1967 | Ground Aircraft | Utility Helo | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 42 | 0 | 0 | 0 | 4360 | 4371 |
| 4371 | German | Tiger UHT | 2005 | Ground Aircraft | Attack Helo | Aircraft | 8500 | 7 | 17000 | 7 | 45 | 118 | 0 | 0 | 0 | 4370 |  |
| 4400 | Japanese | A6M Zero | 1940 | Ground Aircraft | Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4401 |
| 4401 | Japanese | Ki-43 Hayabusa (Oscar) | 1941 | Ground Aircraft | Fighter | Aircraft | 2000 | 2 | 4000 | 2 | 12 | 18 | 0 | 0 | 0 | 4400 | 4402 |
| 4402 | Japanese | Ki-61 Hien (Tony) | 1943 | Ground Aircraft | Fighter | Aircraft | 2500 | 2 | 5000 | 2 | 15 | 22 | 0 | 0 | 0 | 4401 | 4403 |
| 4403 | Japanese | Ki-84 Hayate (Frank) | 1944 | Ground Aircraft | Fighter | Aircraft | 3000 | 3 | 6000 | 3 | 18 | 28 | 0 | 0 | 0 | 4402 | 4410 |
| 4410 | Japanese | F-86F Sabre (JASDF) | 1956 | Ground Aircraft | Jet Fighter | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4411 |
| 4411 | Japanese | F-104J Starfighter | 1962 | Ground Aircraft | Interceptor | Aircraft | 6500 | 5 | 13000 | 5 | 38 | 72 | 0 | 0 | 0 | 4410 | 4412 |
| 4412 | Japanese | F-4EJ Phantom II | 1971 | Ground Aircraft | Multi-Role | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 105 | 0 | 0 | 0 | 4411 | 4413 |
| 4413 | Japanese | F-4EJ Kai | 1984 | Ground Aircraft | Multi-Role | Aircraft | 9500 | 8 | 19000 | 8 | 50 | 115 | 0 | 0 | 0 | 4412 | 4420 |
| 4420 | Japanese | F-15J Eagle | 1981 | Ground Aircraft | Air Superiority | Aircraft | 12000 | 10 | 24000 | 10 | 55 | 135 | 0 | 0 | 0 | 4413 | 4421 |
| 4421 | Japanese | F-15J(M) Kai | 2004 | Ground Aircraft | Air Superiority | Aircraft | 13000 | 10 | 26000 | 10 | 58 | 148 | 0 | 0 | 0 | 4420 | 4430 |
| 4430 | Japanese | F-2A | 2000 | Ground Aircraft | Multi-Role | Aircraft | 11000 | 9 | 22000 | 9 | 52 | 138 | 0 | 0 | 0 | 4421 | 4431 |
| 4431 | Japanese | F-2B | 2002 | Ground Aircraft | Multi-Role | Aircraft | 11500 | 9 | 23000 | 9 | 54 | 145 | 0 | 0 | 0 | 4430 | 4440 |
| 4440 | Japanese | F-35A Lightning II (JASDF) | 2018 | Ground Aircraft | Stealth Multi-Role | Aircraft | 22000 | 17 | 44000 | 17 | 75 | 245 | 0 | 0 | 0 | 4431 | 4441 |
| 4441 | Japanese | F-15EX (JASDF) | 2024 | Ground Aircraft | Multi-Role | Aircraft | 16000 | 13 | 32000 | 13 | 65 | 185 | 0 | 0 | 0 | 4440,4421 |  |
| 4450 | Japanese | C-1 | 1974 | Ground Aircraft | Transport | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4451 |
| 4451 | Japanese | C-2 | 2017 | Ground Aircraft | Transport | Aircraft | 10000 | 8 | 20000 | 8 | 52 | 142 | 0 | 0 | 0 | 4450 |  |
| 4452 | Japanese | C-130H Hercules (JASDF) | 1981 | Ground Aircraft | Transport | Aircraft | 6000 | 5 | 12000 | 5 | 38 | 78 | 0 | 0 | 0 | 4450 | 4453 |
| 4453 | Japanese | KC-767 | 2008 | Ground Aircraft | Tanker | Aircraft | 9500 | 8 | 19000 | 8 | 52 | 128 | 0 | 0 | 0 | 4452 |  |
| 4460 | Japanese | UH-1H (JASDF) | 1973 | Ground Aircraft | Utility Helo | Aircraft | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 4461 |
| 4461 | Japanese | UH-60J Black Hawk | 1992 | Ground Aircraft | Utility Helo | Aircraft | 5500 | 5 | 11000 | 5 | 30 | 72 | 0 | 0 | 0 | 4460 | 4462 |
| 4462 | Japanese | UH-60J Kai | 2012 | Ground Aircraft | Utility Helo | Aircraft | 6500 | 5 | 13000 | 5 | 34 | 88 | 0 | 0 | 0 | 4461 |  |
| 4470 | Japanese | AH-1S Cobra (JASDF) | 1978 | Ground Aircraft | Attack Helo | Aircraft | 4500 | 4 | 9000 | 4 | 24 | 58 | 0 | 0 | 0 | 4460 | 4471 |
| 4471 | Japanese | AH-64D Apache (JASDF) | 2006 | Ground Aircraft | Attack Helo | Aircraft | 9000 | 7 | 18000 | 7 | 48 | 125 | 0 | 0 | 0 | 4470 |  |
| 4480 | Japanese | CH-47J Chinook | 1986 | Ground Aircraft | Transport Helo | Aircraft | 5500 | 5 | 11000 | 5 | 32 | 72 | 0 | 0 | 0 | 4460 | 4481 |
| 4481 | Japanese | CH-47JA Chinook | 2001 | Ground Aircraft | Transport Helo | Aircraft | 6500 | 5 | 13000 | 5 | 36 | 85 | 0 | 0 | 0 | 4480 |  |
| 9000 | USA | AN-M30 | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9001 | 0 |
| 9001 | USA | AN-M64 | GP Bomb | 1941 | Bombs | Bomb | 1500 | 2 | 3000 | 2 | 150 | 8 | 12 | 0 | 0 | 9000 | 9002 | 0 |
| 9002 | USA | AN-M65 | GP Bomb | 1942 | Bombs | Bomb | 1800 | 2 | 3600 | 2 | 180 | 10 | 15 | 0 | 0 | 9001 | 9003 | 0 |
| 9003 | USA | AN-M66 | GP Bomb | 1943 | Bombs | Bomb | 2200 | 2 | 4400 | 2 | 220 | 12 | 18 | 0 | 0 | 9002 | 9010 | 0 |
| 9010 | USA | Mk 81 | GP Bomb | 1950 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 14 | 22 | 0 | 0 | 9003 | 9011 | 0 |
| 9011 | USA | Mk 82 | GP Bomb | 1952 | Bombs | Bomb | 2800 | 3 | 5600 | 3 | 280 | 16 | 25 | 0 | 0 | 9010 | 9012,9020 | 0 |
| 9012 | USA | Mk 83 | GP Bomb | 1955 | Bombs | Bomb | 3200 | 3 | 6400 | 3 | 320 | 18 | 28 | 0 | 0 | 9011 | 9013 | 0 |
| 9013 | USA | Mk 84 | GP Bomb | 1958 | Bombs | Bomb | 3800 | 3 | 7600 | 3 | 380 | 22 | 35 | 0 | 0 | 9012 | 9020,9030 | 0 |
| 9020 | USA | GBU-10 Paveway I | LGB | 1968 | Bombs | Bomb | 9500 | 5 | 19000 | 5 | 950 | 28 | 55 | 0 | 0 | 9011,9013 | 9021 | 0 |
| 9021 | USA | GBU-12 Paveway II | LGB | 1976 | Bombs | Bomb | 6200 | 5 | 12400 | 5 | 620 | 32 | 62 | 0 | 0 | 9020 | 9022 | 0 |
| 9022 | USA | GBU-16 Paveway II | LGB | 1980 | Bombs | Bomb | 6800 | 6 | 13600 | 6 | 680 | 35 | 68 | 0 | 0 | 9021 | 9023 | 0 |
| 9023 | USA | GBU-24 Paveway III | LGB | 1983 | Bombs | Bomb | 7500 | 6 | 15000 | 6 | 750 | 38 | 78 | 0 | 0 | 9022 | 9024,9040 | 0 |
| 9024 | USA | GBU-28 | Bunker Buster | 1991 | Bombs | Bomb | 9500 | 8 | 19000 | 8 | 950 | 52 | 95 | 0 | 0 | 9023 | 9050 | 0 |
| 9030 | USA | Mk 117 | GP Bomb | 1960 | Bombs | Bomb | 3000 | 3 | 6000 | 3 | 300 | 18 | 32 | 0 | 0 | 9013 | 9031 | 0 |
| 9031 | USA | M117R | GP Bomb | 1970 | Bombs | Bomb | 3500 | 3 | 7000 | 3 | 350 | 22 | 38 | 0 | 0 | 9030 | 9032 | 0 |
| 9032 | USA | Mk 118 | Demolition Bomb | 1975 | Bombs | Bomb | 4200 | 4 | 8400 | 4 | 420 | 28 | 45 | 0 | 0 | 9031 | 9024 | 0 |
| 9040 | USA | GBU-15 | TV-Guided | 1975 | Bombs | Bomb | 7000 | 6 | 14000 | 6 | 700 | 38 | 72 | 0 | 0 | 9023 | 9041 | 0 |
| 9041 | USA | AGM-62 Walleye | TV-Guided | 1967 | Bombs | Bomb | 6500 | 5 | 13000 | 5 | 650 | 35 | 65 | 0 | 0 | 9020 | 9040 | 0 |
| 9050 | USA | GBU-31 JDAM | GPS-Guided | 1997 | Bombs | Bomb | 11000 | 9 | 22000 | 9 | 1100 | 55 | 125 | 0 | 0 | 9024 | 9051 | 0 |
| 9051 | USA | GBU-32 JDAM | GPS-Guided | 1999 | Bombs | Bomb | 11500 | 9 | 23000 | 9 | 1150 | 58 | 132 | 0 | 0 | 9050 | 9052 | 0 |
| 9052 | USA | GBU-38 JDAM | GPS-Guided | 2001 | Bombs | Bomb | 12000 | 10 | 24000 | 10 | 1200 | 62 | 138 | 0 | 0 | 9051 | 9053,9060 | 0 |
| 9053 | USA | GBU-54 LJDAM | Laser/GPS | 2008 | Bombs | Bomb | 13500 | 11 | 27000 | 11 | 1350 | 68 | 155 | 0 | 0 | 9052 | 9054 | 0 |
| 9054 | USA | GBU-56 LJDAM | Laser/GPS | 2010 | Bombs | Bomb | 14000 | 11 | 28000 | 11 | 1400 | 72 | 162 | 0 | 0 | 9053 | 9070 | 0 |
| 9060 | USA | GBU-39 SDB | Small Diameter | 2006 | Bombs | Bomb | 12500 | 10 | 25000 | 10 | 1250 | 58 | 145 | 0 | 0 | 9052 | 9061 | 0 |
| 9061 | USA | GBU-53 SDB II | Small Diameter | 2014 | Bombs | Bomb | 15000 | 12 | 30000 | 12 | 1500 | 72 | 178 | 0 | 0 | 9060 | 9070 | 0 |
| 9070 | USA | GBU-57 MOP | Bunker Buster | 2011 | Bombs | Bomb | 18000 | 14 | 36000 | 14 | 1800 | 85 | 195 | 0 | 0 | 9054,9061 |  | 0 |
| 9080 | USA | CBU-87 | Cluster Bomb | 1986 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9081 | 0 |
| 9081 | USA | CBU-97 | Sensor Fused | 1992 | Bombs | Bomb | 8500 | 7 | 17000 | 7 | 850 | 45 | 95 | 0 | 0 | 9080 | 9082 | 0 |
| 9082 | USA | CBU-103 | Cluster Bomb | 1997 | Bombs | Bomb | 9200 | 8 | 18400 | 8 | 920 | 48 | 105 | 0 | 0 | 9081 | 9083 | 0 |
| 9083 | USA | CBU-105 | Sensor Fused | 2001 | Bombs | Bomb | 10500 | 9 | 21000 | 9 | 1050 | 55 | 122 | 0 | 0 | 9082 |  | 0 |
| 9090 | USA | Mk 4 | Nuclear | 1949 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9091 | 0 |
| 9091 | USA | Mk 7 | Nuclear | 1952 | Bombs | Bomb | 12000 | 10 | 24000 | 10 | 1200 | 0 | 168 | 0 | 0 | 9090 | 9092 | 0 |
| 9092 | USA | Mk 15 | Nuclear | 1955 | Bombs | Bomb | 13500 | 11 | 27000 | 11 | 1350 | 0 | 188 | 0 | 0 | 9091 | 9093 | 0 |
| 9093 | USA | Mk 28 | Nuclear | 1958 | Bombs | Bomb | 15000 | 12 | 30000 | 12 | 1500 | 0 | 208 | 0 | 0 | 9092 | 9094 | 0 |
| 9094 | USA | Mk 43 | Nuclear | 1961 | Bombs | Bomb | 16500 | 13 | 33000 | 13 | 1650 | 0 | 228 | 0 | 0 | 9093 | 9095 | 0 |
| 9095 | USA | B57 | Nuclear | 1963 | Bombs | Bomb | 18000 | 14 | 36000 | 14 | 1800 | 0 | 248 | 0 | 0 | 9094 | 9096 | 0 |
| 9096 | USA | B61 | Nuclear | 1968 | Bombs | Bomb | 20000 | 16 | 40000 | 16 | 2000 | 0 | 285 | 0 | 0 | 9095 | 9097 | 0 |
| 9097 | USA | B83 | Nuclear | 1983 | Bombs | Bomb | 24000 | 19 | 48000 | 19 | 2400 | 0 | 348 | 0 | 0 | 9096 | 9098 | 0 |
| 9098 | USA | B61-12 | Nuclear | 2020 | Bombs | Bomb | 28000 | 22 | 56000 | 22 | 2800 | 0 | 425 | 0 | 0 | 9097 |  | 0 |
| 9100 | USA | Mk 77 | Incendiary | 1965 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9101 | 0 |
| 9101 | USA | BLU-27 | Incendiary | 1967 | Bombs | Bomb | 3500 | 3 | 7000 | 3 | 350 | 18 | 42 | 0 | 0 | 9100 | 9102 | 0 |
| 9102 | USA | Mk 78 | Incendiary | 1970 | Bombs | Bomb | 4000 | 4 | 8000 | 4 | 400 | 22 | 48 | 0 | 0 | 9101 |  | 0 |
| 9110 | USA | Mk 36 | Mine | 1943 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9111 | 0 |
| 9111 | USA | Mk 82 Mine | Mine | 1960 | Bombs | Bomb | 3200 | 3 | 6400 | 3 | 320 | 18 | 38 | 0 | 0 | 9110 | 9112 | 0 |
| 9112 | USA | Mk 62 Quickstrike | Mine | 1983 | Bombs | Bomb | 9500 | 5 | 19000 | 5 | 950 | 32 | 65 | 0 | 0 | 9111 | 9113 | 0 |
| 9113 | USA | Mk 63 Quickstrike | Mine | 1985 | Bombs | Bomb | 6000 | 5 | 12000 | 5 | 600 | 35 | 72 | 0 | 0 | 9112 | 9114 | 0 |
| 9114 | USA | Mk 65 Quickstrike | Mine | 1988 | Bombs | Bomb | 6800 | 6 | 13600 | 6 | 680 | 42 | 82 | 0 | 0 | 9113 |  | 0 |
| 9120 | USA | BLU-109 | Penetrator | 1985 | Bombs | Bomb | 7500 | 6 | 15000 | 6 | 750 | 48 | 85 | 0 | 0 | 9023 | 9121 | 0 |
| 9121 | USA | BLU-116 | Penetrator | 1996 | Bombs | Bomb | 9000 | 7 | 18000 | 7 | 900 | 55 | 105 | 0 | 0 | 9120 | 9122 | 0 |
| 9122 | USA | BLU-122 | Penetrator | 2003 | Bombs | Bomb | 11000 | 9 | 22000 | 9 | 1100 | 65 | 132 | 0 | 0 | 9121 |  | 0 |
| 9200 | British | 250 lb GP | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9201 | 0 |
| 9201 | British | 500 lb GP | GP Bomb | 1941 | Bombs | Bomb | 1500 | 2 | 3000 | 2 | 150 | 8 | 12 | 0 | 0 | 9200 | 9202 | 0 |
| 9202 | British | 1000 lb MC | GP Bomb | 1942 | Bombs | Bomb | 1800 | 2 | 3600 | 2 | 180 | 10 | 15 | 0 | 0 | 9201 | 9203 | 0 |
| 9203 | British | 4000 lb HC | Heavy Bomb | 1943 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 15 | 22 | 0 | 0 | 9202 | 9210 | 0 |
| 9210 | British | Tallboy | Heavy Bomb | 1944 | Bombs | Bomb | 4500 | 4 | 9000 | 4 | 450 | 28 | 42 | 0 | 0 | 9203 | 9211 | 0 |
| 9211 | British | Grand Slam | Heavy Bomb | 1945 | Bombs | Bomb | 6000 | 5 | 12000 | 5 | 600 | 38 | 55 | 0 | 0 | 9210 | 9220 | 0 |
| 9220 | British | 1000 lb GP (Post-war) | GP Bomb | 1950 | Bombs | Bomb | 2200 | 2 | 4400 | 2 | 220 | 12 | 22 | 0 | 0 | 9211 | 9221 | 0 |
| 9221 | British | 1000 lb HE | GP Bomb | 1955 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 14 | 25 | 0 | 0 | 9220 | 9222 | 0 |
| 9222 | British | Mk 13 (British) | GP Bomb | 1960 | Bombs | Bomb | 2800 | 3 | 5600 | 3 | 280 | 16 | 28 | 0 | 0 | 9221 | 9230 | 0 |
| 9230 | British | Paveway II (RAF) | LGB | 1977 | Bombs | Bomb | 6200 | 5 | 12400 | 5 | 620 | 32 | 62 | 0 | 0 | 9222 | 9231 | 0 |
| 9231 | British | Paveway III (RAF) | LGB | 1985 | Bombs | Bomb | 7500 | 6 | 15000 | 6 | 750 | 38 | 78 | 0 | 0 | 9230 | 9232 | 0 |
| 9232 | British | Enhanced Paveway II | LGB | 1998 | Bombs | Bomb | 9500 | 8 | 19000 | 8 | 950 | 48 | 105 | 0 | 0 | 9231 | 9240 | 0 |
| 9240 | British | Paveway IV | Dual-Mode | 2008 | Bombs | Bomb | 13000 | 11 | 26000 | 11 | 1300 | 62 | 152 | 0 | 0 | 9232 | 9241 | 0 |
| 9241 | British | SPEAR 3 | Powered Bomb | 2021 | Bombs | Bomb | 16500 | 13 | 33000 | 13 | 1650 | 72 | 198 | 0 | 0 | 9240 |  | 0 |
| 9250 | British | BL755 | Cluster Bomb | 1973 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9251 | 0 |
| 9251 | British | RBL755 | Cluster Bomb | 1985 | Bombs | Bomb | 9500 | 5 | 19000 | 5 | 950 | 32 | 65 | 0 | 0 | 9250 |  | 0 |
| 9260 | British | Blue Danube | Nuclear | 1953 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9261 | 0 |
| 9261 | British | Red Beard | Nuclear | 1961 | Bombs | Bomb | 15000 | 12 | 30000 | 12 | 1500 | 0 | 208 | 0 | 0 | 9260 | 9262 | 0 |
| 9262 | British | WE.177 | Nuclear | 1966 | Bombs | Bomb | 18000 | 14 | 36000 | 14 | 1800 | 0 | 248 | 0 | 0 | 9261 | 9263 | 0 |
| 9263 | British | WE.177A/B | Nuclear | 1976 | Bombs | Bomb | 21000 | 17 | 42000 | 17 | 2100 | 0 | 295 | 0 | 0 | 9262 |  | 0 |
| 9270 | British | CRV7 Pod | Rocket Pod | 1975 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9271 | 0 |
| 9271 | British | SNEB Rocket | Rocket Pod | 1980 | Bombs | Bomb | 3500 | 3 | 7000 | 3 | 350 | 18 | 42 | 0 | 0 | 9270 |  | 0 |
| 9300 | German | SC 50 | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9301 | 0 |
| 9301 | German | SC 250 | GP Bomb | 1941 | Bombs | Bomb | 1500 | 2 | 3000 | 2 | 150 | 8 | 12 | 0 | 0 | 9300 | 9302 | 0 |
| 9302 | German | SC 500 | GP Bomb | 1942 | Bombs | Bomb | 1800 | 2 | 3600 | 2 | 180 | 10 | 15 | 0 | 0 | 9301 | 9303 | 0 |
| 9303 | German | SC 1000 | GP Bomb | 1943 | Bombs | Bomb | 2200 | 2 | 4400 | 2 | 220 | 12 | 18 | 0 | 0 | 9302 | 9310 | 0 |
| 9310 | German | SC 1800 | Heavy Bomb | 1944 | Bombs | Bomb | 3500 | 3 | 7000 | 3 | 350 | 18 | 28 | 0 | 0 | 9303 | 9311 | 0 |
| 9311 | German | PC 1400 | AP Bomb | 1943 | Bombs | Bomb | 4000 | 4 | 8000 | 4 | 400 | 22 | 35 | 0 | 0 | 9303 | 9320 | 0 |
| 9320 | German | Fritz X | Guided Bomb | 1943 | Bombs | Bomb | 9500 | 5 | 19000 | 5 | 950 | 28 | 55 | 0 | 0 | 9311 | 9321 | 0 |
| 9321 | German | Hs 293 | Glide Bomb | 1943 | Bombs | Bomb | 9800 | 5 | 19600 | 5 | 980 | 32 | 62 | 0 | 0 | 9320 | 9330 | 0 |
| 9330 | German | 250 kg (Bundeswehr) | GP Bomb | 1960 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9331 | 0 |
| 9331 | German | 500 kg (Bundeswehr) | GP Bomb | 1965 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 14 | 22 | 0 | 0 | 9330 | 9332 | 0 |
| 9332 | German | DM 91 | GP Bomb | 1975 | Bombs | Bomb | 3000 | 3 | 6000 | 3 | 300 | 18 | 28 | 0 | 0 | 9331 | 9340 | 0 |
| 9340 | German | GBU-12 (Luftwaffe) | LGB | 1985 | Bombs | Bomb | 6200 | 5 | 12400 | 5 | 620 | 32 | 62 | 0 | 0 | 9332 | 9341 | 0 |
| 9341 | German | GBU-24 (Luftwaffe) | LGB | 1995 | Bombs | Bomb | 7500 | 6 | 15000 | 6 | 750 | 38 | 78 | 0 | 0 | 9340 | 9350 | 0 |
| 9350 | German | GBU-38 (Luftwaffe) | GPS-Guided | 2010 | Bombs | Bomb | 12000 | 10 | 24000 | 10 | 1200 | 62 | 138 | 0 | 0 | 9341 | 9351 | 0 |
| 9351 | German | GBU-54 (Luftwaffe) | Laser/GPS | 2015 | Bombs | Bomb | 13500 | 11 | 27000 | 11 | 1350 | 68 | 155 | 0 | 0 | 9350 |  | 0 |
| 9360 | German | MW-1 | Cluster Munition | 1982 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9361 | 0 |
| 9361 | German | DM 118 | Dispenser | 1990 | Bombs | Bomb | 6500 | 5 | 13000 | 5 | 650 | 38 | 72 | 0 | 0 | 9360 |  | 0 |
| 9400 | Japanese | Type 94 | GP Bomb | 1940 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9401 | 0 |
| 9401 | Japanese | Type 97 | GP Bomb | 1941 | Bombs | Bomb | 1500 | 2 | 3000 | 2 | 150 | 8 | 12 | 0 | 0 | 9400 | 9402 | 0 |
| 9402 | Japanese | Type 98 | GP Bomb | 1942 | Bombs | Bomb | 1800 | 2 | 3600 | 2 | 180 | 10 | 15 | 0 | 0 | 9401 | 9403 | 0 |
| 9403 | Japanese | Type 99 | GP Bomb | 1943 | Bombs | Bomb | 2200 | 2 | 4400 | 2 | 220 | 12 | 18 | 0 | 0 | 9402 | 9410 | 0 |
| 9410 | Japanese | Type 80 AP | AP Bomb | 1941 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 15 | 22 | 0 | 0 | 9401 | 9411 | 0 |
| 9411 | Japanese | Type 91 AP | AP Bomb | 1941 | Bombs | Bomb | 3000 | 3 | 6000 | 3 | 300 | 18 | 28 | 0 | 0 | 9410 |  | 0 |
| 9420 | Japanese | Type 3 Cluster | Incendiary | 1944 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9421 | 0 |
| 9421 | Japanese | Type 100 | Incendiary | 1944 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 12 | 22 | 0 | 0 | 9420 |  | 0 |
| 9430 | Japanese | 250 kg (JASDF) | GP Bomb | 1960 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9431 | 0 |
| 9431 | Japanese | 500 kg (JASDF) | GP Bomb | 1965 | Bombs | Bomb | 2500 | 2 | 5000 | 2 | 250 | 14 | 22 | 0 | 0 | 9430 | 9432 | 0 |
| 9432 | Japanese | Mk 82 (JASDF) | GP Bomb | 1975 | Bombs | Bomb | 2800 | 3 | 5600 | 3 | 280 | 16 | 25 | 0 | 0 | 9431 | 9440 | 0 |
| 9440 | Japanese | GBU-12 (JASDF) | LGB | 1990 | Bombs | Bomb | 6200 | 5 | 12400 | 5 | 620 | 32 | 62 | 0 | 0 | 9432 | 9441 | 0 |
| 9441 | Japanese | GBU-24 (JASDF) | LGB | 1998 | Bombs | Bomb | 7500 | 6 | 15000 | 6 | 750 | 38 | 78 | 0 | 0 | 9440 | 9450 | 0 |
| 9450 | Japanese | GBU-38 (JASDF) | GPS-Guided | 2012 | Bombs | Bomb | 12000 | 10 | 24000 | 10 | 1200 | 62 | 138 | 0 | 0 | 9441 | 9451 | 0 |
| 9451 | Japanese | GBU-54 (JASDF) | Laser/GPS | 2016 | Bombs | Bomb | 13500 | 11 | 27000 | 11 | 1350 | 68 | 155 | 0 | 0 | 9450 | 9460 | 0 |
| 9460 | Japanese | JDAM-ER (JASDF) | Extended Range | 2020 | Bombs | Bomb | 15000 | 12 | 30000 | 12 | 1500 | 72 | 172 | 0 | 0 | 9451 |  | 0 |
| 9470 | Japanese | CBU-87 (JASDF) | Cluster Bomb | 1995 | Bombs | Bomb | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |  | 9471 | 0 |
| 9471 | Japanese | CBU-97 (JASDF) | Sensor Fused | 2005 | Bombs | Bomb | 8500 | 7 | 17000 | 7 | 850 | 45 | 95 | 0 | 0 | 9470 |  | 0 |

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
