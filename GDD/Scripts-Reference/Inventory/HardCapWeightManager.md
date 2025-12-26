---
tags: [script, inventory, weight, validation, implemented]
script-type: Serializable Class
namespace: WOS.Inventory.Core
file-path: Assets/Scripts/Inventory/Core/HardCapWeightManager.cs
status: IMPLEMENTED
size: ~6 KB (237 lines)
feature-group: inventory
---

# HardCapWeightManager.cs

## Quick Reference
**Type**: Serializable Class (implements IHardCapWeightSystem)
**Namespace**: WOS.Inventory.Core
**File**: `Assets/Scripts/Inventory/Core/HardCapWeightManager.cs`
**Size**: ~6 KB (237 lines)
**Dependencies**: IHardCapWeightSystem interface

---

## Purpose
Enforces hard cap weight limits for ship cargo inventory. GDD mandates weight as a HARD CAP at 100% - cannot pick up cargo exceeding limit, cannot undock at 100%+ weight. NO EXCEPTIONS.

**Scope**: Applies to Ship Cargo (Tetris grid), NOT equipment slots.

---

## GDD Rules

| Rule | Enforcement |
|------|-------------|
| Cannot pick up cargo exceeding 100% | `CanAddWeight()` returns false |
| Cannot undock at 100%+ weight | `CanUndock()` returns false |
| Hard block, not penalty | No gradual degradation |

---

## Configuration

```csharp
[SerializeField]
private float currentWeight = 0f;  // Current weight in tons

[SerializeField]
private float maxWeight = 100f;    // Maximum capacity (hard cap)
```

---

## Constructors

```csharp
// Default: 100 ton capacity
public HardCapWeightManager()

// Custom capacity
public HardCapWeightManager(float maxWeightCapacity)
```

---

## Events

```csharp
// Fired when weight changes (currentWeight, maxWeight)
public event Action<float, float> OnWeightChanged;

// Fired when hard cap is reached or exceeded
public event Action OnHardCapReached;
```

---

## Properties

```csharp
public float CurrentWeight => currentWeight;
public float MaxWeight => maxWeight;
public float WeightPercentage => (currentWeight / maxWeight) * 100f;
public bool IsAtHardCap => currentWeight >= maxWeight;
```

---

## Core Validation Methods

### CanAddWeight
```csharp
public bool CanAddWeight(float additionalWeight)
```
Returns true if adding weight stays within hard cap.

### CanUndock
```csharp
public bool CanUndock()
```
Returns true if weight is **strictly less than** max weight.
- At exactly 100%: Cannot undock
- At 99.9%: Can undock

---

## Weight Operations

### TryAddWeight
```csharp
public bool TryAddWeight(float weight)
```
Attempts to add weight. Returns false if blocked by hard cap.
- Fires `OnHardCapReached` if blocked or cap reached.

### RemoveWeight
```csharp
public void RemoveWeight(float weight)
```
Removes weight (cannot go below 0).

### Reset
```csharp
public void Reset()
```
Resets weight to zero.

---

## Capacity Helpers

```csharp
public float GetRemainingCapacity()     // Max 0 if over cap
public float GetAddableWeight(float desiredWeight)  // For partial pickups
```

---

## Weight Status System

```csharp
public WeightStatus GetStatus()
public Color GetStatusColor()
```

Uses `WeightStatusHelper` for UI-friendly status display.

---

## Initialization

```csharp
public void Initialize(float current, float max)
public void SetMaxWeight(float newMaxWeight)
```

`Initialize()` - Used for loading saved state.
`SetMaxWeight()` - Fires `OnHardCapReached` if now over capacity.

---

## Weight Status Thresholds

| Status | Range | Description |
|--------|-------|-------------|
| Empty | 0% | No cargo |
| Light | 0-25% | Minimal impact |
| Moderate | 25-50% | Noticeable load |
| Heavy | 50-75% | Significant load |
| Critical | 75-99% | Near capacity |
| AtCap | 100%+ | Cannot add or undock |

---

## Debug Output

```csharp
public override string ToString()
// Output: "Weight: 85.0/100.0t (85.0%) - Heavy"
```

---

## Integration Points

### Dependencies
- [[IHardCapWeightSystem]] - Interface contract
- [[WeightStatusHelper]] - Status color/enum mapping

### Used By
- [[ShipInventory]] - Cargo weight enforcement
- [[InventoryPanel]] - Weight display
- [[PortInventory]] - Transfer validation (uses destination checks)

---

## Related Files
- [[ShipInventory]] - Primary consumer for cargo grid
- [[SlotMatchingValidator]] - Equipment slot weight (different system)
- [[IHardCapWeightSystem]] - Interface definition

---

## Key Difference from SlotMatchingValidator

| System | HardCapWeightManager | SlotMatchingValidator |
|--------|---------------------|----------------------|
| Applies To | Ship Cargo (Tetris grid) | Equipment Slots |
| Type | Global capacity limit | Per-slot weight limit |
| Rule | Total weight < 100% | Module + Crew <= Slot capacity |

---

## Testing Notes
- Serializable for persistence
- Events fire for UI updates
- `CanUndock()` uses strict less-than (100% = blocked)
- `TryAddWeight()` fires `OnHardCapReached` on both block and reaching cap
- Negative weight additions return false

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added weight status system
- **2025-01**: Added partial pickup support
- **2025-01**: Added event system

