# ResearchTreeSO.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Research/ResearchTreeSO.cs` |
| **Namespace** | `WOS.ScriptableObjects.Research` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | ~489 |
| **Architecture** | Tech tree container and navigation |

## Purpose
Organizes ResearchNodeSO instances into a navigable tech tree structure. Handles tier progression, node relationships, and tree validation. Each nation typically has its own ResearchTreeSO asset.

---

## Configuration

| Setting | Type | Description |
|---------|------|-------------|
| `treeId` | string | Unique tree identifier |
| `displayName` | string | UI display name |
| `nation` | ResearchNation | Associated nation |
| `description` | string | Tree description |
| `icon` | Sprite | Tree icon |

---

## Node Organization

```csharp
[Header("Nodes")]
public List<ResearchNodeSO> allNodes;

[Header("Tier Configuration")]
public int maxTier = 10;
public List<TierConfiguration> tierConfigs;

[System.Serializable]
public class TierConfiguration
{
    public int tier;
    public string tierName;
    public int requiredResearchCount;  // Research needed to unlock tier
    public Sprite tierIcon;
}
```

---

## Tree Structure

```csharp
[Header("Tree Layout")]
public List<TierNodes> nodesByTier;

[System.Serializable]
public class TierNodes
{
    public int tier;
    public List<ResearchNodeSO> nodes;
}
```

---

## Public API

### Node Queries
```csharp
// Get node by ID
public ResearchNodeSO GetNode(string nodeId)
{
    return allNodes.FirstOrDefault(n => n.nodeId == nodeId);
}

// Get all nodes at tier
public List<ResearchNodeSO> GetNodesAtTier(int tier)
{
    return allNodes.Where(n => n.tier == tier).ToList();
}

// Get available nodes (prerequisites met)
public List<ResearchNodeSO> GetAvailableNodes(HashSet<string> completedResearch, int playerTier)
{
    return allNodes.Where(n =>
        !completedResearch.Contains(n.nodeId) &&
        n.ArePrerequisitesMet(completedResearch) &&
        n.MeetsTierRequirement(playerTier)
    ).ToList();
}
```

### Tier Management
```csharp
// Get player's current tier
public int CalculatePlayerTier(HashSet<string> completedResearch)
{
    int currentTier = 1;

    foreach (var tierConfig in tierConfigs.OrderBy(t => t.tier))
    {
        int completedAtTier = allNodes.Count(n =>
            n.tier <= tierConfig.tier &&
            completedResearch.Contains(n.nodeId));

        if (completedAtTier >= tierConfig.requiredResearchCount)
            currentTier = tierConfig.tier + 1;
        else
            break;
    }

    return Mathf.Min(currentTier, maxTier);
}

// Get tier progress
public (int completed, int required) GetTierProgress(int tier, HashSet<string> completedResearch)
{
    var config = tierConfigs.FirstOrDefault(t => t.tier == tier);
    if (config == null) return (0, 0);

    int completed = allNodes.Count(n =>
        n.tier <= tier &&
        completedResearch.Contains(n.nodeId));

    return (completed, config.requiredResearchCount);
}
```

### Dependency Traversal
```csharp
// Get all prerequisites (recursive)
public List<ResearchNodeSO> GetAllPrerequisites(ResearchNodeSO node)
{
    var result = new List<ResearchNodeSO>();
    var visited = new HashSet<string>();

    void Traverse(ResearchNodeSO current)
    {
        if (current.prerequisites == null) return;

        foreach (var prereq in current.prerequisites)
        {
            if (!visited.Contains(prereq.nodeId))
            {
                visited.Add(prereq.nodeId);
                result.Add(prereq);
                Traverse(prereq);
            }
        }
    }

    Traverse(node);
    return result;
}

// Get all dependents (what this unlocks)
public List<ResearchNodeSO> GetDependents(ResearchNodeSO node)
{
    return allNodes.Where(n =>
        n.prerequisites != null &&
        n.prerequisites.Contains(node)
    ).ToList();
}
```

---

## Validation

```csharp
// Validate entire tree
public bool ValidateTree(out List<string> errors)
{
    errors = new List<string>();

    // Check for duplicate IDs
    var duplicates = allNodes.GroupBy(n => n.nodeId)
                             .Where(g => g.Count() > 1);
    foreach (var dup in duplicates)
        errors.Add($"Duplicate nodeId: {dup.Key}");

    // Check prerequisite references
    foreach (var node in allNodes)
    {
        if (node.prerequisites != null)
        {
            foreach (var prereq in node.prerequisites)
            {
                if (!allNodes.Contains(prereq))
                    errors.Add($"Node {node.nodeId} has invalid prerequisite");

                if (prereq.tier >= node.tier)
                    errors.Add($"Node {node.nodeId} prerequisite tier >= node tier");
            }
        }
    }

    // Check for circular dependencies
    foreach (var node in allNodes)
    {
        if (HasCircularDependency(node))
            errors.Add($"Circular dependency detected for {node.nodeId}");
    }

    return errors.Count == 0;
}

private bool HasCircularDependency(ResearchNodeSO node)
{
    var visited = new HashSet<string>();
    return CheckCircular(node, visited);
}

private bool CheckCircular(ResearchNodeSO node, HashSet<string> visited)
{
    if (visited.Contains(node.nodeId)) return true;

    visited.Add(node.nodeId);

    if (node.prerequisites != null)
    {
        foreach (var prereq in node.prerequisites)
        {
            if (CheckCircular(prereq, new HashSet<string>(visited)))
                return true;
        }
    }

    return false;
}
```

---

## Usage Example

```csharp
// Get US Navy tech tree
ResearchTreeSO usTree = researchDatabase.GetTree(ResearchNation.USA);

// Find available research for player
var available = usTree.GetAvailableNodes(playerCompleted, playerTier);

// Display tier progress
var (completed, required) = usTree.GetTierProgress(playerTier, playerCompleted);
tierProgressText.text = $"Tier {playerTier}: {completed}/{required}";

// Show what completing a node unlocks
var unlocks = usTree.GetDependents(selectedNode);
foreach (var unlock in unlocks)
{
    Debug.Log($"Completing {selectedNode.displayName} unlocks: {unlock.displayName}");
}
```

---

## Integration Points

### Dependencies
- `ResearchNodeSO` - Individual nodes
- `ResearchDatabaseSO` - Contains all trees
- `ResearchManager` - Server-side logic
- `WOS.Debugging.DebugManager` - Logging

### ScriptableObject Menu
`Create > WOS > Research > Research Tree`

---

## Design Notes

### Nation Trees
- Each nation has its own tech tree
- Trees can share International nodes
- Enables nation-specific progression paths

### Tier Gating
- Players must complete enough research to unlock next tier
- Prevents rushing to high-tier content
- Encourages breadth of research

### Visual Layout
- TierNodes structure enables visual tree layout
- Nodes organized by tier for UI display
- Prerequisite lines connect related nodes
