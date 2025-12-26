# WeatherSystem.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/World/Controllers/WeatherSystem.cs` |
| **Namespace** | `WOS.World.Controllers` |
| **Inheritance** | `NetworkBehaviour` |
| **Pattern** | Singleton |
| **Lines** | ~627 |
| **Architecture** | Server-authoritative weather and time simulation |

## Purpose
Manages the game's weather system including time of day progression, weather conditions, sea states, and their effects on gameplay. Provides synchronized weather state across all clients with smooth transitions and combat modifiers.

---

## Class Diagram

```
WeatherSystem (NetworkBehaviour, Singleton)
├── Time System
│   ├── UpdateGameTime()
│   ├── GetTimeOfDay()
│   ├── CheckTimeOfDayTransition()
│   └── UpdateVisibilityForTime()
├── Weather System
│   ├── InitializeWeather()
│   ├── GenerateInitialForecast()
│   ├── UpdateWeather()
│   └── StartWeatherTransition()
├── Weather Transitions
│   ├── UpdateWeatherTransition()
│   ├── CompleteWeatherTransition()
│   └── InterpolateWeather()
├── Zone Weather
│   ├── GetZoneWeather()
│   └── SetZoneWeather()
└── Combat Modifiers
    ├── GetAccuracyModifier()
    ├── GetDetectionModifier()
    ├── GetSpeedModifier()
    └── GetAircraftModifier()
```

---

## Configuration

### Time Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `gameTimeScale` | 60 | Real-to-game time ratio (1 min = 1 hour) |
| `dayStartHour` | 5.0 | Hour when day begins |
| `nightStartHour` | 21.0 | Hour when night begins |

### Weather Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `weatherUpdateInterval` | 300s (5 min) | Time between weather checks |
| `weatherTransitionDuration` | 60s | Smooth transition time |
| `stormProbability` | 0.1 (10%) | Chance of storm weather |

### Forecast Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `forecastHours` | 6 | Hours to forecast ahead |
| `forecastAccuracy` | 0.8 (80%) | Forecast reliability |

---

## Synced State

```csharp
[SyncVar(hook = nameof(OnGameTimeChanged))]
private float currentGameTime;          // Hours since midnight

[SyncVar(hook = nameof(OnWeatherChanged))]
private WeatherCondition currentWeather;

[SyncVar(hook = nameof(OnSeaStateChanged))]
private SeaState currentSeaState;

[SyncVar] private float windSpeed;
[SyncVar] private float windDirection;
[SyncVar] private float visibility;
```

---

## Events

| Event | Signature | Trigger |
|-------|-----------|---------|
| `OnTimeOfDayChanged` | `Action<TimeOfDay>` | Time period changed |
| `OnWeatherConditionChanged` | `Action<WeatherCondition>` | Weather updated |
| `OnSeaStateConditionChanged` | `Action<SeaState>` | Sea state changed |
| `OnVisibilityChanged` | `Action<float>` | Visibility updated |
| `OnStormWarning` | `Action` | Storm approaching |
| `OnStormArrived` | `Action` | Storm conditions active |
| `OnStormCleared` | `Action` | Storm has passed |

---

## Time System

### Time Progression
```csharp
[Server]
private void UpdateGameTime(float deltaTime)
{
    float previousTime = currentGameTime;

    // Convert real time to game hours
    currentGameTime += (deltaTime / 60f) * gameTimeScale / 60f;

    if (currentGameTime >= 24f)
        currentGameTime -= 24f;

    CheckTimeOfDayTransition(previousTime, currentGameTime);
}
```

**Default Scale**: 1 real minute = 1 game hour
- Full day cycle = 24 real minutes

### Time of Day Mapping
```csharp
public TimeOfDay GetTimeOfDay(float hour)
{
    if (hour >= 5f && hour < 7f) return TimeOfDay.Dawn;
    if (hour >= 7f && hour < 12f) return TimeOfDay.Morning;
    if (hour >= 12f && hour < 17f) return TimeOfDay.Afternoon;
    if (hour >= 17f && hour < 19f) return TimeOfDay.Dusk;
    if (hour >= 19f && hour < 22f) return TimeOfDay.Evening;
    if (hour >= 0f && hour < 2f) return TimeOfDay.Midnight;
    return TimeOfDay.Night;
}
```

### Visibility by Time
| Time of Day | Base Visibility |
|-------------|-----------------|
| Midnight | 1,500m |
| Night | 2,000m |
| Evening | 4,000m |
| Dawn | 5,000m |
| Dusk | 6,000m |
| Morning | 10,000m |
| Afternoon | 12,000m |

---

## Weather System

### Weather Generation
```csharp
private WeatherForecast GenerateForecastEntry(float time,
                                               WeatherCondition previousWeather)
{
    WeatherCondition newWeather = previousWeather;

    // 30% chance of weather change
    if (Random.value < 0.3f)
    {
        float roll = Random.value;
        if (roll < stormProbability)      // 10% storm
            newWeather = WeatherCondition.Storm;
        else if (roll < 0.3f)             // 20% overcast
            newWeather = WeatherCondition.Overcast;
        else if (roll < 0.5f)             // 20% rain
            newWeather = WeatherCondition.Rain;
        else                              // 50% clear
            newWeather = WeatherCondition.Clear;
    }

    return new WeatherForecast { ... };
}
```

### Sea State from Weather
```csharp
private SeaState CalculateSeaStateFromWeather(WeatherCondition weather)
{
    return weather switch
    {
        WeatherCondition.Clear => SeaState.Slight,
        WeatherCondition.PartlyCloudy => SeaState.Light,
        WeatherCondition.Overcast => SeaState.Moderate,
        WeatherCondition.Fog => SeaState.Slight,
        WeatherCondition.Rain => SeaState.Moderate,
        WeatherCondition.Storm => SeaState.Rough,
        WeatherCondition.Hurricane => SeaState.Severe,
        _ => SeaState.Moderate
    };
}
```

### Wind Speed by Weather
| Weather | Base Wind (knots) |
|---------|-------------------|
| Clear | 8 |
| Partly Cloudy | 12 |
| Overcast | 15 |
| Fog | 5 |
| Rain | 20 |
| Storm | 40 |
| Hurricane | 80 |

**Sea State Modifier**: +2 knots per sea state level

### Visibility by Weather
| Weather | Visibility |
|---------|------------|
| Clear | 15,000m |
| Partly Cloudy | 12,000m |
| Overcast | 8,000m |
| Fog | 500m |
| Rain | 3,000m |
| Storm | 1,500m |
| Hurricane | 500m |

---

## Weather Transitions

### Transition Flow
```csharp
[Server]
private void StartWeatherTransition(WeatherForecast forecast)
{
    // Storm warning
    if (forecast.condition == WeatherCondition.Storm ||
        forecast.condition == WeatherCondition.Hurricane)
    {
        OnStormWarning?.Invoke();
        RpcNotifyStormWarning();
    }

    transitionTarget = new ZoneWeatherState { ... };
    isTransitioning = true;
    transitionProgress = 0f;
}

[Server]
private void UpdateWeatherTransition(float deltaTime)
{
    transitionProgress += deltaTime / weatherTransitionDuration;

    if (transitionProgress >= 1f)
        CompleteWeatherTransition();
    else
        InterpolateWeather(transitionProgress);
}
```

### Smooth Interpolation
```csharp
[Server]
private void InterpolateWeather(float t)
{
    // Smooth wind changes
    float targetWind = CalculateWindSpeed(target.condition, target.seaState);
    windSpeed = Mathf.Lerp(windSpeed, targetWind, t);

    // Gradual visibility changes
    float targetVisibility = CalculateVisibility(target.condition);
    visibility = Mathf.Lerp(visibility, targetVisibility, t);
}
```

---

## Combat Modifiers

### Accuracy Modifier
```csharp
public float GetAccuracyModifier()
{
    float modifier = 1f;

    // Sea state affects stability (-3% per level)
    modifier -= (int)currentSeaState * 0.03f;

    // Wind affects ballistics (-0.2% per knot)
    modifier -= windSpeed * 0.002f;

    // Visibility affects targeting
    modifier *= Mathf.Clamp01(visibility / 5000f);

    return Mathf.Max(0.3f, modifier);  // Minimum 30%
}
```

### Detection Modifier
```csharp
public float GetDetectionModifier()
{
    return Mathf.Clamp01(visibility / 10000f);
}
```

### Speed Modifier
```csharp
public float GetSpeedModifier()
{
    return 1f - ((int)currentSeaState * 0.03f);  // -3% per sea state level
}
```

### Aircraft Operations Modifier
```csharp
public float GetAircraftModifier()
{
    if (currentWeather == WeatherCondition.Hurricane) return 0f;   // No ops
    if (currentWeather == WeatherCondition.Storm) return 0.2f;     // 20%
    if ((int)currentSeaState >= 6) return 0.3f;                    // 30%

    return 1f - ((int)currentSeaState * 0.1f);  // -10% per sea state
}
```

### Modifier Summary Table
| Condition | Accuracy | Detection | Speed | Aircraft |
|-----------|----------|-----------|-------|----------|
| Clear, Calm | 100% | 100% | 100% | 100% |
| Moderate Sea | 91% | 100% | 91% | 70% |
| Storm | 70% | 15% | 88% | 20% |
| Hurricane | 55% | 5% | 79% | 0% |

---

## Zone-Specific Weather

```csharp
// Get weather for specific zone
public ZoneWeatherState GetZoneWeather(string zoneId)
{
    if (zoneWeather.TryGetValue(zoneId, out var weather))
        return weather;

    // Return global weather if zone-specific not set
    return new ZoneWeatherState
    {
        condition = currentWeather,
        seaState = currentSeaState,
        timeOfDay = GetTimeOfDay(currentGameTime),
        windSpeed = windSpeed,
        windDirection = windDirection,
        visibility = visibility
    };
}

// Set weather for specific zone (events, etc.)
[Server]
public void SetZoneWeather(string zoneId, ZoneWeatherState weather)
{
    zoneWeather[zoneId] = weather;
    weather.CalculateModifiers();
    RpcNotifyZoneWeatherChanged(zoneId, weather.condition, weather.seaState);
}
```

---

## Public API

### Time Queries
```csharp
public float GetGameTime()                    // Hours since midnight
public TimeOfDay GetCurrentTimeOfDay()        // Current time period
public bool IsNightTime()                     // Night check
```

### Weather Queries
```csharp
public WeatherCondition GetCurrentWeather()
public SeaState GetCurrentSeaState()
public float GetWindSpeed()
public float GetWindDirection()
public float GetVisibility()
public List<WeatherForecast> GetForecast()
```

### Combat Modifier Queries
```csharp
public float GetAccuracyModifier()
public float GetDetectionModifier()
public float GetSpeedModifier()
public float GetAircraftModifier()
```

---

## Usage Example

```csharp
// Check current conditions
var weather = WeatherSystem.Instance.GetCurrentWeather();
var seaState = WeatherSystem.Instance.GetCurrentSeaState();
Debug.Log($"Weather: {weather}, Sea: {seaState}");

// Check time
var timeOfDay = WeatherSystem.Instance.GetCurrentTimeOfDay();
bool isNight = WeatherSystem.Instance.IsNightTime();

// Apply combat modifiers
float accuracy = baseAccuracy * WeatherSystem.Instance.GetAccuracyModifier();
float detection = baseDetection * WeatherSystem.Instance.GetDetectionModifier();
float speed = baseSpeed * WeatherSystem.Instance.GetSpeedModifier();

// Check aircraft operations
float aircraftOps = WeatherSystem.Instance.GetAircraftModifier();
if (aircraftOps < 0.5f)
    Debug.Log("Poor conditions for flight operations");

// Get forecast
var forecast = WeatherSystem.Instance.GetForecast();
foreach (var entry in forecast)
{
    Debug.Log($"At {entry.gameTime}:00 - {entry.condition}");
}

// Subscribe to events
WeatherSystem.Instance.OnStormWarning += () => {
    Debug.Log("Storm incoming!");
};
```

---

## Integration Points

### Dependencies
- `WOS.World.Data` - Data structures
- `WOS.Debugging.DebugManager` - Logging
- `Mirror` - Networking

### Integrates With
- `ZoneManager` - Zone-specific weather
- Combat systems - Accuracy/detection modifiers
- Carrier systems - Aircraft operation restrictions
- Visual systems - Rendering effects

---

## Design Notes

### Time Acceleration
- 1 real minute = 1 game hour (configurable)
- Full day cycle in 24 real minutes
- Supports variable time scaling

### Weather Persistence
- Gradual weather transitions (60s default)
- 6-hour weather forecasting
- Storm warnings before arrival

### Combat Impact
- Weather significantly affects gameplay
- Sea state reduces accuracy and speed
- Visibility affects detection range
- Hurricanes ground all aircraft

### Future Enhancements
- Regional weather variation
- Seasonal weather patterns
- Player-visible forecasting UI
- Weather-based missions/events
