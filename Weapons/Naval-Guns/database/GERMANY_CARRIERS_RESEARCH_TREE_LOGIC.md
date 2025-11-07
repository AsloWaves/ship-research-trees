# German Aircraft Carriers Research Tree Logic

## Overview

This document defines the research tree structure for German Aircraft Carriers (CV) in the naval warfare system. This is a UNIQUE research tree as **Germany never successfully operated any aircraft carriers during WWII**. The famous Graf Zeppelin was 85% complete but never commissioned, and all German carrier development ended with the ship being scuttled in 1945. This tree represents what could have been rather than what was.

**Node ID Range**: 3100-3114 (15 nodes)
**Nation**: Germany
**Ship Type**: CV (Aircraft Carrier)
**Time Period**: 1918-1960
**Tech Tiers**: 3-10

## Historical Context

### WWI and Interwar Period (1918-1935)

After WWI, Germany was prohibited from building aircraft carriers by the Versailles Treaty. However, naval theorists studied carrier development, particularly Japanese designs, recognizing the strategic importance of naval aviation. The Anglo-German Naval Agreement (1935) lifted carrier restrictions, leading to Plan Z.

### Graf Zeppelin Era (1935-1945)

Grand Admiral Erich Raeder initiated carrier development as part of Plan Z rearmament. **Graf Zeppelin** was laid down December 28, 1936, and launched December 8, 1938. She reached **85% completion** but was never commissioned due to:
1. Strategic priority shifts during WWII
2. Hitler's suspension (April 1940) for Norwegian coastal defenses
3. Hitler's order (January 1943) to scrap large surface ships for U-boat resources
4. Final scuttling (April 25, 1945) to prevent Soviet capture

**Peter Strasser** (Flugzeugträger B) had construction halted September 1939 and was scrapped February 1940. Plan Z carriers C and D were planned but never started.

### The Reality

Germany never operated an aircraft carrier in combat. Graf Zeppelin's 85% completion represents the closest Germany came to carrier aviation. This research tree is largely theoretical, representing "what if" scenarios.

## Key Innovations (Theoretical)

1. **Dual-Purpose Design** (Graf Zeppelin): Carriers with heavy gun armament (16×15cm guns), unique concept combining carrier and cruiser roles
2. **Bf 109T Naval Fighters** (1939): Carrier-adapted version of Bf 109 with folding wings, arresting hook
3. **Ju 87C Stuka Dive Bomber** (1939): Carrier-adapted Stuka with folding wings, proven dive-bombing capability
4. **Armored Flight Deck Concept** (Plan Z): German interest in British armored deck design
5. **Plan Z Carrier Fleet** (1939): Ambitious plan for 4 carriers (never realized)

## Research Tree Structure

### Research Nodes Table

| Node_ID | Ship_Class | Tech_Tier | Year | Research_Cost_RP | Build_Cost | Build_Time_Days | Description | Special_Notes |
|---------|------------|-----------|------|------------------|------------|-----------------|-------------|---------------|
| 3100 | Conversion Study | 3 | 1918 | 8,000 | $1,000,000 | 36 | Early carrier concepts | Post-WWI carrier studies |
| 3101 | Japanese Study | 4 | 1928 | 12,000 | $1,500,000 | 42 | Japanese carrier analysis | Study of Akagi/Kaga designs |
| 3102 | Plan Z Concept | 5 | 1935 | 18,000 | $2,000,000 | 48 | Initial Plan Z carrier | Anglo-German Naval Agreement |
| 3103 | Graf Zeppelin | 8 | 1938 | 40,000 | $50,000,000 | 108 | Famous unfinished carrier | 85% complete, 42 aircraft |
| 3104 | Peter Strasser | 7 | 1939 | 35,000 | $45,000,000 | 96 | Second carrier | Construction halted, scrapped |
| 3105 | Flugzeugträger C | 8 | 1940 | 45,000 | $55,000,000 | 108 | Third Plan Z carrier | Never started |
| 3106 | Flugzeugträger D | 8 | 1940 | 45,000 | $55,000,000 | 108 | Fourth Plan Z carrier | Never started |
| 3107 | Europa Conversion | 7 | 1942 | 35,000 | $40,000,000 | 90 | Liner conversion concept | Theoretical conversion |
| 3108 | Improved Graf Zeppelin | 9 | 1943 | 55,000 | $65,000,000 | 120 | Enhanced design | Paper ship |
| 3109 | Armored Deck Carrier | 9 | 1944 | 60,000 | $70,000,000 | 120 | British-style armored deck | Paper ship |
| 3110 | Plan Z Super Carrier | 10 | 1945 | 75,000 | $90,000,000 | 150 | Ultimate WWII design | Paper ship |
| 3111 | Post-War Carrier | 10 | 1950 | 90,000 | $120,000,000 | 180 | Post-war concept | Theoretical |
| 3112 | Jet Age Carrier | 10 | 1955 | 110,000 | $150,000,000 | 210 | Jet aircraft capable | Theoretical |
| 3113 | Modern Carrier | 10 | 1960 | 130,000 | $200,000,000 | 240 | Modern systems | Theoretical |
| 3114 | Future CV Concept | 10 | 1970 | 180,000 | $300,000,000 | 300 | Advanced future | Future technology |

### Special Abilities

**Node-Specific Abilities**:

| Node_ID | Ship_Class | Special_Ability | Effect |
|---------|------------|----------------|--------|
| 3100 | Conversion Study | "Early Concepts" | First German carrier studies, +10% research speed |
| 3101 | Japanese Study | "Learning from Experts" | Japanese carrier expertise, +20% effectiveness |
| 3102 | Plan Z Concept | "Plan Z Initiative" | Ambitious naval program, +15% capability |
| 3103 | Graf Zeppelin | "85% Complete" | Famous unfinished carrier, +30% capability if completed |
| 3104 | Peter Strasser | "Halted Construction" | Early cancellation, -20% reliability (incomplete) |
| 3108 | Improved Graf Zeppelin | "Lessons Learned" | Incorporates Graf Zeppelin experience, +25% |
| 3109 | Armored Deck Carrier | "British Influence" | Armored flight deck, +40% survivability |
| 3110 | Plan Z Super Carrier | "Ultimate Design" | Maximum WWII carrier, +50% capability |

**National Special Abilities** (Apply to all German CV):
- "German Engineering": +15% reliability and mechanical efficiency
- "Dual-Purpose Design": Carriers have heavy gun armament (+20% surface combat)
- "Never Realized": -25% effectiveness (no operational experience, HISTORICAL PENALTY)

### Prerequisites Table

| Node_ID | Ship_Class | Prerequisite_Node_ID | Prerequisite_Ship_Class | Prerequisite_Type |
|---------|------------|---------------------|------------------------|-------------------|
| 3100 | Conversion Study | NULL | NULL | Starting |
| 3101 | Japanese Study | 3100 | Conversion Study | Required |
| 3102 | Plan Z Concept | 3101 | Japanese Study | Required |
| 3103 | Graf Zeppelin | 3102 | Plan Z Concept | Required |
| 3104 | Peter Strasser | 3103 | Graf Zeppelin | Required |
| 3105 | Flugzeugträger C | 3103 | Graf Zeppelin | Required |
| 3106 | Flugzeugträger D | 3105 | Flugzeugträger C | Required |
| 3107 | Europa Conversion | 3103 | Graf Zeppelin | Required |
| 3108 | Improved Graf Zeppelin | 3103, 3104 | Graf Zeppelin, Peter Strasser | Required (AND) |
| 3109 | Armored Deck Carrier | 3108 | Improved Graf Zeppelin | Required |
| 3110 | Plan Z Super Carrier | 3108, 3109 | Improved Graf Zeppelin, Armored Deck | Required (AND) |
| 3111 | Post-War Carrier | 3110 | Plan Z Super Carrier | Required |
| 3112 | Jet Age Carrier | 3111 | Post-War Carrier | Required |
| 3113 | Modern Carrier | 3112 | Jet Age Carrier | Required |
| 3114 | Future CV Concept | 3113 | Modern Carrier | Required |

### Unlocks Table

| Node_ID | Ship_Class | Unlocks_Node_ID | Unlocks_Ship_Class | Unlock_Type |
|---------|------------|----------------|-------------------|-------------|
| 3100 | Conversion Study | 3101 | Japanese Study | Research |
| 3101 | Japanese Study | 3102 | Plan Z Concept | Research |
| 3102 | Plan Z Concept | 3103 | Graf Zeppelin | Research |
| 3103 | Graf Zeppelin | 3104, 3105, 3107 | Multiple | Research |
| 3104 | Peter Strasser | 3108 | Improved Graf Zeppelin | Research |
| 3105 | Flugzeugträger C | 3106 | Flugzeugträger D | Research |
| 3108 | Improved Graf Zeppelin | 3109, 3110 | Multiple | Research |
| 3109 | Armored Deck Carrier | 3110 | Plan Z Super Carrier | Research |
| 3110 | Plan Z Super Carrier | 3111 | Post-War Carrier | Research |
| 3111 | Post-War Carrier | 3112 | Jet Age Carrier | Research |
| 3112 | Jet Age Carrier | 3113 | Modern Carrier | Research |
| 3113 | Modern Carrier | 3114 | Future CV Concept | Research |

### Research Branches Table

| Branch_ID | Branch_Name | Description | Starting_Node_ID | Tech_Tier_Range |
|-----------|-------------|-------------|------------------|-----------------|
| DE_CV_01 | Early Studies | Post-WWI carrier concepts and foreign studies | 3100-3102 | 3-5 |
| DE_CV_02 | Graf Zeppelin Class | Historical Graf Zeppelin-class carriers | 3103-3104 | 7-8 |
| DE_CV_03 | Plan Z Expansion | Additional Plan Z carriers | 3105-3107 | 7-8 |
| DE_CV_04 | Paper Ships | Theoretical improved designs | 3108-3110 | 9-10 |
| DE_CV_05 | Future Concepts | Post-war and modern theoretical carriers | 3111-3114 | 10 |

## Branch Descriptions

### 1. Early Studies (3 nodes)
**Conversion Study (1918)**: Post-WWI theoretical work on carrier development despite Versailles Treaty restrictions. German naval theorists studied carrier concepts, recognizing their strategic importance but unable to build due to treaty limitations.

**Japanese Study (1928)**: Comprehensive analysis of Japanese carrier designs, particularly Akagi and Kaga. Germany maintained secret naval ties and studied successful carrier programs. This research informed later Plan Z designs (+20% effectiveness from expert knowledge).

**Plan Z Concept (1935)**: After the Anglo-German Naval Agreement lifted carrier restrictions, Grand Admiral Raeder initiated carrier development as part of the ambitious Plan Z naval expansion program. This laid the foundation for Graf Zeppelin construction.

### 2. Graf Zeppelin Class (2 nodes)
**Graf Zeppelin (1938)**: The famous unfinished German aircraft carrier. Specifications:
- Displacement: 33,550 tons full load
- Dimensions: 262.5 x 36.2 x 8.5 m
- Aircraft: 42 total (12 Bf 109T fighters, 30 Ju 87C Stuka dive bombers)
- Unique Feature: Heavy gun armament (16×15cm guns) - dual carrier/cruiser role
- Status: 85% complete but never commissioned
- Timeline: Keel laid Dec 28, 1936 → Launched Dec 8, 1938 → Suspended April 1940 → Scuttled April 25, 1945

**Peter Strasser (1939)**: Second Graf Zeppelin-class carrier (Flugzeugträger B). Construction began 1938 but halted September 19, 1939 due to U-boat priority. Hull only completed to armored deck level. Scrapped February 28, 1940. Named after WWI naval airship commander Peter Strasser.

### 3. Plan Z Expansion (3 nodes)
**Flugzeugträger C (1940)**: Third carrier planned under Plan Z. Never started construction due to WWII outbreak and strategic priority shifts. Would have been improved Graf Zeppelin design incorporating lessons learned.

**Flugzeugträger D (1940)**: Fourth Plan Z carrier. Never started. Plan Z envisioned a carrier fleet of 4 ships to support surface fleet operations in Atlantic and North Sea. All Plan Z carrier development ended with Peter Strasser's scrapping.

**Europa Conversion (1942)**: Theoretical conversion of passenger liner Europa into auxiliary carrier. Studied but never pursued. Germany lacked operational carrier experience to guide effective conversions, unlike Britain's successful merchant conversions.

### 4. Paper Ships (3 nodes)
**Improved Graf Zeppelin (1943)**: Enhanced design incorporating theoretical lessons from Graf Zeppelin construction and Allied carrier operations. Would have featured improved aircraft handling, enhanced AA armament, and better damage control. Never built (-20% reliability, paper ship penalty).

**Armored Deck Carrier (1944)**: Theoretical carrier incorporating British armored flight deck concept. Would have traded aircraft capacity for survivability (+40% survivability). Influenced by intelligence on HMS Illustrious-class performance. Never built.

**Plan Z Super Carrier (1945)**: Ultimate WWII German carrier design. Theoretical specifications: 45,000+ tons, 60+ aircraft, heavy armament, armored deck. Represents maximum development of German carrier doctrine. Never built (-25% reliability, pure speculation).

### 5. Future Concepts (4 nodes)
**Post-War Carrier (1950)**: Theoretical post-war carrier design incorporating jet aircraft capability and lessons from Pacific War. Pure speculation as West Germany was prohibited from carriers and East Germany had no carrier program.

**Jet Age Carrier (1955)**: Advanced jet-capable carrier with angled flight deck, steam catapults, and modern systems. Theoretical German development if carrier program had continued.

**Modern Carrier (1960)**: Modern systems integration, advanced electronics, guided missiles. Pure speculation—unified Germany eventually had no carrier program.

**Future CV Concept (1970)**: Advanced future carrier technology. Theoretical only—Germany focused on land forces and submarines in Cold War.

## Gameplay Notes

### Balance Considerations

1. **Historical Penalty**: German carriers suffer -25% effectiveness due to never being operational (REALISTIC)
2. **85% Complete**: Graf Zeppelin gets +30% capability bonus IF completed (represents advanced construction)
3. **No Experience Bonus**: Unlike USA/Britain/Japan, Germany has no carrier combat experience bonuses
4. **Paper Ship Heavy**: 10 of 15 nodes are paper ships/theoretical (reflects historical reality)
5. **Cost Scaling**: Very expensive due to lack of expertise (Graf Zeppelin: $50M vs. other nations' equivalents)
6. **Research Costs**: Higher research costs reflect lack of operational data

### German Carrier Characteristics

**Unique Features**:
- Dual-purpose design with heavy gun armament (16×15cm guns, +20% surface combat)
- German aircraft (Bf 109T, Ju 87C) optimized for dive-bombing and fighter roles
- German engineering standards (+15% mechanical reliability)
- Studied Japanese designs (+20% from expert knowledge)

**Critical Weaknesses**:
- **Never Operational**: -25% effectiveness (historical penalty)
- **No Combat Experience**: No carrier doctrine development
- **Incomplete Development**: 85% complete = never tested systems
- **Lack of Expertise**: No operational carrier navy to draw upon
- **Strategic Abandonment**: Hitler prioritized U-boats over carriers (historical fact)

### Strategic Role (Theoretical)

If Germany had operated carriers, their role would have been:
1. **Atlantic Operations**: Supporting surface raiders and U-boat wolf packs
2. **North Sea Control**: Challenging Royal Navy in confined waters
3. **Norway Operations**: Air cover for Norwegian coastal operations
4. **Convoy Interdiction**: Attacking Allied Arctic convoys
5. **Baltic Sea**: Dominance in Baltic operations against Soviet Navy

### Reality Check

**Historical Facts**:
- Germany NEVER operated an aircraft carrier in combat
- Graf Zeppelin reached 85% completion but was never commissioned
- All carrier development ended with scuttling of Graf Zeppelin (April 1945)
- Germany had no carrier pilots, no carrier doctrine, no carrier experience
- Post-war Germany had no carrier program (focused on U-boats and land forces)

**This research tree represents "alternate history" more than reality.**

## Historical Ship Counts

**WWI**: 0 carriers (none planned or built)

**WWII**: 0 carriers commissioned
- Graf Zeppelin: 85% complete, never commissioned, scuttled 1945
- Peter Strasser: Early construction, scrapped 1940
- Flugzeugträger C: Planned, never started
- Flugzeugträger D: Planned, never started

**Post-War**: 0 carriers (West/East Germany and unified Germany had no carrier programs)

**Total Achievements**:
- Carriers operated: 0
- Combat missions: 0
- Ships sunk: 0
- Aircraft launched: 0

**The German carrier program represents one of WWII's great "what ifs" but resulted in zero operational carriers.**

---

*Document Version: 1.0*
*Last Updated: 2025-10-11*
*Status: Complete - Ready for database implementation*
*Note: This tree is largely theoretical/alternate history due to Germany never operating carriers*
