---
tags: [script, carriers, controller, networking, implemented]
script-type: NetworkBehaviour
namespace: WOS.Carriers.Controllers
file-path: Assets/Scripts/Carriers/Controllers/CarrierController.cs
status: IMPLEMENTED
size: ~695 lines
feature-group: carriers
---

# CarrierController.cs

## Quick Reference
**Type**: NetworkBehaviour (per-carrier)
**Namespace**: WOS.Carriers.Controllers
**File**: `Assets/Scripts/Carriers/Controllers/CarrierController.cs`
**Size**: ~695 lines
**Dependencies**: CarrierData, Mirror, WOS.Debugging

---

## Purpose
Server-authoritative carrier operations controller. Handles flight deck operations, aircraft launch/recovery, squadron management, elevator operations, strike coordination, and damage. Based on GDD Carrier-Operations.md specifications.

---

## Configuration

```csharp
[Header("Air Wing Configuration")]
[SerializeField] private int maxSquadrons = 4;
[SerializeField] private int hangarCapacity = 50;
[SerializeField] private int deckCapacity = 12;

[Header("Operations")]
[SerializeField] private float launchInterval = 10f;
[SerializeField] private float recoveryInterval = 15f;
[SerializeField] private float serviceTime = 60f;

[Header("Requirements")]
[SerializeField] private float minWindForOperations = 15f;
[SerializeField] private float maxSeaStateForOperations = 6f;

[Header("Debug")]
[SerializeField] private bool enableDebugLogs = false;
```

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnDeckStateChanged))]
private DeckState deckState = DeckState.Clear;

[SyncVar]
private int readyAircraftCount;

[SyncVar]
private int airborneAircraftCount;
```

---

## Events

```csharp
public event Action<string> OnAircraftLaunched;
public event Action<string> OnAircraftRecovered;
public event Action<string> OnAircraftLost;
public event Action<StrikePackage> OnStrikeLaunched;
public event Action<StrikePackage> OnStrikeComplete;
public event Action<DeckState> OnDeckStatusChanged;
public event Action OnDeckFire;
```

---

## Squadron Management

### Create Squadron

```csharp
[Command]
public void CmdCreateSquadron(AircraftType type, string squadronName)
{
    if (airWing.squadrons.Count >= maxSquadrons) return;

    var squadron = new Squadron
    {
        squadronId = Guid.NewGuid().ToString(),
        squadronName = squadronName,
        aircraftType = type,
        maxAircraft = 6
    };

    airWing.squadrons.Add(squadron);
    RpcNotifySquadronCreated(squadron.squadronId, squadronName);
}
```

### Assign Mission

```csharp
[Command]
public void CmdAssignMission(string squadronId, SquadronMission mission, string targetId)
{
    var squadron = airWing.GetSquadron(squadronId);
    if (squadron == null) return;

    squadron.currentMission = mission;
    squadron.missionTargetId = targetId;
    squadron.missionStartTime = Time.time;
}
```

---

## Launch Operations

### Launch Aircraft

```csharp
[Command]
public void CmdLaunchAircraft(string aircraftId)
{
    if (!CanLaunch()) return;

    var aircraft = allAircraft[aircraftId];
    if (aircraft.state != AircraftState.OnDeck)
    {
        // Queue for elevator if in hangar
        if (aircraft.state == AircraftState.Hangar)
        {
            QueueForElevator(aircraftId, toDeck: true);
        }
        return;
    }

    aircraft.state = AircraftState.Launching;
    flightDeck.currentlyLaunching = aircraftId;
    deckState = DeckState.LaunchOperations;
    launchCooldown = launchInterval;

    StartCoroutine(LaunchSequence(aircraft));
}
```

### Launch Sequence

```csharp
private IEnumerator LaunchSequence(AircraftInstance aircraft)
{
    yield return new WaitForSeconds(5f);  // Launch animation

    aircraft.state = AircraftState.Airborne;
    aircraft.sorties++;
    flightDeck.currentlyLaunching = null;
    flightDeck.usedSpots--;
    airborneAircraftCount++;

    if (flightDeck.launchQueue.Count == 0)
    {
        deckState = DeckState.Clear;
    }

    OnAircraftLaunched?.Invoke(aircraft.aircraftId);
    RpcNotifyAircraftLaunched(aircraft.aircraftId);
}
```

### Launch Strike

```csharp
[Command]
public void CmdLaunchStrike(string targetId, List<string> strikeSquadronIds, List<string> escortSquadronIds)
{
    var strike = new StrikePackage
    {
        strikeId = Guid.NewGuid().ToString(),
        targetId = targetId,
        strikeSquadronIds = strikeSquadronIds,
        escortSquadronIds = escortSquadronIds,
        phase = StrikePhase.Launching,
        launchTime = Time.time
    };

    // Queue all aircraft for launch
    foreach (var squadronId in strikeSquadronIds.Concat(escortSquadronIds))
    {
        var squadron = airWing.GetSquadron(squadronId);
        foreach (var aircraftId in squadron.aircraftIds)
        {
            flightDeck.launchQueue.Add(aircraftId);
            strike.totalAircraft++;
        }
    }

    activeStrikes.Add(strike);
    OnStrikeLaunched?.Invoke(strike);
}
```

### Can Launch Check

```csharp
public bool CanLaunch()
{
    if (deckState == DeckState.Damaged || deckState == DeckState.Destroyed)
        return false;

    if (deckState == DeckState.Firefighting)
        return false;

    if (flightDeck.deckHealth < 20f)
        return false;

    if (flightDeck.windOverDeck < minWindForOperations)
        return false;

    if (launchCooldown > 0f)
        return false;

    return true;
}
```

---

## Recovery Operations

### Recover Aircraft

```csharp
[Command]
public void CmdRecoverAircraft(string aircraftId)
{
    if (!CanRecover()) return;

    var aircraft = allAircraft[aircraftId];
    if (aircraft.state != AircraftState.Returning) return;

    aircraft.state = AircraftState.Landing;
    flightDeck.currentlyLanding = aircraftId;
    deckState = DeckState.RecoveryOperations;
    recoveryCooldown = recoveryInterval;

    StartCoroutine(RecoverySequence(aircraft));
}
```

### Recovery Sequence

```csharp
private IEnumerator RecoverySequence(AircraftInstance aircraft)
{
    yield return new WaitForSeconds(8f);  // Landing animation

    // Check for deck space
    if (flightDeck.usedSpots >= flightDeck.totalSpots)
    {
        QueueForElevator(aircraft.aircraftId, toDeck: false);
    }
    else
    {
        flightDeck.usedSpots++;
    }

    aircraft.state = AircraftState.OnDeck;
    flightDeck.currentlyLanding = null;
    airborneAircraftCount--;
    readyAircraftCount++;

    if (flightDeck.landingQueue.Count == 0)
    {
        deckState = DeckState.Clear;
    }

    OnAircraftRecovered?.Invoke(aircraft.aircraftId);
    RpcNotifyAircraftRecovered(aircraft.aircraftId);
}
```

---

## Elevator Operations

```csharp
[Server]
private void QueueForElevator(string aircraftId, bool toDeck)
{
    DeckElevator availableElevator = null;

    foreach (var elevator in elevators)
    {
        if (!elevator.isOperational) continue;

        if (toDeck && elevator.state == ElevatorState.AtHangar)
        {
            availableElevator = elevator;
            break;
        }
        else if (!toDeck && elevator.state == ElevatorState.AtDeck)
        {
            availableElevator = elevator;
            break;
        }
    }

    if (availableElevator != null)
    {
        StartCoroutine(ElevatorCycle(availableElevator, aircraftId, toDeck));
    }
}

private IEnumerator ElevatorCycle(DeckElevator elevator, string aircraftId, bool toDeck)
{
    elevator.loadedAircraftId = aircraftId;
    elevator.state = ElevatorState.Loading;

    yield return new WaitForSeconds(5f);

    elevator.state = toDeck ? ElevatorState.MovingUp : ElevatorState.MovingDown;

    float elapsed = 0f;
    while (elapsed < elevator.cycleTime)
    {
        elapsed += Time.deltaTime;
        elevator.transitionProgress = elapsed / elevator.cycleTime;
        yield return null;
    }

    elevator.state = ElevatorState.Unloading;
    yield return new WaitForSeconds(5f);

    elevator.state = toDeck ? ElevatorState.AtDeck : ElevatorState.AtHangar;
    elevator.loadedAircraftId = null;

    // Update aircraft location
    var aircraft = allAircraft[aircraftId];
    if (toDeck)
    {
        aircraft.state = AircraftState.OnDeck;
        flightDeck.usedSpots++;
        hangar.usedSlots--;
    }
    else
    {
        aircraft.state = AircraftState.Hangar;
        flightDeck.usedSpots--;
        hangar.usedSlots++;
    }
}
```

---

## Update Methods

### Flight Deck Operations

```csharp
[Server]
private void UpdateFlightDeckOperations(float deltaTime)
{
    // Process launch queue
    if (flightDeck.launchQueue.Count > 0 && CanLaunch() &&
        string.IsNullOrEmpty(flightDeck.currentlyLaunching))
    {
        string nextAircraft = flightDeck.launchQueue[0];
        flightDeck.launchQueue.RemoveAt(0);
        CmdLaunchAircraft(nextAircraft);
    }

    // Process landing queue
    if (flightDeck.landingQueue.Count > 0 && CanRecover() &&
        string.IsNullOrEmpty(flightDeck.currentlyLanding))
    {
        string nextAircraft = flightDeck.landingQueue[0];
        flightDeck.landingQueue.RemoveAt(0);
        CmdRecoverAircraft(nextAircraft);
    }
}
```

### Airborne Aircraft

```csharp
[Server]
private void UpdateAirborneAircraft(float deltaTime)
{
    foreach (var aircraft in allAircraft.Values)
    {
        if (aircraft.state != AircraftState.Airborne &&
            aircraft.state != AircraftState.Attacking)
            continue;

        // Consume fuel
        aircraft.fuel -= deltaTime * 0.1f;

        // Check for fuel emergency (<20%)
        if (aircraft.fuel < 20f && aircraft.state != AircraftState.Returning)
        {
            aircraft.state = AircraftState.Returning;
            flightDeck.landingQueue.Add(aircraft.aircraftId);
        }

        // Check for crash (out of fuel)
        if (aircraft.fuel <= 0f)
        {
            aircraft.state = AircraftState.Crashed;
            OnAircraftLost?.Invoke(aircraft.aircraftId);
            airborneAircraftCount--;
        }
    }
}
```

---

## Damage Handling

### Deck Damage

```csharp
[Server]
public void DamageDeck(float damage, bool causeFire)
{
    flightDeck.deckHealth -= damage;

    if (causeFire && !flightDeck.hasFire)
    {
        flightDeck.hasFire = true;
        flightDeck.fireIntensity = 0.5f;
        deckState = DeckState.Firefighting;
        OnDeckFire?.Invoke();
        RpcNotifyDeckFire();
    }

    if (flightDeck.deckHealth <= 0f)
    {
        deckState = DeckState.Destroyed;
    }
    else if (flightDeck.deckHealth < 50f)
    {
        deckState = DeckState.Damaged;
    }
}
```

### Hangar Damage

```csharp
[Server]
public void DamageHangar(float damage, bool causeExplosion)
{
    hangar.hangarHealth -= damage;

    if (causeExplosion)
    {
        hangar.hasExplosion = true;
        // TODO: Destroy aircraft in hangar
    }
}
```

---

## Operation Timings

| Operation | Duration |
|-----------|----------|
| Launch Sequence | 5 seconds |
| Launch Cooldown | 10 seconds |
| Recovery Sequence | 8 seconds |
| Recovery Cooldown | 15 seconds |
| Elevator Loading | 5 seconds |
| Elevator Cycle | 30 seconds |
| Elevator Unloading | 5 seconds |
| Service Time | 60 seconds |

---

## Public API

```csharp
public AirWing GetAirWing();
public FlightDeckState GetFlightDeck();
public HangarState GetHangar();
public int GetReadyAircraftCount();
public int GetAirborneAircraftCount();
public DeckState GetDeckState();
public List<StrikePackage> GetActiveStrikes();
```

---

## Client RPCs

```csharp
[ClientRpc] private void RpcNotifySquadronCreated(string squadronId, string squadronName);
[ClientRpc] private void RpcNotifyAircraftLaunched(string aircraftId);
[ClientRpc] private void RpcNotifyAircraftRecovered(string aircraftId);
[ClientRpc] private void RpcNotifyDeckFire();
```

---

## Integration Points

### Dependencies
- [[CarrierData]] - Data structures
- Mirror networking
- WOS.Debugging

### Used By
- Carrier UI panels
- Strike planning systems
- Combat systems

---

## Related Files
- [[CarrierData]] - Data structures
- [[DamageController]] - Deck/hangar damage integration
- [[SonarSystem]] - ASW patrol coordination

---

## Design Notes
- Server-authoritative with SyncVar synchronization
- Maximum 4 squadrons per carrier
- 50 hangar slots, 12 deck spots
- 2 elevators between hangar and deck
- Wind required for launch/recovery (15 kts min)
- Fuel consumption during flight (0.1/sec)
- Fuel < 20% triggers automatic RTB
- Fuel = 0 causes aircraft crash
- Deck fire blocks operations
- Deck health < 20% blocks launch
- Deck health < 50% marks as damaged
- Strike packages coordinate multiple squadrons
- Launch and recovery have cooldowns

