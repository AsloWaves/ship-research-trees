# Naval Warfare Research Database

Comprehensive research database for naval warfare systems including ships, aircraft, and weapons. Organized for Obsidian workflow with integrated Game Design Document (GDD) for **Fathoms Deep** naval game development.

**Last Updated**: December 2025
**Organization**: Dual-structure (Research Database + Game Design Document)

---

## Repository Structure

```
C:\Research/
├── Fathoms Deep Research/          # Game Design Document (GDD)
│   ├── GDD/                        # 12-section game design
│   │   ├── 00-Meta/                # Project overview & status
│   │   ├── 01-Core-Concepts/       # Vision, audience, mechanics
│   │   ├── 02-Core-Gameplay/       # Crew, missions, physics
│   │   ├── 03-Combat-Systems/      # Combat, ammunition, carriers
│   │   ├── 04-Ship-Customization/  # Modules, armor, ship database
│   │   ├── 05-UI-Systems/          # Menus, controls, settings
│   │   ├── 06-Multiplayer/         # Networking, guilds, chat
│   │   ├── 07-Economy/             # Resources (252 files), trading
│   │   ├── Modules/                # Aircraft, weapons, utilities
│   │   └── [08-12 sections...]     # Additional systems
│   ├── Scripts/                    # Unity script documentation
│   ├── Scripts-Reference/          # Implementation references
│   └── Canvases/                   # Visual design canvases
│
├── Ships/                          # Historical ship research (794 files)
│   ├── USA/                        # 246 ships
│   ├── Japan/                      # 140 ships
│   ├── Germany/                    # 221 ships
│   ├── Great-Britain/              # 187 ships
│   └── Overviews/                  # Nation summaries
│
├── Aircraft/                       # Aircraft research (399 files)
│   ├── USA/                        # 177 aircraft
│   ├── Japan/                      # 87 aircraft
│   ├── Germany/                    # 44 aircraft
│   ├── Great-Britain/              # 91 aircraft
│   └── Research-Trees/             # Tech progression trees
│
├── Weapons/                        # Weapons research
│   ├── Naval-Weapons/
│   │   ├── Naval-Guns/             # 372 guns + 1,132 turrets
│   │   ├── Torpedoes/              # 234 torpedoes
│   │   ├── Missiles/               # 192 missiles
│   │   └── Bombs/                  # 107 bombs
│   └── Aircraft-Weapons/           # Air-launched ordnance
│
├── _Archive/                       # Historical backups
├── _DBs/                           # SQLite databases
├── _Documentation/                 # Guides & audit reports
├── _Reports/                       # Analysis summaries
├── _Scripts/                       # Utility scripts (49 files)
└── _Templates/                     # Markdown templates (15 files)
```

---

## Content Statistics

### Research Database

| Category | USA | Japan | Germany | GB | Total |
|----------|-----|-------|---------|-----|-------|
| **Ships** | 246 | 140 | 221 | 187 | **794** |
| **Aircraft** | 177 | 87 | 44 | 91 | **399** |
| **Naval Guns** | 83 | 100 | 96 | 93 | **372** |
| **Torpedoes** | 62 | 62 | 54 | 56 | **234** |

### Game Design Document

| Section | Files | Status |
|---------|-------|--------|
| Economy Resources | 252 | Complete |
| Ship Database | 794 indexed | Linked |
| Weapons Modules | 372 indexed | Linked |
| Aircraft Modules | 399 indexed | Linked |
| Ammunition | 234 indexed | Linked |

**Total Files**: ~3,800 markdown files
**Nations**: USA, Great Britain, Japan, Germany
**Time Period**: 1890-2020

---

## GDD Integration

The Game Design Document links to the research database through comprehensive index files:

| Index | Location | Entries |
|-------|----------|---------|
| Ships | `GDD/04-Ship-Customization/Ship-Database/_Complete-Ships-Index.md` | 794 |
| Guns | `GDD/Modules/Weapons/Main-Guns/_Complete-Guns-Index.md` | 372 |
| Aircraft | `GDD/Modules/Aircraft/_Complete-Aircraft-Index.md` | 399 |
| Torpedoes | `GDD/03-Combat-Systems/Ammunition/Torpedoes/_Complete-Torpedoes-Index.md` | 234 |

> **Design Philosophy**: Research folders contain comprehensive historical data. The GDD contains game-focused interpretations with links back to detailed research.

---

## Obsidian Integration

### File Format
All markdown files include YAML frontmatter:
```yaml
---
designation: Iowa-Class
nation: USA
type: Battleship
commissioned: 1943
tags: [battleship, fast-battleship, wwii]
---
```

### Linking Conventions
- Ships: `[[Ship-Class-Name]]`
- Aircraft: `[[Designation]]`
- Weapons: `[[Weapon-Designation]]`
- Cross-links: `[[/Ships/USA/Battleships/Iowa-Class.md|Iowa Class]]`

---

## Getting Started

### For Research
1. Browse research in `Ships/`, `Aircraft/`, `Weapons/`
2. Use index files in GDD for quick navigation
3. Cross-reference using Obsidian links

### For Game Development
1. Start with `Fathoms Deep Research/GDD/00-Meta/GDD-Overview.md`
2. Reference module indexes for asset data
3. See `Scripts-Reference/` for implementation details

### For Obsidian
1. Open vault at `C:\Research`
2. Enable Dataview plugin for queries
3. Use Canvas for visual research trees

---

## Key Documents

### Game Design
- `Fathoms Deep Research/GDD/CLAUDE.md` - AI assistant context
- `Fathoms Deep Research/GDD/00-Meta/GDD-Overview.md` - Project overview
- `Fathoms Deep Research/GDD/00-Meta/Development-Status.md` - Progress tracking

### Research Reference
- `Ships/Overviews/` - Nation ship summaries
- `Aircraft/Research-Trees/` - Aircraft tech trees
- `Weapons/*/Research-Trees/` - Weapon progression

### Technical
- `_Documentation/DATABASE_AUDIT_REPORT.md` - Data quality analysis
- `_Documentation/OBSIDIAN_GUIDE.md` - Obsidian best practices
- `_Reports/PROJECT_SUMMARY.md` - Standardization history

---

## Scripts

Utility scripts are organized in `_Scripts/`:

| Category | Purpose |
|----------|---------|
| `generate_*.py` | Markdown generation from databases |
| `validate_*.py` | File format validation |
| `analyze_*.py` | Content analysis tools |
| `fix_*.py` | Auto-correction utilities |

Run index generator:
```bash
python _Scripts/generate_gdd_indexes.py
```

---

## Related Links

- **Repository**: https://github.com/AsloWaves/ship-research-trees
- **Game Project**: Fathoms Deep (Unity naval MMO)

---

**Version**: 4.0 (GDD Integration)
**Last Major Update**: December 2025 - GDD consolidation, comprehensive index generation, folder cleanup
