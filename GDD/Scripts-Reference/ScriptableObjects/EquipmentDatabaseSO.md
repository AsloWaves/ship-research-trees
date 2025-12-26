# EquipmentDatabaseSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Database/EquipmentDatabaseSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Database` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | 311 |

---

## Purpose

**Specialized equipment database** with advanced query and filtering capabilities. Focused on ship equipment (turrets, torpedoes, modules) with nation, tier, era, and caliber filtering.

**Difference from ItemDatabaseSO**:
- **ItemDatabaseSO**: General item database for all items
- **EquipmentDatabaseSO**: Specialized database for equipment with advanced filters

---

## Equipment Collections

| Property | Type | Description |
|----------|------|-------------|
| `turrets` | `List<TurretDefinitionSO>` | All turret definitions in the game |
| `torpedoes` | `List<TorpedoDefinitionSO>` | All torpedo launcher definitions |
| `modules` | `List<ModuleDefinitionSO>` | All module definitions (radar, fire control, etc.) |

---

## Database Stats

| Property | Type | Description |
|----------|------|-------------|
| `totalEquipment` | `int` (SerializeField) | Total equipment count |
| `turretsWithoutSprites` | `int` (SerializeField) | Turrets missing icon sprites |
| `turretsWithoutGeometry` | `int` (SerializeField) | Turrets missing muzzle geometry |
| `lastValidation` | `string` (SerializeField) | Last validation timestamp |

**Updated by**: `UpdateStats()` method

---

## Turret Query Methods

### Get Turrets by Nation
```csharp
public List<TurretDefinitionSO> GetTurretsByNation(EquipmentNation nation)
```
Get all turrets for a specific nation (USA, Japan, Britain, etc.).

### Get Turrets by Tier
```csharp
public List<TurretDefinitionSO> GetTurretsByTier(int tier)
```
Get all turrets of a specific tier (1-7).

### Get Turrets by Type
```csharp
public List<TurretDefinitionSO> GetTurretsByType(TurretCategory category)
```
Get all turrets by category (Main, Secondary, AA, DualPurpose).

### Get Turrets by Caliber Range
```csharp
public List<TurretDefinitionSO> GetTurretsByCaliberRange(float minCaliber, float maxCaliber)
```
Get all turrets within a caliber range (inches).

**Example**: `GetTurretsByCaliberRange(5f, 8f)` → All 5"-8" guns

### Get Turrets by Era
```csharp
public List<TurretDefinitionSO> GetTurretsByEra(Era era)
```
Get all turrets from a specific era (PreDreadnought, WWI, WWII, etc.).

### Filter Turrets (Combined)
```csharp
public List<TurretDefinitionSO> FilterTurrets(
    EquipmentNation? nation = null,
    int? tier = null,
    TurretCategory? category = null,
    Era? era = null,
    float? minCaliber = null,
    float? maxCaliber = null)
```
**Advanced combined filter** with optional parameters.

**Example**: Get all USA WWII-era 5" dual-purpose guns
```csharp
var results = database.FilterTurrets(
    nation: EquipmentNation.USA,
    era: Era.WWII,
    category: TurretCategory.DualPurpose,
    minCaliber: 5f,
    maxCaliber: 5f
);
```

### Get Turret by ID
```csharp
public TurretDefinitionSO GetTurretById(string equipmentId)
```
Find turret by equipment ID.

---

## Torpedo Query Methods

### Get Torpedoes by Nation
```csharp
public List<TorpedoDefinitionSO> GetTorpedoesByNation(EquipmentNation nation)
```
Get all torpedoes for a specific nation.

### Get Torpedoes by Tier
```csharp
public List<TorpedoDefinitionSO> GetTorpedoesByTier(int tier)
```
Get all torpedoes of a specific tier.

### Get Torpedo by ID
```csharp
public TorpedoDefinitionSO GetTorpedoById(string equipmentId)
```
Find torpedo by equipment ID.

---

## General Query Methods

### Get Equipment by ID
```csharp
public EquipmentDefinitionSO GetEquipmentById(string equipmentId)
```
Get **any equipment** by ID (searches all categories: turrets, torpedoes, modules).

**Search Order**: Turrets → Torpedoes → Modules

### Get All Equipment by Nation
```csharp
public List<EquipmentDefinitionSO> GetAllEquipmentByNation(EquipmentNation nation)
```
Get all equipment (turrets, torpedoes, modules) for a nation.

---

## Validation

### Validate Database
```csharp
public ValidationReport ValidateDatabase()
```
Validate all equipment entries and report issues.

**Returns**: `ValidationReport` with errors, warnings, and info messages.

**Validation Checks**:
- Null equipment references
- Empty equipment IDs
- Missing icon sprites
- Missing muzzle exit points
- Muzzle count vs barrel count mismatch
- Duplicate equipment IDs

**Example Output**:
```
Validation: 2 errors, 5 warnings
Errors:
- Null turret reference in database
- Duplicate equipment ID: MainBattery_T5_16inch
Warnings:
- Turret 'Mark 12 5"/38' has no icon sprite
- Turret '16"/50 Mark 7' muzzle count (2) doesn't match barrel count (3)
```

### Update Stats
```csharp
public void UpdateStats()
```
Update cached statistics (total equipment, missing sprites, missing geometry, validation timestamp).

**Called automatically** by `ValidateDatabase()`.

---

## Statistics

### Get Equipment Count by Nation
```csharp
public Dictionary<EquipmentNation, int> GetEquipmentCountByNation()
```
Returns dictionary of equipment counts per nation.

**Example**:
```csharp
var counts = database.GetEquipmentCountByNation();
Debug.Log($"USA: {counts[EquipmentNation.USA]} equipment");
Debug.Log($"Japan: {counts[EquipmentNation.Japan]} equipment");
```

### Get Turret Count by Tier
```csharp
public Dictionary<int, int> GetTurretCountByTier()
```
Returns dictionary of turret counts per tier (1-7).

**Example**:
```csharp
var counts = database.GetTurretCountByTier();
for (int tier = 1; tier <= 7; tier++)
{
    Debug.Log($"Tier {tier}: {counts[tier]} turrets");
}
```

---

## ValidationReport Structure

```csharp
[Serializable]
public class ValidationReport
{
    public List<string> errors;
    public List<string> warnings;
    public List<string> info;

    public bool HasErrors { get; }
    public bool HasWarnings { get; }
    public bool IsValid { get; }

    public override string ToString();
}
```

**Properties**:
- `HasErrors`: True if any errors exist
- `HasWarnings`: True if any warnings exist
- `IsValid`: True if no errors (warnings allowed)

---

## Usage Example

```csharp
public EquipmentDatabaseSO equipmentDB;

void Example()
{
    // Get all USA turrets
    var usaTurrets = equipmentDB.GetTurretsByNation(EquipmentNation.USA);
    Debug.Log($"Found {usaTurrets.Count} USA turrets");

    // Get all Tier 5 turrets
    var tier5Turrets = equipmentDB.GetTurretsByTier(5);

    // Advanced filter: USA WWII 5" dual-purpose guns
    var results = equipmentDB.FilterTurrets(
        nation: EquipmentNation.USA,
        era: Era.WWII,
        category: TurretCategory.DualPurpose,
        minCaliber: 5f,
        maxCaliber: 5f
    );
    Debug.Log($"Found {results.Count} matching turrets");

    // Get equipment by ID
    var equipment = equipmentDB.GetEquipmentById("MainBattery_T5_16inch");
    if (equipment != null)
    {
        Debug.Log($"Found: {equipment.equipmentName}");
    }

    // Validate database
    var report = equipmentDB.ValidateDatabase();
    if (report.HasErrors)
    {
        Debug.LogError($"Database validation failed: {report}");
    }

    // Get statistics
    var nationCounts = equipmentDB.GetEquipmentCountByNation();
    var tierCounts = equipmentDB.GetTurretCountByTier();
}
```

---

## Setup Workflow

### Step 1: Create Database Asset
1. Right-click in Project window
2. `Create > WOS > Database > Equipment Database`
3. Name it "EquipmentDatabase"

### Step 2: Populate Collections
1. Select EquipmentDatabase asset
2. Drag equipment ScriptableObjects into lists:
   - Turrets → `turrets` list
   - Torpedoes → `torpedoes` list
   - Modules → `modules` list

### Step 3: Validate
1. Right-click EquipmentDatabase
2. Inspector shows validation stats
3. Run `ValidateDatabase()` to check for issues

---

## Integration Points

### Used By
- **EquipmentPanel.cs** - Equipment filtering and display
- **ShopManager.cs** - Equipment catalog generation
- **LoadoutEditor.cs** - Equipment selection UI
- **BalanceTools (Editor)** - Equipment balance analysis

### Related Systems
- **ItemDatabaseSO** - General item database
- **TurretDefinitionSO** - Turret equipment
- **TorpedoDefinitionSO** - Torpedo equipment
- **ModuleDefinitionSO** - Module equipment

---

## Design Notes

### Why Separate from ItemDatabaseSO?

**EquipmentDatabaseSO** provides:
1. **Advanced Filtering**: Nation, tier, era, caliber filters
2. **Equipment-Specific Validation**: Geometry, sprites, muzzle points
3. **Statistics**: Equipment distribution analysis
4. **Performance**: Optimized for equipment queries

**ItemDatabaseSO** is general-purpose for all items.

### Validation Philosophy

**Strict validation** catches content errors early:
- Missing sprites → Players see placeholder icons
- Missing geometry → Turrets render incorrectly
- Duplicate IDs → Database lookup failures
- Barrel/muzzle mismatch → Visual glitches

**Run validation before build** to ensure content quality.

### Filter Performance

**LINQ-based filtering** is efficient for small-medium databases (<1000 items).

For large databases, consider:
- Caching filter results
- Pre-building lookup dictionaries
- Using HashSet for membership tests

### Statistics Use Cases

**Equipment distribution statistics** help with:
- **Balance Analysis**: Are all nations represented equally?
- **Content Planning**: Which tiers need more equipment?
- **QA Testing**: Which equipment categories are missing content?

---

## Create via Unity Menu

**Path**: `Create > WOS > Database > Equipment Database`

**Order**: 0

**Default Filename**: `EquipmentDatabase`
