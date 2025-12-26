---
tags: [script, ships, data, enums, implemented]
script-type: Data Classes
namespace: WOS.Ships.Data
file-path: Assets/Scripts/Ships/Data/ShipProgressionData.cs
status: IMPLEMENTED
size: ~1188 lines
feature-group: ships
---

# ShipProgressionData.cs

## Quick Reference
**Type**: Data Classes & Enums
**Namespace**: WOS.Ships.Data
**File**: `Assets/Scripts/Ships/Data/ShipProgressionData.cs`
**Size**: ~1188 lines
**Dependencies**: None (standalone data)

---

## Purpose
Comprehensive data structures for ship progression and fleet management. Based on GDD Ship-Progression.md and Tiers.md. Includes enums, ship instance data, fleet data, armor system, and upgrade structures.

---

## Ship Classification Enums

### ShipClass (16 types)

```csharp
public enum ShipClass
{
    // Surface Warships
    Destroyer,        // T1-T5: Fast, torpedo-focused
    LightCruiser,     // T2-T6: Versatile
    HeavyCruiser,     // T3-T7: Armored
    Battlecruiser,    // T5-T8: Fast capital
    Battleship,       // T6-T10: Maximum firepower
    Dreadnought,      // T8-T10: Ultimate

    // Carriers
    EscortCarrier,    // T3-T5
    FleetCarrier,     // T5-T8
    SuperCarrier,     // T8-T10

    // Submarines
    CoastalSubmarine, // T1-T3
    FleetSubmarine,   // T3-T6
    CruiserSubmarine, // T5-T8
    HunterKiller,     // T7-T10

    // Support
    Transport,        // T1-T5
    Tanker,           // T1-T5
    RepairShip,       // T3-T6
    Minelayer,        // T2-T5
    Minesweeper,      // T1-T4

    // Premium
    MuseumShip,
    PrototypeShip
}
```

### ShipTier

```csharp
public enum ShipTier
{
    T1 = 1,  // No permadeath
    T2 = 2,  // No permadeath
    T3 = 3,  // 5% permadeath
    T4 = 4,  // 10%
    T5 = 5,  // 15%
    T6 = 6,  // 20%
    T7 = 7,  // 25%
    T8 = 8,  // 30%
    T9 = 9,  // 35%
    T10 = 10 // 40% permadeath
}
```

### ShipNation

```csharp
public enum ShipNation
{
    International,  // Multi-nation starter
    USN,           // United States Navy
    RN,            // Royal Navy (UK)
    IJN,           // Imperial Japanese Navy
    KM,            // Kriegsmarine (Germany)
    MN,            // Marine Nationale (France)
    RM,            // Regia Marina (Italy)
    VMF            // Soviet Navy
}
```

### Other Enums

- **ShipUnlockStatus**: Locked, Unlocked, Owned, Lost, Retired
- **ShipCondition**: Perfect, Good, Damaged, Crippled, Wreck, Destroyed

---

## Ship Data Classes

### ShipInstanceData

```csharp
public class ShipInstanceData
{
    // Identity
    public string shipInstanceId;
    public string shipDefinitionId;
    public string shipName;

    // Classification
    public ShipClass shipClass;
    public ShipTier tier;
    public ShipNation nation;

    // Status
    public ShipUnlockStatus unlockStatus;
    public ShipCondition condition;
    public bool isActiveShip;

    // Experience
    public int battlesFought;
    public int victoriesWon;
    public int shipsDestroyed;
    public float totalDamageDealt;

    // Stats
    public float currentHealth;
    public float maxHealth;
    public float repairCost;

    // Insurance
    public bool hasInsurance;
    public int insuranceLevel;
    public DateTime insuranceExpiry;

    public float GetEfficiency();
    public float GetPermadeathRisk();
}
```

### PlayerFleet

```csharp
public class PlayerFleet
{
    public string playerId;
    public string fleetName;
    public int maxShips;
    public List<ShipInstanceData> ships;
    public string activeShipId;

    // Statistics
    public int totalBattles;
    public int totalVictories;
    public int shipsLost;
    public float fleetValue;

    public ShipInstanceData GetShip(string instanceId);
    public ShipInstanceData GetActiveShip();
    public List<ShipInstanceData> GetShipsByTier(ShipTier tier);
    public List<ShipInstanceData> GetShipsByClass(ShipClass shipClass);
}
```

---

## Equipment Slot Enums

### ModuleSlotType

```csharp
public enum ModuleSlotType
{
    Bridge,   // Command & control
    Engine,   // Propulsion
    Support   // Utility
}
```

### SupportModuleCategory

```csharp
public enum SupportModuleCategory
{
    Any, FireControl, Radar, Sonar,
    Communications, DamageControl, Medical,
    Concealment, Utility
}
```

### TurretMountType

```csharp
public enum TurretMountType
{
    MainBattery, Secondary, AntiAircraft, Torpedo, Depth
}
```

---

## Armor System (Navy Field Style)

### ArmorType (6 types)

| Type | AP Prot | HE Prot | Weight/in | Nation |
|------|---------|---------|-----------|--------|
| RHA | 1.0 | 1.0 | 40t | All |
| FaceHardened | 1.3 | 0.8 | 45t | All |
| KruppCemented | 1.4 | 1.1 | 50t | Germany |
| TerniSteel | 0.9 | 1.2 | 32t | Italy |
| DucolSteel | 0.85 | 1.0 | 28t | UK |
| STS | 1.15 | 1.15 | 42t | USA |

### ArmorZoneType (9 zones)

- **Deck**: ForwardDeck, CenterDeck, AftDeck
- **Belt**: ForwardBelt, CenterBelt, AftBelt
- **Structural**: ConningTower, MainTurrets, SecondaryTurrets

### ArmorConfiguration Class

```csharp
public class ArmorConfiguration
{
    public ArmorZone forwardDeck, centerDeck, aftDeck;
    public ArmorZone forwardBelt, centerBelt, aftBelt;
    public ArmorZone conningTower, mainTurrets, secondaryTurrets;

    public ArmorZone GetZone(ArmorZoneType zoneType);
    public float GetTotalWeight(ShipClass shipClass);
    public long GetTotalCost();
    public float GetSpeedPenalty(ShipClass shipClass);
    public bool IsValid(ShipClass shipClass);
    public void ApplyScheme(ArmorScheme scheme, ShipClass shipClass);
}
```

### ArmorScheme Presets

- **Unarmored**: Maximum speed
- **Lightweight**: Speed-focused, minimal armor (DucolSteel)
- **Balanced**: Standard protection (RHA)
- **HeavyProtection**: Maximum survivability (STS)
- **AllOrNothing**: Heavy citadel, light extremities (FaceHardened)

---

## Ship Class Armor Limits

| Class | Max Deck | Max Belt | Max Turret |
|-------|----------|----------|------------|
| Destroyer | 0.5" | 2" | 1" |
| LightCruiser | 2" | 4" | 3" |
| HeavyCruiser | 3" | 8" | 6" |
| Battlecruiser | 5" | 12" | 12" |
| Battleship | 7" | 18" | 17" |
| Dreadnought | 7" | 18" | 17" |

---

## Ship Upgrades

### ShipUpgrade Class

```csharp
public class ShipUpgrade
{
    public string upgradeId;
    public string upgradeName;
    public ShipUpgradeCategory category;
    public List<ShipStatModifier> modifiers;
    public long creditCost;
    public int minShipTier;
}
```

### ShipUpgradeCategory

- Hull, Propulsion, FireControl, Survivability, Concealment, Aircraft

### ShipStatType (18 stats)

- MaxHealth, ArmorThickness, MaxSpeed, Acceleration
- TurnRate, RudderShift, MainBatteryRange, MainBatteryReload
- SecondaryRange, TorpedoReload, AAEfficiency
- SurfaceDetection, AirDetection, FireResistance
- FloodingResistance, RepairSpeed, AircraftCapacity, AircraftSpeed

---

## Integration Points

### Dependencies
- None (standalone data)

### Used By
- [[ShipDefinitionSO]] - Ship configuration
- [[FleetManager]] - Fleet management
- [[EquipmentPanel]] - Slot types
- Combat systems - Armor calculations

---

## Related Files
- [[ShipDefinitionSO]] - Ship definitions
- [[FleetManager]] - Fleet controller
- [[ArmorConfiguration]] - Armor system

