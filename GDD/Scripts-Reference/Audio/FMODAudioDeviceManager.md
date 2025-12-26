# FMODAudioDeviceManager.cs

## Quick Reference
| Property | Value |
|----------|-------|
| **File** | `Assets/Scripts/Audio/FMODAudioDeviceManager.cs` |
| **Namespace** | `WOS.Audio` |
| **Type** | Static class |
| **Lines** | ~312 |
| **Architecture** | Cross-platform FMOD output device management |

## Purpose
FMOD-based audio device manager providing output device enumeration and runtime switching. Replaces Windows-specific implementation with cross-platform FMOD solution. Requires FMOD for Unity plugin.

---

## AudioDevice Class

```csharp
public class AudioDevice
{
    public int DriverIndex { get; set; }   // FMOD driver index
    public string Name { get; set; }        // Display name
    public Guid Guid { get; set; }          // Device GUID
    public int SystemRate { get; set; }     // Sample rate (Hz)
    public bool IsDefault { get; set; }     // Is current driver
}
```

---

## Public API

### Device Enumeration
```csharp
// Get all available output devices
public static List<AudioDevice> GetOutputDevices()

// Get current output device index
public static int GetCurrentOutputDevice()
```

### Device Selection
```csharp
// Set output device by driver index (runtime switching!)
public static bool SetOutputDevice(int driverIndex)

// Apply saved preference on startup
public static void ApplySavedOutputDevice()
```

### Availability Check
```csharp
// Check if FMOD is available
public static bool IsFMODAvailable()
```

---

## Device Enumeration Flow

```csharp
public static List<AudioDevice> GetOutputDevices()
{
    // 1. Initialize FMOD Core System
    if (!InitializeFMODSystem()) return fallback;

    // 2. Get driver count
    coreSystem.getNumDrivers(out numDrivers);

    // 3. Get current driver (for IsDefault marking)
    coreSystem.getDriver(out currentDriver);

    // 4. Enumerate all drivers
    for (int i = 0; i < numDrivers; i++)
    {
        coreSystem.getDriverInfo(i, out name, 256, out guid,
                                  out systemRate, out speakerMode,
                                  out speakerModeChannels);
        devices.Add(new AudioDevice { ... });
    }

    // 5. Sort: default first, then alphabetically
    devices.Sort(...);

    return devices;
}
```

---

## Runtime Device Switching

**Key Feature**: FMOD allows runtime device switching without restart!

```csharp
public static bool SetOutputDevice(int driverIndex)
{
    // Validate driver index
    coreSystem.getNumDrivers(out numDrivers);
    if (driverIndex < 0 || driverIndex >= numDrivers)
        return false;

    // Set the output driver (takes effect immediately!)
    RESULT result = coreSystem.setDriver(driverIndex);

    if (result == RESULT.OK)
    {
        // Save preference
        FMODAudioSettings.SaveOutputDevice(driverIndex);
        return true;
    }
    return false;
}
```

---

## Conditional Compilation

Uses `FMOD_INSTALLED` preprocessor define:

```csharp
#if FMOD_INSTALLED
    // Full FMOD implementation
    private static FMOD.System coreSystem;

    public static List<AudioDevice> GetOutputDevices()
    {
        // Full enumeration via FMOD Core System
    }
#else
    // Fallback when FMOD not installed
    public static List<AudioDevice> GetOutputDevices()
    {
        return new List<AudioDevice>
        {
            new AudioDevice {
                DriverIndex = 0,
                Name = "Default (Install FMOD for device selection)",
                IsDefault = true
            }
        };
    }
#endif
```

---

## Error Handling

All operations have comprehensive error handling:

| Error | Handling |
|-------|----------|
| FMOD not initialized | Return fallback device list |
| Invalid driver index | Log error, return false |
| Driver enumeration fails | Return single "Default" device |
| GetDriverInfo fails | Skip device, log warning |

---

## Usage Example

```csharp
// Check FMOD availability
if (FMODAudioDeviceManager.IsFMODAvailable())
{
    // Get available devices
    var devices = FMODAudioDeviceManager.GetOutputDevices();

    // Populate dropdown
    foreach (var device in devices)
    {
        dropdown.options.Add(new TMP_Dropdown.OptionData(device.ToString()));
    }

    // Set selected device
    int selected = dropdown.value;
    FMODAudioDeviceManager.SetOutputDevice(devices[selected].DriverIndex);
}

// On startup
FMODAudioDeviceManager.ApplySavedOutputDevice();
```

---

## Integration Points

### Dependencies
- `FMOD` - Core audio system
- `FMODUnity.RuntimeManager` - FMOD Unity integration
- `FMODAudioSettings` - Preference persistence
- `WOS.Debugging.DebugManager` - Logging

### Used By
- `FMODAudioInitializer` - Startup initialization
- Options menu UI - Device selection dropdown

---

## Design Notes

### Runtime Switching
- Unlike Unity's AudioListener, FMOD allows hot-swapping
- No game restart required
- Takes effect immediately

### Cross-Platform
- Works on all FMOD-supported platforms
- Fallback implementation when FMOD not installed
- Graceful degradation

### Device Sorting
- Default device always first
- Remaining devices sorted alphabetically
- Consistent UI presentation
