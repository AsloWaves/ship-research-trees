# Fathoms Deep - Game Design Document

Unified GDD and naval warfare research database for the Fathoms Deep / Waves of Steel naval MMO.

**Format**: Obsidian vault
**Files**: ~6,000 markdown documents
**Last Updated**: December 2025

---

## Repository Structure

```
ship-research-trees/
├── GDD/                          # Game Design Document
│   ├── 00-Meta/                  # Project overview & status
│   ├── 01-Core-Concepts/         # Vision, audience, mechanics
│   ├── 02-Core-Gameplay/         # Crew, missions, physics
│   ├── 03-Combat-Systems/        # Combat, ballistics, detection
│   ├── 04-Ships/                 # Ship database (842 files)
│   ├── 05-Aircraft/              # Aircraft database (437 files)
│   ├── 06-Weapons/               # Weapons database (4,100+ files)
│   ├── 07-Economy/               # Resources & trading (257 files)
│   ├── 08-UI-Systems/            # Controls, menus, settings
│   ├── 09-Multiplayer/           # Networking, guilds, chat
│   ├── 10-World-Design/          # Map, biomes, weather
│   ├── 11-Factions/              # Nations, diplomacy
│   ├── 12-Progression/           # Crew specialization, research
│   ├── 13-Technical/             # Tech stack, performance
│   ├── 14-Art-Audio/             # Visual design, audio
│   ├── Modules/                  # Ship modules (Engines, Bridge, Support)
│   ├── Scripts/                  # Unity implementation scripts
│   └── Canvases/                 # Visual design diagrams
├── _Templates/                   # Markdown templates
├── _Reports/                     # Audit reports
└── _Archive/                     # Historical backups
```

---

## Content Summary

| Category | Count | Nations |
|----------|-------|---------|
| **Ships** | 842 | USA (247), Germany (223), GB (188), Japan (160) |
| **Aircraft** | 437 | USA (178), GB (92), Japan (88), Germany (75) |
| **Naval Guns** | 372 | All nations |
| **Turrets** | 2,857 | All nations |
| **Torpedoes** | 234 | All nations |
| **Missiles** | 202 | All nations |
| **Economy Resources** | 257 | Game-specific |

**Time Period**: 1890-2020

---

## Getting Started

### For Game Development
1. Start with `GDD/00-Meta/` for project overview
2. Reference ship/weapon data in sections 04-06
3. See `GDD/Scripts/` for Unity implementation

### For Obsidian
1. Open vault at repository root
2. Enable Dataview plugin for queries
3. Use Canvases for visual research trees

---

## File Format

All files use YAML frontmatter:
```yaml
---
designation: Iowa-Class
nation: USA
type: Battleship
commissioned: 1943
tags: [battleship, wwii]
---
```

## Linking Conventions

- Ships: `[[/GDD/04-Ships/USA/Battleships/Iowa-Class.md|Iowa Class]]`
- Aircraft: `[[/GDD/05-Aircraft/USA/Naval-Fighter/F4U-Corsair.md|F4U Corsair]]`
- Weapons: `[[/GDD/06-Weapons/Naval-Weapons/...]]`

---

## Related

- **Game Repository**: [WOS2.3_V2](https://github.com/AsloWaves/WOS2.3_V2)
- **Engine**: Unity 6000.0.55f1 with Mirror networking

---

**Version**: 5.0 (Unified GDD Structure)
**Restructured**: December 2025
