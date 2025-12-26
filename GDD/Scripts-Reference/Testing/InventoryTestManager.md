# InventoryTestManager

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/InventoryTestManager.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `MonoBehaviour` |
| **Lines** | 800+ |
| **Architecture** | Comprehensive inventory/equipment testing framework with mock data and persistence |

## Purpose

Advanced test manager for inventory, equipment, crew, ship selection, and trading systems. Provides two modes:
- **Testing Mode**: Mock/persistent data for UI development
- **Live Mode**: PlayFab integration for production testing

Supports hotkey-driven testing, local file persistence, and async API simulation.

## Configuration

### Master Controls

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `useTestingMode` | `bool` | `true` | MASTER TOGGLE: Enable mock data or use PlayFab live data |
| `usePersistence` | `bool` | `true` | Save inventory/equipment changes to disk |
| `testPlayerId` | `string` | `"test_player_001"` | Player ID for file persistence |
| `testShipId` | `string` | `"ship_001"` | Ship ID for loadout persistence |
| `autoLoadOnStart` | `bool` | `true` | Auto-load inventory data on Start |
| `enableHotkeys` | `bool` | `true` | Enable keyboard shortcuts |

### Advanced Options

| Field | Type | Description |
|-------|------|-------------|
| `useLocalService` | `bool` | Use LocalInventoryService for async API simulation |
| `localInventoryService` | `LocalInventoryService` | Reference to local file service |

### Panel References

| Field | Type | Description |
|-------|------|-------------|
| `inventoryPanel` | `InventoryPanel` | Main cargo/inventory panel |
| `equipmentPanel` | `EquipmentPanel` | Ship equipment fitting panel |
| `crewPanel` | `CrewPanel` | Crew management panel |
| `shipSelectionPanel` | `ShipSelectionPanel` | Ship selection/switching panel |
| `tradingPanel` | `TradingPanel` | Port trading interface |

## Hotkey System

### Panel Toggles

| Key | Action | Description |
|-----|--------|-------------|
| **I** | Toggle Inventory | Show/hide cargo inventory |
| **E** | Toggle Equipment | Show/hide equipment fitting |
| **C** | Toggle Crew | Show/hide crew management |
| **P** | Toggle Ship Selection | Show/hide ship selector |
| **T** | Toggle Trading | Show/hide trading interface |
| **R** | Refresh All | Reload all panels with mock data |

### API Testing (when useLocalService = true)

| Key | Action | Description |
|-----|--------|-------------|
| **F1** | Load Inventory | Async load from LocalInventoryService |
| **F2** | Save Inventory | Async save to LocalInventoryService |
| **F3** | Load Loadout | Load ship equipment configuration |
| **F4** | Save Loadout | Save ship equipment configuration |
| **F5** | Reset Data | Clear persistence and reload defaults |
| **F6** | Load Ships | Load available ships data |
| **F7** | Load Crew | Load crew roster data |
| **F8** | Print Stats | Display inventory statistics |

## Key Features

### Dual Mode Operation

```csharp
// Testing Mode (useTestingMode = true)
// - Uses mock/persistent data
// - Local file persistence optional
// - No network dependency
// - Instant feedback

// Live Mode (useTestingMode = false)
// - Uses PlayFab Inventory API
// - Real-time data sync
// - Network required
// - Production-ready
```

### Mock Data Generation

```csharp
// Automatically generates realistic test data:
// - 50+ cargo items (ammo, equipment, modules)
// - Equipment slots (turrets, engines, modules, bridge)
// - 10 crew members (officers, engineers, gunners)
// - 5 ships (destroyers, cruisers, battleships)
// - Market items (buy/sell prices)
```

### Persistence System

```csharp
// File-based persistence for rapid iteration
var fileService = LocalFileInventoryService.Instance;
var savedInventory = await fileService.LoadInventory(testPlayerId);
var savedLoadout = await fileService.LoadLoadout(testPlayerId, testShipId);

// Auto-saves on:
// - Equipment installation/removal
// - Crew assignment/removal
// - Inventory modifications
```

## Public API

### Panel Control Methods

#### `ToggleInventoryPanel()`
```csharp
public void ToggleInventoryPanel()
```
Show/hide cargo inventory panel.

#### `ToggleEquipmentPanel()`
```csharp
public void ToggleEquipmentPanel()
```
Show/hide equipment fitting panel.

#### `ToggleCrewPanel()`
```csharp
public void ToggleCrewPanel()
```
Show/hide crew management panel.

#### `ToggleShipSelectionPanel()`
```csharp
public void ToggleShipSelectionPanel()
```
Show/hide ship selection panel.

#### `ToggleTradingPanel()`
```csharp
public void ToggleTradingPanel()
```
Show/hide trading interface panel.

### Data Management

#### `RefreshAllPanels()` (R key)
```csharp
public void RefreshAllPanels()
```
Reload all panels with current mock data. Useful for resetting UI state during testing.

#### `LoadAllPanelsWithMockData()`
```csharp
private void LoadAllPanelsWithMockData()
```
Populate all panels with generated mock data (cargo, equipment, crew, ships, trading).

## Usage Examples

### Basic Testing Setup

```csharp
// 1. Add InventoryTestManager to scene
// 2. Assign panel references in Inspector
// 3. Enable useTestingMode = true
// 4. Enable usePersistence for auto-save
// 5. Press Play
// 6. Use hotkeys: I/E/C/P/T to test panels
```

### Persistent Testing Workflow

```csharp
// Day 1: Setup initial inventory
// 1. Press I to open inventory
// 2. Add/remove items
// 3. Data auto-saves to Logs/InventoryData/

// Day 2: Continue testing
// 1. Press Play
// 2. Data auto-loads from persistence
// 3. Continue where you left off
```

### Live Mode Testing

```csharp
// Switch to PlayFab testing:
// 1. Set useTestingMode = false
// 2. Ensure PlayFab authenticated
// 3. Panels load from PlayFab inventory
// 4. Changes sync to cloud
```

## Integration Points

### Network Events

```csharp
// Subscribes to inventory network events
InventoryNetworkBehaviour.OnShipInventoryLoaded += HandleShipInventoryLoaded;
InventoryNetworkBehaviour.OnShipInventoryUpdated += HandleShipInventoryUpdated;
```

### Panel Events

```csharp
// Auto-save on equipment changes
equipmentPanel.OnEquipmentItemAddedToInventory += OnEquipmentAddedToInventory;
equipmentPanel.OnCrewItemRemovedFromInventory += OnCrewRemovedFromInventory;
```

### Services Integration

- **LocalFileInventoryService**: File-based persistence
- **PlayFabInventoryService**: Cloud-based inventory (live mode)
- **InventoryServiceProvider**: Automatic service selection

## Mock Data Details

### Cargo Items (50+ items)

```csharp
// Ammunition types
5" shells, 40mm rounds, .50 cal ammo, depth charges, torpedoes

// Equipment
Main guns, AA guns, torpedo tubes, radar, sonar, fire control

// Modules
Armor plating, engine upgrades, fuel tanks, damage control
```

### Equipment Slots

```csharp
// Turret mounts (based on ShipDefinitionSO)
Main Battery: 4-8 slots (5" guns)
AA Battery: 6-12 slots (40mm/20mm)

// Engine slots
Main Engines: 2-4 slots
Auxiliary: 1-2 slots

// Module slots
General: 8-12 slots (radar, sonar, armor, etc.)

// Bridge slot
1 command module slot
```

### Crew Roster (10 members)

```csharp
Roles: Captain, XO, Gunnery Officer, Navigation Officer,
       Engineer, Damage Control, Radar, Sonar, Medic, Quartermaster

Skills: Leadership, Gunnery, Engineering, Navigation, Medical
```

### Ships (5 available)

```csharp
USS Bainbridge (DD-1) - Destroyer
USS Sampson (DD-63) - Destroyer
USS Portland (CA-33) - Heavy Cruiser
USS Cleveland (CL-55) - Light Cruiser
USS Iowa (BB-61) - Battleship
```

## Design Notes

### Type Aliasing Strategy

```csharp
// Distinguishes UI types from Network/Data types
using NetworkCargoGrid = WOS.Networking.Data.CargoGrid;
using UICargoGrid = WOS.UI.Inventory.CargoGrid;
using NetworkShipLoadout = WOS.Player.Data.ShipLoadout;
using UIShipLoadout = WOS.UI.Inventory.ShipLoadout;
```

### Version Tracking

```csharp
// Persistence versioning for data migration
private int currentInventoryVersion = 0;
```

### Auto-Save Triggers

```csharp
// Persistence updates triggered by:
// 1. Equipment installed/removed
// 2. Crew assigned/removed
// 3. Inventory items added/removed
// 4. Ship loadout changed
```

## Troubleshooting

### Issue: Panels don't open
**Solution**: Check panel references assigned in Inspector

### Issue: Data not persisting
**Solution**: Verify `usePersistence = true` and check `Logs/InventoryData/` folder exists

### Issue: Hotkeys not working
**Solution**: Ensure `enableHotkeys = true` and no UI input field is focused

### Issue: Wrong ship slots
**Solution**: Assign correct `defaultShipConfig` (ShipDefinitionSO) in Inspector

## Related Scripts

- **InventoryPanel**: Main cargo inventory UI
- **EquipmentPanel**: Ship equipment fitting UI
- **LocalFileInventoryService**: File persistence service
- **PlayFabInventoryService**: Cloud inventory service
- **ShipDefinitionSO**: Ship configuration (slots, stats)
