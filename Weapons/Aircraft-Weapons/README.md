# Aircraft Weapons Database

Aircraft-launched weapons are stored in the main aircraft database: `../../Aircraft/research.db`

## Contents

**142 weapons across 2 nations:**
- USA: 112 weapons
- UK: 30 weapons

## Weapon Categories

### Bombs
- General purpose bombs (Mk 82, Mk 83, Mk 84)
- Precision guided munitions
- Depth charges
- Naval mines

### Torpedoes (Air-Launched)
- Mk 13 aerial torpedo
- Other air-dropped torpedoes

### Rockets
- HVAR 5-inch rockets
- Other unguided rocket types

### Missiles
- Air-to-air: AIM-9 Sidewinder, AIM-7 Sparrow, AIM-120 AMRAAM
- Air-to-ground: AGM-12 Bullpup, AGM-84 Harpoon, AGM-65 Maverick

## Database Access

Query aircraft weapons from the SQLite database:

```sql
-- List all weapons by nation
SELECT nation, COUNT(*) FROM weapons GROUP BY nation;

-- Find missiles
SELECT designation, common_name, weapon_type
FROM weapons
WHERE weapon_type LIKE '%Missile%';

-- Get weapon details
SELECT * FROM weapons WHERE designation = 'AIM-9X';
```

## Related Data

- **Aircraft**: See `../../Aircraft/research.db` for aircraft that carry these weapons
- **Armament Loadouts**: Links aircraft to compatible weapons
- **Weapon Categories**: Classification and game mechanics

## Cross-Reference

For ship-launched weapons, see `../Naval-Guns/`
