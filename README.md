# Ship Research Trees

Comprehensive research database for naval warfare systems including ships, aircraft, and weapons.

## Repository Structure

```
├── Ships/               # Naval vessel research
│   ├── USA/            # United States Navy vessels
│   └── Great Britain/  # Royal Navy vessels
│
├── Aircraft/           # Carrier-based aircraft research
│   ├── research.db     # SQLite database (113 aircraft, 142 weapons)
│   ├── 00_US_Aircraft_Research_Tree.md
│   ├── 00_GB_Aircraft_Research_Tree.md
│   └── 00_GB_Weapons_Overview.md
│
└── Weapons/            # Naval weapons systems (future)
```

## Database Contents

### Aircraft (113 total)
- **USA**: 46 aircraft (35 production + 11 experimental)
- **UK**: 32 aircraft (29 production + 3 experimental)
- **Japan**: 27 aircraft (20 production + 7 experimental)
- **Germany**: 8 aircraft (2 production + 6 experimental)

### Weapons (142 total)
- **USA**: 112 weapons
- **UK**: 30 weapons

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

## Contributing

Research is ongoing. Current focus areas:
- Japanese and German weapons systems
- Additional nations (France, Italy, Soviet Union)
- Modern aircraft (post-2019)
- Ship weapons integration
