---
tags: [script, combat, networking, weapons, implemented]
script-type: NetworkBehaviour
namespace: WOS.Combat.Controllers
file-path: Assets/Scripts/Combat/Controllers/WeaponController.cs
status: ✅ IMPLEMENTED
size: ~12 KB (462 lines)
feature-group: combat
---

# WeaponController.cs

## Quick Reference
**Type**: NetworkBehaviour
**Namespace**: WOS.Combat.Controllers
**File**: `Assets/Scripts/Combat/Controllers/WeaponController.cs`
**Size**: ~12 KB (462 lines)
**Dependencies**: Mirror, WeaponData, BallisticsCalculator

---

## Purpose
Server-authoritative weapon controller for a ship. Manages all weapon mounts, firing, ammunition, and reload cycles.

This is the **primary weapon management system** for each ship. It handles:
- Weapon mount initialization and state management
- Firing commands and projectile spawning
- Ammunition tracking and consumption
- Reload progress updates
- Weapon group selection
- Damage to weapon mounts

---

## Implements GDD Features
- [[Surface-Combat]] - Weapon systems specifications
- [[Network-Architecture]] - Server-authoritative combat

---

## Key Components

### SyncVars (Networked State)
```
weaponLoadout (ShipWeaponLoadout): Current weapon configuration (synced to clients)
selectedWeaponGroup (WeaponCategory): Currently selected weapon group
currentTargetNetId (uint): Network ID of current target
```

### Public Methods
- `CmdFireWeapons()` - Fire currently selected weapon group (Command)
- `CmdSetTarget(uint targetNetId)` - Set current target (Command)
- `CmdSelectWeaponGroup(WeaponCategory category)` - Select weapon group (Command)
- `CmdSetAmmoType(AmmunitionType ammoType)` - Set ammo type for selected weapons (Command)
- `ApplyDamageToMount(int index, WeaponCategory cat, float damage)` - Apply damage to mount (Server)
- `SetMountJammed(int index, WeaponCategory cat, bool jammed)` - Set jam state (Server)

### Events
```csharp
event Action<int, WeaponCategory> OnWeaponFired;      // Fired when weapon fires
event Action<int, WeaponState> OnWeaponStateChanged;  // Fired on state change
event Action<WeaponCategory, AmmunitionType, int> OnAmmoChanged;  // Fired on ammo change
```

---

## Configuration

### Inspector Fields
```
[Header("Configuration")]
weaponConfig (WeaponConfigurationSO): Weapon stats and settings

[Header("Weapon Mounts")]
mainGunMounts (List<Transform>): Main gun mount transforms
secondaryMounts (List<Transform>): Secondary gun mount transforms
torpedoMounts (List<Transform>): Torpedo tube transforms
aaMounts (List<Transform>): Anti-aircraft mount transforms

[Header("Debug")]
enableDebugLogs (bool): Enable combat debug logging
```

---

## Weapon Categories

| Category | Description | Typical Caliber |
|----------|-------------|-----------------|
| MainGun | Primary armament | 200-460mm |
| SecondaryGun | Secondary/dual-purpose | 100-200mm |
| Torpedo | Torpedo tubes | - |
| AntiAir | Dedicated AA guns | 20-127mm |

---

## Technical Details

### Server-Authoritative Pattern
All weapon actions validated on server:
```csharp
[Command]
public void CmdFireWeapons()
{
    if (!CanFire()) return;

    var mounts = weaponLoadout.GetMounts(selectedWeaponGroup);
    foreach (var mount in mounts)
    {
        if (mount.CanFire())
        {
            FireMount(mount);
        }
    }
}
```

### Reload System
```csharp
[Server]
private void UpdateReloads()
{
    float reloadRate = GetBaseReloadRate() * Time.deltaTime;

    foreach (var mount in mounts)
    {
        if (mount.state != WeaponState.Reloading) continue;

        mount.reloadProgress += reloadRate * mount.GetReloadModifier();

        if (mount.reloadProgress >= 1f)
        {
            mount.state = mount.currentAmmo > 0 ? WeaponState.Ready : WeaponState.OutOfAmmo;
        }
    }
}
```

### Crew Efficiency
Reload speed modified by crew:
- `crewEfficiency` - Crew skill factor (0-1.5)
- `assignedCrew / requiredCrew` - Manning ratio
- Result clamped to 0.25-1.5x modifier

---

## Integration Points

### Dependencies
- **Mirror** - NetworkBehaviour, SyncVar, Command, ClientRpc
- [[WeaponData]] - Weapon state structures
- [[BallisticsCalculator]] - Firing solution calculations

### Used By
- [[PlayerShipManager]] - Ship systems coordinator
- [[TargetingSystem]] - Target selection integration
- **ShipUI** - Weapon status display

---

## Example Usage

### Firing Weapons (Client)
```csharp
// Player presses fire button
weaponController.CmdFireWeapons();
```

### Selecting Weapon Group
```csharp
// Switch to torpedoes
weaponController.CmdSelectWeaponGroup(WeaponCategory.Torpedo);
```

### Changing Ammo Type
```csharp
// Switch to HE rounds
weaponController.CmdSetAmmoType(AmmunitionType.HE);
```

---

## Related Files
- [[TargetingSystem]] - Target acquisition and lock
- [[BallisticsCalculator]] - Trajectory calculations
- [[ProjectileManager]] - Projectile spawning and physics
- [[TurretRotator]] - Individual turret control
- [[WeaponData]] - Data structures

---

## Testing Notes
- Server-only: All firing logic runs on server
- Weapon states validated before firing
- Ammo consumption tracked per mount
- Crew efficiency affects reload speed

---

## Changelog
- **2024-12**: Initial implementation with basic firing
- **2025-01**: Added crew efficiency modifiers
- **2025-01**: Added damage and jam states
