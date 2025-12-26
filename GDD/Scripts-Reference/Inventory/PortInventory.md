---
tags: [script, inventory, port, warehouse, tier-based, implemented]
script-type: Data Class
namespace: WOS.Inventory.Core
file-path: Assets/Scripts/Inventory/Core/PortInventory.cs
status: IMPLEMENTED
size: ~10 KB (375 lines)
feature-group: inventory
---

# PortInventory.cs

## Quick Reference
**Type**: Serializable Data Class
**Namespace**: WOS.Inventory.Core
**File**: `Assets/Scripts/Inventory/Core/PortInventory.cs`
**Size**: ~10 KB (375 lines)
**Dependencies**: CargoGrid, ItemData, ShipInventory

---

## Purpose
Port warehouse inventory wrapper. Per-port persistent storage with tier-based capacity. No weight limit - only space constraint. Supports transfer operations between ship cargo and warehouse.

---

## GDD Tier-Based Capacity

| Port Tier | Grid Height | Total Cells |
|-----------|-------------|-------------|
| T1-T3 | 50 rows | 500 cells |
| T4-T7 | 75 rows | 750 cells |
| T8-T10 | 100 rows | 1000 cells |

Grid width is always 10 cells.

---

## Configuration

```csharp
[Header("Port Configuration")]
public string PortId;
public string PortName;
public int PortTier = 1;     // 1-10
public string PlayerId;

[Header("Capacity")]
public int GridWidth = 10;
public int GridHeight = 50;  // Tier-based
public int TotalCapacity => GridWidth * GridHeight;

[Header("Storage Grid")]
public CargoGrid Warehouse;
```

---

## Constructors

```csharp
// Full constructor
public PortInventory(string portId, string portName, int tier, string playerId)

// Default for serialization
public PortInventory()
```

**Note**: `Warehouse.MaxWeight = 0f` (no weight limit for port storage)

---

## Tier Configuration

```csharp
public static int GetHeightForTier(int tier)
{
    if (tier <= 3) return 50;
    if (tier <= 7) return 75;
    return 100;
}

public static int GetCapacityForTier(int tier)
{
    return 10 * GetHeightForTier(tier);
}
```

---

## Upgrade System

```csharp
public bool UpgradeToTier(int newTier)
```

**Process**:
1. Validate new tier > current tier
2. Create new larger warehouse grid
3. Transfer all existing items (preserve positions)
4. Replace warehouse reference

---

## Capacity Management

```csharp
public int UsedCells => Warehouse.GetOccupiedCellCount();
public int FreeCells => TotalCapacity - UsedCells;
public float FillPercentage => Warehouse.GetOccupiedPercentage();

public bool HasSpaceFor(int width, int height)
```

`HasSpaceFor()` performs actual placement check, not just cell count.

---

## Item Operations

```csharp
public bool TryAddItem(ItemData item)
public bool TryAddItemAt(ItemData item, int x, int y)
public bool RemoveItem(string itemId)
public ItemData GetItemAt(int x, int y)
public bool MoveItem(string itemId, int newX, int newY)
public bool RotateItem(string itemId)
```

---

## Transfer Operations

### Ship → Port
```csharp
public bool TransferFromShip(ShipInventory ship, string itemId)
```
- Clones item with new ID
- Checks port has space
- Removes from ship on success

### Port → Ship
```csharp
public bool TransferToShip(ShipInventory ship, string itemId)
```
- Clones item with new ID
- Checks ship weight capacity
- Removes from port on success

### Partial Quantity Transfer
```csharp
public bool TransferQuantityToShip(ShipInventory ship, string itemId, int quantity)
```
- Creates new item with requested quantity
- Reduces original stack or removes if empty

---

## Filtering Methods

```csharp
public List<ItemData> GetItemsByType(string itemType)
public List<ItemData> GetCargoItems()
public List<ItemData> GetEquipmentItems()
public int GetTotalQuantity(string itemTypeOrId)
```

---

## OwnerId Format

```csharp
Warehouse.OwnerId = $"{playerId}_{portId}";
```

Combines player and port IDs for unique identification.

---

## Integration Points

### Dependencies
- [[CargoGrid]] - Core inventory grid
- [[ItemData]] - Item data structure
- [[ShipInventory]] - Transfer operations

### Used By
- [[PlayFabInventoryService]] - Persistence
- [[TradingPanel]] - Port UI

---

## Key Differences from ShipInventory

| Feature | ShipInventory | PortInventory |
|---------|--------------|---------------|
| Weight Limit | Yes (hard cap) | No |
| Performance Impact | Yes (speed/turn) | No |
| Tier System | Ship tier | Port tier |
| Upgradeable | No | Yes |
| Transfer | Source/Target | Source/Target |

---

## Related Files
- [[CargoGrid]] - Core grid functionality
- [[ShipInventory]] - Ship cargo wrapper
- [[PlayFabInventoryService]] - Port storage persistence
- [[TradingPanel]] - Port trading UI

---

## Testing Notes
- Warehouse.Type = InventoryType.PortWarehouse
- No weight validation (space only)
- Transfer creates new item IDs
- Upgrade preserves item positions

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added tier upgrade system
- **2025-01**: Added transfer operations
- **2025-01**: Added quantity-based transfers

