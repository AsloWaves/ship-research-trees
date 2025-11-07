# Naval Warfare Research Database

Comprehensive research database for naval warfare systems including ships, aircraft, and weapons organized for Obsidian Canvas workflow.

**Last Updated**: November 6, 2025
**Organization**: Type-based structure (Ships/, Aircraft/, Weapons/, Ammunition/)

---

## 📁 Repository Structure

```
D:\Research/
├── Ships/                          # 782 ship classes (1890-2020)
│   ├── USA/                        # United States Navy
│   │   ├── Battleships/
│   │   ├── Carriers/
│   │   ├── Cruisers/
│   │   ├── Destroyers/
│   │   ├── Submarines/
│   │   ├── Amphibious/
│   │   └── Overviews/              # Research trees
│   ├── Great-Britain/              # Royal Navy
│   ├── Japan/                      # Imperial Japanese Navy
│   ├── Germany/                    # Kriegsmarine
│   └── _Database/                  # Ship database files (future)
│
├── Aircraft/                       # Carrier aviation
│   ├── USA/                        # 46 aircraft markdown files
│   ├── Great-Britain/              # 32 aircraft markdown files (UK)
│   ├── Japan/                      # 27 aircraft markdown files
│   ├── Germany/                    # 8 aircraft markdown files
│   ├── aircraft.db                 # 113 aircraft + 142 weapons
│   ├── aircraft_schema.txt
│   └── Research-Trees/
│       ├── 00_US_Aircraft_Research_Tree.md
│       ├── 00_GB_Aircraft_Research_Tree.md
│       └── 00_GB_Weapons_Overview.md
│
├── Weapons/                        # All weapons systems
│   ├── Naval-Guns/                 # Ship-based guns
│   │   ├── database/
│   │   │   ├── naval_guns.db       # 83 guns, 72 ammo, 1700 turrets
│   │   │   └── *.md                # Research tree logic
│   │   ├── scripts/                # Analysis tools
│   │   ├── docs/
│   │   └── reports/
│   │
│   ├── Torpedoes/                  # Naval torpedoes
│   │   └── Research-Trees/
│   │       ├── USA_TORPEDOES_RESEARCH_TREE_LOGIC.md
│   │       ├── BRITAIN_TORPEDOES_RESEARCH_TREE_LOGIC.md
│   │       ├── GERMANY_TORPEDOES_RESEARCH_TREE_LOGIC.md
│   │       └── JAPAN_TORPEDOES_RESEARCH_TREE_LOGIC.md
│   │
│   ├── Missiles/                   # Naval missiles
│   │   └── Research-Trees/
│   │       └── [NATION]_MISSILES_RESEARCH_TREE_LOGIC.md (×4)
│   │
│   ├── Bombs/                      # Naval bombs
│   │   └── Research-Trees/
│   │       └── [NATION]_BOMBS_RESEARCH_TREE_LOGIC.md (×4)
│   │
│   └── Aircraft-Weapons/           # Air-launched weapons
│       ├── Bombs/                  # 53 bomb markdown files
│       ├── Missiles/               # 47 missile markdown files
│       ├── Rockets/                # 10 rocket markdown files
│       ├── Torpedoes/              # 11 torpedo markdown files
│       ├── Depth-Charges/          # 10 depth charge markdown files
│       ├── Mines/                  # 5 mine markdown files
│       └── Practice-Munitions/     # 6 practice munition markdown files
│
├── _Archive/                       # Historical preservation
│   ├── ship-research-trees-original/  # 19 MB original research
│   ├── naval-weapons-data-legacy/     # 5.1 MB old markdown tables
│   ├── database-backups/              # 30 MB backup databases
│   └── migration-scripts/             # 749 KB conversion tools
│
├── _Documentation/
│   ├── README.md                   # This file
│   ├── DATABASE_AUDIT_REPORT.md    # Database vs markdown gaps
│   ├── OBSIDIAN_GUIDE.md          # Obsidian optimization
│   └── DATABASE_SCHEMA.md          # SQL schema reference
│
└── _Scripts/                       # Active utility scripts
    ├── analysis/
    ├── conversion/
    └── validation/
```

---

## 📊 Database Contents

### Ships (782 classes)
- **USA**: 500+ ship classes (1890-2020)
- **Great Britain**: 150+ ship classes (1900-2020)
- **Japan**: 100+ Imperial Japanese Navy classes
- **Germany**: 50+ Kriegsmarine vessels
- **Format**: Markdown files with YAML frontmatter, Obsidian-optimized

### Aircraft (113 total) ✅ *Markdown files generated*
- **USA**: 46 aircraft
- **UK**: 32 aircraft
- **Japan**: 27 aircraft
- **Germany**: 8 aircraft
- **Status**: All 113 aircraft have markdown files in `Aircraft/[Nation]/`
- **Format**: Markdown files with YAML frontmatter, Obsidian-optimized

### Aircraft Weapons (142 total) ✅ *Markdown files generated*
- **USA**: 112 weapons (bombs, torpedoes, rockets, missiles, depth charges, mines)
- **UK**: 30 weapons (bombs, missiles, rockets, torpedoes, depth charges)
- **Status**: All 142 weapons have markdown files in `Weapons/Aircraft-Weapons/[Category]/`
- **Format**: Markdown files with YAML frontmatter, organized by weapon type

### Naval Weapons Systems
**Naval Guns** ✅ *Markdown files generated*:
- **Guns**: 372 gun models (3" to 18" caliber, 1890-1990) across 4 nations
  - USA: 83 guns
  - British: 93 guns
  - German: 96 guns
  - Japanese: 100 guns
- **Ammunition**: 72 projectile types (AP, HC, HE, AAC, etc.) - All USA
- **Turrets**: 1,700 mount configurations - All USA
- **Status**: All have markdown files in `Weapons/Naval-Guns/Guns/[Nation]/`
- **Format**: Markdown files with YAML frontmatter, organized by nation

**Naval Torpedoes** ✅ *Markdown files generated*:
- **Entries**: 234 torpedoes (USA, British, German, Japanese)
- **Coverage**: 1889-2024
- **Status**: All have markdown files in `Weapons/Torpedoes/[Nation]/`
- **Format**: Markdown files with YAML frontmatter, organized by nation

**Naval Missiles** ✅ *Markdown files generated*:
- **Entries**: 192 missiles (USA, British, French, Soviet/Russian, Japanese, others)
- **Coverage**: 1950-2025
- **Status**: All have markdown files in `Weapons/Missiles/[Nation]/`
- **Format**: Markdown files with YAML frontmatter, organized by nation

**Naval Bombs** ✅ *Markdown files generated*:
- **Entries**: 107 bombs (USA, British, German, Japanese)
- **Coverage**: 1940-2024
- **Status**: All have markdown files in `Weapons/Bombs/[Nation]/`
- **Format**: Markdown files with YAML frontmatter, organized by nation

**Naval Aircraft** ✅ *Markdown files generated*:
- **Entries**: 144 naval aircraft (carrier-based)
- **Status**: All have markdown files in `Aircraft/Naval/`
- **Format**: Markdown files with YAML frontmatter

**Ground Aircraft** ✅ *Markdown files generated*:
- **Entries**: 147 ground-based aircraft
- **Status**: All have markdown files in `Aircraft/Ground/`
- **Format**: Markdown files with YAML frontmatter

---

## 🎯 Current Status

### ✅ Complete
- Ship markdown files (782 files, 6 MB)
- Aircraft markdown files (113 files, organized by nation)
- Aircraft weapons markdown files (142 files, organized by weapon type)
- Research tree logic for all weapon types and nations
- Type-based organization optimized for Obsidian
- Database consolidation and cleanup
- Archive organization (historical preservation)
- Markdown generation scripts in `_Scripts/`

### ⚠️ In Progress
- Ship-to-weapon linking implementation

### 📋 Future Work
- Ship-to-weapon linking (which ships carried which guns)
- Aircraft-to-weapon compatibility mappings
- Cross-reference system between Ships, Aircraft, and Weapons
- Obsidian Canvas templates for research trees
- Additional nations (France, Italy, Soviet Union)
- Modern systems (post-1990)

---

## 🔧 Obsidian Integration

### Research Trees
Research trees are kept with their content for context:
- **Ships**: `Ships/[Nation]/Overviews/00_[Type]_Research_Tree.md`
- **Aircraft**: `Aircraft/Research-Trees/00_[Nation]_Aircraft_Research_Tree.md`
- **Weapons**: `Weapons/[Type]/Research-Trees/[NATION]_[TYPE]_RESEARCH_TREE_LOGIC.md`

### Linking Conventions
- Ship classes: `[[Ship-Class-Name]]`
- Aircraft: `[[Designation]]` (e.g., `[[F4U-1]]`)
- Weapons: `[[Weapon-Designation]]`

### YAML Frontmatter
All markdown files include YAML frontmatter for Obsidian queries:
```yaml
---
designation: Iowa-Class
nation: USA
type: Battleship
commissioned: 1943
decommissioned: 1992
tags: [battleship, fast-battleship, iowa-class]
---
```

---

## 💾 Databases

### Primary Databases
1. **aircraft.db** (`Aircraft/aircraft.db`) - 184 KB
   - Tables: aircraft, weapons, armament_loadouts, upgrades
   - Purpose: Aircraft specifications and weapons compatibility

2. **naval_guns.db** (`Weapons/Naval-Guns/database/naval_guns.db`) - 4.9 MB
   - Tables: Guns, Ammunition, Turrets, Gun_Ammunition_Compatibility
   - Purpose: Naval artillery systems and specifications

### Database Strategy
**Current Approach**: Markdown-first with database support
- **Primary Source**: Markdown files (human-readable, Git-friendly, Obsidian-optimized)
- **Database Role**: Complex queries, cross-references, analytics
- **Sync**: Generate databases FROM markdown (one-way)
- **Exception**: Aircraft/weapons currently database-only (temporary)

---

## 📚 Key Documents

### Research Reference
- `Ships/[Nation]/Overviews/` - Ship research trees by nation and type
- `Aircraft/Research-Trees/` - Aircraft and weapons research trees
- `Weapons/*/Research-Trees/` - Weapons research tree logic

### Technical Documentation
- `_Documentation/DATABASE_AUDIT_REPORT.md` - Database vs markdown gap analysis
- `_Documentation/OBSIDIAN_GUIDE.md` - Obsidian Canvas best practices
- `_Documentation/DATABASE_SCHEMA.md` - SQL schema documentation
- `Aircraft/aircraft_schema.txt` - Aircraft database schema
- `Weapons/Naval-Guns/DATABASE_STATUS.md` - Naval guns database status

### Historical Archives
- `_Archive/ship-research-trees-original/` - Original research source (19 MB)
- `_Archive/naval-weapons-data-legacy/` - Legacy markdown tables (5.1 MB)
- `_Archive/migration-scripts/` - Conversion and migration tools (749 KB)
- `_Archive/database-backups/` - Database backup history (30 MB)

---

## 🚀 Getting Started

### For Research
1. Browse ship classes in `Ships/[Nation]/[Type]/`
2. Review research trees in `*/Overviews/` or `*/Research-Trees/`
3. Cross-reference using Obsidian links

### For Database Queries
```sql
-- Aircraft by nation
sqlite3 Aircraft/aircraft.db "SELECT nation, COUNT(*) FROM aircraft GROUP BY nation;"

-- Naval guns by caliber
sqlite3 Weapons/Naval-Guns/database/naval_guns.db "SELECT designation, caliber_inches, nation FROM Guns ORDER BY caliber_inches DESC LIMIT 10;"
```

### For Obsidian Canvas
1. Open Obsidian vault at `D:\Research`
2. Create new Canvas for research trees
3. Link to research tree markdown files
4. Build visual relationships between ship classes

---

## 📝 Contributing

### Adding New Ships
1. Create markdown file in appropriate `Ships/[Nation]/[Type]/` directory
2. Use YAML frontmatter for metadata
3. Follow existing ship class format
4. Update relevant research tree in `Overviews/`

### Adding Aircraft/Weapons (Future)
1. Run markdown generation script (to be created)
2. Review generated files for accuracy
3. Add to appropriate nation directory
4. Update research trees

### Database Updates
⚠️ **Important**: Markdown files are the primary source. Update markdown first, then regenerate databases if needed.

---

## 🔗 Related Repositories

### Original Sources (Now Archived)
- **ship-research-trees**: Ship and aircraft research (archived to `_Archive/`)
- **usa-naval-weapons-research**: Naval weapons systems (consolidated into Weapons/)

### Current Repository
- **Unified Naval Research**: Single repository for all naval warfare research
- **Remote**: https://github.com/AsloWaves/usa-naval-weapons-research.git (to be renamed)

---

## 📈 Statistics

| Category | Count | Format | Status |
|----------|-------|--------|--------|
| Ship Classes | 782 | Markdown | ✅ Complete |
| Carrier Aircraft | 113 | Markdown + DB | ✅ Complete |
| Aircraft Weapons | 142 | Markdown + DB | ✅ Complete |
| Naval Guns | 372 | Markdown + DB | ✅ Complete |
| Ammunition Types | 72 | Markdown + DB | ✅ Complete |
| Turret Configs | 1700 | Markdown + DB | ✅ Complete |
| Naval Torpedoes | 234 | Markdown | ✅ Complete |
| Naval Missiles | 192 | Markdown | ✅ Complete |
| Naval Bombs | 107 | Markdown | ✅ Complete |
| Naval Aircraft | 144 | Markdown | ✅ Complete |
| Ground Aircraft | 147 | Markdown | ✅ Complete |
| Research Trees | 50+ | Markdown | ✅ Complete |

**Total Active Files**: 4,005 markdown files, 2 databases
**Total Size**: ~50 MB active + 43 MB archived
**Nations Covered**: USA, Great Britain, Japan, Germany
**Time Period**: 1890-2020 (130 years)

---

## 📧 Contact & Feedback

For questions, issues, or contributions regarding this research database, please open an issue on GitHub.

---

**Version**: 3.1 (Naval Guns Expansion)
**Last Major Update**: November 6, 2025 - Naval guns markdown generation expanded to all 4 nations (372 files: USA, British, German, Japanese guns)
**Previous Update**: November 6, 2025 - All weapons systems markdown generation (826 files: torpedoes, missiles, bombs, naval/ground aircraft)
**Next Milestone**: Ship-to-weapon linking and cross-reference system implementation
