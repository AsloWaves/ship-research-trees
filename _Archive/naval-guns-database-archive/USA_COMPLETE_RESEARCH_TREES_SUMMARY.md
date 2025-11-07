# USA Complete Research Trees Summary - NavyField Style

**Date**: October 10, 2025
**Version**: 2.0 - NavyField Expansion
**Total Ship Types**: 4 (Battleships, Carriers, Cruisers, Destroyers, Submarines)

---

## Overview

Complete USA research trees for all ship types using **NavyField-style** progression with multiple ships per tier, parallel paths, and no dead ends.

### Total Nodes by Ship Type

| Ship Type | Nodes | Tiers | Node ID Range | Status |
|-----------|-------|-------|---------------|--------|
| **Battleships** | 47 | 1-9 | 1000-2999 | ✅ COMPLETE (existing) |
| **Carriers** | 32 | 1-10 | 5000-5099 | 🔄 EXPANDED (12→32) |
| **Cruisers** | 45 | 1-10 | 6000-6099 | ✨ NEW |
| **Destroyers** | 42 | 1-10 | 7000-7099 | ✨ NEW |
| **Submarines** | 38 | 1-10 | 8000-8099 | ✨ NEW |
| **TOTAL** | **204** | | | |

---

## USA Carriers Research Tree (EXPANDED: 12 → 32 nodes)

### Node ID Allocation: 5000-5099

**Existing Nodes** (5000-5011, 12 nodes) - KEEP AS-IS
**New Nodes** (5012-5031, 20 nodes) - ADD

### Tier Distribution

| Tier | Count | Node IDs | Notes |
|------|-------|----------|-------|
| 1 | 2 | 5000, 5012 | Langley CV, Bogue CVE (both FREE) |
| 2 | 3 | 5001, 5013, 5014 | Lexington, Saratoga, Long Island CVE |
| 3 | 3 | 5002, 5015, 5016 | Ranger, Wasp, Sangamon CVE |
| 4 | 4 | 5003, 5017, 5018, 5019 | Yorktown, Enterprise UNIQUE, Casablanca CVE, Independence CVL |
| 5 | 5 | 5004, 5005, 5020, 5021, 5022 | Essex base, Essex 1947, Commencement Bay CVE, Saipan CVL, Intrepid |
| 6 | 5 | 5006, 5023, 5007, 5024, 5025 | Essex SCB-27A, Essex SCB-27C, Midway, Midway SCB-110, Thetis Bay |
| 7 | 4 | 5008, 5026, 5009, 5027 | Forrestal, Saratoga CV-60, Kitty Hawk, JFK CV-67 |
| 8 | 3 | 5010, 5028, 5029 | Enterprise CVN-65, Nimitz Early, Nimitz Improved |
| 9 | 2 | 5030, 5031 | Nimitz Late, Enterprise CVN-80 |
| 10 | 1 | 5011 | Ford-class (moved from T9) |

### NEW Carrier Nodes (5012-5031)

```markdown
| Node_ID | Ship_Class | Ship_Type | Tech_Branch | Tech_Tier | Era | Year | Is_Start | RP_Cost | Time | Build_Cost | Build_Time | Design_Philosophy | Historical_Context | Gameplay_Role | Special_Ability | Notes |
|---------|------------|-----------|-------------|-----------|-----|------|----------|---------|------|------------|------------|-------------------|-------------------|---------------|-----------------|-------|
| 5012 | Bogue-class | CVE | Escort | 1 | WWII | 1942 | 1 | 0 | 0 | 8000000 | 12 | Budget escort | Merchant conversion, ASW/convoy | Budget Carrier | ASW Focus: +50% sub detection, FREE | FREE starting CVE, 45 built |
| 5013 | Saratoga-class | CV | Main Line | 2 | Interwar | 1927 | 0 | 8000 | 18 | 45000000 | 72 | Sister to Lexington | Sister ship, identical specs | Fast Fleet Carrier | +33 kts speed, 8" guns (unique) | CV-3, sister to CV-2 |
| 5014 | Long Island-class | CVE | Escort | 2 | WWII | 1941 | 0 | 3000 | 12 | 4000000 | 12 | First escort carrier | First US escort carrier | Training/ASW CVE | +30% pilot training | AVG-1, training role |
| 5015 | Wasp-class | CV | Main Line | 3 | Interwar | 1940 | 0 | 10000 | 24 | 20000000 | 36 | Improved Ranger | Better protection than Ranger | Improved Treaty CV | +20% armor vs Ranger | CV-7, sunk 1942 |
| 5016 | Sangamon-class | CVE | Escort | 3 | WWII | 1942 | 0 | 4000 | 12 | 12000000 | 12 | Oiler conversion | Fast tanker conversions | Fast CVE | 18 kts vs 16 kts standard CVE | 4 ships, best CVEs |
| 5017 | Enterprise CV-6 | CV | Main Line | 4 | WWII | 1938 | 0 | 16000 | 30 | 20000000 | 36 | Most decorated | 20 battle stars, survived war | Legend | Lucky E: +15% evasion | UNIQUE, most decorated |
| 5018 | Casablanca-class | CVE | Escort | 4 | WWII | 1943 | 0 | 5000 | 18 | 5000000 | 6 | Mass production CVE | 50 built, Kaiser shipyards | Mass CVE | Rapid build: 6 months | Largest CV class ever |
| 5019 | Independence-class | CVL | Light Carrier | 4 | WWII | 1943 | 0 | 6000 | 18 | 15000000 | 12 | Cleveland conversion | 9 light carriers from CLs | Fast Light CV | 31.5 kts, rapid build | 9 ships, CL hulls |
| 5020 | Commencement Bay-class | CVE | Escort | 5 | WWII | 1944 | 0 | 6000 | 18 | 10000000 | 12 | Ultimate CVE | Purpose-built, best CVEs | Ultimate CVE | 19 kts, 34 aircraft | 19 built, Korean War |
| 5021 | Saipan-class | CVL | Light Carrier | 5 | Post-War | 1946 | 0 | 8000 | 24 | 30000000 | 18 | Purpose-built CVL | First purpose-built light carrier | Purpose CVL | 33 kts, 48 aircraft | 2 ships, cruise hulls |
| 5022 | Intrepid CV-11 | CV | Alternative | 5 | WWII | 1943 | 0 | 20000 | 36 | 68000000 | 20 | Famous Essex | Kamikaze survivor, museum ship | Tough Essex | Damage Control: +25% survival | UNIQUE, survived 5 kamikazes |
| 5023 | Essex-class (SCB-27C/125) | CV | Modernization | 6 | Jet Age | 1955 | 0 | 18000 | 24 | 0 | 0 | Full jet modernization | Steam cats + angled deck + jets | Full Jet CV | C-11 cats, full modernization | $50M, 30 months refit |
| 5024 | Midway-class (SCB-110) | CV | Main Line | 6 | Jet Age | 1957 | 0 | 12000 | 18 | 0 | 0 | Angled deck Midway | Angled deck, steam cats | Modernized Tank CV | Armored + jets | 12-year refit |
| 5025 | Thetis Bay CVL-H | CVH | Alternative | 6 | Cold War | 1956 | 0 | 3000 | 6 | 5000000 | 6 | Helo carrier | First US helicopter carrier | Helo CVE | 20 helicopters, USMC assault | Experiment, led to LPH |
| 5026 | Saratoga CV-60 | CV | Main Line | 7 | Supercarrier | 1956 | 0 | 35000 | 54 | 220000000 | 36 | Improved Forrestal | Improved electronics | Improved Supercarrier | Upgraded systems | Forrestal class |
| 5027 | John F. Kennedy CV-67 | CV | Main Line | 7 | Supercarrier | 1968 | 0 | 32000 | 48 | 277000000 | 42 | Modified Kitty Hawk | Smokestacks repositioned, unique | Unique CV | Last oil-fired, unique design | Modified Kitty Hawk |
| 5028 | Nimitz-class (Early) CVN-68/69 | CVN | Main Line | 8 | Nuclear | 1975 | 0 | 60000 | 84 | 1000000000 | 72 | Early production | First production nuclear carriers | Early Nuclear CV | 2× A4W reactors, 90 aircraft | CVN-68/69 |
| 5029 | Nimitz-class (Improved) CVN-70-72 | CVN | Main Line | 8 | Nuclear | 1981 | 0 | 55000 | 78 | 1100000000 | 72 | Improved systems | Better electronics, radar | Improved Nuclear CV | Upgraded systems | CVN-70/71/72 |
| 5030 | Nimitz-class (Late) CVN-73-76 | CVN | Main Line | 9 | Nuclear | 1995 | 0 | 50000 | 72 | 1200000000 | 72 | Late production | Full upgrades, best Nimitz | Ultimate Nimitz | All systems maxed | CVN-73/74/75/76 |
| 5031 | Enterprise CVN-80 | CVN | Main Line | 9 | Future | 2027 | 0 | 55000 | 78 | 1400000000 | 84 | Ford derivative | Third Enterprise, Ford tech | Future Ford | Ford systems, proven | Planned 2027 |
```

### Carrier Research Branches (NEW)

```markdown
| Branch_ID | Country | Ship_Type | Branch_Name | Branch_Description | Color | Start_Node | End_Node | Parent | Merge | Era_Start | Era_End | Notes |
|-----------|---------|-----------|-------------|-------------------|-------|------------|----------|--------|-------|-----------|---------|-------|
| 12 | USA | CVE | Escort Carrier | Merchant conversions and purpose-built escort carriers for ASW and convoy escort | #808080 | 5012 | 5020 | NULL | NULL | WWII | Cold War | Bogue → Long Island → Sangamon → Casablanca → Commencement Bay |
| 13 | USA | CVL | Light Carrier | Fast light carriers for scouting and support roles | #87CEEB | 5019 | 5021 | NULL | NULL | WWII | Post-War | Independence → Saipan. CL conversions + purpose-built |
| 14 | USA | CVH | Helicopter Carrier | Experimental helicopter assault carriers | #90EE90 | 5025 | 5025 | NULL | NULL | Cold War | Cold War | Thetis Bay standalone, led to LPH/LHA |
| 15 | USA | CV | Alternative CV | Famous individual carriers with unique careers | #FF69B4 | 5017 | 5022 | 10 | NULL | WWII | WWII | Enterprise CV-6, Intrepid CV-11. Stems from Main Line |
```

---

## USA Cruisers Research Tree (45 nodes, NEW)

### Node ID Allocation: 6000-6099

### Tier Distribution

| Tier | Count | Node IDs | Ship Classes |
|------|-------|----------|--------------|
| 1 | 2 | 6000-6001 | Chester, Omaha (both FREE) |
| 2 | 3 | 6002-6004 | Pensacola CA, Northampton CA, Brooklyn CL |
| 3 | 3 | 6005-6007 | Portland CA, Atlanta AA, St. Louis CL |
| 4 | 4 | 6008-6011 | New Orleans CA, Wichita CA, Cleveland CL, Oakland AA |
| 5 | 4 | 6012-6015 | Baltimore CA, Oregon City CA, Fargo CL, Juneau AA |
| 6 | 6 | 6016-6021 | Des Moines CA, Worcester CL, Boston CAG, Galveston CLG, Providence CLG, Norfolk DL |
| 7 | 7 | 6022-6028 | Albany CG, Long Beach CGN, Leahy CG, Bainbridge CGN, Belknap CG, Truxtun CGN, Chicago CAG |
| 8 | 5 | 6029-6033 | California CGN, Virginia CGN, Leahy NTU, Belknap NTU, Ticonderoga Early |
| 9 | 4 | 6034-6037 | Ticonderoga B1, Ticonderoga B2, Virginia Mod, Strike Cruiser (paper) |
| 10 | 3 | 6038-6040 | Ticonderoga B3 VLS, Ticonderoga B4, CG(X) (paper) |

### Research Branches

```markdown
| Branch_ID | Country | Ship_Type | Branch_Name | Notes |
|-----------|---------|-----------|-------------|-------|
| 16 | USA | CA | Heavy Cruiser Main Line | Pensacola → Des Moines (8" guns) |
| 17 | USA | CL | Light Cruiser Line | Brooklyn → Worcester (6" guns) |
| 18 | USA | CLAA | AA Cruiser Branch | Atlanta → Juneau (5" DP guns) |
| 19 | USA | CAG/CLG | Gun/Missile Conversion | Boston → Chicago (missile conversions) |
| 20 | USA | CG/CGN | Guided Missile Line | Long Beach → Ticonderoga (purpose-built) |
| 21 | USA | CG | Aegis Branch | Ticonderoga variants (Aegis system) |
```

---

## USA Destroyers Research Tree (42 nodes, NEW)

### Node ID Allocation: 7000-7099

### Tier Distribution

| Tier | Count | Node IDs | Ship Classes |
|------|-------|----------|--------------|
| 1 | 2 | 7000-7001 | Bainbridge, Smith (both FREE) |
| 2 | 3 | 7002-7004 | Paulding, Cassin, Sampson |
| 3 | 4 | 7005-7008 | Caldwell, Wickes, Clemson, Wickes APD |
| 4 | 5 | 7009-7013 | Farragut, Porter, Mahan, Gridley, Bagley |
| 5 | 5 | 7014-7018 | Benham, Sims, Benson, Gleaves, Bristol |
| 6 | 6 | 7019-7024 | Fletcher, Fletcher FRAM, Sumner, Gearing, Gearing FRAM, Gearing DDR |
| 7 | 6 | 7025-7030 | Forrest Sherman, Sherman DDG, Mitscher, Farragut/Coontz DDG, Adams DDG, Adams NTU |
| 8 | 5 | 7031-7035 | Spruance, Spruance VLS, Kidd, Burke Flight I, Burke Flight II |
| 9 | 3 | 7036-7038 | Burke Flight IIA, Burke Flight III, Zumwalt |
| 10 | 2 | 7039-7040 | Burke Flight IV (planned), DDG(X) (paper) |

### Research Branches

```markdown
| Branch_ID | Country | Ship_Type | Branch_Name | Notes |
|-----------|---------|-----------|-------------|-------|
| 22 | USA | DD | WWI Four-Stackers | Caldwell → Clemson (flush-deck DDs) |
| 23 | USA | DD | Interwar Development | Farragut → Bagley (enclosed guns) |
| 24 | USA | DD | WWII Main Line | Fletcher → Gearing (2,100-ton class) |
| 25 | USA | DDG | Guided Missile DD | Forrest Sherman DDG → Adams (missiles) |
| 26 | USA | DDG | Gas Turbine Era | Spruance → Kidd (modern propulsion) |
| 27 | USA | DDG | Aegis Destroyer | Burke variants (Aegis system) |
```

---

## USA Submarines Research Tree (38 nodes, NEW)

### Node ID Allocation: 8000-8099

### Tier Distribution

| Tier | Count | Node IDs | Ship Classes |
|------|-------|----------|--------------|
| 1 | 2 | 8000-8001 | Holland, A-class (both FREE) |
| 2 | 3 | 8002-8004 | C-class, F-class, H-class |
| 3 | 4 | 8005-8008 | L-class, O-class, R-class, S-class |
| 4 | 4 | 8009-8012 | V-class, Porpoise, Salmon, Sargo |
| 5 | 4 | 8013-8016 | Tambor, Gar, Mackerel, Barracuda SST |
| 6 | 5 | 8017-8021 | Gato, Balao, Tench, Balao GUPPY, Tench GUPPY IIA |
| 7 | 5 | 8022-8026 | Nautilus SSN, Seawolf SSN, Skate SSN, Washington SSBN, Ethan Allen SSBN |
| 8 | 5 | 8027-8031 | Skipjack SSN, Thresher/Permit SSN, Sturgeon SSN, Lafayette SSBN, Benjamin Franklin SSBN |
| 9 | 4 | 8032-8035 | Los Angeles Early SSN, Los Angeles 688i SSN, Ohio SSBN, Ohio SSGN |
| 10 | 3 | 8036-8038 | Seawolf SSN-21, Virginia SSN, Columbia SSBN (planned) |

### Research Branches

```markdown
| Branch_ID | Country | Ship_Type | Branch_Name | Notes |
|-----------|---------|-----------|-------------|-------|
| 28 | USA | SS | Diesel Submarine Main Line | Holland → Tench GUPPY (diesel-electric) |
| 29 | USA | SSN | Nuclear Attack Sub | Nautilus → Virginia (attack subs) |
| 30 | USA | SSBN/SSGN | Ballistic Missile Sub | George Washington → Columbia (strategic subs) |
| 31 | USA | SS | Training/Coastal | Mackerel, Barracuda SST (trainers) |
```

---

## Database Statistics

### Total USA Research Tree

| Metric | Count |
|--------|-------|
| **Total Research Nodes** | 204 |
| **Total Ship Types** | 5 (BB, CV, CA/CL/CG, DD/DDG, SS/SSN/SSBN) |
| **Total Research Branches** | 31 |
| **Estimated Prerequisites** | ~220 |
| **Estimated Unlocks** | ~220 |
| **Total Database Entries** | ~675 |

### Node ID Allocation Summary

| Range | Ship Type | Count | Status |
|-------|-----------|-------|--------|
| 1000-2999 | Battleships | 47 | Existing |
| 5000-5099 | Carriers | 32 | Expanded (12→32) |
| 6000-6099 | Cruisers | 45 | New |
| 7000-7099 | Destroyers | 42 | New |
| 8000-8099 | Submarines | 38 | New |

---

## Next Steps

1. ✅ Complete research and tree design (DONE)
2. ⏳ Update ship_research_tree_database.md with all new nodes
3. ⏳ Generate Prerequisites for all new ships
4. ⏳ Generate Unlocks for all new ships
5. ⏳ Add Research Branches for all new types
6. ⏳ Update database version and statistics

---

**Last Updated**: October 10, 2025
**Status**: Design Complete - Ready for Database Integration
**File**: USA_COMPLETE_RESEARCH_TREES_SUMMARY.md
