# ProximityDetector.cs (Chat)

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Chat/ProximityDetector.cs` |
| **Namespace** | `WOS.Chat` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~142 |
| **Architecture** | Client-side nearby ship detection for chat |

## Purpose
Detects nearby ships for proximity chat using Physics2D overlap detection. Updates the nearby ships list periodically for performance. Used by chat system to know which players are within proximity range.

---

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `proximityRange` | 50 | Detection range in Unity units |
| `updateInterval` | 0.5 | Seconds between updates |
| `shipLayerMask` | -1 (All) | Layer mask for ship detection |
| `showDebugGizmos` | true | Show range in Scene view |

---

## State

```csharp
// Nearby ships (read-only access)
private List<NetworkIdentity> nearbyShips = new List<NetworkIdentity>();
public IReadOnlyList<NetworkIdentity> NearbyShips => nearbyShips.AsReadOnly();

// Update timer
private float updateTimer = 0f;
```

---

## Public API

### Range Queries
```csharp
// Check if specific NetworkIdentity is in range
public bool IsInRange(NetworkIdentity identity)

// Check if specific connection ID is in range
public bool IsInRange(uint connectionId)

// Get distance to ship (-1 if not in range)
public float GetDistanceToShip(NetworkIdentity identity)
```

### Configuration
```csharp
// Update proximity range (clamped 10-200)
public void SetProximityRange(float range)
```

---

## Detection Logic

```csharp
private void Update()
{
    // Only run on local player
    if (!isClient || !isLocalPlayer)
        return;

    updateTimer += Time.deltaTime;
    if (updateTimer >= updateInterval)
    {
        UpdateNearbyShips();
        updateTimer = 0f;
    }
}

private void UpdateNearbyShips()
{
    nearbyShips.Clear();

    // Physics2D overlap detection
    Collider2D[] colliders = Physics2D.OverlapCircleAll(
        transform.position,
        proximityRange,
        shipLayerMask
    );

    foreach (Collider2D collider in colliders)
    {
        if (collider.transform == transform) continue;  // Skip self

        NetworkIdentity identity = collider.GetComponent<NetworkIdentity>();
        if (identity != null)
            nearbyShips.Add(identity);
    }
}
```

---

## Debug Visualization

```csharp
private void OnDrawGizmosSelected()
{
    if (!showDebugGizmos) return;

    // Draw range circle
    Gizmos.color = new Color(0f, 1f, 0f, 0.2f);
    Gizmos.DrawWireSphere(transform.position, proximityRange);

    // Draw lines to nearby ships
    Gizmos.color = Color.green;
    foreach (var ship in nearbyShips)
    {
        if (ship != null)
            Gizmos.DrawLine(transform.position, ship.transform.position);
    }
}
```

---

## Range Clamping

```csharp
public void SetProximityRange(float range)
{
    proximityRange = Mathf.Clamp(range, 10f, 200f);
}
```

| Minimum | Maximum | Default |
|---------|---------|---------|
| 10 units | 200 units | 50 units |

---

## Usage Example

```csharp
// Check if player is nearby
if (proximityDetector.IsInRange(targetIdentity))
{
    // Can send proximity chat
}

// Get all nearby ships
foreach (var ship in proximityDetector.NearbyShips)
{
    Debug.Log($"Nearby: {ship.name}");
}

// Get distance
float distance = proximityDetector.GetDistanceToShip(targetIdentity);
if (distance >= 0)
    Debug.Log($"Distance: {distance} units");

// Adjust range from settings
proximityDetector.SetProximityRange(75f);
```

---

## Integration Points

### Dependencies
- `Mirror` - NetworkBehaviour, NetworkIdentity
- `Physics2D` - OverlapCircleAll
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `ChatManager` - Server-side proximity filtering
- `ChatPanel` - Show nearby player count

---

## Design Notes

### Client-Side Only
- Only runs on local player (isLocalPlayer check)
- Each player tracks their own nearby ships

### Performance
- Updates every 0.5 seconds (not every frame)
- Uses Physics2D overlap (efficient)
- Layer mask can filter irrelevant objects

### Note: Server Uses Different Logic
ChatManager does its own proximity check server-side using Vector3.Distance() for authoritative filtering. This component is for client-side awareness/UI.
