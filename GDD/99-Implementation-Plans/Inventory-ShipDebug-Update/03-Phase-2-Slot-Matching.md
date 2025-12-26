# Phase 2: Slot-Matching Equipment System

**Goal**: Implement GDD-compliant slot-matching for equipment (NOT Tetris)

**CRITICAL**: This phase implements **SLOT-MATCHING**, which is fundamentally different from Tetris:
- Tetris = freeform placement, rotation, collision detection
- Slot-Matching = fixed slots, exact category + dimension match required

---

## 2.1 Validation Order (GDD-Compliant)

The GDD specifies a strict validation order that MUST be followed:

```
EQUIPMENT SLOT VALIDATION ORDER
===============================

Step 0: CATEGORY CHECK (FIRST - Often overlooked!)
  └── Module category == Slot category?
      ├── YES → Continue to Step 1
      └── NO → RED HIGHLIGHT "Wrong module type for this slot"

      Example: Cannot put Engine module in Main Battery slot
               even if dimensions match

Step 1: GRID DIMENSION CHECK
  └── Module dimension == Slot dimension? (EXACT MATCH)
      ├── YES → Continue to Step 2
      └── NO → RED HIGHLIGHT "Module size [X×Y] does not fit slot [A×B]"

      Note: NO rotation allowed. 2×3 module cannot fit in 3×2 slot.

Step 2: WEIGHT CHECK (Module Only)
  └── Module weight ≤ Slot weight capacity?
      ├── YES → Module CAN be installed
      └── NO → RED HIGHLIGHT "Module too heavy for this mount"

Step 3: CREW ASSIGNMENT (Optional - After Installation)
  └── Player drags crew card to installed module
      └── Module weight + Crew weight ≤ Slot weight capacity?
          ├── YES → Crew assigned, module operational
          └── NO → RED HIGHLIGHT "Crew assignment would exceed mount capacity"

IMPORTANT: Module can be INSTALLED at Step 2 without crew,
          but will be NON-FUNCTIONAL until crew assigned at Step 3.
```

---

## 2.2 SlotMatchingValidator Implementation

```csharp
// Assets/Scripts/Inventory/Validation/SlotMatchingValidator.cs
namespace WOS.Inventory.Validation
{
    public class SlotMatchingValidator : ISlotMatchingValidator
    {
        /// <summary>
        /// GDD Rule: Module category MUST match slot category
        /// This is checked FIRST, before dimension or weight
        /// </summary>
        public bool ValidateCategoryMatch(EquipmentSlotCategory moduleCategory, EquipmentSlotCategory slotCategory)
        {
            // Exact match required
            return moduleCategory == slotCategory;
        }

        /// <summary>
        /// GDD Rule: Module dimension MUST EXACTLY MATCH slot dimension
        /// NO rotation allowed - this is NOT Tetris
        /// </summary>
        public bool ValidateDimensionMatch(Vector2Int moduleDim, Vector2Int slotDim)
        {
            // Exact match required - no rotation, no flexibility
            // 2x3 module CANNOT fit in 3x2 slot
            return moduleDim.x == slotDim.x && moduleDim.y == slotDim.y;
        }

        /// <summary>
        /// GDD Rule: Module weight must fit within slot capacity
        /// </summary>
        public bool ValidateModuleWeight(float moduleWeight, float slotCapacity)
        {
            return moduleWeight <= slotCapacity;
        }

        /// <summary>
        /// GDD Rule: Module weight + Crew weight ≤ Slot capacity
        /// </summary>
        public bool ValidateTotalWeight(float moduleWeight, float crewWeight, float slotCapacity)
        {
            return (moduleWeight + crewWeight) <= slotCapacity;
        }

        /// <summary>
        /// Complete validation following GDD order: Category → Dimension → Weight → Crew
        /// </summary>
        public SlotValidationResult ValidateComplete(
            ModuleDefinitionSO module,
            CrewCard crew,
            EquipmentSlotDefinition slot)
        {
            var result = new SlotValidationResult { IsValid = true };

            // Step 0: Category check (FIRST!)
            result.CategoryMatch = ValidateCategoryMatch(module.SlotCategory, slot.category);
            if (!result.CategoryMatch)
            {
                result.IsValid = false;
                result.FailedAtStep = SlotValidationStep.Category;
                result.FailureReason = $"Module type [{module.SlotCategory}] cannot be installed in [{slot.category}] slot";
                return result;
            }

            // Step 1: Dimension check
            result.DimensionMatch = ValidateDimensionMatch(module.GridSize, slot.requiredDimension);
            if (!result.DimensionMatch)
            {
                result.IsValid = false;
                result.FailedAtStep = SlotValidationStep.Dimension;
                result.FailureReason = $"Module size [{module.GridSize.x}×{module.GridSize.y}] does not match slot [{slot.requiredDimension.x}×{slot.requiredDimension.y}]";
                return result;
            }

            // Step 2: Module weight check
            result.ModuleWeightOk = ValidateModuleWeight(module.WeightTons, slot.weightCapacityTons);
            if (!result.ModuleWeightOk)
            {
                result.IsValid = false;
                result.FailedAtStep = SlotValidationStep.ModuleWeight;
                result.FailureReason = $"Module ({module.WeightTons:F1}t) exceeds slot capacity ({slot.weightCapacityTons:F1}t)";
                return result;
            }

            // Step 3: Crew weight check (only if crew provided)
            if (crew != null)
            {
                float crewWeight = CalculateCrewWeight(crew);
                float totalWeight = module.WeightTons + crewWeight;

                result.CrewWeightOk = ValidateTotalWeight(module.WeightTons, crewWeight, slot.weightCapacityTons);
                if (!result.CrewWeightOk)
                {
                    result.IsValid = false;
                    result.FailedAtStep = SlotValidationStep.CrewWeight;
                    result.FailureReason = $"Module + Crew ({totalWeight:F1}t) exceeds slot capacity ({slot.weightCapacityTons:F1}t)";
                    return result;
                }
            }
            else
            {
                result.CrewWeightOk = true; // No crew = no crew weight check needed
            }

            result.FailedAtStep = SlotValidationStep.None;
            return result;
        }

        /// <summary>
        /// GDD Formula: Crew_Weight = Sailor_Count × 0.1 × (1.0 + Level/100)
        /// </summary>
        private float CalculateCrewWeight(CrewCard crew)
        {
            return crew.MaxSailors * 0.1f * (1.0f + crew.Level / 100.0f);
        }

        /// <summary>
        /// Quick check if module can be installed (ignoring crew)
        /// Used for drag-over highlighting
        /// </summary>
        public SlotValidationResult ValidateInstallation(ModuleDefinitionSO module, EquipmentSlotDefinition slot)
        {
            return ValidateComplete(module, null, slot);
        }

        /// <summary>
        /// Check if crew can be assigned to already-installed module
        /// </summary>
        public bool ValidateCrewAssignment(ModuleDefinitionSO installedModule, CrewCard crew, EquipmentSlotDefinition slot)
        {
            float crewWeight = CalculateCrewWeight(crew);
            return ValidateTotalWeight(installedModule.WeightTons, crewWeight, slot.weightCapacityTons);
        }
    }
}
```

---

## 2.3 Module Definition Extensions

```csharp
// Additions to Assets/Scripts/ScriptableObjects/Items/ModuleDefinitionSO.cs
namespace WOS.ScriptableObjects.Items
{
    public class ModuleDefinitionSO : ScriptableObject
    {
        [Header("Module Identity")]
        public string moduleId;
        public string moduleName;
        public string moduleDescription;
        public Sprite moduleIcon;

        [Header("Slot-Matching Properties (CRITICAL)")]
        [Tooltip("Must match slot category EXACTLY")]
        public EquipmentSlotCategory slotCategory;

        [Tooltip("Must match slot dimension EXACTLY - no rotation")]
        public Vector2Int gridSize;  // e.g., (3, 4) for a 3×4 module

        [Tooltip("Module base weight in tons")]
        public float weightTons;

        [Header("Crew Requirements")]
        [Tooltip("Which crew stat affects this module's efficiency")]
        public CrewStatType primaryStat;

        [Tooltip("Maximum sailors this module can use")]
        public int maxSailors;

        [Tooltip("Minimum sailors for module to function")]
        public int minSailors;

        [Tooltip("If true, module works at reduced efficiency without crew")]
        public bool canOperateWithoutCrew;

        [Header("Module Statistics")]
        public ModuleStats baseStats;

        [Header("Visual")]
        public GameObject moduleModel;  // 3D model for fitting view
        public Vector3 modelOffset;
        public Vector3 modelRotation;
    }

    [Serializable]
    public class ModuleStats
    {
        // Weapon stats (if applicable)
        public float baseDamage;
        public float baseReloadTime;
        public float baseAccuracy;
        public float range;

        // Engine stats (if applicable)
        public float basePowerOutput;
        public float fuelEfficiency;

        // Support stats (if applicable)
        public float effectRadius;
        public float effectStrength;

        // Common stats
        public float durability;
        public float repairCost;
    }

    public enum CrewStatType
    {
        Gunnery,        // Main/secondary batteries
        Engineering,    // Engines, propulsion
        DamageControl,  // DC systems
        Signaling,      // Radar, comms
        Aviation,       // Aircraft handling
        Medical,        // Medical systems
        Command         // Bridge systems
    }
}
```

---

## 2.4 Equipment Slot UI Component

```csharp
// Assets/Scripts/UI/Inventory/EquipmentSlotUI.cs
namespace WOS.UI.Inventory
{
    public class EquipmentSlotUI : MonoBehaviour, IDropHandler, IPointerEnterHandler, IPointerExitHandler
    {
        [Header("Slot Configuration")]
        [SerializeField] private EquipmentSlotDefinition slotDefinition;

        [Header("Visual Elements")]
        [SerializeField] private Image slotBackground;
        [SerializeField] private Image moduleIcon;
        [SerializeField] private Image crewIndicator;
        [SerializeField] private TextMeshProUGUI slotNameText;
        [SerializeField] private TextMeshProUGUI dimensionText;
        [SerializeField] private TextMeshProUGUI capacityText;
        [SerializeField] private TextMeshProUGUI efficiencyText;
        [SerializeField] private GameObject emptyStateOverlay;
        [SerializeField] private GameObject installedStateOverlay;

        [Header("Visual Feedback Colors")]
        [SerializeField] private Color emptyColor = new Color(0.3f, 0.3f, 0.3f, 1f);
        [SerializeField] private Color validHoverColor = new Color(0.2f, 0.8f, 0.2f, 1f);
        [SerializeField] private Color invalidHoverColor = new Color(0.8f, 0.2f, 0.2f, 1f);
        [SerializeField] private Color installedColor = new Color(0.2f, 0.5f, 0.8f, 1f);
        [SerializeField] private Color unmannedColor = new Color(0.8f, 0.6f, 0.2f, 1f);

        [Header("Slot Type Visual Indicators (per GDD)")]
        [SerializeField] private Color mainBatteryOutline = Color.red;
        [SerializeField] private Color secondaryOutline = new Color(1f, 0.5f, 0f);  // Orange
        [SerializeField] private Color aaOutline = Color.yellow;
        [SerializeField] private Color engineOutline = new Color(0f, 0.8f, 0f);
        [SerializeField] private Color supportOutline = Color.cyan;

        // State
        private ISlotMatchingValidator validator;
        private ModuleDefinitionSO installedModule;
        private CrewCard assignedCrew;
        private SlotVisualState currentVisualState;

        private void Awake()
        {
            validator = new SlotMatchingValidator();
        }

        private void Start()
        {
            RefreshDisplay();
            ApplyCategoryOutline();
        }

        /// <summary>
        /// Display slot info per GDD UI spec
        /// </summary>
        public void RefreshDisplay()
        {
            slotNameText.text = slotDefinition.slotName;
            dimensionText.text = $"[{slotDefinition.requiredDimension.x}×{slotDefinition.requiredDimension.y}]";
            capacityText.text = $"{slotDefinition.weightCapacityTons:F0}t";

            if (installedModule != null)
            {
                emptyStateOverlay.SetActive(false);
                installedStateOverlay.SetActive(true);
                moduleIcon.sprite = installedModule.moduleIcon;
                moduleIcon.enabled = true;

                if (assignedCrew != null)
                {
                    crewIndicator.color = Color.green;
                    float efficiency = CalculateEfficiency();
                    efficiencyText.text = $"{efficiency * 100:F0}%";
                    SetVisualState(SlotVisualState.Manned);
                }
                else
                {
                    crewIndicator.color = unmannedColor;
                    efficiencyText.text = "0%";
                    SetVisualState(SlotVisualState.Unmanned);
                }
            }
            else
            {
                emptyStateOverlay.SetActive(true);
                installedStateOverlay.SetActive(false);
                moduleIcon.enabled = false;
                efficiencyText.text = "-";
                SetVisualState(SlotVisualState.Empty);
            }
        }

        /// <summary>
        /// Apply outline color based on slot category per GDD
        /// </summary>
        private void ApplyCategoryOutline()
        {
            Color outlineColor = slotDefinition.category switch
            {
                EquipmentSlotCategory.MainBattery => mainBatteryOutline,
                EquipmentSlotCategory.SecondaryBattery => secondaryOutline,
                EquipmentSlotCategory.TertiaryBattery or
                EquipmentSlotCategory.AAHeavy or
                EquipmentSlotCategory.AALight => aaOutline,
                EquipmentSlotCategory.EngineRoom or
                EquipmentSlotCategory.Boiler => engineOutline,
                _ => supportOutline
            };

            // Apply to outline image or shader
            GetComponent<Outline>()?.SetColor(outlineColor);
        }

        /// <summary>
        /// Called when module is dragged over this slot
        /// GDD: Show immediate visual feedback for validation
        /// </summary>
        public void OnPointerEnter(PointerEventData eventData)
        {
            if (DragDropManager.Instance.IsDraggingModule)
            {
                var draggedModule = DragDropManager.Instance.DraggedModule;
                var result = validator.ValidateInstallation(draggedModule, slotDefinition);

                if (result.IsValid)
                {
                    SetVisualState(SlotVisualState.ValidHover);
                    ShowTooltip("Click to install");
                }
                else
                {
                    SetVisualState(SlotVisualState.InvalidHover);
                    ShowTooltip(result.FailureReason);
                }
            }
        }

        public void OnPointerExit(PointerEventData eventData)
        {
            RefreshDisplay(); // Reset to normal state
            HideTooltip();
        }

        /// <summary>
        /// Handle module drop
        /// </summary>
        public void OnDrop(PointerEventData eventData)
        {
            if (!FittingRestrictionManager.Instance.CanModifyEquipment)
            {
                ShowError("Cannot modify equipment - must be docked at a port with fitting services");
                return;
            }

            if (DragDropManager.Instance.IsDraggingModule)
            {
                var draggedModule = DragDropManager.Instance.DraggedModule;
                TryInstallModule(draggedModule);
            }
            else if (DragDropManager.Instance.IsDraggingCrew)
            {
                var draggedCrew = DragDropManager.Instance.DraggedCrew;
                TryAssignCrew(draggedCrew);
            }
        }

        private void TryInstallModule(ModuleDefinitionSO module)
        {
            var result = validator.ValidateInstallation(module, slotDefinition);

            if (result.IsValid)
            {
                // Uninstall existing module first (if any)
                if (installedModule != null)
                {
                    UninstallModule();
                }

                // Install new module
                installedModule = module;
                assignedCrew = null;  // New module has no crew
                RefreshDisplay();

                // Fire event for other systems
                OnModuleInstalled?.Invoke(this, module);

                // Play install sound
                AudioManager.Instance.PlaySound("module_install");
            }
            else
            {
                ShowError(result.FailureReason);
                AudioManager.Instance.PlaySound("error_buzz");
            }
        }

        private void TryAssignCrew(CrewCard crew)
        {
            if (installedModule == null)
            {
                ShowError("Install a module first before assigning crew");
                return;
            }

            if (!validator.ValidateCrewAssignment(installedModule, crew, slotDefinition))
            {
                float crewWeight = crew.MaxSailors * 0.1f * (1.0f + crew.Level / 100.0f);
                float totalWeight = installedModule.WeightTons + crewWeight;
                ShowError($"Crew too heavy! Total ({totalWeight:F1}t) exceeds capacity ({slotDefinition.weightCapacityTons:F1}t)");
                return;
            }

            assignedCrew = crew;
            RefreshDisplay();
            OnCrewAssigned?.Invoke(this, crew);
            AudioManager.Instance.PlaySound("crew_assign");
        }

        public void UninstallModule()
        {
            var oldModule = installedModule;
            installedModule = null;
            assignedCrew = null;
            RefreshDisplay();
            OnModuleUninstalled?.Invoke(this, oldModule);
        }

        public void UnassignCrew()
        {
            var oldCrew = assignedCrew;
            assignedCrew = null;
            RefreshDisplay();
            OnCrewUnassigned?.Invoke(this, oldCrew);
        }

        private float CalculateEfficiency()
        {
            if (installedModule == null || assignedCrew == null)
                return 0f;

            return ModuleEfficiencyCalculator.CalculateEfficiency(
                assignedCrew,
                installedModule.primaryStat
            );
        }

        private void SetVisualState(SlotVisualState state)
        {
            currentVisualState = state;

            slotBackground.color = state switch
            {
                SlotVisualState.Empty => emptyColor,
                SlotVisualState.ValidHover => validHoverColor,
                SlotVisualState.InvalidHover => invalidHoverColor,
                SlotVisualState.Manned => installedColor,
                SlotVisualState.Unmanned => unmannedColor,
                _ => emptyColor
            };
        }

        // Events
        public event Action<EquipmentSlotUI, ModuleDefinitionSO> OnModuleInstalled;
        public event Action<EquipmentSlotUI, ModuleDefinitionSO> OnModuleUninstalled;
        public event Action<EquipmentSlotUI, CrewCard> OnCrewAssigned;
        public event Action<EquipmentSlotUI, CrewCard> OnCrewUnassigned;

        // Tooltip helpers (implement based on your tooltip system)
        private void ShowTooltip(string message) { /* ... */ }
        private void HideTooltip() { /* ... */ }
        private void ShowError(string message) { /* ... */ }
    }

    public enum SlotVisualState
    {
        Empty,
        ValidHover,
        InvalidHover,
        Manned,
        Unmanned
    }
}
```

---

## 2.5 Firing Arc Visualization (Weapons Only)

```csharp
// Assets/Scripts/UI/ShipFitting/FiringArcVisualizer.cs
namespace WOS.UI.ShipFitting
{
    public class FiringArcVisualizer : MonoBehaviour
    {
        [Header("Arc Visualization")]
        [SerializeField] private LineRenderer arcLine;
        [SerializeField] private Color arcColor = new Color(1f, 1f, 0f, 0.5f);
        [SerializeField] private int arcSegments = 32;

        private EquipmentSlotDefinition currentSlot;

        public void ShowArc(EquipmentSlotDefinition slot)
        {
            if (!slot.hasFiringArc)
            {
                HideArc();
                return;
            }

            currentSlot = slot;
            arcLine.enabled = true;
            DrawArc(slot.arcMinDegrees, slot.arcMaxDegrees);
        }

        public void HideArc()
        {
            arcLine.enabled = false;
            currentSlot = null;
        }

        private void DrawArc(float minDegrees, float maxDegrees)
        {
            float arcSpan = maxDegrees - minDegrees;
            arcLine.positionCount = arcSegments + 1;

            for (int i = 0; i <= arcSegments; i++)
            {
                float t = (float)i / arcSegments;
                float angle = Mathf.Lerp(minDegrees, maxDegrees, t);
                float radians = angle * Mathf.Deg2Rad;

                // Assuming top-down view with 0° = forward
                Vector3 point = new Vector3(
                    Mathf.Sin(radians),
                    0,
                    Mathf.Cos(radians)
                ) * 100f; // Scale for visibility

                arcLine.SetPosition(i, point);
            }
        }
    }
}
```

---

## Phase 2 Validation Checklist

```
Slot-Matching Validator
[ ] Category validation checked FIRST
[ ] Dimension validation requires EXACT match
[ ] No rotation support (this is NOT Tetris)
[ ] Module weight validation correct
[ ] Crew weight validation uses GDD formula
[ ] Complete validation returns detailed result

Equipment Slot UI
[ ] Slot displays category, dimension, capacity
[ ] Category-based outline colors per GDD
[ ] Drag-over shows green for valid, red for invalid
[ ] Tooltip shows failure reason when invalid
[ ] Module installation respects port restrictions
[ ] Crew assignment validates weight
[ ] Unmanned state shows orange indicator
[ ] Efficiency percentage displayed when crewed

Module Definition
[ ] SlotCategory field added
[ ] GridSize field added
[ ] WeightTons field added
[ ] PrimaryStat field added for crew efficiency
[ ] All existing modules updated with new fields

Integration
[ ] Firing arc visualization for weapon slots
[ ] Sound effects for install/error
[ ] Events fire correctly for tracking
[ ] Undo system integration (Phase 6)
```

---

*Phase 2: Slot-Matching Equipment System - Version 3.0*
