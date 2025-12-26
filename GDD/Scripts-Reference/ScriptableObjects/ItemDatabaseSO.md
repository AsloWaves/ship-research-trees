# ItemDatabaseSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Database/ItemDatabaseSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Database` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | 415 |

---

## Purpose

**Master item database** - central registry for all equipment, cargo, consumables, crew templates, and ship definitions. Provides lookup, filtering, and validation utilities.

**Single Source of Truth**: One ItemDatabaseSO asset (e.g., "MasterItemDatabase") contains all game items.

---

## Equipment Collections

| Property | Type | Description |
|----------|------|-------------|
| `turrets` | `List<TurretDefinitionSO>` | All turret definitions |
| `torpedoes` | `List<TorpedoDefinitionSO>` | All torpedo launcher definitions |
| `engines` | `List<EngineDefinitionSO>` | All engine definitions |
| `modules` | `List<ModuleDefinitionSO>` | All module definitions |

---

## Items Collections

| Property | Type | Description |
|----------|------|-------------|
| `cargoItems` | `List<CargoItemDefinitionSO>` | All cargo item definitions |
| `consumables` | `List<ConsumableItemDefinitionSO>` | All consumable item definitions |

---

## Crew & Ships

| Property | Type | Description |
|----------|------|-------------|
| `crewTemplates` | `List<CrewTemplateSO>` | All crew template definitions |
| `shipDefinitions` | `List<ShipDefinitionSO>` | All ship definition ScriptableObjects |

---

## Generic Items

| Property | Type | Description |
|----------|------|-------------|
| `items` | `List<ItemDefinitionSO>` | General item definitions (for ItemDatabase.cs compatibility) |

---

## Initialization

### Initialize
```csharp
public void Initialize()
```
Initialize the database and build lookup caches for performance.

**Caching**: Builds dictionary for O(1) item lookups by ID.

**Call this once** at game startup (e.g., in startup scene or manager Awake()).

### Item Count
```csharp
public int ItemCount { get; }
```
Total count of generic items.

---

## Generic Item Lookup Methods

### Get Item by ID
```csharp
public ItemDefinitionSO GetItem(string itemId)
```
Get item definition by ID using cached lookup (O(1) after initialization).

### Has Item
```csharp
public bool HasItem(string itemId)
```
Check if item exists in database.

### Get Items by Category
```csharp
public List<ItemDefinitionSO> GetItemsByCategory(ItemCategory category)
```
Get all items of specific category.

### Get Tradeable Items
```csharp
public List<ItemDefinitionSO> GetTradeableItems(bool includeContraband = false)
```
Get all tradeable items (optionally include contraband).

### Get Usable Items
```csharp
public List<ItemDefinitionSO> GetUsableItems()
```
Get all usable items.

### Search Items
```csharp
public List<ItemDefinitionSO> SearchItems(string query)
```
Search items by name, description, or ID (case-insensitive).

---

## Equipment Lookup Methods

### Get Turret
```csharp
public TurretDefinitionSO GetTurret(string equipmentId)
```
Get turret by equipment ID.

### Get Engine
```csharp
public EngineDefinitionSO GetEngine(string equipmentId)
```
Get engine by equipment ID.

### Get Module
```csharp
public ModuleDefinitionSO GetModule(string equipmentId)
```
Get module by equipment ID.

### Get Torpedo
```csharp
public TorpedoDefinitionSO GetTorpedo(string equipmentId)
```
Get torpedo launcher by equipment ID.

### Get Cargo Item
```csharp
public CargoItemDefinitionSO GetCargoItem(string itemId)
```
Get cargo item by item ID.

### Get Consumable
```csharp
public ConsumableItemDefinitionSO GetConsumable(string itemId)
```
Get consumable by item ID.

### Get Crew Template
```csharp
public CrewTemplateSO GetCrewTemplate(string templateId)
```
Get crew template by template ID.

### Get Ship Definition
```csharp
public ShipDefinitionSO GetShipDefinition(string shipDefinitionId)
```
Get ship definition by ship definition ID.

---

## Filtering Methods

### Get Equipment by Tier
```csharp
public List<EquipmentDefinitionSO> GetEquipmentByTier(int tier)
```
Get all equipment (turrets, torpedoes, engines, modules) of specific tier.

### Get Turrets by Type
```csharp
public List<TurretDefinitionSO> GetTurretsByType(TurretType type)
```
Get all turrets of specific type (Main, Secondary, AA).

### Get Crew by Classification
```csharp
public List<CrewTemplateSO> GetCrewByClassification(CrewClassificationType classificationType)
```
Get all crew templates of specific classification.

### Get Recruitable Crew
```csharp
public List<CrewTemplateSO> GetRecruitableCrew()
```
Get all crew templates available for recruitment.

### Get Cargo by Category
```csharp
public List<CargoItemDefinitionSO> GetCargoByCategory(CargoCategory category)
```
Get all cargo items by category.

---

## Validation & Utility

### Get Total Item Count
```csharp
public int GetTotalItemCount()
```
Get total count of all items across all categories.

**Includes**: turrets, torpedoes, engines, modules, cargo, consumables, crew, ships.

### Validate Database
```csharp
[ContextMenu("Validate Database")]
public void ValidateDatabase()
```
Validate database for missing references or duplicate IDs.

**Checks**:
- Null entries
- Empty equipment IDs
- Duplicate equipment IDs
- Missing icons

**Logs**: Errors and warnings to DebugManager.

### Export to JSON
```csharp
[ContextMenu("Export to JSON")]
public void ExportToJSON()
```
Generate all items as JSON for backend import.

**TODO**: Implement JSON export for backend seeding.

---

## Usage Example

```csharp
// Reference the master database
public ItemDatabaseSO masterDatabase;

void Awake()
{
    // Initialize database (builds lookup caches)
    masterDatabase.Initialize();
}

void Example()
{
    // Get turret by ID
    var turret = masterDatabase.GetTurret("MainBattery_T5_16inch");
    if (turret != null)
    {
        Debug.Log($"Found turret: {turret.equipmentName}");
    }

    // Get all Tier 5 equipment
    var tier5Equipment = masterDatabase.GetEquipmentByTier(5);
    Debug.Log($"Found {tier5Equipment.Count} Tier 5 equipment");

    // Get recruitable crew
    var recruitableCrew = masterDatabase.GetRecruitableCrew();
    foreach (var crew in recruitableCrew)
    {
        Debug.Log($"Recruitable: {crew.crewName}");
    }

    // Search items
    var searchResults = masterDatabase.SearchItems("fire control");
    Debug.Log($"Found {searchResults.Count} items matching 'fire control'");

    // Get total database size
    int totalItems = masterDatabase.GetTotalItemCount();
    Debug.Log($"Database contains {totalItems} total items");
}
```

---

## Setup Workflow

### Step 1: Create Database Asset
1. Right-click in Project window
2. `Create > WOS > Database > Item Database`
3. Name it "MasterItemDatabase"

### Step 2: Populate Collections
1. Select MasterItemDatabase asset
2. Drag ScriptableObjects into appropriate lists:
   - Turrets → `turrets` list
   - Torpedoes → `torpedoes` list
   - Modules → `modules` list
   - Crew → `crewTemplates` list
   - etc.

### Step 3: Validate
1. Right-click MasterItemDatabase
2. Select "Validate Database" from context menu
3. Fix any errors/warnings in Console

### Step 4: Reference in Managers
```csharp
public class InventoryManager : MonoBehaviour
{
    public ItemDatabaseSO database;

    void Awake()
    {
        database.Initialize();
    }
}
```

---

## Integration Points

### Used By
- **ServerInventoryManager.cs** - Server-side item management
- **PlayFabInventoryService.cs** - Item persistence
- **EquipmentPanel.cs** - Equipment UI
- **ShopManager.cs** - Shop catalog
- **LootManager.cs** - Loot generation

### Related Systems
- **EquipmentDatabaseSO** - Specialized equipment database
- **ItemDefinitionSO** - Generic item definition
- **EquipmentDefinitionSO** - Equipment base class
- **CrewTemplateSO** - Crew template definitions
- **ShipDefinitionSO** - Ship definitions

---

## Design Notes

### Single Source of Truth

**One database asset** contains all game items. This ensures:
- Consistent item lookups across all systems
- Easy validation (one place to check)
- Simple backend seeding (export one database)

### Performance Optimization

**Dictionary caching** after `Initialize()`:
- O(1) lookup by ID (instant)
- No linear search through lists
- Minimal memory overhead

**Call `Initialize()` once** at game startup.

### Validation System

**Built-in validation** catches common errors:
- Missing equipment IDs
- Duplicate IDs
- Null references
- Missing icons/prefabs

**Run validation** before building to ensure data integrity.

### Dual Item Systems

**Two item systems coexist**:
1. **ItemDefinitionSO**: Generic items (cargo, consumables)
2. **EquipmentDefinitionSO**: Ship equipment (turrets, modules, etc.)

ItemDatabaseSO supports **both systems** for compatibility.

---

## Create via Unity Menu

**Path**: `Create > WOS > Database > Item Database`

**Order**: 100

**Default Filename**: `MasterItemDatabase`
