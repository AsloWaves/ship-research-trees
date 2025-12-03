# Controls Reference
**Status**: 📋 PLANNED
**Phase**: Phase 2
**Last Updated**: 2025-12-03

---

## Overview

This document defines all player inputs, their default bindings, and the contexts in which they are available or disabled. All controls are rebindable through the Settings menu.

---

## Input Devices

| Device | Supported | Notes |
|--------|-----------|-------|
| Keyboard | ✅ Yes | Primary input |
| Mouse | ✅ Yes | Camera, targeting, UI |
| Gamepad | ❌ No | Not supported |
| Touch | ❌ No | Not supported |

---

## Control Contexts

Controls are enabled/disabled based on the current game state:

| Context | Description | Active Controls |
|---------|-------------|-----------------|
| **At Sea** | Controlling ship in open water | All ship controls |
| **In Port** | Docked at port | UI navigation only |
| **In Menu** | Any menu open | Menu navigation only |
| **In Combat** | Actively engaged | All ship + combat controls |
| **Dead** | Ship destroyed | Spectate only |
| **Chat Active** | Typing in chat | Text input only |
| **Map Open** | Viewing map overlay | Map + limited ship |

---

## Ship Movement Controls

### Throttle

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Throttle Up | W | Up Arrow | At Sea | Increase by 1 step |
| Throttle Down | S | Down Arrow | At Sea | Decrease by 1 step |
| Full Ahead | Shift + W | - | At Sea | Jump to +4 (flank) |
| Full Astern | Shift + S | - | At Sea | Jump to -4 (emergency reverse) |
| All Stop | X | Numpad 0 | At Sea | Set throttle to 0 |

**Throttle Steps**: -4 (Full Astern) → -2 (Half Astern) → 0 (Stop) → +2 (Half Ahead) → +4 (Full Ahead)

### Steering

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Rudder Left | A | Left Arrow | At Sea | Turn port |
| Rudder Right | D | Right Arrow | At Sea | Turn starboard |
| Rudder Amidships | - | - | At Sea | Release A/D |

**Rudder Behavior**: Hold to turn, release to center rudder

### Autopilot / Waypoints

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Set Waypoint | Right Click | - | At Sea + Map | Click on map to set |
| Clear Waypoints | Ctrl + Right Click | - | At Sea | Clear all waypoints |
| Toggle Autopilot | P | - | At Sea | Follow waypoints |

---

## Camera Controls

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Zoom In | Mouse Wheel Up | + (Plus) | At Sea | Closer view |
| Zoom Out | Mouse Wheel Down | - (Minus) | At Sea | Further view |
| Pan Camera | Middle Mouse (Hold) | - | At Sea | Drag to pan |
| Toggle Camera Mode | C | - | At Sea | Centered ↔ Look-Ahead |
| Reset Camera | Home | - | At Sea | Return to ship |
| Lock Camera | L | - | At Sea | Lock to current position |

**Camera Modes**:
- **Centered**: Camera stays centered on ship
- **Look-Ahead**: Camera leads in direction of movement

---

## Combat Controls

### Weapons

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Fire Primary | Left Click | Space | Combat | Fire main battery |
| Fire Secondary | Ctrl + Left Click | - | Combat | Fire secondary guns |
| Fire Torpedoes | T | - | Combat | Launch torpedo spread |
| Fire AA | Automatic | - | Combat | Auto-fires at aircraft |
| Cease Fire | Z | - | Combat | Stop all firing |

### Targeting

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Select Target | Left Click (on ship) | - | At Sea | Set primary target |
| Cycle Targets | Tab | - | At Sea | Next visible target |
| Cycle Targets (Reverse) | Shift + Tab | - | At Sea | Previous target |
| Clear Target | Escape | - | At Sea | Deselect target |
| Target Nearest | Q | - | Combat | Auto-select closest |

### Weapon Groups

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Select All Weapons | ` (Backtick) | - | Combat | Control all |
| Weapon Group 1 | 1 | Numpad 1 | Combat | Forward guns |
| Weapon Group 2 | 2 | Numpad 2 | Combat | Aft guns |
| Weapon Group 3 | 3 | Numpad 3 | Combat | Port weapons |
| Weapon Group 4 | 4 | Numpad 4 | Combat | Starboard weapons |
| Weapon Group 5-9 | 5-9 | Numpad 5-9 | Combat | Custom groups |

---

## Carrier Controls

*Only available when controlling a carrier*

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Open Air Operations | V | - | At Sea | Aircraft management UI |
| Launch Fighters | Ctrl + 1 | - | At Sea | Launch fighter squadron |
| Launch Bombers | Ctrl + 2 | - | At Sea | Launch bomber squadron |
| Launch Torpedoes | Ctrl + 3 | - | At Sea | Launch torpedo bombers |
| Recall Aircraft | Ctrl + R | - | At Sea | Order all aircraft to return |
| Set CAP | Ctrl + C | - | At Sea | Combat air patrol |

---

## Submarine Controls

*Only available when controlling a submarine*

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Dive | F | - | At Sea (Surface) | Begin dive |
| Surface | R | - | At Sea (Submerged) | Begin surfacing |
| Periscope Depth | Shift + F | - | At Sea | Go to periscope depth |
| Emergency Dive | Ctrl + F | - | At Sea | Crash dive |
| Periscope Up | E | - | Periscope Depth | Raise periscope |
| Periscope Down | Shift + E | - | Periscope Depth | Lower periscope |
| Silent Running | G | - | Submerged | Reduce noise, slower |

---

## Interface Controls

### General UI

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Open Menu | Escape | - | Always | Pause/options menu |
| Open Map | M | Tab | At Sea | Toggle map overlay |
| Open Inventory | I | B | At Sea | Ship inventory |
| Open Ship Status | O | - | At Sea | Damage/crew status |
| Open Chat | Enter | T | At Sea | Chat input |
| Close Window | Escape | - | Any Menu | Close current window |
| Controls Help | F1 | - | Always | Show controls overlay |

### Quick Slots

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Quick Slot 1 | 1 | Numpad 1 | At Sea | Use item in slot 1 |
| Quick Slot 2 | 2 | Numpad 2 | At Sea | Use item in slot 2 |
| Quick Slot 3-9 | 3-9 | Numpad 3-9 | At Sea | Use items 3-9 |

*Note: Number keys default to weapon groups in combat, quick slots otherwise*

### Map Controls

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Pan Map | Click + Drag | Arrow Keys | Map Open | Move map view |
| Zoom Map | Scroll Wheel | +/- | Map Open | Zoom map |
| Center on Ship | Space | Home | Map Open | Jump to player |
| Set Waypoint | Right Click | - | Map Open | Navigation waypoint |
| Ping Location | Ctrl + Click | - | Map Open | Alert squadron |

### Chat Controls

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Send Message | Enter | - | Chat Active | Send typed message |
| Cancel Chat | Escape | - | Chat Active | Close without sending |
| Chat History Up | Up Arrow | - | Chat Active | Previous message |
| Chat History Down | Down Arrow | - | Chat Active | Next message |
| Switch Channel | Tab | - | Chat Active | Cycle: All → Squadron → Local |

---

## Debug Controls

*Only available in development builds*

| Action | Primary | Secondary | Context | Notes |
|--------|---------|-----------|---------|-------|
| Toggle Debug UI | F3 | - | Always | Show debug info |
| Toggle Collision | F4 | - | Debug | Disable collision |
| Spawn Enemy | F5 | - | Debug | Create test enemy |
| God Mode | F6 | - | Debug | Invincibility |
| Free Camera | F7 | - | Debug | Detach camera |
| Time Scale | F8 | - | Debug | Cycle game speed |

---

## Control Lock States

### When Controls Are Disabled

| State | Disabled Controls | Active Controls |
|-------|-------------------|-----------------|
| Menu Open | All ship controls | Menu navigation |
| Chat Active | All except Escape | Text input |
| Dead | All ship controls | Spectate, menu |
| Cutscene | All | Skip (Space) |
| Loading | All | None |
| Disconnected | All | Reconnect prompt |

### Input Priority

When multiple systems want the same input:

```
1. Modal UI (menus, dialogs) - Highest priority
2. Chat input
3. Map controls
4. Combat controls
5. Ship movement
6. Camera controls - Lowest priority
```

---

## Modifier Keys

| Modifier | Effect |
|----------|--------|
| Shift | Alternate action (full throttle, reverse cycle) |
| Ctrl | Secondary action (fire secondary, weapon groups) |
| Alt | Reserved for system (Alt+Tab, etc.) |

---

## Rebinding Restrictions

Some controls cannot be rebound:

| Control | Reason |
|---------|--------|
| Escape | Always opens menu (system standard) |
| Enter | Always activates chat (convention) |
| F1 | Always shows help (accessibility) |
| Mouse movement | Cannot be rebound |

---

## Cross-References

- [[05-UI-Systems/Settings-Options]] - Keybinding settings
- [[02-Core-Gameplay/Ship-Physics]] - Movement mechanics
- [[03-Combat-Systems/Surface-Combat]] - Combat mechanics
- [[03-Combat-Systems/Carrier-Operations]] - Carrier controls
- [[03-Combat-Systems/Submarine-Warfare]] - Submarine controls
- [[05-UI-Systems/Menu-System]] - Menu navigation

---

*Document created: 2025-12-03*
