# Naval Weapons Research Template - Worker Agent Guide

**Version**: 1.0
**Date**: 2025-10-08

This template provides standardized research methodology for naval weapons database completion.

---

## Research Methodology

### Primary Sources (Priority Order)
1. **NavWeaps.com** - Primary technical specifications source
2. **Wikipedia** - Ship class and gun articles for historical context
3. **Naval History Magazine** - Specific weapon system articles
4. **Navy General Board** - Experimental and design studies
5. **Ship-specific archives** (USS Slater, battleship museums, etc.)

### Data Validation
- **Confirmed Data**: Found in ≥2 independent sources
- **Estimated Data**: Calculated using established formulas with (est) notation
- **Missing Data**: Document as NULL if not found after reasonable search

---

## Established Formulas (From Batch 1 Research)

### Shell Length Calculation
```
AP shells: shell_length = caliber_diameter × 4.5
HC shells: shell_length = caliber_diameter × 4.0
Older/special: shell_length = caliber_diameter × 3.5-4.0
```
**Example**: 14" AP shell = 14 × 4.5 = 63 inches

### Bursting Charge Calculation
```
AP shells: bursting_charge = projectile_weight × 0.015 (1.5%)
HC shells: bursting_charge = projectile_weight × 0.08 (8.0%)
HE shells: bursting_charge = projectile_weight × 0.10 (10%)
```
**Example**: 2,700 lb AP shell = 2,700 × 0.015 = 40.5 lbs

### Cartridge Type Assignment (By Caliber)
```
Separate: Caliber ≥ 8" (projectile and powder loaded separately)
Semi-fixed: Caliber 6"-8" (adjustable powder case)
Fixed: Caliber ≤ 5" (crimped one-piece round)
```
**Exception**: Some 6" guns use Separate loading (check sources)

### Typical Performance Ranges (For Estimation)

**Traverse Rates** (deg/sec):
- Battleship main battery: 2-5 deg/sec
- Cruiser main battery: 4-6 deg/sec
- Dual-purpose mounts: 15-30 deg/sec
- AA mounts: 25-40 deg/sec

**Elevation Rates** (deg/sec):
- Battleship main battery: 4-12 deg/sec
- Cruiser main battery: 8-12 deg/sec
- Dual-purpose mounts: 15-30 deg/sec
- AA mounts: 20-40 deg/sec

**Crew Sizes** (Typical):
- 18" turrets: 150-200 men
- 16" turrets: 77-150 men
- 14" turrets: 60-100 men
- 12" turrets: 50-80 men
- 8" turrets: 30-50 men
- 6" turrets: 20-35 men
- 5" turrets: 6-15 men (mount dependent)
- 3"-4" mounts: 5-10 men

**Armor Thickness** (Typical):
- 16"-18" turrets: 17-22" face, 8-12" sides, 5-9" roof
- 14" turrets: 14-18" face, 8-11" sides, 4-6" roof
- 12" turrets: 10-15" face, 6-9" sides, 4-6" roof
- 8" turrets: 6-8" face, 3-5" sides, 2-3" roof
- 6" turrets: 2-6" face, 1-3" sides, 1-2" roof
- 5" mounts: 0-2" shields (often open mounts)
- 3"-4" mounts: 0" (open mounts)

---

## Research Process for Each Gun

### Step 1: Identify Gun and Ship Classes
```
- Gun ID: [from database]
- Caliber: [e.g., "16\""]
- Mark Designation: [e.g., "Mark 7"]
- Ship Classes: [e.g., "Iowa, New Jersey, Missouri, Wisconsin"]
- Years of Service: [e.g., "1943-1992"]
```

### Step 2: Find Ammunition Data
For EACH ammunition type associated with this gun:

**Shell Length (inches)**:
1. Search NavWeaps for "shell length" or "projectile length"
2. Check Wikipedia gun article for dimensional data
3. If not found, apply formula based on projectile type
4. Document as (est) if estimated

**Bursting Charge (pounds)**:
1. Search NavWeaps for "bursting charge" or "explosive fill"
2. Check specification tables for TNT/explosive D weight
3. If not found, apply % formula based on projectile weight
4. Document as (est) if estimated

**Cartridge Type**:
1. Determine from caliber range (≥8" = Separate, etc.)
2. Verify with source descriptions ("fixed ammunition", "bag charges", etc.)
3. Special cases: Some 6" guns use Separate (check sources)

### Step 3: Find Turret/Mount Data

**Crew Size**:
1. Search NavWeaps turret specifications for crew numbers
2. Check Wikipedia for "turret crew" or "gun crew"
3. Use ship crew breakdowns if available
4. If range given, use middle value (e.g., "77-110" → use 94)
5. Estimate from similar gun/mount if not found

**Armor Specifications**:
1. Search for turret armor: face, sides, roof, barbette
2. NavWeaps typically lists all armor values
3. Note armor type: Class A (face/sides), Class B (roof)
4. STS (Special Treatment Steel) backing plates
5. Some mounts have no armor (open mounts) → document as 0" or NULL

**Traverse Rate** (deg/sec):
1. Search NavWeaps for "training speed" or "traverse rate"
2. Wikipedia may list as "degrees/second" or "°/sec"
3. Verify units (degrees vs mils, seconds vs minutes)
4. Estimate from gun type if not found (use typical ranges)

**Elevation Rate** (deg/sec):
1. Search NavWeaps for "elevation speed" or "elevation rate"
2. Often listed with traverse rate
3. Verify units and convert if necessary
4. Estimate from gun type if not found

---

## Output Format

### For Each Gun Researched:

```markdown
## Gun: [Caliber] [Mark] - [Ship Class]

### Gun Information
- **Gun_ID**: [from database]
- **Caliber**: [e.g., 16"]
- **Mark**: [e.g., Mark 7]
- **Ship Classes**: [e.g., Iowa, New Jersey, Missouri, Wisconsin]

### Ammunition Data

#### [Ammo ID]: [Mark] [Type] ([Weight] lbs)
- **Shell Length**: [value] in ([confirmed/est using X.X cal formula])
- **Bursting Charge**: [value] lbs ([confirmed/est using X.X% formula])
- **Cartridge Type**: [Separate/Semi-fixed/Fixed] ([confirmed/inferred from caliber])
- **Sources**: [NavWeaps, Wikipedia, etc.]

[Repeat for each ammunition type]

### Turret Data

#### Turret_ID [X]: [Designation]
- **Crew Size**: [value] ([confirmed/estimated from similar])
- **Armor Face**: [value] in ([confirmed/NULL if not found])
- **Armor Sides**: [value] in ([confirmed/NULL if not found])
- **Armor Roof**: [value] in ([confirmed/NULL if not found])
- **Traverse Rate**: [value] deg/sec ([confirmed/estimated])
- **Elevation Rate**: [value] deg/sec ([confirmed/estimated])
- **Sources**: [NavWeaps, Wikipedia, etc.]

### SQL Updates

```sql
-- Ammunition updates
UPDATE Ammunition SET Length_IN = [value], Bursting_Charge = [value], Cartridge_Type = '[type]',
  Notes = '[description with source]' WHERE ID = [ID];

-- Turret updates
UPDATE Turrets SET Crew_Size = [value], Armor_Face_IN = [value], Armor_Sides_IN = [value],
  Armor_Roof_IN = [value], Traverse_Rate_Deg_Sec = [value], Elevation_Rate_Deg_Sec = [value],
  Notes = '[description with source]' WHERE Turret_ID = [ID];
```
```

---

## Quality Checklist

Before submitting results, verify:

- [ ] All assigned guns researched
- [ ] All ammunition types for each gun documented
- [ ] Shell lengths use correct formula (4.5 for AP, 4.0 for HC)
- [ ] Bursting charges use correct formula (1.5% AP, 8% HC)
- [ ] Cartridge types match caliber conventions
- [ ] Turret data includes all available specifications
- [ ] Sources cited for all confirmed data
- [ ] Estimated data clearly marked with (est)
- [ ] SQL syntax validated
- [ ] No duplicate Gun_IDs or Ammunition IDs

---

## Example: Complete Gun Research

```markdown
## Gun: 8"/55 Mark 15 - Baltimore Class Heavy Cruisers

### Gun Information
- **Gun_ID**: 428
- **Caliber**: 8"
- **Mark**: Mark 15
- **Ship Classes**: Baltimore, Boston, Pittsburgh (CA-68 class, 14 ships)
- **Years**: 1943-1971

### Ammunition Data

#### ID 38: Mark 21 AP (335 lbs)
- **Shell Length**: 36.0 in (confirmed NavWeaps - 4.5 cal)
- **Bursting Charge**: 5.03 lbs (confirmed NavWeaps - 1.5%)
- **Cartridge Type**: Separate (confirmed - bag charges)
- **Sources**: NavWeaps 8"/55 Mark 15, Wikipedia Baltimore-class

#### ID 39: Mark 25 HC (260 lbs)
- **Shell Length**: 32.0 in (est using 4.0 cal formula)
- **Bursting Charge**: 20.8 lbs (confirmed NavWeaps - 8.0%)
- **Cartridge Type**: Separate (confirmed - bag charges)
- **Sources**: NavWeaps, Wikipedia

### Turret Data

#### Turret_ID 38: 8"/55 Mark 15 Triple Turret
- **Crew Size**: 40 (confirmed NavWeaps)
- **Armor Face**: 6.3 in (confirmed Wikipedia)
- **Armor Sides**: 3.0 in (confirmed Wikipedia)
- **Armor Roof**: 2.5 in (confirmed Wikipedia)
- **Traverse Rate**: 5.3 deg/sec (confirmed NavWeaps)
- **Elevation Rate**: 10.6 deg/sec (confirmed NavWeaps)
- **Sources**: NavWeaps 8"/55 Marks 12 and 15, Wikipedia Baltimore-class

### SQL Updates

```sql
-- Ammunition: Mark 21 AP
UPDATE Ammunition SET Length_IN = 36.0, Bursting_Charge = 5.03, Cartridge_Type = 'Separate',
  Notes = 'Mark 21 AP for Mark 15, 335 lbs @ 2,800 fps, 1.5% bursting charge, 4.5 calibers'
WHERE ID = 38;

-- Ammunition: Mark 25 HC
UPDATE Ammunition SET Length_IN = 32.0, Bursting_Charge = 20.8, Cartridge_Type = 'Separate',
  Notes = 'Mark 25 HC for Mark 15, 260 lbs, 8.0% bursting charge (est), 4.0 calibers (est)'
WHERE ID = 39;

-- Turret: Mark 15 Triple
UPDATE Turrets SET Crew_Size = 40, Armor_Face_IN = 6.3, Armor_Sides_IN = 3.0,
  Armor_Roof_IN = 2.5, Traverse_Rate_Deg_Sec = 5.3, Elevation_Rate_Deg_Sec = 10.6,
  Notes = 'Baltimore class, 40 crew, 6.3"/3"/2.5" armor, 5.3/10.6 deg/sec rates, 451 tons'
WHERE Turret_ID = 38;
```
```

---

## Common Pitfalls to Avoid

1. **Don't confuse gun marks with ammunition marks** - "Mark 15 gun fires Mark 21 ammunition"
2. **Watch for metric/imperial units** - Convert mm to inches, meters to feet
3. **Verify caliber references** - "50-caliber" means barrel length, not diameter
4. **Check date ranges** - Specifications changed over service life
5. **Distinguish mount types** - Single, twin, triple turrets have different characteristics
6. **Note armor types** - Class A (face-hardened) vs Class B (homogeneous)
7. **Handle NULL vs 0** - NULL = unknown, 0 = actually zero (like open mounts)
8. **Source conflicts** - If sources disagree, document both and choose most authoritative

---

## Time Allocation (Per Gun)

- Basic search: 5-10 min
- Ammunition research: 10-15 min
- Turret research: 10-15 min
- Documentation: 5 min
- SQL generation: 5 min

**Total per gun**: 35-50 minutes
**For 7-8 guns**: 4-6 hours per agent

---

## Help & Support

If stuck on specific guns:
1. Check if similar gun/ship class already researched
2. Use established formulas for estimates
3. Document as NULL if truly unavailable
4. Note in research that exhaustive search performed
5. Main orchestrator will handle gaps during validation

**Remember**: Quality over speed - accurate estimated data is better than guessed confirmed data.
