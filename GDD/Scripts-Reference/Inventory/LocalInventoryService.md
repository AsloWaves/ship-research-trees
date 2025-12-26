---
tags: [script, inventory, testing, mock, implemented]
script-type: MonoBehaviour
namespace: WOS.Inventory
file-path: Assets/Scripts/Inventory/LocalInventoryService.cs
status: IMPLEMENTED
size: ~17 KB (656 lines)
feature-group: inventory
---

# LocalInventoryService.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Inventory
**File**: `Assets/Scripts/Inventory/LocalInventoryService.cs`
**Size**: ~17 KB (656 lines)
**Dependencies**: DebugManager, UI.Inventory types

---

## Purpose
Local mock implementation of inventory service for testing. Mirrors InventoryAPIService interface but uses in-memory data. Allows testing UI without backend connection. Supports configurable latency and failure simulation.

---

## Configuration

```csharp
[Header("Test Configuration")]
[SerializeField] private bool simulateLatency = true;
[SerializeField] private float minLatencyMs = 50f;
[SerializeField] private float maxLatencyMs = 200f;
[SerializeField] private float failureRate = 0f;  // 0 to 1

[Header("Initial State")]
[SerializeField] private int startingBalance = 50000;
```

---

## In-Memory Storage

```csharp
private List<PlayerShipData> playerShips;
private List<CrewData> playerCrew;
private List<EquipmentItemData> playerEquipment;
private string activeShipId;
private int playerBalance;
```

---

## Initialization

```csharp
public void Initialize()
```

Called in `Awake()`. Generates:
- 3 mock ships (Destroyer, Cruiser, Battleship)
- 10 mock crew members
- 12 mock equipment items

---

## Mock Ships Data

| Ship | Class | Hull | Speed | Weight | Cargo |
|------|-------|------|-------|--------|-------|
| USS Fletcher | Fletcher-class | 2100 | 36.5 | 2500 | 50 |
| USS Cleveland | Cleveland-class | 5500 | 32.5 | 14000 | 100 |
| USS Iowa | Iowa-class | 12000 | 33 | 58000 | 200 |

---

## Mock Crew Data

10 crew members with:
- Classifications: Gunner, Engineer, Navigator, Repairman, Medic
- Random levels 1-20
- Random XP 0-10000
- First 2 assigned to active ship

---

## Mock Equipment Data

| Type | Count | Examples |
|------|-------|----------|
| Turrets | 5 | Main Battery Mk7, Secondary Mk12, AA Bofors |
| Engines | 3 | Westinghouse Turbine, Diesel Mk3 |
| Modules | 4 | Fire Control Mk37, Radar SK-2 |

---

## API Methods (Mirrors InventoryAPIService)

### Ships
```csharp
public async Task<GetShipsResult> GetPlayerShipsAsync()
public async Task<SetActiveShipResult> SetActiveShipAsync(string shipId)
public async Task<SaveLoadoutResult> SaveShipLoadoutAsync(string shipId, ShipLoadout loadout)
public async Task<SaveCargoResult> SaveShipCargoAsync(string shipId, CargoGrid cargo)
```

### Crew
```csharp
public async Task<GetCrewResult> GetPlayerCrewAsync()
public async Task<CreateCrewResult> CreateCrewAsync(string name, string classification)
public async Task<SaveCrewBatchResult> SaveCrewBatchAsync(List<CrewData> crewUpdates)
public async Task<SaveCrewAssignmentResult> SaveCrewAssignmentAsync(string crewId, string shipId, string position)
public async Task<RestoreCrewResult> RestoreCrewSailorsAsync(string crewId)
```

### Equipment (Extended)
```csharp
public async Task<GetEquipmentResult> GetPlayerEquipmentAsync()
```

### Trading
```csharp
public async Task<GetBalanceResult> GetBalanceAsync()
public async Task<GetMarketResult> GetPortMarketAsync(string portId)
public async Task<TransactionResult> ProcessBatchTransactionAsync(...)
```

---

## Latency Simulation

```csharp
private async Task SimulateLatency()
{
    if (simulateLatency)
    {
        float delay = Random.Range(minLatencyMs, maxLatencyMs) / 1000f;
        await Task.Delay(TimeSpan.FromSeconds(delay));
    }
}
```

---

## Failure Simulation

```csharp
private bool ShouldFail()
{
    return Random.value < failureRate;
}
```

All methods check `ShouldFail()` and return error result if true.

---

## Mock Market Data

Generated for each port:
- 5 buyable goods (Iron Ore, Coal, Oil, Steel, Ammo)
- 4 sellable goods (same minus Ammo)
- Buy prices ~10% above base
- Sell prices ~20% below base

---

## Port Names

```csharp
"port_nyc" → "New York Harbor"
"port_norfolk" → "Norfolk Naval Base"
"port_pearl" → "Pearl Harbor"
"port_san_diego" → "San Diego Naval Base"
```

---

## Testing Utilities

```csharp
public void ResetToInitialState()     // Reset all data
public void AddBalance(int amount)     // Add currency
public int GetCurrentBalance()         // Direct access
public List<PlayerShipData> GetShipsDirect()
public List<CrewData> GetCrewDirect()
public List<EquipmentItemData> GetEquipmentDirect()
```

---

## Extended Data Classes

### EquipmentItemData
```csharp
public class EquipmentItemData
{
    public string EquipmentId;
    public string EquipmentName;
    public EquipmentSlotType SlotType;
    public int Tier;
    public float WeightTons;
    public string Description;
    public bool IsInstalled;
    public string InstalledOnShipId;
}
```

### GetEquipmentResult
```csharp
public class GetEquipmentResult
{
    public bool Success;
    public string Error;
    public List<EquipmentItemData> Equipment;
}
```

---

## Transaction Logic

```csharp
// Mock prices
int purchaseCost = quantity * 100;  // 100 per item
int saleRevenue = quantity * 80;    // 80 per item

// Validate funds
if (playerBalance + netChange < 0)
    return Error("Insufficient funds");
```

---

## Integration Points

### Dependencies
- [[DebugManager]] - Logging

### Used By
- [[InventoryManager]] - As alternative to InventoryAPIService
- UI Testing scenarios

---

## Related Files
- [[InventoryAPIService]] - Production API implementation
- [[InventoryManager]] - Client orchestrator

---

## Testing Notes
- Set failureRate to test error handling
- Adjust latency to test loading states
- Use ResetToInitialState() between tests
- Direct access methods bypass async for debugging
- startingBalance configurable in Inspector

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added equipment API
- **2025-01**: Added port market generation
- **2025-01**: Added testing utilities

