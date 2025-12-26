# Testing Requirements by Phase

**Purpose**: Define testing requirements for each implementation phase

---

## Testing Strategy Overview

### Testing Tiers (from CLAUDE.md)

| Tier | Description | Time | Use Case |
|------|-------------|------|----------|
| **Tier 1** | Editor Play Mode | 30 sec | UI, graphics, local scripts |
| **Tier 2** | Local Build | 5 min | Client validation |
| **Tier 3** | Docker | 20 min | NetworkBehaviour, server logic |
| **Tier 4** | PlayFab | 60 min | Full integration testing |

### Testing Principles

1. **Test Each Formula**: Every GDD formula must have dedicated unit tests
2. **Edge Case Coverage**: Test boundary conditions (0%, 100%, overflow)
3. **Integration Testing**: Verify systems work together
4. **Regression Testing**: All existing tests must pass after changes

---

## Pre-Phase: Foundation Testing

### Unit Tests

```csharp
// Tests/EditMode/ShipConfigurationSOTests.cs

[Test]
public void ShipConfigurationSO_HasRequiredFields()
{
    var config = ScriptableObject.CreateInstance<ShipConfigurationSO>();

    // Identity fields
    Assert.IsNotNull(config.shipId);
    Assert.IsNotNull(config.equipmentSlots);
    Assert.IsNotNull(config.armorConfig);
    Assert.GreaterOrEqual(config.tier, 1);
    Assert.LessOrEqual(config.tier, 10);
}

[Test]
public void EquipmentSlotDefinition_HasCategoryAndDimension()
{
    var slot = new EquipmentSlotDefinition
    {
        slotId = "test",
        category = EquipmentSlotCategory.MainBattery,
        requiredDimension = new Vector2Int(3, 4),
        weightCapacityTons = 100f
    };

    Assert.AreEqual(EquipmentSlotCategory.MainBattery, slot.category);
    Assert.AreEqual(new Vector2Int(3, 4), slot.requiredDimension);
    Assert.AreEqual(100f, slot.weightCapacityTons);
}
```

### Validation Checklist

```
[ ] ShipConfigurationSO creates without errors
[ ] All enum values defined
[ ] No namespace conflicts
[ ] Unity compiles without errors
[ ] No missing script warnings in Inspector
```

---

## Phase 1: Port Integration Testing

### Unit Tests

```csharp
// Tests/EditMode/PortIntegrationTests.cs

[Test]
public void PortTier_StorageSize_MatchesGDD()
{
    // GDD: T1-T3 = 500, T4-T7 = 750, T8-T10 = 1000
    Assert.AreEqual(500, GetStorageSize(PortTier.T1));
    Assert.AreEqual(500, GetStorageSize(PortTier.T2));
    Assert.AreEqual(500, GetStorageSize(PortTier.T3));
    Assert.AreEqual(750, GetStorageSize(PortTier.T4));
    Assert.AreEqual(750, GetStorageSize(PortTier.T7));
    Assert.AreEqual(1000, GetStorageSize(PortTier.T8));
    Assert.AreEqual(1000, GetStorageSize(PortTier.T10));
}

[Test]
public void UndockingValidator_BlocksOverweight()
{
    var validator = new UndockingValidator();
    var ship = CreateTestShip(maxWeight: 1000f);
    ship.currentWeight = 1100f; // 110%

    var result = validator.ValidateUndocking(ship);

    Assert.IsFalse(result.CanUndock);
    Assert.IsTrue(result.FailureReasons.Contains(UndockFailure.Overweight));
}

[Test]
public void UndockingValidator_BlocksInsufficientCrew()
{
    var validator = new UndockingValidator();
    var ship = CreateTestShip(minCrew: 100);
    ship.currentCrew = 50;

    var result = validator.ValidateUndocking(ship);

    Assert.IsFalse(result.CanUndock);
    Assert.IsTrue(result.FailureReasons.Contains(UndockFailure.InsufficientCrew));
}

[Test]
public void FittingRestriction_OnlyInPort()
{
    var manager = FittingRestrictionManager.Instance;

    // Not in safe zone
    manager.SetInSafeZone(false);
    Assert.IsFalse(manager.CanModifyFitting());

    // In safe zone
    manager.SetInSafeZone(true);
    Assert.IsTrue(manager.CanModifyFitting());
}
```

### Integration Tests

```csharp
// Tests/PlayMode/PortIntegrationPlayTests.cs

[UnityTest]
public IEnumerator Player_CanSpawnAtLastDockedPort()
{
    var spawnManager = new PlayerSpawnManager();
    var player = CreateTestPlayer();
    player.lastDockedPortId = "port_001";

    yield return spawnManager.SpawnPlayer(player, SpawnType.LastDocked);

    Assert.AreEqual("port_001", player.currentPortId);
}

[UnityTest]
public IEnumerator SafeZone_TriggerEnter_EnablesFitting()
{
    var player = SpawnTestPlayer();
    var safeZone = CreateSafeZone();

    // Move player into safe zone
    player.transform.position = safeZone.transform.position;
    yield return new WaitForSeconds(0.1f);

    Assert.IsTrue(FittingRestrictionManager.Instance.CanModifyFitting());
}
```

---

## Phase 2: Slot-Matching Testing

### Unit Tests

```csharp
// Tests/EditMode/SlotMatchingTests.cs

[Test]
public void SlotValidation_CategoryMustMatchFirst()
{
    var validator = new SlotMatchingValidator();
    var module = CreateModule(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4));
    var slot = CreateSlot(EquipmentSlotCategory.AAHeavy, new Vector2Int(3, 4));

    var result = validator.ValidateComplete(module, null, slot);

    Assert.IsFalse(result.IsValid);
    Assert.AreEqual(SlotValidationStep.Category, result.FailedAtStep);
}

[Test]
public void SlotValidation_DimensionMustMatchExactly()
{
    var validator = new SlotMatchingValidator();
    var module = CreateModule(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4));
    var slot = CreateSlot(EquipmentSlotCategory.MainBattery, new Vector2Int(4, 4)); // Wrong!

    var result = validator.ValidateComplete(module, null, slot);

    Assert.IsFalse(result.IsValid);
    Assert.AreEqual(SlotValidationStep.Dimension, result.FailedAtStep);
}

[Test]
public void SlotValidation_ModuleWeightMustFit()
{
    var validator = new SlotMatchingValidator();
    var module = CreateModule(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4));
    module.weightTons = 150f;
    var slot = CreateSlot(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4));
    slot.weightCapacityTons = 100f; // Module too heavy

    var result = validator.ValidateComplete(module, null, slot);

    Assert.IsFalse(result.IsValid);
    Assert.AreEqual(SlotValidationStep.ModuleWeight, result.FailedAtStep);
}

[Test]
public void SlotValidation_CrewWeightAddsToModuleWeight()
{
    var validator = new SlotMatchingValidator();
    var module = CreateModule(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4));
    module.weightTons = 80f;
    var crew = CreateCrew(level: 100); // 91 tons
    var slot = CreateSlot(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4));
    slot.weightCapacityTons = 150f; // 80 + 91 = 171 > 150

    var result = validator.ValidateComplete(module, crew, slot);

    Assert.IsFalse(result.IsValid);
    Assert.AreEqual(SlotValidationStep.CrewWeight, result.FailedAtStep);
}

[Test]
public void SlotValidation_OrderIsCorrect()
{
    // GDD Order: Category → Dimension → ModuleWeight → CrewWeight
    var validator = new SlotMatchingValidator();

    // Fail at Category (should not check Dimension)
    var result1 = validator.ValidateComplete(
        CreateModule(EquipmentSlotCategory.AAHeavy, new Vector2Int(1, 1)),
        null,
        CreateSlot(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4)));
    Assert.AreEqual(SlotValidationStep.Category, result1.FailedAtStep);

    // Fail at Dimension (Category passes)
    var result2 = validator.ValidateComplete(
        CreateModule(EquipmentSlotCategory.MainBattery, new Vector2Int(2, 2)),
        null,
        CreateSlot(EquipmentSlotCategory.MainBattery, new Vector2Int(3, 4)));
    Assert.AreEqual(SlotValidationStep.Dimension, result2.FailedAtStep);
}
```

---

## Phase 3: Cargo Storage Testing

### Unit Tests

```csharp
// Tests/EditMode/CargoStorageTests.cs

[Test]
public void HardCap_CannotExceed100Percent()
{
    var weightManager = new HardCapWeightManager(maxWeight: 1000f);

    // Add to 95%
    Assert.IsTrue(weightManager.TryAddWeight(950f));

    // Try to add 10% more (would be 105%)
    Assert.IsFalse(weightManager.TryAddWeight(100f));
    Assert.AreEqual(950f, weightManager.CurrentWeightTons);
}

[Test]
public void WeightBands_ColorCode_MatchesGDD()
{
    // GDD: Green 0-80%, Yellow 80-95%, Orange 95-100%, Red 100%
    Assert.AreEqual(WeightBand.Green, GetWeightBand(0.5f));
    Assert.AreEqual(WeightBand.Green, GetWeightBand(0.79f));
    Assert.AreEqual(WeightBand.Yellow, GetWeightBand(0.80f));
    Assert.AreEqual(WeightBand.Yellow, GetWeightBand(0.94f));
    Assert.AreEqual(WeightBand.Orange, GetWeightBand(0.95f));
    Assert.AreEqual(WeightBand.Orange, GetWeightBand(0.99f));
    Assert.AreEqual(WeightBand.Red, GetWeightBand(1.0f));
}

[Test]
public void TetrisGrid_CanPlaceItem_ChecksBounds()
{
    var grid = new ShipCargoGrid(new Vector2Int(10, 12));
    var item = CreateCargoItem(new Vector2Int(3, 3));

    // Within bounds
    Assert.IsTrue(grid.CanPlaceItem(item, new Vector2Int(0, 0)));
    Assert.IsTrue(grid.CanPlaceItem(item, new Vector2Int(7, 9)));

    // Out of bounds
    Assert.IsFalse(grid.CanPlaceItem(item, new Vector2Int(8, 9)));
    Assert.IsFalse(grid.CanPlaceItem(item, new Vector2Int(-1, 0)));
}

[Test]
public void TetrisGrid_CanPlaceItem_ChecksCollision()
{
    var grid = new ShipCargoGrid(new Vector2Int(10, 12));
    var item1 = CreateCargoItem(new Vector2Int(3, 3));
    var item2 = CreateCargoItem(new Vector2Int(2, 2));

    grid.PlaceItem(item1, new Vector2Int(0, 0));

    // Collides with item1
    Assert.IsFalse(grid.CanPlaceItem(item2, new Vector2Int(1, 1)));

    // Does not collide
    Assert.IsTrue(grid.CanPlaceItem(item2, new Vector2Int(3, 0)));
}

[Test]
public void TetrisGrid_RotatedItem_SwapsDimensions()
{
    var item = CreateCargoItem(new Vector2Int(3, 2));

    Assert.AreEqual(new Vector2Int(3, 2), item.GridSize);

    item.Rotate();
    Assert.IsTrue(item.IsRotated);
    Assert.AreEqual(new Vector2Int(2, 3), item.GridSize);
}

[Test]
public void PortStorageGrid_NoWeightLimit()
{
    var grid = new PortStorageGrid(new Vector2Int(25, 20), PortTier.T5);

    // Should not have weight limit
    Assert.AreEqual(float.MaxValue, grid.MaxWeightTons);
}

[Test]
public void ShipCargoGrid_EnforcesPartitionRestrictions()
{
    var grid = new ShipCargoGrid(new Vector2Int(10, 12));
    grid.AddPartition(new CargoPartitionDefinition
    {
        partitionType = CargoPartitionType.Magazine,
        allowedItemTypes = new List<CargoItemType> { CargoItemType.ShellsAP, CargoItemType.ShellsHE }
    });

    var ammoItem = CreateCargoItem(CargoItemType.ShellsAP);
    var foodItem = CreateCargoItem(CargoItemType.Food);

    // Ammo can go in magazine
    Assert.IsTrue(grid.CanPlaceInPartition(ammoItem, "magazine"));

    // Food cannot go in magazine
    Assert.IsFalse(grid.CanPlaceInPartition(foodItem, "magazine"));
}
```

---

## Phase 4: UI Framework Testing

### Unit Tests

```csharp
// Tests/EditMode/UIFrameworkTests.cs

[Test]
public void TooltipManager_DelayIs500ms()
{
    var manager = new TooltipManager();
    Assert.AreEqual(0.5f, manager.HoverDelay);
}

[Test]
public void CommonStatsPanel_UpdatesOnWeightChange()
{
    var panel = CreateStatsPanel();
    panel.SetWeight(800f, 1000f);

    Assert.AreEqual("80%", panel.WeightPercentText);
    Assert.AreEqual(WeightBand.Green, panel.CurrentWeightBand);
}
```

### PlayMode Tests

```csharp
// Tests/PlayMode/UIFrameworkPlayTests.cs

[UnityTest]
public IEnumerator ScreenNavigation_TabCycles1to5()
{
    var controller = CreateFittingController();
    controller.SwitchToScreen(0);

    // Cycle through all screens
    for (int i = 0; i < 5; i++)
    {
        controller.CycleToNextScreen();
        yield return null;
        Assert.AreEqual((i + 1) % 5, controller.CurrentScreenIndex);
    }
}

[UnityTest]
public IEnumerator DragDrop_Module_ToValidSlot_Works()
{
    var screen = CreateWeaponScreen();
    var module = CreateTestModule();
    var slot = screen.GetSlot(0);

    yield return SimulateDragDrop(module, slot);

    Assert.IsTrue(slot.HasModule);
    Assert.AreEqual(module, slot.InstalledModule);
}

[UnityTest]
public IEnumerator DragDrop_Module_ToInvalidSlot_Rejected()
{
    var screen = CreateWeaponScreen();
    var module = CreateTestModule(EquipmentSlotCategory.MainBattery);
    var slot = screen.GetSlot(EquipmentSlotCategory.AAHeavy);

    yield return SimulateDragDrop(module, slot);

    Assert.IsFalse(slot.HasModule);
}
```

---

## Phase 5: Crew Efficiency Testing

### Unit Tests

```csharp
// Tests/EditMode/CrewEfficiencyTests.cs

[Test]
public void SailorScaling_MatchesGDDFormula()
{
    // Level 1-50: 10 + (Level - 1) × 5
    Assert.AreEqual(10, SailorScaling.GetMaxSailors(1));
    Assert.AreEqual(15, SailorScaling.GetMaxSailors(2));
    Assert.AreEqual(255, SailorScaling.GetMaxSailors(50));

    // Level 51-100: 255 + (Level - 50) × 4
    Assert.AreEqual(259, SailorScaling.GetMaxSailors(51));
    Assert.AreEqual(455, SailorScaling.GetMaxSailors(100));

    // Level 101-150: 455 + (Level - 100) × 3
    Assert.AreEqual(458, SailorScaling.GetMaxSailors(101));
    Assert.AreEqual(605, SailorScaling.GetMaxSailors(150));

    // Level 151-200: 605 + (Level - 150) × 2
    Assert.AreEqual(607, SailorScaling.GetMaxSailors(151));
    Assert.AreEqual(705, SailorScaling.GetMaxSailors(200));
}

[Test]
public void CrewWeight_MatchesGDDFormula()
{
    // Level 1: 10 × 0.1 × 1.01 = 1.01
    Assert.AreEqual(1.01f, CrewWeightCalculator.CalculateCrewWeight(1, 10), 0.01f);

    // Level 50: 255 × 0.1 × 1.50 = 38.25
    Assert.AreEqual(38.25f, CrewWeightCalculator.CalculateCrewWeight(50, 255), 0.1f);

    // Level 100: 455 × 0.1 × 2.00 = 91
    Assert.AreEqual(91f, CrewWeightCalculator.CalculateCrewWeight(100, 455), 0.1f);

    // Level 200: 705 × 0.1 × 3.00 = 211.5
    Assert.AreEqual(211.5f, CrewWeightCalculator.CalculateCrewWeight(200, 705), 0.1f);
}

[Test]
public void StatFactor_MatchesGDDFormula()
{
    var calculator = new ModuleEfficiencyCalculator();

    // Stat 7: 0.84
    Assert.AreEqual(0.84f, calculator.CalculateStatFactor(7), 0.01f);

    // Stat 15 (baseline): 1.00
    Assert.AreEqual(1.00f, calculator.CalculateStatFactor(15), 0.01f);

    // Stat 35: 1.40
    Assert.AreEqual(1.40f, calculator.CalculateStatFactor(35), 0.01f);

    // Stat 50 (cap): 1.70
    Assert.AreEqual(1.70f, calculator.CalculateStatFactor(50), 0.01f);
}

[Test]
public void StatFactor_CappedAt50()
{
    var calculator = new ModuleEfficiencyCalculator();

    // Stat 60 should still be 1.70 (capped at 50)
    Assert.AreEqual(1.70f, calculator.CalculateStatFactor(60), 0.01f);
    Assert.AreEqual(1.70f, calculator.CalculateStatFactor(100), 0.01f);
}

[Test]
public void EngineEfficiency_HasFloorAt70Percent()
{
    var calculator = new ModuleEfficiencyCalculator();
    var crew = CreateCrew(currentSailors: 10, maxSailors: 100); // 10% sailor factor
    var engineModule = CreateModule(EquipmentSlotCategory.EngineRoom);

    var result = calculator.CalculateEfficiency(crew, engineModule, false, true);

    // Without floor would be ~10%, with floor should be 70%
    Assert.GreaterOrEqual(result.TotalEfficiency, 0.70f);
    Assert.IsTrue(result.EngineFloorApplied);
}

[Test]
public void NeutralCrew_Has20PercentPenalty()
{
    var calculator = new ModuleEfficiencyCalculator();
    var crew = CreateCrew(currentSailors: 100, maxSailors: 100);
    var module = CreateModule(EquipmentSlotCategory.MainBattery);

    var normalResult = calculator.CalculateEfficiency(crew, module, false, false);
    var neutralResult = calculator.CalculateEfficiency(crew, module, true, false);

    Assert.AreEqual(normalResult.TotalEfficiency * 0.80f, neutralResult.TotalEfficiency, 0.01f);
    Assert.IsTrue(neutralResult.NeutralPenaltyApplied);
}

[Test]
public void Casualties_MatchGDDLethality()
{
    var manager = new CrewCasualtyManager();
    var crew = CreateCrew(currentSailors: 100, maxSailors: 100);

    // HE: 0.15 lethality
    int heCasualties = manager.CalculateCasualties(500f, 1000f, crew, DamageType.HE);
    // (500/1000) × 100 × 0.15 = 7.5 → 7
    Assert.AreEqual(7, heCasualties);

    // AP Penetrating: 0.25 lethality
    int apCasualties = manager.CalculateCasualties(500f, 1000f, crew, DamageType.APPenetrating);
    // (500/1000) × 100 × 0.25 = 12.5 → 12
    Assert.AreEqual(12, apCasualties);
}

[Test]
public void SpeedModifier_UsesGDDFormula()
{
    // Speed_Mod = 0.7 + (0.3 × Efficiency)
    Assert.AreEqual(0.70f, ModuleEffectCalculator.CalculateSpeedModifier(0f), 0.01f);
    Assert.AreEqual(0.85f, ModuleEffectCalculator.CalculateSpeedModifier(0.5f), 0.01f);
    Assert.AreEqual(1.00f, ModuleEffectCalculator.CalculateSpeedModifier(1.0f), 0.01f);
}
```

---

## Phase 6: Loadouts & Polish Testing

### Unit Tests

```csharp
// Tests/EditMode/LoadoutsTests.cs

[Test]
public void ShareCode_Format_Correct()
{
    var preset = CreatePreset("USS Iowa", new[] { "AA Build" });

    // Format: SHIP-STYLE-XXXXXX
    Assert.IsTrue(preset.shareCode.StartsWith("IOWA-AA-"));
    Assert.AreEqual(14, preset.shareCode.Length); // IOWA-AA-XXXXXX
}

[Test]
public void PresetApplication_DetectsMissingModules()
{
    var preset = CreatePresetWithModules("mod_1", "mod_2", "mod_3");
    var playerInventory = CreateInventoryWith("mod_1"); // Only has mod_1

    var result = manager.ApplyPreset(preset, ship, itemDatabase);

    Assert.IsFalse(result.Success);
    Assert.AreEqual(2, result.MissingModules.Count);
}

[Test]
public void UndoRedo_TracksModuleInstall()
{
    var undoRedo = new UndoRedoManager();

    undoRedo.RecordChange(new ModuleInstallChange("slot1", newModule, null, ApplyModule));

    Assert.IsTrue(undoRedo.CanUndo);
    Assert.IsFalse(undoRedo.CanRedo);

    undoRedo.Undo();

    Assert.IsFalse(undoRedo.CanUndo);
    Assert.IsTrue(undoRedo.CanRedo);
}

[Test]
public void ColorblindMode_AllSchemesValid()
{
    foreach (ColorblindMode mode in Enum.GetValues(typeof(ColorblindMode)))
    {
        var scheme = GetColorScheme(mode);

        // All colors should be distinct
        Assert.AreNotEqual(scheme.Valid, scheme.Warning);
        Assert.AreNotEqual(scheme.Warning, scheme.Invalid);
        Assert.AreNotEqual(scheme.Valid, scheme.Invalid);
    }
}
```

### PlayMode Tests

```csharp
// Tests/PlayMode/LoadoutsPlayTests.cs

[UnityTest]
public IEnumerator SavePreset_AppearsInList()
{
    var manager = LoadoutPresetManager.Instance;
    int initialCount = manager.GetLocalPresets().Count;

    yield return manager.SavePreset(ship, modules, armor, "Test Preset", "",
        LoadoutVisibility.Private, new List<LoadoutTag>());

    Assert.AreEqual(initialCount + 1, manager.GetLocalPresets().Count);
}

[UnityTest]
public IEnumerator KeyboardShortcut_CtrlZ_Undoes()
{
    var controller = CreateFittingController();
    var undoManager = controller.GetUndoManager();

    // Make a change
    controller.InstallModule("slot1", testModule);
    Assert.IsTrue(undoManager.CanUndo);

    // Simulate Ctrl+Z
    yield return SimulateKeyPress(KeyCode.Z, ctrl: true);

    Assert.IsFalse(undoManager.CanUndo);
}
```

---

## Integration Test Suite

### Full Workflow Tests

```csharp
// Tests/PlayMode/IntegrationTests.cs

[UnityTest]
public IEnumerator FullFittingWorkflow()
{
    // 1. Spawn player in port
    yield return SpawnPlayerInPort("port_001");
    Assert.IsTrue(FittingRestrictionManager.Instance.CanModifyFitting());

    // 2. Open fitting UI
    var fittingUI = OpenFittingUI();
    Assert.IsTrue(fittingUI.gameObject.activeSelf);

    // 3. Install module with crew
    var module = GetTestModule();
    var slot = fittingUI.GetSlot(0);
    var crew = GetTestCrew();

    yield return fittingUI.InstallModule(slot, module);
    yield return fittingUI.AssignCrew(slot, crew);

    // 4. Verify efficiency calculation
    var efficiency = slot.GetEfficiency();
    Assert.Greater(efficiency, 0f);

    // 5. Save as preset
    var preset = yield return fittingUI.SaveAsPreset("Test Build");
    Assert.IsNotNull(preset.shareCode);

    // 6. Try to undock
    yield return CloseFittingUI();
    var undockResult = TryUndock();

    Assert.IsTrue(undockResult.CanUndock);
}

[UnityTest]
public IEnumerator CargoTransferWorkflow()
{
    yield return SpawnPlayerInPort("port_001");

    // 1. Open cargo UI
    var cargoUI = OpenCargoScreen();

    // 2. Transfer item from port to ship
    var item = GetTestCargoItem();
    var portGrid = cargoUI.GetPortGrid();
    var shipGrid = cargoUI.GetShipGrid();

    Assert.IsTrue(portGrid.Contains(item));

    yield return TransferItem(item, portGrid, shipGrid, new Vector2Int(0, 0));

    Assert.IsFalse(portGrid.Contains(item));
    Assert.IsTrue(shipGrid.Contains(item));

    // 3. Verify weight updated
    Assert.Greater(shipGrid.CurrentWeight, 0f);

    // 4. Transfer back
    yield return TransferItem(item, shipGrid, portGrid, new Vector2Int(0, 0));

    Assert.IsTrue(portGrid.Contains(item));
    Assert.IsFalse(shipGrid.Contains(item));
}
```

---

## Test Execution Order

### Pre-Commit (< 5 min)

1. All EditMode unit tests
2. Critical PlayMode tests

### Pre-Merge (< 30 min)

1. All unit tests
2. All PlayMode tests
3. Integration tests

### Nightly (Full Suite)

1. Complete test suite
2. Performance benchmarks
3. Memory profiling

---

## Performance Benchmarks

```csharp
// Tests/Performance/PerformanceTests.cs

[Test, Performance]
public void CargoGrid_AutoArrange_1000Items()
{
    var grid = new ShipCargoGrid(new Vector2Int(50, 50));
    var items = CreateRandomItems(1000);

    Measure.Method(() =>
    {
        grid.TryAutoArrange();
    })
    .WarmupCount(3)
    .MeasurementCount(10)
    .Run();

    // Should complete in < 100ms
}

[Test, Performance]
public void EfficiencyCalculation_1000Crews()
{
    var calculator = new ModuleEfficiencyCalculator();
    var crews = CreateRandomCrews(1000);
    var module = CreateTestModule();

    Measure.Method(() =>
    {
        foreach (var crew in crews)
        {
            calculator.CalculateEfficiency(crew, module, false, false);
        }
    })
    .WarmupCount(3)
    .MeasurementCount(10)
    .Run();

    // Should complete in < 10ms
}
```

---

*Testing Requirements - Version 3.0*
