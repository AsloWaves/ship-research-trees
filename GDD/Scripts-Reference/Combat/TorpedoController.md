---
tags: [script, combat, networking, torpedoes, implemented]
script-type: NetworkBehaviour
namespace: WOS.Combat.Controllers
file-path: Assets/Scripts/Combat/Controllers/TorpedoController.cs
status: IMPLEMENTED
size: ~13 KB (459 lines)
feature-group: combat
---

# TorpedoController.cs

## Quick Reference
**Type**: NetworkBehaviour
**Namespace**: WOS.Combat.Controllers
**File**: `Assets/Scripts/Combat/Controllers/TorpedoController.cs`
**Size**: ~13 KB (459 lines)
**Dependencies**: Mirror, TorpedoDefinitionSO, ProjectileManager

---

## Purpose
Server-authoritative torpedo management for a ship. Handles torpedo tubes, loading, aiming, and launching. Based on GDD Submarine-Warfare.md specifications.

This is the **per-ship torpedo controller** that manages:
- Torpedo tube initialization and state
- Target bearing and spread angle settings
- Individual and salvo launches
- Reload cycle management
- Depth-based launch restrictions (submarines)
- Firing arc validation

---

## Implements GDD Features
- [[Submarine-Warfare]] - Torpedo mechanics
- [[Network-Architecture]] - Server-authoritative combat

---

## Key Components

### SyncVars (Networked State)
```
targetBearing (float): Current aim bearing (0-360)
spreadAngle (float): Spread angle for salvos
```

### Public Methods
- `CmdSetTargetBearing(float bearing)` - Set target bearing (Command)
- `CmdSetSpreadAngle(float angle)` - Set spread for salvos (Command)
- `CmdLaunchTorpedo(int tubeIndex)` - Launch single torpedo (Command)
- `CmdLaunchSalvo(TubeFacing facing)` - Launch all ready tubes (Command)
- `SetCurrentDepth(float depth)` - Set depth for submarines
- `GetTubeState(int index)` - Get tube status for UI
- `GetAllTubeStates()` - Get all tube states
- `CountReadyTubes(TubeFacing facing)` - Count ready tubes by facing

### Events
```csharp
event Action<int> OnTorpedoLaunched;                    // Torpedo fired
event Action<int> OnTubeReloaded;                       // Tube reloaded
event Action<int, TorpedoTubeStatus> OnTubeStatusChanged;  // Status changed
```

---

## Configuration

### Inspector Fields
```
[Header("Configuration")]
defaultTorpedoType (TorpedoDefinitionSO): Default torpedo type

[Header("Tube Configuration")]
tubeConfigs (List<TorpedoTubeConfig>): Tube mount configs

[Header("Aiming")]
defaultSpreadAngle (float, 5): Default spread degrees
maxSpreadAngle (float, 30): Maximum spread degrees

[Header("Debug")]
enableDebugLogs (bool): Enable debug logging
```

---

## Tube Facings

| Facing | Direction | Typical Use |
|--------|-----------|-------------|
| Bow | Forward | Destroyers, Submarines |
| Stern | Rear | Submarines |
| Port | Left side | Cruisers, Destroyers |
| Starboard | Right side | Cruisers, Destroyers |

---

## Tube States

| Status | Description |
|--------|-------------|
| Ready | Loaded and ready to fire |
| Reloading | Reloading a torpedo |
| Empty | No more reloads available |
| Damaged | Tube damaged, cannot fire |
| Flooded | Flooded (submarines) |

---

## Technical Details

### Salvo Spread Calculation
```csharp
[Command]
public void CmdLaunchSalvo(TubeFacing facing)
{
    var readyTubes = GetReadyTubes(facing);
    if (readyTubes.Count == 0) return;

    // Calculate spread angles
    float totalSpread = spreadAngle * (readyTubes.Count - 1);
    float startAngle = targetBearing - (totalSpread / 2f);

    for (int i = 0; i < readyTubes.Count; i++)
    {
        float launchAngle = startAngle + (spreadAngle * i);
        LaunchFromTube(readyTubes[i].tubeIndex, launchAngle);
    }
}
```

### Firing Arc Check
```csharp
private bool IsBearingInArc(float bearing, TorpedoTubeState tube)
{
    float tubeBearing = tube.fixedAngle;
    float arcHalf = 45f; // 90 degree arc per side

    switch (tube.facing)
    {
        case TubeFacing.Bow: tubeBearing = 0f; break;
        case TubeFacing.Stern: tubeBearing = 180f; break;
        case TubeFacing.Port: tubeBearing = 270f; break;
        case TubeFacing.Starboard: tubeBearing = 90f; break;
    }

    float diff = Mathf.Abs(Mathf.DeltaAngle(bearing, tubeBearing));
    return diff <= arcHalf;
}
```

### Reload System
```csharp
[Server]
private void UpdateTubeReloads()
{
    foreach (var tube in tubeStates)
    {
        if (tube.status != TorpedoTubeStatus.Reloading) continue;
        if (tube.reloadsRemaining <= 0) continue;

        float reloadTime = tube.loadedTorpedo?.reloadTime ?? 60f;
        tube.reloadProgress += Time.deltaTime / reloadTime;

        if (tube.reloadProgress >= 1f)
        {
            tube.status = TorpedoTubeStatus.Ready;
            OnTubeReloaded?.Invoke(tube.tubeIndex);
        }
    }
}
```

---

## Support Types

### TorpedoTubeConfig
```csharp
[Serializable]
public class TorpedoTubeConfig
{
    public TubeFacing facing = TubeFacing.Bow;
    public float fixedAngle = 0f;
    public Vector3 localPosition;
}
```

### TorpedoTubeState
```csharp
[Serializable]
public class TorpedoTubeState
{
    public int tubeIndex;
    public TubeFacing facing;
    public float fixedAngle;
    public TorpedoTubeStatus status;
    public TorpedoDefinitionSO loadedTorpedo;
    public float reloadProgress;
    public int reloadsRemaining;
}
```

---

## Integration Points

### Dependencies
- **Mirror** - NetworkBehaviour, SyncVar, Command, ClientRpc
- [[TorpedoDefinitionSO]] - Torpedo configuration
- [[ProjectileManager]] - Torpedo spawning

### Used By
- [[PlayerShipManager]] - Ship systems coordinator
- **TorpedoUI** - Tube status display

---

## Example Usage

### Launching Single Torpedo
```csharp
// Set target bearing
torpedoController.CmdSetTargetBearing(45f);

// Launch from tube 0
torpedoController.CmdLaunchTorpedo(0);
```

### Launching Salvo
```csharp
// Set spread angle
torpedoController.CmdSetSpreadAngle(10f);

// Launch all port tubes
torpedoController.CmdLaunchSalvo(TubeFacing.Port);
```

### Checking Tube Status
```csharp
int readyCount = torpedoController.CountReadyTubes(TubeFacing.Bow);
if (readyCount > 0)
{
    torpedoController.CmdLaunchSalvo(TubeFacing.Bow);
}
```

---

## Related Files
- [[TorpedoDefinitionSO]] - Torpedo configuration asset
- [[ProjectileManager]] - Handles torpedo spawning
- [[TorpedoVisual]] - Client-side torpedo rendering
- [[WeaponController]] - Gun weapon management

---

## Testing Notes
- Server-only logic with Command/ClientRpc pattern
- Depth restrictions for submarine torpedoes
- 90 degree arc per facing direction
- Reloads tracked per tube

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added salvo spread calculation
- **2025-01**: Added depth-based restrictions

