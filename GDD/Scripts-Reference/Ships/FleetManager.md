---
tags: [script, ships, manager, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Ships.Controllers
file-path: Assets/Scripts/Ships/Controllers/FleetManager.cs
status: IMPLEMENTED
size: ~592 lines
feature-group: ships
---

# FleetManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Ships.Controllers
**File**: `Assets/Scripts/Ships/Controllers/FleetManager.cs`
**Size**: ~592 lines
**Dependencies**: ShipDefinitionSO, ShipProgressionData, Mirror

---

## Purpose
Server-authoritative fleet and ship progression management. Handles ship unlocking, purchasing, fleet composition, permadeath with insurance, repair, and tech tree research. Based on GDD Ship-Progression.md and Tiers.md.

---

## Configuration

```csharp
[Header("Fleet Configuration")]
[SerializeField] private int baseFleetSlots = 5;
[SerializeField] private int maxFleetSlots = 20;
[SerializeField] private int slotsPerLevel = 1;

[Header("Starter Ships")]
[SerializeField] private List<string> starterShipIds;
[SerializeField] private ShipNation defaultNation = ShipNation.International;

[Header("Permadeath Settings")]
[SerializeField] private bool enablePermadeath = true;
[SerializeField] private float insuranceRefundPercent = 50f;
```

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnFleetChanged))]
private PlayerFleet playerFleet;
```

---

## Events

```csharp
public event Action<ShipInstanceData> OnShipUnlocked;
public event Action<ShipInstanceData> OnShipPurchased;
public event Action<ShipInstanceData> OnShipLost;
public event Action<string> OnActiveShipChanged;
public event Action<PlayerFleet> OnFleetUpdated;
```

---

## Initialization

### Server Start

```csharp
[Server]
private void LoadShipDefinitions()
{
    var definitions = Resources.LoadAll<ShipDefinitionSO>("Ships");
    foreach (var def in definitions)
    {
        shipDefinitions[def.shipDefinitionId] = def;
    }
}
```

### Fleet Initialization

```csharp
[Server]
public void InitializeFleet(string playerId)
{
    playerFleet = new PlayerFleet
    {
        playerId = playerId,
        maxShips = baseFleetSlots
    };

    // Grant starter ships
    foreach (var shipId in starterShipIds)
    {
        GrantShip(shipId, "Starter ship");
    }
}
```

---

## Ship Unlocking & Purchase

```csharp
public bool CanUnlockShip(string shipDefinitionId)
{
    // Check prerequisites
    // Check player level
    // Check faction reputation
}

[Command]
public void CmdUnlockShip(string shipDefinitionId);

[Command]
public void CmdPurchaseShip(string shipDefinitionId, string customName);

[Server]
private void GrantShip(string shipDefinitionId, string reason, string customName = null);
```

---

## Ship Selection

```csharp
[Command]
public void CmdSetActiveShip(string shipInstanceId)
{
    var ship = playerFleet.GetShip(shipInstanceId);
    if (ship == null || ship.unlockStatus != ShipUnlockStatus.Owned) return;

    // Check condition (no wrecks)
    if (ship.condition == ShipCondition.Destroyed) return;

    // Deactivate previous, activate new
    ship.isActiveShip = true;
    playerFleet.activeShipId = shipInstanceId;

    RpcNotifyActiveShipChanged(shipInstanceId);
}
```

---

## Permadeath System

```csharp
[Server]
public void ProcessShipDestruction(string shipInstanceId)
{
    var ship = playerFleet.GetShip(shipInstanceId);
    ship.condition = ShipCondition.Destroyed;

    if (!enablePermadeath) return;

    // Calculate permadeath risk
    float risk = ship.GetPermadeathRisk();

    // Insurance reduces risk
    if (ship.hasInsurance)
    {
        float reduction = ship.insuranceLevel * 0.25f;
        risk *= (1f - reduction);
    }

    bool permanentLoss = Random.value < risk;

    if (permanentLoss)
    {
        ship.unlockStatus = ShipUnlockStatus.Lost;
        playerFleet.shipsLost++;

        // Insurance payout
        if (ship.hasInsurance)
        {
            float payout = insuranceRefundPercent + (ship.insuranceLevel * 10f);
            // Grant payout...
        }

        OnShipLost?.Invoke(ship);
    }
}
```

### Insurance Levels

| Level | Risk Reduction | Refund |
|-------|----------------|--------|
| 0 | 0% | 50% |
| 1 | 25% | 60% |
| 2 | 50% | 70% |
| 3 | 75% | 80% |

---

## Ship Repair

```csharp
[Command]
public void CmdRepairShip(string shipInstanceId)
{
    var ship = playerFleet.GetShip(shipInstanceId);

    // Calculate repair cost
    float damagePercent = 1f - (ship.currentHealth / ship.maxHealth);
    ship.repairCost = CalculateRepairCost(ship, damagePercent);

    // Deduct currency, restore health
    ship.currentHealth = ship.maxHealth;
    ship.condition = ShipCondition.Perfect;
}
```

---

## Insurance Purchase

```csharp
[Command]
public void CmdPurchaseInsurance(string shipInstanceId, int level)
{
    var ship = playerFleet.GetShip(shipInstanceId);
    level = Mathf.Clamp(level, 1, 3);

    ship.hasInsurance = true;
    ship.insuranceLevel = level;
    ship.insuranceExpiry = DateTime.UtcNow.AddDays(30);
}
```

---

## Public API

```csharp
public PlayerFleet GetFleet();
public ShipInstanceData GetActiveShip();
public ShipDefinitionSO GetShipDefinition(string definitionId);
public bool HasOwnedShip(string definitionId);
public List<ShipInstanceData> GetShipsByTier(ShipTier tier);
public List<ShipInstanceData> GetShipsByClass(ShipClass shipClass);
```

---

## Network Callbacks

```csharp
[ClientRpc] private void RpcNotifyShipAcquired(string instanceId, string definitionId);
[ClientRpc] private void RpcNotifyActiveShipChanged(string instanceId);
[ClientRpc] private void RpcNotifyShipLost(string instanceId, bool permanent);
[ClientRpc] private void RpcNotifyShipRepaired(string instanceId);
[ClientRpc] private void RpcNotifyInsurancePurchased(string instanceId, int level);
```

---

## Integration Points

### Dependencies
- [[ShipDefinitionSO]] - Ship definitions
- [[ShipProgressionData]] - Data structures
- Mirror networking

### Used By
- [[ShipSelectionPanel]] - Ship selection UI
- [[EquipmentPanel]] - Active ship equipment
- [[CombatController]] - Damage processing

---

## Related Files
- [[ShipDefinitionSO]] - Ship configuration
- [[ShipProgressionData]] - Data structures
- [[PlayerFleet]] - Fleet data

---

## Design Notes
- Server-authoritative with SyncVar
- Singleton pattern for global access
- Permadeath risk increases with tier
- Insurance mitigates risk and provides refund
- Starter ships granted on initialization
- Tech tree research placeholder

