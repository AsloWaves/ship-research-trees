---
tags: [script, port, harbor, trigger, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Harbor
file-path: Assets/Scripts/Port/Harbor/DockingSquareController.cs
status: IMPLEMENTED
size: ~186 lines
feature-group: port
---

# DockingSquareController.cs

## Quick Reference
**Type**: NetworkBehaviour (Trigger Controller)
**Namespace**: WOS.Port.Harbor
**File**: `Assets/Scripts/Port/Harbor/DockingSquareController.cs`
**Size**: ~186 lines
**Dependencies**: HarborSceneManager, CircleCollider2D

---

## Purpose
Individual dock trigger controller. Manages CircleCollider2D trigger detection for dock zones, provides visual highlight feedback, and delegates player detection to HarborSceneManager. Server-only trigger processing.

---

## Configuration

```csharp
[Header("Dock Identity")]
[SerializeField] private int dockIndex = -1;
[SerializeField] private bool isLargeDock = false;

[Header("Visual Feedback")]
[SerializeField] private SpriteRenderer highlightRenderer;
[SerializeField] private Color normalColor = new Color(0.2f, 0.5f, 0.8f, 0.3f);
[SerializeField] private Color occupiedColor = new Color(0.8f, 0.2f, 0.2f, 0.3f);
[SerializeField] private Color activeColor = new Color(0.2f, 0.8f, 0.2f, 0.5f);

[Header("State")]
[SyncVar(hook = nameof(OnOccupiedChanged))]
[SerializeField] private bool isOccupied = false;
```

---

## Properties

```csharp
public int DockIndex => dockIndex;
public bool IsLargeDock => isLargeDock;
public bool IsOccupied => isOccupied;
```

---

## Initialization

```csharp
public void Initialize(int index, Vector2 size, bool largeDock)
{
    dockIndex = index;
    isLargeDock = largeDock;

    // Configure collider
    var collider = GetComponent<CircleCollider2D>();
    collider.isTrigger = true;
    collider.radius = Mathf.Max(size.x, size.y) * 0.5f;

    // Configure visual
    if (highlightRenderer != null)
    {
        highlightRenderer.transform.localScale = new Vector3(size.x, size.y, 1f);
        UpdateVisual();
    }
}
```

---

## Trigger Detection (Server-Only)

```csharp
private void OnTriggerEnter2D(Collider2D other)
{
    if (!isServer) return;

    var netId = other.GetComponent<NetworkIdentity>();
    if (netId == null) return;

    // Only process player ships
    var playerShip = other.GetComponent<PlayerShipManager>();
    if (playerShip == null) return;

    // Check if dock can accept this ship
    if (!CanAcceptShip(playerShip))
    {
        return;
    }

    HarborSceneManager.Instance?.OnPlayerEnteredDockZone(netId, dockIndex);
    SetActiveHighlight(true);
}

private void OnTriggerExit2D(Collider2D other)
{
    if (!isServer) return;

    var netId = other.GetComponent<NetworkIdentity>();
    if (netId == null) return;

    var playerShip = other.GetComponent<PlayerShipManager>();
    if (playerShip == null) return;

    HarborSceneManager.Instance?.OnPlayerExitedDockZone(netId, dockIndex);
    SetActiveHighlight(false);
}
```

---

## Ship Validation

```csharp
private bool CanAcceptShip(PlayerShipManager ship)
{
    // Check if dock is already occupied
    if (isOccupied) return false;

    // Large ships require large docks
    if (ship.ShipConfig.IsCapitalShip && !isLargeDock)
    {
        return false;
    }

    return true;
}
```

---

## Occupancy Management

```csharp
[Server]
public void SetOccupied(bool occupied)
{
    isOccupied = occupied;
}

private void OnOccupiedChanged(bool oldValue, bool newValue)
{
    UpdateVisual();
}
```

---

## Visual Feedback

```csharp
private void UpdateVisual()
{
    if (highlightRenderer == null) return;

    if (isOccupied)
    {
        highlightRenderer.color = occupiedColor;
    }
    else
    {
        highlightRenderer.color = normalColor;
    }
}

private void SetActiveHighlight(bool active)
{
    if (highlightRenderer == null) return;

    if (active && !isOccupied)
    {
        highlightRenderer.color = activeColor;
    }
    else
    {
        UpdateVisual();
    }
}
```

---

## Visual States

| State | Color | Description |
|-------|-------|-------------|
| Normal | Blue (0.2, 0.5, 0.8, 0.3) | Available dock |
| Occupied | Red (0.8, 0.2, 0.2, 0.3) | Ship docked here |
| Active | Green (0.2, 0.8, 0.2, 0.5) | Player in zone, can dock |

---

## Integration Points

### Dependencies
- [[HarborSceneManager]] - Receives detection events
- CircleCollider2D - Trigger detection
- SpriteRenderer - Visual feedback

### Used By
- [[HarborSceneManager]] - Spawns and queries
- [[PlayerPortStateController]] - Receives state updates

---

## Related Files
- [[HarborSceneManager]] - Parent manager
- [[ExitZoneController]] - Similar pattern
- [[PlayerPortStateController]] - State updates

---

## Design Notes
- Server-only trigger processing (prevents client manipulation)
- Visual feedback synchronized via SyncVar hook
- Large dock validation prevents capital ships at small docks
- Delegates all logic to HarborSceneManager
- Color-coded states for player feedback

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added large dock validation
- **2025-01**: Added SyncVar for occupancy

