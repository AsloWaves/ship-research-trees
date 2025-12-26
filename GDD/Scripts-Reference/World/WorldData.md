# WorldData.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/World/Data/WorldData.cs` |
| **Namespace** | `WOS.World.Data` |
| **Lines** | ~499 |
| **Architecture** | Pure data classes and enums for zone, faction, weather systems |

## Purpose
Defines all data structures, enumerations, and serializable classes for the world systems including zones, factions, weather, and dynamic events. Provides the complete type foundation for the open-world naval gameplay.

---

## Zone Enumerations

### Zone Danger Levels
| Level | Ship Tiers | Description |
|-------|------------|-------------|
| Safe | T1-T2 | No permadeath, practice area |
| Low | T2-T4 | Light PvE, low risk |
| Medium | T3-T6 | Moderate PvE/PvP |
| High | T5-T8 | Heavy combat, high rewards |
| Extreme | T7-T10 | Maximum risk/reward |
| Extraction | Special | Permadeath extraction zones |

### Zone Types (14 Types)
```csharp
public enum ZoneType
{
    // Safe Zones
    Port,               // Protected harbor
    Anchorage,          // Safe spawn area
    TrainingGround,     // Tutorial/practice

    // Transit Zones
    Shipping,           // Trade routes
    Coastal,            // Near-shore waters
    OpenOcean,          // Deep water transit

    // Combat Zones
    Contested,          // PvP hotspot
    Battlefield,        // Large-scale combat
    Ambush,             // Submarine hunting grounds

    // Resource Zones
    Fishing,            // Resource gathering
    Salvage,            // Wreck exploration
    Mining,             // Underwater resources

    // Special Zones
    Extraction,         // Loot extraction
    Event,              // Limited-time events
    Boss                // Special encounters
}
```

### Zone Control States
| State | Description |
|-------|-------------|
| Neutral | No faction control |
| Contested | Multiple factions fighting |
| Controlled | Single faction dominance |
| Occupied | Full faction ownership |

---

## Faction Enumerations

### Major Factions (12 Factions)
```csharp
public enum Faction
{
    // Major Powers
    Atlantic,           // Western alliance
    Pacific,            // Eastern coalition
    Mediterranean,      // Southern confederation

    // Minor Factions
    FreeTraders,        // Merchant guild
    Privateers,         // Licensed raiders
    Salvagers,          // Wreck hunters
    Research,           // Scientific expeditions

    // Hostile Factions
    Pirates,            // Outlaws
    Separatists,        // Rebels
    Mercenaries,        // For hire

    // Neutral
    Independent,        // Unaligned players
    International       // UN/Neutral observers
}
```

### Faction Standing Levels
| Level | Value | Effects |
|-------|-------|---------|
| Hostile | -3 | Attack on sight |
| Unfriendly | -2 | No services |
| Suspicious | -1 | Limited services |
| Neutral | 0 | Basic services |
| Friendly | +1 | Full services |
| Allied | +2 | Discounts, missions |
| Exalted | +3 | Special access |

**Standing Thresholds**: -10000, -5000, -1000, 0, 5000, 15000, 50000 reputation points

---

## Weather Enumerations

### Weather Conditions (9 Types)
```csharp
public enum WeatherCondition
{
    Clear,              // Perfect visibility
    PartlyCloudy,       // Light clouds
    Overcast,           // Full cloud cover
    Fog,                // Reduced visibility
    Rain,               // Light precipitation
    Storm,              // Heavy weather
    Hurricane,          // Extreme conditions
    Snow,               // Arctic weather
    Sandstorm           // Desert regions
}
```

### Sea States (Douglas Scale)
| Level | Name | Description |
|-------|------|-------------|
| 0 | Calm | Glassy sea |
| 1 | Slight | Small wavelets |
| 2 | Light | Short waves |
| 3 | Moderate | Moderate waves |
| 4 | Rough | Rough waves |
| 5 | VeryRough | High waves |
| 6 | High | Very high waves |
| 7 | Severe | Severe conditions |
| 8 | Phenomenal | Extreme danger |

### Time of Day
| Period | Hours |
|--------|-------|
| Dawn | 05:00-07:00 |
| Morning | 07:00-12:00 |
| Afternoon | 12:00-17:00 |
| Dusk | 17:00-19:00 |
| Evening | 19:00-22:00 |
| Night | 22:00-05:00 |
| Midnight | 00:00-02:00 |

---

## Zone Data Classes

### ZoneDefinition
Complete zone configuration.

```csharp
[Serializable]
public class ZoneDefinition
{
    public string zoneId;
    public string zoneName;
    public string description;

    // Classification
    public ZoneType zoneType;
    public ZoneDangerLevel dangerLevel;

    // Tier Range
    public int minTier = 1;
    public int maxTier = 10;

    // Location
    public Vector2 worldPosition;
    public float radius;
    public List<Vector2> boundaryPoints;  // Polygon boundary

    // Connections
    public List<string> connectedZoneIds;
    public float travelTimeMinutes;

    // Control
    public Faction controllingFaction;
    public ZoneControlState controlState;
    public float controlStrength;  // 0-100%

    // Resources
    public List<ZoneResource> resources;
    public float resourceRespawnTime = 300f;

    // Spawns
    public List<SpawnPoint> spawnPoints;
    public float npcDensity = 1f;
    public List<string> npcFleetIds;

    // Special Features
    public bool hasPort;
    public bool hasRepairFacility;
    public bool hasMarket;
    public bool hasExtractionPoint;
}
```

### ZoneResource
Resource spawn in a zone.

```csharp
[Serializable]
public class ZoneResource
{
    public string resourceId;
    public string resourceType;
    public Vector2 spawnArea;
    public float spawnRate;
    public int maxQuantity;
    public int currentQuantity;
}
```

### SpawnPoint
Spawn point for players/NPCs.

```csharp
[Serializable]
public class SpawnPoint
{
    public string spawnId;
    public Vector3 position;
    public float heading;
    public SpawnPointType spawnType;
    public Faction owningFaction;
    public bool isActive;
}

public enum SpawnPointType
{
    PlayerSpawn,
    NPCPatrol,
    NPCTrader,
    NPCMission,
    BossSpawn,
    EventSpawn
}
```

### ZoneInstanceState
Runtime zone state.

```csharp
[Serializable]
public class ZoneInstanceState
{
    public string instanceId;
    public string zoneDefinitionId;

    // Population
    public int playerCount;
    public int npcCount;
    public int maxPlayers = 100;

    // Control
    public Dictionary<Faction, float> factionInfluence;
    public ZoneControlState currentControlState;

    // Events
    public List<ActiveZoneEvent> activeEvents;

    // Weather
    public ZoneWeatherState weather;
}
```

---

## Faction Data Classes

### FactionDefinition
Complete faction configuration.

```csharp
[Serializable]
public class FactionDefinition
{
    public Faction factionId;
    public string factionName;
    public string description;
    public Color factionColor;
    public Sprite factionEmblem;

    // Relations
    public Dictionary<Faction, int> defaultRelations;

    // Territory
    public List<string> homeZoneIds;
    public List<string> influenceZoneIds;

    // Services
    public bool offersRepairs;
    public bool offersMarket;
    public bool offersContracts;
    public bool offersInsurance;

    // Rewards
    public float reputationMultiplier = 1f;
    public List<string> exclusiveShipIds;
    public List<string> exclusiveItemIds;
}
```

### FactionReputation
Player reputation with a faction.

```csharp
[Serializable]
public class FactionReputation
{
    public Faction factionId;
    public int reputationPoints;
    public FactionStanding standing;

    // History
    public int missionsCompleted;
    public int shipsDestroyed;      // Negative impact
    public int friendliesHelped;
    public float totalTradeValue;

    // Calculate standing from points
    public void UpdateStanding()
    {
        // Uses StandingThresholds array
    }
}
```

### FactionRelation
Relation between two factions.

```csharp
[Serializable]
public class FactionRelation
{
    public Faction factionA;
    public Faction factionB;
    public int relationValue;       // -100 to +100
    public bool atWar;
    public bool hasTradeAgreement;
    public bool hasAlliance;
}
```

---

## Weather Data Classes

### ZoneWeatherState
Weather state for a zone with combat effects.

```csharp
[Serializable]
public class ZoneWeatherState
{
    public WeatherCondition condition;
    public SeaState seaState;
    public TimeOfDay timeOfDay;

    // Visibility
    public float visibility;        // Meters
    public float fogDensity;

    // Wind
    public float windSpeed;         // Knots
    public float windDirection;     // Degrees
    public float gustFactor;

    // Waves
    public float waveHeight;        // Meters
    public float waveFrequency;
    public float waveDirection;

    // Combat Effects
    public float detectionModifier;
    public float accuracyModifier;
    public float speedModifier;
    public float aircraftModifier;

    public void CalculateModifiers()
    {
        // Detection: visibility / 10000
        detectionModifier = Mathf.Clamp01(visibility / 10000f);

        // Accuracy: 1 - (seaState * 0.05)
        accuracyModifier = 1f - ((int)seaState * 0.05f);

        // Speed: 1 - (seaState * 0.03)
        speedModifier = 1f - ((int)seaState * 0.03f);

        // Aircraft: weather-dependent
        aircraftModifier = condition switch
        {
            WeatherCondition.Clear => 1f,
            WeatherCondition.Storm => 0.3f,
            WeatherCondition.Hurricane => 0f,
            _ => 0.85f
        };
    }
}
```

### WeatherForecast
Weather forecast entry.

```csharp
[Serializable]
public class WeatherForecast
{
    public float gameTime;          // When this weather starts
    public WeatherCondition condition;
    public SeaState seaState;
    public float transitionDuration;
}
```

---

## Zone Event Classes

### ActiveZoneEvent
Active event in a zone.

```csharp
[Serializable]
public class ActiveZoneEvent
{
    public string eventId;
    public string eventDefinitionId;
    public string eventName;

    // Timing
    public float startTime;
    public float endTime;
    public float duration;

    // Location
    public Vector3 eventPosition;
    public float eventRadius;

    // Participation
    public List<string> participantIds;
    public int maxParticipants;

    // Progress
    public float progress;          // 0-1
    public bool isComplete;
    public List<string> objectiveIds;

    // Rewards
    public float rewardMultiplier;
    public List<string> exclusiveRewardIds;
}
```

### Zone Event Types (10 Types)
```csharp
public enum ZoneEventType
{
    Invasion,           // Faction assault
    Defense,            // Protect position
    Escort,             // Convoy protection
    Hunt,               // Target elimination
    Salvage,            // Limited-time wreck
    Race,               // Time trial
    Tournament,         // PvP competition
    BossSpawn,          // Special enemy
    ResourceRush,       // Increased spawns
    StormSurvival       // Weather challenge
}
```

---

## Integration Points

### Used By
- `ZoneManager.cs` - Zone management and transitions
- `WeatherSystem.cs` - Weather conditions and effects
- `PermadeathManager.cs` - Risk zone penalties
- `ExtractionController.cs` - Extraction zone management
- UI systems for map, weather, faction displays

### Design References
- Based on GDD World-Design.md specifications

---

## Design Notes

### Zone System Architecture
- Hierarchical zone organization with connections
- Tier-based access control
- Dynamic faction control mechanics
- Resource spawning and management

### Faction System
- Multi-faction world with alliances/wars
- Player reputation affects access and pricing
- Faction-exclusive content unlocks

### Weather Effects on Gameplay
- Visibility affects detection and targeting
- Sea state affects accuracy and speed
- Weather conditions affect aircraft operations
- Dynamic combat modifiers

### Event System
- Time-limited dynamic events
- Multiple event types for variety
- Participation tracking and rewards
