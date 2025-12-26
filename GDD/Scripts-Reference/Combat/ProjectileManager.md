---
tags: [script, combat, networking, projectiles, implemented]
script-type: NetworkBehaviour (Singleton)
namespace: WOS.Combat.Controllers
file-path: Assets/Scripts/Combat/Controllers/ProjectileManager.cs
status: ✅ IMPLEMENTED
size: ~13 KB (493 lines)
feature-group: combat
---

# ProjectileManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Combat.Controllers
**File**: `Assets/Scripts/Combat/Controllers/ProjectileManager.cs`
**Size**: ~13 KB (493 lines)
**Dependencies**: Mirror, WeaponData, BallisticsCalculator

---

## Purpose
Server-authoritative projectile management system. Handles spawning, physics updates, collision detection, and damage application for all projectiles.

This is the **central projectile coordinator** that manages:
- Shell and torpedo spawning
- Physics simulation (gravity, drag)
- Collision detection via raycasting
- Hit result calculation via BallisticsCalculator
- Visual projectile synchronization to clients
- Object pooling for performance

---

## Implements GDD Features
- [[Surface-Combat]] - Projectile physics
- [[Network-Architecture]] - Server-authoritative projectiles

---

## Key Components

### Singleton Access
```csharp
public static ProjectileManager Instance { get; }
```

### Public Methods
- `SpawnProjectile(...)` - Spawn a shell projectile (Server)
- `SpawnTorpedo(...)` - Spawn a torpedo (Server)

### Events
```csharp
event Action<ProjectileData> OnProjectileSpawned;       // New projectile created
event Action<ProjectileData, HitResult> OnProjectileHit; // Projectile hit target
event Action<ProjectileData> OnProjectileExpired;       // Projectile expired (missed)
```

---

## Configuration

### Inspector Fields
```
[Header("Configuration")]
maxProjectileLifetime (float, 30): Max flight time in seconds
maxActiveProjectiles (int, 500): Pool limit
hitLayers (LayerMask): Layers that can be hit

[Header("Projectile Prefabs")]
smallShellPrefab (GameObject): <100mm shells
mediumShellPrefab (GameObject): 100-200mm shells
largeShellPrefab (GameObject): 200-350mm shells
torpedoPrefab (GameObject): Torpedo visual

[Header("Debug")]
enableDebugLogs (bool): Combat logging
drawTrajectories (bool): Gizmo trajectory lines
```

---

## Projectile Spawning

### Shell Spawning
```csharp
[Server]
public ProjectileData SpawnProjectile(
    uint sourceShipNetId,      // Firing ship
    int sourceMountIndex,      // Which weapon mount
    Vector3 position,          // Spawn position
    Vector3 direction,         // Aim direction
    BallisticProfile profile,  // Shell characteristics
    AmmunitionType ammoType    // AP, HE, SAP
)
```

### Torpedo Spawning
```csharp
[Server]
public ProjectileData SpawnTorpedo(
    uint sourceShipNetId,
    int sourceMountIndex,
    Vector3 position,
    Vector3 direction,
    float speed,
    float damage,
    float range
)
```

---

## Physics Simulation

### Update Loop (FixedUpdate)
```csharp
[Server]
private void UpdateProjectiles(float deltaTime)
{
    for (int i = activeProjectiles.Count - 1; i >= 0; i--)
    {
        var projectile = activeProjectiles[i];

        // Check lifetime
        projectile.timeAlive += deltaTime;
        if (projectile.timeAlive >= projectile.maxLifetime)
        {
            OnProjectileExpired?.Invoke(projectile);
            projectile.hasDetonated = true;
            continue;
        }

        // Store old position for raycast
        Vector3 oldPosition = projectile.position;

        // Apply physics
        UpdateProjectilePhysics(projectile, deltaTime);

        // Check collisions
        CheckProjectileCollision(projectile, oldPosition);
    }
}
```

### Physics Application
```csharp
private void UpdateProjectilePhysics(ProjectileData projectile, float deltaTime)
{
    // Gravity
    projectile.velocity.y -= BallisticsConstants.Gravity * deltaTime;

    // Drag (simplified)
    float dragForce = BallisticsConstants.DragCoefficient * 0.0001f *
                     projectile.velocity.sqrMagnitude;
    projectile.velocity -= projectile.velocity.normalized * dragForce * deltaTime;

    // Position update
    projectile.position += projectile.velocity * deltaTime;
    projectile.currentVelocity = projectile.velocity.magnitude;
}
```

---

## Collision Detection

### Raycast Check
```csharp
private void CheckProjectileCollision(ProjectileData projectile, Vector3 oldPosition)
{
    Vector3 moveDir = projectile.position - oldPosition;
    float moveDistance = moveDir.magnitude;

    // Raycast along movement path
    if (Physics.Raycast(oldPosition, moveDir.normalized, out RaycastHit hit,
        moveDistance, hitLayers))
    {
        ProcessHit(projectile, hit);
    }

    // Water surface check (y = 0)
    if (oldPosition.y > 0 && projectile.position.y <= 0)
    {
        ProcessWaterHit(projectile, oldPosition);
    }
}
```

### Hit Processing
```csharp
private void ProcessHit(ProjectileData projectile, RaycastHit hit)
{
    // Get target info
    var netId = hit.collider.GetComponentInParent<NetworkIdentity>();
    var armorZone = hit.collider.GetComponent<ArmorZone>();

    // Calculate hit result
    HitResult result = BallisticsCalculator.CalculateHit(
        projectile,
        hit.point,
        hit.normal,
        armorZone?.ArmorThickness ?? 0f,
        hit.point.y > 0,
        armorZone?.CompartmentName ?? "Hull"
    );

    // Apply damage
    if (result.damageDealt > 0 && netId != null)
    {
        ApplyDamage(netId.netId, result);
    }

    // Create visual effects
    RpcCreateHitEffect(hit.point, hit.normal, result.didPenetrate);

    projectile.hasDetonated = true;
}
```

---

## ArmorZone Component

Attached to ship colliders to define armor properties:

```csharp
public class ArmorZone : MonoBehaviour
{
    [SerializeField] private float armorThickness = 100f;   // mm
    [SerializeField] private string compartmentName = "Hull";
    [SerializeField] private bool isVital = false;          // Magazine, engine, etc.

    public float ArmorThickness => armorThickness;
    public string CompartmentName => compartmentName;
    public bool IsVital => isVital;
}
```

---

## Client RPCs

```csharp
[ClientRpc] void RpcSpawnProjectileVisual(uint id, Vector3 pos, Vector3 dir, int caliber);
[ClientRpc] void RpcSpawnTorpedoVisual(uint id, Vector3 pos, Vector3 dir);
[ClientRpc] void RpcDestroyProjectileVisual(uint id);
[ClientRpc] void RpcCreateHitEffect(Vector3 pos, Vector3 normal, bool penetrated);
[ClientRpc] void RpcCreateWaterSplash(Vector3 pos, GunCaliber caliber);
```

---

## Object Pooling

```csharp
private Queue<ProjectileData> projectilePool = new Queue<ProjectileData>();

private ProjectileData GetPooledProjectile()
{
    if (projectilePool.Count > 0)
        return projectilePool.Dequeue();
    return new ProjectileData();
}

private void ReturnToPool(ProjectileData projectile)
{
    projectile.hasDetonated = true;
    projectilePool.Enqueue(projectile);
}
```

---

## Integration Points

### Dependencies
- **Mirror** - NetworkBehaviour, ClientRpc
- [[BallisticsCalculator]] - Hit calculations
- [[WeaponData]] - ProjectileData structure

### Used By
- [[WeaponController]] - Requests projectile spawning
- **DamageController** - Receives damage results

---

## Example Usage

### Spawning from WeaponController
```csharp
// Server-side firing
ProjectileData shell = ProjectileManager.Instance.SpawnProjectile(
    netId,
    mountIndex,
    muzzlePosition,
    aimDirection,
    shellProfile,
    AmmunitionType.AP
);
```

### Listening to Events
```csharp
void Start()
{
    ProjectileManager.Instance.OnProjectileHit += HandleHit;
}

void HandleHit(ProjectileData projectile, HitResult result)
{
    if (result.didPenetrate)
    {
        Debug.Log($"Hit for {result.damageDealt} damage!");
    }
}
```

---

## Related Files
- [[WeaponController]] - Triggers projectile spawning
- [[BallisticsCalculator]] - Hit calculation math
- [[WeaponData]] - ProjectileData structure
- [[BallisticsData]] - HitResult structure

---

## Testing Notes
- Max 500 active projectiles (pooled)
- 30 second max lifetime
- Water hit at y=0
- Gizmos available for trajectory debugging

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added object pooling
- **2025-01**: Added ArmorZone component
