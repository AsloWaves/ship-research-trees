# Modular Ship Building System Design
## Research Tree Integration with Component-Based Gameplay

**Date**: October 10, 2025
**Game Type**: Modular ship builder with Tarkov-style inventory management
**Core Mechanic**: Player builds hulls, installs components, assigns crew, loads inventory

---

## 🎮 Game Mechanics Understanding

### Player Workflow:
1. **Build/Acquire Hull** (ship chassis/template)
2. **Install Turrets** (main guns, secondary guns)
3. **Install Modules** (engines, FCS, radar, sonar, etc.)
4. **Assign Crew** to each module (required for operation)
5. **Load Inventory** (ammo, fuel, supplies - Tarkov-style tetris)
6. **Sail Out** of port

### Key Insight:
**Ships are NOT pre-built units** - they are **customizable platforms** where players install components

---

## 🔧 What Research Actually Unlocks

### Current Problem:
Research tree says "Indiana-class" but what does that actually give the player?

### Solution: Research Unlocks Multiple Things

#### Example 1: Research "Indiana-class (1895)"

**Unlocks:**
1. ✅ **Indiana-class Hull** (blueprint to build chassis)
2. ✅ **13"/35 Mk 1 Gun** (weapon technology)
3. ✅ **13"/35 Mk 1 Turret** (mounting system for gun)
4. ✅ **Triple Expansion Steam Engine** (propulsion tech)
5. ✅ **Optical Fire Control Mk 1** (basic FCS)
6. ✅ **Harvey Armor** (armor technology)

**What Player Gets:**
- Can now BUILD Indiana-class hulls at shipyard
- Can now MANUFACTURE 13" guns and turrets
- Can now INSTALL appropriate engines
- Can now USE 1890s-era fire control

#### Example 2: Research "Iowa-class (1943)"

**Unlocks:**
1. ✅ **Iowa-class Hull** (massive 887' chassis)
2. ✅ **16"/50 Mk 7 Gun** (most powerful USN gun)
3. ✅ **16"/50 Mk 7 Triple Turret** (3-gun mount)
4. ✅ **Geared Steam Turbines** (high-speed engines)
5. ✅ **Mk 38 Fire Control Director** (WWII-era FCS)
6. ✅ **SK-2 Air Search Radar** (long-range air detection)
7. ✅ **SG Surface Search Radar** (surface targeting)
8. ✅ **Class A Armor** (face-hardened steel)

#### Example 3: Research "Iowa 1984 Reactivation"

**Unlocks:**
1. ✅ **Iowa 1984 Refit Hull** (modified superstructure, helicopter deck)
2. ✅ **BGM-109 Tomahawk Launcher** (32-cell cruise missile system)
3. ✅ **RGM-84 Harpoon Launcher** (16-cell anti-ship missile)
4. ✅ **Phalanx CIWS** (20mm gatling point defense)
5. ✅ **AN/SPS-49 Radar** (3D air search)
6. ✅ **AN/SLQ-32 ECM Suite** (electronic warfare)
7. ✅ **Mk 13 Fire Control System** (digital FCS)

**Player Can:**
- Refit existing Iowa hull with new components
- OR build new hull with 1984 configuration

---

## 📊 What "Upgraded" Ships Actually Are

### Critical Realization:
**"Tennessee 1943 Rebuild" is NOT an upgrade - it's a DIFFERENT HULL**

### Comparison: Tennessee-class vs Tennessee 1943 Rebuild

#### **Tennessee-class (Original 1920 Hull)**

**Hull Specifications:**
- Displacement: 32,300 tons
- Beam: 97.5 feet
- Draft: 30 feet

**Hardpoint Layout:**
- **Main Battery**: 4× Heavy turret mounts (14" caliber capable)
  - Position: 2 fore, 2 aft, all centerline
- **Secondary Battery**: 14× Casemate mounts (5"/51)
  - Position: 7 per side, armored casemates
- **Anti-Aircraft**: 4× Light AA mounts (3")
- **Torpedo Defense**: None (original design)

**Internal Compartments:**
- **Magazine Space**: 2,800 tons capacity (14" and 5" shells)
- **Fuel Bunkers**: 4,600 tons oil capacity
- **Crew Quarters**: 1,100 capacity
- **Engine Rooms**: 4× boiler rooms, 2× turbine rooms

**Module Slots:**
- Engine Slots: 8× boiler units, 2× turbine units
- Fire Control: 2× director positions (fore/aft)
- Radar Mounts: 0 (not designed for radar)
- Sonar: None

#### **Tennessee 1943 Rebuild Hull** (DIFFERENT HULL)

**Hull Specifications:**
- Displacement: 40,500 tons (+8,200 tons)
- Beam: **114 feet** (+16.5 feet - MUCH WIDER)
- Draft: 28 feet (torpedo bulges reduce draft)

**Hardpoint Layout:**
- **Main Battery**: 4× Heavy turret mounts (14" caliber) - SAME
  - Position: 2 fore, 2 aft, centerline - SAME
- **Secondary Battery**: 16× Dual-Purpose mounts (5"/38)
  - Position: 8 per side, enclosed turrets (NOT casemates)
- **Anti-Aircraft**:
  - 10× Quad 40mm Bofors mounts
  - 43× Single 20mm Oerlikon mounts
- **Torpedo Defense**: Anti-torpedo bulges (blister armor)

**Internal Compartments:**
- **Magazine Space**: 3,800 tons capacity (+1,000 tons for AA ammo)
- **Fuel Bunkers**: 4,600 tons oil capacity (same)
- **Crew Quarters**: **2,200 capacity** (+1,100 - DOUBLED)
- **Engine Rooms**: 4× boiler rooms, 2× turbine rooms (same)

**Module Slots:**
- Engine Slots: 8× boiler units, 2× turbine units (same)
- Fire Control: 4× director positions (main, secondary, 2× AA)
- Radar Mounts: **4× radar positions** (NEW)
  - 1× air search mast
  - 2× fire control radar
  - 1× surface search
- Sonar: 1× bow sonar dome (NEW)

**Structural Differences:**
- **Superstructure**: COMPLETELY different - tower mast vs cage mast
- **Armor Deck**: +3" STS over magazines, +2" elsewhere
- **Hull Form**: Wider beam with anti-torpedo bulges
- **Weight Distribution**: Higher center of gravity (more topweight)

---

## 🔄 How "Upgrades" Work in Modular System

### Scenario: Player Has USS Tennessee

**Player's Ship (1920 Hull)**:
```
HULL: Tennessee-class (1920)
INSTALLED MODULES:
├─ Main Battery:
│  ├─ Turret 1: 14"/50 Mk 4 Triple Turret (fore)
│  ├─ Turret 2: 14"/50 Mk 4 Triple Turret (fore superfiring)
│  ├─ Turret 3: 14"/50 Mk 4 Triple Turret (aft)
│  └─ Turret 4: 14"/50 Mk 4 Triple Turret (aft superfiring)
├─ Secondary Battery:
│  └─ 14× 5"/51 Casemate Guns
├─ Fire Control:
│  └─ Mk 19 Optical Director
├─ Engines:
│  ├─ 8× Oil-fired Boilers
│  └─ 2× Curtis Turbines
└─ Crew: 1,057 assigned

INVENTORY (Tarkov Grid):
├─ Forward Magazine:
│  ├─ 600× 14" AP shells (8 tons each)
│  └─ 400× 14" HC shells
├─ Aft Magazine:
│  ├─ 600× 14" AP shells
│  └─ 1,200× 5" shells
└─ Fuel Bunker: 4,200 tons oil
```

### Player Researches "Tennessee 1943 Rebuild"

**Two Options Appear:**

#### **Option A: Refit Existing Ship** 🔧
```
PROCESS:
1. Ship enters drydock (18 months)
2. All modules REMOVED and stored:
   - 4× 14" turrets (saved - can reuse)
   - 14× 5" casemate guns (saved - might sell)
   - Mk 19 FCS (obsolete - scrap)
   - 8× boilers (saved - can reuse)
   - 2× turbines (saved - can reuse)
3. Old Tennessee hull SCRAPPED or MOTHBALLED
4. New Tennessee 1943 hull CONSTRUCTED
5. Modules REINSTALLED:
   - 4× 14" turrets (reused - no cost)
   - 16× NEW 5"/38 DP turrets (must build)
   - 10× NEW quad 40mm mounts (must build)
   - 43× NEW 20mm guns (must build)
   - NEW Mk 37 FCS (must build)
   - NEW SK radar (must build)
   - 8× boilers (reused - no cost)
   - 2× turbines (reused - no cost)
6. Crew expanded: 1,057 → 2,200 (recruit +1,143 crew)
7. Ship recommissioned as USS Tennessee (Rebuilt)

COST:
- New hull construction: 50% of original cost
- New components: 5"/38 turrets, 40mm mounts, radar, FCS
- Crew recruitment/training: +1,143 sailors
- Drydock time: 18 months
- Resources: Steel, electronics, ammunition

BENEFIT:
- Same main guns (14" turrets)
- MUCH better AA defense (10× quad 40mm + 43× 20mm)
- Radar capability (air/surface search + fire control)
- Better torpedo protection (bulges)
- Can engage aircraft and surface targets simultaneously (DP guns)
```

#### **Option B: Build New Ship** 🏗️
```
PROCESS:
1. Keep existing USS Tennessee (1920 hull) in service
2. Build NEW ship with Tennessee 1943 hull
3. Name it something else (e.g., USS California if available)

COST:
- Full new hull construction: 100% cost
- All new components: 14" turrets, 5"/38, 40mm, radar, engines, FCS
- Full crew: 2,200 sailors
- Build time: 36 months
- Resources: Full material cost

BENEFIT:
- Keep old ship operational during construction
- Two ships instead of one
- Old ship can serve secondary role or be scrapped later
```

---

## 🗂️ Database Structure Changes Needed

### 1. **Ship Hulls Table** (Primary)

```markdown
| Hull_ID | Country | Hull_Class | Hull_Variant | Year | Ship_Type | Length_FT | Beam_FT | Draft_FT | Displacement_Tons | Crew_Capacity | Main_Hardpoints | Secondary_Hardpoints | AA_Hardpoints | Torpedo_Hardpoints | Missile_Hardpoints | Engine_Slots | FCS_Slots | Radar_Slots | Sonar_Slots | Magazine_Capacity_Tons | Fuel_Capacity_Tons | Supply_Hold_Tons | Armor_Scheme_ID | Max_Speed_KTS | Turning_Radius_YD | Build_Cost | Build_Time_Months | Notes |
```

**Example Entries:**

```markdown
| 10001 | USA | Tennessee-class | Base (1920) | 1920 | BB | 624 | 97.5 | 30 | 32300 | 1100 | 4× Heavy-14" | 14× Casemate-5" | 4× Light-3" | 0 | 0 | 8B+2T | 2 | 0 | 0 | 2800 | 4600 | 200 | STD-1916 | 21 | 750 | $15M | 48 | Original configuration |

| 10002 | USA | Tennessee-class | 1943 Rebuild | 1943 | BB | 624 | 114 | 28 | 40500 | 2200 | 4× Heavy-14" | 16× DP-5" | 10× Quad-40mm + 43× Single-20mm | 0 | 0 | 8B+2T | 4 | 4 | 1 | 3800 | 4600 | 300 | STD-1943 | 20 | 780 | $45M | 18 (refit) | Pearl Harbor rebuild |
```

### 2. **Hardpoints Table** (NEW - Critical)

Defines what can be mounted where on each hull

```markdown
| Hardpoint_ID | Hull_ID | Hardpoint_Type | Hardpoint_Size | Position | Elevation_Arc | Traverse_Arc | Max_Weight_Tons | Compatible_Module_Types | Notes |
```

**Example:**

```markdown
| 1 | 10001 | Main_Battery | Heavy-14" | Fore_Centerline_Lower | -5° to +30° | 270° | 850 | 14" Triple Turrets | Turret 1 position |
| 2 | 10001 | Main_Battery | Heavy-14" | Fore_Centerline_Super | -5° to +30° | 270° | 850 | 14" Triple Turrets | Turret 2 position (superfiring) |
| 3 | 10001 | Secondary_Battery | Casemate-5" | Port_Amidships_1 | -5° to +15° | 120° | 12 | 5"/51 Casemate | Fixed casemate mount |
...

| 100 | 10002 | Secondary_Battery | DP-5" | Port_Amidships_1 | -10° to +85° | 360° | 25 | 5"/38 DP Twin | Enclosed turret, AA capable |
| 101 | 10002 | AA_Battery | Quad-40mm | Port_Bridge_Wing | -5° to +90° | 360° | 8 | 40mm Quad Bofors | Radar-directed mount |
| 102 | 10002 | Radar_Mount | Air_Search | Main_Mast_Top | N/A | 360° | 5 | SK, SK-2 radars | Rotating antenna |
```

### 3. **Turrets/Weapons Modules Table** (Links to Guns DB)

```markdown
| Turret_ID | Turret_Name | Gun_ID | Mount_Config | Guns_Per_Mount | Turret_Weight_Tons | Rotation_Rate_DEG_SEC | Elevation_Rate_DEG_SEC | Elevation_Range | Crew_Required | Power_Draw_KW | Ammo_Capacity | Compatible_Hardpoint_Sizes | Year_Available | Notes |
```

**Example:**

```markdown
| 5001 | 14"/50 Mk 4 Triple | 1045 | Triple | 3 | 850 | 2.0 | 4.0 | -5° to +30° | 94 | 150 | 300 shells | Heavy-14", XHeavy-16" | 1916 | Standard-type BB turret |

| 5010 | 16"/50 Mk 7 Triple | 1072 | Triple | 3 | 1,708 | 2.0 | 12.0 | -2° to +45° | 110 | 450 | 390 shells | XHeavy-16" | 1943 | Iowa-class turret, fastest elevation |

| 5020 | 5"/38 Mk 12 Twin DP | 1150 | Twin | 2 | 25 | 15.0 | 15.0 | -10° to +85° | 15 | 75 | 800 shells | DP-5" | 1934 | Dual-purpose, AA capable |
```

### 4. **Engine Modules Table**

```markdown
| Engine_ID | Engine_Name | Engine_Type | Horsepower | Fuel_Type | Fuel_Consumption_TONS_HR | Weight_Tons | Space_Required | Crew_Required | Compatible_Hull_Types | Year_Available | Notes |
```

**Example:**

```markdown
| 3001 | Curtis Turbine | Geared_Steam | 14000 | Oil | 1.2 | 420 | Large | 45 | BB, CA, CL | 1916 | Standard-type propulsion |

| 3010 | General Electric Turbine | Geared_Steam | 53000 | Oil | 2.8 | 850 | XLarge | 60 | Fast_BB | 1940 | Iowa-class, 33-knot capable |
```

### 5. **Fire Control Systems Table**

```markdown
| FCS_ID | FCS_Name | FCS_Type | Year | Range_Calculation | Accuracy_Bonus | Radar_Integration | Crew_Required | Power_Draw_KW | Weight_Tons | Compatible_Weapon_Types | Notes |
```

**Example:**

```markdown
| 4001 | Mk 19 Optical Director | Optical_Rangefinder | 1916 | Stereoscopic | +5% | No | 8 | 5 | 15 | All guns | Standard-type FCS |

| 4010 | Mk 37 Director | Radar_FCS | 1940 | Radar + Analog_Computer | +25% | Yes (requires Mk 4 radar) | 15 | 50 | 25 | 5" DP, 40mm | WWII AA director |

| 4020 | Mk 38 GFCS | Radar_FCS | 1943 | Radar + Ballistic_Computer | +35% | Yes (requires Mk 8 radar) | 22 | 85 | 40 | 14", 16" guns | Main battery fire control |
```

### 6. **Radar Systems Table**

```markdown
| Radar_ID | Radar_Name | Radar_Type | Year | Detection_Range_NM | Accuracy | Targets_Tracked | Crew_Required | Power_Draw_KW | Weight_Tons | Compatible_Mount_Types | Notes |
```

**Example:**

```markdown
| 6001 | SK Air Search | Air_Search | 1941 | 100 | Medium | 20 | 6 | 35 | 4 | Air_Search_Mast | Long-range air detection |

| 6010 | Mk 8 Fire Control | Fire_Control | 1943 | 30 | High | 1 | 4 | 25 | 3 | FCS_Director | Main battery ranging |

| 6020 | AN/SPS-49 | 3D_Air_Search | 1975 | 250 | Very_High | 300 | 8 | 180 | 12 | Modern_Mast | Digital air search |
```

### 7. **Ammunition/Consumables Table**

```markdown
| Item_ID | Item_Name | Item_Type | Caliber | Weight_LBS | Stack_Size | Storage_Type | Compatible_Weapons | Cost_Per_Unit | Notes |
```

**Example:**

```markdown
| 8001 | 14" AP Mk 16 Shell | Main_Gun_Shell | 14" | 1,400 | 1 | Magazine | 14"/50 Mk 4 | $850 | Armor-piercing, 2,240 fps |

| 8010 | 16" AP Mk 8 Shell | Main_Gun_Shell | 16" | 2,700 | 1 | Magazine | 16"/50 Mk 7 | $1,500 | Super-heavy shell |

| 8020 | 5"/38 AA Shell VT | DP_Shell | 5" | 55 | 20 | Magazine | 5"/38 Mk 12 | $45 | Proximity fuse |

| 8030 | Bunker C Fuel Oil | Fuel | N/A | 8.3/gal | 1000gal | Fuel_Bunker | Oil_Boilers | $0.15/gal | Standard naval fuel |

| 8040 | BGM-109 Tomahawk | Cruise_Missile | N/A | 3,500 | 1 | Missile_Magazine | Tomahawk_Launcher | $1.5M | 1,000nm range |
```

---

## 🎯 Research Tree Unlocks - Revised Structure

### Each Research Node Unlocks Package:

#### **Research Node: Indiana-class (1895)**
**RP Cost**: 5,000

**Unlocks:**
1. **Hull**: Indiana-class (Base)
   - Hull_ID: 10010
   - 4× Heavy-13" hardpoints
   - 8× Secondary-8" hardpoints
   - Crew capacity: 586

2. **Turrets**:
   - 13"/35 Mk 1 Twin Turret
   - 8"/35 Mk 2 Single Turret

3. **Guns** (links to Guns DB):
   - 13"/35 Mk 1
   - 8"/35 Mk 2

4. **Engines**:
   - Vertical Triple Expansion Engine (9,000 HP)

5. **Fire Control**:
   - Optical Rangefinder Mk 1 (basic)

6. **Armor**:
   - Harvey Nickel Steel Armor (18" belt)

**Player Can Now:**
- Build Indiana-class hulls
- Manufacture 13" and 8" turrets
- Install 1890s steam engines
- Use optical fire control

---

#### **Research Node: Tennessee 1943 Rebuild**
**RP Cost**: 16,000
**Prerequisites**: Tennessee-class (Base)

**Unlocks:**
1. **Hull**: Tennessee-class (1943 Rebuild Variant)
   - Hull_ID: 10002
   - 4× Heavy-14" hardpoints (SAME as base)
   - 16× DP-5" hardpoints (DIFFERENT from base)
   - 10× Quad-40mm hardpoints (NEW)
   - 43× Single-20mm hardpoints (NEW)
   - 4× Radar mount positions (NEW)
   - 1× Sonar position (NEW)
   - Crew capacity: 2,200 (vs 1,100 base)

2. **Turrets**:
   - 5"/38 Mk 12 Twin DP Turret (if not already unlocked)
   - 40mm Bofors Quad Mount (if not already unlocked)
   - 20mm Oerlikon Single Mount (if not already unlocked)

3. **Fire Control**:
   - Mk 37 Director (5" and 40mm control)
   - Mk 38 GFCS (main battery radar FCS)

4. **Radar**:
   - SK-2 Air Search Radar
   - SG Surface Search Radar
   - Mk 8 Fire Control Radar (for main battery)

5. **Sonar**:
   - QC Sonar (basic submarine detection)

**Player Can Now:**
- **Option A**: Refit existing Tennessee ships to 1943 configuration
  - Strip all modules from old hull
  - Build new Tennessee 1943 hull
  - Reinstall compatible modules (14" turrets, engines)
  - Install new modules (5"/38, 40mm, radar)
- **Option B**: Build new ships with 1943 hull from scratch

**Existing 14" Turrets Are Compatible!**
- Player can reuse 14"/50 turrets from base Tennessee
- No need to rebuild main battery
- Just add new AA and electronics

---

#### **Research Node: Iowa 1984 Reactivation**
**RP Cost**: 75,000
**Prerequisites**: Iowa-class (1943)

**Unlocks:**
1. **Hull**: Iowa-class (1984 Refit Variant)
   - Hull_ID: 10075
   - 3× XHeavy-16" hardpoints (SAME as 1943)
   - 8× DP-5" hardpoints (REDUCED from 10× in 1943)
   - 32× Tomahawk VLS cells (NEW)
   - 16× Harpoon launchers (NEW)
   - 4× Phalanx mounts (NEW)
   - 6× Modern radar positions (NEW)
   - 1× Helicopter deck (NEW)
   - Crew capacity: 1,800 (LESS than 1943 - automation)

2. **Weapons**:
   - BGM-109 Tomahawk VLS (32-cell)
   - RGM-84 Harpoon Quad Launcher
   - Phalanx CIWS Mk 15

3. **Fire Control**:
   - Mk 13 Weapons Direction System (digital FCS)
   - Tomahawk Fire Control System

4. **Radar**:
   - AN/SPS-49 3D Air Search
   - AN/SPS-67 Surface Search
   - AN/SPQ-9 Fire Control

5. **Electronics**:
   - AN/SLQ-32 ECM Suite
   - Link 11/16 Data Link
   - Satellite Communications

**Player Can:**
- Refit existing Iowa 1943 ships to 1984 configuration
- Keep 16" main guns (reuse turrets)
- Add cruise missile capability
- Modernize all electronics
- Reduce crew (automation reduces manning)

---

## 🧩 Inventory System (Tarkov-Style)

### Magazine/Storage Grid System

Each hull has defined **compartment spaces** with Tetris-style grid loading:

#### **Example: Iowa-class Magazine Layout**

**Turret 1 Magazine** (Forward):
```
Grid Size: 12×8 (96 slots)
Ammunition Types:
- 16" AP Shell: 4×4 slots, 2.7 tons each
- 16" HC Shell: 4×4 slots, 1.9 tons each

Current Load:
[AP][AP][AP][--]
[AP][AP][AP][HC]
[AP][AP][AP][HC]
[--][--][HC][HC]

Total: 16× AP shells, 8× HC shells
Weight: 58.4 tons / 400 tons capacity
```

**40mm Magazine** (Amidships):
```
Grid Size: 20×10 (200 slots)
Ammunition Types:
- 40mm Clip (4 rounds): 1×1 slot, 6 lbs each

Current Load:
[Packed with 180× clips = 720 rounds]

Total: 720× 40mm shells ready
Weight: 2.1 tons / 50 tons capacity
```

**Fuel Bunker** (Multiple compartments):
```
Total Capacity: 8,841 tons oil
Current Load: 7,200 tons (81% full)

Endurance: At 25 knots = 9,600 nm
           At 15 knots = 16,200 nm
```

### Item Stacking Rules:

**Large Items** (don't stack well):
- 16" AP shells: 4×4 slots each
- Torpedoes: 6×2 slots each
- Tomahawk missiles: 3×3 slots each

**Medium Items** (stack moderately):
- 5" shells: 1×2 slots, stack up to 20
- 40mm clips: 1×1 slots, stack up to 50

**Small Items** (stack highly):
- 20mm magazines: 1×1 slot, stack up to 100
- Small arms ammo: 1×1 slot, stack up to 500

**Bulk Items** (fill large areas):
- Fuel oil: Pumped into bunkers, measured in tons
- Potable water: Tank storage, measured in gallons
- Food supplies: Hold storage, measured in days of supply

---

## 🔄 Refit Process Detailed Example

### Player Scenario: USS Tennessee Refit

**Starting State (1941)**:
```
Ship: USS Tennessee
Hull: Tennessee-class (Base 1920)
Status: Damaged at Pearl Harbor (torpedoes, bomb hits)

CURRENT CONFIGURATION:
├─ Main Battery: 4× 14"/50 Mk 4 Triple (Operational)
├─ Secondary: 14× 5"/51 Casemate (Some damaged)
├─ AA: 4× 3"/23 (Inadequate)
├─ FCS: Mk 19 Optical (Obsolete)
├─ Radar: None
├─ Engines: 8× Boilers, 2× Turbines (Operational)
└─ Crew: 1,057 (Some casualties)

DAMAGE REPORT:
- Hull: Moderate (flooding controlled)
- Armor belt: Minor damage
- Turrets 1-4: Operational
- 6× Secondary guns: Destroyed
- Superstructure: Fire damage
```

**Player Decision Point:**

**Option 1: Basic Repair** ($5M, 3 months)
- Patch hull
- Repair damaged secondaries
- Return to service quickly
- Same capabilities as before

**Option 2: Modernization Refit** (Research required: "Tennessee 1943 Rebuild")
- Cost: $45M, 18 months
- Transform into essentially new ship

**Player Chooses Option 2**

**Refit Process:**

**Phase 1: Decommissioning** (Month 1)
```
1. Remove all ammunition from ship
   - Offload 1,200× 14" shells → Shore magazine
   - Offload 2,000× 5" shells → Shore magazine
   - Offload 4,200 tons fuel → Shore tanks

2. Remove crew
   - 1,057 sailors transferred to other ships or shore duty
   - Retain core crew (200) for refit supervision

3. Enter drydock
   - Drydock #1, Puget Sound Navy Yard
```

**Phase 2: Demolition** (Months 2-4)
```
1. Remove all weapons:
   - 4× 14"/50 turrets → SAVED (850 tons each, $2M each)
   - 14× 5"/51 casemate guns → Scrapped ($50K salvage)
   - 4× 3"/23 AA guns → Scrapped

2. Strip superstructure:
   - Remove cage masts → Scrapped
   - Remove armored conning tower → Scrapped (120 tons armor plate)
   - Remove funnels → Scrapped

3. Remove internal equipment:
   - Mk 19 FCS → Obsolete, scrapped
   - Old wiring → Salvage copper
   - Steam piping → Some reused

4. Remove engines:
   - 8× Boilers → SAVED (can reuse)
   - 2× Turbines → SAVED (can reuse)

5. Cut hull:
   - Remove damaged sections
   - Widen beam for anti-torpedo bulges
```

**Phase 3: Hull Reconstruction** (Months 5-9)
```
1. Install anti-torpedo bulges:
   - Add 16.5 feet to beam (97.5' → 114')
   - Internal compartmentalization
   - +5,000 tons displacement

2. Reinforce armor deck:
   - Add 3" STS over magazines
   - Add 2" STS over machinery
   - +1,400 tons armor weight

3. Rebuild internal spaces:
   - Expand crew quarters (1,100 → 2,200 capacity)
   - Add new magazine spaces for AA ammunition
   - Install radar equipment rooms
   - Install improved damage control stations

4. Build new superstructure:
   - Tower mast (forward)
   - Tower mast (aft)
   - Integrated fire control platforms
   - Radar mounts on masts
```

**Phase 4: Module Installation** (Months 10-15)
```
1. Reinstall saved modules:
   - 8× Boilers (reused) → $0
   - 2× Turbines (reused) → $0
   - 4× 14"/50 Turrets (reused) → $0

2. Install NEW modules (must manufacture or purchase):

   Main Battery FCS:
   - 1× Mk 38 GFCS → $800K
   - 1× Mk 8 Fire Control Radar → $200K

   Secondary Battery:
   - 16× 5"/38 Mk 12 Twin DP Turrets → $2.4M ($150K each)
   - 2× Mk 37 Directors → $400K ($200K each)
   - 2× Mk 4 Fire Control Radar → $300K

   Anti-Aircraft:
   - 10× Quad 40mm Bofors Mounts → $500K ($50K each)
   - 43× 20mm Oerlikon Single Mounts → $215K ($5K each)

   Radar Suite:
   - 1× SK-2 Air Search Radar → $400K
   - 1× SG Surface Search Radar → $250K

   Sonar:
   - 1× QC Sonar → $150K

   Electronics:
   - New electrical system → $1M
   - Communications upgrade → $200K
   - Fire control computers → $500K

TOTAL NEW EQUIPMENT: $7.5M
LABOR: $35M
TOTAL REFIT COST: $42.5M
```

**Phase 5: Testing & Shakedown** (Months 16-18)
```
1. Crew recruitment:
   - Recall original crew: 200
   - Recruit new crew: +2,000
   - Training: 3 months

2. Load ship:
   - Ammunition:
     - 1,200× 14" shells (reused from shore)
     - 4,000× 5"/38 shells (NEW)
     - 20,000× 40mm rounds (NEW)
     - 50,000× 20mm rounds (NEW)
   - Fuel: 4,600 tons oil
   - Supplies: 90 days provisions

3. Sea trials:
   - Speed trials: 20.5 knots achieved
   - Gunnery practice:
     - Main battery: Mk 38 + Mk 8 radar = +35% accuracy
     - AA battery: Mk 37 + Mk 4 radar = +40% vs aircraft
   - Radar testing: SK-2 detects aircraft at 100nm

4. Commission: USS Tennessee (Rebuilt)
   - New hull designation: BB-43 (Mod 1943)
   - Ready for combat
```

**Final Result:**
```
Ship: USS Tennessee (Rebuilt)
Hull: Tennessee-class (1943 Rebuild Variant)

CONFIGURATION:
├─ Main Battery: 4× 14"/50 Mk 4 Triple (REUSED)
├─ Secondary: 16× 5"/38 Mk 12 Twin DP (NEW)
├─ AA Light: 10× Quad 40mm Bofors (NEW)
├─ AA Close: 43× 20mm Oerlikon (NEW)
├─ Main FCS: Mk 38 + Mk 8 Radar (NEW)
├─ AA FCS: 2× Mk 37 + Mk 4 Radar (NEW)
├─ Air Search: SK-2 Radar (NEW)
├─ Surface Search: SG Radar (NEW)
├─ Sonar: QC (NEW)
├─ Engines: 8× Boilers + 2× Turbines (REUSED)
└─ Crew: 2,200

CAPABILITIES:
- Main battery effectiveness: +35% (radar FCS)
- AA effectiveness: +200% (modern guns + radar)
- Air detection: 100nm (vs 0nm before)
- Surface detection: 40nm (vs visual only)
- Submarine detection: 3,000 yards (vs none)
- Torpedo protection: Bulges (vs none)
- Crew comfort: Improved (modern quarters)

COMBAT EFFECTIVENESS: +150% overall
```

---

## ✅ Summary: How System Works

### Research Tree:
**Unlocks PACKAGES** of hull + components, not complete ships

### Ship Building:
1. Build hull (chassis)
2. Install modules (turrets, engines, FCS, radar)
3. Assign crew
4. Load inventory (ammo, fuel, supplies)

### Upgrades:
**NOT upgrades** - they're **DIFFERENT HULLS** with different hardpoint layouts

### Refits:
1. Remove modules from old hull
2. Build new hull variant
3. Reinstall compatible modules (save cost)
4. Install new modules (modern systems)
5. Recruit additional crew if needed

### Key Advantages:
- **Modularity**: Mix and match components
- **Customization**: Player choice in loadouts
- **Economy**: Reuse expensive components (turrets)
- **Progression**: Unlock better modules over time
- **Inventory Management**: Tarkov-style supply logistics

---

**This system makes "upgraded" ships make sense** - they're alternate hull configurations that can reuse some components (main guns, engines) while requiring new components (AA guns, radar, FCS).

**Created**: October 10, 2025
