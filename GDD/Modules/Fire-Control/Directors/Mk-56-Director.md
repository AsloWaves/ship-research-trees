# Mk 56 Gun Fire Control System

---
module_id: FCS-DIR-006
name: Mk 56 GFCS
category: fire-control
type: anti-aircraft
era: 1945
nation: USA
manufacturer: General Electric

# Physical
weight_kg: 2720
crew: 2
armored: false
armor_mm: 0

# Radar
radar_integrated: Mk 35
tracking: automatic
range_m: 18000

# Performance
elevation_range: -15 to +85
train_rate_deg_s: 40
elevation_rate_deg_s: 30
stabilization: 3-axis
target_types: [aircraft, surface]

# Relationships
predecessor: "[[Mk-37-Director]]"
successor: "[[Mk-68-Director]]"

tags: [director, anti-aircraft, usa, late-wwii, korea, automatic]
---

**Radar-Only Director** - The Mk 56 represented the next generation of AA fire control. Fully radar-directed with no optical backup required. Automatic tracking eliminated human lag. Entered service late WWII, saw extensive Korea/Vietnam use. First truly "blind fire" system.

**Key Specs:** 2,720 kg | Mk 35 radar | -15° to +85° | 40°/sec train | Auto-tracking | 2 crew

**Features:**
- Automatic tracking: Radar locks target, no manual tracking needed
- Minimal crew: 2 operators vs 6 for Mk 37
- Faster slew: 40°/sec vs 30°/sec for Mk 37
- All-weather: No optical dependency

**Limitations:** No optical backup (early models). Radar-dependent. Late WWII entry limited combat data.

**Combat Record:** Korea (1950-53) - shore bombardment fire control. Taiwan Strait (1958) - AA defense. Vietnam (1964-73) - coastal fire support.

**Ships:** Post-war destroyers (Gearing FRAM), cruisers, carriers. Standard cold war AA director.

---
**Tree:** [[_FCS-Index]] | **Predecessor:** [[Directors/Mk-37-Director]] | **Radar:** [[/GDD/Modules/Support/Detection-Radar/Radar-FC-Mk35]]

#director #anti-aircraft #usa #late-wwii #korea #automatic
