---
tags: [script, inventory, ship, cargo, performance, implemented]
script-type: Data Class
namespace: WOS.Inventory.Core
file-path: Assets/Scripts/Inventory/Core/ShipInventory.cs
status: IMPLEMENTED
size: ~8 KB (293 lines)
feature-group: inventory
---

# ShipInventory.cs

## Quick Reference
**Type**: Serializable Data Class
**Namespace**: WOS.Inventory.Core
**File**: `Assets/Scripts/Inventory/Core/ShipInventory.cs`
**Size**: ~8 KB (293 lines)
**Dependencies**: CargoGrid, ItemData

---

## Purpose
Ship cargo hold inventory wrapper. Extends CargoGrid with ship-specific behavior including weight-based performance penalties. Cargo weight directly affects ship speed, turning, and acceleration.

---

## Configuration

```csharp
[Header("Ship Configuration")]
public string PlayerId;
public string ShipClass;
public int ShipTier = 1;          // 1-10

[Header("Capacity")]
public float MaxWeightCapacity = 500f;
public int GridWidth = 10;
public int GridHeight = 10;

[Header("Cargo Grid")]
public CargoGrid CargoHold;
```

---

## Constructors

```csharp
// Full constructor
public ShipInventory(string playerId, string shipClass, int tier,
    float maxWeight, int width, int height)

// Default for serialization
public ShipInventory()
```

---

## Weight & Performance

### Weight Properties
```csharp
public float CurrentWeight => CargoHold.GetTotalWeight(GetItemWeightFunc);
public float RemainingCapacity => MaxWeightCapacity - CurrentWeight;
public float WeightFillPercentage => CurrentWeight / MaxWeightCapacity;
```

### Performance Multipliers

Based on GDD specifications:

| Property | Empty (0%) | Full (100%) | Formula |
|----------|-----------|-------------|---------|
| Speed | 1.0x | 0.7x | Lerp(1.0, 0.7, fill) |
| Turn Rate | 1.0x | 0.8x | Lerp(1.0, 0.8, fill) |
| Acceleration | 1.0x | 0.6x | Lerp(1.0, 0.6, fill) |

```csharp
public float GetSpeedMultiplier()
{
    return Mathf.Lerp(1.0f, 0.7f, WeightFillPercentage);
}

public float GetTurnRateMultiplier()
{
    return Mathf.Lerp(1.0f, 0.8f, WeightFillPercentage);
}

public float GetAccelerationMultiplier()
{
    return Mathf.Lerp(1.0f, 0.6f, WeightFillPercentage);
}
```

**GDD Reference**: Full cargo = 30% speed reduction, 20% turn reduction, 40% acceleration reduction

---

## Item Operations

### TryAddItem
Checks weight capacity before placement.
```csharp
public bool TryAddItem(ItemData item)
```

### TryAddItemAt
Checks weight and places at specific position.
```csharp
public bool TryAddItemAt(ItemData item, int x, int y)
```

### Other Operations
```csharp
public bool RemoveItem(string itemId)
public ItemData GetItemAt(int x, int y)
public bool MoveItem(string itemId, int newX, int newY)
public bool RotateItem(string itemId)
```

---

## Stacking & Merging

```csharp
public int MergeWithStacks(ItemData item, int maxStackSize)
public ItemData SplitStack(string itemId, int keepQuantity)
```

---

## Trading & Value

```csharp
public int GetTotalCargoValue(Func<string, int> getItemValue)
public List<ItemData> GetTradeableCargo()
```

---

## Container Access

Access nested container items (wallets, chests):

```csharp
public List<ItemData> GetContainers()
public CargoGrid OpenContainer(string containerId)
```

---

## Weight Lookup Function

```csharp
[NonSerialized]
public Func<string, float> GetItemWeightFunc;
```

Set from `ServerInventoryManager` or `ItemDatabase` for weight calculations.

---

## Integration Points

### Dependencies
- [[CargoGrid]] - Core inventory grid
- [[ItemData]] - Item data structure

### Used By
- [[PortInventory]] - Transfer operations
- [[ServerInventoryManager]] - Server-side caching
- [[NetworkedNavalController]] - Performance penalties

---

## Performance Impact on Ship

```
CurrentWeight → WeightFillPercentage → Multipliers
     ↓
NetworkedNavalController reads multipliers
     ↓
Applies to: maxSpeed, turnRate, acceleration
```

---

## Related Files
- [[CargoGrid]] - Core grid functionality
- [[PortInventory]] - Port warehouse (similar wrapper)
- [[HardCapWeightManager]] - Weight enforcement
- [[NetworkedNavalController]] - Uses performance multipliers

---

## Testing Notes
- CargoHold.Type = InventoryType.ShipCargo
- Weight affects physics, not just UI
- GetItemWeightFunc must be set for weight calculations
- Default grid: 10x10 with 500f max weight

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added performance multipliers
- **2025-01**: Added container access methods
- **2025-01**: Added trading value calculation

