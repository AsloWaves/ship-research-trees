# AutoSaveSystem.cs

## Quick Reference

| **File** | AutoSaveSystem.cs |
|----------|------------------|
| **Namespace** | WOS.Networking.Managers |
| **Inheritance** | MonoBehaviour |
| **Lines** | 237 |
| **Architecture** | Singleton, dirty flag batching, coroutine-based scheduling |

---

## Purpose

Automatic save system for inventory data using dirty flag batching to reduce database writes by 95%+.

**Performance Impact**:
- **Without AutoSave**: 50-100 DB writes per player per minute (2000+ for 20 players)
- **With AutoSave**: 1 DB write per player per minute (20 for 20 players)
- **Reduction**: 95-99% fewer database operations

---

## How It Works

```
1. Items are used/moved in-memory (instant, no DB queries)
   ↓
2. Inventory is marked "dirty" when modified (HashSet add)
   ↓
3. Every 60 seconds, all dirty inventories are saved in a batch
   ↓
4. Database writes reduced from 1000+/min to ~20/min
```

---

## Configuration

### Inspector Settings

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `saveInterval` | float | `60f` | Auto-save interval in seconds |
| `maxConcurrentSaves` | int | `5` | Max concurrent saves (prevents lag) |

### Statistics (Read-Only)

| Field | Type | Description |
|-------|------|-------------|
| `totalSaveCount` | int | Total number of auto-saves performed |
| `lastBatchSuccessCount` | int | Successful saves in last batch |
| `lastBatchFailCount` | int | Failed saves in last batch |
| `lastSaveTime` | string | Time of last auto-save |

---

## Public API

### Auto-Save Methods

#### `PerformAutoSave()` (Coroutine)
Performs auto-save of all dirty inventories. Called automatically every 60 seconds.

**Process**:
1. Get all dirty player IDs from ServerInventoryManager
2. Save in batches (max 5 concurrent)
3. Update statistics
4. Schedule next save

#### `ForceSaveAll(Action callback)` (Coroutine)
Forces immediate save of all dirty inventories.

**Parameters**:
- `callback` - Callback when complete

**Example**:
```csharp
// Server shutdown
void OnApplicationQuit()
{
    yield return AutoSaveSystem.Instance.ForceSaveAll(() =>
    {
        Debug.Log("All inventories saved on shutdown");
    });
}
```

### Statistics Methods

#### `GetTimeUntilNextSave()`
Gets time remaining until next auto-save.

**Returns**: `float` (seconds)

**Example**:
```csharp
float timeLeft = AutoSaveSystem.Instance.GetTimeUntilNextSave();
Debug.Log($"Next auto-save in {timeLeft:F0} seconds");
```

#### `GetStatistics()`
Gets auto-save statistics for server monitoring.

**Returns**: `(int total, int lastSuccess, int lastFail, string lastTime)`

**Example**:
```csharp
var stats = AutoSaveSystem.Instance.GetStatistics();
Debug.Log($"Total saves: {stats.total}, Last batch: {stats.lastSuccess}/{stats.lastFail}");
```

---

## Integration with ServerInventoryManager

### Workflow

```csharp
// 1. Player modifies inventory (instant, in-memory)
inventory.AddItem(newItem);

// 2. Mark inventory as dirty
ServerInventoryManager.Instance.MarkInventoryDirty(playerId);

// 3. AutoSaveSystem saves automatically after 60 seconds
// (No blocking DB write during gameplay!)
```

### Automatic Saving

```csharp
// AutoSaveSystem.Update() - runs every frame
void Update()
{
    if (!NetworkServer.active) return;

    // Check if it's time to save
    if (Time.time >= nextSaveTime && !isSaving)
    {
        StartCoroutine(PerformAutoSave());
    }
}
```

---

## Performance Optimization

### Batch Saving

**Problem**: Individual saves cause lag
```
Player 1: Use item → Save (200ms lag)
Player 2: Move item → Save (200ms lag)
Player 3: Split stack → Save (200ms lag)
```

**Solution**: Batch saves every 60 seconds
```
00:00 - Player 1 uses 5 items (marked dirty)
00:15 - Player 2 moves 3 items (marked dirty)
00:30 - Player 3 splits stack (marked dirty)
01:00 - AutoSave saves all 3 inventories in parallel (no lag!)
```

### Concurrent Save Limiting

**maxConcurrentSaves = 5** prevents server lag:

```csharp
// Save in batches to prevent lag
foreach (string playerId in dirtyPlayers)
{
    // Wait if we've reached max concurrent saves
    while (activeSaves.Count >= maxConcurrentSaves)
    {
        yield return new WaitForSeconds(0.1f);
    }

    // Start save coroutine
    activeSaves.Add(StartCoroutine(SaveSingleInventory(playerId)));
}
```

**Result**: Even with 100 dirty inventories, only 5 save at once (prevents CPU spike).

---

## Usage Example

### Complete Workflow

```csharp
// Gameplay: Player uses item
[Server]
public void UseConsumableItem(NetworkConnection conn, string itemId)
{
    string playerId = AccountManager.Instance.GetPlayerId(conn.connectionId);
    var inventory = ServerInventoryManager.Instance.GetCachedInventory(playerId);

    // Use item (instant, in-memory)
    inventory.RemoveItem(itemId);

    // Mark dirty (instant, HashSet add)
    ServerInventoryManager.Instance.MarkInventoryDirty(playerId);

    // AutoSaveSystem will save automatically within 60 seconds
    // No blocking DB write!
}

// Server monitoring
IEnumerator MonitorAutoSave()
{
    while (true)
    {
        var stats = AutoSaveSystem.Instance.GetStatistics();
        float timeLeft = AutoSaveSystem.Instance.GetTimeUntilNextSave();

        Debug.Log($"AutoSave Stats: {stats.total} total, Next in {timeLeft:F0}s");

        yield return new WaitForSeconds(10f);
    }
}
```

---

## Design Notes

### Dirty Flag Pattern

**Why it works**:
1. Most inventories are modified multiple times between saves
2. Marking dirty is O(1) (HashSet add)
3. Batch saves eliminate redundant writes

**Example**:
```
00:00 - Use item (dirty flag = true, 0 saves)
00:10 - Move item (dirty flag = true, 0 saves)  ← Still only 1 dirty flag
00:20 - Split stack (dirty flag = true, 0 saves) ← Still only 1 dirty flag
01:00 - AutoSave (1 save instead of 3!)
```

### Server Shutdown Handling

**OnApplicationQuit()**:
```csharp
void OnApplicationQuit()
{
    if (NetworkServer.active)
    {
        // Force save all dirty inventories
        List<string> dirtyPlayers = ServerInventoryManager.Instance.GetDirtyPlayerIds();

        foreach (string playerId in dirtyPlayers)
        {
            // Initiate saves (simplified - real implementation would wait)
            StartCoroutine(ServerInventoryManager.Instance.SaveInventory(playerId, ...));
        }
    }
}
```

**Note**: Current implementation initiates saves but doesn't wait for completion. Future enhancement: block shutdown until saves complete.

---

## Key Takeaways

1. **95%+ Reduction**: Dirty flag batching drastically reduces database writes
2. **60-Second Interval**: Automatic saves every minute
3. **Concurrent Limiting**: Max 5 saves at once prevents server lag
4. **ServerInventoryManager Integration**: Works seamlessly with dirty flag system
5. **Force Save Support**: Manual saves for server shutdown or admin commands
