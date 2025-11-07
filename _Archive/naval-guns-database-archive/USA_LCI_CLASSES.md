# US Navy Landing Craft Infantry (LCI) Classes - Complete Technical Documentation

## Overview

The Landing Craft Infantry (LCI) was a dedicated amphibious assault ship designed to transport 200 infantry troops directly to hostile beaches. Developed in response to a British request for a seagoing vessel larger than assault landing craft like the LCVP but smaller than LSTs, the LCI filled a critical gap in amphibious warfare capabilities. These 158-foot vessels could travel from rear bases under their own power at speeds up to 15 knots, participating in every major amphibious operation from 1943 onwards.

**Total Production**: 923 LCI vessels built (1942-1944)
**Service**: Both Pacific and European theaters
**Variants**: LCI(L) transport, LCI(G) gunboat, LCI(R) rocket ship, LCI(M) mortar support

---

## LCI(L)-1 Class (Square Conning Tower, Side Ramps)

### Basic Information
```yaml
class_name: LCI(L)-1 Class
hull_numbers: LCI(L)-1 through LCI(L)-350
total_built: 350
commissioned: 1942-1943
decommissioned: 1946-1948 (majority 1946)
modded: false
```

### Physical Specifications
```yaml
displacement:
  light: 216 tons
  landing: 234 tons
  full_load: 389 tons

dimensions:
  length: 158 feet 5.5 inches (158.5 ft)
  beam: 23 feet 3 inches (23.25 ft)
  draft_light_mean: 3 feet 1.5 inches
  draft_landing_forward: 2 feet 8 inches
  draft_landing_aft: 4 feet 10 inches
  draft_loaded_forward: 5 feet 4 inches
  draft_loaded_aft: 5 feet 11 inches
  hull_material: "1/4 inch steel plate"
```

### Propulsion System
```yaml
propulsion:
  type: "Twin shaft diesel"
  engines: "Two banks of Detroit Diesel 6-71 'Quad' engines (8 total, 4 per shaft)"
  horsepower: 1,600 BHP total
  shafts: 2
  propellers: "Twin variable pitch"
  fuel_type: Diesel
  fuel_capacity: 120 tons diesel fuel
  lube_oil: 200 gallons

performance:
  speed_maximum: 16 knots
  speed_continuous: 14 knots
  speed_operational: "Approximately 14 knots"
  range_12_knots: 4,000 nautical miles (loaded)
  range_15_knots: 500 nautical miles (with 110 tons fuel)
  endurance_extended: "Up to 4,000 nautical miles at 12 knots without troops"
```

### Crew and Troop Capacity
```yaml
crew:
  officers: 2
  enlisted: 21
  total: 24 (some sources indicate up to 60 for specialized variants)

troop_capacity:
  officers: 6
  enlisted: 182
  total: 188-200 infantry troops
  voyage_duration: "Designed for 48-hour passage"
```

### Armament (Standard LCI(L))
```yaml
anti_aircraft:
  primary: "Five (5) single 20mm Oerlikon Mk 4 AA guns"
  placement:
    - "One bow mounted"
    - "One port forward of wheelhouse"
    - "One starboard forward of wheelhouse"
    - "One port aft of wheelhouse"
    - "One starboard aft of wheelhouse"
  alternate_config: "Some had four 20mm guns plus two .50 cal machine guns"

notes: "Light AA armament for protection during beach approach"
```

### Design Features
```yaml
landing_system:
  type: "Side ramps (port and starboard)"
  description: "Two gangways on either side of bow led to pair of lowered ramps"
  limitation: "Deck wider than prow; ramps exposed troops to enemy fire"

conning_tower:
  type: "Square, low profile"
  location: "Center of ship"
  note: "Provided limited visibility from bridge"

construction:
  hull_composition: "Quarter-inch steel plate throughout"
  bow_design: "Narrower than main deck to accommodate side ramps"
```

### Service History
```yaml
theaters: ["Pacific", "European"]

major_operations:
  european:
    - "Anzio (January 1944)"
    - "Normandy D-Day (June 6, 1944)"
    - "Southern France (August 1944)"
    - "Elba"
  pacific:
    - "Tarawa (November 1943)"
    - "Saipan (June 1944)"
    - "Guam (July 1944)"
    - "Philippines (1944-1945)"
    - "Iwo Jima (February 1945)"
    - "Okinawa (April 1945)"

tactical_role: "Direct troop delivery to hostile beaches"
limitations: "Side ramp design made vessels vulnerable during initial assault waves"
post_tarawa: "Lessons learned led to increased fire support requirements"

decommissioning:
  pattern: "Most decommissioned 1946, struck from Naval Register same year"
  disposal: "Transferred to Maritime Commission 1947-1948 for scrapping"
  examples:
    - "LCI(L)-47: Decommissioned April 24, 1946; transferred January 22, 1948"
    - "LCI(L)-759: Decommissioned May 13, 1946; transferred February 17, 1948"
    - "LCI(L)-493: Struck December 13, 1946; sold October 28, 1947"
```

### Notable Vessels
```yaml
representative_ships:
  - name: "USS LCI(L)-10"
    notes: "Early production vessel; transferred to State Department June 1947"
  - name: "USS LCI(L)-94"
    notes: "Coast Guard manned; participated in D-Day Normandy operations"
  - name: "USS LCI(L)-24"
    notes: "Later converted to LCI(G)-24; sold for scrap December 13, 1946"
```

---

## LCI(L)-351 Class (Round Conning Tower, Bow Ramp)

### Basic Information
```yaml
class_name: LCI(L)-351 Class
hull_numbers: LCI(L)-351 through LCI(L)-1098
total_built: 748 (approximate)
commissioned: 1943-1944
decommissioned: 1946-1948
modded: false
improvements_over_predecessor: "Taller round conning tower, enclosed bow ramp design"
```

### Physical Specifications
```yaml
displacement:
  light: 216 tons
  landing: 234 tons
  full_load: 387-389 tons
  note: "Slightly different from LCI-1 class due to bow door configuration"

dimensions:
  length: 158 feet 5.5 inches
  beam: 23 feet 3 inches
  draft_light: 3 feet 1.5 inches forward
  draft_landing_forward: 2 feet 10 inches
  draft_landing_aft: 5 feet 3 inches
  draft_loaded: 5 feet 4 inches forward, 5 feet 11 inches aft
```

### Propulsion System
```yaml
propulsion:
  type: "Twin shaft diesel"
  engines: "Two banks of Detroit Diesel 6-71 'Quad' diesel engines"
  configuration: "8 engines total (4 per shaft)"
  horsepower: 1,600 BHP
  shafts: 2
  fuel_type: Diesel
  fuel_capacity: 110 tons (approximately 10 tons less than predecessors)
  lube_oil: 200 gallons

performance:
  speed_maximum: 15.5 knots
  speed_continuous: 14-15 knots
  range_12_knots: 4,000 nautical miles
  range_15_knots: 500 nautical miles
```

### Crew and Troop Capacity
```yaml
crew:
  officers: 2
  enlisted: 21-22
  total: 24

troop_capacity:
  standard: 200 infantry troops
  officers: 6
  enlisted: 182-194
```

### Armament
```yaml
anti_aircraft:
  standard: "Five (5) single 20mm Oerlikon Mk 4 AA cannons"
  placement:
    - "One bow mounted"
    - "Two forward of wheelhouse (port/starboard)"
    - "Two aft of wheelhouse (port/starboard)"
  additional: "Some vessels equipped with two .50 cal machine guns"
```

### Design Improvements
```yaml
conning_tower:
  type: "Round, taller design"
  improvement: "Afforded significantly better visibility from bridge"
  introduced: "LCI(L)-350 and higher hull numbers"

bow_ramp_system:
  type: "Single enclosed bow ramp with two bow doors"
  configuration: "Doors swing open; ramp extends forward"
  advantage: "Provided protection and concealment for disembarking troops"
  tactical_benefit: "Reduced exposure to enemy observation and fire"
  comparison: "Significant improvement over vulnerable side ramps of LCI-1 class"
```

### Service History
```yaml
commissioning_examples:
  - vessel: "LCI(L)-351"
    laid_down: "March 5, 1943"
    launched: "April 8, 1943"
    commissioned: "May 14, 1943"
    redesignations:
      - "LCI(G)-351: December 31, 1944"
      - "LCI(M)-351: April 30, 1945"

  - vessel: "LCI(L)-449"
    laid_down: "June 17, 1943"
    launched: "August 14, 1943"
    commissioned: "August 25, 1943"
    note: "Later converted to LCI(G)-449"

  - vessel: "LCI(L)-1091"
    commissioned: "September 21, 1944"
    note: "Late production vessel"

operations: "Same major amphibious operations as LCI-1 class, with improved survivability"
post_war: "Decommissioned 1946; transferred to Maritime Commission 1947-1948"
```

### Notable Vessels
```yaml
representative_ships:
  - name: "USS LCI(L)-351"
    significance: "First of improved class with bow ramp design"
    conversions: "Served as LCI(G)-351, then LCI(M)-351"

  - name: "USS LCI(L)-449"
    conversions: "Converted to LCI(G)-449 gunboat variant"
    decommissioning: "January 1946, Pacific Reserve Fleet San Diego"

  - name: "USS LCI(L)-1091"
    notes: "Late war construction, commissioned September 1944"
```

---

## LCI(G) Class (Gunboat Conversion)

### Basic Information
```yaml
class_name: Landing Craft Infantry (Gunboat)
designation: LCI(G)
type: "Fire support gunboat converted from LCI(L)"
purpose: "Close-in fire support for amphibious operations"
conversions_from: "LCI(L) hulls of both 1-350 and 351+ classes"
total_converted: "Precise number unknown; multiple flotillas converted"
service_period: 1943-1946
modded: false
role_change: "No longer transported troops; dedicated fire support vessel"
```

### Physical Specifications
```yaml
displacement:
  full_load: 387 tons (LCI(G)-1 class specification)

dimensions:
  length: 160 feet (some sources indicate 158.5 feet)
  beam: 23 feet 3 inches
  draft_forward_landing: 2 feet 10 inches
  draft_aft_landing: 5 feet 3 inches
```

### Propulsion System
```yaml
propulsion:
  type: "Same as base LCI(L) class"
  engines: "Detroit Diesel 6-71 'Quad' engines"
  horsepower: 1,600 BHP
  shafts: 2

performance:
  speed: 15.5 knots
  range: "Similar to base LCI(L) class"
```

### Crew
```yaml
complement:
  officers: 5
  enlisted: 65
  total: 70
  note: "Increased from base LCI(L) due to additional weapons systems"
```

### Armament Configurations

#### Early Conversions (LCI(G) 21, 22, 23, 70)
```yaml
main_guns:
  type: "3-inch/50 caliber dual purpose guns"
  number: "Not specified in sources"

secondary:
  - "40mm Bofors AA guns"
  - "20mm Oerlikon AA guns"
  - ".50 caliber machine guns"
```

#### Standard LCI(G) Configuration
```yaml
main_armament:
  type: "40mm Bofors AA guns"
  number: 2-3 guns
  configuration: "Single barrel mounts"
  note: "Replaced three forward-mounted 20mm guns from LCI(L)"

secondary_armament:
  20mm_guns:
    number: 4
    type: "20mm Oerlikon AA"

  machine_guns:
    number: 6
    type: ".50 caliber heavy machine guns"

  rockets:
    number: 10
    type: "Mk 7 rocket launchers"
    capability: "12 x 4.5-inch barrage rockets per launcher"
    rate_of_fire: "Full salvo in approximately 4 seconds"
    feed: "Automatic feed from one rail"
    range: 1,120 yards maximum
```

#### LCI(G)-449 Specific Configuration
```yaml
armament_example:
  40mm_guns: 2
  20mm_guns: 4
  machine_guns_50cal: 6
  mk7_rocket_launchers: 10
```

### Conversion Details
```yaml
modifications:
  removed:
    - "Troop landing ramps (side or bow depending on base class)"
    - "Three forward 20mm guns"
    - "Troop berthing spaces"

  added:
    - "40mm gun mounts (typically 2-3 guns)"
    - "Additional 20mm gun positions"
    - "Rocket launcher mounts"
    - "Ammunition storage for increased firepower"
    - "Fire control equipment"

  structural: "Well deck and troop compartments modified for ammunition stowage"
```

### Tactical Employment
```yaml
mission: "Close-in fire support during amphibious assaults"

capabilities:
  - "Direct fire on beach defenses"
  - "Anti-aircraft protection for landing forces"
  - "Suppressive fire during troop landing phases"
  - "Rocket barrage for area saturation"

doctrine:
  timing: "Provided fire support from cessation of naval bombardment until troops ashore"
  positioning: "Operated close to beach, within small arms range"
  coordination: "Worked with LCI(R) rocket ships for combined fire missions"
```

### Service History
```yaml
first_conversions: 1943

flotilla_organization:
  example: "Group Thirteen of Flotilla Five (mid-1944)"
  composition: "LCI(G)s 21-24, 61, and 64-70"
  note: "Consisted solely of gunboats"

major_operations:
  - "Saipan (June 15, 1944)"
  - "Philippines campaign"
  - "Iwo Jima (February 1945)"
  - "Okinawa (April 1945)"

combat_examples:
  saipan:
    vessels: "LCI(G)-725, LCI(G)-726"
    date: "June 15, 1944"
    mission: "Fire support for landing craft assault waves"
    casualties: "LCI(G)-726: 2 KIA, several WIA from enemy fire"

decommissioning:
  pattern: "Most decommissioned 1946"
  example: "LCI(G)-449 decommissioned January 1946, Pacific Reserve Fleet San Diego"
  disposal: "Transferred to Maritime Commission May 3, 1948"
```

### Notable Vessels
```yaml
representative_ships:
  - name: "LCI(G)-21"
    notes: "First gunboat conversion; 3-inch/50 cal guns"

  - name: "LCI(G)-22"
    notes: "Early conversion with 3-inch guns"

  - name: "LCI(G)-351"
    original: "LCI(L)-351"
    redesignated: "December 31, 1944"
    further_conversion: "LCI(M)-351 on April 30, 1945"

  - name: "LCI(G)-449"
    original: "LCI(L)-449"
    operations: "Pacific theater fire support"
    decommissioned: "January 1946"

  - name: "LCI(G)-725"
    operation: "Saipan assault, June 15, 1944"

  - name: "LCI(G)-726"
    operation: "Saipan assault; sustained casualties from enemy fire"
```

---

## LCI(R) Class (Rocket Ship Conversion)

### Basic Information
```yaml
class_name: Landing Craft Infantry (Rocket)
designation: LCI(R)
type: "Rocket bombardment ship converted from LCI(L)"
purpose: "Shore bombardment and suppressive fire support"
conversions_from: "LCI(L) hulls, both early and late classes"
conversion_timing: "Late 1943 onwards; some converted during construction"
first_combat_use: "Late 1943, New Britain Island (New Guinea)"
service_period: 1943-1946
modded: false
```

### Physical Specifications
```yaml
displacement:
  note: "Same as base LCI(L) class, approximately 387 tons full load"

dimensions:
  length: 158.5 feet
  beam: 23.2 feet
  draft: 6 feet
  note: "Dimensions identical to base LCI(L) class"
```

### Propulsion System
```yaml
propulsion:
  type: "Same as base LCI(L)"
  engines: "Detroit Diesel 6-71 'Quad' engines"
  horsepower: 1,600 BHP
  shafts: 2
  fuel: Diesel

performance:
  speed: "14-15 knots"
  range: "Similar to base LCI(L), approximately 4,000 nm at 12 knots"
```

### Crew
```yaml
complement:
  note: "Similar to LCI(G), increased from base LCI(L)"
  estimate: "60-70 personnel for rocket operations and fire control"
```

### Rocket Armament

#### Primary Rocket System
```yaml
rocket_launchers:
  type: "Mark 7 (Mk 7) rocket launchers"
  number: 10 launchers
  configuration: "Mounted in place of side ramps and inside well deck"

rocket_specifications:
  type: "4.5-inch barrage rockets"
  launchers_per_rail: 12 rockets
  feed_system: "Automatic feed"
  rate_of_fire: "Full salvo in approximately 4 seconds"
  maximum_range: 1,120 yards

total_capacity:
  rockets: 504 total rockets (some sources indicate up to 1,000+ rounds)
  note: "Could fire all 504 rockets in a single beach bombardment run"
```

#### Alternative Configuration
```yaml
some_vessels:
  launchers: "6 x 5-inch rocket launchers"
  note: "Variant configuration; less common than 4.5-inch system"
```

#### Defensive Armament
```yaml
anti_aircraft:
  20mm_guns: "Retained from base LCI(L) configuration"
  configuration: "Likely reduced from standard five guns due to rocket installation"
```

### Conversion Details
```yaml
modifications:
  removed:
    - "Side landing ramps (both port and starboard)"
    - "Troop berthing facilities"
    - "Some internal troop compartments"

  added:
    - "10 x Mk 7 rocket launcher racks"
    - "Rocket ammunition magazines (No. 2 Troop Compartment converted)"
    - "Fire control systems for rocket salvoes"
    - "Extensive ammunition stowage throughout well deck"

  structural:
    well_deck: "Filled with rocket launcher racks and ammunition"
    magazine: "Former troop compartment converted to rocket magazine"
```

### Tactical Employment
```yaml
doctrine:
  primary_mission: "Saturation bombardment of beach defenses immediately before assault"
  timing: "Started when heavy naval/aerial bombardment ceased"
  duration: "Continued until first assault wave troops landed"
  positioning: "Close to beach for maximum accuracy and psychological effect"

firepower:
  total_rockets: "504 x 4.5-inch rockets in single run"
  effect: "Massive suppressive fire; area saturation bombardment"
  psychological: "Furious barrage to suppress enemy positions"

coordination:
  radar_ships: "Circled around destroyer or other radar-equipped vessels"
  fire_control: "Received target direction and distance from radar ships"
  targeting: "Radar ships relayed coordinates of suspected enemy positions"
  execution: "LCI(R) would loose barrages on command"
```

### Service History
```yaml
first_combat: "Late 1943, seizure of New Britain Island (New Guinea)"

adoption: "After painful lessons at Tarawa, Marine Corps adopted LCI rocket and gunship fire support as integral to amphibious doctrine"

major_operations:
  pacific_theater:
    - "New Britain (December 1943)"
    - "Saipan (June 1944)"
    - "Philippines (1944-1945)"
    - "Iwo Jima (February 1945)"
    - "Okinawa (April 1945)"

effectiveness: "Provided critical suppressive fire during vulnerable assault phases"

post_war:
  decommissioning: "1946"
  disposal: "Transferred to Maritime Commission 1947-1948"
```

### Notable Vessels
```yaml
representative_ships:
  - name: "LCI(R)-707"
    service: "Pacific theater operations"
    note: "Documented in multiple amphibious assaults"

  - name: "LCI(R)-771"
    operations: "Iwo Jima and Okinawa campaigns"
    note: "Redesignated LCI(R) in March 1945"
```

### Combat Effectiveness
```yaml
advantages:
  - "Massive firepower from compact platform"
  - "Ability to deliver 504 rockets in single pass"
  - "Close-in support unavailable from larger ships"
  - "Precision timing to support assault waves"

tactical_innovation: "Filled gap between naval bombardment and troops ashore"
doctrine_integration: "Became standard element of Pacific amphibious operations post-Tarawa"
```

---

## LCI(M) Class (Mortar Support Conversion)

### Basic Information
```yaml
class_name: Landing Craft Infantry (Mortar)
designation: LCI(M)
type: "Mortar fire support ship converted from LCI(L)"
purpose: "Naval surface fire support using chemical mortars"
conversions_from: "LCI(L) hulls"
service_period: 1945-1946
modded: false
note: "Least common LCI variant; specialized fire support role"
```

### Physical Specifications
```yaml
displacement:
  note: "Same as base LCI(L) class"

dimensions:
  length: 158.5 feet
  beam: 23 feet 3 inches
  draft: "Similar to base LCI(L)"
  note: "Hull unchanged from base class"
```

### Propulsion System
```yaml
propulsion:
  type: "Standard LCI twin shaft diesel"
  engines: "Detroit Diesel 6-71 'Quad' engines"
  horsepower: 1,600 BHP
  shafts: 2
  fuel: Diesel

performance:
  speed: "14-15 knots"
  range: "Similar to base LCI(L)"
```

### Crew
```yaml
complement:
  note: "Increased from base LCI(L) for mortar operations"
  estimate: "50-60 personnel including mortar crews"
```

### Armament

#### Primary Mortar Armament
```yaml
mortars:
  type: "M2 4.2-inch chemical mortars"
  number: 3
  mounting:
    location: "Well deck forward"
    configuration: "Three 4ft x 4ft wooden walled sandboxes"
    sandbox_height: "2 inches x 6 inches walls filled with sand"
    orientation: "Tripod mortar tubes positioned to fire forward over bow"

  ammunition_storage:
    magazine: "No. 2 Troop Compartment (under well deck) converted to mortar magazine"
    capacity: "Extensive stowage for 4.2-inch mortar rounds"
```

#### Defensive Armament
```yaml
anti_aircraft:
  20mm_guns:
    number: 5
    type: "Single 20mm Oerlikon AA guns"
    placement:
      - "One bow mounted"
      - "One port forward of wheelhouse"
      - "One starboard forward of wheelhouse"
      - "One port aft of wheelhouse"
      - "One starboard aft of wheelhouse"

  machine_guns:
    number: 2
    type: ".50 caliber machine guns"
    note: "Added to some vessels for additional defense"
```

### Conversion Details
```yaml
modifications:
  removed:
    - "Troop landing capability"
    - "Troop berthing spaces"
    - "Original use of well deck"

  added:
    - "Three 4ft x 4ft sandboxes for mortar mounts"
    - "M2 4.2-inch chemical mortars with tripod mounts"
    - "Mortar ammunition magazine (converted troop compartment)"
    - "Fire control equipment"

  structural:
    well_deck: "Fitted with three wooden-walled sandboxes for mortar stability"
    no2_compartment: "Converted from troop space to mortar ammunition magazine"
    firing_arc: "Mortars oriented to fire forward over bow"
```

### Tactical Employment
```yaml
fire_support_doctrine:
  primary_role: "Indirect naval surface fire support"
  target_types: "Japanese positions inland or on reverse slopes"
  range: "Extended inland fire support as fighting moved beyond beaches"

coordination:
  radar_ships: "Circled around radar-equipped destroyers or other vessels"
  fire_control_method: "Radar ships relayed direction and distance to targets"
  communication: "LCI(M) received target coordinates via radio"
  execution: "Loosed barrages of mortar shells at suspected enemy positions"

advantages:
  - "High-angle fire for targets behind cover"
  - "Ability to engage reverse slope positions"
  - "Extended fire support as troops advanced inland"
  - "Chemical mortar capability for specialized missions"
```

### Service History
```yaml
introduction: 1945

conversion_example:
  vessel: "LCI(M)-351"
  original: "LCI(L)-351"
  first_redesignation: "LCI(G)-351 on December 31, 1944"
  final_redesignation: "LCI(M)-351 on April 30, 1945"

operations:
  theater: "Pacific"
  period: "1945 (late war)"
  role: "Fire support for advancing troops during island campaigns"

effectiveness: "Provided valuable indirect fire support capability from mobile platform"

post_war:
  decommissioning: "1946"
  disposal: "Transferred to Maritime Commission for disposal 1947-1948"
```

### Notable Vessels
```yaml
representative_ships:
  - name: "LCI(M)-351"
    original_commission: "May 14, 1943 as LCI(L)-351"
    conversions:
      - "LCI(G)-351: December 31, 1944"
      - "LCI(M)-351: April 30, 1945"
    note: "Example of vessel converted through multiple configurations"
```

---

## Comparison Matrix: LCI Variants

### Mission Roles
```yaml
LCI(L):
  primary_mission: "Infantry transport and beach assault"
  secondary_mission: "Light anti-aircraft defense"
  troop_capacity: 200
  fire_support: "Minimal (defensive AA only)"

LCI(G):
  primary_mission: "Close-in fire support for amphibious operations"
  secondary_mission: "Anti-aircraft protection"
  troop_capacity: 0
  fire_support: "Heavy (40mm, 20mm, rockets)"

LCI(R):
  primary_mission: "Beach bombardment and saturation fire"
  secondary_mission: "Suppressive fire for assault waves"
  troop_capacity: 0
  fire_support: "Massive (504 rockets in single salvo)"

LCI(M):
  primary_mission: "Indirect naval surface fire support"
  secondary_mission: "High-angle fire on inland targets"
  troop_capacity: 0
  fire_support: "Medium (3 x 4.2-inch mortars)"
```

### Firepower Comparison
```yaml
LCI(L):
  guns: "5 x 20mm AA"
  rockets: None
  mortars: None

LCI(G):
  guns: "2-3 x 40mm, 4 x 20mm, 6 x .50 cal"
  rockets: "10 x Mk 7 launchers (120 rockets)"
  mortars: None

LCI(R):
  guns: "Reduced AA (some 20mm retained)"
  rockets: "10 x Mk 7 launchers (504 rockets total capacity)"
  mortars: None

LCI(M):
  guns: "5 x 20mm, 2 x .50 cal"
  rockets: None
  mortars: "3 x M2 4.2-inch chemical mortars"
```

### Tactical Employment Timeline
```yaml
assault_phase_minus_30_minutes:
  active: ["LCI(R)"]
  mission: "Initial beach saturation bombardment"

assault_phase_minus_15_minutes:
  active: ["LCI(R)", "LCI(G)"]
  mission: "Sustained suppressive fire on beach defenses"

assault_phase_H_hour:
  active: ["LCI(R)", "LCI(G)", "LCI(L)"]
  missions:
    LCI(R): "Final rocket barrage"
    LCI(G): "Close support fire"
    LCI(L): "Troop delivery to beach"

assault_phase_plus_30_minutes:
  active: ["LCI(G)", "LCI(M)"]
  missions:
    LCI(G): "Close support of troops ashore"
    LCI(M): "Indirect fire on inland positions"

assault_phase_plus_2_hours:
  active: ["LCI(M)"]
  mission: "Extended fire support as troops advance inland"
```

---

## Historical Significance and Legacy

### Amphibious Warfare Innovation
```yaml
doctrinal_impact:
  - "Filled critical gap between small landing craft (LCVP) and large landing ships (LST)"
  - "Demonstrated need for dedicated fire support in amphibious operations"
  - "Post-Tarawa lessons drove development of gunboat and rocket variants"
  - "Established template for specialized fire support craft"

tactical_lessons:
  tarawa_1943: "Heavy casualties highlighted need for close fire support"
  post_tarawa: "LCI(G) and LCI(R) became integral to amphibious doctrine"
  normandy_1944: "Proved effectiveness in European theater"
  pacific_1944_1945: "Essential element of every major island assault"
```

### Production and Service Statistics
```yaml
total_production:
  lci_l_built: 923 vessels
  construction_period: 1942-1944
  builders: "Multiple US shipyards"

conversions:
  lci_g: "Multiple flotillas; exact total unknown"
  lci_r: "Substantial numbers; used extensively Pacific theater"
  lci_m: "Limited conversions; primarily 1945"

theaters:
  european: "Anzio, Normandy, Southern France, Mediterranean"
  pacific: "Guadalcanal through Okinawa; every major operation"

casualties:
  note: "Many LCI vessels damaged or sunk; particularly LCI(G) and LCI(R) operating close to beaches"
  example: "LCI(G)-726: 2 KIA, several WIA at Saipan"
```

### Design Evolution Impact
```yaml
lessons_learned:
  side_ramps: "LCI(L)-1 to 350 proved vulnerable; troops exposed during disembarkation"
  bow_ramp: "LCI(L)-351+ enclosed bow ramp significantly improved survivability"
  fire_support: "Base LCI(L) insufficient for assault; led to LCI(G) and LCI(R) conversions"
  specialized_roles: "Single hull design adapted to multiple mission profiles"

post_war_influence:
  - "Demonstrated value of specialized amphibious fire support craft"
  - "Influenced development of post-war amphibious warfare vessels"
  - "Lessons applied to Korean War and Vietnam War riverine operations"
  - "Template for modern amphibious assault ships and fire support craft"
```

### Operational Achievements
```yaml
major_contributions:
  d_day: "Critical role delivering troops to Normandy beaches under fire"
  pacific_campaign: "Essential fire support for every island assault 1943-1945"
  tarawa_to_okinawa: "Evolution from transport to fire support demonstrated adaptability"
  combined_arms: "Integration with naval gunfire, air support, and ground forces"

effectiveness_metrics:
  troop_delivery: "200 troops per vessel directly to hostile beaches"
  fire_support: "LCI(G)/LCI(R) provided close support unavailable from larger ships"
  rocket_capability: "504 rockets per LCI(R) in single saturation run"
  survivability: "Bow ramp design (LCI-351+) improved troop protection"
```

---

## Technical Notes

### Landing Craft Size Comparison
```yaml
lcvp:
  length: 36 feet
  capacity: 36 troops
  note: "Small, ship-to-shore transport; no ocean transit capability"

lci:
  length: 158.5 feet
  capacity: 200 troops
  note: "Ocean-going; independent transit from rear bases"

lst:
  length: 328 feet
  capacity: 163 troops + 20 tanks
  note: "Large landing ship; cargo and vehicle focus"

conclusion: "LCI filled gap between LCVP tactical transport and LST strategic sealift"
```

### Construction Details
```yaml
hull:
  material: "1/4 inch steel plate throughout"
  construction: "Welded steel construction"
  design: "Shallow draft for beach landing capability"

propulsion:
  manufacturer: "General Motors / Detroit Diesel"
  model: "6-71 'Quad' diesel engines"
  configuration: "Two banks of four engines (8 total)"
  advantages: "Reliable, fuel-efficient, readily available parts"

ramp_mechanisms:
  lci_1_to_350: "Hydraulic side ramps (port and starboard)"
  lci_351_plus: "Hydraulic bow doors with extending ramp"
  capacity: "Designed for rapid troop deployment"
```

### Limitations and Challenges
```yaml
seaworthiness:
  draft: "Shallow draft limited rough sea capability"
  stability: "Top-heavy when fully loaded"
  sea_state: "Best operation in moderate seas"

landing_operations:
  beach_gradient: "Required suitable beach gradient for ramp deployment"
  tide: "Tide-dependent for optimal landing"
  obstacles: "Vulnerable to beach obstacles and mines"

vulnerability:
  armor: "Minimal armor protection (1/4 inch hull plating)"
  exposure: "Close beach approach exposed vessels to direct fire"
  casualties: "Particularly LCI(G) and LCI(R) operating within small arms range"
```

---

## Sources and Research Notes

### Primary Sources
```yaml
official_documentation:
  - "Dictionary of American Naval Fighting Ships (DANFS)"
  - "NavSource Naval History - LCI Photo Archive"
  - "US Navy Bureau of Ships construction records"
  - "Naval History and Heritage Command ship histories"

historical_records:
  - "Pacific War Online Encyclopedia - LCI Class entries"
  - "USS Landing Craft Infantry National Association (USSLCI.org)"
  - "World War II Database - LCI(L) specifications"
  - "HyperWar: US Navy Landing Ships/Craft, 1940-1945"
```

### Technical References
```yaml
specifications:
  - "Naval Encyclopedia - Landing Craft Infantry (LCI) 1942"
  - "MilitaryFactory.com - LCI(L) technical data"
  - "GlobalSecurity.org - LCI specifications"
  - "D-Day Overlord - Landing Craft technical details"

combat_operations:
  - "American Amphibious Gunboats in World War II (Erenow.org)"
  - "Naval History Magazine - Rocket Ships article (June 2021)"
  - "USNI Proceedings - A Tale of Two Invasions"
  - "Pacific Wrecks - Individual vessel histories"
```

### Research Quality Notes
```yaml
specification_verification:
  displacement: "Cross-referenced multiple sources; 216-389 tons confirmed"
  dimensions: "158.5 ft x 23.25 ft consistent across sources"
  propulsion: "1,600 BHP Detroit Diesel confirmed"
  troop_capacity: "188-200 troops (sources vary slightly)"
  fuel_capacity: "110-130 tons depending on variant"

variant_armament:
  lci_g: "40mm and 20mm guns confirmed; rocket numbers vary slightly"
  lci_r: "504 rocket capacity most common figure; some sources indicate higher"
  lci_m: "3 x 4.2-inch mortars consistently reported"

conversion_numbers:
  note: "Exact total conversions for LCI(G), LCI(R), LCI(M) not definitively documented"
  evidence: "Multiple flotillas and individual vessels confirmed in combat records"
  estimate: "Hundreds of LCI(G) and LCI(R) conversions based on operational records"
```

---

## Glossary
```yaml
aa: "Anti-aircraft"
bhp: "Brake horsepower"
danfs: "Dictionary of American Naval Fighting Ships"
lci: "Landing Craft Infantry"
lci_g: "Landing Craft Infantry (Gunboat)"
lci_l: "Landing Craft Infantry (Large)"
lci_m: "Landing Craft Infantry (Mortar)"
lci_r: "Landing Craft Infantry (Rocket)"
lcvp: "Landing Craft, Vehicle, Personnel (Higgins Boat)"
lst: "Landing Ship, Tank"
mk: "Mark (designation for weapon systems)"
nm: "Nautical miles"
usn: "United States Navy"
```

---

**Document Version**: 1.0
**Last Updated**: 2025-10-23
**Research Status**: Complete - Comprehensive technical documentation for all US Navy LCI variants based on authoritative historical sources
