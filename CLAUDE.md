# CLAUDE.md

Project guidance for Claude Code when working with this repository.

## Project Overview

**Name**: Fathoms Deep / WOS Game Design Document
**Type**: Unified GDD with integrated naval warfare research
**Format**: Obsidian vault (~6,000 markdown files)

## Repository Structure

```
ship-research-trees/
├── GDD/                          # Game Design Document (unified)
│   ├── 00-Meta/                  # Project overview, status
│   ├── 01-Core-Concepts/         # Vision, audience, mechanics
│   ├── 02-Core-Gameplay/         # Crew, missions, physics
│   ├── 03-Combat-Systems/        # Combat, ballistics, detection
│   ├── 04-Ships/                 # Ship data + customization (842 files)
│   │   ├── USA/                  # 247 ships
│   │   ├── Germany/              # 223 ships
│   │   ├── Great-Britain/        # 188 ships
│   │   ├── Japan/                # 160 ships
│   │   └── Overviews/            # Nation summaries
│   ├── 05-Aircraft/              # Aircraft data + modules (437 files)
│   ├── 06-Weapons/               # Weapons data + modules (4,100+ files)
│   │   ├── Naval-Weapons/        # Guns, torpedoes, missiles
│   │   └── Aircraft-Weapons/     # Air-launched ordnance
│   ├── 07-Economy/               # Resources, trading (257 files)
│   ├── 08-UI-Systems/            # Controls, menus, settings
│   ├── 09-Multiplayer/           # Networking, guilds, chat
│   ├── 10-World-Design/          # Map, biomes, weather
│   ├── 11-Factions/              # Nations, diplomacy
│   ├── 12-Progression/           # Crew, research unlocks
│   ├── 13-Technical/             # Tech stack, performance
│   ├── 14-Art-Audio/             # Visual design, audio
│   ├── Modules/                  # Ship modules (Engines, Bridge, Support)
│   ├── Scripts/                  # Unity C# scripts
│   ├── Scripts-Reference/        # Implementation docs
│   └── Canvases/                 # Obsidian visual diagrams
├── _Templates/                   # Markdown templates (15 files)
├── _Reports/                     # Audit/analysis reports
├── _Archive/                     # Historical backups
└── README.md
```

## Content Statistics

| Section | Files | Description |
|---------|-------|-------------|
| 04-Ships | 842 | Historical ships by nation |
| 05-Aircraft | 437 | Aircraft specifications |
| 06-Weapons | 4,100+ | Naval guns, turrets, torpedoes, missiles |
| 07-Economy | 257 | Game economy resources |
| Other GDD | ~400 | Game design documentation |
| **Total** | ~6,000 | |

## File Format

All markdown files use YAML frontmatter:
```yaml
---
designation: Iowa-Class
nation: USA
type: Battleship
commissioned: 1943
tags: [battleship, fast-battleship, wwii]
---
```

## Obsidian Conventions

- **Ship links**: `[[/GDD/04-Ships/USA/Battleships/Iowa-Class.md|Iowa Class]]`
- **Aircraft links**: `[[/GDD/05-Aircraft/USA/Naval-Fighter/F4U-Corsair.md|F4U Corsair]]`
- **Weapon links**: `[[/GDD/06-Weapons/Naval-Weapons/Naval-Guns/...]]`

## Related Project

This GDD feeds into **WOS2.3_V2** (Waves of Steel), a Unity naval MMO:
- Repository: `AsloWaves/WOS2.3_V2`
- Engine: Unity 6000.0.55f1
- Networking: Mirror (server-authoritative)

## Key Entry Points

- Project overview: `GDD/00-Meta/`
- Ship database: `GDD/04-Ships/`
- Weapon systems: `GDD/06-Weapons/`
- Economy design: `GDD/07-Economy/`
