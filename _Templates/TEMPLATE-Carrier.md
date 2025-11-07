# [Class Name] Aircraft Carriers

```yaml
---
class_name: [Full Class Name with designation, e.g., "Yorktown-Class-CV"]
hull_numbers: [Hull numbers, e.g., "CV-5, CV-6, CV-8"]
ships_built: [Number of ships completed]
commissioned: [Year range]
decommissioned: [Year range with reason]
era: [Era designation, e.g., "Pre-WWII Fleet Carriers", "WWII Essex-Class", "Supercarriers"]
generation: [Generation number for tech tree progression]
type: Aircraft Carrier (CV)

# Specifications
displacement_standard: [Tons]
displacement_full: [Tons at full load]
length_ft: [Feet, overall length]
beam_ft: [Feet, can specify "flight deck" vs "waterline" if different]
draft_ft: [Feet]
crew: [Number, total including air wing if applicable]

# Performance
speed_design: [Knots, design speed]
speed_max: [Knots, maximum speed if different]
propulsion_type: [Type of turbines/engines, e.g., "Geared steam turbines"]
propulsion_shp: [Shaft horsepower]
shafts: [Number of propeller shafts]
fuel_type: [Usually "Oil"]
range: [Range description, e.g., "12500 nm at 15 knots"]

# Air Group
aircraft: [Number of aircraft carried]

# Armament
guns: "[Defensive armament, e.g., '8× 5-inch/38 cal dual-purpose']"

# Relationships
predecessor: "[[Previous-Class]]"
successor: "[[Next-Class]]"

# Innovation
firsts:
  - [First significant innovation or achievement]
  - [Second innovation]
  - [Third innovation]
  - [Notable operational achievements]
  - [Maximum 5-10 concise bullets]

# Tags
tags: [carrier, class-name, hull-numbers, year, key-battles, notable-features]
---
```

**[Brief One-Line Summary]** - [Ship names]. [Key characteristic]. [Number] ships. [Key specs and achievements in 1-2 sentences].

**Key Specs:** [displacement] | [length] | [speed] | [aircraft capacity] | [propulsion] | [armament]

**Innovation:** [2-3 sentence paragraph highlighting key innovations and design philosophy]

**Ships:**
- **[Ship Name (Hull)]** - [Brief fate/achievement]
- **[Ship Name (Hull)]** - [Brief fate/achievement]

**Service:** [2-4 sentence summary of operational history, major battles, ultimate fates. Keep concise but informative.]

---
**Tree:** [[00_Carrier_Research_Tree]] | **Previous:** [[Previous-Class]] | **Next:** [[Next-Class]]

#[repeat-key-tags-from-yaml]

