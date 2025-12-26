# ExtractionController.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Permadeath/Controllers/ExtractionController.cs` |
| **Namespace** | `WOS.Permadeath.Controllers` |
| **Inheritance** | `NetworkBehaviour` |
| **Pattern** | Singleton |
| **Lines** | ~586 |
| **Architecture** | Server-authoritative extraction point management |

## Purpose
Manages extraction points where players can safely extract with their cargo and rewards. Handles extraction attempts, progress tracking, threat detection, and bonus calculations in a server-authoritative manner.

---

## Class Diagram

```
ExtractionController (NetworkBehaviour, Singleton)
├── Extraction Points
│   ├── RegisterExtractionPoint()
│   ├── GetExtractionPoint()
│   ├── GetPointsInZone()
│   └── SetPointState()
├── Extraction Attempts
│   ├── CmdRequestExtraction()
│   ├── CmdCancelExtraction()
│   └── CancelExtraction()
├── Threat Detection
│   ├── CheckExtractionThreats()
│   ├── CountThreatsNearPoint()
│   ├── HandlePlayerDeath()
│   └── HandlePlayerLeftArea()
└── Network Sync
    ├── SyncDictionary<string, ExtractionState>
    └── RPC Notifications
```

---

## Configuration

### Extraction Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `defaultExtractionDuration` | 30s | Base extraction time |
| `contestedExtractionMultiplier` | 1.5x | Time multiplier when contested |
| `threatCheckInterval` | 2s | Threat detection update rate |
| `threatDetectionRadius` | 150 units | Range to detect threats |

### Reward Multipliers
| Bonus | Multiplier | Condition |
|-------|------------|-----------|
| Base extraction | 1.1x | All successful extractions |
| Contested | 1.25x | Threats present during extraction |
| Speed | 1.1x | Completed in <80% of required time |

### Cooldowns
| Type | Duration | Description |
|------|----------|-------------|
| Point cooldown | 300s (5 min) | Time before point becomes available again |
| Player cooldown | 60s | Time between player extraction attempts |

---

## Synced State

```csharp
private readonly SyncDictionary<string, ExtractionState> pointStates =
    new SyncDictionary<string, ExtractionState>();
```

Automatically synchronizes extraction point states to all clients.

---

## Events

| Event | Signature | Trigger |
|-------|-----------|---------|
| `OnExtractionStarted` | `Action<string, string>` | Player begins extraction (playerId, pointId) |
| `OnExtractionProgress` | `Action<string, float>` | Progress update (playerId, progress 0-1) |
| `OnExtractionCompleted` | `Action<string, ExtractionResult>` | Extraction finished |
| `OnExtractionInterrupted` | `Action<string, string>` | Extraction cancelled (playerId, reason) |
| `OnExtractionPointActivated` | `Action<string>` | Point becomes available |
| `OnExtractionPointDeactivated` | `Action<string>` | Point becomes unavailable |

---

## Core Methods

### Point Management

```csharp
// Register extraction point (Server)
[Server]
public void RegisterExtractionPoint(ExtractionPoint point)

// Get point by ID
public ExtractionPoint GetExtractionPoint(string pointId)

// Get all points in zone
public List<ExtractionPoint> GetPointsInZone(string zoneId)

// Set point state (Server)
[Server]
public void SetPointState(string pointId, ExtractionState state)
```

### Extraction Requests

```csharp
// Client requests extraction
[Command(requiresAuthority = false)]
public void CmdRequestExtraction(string pointId, NetworkConnectionToClient sender = null)

// Client cancels extraction
[Command(requiresAuthority = false)]
public void CmdCancelExtraction(NetworkConnectionToClient sender = null)

// Server cancels extraction
[Server]
public void CancelExtraction(string playerId, string reason)
```

### Threat Handling

```csharp
// Handle player death during extraction
[Server]
public void HandlePlayerDeath(string playerId)

// Handle player leaving extraction area
[Server]
public void HandlePlayerLeftArea(string playerId)
```

---

## Public API

```csharp
// Get all extraction points
public List<ExtractionPoint> GetAllPoints()

// Get active extraction attempt for player
public ExtractionAttempt GetActiveAttempt(string playerId)

// Check if player is currently extracting
public bool IsPlayerExtracting(string playerId)

// Get remaining cooldown for player
public float GetPlayerCooldown(string playerId)
```

---

## Extraction Flow

### 1. Request Validation
```csharp
private bool CanStartExtraction(string playerId, string pointId, out string reason)
{
    // Check point exists and is available
    // Check player cooldown
    // Check if player already extracting
    // Check point uses remaining
    // TODO: Check player position
    // TODO: Check tier requirements
    // TODO: Check area clear requirement
}
```

### 2. Start Extraction
```csharp
[Server]
private void StartExtraction(string playerId, string pointId)
{
    var attempt = new ExtractionAttempt
    {
        attemptId = Guid.NewGuid().ToString(),
        playerId = playerId,
        extractionPointId = pointId,
        startTime = Time.time,
        requiredDuration = point.extractionDuration,
        currentProgress = 0f
    };

    // TODO: Gather cargo from player's ship

    activeAttempts[playerId] = attempt;
    point.state = ExtractionState.InProgress;
    point.occupyingPlayerId = playerId;
}
```

### 3. Progress Updates
```csharp
[Server]
private void UpdateActiveExtractions()
{
    foreach (var kvp in activeAttempts)
    {
        float elapsed = Time.time - attempt.startTime;
        float progress = Mathf.Clamp01(elapsed / attempt.requiredDuration);
        attempt.currentProgress = progress;

        OnExtractionProgress?.Invoke(attempt.playerId, progress);

        if (progress >= 1f)
            completedAttempts.Add(kvp.Key);
    }
}
```

### 4. Completion & Rewards
```csharp
[Server]
private void CompleteExtraction(string playerId)
{
    var result = new ExtractionResultData
    {
        result = ExtractionResult.Success,
        extractionTime = Time.time - attempt.startTime,
        totalValueExtracted = attempt.totalCargoValue,
        bonusMultiplier = CalculateExtractionBonus(attempt)
    };

    result.currencyReward = result.totalValueExtracted * result.bonusMultiplier;
    result.experienceReward = result.totalValueExtracted * 0.1f;
    result.reputationReward = 10f;

    // Set point cooldown
    StartCoroutine(ResetPointAfterCooldown(point.extractionId, pointCooldownDuration));

    // Set player cooldown
    playerCooldowns[playerId] = Time.time + playerCooldownDuration;
}
```

---

## Threat Detection

### Threat Check Loop
```csharp
private void Update()
{
    if (!isServer) return;

    threatCheckTimer += Time.deltaTime;
    if (threatCheckTimer >= threatCheckInterval)  // Every 2 seconds
    {
        threatCheckTimer = 0f;
        CheckExtractionThreats();
    }
}
```

### Contested Extraction
```csharp
[Server]
private void CheckExtractionThreats()
{
    foreach (var kvp in activeAttempts)
    {
        int threatCount = CountThreatsNearPoint(point.position, attempt.playerId);
        attempt.threatCount = threatCount;

        if (threatCount > 0 && point.state == ExtractionState.InProgress)
        {
            // Extend extraction time when contested
            attempt.requiredDuration = point.extractionDuration * contestedExtractionMultiplier;
        }
    }
}
```

---

## Bonus Calculation

```csharp
private float CalculateExtractionBonus(ExtractionAttempt attempt)
{
    float bonus = baseExtractionBonus;  // 1.1x

    // Contested bonus (+25%)
    if (attempt.threatCount > 0)
        bonus *= contestedBonus;  // 1.25x

    // Speed bonus (completed in <80% of time)
    float actualTime = Time.time - attempt.startTime;
    if (actualTime < attempt.requiredDuration * 0.8f)
        bonus *= speedBonus;  // 1.1x

    return bonus;
}
```

**Maximum Bonus**: 1.1 × 1.25 × 1.1 = **1.5125x**

---

## Network RPCs

### Client Notifications
| RPC | Parameters | Purpose |
|-----|------------|---------|
| `RpcNotifyPointStateChanged` | pointId, state | Update point UI |
| `RpcNotifyExtractionStarted` | playerId, pointId, duration | Show extraction timer |
| `RpcNotifyExtractionInterrupted` | playerId, reason | Show interruption |
| `RpcNotifyExtractionComplete` | playerId, reward, bonus | Show rewards |

### Targeted Notifications
| RPC | Parameters | Purpose |
|-----|------------|---------|
| `RpcNotifyExtractionDenied` | connectionId, reason | Deny extraction request |

---

## Usage Example

```csharp
// Register extraction point
var point = new ExtractionPoint
{
    extractionId = "dock_alpha",
    zoneId = "harbor_01",
    displayName = "Alpha Dock",
    position = new Vector3(100, 0, 200),
    extractionDuration = 30f
};
ExtractionController.Instance.RegisterExtractionPoint(point);

// Client requests extraction
ExtractionController.Instance.CmdRequestExtraction("dock_alpha");

// Check player status
if (ExtractionController.Instance.IsPlayerExtracting(playerId))
{
    var attempt = ExtractionController.Instance.GetActiveAttempt(playerId);
    Debug.Log($"Extraction progress: {attempt.currentProgress:P0}");
}

// Get cooldown
float cooldown = ExtractionController.Instance.GetPlayerCooldown(playerId);
if (cooldown > 0)
    Debug.Log($"Extraction available in {cooldown}s");
```

---

## Integration Points

### Dependencies
- `WOS.Permadeath.Data` - Data structures
- `WOS.Debugging.DebugManager` - Logging
- `Mirror` - Networking

### Interacts With
- `PermadeathManager` - Death handling during extraction
- Inventory system (TODO: cargo gathering)
- Zone system (TODO: position validation)

---

## Design Notes

### Extraction as Safe Exit
- Players must reach extraction points to secure loot
- Similar to "Tarkov-style" extraction mechanics
- Risk/reward balance through contested zones

### Server Authority
- All extraction logic runs on server
- Client can only request/cancel
- Prevents extraction exploits

### Cooldown System
- Point cooldowns prevent camping
- Player cooldowns prevent rapid re-extraction
- Creates tactical decisions about when to extract

### Future Improvements (TODOs)
- Cargo gathering from player ship
- Position validation relative to point
- Tier requirements checking
- Area clear requirements
- Threat counting via nearby ships
