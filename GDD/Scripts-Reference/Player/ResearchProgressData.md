# ResearchProgressData.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/Data/ResearchProgressData.cs` |
| **Namespace** | `WOS.Player.Data` |
| **Lines of Code** | 359 |
| **Architecture** | Tech tree research system with time-gated progression |

## Purpose

`ResearchProgressData` manages player research progress in a tech tree system. It tracks which nodes are researched, which are currently in progress, and provides time-based progression mechanics similar to World of Warships or World of Tanks research systems.

**Key Features**:
- Multiple concurrent research slots
- Time-gated research (real-time completion)
- Free XP for instant completion
- Prerequisite validation
- Auto-completion on login

## ResearchProgressData Class

### Player Identity

| Field | Type | Description |
|-------|------|-------------|
| `playerId` | `string` | Player ID this progress belongs to |

### Research State

| Field | Type | Description |
|-------|------|-------------|
| `researchedNodeIds` | `HashSet<string>` | All researched node IDs |
| `activeResearch` | `List<ActiveResearch>` | Currently active research slots |

### Currency

| Field | Type | Description |
|-------|------|-------------|
| `freeXP` | `long` | Free XP available for research |

### Statistics

| Field | Type | Description |
|-------|------|-------------|
| `totalResearchXP` | `long` | Total research points earned (all-time) |
| `totalNodesResearched` | `int` | Total nodes researched (all-time) |
| `lastUpdateTime` | `DateTime` | Timestamp of last research update |

## State Queries

```csharp
// Check if node is already researched
public bool IsNodeResearched(string nodeId)

// Check if node is currently being researched
public bool IsNodeInProgress(string nodeId)

// Get active research for specific node
public ActiveResearch GetActiveResearch(string nodeId)

// Get all completed research (time elapsed)
public List<ActiveResearch> GetCompletedResearch()

// Get number of available research slots
public int GetAvailableSlots(int maxSlots)

// Check if player can start new research
public bool CanStartResearch(int maxSlots)
```

## Research Operations

### Starting Research

```csharp
public ActiveResearch StartResearch(string nodeId, string nodeName,
    long xpCost, int creditCost, int researchTimeSeconds)
{
    var research = new ActiveResearch
    {
        nodeId = nodeId,
        nodeName = nodeName,
        xpCost = xpCost,
        creditCost = creditCost,
        researchTimeSeconds = researchTimeSeconds,
        startTime = DateTime.UtcNow,
        completionTime = DateTime.UtcNow.AddSeconds(researchTimeSeconds)
    };

    activeResearch.Add(research);
    lastUpdateTime = DateTime.UtcNow;

    return research;
}
```

**Purpose**: Start researching a tech tree node. Creates time-gated research that completes after specified duration.

### Completing Research

```csharp
public void CompleteResearch(string nodeId)
{
    var research = GetActiveResearch(nodeId);
    if (research == null) return;

    // Move to researched
    researchedNodeIds.Add(nodeId);
    activeResearch.Remove(research);

    // Update statistics
    totalResearchXP += research.xpCost;
    totalNodesResearched++;
    lastUpdateTime = DateTime.UtcNow;
}
```

**Purpose**: Complete a research node and move it to the researched set.

### Canceling Research

```csharp
public bool CancelResearch(string nodeId, bool refund)
{
    var research = GetActiveResearch(nodeId);
    if (research == null) return false;

    activeResearch.Remove(research);
    lastUpdateTime = DateTime.UtcNow;

    // Note: Refund logic handled by manager
    return true;
}
```

**Purpose**: Cancel active research. Refund logic is handled by calling manager.

### Instant Completion

```csharp
// Complete instantly with premium currency
public void InstantCompleteResearch(string nodeId)
{
    var research = GetActiveResearch(nodeId);
    if (research == null) return;

    // Set completion time to now
    research.completionTime = DateTime.UtcNow;
    lastUpdateTime = DateTime.UtcNow;
}

// Complete instantly with free XP
public bool UseFreeXP(string nodeId, long freeXPCost)
{
    if (freeXP < freeXPCost) return false;

    var research = GetActiveResearch(nodeId);
    if (research == null) return false;

    // Deduct free XP
    freeXP -= freeXPCost;

    // Set completion time to now
    research.completionTime = DateTime.UtcNow;
    lastUpdateTime = DateTime.UtcNow;

    return true;
}
```

**Purpose**: Skip research time using premium currency or free XP.

### Free XP Management

```csharp
public void AddFreeXP(long amount)
{
    freeXP += amount;
    lastUpdateTime = DateTime.UtcNow;
}
```

**Purpose**: Award free XP from matches or events.

## Auto-Completion System

```csharp
public List<string> ProcessCompletedResearch()
{
    List<string> completed = new List<string>();
    DateTime now = DateTime.UtcNow;

    for (int i = activeResearch.Count - 1; i >= 0; i--)
    {
        if (activeResearch[i].IsComplete(now))
        {
            string nodeId = activeResearch[i].nodeId;
            CompleteResearch(nodeId);
            completed.Add(nodeId);
        }
    }

    return completed;
}
```

**Purpose**: Process all completed research and auto-complete them. Call periodically or when player logs in.

**Design**: Iterates backwards to safely remove items during iteration.

## Statistics

```csharp
// Get research completion percentage
public float GetCompletionPercent(int totalNodes)
{
    if (totalNodes == 0) return 0f;
    return (totalNodesResearched / (float)totalNodes) * 100f;
}

// Get statistics summary
public string GetStatisticsSummary()
{
    return $"Researched: {totalNodesResearched}, " +
           $"In Progress: {activeResearch.Count}, " +
           $"Total XP: {totalResearchXP:N0}, " +
           $"Free XP: {freeXP:N0}";
}
```

## ActiveResearch Class

### Purpose
Represents a single research slot currently in progress.

### Research Data

| Field | Type | Description |
|-------|------|-------------|
| `nodeId` | `string` | Node ID being researched |
| `nodeName` | `string` | Node name (for UI display) |
| `xpCost` | `long` | XP cost of this research |
| `creditCost` | `int` | Credit cost of this research |
| `researchTimeSeconds` | `int` | Research time in seconds |

### Time Tracking

| Field | Type | Description |
|-------|------|-------------|
| `startTime` | `DateTime` | When research started |
| `completionTime` | `DateTime` | When research will complete |

## ActiveResearch Methods

```csharp
// Check if research is complete
public bool IsComplete(DateTime currentTime)
{
    return currentTime >= completionTime;
}

// Get time remaining in seconds
public int GetTimeRemaining(DateTime currentTime)
{
    if (IsComplete(currentTime)) return 0;

    TimeSpan remaining = completionTime - currentTime;
    return (int)remaining.TotalSeconds;
}

// Get time remaining as formatted string
public string GetTimeRemainingFormatted(DateTime currentTime)
{
    int seconds = GetTimeRemaining(currentTime);
    if (seconds <= 0) return "Complete!";

    int hours = seconds / 3600;
    int minutes = (seconds % 3600) / 60;
    int secs = seconds % 60;

    if (hours > 0)
        return $"{hours}h {minutes}m {secs}s";
    if (minutes > 0)
        return $"{minutes}m {secs}s";

    return $"{secs}s";
}

// Get research progress percentage
public float GetProgressPercent(DateTime currentTime)
{
    if (researchTimeSeconds == 0) return 100f;

    TimeSpan elapsed = currentTime - startTime;
    float percent = ((float)elapsed.TotalSeconds / researchTimeSeconds) * 100f;

    return Mathf.Clamp(percent, 0f, 100f);
}

// Get elapsed time in seconds
public int GetElapsedTime(DateTime currentTime)
{
    TimeSpan elapsed = currentTime - startTime;
    return (int)elapsed.TotalSeconds;
}
```

## Usage Examples

### Starting Research

```csharp
ResearchProgressData progress = playerResearchProgress;

// Check if player can start research
if (!progress.CanStartResearch(maxSlots: 3))
{
    Debug.LogError("All research slots are full!");
    return;
}

// Start researching a node
ActiveResearch research = progress.StartResearch(
    nodeId: "ship_t5_battleship",
    nodeName: "T5 Battleship",
    xpCost: 50000,
    creditCost: 500000,
    researchTimeSeconds: 86400  // 24 hours
);

Debug.Log($"Research started: {research.nodeName}");
Debug.Log($"Completion time: {research.completionTime}");
```

### Checking Progress

```csharp
ActiveResearch research = progress.GetActiveResearch("ship_t5_battleship");

if (research != null)
{
    DateTime now = DateTime.UtcNow;

    float percent = research.GetProgressPercent(now);
    string timeRemaining = research.GetTimeRemainingFormatted(now);

    Debug.Log($"Progress: {percent:F1}%");
    Debug.Log($"Time remaining: {timeRemaining}");

    if (research.IsComplete(now))
    {
        progress.CompleteResearch(research.nodeId);
        Debug.Log("Research complete!");
    }
}
```

### Using Free XP

```csharp
// Calculate free XP cost (example: 1 XP per remaining second)
ActiveResearch research = progress.GetActiveResearch("ship_t5_battleship");
int remainingSeconds = research.GetTimeRemaining(DateTime.UtcNow);
long freeXPCost = remainingSeconds;

if (progress.UseFreeXP(research.nodeId, freeXPCost))
{
    progress.CompleteResearch(research.nodeId);
    Debug.Log("Research completed instantly with free XP!");
}
else
{
    Debug.LogError($"Insufficient free XP! Need {freeXPCost}, have {progress.freeXP}");
}
```

### Auto-Completing on Login

```csharp
// Called when player logs in
List<string> completedNodes = progress.ProcessCompletedResearch();

if (completedNodes.Count > 0)
{
    Debug.Log($"Auto-completed {completedNodes.Count} research nodes:");
    foreach (string nodeId in completedNodes)
    {
        Debug.Log($"  - {nodeId}");
    }

    // Show notification to player
    ShowResearchCompleteNotification(completedNodes);
}
```

### Managing Multiple Research Slots

```csharp
const int MAX_RESEARCH_SLOTS = 3;

// Get available slots
int availableSlots = progress.GetAvailableSlots(MAX_RESEARCH_SLOTS);
Debug.Log($"Available research slots: {availableSlots}/{MAX_RESEARCH_SLOTS}");

// Display active research
foreach (ActiveResearch research in progress.activeResearch)
{
    float percent = research.GetProgressPercent(DateTime.UtcNow);
    Debug.Log($"{research.nodeName}: {percent:F1}%");
}
```

## Integration Points

### Database Persistence
- **Storage**: PlayFab Player Data or backend database
- **Sync**: Periodic saves on research state changes
- **Auto-completion**: Process on login and periodically

### Related Systems

| System | Integration |
|--------|-------------|
| **Tech Tree System** | Defines research nodes and prerequisites |
| **Currency System** | Deducts XP and credits when starting research |
| **Free XP System** | Awards free XP from matches |
| **Premium Store** | Instant completion with premium currency |
| **Notification System** | Alerts when research completes |

## Design Notes

### Time-Gated Progression

Research uses **real-time timers** similar to World of Warships:
- Start research → wait X hours → auto-complete
- Keeps players engaged long-term
- Creates monetization opportunity (skip timers)

**Design Philosophy**:
1. **Casual-friendly**: Research progresses while offline
2. **Retention**: Players log in to check completed research
3. **Monetization**: Premium currency to skip timers

### Multiple Research Slots

Players can research **multiple nodes simultaneously**:
- Default: 1 slot (free players)
- Premium: 3 slots (purchased with real money)
- This creates monetization tier without "pay-to-win"

### Free XP System

Free XP allows **skipping research timers**:
- Earned passively from all matches (small %)
- Can be used on any research node
- 1 Free XP = 1 second of research time (example ratio)

**Design Intent**:
- Reward active players (earn free XP faster)
- Provide "catch-up" mechanic (skip lower tiers)
- Monetization (can purchase free XP with real money)

### Auto-Completion Logic

Research **auto-completes** when time elapses:
```csharp
if (currentTime >= completionTime)
{
    // Auto-complete
}
```

**When to Process**:
1. **On login**: `ProcessCompletedResearch()` catches up offline research
2. **Periodically**: Every 5 minutes while online
3. **On UI refresh**: When player opens research screen

### Statistics Tracking

Tracks lifetime statistics for:
- **Achievement system**: "Research 100 nodes"
- **Leaderboards**: "Total research XP"
- **Analytics**: Player progression metrics

### HashSet vs. List

Uses **HashSet** for researched nodes:
```csharp
public HashSet<string> researchedNodeIds;
```

**Benefits**:
- O(1) lookup: `IsNodeResearched()` is instant
- Prevents duplicates automatically
- Memory efficient for large tech trees

### Timestamp Handling

All timestamps use **UTC** for consistency:
```csharp
startTime = DateTime.UtcNow;
```

**Why UTC**:
- Prevents timezone bugs
- Works across different regions
- Compatible with server timestamps

### Cancellation Refunds

`CancelResearch()` has `refund` parameter but doesn't implement logic:
```csharp
public bool CancelResearch(string nodeId, bool refund)
```

**Design**: Manager layer handles refund logic (credits, XP) to keep data class simple.

### Premium Currency Integration

`InstantCompleteResearch()` doesn't deduct currency:
```csharp
public void InstantCompleteResearch(string nodeId)
{
    // Set completion time to now (no currency deduction)
}
```

**Design**: Manager layer validates and deducts premium currency before calling this method.

### Free XP Validation

`UseFreeXP()` validates and deducts in same operation:
```csharp
if (freeXP < freeXPCost) return false;
freeXP -= freeXPCost;
```

**Atomic operation** prevents race conditions where:
1. Check passes (have enough XP)
2. Deduction fails (XP spent elsewhere)

### Time Calculation Safety

```csharp
return Mathf.Clamp(percent, 0f, 100f);
```

Clamps progress to 0-100% to prevent:
- Negative progress (time travel bugs)
- >100% progress (display glitches)

### Future Enhancements

Potential additions:
1. **Research bonuses**: +10% speed with premium
2. **Crew research**: Assign crew to speed up research
3. **Event bonuses**: 2x research speed weekends
4. **Research queue**: Queue up multiple nodes per slot
5. **Priority research**: Spend extra credits to speed up specific node
