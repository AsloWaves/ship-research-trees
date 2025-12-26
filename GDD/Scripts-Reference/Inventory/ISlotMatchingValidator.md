---
tags: [script, inventory, interface, validation, implemented]
script-type: Interface
namespace: WOS.Inventory.Interfaces
file-path: Assets/Scripts/Inventory/Interfaces/ISlotMatchingValidator.cs
status: IMPLEMENTED
size: ~3 KB (128 lines)
feature-group: inventory
---

# ISlotMatchingValidator.cs

## Quick Reference
**Type**: Interface + Struct
**Namespace**: WOS.Inventory.Interfaces
**File**: `Assets/Scripts/Inventory/Interfaces/ISlotMatchingValidator.cs`
**Size**: ~3 KB (128 lines)
**Implementors**: SlotMatchingValidator

---

## Purpose
Interface contract for slot-matching validation in the equipment system. Defines GDD-compliant validation rules: exact dimension matching, weight validation, and combined crew weight checks.

---

## GDD Rules

| Rule | Description |
|------|-------------|
| Dimension Match | Module.gridSize == Slot.slotSize (EXACT) |
| No Rotation | Dimensions must match directly |
| Weight Check | Module.weight <= Slot.maxWeightTons |
| Crew Weight | Module + Crew <= Slot.maxWeightTons |

---

## Validation Order

```
1. Dimension Check: Module.gridSize == Slot.slotSize
2. Weight Check: Module.weight <= Slot.maxWeightTons
3. Crew Weight Check: Module.weight + Crew.weight <= Slot.maxWeightTons
```

---

## Interface Methods

### Dimension Validation
```csharp
bool ValidateDimensionMatch(Vector2Int moduleDimension, Vector2Int slotDimension);
```
Returns true only if X and Y match exactly.

### Weight Validation
```csharp
bool ValidateModuleWeight(float moduleWeight, float slotCapacity);
bool ValidateCombinedWeight(float moduleWeight, float crewWeight, float slotCapacity);
```

### Full Validation
```csharp
SlotValidationResult ValidateSlot(
    Vector2Int moduleDimension,
    float moduleWeight,
    Vector2Int slotDimension,
    float slotCapacity);

SlotValidationResult ValidateSlotWithCrew(
    Vector2Int moduleDimension,
    float moduleWeight,
    float crewWeight,
    Vector2Int slotDimension,
    float slotCapacity);
```

---

## SlotValidationResult Struct

```csharp
public struct SlotValidationResult
{
    public bool IsValid;          // All checks passed
    public bool DimensionMatch;   // Dimensions matched
    public bool WeightOk;         // Module weight OK
    public bool CrewWeightOk;     // Combined weight OK
    public string FailureReason;  // Human-readable error

    public static SlotValidationResult Success();
    public static SlotValidationResult Failure(string reason, bool dimensionMatch, bool weightOk, bool crewWeightOk);
}
```

---

## Factory Methods

### Success
```csharp
SlotValidationResult.Success()
```
Returns result with all checks passed.

### Failure
```csharp
SlotValidationResult.Failure(
    "Module size (2x3) does not match slot size (3x3)",
    dimensionMatch: false,
    weightOk: false,
    crewWeightOk: false)
```
Returns result with specific failure reason.

---

## Integration Points

### Dependencies
- UnityEngine (Vector2Int)

### Implementors
- [[SlotMatchingValidator]] - Primary implementation

### Used By
- [[EquipmentPanel]] - Equipment UI validation
- [[EquipmentSlotUI]] - Drag-drop validation
- [[ServerInventoryManager]] - Server-side validation

---

## Related Files
- [[SlotMatchingValidator]] - Implementation
- [[IHardCapWeightSystem]] - Cargo weight interface (different purpose)

---

## Design Notes
- Interface enables dependency injection for testing
- Struct result avoids heap allocation
- Detailed failure info aids user feedback
- Validation order matches GDD specification

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added SlotValidationResult struct
- **2025-01**: Added crew weight validation

