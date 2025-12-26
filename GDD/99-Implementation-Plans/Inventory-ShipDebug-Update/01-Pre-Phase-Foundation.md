# Pre-Phase: Foundation Refactor

**Goal**: Resolve technical debt and establish clean foundation for GDD-compliant development

---

## 1.1 ShipConfigurationSO Namespace Unification

### Problem Statement

Two competing ShipConfigurationSO classes exist:
- **OLD**: `WOS.ScriptableObjects.ShipConfigurationSO`
- **NEW**: `WOS.ScriptableObjects.Ships.ShipConfigurationSO`

This creates confusion, potential null references, and blocks proper implementation.

### Resolution Tasks

```
[ ] 1. Audit all references to OLD ShipConfigurationSO
    - Use Grep to find all "WOS.ScriptableObjects.ShipConfigurationSO" references
    - Document each file and line number

[ ] 2. Audit all references to NEW ShipConfigurationSO
    - Use Grep to find all "WOS.ScriptableObjects.Ships.ShipConfigurationSO" references
    - Compare feature sets between OLD and NEW

[ ] 3. Create migration mapping
    - Map OLD fields → NEW fields
    - Identify any fields in OLD not present in NEW
    - Plan data preservation strategy

[ ] 4. Migrate all references to NEW namespace
    - Update using statements
    - Update type references
    - Update serialized field types

[ ] 5. Update all ScriptableObject assets
    - Re-serialize assets to use NEW class
    - Verify data integrity after migration

[ ] 6. Delete OLD ShipConfigurationSO class
    - Remove old file
    - Remove old .meta file
    - Clean any orphaned references

[ ] 7. Verify no broken references
    - Full Unity project reimport
    - Check Inspector for missing script warnings
    - Run play mode test
```

---

## 1.2 ShipConfigurationSO Expanded Structure

The unified ShipConfigurationSO must support all GDD requirements:

```csharp
// Assets/Scripts/ScriptableObjects/Ships/ShipConfigurationSO.cs
namespace WOS.ScriptableObjects.Ships
{
    [CreateAssetMenu(fileName = "NewShipConfig", menuName = "WOS/Ships/Ship Configuration")]
    public class ShipConfigurationSO : ScriptableObject
    {
        [Header("Ship Identity")]
        public string shipId;
        public string shipName;
        public string shipClass;           // "Fletcher", "Iowa", "Yamato"
        public ShipType shipType;          // Destroyer, Cruiser, Battleship, Carrier
        public int tier;                   // 1-10
        public Nation nation;
        public Era era;
        public Sprite shipIcon;
        public Sprite shipSprite;          // Top-down view for fitting UI
        public Sprite shipSideProfile;     // Side view for armor UI

        [Header("Base Statistics")]
        public float baseDisplacementTons;
        public float maxSpeedKnots;
        public float turningRadiusMeters;
        public float accelerationRate;
        public float decelerationRate;
        public int baseHitPoints;
        public float detectionRangeKm;

        [Header("Equipment Slots (Slot-Matching System)")]
        [Tooltip("Each slot has fixed category + dimensions - modules must EXACTLY match")]
        public List<EquipmentSlotDefinition> equipmentSlots;

        [Header("Wing Slots (Carriers/Seaplane Tenders Only)")]
        [Tooltip("Aircraft capacity for carriers and seaplane ships")]
        public List<WingSlotDefinition> wingSlots;

        [Header("Armor Zones")]
        [Tooltip("Default armor configuration - 9 zones per GDD")]
        public ArmorZoneConfiguration defaultArmor;

        [Header("Cargo Grid (Tetris System)")]
        [Tooltip("Per-ship cargo capacity - NOT standardized by class")]
        public Vector2Int cargoGridSize;      // e.g., USS Fletcher: 10x12 = 120 cells
        public float maxCargoWeightTons;      // HARD CAP - cannot exceed 100%
        public List<CargoPartitionDefinition> cargoPartitions;

        [Header("Crew Capacity")]
        public int maxCrewComplement;         // Total sailors ship can hold
        public int minimumOperatingCrew;      // Minimum to leave port

        [Header("Fuel & Supplies")]
        public float maxFuelTons;
        public float fuelConsumptionRate;     // Tons per hour at full speed
        public float maxSuppliesTons;
        public float suppliesConsumptionRate; // Tons per hour
    }
}
```

---

## 1.3 Equipment Slot Definition Structure

```csharp
// Assets/Scripts/ScriptableObjects/Ships/EquipmentSlotDefinition.cs
namespace WOS.ScriptableObjects.Ships
{
    [Serializable]
    public class EquipmentSlotDefinition
    {
        [Header("Slot Identity")]
        public string slotId;                          // Unique identifier
        public string slotName;                        // "Main Battery Slot A"
        public string slotDescription;                 // Tooltip text

        [Header("Category & Dimension (Slot-Matching)")]
        [Tooltip("Module category MUST match slot category - checked FIRST")]
        public EquipmentSlotCategory category;

        [Tooltip("Module dimension MUST EXACTLY match - checked SECOND")]
        public Vector2Int requiredDimension;           // e.g., (3, 4) for 3x4 slot

        [Header("Weight Capacity")]
        [Tooltip("Module weight + Crew weight must be ≤ this value")]
        public float weightCapacityTons;

        [Header("Firing Arc (Weapons Only)")]
        [Tooltip("Arc limits in degrees relative to ship bow (0° = forward)")]
        public bool hasFiringArc;
        public float arcMinDegrees;                    // e.g., -45 (port limit)
        public float arcMaxDegrees;                    // e.g., +45 (starboard limit)

        [Header("Visual Placement")]
        public Vector3 hardpointPosition;              // World position on ship
        public Vector3 hardpointRotation;              // Default rotation
        public HardpointVisualSize visualSize;         // For UI indicator sizing
    }

    public enum EquipmentSlotCategory
    {
        // Primary Weapons
        MainBattery,           // Large caliber guns (8"+)
        SecondaryBattery,      // Medium caliber guns (5"-8")
        TertiaryBattery,       // Small caliber guns (<5")

        // Anti-Air
        AAHeavy,               // Large AA mounts (40mm+)
        AALight,               // Small AA mounts (<40mm)

        // Torpedoes
        TorpedoTubes,          // Fixed torpedo launchers
        TorpedoReload,         // Torpedo storage/reload system

        // Propulsion
        EngineRoom,            // Main propulsion
        Boiler,                // Steam generation (if separate)

        // Support Systems
        FireControl,           // Rangefinders, targeting computers
        Radar,                 // Detection equipment
        Sonar,                 // Underwater detection
        Communication,         // Radio, signal equipment

        // Damage Control
        DamageControl,         // Firefighting, flooding control
        Medical,               // Crew recovery

        // Utility
        Support,               // General support modules
        Misc,                  // Miscellaneous equipment

        // Armor (special)
        ArmorBelt,
        ArmorDeck,
        ArmorTurret
    }

    public enum HardpointVisualSize
    {
        Small,      // AA guns, small equipment
        Medium,     // Secondary batteries, support
        Large,      // Main batteries, engines
        Massive     // Yamato-class main guns
    }
}
```

---

## 1.4 Wing Slot Definition (Carriers)

```csharp
// Assets/Scripts/ScriptableObjects/Ships/WingSlotDefinition.cs
namespace WOS.ScriptableObjects.Ships
{
    [Serializable]
    public class WingSlotDefinition
    {
        [Header("Wing Identity")]
        public string wingSlotId;
        public string wingSlotName;            // "Hangar Bay A", "Flight Deck 1"

        [Header("Capacity")]
        public int maxAircraftCount;           // Number of planes this bay holds
        public List<AircraftType> allowedTypes; // Fighter, Bomber, Torpedo, Scout

        [Header("Operations")]
        public float launchTimeSeconds;        // Time to launch one aircraft
        public float recoveryTimeSeconds;      // Time to recover one aircraft
        public int simultaneousLaunches;       // How many can launch at once

        [Header("Storage")]
        public bool hasHangarStorage;          // Below-deck storage
        public int hangarCapacity;             // Additional stored aircraft
        public float armingTimeSeconds;        // Time to arm/fuel aircraft
    }

    public enum AircraftType
    {
        Fighter,
        DiveBomber,
        TorpedoBomber,
        Scout,
        Seaplane
    }
}
```

---

## 1.5 Armor Zone Configuration

```csharp
// Assets/Scripts/ScriptableObjects/Ships/ArmorZoneConfiguration.cs
namespace WOS.ScriptableObjects.Ships
{
    [Serializable]
    public class ArmorZoneConfiguration
    {
        [Header("9 Armor Zones per GDD")]
        public ArmorZoneData belt;
        public ArmorZoneData deck;
        public ArmorZoneData bulkhead;
        public ArmorZoneData turretFace;
        public ArmorZoneData turretRoof;
        public ArmorZoneData turretSides;
        public ArmorZoneData barbette;
        public ArmorZoneData conningTower;
        public ArmorZoneData citadel;
    }

    [Serializable]
    public class ArmorZoneData
    {
        public string zoneName;
        public ArmorMaterial material;
        public float thicknessInches;          // Player sets in 0.1" increments
        public float ThicknessMM => thicknessInches * 25.4f;  // Calculated
        public float WeightTons;               // Calculated based on area + thickness
    }

    public enum ArmorMaterial
    {
        None,
        RHA,                // Rolled Homogeneous Armor (baseline)
        FaceHardened,       // Better vs AP at angle
        KruppCemented,      // German high-quality
        TerniCemented,      // Italian
        Ducol,              // British high-tensile
        STS,                // Special Treatment Steel (USN)
        CNC                 // Cast Non-Cemented
    }
}
```

---

## 1.6 Cargo Partition Definition

```csharp
// Assets/Scripts/ScriptableObjects/Ships/CargoPartitionDefinition.cs
namespace WOS.ScriptableObjects.Ships
{
    [Serializable]
    public class CargoPartitionDefinition
    {
        [Header("Partition Identity")]
        public string partitionId;
        public string partitionName;           // "Main Magazine", "Fuel Bunker A"
        public CargoPartitionType partitionType;

        [Header("Grid Location")]
        public RectInt gridArea;               // Which cells belong to this partition

        [Header("Restrictions")]
        public List<CargoItemType> allowedItemTypes;
        public List<CargoItemType> prohibitedItemTypes;

        [Header("Risk Properties")]
        public float explosionRiskMultiplier;  // 1.0 = normal, 2.0 = double
        public float fireRiskMultiplier;
        public bool requiresVentilation;       // Some cargo needs air
        public bool requiresRefrigeration;     // Perishables
    }

    public enum CargoPartitionType
    {
        General,           // No special properties
        Magazine,          // Ammunition storage - explosion risk
        FuelBunker,        // Fuel storage - fire risk
        Refrigerated,      // Perishables - spoilage mechanic
        Hazardous,         // Chemicals, etc.
        Secure,            // Valuables, locked
        FloodableCompartment  // Below waterline
    }

    public enum CargoItemType
    {
        // Ammunition
        ShellsAP,
        ShellsHE,
        ShellsSpecial,
        Torpedoes,
        DepthCharges,
        Mines,

        // Consumables
        Fuel,
        FreshWater,
        Food,
        MedicalSupplies,
        RepairMaterials,

        // Trade Goods
        RawMaterials,
        ManufacturedGoods,
        Luxury,
        Contraband,

        // Special
        Salvage,
        Prisoners,
        Intelligence
    }
}
```

---

## 1.7 Base Interfaces

```csharp
// Assets/Scripts/Inventory/Interfaces/ISlotMatchingValidator.cs
namespace WOS.Inventory.Interfaces
{
    public interface ISlotMatchingValidator
    {
        /// <summary>
        /// GDD Rule: Category must match FIRST, before any other checks
        /// </summary>
        bool ValidateCategoryMatch(EquipmentSlotCategory moduleCategory, EquipmentSlotCategory slotCategory);

        /// <summary>
        /// GDD Rule: Dimension must EXACTLY match (no rotation, no flexibility)
        /// </summary>
        bool ValidateDimensionMatch(Vector2Int moduleDim, Vector2Int slotDim);

        /// <summary>
        /// GDD Rule: Module weight must fit within slot capacity
        /// </summary>
        bool ValidateModuleWeight(float moduleWeight, float slotCapacity);

        /// <summary>
        /// GDD Rule: Module weight + Crew weight must fit within slot capacity
        /// </summary>
        bool ValidateTotalWeight(float moduleWeight, float crewWeight, float slotCapacity);

        /// <summary>
        /// Complete validation following GDD order: Category → Dimension → Weight → Crew
        /// </summary>
        SlotValidationResult ValidateComplete(ModuleDefinitionSO module, CrewCard crew, EquipmentSlotDefinition slot);
    }

    public struct SlotValidationResult
    {
        public bool IsValid;
        public bool CategoryMatch;
        public bool DimensionMatch;
        public bool ModuleWeightOk;
        public bool CrewWeightOk;
        public string FailureReason;
        public SlotValidationStep FailedAtStep;
    }

    public enum SlotValidationStep
    {
        None,           // All passed
        Category,       // Failed at category check
        Dimension,      // Failed at dimension check
        ModuleWeight,   // Failed at module weight check
        CrewWeight      // Failed at crew weight check
    }
}
```

```csharp
// Assets/Scripts/Inventory/Interfaces/IHardCapWeightSystem.cs
namespace WOS.Inventory.Interfaces
{
    public interface IHardCapWeightSystem
    {
        float CurrentWeightTons { get; }
        float MaxWeightTons { get; }
        float WeightPercentage { get; }
        bool IsAtHardCap { get; }

        /// <summary>
        /// Check if additional weight can be added (HARD CAP enforcement)
        /// </summary>
        bool CanAddWeight(float additionalWeightTons);

        /// <summary>
        /// Check if ship can undock (must be at or below 100%)
        /// </summary>
        bool CanUndock();

        /// <summary>
        /// Attempt to add weight - returns false if would exceed hard cap
        /// </summary>
        bool TryAddWeight(float weightTons);

        /// <summary>
        /// Remove weight (always succeeds)
        /// </summary>
        void RemoveWeight(float weightTons);

        /// <summary>
        /// Event fired when weight changes
        /// </summary>
        event Action<float, float> OnWeightChanged;
    }
}
```

```csharp
// Assets/Scripts/Inventory/Interfaces/ITetrisGrid.cs
namespace WOS.Inventory.Interfaces
{
    public interface ITetrisGrid
    {
        Vector2Int GridSize { get; }
        int TotalCells { get; }
        int UsedCells { get; }
        int FreeCells { get; }

        /// <summary>
        /// Check if item can be placed at position (collision + bounds check)
        /// </summary>
        bool CanPlaceItem(ITetrisItem item, Vector2Int position);

        /// <summary>
        /// Place item at position (assumes CanPlaceItem was true)
        /// </summary>
        void PlaceItem(ITetrisItem item, Vector2Int position);

        /// <summary>
        /// Remove item from grid
        /// </summary>
        void RemoveItem(ITetrisItem item);

        /// <summary>
        /// Get item at specific cell (or null if empty)
        /// </summary>
        ITetrisItem GetItemAtCell(Vector2Int cell);

        /// <summary>
        /// Auto-arrange all items for optimal packing
        /// </summary>
        bool TryAutoArrange();
    }

    public interface ITetrisItem
    {
        string ItemId { get; }
        Vector2Int GridSize { get; }
        bool IsRotated { get; }
        Vector2Int CurrentPosition { get; }

        /// <summary>
        /// Rotate item 90 degrees clockwise (swaps dimensions)
        /// </summary>
        void Rotate();

        /// <summary>
        /// Get all cells this item occupies at given position
        /// </summary>
        IEnumerable<Vector2Int> GetOccupiedCells(Vector2Int position);
    }
}
```

---

## 1.8 Supporting Enums

```csharp
// Assets/Scripts/Core/Enums/ShipEnums.cs
namespace WOS.Core
{
    public enum ShipType
    {
        Destroyer,
        LightCruiser,
        HeavyCruiser,
        Battlecruiser,
        Battleship,
        LightCarrier,
        FleetCarrier,
        Submarine,
        AuxiliaryShip,
        PatrolBoat
    }

    public enum Nation
    {
        USA,
        UK,
        Japan,
        Germany,
        Italy,
        France,
        USSR,
        Netherlands,
        Generic
    }

    public enum Era
    {
        PreWWI,
        WWI,
        Interwar,
        EarlyWWII,
        MidWWII,
        LateWWII,
        PostWWII
    }
}
```

---

## Pre-Phase Validation Checklist

```
[ ] ShipConfigurationSO namespace conflict resolved
[ ] All assets using unified NEW namespace
[ ] No missing script warnings in Unity
[ ] EquipmentSlotDefinition with category + dimension + weight
[ ] WingSlotDefinition for carrier support
[ ] ArmorZoneConfiguration with 9 zones
[ ] CargoPartitionDefinition with risk properties
[ ] ISlotMatchingValidator interface defined
[ ] IHardCapWeightSystem interface defined
[ ] ITetrisGrid interface defined
[ ] All enums created and documented
[ ] Play mode test passes
[ ] Compile with no errors
```

---

*Pre-Phase Foundation - Version 3.0*
