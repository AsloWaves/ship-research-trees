# PortConfigurationSO

## Quick Reference

| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/ScriptableObjects/Configs/PortConfigurationSO.cs` |
| **Namespace** | `WOS.ScriptableObjects` |
| **Inheritance** | `ScriptableObject` |
| **Lines** | 395 |

---

## Purpose

Core port/harbor configuration defining services, protection zones, economy, and scene settings. Ports are safe zones where players can dock, trade, repair, and access services.

**Key Features**:
- **GDD Tier-Based Protection Zones** (T1=10km, T2=25km, T3+=50km)
- **Service Availability Configuration** (repair, trading, crew, banking)
- **Economic Factors** (prosperity, security, prices)
- **Scene Loading Configuration** (async scene loading for harbor interiors)
- **Cross-Reference System** (docking, services, visual, UI, integration configs)

---

## Port Identity

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `portName` | `string` | "New Harbor" | Display name of the port |
| `portType` | `PortType` | `TradingPort` | Type of port determining available services |
| `portSize` | `PortSize` | `Medium` | Size category affecting capacity and features |
| `portDescription` | `string` (TextArea) | Default | Detailed description of the port |

### PortType Values
- **TradingPort**: Commercial trading hub (full trading services)
- **MilitaryBase**: Naval military installation (repair, upgrade priority)
- **FishingVillage**: Small fishing community (basic services only)
- **IndustrialPort**: Manufacturing and industry (cheap prices, good availability)
- **CulturalHub**: Tourist and cultural center (expensive but high quality)

### PortSize Values
- **Small**: 1-3 docking zones
- **Medium**: 4-6 docking zones
- **Large**: 7-10 docking zones
- **Massive**: 11+ docking zones

---

## Scene Configuration

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `harborSceneName` | `string` | "HarborScene" | Name of the harbor scene to load when docking |
| `useAsyncLoading` | `bool` | `true` | Should we use async scene loading |
| `harborSpawnPointName` | `string` | "PlayerSpawn" | Spawn point name in the harbor scene |

**Scene Loading**: When player docks, game loads `harborSceneName` asynchronously and spawns player at `harborSpawnPointName`.

---

## Protection Zone (GDD Tier System)

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `portTier` | `PortTier` | `T1` | Port tier determines safe zone radius |
| `protectionRadius` | `float` | 10,000m | Radius around port where players are invincible (auto-calculated from tier) |
| `useGDDTierRadius` | `bool` | `true` | Use GDD tier-based radius vs custom value |
| `showProtectionZoneBoundary` | `bool` | `true` | Show protection zone boundary to players |
| `protectionWarningDistance` | `float` | 150m | Warning distance before leaving protection zone |

### GDD Tier-Based Protection Radius
| Tier | Radius | Description |
|------|--------|-------------|
| **T1** | 10 km | Small ports, basic protection |
| **T2** | 25 km | Medium ports, extended protection |
| **T3+** | 50 km | Large ports, maximum protection |

**Auto-Calculation**: If `useGDDTierRadius` is true, `protectionRadius` is auto-calculated from `portTier`.

**Protection Zone**: Players within radius are:
- Invincible (cannot be damaged)
- Cannot be attacked by other players
- Safe from NPC threats
- Can repair and resupply freely

---

## Service Availability

### ServiceAvailability Class
| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `hasRepairService` | `bool` | `true` | Can players repair ships here |
| `hasRefuelService` | `bool` | `true` | Can players refuel ships here |
| `hasTradingService` | `bool` | `true` | Can players buy/sell cargo here |
| `hasUpgradeService` | `bool` | `false` | Can players upgrade ships here |
| `hasStorageService` | `bool` | `false` | Can players store items here |
| `hasCrewService` | `bool` | `false` | Can players recruit crew here |
| `hasMissionService` | `bool` | `true` | Can players access missions here |
| `hasBankingService` | `bool` | `false` | Can players access bank services here |

### Service Quality
| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `serviceQuality` | `float` | 0.5-2.0 | 1.0 | Quality multiplier for services (affects speed/cost) |
| `priceMultiplier` | `float` | 0.5-2.0 | 1.0 | Price multiplier for services |

---

## Economic Settings

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `prosperityLevel` | `float` | 0.0-1.0 | 0.6 | Base economic prosperity level (affects prices/availability) |
| `tradingVolume` | `float` | 0.1-3.0 | 1.0 | Trading volume multiplier |
| `securityLevel` | `float` | 0.0-1.0 | 0.7 | Security level (affects piracy/safety) |

### Price Modifier Calculation
```csharp
public float GetPriceModifier()
```
Combines prosperity, security, size, and service multipliers:
- **Prosperity**: Low prosperity → Higher prices (1.2×), High prosperity → Lower prices (0.8×)
- **Security**: Low security → Higher prices (1.3×), High security → Lower prices (0.9×)
- **Size**: Small ports → 10% markup, Massive ports → 10% discount
- **Service Multiplier**: Custom multiplier from `services.priceMultiplier`

**Example**: Small port, low prosperity (0.3), low security (0.4)
- Prosperity modifier: 1.2 - (0.3 × 0.4) = 1.08
- Security modifier: 1.3 - (0.4 × 0.4) = 1.14
- Size modifier: 1.1 (small)
- **Total**: 1.08 × 1.14 × 1.1 = 1.35× (35% markup)

### Service Efficiency Calculation
```csharp
public float GetServiceEfficiency()
```
Combines prosperity, infrastructure, size, and quality:
- **Prosperity Bonus**: Up to +20%
- **Infrastructure Bonus**: Up to +30%
- **Size Bonus**: Small (0%), Medium (+10%), Large (+20%), Massive (+30%)
- **Service Quality**: Custom multiplier

---

## Environmental Factors

| Property | Type | Range | Default | Description |
|----------|------|-------|---------|-------------|
| `shelterLevel` | `float` | 0.0-1.0 | 0.8 | How sheltered the port is from storms |
| `waterDepth` | `float` | 0.0-1.0 | 0.7 | Water depth level (affects ship access) |
| `infrastructureQuality` | `float` | 0.0-1.0 | 0.6 | Port infrastructure quality |

---

## Spawn Configuration

| Property | Type | Description |
|----------|------|-------------|
| `spawnPoints` | `Transform[]` | Where ships should spawn when leaving this port |
| `patrolRoutes` | `Transform[]` | Patrol routes for NPC ships near this port |

---

## Cross-References

| Property | Type | Description |
|----------|------|-------------|
| `dockingConfig` | `DockingConfigurationSO` | Docking configuration for this port |
| `servicesConfig` | `PortServicesConfigurationSO` | Services configuration |
| `visualConfig` | `PortVisualConfigurationSO` | Visual effects configuration |
| `uiConfig` | `PortUIConfigurationSO` | UI configuration |
| `integrationConfig` | `PortIntegrationConfigurationSO` | Integration settings |

**Modular Design**: Port configuration is split across multiple SOs for organization and reusability.

---

## Key Methods

### Protection Radius (Auto or Custom)
```csharp
public float ProtectionRadius { get; }
```
Returns effective protection radius (GDD tier-based or custom).

### Is Within Protection Zone
```csharp
public bool IsWithinProtectionZone(Vector3 playerPosition, Vector3 portPosition)
```
Check if position is within protection zone.

### Is Approaching Protection Boundary
```csharp
public bool IsApproachingProtectionBoundary(Vector3 playerPosition, Vector3 portPosition)
```
Check if player is approaching zone boundary (for warning).

### Get Suggested Docking Locations
```csharp
public int GetSuggestedDockingLocations()
```
Returns suggested docking location count based on port size.

### Is Service Available
```csharp
public bool IsServiceAvailable(string serviceType)
```
Check if specific service is available (repair, refuel, trading, etc.).

### Validate Configuration
```csharp
public bool ValidateConfiguration()
```
Validate configuration and log warnings for issues.

### Get Port Stats
```csharp
public PortStats GetPortStats()
```
Returns comprehensive port statistics for UI/debugging.

---

## Usage Example

```csharp
PortConfigurationSO port = // from scene or database

// Check protection zone
Vector3 playerPos = player.transform.position;
Vector3 portPos = portTransform.position;

if (port.IsWithinProtectionZone(playerPos, portPos))
{
    Debug.Log("Player is safe in protection zone");
    player.SetInvincible(true);
}

// Check approaching boundary
if (port.IsApproachingProtectionBoundary(playerPos, portPos))
{
    UIManager.ShowWarning("Leaving safe zone!");
}

// Check service availability
if (port.IsServiceAvailable("repair"))
{
    Debug.Log("Repair service available");
}

// Get price modifier
float priceMultiplier = port.GetPriceModifier();
int repairCost = baseRepairCost * priceMultiplier;

// Get service efficiency
float efficiency = port.GetServiceEfficiency();
float repairTime = baseRepairTime / efficiency;
```

---

## PortStats Structure

Comprehensive port statistics for debugging and UI:

```csharp
public struct PortStats
{
    public string portName;
    public PortType portType;
    public PortSize portSize;
    public PortTier portTier;
    public int suggestedDockingLocations;
    public float protectionRadius;
    public float prosperityLevel;
    public float securityLevel;
    public float serviceEfficiency;
    public float priceModifier;
    public float shelterLevel;
    public float infrastructureQuality;
}
```

---

## Design Notes

### GDD Tier System

Protection zones use **GDD tier-based system** for consistency:
- **T1 (10km)**: Starting zones, basic safety
- **T2 (25km)**: Mid-game zones, extended safety
- **T3+ (50km)**: End-game zones, maximum safety

This prevents griefing near ports while allowing PvP in open waters.

### Economic Realism

Port economy reflects real-world factors:
- **Prosperity**: Wealthy ports have lower prices (economy of scale)
- **Security**: Dangerous waters increase insurance costs
- **Size**: Larger ports have better efficiency and lower prices
- **Infrastructure**: Better facilities provide faster service

### Modular Configuration

Port config is split across multiple SOs:
1. **PortConfigurationSO**: Core settings (this class)
2. **DockingConfigurationSO**: Docking mechanics
3. **PortServicesConfigurationSO**: Service details
4. **PortVisualConfigurationSO**: Visual effects
5. **PortUIConfigurationSO**: UI layout
6. **PortIntegrationConfigurationSO**: System integration

This allows:
- **Reusability**: Share visual configs across multiple ports
- **Organization**: Clear separation of concerns
- **Flexibility**: Mix and match configurations

---

## Create via Unity Menu

**Path**: `Create > WOS > Environment > Port Configuration`

**Default Filename**: `PortConfig`
