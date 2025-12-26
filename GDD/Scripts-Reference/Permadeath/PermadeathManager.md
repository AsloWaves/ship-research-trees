# PermadeathManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Permadeath/Controllers/PermadeathManager.cs` |
| **Namespace** | `WOS.Permadeath.Controllers` |
| **Inheritance** | `NetworkBehaviour` |
| **Pattern** | Singleton |
| **Lines** | ~783 |
| **Architecture** | Server-authoritative death penalty, insurance, and salvage management |

## Purpose
Central manager for the permadeath system handling death processing, insurance claims, salvage operations, and respawn mechanics. Calculates death penalties based on risk zones and ship tiers, manages insurance policies, and creates salvageable wrecks.

---

## Class Diagram

```
PermadeathManager (NetworkBehaviour, Singleton)
├── Death Processing
│   ├── ProcessDeath()
│   ├── GetZoneRiskLevel()
│   ├── GetRiskConfig()
│   └── GetTierPenalty()
├── Insurance System
│   ├── CmdPurchaseInsurance()
│   ├── ProcessInsuranceClaim()
│   ├── GetInsuranceConfig()
│   └── GetInsurancePolicy()
├── Salvage System
│   ├── CreateSalvageableWreck()
│   ├── CmdStartSalvage()
│   ├── ProcessSalvageOperation()
│   ├── CompleteSalvage()
│   └── UpdateWreckDecay()
├── Respawn System
│   ├── CanRespawn()
│   ├── GetRespawnCooldown()
│   ├── CmdRequestRespawn()
│   └── UpdateRespawnCooldowns()
└── Statistics
    ├── UpdateDeathStats()
    └── GetPlayerStats()
```

---

## Configuration

### Death Penalty Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `tierPenalties` | List | Per-tier death penalty configurations |
| `riskConfigs` | List | Per-risk-zone configurations |

### Insurance Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `insuranceConfigs` | List | Per-tier insurance configurations |
| `insuranceProcessingTime` | 10s | Time to process claims |

### Salvage Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `defaultSalvageWindow` | 300s (5 min) | Time wrecks remain salvageable |
| `salvageOperationTime` | 60s | Time to complete salvage |
| `salvageDecayRate` | 0.01 | Value decay rate per second |

### Respawn Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `baseRespawnCooldown` | 30s | Base time before respawn |
| `defaultRespawnZoneId` | "safe_harbor" | Default respawn location |

---

## Events

| Event | Signature | Trigger |
|-------|-----------|---------|
| `OnPlayerDied` | `Action<DeathPenalty>` | Player death processed |
| `OnInsuranceClaimProcessed` | `Action<InsuranceClaim>` | Insurance claim resolved |
| `OnWreckCreated` | `Action<SalvageableWreck>` | New salvageable wreck |
| `OnSalvageComplete` | `Action<string, SalvageResult>` | Salvage operation done |
| `OnPlayerRespawnReady` | `Action<string>` | Player can respawn |

---

## Death Processing

### Main Death Flow
```csharp
[Server]
public DeathPenalty ProcessDeath(string playerId, string shipId,
                                  DeathType deathType, string zoneId)
{
    // Get zone risk level and configs
    RiskZone riskLevel = GetZoneRiskLevel(zoneId);
    var riskConfig = GetRiskConfig(riskLevel);
    var tierPenalty = GetTierPenalty(GetShipTier(shipId));

    var penalty = new DeathPenalty { ... };

    // Calculate ship loss
    penalty.shipDestroyed = Random.value <
        tierPenalty.shipLossChance * riskConfig.deathPenaltyMultiplier;

    if (penalty.shipDestroyed)
    {
        penalty.shipValueLost = GetShipValue(shipId);

        // Process insurance claim
        if (activePolicies.TryGetValue(shipId, out var policy))
            penalty.insurancePayout = ProcessInsuranceClaim(policy, penalty);

        // Create salvageable wreck
        if (tierPenalty.allowsSalvage && riskConfig.allowsSalvage)
        {
            var wreck = CreateSalvageableWreck(playerId, shipId, zoneId);
            penalty.canSalvage = true;
            penalty.salvageLocationId = wreck.wreckId;
        }
    }

    // Calculate cargo loss
    float cargoLossPercent = tierPenalty.cargoLossPercent *
                             riskConfig.cargoLossMultiplier;
    penalty.lostCargo = CalculateCargoLoss(playerId, cargoLossPercent);

    // Calculate crew loss
    if (Random.value < tierPenalty.crewLossChance)
        penalty.lostCrewIds = CalculateCrewLoss(playerId, shipId);

    // Calculate currency penalty
    penalty.currencyLost = GetPlayerCurrency(playerId) *
        tierPenalty.currencyPenaltyPercent * riskConfig.currencyLossMultiplier;

    // Set respawn cooldown
    float cooldown = baseRespawnCooldown * tierPenalty.respawnCooldown *
                     riskConfig.respawnCooldownMultiplier;
    respawnCooldowns[playerId] = Time.time + cooldown;

    return penalty;
}
```

### Death Penalty Calculation
```
Ship Loss Chance = tierPenalty.shipLossChance × riskConfig.deathPenaltyMultiplier
Cargo Loss = tierPenalty.cargoLossPercent × riskConfig.cargoLossMultiplier
Currency Loss = playerCurrency × tierPenalty.currencyPenaltyPercent × riskConfig.currencyLossMultiplier
Respawn Cooldown = base × tierMultiplier × riskMultiplier
```

---

## Insurance System

### Purchasing Insurance
```csharp
[Command(requiresAuthority = false)]
public void CmdPurchaseInsurance(string shipId, InsuranceTier tier,
                                  NetworkConnectionToClient sender = null)
{
    var config = GetInsuranceConfig(tier);
    float shipValue = GetShipValue(shipId);
    float premium = shipValue * config.premiumMultiplier;

    // TODO: Check affordability and deduct premium

    var policy = new InsurancePolicy
    {
        policyId = Guid.NewGuid().ToString(),
        playerId = playerId,
        shipId = shipId,
        tier = tier,
        coveragePercent = config.hullCoverage,
        maxPayout = shipValue * config.hullCoverage,
        deductible = shipValue * config.deductiblePercent,
        premiumCost = premium,
        expirationTime = Time.time + 86400f,  // 24 hours
        claimsRemaining = config.claimsPerPolicy
    };

    activePolicies[shipId] = policy;
}
```

### Processing Claims
```csharp
[Server]
private float ProcessInsuranceClaim(InsurancePolicy policy, DeathPenalty penalty)
{
    var claim = new InsuranceClaim { ... };

    // Check exclusions
    if (policy.excludedDeathTypes.Contains(penalty.deathType))
    {
        claim.isApproved = false;
        claim.denialReason = "Death type excluded from coverage";
        return 0f;
    }

    if (policy.claimsRemaining <= 0)
    {
        claim.isApproved = false;
        claim.denialReason = "No claims remaining";
        return 0f;
    }

    // Calculate payout
    float basePayout = penalty.shipValueLost * policy.coveragePercent;
    float payout = Mathf.Min(basePayout, policy.maxPayout);
    payout = Mathf.Max(0, payout - policy.deductible);

    claim.approvedAmount = payout;
    claim.isApproved = true;
    policy.claimsRemaining--;

    return payout;
}
```

---

## Salvage System

### Wreck Creation
```csharp
[Server]
private SalvageableWreck CreateSalvageableWreck(string playerId,
                                                 string shipId, string zoneId)
{
    var wreck = new SalvageableWreck
    {
        wreckId = Guid.NewGuid().ToString(),
        originalShipId = shipId,
        originalPlayerId = playerId,
        zoneId = zoneId,
        position = GetShipPosition(shipId),
        creationTime = Time.time,
        expirationTime = Time.time + defaultSalvageWindow  // 5 minutes
    };

    wreck.salvageItems = GenerateSalvageItems(shipId);
    wreck.totalSalvageValue = CalculateSalvageValue(wreck.salvageItems);

    activeWrecks[wreck.wreckId] = wreck;
    return wreck;
}
```

### Salvage Operation
```csharp
[Command(requiresAuthority = false)]
public void CmdStartSalvage(string wreckId, NetworkConnectionToClient sender = null)
{
    // Validate wreck exists, not already being salvaged, not expired

    wreck.isBeingSalvaged = true;
    wreck.salvagingPlayerId = playerId;

    StartCoroutine(ProcessSalvageOperation(wreckId, playerId));
}

private IEnumerator ProcessSalvageOperation(string wreckId, string playerId)
{
    float startTime = Time.time;

    while (Time.time - startTime < salvageOperationTime)  // 60 seconds
    {
        wreck.salvageProgress = (Time.time - startTime) / salvageOperationTime;
        yield return null;
    }

    CompleteSalvage(wreckId, playerId);
}

[Server]
private void CompleteSalvage(string wreckId, string playerId)
{
    var result = new SalvageResult { ... };

    // Determine which items are recovered (RNG per item)
    foreach (var item in wreck.salvageItems)
    {
        if (Random.value < item.salvageChance)
        {
            item.isRecovered = true;
            result.recoveredItems.Add(item);
            result.totalValueRecovered +=
                item.baseValue * GetQualityMultiplier(item.quality);
        }
    }

    activeWrecks.Remove(wreckId);
}
```

### Quality Multipliers
```csharp
private float GetQualityMultiplier(SalvageQuality quality)
{
    return quality switch
    {
        SalvageQuality.Debris => 0.1f,
        SalvageQuality.Damaged => 0.5f,
        SalvageQuality.Recovered => 1f,
        SalvageQuality.Pristine => 1.5f,
        _ => 1f
    };
}
```

### Wreck Decay
```csharp
[Server]
private void UpdateWreckDecay()
{
    foreach (var kvp in activeWrecks)
    {
        var wreck = kvp.Value;

        // Check expiration
        if (Time.time > wreck.expirationTime)
        {
            expiredWrecks.Add(kvp.Key);
            continue;
        }

        // Decay salvage value over time
        wreck.totalSalvageValue *= (1f - salvageDecayRate * Time.deltaTime);
    }
}
```

---

## Respawn System

```csharp
public bool CanRespawn(string playerId)
{
    if (!respawnCooldowns.TryGetValue(playerId, out float cooldown))
        return true;
    return Time.time >= cooldown;
}

public float GetRespawnCooldown(string playerId)
{
    if (!respawnCooldowns.TryGetValue(playerId, out float cooldown))
        return 0f;
    return Mathf.Max(0, cooldown - Time.time);
}

[Command(requiresAuthority = false)]
public void CmdRequestRespawn(string preferredZoneId,
                               NetworkConnectionToClient sender = null)
{
    if (!CanRespawn(playerId))
    {
        float remaining = GetRespawnCooldown(playerId);
        RpcNotifyRespawnDenied(sender.connectionId, $"Respawn cooldown: {remaining:F0}s");
        return;
    }

    string respawnZone = string.IsNullOrEmpty(preferredZoneId)
        ? defaultRespawnZoneId
        : preferredZoneId;

    respawnCooldowns.Remove(playerId);
    OnPlayerRespawnReady?.Invoke(playerId);
}
```

---

## Statistics Tracking

```csharp
[Server]
private void UpdateDeathStats(string playerId, DeathPenalty penalty)
{
    if (!playerStats.TryGetValue(playerId, out var stats))
    {
        stats = new PlayerDeathStats { playerId = playerId };
        playerStats[playerId] = stats;
    }

    stats.totalDeaths++;

    switch (penalty.deathType)
    {
        case DeathType.Combat: stats.combatDeaths++; break;
        case DeathType.Environmental: stats.environmentalDeaths++; break;
        case DeathType.Extraction: stats.extractionDeaths++; break;
    }

    if (penalty.shipDestroyed) stats.shipsLost++;

    stats.crewLost += penalty.crewCasualties;
    stats.totalValueLost += penalty.shipValueLost +
                            penalty.cargoValueLost +
                            penalty.currencyLost;

    if (penalty.insurancePayout > 0)
    {
        stats.insuranceClaimsPaid++;
        stats.totalInsuranceReceived += penalty.insurancePayout;
    }
}
```

---

## Network RPCs

### Broadcast RPCs
| RPC | Purpose |
|-----|---------|
| `RpcNotifyPlayerDeath` | Announce death (playerId, shipDestroyed, cooldown) |
| `RpcNotifyWreckCreated` | Spawn wreck visual (wreckId, position, expiration) |
| `RpcNotifyWreckExpired` | Remove wreck visual |
| `RpcNotifySalvageStarted` | Show salvage progress |
| `RpcNotifySalvageComplete` | Show salvage rewards |

### Targeted RPCs
| RPC | Purpose |
|-----|---------|
| `RpcNotifyInsuranceDenied` | Insurance purchase denied |
| `RpcNotifyInsurancePurchased` | Insurance purchase confirmed |
| `RpcNotifySalvageDenied` | Salvage request denied |
| `RpcNotifyRespawnDenied` | Respawn request denied |
| `RpcNotifyRespawnReady` | Trigger respawn UI |

---

## Public API

```csharp
// Insurance
public InsurancePolicy GetInsurancePolicy(string shipId)

// Salvage
public List<SalvageableWreck> GetActiveWrecks()
public SalvageableWreck GetWreck(string wreckId)

// Respawn
public bool CanRespawn(string playerId)
public float GetRespawnCooldown(string playerId)

// Statistics
public PlayerDeathStats GetPlayerStats(string playerId)
```

---

## Usage Example

```csharp
// Process player death
var penalty = PermadeathManager.Instance.ProcessDeath(
    playerId: "player_001",
    shipId: "destroyer_mk2",
    deathType: DeathType.Combat,
    zoneId: "high_risk_zone"
);

if (penalty.shipDestroyed)
{
    Debug.Log($"Ship lost! Value: {penalty.shipValueLost}");

    if (penalty.insurancePayout > 0)
        Debug.Log($"Insurance payout: {penalty.insurancePayout}");

    if (penalty.canSalvage)
        Debug.Log($"Wreck available at: {penalty.salvageLocationId}");
}

// Check respawn
if (PermadeathManager.Instance.CanRespawn(playerId))
    PermadeathManager.Instance.CmdRequestRespawn("safe_harbor");

// View stats
var stats = PermadeathManager.Instance.GetPlayerStats(playerId);
Debug.Log($"Total deaths: {stats.totalDeaths}, Ships lost: {stats.shipsLost}");
```

---

## Integration Points

### Dependencies
- `WOS.Permadeath.Data` - Data structures
- `WOS.Debugging.DebugManager` - Logging
- `Mirror` - Networking

### Integrates With
- `ExtractionController` - Extraction death handling
- Zone system - Risk level queries
- Inventory system - Cargo/crew loss calculation
- Currency system - Insurance/penalties

---

## Design Notes

### Risk-Reward Philosophy
- Higher risk zones have higher penalties but better rewards
- Insurance provides safety net at premium cost
- Salvage allows partial recovery of losses

### Death Penalty Scaling
- Ship tier affects loss percentages
- Risk zone multiplies all penalties
- Multiple factors combine for final penalty

### Salvage Economy
- Wrecks decay over time (value decreases)
- Limited salvage window (5 minutes default)
- Quality affects recovered value (0.1x to 1.5x)
- Creates player-driven content (wreck hunting)

### Insurance Mechanics
- Premium based on ship value
- Limited claims per policy
- Death type exclusions possible
- Coverage percentage varies by tier

### Future Improvements (TODOs)
- Zone risk level queries
- Cargo/crew loss calculation
- Integration with currency system
- Respawn zone validation
