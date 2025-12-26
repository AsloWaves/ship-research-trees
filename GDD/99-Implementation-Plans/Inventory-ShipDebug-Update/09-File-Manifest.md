# File Manifest

**Purpose**: Complete list of all files to create or modify across all phases

---

## Summary

| Phase | New Files | Modified Files | Total |
|-------|-----------|----------------|-------|
| Pre-Phase | 12 | 2 | 14 |
| Phase 1 | 6 | 3 | 9 |
| Phase 2 | 5 | 2 | 7 |
| Phase 3 | 8 | 1 | 9 |
| Phase 4 | 12 | 1 | 13 |
| Phase 5 | 8 | 2 | 10 |
| Phase 6 | 10 | 1 | 11 |
| **Total** | **61** | **12** | **73** |

---

## Pre-Phase: Foundation

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/ScriptableObjects/Ships/ShipConfigurationSO.cs` | Unified ship configuration (expanded) |
| `Assets/Scripts/ScriptableObjects/Ships/EquipmentSlotDefinition.cs` | Slot definition with category + dimension |
| `Assets/Scripts/ScriptableObjects/Ships/WingSlotDefinition.cs` | Carrier wing slots |
| `Assets/Scripts/ScriptableObjects/Ships/ArmorZoneConfiguration.cs` | 9 armor zones |
| `Assets/Scripts/ScriptableObjects/Ships/CargoPartitionDefinition.cs` | Cargo partition system |
| `Assets/Scripts/Core/Enums/ShipEnums.cs` | ShipType, Nation, Era enums |
| `Assets/Scripts/Inventory/Interfaces/ISlotMatchingValidator.cs` | Slot validation interface |
| `Assets/Scripts/Inventory/Interfaces/IHardCapWeightSystem.cs` | Weight management interface |
| `Assets/Scripts/Inventory/Interfaces/ITetrisGrid.cs` | Tetris grid interface |
| `Assets/Scripts/ScriptableObjects/Ships/HardpointVisualSize.cs` | Visual sizing enum |
| `Assets/Scripts/ScriptableObjects/Ships/AircraftType.cs` | Aircraft type enum |
| `Assets/Scripts/ScriptableObjects/Ships/ArmorMaterial.cs` | Armor material enum |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/ScriptableObjects/ShipConfigurationSO.cs` | DELETE (old namespace) |
| All files referencing old ShipConfigurationSO | Update using statements |

---

## Phase 1: Port Integration

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/Ports/PortTier.cs` | Port tier enum (T1-T10) |
| `Assets/Scripts/ScriptableObjects/Ports/PortConfigurationSO.cs` | Port configuration |
| `Assets/Scripts/Player/PlayerSpawnManager.cs` | Spawn handling |
| `Assets/Scripts/Ports/FittingRestrictionManager.cs` | Singleton for fitting restrictions |
| `Assets/Scripts/Ports/PortSafeZone.cs` | Safe zone trigger component |
| `Assets/Scripts/Ports/UndockingValidator.cs` | Undocking validation |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/UI/Inventory/InventoryPanel.cs` | Add port restriction checks |
| `Assets/Scripts/UI/Inventory/EquipmentPanel.cs` | Add port restriction checks |
| `Assets/Scenes/Main.unity` | Add port safe zone triggers |

---

## Phase 2: Slot-Matching System

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/Inventory/SlotMatchingValidator.cs` | Validation implementation |
| `Assets/Scripts/UI/Fitting/EquipmentSlotUI.cs` | Slot UI component |
| `Assets/Scripts/UI/Fitting/FiringArcVisualizer.cs` | Weapon arc display |
| `Assets/Scripts/UI/Fitting/ModuleDragHandler.cs` | Drag-drop handling |
| `Assets/Scripts/UI/Fitting/SlotHighlightSystem.cs` | Visual feedback system |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/ScriptableObjects/Items/ModuleDefinitionSO.cs` | Add slotCategory, gridSize, weightTons |
| `Assets/Scripts/ScriptableObjects/Items/TurretDefinitionSO.cs` | Add slot-matching fields |

---

## Phase 3: Cargo Storage System

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/Cargo/HardCapWeightManager.cs` | Weight management with hard cap |
| `Assets/Scripts/Cargo/TetrisGridBase.cs` | Abstract grid class |
| `Assets/Scripts/Cargo/ShipCargoGrid.cs` | Ship cargo with weight + partitions |
| `Assets/Scripts/Cargo/PortStorageGrid.cs` | Port storage (no weight) |
| `Assets/Scripts/Cargo/CargoItem.cs` | Cargo item with stacking, rotation |
| `Assets/Scripts/Cargo/CargoTransferManager.cs` | Transfer operations |
| `Assets/Scripts/Cargo/CargoDamageManager.cs` | Explosion/fire risk |
| `Assets/Scripts/Cargo/CargoAutoArranger.cs` | Auto-sort algorithm |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/ScriptableObjects/Ships/ShipConfigurationSO.cs` | Add cargoGridSize, cargoPartitions |

---

## Phase 4: UI Framework

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/UI/Fitting/WeaponHardpointScreen.cs` | Screen 1: Weapons |
| `Assets/Scripts/UI/Fitting/ShipSystemsScreen.cs` | Screen 2: Systems |
| `Assets/Scripts/UI/Fitting/ArmorConfigScreen.cs` | Screen 3: Armor |
| `Assets/Scripts/UI/Fitting/CargoGridScreen.cs` | Screen 4: Cargo |
| `Assets/Scripts/UI/Fitting/LoadoutPresetsScreen.cs` | Screen 5: Loadouts |
| `Assets/Scripts/UI/Fitting/CommonStatsPanel.cs` | Bottom stats panel |
| `Assets/Scripts/UI/Fitting/TooltipManager.cs` | Tooltip with 0.5s delay |
| `Assets/Scripts/UI/Fitting/ComparisonTooltip.cs` | Module comparison |
| `Assets/Scripts/UI/Fitting/CargoGridCell.cs` | Grid cell component |
| `Assets/Scripts/UI/Fitting/CargoPartitionOverlay.cs` | Partition visualization |
| `Assets/Scripts/UI/Fitting/ArmorZoneSlider.cs` | Armor thickness slider |
| `Assets/Scripts/UI/Fitting/WeightBarDisplay.cs` | Weight bar with colors |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/Testing/InventoryTestManager.cs` | Update for new UI |

---

## Phase 5: Crew Efficiency

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/Crew/SailorScaling.cs` | Sailor count formulas |
| `Assets/Scripts/Crew/CrewWeightCalculator.cs` | Crew weight formulas |
| `Assets/Scripts/Crew/ModuleEfficiencyCalculator.cs` | Efficiency calculations |
| `Assets/Scripts/Crew/ModuleEffectCalculator.cs` | Stat-to-module effects |
| `Assets/Scripts/Crew/CrewCard.cs` | Crew card data structure |
| `Assets/Scripts/Crew/CrewCasualtyManager.cs` | Casualty system |
| `Assets/Scripts/UI/Fitting/CrewAssignmentPanel.cs` | Crew assignment UI |
| `Assets/Scripts/UI/HUD/ModuleStatusDisplay.cs` | Real-time status |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/Player/Data/CrewData.cs` | Align with new CrewCard |
| `Assets/Scripts/UI/Inventory/CrewSlotUI.cs` | Update for efficiency display |

---

## Phase 6: Loadouts & Polish

### New Files

| File Path | Description |
|-----------|-------------|
| `Assets/Scripts/Loadouts/LoadoutPreset.cs` | Preset data structure |
| `Assets/Scripts/Loadouts/LoadoutPresetManager.cs` | Preset management |
| `Assets/Scripts/UI/Fitting/UndoRedoManager.cs` | Change tracking |
| `Assets/Scripts/UI/Fitting/FittingKeyboardShortcuts.cs` | Keyboard shortcuts |
| `Assets/Scripts/UI/Accessibility/ColorblindModeManager.cs` | Colorblind support |
| `Assets/Scripts/UI/Fitting/PresetCardUI.cs` | Preset card display |
| `Assets/Scripts/UI/Fitting/ShareCodeGenerator.cs` | Share code creation |
| `Assets/Scripts/UI/Fitting/ShipFittingUIController.cs` | Main controller |
| `Assets/Scripts/UI/Fitting/CrewSelectionSlotUI.cs` | Crew selection UI |
| `Assets/Scripts/UI/Fitting/SaveConfirmDialog.cs` | Save confirmation |

### Modified Files

| File Path | Changes |
|-----------|---------|
| `Assets/Scripts/UI/Inventory/InventoryPanel.cs` | Final integration |

---

## Test Files

### EditMode Tests

| File Path | Description |
|-----------|-------------|
| `Assets/Tests/EditMode/ShipConfigurationSOTests.cs` | Pre-Phase tests |
| `Assets/Tests/EditMode/PortIntegrationTests.cs` | Phase 1 tests |
| `Assets/Tests/EditMode/SlotMatchingTests.cs` | Phase 2 tests |
| `Assets/Tests/EditMode/CargoStorageTests.cs` | Phase 3 tests |
| `Assets/Tests/EditMode/UIFrameworkTests.cs` | Phase 4 tests |
| `Assets/Tests/EditMode/CrewEfficiencyTests.cs` | Phase 5 tests |
| `Assets/Tests/EditMode/LoadoutsTests.cs` | Phase 6 tests |

### PlayMode Tests

| File Path | Description |
|-----------|-------------|
| `Assets/Tests/PlayMode/PortIntegrationPlayTests.cs` | Phase 1 play tests |
| `Assets/Tests/PlayMode/UIFrameworkPlayTests.cs` | Phase 4 play tests |
| `Assets/Tests/PlayMode/LoadoutsPlayTests.cs` | Phase 6 play tests |
| `Assets/Tests/PlayMode/IntegrationTests.cs` | Full workflow tests |

### Performance Tests

| File Path | Description |
|-----------|-------------|
| `Assets/Tests/Performance/PerformanceTests.cs` | Benchmark tests |

---

## ScriptableObject Assets

### New Assets to Create

| Asset Path | Type |
|------------|------|
| `Assets/ScriptableObjects/Ports/PortConfig_T1.asset` | PortConfigurationSO |
| `Assets/ScriptableObjects/Ports/PortConfig_T5.asset` | PortConfigurationSO |
| `Assets/ScriptableObjects/Ports/PortConfig_T10.asset` | PortConfigurationSO |
| `Assets/ScriptableObjects/Ships/Fletcher_DD.asset` | ShipConfigurationSO |
| `Assets/ScriptableObjects/Ships/Cleveland_CL.asset` | ShipConfigurationSO |
| `Assets/ScriptableObjects/Ships/Iowa_BB.asset` | ShipConfigurationSO |

---

## Prefabs

### New Prefabs

| Prefab Path | Description |
|-------------|-------------|
| `Assets/Prefabs/UI/Fitting/FittingUICanvas.prefab` | Main fitting UI |
| `Assets/Prefabs/UI/Fitting/EquipmentSlotUI.prefab` | Slot component |
| `Assets/Prefabs/UI/Fitting/CargoGridCell.prefab` | Grid cell |
| `Assets/Prefabs/UI/Fitting/CargoItem.prefab` | Draggable cargo |
| `Assets/Prefabs/UI/Fitting/TooltipPanel.prefab` | Tooltip UI |
| `Assets/Prefabs/UI/Fitting/PresetCard.prefab` | Preset display |
| `Assets/Prefabs/UI/Fitting/CrewSlotUI.prefab` | Crew selection |
| `Assets/Prefabs/Ports/PortSafeZone.prefab` | Safe zone trigger |

### Modified Prefabs

| Prefab Path | Changes |
|-------------|---------|
| `Assets/Prefabs/Player/PlayerShip.prefab` | Add cargo grid reference |

---

## Scenes

### Modified Scenes

| Scene Path | Changes |
|------------|---------|
| `Assets/Scenes/Main.unity` | Add port safe zones, fitting UI |
| `Assets/Scenes/MainMenu.unity` | Add loadout selection |

---

## Directory Structure

```
Assets/Scripts/
├── Cargo/
│   ├── CargoAutoArranger.cs
│   ├── CargoDamageManager.cs
│   ├── CargoItem.cs
│   ├── CargoTransferManager.cs
│   ├── HardCapWeightManager.cs
│   ├── PortStorageGrid.cs
│   ├── ShipCargoGrid.cs
│   └── TetrisGridBase.cs
├── Core/
│   └── Enums/
│       └── ShipEnums.cs
├── Crew/
│   ├── CrewCard.cs
│   ├── CrewCasualtyManager.cs
│   ├── CrewWeightCalculator.cs
│   ├── ModuleEffectCalculator.cs
│   ├── ModuleEfficiencyCalculator.cs
│   └── SailorScaling.cs
├── Inventory/
│   ├── Interfaces/
│   │   ├── IHardCapWeightSystem.cs
│   │   ├── ISlotMatchingValidator.cs
│   │   └── ITetrisGrid.cs
│   └── SlotMatchingValidator.cs
├── Loadouts/
│   ├── LoadoutPreset.cs
│   └── LoadoutPresetManager.cs
├── Ports/
│   ├── FittingRestrictionManager.cs
│   ├── PortSafeZone.cs
│   ├── PortTier.cs
│   └── UndockingValidator.cs
├── ScriptableObjects/
│   ├── Ports/
│   │   └── PortConfigurationSO.cs
│   └── Ships/
│       ├── AircraftType.cs
│       ├── ArmorMaterial.cs
│       ├── ArmorZoneConfiguration.cs
│       ├── CargoPartitionDefinition.cs
│       ├── EquipmentSlotDefinition.cs
│       ├── HardpointVisualSize.cs
│       ├── ShipConfigurationSO.cs
│       └── WingSlotDefinition.cs
└── UI/
    ├── Accessibility/
    │   └── ColorblindModeManager.cs
    ├── Fitting/
    │   ├── ArmorConfigScreen.cs
    │   ├── ArmorZoneSlider.cs
    │   ├── CargoGridCell.cs
    │   ├── CargoGridScreen.cs
    │   ├── CargoPartitionOverlay.cs
    │   ├── CommonStatsPanel.cs
    │   ├── ComparisonTooltip.cs
    │   ├── CrewAssignmentPanel.cs
    │   ├── CrewSelectionSlotUI.cs
    │   ├── EquipmentSlotUI.cs
    │   ├── FiringArcVisualizer.cs
    │   ├── FittingKeyboardShortcuts.cs
    │   ├── LoadoutPresetsScreen.cs
    │   ├── ModuleDragHandler.cs
    │   ├── PresetCardUI.cs
    │   ├── SaveConfirmDialog.cs
    │   ├── ShareCodeGenerator.cs
    │   ├── ShipFittingUIController.cs
    │   ├── ShipSystemsScreen.cs
    │   ├── SlotHighlightSystem.cs
    │   ├── TooltipManager.cs
    │   ├── UndoRedoManager.cs
    │   ├── WeaponHardpointScreen.cs
    │   └── WeightBarDisplay.cs
    └── HUD/
        └── ModuleStatusDisplay.cs
```

---

## Implementation Order

### Phase Execution Sequence

1. **Pre-Phase**: Foundation (namespaces, enums, interfaces)
2. **Phase 1**: Port Integration (spawn, safe zones, restrictions)
3. **Phase 2**: Slot-Matching (validation, drag-drop)
4. **Phase 3**: Cargo Storage (grids, weight, partitions)
5. **Phase 4**: UI Framework (5 screens, common panel)
6. **Phase 5**: Crew Efficiency (formulas, casualties)
7. **Phase 6**: Loadouts (presets, undo/redo, polish)

### Dependencies

```
Pre-Phase → Phase 1 → Phase 2 → Phase 4
                  ↓         ↓
               Phase 3 → Phase 4
                              ↓
                         Phase 5 → Phase 6
```

---

## Critical Path Files

These files must be completed first as others depend on them:

1. `ShipConfigurationSO.cs` (Pre-Phase)
2. `EquipmentSlotDefinition.cs` (Pre-Phase)
3. `ISlotMatchingValidator.cs` (Pre-Phase)
4. `ITetrisGrid.cs` (Pre-Phase)
5. `SlotMatchingValidator.cs` (Phase 2)
6. `TetrisGridBase.cs` (Phase 3)
7. `ModuleEfficiencyCalculator.cs` (Phase 5)

---

*File Manifest - Version 3.0*
