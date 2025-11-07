# US Navy WWII-Era Transport and Cargo Ship Classes

Comprehensive specifications for US Navy World War II transport (AP/APA) and cargo (AK/AKA) ship classes.

---

## 1. Admiral W.S. Benson-Class (AP-120 class)
**Type:** Transport (AP) | **Hull Type:** MC P2-SE2-R1 (C3 conversion)

### Class Overview
- **Lead Ship:** USS Admiral W.S. Benson (AP-120)
- **Total Built:** 8 ships
- **Builder:** Bethlehem Steel, Alameda, California
- **Commissioned:** 1944-1945
- **Significance:** Converted C3 cargo ships for Army transport service; all named for US Navy admirals; later converted for Army use and renamed for generals

### Complete Ship List
1. AP-120 - USS Admiral W.S. Benson (1944)
2. AP-121 - USS Admiral W.L. Capps (1944)
3. AP-122 - USS Admiral R.E. Coontz (1944)
4. AP-123 - USS Admiral E.W. Eberle (1944)
5. AP-124 - USS Admiral C.F. Hughes (1944)
6. AP-125 - USS Admiral H.T. Mayo (1944)
7. AP-126 - USS Admiral Hugh Rodman (1944)
8. AP-127 - USS Admiral W.S. Sims (1945)

### Specifications
```yaml
displacement_standard: 9676
displacement_full: 20120
length_ft: 608.9
length_waterline_ft: 573.0
beam_ft: 75.5
draft_ft: 26.5
crew: ~450
speed_design: 19
propulsion_type: turbo-electric
propulsion_shp: 18000
propulsion_screws: 2
propulsion_details: G.E. turbo-electric drive
armament_main: 4x 5"/38
armament_secondary: 4x 1.1" quad, 16-20x 20mm
troop_capacity: ~4500
cargo_capacity_tons: ~8000
service_notes: |
  - Converted from C3 cargo ship design
  - Divided machinery spaces for safety
  - Transferred to Army 1946 and renamed for generals
  - Assigned to MSTS 1950 with civilian crews
predecessor: None (conversion program)
successor: None (post-war conversions)
```

---

## 2. Doyen-Class (APA-1 class)
**Type:** Attack Transport (APA) | **Hull Type:** Maritime Commission Design 1029

### Class Overview
- **Lead Ship:** USS Doyen (APA-1)
- **Total Built:** 2 ships
- **Builder:** Consolidated Steel Corporation, Los Angeles, California
- **Commissioned:** 1943
- **Significance:** First dedicated attack transports; converted from commercial standards with military features built in during construction; named after USMC generals

### Complete Ship List
1. APA-1 - USS Doyen (22 May 1943)
2. APA-11 - USS Feland (22 May 1943)

### Specifications
```yaml
displacement_standard: 4351
displacement_full: 6710
length_ft: 414.5
length_waterline_ft: 405.0
beam_ft: 56.0
draft_ft: 18.5
crew: 456
speed_design: 19
propulsion_type: geared turbine
propulsion_shp: 8000
propulsion_screws: 2
propulsion_details: Westinghouse turbines
armament_main: 4x 3"/50
armament_secondary: 2x 40mm twin, 10x 20mm
troop_capacity: 710 (60 officers, 650 enlisted)
cargo_capacity_cubic_ft: 75000
landing_craft: LCVPs and LCMs
service_notes: |
  - Built on commercial standards with military conversion features
  - Unusually shallow 18-foot draft
  - Inspired by British "Glen" liner conversions
  - Originally classified AP-2, reclassified APA-1 on 1 Feb 1943
predecessor: None (first dedicated APA class)
successor: Harris-Class
```

---

## 3. Harris-Class (APA-2 class)
**Type:** Attack Transport (APA) | **Hull Type:** Shipping Board Design 1029 ("535 class")

### Class Overview
- **Lead Ship:** USS Harris (APA-2)
- **Total Built:** 8 ships
- **Builder:** Various (Bethlehem Steel, New York Shipbuilding)
- **Commissioned:** 1919-1922 (original); 1941-1943 (as APA)
- **Significance:** WWI-era transports converted to early attack transports; saw action in all major WWII theaters

### Complete Ship List
1. APA-2 - USS Harris
2. APA-3 - USS Zeilin
3. APA-12 - USS Leonard Wood
4. APA-13 - USS Joseph T. Dickman
5. APA-14 - USS Hunter Liggett
6. APA-15 - USS Henry T. Allen
7. APA-16 - USS J. Franklin Bell
8. APA-17 - USS American Legion

### Specifications
```yaml
displacement_standard: 13529
displacement_full: 21900
length_ft: 535.2
beam_ft: 72.5
draft_ft: 31.25
crew: 472
speed_design: 17.2
propulsion_type: geared turbine
propulsion_shp: 12000
propulsion_screws: 2
propulsion_details: 8 Yarrow boilers, 2 Curtis turbines
armament_main: None
armament_secondary: 6x 40mm, 10x 20mm twin
troop_capacity: 1650
cargo_capacity_tons: 400
landing_craft: 33x LCVP, 2-4x LCM(3)
service_notes: |
  - Originally WWI Shipping Board "535 class" (535 feet length)
  - Built 1919-1922, converted to APA 1941-1943
  - Saw action in Mediterranean, Atlantic, and Pacific theaters
  - Oldest ships used as attack transports in WWII
predecessor: Doyen-Class
successor: Crescent City-Class
```

---

## 4. Crescent City-Class (APA-21 class)
**Type:** Attack Transport (APA) | **Hull Type:** C3-P/C3-Delta

### Class Overview
- **Lead Ship:** USS Crescent City (APA-21)
- **Total Built:** 4 ships
- **Builder:** Bethlehem Steel, Sparrows Point, Maryland
- **Commissioned:** 1941-1942
- **Significance:** First C3-based attack transports; earned 33 battle stars collectively; USS Crescent City traveled 160,000 miles and transported 90,000 men

### Complete Ship List
1. APA-21 - USS Crescent City (10 Oct 1941)
2. APA-28 - USS Charles Carroll (Aug 1942)
3. APA-31 - USS Monrovia (Sep 1942)
4. APA-32 - USS Calvert (Dec 1942)

### Specifications
```yaml
displacement_standard: 8889
displacement_full: 14247
length_ft: 491.0
length_waterline_ft: 465.0
beam_ft: 65.5
draft_ft: 25.7
crew: ~450
speed_design: 18-19
propulsion_type: geared turbine
propulsion_shp: ~8500
propulsion_screws: 1
propulsion_details: C3 standard machinery
armament_main: 3-4x 3"/50 or 1x 5"/38 (varied by ship)
armament_secondary: Various 40mm and 20mm (no two ships identical)
troop_capacity: 1200-1500
cargo_capacity_tons: 2300-2700
landing_craft: LCVPs and LCMs
service_notes: |
  - Based on C3-P/C3-Delta merchant hull
  - Originally classified AP-40, reclassified APA-21 on 1 Feb 1943
  - No two ships had identical armament configurations
  - USS Crescent City earned 10 battle stars, shot down 8 Japanese aircraft
  - Served from Guadalcanal through Okinawa
  - Class earned 33 battle stars and 2 Navy Unit Commendations
predecessor: Harris-Class
successor: Arthur Middleton-Class
```

---

## 5. Arthur Middleton-Class (APA-25 class)
**Type:** Attack Transport (APA) | **Hull Type:** C3-P&C (Passenger and Cargo)

### Class Overview
- **Lead Ship:** USS Arthur Middleton (APA-25)
- **Total Built:** 3 ships
- **Builder:** Ingalls Shipbuilding, Pascagoula, Mississippi
- **Commissioned:** 1942
- **Significance:** Larger C3-based transports with enhanced passenger/cargo capacity; all named after American colonial leaders

### Complete Ship List
1. APA-25 - USS Arthur Middleton (7 Sep 1942)
2. APA-26 - USS Samuel Chase (13 Jun 1942)
3. APA-27 - USS George Clymer (15 Jun 1942)

### Specifications
```yaml
displacement_standard: 10812
displacement_full: 18000
length_ft: 489.0
length_waterline_ft: 465.0
beam_ft: 69.5
draft_ft: 27.3
crew: 499
speed_design: 18.4
propulsion_type: geared turbine
propulsion_shp: 8500
propulsion_screws: 1
propulsion_details: G.E. turbine
armament_main: 1x 5"/51
armament_secondary: 4x 3"/50, 8x 20mm (1942); 4x 3"/50, 2x 40mm twin, 10-14x 20mm (1943-45)
troop_capacity: ~1500
cargo_capacity_tons: ~2500
landing_craft: LCVPs and LCMs
service_notes: |
  - Based on C3-P&C (Passenger and Cargo) hull type
  - Originally classified AP-55, reclassified APA-25 on 1 Feb 1943
  - Built as African Comet/American Banker-class merchant ships
  - Larger and more capable than earlier Crescent City-class
  - Enhanced passenger accommodations and cargo capacity
predecessor: Crescent City-Class
successor: Bayfield-Class
```

---

## 6. Bayfield-Class (APA-33 class)
**Type:** Attack Transport (APA) | **Hull Type:** C3-S-A2

### Class Overview
- **Lead Ship:** USS Bayfield (APA-33)
- **Total Built:** 34 ships
- **Builders:** Ingalls Shipbuilding (20), Western Pipe & Steel (14)
- **Commissioned:** 1943-1944
- **Significance:** First APA class built in substantial numbers; second most numerous APA class after Haskell-class; many served through Korean and Vietnam wars

### Complete Ship List
1. APA-33 - USS Bayfield
2. APA-34 - USS Bolivar
3. APA-35 - USS Callaway
4. APA-36 - USS Cambria
5. APA-37 - USS Cavalier
6. APA-38 - USS Chilton
7. APA-39 - USS Clay
8. APA-40 - USS Custer
9. APA-41 - USS Du Page
10. APA-42 - USS Elmore
11. APA-43 - USS Fayette
12. APA-44 - USS Fremont
13. APA-45 - USS Henrico
14. APA-46 - USS Knox
15. APA-47 - USS Lamar
16. APA-48 - USS Leon
17. APA-92 - USS Alpine
18. APA-93 - USS Barnstable
19. APA-95 - USS Burleigh
20. APA-96 - USS Cecil
21. APA-99 - USS Dade
22. APA-100 - USS Mendocino
23. APA-101 - USS Montour
24. APA-102 - USS Riverside
25. APA-104 - USS Westmoreland
26. APA-106 - USS Gladwin/Hansford
27. APA-107 - USS Goodhue
28. APA-108 - USS Goshen
29. APA-109 - USS Grafton
30. APA-110 - USS Griggs
31. APA-111 - USS Grundy
32. APA-112 - USS Guilford
33. APA-113 - USS Sitka
34. APA-114 - USS Hamblen
35. APA-115 - USS Hampton
36. APA-116 - USS Hanover

### Specifications
```yaml
displacement_standard: 8100
displacement_full: 16100
length_ft: 492.0
beam_ft: 69.5
draft_ft: 23.25
crew: ~575
speed_design: 18.4
propulsion_type: geared turbine
propulsion_shp: ~8500
propulsion_screws: 1
propulsion_details: C3-S-A2 standard machinery
armament_main: 2x 5"/38 (1 fore, 1 aft)
armament_secondary: 2-4x 40mm twin (or 2x 1.1" quad early), 2x 40mm single, 18x 20mm
troop_capacity: ~1500
cargo_capacity_tons: ~2000
landing_craft: 15-33x LCVP, 2-4x LCM
service_notes: |
  - Based on C3-S-A2 merchant hull design
  - First class built in substantial numbers (34 ships)
  - Originally designated AP-78 through AP-101, redesignated APA
  - Many ships served in Korean and Vietnam wars
  - Second most numerous APA class after Haskell-class
  - Built 1942-1944 at two shipyards
predecessor: Arthur Middleton-Class
successor: Haskell-Class (117 ships)
```

---

## 7. Artemis-Class (AKA-21 class)
**Type:** Attack Cargo Ship (AKA) | **Hull Type:** S4-SE2-BE1

### Class Overview
- **Lead Ship:** USS Artemis (AKA-21)
- **Total Built:** 32 ships (AKA-21 through AKA-52)
- **Builder:** Walsh-Kaiser Company, Cranston and Providence, Rhode Island
- **Commissioned:** 1944-1945
- **Significance:** Shallow-draft attack cargo ships; carried combat-loaded cargo and landing craft; distinctive lower main deck aft; 2 ships converted to survey ships (AGS)

### Complete Ship List
1. AKA-21 - USS Artemis
2. AKA-22 - USS Athene
3. AKA-23 - USS Aurelia
4. AKA-24 - USS Birgit
5. AKA-25 - USS Circe
6. AKA-26 - USS Corvus
7. AKA-27 - USS Devosa
8. AKA-28 - USS Hydrus
9. AKA-29 - USS Lacerta
10. AKA-30 - USS Lumen
11. AKA-31 - USS Medea
12. AKA-32 - USS Mellena
13. AKA-33 - USS Ostara
14. AKA-34 - USS Pamina/Tanner (later AGS-15)
15. AKA-35 - USS Polana
16. AKA-37 - USS Roxane
17. AKA-38 - USS Sappho
18. AKA-39 - USS Sarita
19. AKA-40 - USS Scania
20. AKA-41 - USS Selinur
21. AKA-42 - USS Sidonia
22. AKA-43 - USS Sirona
23. AKA-44 - USS Sylvania
24. AKA-45 - USS Tabora
25. AKA-46 - USS Troilus
26. AKA-47 - USS Turandot
27. AKA-48 - USS Valeria
28. AKA-49 - USS Vanadis
29. AKA-50 - USS Veritas
30. AKA-51 - USS Xenia
31. AKA-52 - USS Zenobia
32. (Note: AKA-36 skipped; USS Maury became AGS-16)

### Specifications
```yaml
displacement_standard: 4087
displacement_full: 6740
length_ft: 426.0
length_meters: 129.85
beam_ft: 58.0
beam_meters: 17.68
draft_ft: 15.0
draft_meters: 4.72
crew: 283
passenger_capacity: ~850
speed_design: 18
propulsion_type: geared turbine
propulsion_shp: 8000
propulsion_screws: 2
propulsion_details: 1x GE GD turbine, 2 boilers
armament_main: 1x 5"/38
armament_secondary: 4x 40mm twin, 10x 20mm
cargo_capacity_tons: 4450
landing_craft: 13x LCVP, 1x LCP(L)
service_notes: |
  - Based on S4-SE2-BE1 Maritime Commission design
  - Much shallower draft than other AKA classes
  - Lower main deck aft compared to other classes
  - Designed for amphibious cargo operations
  - Two ships converted to survey ships (AGS-15, AGS-16)
  - Built specifically for Pacific island operations
predecessor: None (first dedicated AKA class of this type)
successor: Tolland-Class
```

---

## 8. Tolland-Class (AKA-64 class)
**Type:** Attack Cargo Ship (AKA) | **Hull Type:** C2-S-AJ3

### Class Overview
- **Lead Ship:** USS Tolland (AKA-64)
- **Total Built:** 32 ships (AKA-64 through AKA-108, one cancelled)
- **Builder:** North Carolina Shipbuilding Company, Wilmington, North Carolina
- **Commissioned:** 1944-1945
- **Significance:** Larger capacity than Artemis-class; some ships served at Tokyo Bay surrender ceremony; many converted to LKA amphibious cargo ships for post-war service

### Complete Ship List
**First Series (AKA-64 through AKA-87):**
1. AKA-64 - USS Tolland
2. AKA-65 - USS Shoshone
3. AKA-66 - USS Southampton
4. AKA-67 - USS Starr
5. AKA-68 - USS Stokes
6. AKA-69 - USS Suffolk
7. AKA-70 - USS Tate
8. AKA-71 - USS Todd
9. AKA-72 - USS Caswell
10. AKA-73 - USS New Hanover
11. AKA-74 - USS Lenoir
12. AKA-75 - USS Alamance
13. AKA-76 - USS Torrance
14. AKA-77 - USS Towner
15. AKA-78 - USS Trego
16. AKA-79 - USS Trousdale
17. AKA-80 - USS Tyrrell
18. AKA-81 - USS Valencia
19. AKA-82 - USS Venango
20. AKA-83 - USS Vinton
21. AKA-84 - USS Waukesha
22. AKA-85 - USS Wheatland
23. AKA-86 - USS Woodford
24. AKA-87 - USS Duplin

**Second Series (AKA-101 through AKA-108):**
25. AKA-101 - USS Ottawa
26. AKA-102 - USS Prentiss
27. AKA-103 - USS Rankin (later LKA-103)
28. AKA-104 - USS Seminole (later LKA-104)
29. AKA-105 - USS Skagit (later LKA-105)
30. AKA-106 - USS Union (later LKA-106)
31. AKA-107 - USS Vermilion (later LKA-107)
32. AKA-108 - USS Washburn (later LKA-108)

**Cancelled:**
- AKA-109 - USS San Joaquin (cancelled 27 Aug 1945)

### Specifications
```yaml
displacement_standard: 8635
displacement_full: 13910
length_ft: 459.2
beam_ft: 63.0
draft_ft: 26.3
crew: 375
speed_design: 16.5
speed_economical: 12
propulsion_type: geared turbine
propulsion_shp: 6000
propulsion_screws: 1
propulsion_details: Single geared turbine
armament_main: 1x 5"/38
armament_secondary: 8x 40mm, 16x 20mm
cargo_capacity_dwt: 4450
landing_craft: 8x LCM(3), 15-16x LCVP, 1x LCP(L)
service_notes: |
  - Based on C2-S-AJ3 Maritime Commission design
  - Built in two series with different completion methods
  - AKA-64-75 and 101-104 completed at Charleston Navy Yard
  - AKA-76-87 and 105-108 towed to New York/Baltimore for completion
  - Nine AKAs present at Tokyo Bay surrender (2 Sep 1945)
  - Many converted to LKA designation for Korean/Vietnam service
  - 70 of 108 total AKAs decommissioned within one year of war's end
  - Larger cargo capacity than Artemis-class
predecessor: Artemis-Class
successor: Andromeda-Class (AKA-88 to AKA-100)
```

---

## Class Comparison Summary

### Transport Classes (AP/APA)
| Class | Type | Ships | Years | Displacement (tons) | Speed (kts) | Troops | Significance |
|-------|------|-------|-------|---------------------|-------------|--------|--------------|
| Admiral W.S. Benson | AP | 8 | 1944-45 | 9,676/20,120 | 19 | 4,500 | C3 conversions, later Army use |
| Doyen | APA | 2 | 1943 | 4,351/6,710 | 19 | 710 | First dedicated APAs |
| Harris | APA | 8 | 1919-22/41-43 | 13,529/21,900 | 17.2 | 1,650 | WWI ships converted |
| Crescent City | APA | 4 | 1941-42 | 8,889/14,247 | 18-19 | 1,200-1,500 | First C3-based APAs |
| Arthur Middleton | APA | 3 | 1942 | 10,812/18,000 | 18.4 | 1,500 | Enhanced C3-P&C |
| Bayfield | APA | 34 | 1943-44 | 8,100/16,100 | 18.4 | 1,500 | Primary APA class |

### Cargo Classes (AKA)
| Class | Type | Ships | Years | Displacement (tons) | Speed (kts) | Cargo (DWT) | Significance |
|-------|------|-------|-------|---------------------|-------------|-------------|--------------|
| Artemis | AKA | 32 | 1944-45 | 4,087/6,740 | 18 | 4,450 | Shallow draft design |
| Tolland | AKA | 32 | 1944-45 | 8,635/13,910 | 16.5 | 4,450 | Larger capacity, C2 hull |

---

## Technical Notes

### Hull Type Designations
- **C2-S-AJ3:** Maritime Commission Type C2 cargo ship, steam turbine, modified for attack cargo
- **C3-S-A2:** Maritime Commission Type C3 cargo ship, steam turbine, military conversion
- **C3-P&C:** Maritime Commission Type C3 passenger and cargo ship
- **C3-P/C3-Delta:** Maritime Commission Type C3 passenger or delta variant
- **S4-SE2-BE1:** Maritime Commission Type S4 ship, steam electric, modified design
- **MC P2-SE2-R1:** Maritime Commission passenger ship Type P2, steam electric, revised design
- **Design 1029:** Shipping Board WWI-era design (535-class)

### Armament Evolution
- **Early War (1941-42):** 3"/50 guns predominant, limited AA capability
- **Mid War (1943-44):** 5"/38 dual-purpose guns introduced, 40mm Bofors added
- **Late War (1944-45):** Enhanced AA with multiple 40mm and 20mm mounts

### Landing Craft Designations
- **LCVP:** Landing Craft, Vehicle, Personnel (Higgins boat)
- **LCM(3):** Landing Craft, Mechanized, Mark 3
- **LCP(L):** Landing Craft, Personnel, Large

### Conversion Programs
- **AP to APA:** Attack Transport redesignation occurred 1 February 1943 for most classes
- **AKA to LKA:** Amphibious Cargo Ship redesignation for Korean War-era service
- **AKA to AGS:** Survey Ship conversion (Artemis-class ships Tanner and Maury)
- **AP to Army Transport:** Admiral W.S. Benson class transferred 1946

---

## Service Record Highlights

### Battle Stars and Decorations
- **Crescent City-Class:** 33 battle stars collectively, 2 Navy Unit Commendations
- **USS Crescent City (APA-21):** 10 battle stars, 8 enemy aircraft shot down, 160,000 miles traveled, 90,000 troops transported
- **Tolland-Class Ships at Tokyo Bay Surrender:** USS Libra (AKA-12), USS Medea (AKA-31), USS Pamina (AKA-34), USS Sirona (AKA-43), USS Skagit (AKA-105), USS Todd (AKA-71), USS Tolland (AKA-64), USS Whiteside (AKA-90), USS Yancey (AKA-93)

### Major Campaigns
- **Atlantic/Mediterranean:** North Africa, Sicily, Salerno, Anzio, Southern France
- **Pacific:** Guadalcanal, Tarawa, Kwajalein, Saipan, Leyte, Iwo Jima, Okinawa
- **Post-War:** Korean War, Vietnam War (many Bayfield and Tolland-class ships)

### Fleet Reduction
- Within one year of war's end (1945-46), 70 of 108 AKAs were decommissioned
- Most transport classes reduced to National Defense Reserve Fleet by 1946-47
- Selected ships retained for Korean War reactivation
- Some Bayfield and Tolland-class ships served through Vietnam War era

---

## Sources
- DANFS (Dictionary of American Naval Fighting Ships)
- NavSource Online
- ShipScribe.com
- GlobalSecurity.org
- Naval History and Heritage Command
- Maritime Commission Records
- Pacific War Online Encyclopedia

---

*Last Updated: 2025-10-23*
*Database Version: 1.0*
