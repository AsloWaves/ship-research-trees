# CrewTemplateSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Crew/CrewTemplateSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Crew` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | 372 |
| **Architecture** | RNG-Based Stat Generation with GDD Crew-Skills Spec |

---

## Purpose

Crew template definition with **RNG stat ranges** (7-15 recruitment range per GDD). Defines crew specialists with classification types, stat growth, and progression formulas. Each template generates unique crew instances with rolled stats.

**Key Features**:
- **18 Crew Classifications** (Gunner, Engineer, Navigator, etc.)
- **RNG Stat Ranges**: 7-15 base stats per GDD specification
- **Stat Growth**: +0.19/+0.10 per level with +5 classification bonus at L25
- **Sailor Count Scaling**: Tiered scaling formula (L1-50, L51-100, L101-200)
- **Crew Weight**: Dynamic weight calculation based on sailor count and level
- **5 Rarity Tiers**: Common, Uncommon, Rare, Epic, Legendary

---

## Crew Identity

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `templateId` | `string` | Auto-generated | Crew template ID (e.g., 'veteran_gunner', 'rookie_engineer') |
| `crewName` | `string` | Empty | Crew name/title |
| `description` | `string` (TextArea) | Empty | Crew backstory and special traits |

---

## Classification (18 Types from GDD)

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `classificationType` | `CrewClassificationType` | `Gunner` | Type of crew specialist - determines primary/secondary stats |

### CrewClassificationType Values (18 Types)
- **Gunner**: Primary = Gunnery, Secondary = Loading
- **Navigator**: Primary = Navigation, Secondary = Observation
- **Engineer**: Primary = Engineering, Secondary = Repair
- **Damage Control**: Primary = Repair, Secondary = Engineering
- **Radar Operator**: Primary = Observation, Secondary = Electronic Warfare
- **Sonar Operator**: Primary = ASW (Anti-Submarine Warfare), Secondary = Observation
- **AA Gunner**: Primary = AA Gunnery, Secondary = Observation
- **Torpedo Specialist**: Primary = Torpedo, Secondary = Engineering
- **Fire Control**: Primary = Fire Control, Secondary = Gunnery
- **Communications**: Primary = Communications, Secondary = Leadership
- **Medic**: Primary = Medicine, Secondary = Morale
- **Quartermaster**: Primary = Logistics, Secondary = Navigation
- **Mechanic**: Primary = Engineering, Secondary = Repair
- **Pilot** (carriers): Primary = Aviation, Secondary = Observation
- **Deck Officer**: Primary = Leadership, Secondary = Navigation
- **Helmsman**: Primary = Helm Control, Secondary = Navigation
- **Lookout**: Primary = Observation, Secondary = AA Gunnery
- **Radio Operator**: Primary = Communications, Secondary = Electronic Warfare

---

## Base Stats (RNG Ranges per GDD: 7-15)

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `primaryStatRange` | `StatRangeInt` | (7, 15) | Primary stat range (classification bonus applies at L25) |
| `secondaryStatRange` | `StatRangeInt` | (7, 15) | Secondary stat range |
| `generalStatRange` | `StatRangeInt` | (7, 12) | General stats range (non-specialty) |

**GDD Specification**: All stats roll 7-15 at recruitment.

**Example**: Recruit a Gunner crew
- Primary stat (Gunnery): Rolls 7-15 (e.g., 12)
- Secondary stat (Loading): Rolls 7-15 (e.g., 9)
- General stats: Roll 7-12 each

---

## Progression Settings

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `startingLevel` | `int` | 1-200 | 1 | Starting level for this template |
| `primaryGrowthPerLevel` | `float` | 0.1-0.5 | 0.19 | Primary stat growth per level (GDD: +0.19) |
| `secondaryGrowthPerLevel` | `float` | 0.05-0.3 | 0.10 | Secondary stat growth per level (GDD: +0.10) |
| `classificationBonusAtL25` | `int` | 0-10 | 5 | Classification bonus at Level 25 (GDD: +5) |
| `maxStatCap` | `int` | 30-100 | 50 | Maximum stat cap (GDD: 50) |

### Stat Calculation Formula
```csharp
effectiveStat = baseStat + (level - 1) × growthRate + classificationBonus
```

**Classification Bonus**: +5 to primary stat at Level 25+ (GDD spec)

**Example**: Gunner with base Gunnery 12 at Level 50
- Base: 12
- Growth: (50 - 1) × 0.19 = 9.31
- Classification bonus: +5 (L25+)
- **Total**: 12 + 9.31 + 5 = 26.31 → **26 Gunnery** (capped at 50)

---

## Crew Size & Weight

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `baseSailorCount` | `int` | 50-200 | 50 | Sailor count multiplier (base offset for balance tuning) |

### Sailor Count Formula (GDD Tiered Scaling)
```
Levels 1-50:   10 + (Level - 1) × 5 sailors
Levels 51-100: 255 + (Level - 50) × 4 sailors
Levels 101-200: 455 + (Level - 100) × 2.5 sailors
```

**Examples**:
- Level 1: 10 sailors
- Level 25: 10 + 24×5 = 130 sailors
- Level 50: 10 + 49×5 = 255 sailors
- Level 100: 255 + 50×4 = 455 sailors
- Level 200: 455 + 100×2.5 = 705 sailors

### Crew Weight Formula (GDD)
```
crewWeight = sailorCount × 0.1 × (1.0 + level / 100)
```

**Example**: Level 50 crew with 255 sailors
- Weight = 255 × 0.1 × (1.0 + 50/100)
- Weight = 25.5 × 1.5 = **38.25 tons**

---

## Special Traits

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `hasSpecialAbility` | `bool` | - | `false` | Does this crew have special abilities? |
| `specialAbilityDescription` | `string` (TextArea) | Empty | Special ability description |
| `efficiencyBonus` | `float` | 0-50% | 0 | Efficiency bonus percentage (+10% = 1.1× effectiveness) |

---

## Rarity & Acquisition

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `rarity` | `CrewRarity` | Enum | `Common` | Crew rarity tier |
| `recruitmentCost` | `int` | 100-100,000 | 1,000 | Recruitment cost in credits |
| `availableForRecruitment` | `bool` | - | `true` | Can this crew be found through recruitment? |
| `requiresSpecialUnlock` | `bool` | - | `false` | Special event or quest required to unlock? |
| `unlockRequirement` | `string` | - | Empty | Unlock requirement description |

### CrewRarity Values
- **Common** (Gray): Level 1-20, 100-1,000 credits
- **Uncommon** (Green): Level 10-50, 500-5,000 credits
- **Rare** (Blue): Level 30-80, 2,000-20,000 credits
- **Epic** (Purple): Level 60-120, 10,000-50,000 credits, special ability
- **Legendary** (Gold): Level 100-200, 50,000-100,000 credits, special ability, special unlock required

---

## Visual

| Property | Type | Description |
|----------|------|-------------|
| `portrait` | `Sprite` | Crew portrait icon |
| `cardBackground` | `Sprite` | Crew card background (based on rarity) |

---

## Key Methods

### Generate Crew Instance
```csharp
public CrewInstanceData GenerateCrewInstance(string playerId)
```
Generates a unique crew instance with rolled stats.

**Returns**: `CrewInstanceData` with:
- Unique crew ID (GUID)
- Random name (from name generator)
- Rolled stats (7-15 range)
- Calculated sailor count and weight
- Creation timestamp

### Calculate Stat at Level
```csharp
public int CalculateStatAtLevel(int baseValue, int level, bool isPrimary)
```
Calculate effective stat at given level with growth and classification bonus.

### Calculate Sailor Count
```csharp
public int CalculateSailorCount(int level)
```
Calculate sailor count using GDD tiered scaling formula.

### Calculate Crew Weight
```csharp
public float CalculateCrewWeight(int sailorCount, int level)
```
Calculate crew weight using GDD formula.

### Calculate XP for Level
```csharp
public long CalculateXPForLevel(int targetLevel)
```
Calculate XP required for target level.

**Formula**: `100 × (level ^ 1.5)`

**Examples**:
- Level 10: 100 × (10^1.5) = 3,162 XP
- Level 50: 100 × (50^1.5) = 35,355 XP
- Level 100: 100 × (100^1.5) = 100,000 XP

### Get Stat Mapping
```csharp
public ClassificationStatMapping GetStatMapping()
```
Returns stat mapping for this crew's classification type.

### Get Rarity Color
```csharp
public Color GetRarityColor()
```
Returns Unity Color for UI based on rarity tier.

---

## CrewInstanceData Structure

Runtime instance of a crew card with rolled stats.

### Identity
- `crewId`: Unique ID (GUID)
- `playerId`: Owner player ID
- `templateId`: Reference to template
- `crewName`: Generated name
- `classificationType`: Crew classification

### Progression
- `level`: Current level (1-200)
- `currentXP`: Current experience points

### Rolled Stats (7-15 base)
- `basePrimaryStat`: Rolled primary stat (7-15)
- `baseSecondaryStat`: Rolled secondary stat (7-15)
- `baseGeneralStat`: Rolled general stat (7-12)

### Crew Size
- `sailorCount`: Current sailor count
- `crewWeight`: Crew weight in tons
- `currentSailors`: After casualties

### Assignment
- `isAssigned`: Is crew assigned to ship?
- `assignedShipId`: Ship ID
- `assignedPosition`: Position identifier

### Instance Methods
- `GetEffectivePrimaryStat()`: Calculate effective primary stat at current level
- `GetEffectiveSecondaryStat()`: Calculate effective secondary stat at current level

---

## Usage Example

```csharp
// Create via Unity menu: Create > WOS > Crew > Crew Template
CrewTemplateSO veteranGunner = // from database

// Generate crew instance
CrewInstanceData crew = veteranGunner.GenerateCrewInstance("player_12345");

Debug.Log($"Crew: {crew.crewName}"); // "John Smith"
Debug.Log($"Level: {crew.level}");
Debug.Log($"Gunnery: {crew.basePrimaryStat}"); // Rolled 7-15
Debug.Log($"Sailors: {crew.sailorCount}");
Debug.Log($"Weight: {crew.crewWeight} tons");

// Calculate stats at higher level
int level50Gunnery = veteranGunner.CalculateStatAtLevel(crew.basePrimaryStat, 50, true);
Debug.Log($"At Level 50: {level50Gunnery} Gunnery");

// Calculate sailor count at level 100
int sailorsL100 = veteranGunner.CalculateSailorCount(100);
Debug.Log($"At Level 100: {sailorsL100} sailors");

// Get XP requirement
long xpNeeded = veteranGunner.CalculateXPForLevel(50);
Debug.Log($"XP for Level 50: {xpNeeded}");
```

---

## Integration Points

### Used By
- **PlayFabCrewService.cs** - Crew instance generation and management
- **CrewManager.cs** - Crew assignment and progression
- **ItemDatabaseSO.cs** - Master crew database
- **EquipmentPanel.cs** - Crew UI display

### Related Systems
- **ClassificationStatMapping** - Stat mapping data
- **QualityGenerator** - Quality variance (similar system for modules)
- **StatRangeInt** - Integer range data structure
- **CrewInstanceData** - Runtime crew instance

---

## Create via Unity Menu

**Path**: `Create > WOS > Crew > Crew Template`

**Order**: 20

**Default Filename**: `Crew_Gunner_Veteran`
