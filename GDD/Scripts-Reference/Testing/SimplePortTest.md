# SimplePortTest

## Quick Reference

| Attribute | Value |
|-----------|-------|
| **File** | `Assets/Scripts/Testing/SimplePortTest.cs` |
| **Namespace** | `WOS.Testing` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | 826 |
| **Architecture** | Networked port system with docking, protection zones, and scene transitions |

## Purpose

Comprehensive networked port test system for harbor entry/exit mechanics. Handles:
- Protection zone detection (combat disabled)
- Docking zone auto-stop and entry prompt
- Scene transitions to harbor interiors
- Exit positioning with 180° rotation
- Equipment fitting restriction management

## Configuration

### Test Configuration

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `portConfig` | `PortConfigurationSO` | - | Port definition (tier, protection radius, services) |
| `playerShip` | `Transform` | - | Player ship reference (auto-finds if null) |
| `simpleCameraController` | `SimpleCameraController` | - | Camera controller (auto-finds) |

### Docking Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `dockingTransportDistance` | `float` | `100f` | Distance from port edge for docking prompt |
| `alwaysShowGizmos` | `bool` | `true` | Show debug gizmos even when not selected |

### Entry/Exit System

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `testEntryExitSystem` | `bool` | `true` | Enable E/R key entry/exit testing |
| `showEntryPosition` | `bool` | `true` | Show entry position markers in Scene view |

### Scene Transition

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `enableSceneTransition` | `bool` | `false` | Load harbor scene on E key press |
| `overrideSceneName` | `string` | `""` | Override harbor scene name for testing |

## Key Features

### Protection Zone System

```csharp
// GDD-compliant tier-based protection zones
Tier 1: 10km radius (combat disabled)
Tier 2: 25km radius (combat disabled)
Tier 3+: 50km radius (combat disabled)

// Warning boundary
protectionRadius - protectionWarningDistance
```

### Docking Mechanics

```csharp
// Auto-stop when entering docking zone
1. Ship enters blue circle (≤100m from port)
2. Ship auto-stops (velocity = 0, throttle = 0)
3. Entry position saved (for exit)
4. Simulation mode: Auto-enters harbor
5. Scene mode: Wait for E key press
```

### Entry/Exit Controls

| Key | Action | Requirements |
|-----|--------|-------------|
| **E** | Enter Harbor | Must be within docking zone (blue circle) |
| **R** | Exit Harbor | Must be in harbor (after E key press) |

### Equipment Fitting Integration

```csharp
// GDD Requirement: Fitting ONLY allowed in harbor
// Protection zone = Combat disabled, NOT fitting enabled

// Entry (E key)
FittingRestrictionManager.NotifyEnteredPort()
// → Equipment fitting ENABLED

// Exit (R key)
FittingRestrictionManager.NotifyExitedPort()
// → Equipment fitting DISABLED
```

## Public API

### Context Menu Methods

#### `ManualTest()`
```csharp
[ContextMenu("Manual Test")]
public void ManualTest()
```

Tests port configuration with various distances (center, inside, boundary, outside).

## Usage Examples

### Basic Setup

```csharp
// 1. Create empty GameObject "Port_Pearl_Harbor"
// 2. Add SimplePortTest component
// 3. Assign PortConfigurationSO in Inspector
// 4. Position in Ocean scene
// 5. Configure dockingTransportDistance = 100
```

### Scene Transition Setup

```csharp
// Enable real harbor scene loading:
// 1. Set enableSceneTransition = true
// 2. Create harbor scene (e.g., "Harbor_PearlHarbor")
// 3. Set scene name in PortConfigurationSO
// 4. Add ScenePortManager to harbor scene
// 5. Test: Drive ship to port → Press E → Loads scene
```

### Testing Workflow

```csharp
// Step 1: Drive ship toward port
// → Yellow circle appears (approaching warning)
// → Green circle reached (protection zone, combat disabled)
// → Blue circle reached (docking zone, auto-stop)

// Step 2: Press E to enter harbor
// → Ship controller disabled
// → Rigidbody set to Kinematic
// → Position/rotation saved for exit
// → Fitting enabled (if port has upgrade service)

// Step 3: Press R to exit harbor
// → Ship teleported to saved position
// → 180° rotation applied
// → Rigidbody restored to Dynamic
// → Controller re-enabled
// → Throttle/speed reset to 0
```

## Integration Points

### Port Configuration

```csharp
// Reads from PortConfigurationSO:
portConfig.portTier          // Tier 1/2/3 (determines protection radius)
portConfig.ProtectionRadius  // Auto-calculated from tier
portConfig.protectionWarningDistance // Warning zone distance
portConfig.services.hasUpgradeService // Fitting availability
portConfig.harborSceneName   // Scene to load on entry
portConfig.useAsyncLoading   // Use async scene loading
```

### Fitting Restriction Manager

```csharp
// Maps PortConfigurationSO to FittingRestrictionManager
NotifyEnteredPort(portId, portName, portTier, supportsFitting)
NotifyExitedPort(portId, portName)
```

### Network Synchronization

```csharp
// SERVER-AUTHORITATIVE
// - Entry/exit handled server-side
// - Position/rotation synced to all clients
// - Ship state reset via SyncVars
```

### Player Ship Detection

```csharp
// Finds LOCAL networked player
NetworkedNavalController[] allShips = FindObjectsByType<...>();
foreach (var ship in allShips)
{
    if (ship.GetComponent<NetworkIdentity>().isLocalPlayer)
        return ship;
}
```

## Design Notes

### Ship State Management

```csharp
// Harbor Entry: Ship LOCKED
shipController.enabled = false;      // Disable controller
rb.bodyType = RigidbodyType2D.Kinematic; // Disable physics
rb.linearVelocity = Vector2.zero;    // Stop movement
rb.angularVelocity = 0f;             // Stop rotation
SetValue(shipController, "currentThrottle", 0f); // Reset SyncVar

// Harbor Exit: Ship UNLOCKED
rb.bodyType = RigidbodyType2D.Dynamic;   // Restore physics
rb.rotation = exitRotation.eulerAngles.z; // Set rotation
shipController.enabled = true;        // Re-enable controller
```

### Reflection Usage

```csharp
// Resets NetworkedNavalController private fields
var throttleField = typeof(NetworkedNavalController)
    .GetField("currentThrottle", BindingFlags.NonPublic | BindingFlags.Instance);
throttleField.SetValue(shipController, 0f);
```

### Position Persistence

```csharp
// Saved via PlayerPrefs for cross-scene transitions
PlayerPrefs.SetString("PortEntry_Position", JsonUtility.ToJson(position));
PlayerPrefs.SetString("PortEntry_Rotation", JsonUtility.ToJson(rotation));
PlayerPrefs.SetString("PortEntry_PortID", portConfig.name);
PlayerPrefs.SetString("PortEntry_ExitScene", SceneManager.GetActiveScene().name);

// Port-relative offset for multi-port support
PlayerPrefs.SetString("PortEntry_PortCenter", JsonUtility.ToJson(portCenter));
PlayerPrefs.SetString("PortEntry_RelativeOffset", JsonUtility.ToJson(offset));
```

## Visual Debugging

### Gizmo System

```csharp
// Scene View Visualization:
Green Circle    → Protection Zone (combat disabled)
Yellow Circle   → Warning Boundary (approaching)
Blue Circle     → Docking Zone (entry prompt)
White Sphere    → Port center marker
Cyan Sphere     → Saved entry position
Magenta Arrow   → Entry direction
Yellow Arrow    → Exit direction (180° rotated)
Green/Red Line  → Connection to player ship (color = protection status)
```

## Troubleshooting

### Issue: Ship not stopping in docking zone
**Solution**: Check `dockingTransportDistance` (100m recommended)

### Issue: E key not working
**Solution**: Verify ship is within blue circle and chat panel is closed

### Issue: Ship still moving after harbor entry
**Solution**: Ensure `Rigidbody2D.bodyType` is Kinematic, controller is disabled

### Issue: Exit rotation incorrect
**Solution**: Check `shipSpriteForwardOffset` (90° if sprite points up, 0° if right)

### Issue: Can't find player ship
**Solution**: Verify `NetworkIdentity.isLocalPlayer` is true on ship

## Related Scripts

- **PortConfigurationSO**: Port tier, radius, services configuration
- **FittingRestrictionManager**: Equipment fitting availability control
- **HarborExitManager**: Harbor scene exit handler (DEPRECATED)
- **ScenePortManager**: Main scene port return handler (DEPRECATED)
- **NetworkedNavalController**: Ship physics and movement
