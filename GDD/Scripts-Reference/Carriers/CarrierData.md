---
tags: [script, carriers, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Carriers.Data
file-path: Assets/Scripts/Carriers/Data/CarrierData.cs
status: IMPLEMENTED
size: ~476 lines
feature-group: carriers
---

# CarrierData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Carriers.Data
**File**: `Assets/Scripts/Carriers/Data/CarrierData.cs`
**Size**: ~476 lines
**Dependencies**: None (standalone data)

---

## Purpose
Carrier operations and aircraft data structures. Includes aircraft types, states, squadrons, air wings, flight deck operations, hangar management, elevator systems, and strike coordination. Based on GDD Carrier-Operations.md specifications.

---

## Aircraft Enums

### AircraftType (10 types)

| Type | Category | Role |
|------|----------|------|
| Fighter | Fighter | Air superiority |
| InterceptorFighter | Fighter | Fast, anti-bomber |
| DiveBomber | Attack | Anti-ship, armor-piercing |
| TorpedoBomber | Attack | Anti-ship, torpedoes |
| LevelBomber | Attack | Area bombing |
| FighterBomber | Multi-Role | Versatile |
| AttackAircraft | Multi-Role | Ground attack |
| Scout | Support | Reconnaissance |
| Spotter | Support | Artillery spotting |
| ASWPatrol | Support | Anti-submarine warfare |

### AircraftState (10 states)

```csharp
public enum AircraftState
{
    Hangar,             // In hangar, not ready
    Preparing,          // Being prepared for launch
    OnDeck,             // Ready on flight deck
    Launching,          // Taking off
    Airborne,           // In flight
    Attacking,          // Engaged in combat
    Returning,          // RTB
    Landing,            // Landing sequence
    Crashed,            // Lost in action
    Damaged             // Requires repair
}
```

### AircraftLoadout (8 types)

```csharp
public enum AircraftLoadout
{
    Empty,              // No weapons
    AirToAir,           // Air superiority
    Bombs,              // General purpose bombs
    ArmorPiercing,      // AP bombs
    Torpedoes,          // Aerial torpedoes
    DepthCharges,       // ASW weapons
    Rockets,            // Unguided rockets
    Mixed               // Multi-role loadout
}
```

---

## Flight Deck Enums

### DeckState (6 states)

```csharp
public enum DeckState
{
    Clear,              // Ready for operations
    LaunchOperations,   // Launching aircraft
    RecoveryOperations, // Recovering aircraft
    Firefighting,       // Deck fire
    Damaged,            // Cannot operate
    Destroyed           // Deck destroyed
}
```

### ElevatorState (7 states)

```csharp
public enum ElevatorState
{
    AtDeck,             // On flight deck
    AtHangar,           // In hangar
    MovingUp,           // Hangar to deck
    MovingDown,         // Deck to hangar
    Damaged,            // Non-operational
    Loading,            // Aircraft embarking
    Unloading           // Aircraft disembarking
}
```

---

## Squadron Enums

### SquadronMission (7 types)

```csharp
public enum SquadronMission
{
    None,               // No active mission
    CombatAirPatrol,    // CAP - defend carrier
    Strike,             // Attack enemy ships
    AntiSubmarine,      // ASW patrol
    Reconnaissance,     // Scout ahead
    Escort,             // Protect strike group
    Intercept           // Attack incoming aircraft
}
```

### StrikePhase (8 phases)

```csharp
public enum StrikePhase
{
    Planning,           // Strike being organized
    Launching,          // Aircraft taking off
    Outbound,           // En route to target
    Attacking,          // Engaged with target
    Egressing,          // Withdrawing from target
    Returning,          // RTB
    Recovery,           // Landing operations
    Complete            // Mission finished
}
```

---

## Aircraft Data

### AircraftInstance

```csharp
[Serializable]
public class AircraftInstance
{
    public string aircraftId;
    public string aircraftDefinitionId;
    public string pilotId;              // Assigned crew member

    // Classification
    public AircraftType type;
    public int tier;

    // State
    public AircraftState state;
    public AircraftLoadout currentLoadout;
    public float health;
    public float maxHealth = 100f;
    public float fuel;
    public float maxFuel = 100f;
    public float ammo;
    public float maxAmmo = 100f;

    // Performance (runtime)
    public float currentAltitude;
    public float currentSpeed;
    public Vector3 currentPosition;
    public float heading;

    // Combat
    public int killCount;
    public float damageDealt;
    public string currentTargetId;

    // Experience
    public int sorties;                 // Missions flown
    public float pilotXP;
}
```

### AircraftDefinition

```csharp
[Serializable]
public class AircraftDefinition
{
    public string definitionId;
    public string displayName;
    public AircraftType type;
    public int tier;

    // Performance
    public float maxSpeed = 300f;       // km/h
    public float cruiseSpeed = 200f;
    public float climbRate = 10f;       // m/s
    public float turnRate = 30f;        // deg/s
    public float range = 500f;          // km
    public float serviceAltitude = 8000f;

    // Combat
    public float firepower = 50f;       // Gun damage
    public float armor = 10f;           // Survivability
    public float accuracy = 0.7f;       // Hit probability

    // Capacity
    public int bombCapacity = 0;
    public int torpedoCapacity = 0;
    public int rocketCapacity = 0;
    public float fuelCapacity = 100f;
    public float ammoCapacity = 100f;

    // Carrier Operations
    public float takeoffTime = 10f;     // Seconds to launch
    public float landingTime = 15f;     // Seconds to recover
    public float serviceTime = 60f;     // Seconds to rearm/refuel
    public int hangarSize = 1;          // Slots required
}
```

---

## Squadron Data

### Squadron

```csharp
[Serializable]
public class Squadron
{
    public string squadronId;
    public string squadronName;
    public string callsign;

    // Configuration
    public AircraftType aircraftType;
    public int maxAircraft = 6;

    // Aircraft
    public List<string> aircraftIds;
    public int readyCount;
    public int airborneCount;
    public int lostCount;

    // Mission
    public SquadronMission currentMission;
    public string missionTargetId;
    public Vector3 missionWaypoint;
    public float missionStartTime;

    // Stats
    public int totalSorties;
    public int totalKills;
    public int totalLosses;
    public float averagePilotXP;
}
```

**Methods**:
- `GetReadyAircraftCount()` - Returns ready aircraft count
- `GetEffectiveness()` - Returns 0-1 effectiveness based on aircraft ratio and experience

### AirWing

```csharp
[Serializable]
public class AirWing
{
    public string airWingId;
    public string carrierShipId;

    // Squadrons
    public List<Squadron> squadrons;
    public int maxSquadrons = 4;

    // Capacity
    public int totalHangarCapacity;
    public int usedHangarCapacity;
    public int totalDeckSpots;

    // Resources
    public float fuelReserve;           // Aviation fuel
    public float ammoReserve;           // Aircraft munitions
    public float sparePartsReserve;     // For repairs
}
```

**Methods**:
- `GetSquadron(string squadronId)` - Returns squadron by ID
- `GetAircraftByType(AircraftType type)` - Returns all aircraft IDs of type

---

## Flight Deck Data

### FlightDeckState

```csharp
[Serializable]
public class FlightDeckState
{
    public string deckId;
    public DeckState state;

    // Capacity
    public int totalSpots = 12;         // Aircraft on deck
    public int usedSpots;
    public int launchSpots = 2;         // Catapults/launch positions
    public int recoverySpots = 1;       // Arresting gear/landing spots

    // Operations
    public List<string> launchQueue;
    public List<string> landingQueue;
    public string currentlyLaunching;
    public string currentlyLanding;

    // Status
    public float deckHealth = 100f;
    public bool hasFire;
    public float fireIntensity;
    public float windOverDeck;          // Important for operations
    public float requiredWindSpeed = 15f;

    // Timing
    public float launchCooldown;
    public float recoveryCooldown;
}
```

### HangarState

```csharp
[Serializable]
public class HangarState
{
    public string hangarId;

    // Capacity
    public int totalSlots = 50;
    public int usedSlots;

    // Aircraft
    public List<string> storedAircraftIds;
    public List<string> servicingAircraftIds;

    // Resources
    public float fuelStorage = 10000f;
    public float ammoStorage = 5000f;
    public float spareParts = 1000f;

    // Status
    public bool hasFire;
    public bool hasExplosion;
    public float hangarHealth = 100f;
}
```

### DeckElevator

```csharp
[Serializable]
public class DeckElevator
{
    public string elevatorId;
    public int elevatorNumber;

    // State
    public ElevatorState state;
    public string loadedAircraftId;
    public float transitionProgress;

    // Configuration
    public float cycleTime = 30f;       // Seconds for full cycle
    public int capacity = 1;            // Aircraft at once
    public Vector3 deckPosition;
    public Vector3 hangarPosition;

    // Status
    public float health = 100f;
    public bool isOperational = true;
}
```

---

## Strike Data

### StrikePackage

```csharp
[Serializable]
public class StrikePackage
{
    public string strikeId;
    public string targetId;
    public string targetName;

    // Composition
    public List<string> strikeSquadronIds;
    public List<string> escortSquadronIds;
    public int totalAircraft;

    // Mission
    public StrikePhase phase;
    public Vector3 targetPosition;
    public float targetBearing;
    public float targetRange;

    // Timing
    public float launchTime;
    public float estimatedTimeOnTarget;
    public float estimatedReturnTime;

    // Results
    public float damageDealt;
    public int aircraftLost;
    public bool missionSuccess;
}
```

### IncomingRaid

```csharp
[Serializable]
public class IncomingRaid
{
    public string raidId;
    public string sourceShipId;

    // Raid Composition
    public int totalAircraft;
    public int fighterCount;
    public int bomberCount;
    public int torpedoBomberCount;

    // Position
    public Vector3 raidPosition;
    public float bearing;
    public float range;
    public float altitude;
    public float estimatedTimeToTarget;

    // Detection
    public float detectionTime;
    public float detectionConfidence;
    public bool isConfirmed;

    // Engagement
    public int aircraftIntercepted;
    public int aircraftDestroyed;
    public bool hasReachedTarget;
}
```

---

## Integration Points

### Dependencies
- None (standalone data)

### Used By
- [[CarrierController]] - Carrier operations
- Aircraft AI systems
- Strike planning UI

---

## Related Files
- [[CarrierController]] - Carrier mechanics
- [[DamageController]] - Deck/hangar damage
- [[SonarSystem]] - ASW patrol integration

---

## Design Notes
- 10 aircraft types covering fighters, bombers, and support
- 10 aircraft states from hangar to crashed
- Squadrons max 6 aircraft each
- Air wings max 4 squadrons
- Flight deck has 12 spots, hangar has 50 slots
- 2 elevators between deck and hangar
- Wind over deck required for operations (15 kts min)
- Strike packages coordinate multiple squadrons
- Incoming raids tracked for CAP intercept
- Fuel consumption during airborne operations
- XP and sorties track pilot experience

