---
tags: [script, submarines, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Submarines.Data
file-path: Assets/Scripts/Submarines/Data/SubmarineData.cs
status: IMPLEMENTED
size: ~382 lines
feature-group: submarines
---

# SubmarineData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Submarines.Data
**File**: `Assets/Scripts/Submarines/Data/SubmarineData.cs`
**Size**: ~382 lines
**Dependencies**: None (standalone data)

---

## Purpose
Submarine warfare data structures. Includes depth states, operating modes, sonar systems, torpedo mechanics, and depth charge attacks. Based on GDD Submarine-Warfare.md specifications.

---

## Depth & Mode Enums

### DepthState (7 states)

| State | Depth (m) | Description |
|-------|-----------|-------------|
| Surfaced | <1 | Full speed, visible |
| PeriscopeDepth | 10-15 | Can use periscope, partially visible |
| ShallowDepth | 20-40 | Normal submerged operations |
| OperatingDepth | 40-100 | Optimal for most operations |
| DeepDepth | 100-200 | Reduced detection, some damage |
| CrushDepth | 200+ | Taking progressive hull damage |
| Destroyed | - | Hull collapsed |

### SubmarineMode (5 modes)

```csharp
public enum SubmarineMode
{
    Surface,    // Diesel engines, fast, visible
    Snorkel,    // Diesel at periscope depth
    Electric,   // Battery power, silent
    Silent,     // Ultra-quiet, minimum systems
    Emergency   // Emergency blow, rapid surface
}
```

---

## Sonar Enums

### SonarType (4 types)

```csharp
public enum SonarType
{
    PassiveSonar,   // Listening only, no detection risk
    ActiveSonar,    // Ping, high detection, accurate bearing
    PassiveArray,   // Towed array for extended range
    Hydrophone      // Fixed position underwater sensor
}
```

### ContactClassification (7 types)

```csharp
public enum ContactClassification
{
    Unknown,        // Unidentified contact
    Merchant,       // Civilian vessel
    Warship,        // Surface combatant
    Submarine,      // Underwater contact
    Torpedo,        // Incoming weapon
    Biologic,       // Marine life
    Environmental   // Weather/water noise
}
```

---

## Torpedo Enums

### TorpedoGuidance (5 types)

```csharp
public enum TorpedoGuidance
{
    Unguided,       // Straight-running
    PassiveHoming,  // Homes on target noise
    ActiveHoming,   // Onboard active sonar
    WireGuided,     // Operator-controlled via wire
    WakeHoming      // Follows ship's wake
}
```

### TorpedoWarhead (4 types)

```csharp
public enum TorpedoWarhead
{
    Contact,    // Detonates on impact
    Magnetic,   // Detonates under keel
    Proximity,  // Detonates near target
    Nuclear     // Special/event only
}
```

### TorpedoTubeState (6 states)

```csharp
public enum TorpedoTubeState
{
    Empty,      // No torpedo loaded
    Loading,    // Reload in progress
    Ready,      // Loaded, ready to fire
    Flooded,    // Outer door open
    Firing,     // Launch in progress
    Damaged     // Cannot operate
}
```

---

## Submarine State Data

### SubmarineState

```csharp
[Serializable]
public class SubmarineState
{
    // Depth
    public float currentDepth;
    public float targetDepth;
    public DepthState depthState;
    public float maxOperatingDepth = 150f;
    public float crushDepth = 250f;

    // Power
    public SubmarineMode operatingMode;
    public float batteryCharge;         // 0-100%
    public float maxBatteryCapacity = 100f;
    public float batteryDrainRate;
    public float dieselFuel;            // 0-100%

    // Atmosphere
    public float oxygenLevel;           // 0-100%
    public float co2Level;              // Dangerous above 3%
    public float maxDiveTime;

    // Stealth
    public float noiseLevel;
    public float thermalSignature;
    public bool isCavitating;           // Propeller noise

    // Buoyancy
    public float buoyancy;              // -1 to +1
    public float trim;                  // Bow angle
    public float ballastLevel;          // 0-100%
}
```

### SubmarineStats

```csharp
[Serializable]
public class SubmarineStats
{
    // Depth Performance
    public float testDepth = 150f;
    public float crushDepth = 250f;
    public float diveRate = 2f;         // m/s
    public float surfaceRate = 3f;      // Emergency blow

    // Power Systems
    public float batteryCapacity = 100f;
    public float dieselRechargeRate = 5f;   // %/min on diesel
    public float electricConsumption = 1f;
    public float silentModeMultiplier = 0.3f;

    // Stealth
    public float baseNoiseLevel = 50f;
    public float surfaceNoiseMultiplier = 2f;
    public float silentNoiseMultiplier = 0.2f;
    public float cavitationSpeed = 15f;     // Knots

    // Atmosphere
    public float oxygenConsumption = 0.1f;  // /min/crew
    public float co2Production = 0.05f;
    public float scrubberEfficiency = 0.8f;
}
```

---

## Sonar Data

### SonarContact

```csharp
[Serializable]
public class SonarContact
{
    public string contactId;
    public string targetNetId;

    // Detection
    public ContactClassification classification;
    public float confidence;            // 0-1
    public float signalStrength;

    // Position
    public float bearing;               // Degrees
    public float estimatedRange;        // Meters
    public float estimatedDepth;
    public Vector3 lastKnownPosition;

    // Movement
    public float estimatedSpeed;        // Knots
    public float estimatedCourse;       // Degrees
    public bool isClosing;

    // Tracking
    public float firstDetectedTime;
    public float lastUpdateTime;
    public bool isLostContact;
    public int trackNumber;
}
```

### SonarConfig

```csharp
[Serializable]
public class SonarConfig
{
    // Passive
    public float passiveRange = 5000f;
    public float passiveBearingAccuracy = 5f;   // Degrees
    public float passiveUpdateRate = 2f;        // Seconds

    // Active
    public float activeRange = 15000f;
    public float activeBearingAccuracy = 1f;
    public float activeRangeAccuracy = 50f;     // Meters
    public float activePingCooldown = 30f;
    public float activePingDetectionRange = 20000f;

    // Detection Modifiers
    public float depthLayerPenalty = 0.3f;      // Thermocline
    public float noiseFloorThreshold = 20f;
}
```

---

## Torpedo Data

### TorpedoTube

```csharp
[Serializable]
public class TorpedoTube
{
    public string tubeId;
    public int tubeNumber;              // 1-6 typically

    // State
    public TorpedoTubeState state;
    public string loadedTorpedoId;
    public float reloadProgress;        // 0-1
    public float reloadTime = 30f;      // Seconds

    // Configuration
    public Vector3 tubePosition;
    public float tubeAngle;
    public bool isBowTube;
}
```

### FiringSolution

```csharp
[Serializable]
public class FiringSolution
{
    public string targetId;
    public string targetName;

    // Target Data
    public Vector3 targetPosition;
    public float targetBearing;
    public float targetRange;
    public float targetSpeed;
    public float targetCourse;
    public float targetDepth;

    // Solution
    public float interceptBearing;
    public float interceptRange;
    public float runTime;               // Expected run time
    public float hitProbability;        // 0-1
    public bool isValidSolution;

    // Settings
    public float torpedoRunDepth = 5f;
    public bool enablePatternRun;
    public float spreadAngle = 0f;
}
```

---

## Depth Charge Data

### DepthCharge

```csharp
[Serializable]
public class DepthCharge
{
    public string chargeId;
    public Vector3 dropPosition;
    public float setDepth;              // Detonation depth
    public float sinkRate = 3f;         // m/s
    public float currentDepth;
    public bool hasDetonated;
    public float damage = 500f;
    public float blastRadius = 30f;
}
```

### DepthChargePattern (5 patterns)

```csharp
public enum DepthChargePattern
{
    Single,         // One charge
    Diamond,        // 4-charge diamond
    Ladder,         // Line pattern
    FullPattern,    // Maximum coverage
    Hedgehog        // Forward-thrown pattern
}
```

---

## Integration Points

### Dependencies
- None (standalone data)

### Used By
- [[SubmarineController]] - Submarine mechanics
- [[SonarSystem]] - Sonar detection
- [[TorpedoController]] - Torpedo operations

---

## Related Files
- [[SubmarineController]] - Submarine mechanics
- [[SonarSystem]] - Sonar system
- [[TorpedoDefinitionSO]] - Torpedo configuration

---

## Design Notes
- 7 depth states from surface to destruction
- 5 operating modes with different power/stealth tradeoffs
- Battery power is limited, diesel recharges
- Cavitation occurs at high speed, increases noise
- Active sonar reveals submarine position
- Firing solutions calculate intercept point
- Depth charges have multiple attack patterns

