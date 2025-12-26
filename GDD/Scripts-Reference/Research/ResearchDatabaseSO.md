# ResearchDatabaseSO.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Research/ResearchDatabaseSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Research` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | ~489 |
| **Architecture** | Master research configuration and global settings |

## Purpose
Master database containing all research trees, global research settings, and premium features. Provides centralized access to all research content. Server uses for authoritative research validation.

---

## Global Configuration

```csharp
[Header("Global Settings")]
public float xpMultiplier = 1.0f;          // Global XP cost modifier
public float creditMultiplier = 1.0f;       // Global credit cost modifier
public float timeMultiplier = 1.0f;         // Global research time modifier

[Header("Research Slots")]
public int maxResearchSlots = 3;            // Base research slots
public int premiumBonusSlots = 2;           // Extra slots for premium

[Header("Free XP")]
public float freeXPPercentage = 5f;         // % of XP goes to Free XP pool
public float freeXPConversionRate = 1.0f;   // Rate for Free XP usage
```

---

## Tree Registry

```csharp
[Header("Research Trees")]
public List<ResearchTreeSO> allTrees;

[Header("By Nation")]
public ResearchTreeSO usaTree;
public ResearchTreeSO japanTree;
public ResearchTreeSO britainTree;
public ResearchTreeSO germanyTree;
public ResearchTreeSO russiaTree;
public ResearchTreeSO franceTree;
public ResearchTreeSO italyTree;
public ResearchTreeSO chinaTree;
public ResearchTreeSO internationalTree;
```

---

## Premium Features

```csharp
[Header("Premium Options")]
public bool allowInstantResearch = true;
public int instantResearchBaseCost = 100;   // Premium currency
public float instantResearchMultiplier = 0.01f;  // Per XP cost
public bool allowFreeXPConversion = true;
public int freeXPConversionMinimum = 100;   // Minimum Free XP to use
```

---

## Public API

### Tree Access
```csharp
// Get tree by nation
public ResearchTreeSO GetTree(ResearchNation nation)
{
    return nation switch
    {
        ResearchNation.USA => usaTree,
        ResearchNation.Japan => japanTree,
        ResearchNation.Britain => britainTree,
        ResearchNation.Germany => germanyTree,
        ResearchNation.Russia => russiaTree,
        ResearchNation.France => franceTree,
        ResearchNation.Italy => italyTree,
        ResearchNation.China => chinaTree,
        ResearchNation.International => internationalTree,
        _ => null
    };
}

// Get all trees
public IEnumerable<ResearchTreeSO> GetAllTrees()
{
    return allTrees.Where(t => t != null);
}
```

### Node Lookup
```csharp
// Find node across all trees
public ResearchNodeSO FindNode(string nodeId)
{
    foreach (var tree in allTrees)
    {
        var node = tree?.GetNode(nodeId);
        if (node != null) return node;
    }
    return null;
}

// Find node's parent tree
public ResearchTreeSO GetNodeTree(string nodeId)
{
    foreach (var tree in allTrees)
    {
        if (tree?.GetNode(nodeId) != null)
            return tree;
    }
    return null;
}
```

### Cost Calculations
```csharp
// Get adjusted XP cost
public int GetAdjustedXPCost(ResearchNodeSO node)
{
    return Mathf.RoundToInt(node.xpCost * xpMultiplier);
}

// Get adjusted credit cost
public int GetAdjustedCreditCost(ResearchNodeSO node)
{
    return Mathf.RoundToInt(node.creditCost * creditMultiplier);
}

// Get adjusted research time
public float GetAdjustedResearchTime(ResearchNodeSO node)
{
    return node.researchTime * timeMultiplier;
}

// Calculate instant complete cost
public int GetInstantCompleteCost(ResearchNodeSO node)
{
    if (!allowInstantResearch || !node.allowInstantComplete)
        return -1;

    return Mathf.RoundToInt(
        instantResearchBaseCost +
        (node.xpCost * instantResearchMultiplier)
    );
}
```

### Free XP System
```csharp
// Calculate Free XP earned from research XP
public int CalculateFreeXPEarned(int researchXPSpent)
{
    return Mathf.RoundToInt(researchXPSpent * (freeXPPercentage / 100f));
}

// Calculate how much Free XP needed to complete research
public int CalculateFreeXPNeeded(ResearchNodeSO node, int currentProgress)
{
    int remaining = GetAdjustedXPCost(node) - currentProgress;
    return Mathf.RoundToInt(remaining * freeXPConversionRate);
}

// Check if Free XP can be used
public bool CanUseFreeXP(int playerFreeXP)
{
    return allowFreeXPConversion && playerFreeXP >= freeXPConversionMinimum;
}
```

### Slot Management
```csharp
// Get total research slots
public int GetTotalSlots(bool isPremium)
{
    return isPremium ? maxResearchSlots + premiumBonusSlots : maxResearchSlots;
}

// Check if slot available
public bool HasAvailableSlot(int activeResearchCount, bool isPremium)
{
    return activeResearchCount < GetTotalSlots(isPremium);
}
```

---

## Validation

```csharp
// Validate entire database
public bool ValidateDatabase(out List<string> errors)
{
    errors = new List<string>();

    // Validate all trees
    foreach (var tree in allTrees)
    {
        if (tree == null)
        {
            errors.Add("Null tree reference in database");
            continue;
        }

        if (!tree.ValidateTree(out var treeErrors))
        {
            errors.AddRange(treeErrors.Select(e => $"{tree.treeId}: {e}"));
        }
    }

    // Check for cross-tree duplicate IDs
    var allNodeIds = allTrees
        .Where(t => t != null)
        .SelectMany(t => t.allNodes)
        .Select(n => n.nodeId);

    var duplicates = allNodeIds.GroupBy(id => id).Where(g => g.Count() > 1);
    foreach (var dup in duplicates)
        errors.Add($"Cross-tree duplicate nodeId: {dup.Key}");

    return errors.Count == 0;
}
```

---

## Usage Example

```csharp
// Singleton access pattern
ResearchDatabaseSO database = Resources.Load<ResearchDatabaseSO>("Research/ResearchDatabase");

// Find a node
ResearchNodeSO node = database.FindNode("us_destroyer_mk2");

// Calculate costs with multipliers
int xpCost = database.GetAdjustedXPCost(node);
int creditCost = database.GetAdjustedCreditCost(node);
int instantCost = database.GetInstantCompleteCost(node);

// Check research slots
if (database.HasAvailableSlot(player.activeResearch.Count, player.isPremium))
{
    researchManager.StartResearch(playerId, node.nodeId);
}

// Free XP usage
if (database.CanUseFreeXP(player.freeXP))
{
    int freeXPNeeded = database.CalculateFreeXPNeeded(node, currentProgress);
    // Show option to use Free XP
}
```

---

## Integration Points

### Dependencies
- `ResearchTreeSO` - Individual trees
- `ResearchNodeSO` - Individual nodes
- `ResearchManager` - Server-side logic
- `WOS.Debugging.DebugManager` - Logging

### ScriptableObject Menu
`Create > WOS > Research > Research Database`

### Resource Loading
`Resources/Research/ResearchDatabase`

---

## Design Notes

### Global Multipliers
- `xpMultiplier`: Events can reduce costs (0.5x = half price)
- `timeMultiplier`: Events can speed up research
- Multipliers apply to all research uniformly

### Premium Benefits
- Extra research slots (3 → 5)
- Instant research option
- Free XP conversion access

### Free XP System
- 5% of all earned XP goes to Free XP pool
- Free XP can complete any research
- Enables skipping grindy nodes
- Premium feature gate for conversion

### Server Authority
- All costs calculated server-side using this database
- Client displays values, server validates
- Prevents client-side cost manipulation
