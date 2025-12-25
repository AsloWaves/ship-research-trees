---
tags: [script, ui, debug, implemented, phase1]
script-type: MonoBehaviour
namespace: WOS.UI
file-path: WOS2.3V2 Research/Scripts/UI/ShipDebugUI.cs
status: ✅ IMPLEMENTED (Legacy - replaced by ShipDebugUIManager)
size: 3.1 KB
---

# ShipDebugUI.cs

## Quick Reference
**Type**: MonoBehaviour
**Namespace**: WOS.UI
**File**: `Scripts/UI/ShipDebugUI.cs`
**Size**: 3.1 KB
**Dependencies**: Unity.Mathematics, Mirror, TMPro, WOS.Player, WOS.Environment

---

## Purpose
Legacy real-time debug UI panel displaying ship telemetry and ocean information in a single text field.

Updates ship speed, heading, position, velocity, throttle, rudder, navigation mode, and ocean depth/biome data at 10Hz. Toggle with F3 key. **Note**: Superseded by ShipDebugUIManager for improved layout control.

---

## Implements GDD Features
- [[GDD-Debug-UI]] - Developer debug information display
- [[GDD-Development-Tools]] - In-game telemetry monitoring

---

## Key Components

### Public Properties
```
debugTextField (TMP_InputField): Multi-line text field for debug output
updateRate (float): Update frequency in Hz (default 10Hz)
showInMultiplayer (bool): Display for local player only
```

### Public Methods
- `ToggleDebugPanel()` - Show/hide debug UI
- `SetUpdateRate(float hz)` - Change update frequency

### Key Private Methods
- `UpdateDebugInfo()` - Refresh all telemetry data
- `FindLocalPlayer()` - Auto-detect player ship in multiplayer
- `FormatDebugText()` - Build formatted string with all data

---

## Configuration

### Inspector Fields
```
[Header("UI Reference")]
debugTextField (TMP_InputField or TextMeshProUGUI): Text display field

[Header("Settings")]
updateRate (float, 10.0f): Updates per second
toggleKey (KeyCode, F3): Key to show/hide panel
autoHideOnStart (bool, true): Start with panel hidden

[Header("Multiplayer")]
showInMultiplayer (bool, true): Enable in networked games
localPlayerOnly (bool, true): Only show for controlled ship
```

---

## Integration Points

### Dependencies (What This Needs)
- WOS.Player.SimpleNavalController - Ship physics and controls
- WOS.Player.NetworkedNavalController - Multiplayer ship support
- WOS.Environment.OceanChunkManager - Ocean depth and biome data
- WOS.Debugging.DebugManager - Debug system integration
- Mirror.NetworkIdentity - Multiplayer local player detection
- Unity.Mathematics - Vector math
- TMPro - Text display

### Used By (What Uses This)
- [[DebugManager]] - Coordinates debug UI systems
- [[GameUIManager]] - UI panel management

---

## Technical Details

### Performance Considerations
- Updates at 10Hz (every 0.1 seconds) to reduce overhead
- String formatting creates garbage (use sparingly)
- Auto-finds components on first update, then caches
- Only updates when panel is visible
- Multiplayer-aware: local player only

### Display Information
**Ship Data**: Speed (knots), heading (degrees), throttle (%), rudder angle (degrees), position (world coordinates), velocity (vector), rate of turn (degrees/second)

**Navigation**: Auto/manual mode, waypoint distance

**Ocean Data**: Depth (meters), biome type, ocean tile coordinates

---

## How It Works

### Initialization
On Start, caches references to debug text field. Auto-hides panel if configured. In multiplayer, finds local player's NetworkIdentity for proper data display.

### Main Loop
Update checks for F3 key press to toggle visibility. InvokeRepeating calls UpdateDebugInfo at configured Hz rate (default 10Hz). Only updates when panel is visible.

### Key Algorithms
**Data Collection**: Queries SimpleNavalController/NetworkedNavalController for ship telemetry. Retrieves ocean data from OceanChunkManager at ship position. Formats all data into multi-line string.

**String Formatting**: Uses string interpolation to build formatted output with labels and units. Includes line breaks for readability.

---

## Example Usage
```csharp
// Add to UI canvas
var debugUI = gameObject.AddComponent<ShipDebugUI>();
debugUI.debugTextField = GetComponent<TMP_InputField>();
debugUI.updateRate = 10.0f; // 10Hz

// Toggle programmatically
debugUI.ToggleDebugPanel();

// Change update rate
debugUI.SetUpdateRate(5.0f); // 5Hz for better performance
```

---

## Related Files
- [[ShipDebugUIManager]] - Replacement with 6 separate panels for better layout
- [[SimpleNavalController]] - Source of ship telemetry data
- [[NetworkedNavalController]] - Multiplayer ship controller
- [[OceanChunkManager]] - Ocean depth and biome data source
- [[DebugManager]] - Debug system coordinator
- [[GDD-Debug-UI]] - Design specification for debug tools

---

## Testing Notes
- F3 toggle tested in both single-player and multiplayer
- Data accuracy verified against ship controller values
- Update rate tested at 1Hz, 5Hz, 10Hz, 30Hz
- Multiplayer local player detection confirmed
- Ocean depth and biome data validated
- String formatting tested with various ship states
- Legacy UI Text and TextMeshPro both supported
- MUIP InputField integration verified

**Known Limitations**:
- Single-text-field layout limits formatting flexibility
- String concatenation creates garbage every update
- **Recommendation**: Use ShipDebugUIManager for new projects

---

## Changelog
- **2024-01**: Initial implementation with basic ship telemetry
- **2024-02**: Added ocean depth and biome information
- **2024-03**: Added multiplayer local player detection
- **2024-04**: Marked as legacy, recommend ShipDebugUIManager replacement
