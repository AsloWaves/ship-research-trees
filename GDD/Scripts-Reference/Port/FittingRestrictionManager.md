---
tags: [script, port, fitting, restriction, implemented]
script-type: MonoBehaviour
namespace: WOS.Port
file-path: Assets/Scripts/Port/FittingRestrictionManager.cs
status: IMPLEMENTED
size: ~223 lines
feature-group: port
---

# FittingRestrictionManager.cs

## Quick Reference
**Type**: MonoBehaviour (Singleton, DontDestroyOnLoad)
**Namespace**: WOS.Port
**File**: `Assets/Scripts/Port/FittingRestrictionManager.cs`
**Size**: ~223 lines
**Dependencies**: PortTier, PortTierHelper

---

## Purpose
Client-side manager enforcing GDD rule: Equipment fitting is ONLY available in Port. Cannot modify equipment or assign crew at sea.

---

## GDD Rules

| Rule | Enforcement |
|------|-------------|
| Equipment fitting only in port | `IsFittingAllowed` check |
| Cannot modify equipment at sea | `CanPerformFitting()` returns false |
| Cannot assign/unassign crew at sea | `CanPerformFitting()` returns false |

---

## Events

```csharp
public event Action<bool> OnFittingAvailabilityChanged;
public event Action<string, string> OnEnteredPort;
public event Action<string, string> OnExitedPort;
```

---

## Properties

```csharp
public bool IsInPort => isInPort;
public bool IsFittingAllowed => isInPort && currentPortSupportsFitting;
public string CurrentPortId => currentPortId;
public PortTier CurrentPortTier => currentPortTier;
```

---

## Validation

```csharp
public bool CanPerformFitting(string operationName)
{
    if (!IsFittingAllowed)
    {
        string reason = !isInPort
            ? "You must be in a port to modify equipment."
            : "This port does not support ship customization.";
        return false;
    }
    return true;
}

public string GetFittingBlockedReason();
public int GetCurrentPortStorageCapacity();
```

---

## Integration Points

### Used By
- [[EquipmentPanel]], [[CrewPanel]], [[PortZone]]

