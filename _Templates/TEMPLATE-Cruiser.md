# [Class Name] Cruisers

```yaml
---
class_name: [Full Class Name]
hull_numbers: [Hull numbers or ship names]
ships_built: [Number of ships completed]
commissioned: [Year range]
decommissioned: [Year range with reason]
era: [Era designation]
generation: [Generation number for tech tree progression]
type: [Cruiser type: "Heavy Cruiser", "Light Cruiser", "Battle Cruiser", "Armored Cruiser", "Protected Cruiser"]

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
fuel_type: [Usually "Oil" or "Coal"]
range: [Range description]

# Armament
main_guns: "[Primary armament]"
secondary_guns: "[Secondary guns if applicable]"
aa_guns: "[Anti-aircraft armament]"
torpedo_tubes: "[Torpedo armament or 'None']"
armor_belt: [Armor thickness if applicable, or "None" for unarmored cruisers]
armor_deck: [Deck armor if applicable]
armor_turrets: [Turret armor if applicable]

# Technology
fire_control: [Fire control systems]
radar_systems: [Radar if applicable]
other_systems: [Other notable technology]

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
tags: [cruiser, cruiser-type, class-name, year, nation, key-features]
---
```

**[Brief One-Line Summary]** - Built [years]. [Key specs]. [Most notable characteristic or achievement].

**Key Features:** [3-5 most important features separated by |]

**Ships:** [List of ship names, can include brief individual fates]

**Service:** [2-4 sentence summary of operational history, major deployments, ultimate fates. Keep concise but informative.]

---
**Tree:** [[00_Cruiser_Research_Tree]] | **Previous:** [[Previous-Class]] | **Next:** [[Next-Class]]

#[repeat-key-tags-from-yaml]

