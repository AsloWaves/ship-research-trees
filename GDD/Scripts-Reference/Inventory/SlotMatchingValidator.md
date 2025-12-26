---
tags: [script, inventory, validation, equipment, implemented]
script-type: Class (Singleton)
namespace: WOS.Inventory.Validation
file-path: Assets/Scripts/Inventory/Validation/SlotMatchingValidator.cs
status: IMPLEMENTED
size: ~5 KB (201 lines)
feature-group: inventory
---

# SlotMatchingValidator.cs

## Quick Reference
**Type**: Class (implements ISlotMatchingValidator)
**Namespace**: WOS.Inventory.Validation
**File**: `Assets/Scripts/Inventory/Validation/SlotMatchingValidator.cs`
**Size**: ~5 KB (201 lines)
**Dependencies**: ISlotMatchingValidator interface

---

## Purpose
Validates equipment slot matching for the equipment system. GDD mandates EXACT dimension matching - module dimensions must match slot dimensions exactly. No Tetris-style freeform placement, no rotation.

---

## GDD Rules

| Rule | Enforcement |
|------|-------------|
| Module dimensions = Slot dimensions | Exact match required |
| No rotation allowed | Width/Height must match directly |
| Module weight <= Slot capacity | Weight validation |
| Module + Crew weight <= Slot capacity | Combined weight check |

---

## Singleton Access

```csharp
public static SlotMatchingValidator Instance { get; } = new SlotMatchingValidator();
```

Static singleton instance. Can also be instantiated directly.

---

## Validation Order

```
1. Dimension Check: Module.gridSize == Slot.slotSize (EXACT)
2. Weight Check: Module.weight <= Slot.maxWeightTons
3. Crew Weight Check: Module.weight + Crew.weight <= Slot.maxWeightTons
```

---

## Core Validation Methods

### Dimension Validation
```csharp
public bool ValidateDimensionMatch(Vector2Int moduleDimension, Vector2Int slotDimension)
```
Returns true only if both X and Y dimensions match exactly.

### Weight Validation
```csharp
public bool ValidateModuleWeight(float moduleWeight, float slotCapacity)
public bool ValidateCombinedWeight(float moduleWeight, float crewWeight, float slotCapacity)
```

---

## Full Validation Methods

### ValidateSlot (Equipment Only)
```csharp
public SlotValidationResult ValidateSlot(
    Vector2Int moduleDimension,
    float moduleWeight,
    Vector2Int slotDimension,
    float slotCapacity)
```

Returns `SlotValidationResult` with detailed failure information.

### ValidateSlotWithCrew (Equipment + Crew)
```csharp
public SlotValidationResult ValidateSlotWithCrew(
    Vector2Int moduleDimension,
    float moduleWeight,
    float crewWeight,
    Vector2Int slotDimension,
    float slotCapacity)
```

Three-step validation including crew weight.

---

## SlotValidationResult

```csharp
public class SlotValidationResult
{
    public bool IsValid;
    public string FailureReason;
    public bool DimensionMatch;
    public bool WeightOk;
    public bool CrewWeightOk;

    public static SlotValidationResult Success()
    public static SlotValidationResult Failure(string reason, bool dimensionMatch, bool weightOk, bool crewWeightOk)
}
```

---

## Failure Messages

| Check Failed | Message Format |
|-------------|----------------|
| Dimension | "Module size (2x3) does not match slot size (3x3)" |
| Weight | "Module weight (15.0t) exceeds slot capacity (12.0t)" |
| Combined | "Combined weight (18.5t = 15.0t module + 3.5t crew) exceeds slot capacity (15.0t)" |

---

## Crew Weight Calculation

### GDD Formula
```csharp
public static float CalculateCrewWeight(int sailorCount, float averageLevel)
{
    // Sailor_Count x 0.1 x (1 + Level/100)
    return sailorCount * 0.1f * (1f + averageLevel / 100f);
}
```

**Explanation**: Each sailor ~100kg (0.1 tons), with slight increase for experience/gear.

### Examples
| Sailors | Level | Weight |
|---------|-------|--------|
| 10 | 1 | 1.01t |
| 10 | 50 | 1.50t |
| 10 | 100 | 2.00t |
| 50 | 50 | 7.50t |

---

## Capacity Helpers

```csharp
public static float GetRemainingCapacity(float moduleWeight, float crewWeight, float slotCapacity)
public static float GetMaxCrewWeight(float moduleWeight, float slotCapacity)
```

---

## Integration Points

### Dependencies
- [[ISlotMatchingValidator]] - Interface contract

### Used By
- [[EquipmentPanel]] - Equipment installation validation
- [[EquipmentSlotUI]] - Drag-drop validation
- [[ServerInventoryManager]] - Server-side validation

---

## Related Files
- [[HardCapWeightManager]] - Cargo weight system (different purpose)
- [[EquipmentSlotUI]] - Equipment slot UI component
- [[EquipmentPanel]] - Equipment management panel
- [[ISlotMatchingValidator]] - Interface definition

---

## Key Difference from HardCapWeightManager

| Aspect | SlotMatchingValidator | HardCapWeightManager |
|--------|----------------------|---------------------|
| Scope | Per equipment slot | Entire cargo hold |
| Rule | Module fits slot exactly | Total under 100% |
| Dimensions | Yes (exact match) | No (Tetris grid) |
| Crew Weight | Per-slot calculation | N/A |

---

## Validation Flow Example

```csharp
// Installing a turret with crew
var result = SlotMatchingValidator.Instance.ValidateSlotWithCrew(
    moduleDimension: new Vector2Int(2, 2),   // Turret is 2x2
    moduleWeight: 10.0f,                      // 10 tons
    crewWeight: 1.5f,                         // 15 sailors at level 50
    slotDimension: new Vector2Int(2, 2),      // Slot requires 2x2
    slotCapacity: 15.0f                       // 15 ton max
);

if (result.IsValid)
{
    // Install equipment
}
else
{
    Debug.Log(result.FailureReason);
    // "Module weight (10.0t) exceeds slot capacity (8.0t)"
}
```

---

## Testing Notes
- Dimensions must match EXACTLY (no rotation)
- Weight validation uses <= (equal is allowed)
- Static helpers for crew weight calculation
- Returns detailed failure information
- Singleton pattern but can be instantiated directly

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added crew weight formula from GDD
- **2025-01**: Added SlotValidationResult for detailed feedback
- **2025-01**: Added capacity helper methods

