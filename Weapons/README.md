# Weapons Systems Research

Comprehensive database of naval and aviation weapons systems.

## Directory Structure

```
Weapons/
├── Naval-Guns/           # Ship-based weapons systems
│   ├── database/         # Markdown databases
│   ├── scripts/          # Analysis tools
│   ├── reports/          # Research findings
│   └── README.md         # Naval guns documentation
│
└── Aircraft-Weapons/     # Aircraft-launched weapons
    └── README.md         # Links to ../Aircraft/research.db
```

## Weapons Coverage

### Naval Guns (Ship-Based)
**Location**: `Naval-Guns/database/`
**Format**: Markdown tables + SQLite (future)

**Coverage**:
- **278 guns** (3" to 18" caliber, 1890-1990)
- **217 ammunition types** (AP, HE, special projectiles)
- **1132 turrets/mounts** (single, twin, triple configurations)
- **321 compatibility records** (gun-ammo pairings)

**Nations**: USA, British, German, Japanese

**Key Files**:
- `naval_guns_database.md` - Complete gun specifications
- `DATABASE_STATUS.md` - Database metrics and progress
- `VALIDATION_REPORT.md` - Data verification results

### Aircraft Weapons (Air-Launched)
**Location**: `../Aircraft/research.db` (SQLite)

**Coverage**:
- **142 weapons** (USA: 112, UK: 30)
- Bombs, torpedoes, rockets, missiles
- Air-to-air and air-to-ground munitions

## Cross-Reference Integration

### Ship → Guns
Link ship classes to their historical armament:
- Example: Iowa-class → 16"/50 Mark 7 guns
- See `Ships/` directory for vessel data

### Aircraft → Weapons
Link aircraft to compatible weapons:
- Example: F-14 Tomcat → AIM-54 Phoenix
- See `Aircraft/research.db` for loadouts

### Future Integration
- Ship-launched torpedoes vs air-launched torpedoes
- Naval missiles (ship-to-air, ship-to-ship)
- Anti-submarine weapons
- Electronic warfare systems

## Research Status

| Category | Status | Records | Nations |
|----------|--------|---------|---------|
| Naval Guns | ⚠️ Markdown | 278 | 4 |
| Naval Ammunition | ⚠️ Markdown | 217 | 4 |
| Naval Turrets | ⚠️ Markdown | 1132 | 4 |
| Aircraft Weapons | ✅ SQLite | 142 | 2 |

## Usage Examples

### Query Aircraft Weapons
```sql
-- In ../Aircraft/research.db
SELECT designation, common_name, nation, weapon_type
FROM weapons
WHERE nation = 'USA'
ORDER BY year_introduced;
```

### Find Naval Gun Data
```bash
# Search naval guns markdown
grep "16\"/50" Weapons/Naval-Guns/database/naval_guns_database.md
```

## Future Work

1. **Convert Naval Guns to SQLite**: Migrate markdown data to structured database
2. **Unified Weapons DB**: Consider merging aircraft/naval weapons
3. **Add Missiles**: Ship-launched SAMs, cruise missiles, ASROCs
4. **Torpedo Database**: Separate air/ship-launched torpedo specs
5. **Integration Layer**: Cross-reference ships/aircraft to weapons

## See Also

- [Ships Research](../Ships/) - Vessel specifications and classes
- [Aircraft Research](../Aircraft/) - Carrier aviation database
- [Naval Weapons README](Naval-Guns/README.md) - Detailed naval guns documentation
