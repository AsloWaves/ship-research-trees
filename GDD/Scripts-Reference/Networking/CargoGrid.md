---
tags: [script, networking, inventory, data, tetris, implemented]
script-type: Data Class
namespace: WOS.Networking.Data
file-path: Assets/Scripts/Networking/Data/CargoGrid.cs
status: IMPLEMENTED
size: ~22 KB (795 lines)
feature-group: inventory
---

# CargoGrid.cs

## Quick Reference
**Type**: Serializable Data Class
**Namespace**: WOS.Networking.Data
**File**: `Assets/Scripts/Networking/Data/CargoGrid.cs`
**Size**: ~22 KB (795 lines)
**Dependencies**: ItemData, DebugManager

---

## Purpose
Tetris-style cargo grid for inventory management. Provides O(1) collision detection for item placement using a 2D cell array. Supports item rotation, auto-placement, weight management, stacking, and grid organization.

This is the **core inventory data structure** used for:
- Ship cargo holds
- Port warehouse storage
- Container item internal storage
- Crew quarters

---

## Inventory Type Enum

```csharp
public enum InventoryType
{
    Generic,        // Default/unspecified
    ShipCargo,      // Ship cargo hold - weight affects performance
    PortWarehouse,  // Port storage - tier-based capacity
    Wallet,         // Container item internal storage
    CrewQuarters    // Crew card storage
}
```

---

## Core Properties

```csharp
public int Width = 10;                  // Grid width in cells
public int Height = 10;                 // Grid height in cells
public InventoryType Type;              // Type of inventory
public float MaxWeight = 0f;            // 0 = unlimited capacity
public string OwnerId;                  // PlayerId or PortId
public List<List<string>> Cells;        // 2D cell occupancy array
public List<ItemData> Items;            // All items in grid
```

---

## Data Structure

### Cell Occupancy Array
```
Cells[y][x] = itemId (or null if empty)
```

Enables O(1) collision detection:
- Each cell stores the ItemId occupying it
- Null means cell is empty
- Multi-cell items occupy all cells with same ItemId

### Items List
```
List<ItemData> - Stores actual item data
```

Uses List instead of Dictionary for Mirror network serialization support.

---

## Core Methods

### CanPlaceItem
Checks if item fits at position without collision.
```csharp
public bool CanPlaceItem(ItemData item, int x, int y)
```
- O(width × height) for item size
- Checks bounds and cell occupancy

### PlaceItem
Places item in grid at specified position.
```csharp
public bool PlaceItem(ItemData item, int x, int y)
```
- Updates item.Position
- Marks cells as occupied
- Adds to Items list

### RemoveItem
Removes item from grid by ItemId.
```csharp
public bool RemoveItem(string itemId)
```
- Clears cell occupancy
- Removes from Items list

### GetItemAt
Gets item at specific grid cell.
```csharp
public ItemData GetItemAt(int x, int y)
```

### MoveItem
Moves item to new position.
```csharp
public bool MoveItem(string itemId, int newX, int newY)
```
- Removes from current position
- Attempts placement at new position
- Restores original on failure

---

## Item Rotation

### RotateItem
Rotates item 90 degrees clockwise.
```csharp
public bool RotateItem(string itemId)
```

### RotateItemTo
Rotates item to specific angle.
```csharp
public bool RotateItemTo(string itemId, int targetRotation)
```
- Valid angles: 0, 90, 180, 270
- Swaps width/height for 90/270
- Restores original on failure

### CanRotateItem
Checks if rotation would succeed.
```csharp
public bool CanRotateItem(string itemId)
```

**Rotation Logic**:
```
90°/270°: Width ↔ Height swap
0°/180°: Original dimensions
```

---

## Auto-Placement

### FindFirstAvailablePosition
Finds first empty position for item.
```csharp
public Position FindFirstAvailablePosition(ItemData item)
```
- Scans left-to-right, top-to-bottom
- Returns null if no space

### AutoPlaceItem
Places item in first available position.
```csharp
public bool AutoPlaceItem(ItemData item)
```

### AutoPlaceItemWithRotation
Tries all rotations to find placement.
```csharp
public bool AutoPlaceItemWithRotation(ItemData item, int x, int y)
```
- Tries 0°, 90°, 180°, 270° rotations
- Returns true if any rotation fits

---

## Weight & Capacity Management

### GetTotalWeight
Gets total weight of all items.
```csharp
public float GetTotalWeight(Func<string, float> getItemWeight = null)
```
- Equipment uses EquipmentWeight field
- Cargo uses lookup function

### Weight Properties
```csharp
public bool HasWeightLimit => MaxWeight > 0f;

public float GetRemainingWeightCapacity(...)
public bool CanAcceptWeight(float additionalWeight, ...)
public bool WouldExceedCapacity(ItemData item, ...)
```

### Grid Occupancy
```csharp
public int GetOccupiedCellCount()
public float GetOccupiedPercentage()
```

---

## Item Stacking

### MergeWithExistingStacks
Merges new item with compatible stacks.
```csharp
public int MergeWithExistingStacks(ItemData newItem, int maxStackSize)
```
- Returns remaining quantity that couldn't stack
- Equipment items don't stack

### SplitStack
Splits a stack into two.
```csharp
public ItemData SplitStack(string itemId, int splitQuantity)
```
- Returns new ItemData with split quantity
- Original keeps specified quantity

---

## Item Filtering & Search

```csharp
public List<ItemData> GetItemsByType(string itemType)
public List<ItemData> GetEquipmentItems()
public List<ItemData> GetCargoItems()
public List<ItemData> GetContainerItems()
public List<ItemData> GetCrewCards()
public List<ItemData> GetEquipmentByTier(int tier)
public List<ItemData> GetEquipmentBySubType(string subType)
public int GetTotalQuantityOfItem(string itemId)
```

---

## Grid Organization

### CompactGrid
Repacks grid for minimal wasted space.
```csharp
public void CompactGrid()
```
- Extracts all items
- Sorts by size (largest first)
- Re-places using auto-placement

### SortByType
Sorts items by category.
```csharp
public void SortByType()
```
- Equipment first (by tier descending)
- Then cargo (alphabetical)

---

## Serialization

```csharp
public string ToJson()
public static CargoGrid FromJson(string json)
public CargoGrid Clone()  // Deep copy including nested containers
```

---

## Integration Points

### Used By
- [[PlayFabInventoryService]] - Persistence layer
- [[ServerInventoryManager]] - Server-side caching
- [[InventoryPanel]] - UI display
- [[ItemData]] - Items reference container grid

### Data Flow
```
PlayFab → CargoGrid.FromJson() → Items list
Grid operations → ToJson() → PlayFab
```

---

## Performance Characteristics

| Operation | Complexity |
|-----------|------------|
| CanPlaceItem | O(item_area) |
| PlaceItem | O(item_area) |
| RemoveItem | O(item_area + n) |
| GetItemAt | O(1) lookup + O(n) find |
| AutoPlaceItem | O(grid_area × item_area) worst case |
| CompactGrid | O(n log n + n × grid_area) |

---

## Related Files
- [[ItemData]] - Item data structure
- [[PlayFabInventoryService]] - Persistence
- [[ServerInventoryManager]] - Server caching
- [[InventoryPanel]] - UI rendering

---

## Testing Notes
- Default grid: 10x10 (100 cells)
- MaxWeight 0 = unlimited
- Cells array uses List<List<>> for serialization
- Equipment items never stack
- Rotation swaps Width/Height for 90°/270°

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added rotation support
- **2025-01**: Added weight management
- **2025-01**: Added stacking and splitting
- **2025-01**: Added grid organization methods
- **2025-01**: Added InventoryType enum

