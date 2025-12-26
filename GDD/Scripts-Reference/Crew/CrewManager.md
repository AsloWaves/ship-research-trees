---
tags: [script, crew, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Crew.Controllers
file-path: Assets/Scripts/Crew/Controllers/CrewManager.cs
status: IMPLEMENTED
size: ~615 lines
feature-group: crew
---

# CrewManager.cs

## Quick Reference
**Type**: NetworkBehaviour (per-ship)
**Namespace**: WOS.Crew.Controllers
**File**: `Assets/Scripts/Crew/Controllers/CrewManager.cs`
**Size**: ~615 lines
**Dependencies**: CrewManagementData, Mirror, WOS.Player.Data

---

## Purpose
Server-authoritative crew management for individual ships. Handles crew card assignment, station efficiency, morale/fatigue systems, casualties, and experience progression. Based on GDD Crew-Management.md specifications.

---

## Configuration

```csharp
[Header("Configuration")]
[SerializeField] private int baseCrewCapacity = 500;
[SerializeField] private float moraleDecayRate = 0.01f;     // Per hour in combat
[SerializeField] private float fatigueGainRate = 0.05f;     // Per hour active

[Header("Station Definitions")]
[SerializeField] private List<StationDefinition> stationDefinitions;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
[SyncVar] private int totalCrew;
[SyncVar] private int availableCrew;
[SyncVar] private MoraleState moraleState = MoraleState.Normal;
[SyncVar] private FatigueLevel fatigueLevel = FatigueLevel.Normal;
[SyncVar] private float overallEfficiency = 1f;
```

---

## Events

```csharp
public event Action<int, int> OnCrewChanged;                    // current, max
public event Action<MoraleState> OnMoraleChanged;
public event Action<FatigueLevel> OnFatigueChanged;
public event Action<CrewStation, float> OnStationEfficiencyChanged;
public event Action<int> OnCasualtiesTaken;
public event Action<CrewEvent> OnCrewEvent;
```

---

## Initialization

```csharp
[Server]
private void InitializeCrewComplement()
{
    crewComplement = new ShipCrewComplement
    {
        maxCrew = baseCrewCapacity,
        totalCrew = baseCrewCapacity,
        reserveCrew = baseCrewCapacity
    };

    // Initialize stations from definitions
    foreach (var def in stationDefinitions)
    {
        var station = new CrewStationState
        {
            stationType = def.stationType,
            stationId = def.stationId,
            requiredCrew = def.requiredCrew,
            assignedCrew = 0,
            isOperational = true
        };
        crewComplement.stations.Add(station);
    }

    // Recovery timers
    recoveryData = new CrewRecoveryData
    {
        lightRecoveryTime = 1f,     // 1 hour
        seriousRecoveryTime = 24f,  // 1 day
        criticalRecoveryTime = 168f // 1 week
    };

    AutoAssignCrew();
}
```

---

## Crew Card System

### Assign Crew Card

```csharp
[Server]
public bool AssignCrewCard(CrewData crewCard)
{
    // Check for duplicate
    foreach (var existing in assignedCrewCards)
    {
        if (existing.Id == crewCard.Id) return false;
    }

    assignedCrewCards.Add(crewCard);
    ApplyCrewCardBonuses(crewCard);
    return true;
}
```

### Crew Card Bonuses

```csharp
private void ApplyCrewCardBonuses(CrewData crewCard)
{
    var primaryStation = GetPrimaryStation(crewCard.Classification);

    if (primaryStation != null)
    {
        // Normalize skill average to 0-1
        float skillBonus = crewCard.GetEffectiveSkillAverage() / 50f;
        primaryStation.skillModifier = Mathf.Max(primaryStation.skillModifier, skillBonus);
    }

    UpdateEfficiency();
}
```

### Classification to Station Mapping

```csharp
private CrewStationState GetPrimaryStation(CrewClassification classification)
{
    CrewStation targetStation = classification switch
    {
        CrewClassification.Gunner => CrewStation.MainBattery,
        CrewClassification.AAGunner => CrewStation.AntiAircraft,
        CrewClassification.Engineer => CrewStation.Engine,
        CrewClassification.Navigator => CrewStation.Bridge,
        CrewClassification.DamageControl => CrewStation.DamageControl,
        CrewClassification.FireControl => CrewStation.FireControl,
        _ => CrewStation.Reserve
    };

    return crewComplement.GetStation(targetStation);
}
```

---

## Station Assignment

### Auto-Assign Crew

```csharp
[Server]
public void AutoAssignCrew()
{
    // Reset all stations
    foreach (var station in crewComplement.stations)
    {
        crewComplement.reserveCrew += station.assignedCrew;
        station.assignedCrew = 0;
    }

    // Priority order (vital stations first)
    var priorityOrder = new List<CrewStation>
    {
        CrewStation.Engine,
        CrewStation.Bridge,
        CrewStation.Helm,
        CrewStation.MainBattery,
        CrewStation.DamageControl,
        CrewStation.SecondaryBattery,
        CrewStation.AntiAircraft,
        CrewStation.TorpedoTubes,
        CrewStation.FireControl,
        CrewStation.Radar,
        CrewStation.Lookout
    };

    foreach (var stationType in priorityOrder)
    {
        var station = crewComplement.GetStation(stationType);
        if (station == null) continue;

        int toAssign = Mathf.Min(station.requiredCrew, crewComplement.reserveCrew);
        station.AssignCrew(toAssign);
        crewComplement.reserveCrew -= toAssign;
    }

    UpdateEfficiency();
}
```

### Manual Assignment

```csharp
[Command]
public void CmdAssignCrewToStation(CrewStation stationType, int count)
{
    var station = crewComplement.GetStation(stationType);
    if (station == null) return;

    int toAssign = Mathf.Min(count, crewComplement.reserveCrew);
    int assigned = station.AssignCrew(toAssign);

    crewComplement.reserveCrew -= assigned;
    availableCrew = crewComplement.reserveCrew;

    OnStationEfficiencyChanged?.Invoke(stationType, station.GetEffectiveness());
    UpdateEfficiency();
}
```

---

## Casualty System

```csharp
[Server]
public void ApplyCasualties(int count, CrewStation? targetStation = null)
{
    int remaining = count;

    // Target specific station first
    if (targetStation.HasValue)
    {
        var station = crewComplement.GetStation(targetStation.Value);
        if (station != null)
        {
            remaining -= station.ApplyCasualties(remaining);
        }
    }

    // Apply to reserve
    if (remaining > 0 && crewComplement.reserveCrew > 0)
    {
        int fromReserve = Mathf.Min(remaining, crewComplement.reserveCrew);
        crewComplement.reserveCrew -= fromReserve;
        remaining -= fromReserve;
    }

    // Spread across stations
    if (remaining > 0)
    {
        foreach (var station in crewComplement.stations)
        {
            if (remaining <= 0) break;
            remaining -= station.ApplyCasualties(remaining);
        }
    }

    // Process wounded (30% killed, 30% serious, 40% light)
    int actualCasualties = count - remaining;
    int killed = Mathf.FloorToInt(actualCasualties * 0.3f);
    int serious = Mathf.FloorToInt(actualCasualties * 0.3f);
    int light = actualCasualties - killed - serious;

    recoveryData.lightlyWounded += light;
    recoveryData.seriouslyWounded += serious;

    UpdateMoraleFromCasualties(actualCasualties);
    OnCasualtiesTaken?.Invoke(actualCasualties);
}
```

### Casualty Distribution

| Outcome | Percentage |
|---------|------------|
| Killed | 30% |
| Seriously Wounded | 30% |
| Lightly Wounded | 40% |

---

## Morale System

### Morale Modifiers

| State | Effectiveness Modifier |
|-------|------------------------|
| Broken | 0.3x |
| Low | 0.7x |
| Normal | 1.0x |
| High | 1.15x |
| Heroic | 1.3x |

```csharp
[Server]
public void IncreaseMorale()
{
    MoraleState newState = moraleState switch
    {
        MoraleState.Broken => MoraleState.Low,
        MoraleState.Low => MoraleState.Normal,
        MoraleState.Normal => MoraleState.High,
        MoraleState.High => MoraleState.Heroic,
        _ => moraleState
    };
    SetMorale(newState);
}

[Server]
public void DecreaseMorale()
{
    MoraleState newState = moraleState switch
    {
        MoraleState.Heroic => MoraleState.High,
        MoraleState.High => MoraleState.Normal,
        MoraleState.Normal => MoraleState.Low,
        MoraleState.Low => MoraleState.Broken,
        _ => moraleState
    };
    SetMorale(newState);
}
```

---

## Fatigue System

```csharp
private void UpdateFatigue(float deltaTime)
{
    activeTime += deltaTime;
    float hoursPassed = activeTime / 3600f;

    FatigueLevel newFatigue = hoursPassed switch
    {
        < 4f => FatigueLevel.Rested,
        < 8f => FatigueLevel.Normal,
        < 12f => FatigueLevel.Tired,
        < 16f => FatigueLevel.Exhausted,
        _ => FatigueLevel.Critical
    };

    if (newFatigue != fatigueLevel)
    {
        fatigueLevel = newFatigue;
        OnFatigueChanged?.Invoke(newFatigue);
        UpdateEfficiency();
    }
}
```

### Fatigue Modifiers

| Level | Hours Active | Effectiveness |
|-------|--------------|---------------|
| Rested | <4 | 1.1x |
| Normal | 4-8 | 1.0x |
| Tired | 8-12 | 0.9x |
| Exhausted | 12-16 | 0.7x |
| Critical | 16+ | 0.5x |

---

## Experience System

```csharp
[Server]
public void AwardExperience(int xp)
{
    foreach (var crewCard in assignedCrewCards)
    {
        int oldLevel = crewCard.Level;
        crewCard.AddExperience(xp);

        if (crewCard.Level > oldLevel)
        {
            OnCrewEvent?.Invoke(new CrewEvent
            {
                eventType = CrewEventType.LevelUp,
                crewId = crewCard.Id,
                effectValue = crewCard.Level,
                timestamp = Time.time
            });
        }
    }

    UpdateEfficiency();
}
```

---

## Public API

```csharp
public int GetTotalCrew();
public int GetAvailableCrew();
public int GetCasualties();
public MoraleState GetMorale();
public FatigueLevel GetFatigue();
public float GetOverallEfficiency();
public ShipCrewComplement GetCrewComplement();
public List<CrewData> GetAssignedCrewCards();
public float GetStationEfficiency(CrewStation stationType);
public float GetSystemModifier(string system);
```

### System Modifiers

```csharp
public float GetSystemModifier(string system)
{
    return system switch
    {
        "gunnery" => GetStationEfficiency(CrewStation.MainBattery),
        "engineering" => GetStationEfficiency(CrewStation.Engine),
        "navigation" => GetStationEfficiency(CrewStation.Bridge),
        "damage_control" => GetStationEfficiency(CrewStation.DamageControl),
        "fire_control" => GetStationEfficiency(CrewStation.FireControl),
        _ => overallEfficiency
    };
}
```

---

## Station Definition

```csharp
[Serializable]
public class StationDefinition
{
    public CrewStation stationType;
    public string stationId;
    public int requiredCrew;
    public int priority;
}
```

---

## Integration Points

### Dependencies
- [[CrewManagementData]] - Data structures and enums
- Mirror networking
- WOS.Debugging

### Used By
- [[DamageController]] - Applies casualties
- [[WeaponController]] - Gets gunnery efficiency
- [[NetworkedNavalController]] - Gets navigation efficiency
- [[DamageControlTeam]] - Gets damage control efficiency

---

## Related Files
- [[CrewManagementData]] - Data structures
- [[ShipDefinitionSO]] - Station configuration
- [[DamageData]] - Casualty integration

---

## Design Notes
- Server-authoritative with SyncVar synchronization
- Crew cards provide skill bonuses to primary stations
- Auto-assign prioritizes vital stations
- Casualties reduce station effectiveness
- Morale and fatigue multiply all effectiveness
- Experience awarded to all assigned crew cards
- System modifiers used by other controllers

