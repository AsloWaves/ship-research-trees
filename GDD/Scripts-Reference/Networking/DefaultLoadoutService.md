# DefaultLoadoutService.cs

## Quick Reference

| **File** | DefaultLoadoutService.cs |
|----------|------------------------|
| **Namespace** | WOS.Networking.Managers |
| **Type** | Static Class |
| **Lines** | 411 |
| **Architecture** | Static service, ScriptableObject configuration, quality rolling system |

---

## Purpose

Service for generating default starting items from DefaultLoadoutConfigSO. Creates ItemData instances with rolled stats/quality from equipment and crew definitions. Integrates with PlayFabInventoryService to populate new player inventories.

---

## Configuration

### DefaultLoadoutConfigSO

**Path**: `Resources/Loadouts/DefaultLoadout`

**Structure**:
```csharp
public class DefaultLoadoutConfigSO : ScriptableObject
{
    public bool enabled;

    // Starting equipment
    public List<StartingEquipment> startingModules;
    public List<StartingEquipment> startingTurrets;
    public List<StartingEquipment> startingEngines;

    // Starting crew
    public List<StartingCrew> startingCrew;

    // Starting cargo
    public List<StartingCargo> startingCargo;

    // Starting economy
    public long startingCredits = 10000;
    public int startingPremiumCurrency = 0;
}
```

### Default Inventory Dimensions

| Parameter | Default Value |
|-----------|--------------|
| Grid Width | 10 |
| Grid Height | 10 |
| Max Weight | 5000kg |

---

## Public API

### Core Methods

#### `GenerateDefaultInventory(string playerId, DefaultLoadoutConfigSO config = null)`
Generates fully populated default inventory for new player.

**Parameters**:
- `playerId` - Player's PlayFab ID
- `config` - Optional override config (uses default from Resources if null)

**Returns**: `CargoGrid` - Populated with starting items

**Example**:
```csharp
CargoGrid inventory = DefaultLoadoutService.GenerateDefaultInventory(playFabId);
Debug.Log($"Created inventory with {inventory.Items.Count} starting items");
```

#### `GetDefaultConfig()`
Gets default loadout configuration from Resources.

**Returns**: `DefaultLoadoutConfigSO`

#### `ClearCache()`
Clears cached configuration (useful for editor refresh).

---

## Item Generation

### Equipment Generation

Equipment items are created with **rolled quality**:

```csharp
// Generate equipment with quality variance
private static ItemData CreateEquipmentItemData(EquipmentDefinitionSO definition, ...)
{
    // Roll quality (0.0 - 1.0)
    float quality = QualityGenerator.GenerateQualityPercent();

    // Apply minimum quality override if specified
    if (minimumQualityOverride > 0f)
    {
        quality = Mathf.Max(quality, minimumQualityOverride);
    }

    var tier = QualityGenerator.GetTierFromPercent(quality);
    string qualityName = QualityGenerator.GetQualityName(tier);

    // Create ItemData with rolled quality
    return new ItemData
    {
        QualityPercent = quality,          // e.g., 0.75 (75%)
        QualityTierName = qualityName,     // e.g., "Superior"
        EquipmentDefinitionId = definition.equipmentId,
        // ... other properties
    };
}
```

**Quality Tiers**:
- Common: 0.0 - 0.2
- Uncommon: 0.2 - 0.4
- Rare: 0.4 - 0.6
- Superior: 0.6 - 0.8
- Epic: 0.8 - 1.0

### Crew Generation

Crew cards are created with **rolled stats**:

```csharp
private static ItemData CreateCrewItemData(CrewTemplateSO template, ...)
{
    // Generate crew instance with rolled stats
    var crewInstance = template.GenerateCrewInstance(playerId);

    // Apply minimum stat override if specified
    if (minimumStatOverride > 0)
    {
        crewInstance.basePrimaryStat = Mathf.Max(crewInstance.basePrimaryStat, minimumStatOverride);
        // ... other stats
    }

    // Serialize full crew instance to JSON
    string crewInstanceJson = JsonUtility.ToJson(crewInstance);

    return new ItemData
    {
        ItemType = "CrewCard",
        ExtendedDataJson = crewInstanceJson,  // Full crew data
        EquipmentTier = crewInstance.level,
        EquipmentWeight = crewInstance.crewWeight,
        // ...
    };
}
```

### Cargo Generation

Cargo items are simple stacks:

```csharp
private static ItemData CreateCargoItemData(CargoItemDefinitionSO definition, int quantity)
{
    return new ItemData
    {
        ItemType = "Cargo",
        Quantity = Mathf.Min(quantity, definition.maxStack),
        ItemDefinitionId = definition.itemId,
        Size = new GridSize(definition.gridSize.x, definition.gridSize.y),
        // ...
    };
}
```

---

## Usage Example

### New Player Creation

```csharp
// Server-side new player initialization
[Server]
public void CreateNewPlayer(string playFabId)
{
    // Generate default inventory with starting items
    CargoGrid inventory = DefaultLoadoutService.GenerateDefaultInventory(playFabId);

    Debug.Log($"Created new player inventory:");
    Debug.Log($"  Total items: {inventory.Items.Count}");
    Debug.Log($"  Equipment: {inventory.Items.Count(i => i.ItemType == "Module" || i.ItemType == "Turret")}");
    Debug.Log($"  Crew cards: {inventory.Items.Count(i => i.ItemType == "CrewCard")}");
    Debug.Log($"  Cargo: {inventory.Items.Count(i => i.ItemType == "Cargo")}");

    // Save to PlayFab
    PlayFabInventoryService.Instance.SaveInventory(playFabId, inventory, 0, (newVersion, success) =>
    {
        if (success)
        {
            Debug.Log($"New player inventory saved (v{newVersion})");
        }
    });
}
```

### Custom Loadout Configuration

```csharp
// Create custom starter loadout in Unity Editor
[CreateAssetMenu(fileName = "StarterLoadout", menuName = "WOS/Loadouts/Starter Loadout")]
public class DefaultLoadoutConfigSO : ScriptableObject
{
    public bool enabled = true;

    [Header("Starting Equipment")]
    public List<StartingEquipment> startingModules = new List<StartingEquipment>
    {
        new StartingEquipment
        {
            equipmentDefinition = ModuleDefinitions.BasicArmor,
            quantity = 2,
            minimumQualityOverride = 0.5f  // Guarantee at least Rare quality
        }
    };

    [Header("Starting Crew")]
    public List<StartingCrew> startingCrew = new List<StartingCrew>
    {
        new StartingCrew
        {
            crewTemplate = CrewTemplates.BasicGunner,
            quantity = 3,
            minimumStatOverride = 10  // Guarantee at least 10 base stats
        }
    };

    [Header("Starting Economy")]
    public long startingCredits = 10000;
}
```

---

## Integration Points

### PlayFabInventoryService

```csharp
// PlayFabInventoryService.cs - New player creation
private CargoGrid CreateDefaultInventory(string playFabId)
{
    // Use DefaultLoadoutService for new player
    return DefaultLoadoutService.GenerateDefaultInventory(playFabId);
}
```

### LocalFileInventoryService

```csharp
// LocalFileInventoryService.cs - New player creation
private CargoGrid CreateDefaultInventory(string playFabId)
{
    // Use DefaultLoadoutService for new player
    var inventory = DefaultLoadoutService.GenerateDefaultInventory(playFabId);

    if (inventory != null)
    {
        Log($"Created default inventory with {inventory.Items.Count} starting items");
    }

    return inventory;
}
```

---

## Design Notes

### Quality Rolling System

**Why roll quality?**
- Adds variety to starting equipment
- Prevents all players having identical gear
- Creates sense of luck/RNG excitement
- Can be overridden for guaranteed quality

**Quality Override Example**:
```csharp
// VIP package: Guarantee Superior quality starting items
var config = DefaultLoadoutService.GetDefaultConfig();
foreach (var module in config.startingModules)
{
    module.minimumQualityOverride = 0.6f;  // Minimum 60% = Superior
}

var inventory = DefaultLoadoutService.GenerateDefaultInventory(playerId, config);
```

### Auto-Placement Algorithm

Items are auto-placed using Tetris-style algorithm:

```csharp
bool success = inventory.AutoPlaceItem(itemData);
```

**Algorithm**:
1. Try each grid position (left-to-right, top-to-bottom)
2. Check if item fits (width x height)
3. Check for collisions with existing items
4. Place at first valid position
5. If no valid position, item creation fails (logged as warning)

---

## Key Takeaways

1. **Static Service**: No instance needed, call directly from anywhere
2. **ScriptableObject Config**: Easy to customize starting items in Unity Editor
3. **Quality Rolling**: Equipment created with random quality (can override minimum)
4. **Stat Rolling**: Crew cards created with random stats (can override minimum)
5. **Auto-Placement**: Items automatically placed in inventory grid
6. **Integration Ready**: Used by PlayFabInventoryService and LocalFileInventoryService
