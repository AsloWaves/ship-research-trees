---
tags: [script, port, enum, implemented]
script-type: Enums
namespace: WOS.Port
file-path: Assets/Scripts/ScriptableObjects/Port/PortEnums.cs
status: IMPLEMENTED
size: ~85 lines
feature-group: port
---

# PortEnums.cs

## Quick Reference
**Type**: Enum Definitions
**Namespace**: WOS.Port
**File**: `Assets/Scripts/ScriptableObjects/Port/PortEnums.cs`
**Size**: ~85 lines
**Dependencies**: None

---

## Purpose
Centralized enum definitions for the Port system. Defines nationality theming and player state machine states for port interactions.

---

## Nationality Enum

```csharp
public enum Nationality
{
    UnitedStates,   // USA visual theme
    UnitedKingdom,  // UK visual theme
    Germany,        // German visual theme
    Japan,          // Japanese visual theme
    France,         // French visual theme
    Italy,          // Italian visual theme
    Russia,         // Russian visual theme
    Neutral         // No national affiliation
}
```

### Nationality Usage
- **Port Theming**: Determines visual style (buildings, flags, decorations)
- **NPC Behavior**: Faction relationships, trade modifiers
- **Visual Style**: Links to PortVisualStyleSO for nation-specific assets

---

## PortPlayerState Enum

```csharp
public enum PortPlayerState
{
    Ocean_Normal,       // Default ocean state
    Ocean_InAoP,        // Inside Area of Protection (invincible)
    Ocean_InAoI,        // Inside Area of Interaction (can enter port)
    Harbor_Sailing,     // Inside harbor, sailing
    Harbor_InDockZone,  // Inside dock trigger zone
    Harbor_AutoDocking, // Auto-docking animation in progress
    Harbor_Docked,      // Fully docked, UI accessible
    Harbor_Undocking,   // Undocking animation in progress
    Harbor_AtExitZone   // At exit zone, can leave harbor
}
```

### State Machine Flow

```
Ocean_Normal
    ↓ (enter AoP radius)
Ocean_InAoP
    ↓ (enter AoI radius)
Ocean_InAoI
    ↓ (press E to enter)
Harbor_Sailing
    ↓ (enter dock zone)
Harbor_InDockZone
    ↓ (press E to dock)
Harbor_AutoDocking
    ↓ (animation complete)
Harbor_Docked
    ↓ (press E to undock)
Harbor_Undocking
    ↓ (animation complete)
Harbor_Sailing
    ↓ (enter exit zone)
Harbor_AtExitZone
    ↓ (press E to exit)
Ocean_InAoI
```

---

## State Behavior Summary

| State | Location | Combat | UI Access | Can Move |
|-------|----------|--------|-----------|----------|
| Ocean_Normal | Ocean | Yes | No | Yes |
| Ocean_InAoP | Ocean (AoP) | No (invincible) | No | Yes |
| Ocean_InAoI | Ocean (AoI) | No (invincible) | Port prompt | Yes |
| Harbor_Sailing | Harbor | No | No | Yes |
| Harbor_InDockZone | Harbor (dock) | No | Dock prompt | Yes |
| Harbor_AutoDocking | Harbor (dock) | No | No | No (auto) |
| Harbor_Docked | Harbor (dock) | No | Port services | No |
| Harbor_Undocking | Harbor (dock) | No | No | No (auto) |
| Harbor_AtExitZone | Harbor (exit) | No | Exit prompt | Yes |

---

## Integration Points

### Dependencies
- None (standalone enum file)

### Used By
- [[PlayerPortStateController]] - State machine implementation
- [[PortDefinitionSO]] - Nationality configuration
- [[HarborSceneManager]] - Visual theme selection
- [[PortVisualStyleSO]] - Nationality-specific assets

---

## Related Files
- [[PlayerPortStateController]] - State machine consumer
- [[PortDefinitionSO]] - Nationality assignment
- [[PortVisualStyleSO]] - Nation-specific visuals

---

## Design Notes
- Centralized enums prevent circular dependencies
- PortPlayerState mirrors networking SyncVar requirements
- Nationality supports future faction system expansion
- States designed for clear UI prompt triggers

---

## Changelog
- **2024-12**: Initial implementation
- **2025-01**: Added Ocean_InAoP and Ocean_InAoI states
- **2025-01**: Added auto-docking/undocking states

