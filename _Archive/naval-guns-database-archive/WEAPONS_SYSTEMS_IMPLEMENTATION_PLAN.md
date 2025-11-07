# Weapons Systems Implementation Plan
**Created**: October 11, 2025
**Scope**: Torpedoes, Missiles, Naval Aircraft, Ground Aircraft
**Nations**: USA, British, German, Japanese (+ Soviet/Russian for modern systems)

---

## Executive Summary

**Total Scope**: 2,000-3,100 entries across 4 weapon systems
**Approach**: Research trees + detailed specifications (mirroring ship implementation)
**Estimated Completion**: Phased approach over multiple sessions
**Complexity**: High - requires historical research, technical specifications, game balance

### Database Status Overview

| Database | Current | Target | Tables | Fields | ID Range | Era Coverage |
|----------|---------|--------|--------|--------|----------|--------------|
| **Torpedoes** | 0 | 300-500 | 3 | 18 | 1000-1399 | 1890-1990 |
| **Missiles** | 0 | 400-600 | 4 | 22 | 2000-2999 | 1950-2025 |
| **Naval Aircraft** | 0 | 500-800 | 4 | 32 | 3000-3999 | 1910-2025 |
| **Ground Aircraft** | 0 | 800-1,200 | 4 | 33 | 4000-5499 | 1914-2025 |
| **TOTAL** | **0** | **2,000-3,100** | **15** | - | - | **1890-2025** |

---

## Implementation Strategy

### Proven Pattern (from Ship Implementation)
1. ✅ **Research Tree First** → Create tier-based progression with prerequisites
2. ✅ **Basic Entries** → Convert research tree to database with essential fields
3. ⏳ **Detailed Expansion** → Add full specifications later

### Rationale
- Research trees establish game progression logic (tiers, costs, unlock paths)
- Basic database entries provide immediate gameplay functionality
- Detailed specifications can be added incrementally
- Allows parallel work (research trees for multiple systems)

---

## Phase 1: Torpedoes (Priority: HIGH)

**Complexity**: ⭐⭐⚪⚪⚪ (Simplest)
**Entries**: 300-500 torpedoes
**Timeline**: 2-3 sessions

### Why Start Here?
- **Smallest scope** (300-500 entries vs 800-1,200 for ground aircraft)
- **Clear progression**: Steam → Electric → Acoustic → Wire-guided
- **Well-documented history**: Excellent sources for WWII torpedoes
- **Existing examples**: Database already lists key torpedoes per nation

### Research Tree Structure

**USA Torpedoes** (50-70 nodes):
- **Tier 1-3**: Early steam torpedoes (1890-1915)
  - Whitehead patterns, Howell torpedo, Bliss-Leavitt
- **Tier 4-6**: WWI-Interwar (1915-1940)
  - Mark 8, Mark 10, Mark 11, Mark 13 (air), Mark 14 development
- **Tier 7-9**: WWII (1940-1945)
  - Mark 14 (with detonator fixes), Mark 15, Mark 13 (improved), Mark 18 electric
- **Tier 10**: Post-WWII/Modern (1945-1990)
  - Mark 37, Mark 45 ASTOR, Mark 46, Mark 48

**British Torpedoes** (45-65 nodes):
- **Tier 1-3**: Early development (1890-1915)
  - Whitehead originals, 18" Mark I-VIII
- **Tier 4-6**: WWI-Interwar (1915-1940)
  - 21" Mark II, Mark IV, Mark VIII
- **Tier 7-9**: WWII (1940-1945)
  - Mark VIII**, Mark IX, Mark X, Mark XII, Mark XV
- **Tier 10**: Modern (1945-1990)
  - Mark 20, Mark 23, Mark 24 Tigerfish, Spearfish

**German Torpedoes** (45-60 nodes):
- **Tier 1-3**: Early development (1890-1915)
  - Schwarzkopf patterns, early C-types
- **Tier 4-6**: WWI-Interwar (1915-1940)
  - G7 development, H8, C/06, C/12
- **Tier 7-9**: WWII (1940-1945)
  - **G7a (TI)** steam, **G7e (TII)** electric, **G7es (TIII)** pattern-running
  - **T5 Zaunkönig** acoustic homing, **T11** advanced acoustic
- **Tier 10**: Post-WWII (1945-1960)
  - Early Bundesmarine torpedoes

**Japanese Torpedoes** (50-70 nodes):
- **Tier 1-3**: Early development (1890-1915)
  - Licensed Whitehead, Type 4, Type 6
- **Tier 4-6**: Interwar innovation (1915-1935)
  - Type 8, Type 90, **Oxygen torpedo development**
- **Tier 7-9**: WWII dominance (1935-1945)
  - **Type 93 "Long Lance"** (24" oxygen, 49-51 kts, 40,000 yd range) - LEGENDARY
  - **Type 95** submarine torpedo (oxygen)
  - **Type 91** air-launched (Pearl Harbor torpedo)
  - **Type 97** destroyer torpedo
- **Tier 10**: Limited post-war (1945-1960)
  - JMSDF modern torpedoes

**Total Torpedo Research Nodes**: ~190-265 nodes

### Database Fields Priority
- ✅ **Essential** (auto-populate from research tree):
  - Torpedo_ID, Country, Designation, Type, Year_Introduced, Diameter, Length, Weight, Warhead_LBS, Max_Speed, Max_Range, Propulsion, Guidance, Launch_Platform, Modded, Notes

- 🔲 **Detailed** (future expansion):
  - Warheads table, Launch Systems table, exact running depth, turn radius

---

## Phase 2: Missiles (Priority: HIGH)

**Complexity**: ⭐⭐⭐⭐⚪ (Complex)
**Entries**: 400-600 missiles
**Timeline**: 4-5 sessions

### Why Second?
- **Cold War focus** (1950-2025) - narrower time range than aircraft
- **Clear categories**: SAM, SSM, ASW, Cruise
- **Well-documented**: Modern weapons with abundant technical data
- **Strategic importance**: Critical for modern naval warfare gameplay

### Research Tree Structure

**USA Missiles** (100-120 nodes):
- **Tier 1-2**: Early SAM (1950-1960)
  - RIM-2 Terrier, RIM-8 Talos, RIM-24 Tartar ("3T" family)
- **Tier 3-5**: First generation SSM (1955-1970)
  - RGM-6 Regulus, RGM-15 Regulus II, RGM-84 Harpoon (early)
- **Tier 6-8**: Modern SAM/SSM (1970-1990)
  - RIM-66 Standard SM-1/SM-2, RIM-67 Standard ER
  - BGM-109 Tomahawk, RUR-5 ASROC
- **Tier 9-10**: Advanced systems (1990-2025)
  - RIM-161 SM-3 (ballistic missile defense), RIM-162 ESSM
  - RIM-174 SM-6, AGM-158C LRASM

**British Missiles** (30-40 nodes):
- **Tier 1-3**: Early systems (1955-1975)
  - Sea Slug, Sea Cat, Sea Dart
- **Tier 4-7**: Modern era (1975-2010)
  - Sea Wolf, Sea Skua, Exocet MM.38 (licensed)
- **Tier 8-10**: Current generation (2000+)
  - Sea Viper (Aster 15/30), Sea Ceptor

**German Missiles** (20-30 nodes):
- Post-WWII focus, primarily NATO systems
- Exocet, Harpoon (licensed), RAM, IRIS-T SL

**Japanese Missiles** (25-35 nodes):
- **Tier 3-6**: Indigenous development (1970-2000)
  - Type 80/90 SAMs, Type 88/90 SSMs
- **Tier 7-10**: Modern systems (2000+)
  - Type 03/07/12, advanced SAMs

**Soviet/Russian Missiles** (80-100 nodes) - **Critical Addition**:
- **Tier 1-3**: First generation (1955-1970)
  - P-15 Termit (SS-N-2 Styx), S-75 Dvina (SA-2)
- **Tier 4-7**: Cold War advancement (1970-1990)
  - P-270 Moskit (SS-N-22 Sunburn), P-500 Bazalt (SS-N-12)
  - P-700 Granit (SS-N-19 Shipwreck)
  - S-300F Fort (SA-N-6)
- **Tier 8-10**: Modern/hypersonic (1990-2025)
  - P-800 Oniks (SS-N-26), 3M-54 Kalibr (SS-N-27)
  - 3M22 Zircon (hypersonic), 9M96 (SA-N-21)

**Total Missile Research Nodes**: ~255-325 nodes

### Database Fields Priority
- ✅ **Essential**:
  - Missile_ID, Country, Designation, NATO_Codename, Type, Role, Year_Introduced, Diameter, Length, Weight, Warhead_LBS, Max_Speed_MACH, Max_Range_NM, Propulsion, Guidance, Launch_Platform, Modded, Notes

- 🔲 **Detailed**:
  - Warheads, Launch Systems, Targeting Systems tables

---

## Phase 3: Naval Aircraft (Priority: MEDIUM)

**Complexity**: ⭐⭐⭐⭐⚪ (Complex)
**Entries**: 500-800 aircraft
**Timeline**: 5-6 sessions

### Why Third?
- **Large scope** but narrower focus (carrier-based only)
- **Clear progression**: Biplane → Monoplane → Jet → Supersonic → Stealth
- **Rich history**: WWII carrier battles, modern supercarrier operations
- **Cross-database integration**: Aircraft use torpedoes, missiles

### Research Tree Structure

**USA Naval Aircraft** (120-150 nodes):
- **Tier 1-2**: Early carrier aviation (1920-1935)
  - F2F, F3F, TBD Devastator, F2A Buffalo
- **Tier 3-5**: WWII dominance (1935-1945)
  - **F4F Wildcat, F6F Hellcat, F4U Corsair** (fighters)
  - **SBD Dauntless, SB2C Helldiver** (dive bombers)
  - **TBF/TBM Avenger** (torpedo bombers)
- **Tier 6-8**: Jet transition/Korea/Vietnam (1945-1975)
  - F9F Panther/Cougar, F2H Banshee, F7U Cutlass
  - **F-8 Crusader, F-4 Phantom II, F-14 Tomcat**
  - **A-4 Skyhawk, A-6 Intruder, A-7 Corsair II**
- **Tier 9-10**: Modern supercarrier era (1975-2025)
  - **F/A-18 Hornet C/D, F/A-18E/F Super Hornet**
  - **EA-18G Growler, F-35C Lightning II**
  - E-2 Hawkeye, S-3 Viking, MH-60 Seahawk

**British Naval Aircraft** (60-80 nodes):
- **Tier 1-3**: WWI/Interwar (1915-1939)
  - Sopwith Pup (shipboard), Fairey Flycatcher
- **Tier 4-6**: WWII (1939-1945)
  - **Fairey Swordfish** (sank Bismarck), Fairey Fulmar
  - **Supermarine Seafire** (navalised Spitfire), Fairey Firefly
  - **Sea Fury** (last piston fighter)
- **Tier 7-9**: Jet era (1945-1990)
  - Sea Hawk, Sea Venom, Sea Vixen, **Buccaneer**
  - **Sea Harrier** FA.1/FA.2 (Falklands War hero)
- **Tier 10**: Modern (1990+)
  - **F-35B Lightning II** (STOVL for Queen Elizabeth-class)

**Japanese Naval Aircraft** (70-90 nodes):
- **Tier 1-3**: Early development (1920-1935)
  - A2N, A4N, B4Y
- **Tier 4-7**: WWII naval aviation peak (1935-1945)
  - **A6M Zero** - most produced Japanese aircraft, legendary agility
  - **D3A Val** - dive bomber (Pearl Harbor, Midway)
  - **B5N Kate** - torpedo bomber (Pearl Harbor primary weapon)
  - **D4Y Judy** - fast reconnaissance/dive bomber
  - **B6N Jill** - late-war torpedo bomber
  - **A7M Reppū** - Zero successor (limited production)
- **Tier 8-10**: Post-war JMSDF (1960-2025)
  - P-1 maritime patrol, SH-60J/K helicopters
  - Limited carrier aviation (helicopter carriers only)

**German Naval Aircraft** (15-25 nodes):
- **Tier 3-5**: Graf Zeppelin aircraft (never operational)
  - **Bf 109T** (carrier variant)
  - **Ju 87C** (carrier Stuka)
  - Fi 167 torpedo bomber
- **Tier 6-10**: Post-WWII limited (helicopters, patrol aircraft)

**Total Naval Aircraft Research Nodes**: ~265-345 nodes

### Database Fields Priority
- ✅ **Essential**:
  - Aircraft_ID, Country, Designation, Nickname, Manufacturer, Type, Role, Year_Introduced, Crew, Length, Wingspan, Empty_Weight, Max_Takeoff_Weight, Engine_Type, Max_Speed, Range, Combat_Radius, Carrier_Capable, Folding_Wings, Modded, Notes

- 🔲 **Detailed**:
  - Armament, Performance, Carrier Compatibility tables

---

## Phase 4: Ground Aircraft (Priority: MEDIUM-LOW)

**Complexity**: ⭐⭐⭐⭐⭐ (Most Complex)
**Entries**: 800-1,200 aircraft
**Timeline**: 8-10 sessions

### Why Last?
- **Largest scope** (800-1,200 entries)
- **Most categories**: Fighters, bombers, attack, interceptors, CAS, etc.
- **111 years of aviation history** (1914-2025)
- **Complex generation system**: 1st gen through 5th+ gen jets
- **Can leverage patterns** from naval aircraft implementation

### Research Tree Structure

**USA Ground Aircraft** (200-280 nodes):
- **Tier 1**: WWI (1917-1918)
  - SPAD XIII, Sopwith Camel (US-built), DH-4
- **Tier 2-4**: Interwar/Pre-WWII (1919-1941)
  - P-26 Peashooter, P-36 Hawk, P-40 Warhawk
- **Tier 5-6**: WWII (1941-1945)
  - **P-51 Mustang, P-47 Thunderbolt, P-38 Lightning**
  - **B-17 Flying Fortress, B-24 Liberator, B-29 Superfortress**
  - P-39 Airacobra, P-61 Black Widow
- **Tier 7-8**: Early jets/Korea (1945-1960)
  - **F-86 Sabre, F-84 Thunderjet, F-80 Shooting Star**
  - **F-100 Super Sabre** (first supersonic), F-101 Voodoo
  - **B-47 Stratojet, B-52 Stratofortress**
- **Tier 9**: Vietnam/Cold War (1960-1990)
  - **F-4 Phantom II, F-105 Thunderchief**
  - **F-15 Eagle** (undefeated), **F-16 Fighting Falcon**
  - **F-111 Aardvark, A-10 Thunderbolt II**
  - B-1B Lancer
- **Tier 10**: Modern/5th gen (1990+)
  - **F-22 Raptor** (air superiority), **F-35A Lightning II** (multi-role)
  - F-15EX Eagle II, **B-2 Spirit** (stealth bomber)
  - A-10C (upgraded)

**British Ground Aircraft** (110-140 nodes):
- **Tier 1**: WWI (1914-1918)
  - **Sopwith Camel** (most successful WWI fighter)
  - SE.5a, Bristol F.2 Fighter, Sopwith Pup
- **Tier 2-4**: Interwar (1919-1939)
  - Gloster Gladiator, Bristol Bulldog, Hawker Fury
- **Tier 5-6**: WWII (1939-1945)
  - **Supermarine Spitfire** (iconic), **Hawker Hurricane**
  - **Avro Lancaster** (heavy bomber), **De Havilland Mosquito**
  - Hawker Typhoon, Hawker Tempest
- **Tier 7-8**: Jet era (1945-1980)
  - **Gloster Meteor** (first Allied jet), Hawker Hunter
  - **English Electric Lightning** (supersonic), Harrier GR.3
  - Tornado GR.1/GR.4
- **Tier 9-10**: Modern (1980+)
  - Harrier GR.7/GR.9, **Typhoon FGR.4** (Eurofighter)
  - F-35B (STOVL)

**German Ground Aircraft** (100-130 nodes):
- **Tier 1**: WWI (1914-1918)
  - **Fokker Dr.I** (Red Baron's triplane), **Fokker D.VII** (best WWI fighter)
  - Albatros D.V, Pfalz D.III
- **Tier 2-4**: Interwar/Pre-WWII (1933-1939)
  - Bf 109A-E (early variants), He 51
- **Tier 5-6**: WWII dominance (1939-1945)
  - **Bf 109** (most-produced fighter ever, 34,000 built)
  - **Fw 190** (excellent fighter-bomber)
  - **Me 262** (first operational jet fighter)
  - He 111, Ju 87 Stuka, Ju 88
  - Me 163 Komet (rocket interceptor), Me 410
- **Tier 7-10**: Post-war/Modern (1955+)
  - F-4F Phantom II (Luftwaffe), Tornado IDS/ECR
  - **Typhoon** (Eurofighter, German participation)

**Soviet/Russian Ground Aircraft** (150-200 nodes):
- **Tier 2-4**: Interwar/Pre-WWII (1930-1941)
  - I-15, I-16, LaGG-3
- **Tier 5-6**: WWII (1941-1945)
  - **Yak-3, Yak-9** (agile fighters)
  - **La-5, La-7** (radial-engine fighters)
  - **Il-2 Shturmovik** (most-produced military aircraft ever, 36,000+)
  - Pe-2, Tu-2
- **Tier 7-8**: Jet era/Korea/Vietnam (1945-1980)
  - **MiG-15** (Korean War jet)
  - **MiG-17, MiG-19, MiG-21 Fishbed** (most-produced supersonic)
  - **MiG-23 Flogger, MiG-25 Foxbat** (Mach 3)
  - Su-7/Su-17 Fitter, **Su-24 Fencer**
  - **Su-25 Frogfoot** (CAS)
- **Tier 9-10**: Modern (1980+)
  - **MiG-29 Fulcrum, MiG-31 Foxhound**
  - **Su-27 Flanker** (highly maneuverable)
  - **Su-30, Su-35** (advanced Flanker variants)
  - Su-34 Fullback, **Su-57 Felon** (5th gen)

**Japanese Ground Aircraft** (70-90 nodes):
- **Tier 4-6**: WWII Army Air Force (1935-1945)
  - **Ki-43 Oscar, Ki-61 Tony, Ki-84 Frank**
  - **Ki-100** (radial variant), J2M Raiden (Jack), N1K Shiden (George)
  - G4M Betty, Ki-21 Sally
- **Tier 7-10**: JASDF modern (1955+)
  - F-4EJ Phantom II, F-15J Eagle (license-built)
  - F-2 (indigenous), F-35A

**Total Ground Aircraft Research Nodes**: ~630-840 nodes

### Database Fields Priority
- ✅ **Essential**:
  - Aircraft_ID, Country, Designation, Nickname, Manufacturer, Type, Role, Generation, Year_Introduced, Crew, Length, Wingspan, Empty_Weight, Max_Takeoff_Weight, Engine_Type, Max_Speed, Range, Combat_Radius, Stealth_Capable, Supercruise_Capable, Modded, Notes

- 🔲 **Detailed**:
  - Armament, Performance, Base Operations tables

---

## Total Research Tree Nodes Estimate

| System | USA | British | German | Japanese | Soviet/Russian | Others | **Total** |
|--------|-----|---------|--------|----------|----------------|--------|-----------|
| **Torpedoes** | 50-70 | 45-65 | 45-60 | 50-70 | - | - | **190-265** |
| **Missiles** | 100-120 | 30-40 | 20-30 | 25-35 | 80-100 | - | **255-325** |
| **Naval Aircraft** | 120-150 | 60-80 | 15-25 | 70-90 | - | - | **265-345** |
| **Ground Aircraft** | 200-280 | 110-140 | 100-130 | 70-90 | 150-200 | - | **630-840** |
| **TOTALS** | **470-620** | **245-325** | **180-245** | **215-285** | **230-300** | - | **1,340-1,775** |

**Grand Total Research Nodes**: 1,340-1,775 nodes (comparable to ships: 1,163 nodes)

---

## Implementation Workflow (Per System)

### Step 1: Research & Planning (1-2 hours)
- Historical research using Context7 MCP
- Identify iconic/essential weapons per nation
- Establish tier progression and prerequisites
- Define research costs and unlock requirements

### Step 2: Research Tree Creation (2-4 hours per nation)
- Create `[NATION]_[SYSTEM]_RESEARCH_TREE_LOGIC.md` files
- Define node structure: Node_ID, Country, Designation, Tier, Year, Cost, Time, Design, Notes
- Establish prerequisite chains
- Balance gameplay progression

### Step 3: Database Insertion (1-2 hours per nation)
- Use sed insertion method (proven from ship implementation)
- Create temp files with research tree nodes
- Insert into research tree database
- Verify insertion and node counts

### Step 4: Database Conversion (2-3 hours per system)
- Create AWK conversion scripts (adapt from ship script)
- Extract essential fields from research tree
- Apply estimation algorithms for missing technical specs
- Generate basic database entries

### Step 5: Database Population (1-2 hours)
- Insert converted entries into main database
- Update database status and statistics
- Verify entry counts and data integrity

### Step 6: Validation & Documentation (1 hour)
- Verify all research trees complete
- Check database entry counts
- Document completion status
- Create summary reports

**Total Time Estimate Per System**:
- Torpedoes: 15-20 hours
- Missiles: 20-25 hours
- Naval Aircraft: 25-30 hours
- Ground Aircraft: 40-50 hours
- **TOTAL**: 100-125 hours of implementation

---

## Recommended Implementation Order

### Option A: Sequential (Proven Approach)
1. ✅ **Phase 1**: Torpedoes (complete all 4 nations) → 2-3 sessions
2. ✅ **Phase 2**: Missiles (complete all nations) → 4-5 sessions
3. ✅ **Phase 3**: Naval Aircraft (complete all nations) → 5-6 sessions
4. ✅ **Phase 4**: Ground Aircraft (complete all nations) → 8-10 sessions

**Pros**: Clean phase boundaries, can validate each system fully before moving on
**Cons**: Longer before seeing complete picture

### Option B: Parallel by Nation (Alternative)
1. **USA Complete**: All systems for USA (torpedoes, missiles, aircraft)
2. **British Complete**: All systems for British
3. **German Complete**: All systems for German
4. **Japanese Complete**: All systems for Japanese

**Pros**: Complete arsenal per nation, easier to balance per nation
**Cons**: More context switching, harder to establish consistent patterns

### Option C: Hybrid (Recommended)
1. **Torpedoes**: All 4 nations (establish patterns)
2. **USA Complete**: Missiles + Aircraft (largest arsenal, establish standards)
3. **Other Nations**: Mirror USA patterns for missiles + aircraft
4. **Balance Pass**: Fine-tune all systems

**Pros**: Combines benefits of both approaches
**Cons**: Requires discipline to maintain consistency

---

## Recommended Start: Phase 1 - Torpedoes (USA)

**Next Immediate Actions**:
1. ✅ Research USA torpedo history (1890-1990)
2. ✅ Create USA_TORPEDOES_RESEARCH_TREE_LOGIC.md
3. ✅ Define 50-70 torpedo nodes with tiers, costs, prerequisites
4. ✅ Insert into research tree database
5. ✅ Create conversion script for torpedo database population

**Why Start with USA Torpedoes?**
- Most documented (Mark 14, Mark 48 extensively studied)
- Clear progression (steam → electric → acoustic → wire-guided)
- Moderate complexity (not simplest, not hardest)
- Establishes pattern for other nations

---

## Success Criteria

### Research Trees
- ✅ All nodes have unique IDs within allocated range
- ✅ Prerequisites form valid progression (no circular dependencies)
- ✅ Costs and build times balanced by tier
- ✅ Historical accuracy with sources cited
- ✅ Game balance considerations documented

### Databases
- ✅ All essential fields populated
- ✅ Node ID matches research tree for traceability
- ✅ Technical specifications within historical ranges
- ✅ Entry counts meet targets (80-100% of planned)
- ✅ Database status updated with accurate statistics

### Documentation
- ✅ Each research tree has narrative descriptions
- ✅ Legendary/iconic weapons highlighted
- ✅ Historical context provided
- ✅ Cross-references to related databases
- ✅ Summary statistics accurate

---

## Risk Mitigation

### Historical Accuracy Risks
- **Risk**: Insufficient documentation for obscure weapons
- **Mitigation**: Use Context7 MCP for research, cite sources, mark uncertain data

### Scope Creep Risks
- **Risk**: Attempting too many detailed specifications
- **Mitigation**: Use proven "basic entries first" approach from ships

### Balance Risks
- **Risk**: Over-powered or under-powered weapons
- **Mitigation**: Tier-based progression, cost balancing, playtesting notes

### Technical Risks
- **Risk**: Database corruption or insertion errors
- **Mitigation**: Use proven sed method, verify after each insertion, backup files

---

## Tools & Automation

### Proven Scripts (from Ship Implementation)
- ✅ `process_ships.awk` → Adapt for torpedoes/missiles/aircraft
- ✅ Sed insertion method → Use for all research tree insertions
- ✅ Bash estimation functions → Adapt for weapon specs

### New Scripts Needed
- `process_torpedoes.awk` → Convert torpedo research tree to database
- `process_missiles.awk` → Convert missile research tree to database
- `process_aircraft.awk` → Convert aircraft research tree to database
- `validate_research_trees.sh` → Check for circular dependencies, ID conflicts

---

## Completion Checklist

### Phase 1: Torpedoes ⬜
- ⬜ USA torpedoes research tree (50-70 nodes)
- ⬜ British torpedoes research tree (45-65 nodes)
- ⬜ German torpedoes research tree (45-60 nodes)
- ⬜ Japanese torpedoes research tree (50-70 nodes)
- ⬜ Torpedo database populated (300-500 entries)

### Phase 2: Missiles ⬜
- ⬜ USA missiles research tree (100-120 nodes)
- ⬜ British missiles research tree (30-40 nodes)
- ⬜ German missiles research tree (20-30 nodes)
- ⬜ Japanese missiles research tree (25-35 nodes)
- ⬜ Soviet/Russian missiles research tree (80-100 nodes)
- ⬜ Missile database populated (400-600 entries)

### Phase 3: Naval Aircraft ⬜
- ⬜ USA naval aircraft research tree (120-150 nodes)
- ⬜ British naval aircraft research tree (60-80 nodes)
- ⬜ German naval aircraft research tree (15-25 nodes)
- ⬜ Japanese naval aircraft research tree (70-90 nodes)
- ⬜ Naval aircraft database populated (500-800 entries)

### Phase 4: Ground Aircraft ⬜
- ⬜ USA ground aircraft research tree (200-280 nodes)
- ⬜ British ground aircraft research tree (110-140 nodes)
- ⬜ German ground aircraft research tree (100-130 nodes)
- ⬜ Japanese ground aircraft research tree (70-90 nodes)
- ⬜ Soviet/Russian ground aircraft research tree (150-200 nodes)
- ⬜ Ground aircraft database populated (800-1,200 entries)

---

**Status**: ⏳ **READY TO BEGIN** - Phase 1: USA Torpedoes
**Next Step**: Research USA torpedo history and create first research tree
**Estimated Completion**: 10-12 sessions (assuming 2-3 systems per session)
