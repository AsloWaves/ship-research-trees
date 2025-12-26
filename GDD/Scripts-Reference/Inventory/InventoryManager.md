---
tags: [script, inventory, manager, singleton, implemented]
script-type: MonoBehaviour (Singleton)
namespace: WOS.Inventory
file-path: Assets/Scripts/Inventory/InventoryManager.cs
status: IMPLEMENTED
size: ~20 KB (694 lines)
feature-group: inventory
---

# InventoryManager.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton)
**Namespace**: WOS.Inventory
**File**: `Assets/Scripts/Inventory/InventoryManager.cs`
**Size**: ~20 KB (694 lines)
**Dependencies**: InventoryAPIService, UI Panels, DebugManager

---

## Purpose
Unified inventory management system. Coordinates between UI panels, backend API, and local state. Handles ships, crew, balance, cargo, equipment loadouts, and trading operations.

This is the **client-side inventory orchestrator** that manages:
- Ship collection and active ship selection
- Crew card management and assignment
- Player balance and currency
- Cargo and equipment loadouts
- Trading at ports
- Auto-save with dirty state tracking

---

## Singleton Access

```csharp
public static InventoryManager Instance { get; private set; }
```

Uses `DontDestroyOnLoad` for persistence across scenes.

---

## Configuration

### Inspector Fields
```csharp
[Header("UI Panel References")]
inventoryPanel (InventoryPanel): Cargo grid UI
equipmentPanel (EquipmentPanel): Ship loadout UI
crewPanel (CrewPanel): Crew management UI
shipSelectionPanel (ShipSelectionPanel): Ship fleet UI
tradingPanel (TradingPanel): Port trading UI

[Header("Settings")]
autoSaveInterval (float, 30): Seconds between auto-saves
enableAutoSave (bool, true): Enable auto-save
```

---

## Events

```csharp
public event Action<int> OnBalanceChanged;
public event Action<string> OnActiveShipChanged;
public event Action OnInventoryLoaded;
public event Action OnInventorySaved;
```

---

## Public API

### Data Loading
```csharp
public async Task LoadInventoryAsync()
```
Loads all player data from backend:
- Ships collection
- Crew cards
- Balance
- Active ship cargo

### Data Saving
```csharp
public async Task SaveAllAsync()
```
Saves all pending changes:
- Active ship loadout and cargo
- Pending crew updates

### Accessors
```csharp
public int GetBalance()
public string GetActiveShipId()
public PlayerShipData GetActiveShip()
```

### Panel Opening
```csharp
public void OpenInventory()      // Cargo grid for active ship
public void OpenEquipment()      // Equipment loadout for active ship
public void OpenCrew()           // Crew management
public void OpenShipSelection()  // Fleet management
public async Task OpenTradingAsync(string portId, string portName)
```

---

## Auto-Save System

```csharp
private void Update()
{
    if (enableAutoSave && isDirty && Time.time - lastSaveTime > autoSaveInterval)
    {
        SaveAllAsync();
    }
}
```

- `isDirty` flag tracks unsaved changes
- Saves automatically every 30 seconds (configurable)
- Tracks `lastSaveTime` to avoid excessive saves

---

## UI Event Handlers

Inventory changes tracked via event handlers:

| Event | Sets Dirty | Action |
|-------|-----------|--------|
| OnInventoryItemMoved | Yes | Log position change |
| OnInventoryItemUsed | No | Item usage logic |
| OnInventoryItemDropped | Yes | Remove from cargo |
| OnEquipmentLoadoutSaved | Yes | Update loadout |
| OnEquipmentInstalled | Yes | Log installation |
| OnEquipmentRemoved | Yes | Log removal |
| OnCrewAssigned | Yes | Log assignment |
| OnCrewUnassigned | Yes | Log removal |

---

## State Classes

### PlayerInventoryState
```csharp
public class PlayerInventoryState
{
    public int Balance;
    public List<PlayerShipData> Ships;
    public List<CrewData> Crew;
    public List<CrewData> PendingCrewUpdates;
}
```

### PlayerShipData
```csharp
public class PlayerShipData
{
    public string ShipId;
    public string ShipName;
    public string ShipDefinitionId;
    public string ShipClass;
    public string Nation;
    public int MaxHull, CurrentHull;
    public float MaxSpeed, MaxWeight;
    public int CargoCapacity, CrewAssigned;
    public UIShipLoadout Loadout;
    public UICargoGrid Cargo;
}
```

### CrewData
```csharp
public class CrewData
{
    public string CrewId, CrewName, Classification;
    public int Level, TotalXP;
    public int MaxSailors, CurrentSailors;
    public string AssignedShipId, AssignedPosition;
}
```

---

## Trading Integration

```csharp
public async Task OpenTradingAsync(string portId, string portName)
```

**Flow**:
1. Fetch port market data from API
2. Get active ship cargo info
3. Convert to UI-friendly data structures
4. Open trading panel

**Transaction Handler**:
```csharp
private async void OnTradingTransactionRequested(
    string portId,
    Dictionary<string, int> purchases,
    Dictionary<string, int> sales)
```

---

## Data Conversion Helpers

Converts backend data to UI-friendly structures:
- `ConvertToShipCardData()` → Ship selection cards
- `ConvertToCrewCardData()` → Crew panel cards
- `ConvertToMarketItemData()` → Trading panel items

---

## Integration Points

### Dependencies
- [[InventoryAPIService]] - Backend communication
- [[InventoryPanel]] - Cargo grid UI
- [[EquipmentPanel]] - Equipment UI
- [[CrewPanel]] - Crew management UI
- [[ShipSelectionPanel]] - Fleet UI
- [[TradingPanel]] - Port trading UI

### Uses
- [[DebugManager]] - Logging

---

## Related Files
- [[InventoryAPIService]] - API layer
- [[ShipInventory]] - Ship cargo wrapper
- [[PortInventory]] - Port warehouse wrapper
- [[ItemDatabase]] - Item definitions

---

## Testing Notes
- Singleton with DontDestroyOnLoad
- Auto-save every 30 seconds when dirty
- Type aliases resolve UI/Data type conflicts
- Ships, crew, balance loaded async on startup

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added trading integration
- **2025-01**: Added auto-save system
- **2025-01**: Added crew management

