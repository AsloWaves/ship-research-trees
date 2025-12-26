---
tags: [script, economy, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Economy.Controllers
file-path: Assets/Scripts/Economy/Controllers/ContractManager.cs
status: IMPLEMENTED
size: ~476 lines
feature-group: economy
---

# ContractManager.cs

## Quick Reference
**Type**: NetworkBehaviour (Singleton)
**Namespace**: WOS.Economy.Controllers
**File**: `Assets/Scripts/Economy/Controllers/ContractManager.cs`
**Size**: ~476 lines
**Dependencies**: EconomyData, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative contract/mission management. Handles contract assignment, progress tracking, objective completion, rewards calculation, and zone-based availability. Based on GDD Contract-System.md specifications.

---

## Singleton Access

```csharp
private static ContractManager _instance;
public static ContractManager Instance => _instance;
```

---

## Configuration

```csharp
[Header("Contract Configuration")]
[SerializeField] private int maxActiveContractsPerPlayer = 5;
[SerializeField] private float contractRefreshInterval = 3600f;  // 1 hour
[SerializeField] private int availableContractsPerZone = 10;

[Header("Rewards")]
[SerializeField] private float bonusRewardMultiplier = 1.5f;
[SerializeField] private float difficultyRewardMultiplier = 0.25f;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Events

```csharp
public event Action<ActiveContract> OnContractAccepted;
public event Action<ActiveContract> OnContractCompleted;
public event Action<ActiveContract> OnContractFailed;
public event Action<ActiveContract, ContractObjective> OnObjectiveProgress;
public event Action<string> OnContractsRefreshed;      // Zone ID
```

---

## Contract Acceptance

```csharp
[Command(requiresAuthority = false)]
public void CmdAcceptContract(string contractId, NetworkConnectionToClient sender = null)
{
    // Check active contract limit
    if (playerActiveCount >= maxActiveContractsPerPlayer) return;

    // Find contract template
    if (!contractTemplates.TryGetValue(contractId, out var template)) return;

    // TODO: Check tier requirement, reputation, cooldown

    // Create active contract instance
    var activeContract = new ActiveContract
    {
        instanceId = Guid.NewGuid().ToString(),
        contractId = contractId,
        playerId = playerId,
        state = ContractState.Active,
        acceptedTime = DateTime.UtcNow,
        expirationTime = template.timeLimit > 0
            ? DateTime.UtcNow.AddSeconds(template.timeLimit)
            : DateTime.MaxValue
    };

    // Clone objectives
    foreach (var obj in template.objectives)
    {
        activeContract.objectives.Add(new ContractObjective
        {
            objectiveId = obj.objectiveId,
            description = obj.description,
            objectiveType = obj.objectiveType,
            targetId = obj.targetId,
            requiredCount = obj.requiredCount,
            currentCount = 0,
            isOptional = obj.isOptional
        });
    }

    activeContracts.Add(activeContract);
    OnContractAccepted?.Invoke(activeContract);
}
```

---

## Objective Progress

### Report Progress

```csharp
[Server]
public void ReportObjectiveProgress(string playerId, ObjectiveType objectiveType,
    string targetId, int count)
{
    foreach (var contract in activeContracts)
    {
        if (contract.playerId != playerId || contract.state != ContractState.Active)
            continue;

        foreach (var objective in contract.objectives)
        {
            if (objective.objectiveType != objectiveType)
                continue;

            if (!string.IsNullOrEmpty(objective.targetId) &&
                objective.targetId != targetId)
                continue;

            objective.currentCount += count;
            objective.currentCount = Mathf.Min(objective.currentCount, objective.requiredCount);

            OnObjectiveProgress?.Invoke(contract, objective);
        }

        // Check if contract is complete
        CheckContractCompletion(contract);
    }
}
```

### Check Completion

```csharp
[Server]
private void CheckContractCompletion(ActiveContract contract)
{
    // Check required objectives (non-optional)
    foreach (var objective in contract.objectives)
    {
        if (!objective.isOptional && !objective.isComplete)
            return; // Not complete
    }

    // Contract complete!
    contract.state = ContractState.Completed;
    contract.completedTime = DateTime.UtcNow;
    contract.wasSuccessful = true;

    CalculateAndAwardRewards(contract, template);
    OnContractCompleted?.Invoke(contract);
}
```

---

## Reward Calculation

```csharp
[Server]
private void CalculateAndAwardRewards(ActiveContract contract, ContractData template)
{
    // Difficulty multiplier: 1.0 + (difficultyLevel * 0.25)
    float difficultyMultiplier = 1f + ((int)template.difficulty * difficultyRewardMultiplier);

    // Base rewards (with probability check)
    foreach (var reward in template.rewards)
    {
        if (UnityEngine.Random.value <= reward.chance)
        {
            var earnedReward = new ContractReward
            {
                rewardType = reward.rewardType,
                rewardId = reward.rewardId,
                quantity = Mathf.RoundToInt(reward.quantity * difficultyMultiplier)
            };
            contract.earnedRewards.Add(earnedReward);
            // TODO: Grant reward to player
        }
    }

    // Bonus rewards from optional objectives (1.5x multiplier)
    foreach (var objective in contract.objectives)
    {
        if (objective.isOptional && objective.isComplete)
        {
            foreach (var bonus in objective.bonusRewards)
            {
                if (UnityEngine.Random.value <= bonus.chance)
                {
                    var earnedBonus = new ContractReward
                    {
                        rewardType = bonus.rewardType,
                        rewardId = bonus.rewardId,
                        quantity = Mathf.RoundToInt(bonus.quantity * bonusRewardMultiplier)
                    };
                    contract.earnedRewards.Add(earnedBonus);
                }
            }
        }
    }
}
```

---

## Difficulty Multipliers

| Difficulty | Base Multiplier |
|------------|-----------------|
| Routine (0) | 1.00x |
| Standard (1) | 1.25x |
| Hazardous (2) | 1.50x |
| Dangerous (3) | 1.75x |
| Extreme (4) | 2.00x |

---

## Contract Expiration

```csharp
[Server]
private void UpdateActiveContracts(float deltaTime)
{
    DateTime now = DateTime.UtcNow;

    foreach (var contract in activeContracts)
    {
        if (contract.state != ContractState.Active) continue;

        // Update time remaining
        contract.timeRemaining = (float)(contract.expirationTime - now).TotalSeconds;

        // Check expiration
        if (contract.expirationTime < now)
        {
            contract.state = ContractState.Expired;
            contract.wasSuccessful = false;
            OnContractFailed?.Invoke(contract);
        }
    }
}
```

---

## Zone Contracts

```csharp
[Server]
public void RefreshZoneContracts(string zoneId)
{
    // Generate new available contracts based on zone and difficulty
    OnContractsRefreshed?.Invoke(zoneId);
}
```

---

## Public API

```csharp
public List<ContractData> GetAvailableContracts(string zoneId);
public List<ActiveContract> GetPlayerActiveContracts(string playerId);
public ActiveContract GetActiveContract(string instanceId);
public int GetMaxActiveContracts();
```

---

## Client RPCs

```csharp
[ClientRpc] private void RpcNotifyContractAccepted(string playerId, string instanceId, string contractId);
[ClientRpc] private void RpcNotifyContractAbandoned(string playerId, string instanceId);
[ClientRpc] private void RpcNotifyObjectiveProgress(string playerId, string instanceId, string objectiveId, int current, int required);
[ClientRpc] private void RpcNotifyContractCompleted(string playerId, string instanceId);
[ClientRpc] private void RpcNotifyContractExpired(string playerId, string instanceId);
```

---

## Integration Points

### Dependencies
- [[EconomyData]] - Data structures
- Mirror networking
- WOS.Debugging

### Used By
- Contract UI panels
- Combat system (objective progress)
- [[WalletManager]] - Currency rewards

---

## Related Files
- [[EconomyData]] - Data structures
- [[WalletManager]] - Currency rewards
- [[MarketController]] - Trade objectives

---

## Design Notes
- Server-authoritative with Singleton pattern
- Maximum 5 active contracts per player
- Contracts refresh hourly per zone
- 10 available contracts per zone
- Objectives cloned on acceptance
- Only required objectives needed for completion
- Optional objectives give 1.5x bonus rewards
- Difficulty scales rewards by 0.25x per tier
- Time limit 0 means no expiration
- Rewards have probability (chance 0-1)
- Abandoned contracts marked as failed
- Progress updates check all matching objectives

