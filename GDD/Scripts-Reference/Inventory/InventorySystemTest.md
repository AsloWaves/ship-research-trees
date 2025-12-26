---
tags: [script, inventory, testing, implemented]
script-type: MonoBehaviour
namespace: WOS.Inventory.Testing
file-path: Assets/Scripts/Inventory/Testing/InventorySystemTest.cs
status: IMPLEMENTED
size: ~18 KB (707 lines)
feature-group: inventory
---

# InventorySystemTest.cs

## Quick Reference
**Type**: MonoBehaviour (Test Suite)
**Namespace**: WOS.Inventory.Testing
**File**: `Assets/Scripts/Inventory/Testing/InventorySystemTest.cs`
**Size**: ~18 KB (707 lines)
**Dependencies**: DebugManager, ItemData, CargoGrid, ShipInventory, PortInventory, WalletInventory

---

## Purpose
Comprehensive test suite for the inventory system. Attach to any GameObject and press Play to run tests. Results logged via DebugManager. Tests all inventory components including network messages.

---

## Configuration

```csharp
[Header("Test Configuration")]
public bool RunOnStart = true;
public bool StopOnFailure = false;

[Header("Test Item Definitions (Optional)")]
public ItemDefinitionSO TestCargoItem;
public ItemDefinitionSO TestEquipmentItem;
public ItemDefinitionSO TestWalletItem;
public ItemDefinitionSO TestCurrencyItem;

[Header("Test Results")]
[SerializeField] private int testsRun = 0;
[SerializeField] private int testsPassed = 0;
[SerializeField] private int testsFailed = 0;
```

---

## Test Categories

| Category | Tests | Purpose |
|----------|-------|---------|
| ItemData Extensions | 8 | Container detection, weight, clone |
| CargoGrid Extensions | 7 | Grid type, weight, containers |
| ShipInventory | 10 | Weight limits, performance multipliers |
| PortInventory | 8 | Tier capacity, upgrades |
| WalletInventory | 12 | Currency, nesting prevention |
| Inventory Transfers | 6 | Ship-Port transfers, partial |
| Container Nesting | 6 | Wallet in ship, weight, clone |
| Network Messages | 15 | Phase 2 message structs |

---

## Running Tests

### Automatic
Set `RunOnStart = true` in Inspector.

### Manual
Right-click component → "Run All Tests"

### Via Code
```csharp
GetComponent<InventorySystemTest>().RunAllTests();
```

---

## Mock Data

### Item Weights
```csharp
mockItemWeights["cargo_iron"] = 1.0f;
mockItemWeights["cargo_gold"] = 2.5f;
mockItemWeights["cargo_food"] = 0.5f;
mockItemWeights["wallet_basic"] = 0.1f;
mockItemWeights["currency_gold"] = 0.01f;
mockItemWeights["equipment_cannon"] = 5.0f;
```

---

## Test Coverage

### ItemData Tests
- Container detection (IsContainer)
- Cargo detection (IsCargo)
- Container initialization
- ContainerGrid dimensions
- CrewCard detection
- Equipment weight
- Stack weight calculation
- Clone with container

### CargoGrid Tests
- Inventory type assignment
- Weight limit property
- Weight calculation
- Remaining capacity
- Weight acceptance
- Container item filter
- Clone preserves fields

### ShipInventory Tests
- Player ID assignment
- Cargo type
- Max weight
- Add item success
- Weight tracking
- Speed multiplier at 20%
- Speed multiplier at 80%
- Weight limit rejection
- Container access
- Container opening

### PortInventory Tests
- Tier-based heights (T1-T10)
- Port tier assignment
- Grid height calculation
- Total capacity
- Warehouse type
- Add item (no weight limit)
- Upgrade functionality
- Downgrade prevention

### WalletInventory Tests
- External dimensions
- Internal dimensions
- Total capacity
- Empty state
- Add item
- Nested container rejection
- Currency add
- Currency total
- Currency has check
- Currency remove
- Open/close state

### Transfer Tests
- Ship to port transfer
- Port to ship transfer
- Item count after transfer
- New item ID generation
- Partial quantity transfer
- Remaining stack quantity

### Container Nesting Tests
- Add wallet to ship
- Open wallet grid
- Add item to wallet
- Wallet weight with contents
- Clone ship with wallet
- Deep copy verification

### Network Message Tests
- TransferItemMessage
- TransferResultMessage
- OpenContainerMessage
- ContainerOpenedMessage
- SplitStackMessage
- StackSplitResultMessage
- MergeStacksMessage
- StackMergeResultMessage
- RequestPortStorageMessage
- PortStorageLoadedMessage
- RotateItemMessage
- ItemRotatedMessage
- MultiInventorySyncMessage
- InventoryChangeNotification

---

## Test Output

```
========================================
INVENTORY SYSTEM TEST SUITE
========================================

--- Testing ItemData Extensions ---
[PASS] Cargo item is not container
[PASS] Cargo item is cargo
...

========================================
TEST SUMMARY: 72/72 passed, 0 failed
========================================
ALL TESTS PASSED!
```

---

## Assert Method

```csharp
private void Assert(string testName, bool condition)
{
    testsRun++;
    if (condition)
    {
        testsPassed++;
        LogSuccess($"[PASS] {testName}");
    }
    else
    {
        testsFailed++;
        LogError($"[FAIL] {testName}");
        if (StopOnFailure) throw new Exception($"Test failed: {testName}");
    }
}
```

---

## Integration Points

### Dependencies
- [[DebugManager]] - Logging
- [[ItemData]] - Test subject
- [[CargoGrid]] - Test subject
- [[ShipInventory]] - Test subject
- [[PortInventory]] - Test subject
- [[WalletInventory]] - Test subject
- Network Messages - Test subject

---

## Related Files
- [[ShipInventory]] - Primary test subject
- [[PortInventory]] - Primary test subject
- [[WalletInventory]] - Primary test subject
- [[CargoGrid]] - Primary test subject

---

## Testing Notes
- Uses mock weight lookup (not ItemDatabase)
- Tests run in Play Mode only
- Results visible in Inspector
- StopOnFailure throws exception
- ContextMenu for manual execution

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added Phase 2 network message tests
- **2025-01**: Added transfer tests
- **2025-01**: Added container nesting tests

