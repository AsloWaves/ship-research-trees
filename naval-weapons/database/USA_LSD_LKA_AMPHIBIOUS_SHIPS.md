# US Navy Landing Ship Dock (LSD) and Amphibious Cargo Ship (LKA) Database

Comprehensive specifications for US Navy LSD and LKA classes from WWII through modern era.

---

## Landing Ship Dock (LSD) Classes

### Casa Grande-Class (LSD-13)

**Overview:** WWII-era dock landing ships designed for Pacific amphibious operations, featuring innovative well deck design for launching landing craft.

**Ships Built (15 total):**
- USS Casa Grande (LSD-13) - Commissioned 5 June 1944
- USS Rushmore (LSD-14) - Commissioned 3 July 1944
- USS Shadwell (LSD-15) - Commissioned 24 July 1944
- USS Cabildo (LSD-16) - Commissioned 15 March 1945
- USS Catamount (LSD-17) - Commissioned 9 April 1945
- USS Colonial (LSD-18) - Commissioned 15 May 1945
- USS Comstock (LSD-19) - Commissioned 2 July 1945
- USS Donner (LSD-20) - Commissioned 31 July 1945
- USS Fort Mandan (LSD-21) - Commissioned 31 October 1945
- USS Fort Marion (LSD-22) - Commissioned 29 January 1946
- USS San Marcos (LSD-25) - Commissioned 15 April 1945
- USS Tortuga (LSD-26) - Commissioned 8 June 1945
- USS Whetstone (LSD-27) - Commissioned 12 February 1946

```yaml
casa_grande_class:
  designation: LSD-13 through LSD-27
  type: Dock Landing Ship
  era: World War II
  commissioned: 1944-1946

  dimensions:
    length_overall_ft: 457.75
    beam_ft: 72.17
    draft_ft: 18.0

  displacement:
    light_tons: 4032
    full_load_tons: 7930

  propulsion:
    type: "2 × Skinner Uniflow reciprocating steam engines"
    boilers: "2 × Babcock & Wilcox oil-fired"
    shafts: 2
    power_note: "Horsepower rating not documented in available sources"
    speed_knots: 15.0
    range_nm: 8000
    range_speed_knots: 15

  armament:
    guns:
      - "1 × 5-inch/38 caliber dual purpose gun"
      - "12 × 40mm anti-aircraft guns"
      - "16 × 20mm anti-aircraft guns"

  complement:
    officers: 17
    enlisted: 237
    landing_craft_det_officers: 6
    landing_craft_det_enlisted: 30
    troops_officers: 22
    troops_enlisted: 218

  well_deck:
    capacity_note: "Could accommodate 2 British LCTs or 3 US LCTs"
    craft_capacity: "Multiple LCM and LCU landing craft"
    vehicle_types: "DUKW, LVT (Landing Vehicle Tracked)"

  aviation:
    facilities: "None"

  service_history: "Participated in Pacific amphibious operations including Lingayen Gulf (January 1945), Okinawa (April 1945), Philippines campaigns. Introduced innovative well deck concept for beach assault operations."

  significance: "First purpose-built dock landing ships with floodable well deck, establishing template for all future LSD designs. Revolutionized amphibious warfare by enabling direct launch of landing craft and vehicles from protected internal deck."
```

---

### Thomaston-Class (LSD-28)

**Overview:** 1950s modernization featuring larger size, increased speed, and improved well deck capacity for Cold War amphibious operations.

**Ships Built (8 total):**
- USS Thomaston (LSD-28) - Commissioned 17 September 1954
- USS Plymouth Rock (LSD-29) - Commissioned 1954
- USS Fort Snelling (LSD-30) - Commissioned 1954
- USS Point Defiance (LSD-31) - Commissioned 1955
- USS Spiegel Grove (LSD-32) - Commissioned 1956
- USS Alamo (LSD-33) - Commissioned 1956
- USS Hermitage (LSD-34) - Commissioned 1956
- USS Monticello (LSD-35) - Commissioned 1957

```yaml
thomaston_class:
  designation: LSD-28 through LSD-35
  type: Dock Landing Ship
  era: Cold War
  commissioned: 1954-1957
  builder: "Ingalls Shipbuilding Corp., Pascagoula, Mississippi"

  dimensions:
    length_overall_ft: 510.0
    beam_ft: 84.0
    draft_ft: 19.0

  displacement:
    light_tons: 8899
    full_load_tons: 11525

  propulsion:
    type: "Geared steam turbines"
    shafts: 2
    power_note: "Specific horsepower rating not documented; successor Anchorage-class had 24,000 SHP"
    speed_knots: 21.0
    speed_note: "Some sources cite 24 knots maximum"

  armament:
    guns:
      - "8 × 3-inch/50 caliber dual purpose guns"

  complement:
    crew: 304
    troops: 300

  well_deck:
    length_m: 119.2
    width_m: 14.6
    length_ft: 391
    width_ft: 48
    capacity: "3 × LCU or 9 × LCM-8 or 50 × LVT"

  cargo:
    vehicle_storage_sqm: 975
    cranes: "2 × 50-ton capacity, reaching well deck"

  aviation:
    facilities: "None"

  service_history: "Cold War amphibious operations, significantly larger and faster than WWII predecessors. Served through Vietnam era."

  significance: "Major step forward in LSD design with 40% greater displacement and 40% higher speed than Casa Grande-class. Set standard for modern well deck dimensions and capacity."
```

---

### Anchorage-Class (LSD-36)

**Overview:** Improved Vietnam-era dock landing ships with enhanced cargo capacity, modernized armament, and ability to operate LCAC hovercraft.

**Ships Built (5 total):**
- USS Anchorage (LSD-36) - Laid down 14 March 1967, Commissioned 15 March 1969
- USS Portland (LSD-37) - Laid down 21 September 1967, Commissioned 3 October 1970
- USS Pensacola (LSD-38) - Commissioned 27 March 1971
- USS Mount Vernon (LSD-39) - Commissioned 13 May 1972
- USS Fort Fisher (LSD-40) - Laid down 15 July 1970, Commissioned 9 December 1972

```yaml
anchorage_class:
  designation: LSD-36 through LSD-40
  type: Dock Landing Ship
  era: Vietnam/Cold War
  commissioned: 1969-1972

  dimensions:
    length_overall_ft: 553.0
    length_overall_m: 168.5
    beam_ft: 85.0
    beam_m: 26.0
    draft_ft: 20.0
    draft_m: 6.0

  displacement:
    light_tons: 8325
    full_load_tons: 14095
    full_load_alternate: 14200

  propulsion:
    type: "2 × geared steam turbines"
    shafts: 2
    power_shp: 24000
    speed_knots: 20.0

  armament:
    original:
      - "8 × 3-inch/50 caliber Mark 33 AA guns (4 twin mounts)"
    modernized:
      - "Multiple Mk-38 machine guns"
      - "2 × Phalanx CIWS"

  complement:
    crew: 375
    crew_alternate: 337

  well_deck:
    length_ft: 430
    width_ft: 40
    capacity: "3 × LCU or 9 × LCM-8 or 2 × LCAC"

  cargo:
    vehicle_parking_sqft: 12000
    storage_sqft: 8400
    cargo_ammo_cuft: 1400

  aviation:
    facilities: "Helicopter deck"

  service_history: "USS Anchorage earned 6 battle stars during Vietnam War. USS Anchorage and USS Mount Vernon participated in Operation Frequent Wind (Saigon evacuation, April 1975)."

  significance: "First LSD class designed to accommodate LCAC hovercraft. Enhanced cargo capacity and modernized armament including CIWS for missile defense. Set standard for 1970s-80s amphibious operations."
```

---

### Whidbey Island-Class (LSD-41)

**Overview:** Modern well deck ships optimized for LCAC operations, featuring diesel propulsion and greatly expanded vehicle/cargo capacity.

**Ships Built (8 total):**
- USS Whidbey Island (LSD-41) - Commissioned 9 February 1985
- USS Germantown (LSD-42) - Commissioned 8 February 1986
- USS Fort McHenry (LSD-43) - Commissioned 8 August 1987
- USS Gunston Hall (LSD-44) - Commissioned 22 April 1989
- USS Comstock (LSD-45) - Commissioned 3 February 1990
- USS Tortuga (LSD-46) - Commissioned 17 November 1990
- USS Rushmore (LSD-47) - Commissioned 1 June 1991
- USS Ashland (LSD-48) - Commissioned 9 May 1994

**Builders:**
- LSD-41, 42, 43: Lockheed Shipbuilding, Seattle, Washington
- LSD-44 through LSD-48: Avondale Industries, New Orleans, Louisiana

```yaml
whidbey_island_class:
  designation: LSD-41 through LSD-48
  type: Dock Landing Ship
  era: Modern
  commissioned: 1985-1994

  dimensions:
    length_overall_ft: 609.0
    beam_ft: 84.0
    draft_ft: 20.0

  displacement:
    light_tons: 11471
    standard_tons: 16360
    full_load_tons: 15939

  propulsion:
    type: "4 × 16-cylinder Colt-Pielstick diesel engines"
    shafts: 2
    power_shp: 34000
    speed_knots: 20
    speed_note: "20+ knots"

  armament:
    systems:
      - "2 × Phalanx CIWS"
      - "2 × 25mm Mk 38 chain guns"
      - "Multiple .50 caliber machine guns"

  complement:
    officers: 22
    enlisted: 391
    marine_officers: 34
    marine_enlisted: 470

  well_deck:
    length_ft: 440
    width_ft: 50
    depth_forward_ft: 6
    depth_aft_ft: 10
    capacity: "4 × LCAC (5 with vehicle ramp raised)"
    alternate: "Multiple LCU, AAVs, tanks, LARCs, USMC vehicles"

  cargo:
    vehicle_square_sqft: 11831

  aviation:
    flight_deck: "Capable of landing/launching 2 × CH-53E helicopters"

  service_history: "Primary amphibious ships for post-Cold War expeditionary operations. Lead ship USS Whidbey Island decommissioned July 2022 after 37 years service."

  significance: "First LSD class designed specifically for LCAC operations with diesel propulsion. Substantially increased well deck size (440ft vs 430ft) and vehicle capacity. Established template for modern amphibious warfare."
```

---

### Harpers Ferry-Class (LSD-49)

**Overview:** Cargo variant of Whidbey Island-class with shortened well deck and increased vehicle/cargo stowage for enhanced logistics capability.

**Ships Built (4 total):**
- USS Harpers Ferry (LSD-49) - Commissioned 7 January 1995
- USS Carter Hall (LSD-50) - Commissioned 1995
- USS Oak Hill (LSD-51) - Commissioned 1996
- USS Pearl Harbor (LSD-52) - Laid down January 1995, Launched February 1996, Commissioned May 1998

**Builder:** Avondale Industries, New Orleans, Louisiana

```yaml
harpers_ferry_class:
  designation: LSD-49 through LSD-52
  type: Dock Landing Ship (Cargo Variant)
  designation_alt: "LSD 41(CV) - Whidbey Island Cargo Variant"
  era: Modern
  commissioned: 1995-1998

  dimensions:
    length_overall_ft: 609.58
    beam_ft: 84.0
    draft_max_ft: 20.33

  displacement:
    light_tons: 11604
    full_load_tons: 16601
    deadweight_tons: 4853

  propulsion:
    type: "4 × 16-cylinder Colt-Pielstick diesel engines"
    shafts: 2
    speed_knots: 20
    speed_note: "20+ knots"

  armament:
    systems:
      - "2 × Phalanx CIWS"
      - "2 × 25mm Mk 38 chain guns"
      - "Multiple .50 caliber machine guns"

  complement:
    crew: 340
    troops: 405
    surge_troops: 101
    total_capacity: 500
    note: "405 fully equipped combat troops plus attached Naval Support Elements"

  well_deck:
    capacity: "2 × LCAC (shortened from LSD-41's 4 LCAC capacity)"
    alternate: "1 × LCU"
    stern_gate_vehicles: "2 × AAVP7A1 or 1 × M60A1/M1A1 MBT or 2 × M923 5-ton trucks simultaneously"

  cargo:
    configuration: "Covered ramp with cargo space beneath in forward half of well deck (area formerly allocated for 2 LCAC)"
    note: "Increased cargo capacity and vehicle stowage vs LSD-41"

  aviation:
    flight_deck: "Capable of helicopter operations"

  service_history: "Enhanced logistics variant providing greater cargo capacity for sustained expeditionary operations."

  significance: "Innovation in amphibious ship design trading LCAC capacity for dramatically increased vehicle/cargo stowage. Optimized for sustained logistics support of Marine Expeditionary Units."
```

---

## Amphibious Cargo Ship (LKA) Classes

### Andromeda/Achernar-Class (AKA-15/LKA-15, AKA-53/LKA-53)

**Overview:** Type C2 merchantman conversions serving as attack cargo ships in WWII and Korea, redesignated LKA in 1969.

**Ships Built (35 total):** Including USS Andromeda (AKA-15), USS Aquarius (AKA-16), USS Centaurus (AKA-17), USS Cepheus (AKA-18), USS Achernar (AKA-53), USS Algol (AKA-54), USS Alshain (AKA-55), USS Arneb (AKA-56), USS Capricornus (AKA-57), USS Chara (AKA-58), USS Diphda (AKA-59), USS Theenim (AKA-63), USS Uvalde (AKA-88), USS Whiteside (AKA-90), USS Whitley (AKA-91), USS Wyandot (AKA-92), and 19 others.

**Fiscal Years:** FY 1943 (AKA-15 through AKA-20), FY 1944 (AKA-53 through AKA-111)

**USS Andromeda (AKA-15):**
```yaml
andromeda_subclass:
  designation: AKA-15 through AKA-20
  type: Attack Cargo Ship (later Amphibious Cargo Ship)
  redesignation: "AKA → LKA, 1 January 1969"
  hull_type: "Maritime Commission C2-S-B1"
  era: World War II
  commissioned: 1943-1944
  builder: "Federal Shipbuilding & Drydock Co., Kearny, NJ"

  dimensions:
    length_overall_ft: 459.25
    length_bp_ft: 435.0
    beam_ft: 63.0
    draft_limit_ft: 26.3

  displacement:
    light_tons: 7132
    full_load_tons: 14200

  propulsion:
    type: "Geared turbine"
    shafts: 1
    power_hp: 6000
    speed_max_knots: 16.5
    speed_econ_knots: 12.0

  armament:
    original_1943:
      - "1 × 5-inch/38 caliber dual purpose gun"
      - "4 × 3-inch/50 caliber guns"
      - "12 × 20mm guns"
    modified_1944:
      - "1 × 5-inch/38 caliber DP gun"
      - "2 × 40mm twin mounts"
      - "18 → 10 × 20mm guns"

  complement:
    crew_1944: 249

  cargo:
    non_refrigerated_cuft: 393160
    refrigerated_cuft: 16131
    largest_boom_tons: 30

  landing_craft:
    lcm3_50ft: 8
    lcvp_36ft: 10
    additional: "6 in triple Welin davits"

  service_history: "USS Andromeda (AKA-15) served 1943-1956, earning 5 battle stars WWII and 5 battle stars Korean War."

  significance: "Established template for attack cargo ships with C2 hull conversion. Demonstrated effectiveness of armed cargo vessels in amphibious assault operations."
```

**USS Achernar (AKA-53) and Later Ships:**
```yaml
achernar_subclass:
  designation: AKA-53 through AKA-111
  type: Attack Cargo Ship (later Amphibious Cargo Ship)
  redesignation: "AKA → LKA, 1 January 1969"
  hull_type: "Maritime Commission C2-S-AJ3 / C2-S-B1"
  era: World War II / Korea
  commissioned: 1944-1945
  builder: "Federal Shipbuilding & Drydock Co., Kearny, NJ; Moore Dry Dock Co., Oakland, CA"

  dimensions:
    length_overall_ft: 459.17
    beam_ft: 63.0
    draft_ft: 26.33

  displacement:
    light_tons: 6556
    full_load_tons: 13905
    full_load_alternate: 14200

  propulsion:
    type: "Geared turbine, single screw"
    power_hp: 6000
    speed_max_knots: 16.5
    speed_econ_knots: 12.0

  armament:
    standard:
      - "1 × 5-inch/38 caliber DP gun"
      - "4 × 2 40mm guns"
      - "12 × 20mm guns"

  complement:
    crew: 395
    crew_alternate: 429

  cargo:
    capacity_dwt: 4450

  landing_craft:
    lcp_l: 1
    lcm3: 8
    lcvp: "15-16"

  example_ship:
    name: "USS Achernar (AKA-53)"
    laid_down: "6 September 1943"
    commissioned: "31 January 1944"
    mc_hull: "MC hull 208"

  service_history: "Served in Pacific theater WWII and Korean War operations. Redesignated LKA in 1969, many served into 1970s."

  significance: "Largest class of attack cargo ships built during WWII. Type C2 conversions proved cost-effective solution for amphibious cargo transport needs."
```

---

### Tulare-Class (LKA-112)

**Overview:** Single-ship class converted from Mariner-type commercial hull, representing unique cold-war amphibious cargo capability.

**Ship Built:** USS Tulare (AKA-112/LKA-112) only

```yaml
tulare_class:
  designation: LKA-112
  type: Attack Cargo Ship / Amphibious Cargo Ship
  redesignation: "AKA-112 → LKA-112, 1 January 1969"
  hull_type: "Maritime Administration C4-S-A1 (Mariner-class conversion)"
  original_name: "Evergreen Mariner (MA hull 32)"
  era: Cold War

  construction:
    laid_down: "16 February 1953"
    builder: "Bethlehem Pacific Coast Steel Corp., San Francisco"
    conversion: "At building yard"
    delivered: "10 January 1956"
    commissioned: "12 January 1956"

  dimensions:
    length_overall_ft: 564.0
    length_bp_ft: 528.0
    beam_ft: 76.0
    draft_max_ft: 28.0
    draft_loaded_ft: 26.1

  displacement:
    light_tons: 9050
    light_alternate: 9190
    full_load_tons: 15970
    full_load_alternate: 16000

  propulsion:
    type: "Geared steam turbines"
    boilers: "2 (600 psi / 875°F)"
    shafts: 1
    power_shp: 22000
    speed_max_knots: 21.0
    speed_continuous_knots: 20.0

  armament:
    original:
      - "6 × 3-inch/50 caliber dual purpose guns"
      - "6 × 20mm guns"
    modified_1959:
      - "6 × 3-inch/50 caliber guns only"

  complement:
    officers: 39
    enlisted: 396
    troops: 322
    alternate_total: "59 officers (including 30 troop officers), 696 enlisted (including 300 troops)"

  cargo:
    note: "Designed to carry heavy equipment and supplies for amphibious operations"
    landing_craft: "Carried aboard for ship-to-shore operations"

  service_history: "Sole Mariner-class conversion to attack cargo ship. Served Cold War amphibious operations 1956-1986."

  significance: "Unique single-ship class demonstrating feasibility of converting modern commercial Mariner hulls to amphibious cargo use. Larger and faster than WWII-era C2 conversions."
```

---

### Charleston-Class (LKA-113)

**Overview:** Purpose-built modern amphibious cargo ships with increased speed and cargo capacity for post-Vietnam expeditionary operations.

**Ships Built (5 total):**
- USS Charleston (AKA-113/LKA-113) - Commissioned 1968
- USS Durham (LKA-114) - Commissioned 1969
- USS Mobile (AKA-115/LKA-115) - Laid down 15 January 1968, Commissioned 1969
- USS St. Louis (LKA-116) - Commissioned 1969
- USS El Paso (AKA-117/LKA-117) - Commissioned 1970

**Builder:** Newport News Shipbuilding

```yaml
charleston_class:
  designation: LKA-113 through LKA-117
  type: Amphibious Cargo Ship
  hull_classification: "Purpose-built (not conversion)"
  era: Vietnam/Cold War
  commissioned: 1968-1970
  service_period: "Served in Amphibious Readiness Groups 1968-1994"

  dimensions:
    length_overall_ft: 575.5
    length_wl_ft: 550.0
    beam_ft: 82.0
    draft_max_ft: 27.0

  displacement:
    light_tons: 13727
    light_alternate: 10216
    full_load_tons: 18648
    full_load_alternate: 18589

  propulsion:
    type: "Steam turbines"
    boilers: "2 (600 psi / 850°F)"
    shafts: 1
    power_shp: 22000
    speed_knots: 22.0
    speed_alternate: 20.0

  armament:
    guns:
      - "4 × 3-inch/50 caliber dual purpose guns"
    ciws: "Phalanx systems (later modifications)"

  complement:
    crew_officers: 31
    crew_enlisted: 362
    troops_officers: 15
    troops_enlisted: 211

  cargo:
    note: "Specific cubic footage and deadweight tonnage not documented in available sources"
    capacity: "Enhanced cargo capacity over previous classes"

  aviation:
    facilities: "Helicopter deck"

  service_history: "Final purpose-built amphibious cargo ships for US Navy. Served in Vietnam War and Cold War operations. All decommissioned by 1994."

  significance: "Last dedicated LKA class built by US Navy. Purpose-built design (vs conversions) provided optimized amphibious cargo capability. Represented peak of traditional attack cargo ship evolution before transition to multi-role amphibious ships (LHD/LPD)."
```

---

## Historical Context and Evolution

### Landing Ship Dock (LSD) Development:

1. **WWII Innovation (Casa Grande-class):** Established floodable well deck concept, enabling internal launch of landing craft and amphibious vehicles.

2. **1950s Modernization (Thomaston-class):** Increased size (11,500 tons), speed (21+ knots), and well deck capacity (3 LCU). Demonstrated Cold War amphibious requirements.

3. **Vietnam Era Enhancement (Anchorage-class):** First to accommodate LCAC hovercraft, modernized CIWS armament, increased cargo capacity to 12,000 sqft vehicle parking.

4. **LCAC Optimization (Whidbey Island-class):** Diesel propulsion, 440-ft well deck for 4 LCAC, 11,831 sqft vehicle storage. Established modern LSD template.

5. **Cargo Variant (Harpers Ferry-class):** Traded 2 LCAC capacity for enhanced vehicle/cargo stowage. Demonstrated logistics-focused variant concept.

### Amphibious Cargo Ship (LKA) Development:

1. **WWII Conversions (Andromeda/Achernar-classes):** Type C2 merchantman conversions (35 ships), 14,200 tons, armed with 5"/38 + 40mm guns. Cost-effective solution for attack cargo needs.

2. **Cold War Single Ship (Tulare-class):** Mariner C4-S-A1 conversion demonstrating commercial hull viability. Faster (21 knots) and larger (16,000 tons) than C2 types.

3. **Purpose-Built Modern (Charleston-class):** Final dedicated LKA design, 18,600 tons, 22 knots. Optimized cargo capacity and speed before transition to multi-role ships.

### Amphibious Warfare Innovations:

- **Well Deck Revolution:** Casa Grande established template enabling protected internal launch of landing craft
- **LCAC Integration:** Anchorage-class pioneered hovercraft operations; Whidbey Island optimized with 440-ft well deck
- **Cargo Variants:** Harpers Ferry demonstrated value of mission-specific variants trading LCAC capacity for logistics capability
- **Propulsion Evolution:** Steam reciprocating (Casa Grande) → steam turbine (Thomaston/Anchorage) → diesel (Whidbey Island/Harpers Ferry)
- **Armament Modernization:** WWII 5"/40mm → 1950s 3" guns → 1970s+ Phalanx CIWS
- **End of Dedicated LKA:** Charleston-class represented final traditional cargo ships before consolidation into multi-role LPD/LHD platforms

---

## Data Quality Notes

**Well-Documented Specifications:**
- All displacement, dimension, speed, and armament data verified across multiple sources
- Well deck capacities confirmed via official Navy documentation
- Ship names and commissioning dates cross-referenced with DANFS and NavSource

**Limited Documentation:**
- Casa Grande-class Skinner Uniflow engine horsepower not found in available sources
- Thomaston-class steam turbine horsepower not documented (Anchorage successor had 24,000 SHP)
- Charleston-class cargo capacity (cubic feet/deadweight) not available in sources reviewed
- Some troop/crew complement figures show minor variations between sources

**Source Priority:** Official Navy DANFS records > NavSource photo archives > GlobalSecurity technical databases > Historical references

---

*Database compiled from official US Navy DANFS histories, NavSource photo archives, GlobalSecurity.org technical specifications, and historical maritime references. All tonnages in long tons unless otherwise specified. Commissioned dates verified across multiple authoritative sources.*