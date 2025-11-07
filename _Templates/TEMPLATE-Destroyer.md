# [Class Name] Destroyers

```yaml
---
class_name: [Full Class Name]
hull_numbers: [Hull numbers or ship names]
ships_built: [Number of ships completed]
commissioned: [Year range]
decommissioned: [Year range with reason]
era: [Era designation]
generation: [Generation number for tech tree progression]
type: [Destroyer type: "Destroyer", "Destroyer-Modern", "Torpedo Boat Destroyer", "Guided Missile Destroyer (DDG)"]

# Specifications
displacement_standard: [Tons]
displacement_full: [Tons at full load]
length_ft: [Feet, overall length]
beam_ft: [Feet]
draft_ft: [Feet]
crew: [Number]

# Performance
speed_design: [Knots, design speed]
speed_trial: [Knots, trial speed if significantly different]
propulsion_type: [Type of turbines/engines]
propulsion_shp: [Shaft horsepower]
shafts: [Number of propeller shafts]
fuel_type: [Usually "Oil"]
range: [Range description]

# Armament
main_guns: "[Primary gun armament]"
aa_guns: "[Anti-aircraft armament]"
torpedo_tubes: "[Torpedo armament]"
depth_charges: "[ASW armament if applicable]"
missiles: "[Guided missiles for modern destroyers, or 'None']"

# Technology
fire_control: [Fire control systems]
radar_systems: [Radar systems]
sonar_systems: [Sonar for ASW if applicable]

# Relationships
predecessor: "[[Previous-Class]]"
successor: "[[Next-Class]]"
contemporary: "[[Contemporary-Ship]]"

# Innovation
firsts:
  - [First significant innovation or achievement]
  - [Second innovation]
  - [Third innovation]
  - [Maximum 5-10 concise bullets]

# Tags
tags: [destroyer, class-name, year, nation, key-features]
---
```

**[Brief One-Line Summary]** - Built [years]. [Key specs]. [Most notable characteristic].

**Key Features:** [3-5 most important features separated by |]

**Ships:** [List of ship names or general description if many ships]

**Service:** [2-4 sentence summary of operational history, major deployments, combat record. Keep concise but informative.]

---
**Tree:** [[00_Destroyer_Research_Tree]] | **Previous:** [[Previous-Class]] | **Next:** [[Next-Class]]

#[repeat-key-tags-from-yaml]

