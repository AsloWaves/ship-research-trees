# FMODAudioInitializer.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Audio/FMODAudioInitializer.cs` |
| **Namespace** | `WOS.Audio` |
| **Inheritance** | `MonoBehaviour` |
| **Pattern** | Singleton (DontDestroyOnLoad) |
| **Lines** | ~167 |
| **Architecture** | Game startup audio initialization |

## Purpose
Initializes FMOD audio system on game startup. Automatically applies saved output device and volume preferences. Must be placed on a persistent GameObject in the first scene (MainMenu).

---

## Configuration

### Inspector Settings
| Setting | Default | Description |
|---------|---------|-------------|
| `autoApplyOutputDevice` | true | Apply saved device on startup |
| `autoApplyVolumes` | true | Apply saved volumes on startup |
| `showDebugLogs` | true | Show detailed FMOD logs |

---

## Singleton Pattern

```csharp
private static FMODAudioInitializer instance;

private void Awake()
{
    // Prevent duplicate initialization
    if (instance != null && instance != this)
    {
        Destroy(gameObject);
        return;
    }

    instance = this;
    DontDestroyOnLoad(gameObject);

    InitializeFMODAudio();
}
```

---

## Initialization Flow

```csharp
private void InitializeFMODAudio()
{
    // 1. Check FMOD availability
    if (!FMODAudioDeviceManager.IsFMODAvailable())
    {
        LogWarning("FMOD not available");
        return;
    }

    // 2. Apply saved output device
    if (autoApplyOutputDevice)
        ApplyOutputDevice();

    // 3. Apply saved volume settings
    if (autoApplyVolumes)
        ApplyVolumeSettings();
}
```

---

## Volume Bus Mapping

Applies volumes to FMOD mixer buses:

| Bus Path | Setting Key | Default |
|----------|-------------|---------|
| `bus:/` | Master | 1.0 |
| `bus:/Music` | Music | 1.0 |
| `bus:/SFX` | SFX | 1.0 |
| `bus:/UI` | UI | 1.0 |

```csharp
#if FMOD_INSTALLED
private void ApplyVolumeSettings()
{
    // Master bus
    FMOD.Studio.Bus masterBus = FMODUnity.RuntimeManager.GetBus("bus:/");
    if (masterBus.isValid())
    {
        float masterVolume = FMODAudioSettings.LoadMasterVolume();
        masterBus.setVolume(masterVolume);
    }

    // Music bus
    FMOD.Studio.Bus musicBus = FMODUnity.RuntimeManager.GetBus("bus:/Music");
    if (musicBus.isValid())
    {
        float musicVolume = FMODAudioSettings.LoadMusicVolume();
        musicBus.setVolume(musicVolume);
    }

    // SFX and UI buses...
}
#endif
```

---

## Public Methods

### Device Refresh
```csharp
// Call when device is plugged/unplugged
public void RefreshOutputDevice()
```

### Volume Refresh
```csharp
// Call after user changes volumes
public void RefreshVolumeSettings()
```

---

## Error Handling

All operations wrapped in try-catch:

```csharp
private void ApplyOutputDevice()
{
    try
    {
        FMODAudioDeviceManager.ApplySavedOutputDevice();
    }
    catch (System.Exception ex)
    {
        DebugManager.LogError(DebugCategory.Audio,
            $"Failed to apply output device: {ex.Message}", this);
    }
}
```

---

## Usage

### Scene Setup
1. Create empty GameObject in MainMenu scene
2. Add `FMODAudioInitializer` component
3. Configure settings in Inspector
4. GameObject persists across scenes

### Runtime Refresh
```csharp
// After user changes settings
FMODAudioInitializer.Instance.RefreshVolumeSettings();

// After device hot-plug event
FMODAudioInitializer.Instance.RefreshOutputDevice();
```

---

## Integration Points

### Dependencies
- `FMODAudioDeviceManager` - Device management
- `FMODAudioSettings` - Preference storage
- `FMODUnity.RuntimeManager` - FMOD Studio integration
- `WOS.Debugging.DebugManager` - Logging

### Used By
- Options menu (refresh after changes)
- Hot-plug event handlers

---

## Conditional Compilation

Volume application uses conditional:

```csharp
#if FMOD_INSTALLED
    // FMOD Studio Bus access
    FMOD.Studio.Bus masterBus = FMODUnity.RuntimeManager.GetBus("bus:/");
    masterBus.setVolume(volume);
#endif
```

---

## Design Notes

### First Scene Requirement
- Must be in first loaded scene (MainMenu)
- `DontDestroyOnLoad` keeps it alive
- Singleton prevents duplicates

### FMOD Availability
- Gracefully handles missing FMOD
- Logs warning but doesn't crash
- Game runs with default audio

### Bus Hierarchy
- FMOD uses hierarchical bus structure
- Master (`bus:/`) affects all audio
- Child buses (Music, SFX, UI) are independent
- All validated before setting volume
