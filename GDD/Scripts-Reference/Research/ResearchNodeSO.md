# ResearchNodeSO.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Research/ResearchNodeSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Research` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | ~332 |
| **Architecture** | Research tech tree node definition |

## Purpose
Defines individual research nodes in the tech tree. Contains research costs, prerequisites, unlock content, and tier progression. Used by ResearchTreeSO and ResearchManager for tech tree navigation and unlocking.

---

## Enums

### ResearchType
```csharp
public enum ResearchType
{
    Ship,
    Turret,
    Engine,
    Module,
    Crew,
    Airplane,
    Armament,
    Technology
}
```

### ResearchNation
```csharp
public enum ResearchNation
{
    USA,
    Japan,
    Britain,
    Germany,
    Russia,
    France,
    Italy,
    China,
    International
}
```

### UnlockType
```csharp
public enum UnlockType
{
    Ship,
    Turret,
    Engine,
    Module,
    Crew,
    Airplane,
    Armament,
    Technology,
    Ability,
    Bundle
}
```

---

## Configuration

| Setting | Type | Description |
|---------|------|-------------|
| `nodeId` | string | Unique identifier |
| `displayName` | string | UI display name |
| `description` | string | Research description |
| `icon` | Sprite | Node icon |
| `researchType` | ResearchType | Category of research |
| `nation` | ResearchNation | Nation affiliation |
| `tier` | int | Tech tree tier (1-10) |

---

## Cost Configuration

```csharp
[Header("Costs")]
public int xpCost;           // Research XP required
public int creditCost;       // Credits required
public float researchTime;   // Seconds to complete (if time-gated)

[Header("Premium Options")]
public int instantCompleteCost;  // Premium currency for instant
public bool allowInstantComplete = true;
```

---

## Prerequisites

```csharp
[Header("Prerequisites")]
public List<ResearchNodeSO> prerequisites;  // Required prior research
public int requiredTier;                     // Minimum tier required
public bool requiresAllPrerequisites = true; // AND vs OR logic
```

---

## Unlock Content

```csharp
[Header("Unlocks")]
public UnlockType unlockType;
public string unlockId;           // ID of item/ship/etc to unlock
public List<string> additionalUnlocks;  // Bonus unlocks
public bool grantsAbility;
public string abilityId;
```

---

## Public API

### Prerequisite Checks
```csharp
// Check if all prerequisites are met
public bool ArePrerequisitesMet(HashSet<string> completedResearch)
{
    if (prerequisites == null || prerequisites.Count == 0)
        return true;

    if (requiresAllPrerequisites)
    {
        return prerequisites.All(p => completedResearch.Contains(p.nodeId));
    }
    else
    {
        return prerequisites.Any(p => completedResearch.Contains(p.nodeId));
    }
}

// Check tier requirement
public bool MeetsTierRequirement(int playerTier)
{
    return playerTier >= requiredTier;
}
```

### Cost Calculations
```csharp
// Get adjusted XP cost (with multipliers)
public int GetAdjustedXPCost(float multiplier = 1.0f)
{
    return Mathf.RoundToInt(xpCost * multiplier);
}

// Check if player can afford
public bool CanAfford(int playerXP, int playerCredits)
{
    return playerXP >= xpCost && playerCredits >= creditCost;
}
```

### Validation
```csharp
// Validate node configuration
public bool IsValid()
{
    return !string.IsNullOrEmpty(nodeId) &&
           !string.IsNullOrEmpty(displayName) &&
           tier > 0 &&
           xpCost >= 0;
}
```

---

## Editor Integration

```csharp
#if UNITY_EDITOR
[ContextMenu("Validate Node")]
private void ValidateNode()
{
    if (string.IsNullOrEmpty(nodeId))
        Debug.LogError($"Node {name} missing nodeId");

    if (prerequisites != null)
    {
        foreach (var prereq in prerequisites)
        {
            if (prereq.tier >= tier)
                Debug.LogWarning($"Prerequisite {prereq.nodeId} tier >= this node tier");
        }
    }
}
#endif
```

---

## Usage Example

```csharp
// Check if research can be started
ResearchNodeSO node = researchDatabase.GetNode("destroyer_mk2");

if (node.ArePrerequisitesMet(playerCompletedResearch) &&
    node.MeetsTierRequirement(playerTier) &&
    node.CanAfford(playerXP, playerCredits))
{
    researchManager.StartResearch(playerId, node.nodeId);
}

// Get unlock on completion
if (node.unlockType == UnlockType.Ship)
{
    ShipDatabase.UnlockShip(node.unlockId);
}
```

---

## Tier Progression

| Tier | Typical Content | XP Range |
|------|-----------------|----------|
| 1 | Starter ships, basic modules | 0-1,000 |
| 2-3 | Early destroyers, light cruisers | 1,000-5,000 |
| 4-5 | Heavy cruisers, early battleships | 5,000-15,000 |
| 6-7 | Battleships, carriers | 15,000-40,000 |
| 8-9 | Advanced capital ships | 40,000-100,000 |
| 10 | End-game content | 100,000+ |

---

## Integration Points

### Dependencies
- `ResearchTreeSO` - Contains collections of nodes
- `ResearchDatabaseSO` - Master registry
- `ResearchManager` - Server-side research logic
- `WOS.Debugging.DebugManager` - Logging

### ScriptableObject Menu
`Create > WOS > Research > Research Node`

---

## Design Notes

### Prerequisite Logic
- **requiresAllPrerequisites = true**: All prerequisites must be complete (AND)
- **requiresAllPrerequisites = false**: Any prerequisite is sufficient (OR)

### Tier System
- Players unlock tiers by completing research
- Higher tiers have higher costs
- Tier gates prevent rushing to end-game

### Nation Affiliation
- Nodes belong to specific nations
- International nodes available to all
- Enables nation-specific tech trees
