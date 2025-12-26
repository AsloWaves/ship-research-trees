# NationManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Nations/NationManager.cs` |
| **Namespace** | `WOS.Nations` |
| **Inheritance** | `NetworkBehaviour` |
| **Pattern** | Singleton |
| **Lines** | ~580 |
| **Architecture** | Server-authoritative nation/faction system |

## Purpose
Manages nation/faction system with player assignment, diplomatic relations, reputation tracking, and faction-based PvP rules. Phase 4 feature (disabled by default).

---

## Configuration

### Nation Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `enableNations` | false | Enable nation system |
| `allowNationChoice` | true | Let players choose nation |
| `autoAssignIfNoChoice` | true | Auto-assign if no choice |
| `enableFactionPvP` | true | Faction-based PvP rules |
| `enableReputation` | true | Enable reputation system |

### Reputation Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `startingOwnNationReputation` | 0 | Rep with own nation |
| `startingAlliedReputation` | 0 | Rep with allies |
| `startingNeutralReputation` | 0 | Rep with neutrals |
| `startingEnemyReputation` | -1000 | Rep with enemies |
| `reputationPerEnemyKill` | +100 | Rep for enemy kill |
| `reputationPenaltyAllyKill` | -500 | Rep for ally kill |

---

## Faction Relations

```csharp
public enum FactionRelation
{
    Allied,     // Same faction or formal allies
    Enemy,      // At war
    Neutral     // No formal relations
}
```

### Default Relation Matrix

| Faction | Allies | Axis | Neutral | Pirates |
|---------|--------|------|---------|---------|
| **Allies** | Allied | Enemy | Neutral | Enemy |
| **Axis** | Enemy | Allied | Neutral | Enemy |
| **Neutral** | Neutral | Neutral | Allied | Neutral |
| **Pirates** | Enemy | Enemy | Neutral | Neutral |

---

## Server State

```csharp
// Player nation assignments
private Dictionary<uint, NationID> playerNations;

// Player reputation with each nation
private Dictionary<uint, Dictionary<NationID, int>> playerReputations;

// Pending nation choices (60s timeout)
private Dictionary<uint, DateTime> pendingNationChoices;

// Faction relations matrix
private Dictionary<NationID, Dictionary<NationID, FactionRelation>> factionRelations;
```

---

## Commands

```csharp
// Player chooses their nation
[Command] public void CmdChooseNation(NationID chosenNation)
```

---

## Public API (Server)

### Nation Queries
```csharp
public NationID GetPlayerNation(uint connectionId)
public List<uint> GetPlayersInNation(NationID nationId)
public bool HasNation(uint connectionId)
```

### Relation Queries
```csharp
public FactionRelation GetFactionRelation(NationID nation1, NationID nation2)
public FactionRelation GetPlayerRelation(uint player1, uint player2)
```

### PvP Rules
```csharp
public bool IsPvPAllowed(uint attacker, uint target)
// Returns true if can attack (enemy or neutral, not allied)
```

### Reputation
```csharp
public int GetPlayerReputation(uint connectionId, NationID nationId)
public Dictionary<NationID, int> GetPlayerReputations(uint connectionId)
public void ModifyReputation(uint connectionId, NationID nationId, int amount)
```

### Combat Events
```csharp
public void OnEnemyShipKilled(uint killerId, uint victimId)
// Awards +100 rep for enemy kill, -500 for ally kill
```

---

## PvP Rule Logic

```csharp
[Server]
public bool IsPvPAllowed(uint attacker, uint target)
{
    if (!enableFactionPvP)
        return true;  // No faction rules

    NationID attackerNation = GetPlayerNation(attacker);
    NationID targetNation = GetPlayerNation(target);

    if (attackerNation == NationID.None || targetNation == NationID.None)
        return true;  // No nation = free fire

    FactionRelation relation = GetFactionRelation(attackerNation, targetNation);

    // Can attack enemies, neutrals, and pirate vs pirate
    return relation == FactionRelation.Enemy ||
           relation == FactionRelation.Neutral ||
           (attackerNation == NationID.Pirate && targetNation == NationID.Pirate);
}
```

---

## Player Connection Flow

1. Player connects
2. If `allowNationChoice`: Send nation selection UI (60s timeout)
3. Player chooses or timeout expires
4. If `autoAssignIfNoChoice`: Assign random nation
5. Initialize reputation with all nations

---

## Client RPCs

| RPC | Purpose |
|-----|---------|
| `TargetRequestNationChoice` | Show nation selection UI |
| `TargetNationAssigned` | Confirm nation assignment |
| `TargetReputationChanged` | Notify rep change |
| `TargetNationError` | Show error message |

---

## Usage Example

```csharp
// Check if PvP allowed
if (NationManager.Instance.IsPvPAllowed(attackerId, targetId))
{
    // Allow attack
}

// Get relation between players
var relation = NationManager.Instance.GetPlayerRelation(player1, player2);
if (relation == FactionRelation.Allied)
    Debug.Log("Friendly fire warning!");

// Handle kill
NationManager.Instance.OnEnemyShipKilled(killerId, victimId);

// Get players in faction
var allies = NationManager.Instance.GetPlayersInNation(NationID.Nation1);
```

---

## Integration Points

### Dependencies
- `Mirror` - Networking
- `WOS.Debugging.DebugManager` - Logging

### TODOs
- AccountManager integration for persistence
- Saved nation choice

---

## Design Notes

### Phase 4 Feature
- Disabled by default (`enableNations = false`)
- Placeholder nation names
- Ready for historical/fantasy expansion

### Reputation System
- Per-nation reputation tracking
- Combat affects reputation
- Ally kills heavily penalized (-500)

### Pirate Special Rules
- Enemies with all nations
- Neutral with other pirates
- Can still attack pirates
