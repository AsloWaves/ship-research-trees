# PortZone

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Zones/PortZone.cs` |
| **Namespace** | `WOS.Zones` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | 214 |
| **Architecture** | Trigger-based port zone detection (DEPRECATED) |
| **Status** | ⚠️ **DEPRECATED** - See migration path below |

---

## Purpose

**[DEPRECATED]** Trigger-based component that detects when ships enter/exit port zones using Unity's 2D physics system. Communicates with `PortZoneManager` to track port occupancy and notifies clients when they enter/exit ports.

**Deprecation Notice**: This script uses `PortZoneData` which has been replaced by:
- `WOS.Port.Ocean.PortZoneManager` - New port zone management
- `WOS.Port.Ocean.PortZoneInstance` - Individual zone instances
- `WOS.ScriptableObjects.PortDefinitionSO` - Port configuration
- `WOS.Port.Core.PortTransitionManager` - Scene transitions
- **Concentric Zone Model** (AoP/AoI - Area of Protection/Interest)

**Migration Path**: Replace with new port system components listed above.

---

## Configuration

### Inspector Settings

| Field | Type | Description |
|-------|------|-------------|
| **portData** | `PortZoneData` | Port zone data asset (DEPRECATED - use PortDefinitionSO) |
| **showDebugGizmos** | `bool` | Show port zone visualization in Scene view |

### Required Components
```csharp
[RequireComponent(typeof(CircleCollider2D))]
```
Automatically adds `CircleCollider2D` if not present.

---

## Key Code Snippets

### Collider Setup
```csharp
private void Awake()
{
    // Setup collider as trigger
    zoneCollider = GetComponent<CircleCollider2D>();
    if (zoneCollider != null)
    {
        zoneCollider.isTrigger = true;

        // Set collider radius from port data
        if (portData != null)
        {
            zoneCollider.radius = portData.portRadius;
        }
    }

    // Find port manager
    portManager = FindFirstObjectByType<PortZoneManager>();
}
```

**Design Choice**: Automatically configures collider radius from `PortZoneData` to ensure consistency between data and collider bounds.

---

### Trigger Detection
```csharp
private void OnTriggerEnter2D(Collider2D other)
{
    // Only process on server
    if (!isServer)
        return;

    // Check if entering object is a networked ship
    NetworkIdentity identity = other.GetComponent<NetworkIdentity>();
    if (identity != null && portData != null)
    {
        OnShipEnterPort(identity);
    }
}
```

**Server-Authoritative**: Only the server processes trigger events to prevent client manipulation.

---

### Ship Entry Notification
```csharp
[Server]
private void OnShipEnterPort(NetworkIdentity ship)
{
    // Notify port manager (server-side tracking)
    if (portManager != null)
    {
        portManager.OnShipEnterPort(ship, portData.portId);
    }

    // Notify ship's client with full port info
    if (ship.connectionToClient != null)
    {
        TargetPortEntered(
            ship.connectionToClient,
            portData.portId,
            portData.portName,
            (int)portData.tier,
            portData.customizationAvailable
        );
    }
}
```

**Dual Notification**:
1. **Server-side**: Update `PortZoneManager` tracking
2. **Client-side**: Send `TargetRpc` to ship's owning client

---

### Client Notification
```csharp
[TargetRpc]
private void TargetPortEntered(NetworkConnection target, string portId, string portName,
                               int tierValue, bool supportsFitting)
{
    DebugManager.Log(DebugCategory.System, $"[PortZone] ⚓ Entered {portName} (Tier {tierValue})", this);

    // Notify FittingRestrictionManager
    if (FittingRestrictionManager.Instance != null)
    {
        PortTier tier = (PortTier)tierValue;
        FittingRestrictionManager.Instance.NotifyEnteredPort(portId, portName, tier, supportsFitting);
    }
}
```

**Integration**: Automatically notifies `FittingRestrictionManager` to enable/disable ship customization based on port capabilities.

---

## Public API

### Data Access
```csharp
public PortZoneData GetPortData() => portData;
```
Returns the port's configuration data.

---

## Lifecycle Events

### Initialization
```csharp
Awake()
    ↓ Configure CircleCollider2D as trigger
    ↓ Set radius from portData
    ↓ Find PortZoneManager

Start()
    ↓ Position at portData.portCenter
    ↓ Register with PortZoneManager
```

---

### Trigger Events
```csharp
OnTriggerEnter2D()
    ↓ Check if server
    ↓ Get NetworkIdentity from collider
    ↓ OnShipEnterPort(ship)
        ↓ portManager.OnShipEnterPort(ship, portId)
        ↓ TargetPortEntered(ship.connectionToClient, ...)

OnTriggerExit2D()
    ↓ Check if server
    ↓ Get NetworkIdentity from collider
    ↓ OnShipExitPort(ship)
        ↓ portManager.OnShipExitPort(ship, portId)
        ↓ TargetPortExited(ship.connectionToClient, ...)
```

---

## Debug Visualization

### Scene View Gizmos
```csharp
private void OnDrawGizmos()
{
    if (!showDebugGizmos || portData == null)
        return;

    // Draw port zone circle (wireframe)
    Gizmos.color = portData.portColor;
    Gizmos.DrawWireSphere(transform.position, portData.portRadius);

    // Draw filled circle (semi-transparent)
    Gizmos.color = new Color(portData.portColor.r, portData.portColor.g,
                             portData.portColor.b, 0.1f);
    Gizmos.DrawSphere(transform.position, portData.portRadius);
}

private void OnDrawGizmosSelected()
{
    if (!showDebugGizmos || portData == null)
        return;

    // Draw port name in Scene view
    #if UNITY_EDITOR
    UnityEditor.Handles.Label(transform.position, portData.portName);
    #endif
}
```

**Visual Debugging**:
- **Wireframe sphere**: Port zone boundary
- **Semi-transparent fill**: Zone area
- **Label (selected)**: Port name displayed in Scene view

---

## Usage Examples

### Example 1: Setup Port Zone in Scene
```csharp
// 1. Create empty GameObject
GameObject portObj = new GameObject("Port_NewYork");

// 2. Add PortZone component
PortZone zone = portObj.AddComponent<PortZone>();

// 3. Assign port data asset
zone.portData = Resources.Load<PortZoneData>("Ports/NewYork");

// 4. Enable debug visualization
zone.showDebugGizmos = true;

// 5. Position will be set from portData.portCenter in Start()
```

**Note**: CircleCollider2D is automatically added by `RequireComponent` attribute.

---

### Example 2: Create Port Data Asset
```csharp
PortZoneData portData = ScriptableObject.CreateInstance<PortZoneData>();
portData.portId = "newyork";
portData.portName = "New York";
portData.portCenter = new Vector2(1000, 500);
portData.portRadius = 150f;
portData.tier = PortTier.Tier3_Regional;
portData.customizationAvailable = true;
portData.portColor = new Color(0.2f, 0.5f, 0.8f, 1f);

#if UNITY_EDITOR
UnityEditor.AssetDatabase.CreateAsset(portData, "Assets/Resources/Ports/NewYork.asset");
#endif
```

---

## Integration Points

### With PortZoneManager
```
PortZone (Physics Detection)
    ↓ OnTriggerEnter2D
    ↓ OnShipEnterPort()
        ↓ portManager.OnShipEnterPort(ship, portId)
PortZoneManager (Centralized Tracking)
    ↓ Updates shipsInPorts dictionary
    ↓ Updates shipPortMap dictionary
```

**Separation of Concerns**:
- `PortZone`: Physics detection (instance-based)
- `PortZoneManager`: Centralized tracking (singleton pattern)

---

### With FittingRestrictionManager
```
PortZone
    ↓ TargetPortEntered (TargetRpc)
Client receives notification
    ↓ FittingRestrictionManager.NotifyEnteredPort()
        ↓ Enable/disable ship customization UI
        ↓ Update fitting restrictions based on port tier
```

**Client-Side Integration**: Automatically enables/disables ship customization based on port capabilities.

---

## Design Notes

### Server-Client Architecture
- **Server**: Processes trigger events, updates PortZoneManager, sends notifications
- **Client**: Receives TargetRpc notifications, updates UI systems

**Security**: Client cannot fake port entry/exit events.

---

### TargetRpc vs ObserversRpc
```csharp
[TargetRpc]  // Only sent to ship's owning client
private void TargetPortEntered(NetworkConnection target, ...)

// NOT using:
[ObserversRpc]  // Would be sent to all clients
```

**Optimization**: Port entry notifications only sent to the ship's owner, not broadcast to all clients.

---

### Collider Configuration
- **Trigger Mode**: `isTrigger = true` prevents physical collisions
- **Radius Sync**: Collider radius matches `portData.portRadius`
- **Position Sync**: Transform position set to `portData.portCenter`

**Data-Driven Design**: All port properties defined in ScriptableObject, not in Inspector.

---

### Migration to New Port System

#### Old System (Deprecated)
```csharp
// Old: Single-zone model
PortZone zone;
zone.portData.portRadius;  // Single radius
```

#### New System
```csharp
// New: Concentric zone model
PortDefinitionSO portDef;
portDef.areaOfProtection;   // Inner zone (safe harbor)
portDef.areaOfInterest;     // Outer zone (port approach)
```

**Key Differences**:
- **Old**: Single circular zone
- **New**: Dual concentric zones (AoP + AoI)
- **Old**: `PortZoneData` (data-only)
- **New**: `PortDefinitionSO` (configuration + behaviors)
- **Old**: Trigger-based detection
- **New**: Zone instance management with transition states

---

### Performance Considerations
- **Minimal Allocations**: Trigger events don't allocate memory
- **Server-Only Processing**: Reduces client CPU load
- **One-Time Setup**: Collider configuration happens once in Awake()

**Physics Layer**: Should be on a dedicated layer to avoid unnecessary trigger checks with non-ship objects.

---

### Known Limitations
1. **Single Zone**: Cannot represent complex port areas (solved in new system with AoP/AoI)
2. **No Transition States**: Instant entry/exit (new system adds gradual transitions)
3. **PortZoneData**: Deprecated data format (replaced by PortDefinitionSO)
4. **No Visual Styling**: Limited customization (new system adds PortVisualStyleSO)

---

## Deprecation Timeline

**Current Status**: ⚠️ Marked as `[Obsolete]` but still functional

**Migration Steps**:
1. Audit existing PortZone instances in scenes
2. Create equivalent PortDefinitionSO assets
3. Replace PortZone with new port system components
4. Update scripts that reference PortZoneData
5. Test zone transitions with new concentric model
6. Remove deprecated components

**Blocking Issues**: None - old system continues to work during migration.

**Recommendation**: New features should use the new port system exclusively.
