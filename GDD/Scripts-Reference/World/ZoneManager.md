# ZoneManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/World/Controllers/ZoneManager.cs` |
| **Namespace** | `WOS.World.Controllers` |
| **Inheritance** | `NetworkBehaviour` |
| **Pattern** | Singleton |
| **Lines** | ~563 |
| **Architecture** | Server-authoritative zone management system |

## Purpose
Manages the world's zone system including zone transitions, population tracking, faction control, and dynamic events. Handles server-authoritative validation of zone changes and maintains synchronized state across all clients.

---

## Class Diagram

```
ZoneManager (NetworkBehaviour, Singleton)
├── Zone Registry
│   ├── InitializeZones()
│   ├── GetZone()
│   ├── GetZoneInstance()
│   └── GetAllZones()
├── Zone Transitions
│   ├── CmdRequestZoneTransition()
│   ├── CanTransitionTo()
│   └── ExecuteZoneTransition()
├── Population Tracking
│   ├── UpdateZonePopulations()
│   ├── GetPlayerZone()
│   └── SyncDictionary<zonePopulations>
├── Faction Control
│   ├── UpdateZoneControl()
│   ├── CalculateFactionInfluence()
│   ├── DetermineControlState()
│   └── ReportCombatActivity()
└── Zone Events
    ├── StartZoneEvent()
    ├── EndZoneEvent()
    └── GetZoneEvents()
```

---

## Configuration

### Zone Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `zoneDefinitions` | List | Configured zone definitions |
| `startingZoneId` | "safe_harbor" | Default spawn zone |

### Population Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `maxPlayersPerZone` | 100 | Player capacity per zone |
| `populationUpdateInterval` | 5s | Population sync frequency |

### Control Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `controlUpdateInterval` | 60s | Control state recalculation |
| `controlDecayRate` | 0.1 | Influence decay in contested zones |

---

## Synced State

```csharp
private readonly SyncDictionary<string, int> zonePopulations =
    new SyncDictionary<string, int>();
```

Zone population counts automatically synchronized to all clients.

---

## Events

| Event | Signature | Trigger |
|-------|-----------|---------|
| `OnPlayerZoneChanged` | `Action<string, string>` | Player entered new zone (playerId, zoneId) |
| `OnZoneControlChanged` | `Action<string, ZoneControlState>` | Zone control state changed |
| `OnZoneEventStarted` | `Action<ActiveZoneEvent>` | New zone event began |
| `OnZoneEventEnded` | `Action<string>` | Zone event completed |

---

## Zone Initialization

```csharp
[Server]
private void InitializeZones()
{
    foreach (var zone in zoneDefinitions)
    {
        zoneRegistry[zone.zoneId] = zone;
        zonePopulations[zone.zoneId] = 0;

        zoneInstances[zone.zoneId] = new ZoneInstanceState
        {
            instanceId = Guid.NewGuid().ToString(),
            zoneDefinitionId = zone.zoneId,
            currentControlState = zone.controlState,
            weather = new ZoneWeatherState
            {
                condition = WeatherCondition.Clear,
                seaState = SeaState.Moderate,
                timeOfDay = TimeOfDay.Morning,
                visibility = 10000f
            }
        };
    }
}
```

---

## Zone Transitions

### Request Flow
```csharp
[Command(requiresAuthority = false)]
public void CmdRequestZoneTransition(string targetZoneId,
                                      NetworkConnectionToClient sender = null)
{
    string playerId = sender.connectionId.ToString();
    string currentZone = GetPlayerZone(sender);

    // Validate transition
    if (!CanTransitionTo(currentZone, targetZoneId, out string reason))
    {
        RpcNotifyTransitionFailed(sender.connectionId, reason);
        return;
    }

    // Check zone population capacity
    if (targetInstance.playerCount >= maxPlayersPerZone)
    {
        RpcNotifyTransitionFailed(sender.connectionId, "Zone at capacity");
        return;
    }

    ExecuteZoneTransition(sender, currentZone, targetZoneId);
}
```

### Transition Validation
```csharp
private bool CanTransitionTo(string fromZone, string toZone, out string reason)
{
    // Check zone exists
    if (!zoneRegistry.TryGetValue(toZone, out var targetDef))
    {
        reason = "Unknown zone";
        return false;
    }

    // Check zones are connected
    if (!sourceDef.connectedZoneIds.Contains(toZone))
    {
        reason = "Zones not connected";
        return false;
    }

    // TODO: Check tier requirements
    // TODO: Check faction standing
    // TODO: Check ship can enter zone

    return true;
}
```

### Execute Transition
```csharp
[Server]
private void ExecuteZoneTransition(NetworkConnectionToClient conn,
                                    string fromZone, string toZone)
{
    // Update old zone population
    if (oldInstance != null)
    {
        oldInstance.playerCount--;
        zonePopulations[fromZone] = oldInstance.playerCount;
    }

    // Update new zone population
    newInstance.playerCount++;
    zonePopulations[toZone] = newInstance.playerCount;

    // Track player zone
    playerZones[conn] = toZone;

    OnPlayerZoneChanged?.Invoke(playerId, toZone);
    RpcNotifyZoneEntered(conn.connectionId, toZone);
}
```

---

## Faction Control System

### Control State Determination
```csharp
[Server]
private void DetermineControlState(string zoneId, ZoneInstanceState instance,
                                    ZoneDefinition definition)
{
    // Find dominant faction
    Faction dominant = Faction.Independent;
    float highestInfluence = 0f;
    float secondHighest = 0f;

    foreach (var kvp in instance.factionInfluence)
    {
        if (kvp.Value > highestInfluence)
        {
            secondHighest = highestInfluence;
            highestInfluence = kvp.Value;
            dominant = kvp.Key;
        }
    }

    // Determine state based on influence
    ZoneControlState newState;
    if (highestInfluence < 20f)
        newState = ZoneControlState.Neutral;
    else if (highestInfluence - secondHighest < 20f)
        newState = ZoneControlState.Contested;
    else if (highestInfluence >= 80f)
        newState = ZoneControlState.Occupied;
    else
        newState = ZoneControlState.Controlled;
}
```

### Control Thresholds
| Influence | State | Faction Assignment |
|-----------|-------|-------------------|
| < 20% | Neutral | None |
| 20%+ (close) | Contested | None |
| 20-80% (dominant) | Controlled | Dominant faction |
| 80%+ | Occupied | Dominant faction |

### Combat Activity Reporting
```csharp
[Server]
public void ReportCombatActivity(string zoneId, Faction faction, float impact)
{
    if (!instance.factionInfluence.ContainsKey(faction))
        instance.factionInfluence[faction] = 0f;

    instance.factionInfluence[faction] += impact;
    instance.factionInfluence[faction] = Mathf.Min(100f, influence);
}
```

### Control Decay
```csharp
[Server]
private void ApplyControlDecay(ZoneInstanceState instance)
{
    // Decay all faction influence in contested zones
    foreach (var faction in instance.factionInfluence.Keys)
    {
        instance.factionInfluence[faction] *= (1f - controlDecayRate);
    }
}
```

---

## Zone Events

### Starting Events
```csharp
[Server]
public void StartZoneEvent(string zoneId, ActiveZoneEvent zoneEvent)
{
    var instance = GetZoneInstance(zoneId);

    zoneEvent.startTime = Time.time;
    instance.activeEvents.Add(zoneEvent);

    OnZoneEventStarted?.Invoke(zoneEvent);
    RpcNotifyZoneEventStarted(zoneId, zoneEvent.eventId, zoneEvent.eventName);
}
```

### Ending Events
```csharp
[Server]
public void EndZoneEvent(string zoneId, string eventId)
{
    var zoneEvent = instance.activeEvents.Find(e => e.eventId == eventId);
    instance.activeEvents.Remove(zoneEvent);

    OnZoneEventEnded?.Invoke(eventId);
    RpcNotifyZoneEventEnded(zoneId, eventId);
}
```

---

## Public API

### Zone Queries
```csharp
// Get zone definition by ID
public ZoneDefinition GetZone(string zoneId)

// Get zone instance state
public ZoneInstanceState GetZoneInstance(string zoneId)

// Get all zones
public List<ZoneDefinition> GetAllZones()

// Get zones by danger level
public List<ZoneDefinition> GetZonesByDangerLevel(ZoneDangerLevel level)

// Get zones suitable for ship tier
public List<ZoneDefinition> GetZonesForTier(int tier)
```

### Player Queries
```csharp
// Get player's current zone
public string GetPlayerZone(NetworkConnectionToClient conn)

// Get starting zone ID
public string GetStartingZoneId()
```

### Population Queries
```csharp
// Get current zone population
public int GetZonePopulation(string zoneId)

// Get max players per zone
public int GetMaxPlayersPerZone()
```

### Event Queries
```csharp
// Get active events in zone
public List<ActiveZoneEvent> GetZoneEvents(string zoneId)
```

---

## Network RPCs

### Targeted RPCs
| RPC | Purpose |
|-----|---------|
| `RpcNotifyTransitionFailed` | Deny zone transition with reason |
| `RpcNotifyZoneEntered` | Confirm zone entry, trigger load |

### Broadcast RPCs
| RPC | Purpose |
|-----|---------|
| `RpcNotifyZoneControlChanged` | Zone control state update |
| `RpcNotifyZoneEventStarted` | New event notification |
| `RpcNotifyZoneEventEnded` | Event completion notification |

---

## Update Loop

```csharp
private void Update()
{
    if (!isServer) return;

    // Population sync (every 5 seconds)
    populationTimer += Time.deltaTime;
    if (populationTimer >= populationUpdateInterval)
    {
        populationTimer = 0f;
        UpdateZonePopulations();
    }

    // Control recalculation (every 60 seconds)
    controlTimer += Time.deltaTime;
    if (controlTimer >= controlUpdateInterval)
    {
        controlTimer = 0f;
        UpdateZoneControl();
    }
}
```

---

## Usage Example

```csharp
// Request zone transition
ZoneManager.Instance.CmdRequestZoneTransition("combat_zone_alpha");

// Get current zone
string currentZone = ZoneManager.Instance.GetPlayerZone(connection);

// Check zone population
int pop = ZoneManager.Instance.GetZonePopulation("harbor_01");
int max = ZoneManager.Instance.GetMaxPlayersPerZone();
Debug.Log($"Zone population: {pop}/{max}");

// Get zones for ship tier
List<ZoneDefinition> availableZones = ZoneManager.Instance.GetZonesForTier(5);

// Report combat for faction control
ZoneManager.Instance.ReportCombatActivity("contested_waters", Faction.Atlantic, 15f);

// Start a zone event
var event = new ActiveZoneEvent
{
    eventId = Guid.NewGuid().ToString(),
    eventName = "Convoy Defense",
    duration = 1800f  // 30 minutes
};
ZoneManager.Instance.StartZoneEvent("shipping_lane", event);
```

---

## Integration Points

### Dependencies
- `WOS.World.Data` - Data structures
- `WOS.Debugging.DebugManager` - Logging
- `Mirror` - Networking

### Integrates With
- `WeatherSystem` - Zone-specific weather
- `PermadeathManager` - Risk zone penalties
- `ExtractionController` - Extraction point zones
- Ship systems - Tier-based zone access

---

## Design Notes

### Zone Connectivity
- Zones must be explicitly connected
- Prevents arbitrary teleportation
- Creates strategic chokepoints

### Faction Control Mechanics
- Player combat contributes to faction influence
- Contested zones decay all influence over time
- Creates dynamic territory control

### Population Management
- Capacity limits per zone
- Synchronized population counts
- Prevents zone overcrowding

### Future Improvements (TODOs)
- Tier requirement validation
- Faction standing checks
- Ship type restrictions
