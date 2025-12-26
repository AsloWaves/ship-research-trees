---
tags: [script, crew, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Crew.Data
file-path: Assets/Scripts/Crew/Data/CrewManagementData.cs
status: IMPLEMENTED
size: ~588 lines
feature-group: crew
---

# CrewManagementData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Crew.Data
**File**: `Assets/Scripts/Crew/Data/CrewManagementData.cs`
**Size**: ~588 lines
**Dependencies**: WOS.Player.Data (CrewClassification)

---

## Purpose
Comprehensive data structures for crew management system. Includes crew cards, station assignments, morale/fatigue states, training, recovery, and specialization systems. Based on GDD Crew-Management.md specifications.

---

## Crew Classification Enums

### CrewStation (17 types)

```csharp
public enum CrewStation
{
    // Gunnery
    MainBattery,
    SecondaryBattery,
    AntiAircraft,
    TorpedoTubes,

    // Engineering
    Engine,
    Boiler,
    DamageControl,

    // Navigation
    Bridge,
    Helm,
    Lookout,

    // Special
    FireControl,
    Radar,
    Sonar,
    Communications,

    // Carrier
    FlightDeck,
    Hangar,
    AirTrafficControl,

    // Reserve
    Reserve     // Unassigned, available for casualties
}
```

### MoraleState (5 levels)

```csharp
public enum MoraleState
{
    Broken,     // 0.3x effectiveness
    Low,        // 0.7x effectiveness
    Normal,     // 1.0x effectiveness
    High,       // 1.15x effectiveness
    Heroic      // 1.3x effectiveness (rare)
}
```

### FatigueLevel (5 levels)

```csharp
public enum FatigueLevel
{
    Rested,     // 1.1x effectiveness (<4 hours active)
    Normal,     // 1.0x effectiveness (4-8 hours)
    Tired,      // 0.9x effectiveness (8-12 hours)
    Exhausted,  // 0.7x effectiveness (12-16 hours)
    Critical    // 0.5x effectiveness (16+ hours)
}
```

### CrewEventType

```csharp
public enum CrewEventType
{
    Casualty, LevelUp, SkillGained, MoraleChange,
    FatigueChange, StationAssigned, Promoted,
    Decorated, Wounded, Recovered
}
```

---

## Crew Card Data

### CrewData

```csharp
[Serializable]
public class CrewData
{
    // Identity
    public string Id;
    public string Name;
    public CrewClassification Classification;

    // Progression
    public int Level = 1;
    public int Experience;
    public int ExperienceToNextLevel = 100;

    // Skills (0-50 scale)
    public int Gunnery = 10;
    public int Navigation = 10;
    public int Engineering = 10;
    public int Leadership = 10;
    public int DamageControlSkill = 10;

    // Status
    public bool IsAssigned;
    public string AssignedShipId;

    // Methods
    public float GetEffectiveSkillAverage();
    public void AddExperience(int xp);
    public static CrewData CreateNew(string name, CrewClassification classification);
}
```

### Skill Progression by Classification

| Classification | Level Up Bonuses |
|----------------|------------------|
| Gunner/AAGunner | Gunnery +2, DamageControl +1 |
| Navigator | Navigation +2, Leadership +1 |
| Engineer | Engineering +2, DamageControl +1 |
| DamageControl | DamageControl +2, Engineering +1 |
| FireControl | Gunnery +1, Navigation +1, Leadership +1 |

### XP Formula

```csharp
ExperienceToNextLevel = 100 * Mathf.Pow(targetLevel, 1.3f)
```

---

## Station System

### CrewStationState

```csharp
[Serializable]
public class CrewStationState
{
    // Station Info
    public CrewStation stationType;
    public string stationId;
    public int requiredCrew;
    public int assignedCrew;

    // Performance
    public float efficiency = 1f;
    public float skillModifier = 1f;
    public float equipmentModifier = 1f;

    // Status
    public bool isOperational = true;
    public bool isUnderAttack;
    public int casualties;

    public float GetEffectiveness();
    public int ApplyCasualties(int count);
    public int AssignCrew(int count);
}
```

### Station Effectiveness Formula

```csharp
float crewRatio = assignedCrew / requiredCrew;
float baseEfficiency = Clamp01(crewRatio);
return baseEfficiency * skillModifier * equipmentModifier;
```

---

## Ship Crew Complement

### ShipCrewComplement

```csharp
[Serializable]
public class ShipCrewComplement
{
    // Totals
    public int totalCrew;
    public int maxCrew;
    public int casualties;
    public int reserveCrew;

    // Stations
    public List<CrewStationState> stations;

    // Status
    public MoraleState morale = MoraleState.Normal;
    public FatigueLevel fatigue = FatigueLevel.Normal;
    public float overallEfficiency = 1f;

    public CrewStationState GetStation(CrewStation type);
    public void UpdateOverallEfficiency();
    public float GetMoraleModifier();
    public float GetFatigueModifier();
}
```

---

## Training System

### CrewTrainingData

```csharp
[Serializable]
public class CrewTrainingData
{
    // Current Training
    public string currentSkillTraining;
    public float trainingProgress;          // 0-1
    public float trainingRate;              // Progress per day

    // Training History
    public int totalTrainingSessions;
    public int completedTrainingSessions;
    public List<string> masteredSkills;

    // Bonuses
    public float experienceMultiplier = 1f;
    public float skillGainMultiplier = 1f;
}
```

### PromotionRequirements

```csharp
[Serializable]
public class PromotionRequirements
{
    public int requiredLevel;
    public int requiredBattles;
    public int requiredKills;
    public List<string> requiredSkills;
    public int requiredTrainingSessions;
}
```

---

## Recovery System

### CrewRecoveryData

```csharp
[Serializable]
public class CrewRecoveryData
{
    // Wounded Categories
    public int lightlyWounded;      // Return quickly
    public int seriouslyWounded;    // Return slowly
    public int criticallyWounded;   // May not return

    // Recovery Timers (hours)
    public float lightRecoveryTime;     // Default: 1 hour
    public float seriousRecoveryTime;   // Default: 24 hours
    public float criticalRecoveryTime;  // Default: 168 hours (1 week)

    // Medical
    public bool hasFieldHospital;
    public float medicalEfficiency = 1f;

    public int GetTotalWounded();
    public int ProcessRecovery(float hours);
}
```

### Recovery Rates

| Wound Type | Normal Rate | Field Hospital Rate |
|------------|-------------|---------------------|
| Light | 25% per recovery period | 50% per recovery period |
| Serious | 10% per recovery period | 20% per recovery period |
| Critical | - | - |

---

## Specialization System

### CrewSpecialization

```csharp
[Serializable]
public class CrewSpecialization
{
    public string specializationId;
    public string name;
    public string description;

    // Requirements
    public int requiredLevel;
    public int requiredBattles;
    public List<string> requiredSkills;

    // Bonuses
    public List<SpecializationBonus> bonuses;
}
```

### SpecializationBonus

```csharp
[Serializable]
public class SpecializationBonus
{
    public string statName;
    public float bonusValue;
    public bool isPercentage;
}
```

---

## Transfer System

### CrewTransferData

```csharp
[Serializable]
public class CrewTransferData
{
    public string sourceShipId;
    public string targetShipId;
    public string crewId;
    public bool isTemporary;
    public float transferCost;
    public float returnTime;    // For temporary transfers
}
```

---

## Crew Events

### CrewEvent

```csharp
[Serializable]
public class CrewEvent
{
    public string eventId;
    public CrewEventType eventType;
    public string crewId;
    public string description;
    public float timestamp;

    // Event-specific data
    public int casualtyCount;
    public string stationId;
    public float effectValue;
}
```

---

## Integration Points

### Dependencies
- WOS.Player.Data (CrewClassification enum)

### Used By
- [[CrewManager]] - Crew management controller
- [[DamageController]] - Casualty processing
- [[WeaponController]] - Gunnery efficiency
- [[EquipmentPanel]] - Crew slot UI

---

## Related Files
- [[CrewManager]] - Server-authoritative management
- [[ShipDefinitionSO]] - Crew slot definitions
- [[DamageData]] - Casualty processing

---

## Design Notes
- Skills capped at 50 for balance
- XP formula uses power curve (1.3 exponent)
- Classification affects level-up bonuses
- Morale and fatigue multiply effectiveness
- 17 station types cover all ship systems
- Recovery system allows crew to return after wounds
- Specialization provides additional bonuses

