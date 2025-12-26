# ResearchManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Research/ResearchManager.cs` |
| **Namespace** | `WOS.Research` |
| **Inheritance** | `NetworkBehaviour` |
| **Lines** | ~449 |
| **Architecture** | Server-authoritative research system |

## Purpose
Server-authoritative manager for all research operations. Handles starting, completing, canceling research. Validates costs, prerequisites, and slots. Syncs research progress to clients.

---

## Dependencies

```csharp
[SerializeField] private ResearchDatabaseSO researchDatabase;
private Dictionary<string, PlayerResearchState> playerStates;
```

---

## Player Research State

```csharp
[System.Serializable]
public class PlayerResearchState
{
    public string playerId;
    public HashSet<string> completedResearch;
    public List<ActiveResearch> activeResearch;
    public int freeXP;
    public bool isPremium;
    public Dictionary<ResearchNation, int> nationTiers;
}

[System.Serializable]
public class ActiveResearch
{
    public string nodeId;
    public int xpProgress;
    public float startTime;
    public bool isPaused;
}
```

---

## Server Commands

### Start Research
```csharp
[Command]
public void CmdStartResearch(string playerId, string nodeId, bool useFreeXP = false)
{
    // Validate node exists
    ResearchNodeSO node = researchDatabase.FindNode(nodeId);
    if (node == null)
    {
        TargetResearchError(connectionToClient, "Invalid research node");
        return;
    }

    // Get player state
    var state = GetPlayerState(playerId);

    // Check slot availability
    if (!researchDatabase.HasAvailableSlot(state.activeResearch.Count, state.isPremium))
    {
        TargetResearchError(connectionToClient, "No research slots available");
        return;
    }

    // Check prerequisites
    if (!node.ArePrerequisitesMet(state.completedResearch))
    {
        TargetResearchError(connectionToClient, "Prerequisites not met");
        return;
    }

    // Check tier
    int playerTier = GetPlayerTier(playerId, node.nation);
    if (!node.MeetsTierRequirement(playerTier))
    {
        TargetResearchError(connectionToClient, "Tier requirement not met");
        return;
    }

    // Check costs
    int xpCost = researchDatabase.GetAdjustedXPCost(node);
    int creditCost = researchDatabase.GetAdjustedCreditCost(node);

    if (!DeductCosts(playerId, creditCost))
    {
        TargetResearchError(connectionToClient, "Insufficient credits");
        return;
    }

    // Start research
    var activeResearch = new ActiveResearch
    {
        nodeId = nodeId,
        xpProgress = 0,
        startTime = Time.time,
        isPaused = false
    };

    state.activeResearch.Add(activeResearch);

    // Notify client
    TargetResearchStarted(connectionToClient, nodeId);

    DebugManager.Log($"Research started: {nodeId} for {playerId}", "Research");
}
```

### Complete Research
```csharp
[Command]
public void CmdCompleteResearch(string playerId, string nodeId)
{
    var state = GetPlayerState(playerId);
    var active = state.activeResearch.FirstOrDefault(r => r.nodeId == nodeId);

    if (active == null)
    {
        TargetResearchError(connectionToClient, "Research not active");
        return;
    }

    ResearchNodeSO node = researchDatabase.FindNode(nodeId);
    int requiredXP = researchDatabase.GetAdjustedXPCost(node);

    // Check if XP requirement met
    if (active.xpProgress < requiredXP)
    {
        TargetResearchError(connectionToClient, "Research not complete");
        return;
    }

    // Complete research
    state.activeResearch.Remove(active);
    state.completedResearch.Add(nodeId);

    // Grant Free XP
    int freeXPEarned = researchDatabase.CalculateFreeXPEarned(requiredXP);
    state.freeXP += freeXPEarned;

    // Grant unlocks
    GrantUnlocks(playerId, node);

    // Update tier
    UpdatePlayerTier(playerId, node.nation);

    // Notify client
    TargetResearchCompleted(connectionToClient, nodeId, freeXPEarned);

    DebugManager.Log($"Research completed: {nodeId} for {playerId}", "Research");
}
```

### Instant Complete (Premium)
```csharp
[Command]
public void CmdInstantCompleteResearch(string playerId, string nodeId)
{
    var state = GetPlayerState(playerId);
    var active = state.activeResearch.FirstOrDefault(r => r.nodeId == nodeId);

    if (active == null)
    {
        TargetResearchError(connectionToClient, "Research not active");
        return;
    }

    ResearchNodeSO node = researchDatabase.FindNode(nodeId);

    // Check if instant complete allowed
    if (!researchDatabase.allowInstantResearch || !node.allowInstantComplete)
    {
        TargetResearchError(connectionToClient, "Instant complete not available");
        return;
    }

    // Calculate and deduct premium currency cost
    int cost = researchDatabase.GetInstantCompleteCost(node);
    if (!DeductPremiumCurrency(playerId, cost))
    {
        TargetResearchError(connectionToClient, "Insufficient premium currency");
        return;
    }

    // Complete instantly
    active.xpProgress = researchDatabase.GetAdjustedXPCost(node);
    CmdCompleteResearch(playerId, nodeId);
}
```

### Cancel Research
```csharp
[Command]
public void CmdCancelResearch(string playerId, string nodeId)
{
    var state = GetPlayerState(playerId);
    var active = state.activeResearch.FirstOrDefault(r => r.nodeId == nodeId);

    if (active == null)
    {
        TargetResearchError(connectionToClient, "Research not active");
        return;
    }

    // Remove from active
    state.activeResearch.Remove(active);

    // Partial credit refund (50%)
    ResearchNodeSO node = researchDatabase.FindNode(nodeId);
    int refund = researchDatabase.GetAdjustedCreditCost(node) / 2;
    GrantCredits(playerId, refund);

    // Notify client
    TargetResearchCanceled(connectionToClient, nodeId, refund);

    DebugManager.Log($"Research canceled: {nodeId} for {playerId}", "Research");
}
```

---

## XP Progress

```csharp
[Server]
public void AddResearchXP(string playerId, string nodeId, int xpAmount)
{
    var state = GetPlayerState(playerId);
    var active = state.activeResearch.FirstOrDefault(r => r.nodeId == nodeId);

    if (active == null || active.isPaused) return;

    ResearchNodeSO node = researchDatabase.FindNode(nodeId);
    int requiredXP = researchDatabase.GetAdjustedXPCost(node);

    active.xpProgress = Mathf.Min(active.xpProgress + xpAmount, requiredXP);

    // Sync progress to client
    TargetResearchProgress(connectionToClient, nodeId, active.xpProgress, requiredXP);

    // Auto-complete if ready
    if (active.xpProgress >= requiredXP)
    {
        TargetResearchReady(connectionToClient, nodeId);
    }
}

[Server]
public void AddBattleXP(string playerId, int xpAmount, ResearchNation nation)
{
    var state = GetPlayerState(playerId);

    // Distribute to active research of matching nation
    var nationResearch = state.activeResearch
        .Where(r => researchDatabase.FindNode(r.nodeId)?.nation == nation)
        .ToList();

    if (nationResearch.Count == 0) return;

    int xpPerResearch = xpAmount / nationResearch.Count;

    foreach (var research in nationResearch)
    {
        AddResearchXP(playerId, research.nodeId, xpPerResearch);
    }
}
```

---

## Client RPCs

```csharp
[TargetRpc]
private void TargetResearchStarted(NetworkConnection target, string nodeId)

[TargetRpc]
private void TargetResearchProgress(NetworkConnection target, string nodeId, int current, int required)

[TargetRpc]
private void TargetResearchReady(NetworkConnection target, string nodeId)

[TargetRpc]
private void TargetResearchCompleted(NetworkConnection target, string nodeId, int freeXPEarned)

[TargetRpc]
private void TargetResearchCanceled(NetworkConnection target, string nodeId, int refund)

[TargetRpc]
private void TargetResearchError(NetworkConnection target, string message)
```

---

## Unlock Granting

```csharp
[Server]
private void GrantUnlocks(string playerId, ResearchNodeSO node)
{
    switch (node.unlockType)
    {
        case UnlockType.Ship:
            PlayFabShipService.UnlockShip(playerId, node.unlockId);
            break;
        case UnlockType.Turret:
            PlayFabInventoryService.UnlockTurret(playerId, node.unlockId);
            break;
        case UnlockType.Module:
            PlayFabInventoryService.UnlockModule(playerId, node.unlockId);
            break;
        case UnlockType.Ability:
            PlayFabInventoryService.UnlockAbility(playerId, node.abilityId);
            break;
        case UnlockType.Bundle:
            foreach (var unlock in node.additionalUnlocks)
            {
                PlayFabInventoryService.UnlockItem(playerId, unlock);
            }
            break;
    }
}
```

---

## Usage Example

```csharp
// Client requests research start
researchManager.CmdStartResearch(myPlayerId, "us_destroyer_mk2");

// Server adds XP from battle
researchManager.AddBattleXP(playerId, battleXPEarned, ResearchNation.USA);

// Client requests completion
researchManager.CmdCompleteResearch(myPlayerId, "us_destroyer_mk2");

// Premium instant complete
researchManager.CmdInstantCompleteResearch(myPlayerId, "us_battleship_mk3");
```

---

## Integration Points

### Dependencies
- `ResearchDatabaseSO` - Configuration
- `PlayFabInventoryService` - Grant unlocks
- `PlayFabShipService` - Unlock ships
- `WOS.Debugging.DebugManager` - Logging
- Mirror networking

### Events
```csharp
public static event Action<string, string> OnResearchStarted;
public static event Action<string, string> OnResearchCompleted;
public static event Action<string, string, int, int> OnResearchProgress;
```

---

## Design Notes

### Server Authority
- All validation server-side
- Clients only request operations
- Prevents XP/cost manipulation

### Research Slots
- Base 3 slots for free players
- Premium adds 2 more slots
- Encourages parallel research

### XP Distribution
- Battle XP splits among active research
- Nation-specific XP routing
- Encourages playing ships you're researching

### Cancellation Policy
- 50% credit refund on cancel
- No XP refund
- Discourages frivolous cancellation
