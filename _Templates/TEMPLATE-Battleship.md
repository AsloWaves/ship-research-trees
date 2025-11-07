# [Class Name] Battleships

```yaml
---
class_name: [Full Class Name]
hull_numbers: [Hull numbers or "None (naming convention)"]
ships_built: [Number of ships completed]
commissioned: [Year range, e.g., "1940-1941"]
decommissioned: [Year range with reason, e.g., "1941-1944 (sunk/scrapped)"]
era: [Era designation, e.g., "WWII", "Pre-Dreadnought", "Dreadnought"]
generation: [Generation number for tech tree progression]
type: Battleship

# Specifications
displacement_standard: [Tons, can be range like "41700-42900"]
displacement_full: [Tons at full load]
length_ft: [Feet, overall length]
beam_ft: [Feet]
draft_ft: [Feet, can be range]
crew: [Number, can be range like "1673-1968"]

# Performance
speed_design: [Knots, design speed]
speed_trial: [Knots, trial speed if different from design]
propulsion_type: [Type of turbines/engines, e.g., "Brown-Boveri geared steam turbines"]
propulsion_shp: [Shaft horsepower]
shafts: [Number of propeller shafts]
fuel_type: [Usually "Oil" or "Coal"]
range: [Range in nm at specific speed, e.g., "8870 nm at 19 knots"]

# Armament
main_guns: "[Number and caliber, e.g., '8× 38cm (15-inch) SK C/34']"
secondary_guns: "[Number and caliber]"
tertiary_guns: "[AA and smaller guns]"
torpedo_tubes: "[If applicable, or 'None']"
armor_belt: [Thickness in mm, can include type like "320mm Krupp cemented"]
armor_deck: [Thickness in mm, can be range]
armor_turrets: [Thickness in mm, can specify "face/sides"]
armor_conning_tower: [Thickness in mm]

# Technology
fire_control: [Fire control systems, radar systems]
engine_type: [Detailed engine description]
boiler_type: [Boiler specifications]
boiler_count: [Number of boilers]
armor_type: [Type of armor steel used]

# Relationships
predecessor: "[[Previous-Class]]"
successor: "[[Next-Class]]"
contemporary: "[[Contemporary-Foreign-Ship]]"

# Innovation
firsts:
  - [First significant innovation or achievement]
  - [Second innovation]
  - [Third innovation]
  - [Notable combat achievements]
  - [Technical milestones]
  - [Maximum 5-10 concise bullets focusing on most significant achievements]

# Tags
tags: [battleship, class-name, year, key-battles, nation-specific-tags, notable-features]
---
```

**[Brief One-Line Summary]** - Built [years]. [Key specs summary]. [Most notable achievement or characteristic in 1-2 sentences].

**Key Features:** [3-5 most important features separated by |]

**Ships:** [List of ship names, can include individual fates if brief]

**Service:** [2-4 sentence summary of operational history, major battles, ultimate fate. Keep concise but informative.]

---
**Tree:** [[00_Battleship_Research_Tree]] | **Previous:** [[Previous-Class]] | **Next:** [[Next-Class]]

#[repeat-key-tags-from-yaml]

