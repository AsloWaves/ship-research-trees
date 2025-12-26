# PortZoneManager

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Zones/PortZoneManager.cs` |
| **Namespace** | `WOS.Zones` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | 221 |
| **Architecture** | Server-authoritative port zone manager |

---

## Purpose

**Server-side manager** that coordinates all port zones in the scene. Tracks which ships are in which ports, handles automatic port registration, and provides a centralized API for port-ship relationships.

**Key Responsibilities**:
- Auto-discover and register all `PortZone` components in scene
- Track ship entry/exit from port zones (server-authoritative)
- Maintain bidirectional mappings: port→ships and ship→port
- Provide query API for port occupancy and ship location

**Integration**: Works with `PortZone` triggers to create a centralized port management system.

---

## Configuration

### Inspector Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `autoRegisterPorts` | `bool` | `true` | Automatically find and register all PortZone components in scene on server start |

---

## Server-Only Data Structures

### Port Registry
```csharp
// Port zones indexed by portId
Dictionary<string, PortZone> registeredPorts

// Ships in each port (portId -> List<NetworkIdentity>)
Dictionary<string, List<NetworkIdentity>> shipsInPorts

// Ship to port mapping (shipNetId -> portId)
Dictionary<uint, string> shipPortMap
```

**Data Flow**:
1. **OnStartServer**: Clear all dictionaries
2. **AutoRegisterAllPorts**: Find all `PortZone` components → call `RegisterPort` for each
3. **RegisterPort**: Add to `registeredPorts`, initialize empty ship list in `shipsInPorts`
4. **OnShipEnterPort**: Update `shipsInPorts` and `shipPortMap`
5. **OnShipExitPort**: Remove from `shipsInPorts` and `shipPortMap`

---

## Key Code Snippets

### Auto-Registration System
```csharp
[Server]
private void AutoRegisterAllPorts()
{
    PortZone[] allPorts = FindObjectsByType<PortZone>(FindObjectsSortMode.None);
    foreach (PortZone port in allPorts)
    {
        RegisterPort(port);
    }

    DebugManager.Log(DebugCategory.System,
        $"[PortZoneManager] Auto-registered {allPorts.Length} port zones", this);
}
```

**Design Choice**: Uses `FindObjectsByType<T>()` instead of deprecated `FindObjectsOfType<T>()` for Unity 6 compatibility.

---

### Ship Entry Tracking
```csharp
[Server]
public void OnShipEnterPort(NetworkIdentity ship, string portId)
{
    // Check if ship is already in a port
    if (shipPortMap.TryGetValue(ship.netId, out string currentPortId))
    {
        // Remove from previous port
        if (shipsInPorts.ContainsKey(currentPortId))
        {
            shipsInPorts[currentPortId].Remove(ship);
        }
    }

    // Add to new port
    if (!shipsInPorts.ContainsKey(portId))
    {
        shipsInPorts[portId] = new List<NetworkIdentity>();
    }

    shipsInPorts[portId].Add(ship);
    shipPortMap[ship.netId] = portId;

    DebugManager.Log(DebugCategory.System,
        $"[PortZoneManager] Ship {ship.netId} entered port {portId} ({GetShipCountInPort(portId)} ships now in port)",
        this);
}
```

**Automatic Port Switching**: If a ship enters a new port while already in another port, it's automatically removed from the previous port before being added to the new one.

---

## Public API

### Server-Side Methods

#### Port Registration
```csharp
[Server]
public void RegisterPort(PortZone port)
```
Register a port zone with the manager. Validates port data and portId before registration.

**Validation**:
- Port and port data cannot be null
- Port ID must not be empty
- Warns if port ID already registered (overwrites)

---

#### Ship Entry/Exit
```csharp
[Server]
public void OnShipEnterPort(NetworkIdentity ship, string portId)

[Server]
public void OnShipExitPort(NetworkIdentity ship, string portId)
```
Track ship entering/exiting ports. Automatically handles port switching if ship enters new port.

**Called By**: `PortZone.OnTriggerEnter2D()` and `PortZone.OnTriggerExit2D()`

---

#### Port Queries
```csharp
[Server]
public string GetShipCurrentPort(NetworkIdentity ship)           // Returns null if not in port
public List<NetworkIdentity> GetShipsInPort(string portId)       // Returns copy of ship list
public int GetShipCountInPort(string portId)                     // Returns 0 if port not found
public bool IsShipInPort(NetworkIdentity ship, string portId)    // Check specific port
public bool IsShipInAnyPort(NetworkIdentity ship)                // Check any port
```

**Design Choice**: `GetShipsInPort()` returns a **copy** of the internal list to prevent external modification of server state.

---

#### Port Lookup
```csharp
public PortZone GetPort(string portId)           // Returns null if not found
public List<PortZone> GetAllPorts()              // Returns copy of all registered ports
```

**Thread Safety**: These methods can be called from client or server, but port registration data is only maintained on server.

---

## Usage Examples

### Example 1: Check if Ship Can Customize
```csharp
public class ShipCustomizationMenu : MonoBehaviour
{
    private PortZoneManager portManager;

    private void Start()
    {
        portManager = FindFirstObjectByType<PortZoneManager>();
    }

    public bool CanCustomizeShip(NetworkIdentity ship)
    {
        if (!NetworkServer.active)
            return false;

        // Get current port
        string portId = portManager.GetShipCurrentPort(ship);
        if (string.IsNullOrEmpty(portId))
            return false; // Not in port

        // Get port zone
        PortZone port = portManager.GetPort(portId);
        if (port == null)
            return false;

        // Check if port supports customization
        return port.GetPortData().customizationAvailable;
    }
}
```

---

### Example 2: Get Port Occupancy Info
```csharp
[Server]
public void LogPortOccupancy()
{
    List<PortZone> allPorts = portManager.GetAllPorts();

    foreach (PortZone port in allPorts)
    {
        string portId = port.GetPortData().portId;
        int shipCount = portManager.GetShipCountInPort(portId);
        List<NetworkIdentity> ships = portManager.GetShipsInPort(portId);

        Debug.Log($"Port: {port.GetPortData().portName}, Ships: {shipCount}");
        foreach (NetworkIdentity ship in ships)
        {
            Debug.Log($"  - Ship NetID: {ship.netId}");
        }
    }
}
```

---

### Example 3: Force Evict Ship from Port
```csharp
[Server]
public void EvictShipFromPort(NetworkIdentity ship)
{
    string currentPort = portManager.GetShipCurrentPort(ship);
    if (!string.IsNullOrEmpty(currentPort))
    {
        portManager.OnShipExitPort(ship, currentPort);
        Debug.Log($"Evicted ship {ship.netId} from port {currentPort}");
    }
}
```

---

## Integration Points

### With PortZone
```
PortZone (Trigger Detection)
    ↓ OnTriggerEnter2D
PortZoneManager.OnShipEnterPort(ship, portId)
    ↓ Updates tracking dictionaries
    ↓ Logs entry event
```

**Relationship**: `PortZone` components handle physics trigger detection, `PortZoneManager` centralizes tracking logic.

---

### With Ship Systems
```
Ship enters port trigger
    ↓
PortZoneManager tracks entry (server)
    ↓
Ship systems query:
    - Can repair? (port tier check)
    - Can customize? (port capabilities)
    - Can trade? (market access)
```

**Query Pattern**: Ship systems use `GetShipCurrentPort()` then query port data for capabilities.

---

## Design Notes

### Server-Authoritative Architecture
- All tracking dictionaries are **server-only**
- Port entry/exit validation happens on server
- Clients receive notifications via TargetRpc from `PortZone`

**Security**: Prevents client tampering with port state.

---

### Automatic Port Switching
When a ship enters a new port while already in another port:
1. Remove from previous port's ship list
2. Add to new port's ship list
3. Update ship→port mapping

**Use Case**: Supports multi-port scenes where ships can move between ports without explicit exit handling.

---

### Thread Safety Considerations
- `GetShipsInPort()` returns a **copy** to prevent external modification
- `GetAllPorts()` returns a **copy** to prevent external modification
- All dictionaries are private and only modified via controlled methods

**Design Principle**: Immutable external API prevents accidental state corruption.

---

### Performance Considerations
- **O(1) lookups**: Dictionary-based tracking for fast port/ship queries
- **Minimal allocations**: Only allocates on entry/exit events, not per frame
- **Auto-registration**: One-time `FindObjectsByType<T>()` call on server start

**Scalability**: Supports hundreds of ships and dozens of ports with minimal overhead.

---

### Deprecated Notice
**Current Status**: Active implementation (Phase 2)

**Future Migration**: Will be replaced by:
- `WOS.Port.Ocean.PortZoneManager` (new implementation)
- `WOS.Port.Ocean.PortZoneInstance` (instance management)
- `WOS.ScriptableObjects.PortDefinitionSO` (configuration)
- Concentric zone model (AoP/AoI - Area of Protection/Interest)

**Migration Timeline**: TBD - existing system remains functional.
