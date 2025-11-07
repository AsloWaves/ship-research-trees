# [Class Name] Submarines

```yaml
---
class_name: [Full Class Name]
hull_numbers: [Hull numbers or naming system]
ships_built: [Number of boats completed]
commissioned: [Year range]
decommissioned: [Year range with reason]
era: [Era designation]
generation: [Generation number for tech tree progression]
type: [Submarine type: "Submarine", "Fleet Submarine", "Coastal Submarine", "Midget Submarine", "Nuclear Submarine (SSN)", "Ballistic Missile Submarine (SSBN)"]

# Specifications
displacement_surfaced: [Tons surfaced]
displacement_submerged: [Tons submerged]
length_ft: [Feet, overall length]
beam_ft: [Feet]
draft_ft: [Feet]
crew: [Number]

# Performance
speed_surfaced: [Knots surfaced]
speed_submerged: [Knots submerged]
propulsion_surfaced: [Diesel engines or other]
propulsion_submerged: [Electric motors, nuclear reactor, etc.]
propulsion_hp_surfaced: [Horsepower surfaced]
propulsion_hp_submerged: [Horsepower submerged]
range_surfaced: [Range description surfaced]
range_submerged: [Range description submerged]
test_depth: [Operating depth in feet]
max_depth: [Maximum depth if known]

# Armament
torpedo_tubes: "[Number and location, e.g., '6× 21-inch bow tubes']"
torpedoes_carried: [Total torpedo capacity]
deck_gun: "[Deck gun if applicable, or 'None']"
missiles: "[Missiles for modern subs, or 'None']"

# Technology
fire_control: [Fire control/targeting systems]
sonar_systems: [Sonar equipment]
other_systems: [Other notable technology]

# Relationships
predecessor: "[[Previous-Class]]"
successor: "[[Next-Class]]"
contemporary: "[[Contemporary-Submarine]]"

# Innovation
firsts:
  - [First significant innovation or achievement]
  - [Second innovation]
  - [Third innovation]
  - [Maximum 5-10 concise bullets]

# Tags
tags: [submarine, class-name, year, nation, key-features]
---
```

**[Brief One-Line Summary]** - Built [years]. [Key specs]. [Most notable characteristic or achievement].

**Key Features:** [3-5 most important features separated by |]

**Ships:** [List of boat names or general description if large class]

**Service:** [2-4 sentence summary of operational history, combat successes, ultimate fates. Keep concise but informative.]

---
**Tree:** [[00_Submarine_Research_Tree]] | **Previous:** [[Previous-Class]] | **Next:** [[Next-Class]]

#[repeat-key-tags-from-yaml]

