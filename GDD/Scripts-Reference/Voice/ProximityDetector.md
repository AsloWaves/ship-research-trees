# ProximityDetector.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Voice/ProximityDetector.cs` |
| **Namespace** | `WOS.Voice` |
| **Inheritance** | `NetworkBehaviour` |
| **Required Components** | `NetworkedNavalController` |
| **Lines** | ~187 |
| **Architecture** | Nearby ship detection for voice/chat |

## Purpose
Detects nearby ships for proximity voice chat and other proximity-based systems. Uses spatial detection to track ships within configurable range and provides distance/direction queries for 3D positional audio.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `detectionRange` | 50 units | Maximum detection range |
| `updateInterval` | 0.5s | Detection update frequency |
| `shipLayerMask` | All | Layer mask filter |
| `showDebugInfo` | false | Enable debug logging |

---

## Public Properties

```csharp
// Read-only list of nearby ships
public IReadOnlyList<NetworkedNavalController> NearbyShips => nearbyShips;
```

---

## Core Detection Logic

```csharp
private void Update()
{
    if (!isLocalPlayer) return;

    updateTimer += Time.deltaTime;
    if (updateTimer >= updateInterval)  // Every 0.5s
    {
        updateTimer = 0f;
        UpdateNearbyShips();
    }
}

private void UpdateNearbyShips()
{
    nearbyShips.Clear();

    // Find all ships in scene
    NetworkedNavalController[] allShips =
        FindObjectsByType<NetworkedNavalController>(FindObjectsSortMode.None);

    foreach (var ship in allShips)
    {
        // Skip self
        if (ship == localShip) continue;

        // Skip inactive
        if (ship == null || !ship.gameObject.activeInHierarchy) continue;

        // Check distance
        float distance = Vector3.Distance(transform.position, ship.transform.position);

        if (distance <= detectionRange)
            nearbyShips.Add(ship);
    }
}
```

---

## Query Methods

```csharp
// Get ship at index
public NetworkedNavalController GetNearbyShip(int index)

// Check if ship is in range
public bool IsShipInRange(NetworkedNavalController ship)

// Get distance to ship
public float GetDistanceToShip(NetworkedNavalController ship)

// Get normalized direction to ship
public Vector3 GetDirectionToShip(NetworkedNavalController ship)

// Force immediate detection update
public void ForceUpdate()
```

---

## Editor Visualization

```csharp
private void OnDrawGizmosSelected()
{
    // Draw detection range sphere
    Gizmos.color = Color.cyan;
    Gizmos.DrawWireSphere(transform.position, detectionRange);

    // Draw lines to nearby ships
    if (Application.isPlaying && nearbyShips != null)
    {
        Gizmos.color = Color.green;
        foreach (var ship in nearbyShips)
            if (ship != null)
                Gizmos.DrawLine(transform.position, ship.transform.position);
    }
}
```

---

## Usage Example

```csharp
var detector = GetComponent<ProximityDetector>();

// Get all nearby ships
foreach (var ship in detector.NearbyShips)
{
    float distance = detector.GetDistanceToShip(ship);
    Vector3 direction = detector.GetDirectionToShip(ship);

    Debug.Log($"{ship.name} at {distance:F1}m, direction: {direction}");
}

// Check specific ship
if (detector.IsShipInRange(targetShip))
    Debug.Log("Target in range!");

// Force update
detector.ForceUpdate();
```

---

## Integration Points

### Dependencies
- `WOS.Player.NetworkedNavalController` - Ship reference (required)
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `ProximityVoiceHandler` - 3D voice positioning
- `ProximityDetector` (Chat) - Proximity chat detection

---

## Design Notes

### Local Player Only
- Detection only runs on local player
- Disables on remote clients for performance

### Update Frequency
- Default 0.5s between updates
- Balances accuracy vs performance
- Use `ForceUpdate()` for immediate detection

### Scene Query
- Uses `FindObjectsByType` for ship discovery
- Filters by distance and active state
- No physics-based detection (layer mask prepared but not used)
