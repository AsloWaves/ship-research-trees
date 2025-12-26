# Phase 4: UI Framework (5 Ship Fitting Screens)

**Goal**: Implement 5 GDD-compliant Ship Fitting UI screens with full interaction specifications

---

## 4.1 Five Primary Screens (GDD Specification)

```
SHIP FITTING UI ARCHITECTURE
============================

┌─────────────────────────────────────────────────────────────────────────────┐
│ [1. Weapons] [2. Systems] [3. Armor] [4. Cargo] [5. Loadouts]   [X]        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                                                                             │
│                         SCREEN-SPECIFIC CONTENT                             │
│                            (70-80% of area)                                 │
│                                                                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Weight: 45,230/50,000t (90.5%)  ████████████░░  Speed: -5%  Crew: 1,234    │
│ Firepower: 856  Protection: 721  Detection: 12km  [Undo] [Redo] [Apply]    │
└─────────────────────────────────────────────────────────────────────────────┘

Navigation:
- Tab bar at top: Click to switch, keyboard 1-5
- Ctrl+Tab: Cycle through screens
- Common bottom panel on ALL screens
```

---

## 4.2 Screen 1: Weapon Hardpoint View

### Layout

```
WEAPON HARDPOINT VIEW
=====================

┌─────────────────────────────────────────────────────────────────────────────┐
│ LEFT PANEL (70%)                    │ RIGHT PANEL (30%)                     │
│ Ship Top-Down Sprite                │ Turret/Weapon Inventory               │
│                                     │                                       │
│        ┌──┐                        │ [Filter: All▾] [Sort: Caliber▾]       │
│        │MA│ (Main Battery A)       │                                       │
│    ┌──┐│  │┌──┐                    │ ┌────────────────────────────┐       │
│    │MB││  ││MC│                    │ │ 16"/50 Mark 7             │       │
│    └──┘│  │└──┘                    │ │ [3×4] 1,500t Main Battery │       │
│        └──┘                        │ │ ⚔ 14,400 DPM  ◎ 38km     │       │
│   ○ ○      ○ ○  (Secondary)        │ └────────────────────────────┘       │
│  ○○○○○    ○○○○○ (AA)               │ ┌────────────────────────────┐       │
│                                     │ │ 5"/38 Mark 12 Twin        │       │
│   Click hardpoint to select        │ │ [1×2] 65t Secondary       │       │
│   Drag turret from inventory       │ │ ⚔ 2,100 DPM  ◎ 15km      │       │
│                                     │ └────────────────────────────┘       │
│ [Arc Overlay: ON/OFF]              │                                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Hardpoint Visual Indicators (per GDD)

```csharp
// Hardpoint outline colors
MainBattery:     Color.red          // Large circles
SecondaryBattery: new Color(1,0.5f,0) // Medium circles, orange
Tertiary/AA:     Color.yellow       // Small circles
Torpedo:         Color.blue         // Unique icon
Special:         Color.magenta      // Unique icon

// Hardpoint states
Empty:           Gray fill, dashed outline
Occupied:        Colored fill, solid outline
Selected:        Glowing pulse effect
Hover:           Brightened, scale 1.1x
InvalidHover:    Red tint, X overlay
```

### Implementation

```csharp
// Assets/Scripts/UI/ShipFitting/Screens/WeaponHardpointScreen.cs
namespace WOS.UI.ShipFitting.Screens
{
    public class WeaponHardpointScreen : BaseShipFittingScreen
    {
        [Header("Ship Display")]
        [SerializeField] private Image shipSprite;
        [SerializeField] private RectTransform hardpointContainer;
        [SerializeField] private GameObject hardpointIndicatorPrefab;

        [Header("Inventory Panel")]
        [SerializeField] private Transform turretListContainer;
        [SerializeField] private TMP_Dropdown filterDropdown;
        [SerializeField] private TMP_Dropdown sortDropdown;
        [SerializeField] private TMP_InputField searchField;

        [Header("Arc Visualization")]
        [SerializeField] private Toggle arcOverlayToggle;
        [SerializeField] private FiringArcVisualizer arcVisualizer;

        private List<HardpointIndicator> hardpointIndicators = new List<HardpointIndicator>();
        private HardpointIndicator selectedHardpoint;

        public override void Initialize(ShipConfigurationSO shipConfig)
        {
            base.Initialize(shipConfig);

            // Load ship sprite (top-down view)
            shipSprite.sprite = shipConfig.shipSprite;

            // Create hardpoint indicators for weapon slots
            CreateHardpointIndicators(shipConfig.equipmentSlots
                .Where(s => IsWeaponCategory(s.category)));

            // Populate turret inventory
            RefreshTurretList();
        }

        private void CreateHardpointIndicators(IEnumerable<EquipmentSlotDefinition> weaponSlots)
        {
            foreach (var slot in weaponSlots)
            {
                var indicator = Instantiate(hardpointIndicatorPrefab, hardpointContainer);
                var hardpoint = indicator.GetComponent<HardpointIndicator>();
                hardpoint.Initialize(slot);
                hardpoint.OnClicked += HandleHardpointClicked;
                hardpoint.OnModuleDropped += HandleModuleDropped;
                hardpointIndicators.Add(hardpoint);
            }
        }

        private void HandleHardpointClicked(HardpointIndicator hardpoint)
        {
            // Deselect previous
            selectedHardpoint?.SetSelected(false);

            // Select new
            selectedHardpoint = hardpoint;
            selectedHardpoint.SetSelected(true);

            // Show firing arc if applicable
            if (arcOverlayToggle.isOn && hardpoint.SlotDefinition.hasFiringArc)
            {
                arcVisualizer.ShowArc(hardpoint.SlotDefinition);
            }

            // Update inventory to highlight compatible turrets
            RefreshTurretList(hardpoint.SlotDefinition);
        }

        private void HandleModuleDropped(HardpointIndicator hardpoint, ModuleDefinitionSO module)
        {
            var slotUI = hardpoint.GetComponent<EquipmentSlotUI>();
            slotUI.TryInstallModule(module);
        }

        private void RefreshTurretList(EquipmentSlotDefinition filterSlot = null)
        {
            // Get player's turret inventory
            var turrets = InventoryManager.Instance.GetTurretsInInventory();

            // Apply filters
            var filter = (TurretFilter)filterDropdown.value;
            var sort = (TurretSort)sortDropdown.value;
            var search = searchField.text;

            turrets = ApplyFilters(turrets, filter, sort, search);

            // Mark compatible turrets if slot selected
            foreach (var turretUI in turretListContainer.GetComponentsInChildren<TurretListItem>())
            {
                if (filterSlot != null)
                {
                    var validator = new SlotMatchingValidator();
                    var result = validator.ValidateInstallation(turretUI.Module, filterSlot);
                    turretUI.SetCompatibility(result.IsValid, result.FailureReason);
                }
                else
                {
                    turretUI.SetCompatibility(true, null);
                }
            }
        }

        private bool IsWeaponCategory(EquipmentSlotCategory category)
        {
            return category is EquipmentSlotCategory.MainBattery or
                              EquipmentSlotCategory.SecondaryBattery or
                              EquipmentSlotCategory.TertiaryBattery or
                              EquipmentSlotCategory.AAHeavy or
                              EquipmentSlotCategory.AALight or
                              EquipmentSlotCategory.TorpedoTubes;
        }
    }
}
```

---

## 4.3 Screen 2: Ship Systems Fitting

### Layout

```
SHIP SYSTEMS FITTING
====================

┌─────────────────────────────────────────────────────────────────────────────┐
│ CENTER PANEL (60%)                                  │ RIGHT PANEL (40%)     │
│ Grid-Based Slot Layout                              │                       │
│                                                     │ [Engines][Support]    │
│ ┌───────────────────────────┐                      │ [Misc][All]           │
│ │ ENGINE SECTION (Orange)   │                      │                       │
│ │ ┌────┐ ┌────┐ ┌────┐     │                      │ Module Inventory      │
│ │ │Eng1│ │Eng2│ │Eng3│     │                      │ ┌────────────────┐    │
│ │ └────┘ └────┘ └────┘     │                      │ │ Steam Turbine  │    │
│ └───────────────────────────┘                      │ │ [2×3] 450t     │    │
│                                                     │ │ 35,000 SHP     │    │
│ ┌───────────────────────────┐                      │ └────────────────┘    │
│ │ SUPPORT SECTION (Blue)    │                      │                       │
│ │ ┌──┐ ┌──┐ ┌──┐ ┌──┐      │                      │ ────────────────────  │
│ │ │S1│ │S2│ │S3│ │S4│      │                      │ CREW PANEL            │
│ │ └──┘ └──┘ └──┘ └──┘      │                      │                       │
│ └───────────────────────────┘                      │ Available Crew:       │
│                                                     │ ┌──────────────────┐ │
│ ┌───────────────────────────┐                      │ │ Chief Engineer   │ │
│ │ MISC SECTION (Purple)     │                      │ │ Lvl 45, Eng: 38  │ │
│ │ ┌──┐ ┌──┐                 │                      │ │ Weight: 12.5t    │ │
│ │ │M1│ │M2│                 │                      │ └──────────────────┘ │
│ │ └──┘ └──┘                 │                      │                       │
│ └───────────────────────────┘                      │                       │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Power Budget System

```csharp
// Ship Systems tracks power generation and consumption
public class PowerBudgetManager
{
    public float PowerGenerated { get; private set; }  // From engines
    public float PowerConsumed { get; private set; }   // By support modules
    public float PowerBalance => PowerGenerated - PowerConsumed;
    public bool IsOverloaded => PowerBalance < 0;

    // Visual feedback in UI:
    // Green bar: Power generated
    // Blue bar overlay: Power consumed
    // Red warning: If consumed > generated (overload)
}
```

### Implementation

```csharp
// Assets/Scripts/UI/ShipFitting/Screens/ShipSystemsScreen.cs
namespace WOS.UI.ShipFitting.Screens
{
    public class ShipSystemsScreen : BaseShipFittingScreen
    {
        [Header("Section Panels")]
        [SerializeField] private RectTransform engineSection;
        [SerializeField] private RectTransform supportSection;
        [SerializeField] private RectTransform miscSection;

        [Header("Section Colors")]
        [SerializeField] private Color engineColor = new Color(1f, 0.5f, 0f);
        [SerializeField] private Color supportColor = Color.cyan;
        [SerializeField] private Color miscColor = new Color(0.5f, 0f, 0.5f);

        [Header("Power Display")]
        [SerializeField] private Slider powerGeneratedBar;
        [SerializeField] private Slider powerConsumedBar;
        [SerializeField] private TextMeshProUGUI powerBalanceText;
        [SerializeField] private GameObject overloadWarning;

        [Header("Module Tabs")]
        [SerializeField] private Toggle enginesTab;
        [SerializeField] private Toggle supportTab;
        [SerializeField] private Toggle miscTab;
        [SerializeField] private Toggle allTab;

        [Header("Crew Panel")]
        [SerializeField] private CrewAssignmentPanel crewPanel;

        public override void Initialize(ShipConfigurationSO shipConfig)
        {
            base.Initialize(shipConfig);

            // Create slot UIs for each section
            CreateSectionSlots(engineSection, shipConfig.equipmentSlots
                .Where(s => s.category == EquipmentSlotCategory.EngineRoom));

            CreateSectionSlots(supportSection, shipConfig.equipmentSlots
                .Where(s => s.category == EquipmentSlotCategory.Support));

            CreateSectionSlots(miscSection, shipConfig.equipmentSlots
                .Where(s => s.category == EquipmentSlotCategory.Misc));

            // Setup tab switching
            enginesTab.onValueChanged.AddListener(v => { if (v) FilterModules(EquipmentSlotCategory.EngineRoom); });
            supportTab.onValueChanged.AddListener(v => { if (v) FilterModules(EquipmentSlotCategory.Support); });
            miscTab.onValueChanged.AddListener(v => { if (v) FilterModules(EquipmentSlotCategory.Misc); });
            allTab.onValueChanged.AddListener(v => { if (v) FilterModules(null); });
        }

        private void UpdatePowerDisplay()
        {
            var budget = GetPowerBudget();

            powerGeneratedBar.value = budget.PowerGenerated / budget.MaxPower;
            powerConsumedBar.value = budget.PowerConsumed / budget.MaxPower;
            powerBalanceText.text = $"{budget.PowerBalance:+#;-#;0} MW";

            overloadWarning.SetActive(budget.IsOverloaded);
        }
    }
}
```

---

## 4.4 Screen 3: Armor Configuration

### Layout

```
ARMOR CONFIGURATION
===================

┌─────────────────────────────────────────────────────────────────────────────┐
│ LEFT PANEL (60%)                        │ RIGHT PANEL (40%)                 │
│ Ship Schematics                         │ Armor Zone Controls               │
│                                         │                                   │
│ ┌─────────────────────────────────────┐│ BELT ARMOR                        │
│ │ SIDE PROFILE VIEW                   ││ Material: [RHA        ▾]          │
│ │                                     ││ Thickness: [12.5"] = 318mm        │
│ │  ═══════════════════════════════   ││ Weight: 2,450 tons                │
│ │   Belt  │ Citadel │  Belt          ││                                   │
│ │  ═══════════════════════════════   ││ DECK ARMOR                        │
│ │                                     ││ Material: [STS        ▾]          │
│ │ (Click zone to select)              ││ Thickness: [5.0"] = 127mm         │
│ └─────────────────────────────────────┘│ Weight: 980 tons                  │
│                                         │                                   │
│ ┌─────────────────────────────────────┐│ TURRET FACE                       │
│ │ TOP-DOWN VIEW                       ││ Material: [Face-Hard ▾]           │
│ │                                     ││ Thickness: [18.0"] = 457mm        │
│ │      ┌─────┐                        ││ Weight: 450 tons (per turret)     │
│ │      │Turret│                       ││                                   │
│ │ ═════│     │═════                   ││ ... (9 zones total)               │
│ │      └─────┘                        ││                                   │
│ │                                     ││ ─────────────────────────────     │
│ │ (Highlighted zone shows selection)  ││ TOTAL ARMOR: 8,750 tons           │
│ └─────────────────────────────────────┘│ Protection Rating: 721            │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 9 Armor Zones

```csharp
public enum ArmorZone
{
    Belt,           // Main side armor
    Deck,           // Horizontal protection
    Bulkhead,       // Internal compartment dividers
    TurretFace,     // Front of turrets
    TurretRoof,     // Top of turrets
    TurretSides,    // Sides of turrets
    Barbette,       // Turret support structure
    ConningTower,   // Command structure
    Citadel         // Central protected zone
}
```

### Implementation

```csharp
// Assets/Scripts/UI/ShipFitting/Screens/ArmorConfigScreen.cs
namespace WOS.UI.ShipFitting.Screens
{
    public class ArmorConfigScreen : BaseShipFittingScreen
    {
        [Header("Ship Views")]
        [SerializeField] private Image sideProfileImage;
        [SerializeField] private Image topDownImage;
        [SerializeField] private ArmorZoneHighlight[] zoneHighlights;

        [Header("Zone Control Panels")]
        [SerializeField] private Transform zoneControlContainer;
        [SerializeField] private GameObject zoneControlPrefab;

        [Header("Armor Materials")]
        [SerializeField] private ArmorMaterialDatabase materialDatabase;

        private ArmorZone selectedZone;
        private Dictionary<ArmorZone, ArmorZoneControl> zoneControls = new Dictionary<ArmorZone, ArmorZoneControl>();

        public override void Initialize(ShipConfigurationSO shipConfig)
        {
            base.Initialize(shipConfig);

            // Load ship profile images
            sideProfileImage.sprite = shipConfig.shipSideProfile;
            topDownImage.sprite = shipConfig.shipSprite;

            // Create control panel for each zone
            foreach (ArmorZone zone in Enum.GetValues(typeof(ArmorZone)))
            {
                var control = Instantiate(zoneControlPrefab, zoneControlContainer);
                var zoneControl = control.GetComponent<ArmorZoneControl>();
                zoneControl.Initialize(zone, shipConfig.defaultArmor.GetZone(zone), materialDatabase);
                zoneControl.OnThicknessChanged += HandleThicknessChanged;
                zoneControl.OnMaterialChanged += HandleMaterialChanged;
                zoneControls[zone] = zoneControl;
            }

            // Setup zone click handlers on ship images
            foreach (var highlight in zoneHighlights)
            {
                highlight.OnClicked += HandleZoneClicked;
            }
        }

        private void HandleZoneClicked(ArmorZone zone)
        {
            selectedZone = zone;

            // Highlight selected zone on both views
            foreach (var highlight in zoneHighlights)
            {
                highlight.SetSelected(highlight.Zone == zone);
            }

            // Scroll control panel to selected zone
            ScrollToZoneControl(zone);
        }

        private void HandleThicknessChanged(ArmorZone zone, float thicknessInches)
        {
            // GDD: Thickness in 0.1" increments
            float roundedThickness = Mathf.Round(thicknessInches * 10f) / 10f;

            // Calculate new weight
            float newWeight = CalculateArmorWeight(zone, roundedThickness);

            // Check if within ship's armor weight budget
            float totalArmorWeight = CalculateTotalArmorWeight();
            if (totalArmorWeight > currentShip.maxArmorWeightTons)
            {
                ShowWarning($"Total armor weight ({totalArmorWeight:N0}t) exceeds maximum ({currentShip.maxArmorWeightTons:N0}t)");
            }

            // Update display
            zoneControls[zone].UpdateWeight(newWeight);
            UpdateTotalArmorDisplay();
        }

        private void HandleMaterialChanged(ArmorZone zone, ArmorMaterial material)
        {
            // Different materials have different protection multipliers
            zoneControls[zone].UpdateProtectionRating(CalculateZoneProtection(zone, material));
            UpdateTotalArmorDisplay();
        }

        private void UpdateTotalArmorDisplay()
        {
            float totalWeight = CalculateTotalArmorWeight();
            int protectionRating = CalculateTotalProtectionRating();

            totalArmorWeightText.text = $"TOTAL ARMOR: {totalWeight:N0} tons";
            protectionRatingText.text = $"Protection Rating: {protectionRating}";
        }
    }
}
```

---

## 4.5 Screen 4: Cargo Grid Inventory

### Layout

```
CARGO GRID INVENTORY
====================

┌─────────────────────────────────────────────────────────────────────────────┐
│ LEFT PANEL (70%)                        │ RIGHT PANEL (30%)                 │
│ Tetris Cargo Grid                       │ Item Inventory                    │
│                                         │                                   │
│ ┌─────────────────────────────────────┐│ [Filter▾] [Sort▾] [🔍______]      │
│ │ ████│░░░░░░│████████│              ││                                   │
│ │ ████│Magazine░░░░░░░│              ││ ┌────────────────────────┐        │
│ │ ████│░░░░░░░░░░░░░░░│ General     ││ │ 16" AP Shells (x100)  │        │
│ │     │░░░░░░░░░░░░░░░│ Cargo       ││ │ [2×3] 5.2t per crate  │        │
│ │     │───────────────│              ││ │ Magazine only         │        │
│ │     │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ Fuel        ││ └────────────────────────┘        │
│ │     │▓▓Fuel▓▓▓▓▓▓▓▓▓│ Bunker      ││                                   │
│ │     │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│              ││ ┌────────────────────────┐        │
│ └─────────────────────────────────────┘│ │ Heavy Fuel Oil        │        │
│                                         │ │ [1×1] 0.9t per unit   │        │
│ [R] Rotate  [Auto-Arrange]             │ │ Fuel Bunker only      │        │
│                                         │ └────────────────────────┘        │
├─────────────────────────────────────────────────────────────────────────────┤
│ Grid: 89/120 cells  Weight: 4,523/5,000t (90.5%)  ████████████░░░░ NEAR CAP │
│ Space: 31 cells free  Weight: 477t remaining     [Transfer All→] [←All]    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Weight Display Colors (per GDD)

```csharp
// Weight bar color bands
0-80%:   Color.green     // Optimal
80-95%:  Color.yellow    // Near limit
95-100%: Color.orange    // At limit
100%:    Color.red       // HARD CAP - cannot add more
```

### Implementation

```csharp
// Assets/Scripts/UI/ShipFitting/Screens/CargoGridScreen.cs
namespace WOS.UI.ShipFitting.Screens
{
    public class CargoGridScreen : BaseShipFittingScreen
    {
        [Header("Grid Display")]
        [SerializeField] private CargoGridUI gridUI;
        [SerializeField] private RectTransform partitionOverlay;

        [Header("Inventory List")]
        [SerializeField] private Transform itemListContainer;
        [SerializeField] private TMP_Dropdown filterDropdown;
        [SerializeField] private TMP_Dropdown sortDropdown;
        [SerializeField] private TMP_InputField searchField;

        [Header("Weight Display")]
        [SerializeField] private Slider weightBar;
        [SerializeField] private TextMeshProUGUI weightText;
        [SerializeField] private TextMeshProUGUI cellCountText;
        [SerializeField] private TextMeshProUGUI remainingText;
        [SerializeField] private Image weightBarFill;

        [Header("Weight Colors (per GDD)")]
        [SerializeField] private Color optimalColor = Color.green;
        [SerializeField] private Color nearLimitColor = Color.yellow;
        [SerializeField] private Color atLimitColor = new Color(1f, 0.5f, 0f);
        [SerializeField] private Color hardCapColor = Color.red;

        [Header("Transfer Buttons")]
        [SerializeField] private Button transferAllToPortButton;
        [SerializeField] private Button transferAllToShipButton;
        [SerializeField] private Button autoArrangeButton;

        [Header("Input")]
        [SerializeField] private KeyCode rotateKey = KeyCode.R;

        private ShipCargoGrid cargoGrid;
        private CargoItem previewItem;

        public override void Initialize(ShipConfigurationSO shipConfig)
        {
            base.Initialize(shipConfig);

            cargoGrid = GetComponent<ShipCargoGrid>();
            cargoGrid.Initialize(shipConfig);

            // Setup grid UI
            gridUI.Initialize(cargoGrid);
            gridUI.OnCellHovered += HandleCellHovered;
            gridUI.OnCellClicked += HandleCellClicked;

            // Show partition zones
            DrawPartitionOverlay(shipConfig.cargoPartitions);

            // Subscribe to weight changes
            cargoGrid.OnWeightChanged += UpdateWeightDisplay;

            // Setup transfer buttons
            transferAllToPortButton.onClick.AddListener(HandleTransferAllToPort);
            transferAllToShipButton.onClick.AddListener(HandleTransferAllToShip);
            autoArrangeButton.onClick.AddListener(HandleAutoArrange);
        }

        private void Update()
        {
            // R key to rotate during drag
            if (Input.GetKeyDown(rotateKey) && previewItem != null)
            {
                previewItem.Rotate();
                UpdatePreviewDisplay();
                AudioManager.Instance.PlaySound("rotate_item");
            }
        }

        private void UpdateWeightDisplay(float current, float max)
        {
            float percentage = (current / max) * 100f;

            weightBar.value = current / max;
            weightText.text = $"Weight: {current:N0}/{max:N0}t ({percentage:F1}%)";
            cellCountText.text = $"Grid: {cargoGrid.UsedCells}/{cargoGrid.TotalCells} cells";
            remainingText.text = $"Weight: {max - current:N0}t remaining";

            // Update color based on weight band
            weightBarFill.color = cargoGrid.CurrentWeightBand switch
            {
                WeightBand.Optimal => optimalColor,
                WeightBand.NearLimit => nearLimitColor,
                WeightBand.AtLimit => atLimitColor,
                WeightBand.HardCap => hardCapColor,
                _ => optimalColor
            };

            // Show/hide hard cap warning
            if (cargoGrid.IsAtHardCap)
            {
                ShowHardCapWarning();
            }
            else
            {
                HideHardCapWarning();
            }
        }

        private void HandleCellHovered(Vector2Int cell)
        {
            if (previewItem == null) return;

            var result = cargoGrid.GetPlacementResult(previewItem, cell);
            gridUI.ShowPreview(previewItem, cell, result == PlacementResult.Valid);

            // Show tooltip with failure reason if invalid
            if (result != PlacementResult.Valid)
            {
                ShowTooltip(GetPlacementErrorMessage(result));
            }
        }

        private string GetPlacementErrorMessage(PlacementResult result)
        {
            return result switch
            {
                PlacementResult.OutOfBounds => "Outside cargo hold",
                PlacementResult.Collision => "Space occupied",
                PlacementResult.WrongPartition => "Wrong cargo section",
                PlacementResult.ExceedsWeightCap => "Would exceed weight limit!",
                _ => ""
            };
        }

        private void HandleAutoArrange()
        {
            if (cargoGrid.TryAutoArrange())
            {
                gridUI.RefreshDisplay();
                AudioManager.Instance.PlaySound("auto_arrange_success");
            }
            else
            {
                ShowWarning("Could not auto-arrange - some items may not fit");
                AudioManager.Instance.PlaySound("error_buzz");
            }
        }
    }
}
```

---

## 4.6 Screen 5: Loadout Presets

### Layout

```
LOADOUT PRESETS
===============

┌─────────────────────────────────────────────────────────────────────────────┐
│ CENTER PANEL (80%)                              │ DETAILS PANEL (20%)       │
│ Preset Cards Grid                               │                           │
│                                                 │ SELECTED PRESET           │
│ ┌──────────────────┐ ┌──────────────────┐      │ ─────────────────         │
│ │ ★ Combat Ready   │ │ Long Range Patrol│      │ "Combat Ready"            │
│ │ All weapons max  │ │ Extra fuel       │      │                           │
│ │ Full crew        │ │ Minimal weapons  │      │ Created: 2024-03-15       │
│ │                  │ │                  │      │ Modified: 2024-06-20      │
│ │ [Apply] [Edit]   │ │ [Apply] [Edit]   │      │                           │
│ └──────────────────┘ └──────────────────┘      │ Weapons: 12/12            │
│                                                 │ Systems: 8/8              │
│ ┌──────────────────┐ ┌──────────────────┐      │ Crew: 1,234               │
│ │ Trade Route      │ │ + New Preset     │      │ Weight: 48,500t           │
│ │ Max cargo space  │ │                  │      │                           │
│ │ Basic defense    │ │ Create new       │      │ [Preview]                 │
│ │                  │ │ loadout preset   │      │ [Apply]                   │
│ │ [Apply] [Edit]   │ │                  │      │ [Share]                   │
│ └──────────────────┘ └──────────────────┘      │ [Delete]                  │
│                                                 │                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Implementation

```csharp
// Assets/Scripts/UI/ShipFitting/Screens/LoadoutPresetsScreen.cs
namespace WOS.UI.ShipFitting.Screens
{
    public class LoadoutPresetsScreen : BaseShipFittingScreen
    {
        [Header("Preset Grid")]
        [SerializeField] private Transform presetGridContainer;
        [SerializeField] private GameObject presetCardPrefab;
        [SerializeField] private GameObject newPresetCardPrefab;

        [Header("Details Panel")]
        [SerializeField] private GameObject detailsPanel;
        [SerializeField] private TextMeshProUGUI presetNameText;
        [SerializeField] private TextMeshProUGUI createdDateText;
        [SerializeField] private TextMeshProUGUI modifiedDateText;
        [SerializeField] private TextMeshProUGUI weaponSummaryText;
        [SerializeField] private TextMeshProUGUI systemSummaryText;
        [SerializeField] private TextMeshProUGUI crewSummaryText;
        [SerializeField] private TextMeshProUGUI weightSummaryText;

        [Header("Action Buttons")]
        [SerializeField] private Button previewButton;
        [SerializeField] private Button applyButton;
        [SerializeField] private Button shareButton;
        [SerializeField] private Button deleteButton;

        private ShipLoadoutPreset selectedPreset;
        private List<PresetCard> presetCards = new List<PresetCard>();

        public override void Initialize(ShipConfigurationSO shipConfig)
        {
            base.Initialize(shipConfig);

            // Load presets for this ship
            var presets = LoadoutManager.Instance.GetPresetsForShip(shipConfig.shipId);
            CreatePresetCards(presets);

            // Setup action buttons
            previewButton.onClick.AddListener(HandlePreview);
            applyButton.onClick.AddListener(HandleApply);
            shareButton.onClick.AddListener(HandleShare);
            deleteButton.onClick.AddListener(HandleDelete);
        }

        private void CreatePresetCards(List<ShipLoadoutPreset> presets)
        {
            // Clear existing
            foreach (Transform child in presetGridContainer)
            {
                Destroy(child.gameObject);
            }
            presetCards.Clear();

            // Create preset cards
            foreach (var preset in presets)
            {
                var card = Instantiate(presetCardPrefab, presetGridContainer);
                var presetCard = card.GetComponent<PresetCard>();
                presetCard.Initialize(preset);
                presetCard.OnClicked += HandlePresetClicked;
                presetCard.OnApplyClicked += HandleApplyClicked;
                presetCard.OnEditClicked += HandleEditClicked;
                presetCards.Add(presetCard);
            }

            // Add "New Preset" card
            Instantiate(newPresetCardPrefab, presetGridContainer);
        }

        private void HandlePresetClicked(ShipLoadoutPreset preset)
        {
            selectedPreset = preset;
            UpdateDetailsPanel();
        }

        private void UpdateDetailsPanel()
        {
            if (selectedPreset == null)
            {
                detailsPanel.SetActive(false);
                return;
            }

            detailsPanel.SetActive(true);
            presetNameText.text = $"\"{selectedPreset.PresetName}\"";
            createdDateText.text = $"Created: {selectedPreset.CreatedAt:yyyy-MM-dd}";
            modifiedDateText.text = $"Modified: {selectedPreset.ModifiedAt:yyyy-MM-dd}";

            // Calculate summary stats
            int weaponCount = selectedPreset.SlotAssignments.Count(a => IsWeaponSlot(a.SlotCategory));
            int systemCount = selectedPreset.SlotAssignments.Count(a => !IsWeaponSlot(a.SlotCategory));
            int crewCount = selectedPreset.CrewAssignments.Sum(c => c.SailorCount);
            float totalWeight = CalculatePresetWeight(selectedPreset);

            weaponSummaryText.text = $"Weapons: {weaponCount}";
            systemSummaryText.text = $"Systems: {systemCount}";
            crewSummaryText.text = $"Crew: {crewCount:N0}";
            weightSummaryText.text = $"Weight: {totalWeight:N0}t";
        }

        private void HandleApply()
        {
            if (selectedPreset == null) return;

            // Validate preset is still compatible
            var validation = ValidatePreset(selectedPreset);
            if (!validation.IsValid)
            {
                ShowValidationErrors(validation);
                return;
            }

            // Apply preset
            LoadoutManager.Instance.ApplyPreset(selectedPreset);
            AudioManager.Instance.PlaySound("loadout_applied");
            ShowMessage($"Loadout \"{selectedPreset.PresetName}\" applied!");
        }

        private void HandleShare()
        {
            if (selectedPreset == null) return;

            // Generate share code
            string shareCode = LoadoutManager.Instance.GenerateShareCode(selectedPreset);

            // Copy to clipboard
            GUIUtility.systemCopyBuffer = shareCode;
            ShowMessage("Share code copied to clipboard!");
        }

        private void HandleDelete()
        {
            if (selectedPreset == null) return;

            // Show confirmation dialog
            ShowConfirmDialog(
                $"Delete \"{selectedPreset.PresetName}\"?",
                "This action cannot be undone.",
                () => {
                    LoadoutManager.Instance.DeletePreset(selectedPreset.PresetId);
                    RefreshPresetList();
                }
            );
        }
    }
}
```

---

## 4.7 Common Bottom Panel

```csharp
// Assets/Scripts/UI/ShipFitting/CommonStatsPanel.cs
namespace WOS.UI.ShipFitting
{
    /// <summary>
    /// Shared bottom panel across all 5 fitting screens
    /// Per GDD Ship-Fitting-UI.md lines 450-500
    /// </summary>
    public class CommonStatsPanel : MonoBehaviour
    {
        [Header("Weight Display")]
        [SerializeField] private TextMeshProUGUI weightText;
        [SerializeField] private Slider weightBar;
        [SerializeField] private TextMeshProUGUI speedImpactText;

        [Header("Stats Display")]
        [SerializeField] private TextMeshProUGUI firepowerText;
        [SerializeField] private TextMeshProUGUI protectionText;
        [SerializeField] private TextMeshProUGUI detectionText;
        [SerializeField] private TextMeshProUGUI crewText;

        [Header("Action Buttons")]
        [SerializeField] private Button undoButton;
        [SerializeField] private Button redoButton;
        [SerializeField] private Button applyButton;

        public void UpdateStats(ShipStats stats)
        {
            // Weight (GDD format: Current/Max with percentage)
            weightText.text = $"Weight: {stats.CurrentWeight:N0}/{stats.MaxWeight:N0}t ({stats.WeightPercentage:F1}%)";
            weightBar.value = stats.WeightPercentage / 100f;

            // Speed impact (only shown if overweight affects speed)
            // Note: In this GDD, weight is HARD CAP, so speed impact may not apply
            speedImpactText.text = stats.SpeedModifier < 0 ? $"Speed: {stats.SpeedModifier:+0;-0}%" : "";

            // Other stats
            firepowerText.text = $"Firepower: {stats.FirepowerRating:N0}";
            protectionText.text = $"Protection: {stats.ProtectionRating:N0}";
            detectionText.text = $"Detection: {stats.DetectionRange:F1}km";
            crewText.text = $"Crew: {stats.CurrentCrew:N0}";
        }

        public void SetUndoRedoState(bool canUndo, bool canRedo)
        {
            undoButton.interactable = canUndo;
            redoButton.interactable = canRedo;
        }
    }
}
```

---

## 4.8 Tooltip System (0.5s delay per GDD)

```csharp
// Assets/Scripts/UI/Common/TooltipManager.cs
namespace WOS.UI.Common
{
    public class TooltipManager : MonoBehaviour
    {
        public static TooltipManager Instance { get; private set; }

        [Header("Configuration")]
        [SerializeField] private float hoverDelay = 0.5f;  // GDD-specified
        [SerializeField] private GameObject tooltipPanel;
        [SerializeField] private TextMeshProUGUI tooltipText;
        [SerializeField] private CanvasGroup tooltipCanvasGroup;

        private Coroutine showCoroutine;
        private bool isShowing;

        public void ShowTooltip(string content, Vector2 position)
        {
            if (showCoroutine != null)
            {
                StopCoroutine(showCoroutine);
            }
            showCoroutine = StartCoroutine(ShowTooltipDelayed(content, position));
        }

        public void HideTooltip()
        {
            if (showCoroutine != null)
            {
                StopCoroutine(showCoroutine);
                showCoroutine = null;
            }

            tooltipPanel.SetActive(false);
            isShowing = false;
        }

        private IEnumerator ShowTooltipDelayed(string content, Vector2 position)
        {
            yield return new WaitForSeconds(hoverDelay);

            tooltipText.text = content;
            tooltipPanel.transform.position = ClampToScreen(position);
            tooltipPanel.SetActive(true);
            isShowing = true;
        }

        private Vector2 ClampToScreen(Vector2 position)
        {
            // Ensure tooltip doesn't go off screen
            var rect = tooltipPanel.GetComponent<RectTransform>();
            // ... clamp logic
            return position;
        }
    }
}
```

---

## Phase 4 Validation Checklist

```
Navigation
[ ] Tab bar switching works
[ ] Keyboard 1-5 shortcuts work
[ ] Ctrl+Tab cycles screens
[ ] Common bottom panel on all screens

Screen 1: Weapon Hardpoints
[ ] Top-down ship view displays
[ ] Hardpoint indicators show correctly
[ ] Category-based outline colors (red/orange/yellow)
[ ] Click hardpoint to select
[ ] Drag turret to install
[ ] Firing arc visualization toggle
[ ] Inventory filters/sort work

Screen 2: Ship Systems
[ ] Engine/Support/Misc sections visible
[ ] Section coloring (orange/blue/purple)
[ ] Power budget display (if applicable)
[ ] Module tabs filter correctly
[ ] Crew assignment integration

Screen 3: Armor Configuration
[ ] Side profile and top-down views
[ ] 9 armor zones selectable
[ ] Material dropdown with all types
[ ] Thickness input in 0.1" increments
[ ] MM equivalent calculated
[ ] Weight impact shown
[ ] Total protection rating calculated

Screen 4: Cargo Grid
[ ] Tetris grid displays correctly
[ ] Partition zones visible
[ ] R key rotation works
[ ] Weight bar with color bands
[ ] HARD CAP 100% enforced visually
[ ] Transfer buttons functional
[ ] Auto-arrange button works

Screen 5: Loadout Presets
[ ] Preset cards grid displays
[ ] New preset creation works
[ ] Apply preset works
[ ] Preview shows differences
[ ] Share code generation works
[ ] Delete with confirmation

Common Elements
[ ] Tooltip 0.5s delay works
[ ] Undo/Redo buttons functional
[ ] Stats update in real-time
[ ] Unsaved changes warning
```

---

*Phase 4: UI Framework - Version 3.0*
