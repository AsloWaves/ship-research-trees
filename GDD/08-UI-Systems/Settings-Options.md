# Settings & Options Menu
**Status**: 📋 PLANNED
**Phase**: Phase 2
**Last Updated**: 2025-12-03

---

## Overview

The Settings menu provides player-configurable options for graphics, audio, controls, and gameplay. As a 2D top-down game with specific naval combat mechanics, many traditional 3D settings are unnecessary.

---

## Settings Categories

### 1. Graphics Settings

#### Display

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Resolution | System resolutions | Native | Standard dropdown |
| Display Mode | Fullscreen / Windowed / Borderless | Fullscreen | |
| VSync | On / Off | On | Prevents screen tearing |
| Frame Rate Limit | 30 / 60 / 120 / Unlimited | 60 | |

#### Visual Quality

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Particle Effects | Low / Medium / High | Medium | Explosions, smoke, ship wakes |
| Weather Effects | On / Off | On | Rain, fog, storm overlays |
| UI Scale | 75% / 100% / 125% / 150% | 100% | Accessibility |

#### Post-Processing Effects

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Post-Processing | On / Off | On | Master toggle for all effects |
| Bloom Intensity | Off / Low / Medium / High | Medium | Glow on explosions, lights |
| Color Grading | Default / Warm / Cool / High Contrast | Default | Visual style preference |
| Vignette | On / Off | On | Screen edge darkening |

#### NOT NEEDED (2D Game)
- ~~Shadow Quality~~ - No 3D shadows
- ~~Anti-Aliasing~~ - Sprites handle this
- ~~Texture Quality~~ - Fixed sprite resolution
- ~~Draw Distance~~ - 2D ocean chunks handle this
- ~~Ambient Occlusion~~ - 3D only
- ~~Ocean Quality~~ - Chunk system is consistent, no quality levels needed
- ~~Ship Detail~~ - Sprites are fixed resolution

---

### 2. Audio Settings

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Master Volume | 0-100 slider | 80 | Controls all audio |
| Music Volume | 0-100 slider | 70 | Background music |
| SFX Volume | 0-100 slider | 100 | Weapons, explosions, UI |
| Ambient Volume | 0-100 slider | 60 | Ocean, weather, environment |
| Voice/Radio Volume | 0-100 slider | 100 | Mission briefings, alerts |
| Mute When Minimized | On / Off | On | |

#### Audio Device
| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Output Device | System devices | Default | May not be needed |

---

### 3. Control Settings

#### Ship Controls

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Throttle Mode | Incremental / Direct | Incremental | Inc: W/S steps, Direct: hold |
| Rudder Mode | Hold / Toggle | Hold | Toggle: A/D sets direction |
| Mouse Steering | On / Off | Off | Optional mouse-based steering |

#### Camera Controls

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Zoom Sensitivity | 0.5x - 2.0x slider | 1.0x | Mouse wheel speed |
| Pan Speed | 0.5x - 2.0x slider | 1.0x | Middle mouse pan speed |
| Edge Scrolling | On / Off | Off | Pan when mouse at screen edge |
| Camera Mode | Centered / Look-Ahead | Look-Ahead | |

#### Keybindings

**Rebindable Keys** (store in PlayerPrefs or config file):

| Action | Default Primary | Default Secondary |
|--------|-----------------|-------------------|
| Throttle Up | W | Up Arrow |
| Throttle Down | S | Down Arrow |
| Rudder Left | A | Left Arrow |
| Rudder Right | D | Right Arrow |
| All Stop | X | - |
| Full Ahead | Shift + W | - |
| Full Astern | Shift + S | - |
| Toggle Camera Mode | C | - |
| Zoom In | Mouse Wheel Up | + |
| Zoom Out | Mouse Wheel Down | - |
| Open Map | M | Tab |
| Open Inventory | I | - |
| Open Chat | Enter | T |
| Quick Slots 1-9 | 1-9 | - |
| Controls Help | F1 | - |
| Pause/Menu | Escape | - |

---

### 4. Gameplay Settings

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Show Tutorials | On / Off | On | Tutorial mission prompts |
| Combat Tooltips | On / Off | On | Damage numbers, hit indicators |
| Show Ship Names | Always / Hostile Only / Never | Always | |
| Minimap Size | Small / Medium / Large | Medium | |
| Auto-Anchor at Port | On / Off | On | |

#### HUD Options

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Show Speed/Heading | On / Off | On | |
| Show Throttle Indicator | On / Off | On | |
| Show Damage Indicators | On / Off | On | Directional damage |
| Show Crew Status | On / Off | On | |
| Compact HUD | On / Off | Off | Minimal HUD mode |

---

### 5. Accessibility Settings

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Colorblind Mode | Off / Deuteranopia / Protanopia / Tritanopia | Off | Adjust UI colors |
| High Contrast UI | On / Off | Off | Increased contrast |
| Screen Shake | 0% - 100% slider | 100% | Reduce/disable camera shake |
| Flash Effects | On / Reduced / Off | On | Explosion flashes |
| Text Size | Small / Medium / Large / XL | Medium | |
| Subtitles | On / Off | On | For any voice content |

---

### 6. Network/Online Settings

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Show Ping | On / Off | Off | Display latency |
| Chat Filter | On / Off | On | Profanity filter |
| Chat Timestamps | On / Off | Off | |
| Allow Trade Requests | All / Friends / Squadron / None | All | |
| Allow Party Invites | All / Friends / None | All | |

---

### 7. Language Settings

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Language | See priority list below | English | Full UI localization |
| Voice Language | Match UI / English Only | Match UI | If voice content exists |

#### Language Priority Order
1. **English** (Primary)
2. **Spanish** (Large global audience)
3. **Portuguese** (Brazil market)
4. **German** (Strong naval history interest)
5. **French**
6. **Japanese** (Naval gaming market)
7. **Simplified Chinese**
8. **Russian**
9. **Korean**

#### Localization Scope
- **Full Localization**: UI text, menus, tooltips, mission text
- **Partial Localization**: Ship names (historical, may keep original)
- **Not Localized**: Player names, chat messages

---

### 8. Streamer Mode

Privacy settings for content creators streaming/recording gameplay.

| Setting | Options | Default | Notes |
|---------|---------|---------|-------|
| Streamer Mode | On / Off | Off | Master toggle |
| Hide Username | On / Off | Off | Replaces name with generic |
| Hide Chat | On / Off | Off | Hides chat window entirely |
| Hide Squadron Names | On / Off | Off | Anonymizes squadron/guild |
| Hide Other Player Names | On / Off | Off | Shows "Player" instead |
| Delay Chat | 0 / 30 / 60 / 120 sec | 0 | Stream delay for chat |

#### When Streamer Mode is ON
- Player's username replaced with "Commander" or custom alias
- Chat can be hidden or delayed
- Other players' names can be anonymized
- Squadron/guild names hidden
- Prevents stream sniping via player lookup

---

## F1 Controls Panel

A quick-reference panel accessible anytime via F1 key:

```
┌─────────────────────────────────────────────────────────┐
│                    CONTROLS HELP (F1)                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  MOVEMENT                    CAMERA                     │
│  W/S - Throttle Up/Down      Scroll - Zoom In/Out      │
│  A/D - Rudder Left/Right     MMB - Pan Camera          │
│  X - All Stop                C - Toggle Camera Mode    │
│  Shift+W - Full Ahead                                  │
│  Shift+S - Full Astern       INTERFACE                 │
│                              M - Map                    │
│  COMBAT                      I - Inventory             │
│  LMB - Fire Primary          Enter - Chat              │
│  RMB - Fire Secondary        Esc - Menu                │
│  1-9 - Quick Slots           Tab - Scoreboard          │
│                                                         │
│             [View Full Keybindings]                     │
│                                                         │
│               Press F1 to close                         │
└─────────────────────────────────────────────────────────┘
```

---

## Settings Storage

### PlayerPrefs (Unity)
- Simple key-value storage
- Persists across sessions
- Good for: Volume, keybindings, toggles

### Config File (JSON)
- More complex settings
- Shareable between machines
- Good for: Full keybind profiles, advanced options

### Server-Synced Settings
- Stored in player account database
- Follows player across devices
- Good for: Gameplay preferences, UI layout

---

## Reset Options

| Reset Type | What It Resets |
|------------|----------------|
| Reset Keybindings | All keybinds to default |
| Reset Graphics | Graphics settings to auto-detected |
| Reset Audio | All volumes to default |
| Reset All | Complete settings reset |

---

## Design Decisions (Resolved)

| Question | Decision |
|----------|----------|
| Post-Processing? | **YES** - Bloom, color grading, vignette with toggle |
| Gamepad Support? | **NO** - Keyboard/mouse only |
| Localization? | **YES** - Multi-language, English first priority |
| Streamer Mode? | **YES** - Hide username, chat, other player names |
| Language Priority? | EN → ES → PT → DE → FR → JA → ZH → RU → KO |

---

## Open Questions

1. **Cloud Save Settings**: Sync settings across devices via account?

---

## Implementation Notes

### What We DON'T Need (2D Game / Solo Dev)
- Complex graphics presets (Low/Medium/High/Ultra auto-detect)
- Benchmark mode
- HDR settings
- Ray tracing options
- Advanced audio (surround sound configuration)
- Gamepad configuration
- Ocean/ship quality levels (sprites are fixed)
- Anti-aliasing controls

### What We DO Need (Core Experience)
- Resolution/display mode
- VSync/frame rate limit
- Post-processing toggles (bloom, etc.)
- Volume sliders (5 channels)
- Keybinding system
- UI scale
- Colorblind modes
- Language selection

---

## Cross-References

- [[08-UI-Systems/Menu-System]] - Menu navigation
- [[08-UI-Systems/UI-Overview]] - MUIP framework
- [[13-Technical/Performance-Targets]] - Graphics targets

---

*Document created: 2025-12-03*
*To be refined through discussion*
