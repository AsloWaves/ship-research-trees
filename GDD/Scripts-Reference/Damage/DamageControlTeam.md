---
tags: [script, damage, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Damage.Controllers
file-path: Assets/Scripts/Damage/Controllers/DamageControlTeam.cs
status: IMPLEMENTED
size: ~533 lines
feature-group: damage
---

# DamageControlTeam.cs

## Quick Reference
**Type**: NetworkBehaviour (per-ship)
**Namespace**: WOS.Damage.Controllers
**File**: `Assets/Scripts/Damage/Controllers/DamageControlTeam.cs`
**Size**: ~533 lines
**Dependencies**: DamageData, DamageController, Mirror

---

## Purpose
Server-authoritative damage control team management. Handles fire fighting, flooding repair, compartment repair, and breach sealing operations. Based on GDD crew management specifications.

---

## Configuration

```csharp
[Header("Team Configuration")]
[SerializeField] private int maxDamageControlTeams = 3;
[SerializeField] private int crewPerTeam = 10;

[Header("Efficiency")]
[SerializeField] private float baseFireFightingRate = 0.1f;  // Intensity/sec
[SerializeField] private float basePumpingRate = 0.05f;      // Flood level/sec
[SerializeField] private float baseRepairRate = 10f;         // Health/sec

[Header("References")]
[SerializeField] private DamageController damageController;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
[SyncVar]
private int availableTeams;
```

---

## Events

```csharp
public event Action<string, DamageControlTaskType> OnTaskStarted;
public event Action<string, DamageControlTaskType> OnTaskCompleted;
public event Action<int> OnTeamsAvailableChanged;
```

---

## Task Types

```csharp
public enum DamageControlTaskType
{
    FireFighting,   // Reduce fire intensity
    Pumping,        // Remove flood water
    Repair,         // Restore compartment health
    SealBreach      // Stop flooding ingress
}
```

---

## Task Assignment Commands

### Fight Fire

```csharp
[Command]
public void CmdFightFire(string compartmentId)
{
    if (availableTeams <= 0) return;
    if (IsTaskActive(compartmentId, DamageControlTaskType.FireFighting)) return;

    var task = new DamageControlTask
    {
        taskId = Guid.NewGuid().ToString(),
        compartmentId = compartmentId,
        taskType = DamageControlTaskType.FireFighting,
        assignedCrew = crewPerTeam,
        progress = 0f,
        startTime = Time.time
    };

    activeTasks.Add(task);
    availableTeams--;

    OnTaskStarted?.Invoke(compartmentId, DamageControlTaskType.FireFighting);
}
```

### Pump Flooding

```csharp
[Command]
public void CmdPumpFlooding(string compartmentId)
{
    if (availableTeams <= 0) return;
    if (IsTaskActive(compartmentId, DamageControlTaskType.Pumping)) return;

    var task = new DamageControlTask
    {
        taskType = DamageControlTaskType.Pumping,
        compartmentId = compartmentId,
        assignedCrew = crewPerTeam
    };

    activeTasks.Add(task);
    availableTeams--;
}
```

### Repair Compartment

```csharp
[Command]
public void CmdRepairCompartment(string compartmentId)
{
    if (availableTeams <= 0) return;
    if (IsTaskActive(compartmentId, DamageControlTaskType.Repair)) return;

    var task = new DamageControlTask
    {
        taskType = DamageControlTaskType.Repair,
        compartmentId = compartmentId,
        assignedCrew = crewPerTeam
    };

    activeTasks.Add(task);
    availableTeams--;
}
```

### Cancel Task

```csharp
[Command]
public void CmdCancelTask(string compartmentId)
{
    for (int i = activeTasks.Count - 1; i >= 0; i--)
    {
        if (activeTasks[i].compartmentId == compartmentId)
        {
            activeTasks.RemoveAt(i);
            availableTeams++;
            OnTeamsAvailableChanged?.Invoke(availableTeams);
            return;
        }
    }
}
```

---

## Task Updates

### Fire Fighting

```csharp
private bool UpdateFireFighting(DamageControlTask task, float deltaTime)
{
    var compartment = GetCompartment(task.compartmentId);
    if (compartment.fireSeverity == FireSeverity.None) return true;

    float efficiency = GetTaskEfficiency(task);
    compartment.fireIntensity -= baseFireFightingRate * efficiency * deltaTime;
    compartment.isBeingFought = true;

    if (compartment.fireIntensity <= 0)
    {
        damageController.ExtinguishFire(task.compartmentId);
        return true; // Task complete
    }

    return false;
}
```

### Pumping

```csharp
private bool UpdatePumping(DamageControlTask task, float deltaTime)
{
    var compartment = GetCompartment(task.compartmentId);
    if (compartment.floodSeverity == FloodSeverity.None) return true;

    float efficiency = GetTaskEfficiency(task);
    float pumpRate = basePumpingRate * efficiency;

    // Net rate = ingress - pumping
    float netRate = compartment.floodRate - pumpRate;
    compartment.floodLevel += netRate * deltaTime;
    compartment.floodLevel = Mathf.Clamp01(compartment.floodLevel);

    if (compartment.floodLevel <= 0)
    {
        compartment.floodSeverity = FloodSeverity.None;
        return true;
    }

    return false;
}
```

### Repair

```csharp
private bool UpdateRepair(DamageControlTask task, float deltaTime)
{
    var compartment = GetCompartment(task.compartmentId);

    // Can't repair if on fire or heavily flooding
    if (compartment.fireSeverity != FireSeverity.None ||
        compartment.floodSeverity >= FloodSeverity.Moderate)
    {
        return false; // Blocked but not complete
    }

    float efficiency = GetTaskEfficiency(task);
    float repairAmount = baseRepairRate * efficiency * deltaTime;

    compartment.currentHealth = Mathf.Min(
        compartment.currentHealth + repairAmount,
        compartment.maxHealth
    );

    // Check if 90% repaired (functional)
    if (compartment.currentHealth >= compartment.maxHealth * 0.9f)
    {
        compartment.isDestroyed = false;
        compartment.isFunctional = true;
        return true;
    }

    return false;
}
```

### Seal Breach

```csharp
private bool UpdateSealBreach(DamageControlTask task, float deltaTime)
{
    float efficiency = GetTaskEfficiency(task);
    task.progress += efficiency * deltaTime * 0.2f; // 5 seconds at full

    if (task.progress >= 1f)
    {
        damageController?.SealFlooding(task.compartmentId);
        return true;
    }

    return false;
}
```

---

## Efficiency System

```csharp
private float GetTaskEfficiency(DamageControlTask task)
{
    float crewRatio = (float)task.assignedCrew / crewPerTeam;
    return crewRatio * crewEfficiencyModifier;
}

public void SetCrewEfficiency(float efficiency)
{
    crewEfficiencyModifier = Mathf.Clamp(efficiency, 0.1f, 2f);
}
```

---

## Crew Casualties

```csharp
[Server]
public void ApplyCrewCasualties(int casualties)
{
    int remaining = casualties;

    foreach (var task in activeTasks)
    {
        int taskCasualties = Mathf.Min(remaining, task.assignedCrew / 2);
        task.assignedCrew -= taskCasualties;
        remaining -= taskCasualties;

        if (remaining <= 0) break;
    }
}
```

---

## Task Data

```csharp
[Serializable]
public class DamageControlTask
{
    public string taskId;
    public string compartmentId;
    public DamageControlTaskType taskType;
    public int assignedCrew;
    public float progress;          // 0-1 for timed tasks
    public float startTime;
}
```

---

## Public API

```csharp
public int GetAvailableTeams();
public int GetMaxTeams();
public List<DamageControlTask> GetActiveTasks();
public bool HasActiveTask(string compartmentId);
```

---

## Base Rates

| Task Type | Base Rate | Description |
|-----------|-----------|-------------|
| Fire Fighting | 0.1 | Intensity reduction/sec |
| Pumping | 0.05 | Flood level reduction/sec |
| Repair | 10 | Health restored/sec |
| Seal Breach | 0.2 | Progress/sec (5s total) |

---

## Integration Points

### Dependencies
- [[DamageController]] - Fire/flood state access
- [[DamageData]] - Severity enums
- Mirror networking

### Used By
- UI damage control panel
- [[CrewManager]] - Efficiency modifier

---

## Related Files
- [[DamageController]] - Damage state management
- [[DamageData]] - Data structures
- [[CrewManager]] - Crew efficiency

---

## Design Notes
- Maximum 3 damage control teams by default
- Teams are consumed while working, freed on completion
- Fire fighting marks compartment as "being fought" (reduces intensity growth)
- Pumping competes against flood rate (net positive = draining)
- Repair blocked by active fire or moderate+ flooding
- Crew casualties reduce team effectiveness
- Efficiency modifier from CrewManager damage control skill
- Tasks can be cancelled and team recovered

