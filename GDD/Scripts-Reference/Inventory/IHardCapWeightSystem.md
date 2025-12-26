---
tags: [script, inventory, interface, weight, implemented]
script-type: Interface
namespace: WOS.Inventory.Interfaces
file-path: Assets/Scripts/Inventory/Interfaces/IHardCapWeightSystem.cs
status: IMPLEMENTED
size: ~3 KB (135 lines)
feature-group: inventory
---

# IHardCapWeightSystem.cs

## Quick Reference
**Type**: Interface + Enum + Helper Class
**Namespace**: WOS.Inventory.Interfaces
**File**: `Assets/Scripts/Inventory/Interfaces/IHardCapWeightSystem.cs`
**Size**: ~3 KB (135 lines)
**Implementors**: HardCapWeightManager

---

## Purpose
Interface contract for HARD CAP weight system in cargo/inventory. Defines GDD-compliant rules: weight at 100% is a hard block (cannot add cargo, cannot undock). No exceptions.

---

## GDD Rules

| Rule | Enforcement |
|------|-------------|
| Cannot pick up cargo exceeding 100% | `CanAddWeight()` returns false |
| Cannot undock at 100%+ weight | `CanUndock()` returns false |
| Hard block, not penalty | No gradual degradation |
| Applies to Ship Cargo only | NOT equipment slots |

---

## Interface Properties

```csharp
float CurrentWeight { get; }      // Current weight in tons
float MaxWeight { get; }          // Hard cap in tons
float WeightPercentage { get; }   // 0-100+ percentage
bool IsAtHardCap { get; }         // True at 100%+
```

---

## Interface Methods

### Validation
```csharp
bool CanAddWeight(float additionalWeight);  // Check before adding
bool CanUndock();                           // Check before leaving port
```

### Operations
```csharp
bool TryAddWeight(float weight);   // Add weight (fails at cap)
void RemoveWeight(float weight);   // Remove weight
```

---

## Interface Events

```csharp
event Action<float, float> OnWeightChanged;  // (current, max)
event Action OnHardCapReached;               // Cap hit or exceeded
```

---

## WeightStatus Enum

```csharp
public enum WeightStatus
{
    Optimal,   // 0-80%  - Green
    NearLimit, // 80-95% - Yellow
    AtLimit,   // 95-100% - Orange
    HardCap    // 100%+ - Red (blocked)
}
```

---

## WeightStatusHelper Class

```csharp
public static class WeightStatusHelper
{
    public static WeightStatus GetStatus(float percentage);
    public static Color GetStatusColor(WeightStatus status);
}
```

### Status Thresholds

| Range | Status | Color |
|-------|--------|-------|
| 0-80% | Optimal | Green |
| 80-95% | NearLimit | Yellow |
| 95-100% | AtLimit | Orange |
| 100%+ | HardCap | Red |

### Status Colors

| Status | Color | RGB |
|--------|-------|-----|
| Optimal | Green | (0.2, 0.8, 0.2) |
| NearLimit | Yellow | (0.9, 0.9, 0.2) |
| AtLimit | Orange | (0.9, 0.5, 0.1) |
| HardCap | Red | (0.9, 0.2, 0.2) |

---

## Scope Distinction

| System | IHardCapWeightSystem | ISlotMatchingValidator |
|--------|---------------------|------------------------|
| Applies To | Ship Cargo (Tetris grid) | Equipment Slots |
| Rule | Total weight < 100% | Module + Crew <= Slot |
| Type | Global capacity | Per-slot validation |

---

## Integration Points

### Dependencies
- System (Action events)
- UnityEngine (Color)

### Implementors
- [[HardCapWeightManager]] - Primary implementation

### Used By
- [[ShipInventory]] - Cargo weight tracking
- [[InventoryPanel]] - Weight bar display
- [[PortZone]] - Undock validation

---

## Related Files
- [[HardCapWeightManager]] - Implementation
- [[ISlotMatchingValidator]] - Equipment slot interface
- [[ShipInventory]] - Primary consumer

---

## Design Notes
- Interface enables dependency injection
- Static helper avoids instantiation
- Event-based for UI updates
- Color-coded for visual feedback

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added WeightStatus enum
- **2025-01**: Added WeightStatusHelper class

