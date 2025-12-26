---
tags: [script, inventory, database, singleton, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Inventory
file-path: Assets/Scripts/Inventory/ItemDatabase.cs
status: IMPLEMENTED
size: ~10 KB (378 lines)
feature-group: inventory
---

# ItemDatabase.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Inventory
**File**: `Assets/Scripts/Inventory/ItemDatabase.cs`
**Size**: ~10 KB (378 lines)
**Dependencies**: ItemDatabaseSO, ItemDefinitionSO, DebugManager

---

## Purpose
Runtime item definition manager providing global static access to item definitions. Wraps `ItemDatabaseSO` ScriptableObject with convenient lookup methods for weight, icons, prices, stacking, and item usage effects.

---

## Singleton Pattern

```csharp
public static ItemDatabase Instance { get; private set; }
```

Uses `DontDestroyOnLoad` for persistence across scenes.

---

## Configuration

```csharp
[Header("Configuration")]
[SerializeField] private ItemDatabaseSO itemDatabase;
[SerializeField] private bool initializeOnAwake = true;
```

**Fallback Loading**: If no database assigned, loads from `Resources/Items/ItemDatabase`.

---

## Initialization

```csharp
public void Initialize()
```

**Process**:
1. Load database from Resources if not assigned
2. Call `itemDatabase.Initialize()` to build lookup dictionary
3. Load default item icon from `Resources/Icons/Items/Default`
4. Load category icons from `Resources/Icons/Categories/{CategoryName}`

---

## Static Lookup API

### Core Lookups
```csharp
public static ItemDefinitionSO GetItem(string itemId)
public static string GetItemName(string itemId)
public static Sprite GetItemIcon(string itemId)
public static float GetItemWeight(string itemId)
public static Vector2Int GetItemGridSize(string itemId)
public static int GetItemBasePrice(string itemId)
```

### Stacking & Properties
```csharp
public static bool IsStackable(string itemId)
public static int GetMaxStackSize(string itemId)
public static bool IsContraband(string itemId)
public static bool IsUsable(string itemId)
public static bool ItemExists(string itemId)
```

### Collection Queries
```csharp
public static List<ItemDefinitionSO> GetItemsByCategory(ItemCategory category)
public static List<ItemDefinitionSO> GetTradeableItems(bool includeContraband = false)
public static List<ItemDefinitionSO> GetUsableItems()
public static List<ItemDefinitionSO> SearchItems(string query)
```

### UI Support
```csharp
public static Sprite GetCategoryIcon(ItemCategory category)
public static int TotalItemCount { get; }
```

---

## Item Usage System

### UseItem Method
```csharp
public static ItemUseResult UseItem(string itemId, GameObject target = null)
```

**Returns**: `ItemUseResult` with success flag, message, and effect details.

### Supported Item Effects
| Effect | Description | Status |
|--------|-------------|--------|
| None | No effect | Implemented |
| RestoreHealth | Heal ship damage | TODO |
| RestoreSailors | Add crew members | TODO |
| RepairHull | Repair hull integrity | TODO |
| BoostSpeed | Temporary speed buff | TODO |
| BoostFireRate | Temporary fire rate buff | TODO |
| ReduceDamage | Temporary damage reduction | TODO |
| RevealMap | Reveal map area | TODO |

---

## ItemUseResult Class

```csharp
public class ItemUseResult
{
    public bool Success;
    public string Message;
    public ItemEffect EffectApplied;
    public float EffectValue;
}
```

---

## Default Values

When item not found, methods return sensible defaults:
- **Name**: Returns itemId as fallback
- **Weight**: 1f
- **Grid Size**: (1, 1)
- **Base Price**: 100
- **Stackable**: false
- **Max Stack**: 1
- **Contraband**: false
- **Usable**: false

---

## Resource Paths

| Resource | Path |
|----------|------|
| Item Database | `Resources/Items/ItemDatabase` |
| Default Icon | `Resources/Icons/Items/Default` |
| Category Icons | `Resources/Icons/Categories/{CategoryName}` |

---

## Integration Points

### Dependencies
- [[ItemDatabaseSO]] - ScriptableObject data source
- [[ItemDefinitionSO]] - Individual item definitions
- [[DebugManager]] - Logging

### Used By
- [[InventoryManager]] - Item display and operations
- [[ShipInventory]] - Weight calculations via `GetItemWeight()`
- [[TradingPanel]] - Prices and tradeable items
- [[InventoryPanel]] - Icons and item info display

---

## Related Files
- [[ItemDatabaseSO]] - ScriptableObject data container
- [[ItemDefinitionSO]] - Item definition structure
- [[InventoryManager]] - Main inventory orchestrator
- [[ShipInventory]] - Uses weight lookup

---

## Testing Notes
- Singleton with DontDestroyOnLoad
- Auto-initializes on Awake if `initializeOnAwake = true`
- Falls back to Resources loading if no database assigned
- All static methods null-safe (return defaults if not initialized)
- Item effects are placeholder TODOs

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added item usage system
- **2025-01**: Added category icon support
- **2025-01**: Added search functionality

