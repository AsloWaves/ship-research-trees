---
tags: [script, inventory, api, networking, implemented]
script-type: MonoBehaviour
namespace: WOS.Inventory
file-path: Assets/Scripts/Inventory/InventoryAPIService.cs
status: IMPLEMENTED
size: ~18 KB (699 lines)
feature-group: inventory
---

# InventoryAPIService.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.Inventory
**File**: `Assets/Scripts/Inventory/InventoryAPIService.cs`
**Size**: ~18 KB (699 lines)
**Dependencies**: UnityWebRequest, DebugManager

---

## Purpose
Client-side API service for inventory backend communication. Handles authentication, HTTP request formatting, and JSON response parsing. Provides async methods for ships, crew, and trading operations.

---

## Configuration

```csharp
[Header("API Configuration")]
[SerializeField] private string baseUrl = "https://api.example.com";
[SerializeField] private float requestTimeout = 30f;
```

---

## Authentication

```csharp
public void SetAuthToken(string token)
public bool IsAuthenticated => !string.IsNullOrEmpty(authToken);
```

Token set from external login flow, added to all requests as Bearer token.

---

## Ships API

| Method | HTTP | Endpoint | Returns |
|--------|------|----------|---------|
| GetPlayerShipsAsync() | GET | /api/ships/list | GetShipsResult |
| SetActiveShipAsync(shipId) | POST | /api/ships/set-active | SetActiveShipResult |
| SaveShipLoadoutAsync(shipId, loadout) | POST | /api/ships/save-loadout | SaveLoadoutResult |
| SaveShipCargoAsync(shipId, cargo) | POST | /api/ships/save-cargo | SaveCargoResult |

### GetShipsResult
```csharp
public class GetShipsResult
{
    public bool Success;
    public string Error;
    public List<PlayerShipData> Ships;
    public string ActiveShipId;
}
```

---

## Crew API

| Method | HTTP | Endpoint | Returns |
|--------|------|----------|---------|
| GetPlayerCrewAsync() | GET | /api/crew/list | GetCrewResult |
| CreateCrewAsync(name, classification) | POST | /api/crew/create | CreateCrewResult |
| SaveCrewBatchAsync(crewUpdates) | POST | /api/crew/save-batch | SaveCrewBatchResult |
| SaveCrewAssignmentAsync(crewId, shipId, position) | POST | /api/crew/save-assignment | SaveCrewAssignmentResult |
| RestoreCrewSailorsAsync(crewId) | POST | /api/crew/restore | RestoreCrewResult |

---

## Trading API

| Method | HTTP | Endpoint | Returns |
|--------|------|----------|---------|
| GetBalanceAsync() | GET | /api/trading/balance | GetBalanceResult |
| GetPortMarketAsync(portId) | GET | /api/trading/market/{portId} | GetMarketResult |
| ProcessBatchTransactionAsync(portId, purchases, sales) | POST | /api/trading/batch | TransactionResult |

### TransactionResult
```csharp
public class TransactionResult
{
    public bool Success;
    public string Error;
    public int NewBalance;
    public int NetChange;
}
```

---

## HTTP Implementation

```csharp
private async Task<T> SendRequestAsync<T>(string method, string endpoint, object body = null)
```

**Features**:
- Bearer token authentication
- JSON content type
- Configurable timeout
- UploadHandlerRaw for POST body
- DownloadHandlerBuffer for response
- JsonUtility parsing

---

## Data Conversion

```csharp
private List<PlayerShipData> ConvertShips(List<ShipData> ships)
private List<CrewData> ConvertCrew(List<CrewDataResponse> crew)
```

Converts API response models to game data models.

---

## API Response Classes

### Ship Responses
- ListShipsResponse
- ShipData
- SetActiveShipResponse
- SaveLoadoutResponse
- SaveCargoResponse

### Crew Responses
- ListCrewResponse
- CrewDataResponse
- CreateCrewResponse
- SaveCrewBatchResponse
- SaveCrewAssignmentResponse
- RestoreSailorsResponse

### Trading Responses
- BalanceResponse
- GetPortMarketResponse
- PortMarketData
- TransactionItem
- BatchTransactionResponse

---

## Result Classes

All result classes follow pattern:
```csharp
public class [Operation]Result
{
    public bool Success;
    public string Error;
    // Operation-specific data
}
```

---

## Port Market Data

```csharp
public class PortMarketData
{
    public string PortId;
    public string PortName;
    public List<MarketItem> BuyableGoods;
    public List<MarketItem> SellableGoods;
}
```

---

## Error Handling

All methods:
1. Wrap in try-catch
2. Log errors via DebugManager
3. Return Result with Success = false and Error message
4. Never throw to caller

---

## Integration Points

### Dependencies
- [[DebugManager]] - Error logging
- UnityWebRequest - HTTP communication

### Used By
- [[InventoryManager]] - Primary consumer
- [[TradingPanel]] - Trading UI
- [[ShipSelectionPanel]] - Ship selection

---

## Related Files
- [[LocalInventoryService]] - Mock implementation for testing
- [[InventoryManager]] - Client-side orchestrator
- [[PlayFabInventoryService]] - PlayFab-based persistence

---

## Testing Notes
- Requires auth token before API calls
- 30 second default timeout
- All methods are async Task
- JSON serialization via JsonUtility
- Bearer token in Authorization header

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added crew batch operations
- **2025-01**: Added trading endpoints
- **2025-01**: Added error logging

