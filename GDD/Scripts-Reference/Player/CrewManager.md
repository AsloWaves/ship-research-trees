# CrewManager.cs

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Player/CrewManager.cs` |
| **Namespace** | `WOS.Player` |
| **Inheritance** | `NetworkBehaviour` (Mirror networking) |
| **Lines of Code** | 834 |
| **Architecture** | Server-authoritative singleton managing Navy Field crew progression |

## Purpose

`CrewManager` is the server-authoritative manager for the Navy Field-style crew progression system. It handles:
- Crew assignment/unassignment to ship positions
- XP gain and level-ups after combat
- Casualty application from combat damage
- Crew recruitment
- PlayFab persistence with optimistic locking

**Key Design**: All crew operations are **server-authoritative** to prevent cheating. Client sends commands, server validates and executes.

## Singleton Pattern

```csharp
private static CrewManager _instance;
public static CrewManager Instance { get; }
```

**Access**: `CrewManager.Instance.CmdAssignCrew(...)`

**Lifecycle**: `DontDestroyOnLoad` - persists across scene changes.

## Configuration

| Field | Type | Description |
|-------|------|-------------|
| `enableDebugLogs` | `bool` | Enable detailed debug logging |
| `startingCredits` | `long` | Starting credits for new players (10,000) |
| `crewRecruitmentCost` | `long` | Cost to recruit new crew (1,000 credits) |

## Server State

### Cached Data

| Cache | Type | Description |
|-------|------|-------------|
| `playerCrewCards` | `Dictionary<string, List<CrewCard>>` | Player ID → Crew roster |
| `playerActiveShips` | `Dictionary<string, PlayerShipData>` | Player ID → Active ship data |
| `crewCardsVersions` | `Dictionary<string, int>` | Optimistic locking versions |
| `dirtyFlags` | `Dictionary<string, bool>` | Track unsaved changes |

## Crew Assignment System

### Assign Crew to Position

```csharp
[Command(requiresAuthority = false)]
public void CmdAssignCrew(string crewId, string positionId,
    NetworkConnectionToClient sender = null)
```

**Purpose**: Client command to assign crew card to ship position.

**Validation**:
1. Player ID lookup from connection
2. Crew cards loaded in cache
3. Active ship exists
4. Crew card exists and not already assigned
5. Position exists on ship
6. Crew classification matches position requirement
7. Crew level meets minimum requirement
8. Total crew weight doesn't exceed ship limit

**On Success**:
- Sets `crew.IsAssigned = true`
- Links crew to ship via `AssignedShipId`
- Updates position with crew stats (name, level, weight)
- Saves to PlayFab
- Sends success RPC to client

**Example Error Messages**:
- "Crew card not found"
- "Crew is already assigned to another position"
- "Engineer required, but this crew is Gunner"
- "Crew Level 5 required, but this crew is Level 3"
- "Adding this crew would exceed ship's crew weight limit"

### Validation Logic

```csharp
[Server]
private bool ValidateCrewAssignment(CrewCard crew, CrewAssignment position,
    PlayerShipData ship, out string errorMessage)
{
    // Check position occupied
    if (!string.IsNullOrEmpty(position.CrewId))
    {
        errorMessage = "Position already occupied";
        return false;
    }

    // Check classification match
    if (crew.Classification != position.Classification)
    {
        errorMessage = $"Need {position.Classification}, got {crew.Classification}";
        return false;
    }

    // Check level requirement
    if (crew.CurrentLevel < position.MinLevel)
    {
        errorMessage = $"Need Level {position.MinLevel}+, got {crew.CurrentLevel}";
        return false;
    }

    // Check weight limit
    float currentCrewWeight = ship.Loadout.GetCrewWeight();
    float newTotalWeight = currentCrewWeight + crew.CrewWeight;
    float maxCrewWeight = 150f; // TODO: Get from ShipDefinitionSO

    if (newTotalWeight > maxCrewWeight)
    {
        errorMessage = "Crew weight limit exceeded";
        return false;
    }

    return true;
}
```

### Unassign Crew from Position

```csharp
[Command(requiresAuthority = false)]
public void CmdUnassignCrew(string crewId, NetworkConnectionToClient sender = null)
```

**Purpose**: Remove crew from ship position.

**Process**:
1. Find crew card by ID
2. Verify crew is actually assigned
3. Find and clear position in ship loadout
4. Clear crew assignment fields
5. Save to PlayFab
6. Send result RPC to client

## Crew Progression System

### Award Combat XP

```csharp
[Server]
public void AddCombatXP(string playerId, int shipTier, int kills,
    float damageDealt, bool victory)
{
    // Calculate base combat XP
    long combatXP = CrewXPCalculator.CalculateCombatXP(shipTier, kills,
        damageDealt, victory);

    // Add XP to all assigned crew on active ship
    List<CrewCard> assignedCrew = crewList.Where(c =>
        c.AssignedShipId == ship.ShipId).ToList();

    foreach (CrewCard crew in assignedCrew)
    {
        int previousLevel = crew.CurrentLevel;
        int levelsGained = crew.AddXP(combatXP);

        if (levelsGained > 0)
        {
            // Log level-up
            DebugManager.Log($"{crew.CrewName} leveled up! " +
                $"{previousLevel} → {crew.CurrentLevel}");

            // Update position in ship loadout
            CrewAssignment position = ship.Loadout.Crew.Find(p =>
                p.CrewId == crew.CrewId);
            if (position != null)
            {
                position.CrewLevel = crew.CurrentLevel;
                position.CrewWeight = crew.CrewWeight;
            }
        }
    }

    // Persist to PlayFab
    SaveCrewCardsToPlayFab(playerId);
}
```

**Purpose**: Server-only method called after combat to award XP to all assigned crew.

**Features**:
- Awards XP to **all crew** on active ship (not just gunners)
- Handles multiple level-ups per combat
- Updates cached position data when crew levels up
- Automatically saves to PlayFab

### Manual XP Addition (Admin)

```csharp
[Command(requiresAuthority = false)]
public void CmdAddCrewXP(string crewId, long xpAmount,
    NetworkConnectionToClient sender = null)
```

**Purpose**: Admin command to manually add XP to crew.

**Security**: Requires **Game Master (Level 2)** admin privileges.

**Process**:
1. Validate admin permissions via `AdminManager`
2. Find crew card
3. Add XP and handle level-ups
4. Update position data if assigned
5. Save to PlayFab
6. Send result RPC to client

**Security Design**: Regular gameplay uses `AddCombatXP()` which is `[Server]` only. Players cannot call this directly - prevents XP exploits.

## Crew Casualty System

### Apply Combat Casualties

```csharp
[Server]
public void ApplyCombatCasualties(string playerId, int shipTier,
    float damagePercent)
{
    // Calculate casualty rate
    float casualtyRate = CrewXPCalculator.CalculateCasualtyRate(shipTier,
        damagePercent);

    if (casualtyRate <= 0f) return; // T1-T3 safe

    // Apply casualties to all assigned crew
    List<CrewCard> assignedCrew = crewList.Where(c =>
        c.AssignedShipId == ship.ShipId).ToList();

    int totalSailorsLost = 0;
    foreach (CrewCard crew in assignedCrew)
    {
        int sailorsLost = crew.ApplyCasualties(casualtyRate);
        totalSailorsLost += sailorsLost;
    }

    SaveCrewCardsToPlayFab(playerId);
}
```

**Purpose**: Server-only method called when ship takes damage in combat.

**Formula**: `casualtyRate = baseTierRate × damagePercent`

**Example**:
- T7 ship (60% base rate)
- 75% damage taken
- Casualty rate = `0.6 × 0.75 = 0.45` (45% of crew killed)

### Manual Casualty Application (Admin)

```csharp
[Command(requiresAuthority = false)]
public void CmdApplyCasualties(string crewId, float casualtyPercent,
    NetworkConnectionToClient sender = null)
```

**Purpose**: Admin command to manually apply casualties.

**Security**: Requires **Game Master (Level 2)** admin privileges.

## Crew Recruitment System

```csharp
[Command(requiresAuthority = false)]
public void CmdRecruitCrew(string crewName, CrewClassification classification,
    NetworkConnectionToClient sender = null)
{
    // Validate crew name
    if (string.IsNullOrWhiteSpace(crewName) || crewName.Length > 100)
    {
        TargetRpcRecruitmentResult(sender, false, "Invalid crew name");
        return;
    }

    // TODO: Check player credits via AccountManager

    // Create new Level 1 crew card
    CrewCard newCrew = new CrewCard
    {
        CrewId = Guid.NewGuid().ToString(),
        PlayerId = playerId,
        CrewName = crewName,
        Classification = classification,
        CurrentLevel = 1,
        CurrentXP = 0,
        IsAssigned = false
    };

    // Calculate stats using Navy Field formulas
    newCrew.RecalculateStats();

    // Add to player's crew collection
    playerCrewCards[playerId].Add(newCrew);

    // Persist to PlayFab
    SaveCrewCardsToPlayFab(playerId);

    TargetRpcRecruitmentResult(sender, true,
        $"Recruited {crewName} as {classification}");
}
```

**Purpose**: Recruit new Level 1 crew card.

**Cost**: 1,000 credits (TODO: implement credit deduction)

**Process**:
1. Validate crew name (max 100 characters)
2. Check player credits (TODO)
3. Create new `CrewCard` with Level 1 stats
4. Add to player's crew roster
5. Save to PlayFab
6. Notify client

## PlayFab Persistence

### Save Crew Cards

```csharp
[Server]
private void SaveCrewCardsToPlayFab(string playerId)
{
    if (!dirtyFlags[playerId]) return; // Skip if no changes

    List<CrewCard> crewCards = playerCrewCards[playerId];
    int currentVersion = crewCardsVersions[playerId];

    playFabCrewService.SaveCrewCards(playerId, crewCards, currentVersion,
        (newVersion, success) =>
    {
        if (success)
        {
            crewCardsVersions[playerId] = newVersion;
            dirtyFlags[playerId] = false;
        }
    });
}
```

**Purpose**: Save crew cards to PlayFab with optimistic locking.

**Optimistic Locking**:
- Each save includes current version number
- PlayFab increments version on successful save
- If version mismatch → reject save (someone else modified data)
- Prevents concurrent modification conflicts

### Load Crew Cards

```csharp
[Server]
public void LoadCrewCardsFromPlayFab(string playerId,
    Action<List<CrewCard>> callback = null)
{
    playFabCrewService.LoadCrewCards(playerId, (crewCards, version, success) =>
    {
        if (success && crewCards != null)
        {
            LoadPlayerCrewCards(playerId, crewCards, version);
            callback?.Invoke(crewCards);
        }
    });
}
```

**Purpose**: Load crew cards from PlayFab on player connect.

### Mark Dirty

```csharp
[Server]
private void MarkDirty(string playerId)
{
    dirtyFlags[playerId] = true;
}
```

**Purpose**: Mark crew data as modified (needs saving).

**Pattern**: All modification methods call `MarkDirty()` then `SaveCrewCardsToPlayFab()`.

## Client RPC Responses

```csharp
[TargetRpc]
private void TargetRpcAssignmentResult(NetworkConnectionToClient conn,
    bool success, string message)

[TargetRpc]
private void TargetRpcXPResult(NetworkConnectionToClient conn, bool success,
    string message, int previousLevel, int newLevel)

[TargetRpc]
private void TargetRpcCasualtyResult(NetworkConnectionToClient conn,
    bool success, string message, int previousSailors, int currentSailors)

[TargetRpc]
private void TargetRpcRecruitmentResult(NetworkConnectionToClient conn,
    bool success, string message)
```

**Purpose**: Send operation results back to requesting client.

**Pattern**: All commands have corresponding RPC for UI feedback.

## Public API (Called by Other Managers)

### Load Player Crew Cards

```csharp
[Server]
public void LoadPlayerCrewCards(string playerId, List<CrewCard> crewCards,
    int version = 1)
{
    playerCrewCards[playerId] = crewCards;
    crewCardsVersions[playerId] = version;
    dirtyFlags[playerId] = false;
}
```

**Purpose**: Load crew roster into cache.

**Called By**: `AccountManager` on player connect or `LoadCrewCardsFromPlayFab()` callback.

### Load Player Active Ship

```csharp
[Server]
public void LoadPlayerActiveShip(string playerId, PlayerShipData ship)
{
    playerActiveShips[playerId] = ship;
}
```

**Purpose**: Cache player's active ship data.

**Called By**: `PlayerShipManager` when active ship changes.

### Unload Player Data

```csharp
[Server]
public void UnloadPlayerData(string playerId)
{
    // Save pending changes
    if (dirtyFlags[playerId])
    {
        SaveCrewCardsToPlayFab(playerId);
    }

    // Remove from caches
    playerCrewCards.Remove(playerId);
    playerActiveShips.Remove(playerId);
    crewCardsVersions.Remove(playerId);
    dirtyFlags.Remove(playerId);
}
```

**Purpose**: Clean up player data on disconnect.

**Called By**: `AccountManager` on player disconnect.

### Query Methods

```csharp
[Server]
public List<CrewCard> GetPlayerCrewCards(string playerId)

[Server]
public List<CrewCard> GetAssignedCrew(string playerId, string shipId)

[Server]
public List<CrewCard> GetUnassignedCrew(string playerId)
```

**Purpose**: Query crew roster for UI display or gameplay logic.

## Integration Points

### Manager References

| Manager | Purpose |
|---------|---------|
| `AccountManager` | Player ID lookup from connection ID |
| `PlayFabCrewService` | Save/load crew cards from PlayFab |
| `AdminManager` | Admin permission validation |

### Related Systems

| System | Integration |
|--------|-------------|
| **Combat System** | Calls `AddCombatXP()` and `ApplyCombatCasualties()` after matches |
| **PlayerShipManager** | Shares active ship cache |
| **CrewCard** | Data model for crew members |
| **ShipLoadout** | Crew assignments stored in loadout |

### Data Flow

```
Client: CmdAssignCrew()
    ↓
Server: Validate (classification, level, weight)
    ↓
Server: Update CrewCard and ShipLoadout
    ↓
Server: SaveCrewCardsToPlayFab()
    ↓
PlayFab: Optimistic locking save
    ↓
Server: TargetRpcAssignmentResult()
    ↓
Client: Update UI
```

## Usage Examples

### Assigning Crew (Client)

```csharp
// Client calls command
CrewManager.Instance.CmdAssignCrew(
    crewId: "crew-uuid-123",
    positionId: "MainBattery1"
);

// Server validates and executes
// Client receives TargetRpcAssignmentResult() with success/failure
```

### Awarding XP After Combat (Server)

```csharp
// Called by combat system after match ends
CrewManager.Instance.AddCombatXP(
    playerId: "player123",
    shipTier: 5,
    kills: 2,
    damageDealt: 50000f,
    victory: true
);

// XP awarded to all assigned crew
// Level-ups automatically handled
// Position data updated
// Saved to PlayFab
```

### Applying Casualties (Server)

```csharp
// Called when ship takes damage
CrewManager.Instance.ApplyCombatCasualties(
    playerId: "player123",
    shipTier: 7,
    damagePercent: 0.75f  // 75% damage
);

// Casualties calculated based on tier and damage
// Crew sailor counts reduced
// Saved to PlayFab
```

### Loading Player Data (Server)

```csharp
// Called by AccountManager when player connects
CrewManager.Instance.LoadCrewCardsFromPlayFab("player123", (crewCards) =>
{
    if (crewCards != null)
    {
        Debug.Log($"Loaded {crewCards.Count} crew cards");
    }
});
```

## Design Notes

### Server-Authoritative Architecture

All crew operations are **server-authoritative**:
- **Commands** (`[Command]`): Client requests, server validates
- **Server methods** (`[Server]`): Server-only execution
- **RPCs** (`[TargetRpc]`): Server → Client responses

This prevents:
- XP hacking (client can't add XP directly)
- Crew duplication exploits
- Invalid crew assignments

### Optimistic Locking

Uses **version numbers** to prevent concurrent modification:
```
Client A: Load crew (version 5)
Client B: Load crew (version 5)
Client A: Save crew (version 5 → 6) ✓ Success
Client B: Save crew (version 5 → 6) ✗ Rejected (version mismatch)
```

Client B must reload and retry to get latest version.

### Dirty Flag Pattern

Tracks **unsaved changes** per player:
- Modification → `MarkDirty(playerId)`
- Save → Clear dirty flag
- Disconnect → Save if dirty

Benefits:
- Avoids redundant saves
- Ensures changes aren't lost
- Batch multiple operations before save

### Cached Active Ship

Shares active ship data with `PlayerShipManager`:
```csharp
playerActiveShips[playerId] = ship;
```

Benefits:
- Avoids duplicate caching
- Single source of truth
- Automatic sync when active ship changes

### Admin Commands Security

Admin commands use **tiered permission system**:
```csharp
int requiredLevel = AdminManager.GetRequiredLevel(AdminPermission.AddCrewXP);
if (!AdminManager.Instance.HasAdminLevelByConnection(connectionId, requiredLevel))
{
    // Blocked - insufficient privileges
    return;
}
```

**Admin Levels**:
- Level 0: Regular player
- Level 1: Moderator
- Level 2: Game Master
- Level 3: Senior GM
- Level 4: Administrator
- Level 5: Owner

### Weight Limit Validation

Currently uses **placeholder value**:
```csharp
float maxCrewWeight = 150f; // TODO: Get from ShipDefinitionSO
```

**Production**: Should load from `ShipDefinitionSO.MaxCrewWeight` based on ship class.

### Crew Name Validation

Prevents abuse:
```csharp
if (string.IsNullOrWhiteSpace(crewName) || crewName.Length > 100)
{
    return; // Invalid
}
```

**Future**: Add profanity filter, reserved name list, duplicate check.

### Position Update After Level-Up

When crew levels up, position cache is updated:
```csharp
position.CrewLevel = crew.CurrentLevel;
position.CrewWeight = crew.CrewWeight;
```

This ensures ship loadout has latest crew stats without reloading.

### Unload Safety

`UnloadPlayerData()` saves before cleanup:
```csharp
if (dirtyFlags[playerId])
{
    SaveCrewCardsToPlayFab(playerId);
}
```

Prevents data loss if player disconnects with unsaved changes.

### Future Enhancements

1. **Credit deduction**: Implement in `CmdRecruitCrew()`
2. **Weight limits**: Load from `ShipDefinitionSO`
3. **Crew portraits**: Add visual customization
4. **Crew traits**: Special abilities per crew
5. **Crew retirement**: Remove old crew for credits
6. **Crew transfer**: Trade crew between players
7. **Crew XP boost items**: Consumables for faster progression
