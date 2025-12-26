# Phase 1: Port Integration

**Goal**: Establish Port as the central hub with player spawn, safe zones, and fitting restrictions

---

## 1.1 Port Tier System

### PortTier Enum

```csharp
// Assets/Scripts/World/Ports/PortTier.cs
namespace WOS.World.Ports
{
    public enum PortTier
    {
        T1 = 1,   // Small outpost
        T2 = 2,   // Minor port
        T3 = 3,   // Regional port
        T4 = 4,   // Major port
        T5 = 5,   // Naval base
        T6 = 6,   // Fleet headquarters
        T7 = 7,   // Strategic hub
        T8 = 8,   // Major naval installation
        T9 = 9,   // Capital port
        T10 = 10  // Superport
    }
}
```

### Port Configuration

```csharp
// Assets/Scripts/World/Ports/PortConfiguration.cs
namespace WOS.World.Ports
{
    [CreateAssetMenu(fileName = "NewPortConfig", menuName = "WOS/Ports/Port Configuration")]
    public class PortConfigurationSO : ScriptableObject
    {
        [Header("Port Identity")]
        public string portId;
        public string portName;
        public PortTier tier;
        public Nation controllingNation;
        public Vector2 worldPosition;

        [Header("Safe Zone (per GDD)")]
        [Tooltip("T1: 10km, T2: 25km, T3+: 50km")]
        public float safeZoneRadiusKm;

        [Header("Storage Capacity (per GDD)")]
        [Tooltip("T1-3: 500 cells, T4-7: 750 cells, T8-10: 1000 cells")]
        public int storageGridCells;

        [Header("Services Available")]
        public PortServices availableServices;

        [Header("Repair Rates")]
        public float hullRepairPerHour;
        public float systemRepairPerHour;
        public float maxRepairPercentPerVisit;

        [Header("Recruitment")]
        public int maxCrewAvailable;
        public float crewRefreshRatePerHour;

        // Calculated properties
        public static float GetSafeZoneRadius(PortTier tier)
        {
            return tier switch
            {
                PortTier.T1 => 10f,
                PortTier.T2 => 25f,
                _ => 50f  // T3-T10 all have 50km
            };
        }

        public static int GetStorageCapacity(PortTier tier)
        {
            return (int)tier switch
            {
                <= 3 => 500,
                <= 7 => 750,
                _ => 1000
            };
        }
    }

    [Flags]
    public enum PortServices
    {
        None = 0,
        Docking = 1 << 0,           // Basic docking
        Fitting = 1 << 1,           // Equipment changes
        Repairs = 1 << 2,           // Hull/system repair
        Storage = 1 << 3,           // Port storage access
        Marketplace = 1 << 4,       // Buy/sell goods
        Recruitment = 1 << 5,       // Hire crew
        FuelResupply = 1 << 6,      // Fuel purchase
        AmmunitionResupply = 1 << 7,// Ammo purchase
        Drydock = 1 << 8,           // Major repairs/refit
        Intelligence = 1 << 9,      // Mission briefings
        Bank = 1 << 10,             // Currency exchange

        // Common bundles
        BasicServices = Docking | Repairs | FuelResupply,
        StandardServices = BasicServices | Fitting | Storage | Marketplace,
        FullServices = StandardServices | Recruitment | AmmunitionResupply | Drydock | Intelligence | Bank
    }
}
```

---

## 1.2 Player Spawn System

### Spawn Position Change

**GDD Requirement**: Players start in Port, not open ocean

```csharp
// Assets/Scripts/Networking/PlayerSpawnManager.cs
namespace WOS.Networking
{
    public class PlayerSpawnManager : NetworkBehaviour
    {
        [Header("Spawn Configuration")]
        [SerializeField] private PortConfigurationSO defaultTutorialPort;
        [SerializeField] private Transform[] portSpawnPoints;

        public enum SpawnType
        {
            TutorialPort,      // First-time players
            LastDockedPort,    // Returning players
            RespawnPort,       // After ship destruction
            DesignatedPort     // Specific port assignment
        }

        [Server]
        public Vector3 GetSpawnPosition(PlayerData playerData)
        {
            SpawnType spawnType = DetermineSpawnType(playerData);

            return spawnType switch
            {
                SpawnType.TutorialPort => GetTutorialPortSpawn(),
                SpawnType.LastDockedPort => GetLastDockedPortSpawn(playerData),
                SpawnType.RespawnPort => GetRespawnPortSpawn(playerData),
                SpawnType.DesignatedPort => GetDesignatedPortSpawn(playerData),
                _ => GetDefaultSpawn()
            };
        }

        private SpawnType DetermineSpawnType(PlayerData playerData)
        {
            // First-time player detection
            if (playerData.IsNewPlayer || playerData.TutorialComplete == false)
            {
                return SpawnType.TutorialPort;
            }

            // Ship destroyed - respawn at insurance port
            if (playerData.ShipDestroyed)
            {
                return SpawnType.RespawnPort;
            }

            // Normal case - return to last docked port
            if (!string.IsNullOrEmpty(playerData.LastDockedPortId))
            {
                return SpawnType.LastDockedPort;
            }

            return SpawnType.TutorialPort; // Fallback
        }

        private Vector3 GetTutorialPortSpawn()
        {
            // Tutorial port is always a T3 port with full services
            var spawnPoint = portSpawnPoints.FirstOrDefault(p => p.name.Contains("Tutorial"));
            return spawnPoint != null ? spawnPoint.position : Vector3.zero;
        }

        private Vector3 GetLastDockedPortSpawn(PlayerData playerData)
        {
            var port = PortManager.Instance.GetPort(playerData.LastDockedPortId);
            if (port != null)
            {
                return port.GetRandomSpawnPoint();
            }
            return GetTutorialPortSpawn(); // Fallback
        }

        private Vector3 GetRespawnPortSpawn(PlayerData playerData)
        {
            // Find nearest friendly port, or insurance designated port
            var insurancePort = PortManager.Instance.GetPort(playerData.InsurancePortId);
            if (insurancePort != null)
            {
                return insurancePort.GetRandomSpawnPoint();
            }
            return GetTutorialPortSpawn(); // Fallback
        }
    }
}
```

### WOSNetworkManager Modifications

```csharp
// Modifications to Assets/Scripts/Networking/WOSNetworkManager.cs
// Add to existing OnServerAddPlayer method:

public override void OnServerAddPlayer(NetworkConnectionToClient conn)
{
    // Get player data from PlayFab/database
    PlayerData playerData = GetPlayerData(conn);

    // Get spawn position from Port system (NEW)
    Vector3 spawnPosition = playerSpawnManager.GetSpawnPosition(playerData);
    Quaternion spawnRotation = Quaternion.identity;

    // Spawn player at port
    GameObject playerShip = Instantiate(playerPrefab, spawnPosition, spawnRotation);
    NetworkServer.AddPlayerForConnection(conn, playerShip);

    // Initialize player in docked state (NEW)
    var shipController = playerShip.GetComponent<NetworkedNavalController>();
    shipController.SetDockedState(true);

    // Notify port of player arrival
    PortManager.Instance.OnPlayerDocked(playerShip, playerData.LastDockedPortId);
}
```

---

## 1.3 Fitting Restriction System

### FittingRestrictionManager

**GDD Requirement**: Equipment fitting ONLY available in Port

```csharp
// Assets/Scripts/Port/FittingRestrictionManager.cs
namespace WOS.Port
{
    public class FittingRestrictionManager : MonoBehaviour
    {
        public static FittingRestrictionManager Instance { get; private set; }

        [Header("State")]
        [SerializeField] private bool isPlayerInPort = false;
        [SerializeField] private PortConfigurationSO currentPort;

        public bool CanModifyEquipment => isPlayerInPort && HasFittingService;
        public bool CanAccessStorage => isPlayerInPort && HasStorageService;
        public bool CanModifyCrew => isPlayerInPort && HasFittingService;

        private bool HasFittingService => currentPort != null &&
            currentPort.availableServices.HasFlag(PortServices.Fitting);
        private bool HasStorageService => currentPort != null &&
            currentPort.availableServices.HasFlag(PortServices.Storage);

        public event Action<bool> OnFittingAccessChanged;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }
            Instance = this;
        }

        public void OnPlayerEnteredPort(PortConfigurationSO port)
        {
            isPlayerInPort = true;
            currentPort = port;
            OnFittingAccessChanged?.Invoke(true);
        }

        public void OnPlayerLeftPort()
        {
            isPlayerInPort = false;
            currentPort = null;
            OnFittingAccessChanged?.Invoke(false);
        }

        /// <summary>
        /// Call this before any equipment modification operation
        /// </summary>
        public FittingRestrictionResult CheckFittingAllowed()
        {
            if (!isPlayerInPort)
            {
                return new FittingRestrictionResult
                {
                    IsAllowed = false,
                    Reason = FittingBlockReason.NotInPort,
                    Message = "Must be docked at a port to modify equipment"
                };
            }

            if (!HasFittingService)
            {
                return new FittingRestrictionResult
                {
                    IsAllowed = false,
                    Reason = FittingBlockReason.PortLacksFittingService,
                    Message = $"{currentPort.portName} does not have fitting facilities"
                };
            }

            return new FittingRestrictionResult
            {
                IsAllowed = true,
                Reason = FittingBlockReason.None,
                Message = string.Empty
            };
        }
    }

    public struct FittingRestrictionResult
    {
        public bool IsAllowed;
        public FittingBlockReason Reason;
        public string Message;
    }

    public enum FittingBlockReason
    {
        None,
        NotInPort,
        PortLacksFittingService,
        ShipDamaged,
        InCombat
    }
}
```

### UI Integration

```csharp
// Modifications to Ship Fitting UI screens
// Each screen must check FittingRestrictionManager before allowing changes

public class BaseShipFittingScreen : MonoBehaviour
{
    protected bool CanMakeChanges => FittingRestrictionManager.Instance.CanModifyEquipment;

    protected virtual void OnEnable()
    {
        FittingRestrictionManager.Instance.OnFittingAccessChanged += HandleFittingAccessChanged;
        UpdateInteractability();
    }

    protected virtual void OnDisable()
    {
        if (FittingRestrictionManager.Instance != null)
            FittingRestrictionManager.Instance.OnFittingAccessChanged -= HandleFittingAccessChanged;
    }

    protected virtual void HandleFittingAccessChanged(bool canFit)
    {
        UpdateInteractability();
    }

    protected virtual void UpdateInteractability()
    {
        // Override in derived classes to enable/disable UI elements
        if (!CanMakeChanges)
        {
            ShowRestrictionOverlay();
        }
        else
        {
            HideRestrictionOverlay();
        }
    }

    protected void ShowRestrictionOverlay()
    {
        var result = FittingRestrictionManager.Instance.CheckFittingAllowed();
        restrictionOverlay.SetActive(true);
        restrictionMessageText.text = result.Message;
    }

    protected void HideRestrictionOverlay()
    {
        restrictionOverlay.SetActive(false);
    }
}
```

---

## 1.4 Port Safe Zone Implementation

```csharp
// Assets/Scripts/World/Ports/PortSafeZone.cs
namespace WOS.World.Ports
{
    public class PortSafeZone : MonoBehaviour
    {
        [Header("Configuration")]
        [SerializeField] private PortConfigurationSO portConfig;
        [SerializeField] private SphereCollider safeZoneTrigger;

        [Header("Safe Zone Rules")]
        [SerializeField] private bool disableWeapons = true;
        [SerializeField] private bool disablePvP = true;
        [SerializeField] private bool healOverTime = true;
        [SerializeField] private float healPercentPerMinute = 1f;

        private HashSet<GameObject> shipsInZone = new HashSet<GameObject>();

        private void Awake()
        {
            // Set safe zone radius from port tier
            float radiusKm = PortConfigurationSO.GetSafeZoneRadius(portConfig.tier);
            float radiusUnits = radiusKm * 1000f; // Convert to Unity units (assuming 1 unit = 1m)
            safeZoneTrigger.radius = radiusUnits;
        }

        private void OnTriggerEnter(Collider other)
        {
            if (other.TryGetComponent<PlayerShip>(out var ship))
            {
                shipsInZone.Add(ship.gameObject);
                ApplySafeZoneEffects(ship);
                OnShipEnteredSafeZone?.Invoke(ship, portConfig);
            }
        }

        private void OnTriggerExit(Collider other)
        {
            if (other.TryGetComponent<PlayerShip>(out var ship))
            {
                shipsInZone.Remove(ship.gameObject);
                RemoveSafeZoneEffects(ship);
                OnShipLeftSafeZone?.Invoke(ship, portConfig);
            }
        }

        private void ApplySafeZoneEffects(PlayerShip ship)
        {
            if (disableWeapons)
            {
                ship.SetWeaponsEnabled(false);
            }

            if (disablePvP)
            {
                ship.SetPvPEnabled(false);
            }

            ship.SetInSafeZone(true, portConfig);
        }

        private void RemoveSafeZoneEffects(PlayerShip ship)
        {
            ship.SetWeaponsEnabled(true);
            ship.SetPvPEnabled(true);
            ship.SetInSafeZone(false, null);
        }

        public static event Action<PlayerShip, PortConfigurationSO> OnShipEnteredSafeZone;
        public static event Action<PlayerShip, PortConfigurationSO> OnShipLeftSafeZone;
    }
}
```

---

## 1.5 Undocking Prerequisites

```csharp
// Assets/Scripts/Port/UndockingValidator.cs
namespace WOS.Port
{
    public class UndockingValidator : MonoBehaviour
    {
        [Header("References")]
        [SerializeField] private HardCapWeightManager weightManager;
        [SerializeField] private CrewManager crewManager;
        [SerializeField] private FuelManager fuelManager;

        public UndockValidationResult ValidateUndocking()
        {
            var result = new UndockValidationResult();
            result.Errors = new List<string>();
            result.Warnings = new List<string>();

            // Check 1: Weight HARD CAP (CRITICAL - cannot undock at 100%+)
            if (!weightManager.CanUndock())
            {
                result.CanUndock = false;
                result.Errors.Add($"Ship is overweight ({weightManager.WeightPercentage:F1}%). Maximum is 100%.");
            }

            // Check 2: Minimum crew (WARNING if not met, but can still undock)
            if (crewManager.TotalSailors < crewManager.MinimumOperatingCrew)
            {
                result.Warnings.Add($"Ship is understaffed ({crewManager.TotalSailors}/{crewManager.MinimumOperatingCrew}). Some systems may not function.");
            }

            // Check 3: Unmanned modules (WARNING)
            var unmannedModules = GetUnmannedModules();
            if (unmannedModules.Count > 0)
            {
                result.Warnings.Add($"{unmannedModules.Count} modules have no crew assigned and will be non-functional.");
            }

            // Check 4: Fuel (WARNING if low, ERROR if zero)
            if (fuelManager.CurrentFuel <= 0)
            {
                result.CanUndock = false;
                result.Errors.Add("No fuel! Cannot leave port.");
            }
            else if (fuelManager.FuelPercentage < 20f)
            {
                result.Warnings.Add($"Low fuel ({fuelManager.FuelPercentage:F0}%). Consider refueling.");
            }

            // Final result
            if (result.Errors.Count == 0)
            {
                result.CanUndock = true;
            }

            return result;
        }

        private List<ModuleDefinitionSO> GetUnmannedModules()
        {
            // Return list of installed modules with no crew assigned
            // (Implementation depends on equipment tracking system)
            return new List<ModuleDefinitionSO>();
        }
    }

    public class UndockValidationResult
    {
        public bool CanUndock;
        public List<string> Errors;
        public List<string> Warnings;
    }
}
```

---

## Phase 1 Validation Checklist

```
Port Tier System
[ ] PortTier enum with 10 tiers
[ ] PortConfigurationSO with all fields
[ ] Safe zone radius calculation (10/25/50 km)
[ ] Storage capacity calculation (500/750/1000)
[ ] PortServices flags working

Player Spawn
[ ] First-time players spawn at tutorial port
[ ] Returning players spawn at last docked port
[ ] Destroyed ship respawns at insurance port
[ ] Spawn position is inside port (docked state)

Fitting Restrictions
[ ] FittingRestrictionManager singleton working
[ ] Equipment changes blocked when at sea
[ ] UI shows restriction message when blocked
[ ] All 5 fitting screens respect restrictions

Safe Zones
[ ] Safe zone collider matches tier radius
[ ] Weapons disabled in safe zone
[ ] PvP disabled in safe zone
[ ] Visual indicator when in safe zone

Undocking
[ ] Weight hard cap prevents undocking at 100%+
[ ] Crew warnings displayed but don't block
[ ] Fuel check prevents undocking with no fuel
[ ] Confirmation dialog shows all warnings
```

---

*Phase 1: Port Integration - Version 3.0*
