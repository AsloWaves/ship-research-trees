---
tags: [script, combat, networking, targeting, implemented]
script-type: NetworkBehaviour
namespace: WOS.Combat.Controllers
file-path: Assets/Scripts/Combat/Controllers/TargetingSystem.cs
status: ✅ IMPLEMENTED
size: ~15 KB (556 lines)
feature-group: combat
---

# TargetingSystem.cs

## Quick Reference
**Type**: NetworkBehaviour
**Namespace**: WOS.Combat.Controllers
**File**: `Assets/Scripts/Combat/Controllers/TargetingSystem.cs`
**Size**: ~15 KB (556 lines)
**Dependencies**: Mirror, BallisticsData, BallisticsCalculator

---

## Purpose
Server-authoritative targeting system for a ship. Handles target acquisition, tracking, and fire control solutions.

This is the **fire control system** that manages:
- Target detection within visual/radar range
- Multiple target tracking (up to 10 targets)
- Target lock acquisition and maintenance
- Firing solution calculation with lead angles
- Line-of-sight validation
- Environmental condition effects

---

## Implements GDD Features
- [[Surface-Combat]] - Targeting and fire control specifications
- [[Network-Architecture]] - Server-authoritative combat

---

## Key Components

### SyncVars (Networked State)
```
primaryTargetNetId (uint): Current primary target's network ID
lockState (TargetLockState): Current lock state (NoTarget, Acquiring, Locked, Jamming)
lockProgress (float): Lock acquisition progress (0-1)
```

### Public Methods
- `ScanForTargets()` - Scan for targets in detection range (Server)
- `CmdSetPrimaryTarget(uint targetNetId)` - Set primary target (Command)
- `ClearPrimaryTarget()` - Clear current target (Server)
- `GetFiringSolution(BallisticProfile profile)` - Calculate firing solution
- `GetFireControlAccuracy()` - Get accuracy bonus from fire control
- `SetEnvironment(BallisticEnvironment env)` - Set weather conditions
- `GetPredictedPosition(uint netId, float time)` - Get predicted target position

### Events
```csharp
event Action<uint> OnTargetAcquired;          // New target detected
event Action<uint> OnTargetLost;              // Target lost from tracking
event Action<uint> OnTargetLocked;            // Full lock achieved
event Action<TargetLockState> OnLockStateChanged;  // Lock state changed
```

---

## Configuration

### Inspector Fields
```
[Header("Detection")]
visualDetectionRange (float, 20000): Visual range in meters
radarDetectionRange (float, 30000): Radar range in meters
updateInterval (float, 0.5): Seconds between scans

[Header("Tracking")]
maxTrackedTargets (int, 10): Maximum simultaneous targets
trackingLossTime (float, 5): Seconds before losing track

[Header("Fire Control")]
fireControlAccuracyBonus (float, 0.1): Base accuracy bonus
targetLockTime (float, 3): Seconds to achieve lock

[Header("Debug")]
enableDebugLogs (bool): Enable targeting debug logs
```

---

## Target Lock States

| State | Description | UI Indicator |
|-------|-------------|--------------|
| NoTarget | No target selected | Empty reticle |
| Acquiring | Building lock on target | Spinning/pulsing |
| Locked | Full lock achieved | Solid/green |
| Jamming | Lock being disrupted | Flickering |

---

## Technical Details

### Target Detection Algorithm
```csharp
[Server]
private List<NetworkIdentity> FindPotentialTargets()
{
    var targets = new List<NetworkIdentity>();
    float detectRange = GetEffectiveDetectionRange();

    var colliders = Physics.OverlapSphere(transform.position, detectRange);
    foreach (var col in colliders)
    {
        var netId = col.GetComponentInParent<NetworkIdentity>();
        if (netId != null && netId.netId != this.netId)
        {
            if (HasLineOfSight(netId.transform.position))
            {
                targets.Add(netId);
            }
        }
    }
    return targets;
}
```

### Track Quality System
```
trackQuality (float, 0-1):
  - Increases when target visible (+0.1 per update)
  - Decreases when not visible (-0.05 per update)
  - Affects lock acquisition speed
  - Affects accuracy bonus
```

### Lock Acquisition
```csharp
[Server]
private void UpdateTargetLock()
{
    if (lockState != TargetLockState.Acquiring) return;

    if (primary.isVisible)
    {
        lockProgress += (updateInterval / targetLockTime) * primary.trackQuality;

        if (lockProgress >= 1f)
        {
            lockState = TargetLockState.Locked;
            OnTargetLocked?.Invoke(primaryTargetNetId);
        }
    }
    else
    {
        // Lock decays if not visible
        lockProgress -= updateInterval / (targetLockTime * 2f);
    }
}
```

### Firing Solution Calculation
```csharp
public FiringSolution GetFiringSolution(BallisticProfile profile)
{
    if (primaryTargetNetId == 0 || lockState != TargetLockState.Locked)
        return null;

    var solution = BallisticsCalculator.CalculateFiringSolution(
        transform.position,
        target.lastKnownPosition,
        target.lastKnownVelocity,
        profile,
        currentEnvironment
    );

    solution.accuracy += fireControlAccuracyBonus * target.trackQuality;
    return solution;
}
```

---

## TrackedTarget Data Structure

```csharp
public class TrackedTarget
{
    public uint netId;               // Network identity
    public Transform transform;       // Target transform
    public Vector3 lastKnownPosition; // Last observed position
    public Vector3 lastKnownVelocity; // Calculated velocity
    public float lastSeenTime;        // Time last visible
    public float trackQuality;        // 0-1, tracking data quality
    public bool isVisible;            // Currently has LOS
}
```

---

## Integration Points

### Dependencies
- **Mirror** - NetworkBehaviour, SyncVar, Command
- [[BallisticsData]] - Environment and profile data
- [[BallisticsCalculator]] - Firing solution math

### Used By
- [[WeaponController]] - Firing decisions
- **ShipUI** - Target display and lock indicator

---

## Example Usage

### Setting Target (Client)
```csharp
// Player clicks on enemy ship
uint targetNetId = clickedShip.netId;
targetingSystem.CmdSetPrimaryTarget(targetNetId);
```

### Getting Firing Solution
```csharp
// WeaponController requests solution
FiringSolution solution = targetingSystem.GetFiringSolution(shellProfile);
if (solution != null && solution.isValid)
{
    FireAtTarget(solution.predictedPosition, solution.elevationAngle);
}
```

### Checking Lock Status
```csharp
if (targetingSystem.GetLockState() == TargetLockState.Locked)
{
    // Full accuracy available
    float accuracyBonus = targetingSystem.GetFireControlAccuracy();
}
```

---

## Related Files
- [[WeaponController]] - Uses targeting for firing
- [[BallisticsCalculator]] - Firing solution math
- [[BallisticsData]] - Data structures
- [[ProjectileManager]] - Projectile physics

---

## Testing Notes
- Detection uses Physics.OverlapSphere
- LOS uses Physics.Raycast
- Track quality affects lock speed and accuracy
- Environmental conditions modify effective range

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added track quality system
- **2025-01**: Added environmental modifiers
