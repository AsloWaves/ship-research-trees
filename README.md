# Naval Warfare Research Database

Comprehensive research database for naval warfare systems including ships, aircraft, and weapons.

**Consolidated from**: ship-research-trees + usa-naval-weapons-research

## Repository Structure

```
├── Ships/                  # Naval vessel research (300+ classes)
│   ├── USA/               # United States Navy
│   ├── Great Britain/     # Royal Navy
│   ├── Japan/             # Imperial Japanese Navy
│   └── Germany/           # Kriegsmarine
│
├── Aircraft/              # Carrier-based aircraft (113 aircraft)
│   ├── research.db        # SQLite: aircraft + aircraft weapons
│   └── *.md               # Research trees and overviews
│
└── Weapons/               # Weapons systems
    ├── Naval-Guns/        # Ship-based weapons
    │   ├── database/      # 278 guns, 217 ammo, 1132 turrets
    │   ├── scripts/       # Analysis tools
    │   └── reports/       # Research findings
    │
    └── Aircraft-Weapons/  # Air-launched weapons (in research.db)
```

## Database Contents

### Ships (300+ classes)
- **USA**: 250+ ship classes (1890-2020)
- **UK**: 50+ ship classes (1900-2020)
- **Japan**: Multiple IJN classes
- **Germany**: Kriegsmarine vessels

### Aircraft (113 total)
- **USA**: 46 aircraft (35 production + 11 experimental)
- **UK**: 32 aircraft (29 production + 3 experimental)
- **Japan**: 27 aircraft (20 production + 7 experimental)
- **Germany**: 8 aircraft (2 production + 6 experimental)

### Weapons Systems

#### Aircraft Weapons (142 total)
**Location**: `Aircraft/research.db`
- **USA**: 112 weapons (bombs, torpedoes, rockets, missiles)
- **UK**: 30 weapons

#### Naval Guns (278 total)
**Location**: `Weapons/Naval-Guns/database/`
- **Calibers**: 3" to 18" (1890-1990)
- **Nations**: USA, British, German, Japanese
- **Ammunition**: 217 projectile types
- **Turrets**: 1132 mount configurations
- **Compatibility**: 321 gun-ammo pairings

### Aircraft Status Categories
- **Production**: Operational service aircraft
- **Prototype**: Test aircraft (1-10 built)
- **Limited Production**: Small production runs (10-100 built)
- **Failed Production**: Built but never used operationally
- **Design Only**: Paper designs, never built

## Research Coverage

### Time Periods
- **USA**: 1911-2019 (Century+ of naval aviation)
- **UK**: 1915-2018
- **Japan**: 1921-1945 (Imperial Japanese Navy)
- **Germany**: 1936-1945 (Kriegsmarine carrier aircraft)

### Includes
- Carrier-based fighters, bombers, torpedo bombers
- Reconnaissance and patrol aircraft
- Floatplanes and seaplanes
- Experimental and prototype aircraft
- Weapons: Bombs, torpedoes, rockets, missiles

## Tools & Files

- `CODECKS_IMPORT_INSTRUCTIONS.md` - Documentation importer setup
- `codecks_importer.py` - Python import script
- `.gitignore` - Git exclusions

## Usage

The SQLite database (`Aircraft/research.db`) can be queried directly:

```sql
-- List all aircraft by nation
SELECT nation, COUNT(*) FROM aircraft GROUP BY nation;

-- Find experimental aircraft
SELECT designation, common_name, nation, aircraft_status
FROM aircraft
WHERE aircraft_status != 'Production';

-- Search weapons
SELECT designation, common_name, nation FROM weapons;
```

## Research Status & Future Work

### Completed ✅
- USA ships (250+ classes, 1890-2020)
- UK ships (50+ classes)
- Aircraft database (113 aircraft, 4 nations)
- Aircraft weapons (142 weapons, 2 nations)
- Naval guns (278 guns, 4 nations)
- Naval ammunition & turrets

### In Progress 🔄
- Converting naval guns from markdown to SQLite
- Japan & Germany ship research
- Expanding aircraft weapons to all 4 nations

### Future Priorities 📋
- Ship-to-weapon linking (which ships carried which guns)
- Aircraft-to-weapon compatibility
- Naval missiles (SAMs, cruise missiles, ASROCs)
- Ship-launched torpedoes
- Additional nations (France, Italy, Soviet Union)
- Modern systems (post-1990)

## Repository Consolidation

This repository consolidates research from two previously separate projects:

1. **ship-research-trees**: Ships & aircraft research
2. **usa-naval-weapons-research**: Naval guns & ammunition systems

Combined into a unified naval warfare research database covering all aspects of naval combat systems from 1890-2020.

## Related Repositories

- Original usa-naval-weapons-research: [archived after merge]
