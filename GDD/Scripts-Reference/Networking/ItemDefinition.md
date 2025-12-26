# ItemDefinition.cs

## Quick Reference

| **File** | ItemDefinition.cs |
|----------|------------------|
| **Namespace** | WOS.Networking.Data |
| **Type** | Data Model |
| **Lines** | 81 |
| **Architecture** | JSON serialization, backend cache model |

---

## Purpose

Item type definition model that matches backend ItemDefinition. Defines properties of each item type (consumable, cargo, equipment) and is cached from backend API on server startup.

---

## ItemDefinition Class

```csharp
[Serializable]
public class ItemDefinition
{
    public string ItemId;
    public string ItemName;
    public string ItemType;
    public GridSize GridSize;
    public Dictionary<string, object> Properties;
    public int MaxStack = 1;
    public bool IsTradeable = true;
    public bool IsConsumable = false;
    public int BaseValue;
    public float Weight;
}
```

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `ItemId` | string | Unique item identifier |
| `ItemName` | string | Display name |
| `ItemType` | string | Type: "Consumable", "Cargo", "Equipment", etc. |
| `GridSize` | GridSize | Tetris-style inventory size (width x height) |
| `Properties` | Dictionary<string, object> | Custom item properties (JSON) |
| `MaxStack` | int | Maximum stack size (default: 1) |
| `IsTradeable` | bool | Can be traded (default: true) |
| `IsConsumable` | bool | Is consumed on use (default: false) |
| `BaseValue` | int | Base price in credits |
| `Weight` | float | Weight in kg/tons |

---

## GridSize Class

Defines Tetris-style inventory placement dimensions.

```csharp
[Serializable]
public class GridSize
{
    public int Width;
    public int Height;

    public GridSize() { }

    public GridSize(int width, int height)
    {
        Width = width;
        Height = height;
    }
}
```

**Examples**:
- 1x1: Small items (ammo, consumables)
- 2x2: Medium items (modules)
- 3x2: Large items (turrets)
- 4x3: Huge items (engines)

---

## Public API

### Static Methods

#### `FromJson(string json)`
Creates an ItemDefinition from backend JSON response.

**Returns**: `ItemDefinition`

**Example**:
```csharp
string json = "{ \"ItemId\": \"item_cannon\", \"ItemName\": \"Cannon\", ... }";
var definition = ItemDefinition.FromJson(json);
```

#### `FromJsonArray(string json)`
Creates a list of ItemDefinitions from backend JSON array.

**Returns**: `List<ItemDefinition>`

**Example**:
```csharp
string json = "[{ \"ItemId\": \"item_1\", ... }, { \"ItemId\": \"item_2\", ... }]";
var definitions = ItemDefinition.FromJsonArray(json);
```

### Instance Methods

#### `ToJson()`
Converts to JSON for sending to backend.

**Returns**: `string`

**Example**:
```csharp
var definition = new ItemDefinition { ItemId = "item_test", ItemName = "Test Item" };
string json = definition.ToJson();
```

---

## Usage Example

### Loading Item Definitions

```csharp
// Server startup: Cache all item definitions
public class ItemDatabase : MonoBehaviour
{
    private Dictionary<string, ItemDefinition> itemDefinitions = new Dictionary<string, ItemDefinition>();

    void Start()
    {
        LoadItemDefinitionsFromBackend();
    }

    void LoadItemDefinitionsFromBackend()
    {
        // Fetch from backend API
        BackendAPI.GetItemDefinitions((jsonArray, success) =>
        {
            if (success)
            {
                var definitions = ItemDefinition.FromJsonArray(jsonArray);

                foreach (var def in definitions)
                {
                    itemDefinitions[def.ItemId] = def;
                }

                Debug.Log($"Loaded {definitions.Count} item definitions");
            }
        });
    }

    public ItemDefinition GetDefinition(string itemId)
    {
        return itemDefinitions.ContainsKey(itemId) ? itemDefinitions[itemId] : null;
    }
}
```

### Item Creation from Definition

```csharp
// Create item instance from definition
public ItemData CreateItem(string itemDefinitionId, int quantity)
{
    var definition = ItemDatabase.GetDefinition(itemDefinitionId);
    if (definition == null) return null;

    return new ItemData
    {
        ItemId = Guid.NewGuid().ToString(),
        ItemType = definition.ItemType,
        ItemDefinitionId = definition.ItemId,
        Quantity = Mathf.Min(quantity, definition.MaxStack),
        Size = definition.GridSize,
        Position = new Position(0, 0)
    };
}
```

---

## Design Notes

### Backend Integration

ItemDefinition is designed to match backend database schema:

**Backend Table** (conceptual):
```sql
CREATE TABLE ItemDefinitions (
    ItemId VARCHAR PRIMARY KEY,
    ItemName VARCHAR NOT NULL,
    ItemType VARCHAR NOT NULL,
    GridWidth INT DEFAULT 1,
    GridHeight INT DEFAULT 1,
    Properties JSON,
    MaxStack INT DEFAULT 1,
    IsTradeable BOOLEAN DEFAULT TRUE,
    IsConsumable BOOLEAN DEFAULT FALSE,
    BaseValue INT DEFAULT 0,
    Weight FLOAT DEFAULT 0
);
```

### Caching Strategy

**Server-Side**:
- Load all ItemDefinitions on server startup
- Cache in Dictionary<string, ItemDefinition> for O(1) lookup
- Refresh periodically or on admin command

**Client-Side**:
- Request only definitions for owned items
- Cache incrementally as items are acquired
- Reduces network traffic and memory usage

### Properties Dictionary

`Properties` field stores custom item-specific data:

**Consumable Example**:
```json
{
  "Properties": {
    "healAmount": 50,
    "duration": 10,
    "buffType": "health_regen"
  }
}
```

**Equipment Example**:
```json
{
  "Properties": {
    "damage": 100,
    "range": 500,
    "accuracy": 0.85,
    "fireRate": 2.5
  }
}
```

---

## Key Takeaways

1. **Backend Mirror**: Matches backend ItemDefinition model exactly
2. **Cached Definitions**: Loaded once on server startup, cached for fast lookups
3. **Tetris-Style Grid**: GridSize defines inventory space requirements
4. **Flexible Properties**: Dictionary allows custom item-specific data
5. **JSON Serialization**: Easy integration with backend REST API
