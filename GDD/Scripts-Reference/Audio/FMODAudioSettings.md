# FMODAudioSettings.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Audio/FMODAudioSettings.cs` |
| **Namespace** | `WOS.Audio` |
| **Type** | Static class |
| **Lines** | ~142 |
| **Architecture** | PlayerPrefs-based audio preferences persistence |

## Purpose
Static utility class managing FMOD audio settings persistence. Saves and loads user preferences for output device selection and volume levels using Unity PlayerPrefs for cross-session storage.

---

## PlayerPrefs Keys

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| `FMOD_OutputDevice` | int | -1 | Driver index (-1 = system default) |
| `FMOD_MasterVolume` | float | 1.0 | Master volume (0.0 - 1.0) |
| `FMOD_MusicVolume` | float | 1.0 | Music bus volume |
| `FMOD_SFXVolume` | float | 1.0 | Sound effects bus volume |
| `FMOD_UIVolume` | float | 1.0 | UI sounds bus volume |

---

## Public API

### Output Device
```csharp
// Save output device driver index
public static void SaveOutputDevice(int driverIndex)

// Load output device (-1 if no preference)
public static int LoadOutputDevice()

// Clear preference (use system default)
public static void ClearOutputDevice()
```

### Volume Controls
```csharp
// Master volume (all audio)
public static void SaveMasterVolume(float volume)
public static float LoadMasterVolume()

// Music bus
public static void SaveMusicVolume(float volume)
public static float LoadMusicVolume()

// Sound effects bus
public static void SaveSFXVolume(float volume)
public static float LoadSFXVolume()

// UI sounds bus
public static void SaveUIVolume(float volume)
public static float LoadUIVolume()
```

### Reset
```csharp
// Clear all FMOD settings
public static void ClearAllSettings()
```

---

## Volume Handling

All volume values are clamped to 0.0 - 1.0 range using `Mathf.Clamp01()`.

```csharp
public static void SaveMasterVolume(float volume)
{
    PlayerPrefs.SetFloat(PREF_MASTER_VOLUME, Mathf.Clamp01(volume));
    PlayerPrefs.Save();
}
```

---

## Usage Example

```csharp
// Save user preferences
FMODAudioSettings.SaveOutputDevice(2);  // Driver index 2
FMODAudioSettings.SaveMasterVolume(0.8f);
FMODAudioSettings.SaveMusicVolume(0.5f);
FMODAudioSettings.SaveSFXVolume(1.0f);

// Load on startup
int device = FMODAudioSettings.LoadOutputDevice();
float master = FMODAudioSettings.LoadMasterVolume();

// Reset to defaults
FMODAudioSettings.ClearAllSettings();
```

---

## Integration Points

### Used By
- `FMODAudioInitializer` - Loads settings on startup
- `FMODAudioDeviceManager` - Saves device selection
- Options menu UI - User volume controls

### Dependencies
- `UnityEngine.PlayerPrefs` - Persistence
- `WOS.Debugging.DebugManager` - Logging

---

## Design Notes

### PlayerPrefs Storage
- Simple cross-platform persistence
- Survives game restarts
- Per-user settings on Windows

### Volume Buses
- Four separate buses: Master, Music, SFX, UI
- Maps to FMOD mixer hierarchy
- All default to 1.0 (full volume)

### Device Selection
- Stores driver index (not device name)
- -1 indicates no preference (system default)
- Must be validated on load (device may be disconnected)
