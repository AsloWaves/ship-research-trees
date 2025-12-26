# Phase 3: Cargo & Storage Grids (True Tetris)

**Goal**: Implement Tetris-style grids for cargo and port storage with HARD CAP weight and partition system

**NOTE**: This phase implements **TRUE TETRIS** mechanics, which is different from the Slot-Matching system in Phase 2:
- Tetris = freeform placement, rotation, collision detection
- Dual constraints: Grid cells + Weight limit (ship cargo only)

---

## 3.1 Hard Cap Weight Manager

```csharp
// Assets/Scripts/Inventory/HardCapWeightManager.cs
namespace WOS.Inventory
{
    /// <summary>
    /// GDD: HARD CAP at 100% - Cannot exceed ship weight capacity
    /// This is NOT a soft cap with penalties - exceeding is BLOCKED
    /// </summary>
    public class HardCapWeightManager : MonoBehaviour, IHardCapWeightSystem
    {
        [Header("Configuration")]
        [SerializeField] private float maxWeightTons;

        [Header("Debug Display")]
        [SerializeField] private float currentWeightTons;

        // IHardCapWeightSystem implementation
        public float CurrentWeightTons => currentWeightTons;
        public float MaxWeightTons => maxWeightTons;
        public float WeightPercentage => maxWeightTons > 0 ? (currentWeightTons / maxWeightTons) * 100f : 0f;
        public bool IsAtHardCap => currentWeightTons >= maxWeightTons;

        // Remaining capacity
        public float RemainingCapacityTons => Mathf.Max(0, maxWeightTons - currentWeightTons);

        // Weight band for UI coloring
        public WeightBand CurrentWeightBand
        {
            get
            {
                float pct = WeightPercentage;
                if (pct >= 100f) return WeightBand.HardCap;
                if (pct >= 95f) return WeightBand.AtLimit;
                if (pct >= 80f) return WeightBand.NearLimit;
                return WeightBand.Optimal;
            }
        }

        public event Action<float, float> OnWeightChanged;
        public event Action OnHardCapReached;
        public event Action<WeightBand> OnWeightBandChanged;

        private WeightBand previousBand;

        public void Initialize(float maxWeight)
        {
            maxWeightTons = maxWeight;
            currentWeightTons = 0f;
            previousBand = WeightBand.Optimal;
        }

        /// <summary>
        /// GDD Rule: Cannot pick up cargo that would exceed 100%
        /// </summary>
        public bool CanAddWeight(float additionalWeightTons)
        {
            return (currentWeightTons + additionalWeightTons) <= maxWeightTons;
        }

        /// <summary>
        /// GDD Rule: Cannot undock at 100%+ weight
        /// </summary>
        public bool CanUndock()
        {
            return currentWeightTons <= maxWeightTons;
        }

        /// <summary>
        /// Attempt to add weight - returns false if would exceed hard cap
        /// </summary>
        public bool TryAddWeight(float weightTons)
        {
            if (!CanAddWeight(weightTons))
            {
                Debug.Log($"[HardCap] BLOCKED: Cannot add {weightTons:F1}t - would exceed cap " +
                         $"({currentWeightTons + weightTons:F1}/{maxWeightTons:F1})");
                return false;
            }

            currentWeightTons += weightTons;
            NotifyWeightChange();
            return true;
        }

        /// <summary>
        /// Remove weight (always succeeds)
        /// </summary>
        public void RemoveWeight(float weightTons)
        {
            currentWeightTons = Mathf.Max(0, currentWeightTons - weightTons);
            NotifyWeightChange();
        }

        /// <summary>
        /// Set exact weight (for loading saved state)
        /// </summary>
        public void SetWeight(float weightTons)
        {
            currentWeightTons = Mathf.Clamp(weightTons, 0, maxWeightTons);
            NotifyWeightChange();
        }

        private void NotifyWeightChange()
        {
            OnWeightChanged?.Invoke(currentWeightTons, maxWeightTons);

            var newBand = CurrentWeightBand;
            if (newBand != previousBand)
            {
                OnWeightBandChanged?.Invoke(newBand);
                previousBand = newBand;
            }

            if (IsAtHardCap)
            {
                OnHardCapReached?.Invoke();
            }
        }
    }

    public enum WeightBand
    {
        Optimal,     // 0-80%   Green
        NearLimit,   // 80-95%  Yellow
        AtLimit,     // 95-100% Orange
        HardCap      // 100%    Red (cannot add more)
    }
}
```

---

## 3.2 Tetris Grid Base System

```csharp
// Assets/Scripts/Inventory/TetrisGrid/TetrisGridBase.cs
namespace WOS.Inventory.TetrisGrid
{
    /// <summary>
    /// Base implementation of true Tetris-style grid
    /// Used for both ship cargo and port storage
    /// </summary>
    public abstract class TetrisGridBase : MonoBehaviour, ITetrisGrid
    {
        [Header("Grid Configuration")]
        [SerializeField] protected Vector2Int gridSize;

        protected TetrisCell[,] cells;
        protected List<TetrisItem> placedItems = new List<TetrisItem>();

        // ITetrisGrid implementation
        public Vector2Int GridSize => gridSize;
        public int TotalCells => gridSize.x * gridSize.y;
        public int UsedCells => placedItems.Sum(item => item.OccupiedCellCount);
        public int FreeCells => TotalCells - UsedCells;

        protected virtual void Awake()
        {
            InitializeGrid();
        }

        protected virtual void InitializeGrid()
        {
            cells = new TetrisCell[gridSize.x, gridSize.y];
            for (int x = 0; x < gridSize.x; x++)
            {
                for (int y = 0; y < gridSize.y; y++)
                {
                    cells[x, y] = new TetrisCell { Position = new Vector2Int(x, y) };
                }
            }
        }

        /// <summary>
        /// Check if item can be placed at position (collision + bounds + weight)
        /// </summary>
        public virtual bool CanPlaceItem(ITetrisItem item, Vector2Int position)
        {
            // Check 1: Bounds
            if (!IsWithinBounds(position, item.GridSize))
            {
                return false;
            }

            // Check 2: Collision with existing items
            if (HasCollision(position, item.GridSize, item))
            {
                return false;
            }

            // Check 3: Partition compatibility (if grid has partitions)
            if (!ValidatePartitionPlacement(item, position))
            {
                return false;
            }

            return true;
        }

        protected bool IsWithinBounds(Vector2Int position, Vector2Int size)
        {
            return position.x >= 0 &&
                   position.y >= 0 &&
                   position.x + size.x <= gridSize.x &&
                   position.y + size.y <= gridSize.y;
        }

        protected bool HasCollision(Vector2Int position, Vector2Int size, ITetrisItem excludeItem = null)
        {
            for (int x = position.x; x < position.x + size.x; x++)
            {
                for (int y = position.y; y < position.y + size.y; y++)
                {
                    var cell = cells[x, y];
                    if (cell.OccupyingItem != null && cell.OccupyingItem != excludeItem)
                    {
                        return true;
                    }
                }
            }
            return false;
        }

        protected virtual bool ValidatePartitionPlacement(ITetrisItem item, Vector2Int position)
        {
            // Override in derived classes with partition support
            return true;
        }

        /// <summary>
        /// Place item at position
        /// </summary>
        public virtual void PlaceItem(ITetrisItem item, Vector2Int position)
        {
            if (!CanPlaceItem(item, position))
            {
                Debug.LogError($"[TetrisGrid] Cannot place {item.ItemId} at {position}");
                return;
            }

            var tetrisItem = item as TetrisItem;
            if (tetrisItem == null) return;

            tetrisItem.CurrentPosition = position;

            // Mark cells as occupied
            foreach (var cell in GetCellsForItem(position, tetrisItem.EffectiveSize))
            {
                cells[cell.x, cell.y].OccupyingItem = item;
            }

            placedItems.Add(tetrisItem);
            OnItemPlaced?.Invoke(tetrisItem);
        }

        /// <summary>
        /// Remove item from grid
        /// </summary>
        public virtual void RemoveItem(ITetrisItem item)
        {
            var tetrisItem = item as TetrisItem;
            if (tetrisItem == null || !placedItems.Contains(tetrisItem)) return;

            // Clear cells
            foreach (var cell in GetCellsForItem(tetrisItem.CurrentPosition, tetrisItem.EffectiveSize))
            {
                if (cells[cell.x, cell.y].OccupyingItem == item)
                {
                    cells[cell.x, cell.y].OccupyingItem = null;
                }
            }

            placedItems.Remove(tetrisItem);
            tetrisItem.CurrentPosition = new Vector2Int(-1, -1);
            OnItemRemoved?.Invoke(tetrisItem);
        }

        /// <summary>
        /// Get item at specific cell
        /// </summary>
        public ITetrisItem GetItemAtCell(Vector2Int cell)
        {
            if (cell.x < 0 || cell.x >= gridSize.x || cell.y < 0 || cell.y >= gridSize.y)
                return null;

            return cells[cell.x, cell.y].OccupyingItem;
        }

        /// <summary>
        /// Get all cells an item would occupy at given position
        /// </summary>
        protected IEnumerable<Vector2Int> GetCellsForItem(Vector2Int position, Vector2Int size)
        {
            for (int x = position.x; x < position.x + size.x; x++)
            {
                for (int y = position.y; y < position.y + size.y; y++)
                {
                    yield return new Vector2Int(x, y);
                }
            }
        }

        /// <summary>
        /// Auto-arrange all items for optimal packing
        /// Uses First-Fit Decreasing Height algorithm
        /// </summary>
        public virtual bool TryAutoArrange()
        {
            // Store items and clear grid
            var itemsToArrange = new List<TetrisItem>(placedItems);
            foreach (var item in itemsToArrange)
            {
                RemoveItem(item);
            }

            // Sort by area (largest first)
            itemsToArrange.Sort((a, b) =>
                (b.EffectiveSize.x * b.EffectiveSize.y).CompareTo(a.EffectiveSize.x * a.EffectiveSize.y));

            // Try to place each item
            foreach (var item in itemsToArrange)
            {
                var position = FindFirstAvailablePosition(item);
                if (position.HasValue)
                {
                    PlaceItem(item, position.Value);
                }
                else
                {
                    // Cannot fit all items - restore original state
                    Debug.LogWarning($"[TetrisGrid] Auto-arrange failed - cannot fit {item.ItemId}");
                    return false;
                }
            }

            return true;
        }

        protected Vector2Int? FindFirstAvailablePosition(TetrisItem item)
        {
            // Scan grid from top-left, row by row
            for (int y = 0; y <= gridSize.y - item.EffectiveSize.y; y++)
            {
                for (int x = 0; x <= gridSize.x - item.EffectiveSize.x; x++)
                {
                    var pos = new Vector2Int(x, y);
                    if (CanPlaceItem(item, pos))
                    {
                        return pos;
                    }
                }
            }

            // Try rotated (if not already tried)
            if (!item.IsRotated)
            {
                item.Rotate();
                var rotatedResult = FindFirstAvailablePosition(item);
                if (!rotatedResult.HasValue)
                {
                    item.Rotate(); // Rotate back if no fit
                }
                return rotatedResult;
            }

            return null;
        }

        // Events
        public event Action<TetrisItem> OnItemPlaced;
        public event Action<TetrisItem> OnItemRemoved;
    }

    [Serializable]
    public class TetrisCell
    {
        public Vector2Int Position;
        public ITetrisItem OccupyingItem;
        public CargoPartitionType? Partition;
    }
}
```

---

## 3.3 Ship Cargo Grid (with Weight + Partitions)

```csharp
// Assets/Scripts/Inventory/TetrisGrid/ShipCargoGrid.cs
namespace WOS.Inventory.TetrisGrid
{
    /// <summary>
    /// Ship cargo grid with:
    /// - True Tetris placement
    /// - HARD CAP weight system
    /// - Partition zones (Magazine, Fuel, General, Refrigerated)
    /// - Damage/integrity mechanics
    /// </summary>
    public class ShipCargoGrid : TetrisGridBase
    {
        [Header("Weight System")]
        [SerializeField] private HardCapWeightManager weightManager;

        [Header("Partition Configuration")]
        [SerializeField] private List<CargoPartitionDefinition> partitionDefinitions;

        private Dictionary<CargoPartitionType, List<Vector2Int>> partitionCells;

        protected override void Awake()
        {
            base.Awake();
            InitializePartitions();
        }

        public void Initialize(ShipConfigurationSO shipConfig)
        {
            gridSize = shipConfig.cargoGridSize;
            weightManager.Initialize(shipConfig.maxCargoWeightTons);
            partitionDefinitions = shipConfig.cargoPartitions;

            InitializeGrid();
            InitializePartitions();
        }

        private void InitializePartitions()
        {
            partitionCells = new Dictionary<CargoPartitionType, List<Vector2Int>>();

            foreach (var partition in partitionDefinitions)
            {
                var cellList = new List<Vector2Int>();

                for (int x = partition.gridArea.x; x < partition.gridArea.x + partition.gridArea.width; x++)
                {
                    for (int y = partition.gridArea.y; y < partition.gridArea.y + partition.gridArea.height; y++)
                    {
                        if (x >= 0 && x < gridSize.x && y >= 0 && y < gridSize.y)
                        {
                            cells[x, y].Partition = partition.partitionType;
                            cellList.Add(new Vector2Int(x, y));
                        }
                    }
                }

                if (!partitionCells.ContainsKey(partition.partitionType))
                {
                    partitionCells[partition.partitionType] = new List<Vector2Int>();
                }
                partitionCells[partition.partitionType].AddRange(cellList);
            }
        }

        /// <summary>
        /// Override to add weight check
        /// </summary>
        public override bool CanPlaceItem(ITetrisItem item, Vector2Int position)
        {
            if (!base.CanPlaceItem(item, position))
                return false;

            // Additional check: Weight
            var cargoItem = item as CargoItem;
            if (cargoItem != null)
            {
                if (!weightManager.CanAddWeight(cargoItem.WeightTons))
                {
                    return false;
                }
            }

            return true;
        }

        /// <summary>
        /// Check partition compatibility
        /// </summary>
        protected override bool ValidatePartitionPlacement(ITetrisItem item, Vector2Int position)
        {
            var cargoItem = item as CargoItem;
            if (cargoItem == null) return true;

            // Get partition at placement position
            var partition = GetPartitionAt(position);
            if (partition == null) return true; // No partition = general area

            // Check if item type is allowed in this partition
            var partitionDef = partitionDefinitions.FirstOrDefault(p => p.partitionType == partition.Value);
            if (partitionDef == null) return true;

            // Check prohibited types
            if (partitionDef.prohibitedItemTypes.Contains(cargoItem.ItemType))
            {
                return false;
            }

            // If partition has allowed types list, item must be in it
            if (partitionDef.allowedItemTypes.Count > 0 &&
                !partitionDef.allowedItemTypes.Contains(cargoItem.ItemType))
            {
                return false;
            }

            return true;
        }

        /// <summary>
        /// Override to track weight
        /// </summary>
        public override void PlaceItem(ITetrisItem item, Vector2Int position)
        {
            var cargoItem = item as CargoItem;
            if (cargoItem != null)
            {
                if (!weightManager.TryAddWeight(cargoItem.WeightTons))
                {
                    Debug.LogError($"[CargoGrid] Cannot place {item.ItemId} - would exceed weight cap");
                    return;
                }
            }

            base.PlaceItem(item, position);
        }

        /// <summary>
        /// Override to track weight removal
        /// </summary>
        public override void RemoveItem(ITetrisItem item)
        {
            var cargoItem = item as CargoItem;
            if (cargoItem != null)
            {
                weightManager.RemoveWeight(cargoItem.WeightTons);
            }

            base.RemoveItem(item);
        }

        public CargoPartitionType? GetPartitionAt(Vector2Int position)
        {
            if (position.x < 0 || position.x >= gridSize.x ||
                position.y < 0 || position.y >= gridSize.y)
                return null;

            return cells[position.x, position.y].Partition;
        }

        public PlacementResult GetPlacementResult(CargoItem item, Vector2Int position)
        {
            // Check bounds
            if (!IsWithinBounds(position, item.EffectiveSize))
                return PlacementResult.OutOfBounds;

            // Check collision
            if (HasCollision(position, item.EffectiveSize, item))
                return PlacementResult.Collision;

            // Check partition
            if (!ValidatePartitionPlacement(item, position))
                return PlacementResult.WrongPartition;

            // Check weight
            if (!weightManager.CanAddWeight(item.WeightTons))
                return PlacementResult.ExceedsWeightCap;

            return PlacementResult.Valid;
        }

        // Weight system accessors
        public float CurrentWeight => weightManager.CurrentWeightTons;
        public float MaxWeight => weightManager.MaxWeightTons;
        public float WeightPercentage => weightManager.WeightPercentage;
        public bool IsAtHardCap => weightManager.IsAtHardCap;
        public WeightBand CurrentWeightBand => weightManager.CurrentWeightBand;
    }

    public enum PlacementResult
    {
        Valid,
        OutOfBounds,
        Collision,
        WrongPartition,
        ExceedsWeightCap
    }
}
```

---

## 3.4 Port Storage Grid (No Weight Limit)

```csharp
// Assets/Scripts/Inventory/TetrisGrid/PortStorageGrid.cs
namespace WOS.Inventory.TetrisGrid
{
    /// <summary>
    /// Port storage grid with:
    /// - True Tetris placement
    /// - NO weight limit (grid cells only)
    /// - Tier-based capacity (500/750/1000 cells)
    /// - Per-port separate storage
    /// </summary>
    public class PortStorageGrid : TetrisGridBase
    {
        [Header("Port Configuration")]
        [SerializeField] private string portId;
        [SerializeField] private PortTier portTier;

        public string PortId => portId;
        public PortTier Tier => portTier;

        public void Initialize(PortConfigurationSO portConfig)
        {
            portId = portConfig.portId;
            portTier = portConfig.tier;

            // Calculate grid size from tier capacity
            int capacity = PortConfigurationSO.GetStorageCapacity(portTier);
            gridSize = CalculateGridDimensions(capacity);

            InitializeGrid();
        }

        private Vector2Int CalculateGridDimensions(int targetCells)
        {
            // Create roughly square grid
            int width = Mathf.CeilToInt(Mathf.Sqrt(targetCells));
            int height = Mathf.CeilToInt((float)targetCells / width);
            return new Vector2Int(width, height);
        }

        /// <summary>
        /// Port storage has NO weight limit - only grid space matters
        /// </summary>
        public bool CanStoreItem(CargoItem item)
        {
            // Only check if there's grid space - no weight check
            return FreeCells >= item.OccupiedCellCount;
        }

        /// <summary>
        /// Find any valid position for item
        /// </summary>
        public Vector2Int? FindStoragePosition(CargoItem item)
        {
            return FindFirstAvailablePosition(item);
        }
    }
}
```

---

## 3.5 Cargo Item Definition

```csharp
// Assets/Scripts/Inventory/TetrisGrid/CargoItem.cs
namespace WOS.Inventory.TetrisGrid
{
    public class CargoItem : MonoBehaviour, ITetrisItem
    {
        [Header("Item Identity")]
        [SerializeField] private string itemId;
        [SerializeField] private string itemName;
        [SerializeField] private CargoItemType itemType;
        [SerializeField] private Sprite itemIcon;

        [Header("Grid Properties")]
        [SerializeField] private Vector2Int baseGridSize;
        [SerializeField] private bool isRotated;

        [Header("Physical Properties")]
        [SerializeField] private float weightTons;
        [SerializeField] private float valueCurrency;

        [Header("Stacking")]
        [SerializeField] private bool isStackable;
        [SerializeField] private int stackLimit = 1;
        [SerializeField] private int currentStackCount = 1;

        [Header("State")]
        [SerializeField] private Vector2Int currentPosition = new Vector2Int(-1, -1);
        [SerializeField] private float integrity = 100f; // Damage system

        // ITetrisItem implementation
        public string ItemId => itemId;
        public Vector2Int GridSize => baseGridSize;
        public bool IsRotated => isRotated;
        public Vector2Int CurrentPosition
        {
            get => currentPosition;
            set => currentPosition = value;
        }

        // Additional properties
        public CargoItemType ItemType => itemType;
        public float WeightTons => weightTons * currentStackCount;
        public float ValueCurrency => valueCurrency * currentStackCount;
        public Vector2Int EffectiveSize => isRotated ?
            new Vector2Int(baseGridSize.y, baseGridSize.x) : baseGridSize;
        public int OccupiedCellCount => EffectiveSize.x * EffectiveSize.y;
        public float Integrity => integrity;
        public bool IsStackable => isStackable;
        public int StackLimit => stackLimit;
        public int StackCount => currentStackCount;

        /// <summary>
        /// Rotate item 90 degrees clockwise
        /// GDD: R key to rotate during placement
        /// </summary>
        public void Rotate()
        {
            isRotated = !isRotated;
        }

        public IEnumerable<Vector2Int> GetOccupiedCells(Vector2Int position)
        {
            var size = EffectiveSize;
            for (int x = 0; x < size.x; x++)
            {
                for (int y = 0; y < size.y; y++)
                {
                    yield return new Vector2Int(position.x + x, position.y + y);
                }
            }
        }

        /// <summary>
        /// Apply damage to cargo (combat system integration)
        /// </summary>
        public void ApplyDamage(float damagePercent)
        {
            integrity = Mathf.Max(0, integrity - damagePercent);

            if (integrity <= 0)
            {
                OnCargoDestroyed?.Invoke(this);
            }
            else if (integrity < 50)
            {
                OnCargoDamaged?.Invoke(this);
            }
        }

        /// <summary>
        /// Try to add to stack (returns amount that couldn't be added)
        /// </summary>
        public int TryAddToStack(int amount)
        {
            if (!isStackable) return amount;

            int canAdd = Mathf.Min(amount, stackLimit - currentStackCount);
            currentStackCount += canAdd;
            return amount - canAdd;
        }

        /// <summary>
        /// Remove from stack (returns actual amount removed)
        /// </summary>
        public int RemoveFromStack(int amount)
        {
            int toRemove = Mathf.Min(amount, currentStackCount - 1);
            currentStackCount -= toRemove;
            return toRemove;
        }

        // Events
        public event Action<CargoItem> OnCargoDamaged;
        public event Action<CargoItem> OnCargoDestroyed;
    }
}
```

---

## 3.6 Transfer System

```csharp
// Assets/Scripts/Inventory/Transfer/CargoTransferManager.cs
namespace WOS.Inventory.Transfer
{
    /// <summary>
    /// Handles transfers between Ship Cargo and Port Storage
    /// GDD Rules:
    /// - Ship → Port: No weight restriction (port has no weight limit)
    /// - Port → Ship: Must check weight hard cap
    /// - Drag-drop between windows
    /// - Quick transfer buttons (Transfer All, Transfer Selected)
    /// </summary>
    public class CargoTransferManager : MonoBehaviour
    {
        [Header("References")]
        [SerializeField] private ShipCargoGrid shipCargo;
        [SerializeField] private PortStorageGrid portStorage;

        public bool CanTransferToShip(CargoItem item)
        {
            // Check ship weight capacity
            if (!shipCargo.CanAddWeight(item.WeightTons))
            {
                return false;
            }

            // Check ship has grid space
            var pos = shipCargo.FindFirstAvailablePosition(item);
            return pos.HasValue;
        }

        public bool CanTransferToPort(CargoItem item)
        {
            // Port has no weight limit - only grid space
            return portStorage.CanStoreItem(item);
        }

        public TransferResult TransferToShip(CargoItem item)
        {
            if (!FittingRestrictionManager.Instance.CanAccessStorage)
            {
                return new TransferResult { Success = false, Message = "Not docked at port" };
            }

            if (!shipCargo.CanAddWeight(item.WeightTons))
            {
                return new TransferResult
                {
                    Success = false,
                    Message = $"Would exceed ship weight capacity ({shipCargo.WeightPercentage:F1}%)"
                };
            }

            var position = shipCargo.FindFirstAvailablePosition(item);
            if (!position.HasValue)
            {
                return new TransferResult { Success = false, Message = "No room in cargo hold" };
            }

            // Execute transfer
            portStorage.RemoveItem(item);
            shipCargo.PlaceItem(item, position.Value);

            return new TransferResult { Success = true, Message = "Transferred to ship" };
        }

        public TransferResult TransferToPort(CargoItem item)
        {
            if (!FittingRestrictionManager.Instance.CanAccessStorage)
            {
                return new TransferResult { Success = false, Message = "Not docked at port" };
            }

            var position = portStorage.FindStoragePosition(item);
            if (!position.HasValue)
            {
                return new TransferResult { Success = false, Message = "Port storage is full" };
            }

            // Execute transfer
            shipCargo.RemoveItem(item);
            portStorage.PlaceItem(item, position.Value);

            return new TransferResult { Success = true, Message = "Transferred to port" };
        }

        /// <summary>
        /// GDD: "Transfer All" button
        /// </summary>
        public BatchTransferResult TransferAllToPort()
        {
            var result = new BatchTransferResult();
            var itemsToTransfer = new List<CargoItem>(shipCargo.GetAllItems());

            foreach (var item in itemsToTransfer)
            {
                var transferResult = TransferToPort(item);
                if (transferResult.Success)
                {
                    result.SuccessCount++;
                }
                else
                {
                    result.FailCount++;
                    result.FailReasons.Add($"{item.ItemId}: {transferResult.Message}");
                }
            }

            return result;
        }

        /// <summary>
        /// GDD: "Transfer All" button (port to ship)
        /// </summary>
        public BatchTransferResult TransferAllToShip()
        {
            var result = new BatchTransferResult();
            var itemsToTransfer = new List<CargoItem>(portStorage.GetAllItems());

            foreach (var item in itemsToTransfer)
            {
                var transferResult = TransferToShip(item);
                if (transferResult.Success)
                {
                    result.SuccessCount++;
                }
                else
                {
                    result.FailCount++;
                    result.FailReasons.Add($"{item.ItemId}: {transferResult.Message}");
                    break; // Stop on first failure (usually weight limit)
                }
            }

            return result;
        }
    }

    public struct TransferResult
    {
        public bool Success;
        public string Message;
    }

    public class BatchTransferResult
    {
        public int SuccessCount;
        public int FailCount;
        public List<string> FailReasons = new List<string>();
    }
}
```

---

## 3.7 Cargo Damage System

```csharp
// Assets/Scripts/Inventory/Damage/CargoDamageManager.cs
namespace WOS.Inventory.Damage
{
    /// <summary>
    /// Handles cargo damage from combat
    /// GDD Rules:
    /// - Magazine hit → explosion risk
    /// - Fuel hit → fire risk
    /// - Damaged cargo loses value
    /// </summary>
    public class CargoDamageManager : MonoBehaviour
    {
        [Header("References")]
        [SerializeField] private ShipCargoGrid cargoGrid;

        [Header("Risk Configuration")]
        [SerializeField] private float magazineExplosionChance = 0.3f;
        [SerializeField] private float fuelFireChance = 0.5f;

        public void OnCompartmentHit(Vector2Int gridPosition, float damageAmount)
        {
            // Get items in hit area
            var hitItem = cargoGrid.GetItemAtCell(gridPosition) as CargoItem;
            if (hitItem == null) return;

            // Apply damage to item
            hitItem.ApplyDamage(damageAmount);

            // Check partition risks
            var partition = cargoGrid.GetPartitionAt(gridPosition);
            if (partition.HasValue)
            {
                HandlePartitionRisk(partition.Value, hitItem, damageAmount);
            }
        }

        private void HandlePartitionRisk(CargoPartitionType partition, CargoItem item, float damage)
        {
            switch (partition)
            {
                case CargoPartitionType.Magazine:
                    if (Random.value < magazineExplosionChance * (damage / 100f))
                    {
                        TriggerMagazineExplosion(item);
                    }
                    break;

                case CargoPartitionType.FuelBunker:
                    if (Random.value < fuelFireChance * (damage / 100f))
                    {
                        TriggerFuelFire(item);
                    }
                    break;
            }
        }

        private void TriggerMagazineExplosion(CargoItem item)
        {
            Debug.Log($"[CargoDamage] MAGAZINE EXPLOSION! Item: {item.ItemId}");
            OnMagazineExplosion?.Invoke(item);
            // This could trigger massive ship damage or instant destruction
        }

        private void TriggerFuelFire(CargoItem item)
        {
            Debug.Log($"[CargoDamage] FUEL FIRE! Item: {item.ItemId}");
            OnFuelFire?.Invoke(item);
            // This starts spreading fire damage
        }

        public event Action<CargoItem> OnMagazineExplosion;
        public event Action<CargoItem> OnFuelFire;
    }
}
```

---

## Phase 3 Validation Checklist

```
Hard Cap Weight System
[ ] Cannot add cargo exceeding 100%
[ ] Cannot undock at 100%+
[ ] Weight bands update correctly (0-80-95-100)
[ ] Events fire on weight change

Tetris Grid
[ ] Freeform placement works
[ ] R key rotation works
[ ] Collision detection accurate
[ ] Bounds checking accurate
[ ] Auto-arrange algorithm functional

Ship Cargo Grid
[ ] Inherits Tetris grid behavior
[ ] Weight validation on placement
[ ] Partition zones defined
[ ] Partition validation works
[ ] Items only place in allowed partitions

Port Storage
[ ] No weight limit (grid only)
[ ] Capacity matches tier (500/750/1000)
[ ] Per-port separate storage
[ ] Storage persists between sessions

Transfer System
[ ] Ship → Port ignores weight
[ ] Port → Ship checks weight hard cap
[ ] Transfer All button works
[ ] Transfer Selected button works
[ ] Drag-drop between grids works

Damage System
[ ] Cargo takes damage from combat hits
[ ] Magazine explosion chance
[ ] Fuel fire chance
[ ] Damaged cargo loses value
```

---

*Phase 3: Cargo & Storage Grids - Version 3.0*
