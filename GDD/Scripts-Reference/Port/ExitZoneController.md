---
tags: [script, port, harbor, trigger, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Port.Harbor
file-path: Assets/Scripts/Port/Harbor/ExitZoneController.cs
status: IMPLEMENTED
size: ~96 lines
feature-group: port
---

# ExitZoneController.cs

## Quick Reference
**Type**: NetworkBehaviour (Trigger Controller)
**Namespace**: WOS.Port.Harbor
**File**: `Assets/Scripts/Port/Harbor/ExitZoneController.cs`
**Size**: ~96 lines
**Dependencies**: HarborSceneManager, CircleCollider2D

---

## Purpose
Exit zone trigger controller for leaving harbor. Simple trigger detection that delegates to HarborSceneManager. Server-only processing with visual feedback.

---

## Configuration

```csharp
[Header("Visual Feedback")]
[SerializeField] private SpriteRenderer highlightRenderer;
[SerializeField] private Color normalColor = new Color(0.8f, 0.6f, 0.2f, 0.3f);
[SerializeField] private Color activeColor = new Color(0.8f, 0.8f, 0.2f, 0.5f);
```

---

## Initialization

```csharp
public void Initialize(float radius)
{
    var collider = GetComponent<CircleCollider2D>();
    collider.isTrigger = true;
    collider.radius = radius;

    if (highlightRenderer != null)
    {
        highlightRenderer.transform.localScale = Vector3.one * radius * 2f;
        highlightRenderer.color = normalColor;
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

    var playerShip = other.GetComponent<PlayerShipManager>();
    if (playerShip == null) return;

    HarborSceneManager.Instance?.OnPlayerEnteredExitZone(netId);
    SetActiveHighlight(true);
}

private void OnTriggerExit2D(Collider2D other)
{
    if (!isServer) return;

    var netId = other.GetComponent<NetworkIdentity>();
    if (netId == null) return;

    var playerShip = other.GetComponent<PlayerShipManager>();
    if (playerShip == null) return;

    HarborSceneManager.Instance?.OnPlayerExitedExitZone(netId);
    SetActiveHighlight(false);
}
```

---

## Visual Feedback

```csharp
private void SetActiveHighlight(bool active)
{
    if (highlightRenderer == null) return;

    highlightRenderer.color = active ? activeColor : normalColor;
}
```

---

## Visual States

| State | Color | Description |
|-------|-------|-------------|
| Normal | Orange (0.8, 0.6, 0.2, 0.3) | Exit zone visible |
| Active | Yellow (0.8, 0.8, 0.2, 0.5) | Player in zone, can exit |

---

## Integration Points

### Dependencies
- [[HarborSceneManager]] - Receives detection events
- CircleCollider2D - Trigger detection
- SpriteRenderer - Visual feedback

### Used By
- [[HarborSceneManager]] - Spawns and initializes

---

## Related Files
- [[HarborSceneManager]] - Parent manager
- [[DockingSquareController]] - Similar pattern
- [[PlayerPortStateController]] - State updates

---

## Design Notes
- Simple delegation pattern to HarborSceneManager
- Server-only trigger processing
- Minimal state (no occupancy tracking)
- Visual feedback for player awareness
- Orange/yellow color scheme distinguishes from dock zones

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added visual feedback

