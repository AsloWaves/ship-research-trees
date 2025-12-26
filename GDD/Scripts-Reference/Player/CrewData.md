# CrewData.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/Data/CrewData.cs` |
| **Namespace** | `WOS.Player.Data` |
| **Inheritance** | None (Serializable data classes) |
| **Lines of Code** | 513 |
| **Architecture** | Navy Field crew progression system with level 1-200 scaling |

## Purpose

`CrewData.cs` implements the **Navy Field-style crew progression system** with crew cards that level from 1-200, gain XP, suffer casualties in combat, and provide performance bonuses based on level and sailor count.

Key features:
- **CrewCard**: Individual crew member with level progression (1-200)
- **CrewCollection**: Player's roster of all crew cards
- **CrewXPCalculator**: Combat XP and casualty rate formulas
- **Navy Field Formulas**: Authentic sailor scaling and weight calculations

## CrewCard Class

### Crew Identity

| Field | Type | Description |
|-------|------|-------------|
| `CrewId` | `string` | UUID from database |
| `PlayerId` | `string` | Owner's player ID |
| `CrewName` | `string` | Player-defined or generated name |
| `Classification` | `CrewClassification` | Gunner, Engineer, Navigator, etc. |

### Navy Field Progression (Levels 1-200)

| Field | Type | Description |
|-------|------|-------------|
| `CurrentLevel` | `int` | Current level (1-200) |
| `CurrentXP` | `long` | Current experience points |

### Crew Size & Weight

| Field | Type | Description |
|-------|------|-------------|
| `MaxSailors` | `int` | Maximum sailors at current level |
| `CurrentSailors` | `int` | Current sailors (after casualties) |
| `CrewWeight` | `float` | Weight in tons (sailors × 0.1 × level modifier) |

### Assignment

| Field | Type | Description |
|-------|------|-------------|
| `IsAssigned` | `bool` | Whether assigned to a ship |
| `AssignedShipId` | `string` | Ship UUID (null if unassigned) |
| `AssignedPosition` | `string` | Position on ship (e.g., "Main Battery 1") |

## Navy Field Formulas (Static Methods)

### Sailor Count Scaling

```csharp
public static int CalculateMaxSailors(int level)
{
    if (level <= 50)
    {
        // Levels 1-50: 10 + (Level - 1) × 5
        return 10 + (level - 1) * 5;
    }
    else if (level <= 100)
    {
        // Levels 51-100: 255 + (Level - 50) × 4
        return 255 + (level - 50) * 4;
    }
    else
    {
        // Levels 101-200: 455 + (Level - 100) × 2.5
        return 455 + (int)((level - 100) * 2.5f);
    }
}
```

**GDD Formula**: Tiered scaling for realistic naval crew sizes.

| Level Range | Formula | Example |
|-------------|---------|---------|
| 1-50 | `10 + (Level - 1) × 5` | Level 1 = 10 sailors<br>Level 50 = 255 sailors |
| 51-100 | `255 + (Level - 50) × 4` | Level 100 = 455 sailors |
| 101-200 | `455 + (Level - 100) × 2.5` | Level 200 = 705 sailors |

### Crew Weight Calculation

```csharp
public static float CalculateCrewWeight(int sailorCount, int level)
{
    float baseWeight = 0.1f;  // 0.1 ton per sailor
    float levelModifier = 1.0f + (level / 100f);  // 1.0 + (Level / 100)
    return sailorCount * baseWeight * levelModifier;
}
```

**GDD Formula**: `Sailor Count × Base Weight (0.1 ton) × Level Modifier`

**Level Modifier**: `1.0 + (Level / 100)`
- Higher level crew = heavier weight per sailor (better trained = more equipment)

| Level | Sailors | Weight Calculation | Total Weight |
|-------|---------|-------------------|--------------|
| 1 | 10 | `10 × 0.1 × 1.01` | 1.01 tons |
| 20 | 105 | `105 × 0.1 × 1.20` | 12.6 tons |
| 50 | 255 | `255 × 0.1 × 1.50` | 38.25 tons |
| 100 | 455 | `455 × 0.1 × 2.00` | 91.0 tons |
| 200 | 705 | `705 × 0.1 × 3.00` | 211.5 tons |

### XP Requirements

```csharp
public static long CalculateXPForLevel(int targetLevel)
{
    return (long)(100 * Math.Pow(targetLevel, 1.5));
}

public static long CalculateXPForNextLevel(int currentLevel)
{
    return CalculateXPForLevel(currentLevel + 1) - CalculateXPForLevel(currentLevel);
}
```

**Formula**: `100 × (Level ^ 1.5)`

| Level | Total XP Required | XP for Next Level |
|-------|-------------------|-------------------|
| 1 | 100 | 182 |
| 10 | 3,162 | 739 |
| 50 | 35,355 | 2,466 |
| 100 | 100,000 | 4,025 |
| 200 | 282,843 | - |

### Crew Efficiency

```csharp
public static float CalculateCrewEfficiency(int crewLevel, int equipmentTier)
{
    int targetLevel = equipmentTier * 20; // T1=20, T5=100, T7=140
    int levelGap = crewLevel - targetLevel;
    float efficiency = 1.0f + (levelGap * 0.02f); // ±2% per level difference

    // Clamp to 20%-200%
    return Mathf.Clamp(efficiency, 0.2f, 2.0f);
}
```

**Formula**: `100% base + (level_gap × 2%)`

| Scenario | Crew Level | Equipment Tier | Target Level | Efficiency |
|----------|------------|----------------|--------------|------------|
| Perfect match | 100 | T5 (100) | 100 | 100% |
| Overqualified | 120 | T5 (100) | 100 | 140% (+40%) |
| Underqualified | 80 | T5 (100) | 100 | 60% (-40%) |
| Max efficiency | 140+ | T5 (100) | 100 | 200% (capped) |
| Min efficiency | 60- | T5 (100) | 100 | 20% (capped) |

**Design Intent**: Higher level crew operates equipment more effectively, but lower level crew can still use high-tier equipment at reduced efficiency.

## Instance Methods

### Level Progression

```csharp
public int AddXP(long xpGain)
{
    CurrentXP += xpGain;
    int levelsGained = 0;

    // Check for level-ups (can gain multiple levels at once)
    while (CurrentLevel < 200)
    {
        long xpRequired = CalculateXPForLevel(CurrentLevel + 1);

        if (CurrentXP >= xpRequired)
        {
            CurrentLevel++;
            levelsGained++;
            RecalculateStats(); // Recalculate sailors and weight
        }
        else
        {
            break;
        }
    }

    UpdatedAt = DateTime.Now;
    return levelsGained;
}
```

**Purpose**: Add XP and automatically level up crew when threshold reached. Can gain multiple levels from a single XP gain.

**Returns**: Number of levels gained (0 if no level-up)

### Casualty System

```csharp
public int ApplyCasualties(float casualtyPercent)
{
    int sailorsLost = (int)(CurrentSailors * casualtyPercent);
    CurrentSailors -= sailorsLost;

    // Minimum 10% of max sailors must survive (critically undermanned)
    int minSailors = (int)(MaxSailors * 0.1f);
    if (CurrentSailors < minSailors)
    {
        CurrentSailors = minSailors;
    }

    UpdatedAt = DateTime.Now;
    return sailorsLost;
}
```

**Purpose**: Apply casualties to crew when ship takes damage in combat.

**Parameters**: `casualtyPercent` - Percentage of current sailors lost (0.0 - 1.0)

**Returns**: Number of sailors lost

**Safety**: Crew can never fall below 10% of max sailors (critically undermanned but not wiped out)

### Undermanned Penalties

```csharp
public bool IsUndermanned()
{
    return CurrentSailors < (MaxSailors * 0.5f);
}

public float GetUndermannedPenalty()
{
    float sailorRatio = (float)CurrentSailors / MaxSailors;

    if (sailorRatio >= 1.0f)
        return 1.0f; // Full efficiency

    if (sailorRatio >= 0.5f)
        return 0.75f + (sailorRatio - 0.5f) * 0.5f; // 0.75x to 1.0x

    return 0.5f + (sailorRatio - 0.1f) * 0.625f; // 0.5x to 0.75x
}
```

**Undermanned Thresholds**:

| Sailor Ratio | Efficiency | Status |
|--------------|------------|--------|
| 100% | 1.0x | Full strength |
| 75% | 0.875x | Reduced |
| 50% | 0.75x | Undermanned |
| 25% | 0.625x | Critically undermanned |
| 10% | 0.5x | Minimal crew (survival mode) |

### Total Efficiency

```csharp
public float GetTotalEfficiency(int equipmentTier)
{
    float levelEfficiency = CalculateCrewEfficiency(CurrentLevel, equipmentTier);
    float undermannedPenalty = GetUndermannedPenalty();
    return levelEfficiency * undermannedPenalty;
}
```

**Purpose**: Combine level efficiency and undermanned penalty for final equipment performance.

**Example**:
- Level 120 crew on T5 equipment = 140% level efficiency
- 75% sailors remaining = 0.875x undermanned penalty
- Total efficiency = `1.4 × 0.875 = 1.225x` (122.5%)

## CrewCollection Class

### Purpose
Manages the player's roster of all crew cards.

### Key Methods

```csharp
// Get crew by ID
public CrewCard GetCrewById(string crewId)

// Get unassigned crew (available for assignment)
public List<CrewCard> GetUnassignedCrew()

// Get crew by classification (Gunner, Engineer, etc.)
public List<CrewCard> GetCrewByClassification(CrewClassification classification)

// Get crew assigned to specific ship
public List<CrewCard> GetCrewAssignedToShip(string shipId)

// Get total crew weight for specific ship
public float GetTotalCrewWeightForShip(string shipId)

// Get average crew level
public float GetAverageCrewLevel()
```

## CrewXPCalculator (Static Helper)

### Combat XP Formula

```csharp
public static long CalculateCombatXP(int shipTier, int enemyShipsKilled,
    float damageDealt, bool isVictory)
{
    // Base XP per combat
    long baseXP = 100;

    // Tier multiplier (T1=1x, T7=7x)
    float tierMultiplier = shipTier;

    // Kill bonus (+50 XP per kill)
    long killBonus = enemyShipsKilled * 50;

    // Damage bonus (damage_dealt / 1000 XP)
    long damageBonus = (long)(damageDealt / 1000f);

    // Victory bonus (+50% if team won)
    float victoryMultiplier = isVictory ? 1.5f : 1.0f;

    // Total XP
    long totalXP = (long)((baseXP * tierMultiplier + killBonus + damageBonus)
        * victoryMultiplier);

    return totalXP;
}
```

**Formula**: `(Base XP × Tier + Kill Bonus + Damage Bonus) × Victory Multiplier`

**Example Calculation**:
- T5 match (tier multiplier = 5x)
- 2 kills (+100 XP)
- 50,000 damage dealt (+50 XP)
- Victory (+50% multiplier)
- **Total**: `(100 × 5 + 100 + 50) × 1.5 = 975 XP`

### Casualty Rate Formula

```csharp
public static float CalculateCasualtyRate(int shipTier, float damagePercent)
{
    float baseCasualtyRate = 0f;

    switch (shipTier)
    {
        case 1:
        case 2:
        case 3:
            baseCasualtyRate = 0f; // Low-tier is safe
            break;
        case 4:
            baseCasualtyRate = 0.1f; // 10% base
            break;
        case 5:
            baseCasualtyRate = 0.2f; // 20% base
            break;
        case 6:
            baseCasualtyRate = 0.3f; // 30% base
            break;
        case 7:
            baseCasualtyRate = 0.6f; // 60% base (very dangerous)
            break;
    }

    // Scale by damage taken (more damage = more casualties)
    float casualtyRate = baseCasualtyRate * damagePercent;

    return Mathf.Clamp01(casualtyRate); // Max 100% casualties
}
```

**Tier-Based Casualty Rates**:

| Tier | Base Rate | Example (50% damage) | Example (100% damage) |
|------|-----------|----------------------|-----------------------|
| T1-T3 | 0% | 0% | 0% (safe training grounds) |
| T4 | 10% | 5% | 10% |
| T5 | 20% | 10% | 20% |
| T6 | 30% | 15% | 30% |
| T7 | 60% | 30% | 60% (high-stakes combat) |

## Crew Classifications

```csharp
public enum CrewClassification
{
    Gunner,             // Main/Secondary battery crew
    Engineer,           // Engine room crew
    Navigator,          // Navigation and helm
    DamageControl,      // Repair and firefighting
    FireControl,        // Fire control systems
    AAGunner            // Anti-aircraft gunners
}
```

## Usage Examples

### Creating a New Crew Card

```csharp
CrewCard newCrew = new CrewCard(
    playerId: "player123",
    classification: CrewClassification.Gunner,
    crewName: "John Smith"
);

// Stats are automatically calculated for Level 1
// newCrew.MaxSailors = 10
// newCrew.CrewWeight = 1.01 tons
```

### Adding Combat XP

```csharp
// Award XP after match
long xpGained = CrewXPCalculator.CalculateCombatXP(
    shipTier: 5,
    enemyShipsKilled: 2,
    damageDealt: 50000f,
    isVictory: true
);

int levelsGained = crewCard.AddXP(xpGained);

if (levelsGained > 0)
{
    Debug.Log($"{crewCard.CrewName} leveled up! Now level {crewCard.CurrentLevel}");
    Debug.Log($"Max sailors: {crewCard.MaxSailors}, Weight: {crewCard.CrewWeight} tons");
}
```

### Applying Combat Casualties

```csharp
// Ship took 75% damage in T7 combat
float casualtyRate = CrewXPCalculator.CalculateCasualtyRate(
    shipTier: 7,
    damagePercent: 0.75f
);
// casualtyRate = 0.6 × 0.75 = 0.45 (45% casualties)

int sailorsLost = crewCard.ApplyCasualties(casualtyRate);

Debug.Log($"{crewCard.CrewName} lost {sailorsLost} sailors");
Debug.Log($"Remaining: {crewCard.CurrentSailors}/{crewCard.MaxSailors}");

if (crewCard.IsUndermanned())
{
    Debug.LogWarning("Crew is undermanned - reduced efficiency!");
    float penalty = crewCard.GetUndermannedPenalty();
    Debug.Log($"Efficiency penalty: {penalty * 100f}%");
}
```

### Checking Crew Efficiency

```csharp
// Level 120 Gunner operating T5 main battery turret
float efficiency = crewCard.GetTotalEfficiency(equipmentTier: 5);

// Calculate effective damage
TurretEquipment turret = GetMainBattery();
float effectiveDamage = turret.Damage * efficiency;

Debug.Log($"Crew efficiency: {efficiency * 100f}%");
Debug.Log($"Base damage: {turret.Damage}, Effective: {effectiveDamage}");
```

### Managing Crew Roster

```csharp
CrewCollection roster = new CrewCollection();

// Get available gunners
List<CrewCard> gunners = roster.GetCrewByClassification(CrewClassification.Gunner);
List<CrewCard> availableGunners = roster.GetUnassignedCrew()
    .Where(c => c.Classification == CrewClassification.Gunner)
    .ToList();

// Get crew on specific ship
float totalCrewWeight = roster.GetTotalCrewWeightForShip("ship-uuid-123");

// Check roster strength
float avgLevel = roster.GetAverageCrewLevel();
Debug.Log($"Average crew level: {avgLevel}");
```

## Integration Points

### Database Persistence
- **Table**: `crew_cards`
- **Primary Key**: `CrewId` (UUID)
- **Foreign Key**: `PlayerId` references `players.player_id`
- **Persistence Service**: `PlayFabCrewService` handles loading/saving

### Related Systems

| System | Integration |
|--------|-------------|
| **CrewManager** | Server-authoritative crew management and progression |
| **PlayerShipData** | Crew assignments stored in `ShipLoadout.Crew` |
| **EquipmentData** | Crew efficiency affects equipment performance |
| **Combat System** | Awards XP and applies casualties based on combat results |

## Design Notes

### Navy Field Authenticity

The crew system replicates the **Navy Field** progression mechanics:
1. **Tiered Sailor Scaling**: Realistic crew sizes (10 → 705 sailors)
2. **Level-Based Weight**: Higher level crew = more equipment weight
3. **Combat Casualties**: Higher tier = higher risk
4. **Efficiency System**: Crew level vs. equipment tier matching
5. **XP Curve**: Exponential scaling to level 200

### Weight Progression Design

Crew weight increases with level for two reasons:
1. **Game Balance**: Prevent overpowered low-weight high-level crew
2. **Realism**: Higher trained crews carry more equipment and supplies

This creates strategic choices:
- Use high-level crew for maximum performance (but heavier)
- Use mid-level crew for weight-constrained builds
- Balance crew levels across positions for optimal weight distribution

### Casualty Recovery

Casualties are **permanent** until crew levels up:
- Lost sailors do NOT regenerate over time
- Leveling up restores crew to max sailors (recruits replace casualties)
- This creates tension: risk crew in T7 combat for XP, but may suffer heavy losses

**Minimum Survival**: Crew can never fall below 10% max sailors to prevent total wipeout.

### Efficiency Clamping

Efficiency is clamped to **20%-200%** to prevent extreme edge cases:
- **Minimum 20%**: Even Level 1 crew on T7 equipment can function (poorly)
- **Maximum 200%**: Prevents runaway scaling from overleveled crew

This ensures gameplay remains balanced across all tier combinations.

### Auto-Leveling Logic

The `AddXP()` method handles **multiple level-ups** in a single call:
```csharp
while (CurrentLevel < 200)
{
    if (CurrentXP >= CalculateXPForLevel(CurrentLevel + 1))
    {
        CurrentLevel++;
        levelsGained++;
        RecalculateStats();
    }
    else break;
}
```

This prevents bugs when awarding massive XP bonuses (e.g., event rewards, admin commands).

### Random Name Generation

Default crew names use a simple random combination system:
```csharp
string[] firstNames = { "John", "William", "James", ... };
string[] lastNames = { "Smith", "Johnson", "Brown", ... };
```

Players can override these with custom names. Future enhancement: nationality-based name pools matching ship nation.
