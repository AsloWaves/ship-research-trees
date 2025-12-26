---
tags: [script, inventory, container, wallet, implemented]
script-type: Serializable Class
namespace: WOS.Inventory.Core
file-path: Assets/Scripts/Inventory/Core/WalletInventory.cs
status: IMPLEMENTED
size: ~11 KB (426 lines)
feature-group: inventory
---

# WalletInventory.cs

## Quick Reference
**Type**: Serializable Class
**Namespace**: WOS.Inventory.Core
**File**: `Assets/Scripts/Inventory/Core/WalletInventory.cs`
**Size**: ~11 KB (426 lines)
**Dependencies**: CargoGrid, ItemData, ShipInventory

---

## Purpose
Portable container inventory wrapper for wallets and similar nested containers. Containers are 2x2 items in parent inventory that open to reveal a 10x25 internal grid. Supports currency operations and item transfers.

---

## GDD Specifications

| Property | Value | Notes |
|----------|-------|-------|
| External Size | 2x2 | Size in parent grid |
| Internal Grid | 10x25 | 250 cells |
| Weight Limit | None | No weight limit for containers |
| Nesting | 1 level | Containers cannot hold containers |

---

## Configuration

```csharp
[Header("Container Configuration")]
public string ContainerItemId;
public string PlayerId;
public string ContainerType;  // "basic_wallet", "large_chest"

[Header("Dimensions")]
public int ExternalWidth = 2;
public int ExternalHeight = 2;
public int InternalWidth = 10;
public int InternalHeight = 25;

[Header("Contents")]
public CargoGrid Contents;

[Header("State")]
public bool IsOpen = false;
```

---

## Constructors

```csharp
// Standard wallet (2x2 external, 10x25 internal)
public WalletInventory(string playerId, string containerItemId, string containerType = "basic_wallet")

// Custom-sized container
public WalletInventory(string playerId, string containerItemId, string containerType,
    int extWidth, int extHeight, int intWidth, int intHeight)

// Default for serialization
public WalletInventory()
```

---

## Container State

```csharp
public void Open()
public void Close()

public int TotalCapacity => InternalWidth * InternalHeight;  // 250
public int UsedCells => Contents.GetOccupiedCellCount();
public int FreeCells => TotalCapacity - UsedCells;
public float FillPercentage => Contents.GetOccupiedPercentage();
public bool IsEmpty => Contents.Items.Count == 0;
public float TotalWeight => Contents.GetTotalWeight(GetItemWeightFunc);
```

---

## Item Operations

```csharp
public bool TryAddItem(ItemData item)
public bool TryAddItemAt(ItemData item, int x, int y)
public bool RemoveItem(string itemId)
public ItemData GetItemAt(int x, int y)
public bool MoveItem(string itemId, int newX, int newY)
public bool RotateItem(string itemId)
public bool HasSpaceFor(ItemData item)
```

**Important**: `TryAddItem()` rejects containers (no nested containers).

---

## Currency Operations

### Get Total Currency
```csharp
public int GetTotalCurrency()
```
Sums all items with `ItemType == "Currency"`.

### Add Currency
```csharp
public bool AddCurrency(int amount, string currencyItemId, int maxStack = 999)
```
Stacks with existing currency or creates new item.

### Remove Currency
```csharp
public int RemoveCurrency(int amount, string currencyItemId)
```
Returns actual amount removed (may be less if insufficient).

### Has Currency
```csharp
public bool HasCurrency(int amount, string currencyItemId)
```
Checks if container has at least specified amount.

---

## Transfer Operations

### To Ship
```csharp
public bool TransferToShip(ShipInventory ship, string itemId)
```
Clones item with new ID, places in ship cargo, removes from container.

### From Ship
```csharp
public bool TransferFromShip(ShipInventory ship, string itemId)
```
Clones item with new ID, places in container, removes from ship.

**Note**: Containers cannot be transferred into containers (nesting blocked).

---

## Serialization

### Clone
```csharp
public WalletInventory Clone()
```
Creates deep copy including all contents.

### Sync With ItemData
```csharp
public void SyncWithItemData(ItemData containerItem)
```
Updates wallet from ItemData's ContainerGrid (after loading from backend).

### Update ItemData
```csharp
public void UpdateItemData(ItemData containerItem)
```
Copies wallet contents back to ItemData (before saving to backend).

---

## OwnerId Format

```csharp
Contents.OwnerId = $"{playerId}_{containerItemId}";
Contents.Type = InventoryType.Wallet;
Contents.MaxWeight = 0f;  // No weight limit
```

---

## Container Types

| Type | External | Internal | Purpose |
|------|----------|----------|---------|
| basic_wallet | 2x2 | 10x25 | Currency and small items |
| large_chest | 3x3 | 15x30 | General storage |
| lockbox | 2x2 | 5x10 | Secure valuables |

---

## Integration Points

### Dependencies
- [[CargoGrid]] - Internal storage grid
- [[ItemData]] - Item storage and container data
- [[ShipInventory]] - Transfer operations

### Used By
- [[InventoryPanel]] - Container UI
- [[ShipInventory]] - Container access via `OpenContainer()`
- [[InventoryNetworkBehaviour]] - Network sync

---

## Related Files
- [[ShipInventory]] - Parent inventory access
- [[CargoGrid]] - Internal grid implementation
- [[ItemData]] - Container item wrapper

---

## Testing Notes
- Containers cannot hold other containers
- MaxWeight = 0f (no weight limit)
- InventoryType.Wallet for type identification
- Currency stacking up to 999 per stack
- Transfer creates new item IDs

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added currency operations
- **2025-01**: Added transfer methods
- **2025-01**: Added serialization sync methods

