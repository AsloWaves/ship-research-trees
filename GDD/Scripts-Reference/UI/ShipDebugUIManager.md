---
tags: [script, ui, debug, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ShipDebugUIManager.cs
status: ✅ IMPLEMENTED
size: 4.2 KB
---

# ShipDebugUIManager.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/ShipDebugUIManager.cs`
**Size**: 4.2 KB
**Dependencies**: Unity.Mathematics, Mirror, TMPro, WOS.Player, WOS.Environment

---

## Purpose
Manages 6 separate debug panels displaying comprehensive ship telemetry across the bottom of the screen.

Replaces monolithic ShipDebugUI with individual TextMeshProUGUI fields for superior layout control. Always visible, updates at 10Hz, local player only in multiplayer. Displays vessel specs, propulsion, navigation, nearest port, network stats, and reserved panel.

---

## Implements GDD Features
- [[GDD-Debug-UI-Advanced]] - Multi-panel debug system with organized information
- [[GDD-Development-Tools]] - Comprehensive telemetry monitoring
- [[GDD-Network-Stats]] - Multiplayer connection diagnostics

---

## Key Components

### Public Properties
```
Panel 1 - VESSEL & SPECS (6 TextMeshProUGUI fields):
  - vesselName, vesselClass, vesselLength, vesselDisplacement, maxRudderAngle

Panel 2 - PROPULSION & OCEAN (7 TextMeshProUGUI fields):
  - currentSpeed, targetSpeed, throttle, maxSpeed, oceanDepth, oceanTile, oceanZone

Panel 3 - NAVIGATION (4 TextMeshProUGUI fields):
  - bearing, rateOfTurn, rudderAngle, navigationMode

Panel 4 - NEAREST PORT (3 TextMeshProUGUI fields):
  - portName, portBearing, portDistance

Panel 5 - NETWORK (5 TextMeshProUGUI fields):
  - connectionStatus, networkMode, ping, rtt, connectionQuality

Panel 6 - RESERVED (placeholder for future features)
```

### Public Methods
- `SetUpdateRate(float hz)` - Change refresh frequency
- `SetPrecision(int decimals)` - Configure decimal places for floats
- `ShowPanel(int panelIndex, bool show)` - Toggle individual panels

### Key Private Methods
- `UpdateVesselPanel()` - Refresh Panel 1 vessel/specs data
- `UpdatePropulsionPanel()` - Refresh Panel 2 propulsion/ocean data
- `UpdateNavigationPanel()` - Refresh Panel 3 navigation data
- `UpdatePortPanel()` - Refresh Panel 4 nearest port data
- `UpdateNetworkPanel()` - Refresh Panel 5 network stats
- `FindLocalPlayer()` - Auto-detect player ship in multiplayer

---

## Configuration

### Inspector Fields
```
[Header("Panel 1 - Vessel & Specs")]
vesselNameText (TextMeshProUGUI): Ship name display
vesselClassText (TextMeshProUGUI): Ship class display
vesselLengthText (TextMeshProUGUI): Length in meters
vesselDisplacementText (TextMeshProUGUI): Displacement in tons
maxRudderAngleText (TextMeshProUGUI): Max rudder angle in degrees

[Header("Panel 2 - Propulsion & Ocean")]
currentSpeedText (TextMeshProUGUI): Current speed in knots
targetSpeedText (TextMeshProUGUI): Desired speed in knots
throttleText (TextMeshProUGUI): Throttle percentage
maxSpeedText (TextMeshProUGUI): Maximum speed capability
oceanDepthText (TextMeshProUGUI): Ocean depth in meters
oceanTileText (TextMeshProUGUI): Tile coordinates
oceanZoneText (TextMeshProUGUI): Biome/zone name

[Header("Panel 3 - Navigation")]
bearingText (TextMeshProUGUI): Ship heading in degrees
rateOfTurnText (TextMeshProUGUI): Turn rate in degrees/second
rudderAngleText (TextMeshProUGUI): Current rudder angle
navigationModeText (TextMeshProUGUI): Auto/Manual mode

[Header("Panel 4 - Nearest Port")]
portNameText (TextMeshProUGUI): Port name
portBearingText (TextMeshProUGUI): Bearing to port in degrees
portDistanceText (TextMeshProUGUI): Distance in nautical miles

[Header("Panel 5 - Network Stats")]
connectionStatusText (TextMeshProUGUI): Connected/Disconnected
networkModeText (TextMeshProUGUI): Host/Client/Server
pingText (TextMeshProUGUI): Ping in milliseconds
rttText (TextMeshProUGUI): Round-trip time
connectionQualityText (TextMeshProUGUI): Excellent/Good/Poor

[Header("Panel 6 - Reserved")]
reserved1Text (TextMeshProUGUI): Future use
reserved2Text (TextMeshProUGUI): Future use
reserved3Text (TextMeshProUGUI): Future use

[Header("Settings")]
updateRate (float, 10.0f): Updates per second
decimalPrecision (int, 1): Decimal places for floats
alwaysVisible (bool, true): Always show panels
localPlayerOnly (bool, true): Multiplayer local player only
```

---

## Integration Points

### Dependencies (What This Needs)
- WOS.Player.SimpleNavalController - Ship physics and controls
- WOS.Player.NetworkedNavalController - Multiplayer ship support
- WOS.Environment.OceanChunkManager - Ocean depth and biome data
- WOS.Debugging.DebugManager - Debug system integration
- WOS.Navigation.PortManager - Nearest port calculation
- Mirror.NetworkIdentity - Multiplayer local player detection
- Mirror.NetworkManager - Network statistics
- Unity.Mathematics - Vector math
- TMPro - Individual text field display

### Used By (What Uses This)
- [[DebugManager]] - Coordinates debug UI systems
- [[GameUIManager]] - UI panel hierarchy management
- [[DeveloperConsole]] - Advanced debug integration

---

## Technical Details

### Performance Considerations
- Updates at 10Hz (every 0.1 seconds) default
- Individual TextMeshProUGUI fields avoid string concatenation
- Cached component references minimize GetComponent calls
- Only updates active/visible fields
- Multiplayer-aware: local player only
- No garbage generation during updates (pre-allocated strings)

### Panel Organization
**Bottom Screen Layout**: 6 horizontal panels spanning screen width, organized by information category for quick reference during development and testing.

---

## How It Works

### Initialization
On Start, caches all TextMeshProUGUI references for 6 panels. Auto-finds ship controller, ocean manager, and port manager. In multiplayer, identifies local player's NetworkIdentity. Validates all field assignments.

### Main Loop
InvokeRepeating calls update methods at configured Hz (default 10Hz). Each panel has dedicated update method for modularity. Updates only visible panels to save processing.

### Key Algorithms
**Panel 1 - Vessel**: Queries ship ScriptableObject for static specs (name, class, length, displacement, max rudder). Updates once on ship change, otherwise cached.

**Panel 2 - Propulsion**: Reads current/target speed, throttle from NavalController. Retrieves max speed from ship specs. Queries OceanChunkManager for depth, tile coordinates, biome name.

**Panel 3 - Navigation**: Calculates bearing from ship's forward vector. Retrieves rate of turn and rudder angle from controller. Shows auto/manual navigation mode.

**Panel 4 - Port**: Calls PortManager to find nearest port. Calculates bearing and distance. Updates port name. Shows "None" if no ports in range.

**Panel 5 - Network**: Queries Mirror NetworkManager for connection status, mode, ping, RTT. Calculates connection quality from latency thresholds.

**Panel 6 - Reserved**: Empty, ready for future features.

---

## Example Usage
```csharp
// Add to UI canvas
var debugUIManager = gameObject.AddComponent<ShipDebugUIManager>();

// Assign all TextMeshProUGUI fields in Inspector

// Configure update rate
debugUIManager.SetUpdateRate(5.0f); // 5Hz for better performance

// Set decimal precision
debugUIManager.SetPrecision(2); // 2 decimal places

// Hide specific panel
debugUIManager.ShowPanel(5, false); // Hide network panel
```

---

## Related Files
- [[ShipDebugUI]] - Legacy single-text-field predecessor
- [[SimpleNavalController]] - Ship telemetry data source
- [[NetworkedNavalController]] - Multiplayer ship controller
- [[OceanChunkManager]] - Ocean depth and biome data
- [[PortManager]] - Nearest port calculations
- [[DebugManager]] - Debug system coordinator
- [[GDD-Debug-UI-Advanced]] - Design specification for multi-panel debug system

---

## Testing Notes
- All 6 panels tested with various ship states
- Data accuracy verified against ship controller values
- Update rate tested at 1Hz, 5Hz, 10Hz, 30Hz
- Multiplayer local player detection confirmed
- Ocean depth and biome data validated
- Nearest port calculations verified
- Network stats tested in host/client/server modes
- Individual panel visibility toggle confirmed
- Decimal precision tested with 0, 1, 2, 3 places
- Performance profiled: <0.1ms per update at 10Hz

**Advantages Over ShipDebugUI**:
- Individual text fields enable precise layout control
- No string concatenation reduces garbage generation
- Modular panels allow selective display
- Network stats panel for multiplayer diagnostics
- Reserved panel for future expansion
- Better visual organization across screen bottom

---

## Changelog
- **2024-04**: Initial implementation replacing ShipDebugUI
- **2024-05**: Added Panel 4 nearest port information
- **2024-06**: Added Panel 5 network statistics
- **2024-07**: Added configurable decimal precision
- **2024-08**: Added individual panel visibility controls
